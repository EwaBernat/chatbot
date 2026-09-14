#!/usr/bin/env node
/**
 * Bank rozwiązań do IPE — generator dokumentów Word
 * Forma: EduPlaner2026-MJ-PCTP (fiolet #2D1B69 + pomarańcz #E8450A, Arial, A4)
 *
 * Użycie:  node generate_bank.js [1] [2] [3] [4]     (bez argumentów = wszystkie obszary)
 */
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, LevelFormat, HeadingLevel, BorderStyle, WidthType,
  ShadingType, PageBreak, TabStopType, Header, Footer, PageNumber, VerticalAlign
} = require(process.env.DOCX_PATH || 'docx');

/* ─────────────────────────── Stałe marki ─────────────────────────── */

const FONT = 'Arial';
const BRAND = 'EduPlaner2026-MJ-PCTP';
const AUTOR = 'mgr Mirosława Jurczyszyn';
const PLACOWKA = 'PCTP Koszalin · Pomorskie Centrum Terapii Pedagogicznej';
const WERSJA = 'wyd. 2026';

const A4 = { width: 11906, height: 16838 };
const MARGINS = { top: 1440, right: 1080, bottom: 1440, left: 1080 };
const W = 9746;           // szerokość obszaru treści
const TAB_RIGHT = 9740;

const COLOR = {
  purple:     '2D1B69',
  orange:     'E8450A',
  green:      '0D7D5C',
  red:        'B8350D',
  amber:      'C47A10',
  teal:       '2B6E6E',
  muted:      '6B6378',
  rule:       'D8D2C5',
  paper:      'FBF9F4',
  ink:        '1A1530',
  purpleMist: 'F3F1FB',
  orangeMist: 'FEF0E8',
  white:      'FFFFFF'
};

/* ─────────────────────────── Helpery ─────────────────────────── */

const para = (text, opts = {}) => new Paragraph({
  spacing: { before: opts.before || 0, after: opts.after === undefined ? 120 : opts.after, line: opts.line || 280 },
  alignment: opts.align || AlignmentType.LEFT,
  ...(opts.numbering ? { numbering: opts.numbering } : {}),
  ...(opts.shading ? { shading: { fill: opts.shading, type: ShadingType.CLEAR, color: 'auto' } } : {}),
  ...(opts.border ? { border: opts.border } : {}),
  children: [new TextRun({
    text: text || '', font: FONT,
    size: opts.size || 20,
    bold: opts.bold || false,
    italics: opts.italic || false,
    allCaps: opts.caps || false,
    characterSpacing: opts.spacing || 0,
    color: opts.color || COLOR.ink
  })]
});

const runs = (children, opts = {}) => new Paragraph({
  spacing: { before: opts.before || 0, after: opts.after === undefined ? 120 : opts.after, line: opts.line || 280 },
  alignment: opts.align || AlignmentType.LEFT,
  ...(opts.shading ? { shading: { fill: opts.shading, type: ShadingType.CLEAR, color: 'auto' } } : {}),
  ...(opts.border ? { border: opts.border } : {}),
  children
});

const run = (text, opts = {}) => new TextRun({
  text: text || '', font: FONT,
  size: opts.size || 20,
  bold: opts.bold || false,
  italics: opts.italic || false,
  allCaps: opts.caps || false,
  characterSpacing: opts.spacing || 0,
  color: opts.color || COLOR.ink
});

const noBorders = {
  top: { style: BorderStyle.NIL }, bottom: { style: BorderStyle.NIL },
  left: { style: BorderStyle.NIL }, right: { style: BorderStyle.NIL }
};
const ruleBorders = (color = COLOR.rule) => ({
  top: { style: BorderStyle.SINGLE, size: 4, color },
  bottom: { style: BorderStyle.SINGLE, size: 4, color },
  left: { style: BorderStyle.SINGLE, size: 4, color },
  right: { style: BorderStyle.SINGLE, size: 4, color }
});

const cellOf = (children, opts = {}) => new TableCell({
  width: { size: opts.width, type: WidthType.DXA },
  ...(opts.span ? { columnSpan: opts.span } : {}),
  ...(opts.bg ? { shading: { fill: opts.bg, type: ShadingType.CLEAR, color: 'auto' } } : {}),
  margins: opts.margins || { top: 100, bottom: 100, left: 140, right: 140 },
  borders: opts.borders || ruleBorders(),
  verticalAlign: opts.vAlign || VerticalAlign.TOP,
  children
});

const cell = (text, opts = {}) => cellOf([para(text, {
  after: 0, line: 260,
  size: opts.size || 18, bold: opts.bold, italic: opts.italic, caps: opts.caps,
  color: opts.color || COLOR.ink, align: opts.align, spacing: opts.spacing
})], opts);

const headerCell = (text, width, span) => cell(text, {
  width, span, bg: COLOR.purple, color: COLOR.white,
  bold: true, size: 16, caps: true, spacing: 8,
  borders: ruleBorders(COLOR.purple)
});

const table = (rows, opts = {}) => new Table({
  width: { size: opts.width || W, type: WidthType.DXA },
  columnWidths: opts.columnWidths,
  rows
});

/** Pasek sekcji — pełna szerokość, purpurowe tło, białe kapitaliki. */
const sectionBar = (text, accent = COLOR.orange) => table([
  new TableRow({
    children: [
      new TableCell({
        width: { size: 60, type: WidthType.DXA },
        shading: { fill: accent, type: ShadingType.CLEAR, color: 'auto' },
        borders: ruleBorders(accent), margins: { top: 0, bottom: 0, left: 0, right: 0 },
        children: [para('', { after: 0, size: 12 })]
      }),
      cell(text, {
        width: W - 60, bg: COLOR.purple, color: COLOR.white,
        bold: true, size: 16, caps: true, spacing: 10,
        borders: ruleBorders(COLOR.purple),
        margins: { top: 70, bottom: 70, left: 160, right: 140 }
      })
    ]
  })
], { columnWidths: [60, W - 60] });

/** Pudełko treści: tło papierowe + pomarańczowa krawędź z lewej. */
const infoBox = (children, opts = {}) => table([
  new TableRow({
    children: [cellOf(children, {
      width: W, bg: opts.bg || COLOR.paper,
      borders: {
        top: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule },
        bottom: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule },
        left: { style: BorderStyle.SINGLE, size: 18, color: opts.accent || COLOR.orange },
        right: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule }
      },
      margins: { top: 140, bottom: 140, left: 200, right: 180 }
    })]
  })
], { columnWidths: [W] });

const spacer = (h = 80) => new Paragraph({ spacing: { before: 0, after: h }, children: [] });

const divider = (color = COLOR.purple, size = 12) => new Paragraph({
  spacing: { before: 80, after: 160 },
  border: { bottom: { style: BorderStyle.SINGLE, size, color, space: 1 } },
  children: []
});

/** Etykieta „POMOCE: treść" w jednym akapicie. */
const labelRun = (label, value, opts = {}) => runs([
  run(label.toUpperCase() + ': ', { size: 16, bold: true, color: opts.labelColor || COLOR.orange, spacing: 6 }),
  run(value || '—', { size: 18, color: COLOR.ink })
], { after: opts.after === undefined ? 60 : opts.after, line: 260 });

/* ─────────────────── Poziomy wsparcia (badge + opis) ─────────────────── */

const LEVEL_STYLE = [
  { name: 'ZNACZNE',      color: COLOR.red,   bg: 'F7E6E0' },
  { name: 'UMIARKOWANE',  color: COLOR.amber, bg: 'FBF2DF' },
  { name: 'NISKIE',       color: COLOR.green, bg: 'E2F0EB' }
];

const levelRow = (idx, text) => {
  const st = LEVEL_STYLE[idx] || LEVEL_STYLE[2];
  // "Wsparcie Znaczne: opis" → badge + opis
  const m = text.match(/^\s*Wsparcie\s+\w+\s*:\s*(.*)$/s);
  const opis = m ? m[1] : text;
  return new TableRow({
    children: [
      cellOf([
        para(String(idx + 1), { after: 0, size: 18, bold: true, color: st.color, align: AlignmentType.CENTER }),
        para('WSPARCIE', { after: 0, size: 11, color: COLOR.muted, align: AlignmentType.CENTER, spacing: 8 }),
        para(st.name, { after: 0, size: 13, bold: true, color: st.color, align: AlignmentType.CENTER, spacing: 8 })
      ], {
        width: 1700, bg: st.bg, vAlign: VerticalAlign.CENTER,
        borders: {
          top: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule },
          bottom: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule },
          left: { style: BorderStyle.SINGLE, size: 14, color: st.color },
          right: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule }
        },
        margins: { top: 90, bottom: 90, left: 100, right: 100 }
      }),
      cell(opis, { width: W - 1700, size: 18, vAlign: VerticalAlign.CENTER })
    ]
  });
};

/* ─────────────────────────── Karta celu ─────────────────────────── */

function kartaCelu(k, nrKarty, obszar) {
  const out = [];

  // Nagłówek karty: numer + kod ICF + nazwa
  out.push(table([
    new TableRow({
      children: [
        cellOf([
          para('KARTA', { after: 0, size: 11, color: COLOR.purpleMist, align: AlignmentType.CENTER, spacing: 10 }),
          para(String(nrKarty), { after: 0, size: 32, bold: true, color: COLOR.white, align: AlignmentType.CENTER })
        ], {
          width: 900, bg: COLOR.purple, vAlign: VerticalAlign.CENTER,
          borders: ruleBorders(COLOR.purple), margins: { top: 80, bottom: 100, left: 60, right: 60 }
        }),
        cellOf([
          runs([
            run('KARTA CELU IPE', { size: 14, bold: true, color: COLOR.orange, spacing: 14 }),
            run('   ·   ', { size: 14, color: COLOR.rule }),
            run('KOD ICF', { size: 14, bold: true, color: COLOR.muted, spacing: 14 })
          ], { after: 40 }),
          runs([
            run(k.kod + '  ', { size: 26, bold: true, color: COLOR.orange }),
            run(k.nazwa, { size: 26, bold: true, color: COLOR.purple })
          ], { after: k.podtytul ? 40 : 0, line: 300 }),
          ...(k.podtytul ? [para(k.podtytul, { after: 0, size: 17, italic: true, color: COLOR.muted })] : [])
        ], {
          width: W - 900, bg: COLOR.purpleMist, vAlign: VerticalAlign.CENTER,
          borders: {
            top: { style: BorderStyle.SINGLE, size: 4, color: COLOR.purple },
            bottom: { style: BorderStyle.SINGLE, size: 4, color: COLOR.purple },
            left: { style: BorderStyle.NIL },
            right: { style: BorderStyle.SINGLE, size: 4, color: COLOR.purple }
          },
          margins: { top: 130, bottom: 130, left: 200, right: 160 }
        })
      ]
    })
  ], { columnWidths: [900, W - 900] }));

  out.push(spacer(160));

  // I. Problem ↔ Cel SMART
  out.push(table([
    new TableRow({
      tableHeader: true,
      children: [
        headerCell('I.  Problem / trudność', 3800),
        headerCell('II.  Cel szczegółowy (S.M.A.R.T.)', W - 3800)
      ]
    }),
    new TableRow({
      children: [
        cell(k.problem, { width: 3800, size: 18, bg: 'FDF6F3', color: COLOR.ink }),
        cell(k.cel, { width: W - 3800, size: 18, bold: false, bg: COLOR.paper })
      ]
    })
  ], { columnWidths: [3800, W - 3800] }));

  out.push(spacer(180));

  // III. Strategia i poziomy wsparcia
  out.push(sectionBar('III.  Strategia i poziomy wsparcia'));
  if (k.strategia) {
    out.push(runs([
      run('STRATEGIA WIODĄCA: ', { size: 15, bold: true, color: COLOR.orange, spacing: 8 }),
      run(k.strategia, { size: 19, bold: true, italic: true, color: COLOR.purple })
    ], { before: 80, after: 80 }));
  } else {
    out.push(spacer(60));
  }
  out.push(table(k.poziomy.map((p, i) => levelRow(i, p)), { columnWidths: [1700, W - 1700] }));

  out.push(spacer(180));

  // IV. Pomoce i metody
  out.push(sectionBar('IV.  Pomoce dydaktyczne i metody', COLOR.green));
  out.push(spacer(60));
  out.push(infoBox([
    labelRun('Pomoce', k.pomoce, { labelColor: COLOR.green }),
    labelRun('Metody', k.metody, { labelColor: COLOR.green, after: 0 })
  ], { accent: COLOR.green }));

  out.push(spacer(180));

  // V. Dostosowania / UDL
  out.push(sectionBar('V.  Dostosowania / projektowanie uniwersalne (UDL)', COLOR.teal));
  out.push(spacer(60));
  out.push(infoBox([
    labelRun('Dostosowania', k.dostosowania, { labelColor: COLOR.teal }),
    labelRun('UDL', k.udl, { labelColor: COLOR.teal, after: 0 })
  ], { accent: COLOR.teal, bg: COLOR.purpleMist }));

  out.push(spacer(180));

  // VI. Operacjonalizacja
  out.push(sectionBar('VI.  Operacjonalizacja (kroki do realizacji)'));
  out.push(spacer(60));
  out.push(table(k.kroki.map((krok, i) => new TableRow({
    children: [
      cellOf([
        para('KROK', { after: 0, size: 11, color: COLOR.muted, align: AlignmentType.CENTER, spacing: 8 }),
        para(String(i + 1), { after: 0, size: 20, bold: true, color: COLOR.orange, align: AlignmentType.CENTER })
      ], {
        width: 1000, bg: COLOR.orangeMist, vAlign: VerticalAlign.CENTER,
        borders: {
          top: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule },
          bottom: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule },
          left: { style: BorderStyle.SINGLE, size: 14, color: COLOR.orange },
          right: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule }
        },
        margins: { top: 80, bottom: 80, left: 80, right: 80 }
      }),
      cell(krok, { width: W - 1000, size: 18, vAlign: VerticalAlign.CENTER })
    ]
  })), { columnWidths: [1000, W - 1000] }));

  out.push(spacer(180));

  // VII. Odpowiedzialność i ewaluacja
  out.push(table([
    new TableRow({
      tableHeader: true,
      children: [
        headerCell('VII.  Osoba odpowiedzialna', 4873),
        headerCell('VIII.  Ewaluacja / termin', 4873)
      ]
    }),
    new TableRow({
      children: [
        cell(k.osoba, { width: 4873, size: 19, bold: true, color: COLOR.purple, bg: COLOR.paper }),
        cell(k.ewaluacja, { width: 4873, size: 19, bold: true, color: COLOR.orange, bg: COLOR.orangeMist })
      ]
    }),
    new TableRow({
      children: [
        cell('Podpis osoby odpowiedzialnej / data wdrożenia', {
          width: 4873, size: 13, italic: true, color: COLOR.muted,
          margins: { top: 480, bottom: 100, left: 140, right: 140 }
        }),
        cell('Wynik ewaluacji (osiągnięty / częściowo / kontynuacja)', {
          width: 4873, size: 13, italic: true, color: COLOR.muted,
          margins: { top: 480, bottom: 100, left: 140, right: 140 }
        })
      ]
    })
  ], { columnWidths: [4873, 4873] }));

  return out;
}

/* ─────────────────────────── Okładka ─────────────────────────── */

function okladka(d) {
  const out = [];
  out.push(spacer(600));

  out.push(runs([
    run(BRAND, { size: 18, bold: true, color: COLOR.purple, spacing: 30 })
  ], { after: 40 }));
  out.push(runs([
    run(PLACOWKA, { size: 15, color: COLOR.muted })
  ], { after: 300 }));

  out.push(divider(COLOR.orange, 24));

  out.push(para('BANK ROZWIĄZAŃ', { after: 0, size: 52, bold: true, color: COLOR.purple, line: 560 }));
  out.push(runs([
    run('DO IPE', { size: 52, bold: true, color: COLOR.purple }),
    run('   ·   ', { size: 40, color: COLOR.rule }),
    run('OBSZAR ' + d.nr, { size: 52, bold: true, color: COLOR.orange })
  ], { after: 220, line: 560 }));

  out.push(para(d.obszar, { after: 60, size: 30, bold: true, color: COLOR.ink, line: 380 }));

  out.push(runs([
    run('KODY ICF: ', { size: 16, bold: true, color: COLOR.orange, spacing: 10 }),
    run(d.kody, { size: 20, bold: true, color: COLOR.purple }),
    run('     |     ', { size: 16, color: COLOR.rule }),
    run('ETAP: ', { size: 16, bold: true, color: COLOR.orange, spacing: 10 }),
    run(d.etap, { size: 18, color: COLOR.ink })
  ], { after: 260 }));

  out.push(divider(COLOR.purple, 12));
  out.push(spacer(200));

  // Pudełko instrukcji
  out.push(infoBox([
    para('JAK KORZYSTAĆ Z TEGO BANKU', { after: 100, size: 15, bold: true, color: COLOR.purple, spacing: 14 }),
    ...d.instrukcja.map((t, i) => para(t, {
      after: i === d.instrukcja.length - 1 ? 0 : 60, size: 19, italic: true, color: COLOR.purple
    }))
  ], { bg: COLOR.purpleMist }));

  out.push(spacer(260));

  // Metryka dokumentu
  out.push(table([
    new TableRow({
      tableHeader: true,
      children: [
        headerCell('Liczba kart celu', 2436),
        headerCell('Zakres kodów ICF', 2436),
        headerCell('Wersja', 2437),
        headerCell('Data wydruku', 2437)
      ]
    }),
    new TableRow({
      children: [
        cell(String(d.karty.length), { width: 2436, size: 20, bold: true, color: COLOR.orange, align: AlignmentType.CENTER, bg: COLOR.paper }),
        cell(d.kody, { width: 2436, size: 20, bold: true, color: COLOR.purple, align: AlignmentType.CENTER, bg: COLOR.paper }),
        cell(WERSJA, { width: 2437, size: 18, align: AlignmentType.CENTER, bg: COLOR.paper }),
        cell('....... / ....... / 20.......', { width: 2437, size: 16, color: COLOR.muted, align: AlignmentType.CENTER, bg: COLOR.paper })
      ]
    })
  ], { columnWidths: [2436, 2436, 2437, 2437] }));

  out.push(spacer(400));

  out.push(divider(COLOR.rule, 6));
  out.push(runs([
    run('Opracowanie: ', { size: 15, color: COLOR.muted }),
    run(AUTOR, { size: 15, bold: true, color: COLOR.purple })
  ], { after: 40 }));
  out.push(para('Materiał wspiera zespół w konstruowaniu celów IPE na podstawie WOPFU. Nie zastępuje indywidualnej diagnozy ucznia.',
    { after: 0, size: 14, italic: true, color: COLOR.muted }));

  return out;
}

/* ────────────────── Lista kontrolna (strona 2) ────────────────── */

function listaKontrolna(d) {
  const out = [];
  out.push(runs([
    run('LISTA KONTROLNA', { size: 30, bold: true, color: COLOR.purple })
  ], { after: 40, line: 400 }));
  out.push(para('Kluczowe pytania diagnostyczne — zanim wpiszesz cel do IPE',
    { after: 140, size: 19, italic: true, color: COLOR.muted }));
  out.push(divider(COLOR.orange, 18));
  out.push(spacer(120));

  out.push(table(d.checklist.map((q, i) => new TableRow({
    children: [
      cell(String(i + 1) + '.', {
        width: 640, size: 18, bold: true, color: COLOR.orange, align: AlignmentType.CENTER,
        bg: i % 2 === 0 ? COLOR.paper : COLOR.white, vAlign: VerticalAlign.CENTER,
        margins: { top: 90, bottom: 90, left: 60, right: 60 }
      }),
      cell(q, {
        width: W - 640 - 900, size: 18,
        bg: i % 2 === 0 ? COLOR.paper : COLOR.white, vAlign: VerticalAlign.CENTER,
        margins: { top: 90, bottom: 90, left: 160, right: 140 }
      }),
      cell('TAK  /  NIE', {
        width: 900, size: 13, bold: true, color: COLOR.muted, align: AlignmentType.CENTER,
        bg: i % 2 === 0 ? COLOR.paper : COLOR.white, vAlign: VerticalAlign.CENTER,
        margins: { top: 90, bottom: 90, left: 40, right: 40 }
      })
    ]
  })), { columnWidths: [640, W - 640 - 900, 900] }));

  out.push(spacer(220));
  out.push(infoBox([
    runs([
      run('ZASADA PCTP:  ', { size: 15, bold: true, color: COLOR.orange, spacing: 10 }),
      run('każde „NIE” w tej liście to zadanie do wykonania przed zatwierdzeniem celu przez zespół — nie powód do rezygnacji z celu.',
        { size: 19, italic: true, color: COLOR.purple })
    ], { after: 0 })
  ], { bg: COLOR.purpleMist }));

  return out;
}

/* ────────────────── Spis kart (strona 3) ────────────────── */

function spisKart(d) {
  const out = [];
  out.push(runs([run('SPIS KART CELU', { size: 30, bold: true, color: COLOR.purple })], { after: 40, line: 400 }));
  out.push(para('Wydrukuj tylko te karty, które dotyczą Twojego ucznia.',
    { after: 140, size: 19, italic: true, color: COLOR.muted }));
  out.push(divider(COLOR.orange, 18));
  out.push(spacer(120));

  out.push(table([
    new TableRow({
      tableHeader: true,
      children: [
        headerCell('Karta', 900),
        headerCell('Kod ICF', 1500),
        headerCell('Obszar umiejętności', 4600),
        headerCell('Osoba odpowiedzialna', W - 900 - 1500 - 4600)
      ]
    }),
    ...d.karty.map((k, i) => new TableRow({
      children: [
        cell(String(i + 1), {
          width: 900, size: 18, bold: true, color: COLOR.orange, align: AlignmentType.CENTER,
          bg: i % 2 === 0 ? COLOR.paper : COLOR.white, vAlign: VerticalAlign.CENTER
        }),
        cell(k.kod, {
          width: 1500, size: 18, bold: true, color: COLOR.purple,
          bg: i % 2 === 0 ? COLOR.paper : COLOR.white, vAlign: VerticalAlign.CENTER
        }),
        cellOf([
          para(k.nazwa, { after: k.podtytul ? 30 : 0, size: 18, color: COLOR.ink, line: 250 }),
          ...(k.podtytul ? [para(k.podtytul, { after: 0, size: 14, italic: true, color: COLOR.muted, line: 230 })] : [])
        ], { width: 4600, bg: i % 2 === 0 ? COLOR.paper : COLOR.white, vAlign: VerticalAlign.CENTER }),
        cell(k.osoba, {
          width: W - 900 - 1500 - 4600, size: 16, color: COLOR.muted,
          bg: i % 2 === 0 ? COLOR.paper : COLOR.white, vAlign: VerticalAlign.CENTER
        })
      ]
    }))
  ], { columnWidths: [900, 1500, 4600, W - 900 - 1500 - 4600] }));

  return out;
}

/* ─────────────────────────── Dokument ─────────────────────────── */

function buildDoc(d) {
  const children = [];

  children.push(...okladka(d));
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(...listaKontrolna(d));
  children.push(new Paragraph({ children: [new PageBreak()] }));
  children.push(...spisKart(d));

  d.karty.forEach((k, i) => {
    children.push(new Paragraph({ children: [new PageBreak()] }));
    children.push(...kartaCelu(k, i + 1, d));
  });

  const headerPara = new Paragraph({
    spacing: { before: 0, after: 0 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: COLOR.purple, space: 4 } },
    tabStops: [{ type: TabStopType.RIGHT, position: TAB_RIGHT }],
    children: [
      run(BRAND, { size: 16, bold: true, color: COLOR.purple }),
      run('  ·  ', { size: 16, color: COLOR.rule }),
      run('BANK IPE', { size: 16, bold: true, color: COLOR.orange }),
      new TextRun({ text: '\t', font: FONT }),
      run(d.stopka + '  ·  ', { size: 14, color: COLOR.muted }),
      run(d.kody, { size: 14, bold: true, italics: true, color: COLOR.purple })
    ]
  });

  const footerPara = new Paragraph({
    spacing: { before: 60, after: 0 },
    border: { top: { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule, space: 4 } },
    tabStops: [{ type: TabStopType.RIGHT, position: TAB_RIGHT }],
    children: [
      run('Bank rozwiązań do IPE · ' + WERSJA, { size: 12, color: COLOR.muted }),
      run('   ·   ', { size: 12, color: COLOR.rule }),
      run(AUTOR, { size: 12, color: COLOR.muted }),
      new TextRun({ text: '\t', font: FONT }),
      run('Strona ', { size: 12, color: COLOR.muted }),
      new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 12, bold: true, color: COLOR.orange }),
      run(' z ', { size: 12, color: COLOR.muted }),
      new TextRun({ children: [PageNumber.TOTAL_PAGES], font: FONT, size: 12, bold: true, color: COLOR.purple })
    ]
  });

  return new Document({
    creator: AUTOR,
    title: 'Bank rozwiązań do IPE — Obszar ' + d.nr + ': ' + d.obszar,
    description: BRAND + ' · karty celu IPE dla kodów ICF ' + d.kody,
    styles: { default: { document: { run: { font: FONT, size: 20, color: COLOR.ink } } } },
    numbering: {
      config: [
        { reference: 'check', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } }, run: { color: COLOR.orange, bold: true } } }] },
        { reference: 'steps', levels: [{ level: 0, format: LevelFormat.BULLET, text: '●', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 360 } }, run: { color: COLOR.orange } } }] }
      ]
    },
    sections: [{
      properties: { titlePage: true, page: { size: A4, margin: MARGINS } },
      headers: {
        first: new Header({ children: [new Paragraph({ children: [] })] }),
        default: new Header({ children: [headerPara] })
      },
      footers: {
        first: new Footer({ children: [new Paragraph({ children: [] })] }),
        default: new Footer({ children: [footerPara] })
      },
      children
    }]
  });
}

/* ─────────────────────────── main ─────────────────────────── */

(async () => {
  const args = process.argv.slice(2).filter(a => /^[1-4]$/.test(a));
  const which = args.length ? args : ['1', '2', '3', '4'];
  const outDir = path.join(__dirname, 'out');
  fs.mkdirSync(outDir, { recursive: true });

  for (const n of which) {
    const d = require(path.join(__dirname, 'data', 'obszar' + n + '.js'));
    const buf = await Packer.toBuffer(buildDoc(d));
    const slug = d.obszar.toLowerCase()
      .replace(/ą/g, 'a').replace(/ć/g, 'c').replace(/ę/g, 'e').replace(/ł/g, 'l')
      .replace(/ń/g, 'n').replace(/ó/g, 'o').replace(/ś/g, 's').replace(/[żź]/g, 'z')
      .replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '');
    const file = path.join(outDir, `Bank_IPE_Obszar${d.nr}_${slug}.docx`);
    fs.writeFileSync(file, buf);
    console.log(`✔ ${path.basename(file)}  —  ${d.karty.length} kart celu, ${d.checklist.length} pytań listy kontrolnej`);
  }
})().catch(e => { console.error(e); process.exit(1); });
