/* Katalog szkoleń PCTP Koszalin — treść merytoryczna.
   Skład: generuj.js                                                        */

const SCIEZKI = [
  { id: "A", nazwa: "Emocje i kompetencje społeczne", hex: "#E8450A",
    opis: "Praca z emocjami od przedszkola po szkołę ponadpodstawową — metodą pięciu kolorów i treningiem umiejętności społecznych." },
  { id: "B", nazwa: "Dokumentacja i ocena funkcjonalna", hex: "#2D1B69",
    opis: "WOPF, IPET, poziomy wsparcia i ewaluacja — dokumentacja, która opisuje dziecko, a nie wypełnia rubryki." },
  { id: "C", nazwa: "Uczeń o specjalnych potrzebach", hex: "#2E6FB7",
    opis: "Spektrum autyzmu, zachowania trudne i dostosowania — w grupie ogólnodostępnej, przy realnej liczbie dzieci." },
  { id: "D", nazwa: "Narzędzia i wdrożenia", hex: "#0D7D5C",
    opis: "Komunikacja alternatywna i aplikacja EduPlaner 2026 — narzędzia, które zostają w placówce po szkoleniu." },
];

const FORMY = [
  { nazwa: "Rada szkoleniowa u Państwa", opis: "Szkolenie na miejscu, dla całego zespołu. Materiały i przykłady dobieramy do specyfiki placówki — przedszkole, szkoła, poradnia, ośrodek.", ile: "do 30 osób" },
  { nazwa: "Warsztat otwarty", opis: "Zapisy indywidualne. Uczestnicy z różnych placówek, dużo pracy na przypadkach wniesionych przez grupę.", ile: "12–18 osób" },
  { nazwa: "Webinar", opis: "Wersja online, skrócona do części wykładowej i pokazu narzędzi. Nagranie dostępne przez 30 dni.", ile: "bez limitu" },
  { nazwa: "Konsultacja wdrożeniowa", opis: "Po szkoleniu — praca na dokumentacji konkretnych dzieci z Państwa placówki. Online albo na miejscu.", ile: "zespół 3–8 osób" },
];

const SZKOLENIA = [
  /* ── Ścieżka A ─────────────────────────────────────────────────────── */
  { kod: "A1", sciezka: "A", polecane: true,
    tytul: "Kolorowy Świat Emocji",
    podtytul: "Metoda pięciu kolorów w pracy z nastolatkiem ze spektrum autyzmu",
    opis: "Nastolatek, który czuje wszystko bardzo mocno i nie ma na to słowa, potrzebuje narzędzia prostszego niż rozmowa o uczuciach. Tym narzędziem jest kolor. Szkolenie prowadzi przez całą metodę — od pierwszego kontaktu po grę planszową domykającą cykl.",
    czas: "6 godzin dydaktycznych", uczestnicy: "12–25 osób",
    dlaKogo: ["Nauczyciele współorganizujący kształcenie", "Pedagodzy specjalni i psycholodzy szkolni", "Terapeuci prowadzący zajęcia rewalidacyjne", "Wychowawcy klas z uczniem w spektrum"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty", "Webinar (4 h)"],
    program: [
      { modul: "Dlaczego kolor działa tam, gdzie nie działa rozmowa", czas: "45 min", punkty: [
        "Aleksytymia i trudność w nazywaniu stanów wewnętrznych u osób w spektrum",
        "Kolor jako etykieta zewnętrzna — dlaczego jest łatwiejszy niż pojęcie abstrakcyjne",
        "Pięć emocji podstawowych i przypisane im kolory: radość, smutek, złość, wstyd, lęk" ]},
      { modul: "Osiem kroków rozdziału — praca na materiale", czas: "90 min", punkty: [
        "Mapa ciała: uczenie rozpoznawania emocji po sygnałach somatycznych",
        "Opowiadanie jako bezpieczny dystans — dlaczego bohater przeżywa zamiast ucznia",
        "Trzy poziomy trudności zadań i prawo ucznia do wyboru poziomu",
        "Strona osobista: termometr emocji, rysunek, własne zdjęcie" ]},
      { modul: "Praca z każdą z pięciu emocji", czas: "120 min", punkty: [
        "Radość — jak ją zatrzymać i po co to robić",
        "Smutek — towarzyszenie zamiast pocieszania; najczęstsze błędy dorosłych",
        "Złość — cztery kroki STOP / ODDECH / ODEJDŹ / POWIEDZ i przygotowane zdanie",
        "Wstyd — praca po pomyłce publicznej, sprawdzanie faktów",
        "Lęk — technika 5–4–3–2–1, rozdzielenie obaw i planu na dwie kolumny" ]},
      { modul: "Narzędzia, które zostają po zajęciach", czas: "60 min", punkty: [
        "Karty emocji jako pomoc komunikacyjna — w tym karta „Nie wiem jeszcze”",
        "Plan na trudny dzień: umówiony sygnał przerwy i miejsce na ochłonięcie",
        "Gra „Ścieżka Kolorów” — rozgrywka w grupie szkoleniowej",
        "Strona bezpieczeństwa: kiedy kierować do specjalisty" ]},
      { modul: "Wdrożenie w Państwa placówce", czas: "45 min", punkty: [
        "Jak rozłożyć cykl w czasie i wpisać go w plan zajęć rewalidacyjnych",
        "Rozmowa z rodzicem przed startem — o co zapytać",
        "Dowody efektywności do dokumentacji" ]},
    ],
    efekty: [
      "Prowadzisz cały cykl pięciu rozdziałów bez dodatkowego przygotowania",
      "Wiesz, co robić, gdy uczeń odmawia odpowiedzi — i dlaczego zasada „pas” jest ważniejsza od wypełnionej strony",
      "Umiesz przełożyć pracę z zeszytem na zapisy w IPET-cie",
    ],
    materialy: ["Zeszyt „Kolorowy Świat Emocji” cz. 1 — licencja indywidualna dla każdego uczestnika", "Komplet kart emocji do wycięcia", "Skrypt szkolenia", "Zaświadczenie o ukończeniu"] },

  { kod: "A2", sciezka: "A",
    tytul: "Emocje w przedszkolu",
    podtytul: "Gotowe konspekty i praktyka dla grup 3–6 lat",
    opis: "Trzylatek nie opowie o swoich uczuciach, ale pokaże kolor. Szkolenie daje komplet siedmiu konspektów na dwanaście tygodni pracy oraz gotowe cele SMART do IPET-u — po jednym na każdy poziom wsparcia.",
    czas: "6 godzin dydaktycznych", uczestnicy: "12–25 osób",
    dlaKogo: ["Nauczyciele wychowania przedszkolnego", "Nauczyciele współorganizujący w przedszkolu", "Psycholodzy i pedagodzy przedszkolni", "Terapeuci pracujący z małym dzieckiem"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty", "Webinar (4 h)"],
    program: [
      { modul: "Co trzylatek naprawdę potrafi", czas: "45 min", punkty: [
        "Rozwój emocjonalny 3–6 lat: co jest w zasięgu, a co jeszcze nie",
        "Dlaczego mówimy „strach”, a nie „lęk”, i dlaczego wstyd pracujemy obrazkiem",
        "Dwadzieścia minut jako granica zorganizowanej uwagi" ]},
      { modul: "Siedem konspektów — przejście przez cykl", czas: "120 min", punkty: [
        "Konspekt wprowadzający: budowanie wspólnego kodu grupy",
        "Pięć konspektów kolorów: pięcioetapowa struktura zajęć",
        "Konspekt podsumowujący z grą planszową",
        "Miś Kolorek — bohater, który zmienia chustkę razem z emocją" ]},
      { modul: "Cele SMART dla trzech poziomów wsparcia", czas: "105 min", punkty: [
        "Jak ten sam konspekt daje trzy różne cele — praca warsztatowa",
        "Zapis celu z podpowiedzią: dlaczego cel na poziomie III nie jest „gorszy”",
        "Obszary KSzOF i kody ICF przy celach przedszkolnych",
        "Karta obserwacji jako załącznik do ewaluacji IPET-u" ]},
      { modul: "Trudne momenty w grupie", czas: "60 min", punkty: [
        "Kącik Ciszy — gdzie go umieścić, żeby dziecko do niego doszło",
        "Sygnał STOP wspólny dla wszystkich dorosłych w sali",
        "Rozstanie z rodzicem i dziecko, które płacze codziennie" ]},
      { modul: "Dostosowania w grupie mieszanej", czas: "30 min", punkty: [
        "Dziecko niemówiące, mutyzm wybiórczy, nadwrażliwość sensoryczna",
        "Jak prowadzić zajęcia, gdy troje dzieci ma trzy różne cele" ]},
    ],
    efekty: [
      "Wychodzisz z gotowym planem dwunastu tygodni pracy z grupą",
      "Masz 21 celów SMART do przeniesienia wprost do IPET-u",
      "Wiesz, jak zapisać ten sam cel na trzech poziomach wsparcia",
    ],
    materialy: ["Konspekty 3–4 lata — pełny komplet w PDF i Wordzie", "Karta obserwacji celów do wydruku", "Wzory kart emocji dla przedszkolaka", "Zaświadczenie o ukończeniu"] },

  { kod: "A3", sciezka: "A",
    tytul: "Trening umiejętności społecznych od podstaw",
    podtytul: "Jak poprowadzić TUS, gdy nie jesteś psychoterapeutą",
    opis: "TUS bywa wpisywany do IPET-u szybciej, niż powstaje pomysł, co właściwie robić przez czterdzieści pięć minut. Szkolenie daje strukturę zajęć, zestaw ćwiczeń i sposób mierzenia postępu.",
    czas: "8 godzin dydaktycznych", uczestnicy: "12–20 osób",
    dlaKogo: ["Prowadzący zajęcia rozwijające kompetencje emocjonalno-społeczne", "Pedagodzy specjalni i psycholodzy", "Nauczyciele współorganizujący", "Wychowawcy świetlic i ośrodków"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty"],
    program: [
      { modul: "Czym TUS jest, a czym nie jest", czas: "60 min", punkty: [
        "Granica między treningiem umiejętności a psychoterapią",
        "Kwalifikacja do grupy: kto skorzysta, a komu zaszkodzi",
        "Dobór grupy — wiek, poziom funkcjonowania, liczebność" ]},
      { modul: "Stała struktura zajęć", czas: "90 min", punkty: [
        "Pięć etapów spotkania i po co każdy z nich jest",
        "Rytuał otwarcia i zamknięcia — dlaczego nie wolno go skracać",
        "Kontrakt grupowy z dziećmi, które nie czytają" ]},
      { modul: "Bank ćwiczeń", czas: "150 min", punkty: [
        "Rozpoznawanie emocji u siebie i u innych",
        "Proszenie, odmawianie, czekanie na swoją kolej",
        "Wchodzenie do zabawy i wychodzenie z niej",
        "Konflikt rówieśniczy — scenki i modelowanie",
        "Praca z przegraną w grze" ]},
      { modul: "Mierzenie postępu", czas: "90 min", punkty: [
        "Cel SMART dla umiejętności społecznej — warsztat na przykładach uczestników",
        "Arkusz obserwacji zachowań docelowych",
        "Generalizacja: jak przenieść umiejętność z sali TUS do klasy" ]},
      { modul: "Współpraca z rodzicami i zespołem", czas: "60 min", punkty: [
        "Informacja zwrotna dla rodzica po cyklu",
        "Co przekazać wychowawcy, żeby efekt się utrzymał" ]},
    ],
    efekty: [
      "Prowadzisz zajęcia według stałej struktury, bez wymyślania scenariusza co tydzień",
      "Masz bank ćwiczeń na cały rok szkolny",
      "Umiesz udowodnić postęp liczbą, a nie wrażeniem",
    ],
    materialy: ["Skrypt z bankiem 40 ćwiczeń", "Arkusze obserwacji", "Wzory kontraktu grupowego", "Zaświadczenie o ukończeniu"] },

  /* ── Ścieżka B ─────────────────────────────────────────────────────── */
  { kod: "B1", sciezka: "B", polecane: true,
    tytul: "WOPF krok po kroku",
    podtytul: "Wielospecjalistyczna ocena poziomu funkcjonowania, która się przydaje",
    opis: "WOPF bywa dokumentem pisanym w jeden wieczór, żeby zdążyć przed terminem. Szkolenie pokazuje, jak zebrać dane, których naprawdę potrzebuje zespół — i jak napisać ocenę, z której da się wyprowadzić cele.",
    czas: "8 godzin dydaktycznych", uczestnicy: "12–25 osób",
    dlaKogo: ["Członkowie zespołów opracowujących IPET", "Pedagodzy specjalni, psycholodzy, logopedzi", "Dyrektorzy nadzorujący dokumentację", "Nauczyciele współorganizujący"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty", "Konsultacja wdrożeniowa"],
    program: [
      { modul: "Po co komu WOPF", czas: "60 min", punkty: [
        "Miejsce WOPF-u w cyklu: orzeczenie → ocena → IPET → ewaluacja",
        "Terminy i obowiązki zespołu — co mówi rozporządzenie",
        "Najczęstsze uchybienia wychwytywane przez kuratorium" ]},
      { modul: "Dziewięć obszarów KSzOF", czas: "120 min", punkty: [
        "Uczenie się · zadania i obowiązki · porozumiewanie się · motoryka",
        "Samodzielność · życie domowe · relacje · rola ucznia · społeczność lokalna",
        "Opis funkcjonalny zamiast etykiety diagnostycznej",
        "Ćwiczenie: przepisujemy zdanie oceniające na zdanie funkcjonalne" ]},
      { modul: "Skąd brać dane", czas: "90 min", punkty: [
        "Obserwacja ustrukturyzowana w klasie i podczas przerwy",
        "Wywiad z rodzicem — pytania, które faktycznie coś wnoszą",
        "Profil sensoryczny i model ABC jako źródła danych",
        "Co zrobić, gdy specjaliści widzą dziecko inaczej" ]},
      { modul: "Mocne strony, których nikt nie wpisuje", czas: "60 min", punkty: [
        "Zainteresowania jako zasób w planowaniu zajęć",
        "Teoria umysłu (ToM) i co z niej wynika dla pracy w grupie" ]},
      { modul: "Warsztat pisania", czas: "120 min", punkty: [
        "Praca na anonimowych przypadkach z Państwa placówki",
        "Redakcja: krótkie zdania, konkret, brak ocen wartościujących",
        "Przejście z WOPF-u do celów IPET-u — most, na którym najczęściej się gubi" ]},
    ],
    efekty: [
      "Piszesz ocenę funkcjonalną, z której cele wynikają same",
      "Wiesz, jakie dane zebrać przed posiedzeniem zespołu",
      "Rozpoznajesz zdania, które nic nie znaczą — i umiesz je przepisać",
    ],
    materialy: ["Szablon WOPF (Word) — ekosystem EduPlaner 2026", "Arkusze obserwacji i wywiadu z rodzicem", "Zestaw przykładowych opisów funkcjonalnych", "Zaświadczenie o ukończeniu"] },

  { kod: "B2", sciezka: "B", polecane: true,
    tytul: "IPET, który działa",
    podtytul: "Cele SMART w modelu KSzOF + ICF",
    opis: "Różnica między IPET-em użytecznym a IPET-em na półkę leży w jednym miejscu: w celach. Szkolenie jest w całości warsztatem pisania celów, które da się zmierzyć i po roku uczciwie ocenić.",
    czas: "8 godzin dydaktycznych", uczestnicy: "12–20 osób",
    dlaKogo: ["Zespoły opracowujące IPET", "Nauczyciele współorganizujący", "Pedagodzy specjalni i psycholodzy", "Dyrektorzy i wicedyrektorzy"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty", "Konsultacja wdrożeniowa"],
    program: [
      { modul: "Dziewięć sekcji IPET-u", czas: "60 min", punkty: [
        "Co musi się znaleźć, a co dopisujemy z ostrożności",
        "Podstawa prawna przy każdej sekcji — § 6 i § 7",
        "Kto podpisuje i za co odpowiada" ]},
      { modul: "Anatomia celu SMART", czas: "120 min", punkty: [
        "Pięć warunków: konkret, miara, osiągalność, istotność, termin",
        "Kryterium liczbowe: skąd brać „4 na 5 prób”, żeby nie było z sufitu",
        "Podpowiedź wpisana w cel — gestowa, wzrokowa, słowna, fizyczna",
        "Dwadzieścia celów do poprawienia — praca w parach" ]},
      { modul: "KSzOF i ICF przy celu", czas: "90 min", punkty: [
        "Dobór obszaru KSzOF do rzeczywistej trudności dziecka",
        "Kody ICF: d — aktywność i uczestniczenie, b — funkcje ciała, e — środowisko",
        "Kiedy jeden cel obsługuje dwa obszary, a kiedy trzeba go rozbić" ]},
      { modul: "Cel a poziom wsparcia", czas: "90 min", punkty: [
        "Ten sam cel na poziomie I, II i III — warsztat przepisywania",
        "Dlaczego wyższy poziom wsparcia to niższe kryterium samodzielności",
        "Powiązanie celu z formą realizacji i liczbą godzin" ]},
      { modul: "Dostosowania i system motywacyjny", czas: "60 min", punkty: [
        "Projektowanie uniwersalne zamiast listy wyjątków",
        "Model ABC w sekcji zarządzania emocjami" ]},
      { modul: "Ewaluacja od pierwszego dnia", czas: "60 min", punkty: [
        "Jak zapisać cel, żeby dało się go ocenić bez dodatkowej pracy",
        "Karta obserwacji jako załącznik" ]},
    ],
    efekty: [
      "Piszesz cele, które da się zmierzyć bez interpretacji",
      "Umiesz zapisać ten sam cel na trzech poziomach wsparcia",
      "Masz gotowe wzory zapisów z podstawą prawną",
    ],
    materialy: ["Szablon IPET (Word) — dziewięć sekcji rzymskich", "Katalog 60 wzorcowych celów SMART z kodami ICF", "Ściąga: obszary KSzOF i kody ICF", "Zaświadczenie o ukończeniu"] },

  { kod: "B3", sciezka: "B",
    tytul: "Trzy poziomy wsparcia",
    podtytul: "Kwalifikacja, formy pomocy i podstawa prawna",
    opis: "Krótkie, konkretne szkolenie o jednej decyzji: na jakim poziomie wsparcia jest to dziecko i co z tego wynika dla arkusza organizacyjnego. Dla zespołów, które mają IPET-y, ale nie mają pewności co do kwalifikacji.",
    czas: "4 godziny dydaktyczne", uczestnicy: "12–30 osób",
    dlaKogo: ["Dyrektorzy i wicedyrektorzy", "Koordynatorzy pomocy psychologiczno-pedagogicznej", "Zespoły opracowujące IPET"],
    formy: ["Rada szkoleniowa", "Webinar"],
    program: [
      { modul: "Poziom I — bieżąca praca z uczniem", czas: "45 min", punkty: [
        "Dostosowanie metod, form i warunków bez dodatkowych godzin",
        "Kiedy poziom I wystarcza — i kiedy jest udawaniem, że wystarcza" ]},
      { modul: "Poziom II — zajęcia specjalistyczne", czas: "60 min", punkty: [
        "Katalog form z rozporządzenia o pomocy psychologiczno-pedagogicznej",
        "Liczebność grup i wymiar godzin",
        "Kto może prowadzić które zajęcia" ]},
      { modul: "Poziom III — rewalidacja i wsparcie indywidualne", czas: "60 min", punkty: [
        "Nauczyciel współorganizujący a pomoc nauczyciela — różnica, o którą najczęściej się potyka",
        "Zajęcia rewalidacyjne: wymiar, dobór, dokumentowanie" ]},
      { modul: "Decyzja i jej konsekwencje", czas: "45 min", punkty: [
        "Ścieżka decyzyjna zespołu — arkusz kwalifikacyjny",
        "Przełożenie na arkusz organizacyjny i budżet",
        "Zmiana poziomu w trakcie roku" ]},
    ],
    efekty: [
      "Kwalifikujesz dziecko do poziomu wsparcia świadomie, z podstawą prawną",
      "Wiesz, co każdy poziom oznacza w godzinach i etatach",
    ],
    materialy: ["Arkusz kwalifikacyjny do poziomu wsparcia", "Zestawienie podstaw prawnych", "Zaświadczenie o ukończeniu"] },

  { kod: "B4", sciezka: "B",
    tytul: "Ewaluacja IPET-u",
    podtytul: "Jak udowodnić, że program zadziałał",
    opis: "Ocena efektywności bywa pisana zdaniem „cele zostały osiągnięte w stopniu zadowalającym”. Szkolenie pokazuje, jak zbierać dowody przez cały rok, żeby ewaluacja pisała się sama — i broniła podczas kontroli.",
    czas: "4 godziny dydaktyczne", uczestnicy: "12–25 osób",
    dlaKogo: ["Zespoły opracowujące IPET", "Dyrektorzy", "Nauczyciele współorganizujący", "Specjaliści prowadzący zajęcia"],
    formy: ["Rada szkoleniowa", "Webinar", "Konsultacja wdrożeniowa"],
    program: [
      { modul: "Ewaluacja zaczyna się przy pisaniu celu", czas: "45 min", punkty: [
        "Cel niemierzalny to ewaluacja niemożliwa — przykłady z życia",
        "Punkt odniesienia: pomiar wyjściowy przed rozpoczęciem pracy" ]},
      { modul: "Zbieranie danych w ciągu roku", czas: "75 min", punkty: [
        "Karta obserwacji zachowań docelowych — jak ją wypełniać bez dodatkowej pracy",
        "Wytwory dziecka jako dowód: prace, nagrania, zdjęcia",
        "Zgody rodziców na dokumentowanie" ]},
      { modul: "Pisanie oceny efektywności", czas: "75 min", punkty: [
        "Struktura: cel — dane — wniosek — rekomendacja",
        "Co zrobić z celem nieosiągniętym: modyfikacja, przedłużenie, wycofanie",
        "Warsztat na przykładach uczestników" ]},
      { modul: "Rozmowa z rodzicem o wynikach", czas: "45 min", punkty: [
        "Jak przekazać brak postępu, nie odbierając nadziei",
        "Rekomendacje do dalszej diagnozy" ]},
    ],
    efekty: [
      "Masz system zbierania dowodów, który nie generuje nadgodzin",
      "Piszesz ocenę efektywności opartą na liczbach, nie na wrażeniu",
    ],
    materialy: ["Karty obserwacji do wydruku", "Wzór oceny efektywności", "Zaświadczenie o ukończeniu"] },

  /* ── Ścieżka C ─────────────────────────────────────────────────────── */
  { kod: "C1", sciezka: "C",
    tytul: "Uczeń w spektrum autyzmu w grupie ogólnodostępnej",
    podtytul: "Praktyka przy realnej liczbie dzieci w klasie",
    opis: "Szkolenie dla tych, którzy mają w klasie dwadzieścioro pięcioro dzieci i jedno orzeczenie, a wszystkie rady zaczynają się od słowa „indywidualnie”. Rozwiązania, które da się zastosować przy tablicy, nie tylko w gabinecie.",
    czas: "8 godzin dydaktycznych", uczestnicy: "12–30 osób",
    dlaKogo: ["Nauczyciele przedmiotowi i wychowawcy", "Nauczyciele wychowania przedszkolnego", "Nauczyciele współorganizujący", "Pomoc nauczyciela i asystenci"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty"],
    program: [
      { modul: "Jak wygląda świat ucznia w spektrum", czas: "75 min", punkty: [
        "Przetwarzanie sensoryczne: dlaczego świetlówka bywa gorsza od klasówki",
        "Teoria umysłu i funkcje wykonawcze w praktyce lekcyjnej",
        "Sztywność i potrzeba przewidywalności — co za tym stoi" ]},
      { modul: "Przestrzeń i organizacja dnia", czas: "90 min", punkty: [
        "Miejsce w sali, oświetlenie, poziom hałasu",
        "Plan dnia obrazkowy i zapowiadanie zmian",
        "Umówiony sygnał przerwy i miejsce na ochłonięcie" ]},
      { modul: "Komunikacja", czas: "90 min", punkty: [
        "Polecenia: krótko, po kolei, bez metafor",
        "Czas na odpowiedź — cisza, której dorośli nie wytrzymują",
        "Karty komunikacyjne w klasie ogólnodostępnej" ]},
      { modul: "Przeciążenie i wycofanie", czas: "90 min", punkty: [
        "Wczesne sygnały przed wybuchem — czego szukać",
        "Co robić w trakcie, a czego nigdy nie robić",
        "Rozmowa po — kiedy i jak" ]},
      { modul: "Grupa rówieśnicza", czas: "60 min", punkty: [
        "Jak rozmawiać z klasą o koledze — i czy w ogóle",
        "Moderowana praca w parach zamiast wymuszonej integracji" ]},
    ],
    efekty: [
      "Masz zestaw dostosowań możliwych do wprowadzenia w klasie liczącej 25 osób",
      "Rozpoznajesz sygnały przeciążenia, zanim dojdzie do wybuchu",
      "Wiesz, jak zapowiadać zmiany, żeby nie kosztowały całej lekcji",
    ],
    materialy: ["Zestaw piktogramów do planu dnia", "Karty „Przerwa” i „Potrzebuję pomocy”", "Lista kontrolna dostosowań w sali", "Zaświadczenie o ukończeniu"] },

  { kod: "C2", sciezka: "C",
    tytul: "Zachowania trudne — model ABC",
    podtytul: "Od opisu zdarzenia do zmiany, która się utrzymuje",
    opis: "Zachowanie trudne prawie zawsze coś komunikuje. Model ABC pozwala odczytać, co dokładnie — i zmienić warunki, zamiast walczyć z objawem. Szkolenie w całości oparte na analizie realnych sytuacji.",
    czas: "8 godzin dydaktycznych", uczestnicy: "12–20 osób",
    dlaKogo: ["Nauczyciele i wychowawcy", "Pedagodzy specjalni i psycholodzy", "Nauczyciele współorganizujący", "Zespoły ośrodków i świetlic"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty", "Konsultacja wdrożeniowa"],
    program: [
      { modul: "Zachowanie jako komunikat", czas: "60 min", punkty: [
        "Cztery funkcje zachowania: uwaga, ucieczka, dostęp, autostymulacja",
        "Dlaczego kara wzmacnia zachowanie, które miała wygasić" ]},
      { modul: "Poprzednik — Zachowanie — Konsekwencja", czas: "120 min", punkty: [
        "Opis zachowania w kategoriach obserwowalnych, bez interpretacji",
        "Arkusz ABC: jak go wypełniać, żeby dane były użyteczne",
        "Ćwiczenie na nagraniach i opisach przypadków" ]},
      { modul: "Hipoteza funkcji i plan", czas: "120 min", punkty: [
        "Od danych do hipotezy — praca zespołowa",
        "Modyfikacja poprzedników: co zmienić przed zachowaniem",
        "Zachowanie alternatywne: czego uczymy zamiast",
        "Spójność konsekwencji w całym zespole" ]},
      { modul: "Sytuacje kryzysowe", czas: "60 min", punkty: [
        "Procedura postępowania w placówce",
        "Bezpieczeństwo dziecka, grupy i dorosłego",
        "Dokumentowanie zdarzenia" ]},
      { modul: "Współpraca z rodziną", czas: "60 min", punkty: [
        "Rozmowa bez oskarżania",
        "Spójność oddziaływań dom — placówka" ]},
    ],
    efekty: [
      "Opisujesz zachowanie tak, że dwie osoby zapiszą je tak samo",
      "Stawiasz hipotezę funkcji i budujesz na niej plan",
      "Masz gotową procedurę na sytuację kryzysową",
    ],
    materialy: ["Arkusze ABC do wydruku", "Wzór planu modyfikacji zachowania", "Procedura kryzysowa do adaptacji", "Zaświadczenie o ukończeniu"] },

  { kod: "C3", sciezka: "C",
    tytul: "Dostosowania w projektowaniu uniwersalnym",
    podtytul: "Jeden materiał, piętnaście dróg",
    opis: "Zamiast robić osobny materiał dla każdego dziecka — zaprojektować jeden tak, żeby działał dla wszystkich. Szkolenie pokazuje piętnaście grup potrzeb i konkretne dostosowanie dla każdej, na tym samym materiale.",
    czas: "6 godzin dydaktycznych", uczestnicy: "12–30 osób",
    dlaKogo: ["Nauczyciele wszystkich etapów edukacyjnych", "Autorzy materiałów i kart pracy", "Nauczyciele współorganizujący", "Bibliotekarze i nauczyciele świetlic"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty", "Webinar (4 h)"],
    program: [
      { modul: "Projektowanie uniwersalne zamiast listy wyjątków", czas: "60 min", punkty: [
        "To, co konieczne dla jednego, pomaga wszystkim — zasada i jej granice",
        "Sześć rzeczy, które da się dostosować raz, na etapie tworzenia materiału" ]},
      { modul: "Typografia i skład, które czytają się same", czas: "75 min", punkty: [
        "Kroje o wysokiej czytelności — Atkinson Hyperlegible i alternatywy",
        "Tekst niejustowany, interlinia, długość wiersza",
        "Kontrast, wydruk A3, praca na ekranie" ]},
      { modul: "Piętnaście grup potrzeb", czas: "150 min", punkty: [
        "Spektrum autyzmu · ADHD · niepełnosprawność intelektualna lekka i umiarkowana",
        "Dysleksja · słabowzroczność · niedosłuch",
        "Mutyzm wybiórczy · uczeń niemówiący i AAC · afazja",
        "Zaburzenia lękowe · przetwarzanie sensoryczne · niepełnosprawność ruchowa",
        "Zaburzenia zachowania · FASD i funkcje wykonawcze" ]},
      { modul: "Warsztat: przerabiamy Państwa materiał", czas: "75 min", punkty: [
        "Uczestnicy przynoszą własną kartę pracy",
        "Dostosowanie na miejscu, w trzech wariantach",
        "Zapis dostosowania do IPET-u" ]},
    ],
    efekty: [
      "Projektujesz materiał, którego nie trzeba potem przerabiać dla trojga dzieci",
      "Masz gotowe formuły dostosowań do wpisania w dokumentację",
    ],
    materialy: ["Karta piętnastu grup potrzeb z gotowymi zapisami", "Lista kontrolna czytelności materiału", "Zaświadczenie o ukończeniu"] },

  /* ── Ścieżka D ─────────────────────────────────────────────────────── */
  { kod: "D1", sciezka: "D",
    tytul: "Komunikacja alternatywna i wspomagająca",
    podtytul: "AAC — pierwsze kroki w przedszkolu i szkole",
    opis: "Dziecko, które nie mówi, nie znaczy, że nie ma nic do powiedzenia. Szkolenie wprowadzające: od pierwszej karty komunikacyjnej po tablicę, z której dziecko korzysta w klasie i w domu.",
    czas: "6 godzin dydaktycznych", uczestnicy: "12–20 osób",
    dlaKogo: ["Nauczyciele i terapeuci pracujący z dzieckiem niemówiącym", "Logopedzi", "Nauczyciele współorganizujący", "Rodzice — na życzenie placówki"],
    formy: ["Rada szkoleniowa", "Warsztat otwarty"],
    program: [
      { modul: "Kto potrzebuje AAC", czas: "45 min", punkty: [
        "Brak mowy czynnej, mowa niefunkcjonalna, mowa zawodząca w stresie",
        "Mit, który wciąż wraca: „AAC zablokuje mowę” — co mówią badania" ]},
      { modul: "Od czego zacząć", czas: "90 min", punkty: [
        "Pierwsze karty: prośba, odmowa, przerwa, pomoc",
        "Karta „Nie wiem jeszcze” — sygnał, którego brakuje najczęściej",
        "Symbole: dobór, rozmiar, laminowanie, mocowanie" ]},
      { modul: "Tablica i książka komunikacyjna", czas: "90 min", punkty: [
        "Układ tablicy i logika rozmieszczenia symboli",
        "Rozbudowa w czasie — kiedy dokładać kolejne pola",
        "Modelowanie: dorosły też pokazuje, nie tylko mówi" ]},
      { modul: "AAC w codzienności grupy", czas: "90 min", punkty: [
        "Komunikacja w kręgu, przy stole, na wyjściu",
        "Rówieśnicy jako partnerzy komunikacyjni",
        "Spójność między placówką a domem" ]},
      { modul: "Dokumentowanie i cele", czas: "45 min", punkty: [
        "Cel SMART dla umiejętności komunikacyjnej",
        "Kody ICF przy komunikacji: d310, d330, d335, d360" ]},
    ],
    efekty: [
      "Wprowadzasz pierwszy zestaw kart w tydzień po szkoleniu",
      "Wiesz, jak modelować i dlaczego bez tego AAC nie ruszy",
    ],
    materialy: ["Zestaw startowy kart komunikacyjnych do wydruku", "Wzór tablicy komunikacyjnej", "Zaświadczenie o ukończeniu"] },

  { kod: "D2", sciezka: "D",
    tytul: "EduPlaner 2026 — dokumentacja bez nadgodzin",
    podtytul: "Wdrożenie aplikacji w placówce",
    opis: "Szkolenie z narzędzia: jak z jednego zestawu danych o dziecku powstaje WOPF, IPET, raport dla dyrekcji i wpis do bazy uczniów — bez trzykrotnego przepisywania tego samego.",
    czas: "4 godziny dydaktyczne", uczestnicy: "8–20 osób",
    dlaKogo: ["Zespoły opracowujące dokumentację", "Dyrektorzy i koordynatorzy pomocy p-p", "Sekretariaty prowadzące ewidencję"],
    formy: ["Rada szkoleniowa", "Webinar", "Konsultacja wdrożeniowa"],
    program: [
      { modul: "Jedno źródło danych", czas: "45 min", punkty: [
        "Karta dziecka jako punkt wyjścia dla wszystkich dokumentów",
        "Co wpisujemy raz, a co ciągnie się automatycznie" ]},
      { modul: "Cztery dokumenty z jednego wpisu", czas: "90 min", punkty: [
        "WOPF — ocena funkcjonalna",
        "IPET — dziewięć sekcji z celami SMART",
        "Raport ucznia — synteza dla dyrekcji i rodzica",
        "Baza uczniów — ewidencja i zestawienia" ]},
      { modul: "Moduł realizacji zajęć", czas: "60 min", punkty: [
        "Planowanie i rozliczanie godzin",
        "Powiązanie zajęć z celami IPET-u" ]},
      { modul: "Wdrożenie i bezpieczeństwo danych", czas: "45 min", punkty: [
        "Podział ról w zespole",
        "Przechowywanie danych wrażliwych — o czym pamiętać" ]},
    ],
    efekty: [
      "Wychodzisz z gotowym do pracy zestawem szablonów",
      "Skracasz czas przygotowania kompletu dokumentów dla jednego dziecka",
    ],
    materialy: ["Komplet szablonów: WOPF, IPET, Raport, Baza", "Instrukcja wdrożenia dla zespołu", "Zaświadczenie o ukończeniu"] },
];

const PAKIETY = [
  { nazwa: "Pakiet przedszkolny", kod: "P-PRZ", sklad: ["A2", "C1", "C3"],
    opis: "Trzy szkolenia dla zespołu przedszkola: emocje w grupie 3–6 lat, dziecko w spektrum i dostosowania materiałów. Realizacja w ciągu jednego semestru.",
    bonus: "Konsultacja wdrożeniowa po ostatnim szkoleniu — w cenie pakietu." },
  { nazwa: "Pakiet dokumentacyjny", kod: "P-DOK", sklad: ["B1", "B2", "B3", "B4"],
    opis: "Pełna ścieżka dokumentacyjna: od oceny funkcjonalnej, przez cele SMART i kwalifikację do poziomu wsparcia, po ewaluację. Dla zespołów, które chcą raz uporządkować cały cykl.",
    bonus: "Przegląd trzech IPET-ów z Państwa placówki z pisemną informacją zwrotną." },
  { nazwa: "Pakiet szkolny", kod: "P-SZK", sklad: ["A1", "C1", "C2"],
    opis: "Dla szkół podstawowych i ponadpodstawowych z uczniami z orzeczeniami: praca z emocjami, uczeń w spektrum w klasie i zachowania trudne.",
    bonus: "Superwizja zespołu po trzech miesiącach — online." },
];

module.exports = { SCIEZKI, FORMY, SZKOLENIA, PAKIETY };
