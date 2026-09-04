// Skrypt dla nauczycieli: transkrypcja filmu + podstawy prawne + sposób przygotowania dokumentów.
// Uruchom: node skrypt_nauczyciela.js → ../../film/Skrypt_dla_nauczycieli.docx
const G = require('./gen.js');
const { Document, Packer, Paragraph, AlignmentType, BorderStyle, Header, Footer, PageNumber, LevelFormat,
        fs, t, p, H2, H3, bullet, numItem, spacer, pageBreak, box, table, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO, FONT } = G;
const { TextRun } = require('docx');

const NARR = __dirname + '/../../film/narracja/';
const akapity = (plik) => fs.readFileSync(NARR + plik, 'utf8').trim().split(/\n\s*\n/).map(s => s.replace(/\s+/g, ' ').trim());

const banner = (nr, tytul, czas, plik) => p([
  t('  ' + nr + '  ', { bold: true, size: 20, color: ORANGE }),
  t('   ' + tytul, { bold: true, size: 26, color: PURPLE }),
  t('   ·   ' + czas + '  ·  ' + plik, { bold: true, size: 20, color: ORANGE }),
], { before: 120, after: 120, align: AlignmentType.LEFT, fill: LIGHT });

const transkrypcja = (plik) => {
  const out = [H2('Transkrypcja narracji')];
  akapity(plik).forEach((a, i) => {
    out.push(p([t(String(i + 1).padStart(2, '0') + '   ', { bold: true, size: 16, color: ORANGE }), t(a)],
      { before: 70, after: 70 }));
  });
  return out;
};

const kroki = (tytul, lista) => [H2(tytul), ...lista.map(x => numItem(x))];

const CZ = [];

/* ======================= strona tytułowa ======================= */
CZ.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400, after: 80 },
  children: [t('EDUPLANER 2026 · PCTP · SZKOLENIE RADY PEDAGOGICZNEJ', { bold: true, size: 18, color: ORANGE, sp: 30 })] }));
CZ.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60, line: 520 },
  children: [t('Skrypt dla nauczycieli', { bold: true, size: 40, color: PURPLE })] }));
CZ.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200, line: 400 },
  children: [t('Transkrypcja filmu · podstawy prawne · sposób przygotowania dokumentów', { size: 24, color: PURPLE })] }));
CZ.push(new Paragraph({ alignment: AlignmentType.CENTER,
  border: { top: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 8 } },
  spacing: { before: 80, after: 200 },
  children: [t('Dokumentacja przedszkolna · rok szkolny 2026/2027 · sześć części · 53 minuty 57 sekund', { size: 18, color: '4A4A4A' })] }));
CZ.push(box('JAK KORZYSTAĆ ZE SKRYPTU', [
  p([t('Skrypt odpowiada dokładnie temu, co słychać w filmie. ', { bold: true }), t('Każda część ma trzy warstwy: podstawę prawną (żeby wiedzieć, z czego wynika obowiązek), pełną transkrypcję narracji (żeby wrócić do zdania, które umknęło) oraz instrukcję przygotowania dokumentu krok po kroku (żeby usiąść i zrobić). Numery akapitów transkrypcji odpowiadają kolejnym planszom w filmie.')]),
  p([t('Skrypt można drukować w całości albo częściami — każda część zaczyna się od nowej strony.', { size: 18 })]),
], { fill: LIGHTO, bar: ORANGE }));
CZ.push(spacer(160));
CZ.push(H2('Spis części'));
CZ.push(table(['Część', 'Tytuł', 'Czas'], [
  ['Część 1', 'Podstawa prawna — co obowiązuje od 1 września 2026 r.', '9:30'],
  ['Część 2', 'Obieg dokumentów — jak jeden wynika z drugiego', '5:36'],
  ['Część 3', 'Metryczka dziecka — pierwszy dokument września', '5:45'],
  ['Część 4', 'KPOF — budowa narzędzia, skala, liczenie wyniku, odczyt profilu', '10:08'],
  ['Część 5', 'Obserwacja pogłębiona — ABC, profil sensoryczny, teoria umysłu, karta mowy', '9:46'],
  ['Część 6', 'WOPF, IPET, cele SMART, ewaluacja i opinia dla poradni', '13:12'],
], [1200, CONTENT - 1200 - 1000, 1000], { boldCol0: true }));

/* ======================= część 1 ======================= */
CZ.push(pageBreak());
CZ.push(banner('CZĘŚĆ 1', 'Podstawa prawna — co obowiązuje od 1 września 2026 r.', '9:30', 'M1.mp4'));
CZ.push(box('PODSTAWA PRAWNA CZĘŚCI', [
  bullet('Podstawa programowa wychowania przedszkolnego — rozporządzenie ME z 11 marca 2026 r. (Dz.U. 2026 poz. 378), obowiązuje od 1.09.2026.'),
  bullet('Orzeczenia i opinie zespołów orzekających — rozporządzenie ME z 2 marca 2026 r. (Dz.U. 2026 poz. 428); § 7 ust. 6–7 i § 8 od 1.09.2026; § 7 ust. 3 — opinia w terminie 10 dni od dnia otrzymania prośby przez dyrektora.'),
  bullet('Pomoc psychologiczno-pedagogiczna — rozporządzenie MEN z 9 sierpnia 2017 r., tekst jedn. Dz.U. 2023 poz. 1798.'),
  bullet('Kształcenie specjalne (WOPF, IPET) — rozporządzenie MEN z 9 sierpnia 2017 r., tekst jedn. Dz.U. 2020 poz. 1309.'),
  bullet('Dokumentacja przebiegu nauczania — rozporządzenie MEN z 25 sierpnia 2017 r., tekst jedn. Dz.U. 2024 poz. 50.'),
  bullet('Prawo oświatowe — ustawa z 14 grudnia 2016 r., tekst jedn. Dz.U. 2026 poz. 820; RODO — rozporządzenie (UE) 2016/679.'),
], { fill: LIGHT, bar: PURPLE }));
CZ.push(...transkrypcja('M1_prawo.txt'));
CZ.push(...kroki('Jak przygotować placówkę do zmian — krok po kroku', [
  'Zrób przegląd wzorów druków używanych w przedszkolu. Sprawdź w każdym, czy w podstawie prawnej stoi obowiązujący tekst jednolity, a nie pierwotny publikator.',
  'Przemapuj narzędzia obserwacji i programy z czterech obszarów rozwoju na dziewięć obszarów nowej podstawy programowej. Kwestionariusz KPOF ma ten układ wbudowany.',
  'Wpisz do kalendarza placówki wrześniową obserwację wszystkich dzieci. To ona daje dane, gdy poradnia poprosi o opinię z terminem dziesięciu dni.',
  'Ustal, kto pełni funkcję Strażnika Prawa i w jakim rytmie funkcja się zmienia. Zadanie jest jedno: przy każdej decyzji pytać, z czego to wynika i gdzie jest zapisane.',
  'Przygotuj zarządzenie dyrektora porządkujące obieg dokumentacji dziecka: kto zakłada teczkę, gdzie jest przechowywana, kto ma do niej dostęp.',
  'Nie przepisuj dokumentów już sporządzonych. Program i ocenę aktualizuj przy najbliższej wielospecjalistycznej ocenie; dotychczasowe zapisy zostają w teczce jako historia wsparcia.',
]));

/* ======================= część 2 ======================= */
CZ.push(pageBreak());
CZ.push(banner('CZĘŚĆ 2', 'Obieg dokumentów — jak jeden wynika z drugiego', '5:36', 'M2.mp4'));
CZ.push(box('PODSTAWA PRAWNA CZĘŚCI', [
  bullet('Kształcenie specjalne — § 6 rozporządzenia MEN z 9 sierpnia 2017 r. (t.j. Dz.U. 2020 poz. 1309): WOPF poprzedza IPET i jest jego podstawą; ocena co najmniej dwa razy w roku szkolnym.'),
  bullet('Pomoc psychologiczno-pedagogiczna — rozpoznawanie potrzeb, formy pomocy i ocena efektywności (t.j. Dz.U. 2023 poz. 1798).'),
  bullet('Opinia o funkcjonowaniu dziecka dla poradni — § 7 ust. 2–3 rozporządzenia o orzekaniu (Dz.U. 2026 poz. 428).'),
], { fill: LIGHT, bar: PURPLE }));
CZ.push(...transkrypcja('M2_mapa.txt'));
CZ.push(...kroki('Jak ustawić obieg dokumentów w przedszkolu', [
  'Załóż teczkę dziecka i umieść w niej metryczkę jako pierwszy dokument. To ona odpowiada na pytania: kogo wezwać, co podać, od kiedy liczyć termin.',
  'We wrześniu wypełnij kwestionariusz KPOF dla wszystkich dzieci w grupie. Wynik wskazuje obszary, a nie diagnozę.',
  'Uruchom obserwację pogłębioną tylko wtedy, gdy zadziała reguła przekierowania. Wybór narzędzia zapisz w karcie decyzyjnej.',
  'Zbierz dane w wielospecjalistycznej ocenie poziomu funkcjonowania. Każdy blok oceny ma mieć źródło w dokumencie, który już powstał.',
  'Opracuj IPET wprost z oceny: zalecenia z orzeczenia i z oceny, przy każdym zapis realizacji — forma, kto, wymiar.',
  'Zaplanuj ewaluację w kalendarzu roku i po każdym pomiarze podejmij jedną z czterech decyzji: zamykamy cel, kontynuujemy, modyfikujemy metodę albo występujemy do poradni.',
]));

/* ======================= część 3 ======================= */
CZ.push(pageBreak());
CZ.push(banner('CZĘŚĆ 3', 'Metryczka dziecka — pierwszy dokument września', '5:45', 'M3.mp4'));
CZ.push(box('PODSTAWA PRAWNA CZĘŚCI', [
  bullet('Dokumentacja przebiegu wychowania przedszkolnego — rozporządzenie MEN z 25 sierpnia 2017 r. (t.j. Dz.U. 2024 poz. 50): księga dzieci, dzienniki, dokumentacja badań i czynności uzupełniających.'),
  bullet('Metryczka jest narzędziem wewnętrznym placówki — wprowadza ją zarządzenie dyrektora; porządkuje dane gromadzone z innych tytułów.'),
  bullet('RODO — art. 5 ust. 1 lit. c (minimalizacja danych) i art. 9 (dane o zdrowiu jako dane szczególnej kategorii).'),
], { fill: LIGHT, bar: PURPLE }));
CZ.push(...transkrypcja('M3_metryczka.txt'));
CZ.push(...kroki('Jak przygotować metryczkę — krok po kroku', [
  'Sekcja I. Wpisz imię i nazwisko, datę i miejsce urodzenia oraz adres — z dokumentów rekrutacyjnych. Numeru PESEL nie powielamy; jest w księdze dzieci. Przepisz numer w księdze dzieci z ewidencji.',
  'Sekcja II. Uzupełnij grupę, datę przyjęcia, godziny pobytu i posiłki. Zaznacz, czy dziecko realizuje roczne obowiązkowe przygotowanie przedszkolne — od tego zależy informacja o gotowości szkolnej w kwietniu.',
  'Sekcje III–V. Wypełnij razem z rodzicami: dane kontaktowe i preferowaną formę kontaktu, listę osób upoważnionych do odbioru oraz kolejność powiadamiania w nagłych wypadkach.',
  'Sekcja VI. Zaznacz występujące pozycje i opisz szczegóły: choroby przewlekłe (np. astma, cukrzyca), przyjmowane leki, dietę i ostrzeżenia. W polu zaleceń zapisz konkretnie: kto podaje lek, na jakiej podstawie, gdzie lek jest przechowywany i kogo powiadamiamy w jakiej kolejności.',
  'Sekcja VII. Przy każdej formie wsparcia wpisz numer i datę dokumentu, a przy orzeczeniu także podstawę jego wydania (rodzaj niepełnosprawności lub schorzenie). Data uruchamia trzydziestodniowy termin na program.',
  'Sekcja XI. Notuj każdą rozmowę i ustalenie z rodzicami: data, forma kontaktu, temat, ustalenia, podpis. Ten rejestr zasili później opinię dla poradni.',
  'Aktualizuj metryczkę przy każdej zmianie zgłoszonej przez rodzica — z datą. Przechowuj ją w miejscu wskazanym zarządzeniem dyrektora.',
]));
CZ.push(spacer(120));
CZ.push(H3('Czego pilnujemy w metryczce'));
CZ.push(table(['Element', 'Co wpisujemy', 'Skąd bierzemy dane'], [
  ['Dane osobowe', 'imię i nazwisko, data i miejsce urodzenia, adres, numer w księdze dzieci', 'dokumenty rekrutacyjne, ewidencja przedszkola'],
  ['PESEL', 'nie wpisujemy — dane są w księdze dzieci', 'zasada minimalizacji danych'],
  ['Rodzice i odbiór', 'kontakty, forma kontaktu, osoby upoważnione, kolejność powiadamiania', 'oświadczenia rodziców, wyłącznie na piśmie'],
  ['Zdrowie', 'choroby przewlekłe, leki, dieta, ostrzeżenia, procedura postępowania', 'zaświadczenia lekarskie, zgody rodziców'],
  ['Wsparcie', 'numer i data orzeczenia lub opinii, podstawa wydania orzeczenia, data objęcia pomocą', 'orzeczenie, opinia, decyzja dyrektora'],
  ['Rejestr kontaktów', 'data, forma, temat, ustalenia, podpis', 'bieżące notatki nauczyciela'],
], [1800, 4000, CONTENT - 1800 - 4000], { boldCol0: true }));

/* ======================= część 4 ======================= */
CZ.push(pageBreak());
CZ.push(banner('CZĘŚĆ 4', 'KPOF — budowa narzędzia, skala, liczenie wyniku, odczyt profilu', '10:08', 'M4.mp4'));
CZ.push(box('PODSTAWA PRAWNA CZĘŚCI', [
  bullet('Rozpoznawanie potrzeb dziecka przez nauczycieli — rozporządzenie o pomocy psychologiczno-pedagogicznej (t.j. Dz.U. 2023 poz. 1798).'),
  bullet('Obserwacja pedagogiczna i analiza gotowości szkolnej — rozporządzenie o dokumentacji (t.j. Dz.U. 2024 poz. 50) jako dokumentacja badań i czynności uzupełniających.'),
  bullet('Podstawa programowa wychowania przedszkolnego — Dz.U. 2026 poz. 378: dziewięć obszarów osiągnięć dziecka; każde twierdzenie kwestionariusza odsyła do punktu podstawy.'),
  bullet('ICF (WHO 2001) — model biopsychospołeczny; rozporządzenie o orzekaniu (Dz.U. 2026 poz. 428) nakazuje opisywać funkcjonowanie w kategoriach aktywności i uczestniczenia.'),
], { fill: LIGHT, bar: PURPLE }));
CZ.push(...transkrypcja('M4_kpof.txt'));
CZ.push(...kroki('Jak przygotować i policzyć kwestionariusz — krok po kroku', [
  'Wybierz wersję arkusza odpowiednią do wieku dziecka: A dla 3–4 lat, B dla 5 lat, C dla 6 lat.',
  'Wypełnij metryczkę arkusza: dziecko, grupa, okres obserwacji, osoba wypełniająca. Kwestionariusz wypełniają niezależnie obie nauczycielki grupy.',
  'Obserwuj w naturalnych sytuacjach przez ustalony okres, zanim zaznaczysz odpowiedzi. Oceniaj zachowanie, nie wrażenie.',
  'Zaznacz jedną wartość skali przy każdym twierdzeniu. Odpowiedź N — nie obserwowano — jest pełnoprawna i nie obniża wyniku.',
  'Policz średnią obszaru: suma punktów podzielona przez liczbę ocenionych twierdzeń, z pominięciem N.',
  'Odczytaj wynik przez progi kryterialne i zastosuj regułę nadrzędną: każde twierdzenie ocenione na 1 lub 2 podlega osobnej analizie, niezależnie od średniej.',
  'Nanieś wyniki na profil dziewięciu obszarów. Kolor zielony to zasób, żółty — obserwuj, czerwony — działaj.',
  'Powtórz kwestionariusz w maju. Trzylatki badaj we wrześniu, bo dla dziecka z orzeczeniem IPET musi powstać do 30 września.',
]));

/* ======================= część 5 ======================= */
CZ.push(pageBreak());
CZ.push(banner('CZĘŚĆ 5', 'Obserwacja pogłębiona — ABC, profil sensoryczny, teoria umysłu, karta mowy', '9:46', 'M5.mp4'));
CZ.push(box('PODSTAWA PRAWNA CZĘŚCI', [
  bullet('Rozpoznawanie indywidualnych potrzeb i możliwości psychofizycznych dziecka oraz ocena efektywności udzielanej pomocy — rozporządzenie o pomocy psychologiczno-pedagogicznej (t.j. Dz.U. 2023 poz. 1798).'),
  bullet('Wystąpienie do poradni, gdy mimo udzielanej pomocy nie ma poprawy — za zgodą rodziców, wniosek dyrektora.'),
  bullet('Reguły przekierowania i karta decyzyjna nie wynikają wprost z przepisu — to decyzja rady pedagogicznej wpisana do procedury placówki.'),
], { fill: LIGHT, bar: PURPLE }));
CZ.push(...transkrypcja('M5_obserwacja.txt'));
CZ.push(...kroki('Jak przeprowadzić obserwację pogłębioną — krok po kroku', [
  'Sprawdź reguły przekierowania. Wystarczy jedna spełniona, żeby uruchomić moduł pogłębiony.',
  'Załóż kartę decyzyjną — jedną na jedno dziecko. Zapisz w niej, która reguła zadziałała i jakie narzędzie wybieramy.',
  'Model ABC stosuj wtedy, gdy pytanie brzmi: dlaczego to zachowanie się powtarza. Notuj trzy kolumny: co było przed, zachowanie, co nastąpiło po.',
  'Profil sensoryczny stosuj, gdy dziecko reaguje nadmiernie albo zbyt słabo na bodźce. Opisz wzorzec i wskaż konsekwencję dla organizacji sali.',
  'Obserwację teorii umysłu prowadź, gdy trudność dotyczy rozumienia intencji i przekonań innych. To nie jest test i nie prowadzi do rozpoznania.',
  'Kartę obserwacji rozwoju mowy uruchom, gdy dziecko nie rozumie poleceń albo nie buduje wypowiedzi. Brak rozumienia bywa przyczyną trudności, które wyglądają na nieposłuszeństwo.',
  'Zapisz wniosek: co obserwowaliśmy, jak często, w jakich sytuacjach i co z tego wynika dla wsparcia. Wnioski przechodzą do wielospecjalistycznej oceny.',
]));

/* ======================= część 6 ======================= */
CZ.push(pageBreak());
CZ.push(banner('CZĘŚĆ 6', 'WOPF, IPET, cele SMART, ewaluacja i opinia dla poradni', '13:12', 'M6.mp4'));
CZ.push(box('PODSTAWA PRAWNA CZĘŚCI', [
  bullet('WOPF i IPET — § 6 rozporządzenia MEN z 9 sierpnia 2017 r. (t.j. Dz.U. 2020 poz. 1309): ust. 1 pkt 1–8 (zawartość programu), ust. 4 (program po ocenie, z uwzględnieniem zaleceń z orzeczenia), ust. 9–11 (ocena co najmniej dwa razy w roku, prawa rodziców).'),
  bullet('Terminy IPET: do 30 września dla dziecka rozpoczynającego kształcenie z orzeczeniem albo 30 dni od złożenia orzeczenia w przedszkolu.'),
  bullet('Opinia o funkcjonowaniu dziecka — § 7 ust. 2–3 rozporządzenia o orzekaniu (Dz.U. 2026 poz. 428): wydaje się w terminie 10 dni od dnia otrzymania przez dyrektora prośby o jej wydanie; kopię otrzymują rodzice.'),
  bullet('Cele SMART nie są nazwane w rozporządzeniu. Wymagana jest ocena efektywności, a cel z kryterium jest najprostszym sposobem, żeby ją przeprowadzić.'),
], { fill: LIGHT, bar: PURPLE }));
CZ.push(...transkrypcja('M6_wopf_ipet.txt'));
CZ.push(...kroki('Jak przygotować wielospecjalistyczną ocenę (WOPF)', [
  'Zwołaj zespół: nauczyciel grupy, psycholog, logopeda, pedagog specjalny, terapeuta. Dyrektor zawiadamia rodziców o terminie spotkania.',
  'Wypełnij dane dziecka i skład zespołu, zaznacz rodzaj oceny: pierwsza przed IPET, śródroczna albo roczna.',
  'Wpisz wyniki diagnozy funkcjonalnej w dziewięciu obszarach ICF: punkty z kwestionariusza, sten i wynikający z niego poziom wsparcia.',
  'Opisz mocne strony i potrzeby, a potem trudności — z częstotliwością i kontekstem, nie w formie etykiety.',
  'Zaznacz czynniki środowiskowe i opisz bariery oraz ułatwienia. To one uzasadniają dostosowania w programie.',
  'Zamknij ocenę wnioskami. Każde zalecenie przechodzi do IPET jako wiersz „zalecenie z WOPF → realizacja”.',
  'Przekaż rodzicom kopię oceny.',
]));
CZ.push(...kroki('Jak przygotować IPET', [
  'Sprawdź termin: do 30 września albo 30 dni od złożenia orzeczenia w przedszkolu.',
  'Przepisz zalecenia z orzeczenia poradni, jedno po drugim, a przy każdym zapisz sposób realizacji: forma, kto prowadzi, wymiar godzin, od kiedy.',
  'Zrób to samo z zaleceniami z wielospecjalistycznej oceny. Orzeczenie mówi, co dziecku zalecono; ocena mówi, co widzimy w przedszkolu.',
  'Opisz zakres i sposób dostosowania: sposób podania treści, czas, przestrzeń, sposób sprawdzania umiejętności, pomoce. Każde dostosowanie ma źródło w barierze opisanej w ocenie.',
  'Zapisz zintegrowane działania nauczycieli i specjalistów: jeden cel, jeden plan, wiele rąk — z rolą rodziców w domu.',
  'Sformułuj cele w postaci mierzalnej: dziecko, w konkretnej sytuacji, wykona obserwowalne zachowanie, w określonej liczbie prób, przy określonym wsparciu, do określonej daty, z określonym sposobem pomiaru.',
  'Zaplanuj ewaluację i wpisz ją do kalendarza. Rodzice otrzymują kopię programu.',
]));
CZ.push(...kroki('Jak przygotować opinię o funkcjonowaniu dziecka dla poradni', [
  'Zanotuj datę otrzymania prośby przez dyrektora — od niej liczy się dziesięć dni.',
  'Zbierz dane, które już masz: metryczka, kwestionariusz, obserwacja pogłębiona, karty ewaluacji, rejestr kontaktów z rodzicami.',
  'Napisz siedem punktów: dane formalne, mocne strony i uzdolnienia, funkcjonowanie w obszarach, trudności z częstotliwością i kontekstem, bariery i ułatwienia, udzielone wsparcie i jego efekty, współpraca z rodzicami.',
  'Punkt o mocnych stronach napisz jako pierwszy i co najmniej tak samo obszernie jak punkt o trudnościach.',
  'Używaj języka funkcjonalnego: co dziecko robi, w jakich warunkach, przy jakim wsparciu, jak często. Rozpoznania i hipotezy diagnostyczne zostaw poradni.',
  'Informacje od rodziców i specjalistów spoza przedszkola oznacz jako relację ze wskazaniem źródła.',
  'Przekaż kopię opinii rodzicom i odnotuj to w dokumentacji.',
]));

/* ======================= kalendarz ======================= */
CZ.push(pageBreak());
CZ.push(banner('DODATEK', 'Kalendarz dokumentacji na rok szkolny', '', ''));
CZ.push(table(['Miesiąc', 'Co robimy', 'Dokument'], [
  ['sierpień / wrzesień', 'Zakładamy teczkę dziecka, uzupełniamy metryczkę, zbieramy zgody rodziców.', 'Metryczka dziecka'],
  ['wrzesień', 'Kwestionariusz KPOF dla wszystkich dzieci; trzylatki obowiązkowo.', 'KPOF (wersja A, B albo C)'],
  ['do 30 września', 'IPET dla dziecka rozpoczynającego kształcenie z orzeczeniem; pierwsza wielospecjalistyczna ocena.', 'WOPF + IPET'],
  ['wrzesień / październik', 'Obserwacja pogłębiona tam, gdzie zadziałała reguła przekierowania.', 'Karta decyzyjna + wybrane narzędzie'],
  ['listopad', 'Krótki przegląd wskaźników — piętnaście minut na dziecko, notatka w dzienniku.', 'Karta celu SMART'],
  ['styczeń', 'Druga wielospecjalistyczna ocena; ewaluacja półroczna celów; ocena efektywności pomocy.', 'WOPF + IPET + karta ewaluacji'],
  ['marzec', 'Krótki przegląd wskaźników.', 'Karta celu SMART'],
  ['do końca kwietnia', 'Informacja o gotowości szkolnej dla dzieci realizujących roczne przygotowanie.', 'Informacja o gotowości szkolnej'],
  ['maj', 'Kwestionariusz KPOF po raz drugi; trzecia, zalecana ocena wielospecjalistyczna.', 'KPOF + WOPF'],
  ['czerwiec', 'Ocena efektywności udzielanej pomocy na zakończenie form.', 'Karta ewaluacji'],
  ['cały rok', 'Opinia dla poradni na prośbę przewodniczącego zespołu orzekającego — w terminie 10 dni.', 'Opinia o funkcjonowaniu dziecka'],
], [2000, CONTENT - 2000 - 2600, 2600], { boldCol0: true }));
CZ.push(spacer(140));
CZ.push(box('JĘZYK FUNKCJONALNY — CZTERY PYTANIA DO KAŻDEGO ZDANIA', [
  bullet('Co dziecko robi? — zachowanie, które można zobaczyć, a nie cecha.'),
  bullet('W jakich warunkach? — sytuacja, pora dnia, wielkość grupy, poziom hałasu.'),
  bullet('Przy jakim wsparciu? — samodzielnie, po podpowiedzi słownej, po pokazie, z pomocą dorosłego.'),
  bullet('Jak często? — liczba prób, dni w tygodniu, epizody w obserwowanym okresie.'),
], { fill: LIGHTO, bar: ORANGE }));

/* ======================= zapis ======================= */
const naglowekTxt = 'Skrypt dla nauczycieli — transkrypcja, podstawy prawne, przygotowanie dokumentów';
const header = new Header({ children: [new Paragraph({ spacing: { after: 60 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [t('PCTP · EduPlaner 2026', { size: 15, color: ORANGE, bold: true }), t('     ' + naglowekTxt, { size: 15, color: '8A8A8A' })] })] });
const footer = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [new TextRun({ font: FONT, size: 15, color: '8A8A8A', children: ['Strona ', PageNumber.CURRENT, ' z ', PageNumber.TOTAL_PAGES, ' · skrypt dla nauczycieli'] })] })] });

const doc = new Document({
  creator: 'EduPlaner 2026 · PCTP', title: naglowekTxt,
  styles: { default: { document: { run: { font: FONT, size: 20, color: '1A1A1A' }, paragraph: { spacing: { line: 264 } } } } },
  numbering: { config: [
    { reference: 'kropki', levels: [{ level: 0, format: LevelFormat.BULLET, text: '▪', alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 340, hanging: 220 } }, run: { color: ORANGE, font: FONT, size: 18 } } }] },
    { reference: 'kroki', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 380, hanging: 380 } }, run: { color: ORANGE, font: FONT, bold: true } } }] },
  ] },
  sections: [{ properties: { page: { margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } },
    headers: { default: header }, footers: { default: footer }, children: CZ }],
});

Packer.toBuffer(doc).then(b => {
  const plik = __dirname + '/../../film/Skrypt_dla_nauczycieli.docx';
  fs.writeFileSync(plik, b);
  console.log('OK ->', plik, (b.length / 1024).toFixed(0) + ' KB');
});
