const L = require('../lib.js');
const { section, partBanner, howto, legal, note, ta, fields, checks, table, signatures,
        brk, text, subhead, C, AlignmentType } = L;

const B = [];
const add = (...xs) => xs.forEach(x => Array.isArray(x) ? B.push(...x) : B.push(x));

/* ====================== XVI. DOSTOSOWANIE WYMAGAŃ ====================== */
add(section('XVI', 'Zakres i sposób dostosowania wymagań edukacyjnych', 'projektowanie uniwersalne (UDL) · § 6 ust. 1 pkt 1'));
add(subhead('Metody i formy pracy'));
add(checks([
  'Wydłużony czas pracy', 'Instrukcje krokowe',
  'Dostosowanie progów ocen', 'Alternatywne formy sprawdzania wiedzy',
  'Indywidualizacja tempa pracy', 'Praca na konkretach i materiałach poglądowych',
  'Miejsce w pierwszej ławce', 'Krótsze zestawy zadań'
], 2));
add(subhead('Środowisko i technologie'));
add(checks([
  'Text-to-Speech / Speech-to-Text', 'Systemy wizualne / AAC',
  'Strefa wyciszenia / słuchawki wygłuszające', 'Ograniczenie dystraktorów',
  'Plany aktywności i piktogramy', 'Dostosowanie stanowiska pracy',
  'Materiały w wersji dostępnej (powiększenie, kontrast, audio)', 'Dostęp do komputera na lekcji'
], 2));
add(ta('Dostosowania z podziałem na przedmioty — komentarz zespołu', { lines: 6, hint: 'Podpowiedź: dostosowania obowiązują na wszystkich przedmiotach; wymagania edukacyjne pozostają zgodne z podstawą programową, zmienia się sposób ich realizacji i sprawdzania. Język polski: wydłużony czas prac pisemnych, odpowiedź ustna zamiast pisemnej, ocena treści bez obniżania za stronę graficzną. Matematyka: materiał konkretny, wzory dostępne w czasie pracy, krótsze zestawy. Języki obce: przewaga formy ustnej. Wychowanie fizyczne i przedmioty artystyczne: ocena wysiłku i zaangażowania. Szczegółowy wykaz — w załączniku.' }));
add(legal('IPET określa „zakres i sposób dostosowania (…) wymagań edukacyjnych (…) do indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych ucznia, w szczególności przez zastosowanie odpowiednich metod i form pracy z uczniem” — § 6 ust. 1 pkt 1 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.). Dostosowanie wymagań — art. 44b ust. 8 pkt 1 ustawy o systemie oświaty oraz rozporządzenie w sprawie podstawy programowej kształcenia ogólnego (zalecane warunki i sposób realizacji).'));

add(brk());

/* ====================== XVII. WARUNKI ORGANIZACJI ====================== */
add(section('XVII', 'Dostosowanie warunków organizacji kształcenia', 'technologie wspomagające · § 6 ust. 1 pkt 7'));
add(checks([
  'Dostosowanie sali i miejsca pracy (oświetlenie, akustyka)', 'Sprzęt specjalistyczny (laptop, tablet, system FM, pętla indukcyjna)',
  'Technologie wspomagające (TTS / STT, oprogramowanie specjalistyczne)', 'Materiały w wersji dostępnej (powiększenie, kontrast, wersja audio)',
  'Dostosowanie planu lekcji i organizacji dnia', 'Likwidacja barier architektonicznych'
], 2));
add(ta('Inne dostosowania warunków — opis i termin wprowadzenia', { lines: 6, hint: 'Podpowiedź: stałe miejsce w pierwszej ławce, z dala od drzwi i okna — od początku roku szkolnego. Słuchawki wygłuszające w czasie pracy samodzielnej — od października. Dostęp do kącika wyciszenia i zgoda na krótką przerwę regulacyjną — od początku roku. Sprawdziany pisane w mniejszej grupie — od II okresu. Wpisz odpowiedzialnego za wprowadzenie każdego dostosowania.' }));
add(legal('IPET określa „rodzaj i sposób dostosowania warunków organizacji kształcenia do rodzaju niepełnosprawności ucznia, w tym w zakresie wykorzystywania technologii wspomagających to kształcenie” — § 6 ust. 1 pkt 7 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.).'));

add(brk());

/* ====================== XVIII. ZAJĘCIA REWALIDACYJNE ====================== */
add(section('XVIII', 'Zajęcia rewalidacyjne', '§ 6 ust. 1 pkt 5 i § 6 ust. 2 · minimum 2 godziny tygodniowo'));
add(table(['✓', 'Rodzaj zajęć', 'H / tydz.', 'Okres', 'Realizator'],
  [
    ['□', 'Trening umiejętności społecznych (TUS)', '', '', 'psycholog'],
    ['□', 'Trening umiejętności emocjonalnych (TUE)', '', '', 'psycholog / pedagog'],
    ['□', 'Trening umiejętności komunikacyjnych (TUK)', '', '', 'logopeda / pedagog'],
    ['□', 'Trening funkcjonowania codziennego (TFC)', '', '', 'oligofrenopedagog'],
    ['□', 'Trening orientacji przestrzennej i poruszania się', '', '', 'tyflopedagog'],
    ['□', 'Rozwijanie komunikowania się (AAC)', '', '', 'logopeda'],
    ['□', 'Trening rozwoju sensorycznego (SI)', '', '', 'terapeuta SI'],
    ['□', 'Trening rozwoju funkcji poznawczych', '', '', 'pedagog specjalny'],
    ['□', 'Gimnastyka korekcyjna', '', '', 'nauczyciel wychowania fizycznego'],
    ['□', 'Logopedia rewalidacyjna', '', '', 'logopeda'],
    ['□', 'Terapia ręki', '', '', 'terapeuta pedagogiczny'],
    ['□', 'Zajęcia resocjalizacyjne / socjoterapeutyczne', '', '', 'socjoterapeuta']
  ], [600, 4046, 1200, 1600, 2300], { center: [0, 2, 3], rowHeight: 360 }));
add(legal('„W ramach zajęć rewalidacyjnych w programie należy uwzględnić w szczególności rozwijanie umiejętności komunikacyjnych przez: 1) naukę orientacji przestrzennej i poruszania się oraz naukę systemu Braille’a lub innych alternatywnych metod komunikacji — w przypadku ucznia niewidomego; 2) naukę języka migowego lub innych sposobów komunikowania się, w szczególności wspomagających i alternatywnych metod komunikacji (AAC) — w przypadku ucznia niepełnosprawnego z zaburzeniami mowy lub jej brakiem; 3) zajęcia rozwijające umiejętności społeczne, w tym umiejętności komunikacyjne — w przypadku ucznia z autyzmem, w tym z zespołem Aspergera” — § 6 ust. 2 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.). Minimalny tygodniowy wymiar zajęć rewalidacyjnych — po 2 godziny na ucznia — wynika z rozporządzenia w sprawie ramowych planów nauczania.'));

add(brk());

/* ====================== XIX. POMOC PP ====================== */
add(section('XIX', 'Formy pomocy psychologiczno-pedagogicznej', '§ 6 ust. 1 pkt 3 · jednostka 45 minut'));
add(table(['✓', 'Rodzaj zajęć', 'H / tydz.', 'Okres', 'Realizator'],
  [
    ['□', 'Zajęcia korekcyjno-kompensacyjne', '', '', 'terapeuta pedagogiczny'],
    ['□', 'Zajęcia logopedyczne', '', '', 'logopeda'],
    ['□', 'Rozwijające kompetencje emocjonalno-społeczne', '', '', 'pedagog / psycholog'],
    ['□', 'Zajęcia dydaktyczno-wyrównawcze', '', '', 'nauczyciel przedmiotu'],
    ['□', 'Zajęcia rozwijające umiejętności uczenia się', '', '', 'nauczyciel / specjalista'],
    ['□', 'Zajęcia rozwijające uzdolnienia', '', '', 'nauczyciel / specjalista'],
    ['□', 'Zajęcia związane z wyborem kierunku kształcenia i zawodu', '', '', 'doradca zawodowy'],
    ['□', 'Zindywidualizowana ścieżka kształcenia', '', '', 'nauczyciel / specjalista'],
    ['□', 'Terapia pedagogiczna', '', '', 'terapeuta pedagogiczny'],
    ['□', 'Porady, konsultacje i warsztaty dla rodziców', '', '', 'specjaliści']
  ], [600, 4046, 1200, 1600, 2300], { center: [0, 2, 3], rowHeight: 380 }));
add(legal('„Pomoc psychologiczno-pedagogiczna w przedszkolu, szkole i placówce jest udzielana w trakcie bieżącej pracy z uczniem oraz przez zintegrowane działania nauczycieli i specjalistów, a także w formie: zajęć rozwijających uzdolnienia; zajęć rozwijających umiejętności uczenia się; zajęć dydaktyczno-wyrównawczych; zajęć specjalistycznych: korekcyjno-kompensacyjnych, logopedycznych, rozwijających kompetencje emocjonalno-społeczne oraz innych zajęć o charakterze terapeutycznym; zajęć związanych z wyborem kierunku kształcenia i zawodu; zindywidualizowanej ścieżki kształcenia; porad i konsultacji; warsztatów” — § 6 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1591, z późn. zm.). Godzina zajęć trwa 45 minut. Doradztwo zawodowe i zajęcia dydaktyczno-wyrównawcze ujęto wyłącznie w tej sekcji, aby nie figurowały równolegle w dwóch miejscach programu.'));

add(brk());

/* ====================== XX. WSPARCIE OSOBOWE ====================== */
add(section('XX', 'Wsparcie osobowe i jego uzasadnienie', '§ 6 ust. 1 pkt 8'));
add(fields([
  { label: 'Nauczyciel współorganizujący kształcenie', value: '', hint: 'tak / nie' },
  { label: 'Pomoc nauczyciela — asystent ucznia', value: '', hint: 'tak / nie' },
  { label: 'Wymiar wsparcia (h / tydz.)', value: '' },
  { label: 'Poziom wsparcia uzasadniający wniosek', value: '', hint: 'I / II / III' }
], 2));
add(howto('Uzasadnienie musi wskazywać zakres, w jakim uczeń nie może realizować zajęć samodzielnie — konkretnie, przez odniesienie do sytuacji szkolnych i kodów ICF, a nie przez ogólne stwierdzenie o potrzebie wsparcia. Dla każdej wskazanej bariery podaj, co dzieje się bez wsparcia i co zmienia jego obecność.'));
add(table(['Kod ICF', 'Bariera bezpieczeństwa', 'Bariera edukacyjna', 'Bariera w relacjach'],
  [
    ['e330', '', '', ''],
    ['d160 / d240', '', '', ''],
    ['d250 / d570', '', '', ''],
    ['d310 / d330', '', '', '']
  ], [1746, 2666, 2667, 2667], { center: [0], rowHeight: 800 }));
add(legal('W programie określa się „w przypadku ucznia, o którym mowa w § 7 ust. 2 i 3 — rodzaj i sposób (…) wsparcia tego ucznia przez dodatkowo zatrudnionych nauczycieli, specjalistów lub pomoc nauczyciela” wraz ze szczegółowym uzasadnieniem ze wskazaniem zakresu, w jakim uczeń nie może realizować zajęć samodzielnie — § 6 ust. 1 pkt 8 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.). Decyzję o dodatkowym zatrudnieniu podejmuje dyrektor za zgodą organu prowadzącego — art. 165 ust. 4 ustawy Prawo oświatowe.'));

add(brk());

/* ====================== XXI. RODZICE ====================== */
add(section('XXI', 'Współpraca z rodzicami i działania wspierające rodzinę', '§ 6 ust. 1 pkt 4 i pkt 6'));
add(checks([
  'Konsultacje i porady ze specjalistami', 'Instruktaż do pracy i utrwalania w domu',
  'Warsztaty i szkolenia (pedagogizacja rodziców)', 'Wsparcie w kontakcie z poradnią i instytucjami',
  'Pomoc w rozumieniu orzeczenia i dokumentacji', 'Wsparcie emocjonalne i informacyjne',
  'Udział w spotkaniach zespołu i współtworzeniu programu', 'Ujednolicenie strategii i systemu nagród szkoła–dom'
], 2));
add(table(['Obszar współpracy', 'Planowane działania', 'Częstotliwość', 'Odpowiedzialny'],
  [
    ['Działania wspierające rodziców', '', '', ''],
    ['Współpraca z poradnią psychologiczno-pedagogiczną', '', '', ''],
    ['Współpraca z placówką doskonalenia nauczycieli / SCWEW', '', '', ''],
    ['Współpraca z organizacjami pozarządowymi i służbą zdrowia', '', '', ''],
    ['Współpraca z organem prowadzącym (JST)', '', '', '']
  ], [3146, 3400, 1600, 1600], { nrCol: false, rowHeight: 560 }));
add(legal('IPET określa „działania wspierające rodziców ucznia oraz — w zależności od potrzeb — zakres współdziałania z poradniami psychologiczno-pedagogicznymi, placówkami doskonalenia nauczycieli, organizacjami pozarządowymi oraz innymi instytucjami i podmiotami działającymi na rzecz rodziny, dzieci i młodzieży” (§ 6 ust. 1 pkt 4) oraz „zakres współpracy nauczycieli i specjalistów z rodzicami ucznia w realizacji zadań” (§ 6 ust. 1 pkt 6) — rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.). Rodzice mają prawo uczestniczyć w opracowaniu i modyfikacji programu oraz w dokonywaniu ocen (§ 6 ust. 11), o terminie każdego spotkania zespołu zawiadamia ich dyrektor (§ 6 ust. 12), a kopię WOPFU i IPET otrzymują na wniosek (§ 6 ust. 13).'));

add(brk());

/* ====================== XXII. WSPÓŁPRACA MIĘDZYSEKTOROWA ====================== */
add(section('XXII', 'Plan współpracy międzysektorowej', 'nowy model 26/27 · kto co realizuje'));
add(subhead('Szkoła / placówka — zaznacz przyjęte zadania'));
add(checks([
  'Realizacja programu i dostosowań na wszystkich zajęciach', 'Zajęcia rewalidacyjne i pomoc psychologiczno-pedagogiczna',
  'Monitorowanie postępów i prowadzenie dokumentacji', 'Spójne reagowanie na zachowania trudne',
  'Współpraca nauczycieli i specjalistów', 'Informowanie rodziców o postępach'
], 2));
add(subhead('Rodzina — zaznacz przyjęte zadania'));
add(checks([
  'Udział w pracach zespołu i współtworzeniu programu', 'Utrwalanie umiejętności w domu',
  'Stały kontakt z wychowawcą i koordynatorem', 'Ujednolicenie strategii i systemu nagród',
  'Zgody i wymiana informacji', 'Udział w konsultacjach ze specjalistami'
], 2));
add(subhead('Uczeń — zaznacz przyjęte zadania'));
add(checks([
  'Udział w wyznaczaniu celów (wywiad — autorefleksja)', 'Korzystanie z dostosowań i strategii',
  'Samoocena postępów', 'Udział w zajęciach specjalistycznych',
  'Rozwijanie mocnych stron i zainteresowań', 'Informowanie o potrzebie przerwy'
], 2));

add(brk());

add(subhead('Podmioty zewnętrzne — zaznacz przyjęte zadania'));
add(checks([
  'Konsultacje z poradnią psychologiczno-pedagogiczną', 'Współpraca ze SCWEW i placówką doskonalenia nauczycieli',
  'Wsparcie organizacji pozarządowych', 'Współpraca ze służbą zdrowia',
  'Działania organu prowadzącego (JST)', 'Inne — jakie?'
], 2));
add(ta('Ustalenia dodatkowe i osoby kontaktowe', { lines: 5, hint: 'Podpowiedź: osobą koordynującą kontakty z podmiotami zewnętrznymi jest koordynator zespołu (funkcja wpisana w sekcji I). Wymiana informacji z poradnią i placówką terapeutyczną odbywa się wyłącznie za pisemną zgodą rodziców i w zakresie niezbędnym do realizacji programu. Ustal wspólny termin przeglądu ustaleń. Kontakty zapisujemy funkcją i instytucją, bez danych prywatnych.' }));
add(note('Uzasadnienie sekcji.', 'Plan współpracy międzysektorowej nie jest wymagany rozporządzeniem — porządkuje odpowiedzialność za realizację programu poza szkołą i zapobiega sytuacji, w której zalecenie z orzeczenia nie ma przypisanego wykonawcy.'));

add(brk());

/* ====================== CZĘŚĆ III + XXIII ====================== */
add(partBanner('Część III · decyzja', 'Zespół, zatwierdzenie programu i ocena efektywności',
  'skład zespołu · zgoda rodziców · ewaluacja okresowa · załączniki'));
add(section('XXIII', 'Skład zespołu opracowującego program', '§ 6 ust. 3–6'));
add(table(['Lp.', 'Funkcja w zespole', 'Imię i nazwisko', 'Zakres działań', 'Podpis'],
  [
    ['1', 'Koordynator zespołu', '', '', ''],
    ['2', 'Wychowawca oddziału', '', '', ''],
    ['3', 'Pedagog specjalny', '', '', ''],
    ['4', 'Psycholog', '', '', ''],
    ['5', 'Logopeda', '', '', ''],
    ['6', 'Nauczyciel przedmiotu', '', '', ''],
    ['7', 'Inny specjalista', '', '', ''],
    ['8', 'Inna funkcja', '', '', '']
  ], [600, 2546, 2200, 2400, 2000], { center: [0], rowHeight: 520 }));
add(note('Zmiany w składzie zespołu.', 'Zmiany w składzie zespołu w trakcie roku szkolnego odnotowuje się w odrębnym rejestrze — druk „Zespół 7 — rejestr zmian składu”.'));
add(legal('Program opracowuje zespół tworzony przez nauczycieli i specjalistów prowadzących zajęcia z uczniem. Pracę zespołu koordynuje wychowawca oddziału albo inny nauczyciel lub specjalista wyznaczony przez dyrektora. Program opracowuje się w terminie do 30 września roku, w którym uczeń rozpoczyna kształcenie, albo w terminie 30 dni od dnia złożenia w szkole orzeczenia o potrzebie kształcenia specjalnego — § 6 ust. 3–6 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.).'));

add(brk());

/* ====================== XXIV. ZATWIERDZENIE ====================== */
add(section('XXIV', 'Zatwierdzenie programu i odbiór kopii przez rodziców', '§ 6 ust. 11–13'));
add(note('Oświadczenie rodzica / opiekuna prawnego.', 'Potwierdzam udział w spotkaniach zespołu oraz odbiór kopii niniejszego programu wraz z arkuszem wielospecjalistycznej oceny poziomu funkcjonowania. Zostałam / zostałem poinformowana / poinformowany o celach programu, formach wsparcia oraz o prawie wglądu w dokumentację.', '2D1B69'));
add(signatures(['Miejscowość i data', 'Podpis rodzica / opiekuna prawnego'], 2));
add(signatures(['Koordynator zespołu — podpis i data', 'Dyrektor szkoły — zatwierdzenie programu'], 2));

add(brk());

/* ====================== XXV. EFEKTYWNOŚĆ ====================== */
add(section('XXV', 'Okresowa wielospecjalistyczna ocena efektywności', '§ 6 ust. 9 · co najmniej dwa razy w roku szkolnym'));
add(table(['Termin oceny', 'Data', 'Efektywność programu', 'Wnioski i rekomendacje'],
  [
    ['Ocena śródroczna', '', 'w pełni / częściowo / brak', ''],
    ['Ocena końcoworoczna', '', 'w pełni / częściowo / brak', '']
  ], [2200, 1600, 2546, 3400], { nrCol: false, rowHeight: 900 }));
add(ta('Zakres modyfikacji programu wynikający z oceny efektywności', { lines: 6, hint: 'Podpowiedź: po ocenie śródrocznej zespół utrzymuje cele w sferach, w których uczeń osiągnął kryterium, i modyfikuje te, w których postęp jest mniejszy niż zakładany: obniża próg trudności pierwszego etapu, zwiększa udział wsparcia wizualnego, wydłuża czas realizacji celu. Zmiany dotyczą sposobu pracy, nie zakresu podstawy programowej. Modyfikację odnotowujemy z datą, uzasadnieniem i podpisami zespołu; rodzice otrzymują informację o zmianie i kopię zmodyfikowanego programu.' }));
add(legal('„Zespół co najmniej dwa razy w roku szkolnym dokonuje okresowej wielospecjalistycznej oceny poziomu funkcjonowania ucznia, uwzględniając ocenę efektywności programu w zakresie, o którym mowa w ust. 1, oraz, w miarę potrzeb, dokonuje modyfikacji programu” — § 6 ust. 9 rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.).'));

add(brk());

/* ====================== XXVI. ZAŁĄCZNIKI ====================== */
add(section('XXVI', 'Załączniki do programu', 'dołącza się to, co zaznaczono w sekcjach XVIII i XIX'));
add(table(['Lp.', 'Rodzaj załącznika', 'Numer / data', 'Dołączono'],
  [
    ['1', 'Arkusz oceny funkcjonalnej KSzOF', '', '□  tak    □  nie'],
    ['2', 'Harmonogram i zakres ewaluacji', '', '□  tak    □  nie'],
    ['3', 'Dostosowania z podziałem na przedmioty', '', '□  tak    □  nie'],
    ['4', 'Szczegółowy plan pracy z rodzicami', '', '□  tak    □  nie'],
    ['5', 'Protokół z posiedzenia zespołu (rekomendacja poziomu wsparcia)', '', '□  tak    □  nie'],
    ['6', 'Programy zajęć rewalidacyjnych — wg zaznaczeń w sekcji XVIII', '', '□  tak    □  nie'],
    ['7', 'Programy zajęć pomocy pp — wg zaznaczeń w sekcji XIX', '', '□  tak    □  nie'],
    ['8', 'Karta obserwacji ABC / FBA', '', '□  tak    □  nie'],
    ['9', '', '', '□  tak    □  nie'],
    ['10', '', '', '□  tak    □  nie']
  ], [600, 5146, 2000, 2000], { center: [0, 3], rowHeight: 380 }));
add(note('Zasada doboru załączników.', 'Programy zajęć nie są wyliczane po jednym wierszu na każdy możliwy rodzaj terapii — dołącza się wyłącznie programy tych zajęć, które zespół zaznaczył w sekcjach XVIII i XIX. Dwa ostatnie wiersze pozostają puste na załączniki własne.'));

add(brk());

/* ====================== XXVII. KARTA KONTROLNA ====================== */
add(section('XXVII', 'Karta kontrolna zgodności programu', 'rozliczenie wymogów § 6 rozporządzenia'));
add(howto('Przed zatwierdzeniem programu zespół sprawdza i odhacza każdy wymóg § 6 rozporządzenia. Wiersze opisane jako „model” to elementy oceny funkcjonalnej — wykraczają ponad minimum prawne i nie podlegają kontroli organu nadzoru.'));
add(table(['Podstawa', 'Wymagany element programu', 'Gdzie w dokumencie', 'Ujęte'],
  [
    ['§ 6 ust. 1 pkt 1', 'Zakres i sposób dostosowania wymagań edukacyjnych', 'sekcja XVI', '□'],
    ['§ 6 ust. 1 pkt 2', 'Zintegrowane działania nauczycieli i specjalistów', 'sekcje X–XV', '□'],
    ['§ 6 ust. 1 pkt 3', 'Formy i okres pomocy pp oraz wymiar godzin', 'sekcja XIX', '□'],
    ['§ 6 ust. 1 pkt 4', 'Działania wspierające rodziców i współdziałanie z instytucjami', 'sekcje XXI–XXII', '□'],
    ['§ 6 ust. 1 pkt 5', 'Zajęcia rewalidacyjne, resocjalizacyjne, socjoterapeutyczne', 'sekcja XVIII', '□'],
    ['§ 6 ust. 1 pkt 6', 'Zakres współpracy nauczycieli i specjalistów z rodzicami', 'sekcja XXI', '□'],
    ['§ 6 ust. 1 pkt 7', 'Dostosowanie warunków organizacji i technologie wspomagające', 'sekcja XVII', '□'],
    ['§ 6 ust. 1 pkt 8', 'Wsparcie kadrowe ze szczegółowym uzasadnieniem', 'sekcja XX', '□'],
    ['§ 6 ust. 2', 'Autyzm / zespół Aspergera — umiejętności społeczne i komunikacyjne', 'sekcja XVIII', '□'],
    ['§ 6 ust. 5–6', 'Termin opracowania programu', 'sekcja XXIII', '□'],
    ['§ 6 ust. 9', 'WOPFU i ocena efektywności co najmniej dwa razy w roku', 'część I i sekcja XXV', '□'],
    ['§ 6 ust. 11–13', 'Prawa rodziców: udział, zawiadomienie, kopia dokumentów', 'sekcja XXIV', '□'],
    ['model', 'Wywiad z uczniem — autorefleksja i udział ucznia', 'sekcja II', '□'],
    ['model', 'Ocena funkcjonalna KSzOF / ICF i poziomy wsparcia I–III', 'sekcje VII–VIII', '□'],
    ['model', 'Projektowanie uniwersalne (UDL) w dostosowaniach', 'sekcja XVI', '□'],
    ['model', 'Plan współpracy międzysektorowej', 'sekcja XXII', '□']
  ], [1800, 4646, 2200, 1100], { nrCol: false, center: [3], rowHeight: 320 }));

add(brk());

/* ====================== XXVIII. BRAKI ====================== */
add(section('XXVIII', 'Podsumowanie weryfikacji — braki i terminy', 'co trzeba uzupełnić i do kiedy'));
add(table(['Lp.', 'Stwierdzony brak lub element do uzupełnienia', 'Termin', 'Odpowiedzialny', 'Status'],
  [
    ['1', '', '', '', ''],
    ['2', '', '', '', ''],
    ['3', '', '', '', ''],
    ['4', '', '', '', '']
  ], [600, 4146, 1600, 2000, 1400], { center: [0, 2, 4], rowHeight: 700 }));
add(legal('Terminy ustawowe — przypomnienie. Program: do 30 września albo 30 dni od złożenia orzeczenia (§ 6 ust. 5–6). Wielospecjalistyczna ocena i ocena efektywności: co najmniej dwa razy w roku szkolnym (§ 6 ust. 9). Zawiadomienie rodziców o każdym spotkaniu zespołu — przed spotkaniem (§ 6 ust. 12). Kopia WOPFU i IPET dla rodziców na wniosek (§ 6 ust. 13) — rozp. MEN z 9.08.2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.).'));
add(signatures(['Data weryfikacji', 'Podpis koordynatora zespołu'], 2));

add(brk());

/* ====================== XXIX. RODO ====================== */
add(section('XXIX', 'Klauzula informacyjna RODO', 'dokument zawiera dane szczególnej kategorii'));
[
  ['Administrator danych.', 'Administratorem danych osobowych jest szkoła lub placówka, do której uczęszcza uczeń, reprezentowana przez dyrektora. Kontakt z inspektorem ochrony danych — adres wskazany w klauzuli informacyjnej szkoły.'],
  ['Cel i podstawa prawna.', 'Dane przetwarzane są w celu realizacji zadań dydaktycznych, wychowawczych i opiekuńczych oraz organizacji kształcenia specjalnego i pomocy psychologiczno-pedagogicznej — na podstawie art. 6 ust. 1 lit. c i e oraz art. 9 ust. 2 lit. g RODO w związku z ustawą Prawo oświatowe i ustawą o systemie oświaty (obowiązek prawny administratora).'],
  ['Kategorie danych i odbiorcy.', 'Dokument zawiera dane szczególnej kategorii — dane o zdrowiu oraz treść orzeczenia (art. 9 RODO). Dane udostępnia się wyłącznie podmiotom uprawnionym na podstawie przepisów prawa: poradni psychologiczno-pedagogicznej, organowi prowadzącemu i organowi nadzoru pedagogicznego.'],
  ['Okres przechowywania i prawa osób.', 'Dane przechowuje się przez okres nauki ucznia oraz przez czas wymagany przepisami o archiwizacji dokumentacji przebiegu nauczania. Przysługuje prawo dostępu do danych, ich sprostowania i ograniczenia przetwarzania oraz prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych. Prawo do usunięcia danych nie przysługuje w zakresie, w jakim przetwarzanie jest niezbędne do wypełnienia obowiązku prawnego — art. 17 ust. 3 lit. b RODO.'],
  ['Bezpieczeństwo.', 'Dokument zawiera dane wrażliwe i przechowywany jest w sposób uniemożliwiający dostęp osobom nieupoważnionym. Kopie wydaje się wyłącznie rodzicom lub opiekunom prawnym ucznia.']
].forEach(([t, b]) => add(L.P([L.run(t + ' ', { size: 15, bold: true, color: C.purple }), L.run(b, { size: 15, color: '3D384C' })], { after: 80, line: 240 })));
add(fields([
  { label: 'Imię i nazwisko lub nazwa podmiotu pełniącego funkcję IOD', value: '', hint: 'wpisz zgodnie z klauzulą informacyjną szkoły' },
  { label: 'Adres e-mail lub adres korespondencyjny do kontaktu z IOD', value: '', hint: 'np. iod@szkola.edu.pl' }
], 2));
add(subhead('Potwierdzenie zapoznania się z klauzulą — zaznacz'));
add(checks([
  'Zapoznałam / zapoznałem się z klauzulą informacyjną', 'Otrzymałam / otrzymałem kopię IPET',
  'Znam zakres danych zawartych w dokumencie', 'Wiem, komu dokument może zostać udostępniony',
  'Znam przysługujące mi prawa wobec administratora', 'Znam zasady przechowywania dokumentacji ucznia'
], 2));

add(brk());

add(note('Zasada minimalizacji.', 'Metryczka tego druku nie zawiera numeru PESEL, adresu zamieszkania, miejsca urodzenia, obywatelstwa, numeru w ewidencji ani danych zakładu pracy rodziców — dane te pozostają wyłącznie w dokumentacji przebiegu nauczania prowadzonej przez szkołę.'));
add(ta('Uwagi rodzica / opiekuna prawnego do sposobu przetwarzania danych', { lines: 5, hint: 'Przykład: Proszę o przekazywanie kopii dokumentacji wyłącznie do rąk własnych oraz o wcześniejsze informowanie mnie o każdym przekazaniu dokumentu poza szkołę. Proszę też o kontakt drogą elektroniczną w sprawach dotyczących realizacji programu. Jeżeli rodzic nie zgłasza uwag, wpisz: brak uwag.' }));
add(signatures(['Miejscowość i data', 'Podpis rodzica / opiekuna prawnego'], 2));
add(legal('Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony osób fizycznych w związku z przetwarzaniem danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (ogólne rozporządzenie o ochronie danych) — art. 5, art. 6, art. 9, art. 13 i art. 17.'));
add(text('EduPlaner 2026 · PCTP · Indywidualny Program Edukacyjno-Terapeutyczny z WOPFU (ICF) — druk szkolny · wersja Word',
  { size: 13, italic: true, color: C.muted, align: AlignmentType.CENTER, before: 200, after: 0 }));

module.exports = B;
