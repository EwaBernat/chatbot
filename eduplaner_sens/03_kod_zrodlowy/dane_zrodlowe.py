# -*- coding: utf-8 -*-
"""Bank celów SMART — profil sensoryczny (przedszkole) · EduPlaner 2026 · PCTP.

Autorka treści: mgr Mirosława Ewa Jurczyszyn, pedagog specjalny, PCTP Koszalin.

To jest JEDYNE źródło treści merytorycznej modułu. Wszystkie pliki JSON, druki
HTML i manifest nagrań powstają z tego pliku — nie odwrotnie. Poprawka autorki
wchodzi tutaj i po przebudowie rozchodzi się do wszystkich materiałów.

Struktura odpowiada bankowi KPOF i modułowi ABC/FBA:
    21 wskaźników  =  7 zmysłów × 3 sektory objawów
    189 celów      =  21 wskaźników × 3 poziomy wsparcia × 3 wersje wiekowe
"""

MODUL = {
    "nazwa": "Profil sensoryczny — bank celów SMART (przedszkole)",
    "kod": "SENS",
    "wersja": "2026.1",
    "autorka": "mgr Mirosława Ewa Jurczyszyn, pedagog specjalny, PCTP Koszalin",
    "aplikacja": "EduPlaner 2026",
    "druk_zrodlowy": "Profil sensoryczny (przedszkole) 2026 — obserwacja pogłębiona WOPF · SI",
    "podstawa_merytoryczna": (
        "Narzędzie obserwacyjne oparte na elementach Profilu Sensorycznego Winnie Dunn "
        "(Sensory Profile 2 — model czterech wzorców przetwarzania sensorycznego) oraz na "
        "teorii integracji sensorycznej A. Jean Ayres. Nie zastępuje diagnozy SI."
    ),
    "podstawa_prawna": [
        "Rozp. MEN z 14.02.2017 r. w sprawie podstawy programowej wychowania przedszkolnego "
        "(Dz.U. 2017 poz. 356, ze zm.) — fizyczny obszar rozwoju.",
        "Rozp. MEN z 9.08.2017 r. w sprawie pomocy psychologiczno-pedagogicznej "
        "(Dz.U. 2017 poz. 1591).",
        "Rozp. MEN z 9.08.2017 r. w sprawie kształcenia specjalnego (Dz.U. 2017 poz. 1578) — "
        "zajęcia rewalidacyjne dla dzieci z orzeczeniem.",
    ],
    # Zdanie, którego nie wolno zgubić przy wpinaniu modułu do aplikacji:
    "zasada_modulu": (
        "Cel z tego banku opisuje STRATEGIĘ SENSORYCZNĄ dziecka — co dziecko ROBI, żeby "
        "poradzić sobie z bodźcem — a nie zanik objawu. „Nie będzie zatykał uszu” nie jest "
        "celem z tego modułu. „Założy słuchawki wygłuszające, zanim hałas w szatni go "
        "przeciąży” — jest. Każdy wskaźnik niesie pole `strategia_sensoryczna`; cel bez "
        "niego traci sens terapeutyczny."
    ),
}

# --- 7 zmysłów z druku obserwacji ------------------------------------------
ZMYSLY = {
    "wzrok":         {"rzymska": "I",   "nazwa": "Wzrok",         "icf": "b210",
                      "opis": "widzenie i przetwarzanie bodźców wzrokowych"},
    "sluch":         {"rzymska": "II",  "nazwa": "Słuch",         "icf": "b230",
                      "opis": "słyszenie i przetwarzanie bodźców słuchowych"},
    "dotyk":         {"rzymska": "III", "nazwa": "Dotyk",         "icf": "b265",
                      "opis": "czucie powierzchniowe, faktury, bliskość fizyczna"},
    "smak":          {"rzymska": "IV",  "nazwa": "Smak",          "icf": "b250",
                      "opis": "smak i konsystencje pokarmów, czucie w obrębie jamy ustnej"},
    "wech":          {"rzymska": "V",   "nazwa": "Węch",          "icf": "b255",
                      "opis": "zapachy i reakcje na nie"},
    "propriocepcja": {"rzymska": "VI",  "nazwa": "Propriocepcja", "icf": "b760",
                      "opis": "czucie głębokie, napięcie mięśniowe, dozowanie siły"},
    "rownowaga":     {"rzymska": "VII", "nazwa": "Równowaga",     "icf": "b235",
                      "opis": "układ przedsionkowy — ruch, wysokość, zmiana pozycji"},
}

# --- 3 sektory objawów (z druku: nadwrażliwość · podwrażliwość · biały szum) -
SEKTORY = {
    "nadwrazliwosc": {
        "nazwa": "Nadwrażliwość",
        "skrot": "NAD",
        "kierunek": "↑ za dużo bodźca",
        "opis": "układ nerwowy odbiera bodziec jako zbyt silny — dziecko broni się, ucieka, unika",
        "cel_ogolny": "obniżyć próg przeciążenia: dać dziecku sposób na osłonę i wycofanie się z bodźca ZANIM nastąpi reakcja obronna",
    },
    "podwrazliwosc": {
        "nazwa": "Podwrażliwość / poszukiwanie bodźców",
        "skrot": "POD",
        "kierunek": "↓ za mało bodźca",
        "opis": "układ nerwowy odbiera bodziec jako zbyt słaby — dziecko dobiera go sobie samo, często w sposób nieakceptowany",
        "cel_ogolny": "dać bodziec w formie zaplanowanej i bezpiecznej, żeby dziecko nie musiało dobierać go kosztem zabawy, przedmiotów lub innych dzieci",
    },
    "bialy_szum": {
        "nazwa": "Biały szum (reaktywność zmienna)",
        "skrot": "SZUM",
        "kierunek": "↕ raz za dużo, raz za mało",
        "opis": "reakcja na ten sam bodziec zmienia się z dnia na dzień — dziecko nie może przewidzieć własnej reakcji",
        "cel_ogolny": "nauczyć rozpoznawania i sygnalizowania własnego stanu, a dorosłego — codziennego sprawdzania poziomu, zamiast zakładania stałego profilu",
    },
}

# --- 3 poziomy wsparcia (jak w druku FBA-T i IPET) --------------------------
# Uwaga merytoryczna: na Poziomie I kryterium ZOSTAJE 4 z 5 — rośnie trudność
# samego zachowania, nie liczba prób. „Za każdym razem” to w przedszkolu cel
# nie do osiągnięcia.
POZIOMY = {
    "III": {
        "nazwa": "Poziom III — wsparcie intensywne",
        "wsparcie": "z pełnym wsparciem dorosłego (dorosły obok przez cały czas, prowadzenie ręka w rękę, wspólne wykonanie)",
        "podpowiedz": "fizyczna i słowna",
        "rola_doroslego": "dorosły rozpoznaje sygnał przeciążenia za dziecko, zapowiada i wykonuje strategię razem z nim",
        "kolejnosc": 1,
    },
    "II": {
        "nazwa": "Poziom II — wsparcie umiarkowane",
        "wsparcie": "po podpowiedzi słownej i pokazaniu karty-symbolu, z dorosłym w pobliżu",
        "podpowiedz": "słowna i obrazkowa",
        "rola_doroslego": "dorosły podaje kartę i nazywa stan, dziecko wykonuje strategię samo",
        "kolejnosc": 2,
    },
    "I": {
        "nazwa": "Poziom I — wsparcie podstawowe",
        "wsparcie": "samodzielnie, po jednym przypomnieniu wizualnym (karta w kąciku, plan dnia)",
        "podpowiedz": "wizualna",
        "rola_doroslego": "dorosły tylko obserwuje i odnotowuje; strategię inicjuje dziecko",
        "kolejnosc": 3,
    },
}

# --- 3 wersje wiekowe -------------------------------------------------------
WIEK = {
    "3-4": {"nazwa": "3–4 lata", "opis": "grupa młodsza — polecenie 2–3 słowa, symbol zawsze przy słowie, czas zadania do 3 minut"},
    "5":   {"nazwa": "5 lat",    "opis": "grupa średnia — polecenie jednozdaniowe, dziecko nazywa stan słowem, czas zadania 5–7 minut"},
    "6":   {"nazwa": "6 lat",    "opis": "grupa zerówkowa — dziecko planuje strategię z wyprzedzeniem, czas zadania 8–10 minut"},
}

# --- progi: kryterium i horyzont z sumy zmysłu (0–24) -----------------------
# Suma zmysłu z druku obserwacji przelicza się na natężenie 0–10 (× 10/24).
# Kryterium i horyzont NIE są stałe — biorą się z pasma, w którym wypadł zmysł.
PROGI = [
    {
        "zakres_sumy": [0, 5], "natezenie": "0–2",
        "pasmo": "modulacja prawidłowa — zasób",
        "decyzja": "cel podtrzymujący; obserwacja bez interwencji",
        "proba": "3 z 5",
        "horyzont": {"mianownik": "12 tygodni", "dopelniacz": "12 tygodni", "miejscownik": "12 tygodniach"},
    },
    {
        "zakres_sumy": [6, 12], "natezenie": "3–5",
        "pasmo": "modulacja częściowo zaburzona — monitorowanie",
        "decyzja": "dieta sensoryczna wpisana do planu dnia; weryfikacja w połowie okresu",
        "proba": "4 z 5",
        "horyzont": {"mianownik": "8 tygodni", "dopelniacz": "8 tygodni", "miejscownik": "8 tygodniach"},
    },
    {
        "zakres_sumy": [13, 24], "natezenie": "6–10",
        "pasmo": "duża nad- lub podwrażliwość — priorytet diety sensorycznej",
        "decyzja": "dieta sensoryczna codziennie, konsultacja terapeuty SI, krótki cykl weryfikacji",
        "proba": "4 z 5",
        "horyzont": {"mianownik": "4 tygodnie", "dopelniacz": "4 tygodni", "miejscownik": "4 tygodniach"},
    },
]

TORY_ZAJEC = [
    "rewalidacja",
    "pomoc psychologiczno-pedagogiczna",
    "kształcenie specjalne (IPET)",
]

RODZAJE_ZAJEC = [
    "zajęcia o charakterze terapeutycznym (terapia SI)",
    "zajęcia rewalidacyjne",
    "zajęcia korekcyjno-kompensacyjne",
    "zajęcia rozwijające kompetencje emocjonalno-społeczne",
    "wsparcie nauczyciela współorganizującego kształcenie",
    "porada / konsultacja (terapeuta SI)",
]


# ---------------------------------------------------------------------------
# 21 WSKAŹNIKÓW = 7 zmysłów × 3 sektory objawów
# ---------------------------------------------------------------------------
# `strategia_sensoryczna` to serce rekordu — to ona wchodzi w cel SMART.
# `czynnosc` różni się wersją wiekową, `instrukcja_slowna` i `polecenia`
# — poziomem wsparcia. Teksty z kluczy `*_dla_dziecka` mówi się DZIECKU
# (krótko, bez trudnych słów) i to one są nagrywane głosem autorki.

WSKAZNIKI = [

# ===== I · WZROK (b210) ====================================================
{
    "id": "SENS-01", "kod": "WZR-NAD", "zmysl": "wzrok", "sektor": "nadwrazliwosc",
    "nazwa": "Osłona wzrokowa przy jasnym świetle i nadmiarze bodźców",
    "objawy": [
        "Mruży oczy, osłania je lub odwraca wzrok przy jasnym świetle, słońcu, migoczących ekranach",
        "Męczy się przy pracy wzrokowej (obrazek, książeczka, układanka) szybciej niż rówieśnicy",
        "Przeszkadza mu ruch i nadmiar bodźców wzrokowych (dekoracje, tłum, wirujące zabawki)",
    ],
    "opis_dla_doroslego": (
        "Dziecko odbiera światło i nadmiar szczegółów jako bodziec za silny. Pracę wzrokową "
        "przerywa nie z niechęci, lecz z przeciążenia — objawem jest mrużenie oczu, "
        "pocieranie ich, odwracanie głowy i narastające rozdrażnienie."
    ),
    "strategia_sensoryczna": (
        "Dziecko samo sięga po osłonę wzrokową (parawan na stoliku, daszek, miejsce tyłem do okna) "
        "albo przechodzi do kącika o małej liczbie bodźców — ZANIM zacznie mrużyć oczy i wycofywać się z zadania."
    ),
    "sygnal_dziecka": "karta „ZA JASNO” podana dorosłemu lub położona na blacie",
    "kontekst": "przy stoliku i w zabawie w sali, w której świeci mocne światło lub wisi dużo dekoracji",
    "czynnosc": {
        "3-4": "postawi parawan na stoliku albo przesiądzie się na miejsce tyłem do okna i wróci do układanki",
        "5":   "poda kartę „ZA JASNO”, wybierze osłonę (parawan albo daszek) i dokończy zadanie wzrokowe",
        "6":   "przed zadaniem wzrokowym samo przygotuje stanowisko o małej liczbie bodźców — parawan, jedna pomoc na blacie, miejsce z dala od okna",
    },
    "wskaznik_obserwacji": "liczba sytuacji, w których dziecko użyło osłony wzrokowej zamiast przerwać zadanie",
    "dieta_sensoryczna": [
        "krótkie zadania wzrokowe (3–7 minut) przeplatane przerwą z zamkniętymi oczami lub patrzeniem w dal",
        "„kącik małych bodźców” — ściana bez dekoracji, jedna pomoc na blacie",
        "przyciemnienie części sali w porze zajęć przy stoliku",
    ],
    "dostosowania": [
        "miejsce tyłem do okna i z dala od migoczących świateł oraz wirujących zabawek",
        "większe, wyraźne obrazki z dużym odstępem między elementami",
        "usunięcie dekoracji z pola pracy dziecka (ściana i blat)",
    ],
    "pomoc": {
        "nazwa": "Parawan stolikowy „Spokojne oczy” z kartą ZA JASNO",
        "opis_dla_doroslego": (
            "Składany parawan z szarego kartonu (3 pola po 25 × 30 cm) ustawiany na blacie, "
            "wraz z kartą-symbolem „ZA JASNO” w kolorze pomarańczowym. Parawan odcina boczne bodźce "
            "wzrokowe; karta daje dziecku sposób, żeby o osłonę poprosić."
        ),
        "trzy_kroki_uzycia": [
            "Postaw parawan po lewej stronie blatu i połóż kartę „ZA JASNO” w zasięgu ręki dziecka.",
            "Przy pierwszym mrużeniu oczu pokaż kartę i powiedz krótko, co robimy — nie czekaj na wycofanie.",
            "Po zadaniu złóż parawan razem z dzieckiem i odnotuj, czy sygnał wyszedł od dziecka.",
        ],
        "wskazowka_dla_doroslego": (
            "Nie zabieraj parawanu za wcześnie „bo już nie potrzebuje”. Osłona ma zostać dostępna także "
            "wtedy, gdy dziecko przez kilka dni z niej nie korzysta — to ona daje poczucie kontroli."
        ),
        "etykieta_dla_dziecka": "ZA JASNO — chowam oczy",
        "polecenia": {
            "III": "Za jasno. Stawiamy parawan. Robimy to razem.",
            "II":  "Popatrz na kartę. Za jasno? Postaw parawan i wracaj do układanki.",
            "I":   "Zanim zaczniesz, ustaw sobie miejsce dla oczu.",
        },
    },
    "instrukcja_slowna": {
        "III": "Widzę, że mrużysz oczy. Za jasno. Stawiam parawan i siadam obok — robimy to razem.",
        "II":  "Podaję ci kartę „ZA JASNO”. Wybierz: parawan czy daszek? Ja jestem obok.",
        "I":   "Karta leży w kąciku. Przygotuj sobie miejsce, zanim zaczniesz.",
    },
    "konspekt": {
        "temat": "Spokojne oczy — buduję sobie miejsce do patrzenia",
        "wprowadzenie": "zabawa „Latarka i cień” — dziecko obserwuje, jak zmienia się obraz, gdy zasłonimy źródło światła",
        "glowna": "budowanie własnego stanowiska: parawan, jedna pomoc na blacie, wybór miejsca w sali; potem krótkie zadanie wzrokowe (układanka 6–12 elementów) przy tym stanowisku",
        "zakonczenie": "„Pokaż, gdzie twoim oczom było dobrze” — dziecko wskazuje wybrane miejsce i dostaje kartę do kącika",
        "metody": ["zabawa badawcza", "pokaz z objaśnieniem", "ćwiczenia praktyczne"],
        "formy": "indywidualna, w parze z nauczycielem",
        "ewaluacja_uwaga": "liczy się, czy dziecko samo sięgnęło po osłonę — nie to, czy dokończyło układankę",
    },
    "arkusz": {
        "tytul": "ZA JASNO — karty i szablon parawanu",
        "elementy": [
            "karta „ZA JASNO” (9 × 9 cm) — 2 sztuki: do kącika i do planu dnia",
            "karta „MOJE MIEJSCE” z rysunkiem stolika z parawanem",
            "szablon parawanu 3 × (25 × 30 cm) z linią zagięcia",
        ],
        "symbole": ["k_za_jasno.jpg", "k_moje_miejsce.jpg", "k_postawa_stolik.jpg"],
    },
    "ryzyko": "przy skargach na ból oczu, częstym mrużeniu jednego oka lub przybliżaniu twarzy do kartki — skierowanie do okulisty przed pracą sensoryczną",
},
{
    "id": "SENS-02", "kod": "WZR-POD", "zmysl": "wzrok", "sektor": "podwrazliwosc",
    "nazwa": "Zaplanowany bodziec wzrokowy zamiast wpatrywania się",
    "objawy": [
        "Wpatruje się w źródła światła, wirujące lub błyszczące przedmioty",
        "Przysuwa przedmioty blisko oczu, ogląda je pod kątem",
        "Gubi miejsce na obrazku, pomija szczegóły, „nie widzi” rzeczy przed sobą",
    ],
    "opis_dla_doroslego": (
        "Dziecko dobiera sobie bodziec wzrokowy samo, bo zwykły obraz jest dla niego za słaby — "
        "stąd wpatrywanie się w światło i oglądanie przedmiotów pod kątem. Skutkiem ubocznym jest "
        "gubienie się na obrazku i pomijanie szczegółów w zadaniu."
    ),
    "strategia_sensoryczna": (
        "Dziecko korzysta z zaplanowanego, mocnego bodźca wzrokowego (butelka sensoryczna, tuba z brokatem, "
        "lampka światłowodowa) w wyznaczonym momencie dnia, a w zadaniu prowadzi wzrok palcem lub okienkiem "
        "czytelniczym — zamiast szukać bodźca w suficie i lampach."
    ),
    "sygnal_dziecka": "karta „POTRZEBUJĘ ŚWIATEŁEK” wymieniana na 2 minuty przy butelce sensorycznej",
    "kontekst": "podczas zadań przy stoliku i w czasie zabawy swobodnej w sali",
    "czynnosc": {
        "3-4": "weźmie butelkę sensoryczną z półki, popatrzy na nią przez chwilę i odłoży ją, wracając do zabawy",
        "5":   "wymieni kartę na 2 minuty przy butelce sensorycznej, a w zadaniu poprowadzi wzrok palcem po obrazku",
        "6":   "samo zaplanuje moment przerwy wzrokowej przed dłuższym zadaniem i użyje okienka czytelniczego, żeby nie gubić miejsca",
    },
    "wskaznik_obserwacji": "liczba zadań, w których dziecko użyło prowadzenia wzroku (palec, okienko) i nie zgubiło miejsca",
    "dieta_sensoryczna": [
        "butelka sensoryczna lub tuba z brokatem dostępna na półce — 2 minuty na sygnał",
        "zabawy „szukaj i pokaż” z kontrastowym obrazkiem (czarno-biały, duże pola)",
        "latarka w ciemnym namiocie — kontrolowany, mocny bodziec zamiast wpatrywania się w lampę",
    ],
    "dostosowania": [
        "okienko czytelnicze lub kartka zasłaniająca resztę obrazka",
        "obrazki z wyraźnym konturem i jednym elementem na polu",
        "przypomnienie palcem: „prowadź od lewej”",
    ],
    "pomoc": {
        "nazwa": "Butelka sensoryczna + okienko czytelnicze",
        "opis_dla_doroslego": (
            "Przezroczysta butelka z gliceryną i brokatem (bodziec na sygnał) oraz kartonowe okienko "
            "6 × 3 cm do prowadzenia wzroku po obrazku. Dwie pomoce, jedna zasada: mocny bodziec ma "
            "swoje miejsce i swój czas, a zadanie ma swoje okienko."
        ),
        "trzy_kroki_uzycia": [
            "Postaw butelkę na stałej półce — zawsze tej samej — i pokaż dziecku, gdzie stoi.",
            "W zadaniu połóż okienko na pierwszym elemencie i przesuwaj je razem z dzieckiem od lewej do prawej.",
            "Po zadaniu odnotuj, czy dziecko sięgnęło po butelkę na sygnał, czy wpatrywało się w lampę.",
        ],
        "wskazowka_dla_doroslego": (
            "Bodźca nie odbieramy — przenosimy go. Zabranie butelki „za karę” cofa cały plan: dziecko "
            "wróci do wpatrywania się w światło, bo potrzeba została ta sama."
        ),
        "etykieta_dla_dziecka": "ŚWIATEŁKA — patrzę tutaj",
        "polecenia": {
            "III": "Światełka są tutaj. Patrzymy razem. Liczę do dwudziestu.",
            "II":  "Chcesz światełka? Podaj kartę i idź do półki.",
            "I":   "Weź okienko. Prowadź od lewej strony.",
        },
    },
    "instrukcja_slowna": {
        "III": "Widzę, że szukasz światła. Idziemy razem po butelkę, patrzymy chwilę i wracamy do stolika.",
        "II":  "Masz kartę „ŚWIATEŁKA”. Dwie minuty przy półce, potem wracasz do zadania.",
        "I":   "Zaplanuj sobie przerwę na światełka — powiedz, kiedy ją zrobisz.",
    },
    "konspekt": {
        "temat": "Światełka mają swoje miejsce — wzrok, który prowadzi",
        "wprowadzenie": "zabawa z butelką sensoryczną: „co opada najwolniej?” — wspólne patrzenie i nazywanie",
        "glowna": "ćwiczenie prowadzenia wzroku: okienko czytelnicze na ścieżce obrazkowej (8 pól), potem wyszukiwanie 3 ukrytych elementów na obrazku kontrastowym",
        "zakonczenie": "ustalenie z dzieckiem, gdzie w sali stoi butelka i kiedy można po nią sięgnąć",
        "metody": ["ćwiczenia praktyczne", "zabawa dydaktyczna", "instruktaż"],
        "formy": "indywidualna lub w parze",
        "ewaluacja_uwaga": "cel dotyczy sięgnięcia po zaplanowany bodziec, a nie liczby znalezionych elementów",
    },
    "arkusz": {
        "tytul": "ŚWIATEŁKA — karta wymiany i okienko czytelnicze",
        "elementy": [
            "karta „ŚWIATEŁKA” (9 × 9 cm) — do wymiany na 2 minuty przy półce",
            "okienko czytelnicze 6 × 3 cm — szablon do wycięcia, 2 sztuki",
            "ścieżka obrazkowa 8 pól do prowadzenia wzroku",
        ],
        "symbole": ["k_swiatelka.jpg", "k_okienko.jpg", "k_patrz_tu.jpg"],
    },
    "ryzyko": "przysuwanie przedmiotów do oczu i pomijanie części obrazka wymaga wykluczenia wady wzroku — kontrola okulistyczna przed interwencją sensoryczną",
},
{
    "id": "SENS-03", "kod": "WZR-SZUM", "zmysl": "wzrok", "sektor": "bialy_szum",
    "nazwa": "Codzienne sprawdzanie, jak dziś pracują oczy",
    "objawy": [
        "Reakcje na światło i bodźce wzrokowe są zmienne — raz przesadne, raz brak reakcji",
        "Raz dostrzega drobne szczegóły, innym razem nie zauważa rzeczy oczywistych",
    ],
    "opis_dla_doroslego": (
        "Reaktywność wzrokowa dziecka zmienia się z dnia na dzień. Największym błędem jest przyjęcie "
        "stałego profilu („jest nadwrażliwy”) i planowanie pod niego zajęć — w dniu obniżonej "
        "reaktywności to samo dostosowanie działa przeciwko dziecku."
    ),
    "strategia_sensoryczna": (
        "Dziecko codziennie rano ustawia własny „termometr oczu” (3 pola: dużo światła / średnio / mało) "
        "i na tej podstawie razem z nauczycielem wybiera miejsce i pomoc na dany dzień."
    ),
    "sygnal_dziecka": "przestawienie klamerki na termometrze oczu przy porannym powitaniu",
    "kontekst": "podczas porannego powitania i przed pierwszym zadaniem przy stoliku",
    "czynnosc": {
        "3-4": "z pomocą dorosłego przypnie klamerkę na jednym z trzech pól termometru oczu",
        "5":   "ustawi termometr oczu i wskaże miejsce w sali, w którym dziś chce pracować",
        "6":   "ustawi termometr, wybierze pomoc na dany dzień i powie, po czym poznało, że dziś jest inaczej",
    },
    "wskaznik_obserwacji": "liczba dni, w których dziecko ustawiło termometr przed pierwszym zadaniem",
    "dieta_sensoryczna": [
        "poranne 30 sekund na ustawienie termometru — stały punkt planu dnia",
        "dwa gotowe miejsca w sali: jasne i przyciemnione — wybór należy do dziecka",
        "krótkie sprawdzenie po obiedzie, czy poziom się zmienił",
    ],
    "dostosowania": [
        "plan dnia z polem na termometr oczu",
        "brak automatycznych dostosowań „na stałe” — decyzja zapada codziennie",
        "notatka w dzienniku obserwacji: poziom i to, co po nim ustalono",
    ],
    "pomoc": {
        "nazwa": "Termometr oczu (3 pola z klamerką)",
        "opis_dla_doroslego": (
            "Kartonowy pasek 10 × 30 cm z trzema polami — zielonym, żółtym i czerwonym — "
            "opisanymi obrazkiem, nie słowem. Klamerka pokazuje dzisiejszy poziom. "
            "Termometr wisi na wysokości oczu dziecka."
        ),
        "trzy_kroki_uzycia": [
            "Rano, przy powitaniu, poproś dziecko o przypięcie klamerki — bez pytania „dlaczego”.",
            "Odczytaj poziom na głos i powiedz, co z niego wynika: gdzie siadamy, jaka pomoc leży na stole.",
            "Wieczorem przenieś odczyt do dziennika obserwacji — to on pokaże wzór zmienności.",
        ],
        "wskazowka_dla_doroslego": (
            "Nie poprawiaj wyboru dziecka, nawet gdy „widać, że dziś jest inaczej”. Termometr uczy "
            "rozpoznawania własnego stanu, a nie zgadywania odpowiedzi, której oczekuje dorosły."
        ),
        "etykieta_dla_dziecka": "MOJE OCZY DZISIAJ",
        "polecenia": {
            "III": "Jak dziś mają się twoje oczy? Przypinamy klamerkę razem.",
            "II":  "Przypnij klamerkę. Zielone, żółte czy czerwone?",
            "I":   "Ustaw termometr i powiedz, gdzie dziś siadasz.",
        },
    },
    "instrukcja_slowna": {
        "III": "Dzień dobry. Sprawdzamy oczy. Trzymam pasek, ty przypinasz klamerkę.",
        "II":  "Ustaw dziś swój termometr oczu, a potem wybierz miejsce przy stole.",
        "I":   "Termometr wisi na miejscu. Ustaw go i powiedz mi, co z niego wynika.",
    },
    "konspekt": {
        "temat": "Moje oczy dzisiaj — poziom, który zmienia się z dnia na dzień",
        "wprowadzenie": "rozmowa z obrazkami: „raz jest za jasno, raz w sam raz” — dziecko dopasowuje buźki do sytuacji",
        "glowna": "wykonanie własnego termometru oczu (klejenie trzech pól, przypięcie klamerki) i próbne ustawienie na dziś; potem to samo zadanie wzrokowe w dwóch miejscach sali i porównanie, gdzie było łatwiej",
        "zakonczenie": "powieszenie termometru na stałym miejscu i ustalenie pory sprawdzania",
        "metody": ["rozmowa kierowana", "praca plastyczno-techniczna", "ćwiczenia porównawcze"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "sukcesem jest ustawienie termometru, a nie zgodność odczytu z opinią dorosłego",
    },
    "arkusz": {
        "tytul": "TERMOMETR OCZU — szablon do wycięcia",
        "elementy": [
            "pasek termometru 10 × 30 cm z trzema polami (zielone / żółte / czerwone) i obrazkami",
            "3 karty sytuacji do dopasowania (jasna sala, przyciemniony kącik, stolik z parawanem)",
            "instrukcja dla nauczyciela na odwrocie — kiedy sprawdzamy poziom",
        ],
        "symbole": ["k_termometr_oczu.jpg", "k_za_jasno.jpg", "k_moje_miejsce.jpg"],
    },
    "ryzyko": "zmienność reakcji utrzymująca się mimo diety sensorycznej wymaga konsultacji neurologicznej i okulistycznej — może maskować napady nieświadomości",
},

# ===== II · SŁUCH (b230) ===================================================
{
    "id": "SENS-04", "kod": "SLU-NAD", "zmysl": "sluch", "sektor": "nadwrazliwosc",
    "nazwa": "Ochrona słuchu przed hałasem sali i szatni",
    "objawy": [
        "Zatyka uszy, płacze lub ucieka przy hałasie (dzwonek, suszarka, gwar sali)",
        "Rozprasza się przy dźwiękach, których inni nie zauważają (brzęczenie, tykanie)",
        "Reaguje lękiem lub złością na nagłe, głośne dźwięki",
    ],
    "opis_dla_doroslego": (
        "Gwar sali i szatni dezorganizuje dziecku zabawę, zanim ono samo zdąży to nazwać. "
        "Ucieczka i płacz są końcem procesu, nie jego początkiem — praca dotyczy tego, "
        "co dziecko robi na pierwszym sygnale narastania hałasu."
    ),
    "strategia_sensoryczna": (
        "Dziecko zakłada słuchawki wygłuszające albo przechodzi do kącika wyciszenia ZANIM hałas "
        "je przeciąży — na podstawie zapowiedzi dorosłego („za chwilę szatnia”) lub własnego rozpoznania."
    ),
    "sygnal_dziecka": "karta „ZA GŁOŚNO” albo samodzielne sięgnięcie po słuchawki z wieszaka",
    "kontekst": "w hałaśliwych porach dnia — szatnia, stołówka, zabawa swobodna w pełnej sali",
    "czynnosc": {
        "3-4": "założy słuchawki wygłuszające podane przez dorosłego i zostanie w szatni do końca ubierania",
        "5":   "poda kartę „ZA GŁOŚNO”, samo zdejmie słuchawki z wieszaka i wróci do grupy w nich",
        "6":   "po zapowiedzi hałaśliwej sytuacji samo zdecyduje, czy zakłada słuchawki, czy idzie do kącika wyciszenia, i wróci do zabawy po ustaniu hałasu",
    },
    "wskaznik_obserwacji": "liczba hałaśliwych sytuacji, w których dziecko użyło ochrony słuchu zamiast uciec lub zapłakać",
    "dieta_sensoryczna": [
        "słuchawki wygłuszające na stałym wieszaku, w zasięgu dziecka — bez proszenia dorosłego",
        "kącik wyciszenia z miękką ścianą i jedną książeczką, dostępny bez pytania",
        "uprzedzanie o głośnych sytuacjach 2 minuty wcześniej, tym samym zdaniem",
    ],
    "dostosowania": [
        "miejsce z dala od dzwonka, suszarki i drzwi do szatni",
        "wyjście do szatni przed resztą grupy lub po niej",
        "sygnał wizualny zamiast dzwonka na zmianę aktywności",
    ],
    "pomoc": {
        "nazwa": "Słuchawki wygłuszające na wieszaku + karta ZA GŁOŚNO",
        "opis_dla_doroslego": (
            "Nauszniki pasywne (bez elektroniki) na wieszaku na wysokości dziecka, obok karta-symbol "
            "„ZA GŁOŚNO”. Zestaw działa tylko wtedy, gdy dziecko sięga po niego samo — wydawanie "
            "słuchawek „na prośbę dorosłego” nie buduje strategii."
        ),
        "trzy_kroki_uzycia": [
            "Powieś słuchawki na stałym, dostępnym wieszaku i pokaż dziecku, gdzie wiszą.",
            "Na dwie minuty przed hałaśliwą porą uprzedź tym samym zdaniem i wskaż wieszak.",
            "Odnotuj, czy dziecko sięgnęło samo, czy dopiero po podaniu przez dorosłego.",
        ],
        "wskazowka_dla_doroslego": (
            "Słuchawki nie izolują dziecka od grupy — pozwalają w niej zostać. Zdejmowanie ich "
            "„bo już nie jest tak głośno” odbiera dziecku kontrolę i cofa efekt."
        ),
        "etykieta_dla_dziecka": "ZA GŁOŚNO — zakładam słuchawki",
        "polecenia": {
            "III": "Za głośno. Zakładamy słuchawki. Jestem obok.",
            "II":  "Za chwilę szatnia. Weź słuchawki z wieszaka.",
            "I":   "Zaraz będzie głośno. Zdecyduj, co robisz.",
        },
    },
    "instrukcja_slowna": {
        "III": "Słyszę, że robi się głośno. Podaję ci słuchawki i zakładamy je razem — zostajemy tutaj.",
        "II":  "Za dwie minuty idziemy do szatni. Masz kartę i wieszak — weź słuchawki.",
        "I":   "Za dwie minuty szatnia. Wybierz: słuchawki czy kącik wyciszenia?",
    },
    "konspekt": {
        "temat": "Za głośno — co robię, zanim hałas mnie zmęczy",
        "wprowadzenie": "zabawa „cicho–głośno”: dziecko pokazuje ręką poziom dźwięku wydawanego przez nauczyciela",
        "glowna": "próba ze słuchawkami w kontrolowanym hałasie (nagranie gwaru sali z tabletu, głośność narastająca): dziecko ćwiczy sięgnięcie po słuchawki na pierwszy sygnał, a nie na szczycie hałasu; potem to samo w prawdziwej szatni",
        "zakonczenie": "ustalenie miejsca wieszaka i zdania zapowiadającego hałas („za dwie minuty szatnia”)",
        "metody": ["ćwiczenia praktyczne", "symulacja sytuacji", "instruktaż"],
        "formy": "indywidualna, następnie w małej grupie",
        "ewaluacja_uwaga": "liczy się moment sięgnięcia po słuchawki — im wcześniej, tym wyższa wartość próby",
    },
    "arkusz": {
        "tytul": "ZA GŁOŚNO — karty i tabliczka wieszaka",
        "elementy": [
            "karta „ZA GŁOŚNO” (9 × 9 cm) — 2 sztuki",
            "karta „KĄCIK WYCISZENIA” z rysunkiem miejsca",
            "tabliczka na wieszak ze słuchawkami (10 × 6 cm)",
        ],
        "symbole": ["k_za_glosno.jpg", "k_sluchawki.jpg", "k_kacik_wyciszenia.jpg"],
    },
    "ryzyko": "nadwrażliwość słuchowa z zatykaniem uszu wymaga wykluczenia stanu zapalnego ucha i badania słuchu przed wdrożeniem diety sensorycznej",
},
{
    "id": "SENS-05", "kod": "SLU-POD", "zmysl": "sluch", "sektor": "podwrazliwosc",
    "nazwa": "Reakcja na imię i zaplanowany bodziec dźwiękowy",
    "objawy": [
        "Nie reaguje na wołanie po imieniu, choć słuch ma prawidłowy",
        "Samo wytwarza głośne dźwięki (pomrukuje, stuka, trzaska)",
        "Potrzebuje głośnych bodźców — przybliża ucho do źródła dźwięku, pogłaśnia",
    ],
    "opis_dla_doroslego": (
        "Dziecko dobiera sobie bodziec słuchowy samo — stukaniem, pomrukiwaniem, trzaskaniem — bo "
        "zwykły poziom dźwięku do niego nie dociera. Wołanie po imieniu ginie w tle. To nie jest "
        "ignorowanie dorosłego."
    ),
    "strategia_sensoryczna": (
        "Dziecko korzysta z instrumentu lub „kącika dźwięków” w zaplanowanym momencie dnia, a na "
        "wołanie odpowiada po sygnale dotykowo-wzrokowym (dotknięcie ramienia i pokazanie karty), "
        "który zastępuje sam głos."
    ),
    "sygnal_dziecka": "podanie karty „CHCĘ DŹWIĘKI” w zamian za 2 minuty z instrumentem",
    "kontekst": "podczas zabawy swobodnej i przy zbiórkach grupy w sali",
    "czynnosc": {
        "3-4": "po dotknięciu ramienia i pokazaniu karty popatrzy na dorosłego i podejdzie do niego",
        "5":   "odpowie na wołanie po imieniu wspartym kartą, a bodziec dźwiękowy weźmie z kącika dźwięków",
        "6":   "odpowie na samo wołanie po imieniu i samo zaplanuje moment dwuminutowej przerwy z instrumentem",
    },
    "wskaznik_obserwacji": "liczba wołań, na które dziecko zareagowało do trzeciego powtórzenia",
    "dieta_sensoryczna": [
        "„kącik dźwięków”: bębenek, marakas, rura grzmotowa — 2 minuty na sygnał",
        "zabawy rytmiczne z mocnym akcentem przed zadaniem wymagającym słuchania",
        "śpiewane polecenia zamiast mówionych w porach niskiej uwagi",
    ],
    "dostosowania": [
        "wołanie po imieniu zawsze z podejściem na odległość wyciągniętej ręki i kontaktem wzrokowym",
        "polecenie do dziecka po jego imieniu, nie do całej grupy",
        "sprawdzenie zrozumienia gestem, nie pytaniem „rozumiesz?”",
    ],
    "pomoc": {
        "nazwa": "Kącik dźwięków z kartą wymiany",
        "opis_dla_doroslego": (
            "Trzy instrumenty w koszyku na stałej półce (bębenek, marakas, rura grzmotowa) i karta "
            "„CHCĘ DŹWIĘKI”. Dziecko wymienia kartę na dwie minuty grania — bodziec zostaje "
            "zaspokojony w miejscu i czasie, które nie rozbijają zabawy grupy."
        ),
        "trzy_kroki_uzycia": [
            "Ustaw koszyk z instrumentami na stałej półce i pokaż dziecku kartę wymiany.",
            "Przyjmij kartę, odlicz dwie minuty (klepsydra) i zamknij przerwę tym samym zdaniem.",
            "Odnotuj, ile razy dziecko sięgnęło po kartę zamiast stukać w blat lub pomrukiwać.",
        ],
        "wskazowka_dla_doroslego": (
            "Uciszanie („nie stukaj”) usuwa objaw i nie daje nic w zamian. Dopóki dziecko nie ma "
            "dokąd pójść po dźwięk, będzie go dobierać w czasie zajęć."
        ),
        "etykieta_dla_dziecka": "CHCĘ DŹWIĘKI — idę do koszyka",
        "polecenia": {
            "III": "Popatrz na mnie. Jestem tu. Idziemy po bębenek razem.",
            "II":  "Podaj kartę. Dwie minuty z instrumentem, potem wracamy.",
            "I":   "Powiedz, kiedy zrobisz sobie przerwę na dźwięki.",
        },
    },
    "instrukcja_slowna": {
        "III": "Dotykam twojego ramienia i pokazuję kartę. Popatrz na mnie — teraz idziemy razem.",
        "II":  "Wołam cię po imieniu i pokazuję kartę. Podejdź do mnie.",
        "I":   "Wołam cię po imieniu. Czekam przy stoliku.",
    },
    "konspekt": {
        "temat": "Słyszę swoje imię — dźwięki, które mam zaplanowane",
        "wprowadzenie": "zabawa „bęben mówi twoje imię” — rytm imienia wystukany na bębenku, dziecko odpowiada gestem",
        "glowna": "ćwiczenie reakcji na imię w trzech odległościach (1 m, 3 m, drugi koniec sali), z sygnałem dotykowo-wzrokowym wycofywanym stopniowo; potem wymiana karty na przerwę dźwiękową",
        "zakonczenie": "wspólne ustalenie, gdzie stoi koszyk z instrumentami i ile trwa przerwa",
        "metody": ["zabawa rytmiczna", "ćwiczenia praktyczne", "stopniowanie trudności"],
        "formy": "indywidualna, potem w parze z dzieckiem z grupy",
        "ewaluacja_uwaga": "notujemy odległość, z jakiej dziecko zareagowało — to ona pokazuje postęp",
    },
    "arkusz": {
        "tytul": "CHCĘ DŹWIĘKI — karty wymiany i tabliczka koszyka",
        "elementy": [
            "karta „CHCĘ DŹWIĘKI” (9 × 9 cm) — 2 sztuki",
            "karta z imieniem dziecka i symbolem „POPATRZ NA MNIE”",
            "tabliczka na koszyk z instrumentami (10 × 6 cm)",
        ],
        "symbole": ["k_chce_dzwieki.jpg", "k_popatrz_na_mnie.jpg", "k_instrumenty.jpg"],
    },
    "ryzyko": "brak reakcji na imię zawsze wymaga aktualnego badania słuchu (audiometria) — dopiero jego prawidłowy wynik pozwala mówić o podwrażliwości",
},
{
    "id": "SENS-06", "kod": "SLU-SZUM", "zmysl": "sluch", "sektor": "bialy_szum",
    "nazwa": "Sprawdzanie poziomu słuchowego przed zajęciami",
    "objawy": [
        "Reakcje na dźwięki są niestałe — ten sam hałas raz przeszkadza, raz pozostaje niezauważony",
        "Raz reaguje na szept, innym razem nie słyszy głośnego wołania",
    ],
    "opis_dla_doroslego": (
        "Dziecko nie potrafi przewidzieć własnej reakcji na dźwięk, a dorosły czyta tę zmienność "
        "jako niekonsekwencję lub upór. Plan dnia musi zakładać sprawdzenie poziomu, a nie stały profil."
    ),
    "strategia_sensoryczna": (
        "Dziecko przed zajęciami ustawia „radio uszu” (3 pola: cicho / średnio / głośno) i wybiera "
        "z niego dzisiejsze dostosowanie: słuchawki, miejsce z brzegu albo brak dodatkowego wsparcia."
    ),
    "sygnal_dziecka": "przestawienie strzałki na tarczy „radio uszu”",
    "kontekst": "przed zajęciami dydaktycznymi i przed wyjściem do szatni",
    "czynnosc": {
        "3-4": "z pomocą dorosłego przestawi strzałkę na tarczy i weźmie wskazane wsparcie",
        "5":   "samo ustawi tarczę i wybierze jedno z trzech dostosowań na dany dzień",
        "6":   "ustawi tarczę, wybierze dostosowanie i powie, po czym poznało, że dziś słyszy inaczej",
    },
    "wskaznik_obserwacji": "liczba dni, w których dziecko ustawiło tarczę przed pierwszymi zajęciami",
    "dieta_sensoryczna": [
        "sprawdzenie poziomu dwa razy dziennie: rano i po odpoczynku",
        "trzy gotowe dostosowania do wyboru, zawsze te same",
        "wpis poziomu do dziennika — po dwóch tygodniach widać wzór dni trudnych",
    ],
    "dostosowania": [
        "brak stałego przypisania dziecku „nadwrażliwości słuchowej” w dokumentacji",
        "polecenia zawsze sprawdzane gestem, niezależnie od poziomu",
        "informacja o poziomie przekazywana wszystkim dorosłym pracującym tego dnia z grupą",
    ],
    "pomoc": {
        "nazwa": "Radio uszu — tarcza z trzema poziomami",
        "opis_dla_doroslego": (
            "Kartonowa tarcza o średnicy 20 cm z ruchomą strzałką i trzema polami opisanymi obrazkiem: "
            "ucho przekreślone (cicho), ucho zwykłe (średnio), ucho z falami (głośno). Przy każdym polu "
            "narysowane dostosowanie, które z niego wynika."
        ),
        "trzy_kroki_uzycia": [
            "Powieś tarczę przy planie dnia, na wysokości oczu dziecka.",
            "Poproś o ustawienie strzałki przed pierwszymi zajęciami i odczytaj wybór na głos.",
            "Przekaż odczyt drugiemu nauczycielowi i zapisz go w dzienniku obserwacji.",
        ],
        "wskazowka_dla_doroslego": (
            "Zmienność nie jest kaprysem. Jeżeli dziecko dziś nie reaguje na wołanie, a wczoraj "
            "reagowało — to jest dana do zapisania, a nie powód do upomnienia."
        ),
        "etykieta_dla_dziecka": "MOJE USZY DZISIAJ",
        "polecenia": {
            "III": "Sprawdzamy uszy. Ustawiam strzałkę z tobą.",
            "II":  "Ustaw strzałkę. Co dziś wybierasz?",
            "I":   "Ustaw radio uszu i powiedz, co z niego wynika.",
        },
    },
    "instrukcja_slowna": {
        "III": "Sprawdzamy, jak dziś słyszysz. Trzymam tarczę, ty przesuwasz strzałkę.",
        "II":  "Ustaw dziś swoje radio uszu i weź to, co przy nim narysowane.",
        "I":   "Ustaw tarczę przed zajęciami i powiedz mi, czego dziś potrzebujesz.",
    },
    "konspekt": {
        "temat": "Moje uszy dzisiaj — poziom, który sprawdzam codziennie",
        "wprowadzenie": "zabawa „ten sam dźwięk, dwa dni”: nagranie gwaru raz cicho, raz głośno — dziecko dopasowuje buźkę",
        "glowna": "wykonanie tarczy „radio uszu” i próbne ustawienie; sprawdzenie na żywo, czy wybrane dostosowanie pomaga w krótkiej zabawie w hałaśliwym kąciku",
        "zakonczenie": "powieszenie tarczy przy planie dnia i ustalenie dwóch pór sprawdzania",
        "metody": ["rozmowa kierowana", "praca techniczna", "próba w warunkach naturalnych"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "sukces = ustawienie tarczy; trafność odczytu ocenia się dopiero po dwóch tygodniach wpisów",
    },
    "arkusz": {
        "tytul": "RADIO USZU — tarcza i strzałka do wycięcia",
        "elementy": [
            "tarcza o średnicy 20 cm z trzema polami i rysunkami dostosowań",
            "strzałka do wycięcia z otworem na zapinkę",
            "3 karty dostosowań (słuchawki / miejsce z brzegu / bez wsparcia)",
        ],
        "symbole": ["k_radio_uszu.jpg", "k_sluchawki.jpg", "k_miejsce_z_brzegu.jpg"],
    },
    "ryzyko": "naprzemienne reagowanie na szept i brak reakcji na głośne wołanie może wskazywać na wysiękowe zapalenie ucha — wymaga kontroli laryngologicznej",
},

# ===== III · DOTYK (b265) ==================================================
{
    "id": "SENS-07", "kod": "DOT-NAD", "zmysl": "dotyk", "sektor": "nadwrazliwosc",
    "nazwa": "Bezpieczna odległość i uprzedzanie o dotyku",
    "objawy": [
        "Unika dotyku, przytulania, mycia twarzy/głowy, obcinania paznokci i włosów",
        "Przeszkadzają mu metki, szwy, niektóre faktury ubrań i materiałów plastycznych",
        "Reaguje obronnie na przypadkowy dotyk (kolejka, ciasnota, zabawy grupowe)",
    ],
    "opis_dla_doroslego": (
        "Przypadkowy dotyk w kolejce czy w kręgu dziecko odbiera jak zagrożenie — odpowiada "
        "odepchnięciem, krzykiem albo ucieczką. Reakcja obronna jest odruchem, nie decyzją; "
        "karanie za nią pogłębia napięcie."
    ),
    "strategia_sensoryczna": (
        "Dziecko zajmuje ustalone miejsce chroniące plecy i boki (koniec kolejki, brzeg dywanu, "
        "krzesło przy ścianie) i korzysta z zapowiedzi dotyku — dorosły mówi, zanim dotknie, "
        "a dziecko odpowiada „tak” albo „nie teraz”."
    ),
    "sygnal_dziecka": "karta „NIE TERAZ” lub gest otwartej dłoni oznaczający „daj mi miejsce”",
    "kontekst": "w kolejce do szatni i łazienki, w kręgu na dywanie i w zabawach grupowych",
    "czynnosc": {
        "3-4": "stanie na końcu kolejki na wyznaczonym znaku i przejdzie z grupą bez odpychania innych",
        "5":   "wybierze miejsce chroniące plecy (brzeg dywanu, przy ścianie) i użyje karty „NIE TERAZ”, gdy zbliży się dotyk",
        "6":   "zaplanuje z wyprzedzeniem swoje miejsce w kolejce i w kręgu, a o dotyku uprzedzi rówieśnika słowem",
    },
    "wskaznik_obserwacji": "liczba sytuacji z bliskością, w których dziecko użyło miejsca lub karty zamiast reakcji obronnej",
    "dieta_sensoryczna": [
        "mocny docisk przed sytuacją bliskości (przytulenie w kocyk, przeciskanie przez tunel) — proprioceptywne wyciszenie dotyku",
        "zabawy fakturami w tempie dziecka: najpierw suche i twarde, dopiero potem mokre i lepkie",
        "stały znak na podłodze wyznaczający „moje miejsce” w kolejce",
    ],
    "dostosowania": [
        "pierwsze lub ostatnie miejsce w kolejce — nigdy w środku",
        "akceptacja własnych ubrań dziecka, odcinanie metek, brak wymuszania fartuszka",
        "uprzedzanie o każdym dotyku dorosłego, także przy pomaganiu w ubieraniu",
    ],
    "pomoc": {
        "nazwa": "Znak „MOJE MIEJSCE” + karta NIE TERAZ",
        "opis_dla_doroslego": (
            "Naklejka-stopy na podłodze (koniec kolejki, brzeg dywanu) oraz karta „NIE TERAZ” "
            "z symbolem otwartej dłoni. Znak daje przewidywalność, karta — sposób odmowy inny "
            "niż odepchnięcie."
        ),
        "trzy_kroki_uzycia": [
            "Naklej znak w dwóch miejscach: przy drzwiach do szatni i na brzegu dywanu.",
            "Ucz karty „NIE TERAZ” na spokojnie, w zabawie — nie w momencie konfliktu.",
            "Po każdej sytuacji z bliskością odnotuj, czy dziecko użyło znaku, karty, czy odepchnęło.",
        ],
        "wskazowka_dla_doroslego": (
            "Uprzedzaj o dotyku zawsze — także wtedy, gdy pomagasz. Dotyk „z zaskoczenia”, nawet "
            "życzliwy, uruchamia obronę i psuje efekt tygodni pracy."
        ),
        "etykieta_dla_dziecka": "NIE TERAZ — potrzebuję miejsca",
        "polecenia": {
            "III": "Stajemy na stópkach. Ja jestem obok ciebie.",
            "II":  "Twoje miejsce jest na stópkach. Masz kartę „NIE TERAZ”.",
            "I":   "Wybierz miejsce, zanim ustawimy się w kolejce.",
        },
    },
    "instrukcja_slowna": {
        "III": "Idziemy do szatni. Stajemy na stópkach, ja stoję obok ciebie i nikt cię nie dotknie.",
        "II":  "Pamiętasz swoje miejsce? Stópki przy drzwiach. Karta „NIE TERAZ” jest w kieszeni.",
        "I":   "Za chwilę kolejka. Powiedz, gdzie dziś stajesz.",
    },
    "konspekt": {
        "temat": "Moje miejsce, mój dotyk — mówię, zanim ktoś mnie dotknie",
        "wprowadzenie": "zabawa „bańka”: dziecko rysuje kredą własną bańkę na podłodze i sprawdza, jak daleko sięga ręką",
        "glowna": "ćwiczenie kolejki w małej grupie (3 dzieci) ze znakami na podłodze; nauka i próba karty „NIE TERAZ”; na koniec krótka zabawa fakturami wybranymi przez dziecko",
        "zakonczenie": "naklejenie znaku w prawdziwym miejscu w sali i pokazanie go całej grupie",
        "metody": ["zabawa ruchowa", "symulacja sytuacji", "ćwiczenia praktyczne"],
        "formy": "indywidualna, następnie w małej grupie",
        "ewaluacja_uwaga": "notujemy sposób reakcji na bliskość, nie czas wytrwania w kolejce",
    },
    "arkusz": {
        "tytul": "MOJE MIEJSCE — znaki na podłogę i karta NIE TERAZ",
        "elementy": [
            "para stópek do wycięcia (2 komplety) — na podłogę przy szatni i na dywan",
            "karta „NIE TERAZ” (9 × 9 cm) — 2 sztuki, jedna do kieszeni",
            "karta „UPRZEDZAM O DOTYKU” dla dorosłego, do planu dnia",
        ],
        "symbole": ["k_moje_miejsce.jpg", "k_nie_teraz.jpg", "k_kolejka.jpg"],
    },
    "ryzyko": "gwałtowna obrona przed myciem głowy i obcinaniem paznokci bywa objawem obronności dotykowej wymagającej terapii SI — sama dieta sensoryczna nie wystarczy",
},
{
    "id": "SENS-08", "kod": "DOT-POD", "zmysl": "dotyk", "sektor": "podwrazliwosc",
    "nazwa": "Zaplanowane wrażenia dotykowe zamiast dotykania wszystkiego",
    "objawy": [
        "Dotyka wszystkiego i wszystkich, mocno ściska, potrąca inne dzieci",
        "Nie zauważa brudu na twarzy/rękach, słabo czuje ból i temperaturę",
        "Poszukuje intensywnych wrażeń dotykowych (grzebanie w materiałach, ugniatanie)",
    ],
    "opis_dla_doroslego": (
        "Dziecko zbiera informację o świecie przez ręce — dotyka, ściska, grzebie. Rówieśnicy "
        "odbierają to jako zaczepki, choć intencja jest inna. Praca polega na daniu tego samego "
        "wrażenia w miejscu, w którym nikomu nie przeszkadza."
    ),
    "strategia_sensoryczna": (
        "Dziecko korzysta ze skrzynki sensorycznej (ryż, kasztany, masa) i „gniotka w kieszeni” "
        "w zaplanowanych momentach dnia, a w kręgu trzyma ręce na własnej pomocy zamiast na sąsiedzie."
    ),
    "sygnal_dziecka": "sięgnięcie po gniotka do kieszeni fartuszka lub karta „RĘCE DO PRACY”",
    "kontekst": "w kręgu na dywanie, w kolejce i podczas zabawy swobodnej w sali",
    "czynnosc": {
        "3-4": "położy ręce na własnym gniotku i zostanie w kręgu przez czas piosenki, bez dotykania sąsiada",
        "5":   "przed kręgiem weźmie gniotka, a po zajęciach skorzysta ze skrzynki sensorycznej przez 3 minuty",
        "6":   "samo zaplanuje dwa momenty pracy rękami w ciągu dnia i użyje ich, zanim zacznie dotykać innych dzieci",
    },
    "wskaznik_obserwacji": "liczba sytuacji w kręgu lub kolejce bez dotykania innych dzieci, z użyciem własnej pomocy",
    "dieta_sensoryczna": [
        "skrzynka sensoryczna (ryż, kasztany, makaron) — 3 minuty przed zajęciami wymagającymi siedzenia",
        "gniotek lub kawałek masy w kieszeni fartuszka, dostępny bez pytania",
        "prace z ugniataniem: ciastolina, glina, wyciskanie gąbki — codziennie",
    ],
    "dostosowania": [
        "miejsce w kręgu z jednym sąsiadem, nie dwoma (brzeg półkola)",
        "zadania z materiałem w rękach — dziecko trzyma pomoc, a nie „nic”",
        "sprawdzanie twarzy i rąk przed wyjściem — dziecko może nie czuć brudu",
    ],
    "pomoc": {
        "nazwa": "Skrzynka sensoryczna + gniotek kieszonkowy",
        "opis_dla_doroslego": (
            "Płaska skrzynka (40 × 30 cm) z sypkim materiałem i ukrytymi w nim drobiazgami oraz "
            "gniotek trzymany w kieszeni fartuszka. Skrzynka to bodziec zaplanowany, gniotek — "
            "bodziec dostępny w każdej chwili, także w kręgu."
        ),
        "trzy_kroki_uzycia": [
            "Ustaw skrzynkę na stałym miejscu i ustal z dzieckiem porę: przed kręgiem, po obiedzie.",
            "Włóż gniotka do kieszeni fartuszka rano — nie wydawaj go „za dobre zachowanie”.",
            "Odnotuj, czy w kręgu ręce dziecka były na gniotku, czy na sąsiedzie.",
        ],
        "wskazowka_dla_doroslego": (
            "Zabranie gniotka za potrącenie kolegi jest karą za potrzebę, nie za czyn — i wraca "
            "podwójnym dotykaniem po pięciu minutach."
        ),
        "etykieta_dla_dziecka": "RĘCE DO PRACY — mam swojego gniotka",
        "polecenia": {
            "III": "Ręce na gniotka. Trzymamy razem. Siedzimy do końca piosenki.",
            "II":  "Weź gniotka do ręki. Ręce pracują tutaj.",
            "I":   "Przygotuj ręce, zanim usiądziemy w kręgu.",
        },
    },
    "instrukcja_slowna": {
        "III": "Widzę, że rękom trzeba pracy. Daję ci gniotka i kładę na nim twoje dłonie — siedzę obok.",
        "II":  "Weź gniotka z kieszeni. Twoje ręce pracują na nim, nie na koledze.",
        "I":   "Zaplanuj, kiedy dziś idziesz do skrzynki.",
    },
    "konspekt": {
        "temat": "Ręce, które mają swoją pracę",
        "wprowadzenie": "„co jest w skrzynce?” — wyszukiwanie 5 drobiazgów w ryżu bez patrzenia",
        "glowna": "ćwiczenie siedzenia w kręgu z gniotkiem przez czas jednej i dwóch piosenek; porównanie z próbą bez pomocy — dziecko samo nazywa różnicę",
        "zakonczenie": "wybór własnego gniotka i włożenie go do kieszeni fartuszka",
        "metody": ["zabawa sensoryczna", "ćwiczenia praktyczne", "rozmowa podsumowująca"],
        "formy": "indywidualna, następnie w kręgu grupowym",
        "ewaluacja_uwaga": "notujemy dotknięcia innych dzieci w czasie kręgu — spadek liczby jest miarą postępu",
    },
    "arkusz": {
        "tytul": "RĘCE DO PRACY — karty i lista wypełnień skrzynki",
        "elementy": [
            "karta „RĘCE DO PRACY” (9 × 9 cm) — 2 sztuki",
            "karta „SKRZYNKA” z rysunkiem miejsca w sali",
            "lista 8 bezpiecznych wypełnień skrzynki z uwagą o wieku i nadzorze",
        ],
        "symbole": ["k_rece_do_pracy.jpg", "k_skrzynka.jpg", "k_gniotek.jpg"],
    },
    "ryzyko": "obniżone czucie bólu i temperatury wymaga codziennej kontroli skóry (oparzenia, otarcia) i informacji dla rodziców — dziecko może nie zgłosić urazu",
},
{
    "id": "SENS-09", "kod": "DOT-SZUM", "zmysl": "dotyk", "sektor": "bialy_szum",
    "nazwa": "Sprawdzanie tolerancji ubrania i faktur w danym dniu",
    "objawy": [
        "Reakcje na dotyk są zmienne — ten sam bodziec raz drażni, raz jest poszukiwany",
        "Tolerancja ubrań, mycia i przytulania zmienia się z dnia na dzień",
    ],
    "opis_dla_doroslego": (
        "Ta sama bluza w poniedziałek jest w porządku, a we wtorek nie do zniesienia. Dorosły widzi "
        "w tym kaprys, dziecko przeżywa zmianę progu czucia. Bez codziennego sprawdzenia poranek "
        "kończy się konfliktem o ubranie."
    ),
    "strategia_sensoryczna": (
        "Dziecko rano sprawdza „mapę ubrania” (co dziś pasuje, co drapie) i wybiera z dwóch "
        "przygotowanych wariantów, a przed pracą z materiałami wskazuje na skali, ile dziś zniesie."
    ),
    "sygnal_dziecka": "wskazanie pola na skali faktur (1 – suche, 2 – wilgotne, 3 – lepkie)",
    "kontekst": "przy przebieraniu w szatni i przed zajęciami plastycznymi",
    "czynnosc": {
        "3-4": "wskaże z dwóch przygotowanych bluz tę, którą dziś zakłada, i przebierze się z pomocą",
        "5":   "sprawdzi mapę ubrania i wskaże na skali faktur, do którego poziomu dziś sięga w plastyce",
        "6":   "samo ustali swój poziom, wybierze materiał plastyczny i powie, czego dziś nie chce dotykać",
    },
    "wskaznik_obserwacji": "liczba dni, w których dziecko wskazało poziom przed zajęciami zamiast odmówić w trakcie",
    "dieta_sensoryczna": [
        "docisk przed przebieraniem (mocne przytulenie w kocyk, zabawa w naleśnik) — obniża próg drażliwości",
        "trzystopniowa skala faktur zawsze dostępna na stole plastycznym",
        "dwa warianty ubrania przygotowane przez rodzica w worku",
    ],
    "dostosowania": [
        "brak wymuszania fartuszka i rękawiczek w dniu wysokiej drażliwości",
        "materiały suche zawsze jako alternatywa dla mokrych",
        "informacja dla rodzica o poziomie z danego dnia — poranek w domu wygląda tak samo",
    ],
    "pomoc": {
        "nazwa": "Mapa ubrania i skala faktur 1–2–3",
        "opis_dla_doroslego": (
            "Karta z sylwetką dziecka do zaznaczenia miejsc, które dziś drapią, oraz pasek ze skalą "
            "faktur: suche (piasek, ryż) — wilgotne (masa, ciastolina) — lepkie (klej, farba palcowa)."
        ),
        "trzy_kroki_uzycia": [
            "Rano pokaż sylwetkę i poproś o wskazanie miejsc, które dziś przeszkadzają.",
            "Przed plastyką połóż pasek skali i przyjmij wskazanie dziecka bez negocjacji.",
            "Zapisz poziom w dzienniku i przekaż go rodzicowi przy odbiorze.",
        ],
        "wskazowka_dla_doroslego": (
            "Nie podnoś poziomu „na próbę”, gdy dziecko wskazało 1. Jedno wymuszone dotknięcie kleju "
            "potrafi zamknąć plastykę na kilka tygodni."
        ),
        "etykieta_dla_dziecka": "DZISIAJ MOGĘ TYLE",
        "polecenia": {
            "III": "Pokaż, co dziś drapie. Wybieramy ubranie razem.",
            "II":  "Wskaż na pasku: jeden, dwa czy trzy?",
            "I":   "Ustal swój poziom i powiedz, czego dziś nie chcesz dotykać.",
        },
    },
    "instrukcja_slowna": {
        "III": "Sprawdzamy, co dziś drapie. Pokazuję sylwetkę, ty wskazujesz palcem.",
        "II":  "Zanim zaczniemy plastykę — wskaż na pasku, ile dziś zniesiesz.",
        "I":   "Ustal poziom faktur i wybierz sobie materiał.",
    },
    "konspekt": {
        "temat": "Dzisiaj mogę tyle — dotyk, który zmienia się z dnia na dzień",
        "wprowadzenie": "„suche, wilgotne, lepkie” — dziecko dotyka trzech materiałów i układa je w kolejności od najłatwiejszego",
        "glowna": "wykonanie własnej mapy ubrania i paska skali; próba plastyczna na poziomie wskazanym przez dziecko, z możliwością zejścia o stopień w dół w każdej chwili",
        "zakonczenie": "umieszczenie paska na stole plastycznym i mapy w szatni",
        "metody": ["doświadczanie sensoryczne", "praca techniczna", "wybór kierowany"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "zejście o stopień w dół w trakcie zajęć jest sukcesem strategii, nie porażką dziecka",
    },
    "arkusz": {
        "tytul": "DZISIAJ MOGĘ TYLE — mapa ubrania i skala faktur",
        "elementy": [
            "sylwetka dziecka do zaznaczania miejsc drażniących (A4)",
            "pasek skali faktur 1–2–3 z obrazkami materiałów",
            "karta dla rodzica: dwa warianty ubrania w worku",
        ],
        "symbole": ["k_mapa_ubrania.jpg", "k_skala_faktur.jpg", "k_plastyka.jpg"],
    },
    "ryzyko": "nagły wzrost drażliwości dotykowej może być objawem infekcji, gorączki lub bólu — najpierw wyklucz przyczynę medyczną",
},

# ===== IV · SMAK (b250) ====================================================
{
    "id": "SENS-10", "kod": "SMA-NAD", "zmysl": "smak", "sektor": "nadwrazliwosc",
    "nazwa": "Oswajanie nowej potrawy bez presji jedzenia",
    "objawy": [
        "Je bardzo wąski repertuar potraw — odmawia nowych smaków i konsystencji",
        "Reaguje odruchem wymiotnym na niektóre konsystencje jedzenia",
        "Preferuje potrawy „bez smaku”, oddziela składniki na talerzu",
    ],
    "opis_dla_doroslego": (
        "Wybiórczość pokarmowa u dziecka z nadwrażliwością smakową nie jest grymaszeniem — "
        "odruch wymiotny jest realny. Namawianie i „jeszcze jedna łyżeczka” zawężają repertuar "
        "zamiast go poszerzać."
    ),
    "strategia_sensoryczna": (
        "Dziecko poznaje nową potrawę po drabinie oswajania: patrzę → dotykam widelcem → wącham → "
        "dotykam wargą → liżę → gryzę. Każdy szczebel jest sukcesem, jedzenie nie jest warunkiem."
    ),
    "sygnal_dziecka": "wskazanie szczebla na drabinie oswajania („dziś jestem tutaj”)",
    "kontekst": "przy posiłku w sali lub stołówce, przy własnym talerzyku do prób",
    "czynnosc": {
        "3-4": "z pomocą dorosłego położy nową potrawę na osobnym talerzyku i dotknie jej widelcem",
        "5":   "przejdzie o jeden szczebel drabiny oswajania w stosunku do poprzedniego posiłku z tą potrawą",
        "6":   "samo wskaże szczebel, na którym dziś jest, i wykona go bez namawiania przez dorosłego",
    },
    "wskaznik_obserwacji": "liczba posiłków, w których dziecko wykonało wskazany szczebel drabiny (nie: zjadło)",
    "dieta_sensoryczna": [
        "osobny mały talerzyk „do prób” obok talerza z jedzeniem znanym — nowa potrawa nigdy nie miesza się ze znaną",
        "przygotowanie jamy ustnej przed posiłkiem: picie przez rurkę, gryzak, chrupiąca przekąska",
        "udział w przygotowaniu potrawy (mycie, krojenie miękkiego) — dotyk poprzedza smak",
    ],
    "dostosowania": [
        "brak namawiania, komentowania i nagradzania za jedzenie",
        "składniki podawane osobno, nie wymieszane",
        "stałe, przewidywalne miejsce i pora posiłku",
    ],
    "pomoc": {
        "nazwa": "Drabina oswajania jedzenia (6 szczebli) + talerzyk do prób",
        "opis_dla_doroslego": (
            "Pionowa karta z sześcioma szczeblami: patrzę · dotykam widelcem · wącham · dotykam wargą · "
            "liżę · gryzę, każdy z obrazkiem. Do tego mały talerzyk na nową potrawę, stawiany zawsze "
            "z tej samej strony."
        ),
        "trzy_kroki_uzycia": [
            "Postaw talerzyk do prób obok talerza i połóż na nim jedną nową rzecz — nie trzy.",
            "Pokaż drabinę i zapytaj wyłącznie: „gdzie dziś jesteś?”. Nie proponuj wyżej.",
            "Odnotuj szczebel; przy następnym posiłku zacznij od tego samego, nie od wyższego.",
        ],
        "wskazowka_dla_doroslego": (
            "Zdanie „spróbuj tylko kawałeczek” cofa dziecko na sam dół drabiny. Sukcesem jest to, "
            "że nowa potrawa leży na stole i dziecko na nią patrzy."
        ),
        "etykieta_dla_dziecka": "MOJA DRABINA — dziś jestem tutaj",
        "polecenia": {
            "III": "Patrzymy na nowe jedzenie. Nie musisz jeść. Dotykam widelcem, zrób tak samo.",
            "II":  "Pokaż na drabinie, gdzie dziś jesteś. Zrób ten jeden szczebel.",
            "I":   "Wybierz swój szczebel na dziś i powiedz mi, kiedy skończysz.",
        },
    },
    "instrukcja_slowna": {
        "III": "To jest talerzyk do prób. Nie musisz jeść. Ja dotykam widelcem — spróbuj tak samo, razem.",
        "II":  "Na drabinie byłeś wczoraj tutaj. Gdzie jesteś dziś?",
        "I":   "Talerzyk stoi. Zdecyduj, który szczebel robisz dziś.",
    },
    "konspekt": {
        "temat": "Moja drabina — poznaję jedzenie bez jedzenia",
        "wprowadzenie": "zabawa „co to jest?” — rozpoznawanie warzyw po kształcie i zapachu, bez próbowania",
        "glowna": "wykonanie własnej drabiny oswajania (6 szczebli, naklejki), a potem jedna próba na talerzyku z nową potrawą — dziecko wybiera szczebel samo",
        "zakonczenie": "przypięcie drabiny w miejscu posiłku i ustalenie, że nikt nie namawia",
        "metody": ["zabawa badawcza", "praca plastyczna", "próba w warunkach naturalnych"],
        "formy": "indywidualna, przy stole",
        "ewaluacja_uwaga": "mierzymy szczebel drabiny, nigdy liczbę zjedzonych kęsów",
    },
    "arkusz": {
        "tytul": "DRABINA OSWAJANIA — karta do wycięcia",
        "elementy": [
            "drabina 6 szczebli (A4, pionowo) z obrazkami i strzałką do przesuwania",
            "karta „TALERZYK DO PRÓB” do położenia na stole",
            "karta dla rodzica: te same szczeble w domu",
        ],
        "symbole": ["k_drabina_jedzenie.jpg", "k_talerzyk_prob.jpg", "k_posilek.jpg"],
    },
    "ryzyko": "repertuar poniżej 15 produktów, spadek masy ciała lub krztuszenie się wymagają skierowania do lekarza i logopedy/neurologopedy — to zaburzenie karmienia, nie tylko sensoryka",
},
{
    "id": "SENS-11", "kod": "SMA-POD", "zmysl": "smak", "sektor": "podwrazliwosc",
    "nazwa": "Bezpieczny bodziec w jamie ustnej zamiast gryzienia przedmiotów",
    "objawy": [
        "Wkłada do ust przedmioty niejadalne, liże lub gryzie zabawki i przybory",
        "Poszukuje intensywnych smaków (ostre, kwaśne, bardzo słodkie)",
        "Przepełnia usta jedzeniem, je łapczywie",
    ],
    "opis_dla_doroslego": (
        "Jama ustna dziecka potrzebuje mocnego bodźca — stąd gryzienie rękawów, kredek i "
        "przepełnianie ust. To ryzyko połknięcia i urazu, ale też czytelna informacja: brakuje "
        "czucia, nie dyscypliny."
    ),
    "strategia_sensoryczna": (
        "Dziecko korzysta z bezpiecznego gryzaka na sznurku i „mocnych” bodźców jadalnych "
        "(picie gęstego przez rurkę, chrupiące, kwaśne) w stałych momentach dnia, a przy posiłku "
        "je łyżeczką odmierzającą jeden kęs."
    ),
    "sygnal_dziecka": "sięgnięcie po gryzak zawieszony przy fartuszku",
    "kontekst": "podczas zajęć przy stoliku i przy posiłkach w sali",
    "czynnosc": {
        "3-4": "użyje gryzaka zamiast rękawa lub kredki przy zadaniu przy stoliku",
        "5":   "przed zadaniem napije się gęstego napoju przez rurkę, a przy posiłku nabierze jeden kęs łyżeczką",
        "6":   "samo zaplanuje trzy momenty bodźca ustnego w ciągu dnia i utrzyma jeden kęs na raz przez cały posiłek",
    },
    "wskaznik_obserwacji": "liczba zajęć bez gryzienia przedmiotów niejadalnych, z użyciem gryzaka lub bodźca jadalnego",
    "dieta_sensoryczna": [
        "picie gęstego napoju (kisiel, jogurt pitny) przez wąską rurkę przed zajęciami wymagającymi skupienia",
        "chrupiąca przekąska (marchewka, wafel ryżowy) w połowie przedpołudnia",
        "gryzak silikonowy na sznurku, dostępny cały czas",
    ],
    "dostosowania": [
        "usunięcie z zasięgu drobnych przedmiotów, które można połknąć",
        "łyżeczka odmierzająca jeden kęs i przypomnienie „jeden kęs, potem następny”",
        "picie wody między kęsami — spowalnia jedzenie",
    ],
    "pomoc": {
        "nazwa": "Gryzak na sznurku + rurka i łyżeczka jednego kęsa",
        "opis_dla_doroslego": (
            "Silikonowy gryzak przypięty do fartuszka (mycie codziennie), wąska rurka do gęstych "
            "napojów oraz mała łyżeczka wyznaczająca wielkość kęsa. Trzy przedmioty, jedna zasada: "
            "usta dostają mocny bodziec w formie bezpiecznej."
        ),
        "trzy_kroki_uzycia": [
            "Przypnij gryzak rano i pokaż dziecku, że jest jego — nie wydawaj go na prośbę.",
            "Przed zadaniem przy stoliku podaj gęsty napój przez rurkę (1–2 minuty ssania).",
            "Przy posiłku połóż małą łyżeczkę i przypominaj krótko: „jeden kęs”.",
        ],
        "wskazowka_dla_doroslego": (
            "Zabranie gryzaka nie kończy gryzienia — przenosi je na rękawy i kredki. Gryzak myje się "
            "codziennie i wymienia przy pierwszych śladach nadgryzienia."
        ),
        "etykieta_dla_dziecka": "MOCNO W BUZI — mam swój gryzak",
        "polecenia": {
            "III": "Buzia chce mocno. Bierzemy gryzak. Kredka zostaje na stole.",
            "II":  "Weź gryzak, nie rękaw. Napij się przez rurkę.",
            "I":   "Przygotuj buzię przed zadaniem — wiesz, co robić.",
        },
    },
    "instrukcja_slowna": {
        "III": "Widzę, że buzia szuka. Podaję gryzak i przypinam go — kredka zostaje na stole.",
        "II":  "Zanim zaczniemy, napij się przez rurkę. Gryzak masz przy fartuszku.",
        "I":   "Zaplanuj, kiedy dziś napijesz się przez rurkę i kiedy zjesz chrupiące.",
    },
    "konspekt": {
        "temat": "Mocno w buzi — bezpieczne bodźce dla ust",
        "wprowadzenie": "zabawa „kto dmuchnie dalej” — dmuchanie przez rurkę na piłeczkę z waty",
        "glowna": "ćwiczenie ssania gęstego napoju przez wąską rurkę, gryzienia chrupiącej przekąski i używania gryzaka podczas krótkiego zadania przy stoliku; potem posiłek z łyżeczką jednego kęsa",
        "zakonczenie": "przypięcie gryzaka i ustalenie trzech pór bodźca ustnego w planie dnia",
        "metody": ["ćwiczenia oralno-motoryczne", "zabawa", "ćwiczenia praktyczne"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "notujemy gryzienie przedmiotów niejadalnych — spadek liczby jest miarą skuteczności",
    },
    "arkusz": {
        "tytul": "MOCNO W BUZI — karty i plan bodźców ustnych",
        "elementy": [
            "karta „GRYZAK” i karta „RURKA” (9 × 9 cm)",
            "plan dnia z trzema polami na bodziec ustny",
            "lista bezpiecznych chrupiących przekąsek z uwagą o alergiach",
        ],
        "symbole": ["k_gryzak.jpg", "k_rurka.jpg", "k_chrupiace.jpg"],
    },
    "ryzyko": "wkładanie do ust przedmiotów niejadalnych to ryzyko zadławienia i zatrucia — wymaga stałego nadzoru, kontroli zasięgu drobnych przedmiotów oraz wykluczenia niedoboru żelaza (pica)",
},
{
    "id": "SENS-12", "kod": "SMA-SZUM", "zmysl": "smak", "sektor": "bialy_szum",
    "nazwa": "Przewidywalny posiłek mimo zmiennej akceptacji smaków",
    "objawy": [
        "Akceptacja smaków i konsystencji zmienia się bez wyraźnej przyczyny",
        "Raz odmawia potrawy, którą innym razem je chętnie",
    ],
    "opis_dla_doroslego": (
        "Ta sama zupa raz jest zjadana, raz odrzucana. Dorosły odbiera to jako granie na nerwach; "
        "dla dziecka zmienia się sam odbiór smaku i konsystencji. Stałą ma być procedura posiłku, "
        "nie menu."
    ),
    "strategia_sensoryczna": (
        "Dziecko przed posiłkiem wskazuje na karcie „jak dziś smakuje” jeden z trzech wariantów "
        "(jem swoje · próbuję · dziś tylko patrzę) i według niego przebiega posiłek — bez negocjacji."
    ),
    "sygnal_dziecka": "położenie na stole jednej z trzech kart posiłku",
    "kontekst": "przy każdym posiłku w przedszkolu",
    "czynnosc": {
        "3-4": "z pomocą dorosłego wybierze jedną z trzech kart i zostanie przy stole do końca posiłku",
        "5":   "samo położy kartę przed posiłkiem i zje zgodnie z wybranym wariantem",
        "6":   "wybierze kartę, powie, co dziś jest inaczej, i zaproponuje, co zje zamiast odrzuconej potrawy",
    },
    "wskaznik_obserwacji": "liczba posiłków rozpoczętych wyborem karty i zakończonych przy stole, bez konfliktu",
    "dieta_sensoryczna": [
        "stała pora, miejsce i kolejność czynności przy posiłku — zmienne jest tylko menu",
        "zawsze jeden produkt pewny na talerzu, niezależnie od dania dnia",
        "przygotowanie ust przed posiłkiem (rurka, chrupiące) — obniża zmienność odbioru",
    ],
    "dostosowania": [
        "brak komentarza do wyboru dziecka przy stole",
        "informacja dla rodzica: dziś wariant „tylko patrzę” — kolacja zaplanowana z zapasem",
        "zapis wariantu w dzienniku — po dwóch tygodniach widać, czy zmienność ma rytm",
    ],
    "pomoc": {
        "nazwa": "Trzy karty posiłku",
        "opis_dla_doroslego": (
            "Zestaw trzech kart: „JEM SWOJE” (produkt pewny), „PRÓBUJĘ” (szczebel drabiny), "
            "„DZIŚ TYLKO PATRZĘ” (obecność przy stole bez jedzenia nowego). Wariant wybiera dziecko, "
            "dorosły go realizuje bez komentarza."
        ),
        "trzy_kroki_uzycia": [
            "Połóż trzy karty przy talerzu, zanim jedzenie trafi na stół.",
            "Przyjmij wybór dziecka bez pytania „dlaczego” i bez propozycji zmiany.",
            "Zapisz wariant w dzienniku i przekaż go rodzicowi przy odbiorze.",
        ],
        "wskazowka_dla_doroslego": (
            "Wariant „dziś tylko patrzę” też jest sukcesem: dziecko zostaje przy stole z grupą. "
            "Namawianie w takim dniu kosztuje więcej niż jeden pominięty posiłek."
        ),
        "etykieta_dla_dziecka": "JAK DZIŚ SMAKUJE",
        "polecenia": {
            "III": "Wybieramy kartę. Jem swoje, próbuję czy tylko patrzę?",
            "II":  "Połóż kartę przed jedzeniem.",
            "I":   "Wybierz kartę i powiedz, co dziś jest inaczej.",
        },
    },
    "instrukcja_slowna": {
        "III": "Zanim zjemy, wybieramy kartę. Trzymam trzy, ty wskazujesz jedną.",
        "II":  "Połóż kartę przed posiłkiem — będzie tak, jak wybierzesz.",
        "I":   "Wybierz kartę i powiedz mi, co dziś zjesz zamiast tego.",
    },
    "konspekt": {
        "temat": "Jak dziś smakuje — posiłek, który zawsze wygląda tak samo",
        "wprowadzenie": "rozmowa z obrazkami: „raz smakuje, raz nie” — dziecko dopasowuje buźki do potraw",
        "glowna": "wykonanie trzech kart posiłku i próba przy prawdziwym posiłku: dziecko wybiera kartę, dorosły realizuje wariant bez komentarza",
        "zakonczenie": "ustalenie miejsca kart przy stole i przekazanie informacji rodzicowi",
        "metody": ["rozmowa kierowana", "praca plastyczna", "próba w warunkach naturalnych"],
        "formy": "indywidualna, przy stole grupowym",
        "ewaluacja_uwaga": "sukces = wybór karty i pozostanie przy stole; ilość zjedzonego nie jest kryterium",
    },
    "arkusz": {
        "tytul": "JAK DZIŚ SMAKUJE — trzy karty posiłku",
        "elementy": [
            "karta „JEM SWOJE”, „PRÓBUJĘ”, „DZIŚ TYLKO PATRZĘ” (po 9 × 9 cm)",
            "podkładka na stół z polem na kartę dnia",
            "karta informacyjna dla rodzica",
        ],
        "symbole": ["k_jem_swoje.jpg", "k_probuje.jpg", "k_tylko_patrze.jpg"],
    },
    "ryzyko": "seria dni z wariantem „tylko patrzę” (powyżej 3 pod rząd) wymaga kontaktu z rodzicem i lekarzem — sprawdź ból gardła, zęby, refluks",
},

# ===== V · WĘCH (b255) =====================================================
{
    "id": "SENS-13", "kod": "WEC-NAD", "zmysl": "wech", "sektor": "nadwrazliwosc",
    "nazwa": "Pozostanie w sali mimo intensywnego zapachu",
    "objawy": [
        "Skarży się na zapachy, których inni nie czują; unika stołówki, toalet",
        "Reaguje mdłościami lub odmową na zapach jedzenia, środków czystości",
        "Zapach potrafi wytrącić je z równowagi na długi czas",
    ],
    "opis_dla_doroslego": (
        "Zapach stołówki albo płynu do podłóg potrafi wyłączyć dziecko z zajęć na godzinę. "
        "Reakcja bywa fizjologiczna — mdłości są prawdziwe. Unikanie toalety z tego powodu "
        "kończy się zatrzymywaniem moczu."
    ),
    "strategia_sensoryczna": (
        "Dziecko korzysta z „zapachu ratunkowego” (chusteczka z zapachem lubianym, np. cytryny, "
        "w kieszeni) i miejsca przy oknie, zamiast wychodzić z sali albo odmawiać wejścia do stołówki."
    ),
    "sygnal_dziecka": "wyjęcie chusteczki zapachowej lub karta „BRZYDKI ZAPACH”",
    "kontekst": "w stołówce, przy toalecie i w sali po sprzątaniu",
    "czynnosc": {
        "3-4": "przyłoży do nosa chusteczkę podaną przez dorosłego i wejdzie do stołówki z grupą",
        "5":   "samo wyjmie chusteczkę, usiądzie przy oknie i zostanie przy stole do końca posiłku",
        "6":   "przed wejściem zapowie, którego miejsca dziś potrzebuje, i skorzysta z chusteczki bez przypomnienia",
    },
    "wskaznik_obserwacji": "liczba sytuacji zapachowych, w których dziecko zostało w pomieszczeniu, korzystając ze strategii",
    "dieta_sensoryczna": [
        "chusteczka z 2 kroplami olejku cytrynowego w kieszeni — wymieniana codziennie",
        "wietrzenie sali przed zajęciami i po sprzątaniu, zawsze w tej samej porze",
        "krótka przerwa przy oknie po wejściu do stołówki (30 sekund) — zanim dziecko usiądzie",
    ],
    "dostosowania": [
        "miejsce przy oknie lub drzwiach, z dala od okienka wydawania posiłków i toalety",
        "sprzątanie środkami bezzapachowymi w porze pobytu dziecka",
        "uprzedzanie o mopowaniu i o daniach o intensywnym zapachu",
    ],
    "pomoc": {
        "nazwa": "Chusteczka ratunkowa + karta BRZYDKI ZAPACH",
        "opis_dla_doroslego": (
            "Bawełniana chusteczka w woreczku, z dwiema kroplami zapachu wybranego przez dziecko "
            "(najczęściej cytryna lub mięta), oraz karta-symbol pozwalająca zgłosić problem bez wychodzenia."
        ),
        "trzy_kroki_uzycia": [
            "Pozwól dziecku wybrać zapach z trzech propozycji — narzucony nie zadziała.",
            "Włóż chusteczkę do kieszeni rano; przy wejściu do stołówki tylko wskaż kieszeń.",
            "Odnotuj, czy dziecko weszło i zostało, i jak długo korzystało z chusteczki.",
        ],
        "wskazowka_dla_doroslego": (
            "Nie mów „przecież nic nie czuć”. Podważanie doznania odbiera dziecku sens sygnalizowania "
            "i kończy się wyjściem z sali bez uprzedzenia."
        ),
        "etykieta_dla_dziecka": "MÓJ ZAPACH — mam go w kieszeni",
        "polecenia": {
            "III": "Brzydki zapach. Dajemy chusteczkę do nosa. Wchodzimy razem.",
            "II":  "Weź chusteczkę z kieszeni. Usiądź przy oknie.",
            "I":   "Powiedz, gdzie dziś siadasz w stołówce.",
        },
    },
    "instrukcja_slowna": {
        "III": "Czuję, że tu mocno pachnie. Podaję ci chusteczkę i wchodzimy razem, na chwilę przy oknie.",
        "II":  "Chusteczka jest w kieszeni. Miejsce przy oknie jest wolne.",
        "I":   "Za chwilę stołówka. Zaplanuj, jak sobie poradzisz z zapachem.",
    },
    "konspekt": {
        "temat": "Mój zapach w kieszeni — zostaję, mimo że pachnie",
        "wprowadzenie": "„zgadnij, co pachnie” — trzy woreczki zapachowe, dziecko wybiera swój ulubiony",
        "glowna": "przygotowanie chusteczki ratunkowej i próba wejścia do stołówki poza porą posiłku, potem podczas posiłku, z miejscem przy oknie",
        "zakonczenie": "ustalenie stałego miejsca w stołówce i pory wymiany chusteczki",
        "metody": ["doświadczanie sensoryczne", "wybór kierowany", "próba w warunkach naturalnych"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "mierzymy pozostanie w pomieszczeniu, nie ilość zjedzonego posiłku",
    },
    "arkusz": {
        "tytul": "MÓJ ZAPACH — karty i woreczek na chusteczkę",
        "elementy": [
            "karta „BRZYDKI ZAPACH” (9 × 9 cm)",
            "karta „MOJE MIEJSCE PRZY OKNIE”",
            "szablon woreczka na chusteczkę zapachową",
        ],
        "symbole": ["k_brzydki_zapach.jpg", "k_okno.jpg", "k_stolowka.jpg"],
    },
    "ryzyko": "unikanie toalety z powodu zapachu prowadzi do zatrzymywania moczu i zaparć — wymaga natychmiastowego dostosowania i informacji dla rodzica",
},
{
    "id": "SENS-14", "kod": "WEC-POD", "zmysl": "wech", "sektor": "podwrazliwosc",
    "nazwa": "Zaplanowane wąchanie zamiast obwąchiwania ludzi i przedmiotów",
    "objawy": [
        "Obwąchuje przedmioty, jedzenie, ubrania, innych ludzi",
        "Nie zauważa wyraźnych, nieprzyjemnych zapachów",
        "Poszukuje intensywnych zapachów (klej, pisaki, środki czystości)",
    ],
    "opis_dla_doroslego": (
        "Obwąchiwanie kolegów bywa odbierane jako zaczepka, a poszukiwanie zapachu kleju i środków "
        "czystości jest realnie niebezpieczne. Dziecko szuka mocnego bodźca węchowego, którego "
        "w sali nie ma w wersji bezpiecznej."
    ),
    "strategia_sensoryczna": (
        "Dziecko korzysta z pudełka zapachów (3–5 woreczków: cytryna, mięta, kawa, cynamon) "
        "w zaplanowanych momentach dnia, zamiast obwąchiwać ludzi i sięgać po chemię."
    ),
    "sygnal_dziecka": "karta „CHCĘ POWĄCHAĆ” wymieniana na dostęp do pudełka zapachów",
    "kontekst": "podczas zabawy swobodnej i zajęć przy stoliku w sali",
    "czynnosc": {
        "3-4": "podejdzie do pudełka zapachów wskazanego przez dorosłego i powącha woreczek zamiast kolegi",
        "5":   "wymieni kartę na dostęp do pudełka i wróci do zabawy po dwóch minutach",
        "6":   "samo zaplanuje dwa momenty wąchania w ciągu dnia i skorzysta z nich, zanim zacznie obwąchiwać innych",
    },
    "wskaznik_obserwacji": "liczba dni bez obwąchiwania innych dzieci i sięgania po środki chemiczne",
    "dieta_sensoryczna": [
        "pudełko zapachów na stałej półce — 2 minuty na sygnał, 2 razy dziennie",
        "zajęcia kulinarne z przyprawami (cynamon, wanilia) jako mocny bodziec zaplanowany",
        "wąchanie przed jedzeniem — zapach jako element rozpoznawania potrawy",
    ],
    "dostosowania": [
        "kleje, pisaki i środki czystości zamknięte i poza zasięgiem dziecka",
        "zamiast upomnienia „nie wąchaj” — wskazanie pudełka",
        "informacja dla wszystkich dorosłych w grupie: to potrzeba, nie zaczepka",
    ],
    "pomoc": {
        "nazwa": "Pudełko zapachów (5 woreczków) z kartą wymiany",
        "opis_dla_doroslego": (
            "Pudełko z pięcioma woreczkami z gazy: cytryna, mięta, kawa, cynamon, lawenda. "
            "Zawartość wymieniana co dwa tygodnie. Karta „CHCĘ POWĄCHAĆ” zamienia bodziec "
            "przypadkowy na zaplanowany."
        ),
        "trzy_kroki_uzycia": [
            "Postaw pudełko na stałej półce i przedstaw wszystkie zapachy pierwszego dnia.",
            "Przyjmuj kartę i odliczaj dwie minuty klepsydrą — koniec zawsze tym samym zdaniem.",
            "Zapisuj, po który zapach dziecko sięga najczęściej — to on działa najlepiej.",
        ],
        "wskazowka_dla_doroslego": (
            "Środki czystości i kleje muszą zniknąć z zasięgu, zanim wprowadzisz pudełko. "
            "Sama alternatywa nie wystarczy, gdy silniejszy bodziec stoi na parapecie."
        ),
        "etykieta_dla_dziecka": "CHCĘ POWĄCHAĆ — idę do pudełka",
        "polecenia": {
            "III": "Wąchamy tutaj. To jest pudełko zapachów. Idziemy razem.",
            "II":  "Podaj kartę i idź do pudełka. Dwie minuty.",
            "I":   "Powiedz, kiedy dziś pójdziesz powąchać.",
        },
    },
    "instrukcja_slowna": {
        "III": "Widzę, że szukasz zapachu. Idziemy do pudełka — kolegi nie wąchamy, wąchamy woreczki.",
        "II":  "Masz kartę „CHCĘ POWĄCHAĆ”. Pudełko stoi na półce.",
        "I":   "Zaplanuj sobie dziś dwie chwile przy pudełku zapachów.",
    },
    "konspekt": {
        "temat": "Pudełko zapachów — wąchanie, które ma swoje miejsce",
        "wprowadzenie": "„zgadnij po zapachu” — rozpoznawanie trzech przypraw z zawiązanymi oczami",
        "glowna": "przygotowanie własnych woreczków zapachowych (napełnianie, wiązanie, opisanie obrazkiem) i ćwiczenie wymiany karty na dostęp; rozmowa o tym, czego się nie wącha (klej, chemia)",
        "zakonczenie": "ustawienie pudełka na półce i ustalenie dwóch pór w planie dnia",
        "metody": ["zabawa badawcza", "praca techniczna", "rozmowa o bezpieczeństwie"],
        "formy": "indywidualna lub w parze",
        "ewaluacja_uwaga": "notujemy obwąchiwanie ludzi i sięganie po chemię — to te liczby mają spadać",
    },
    "arkusz": {
        "tytul": "PUDEŁKO ZAPACHÓW — karty i etykiety woreczków",
        "elementy": [
            "karta „CHCĘ POWĄCHAĆ” (9 × 9 cm)",
            "5 etykiet na woreczki z obrazkami (cytryna, mięta, kawa, cynamon, lawenda)",
            "karta „TEGO NIE WĄCHAMY” z rysunkami kleju i środków czystości",
        ],
        "symbole": ["k_chce_powachac.jpg", "k_pudelko_zapachow.jpg", "k_stop_chemia.jpg"],
    },
    "ryzyko": "wdychanie kleju i środków czystości grozi zatruciem i uszkodzeniem dróg oddechowych — zabezpieczenie chemii jest warunkiem wstępnym, nie zaleceniem",
},
{
    "id": "SENS-15", "kod": "WEC-SZUM", "zmysl": "wech", "sektor": "bialy_szum",
    "nazwa": "Codzienne sprawdzenie wrażliwości na zapachy",
    "objawy": [
        "Reakcje na zapachy są niestałe — ten sam zapach raz przeszkadza, raz jest niezauważany",
        "Wrażliwość na zapachy zmienia się z dnia na dzień",
    ],
    "opis_dla_doroslego": (
        "Zmienność węchowa najczęściej wiąże się z katarem, alergią i porą roku, ale dla dziecka "
        "oznacza jedno: nie wie, czy dziś wytrzyma w stołówce. Sprawdzenie przed posiłkiem "
        "zajmuje pół minuty i oszczędza konflikt."
    ),
    "strategia_sensoryczna": (
        "Dziecko przed posiłkiem sprawdza swój „nos dnia” na dwóch woreczkach kontrolnych i na tej "
        "podstawie decyduje, czy bierze chusteczkę ratunkową i miejsce przy oknie."
    ),
    "sygnal_dziecka": "wskazanie buźki przy karcie „NOS DNIA” (mocno czuję / normalnie / nie czuję)",
    "kontekst": "przed posiłkami i przed zajęciami plastycznymi z farbami lub klejem",
    "czynnosc": {
        "3-4": "powącha woreczek kontrolny z dorosłym i wskaże jedną z dwóch buziek",
        "5":   "samo sprawdzi nos dnia i weźmie chusteczkę, jeśli wskazał „mocno czuję”",
        "6":   "sprawdzi nos dnia, wybierze miejsce i powie, czego dziś unika",
    },
    "wskaznik_obserwacji": "liczba posiłków poprzedzonych sprawdzeniem nosa dnia",
    "dieta_sensoryczna": [
        "dwa woreczki kontrolne (cytryna i mięta) przy wejściu do sali",
        "sprawdzenie przed posiłkiem i przed plastyką — dwa razy dziennie",
        "wietrzenie sali według wskazania dziecka, nie tylko według harmonogramu",
    ],
    "dostosowania": [
        "brak stałego wpisu „nadwrażliwość węchowa” — decyzja zapada codziennie",
        "informacja dla rodzica przy katarze: dziś wskazania mogą być inne",
        "zapis wskazania w dzienniku obserwacji",
    ],
    "pomoc": {
        "nazwa": "Nos dnia — dwa woreczki kontrolne i karta z buźkami",
        "opis_dla_doroslego": (
            "Dwa woreczki o stałym, znanym zapachu (cytryna, mięta) oraz karta z trzema buźkami: "
            "mocno czuję · normalnie · nie czuję. Stałość zapachu jest tu warunkiem — inaczej "
            "porównanie z wczoraj traci sens."
        ),
        "trzy_kroki_uzycia": [
            "Powieś kartę i woreczki przy wejściu do sali, na wysokości dziecka.",
            "Przed posiłkiem poproś o powąchanie obu woreczków i wskazanie buźki.",
            "Zrealizuj to, co ze wskazania wynika (chusteczka, miejsce) i zapisz wynik.",
        ],
        "wskazowka_dla_doroslego": (
            "Woreczki wymieniaj co dwa tygodnie, zawsze na ten sam zapach. Zapach, który zwietrzał, "
            "daje fałszywe „nie czuję”."
        ),
        "etykieta_dla_dziecka": "MÓJ NOS DZISIAJ",
        "polecenia": {
            "III": "Sprawdzamy nos. Wąchamy woreczek. Którą buźkę wybierasz?",
            "II":  "Powąchaj oba woreczki i wskaż buźkę.",
            "I":   "Sprawdź nos dnia i powiedz, czego dziś potrzebujesz.",
        },
    },
    "instrukcja_slowna": {
        "III": "Zanim pójdziemy jeść, sprawdzimy twój nos. Podaję woreczek — powąchaj.",
        "II":  "Sprawdź nos dnia. Jeśli mocno czujesz, weź chusteczkę.",
        "I":   "Sprawdź nos i zdecyduj, gdzie dziś siadasz.",
    },
    "konspekt": {
        "temat": "Mój nos dzisiaj — sprawdzam, zanim wejdę",
        "wprowadzenie": "porównanie dwóch woreczków: „który mocniejszy?” — dziecko ustawia je w kolejności",
        "glowna": "wykonanie karty z buźkami i pierwsze sprawdzenie przed prawdziwym posiłkiem; realizacja wynikającego dostosowania i porównanie z dniem poprzednim",
        "zakonczenie": "powieszenie karty i woreczków przy wejściu, ustalenie dwóch pór sprawdzania",
        "metody": ["doświadczanie sensoryczne", "praca plastyczna", "ćwiczenia porównawcze"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "sukces = sprawdzenie przed sytuacją zapachową; trafność ocenia się po dwóch tygodniach wpisów",
    },
    "arkusz": {
        "tytul": "NOS DNIA — karta z buźkami i etykiety woreczków",
        "elementy": [
            "karta „NOS DNIA” z trzema buźkami (A5)",
            "2 etykiety woreczków kontrolnych z datą wymiany",
            "karta informacyjna dla rodzica o katarze i alergii",
        ],
        "symbole": ["k_nos_dnia.jpg", "k_woreczek_zapach.jpg", "k_brzydki_zapach.jpg"],
    },
    "ryzyko": "utrzymujące się „nie czuję” wymaga kontroli laryngologicznej (przerost migdałka, alergia) — brak węchu wpływa też na apetyt",
},

# ===== VI · PROPRIOCEPCJA (b760) ===========================================
{
    "id": "SENS-16", "kod": "PRO-NAD", "zmysl": "propriocepcja", "sektor": "nadwrazliwosc",
    "nazwa": "Udział w wysiłku fizycznym małymi krokami",
    "objawy": [
        "Unika wysiłku fizycznego, wspinania, przepychania — szybko się męczy",
        "Słabo dozuje siłę — rysuje zbyt lekko, upuszcza przedmioty",
        "Jest ostrożne ruchowo, sztywno trzyma ciało przy nowych czynnościach",
    ],
    "opis_dla_doroslego": (
        "Dziecko wycofuje się z zabaw ruchowych, bo wysiłek jest dla niego kosztowny, a informacja "
        "z mięśni niepewna. Sztywność ciała przy nowej czynności to ostrożność, nie lenistwo. "
        "Zbyt lekki nacisk kredki ma to samo źródło."
    ),
    "strategia_sensoryczna": (
        "Dziecko wchodzi w wysiłek po własnej „drabinie ruchu” — od zadań z podparciem i małym "
        "obciążeniem do większych — i samo decyduje o kolejnym szczeblu, korzystając z pomocy "
        "wyznaczających siłę (kredka z nakładką, dzbanek z miarką)."
    ),
    "sygnal_dziecka": "wskazanie szczebla na drabinie ruchu („dziś robię ten”)",
    "kontekst": "podczas zajęć ruchowych w sali i na placu zabaw oraz przy pracy przy stoliku",
    "czynnosc": {
        "3-4": "wykona jedno zadanie z oporem (pchanie pudła z klockami po podłodze) z pomocą dorosłego",
        "5":   "wykona dwa kolejne szczeble drabiny ruchu i użyje nakładki na kredkę przy rysowaniu",
        "6":   "samo wskaże szczebel, wykona go i powie, w której części ciała poczuło pracę mięśni",
    },
    "wskaznik_obserwacji": "liczba zajęć ruchowych, w których dziecko wykonało zaplanowany szczebel zamiast wycofać się",
    "dieta_sensoryczna": [
        "zadania oporowe wplecione w dzień: pchanie pudła, noszenie koszyka z klockami, wycieranie stołu",
        "praca w pozycji na brzuchu przy niskim stoliku — buduje napięcie mięśniowe",
        "krótkie serie (2–3 minuty) częściej, zamiast jednego długiego wysiłku",
    ],
    "dostosowania": [
        "krzesło z podparciem stóp i blat na wysokości łokci",
        "nakładka na kredkę i kredki trójkątne — wyznaczają nacisk",
        "brak porównywania z rówieśnikami i wyścigów na czas",
    ],
    "pomoc": {
        "nazwa": "Drabina ruchu (5 szczebli) + nakładka na kredkę",
        "opis_dla_doroslego": (
            "Karta z pięcioma szczeblami zadań oporowych — od najlżejszego (wycieranie stołu) "
            "do najcięższego (pchanie pudła z klockami) — oraz gumowa nakładka wyznaczająca chwyt "
            "i nacisk kredki."
        ),
        "trzy_kroki_uzycia": [
            "Ułóż z dzieckiem drabinę: pięć zadań, od najłatwiejszego do najcięższego.",
            "Przed zajęciami ruchowymi poproś o wskazanie dzisiejszego szczebla — bez podnoszenia poprzeczki.",
            "Po zadaniu nazwij, gdzie pracowały mięśnie („czujesz ręce?”) i odnotuj szczebel.",
        ],
        "wskazowka_dla_doroslego": (
            "„Spróbuj jeszcze raz, dasz radę” nie działa przy nadwrażliwości proprioceptywnej. "
            "Działa mniejszy szczebel wykonany do końca."
        ),
        "etykieta_dla_dziecka": "MOJA DRABINA RUCHU",
        "polecenia": {
            "III": "Pchamy pudło razem. Ja z jednej strony, ty z drugiej.",
            "II":  "Wskaż szczebel na drabinie i zrób go.",
            "I":   "Wybierz dziś swój szczebel i powiedz, gdzie poczułeś mięśnie.",
        },
    },
    "instrukcja_slowna": {
        "III": "Robimy jedno zadanie, razem. Trzymam pudło z tobą — pchamy do dywanu i koniec.",
        "II":  "Pokaż na drabinie, który szczebel robisz dziś.",
        "I":   "Wybierz szczebel przed zajęciami i powiedz mi, jak poszło.",
    },
    "konspekt": {
        "temat": "Moja drabina ruchu — wysiłek w moim tempie",
        "wprowadzenie": "zabawa „ciężkie i lekkie” — dziecko porównuje dwa koszyki i nazywa różnicę",
        "glowna": "ułożenie własnej drabiny ruchu z pięciu zadań oporowych i wykonanie dwóch najniższych szczebli; ćwiczenie nacisku kredki na papierze z trzema polami (lekko / średnio / mocno)",
        "zakonczenie": "powieszenie drabiny w sali i wybór szczebla na jutro",
        "metody": ["ćwiczenia oporowe", "zabawa porównawcza", "ćwiczenia grafomotoryczne"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "notujemy dokończone szczeble, nie czas ani liczbę powtórzeń",
    },
    "arkusz": {
        "tytul": "DRABINA RUCHU — karta i pola nacisku kredki",
        "elementy": [
            "drabina 5 szczebli (A4) z obrazkami zadań oporowych",
            "karta ćwiczenia nacisku: trzy pola (lekko / średnio / mocno)",
            "lista 10 zadań oporowych do wplecenia w dzień",
        ],
        "symbole": ["k_drabina_ruchu.jpg", "k_pchanie.jpg", "k_nacisk_kredki.jpg"],
    },
    "ryzyko": "szybka męczliwość i sztywność ciała wymagają wykluczenia przyczyn ortopedycznych i neurologicznych (obniżone napięcie mięśniowe) — konsultacja fizjoterapeuty",
},
{
    "id": "SENS-17", "kod": "PRO-POD", "zmysl": "propriocepcja", "sektor": "podwrazliwosc",
    "nazwa": "Zaplanowana przerwa proprioceptywna zamiast napierania na innych",
    "objawy": [
        "Poszukuje mocnego docisku — rzuca się na podłogę/materace, wciska w ciasne miejsca, mocno przytula",
        "Gryzie rękawy/przybory, zaciska pięści, napiera na innych podczas zabawy",
        "Rysuje z bardzo mocnym naciskiem, niszczy przybory",
    ],
    "opis_dla_doroslego": (
        "To najczęstszy profil w grupie przedszkolnej: dziecko potrzebuje mocnego docisku i dobiera "
        "go sobie kosztem innych dzieci i przyborów. Zakaz („nie przewracaj się na kolegów”) nie "
        "zaspokaja potrzeby; zaplanowany docisk — tak."
    ),
    "strategia_sensoryczna": (
        "Dziecko korzysta z zaplanowanej przerwy proprioceptywnej — docisk (kocyk obciążeniowy, "
        "poduszka, przeciskanie przez tunel), praca oporowa, ugniatanie — i wraca do zabawy, "
        "zamiast napierać na rówieśników."
    ),
    "sygnal_dziecka": "karta „MOCNO” wymieniana na 3 minuty przerwy proprioceptywnej",
    "kontekst": "podczas zabawy swobodnej, w kręgu i przed zajęciami wymagającymi siedzenia",
    "czynnosc": {
        "3-4": "z pomocą dorosłego skorzysta z kocyka obciążeniowego przez 3 minuty i wróci do zabawy",
        "5":   "poda kartę „MOCNO”, wykona przerwę proprioceptywną i wróci do zabawy bez napierania na dzieci",
        "6":   "samo zaplanuje trzy przerwy w ciągu dnia i skorzysta z nich, zanim napięcie zamieni się w przewracanie kolegów",
    },
    "wskaznik_obserwacji": "liczba dni, w których dziecko użyło przerwy proprioceptywnej zamiast napierać na inne dzieci",
    "dieta_sensoryczna": [
        "docisk co 90 minut: kocyk obciążeniowy 3–5 minut albo mocne przytulenie w zwiniętym kocu",
        "praca oporowa: pchanie skrzynki, przeciąganie liny, przeciskanie przez tunel",
        "ugniatanie ciastoliny lub gąbki przed siedzeniem w kręgu",
    ],
    "dostosowania": [
        "poduszka sensoryczna na krześle — pozwala pracować mięśniom w czasie siedzenia",
        "miejsce w kręgu przy brzegu, z jednym sąsiadem",
        "przybory odporne na nacisk (kredki woskowe, gruby papier)",
    ],
    "pomoc": {
        "nazwa": "Kącik docisku: kocyk obciążeniowy, tunel, poduszka sensoryczna",
        "opis_dla_doroslego": (
            "Wydzielone miejsce z kocykiem obciążeniowym (do 10% masy ciała dziecka), tunelem do "
            "przeciskania i poduszką sensoryczną, plus karta „MOCNO” do wymiany. Kącik jest dostępny "
            "zawsze, nie na nagrodę."
        ),
        "trzy_kroki_uzycia": [
            "Wyznacz kącik i pokaż dziecku trzy rzeczy, których może w nim użyć.",
            "Wpisz przerwy do planu dnia (co 90 minut) — nie czekaj na przewrócenie kolegi.",
            "Po przerwie zamknij ją tym samym zdaniem i odnotuj, czy sygnał wyszedł od dziecka.",
        ],
        "wskazowka_dla_doroslego": (
            "Kocyk obciążeniowy: maksymalnie 10% masy ciała, nigdy na głowę i klatkę piersiową, "
            "zawsze pod nadzorem dorosłego i nigdy podczas snu."
        ),
        "etykieta_dla_dziecka": "MOCNO — idę po docisk",
        "polecenia": {
            "III": "Twoje ciało chce mocno. Idziemy po kocyk. Liczę do stu.",
            "II":  "Podaj kartę „MOCNO” i idź do kącika. Trzy minuty.",
            "I":   "Powiedz, kiedy robisz dziś przerwę na docisk.",
        },
    },
    "instrukcja_slowna": {
        "III": "Widzę, że ciało szuka mocnego. Idziemy do kącika, przykrywam cię kocykiem i siedzę obok.",
        "II":  "Masz kartę „MOCNO”. Kącik jest wolny — trzy minuty i wracasz.",
        "I":   "Zaplanuj trzy przerwy na docisk. Powiedz mi, kiedy pierwsza.",
    },
    "konspekt": {
        "temat": "Mocno i bezpiecznie — docisk, który mam zaplanowany",
        "wprowadzenie": "zabawa „naleśnik” — zawijanie dziecka w koc i mocne, równomierne dociskanie dłońmi",
        "glowna": "obwód proprioceptywny: przeciskanie przez tunel, pchanie skrzynki z klockami, przeciąganie liny, ugniatanie ciastoliny; po obwodzie próba siedzenia w kręgu przez czas dwóch piosenek",
        "zakonczenie": "wyznaczenie kącika docisku i wpisanie trzech przerw do planu dnia",
        "metody": ["ćwiczenia proprioceptywne", "obwód stacyjny", "ćwiczenia praktyczne"],
        "formy": "indywidualna, następnie w małej grupie",
        "ewaluacja_uwaga": "notujemy liczbę napierań na inne dzieci — to ona ma spadać po wprowadzeniu przerw",
    },
    "arkusz": {
        "tytul": "MOCNO — karta wymiany i plan przerw proprioceptywnych",
        "elementy": [
            "karta „MOCNO” (9 × 9 cm) — 2 sztuki",
            "plan dnia z trzema polami na przerwę proprioceptywną",
            "karta bezpieczeństwa kocyka obciążeniowego (10% masy ciała, nadzór, nigdy podczas snu)",
        ],
        "symbole": ["k_mocno.jpg", "k_kocyk.jpg", "k_tunel.jpg"],
    },
    "ryzyko": "kocyk obciążeniowy tylko pod nadzorem, do 10% masy ciała, nigdy podczas snu i nigdy na klatkę piersiową — przy wadach serca i padaczce wymaga zgody lekarza",
},
{
    "id": "SENS-18", "kod": "PRO-SZUM", "zmysl": "propriocepcja", "sektor": "bialy_szum",
    "nazwa": "Rozpoznawanie i dozowanie siły w danym dniu",
    "objawy": [
        "Dozowanie siły jest zmienne — raz za mocno, raz za słabo (rysowanie, zabawa, przybory)",
        "Raz unika wysiłku, innym razem poszukuje mocnego docisku",
    ],
    "opis_dla_doroslego": (
        "Dziecko nie ma stabilnej informacji o sile własnych ruchów — raz rozdziera kartkę, raz "
        "rysuje ledwie widoczną kreskę. Rówieśnicy odbierają zbyt mocny dotyk jako bicie, choć "
        "dziecko chciało tylko dotknąć."
    ),
    "strategia_sensoryczna": (
        "Dziecko przed zadaniem sprawdza siłę na „mierniku siły” (trzy pola nacisku na papierze) "
        "i dobiera do dnia narzędzie oraz sposób dotykania kolegów („dotyk jak piórko”)."
    ),
    "sygnal_dziecka": "wskazanie pola na mierniku siły przed zadaniem",
    "kontekst": "przed zadaniami przy stoliku i przed zabawą w parze z rówieśnikiem",
    "czynnosc": {
        "3-4": "z pomocą dorosłego zrobi próbę na trzech polach nacisku i zacznie rysować",
        "5":   "samo sprawdzi miernik siły, dobierze kredkę i przypomni sobie „dotyk jak piórko” przed zabawą w parze",
        "6":   "sprawdzi siłę, dobierze narzędzie i samo skoryguje nacisk w trakcie zadania, gdy zauważy, że jest za mocny",
    },
    "wskaznik_obserwacji": "liczba zadań rozpoczętych sprawdzeniem siły i skończonych bez zniszczenia przyboru lub kartki",
    "dieta_sensoryczna": [
        "sprawdzenie miernika siły przed każdym zadaniem grafomotorycznym",
        "praca oporowa przed zadaniem — porządkuje czucie i zmniejsza zmienność",
        "zabawy z dozowaniem: przelewanie wody, przenoszenie piórka na łyżce, budowanie z kubków",
    ],
    "dostosowania": [
        "gruby papier i kredki odporne na nacisk",
        "podkładka antypoślizgowa pod kartkę",
        "przypomnienie o sile przed zabawą w parze, nie po incydencie",
    ],
    "pomoc": {
        "nazwa": "Miernik siły — trzy pola nacisku",
        "opis_dla_doroslego": (
            "Kartka z trzema polami: „piórko” (ledwie widoczna kreska), „w sam raz”, „za mocno” "
            "(kartka się rwie). Dziecko wykonuje trzy kreski i sprawdza, gdzie dziś jest jego ręka."
        ),
        "trzy_kroki_uzycia": [
            "Połóż miernik przed zadaniem i poproś o trzy kreski — po jednej na pole.",
            "Nazwij wynik i dobierz narzędzie: cienka kredka przy „za mocno”, gruba przy „piórku”.",
            "W trakcie zadania przypomnij raz, wskazując pole „w sam raz”.",
        ],
        "wskazowka_dla_doroslego": (
            "Nie mów „rysuj mocniej” ani „delikatniej” bez odniesienia. Dziecko nie ma wzorca — "
            "miernik daje mu ten wzorzec na papierze."
        ),
        "etykieta_dla_dziecka": "MOJA SIŁA DZISIAJ",
        "polecenia": {
            "III": "Robimy trzy kreski. Piórko, w sam raz, za mocno. Prowadzę twoją rękę.",
            "II":  "Zrób trzy kreski na mierniku. Która jest w sam raz?",
            "I":   "Sprawdź siłę i wybierz kredkę na dziś.",
        },
    },
    "instrukcja_slowna": {
        "III": "Sprawdzamy twoją rękę. Trzy kreski — prowadzę razem z tobą.",
        "II":  "Zanim zaczniesz, zrób próbę na mierniku i wskaż „w sam raz”.",
        "I":   "Sprawdź miernik, dobierz kredkę i pamiętaj o dotyku jak piórko w parze.",
    },
    "konspekt": {
        "temat": "Moja siła dzisiaj — mocno, delikatnie, w sam raz",
        "wprowadzenie": "zabawa „piórko i kamień” — dotykanie dłoni dorosłego raz lekko, raz mocno, z nazywaniem",
        "glowna": "próba na mierniku siły i dobór narzędzia; zabawy z dozowaniem (przenoszenie piórka, przelewanie wody, wieża z kubków); ćwiczenie „dotyk jak piórko” w parze z rówieśnikiem",
        "zakonczenie": "przypięcie miernika przy stoliku i ustalenie, że sprawdzamy przed każdym rysowaniem",
        "metody": ["ćwiczenia dozowania siły", "zabawa w parze", "ćwiczenia grafomotoryczne"],
        "formy": "indywidualna, potem w parze",
        "ewaluacja_uwaga": "notujemy zniszczone kartki i przybory oraz zbyt mocne dotknięcia rówieśników",
    },
    "arkusz": {
        "tytul": "MIERNIK SIŁY — karta z trzema polami nacisku",
        "elementy": [
            "karta miernika (A4) z polami: piórko / w sam raz / za mocno",
            "karta „DOTYK JAK PIÓRKO” do zabawy w parze",
            "lista 6 zabaw z dozowaniem siły",
        ],
        "symbole": ["k_miernik_sily.jpg", "k_piorko.jpg", "k_w_sam_raz.jpg"],
    },
    "ryzyko": "duża zmienność siły przy jednoczesnym potykaniu się i upuszczaniu przedmiotów wymaga konsultacji fizjoterapeuty i terapeuty SI",
},

# ===== VII · RÓWNOWAGA / UKŁAD PRZEDSIONKOWY (b235) ========================
{
    "id": "SENS-19", "kod": "ROW-NAD", "zmysl": "rownowaga", "sektor": "nadwrazliwosc",
    "nazwa": "Oswajanie ruchu i wysokości metodą małych kroków",
    "objawy": [
        "Boi się huśtawek, zjeżdżalni, schodów, oderwania nóg od podłoża",
        "Ma chorobę lokomocyjną, unika zabaw z obracaniem i zmianą pozycji głowy",
        "Unika zajęć ruchowych, placu zabaw, jazdy na rowerku/hulajnodze",
    ],
    "opis_dla_doroslego": (
        "Lęk przed oderwaniem nóg od podłoża jest reakcją układu przedsionkowego, nie tchórzostwem. "
        "Wsadzenie dziecka na huśtawkę „żeby się przekonało” utrwala lęk na miesiące. Praca idzie "
        "wyłącznie małymi krokami, z zachowaniem kontroli po stronie dziecka."
    ),
    "strategia_sensoryczna": (
        "Dziecko wchodzi w ruch po własnej drabinie (stopy na podłożu → huśtanie z podparciem nóg → "
        "krótkie huśtanie → zjeżdżalnia z asekuracją), zawsze samo decyduje o wejściu i ma słowo, "
        "którym ruch zatrzymuje („stop”)."
    ),
    "sygnal_dziecka": "słowo „STOP” lub karta STOP zatrzymująca ruch natychmiast",
    "kontekst": "na placu zabaw i podczas zajęć ruchowych w sali",
    "czynnosc": {
        "3-4": "usiądzie na huśtawce z nogami opartymi o podłoże i pobuja się przez 10 sekund z dorosłym obok",
        "5":   "wykona jeden kolejny szczebel drabiny ruchu przedsionkowego, korzystając ze słowa „STOP”",
        "6":   "samo zaplanuje szczebel na dziś, wejdzie na sprzęt i zatrzyma ruch własnym słowem, gdy poczuje, że to za dużo",
    },
    "wskaznik_obserwacji": "liczba wyjść na plac zabaw, w których dziecko weszło na sprzęt na wybranym przez siebie szczeblu",
    "dieta_sensoryczna": [
        "przed ruchem: docisk i praca oporowa (propriocepcja wycisza układ przedsionkowy)",
        "ruch liniowy (huśtanie przód-tył) zamiast obrotowego — obrót zostawiamy na koniec drogi",
        "krótkie serie 10–20 sekund z przerwą na stanie obiema stopami na ziemi",
    ],
    "dostosowania": [
        "brak wsadzania na sprzęt „na siłę” i brak niespodziewanego rozhuśtania",
        "trzymanie się za ręce przy schodach, stopy zawsze widoczne dla dziecka",
        "uprzedzanie o każdej zmianie pozycji głowy przy ubieraniu i myciu",
    ],
    "pomoc": {
        "nazwa": "Drabina ruchu przedsionkowego + karta STOP",
        "opis_dla_doroslego": (
            "Karta z pięcioma szczeblami wchodzenia w ruch (od stóp na podłożu do zjeżdżalni) "
            "i czerwona karta STOP, która natychmiast zatrzymuje ruch. Kontrola musi zostać "
            "po stronie dziecka — inaczej drabina nie działa."
        ),
        "trzy_kroki_uzycia": [
            "Ustal z dzieckiem pięć szczebli i zapisz je obrazkami na karcie.",
            "Przed wyjściem na plac poproś o wskazanie dzisiejszego szczebla — nigdy nie proponuj wyższego.",
            "Zatrzymaj ruch natychmiast po słowie lub karcie STOP, bez negocjacji i bez „jeszcze chwilkę”.",
        ],
        "wskazowka_dla_doroslego": (
            "Jedno rozhuśtanie wbrew dziecku kosztuje kilka tygodni pracy. Wiarygodność słowa „STOP” "
            "jest tu jedynym narzędziem, które buduje odwagę."
        ),
        "etykieta_dla_dziecka": "STOP — zatrzymuję ruch",
        "polecenia": {
            "III": "Siadamy na huśtawce. Stopy na ziemi. Trzymam cię. Powiedz stop, kiedy chcesz.",
            "II":  "Wskaż szczebel na drabinie. Karta STOP jest u ciebie.",
            "I":   "Wybierz dziś swój szczebel. Pamiętasz, jak zatrzymać ruch?",
        },
    },
    "instrukcja_slowna": {
        "III": "Siadamy razem, stopy zostają na ziemi. Ja trzymam. Kiedy powiesz stop — zatrzymuję.",
        "II":  "Który szczebel robisz dziś? Karta STOP jest w twojej kieszeni.",
        "I":   "Zaplanuj szczebel przed wyjściem i powiedz mi, kiedy zaczynasz.",
    },
    "konspekt": {
        "temat": "Krok po kroku na huśtawkę — ruch, który zatrzymuję sam",
        "wprowadzenie": "praca oporowa przed ruchem: pchanie skrzynki i przeciskanie przez tunel (wyciszenie przedsionkowe)",
        "glowna": "ułożenie drabiny ruchu przedsionkowego z pięciu szczebli i wykonanie dwóch najniższych na placu zabaw; ćwiczenie słowa „STOP” w zabawie — dorosły zatrzymuje się natychmiast, za każdym razem",
        "zakonczenie": "wybór szczebla na następne wyjście i schowanie karty STOP do kieszeni dziecka",
        "metody": ["stopniowanie trudności", "ćwiczenia proprioceptywne", "próba w warunkach naturalnych"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "sukcesem jest wejście na wybrany szczebel i skuteczne użycie STOP — nie wysokość sprzętu",
    },
    "arkusz": {
        "tytul": "DRABINA RUCHU PRZEDSIONKOWEGO — karta i STOP",
        "elementy": [
            "drabina 5 szczebli (A4) z obrazkami: stopy na ziemi → huśtanie z podparciem → 10 sekund → zjeżdżalnia z asekuracją → zjeżdżalnia sama",
            "karta „STOP” (9 × 9 cm), czerwona — 2 sztuki",
            "karta dla dorosłego: czego nie robimy (rozhuśtanie z zaskoczenia, wsadzanie na siłę)",
        ],
        "symbole": ["k_drabina_hustawka.jpg", "k_stop.jpg", "k_plac_zabaw.jpg"],
    },
    "ryzyko": "silny lęk przedsionkowy z wymiotami i bladością wymaga konsultacji neurologicznej i terapii SI — samo oswajanie może nie wystarczyć",
},
{
    "id": "SENS-20", "kod": "ROW-POD", "zmysl": "rownowaga", "sektor": "podwrazliwosc",
    "nazwa": "Zaplanowany ruch zamiast ciągłego bujania się i wstawania",
    "objawy": [
        "Jest w ciągłym ruchu — buja się na krześle, wstaje z miejsca co chwilę, kręci się w kółko",
        "Poszukuje intensywnego ruchu (huśtanie, wirowanie, skakanie) i nie ma zawrotów głowy",
        "Ryzykuje ruchowo ponad miarę — wspina się wysoko, skacze z wysokości",
    ],
    "opis_dla_doroslego": (
        "Dziecko potrzebuje mocnego bodźca przedsionkowego i dobiera go sobie w czasie zajęć — "
        "bujaniem na krześle, wstawaniem, wirowaniem. Brak zawrotów głowy przy wirowaniu to "
        "sygnał podwrażliwości, a wspinanie ponad miarę — realne ryzyko urazu."
    ),
    "strategia_sensoryczna": (
        "Dziecko korzysta z zaplanowanych dawek mocnego ruchu (skakanie, huśtanie, bieg z zadaniem) "
        "przed siedzeniem i w przerwach, a w czasie zajęć ma poduszkę sensoryczną, która pozwala "
        "się ruszać bez wstawania."
    ),
    "sygnal_dziecka": "karta „POTRZEBUJĘ RUCHU” wymieniana na 3 minuty ruchu w wyznaczonym miejscu",
    "kontekst": "podczas zajęć przy stoliku i w kręgu na dywanie",
    "czynnosc": {
        "3-4": "wykona z dorosłym 10 podskoków przed zajęciami i usiądzie na poduszce sensorycznej na czas piosenki",
        "5":   "poda kartę „POTRZEBUJĘ RUCHU”, wykona zaplanowaną dawkę ruchu i wróci na miejsce bez wstawania w trakcie zadania",
        "6":   "samo zaplanuje trzy dawki ruchu w ciągu dnia i wysiedzi zajęcia, korzystając z poduszki zamiast wstawać",
    },
    "wskaznik_obserwacji": "liczba zajęć, w których dziecko wstało z miejsca nie więcej niż raz, po skorzystaniu z dawki ruchu",
    "dieta_sensoryczna": [
        "dawka mocnego ruchu przed każdym zadaniem wymagającym siedzenia: 10 podskoków, bieg do drzwi i z powrotem, huśtanie 1 minuta",
        "poduszka sensoryczna na krześle i możliwość klęczenia lub stania przy stoliku",
        "zadania z ruchem wplecionym w treść (przynieś, podaj, zanieś) zamiast siedzenia bez przerwy",
    ],
    "dostosowania": [
        "miejsce przy brzegu, z drogą wyjścia bez przechodzenia przez środek dywanu",
        "krótsze bloki zadań (5–7 minut) z ruchem między nimi",
        "jasne zasady bezpieczeństwa na sprzęcie: dokąd wolno się wspinać, skąd nie wolno skakać",
    ],
    "pomoc": {
        "nazwa": "Poduszka sensoryczna + karta POTRZEBUJĘ RUCHU",
        "opis_dla_doroslego": (
            "Dmuchana poduszka sensoryczna na krzesło (pozwala na mikroruch bez wstawania) oraz karta "
            "wymiany na trzy minuty mocnego ruchu w wyznaczonym miejscu sali."
        ),
        "trzy_kroki_uzycia": [
            "Połóż poduszkę na krześle dziecka rano — to nie jest nagroda ani przywilej.",
            "Wpisz trzy dawki ruchu do planu dnia i realizuj je, zanim dziecko zacznie wstawać.",
            "Przyjmuj kartę bez oceny i zamykaj przerwę tym samym zdaniem.",
        ],
        "wskazowka_dla_doroslego": (
            "„Siedź spokojnie” jest poleceniem niewykonalnym przy podwrażliwości przedsionkowej. "
            "Wykonalne jest: „ruszaj się tutaj, a potem usiądź”."
        ),
        "etykieta_dla_dziecka": "POTRZEBUJĘ RUCHU",
        "polecenia": {
            "III": "Skaczemy dziesięć razy. Razem. Potem siadamy na poduszce.",
            "II":  "Podaj kartę i idź do znaku. Trzy minuty ruchu, potem stolik.",
            "I":   "Zaplanuj, kiedy dziś ruszasz się przed zadaniem.",
        },
    },
    "instrukcja_slowna": {
        "III": "Ciało chce ruchu. Skaczemy razem dziesięć razy, potem siadasz na poduszce.",
        "II":  "Masz kartę „POTRZEBUJĘ RUCHU”. Trzy minuty przy znaku i wracasz.",
        "I":   "Powiedz, kiedy robisz dziś swoje trzy dawki ruchu.",
    },
    "konspekt": {
        "temat": "Potrzebuję ruchu — dawka, którą mam zaplanowaną",
        "wprowadzenie": "„skacz, kręć się, zatrzymaj” — zabawa z sygnałem zatrzymania i sprawdzeniem, czy kręci się w głowie",
        "glowna": "ustalenie trzech dawek ruchu (podskoki, bieg z zadaniem, huśtanie) i wypróbowanie każdej przed krótkim zadaniem przy stoliku; porównanie: zadanie po ruchu i bez ruchu",
        "zakonczenie": "wpisanie dawek do planu dnia i położenie poduszki na krześle",
        "metody": ["zabawa ruchowa", "ćwiczenia porównawcze", "planowanie z dzieckiem"],
        "formy": "indywidualna, potem w grupie",
        "ewaluacja_uwaga": "notujemy liczbę wstań z miejsca w czasie zadania — porównanie z dniem bez dawek ruchu",
    },
    "arkusz": {
        "tytul": "POTRZEBUJĘ RUCHU — karta wymiany i plan dawek",
        "elementy": [
            "karta „POTRZEBUJĘ RUCHU” (9 × 9 cm) — 2 sztuki",
            "plan dnia z trzema polami na dawkę ruchu",
            "znak na podłogę wyznaczający miejsce ruchu w sali",
        ],
        "symbole": ["k_potrzebuje_ruchu.jpg", "k_poduszka.jpg", "k_skakanie.jpg"],
    },
    "ryzyko": "wspinanie się wysoko i skakanie z wysokości bez oceny ryzyka wymaga stałego nadzoru i ustalenia granic sprzętu — to najczęstsza przyczyna urazów w tej grupie",
},
{
    "id": "SENS-21", "kod": "ROW-SZUM", "zmysl": "rownowaga", "sektor": "bialy_szum",
    "nazwa": "Sprawdzenie poziomu ruchu przed wyjściem na plac zabaw",
    "objawy": [
        "Reakcje na ruch są niestałe — raz lęk przed huśtaniem, raz poszukiwanie intensywnego ruchu",
        "Aktywność ruchowa zmienia się skrajnie z dnia na dzień",
    ],
    "opis_dla_doroslego": (
        "Ten sam sprzęt bywa w poniedziałek atrakcją, a we wtorek źródłem lęku. Planowanie zajęć "
        "ruchowych pod stały profil kończy się albo przymusem, albo brakiem ruchu — obydwa "
        "warianty szkodzą."
    ),
    "strategia_sensoryczna": (
        "Dziecko przed wyjściem ustawia „licznik ruchu” (dużo ruchu / średnio / dziś spokojnie) "
        "i według niego wybiera sprzęt oraz dawkę — codziennie od nowa."
    ),
    "sygnal_dziecka": "przesunięcie suwaka na liczniku ruchu przed wyjściem",
    "kontekst": "przed wyjściem na plac zabaw i przed zajęciami ruchowymi w sali",
    "czynnosc": {
        "3-4": "z pomocą dorosłego ustawi suwak i wybierze jedną z dwóch zabaw",
        "5":   "samo ustawi licznik i wybierze sprzęt zgodny z ustawieniem",
        "6":   "ustawi licznik, wybierze sprzęt i powie, po czym poznało, że dziś ma inaczej niż wczoraj",
    },
    "wskaznik_obserwacji": "liczba wyjść poprzedzonych ustawieniem licznika i zgodnym z nim wyborem zabawy",
    "dieta_sensoryczna": [
        "praca oporowa przed każdym wyjściem — stabilizuje odczyt niezależnie od poziomu",
        "dwie gotowe ścieżki na placu: „dużo ruchu” i „dziś spokojnie”",
        "sprawdzenie licznika także po odpoczynku — poziom potrafi zmienić się w ciągu dnia",
    ],
    "dostosowania": [
        "brak stałego przypisania dziecku profilu ruchowego w dokumentacji",
        "sprzęt dobierany do ustawienia z danego dnia, nie do planu z poprzedniego tygodnia",
        "wpis poziomu do dziennika — po dwóch tygodniach widać rytm zmienności",
    ],
    "pomoc": {
        "nazwa": "Licznik ruchu — suwak z trzema poziomami",
        "opis_dla_doroslego": (
            "Pasek 10 × 30 cm z suwakiem i trzema polami: „dużo ruchu”, „średnio”, „dziś spokojnie”, "
            "przy każdym narysowany sprzęt lub zabawa, którą z niego wybieramy."
        ),
        "trzy_kroki_uzycia": [
            "Powieś licznik przy drzwiach do ogrodu, na wysokości dziecka.",
            "Poproś o ustawienie suwaka przed wyjściem i odczytaj wybór na głos.",
            "Zrealizuj ścieżkę zgodną z ustawieniem i zapisz poziom w dzienniku.",
        ],
        "wskazowka_dla_doroslego": (
            "„Wczoraj się huśtałeś, to dziś też dasz radę” jest zdaniem, które łamie zaufanie do "
            "licznika. Poziom zmienia się bez powodu — i to jest normalne w tym profilu."
        ),
        "etykieta_dla_dziecka": "MÓJ RUCH DZISIAJ",
        "polecenia": {
            "III": "Sprawdzamy ruch. Przesuwamy suwak razem.",
            "II":  "Ustaw suwak i wybierz zabawę.",
            "I":   "Ustaw licznik i powiedz, co dziś wybierasz.",
        },
    },
    "instrukcja_slowna": {
        "III": "Zanim wyjdziemy, sprawdzimy twój ruch. Trzymam pasek, ty przesuwasz suwak.",
        "II":  "Ustaw licznik ruchu i wybierz sprzęt, który przy nim narysowany.",
        "I":   "Ustaw licznik przed wyjściem i powiedz, co dziś robisz na placu.",
    },
    "konspekt": {
        "temat": "Mój ruch dzisiaj — sprawdzam, zanim wyjdę",
        "wprowadzenie": "rozmowa z obrazkami: „raz chcę się huśtać, raz nie” — dopasowanie buziek do sprzętu",
        "glowna": "wykonanie licznika ruchu z suwakiem i pierwsze ustawienie przed wyjściem; realizacja wybranej ścieżki na placu i porównanie z wczorajszą",
        "zakonczenie": "powieszenie licznika przy drzwiach do ogrodu i ustalenie pory sprawdzania",
        "metody": ["rozmowa kierowana", "praca techniczna", "próba w warunkach naturalnych"],
        "formy": "indywidualna",
        "ewaluacja_uwaga": "sukces = ustawienie licznika i zgodny z nim wybór; nie porównujemy poziomów między dniami",
    },
    "arkusz": {
        "tytul": "LICZNIK RUCHU — pasek z suwakiem",
        "elementy": [
            "pasek licznika 10 × 30 cm z trzema polami i rysunkami sprzętu",
            "suwak do wycięcia z prowadnicą",
            "2 karty ścieżek na placu zabaw („dużo ruchu”, „dziś spokojnie”)",
        ],
        "symbole": ["k_licznik_ruchu.jpg", "k_plac_zabaw.jpg", "k_spokojnie.jpg"],
    },
    "ryzyko": "skrajna zmienność aktywności ruchowej z sennością lub nadmiernym pobudzeniem wymaga konsultacji pediatrycznej — sprawdź sen, żelazo i tarczycę",
},
]

assert len(WSKAZNIKI) == 21, f"oczekiwano 21 wskaźników, jest {len(WSKAZNIKI)}"


# --- kryterium i horyzont dla druku SENS-T (z poziomu wsparcia) -------------
# W druku SENS-C kryterium i horyzont biorą się z PUNKTACJI zmysłu (tabela PROGI).
# W druku SENS-T — z POZIOMU WSPARCIA. To dwie różne drogi i nie wolno ich mylić.
# Na Poziomie I kryterium zostaje 4 z 5; rośnie trudność zachowania, nie liczba prób.
KRYTERIA_POZIOMOW = {
    "III": {"proba": "3 z 5",
            "horyzont": {"mianownik": "4 tygodnie", "dopelniacz": "4 tygodni", "miejscownik": "4 tygodniach"},
            "uzasadnienie": "krótki cykl, bo wsparcie jest wycofywane stopniowo i wymaga częstej weryfikacji"},
    "II":  {"proba": "4 z 5",
            "horyzont": {"mianownik": "6 tygodni", "dopelniacz": "6 tygodni", "miejscownik": "6 tygodniach"},
            "uzasadnienie": "dziecko wykonuje strategię samo, dorosły podaje sygnał — potrzeba więcej powtórzeń"},
    "I":   {"proba": "4 z 5",
            "horyzont": {"mianownik": "8 tygodni", "dopelniacz": "8 tygodni", "miejscownik": "8 tygodniach"},
            "uzasadnienie": "strategię inicjuje dziecko; kryterium zostaje 4 z 5, rośnie trudność samego zachowania"},
}

# Domyślne przypisanie do toru i rodzaju zajęć (nauczyciel może zmienić w druku).
DOMYSLNE_ZAJECIA = {
    "tor": "pomoc psychologiczno-pedagogiczna",
    "rodzaj": "zajęcia o charakterze terapeutycznym (terapia SI)",
}
