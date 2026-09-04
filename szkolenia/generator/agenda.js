// Agenda 120-minutowego szkolenia z filmem — buduje Word w stylu scenariusza.
// Uruchom: node agenda.js  (z katalogu szkolenia/generator, po npm install)
const G = require('./gen.js');
const { Document, Packer, Paragraph, AlignmentType, BorderStyle, Header, Footer, PageNumber,
        LevelFormat, fs, t, p, H1, H2, H3, bullet, spacer, box, table, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO, FONT } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));

add(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400, after: 120 },
  children: [t('PCTP  ·  EduPlaner 2026', { bold: true, size: 20, color: ORANGE, sp: 40 })] }));
add(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60, line: 560 },
  children: [t('Agenda szkolenia z filmem', { bold: true, size: 40, color: PURPLE })] }));
add(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60, line: 560 },
  children: [t('Dokumentacja przedszkolna 2026/2027', { bold: true, size: 40, color: PURPLE })] }));
add(new Paragraph({ alignment: AlignmentType.CENTER, border: { top: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 10 } },
  spacing: { before: 120, after: 200 }, children: [t('')] }));
add(new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 },
  children: [t('120 minut  ·  sześć modułów filmowych (ok. 43 min)  ·  ćwiczenia na sali', { size: 22, color: '4A4A4A' })] }));

add(box('JAK PROWADZIĆ', [
  p([t('Film jest przeplatany ćwiczeniami. ', { bold: true }), t('Prowadzący zatrzymuje odtwarzanie po każdym module w miejscu oznaczonym w tabeli i uruchamia ćwiczenie z pełnego scenariusza szkolenia (moduły M1–M10). Film nie zastępuje prowadzącego — jest wykładem, który zawsze brzmi tak samo, żeby prowadzący mógł skupić się na pracy zespołu.')]),
  p([t('Materiały na sali: ', { bold: true }), t('druki Metryczki i KPOF A/B/C dla każdego uczestnika, kazusy A/B/C z modułu M5 scenariusza, karty A5 na cele SMART, flipchart, załączniki Z1–Z8.')]),
], { fill: LIGHTO, bar: ORANGE }));

add(spacer(160));
add(H1('▌', 'Przebieg — 120 minut'));
add(table(['Czas', 'Blok', 'Forma', 'Co się dzieje', 'Materiały'], [
  ['0:00–0:05', 'Otwarcie', 'prowadzący', 'Kontrakt, trzy karteczki: dokument, którego nie rozumiem · który zajmuje najwięcej czasu · pytanie na dziś.', 'karteczki, 3 arkusze na ścianie'],
  ['0:05–0:12', 'FILM · M1', 'film', 'Podstawa prawna — co obowiązuje od 1 września 2026. STOP po ostatniej planszy „Trzy zdania na zamknięcie".', 'Z1 ściąga podstaw prawnych'],
  ['0:12–0:24', 'Ćwiczenie', 'zespoły 3–4', '„Sąd nad dokumentem": Strażnik Prawa · Adwokat dziecka · Kontroler — trzy anonimowe fragmenty dokumentacji z lat ubiegłych.', 'fragmenty WOPF, IPET, opinii'],
  ['0:24–0:30', 'FILM · M2', 'film', 'Obieg dokumentów — sześć przystanków. STOP po planszy „Zapamiętajmy kolejność".', '—'],
  ['0:30–0:35', 'FILM · M3', 'film', 'Metryczka — zasadność i wypełnianie krok po kroku (animacja druku).', 'druk Metryczki'],
  ['0:35–0:45', 'Ćwiczenie', 'indywidualnie + pary', '„Metryczka w 10 minut": sekcje I, II, VI, VII dla jednego dziecka; kontrola krzyżowa sekcji VI (kto podaje lek, gdzie, kogo powiadamiamy).', 'druk Metryczki'],
  ['0:45–0:53', 'FILM · M4', 'film', 'KPOF — budowa, skala, siedem zasad, wypełnianie, liczenie, profil. STOP po planszy „dwa razy w roku".', 'KPOF A/B/C'],
  ['0:53–1:07', 'Ćwiczenie', 'zespoły 3', '„Policz i zdecyduj": kazusy A (profil poszarpany), B (płaski, niski), C (pułapka reguły nadrzędnej). Wniosek jednym zdaniem na flipchart.', 'kazusy A/B/C, kalkulatory'],
  ['1:07–1:14', 'FILM · M5', 'film', 'Obserwacja pogłębiona — reguły R1–R6, ABC, profil sensoryczny, teoria umysłu, karta decyzyjna.', 'Z4 karta decyzyjna'],
  ['1:14–1:22', 'Ćwiczenie', 'zespoły 3', 'Trzy kazusy z modułu M6 scenariusza: która reguła, który moduł, którego NIE uruchamiamy i dlaczego.', 'Z4'],
  ['1:22–1:32', 'FILM · M6', 'film', 'Ocena → program → cele SMART (czym są, czy wymagane) → ewaluacja → opinia o funkcjonowaniu dziecka dla poradni (10 dni, § 7 ust. 3).', 'Z5 karta celu'],
  ['1:32–1:45', 'Warsztat', 'zespoły 3', '„Napisz trzy cele": z wniosków z kazusów A/B/C; kontrola krzyżowa pięcioma pytaniami S-M-A-R-T.', 'karty A5, Z5'],
  ['1:45–1:52', 'Warsztat', 'pary', '„Szkic w 7 minut": punkty 2, 4 i 6 opinii o funkcjonowaniu dziecka; mocne strony PIERWSZE i nie krótsze niż trudności.', 'wzór opinii'],
  ['1:52–2:00', 'Zamknięcie', 'rada', 'Powrót do karteczek z otwarcia; przyjęcie kalendarza (Z6) i reguł R1–R6; jedno zdanie od każdego: „od poniedziałku robię inaczej…"; ankieta (Z7).', 'Z6, Z7'],
], [1150, 1300, 1400, CONTENT - 1150 - 1300 - 1400 - 1900, 1900], { boldCol0: true }));

add(spacer(160));
add(H2('Czas filmu w modułach'));
add(table(['Moduł', 'Temat', 'Czas filmu', 'Ćwiczenie po module'], [
  ['M1', 'Podstawa prawna', '7 min 25 s', 'Sąd nad dokumentem · 12 min'],
  ['M2', 'Obieg dokumentów', '5 min 50 s', '—'],
  ['M3', 'Metryczka', '4 min 53 s', 'Metryczka w 10 minut'],
  ['M4', 'Kwestionariusz KPOF', '7 min 48 s', 'Policz i zdecyduj · 14 min'],
  ['M5', 'Obserwacja pogłębiona', '6 min 54 s', 'Kazusy · 8 min'],
  ['M6', 'Ocena · program · SMART · ewaluacja · poradnia', '9 min 37 s', 'Trzy cele · 13 min + Szkic · 7 min'],
], [900, 4200, 1500, CONTENT - 900 - 4200 - 1500], { boldCol0: true }));

add(spacer(160));
add(box('DWIE ZASADY PROWADZĄCEGO', [
  p([t('1. Film nigdy nie leci bez przerwy. ', { bold: true }), t('Najdłuższy odcinek to niecałe dziesięć minut. Po każdym module zespół coś robi na swoich drukach — inaczej wykład zostaje w sali, a nie w teczkach dzieci.')]),
  p([t('2. Pytania z karteczek mają swój los. ', { bold: true }), t('Każde pytanie z otwarcia dostaje odpowiedź w module albo trafia na kartę „do wyjaśnienia" z nazwiskiem i terminem.')]),
], { fill: LIGHT, bar: PURPLE }));

const header = new Header({ children: [ new Paragraph({ spacing: { after: 60 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [t('PCTP · EduPlaner 2026', { size: 15, color: ORANGE, bold: true }), t('     Agenda szkolenia z filmem · dokumentacja przedszkolna 2026/2027', { size: 15, color: '8A8A8A' })] })]});
const footer = new Footer({ children: [ new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 60 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [ new (require('docx').TextRun)({ font: FONT, size: 15, color: '8A8A8A', children: ['Strona ', PageNumber.CURRENT, ' z ', PageNumber.TOTAL_PAGES] }) ] })]});

const doc = new Document({
  creator: 'EduPlaner 2026 · PCTP', title: 'Agenda szkolenia z filmem — 120 minut',
  styles: { default: { document: { run: { font: FONT, size: 20, color: '1A1A1A' }, paragraph: { spacing: { line: 264 } } } } },
  numbering: { config: [
    { reference: 'kropki', levels: [{ level: 0, format: LevelFormat.BULLET, text: '▪', alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 340, hanging: 220 } }, run: { color: ORANGE, font: FONT, size: 18 } } }] },
    { reference: 'kroki', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 380, hanging: 380 } }, run: { color: ORANGE, font: FONT, bold: true } } }] },
  ] },
  sections: [{ properties: { page: { margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } },
    headers: { default: header }, footers: { default: footer }, children: C }],
});
Packer.toBuffer(doc).then(b => {
  const out = '/home/user/chatbot/film/Agenda_szkolenia_120min.docx';
  fs.writeFileSync(out, b); console.log('OK ->', out, (b.length / 1024).toFixed(0) + ' KB');
});
