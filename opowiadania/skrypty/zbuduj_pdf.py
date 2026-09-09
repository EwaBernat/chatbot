#!/usr/bin/env python3
"""Buduje wersję do druku (HTML -> PDF) z pliku rajmund-i-arystoteles.md.

Uruchomienie:
    python3 opowiadania/skrypty/zbuduj_pdf.py            # obie czesci
    python3 opowiadania/skrypty/zbuduj_pdf.py 2          # tylko czesc druga
Wymaga: chromium (headless) do wydruku PDF.
"""
import html
import re
import subprocess
import sys
from pathlib import Path

KATALOG = Path(__file__).resolve().parent.parent
CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

KSIAZKI = {
    "1": {
        "zrodlo": "rajmund-i-arystoteles.md",
        "html": "rajmund-i-arystoteles.html",
        "pdf": "Rajmund-i-Arystoteles-do-druku.pdf",
        "tytul": "Rajmund<br>i Arystoteles",
        "podtytul": ("Opowiadanie o życiu i hasłach Arystotelesa.<br>"
                     "O tym, jak używać ich w zwykłym dniu.<br>"
                     "I o pytaniach, na które nikt nie zna odpowiedzi."),
        "okladka": "obrazy/01-okladka.jpg",
        "ile_rozdzialow": "trzydzieści siedem",
        "ilustracje": {
            2: ("obrazy/02-strych.jpg", "Strych, deszcz za oknem i stara księga bez okładki."),
            8: ("obrazy/03-likejon.jpg", "Likejon. Perypatetycy myśleli, spacerując pod kolumnami."),
            11: ("obrazy/04-zoladz.jpg", "Żołądź to dąb w możności. Dąb to żołądź w akcie."),
            22: ("obrazy/05-waga.jpg", "Złoty środek. Dobra cecha leży między za dużo i za mało."),
            36: ("obrazy/06-szpital.jpg", "Rajmund przyniósł babci rysunek dębu."),
        },
    },
    "2": {
        "zrodlo": "rajmund-i-arystoteles-czesc-2.md",
        "html": "rajmund-i-arystoteles-czesc-2.html",
        "pdf": "Rajmund-i-Arystoteles-czesc-2-do-druku.pdf",
        "tytul": "Rajmund<br>i Arystoteles<br><span class=\"czesc\">część druga</span>",
        "podtytul": ("W czym może mi pomóc filozofia?<br>"
                     "O pamięci, o pytaniach, o hałasie i o dotyku.<br>"
                     "O emocjach i o ludziach, którzy mówią jedno, a robią drugie."),
        "okladka": "obrazy/07-okladka-2.jpg",
        "ile_rozdzialow": "trzydzieści jeden",
        "ilustracje": {
            1: ("obrazy/08-dab-okno.jpg", "Dąb rośnie powoli. Ale rośnie."),
            4: ("obrazy/09-wosk.jpg", "Pamięć to ślad, jak odcisk pieczęci w wosku."),
            19: ("obrazy/10-uscisk.jpg", "Przytul mnie mocniej, wtedy to czuję."),
            30: ("obrazy/11-lawka.jpg", "Ławka o zmierzchu. Zeszyt został otwarty."),
        },
    },
}

STYL = """
@page { size: A4; margin: 20mm 22mm 18mm 22mm; }
@page :first { margin: 0; }
* { box-sizing: border-box; }
body {
  font-family: "DejaVu Sans", Arial, Helvetica, sans-serif;
  font-size: 12.5pt; line-height: 1.75; color: #1c1c1c; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
p { margin: 0 0 0.85em 0; text-align: left; hyphens: none; }
strong { font-weight: 700; }
em { font-style: italic; }

/* --- okładka --- */
.okladka { height: 297mm; display: flex; flex-direction: column; page-break-after: always; }
.okladka img { width: 100%; height: 148mm; object-fit: cover; display: block; }
.okladka-tekst { padding: 18mm 22mm 0 22mm; }
.okladka h1 { font-size: 34pt; line-height: 1.15; margin: 0 0 6mm 0; color: #3E4E2C; }
.okladka .podtytul { font-size: 14pt; color: #7A4A22; margin: 0 0 12mm 0; line-height: 1.5; }
.okladka h1 .czesc { font-size: 20pt; color: #7A4A22; font-weight: 400; }
.okladka .dla { font-size: 13pt; color: #444; }

/* --- strony --- */
.strona { page-break-before: always; }
h2.rozdzial { font-size: 17pt; color: #3E4E2C; margin: 0 0 6mm 0; line-height: 1.3;
  padding-bottom: 3mm; border-bottom: 2px solid #D8CDB6; }
h2.rozdzial .nr { display: inline-block; min-width: 11mm; padding-right: 2mm; color: #B5651D; font-weight: 700; }
h1.dzial { font-size: 24pt; color: #3E4E2C; margin: 0 0 8mm 0; }
h3 { font-size: 14pt; color: #7A4A22; margin: 8mm 0 4mm 0; }

figure { margin: 0 0 7mm 0; page-break-inside: avoid; }
figure img { width: 100%; border-radius: 3mm; display: block; }
figcaption { font-size: 10.5pt; color: #5c5c5c; font-style: italic; margin-top: 2mm; }

.ramka { background: #F7F1E6; border-left: 5px solid #B5651D; border-radius: 2mm;
  padding: 5mm 6mm; margin: 0 0 7mm 0; page-break-inside: avoid; }
.ramka p:last-child { margin-bottom: 0; }

ul.spis { list-style: none; padding: 0; margin: 0; column-count: 2; column-gap: 10mm; }
ul.spis li { font-size: 11pt; line-height: 1.55; margin-bottom: 1.5mm; break-inside: avoid; }
ul.spis li .nr { color: #B5651D; font-weight: 700; display: inline-block; min-width: 8mm; }

dl.slownik dt { font-weight: 700; color: #3E4E2C; margin-top: 4mm; }
dl.slownik dd { margin: 0.5mm 0 0 0; }
dl.slownik div { page-break-inside: avoid; }

ol.pytania { padding-left: 9mm; margin: 0 0 6mm 0; }
ol.pytania li { margin-bottom: 3.5mm; page-break-inside: avoid; }

ul.zwykla { padding-left: 6mm; }
ul.zwykla li { margin-bottom: 2.5mm; }

.stopka { margin-top: 10mm; font-size: 10.5pt; color: #5c5c5c; font-style: italic;
  border-top: 1px solid #D8CDB6; padding-top: 4mm; }
"""


def cudzyslowy(t: str) -> str:
    """Zamienia proste cudzyslowy na polskie: "tak" -> „tak"."""
    t = re.sub(r'"([^"]*)"', lambda m: "\u201e" + m.group(1) + "\u201d", t)
    return t.replace(" - ", " \u2013 ")           # myslnik dialogowy


def inline(t: str) -> str:
    t = html.escape(cudzyslowy(t))
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<em>\1</em>", t)
    return t


def akapity(blok: str) -> str:
    out = []
    for kawalek in [k.strip() for k in blok.split("\n\n") if k.strip()]:
        linie = [l.strip() for l in kawalek.split("\n") if l.strip()]
        if all(l.startswith("- ") for l in linie):
            punkty = "".join(f"<li>{inline(l[2:])}</li>" for l in linie)
            out.append(f'<ul class="zwykla">{punkty}</ul>')
        elif all(re.match(r"^\d+\.\s", l) for l in linie):
            wzor = re.compile(r"^(\d+)\.\s")
            start = wzor.match(linie[0]).group(1)
            punkty = "".join("<li>%s</li>" % inline(wzor.sub("", l)) for l in linie)
            out.append(f'<ol class="pytania" start="{start}">{punkty}</ol>')
        else:
            out.append(f"<p>{inline(' '.join(linie))}</p>")
    return "\n".join(out)


def zbuduj_html(md: str, cfg: dict) -> str:
    tresc = md.split("---", 1)[1] if md.startswith("# ") else md
    opowiadanie, reszta = tresc.split("\n# Słowniczek nowych pojęć", 1)
    slownik_md, pytania_md = reszta.split("\n# 45 pytań", 1)

    czesci = re.split(r"\n## ", opowiadanie)
    rozdzialy = []
    for kawalek in czesci[1:]:
        naglowek, tekst = kawalek.split("\n", 1)
        if not re.match(r"^\d+\.\s", naglowek):
            continue                      # np. podtytul ksiazki, nie rozdzial
        nr, tytul = naglowek.split(". ", 1)
        rozdzialy.append((int(nr), tytul.strip(), tekst.split("\n---")[0]))

    czesci_html = []

    # okładka
    czesci_html.append(
        '<section class="okladka">'
        f'<img src="{cfg["okladka"]}" alt="">'
        '<div class="okladka-tekst">'
        f'<h1>{cfg["tytul"]}</h1>'
        f'<p class="podtytul">{cfg["podtytul"]}</p>' 
        '<p class="dla">Dla Maksymiliana</p>'
        "</div></section>"
    )

    # jak korzystać + spis treści
    spis = "".join(
        f'<li><span class="nr">{nr}.</span>{html.escape(tytul)}</li>' for nr, tytul, _ in rozdzialy
    )
    czesci_html.append(
        '<section class="strona">'
        '<h1 class="dzial">Jak czytać tę książeczkę</h1>'
        '<div class="ramka">'
        "<p>Tekst jest napisany prostym językiem. Zdania są krótkie. "
        "Jedno zdanie mówi jedną rzecz.</p>"
        "<p>Każde trudne słowo jest wyjaśnione zaraz po tym, jak się pojawi. "
        "Wszystkie trudne słowa są jeszcze raz zebrane w słowniczku na końcu.</p>"
        f"<p>Rozdziałów jest {cfg['ile_rozdzialow']}. Każdy zaczyna się na nowej stronie. "
        "Można czytać po jednym rozdziale dziennie. Nie trzeba czytać wszystkiego naraz.</p>"
        "<p>Na końcu jest 45 pytań. Pytania są w czterech grupach. "
        "Grupa mówi, jakiej odpowiedzi można się spodziewać. "
        "W grupie D są pytania, na które nikt nie zna odpowiedzi. To nie jest błąd.</p>"
        "</div>"
        '<h1 class="dzial">Spis rozdziałów</h1>'
        f'<ul class="spis">{spis}</ul>'
        "</section>"
    )

    # rozdziały
    for nr, tytul, tekst in rozdzialy:
        obraz = ""
        if nr in cfg["ilustracje"]:
            plik, podpis = cfg["ilustracje"][nr]
            obraz = f'<figure><img src="{plik}" alt=""><figcaption>{html.escape(podpis)}</figcaption></figure>'
        czesci_html.append(
            '<section class="strona">'
            f'<h2 class="rozdzial"><span class="nr">{nr}.</span>{html.escape(tytul)}</h2>'
            f"{obraz}{akapity(tekst)}"
            "</section>"
        )

    # słowniczek
    wpisy = []
    for linia in [l.strip() for l in slownik_md.split("\n") if l.strip().startswith("**")]:
        m = re.match(r"\*\*(.+?)\*\*\s*(?:—|-)\s*(.+)", linia)
        if m:
            wpisy.append(f"<div><dt>{inline(m.group(1))}</dt><dd>{inline(m.group(2))}</dd></div>")
    wstep = slownik_md.strip().split("\n")[0]
    czesci_html.append(
        '<section class="strona">'
        '<h1 class="dzial">Słowniczek nowych pojęć</h1>'
        f"<p>{inline(wstep)}</p>"
        f'<dl class="slownik">{"".join(wpisy)}</dl>'
        "</section>"
    )

    # pytania
    bloki = re.split(r"\n## ", pytania_md)
    wstep_pyt = bloki[0].split("\n---")[0].strip()
    grupy_html = []
    for blok in bloki[1:]:
        naglowek, tekst = blok.split("\n", 1)
        tekst = tekst.split("\n---")[0]
        grupy_html.append(f"<h3>{html.escape(naglowek.strip())}</h3>{akapity(tekst)}")
    czesci_html.append(
        '<section class="strona">'
        '<h1 class="dzial">45 pytań</h1>'
        f'<div class="ramka">{akapity(wstep_pyt)}</div>'
        f'{"".join(grupy_html)}'
        "</section>"
    )

    return (
        "<!doctype html><html lang=\"pl\"><head><meta charset=\"utf-8\">"
        "<title>Rajmund i Arystoteles</title>"
        f"<style>{STYL}</style></head><body>{''.join(czesci_html)}</body></html>"
    )


def ponumeruj(pdf: Path) -> None:
    """Dopisuje numery stron na dole (bez okladki). Pomija, gdy brak pymupdf."""
    try:
        import pymupdf
    except ImportError:
        print("(pymupdf niedostepny - PDF bez numeracji stron)")
        return
    dok = pymupdf.open(pdf)
    for i, strona in enumerate(dok):
        if i == 0:
            continue
        tekst = str(i)
        szer = strona.rect.width
        strona.insert_text(
            pymupdf.Point(szer / 2 - 4 * len(tekst), strona.rect.height - 32),
            tekst, fontname="helv", fontsize=10, color=(0.42, 0.42, 0.42),
        )
    dok.save(pdf.with_suffix(".tmp.pdf"))
    dok.close()
    pdf.with_suffix(".tmp.pdf").replace(pdf)


def main() -> int:
    wybor = sys.argv[1] if len(sys.argv) > 1 else "wszystkie"
    klucze = list(KSIAZKI) if wybor == "wszystkie" else [wybor]
    for klucz in klucze:
        cfg = KSIAZKI.get(klucz)
        if cfg is None:
            print(f"Nie znam czesci '{klucz}'. Dostepne: {', '.join(KSIAZKI)} albo 'wszystkie'.")
            return 2
        zrodlo = KATALOG / cfg["zrodlo"]
        html_out = KATALOG / cfg["html"]
        pdf_out = KATALOG / cfg["pdf"]
        html_out.write_text(zbuduj_html(zrodlo.read_text(encoding="utf-8"), cfg), encoding="utf-8")
        print(f"HTML: {html_out}")
        wynik = subprocess.run(
            [CHROMIUM, "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", "--run-all-compositor-stages-before-draw",
             f"--print-to-pdf={pdf_out}", html_out.as_uri()],
            capture_output=True, text=True,
        )
        if not pdf_out.exists():
            print(wynik.stderr[-2000:], file=sys.stderr)
            return 1
        ponumeruj(pdf_out)
        print(f"PDF: {pdf_out} ({pdf_out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
