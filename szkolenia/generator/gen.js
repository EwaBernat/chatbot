const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, BorderStyle,
  Table, TableRow, TableCell, WidthType, ShadingType, VerticalAlign, PageBreak,
  Header, Footer, PageNumber, LevelFormat, convertInchesToTwip, TableLayoutType
} = require('docx');
const fs = require('fs');

const PURPLE = '2D1B69';
const ORANGE = 'E8450A';
const GREY   = '4A4A4A';
const LIGHT  = 'F2F0F7';
const LIGHTO = 'FDF0EA';
const LINE   = 'D6D1E4';
const FONT   = 'Arial';

const CONTENT = 9360; // A4 minus 1" margins, in DXA
const INNER   = 8880; // szerokosc uzyteczna wewnatrz ramki box()

// ---------- helpers ----------
const t = (text, o = {}) => new TextRun({ text, font: FONT, size: o.size || 20, bold: !!o.bold,
  italics: !!o.i, color: o.color || '1A1A1A', allCaps: !!o.caps, characterSpacing: o.sp || 0 });

const p = (text, o = {}) => new Paragraph({
  alignment: o.align || AlignmentType.JUSTIFIED,
  spacing: { before: o.before === undefined ? 60 : o.before, after: o.after === undefined ? 60 : o.after,
             line: o.line || 264 },
  indent: o.indent,
  border: o.border,
  shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: 'auto' } : undefined,
  children: Array.isArray(text) ? text : [t(text, o)],
});

const H1 = (num, text) => new Paragraph({
  spacing: { before: 320, after: 160 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 6 } },
  children: [
    t(num + '  ', { bold: true, size: 28, color: ORANGE }),
    t(text, { bold: true, size: 28, color: PURPLE }),
  ],
});

const H2 = (text) => new Paragraph({
  spacing: { before: 240, after: 100 },
  children: [t(text, { bold: true, size: 22, color: PURPLE })],
});

const H3 = (text) => new Paragraph({
  spacing: { before: 160, after: 70 },
  children: [t(text, { bold: true, size: 20, color: ORANGE })],
});

const bullet = (text, o = {}) => new Paragraph({
  numbering: { reference: 'kropki', level: 0 },
  spacing: { before: 40, after: 40, line: 260 },
  alignment: AlignmentType.JUSTIFIED,
  children: Array.isArray(text) ? text : [t(text, o)],
});

const numItem = (text, ref) => new Paragraph({
  numbering: { reference: ref || 'kroki', level: 0 },
  spacing: { before: 40, after: 40, line: 260 },
  alignment: AlignmentType.JUSTIFIED,
  children: Array.isArray(text) ? text : [t(text)],
});

// kolejne linie musza roznic sie kolorem obramowania - inaczej Word/LO scala je w jedna
const lines = (n, o = {}) => Array.from({ length: n || 3 }, (_, i) => new Paragraph({
  spacing: { before: (o.gap || 150), after: 0 },
  border: { bottom: { style: BorderStyle.DOTTED, size: 6,
    color: (i % 2 ? (o.color2 || 'C2C2C2') : (o.color || 'BEBEBE')), space: 3 } },
  children: [t(' ')],
}));

const spacer = (h) => new Paragraph({ spacing: { before: 0, after: h || 80 }, children: [t('')] });
const pageBreak = () => new Paragraph({ children: [new PageBreak()] });

// coloured callout box (single-cell table)
function box(titleText, bodyParas, opts = {}) {
  const fill = opts.fill || LIGHT;
  const bar  = opts.bar  || PURPLE;
  const kids = [];
  if (titleText) {
    kids.push(new Paragraph({
      spacing: { before: 20, after: 90 },
      children: [t(titleText, { bold: true, size: 20, color: bar, caps: !!opts.caps, sp: opts.caps ? 12 : 0 })],
    }));
  }
  bodyParas.forEach(x => kids.push(x));
  return new Table({
    width: { size: CONTENT, type: WidthType.DXA },
    columnWidths: [CONTENT],
    layout: TableLayoutType.FIXED,
    borders: {
      top:    { style: BorderStyle.SINGLE, size: 2,  color: fill },
      bottom: { style: BorderStyle.SINGLE, size: 2,  color: fill },
      right:  { style: BorderStyle.SINGLE, size: 2,  color: fill },
      left:   { style: BorderStyle.SINGLE, size: 18, color: bar },
      insideHorizontal: { style: BorderStyle.NONE, size: 0, color: fill },
      insideVertical:   { style: BorderStyle.NONE, size: 0, color: fill },
    },
    rows: [ new TableRow({ children: [ new TableCell({
      width: { size: CONTENT, type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill, color: 'auto' },
      margins: { top: 140, bottom: 140, left: 200, right: 180 },
      children: kids,
    })]})],
  });
}

// generic data table: head = [str], rows = [[str|Paragraph[]]], widths = [ints summing CONTENT]
function table(head, rows, widths, opts = {}) {
  const zebra = opts.zebra !== false;
  const cellP = (v, o) => Array.isArray(v) ? v : [new Paragraph({
    spacing: { before: 50, after: 50, line: 250 },
    alignment: o.align || AlignmentType.LEFT,
    children: [t(String(v), { size: o.size || 18, bold: !!o.bold, color: o.color || '1A1A1A' })],
  })];
  const trs = [];
  if (head) {
    trs.push(new TableRow({
      tableHeader: true,
      children: head.map((h, i) => new TableCell({
        width: { size: widths[i], type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: PURPLE, color: 'auto' },
        margins: { top: 90, bottom: 90, left: 120, right: 120 },
        verticalAlign: VerticalAlign.CENTER,
        children: cellP(h, { size: 17, bold: true, color: 'FFFFFF' }),
      })),
    }));
  }
  rows.forEach((r, ri) => {
    trs.push(new TableRow({
      cantSplit: true,
      children: r.map((c, i) => new TableCell({
        width: { size: widths[i], type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: (zebra && ri % 2 === 1) ? 'F7F6FA' : 'FFFFFF', color: 'auto' },
        margins: { top: 90, bottom: 90, left: 120, right: 120 },
        verticalAlign: VerticalAlign.TOP,
        children: cellP(c, { size: 18, bold: (opts.boldCol0 && i === 0) }),
      })),
    }));
  });
  return new Table({
    width: { size: CONTENT, type: WidthType.DXA },
    columnWidths: widths,
    layout: TableLayoutType.FIXED,
    borders: {
      top:    { style: BorderStyle.SINGLE, size: 4, color: LINE },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: LINE },
      left:   { style: BorderStyle.SINGLE, size: 4, color: LINE },
      right:  { style: BorderStyle.SINGLE, size: 4, color: LINE },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 2, color: LINE },
      insideVertical:   { style: BorderStyle.SINGLE, size: 2, color: LINE },
    },
    rows: trs,
  });
}

// tabela wewnatrz ramki box() - skalowana do INNER
function tableIn(head, rows, widths, opts = {}) {
  const sum = widths.reduce((a, b) => a + b, 0);
  const scaled = widths.map(w => Math.round(w * INNER / sum));
  scaled[scaled.length - 1] = INNER - scaled.slice(0, -1).reduce((a, b) => a + b, 0);
  const tb = table(head, rows, scaled, opts);
  
  return tb;
}

// module banner
function modul(kod, tytul, czas, cel) {
  return new Table({
    width: { size: CONTENT, type: WidthType.DXA },
    columnWidths: [1500, CONTENT - 1500 - 1500, 1500],
    layout: TableLayoutType.FIXED,
    borders: {
      top: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      bottom: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      left: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      right: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      insideHorizontal: { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' },
      insideVertical: { style: BorderStyle.SINGLE, size: 4, color: 'FFFFFF' },
    },
    rows: [ new TableRow({ children: [
      new TableCell({
        width: { size: 1500, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: ORANGE, color: 'auto' },
        margins: { top: 130, bottom: 130, left: 100, right: 100 },
        verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 },
          children: [t(kod, { bold: true, size: 22, color: 'FFFFFF' })] })],
      }),
      new TableCell({
        width: { size: CONTENT - 3000, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: PURPLE, color: 'auto' },
        margins: { top: 130, bottom: 130, left: 200, right: 140 },
        verticalAlign: VerticalAlign.CENTER,
        children: [
          new Paragraph({ spacing: { before: 0, after: 30 }, children: [t(tytul, { bold: true, size: 22, color: 'FFFFFF' })] }),
          new Paragraph({ spacing: { before: 0, after: 0 }, children: [t('Cel: ' + cel, { size: 16, color: 'D9D3EA' })] }),
        ],
      }),
      new TableCell({
        width: { size: 1500, type: WidthType.DXA },
        shading: { type: ShadingType.CLEAR, fill: PURPLE, color: 'auto' },
        margins: { top: 130, bottom: 130, left: 100, right: 120 },
        verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { before: 0, after: 0 },
          children: [t(czas, { bold: true, size: 20, color: 'FFFFFF' })] })],
      }),
    ]})],
  });
}

// "Strażnik Prawa" card
function straznik(nr, tytul, paras) {
  return box('STRAŻNIK PRAWA · KARTA ' + nr + '  —  ' + tytul, paras, { fill: LIGHTO, bar: ORANGE });
}

const cw = (nazwa, paras) => box('ĆWICZENIE · ' + nazwa, paras, { fill: LIGHT, bar: PURPLE });

module.exports = { Document, Packer, Paragraph, TextRun, AlignmentType, BorderStyle, Table, TableRow,
  TableCell, WidthType, ShadingType, VerticalAlign, PageBreak, Header, Footer, PageNumber, LevelFormat,
  fs, PURPLE, ORANGE, GREY, LIGHT, LIGHTO, LINE, FONT, CONTENT, t, p, H1, H2, H3, bullet, numItem,
  spacer, lines, pageBreak, box, table, tableIn, modul, straznik, cw, INNER, HeadingLevel, TableLayoutType };
