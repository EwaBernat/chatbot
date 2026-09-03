const L = require('../lib.js');
const { section, partBanner, howto, lead, legal, note, ta, fields, checks, table, scale, bars,
        signatures, brk, text, subhead, C, AlignmentType } = L;

const B = [];
const add = (...xs) => xs.forEach(x => Array.isArray(x) ? B.push(...x) : B.push(x));

/* ====================== STRONA TYTUŁOWA ====================== */
add(text('Program obowiązkowy · dokument do wypełnienia przez zespół', { size: 15, bold: true, color: C.orange, caps: true, align: AlignmentType.CENTER, before: 200, after: 160 }));
add(text('Indywidualny Program Edukacyjno-Terapeutyczny (IPET)', { size: 38, bold: true, color: C.purple, align: AlignmentType.CENTER, after: 80, line: 300 }));
add(text('· · ·   z wielospecjalistyczną oceną poziomu funkcjonowania (WOPFU · ICF) · szkoła · 2026   · · ·', { size: 15, bold: true, color: C.orange, caps: true, align: AlignmentType.CENTER, after: 200 }));
add(fields([
  { label: 'Dotyczy ucznia', value: '' },
  { label: 'Klasa / oddział', value: '' },
  { label: 'Data opracowania', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Rok szkolny', value: '', hint: '20…/20…' }
], 2));
add(lead('IPET 2026 + WOPFU (ICF) — jeden dokument, trzy części',
  'Indywidualny program edukacyjno-terapeutyczny opracowuje się dla ucznia posiadającego orzeczenie o potrzebie kształcenia specjalnego. Program określa zakres i sposób dostosowania wymagań edukacyjnych, zintegrowane działania nauczycieli i specjalistów, formy i wymiar pomocy oraz zakres współpracy z rodzicami. Część I to wielospecjalistyczna ocena poziomu funkcjonowania ucznia (WOPFU) — ustala, gdzie uczeń jest dzisiaj. Część II to program — ustala, co zespół z tym zrobi. Część III to zatwierdzenie programu i ocena jego efektywności.'));
add(howto('Wypełniaj po kolei — dokument jest tak ułożony, że każda informacja pojawia się dokładnie raz. Mocne strony i system motywacji wpisujesz w sekcjach III i IV i już do nich nie wracasz: sfery celów SMART tylko z nich korzystają. Ogólne przyczyny niepowodzeń zaznaczasz w sekcji V, a szczegółowe trudności z kodami ICF — dopiero przy właściwej sferze. Wynik KSzOF przenosisz z arkusza oceny do tabeli w sekcji VII i to on wyznacza poziom wsparcia w każdej sferze. Opis trzech poziomów wsparcia jest wydrukowany raz, w sekcji VIII — przy sferze wpisujesz już tylko literę I, II albo III.'));

add(brk());

/* ====================== I. DANE ====================== */
add(section('I', 'Dane osoby uczącej się', 'zakres minimalny — bez danych zbędnych'));
add(fields([
  { label: 'Imię i nazwisko', value: '' },
  { label: 'Data urodzenia', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Klasa / oddział', value: '' },
  { label: 'Rok szkolny', value: '', hint: '2026 / 2027' },
  { label: 'Szkoła / placówka', value: '' },
  { label: 'Etap edukacyjny', value: '', hint: 'I / II / III' },
  { label: 'Podstawa wydania orzeczenia', value: '', hint: 'np. autyzm, niepełnosprawność intelektualna, sprzężona' },
  { label: 'Numer i data orzeczenia · poradnia', value: '' },
  { label: 'Okres obowiązywania programu', value: '', hint: 'od — do' },
  { label: 'Rodzaj programu', value: '', hint: 'nowy / kontynuacja / modyfikacja' },
  { label: 'Koordynator zespołu', value: '', hint: 'funkcja, nie nazwisko — nazwiska w sekcji XXIII' },
  { label: 'Data opracowania programu', value: '', hint: 'dd.mm.rrrr' }
], 2));
add(legal('Zasada minimalizacji danych — art. 5 ust. 1 lit. c RODO (UE 2016/679): przetwarza się wyłącznie dane niezbędne do celu. Dlatego metryczka nie zawiera numeru PESEL, adresu zamieszkania, miejsca urodzenia, obywatelstwa, numerów dokumentów ani danych o miejscu pracy rodziców — te dane pozostają wyłącznie w dokumentacji przebiegu nauczania (rozp. MEN z 25.08.2017 r., Dz.U. 2017 poz. 1646, z późn. zm.). Program opracowuje się na okres, na jaki wydano orzeczenie o potrzebie kształcenia specjalnego, nie dłuższy niż etap edukacyjny — § 6 ust. 4 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.).'));

add(brk());

/* ====================== II. WYWIAD Z UCZNIEM ====================== */
add(section('II', 'Wywiad z uczniem — autorefleksja ucznia', 'nowy model 26/27 · rozmowa prowadzona z uczniem'));
add(howto('Sekcja to zapis wywiadu przeprowadzonego z uczniem — rozmowy prowadzonej w sposób dostosowany do jego możliwości komunikacyjnych: pytaniem otwartym, obrazkiem, kartą wyboru albo systemem AAC. Zapisujemy to, co uczeń powiedział lub wskazał, a nie to, co dorosły uważa za słuszne. Jeżeli uczeń nie komunikuje preferencji, odnotowujemy sposób próby kontaktu i obserwację reakcji.'));
add(ta('Moje mocne strony i supermoce', { lines: 3, hint: 'Zapisz słowami ucznia: co mi najlepiej wychodzi, co lubię robić, w czym jestem dobry.' }));
add(ta('Z czym mam największą trudność w szkole', { lines: 3, hint: 'Zapisz słowami ucznia: co jest dla mnie najtrudniejsze, kiedy i na jakich lekcjach.' }));
add(subhead('Co mi najbardziej pomaga na lekcjach — zaznacz razem z uczniem'));
add(checks(['cisza', 'czas', 'ruch', 'piktogramy', 'praca na komputerze', 'przerwy', 'wsparcie nauczyciela', 'praca w parze'], 2));
add(ta('Inne — co jeszcze mi pomaga (słowami ucznia)', { lines: 3 }));
add(ta('Sposób przeprowadzenia wywiadu (rozmowa / karty wyboru / AAC / obserwacja) i data', { lines: 3 }));
add(note('Udział ucznia.', 'Udział ucznia w planowaniu własnego wsparcia nie wynika wprost z rozporządzenia — jest elementem modelu oceny funkcjonalnej opartej na ICF i wykracza ponad minimum prawne. Zespół uwzględnia perspektywę ucznia przy formułowaniu celów SMART.'));

add(brk());

/* ====================== CZĘŚĆ I ====================== */
add(partBanner('Część I · ocena', 'WOPFU — wielospecjalistyczna ocena poziomu funkcjonowania',
  'mocne strony · motywacja · bariery · obserwacja funkcjonalna · wynik KSzOF'));
add(howto('Ocena obejmuje mocne strony, system motywacji, przyczyny niepowodzeń oraz obserwację funkcjonalną, uporządkowane zgodnie z Międzynarodową Klasyfikacją Funkcjonowania (ICF). Ocenę przeprowadza się przed opracowaniem programu, a następnie co najmniej dwa razy w roku szkolnym.'));

add(section('III', 'Mocne strony, predyspozycje, zainteresowania i uzdolnienia', 'punkt wyjścia całego programu'));
add(checks([
  'Dobra pamięć wzrokowa i spostrzegawczość', 'Zdolności manualne i plastyczne',
  'Zainteresowania przyrodnicze i techniczne', 'Wysoka sprawność fizyczna i sportowa',
  'Umiejętność logicznego myślenia', 'Empatia i chęć niesienia pomocy innym',
  'Zainteresowanie technologiami cyfrowymi', 'Dobra orientacja w przestrzeni',
  'Zdolności muzyczne i poczucie rytmu', 'Łatwość nawiązywania kontaktów'
], 2));
add(ta('Inne mocne strony — opis własny zespołu', { lines: 4, hint: 'Podpowiedź: opisz mocne strony w kategoriach obserwowalnych — co uczeń robi dobrze, w jakich sytuacjach i co z tego wykorzystujemy jako punkt wyjścia do pracy nad trudnościami.' }));

add(brk());

add(section('IV', 'System motywacji oparty na mocnych stronach', 'ustalany raz — obowiązuje we wszystkich sferach'));
add(checks([
  'System żetonowy (punkty / naklejki)', 'Kontrakt behawioralny (zasady i nagrody)',
  'Wzmocnienia pozytywne (pochwała opisowa)', 'Tablica wyboru nagród (autonomia)',
  'System „First-Then” (najpierw zadanie, potem nagroda)', 'Wykorzystanie zainteresowań jako nagroda',
  'Przerwy na relaksację jako wzmocnienie', 'Funkcja pomocnika nauczyciela'
], 2));
add(ta('Zasady stosowania systemu motywacji — kto, kiedy, jak często wzmacnia', { lines: 5, hint: 'Podpowiedź: system obowiązuje wszystkich nauczycieli uczących w klasie i specjalistów. Zapisz, za co uczeń otrzymuje wzmocnienie, po ilu wzmocnieniach następuje nagroda, kto prowadzi kartę i jak często zespół przegląda system. Raz przyznanych żetonów nie odbieramy.' }));
add(note('Zasada jednego systemu.', 'System motywacji ustalony w tej sekcji obowiązuje wszystkich nauczycieli i specjalistów pracujących z uczniem oraz — w uzgodnionym zakresie — dom. Przy poszczególnych sferach opisuje się wyłącznie sposób jego zastosowania, a nie buduje osobnego systemu.'));

add(brk());

/* ====================== V. PRZYCZYNY ====================== */
add(section('V', 'Przyczyny niepowodzeń edukacyjnych — trudności i bariery', 'poziom ogólny · szczegóły z kodami ICF przy sferach'));
add(checks([
  'Trudności z koncentracją uwagi', 'Niska samoocena i lęk przed porażką',
  'Trudności w rozumieniu poleceń złożonych', 'Problemy z grafomotoryką i tempem pisania',
  'Trudności w relacjach rówieśniczych', 'Bariery komunikacyjne (mowa, język)',
  'Nadwrażliwość sensoryczna (hałas, światło)', 'Trudności w planowaniu i organizacji pracy',
  'Niska motywacja do wysiłku', 'Trudności w radzeniu sobie z emocjami'
], 2));
add(ta('Bariery i ograniczenia utrudniające funkcjonowanie i uczestnictwo w życiu szkolnym', { lines: 4, hint: 'Podpowiedź: opisz osobno bariery po stronie środowiska (hałas, liczna klasa, tempo pracy, zmiany planu bez uprzedzenia, materiały wyłącznie w formie tekstu ciągłego), po stronie ucznia oraz bariery w uczestnictwie (rezygnacja z pracy w grupie, z wystąpień na forum klasy).' }));
add(ta('Uwarunkowania zdrowotne, leki, zalecenia i postępowanie w sytuacji nagłej', { lines: 4, hint: 'Podpowiedź: przeciwwskazania do zajęć wychowania fizycznego i wyjść, zasady podawania leków (rodzic albo osoba pisemnie upoważniona, zaświadczenie i pisemna zgoda), procedura w sytuacji nagłej: bezpieczeństwo, powiadomienie dyrektora i rodzica, w razie potrzeby pomoc medyczna, odnotowanie zdarzenia.' }));
add(legal('Wielospecjalistyczna ocena uwzględnia „występujące trudności w funkcjonowaniu ucznia (…) oraz, w zależności od potrzeb, zakres i charakter wsparcia ze strony nauczycieli, specjalistów (…) lub przyczyny niepowodzeń edukacyjnych albo trudności w funkcjonowaniu ucznia, w tym bariery i ograniczenia utrudniające funkcjonowanie i uczestnictwo ucznia w życiu szkolnym” — § 6 ust. 10 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.). Dane o stanie zdrowia przetwarza się na podstawie art. 9 ust. 2 lit. g RODO.'));

add(brk());

/* ====================== VI. ABC ====================== */
add(section('VI', 'Obserwacja ABC — funkcjonalna analiza zachowania', 'wypełniana, gdy występuje zachowanie trudne'));
add(howto('Obserwacja ABC pozwala zrozumieć przyczynę i cel zachowania trudnego, a nie tylko je ocenić. Notujemy trzy elementy: A — poprzednik, czyli co działo się tuż przed i wyzwoliło zachowanie; B — zachowanie, czyli co dokładnie i obserwowalnie zrobił uczeń, opis faktów bez ocen; C — następstwo, czyli reakcja otoczenia tuż po zachowaniu, która je podtrzymuje albo wygasza. Celem jest rozpoznanie funkcji zachowania i nauczenie ucznia zachowania zastępczego, które tę samą funkcję spełni w sposób akceptowalny (model pozytywnego wsparcia zachowań — PBS).'));
add(subhead('A · Poprzedniki — co wyzwoliło zachowanie'));
add(checks([
  'Polecenie nauczyciela', 'Zmiana aktywności',
  'Hałas w klasie', 'Trudne zadanie',
  'Brak uwagi dorosłego', 'Odmowa prośby',
  'Przerwa / czas wolny', 'Interakcja z rówieśnikiem'
], 2));
add(subhead('B · Zachowanie — co wystąpiło'));
add(checks([
  'Krzyk / hałasowanie', 'Odmowa wykonania zadania',
  'Agresja słowna lub fizyczna', 'Ucieczka z miejsca pracy',
  'Niszczenie przedmiotów', 'Autoagresja',
  'Płacz / wycofanie', 'Ignorowanie poleceń'
], 2));
add(subhead('C · Konsekwencja — jaka była reakcja otoczenia'));
add(checks([
  'Upomnienie słowne', 'Przerwanie zadania',
  'Odesłanie do wyciszenia', 'Utrata przywileju',
  'Pomoc w wykonaniu zadania', 'Ignorowanie zachowania',
  'Kontakt z rodzicem', 'Pochwała za uspokojenie'
], 2));

add(brk());

add(ta('Hipoteza funkcji zachowania — czemu to zachowanie służy (uwaga · ucieczka · dostęp · stymulacja)', { lines: 5, hint: 'Podpowiedź: kiedy zachowanie pojawia się najczęściej, jaką funkcję pełni (ucieczka i unikanie wymagania, uzyskanie uwagi, dostęp do przedmiotu lub aktywności, stymulacja) i w jakich sytuacjach się NIE pojawia — to ostatnie potwierdza hipotezę.' }));
add(ta('Zachowanie alternatywne do wyuczenia i sposób reagowania zespołu (PBS)', { lines: 5, hint: 'Podpowiedź: jak modyfikujemy poprzedniki (uprzedzanie o zmianie, plan dnia, minutnik, podział zadania na etapy, wybór z dwóch opcji, ograniczenie hałasu) oraz jakie zachowanie zastępcze pełniące tę samą funkcję uczeń ma opanować (np. karta „przerwa”). Zachowanie trudne nie kończy zadania — po wyciszeniu wracamy do niego w skróconej formie.' }));
add(note('Przeniesienie wyniku.', 'Wniosek z obserwacji ABC przenosi się do sfery 2 (emocjonalno-społecznej) jako podstawę celu SMART oraz do sekcji XX, jeżeli zachowanie uzasadnia wsparcie osobowe. Bez hipotezy funkcji i zachowania alternatywnego analiza pozostaje opisem zdarzeń i nie prowadzi do żadnego działania.'));

add(brk());

/* ====================== VII. KSZOF ====================== */
add(section('VII', 'Podsumowanie obszarów KSzOF — wynik oceny funkcjonalnej', 'wyniki przenoszone z arkusza KSzOF'));
add(howto('Wyniki punktowe i steny przenosisz z wypełnionego arkusza KSzOF. Sten wyznacza poziom wsparcia w obszarze według legendy pod tabelą. Etap oznacza moment oceny: W — wstępna, Ś — śródroczna, K — końcoworoczna. W kolumnie „oceniający” wpisujesz inicjał roli: N — nauczyciel, K — koordynator, R — rodzic, S — specjalista.'));
add(table(['Lp.', 'Obszar funkcjonowania (ICF)', 'Pkt', 'Sten', 'Oceniający', 'Etap', 'Poziom'],
  [
    ['1', 'Uczenie się i stosowanie wiedzy · d110–d179', '', '', '', '', ''],
    ['2', 'Ogólne zadania i obowiązki · d210–d240', '', '', '', '', ''],
    ['3', 'Porozumiewanie się · d310–d360', '', '', '', '', ''],
    ['4', 'Motoryka i poruszanie się · d410–d475', '', '', '', '', ''],
    ['5', 'Dbanie o siebie i samoobsługa · d510–d570', '', '', '', '', ''],
    ['6', 'Życie domowe · d610–d660', '', '', '', '', ''],
    ['7', 'Wzajemne kontakty i związki · d710–d770', '', '', '', '', ''],
    ['8', 'Edukacja szkolna · d810–d839', '', '', '', '', ''],
    ['9', 'Życie w społeczności lokalnej · d910–d950', '', '', '', '', '']
  ], [600, 3746, 900, 900, 1300, 900, 1400], { center: [0, 2, 3, 4, 5, 6], rowHeight: 400 }));
add(scale([
  { k: 'sten 1–4', v: 'Poziom III — wsparcie specjalistyczne', bg: 'FBE3DC', fg: 'B8350D' },
  { k: 'sten 5–7', v: 'Poziom II — wsparcie dodatkowe (pomoc pp)', bg: 'FDF0E2', fg: 'C47A10' },
  { k: 'sten 8–10', v: 'Poziom I — wsparcie minimalne (bieżąca praca nauczyciela)', bg: 'EFEAF9', fg: '2D1B69' }
]));
add(fields([
  { label: 'Sten najniższy — obszar decydujący', value: '' },
  { label: 'Rekomendowany ogólny poziom wsparcia', value: '', hint: 'I / II / III' }
], 2));
add(note('Reguła nadrzędna:', 'o ogólnym poziomie wsparcia decyduje obszar o najniższym wyniku, a nie średnia wszystkich obszarów. Uczeń z jednym obszarem na poziomie III wymaga wsparcia specjalistycznego w tym obszarze niezależnie od tego, jak dobre są wyniki pozostałe. Skala stenowa 1–10 i trzystopniowe poziomy wsparcia I–III wynikają z modelu oceny funkcjonalnej, nie wprost z rozporządzenia.'));

add(brk());

/* ====================== VIII. PROFIL ====================== */
add(section('VIII', 'Profil funkcjonalny i charakterystyka poziomów wsparcia', 'opis poziomów I–III · jedno miejsce w całym dokumencie'));
add(bars([
  { label: 'I · Uczenie się', value: null }, { label: 'II · Zadania i obowiązki', value: null },
  { label: 'III · Porozumiewanie się', value: null }, { label: 'IV · Motoryka', value: null },
  { label: 'V · Dbanie o siebie', value: null }, { label: 'VI · Życie domowe', value: null },
  { label: 'VII · Kontakty', value: null }, { label: 'VIII · Edukacja szkolna', value: null },
  { label: 'IX · Życie społeczne', value: null }
], { title: 'Profil funkcjonalny KSzOF — sten w obszarach (skala 1–10)' }));
add(text('Wpisz sten z tabeli w sekcji VII i zamaluj słupek do odpowiedniej wysokości — skala 0–10 od lewej do prawej. Mapa profilu pokazuje, które obszary decydują o poziomie wsparcia w poszczególnych sferach programu.',
  { size: 14, italic: true, color: C.muted, after: 160 }));
add(note('Poziom I — wsparcie minimalne · bieżąca praca nauczyciela · sten 8–10', 'Uczeń pracuje w większości samodzielnie. Potrzebuje okazjonalnych wskazówek, przypomnienia polecenia i sprawdzenia efektu pracy. Wystarczają rozwiązania dostępne w bieżącej pracy nauczyciela: miejsce w pierwszej ławce, powtórzenie instrukcji, dodatkowy czas na dokończenie zadania. Obszar traktujemy jako zasób i wykorzystujemy go do wprowadzania umiejętności z obszarów słabszych.', '2D1B69'));
add(note('Poziom II — wsparcie dodatkowe · pomoc psychologiczno-pedagogiczna · sten 5–7', 'Funkcje częściowo obniżone. Uczeń realizuje zadania z umiarkowanym wsparciem: wydłużony czas, podział zadania na etapy, wsparcie wizualne, przypomnienia i sprawdzanie zrozumienia polecenia. Konieczne są stałe dostosowania metod i form pracy oraz zajęcia w ramach pomocy psychologiczno-pedagogicznej (sekcja XIX).', 'C47A10'));
add(note('Poziom III — wsparcie specjalistyczne · sten 1–4', 'Funkcje znacznie ograniczone. Uczeń pracuje krok po kroku, ze stałym wsparciem dorosłego, na materiale konkretnym, z indywidualnym dostosowaniem i — gdy trzeba — pomocą „ręka na ręce”. Wymaga zajęć rewalidacyjnych (sekcja XVIII), indywidualnego programu w tym obszarze, a często również wsparcia osobowego (sekcja XX).', 'B8350D'));
add(ta('Opis wyników oceny funkcjonalnej — synteza zespołu', { lines: 4 }));

add(brk());

/* ====================== CZĘŚĆ II + IX ====================== */
add(partBanner('Część II · program', 'IPET — indywidualny program edukacyjno-terapeutyczny',
  'zalecenia · cele SMART w sześciu sferach · dostosowania · formy wsparcia'));
add(section('IX', 'Zalecenia i sposób ich realizacji w szkole', 'jedna tabela · kolumna źródła'));
add(table(['Lp.', 'Źródło', 'Treść zalecenia', 'Sposób realizacji w szkole / placówce'],
  [
    ['1', 'orzeczenie', '', ''],
    ['2', 'orzeczenie', '', ''],
    ['3', 'orzeczenie', '', ''],
    ['4', 'orzeczenie', '', ''],
    ['5', 'opinia PPP', '', ''],
    ['6', 'opinia PPP', '', '']
  ], [600, 1500, 3823, 3823], { center: [0], rowHeight: 620 }));
add(legal('Program opracowuje się „uwzględniając zalecenia zawarte w orzeczeniu o potrzebie kształcenia specjalnego” — § 6 ust. 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.). Wiersze oznaczone „opinia PPP” wypełnia się wyłącznie wtedy, gdy uczeń posiada odrębną opinię poradni psychologiczno-pedagogicznej — dla ucznia z orzeczeniem nie jest ona wymagana.'));

add(brk());

module.exports = B;
