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
   'podtytul': 'Z czego wynika każdy dokument, który wypełniamy w szkole od 1 września 2026 roku.',
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
   'naglowek': 'Kiedy IPET musi być gotowy',
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
   'typ': 'punkty', 'nadtytul': 'CO TO OZNACZA DLA SZKOŁY',
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
   'naglowek': 'Dlaczego wrzesień, a nie kwiecień',
   'punkty': [
     'Dziesięć dni to bardzo mało, jeśli obserwację **zaczynamy dopiero po wpłynięciu prośby**.',
     'Ucznia klasy szóstej uczy **dziewięcioro nauczycieli** i żaden nie widzi go przez cały dzień.',
     'Kwestionariusz wypełniamy **we wrześniu** — nie po to, żeby leżał w segregatorze.',
     'Po to, żeby w dowolnym dniu roku odpowiedzieć poradni **na podstawie danych, spokojnie i na czas**.',
   ],
 }),
 ('S1-19', [21, 22], {
   'typ': 'punkty', 'nadtytul': 'AKT CZWARTY · DOKUMENTACJA PRZEBIEGU NAUCZANIA',
   'naglowek': 'Gdzie mieszczą się nasze arkusze obserwacji',
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
   'naglowek': 'Na jakiej podstawie dostosowujemy wymagania',
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
   'naglowek': 'Którą podstawę wpisujemy w programie ucznia',
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

PLANY = {1: PLAN_1}


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
