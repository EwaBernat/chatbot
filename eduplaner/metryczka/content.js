const L = require('../lib.js');
const { section, howto, lead, legal, note, ta, fields, checks, table, signatures,
        brk, text, subhead, C, AlignmentType } = L;

const B = [];
const add = (...xs) => xs.forEach(x => Array.isArray(x) ? B.push(...x) : B.push(x));

/* ====================== NAGŁÓWEK DOKUMENTU ====================== */
add(text('Metryczka · rok szkolny 2026 / 27', { size: 15, bold: true, color: C.orange, caps: true, align: AlignmentType.CENTER, before: 160, after: 140 }));
add(text('Metryczka dziecka', { size: 40, bold: true, color: C.purple, align: AlignmentType.CENTER, after: 80, line: 300 }));
add(text('· · ·   EduPlaner 2026 · karta danych dziecka · dane i dokumentacja   · · ·', { size: 15, bold: true, color: C.orange, caps: true, align: AlignmentType.CENTER, after: 180 }));
add(fields([
  { label: 'Dotyczy dziecka', value: '' },
  { label: 'Grupa', value: '' },
  { label: 'Rok szkolny', value: '', hint: '2026 / 2027' },
  { label: 'Data założenia karty', value: '', hint: 'dd.mm.rrrr' }
], 2));
add(lead('Karta danych dziecka — jedno miejsce dla całej teczki',
  'Karta gromadzi w jednym miejscu dane osobowe dziecka, informacje o rodzicach i opiekunach, stanie zdrowia i potrzebach oraz spis dokumentacji prowadzonej w przedszkolu. Stanowi element dokumentacji przebiegu wychowania przedszkolnego. Dane przetwarzane są wyłącznie w celach dydaktyczno-wychowawczych i opiekuńczych, zgodnie z RODO oraz ustawą — Prawo oświatowe. Dokument zawiera dane wrażliwe — przechowywany jest w sposób uniemożliwiający dostęp osobom nieupoważnionym.'));

/* ====================== I. DANE OSOBOWE ====================== */
add(section('I', 'Dane osobowe dziecka', 'metryczka podstawowa'));
add(fields([
  { label: 'Imię i nazwisko', value: '' },
  { label: 'PESEL', value: '' },
  { label: 'Data urodzenia', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Miejsce urodzenia', value: '' },
  { label: 'Obywatelstwo', value: '' },
  { label: 'Adres zamieszkania', value: '' },
  { label: 'Adres zameldowania (jeśli inny)', value: '' },
  { label: 'Numer w ewidencji / księdze dzieci', value: '' }
], 2));

add(brk());

/* ====================== II. POBYT ====================== */
add(section('II', 'Przynależność i organizacja pobytu', 'grupa · czas pobytu · posiłki'));
add(fields([
  { label: 'Grupa / oddział', value: '' },
  { label: 'Rok szkolny', value: '', hint: '2026 / 2027' },
  { label: 'Data przyjęcia', value: '', hint: 'dd.mm.rrrr' },
  { label: 'Nauczyciel / wychowawca grupy', value: '' },
  { label: 'Godziny pobytu', value: '', hint: 'od — do' },
  { label: 'Posiłki', value: '', hint: 'śniadanie / obiad / podwieczorek' },
  { label: 'Rok obowiązkowego przygotowania przedszkolnego', value: '', hint: 'tak / nie · rok' },
  { label: 'Sposób przyprowadzania i odbioru', value: '' }
], 2));

/* ====================== III. RODZICE ====================== */
add(section('III', 'Rodzice / opiekunowie prawni', 'dane kontaktowe'));
add(subhead('Matka / opiekun prawny'));
add(fields([
  { label: 'Imię i nazwisko', value: '' },
  { label: 'Telefon', value: '' },
  { label: 'E-mail', value: '' },
  { label: 'Miejsce pracy', value: '' },
  { label: 'Adres zamieszkania', value: '' },
  { label: 'Preferowana forma kontaktu', value: '' }
], 2));
add(subhead('Ojciec / opiekun prawny'));
add(fields([
  { label: 'Imię i nazwisko', value: '' },
  { label: 'Telefon', value: '' },
  { label: 'E-mail', value: '' },
  { label: 'Miejsce pracy', value: '' },
  { label: 'Adres zamieszkania', value: '' },
  { label: 'Preferowana forma kontaktu', value: '' }
], 2));

add(brk());

/* ====================== IV. ODBIÓR DZIECKA ====================== */
add(section('IV', 'Osoby upoważnione do odbioru dziecka', 'upoważnienie pisemne rodziców'));
add(table(['Lp.', 'Imię i nazwisko', 'Pokrewieństwo', 'Nr dokumentu', 'Telefon'],
  [
    ['1', '', '', '', ''],
    ['2', '', '', '', ''],
    ['3', '', '', '', ''],
    ['4', '', '', '', ''],
    ['5', '', '', '', ''],
    ['6', '', '', '', '']
  ], [600, 3146, 2000, 2000, 2000], { center: [0], rowHeight: 480 }));
add(note('Zasada odbioru.', 'Dziecko wydaje się wyłącznie rodzicom (opiekunom prawnym) albo osobom pisemnie przez nich upoważnionym, po okazaniu dokumentu tożsamości. Zmianę listy upoważnień rodzic zgłasza na piśmie; poprzedni wpis pozostaje w dokumentacji z datą wykreślenia.'));

/* ====================== V. NAGŁE WYPADKI ====================== */
add(section('V', 'Kontakt w nagłych wypadkach', 'kolejność powiadamiania'));
add(table(['Lp.', 'Osoba do kontaktu', 'Telefon', 'Relacja / pokrewieństwo'],
  [
    ['1', '', '', ''],
    ['2', '', '', ''],
    ['3', '', '', '']
  ], [600, 3746, 2200, 3200], { center: [0], rowHeight: 480 }));

add(brk());

/* ====================== VI. ZDROWIE ====================== */
add(section('VI', 'Informacje o zdrowiu i potrzebach', 'zaznacz występujące — szczegóły poniżej'));
add(checks([
  'Alergie pokarmowe', 'Alergie inne (leki, kontaktowe)',
  'Choroby przewlekłe', 'Stałe przyjmowanie leków',
  'Dieta eliminacyjna / specjalna', 'Wady wzroku / słuchu',
  'Ograniczenia ruchowe', 'Nadwrażliwość sensoryczna'
], 2));
add(ta('Szczegóły — alergie, choroby, leki, dieta, zalecenia lekarskie', { lines: 5, hint: 'Wpisz rozpoznanie, objawy, czynniki wyzwalające oraz zalecenia lekarza. Przy diecie podaj produkty wykluczone i sposób ich zastępowania.' }));
add(ta('Zalecenia dotyczące postępowania (np. pomoc przedmedyczna, procedury)', { lines: 5, hint: 'Wpisz, co robi nauczyciel w sytuacji nagłej, kto podaje lek i na jakiej podstawie (zaświadczenie lekarskie i pisemna zgoda rodziców), gdzie przechowywany jest lek oraz kogo i w jakiej kolejności powiadamiamy.' }));

add(brk());

/* ====================== VII. WSPARCIE ====================== */
add(section('VII', 'Objęcie wsparciem i dokumentacja specjalna', 'podstawa objęcia wsparciem'));
add(table(['Rodzaj dokumentu / formy wsparcia', 'Czy dotyczy', 'Numer i data / od kiedy'],
  [
    ['Orzeczenie o potrzebie kształcenia specjalnego', '□  tak      □  nie', ''],
    ['Opinia poradni psychologiczno-pedagogicznej', '□  tak      □  nie', ''],
    ['Objęcie pomocą psychologiczno-pedagogiczną', '□  tak      □  nie', ''],
    ['Wczesne wspomaganie rozwoju (WWR)', '□  tak      □  nie', ''],
    ['Orzeczenie o niepełnosprawności', '□  tak      □  nie', ''],
    ['Zindywidualizowana ścieżka realizacji wychowania przedszkolnego', '□  tak      □  nie', '']
  ], [4746, 2400, 2600], { nrCol: false, center: [1], rowHeight: 480 }));
add(note('Powiązane dokumenty:', 'jeśli dziecko jest objęte wsparciem, do teczki dołącza się arkusz obserwacji / KPOF, WOPF oraz — zależnie od podstawy — IPET (z orzeczeniem) albo plan wsparcia w ramach pomocy psychologiczno-pedagogicznej (bez orzeczenia). Pełny spis dokumentów — sekcja VIII.'));

add(brk());

/* ====================== VIII. TECZKA ====================== */
add(section('VIII', 'Dokumentacja dziecka — spis zawartości teczki', 'zaznacz, co znajduje się w teczce'));
add(table(['✓', 'Lp.', 'Rodzaj dokumentu', 'Data / nr', 'Uwagi'],
  [
    ['□', '1', 'Karta zgłoszenia / przyjęcia do przedszkola', '', ''],
    ['□', '2', 'Zgody i oświadczenia rodziców', '', ''],
    ['□', '3', 'Klauzula informacyjna RODO', '', ''],
    ['□', '4', 'Orzeczenie o potrzebie kształcenia specjalnego', '', ''],
    ['□', '5', 'Opinia poradni psychologiczno-pedagogicznej', '', ''],
    ['□', '6', 'Arkusz obserwacji pedagogicznej / KPOF', '', ''],
    ['□', '7', 'Analiza gotowości szkolnej', '', ''],
    ['□', '8', 'WOPF — wielospecjalistyczna ocena funkcjonowania', '', ''],
    ['□', '9', 'IPET / plan wsparcia pp', '', ''],
    ['□', '10', 'Karty pomocy psychologiczno-pedagogicznej', '', ''],
    ['□', '11', 'Karta ABC / analizy zachowania', '', ''],
    ['□', '12', 'Korespondencja i notatki ze spotkań z rodzicami', '', '']
  ], [600, 600, 4346, 1800, 2400], { center: [0, 1], rowHeight: 340 }));

add(brk());

/* ====================== IX. SPECJALIŚCI ====================== */
add(section('IX', 'Specjaliści pracujący z dzieckiem', 'zakres i częstotliwość wsparcia'));
add(table(['Specjalista', 'Imię i nazwisko', 'Zakres wsparcia', 'Częstotliwość'],
  [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
  ], [2400, 2546, 3000, 1800], { nrCol: false, rowHeight: 520 }));
add(text('Specjalność wpisujemy funkcją (psycholog, logopeda, terapeuta SI, pedagog specjalny, fizjoterapeuta), a zakres wsparcia — w kategoriach zajęć wynikających z orzeczenia albo z ustaleń zespołu.',
  { size: 14, italic: true, color: C.muted, after: 140 }));

/* ====================== X. ZGODY ====================== */
add(section('X', 'Zgody i oświadczenia rodziców / opiekunów', 'zaznacz właściwe'));
add(table(['Treść zgody', 'Decyzja rodzica'],
  [
    ['Zgoda na przetwarzanie danych osobowych w zakresie niezbędnym do realizacji zadań przedszkola', '□  tak      □  nie'],
    ['Zgoda na wykorzystanie wizerunku dziecka (foto / wideo) na potrzeby przedszkola', '□  tak      □  nie'],
    ['Zgoda na udział w wycieczkach, wyjściach i spacerach', '□  tak      □  nie'],
    ['Zgoda na objęcie pomocą psychologiczno-pedagogiczną', '□  tak      □  nie'],
    ['Zgoda na konsultacje ze specjalistami i poradnią psychologiczno-pedagogiczną', '□  tak      □  nie'],
    ['Zgoda na udzielenie pomocy przedmedycznej w nagłych wypadkach', '□  tak      □  nie']
  ], [7146, 2600], { nrCol: false, center: [1], rowHeight: 420 }));

add(brk());

add(ta('Dodatkowe oświadczenia / uwagi rodziców', { lines: 5 }));
add(signatures(['Miejscowość i data', 'Podpis rodzica / opiekuna prawnego'], 2));

/* ====================== XI. REJESTR KONTAKTÓW ====================== */
add(section('XI', 'Rejestr kontaktów i istotnych ustaleń z rodzicami', 'rozmowy · konsultacje · ustalenia'));
add(table(['Data', 'Osoba / forma kontaktu', 'Temat i ustalenia', 'Podpis'],
  [
    ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''],
    ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']
  ], [1500, 2546, 3900, 1800], { nrCol: false, rowHeight: 420 }));
add(text('Notuj rozmowy, konsultacje i istotne ustalenia dotyczące dziecka — z datą, formą kontaktu (rozmowa, telefon, e-mail, spotkanie zespołu) i podpisem osoby prowadzącej.',
  { size: 14, italic: true, color: C.muted, after: 140 }));

add(brk());

/* ====================== RODO ====================== */
add(section('RODO', 'Klauzula informacyjna', 'art. 13 RODO · dane szczególnej kategorii'));
[
  ['Administrator danych.', 'Administratorem danych osobowych jest przedszkole, do którego uczęszcza dziecko, reprezentowane przez dyrektora.'],
  ['Inspektor ochrony danych (IOD).', 'Kontakt z inspektorem ochrony danych: [adres e-mail / dane kontaktowe IOD].'],
  ['Cel i podstawa prawna.', 'Dane przetwarzane są w celu realizacji zadań dydaktycznych, wychowawczych i opiekuńczych oraz organizacji i udzielania pomocy psychologiczno-pedagogicznej — na podstawie art. 6 ust. 1 lit. c i e oraz art. 9 ust. 2 lit. g RODO w związku z ustawą — Prawo oświatowe (obowiązek prawny administratora).'],
  ['Kategorie danych.', 'Dokument zawiera dane zwykłe oraz dane szczególnej kategorii (dane o zdrowiu i rozwoju dziecka), o których mowa w art. 9 RODO.'],
  ['Odbiorcy danych.', 'Dane mogą być udostępniane wyłącznie podmiotom uprawnionym na podstawie przepisów prawa (m.in. poradnia psychologiczno-pedagogiczna, organ prowadzący, organ nadzoru).'],
  ['Okres przechowywania.', 'Dane przechowywane są przez okres uczęszczania dziecka do przedszkola oraz przez czas wymagany przepisami o archiwizacji dokumentacji przebiegu wychowania przedszkolnego.'],
  ['Prawa osób.', 'Przysługuje prawo dostępu do danych, ich sprostowania i ograniczenia przetwarzania oraz prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych; prawo do usunięcia danych nie przysługuje w zakresie, w jakim przetwarzanie jest niezbędne do wypełnienia obowiązku prawnego (art. 17 ust. 3 lit. b RODO).'],
  ['Bezpieczeństwo.', 'Dokument zawiera dane wrażliwe i jest przechowywany w sposób uniemożliwiający dostęp osobom nieupoważnionym.']
].forEach(([t, b]) => add(L.P([L.run(t + ' ', { size: 15, bold: true, color: C.purple }), L.run(b, { size: 15, color: '3D384C' })], { after: 80, line: 240 })));
add(signatures(['Miejscowość i data', 'Podpis rodzica / opiekuna prawnego — zapoznanie się z klauzulą'], 2));
add(text('Metryczka dziecka · EduPlaner 2026 · PCTP · wzór', { size: 13, italic: true, color: C.muted, align: AlignmentType.CENTER, before: 160, after: 0 }));

module.exports = B;
