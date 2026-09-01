const fs = require('fs');
const d = require('docx');
const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, Table, TableRow,
        TableCell, WidthType, ShadingType, BorderStyle, PageBreak, Footer, Header, PageNumber } = d;

const DATA = JSON.parse(fs.readFileSync('sceny.json', 'utf8'));
const F = 'Arial';
const PURPLE = '2D1B69', ORANGE = 'E8450A', GREY = '55506B', LINE = 'DDD6EE';

const p = (opts) => new Paragraph(opts);
const run = (text, o = {}) => new TextRun(Object.assign({ text, font: F, size: 22 }, o));

const kids = [];

// ---------- strona tytułowa ----------
kids.push(p({ spacing: { before: 400, after: 60 },
  children: [run('EduPlaner 2026 · PCTP Koszalin', { size: 18, bold: true, color: ORANGE,
    characterSpacing: 30 })] }));
kids.push(p({ spacing: { after: 120 },
  children: [run('SCENARIUSZ SZKOLENIA DLA KADRY PEDAGOGICZNEJ', { size: 18, bold: true, color: GREY,
    characterSpacing: 30 })] }));
kids.push(p({ spacing: { after: 80 },
  children: [run('Sala, która uczy każde dziecko', { size: 48, bold: true, color: PURPLE })] }));
kids.push(p({ spacing: { after: 260 },
  children: [run('Dostosowania sali przedszkolnej dla dzieci ze spektrum autyzmu', { size: 28, color: GREY })] }));
kids.push(p({ border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 6 } },
  spacing: { after: 260 }, children: [run('')] }));

const meta = [
  ['Temat', 'Co zmienia nowa podstawa programowa w organizacji sali i jak dostosować salę dla dziecka ze spektrum autyzmu'],
  ['Odbiorcy', 'Nauczyciele wychowania przedszkolnego, pedagodzy specjalni, nauczyciele wspomagający, dyrektorzy'],
  ['Czas', 'Około 20 minut nagrania (' + DATA.razem + ' czystej narracji) · 20 scen'],
  ['Forma', 'Nagranie z awatarem HeyGen · gotowy tekst narracji w osobnym pliku'],
  ['Autorka', 'Mirosława Ewa Jurczyszyn, pedagog specjalny'],
  ['Materiał towarzyszący', 'Broszura „Sala, która uczy każde dziecko” — 49 stron A4'],
];
kids.push(new Table({
  columnWidths: [2400, 6800],
  width: { size: 9200, type: WidthType.DXA },
  borders: {
    top: { style: BorderStyle.SINGLE, size: 4, color: LINE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: LINE },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
    insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: LINE }, insideVertical: { style: BorderStyle.NONE },
  },
  rows: meta.map(([k, v]) => new TableRow({ children: [
    new TableCell({ width: { size: 2400, type: WidthType.DXA }, margins: { top: 90, bottom: 90, left: 60, right: 120 },
      children: [p({ children: [run(k, { bold: true, color: PURPLE, size: 20 })] })] }),
    new TableCell({ width: { size: 6800, type: WidthType.DXA }, margins: { top: 90, bottom: 90, left: 0, right: 60 },
      children: [p({ children: [run(v, { size: 20 })] })] }),
  ] })),
}));

// ---------- jak korzystać ----------
kids.push(p({ spacing: { before: 380, after: 120 },
  children: [run('Jak korzystać z tego scenariusza', { size: 26, bold: true, color: PURPLE })] }));
[
  'Każda scena to osobny slajd w HeyGenie. Do pola tekstowego awatara wklejasz wyłącznie treść z kolumny „Narracja” — bez tytułu sceny i bez opisu planszy.',
  'Gotowy tekst do wklejania, scena po scenie, znajduje się w pliku HeyGen_narracja_20_scen.txt.',
  'Czasy scen wyliczono dla tempa około 132 słów na minutę. Jeśli ustawisz w HeyGenie szybszą mowę, całość skróci się o dwie–trzy minuty.',
  'Opis „Na ekranie” to podpowiedź, co wyświetlić obok awatara: planszę, zdjęcie sali albo stronę z broszury.',
  'Scenariusz można też przeczytać na żywo — wtedy sceny 14 i 20 warto zamienić na ćwiczenie w parach.',
].forEach(t => kids.push(p({ spacing: { after: 90 }, indent: { left: 340, hanging: 220 },
  children: [run('•  ', { color: ORANGE, bold: true }), run(t, { size: 20 })] })));

// ---------- plan czasowy ----------
kids.push(p({ spacing: { before: 320, after: 140 },
  children: [run('Plan czasowy', { size: 26, bold: true, color: PURPLE })] }));
const hdr = (t, w) => new TableCell({ width: { size: w, type: WidthType.DXA },
  shading: { type: ShadingType.CLEAR, fill: PURPLE }, margins: { top: 80, bottom: 80, left: 90, right: 90 },
  children: [p({ children: [run(t, { bold: true, color: 'FFFFFF', size: 18 })] })] });
const cell = (t, w, sh) => new TableCell({ width: { size: w, type: WidthType.DXA },
  shading: sh ? { type: ShadingType.CLEAR, fill: 'F5F1FB' } : undefined,
  margins: { top: 70, bottom: 70, left: 90, right: 90 },
  children: [p({ children: [run(t, { size: 18 })] })] });
kids.push(new Table({
  columnWidths: [900, 1500, 6800], width: { size: 9200, type: WidthType.DXA },
  borders: { top: { style: BorderStyle.SINGLE, size: 4, color: LINE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: LINE },
    left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
    insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: LINE }, insideVertical: { style: BorderStyle.NONE } },
  rows: [new TableRow({ tableHeader: true, children: [hdr('Scena', 900), hdr('Czas', 1500), hdr('Temat', 6800)] })]
    .concat(DATA.sceny.map((s, i) => new TableRow({ children: [
      cell(String(s.nr).padStart(2, '0'), 900, i % 2 === 1),
      cell(s.od + ' – ' + s.do, 1500, i % 2 === 1),
      cell(s.tytul, 6800, i % 2 === 1)] }))),
}));

kids.push(p({ children: [new PageBreak()] }));

// ---------- sceny ----------
DATA.sceny.forEach((s, idx) => {
  kids.push(p({ spacing: { before: idx === 0 ? 0 : 400, after: 40 },
    children: [run('SCENA ' + String(s.nr).padStart(2, '0') + '  ·  ' + s.od + ' – ' + s.do + '  ·  ok. ' + s.sek + ' s',
      { size: 18, bold: true, color: ORANGE, characterSpacing: 20 })] }));
  kids.push(p({ spacing: { after: 100 },
    children: [run(s.tytul, { size: 28, bold: true, color: PURPLE })] }));
  kids.push(new Table({
    columnWidths: [9200], width: { size: 9200, type: WidthType.DXA },
    borders: { top: { style: BorderStyle.SINGLE, size: 4, color: LINE }, bottom: { style: BorderStyle.SINGLE, size: 4, color: LINE },
      left: { style: BorderStyle.SINGLE, size: 18, color: ORANGE }, right: { style: BorderStyle.SINGLE, size: 4, color: LINE },
      insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE } },
    rows: [new TableRow({ children: [new TableCell({ width: { size: 9200, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: 'FBF8FF' }, margins: { top: 100, bottom: 100, left: 140, right: 140 },
      children: [p({ children: [run('NA EKRANIE:  ', { bold: true, size: 18, color: PURPLE }), run(s.plansza, { size: 19 })] })] })] })],
  }));
  kids.push(p({ spacing: { before: 160, after: 60 },
    children: [run('Narracja', { size: 18, bold: true, color: GREY, characterSpacing: 20 })] }));
  s.narracja.forEach(t => kids.push(p({ spacing: { after: 110, line: 300 },
    children: [run(t, { size: 22 })] })));
});

// ---------- zakończenie ----------
kids.push(p({ children: [new PageBreak()] }));
kids.push(p({ spacing: { after: 140 }, children: [run('Materiały dla uczestników', { size: 26, bold: true, color: PURPLE })] }));
[
  'Broszura „Sala, która uczy każde dziecko” — strony 30–31 (spektrum autyzmu i ADHD), 20–29 (trzy poziomy wsparcia), 41–48 (arkusze monitoringu sali).',
  'Arkusz A — monitoring pięciu stref, do wypełnienia po szkoleniu w każdej sali.',
  'Karta obserwacji dziecka w przestrzeni sali — jako uzupełnienie WOPFU.',
  'Gotowe zapisy do WOPFU i IPET ze sceny 14 — do skopiowania do dokumentacji dziecka.',
].forEach(t => kids.push(p({ spacing: { after: 90 }, indent: { left: 340, hanging: 220 },
  children: [run('•  ', { color: ORANGE, bold: true }), run(t, { size: 20 })] })));

kids.push(p({ spacing: { before: 320, after: 140 }, children: [run('Zadanie wdrożeniowe po szkoleniu', { size: 26, bold: true, color: PURPLE })] }));
kids.push(p({ spacing: { after: 110, line: 300 }, children: [run(
  'W ciągu tygodnia po szkoleniu każdy zespół przechodzi swoją salę na wysokości oczu dziecka, wypełnia Arkusz A i wybiera jedną zmianę do wprowadzenia. Po czterech tygodniach zespół spotyka się ponownie i sprawdza tym samym arkuszem, czy zmiana zadziałała.',
  { size: 22 })] }));

kids.push(p({ spacing: { before: 400 },
  border: { top: { style: BorderStyle.SINGLE, size: 8, color: LINE, space: 8 } },
  children: [run('Autorka: Mirosława Ewa Jurczyszyn, pedagog specjalny', { size: 19, bold: true, color: PURPLE })] }));
kids.push(p({ children: [run('EduPlaner 2026 · PCTP Koszalin — Pomorskie Centrum Terapii Pedagogicznej', { size: 19, color: GREY })] }));
kids.push(p({ children: [run('kontakt@eduplaner2026.pl · 662 888 403', { size: 19, color: GREY })] }));

const doc = new Document({
  styles: { default: { document: { run: { font: F, size: 22 } } } },
  sections: [{
    properties: { page: { margin: { top: 1000, bottom: 1000, left: 1100, right: 1100 } } },
    footers: { default: new Footer({ children: [p({ alignment: AlignmentType.RIGHT,
      children: [run('Sala, która uczy każde dziecko · scenariusz szkolenia · ', { size: 16, color: GREY }),
                 new TextRun({ children: [PageNumber.CURRENT], font: F, size: 16, color: PURPLE, bold: true })] })] }) },
    children: kids,
  }],
});
Packer.toBuffer(doc).then(b => { fs.writeFileSync('Scenariusz_szkolenia_autyzm_20min.docx', b); console.log('OK'); });
