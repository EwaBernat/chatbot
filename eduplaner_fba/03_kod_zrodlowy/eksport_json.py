#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Moduł FBA/PBS w kształcie, którego używają pozostałe moduły EduPlanera.

    python3 eduplaner_fba/03_kod_zrodlowy/eksport_json.py

Autorka oddała moduł FBA jako paczkę z własnym eksportem JSON — starszym niż
kształt, do którego doszły SENS, ToM i MOWA. Treść jest ta sama i nie wolno jej
tu zmieniać: ten skrypt tylko dokłada pola, których nowsze druki potrzebują,
i wyprowadza wynik do 01_dane_json/.

Oryginał autorki leży obok, w zrodlo_autorki/json/. To on jest źródłem — gdy
przyśle nowszą paczkę, podmienia się tamte pliki i uruchamia ten skrypt.
Ręczna poprawka w 01_dane_json/ zniknie przy najbliższym eksporcie.

Czego brakowało i skąd to biorę:

  modul                metryka druku — z README paczki i skilla cele-fba-pbs
  poziomy.rzym         III / II / I — z nazwy poziomu
  poziomy.kolor_oceny  czerwona / żółta / zielona — kolejność jak w banku
  wersje.czas/forma    z konspektów tej wersji; są tam i tak, tylko per konspekt
  wskaznik.pozycja     numer w obrębie funkcji, z numeru wskaźnika
  konspekt.obszar      to samo, co jej „funkcja” — nowsze druki czytają „obszar”
  konspekt.zasada_pbs  z opisu funkcji w druku FBA-C; wchodzi w drugą ramkę
                       konspektu, tam gdzie inne moduły mają „bezpieczeństwo”
  arkusz.format        A4 pionowo — jedyny format arkuszy w tym module
"""
from __future__ import annotations

import json
import pathlib
import re

KORZEN = pathlib.Path(__file__).resolve().parent.parent
ZRODLO = KORZEN / "03_kod_zrodlowy" / "zrodlo_autorki" / "json"
WYJSCIE = KORZEN / "01_dane_json"

RZYM_POZIOMU = {"p3": "III", "p2": "II", "p1": "I"}
KOLOR_OCENY = {"p3": "czerwona", "p2": "żółta", "p1": "zielona"}

MODUL = {
    "nazwa": "Analiza funkcjonalna zachowania i plan pozytywnego wsparcia (FBA/PBS)",
    "kod": "FBA",
    "wersja": "2026",
    "autorka": "mgr Mirosława Ewa Jurczyszyn, pedagog specjalny, PCTP Koszalin",
    "aplikacja": "EduPlaner 2026",
    "druk_zrodlowy": "Kwestionariusz funkcji zachowania — przedszkole",
    "podstawa_merytoryczna": "Analiza funkcjonalna zachowania (FBA) i plan pozytywnego "
                             "wsparcia zachowań (PBS); ICF-CY",
    "podstawa_prawna": "Rozporządzenie MEN z 9 sierpnia 2017 r. w sprawie warunków "
                       "organizowania kształcenia, wychowania i opieki dla dzieci "
                       "i młodzieży niepełnosprawnych",
    "zasada_modulu": (
        "Cel opisuje zachowanie zastępcze, nie brak zachowania trudnego. Plan PBS "
        "uczy innej drogi do tej samej potrzeby, zamiast tę potrzebę dziecku odbierać. "
        "„Nie będzie uciekał od stolika” nie jest celem z tego modułu; „poprosi "
        "o przerwę kartą, zanim wyjdzie od stolika” — jest."
    ),
    "granica_kompetencji": (
        "Ten moduł jest dla nauczyciela i pedagoga prowadzącego plan wsparcia w grupie. "
        "Zachowania z ryzykiem urazu, autoagresja i agresja wymagająca interwencji fizycznej "
        "NIE MAJĄ TU CELÓW — przy nich plan pisze zespół z udziałem psychologa, "
        "a nauczyciel prowadzi rejestr ABC i zgłasza rzecz zespołowi."
    ),
}


def wczytaj(nazwa: str) -> dict:
    return json.loads((ZRODLO / f"{nazwa}.json").read_text(encoding="utf-8"))


def zapisz(nazwa: str, dane: dict) -> int:
    WYJSCIE.mkdir(parents=True, exist_ok=True)
    p = WYJSCIE / f"{nazwa}.json"
    p.write_text(json.dumps(dane, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return p.stat().st_size


def najczestsze(wartosci: list[str]) -> str:
    from collections import Counter
    return Counter(wartosci).most_common(1)[0][0] if wartosci else ""


def main() -> int:
    poziomy = wczytaj("cele_fba_poziomy")
    kons = wczytaj("konspekty_fba")
    pomoce = wczytaj("pomoce_fba")
    materialy = wczytaj("materialy_do_druku")
    obserwacja = wczytaj("cele_fba_obserwacja")
    kontrakt = wczytaj("wlasne_konspekty_kontrakt")

    zasady = {f["nr"]: f.get("zasada_pbs", "") for f in obserwacja["funkcje"]}
    opisy = {f["nr"]: f.get("opis", "") for f in obserwacja["funkcje"]}

    # ——— cele wiek × poziom ——————————————————————————————————————————
    for p in poziomy["poziomy_wsparcia"]:
        p["rzym"] = RZYM_POZIOMU[p["klucz"]]
        p["kolor_oceny"] = KOLOR_OCENY[p["klucz"]]
    for wer in poziomy["wersje_wiekowe"]:
        swoje = [k for k in kons["konspekty"] if k["wersja_wiekowa"] == wer["klucz"]]
        wer["czas"] = najczestsze([k["czas"] for k in swoje])
        wer["forma"] = najczestsze([k["forma"] for k in swoje])
        wer["cykl"] = najczestsze([k["cykl"] for k in swoje])
    # ICF i punkty podstawy programowej stoją w linii sfery każdego konspektu —
    # „(ICF d210·d240 · PP 2.6·2.11)”. Nowsze druki chcą ich osobno, w nagłówku
    # funkcji, więc wyjmuję je stamtąd zamiast przepisywać ręcznie.
    kody = {}
    for k in kons["konspekty"]:
        m = re.search(r"\(ICF ([^·]+(?:·[^ ]+)*) · PP ([^)]+)\)", k.get("sfera", ""))
        if m:
            kody.setdefault(k["wskaznik"].split(".")[0], (m.group(1).strip(), m.group(2).strip()))

    for f in poziomy["funkcje"]:
        f["icf"], f["pp"] = kody.get(f["nr"], ("", ""))
        f["opis"] = opisy.get(f["nr"], "")
        f["zasada_pbs"] = zasady.get(f["nr"], "")
        for i, w in enumerate(f["wskazniki"], 1):
            w["pozycja"] = i
            # W ramce pod tytułem konspektu stoi opis funkcji — po co dziecko to
            # robi i kiedy zachowanie się nasila. Zasada PBS ma własne miejsce
            # na dole konspektu, więc powtarzanie jej tutaj nic nie wnosi.
            w.setdefault("opis_kroku", f["opis"])
    poziomy["modul"] = MODUL
    poziomy["liczba_celow"] = sum(len(w["cele"]) * 3 for f in poziomy["funkcje"]
                                  for w in f["wskazniki"])
    poziomy["rodzaje_zajec"] = sorted({k["rodzaj_zajec"] for k in kons["konspekty"]})
    poziomy["tory_zajec"] = poziomy["rodzaje_zajec"]

    # ——— konspekty ———————————————————————————————————————————————————
    pozycje = {w["nr"]: w["pozycja"] for f in poziomy["funkcje"] for w in f["wskazniki"]}
    for k in kons["konspekty"]:
        k["obszar"] = k.get("funkcja", "")
        k["pozycja"] = pozycje.get(k["wskaznik"], 0)
        k["zasada_pbs"] = zasady.get(k["wskaznik"].split(".")[0], "")

    # ——— pomoce i arkusze ————————————————————————————————————————————
    tytuly = {a["wskaznik"]: a["tytul"] for a in materialy["arkusze"]}
    for p in pomoce["pomoce"]:
        p["obszar"] = next((k["obszar"] for k in kons["konspekty"]
                            if k["wskaznik"] == p["wskaznik"]), "")
        p["pozycja"] = pozycje.get(p["wskaznik"], 0)
        p["arkusz_id"] = p["wskaznik"] if p["wskaznik"] in tytuly else None
        p.setdefault("historyjka", None)
    for a in materialy["arkusze"]:
        a["format"] = "A4 pionowo"
        a.setdefault("historyjka", None)

    obserwacja["modul"] = MODUL

    ile = {
        "cele_fba_poziomy": zapisz("cele_fba_poziomy", poziomy),
        "konspekty_fba": zapisz("konspekty_fba", kons),
        "pomoce_fba": zapisz("pomoce_fba", pomoce),
        "materialy_do_druku": zapisz("materialy_do_druku", materialy),
        "cele_fba_obserwacja": zapisz("cele_fba_obserwacja", obserwacja),
        "wlasne_konspekty_kontrakt": zapisz("wlasne_konspekty_kontrakt", kontrakt),
    }
    for nazwa, bajty in ile.items():
        print(f"  01_dane_json/{nazwa}.json  {bajty // 1024} KB")
    print(f"\n{poziomy['liczba_celow']} celów · {len(kons['konspekty'])} konspektów · "
          f"{len(pomoce['pomoce'])} pomocy · {len(materialy['arkusze'])} arkuszy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
