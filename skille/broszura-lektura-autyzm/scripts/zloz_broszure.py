#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Składa broszurę-adaptację lektury z pliku JSON do jednego pliku HTML.

    python zloz_broszure.py dane.json --out broszura.html
    python zloz_broszure.py dane.json --out broszura.html --fragment artifact.html

Numeracja stron jest wyliczana z faktycznej kolejności sekcji, więc numery w spisie
treści nie rozjadą się po dopisaniu rozdziału.
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from broszura import svg as S
from broszura.style import CSS, css as css_skala
from broszura.uklad import Broszura

KROJE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "kroje.css")


def kroje():
    """Arkusz z osadzonymi krojami.

    Kroje MUSZĄ być w pliku, a nie pod adresem Google Fonts: PDF powstaje
    w przeglądarce bez dostępu do sieci, więc zdalne kroje podmieniają się na
    zastępniki i cały tekst wygląda na zbyt gruby. Odśwież je przez
    `python scripts/pobierz_kroje.py --out assets/kroje.css`.
    """
    if os.path.exists(KROJE):
        return "<style>" + open(KROJE, encoding="utf-8").read() + "</style>"
    sys.stderr.write("UWAGA: brak assets/kroje.css — druk wyjdzie zastępczymi krojami.\n")
    return ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,600;0,700;1,600'
            '&family=Lato:ital,wght@0,400;0,700;1,400&display=swap&subset=latin,latin-ext" rel="stylesheet">')


def nawigacja(b):
    return ('<div class="topbar">'
            f'<b>{b.tytul_biezacy} — {b.meta.get("haslo","")}</b><nav>'
            '<a href="#spis">Spis</a><a href="#jak-korzystac">Jak korzystać</a>'
            '<a href="#narzedzia">Narzędzia</a><a href="#postacie">Postacie</a>'
            '<a href="#r1">Rozdziały</a><a href="#cwiczenia">Ćwiczenia</a>'
            '<a href="#gra">Gra</a><a href="#scenariusz">Przedstawienie</a></nav></div>')


SEKCJA = r'<section class="page[^"]*"[^>]*>.*?</section>'


def zloz(dane, linie=None, katalog_grafik=None):
    b = Broszura(dane, linie=linie, katalog_grafik=katalog_grafik)
    czesci = [nawigacja(b), S.logo_symbol(), b.okladka(), b.metryczka_wydawcy(), b.licencja(), b.spis(), b.jak_korzystac(),
              b.narzedzia(), b.postacie()]
    czesci += [b.rozdzial(r) for r in b.R]
    czesci += [b.cwiczenia(), b.gra(), b.scenariusz(), b.zalaczniki(), b.seria(), b.zakonczenie()]
    # Style obrazów dopisujemy po złożeniu sekcji — dopiero wtedy wiadomo,
    # które pliki są w użyciu.
    core = "\n".join(x for x in czesci if x)
    core = b.znak_wodny_css() + b.logo_css() + b.style_obrazow() + core

    # stopka na stronach, które nie mają własnej (rozdziały mają)
    def dodaj_stopke(m):
        t = m.group(0)
        if "r-foot" in t or 'class="page okladka"' in t:
            return t
        return t[:-len("</section>")] + b.stopka_ogolna() + "</section>"

    core = re.sub(SEKCJA, dodaj_stopke, core, flags=re.S)

    # ciągła numeracja: n-ta sekcja = n-ta strona A4 (okładka liczona, bez nadruku)
    licznik, mapa = {"n": 0}, {}

    def numeruj(m):
        t = m.group(0)
        licznik["n"] += 1
        ident = re.search(r'id="([^"]+)"', t)
        if ident:
            mapa[ident.group(1)] = licznik["n"]
        return t.replace('<span class="f-nr"></span>', f'<span class="f-nr">{licznik["n"]}</span>')

    core = re.sub(SEKCJA, numeruj, core, flags=re.S)
    core = re.sub(r"\{\{STR:([^}]+)\}\}", lambda m: str(mapa.get(m.group(1), "—")), core)
    if "{{STR:" in core:
        raise SystemExit("BŁĄD: nierozwiązany numer strony w spisie treści")
    return b, core, licznik["n"]


def main():
    ap = argparse.ArgumentParser(description="Skład broszury-adaptacji lektury")
    ap.add_argument("dane", help="plik JSON z treścią lektury")
    ap.add_argument("--out", required=True, help="wyjściowy plik HTML")
    ap.add_argument("--fragment", help="dodatkowo wersja bez <html>/<head> (do publikacji jako Artifact)")
    ap.add_argument("--linie", help="JSON z liczbą linii na notatki: {\"1\": 12, ...}")
    ap.add_argument("--grafiki", help="katalog ze zdjęciami, do którego odnoszą się ścieżki w JSON")
    ap.add_argument("--skala", type=float, default=1.0,
                    help="powiększenie stopnia pisma, np. 1.15 dla druku powiększonego")
    a = ap.parse_args()

    dane = json.load(open(a.dane, encoding="utf-8"))
    linie = json.load(open(a.linie, encoding="utf-8")) if a.linie and os.path.exists(a.linie) else {}
    b, core, stron = zloz(dane, linie, a.grafiki or os.path.dirname(os.path.abspath(a.dane)))

    tytul = b.tytul_biezacy
    opis = (f'Broszura edukacyjna: adaptacja lektury „{b.meta["tytul"]}” dla młodzieży ze spektrum autyzmu. '
            f'{len(b.R)} rozdziałów, słowniki pojęć, emocje, wnioskowanie, ocena sytuacji, '
            'teoria umysłu w 5 etapach, ćwiczenia, gra planszowa i scenariusz przedstawienia.')

    html_full = (f'<!doctype html>\n<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
                 f'<meta name="viewport" content="width=device-width, initial-scale=1">\n'
                 f'<title>{tytul} — {b.meta.get("haslo","")}</title>\n'
                 f'<meta name="description" content="{opis}">\n{kroje()}\n'
                 f'<style>{css_skala(a.skala)}</style>\n</head>\n<body>\n{core}\n</body>\n</html>')
    open(a.out, "w", encoding="utf-8").write(html_full)
    print(f"Zapisano {a.out} — {stron} sekcji = {stron} stron A4, {len(html_full)//1024} KB")

    if a.fragment:
        frag = f"<title>{tytul}</title>\n{kroje()}\n<style>{css_skala(a.skala)}</style>\n{core}"
        open(a.fragment, "w", encoding="utf-8").write(frag)
        print(f"Zapisano {a.fragment} (wersja do publikacji jako Artifact)")


if __name__ == "__main__":
    main()
