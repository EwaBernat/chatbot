#!/usr/bin/env python3
"""Buduje src/scenariusz.json — treść plansz plus czasy wzięte z narracji.

Treść plansz jest tu zapisana wprost, bo pochodzi z broszury „Cele SMART
w przedszkolu" (SMART-P1) i zmienia się razem z nią. Czasy scen liczone są
z pliku narracji: każdy akapit narracji to jedna plansza.

Gdy w public/ leży wygenerowane MP3, skrypt bierze jego rzeczywistą długość
i rozdziela ją między sceny proporcjonalnie do liczby znaków. Bez MP3 przyjmuje
tempo 150 słów na minutę, więc projekt renderuje się także przed nagraniem.

Użycie:
    python3 skrypty/zbuduj_scenariusz.py [--mp3-sekundy 372.4]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

KORZEN = Path(__file__).resolve().parent.parent
NARRACJA = KORZEN / "public" / "narracja.txt"
WYJSCIE = KORZEN / "src" / "scenariusz.json"
FPS = 30
SLOW_NA_MINUTE = 150
MAX_ZNAKOW_W_NAPISIE = 92

# Treść plansz — po jednej na akapit narracji, w tej samej kolejności.
PLANSZE = [
    {
        "id": "wstep",
        "typ": "tytul",
        "rozdzial": "Wstęp",
        "naglowek": "Cele SMART\nw przedszkolu",
        "podtytul": "Jak napisać cel, który da się zobaczyć, policzyć i obronić przed zespołem, rodzicem i kuratorium.",
        "autor": "mgr Mirosława Ewa Jurczyszyn · pedagog specjalny · PCTP Koszalin · sygn. SMART-P1",
        "odznaki": ["5 liter", "6 kroków", "1 formuła zdania"],
    },
    {
        "id": "zyczenie-narzedzie",
        "typ": "porownanie",
        "rozdzial": "Po co",
        "naglowek": "Cel-życzenie kontra cel-narzędzie",
        "zle": {
            "etykieta": "Cel-życzenie",
            "tekst": "Dziecko będzie lepiej radziło sobie z emocjami i stanie się spokojniejsze.",
            "komentarz": "Nie wiadomo co, ile razy, w jakiej sytuacji ani do kiedy. „Spokojniejsze” to interpretacja dorosłego, a nie zachowanie dziecka.",
        },
        "dobre": {
            "etykieta": "Cel-narzędzie",
            "tekst": "Dziecko rozpozna narastające napięcie i samodzielnie zastosuje strategię wyciszenia (oddech 4-4-4) w 4 na 5 sytuacji trudnych, do końca semestru.",
            "komentarz": "Rozpozna i zastosuje — widać. 4 na 5 — policzysz. Do końca semestru — wiadomo, kiedy podsumować.",
        },
    },
    {
        "id": "trzech-odbiorcow",
        "typ": "lista",
        "rozdzial": "Po co",
        "naglowek": "Cel ma trzech odbiorców",
        "punkty": [
            {"etykieta": "Dziecko", "tekst": "Przez to, co robisz z nim codziennie — cel przekłada się na poniedziałek rano."},
            {"etykieta": "Rodzic", "tekst": "Musi zrozumieć, nad czym pracujecie, i rozpoznać efekt w grudniu."},
            {"etykieta": "Zespół", "tekst": "Dwa razy w roku ocenia efektywność pomocy. To obowiązek, nie dobra wola."},
        ],
        "stopka": "Zasada trzech osób: gdyby jutro zastąpiła Cię inna nauczycielka, czy z samego zapisu wiedziałaby, co robić i co liczyć?",
    },
    {
        "id": "litera-s",
        "typ": "litera",
        "rozdzial": "Anatomia",
        "naglowek": "Pięć liter, pięć pytań kontrolnych",
        "litera": "S",
        "nazwa": "Skonkretyzowany",
        "angielskie": "Specific · co dokładnie widzę",
        "pytanie": "Czy to zachowanie da się zobaczyć albo usłyszeć? Czy dwie różne osoby opiszą je tak samo?",
        "praktyka": "„rozpozna narastające napięcie i zastosuje oddech 4-4-4”",
        "pulapka": "„będzie spokojniejsze”, „poprawi zachowanie” — to Twoja ocena, nie czynność dziecka.",
    },
    {
        "id": "litera-m",
        "typ": "litera",
        "rozdzial": "Anatomia",
        "naglowek": "Pięć liter, pięć pytań kontrolnych",
        "litera": "M",
        "nazwa": "Mierzalny",
        "angielskie": "Measurable · ile i na ile prób",
        "pytanie": "Ile razy? Na ile okazji? Czym to policzę — kartą obserwacji, żetonami, listą?",
        "praktyka": "„w 4 na 5 sytuacji trudnych”, „w 3 kolejnych dniach”, „w 8 na 10 prób”",
        "pulapka": "„często”, „zazwyczaj”, „w większości sytuacji” — tego nie da się policzyć.",
    },
    {
        "id": "litera-a",
        "typ": "litera",
        "rozdzial": "Anatomia",
        "naglowek": "Pięć liter, pięć pytań kontrolnych",
        "litera": "A",
        "nazwa": "Osiągalny",
        "angielskie": "Achievable · następny krok, nie skok",
        "pytanie": "Czy to jeden krok dalej niż to, co dziecko potrafi dziś? Czy mieści się w przyznanym poziomie wsparcia?",
        "praktyka": "Dziecko już wskazuje kolor na planszy → następny krok: połączy kolor ze strategią wyciszenia.",
        "pulapka": "Cel trzy piętra nad punktem wyjścia. Dziecko przez pół roku nie doświadcza sukcesu.",
    },
    {
        "id": "litera-r",
        "typ": "litera",
        "rozdzial": "Anatomia",
        "naglowek": "Pięć liter, pięć pytań kontrolnych",
        "litera": "R",
        "nazwa": "Istotny",
        "angielskie": "Relevant · zmienia codzienność",
        "pytanie": "Czy osiągnięcie tego celu realnie ułatwi dziecku dzień w przedszkolu? Czy wynika z WOPF i z orzeczenia?",
        "praktyka": "Samoregulacja napięcia = warunek uczestnictwa w zabawie, w posiłku, w wyjściu do ogrodu.",
        "pulapka": "Cel skopiowany z internetu albo z zeszłorocznego IPET-u innego dziecka.",
    },
    {
        "id": "litera-t",
        "typ": "litera",
        "rozdzial": "Anatomia",
        "naglowek": "Pięć liter, pięć pytań kontrolnych",
        "litera": "T",
        "nazwa": "Określony w czasie",
        "angielskie": "Time-bound · termin i punkt kontrolny",
        "pytanie": "Do kiedy? I równie ważne: kiedy zajrzę do celu po drodze, żeby zdążyć go zmodyfikować?",
        "praktyka": "„do końca I semestru”, z przeglądem po 8 tygodniach.",
        "pulapka": "„w ciągu roku szkolnego” bez punktu kontrolnego — orientujesz się w maju, że nic się nie działo.",
    },
    {
        "id": "kroki-1-3",
        "typ": "kroki",
        "rozdzial": "Skrypt",
        "naglowek": "Sześć kroków od obserwacji do zapisu",
        "kroki": [
            {"numer": 1, "tytul": "Zobacz i nazwij zachowanie", "opis": "Przez dwa tygodnie zapisuj, co dokładnie się dzieje — bez ocen i bez przyczyn. „Zaciska pięści, oddycha szybciej” zamiast „złości się”."},
            {"numer": 2, "tytul": "Zmierz punkt wyjścia", "opis": "Na 5 trudnych sytuacji — w ilu dziecko poradziło sobie dziś? Przykład: 1 na 5, i to tylko z podpowiedzią."},
            {"numer": 3, "tytul": "Wybierz czasownik, który widać", "opis": "Serce celu. Czy mogę postawić kreskę w chwili, gdy to się stanie?"},
        ],
    },
    {
        "id": "kroki-4-6",
        "typ": "kroki",
        "rozdzial": "Skrypt",
        "naglowek": "Sześć kroków od obserwacji do zapisu",
        "kroki": [
            {"numer": 4, "tytul": "Dopisz miarę i kryterium", "opis": "Liczba + z ilu prób + w jakim okresie. Punkt wyjścia 1/5 → realne kryterium to 3–4 na 5, nie 5 na 5."},
            {"numer": 5, "tytul": "Ustal warunki i poziom wsparcia", "opis": "Samodzielnie / po jednej podpowiedzi słownej / z pomocą gestu. Dopisz gdzie: w sali, w ogrodzie, przy posiłku."},
            {"numer": 6, "tytul": "Wyznacz termin i sposób sprawdzenia", "opis": "Data końcowa plus punkt kontrolny w połowie drogi. Wpisz narzędzie: karta obserwacji, arkusz zliczeń."},
        ],
    },
    {
        "id": "formula",
        "typ": "formula",
        "rozdzial": "Formuła",
        "naglowek": "Jedno zdanie, siedem miejsc do wypełnienia",
        "pola": [
            {"numer": 1, "etykieta": "Kto"},
            {"numer": 2, "etykieta": "W jakiej sytuacji"},
            {"numer": 3, "etykieta": "Z jakim wsparciem"},
            {"numer": 4, "etykieta": "Co zrobi"},
            {"numer": 5, "etykieta": "Miara"},
            {"numer": 6, "etykieta": "Termin"},
            {"numer": 7, "etykieta": "Sprawdzenie"},
        ],
        "zdanie": [
            {"tekst": "Dziecko", "pole": 1},
            {"tekst": " "},
            {"tekst": "w sytuacjach trudnych w sali i w ogrodzie", "pole": 2},
            {"tekst": " "},
            {"tekst": "samodzielnie, bez podpowiedzi słownej dorosłego", "pole": 3},
            {"tekst": ", "},
            {"tekst": "rozpozna narastające napięcie na termometrze i zastosuje strategię wyciszenia", "pole": 4},
            {"tekst": " "},
            {"tekst": "w 4 na 5 obserwowanych sytuacji", "pole": 5},
            {"tekst": ", "},
            {"tekst": "do końca I semestru", "pole": 6},
            {"tekst": ", co potwierdzi "},
            {"tekst": "zapis w karcie obserwacji", "pole": 7},
            {"tekst": "."},
        ],
    },
    {
        "id": "czasowniki",
        "typ": "czasowniki",
        "rozdzial": "Słownik",
        "naglowek": "Bank czasowników",
        "dobre": ["wskaże", "nazwie", "poda", "powtórzy", "zastosuje", "wybierze", "ułoży", "poprosi o…", "zgłosi", "podejdzie", "odłoży", "poczeka"],
        "zle": ["zrozumie", "poczuje", "będzie wiedziało", "uświadomi sobie", "polubi", "nauczy się", "poprawi", "wzmocni", "rozwinie"],
        "naprawa": "Naprawa: zapytaj „po czym poznam, że dziecko to zrozumiało?” i wpisz właśnie tę odpowiedź. „zrozumie zasadę” → „poda zasadę własnymi słowami lub wskaże ją na obrazku”.",
    },
    {
        "id": "termometr",
        "typ": "termometr",
        "rozdzial": "Wzorzec",
        "naglowek": "Rozbiór celu: „Termometr napięcia”",
        "strefy": [
            {"od": 5, "do": 6, "nazwa": "Strefa czerwona", "opis": "Za późno na naukę — tylko bezpieczeństwo."},
            {"od": 3, "do": 4, "nazwa": "Strefa żółta", "opis": "Tu działa strategia — to jest Twój moment."},
            {"od": 1, "do": 2, "nazwa": "Strefa zielona", "opis": "Spokój, gotowość do uczenia się."},
        ],
        "karta": [True, True, False, True, True],
    },
    {
        "id": "obszary",
        "typ": "obszary",
        "rozdzial": "Bank celów",
        "naglowek": "Dziewięć obszarów nowej podstawy",
        "obszary": [
            {"nazwa": "Społeczny", "opis": "relacje · współpraca · przynależność"},
            {"nazwa": "Osobisty", "opis": "tożsamość · emocje · granice"},
            {"nazwa": "Językowy", "opis": "mowa · komunikacja · droga do czytania"},
            {"nazwa": "Matematyczny", "opis": "orientacja · rytmy · intuicja"},
            {"nazwa": "Przyrodniczy", "opis": "obserwacja · przyroda z bliska"},
            {"nazwa": "Techniczny", "opis": "praca rąk · narzędzia · konstruowanie"},
            {"nazwa": "Cyfrowy", "opis": "rozumienie techniki · higiena cyfrowa"},
            {"nazwa": "Artystyczny", "opis": "proces twórczy · ekspresja emocji"},
            {"nazwa": "Ruchowy", "opis": "motoryka · postawa · bezpieczeństwo"},
        ],
        "stopka": "Dz.U. 2026 poz. 378 — w dokumentacji dopisz numer konkretnego osiągnięcia z załącznika nr 1.",
    },
    {
        "id": "swiatla",
        "typ": "swiatla",
        "rozdzial": "Ewaluacja",
        "naglowek": "Zielony, żółty, czerwony — co zrobić z celem",
        "swiatla": [
            {"kolor": "zielony", "wynik": "4–5 na 5", "decyzja": "Cel osiągnięty — podnieś poprzeczkę w stronę generalizacji.", "ruch": "Inne miejsce, inna osoba dorosła, większa grupa. Nowy cel buduj od tego, co dziecko już robi."},
            {"kolor": "zolty", "wynik": "2–3 na 5", "decyzja": "Cel zostaje — zmieniasz drogę do niego.", "ruch": "Zmniejsz krok, dołóż podpowiedź, wydłuż czas. Zwiększ liczbę prób i dodaj wzmocnienie."},
            {"kolor": "czerwony", "wynik": "0–1 na 5", "decyzja": "Cofnij cel o etap — do poziomu, na którym dziecko odnosi sukces.", "ruch": "Uprość zadanie, zmień kanał na obraz lub gest, zweryfikuj poziom wsparcia i sam zapis celu."},
        ],
    },
    {
        "id": "ewaluacja",
        "typ": "lista",
        "rozdzial": "Ewaluacja",
        "naglowek": "Ewaluacja w trzech zdaniach",
        "punkty": [
            {"etykieta": "1 · Liczba", "tekst": "„W okresie IX–I odnotowano 4 na 5 sytuacji.”"},
            {"etykieta": "2 · Warunki", "tekst": "„Samodzielnie, bez podpowiedzi, w sali i w ogrodzie.”"},
            {"etykieta": "3 · Wniosek i decyzja", "tekst": "„Cel osiągnięty, przechodzimy do generalizacji na wyjścia poza teren przedszkola.”"},
        ],
        "stopka": "Taki zapis jest zarazem oceną efektywności pomocy i materiałem do wielospecjalistycznej oceny poziomu funkcjonowania.",
    },
    {
        "id": "prawo",
        "typ": "lista",
        "rozdzial": "Prawo",
        "naglowek": "Podstawa prawna",
        "punkty": [
            {"etykieta": "Prawo oświatowe\nDz.U. 2025 poz. 1043", "tekst": "Przedszkole dostosowuje treści, metody i organizację do możliwości dziecka."},
            {"etykieta": "Pomoc p-p\nDz.U. 2023 poz. 1798, § 20", "tekst": "Obserwacja pedagogiczna i ocena efektywności udzielanej pomocy."},
            {"etykieta": "Kształcenie specjalne\nDz.U. 2020 poz. 1309, § 6", "tekst": "Zespół dwa razy w roku ocenia program i w miarę potrzeb go modyfikuje."},
        ],
        "stopka": "Bez liczby w celu żadnej z tych ocen nie da się sporządzić.",
    },
    {
        "id": "zakonczenie",
        "typ": "zakonczenie",
        "rozdzial": "Prawo",
        "naglowek": "Weź jeden swój cel\ni przepuść go przez pięć filtrów.",
        "kontakt": [
            {"etykieta": "Strona", "wartosc": "www.eduplaner2026.pl"},
            {"etykieta": "E-mail", "wartosc": "kontakt@eduplaner2026.pl"},
            {"etykieta": "Telefon", "wartosc": "[usunięto]"},
        ],
        "haslo": "Mniej dokumentów. Więcej edukacji.",
    },
]


def akapity(tekst: str) -> list[str]:
    return [a.strip() for a in re.split(r"\n\s*\n", tekst.strip()) if a.strip()]


def zdania(akapit: str) -> list[str]:
    """Dzieli akapit na wiersze napisów: po zdaniach, a długie zdania po przecinkach."""
    surowe = [z.strip() for z in re.split(r"(?<=[.!?])\s+", akapit.replace("\n", " ")) if z.strip()]
    wynik: list[str] = []
    for z in surowe:
        if len(z) <= MAX_ZNAKOW_W_NAPISIE:
            wynik.append(z)
            continue
        bufor = ""
        for czesc in re.split(r"(?<=,)\s+", z):
            kandydat = f"{bufor} {czesc}".strip()
            if bufor and len(kandydat) > MAX_ZNAKOW_W_NAPISIE:
                wynik.append(bufor)
                bufor = czesc
            else:
                bufor = kandydat
        if bufor:
            wynik.append(bufor)
    return wynik


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--mp3-sekundy", type=float, default=None,
                   help="rzeczywista długość nagranej narracji; bez niej przyjmowane jest 150 słów/min")
    p.add_argument("--audio", default="narracja.mp3", help="nazwa pliku audio w public/ (pusta = bez dźwięku)")
    p.add_argument("--awatar", default="awatar.mp4", help="nazwa pliku awatara w public/ (pusta = plansza zastępcza)")
    args = p.parse_args()

    tekst = NARRACJA.read_text(encoding="utf-8")
    czesci = akapity(tekst)
    if len(czesci) != len(PLANSZE):
        print(f"BŁĄD: narracja ma {len(czesci)} akapitów, a plansz jest {len(PLANSZE)}.")
        print("Każdy akapit narracji to jedna plansza — wyrównaj jedno do drugiego.")
        return 1

    znaki = [len(c) for c in czesci]
    razem_znakow = sum(znaki)
    slowa = sum(len(c.split()) for c in czesci)

    calosc = args.mp3_sekundy if args.mp3_sekundy else slowa / SLOW_NA_MINUTE * 60
    zrodlo = "z pliku MP3" if args.mp3_sekundy else f"szacunek {SLOW_NA_MINUTE} słów/min"

    sceny = []
    napisy = []
    kursor = 0.0
    for plansza, akapit, ile_znakow in zip(PLANSZE, czesci, znaki):
        trwanie = calosc * ile_znakow / razem_znakow
        scena = dict(plansza)
        scena["sekundy"] = round(trwanie, 3)
        sceny.append(scena)

        wiersze = zdania(akapit)
        suma = sum(len(w) for w in wiersze) or 1
        lokalny = kursor
        for w in wiersze:
            dl = trwanie * len(w) / suma
            napisy.append({"od": round(lokalny, 3), "do": round(lokalny + dl, 3), "tekst": w})
            lokalny += dl
        kursor += trwanie

    scenariusz = {
        "tytul": "Cele SMART w przedszkolu — szkolenie dla nauczycieli",
        "fps": FPS,
        "audio": args.audio or None,
        "awatar": args.awatar or None,
        "sceny": sceny,
        "napisy": napisy,
    }
    WYJSCIE.write_text(json.dumps(scenariusz, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    minuty, sekundy = divmod(calosc, 60)
    print(f"Zapisano {WYJSCIE.relative_to(KORZEN)}")
    print(f"  scen: {len(sceny)} · wierszy napisów: {len(napisy)}")
    print(f"  słów w narracji: {slowa}")
    print(f"  długość filmu: {int(minuty)} min {sekundy:04.1f} s ({zrodlo})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
