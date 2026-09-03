const L = require('../lib.js');
const { section, howto, lead, legal, note, ta, fields, checks, table, scale, bars, signatures, brk, text, subhead, dotline, C, AlignmentType } = L;

const B = [];
const add = (...xs) => xs.forEach(x => Array.isArray(x) ? B.push(...x) : B.push(x));

/* ====================== STRONA TYTUŁOWA + SEKCJA I ====================== */
add(text('Narzędzie obserwacji · arkusz do wypełnienia', { size: 15, bold: true, color: C.orange, caps: true, align: AlignmentType.CENTER, before: 240, after: 160 }));
add(text('Wielospecjalistyczna Ocena Poziomu Funkcjonowania (WOPF)', { size: 40, bold: true, color: C.purple, align: AlignmentType.CENTER, after: 80, line: 300 }));
add(text('· · ·   ocena zintegrowana · dokument scalający · przedszkole · 2026   · · ·', { size: 15, bold: true, color: C.orange, caps: true, align: AlignmentType.CENTER, after: 200 }));

add(fields([
  { label: 'Dotyczy dziecka', value: '' },
  { label: 'Grupa', value: '' },
  { label: 'Data sporządzenia', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Rok przedszkolny', value: '', hint: '20…/20…' }
], 2));

add(lead('Karta scalająca — WOPF przedszkolny · jeden druk, dwie ścieżki',
  'Wielospecjalistyczna ocena poziomu funkcjonowania zbiera w jeden obraz dziecka wyniki wszystkich druków obserwacyjnych prowadzonych w przedszkolu: KPOF, karty analizy zachowania ABC · FBA, karty oceny teorii umysłu, kwestionariusza rozwoju mowy, profilu sensorycznego oraz profilu biopsychospołecznego. Zespół nie ocenia tutaj powtórnie tego, co zostało już ocenione — przenosi wyniki, interpretuje je łącznie, podejmuje decyzję o poziomie wsparcia i przekazuje wnioski dalej: do indywidualnego programu edukacyjno-terapeutycznego, gdy dziecko ma orzeczenie, albo do planu wsparcia w ramach pomocy psychologiczno-pedagogicznej, gdy orzeczenia nie ma. Ścieżkę wybiera się w sekcji I a. Ocena powstaje w modelu biopsychospołecznym ICF.'));

add(howto('Ten druk nie powtarza oceniania. Wyniki wpisujesz z druków źródłowych: KPOF — do sekcji V, karta analizy zachowania ABC · FBA — do sekcji VI, karta oceny teorii umysłu (ToM) — do sekcji VII, kwestionariusz rozwoju mowy — do sekcji VIII, profil sensoryczny — do sekcji IX, profil biopsychospołeczny — do sekcji X. Sekcja V a to opis jakościowy obszarów, sekcje XI–XIII są syntezą wszystkich źródeł, sekcje XIV–XVI zawierają decyzję zespołu, a sekcja XVIII wskazuje — w dwóch kolumnach — co przenosimy do IPET albo do planu pomocy psychologiczno-pedagogicznej. Pod każdą sekcją znajduje się ramka z podstawą prawną lub metodologiczną. Jeżeli któregoś druku nie prowadzono, wpisz „nie dotyczy” i uzasadnij to w syntezie.'));

add(brk());

/* ====================== I. DANE DZIECKA ====================== */
add(section('I', 'Dane dziecka', 'zakres minimalny — bez danych zbędnych'));
add(fields([
  { label: 'Imię i nazwisko', value: '' },
  { label: 'Wiek dziecka', value: '', hint: 'lat / miesięcy' },
  { label: 'Grupa', value: '' },
  { label: 'Rok przedszkolny', value: '' },
  { label: 'Podstawa objęcia wsparciem', value: '', hint: 'orzeczenie o potrzebie kształcenia specjalnego / opinia / rozpoznanie nauczycieli' },
  { label: 'Rozpoznanie wiodące (wg orzeczenia lub obserwacji)', value: '' },
  { label: 'Koordynator zespołu', value: '' },
  { label: 'Data sporządzenia', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Data poprzedniej oceny', value: '', hint: 'dd.mm.rrrr / nie dotyczy' },
  { label: 'Numer dokumentu w rejestrze', value: '', hint: 'WOPF / … / 20…' }
], 2));
add(ta('Powód sporządzenia oceny — kontekst zgłoszenia i oczekiwania rodziców', { lines: 3, hint: 'Podpowiedź: kto zgłosił potrzebę oceny (nauczyciel, rodzic, poradnia), co skłoniło zespół do jej dokonania oraz czego oczekują rodzice. Wpisz zwięźle, w kategoriach obserwowalnych sytuacji dnia.' }));
add(legal('Zasada minimalizacji danych — art. 5 ust. 1 lit. c RODO (UE 2016/679): przetwarza się wyłącznie dane niezbędne do celu. Dlatego metryczka nie zawiera numeru PESEL, adresu zamieszkania, miejsca urodzenia, obywatelstwa, numerów dokumentów ani danych o miejscu pracy rodziców — te dane pozostają wyłącznie w dokumentacji przebiegu nauczania (rozp. MEN z 25.08.2017 r., Dz.U. 2017 poz. 1646, z późn. zm.).'));

add(brk());

/* ====================== I a. ŚCIEŻKA ====================== */
add(section('I a', 'Ścieżka dokumentacyjna, rodzaj oceny i tryb', 'jeden druk — dwie ścieżki · zaznacz właściwą'));
add(howto('Ten druk obsługuje dwie sytuacje przedszkolne. Zaznacz jedną ścieżkę — od niej zależy wyłącznie nazwa dokumentu wynikowego i jego podstawa prawna. Wszystkie sekcje opisowe (II–XVII) wypełnia się tak samo w obu ścieżkach, a sekcja XVIII ma dwie kolumny: osobno to, co przenosimy do IPET, i osobno to, co przenosimy do planu wsparcia w ramach pomocy psychologiczno-pedagogicznej.'));
add(checks([
  'ŚCIEŻKA A — dziecko POSIADA orzeczenie o potrzebie kształcenia specjalnego → wielospecjalistyczna ocena poziomu funkcjonowania (WOPFU) i indywidualny program edukacyjno-terapeutyczny (IPET) — rozp. Dz.U. 2017 poz. 1578',
  'ŚCIEŻKA B — dziecko NIE POSIADA orzeczenia → rozpoznanie indywidualnych potrzeb rozwojowych i edukacyjnych oraz plan wsparcia w ramach pomocy psychologiczno-pedagogicznej — rozp. Dz.U. 2017 poz. 1591'
], 1));
add(subhead('Rodzaj oceny'));
add(checks([
  'wstępna — przed opracowaniem IPET albo przed ustaleniem form pomocy pp',
  'okresowa — śródroczna',
  'okresowa — roczna',
  'doraźna — po istotnej zmianie w funkcjonowaniu dziecka'
], 2));
add(fields([
  { label: 'Współpraca z poradnią psychologiczno-pedagogiczną', value: '', hint: 'nie dotyczy / nazwa (za zgodą rodziców)' },
  { label: 'Zawiadomienie rodziców o terminie spotkania', value: '', hint: 'data pisma' },
  { label: 'Obecność rodzica na posiedzeniu', value: '', hint: 'tak / nie / nieobecność usprawiedliwiona' },
  { label: 'Data posiedzenia zespołu', value: '', hint: 'dd.mm.rrrr' }
], 2));
add(note('Terminy.', 'ŚCIEŻKA A: IPET opracowuje się do 30 września — gdy dziecko rozpoczyna wychowanie przedszkolne od początku roku — albo w ciągu 30 dni od dnia złożenia w przedszkolu orzeczenia o potrzebie kształcenia specjalnego (§ 6 ust. 6 rozp. poz. 1578); ocena poprzedza opracowanie programu (§ 6 ust. 4), a ocena okresowa dokonywana jest co najmniej dwa razy w roku (§ 6 ust. 9). ŚCIEŻKA B: pomocy udziela się niezwłocznie po rozpoznaniu potrzeby, a nauczyciele i specjaliści oceniają efektywność udzielanej pomocy na bieżąco (§ 20 i § 21 rozp. poz. 1591) — w przedszkolu przyjmujemy ten sam rytm: po pierwszym półroczu i na zakończenie roku.'));
add(legal('ŚCIEŻKA A — art. 127 ustawy z 14.12.2016 r. — Prawo oświatowe (t.j. Dz.U. 2024 poz. 737, z późn. zm.) oraz § 6 ust. 4 i 9 rozp. MEN z 9.08.2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym (Dz.U. 2017 poz. 1578; t.j. Dz.U. 2020 poz. 1309). ŚCIEŻKA B — art. 47 ust. 1 pkt 5 Prawa oświatowego oraz § 2–4 i § 20 rozp. MEN z 9.08.2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej w publicznych przedszkolach, szkołach i placówkach (Dz.U. 2017 poz. 1591, z późn. zm.) — rozpoznawanie indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych dziecka należy do zadań nauczycieli i specjalistów.'));

add(brk());

/* ====================== II. ZESPÓŁ ====================== */
add(section('II', 'Zespół specjalistów', 'skład i funkcje'));
add(table(['Lp.', 'Imię i nazwisko', 'Specjalność', 'Funkcja w zespole'],
  [
    ['1', '', '', 'Koordynator zespołu'],
    ['2', '', '', 'Nauczyciel wychowania przedszkolnego'],
    ['3', '', '', 'Psycholog'],
    ['4', '', '', 'Pedagog specjalny'],
    ['5', '', '', 'Logopeda / neurologopeda'],
    ['6', '', '', 'Terapeuta SI'],
    ['7', '', '', ''],
    ['8', '', '', '']
  ], [700, 3400, 2600, 3046], { center: [0], rowHeight: 620 }));
add(subhead('Osoby uczestniczące w spotkaniu zespołu (§ 6 ust. 8)'));
add(checks([
  'przedstawiciel poradni psychologiczno-pedagogicznej', 'asystent lub pomoc nauczyciela',
  'rodzic / opiekun prawny', 'inne osoby — na wniosek lub za zgodą rodziców'
], 2));
add(fields([
  { label: 'Data spotkania zespołu', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Miejsce spotkania', value: '' }
], 2));
add(legal('Skład zespołu: § 6 ust. 3 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578; t.j. Dz.U. 2020 poz. 1309) — nauczyciele i specjaliści prowadzący zajęcia z uczniem. Praca zespołu koordynowana jest przez wychowawcę albo wyznaczonego nauczyciela lub specjalistę (§ 6 ust. 7). W spotkaniach zespołu mogą uczestniczyć przedstawiciel poradni psychologiczno-pedagogicznej, asystent lub pomoc nauczyciela, a także — na wniosek lub za zgodą rodziców — inne osoby (§ 6 ust. 8). Dyrektor zawiadamia pisemnie rodziców o terminie każdego spotkania zespołu (§ 6 ust. 12). Obowiązek dokonania WOPF: art. 127 ustawy — Prawo oświatowe (t.j. Dz.U. 2024 poz. 737, z późn. zm.) oraz § 6 ust. 4 i 9 rozporządzenia.'));

add(brk());

/* ====================== III. MAPA DOKUMENTÓW ====================== */
add(section('III', 'Mapa dokumentów źródłowych', 'każdy wynik ma jedno źródło'));
add(howto('Zasada jednego źródła: każdy wynik pochodzi z jednego, wskazanego niżej druku i trafia do jednej sekcji tej oceny. W tabeli uzupełnij, kto wypełnił dany druk i kiedy — ostatnia kolumna wskazuje z góry, dokąd wynik przenosimy. Jeżeli danego druku nie prowadzono, wpisz „nie dotyczy”; brak druku nie zwalnia zespołu z opisania obszaru w syntezie.'));
add(table(['Lp.', 'Druk źródłowy (narzędzie)', 'Kto wypełnił', 'Data', 'Wynik przeniesiony do sekcji'],
  [
    ['1', 'KPOF — Kwestionariusz Przedszkolnej Oceny Funkcjonalnej (9 obszarów ICF, skala 1–5)', '', '', 'sekcja V'],
    ['2', 'Karta analizy zachowania ABC · FBA (funkcje zachowania)', '', '', 'sekcja VI'],
    ['3', 'Karta oceny teorii umysłu (ToM)', '', '', 'sekcja VII'],
    ['4', 'Kwestionariusz rozwoju mowy (PCTP)', '', '', 'sekcja VIII'],
    ['5', 'Profil sensoryczny (model Dunn, 7 układów)', '', '', 'sekcja IX'],
    ['6', 'Profil biopsychospołeczny (ICF — czynniki kontekstowe)', '', '', 'sekcja X'],
    ['7', 'Wywiad z rodzicem / dziennik obserwacji', '', '', 'sekcje XI–XII']
  ], [640, 3900, 1900, 1206, 2100], { center: [0, 3, 4], rowHeight: 380 }));
add(subhead('Sytuacje dnia objęte obserwacją — zaznacz wszystkie, w których zbierano dane'));
add(checks([
  'zajęcia kierowane w grupie', 'zabawa swobodna',
  'zabawa w małej grupie', 'sytuacje przejściowe (zmiana aktywności)',
  'posiłek', 'ubieranie i samoobsługa',
  'ogród przedszkolny / plac zabaw', 'leżakowanie i odpoczynek',
  'zajęcia rewalidacyjne i specjalistyczne', 'uroczystości i sytuacje nowe'
], 2));
add(subhead('Zakres i czas obserwacji'));
add(fields([
  { label: 'Typ obserwacji', value: '', hint: 'strukturalna + naturalistyczna' },
  { label: 'Łączny czas / liczba sesji', value: '' },
  { label: 'Okres obserwacji (od–do)', value: '', hint: 'dd.mm.rrrr – dd.mm.rrrr' },
  { label: 'Miejsca obserwacji', value: '', hint: 'sala / ogród / szatnia / stołówka' }
], 2));
add(legal('Obowiązek prowadzenia obserwacji pedagogicznych zakończonych analizą i oceną gotowości dziecka do podjęcia nauki w szkole — § 2 ust. 1 pkt 3 rozp. MEN z 14.02.2017 r. w sprawie podstawy programowej wychowania przedszkolnego (Dz.U. 2017 poz. 356, z późn. zm.). Rozpoznawanie potrzeb w toku bieżącej pracy — § 20 ust. 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591). Wielospecjalistyczny charakter oceny — § 6 ust. 3 i 4 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578). Metodologia wielu źródeł danych: Model Szkolnej Oceny Funkcjonalnej (MEN 2024) — zasada triangulacji, oraz klasyfikacja ICF (WHO 2001).'));

add(brk());

/* ====================== IV. INFORMACJE MEDYCZNE ====================== */
add(section('IV', 'Informacje medyczne istotne dla funkcjonowania', 'dane szczególnej kategorii — art. 9 RODO'));
add(checks([
  'cukrzyca', 'padaczka',
  'alergie pokarmowe / wziewne', 'astma i układ oddechowy',
  'wada serca', 'inna choroba przewlekła',
  'leki podawane w przedszkolu', 'zachowania wymagające interwencji',
  'dieta eliminacyjna', 'wsparcie w samoobsłudze ze względów zdrowotnych'
], 2));
add(ta('Przyjmowane leki i sposób podania', { lines: 3, hint: 'Podpowiedź: Dziecko nie przyjmuje leków na terenie przedszkola. Jeżeli lek jest zlecony — podaje go wyłącznie rodzic albo osoba pisemnie upoważniona, na podstawie zaświadczenia lekarskiego i pisemnej zgody rodziców; fakt podania odnotowujemy w zeszycie zdrowia grupy.' }));
add(ta('Zalecenia i przeciwwskazania (w tym dieta)', { lines: 3, hint: 'Podpowiedź: Brak przeciwwskazań do udziału w zajęciach ruchowych i wyjściach do ogrodu. Obowiązuje dieta bez wskazań eliminacyjnych; przy zmianie zaleceń rodzic dostarcza aktualne zaświadczenie. Zalecana jest przewidywalność planu dnia i uprzedzanie o zmianach — wynika to z profilu funkcjonowania, nie ze wskazań medycznych.' }));
add(ta('Postępowanie w sytuacji nagłej — procedura i kontakt', { lines: 3, hint: 'Podpowiedź: W sytuacji nagłej nauczyciel zapewnia dziecku bezpieczeństwo i spokojne miejsce, powiadamia dyrektora i niezwłocznie rodzica (telefon w karcie zgłoszeniowej), a w razie potrzeby wzywa pomoc medyczną. Zdarzenie odnotowujemy w dokumentacji grupy i omawiamy na najbliższym spotkaniu zespołu.' }));
add(legal('§ 6 ust. 10 pkt 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578; t.j. Dz.U. 2020 poz. 1309) — indywidualne potrzeby rozwojowe i edukacyjne obejmują możliwości psychofizyczne oraz uwarunkowania zdrowotne ucznia. Art. 9 ust. 2 lit. g RODO (UE 2016/679) — dane o zdrowiu jako dane szczególnej kategorii, przetwarzane w związku z realizacją zadań oświatowych. Ustawa z dnia 12 kwietnia 2019 r. o opiece zdrowotnej nad uczniami (Dz.U. 2019 poz. 1078).'));

add(brk());

/* ====================== V. KPOF ====================== */
add(section('V', 'Wyniki oceny funkcjonalnej KPOF — 9 obszarów ICF', 'źródło: arkusz KPOF (3–4 / 5 / 6 lat)'));
add(fields([
  { label: 'Zastosowany wariant KPOF', value: '', hint: '3–4 lata / 5 lat / 6 lat' },
  { label: 'Liczba ocenionych twierdzeń', value: '' },
  { label: 'Data wypełnienia arkusza', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Osoba wypełniająca arkusz', value: '' }
], 2));
add(scale([
  { k: '< 2,0', v: 'Poziom III — wsparcie specjalistyczne', bg: 'FBE3DC', fg: 'B8350D' },
  { k: '2,0–2,9', v: 'Poziom II — wsparcie dodatkowe (pomoc pp)', bg: 'FDF0E2', fg: 'C47A10' },
  { k: '3,0–3,9', v: 'Poziom I — bieżąca praca nauczyciela', bg: 'EFEAF9', fg: '2D1B69' },
  { k: '4,0–5,0', v: 'Zasób — mocna strona dziecka', bg: 'E1F1EB', fg: '0D7D5C' }
]));
add(table(['Obszar funkcjonowania (ICF)', 'Średnia (1–5)', 'Poziom wsparcia'],
  [
    ['I · Uczenie się i stosowanie wiedzy · d110–d179', '', ''],
    ['II · Ogólne zadania i wymagania · d210–d240', '', ''],
    ['III · Porozumiewanie się · d310–d360', '', ''],
    ['IV · Poruszanie się · d410–d475', '', ''],
    ['V · Dbanie o siebie · d510–d570', '', ''],
    ['VI · Życie domowe (czynności użyteczne) · d620–d660', '', ''],
    ['VII · Wzajemne kontakty i związki międzyludzkie · d710–d770', '', ''],
    ['VIII · Główne obszary życia (edukacja przedszkolna i zabawa) · d815–d880', '', ''],
    ['IX · Życie społeczne, lokalne i obywatelskie · d910–d950', '', '']
  ], [5546, 1800, 2400], { nrCol: false, center: [1, 2], rowHeight: 360 }));

add(brk());

add(bars([
  { label: 'I · Uczenie się', value: null }, { label: 'II · Zadania i wymagania', value: null },
  { label: 'III · Porozumiewanie się', value: null }, { label: 'IV · Poruszanie się', value: null },
  { label: 'V · Dbanie o siebie', value: null }, { label: 'VI · Życie domowe', value: null },
  { label: 'VII · Kontakty z ludźmi', value: null }, { label: 'VIII · Edukacja i zabawa', value: null },
  { label: 'IX · Życie społeczne', value: null }
]));
add(text('Średnia obszaru = suma punktów ÷ liczba ocenionych twierdzeń (bez N). Słupki zamaluj po wydruku albo wypełnij w arkuszu interaktywnym — skala 0–5 od lewej do prawej.',
  { size: 14, italic: true, color: C.muted, after: 140 }));
add(fields([
  { label: 'Średnia ogólna (wszystkie obszary)', value: '' },
  { label: 'Poziom wsparcia', value: '', hint: 'I / II / III' },
  { label: 'Liczba twierdzeń ocenionych na 1–2', value: '' },
  { label: 'Obszar priorytetowy (najniższa średnia)', value: '' }
], 2));
add(note('Reguła nadrzędna.', 'Każde twierdzenie ocenione na 1 lub 2 podlega analizie jakościowej zespołu — niezależnie od tego, jak wysoka jest średnia w obszarze. Wysoka średnia nie przesłania pojedynczych, istotnych trudności, zwłaszcza tych, które dotyczą bezpieczeństwa, porozumiewania się i samoobsługi.'));

add(brk());

add(subhead('Synteza wyników — obszary wg poziomów'));
add(ta('Zasoby i Poziom I — na czym opieramy pracę (śr. ≥ 3,0)', { lines: 4, hint: 'Wzór opisu: Najwyższy wynik dziecko uzyskuje w obszarze … (średnia …). Obszar ten traktujemy jako zasób — przez ruch, zabawę i działanie na materiale konkretnym wprowadzamy nowe umiejętności w pozostałych obszarach. W bieżącej pracy nauczyciela wystarczają rozwiązania dostępne dla całej grupy: czytelna instrukcja, pokaz oraz możliwość wykonania zadania w ruchu.' }));
add(ta('Poziom II — wsparcie dodatkowe w przedszkolu (śr. 2,0–2,9)', { lines: 4, hint: 'Wzór opisu: Obszary … mieszczą się w przedziale …, co oznacza, że dziecko podejmuje typowe aktywności przedszkolne, ale wykonuje je niesystematycznie i z wyraźnym wsparciem dorosłego. Obszary te obejmujemy zaplanowanymi działaniami w ramach pomocy psychologiczno-pedagogicznej: pracą w małej grupie, wydłużonym czasem, podziałem zadania na etapy i systematycznym wzmacnianiem samodzielności.' }));
add(ta('Poziom III — wsparcie specjalistyczne, priorytet (śr. < 2,0)', { lines: 4, hint: 'Wzór opisu: Gdy średnia w którymkolwiek obszarze spadnie poniżej 2,0, obszar ten wymaga wsparcia specjalistycznego, uruchomienia modułu pogłębiającego oraz konsultacji z poradnią psychologiczno-pedagogiczną. Niezależnie od średniej zespół omawia jakościowo każde twierdzenie ocenione na 1 lub 2 i w pierwszej kolejności obejmuje działaniem te, które dotyczą bezpieczeństwa i porozumiewania się.' }));
add(legal('Ocena funkcjonalna w 9 obszarach ICF oraz obserwacja pogłębiona realizują § 6 ust. 10 pkt 1 i 3 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578; t.j. Dz.U. 2020 poz. 1309); metodologia — Model Szkolnej Oceny Funkcjonalnej (MEN 2024) i klasyfikacja ICF (WHO 2001). Poziomy wsparcia I–III wynikają z Modelu SOF, a nie wprost z rozporządzenia. W wersji przedszkolnej (KPOF) poziom wsparcia ustala się na podstawie średnich kryterialnych w skali 1–5, a nie na podstawie skal przeliczeniowych (znormalizowanych).'));

add(brk());

/* ====================== V a. CHARAKTERYSTYKA OBSZARÓW ====================== */
add(section('V a', 'Charakterystyka obszarów — mocne strony i trudności', 'opis jakościowy do każdego obszaru KPOF'));
add(howto('Średnia mówi, jak wysoko dziecko wypadło; ten opis mówi, co się za tą liczbą kryje. W każdym wierszu wpisz najpierw to, co dziecko już potrafi, a dopiero potem to, co sprawia mu trudność — zawsze w kategoriach obserwowalnych zachowań i konkretnych sytuacji dnia (zajęcia kierowane, zabawa swobodna, posiłek, ubieranie, ogród). Ten opis jest źródłem sformułowań dla syntezy w sekcji XI oraz dla opinii wydawanej na zewnątrz.'));
add(table(['Obszar KPOF (ICF)', 'Mocne strony — co dziecko potrafi', 'Trudności — co wymaga wsparcia'],
  [
    ['I · Uczenie się i stosowanie wiedzy', '', ''],
    ['II · Ogólne zadania i wymagania', '', ''],
    ['III · Porozumiewanie się', '', ''],
    ['IV · Poruszanie się', '', ''],
    ['V · Dbanie o siebie', '', ''],
    ['VI · Życie domowe (czynności użyteczne)', '', ''],
    ['VII · Wzajemne kontakty i związki międzyludzkie', '', ''],
    ['VIII · Główne obszary życia (edukacja i zabawa)', '', ''],
    ['IX · Życie społeczne, lokalne i obywatelskie', '', '']
  ], [2946, 3400, 3400], { nrCol: false, rowHeight: 720 }));
add(legal('Opis jakościowy obszarów realizuje wymóg wskazania mocnych stron, predyspozycji i zainteresowań obok trudności — § 6 ust. 10 pkt 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578) dla ścieżki A oraz § 20 ust. 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591) dla ścieżki B. Opis prowadzi się w kategoriach funkcjonalnych, zgodnie z modelem biopsychospołecznym ICF (WHO 2001), a nie w kategoriach deficytu.'));

add(brk());

/* ====================== V b. SYNTEZA OPISOWA ====================== */
add(section('V b', 'Opis wyników oceny funkcjonalnej — synteza opisowa', 'propozycja opisu układa się z wyników'));
add(howto('Cztery pola poniżej to gotowy opis wyników — w arkuszu interaktywnym układa się on sam z wpisanych średnich (sekcja V): wskazuje średnią ogólną i poziom wsparcia, wymienia obszary z nazwy wraz z wynikami, opisuje zasoby i trudności oraz proponuje kierunki pracy i formy zajęć. Propozycja jest punktem wyjścia, nie gotowym orzeczeniem — dopisz to, czego liczba nie pokazuje: sytuacje z dnia, reakcje dziecka, obserwacje rodziców.'));
add(ta('1 · Obraz ogólny — średnia ogólna, rozkład poziomów, obszar najmocniejszy i najsłabszy', { lines: 5 }));
add(ta('2 · Zasoby i mocne strony — na czym opieramy codzienną pracę', { lines: 5 }));
add(ta('3 · Obszary wymagające wsparcia — co sprawia trudność i w jakich sytuacjach dnia', { lines: 5 }));

add(brk());

add(ta('4 · Kierunki pracy, rekomendowane formy zajęć i współpraca z rodzicami', { lines: 7 }));
add(legal('Opis wyników stanowi część oceny, o której mowa w § 6 ust. 9 i 10 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578) — ścieżka A, oraz stanowi rozpoznanie indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych dziecka w rozumieniu § 20 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591) — ścieżka B. Automatycznie generowana propozycja opisu ma charakter pomocniczy; treść oceny ustala i podpisuje zespół, o którym mowa w § 6 ust. 1 poz. 1578 (art. 47 ust. 1 pkt 5 ustawy z 14.12.2016 r. — Prawo oświatowe).'));

/* ====================== VI. ZACHOWANIE ====================== */
add(section('VI', 'Zachowanie — funkcje zachowań trudnych', 'przeniesienie z druku: ABC · FBA'));
add(table(['Lp.', 'Funkcja zachowania (FBA)', 'Suma pkt', 'Nasilenie'],
  [
    ['I', 'Ucieczka / unikanie', '', ''],
    ['II', 'Uzyskanie uwagi', '', ''],
    ['III', 'Dostęp do przedmiotu lub aktywności', '', ''],
    ['IV', 'Stymulacja sensoryczna (automatyczna)', '', ''],
    ['V', 'Komunikat o potrzebie / dyskomforcie', '', '']
  ], [700, 4846, 1900, 2300], { center: [0, 2, 3], rowHeight: 340 }));
add(fields([
  { label: 'Zachowanie kluczowe (opis obserwowalny)', value: '' },
  { label: 'Funkcja dominująca', value: '' },
  { label: 'Częstotliwość i czas trwania', value: '' },
  { label: 'Sytuacje wyzwalające (poprzedniki)', value: '' }
], 2));

add(brk());

add(ta('Hipoteza funkcjonalna — kiedy zachowanie występuje i czemu służy', { lines: 4, hint: 'Podpowiedź: Zgodnie z kartą analizy zachowania ABC · FBA zachowanie trudne pojawia się najczęściej przy zmianie aktywności oraz w zadaniach wymagających dłuższej uwagi, przy podwyższonym poziomie hałasu w sali. Pełni funkcję ucieczki i unikania — pozwala odsunąć wymaganie; wtórnie służy uzyskaniu uwagi dorosłego. Wyniku nie ustalamy tutaj powtórnie — przenosimy go z druku źródłowego.' }));
add(ta('Plan pozytywnego wsparcia (PBS) — modyfikacja poprzedników i zachowanie zastępcze pełniące tę samą funkcję', { lines: 5, hint: 'Podpowiedź: Poprzedniki modyfikujemy: uprzedzamy o zmianie aktywności (plan obrazkowy, minutnik), dzielimy zadanie na krótkie etapy z sygnałem końca, dajemy wybór z dwóch opcji i ograniczamy hałas. Zachowanie zastępcze pełniące tę samą funkcję: dziecko sygnalizuje kartą „przerwa” lub gestem, że potrzebuje odpoczynku. Zachowanie trudne nie prowadzi do zakończenia zadania.' }));
add(note('Ochrona dziecka · Standardy Ochrony Małoletnich (SOM).', 'Wszelkie działania wobec zachowań trudnych prowadzi się zgodnie ze Standardami Ochrony Małoletnich (tzw. „ustawa Kamilka”, Dz.U. 2023 poz. 1606). Zakazane są kary fizyczne, izolacja i przymus bezpośredni. Reakcja opiera się na deeskalacji, zapewnieniu bezpieczeństwa i poszanowaniu godności dziecka; każde zdarzenie jest dokumentowane, a rodzic informowany.', 'B8350D'));
add(legal('Rozpoznanie przyczyn trudności w funkcjonowaniu oraz efektów podjętych działań — § 6 ust. 10 pkt 3 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578). Standardy Ochrony Małoletnich — art. 22b–22c ustawy z 13.05.2016 r. o przeciwdziałaniu zagrożeniom przestępczością na tle seksualnym i ochronie małoletnich, w brzmieniu nadanym ustawą z 28.07.2023 r. (Dz.U. 2023 poz. 1606). Zakaz stosowania kar cielesnych — art. 96¹ Kodeksu rodzinnego i opiekuńczego. Metodologia: ocena funkcjonalna zachowania (FBA) i pozytywne wsparcie zachowań (PBS) — analiza w schemacie A–B–C.'));

add(brk());

module.exports = B;
