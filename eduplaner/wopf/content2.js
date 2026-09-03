const L = require('./lib.js');
const { section, howto, lead, legal, note, ta, fields, checks, table, scale, bars, signatures, brk, text, subhead, C, AlignmentType } = L;

const B = [];
const add = (...xs) => xs.forEach(x => Array.isArray(x) ? B.push(...x) : B.push(x));

/* ====================== VII. TEORIA UMYSŁU ====================== */
add(section('VII', 'Poznanie społeczne — teoria umysłu', 'przeniesienie z druku: ToM · skala 0–2'));
add(table(['Lp.', 'Komponent ToM · kod ICF', 'Wynik (0–2)', 'Wniosek do pracy'],
  [
    ['K1', 'Świadomość emocji własnych · b152', '', ''],
    ['K2', 'Rozpoznawanie emocji innych · b1522 · d7104', '', ''],
    ['K3', 'Przyjmowanie perspektywy · d710 · d7203', '', ''],
    ['K4', 'Rozumienie intencji · d7102', '', ''],
    ['K5', 'Język niedosłowny — żart, przenośnia · d310 · d3102', '', '']
  ], [700, 4046, 1400, 3600], { center: [0, 2], rowHeight: 400 }));
add(ta('Kierunek pracy — poznanie społeczne (TUS, historyjki społeczne, trening perspektywy, zabawa w udawanie)', { lines: 4, hint: 'Podpowiedź: Dziecko rozpoznaje podstawowe emocje i podąża za spojrzeniem, trudność sprawia mu rozumienie cudzych przekonań i intencji. Pracujemy w małej grupie: historyjki społeczne z pytaniem „co on teraz myśli / czuje?”, zabawa w udawanie i zamianę ról, komentowanie stanów umysłu w toku dnia. Elementy TUS włączamy do zajęć rewalidacyjnych.' }));
add(legal('Funkcje umysłowe i kontakty międzyludzkie: ICF (WHO 2001) — b152 emocje, b1522 zakres emocji, d710 podstawowe kontakty międzyludzkie, d7104 przyjmowanie perspektywy, d720 złożone kontakty. Trening umiejętności społecznych jest zajęciem obligatoryjnym dla dzieci z autyzmem, w tym z zespołem Aspergera — § 6 ust. 2 pkt 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578). W ścieżce B odpowiednikiem są zajęcia rozwijające kompetencje emocjonalno-społeczne — § 6 ust. 1 pkt 4 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591).'));

add(brk());

/* ====================== VIII. MOWA ====================== */
add(section('VIII', 'Mowa i komunikacja', 'przeniesienie z druku: kwestionariusz rozwoju mowy'));
add(table(['Lp.', 'Dział kwestionariusza', 'Wynik', 'Wniosek'],
  [
    ['I', 'Rozumienie mowy (recepcja)', '', ''],
    ['II', 'Mowa czynna — słownik i zdanie', '', ''],
    ['III', 'Artykulacja i sprawność aparatu mowy', '', ''],
    ['IV', 'Komunikacja w grupie — funkcje pragmatyczne', '', ''],
    ['V', 'Karmienie, oddech, funkcje prymarne', '', '']
  ], [700, 4046, 1400, 3600], { center: [0, 2], rowHeight: 380 }));
add(subhead('Sposób porozumiewania się dziecka w grupie — zaznacz stosowane formy'));
add(checks([
  'mowa werbalna wystarczająca', 'gest naturalny',
  'piktogramy / PCS', 'MAKATON',
  'PECS', 'tablica komunikacyjna',
  'komunikator / aplikacja AAC', 'inne — jakie?'
], 2));

add(brk());

add(subhead('Kierunki terapii logopedycznej — zaznacz rekomendowane'));
add(checks([
  'budowanie i poszerzanie słownika biernego (rozumienie)', 'budowanie słownika czynnego i wypowiedzi zdaniowej',
  'ćwiczenia oddechowe i fonacyjne', 'usprawnianie motoryki narządów mowy (wargi, język, podniebienie)',
  'korekta artykulacji głosek — wywołanie i utrwalanie', 'słuch fonemowy oraz analiza i synteza sylabowa',
  'terapia funkcji prymarnych — jedzenie, picie, gryzienie, połykanie', 'terapia miofunkcjonalna i pionizacja języka',
  'wprowadzenie lub rozwijanie komunikacji wspomagającej (AAC)', 'pragmatyka — inicjowanie, prośba, odmowa, dialog w grupie',
  'profilaktyka jąkania i płynność wypowiedzi', 'współpraca z rodzicem — ćwiczenia do domu'
], 2));
add(ta('Kierunek pracy logopedycznej i sposób porozumiewania się w grupie', { lines: 4, hint: 'Podpowiedź: Rozumienie mowy wyprzedza wypowiadanie się; wypowiedzi są krótkie, wymowa uproszczona, zrozumiała głównie dla znanych osób. Kierunek pracy: usprawnianie aparatu artykulacyjnego, poszerzanie słownika czynnego, budowanie zdania prostego. W grupie stosujemy komunikaty krótkie i pojedyncze, wsparcie obrazkowe i gest, dajemy czas na odpowiedź oraz modelujemy poprawną formę bez poprawiania wprost.' }));
add(legal('Zajęcia logopedyczne organizuje się dla dzieci z deficytami kompetencji i zaburzeniami sprawności językowych — § 6 ust. 1 pkt 3 i § 14 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591). Dla dziecka z orzeczeniem zajęcia rozwijające komunikowanie się i naukę alternatywnych metod komunikacji ujmuje się w IPET — § 6 ust. 1 pkt 5 i ust. 2 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578). Podstawa programowa wychowania przedszkolnego (Dz.U. 2017 poz. 356). Kody ICF: b320 funkcje artykulacyjne, b167 funkcje językowe, d310–d345 porozumiewanie się, e125 produkty i technologie do komunikowania się.'));

add(brk());

/* ====================== IX. SENSORYKA ====================== */
add(section('IX', 'Przetwarzanie sensoryczne', 'przeniesienie z druku: profil sensoryczny (Dunn)'));
add(table(['Lp.', 'Układ zmysłowy', 'Wzorzec przetwarzania', 'Dieta sensoryczna i dostosowania'],
  [
    ['I', 'Wzrok', '', ''],
    ['II', 'Słuch', '', ''],
    ['III', 'Dotyk (w tym sfera oralna)', '', ''],
    ['IV', 'Smak', '', ''],
    ['V', 'Węch', '', ''],
    ['VI', 'Propriocepcja — czucie głębokie', '', ''],
    ['VII', 'Układ przedsionkowy — równowaga i ruch', '', '']
  ], [700, 3046, 2600, 3400], { center: [0], rowHeight: 400 }));
add(note('Wzorzec przetwarzania — legenda:', 'w normie · poszukujący (podwrażliwy) · unikający (nadwrażliwy) · niska rejestracja. Wzorzec przenosi się z profilu sensorycznego; w ostatniej kolumnie wpisuje się konkretne propozycje diety sensorycznej i dostosowań w sali oraz w ogrodzie przedszkolnym.', '2B6E6E'));
add(ta('Wnioski sensoryczne — organizacja sali, przerwy regulacyjne, sygnały przeciążenia', { lines: 4, hint: 'Podpowiedź: Profil wskazuje na wrażliwość słuchową i poszukiwanie bodźców przedsionkowo-proprioceptywnych. Organizacja sali: stałe miejsce z dala od źródeł hałasu, kącik wyciszenia dostępny bez proszenia, ograniczenie dekoracji w polu widzenia. Przerwy regulacyjne co 20–30 minut (ruch, docisk, dźwiganie, huśtanie). Sygnały przeciążenia: zatykanie uszu, wzmożona ruchliwość, wycofanie i milknięcie — reagujemy wtedy przerwą, zanim pojawi się zachowanie trudne.' }));
add(legal('Uwarunkowania psychofizyczne dziecka jako element oceny — § 6 ust. 10 pkt 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578). Terapia integracji sensorycznej jako zajęcie o charakterze terapeutycznym — § 6 ust. 1 pkt 6 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591). Metodologia: model przetwarzania sensorycznego W. Dunn (1997) — cztery wzorce: niska rejestracja, poszukiwanie, wrażliwość, unikanie. Kody ICF: b156 funkcje postrzegania, b235 funkcje przedsionkowe, b260 czucie proprioceptywne, b265 dotyk, e240 światło, e250 dźwięk.'));

add(brk());

/* ====================== X. KONTEKST ====================== */
add(section('X', 'Kontekst biopsychospołeczny — czynniki środowiskowe ICF', 'przeniesienie z profilu biopsychospołecznego'));
add(checks([
  'Wsparcie i zaangażowanie rodziny (e310 · e410)', 'Relacje i akceptacja rówieśników w grupie (e320 · e425)',
  'Postawy nauczycieli i specjalistów (e330 · e430)', 'Dostosowania i pomoce dydaktyczne w sali (e130)',
  'Technologie wspomagające / AAC (e125)', 'Dostępność architektoniczna przedszkola (e150)',
  'Warunki sensoryczne otoczenia — hałas, światło (e240 · e250)', 'Wsparcie instytucji (poradnia pp, SCWEW) i usług (e585)',
  'Sytuacja bytowa i organizacja rytmu dnia (e310 · e165)', 'Leki i opieka zdrowotna w przedszkolu (e110 · e580)'
], 2));
add(ta('Ułatwienia — co w otoczeniu wspiera dziecko', { lines: 3, hint: 'Podpowiedź: Wspierają: przewidywalny rytm dnia i plan obrazkowy, stała, życzliwa relacja z nauczycielem, mała grupa, uprzedzanie o zmianach, dostęp do kącika wyciszenia, pochwała opisowa i rola pomocnika. Rodzice współpracują z przedszkolem i konsekwentnie stosują w domu te same sygnały i strategie.' }));
add(ta('Bariery — co w otoczeniu utrudnia funkcjonowanie i uczestnictwo', { lines: 3, hint: 'Podpowiedź: Utrudniają: hałas i duża liczba dzieci w sali, nagłe zmiany planu, długie polecenia złożone, pośpiech przy ubieraniu i posiłku, sytuacje rywalizacji oraz zabawy o nieokreślonych zasadach. Bariery te ograniczają uczestnictwo bardziej niż same ograniczenia dziecka — dlatego pracujemy przede wszystkim nad otoczeniem.' }));
add(ta('Dobrostan — samopoczucie, poczucie bezpieczeństwa, sprawczość, uczestnictwo w grupie', { lines: 3, hint: 'Podpowiedź: Dziecko czuje się bezpiecznie przy znanym dorosłym i w stałym rytmie dnia; chętnie przychodzi do przedszkola. Poczucie sprawczości wzrasta, gdy ma wybór i widoczny efekt swojego działania. Uczestnictwo w grupie jest częściowe — potrzebuje wprowadzenia w zabawę i pośrednictwa dorosłego w kontaktach z rówieśnikami.' }));
add(legal('Czynniki środowiskowe (bariery i ułatwienia) — § 6 ust. 10 pkt 3 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578; t.j. Dz.U. 2020 poz. 1309) w związku z modelem biopsychospołecznym klasyfikacji ICF (WHO 2001), rozdział „Czynniki środowiskowe” (e110–e599).'));

add(brk());

/* ====================== XI. CAŁOŚCIOWY OBRAZ ====================== */
add(section('XI', 'Całościowy obraz funkcjonowania — synteza wszystkich źródeł', 'mocne strony → trudności'));
add(howto('W każdym wierszu opisz najpierw mocne strony, dopiero potem trudności. Opis ma być konkretny i obserwowalny — podaj, co dziecko robi, w jakich sytuacjach dnia i przy jakim wsparciu dorosłego. Unikaj etykiet i ocen ogólnych; korzystaj z wyników przeniesionych w sekcjach V–X.'));
add(table(['Lp.', 'Obszar', 'Kody ICF', 'Źródło', 'Opis funkcjonowania — mocne strony i trudności'],
  [
    ['1', 'Poznawczy — uwaga, pamięć, myślenie', 'b140 · b144 · b164', 'KPOF I, VIII', ''],
    ['2', 'Społeczny — relacje i współdziałanie', 'd710–d750', 'KPOF VII, IX · ToM', ''],
    ['3', 'Emocjonalny — regulacja, lęk, nastrój', 'b152 · b1263', 'KPOF II · ABC/FBA', ''],
    ['4', 'Komunikacja i mowa', 'd310–d360 · b320', 'Kwestionariusz mowy · KPOF III', ''],
    ['5', 'Zachowanie — zachowania trudne', 'b1250 · b1252', 'ABC/FBA', ''],
    ['6', 'Sensoryczno-motoryczny', 'b156 · b760 · b147', 'Profil sensoryczny · KPOF IV', ''],
    ['7', 'Samoobsługa i samodzielność', 'd510–d570', 'KPOF V, VI', ''],
    ['8', 'Zabawa i uczestnictwo w grupie', 'd880 · d920', 'KPOF VIII · obserwacja', '']
  ], [600, 2500, 1500, 1946, 3200], { center: [0], rowHeight: 620 }));
add(legal('Wielospecjalistyczny i całościowy charakter oceny — § 6 ust. 4 i 10 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578); w ścieżce B — § 20 ust. 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591). Struktura opisu (funkcje i struktury ciała · aktywność i uczestniczenie · czynniki kontekstowe) wynika z klasyfikacji ICF (WHO 2001) oraz z Modelu Szkolnej Oceny Funkcjonalnej (MEN 2024), który nakazuje opis w kategoriach funkcjonalnych i kolejność „mocne strony → trudności”.'));

add(brk());

/* ====================== XII. POTRZEBY ====================== */
add(section('XII', 'Indywidualne potrzeby rozwojowe i edukacyjne', '§ 6 ust. 10 pkt 1'));
add(ta('Indywidualne potrzeby rozwojowe i edukacyjne dziecka', { lines: 4, hint: 'Podpowiedź: Dziecko potrzebuje: przewidywalności i uprzedzania o zmianach, komunikatów krótkich ze wsparciem obrazkowym, zadań podzielonych na etapy z wyraźnym sygnałem końca, przerw regulacyjnych, pośrednictwa dorosłego w kontaktach z rówieśnikami oraz konsekwentnego wzmacniania zachowań pożądanych. Potrzeby wynikają wprost ze średnich w obszarach ICF oraz z wniosków obserwacji pogłębionej.' }));
add(ta('Mocne strony — co dziecko już potrafi', { lines: 4, hint: 'Podpowiedź: Dziecko porusza się sprawnie i chętnie podejmuje aktywność ruchową, rozumie proste polecenia, sygnalizuje potrzeby fizjologiczne, samodzielnie je i myje ręce, dobrze zapamiętuje ulubione treści i piosenki, reaguje na pochwałę oraz nawiązuje kontakt z wybranym dorosłym. Na tych zasobach opieramy plan wsparcia.' }));
add(ta('Zainteresowania, predyspozycje i to, co dziecko motywuje', { lines: 4, hint: 'Podpowiedź: Angażują je zabawy konstrukcyjne (klocki, pojazdy), aktywności ruchowe w ogrodzie, muzyka i rytm oraz ulubione tematy. Motywuje pochwała opisowa, „sukces na start”, wybór z dwóch opcji, rola pomocnika nauczyciela i drobne przywileje. Te motywatory wykorzystujemy jako wzmocnienia w codziennej pracy.' }));
add(legal('ŚCIEŻKA A — § 6 ust. 10 pkt 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578): ocena uwzględnia „indywidualne potrzeby rozwojowe i edukacyjne, mocne strony, predyspozycje, zainteresowania i uzdolnienia ucznia”. ŚCIEŻKA B — § 20 ust. 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591): nauczyciele i specjaliści rozpoznają indywidualne potrzeby rozwojowe i edukacyjne oraz możliwości psychofizyczne dziecka, w tym jego zainteresowania i uzdolnienia.'));

add(brk());

/* ====================== XIII. PRZYCZYNY ====================== */
add(section('XIII', 'Przyczyny trudności, bariery i ograniczenia', '§ 6 ust. 10 pkt 3'));
add(table(['Lp.', 'Zakres', 'Źródło obserwacji', 'Opis'],
  [
    ['1', 'Przyczyny trudności w uczeniu się i w zabawie', 'KPOF (obsz. I, VIII)', ''],
    ['2', 'Trudności w funkcjonowaniu w grupie', 'KPOF · ABC/FBA', ''],
    ['3', 'Bariery i ograniczenia uczestnictwa', 'profil sensoryczny · ToM', ''],
    ['4', 'Ograniczenia sensoryczne (wzrok, słuch, przetwarzanie)', 'profil sensoryczny · b210 · b230 · b156', ''],
    ['5', 'Uwarunkowania medyczne (choroby przewlekłe, leki)', 'dane medyczne — sekcja IV', ''],
    ['6', 'Trudności włączenia w zajęcia i zabawę z grupą', 'obserwacja w kontekstach', ''],
    ['7', 'Efekty działań podjętych w celu ich przezwyciężenia', 'dziennik obserwacji / ewaluacja', '']
  ], [600, 3346, 2400, 3400], { center: [0], rowHeight: 620 }));
add(legal('§ 6 ust. 10 pkt 3 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578): „przyczyny niepowodzeń edukacyjnych lub trudności w funkcjonowaniu ucznia, w tym bariery i ograniczenia utrudniające funkcjonowanie i uczestnictwo ucznia w życiu przedszkolnym lub szkolnym (…), oraz efekty działań podejmowanych w celu ich przezwyciężenia”. W ścieżce B analogiczne rozpoznanie przyczyn trudności i barier prowadzi się na podstawie § 20 ust. 1 i 7 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591) — wraz z oceną efektywności dotychczas udzielanej pomocy.'));

add(brk());

/* ====================== XIV. ZAKRES WSPARCIA ====================== */
add(section('XIV', 'Zakres i charakter wsparcia', '§ 6 ust. 10 pkt 2'));
add(checks([
  'wsparcie nauczyciela w bieżącej pracy w grupie', 'nauczyciel współorganizujący kształcenie',
  'pomoc nauczyciela', 'pedagog specjalny',
  'psycholog', 'logopeda',
  'terapeuta SI', 'fizjoterapeuta',
  'zintegrowane działania nauczycieli i specjalistów', 'inne — jakie?'
], 2));
add(ta('Doprecyzowanie — wymiar i organizacja wsparcia', { lines: 5, hint: 'Podpowiedź: Wsparcie realizujemy w wymiarze wynikającym z orzeczenia: zajęcia rewalidacyjne 2 × 60 minut tygodniowo (indywidualnie) oraz zajęcia z zakresu pomocy psychologiczno-pedagogicznej w małej grupie. W czasie zajęć grupowych dziecko korzysta ze wsparcia nauczyciela współorganizującego kształcenie; stosujemy stałe miejsce, plan obrazkowy i przerwy regulacyjne. Organizację weryfikujemy przy ocenie okresowej.' }));
add(legal('ŚCIEŻKA A — § 6 ust. 10 pkt 2 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578): „w zależności od potrzeb — zakres i charakter wsparcia ze strony nauczycieli, specjalistów lub pomocy nauczyciela, o których mowa w § 7 ust. 1–5”; dodatkowe zatrudnienie specjalistów i pomocy nauczyciela reguluje § 7 tego rozporządzenia. ŚCIEŻKA B — pomocy udzielają nauczyciele oraz specjaliści wykonujący zadania z zakresu pomocy psychologiczno-pedagogicznej: § 5 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591). Zatrudnienie pedagoga specjalnego i psychologa — art. 42d ustawy z 26.01.1982 r. — Karta Nauczyciela (t.j. Dz.U. 2024 poz. 986, z późn. zm.).'));

add(brk());

/* ====================== XV. REKOMENDOWANE ZAJĘCIA ====================== */
add(section('XV', 'Rekomendowane zajęcia', 'dwie osobne rubryki'));
add(subhead('Zajęcia rewalidacyjne (dla dziecka z orzeczeniem o potrzebie kształcenia specjalnego)'));
add(checks([
  'rewalidacja indywidualna — komunikacja i AAC', 'rewalidacja indywidualna — umiejętności społeczne i teoria umysłu',
  'rewalidacja indywidualna — percepcja i koordynacja wzrokowo-ruchowa', 'terapia ręki',
  'trening samoobsługi i samodzielności', 'trening umiejętności społecznych (TUS) — obowiązkowy przy autyzmie i zespole Aspergera',
  'orientacja przestrzenna i poruszanie się', 'nauka alternatywnych metod komunikacji'
], 2));
add(subhead('Zajęcia z pomocy psychologiczno-pedagogicznej'));
add(checks([
  'zajęcia korekcyjno-kompensacyjne', 'zajęcia logopedyczne',
  'zajęcia rozwijające kompetencje emocjonalno-społeczne', 'zajęcia rozwijające umiejętność uczenia się',
  'zajęcia o charakterze terapeutycznym', 'terapia integracji sensorycznej',
  'zajęcia rozwijające uzdolnienia', 'porady i konsultacje dla rodziców',
  'zindywidualizowana ścieżka realizacji wychowania przedszkolnego', 'inne — jakie?'
], 2));
add(note('Wymiar godzin.', 'Wymiar godzin ustala dyrektor przedszkola w indywidualnym programie edukacyjno-terapeutycznym oraz w arkuszu organizacji pracy przedszkola — tutaj zespół wskazuje wyłącznie rodzaj zajęć. Zajęcia rewalidacyjne przysługują dziecku posiadającemu orzeczenie o potrzebie kształcenia specjalnego; pozostałe formy realizuje się w ramach pomocy psychologiczno-pedagogicznej.'));
add(legal('ŚCIEŻKA A — zajęcia rewalidacyjne oraz zajęcia obowiązkowe dla wybranych niepełnosprawności (orientacja przestrzenna i poruszanie się, alternatywne metody komunikacji, umiejętności społeczne przy autyzmie i zespole Aspergera): § 6 ust. 1 pkt 5 i ust. 2 oraz § 5 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578; t.j. Dz.U. 2020 poz. 1309). ŚCIEŻKA B — formy pomocy psychologiczno-pedagogicznej w przedszkolu: § 6 ust. 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591, z późn. zm.). Wymiar godzin ustala dyrektor — § 7 rozp. poz. 1591 i arkusz organizacji przedszkola.'));

add(brk());

/* ====================== XVI. DECYZJA ====================== */
add(section('XVI', 'Decyzja posiedzenia zespołu — rekomendowany poziom wsparcia', 'zaznacz jeden poziom'));
add(checks([
  'Poziom I · śr. 3,0–3,9 — wsparcie w bieżącej pracy wychowawczo-dydaktycznej nauczyciela',
  'Poziom II · śr. 2,0–2,9 — wsparcie dodatkowe: pomoc psychologiczno-pedagogiczna w przedszkolu',
  'Poziom III · śr. < 2,0 — wsparcie specjalistyczne: moduły pogłębiające, WOPF, poradnia pp'
], 1));
add(fields([
  { label: 'Rekomendowany poziom wsparcia', value: '' },
  { label: 'Data posiedzenia zespołu', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Kierunek dalszej pracy', value: '', hint: 'opracowanie / modyfikacja IPET (ścieżka A) · ustalenie form pomocy pp (ścieżka B)' },
  { label: 'Termin kolejnej oceny', value: '', hint: 'dd.mm.rrrr' }
], 2));
add(ta('Cel SMART — edukacyjny (obszar priorytetowy z KPOF)', { lines: 4, hint: 'Podpowiedź: Do końca I półrocza dziecko w obszarze … samodzielnie dołączy do zabawy w parze z rówieśnikiem po jednym sygnale nauczyciela, w 4 z 5 kolejnych sytuacji zabawy swobodnej. Pomiar: karta obserwacji prowadzona raz w tygodniu przez nauczyciela grupy.' }));
add(ta('Cel SMART — terapeutyczny / specjalistyczny (obszar priorytetowy z obserwacji pogłębionej)', { lines: 4, hint: 'Podpowiedź: Do końca I półrocza dziecko zamiast zachowania trudnego użyje karty „przerwa” w sytuacji zadania wymagającego dłuższej uwagi — w 4 z 5 kolejnych zajęć kierowanych, przy jednym wskazaniu dorosłego. Cel wynika z hipotezy funkcjonalnej (ucieczka od wymagania). Pomiar: rejestr zachowań prowadzony przez specjalistę na każdych zajęciach.' }));
add(legal('Rozp. MEN z 9.08.2017 r. w sprawie pomocy psychologiczno-pedagogicznej (Dz.U. 2017 poz. 1591, z późn. zm.). Rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578) — § 6: WOPF jako podstawa IPET. Model Szkolnej Oceny Funkcjonalnej (MEN 2024) — trzystopniowa skala wsparcia. Ustawa — Prawo oświatowe (t.j. Dz.U. 2024 poz. 737, z późn. zm.), art. 127.'));

add(brk());

/* ====================== XVII. EFEKTYWNOŚĆ ====================== */
add(section('XVII', 'Ocena efektywności udzielanego wsparcia', 'wypełnia się przy ocenie okresowej'));
add(howto('Ocenę prowadzi się w trzech punktach pomiaru: na starcie (poziom wyjściowy przy opracowaniu IPET albo przy ustaleniu form pomocy), po pierwszym półroczu (ocena śródroczna) oraz na koniec roku (ocena roczna). W ścieżce A zespół dokonuje oceny okresowej co najmniej dwa razy w roku (§ 6 ust. 9 rozp. poz. 1578) i na jej podstawie decyduje o modyfikacji programu; w ścieżce B nauczyciele i specjaliści oceniają efektywność udzielanej pomocy i formułują wnioski o dalszych działaniach (§ 20 ust. 7 rozp. poz. 1591). Przy ocenie wstępnej wpisz „nie dotyczy”.'));
add(table(['Lp.', 'Zakres oceny efektywności', 'Start', 'Półrocze', 'Koniec roku'],
  [
    ['1', 'Dostosowanie wymagań i organizacji zajęć — metody i formy pracy', '', '', ''],
    ['2', 'Zintegrowane działania nauczycieli i specjalistów (w tym AAC)', '', '', ''],
    ['3', 'Formy i wymiar pomocy psychologiczno-pedagogicznej', '', '', ''],
    ['4', 'Zajęcia rewalidacyjne (ścieżka A) i zajęcia specjalistyczne (ścieżka B)', '', '', ''],
    ['5', 'Działania wspierające rodziców i współpraca z poradnią pp', '', '', ''],
    ['6', 'Stopień realizacji celów edukacyjnych i terapeutycznych', '', '', '']
  ], [600, 4346, 1600, 1600, 1600], { center: [0, 2, 3, 4], rowHeight: 460 }));
add(fields([
  { label: 'Data oceny na starcie', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Data oceny śródrocznej', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Data oceny rocznej', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Osoba odpowiedzialna za ewaluację', value: '' }
], 2));
add(ta('Wnioski — czy dokument wynikowy (IPET / plan pomocy pp) wymaga modyfikacji i w jakim zakresie', { lines: 4 }));
add(legal('ŚCIEŻKA A — § 6 ust. 9 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578): zespół co najmniej dwa razy w roku szkolnym dokonuje okresowej wielospecjalistycznej oceny poziomu funkcjonowania ucznia, uwzględniając ocenę efektywności programu w zakresie § 6 ust. 1, oraz — w miarę potrzeb — dokonuje modyfikacji programu. ŚCIEŻKA B — § 20 ust. 7 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591): nauczyciele i specjaliści oceniają efektywność udzielonej pomocy i formułują wnioski dotyczące dalszych działań mających na celu poprawę funkcjonowania dziecka.'));

add(brk());

/* ====================== XVIII. PRZENIESIENIE WYNIKÓW ====================== */
add(section('XVIII', 'Przeniesienie wyników — do IPET albo do planu pomocy pp', 'wypełnij kolumnę zaznaczonej ścieżki'));
add(howto('Tabela ma dwie kolumny wynikowe. Jeżeli w sekcji I a zaznaczono ŚCIEŻKĘ A (dziecko z orzeczeniem), wypełnia się kolumnę „do IPET” — dziewięć wierszy odpowiada pełnemu zakresowi programu z § 6 ust. 1 rozp. poz. 1578. Jeżeli zaznaczono ŚCIEŻKĘ B (dziecko bez orzeczenia), wypełnia się kolumnę „do planu pomocy pp” — te same rozpoznania przekładają się wtedy na formy, okres i wymiar pomocy psychologiczno-pedagogicznej z rozp. poz. 1591. Drugą kolumnę zostawia się pustą albo wpisuje „nie dotyczy”.'));
add(table(['Element rozpoznania (źródło w tej ocenie)', 'ŚCIEŻKA A · do IPET (§ 6 ust. 1 poz. 1578)', 'ŚCIEŻKA B · do planu pomocy pp (poz. 1591)'],
  [
    ['1 · Zakres i sposób dostosowania wymagań oraz metod pracy — sekcje V, V a, XI, XII', '', ''],
    ['2 · Zintegrowane działania nauczycieli i specjalistów — sekcje VI–X, XIV', '', ''],
    ['3 · Formy, okres i wymiar udzielanej pomocy — sekcja XV', '', ''],
    ['4 · Działania wspierające rodziców, porady i konsultacje — sekcje X, XII', '', ''],
    ['5 · Zajęcia rewalidacyjne (tylko ścieżka A) / zajęcia specjalistyczne (ścieżka B) — sekcja XV', '', ''],
    ['6 · Współpraca z poradnią pp i instytucjami — sekcje I a, X', '', ''],
    ['7 · Zakres współdziałania z rodzicami — sekcje I a, X', '', ''],
    ['8 · Warunki organizacji zajęć, dostosowania i technologie wspomagające (AAC) — sekcje VIII, IX', '', ''],
    ['9 · Forma zajęć — indywidualnie, w grupie do 5 osób (ścieżka A) / liczebność grupy wg rozp. poz. 1591 — sekcje XIV, XVI', '', '']
  ], [3746, 3000, 3000], { nrCol: false, rowHeight: 500 }));

add(brk());

add(fields([
  { label: 'Dokument wynikowy tej oceny', value: '', hint: 'IPET / plan wsparcia w ramach pomocy pp' },
  { label: 'Termin opracowania dokumentu wynikowego', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Osoba odpowiedzialna za opracowanie', value: '' },
  { label: 'Data przekazania kopii rodzicom', value: '', hint: 'dd.mm.rrrr' }
], 2));
add(ta('Priorytety na najbliższe półrocze — trzy najważniejsze kierunki', { lines: 5, hint: 'Podpowiedź: 1) Uczestnictwo w zabawie z rówieśnikiem — od zabawy równoległej do zabawy w parze. 2) Komunikowanie potrzeby przerwy zamiast zachowania trudnego — konsekwentnie we wszystkich sytuacjach dnia. 3) Samodzielność w sytuacjach przejściowych — ubieranie i przygotowanie do posiłku wg planu obrazkowego. Priorytety przenosimy wprost do celów IPET i weryfikujemy przy ocenie okresowej.' }));
add(legal('ŚCIEŻKA A — indywidualny program edukacyjno-terapeutyczny opracowuje zespół po dokonaniu wielospecjalistycznej oceny poziomu funkcjonowania ucznia; zakres programu określa § 6 ust. 1 pkt 1–8, a warunki pracy zespołu § 6 ust. 3–13 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578; t.j. Dz.U. 2020 poz. 1309). ŚCIEŻKA B — o potrzebie objęcia dziecka pomocą psychologiczno-pedagogiczną informuje się dyrektora, który ustala formy, okres i wymiar godzin: § 20 ust. 1–7 oraz § 6 ust. 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591, z późn. zm.). W obu ścieżkach rodzice są informowani o ustalonych dla dziecka formach wsparcia.'));

add(brk());

/* ====================== OPINIA ZESPOŁU ====================== */
add(text('Dokument do wydania na zewnątrz', { size: 14, bold: true, color: C.orange, caps: true, align: AlignmentType.CENTER, before: 60, after: 80 }));
add(text('Opinia zespołu o funkcjonowaniu dziecka', { size: 30, bold: true, color: C.purple, align: AlignmentType.CENTER, after: 60, line: 300 }));
add(text('na podstawie wielospecjalistycznej oceny poziomu funkcjonowania · przedszkole', { size: 15, italic: true, color: C.muted, align: AlignmentType.CENTER, after: 160 }));
add(fields([
  { label: 'Imię i nazwisko dziecka', value: '' },
  { label: 'Grupa', value: '' },
  { label: 'Data sporządzenia opinii', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Adresat opinii', value: '', hint: 'poradnia psychologiczno-pedagogiczna / rodzice' }
], 2));
add(ta('1 · Podstawa opinii i przebieg obserwacji — podstawa (orzeczenie / wniosek rodziców), okres i warunki obserwacji, skład zespołu', { lines: 4, hint: 'Podpowiedź: Opinię sporządzono na wniosek rodziców, w związku z ubieganiem się o wydanie orzeczenia / opinii przez poradnię psychologiczno-pedagogiczną. Obserwację prowadzono przez cały pierwszy semestr roku przedszkolnego, w naturalnych sytuacjach dnia: zajęcia kierowane, zabawa swobodna, posiłek, ubieranie, ogród przedszkolny i sytuacje przejściowe. Ocenę opracował zespół w składzie: nauczyciel wychowania przedszkolnego (koordynator), psycholog, pedagog specjalny, logopeda i terapeuta SI, we współpracy z rodzicami dziecka.' }));
add(ta('2 · Wyniki oceny funkcjonalnej KPOF — mocne obszary i obszary trudności', { lines: 4, hint: 'Podpowiedź: Ocena funkcjonalna KPOF (skala 1–5, kryteria: 4,0–5,0 zasób · 3,0–3,9 poziom I · 2,0–2,9 poziom II · poniżej 2,0 poziom III) dała średnią ogólną …, co odpowiada … poziomowi wsparcia. Najwyższy wynik dziecko uzyskało w obszarze …, najniższy w obszarze … Pozostałe obszary mieszczą się w przedziale …' }));

add(brk());

add(ta('3 · Obserwacja pogłębiona — zastosowane narzędzia i najważniejsze wyniki', { lines: 4, hint: 'Podpowiedź: Obserwację pogłębiono narzędziami: karta analizy zachowania ABC · FBA — dominująca funkcja zachowania …; karta oceny teorii umysłu — …; kwestionariusz rozwoju mowy — …; profil sensoryczny — …; profil biopsychospołeczny — czynniki środowiskowe (hałas, nagłe zmiany, pośpiech) istotnie ograniczają uczestnictwo dziecka w życiu grupy.' }));
add(ta('4 · Charakterystyka funkcjonowania — zasoby, trudności, wpływ otoczenia', { lines: 5, hint: 'Podpowiedź: Dziecko jest pogodne, chętnie przychodzi do przedszkola i nawiązuje kontakt z wybranym dorosłym. Trudność sprawiają mu: dłuższa koncentracja przy zadaniu, wchodzenie w zabawę z rówieśnikiem, regulacja napięcia przy zmianie aktywności oraz formułowanie dłuższych wypowiedzi. Funkcjonowanie wyraźnie poprawia się w warunkach przewidywalnych — przy planie obrazkowym, w małej grupie i przy ograniczonym hałasie; pogarsza w pośpiechu, w hałasie i przy nagłej zmianie planu.' }));
add(ta('5 · Wnioski i rekomendacje — poziom wsparcia i formy pomocy', { lines: 5, hint: 'Podpowiedź: Zespół wnioskuje o … poziom wsparcia. Wskazane są zajęcia rewalidacyjne rozwijające kompetencje społeczne i komunikacyjne oraz zajęcia z zakresu pomocy psychologiczno-pedagogicznej: terapia logopedyczna, zajęcia rozwijające kompetencje emocjonalno-społeczne i zajęcia korekcyjno-kompensacyjne. Warunki niezbędne: przewidywalny rytm dnia, plan obrazkowy, stałe miejsce z dala od hałasu, dostęp do kącika wyciszenia, przerwy regulacyjne.' }));

add(brk());

add(ta('6 · Formuła końcowa i współpraca z rodzicami', { lines: 4, hint: 'Podpowiedź: Zespół zwraca się z prośbą o wskazanie dalszych kierunków pracy z dzieckiem oraz o weryfikację zalecanych form pomocy. Rodzice uczestniczyli w spotkaniu zespołu, zapoznali się z treścią oceny i otrzymali jej kopię; deklarują stosowanie w domu tych samych sygnałów i strategii. Kolejna ocena okresowa zostanie dokonana na zakończenie roku przedszkolnego.' }));
add(signatures(['Koordynator zespołu', 'Dyrektor przedszkola'], 2));
add(legal('Opinię przedszkola dołącza się do wniosku o wydanie orzeczenia lub opinii — § 6 ust. 4 rozp. MEN z 7.09.2017 r. w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające działające w publicznych poradniach psychologiczno-pedagogicznych (Dz.U. 2017 poz. 1743, z późn. zm.): opinia zawiera informacje o rozpoznanych indywidualnych potrzebach rozwojowych i edukacyjnych, możliwościach psychofizycznych dziecka oraz o udzielanej pomocy i jej efektach. Wydanie opinii następuje na wniosek rodziców albo za ich zgodą; kopię opinii przekazuje się rodzicom (art. 47 ust. 1 pkt 5 ustawy — Prawo oświatowe, t.j. Dz.U. 2024 poz. 737, z późn. zm.).'));

add(brk());

/* ====================== XIX. PODPISY ====================== */
add(section('XIX', 'Podpisy zespołu ds. WOPF', 'ocenę podpisują wszyscy członkowie zespołu'));
add(signatures([
  'Koordynator zespołu', 'Nauczyciel wychowania przedszkolnego',
  'Psycholog', 'Pedagog specjalny',
  'Logopeda', 'Terapeuta SI'
], 2));
add(signatures(['Rodzic / opiekun prawny — przyjęcie do wiadomości'], 1));
add(legal('Ocenę podpisują wszyscy członkowie zespołu. Podpis rodzica lub opiekuna prawnego potwierdza zapoznanie się z oceną i otrzymanie jej kopii; brak podpisu nie wstrzymuje dokonania oceny — odmowę należy odnotować. Prawa rodziców (ścieżka A): § 6 ust. 11–13 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578; t.j. Dz.U. 2020 poz. 1309). Ścieżka B: § 20 ust. 6 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591) — dyrektor informuje rodziców o ustalonych formach, okresie i wymiarze godzin udzielanej pomocy.'));

add(brk());

/* ====================== XX. ZAŁĄCZNIKI ====================== */
add(section('XX', 'Wykaz załączników', 'materiał dowodowy oceny'));
add(checks([
  'Arkusz KPOF (obszary I–IX)', 'Karta analizy zachowania ABC · FBA',
  'Karta oceny teorii umysłu (ToM)', 'Profil sensoryczny (model Dunn)',
  'Kwestionariusz rozwoju mowy (PCTP)', 'Profil biopsychospołeczny',
  'Opinie specjalistów', 'Wytwory pracy dziecka',
  'Karty obserwacji i dziennik obserwacji', 'Zgoda rodziców na udział specjalistów / współpracę z poradnią pp',
  'Kopia orzeczenia lub opinii poradni pp (jeżeli dziecko je posiada)', 'Inne — jakie?'
], 2));
add(legal('Załączniki stanowią materiał dowodowy oceny i są przechowywane razem z nią. Dokumentację badań i czynności uzupełniających prowadzonych przez nauczycieli, wychowawców i specjalistów, w tym dokumentację indywidualnych programów edukacyjno-terapeutycznych, prowadzi przedszkole zgodnie z § 19–20 rozp. MEN z 25.08.2017 r. w sprawie sposobu prowadzenia przez publiczne przedszkola, szkoły i placówki dokumentacji przebiegu nauczania, działalności wychowawczej i opiekuńczej (Dz.U. 2017 poz. 1646, z późn. zm.).'));

/* ====================== XXI. RODO ====================== */
add(section('XXI', 'Klauzula informacyjna RODO i ważność dokumentu', 'art. 13 RODO'));
[
  ['1. Administrator danych.', 'Administratorem danych osobowych jest przedszkole, do którego uczęszcza dziecko, reprezentowane przez dyrektora.'],
  ['2. Inspektor ochrony danych (IOD).', 'Kontakt z IOD: [adres e-mail / dane kontaktowe].'],
  ['3. Cel i podstawa prawna.', 'Dane przetwarzane są w celu dokonania wielospecjalistycznej oceny poziomu funkcjonowania oraz organizacji kształcenia specjalnego i pomocy psychologiczno-pedagogicznej — art. 6 ust. 1 lit. c oraz art. 9 ust. 2 lit. g RODO w związku z ustawą — Prawo oświatowe oraz rozporządzeniami Dz.U. 2017 poz. 1578 i Dz.U. 2017 poz. 1591 (obowiązek prawny administratora).'],
  ['4. Kategorie danych.', 'Dokument zawiera dane szczególnej kategorii (dane o zdrowiu, z orzeczenia i diagnozy), o których mowa w art. 9 RODO.'],
  ['5. Odbiorcy.', 'Dane udostępniane są wyłącznie podmiotom uprawnionym (m.in. poradnia psychologiczno-pedagogiczna, organ prowadzący, organ nadzoru pedagogicznego).'],
  ['6. Okres przechowywania.', 'Przez okres uczęszczania dziecka do przedszkola oraz czas wymagany przepisami o archiwizacji dokumentacji przebiegu nauczania.'],
  ['7. Prawa osób.', 'Prawo dostępu, sprostowania, usunięcia lub ograniczenia przetwarzania oraz wniesienia skargi do Prezesa UODO.']
].forEach(([t, b]) => add(L.P([L.run(t + ' ', { size: 15, bold: true, color: C.purple }), L.run(b, { size: 15, color: '3D384C' })], { after: 70, line: 240 })));
add(note('Bezpieczeństwo i ważność dokumentu.', 'Dokument zawiera dane wrażliwe i jest przechowywany w sposób uniemożliwiający dostęp osobom nieupoważnionym. Podpisy członków zespołu potwierdzają dokonanie oceny; podpis rodzica lub opiekuna prawnego potwierdza zapoznanie się z oceną i otrzymanie jej kopii. Brak podpisu rodzica nie wstrzymuje dokonania oceny — rodzice mają prawo, a nie obowiązek, uczestniczyć w pracach zespołu; ewentualną odmowę podpisu należy odnotować.'));
add(text('EduPlaner 2026 · PCTP · Wielospecjalistyczna Ocena Poziomu Funkcjonowania — arkusz przedszkolny · wersja Word',
  { size: 13, italic: true, color: C.muted, align: AlignmentType.CENTER, before: 200, after: 0 }));

module.exports = B;
