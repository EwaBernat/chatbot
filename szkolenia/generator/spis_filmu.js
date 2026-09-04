// Spis części filmu szkoleniowego: tytuł, zakres, czas.
// Uruchom: node spis_filmu.js → ../../film/Spis_czesci_filmu.docx
const G = require('./gen.js');
const { Document, Packer, Paragraph, AlignmentType, BorderStyle, Header, Footer, PageNumber, LevelFormat,
        fs, t, p, H2, H3, bullet, spacer, box, table, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO, FONT } = G;
const { TextRun } = require('docx');

const CZESCI = [
  { nr: 'Część 1', czas: '9:30', plik: 'M1.mp4',
    tytul: 'Podstawa prawna — co obowiązuje od 1 września 2026 r.',
    zakres: [
      'Czy placówka, która ma już szczegółową dokumentację, musi ją zmieniać — odpowiedź i trzy powody zmian; zestawienie „robimy / nie robimy”.',
      'Nowa podstawa programowa wychowania przedszkolnego (Dz.U. 2026 poz. 378) — dziewięć obszarów zamiast czterech.',
      'Rozporządzenie o orzeczeniach i opiniach (Dz.U. 2026 poz. 428) — ocena funkcjonalna, opinia o funkcjonowaniu dziecka, cytat § 7 ust. 3: dziesięć dni od otrzymania prośby przez dyrektora.',
      'Pomoc psychologiczno-pedagogiczna (t.j. Dz.U. 2023 poz. 1798) i kształcenie specjalne — WOPF i IPET (t.j. Dz.U. 2020 poz. 1309).',
      'Dokumentacja przebiegu wychowania (t.j. Dz.U. 2024 poz. 50), Prawo oświatowe i RODO; metryczka jako narzędzie wewnętrzne.',
      'Rola Strażnika Prawa: z czego to wynika i gdzie to jest zapisane.',
    ],
    druki: '—' },
  { nr: 'Część 2', czas: '5:36', plik: 'M2.mp4',
    tytul: 'Obieg dokumentów — jak jeden wynika z drugiego',
    zakres: [
      'Sześć przystanków obiegu: metryczka → KPOF → obserwacja pogłębiona → wielospecjalistyczna ocena → IPET → ewaluacja.',
      'Co każdy dokument przekazuje dalej i na jakie pytanie odpowiada (gdzie? dlaczego? co z tego wynika?).',
      'Opinia o funkcjonowaniu dziecka dla poradni — dokument obok obiegu, zasilany danymi, które już mamy.',
      'Cztery decyzje zespołu po każdym pomiarze.',
    ],
    druki: '—' },
  { nr: 'Część 3', czas: '5:45', plik: 'M3.mp4',
    tytul: 'Metryczka dziecka — pierwszy dokument września',
    zakres: [
      'Pięć powodów, dla których prowadzimy metryczkę; metryczka jako dokument operacyjny.',
      'Wypełnianie druku krok po kroku: sekcja I dane osobowe (bez numeru PESEL), II organizacja pobytu i roczne przygotowanie przedszkolne.',
      'Sekcja III rodzice i preferowana forma kontaktu; sekcje IV–V odbiór dziecka i kolejność powiadamiania.',
      'Sekcja VI zdrowie: choroby przewlekłe, leki, procedura postępowania — kto podaje, na jakiej podstawie, gdzie przechowujemy, kogo powiadamiamy.',
      'Sekcja VII objęcie wsparciem: numer i data dokumentu oraz podstawa wydania orzeczenia; sekcja XI rejestr kontaktów z rodzicami.',
      'Trzy dobre praktyki: minimalizacja danych, aktualizacja z datą, bezpieczne przechowywanie.',
    ],
    druki: 'Metryczka dziecka — druk 7-stronicowy (animacja wypełniania)' },
  { nr: 'Część 4', czas: '10:08', plik: 'M4.mp4',
    tytul: 'KPOF — budowa narzędzia, skala, liczenie wyniku, odczyt profilu',
    zakres: [
      'Czym jest ICF i model biopsychospołeczny; profil biopsychospołeczny dziecka i co ICF zmienia w obserwacji.',
      'Czym kwestionariusz jest, a czym nie jest; trzy wersje arkusza dla 3–4, 5 i 6 lat.',
      'Skala sześciu wartości i odpowiedź N jako pełnoprawna; siedem zasad rzetelnej obserwacji.',
      'Liczenie średniej obszaru, progi kryterialne i reguła nadrzędna dla ocen 1 i 2.',
      'Odczyt profilu dziewięciu obszarów — kolory zielony, żółty i czerwony.',
      'Kalendarz: wrzesień i maj; trzylatki badamy we wrześniu, bo IPET powstaje do 30 września.',
    ],
    druki: 'KPOF wersja A (3–4 lata) — metryczka, skala, obszary, podsumowanie wyniku' },
  { nr: 'Część 5', czas: '9:46', plik: 'M5.mp4',
    tytul: 'Obserwacja pogłębiona — ABC, profil sensoryczny, teoria umysłu, karta mowy',
    zakres: [
      'Przesiew a obserwacja pogłębiona — czym się różnią i kiedy przechodzimy dalej.',
      'Sześć reguł przekierowania — wystarczy jedna, żeby uruchomić moduł pogłębiony.',
      'Narzędzie 1 — model ABC: trzy kolumny, przykład zapisu, zasady prowadzenia.',
      'Narzędzie 2 — profil sensoryczny: siedem układów, trzy wzorce, język zapisu.',
      'Narzędzie 3 — obserwacja teorii umysłu: kiedy jest potrzebna i czym nie jest.',
      'Narzędzie 4 — karta obserwacji rozwoju mowy: pięć obszarów, dwadzieścia pięć wskaźników; problemy w komunikacji jako przyczyna trudności.',
      'Karta decyzyjna: jedna na jedno dziecko, z organizacją obserwacji.',
    ],
    druki: 'Karta obserwacji rozwoju mowy; karta decyzyjna modułu pogłębionego (Z4)' },
  { nr: 'Część 6', czas: '13:12', plik: 'M6.mp4',
    tytul: 'WOPF, IPET, cele SMART, ewaluacja i opinia dla poradni',
    zakres: [
      'Wielospecjalistyczna ocena: po co ją prowadzimy, siedem bloków i źródło każdego z nich.',
      'Druk WOPF w wersji przedszkolnej: dane dziecka i zespół, diagnoza funkcjonalna w dziewięciu obszarach ICF, czynniki środowiskowe — bariery i ułatwienia.',
      'IPET: terminy (30 września albo 30 dni od złożenia orzeczenia), prawa rodziców, zawartość programu wg § 6.',
      'Zalecenia z orzeczenia i z oceny wielospecjalistycznej wraz z zapisem realizacji: forma, kto, wymiar.',
      'Dostosowania w przedszkolu — zmieniamy jak, nie czego; zintegrowane działania nauczycieli i specjalistów; sala pod nową podstawę programową.',
      'Cele SMART: czy przepis ich wymaga, pięć liter, formuła celu i dwa przykłady z pomiarem.',
      'Ewaluacja: kalendarz roku i cztery decyzje zespołu po każdym pomiarze.',
      'Opinia o funkcjonowaniu dziecka dla poradni: dziesięć dni, siedem punktów, język funkcjonalny i sprawdzalny.',
    ],
    druki: 'WOPF przedszkolny; IPET (zalecenia z orzeczenia, dostosowania, zintegrowane działania); karta celu SMART (Z5); wzór opinii dla poradni' },
];

const K = [];
K.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 160, after: 80 },
  children: [t('EDUPLANER 2026 · PCTP · SZKOLENIE RADY PEDAGOGICZNEJ', { bold: true, size: 18, color: ORANGE, sp: 30 })] }));
K.push(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60, line: 480 },
  children: [t('Film szkoleniowy — spis części', { bold: true, size: 34, color: PURPLE })] }));
K.push(new Paragraph({ alignment: AlignmentType.CENTER,
  border: { top: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 8 } },
  spacing: { before: 80, after: 160 },
  children: [t('Dokumentacja przedszkolna w roku szkolnym 2026/2027 · sześć części · łącznie 53 minuty 57 sekund · narracja: mgr Mirosława Ewa Jurczyszyn', { size: 17, color: '4A4A4A' })] }));

K.push(H2('Zestawienie'));
K.push(table(['Część', 'Tytuł', 'Czas', 'Plik'],
  CZESCI.map(c => [c.nr, c.tytul, c.czas, c.plik]),
  [1100, CONTENT - 1100 - 1000 - 1300, 1000, 1300], { boldCol0: true }));
K.push(spacer(80));
K.push(box('ŁĄCZNY CZAS', [
  p([t('53 minuty 57 sekund. ', { bold: true }), t('Film jest podzielony na sześć niezależnych części — można je odtwarzać osobno, w kolejności modułów szkolenia albo pojedynczo, jako materiał do pracy zespołu.', { size: 18 })]),
], { fill: LIGHTO, bar: ORANGE }));

CZESCI.forEach(c => {
  K.push(spacer(220));
  K.push(p([
    t('  ' + c.nr + '  ', { bold: true, size: 20, color: ORANGE }),
    t('   ' + c.tytul, { bold: true, size: 24, color: PURPLE }),
    t('   ·   ' + c.czas, { bold: true, size: 22, color: ORANGE }),
  ], { before: 200, after: 100, align: AlignmentType.LEFT, fill: LIGHT }));
  K.push(H3('Zakres'));
  c.zakres.forEach(z => K.push(bullet(z)));
  K.push(H3('Druki pokazywane w części'));
  K.push(p([t(c.druki, { size: 18 })], { align: AlignmentType.LEFT }));
});

const naglowekTxt = 'Film szkoleniowy — spis części, zakres i czas';
const header = new Header({ children: [new Paragraph({ spacing: { after: 60 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [t('PCTP · EduPlaner 2026', { size: 15, color: ORANGE, bold: true }), t('     ' + naglowekTxt, { size: 15, color: '8A8A8A' })] })] });
const footer = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [new TextRun({ font: FONT, size: 15, color: '8A8A8A', children: ['Strona ', PageNumber.CURRENT, ' z ', PageNumber.TOTAL_PAGES] })] })] });

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
    headers: { default: header }, footers: { default: footer }, children: K }],
});

Packer.toBuffer(doc).then(b => {
  const plik = __dirname + '/../../film/Spis_czesci_filmu.docx';
  fs.writeFileSync(plik, b);
  console.log('OK ->', plik, (b.length / 1024).toFixed(0) + ' KB');
});
