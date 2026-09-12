#!/usr/bin/env python3
"""Buduje interaktywny film z oryginalnego druku „Ocena Funkcjonalna” (EduPlaner 2026).

Wejście:  film/zrodlo/Raport_Oceny_Funkcjonalnej_9.html  (oryginalny druk, 28 stron)
Wyjście:  film/ocena_funkcjonalna_film.html               (film: druk + silnik animacji)

Film zachowuje oryginalny CSS i markup druku. Silnik dokłada:
  * oś czasu ze scenami (każda scena = akapit narracji z film/narracja.txt),
  * kamerę (najazd na wypełniane pole), wpisywanie tekstu, ptaszki, paski, podpisy,
  * awatar (koło / pełny ekran) na film MP4 z HeyGen,
  * głos (MP3 z ElevenLabs) i napisy (SRT) — wczytywane w przeglądarce,
  * karty „§ podstawa prawna” i zdjęcia dla każdej sceny,
  * sterowanie (odtwarzanie, suwak, rozdziały, klawiatura) i tryb ?remotion=1 dla renderu MP4.

Uruchom:  python3 film/build_film.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

TU = Path(__file__).resolve().parent
ZRODLO = TU / "zrodlo" / "Raport_Oceny_Funkcjonalnej_9.html"
NARRACJA = TU / "narracja.txt"
WYJSCIE = TU / "ocena_funkcjonalna_film.html"

# ----------------------------------------------------------------------------
# Dane przykładowe (fikcyjne) wpisywane do druku
# ----------------------------------------------------------------------------
D = {
    "placowka": "Przedszkole nr 7 „Pod Tęczą” w Koszalinie",
    "placowka_krotko": "Przedszkole nr 7 „Pod Tęczą”",
    "adres": "ul. Słoneczna 12, 75-001 Koszalin · tel. 94 000 00 00 · sekretariat@przyklad.pl",
    "dziecko": "Antoni Nowak",
    "grupa": "„Sówki” · 5-latki",
    "data": "15.09.2026",
    "data_ur": "12.04.2021",
    "oddzial": "Przedszkole nr 7 „Pod Tęczą” w Koszalinie, grupa „Sówki” (5-latki)",
    "zespol": [
        "Ewa Malinowska – pedagog specjalny, koordynator Zespołu",
        "Anna Kowalczyk – wychowawca grupy",
        "Katarzyna Zielińska – psycholog",
        "Marta Wiśniewska – logopeda",
        "Piotr Lewandowski – terapeuta integracji sensorycznej",
        "Joanna Nowak – rodzic",
    ],
    "orzeczenie": "Orzeczenie o potrzebie kształcenia specjalnego",
    "nr": "PPP-1.4123.15.2026",
    "data_orz": "14.05.2026",
    "poradnia": "Poradnia Psychologiczno-Pedagogiczna nr 1 w Koszalinie",
    "z_uwagi": "autyzm",
    "miejscowosc": "Koszalin",
    "data_opinii": "18.09.2026",
    "znak": "P7.4131.3.2026",
    "rodzice": "Joanna i Marek Nowak, ul. Leśna 4/2, 75-001 Koszalin",
}

# ----------------------------------------------------------------------------
# Scenariusz: 16 scen = 16 akapitów narracji. Czas kroków w ułamkach sceny (f, fd).
# strona = numer strony druku (1–28). Selektory działają wewnątrz tej strony.
# ----------------------------------------------------------------------------
PRAWO = {
    "428": {"akt": "Rozp. MEN z 2.03.2026 – orzeczenia i opinie", "dz": "Dz. U. 2026 poz. 428"},
    "po": {"akt": "Prawo oświatowe – art. 127", "dz": "Dz. U. 2024 poz. 737"},
    "ks": {"akt": "Rozp. MEN z 9.08.2017 – kształcenie specjalne", "dz": "Dz. U. 2020 poz. 1309"},
    "ppp": {"akt": "Rozp. MEN z 9.08.2017 – pomoc psych.-ped.", "dz": "Dz. U. 2023 poz. 1798"},
    "pp": {"akt": "Rozp. MEN z 11.03.2026 – nowa podstawa programowa", "dz": "Dz. U. 2026 poz. 378"},
    "icf": {"akt": "ICF – klasyfikacja WHO", "dz": "model 2026/27"},
    "rodo": {"akt": "RODO – art. 9 (dane o zdrowiu)", "dz": "Dz. Urz. UE L 119"},
}


def p(klucz, co):
    return {**PRAWO[klucz], "co": co}


SCENY = [
    {  # 0 · intro Ewy PCTP – klip ze skilla awatar-ewa (jej twarz, jej głos), stała długość klipu
        "id": "powitanie", "tytul": "Ewa PCTP wita", "strona": 1, "awatar": "full", "intro": True, "dur_stala": 13.0,
        "foto": "zespol",
        "ekran": {"nad": "EduPlaner 2026 · PCTP Koszalin", "tytul": "Dzień dobry, mam na imię Ewa", "pod": "Twoja przewodniczka po systemie EduPlaner 2026"},
        "prawo": [],
        "kroki": [],
    },
    {  # 1
        "id": "intro", "tytul": "Jak powstaje raport", "strona": 1, "awatar": "full", "foto": "klocki",
        "ekran": {"nad": "EduPlaner 2026 · Ocena Funkcjonalna", "tytul": "Jak powstaje raport", "pod": "opinia · WOPF · IPET na jednym druku, od 1 września 2026"},
        "prawo": [p("428", "§ 7 ust. 6–7 obowiązuje od 1.09.2026")],
        "kroki": [],
    },
    {  # 2
        "id": "okladka", "tytul": "Okładka i Zespół", "strona": 1, "foto": "zespol",
        "prawo": [p("po", "rodzic uczestniczy w pracach Zespołu"), p("rodo", "dokument poufny – dane o zdrowiu")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": ".hdr", "pad": 40},
            {"f": 0.02, "fd": 0.14, "typ": "wpisz", "sel": ".hdr .name", "teksty": [D["placowka"]]},
            {"f": 0.12, "fd": 0.20, "typ": "kamera", "sel": ".fields", "pad": 30},
            {"f": 0.16, "fd": 0.22, "typ": "wpisz", "sel": ".fields .field span", "teksty": [D["dziecko"], D["grupa"], D["data"]]},
            {"f": 0.38, "fd": 0.10, "typ": "wpisz", "sel": ".date-line .fill", "teksty": [D["data"]]},
            {"f": 0.40, "fd": 0.20, "typ": "kamera", "sel": ".ed", "pad": 24},
            {"f": 0.46, "fd": 0.08, "typ": "zaznacz", "sel": "#ed-grid [data-ed='01']"},
            {"f": 0.56, "fd": 0.20, "typ": "kamera", "sel": ".team", "pad": 30},
            {"f": 0.60, "fd": 0.36, "typ": "wpisz", "sel": ".team li span", "teksty": D["zespol"]},
        ],
    },
    {  # 3
        "id": "prawo", "tytul": "Podstawy prawne", "strona": 3, "foto": "podpis",
        "prawo": [p("428", "§ 7 – opinia, 7 elementów, obszary ICF"), p("po", "kształcenie specjalne, IPET, WOPF"),
                  p("ks", "§ 6 treść IPET · § 7 dodatkowa osoba"), p("ppp", "formy pomocy · 45 min"),
                  p("pp", "cele dostosowuje się, nie obniża"), p("icf", "domeny d1–d9, KPOF / KSzOF"), p("rodo", "poufność")],
        "kroki": [
            {"f": 0.00, "fd": 0.25, "typ": "kamera", "sel": "table.grid", "pad": 6, "zoom": 1.3},
            {"f": 0.04, "fd": 0.60, "typ": "pokaz", "sel": "table.grid tr"},
            {"f": 0.10, "fd": 0.30, "typ": "kamera", "sel": "table.grid tr:nth-child(2)", "pad": 16, "zoom": 1.55},
            {"f": 0.50, "fd": 0.40, "typ": "kamera", "sel": "table.grid", "pad": 6, "zoom": 1.3},
        ],
    },
    {  # 4
        "id": "czytanie", "tytul": "Jak czytać raport", "strona": 2, "foto": "zespol",
        "prawo": [p("428", "Część I–II = opinia placówki"), p("ks", "Część III = elementy IPET")],
        "kroki": [
            {"f": 0.00, "fd": 0.25, "typ": "kamera", "sel": ".flow5", "pad": 30},
            {"f": 0.04, "fd": 0.45, "typ": "pokaz", "sel": ".flow5 > div"},
            {"f": 0.55, "fd": 0.25, "typ": "kamera", "sel": ".varbox", "pad": 30},
            {"f": 0.58, "fd": 0.30, "typ": "pokaz", "sel": ".varbox > div"},
        ],
    },
    {  # 5
        "id": "metryczka", "tytul": "1 · Metryczka i procedura", "strona": 4, "foto": "klocki",
        "prawo": [p("428", "§ 7 ust. 6 pkt 1–2 – data i dane dziecka"), p("po", "art. 127 ust. 3 – orzeczenie z poradni")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": "table.meta", "pad": 20},
            {"f": 0.02, "fd": 0.30, "typ": "wpisz", "sel": "table.meta .ph",
             "teksty": [D["dziecko"], D["data_ur"], D["oddzial"], D["orzeczenie"], D["nr"], D["data_orz"], D["poradnia"], D["z_uwagi"], "", "Nie dotyczy"]},
            {"f": 0.30, "fd": 0.20, "typ": "kamera", "sel": "table.meta tr:nth-child(4)", "pad": 24, "zoom": 1.5},
            {"f": 0.40, "fd": 0.06, "typ": "zaznacz", "sel": "table.meta tr:nth-child(4) .opt:nth-child(1)"},
            {"f": 0.48, "fd": 0.06, "typ": "zaznacz", "sel": "table.meta tr:nth-child(6) .opt:nth-child(1)"},
            {"f": 0.58, "fd": 0.22, "typ": "kamera", "sel": ".flow", "pad": 26},
            {"f": 0.62, "fd": 0.30, "typ": "pokaz", "sel": ".flow .step"},
            {"f": 0.86, "fd": 0.14, "typ": "pokaz", "sel": ".icf div"},
        ],
    },
    {  # 6
        "id": "narzedzia", "tytul": "3 · Narzędzia obserwacji", "strona": 5, "foto": "aac",
        "prawo": [p("428", "§ 8 ust. 2 pkt 2 – funkcje i struktury ciała"), p("icf", "profil, ABC, sensoryka, mowa, ToM")],
        "kroki": [
            {"f": 0.00, "fd": 0.25, "typ": "kamera", "sel": ".tools", "pad": 20},
            {"f": 0.05, "fd": 0.85, "typ": "pokaz", "sel": ".tools .tool"},
        ],
    },
    {  # 7
        "id": "funkcjonowanie", "tytul": "4 · Funkcjonowanie: 5 obszarów (przedszkole) i 7 (uczeń)", "strona": 6, "foto": "klocki",
        "prawo": [p("428", "§ 7 ust. 6 pkt 3 · ust. 7 pkt 1 lit. a – 5 obszarów"), p("ks", "§ 6 ust. 10 – WOPF")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.02, "fd": 0.50, "typ": "wpisz", "sel": "table.grid td.plus, table.grid td.minus"},
            {"f": 0.28, "fd": 0.20, "typ": "kamera", "sel": "table.grid tr:nth-child(3)", "pad": 20, "zoom": 1.45},
            {"f": 0.60, "fd": 0.00, "typ": "strona", "nr": 7},
            {"f": 0.60, "fd": 0.20, "typ": "kamera", "strona": 7, "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.61, "fd": 0.38, "typ": "wpisz", "strona": 7, "sel": "table.grid td.plus, table.grid td.minus"},
        ],
    },
    {  # 8
        "id": "liczby", "tytul": "5 · Wyniki liczbowe KPOF", "strona": 8, "foto": "sluchawki",
        "prawo": [p("428", "§ 7 ust. 6 pkt 4 – aktualna WOPF"), p("icf", "9 domen · skala 0–5 · KPOF bez stenów")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": ".stats", "pad": 30},
            {"f": 0.04, "fd": 0.18, "typ": "licz", "sel": ".stats .stat:nth-child(2) .v", "do": 68, "wzor": "{n} <small>/ 180 pkt</small>"},
            {"f": 0.20, "fd": 0.14, "typ": "licz", "sel": ".stats .stat:nth-child(3) .v", "do": 2.1, "dec": 1, "wzor": "Śr: {n} <small>w skali 0–5</small>"},
            {"f": 0.34, "fd": 0.08, "typ": "wpisz", "sel": ".stats .stat.warn .v", "teksty": ["Poziom 2 (Umiarkowany)"]},
            {"f": 0.42, "fd": 0.25, "typ": "kamera", "sel": "table.grid", "pad": 14, "zoom": 1.2},
            {"f": 0.44, "fd": 0.30, "typ": "pokaz", "sel": "table.grid tr"},
            {"f": 0.50, "fd": 0.40, "typ": "pasek", "sel": "table.grid .meter i"},
            {"f": 0.80, "fd": 0.20, "typ": "kamera", "sel": "table.grid tr:nth-child(5)", "pad": 20, "zoom": 1.5},
        ],
    },
    {  # 9
        "id": "arkusze", "tytul": "6 · Arkusze specjalistyczne", "strona": 9, "foto": "sluchawki",
        "prawo": [p("428", "§ 7 ust. 6 – wyniki działań diagnostycznych"), p("428", "§ 8 ust. 2 pkt 2 – funkcje ciała")],
        "kroki": [
            {"f": 0.00, "fd": 0.22, "typ": "kamera", "sel": ".res:nth-of-type(1)", "pad": 24, "zoom": 1.3},
            {"f": 0.02, "fd": 0.90, "typ": "pokaz", "sel": ".res"},
            {"f": 0.20, "fd": 0.22, "typ": "kamera", "sel": ".res:nth-of-type(2)", "pad": 24, "zoom": 1.3},
            {"f": 0.48, "fd": 0.22, "typ": "kamera", "sel": ".res:nth-of-type(3)", "pad": 24, "zoom": 1.3},
            {"f": 0.72, "fd": 0.22, "typ": "kamera", "sel": ".res:nth-of-type(5)", "pad": 24, "zoom": 1.3},
        ],
    },
    {  # 10
        "id": "glos", "tytul": "7 · Mój głos", "strona": 10, "foto": "aac",
        "prawo": [p("428", "§ 8 ust. 3 pkt 3 – informacje od dziecka"), p("icf", "czynniki osobowe · podmiotowość")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": ".cbl", "pad": 24, "zoom": 1.3},
            {"f": 0.02, "fd": 0.22, "typ": "zaznacz", "sel": ".cbl:nth-of-type(1) .cb[data-on]", "stagger": 1},
            {"f": 0.24, "fd": 0.22, "typ": "kamera", "sel": ".voice", "pad": 20, "zoom": 1.25},
            {"f": 0.26, "fd": 0.46, "typ": "wpisz", "sel": ".voice .box p"},
            {"f": 0.72, "fd": 0.18, "typ": "kamera", "sel": ".mood", "pad": 30, "zoom": 1.5},
            {"f": 0.74, "fd": 0.14, "typ": "zaznacz", "sel": ".cbl:nth-of-type(2) .cb[data-on]", "stagger": 1},
            {"f": 0.88, "fd": 0.06, "typ": "zaznacz", "sel": ".mood [data-sel]"},
        ],
    },
    {  # 11
        "id": "dzialania", "tytul": "8–9 · Działania i cele w 9 domenach ICF", "strona": 11, "foto": "sluchawki",
        "prawo": [p("428", "§ 7 ust. 6 pkt 6 – działania i efekty"), p("428", "§ 7 ust. 6 pkt 7 – wnioski do dalszej pracy"), p("ks", "§ 6 ust. 10 – cele w WOPF")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": "table.grid", "pad": 16, "zoom": 1.15},
            {"f": 0.02, "fd": 0.40, "typ": "wpisz", "sel": "table.grid tr td:not(.area)"},
            {"f": 0.22, "fd": 0.20, "typ": "kamera", "sel": "table.grid tr:nth-child(2) td.plus", "pad": 24, "zoom": 1.6},
            {"f": 0.40, "fd": 0.00, "typ": "strona", "nr": 12},
            {"f": 0.40, "fd": 0.20, "typ": "kamera", "strona": 12, "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.41, "fd": 0.28, "typ": "wpisz", "strona": 12, "sel": "ul.tick li"},
            {"f": 0.55, "fd": 0.15, "typ": "kamera", "strona": 12, "sel": "table.grid tr:nth-child(4)", "pad": 20, "zoom": 1.5},
            {"f": 0.72, "fd": 0.00, "typ": "strona", "nr": 13},
            {"f": 0.72, "fd": 0.20, "typ": "kamera", "strona": 13, "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.73, "fd": 0.26, "typ": "wpisz", "strona": 13, "sel": "ul.tick li"},
        ],
    },
    {  # 12
        "id": "decyzja", "tytul": "10 · Decyzja Zespołu", "strona": 14, "foto": "zespol",
        "prawo": [p("po", "art. 127 – zespół ustala poziom wsparcia"), p("ks", "§ 6 ust. 2–3 – IPET po WOPF"), p("428", "§ 7 ust. 6 pkt 7 – rekomendacje dla poradni")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": ".lvlbox", "pad": 24, "zoom": 1.3},
            {"f": 0.06, "fd": 0.08, "typ": "zaznacz", "sel": ".lvlbox .cb[data-on]"},
            {"f": 0.18, "fd": 0.20, "typ": "kamera", "sel": ".kv", "pad": 24, "zoom": 1.4},
            {"f": 0.20, "fd": 0.30, "typ": "pokaz", "sel": ".kv > div"},
            {"f": 0.55, "fd": 0.20, "typ": "kamera", "sel": ".rek", "pad": 24, "zoom": 1.3},
            {"f": 0.58, "fd": 0.26, "typ": "zaznacz", "sel": ".rek .cb[data-on]", "stagger": 1},
            {"f": 0.86, "fd": 0.10, "typ": "wpisz", "sel": ".note .ph", "teksty": [D["data"]]},
        ],
    },
    {  # 13
        "id": "program", "tytul": "11–15 · Program wsparcia", "strona": 15, "foto": "aac",
        "prawo": [p("ks", "§ 6 ust. 1 pkt 1–8 – treść IPET"), p("pp", "dostosowanie bez obniżania wymagań"), p("ppp", "godzina zajęć 45 min"), p("ks", "§ 7 – dodatkowa osoba")],
        "kroki": [
            {"f": 0.00, "fd": 0.15, "typ": "kamera", "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.01, "fd": 0.18, "typ": "pokaz", "sel": "table.grid tr"},
            {"f": 0.20, "fd": 0.00, "typ": "strona", "nr": 16},
            {"f": 0.20, "fd": 0.15, "typ": "kamera", "strona": 16, "sel": ".sub9:nth-of-type(2), table.grid:nth-of-type(2)", "pad": 16, "zoom": 1.1},
            {"f": 0.21, "fd": 0.18, "typ": "pokaz", "strona": 16, "sel": "table.grid tr"},
            {"f": 0.40, "fd": 0.00, "typ": "strona", "nr": 17},
            {"f": 0.40, "fd": 0.15, "typ": "kamera", "strona": 17, "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.41, "fd": 0.16, "typ": "pokaz", "strona": 17, "sel": "table.grid tr"},
            {"f": 0.56, "fd": 0.00, "typ": "strona", "nr": 19},
            {"f": 0.56, "fd": 0.15, "typ": "kamera", "strona": 19, "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.57, "fd": 0.16, "typ": "pokaz", "strona": 19, "sel": "table.grid tr"},
            {"f": 0.72, "fd": 0.00, "typ": "strona", "nr": 21},
            {"f": 0.72, "fd": 0.15, "typ": "kamera", "strona": 21, "sel": ".kv", "pad": 20, "zoom": 1.3},
            {"f": 0.73, "fd": 0.14, "typ": "pokaz", "strona": 21, "sel": ".kv > div, ul.tick li"},
            {"f": 0.86, "fd": 0.00, "typ": "strona", "nr": 22},
            {"f": 0.86, "fd": 0.14, "typ": "kamera", "strona": 22, "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.87, "fd": 0.13, "typ": "pokaz", "strona": 22, "sel": "table.grid tr"},
        ],
    },
    {  # 14
        "id": "efekty", "tytul": "16 · Ocena efektywności i podpisy", "strona": 23, "foto": "podpis",
        "prawo": [p("ks", "§ 6 ust. 9 – WOPF co najmniej 2 × w roku"), p("po", "art. 127 – rodzic otrzymuje kopię")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": "table.grid", "pad": 16, "zoom": 1.1},
            {"f": 0.02, "fd": 0.40, "typ": "pokaz", "sel": "table.grid tr"},
            {"f": 0.48, "fd": 0.22, "typ": "kamera", "sel": ".sigs", "pad": 30, "zoom": 1.4},
            {"f": 0.54, "fd": 0.42, "typ": "podpis", "sel": ".sigs .sig"},
        ],
    },
    {  # 15
        "id": "opinia", "tytul": "Załącznik · Opinia dla poradni", "strona": 24, "foto": "podpis",
        "prawo": [p("428", "§ 7 ust. 2–3 – dyrektor, 10 dni"), p("428", "§ 7 ust. 5 – kopia dla rodziców"), p("428", "§ 7 ust. 6 – 7 elementów opinii")],
        "kroki": [
            {"f": 0.00, "fd": 0.20, "typ": "kamera", "sel": ".op-head", "pad": 24, "zoom": 1.2},
            {"f": 0.02, "fd": 0.18, "typ": "wpisz", "sel": ".op-right .fill", "teksty": [D["data_opinii"], D["znak"], D["poradnia"]]},
            {"f": 0.24, "fd": 0.20, "typ": "kamera", "sel": "table.op", "pad": 16, "zoom": 1.15},
            {"f": 0.26, "fd": 0.50, "typ": "wpisz", "sel": "table.op .ph",
             "teksty": [D["data_opinii"], D["dziecko"], D["data_ur"], D["placowka"] + ", " + D["adres"].split(" · ")[0], D["grupa"],
                        D["rodzice"], "16.09.2026", "PPP-1.4123.15.2026", D["orzeczenie"], D["nr"], D["data_orz"], D["poradnia"], "2025", "wrzesień 2026"]},
            {"f": 0.40, "fd": 0.05, "typ": "zaznacz", "sel": "table.op tr:nth-child(4) .cb:nth-of-type(1)"},
            {"f": 0.55, "fd": 0.05, "typ": "zaznacz", "sel": "table.op tr:nth-child(6) .cb:nth-of-type(1)"},
            {"f": 0.66, "fd": 0.05, "typ": "zaznacz", "sel": "table.op tr:nth-child(7) .cb:nth-of-type(2)"},
            {"f": 0.72, "fd": 0.12, "typ": "kamera", "sel": ".op-law", "pad": 24, "zoom": 1.4},
            {"f": 0.82, "fd": 0.00, "typ": "strona", "nr": 25},
            {"f": 0.82, "fd": 0.18, "typ": "kamera", "strona": 25, "sel": "table.op", "pad": 12, "zoom": 1.15},
        ],
    },
    {  # 16
        "id": "outro", "tytul": "Jeden druk, trzy obowiązki", "strona": 1, "awatar": "full", "foto": "zespol",
        "ekran": {"nad": "EduPlaner 2026", "tytul": "Jeden druk, trzy obowiązki placówki", "pod": "opinia dla poradni · WOPF · IPET"},
        "prawo": [p("428", "zgodność od 1.09.2026")],
        "kroki": [],
    },
]


def czytaj_narracje() -> list[str]:
    tekst = NARRACJA.read_text(encoding="utf-8").strip()
    akapity = [a.strip() for a in re.split(r"\n\s*\n", tekst) if a.strip()]
    if len(akapity) != len(SCENY):
        raise SystemExit(f"narracja.txt ma {len(akapity)} akapitów, scen jest {len(SCENY)} – muszą się zgadzać")
    return akapity


def dur_sceny(akapit: str) -> float:
    """Szacunek czasu: ~150 słów/min po polsku + oddech między scenami."""
    return round(len(akapit.split()) / 2.5 + 1.2, 1)


def usun_bloki(css: str, start: str) -> str:
    """Usuwa każdy blok zaczynający się od `start` aż do domykającego nawiasu (z zagnieżdżeniami)."""
    while True:
        i = css.find(start)
        if i < 0:
            return css
        j = i + len(start)
        glebokosc = 1
        while j < len(css) and glebokosc:
            if css[j] == "{":
                glebokosc += 1
            elif css[j] == "}":
                glebokosc -= 1
            j += 1
        css = css[:i] + css[j:]


def zbalansuj_divy(sekcja: str) -> str:
    """Oryginał ma na jednej stronie nadmiarowe </div>; w body to nieszkodliwe, ale w kontenerze
    kamery zamknęłoby kontener. Usuwamy nadmiar tuż przed stopką strony."""
    while sekcja.count("</div>") > len(re.findall(r"<div\b", sekcja)):
        stopka = sekcja.find('<div class="footer">')
        i = sekcja.rfind("</div>", 0, stopka if stopka > 0 else len(sekcja))
        if i < 0:
            break
        sekcja = sekcja[:i] + sekcja[i + 6:]
    return sekcja


def przygotuj_druk(html: str) -> tuple[str, str]:
    """Zwraca (css, strony_html) z oryginalnego druku, po oczyszczeniu."""
    css = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
    # usuń reguły globalne druku, które kłóciłyby się ze sceną filmu
    css = re.sub(r"html,body\{[^}]*\}", "", css)
    css = css.replace("*{box-sizing:border-box}", "")
    css = re.sub(r"\.modebar[^{]*\{[^}]*\}", "", css)
    css = usun_bloki(css, "@media print{")
    css = usun_bloki(css, "@media screen and (max-width:760px){")

    body = html[html.find("<body"):html.rfind("</body>")]
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r'<div class="modebar">.*?</div>\s*', "", body, flags=re.S)
    body = body[body.find("<section"):]

    # numeracja stron i identyfikatory
    strony = re.split(r"(?=<section class=\"page)", body)
    strony = [s for s in strony if s.strip()]
    wynik = []
    for i, s in enumerate(strony, 1):
        s = s.replace('<section class="page', f'<section id="f-p{i}" data-nr="{i}" class="page', 1)
        s = s.replace("{{TOTAL}}", str(len(strony)))
        s = zbalansuj_divy(s)
        s = s.replace("[Nazwa placówki]", D["placowka_krotko"])
        if "op-page" in s[:120]:
            s = s.replace("[Adres placówki, tel., e-mail]", D["adres"]).replace("[Miejscowość]", D["miejscowosc"])
            s = s.replace('<td class="k">Data urodzenia · PESEL</td><td>[Data urodzenia] · [PESEL]</td>',
                          '<td class="k">Data urodzenia</td><td>[Data urodzenia]</td>')
            # placeholdery w tabelach opinii → span.ph, żeby dało się je wpisać
            s = re.sub(r"\[(Data wydania|Imię i Nazwisko|Data urodzenia|PESEL|Nazwa i adres placówki|grupa / klasa|Imiona i nazwiska, adres do korespondencji|Data otrzymania|Znak sprawy|Orzeczenie / Opinia|Numer|Data|Nazwa Poradni|rok|miesiąc rok)\]",
                       r'<span class="ph">[\1]</span>', s)
        wynik.append(s)
    return css, "\n".join(wynik)


CSS_FILM = r"""
:root{
  --f-bg:#15102B; --f-bg2:#1F1740; --f-panel:#241B4B; --f-line:rgba(182,166,223,.22);
  --f-ink:#F4F1FB; --f-muted:#B6A6DF; --f-dim:#7D6FB0;
  --f-purple:#2D1B69; --f-orange:#E8450A; --f-orange2:#FF7A3D; --f-amber:#DFA22E; --f-green:#5CC489;
  --f-paper:#FFFFFF; --f-shadow:0 30px 80px rgba(0,0,0,.55);
  --f-sans:"Mulish","Segoe UI",Arial,sans-serif; --f-mono:"DM Mono","SFMono-Regular",Consolas,monospace;
  --f-ui-bg:#F5F2FB; --f-ui-ink:#1A1530; --f-ui-muted:#6B6378; --f-ui-line:#D9D0F0; --f-ui-panel:#FFFFFF;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){ --f-ui-bg:#100C22; --f-ui-ink:#F4F1FB; --f-ui-muted:#B6A6DF; --f-ui-line:#2F2657; --f-ui-panel:#1A1435; }
}
:root[data-theme="dark"]{ --f-ui-bg:#100C22; --f-ui-ink:#F4F1FB; --f-ui-muted:#B6A6DF; --f-ui-line:#2F2657; --f-ui-panel:#1A1435; }

html{background:var(--f-ui-bg)}
body{margin:0;background:var(--f-ui-bg);color:var(--f-ui-ink);font-family:var(--f-sans);font-size:15px;line-height:1.5;padding-inline:16px;padding-block:18px 40px}
*,*::before,*::after{box-sizing:border-box}
.f-wrap{max-width:1600px;margin:0 auto}
.f-top{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:8px 24px;margin:0 0 12px}
.f-top h1{margin:0;font-size:22px;font-weight:800;letter-spacing:-.01em;color:var(--f-ui-ink)}
.f-top h1 small{font-weight:600;color:var(--f-ui-muted);font-size:14px;margin-left:10px}
.f-badge{font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--f-orange);border:1px solid currentColor;border-radius:999px;padding:3px 10px}

/* ---------- scena 16:9 ---------- */
.f-stage-box{position:relative;width:100%;aspect-ratio:16/9;background:var(--f-bg);border-radius:14px;overflow:hidden;box-shadow:0 10px 40px rgba(20,12,50,.25)}
.f-stage{position:absolute;left:0;top:0;width:1920px;height:1080px;transform-origin:0 0;background:
  radial-gradient(1200px 700px at 30% 40%, #261C52 0%, var(--f-bg) 60%),
  var(--f-bg);color:var(--f-ink);font-family:var(--f-sans);overflow:hidden}
.f-stage::before{content:"";position:absolute;inset:0;background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .05 0'/></filter><rect width='120' height='120' filter='url(%23n)'/></svg>");opacity:.5;pointer-events:none}

.f-bar{position:absolute;left:48px;right:48px;top:22px;height:44px;display:flex;align-items:center;gap:18px}
.f-bar .f-brand{display:flex;align-items:center;gap:10px;font-weight:800;font-size:17px;letter-spacing:.02em;white-space:nowrap}
.f-bar .f-brand i{width:30px;height:30px;border-radius:50%;background:var(--f-orange);display:grid;place-items:center;font-style:normal;font-size:15px;color:#fff}
.f-bar .f-brand small{font-weight:600;color:var(--f-muted);font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin-left:6px}
.f-chapters{flex:1;display:flex;gap:4px;height:10px;align-items:stretch}
.f-chapters span{flex:1;background:rgba(255,255,255,.10);border-radius:3px;position:relative;overflow:hidden;cursor:pointer}
.f-chapters span::after{content:"";position:absolute;left:0;top:0;bottom:0;width:calc(var(--p,0)*100%);background:var(--f-orange)}
.f-chapters span.done::after{background:var(--f-orange);width:100%;opacity:.55}
.f-chapters span:hover{outline:1px solid var(--f-muted)}
.f-time{font-family:var(--f-mono);font-size:15px;color:var(--f-muted);letter-spacing:.04em;font-variant-numeric:tabular-nums;white-space:nowrap}

/* druk */
.f-druk{position:absolute;left:48px;top:84px;width:1160px;height:916px;border-radius:12px;overflow:hidden;background:#0E0A1F;box-shadow:inset 0 0 0 1px var(--f-line)}
.f-druk-cam{position:absolute;left:0;top:0;transform-origin:0 0;will-change:transform}
.f-druk{color-scheme:light}
.f-druk .page{display:none;margin:0;box-shadow:var(--f-shadow);width:794px;position:relative;color:var(--ink);background:#fff;forced-color-adjust:none}
.f-druk .page .lead2,.f-druk .page .step p,.f-druk .page .flow5 p,.f-druk .page .lvlbox p,.f-druk .page .ed-grid p,.f-druk .page .toc p,.f-druk .page .stnote,.f-druk .page .legend,.f-druk .page .op-law,.f-druk .page .op-right,.f-druk .page .op-stamp,.f-druk .page .mood,.f-druk .page .sig small,.f-druk .page .hdr .cap,.f-druk .page .footer{color:#5A536B}
.f-druk .page table,.f-druk .page tbody,.f-druk .page tr,.f-druk .page td,.f-druk .page th{color:inherit}
.f-druk .page table{color:var(--ink)}
.f-druk .page .ph{color:#5A536B}
.f-druk .page .field label,.f-druk .page .stat .l,.f-druk .page .kv .l,.f-druk .page .icf small{color:#6A5BA8}
.f-druk .page.f-on{display:block}
.f-druk .page::after{content:"";position:absolute;inset:0;pointer-events:none;box-shadow:inset 0 0 0 1px rgba(45,27,105,.08)}
.f-hid{opacity:.35}
.f-cur{position:relative}
.f-cur::after{content:"";display:inline-block;width:2px;height:1em;background:var(--f-orange);vertical-align:-.15em;margin-left:1px;animation:f-blink 1s steps(2) infinite}
.f-remotion .f-cur::after{animation:none}
@keyframes f-blink{to{opacity:0}}
.f-druk .cb{transition:none}
.f-druk .fields .field span,.f-druk .team li span,.f-druk .date-line .fill{height:auto;min-height:14px;font-size:13px;line-height:1.25;color:var(--ink);font-weight:600}
.f-druk .team li span{min-height:16px}
.f-druk .op-right .fill{color:var(--ink);font-weight:600}
.f-druk .fields .field span:not(:empty){padding-bottom:1px}
.f-sub > div{max-width:100%}
.f-sigsvg{display:block;width:150px;height:44px;margin:-38px auto 0;overflow:visible}
.f-sigsvg path{fill:none;stroke:#1F1A5A;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.f-druk .page .f-flash{box-shadow:0 0 0 3px rgba(232,69,10,.35) !important;border-radius:4px}
.f-druk-dim{position:absolute;inset:0;background:rgba(14,10,31,var(--dim,0));pointer-events:none}
.f-przyklad{position:absolute;right:16px;top:12px;font-size:11px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#fff;background:rgba(232,69,10,.9);padding:4px 10px;border-radius:999px;z-index:3}

/* kolumna prawa */
.f-side{position:absolute;left:1248px;top:84px;width:624px;height:916px;display:flex;flex-direction:column;gap:18px}
.f-scene{margin-top:284px}
.f-scene .k{font-size:12px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--f-orange2)}
.f-scene h2{margin:4px 0 0;font-size:34px;line-height:1.1;font-weight:800;letter-spacing:-.01em;text-wrap:balance;color:var(--f-ink)}
.f-law{background:var(--f-panel);border:1px solid var(--f-line);border-radius:14px;padding:16px 18px 14px;flex:0 0 auto}
.f-law .h{display:flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:.18em;text-transform:uppercase;color:var(--f-muted);margin-bottom:10px}
.f-law .h i{width:26px;height:26px;border-radius:50%;background:var(--f-orange);color:#fff;display:grid;place-items:center;font-style:normal;font-weight:800;font-size:15px}
.f-law ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.f-law li{display:grid;grid-template-columns:1fr auto;gap:4px 12px;align-items:baseline;border-top:1px solid var(--f-line);padding-top:8px;opacity:0;transform:translateX(14px)}
.f-law li:first-child{border-top:0;padding-top:0}
.f-law li b{font-size:16px;font-weight:800;color:var(--f-ink);line-height:1.25}
.f-law li .dz{font-family:var(--f-mono);font-size:12px;color:var(--f-orange2);white-space:nowrap}
.f-law li .co{grid-column:1/-1;font-size:14px;color:var(--f-muted);line-height:1.35}
.f-foto{position:relative;flex:1;min-height:150px;border-radius:14px;overflow:hidden;background:var(--f-bg2);border:1px solid var(--f-line);cursor:pointer}
.f-foto img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transform-origin:50% 50%;display:block}
.f-foto .cap{position:absolute;left:0;right:0;bottom:0;padding:26px 16px 12px;font-size:13px;color:#fff;background:linear-gradient(transparent,rgba(14,10,31,.85));letter-spacing:.02em}
.f-foto .swap{position:absolute;right:10px;top:10px;font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;background:rgba(14,10,31,.7);color:#fff;padding:5px 9px;border-radius:999px;opacity:0}
.f-foto:hover .swap{opacity:1}
.f-remotion .f-foto .swap{display:none}

/* awatar */
.f-av{position:absolute;left:calc(var(--ax)*1px);top:calc(var(--ay)*1px);width:calc(var(--ad)*1px);height:calc(var(--ad)*1px);transform:translate(-50%,-50%);border-radius:50%;z-index:5}
.f-av .ring{position:absolute;inset:-10px;border-radius:50%;border:2px solid rgba(232,69,10,.55)}
.f-av .ring2{position:absolute;inset:-22px;border-radius:50%;border:1px solid rgba(232,69,10,.22)}
.f-av .disc{position:absolute;inset:0;border-radius:50%;overflow:hidden;clip-path:circle(50% at 50% 50%);-webkit-clip-path:circle(50% at 50% 50%);isolation:isolate;transform:translateZ(0);background:radial-gradient(circle at 40% 35%,#3B2A80,#1A1240 70%);box-shadow:0 20px 60px rgba(0,0,0,.5)}
.f-av video{width:100%;height:100%;object-fit:cover;display:none}
.f-av.has video.hg{display:block}
.f-av.intro-on video.intro{display:block;position:absolute;inset:0;object-position:50% 0;transform:scale(1.55);transform-origin:50% 18%;z-index:2}
.f-av.intro-on video.hg{display:none}
.f-av.intro-on .ph{display:none}
.f-av .ph{position:absolute;inset:0;display:grid;place-items:center;text-align:center;padding:12%;color:var(--f-muted)}
.f-av .ph{padding:0;overflow:hidden;border-radius:50%;clip-path:circle(50% at 50% 50%)}
.f-av .ph .ewa{position:absolute;left:0;top:5%;width:100%;height:100%;object-fit:cover;object-position:50% 0;transform:none;padding:0}
.f-av .disc{background:radial-gradient(circle at 50% 30%,#4A3596,#1A1240 72%)}
.f-av.has .ph{display:none}
.f-av .ph svg{width:44%;height:auto;opacity:.9}
.f-av .ph b{display:block;font-size:calc(var(--ad)*.06px);color:var(--f-ink);margin-top:6px;line-height:1.2}
.f-av .ph small{display:block;font-size:calc(var(--ad)*.045px);line-height:1.3;margin-top:4px}
.f-av .talk{position:absolute;left:50%;bottom:-6%;transform:translateX(-50%);display:flex;gap:4px;align-items:flex-end;height:18px}
.f-av .talk i{width:4px;background:var(--f-orange);border-radius:2px;height:calc(var(--h,.3)*18px)}

/* ekran tytułowy */
.f-title{position:absolute;left:0;right:0;top:calc(var(--ay)*1px + var(--ad)*.5px + 44px);text-align:center;opacity:var(--o,0);z-index:4}
.f-title .nad{font-size:14px;font-weight:800;letter-spacing:.3em;text-transform:uppercase;color:var(--f-orange2)}
.f-title h2{margin:10px 0 8px;font-size:58px;line-height:1.05;font-weight:800;letter-spacing:-.015em;color:var(--f-ink);text-wrap:balance}
.f-title .pod{font-size:20px;color:var(--f-muted);letter-spacing:.04em}

/* napisy */
.f-sub{position:absolute;left:48px;width:1160px;top:1008px;height:56px;display:flex;align-items:center;justify-content:center;padding:0 24px;text-align:center;font-size:24px;line-height:1.25;font-weight:600;color:var(--f-ink);text-shadow:0 2px 8px rgba(0,0,0,.6)}
.f-sub .w{color:rgba(244,241,251,.45)}
.f-sub .w.on{color:var(--f-ink)}
.f-sub.off{display:none}

/* sterowanie (poza sceną) */
.f-ctl{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin-top:12px;background:var(--f-ui-panel);border:1px solid var(--f-ui-line);border-radius:12px;padding:10px 14px}
.f-btn{font:inherit;font-weight:800;font-size:14px;letter-spacing:.02em;border:1px solid var(--f-ui-line);background:var(--f-ui-panel);color:var(--f-ui-ink);border-radius:999px;padding:8px 14px;cursor:pointer;display:inline-flex;align-items:center;gap:8px}
.f-btn.primary{background:var(--f-orange);border-color:var(--f-orange);color:#fff;min-width:118px;justify-content:center}
.f-btn:focus-visible,.f-chapters span:focus-visible,.f-range:focus-visible,.f-foto:focus-visible{outline:2px solid var(--f-orange);outline-offset:2px}
.f-range{flex:1;min-width:180px;accent-color:var(--f-orange);height:6px}
.f-ctl .t{font-family:var(--f-mono);font-size:14px;font-variant-numeric:tabular-nums;color:var(--f-ui-muted);min-width:96px;text-align:center}
.f-ctl label.sw{display:inline-flex;gap:6px;align-items:center;font-size:13px;color:var(--f-ui-muted);cursor:pointer}
.f-ctl select{font:inherit;font-size:13px;border:1px solid var(--f-ui-line);background:var(--f-ui-panel);color:var(--f-ui-ink);border-radius:8px;padding:5px 8px}

.f-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px;margin-top:14px}
.f-card{background:var(--f-ui-panel);border:1px solid var(--f-ui-line);border-radius:12px;padding:14px 16px}
.f-card h3{margin:0 0 4px;font-size:15px;font-weight:800;display:flex;align-items:center;gap:8px}
.f-card h3 i{width:22px;height:22px;border-radius:6px;display:grid;place-items:center;font-style:normal;font-size:12px;font-weight:800;color:#fff;background:var(--f-purple)}
.f-card p{margin:0 0 10px;font-size:13.5px;color:var(--f-ui-muted);line-height:1.45;max-width:62ch}
.f-card .st{font-size:12px;font-weight:700;color:var(--f-ui-muted);margin-top:8px;display:flex;gap:6px;align-items:center}
.f-card .st.ok{color:#2E7D45}
.f-card input[type=file]{font-size:12px;max-width:100%}
.f-card code{font-family:var(--f-mono);font-size:12px;background:var(--f-ui-bg);border:1px solid var(--f-ui-line);border-radius:6px;padding:1px 6px}
.f-chaplist{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:6px;margin-top:14px}
.f-chaplist button{font:inherit;text-align:left;border:1px solid var(--f-ui-line);background:var(--f-ui-panel);color:var(--f-ui-ink);border-radius:10px;padding:8px 10px;cursor:pointer;display:grid;grid-template-columns:auto 1fr;gap:2px 10px;align-items:baseline}
.f-chaplist button b{font-family:var(--f-mono);font-size:12px;color:var(--f-orange);font-variant-numeric:tabular-nums}
.f-chaplist button span{font-size:13.5px;font-weight:700}
.f-chaplist button small{grid-column:2;font-size:12px;color:var(--f-ui-muted);font-weight:400}
.f-chaplist button.on{border-color:var(--f-orange);box-shadow:0 0 0 2px rgba(232,69,10,.18)}
details.f-nar{margin-top:14px;background:var(--f-ui-panel);border:1px solid var(--f-ui-line);border-radius:12px;padding:10px 16px}
details.f-nar summary{cursor:pointer;font-weight:800}
details.f-nar pre{white-space:pre-wrap;font:inherit;font-size:14px;line-height:1.55;color:var(--f-ui-ink);max-width:70ch}
.f-foot{margin-top:18px;font-size:12.5px;color:var(--f-ui-muted);line-height:1.5;max-width:90ch}

.f-remotion body,.f-remotion .f-wrap{padding:0;max-width:none}
.f-remotion .f-top,.f-remotion .f-ctl,.f-remotion .f-grid,.f-remotion .f-chaplist,.f-remotion details.f-nar,.f-remotion .f-foot{display:none}
.f-remotion .f-stage-box{border-radius:0;width:1920px;height:1080px;aspect-ratio:auto}
.f-remotion *{transition:none !important;animation:none !important}
@media (prefers-reduced-motion: reduce){.f-cur::after{animation:none}}
@media (max-width:760px){.f-top h1{font-size:18px} .f-ctl .t{min-width:0}}
"""

JS_FILM = r"""
(function(){
'use strict';
const S = window.__SCENY__, NAR = window.__NARRACJA__, FOTO = window.__FOTO__;
const Q = new URLSearchParams(location.search);
const REMOTION = Q.get('remotion') === '1';
const $ = (s, r=document) => r.querySelector(s), $$ = (s, r=document) => Array.from(r.querySelectorAll(s));
const clamp = (v,a,b) => v<a?a:v>b?b:v, lerp=(a,b,t)=>a+(b-a)*t;
const ease = t => t<.5 ? 4*t*t*t : 1-Math.pow(-2*t+2,3)/2;
const easeOut = t => 1-Math.pow(1-t,3);
if (REMOTION) document.documentElement.classList.add('f-remotion');

// ---------- czas scen ----------
function ustawCzasy(starty){ let t=0; S.forEach((s,i)=>{ if(starty){ s.start=starty[i]; s.dur=(i+1<S.length?starty[i+1]:starty[i]+s.dur0)-s.start; } else { s.start=t; s.dur=s.dur0; t+=s.dur; } }); }
const OFFSET = () => S[0].intro ? S[0].dur : 0;   // nagranie narracji zaczyna się po intro
function skalujDoNagrania(sek){ const bez=S.filter(s=>!s.intro); const suma=bez.reduce((a,s)=>a+s.dur0,0); const k=sek/suma; bez.forEach(s=>s.dur0*=k); ustawCzasy(null); }
S.forEach(s=>{ s.dur0=s.dur; }); ustawCzasy(null);
const total = () => S[S.length-1].start + S[S.length-1].dur;

// ---------- zdania napisów (z akapitów) ----------
function zdania(ak){ return ak.match(/[^.!?]+[.!?]+["”]?\s*|[^.!?]+$/g).map(z=>z.trim()).filter(Boolean); }
S.forEach((s,i)=>{ const zd=zdania(NAR[i]); const n=zd.reduce((a,z)=>a+z.length,0); let acc=0; s.zdania=zd.map(z=>{ const od=acc/n; acc+=z.length; return {tekst:z, od, do_:acc/n, slowa:z.split(/\s+/)}; }); });
let SRT=null; // [{start,end,text}]

// ---------- DOM ----------
const stage=$('#f-stage'), box=$('#f-stage-box'), cam=$('#f-cam'), pages=$$('#f-cam .page');
const pageByNr = nr => pages[nr-1];
const VW=1160, VH=916;
const av=$('#f-av'), avVideo=$('#f-av video.hg'), introVideo=$('#f-av video.intro'), title=$('#f-title'), sub=$('#f-sub'), law=$('#f-law'), fotoEl=$('#f-foto'), fotoImg=$('#f-foto img'), fotoCap=$('#f-foto .cap');
const sceneK=$('#f-scene .k'), sceneH=$('#f-scene h2'), timeEl=$('#f-time'), chapters=$('#f-chapters'), dim=$('#f-dim');

// skalowanie sceny do szerokości kontenera
function fit(){ const w=box.clientWidth; stage.style.transform='scale('+(w/1920)+')'; }
if(!REMOTION){ new ResizeObserver(fit).observe(box); fit(); }

// ---------- przygotowanie druku: wyczyść to, co film ma wypełnić ----------
const ORIG = new WeakMap();  // el -> [{node,text}] pełny tekst do odsłaniania
function textNodes(el){ const out=[]; const it=document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let n; while((n=it.nextNode())) out.push({node:n,text:n.data}); return out; }
function revealTo(el, chars){ let list=ORIG.get(el); if(!list){ list=textNodes(el); ORIG.set(el,list); } let left=chars; for(const {node,text} of list){ const take=clamp(left,0,text.length); node.data=text.slice(0,take); left-=take; } }
function totalChars(el){ let list=ORIG.get(el); if(!list){ list=textNodes(el); ORIG.set(el,list);} return list.reduce((a,x)=>a+x.text.length,0); }

// wszystkie strony: nagłówek i pola metryczki wypełnione (dokument „ciągnie” dane)
const D = window.__DANE__;
pages.forEach((pg,i)=>{ if(i===0) return; const nm=$('.hdr .name',pg); if(nm) nm.textContent=D.placowka; const f=$$('.fields .field span',pg); if(f.length===3){ f[0].textContent=D.dziecko; f[1].textContent=D.grupa; f[2].textContent=D.data; } });
// strona 8 (wyniki liczbowe): przedszkole → KPOF
(function(){ const p8=pageByNr(8); p8.classList.remove('kszof'); p8.classList.add('kpof'); const r=$('input[value="kpof"]',p8); if(r) r.checked=true; $('input[value="kszof"]',p8).checked=false; })();
// zapamiętaj i wyczyść ptaszki / zaznaczenia
$$('#f-cam .cb.on').forEach(cb=>{ cb.dataset.on='1'; cb.classList.remove('on'); });
$$('#f-cam .lvlbox > div.sel, #f-cam .mood > div.sel, #f-cam .ed-grid > div.sel').forEach(d=>{ d.dataset.sel='1'; d.classList.remove('sel'); });

// kroki: rozwiń selektory raz, przygotuj stan początkowy
S.forEach((s,si)=>{ s.kroki.forEach(k=>{ if(k.typ==='strona') return; const nr=k.strona||s.strona; const pg=pageByNr(nr); k.nr=nr;
  if(k.typ==='kamera'){ return; }
  k.els=$$(k.sel,pg);
  if(k.typ==='wpisz'){ k.els.forEach((el,i)=>{ if(k.teksty){ el.classList.remove('ph'); el.textContent=k.teksty[i]??''; } el.dataset.len=totalChars(el); revealTo(el,0); }); }
  if(k.typ==='pokaz'){ k.els.forEach(el=>el.classList.add('f-hid')); }
  if(k.typ==='pasek'){ k.els.forEach(el=>{ el.dataset.w=el.style.getPropertyValue('--w'); el.style.setProperty('--w','0%'); }); }
  if(k.typ==='licz'){ k.els.forEach(el=>{ el.innerHTML=k.wzor.replace('{n}', (0).toFixed(k.dec||0).replace('.',',')); }); }
  if(k.typ==='podpis'){ k.els.forEach((el,i)=>{ const svg=document.createElementNS('http://www.w3.org/2000/svg','svg'); svg.setAttribute('viewBox','0 0 150 44'); svg.setAttribute('class','f-sigsvg'); const path=document.createElementNS('http://www.w3.org/2000/svg','path'); const d=['M6 30 C 14 6, 24 40, 34 22 S 52 8, 60 26 S 76 36, 86 16 S 102 30, 112 20 S 128 10, 142 24','M8 26 C 20 4, 26 38, 40 24 S 56 6, 66 28 S 84 34, 94 14 S 110 32, 124 18 S 136 12, 144 26','M6 28 C 12 10, 22 36, 32 20 S 50 4, 58 24 S 74 38, 88 18 S 104 28, 116 22 S 130 8, 144 28','M8 30 C 18 8, 26 34, 38 24 S 54 8, 64 26 S 80 36, 92 16 S 106 30, 120 20 S 134 10, 144 26'][i%4]; path.setAttribute('d',d); svg.appendChild(path); el.insertBefore(svg, el.firstChild); const L=path.getTotalLength(); path.style.strokeDasharray=L; path.style.strokeDashoffset=L; k.paths=k.paths||[]; k.paths.push({path,L}); }); }
}); });

// ---------- automatyczne wypełnianie: każda rubryka pokazywanej strony wpisuje się w kolejności czytania ----------
const FILL_SEL='.hdr .name, .fields .field span, .ph, .fill, td:not(.code), .tool p, .step p, .flow5 p, .res p, .res .rec, .box p, ul.tick li, .kv .v, .voice p, .team li span, .op-stamp b, ul.op li, .lead p';
S.forEach((s,si)=>{ if(s.awatar==='full') return;
  const zmiany=[{f:0,nr:s.strona}].concat(s.kroki.filter(k=>k.typ==='strona').map(k=>({f:k.f,nr:k.nr})));
  zmiany.forEach((z,i)=>{ const fKoniec=i+1<zmiany.length?zmiany[i+1].f:1; const pg=pageByNr(z.nr); if(pg.dataset.auto) return; pg.dataset.auto='1';
    const pokryte=[]; S.forEach(x=>x.kroki.forEach(k=>{ if(k.els && k.nr===z.nr && (k.typ==='wpisz'||k.typ==='licz')) pokryte.push(...k.els); }));
    let kand=$$(FILL_SEL,pg).filter(el=>!el.closest('.footer')&&!el.closest('th')&&el.textContent.trim().length>0);
    kand=kand.filter(el=>!pokryte.some(c=>c===el||c.contains(el)||el.contains(c)));
    kand=kand.filter(el=>!kand.some(o=>o!==el&&el.contains(o)));
    if(!kand.length) return;
    kand.forEach(el=>{ el.dataset.len=totalChars(el); revealTo(el,0); });
    const dl=fKoniec-z.f; s.kroki.push({typ:'wpisz',auto:true,nr:z.nr,f:z.f+0.02*dl,fd:0.9*dl,els:kand}); });
});

// ---------- foto ----------
function fotoSrc(id){ try{ const v=localStorage.getItem('film_foto_'+id); if(v) return v; }catch(e){} return FOTO[id].src; }
let fotoId=null;
function ustawFoto(id){ if(id===fotoId) return; fotoId=id; fotoImg.src=fotoSrc(id); fotoImg.alt=FOTO[id].alt; fotoCap.textContent=FOTO[id].alt; }
$('#f-foto-file').addEventListener('change', e=>{ const f=e.target.files[0]; if(!f) return; const r=new FileReader(); r.onload=()=>{ try{ localStorage.setItem('film_foto_'+fotoId, r.result); }catch(err){} fotoImg.src=r.result; }; r.readAsDataURL(f); });
fotoEl.addEventListener('click', ()=>{ if(!REMOTION) $('#f-foto-file').click(); });
fotoEl.addEventListener('keydown', e=>{ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); $('#f-foto-file').click(); } });

// ---------- karta prawna ----------
let lawScene=-1;
function ustawPrawo(si){ if(si===lawScene) return; lawScene=si; const s=S[si]; $('ul',law).innerHTML=s.prawo.map(x=>'<li><b>'+x.akt+'</b><span class="dz">'+x.dz+'</span><span class="co">'+x.co+'</span></li>').join(''); sceneK.textContent='Scena '+(si+1)+' z '+S.length; sceneH.textContent=s.tytul; }

// ---------- kamera ----------
const camCache=new Map();
function pageSize(pg){ return {w:794, h:pg.offsetHeight||1123}; }
function fitCam(pg){ const {w,h}=pageSize(pg); const s=Math.min(VW/w, VH/h); return {s, x:(VW-w*s)/2, y:Math.max(0,(VH-h*s)/2)}; }
function targetCam(pg, k){ const key=pg.dataset.nr+'|'+k.sel+'|'+k.pad+'|'+k.zoom; if(camCache.has(key)) return camCache.get(key);
  const base=fitCam(pg); const els=$$(k.sel,pg); if(!els.length){ camCache.set(key,base); return base; }
  const pr=pg.getBoundingClientRect(); const cs=pr.width/794||1; let x1=1e9,y1=1e9,x2=-1e9,y2=-1e9;
  els.forEach(el=>{ const r=el.getBoundingClientRect(); x1=Math.min(x1,(r.left-pr.left)/cs); y1=Math.min(y1,(r.top-pr.top)/cs); x2=Math.max(x2,(r.right-pr.left)/cs); y2=Math.max(y2,(r.bottom-pr.top)/cs); });
  const pad=k.pad||20, w=x2-x1+2*pad, h=y2-y1+2*pad; let s=Math.min(VW/w, VH/h, k.zoom||1.35); s=Math.max(s, base.s);
  const {w:pw,h:ph}=pageSize(pg); let x=VW/2-(x1+x2)/2*s, y=VH/2-(y1+y2)/2*s;
  if(pw*s<=VW) x=(VW-pw*s)/2; else x=clamp(x, VW-pw*s, 0);
  if(ph*s<=VH) y=(VH-ph*s)/2; else y=clamp(y, VH-ph*s, 0);
  const t={s,x,y}; camCache.set(key,t); return t; }
let curScale=null, curPage=null;
function applyCam(c){ curScale=c.s; cam.style.transform='translate('+c.x.toFixed(2)+'px,'+c.y.toFixed(2)+'px) scale('+c.s.toFixed(4)+')'; }
function showPage(pg){ if(curPage===pg) return; pages.forEach(p=>p.classList.toggle('f-on',p===pg)); curPage=pg; curScale=null; applyCam(fitCam(pg)); }

// ---------- awatar / ekran tytułowy ----------
let avFull=0; // 0..1
let AVPOS={ax:1560,ay:224,ad:260};
function ustawAwatar(p){ const ax=lerp(1560,960,p), ay=lerp(224,470,p), ad=lerp(260,560,p); AVPOS={ax,ay,ad,p}; stage.style.setProperty('--ax',ax); stage.style.setProperty('--ay',ay); stage.style.setProperty('--ad',ad); dim.style.setProperty('--dim',(p*.78).toFixed(3)); $('#f-side').style.opacity=(1-p).toFixed(3); title.style.setProperty('--o',clamp((p-.5)*2,0,1).toFixed(3)); }
function talk(t, on){ $$('#f-av .talk i').forEach((b,i)=>{ b.style.setProperty('--h', on ? (0.3+0.7*Math.abs(Math.sin(t*9+i*1.7))).toFixed(2) : 0.15); }); }

// ---------- render(T) ----------
let lastSub='';
function render(T){
  T=clamp(T,0,total()-0.001);
  let si=S.findIndex(s=>T<s.start+s.dur); if(si<0) si=S.length-1; const s=S[si]; const lt=T-s.start; const p=lt/s.dur;
  ustawPrawo(si); ustawFoto(s.foto);
  // strona widoczna w tej scenie
  let nr=s.strona; s.kroki.forEach(k=>{ if(k.typ==='strona' && lt>=k.f*s.dur) nr=k.nr; });
  const pg=pageByNr(nr); showPage(pg);
  // wszystkie kroki wszystkich scen, deterministycznie
  for(let j=0;j<S.length;j++){ const sc=S[j]; for(const k of sc.kroki){ if(k.typ==='strona'||k.typ==='kamera') continue; const t0=sc.start+k.f*sc.dur, d=Math.max(0.05,k.fd*sc.dur); const kp=clamp((T-t0)/d,0,1); if(k.last===kp) continue; k.last=kp; krok(k,kp); } }
  // kamera: kroki bieżącej sceny dla bieżącej strony
  let c=fitCam(pg), prev=c;
  for(const k of s.kroki){ if(k.typ!=='kamera' || k.nr!==nr) continue; const t0=k.f*s.dur; if(lt<t0) break; const d=Math.max(0.05,k.fd*s.dur); const kp=ease(clamp((lt-t0)/d,0,1)); const tg=targetCam(pg,k); c={s:lerp(prev.s,tg.s,kp), x:lerp(prev.x,tg.x,kp), y:lerp(prev.y,tg.y,kp)}; prev=tg; }
  applyCam(c);
  // awatar pełny / koło
  const want=s.awatar==='full'?1:0; const trans=clamp(lt/0.8,0,1); const prevWant=si>0?(S[si-1].awatar==='full'?1:0):want; avFull=lerp(prevWant,want,easeOut(trans)); ustawAwatar(avFull);
  if(s.ekran){ $('.nad',title).textContent=s.ekran.nad; $('h2',title).textContent=s.ekran.tytul; $('.pod',title).textContent=s.ekran.pod; }
  // zdjęcie: powolny najazd (Ken Burns)
  fotoImg.style.transform='scale('+(1.04+0.08*p).toFixed(4)+')';
  // karta prawna: wjazd pozycji
  $$('li',law).forEach((li,i)=>{ const q=clamp((lt+0.2-i*0.35)/0.6,0,1); li.style.opacity=easeOut(q); li.style.transform='translateX('+(14*(1-easeOut(q))).toFixed(1)+'px)'; });
  // napisy
  let txt='', words=null, wp=1;
  if(SRT){ const cue=SRT.find(c=>T>=c.start&&T<c.end); if(cue){ txt=cue.text; words=cue.text.split(/\s+/); wp=(T-cue.start)/(cue.end-cue.start); } }
  else { const q=clamp(lt/(s.dur-0.6),0,1); const z=s.zdania.find(z=>q<z.do_)||s.zdania[s.zdania.length-1]; txt=z.tekst; words=z.slowa; wp=(q-z.od)/(z.do_-z.od); }
  if(txt!==lastSub){ sub.innerHTML='<div>'+words.map(w=>'<span class="w">'+w+'</span>').join(' ')+'</div>'; lastSub=txt; }
  const n=words.length, on=Math.floor(clamp(wp,0,1)*n+0.35); $$('.w',sub).forEach((w,i)=>w.classList.toggle('on',i<on));
  talk(T, txt.length>0 && wp<0.97);
  if(s.intro && !REMOTION && playing && introVideo && introVideo.paused && T<OFFSET()-0.2){ introVideo.currentTime=T; introVideo.play().catch(()=>{}); }
  // pasek rozdziałów, czas
  $$('span',chapters).forEach((sp,i)=>{ sp.classList.toggle('done',i<si); sp.style.setProperty('--p', i===si?p.toFixed(3):(i<si?1:0)); });
  const mm=t=>{ t=Math.max(0,t); return Math.floor(t/60)+':'+String(Math.floor(t%60)).padStart(2,'0'); };
  timeEl.textContent=mm(T)+' / '+mm(total()); $('#f-ctl-time').textContent=mm(T)+' / '+mm(total()); $('#f-range').value=(T/total()*1000).toFixed(0);
  $$('.f-chaplist button').forEach((b,i)=>b.classList.toggle('on',i===si));
  av.classList.toggle('intro-on', !!s.intro); if(s.intro && introVideo && (Math.abs(introVideo.currentTime-T)>0.4 || REMOTION)) introVideo.currentTime=Math.max(0,T);
  if(avVideo.src && av.classList.contains('has')){ const a=Math.max(0,T-OFFSET()); if(Math.abs(avVideo.currentTime-a)>0.35 || REMOTION) avVideo.currentTime=a; }
}
function krok(k,p){
  switch(k.typ){
    case 'wpisz': { const n=k.els.length; k.els.forEach((el,i)=>{ const q=clamp(p*n-i,0,1); const len=+el.dataset.len; revealTo(el, Math.round(q*len)); el.classList.toggle('f-cur', q>0&&q<1); }); break; }
    case 'pokaz': { const n=k.els.length; k.els.forEach((el,i)=>{ const q=easeOut(clamp(p*(n+1)-i,0,1)); el.style.opacity=(0.35+0.65*q).toFixed(3); el.style.transform='translateY('+(4*(1-q)).toFixed(1)+'px)'; el.classList.toggle('f-hid', false); }); break; }
    case 'zaznacz': { const n=k.els.length; k.els.forEach((el,i)=>{ const q=k.stagger?clamp(p*n-i,0,1):p; const on=q>=0.999; const cb=el.classList.contains('cb')?el:$('.cb',el); const host=el.closest('[data-sel]')||el; if(cb) cb.classList.toggle('on', on); host.classList.toggle('sel', on); }); break; }
    case 'pasek': { const n=k.els.length; k.els.forEach((el,i)=>{ const q=easeOut(clamp(p*(n+2)-i,0,1)); el.style.setProperty('--w', (parseFloat(el.dataset.w)*q).toFixed(1)+'%'); }); break; }
    case 'licz': { const q=easeOut(p); k.els.forEach(el=>{ const v=(k.do*q); el.innerHTML=k.wzor.replace('{n}', v.toFixed(k.dec||0).replace('.',',')); }); break; }
    case 'podpis': { const n=k.paths.length; k.paths.forEach(({path,L},i)=>{ const q=easeOut(clamp(p*n-i,0,1)); path.style.strokeDashoffset=(L*(1-q)).toFixed(1); }); break; }
  }
}

// ---------- zegar ----------
let T=0, playing=false, rate=1, raf=null, lastNow=0;
const audio=$('#f-audio');
function tick(now){ if(!playing) return; const off=OFFSET(); if(audio.src && !audio.paused){ T=audio.currentTime+off; } else { T+= (now-lastNow)/1000*rate; if(audio.src && T>=off && audio.paused && !audio.ended){ audio.currentTime=Math.max(0,T-off); audio.play().catch(()=>{}); } } lastNow=now; if(T>=total()){ T=total()-0.001; pause(); } render(T); raf=requestAnimationFrame(tick); }
function play(){ if(playing) return; if(T>=total()-0.05) T=0; playing=true; lastNow=performance.now(); const off=OFFSET(); if(audio.src && T>=off){ audio.currentTime=T-off; audio.playbackRate=rate; audio.play().catch(()=>{}); } if(avVideo.src){ avVideo.currentTime=Math.max(0,T-off); avVideo.play().catch(()=>{}); } if(introVideo && T<off){ introVideo.currentTime=T; introVideo.playbackRate=rate; introVideo.play().catch(()=>{}); } $('#f-play').innerHTML='&#10074;&#10074; Pauza'; raf=requestAnimationFrame(tick); }
function pause(){ playing=false; cancelAnimationFrame(raf); audio.pause(); avVideo.pause(); if(introVideo) introVideo.pause(); $('#f-play').innerHTML='&#9654; Odtwórz'; }
function seek(t){ T=clamp(t,0,total()-0.001); const off=OFFSET(); if(audio.src){ if(T>=off) audio.currentTime=T-off; else { audio.pause(); audio.currentTime=0; } } if(avVideo.src) avVideo.currentTime=Math.max(0,T-off); if(introVideo){ if(T<off){ introVideo.currentTime=T; if(!playing) introVideo.pause(); } else introVideo.pause(); } render(T); }

// ---------- sterowanie ----------
if(!REMOTION){
  $('#f-play').addEventListener('click', ()=> playing?pause():play());
  $('#f-range').addEventListener('input', e=> seek(e.target.value/1000*total()));
  $('#f-prev').addEventListener('click', ()=>{ const si=S.findIndex(s=>T<s.start+s.dur); const s=S[Math.max(0,(T-S[si].start<1.5)?si-1:si)]; seek(s.start); });
  $('#f-next').addEventListener('click', ()=>{ const si=S.findIndex(s=>T<s.start+s.dur); seek(S[Math.min(S.length-1,si+1)].start); });
  $('#f-rate').addEventListener('change', e=>{ rate=+e.target.value; audio.playbackRate=rate; avVideo.playbackRate=rate; });
  $('#f-subs').addEventListener('change', e=> sub.classList.toggle('off', !e.target.checked));
  $('#f-full').addEventListener('click', ()=>{ (box.requestFullscreen||box.webkitRequestFullscreen).call(box); });
  document.addEventListener('fullscreenchange', ()=>{ setTimeout(fit,50); });
  S.forEach((s,i)=>{ const sp=document.createElement('span'); sp.tabIndex=0; sp.title=s.tytul; sp.addEventListener('click',()=>seek(s.start)); sp.addEventListener('keydown',e=>{ if(e.key==='Enter') seek(s.start); }); chapters.appendChild(sp); });
  const cl=$('#f-chaplist'); S.forEach((s,i)=>{ const b=document.createElement('button'); b.type='button'; const mm=t=>Math.floor(t/60)+':'+String(Math.floor(t%60)).padStart(2,'0'); b.innerHTML='<b>'+mm(s.start)+'</b><span>'+s.tytul+'</span><small>strona '+s.strona+' druku · '+NAR[i].split(' ').length+' słów</small>'; b.addEventListener('click',()=>{ seek(s.start); if(!playing) play(); }); cl.appendChild(b); });
  document.addEventListener('keydown', e=>{ if(e.target.matches('input,select,textarea,button,summary')) return; if(e.key===' '){ e.preventDefault(); playing?pause():play(); } if(e.key==='ArrowRight'){ $('#f-next').click(); } if(e.key==='ArrowLeft'){ $('#f-prev').click(); } });
  // zasoby: głos, napisy, awatar
  function wczytajAudio(src, nazwa){ pause(); audio.src=src; audio.addEventListener('loadedmetadata', ()=>{ if(!SRT){ skalujDoNagrania(audio.duration); } $('#f-st-mp3').textContent='Wczytano: '+nazwa+' · '+Math.round(audio.duration)+' s. Kliknij „Odtwórz”.'; $('#f-st-mp3').classList.add('ok'); seek(0); }, {once:true}); }
  $('#f-file-mp3').addEventListener('change', e=>{ const f=e.target.files[0]; if(!f) return; wczytajAudio(URL.createObjectURL(f), f.name); });
  $('#f-glos').addEventListener('change', e=>{ const v=e.target.value; if(!v){ pause(); audio.removeAttribute('src'); audio.load(); S.forEach(s=>s.dur0=s.dur); ustawCzasy(null); $('#f-st-mp3').textContent='Film gra w ciszy.'; $('#f-st-mp3').classList.remove('ok'); seek(0); return; } wczytajAudio(v, e.target.options[e.target.selectedIndex].text); });
  $('#f-file-srt').addEventListener('change', e=>{ const f=e.target.files[0]; if(!f) return; f.text().then(txt=>{ const ok=zastosujSrt(txt); $('#f-st-srt').textContent='Wczytano: '+f.name+' · '+SRT.length+' napisów'+(ok?' · sceny dosunięte do napisów.':' · nie udało się dopasować scen, zostają proporcje.'); $('#f-st-srt').classList.add('ok'); render(T); }); });
  $('#f-file-mp4').addEventListener('change', e=>{ const f=e.target.files[0]; if(!f) return; avVideo.src=URL.createObjectURL(f); avVideo.muted=!!audio.src; av.classList.add('has'); $('#f-st-mp4').textContent='Wczytano: '+f.name+'. Awatar mówi w kole i na pełnym ekranie.'; $('#f-st-mp4').classList.add('ok'); });
  $('#f-mute-av').addEventListener('change', e=>{ avVideo.muted=e.target.checked; });
}
function zastosujSrt(txt){ SRT=parseSrt(txt); const off=OFFSET(); SRT.forEach(c=>{ c.start+=off; c.end+=off; }); const norm=x=>x.toLowerCase().replace(/[^\p{L}\p{N} ]/gu,''); const starty=S.map((s,i)=>{ if(s.intro) return 0; const first=norm(NAR[i]).split(' ').slice(0,3).join(' '); const cue=SRT.find(c=>norm(c.text).includes(first)); return cue?cue.start:null; }); const ok=starty.every(x=>x!==null); if(ok) ustawCzasy(starty); return ok; }
function parseSrt(txt){ const out=[]; const bl=txt.replace(/\r/g,'').split(/\n\n+/); const tm=s=>{ const m=s.match(/(\d+):(\d+):(\d+)[,.](\d+)/); return +m[1]*3600+ +m[2]*60+ +m[3]+ +m[4]/1000; }; for(const b of bl){ const L=b.split('\n'); const ti=L.findIndex(l=>l.includes('-->')); if(ti<0) continue; const [a,c]=L[ti].split('-->'); out.push({start:tm(a),end:tm(c),text:L.slice(ti+1).join(' ').trim()}); } return out; }

// ---------- start ----------
let readyResolve; window.__filmReadyPromise=new Promise(r=>{ readyResolve=r; });
window.__film={ seek, render, total, sceny:S, get t(){return T;}, awatarPos:()=>AVPOS, srt:()=>SRT };
const t0=parseFloat(Q.get('t')||'0');
const fontsReady = (document.fonts && document.fonts.ready) || Promise.resolve();
if(REMOTION){ // Remotion: ?dur=<sekundy MP3>&srt=napisy.srt  → sceny w rytmie nagrania; awatar rysuje Remotion
  const dur=parseFloat(Q.get('dur')||'0'), srtUrl=Q.get('srt');
  const go=()=>{ if(dur>0 && !SRT){ skalujDoNagrania(dur); } fontsReady.then(()=>{ camCache.clear(); seek(isFinite(t0)?t0:0); readyResolve(true); }); };
  if(srtUrl){ fetch(srtUrl).then(r=>r.ok?r.text():Promise.reject()).then(txt=>{ zastosujSrt(txt); go(); }).catch(go); } else go();
} else {
  seek(isFinite(t0)?t0:0);
  // domyślne nagranie Twoim głosem (narracja.mp3 obok filmu) – jeśli jest, film gra z dźwiękiem po kliknięciu „Odtwórz”
  const domyslneAudio = Q.get('audio') || 'narracja.mp3';
  fetch(domyslneAudio, {method:'HEAD'}).then(r=>{ if(!r.ok) throw 0; return domyslneAudio; }).then(src=>{ audio.src=src; audio.addEventListener('loadedmetadata', ()=>{ if(!SRT){ skalujDoNagrania(audio.duration); } $('#f-st-mp3').textContent='Nagranie z ElevenLabs wczytane: '+Math.round(audio.duration)+' s. Kliknij „Odtwórz”.'; $('#f-st-mp3').classList.add('ok'); render(T); }, {once:true}); }).catch(()=>{ $('#f-st-mp3').textContent='Po intro film gra w ciszy z napisami. Narrację Twoim głosem z HeyGen dodasz plikiem MP3 albo z listy.'; });
  fontsReady.then(()=>{ camCache.clear(); render(T); readyResolve(true); });
}
})();
"""


def buduj():
    zr = ZRODLO.read_text(encoding="utf-8")
    css_druk, strony = przygotuj_druk(zr)
    nar = czytaj_narracje()
    sceny = []
    for s, a in zip(SCENY, nar):
        s2 = dict(s)
        s2["dur"] = s.get("dur_stala") or dur_sceny(a)
        sceny.append(s2)

    foto = {
        "klocki": {"src": "foto/klocki.webp", "alt": "Mocne strony: klocki, planety, pamięć wzrokowa"},
        "zespol": {"src": "foto/zespol.webp", "alt": "Zespół i rodzic przy jednym stole"},
        "sluchawki": {"src": "foto/sluchawki.webp", "alt": "Strefa wyciszenia, słuchawki, wizualny plan dnia"},
        "aac": {"src": "foto/aac.webp", "alt": "Tablica wyboru AAC – ta sama w placówce i w domu"},
        "podpis": {"src": "foto/podpis.webp", "alt": "Podpisy Zespołu i rodzica"},
    }
    for k, v in foto.items():
        if not (TU / v["src"]).exists():
            v["src"] = "data:image/svg+xml;utf8," + (
                "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 640 360'><rect width='640' height='360' fill='%231F1740'/>"
                "<circle cx='320' cy='150' r='60' fill='%232D1B69' stroke='%23E8450A' stroke-width='4'/>"
                "<text x='320' y='260' text-anchor='middle' font-family='Mulish,Arial' font-size='22' fill='%23B6A6DF'>kliknij, aby wstawić zdjęcie</text></svg>"
            )

    narracja_txt = NARRACJA.read_text(encoding="utf-8").strip()
    total = sum(s["dur"] for s in sceny)
    mm = f"{int(total // 60)}:{int(total % 60):02d}"

    html = f"""<title>Ocena Funkcjonalna · Film</title>
<meta name="description" content="Interaktywny film: druk Oceny Funkcjonalnej (EduPlaner 2026) wypełnia się sam, z awatarem, głosem i podstawą prawną.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{css_druk}
{CSS_FILM}
</style>
<div class="f-wrap">
  <div class="f-top">
    <h1>Ocena Funkcjonalna · film <small>druk wypełnia się sam · {len(sceny)} scen · ok. {mm}</small></h1>
    <span class="f-badge">dane przykładowe · dziecko fikcyjne</span>
  </div>

  <div class="f-stage-box" id="f-stage-box">
    <div class="f-stage" id="f-stage" style="--ax:1560;--ay:224;--ad:260">
      <div class="f-bar">
        <div class="f-brand"><i>§</i>Ocena Funkcjonalna <small>EduPlaner 2026</small></div>
        <div class="f-chapters" id="f-chapters"></div>
        <div class="f-time" id="f-time">0:00 / {mm}</div>
      </div>
      <div class="f-druk" id="f-druk">
        <div class="f-druk-cam" id="f-cam">
{strony}
        </div>
        <div class="f-druk-dim" id="f-dim"></div>
        <div class="f-przyklad">Przykład · dane fikcyjne</div>
      </div>
      <div class="f-side" id="f-side">
        <div class="f-scene" id="f-scene"><div class="k">Scena 1</div><h2>Jak powstaje raport</h2></div>
        <div class="f-law" id="f-law"><div class="h"><i>§</i>Podstawa prawna</div><ul></ul></div>
        <div class="f-foto" id="f-foto" tabindex="0" role="button" aria-label="Zmień zdjęcie sceny"><img alt=""><div class="cap"></div><div class="swap">Zmień zdjęcie</div></div>
      </div>
      <div class="f-av" id="f-av">
        <div class="ring2"></div><div class="ring"></div>
        <div class="disc">
          <video class="hg" playsinline preload="auto"></video>
          <video class="intro" playsinline preload="auto" src="awatar/ewa_pctp_intro.webm"></video>
          <div class="ph"><img class="ewa" src="awatar/ewa_pctp.png" alt="Ewa PCTP – awatar autorki"></div>
        </div>
        <div class="talk"><i></i><i></i><i></i><i></i><i></i></div>
      </div>
      <div class="f-title" id="f-title"><div class="nad"></div><h2></h2><div class="pod"></div></div>
      <div class="f-sub" id="f-sub"></div>
    </div>
  </div>

  <div class="f-ctl">
    <button class="f-btn primary" id="f-play" type="button">&#9654; Odtwórz</button>
    <button class="f-btn" id="f-prev" type="button" title="Poprzednia scena (←)">&#9664;</button>
    <button class="f-btn" id="f-next" type="button" title="Następna scena (→)">&#9654;</button>
    <input class="f-range" id="f-range" type="range" min="0" max="1000" value="0" aria-label="Oś czasu">
    <span class="t" id="f-ctl-time">0:00 / {mm}</span>
    <select id="f-rate" aria-label="Tempo"><option value="0.75">0,75×</option><option value="1" selected>1×</option><option value="1.25">1,25×</option><option value="1.5">1,5×</option></select>
    <label class="sw"><input type="checkbox" id="f-subs" checked> napisy</label>
    <button class="f-btn" id="f-full" type="button">Pełny ekran</button>
  </div>
  <div class="f-chaplist" id="f-chaplist"></div>

  <div class="f-grid">
    <div class="f-card"><h3><i>1</i>Twój głos · narracja</h3><p>Wczytaj nagranie narracji Twoim głosem (np. <code>narracja.mp3</code> z HeyGen, <code>bash film/generuj.sh awatar</code>). Plik staje się zegarem filmu, a sceny rozciągają się do jego długości. Bez pliku po intro film gra w ciszy z napisami.</p><select id="f-glos" hidden><option value="" selected></option></select><input type="file" id="f-file-mp3" accept="audio/*"><div class="st" id="f-st-mp3">Bez nagrania film gra w ciszy, w tempie ok. 150 słów na minutę.</div></div>
    <div class="f-card"><h3><i>2</i>Napisy · SRT</h3><p>Plik z ElevenLabs (<code>--srt</code>). Sceny dosuwają się do początków zdań, a napisy mają prawdziwe znaczniki czasu.</p><input type="file" id="f-file-srt" accept=".srt,text/plain"><div class="st" id="f-st-srt">Bez SRT napisy liczone są z długości zdań.</div></div>
    <div class="f-card"><h3><i>3</i>Twój awatar · HeyGen</h3><p>Film MP4 z awatarem mówiącym do tego samego MP3 (<code>heygen_awatar.py --audio</code>, tło fioletowe, kadr <code>circle</code>). Gra w kole i na pełnym ekranie.</p><input type="file" id="f-file-mp4" accept="video/mp4,video/webm"><label class="sw" style="margin-top:6px"><input type="checkbox" id="f-mute-av" checked> wycisz dźwięk awatara (głos gra z MP3)</label><div class="st" id="f-st-mp4">Bez pliku w kole stoi Ewa PCTP (postać ze skilla awatar-ewa).</div></div>
    <div class="f-card"><h3><i>4</i>Zdjęcia</h3><p>Kliknij zdjęcie na scenie, aby podmienić je własnym. Podmiana zapamiętuje się w tej przeglądarce. Skróty: spacja – odtwarzanie, strzałki – sceny.</p><div class="st">Render do MP4: <code>film/remotion</code> (patrz README).</div></div>
  </div>

  <details class="f-nar"><summary>Tekst narracji (do ElevenLabs) · {len(narracja_txt.split())} słów</summary><pre>{narracja_txt}</pre></details>
  <p class="f-foot">Druk: „Ocena Funkcjonalna · podsumowanie WOPF i IPET · obszary ICF”, EduPlaner 2026 (oryginalny markup i style). Podstawa prawna główna: rozporządzenie ME z 2 marca 2026 r. w sprawie orzeczeń i opinii (Dz. U. 2026 poz. 428), § 7 ust. 6–7 od 1 września 2026 r. Dziecko, placówka i Zespół w filmie są fikcyjne.</p>
</div>
<audio id="f-audio" preload="auto"></audio>
<input type="file" id="f-foto-file" accept="image/*" hidden>
<script>
window.__SCENY__ = {json.dumps(sceny, ensure_ascii=False)};
window.__NARRACJA__ = {json.dumps(nar, ensure_ascii=False)};
window.__FOTO__ = {json.dumps(foto, ensure_ascii=False)};
window.__DANE__ = {json.dumps(D, ensure_ascii=False)};
</script>
<script>
{JS_FILM}
</script>
"""
    WYJSCIE.write_text(html, encoding="utf-8")
    print(f"zapisano {WYJSCIE} ({len(html)//1024} KB), scen: {len(sceny)}, czas ok. {mm}")


if __name__ == "__main__":
    buduj()
