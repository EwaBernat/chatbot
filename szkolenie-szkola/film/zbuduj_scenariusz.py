# -*- coding: utf-8 -*-
"""Buduje src/scenariusz.json — plan scen filmu szkoleniowego dla szkoły podstawowej.

Narracja pochodzi wprost ze skryptu (`build_skrypt_szkola.py`), więc film mówi
dokładnie to, co stoi w druku dla nauczycieli. Tutaj dokładamy tylko warstwę
obrazu: jaki typ planszy, jakie hasła zakreślamy, którą tabelę pokazujemy.
"""

import ast, io, json, os, re, subprocess

KATALOG = os.path.dirname(os.path.abspath(__file__))
SKRYPT = os.path.join(KATALOG, '..', 'build_skrypt_szkola.py')
TEMPO_SLOW_NA_MIN = 107.0


def narracja_ze_skryptu():
    """Wyciąga akapity narracji z każdej funkcji czesc_N w skrypcie."""
    drzewo = ast.parse(io.open(SKRYPT, encoding='utf-8').read())
    moduly = {}
    for fn in drzewo.body:
        if not (isinstance(fn, ast.FunctionDef) and re.match(r'czesc_(\d+)$', fn.name)):
            continue
        numer = int(re.match(r'czesc_(\d+)$', fn.name).group(1))
        akapity = []
        for node in ast.walk(fn):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'narration':
                try:
                    wartosc = ast.literal_eval(node.args[1])
                except Exception:
                    continue
                if isinstance(wartosc, list):
                    akapity += wartosc
        moduly[numer] = [czysty(a) for a in akapity]
    return moduly


def czysty(tekst):
    """Zdejmuje znaczniki audytu [[...]] — w filmie nie ma niebieskiego druku."""
    return re.sub(r'\[\[(.*?)\]\]', r'\1', tekst, flags=re.S).strip()


def sekundy_z_tekstu(tekst):
    slowa = len(tekst.split())
    return round(slowa / TEMPO_SLOW_NA_MIN * 60.0 + 0.7, 2)


def dlugosc_mp3(sciezka):
    """Zmierzona długość nagrania — gdy plik już jest, on rządzi czasem sceny."""
    try:
        out = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', sciezka],
            capture_output=True, text=True, check=True)
        return round(float(out.stdout.strip()) + 0.45, 2)
    except Exception:
        return None


# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 1
# Format: (id ujęcia, indeksy akapitów narracji, scena)

PLAN_1 = [
 ('S1-01', [0], {
   'typ': 'czolowka',
   'tytul': 'Dokumentacja ucznia krok po kroku',
   'podtytul': 'Szkoła podstawowa · rok szkolny 2026/2027 · siedem części · EduPlaner 2026',
   'czesci': ['1 · Podstawa prawna', '2 · Dlaczego zmieniamy', '3 · Obieg dokumentów',
              '4 · Metryczka i teczka', '5 · KSzOF', '6 · Obserwacja pogłębiona', '7 · WOPF-SP, IPET, PWES'],
 }),
 ('S1-02', [1], {
   'typ': 'tytulModulu', 'numer': '1', 'czas': '10:40',
   'tytul': 'Podstawa prawna',
   'podtytul': 'Z czego wynika każdy dokument, który wypełniamy w szkole od 1 września 2026 roku?',
 }),
 ('S1-03', [2], {
   'typ': 'punkty', 'nadtytul': 'PYTANIE, KTÓRE PADA NAJCZĘŚCIEJ',
   'naglowek': 'Czy naprawdę musimy to zmieniać?',
   'punkty': [
     '**Nie zaczynamy od zera** — dotychczasowe arkusze, oceny i programy zostają ważnym źródłem danych o uczniu.',
     'Zmienia się **język, w którym opisujemy funkcjonowanie** ucznia.',
     'Zmienia się **sposób, w jaki jeden dokument zasila drugi**.',
   ],
 }),
 ('S1-04', [3], {
   'typ': 'sciezki', 'naglowek': 'Dwie ścieżki — jeden kwestionariusz obserwacji',
   'lewa': {'tytul': 'Kształcenie specjalne', 'kroki': [
     'Uczeń z orzeczeniem o potrzebie kształcenia specjalnego',
     'WOPFU — wielospecjalistyczna ocena poziomu funkcjonowania',
     'IPET — indywidualny program edukacyjno-terapeutyczny']},
   'prawa': {'tytul': 'Pomoc psychologiczno-pedagogiczna', 'kroki': [
     'Uczeń z opinią poradni albo rozpoznany przez nauczycieli',
     'PWES — plan wsparcia edukacyjno-specjalistycznego',
     'Ocena efektywności udzielanej pomocy']},
 }),
 ('S1-05', [4, 5], {
   'typ': 'cytat', 'naglowek': 'Akt pierwszy — ustawa',
   'tresc': 'System oświaty zapewnia **dostosowanie treści, metod i organizacji nauczania '
            'do możliwości psychofizycznych uczniów**. Nie o obniżaniu wymagań, lecz o drodze, '
            'którą uczeń do nich dochodzi.',
   'zrodlo': 'Prawo oświatowe — ustawa z 14 grudnia 2016 r., art. 1 pkt 5–7 · t.j. Dz.U. 2026 poz. 820',
 }),
 ('S1-06', [6], {
   'typ': 'punkty', 'nadtytul': 'PRAWO OŚWIATOWE · ART. 127',
   'naglowek': 'Kształcenie specjalne — skąd bierze się rozporządzenie',
   'punkty': [
     'Artykuł sto dwudziesty siódmy wprowadza kształcenie specjalne dla uczniów **posiadających orzeczenie** o potrzebie kształcenia specjalnego.',
     'Ustawa **odsyła do rozporządzenia** — i to ono jest dla nas najważniejsze.',
   ],
 }),
 ('S1-07', [7], {
   'typ': 'punkty', 'nadtytul': 'AKT DRUGI · KSZTAŁCENIE SPECJALNE',
   'naglowek': 'Rozporządzenie MEN z 9 sierpnia 2017 r.',
   'punkty': [
     'Warunki organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem.',
     'Obowiązujący tekst jednolity: **Dz.U. 2020 poz. 1309** — i tak cytujemy go w dokumentach ucznia.',
     'Pierwotny publikator, **poz. 1578, przestał być właściwym adresem**.',
   ],
 }),
 ('S1-08', [8], {
   'typ': 'tabela', 'nadtytul': 'T.J. DZ.U. 2020 POZ. 1309',
   'naglowek': 'Cztery obowiązki, które z niego wynikają',
   'naglowki': ['PRZEPIS', 'CO NAKŁADA'], 'szerokosci': [26, 74],
   'wiersze': [
     ['§ 5', 'Zajęcia rewalidacyjne dla ucznia z orzeczeniem'],
     ['§ 6 ust. 1', 'IPET i jego **osiem obowiązkowych elementów**'],
     ['§ 6 ust. 4', 'Program opracowujemy **po dokonaniu WOPFU**'],
     ['§ 6 ust. 9', 'Ocenę wykonujemy **co najmniej dwa razy w roku szkolnym**'],
   ],
 }),
 ('S1-09', [9], {
   'typ': 'cytat', 'naglowek': 'Nauczyciel współorganizujący — obowiązek czy zgoda',
   'tresc': 'Ustęp drugi: przy orzeczeniu wydanym ze względu na **autyzm, w tym zespół Aspergera**, '
            'albo **niepełnosprawności sprzężone** — zatrudnia się dodatkowo. To obowiązek, nie dobra wola. '
            'Ustęp trzeci: w pozostałych przypadkach **tylko za zgodą organu prowadzącego**.',
   'zrodlo': '§ 7 ust. 2 i 3 rozporządzenia MEN z 9 sierpnia 2017 r. · t.j. Dz.U. 2020 poz. 1309',
 }),
 ('S1-10', [10], {
   'typ': 'punkty', 'nadtytul': 'TERMINY PROGRAMU',
   'naglowek': 'Kiedy IPET musi być gotowy?',
   'punkty': [
     '**Do 30 września** — dla ucznia, który rozpoczyna kształcenie z orzeczeniem w danym roku szkolnym.',
     '**30 dni od złożenia orzeczenia** w szkole — niezależnie od miesiąca.',
     'Termin liczymy **od daty wpływu orzeczenia**, dlatego datę odnotowujemy w metryczce ucznia.',
   ],
 }),
 ('S1-11', [11, 12], {
   'typ': 'tabela', 'nadtytul': 'DWA AKTY, TA SAMA DATA: 9 SIERPNIA 2017 R.',
   'naglowek': 'Najczęstsza pomyłka w podstawie prawnej',
   'naglowki': ['ZAKRES', 'OBOWIĄZUJĄCY TEKST JEDNOLITY'], 'szerokosci': [52, 48],
   'wiersze': [
     ['Kształcenie specjalne', '**Dz.U. 2020 poz. 1309**'],
     ['Pomoc psychologiczno-pedagogiczna', '**Dz.U. 2023 poz. 1798**'],
   ],
 }),
 ('S1-12', [13], {
   'typ': 'tabela', 'nadtytul': 'W SZKOLE KATALOG JEST SZERSZY NIŻ W PRZEDSZKOLU',
   'naglowek': 'Formy pomocy psychologiczno-pedagogicznej',
   'naglowki': ['', ''], 'szerokosci': [50, 50],
   'wiersze': [
     ['Zajęcia dydaktyczno-wyrównawcze', 'Zajęcia logopedyczne'],
     ['Zajęcia korekcyjno-kompensacyjne', 'Zajęcia związane z wyborem kierunku kształcenia i zawodu'],
     ['Zajęcia rozwijające umiejętności uczenia się', 'Porady, konsultacje i warsztaty'],
     ['Zajęcia rozwijające kompetencje emocjonalno-społeczne', '**Zindywidualizowana ścieżka kształcenia** (§ 12)'],
   ],
 }),
 ('S1-13', [14], {
   'typ': 'tabela', 'nadtytul': 'DWIE INSTYTUCJE, KTÓRE SIĘ MYLĄ',
   'naglowek': 'Ścieżka kształcenia a nauczanie indywidualne',
   'naglowki': ['ZINDYWIDUALIZOWANA ŚCIEŻKA', 'NAUCZANIE INDYWIDUALNE'], 'szerokosci': [50, 50],
   'wiersze': [
     ['Część zajęć z klasą, część indywidualnie', 'Wszystkie zajęcia indywidualnie'],
     ['**Opinia** publicznej poradni', '**Orzeczenie** o potrzebie indywidualnego nauczania'],
     ['Wniosek składają rodzice', 'Osobne rozporządzenie — Dz.U. 2017 poz. 1616'],
     ['**Nie stosujemy** przy kształceniu specjalnym', 'Inna instytucja prawna — nie mylimy pojęć'],
   ],
 }),
 ('S1-14', [15, 16], {
   'typ': 'punkty', 'nadtytul': 'AKT TRZECI — W TYM ROKU NAJWAŻNIEJSZY',
   'naglowek': 'Orzeczenia i opinie zespołów orzekających',
   'punkty': [
     'Rozporządzenie Ministra Edukacji z **2 marca 2026 r.** · **Dz.U. 2026 poz. 428**.',
     'Przepisy dotyczące bezpośrednio szkoły — **§ 7 ust. 6 i 7 oraz § 8** — obowiązują **od 1 września 2026 r.**',
     'To ten akt **zmienia sposób, w jaki opisujemy ucznia**.',
   ],
 }),
 ('S1-15', [17], {
   'typ': 'punkty', 'nadtytul': 'CO TO OZNACZA DLA SZKOŁY?',
   'naglowek': 'Dwie zmiany, które nas dotyczą',
   'punkty': [
     '**Ocena funkcjonalna** ucznia staje się obowiązkowym etapem **poprzedzającym wydanie orzeczenia**.',
     'Szkoła — na prośbę przewodniczącego zespołu orzekającego — **wydaje opinię o funkcjonowaniu ucznia**.',
     'Opinia opisuje trudności, ale **równie starannie mocne strony i uzdolnienia** rozpoznane przez nauczycieli.',
   ],
 }),
 ('S1-16', [18], {
   'typ': 'cytat', 'naglowek': 'Termin, który zmienia rytm pracy szkoły',
   'tresc': 'Opinię, o której mowa w ustępie drugim, wydaje się w terminie **dziesięciu dni '
            'od dnia otrzymania przez dyrektora prośby o jej wydanie**. Kopię opinii otrzymują rodzice ucznia.',
   'zrodlo': '§ 7 ust. 3 rozporządzenia ME z 2 marca 2026 r. · Dz.U. 2026 poz. 428',
 }),
 ('S1-17', [19], {
   'typ': 'sciezki', 'naglowek': 'Podział ról — jasny i wygodny',
   'lewa': {'tytul': 'Poradnia', 'kroki': [
     'Sporządza formalną ocenę funkcjonalną', 'Prowadzi zespół orzekający', 'Wydaje orzeczenie albo opinię']},
   'prawa': {'tytul': 'Szkoła', 'kroki': [
     'Obserwuje ucznia na lekcjach, przerwach i w świetlicy',
     'Opisuje to, co widzi — nie stawia diagnoz',
     'Dostarcza rzetelnych, uporządkowanych danych']},
 }),
 ('S1-18', [20], {
   'typ': 'punkty', 'nadtytul': 'SEDNO CAŁEGO SZKOLENIA',
   'naglowek': 'Dlaczego wrzesień, a nie kwiecień?',
   'punkty': [
     'Dziesięć dni to bardzo mało, jeśli obserwację **zaczynamy dopiero po wpłynięciu prośby**.',
     'Ucznia klasy szóstej uczy **dziewięcioro nauczycieli** i żaden nie widzi go przez cały dzień.',
     'Kwestionariusz wypełniamy **we wrześniu** — nie po to, żeby leżał w segregatorze.',
     'Po to, żeby w dowolnym dniu roku odpowiedzieć poradni **na podstawie danych, spokojnie i na czas**.',
   ],
 }),
 ('S1-19', [21, 22], {
   'typ': 'punkty', 'nadtytul': 'AKT CZWARTY · DOKUMENTACJA PRZEBIEGU NAUCZANIA',
   'naglowek': 'Gdzie mieszczą się nasze arkusze obserwacji?',
   'punkty': [
     'Rozporządzenie z **25 sierpnia 2017 r.** wymienia księgę uczniów, dziennik lekcyjny, dzienniki zajęć i arkusze ocen.',
     'Wymienia też **dokumentację badań i czynności uzupełniających** prowadzonych przez nauczycieli i specjalistów.',
     'W tej kategorii mieszczą się **arkusze obserwacji, karty ABC i profile sensoryczne** — to jest ich podstawa prawna.',
   ],
 }),
 ('S1-20', [23], {
   'typ': 'druk', 'nadtytul': 'EDUPLANER 2026 · TRYB SZKOŁY PODSTAWOWEJ',
   'naglowek': 'Metryczka ucznia — narzędzie wewnętrzne szkoły',
   'plik': 'druki/szkolap_metryczka.png',
   'opis': 'Moduł Metryczka · zgłoszenie i dane wejściowe — wprowadzamy ją zarządzeniem dyrektora',
 }),
 ('S1-21', [24, 25], {
   'typ': 'punkty', 'nadtytul': 'AKT PIĄTY · OCENIANIE — PRZEPIS CZYSTO SZKOLNY',
   'naglowek': 'Na jakiej podstawie dostosowujemy wymagania?',
   'punkty': [
     'Uczeń z orzeczeniem → podstawą jest **orzeczenie i program**.',
     'Uczeń z opinią poradni → podstawą jest **opinia**.',
     'Uczeń objęty pomocą bez opinii → **rozpoznanie nauczycieli zapisane w dokumentacji**.',
     '**Rozmowa w pokoju nauczycielskim nie jest podstawą.**',
   ],
 }),
 ('S1-22', [26], {
   'typ': 'cytat', 'naglowek': 'Ocena zachowania ucznia z orzeczeniem lub opinią',
   'tresc': 'Przy ustalaniu oceny zachowania **uwzględnia się wpływ stwierdzonych zaburzeń '
            'lub zaburzeń rozwojowych na zachowanie ucznia**. To zdanie ratuje wielu uczniów '
            'przed oceną naganną **za objaw**.',
   'zrodlo': 'Rozporządzenie MEN z 22 lutego 2019 r. · t.j. Dz.U. 2023 poz. 2572, z późn. zm.',
 }),
 ('S1-23', [27], {
   'typ': 'tabela', 'nadtytul': 'PODSTAWA PROGRAMOWA WCHODZI ETAPAMI',
   'naglowek': 'Którą podstawę wpisujemy w programie ucznia?',
   'naglowki': ['KOGO DOTYCZY', 'KTÓRA PODSTAWA OD 1.09.2026'], 'szerokosci': [52, 48],
   'wiersze': [
     ['Klasy I i IV', 'Nowa — **Dz.U. 2026 poz. 378**'],
     ['Uczniowie z n. intelektualną w stopniu umiarkowanym lub znacznym', 'Nowa — **w całej szkole podstawowej**'],
     ['Pozostałe klasy, w tym klasa III', 'Dotychczasowa — **Dz.U. 2017 poz. 356**'],
   ],
 }),
 ('S1-24', [28], {
   'typ': 'punkty', 'nadtytul': 'OBSZAR SZÓSTY · EGZAMIN ÓSMOKLASISTY',
   'naglowek': 'Dostosowanie warunków i form egzaminu',
   'punkty': [
     'Przysługuje na podstawie **orzeczenia, opinii poradni** albo pozytywnej **opinii rady pedagogicznej**.',
     'Szczegółowe sposoby ogłasza corocznie **komunikat dyrektora CKE** — sprawdzamy komunikat na dany rok.',
     '**Dostosowanie, którego nie ma w dokumentacji w listopadzie, nie pojawi się na egzaminie w maju.**',
   ],
 }),
 ('S1-25', [29], {
   'typ': 'punkty', 'nadtytul': 'TRZY AKTY, KTÓRE STOJĄ NAD WSZYSTKIMI',
   'naglowek': 'Dostępność, finansowanie, ochrona danych',
   'punkty': [
     'Ustawa o zapewnianiu **dostępności** osobom ze szczególnymi potrzebami.',
     'Ustawa o **finansowaniu zadań oświatowych** — art. 8 ust. 1 adresuje obowiązek do **organu prowadzącego**, nie do szkoły.',
     'To dokumentacja ucznia pokazuje, **jakie zadania szkoła faktycznie realizuje**.',
     'RODO — dane o zdrowiu i rozwoju ucznia to **dane szczególnej kategorii**.',
   ],
 }),
 ('S1-26', [30], {
   'typ': 'punkty', 'nadtytul': 'FUNKCJA, KTÓRA PILNUJE CAŁOŚCI',
   'naglowek': 'Strażnik Prawa',
   'punkty': [
     'To **nie** jest osoba, która zna przepisy na pamięć.',
     'To osoba, która przy każdej decyzji pyta: **z czego to wynika i gdzie to jest zapisane?**',
     'Funkcja jest **rotacyjna** — pełni ją w ciągu roku każdy członek zespołu.',
   ],
 }),
 ('S1-27', [31, 32], {
   'typ': 'domkniecie', 'naglowek': 'Trzy zdania na koniec części pierwszej',
   'zdania': [
     'Każdy druk ma swój przepis, i **my go znamy**.',
     'Obserwacja **wyprzedza pismo z poradni** — wrześniowy arkusz daje nam spokój na cały rok.',
     'Przepisy sprawdzamy **w Dzienniku Ustaw**, zanim wpiszemy je do dokumentu ucznia.',
   ],
 }),
]


# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 3

PLAN_3 = [
 ('S3-01', [0, 1], {
   'typ': 'tytulModulu', 'numer': '3', 'czas': '6:10',
   'tytul': 'Obieg dokumentów w szkole',
   'podtytul': 'Jakie dokumenty tworzymy w ciągu roku, w jakiej kolejności powstają '
               'i dlaczego żaden z nich nie powstaje osobno.',
 }),
 ('S3-02', [2], {
   'typ': 'domkniecie', 'naglowek': 'Najważniejsze zdanie tego szkolenia',
   'zdania': [
     'Dokumentacja ucznia to **jeden obieg**, w którym każdy dokument bierze dane z poprzedniego.',
     'Pominiemy etap — następny trzeba wypełniać **z pamięci**.',
     'A dokumentacja wypełniana z pamięci **nie służy ani uczniowi, ani nam**.',
   ],
 }),
 ('S3-03', [3, 4], {
   'typ': 'obieg', 'naglowek': 'Siedem przystanków i jedno rozgałęzienie',
   'przystanki': [
     {'nazwa': 'Metryczka i teczka', 'opis': 'Kto, od kiedy, z jakim dokumentem'},
     {'nazwa': 'KSzOF', 'opis': 'Przesiew całego oddziału — gdzie?'},
     {'nazwa': 'Obserwacja pogłębiona', 'opis': 'Cztery narzędzia — dlaczego?'},
     {'nazwa': 'WOPF-SP', 'opis': 'Scalenie wszystkiego, co zebraliśmy'},
     {'nazwa': 'IPET albo PWES', 'opis': 'Rozgałęzienie ścieżek'},
     {'nazwa': 'Ewaluacja', 'opis': 'Wskaźnik zapisany wcześniej'},
     {'nazwa': 'Przejście i egzamin', 'opis': 'Czerwiec kl. III, listopad kl. VIII'},
   ],
 }),
 ('S3-04', [5], {
   'typ': 'punkty', 'nadtytul': 'PRZYSTANEK PIERWSZY',
   'naglowek': 'Metryczka ucznia — co przekazuje dalej',
   'punkty': [
     'Czy uczeń **posiada orzeczenie, opinię lub inną formę wsparcia — i od kiedy**?',
     '**Data wpływu orzeczenia** uruchamia trzydziestodniowy termin na program.',
     'Sygnały zdrowotne: nadwrażliwość sensoryczna, choroba przewlekła — **wrócą przy decyzji o obserwacji**.',
   ],
 }),
 ('S3-05', [6, 7], {
   'typ': 'punkty', 'nadtytul': 'PRZYSTANEK DRUGI · KSZOF',
   'naglowek': 'Kwestionariusz Szkolnej Oceny Funkcjonalnej',
   'punkty': [
     'Narzędzie **przesiewowe** — obejmuje **wszystkich uczniów w oddziale**, nie tylko tych, którzy budzą niepokój.',
     'Wypełniają niezależnie **wychowawca i rodzic**, w drugim etapie także nauczyciel przedmiotu i specjalista.',
     'Wynik: profil w **dziewięciu obszarach**, wynik ogólny **w stenach**, lista zachowań do omówienia.',
     'Kwestionariusz odpowiada na pytanie: **gdzie?**',
   ],
 }),
 ('S3-06', [8, 9], {
   'typ': 'tabela', 'nadtytul': 'PRZYSTANEK TRZECI · URUCHAMIANY WARUNKOWO',
   'naglowek': 'Obserwacja pogłębiona — cztery narzędzia',
   'naglowki': ['NARZĘDZIE', 'NA CO ODPOWIADA'], 'szerokosci': [46, 54],
   'wiersze': [
     ['Model ABC + analiza funkcjonalna', 'Co poprzedza zachowanie i co je utrzymuje?'],
     ['Profil sensoryczny', 'Co w otoczeniu przeciąża, a co reguluje?'],
     ['Karta rozwoju mowy i komunikacji', 'Jak uczeń rozumie i jak się porozumiewa?'],
     ['Poznanie społeczne i teoria umysłu', 'Jak czyta intencje innych?'],
   ],
 }),
 ('S3-07', [10], {
   'typ': 'druk', 'nadtytul': 'EDUPLANER 2026 · MODUŁ WOPF',
   'naglowek': 'Narzędzia obserwacji w aplikacji',
   'plik': 'druki/szkolap_wopf.png',
   'opis': 'Menu modułu WOPF w trybie szkoły podstawowej — kolejność druków odpowiada obiegowi',
 }),
 ('S3-08', [11], {
   'typ': 'punkty', 'nadtytul': 'PRZYSTANEK CZWARTY · WOPF-SP',
   'naglowek': 'Ocena scala wszystko, co zebraliśmy',
   'punkty': [
     'Profil z kwestionariusza, wnioski z obserwacji pogłębionej, treść orzeczenia lub opinii.',
     'Informacje od rodziców, **głos ucznia**, efekty dotychczasowego wsparcia.',
     'Piszemy **językiem funkcjonalnym**: co uczeń robi, w jakich warunkach i przy jakim wsparciu.',
     'Opisujemy mocne strony, trudności oraz **bariery i ułatwienia w środowisku**.',
   ],
 }),
 ('S3-09', [12], {
   'typ': 'sciezki', 'naglowek': 'Rozgałęzienie — sekcja I a druku oceny',
   'lewa': {'tytul': 'Uczeń z orzeczeniem', 'kroki': [
     'Orzeczenie o potrzebie kształcenia specjalnego',
     'Indywidualny program edukacyjno-terapeutyczny',
     'Podstawa: rozporządzenie o kształceniu specjalnym']},
   'prawa': {'tytul': 'Uczeń bez orzeczenia', 'kroki': [
     'Opinia poradni albo rozpoznanie nauczycieli',
     'Plan wsparcia edukacyjno-specjalistycznego',
     'Podstawa: rozporządzenie o pomocy p-p']},
 }),
 ('S3-10', [13, 14], {
   'typ': 'punkty', 'nadtytul': 'PRZYSTANEK PIĄTY · ŚCIEŻKA PIERWSZA',
   'naglowek': 'IPET wynika z oceny zdanie po zdaniu',
   'punkty': [
     '**Czego nie ma w ocenie, nie może pojawić się w programie.**',
     'Zalecenia z orzeczenia **wraz ze sposobem realizacji**.',
     'Cele **w postaci mierzalnej** i dostosowania zapisane **przedmiotowo**.',
     'Zintegrowane działania, formy i wymiar wsparcia, współpraca z rodzicami.',
   ],
 }),
 ('S3-11', [15], {
   'typ': 'punkty', 'nadtytul': 'PRZYSTANEK PIĄTY · ŚCIEŻKA DRUGA',
   'naglowek': 'Plan wsparcia edukacyjnego ucznia',
   'punkty': [
     'Powstaje dla ucznia **z opinią poradni albo rozpoznanego przez nauczycieli**.',
     'Ta sama logika: potrzeba → cel z kryterium → forma pomocy → osoba → wymiar → termin oceny.',
     'Różni się **podstawą prawną** i tym, że **nie wymaga orzeczenia**.',
   ],
 }),
 ('S3-12', [16, 17], {
   'typ': 'tabela', 'nadtytul': 'PRZYSTANEK SZÓSTY · EWALUACJA',
   'naglowek': 'Cztery decyzje po pomiarze',
   'naglowki': ['DECYZJA', 'KIEDY'], 'szerokosci': [34, 66],
   'wiersze': [
     ['Zamykamy cel', 'Wskaźnik osiągnięty i utrzymany'],
     ['Kontynuujemy', 'Postęp jest, ale kryterium jeszcze nie spełnione'],
     ['Modyfikujemy', 'Postępu brak — zmieniamy formę, wymiar albo cel'],
     ['Rozmowa i poradnia', 'Spotkanie z rodzicami, rozważenie wystąpienia do poradni'],
   ],
 }),
 ('S3-13', [18], {
   'typ': 'punkty', 'nadtytul': 'PRZYSTANEK SIÓDMY · SEZONOWY, CZYSTO SZKOLNY',
   'naglowek': 'Dokumenty przejścia i egzaminu',
   'punkty': [
     '**Czerwiec klasy trzeciej** — karta przekazania informacji o uczniu do drugiego etapu edukacyjnego.',
     '**Listopad klasy ósmej** — karta dostosowań warunków egzaminu ósmoklasisty.',
     'Obie powstają **z dokumentacji, którą już mamy** — nie piszemy ich od zera.',
   ],
 }),
 ('S3-14', [19, 20], {
   'typ': 'tabela', 'nadtytul': 'OPINIA DLA PORADNI · DZIESIĘĆ DNI',
   'naglowek': 'Nie piszemy jej od zera — składamy z tego, co mamy',
   'naglowki': ['CZĘŚĆ OPINII', 'SKĄD JĄ BIERZEMY'], 'szerokosci': [42, 58],
   'wiersze': [
     ['Mocne strony', 'Kwestionariusz KSzOF'],
     ['Opis trudności', 'Obserwacja pogłębiona'],
     ['Efekty wsparcia', 'Karta ewaluacji'],
     ['Współpraca z rodzicami', 'Rejestr kontaktów w metryczce'],
   ],
 }),
 ('S3-15', [21], {
   'typ': 'domkniecie', 'naglowek': 'Porządek, w którym omówimy każdy druk',
   'zdania': [
     'Siedem przystanków: metryczka, kwestionariusz, obserwacja, ocena, program albo plan, ewaluacja, przejście.',
     'Najpierw **po co dokument powstaje**. Potem **jak go stworzyć**. Na końcu **jak go wypełnić** — na Państwa drukach.',
     'Zapraszam do modułu czwartego.',
   ],
 }),
]



# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 4

PLAN_4 = [
 ('S4-01', [0, 1], {
   'typ': 'tytulModulu', 'numer': '4', 'czas': '6:30',
   'tytul': 'Metryczka i teczka ucznia',
   'podtytul': 'Pierwszy dokument września — po co go prowadzimy, jak wypełnić bez danych '
               'nadmiarowych i co odczytać z niego w kilkanaście sekund.',
 }),
 ('S4-02', [2], {
   'typ': 'punkty', 'nadtytul': 'CZYM JEST METRYCZKA?',
   'naglowek': 'Karta danych, które i tak musimy posiadać',
   'punkty': [
     'Dane identyfikacyjne **w zakresie minimalnym**, kontakty do rodziców, zdrowie istotne dla funkcjonowania w szkole.',
     'Podstawa objęcia wsparciem oraz **spis dokumentacji ucznia**.',
     'Narzędzie **wewnętrzne**, wprowadzone zarządzeniem dyrektora — żeby **oszczędzać czas i chronić ucznia**.',
   ],
 }),
 ('S4-03', [3, 4, 5], {
   'typ': 'punkty', 'nadtytul': 'ZASADNOŚĆ · PUNKTY 1–2',
   'naglowek': 'Jedno miejsce zamiast siedmiu',
   'punkty': [
     'Nauczyciel na zastępstwie **nie szuka po segregatorach** telefonu do rodzica ani informacji o alergii — otwiera jedną kartę.',
     'Kontakt w nagłych wypadkach, choroby przewlekłe, leki, dieta, procedura postępowania.',
     'Metryczka jest dokumentem **operacyjnym, a nie archiwalnym**.',
   ],
 }),
 ('S4-04', [6, 7, 8], {
   'typ': 'punkty', 'nadtytul': 'ZASADNOŚĆ · PUNKTY 3–5',
   'naglowek': 'Wsparcie, współpraca, ochrona danych',
   'punkty': [
     '**Data wpływu orzeczenia** uruchamia trzydziestodniowy termin — to **jedyne miejsce**, w którym jest zapisana.',
     'Rejestr kontaktów potwierdza, że szkoła informowała i ustalała. **Bez rejestru w sporze mamy tylko wspomnienia.**',
     'Klauzula informacyjna jest częścią dokumentu, a zakres danych **ograniczamy do niezbędnego**.',
   ],
 }),
 ('S4-05', [9, 10], {
   'typ': 'punkty', 'nadtytul': 'SEKCJA I · PRZYKŁAD: ZOFIA LEWANDOWSKA, KL. III A',
   'naglowek': 'Dane ucznia w zakresie minimalnym',
   'punkty': [
     'Imię i nazwisko, klasa, etap edukacyjny, rok szkolny, wychowawca.',
     '**Numeru PESEL nie wpisujemy** — jest w księdze uczniów, nie powielamy go w kolejnym dokumencie.',
     'Nie wpisujemy też **adresu zamieszkania, miejsca urodzenia ani miejsca pracy rodziców** — to najczęstszy nadmiar w szkolnych drukach.',
   ],
 }),
 ('S4-06', [11], {
   'typ': 'cytat', 'naglowek': 'Sekcja II — podstawa objęcia wsparciem',
   'tresc': 'Przy każdej formie wsparcia wpisujemy **numer i datę dokumentu**, a nie samo zaznaczenie. '
            'Obok — pole, o którym najczęściej się zapomina — **data wpływu orzeczenia do szkoły**. '
            'To od niej liczymy trzydzieści dni.',
   'zrodlo': 'Przykład: orzeczenie PPP.4223.18.2026 z 12 czerwca 2026 r. · poradnia w Koszalinie · niepełnosprawność sprzężona',
 }),
 ('S4-07', [12], {
   'typ': 'sciezki', 'naglowek': 'Sekcja III — wybór ścieżki wsparcia',
   'lewa': {'tytul': 'Kształcenie specjalne', 'kroki': [
     'Uczeń ma orzeczenie', 'Prowadzi do IPET', 'Zespół pracuje na programie']},
   'prawa': {'tytul': 'Pomoc psychologiczno-pedagogiczna', 'kroki': [
     'Opinia albo rozpoznanie nauczycieli', 'Prowadzi do planu wsparcia', 'Zespół pracuje na planie']},
 }),
 ('S4-08', [13], {
   'typ': 'punkty', 'nadtytul': 'SEKCJA IV · KONTAKTY',
   'naglowek': 'Pole, którego nie ma w przedszkolu',
   'punkty': [
     'Rodzice, preferowana forma kontaktu, **kolejność powiadamiania** w nagłych wypadkach.',
     'W szkole dochodzi **sposób powrotu ucznia do domu** i ewentualne upoważnienia, jeśli uczeń nie wraca samodzielnie.',
   ],
 }),
 ('S4-09', [14], {
   'typ': 'punkty', 'nadtytul': 'SEKCJA V · ZDROWIE I FUNKCJONOWANIE',
   'naglowek': 'Tutaj zatrzymujemy się dłużej',
   'punkty': [
     'Choroby przewlekłe i ostrzeżenia — astma, padaczka, cukrzyca — oraz przyjmowane leki.',
     'W zaleceniach zapisujemy konkretnie: **kto podaje lek, na jakiej podstawie, gdzie jest przechowywany, kogo powiadamiamy**.',
     'Zaznaczamy sygnały uruchamiające obserwację pogłębioną — na przykład **nadwrażliwość sensoryczną**.',
   ],
 }),
 ('S4-10', [15], {
   'typ': 'domkniecie', 'naglowek': 'Granica, której nie przekraczamy',
   'zdania': [
     '**Nie kopiujemy do metryczki dokumentacji medycznej.**',
     'Wpisujemy wyłącznie tę informację, która jest niezbędna do organizacji kształcenia i bezpieczeństwa.',
     'Zaświadczenie lekarskie zostaje **w teczce**, a nie w treści druku.',
   ],
 }),
 ('S4-11', [16, 17], {
   'typ': 'tabela', 'nadtytul': 'SEKCJE VI–VIII',
   'naglowek': 'Trzy sekcje, które pracują przez cały rok',
   'naglowki': ['SEKCJA', 'CO DAJE'], 'szerokosci': [40, 60],
   'wiersze': [
     ['VI · Źródła informacji (audyt)', 'Pokazuje, **czego nie musimy zbierać po raz drugi**'],
     ['VII · Rejestr kontaktów', 'Zasili **opinię dla poradni**; dowód w sytuacji spornej'],
     ['VIII · Wykaz dokumentacji', 'Spis zawartości teczki z datami — **co jest i czego brakuje**'],
   ],
 }),
 ('S4-12', [18], {
   'typ': 'druk', 'nadtytul': 'EDUPLANER 2026 · MODUŁ METRYCZKA',
   'naglowek': 'Metryczka i teczka w aplikacji',
   'plik': 'druki/szkolap_metryczka.png',
   'opis': 'Zgłoszenie i dane wejściowe — stąd dane wędrują do wszystkich kolejnych druków',
 }),
 ('S4-13', [19, 20], {
   'typ': 'punkty', 'nadtytul': 'TRZY DOBRE PRAKTYKI',
   'naglowek': 'Czego pilnujemy przez cały rok?',
   'punkty': [
     'Zbieramy **tylko te dane, które są potrzebne** do realizacji zadań szkoły.',
     'Aktualizujemy metryczkę **przy każdej zmianie zgłoszonej przez rodzica, z datą**.',
     'Przechowujemy ją w miejscu wskazanym zarządzeniem — zawiera **dane szczególnej kategorii**.',
   ],
 }),
 ('S4-14', [21], {
   'typ': 'domkniecie', 'naglowek': 'Metryczka jest gotowa, gdy odpowiada na trzy pytania',
   'zdania': ['**Kogo wezwać?**', '**Co podać?**', '**Od kiedy liczyć termin?**'],
 }),
]



# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 2

PLAN_2 = [
 ('S2-01', [0, 1], {
   'typ': 'tytulModulu', 'numer': '2', 'czas': '12:20',
   'tytul': 'Dlaczego szkoła musi zmienić dokumentację?',
   'podtytul': 'Prowadzimy dokumentację od lat, kuratorium nigdy nic nie zarzuciło. '
               'Po co to zmieniać? Pytanie zasługuje na uczciwą odpowiedź.',
 }),
 ('S2-02', [2], {
   'typ': 'punkty', 'nadtytul': 'ZACZNĘ OD TEGO, CZEGO NIE POWIEM',
   'naglowek': 'Trzy zdania, które nie padną',
   'punkty': [
     'Nie powiem, że dotychczasowa dokumentacja **była zła**.',
     'Nie powiem, że **pracowaliśmy źle**.',
     'Nie poproszę nikogo, żeby **przepisywał dokumenty, które już powstały**.',
   ],
 }),
 ('S2-03', [3], {
   'typ': 'domkniecie', 'naglowek': 'Co się naprawdę zmienia?',
   'zdania': [
     'Zmienia się **nie objętość dokumentacji, lecz jej język i jej funkcja**.',
     'Dokument napisany w starym języku **przestaje działać w nowym obiegu**.',
     'Nie dlatego, że jest brzydki — dlatego, że **nie da się z niego wyjąć informacji, o którą pyta poradnia**.',
   ],
 }),
 ('S2-04', [4], {
   'typ': 'cytat', 'naglowek': 'Zdanie z setek szkolnych ocen',
   'tresc': 'Uczennica ma trudności w koncentracji uwagi wynikające z zaburzeń rozwojowych, '
            '**wymaga stałej pomocy nauczyciela**.',
   'zrodlo': 'Typowy zapis w ocenie wielospecjalistycznej — sprawdźmy, na co odpowiada',
 }),
 ('S2-05', [5, 6], {
   'typ': 'punkty', 'nadtytul': 'PYTANIA, KTÓRE ZADA ZESPÓŁ ORZEKAJĄCY',
   'naglowek': 'Na żadne z nich to zdanie nie odpowiada',
   'punkty': [
     'W jakich sytuacjach uczennica **traci uwagę**, a w jakich ją **utrzymuje**?',
     'Jak długo pracuje bez podpowiedzi **przy karcie pracy**, a jak długo **przy tablicy**?',
     'Co dokładnie znaczy **stała pomoc** — obecność dorosłego, podpowiedź słowna, wspólne wykonanie? Ile razy dziennie?',
     'Nie dlatego, że nauczycielka nie wie. **Ona wie doskonale.** Druk nie miał miejsca na tę wiedzę.',
   ],
 }),
 ('S2-06', [7], {
   'typ': 'cytat', 'naglowek': 'To samo — w języku funkcjonalnym',
   'tresc': 'Zofia pracuje samodzielnie przy karcie pracy przez **około osiem minut**, jeśli siedzi '
            'w pierwszej ławce, a zadanie jest podzielone na trzy kroki z piktogramami. Przy pracy '
            'z tablicą utrzymuje uwagę **około dwóch minut** i wymaga podpowiedzi **średnio cztery razy '
            'na lekcji**. W hałasie czas skraca się **do minuty**. Od września liczba podpowiedzi spadła '
            'z sześciu do czterech.',
   'zrodlo': 'Ta sama uczennica, ta sama wiedza tej samej nauczycielki — inny zapis',
 }),
 ('S2-07', [8], {
   'typ': 'tabela', 'nadtytul': 'NA CZYM POLEGA RÓŻNICA',
   'naglowek': 'Cztery pytania języka funkcjonalnego',
   'naglowki': ['PYTANIE', 'W PRZYKŁADZIE'], 'szerokosci': [34, 66],
   'wiersze': [
     ['Co uczeń robi?', 'Pracuje samodzielnie przy karcie pracy'],
     ['W jakich warunkach?', 'Pierwsza ławka, cicha sala, zadanie w trzech krokach'],
     ['Przy jakim wsparciu?', 'Podpowiedź słowna, piktogramy'],
     ['Jak często?', 'Osiem minut · cztery podpowiedzi na lekcji'],
   ],
 }),
 ('S2-08', [9, 10], {
   'typ': 'punkty', 'nadtytul': 'POWÓD PIERWSZY Z DZIESIĘCIU',
   'naglowek': 'Zmienił się adresat naszej dokumentacji',
   'punkty': [
     'Do tej pory pisaliśmy ją **głównie dla siebie i dla kontroli**.',
     'Od 1 września poradnia opiera orzeczenie **na ocenie funkcjonalnej**, a opis ma odnosić się do **aktywności i uczestniczenia w rozumieniu ICF**.',
     'Jeżeli mówimy innym językiem, **poradnia naszej dokumentacji po prostu nie użyje**.',
     'Orzeczenie powstanie **bez danych od jedynych dorosłych, którzy widzą ucznia codziennie**.',
   ],
 }),
 ('S2-09', [11], {
   'typ': 'punkty', 'nadtytul': 'POWÓD DRUGI · TERMIN DZIESIĘCIU DNI',
   'naglowek': 'Wykonalny tylko wtedy, gdy dane już istnieją',
   'punkty': [
     'Ucznia klasy siódmej uczy nawet **dwanaścioro nauczycieli**.',
     'Zebranie od nich informacji, uzgodnienie i napisanie opinii **w dziesięć dni** wymaga danych, które już są.',
     'Inaczej opinia powstanie **z pamięci albo po terminie**. Obie możliwości są złe.',
   ],
 }),
 ('S2-10', [12, 13], {
   'typ': 'tabela', 'nadtytul': 'POWODY TRZECI I CZWARTY',
   'naglowek': 'Ocena scala, cel się mierzy',
   'naglowki': ['ZASADA', 'CO Z NIEJ WYNIKA'], 'szerokosci': [38, 62],
   'wiersze': [
     ['Każdy wniosek ma źródło', 'Nie widać, skąd wzięło się zdanie → **nie da się obronić zalecenia**'],
     ['Każde zalecenie ma wniosek', 'Najczęstsze pytanie nadzoru: **na jakiej podstawie zespół to stwierdził?**'],
     ['„Rozwijanie kompetencji społecznych"', 'Po pół roku: „cel realizowany częściowo" — **nic nie znaczy**'],
     ['Cel z liczbą', '„Kryterium 3 z 5 dni, osiągnięto 2, **modyfikujemy metodę**"'],
   ],
 }),
 ('S2-11', [14], {
   'typ': 'punkty', 'nadtytul': 'POWÓD PIĄTY',
   'naglowek': 'Zalecenie bez sposobu realizacji nie wystarcza',
   'punkty': [
     'Samo **przepisanie zalecenia poradni** do programu to za mało.',
     'Przy każdym zapisujemy: **w jakiej formie, kto, w jakim wymiarze godzin i od kiedy**.',
     'Brak tej kolumny to **najczęstsze uchybienie** stwierdzane w kontrolach dokumentacji kształcenia specjalnego.',
   ],
 }),
 ('S2-12', [15], {
   'typ': 'punkty', 'nadtytul': 'POWÓD SZÓSTY · O KTÓRYM MÓWI SIĘ NAJRZADZIEJ',
   'naglowek': 'Pieniądze — czyj to obowiązek',
   'punkty': [
     'Art. 8 ust. 1 ustawy o finansowaniu adresuje obowiązek do **jednostki samorządu terytorialnego**, nie do szkoły.',
     'Żaden bezpośredni obowiązek dokumentacyjny **z tego przepisu dla nas nie wynika**.',
     'Wniosek jest pośredni, ale praktyczny: organ prowadzący musi wiedzieć, **jakie zajęcia, w jakim wymiarze i przez kogo**.',
     'Program **bez wymiaru godzin, form i osób** nie daje tej informacji wcale.',
   ],
 }),
 ('S2-13', [16], {
   'typ': 'punkty', 'nadtytul': 'POWÓD SIÓDMY · MODEL BIOPSYCHOSPOŁECZNY',
   'naglowek': 'Dostosowanie bez opisanej bariery wisi w próżni',
   'punkty': [
     'Trudność powstaje **na styku możliwości ucznia i wymagań otoczenia**.',
     'Nie opisaliśmy, że hałas skraca czas pracy z ośmiu minut do jednej?',
     'Wtedy pierwsza ławka i słuchawki wyciszające to zapis, przy którym **nikt nie wie, po czym poznamy, że pomógł**.',
   ],
 }),
 ('S2-14', [17], {
   'typ': 'punkty', 'nadtytul': 'POWÓD ÓSMY',
   'naglowek': 'Prawa rodziców i głos ucznia',
   'punkty': [
     'Rodzice mają prawo **uczestniczyć w spotkaniach zespołu** oraz **otrzymać kopię programu i oceny**.',
     'Zapis o przekazaniu kopii, **z datą i podpisem**, jest elementem dokumentacji — **nie uprzejmością**.',
     'Ponad wymóg rozporządzenia wprowadzamy sekcję **„Mój głos"** — perspektywę ucznia jego słowami albo przez wskazanie.',
   ],
 }),
 ('S2-15', [18], {
   'typ': 'sciezki', 'naglowek': 'Powód dziewiąty — ciągłość między etapami',
   'lewa': {'tytul': 'Klasa III', 'kroki': [
     'Ucznia zna jedna wychowawczyni', 'Widzi go codziennie', 'Wiedza bywa tylko w jej głowie']},
   'prawa': {'tytul': 'Klasa IV', 'kroki': [
     'Ucznia zna dziesięcioro nauczycieli', 'Każdy widzi go dwie godziny w tygodniu',
     'Karta przekazania i dostosowania zapisane przedmiotowo']},
 }),
 ('S2-16', [19, 20, 21], {
   'typ': 'domkniecie', 'naglowek': 'Powód dziesiąty i zdanie do zapamiętania',
   'zdania': [
     'Uczeń, którego trudności **nie opisano w dokumentacji w listopadzie**, nie dostanie dostosowania na egzaminie w maju.',
     'Nie zmieniamy dokumentacji dlatego, że **ktoś nam kazał**.',
     'Zmieniamy ją, bo stara przestała odpowiadać na pytania, które **teraz nam zadają**.',
   ],
 }),
 ('S2-17', [22, 23, 24], {
   'typ': 'tabela', 'nadtytul': 'CZĘŚĆ PRAKTYCZNA · ZMIANY 1–3',
   'naglowek': 'Co dokładnie zmieniamy?',
   'naglowki': ['CO', 'NA CO'], 'szerokosci': [34, 66],
   'wiersze': [
     ['Narzędzie obserwacji', 'Kwestionariusz z kodami i skalą — **KSzOF I–III, IV–VI, VII–VIII**'],
     ['Ocena wielospecjalistyczna', 'Karta **scalająca z wpisanymi źródłami** — każda sekcja wskazuje druk'],
     ['Program', 'Zalecenia **w dwóch kolumnach**: treść i sposób realizacji'],
   ],
 }),
 ('S2-18', [25, 26, 27, 28], {
   'typ': 'tabela', 'nadtytul': 'ZMIANY 4–7',
   'naglowek': 'Cele, dostosowania, uczeń bez orzeczenia, dane',
   'naglowki': ['CO', 'NA CO'], 'szerokosci': [34, 66],
   'wiersze': [
     ['Cele', '**Kryterium liczbowe i data pomiaru** — wskaźnik staje się narzędziem ewaluacji'],
     ['Dostosowania', 'Zapisane **przedmiotowo**, każde ze wskazaniem bariery z oceny'],
     ['Uczeń bez orzeczenia', '**Plan wsparcia** — pomoc p-p dostaje swój dokument'],
     ['Dane', 'Precz z PESEL-em, adresem i kopiami zaświadczeń — **druki dziedziczą z metryczki**'],
   ],
 }),
 ('S2-19', [29, 30, 31], {
   'typ': 'punkty', 'nadtytul': 'ZMIANA ÓSMA I RZECZ RÓWNIE WAŻNA',
   'naglowek': 'Czego nie zmieniamy?',
   'punkty': [
     'Ślad współpracy — rejestr kontaktów, potwierdzenie kopii, udział rodzica — **stały element teczki**.',
     '**Nie przepisujemy** dokumentów już sporządzonych i **nie unieważniamy** dotychczasowych ocen i programów.',
     '**Nie zwiększamy liczby druków** — wprowadzamy je po to, żeby te same dane wpisywać raz, a nie w pięciu miejscach.',
   ],
 }),
 ('S2-20', [32, 33, 34], {
   'typ': 'domkniecie', 'naglowek': 'Podsumowanie części drugiej',
   'zdania': [
     'Program i ocenę aktualizujemy **przy najbliższej ocenie**, a dotychczasowe zapisy zostają jako **historia wsparcia**.',
     'Zmieniamy **język, nie objętość**. Zmieniamy **strukturę, nie liczbę druków**.',
     'Robimy to po to, żeby **dziesięć dni na opinię było terminem realnym, a nie źródłem stresu**.',
   ],
 }),
]



# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 5

PLAN_5 = [
 ('S5-01', [0, 1], {
   'typ': 'tytulModulu', 'numer': '5', 'czas': '11:20',
   'tytul': 'KSzOF — serce całej dokumentacji',
   'podtytul': 'Budowa arkusza, zasady rzetelnej obserwacji, liczenie wyniku, '
               'odczyt stenów i odczyt profilu ucznia.',
 }),
 ('S5-02', [2], {
   'typ': 'punkty', 'nadtytul': 'CZYM JEST KWESTIONARIUSZ?',
   'naglowek': 'Narzędzie kryterialne, nie diagnoza',
   'punkty': [
     'Opisuje funkcjonowanie ucznia w **dziewięciu obszarach ICF**, w codziennych sytuacjach szkolnych i domowych.',
     'Przy każdym twierdzeniu stoi **kod klasyfikacji**.',
     'Dzięki temu nasz opis ucznia mówi **tym samym językiem, co dokumentacja poradni**.',
   ],
 }),
 ('S5-03', [3, 4], {
   'typ': 'punkty', 'nadtytul': 'ICF · WHO 2001',
   'naglowek': 'Model biopsychospołeczny — trzy składniki',
   'punkty': [
     'Nie opisuje choroby ani rozpoznania — opisuje, **jak człowiek funkcjonuje**.',
     'Stan zdrowia i funkcje ciała · aktywność i uczestniczenie · **czynniki środowiskowe i osobowe**.',
     'Dwoje uczniów z tym samym rozpoznaniem funkcjonuje inaczej: **inna klasa, inny hałas, inne wsparcie w domu**.',
     '**Bez opisu barier nie da się zaplanować dostosowań.**',
   ],
 }),
 ('S5-04', [5], {
   'typ': 'tabela', 'nadtytul': 'DZIEWIĘĆ OBSZARÓW = DZIEWIĘĆ ROZDZIAŁÓW ICF',
   'naglowek': 'Aktywność i uczestniczenie',
   'naglowki': ['KOD', 'OBSZAR', 'KOD', 'OBSZAR'], 'szerokosci': [10, 40, 10, 40],
   'wiersze': [
     ['d110', 'Uczenie się i stosowanie wiedzy', 'd640', 'Życie domowe'],
     ['d210', 'Ogólne zadania i obowiązki', 'd710', 'Wzajemne kontakty i związki'],
     ['d310', 'Porozumiewanie się', 'd820', 'Edukacja szkolna'],
     ['d440', 'Motoryka i poruszanie się', 'd920', 'Życie w społeczności lokalnej'],
     ['d510', 'Dbanie o siebie i samoobsługa', '', ''],
   ],
 }),
 ('S5-05', [6, 7], {
   'typ': 'punkty', 'nadtytul': 'TRZY WERSJE ARKUSZA',
   'naglowek': 'O wyborze decyduje wiek rozwojowy, nie metrykalny',
   'punkty': [
     'Klasy **I–III**: pięćdziesiąt dwa twierdzenia. Klasy **IV–VI** i **VII–VIII**: ten sam układ dziewięciu obszarów, twierdzenia dopasowane do wieku.',
     'Ucznia klasy siódmej z niepełnosprawnością intelektualną w stopniu umiarkowanym obserwujemy **wersją I–III**.',
     'Kwestionariusz **nie jest diagnozą** i nie zastępuje badania psychologicznego, logopedycznego ani lekarskiego.',
   ],
 }),
 ('S5-06', [8, 9], {
   'typ': 'tabela', 'nadtytul': 'SKALA · ZAWSZE JEDNA WARTOŚĆ',
   'naglowek': 'Pięć stopni i litera N',
   'naglowki': ['WARTOŚĆ', 'CO OZNACZA'], 'szerokosci': [22, 78],
   'wiersze': [
     ['1 – 2', 'Stopień niewielki i mały'],
     ['3', 'Stopień umiarkowany'],
     ['4', 'Stopień duży'],
     ['5', '**Mocna strona ucznia** — i tak ją zapisujemy w ocenie'],
     ['N', 'Brak możliwości obserwacji — **pełnoprawna, uczciwa odpowiedź**; nie obniża wyniku'],
   ],
 }),
 ('S5-07', [10], {
   'typ': 'cytat', 'naglowek': 'Ograniczenie litery N',
   'tresc': 'Normy stenowe zbudowano dla arkusza wypełnionego w całości. Jeżeli w arkuszu jest '
            '**więcej niż pięć pozycji N**, wyniku ogólnego **nie przeliczamy na steny** — odczytujemy '
            'sam profil obszarowy i zaznaczamy, że arkusz jest niepełny.',
   'zrodlo': 'To uczciwsze niż wynik stenowy policzony z połowy danych',
 }),
 ('S5-08', [11, 12], {
   'typ': 'tabela', 'nadtytul': 'OSIEM ZASAD RZETELNEJ OBSERWACJI',
   'naglowek': 'Jak wypełniamy arkusz?',
   'naglowki': ['', ''], 'szerokosci': [50, 50],
   'wiersze': [
     ['**Cały arkusz** — wszystkie dziewięć obszarów, nie dzielimy ich między oceniających',
      'Odnosimy się do **oczekiwań rozwojowych dla wieku** ucznia'],
     ['**Dwa do czterech tygodni** obserwacji, nie jeden dzień',
      '**Obserwacje jakościowe** — konkretne przykłady przy ocenach skrajnych'],
     ['**Samodzielnie**, bez konsultowania ocen przed spotkaniem zespołu',
      'W drugim etapie **co najmniej trzech nauczycieli przedmiotów**'],
     ['Oceniamy **to, co uczeń robi**, a nie to, co potrafiłby zrobić',
      'Arkusz wraca do koordynatora **w umówionym terminie**'],
   ],
 }),
 ('S5-10', [13, 14], {
   'typ': 'cytat', 'naglowek': 'Przykład wypełnienia — obszar pierwszy',
   'tresc': 'Twierdzenie 2: „uważnie słucha wypowiedzi". Przez trzy tygodnie słucha **przy kartach pracy**, '
            'traci uwagę **przy tablicy** → zaznaczam **2** i dopisuję obserwację jakościową. '
            'Twierdzenie 12: „samodzielnie pisze zdania". Przepisuje z licznymi opuszczeniami → **1**.',
   'zrodlo': 'Uczennica klasy III A · KSzOF I–III',
 }),
 ('S5-11', [15], {
   'typ': 'punkty', 'nadtytul': 'SENS DWÓCH NIEZALEŻNYCH ARKUSZY',
   'naglowek': 'Obszar szósty — życie domowe',
   'punkty': [
     'Ma **tylko dwa twierdzenia** i dotyczy sytuacji, których wychowawczyni nie widzi.',
     'Zaznaczam **N w obu** i pozostawiam ten obszar **arkuszowi rodzica**.',
     'To nie jest luka w danych — to **podział ról między obserwatorami**.',
   ],
 }),
 ('S5-12', [16, 17], {
   'typ': 'tabela', 'nadtytul': 'KROK PIERWSZY',
   'naglowek': 'Wynik ogólny',
   'naglowki': ['ELEMENT', 'WARTOŚĆ'], 'szerokosci': [58, 42],
   'wiersze': [
     ['Twierdzenia × maksymalna ocena', '52 × 5 = **260 punktów**'],
     ['Suma w naszym przykładzie', '**114 punktów**'],
   ],
 }),
 ('S5-13', [18], {
   'typ': 'punkty', 'nadtytul': 'KROK DRUGI · ODCZYT STENA',
   'naglowek': 'Dwie kolumny norm to nie pomyłka w druku',
   'punkty': [
     'Tabela ma **osobne przedziały dla nauczyciela i osobne dla rodzica**.',
     'Nauczyciele i rodzice **systematycznie różnią się** w ocenie tych samych zachowań — normy to uwzględniają.',
     'Sto czternaście punktów w kolumnie nauczyciela to **sten czwarty — wynik niski, sygnał trudności**.',
   ],
 }),
 ('S5-14', [19, 20], {
   'typ': 'cytat', 'naglowek': 'Krok trzeci — profil obszarowy',
   'tresc': 'Obszary mają różną liczbę twierdzeń (pierwszy — piętnaście, dziewiąty — dwa), więc surowych '
            'sum nie da się porównywać. Każdy obszar przeliczamy na skalę 0–20: '
            '**suma obszaru ÷ maksimum obszaru × 20**, zaokrąglone do pełnego punktu. '
            'Obszar I: 23 ÷ 75 × 20 = **6**. Obszar III: 22 ÷ 40 × 20 = **11**.',
   'zrodlo': 'Jeden wzór dla wszystkich dziewięciu obszarów',
 }),
 ('S5-15', [21], {
   'typ': 'tabela', 'nadtytul': 'PROGI NA SKALI 0–20',
   'naglowek': 'Cztery poziomy wsparcia',
   'naglowki': ['WYNIK', 'POZIOM'], 'szerokosci': [22, 78],
   'wiersze': [
     ['18 – 20', '**Zasób** — mocna strona ucznia'],
     ['14 – 17', 'Poziom I — wsparcie minimalne'],
     ['9 – 13', 'Poziom II — wsparcie umiarkowane'],
     ['8 i mniej', 'Poziom III — wsparcie znaczne, **ocena wielospecjalistyczna i konsultacja z poradnią**'],
   ],
 }),
 ('S5-16', [22], {
   'typ': 'punkty', 'nadtytul': 'ODCZYT W NASZYM PRZYKŁADZIE',
   'naglowek': 'Rekomendowany poziom wsparcia',
   'punkty': [
     'W **poziomie trzecim**: uczenie się, zadania i obowiązki, życie domowe, edukacja szkolna.',
     'Pozostałe **pięć obszarów** — poziom drugi.',
     'Rekomendacja ogólna: **poziom drugi**, ale w czterech obszarach wsparcie znaczne. **Ten zapis wędruje wprost do programu.**',
   ],
 }),
 ('S5-17', [23], {
   'typ': 'cytat', 'naglowek': 'Reguła nadrzędna',
   'tresc': 'Każde pojedyncze twierdzenie ocenione na **jeden lub dwa podlega analizie zespołu** — '
            'niezależnie od wyniku obszaru i niezależnie od stena. Uczeń może mieć w porozumiewaniu się '
            'czternaście na dwadzieścia, a jednocześnie jedynkę przy proszeniu o pomoc. '
            '**Średnia to zamaskuje. Reguła nadrzędna nie pozwoli tego przeoczyć.**',
   'zrodlo': 'Zasada obowiązująca przy każdym odczycie kwestionariusza',
 }),
 ('S5-18', [24], {
   'typ': 'punkty', 'nadtytul': 'ODCZYT PROFILU · TRZY KROKI',
   'naglowek': 'Kolor, kształt, pojedyncze twierdzenia',
   'punkty': [
     '**Kolor:** zielony — zasób i poziom I; żółty — poziom II; czerwony — poziom III.',
     '**Kształt płaski i niski** → trudność globalna → ocena wielospecjalistyczna.',
     '**Jedno głębokie wcięcie** → trudność wybiórcza → konkretny moduł pogłębiony.',
     'Na końcu wracamy do **twierdzeń ocenionych nisko, także w obszarach zielonych**.',
   ],
 }),
 ('S5-19', [25], {
   'typ': 'punkty', 'nadtytul': 'ARKUSZE RÓWNOLEGŁE',
   'naglowek': 'Profili nie uśredniamy — rozbieżność jest informacją',
   'punkty': [
     'W domu wyżej niż w szkole → **szukamy barier w klasie**.',
     'W szkole wyżej niż w domu → **dzielimy się z rodzicami sprawdzonymi rutynami**.',
     'Różnią się dwaj nauczyciele przedmiotów → **pytamy, czym różnią się ich lekcje**.',
   ],
 }),
 ('S5-20', [26], {
   'typ': 'domkniecie', 'naglowek': 'Dwa razy w roku, na tym samym arkuszu',
   'zdania': [
     '**Wrzesień** — pomiar bazowy dla **wszystkich uczniów w oddziale**; uczeń z orzeczeniem musi mieć program do 30 września.',
     '**Maj** — pomiar kontrolny, ten sam arkusz, **innym kolorem**.',
     'Wtedy widać **drogę, którą uczeń przeszedł**.',
   ],
 }),
]



# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 6

PLAN_6 = [
 ('S6-01', [0, 1], {
   'typ': 'tytulModulu', 'numer': '6', 'czas': '10:30',
   'tytul': 'Obserwacja pogłębiona',
   'podtytul': 'Kwestionariusz powiedział, gdzie uczeń potrzebuje wsparcia. '
               'Obserwacja pogłębiona odpowiada na pytanie: dlaczego.',
 }),
 ('S6-02', [2], {
   'typ': 'sciezki', 'naglowek': 'Przesiew a obserwacja pogłębiona',
   'lewa': {'tytul': 'Przesiew — KSzOF', 'kroki': [
     'Obejmuje wszystkich uczniów w oddziale', 'Wrzesień i maj', 'Odpowiada na pytanie: gdzie?']},
   'prawa': {'tytul': 'Obserwacja pogłębiona', 'kroki': [
     'Obejmuje pojedynczego ucznia', 'Kilkanaście godzin pracy zespołu',
     'Uruchamiamy z przesłanką, nie na wszelki wypadek']},
 }),
 ('S6-03', [3, 4], {
   'typ': 'tabela', 'nadtytul': 'SIEDEM REGUŁ PRZEKIEROWANIA · WYSTARCZY JEDNA',
   'naglowek': 'Kiedy zespół siada nad kartą decyzyjną?',
   'naglowki': ['REGUŁA', 'PRÓG'], 'szerokosci': [46, 54],
   'wiersze': [
     ['Wynik obszaru', '**8 punktów lub mniej** na skali 0–20 (poziom III)'],
     ['Twierdzenia ocenione nisko', '**Dwa lub więcej** ocen 1–2 w tym samym obszarze'],
     ['Rozbieżność między oceniającymi', '**Dwa steny lub więcej** w wyniku ogólnym'],
     ['Sygnał zdrowotny z metryczki', 'Nadwrażliwość sensoryczna, choroba przewlekła'],
     ['Zachowanie zagrażające', '**Natychmiast — nie czekamy na zespół**'],
     ['Brak poprawy mimo pomocy', 'Około **trzy miesiące**'],
     ['Nagła zmiana funkcjonowania', 'Spadek ocen w **3 przedmiotach** albo **20% nieobecności** w miesiącu'],
   ],
 }),
 ('S6-04', [5], {
   'typ': 'domkniecie', 'naglowek': 'Po co reguły, skoro przepis ich nie wymienia?',
   'zdania': [
     'Reguły są **naszą decyzją jako rady pedagogicznej**, wpisaną do procedury szkoły.',
     'Przepis wymaga **rozpoznawania potrzeb i oceny efektywności**.',
     'Reguły sprawiają, że decyzja **nie zależy od tego, kto danego dnia patrzy na arkusz**.',
   ],
 }),
 ('S6-05', [6, 7, 8], {
   'typ': 'tabela', 'nadtytul': 'NARZĘDZIE PIERWSZE · MODEL ABC',
   'naglowek': 'Trzy litery, trzy pytania',
   'naglowki': ['LITERA', 'CO ZAPISUJEMY'], 'szerokosci': [26, 74],
   'wiersze': [
     ['A · poprzednik', 'Co działo się **bezpośrednio przed** zachowaniem'],
     ['B · zachowanie', 'Opis **obserwowalny i mierzalny**'],
     ['C · następstwo', 'Co stało się **bezpośrednio potem** — w tym reakcja dorosłych i rówieśników'],
   ],
 }),
 ('S6-06', [9], {
   'typ': 'cytat', 'naglowek': 'Zapis poprawny — każde zdanie da się sprawdzić',
   'tresc': 'Na trzeciej lekcji matematyki nauczyciel polecił przepisać zadanie o sześciu linijkach. '
            'Uczeń pisał **około dwóch minut**, odłożył ołówek, położył głowę na ławce i nie reagował '
            'na polecenia **przez około sześć minut**. Nauczyciel podzielił zadanie na trzy części '
            'i zaznaczył pierwszą. Uczeń przepisał zaznaczoną część.',
   'zrodlo': 'Żadne zdanie nie zawiera interpretacji',
 }),
 ('S6-07', [10], {
   'typ': 'cytat', 'naglowek': 'Zapis wadliwy — spotykany najczęściej',
   'tresc': 'Uczeń **zniechęcił się**, bo **nie chciało mu się pracować**, i **zamanifestował swoją '
            'niechęć** do przedmiotu.',
   'zrodlo': 'Trzy interpretacje w jednym zdaniu i ani jednego faktu, który dałoby się policzyć',
 }),
 ('S6-08', [11], {
   'typ': 'punkty', 'nadtytul': 'JAK PROWADZIMY ABC?',
   'naglowek': 'Dane najpierw, interpretacja później',
   'punkty': [
     'Zbieramy **10–15 zapisów w ciągu dwóch, trzech tygodni**, z różnych lekcji i różnych pór dnia.',
     'Szukamy **funkcji zachowania**: uwaga, przedmiot lub aktywność, **uniknięcie trudnego zadania**, regulacja pobudzenia.',
     'Interpretację formułujemy **dopiero na spotkaniu zespołu**, po analizie wielu zdarzeń.',
     'Zapisujemy ją w arkuszu analizy funkcjonalnej: hipoteza, dane, **plan zachowania zastępczego**.',
   ],
 }),
 ('S6-09', [12], {
   'typ': 'domkniecie', 'naglowek': 'To w szkole jest kluczowe',
   'zdania': [
     'Nie wystarczy ustalić, **po co** uczeń zachowuje się w dany sposób.',
     'Trzeba wskazać, **jakim zachowaniem osiągnie ten sam cel** — i tego go nauczyć.',
     'Krzykiem unika trudnego zadania? Uczymy karty **„proszę o przerwę"** i honorujemy ją natychmiast.',
   ],
 }),
 ('S6-10', [13, 14], {
   'typ': 'punkty', 'nadtytul': 'NARZĘDZIE DRUGIE · PROFIL SENSORYCZNY',
   'naglowek': 'Siedem układów, opis wzorca',
   'punkty': [
     'Słuchowy, wzrokowy, dotykowy, węchowy, smakowy, **przedsionkowy i proprioceptywny**.',
     'Ustrukturyzowana obserwacja reakcji na bodźce.',
     '**Opisujemy wzorzec, nie stawiamy rozpoznania.**',
   ],
 }),
 ('S6-11', [15], {
   'typ': 'tabela', 'nadtytul': 'TRZY WZORCE',
   'naglowek': 'Co widzimy w klasie?',
   'naglowki': ['WZORZEC', 'PRZYKŁADY'], 'szerokosci': [30, 70],
   'wiersze': [
     ['Nadreaktywność', 'Zakrywa uszy przy dzwonku, unika tłoku, nie znosi metek'],
     ['Podreaktywność', 'Nie reaguje na wołanie mimo prawidłowego słuchu, wolno rozpoczyna czynności'],
     ['Poszukiwanie bodźców', 'Buja się na krześle, wpada na przedmioty, mówi bardzo głośno'],
   ],
 }),
 ('S6-12', [16, 17], {
   'typ': 'punkty', 'nadtytul': 'TRZY MIEJSCA, KTÓRYCH W PRZEDSZKOLU NIE MA',
   'naglowek': 'Korytarz, stołówka, sala gimnastyczna',
   'punkty': [
     'Tam natężenie bodźców jest **największe**.',
     'Tam najczęściej dochodzi do zachowań, **które potem opisujemy jako zachowania na lekcji**.',
     'Granica kompetencji: nauczyciel **opisuje reakcje**, rozpoznanie należy do **terapeuty integracji sensorycznej**.',
   ],
 }),
 ('S6-13', [18, 19], {
   'typ': 'punkty', 'nadtytul': 'NARZĘDZIE TRZECIE · TEORIA UMYSŁU',
   'naglowek': 'Zdolność przypisywania stanów umysłu',
   'punkty': [
     'Wiedza, przekonania, intencje i emocje — oraz rozumienie, że **mogą różnić się od naszych**.',
     'Fundament współpracy w grupie, **żartu, ironii, pracy projektowej** i rozumienia tekstu literackiego.',
   ],
 }),
 ('S6-14', [20], {
   'typ': 'punkty', 'nadtytul': 'KIEDY TAKA OBSERWACJA JEST POTRZEBNA?',
   'naglowek': 'Sześć sygnałów',
   'punkty': [
     'Obszar wzajemnych kontaktów **wyraźnie niższy** przy zachowanych obszarach uczenia się i poruszania.',
     'Trudność w odczytywaniu **mimiki, gestu i tonu głosu**; rozumienie języka dosłownie.',
     '**Nie odróżnia przypadkowego potrącenia od celowego zaczepienia** — reaguje na oba tak samo.',
     'Zespół rozważa wystąpienie do poradni w sprawie całościowych zaburzeń rozwoju.',
   ],
 }),
 ('S6-15', [21, 22], {
   'typ': 'punkty', 'nadtytul': 'WIEK MA ZASADNICZE ZNACZENIE',
   'naglowek': 'Co obserwujemy w szkole podstawowej?',
   'punkty': [
     'Fałszywe przekonanie **pierwszego rzędu** — od około czwartego roku życia.',
     '**Drugiego rzędu** („co Ola myśli, że Kuba myśli") — od około szóstego, siódmego roku.',
     'W szkole obserwujemy więc **ironię, żart, obietnicę, kłamstwo uprzejmościowe i intencję rówieśnika**.',
     'Obserwacja **nie jest testem** i nie prowadzi do rozpoznania — prowadzi do rzetelnego opisu dla poradni.',
   ],
 }),
 ('S6-16', [23, 24], {
   'typ': 'domkniecie', 'naglowek': 'Narzędzie czwarte — zanim uznamy, że problem leży w zachowaniu',
   'zdania': [
     'Uczeń, który **nie rozumie polecenia**, wygląda na nieposłusznego.',
     'Uczeń, który **nie potrafi powiedzieć, czego chce**, krzyczy albo wychodzi z sali.',
     'Sprawdzamy najpierw, **czy uczeń nas rozumie i czy potrafi się z nami porozumieć**.',
   ],
 }),
 ('S6-17', [25, 26], {
   'typ': 'tabela', 'nadtytul': 'KARTA ROZWOJU MOWY I KOMUNIKACJI',
   'naglowek': 'Pięć obszarów, dwadzieścia pięć wskaźników',
   'naglowki': ['OBSZAR', 'SKALA I UWAGI'], 'szerokosci': [52, 48],
   'wiersze': [
     ['Rozumienie mowy', '0 — nie występuje'],
     ['Mowa czynna i artykulacja', '1 — częściowo lub z pomocą dorosłego'],
     ['Słuch fonematyczny', '2 — samodzielnie'],
     ['Słownictwo i gramatyka', 'Każdy obszar daje **0–10 punktów**'],
     ['Komunikacja i budowanie wypowiedzi', 'W szkole dochodzi **technika czytania i pisania**'],
   ],
 }),
 ('S6-18', [27, 28], {
   'typ': 'punkty', 'nadtytul': 'ODCZYT I GRANICA KOMPETENCJI',
   'naglowek': 'Trzy przedziały, jedna zasada',
   'punkty': [
     '**8–10** to zasób · **4–7** obszar wymagający wsparcia · **0–3 priorytet**.',
     'Wynik zasila cele, ocenę wielospecjalistyczną i opinię dla poradni.',
     'Nauczyciel **opisuje, co słyszy i widzi**. Diagnoza logopedyczna należy do **logopedy**.',
   ],
 }),
 ('S6-19', [29, 30], {
   'typ': 'domkniecie', 'naglowek': 'Karta decyzyjna — jedna na jednego ucznia',
   'zdania': [
     'Sprawdzamy siedem reguł, wybieramy narzędzie, wpisujemy **kto obserwuje, od kiedy i kiedy spotyka się zespół**.',
     'Kartę wpinamy do teczki **również wtedy, gdy decyzja brzmi: nie uruchamiamy**.',
     'Zapis decyzji odmownej **chroni nas**, gdy pół roku później ktoś zapyta, dlaczego nic nie zrobiono.',
   ],
 }),
]



# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 7

PLAN_7 = [
 ('S7-01', [0, 1], {
   'typ': 'tytulModulu', 'numer': '7', 'czas': '14:10',
   'tytul': 'Od danych do zobowiązania',
   'podtytul': 'WOPF-SP, IPET, plan wsparcia dla ucznia bez orzeczenia, cele mierzalne, '
               'ewaluacja i opinia dla poradni.',
 }),
 ('S7-02', [2, 3], {
   'typ': 'cytat', 'naglowek': 'Wielospecjalistyczna ocena poziomu funkcjonowania',
   'tresc': 'Zespół dokonuje oceny **co najmniej dwa razy w roku szkolnym**, a ocena jest '
            '**podstawą opracowania i modyfikacji programu**.',
   'zrodlo': 'Rozporządzenie MEN z 9 sierpnia 2017 r. · t.j. Dz.U. 2020 poz. 1309, § 6',
 }),
 ('S7-03', [4], {
   'typ': 'punkty', 'nadtytul': 'DLACZEGO OCENA JEST TAK WAŻNA?',
   'naglowek': 'Cztery funkcje',
   'punkty': [
     'Wyznacza **punkt startu**, bez którego cele byłyby zgadywaniem.',
     '**Scala perspektywy** wychowawcy, nauczycieli przedmiotów, logopedy, psychologa i rodziców.',
     '**Chroni ucznia przed etykietą** — dwoje uczniów z tym samym orzeczeniem ma dwie różne oceny.',
     'Dokumentuje pracę szkoły.',
   ],
 }),
 ('S7-04', [5, 6], {
   'typ': 'punkty', 'nadtytul': 'DWADZIEŚCIA TRZY SEKCJE — I ANI RAZU WIĘCEJ PRACY',
   'naglowek': 'Jeden druk, który zbiera wyniki z druków wcześniejszych',
   'punkty': [
     'Sekcja I a — **wybór ścieżki**: orzeczenie → program, brak orzeczenia → plan wsparcia.',
     'Sekcje II–IV — zespół, **mapa dokumentów źródłowych**, informacje medyczne istotne dla funkcjonowania.',
     'Sekcja V i V a — wyniki kwestionariusza w dziewięciu obszarach, rozpisane na mocne strony i trudności.',
     'Sekcje VI–X — obserwacja pogłębiona: zachowanie, poznanie społeczne, mowa, sensoryka.',
   ],
 }),
 ('S7-05', [7], {
   'typ': 'tabela', 'nadtytul': 'PRZY KAŻDEJ SEKCJI STOI, SKĄD BRAĆ DANE',
   'naglowek': 'Mapa źródeł oceny',
   'naglowki': ['BLOK OCENY', 'ŹRÓDŁO'], 'szerokosci': [42, 58],
   'wiersze': [
     ['Mocne strony', 'Oceny **najwyższe** w kwestionariuszu'],
     ['Trudności', 'Oceny najniższe i obserwacja pogłębiona'],
     ['Bariery i ułatwienia', 'Analiza ABC i profil sensoryczny'],
     ['Efekty wsparcia', 'Poprzednia karta ewaluacji'],
     ['Głos ucznia', 'Ankieta **„Mój głos"**'],
   ],
 }),
 ('S7-06', [8, 9, 10], {
   'typ': 'punkty', 'nadtytul': 'IPET · TERMINY I PRAWA RODZICÓW',
   'naglowek': 'Kiedy program i co należy rodzicom?',
   'punkty': [
     '**Do 30 września** albo **30 dni od złożenia orzeczenia** w szkole.',
     'Rodzice mają prawo **uczestniczyć w spotkaniach zespołu** oraz **otrzymać kopię programu i oceny**.',
     'Dyrektor zawiadamia o terminie w sposób przyjęty w szkole, a przekazanie kopii **odnotowujemy w rejestrze kontaktów**.',
   ],
 }),
 ('S7-07', [11], {
   'typ': 'tabela', 'nadtytul': 'OSIEM ELEMENTÓW · LISTA KONTROLNA KAŻDEJ KONTROLI',
   'naglowek': 'Co musi znaleźć się w programie?',
   'naglowki': ['ELEMENT', 'ELEMENT'], 'szerokosci': [50, 50],
   'wiersze': [
     ['Zakres i sposób dostosowania wymagań', 'Zajęcia rewalidacyjne i socjoterapeutyczne'],
     ['Zintegrowane działania nauczycieli i specjalistów', 'Doradztwo zawodowe w klasach starszych'],
     ['Formy, okres i wymiar godzin pomocy', 'Zakres współpracy z rodzicami'],
     ['Działania wspierające rodziców, współpraca z poradnią', 'Dostosowanie warunków egzaminu'],
   ],
 }),
 ('S7-08', [12], {
   'typ': 'sciezki', 'naglowek': 'Skąd biorą się zapisy programu?',
   'lewa': {'tytul': 'Orzeczenie', 'kroki': [
     'Mówi, **co uczniowi zalecono**', 'Zalecenia przepisujemy jedno po drugim',
     'Przy każdym: forma, kto, wymiar']},
   'prawa': {'tytul': 'Ocena wielospecjalistyczna', 'kroki': [
     'Mówi, **co widzimy w szkole**', 'Zalecenia z oceny traktujemy tak samo',
     'Program pokazuje, **jak zamieniamy to w działanie**']},
 }),
 ('S7-09', [13, 14], {
   'typ': 'cytat', 'naglowek': 'Dostosowanie zapisane przedmiotowo',
   'tresc': '„Wydłużenie czasu pracy" **nie mówi nic** nauczycielowi geografii. „Na sprawdzianach '
            'z geografii: polecenia czytane na głos, mapa konturowa z pogrubionymi granicami, czas '
            'wydłużony o połowę, ocena za treść bez uwzględniania błędów zapisu" — **mówi wszystko**.',
   'zrodlo': 'Karta dostosowań przedmiotowych — jedna strona na przedmiot, nauczyciel dostaje ją we wrześniu',
 }),
 ('S7-10', [15], {
   'typ': 'tabela', 'nadtytul': 'PIĘĆ RODZAJÓW DOSTOSOWAŃ',
   'naglowek': 'Zmieniamy jak uczymy i jak sprawdzamy — nie czego uczymy',
   'naglowki': ['CO ZMIENIAMY', 'PRZYKŁADY'], 'szerokosci': [32, 68],
   'wiersze': [
     ['Sposób podania treści', 'Polecenie krokowe, wsparcie wizualne, tekst uproszczony'],
     ['Czas', 'Dłuższa chwila na odpowiedź, wydłużony czas na sprawdzianie'],
     ['Przestrzeń', 'Pierwsza ławka, strefa wyciszenia, korytarz przed dzwonkiem'],
     ['Sposób sprawdzania wiedzy', 'Odpowiedź ustna, test wyboru, praca na komputerze'],
     ['Pomoce', 'Nakładki na przybory, powiększona liniatura, słuchawki wyciszające'],
   ],
 }),
 ('S7-11', [16], {
   'typ': 'domkniecie', 'naglowek': 'Zintegrowane działania — jeden cel, jeden plan, wiele rąk',
   'zdania': [
     'Wszyscy pracują nad **tymi samymi celami z programu**, każdy w swoim czasie i swoimi metodami.',
     'Psycholog uczy karty **„proszę o przerwę"** → nauczyciel matematyki honoruje ją na lekcji, a rodzic w domu.',
     'Zespół spotyka się w ustalonym rytmie, prowadzi **wspólny zeszyt komunikacji i jedną kartę ewaluacji**.',
   ],
 }),
 ('S7-12', [17], {
   'typ': 'punkty', 'nadtytul': 'KLASA W DUCHU UNIWERSALNEGO PROJEKTOWANIA',
   'naglowek': 'Dostosowanie dla jednego, dobre środowisko dla wszystkich',
   'punkty': [
     'Strefy w sali, materiały dostępne i opisane, **plan lekcji w formie wizualnej**.',
     'Miejsce dobrane do potrzeb sensorycznych, regulowany hałas i światło.',
     'Jasna struktura lekcji **z zapowiedzią zmian**.',
     'Przy okazji — realizacja **ustawy o zapewnianiu dostępności**.',
   ],
 }),
 ('S7-13', [18, 19], {
   'typ': 'punkty', 'nadtytul': 'UCZEŃ BEZ ORZECZENIA — NAJLICZNIEJSZA GRUPA',
   'naglowek': 'Plan wsparcia edukacyjnego',
   'punkty': [
     'Dla ucznia **z opinią poradni albo rozpoznanego przez nauczycieli** nie sporządzamy programu.',
     'Plan ma tę samą logikę: potrzeba → **cel z kryterium** → forma pomocy → osoba → wymiar → termin oceny efektywności.',
   ],
 }),
 ('S7-14', [20], {
   'typ': 'cytat', 'naglowek': 'Istota pracy Strażnika Prawa',
   'tresc': 'Rozporządzenie o pomocy psychologiczno-pedagogicznej **nie zna dokumentu o nazwie plan '
            'wsparcia edukacyjnego**. Przepis mówi tylko, że formy, okres i wymiar godzin ustala dyrektor, '
            'a nauczyciele oceniają efektywność i dokumentują zajęcia w dziennikach. Plan wsparcia jest '
            '**naszym narzędziem wewnętrznym**, wprowadzanym zarządzeniem dyrektora — tak samo jak metryczka.',
   'zrodlo': 'Mówimy to wprost, zamiast powoływać się na przepis, którego nie ma',
 }),
 ('S7-15', [21, 22, 23], {
   'typ': 'punkty', 'nadtytul': 'CELE SMART · UCZCIWA ODPOWIEDŹ',
   'naglowek': 'Czy przepis wymaga celów SMART? Nie.',
   'punkty': [
     'SMART to sposób formułowania celu: konkretny, mierzalny, osiągalny, istotny, określony w czasie.',
     'Rozporządzenie określa zawartość programu i **nazwa SMART nie pada w nim ani razu**.',
     'Nie ma obowiązku używania tego skrótu w dokumencie.',
   ],
 }),
 ('S7-16', [24], {
   'typ': 'domkniecie', 'naglowek': 'Co natomiast jest wymagane?',
   'zdania': [
     '**Ocena efektywności** — zespół dokonuje jej co najmniej dwa razy w roku.',
     'Ocenić efektywność można tylko wtedy, gdy cel ma **kryterium, do którego da się porównać wynik**.',
     '**Nazwa jest dowolna, mierzalność jest konieczna.**',
   ],
 }),
 ('S7-17', [25, 26], {
   'typ': 'tabela', 'nadtytul': 'PIĘĆ LITER',
   'naglowek': 'Co znaczy każda z nich w celu ucznia?',
   'naglowki': ['LITERA', 'PYTANIE'], 'szerokosci': [16, 84],
   'wiersze': [
     ['S', 'Jakie zachowanie i w jakiej sytuacji?'],
     ['M', 'Ile razy z ilu prób i przy jakim wsparciu?'],
     ['A', '**Jeden krok od tego, co uczeń robi dziś?**'],
     ['R', 'Wynika z oceny i zwiększa uczestnictwo ucznia'],
     ['T', 'Do kiedy i kiedy sprawdzamy?'],
   ],
 }),
 ('S7-18', [27], {
   'typ': 'cytat', 'naglowek': 'Przykład pierwszy — technika pisania',
   'tresc': 'Zamiast „doskonalenie techniki pisania": Zofia na lekcjach języka polskiego **przepisze '
            'z tablicy zdanie do ośmiu wyrazów bez opuszczeń liter w czterech z pięciu kolejnych prób**, '
            'przy zadaniu podzielonym na trzy części z piktogramami i czasie wydłużonym o połowę, '
            'do 18 grudnia 2026 r.',
   'zrodlo': 'Pomiar: karta obserwacji przepisywania, raz w tygodniu',
 }),
 ('S7-19', [28, 29], {
   'typ': 'cytat', 'naglowek': 'Przykład drugi — zachowanie',
   'tresc': 'Zamiast „rozwijanie umiejętności radzenia sobie z emocjami": Zofia w sytuacji zadania '
            'trudnego **użyje karty „proszę o przerwę" zamiast położenia głowy na ławce, w trzech '
            'z pięciu takich sytuacji w tygodniu**, przy jednokrotnym przypomnieniu wizualnym, '
            'do 31 marca 2027 r. **Kryterium nie brzmi „w stu procentach".**',
   'zrodlo': 'Pomiar: dzienniczek zachowań zastępczych prowadzony przez nauczyciela współorganizującego',
 }),
 ('S7-20', [30, 31, 32], {
   'typ': 'tabela', 'nadtytul': 'EWALUACJA · KALENDARZ ROKU',
   'naglowek': 'Ile razy w roku i kiedy?',
   'naglowki': ['CO', 'KIEDY'], 'szerokosci': [52, 48],
   'wiersze': [
     ['Ocena wielospecjalistyczna', 'Wrzesień i styczeń, **zalecana trzecia w maju**'],
     ['Modyfikacja programu', 'Po każdej ocenie'],
     ['Ocena efektywności pomocy p-p', 'Styczeń i czerwiec'],
     ['Kwestionariusz KSzOF', 'Wrzesień i maj'],
     ['Krótkie przeglądy wskaźników', '**Listopad i marzec** — piętnaście minut na ucznia'],
   ],
 }),
 ('S7-21', [33, 34], {
   'typ': 'tabela', 'nadtytul': 'CZTERY DECYZJE PO POMIARZE',
   'naglowek': 'Co robimy z wynikiem?',
   'naglowki': ['WYNIK', 'DECYZJA'], 'szerokosci': [34, 66],
   'wiersze': [
     ['Cel osiągnięty', 'Zamykamy i stawiamy kolejny'],
     ['Osiągnięty częściowo', 'Kontynuujemy i przesuwamy termin — **nie obniżając kryterium**'],
     ['Brak postępu', 'Modyfikujemy metodę i sprawdzamy **bariery środowiskowe**'],
     ['Regres', 'Spotkanie z rodzicami i rozważenie wystąpienia do poradni'],
   ],
 }),
 ('S7-22', [35, 36, 37], {
   'typ': 'punkty', 'nadtytul': 'OPINIA DLA PORADNI · SIEDEM PUNKTÓW',
   'naglowek': 'Dziesięć dni od otrzymania prośby przez dyrektora',
   'punkty': [
     'Dane formalne · **mocne strony i uzdolnienia** · funkcjonowanie w obszarach.',
     'Trudności **z częstotliwością i kontekstem** · bariery i ułatwienia.',
     'Udzielone wsparcie i jego efekty · współpraca z rodzicami.',
   ],
 }),
 ('S7-23', [38, 39], {
   'typ': 'punkty', 'nadtytul': 'JAK PISZEMY?',
   'naglowek': 'Językiem funkcjonalnym i sprawdzalnym',
   'punkty': [
     'Opisujemy **zachowania, ich częstotliwość i kontekst**.',
     '**Rozpoznania i hipotezy diagnostyczne pozostawiamy poradni.**',
     'Informacje od rodziców i specjalistów spoza szkoły oznaczamy **jako relację, ze wskazaniem źródła**.',
     'Kwestionariusz pozostaje **naszym materiałem roboczym**.',
   ],
 }),
 ('S7-24', [40], {
   'typ': 'domkniecie', 'naglowek': 'Jedna dobra praktyka',
   'zdania': [
     'Punkt o **mocnych stronach piszemy jako pierwszy**.',
     'I **co najmniej tak samo obszernie** jak punkt o trudnościach.',
     'Ta proporcja jest najprostszym sprawdzianem, czy nasz opis ucznia **jest naprawdę funkcjonalny**.',
   ],
 }),
 ('S7-25', [41], {
   'typ': 'domkniecie', 'naglowek': 'Podsumowanie całego szkolenia',
   'zdania': [
     'Każdy druk ma swój przepis. **Obserwacja wyprzedza pismo z poradni.**',
     'Cel ma liczbę, a **ewaluacja ma konsekwencję**.',
     'Nie zmieniamy dokumentacji dlatego, że ktoś nam kazał — tylko dlatego, że **stara przestała odpowiadać na pytania, które nam teraz zadają**.',
   ],
 }),
]


PLANY = {1: PLAN_1, 2: PLAN_2, 3: PLAN_3, 4: PLAN_4, 5: PLAN_5, 6: PLAN_6, 7: PLAN_7}


TYTULY = {
  1: ('Podstawa prawna', 'co obowiązuje w szkole od 1 września 2026 r.'),
  2: ('Dlaczego zmieniamy', 'uzasadnienie zmian w dokumentacji kształcenia specjalnego'),
  3: ('Obieg dokumentów', 'jak jeden dokument wynika z drugiego'),
  4: ('Metryczka i teczka ucznia', 'pierwszy dokument września'),
  5: ('KSzOF', 'budowa narzędzia, skala, steny, liczenie wyniku'),
  6: ('Obserwacja pogłębiona', 'ABC i FBA, profil sensoryczny, teoria umysłu, karta mowy'),
  7: ('WOPF-SP, IPET, PWES', 'cele SMART, ewaluacja i opinia dla poradni'),
}

# Wskazówki aktorskie — jedna na ujęcie, dobierana do typu sceny (skill glos-ewy).
WSKAZOWKA = {
  'czolowka': '[warmly]',
  'tytulModulu': '[warmly]',
  'punkty': '[deliberately]',
  'cytat': '[emphatically]',
  'tabela': '[deliberately]',
  'druk': '[thoughtfully]',
  'sciezki': '[thoughtfully]',
  'obieg': '[thoughtfully]',
  'domkniecie': '[reassuring]',
}


def zbuduj():
    narracje = narracja_ze_skryptu()
    moduly = []
    for numer, plan in sorted(PLANY.items()):
        akapity = narracje[numer]
        tytul, podtytul = TYTULY[numer]
        ujecia = []
        for ident, indeksy, scena in plan:
            tekst = ' '.join(akapity[i] for i in indeksy)
            mp3 = os.path.join(KATALOG, 'public', 'glos', f'{ident}.mp3')
            zmierzone = dlugosc_mp3(mp3) if os.path.exists(mp3) else None
            ujecia.append({
              'id': ident,
              'scena': scena,
              'narracja': tekst,
              'narracjaTts': f"{WSKAZOWKA[scena['typ']]} {tekst}",
              'sekundy': zmierzone or sekundy_z_tekstu(tekst),
              **({'glos': f'{ident}.mp3'} if zmierzone else {}),
            })
        moduly.append({
          'id': f'S{numer}',
          'numer': str(numer),
          'tytul': tytul,
          'podtytul': podtytul,
          'ujecia': ujecia,
        })
    return moduly


if __name__ == '__main__':
    moduly = zbuduj()
    sciezka = os.path.join(KATALOG, 'src', 'scenariusz.json')
    io.open(sciezka, 'w', encoding='utf-8').write(json.dumps(moduly, ensure_ascii=False, indent=1))
    for m in moduly:
        sek = sum(u['sekundy'] for u in m['ujecia'])
        nagrane = sum(1 for u in m['ujecia'] if u.get('glos'))
        print(f"S{m['numer']} · {m['tytul']}: {len(m['ujecia'])} ujęć, "
              f"{int(sek // 60)}:{int(sek % 60):02d}, nagrane {nagrane}/{len(m['ujecia'])}")
