#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Druk TOM-C — 25 celów SMART do obserwacji pogłębionej teorii umysłu.

    python3 03_kod_zrodlowy/build_cele_sens.py
    python3 03_kod_zrodlowy/build_cele_sens.py --uczen "Zofia Lewandowska" --grupa "Biedronki" \
            --wyniki 8,6,3,1,2

`--wyniki` to wyniki pięciu komponentów z karty obserwacji (0–10, w kolejności karty:
emocje, pragnienia, udawanie, fałszywe przekonanie, ukryte emocje). Z nich biorą się
kryterium i horyzont każdego celu — dlatego znaczniki `{proba}` i `{horyzont_*}`
podstawia się dopiero tutaj, a nie w banku.

DOKUMENTY Z NAZWISKIEM DZIECKA NIE WCHODZĄ DO REPOZYTORIUM — to dane osobowe.
Zapisują się z prefiksem `uczen_`, który jest wpisany do .gitignore.
"""
from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import unicodedata

KORZEN = pathlib.Path(__file__).resolve().parent.parent
DANE = KORZEN / "01_dane_json" / "cele_tom_obserwacja.json"
KATALOG = KORZEN / "02_gotowe_dokumenty"
KOLEJNOSC = ["I", "II", "III", "IV", "V"]


def e(t) -> str:
    return html.escape(str(t if t is not None else ""))


def slug(tekst: str) -> str:
    t = unicodedata.normalize("NFKD", tekst.replace("ł", "l").replace("Ł", "L"))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9]+", "_", t).strip("_").lower()


def prog_dla(suma: int, progi: list[dict]) -> dict:
    for p in progi:                       # progi są uporządkowane od najwyższego
        if suma >= p["od_punktow"]:
            return p
    return progi[-1]


def podstaw(tekst: str, prog: dict | None) -> str:
    if prog is None:
        return (tekst.replace("{proba}", "……… z 5")
                     .replace("{horyzont_dopelniacz}", "……… tygodni")
                     .replace("{horyzont_miejscownik}", "……… tygodniach"))
    return (tekst.replace("{proba}", prog["kryterium"])
                 .replace("{horyzont_dopelniacz}", prog["horyzont"]["dopelniacz"])
                 .replace("{horyzont_miejscownik}", prog["horyzont"]["miejscownik"]))


STYL = """
:root{--fiolet:#2D1B69;--fiolet-2:#5a4a94;--fiolet-tlo:#efeaf9;--fiolet-linia:#d9d0f0;
  --pomarancz:#E8450A;--pomarancz-tlo:#fdece4;--pomarancz-linia:#f3cdbd;
  --ink:#2b2733;--szary:#6f6a7d;--linia:#e4e1ec;--zebra:#faf7f2;
  --dom:#c0392b;--dom-tlo:#fbebe9;--ist:#c8811b;--ist-tlo:#fbf3e3;--sla:#1f8a5b;--sla-tlo:#eaf6f0}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:#e9e7ef;color:var(--ink);font-family:'Mulish','Segoe UI',Candara,Arial,sans-serif}
.strona{width:210mm;min-height:297mm;margin:12px auto;background:#fff;padding:11mm 12mm 8mm;
  box-shadow:0 6px 30px rgba(45,27,105,.16);display:flex;flex-direction:column}
.head{display:flex;align-items:center;gap:12px}
.mark{width:38px;height:38px;border-radius:50%;background:var(--fiolet);border:2px solid #cfc4ea;color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:8.5px;font-weight:800;flex:0 0 auto}
.mark::after{content:"PCTP"}
.head h1{font-size:16px;margin:0;color:var(--fiolet)}
.head .sub{font-size:8.5px;color:var(--szary);letter-spacing:.6px;text-transform:uppercase;font-weight:700;margin-top:2px}
.head .prawa{margin-left:auto;text-align:right}
.head .prawa b{display:inline-block;background:var(--pomarancz);color:#fff;font-size:10px;padding:4px 12px;border-radius:20px}
.head .prawa span{display:block;font-size:8px;color:var(--szary);letter-spacing:.9px;margin-top:3px;text-transform:uppercase}
.kreska{height:3px;border-radius:3px;margin:8px 0 0;
  background:linear-gradient(90deg,var(--fiolet) 0%,var(--fiolet) 55%,var(--pomarancz) 55%,var(--pomarancz) 100%)}
.metryka{display:flex;gap:8px;margin-top:9px}
.metryka div{flex:1;background:var(--fiolet-tlo);border:1px solid var(--fiolet-linia);border-radius:8px;
  padding:5px 10px;font-size:11px;display:flex;gap:7px;align-items:baseline}
.metryka span{font-size:7.5px;font-weight:800;letter-spacing:.7px;color:var(--fiolet);text-transform:uppercase}
.metryka b{flex:1;border-bottom:1.5px dotted #b7add6;font-size:11px}
.tresc{flex:1;margin-top:10px}
.pas{background:var(--fiolet);color:#fff;border-radius:8px;padding:6px 12px;font-size:11px;font-weight:700;
  letter-spacing:.3px;margin-bottom:9px}
.wstep{font-size:10.5px;line-height:1.6;background:var(--zebra);border-radius:9px;padding:10px 13px}
.wstep b{color:var(--fiolet)}
.dwie{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
.karta-info{border:1px solid var(--fiolet-linia);border-radius:9px;padding:9px 12px;font-size:10px;line-height:1.55}
.karta-info h3{margin:0 0 4px;font-size:10.5px;color:var(--fiolet);letter-spacing:.4px}
table{width:100%;border-collapse:collapse;font-size:10px;margin-top:10px}
th{background:var(--fiolet);color:#fff;font-size:8px;letter-spacing:.6px;text-transform:uppercase;
  padding:5px 7px;text-align:left}
td{border-bottom:1px solid var(--linia);padding:5px 7px;vertical-align:top}
tr:nth-child(even) td{background:var(--zebra)}
td.pkt{font-weight:800;color:var(--fiolet);white-space:nowrap}
.ocena{display:inline-block;font-size:8px;font-weight:800;padding:1px 7px;border-radius:9px;
  background:var(--sla-tlo);color:var(--sla)}
.ocena.pri{background:var(--dom-tlo);color:var(--dom)}
.ocena.mon{background:var(--ist-tlo);color:var(--ist)}
.fn{display:flex;align-items:center;gap:10px;margin-bottom:7px}
.fn .rz{width:26px;height:26px;border-radius:7px;background:var(--pomarancz);color:#fff;display:flex;
  align-items:center;justify-content:center;font-weight:800;font-size:12px;flex:0 0 auto}
.fn h2{margin:0;font-size:14px;color:var(--fiolet)}
.fn .op{font-size:9px;color:var(--szary);margin-top:2px;line-height:1.4}
.fn .bad{margin-left:auto;text-align:right;font-size:9.5px;color:var(--szary);white-space:nowrap}
.fn .bad b{display:block;color:var(--fiolet);font-size:10px;margin-top:2px}
.si{background:var(--pomarancz-tlo);border:1px solid var(--pomarancz-linia);border-radius:8px;
  padding:7px 11px;font-size:9.5px;line-height:1.55;margin-bottom:9px}
.si b{color:var(--fiolet)}
.cel{border:1px solid var(--linia);border-radius:10px;padding:9px 12px;margin-bottom:9px;break-inside:avoid}
.cel-h{display:flex;gap:9px;align-items:flex-start;margin-bottom:5px}
.cel-h .nr{background:var(--fiolet);color:#fff;font-size:9px;font-weight:800;padding:2px 8px;border-radius:10px;flex:0 0 auto}
.cel-h .def{font-size:9.5px;line-height:1.45;color:var(--szary)}
.cel-h .def b{color:var(--fiolet);margin-right:5px}
.strat{font-size:9px;color:var(--pomarancz);font-weight:700;margin:0 0 5px 0}
.cel-t{font-size:10.5px;line-height:1.55;margin:0 0 6px;background:var(--fiolet-tlo);border-radius:8px;padding:7px 11px}
.cel-t b{display:block;font-size:8px;letter-spacing:.7px;text-transform:uppercase;color:var(--fiolet);margin-bottom:3px}
.smart{display:grid;grid-template-columns:1fr 1fr;gap:3px 10px;font-size:9px;line-height:1.4}
.smart div{display:flex;gap:6px}
.smart i{background:var(--fiolet-2);color:#fff;width:14px;height:14px;border-radius:4px;display:flex;
  align-items:center;justify-content:center;font-size:8px;font-style:normal;font-weight:800;flex:0 0 auto}
.obs{display:flex;gap:10px;align-items:center;margin-top:6px;padding-top:6px;border-top:1px dashed var(--linia);
  font-size:9px;color:var(--szary);flex-wrap:wrap}
.obs b{color:var(--fiolet)}
.obs .wynik{margin-left:auto;white-space:nowrap}
.obs .pole{display:inline-block;width:34px;border-bottom:1.5px dotted #b7add6}
.uwagi{font-size:9px;color:var(--szary);line-height:1.5;margin-top:6px}
.stopka{margin-top:auto;padding-top:7px;border-top:1px solid var(--linia);display:flex;
  justify-content:space-between;font-size:8px;color:var(--szary)}
@media print{body{background:#fff}.strona{box-shadow:none;margin:0;page-break-after:always}
  @page{size:A4 portrait;margin:0}}
"""


def naglowek(sub: str, uczen: str, grupa: str) -> str:
    pole = lambda v: e(v) if v else "&nbsp;"
    return f"""<div class="head"><span class="mark" role="img" aria-label="Logo PCTP"></span>
  <div><h1>EduPlaner 2026</h1><div class="sub">{sub}</div></div>
  <div class="prawa"><b>ToM · WOPF</b><span>narzędzie · druk TOM-C</span></div></div>
<div class="kreska"></div>
<div class="metryka">
  <div><span>Dotyczy dziecka</span><b>{pole(uczen)}</b></div>
  <div><span>Grupa</span><b>{pole(grupa)}</b></div>
  <div><span>Data</span><b>&nbsp;</b> r.</div></div>"""


def stopka(nr: int, ile: int, opis: str) -> str:
    return (f'<div class="stopka"><span>EduPlaner 2026 · PCTP · pedagog specjalny '
            f'<b>mgr Mirosława Ewa Jurczyszyn</b></span>'
            f'<span>Strona {nr} z {ile} · {opis}</span></div>')


def klasa_oceny(ocena: str) -> str:
    return {"Priorytet": "pri", "Do monitorowania": "mon"}.get(ocena, "")


def strona_wstepna(dane: dict, wyniki: dict | None, uczen: str, grupa: str, ile: int) -> str:
    wiersze = []
    for nr in KOLEJNOSC:
        z = next(x for x in dane["komponenty"] if x["nr"] == nr)
        if wyniki:
            suma = wyniki[nr]
            prog = prog_dla(suma, dane["progi"])
            wiersze.append(
                f'<tr><td>{e(nr)} · {e(z["nazwa"])}</td><td class="pkt">{suma}/10</td>'
                f'<td style="font-size:9px">{e(z["norma_rozwojowa"])}</td>'
                f'<td><span class="ocena {klasa_oceny(prog["ocena"])}">{e(prog["ocena"])}</span></td>'
                f'<td class="pkt">{e(prog["kryterium"])}</td>'
                f'<td class="pkt">{e(prog["horyzont"]["mianownik"])}</td>'
                f'<td>{e(prog["dlaczego"])}</td></tr>')
        else:
            wiersze.append(
                f'<tr><td>{e(nr)} · {e(z["nazwa"])}</td><td class="pkt">…/10</td>'
                f'<td style="font-size:9px">{e(z["norma_rozwojowa"])}</td>'
                f'<td>………</td><td class="pkt">……</td><td class="pkt">……</td>'
                f'<td>wpisz po odczytaniu pasma z tabeli progów</td></tr>')
    progi = "".join(
        f'<tr><td>{p["od_punktow"]} pkt i więcej</td>'
        f'<td><span class="ocena {klasa_oceny(p["ocena"])}">{e(p["ocena"])}</span></td>'
        f'<td class="pkt">{e(p["kryterium"])}</td><td class="pkt">{e(p["horyzont"]["mianownik"])}</td>'
        f'<td>{e(p["dlaczego"])}</td></tr>' for p in dane["progi"])
    return f"""<section class="strona">
{naglowek('Teoria umysłu (ToM) · cele SMART — wprowadzenie', uczen, grupa)}
<div class="tresc">
  <div class="pas">Cele SMART do obserwacji pogłębionej · 25 wskaźników karty obserwacji ToM</div>
  <div class="wstep"><b>Po co ten druk.</b> Karta obserwacji ToM kończy się pięcioma wynikami —
    po jednym na komponent. Wyznaczają kierunek pracy, ale są za szerokie na obserwację pogłębioną:
    „fałszywe przekonanie 1/10” nie mówi, którą z pięciu pozycji karty ćwiczymy w poniedziałek
    i po czym poznamy postęp. Ten druk rozpisuje tamte pięć wyników na <b>25 celów
    szczegółowych</b> — po jednym do każdej pozycji karty, każdy z zachowaniem, które widać,
    liczbą, którą da się policzyć, i terminem, w którym sprawdzamy.</div>
  <div class="dwie">
    <div class="karta-info"><h3>Jak czytać cel</h3>
      Każdy cel opisuje <b>krok mentalizacji, który widać</b> — to, co dziecko robi albo mówi,
      po czym poznajemy, że uwzględniło cudzą perspektywę. „Zrozumie, że inni myślą inaczej” nie
      jest celem: rozumienia nie da się zaobserwować ani policzyć. Dlatego pod celem stoi rozpisanie
      SMART: co dokładnie widać (S), ile tego liczymy (M), co to umożliwia (A), po co to dziecku (R)
      i kiedy sprawdzamy (T).</div>
    <div class="karta-info"><h3>Skąd kryterium i horyzont</h3>
      Nie z podręcznika, tylko z <b>wyniku tego komponentu u tego dziecka</b>. Uwaga: tu im wyżej,
      tym lepiej. Komponent z wynikiem 0–3 (znaczne trudności) jest priorytetem, więc sprawdzamy go
      najczęściej — po 4 tygodniach, przy kryterium 4 z 5. Wynik 4–7 (częściowo opanowane) —
      po 8 tygodniach, przy 4 z 5. Wynik 8–10 (zasób) — cel podtrzymujący, po 12 tygodniach,
      przy 3 z 5. Ta sama logika, co przy poziomach wsparcia w druku TOM-T.</div>
  </div>
  <table><thead><tr><th>Komponent</th><th>Wynik</th><th>Norma rozwojowa (typowy wiek)</th>
    <th>Pasmo</th><th>Kryterium</th><th>Horyzont</th><th>Znaczenie dla planu pracy</th></tr></thead>
    <tbody>{''.join(wiersze)}</tbody></table>
  <div class="uwagi">{e(dane['przelicznik_natezenia'])} — 5 komponentów × 5 pozycji × skala 0–2.
    Rozbieżność między normą rozwojową a wynikiem wskazuje, na których komponentach skupić pracę.</div>
  <table><thead><tr><th>Wynik komponentu</th><th>Pasmo</th><th>Kryterium</th><th>Horyzont</th>
    <th>Znaczenie</th></tr></thead><tbody>{progi}</tbody></table>
  <div class="uwagi"><b>Nie wszystkie 25 celów naraz.</b> Do planu bierzemy cele z komponentu
    priorytetowego i jeden–dwa z komponentu wymagającego wsparcia; 25 celów to zapas na cały rok,
    nie plan na wrzesień. <b>Kolejność jest rozwojowa</b>: komponenty IV i V mają sens dopiero
    po opanowaniu I–III. Wynik obserwacji wpisujemy w pole przy celu, a zbiorczo — w tabelę ewaluacji
    na ostatniej stronie.</div>
</div>
{stopka(1, ile, 'wprowadzenie')}
</section>"""


CELE_NA_STRONE = 3   # tyle bloków celu mieści się na A4 obok nagłówka komponentu


def strona_komponentu(z: dict, suma: int | None, prog: dict | None, uczen: str, grupa: str,
                  nr_strony: int, ile: int, wskazniki: list[dict] | None = None,
                  dalszy_ciag: bool = False) -> str:
    if prog is not None:
        bad = (f'{suma}/10 · <span class="ocena {klasa_oceny(prog["ocena"])}">{e(prog["ocena"])}</span>'
               f'<b>{e(prog["kryterium"])} sytuacji · {e(prog["horyzont"]["mianownik"])}</b>')
    else:
        bad = '……/10 · <span class="ocena">pasmo ………</span><b>…… z 5 · ……… tygodni</b>'
    cele = []
    for w in (wskazniki if wskazniki is not None else z["wskazniki"]):
        smart = "".join(f'<div><i>{e(s["litera"])}</i>{e(podstaw(s["tresc"], prog))}</div>'
                        for s in w["smart"])
        cele.append(f"""<article class="cel">
  <div class="cel-h"><span class="nr">{e(w['nr'])}</span>
    <span class="def"><b>Wskaźnik</b> {e(w['deficyt'])}</span></div>
  <p class="strat">krok mentalizacji: {e(w['krok_mentalizacji'])} · pozycja karty: {e(w['pozycja'])}</p>
  <p class="cel-t"><b>Cel SMART</b>{e(podstaw(w['cel'], prog))}</p>
  <div class="smart">{smart}</div>
  <div class="obs"><span><b>Obserwacja</b> {e(w['co_obserwowac'])} · {e(w['ile_sytuacji'])}</span>
    <span class="wynik">wynik <span class="pole">&nbsp;</span>/5 · data <span class="pole">&nbsp;</span></span></div>
</article>""")
    dopisek = ' <span style="font-size:9px;color:var(--szary)">· ciąg dalszy</span>' if dalszy_ciag else ""
    zasada = ("" if dalszy_ciag else
              f'<div class="si"><b>Zasada pracy nad teorią umysłu</b> {e(z["zasada_tom"])}</div>')
    return f"""<section class="strona">
{naglowek(f'Teoria umysłu · cele SMART · komponent {e(z["nr"])}', uczen, grupa)}
<div class="tresc">
  <div class="fn"><span class="rz">{e(z['nr'])}</span>
    <div><h2>{e(z['nazwa'])}{dopisek} <span style="font-size:9px;color:var(--szary)">{e(z['icf'])}</span></h2>
      <div class="op">{e(z['opis'])}</div></div>
    <div class="bad">{bad}</div></div>
  {zasada}
  {''.join(cele)}
</div>
{stopka(nr_strony, ile, f"komponent {z['nr']} · {z['nazwa'].lower()}")}
</section>"""


def strona_ewaluacji(dane: dict, uczen: str, grupa: str, ile: int) -> str:
    wiersze = "".join(
        f'<tr><td>{e(z["nr"])} · {e(z["nazwa"])}</td><td class="pkt">&nbsp;</td><td class="pkt">&nbsp;</td>'
        f'<td class="pkt">&nbsp;</td><td>&nbsp;</td></tr>'
        for z in dane["komponenty"])
    return f"""<section class="strona">
{naglowek('Teoria umysłu · ewaluacja', uczen, grupa)}
<div class="tresc">
  <div class="pas">Ewaluacja — postęp wg komponentów (0–10 pkt)</div>
  <div class="wstep">Minimum trzy pomiary: start (pierwsza obserwacja) · połowa okresu · koniec.
    Horyzont każdego komponentu bierze się z jego pasma — komponent priorytetowy sprawdzamy
    po 4 tygodniach, wymagający wsparcia po 8, zasób po 12. <b>Wzrost punktów nie jest jedynym
    wynikiem</b>: równie ważne jest to, na jakim poziomie wsparcia dziecko wykonuje krok
    mentalizacji — przejście z Poziomu III na II jest postępem także bez zmiany punktacji.</div>
  <table><thead><tr><th>Komponent</th><th>Start</th><th>Połowa okresu</th><th>Koniec</th>
    <th>Analiza zmiany</th></tr></thead><tbody>{wiersze}</tbody></table>
  <div class="dwie" style="margin-top:12px">
    <div class="karta-info"><h3>Wnioski z ewaluacji</h3>
      <div style="min-height:70px;border-bottom:1.5px dotted #b7add6"></div></div>
    <div class="karta-info"><h3>Decyzja — kontynuacja / modyfikacja planu pracy</h3>
      <div style="min-height:70px;border-bottom:1.5px dotted #b7add6"></div></div>
  </div>
  <div class="dwie" style="margin-top:12px">
    <div class="karta-info"><h3>Prowadzący obserwację · data i podpis</h3>
      <div style="min-height:46px;border-bottom:1.5px dotted #b7add6"></div></div>
    <div class="karta-info"><h3>Terapeuta SI / rodzic · data i podpis</h3>
      <div style="min-height:46px;border-bottom:1.5px dotted #b7add6"></div></div>
  </div>
  <div class="uwagi">{e(dane['modul']['podstawa_merytoryczna'])}<br><br>
    {'<br>'.join(e(x) for x in dane['modul']['podstawa_prawna'])}</div>
</div>
{stopka(ile, ile, 'ewaluacja')}
</section>"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Druk TOM-C — cele SMART do obserwacji pogłębionej")
    ap.add_argument("--uczen", default="", help="imię i nazwisko dziecka (dokument nie wchodzi do repo)")
    ap.add_argument("--grupa", default="", help="grupa przedszkolna")
    ap.add_argument("--wyniki", default="", help="5 wyników komponentów 0–10 po przecinku, w kolejności karty")
    args = ap.parse_args()

    if not DANE.exists():
        raise SystemExit(f"Brak {DANE}. Uruchom najpierw: python3 03_kod_zrodlowy/eksport_json.py")
    dane = json.loads(DANE.read_text(encoding="utf-8"))

    wyniki = None
    if args.wyniki:
        liczby = [int(x) for x in args.wyniki.replace(" ", "").split(",") if x != ""]
        if len(liczby) != 5:
            raise SystemExit("--wyniki wymaga dokładnie 5 liczb (5 komponentów), 0–10 każda.")
        if any(not 0 <= n <= 10 for n in liczby):
            raise SystemExit("Wynik komponentu mieści się w skali 0–10.")
        wyniki = dict(zip(KOLEJNOSC, liczby))

    # Komponent ma pięć wskaźników, a na A4 mieszczą się trzy bloki celu. Reszta
    # przechodzi na kolejną stronę z tym samym nagłówkiem i dopiskiem „ciąg dalszy” —
    # inaczej kartka rosłaby do 352 mm i drukarka dzieliła ją w przypadkowym miejscu.
    porcje = []
    for nr in KOLEJNOSC:
        z = next(x for x in dane["komponenty"] if x["nr"] == nr)
        w = z["wskazniki"]
        for k in range(0, len(w), CELE_NA_STRONE):
            porcje.append((z, nr, w[k:k + CELE_NA_STRONE], k > 0))

    ile = 2 + len(porcje)
    strony = [strona_wstepna(dane, wyniki, args.uczen, args.grupa, ile)]
    for i, (z, nr, czesc, dalej) in enumerate(porcje, start=2):
        suma = wyniki[nr] if wyniki else None
        prog = prog_dla(suma, dane["progi"]) if suma is not None else None
        strony.append(strona_komponentu(z, suma, prog, args.uczen, args.grupa, i, ile,
                                        wskazniki=czesc, dalszy_ciag=dalej))
    strony.append(strona_ewaluacji(dane, args.uczen, args.grupa, ile))

    nazwa = (f"uczen_{slug(args.uczen)}_TOM-C.html" if args.uczen
             else "Cele_SMART_TOM_obserwacja_poglebiona.html")
    wyjscie = KATALOG / nazwa
    KATALOG.mkdir(parents=True, exist_ok=True)
    tytul = ("Cele SMART · teoria umysłu"
             + (f" · {args.uczen}" if args.uczen else "") + " — EduPlaner 2026 · PCTP")
    wyjscie.write_text(
        f'<!DOCTYPE html>\n<html lang="pl">\n<head>\n<meta charset="UTF-8">\n'
        f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f"<title>{e(tytul)}</title>\n<style>{STYL}</style>\n</head>\n<body>\n"
        + "\n".join(strony) + "\n</body>\n</html>\n", encoding="utf-8")
    print(f"zapisano {wyjscie.relative_to(KORZEN)} ({wyjscie.stat().st_size // 1024} KB · {ile} stron)")
    if args.uczen:
        print("UWAGA: dokument zawiera dane osobowe dziecka — nie wchodzi do repozytorium "
              "(prefiks `uczen_` jest w .gitignore).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
