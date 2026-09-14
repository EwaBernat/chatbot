// Bank rozwiązań do IPE — Obszar 4: Mobilność i motoryka (d410–d499)
module.exports = {
  nr: 4,
  obszar: 'MOBILNOŚĆ I MOTORYKA',
  kody: 'd410–d499',
  etap: 'KLASY 1–3 (EDUKACJA WCZESNOSZKOLNA)',
  stopka: 'Obszar 4: Motoryka',
  instrukcja: [
    'Ten dokument obejmuje kody ICF dotyczące motoryki małej (dłonie) i dużej (chodzenie).',
    'Wybierz karty odpowiednie dla potrzeb Twojego ucznia.'
  ],
  checklist: [
    'Czy cel wynika bezpośrednio z WOPFU? (Czy trudności ruchowe zostały opisane w Wielospecjalistycznej Ocenie?)',
    'Czy cel jest SMART? (Sprecyzowany, Mierzalny, Atrakcyjny, Realistyczny, Terminowy)?',
    'Czy problem ma podłoże napięciowe (za słabe/za silne napięcie mięśniowe)?',
    'Czy uczeń ma zapewnione odpowiednie siedzisko/ławkę (stabilizacja postawy)?',
    'Czy określono poziom wsparcia (fizyczne prowadzenie ręki, asekuracja, słowne)?',
    'Czy cel jest bezpieczny dla dziecka (np. ćwiczenia na schodach)?',
    'Czy środowisko (klasa, korytarz) jest wolne od barier architektonicznych?',
    'Czy przygotowano pomoce adaptacyjne (nakładki, maty antypoślizgowe)?',
    'Czy ustalono system przerw na regenerację (zmęczenie fizyczne wpływa na koncentrację)?',
    'Czy wszyscy nauczyciele (w tym WF) znają ograniczenia ruchowe ucznia?',
    'Czy rodzic wie, jak ćwiczyć te umiejętności w domu?',
    'Czy cel uwzględnia samodzielność (np. samoobsługa w szatni)?',
    'Czy mamy narzędzie do monitorowania (tabelka postępów, filmik)?',
    'Czy przewidziano reakcję na ból lub dyskomfort ucznia?',
    'Czy termin ewaluacji jest realny (rehabilitacja ruchowa wymaga czasu)?',
    'Czy skonsultowano cel z fizjoterapeutą lub terapeutą SI?'
  ],
  karty: [
    {
      kod: 'd440', nazwa: 'Używanie ręki (Motoryka Mała)',
      podtytul: 'Precyzyjne używanie dłoni (chwytanie, manipulowanie)',
      problem: 'Osłabiona precyzja chwytu, wypadanie przedmiotów z dłoni, trudność w chwytaniu drobnych elementów (pieniądze, koraliki, gumka), nieprawidłowy chwyt narzędzia pisarskiego.',
      cel: 'Uczeń wykona zadanie manipulacyjne polegające na przełożeniu 10 drobnych elementów (np. fasolki, monety) z jednego pojemnika do drugiego, używając chwytu pęsetowego (kciuk i palec wskazujący) w czasie do 2 minut. (Sukces: bez upuszczenia).',
      strategia: 'Terapia Ręki + Integracja Sensoryczna (SI).',
      poziomy: [
        'Wsparcie Znaczne: Nauczyciel fizycznie prowadzi rękę ucznia, pomagając utrzymać przedmiot (wsparcie manualne).',
        'Wsparcie Umiarkowane: Nauczyciel stabilizuje pojemnik, uczeń manipuluje samodzielnie.',
        'Wsparcie Niskie: Zachęta słowna: „Złap samymi czubkami palców, jak ptaszek dzióbkiem”.'
      ],
      pomoce: 'Szczypce, pęsety (różnej wielkości), sortery, klocki LEGO, plastelina (do rozgrzewki), nakładki korygujące na ołówek.',
      metody: 'Metoda Dobrego Startu, Zabawy paluszkowe, Ćwiczenia grafomotoryczne.',
      dostosowania: 'Pogrubione narzędzia pisarskie (trójkątne kredki), mata antypoślizgowa na stolik (żeby przedmioty nie uciekały).',
      udl: 'Możliwość użycia tabletu (przesuwanie elementów palcem) jako treningu precyzji dla całej klasy.',
      kroki: [
        'Rozgrzewka dłoni i barków (krążenia, ściskanie piłeczki).',
        'Ćwiczenia separacji palców (zabawa „idzie kominiarz”).',
        'Właściwe zadanie manipulacyjne (np. nawlekanie koralików lub sortowanie).',
        'Zastosowanie umiejętności w zadaniu szkolnym (np. przyklejenie naklejki w wyznaczone miejsce).'
      ],
      osoba: 'Terapeuta ręki, Nauczyciel', ewaluacja: 'Koniec semestru.'
    },
    {
      kod: 'd450', nazwa: 'Chodzenie (Motoryka Duża)',
      podtytul: 'Przemieszczanie się w szkole i po schodach',
      problem: 'Zaburzenia równowagi, częste potykanie się, lęk przed schodami, wpadanie na inne osoby podczas przemieszczania się w grupie.',
      cel: 'Uczeń samodzielnie pokona ciąg schodów (w górę i w dół) między piętrami szkoły, stawiając kroki naprzemiennie i trzymając się poręczy, zachowując bezpieczne tempo (bez zatrzymywania ze strachu).',
      strategia: 'Rehabilitacja Ruchowa + Strategia Bezpieczeństwa.',
      poziomy: [
        'Wsparcie Znaczne: Nauczyciel idzie o krok przed/za uczniem, trzymając go za rękę (asekuracja czynna).',
        'Wsparcie Umiarkowane: Nauczyciel idzie obok (asekuracja bierna) i przypomina: „Patrz pod nogi, trzymaj poręcz”.',
        'Wsparcie Niskie: Uczeń idzie w parze z rówieśnikiem („bodyguardem”), który nadaje tempo.'
      ],
      pomoce: 'Taśmy oznaczające krawędzie schodów (kontrastowe), poręcze na odpowiedniej wysokości.',
      metody: 'Metoda Ruchu Rozwijającego W. Sherborne (świadomość ciała), Tor przeszkód (na WF).',
      dostosowania: 'Pozwolenie na korzystanie z windy (jeśli jest) w dni gorszego samopoczucia, wychodzenie na przerwę minutę wcześniej (puste korytarze).',
      udl: 'Oznaczenie ciągów komunikacyjnych w szkole (strzałki na podłodze) dla porządkowania ruchu wszystkich uczniów.',
      kroki: [
        'Nauka bezpiecznej pozycji na schodach (jedna ręka na poręczy, plecak stabilnie założony).',
        'Ćwiczenie chodu naprzemiennego na płaskim terenie (np. po drabince koordynacyjnej).',
        'Trening na schodach w czasie lekcji (gdy jest cicho i pusto).',
        'Przejście w grupie rówieśniczej (na końcu pary, by nikt nie popychał).'
      ],
      osoba: 'Nauczyciel WF, Fizjoterapeuta', ewaluacja: 'Koniec roku.'
    }
  ]
};
