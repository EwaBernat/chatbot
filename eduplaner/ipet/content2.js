const L = require('../lib.js');
const { section, howto, legal, note, ta, fields, checks, brk, text, subhead, C } = L;

const B = [];
const add = (...xs) => xs.forEach(x => Array.isArray(x) ? B.push(...x) : B.push(x));

/* Jedna sfera = dwie strony: ocena i cel SMART · sposób pracy */
function sfera(s) {
  add(section(s.num, s.title, 'cel SMART · jedna sfera na jednej stronie'));
  add(note('Źródło wyniku i narzędzia.', s.source));
  add(fields([
    { label: 'Wynik w obszarze KSzOF (pkt / sten)', value: '', hint: 'np. 13 / 20 · sten 7' },
    { label: 'Ustalony poziom wsparcia dla tej sfery', value: '', hint: 'I / II / III' }
  ], 2));
  add(subhead('Trudności i bariery — zaznacz występujące'));
  add(checks(s.difficulties, 2));
  add(subhead('Poziom wsparcia w tej sferze — zaznacz jeden'));
  add(checks([
    'POZIOM I · sten 8–10 — bieżąca praca nauczyciela',
    'POZIOM II · sten 5–7 — pomoc psychologiczno-pedagogiczna',
    'POZIOM III · sten 1–4 — wsparcie specjalistyczne'
  ], 1));
  add(ta('Charakterystyka funkcjonowania w tej sferze — na czym konkretnie polega trudność', { lines: 5, hint: s.hintChar }));
  add(brk());
  add(ta('Cel SMART dla tej sfery — specyficzny · mierzalny · osiągalny · istotny · określony w czasie', { lines: 4, hint: s.hintGoal }));
  add(ta('Kryterium osiągnięcia celu i sposób pomiaru', { lines: 3, hint: s.hintMeasure }));
  add(ta('Zintegrowane działania nauczycieli i specjalistów', { lines: 3, hint: s.hintTeam }));
  add(ta('System motywacji — zastosowanie w tej sferze', { lines: 2, hint: s.hintMotiv }));
  add(subhead('Metody pracy — zaznacz'));
  add(checks(s.methods, 2));
  add(subhead('Formy pracy — zaznacz'));
  add(checks(s.forms, 2));
  add(ta('Proponowane pomoce dydaktyczne', { lines: 3, hint: s.hintAids }));
  add(brk());
}

sfera({
  num: 'X', title: 'Sfera 1 — poznawcze — uczenie się i edukacja',
  source: 'Obszar KSzOF będący źródłem wyniku: I · Uczenie się i stosowanie wiedzy + VIII · Edukacja szkolna. Narzędzia oceny i obserwacji: KSzOF (obszary I, VIII) · obserwacja uwagi, pamięci i myślenia · analiza wytworów pracy · arkusz programu poznawczego. Kody ICF: d110–d179 · d820 · b140 (uwaga) · b144 (pamięć) · b164 (funkcje wykonawcze) · b1720 (myślenie).',
  difficulties: [
    'Spostrzeganie · b156', 'Uwaga i koncentracja · b140',
    'Pamięć · b144', 'Myślenie i wnioskowanie · b1720',
    'Umiejętności wykonawcze · b164', 'Tempo uczenia się · d160'
  ],
  methods: ['Praca na konkretach i wielozmysłowa', 'Ćwiczenia uwagi i pamięci', 'Stopniowanie trudności i powtórki', 'Mapy myśli i notatki graficzne'],
  forms: ['Indywidualna (1:1)', 'Mała grupa', 'Z całą klasą', 'Współpraca szkoła–dom'],
  hintChar: 'Podpowiedź: na jakim materiale uczeń pracuje najlepiej, jak długo utrzymuje uwagę, ile kroków polecenia utrzymuje w pamięci, jakie jest tempo pracy wobec tempa klasy i co zmienia wsparcie wizualne oraz pytanie sprawdzające zrozumienie polecenia.',
  hintGoal: 'Podpowiedź: Do końca I półrocza uczeń wykona samodzielnie zadanie złożone z trzech kroków na podstawie planu obrazkowego, w 4 na 5 kolejnych prób, na zajęciach edukacji wczesnoszkolnej i rewalidacyjnych.',
  hintMeasure: 'Podpowiedź: karta obserwacji z liczbą prób udanych i nieudanych, prowadzona raz w tygodniu przez nauczyciela prowadzącego; cel uznajemy za osiągnięty przy 4 z 5 prób w trzech kolejnych tygodniach.',
  hintTeam: 'Podpowiedź: wszyscy nauczyciele stosują krótkie, jednoznaczne polecenia, dzielą materiał na mniejsze partie, dają dodatkowy czas i wsparcie wizualne oraz utrwalają kluczowe treści na każdych zajęciach.',
  hintMotiv: 'Podpowiedź: system żetonowy · wykorzystanie zainteresowań ucznia jako nagrody · pochwała opisowa za wysiłek, nie za wynik.',
  hintAids: 'Propozycja: plan obrazkowy zadania, karty z pojedynczym poleceniem, kolorowe zakładki i podkreślenia, liniatura poszerzona, minutnik wizualny, materiał manipulacyjny, mapy myśli. Zestaw uzgadnia zespół — wpisz tylko to, co szkoła rzeczywiście zapewnia.'
});

sfera({
  num: 'XI', title: 'Sfera 2 — emocjonalno-społeczne — kontakty i społeczność',
  source: 'Obszar KSzOF będący źródłem wyniku: VII · Wzajemne kontakty i związki + IX · Życie w społeczności lokalnej. Narzędzia oceny i obserwacji: KSzOF (obszary VII, IX) · karta oceny ToM · karta ABC · FBA. Kody ICF: d710–d770 · b152 · b1251 · d250 · b1801 · d910–d950.',
  difficulties: [
    'Rozpoznawanie i nazywanie emocji · b152', 'Regulacja emocji i samokontrola · d250',
    'Naprzemienność i czekanie na kolej · d710', 'Współdziałanie z rówieśnikami · d720',
    'Relacje i kontakty · d750', 'Empatia i teoria umysłu · b1801'
  ],
  methods: ['Trening umiejętności społecznych (TUS / TUE / TUK)', 'Modelowanie i odgrywanie ról (drama)', 'Historyjki społeczne', '„Termometr emocji” i techniki regulacji'],
  forms: ['W grupie', 'W parach', 'Indywidualna (1:1)', 'Strefa wyciszenia'],
  hintChar: 'Podpowiedź: jak uczeń nawiązuje kontakt i jak długo go utrzymuje, w jakich sytuacjach narasta napięcie (zmiana planu, przegrana w grze, głośna praca grupowa), jak wtedy reaguje i czy rozpoznaje wczesne sygnały napięcia we własnym ciele. Odnieś się do funkcji zachowania ustalonej w sekcji VI.',
  hintGoal: 'Podpowiedź: Do końca roku szkolnego uczeń w sytuacji narastającego napięcia użyje karty „przerwa” zamiast wyjścia z ławki, w co najmniej 3 na 4 sytuacje trudne w tygodniu, na wszystkich zajęciach.',
  hintMeasure: 'Podpowiedź: tygodniowa karta rejestracji zachowania (liczba użyć karty „przerwa” wobec liczby sytuacji trudnych) prowadzona przez wychowawcę; cel osiągnięty przy 3 z 4 przez cztery kolejne tygodnie.',
  hintTeam: 'Podpowiedź: jednolity system motywacyjny i spójne reagowanie na zachowania trudne (model ABC / FBA) oraz trening umiejętności społecznych.',
  hintMotiv: 'Podpowiedź: wzmocnienia pozytywne · system „First-Then” · funkcja pomocnika nauczyciela jako nagroda społeczna.',
  hintAids: 'Propozycja: karta „przerwa”, termometr emocji, plan dnia z zaznaczoną zmianą, historyjki społeczne, kącik wyciszenia, plansza zasad klasowych, karty emocji. Zestaw uzgadnia zespół.'
});

sfera({
  num: 'XII', title: 'Sfera 3 — motoryczne — motoryka i poruszanie się',
  source: 'Obszar KSzOF będący źródłem wyniku: IV · Motoryka i poruszanie się. Narzędzia oceny i obserwacji: KSzOF (obszar IV) · profil sensoryczny (model Dunn) · ocena motoryki i terapii ręki · próby kliniczne SI. Kody ICF: d440–d455 · b760 (kontrola ruchów dowolnych) · b147 (praksja) · b156 (percepcja) · b235 (przedsionek) · d170 (pisanie).',
  difficulties: [
    'Napięcie mięśniowe i posturalne · b735', 'Koordynacja ruchowa · b760',
    'Koordynacja obustronna i oko–ręka · b7602', 'Praksja — planowanie ruchu · b176',
    'Motoryka mała i chwyt · d440', 'Grafomotoryka i pisanie · d170'
  ],
  methods: ['Ćwiczenia grafomotoryczne i manualne', 'Terapia ręki', 'Zabawy ruchowe i przerwy sensoryczne', 'Integracja sensoryczna (SI)'],
  forms: ['Indywidualna (1:1)', 'Mała grupa', 'Przerwy sensoryczno-ruchowe', 'Z asystą'],
  hintChar: 'Podpowiedź: sprawność motoryki dużej wobec małej, sposób trzymania narzędzia pisarskiego, męczliwość przy pisaniu, mieszczenie się w liniaturze, tempo pisania wobec klasy oraz czucie głębokie (nadmierny docisk, przedzieranie kartki).',
  hintGoal: 'Podpowiedź: Do końca I półrocza uczeń przepisze samodzielnie tekst o długości pięciu zdań, mieszcząc litery w liniaturze poszerzonej, w czasie do 10 minut, w 4 na 5 kolejnych prób.',
  hintMeasure: 'Podpowiedź: porównanie prac ucznia z początku i końca okresu (teczka prac) oraz pomiar czasu; ocena przez nauczyciela i terapeutę ręki co miesiąc.',
  hintTeam: 'Podpowiedź: nauczyciele zapewniają dostosowania warsztatu pracy (nakładki na przybory, powiększona liniatura, możliwość pisania na komputerze), przerwy ruchowe oraz bezpieczne modyfikacje ćwiczeń na wychowaniu fizycznym.',
  hintMotiv: 'Podpowiedź: docenianie wysiłku i postępu, nie efektu · przerwy ruchowe jako wzmocnienie · widoczna karta postępów.',
  hintAids: 'Propozycja: nasadki na ołówek, ołówki trójkątne, liniatura poszerzona i podkładka antypoślizgowa, ćwiczenia rozmachowe, masy sensoryczne, zestaw do terapii ręki, sortery. Zestaw uzgadnia zespół.'
});

sfera({
  num: 'XIII', title: 'Sfera 4 — komunikowanie się',
  source: 'Obszar KSzOF będący źródłem wyniku: III · Porozumiewanie się. Narzędzia oceny i obserwacji: KSzOF (obszar III) · diagnoza logopedyczna · ocena słuchu fonematycznego · obserwacja komunikacji i wskazań do AAC. Kody ICF: d310–d360 · b320 (artykulacja) · b1560 (słuch fonematyczny) · b16700 / b16710 (język) · d3350 (narracja).',
  difficulties: [
    'Rozumienie mowy · d310', 'Przetwarzanie słuchowe i fonematyczne · b1560',
    'Artykulacja i wymowa · b320', 'Płynność i prozodia mowy · b330',
    'Słownictwo i gramatyka · b16710', 'Budowanie wypowiedzi i narracja · d330 / d3350'
  ],
  methods: ['Ćwiczenia logopedyczne', 'Modelowanie wypowiedzi', 'Komunikacja wspomagająca (AAC / PECS)', 'Ćwiczenia słuchu fonematycznego'],
  forms: ['Terapia 1:1', 'Mała grupa', 'Wsparcie na lekcjach', 'Współpraca z logopedą'],
  hintChar: 'Podpowiedź: relacja rozumienia do wypowiadania się, długość i budowa wypowiedzi, umiejętność opowiedzenia zdarzenia w kolejności, zadawania pytania przy niezrozumieniu, zrozumiałość wymowy oraz wpływ napięcia przy wypowiedzi na forum klasy.',
  hintGoal: 'Podpowiedź: Do końca roku szkolnego uczeń opowie zdarzenie z użyciem trzech następujących po sobie obrazków, budując co najmniej trzy zdania proste, w 4 na 5 kolejnych prób na zajęciach logopedycznych i języka polskiego.',
  hintMeasure: 'Podpowiedź: nagranie lub zapis wypowiedzi ucznia raz w miesiącu; liczba zdań i poprawność kolejności zdarzeń oceniane przez logopedę wspólnie z nauczycielem.',
  hintTeam: 'Podpowiedź: nauczyciele ujednolicają sposób wydawania poleceń, stosują wsparcie wizualne i AAC, wydłużają czas na wypowiedź i nie kończą zdania za ucznia; logopeda prowadzi terapię i przekazuje zespołowi zalecenia.',
  hintMotiv: 'Podpowiedź: pochwała za każdą próbę komunikacji · tablica wyboru · obrazkowe wzmocnienia dostępne od ręki.',
  hintAids: 'Propozycja: historyjki obrazkowe, symbole AAC i tablica komunikacyjna, karty pytań „kto · co robi · gdzie”, dyktafon, gry słownikowe, lustro logopedyczne, piktogramy. Zestaw uzgadnia zespół.'
});

sfera({
  num: 'XIV', title: 'Sfera 5 — samodzielność — dbanie o siebie',
  source: 'Obszar KSzOF będący źródłem wyniku: V · Dbanie o siebie i samoobsługa. Narzędzia oceny i obserwacji: KSzOF (obszar V) · obserwacja funkcjonalna samoobsługi · profil sensoryczny · wywiad z rodzicem. Kody ICF: d510–d570 · b164 (planowanie) · b1252 (impulsywność) · d230 (rutyna) · b134 (sen i energia).',
  difficulties: [
    'Higiena i dbanie o siebie · d510', 'Ubieranie się · d540',
    'Jedzenie · d550', 'Samodzielność i zaradność · d570',
    'Organizacja własnych rzeczy · d230', 'Bezpieczeństwo · d571'
  ],
  methods: ['Trening samodzielności metodą małych kroków', 'Plany wizualne czynności', 'Modelowanie i instruktaż', 'Nauka w sytuacjach naturalnych'],
  forms: ['Indywidualna (1:1)', 'W sytuacjach naturalnych', 'Z asystą', 'Współpraca szkoła–dom'],
  hintChar: 'Podpowiedź: które czynności samoobsługowe uczeń wykonuje samodzielnie, przy których potrzebuje przypomnienia o kolejności, jak radzi sobie z organizacją miejsca pracy i przyborów oraz co zmienia lista kontrolna.',
  hintGoal: 'Podpowiedź: Do końca I półrocza uczeń przygotuje miejsce pracy na lekcję na podstawie listy kontrolnej, samodzielnie, w ciągu 2 minut od dzwonka, w 4 na 5 dni w tygodniu.',
  hintMeasure: 'Podpowiedź: codzienny zapis w karcie samodzielności (tak/nie) prowadzony przez wychowawcę przez cztery kolejne tygodnie; cel osiągnięty przy 4 z 5 dni.',
  hintTeam: 'Podpowiedź: zespół stosuje stałą, przewidywalną rutynę i plan wizualny czynności, stopniowo wycofuje pomoc dorosłego (wygaszanie podpowiedzi) i wzmacnia każdy przejaw samodzielności.',
  hintMotiv: 'Podpowiedź: tablica osiągnięć · nagroda za samodzielne wykonanie · autonomia w wyborze kolejności czynności.',
  hintAids: 'Propozycja: lista kontrolna przyborów naklejona na ławce, oznaczone kolorami okładki i przegródki, plan lekcji z symbolami, pudełko na przybory, minutnik, piktogramy krok po kroku. Zestaw uzgadnia zespół.'
});

sfera({
  num: 'XV', title: 'Sfera 6 — ogólne zadania i życie domowe',
  source: 'Obszar KSzOF będący źródłem wyniku: II · Ogólne zadania i obowiązki + VI · Życie domowe. Narzędzia oceny i obserwacji: KSzOF (obszary II, VI) · obserwacja funkcji wykonawczych · analiza ABC (organizacja, samokontrola) · wywiad z rodzicem. Kody ICF: d210–d250 · d610–d660 · b1641 (organizacja) · b1643 (elastyczność) · d240 (radzenie sobie ze stresem) · d160 (uwaga w zadaniu).',
  difficulties: [
    'Rozpoczynanie zadania · d210', 'Zadania złożone · d220',
    'Organizacja i rutyna · d230', 'Radzenie sobie ze stresem · d240',
    'Planowanie i funkcje wykonawcze · b164', 'Życie domowe · d610–d660'
  ],
  methods: ['Planowanie krok po kroku (checklisty)', 'Trening funkcji wykonawczych', 'Instruktaż i przypomnienia', 'Organizacja warsztatu pracy'],
  forms: ['Indywidualna (1:1)', 'Mała grupa', 'Z całą klasą', 'Współpraca szkoła–dom'],
  hintChar: 'Podpowiedź: w jakich warunkach uczeń podejmuje zadanie, jak radzi sobie z zadaniami wieloetapowymi i pracą domową, czy potrafi rozłożyć zadanie w czasie i ocenić, że je skończył, oraz jakiego wsparcia potrzebuje w domu (współpraca z rodzicami — sekcja XXI).',
  hintGoal: 'Podpowiedź: Do końca roku szkolnego uczeń wykona zadanie domowe rozłożone na trzy etapy zgodnie z kartą pracy domowej, odnotowując wykonanie każdego etapu, w 3 na 4 tygodnie w miesiącu.',
  hintMeasure: 'Podpowiedź: karta pracy domowej z podpisem rodzica i wpisem nauczyciela, sprawdzana raz w tygodniu; cel osiągnięty przy 3 z 4 tygodni przez dwa kolejne miesiące.',
  hintTeam: 'Podpowiedź: nauczyciele dostarczają checklisty i plan dnia, przypominają o kolejnych krokach, wspierają w organizacji warsztatu pracy i w radzeniu sobie ze zmianą planu; dom stosuje ten sam schemat.',
  hintMotiv: 'Podpowiedź: checklisty z nagrodą za ukończenie · kontrakt behawioralny · zaplanowane przerwy jako element umowy.',
  hintAids: 'Propozycja: karta pracy domowej z etapami, planer tygodniowy, minutnik lub klepsydra, checklista „czy skończyłem”, przegródki na zadania wykonane i do zrobienia, karty „co teraz / co potem”. Zestaw uzgadnia zespół.'
});

module.exports = B;
