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
import konspekt_fba as KON
import konspekty_fba as KF

KOR = Path(__file__).resolve().parent.parent

STYL = """
:root{
  --ink:#2D1B69; --indigo:#4F3AA8; --violet:#6C4CC4; --accent:#E8450A;
  --on-accent:#FFFFFF; --tekst:#241C3A; --szary:#5B5470;
  --paper:#FFFFFF; --soft:#F6F3FC; --field:#EFEAF9; --row-alt:#FAF8FE;
  --line:#DCD4F0; --line-2:#C9BEEA; --tlo:#EDE9F6;
  /* Poziomy wsparcia mają kolor tylko w legendzie na górze: czerwony, żółty,
     zielony — jak oceny modyfikacji w konspekcie. W tabeli koloru nie ma,
     bo 75 kolorowych komórek przestaje cokolwiek wyróżniać. */
  --p3:#B91C1C; --p2:#A16207; --p1:#15803D;
  --t3:#FEF2F2; --t2:#FEFCE8; --t1:#F0FDF4;
  --r3:#FCA5A5; --r2:#FDE047; --r1:#86EFAC;
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
.leg{border:1px solid var(--line); border-left:5px solid var(--violet); border-radius:0 9px 9px 0;
  padding:10px 13px; font-size:10.5px; line-height:1.5}
.leg b{display:flex; align-items:center; gap:7px; font-size:11.5px; color:var(--ink); margin-bottom:3px}
.leg b i{width:11px; height:11px; border-radius:50%; display:inline-block; border:1px solid rgba(0,0,0,.14)}
.leg.p3{background:var(--t3); border-color:var(--r3); border-left-color:var(--p3)}
.leg.p2{background:var(--t2); border-color:var(--r2); border-left-color:var(--p2)}
.leg.p1{background:var(--t1); border-color:var(--r1); border-left-color:var(--p1)}
.leg.p3 b i{background:var(--r3)} .leg.p2 b i{background:var(--r2)} .leg.p1 b i{background:var(--r1)}
.leg.p3 b{color:var(--p3)} .leg.p2 b{color:var(--p2)} .leg.p1 b{color:var(--p1)}
.leg .kryt{color:var(--szary)}
.uwaga{background:var(--soft); border-left:4px solid var(--accent); border-radius:0 8px 8px 0;
  padding:10px 14px; font-size:11px; line-height:1.55; margin-bottom:14px}
.uwaga b{color:var(--ink)}

table{width:100%; border-collapse:collapse; font-size:11px; table-layout:fixed}
th{background:var(--field); color:var(--ink); text-align:left; font-size:9px; letter-spacing:.1em;
  text-transform:uppercase; padding:8px 9px; border:1px solid var(--line-2)}
th.p3, th.p2, th.p1{color:var(--ink)}
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
td.g.haskon{cursor:pointer; position:relative}
td.g.haskon:hover, td.g.haskon:focus-visible{outline:2px solid var(--accent); outline-offset:-2px}
td.g.haskon .tresc{text-decoration:underline; text-decoration-color:var(--line-2);
  text-underline-offset:2px}
.kzn{display:inline-block; margin-top:5px; background:var(--accent); color:var(--on-accent);
  border-radius:999px; padding:3px 9px; font-size:8px; letter-spacing:.09em; text-transform:uppercase}
/* Wykaz konspektów: siatka minmax, nie rząd pigułek — pigułka miała szerokość
   swojego tytułu, więc kolumny nie trzymały pionu. Pasek rozwijania w kolorze
   akcentu, bo wykaz schowany pod szarą belką nauczyciel przeoczy. */
.kspis{border:1px solid var(--accent); border-radius:10px; margin-bottom:12px; overflow:hidden}
.kspis > summary{cursor:pointer; list-style:none; background:var(--accent); color:var(--on-accent);
  padding:9px 15px; font:700 11px/1.4 "DM Sans",Arial,sans-serif; letter-spacing:.08em;
  text-transform:uppercase; display:flex; align-items:center; gap:9px}
.kspis > summary::-webkit-details-marker{display:none}
.kspis > summary::before{content:"▸"; font-size:13px; transition:transform .15s}
.kspis[open] > summary::before{transform:rotate(90deg)}
.kspis-tresc{padding:12px 15px 14px}
.kgrupa + .kgrupa{margin-top:12px}
.kgrupa h4{margin:0 0 7px; font-size:10px; letter-spacing:.11em; text-transform:uppercase;
  color:var(--accent)}
.ksiatka{display:grid; grid-template-columns:repeat(auto-fill,minmax(232px,1fr)); gap:7px}
.kbtn{text-align:left; background:var(--paper); border:1px solid var(--line); border-radius:8px;
  padding:7px 10px; cursor:pointer; font:400 10.5px/1.4 "DM Sans",Arial,sans-serif; color:var(--tekst)}
.kbtn:hover{border-color:var(--accent)}
.kbtn:hover b{color:var(--accent)}
.kbtn .knr{display:inline-block; min-width:26px; font-weight:700; color:var(--ink); font-size:9.5px}
.kbtn b{color:var(--ink); font-size:11px}
.kbtn .kzast{display:block; color:var(--szary); font-size:9px; margin-top:2px}
.wersja[hidden]{display:none}
.stopka{margin-top:16px; border-top:1px solid var(--line); padding-top:9px;
  display:flex; justify-content:space-between; font-size:9px; color:var(--szary); letter-spacing:.04em}

@media print{
  @page{size:A4 landscape; margin:9mm}
  /* Konspekt to druk pionowy — orientacja pozioma odziedziczona po tabeli
     kładła go na boku i rozciągała kolumny celów na całą szerokość. */
  @page kon{size:A4 portrait; margin:10mm}
  body{background:#fff; padding:0}
  .ark{max-width:none; box-shadow:none; border-radius:0; padding:0}
  .zakladki, .tab{display:none}
  thead{display:table-header-group}
  tr{break-inside:avoid}
  .uwaga{break-inside:avoid}
  .kmodal{display:none !important}
  .kzn, .kspis{display:none}
  td.g.haskon .tresc{text-decoration:none}
  /* Druk konspektu: znika tabela, zostaje sama karta — pionowo, bez przycisków. */
  html.print-konspekt .ark{display:none !important}
  html.print-konspekt .kmodal.open{display:block !important; position:static; background:none;
    padding:0; overflow:visible}
  /* 0.96 to zapas na fonty: pomiar leci na Arialu (bez sieci), DM Sans jest
     odrobinę wyższy, a scenariusz kończy się tuż pod krawędzią kartki. Bez tego
     marginesu konspekt schodziłby u niej na drugą stronę w pół tabeli. */
  html.print-konspekt .kcard{box-shadow:none; max-width:none; padding:0; border-radius:0;
    page:kon; zoom:.96}
  html.print-konspekt .kclose, html.print-konspekt .kfoot, html.print-konspekt .kesc{display:none}
  html.print-konspekt .zal{break-before:page; border-top:none}
  /* Zeszyt jednej wersji wiekowej: wszystkie jej konspekty po kolei, każdy
     scenariusz i każdy arkusz na własnej kartce. */
  html.print-zeszyt .ark{display:none !important}
  html.print-zeszyt .kmodal{display:none !important}
  html.print-zeszyt[data-zeszyt="A"] .kmodal[data-wersja="A"],
  html.print-zeszyt[data-zeszyt="B"] .kmodal[data-wersja="B"],
  html.print-zeszyt[data-zeszyt="C"] .kmodal[data-wersja="C"]{display:block !important;
    position:static; background:none; padding:0; overflow:visible; break-before:page}
  html.print-zeszyt .kcard{box-shadow:none; max-width:none; padding:0; border-radius:0;
    page:kon; zoom:.96}
  html.print-zeszyt .kclose, html.print-zeszyt .kfoot, html.print-zeszyt .kesc{display:none}
  html.print-zeszyt .zal{break-before:page; border-top:none}
  html.print-zeszyt .kwsk, html.print-zeszyt .kmod, html.print-zeszyt .zal-karta{break-inside:avoid}
  /* Zagęszczenie na druk — konspekt ma się zmieścić na jednej kartce, tak jak
     konspekty w banku. Pomiar przed: 1380 px scenariusza przy budżecie 1047. */
  html.print-konspekt .ktitle{margin:9px 0 8px}
  html.print-konspekt .ktitle h3{font-size:16px}
  html.print-konspekt .ksec{margin:9px 0 5px}
  html.print-konspekt .kcele{gap:8px}
  html.print-konspekt .kcel{padding:7px 9px}
  html.print-konspekt .ktresc{font-size:10.5px; line-height:1.4}
  html.print-konspekt .ksmart li{font-size:8.8px; line-height:1.32}
  html.print-konspekt .kkryt{font-size:8.8px; padding-top:4px; margin-top:4px}
  html.print-konspekt .klista{font-size:9.5px; line-height:1.4}
  html.print-konspekt .kkurs{font-size:8.8px; margin:4px 0 3px}
  html.print-konspekt table.ktab{font-size:9.5px}
  html.print-konspekt table.ktab td{padding:4px 7px; line-height:1.35}
  html.print-konspekt .kmod{font-size:9px; padding:6px 8px}
  html.print-konspekt .kwsk{font-size:9.5px; padding:7px 11px; margin-top:8px}
  html.print-konspekt .kmeta{margin-top:6px; gap:8px}
  html.print-konspekt .kmeta .field{padding:2px 2px 3px; font-size:9px}
  html.print-konspekt .kmeta .field .val{font-size:10.5px}
  html.print-konspekt .khead{padding-bottom:8px}
  html.print-konspekt .khead .kw{font-size:12.5px}
  html.print-konspekt .ksec{margin:7px 0 4px}
  html.print-konspekt .ksec .sq{width:19px; height:19px}
  html.print-konspekt .ksmart{gap:2px; margin-top:5px}
  html.print-konspekt .ksmart li{font-size:8.4px; line-height:1.28}
  html.print-konspekt table.ktab td{padding:3px 6px}
  html.print-konspekt table.ktab th{padding:4px 6px}
  html.print-konspekt .kmod{font-size:8.6px; line-height:1.34}
  html.print-konspekt .kmods{gap:7px}
  html.print-konspekt .ktitle{margin:7px 0 6px}
  html.print-konspekt .ktitle h3{font-size:15px}
  html.print-konspekt .ktitle .kp{padding:3px 11px; font-size:8.5px}
  html.print-konspekt .ktitle .ksfera{margin:6px 0 2px; font-size:8.6px}
  html.print-konspekt .ktitle .kpod{font-size:10px}
  html.print-konspekt .ktresc{font-size:10px}
  html.print-konspekt .klista{font-size:9.2px; line-height:1.36}
  /* Zapas na fonty: pomiar leci na Arialu (bez sieci), a DM Sans jest odrobinę
     wyższy — 30 px luzu trzyma konspekt na jednej kartce w obu przypadkach. */
  html.print-konspekt .kcel{padding:6px 9px}
  html.print-konspekt .kcele{gap:7px}
  html.print-konspekt .kdwie{gap:9px}
  html.print-konspekt .kwsk{padding:6px 10px; line-height:1.42}
  /* To samo zagęszczenie w zeszycie — konspekt ma się zmieścić na jednej kartce, tak jak
     konspekty w banku. Pomiar przed: 1380 px scenariusza przy budżecie 1047. */
  html.print-zeszyt .ktitle{margin:9px 0 8px}
  html.print-zeszyt .ktitle h3{font-size:16px}
  html.print-zeszyt .ksec{margin:9px 0 5px}
  html.print-zeszyt .kcele{gap:8px}
  html.print-zeszyt .kcel{padding:7px 9px}
  html.print-zeszyt .ktresc{font-size:10.5px; line-height:1.4}
  html.print-zeszyt .ksmart li{font-size:8.8px; line-height:1.32}
  html.print-zeszyt .kkryt{font-size:8.8px; padding-top:4px; margin-top:4px}
  html.print-zeszyt .klista{font-size:9.5px; line-height:1.4}
  html.print-zeszyt .kkurs{font-size:8.8px; margin:4px 0 3px}
  html.print-zeszyt table.ktab{font-size:9.5px}
  html.print-zeszyt table.ktab td{padding:4px 7px; line-height:1.35}
  html.print-zeszyt .kmod{font-size:9px; padding:6px 8px}
  html.print-zeszyt .kwsk{font-size:9.5px; padding:7px 11px; margin-top:8px}
  html.print-zeszyt .kmeta{margin-top:6px; gap:8px}
  html.print-zeszyt .kmeta .field{padding:2px 2px 3px; font-size:9px}
  html.print-zeszyt .kmeta .field .val{font-size:10.5px}
  html.print-zeszyt .khead{padding-bottom:8px}
  html.print-zeszyt .khead .kw{font-size:12.5px}
  html.print-zeszyt .ksec{margin:7px 0 4px}
  html.print-zeszyt .ksec .sq{width:19px; height:19px}
  html.print-zeszyt .ksmart{gap:2px; margin-top:5px}
  html.print-zeszyt .ksmart li{font-size:8.4px; line-height:1.28}
  html.print-zeszyt table.ktab td{padding:3px 6px}
  html.print-zeszyt table.ktab th{padding:4px 6px}
  html.print-zeszyt .kmod{font-size:8.6px; line-height:1.34}
  html.print-zeszyt .kmods{gap:7px}
  html.print-zeszyt .ktitle{margin:7px 0 6px}
  html.print-zeszyt .ktitle h3{font-size:15px}
  html.print-zeszyt .ktitle .kp{padding:3px 11px; font-size:8.5px}
  html.print-zeszyt .ktitle .ksfera{margin:6px 0 2px; font-size:8.6px}
  html.print-zeszyt .ktitle .kpod{font-size:10px}
  html.print-zeszyt .ktresc{font-size:10px}
  html.print-zeszyt .klista{font-size:9.2px; line-height:1.36}
  /* Zapas na fonty: pomiar leci na Arialu (bez sieci), a DM Sans jest odrobinę
     wyższy — 30 px luzu trzyma konspekt na jednej kartce w obu przypadkach. */
  html.print-zeszyt .kcel{padding:6px 9px}
  html.print-zeszyt .kcele{gap:7px}
  html.print-zeszyt .kdwie{gap:9px}
  html.print-zeszyt .kwsk{padding:6px 10px; line-height:1.42}
  html.print-konspekt .kwsk, html.print-konspekt .kmod, html.print-konspekt .zal-karta{break-inside:avoid}
}
"""


def _e(t):
    return html.escape(str(t), quote=False)


def _legenda():
    k = "".join(
        f'<div class="leg {kod}"><b><i aria-hidden="true"></i>{nazwa}</b>{_e(opis)}'
        f'<div class="kryt">kryterium {kryt} sytuacji · weryfikacja po {hor.replace("tygodni", "tygodniach")}</div></div>'
        for kod, nazwa, kryt, hor, opis in P.POZIOMY)
    return f'<div class="legenda">{k}</div>'


def _wiersze(kod_wersji):
    w = []
    for rzym, f in P.CELE.items():
        w.append(f'<tr class="pas"><td colspan="5">Funkcja {rzym} · {_e(f["nazwa"])}'
                 f'<span class="li">pięć wskaźników kwestionariusza</span></td></tr>')
        for i, wsk in enumerate(f["wskazniki"], 1):
            nrw = f"{rzym}.{i}"
            kid = KF.kid(nrw, kod_wersji)
            kom = ""
            for (kod, _n, kryt, hor, _o), tekst in zip(P.POZIOMY, wsk[kod_wersji]):
                kom += (f'<td class="g haskon" data-kon="{kid}" data-lvl="{kod}"'
                        f' data-wersja="{kod_wersji}" data-wsk="{nrw}" tabindex="0" role="button"'
                        f' title="Otwórz konspekt zajęć do tego celu">'
                        f'<span class="tresc">{_e(tekst)}</span>'
                        f'<span class="ram">{kryt} sytuacji · {hor}</span></td>')
            znak = (f'<span class="kzn">konspekt: {_e(KF.RDZEN[nrw]["tytul"])}</span>')
            w.append(f'<tr data-wsk="{nrw}"><td class="nr">{nrw}</td>'
                     f'<td class="wsk"><b>{_e(wsk["wskaznik"])}</b>'
                     f'<span>zachowanie zastępcze: {_e(wsk["zastepcze"])}</span>{znak}</td>{kom}</tr>')
    return "".join(w)


def _tabela(kod_wersji, nazwa_wersji, aktywna):
    naglowki = "".join(f'<th class="{kod}">{nazwa}</th>' for kod, nazwa, *_ in P.POZIOMY)
    ukryj = "" if aktywna else " hidden"
    return f'''<section class="wersja" id="w-{kod_wersji}" data-wersja="{kod_wersji}"{ukryj}>
  {KON.spis(kod_wersji)}
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
<style>{STYL}{KON.STYL}
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
{KON.modale()}
<script>{SKRYPT}{KON.SKRYPT}</script>
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
