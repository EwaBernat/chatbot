// Druki do filmu i szkolenia: WOPF (przedszkole), IPET (przedszkole), Opinia o funkcjonowaniu dziecka.
// Uruchom: node druki.js  → zapisuje trzy pliki .docx do ../../film/druki/
const G = require('./gen.js');
const { Document, Packer, Paragraph, AlignmentType, BorderStyle, Header, Footer, PageNumber, LevelFormat,
        fs, t, p, H1, H2, H3, bullet, lines, spacer, pageBreak, box, table, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO, FONT } = G;
const { TextRun } = require('docx');

const hint = (txt) => p([t(txt, { i: true, size: 16, color: '6F6A7D' })], { before: 0, after: 40, align: AlignmentType.LEFT });
const pole = (label, n = 2) => [H3(label), ...lines(n, { gap: 190 })];
const blank = (n = 1) => lines(n, { gap: 150 });
const naglowek = (nad, tytul, pod) => [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 80 },
    children: [t(nad, { bold: true, size: 18, color: ORANGE, sp: 30 })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60, line: 480 },
    children: [t(tytul, { bold: true, size: 34, color: PURPLE })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 8 } },
    spacing: { before: 80, after: 120 }, children: [t(pod, { size: 17, color: '4A4A4A' })] }),
];
const metr = (rows) => table(null, rows.map(r => [r, blank(1)]), [3000, CONTENT - 3000], { boldCol0: true, zebra: false });
const podpisy = (osoby) => table(['Funkcja', 'Imię i nazwisko', 'Data', 'Podpis'],
  osoby.map(o => [o, '', '', '']), [2800, 3000, 1500, CONTENT - 2800 - 3000 - 1500], { boldCol0: true, zebra: false });

function dokument(kids, naglowekTxt, plik) {
  const header = new Header({ children: [ new Paragraph({ spacing: { after: 60 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
    children: [t('PCTP · EduPlaner 2026', { size: 15, color: ORANGE, bold: true }), t('     ' + naglowekTxt, { size: 15, color: '8A8A8A' })] })]});
  const footer = new Footer({ children: [ new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
    border: { top: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
    children: [ new TextRun({ font: FONT, size: 15, color: '8A8A8A', children: ['Strona ', PageNumber.CURRENT, ' z ', PageNumber.TOTAL_PAGES] }) ] })]});
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
      headers: { default: header }, footers: { default: footer }, children: kids }],
  });
  return Packer.toBuffer(doc).then(b => { fs.writeFileSync(plik, b); console.log('OK ->', plik, (b.length / 1024).toFixed(0) + ' KB'); });
}

/* ===================== WOPF ===================== */
const W = [];
W.push(...naglowek('WOPF · PRZEDSZKOLE · ROK SZKOLNY 2026 / 2027', 'Wielospecjalistyczna ocena poziomu funkcjonowania dziecka',
  'rozporządzenie w sprawie kształcenia specjalnego (tekst jedn. Dz.U. 2020 poz. 1309) · § 6 ust. 4, 9–11 · ocena co najmniej 2 razy w roku'));
W.push(metr(['Dziecko / grupa', 'Orzeczenie: numer, data, podstawa wydania', 'Ocena nr (I wrzesień · II styczeń · III maj) · data', 'Skład zespołu', 'Źródła danych (KPOF z dnia, obserwacja pogłębiona, karta mowy, rodzice)']));
W.push(spacer(120));
W.push(...pole('1.  Mocne strony i zasoby dziecka', 3)); W.push(hint('Źródło: KPOF — twierdzenia ocenione na 5 i obszary „zasób”; obserwacje jakościowe; relacja rodziców.'));
W.push(H3('2.  Funkcjonowanie w dziewięciu obszarach (ICF d1–d9)'));
W.push(table(['Obszar', 'Średnia KPOF', 'Opis funkcjonowania (co dziecko robi, w jakich warunkach, przy jakim wsparciu)'], [
  ['d1 · uczenie się i stosowanie wiedzy', '', ''], ['d2 · ogólne zadania i obowiązki', '', ''], ['d3 · porozumiewanie się', '', ''],
  ['d4 · poruszanie się', '', ''], ['d5 · dbanie o siebie', '', ''], ['d6 · życie domowe (opisowo)', '', ''],
  ['d7 · relacje z innymi', '', ''], ['d8 · edukacja i zabawa', '', ''], ['d9 · życie społeczne', '', ''],
], [2900, 1200, CONTENT - 2900 - 1200], { boldCol0: true }));
W.push(...pole('3.  Trudności i ich uwarunkowania', 3)); W.push(hint('Źródło: KPOF — twierdzenia 1–2 i reguła nadrzędna; obserwacja pogłębiona (ABC, profil sensoryczny, ToM, karta mowy).'));
W.push(pageBreak());
W.push(H3('4.  Bariery i ułatwienia w środowisku (komponent „e” ICF)'));
W.push(table(['Bariery — co przeszkadza', 'Ułatwienia — co pomaga'], [[blank(3), blank(3)]], [CONTENT / 2, CONTENT / 2], { zebra: false }));
W.push(...pole('5.  Efekty dotychczasowego wsparcia', 3)); W.push(hint('Źródło: karta ewaluacji celów SMART (Z5); dzienniki zajęć specjalistycznych.'));
W.push(...pole('6.  Potrzeby rozwojowe i edukacyjne', 3));
W.push(...pole('7.  Wnioski i rekomendacje — zalecenia do programu (IPET)', 4)); W.push(hint('Każde zalecenie przechodzi do IPET jako wiersz „zalecenie z WOPF → realizacja”.'));
W.push(spacer(120));
W.push(H3('Zespół dokonujący oceny'));
W.push(podpisy(['Koordynator (nauczyciel grupy)', 'Psycholog', 'Logopeda', 'Pedagog specjalny / terapeuta', 'Dyrektor']));
W.push(spacer(80));
W.push(box('RODZICE', [p([t('Rodzice otrzymali kopię wielospecjalistycznej oceny (§ 6 ust. 11): data ..................  podpis ........................................', { size: 18 })])], { fill: LIGHTO, bar: ORANGE }));

/* ===================== IPET ===================== */
const I = [];
I.push(...naglowek('IPET · PRZEDSZKOLE · ROK SZKOLNY 2026 / 2027', 'Indywidualny program edukacyjno-terapeutyczny',
  'rozporządzenie w sprawie kształcenia specjalnego (tekst jedn. Dz.U. 2020 poz. 1309) · § 6 ust. 1 pkt 1–8, ust. 4–5, 9–11 · do 30 września albo 30 dni od złożenia orzeczenia'));
I.push(H2('I.  Dane dziecka i podstawa programu'));
I.push(metr(['Dziecko / grupa', 'Orzeczenie: numer, data, organ, podstawa wydania (rodzaj niepełnosprawności)', 'WOPF z dnia (podstawa programu, § 6 ust. 4)', 'Okres realizacji programu', 'Data opracowania · koordynator zespołu']));
I.push(spacer(100));
I.push(H2('II.  Zalecenia z orzeczenia i ich realizacja  (§ 6 ust. 4)'));
I.push(table(['Zalecenie poradni (z orzeczenia)', 'Forma realizacji w przedszkolu', 'Kto', 'Wymiar · od kiedy', 'Ocena realizacji'],
  [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], [2900, 2400, 1300, 1500, CONTENT - 2900 - 2400 - 1300 - 1500], { zebra: false }));
I.push(spacer(100));
I.push(H2('III.  Zalecenia z WOPF i ich realizacja  (§ 6 ust. 4, 9)'));
I.push(table(['Zalecenie z oceny (blok 7 WOPF)', 'Forma realizacji', 'Kto', 'Wymiar · od kiedy', 'Ocena realizacji'],
  [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], [2900, 2400, 1300, 1500, CONTENT - 2900 - 2400 - 1300 - 1500], { zebra: false }));
I.push(pageBreak());
I.push(H2('IV.  Zakres i sposób dostosowania wymagań oraz warunków organizacji  (§ 6 ust. 1 pkt 1 i 7)'));
I.push(table(['Obszar dostosowania', 'Dostosowanie (co konkretnie robimy)', 'Bariera z WOPF, na którą odpowiada'], [
  ['Sposób podania treści (metody, formy)', '', ''], ['Czas i tempo', '', ''], ['Przestrzeń i organizacja sali', '', ''],
  ['Sposób sprawdzania umiejętności', '', ''], ['Pomoce i technologie wspomagające', '', ''], ['Warunki organizacji kształcenia (rodzaj niepełnosprawności)', '', ''],
], [2900, 3700, CONTENT - 2900 - 3700], { boldCol0: true }));
I.push(spacer(100));
I.push(H2('V.  Zintegrowane działania nauczycieli i specjalistów  (§ 6 ust. 1 pkt 2)'));
I.push(hint('Jeden cel — jeden plan — wiele rąk. Każdy cel SMART ma zapisane działania każdej osoby, także rodziców w domu.'));
I.push(table(['Cel SMART (z części VII)', 'Nauczyciel grupy', 'Logopeda / specjalista', 'Psycholog / terapeuta', 'Rodzice w domu'],
  [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']], [2500, 1750, 1750, 1750, CONTENT - 2500 - 3 * 1750], { zebra: false }));
I.push(spacer(100));
I.push(H2('VI.  Formy i okres pomocy psychologiczno-pedagogicznej, wymiar godzin  (§ 6 ust. 1 pkt 3)'));
I.push(table(['Forma pomocy', 'Wymiar godzin', 'Okres', 'Prowadzący'], [['', '', '', ''], ['', '', '', '']], [3400, 1600, 2000, CONTENT - 3400 - 1600 - 2000], { zebra: false }));
I.push(pageBreak());
I.push(H2('VII.  Cele edukacyjno-terapeutyczne SMART  (mierzalność wymagana do oceny efektywności)'));
I.push(table(['Obszar ICF', 'Cel: dziecko · sytuacja · zachowanie · ile z ilu · wsparcie · do kiedy', 'Pomiar', 'Termin'],
  [['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [1500, 4900, 1700, CONTENT - 1500 - 4900 - 1700], { zebra: false }));
I.push(spacer(100));
I.push(H2('VIII.  Zajęcia rewalidacyjne i inne zajęcia odpowiednie do potrzeb  (§ 6 ust. 1 pkt 5, ust. 2)'));
I.push(table(['Rodzaj zajęć', 'Wymiar', 'Prowadzący', 'Zakres (np. AAC, orientacja, umiejętności społeczne)'], [['', '', '', ''], ['', '', '', '']], [2900, 1200, 2000, CONTENT - 2900 - 1200 - 2000], { zebra: false }));
I.push(spacer(100));
I.push(H2('IX.  Wsparcie rodziców, współpraca z rodzicami i współdziałanie z poradnią  (§ 6 ust. 1 pkt 4 i 6)'));
I.push(...blank(3));
I.push(spacer(60));
I.push(H2('X.  Zajęcia realizowane indywidualnie lub w grupie do 5 dzieci  (§ 6 ust. 1 pkt 8)'));
I.push(...blank(2));
I.push(spacer(60));
I.push(H2('XI.  Ewaluacja programu  (§ 6 ust. 9)'));
I.push(table(['Termin WOPF', 'Ocena efektywności (cele: osiągnięty / częściowo / brak postępu / regres)', 'Decyzja zespołu · modyfikacja programu'],
  [['I · wrzesień', '', ''], ['II · styczeń', '', ''], ['III · maj (zalecana)', '', '']], [2200, 4000, CONTENT - 2200 - 4000], { boldCol0: true, zebra: false }));
I.push(spacer(100));
I.push(H2('XII.  Zespół opracowujący, zatwierdzenie, rodzice'));
I.push(podpisy(['Dyrektor (zatwierdzenie)', 'Koordynator — nauczyciel grupy', 'Logopeda', 'Psycholog', 'Pedagog specjalny / terapeuta']));
I.push(spacer(80));
I.push(box('RODZICE', [p([t('Rodzice uczestniczyli w spotkaniu zespołu / zostali zawiadomieni (data, forma): ..............................   Rodzice otrzymali kopię programu (§ 6 ust. 11): data ..............  podpis ...............................', { size: 18 })])], { fill: LIGHTO, bar: ORANGE }));

/* ===================== OPINIA ===================== */
const O = [];
O.push(...naglowek('OPINIA DLA PORADNI · PRZEDSZKOLE', 'Opinia o funkcjonowaniu dziecka w przedszkolu',
  'rozporządzenie Ministra Edukacji z 2 marca 2026 r. w sprawie orzeczeń i opinii (Dz.U. 2026 poz. 428) · § 7 ust. 2–3 · 10 dni od dnia otrzymania przez dyrektora prośby o jej wydanie'));
O.push(metr(['Dziecko / grupa / okres uczęszczania', 'Prośba przewodniczącego zespołu orzekającego — data otrzymania przez dyrektora', 'Termin wydania (10 dni, § 7 ust. 3) · data wydania opinii', 'Autorzy opinii (nauczyciele, specjaliści) i ich role']));
O.push(spacer(100));
O.push(...pole('1.  Dane formalne — dziecko, grupa, okres uczęszczania, autorzy', 1));
O.push(...pole('2.  Mocne strony i uzdolnienia dziecka  (piszemy jako pierwsze, nie krócej niż trudności)', 4)); O.push(hint('Źródło: KPOF — twierdzenia na 5 i obszary „zasób”; obserwacje jakościowe; karta mowy — obszary 8–10 pkt.'));
O.push(...pole('3.  Funkcjonowanie w obszarach aktywności i uczestniczenia (ICF): uczenie się · komunikacja · ruch · samoobsługa · relacje · zabawa i zajęcia', 4)); O.push(hint('Źródło: KPOF — średnie obszarów d1–d9 przełożone na opis słowny, w konkretnych sytuacjach.'));
O.push(pageBreak());
O.push(...pole('4.  Trudności — zachowania z częstotliwością i kontekstem, bez etykiet i hipotez diagnostycznych', 4)); O.push(hint('Źródło: KPOF — twierdzenia 1–2; obserwacja pogłębiona: ABC, profil sensoryczny, ToM, karta mowy.'));
O.push(...pole('5.  Bariery i ułatwienia w środowisku przedszkolnym', 3));
O.push(...pole('6.  Udzielone wsparcie i jego efekty — co, jak długo, z jakim skutkiem (z liczbami)', 3)); O.push(hint('Źródło: karta ewaluacji celów SMART, dzienniki zajęć specjalistycznych.'));
O.push(...pole('7.  Współpraca z rodzicami — ustalenia, konsultacje, przekazane zalecenia', 3)); O.push(hint('Źródło: metryczka, sekcja XI — rejestr kontaktów i ustaleń. Informacje od rodziców i specjalistów spoza przedszkola oznaczamy jako relację ze wskazaniem źródła.'));
O.push(spacer(120));
O.push(podpisy(['Nauczyciel grupy', 'Specjalista (logopeda / psycholog / pedagog)', 'Dyrektor']));
O.push(spacer(80));
O.push(box('KOPIA DLA RODZICÓW', [p([t('Kopię opinii przekazano rodzicom dziecka: data ..................  podpis rodzica ........................................', { size: 18 })])], { fill: LIGHTO, bar: ORANGE }));

const OUT = '/home/user/chatbot/film/druki/';
Promise.all([
  dokument(W, 'WOPF — wielospecjalistyczna ocena poziomu funkcjonowania · przedszkole', OUT + 'WOPF_przedszkole.docx'),
  dokument(I, 'IPET — indywidualny program edukacyjno-terapeutyczny · przedszkole', OUT + 'IPET_przedszkole.docx'),
  dokument(O, 'Opinia o funkcjonowaniu dziecka w przedszkolu · § 7 ust. 2 rozporządzenia o orzekaniu', OUT + 'Opinia_o_funkcjonowaniu_dziecka.docx'),
]).then(() => console.log('gotowe'));
