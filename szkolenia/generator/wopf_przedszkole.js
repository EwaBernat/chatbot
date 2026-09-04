// WOPF — wielospecjalistyczna ocena poziomu funkcjonowania DZIECKA (przedszkole).
// Układ odwzorowuje druk WOPFU EduPlaner 2026, ale w wersji przedszkolnej:
// dziecko i grupa zamiast ucznia i klasy, obszary ICF opisane po przedszkolnemu.
// Uruchom: node wopf_przedszkole.js  → ../../film/druki/WOPF_przedszkole_2026.docx
const G = require('./gen.js');
const { Document, Packer, Paragraph, AlignmentType, BorderStyle, Header, Footer, PageNumber, LevelFormat,
        fs, t, p, H2, H3, spacer, pageBreak, box, table, lines, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO, FONT } = G;
const { TextRun } = require('docx');

const hint = (txt) => p([t(txt, { i: true, size: 16, color: '6F6A7D' })], { before: 0, after: 60, align: AlignmentType.LEFT });
const sekcja = (nr, tytul, dopisek) => p([
  t('  ' + nr + '  ', { bold: true, size: 20, color: ORANGE }),
  t('   ' + tytul, { bold: true, size: 24, color: PURPLE }),
  ...(dopisek ? [t('   ' + dopisek, { size: 17, color: ORANGE })] : []),
], { before: 240, after: 100, align: AlignmentType.LEFT, fill: LIGHT });
const pole = (label, n = 3) => [H3(label), ...lines(n, { gap: 200 })];
// pary „pole opisowe” w dwóch kolumnach — jak w druku WOPFU
const dwa = (a, b) => table(null, [[a, b]], [CONTENT / 2, CONTENT / 2], { zebra: false });
const wpis = (etykieta) => [
  p([t(etykieta, { bold: true, size: 16, color: PURPLE, caps: true })], { before: 60, after: 20, align: AlignmentType.LEFT }),
  ...lines(1, { gap: 170 }),
];
// lista do zaznaczania — wąska kolumna na ptaszek + treść
const zaznacz = (pary) => table(null, pary.map(([l, r]) => ['', l, '', r]),
  [420, CONTENT / 2 - 420, 420, CONTENT / 2 - 420], { zebra: false });

const naglowek = (nad, tytul, pod) => [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 160, after: 80 },
    children: [t(nad, { bold: true, size: 18, color: ORANGE, sp: 30 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60, line: 460 },
    children: [t(tytul, { bold: true, size: 32, color: PURPLE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 8 } },
    spacing: { before: 80, after: 120 }, children: [t(pod, { size: 17, color: '4A4A4A' })] }),
];

const K = [];

/* ---------- strona 1: dane, tryb oceny, zespół ---------- */
K.push(...naglowek('WOPF · PRZEDSZKOLE · ROK SZKOLNY 2026 / 2027',
  'Wielospecjalistyczna ocena poziomu funkcjonowania dziecka',
  'ocena funkcjonalna wg ICF · poprzedza opracowanie IPET i jest jego podstawą · co najmniej dwa razy w roku szkolnym'));

K.push(sekcja('I', 'DANE DZIECKA'));
K.push(table(null, [
  [[...wpis('Imię i nazwisko dziecka')], [...wpis('Data urodzenia')]],
  [[...wpis('Grupa / oddział')], [...wpis('Etap edukacyjny')]],
  [[...wpis('Numer i data orzeczenia / poradnia')], [...wpis('Podstawa wydania orzeczenia (np. autyzm)')]],
  [[...wpis('Koordynator zespołu')], [...wpis('Data sporządzenia / rok szkolny')]],
], [CONTENT / 2, CONTENT / 2], { zebra: false }));

K.push(sekcja('I a', 'RODZAJ OCENY I TRYB'));
K.push(hint('Zaznacz rodzaj oceny. Ocena pierwsza poprzedza opracowanie IPET (§ 6 ust. 4); ocena okresowa — co najmniej dwa razy w roku szkolnym (§ 6 ust. 9).'));
K.push(table(null, [['', 'pierwsza — przed opracowaniem IPET', '', 'okresowa — śródroczna', '', 'okresowa — roczna']],
  [420, 2700, 420, 2400, 420, CONTENT - 420 * 3 - 2700 - 2400], { zebra: false }));
K.push(dwa([...wpis('Data poprzedniej oceny')], [...wpis('Współpraca z poradnią PP / podmiotami')]));

K.push(sekcja('II', 'ZESPÓŁ DOKONUJĄCY OCENY'));
K.push(table(['Lp.', 'Imię i nazwisko', 'Specjalność', 'Funkcja w zespole'], [
  ['1', '', '', 'Koordynator zespołu'],
  ['2', '', '', 'Nauczyciel grupy'],
  ['3', '', '', 'Psycholog'],
  ['4', '', '', 'Pedagog specjalny'],
  ['5', '', '', 'Logopeda / neurologopeda'],
  ['6', '', '', 'Terapeuta SI'],
], [700, 3200, 2600, CONTENT - 700 - 3200 - 2600], { zebra: false }));
K.push(hint('Podstawa prawna: § 6 ust. 3, 6 i 11 rozporządzenia o kształceniu specjalnym (tekst jedn. Dz.U. 2020 poz. 1309); obowiązek oceny — art. 127 Prawa oświatowego oraz § 6 ust. 4 i 9.'));

/* ---------- strona 2: diagnoza funkcjonalna w 9 obszarach ---------- */
K.push(pageBreak());
K.push(sekcja('III', 'DIAGNOZA FUNKCJONALNA — 9 OBSZARÓW ICF / KPOF'));
K.push(hint('Wynik funkcjonalny każdego obszaru i wynikający z niego poziom wsparcia. Skala stenowa 1–10: sten 8–10 → Poziom I, sten 5–7 → Poziom II, sten 1–4 → Poziom III. Wartości spójne z kwestionariuszem KPOF i z celami SMART w IPET.'));
K.push(table(['Lp.', 'Obszar funkcjonowania (ICF)', 'Kody ICF', 'Pkt', 'Sten', 'Poziom'], [
  ['I', 'Uczenie się i stosowanie wiedzy', 'd110–d179 · b140', '... / 20', '', ''],
  ['II', 'Ogólne zadania i obowiązki', 'd210–d250 · b1641', '... / 20', '', ''],
  ['III', 'Porozumiewanie się', 'd310–d360 · b320', '... / 20', '', ''],
  ['IV', 'Motoryka i poruszanie się', 'd440–d455 · b760', '... / 20', '', ''],
  ['V', 'Dbanie o siebie i samoobsługa', 'd510–d570 · b164', '... / 20', '', ''],
  ['VI', 'Życie domowe (opisowo)', 'd610–d660 · d230', '... / 20', '', ''],
  ['VII', 'Relacje z rówieśnikami i dorosłymi', 'd710–d770 · b1801', '... / 20', '', ''],
  ['VIII', 'Zabawa i zajęcia w przedszkolu', 'd880 · d820 · b1720', '... / 20', '', ''],
  ['IX', 'Życie w społeczności lokalnej', 'd910–d950', '... / 20', '', ''],
], [700, 3000, 2200, 1100, 800, CONTENT - 700 - 3000 - 2200 - 1100 - 800], { zebra: true, boldCol0: true }));
K.push(spacer(120));
K.push(H3('Obszary wymagające wsparcia — synteza wg poziomów'));
K.push(table(['Poziom III · sten 1–4 · wsparcie specjalistyczne', 'Poziom II · sten 5–7 · wsparcie dodatkowe', 'Poziom I · sten 8–10 · zasoby i bieżąca praca'],
  [['', '', '']], [CONTENT / 3, CONTENT / 3, CONTENT - 2 * Math.round(CONTENT / 3)], { zebra: false }));
K.push(spacer(100));
K.push(box('PODSTAWA METODOLOGICZNA', [
  p([t('Ocena funkcjonalna w dziewięciu obszarach realizuje § 6 ust. 10 rozporządzenia o kształceniu specjalnym; klasyfikacja ICF (WHO 2001) oraz nowa podstawa programowa wychowania przedszkolnego (Dz.U. 2026 poz. 378). Skala stenowa i trzystopniowe poziomy wsparcia są narzędziem roboczym przedszkola, nie wynikają wprost z rozporządzenia.', { size: 17 })]),
], { fill: LIGHT, bar: PURPLE }));

/* ---------- strona 3: czynniki środowiskowe ---------- */
K.push(pageBreak());
K.push(sekcja('IV', 'CZYNNIKI ŚRODOWISKOWE (KONTEKSTOWE WG ICF)'));
K.push(hint('Model biopsychospołeczny ICF — wpływ otoczenia (rodzina, przedszkole, rówieśnicy, technologie, postawy) na funkcjonowanie dziecka. Zaznacz czynniki wspierające i utrudniające.'));
K.push(zaznacz([
  ['Wsparcie i zaangażowanie rodziny (e310 · e410)', 'Relacje i akceptacja rówieśników (e320 · e425)'],
  ['Postawy nauczycieli i specjalistów (e330 · e430)', 'Dostosowania i pomoce dydaktyczne (e130)'],
  ['Technologie wspomagające / AAC (e125)', 'Dostępność i organizacja sali (e150)'],
  ['Warunki sensoryczne — hałas, światło (e240 · e250)', 'Wsparcie poradni PP i instytucji (e585)'],
]));
K.push(spacer(80));
K.push(dwa(
  [H3('Ułatwienia w środowisku (czynniki wspierające)'), ...lines(3, { gap: 190 })],
  [H3('Bariery w środowisku (czynniki utrudniające)'), ...lines(3, { gap: 190 })],
));
K.push(spacer(120));
K.push(sekcja('IV a', 'DOBROSTAN DZIECKA'));
K.push(...pole('Samopoczucie, relacje, poczucie bezpieczeństwa i sprawczości, uczestnictwo w życiu grupy', 3));
K.push(hint('Źródło: obserwacja jakościowa, analiza ABC, profil sensoryczny, karta obserwacji rozwoju mowy, relacja rodziców.'));

/* ---------- strona 4: potrzeby, mocne strony, przeniesienie do IPET ---------- */
K.push(pageBreak());
K.push(sekcja('V', 'POTRZEBY, MOCNE STRONY I PREDYSPOZYCJE', '§ 6 ust. 10 pkt 1'));
K.push(...pole('Indywidualne potrzeby rozwojowe i edukacyjne dziecka', 3));
K.push(...pole('Mocne strony — co dziecko już potrafi', 3));
K.push(...pole('Zainteresowania i uzdolnienia — co je motywuje', 2));

K.push(spacer(120));
K.push(sekcja('VI', 'PRZENIESIENIE DO IPET — CO Z CZEGO WYNIKA', '§ 6 ust. 4'));
K.push(hint('Poniższe wskazania wynikają wprost z wyników tej oceny i stanowią podstawę opracowania programu. Szczegółowe dostosowania i wymiar godzin zajęć ustala się dopiero w IPET.'));
K.push(...pole('1.  Mocne strony, predyspozycje, zainteresowania', 2)); K.push(hint('→ IPET: dostosowania i motywacja · źródło: sekcja V'));
K.push(...pole('2.  Cele SMART — edukacyjne i terapeutyczne', 2)); K.push(hint('→ IPET: cele w sferach · źródło: diagnoza funkcjonalna (III) i obserwacja pogłębiona'));
K.push(...pole('3.  Poziom wsparcia i priorytetowe obszary', 2)); K.push(hint('→ IPET: zakres wsparcia · źródło: synteza wg poziomów (III)'));
K.push(...pole('4.  Dostosowania — wskazania ogólne', 2)); K.push(hint('→ IPET § 6 ust. 1 pkt 1: zakres i sposób dostosowania'));
K.push(...pole('5.  Zintegrowane działania nauczycieli i specjalistów (w tym AAC)', 2)); K.push(hint('→ IPET § 6 ust. 1 pkt 2 · źródło: czynniki środowiskowe (IV) i zalecenia obszarów'));
K.push(spacer(140));
K.push(H3('Podpisy zespołu'));
K.push(table(['Funkcja', 'Imię i nazwisko', 'Data', 'Podpis'], [
  ['Koordynator zespołu', '', '', ''],
  ['Nauczyciel grupy', '', '', ''],
  ['Psycholog', '', '', ''],
  ['Logopeda / pedagog specjalny', '', '', ''],
  ['Dyrektor', '', '', ''],
], [2800, 3000, 1500, CONTENT - 2800 - 3000 - 1500], { boldCol0: true, zebra: false }));
K.push(spacer(80));
K.push(box('KOPIA DLA RODZICÓW', [
  p([t('Rodzice otrzymują kopię wielospecjalistycznej oceny poziomu funkcjonowania dziecka (§ 6 ust. 12). Kopię przekazano: data ................. podpis rodzica .....................................', { size: 17 })]),
], { fill: LIGHTO, bar: ORANGE }));

/* ---------- zapis ---------- */
const naglowekTxt = 'WOPF — wielospecjalistyczna ocena poziomu funkcjonowania dziecka · przedszkole';
const header = new Header({ children: [new Paragraph({ spacing: { after: 60 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [t('PCTP · EduPlaner 2026', { size: 15, color: ORANGE, bold: true }), t('     ' + naglowekTxt, { size: 15, color: '8A8A8A' })] })] });
const footer = new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [new TextRun({ font: FONT, size: 15, color: '8A8A8A', children: ['Strona ', PageNumber.CURRENT, ' z ', PageNumber.TOTAL_PAGES, ' · WOPF · przedszkole'] })] })] });

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
  const plik = __dirname + '/../../film/druki/WOPF_przedszkole_2026.docx';
  fs.writeFileSync(plik, b);
  console.log('OK ->', plik, (b.length / 1024).toFixed(0) + ' KB');
});
