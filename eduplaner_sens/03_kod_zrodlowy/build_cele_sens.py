#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Druk SENS-C — 21 celów do obserwacji pogłębionej (profil sensoryczny).

    python3 03_kod_zrodlowy/build_cele_sens.py
    python3 03_kod_zrodlowy/build_cele_sens.py --uczen "Zofia Lewandowska" --grupa "Biedronki" \
            --wyniki 9,17,14,6,4,19,15

`--wyniki` to sumy siedmiu zmysłów z druku obserwacji (0–24, w kolejności:
wzrok, słuch, dotyk, smak, węch, propriocepcja, równowaga). Z nich biorą się
kryterium i horyzont każdego celu — dlatego pola `{proba}` i `{horyzont_*}`
podstawia się dopiero tutaj, a nie w banku.

DOKUMENTY Z NAZWISKIEM DZIECKA NIE WCHODZĄ DO REPOZYTORIUM — to dane osobowe.
Skrypt zapisuje je z prefiksem `uczen_`, który jest wpisany do .gitignore.
"""
from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wspolne_html as wh  # noqa: E402

KORZEN = pathlib.Path(__file__).resolve().parent.parent
DANE = KORZEN / "01_dane_json" / "cele_sens_obserwacja.json"
KATALOG = KORZEN / "02_gotowe_dokumenty"
KOLEJNOSC = ["wzrok", "sluch", "dotyk", "smak", "wech", "propriocepcja", "rownowaga"]


def e(t) -> str:
    return html.escape(str(t))


def slug(tekst: str) -> str:
    t = unicodedata.normalize("NFKD", tekst.replace("ł", "l").replace("Ł", "L"))
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-zA-Z0-9]+", "_", t).strip("_").lower()


def prog_dla(suma: int, progi: list[dict]) -> dict:
    for p in progi:
        if p["zakres_sumy"][0] <= suma <= p["zakres_sumy"][1]:
            return p
    raise SystemExit(f"Suma {suma} poza skalą 0–24.")


def podstaw(cel: str, prog: dict | None) -> str:
    if prog is None:
        return (cel.replace("{proba}", "……… z 5")
                   .replace("{horyzont_dopelniacz}", "……… tygodni")
                   .replace("{horyzont_miejscownik}", "……… tygodniach"))
    return (cel.replace("{proba}", prog["proba"])
               .replace("{horyzont_dopelniacz}", prog["horyzont"]["dopelniacz"])
               .replace("{horyzont_miejscownik}", prog["horyzont"]["miejscownik"]))


def strona_zmyslu(nazwa_zmyslu: str, cele: list[dict], suma: int | None, prog: dict | None,
                  uczen: str, grupa: str, numer: int, ile: int) -> str:
    z = cele[0]["zmysl"]
    natezenie = round(suma * 10 / 24) if suma is not None else None
    if prog is not None:
        podsumowanie = (f'<div class="box o"><b>Suma zmysłu: {suma} / 24</b> · natężenie '
                        f'<b>{natezenie} / 10</b> — {e(prog["pasmo"])}.<br>'
                        f'Kryterium dla wszystkich celów tego zmysłu: <b>{e(prog["proba"])}</b>, '
                        f'horyzont <b>{e(prog["horyzont"]["mianownik"])}</b>. '
                        f'Decyzja: {e(prog["decyzja"])}</div>')
    else:
        podsumowanie = ('<div class="box o"><b>Suma zmysłu: ……… / 24</b> · natężenie ……… / 10.<br>'
                        'Wpisz sumę z druku obserwacji, odczytaj pasmo z tabeli progów na stronie 1 '
                        'i wpisz kryterium oraz horyzont do celów poniżej.</div>')
    bloki = []
    for c in cele:
        bloki.append(f"""<div class="blk">{e(c['sektor']['nazwa'])} · {e(c['kierunek_txt'])}</div>
<div class="box"><b>{e(c['kod'])} — {e(c['nazwa'])}</b><br>
<b>Obserwowane objawy:</b> {e('; '.join(c['objawy_z_druku']))}<br>
<b>Strategia sensoryczna:</b> {e(c['strategia_sensoryczna'])}<br>
<b>Sygnał dziecka:</b> {e(c['sygnal_dziecka'])}</div>
<div class="dziecko"><b>CEL SMART:</b> {e(podstaw(c['cel'], prog))}</div>
<div class="doroslego"><b>Co liczymy:</b> {e(c['wskaznik_obserwacji'])} &nbsp;·&nbsp;
<b>Dieta sensoryczna:</b> {e('; '.join(c['dieta_sensoryczna']))}<br>
<b>Dostosowania:</b> {e('; '.join(c['dostosowania']))} &nbsp;·&nbsp;
<b>Uwaga:</b> {e(c['ryzyko'])}</div>
<div class="edit" contenteditable="true">notatka nauczyciela — kliknij i nadpisz…</div>""")
    return f"""<div class="sheet">
{wh.naglowek(f'Cele do obserwacji pogłębionej · {e(z["nazwa"])}', 'SENS-C', 'WOPF · SI · cele', uczen, grupa)}
<div class="sec"><div class="n">{e(z['rzymska'])}</div><h2>{e(z['nazwa'])}</h2><div class="line"></div>
  <span class="lvl I">{e(z['icf'])}</span></div>
{podsumowanie}
{''.join(bloki)}
{wh.stopka(numer, ile, 'SENS-C · cele do obserwacji')}
</div>"""


def strona_tytulowa(dane: dict, wyniki: dict | None, uczen: str, grupa: str, ile: int) -> str:
    progi = "".join(
        f'<tr><td><b>{p["zakres_sumy"][0]}–{p["zakres_sumy"][1]}</b></td><td>{e(p["natezenie"])}</td>'
        f'<td>{e(p["pasmo"])}</td><td><b>{e(p["proba"])}</b> · {e(p["horyzont"]["mianownik"])}</td>'
        f'<td>{e(p["decyzja"])}</td></tr>' for p in dane["progi"])
    if wyniki:
        wiersze = "".join(
            f'<tr><td>{e(dane["zmysly"][k]["rzymska"])}</td><td><b>{e(dane["zmysly"][k]["nazwa"])}</b></td>'
            f'<td>{wyniki[k]} / 24</td><td>{round(wyniki[k] * 10 / 24)} / 10</td>'
            f'<td>{e(prog_dla(wyniki[k], dane["progi"])["pasmo"])}</td></tr>' for k in KOLEJNOSC)
    else:
        wiersze = "".join(
            f'<tr><td>{e(dane["zmysly"][k]["rzymska"])}</td><td><b>{e(dane["zmysly"][k]["nazwa"])}</b></td>'
            f'<td>……… / 24</td><td>……… / 10</td><td>………</td></tr>' for k in KOLEJNOSC)
    return f"""<div class="sheet">
{wh.naglowek('Profil sensoryczny · cele do obserwacji pogłębionej', 'SENS-C', 'WOPF · SI · cele', uczen, grupa)}
<div class="sec"><div class="n p">I</div><h2>O druku</h2><div class="line"></div></div>
<div class="box"><b>Zasada modułu.</b> {e(dane['modul']['zasada_modulu'])}</div>
<div class="note">{e(dane['jak_liczyc_kryterium'])}</div>

<div class="sec"><div class="n">II</div><h2>Wyniki obserwacji — 7 zmysłów</h2><div class="line"></div></div>
<table class="tbl"><thead><tr><th style="width:8%">LP.</th><th style="width:24%">Zmysł</th>
<th style="width:14%">Suma 0–24</th><th style="width:14%">Natężenie 0–10</th><th>Pasmo</th></tr></thead>
<tbody>{wiersze}</tbody></table>

<div class="sec"><div class="n">III</div><h2>Progi — skąd kryterium i horyzont</h2><div class="line"></div></div>
<div class="note">{e(dane['przelicznik_natezenia'])}</div>
<table class="tbl"><thead><tr><th style="width:11%">Suma</th><th style="width:11%">Natężenie</th>
<th style="width:26%">Pasmo</th><th style="width:16%">Kryterium · horyzont</th><th>Decyzja</th></tr></thead>
<tbody>{progi}</tbody></table>

<div class="sec"><div class="n">IV</div><h2>Podstawa</h2><div class="line"></div></div>
<div class="box">{e(dane['modul']['podstawa_merytoryczna'])}<br><br>
{'<br>'.join(e(x) for x in dane['modul']['podstawa_prawna'])}</div>
{wh.stopka(1, ile, 'SENS-C · cele do obserwacji')}
</div>"""


def main() -> int:
    ap = argparse.ArgumentParser(description="Druk SENS-C — cele do obserwacji pogłębionej")
    ap.add_argument("--uczen", default="", help="imię i nazwisko dziecka (dokument nie wchodzi do repo)")
    ap.add_argument("--grupa", default="", help="grupa przedszkolna")
    ap.add_argument("--wyniki", default="", help="7 sum zmysłów 0–24 po przecinku, w kolejności druku")
    args = ap.parse_args()

    if not DANE.exists():
        raise SystemExit(f"Brak {DANE}. Uruchom najpierw: python3 03_kod_zrodlowy/eksport_json.py")
    dane = json.loads(DANE.read_text(encoding="utf-8"))

    wyniki = None
    if args.wyniki:
        liczby = [int(x) for x in args.wyniki.replace(" ", "").split(",") if x != ""]
        if len(liczby) != 7:
            raise SystemExit("--wyniki wymaga dokładnie 7 liczb (7 zmysłów), 0–24 każda.")
        if any(not 0 <= n <= 24 for n in liczby):
            raise SystemExit("Każda suma zmysłu mieści się w skali 0–24.")
        wyniki = dict(zip(KOLEJNOSC, liczby))

    wg_zmyslu: dict[str, list[dict]] = {}
    for c in dane["cele"]:
        c["kierunek_txt"] = dane["sektory"][c["sektor"]["klucz"]]["kierunek"]
        wg_zmyslu.setdefault(c["zmysl"]["klucz"], []).append(c)

    ile = len(KOLEJNOSC) + 1
    arkusze = [strona_tytulowa(dane, wyniki, args.uczen, args.grupa, ile)]
    for i, klucz in enumerate(KOLEJNOSC, start=2):
        suma = wyniki[klucz] if wyniki else None
        prog = prog_dla(suma, dane["progi"]) if suma is not None else None
        arkusze.append(strona_zmyslu(klucz, wg_zmyslu[klucz], suma, prog, args.uczen, args.grupa, i, ile))

    nazwa = f"uczen_{slug(args.uczen)}_SENS-C.html" if args.uczen else "sens_cele_SENS-C.html"
    wyjscie = KATALOG / nazwa
    KATALOG.mkdir(parents=True, exist_ok=True)
    wyjscie.write_text(
        wh.dokument(f"Profil sensoryczny · cele SMART{' · ' + args.uczen if args.uczen else ''} "
                    f"— EduPlaner 2026 · PCTP", arkusze), encoding="utf-8")
    print(f"zapisano {wyjscie.relative_to(KORZEN)} ({wyjscie.stat().st_size // 1024} KB · {ile} stron)")
    if args.uczen:
        print("UWAGA: dokument zawiera dane osobowe dziecka — nie wchodzi do repozytorium "
              "(prefiks `uczen_` jest w .gitignore).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
