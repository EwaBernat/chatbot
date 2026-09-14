// Bank rozwiązań do IPE — Obszar 3: Komunikacja i porozumiewanie się (d310–d350)
module.exports = {
  nr: 3,
  obszar: 'KOMUNIKACJA I POROZUMIEWANIE SIĘ',
  kody: 'd310–d350',
  etap: 'KLASY 1–3 (EDUKACJA WCZESNOSZKOLNA)',
  stopka: 'Obszar 3: Komunikacja',
  instrukcja: [
    'Ten dokument obejmuje kody ICF dotyczące odbioru i nadawania wiadomości.',
    'Wybierz karty odpowiednie dla potrzeb Twojego ucznia.'
  ],
  checklist: [
    'Czy cel wynika bezpośrednio z WOPFU? (Czy trudności komunikacyjne zostały opisane w Wielospecjalistycznej Ocenie?)',
    'Czy cel jest SMART? (Sprecyzowany, Mierzalny, Atrakcyjny, Realistyczny, Terminowy)?',
    'Czy problem dotyczy bardziej ODBIORU (rozumienia) czy NADAWANIA (mówienia) komunikatów?',
    'Czy uczeń ma sprawdzony słuch fizyczny?',
    'Czy określono poziom wsparcia (gesty, obrazki, modelowanie)?',
    'Czy cel jest zrozumiały dla dziecka (np. „Będę patrzył na panią, gdy mówi”)?',
    'Czy środowisko (hałas w klasie) nie utrudnia realizacji celu?',
    'Czy przygotowano pomoce AAC (komunikacja alternatywna) jeśli są potrzebne?',
    'Czy ustalono system nagradzania prób komunikacji (nawet nieudanych)?',
    'Czy wszyscy nauczyciele reagują tak samo na komunikaty dziecka?',
    'Czy rodzic wie, jak ćwiczyć te umiejętności w domu?',
    'Czy cel uwzględnia komunikację z rówieśnikami, a nie tylko z dorosłym?',
    'Czy mamy narzędzie do monitorowania postępów (np. karta obserwacji logopedycznej)?',
    'Czy przewidziano „koła ratunkowe” w sytuacji braku zrozumienia?',
    'Czy termin ewaluacji jest realny (terapia mowy to proces długotrwały)?'
  ],
  karty: [
    {
      kod: 'd310', nazwa: 'Odbiór wiadomości ustnych', podtytul: null,
      problem: 'Trudność w rozumieniu mowy w hałasie, mylenie podobnie brzmiących słów, nierozumienie poleceń kierowanych do grupy.',
      cel: 'Uczeń poprawnie zrozumie i wykona proste polecenie słowne nauczyciela (np. „otwórz okno”) bez konieczności powtarzania, w warunkach klasowych (przy umiarkowanym szumie). (Sukces: 4/5 prób).',
      strategia: 'Strategia Skupiania Uwagi Słuchowej + Wizualizacja.',
      poziomy: [
        'Wsparcie Znaczne: Nauczyciel nawiązuje kontakt wzrokowy, dotyka ramienia ucznia i mówi powoli wprost do niego.',
        'Wsparcie Umiarkowane: Nauczyciel używa słowa-klucza (imienia dziecka) przed wydaniem polecenia grupowego.',
        'Wsparcie Niskie: Uczeń prosi o powtórzenie („Proszę powtórzyć”), jeśli nie zrozumiał (samoregulacja).'
      ],
      pomoce: 'Piktogramy wspierające treść („Otwórz”, „Zeszyt”), system FM (jeśli uczeń niedosłyszący).',
      metody: 'Trening Słuchowy (elementy Tomatisa/Johansena – na terapii), Zabawy słuchowe („Głuchy telefon”).',
      dostosowania: 'Miejsce w pierwszej ławce, z dala od źródła hałasu (okno, korytarz).',
      udl: 'Zapisywanie kluczowych haseł na tablicy podczas mówienia (wsparcie dla wszystkich).',
      kroki: [
        'Nauczyciel stosuje sygnał „Uwaga” (klaśnięcie).',
        'Wydanie krótkiego, prostego komunikatu (unikanie zdań wielokrotnie złożonych).',
        'Uczeń parafrazuje polecenie („Mam otworzyć okno”).',
        'Wykonanie zadania i pochwała opisowa („Dobrze usłyszałeś”).'
      ],
      osoba: 'Logopeda, Nauczyciel', ewaluacja: 'Koniec semestru.'
    },
    {
      kod: 'd315', nazwa: 'Odbiór wiadomości niewerbalnych', podtytul: null,
      problem: 'Nierozumienie mowy ciała, mimiki (np. złości nauczyciela, znudzenia kolegów), brak reakcji na gesty uciszające.',
      cel: 'Uczeń poprawnie zidentyfikuje emocję lub intencję innej osoby na podstawie mimiki/gestu (np. „Palec na ustach” = cisza, zmarszczone brwi = złość) w sytuacjach szkolnych. (3/5 sytuacji).',
      strategia: 'Trening Umiejętności Społecznych (TUS) + Karty Emocji.',
      poziomy: [
        'Wsparcie Znaczne: Nauczyciel werbalizuje swój stan: „Mam zmarszczone brwi, bo jestem zła”.',
        'Wsparcie Umiarkowane: Nauczyciel pokazuje kartę z odpowiednią minką (emoji) obok swojej twarzy.',
        'Wsparcie Niskie: Nauczyciel robi znaczącą pauzę i patrzy na ucznia, czekając na odczytanie sygnału.'
      ],
      pomoce: 'Plakat „Nasze Emocje”, Lustro, Karty z gestami (Cisza, Stop, Proszę).',
      metody: 'Modelowanie, Odgrywanie scenek (Drama), Analiza zdjęć/filmów.',
      dostosowania: 'Wyrazista (nieco przerysowana) mimika nauczyciela w kontakcie z uczniem.',
      udl: 'Wprowadzenie w klasie umownych znaków migowych dla wszystkich (np. ręka w górę = zgłaszam się).',
      kroki: [
        'Nauka znaczenia podstawowych gestów klasowych (cisza, siadamy).',
        'Ćwiczenia w rozpoznawaniu emocji ze zdjęć (TUS).',
        'Zastosowanie w praktyce: N. pokazuje gest → Uczeń reaguje.',
        'Nagradzanie adekwatnej reakcji na komunikat niewerbalny.'
      ],
      osoba: 'Psycholog, Pedagog', ewaluacja: 'Obserwacja bieżąca.'
    },
    {
      kod: 'd330', nazwa: 'Mówienie (Artykulacja/Płynność)', podtytul: null,
      problem: 'Mowa niewyraźna, cicha, bełkotliwa lub mutyzm wybiórczy (lęk przed mówieniem).',
      cel: 'Podczas odpowiedzi ustnej lub rozmowy z nauczycielem, uczeń wypowie zrozumiałe zdanie (min. 3 wyrazy) z odpowiednią głośnością, utrzymując tempo pozwalające na zrozumienie.',
      strategia: 'Korekcja Logopedyczna + Metoda Małych Kroków (dla lęku).',
      poziomy: [
        'Wsparcie Znaczne: Uczeń odpowiada tylko „Tak/Nie” lub szepcze do ucha nauczyciela (w przypadku mutyzmu).',
        'Wsparcie Umiarkowane: Odpowiedź w małej grupie lub parze, a nie na forum klasy.',
        'Wsparcie Niskie: Uczeń odpowiada na forum, Nauczyciel dyskretnie przypomina: „Głośno i wolno”.'
      ],
      pomoce: 'Mikrofon (zabawkowy lub prawdziwy do ośmielania), Pacynka (pośrednik w rozmowie).',
      metody: 'Ćwiczenia oddechowe i fonacyjne, Logorytmika, Technika „Przedłużonego mówienia”.',
      dostosowania: 'Wydłużony czas na odpowiedź, niepoprawianie błędów artykulacyjnych przy klasie.',
      udl: 'Możliwość nagrania odpowiedzi w domu (podcast/audio) zamiast występu na żywo.',
      kroki: [
        'Ćwiczenia usprawniające narządy mowy (wg zaleceń logopedy).',
        'Ośmielanie do krótkich wypowiedzi w kontakcie 1:1.',
        'Wydłużanie wypowiedzi (budowanie zdań).',
        'Generalizacja: wypowiedź na forum klasy (np. przeczytanie jednego zdania).'
      ],
      osoba: 'Logopeda', ewaluacja: 'Koniec roku.'
    },
    {
      kod: 'd335', nazwa: 'Tworzenie wiadomości niewerbalnych', podtytul: null,
      problem: 'Brak używania gestów (wskazywania, kiwania głową), uboga ekspresja, brak kontaktu wzrokowego podczas komunikacji.',
      cel: 'Chcąc zakomunikować potrzebę lub odpowiedź, uczeń użyje adekwatnego gestu (np. podniesienie ręki, wskazanie palcem, kiwnięcie głową na „tak”), nawiązując przy tym krótki kontakt wzrokowy.',
      strategia: 'Komunikacja Totalna (Gesty + Mowa).',
      poziomy: [
        'Wsparcie Znaczne: Nauczyciel modeluje gest ręką ucznia (np. pomaga wskazać obrazek).',
        'Wsparcie Umiarkowane: Nauczyciel pyta: „Pokaż mi, czego chcesz?” (zachęta werbalna).',
        'Wsparcie Niskie: Nauczyciel czeka na nawiązanie kontaktu wzrokowego przed udzieleniem odpowiedzi.'
      ],
      pomoce: 'Tablice wyboru, Książka do komunikacji (PECS – jeśli dotyczy), Lustro.',
      metody: 'AAC (Wspomagające i alternatywne metody komunikacji), Makaton (podstawowe gesty).',
      dostosowania: 'Akceptowanie gestu jako pełnoprawnej odpowiedzi (np. kciuk w górę zamiast słowa „dobrze”).',
      udl: 'Zabawy w kalambury dla całej klasy (rozwijanie ekspresji ciała).',
      kroki: [
        'Wprowadzenie gestów oznaczających „Tak” i „Nie”.',
        'Nauka gestu zgłaszania potrzeby (podniesienie ręki/kartonika).',
        'Wzmacnianie każdej próby kontaktu wzrokowego (uśmiechem, uwagą).',
        'Łączenie gestu ze słowem (np. mówienie „Cześć” i machanie ręką).'
      ],
      osoba: 'Nauczyciel wsp., Rodzic', ewaluacja: 'Obserwacja.'
    },
    {
      kod: 'd350', nazwa: 'Rozmowa (Prowadzenie dialogu)', podtytul: null,
      problem: 'Przerywanie innym, monologowanie (niezwracanie uwagi na rozmówcę), trudność w utrzymaniu tematu rozmowy (d350.3).',
      cel: 'Podczas pracy w parze lub rozmowy z nauczycielem, uczeń przeprowadzi krótką wymianę zdań (min. 3 tury: pytanie-odpowiedź-pytanie), czekając na swoją kolej i trzymając się tematu.',
      strategia: 'Trening Naprzemienności (Turn-taking).',
      poziomy: [
        'Wsparcie Znaczne: Użycie rekwizytu (np. „Mikrofonu”). Mówi tylko ten, kto trzyma przedmiot.',
        'Wsparcie Umiarkowane: Nauczyciel daje znak gestem (otwarta dłoń), kiedy jest kolej ucznia.',
        'Wsparcie Niskie: Przypomnienie zasady: „Jedna osoba mówi, reszta słucha”.'
      ],
      pomoce: 'Piłka (rzucamy do osoby, która ma głos), „Gadający Kamień”, Komiks konwersacyjny (dymki).',
      metody: 'TUS, Historyjki społeczne, Gry planszowe (wymuszają kolejki).',
      dostosowania: 'Dobranie spokojnego partnera do pary (modelowanie poprawnej rozmowy).',
      udl: 'Zasady dyskusji wiszące na ścianie w formie graficznej (dla całej klasy).',
      kroki: [
        'Nauka zasady naprzemienności w zabawie (rzucanie piłką).',
        'Krótkie dialogi sterowane (N. zadaje pytanie, U. odpowiada).',
        'Zachęcanie ucznia do zadawania pytań koledze (inicjowanie).',
        'Rozmowa swobodna na temat zainteresowań (z pilnowaniem tematu).'
      ],
      osoba: 'Wychowawca, Logopeda', ewaluacja: 'Koniec roku.'
    }
  ]
};
