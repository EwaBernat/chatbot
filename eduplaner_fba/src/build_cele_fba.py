# -*- coding: utf-8 -*-
"""Druk FBA-C — cele SMART do obserwacji pogłębionej po analizie funkcjonalnej.

Składa jeden plik HTML otwierany z dysku, bez serwera: siedem stron A4 pionowo,
25 celów SMART — po jednym do każdego wskaźnika z kwestionariusza funkcji
zachowania (ABC / FBA). Dokument jest ciągiem dalszym karty FBA, nie jej
powtórzeniem: tam pięć celów wyznacza kierunek planu PBS, tu każdy z nich jest
rozpisany na pięć obserwowalnych, policzalnych zachowań.

Kryterium prób i horyzont **wynikają z punktacji funkcji u konkretnego ucznia**
(patrz `dane_fba.PROGI`), więc dokument składa się pod jego profil:

    python3 src/build_cele_fba.py --uczen "Imię Nazwisko" --klasa "III A" \
        --wyniki 7,8,13,7,13

Bez `--uczen` powstaje pusty formularz do wypełnienia ręcznie; bez `--wyniki`
wszystkie funkcje liczą się jako istotne (7 z 10 · 8 tygodni).

Dokument nie zawiera żadnych danych o zdarzeniach ani rozpoznaniu — tylko imię,
klasę i punktację przepisaną z kwestionariusza.
"""

import argparse
import html
from datetime import date
from pathlib import Path

import dane_fba as D

KOR = Path(__file__).resolve().parent.parent
STRON = 8


# ——— wygląd ——————————————————————————————————————————————————————————————
# Paleta rodzinna z bankiem celów SMART (`eduplaner_przedszkole/src/build.py`):
# ten sam fiolet i ta sama pomarańcz akcentu, żeby druki PCTP wyglądały jak
# jeden komplet. Arkusz fontów ładujemy nieblokująco — przy niedostępnym CDN
# przeglądarka trzymała biały ekran kilkanaście sekund.
STYL = """
:root{
  --ink:#2D1B69; --indigo:#4F3AA8; --violet:#6C4CC4; --accent:#E8450A;
  --on-accent:#FFFFFF; --tekst:#241C3A; --szary:#5B5470;
  --paper:#FFFFFF; --soft:#F6F3FC; --field:#EFEAF9;
  --line:#DCD4F0; --line-2:#C9BEEA; --tlo:#EDE9F6;
}
*{box-sizing:border-box}
body{margin:0; background:var(--tlo); color:var(--tekst);
  font:13px/1.5 "DM Sans",Arial,Helvetica,sans-serif; padding:26px 0}
.strona{width:726px; min-height:1054px; margin:0 auto 26px; background:var(--paper);
  padding:0; display:flex; flex-direction:column; box-shadow:0 2px 14px rgba(45,27,105,.13)}
.tresc{flex:1 1 auto; padding:0 4px}

/* nagłówek i stopka — układ przepisany z karty ABC/FBA */
.head{display:flex; align-items:flex-start; gap:12px; border-bottom:2px solid var(--line-2);
  padding:12px 4px 9px; margin-bottom:10px}
.mark{flex:0 0 auto; width:34px; height:34px; border-radius:7px; background:var(--ink);
  color:#fff; font:700 10px/34px "DM Sans",Arial,sans-serif; text-align:center; letter-spacing:.06em}
.head h1{margin:0; font-size:14px; font-weight:700; color:var(--ink); letter-spacing:.01em}
.head .sub{font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--szary); margin-top:3px}
.head .prawa{margin-left:auto; text-align:right}
.head .prawa b{display:block; font-size:10px; letter-spacing:.1em; color:var(--accent); text-transform:uppercase}
.head .prawa span{font-size:8.5px; letter-spacing:.18em; text-transform:uppercase; color:var(--szary)}
.metryka{display:flex; gap:10px; align-items:stretch; margin:0 4px 11px; font-size:10px}
.metryka div{flex:1 1 auto; border-bottom:1px solid var(--line-2); padding:4px 2px 5px;
  display:flex; gap:8px; align-items:baseline}
.metryka span{font-size:8.5px; letter-spacing:.13em; text-transform:uppercase; color:var(--szary); white-space:nowrap}
.metryka b{font-size:12px; color:var(--ink); font-weight:700}
.stopka{margin-top:auto; border-top:1px solid var(--line); padding:8px 4px 12px;
  display:flex; justify-content:space-between; font-size:8.5px; color:var(--szary); letter-spacing:.04em}

/* wspólne elementy treści */
.pas{background:var(--ink); color:#fff; border-radius:7px; padding:9px 14px; margin:0 0 12px;
  font-size:10px; letter-spacing:.16em; text-transform:uppercase; text-align:center}
h2{margin:0 0 8px; font-size:15px; color:var(--ink)}
p{margin:0 0 9px}
.wstep{background:var(--soft); border-left:4px solid var(--violet); border-radius:0 8px 8px 0;
  padding:11px 14px; font-size:11.5px; line-height:1.6; margin-bottom:12px}
.wstep b{color:var(--ink)}
.dwie{display:grid; grid-template-columns:1fr 1fr; gap:11px; margin-bottom:12px}
.karta-info{border:1px solid var(--line); border-radius:9px; padding:11px 13px; font-size:11px; line-height:1.55}
.karta-info h3{margin:0 0 6px; font-size:11.5px; color:var(--accent);
  letter-spacing:.06em; text-transform:uppercase}
table{width:100%; border-collapse:collapse; font-size:11px}
th{background:var(--field); color:var(--ink); text-align:left; font-size:9px; letter-spacing:.1em;
  text-transform:uppercase; padding:7px 8px; border:1px solid var(--line)}
td{padding:6px 8px; border:1px solid var(--line); vertical-align:top}
tbody tr:nth-child(even) td{background:var(--soft)}
.pkt{font-weight:700; color:var(--ink); text-align:center; white-space:nowrap}
.ocena{font-weight:700; white-space:nowrap}
.ocena.dom{color:var(--accent)}
.pole{border-bottom:1px dotted var(--line-2); min-width:54px; display:inline-block}

/* nagłówek funkcji */
.fn{display:flex; align-items:center; gap:11px; margin:0 0 8px}
.fn .rz{flex:0 0 auto; width:32px; height:32px; border-radius:6px; background:var(--accent);
  color:var(--on-accent); font:700 13px/32px "DM Sans",Arial,sans-serif; text-align:center}
.fn h2{margin:0; font-size:15px}
.fn .op{font-size:10px; color:var(--szary); margin-top:2px}
.fn .bad{margin-left:auto; text-align:right; font-size:9.5px; letter-spacing:.08em;
  text-transform:uppercase; color:var(--szary)}
.fn .bad b{display:block; font-size:12px; color:var(--ink); letter-spacing:0; text-transform:none}
.pbs{background:var(--soft); border-radius:8px; padding:7px 11px; font-size:10px;
  line-height:1.45; margin-bottom:7px}
.pbs b{color:var(--accent); letter-spacing:.08em; text-transform:uppercase; font-size:9px}

/* karta jednego celu */
.cel{border:1px solid var(--line); border-radius:9px; padding:5px 10px 6px; margin-bottom:5px;
  break-inside:avoid}
.cel-h{display:flex; align-items:baseline; gap:9px; margin-bottom:4px}
.cel-h .nr{flex:0 0 auto; background:var(--ink); color:#fff; border-radius:4px; padding:2px 7px;
  font:700 9.5px/1.4 "DM Sans",Arial,sans-serif; letter-spacing:.04em}
.cel-h .def{font-size:10px; color:var(--szary); line-height:1.35}
.cel-h .def b{color:var(--ink); font-size:9px; letter-spacing:.1em; text-transform:uppercase}
.cel-t{margin:0 0 5px; font-size:11px; line-height:1.42; color:var(--tekst);
  border-left:3px solid var(--accent); padding-left:9px}
.cel-t b{color:var(--accent); font-size:9px; letter-spacing:.1em; text-transform:uppercase;
  display:block; margin-bottom:1px}
.smart{display:grid; grid-template-columns:repeat(5,1fr); gap:4px; margin-bottom:5px}
.smart div{background:var(--soft); border-radius:5px; padding:4px 5px; font-size:8px; line-height:1.32}
.smart i{display:block; font-style:normal; font-weight:700; color:var(--accent); font-size:9.5px; margin-bottom:1px}
.obs{display:flex; gap:10px; align-items:baseline; font-size:9.2px; color:var(--szary);
  border-top:1px dashed var(--line); padding-top:3px}
.obs b{color:var(--ink); font-size:8.5px; letter-spacing:.09em; text-transform:uppercase}
.obs .wynik{margin-left:auto; white-space:nowrap; color:var(--ink)}

/* podpisy */
.podpisy{display:grid; grid-template-columns:1fr 1fr; gap:36px; margin:20px 4px 12px}
.podpisy div{border-top:1px solid var(--line-2); padding-top:6px; text-align:center;
  font-size:9px; letter-spacing:.12em; text-transform:uppercase; color:var(--szary)}
.podstawa{border:1px solid var(--line); border-radius:8px; padding:10px 13px;
  font-size:9px; line-height:1.55; color:var(--szary)}
.podstawa b{color:var(--ink)}

@media print{
  @page{size:A4 portrait; margin:9mm}
  body{background:#fff; padding:0}
  .strona{width:auto; min-height:0; margin:0; box-shadow:none; break-after:page}
  .strona:last-child{break-after:auto}
}
"""


def _e(t):
    return html.escape(str(t), quote=False)


def _naglowek(tytul, nazwa_sekcji):
    return f"""  <div class="head">
    <span class="mark">PCTP</span>
    <div>
      <h1>EduPlaner 2026</h1>
      <div class="sub">ABC / FBA · {_e(tytul)}</div>
    </div>
    <div class="prawa"><b>ABC · PBS</b><span>narzędzie · druk FBA-C</span></div>
  </div>"""


def _metryka(uczen, klasa, data):
    return f"""  <div class="metryka">
    <div><span>Dotyczy ucznia</span><b>{_e(uczen) or '&nbsp;'}</b></div>
    <div><span>Klasa</span><b>{_e(klasa) or '&nbsp;'}</b></div>
    <div><span>Data</span><b>{_e(data) or '&nbsp;'}</b> r.</div>
  </div>"""


def _stopka(nr, opis):
    return (f'  <div class="stopka"><span>EduPlaner 2026 · PCTP · pedagog specjalny '
            f'mgr Mirosława Ewa Jurczyszyn</span>'
            f'<span>Strona {nr} z {STRON} · {_e(opis)}</span></div>')


def strona(nr, tytul, opis, tresc, uczen, klasa, data):
    return (f'<section class="strona">\n{_naglowek(tytul, opis)}\n'
            f'{_metryka(uczen, klasa, data)}\n  <div class="tresc">\n{tresc}\n  </div>\n'
            f'{_stopka(nr, opis)}\n</section>')


# ——— strona 1: wprowadzenie i profil ————————————————————————————————————
def _profil(wyniki):
    w = []
    for f, pkt in zip(D.FUNKCJE, wyniki):
        nazwa, proba, _dop, _msc, mian, opis = D.ocena(pkt)
        dom = " dom" if nazwa == "Dominująca" else ""
        w.append(f'<tr><td>{f["rzym"]} · {_e(f["nazwa"])}</td><td class="pkt">{pkt}/15</td>'
                 f'<td class="ocena{dom}">{nazwa}</td><td class="pkt">{proba}</td>'
                 f'<td class="pkt">{mian}</td><td>{_e(opis)}</td></tr>')
    return ("<table><thead><tr><th>Funkcja zachowania</th><th>Wynik</th><th>Ocena</th>"
            "<th>Kryterium</th><th>Horyzont</th><th>Znaczenie dla planu</th></tr></thead>"
            f'<tbody>{"".join(w)}</tbody></table>')


def wprowadzenie(wyniki):
    return f"""    <div class="pas">Cele SMART do obserwacji pogłębionej · 25 wskaźników z kwestionariusza funkcji</div>
    <div class="wstep">
      <b>Po co ten druk.</b> Karta ABC / FBA kończy się pięcioma celami SMART — po jednym na funkcję
      zachowania. Wyznaczają kierunek planu PBS, ale są za szerokie na obserwację pogłębioną:
      „skorzysta z ustalonej strategii wyciszenia” nie mówi, w której z pięciu sytuacji napięcia
      liczymy postęp. Ten druk rozpisuje tamte pięć celów na <b>25 celów szczegółowych</b> —
      po jednym do każdego wskaźnika kwestionariusza, każdy z zachowaniem, które widać, liczbą,
      którą da się policzyć, i terminem, w którym sprawdzamy.
    </div>
    <div class="dwie">
      <div class="karta-info">
        <h3>Jak czytać cel</h3>
        Każdy cel opisuje <b>zachowanie zastępcze</b> — takie, które pełni tę samą funkcję,
        co zachowanie trudne, tylko jest akceptowalne. Nie odbieramy dziecku funkcji
        (ucieczki, uwagi, regulacji), uczymy innej drogi do niej. Dlatego pod celem stoi
        rozpisanie SMART: co dokładnie widać (S), ile tego liczymy (M), co to umożliwia (A),
        po co to dziecku (R) i kiedy sprawdzamy (T).
      </div>
      <div class="karta-info">
        <h3>Skąd kryterium i horyzont</h3>
        Nie z podręcznika, tylko z <b>punktacji funkcji u tego ucznia</b>. Funkcja dominująca
        (10–15 pkt) jest priorytetem planu, więc sprawdzamy ją najczęściej — po 4 tygodniach,
        przy kryterium 8 z 10. Funkcja istotna (5–9 pkt) — po 8 tygodniach, przy 7 z 10.
        Funkcja słaba (0–4 pkt) — po 12 tygodniach, przy 6 z 10. Ta sama logika, co przy
        poziomach wsparcia w banku celów SMART.
      </div>
    </div>
    {_profil(wyniki)}
    <div class="dwie" style="margin-top:12px">
      <div class="karta-info">
        <h3>Cel, który da się obserwować</h3>
        <p style="margin-bottom:6px"><b style="color:var(--indigo)">Dobrze:</b> „Uczennica poprosi
        o uwagę dorosłego przez podniesienie ręki, zamiast zachowaniem trudnym, w 8 z 10 sytuacji
        potrzeby kontaktu, w ciągu 4 tygodni.”</p>
        <p style="margin:0"><b style="color:var(--accent)">Źle:</b> „Poprawa umiejętności proszenia
        o uwagę.” — nie widać zachowania, nie ma czego policzyć, więc nie da się zrobić ewaluacji
        ani napisać, czy cel został osiągnięty.</p>
      </div>
      <div class="karta-info">
        <h3>Jak liczyć „8 z 10”</h3>
        Liczymy <b>sytuacje, w których zachowanie mogło wystąpić</b>, nie dni i nie lekcje.
        Dziesięć kolejnych sytuacji z rejestru ABC daje jeden wynik; przy wskaźnikach rzadkich
        (zmiana planu, odmowa) zbiera się to przez dwa–trzy tygodnie i to jest w porządku —
        lepszy wynik z dziesięciu prawdziwych sytuacji niż z dziesięciu wywołanych na próbę.
        Wynik zapisujemy w polu przy celu, w dniu, w którym domknęła się dziesiątka.
      </div>
    </div>
    <div class="wstep">
      <b>Czego ten druk nie zastępuje.</b> Cel wpisujemy do pracy dopiero wtedy, gdy wskaźnik
      został oceniony na 2 albo 3 — przy ocenie 0 lub 1 nie ma czego obserwować. Wybieramy
      zwykle <b>trzy do pięciu celów</b> naraz, zaczynając od funkcji dominującej; 25 celów to
      zapas na cały rok, nie plan na wrzesień. Wynik obserwacji wpisujemy w pole przy celu,
      a zbiorczo — w tabelę ewaluacji na ostatniej stronie.
    </div>"""


# ——— strony 2–6: karty celów ————————————————————————————————————————————
def karta_celu(rzym, lp, wsk, slowa):
    smart = "".join(f'<div><i>{lit}</i>{_e(txt.format(**slowa))}</div>'
                    for lit, txt in wsk["smart"])
    cel = _e(wsk["cel"].format(**slowa))
    return f"""    <article class="cel">
      <div class="cel-h">
        <span class="nr">{rzym}.{lp}</span>
        <span class="def"><b>Deficyt</b> {_e(wsk["deficyt"])}</span>
      </div>
      <p class="cel-t"><b>Cel SMART</b>{cel}</p>
      <div class="smart">{smart}</div>
      <div class="obs">
        <span><b>Obserwacja</b> {_e(wsk["obs"])} · {_e(wsk["ile"])}</span>
        <span class="wynik">wynik <span class="pole">&nbsp;</span>/10 · data <span class="pole">&nbsp;</span></span>
      </div>
    </article>"""


def strona_funkcji(f, pkt):
    nazwa, proba, dop, msc, mian, _ = D.ocena(pkt)
    slowa = dict(proba=proba, horyzont=dop, po=msc)
    dom = " dom" if nazwa == "Dominująca" else ""
    karty = "\n".join(karta_celu(f["rzym"], i, w, slowa)
                      for i, w in enumerate(f["wskazniki"], 1))
    return f"""    <div class="fn">
      <span class="rz">{f["rzym"]}</span>
      <div><h2>{_e(f["nazwa"])}</h2><div class="op">{_e(f["opis"])}</div></div>
      <div class="bad">{pkt}/15 · <span class="ocena{dom}">{nazwa}</span>
        <b>{proba} sytuacji · {mian}</b></div>
    </div>
    <div class="pbs"><b>Zalecenia PBS</b> {_e(f["pbs"])}</div>
{karty}"""


# ——— strona 7: tabela ewaluacji ————————————————————————————————————————
def ewaluacja(wyniki, funkcje):
    w = []
    for f, pkt in ((f, wyniki[D.FUNKCJE.index(f)]) for f in funkcje):
        _n, proba, dop, msc, mian, _o = D.ocena(pkt)
        for i, wsk in enumerate(f["wskazniki"], 1):
            skrot = wsk["cel"].format(proba=proba, horyzont=dop, po=msc).split(", w ")[0]
            w.append(f'<tr><td class="pkt">{f["rzym"]}.{i}</td><td>{_e(skrot)}</td>'
                     f'<td class="pkt">{proba}</td><td class="pkt">{mian}</td>'
                     f'<td></td><td></td><td></td></tr>')
    return ("<table><thead><tr><th>Nr</th><th>Cel — zachowanie zastępcze</th><th>Kryt.</th>"
            "<th>Horyzont</th><th>Data startu</th><th>Wynik</th><th>Osiągnięty</th></tr></thead>"
            f'<tbody>{"".join(w)}</tbody></table>')


def strona_ewaluacji(wyniki, funkcje, z_podpisami):
    """Tabela ewaluacji — dzielona na dwie strony.

    Dwadzieścia pięć wierszy z brzmieniem celu nie mieści się na jednej kartce
    (pomiar: 1584 px przy budżecie 1054). Skrócenie wiersza do samego numeru
    zabrałoby tabeli sens — nauczyciel wypełnia ją, nie wracając na strony
    z kartami — więc dzielimy zestaw, a nie treść wiersza.
    """
    ile = sum(len(f["wskazniki"]) for f in funkcje)
    zakres = " · ".join(f'{f["rzym"]} {f["skrot"].lower()}' for f in funkcje)
    ogon = ""
    if z_podpisami:
        ogon = """
    <div class="podpisy"><div>Podpis oceniającego</div><div>Podpis koordynatora</div></div>
    <div class="podstawa">
      <b>Podstawa.</b> Cele szczegółowe do analizy funkcjonalnej zachowania (FBA) i programu
      pozytywnego wsparcia (PBS) — element wielospecjalistycznej oceny poziomu funkcjonowania
      (WOPF). Model A-B-C (Antecedent–Behaviour–Consequence). Kryterium i horyzont wynikają
      z punktacji kwestionariusza funkcji (0–15 pkt); wynik kwestionariusza wskazuje
      przypuszczalną funkcję i nie zastępuje pełnej diagnozy. Podstawa prawna: ustawa
      z 14.12.2016 r. — Prawo oświatowe (Dz.U. 2024 poz. 737, ze zm.), art. 127; rozp. MEN
      z 9.08.2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej
      (Dz.U. 2017 poz. 1591, ze zm.); rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, ze zm.) —
      zintegrowane działania nauczycieli i specjalistów. Wszystkie pola są edytowalne.
    </div>"""
    return (f'    <div class="pas">Tabela ewaluacji · {ile} celów · {_e(zakres)}</div>'
            '\n'
            f'    {ewaluacja(wyniki, funkcje)}{ogon}')


# ——— złożenie dokumentu ————————————————————————————————————————————————
def dokument(uczen, klasa, data, wyniki):
    strony = [strona(1, "Cele SMART — wprowadzenie", "wprowadzenie",
                     wprowadzenie(wyniki), uczen, klasa, data)]
    for i, (f, pkt) in enumerate(zip(D.FUNKCJE, wyniki), 2):
        strony.append(strona(i, f'Cele SMART · funkcja {f["rzym"]}',
                             f'funkcja {f["rzym"]} · {f["skrot"].lower()}',
                             strona_funkcji(f, pkt), uczen, klasa, data))
    strony.append(strona(STRON - 1, "Tabela ewaluacji · część 1", "ewaluacja I–III",
                         strona_ewaluacji(wyniki, D.FUNKCJE[:3], False), uczen, klasa, data))
    strony.append(strona(STRON, "Tabela ewaluacji · część 2 i podpisy", "ewaluacja IV–V",
                         strona_ewaluacji(wyniki, D.FUNKCJE[3:], True), uczen, klasa, data))
    tytul = "Cele SMART do obserwacji pogłębionej (ABC / FBA)"
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_e(tytul)}{" — " + _e(uczen) if uczen else ""}</title>
<link rel="stylesheet" media="print" onload="this.media='all'"
  href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap">
<style>{STYL}</style>
</head>
<body>
{chr(10).join(strony)}
</body>
</html>
"""


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--uczen", default="", help="imię i nazwisko ucznia (puste = formularz)")
    p.add_argument("--klasa", default="")
    p.add_argument("--data", default="", help="data wypełnienia; puste = pole do wpisania")
    p.add_argument("--wyniki", default="", help="punktacja pięciu funkcji, np. 7,8,13,7,13")
    p.add_argument("--wyjscie", default="", help="ścieżka pliku HTML")
    a = p.parse_args()

    if a.wyniki:
        wyniki = [int(x) for x in a.wyniki.replace(" ", "").split(",")]
        if len(wyniki) != 5 or not all(0 <= x <= 15 for x in wyniki):
            p.error("--wyniki: pięć liczb 0–15, np. 7,8,13,7,13")
    else:
        wyniki = [7] * 5

    cel = Path(a.wyjscie) if a.wyjscie else KOR / (
        "Cele_SMART_FBA_obserwacja_poglebiona.html" if not a.uczen else
        "Cele_SMART_FBA_" + a.uczen.replace(" ", "_") + ".html")
    cel.write_text(dokument(a.uczen, a.klasa, a.data or "", wyniki), encoding="utf-8")
    print(f"{cel} · {cel.stat().st_size / 1024:.0f} kB · {STRON} stron · "
          f"{sum(len(f['wskazniki']) for f in D.FUNKCJE)} celów")


if __name__ == "__main__":
    main()
