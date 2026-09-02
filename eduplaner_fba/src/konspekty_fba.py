# -*- coding: utf-8 -*-
"""Konspekty zajęć do wszystkich wskaźników tabeli FBA-T — wzór druku KC-3.

**75 konspektów**: 25 wskaźników kwestionariusza funkcji × 3 wersje wiekowe.
Jeden konspekt obsługuje trzy poziomy wsparcia — tak samo jak w banku KPOF,
gdzie poziom zmienia nie cel, tylko sekcję VI (modyfikacje). Klucz to para
`(wskaźnik, wersja)`, np. `("I.1", "A")`.

Treść leży w pięciu modułach, po jednym na funkcję zachowania
(`konspekty_fba_1.py` … `_5.py`) — tak jak bank trzyma konspekty w module na
wersję i obszar. Pięć plików zamiast jednego dlatego, że przy dopisywaniu widać
w diffie jedną funkcję, a nie 3000 linii.

Co skąd się bierze:

* **rdzeń** (`RDZEN[wskaźnik]`) — to, co nie zmienia się z wiekiem: tytuł,
  ICF i punkty podstawy, metody, wskazówka dla prowadzącego, rejestr
  obserwacji, materiał do wydruku i sposób modyfikowania zadania.
* **wariant** (`WARIANTY[(wskaźnik, wersja)]`) — to, co się zmienia: cel
  terapeutyczny, przebieg zajęć w parach N/D, pomoc charakterystyczna dla wieku.
* **cel edukacyjny** — nie leży tu w ogóle. Konspekt czyta go **na żywo
  z tabeli** (`dane_poziomy.py`), więc poprawka w banku celów nie zostawia
  w konspekcie nieaktualnej kopii.
* **modyfikacje** — składane z komórek tabeli: Poziom III to warunki z kolumny
  III, Poziom I z kolumny I. Konspekt i tabela nie mogą się rozjechać, bo mówią
  tym samym zdaniem.
* **kryterium i horyzont** — z poziomu wsparcia (III — 3 z 5 i 4 tygodnie,
  II — 4 z 5 i 8 tygodni, I — 4 z 5 i 12 tygodni).
"""

import dane_poziomy as P
import konspekty_fba_1 as F1
import konspekty_fba_2 as F2
import konspekty_fba_3 as F3
import konspekty_fba_4 as F4
import konspekty_fba_5 as F5

# Profil wieku: czas, forma i cykl zajęć. To nie jest treść konspektu, tylko
# ramy organizacyjne grupy — dlatego stoją raz, a nie 75 razy. Wariant może je
# nadpisać (np. runda w grupie ma sens także u trzylatków).
WIEK = {
    "A": dict(wiek="3–4 lata", czas="10 min", forma="para z nauczycielem", cykl="4× w tygodniu"),
    "B": dict(wiek="5 lat", czas="15 min", forma="mała grupa (3–4 dzieci)", cykl="3× w tygodniu"),
    "C": dict(wiek="6 lat", czas="20 min", forma="mała grupa (4–6 dzieci)", cykl="3× w tygodniu"),
}

RDZEN = {}
WARIANTY = {}
for _m in (F1, F2, F3, F4, F5):
    RDZEN.update(_m.RDZEN)
    WARIANTY.update(_m.WARIANTY)

# Wskaźnik → funkcja, żeby konspekt wiedział, do której funkcji zachowania należy.
FUNKCJA = {f"{rzym}.{i}": (rzym, f["nazwa"], wsk)
           for rzym, f in P.CELE.items()
           for i, wsk in enumerate(f["wskazniki"], 1)}


def klucze():
    """Wszystkie pary (wskaźnik, wersja) w kolejności tabeli."""
    return [(nr, w) for nr in FUNKCJA for w, _ in P.WERSJE if (nr, w) in WARIANTY]


def kid(nr, wersja):
    """Identyfikator modalu — bez kropki, bo trafia do CSS i do `getElementById`."""
    return f"kon-{wersja}-{nr.replace('.', '-')}"


def konspekt(nr, wersja):
    """Gotowy konspekt: rdzeń + wariant + to, co wynika z tabeli i z wieku."""
    r, w = RDZEN[nr], WARIANTY[(nr, wersja)]
    rzym, nazwa_funkcji, wsk = FUNKCJA[nr]
    poz3, poz2, poz1 = wsk[wersja]

    # Sekcja VI: warunki zadania wprost z kolumn tabeli plus sposób modyfikowania
    # z rdzenia. Nauczyciel czyta w konspekcie to samo zdanie, które ma w banku.
    mody = {}
    for kod, tekst, dodatek in (("p3", poz3, r["mod"][0]),
                                ("p2", poz2, r["mod"][1]),
                                ("p1", poz1, r["mod"][2])):
        mody[kod] = [tekst + " — cel z kolumny tabeli", dodatek]

    ram = WIEK[wersja].copy()
    for pole in ("czas", "forma", "cykl"):
        if w.get(pole):
            ram[pole] = w[pole]

    return dict(
        nr=nr, wersja=wersja, kid=kid(nr, wersja),
        funkcja=f"{rzym} · {nazwa_funkcji}", zastepcze=wsk["zastepcze"],
        wskaznik_tresc=wsk["wskaznik"],
        tytul=r["tytul"], podtytul=w["podtytul"],
        sfera=(f'FUNKCJA {rzym} · {nazwa_funkcji.upper()} · zachowanie zastępcze: '
               f'{wsk["zastepcze"]} (ICF {r["icf"]} · PP {r["pp"]})'),
        rodzaj=r["rodzaj"], metody=r["metody"], wskazowka=r["wskazowka"],
        ter_kryt=r["ter_kryt"], arkusz=r["arkusz"],
        pomoce=[w["pomoc_wiek"]] + r["pomoce"],
        przebieg=w["przebieg"], ter=w["ter"],
        ter_smart=[
            ("S", w["S"]),
            ("M", "Kryterium z klikniętego poziomu wsparcia — 3 z 5 albo 4 z 5 sytuacji."),
            ("A", w["A"]),
            ("R", r["R"]),
            ("T", "Ewaluacja w horyzoncie poziomu: 4, 8 albo 12 tygodni."),
        ],
        mody=mody, **ram)


def stan():
    """(rdzeni, wariantów, brakujących par) — kontrola po dopisaniu treści."""
    braki = [(nr, w) for nr in FUNKCJA for w, _ in P.WERSJE if (nr, w) not in WARIANTY]
    return len(RDZEN), len(WARIANTY), braki
