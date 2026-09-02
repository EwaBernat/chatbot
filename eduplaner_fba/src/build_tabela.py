# -*- coding: utf-8 -*-
"""Druk FBA-T — tabela celów SMART do wskaźników FBA: wiek × poziom wsparcia.

Ten sam układ, co bank celów SMART KPOF: zakładki wersji wiekowych na górze,
w tabeli wiersz na wskaźnik i trzy kolumny poziomów wsparcia. Nauczyciel czyta
ją tak samo jak bank — schodzi wzrokiem do swojego wskaźnika i w bok do swojego
poziomu — więc kolejność kolumn zostaje taka jak tam: **Poziom III, II, I**,
od największego wsparcia do najmniejszego.

    python3 src/build_tabela.py            # Tabela_celow_FBA_wiek_poziom.html

Tabela drukuje się **poziomo** (trzy poziomy obok siebie nie mieszczą się na
kartce pionowej), a drukuje się ta wersja wiekowa, która jest otwarta — tak jak
w banku. Wydruk wszystkich trzech naraz to trzy razy Ctrl+P, nie jeden;
nauczycielowi i tak potrzebna jest zwykle jedna.
"""

import html
from pathlib import Path

import dane_poziomy as P

KOR = Path(__file__).resolve().parent.parent

STYL = """
:root{
  --ink:#2D1B69; --indigo:#4F3AA8; --violet:#6C4CC4; --accent:#E8450A;
  --on-accent:#FFFFFF; --tekst:#241C3A; --szary:#5B5470;
  --paper:#FFFFFF; --soft:#F6F3FC; --field:#EFEAF9; --row-alt:#FAF8FE;
  --line:#DCD4F0; --line-2:#C9BEEA; --tlo:#EDE9F6;
  --p3:#C2410C; --p2:#B45309; --p1:#15803D;
}
*{box-sizing:border-box}
body{margin:0; background:var(--tlo); color:var(--tekst);
  font:13px/1.55 "DM Sans",Arial,Helvetica,sans-serif; padding:22px 16px}
.ark{max-width:1180px; margin:0 auto; background:var(--paper); border-radius:12px;
  box-shadow:0 2px 16px rgba(45,27,105,.13); padding:22px 26px 28px}

.head{display:flex; align-items:flex-start; gap:12px; border-bottom:2px solid var(--line-2);
  padding-bottom:11px; margin-bottom:14px}
.mark{flex:0 0 auto; width:34px; height:34px; border-radius:7px; background:var(--ink);
  color:#fff; font:700 10px/34px "DM Sans",Arial,sans-serif; text-align:center; letter-spacing:.06em}
.head h1{margin:0; font-size:15px; color:var(--ink)}
.head .sub{font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--szary); margin-top:3px}
.head .prawa{margin-left:auto; text-align:right}
.head .prawa b{display:block; font-size:10px; letter-spacing:.1em; color:var(--accent); text-transform:uppercase}
.head .prawa span{font-size:8.5px; letter-spacing:.18em; text-transform:uppercase; color:var(--szary)}

.tyt{display:flex; align-items:center; gap:14px; margin-bottom:12px}
.tyt .pigula{background:var(--accent); color:var(--on-accent); border-radius:999px;
  padding:7px 18px; font-size:11px; font-weight:700; letter-spacing:.1em; text-transform:uppercase}
.tyt p{margin:0; font-size:11.5px; color:var(--szary); line-height:1.5}

.zakladki{display:flex; gap:8px; margin-bottom:12px; flex-wrap:wrap}
.tab{border:1px solid var(--line-2); background:var(--paper); color:var(--ink); border-radius:999px;
  padding:8px 18px; font:600 12px/1 "DM Sans",Arial,sans-serif; cursor:pointer}
.tab .w{font-size:9px; letter-spacing:.12em; text-transform:uppercase; color:var(--szary); margin-right:6px}
.tab[aria-selected="true"]{background:var(--ink); color:#fff; border-color:var(--ink)}
.tab[aria-selected="true"] .w{color:#CDBEF5}
.tab:focus-visible{outline:2px solid var(--accent); outline-offset:2px}

.legenda{display:grid; grid-template-columns:repeat(3,1fr); gap:10px; margin-bottom:14px}
.leg{border:1px solid var(--line); border-left:4px solid var(--violet); border-radius:0 8px 8px 0;
  padding:9px 12px; font-size:10.5px; line-height:1.5}
.leg b{display:block; font-size:11px; color:var(--ink); margin-bottom:2px}
.leg.p3{border-left-color:var(--p3)} .leg.p2{border-left-color:var(--p2)}
.leg.p1{border-left-color:var(--p1)}
.leg .kryt{color:var(--szary)}
.uwaga{background:var(--soft); border-left:4px solid var(--accent); border-radius:0 8px 8px 0;
  padding:10px 14px; font-size:11px; line-height:1.55; margin-bottom:14px}
.uwaga b{color:var(--ink)}

table{width:100%; border-collapse:collapse; font-size:11px; table-layout:fixed}
th{background:var(--field); color:var(--ink); text-align:left; font-size:9px; letter-spacing:.1em;
  text-transform:uppercase; padding:8px 9px; border:1px solid var(--line-2)}
th.p3{color:var(--p3)} th.p2{color:var(--p2)} th.p1{color:var(--p1)}
.wband th{background:var(--soft); color:var(--szary); font-size:9px; letter-spacing:.12em;
  border-bottom:none; padding:6px 9px}
.wband th b{color:var(--accent); letter-spacing:.1em; margin-left:10px}
td{padding:7px 9px; border:1px solid var(--line); vertical-align:top; line-height:1.45}
tbody tr:nth-child(even) td{background:var(--row-alt)}
td.nr{text-align:center; font-weight:700; color:var(--ink); font-size:10px}
td.wsk b{display:block; color:var(--ink); font-size:11px; margin-bottom:2px}
td.wsk span{color:var(--szary); font-size:9.5px; letter-spacing:.04em; text-transform:uppercase}
td.g{font-size:10.5px}
td.g .ram{display:block; margin-top:3px; color:var(--szary); font-size:9px;
  letter-spacing:.06em; text-transform:uppercase}
tr.pas td{background:var(--ink) !important; color:#fff; font-size:10px; letter-spacing:.14em;
  text-transform:uppercase; padding:7px 10px; border-color:var(--ink)}
tr.pas td .li{color:#CDBEF5; letter-spacing:.06em; text-transform:none; margin-left:8px}
.wersja[hidden]{display:none}
.stopka{margin-top:16px; border-top:1px solid var(--line); padding-top:9px;
  display:flex; justify-content:space-between; font-size:9px; color:var(--szary); letter-spacing:.04em}

@media print{
  @page{size:A4 landscape; margin:9mm}
  body{background:#fff; padding:0}
  .ark{max-width:none; box-shadow:none; border-radius:0; padding:0}
  .zakladki, .tab{display:none}
  thead{display:table-header-group}
  tr{break-inside:avoid}
  .uwaga{break-inside:avoid}
}
"""


def _e(t):
    return html.escape(str(t), quote=False)


def _legenda():
    k = "".join(
        f'<div class="leg {kod}"><b>{nazwa}</b>{_e(opis)}'
        f'<div class="kryt">kryterium {kryt} sytuacji · weryfikacja po {hor.replace("tygodni", "tygodniach")}</div></div>'
        for kod, nazwa, kryt, hor, opis in P.POZIOMY)
    return f'<div class="legenda">{k}</div>'


def _wiersze(kod_wersji):
    w = []
    for rzym, f in P.CELE.items():
        w.append(f'<tr class="pas"><td colspan="5">Funkcja {rzym} · {_e(f["nazwa"])}'
                 f'<span class="li">pięć wskaźników kwestionariusza</span></td></tr>')
        for i, wsk in enumerate(f["wskazniki"], 1):
            kom = ""
            for (kod, _n, kryt, hor, _o), tekst in zip(P.POZIOMY, wsk[kod_wersji]):
                kom += (f'<td class="g"><span class="tresc">{_e(tekst)}</span>'
                        f'<span class="ram">{kryt} sytuacji · {hor}</span></td>')
            w.append(f'<tr><td class="nr">{rzym}.{i}</td>'
                     f'<td class="wsk"><b>{_e(wsk["wskaznik"])}</b>'
                     f'<span>zachowanie zastępcze: {_e(wsk["zastepcze"])}</span></td>{kom}</tr>')
    return "".join(w)


def _tabela(kod_wersji, nazwa_wersji, aktywna):
    naglowki = "".join(f'<th class="{kod}">{nazwa}</th>' for kod, nazwa, *_ in P.POZIOMY)
    ukryj = "" if aktywna else " hidden"
    return f'''<section class="wersja" id="w-{kod_wersji}" data-wersja="{kod_wersji}"{ukryj}>
  <table>
    <colgroup><col style="width:5%"><col style="width:32%">
      <col style="width:21%"><col style="width:21%"><col style="width:21%"></colgroup>
    <caption class="sr-only">Cele SMART · wersja {kod_wersji} · {_e(nazwa_wersji)}</caption>
    <thead>
    <tr class="wband"><th colspan="5">EduPlaner 2026 · druk FBA-T · cele SMART do wskaźników FBA
      <b>wersja {kod_wersji} · {_e(nazwa_wersji)}</b></th></tr>
    <tr>
      <th>Nr</th>
      <th>Wskaźnik z kwestionariusza funkcji</th>
      {naglowki}
    </tr></thead>
    <tbody>{_wiersze(kod_wersji)}</tbody>
  </table>
</section>'''


SKRYPT = """
/* Zakładki wersji wiekowych — jedna widoczna naraz, jak w banku celów SMART.
   Drukuje się wersja otwarta: nauczycielowi potrzebna jest zwykle jedna,
   a trzy naraz to 18 kartek poziomych zamiast sześciu. */
document.querySelectorAll('.tab').forEach(t => t.addEventListener('click', () => {
  const w = t.dataset.wersja;
  document.querySelectorAll('.tab').forEach(x =>
    x.setAttribute('aria-selected', String(x.dataset.wersja === w)));
  document.querySelectorAll('.wersja').forEach(s => { s.hidden = s.dataset.wersja !== w; });
}));
"""


def dokument():
    zak = "".join(
        f'<button type="button" class="tab" role="tab" data-wersja="{kod}" '
        f'aria-selected="{str(i == 0).lower()}"><span class="w">wersja {kod}</span>{_e(nazwa)}</button>'
        for i, (kod, nazwa) in enumerate(P.WERSJE))
    tab = "".join(_tabela(kod, nazwa, i == 0) for i, (kod, nazwa) in enumerate(P.WERSJE))
    _f, wsk, cele = P.stan()
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cele SMART do wskaźników FBA — wiek i poziom wsparcia</title>
<link rel="stylesheet" media="print" onload="this.media='all'"
  href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap">
<style>{STYL}
.sr-only{{position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0)}}</style>
</head>
<body>
<div class="ark">
  <div class="head">
    <span class="mark">PCTP</span>
    <div>
      <h1>EduPlaner 2026</h1>
      <div class="sub">ABC / FBA · tabela celów SMART · wiek i poziom wsparcia</div>
    </div>
    <div class="prawa"><b>ABC · PBS</b><span>narzędzie · druk FBA-T</span></div>
  </div>

  <div class="tyt">
    <span class="pigula">{cele} celów SMART</span>
    <p>{wsk} wskaźników kwestionariusza funkcji zachowania × trzy poziomy wsparcia
       × trzy wersje wiekowe. Wiersz mówi, <b>co dziecko robi zamiast zachowania trudnego</b>;
       kolumna — ile przy tym dostaje podpory.</p>
  </div>

  <div class="zakladki" role="tablist" aria-label="Wersje wiekowe">{zak}</div>

  {_legenda()}

  <div class="uwaga">
    <b>Poziom zmienia warunki, nie funkcję.</b> Na każdym poziomie dziecko uczy się tej samej
    drogi do tej samej funkcji — ucieczki, uwagi, dostępu, regulacji — tylko z inną ilością
    podpory. Cel przepisujemy do IPET-u w brzmieniu z komórki i dokładamy kryterium oraz
    horyzont z nagłówka kolumny. Kryterium na Poziomie I zostaje <b>4 z 5</b>, a nie rośnie
    do 5 z 5: rośnie trudność samego zachowania, nie liczba prób — „za każdym razem” to
    w przedszkolu cel nie do osiągnięcia i psuje ewaluację, zamiast ją domykać.
  </div>

  {tab}

  <div class="stopka">
    <span>EduPlaner 2026 · PCTP · pedagog specjalny mgr Mirosława Ewa Jurczyszyn</span>
    <span>druk FBA-T · tabela drukuje się poziomo · {cele} celów</span>
  </div>
</div>
<script>{SKRYPT}</script>
</body>
</html>
"""


def main():
    cel = KOR / "Tabela_celow_FBA_wiek_poziom.html"
    cel.write_text(dokument(), encoding="utf-8")
    _f, wsk, cele = P.stan()
    print(f"{cel} · {cel.stat().st_size / 1024:.0f} kB · {wsk} wskaźników · {cele} celów")


if __name__ == "__main__":
    main()
