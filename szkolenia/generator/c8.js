const G = require('./gen.js');
const { Paragraph, AlignmentType, BorderStyle, t, p, H1, H2, H3, bullet, numItem, spacer,
        pageBreak, box, table, lines, modul, straznik, cw, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));
const BLANK = '';

/* ---- Z7 ---- */
add(pageBreak());
add(H1('Z7', 'Ankieta ewaluacyjna szkolenia'));
add(p('Ankieta anonimowa. Wypełniana na koniec drugiej sesji. Wyniki prowadzący przedstawia radzie na najbliższym posiedzeniu wraz z decyzją, co zmienia w kolejnej edycji.'));
add(spacer(100));
add(table(['Stwierdzenie', '1 zdecydowanie nie', '2', '3', '4', '5 zdecydowanie tak'], [
  ['Wiem, z jakiego przepisu wynika każdy z omawianych dokumentów.', '☐', '☐', '☐', '☐', '☐'],
  ['Rozumiem, czym jest ICF i po co używamy go w dokumentacji.', '☐', '☐', '☐', '☐', '☐'],
  ['Potrafię samodzielnie wypełnić i policzyć arkusz KPOF.', '☐', '☐', '☐', '☐', '☐'],
  ['Wiem, kiedy uruchamiamy obserwację ABC, sensoryczną i ToM.', '☐', '☐', '☐', '☐', '☐'],
  ['Potrafię sformułować cel SMART i wskazać jego źródło w WOPF.', '☐', '☐', '☐', '☐', '☐'],
  ['Wiem, ile razy w roku i kiedy dokonujemy ewaluacji.', '☐', '☐', '☐', '☐', '☐'],
  ['Wiem, co i w jakim terminie przekazujemy poradni.', '☐', '☐', '☐', '☐', '☐'],
  ['Czas szkolenia był dobrze wykorzystany.', '☐', '☐', '☐', '☐', '☐'],
  ['Ćwiczenia były dla mnie użyteczne w codziennej pracy.', '☐', '☐', '☐', '☐', '☐'],
], [3900, 1150, 900, 900, 900, CONTENT - 3900 - 1150 - 900 - 900 - 900], { boldCol0: false }));
add(spacer(120));
add(table(null, [
  ['Co było najbardziej przydatne?', BLANK],
  ['Czego zabrakło?', BLANK],
  ['Jakie zagadnienie wymaga osobnego szkolenia?', BLANK],
], [3600, CONTENT - 3600], { boldCol0: true, zebra: false }));

/* ---- Z8 ---- */
add(pageBreak());
add(H1('Z8', 'Test sprawdzający — 12 pytań'));
add(p('Test krótkiej odpowiedzi, do wykorzystania na zakończenie szkolenia albo jako powtórka po miesiącu. Czas: 15 minut. Klucz odpowiedzi na następnej stronie — prowadzący rozdaje go dopiero po zebraniu prac.'));
add(spacer(100));
const pyt = [
  'Który akt prawny wprowadza nową podstawę programową wychowania przedszkolnego i od kiedy obowiązuje? Czy przewidziano wdrażanie etapowe?',
  'Co zmienia rozporządzenie z 2 marca 2026 r. w zakresie roli przedszkola wobec poradni psychologiczno-pedagogicznej?',
  'W jakim terminie przedszkole sporządza opinię o funkcjonowaniu dziecka i jakie dwa rodzaje treści musi ona obowiązkowo zawierać?',
  'Rozwiń skrót ICF. Na jakie pytanie odpowiada ICF, a na jakie ICD?',
  'Wymień pięć komponentów opisu funkcjonowania w ICF wraz z ich symbolami. Który z nich opisuje bariery i ułatwienia?',
  'Ile twierdzeń liczy arkusz KPOF w wersji A, a ile w wersjach B i C? Który obszar nie wlicza się do wyniku ogólnego i dlaczego?',
  'Jak liczymy średnią obszaru w KPOF? Co robimy z pozycjami oznaczonymi N?',
  'Podaj cztery progi kryterialne KPOF wraz z przypisanymi im poziomami wsparcia.',
  'Na czym polega reguła nadrzędna KPOF? Podaj przykład sytuacji, w której ratuje ona dziecko przed przeoczeniem.',
  'Kiedy uruchamiamy obserwację ToM? Dlaczego niepowodzenie trzylatka w zadaniu fałszywego przekonania nie jest przesłanką diagnostyczną?',
  'Ile razy w roku szkolnym dokonuje się wielospecjalistycznej oceny poziomu funkcjonowania i z czego ten obowiązek wynika?',
  'Wskaż w podanym celu brakujące kryteria SMART: „Dziecko będzie rozwijać samodzielność podczas posiłków w drugim półroczu”.',
];
pyt.forEach((q, i) => {
  add(new Paragraph({ spacing: { before: 130, after: 40 }, alignment: AlignmentType.JUSTIFIED,
    children: [t((i + 1) + '.  ', { bold: true, color: ORANGE }), t(q)] }));
  lines(2, { gap: 150 }).forEach(l => add(l));
});

add(pageBreak());
add(H1('Z8', 'Klucz odpowiedzi — dla prowadzącego'));
add(table(['#', 'Odpowiedź'], [
  ['1', 'Rozporządzenie Ministra Edukacji z dnia 11 marca 2026 r. w sprawie podstawy programowej wychowania przedszkolnego oraz podstawy programowej kształcenia ogólnego dla szkoły podstawowej, w tym dla uczniów z niepełnosprawnością intelektualną w stopniu umiarkowanym lub znacznym (Dz.U. 2026 poz. 378); obowiązuje od 1 września 2026 r. W przedszkolach nie ma wdrażania etapowego — obejmuje wszystkie grupy wiekowe jednocześnie.'],
  ['2', 'Rozporządzenie ME z 2 marca 2026 r. (Dz.U. 2026 poz. 428) czyni ocenę funkcjonalną obowiązkowym etapem procesu diagnostycznego przed wydaniem orzeczenia i nakłada na przedszkole obowiązek sporządzenia oraz przekazania poradni opinii o funkcjonowaniu dziecka jako elementu tej oceny. Formalną ocenę funkcjonalną sporządza zespół w poradni; przedszkole dostarcza dane z obserwacji. Uwaga na daty: rozporządzenie weszło w życie 14 kwietnia 2026 r., a przepisy dotyczące przedszkola — § 7 ust. 6 i 7 oraz § 8 — dopiero 1 września 2026 r.'],
  ['3', '§ 7 ust. 3: „Opinię, o której mowa w ust. 2, wydaje się w terminie 10 dni od dnia otrzymania przez dyrektora prośby o jej wydanie.” Kopię opinii otrzymują rodzice. Obowiązkowo: trudności dziecka ORAZ jego mocne strony i uzdolnienia rozpoznane przez nauczycieli i specjalistów.'],
  ['4', 'ICF — Międzynarodowa Klasyfikacja Funkcjonowania, Niepełnosprawności i Zdrowia (WHO, 2001; wersja dla dzieci i młodzieży: ICF-CY, 2007). ICF odpowiada na pytanie „jak dziecko funkcjonuje w swoim środowisku”; ICD — „co dziecku dolega”.'],
  ['5', 'b — funkcje ciała; s — struktury ciała; d — aktywność i uczestniczenie; e — czynniki środowiskowe; czynniki osobowe (nieklasyfikowane). Bariery i ułatwienia opisuje komponent „e”.'],
  ['6', 'Wersja A (3–4 lata) — 42 twierdzenia; wersje B (5 lat) i C (6 lat) — po 44. Do wyniku ogólnego nie wlicza się obszaru VI (życie domowe), ponieważ ma charakter opisowy, a przedszkole obserwuje go w ograniczonym zakresie.'],
  ['7', 'Średnia obszaru = suma punktów ÷ liczba twierdzeń ocenionych, z pominięciem pozycji oznaczonych N. N nie obniża wyniku — nie wlicza się do średniej. Wynik ogólny to średnia ze średnich obszarów (bez obszaru VI).'],
  ['8', '4,0–5,0 — zasób (mocna strona); 3,0–3,9 — Poziom I (bieżąca praca i monitorowanie); 2,0–2,9 — Poziom II (działania wspierające w przedszkolu i moduł pogłębiający); poniżej 2,0 — Poziom III (moduły pogłębiające, WOPF, konsultacja z poradnią).'],
  ['9', 'Każde pojedyncze twierdzenie ocenione na 1 lub 2 — niezależnie od średniej obszaru — podlega analizie jakościowej zespołu i sprawdzeniu według reguł przekierowania. Przykład: obszar III ze średnią 3,8 (Poziom I) przy jedynce w twierdzeniu o komunikowaniu potrzeb — średnia maskuje trudność, reguła nadrzędna ją ujawnia.'],
  ['10', 'Gdy d7 jest wyraźnie niższe przy zachowanych d1 i d4; przy niskim d7 wraz z trudnością w odczytywaniu komunikatów pozawerbalnych; przy braku zabawy „na niby”; przy dosłowności; przy braku wskazywania protodeklaratywnego i uwagi wspólnej; przy rozważaniu wystąpienia do poradni. Zadania fałszywego przekonania pierwszego rzędu rozwiązywane są typowo od ok. 4.–4,5 roku życia, więc niepowodzenie trzylatka jest zjawiskiem rozwojowo typowym. U młodszych obserwujemy wyłącznie wskaźniki wczesne.'],
  ['11', 'Co najmniej dwa razy w roku szkolnym — rozporządzenie MEN z 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia… (tekst jedn. Dz.U. 2020 poz. 1309). Rekomendacja szkolenia: trzy razy plus dwa krótkie przeglądy wskaźników.'],
  ['12', 'Brakuje S (jakie zachowanie, w jakiej sytuacji — „rozwijać samodzielność” to nie zachowanie), M (brak liczby i poziomu wsparcia), T w części dotyczącej pomiaru (jest okres, brak daty osiągnięcia i daty pomiaru) oraz R (nie wskazano źródła w WOPF). Spełnione jest co najwyżej częściowo A — czego bez znajomości poziomu wyjściowego nie da się ocenić.'],
], [500, CONTENT - 500], { boldCol0: true }));

/* ---- ŹRÓDŁA ---- */
add(pageBreak());
add(H1('▌', 'Podstawy prawne i źródła — nota metodyczna'));
add(p([t('Stan prawny na dzień opracowania scenariusza. ', { bold: true }), t('Przed każdą edycją szkolenia prowadzący sprawdza aktualność publikatorów w Internetowym Systemie Aktów Prawnych (isap.sejm.gov.pl), a w szczególności — czy do aktów z 2026 r. nie ogłoszono zmian lub tekstów jednolitych.')]));
add(spacer(100));
add(H3('Akty prawne'));
add(bullet('Rozporządzenie Ministra Edukacji z dnia 11 marca 2026 r. w sprawie podstawy programowej wychowania przedszkolnego oraz podstawy programowej kształcenia ogólnego dla szkoły podstawowej, w tym dla uczniów z niepełnosprawnością intelektualną w stopniu umiarkowanym lub znacznym — Dz.U. 2026 poz. 378 (ogł. 20.03.2026; obowiązuje od 01.09.2026).'));
add(bullet('Rozporządzenie Ministra Edukacji z dnia 2 marca 2026 r. w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające działające w publicznych poradniach psychologiczno-pedagogicznych — Dz.U. 2026 poz. 428 (ogł. 30.03.2026; weszło w życie 14.04.2026, a § 7 ust. 6 i 7 oraz § 8 — 01.09.2026).'));
add(bullet('Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej w publicznych przedszkolach, szkołach i placówkach — Dz.U. 2017 poz. 1591; tekst jedn. Dz.U. 2023 poz. 1798.'));
add(bullet('Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym — Dz.U. 2017 poz. 1578; tekst jedn. Dz.U. 2020 poz. 1309.'));
add(bullet('Rozporządzenie Ministra Edukacji Narodowej z dnia 25 sierpnia 2017 r. w sprawie sposobu prowadzenia przez publiczne przedszkola, szkoły i placówki dokumentacji przebiegu nauczania, działalności wychowawczej i opiekuńczej oraz rodzajów tej dokumentacji — Dz.U. 2017 poz. 1646; tekst jedn. Dz.U. 2024 poz. 50.'));
add(bullet('Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO) — Dz.Urz. UE L 119 z 04.05.2016, CELEX 32016R0679.'));
add(bullet('Ustawa z dnia 14 grudnia 2016 r. — Prawo oświatowe; tekst jedn. Dz.U. 2026 poz. 820 (obwieszczenie Marszałka Sejmu z 12 czerwca 2026 r., ogł. 22.06.2026).'));
add(bullet('WYJĄTEK HISTORYCZNY (reguła L4) — akty przywołane wyłącznie w tabeli porównawczej modułu M1, dla zobrazowania stanu sprzed reformy: rozporządzenie MEN z dnia 14 lutego 2017 r., zał. nr 1 (Dz.U. 2017 poz. 356) — utraciło moc z dniem 31.08.2026, a jego zakres rozdzielono na Dz.U. 2026 poz. 378 oraz Dz.U. 2026 poz. 1012; rozporządzenie MEN z dnia 7 września 2017 r. (Dz.U. 2017 poz. 1743 ze zm.) — zastąpione przez Dz.U. 2026 poz. 428. Żaden z tych aktów nie jest w scenariuszu podstawą jakiegokolwiek obowiązku placówki.'));

add(spacer(120));
add(H3('Podstawy merytoryczne'));
add(bullet('World Health Organization, International Classification of Functioning, Disability and Health (ICF), Genewa 2001; International Classification of Functioning, Disability and Health: Children and Youth Version (ICF-CY), Genewa 2007.'));
add(bullet('Kwestionariusz Przedszkolnej Oceny Funkcjonalnej (KPOF), wersje A (3–4 lata), B (5 lat), C (6 lat) — narzędzie autorskie, kryterialne, EduPlaner 2026 / PCTP. Opracowane na podstawie nowej podstawy programowej wychowania przedszkolnego i klasyfikacji ICF.'));
add(bullet('Metryczka dziecka — karta danych dziecka, EduPlaner 2026 / PCTP, rok szkolny 2026/2027.'));

add(spacer(140));
add(box('CZEGO STRAŻNIK PRAWA NIE SPRAWDZIŁ — GRANICA ODPOWIEDZIALNOŚCI', [
  p([t('Publikatory, statusy, daty wejścia w życie i relacje tekstów jednolitych w tym scenariuszu zostały zweryfikowane według reguł L1–L6. Strażnik prawa ')  , t('nie sprawdza jednak zgodności merytorycznej', { bold: true }), t(' — tego, czy dany paragraf mówi to, co twierdzi druk. Ta warstwa należy do odrębnej kontroli.')]),
  p([t('Pozostaje do rozstrzygnięcia merytorycznego: ', { bold: true }), t('brzmienie § 7 ust. 2 i 3 rozporządzenia Dz.U. 2026 poz. 428 (prośba przewodniczącego zespołu orzekającego, opinia o funkcjonowaniu dziecka, termin 10 dni od dnia otrzymania prośby przez dyrektora) przytoczono za tekstem ogłoszonym w Dzienniku Ustaw. Zakres treści opinii od 1 września 2026 r. (§ 7 ust. 6 i 7 — ujęcie według ICF) oraz § 8 opisano na podstawie opracowań branżowych. Przed powołaniem się na konkretną jednostkę redakcyjną w dokumencie dziecka należy sprawdzić tekst w ISAP.')]),
  p([t('Poza zakresem także: ', { bold: true }), t('podstawa prawna przetwarzania danych w metryczce, którą wybiera placówka jako administrator, oraz aktualny wzór informacji o gotowości dziecka do podjęcia nauki w szkole podstawowej — do zweryfikowania w przepisach o świadectwach i drukach szkolnych obowiązujących na dany rok szkolny.')]),
], { fill: LIGHTO, bar: ORANGE }));

add(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300 },
  border: { top: { style: BorderStyle.SINGLE, size: 8, color: ORANGE, space: 10 } },
  children: [t('EduPlaner 2026  ·  PCTP  ·  scenariusz szkolenia rady pedagogicznej  ·  rok szkolny 2026/2027',
    { size: 16, color: '6B6B6B' })] }));

module.exports = C;
