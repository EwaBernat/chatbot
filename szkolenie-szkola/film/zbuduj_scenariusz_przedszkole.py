# -*- coding: utf-8 -*-
"""Buduje src/scenariusz-przedszkole.json — plan scen filmu szkoleniowego dla przedszkola.

Narracja pochodzi wprost ze skryptu po audycie
(`Skrypt_dla_nauczycieli_PRZEDSZKOLE_wydanie2_po_audycie.docx`, transkrypcja narracji),
więc film mówi dokładnie to, co stoi w druku dla nauczycieli. Tutaj dokładamy tylko
warstwę obrazu: jaki typ planszy, jakie hasła zakreślamy, którą tabelę pokazujemy.

Druki pochodzą z aplikacji EduPlaner uruchomionej w trybie przedszkolnym
(`npm run dev:przedszkole`), dziecko przykładowe: Antoni Szymański, grupa 5-latki.
"""

import html, io, json, os, re, subprocess, zipfile

KATALOG = os.path.dirname(os.path.abspath(__file__))
SKRYPT = os.path.join(KATALOG, '..', 'Skrypt_dla_nauczycieli_PRZEDSZKOLE_wydanie2_po_audycie.docx')
TEMPO_SLOW_NA_MIN = 107.0


def narracja_ze_skryptu():
    """Wyciąga ponumerowane akapity narracji z każdej części skryptu."""
    xml = zipfile.ZipFile(SKRYPT).read('word/document.xml').decode('utf-8')
    akapity_xml = re.findall(r'<w:p[ >].*?</w:p>', xml, re.S)
    tekst = [html.unescape(''.join(re.findall(r'<w:t[^>]*>(.*?)</w:t>', p, re.S))).strip()
             for p in akapity_xml]
    granice = [i for i, t in enumerate(tekst) if 'CZĘŚĆ' in t and 'mp4' in t] + [len(tekst)]
    moduly = {}
    for numer, (a, b) in enumerate(zip(granice[:-1], granice[1:]), 1):
        narracja = [t for t in tekst[a:b] if re.match(r'^\d\d\s{2,}', t)]
        moduly[numer] = [re.sub(r'^\d\d\s+', '', t) for t in narracja]
    return moduly


def sekundy_z_tekstu(tekst):
    return round(len(tekst.split()) / TEMPO_SLOW_NA_MIN * 60.0 + 0.7, 2)


def dlugosc_mp3(sciezka):
    """Zmierzona długość nagrania — gdy plik już jest, on rządzi czasem sceny."""
    try:
        out = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', sciezka],
            capture_output=True, text=True, check=True)
        return round(float(out.stdout.strip()) + 0.45, 2)
    except Exception:
        return None


DRUKI = 'druki-przedszkole/przedszkole_'

# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 1
# Format: (id ujęcia, indeksy akapitów narracji, scena)

PLAN_1 = [
 ('P1-01', [0], {
   'typ': 'czolowka',
   'tytul': 'Dokumentacja dziecka krok po kroku',
   'podtytul': 'Przedszkole · rok szkolny 2026/2027 · sześć części · EduPlaner 2026',
   'czesci': ['1 · Podstawa prawna', '2 · Obieg dokumentów', '3 · Metryczka dziecka',
              '4 · KPOF', '5 · Obserwacja pogłębiona', '6 · WOPF, IPET, ewaluacja'],
 }),
 ('P1-02', [1], {
   'typ': 'tytulModulu', 'numer': '1', 'czas': '9:30',
   'tytul': 'Podstawa prawna',
   'podtytul': 'Z czego wynika każdy dokument, który wypełniamy od 1 września 2026 roku?',
 }),
 ('P1-03', [2], {
   'typ': 'punkty', 'nadtytul': 'PYTANIE, KTÓRE PADA NAJCZĘŚCIEJ',
   'naglowek': 'Czy naprawdę musimy to zmieniać?',
   'punkty': [
     '**Nie zaczynamy od zera** — aktualizujemy to, co już mamy.',
     'Dotychczasowe arkusze, oceny i programy **pozostają ważnym źródłem danych** o dziecku.',
     'Zmienia się **język**, w którym opisujemy funkcjonowanie dziecka.',
     'Zmienia się **sposób, w jaki jeden dokument zasila drugi**.',
   ],
 }),
 ('P1-04', [3], {
   'typ': 'tabela', 'nadtytul': 'SKĄD SIĘ BIORĄ ZMIANY',
   'naglowek': 'Trzy powody, dla których zmieniamy dokumentację',
   'naglowki': ['Powód', 'Co się zmienia', 'Skutek dla druków'],
   'szerokosci': [22, 40, 38],
   'wiersze': [
     ['Nowa podstawa programowa', 'osiągnięcia dziecka w **dziewięciu obszarach** zamiast czterech',
      'przemapowanie każdego narzędzia obserwacji i każdego programu'],
     ['Rozporządzenie o orzekaniu', '**ocena funkcjonalna** i opinia o funkcjonowaniu dziecka w 10 dni',
      'opis językiem funkcjonalnym: co, w jakich warunkach, przy jakim wsparciu, jak często'],
     ['Klasyfikacja ICF', 'wspólny język poradni i przedszkola',
      'opis dziecka uzupełniony o **bariery i ułatwienia** w środowisku'],
   ],
 }),
 ('P1-05', [4], {
   'typ': 'sciezki',
   'naglowek': 'Z czym wiąże się zmiana, a z czym nie?',
   'lewa': {'tytul': 'Z tym się wiąże', 'kroki': [
     'przegląd wzorów druków i aktualizacja podstaw prawnych na teksty jednolite',
     'wrześniowa obserwacja wszystkich dzieci, zanim wpłynie prośba z poradni',
     'zarządzenie dyrektora porządkujące obieg dokumentów']},
   'prawa': {'tytul': 'Z tym się NIE wiąże', 'kroki': [
     'przepisywanie dokumentów już sporządzonych',
     'program i ocenę aktualizujemy przy najbliższej ocenie wielospecjalistycznej',
     'dotychczasowe zapisy zostają w teczce jako historia wsparcia']},
 }),
 ('P1-06', [5], {
   'typ': 'punkty', 'nadtytul': 'ROLA W ZESPOLE',
   'naglowek': 'Strażnik Prawa',
   'punkty': [
     'To **nie jest** osoba, która zna przepisy na pamięć.',
     'To osoba, która przy każdej decyzji pyta: **z czego to wynika i gdzie to jest zapisane?**',
     'Funkcja jest **rotacyjna** — w ciągu roku pełni ją każda z nas.',
   ],
 }),
 ('P1-07', [6, 7], {
   'typ': 'punkty', 'nadtytul': 'AKT PIERWSZY',
   'naglowek': 'Podstawa programowa wychowania przedszkolnego',
   'punkty': [
     'Rozporządzenie Ministra Edukacji z **11 marca 2026 r.**',
     '**Dz.U. 2026 poz. 378**',
     'Obowiązuje od **1 września** i obejmuje od razu **wszystkie grupy wiekowe**.',
   ],
 }),
 ('P1-08', [8], {
   'typ': 'tabela', 'nadtytul': 'CO SIĘ ZMIENIŁO',
   'naglowek': 'Cztery obszary rozwoju → dziewięć obszarów osiągnięć',
   'naglowki': ['Było — cztery obszary rozwoju', 'Jest — dziewięć obszarów osiągnięć dziecka'],
   'szerokosci': [38, 62],
   'wiersze': [
     ['fizyczny', 'społeczny · osobisty · językowy'],
     ['emocjonalny', 'matematyczny · przyrodniczy · techniczny'],
     ['społeczny', 'cyfrowy · artystyczny · ruchowy'],
     ['poznawczy', 'oraz **doświadczenia edukacyjne** i **zadania przedszkola**'],
   ],
 }),
 ('P1-09', [9], {
   'typ': 'punkty', 'nadtytul': 'SKUTEK DLA DOKUMENTACJI',
   'naglowek': 'Każde narzędzie odsyła do nowej podstawy',
   'punkty': [
     'Każde narzędzie obserwacyjne **odsyła teraz do nowej podstawy programowej**.',
     'W kwestionariuszu przy **każdym twierdzeniu** stoi punkt nowej podstawy.',
   ],
 }),
 ('P1-10', [10, 11], {
   'typ': 'punkty', 'nadtytul': 'AKT DRUGI — NAJWAŻNIEJSZY W TYM ROKU',
   'naglowek': 'Orzeczenia i opinie zespołów orzekających',
   'punkty': [
     'Rozporządzenie Ministra Edukacji z **2 marca 2026 r.**',
     '**Dz.U. 2026 poz. 428**',
     'Weszło w życie **14 kwietnia**.',
     'Przepisy dotyczące przedszkola — **§ 7 ust. 6 i 7 oraz § 8** — obowiązują od **1 września**.',
   ],
 }),
 ('P1-11', [12], {
   'typ': 'punkty', 'nadtytul': 'CO TO OZNACZA DLA NAS',
   'naglowek': 'Ocena funkcjonalna i opinia przedszkola',
   'punkty': [
     '**Ocena funkcjonalna** dziecka staje się obowiązkowym etapem przed wydaniem orzeczenia.',
     'Przedszkole wydaje **opinię o funkcjonowaniu dziecka** — na prośbę przewodniczącego zespołu orzekającego.',
     'Opinia opisuje trudności, ale **równie starannie mocne strony i uzdolnienia**.',
     'Przepis wprost mówi, że **o dziecku piszemy także dobrze**.',
   ],
 }),
 ('P1-12', [13], {
   'typ': 'cytat',
   'naglowek': 'Termin — § 7 ust. 3',
   'tresc': 'Opinię, o której mowa w ust. 2, wydaje się w terminie **10 dni od dnia otrzymania przez dyrektora** '
            'prośby o jej wydanie.',
   'zrodlo': 'Rozporządzenie Ministra Edukacji z 2 marca 2026 r. w sprawie orzeczeń i opinii wydawanych '
             'przez zespoły orzekające (Dz.U. 2026 poz. 428), § 7 ust. 3. Kopię opinii otrzymują rodzice dziecka.',
 }),
 ('P1-13', [14], {
   'typ': 'sciezki',
   'naglowek': 'Podział ról — kto co robi?',
   'lewa': {'tytul': 'Poradnia', 'kroki': [
     'sporządza formalną ocenę funkcjonalną',
     'stawia rozpoznanie',
     'wydaje orzeczenie albo opinię']},
   'prawa': {'tytul': 'Przedszkole', 'kroki': [
     'obserwuje dziecko w codziennych sytuacjach',
     'opisuje to, co widzi — nie stawia diagnoz',
     'dostarcza rzetelnych, uporządkowanych danych']},
 }),
 ('P1-14', [15], {
   'typ': 'punkty', 'nadtytul': 'SEDNO CAŁEGO SZKOLENIA',
   'naglowek': 'Dziesięć dni to mało — jeśli zaczynamy dopiero po prośbie',
   'punkty': [
     'Arkusz obserwacji wypełniamy **we wrześniu, dla wszystkich dzieci**.',
     'Nie po to, żeby leżał w segregatorze.',
     'Po to, żeby **w dowolnym dniu roku** odpowiedzieć poradni na podstawie danych — spokojnie i na czas.',
   ],
 }),
 ('P1-15', [16, 17], {
   'typ': 'punkty', 'nadtytul': 'AKT TRZECI',
   'naglowek': 'Pomoc psychologiczno-pedagogiczna',
   'punkty': [
     'Rozporządzenie Ministra Edukacji Narodowej z **9 sierpnia 2017 r.**',
     'Obowiązujący tekst jednolity: **Dz.U. 2023 poz. 1798**.',
     'I właśnie tak — **z tekstem jednolitym** — cytujemy je w dokumentach dziecka.',
   ],
 }),
 ('P1-16', [18], {
   'typ': 'obieg',
   'naglowek': 'Ścieżka pomocy — od rozpoznania do poradni',
   'przystanki': [
     {'nazwa': 'Rozpoznanie', 'opis': 'nauczyciele rozpoznają potrzeby dziecka i informują dyrektora'},
     {'nazwa': 'Pomoc', 'opis': 'w bieżącej pracy oraz w formach zajęć'},
     {'nazwa': 'Brak poprawy', 'opis': 'mimo udzielanej pomocy nie widzimy postępu'},
     {'nazwa': 'Poradnia', 'opis': 'dyrektor, za zgodą rodziców, występuje do poradni'},
   ],
 }),
 ('P1-17', [19, 20], {
   'typ': 'tabela', 'nadtytul': 'AKT CZWARTY — KSZTAŁCENIE SPECJALNE',
   'naglowek': 'Do rozpoznania, nie do cytowania',
   'naglowki': ['Akt', 'Publikator pierwotny (tylko do rozpoznania)', 'Tekst jednolity (do cytowania)'],
   'szerokosci': [30, 35, 35],
   'wiersze': [
     ['Kształcenie specjalne', 'Dz.U. 2017 poz. 1578', '**Dz.U. 2020 poz. 1309**'],
     ['Pomoc psychologiczno-pedagogiczna', 'Dz.U. 2017 poz. 1591', '**Dz.U. 2023 poz. 1798**'],
   ],
 }),
 ('P1-18', [21], {
   'typ': 'punkty', 'nadtytul': 'TRZY OBOWIĄZKI Z TEGO ROZPORZĄDZENIA',
   'naglowek': 'Program, ocena, terminy',
   'punkty': [
     '**IPET** — indywidualny program edukacyjno-terapeutyczny dla dziecka z orzeczeniem.',
     '**WOPF** — wielospecjalistyczna ocena poziomu funkcjonowania, co najmniej **dwa razy w roku szkolnym**.',
     'Terminy: program **do 30 września** albo **w ciągu 30 dni** od złożenia orzeczenia.',
   ],
 }),
 ('P1-19', [22, 23], {
   'typ': 'punkty', 'nadtytul': 'AKT PIĄTY',
   'naglowek': 'Dokumentacja przebiegu wychowania',
   'punkty': [
     'Rozporządzenie z **25 sierpnia 2017 r.**, tekst jednolity **Dz.U. 2024 poz. 50**.',
     'Wymienia **księgę dzieci**, **dzienniki zajęć** oraz dokumentację badań i czynności uzupełniających specjalistów.',
     'W tej ostatniej kategorii mieszczą się **nasze arkusze obserwacji**.',
   ],
 }),
 ('P1-20', [24], {
   'typ': 'druk', 'nadtytul': 'NARZĘDZIE WEWNĘTRZNE',
   'naglowek': 'Metryczka dziecka — wprowadzana zarządzeniem dyrektora',
   'plik': DRUKI + 'metryczka_metryczka-dziecka.png',
   'opis': 'Porządkuje dane, które i tak gromadzimy z innych tytułów. Wszystko, co dotyczy dziecka, w jednym miejscu.',
 }),
 ('P1-21', [25, 26], {
   'typ': 'punkty', 'nadtytul': 'DWA AKTY, KTÓRE STOJĄ NAD WSZYSTKIMI',
   'naglowek': 'Prawo oświatowe i ochrona danych',
   'punkty': [
     'Ustawa **Prawo oświatowe** — tekst jednolity **Dz.U. 2026 poz. 820**.',
     'Rozporządzenie o ochronie danych osobowych — **RODO**.',
     'Dane o zdrowiu i rozwoju dziecka to **dane szczególnej kategorii**.',
     'Teczka dziecka ma **swoje bezpieczne miejsce**, a klauzula informacyjna jest **podpisana przez rodzica**.',
   ],
 }),
 ('P1-22', [27, 28], {
   'typ': 'domkniecie',
   'naglowek': 'Trzy zdania na koniec modułu',
   'zdania': [
     'Każdy druk ma swój przepis — i my go znamy.',
     'Obserwacja wyprzedza pismo z poradni: wrześniowy arkusz daje nam spokój na cały rok.',
     'Przepisy sprawdzamy w Dzienniku Ustaw, zanim wpiszemy je do dokumentu dziecka.',
   ],
 }),
]

# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 2

PLAN_2 = [
 ('P2-01', [0], {
   'typ': 'tytulModulu', 'numer': '2', 'czas': '5:36',
   'tytul': 'Obieg dokumentów',
   'podtytul': 'Cała dokumentacja z lotu ptaka — jak jeden dokument wynika z drugiego?',
 }),
 ('P2-02', [1], {
   'typ': 'punkty', 'nadtytul': 'PO TYM MODULE',
   'naglowek': 'Będą Państwo wiedzieć trzy rzeczy',
   'punkty': [
     'Jakie dokumenty **tworzymy w ciągu roku** szkolnego.',
     'W jakiej **kolejności** one powstają.',
     'Dlaczego **żaden z nich nie powstaje osobno**.',
   ],
 }),
 ('P2-03', [2], {
   'typ': 'punkty', 'nadtytul': 'NAJWAŻNIEJSZE ZDANIE TEGO SZKOLENIA',
   'naglowek': 'Dokumentacja dziecka to jeden obieg',
   'punkty': [
     'Każdy dokument **bierze dane z poprzedniego**.',
     'Jeśli którykolwiek etap pominiemy, następny trzeba wypełniać **z pamięci**.',
     'A dokumentacja wypełniana z pamięci **nie służy ani dziecku, ani nam**.',
   ],
 }),
 ('P2-04', [3], {
   'typ': 'obieg',
   'naglowek': 'Sześć przystanków obiegu',
   'przystanki': [
     {'nazwa': 'Metryczka', 'opis': 'dane, zdrowie, wsparcie'},
     {'nazwa': 'KPOF', 'opis': 'przesiew — gdzie?'},
     {'nazwa': 'Obserwacja pogłębiona', 'opis': 'dlaczego?'},
     {'nazwa': 'WOPF', 'opis': 'ocena scalająca'},
     {'nazwa': 'IPET', 'opis': 'program i cele'},
     {'nazwa': 'Ewaluacja', 'opis': 'decyzja i powrót'},
   ],
 }),
 ('P2-05', [4, 5], {
   'typ': 'druk', 'nadtytul': 'PRZYSTANEK PIERWSZY',
   'naglowek': 'Metryczka dziecka',
   'plik': DRUKI + 'metryczka_metryczka-dziecka.png',
   'opis': 'Odpowiada na pytanie, czy dziecko ma orzeczenie, opinię lub inną formę wsparcia — i od kiedy. '
           'Ta data uruchamia trzydziestodniowy termin na program.',
 }),
 ('P2-06', [6, 7], {
   'typ': 'druk', 'nadtytul': 'PRZYSTANEK DRUGI',
   'naglowek': 'Kwestionariusz Przedszkolnej Oceny Funkcjonalnej (KPOF)',
   'plik': DRUKI + 'wopf_kpof-5-lat.png',
   'opis': 'Narzędzie przesiewowe dla wszystkich dzieci w grupie. Odpowiada na pytanie: gdzie? '
           'Gdzie dziecko radzi sobie dobrze, a gdzie potrzebuje naszej pomocy.',
 }),
 ('P2-07', [8, 9], {
   'typ': 'tabela', 'nadtytul': 'PRZYSTANEK TRZECI',
   'naglowek': 'Obserwacja pogłębiona — cztery narzędzia',
   'naglowki': ['Narzędzie', 'Na jakie pytanie odpowiada'],
   'szerokosci': [38, 62],
   'wiersze': [
     ['Model ABC', 'co poprzedza zachowanie i co po nim następuje?'],
     ['Profil sensoryczny', 'jak dziecko reaguje na bodźce w siedmiu układach?'],
     ['Karta obserwacji mowy', 'czy dziecko nas rozumie i czy potrafi się porozumieć?'],
     ['Obserwacja teorii umysłu', 'czy dziecko rozumie, że inni myślą i czują inaczej?'],
   ],
 }),
 ('P2-08', [10, 11], {
   'typ': 'druk', 'nadtytul': 'PRZYSTANEK CZWARTY',
   'naglowek': 'Wielospecjalistyczna ocena poziomu funkcjonowania',
   'plik': DRUKI + 'wopf_wopf-ocena-poziomu-funkcjonowania.png',
   'opis': 'Scala profil z kwestionariusza, wnioski z obserwacji pogłębionej, treść orzeczenia, '
           'informacje od rodziców i efekty dotychczasowego wsparcia.',
 }),
 ('P2-09', [12, 13], {
   'typ': 'druk', 'nadtytul': 'PRZYSTANEK PIĄTY',
   'naglowek': 'Indywidualny program edukacyjno-terapeutyczny',
   'plik': DRUKI + 'ipet_program-wsparcia_ipet-caly.png',
   'opis': 'Program wynika z oceny zdanie po zdaniu. Jeśli czegoś nie ma w ocenie, nie może pojawić się w programie.',
 }),
 ('P2-10', [14, 15], {
   'typ': 'druk', 'nadtytul': 'PRZYSTANEK SZÓSTY',
   'naglowek': 'Ewaluacja',
   'plik': DRUKI + 'ewaluacja_ewaluacja-polrocza.png',
   'opis': 'Nie wymaga nowych narzędzi — wskaźnik został zapisany wcześniej, w celu SMART. '
           'Decyzja wraca do przystanku czwartego i obieg zaczyna się od nowa.',
 }),
 ('P2-11', [16, 17], {
   'typ': 'druk', 'nadtytul': 'OBOK OBIEGU',
   'naglowek': 'Opinia o funkcjonowaniu dziecka dla poradni',
   'plik': DRUKI + 'wopf_opinia-do-poradni.png',
   'opis': 'Nie piszemy jej od zera. Mocne strony z kwestionariusza, trudności z obserwacji pogłębionej, '
           'efekty wsparcia z karty ewaluacji, współpraca z rodzicami z rejestru w metryczce.',
 }),
 ('P2-12', [18], {
   'typ': 'domkniecie',
   'naglowek': 'Sześć przystanków, zawsze w tym samym porządku',
   'zdania': [
     'Metryczka, kwestionariusz, obserwacja pogłębiona, ocena, program, ewaluacja.',
     'Najpierw po co dokument powstaje, potem jak go stworzyć.',
     'Na końcu jak go wypełnić, krok po kroku, na Państwa drukach.',
   ],
 }),
]

# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 3

PLAN_3 = [
 ('P3-01', [0], {
   'typ': 'tytulModulu', 'numer': '3', 'czas': '5:45',
   'tytul': 'Metryczka dziecka',
   'podtytul': 'Pierwszy dokument, który wypełniamy we wrześniu',
 }),
 ('P3-02', [1], {
   'typ': 'punkty', 'nadtytul': 'PO TYM MODULE',
   'naglowek': 'Będą Państwo potrafili',
   'punkty': [
     'Uzasadnić, **po co** prowadzimy metryczkę.',
     'Wypełnić ją **bez zbierania danych nadmiarowych**.',
     'Odczytać z niej w **kilkanaście sekund** trzy najważniejsze informacje.',
   ],
 }),
 ('P3-03', [2], {
   'typ': 'punkty', 'nadtytul': 'CZYM JEST METRYCZKA',
   'naglowek': 'Karta danych, która gromadzi to, co i tak musimy posiadać',
   'punkty': [
     'Dane osobowe, kontakty do rodziców, upoważnienia do odbioru.',
     'Informacje o zdrowiu oraz spis dokumentacji wsparcia.',
     'Jest **naszym narzędziem wewnętrznym**, wprowadzonym zarządzeniem dyrektora.',
     'Powstała po to, żeby **oszczędzać czas i chronić dziecko**.',
   ],
 }),
 ('P3-04', [3, 4, 5, 6, 7, 8], {
   'typ': 'tabela', 'nadtytul': 'ZASADNOŚĆ METRYCZKI',
   'naglowek': 'Pięć powodów, dla których ją prowadzimy',
   'naglowki': ['Powód', 'Co to znaczy w praktyce'],
   'szerokosci': [30, 70],
   'wiersze': [
     ['1 · Jedno miejsce', 'nauczycielka na zastępstwie otwiera **jedną kartę**, a nie siedem segregatorów'],
     ['2 · Bezpieczeństwo', 'osoby upoważnione, alergie, leki, dieta — **dokument operacyjny**'],
     ['3 · Punkt wyjścia', 'sekcja 7: orzeczenie, opinia, WWR i **od kiedy** — start **30-dniowego terminu**'],
     ['4 · Współpraca', 'rejestr kontaktów potwierdza, że informowaliśmy, konsultowaliśmy i ustalaliśmy'],
     ['5 · Zgodność z RODO', 'klauzula informacyjna **podpisana przez rodzica**'],
   ],
 }),
 ('P3-05', [9, 10], {
   'typ': 'druk', 'nadtytul': 'SEKCJA 1 · DANE OSOBOWE',
   'naglowek': 'Czego w metryczce NIE wpisujemy?',
   'plik': DRUKI + 'metryczka_metryczka-dziecka.png',
   'opis': 'Numeru PESEL nie wpisujemy — jest w księdze dzieci i nie powielamy go w kolejnym dokumencie '
           '(zasada minimalizacji danych). Numer w księdze dzieci przepisujemy z ewidencji przedszkola.',
 }),
 ('P3-06', [11], {
   'typ': 'punkty', 'nadtytul': 'SEKCJA 2 · ORGANIZACJA POBYTU',
   'naglowek': 'Grupa, data przyjęcia, godziny, posiłki',
   'punkty': [
     'Zwróćmy uwagę na pole **rocznego obowiązkowego przygotowania przedszkolnego**.',
     'Od niego zależy, czy **w kwietniu wydajemy informację o gotowości szkolnej**.',
   ],
 }),
 ('P3-07', [12, 13], {
   'typ': 'punkty', 'nadtytul': 'SEKCJE 3, 4 I 5 — WYPEŁNIAMY Z RODZICAMI',
   'naglowek': 'Rodzice, kontakty, odbiór dziecka',
   'punkty': [
     'Imiona i nazwiska rodziców, telefony i **preferowana forma kontaktu**.',
     'Osoby **upoważnione do odbioru**.',
     '**Kolejność powiadamiania** w nagłych wypadkach.',
   ],
 }),
 ('P3-08', [14], {
   'typ': 'punkty', 'nadtytul': 'ZASADA JEST JEDNA',
   'naglowek': 'Komu wydajemy dziecko?',
   'punkty': [
     'Wyłącznie **rodzicom** albo osobom **pisemnie przez nich upoważnionym**.',
     'Po **okazaniu dokumentu tożsamości**.',
     'Zmianę listy rodzic zgłasza **na piśmie**.',
     'Poprzedni wpis **pozostaje w dokumentacji** z datą wykreślenia.',
   ],
 }),
 ('P3-09', [15], {
   'typ': 'druk', 'nadtytul': 'SEKCJA 6 · ZDROWIE I FUNKCJONOWANIE',
   'naglowek': 'Podawanie leku — na jakiej podstawie?',
   'plik': DRUKI + 'metryczka_metryczka-dziecka.png',
   'opis': 'Nie chodzi o przepis ustawy — takiego przepisu dla przedszkola nie ma. Chodzi o trzy dokumenty: '
           'pisemne upoważnienie rodziców (lek, dawka, godziny), dobrowolną pisemną zgodę nauczyciela '
           'oraz procedurę przyjętą zarządzeniem dyrektora. Bez tego kompletu leku nie podajemy.',
 }),
 ('P3-10', [16], {
   'typ': 'punkty', 'nadtytul': 'SEKCJA 7 · OBJĘCIE WSPARCIEM',
   'naglowek': 'Numer i data dokumentu, nie tylko zaznaczenie',
   'punkty': [
     'Przy każdej formie wsparcia wpisujemy **numer i datę dokumentu**.',
     'Przy orzeczeniu wpisujemy także **podstawę jego wydania** — rodzaj niepełnosprawności lub schorzenie.',
     'Data mówi nam, **kiedy mija trzydzieści dni**.',
   ],
 }),
 ('P3-11', [17], {
   'typ': 'punkty', 'nadtytul': 'SEKCJA 11 · REJESTR KONTAKTÓW',
   'naglowek': 'Data, forma, temat, ustalenia, podpis',
   'punkty': [
     'Notujemy rozmowę, telefon, spotkanie zespołu.',
     'Ten rejestr **zasili później informację dla poradni**.',
   ],
 }),
 ('P3-12', [18, 19], {
   'typ': 'punkty', 'nadtytul': 'TRZY DOBRE PRAKTYKI',
   'naglowek': 'Co robimy z metryczką przez cały rok?',
   'punkty': [
     'Zbieramy **tylko te dane**, które są potrzebne do realizacji zadań przedszkola.',
     '**Aktualizujemy** przy każdej zmianie zgłoszonej przez rodzica — **z datą**.',
     'Przechowujemy w miejscu wskazanym zarządzeniem dyrektora — zawiera **dane szczególnej kategorii**.',
   ],
 }),
 ('P3-13', [20], {
   'typ': 'domkniecie',
   'naglowek': 'Metryczka jest gotowa, gdy odpowiada na trzy pytania',
   'zdania': [
     'Kogo wezwać?',
     'Co podać?',
     'Od kiedy liczyć termin?',
   ],
 }),
]

# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 4

PLAN_4 = [
 ('P4-01', [0], {
   'typ': 'tytulModulu', 'numer': '4', 'czas': '10:08',
   'tytul': 'KPOF',
   'podtytul': 'Kwestionariusz Przedszkolnej Oceny Funkcjonalnej — serce całej dokumentacji',
 }),
 ('P4-02', [1], {
   'typ': 'punkty', 'nadtytul': 'PO TYM MODULE',
   'naglowek': 'Będą Państwo znać',
   'punkty': [
     '**Budowę arkusza** — trzy wersje wiekowe.',
     'Zasady **rzetelnej obserwacji**.',
     'Sposób **obliczania wyniku**.',
     'Sposób **odczytu profilu** dziecka.',
   ],
 }),
 ('P4-03', [2], {
   'typ': 'punkty', 'nadtytul': 'CZYM JEST KWESTIONARIUSZ',
   'naglowek': 'Narzędzie kryterialne, nie test',
   'punkty': [
     'Opisuje funkcjonowanie dziecka w **dziewięciu obszarach ICF**.',
     'W codziennych sytuacjach **w przedszkolu i w domu**.',
     'Zbudowany na **nowej podstawie programowej**.',
     'Przy każdym twierdzeniu stoi **kod klasyfikacji i punkt podstawy**.',
   ],
 }),
 ('P4-04', [3], {
   'typ': 'punkty', 'nadtytul': 'KLASYFIKACJA, KTÓRA PORZĄDKUJE CAŁĄ DOKUMENTACJĘ',
   'naglowek': 'Czym jest ICF?',
   'punkty': [
     'Międzynarodowa Klasyfikacja **Funkcjonowania, Niepełnosprawności i Zdrowia**.',
     'Światowa Organizacja Zdrowia, **2001 rok**.',
     '**Nie opisuje choroby ani rozpoznania.**',
     'Opisuje, **jak człowiek funkcjonuje**: co robi, w czym uczestniczy i co w otoczeniu mu pomaga albo przeszkadza.',
   ],
 }),
 ('P4-05', [4], {
   'typ': 'druk', 'nadtytul': 'MODEL BIOPSYCHOSPOŁECZNY',
   'naglowek': 'Funkcjonowanie to wypadkowa trzech rzeczy',
   'plik': DRUKI + 'wopf_profil-biopsychospoleczny-icf.png',
   'opis': 'Stan zdrowia i funkcje ciała · aktywność i uczestniczenie · czynniki środowiskowe i osobowe. '
           'Dwoje dzieci z tym samym rozpoznaniem może funkcjonować zupełnie inaczej.',
 }),
 ('P4-06', [5], {
   'typ': 'cytat',
   'naglowek': 'Gdzie przepisy mówią o ICF?',
   'tresc': 'Opinia o funkcjonowaniu dziecka odnosi się do **aktywności i uczestniczenia** w rozumieniu '
            'Międzynarodowej Klasyfikacji Funkcjonowania, Niepełnosprawności i Zdrowia.',
   'zrodlo': 'Rozporządzenie Ministra Edukacji z 2 marca 2026 r. w sprawie orzeczeń i opinii (Dz.U. 2026 poz. 428), '
             '§ 7 ust. 7 — obowiązuje od 1 września. Dziewięć obszarów kwestionariusza to dziewięć rozdziałów '
             'aktywności i uczestniczenia: od d1 (uczenie się) do d9 (życie społeczne).',
 }),
 ('P4-07', [6], {
   'typ': 'punkty', 'nadtytul': 'CO TO ZMIENIA W OBSERWACJI',
   'naglowek': 'Trzy rzeczy',
   'punkty': [
     'Patrzymy na to, **co dziecko robi**, a nie na to, jaką ma diagnozę.',
     'Opisujemy funkcjonowanie **w konkretnym środowisku** — co w sali pomaga, a co przeszkadza.',
     'Używamy **tego samego języka, co poradnia** — nasza obserwacja jest dla niej od razu czytelna.',
   ],
 }),
 ('P4-08', [7], {
   'typ': 'punkty', 'nadtytul': 'CZYM KWESTIONARIUSZ NIE JEST',
   'naglowek': 'Trzy zastrzeżenia',
   'punkty': [
     '**Nie jest diagnozą** i nie zastępuje badania psychologicznego, logopedycznego ani lekarskiego.',
     '**Nie jest testem z normami.**',
     'Jest **uporządkowanym zapisem naszej obserwacji** i punktem wyjścia do decyzji zespołu.',
   ],
 }),
 ('P4-09', [8], {
   'typ': 'tabela', 'nadtytul': 'TRZY WERSJE ARKUSZA',
   'naglowek': 'O wyborze wersji decyduje wiek rozwojowy',
   'naglowki': ['Wersja', 'Dla kogo', 'Liczba twierdzeń'],
   'szerokosci': [22, 52, 26],
   'wiersze': [
     ['A', 'dzieci 3- i 4-letnie', '**42**'],
     ['B', 'pięciolatki', '**44**'],
     ['C', 'sześciolatki', '**44**'],
     ['', 'Dziecko sześcioletnie z głęboką niepełnosprawnością obserwujemy **wersją A** — '
          'bo tylko ona da nam użyteczną informację.', ''],
   ],
 }),
 ('P4-10', [9, 10], {
   'typ': 'tabela', 'nadtytul': 'SKALA',
   'naglowek': 'Sześć wartości — zaznaczamy zawsze jedną',
   'naglowki': ['Ocena', 'Co oznacza'],
   'szerokosci': [18, 82],
   'wiersze': [
     ['1', 'zachowanie występuje w niewielkim stopniu, **nawet przy pełnym wsparciu**'],
     ['2', 'pojawia się rzadko i tylko **z dużą pomocą dorosłego**'],
     ['3', 'pojawia się **niesystematycznie** — umiejętność w trakcie kształtowania'],
     ['4', 'dziecko radzi sobie **zwykle samodzielnie**'],
     ['5', 'robi to **samodzielnie, pewnie i powtarzalnie** — mocna strona dziecka'],
   ],
 }),
 ('P4-11', [11], {
   'typ': 'punkty', 'nadtytul': 'SZÓSTA WARTOŚĆ',
   'naglowek': 'Litera N — brak możliwości obserwacji',
   'punkty': [
     'Pozycję **zostawiamy pustą**. To **pełnoprawna i uczciwa** odpowiedź.',
     'Rodzic nie widzi dziecka na zajęciach grupowych, nauczyciel nie widzi porannego ubierania w domu.',
     '**Nie zgadujemy.**',
     'Litera N **nie obniża wyniku** — nie wlicza się do średniej.',
   ],
 }),
 ('P4-12', [12, 13], {
   'typ': 'tabela', 'nadtytul': 'SIEDEM ZASAD RZETELNEJ OBSERWACJI',
   'naglowek': 'Jak wypełniamy arkusz?',
   'naglowki': ['#', 'Zasada'],
   'szerokosci': [10, 90],
   'wiersze': [
     ['1', 'Wypełniamy **cały arkusz**, wszystkie dziewięć obszarów — nie dzielimy ich między oceniających.'],
     ['2', 'Oceniamy na podstawie **dwóch do czterech tygodni** obserwacji, a nie jednego dnia.'],
     ['3', 'Wypełniamy **samodzielnie**, bez konsultowania ocen przed spotkaniem zespołu.'],
     ['4', 'Oceniamy to, **co dziecko robi**, a nie to, co potrafiłoby zrobić.'],
     ['5', 'Odnosimy się do **oczekiwań rozwojowych dla wieku** dziecka.'],
     ['6', 'Zapisujemy **obserwacje jakościowe** — zwłaszcza przy ocenach skrajnych.'],
     ['7', 'Zwracamy arkusz koordynatorowi **w umówionym terminie**.'],
   ],
 }),
 ('P4-13', [14, 15], {
   'typ': 'druk', 'nadtytul': 'PRZYKŁAD · OBSZAR PIERWSZY',
   'naglowek': 'Uczenie się i stosowanie wiedzy',
   'plik': DRUKI + 'wopf_kpof-3-4-lata.png',
   'opis': 'Twierdzenie 1: przygląda się i przysłuchuje z zainteresowaniem — obserwowane codziennie przez '
           'trzy tygodnie, zaznaczam 4. Twierdzenie 3: skupia uwagę na zabawie przez kilka minut — '
           'udaje się przy stoliku, nie udaje w kole, zaznaczam 3.',
 }),
 ('P4-14', [16], {
   'typ': 'punkty', 'nadtytul': 'PRZYKŁAD · OBSZAR TRZECI — POROZUMIEWANIE SIĘ',
   'naglowek': 'Ocena plus obserwacja jakościowa',
   'punkty': [
     'Twierdzenie 12: komunikuje potrzeby słowem, gestem lub innym czytelnym sygnałem.',
     'Dziecko komunikuje się **gestem i wokalizacją, konsekwentnie** — zaznaczam **2**.',
     'Dopisuję obserwację: *prosi o picie, wskazując kubek i wydając dźwięk*.',
     'Ta notatka trafi później **do oceny wielospecjalistycznej**.',
   ],
 }),
 ('P4-15', [17], {
   'typ': 'punkty', 'nadtytul': 'PRZYKŁAD · OBSZAR SZÓSTY — ŻYCIE DOMOWE',
   'naglowek': 'Kiedy zaznaczamy N?',
   'punkty': [
     'Jako nauczycielka **nie obserwuję**, czy dziecko pomaga w domowych czynnościach.',
     'Zaznaczam **N**.',
   ],
 }),
 ('P4-16', [18, 19], {
   'typ': 'tabela', 'nadtytul': 'LICZENIE WYNIKU',
   'naglowek': 'Średnia obszaru — bez pozycji N',
   'naglowki': ['Krok', 'Działanie', 'Przykład — obszar trzeci'],
   'szerokosci': [26, 38, 36],
   'wiersze': [
     ['Suma punktów', 'dodajemy oceny twierdzeń **ocenionych**', '11 punktów'],
     ['Liczba twierdzeń', 'liczymy tylko ocenione, **bez N**', '4 z 5'],
     ['Średnia obszaru', 'suma ÷ liczba ocenionych', '11 ÷ 4 = **2,75**'],
   ],
 }),
 ('P4-17', [20], {
   'typ': 'punkty', 'nadtytul': 'WYNIK OGÓLNY',
   'naglowek': 'Średnia ze średnich obszarów',
   'punkty': [
     'Wynik ogólny to **średnia ze średnich obszarów**.',
     'Obszar szósty ma charakter **opisowy** i **nie wlicza się** do wyniku ogólnego.',
   ],
 }),
 ('P4-18', [21], {
   'typ': 'tabela', 'nadtytul': 'PROGI KRYTERIALNE',
   'naglowek': 'Cztery poziomy',
   'naglowki': ['Średnia', 'Poziom', 'Co robimy'],
   'szerokosci': [22, 30, 48],
   'wiersze': [
     ['4,0 – 5,0', '**Zasób**', 'mocna strona dziecka — nazywamy ją w ocenie'],
     ['3,0 – 3,9', '**Poziom 1**', 'funkcjonowanie w granicach oczekiwań'],
     ['2,0 – 2,9', '**Poziom 2**', 'trudność — działania wspierające i obserwacja pogłębiona'],
     ['poniżej 2,0', '**Poziom 3**', 'nasilona trudność — ocena wielospecjalistyczna i konsultacja z poradnią'],
   ],
 }),
 ('P4-19', [22], {
   'typ': 'punkty', 'nadtytul': 'REGUŁA NADRZĘDNA',
   'naglowek': 'Średnia potrafi zamaskować pojedynczą trudność',
   'punkty': [
     'Każde twierdzenie ocenione na **1 lub 2** podlega analizie zespołu — **niezależnie od średniej obszaru**.',
     'Dziecko może mieć w obszarze komunikacji średnią **3,8**, a jednocześnie **jedynkę** przy komunikowaniu potrzeb.',
     'Średnia to zamaskuje. **Reguła nadrzędna nie pozwoli tego przeoczyć.**',
   ],
 }),
 ('P4-20', [23], {
   'typ': 'punkty', 'nadtytul': 'ODCZYT PROFILU',
   'naglowek': 'Trzy kroki',
   'punkty': [
     '**Kolor**: zielony to zasób i poziom 1, żółty to poziom 2, czerwony to poziom 3.',
     '**Kształt**: profil płaski i niski — trudność globalna; jedno głębokie wcięcie — trudność wybiórcza.',
     '**Pojedyncze twierdzenia** ocenione nisko — także w obszarach zielonych.',
   ],
 }),
 ('P4-21', [24], {
   'typ': 'sciezki',
   'naglowek': 'Trzy arkusze na jedno dziecko — co robimy z rozbieżnością?',
   'lewa': {'tytul': 'W domu wyżej niż w przedszkolu', 'kroki': [
     'szukamy barier w sali',
     'sprawdzamy hałas, światło, liczbę bodźców',
     'pytamy rodziców, co działa w domu']},
   'prawa': {'tytul': 'W przedszkolu wyżej niż w domu', 'kroki': [
     'dzielimy się z rodzicami sprawdzonymi rutynami',
     'pokazujemy, jak dajemy polecenie',
     'nie uśredniamy profili — kładziemy je obok siebie']},
 }),
 ('P4-22', [25], {
   'typ': 'domkniecie',
   'naglowek': 'Kwestionariusz wypełniamy dwa razy w roku',
   'zdania': [
     'Wrzesień — pomiar bazowy, także dla trzylatków; dziecko z orzeczeniem musi mieć program do 30 września.',
     'Maj — pomiar kontrolny, na tym samym arkuszu, innym kolorem.',
     'Wtedy widać drogę, którą dziecko przeszło.',
   ],
 }),
]

# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 5

PLAN_5 = [
 ('P5-01', [0], {
   'typ': 'tytulModulu', 'numer': '5', 'czas': '9:46',
   'tytul': 'Obserwacja pogłębiona',
   'podtytul': 'Kwestionariusz powiedział gdzie. Obserwacja pogłębiona odpowiada na pytanie: dlaczego?',
 }),
 ('P5-02', [1], {
   'typ': 'punkty', 'nadtytul': 'PO TYM MODULE',
   'naglowek': 'Będą Państwo wiedzieć',
   'punkty': [
     '**Kiedy** uruchamiamy obserwację pogłębioną.',
     'Które z **czterech narzędzi** wybrać.',
     'Gdzie przebiega **granica kompetencji nauczyciela**.',
   ],
 }),
 ('P5-03', [2], {
   'typ': 'sciezki',
   'naglowek': 'Przesiew a obserwacja pogłębiona',
   'lewa': {'tytul': 'Przesiew — KPOF', 'kroki': [
     'obejmuje wszystkie dzieci w grupie',
     'dwa razy w roku',
     'odpowiada na pytanie: gdzie?']},
   'prawa': {'tytul': 'Obserwacja pogłębiona', 'kroki': [
     'obejmuje pojedyncze dziecko',
     'kilkanaście godzin pracy zespołu',
     'uruchamiamy ją z przesłanką, a nie na wszelki wypadek']},
 }),
 ('P5-04', [3, 4], {
   'typ': 'tabela', 'nadtytul': 'SZEŚĆ REGUŁ PRZEKIEROWANIA',
   'naglowek': 'Wystarczy jedna, aby zespół usiadł nad kartą decyzyjną',
   'naglowki': ['#', 'Reguła'],
   'szerokosci': [10, 90],
   'wiersze': [
     ['1', 'średnia któregokolwiek obszaru **poniżej 2,0**'],
     ['2', '**dwa lub więcej** twierdzeń ocenionych na 1 lub 2 w tym samym obszarze'],
     ['3', 'rozbieżność między oceniającymi **1,5 punktu lub więcej**'],
     ['4', '**sygnał zdrowotny z metryczki** — na przykład nadwrażliwość sensoryczna'],
     ['5', 'zachowanie powtarzalne, które **zagraża** dziecku lub innym — obserwację uruchamiamy **natychmiast**'],
     ['6', 'brak poprawy mimo udzielanej pomocy przez **około trzy miesiące**'],
   ],
 }),
 ('P5-05', [5], {
   'typ': 'punkty', 'nadtytul': 'SKĄD SIĘ BIORĄ TE REGUŁY',
   'naglowek': 'To nasza decyzja jako rady pedagogicznej',
   'punkty': [
     'Reguły wpisujemy **do procedury przedszkola**.',
     'Przepis wymaga **rozpoznawania potrzeb i oceny efektywności**.',
     'Reguły sprawiają, że decyzja **nie zależy od tego, kto danego dnia patrzy na arkusz**.',
   ],
 }),
 ('P5-06', [6, 7], {
   'typ': 'tabela', 'nadtytul': 'CZTERY NARZĘDZIA',
   'naglowek': 'Każde odpowiada na inne pytanie',
   'naglowki': ['Narzędzie', 'Pytanie', 'Kiedy je wybieramy'],
   'szerokosci': [26, 30, 44],
   'wiersze': [
     ['Model ABC', 'co poprzedza i co następuje?', 'zachowanie powtarzalne, zagrażające lub przerywające zajęcia'],
     ['Profil sensoryczny', 'jak reaguje na bodźce?', 'sygnał z metryczki, niskie oceny w dbaniu o siebie i poruszaniu'],
     ['Teoria umysłu', 'czy rozumie innych?', 'niski obszar relacji przy zachowanych pozostałych'],
     ['Karta mowy', 'czy rozumie i czy potrafi powiedzieć?', 'niski obszar porozumiewania się'],
   ],
 }),
 ('P5-07', [8], {
   'typ': 'tabela', 'nadtytul': 'NARZĘDZIE PIERWSZE · MODEL ABC',
   'naglowek': 'Trzy litery',
   'naglowki': ['Litera', 'Co oznacza'],
   'szerokosci': [18, 82],
   'wiersze': [
     ['A', '**poprzednik** — to, co działo się bezpośrednio przed zachowaniem'],
     ['B', '**zachowanie** — opisane obserwowalnie i mierzalnie'],
     ['C', '**następstwo** — to, co stało się bezpośrednio potem, w tym reakcja dorosłych'],
   ],
 }),
 ('P5-08', [9], {
   'typ': 'punkty', 'nadtytul': 'PRZYKŁAD POPRAWNEGO ZAPISU',
   'naglowek': 'Każde zdanie da się sprawdzić',
   'punkty': [
     '**A** — nauczycielka ogłosiła sprzątanie zabawek; dziecko od sześciu minut budowało wieżę z klocków.',
     '**B** — rzuciło dwa klocki w kierunku półki i krzyczało przez około czterdzieści sekund.',
     '**C** — nauczycielka przykucnęła obok i nie odbierała klocków; po dwóch minutach dziecko dokończyło wieżę.',
     '**Żadne zdanie nie zawiera interpretacji.**',
   ],
 }),
 ('P5-09', [10], {
   'typ': 'druk', 'nadtytul': 'JAK PROWADZIMY REJESTR ABC',
   'naglowek': 'Dziesięć do piętnastu zapisów w ciągu dwóch–trzech tygodni',
   'plik': DRUKI + 'wopf_abc-rejestr-zdarzen.png',
   'opis': 'Szukamy funkcji zachowania: uzyskania uwagi, uzyskania przedmiotu, uniknięcia trudnego zadania '
           'albo regulacji pobudzenia. Interpretację formułujemy dopiero na spotkaniu zespołu.',
 }),
 ('P5-10', [11, 12], {
   'typ': 'druk', 'nadtytul': 'NARZĘDZIE DRUGIE',
   'naglowek': 'Profil sensoryczny — siedem układów',
   'plik': DRUKI + 'wopf_profil-sensoryczny.png',
   'opis': 'Słuchowy, wzrokowy, dotykowy, węchowy, smakowy, przedsionkowy i proprioceptywny. '
           'Opisujemy wzorzec, nie stawiamy rozpoznania.',
 }),
 ('P5-11', [13], {
   'typ': 'tabela', 'nadtytul': 'TRZY WZORCE',
   'naglowek': 'Co obserwujemy w sali?',
   'naglowki': ['Wzorzec', 'Jak wygląda w przedszkolu'],
   'szerokosci': [26, 74],
   'wiersze': [
     ['Nadreaktywność', 'zakrywa uszy przy hałasie, odsuwa się w kolejce, nie znosi metek, odmawia potraw o określonej konsystencji'],
     ['Podreaktywność', 'nie reaguje na wołanie mimo prawidłowego słuchu, nie zauważa mokrych rękawów, wolno rozpoczyna czynności'],
     ['Poszukiwanie bodźców', 'wspina się i zeskakuje, wpada na przedmioty, gryzie ubrania, mówi bardzo głośno'],
   ],
 }),
 ('P5-12', [14], {
   'typ': 'punkty', 'nadtytul': 'GRANICA KOMPETENCJI',
   'naglowek': 'Co wolno nauczycielowi, a co należy do terapeuty?',
   'punkty': [
     'Nauczyciel **opisuje obserwowane reakcje**.',
     'Rozpoznanie i kwalifikacja do terapii należą do **terapeuty integracji sensorycznej**.',
     'W dokumentacji piszemy: *obserwowany wzorzec poszukiwania bodźców, wskazana konsultacja specjalisty*.',
   ],
 }),
 ('P5-13', [15, 16], {
   'typ': 'druk', 'nadtytul': 'NARZĘDZIE TRZECIE',
   'naglowek': 'Teoria umysłu',
   'plik': DRUKI + 'wopf_tom.png',
   'opis': 'Zdolność przypisywania sobie i innym stanów umysłu — wiedzy, przekonań, intencji i emocji — '
           'oraz rozumienia, że mogą różnić się od naszych. Fundament zabawy na niby, współpracy, żartu i empatii.',
 }),
 ('P5-14', [17], {
   'typ': 'tabela', 'nadtytul': 'KIEDY TAKA OBSERWACJA JEST POTRZEBNA',
   'naglowek': 'Sześć sygnałów',
   'naglowki': ['#', 'Sygnał'],
   'szerokosci': [10, 90],
   'wiersze': [
     ['1', 'obszar relacji **wyraźnie niższy** przy zachowanych obszarach uczenia się i poruszania'],
     ['2', 'trudność w odczytywaniu **mimiki, gestu i tonu głosu**'],
     ['3', 'nie podejmuje **zabawy na niby** mimo odpowiedniego wieku'],
     ['4', 'rozumie język **dosłownie**'],
     ['5', 'wskazuje palcem **tylko po to, żeby coś otrzymać** — nie po to, by podzielić się uwagą'],
     ['6', 'zespół rozważa **wystąpienie do poradni** w sprawie całościowych zaburzeń rozwoju'],
   ],
 }),
 ('P5-15', [18], {
   'typ': 'punkty', 'nadtytul': 'WIEK MA ZASADNICZE ZNACZENIE',
   'naglowek': 'Czego nie wolno pomylić z trudnością?',
   'punkty': [
     'Zadania **fałszywego przekonania** rozwiązują dzieci typowo rozwijające się **od około czwartego roku życia**.',
     'U trzylatka niepowodzenie jest **rozwojowo typowe**.',
     'U młodszych dzieci obserwujemy **wskaźniki wczesne**: uwagę wspólną, wskazywanie „żeby pokazać", '
     'sprawdzanie miny dorosłego, początki zabawy symbolicznej.',
   ],
 }),
 ('P5-16', [19], {
   'typ': 'punkty', 'nadtytul': 'GRANICA KOMPETENCJI',
   'naglowek': 'Obserwacja opisuje zachowania',
   'punkty': [
     '**Nie jest testem** i **nie prowadzi do rozpoznania**.',
     'Prowadzi do **rzetelnego opisu**, który przekażemy poradni.',
   ],
 }),
 ('P5-17', [20, 21], {
   'typ': 'punkty', 'nadtytul': 'NARZĘDZIE CZWARTE',
   'naglowek': 'Karta obserwacji rozwoju mowy i komunikacji',
   'punkty': [
     'Dziecko, które **nie rozumie polecenia**, wygląda na nieposłuszne.',
     'Dziecko, które **nie potrafi powiedzieć, czego chce**, krzyczy albo uderza.',
     'Zanim uznamy, że problem leży w zachowaniu — sprawdzamy, **czy dziecko nas rozumie**.',
   ],
 }),
 ('P5-18', [22], {
   'typ': 'druk', 'nadtytul': 'BUDOWA KARTY',
   'naglowek': 'Pięć obszarów, 25 wskaźników, skala 0–2',
   'plik': DRUKI + 'wopf_mowa.png',
   'opis': 'Rozumienie mowy · mowa czynna i artykulacja · słuch fonematyczny · słownictwo i gramatyka · '
           'komunikacja i budowanie wypowiedzi. 0 — nie występuje, 1 — częściowo lub z pomocą, 2 — samodzielnie. '
           'Każdy obszar daje wynik od 0 do 10 punktów.',
 }),
 ('P5-19', [23], {
   'typ': 'punkty', 'nadtytul': 'KIEDY URUCHAMIAMY KARTĘ MOWY',
   'naglowek': 'Cztery przesłanki',
   'punkty': [
     'W kwestionariuszu obszar **porozumiewania się jest niski**.',
     'Dziecko **nie mówi** albo mówi tak, że rozumie je **tylko najbliższa rodzina**.',
     'Nie wykonuje **prostych poleceń** mimo prawidłowego słuchu.',
     'Podejrzewamy, że za zachowaniem trudnym stoi **brak możliwości porozumienia się**.',
   ],
 }),
 ('P5-20', [24], {
   'typ': 'punkty', 'nadtytul': 'PRZYKŁAD · ROZUMIENIE MOWY',
   'naglowek': 'Obszar rozumienia — osiem punktów',
   'punkty': [
     'Reaguje na imię, wykonuje proste i dwuetapowe polecenia **samodzielnie** — zaznaczamy **2**.',
     'Nazwane obrazki wskazuje i na proste pytania odpowiada **częściowo, z pomocą** — zaznaczamy **1**.',
     'Obszar rozumienia daje **8 punktów**.',
   ],
 }),
 ('P5-21', [25], {
   'typ': 'punkty', 'nadtytul': 'PRZYKŁAD · MOWA CZYNNA I SŁUCH FONEMATYCZNY',
   'naglowek': 'Sześć punktów i trzy punkty',
   'punkty': [
     'Wypowiada pojedyncze słowa, ale łączy je w wypowiedź **tylko z pomocą**.',
     'Pierwszej głoski w słowie **jeszcze nie wyodrębnia** — zaznaczamy **0**.',
     'Mowa czynna: **6 punktów**. Słuch fonematyczny: **3 punkty**.',
   ],
 }),
 ('P5-22', [26], {
   'typ': 'tabela', 'nadtytul': 'ODCZYT WYNIKU',
   'naglowek': 'Trzy przedziały',
   'naglowki': ['Punkty', 'Odczyt', 'Co dalej'],
   'szerokosci': [20, 30, 50],
   'wiersze': [
     ['8 – 10', '**Zasób**', 'nazywamy mocną stronę w ocenie'],
     ['4 – 7', '**Obszar wymagający wsparcia**', 'cel SMART i działanie w bieżącej pracy'],
     ['0 – 3', '**Priorytet**', 'zasila cele, ocenę wielospecjalistyczną i opinię dla poradni'],
   ],
 }),
 ('P5-23', [27], {
   'typ': 'punkty', 'nadtytul': 'GRANICA KOMPETENCJI',
   'naglowek': 'Taka sama jak przy pozostałych narzędziach',
   'punkty': [
     'Nauczyciel opisuje, **co słyszy i widzi** w naturalnych sytuacjach.',
     '**Diagnoza logopedyczna należy do logopedy.**',
     'W dokumentacji piszemy: *obserwowane trudności w wyodrębnianiu głosek i w budowaniu wypowiedzi, '
     'wskazana diagnoza logopedyczna*.',
   ],
 }),
 ('P5-24', [28, 29], {
   'typ': 'domkniecie',
   'naglowek': 'Moduł zamyka karta decyzyjna — jedna na jedno dziecko',
   'zdania': [
     'Sprawdzamy sześć reguł, wybieramy narzędzie, wpisujemy: kto obserwuje, od kiedy i kiedy spotyka się zespół.',
     'Kartę wpinamy do teczki również wtedy, gdy decyzja brzmi: nie uruchamiamy.',
     'Zapis decyzji odmownej jest równie ważny jak zapis decyzji pozytywnej.',
   ],
 }),
]

# ─────────────────────────────────────────────────────────── PLAN SCEN · CZĘŚĆ 6

PLAN_6 = [
 ('P6-01', [0], {
   'typ': 'tytulModulu', 'numer': '6', 'czas': '13:12',
   'tytul': 'WOPF, IPET, ewaluacja',
   'podtytul': 'Od zebranych danych do zobowiązania — ocena, program, cele SMART, opinia dla poradni',
 }),
 ('P6-02', [1], {
   'typ': 'punkty', 'nadtytul': 'PO TYM MODULE',
   'naglowek': 'Będą Państwo potrafili',
   'punkty': [
     'Zbudować ocenę **z danych, które już mają**.',
     'Sformułować **cel mierzalny**.',
     'Zaplanować **ewaluację w kalendarzu** roku szkolnego.',
   ],
 }),
 ('P6-03', [2, 3], {
   'typ': 'cytat',
   'naglowek': 'Wielospecjalistyczna ocena poziomu funkcjonowania',
   'tresc': 'Zespół dokonuje oceny **co najmniej dwa razy w roku szkolnym**, a ocena jest podstawą '
            '**opracowania i modyfikacji programu**.',
   'zrodlo': 'Rozporządzenie MEN z 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia, wychowania '
             'i opieki dla dzieci i młodzieży niepełnosprawnych (tekst jedn. Dz.U. 2020 poz. 1309).',
 }),
 ('P6-04', [4], {
   'typ': 'tabela', 'nadtytul': 'DLACZEGO OCENA JEST TAK WAŻNA',
   'naglowek': 'Cztery powody',
   'naglowki': ['#', 'Powód'],
   'szerokosci': [10, 90],
   'wiersze': [
     ['1', 'wyznacza **punkt startu**, bez którego cele byłyby zgadywaniem'],
     ['2', 'scala perspektywy **nauczyciela, logopedy, psychologa i rodziców** w jeden obraz dziecka'],
     ['3', 'chroni dziecko **przed etykietą** — dwoje dzieci z tym samym orzeczeniem ma dwie różne oceny'],
     ['4', '**dokumentuje pracę przedszkola**'],
   ],
 }),
 ('P6-05', [5], {
   'typ': 'tabela', 'nadtytul': 'BUDOWA OCENY',
   'naglowek': 'Siedem bloków',
   'naglowki': ['#', 'Blok oceny'],
   'szerokosci': [10, 90],
   'wiersze': [
     ['1', 'Mocne strony i zasoby'],
     ['2', 'Funkcjonowanie w dziewięciu obszarach'],
     ['3', 'Trudności i ich uwarunkowania'],
     ['4', 'Bariery i ułatwienia w środowisku'],
     ['5', 'Efekty dotychczasowego wsparcia'],
     ['6', 'Potrzeby rozwojowe i edukacyjne'],
     ['7', 'Wnioski i rekomendacje'],
   ],
 }),
 ('P6-06', [6, 7], {
   'typ': 'tabela', 'nadtytul': 'SKĄD BIERZEMY TREŚĆ',
   'naglowek': 'Każdy blok ma swoje źródło',
   'naglowki': ['Blok oceny', 'Dokument źródłowy'],
   'szerokosci': [42, 58],
   'wiersze': [
     ['Mocne strony', 'oceny **najwyższe** w kwestionariuszu'],
     ['Trudności', 'oceny **najniższe** i obserwacja pogłębiona'],
     ['Bariery i ułatwienia', 'analiza **ABC** i **profil sensoryczny**'],
     ['Efekty wsparcia', 'poprzednia **karta ewaluacji**'],
   ],
 }),
 ('P6-07', [8], {
   'typ': 'punkty', 'nadtytul': 'NAZEWNICTWO',
   'naglowek': 'Pełna nazwa w dokumencie, skrót w pracy zespołu',
   'punkty': [
     'W dokumencie wpinanym do teczki: **wielospecjalistyczna ocena poziomu funkcjonowania**.',
     'W pracy zespołu możemy posługiwać się **skrótem**.',
   ],
 }),
 ('P6-08', [9, 10], {
   'typ': 'punkty', 'nadtytul': 'INDYWIDUALNY PROGRAM EDUKACYJNO-TERAPEUTYCZNY',
   'naglowek': 'Dla kogo i w jakim terminie?',
   'punkty': [
     'Dla dziecka posiadającego **orzeczenie o potrzebie kształcenia specjalnego**.',
     '**Do 30 września** — dla dziecka, które rozpoczyna kształcenie z orzeczeniem.',
     'Albo **30 dni** od złożenia orzeczenia w przedszkolu, niezależnie od miesiąca.',
   ],
 }),
 ('P6-09', [11], {
   'typ': 'punkty', 'nadtytul': 'PRAWA RODZICÓW',
   'naglowek': 'O czym musimy pamiętać?',
   'punkty': [
     'Mają prawo **uczestniczyć w spotkaniach zespołu**.',
     'Mają prawo otrzymać **kopię programu i kopię oceny**.',
     'Dyrektor **zawiadamia o terminie spotkania** w sposób przyjęty w przedszkolu.',
   ],
 }),
 ('P6-10', [12, 13], {
   'typ': 'druk', 'nadtytul': 'CO MUSI ZNALEŹĆ SIĘ W PROGRAMIE',
   'naglowek': 'Zalecenie po zaleceniu — jak je realizujemy?',
   'plik': DRUKI + 'ipet_program-wsparcia_ipet-caly.png',
   'opis': 'Do programu wpisujemy zalecenia poradni z orzeczenia, jedno po drugim, a przy każdym: w jakiej formie, '
           'kto i w jakim wymiarze. Orzeczenie mówi, co dziecku zalecono. Ocena mówi, co widzimy w przedszkolu. '
           'Program pokazuje, jak jedno i drugie zamieniamy w działanie.',
 }),
 ('P6-11', [14], {
   'typ': 'punkty', 'nadtytul': 'DOSTOSOWANIA',
   'naglowek': 'Czym są dostosowania w przedszkolu?',
   'punkty': [
     'To zmiany w tym, **jak uczymy** — a nie w tym, **czego uczymy**.',
     '**Podstawa programowa pozostaje ta sama.**',
   ],
 }),
 ('P6-12', [15], {
   'typ': 'tabela', 'nadtytul': 'PIĘĆ RODZAJÓW DOSTOSOWAŃ',
   'naglowek': 'Co konkretnie zmieniamy?',
   'naglowki': ['Zmieniamy', 'Przykłady w sali'],
   'szerokosci': [30, 70],
   'wiersze': [
     ['Sposób podania treści', 'polecenie poparte **gestem i obrazkiem**'],
     ['Czas', '**dłuższa chwila** na reakcję'],
     ['Przestrzeń', 'miejsce w kole **blisko nauczyciela**, kącik wyciszenia, **wizualny plan dnia**'],
     ['Sposób sprawdzania', 'pozwalamy **pokazać zamiast powiedzieć**'],
     ['Pomoce', 'sztućce z grubym uchwytem, słuchawki wyciszające, **obrazki do komunikacji**'],
   ],
 }),
 ('P6-13', [16, 17], {
   'typ': 'punkty', 'nadtytul': 'ZINTEGROWANE DZIAŁANIA',
   'naglowek': 'Jeden cel, jeden plan, wiele rąk',
   'punkty': [
     'Logopeda, psycholog, terapeuta i nauczyciel grupy pracują nad **tymi samymi celami z programu**.',
     '**Strategia z gabinetu przechodzi do sali** — jeśli logopeda uczy dziecko prosić gestem o picie, '
     'nauczycielka honoruje ten gest przy śniadaniu, a rodzice w domu.',
     'Zespół prowadzi **wspólny zeszyt komunikacji** i **jedną kartę ewaluacji**.',
     '**Żaden specjalista nie ma osobnych celów** w oderwaniu od programu.',
   ],
 }),
 ('P6-14', [18], {
   'typ': 'tabela', 'nadtytul': 'SALA W ŚWIETLE NOWEJ PODSTAWY',
   'naglowek': 'Uniwersalne projektowanie sali',
   'naglowki': ['Element sali', 'Jak ma wyglądać'],
   'szerokosci': [34, 66],
   'wiersze': [
     ['Strefy', 'ruchu · zabawy · przyrody i techniki · książki · sztuki · **kącik wyciszenia**'],
     ['Materiały', 'dostępne **na wysokości dziecka** i opisane **obrazkiem** — dziecko samo wybiera i odkłada'],
     ['Plan dnia', 'wisi w formie **wizualnej**'],
     ['Miejsce dziecka', 'w kole i przy stoliku — dobrane **do potrzeb sensorycznych**'],
     ['Hałas i światło', 'regulowane — to **najczęstsze bariery środowiskowe** w ocenie według ICF'],
   ],
 }),
 ('P6-15', [19, 20], {
   'typ': 'punkty', 'nadtytul': 'CELE SMART',
   'naglowek': 'Czym są cele SMART?',
   'punkty': [
     'Sposób formułowania celu: **konkretny, mierzalny, osiągalny, istotny i określony w czasie**.',
     'Nazwa to skrót od pierwszych liter w języku angielskim — *Specific, Measurable, Achievable, Relevant, Time-bound*.',
     'Metoda pochodzi **z zarządzania, z początku lat osiemdziesiątych**.',
     'W edukacji przyjęła się, bo odpowiada na potrzebę **planowania pracy i sprawdzania jej efektów**.',
   ],
 }),
 ('P6-16', [21], {
   'typ': 'punkty', 'nadtytul': 'ZASADA STRAŻNIKA PRAWA',
   'naglowek': 'Czy przepis wymaga celów SMART?',
   'punkty': [
     '**Nie.**',
     'Rozporządzenie określa **zawartość programu**: dostosowania, zintegrowane działania, formy i okres pomocy, '
     'działania wspierające rodziców, zakres współpracy.',
     'Nazwa **SMART nie pada w rozporządzeniu ani razu**.',
     '**Nie ma obowiązku** używania tego skrótu w dokumencie.',
   ],
 }),
 ('P6-17', [22], {
   'typ': 'punkty', 'nadtytul': 'CO NATOMIAST JEST WYMAGANE',
   'naglowek': 'Ocena efektywności',
   'punkty': [
     'Zespół dokonuje oceny wielospecjalistycznej **co najmniej dwa razy w roku**.',
     'Nauczyciele i specjaliści **oceniają efektywność** udzielanej pomocy.',
     'Ocenić efektywność można tylko wtedy, gdy cel ma **kryterium**, do którego da się porównać wynik.',
     '**Nazwa jest dowolna, mierzalność jest konieczna.**',
   ],
 }),
 ('P6-18', [23], {
   'typ': 'punkty', 'nadtytul': 'JAK ROZUMIEĆ CEL W PRAKTYCE PRZEDSZKOLNEJ',
   'naglowek': 'Opis zachowania, które chcemy zobaczyć za kilka tygodni',
   'punkty': [
     'Zapisany tak, żeby **dwie różne osoby**, patrząc na to samo dziecko, **oceniły go tak samo**.',
     'Zapis „rozwijanie samodzielności” wyraża intencję, ale **nie wskazuje, co ma się wydarzyć**.',
     'Cel SMART **planuje działanie i jednocześnie przygotowuje ewaluację** — '
     'kryterium zapisane w celu jest gotowym wskaźnikiem.',
   ],
 }),
 ('P6-19', [24], {
   'typ': 'tabela', 'nadtytul': 'PIĘĆ LITER',
   'naglowek': 'O co pyta każda z nich?',
   'naglowki': ['Litera', 'Znaczenie', 'Pytanie'],
   'szerokosci': [14, 30, 56],
   'wiersze': [
     ['S', 'konkretny', 'jakie zachowanie i w jakiej sytuacji?'],
     ['M', 'mierzalny', 'ile razy z ilu prób i przy jakim wsparciu?'],
     ['A', 'osiągalny', 'czy to **jeden krok** od tego, co dziecko robi dziś?'],
     ['R', 'istotny', 'czy wynika z oceny i zwiększa uczestnictwo dziecka?'],
     ['T', 'określony w czasie', 'do kiedy i kiedy sprawdzamy?'],
   ],
 }),
 ('P6-20', [25], {
   'typ': 'punkty', 'nadtytul': 'FORMUŁA CELU',
   'naglowek': 'Jedno zdanie, sześć elementów',
   'punkty': [
     '**Dziecko**, w konkretnej **sytuacji**, będzie wykonywać obserwowalne **zachowanie**,',
     'w określonej **liczbie prób**, przy określonym **wsparciu**,',
     'do określonej **daty**, z określonym **sposobem pomiaru**.',
   ],
 }),
 ('P6-21', [26], {
   'typ': 'sciezki',
   'naglowek': 'Przykład pierwszy — samoobsługa',
   'lewa': {'tytul': 'Zapis wyjściowy', 'kroki': [
     'rozwijanie samodzielności w czynnościach samoobsługowych',
     'wyraża intencję',
     'nie da się ocenić efektywności']},
   'prawa': {'tytul': 'Cel SMART', 'kroki': [
     'Zosia podczas przygotowania do wyjścia na dwór założy samodzielnie buty na rzepy',
     'w czterech z pięciu kolejnych dni, przy najwyżej jednej podpowiedzi słownej',
     'do 19 grudnia · pomiar: karta obserwacji szatni']},
 }),
 ('P6-22', [27], {
   'typ': 'sciezki',
   'naglowek': 'Przykład drugi — umiejętności społeczne',
   'lewa': {'tytul': 'Zapis wyjściowy', 'kroki': [
     'rozwijanie umiejętności społecznych',
     'nie wiadomo, co ma się wydarzyć',
     'nie wiadomo, po czym to poznamy']},
   'prawa': {'tytul': 'Cel SMART', 'kroki': [
     'Lena podejmie wspólną zabawę w parze z wyznaczonym rówieśnikiem, przyjmując przydzieloną rolę',
     'przez co najmniej pięć minut, w trzech z pięciu dni w tygodniu, przy wprowadzeniu przez dorosłego',
     'do końca kwietnia · pomiar: karta obserwacji zabawy swobodnej']},
 }),
 ('P6-23', [28, 29], {
   'typ': 'tabela', 'nadtytul': 'EWALUACJA — ILE RAZY W ROKU',
   'naglowek': 'Kalendarz roku szkolnego',
   'naglowki': ['Dokument', 'Kiedy'],
   'szerokosci': [42, 58],
   'wiersze': [
     ['Ocena wielospecjalistyczna', 'wrzesień i styczeń, **zalecana trzecia w maju**'],
     ['Modyfikacja programu', 'po każdej ocenie'],
     ['Ocena efektywności pomocy', 'styczeń i czerwiec'],
     ['Kwestionariusz KPOF', 'wrzesień i maj'],
     ['Informacja o gotowości szkolnej', 'raz, **do końca kwietnia** — wzór: Dz.U. 2023 poz. 1120'],
   ],
 }),
 ('P6-24', [30], {
   'typ': 'punkty', 'nadtytul': 'REKOMENDACJA',
   'naglowek': 'Trzy oceny i dwa krótkie przeglądy',
   'punkty': [
     'Przeglądy wskaźników **w listopadzie i w marcu**.',
     '**Piętnaście minut** na dziecko i notatka w dzienniku.',
     'Dzięki temu o nieskuteczności działania dowiadujemy się **po dwóch miesiącach, a nie po dziesięciu**.',
   ],
 }),
 ('P6-25', [31], {
   'typ': 'tabela', 'nadtytul': 'PO KAŻDYM POMIARZE',
   'naglowek': 'Jedna z czterech decyzji zespołu',
   'naglowki': ['Wynik', 'Decyzja'],
   'szerokosci': [30, 70],
   'wiersze': [
     ['Cel osiągnięty', 'zamykamy i **stawiamy kolejny**'],
     ['Osiągnięty częściowo', 'kontynuujemy i przesuwamy termin — **nie obniżając kryterium**'],
     ['Brak postępu', 'modyfikujemy metodę i **sprawdzamy bariery środowiskowe**'],
     ['Regres', 'spotkanie z rodzicami i **rozważenie wystąpienia do poradni**'],
   ],
 }),
 ('P6-26', [32, 33], {
   'typ': 'druk', 'nadtytul': 'OPINIA DLA PORADNI',
   'naglowek': 'Dziesięć dni od dnia otrzymania prośby przez dyrektora',
   'plik': DRUKI + 'wopf_opinia-do-poradni.png',
   'opis': 'Wydajemy ją na prośbę przewodniczącego zespołu orzekającego.',
 }),
 ('P6-27', [34], {
   'typ': 'tabela', 'nadtytul': 'BUDOWA OPINII',
   'naglowek': 'Siedem punktów',
   'naglowki': ['#', 'Punkt opinii'],
   'szerokosci': [10, 90],
   'wiersze': [
     ['1', 'Dane formalne'],
     ['2', 'Mocne strony i uzdolnienia'],
     ['3', 'Funkcjonowanie w obszarach'],
     ['4', 'Trudności — z częstotliwością i kontekstem'],
     ['5', 'Bariery i ułatwienia'],
     ['6', 'Udzielone wsparcie i jego efekty'],
     ['7', 'Współpraca z rodzicami'],
   ],
 }),
 ('P6-28', [35, 36], {
   'typ': 'punkty', 'nadtytul': 'JAK PISZEMY OPINIĘ',
   'naglowek': 'Językiem funkcjonalnym i sprawdzalnym',
   'punkty': [
     'Opisujemy **zachowania, ich częstotliwość i kontekst**.',
     'Rozpoznania i hipotezy diagnostyczne **pozostawiamy poradni**.',
     'Informacje od rodziców lub specjalistów spoza przedszkola oznaczamy **jako relację, ze wskazaniem źródła**.',
     'Kwestionariusz pozostaje **naszym materiałem roboczym**.',
   ],
 }),
 ('P6-29', [37], {
   'typ': 'punkty', 'nadtytul': 'JEDNA DOBRA PRAKTYKA NA ZAKOŃCZENIE',
   'naglowek': 'Proporcja, która sprawdza cały opis',
   'punkty': [
     'Punkt o **mocnych stronach piszemy jako pierwszy**.',
     'I **co najmniej tak samo obszernie** jak punkt o trudnościach.',
     'To najprostszy sprawdzian, czy nasz opis dziecka jest **naprawdę funkcjonalny**.',
   ],
 }),
 ('P6-30', [38], {
   'typ': 'domkniecie',
   'naglowek': 'Podsumowanie całego szkolenia',
   'zdania': [
     'Każdy druk ma swój przepis.',
     'Obserwacja wyprzedza pismo z poradni.',
     'Cel ma liczbę, a ewaluacja ma konsekwencję.',
   ],
 }),
]

PLANY = {1: PLAN_1, 2: PLAN_2, 3: PLAN_3, 4: PLAN_4, 5: PLAN_5, 6: PLAN_6}

TYTULY = {
  1: ('Podstawa prawna', 'co obowiązuje w przedszkolu od 1 września 2026 r.'),
  2: ('Obieg dokumentów', 'jak jeden dokument wynika z drugiego'),
  3: ('Metryczka dziecka', 'pierwszy dokument września'),
  4: ('KPOF', 'budowa narzędzia, skala, liczenie wyniku, odczyt profilu'),
  5: ('Obserwacja pogłębiona', 'ABC, profil sensoryczny, teoria umysłu, karta mowy'),
  6: ('WOPF, IPET, ewaluacja', 'cele SMART, ewaluacja i opinia dla poradni'),
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
        # Karta tytułowa zapowiada czas trwania modułu. Dopóki nie ma nagrań,
        # zostaje szacunek wpisany w planie; po nagraniu bierzemy sumę zmierzoną,
        # żeby zapowiedź na ekranie zgadzała się z długością pliku.
        laczne = sum(u['sekundy'] for u in ujecia)
        for u in ujecia:
            if u['scena']['typ'] == 'tytulModulu':
                u['scena'] = dict(u['scena'], czas=f'{int(laczne) // 60}:{int(laczne) % 60:02d}')

        moduly.append({
          'id': f'P{numer}',
          'numer': str(numer),
          'tytul': tytul,
          'podtytul': podtytul,
          'ujecia': ujecia,
        })
    return moduly


def sprawdz_pokrycie(moduly, narracje):
    """Każdy akapit skryptu ma trafić do dokładnie jednego ujęcia."""
    for numer, plan in sorted(PLANY.items()):
        uzyte = [i for _, indeksy, _ in plan for i in indeksy]
        powtorzone = sorted({i for i in uzyte if uzyte.count(i) > 1})
        pominiete = [i for i in range(len(narracje[numer])) if i not in uzyte]
        print(f'  część {numer}: powtórzone {powtorzone or "—"}, pominięte {pominiete or "—"}')


if __name__ == '__main__':
    narracje = narracja_ze_skryptu()
    moduly = zbuduj()
    sciezka = os.path.join(KATALOG, 'src', 'scenariusz-przedszkole.json')
    io.open(sciezka, 'w', encoding='utf-8').write(json.dumps(moduly, ensure_ascii=False, indent=1))
    for m in moduly:
        sek = sum(u['sekundy'] for u in m['ujecia'])
        nagrane = sum(1 for u in m['ujecia'] if u.get('glos'))
        print(f"P{m['numer']} · {m['tytul']}: {len(m['ujecia'])} ujęć, "
              f"{int(sek // 60)}:{int(sek % 60):02d}, nagrane {nagrane}/{len(m['ujecia'])}")
    print('Pokrycie narracji:')
    sprawdz_pokrycie(moduly, narracje)
