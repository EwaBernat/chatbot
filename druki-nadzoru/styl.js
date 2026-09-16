/* ============================================================================
 * styl.js — wspólne helpery typograficzne druków nadzoru pedagogicznego
 * Ekosystem EduPlaner2026-MJ-PCTP · Pomorskie Centrum Terapii Pedagogicznej
 * Konwencje wg references/document_style.md (A4, Arial, fiolet + pomarańcz)
 * ========================================================================== */

const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, BorderStyle, WidthType, ShadingType,
  PageNumber, PageBreak, TabStopType, HeadingLevel, LevelFormat,
} = require("docx");

/* ---- marka ------------------------------------------------------------ */
const BRAND = {
  purple:     "2D1B69",
  orange:     "E8450A",
  green:      "0D7D5C",
  red:        "B8350D",
  amber:      "C47A10",
  teal:       "2B6E6E",
  muted:      "6B6378",
  rule:       "D8D2C5",
  paper:      "FBF9F4",
  ink:        "1A1530",
  purpleMist: "F3F1FB",
  orangeMist: "FEF0E8",
  white:      "FFFFFF",
};

const F = "Arial";

/* ---- wymiary A4 (DXA) ------------------------------------------------- */
const PAGE = { width: 11906, height: 16838 };
const MAR = { top: 1300, right: 1080, bottom: 1240, left: 1080 };
const CONTENT_W = PAGE.width - MAR.left - MAR.right; // 9746
const TAB_RIGHT = 9740;

/* ---- run / paragraf --------------------------------------------------- */
const run = (text, o = {}) =>
  new TextRun({
    text: String(text ?? ""),
    font: F,
    size: o.size || 20,
    bold: !!o.bold,
    italics: !!o.italic,
    color: o.color || BRAND.ink,
    allCaps: !!o.caps,
    underline: o.underline ? {} : undefined,
  });

const para = (text, o = {}) =>
  new Paragraph({
    alignment: o.align || AlignmentType.LEFT,
    spacing: { before: o.before ?? 0, after: o.after ?? 100, line: o.line || 264 },
    indent: o.indent ? { left: o.indent } : undefined,
    ...(o.numbering ? { numbering: o.numbering } : {}),
    children: Array.isArray(text) ? text : [run(text, o)],
  });

/* pusty odstęp pionowy */
const spacer = (h = 120) => new Paragraph({ spacing: { before: 0, after: h }, children: [] });

/* separator poziomy */
const divider = (color = BRAND.purple, size = 12) =>
  new Paragraph({
    spacing: { before: 80, after: 160 },
    border: { bottom: { style: BorderStyle.SINGLE, size, color, space: 1 } },
    children: [],
  });

/* ---- nagłówki --------------------------------------------------------- */
/* Tytuł druku na pierwszej stronie: nadtytuł + tytuł + podtytuł */
function blokTytulowy({ kicker, tytul, podtytul }) {
  const out = [];
  if (kicker)
    out.push(
      new Paragraph({
        spacing: { before: 0, after: 60 },
        children: [run(kicker, { size: 16, bold: true, caps: true, color: BRAND.orange })],
      })
    );
  out.push(
    new Paragraph({
      spacing: { before: 0, after: podtytul ? 60 : 120 },
      children: [run(tytul, { size: 34, bold: true, color: BRAND.purple })],
    })
  );
  if (podtytul)
    out.push(
      new Paragraph({
        spacing: { before: 0, after: 120 },
        children: [run(podtytul, { size: 18, italic: true, color: BRAND.muted })],
      })
    );
  out.push(divider(BRAND.orange, 16));
  return out;
}

/* Sekcja rzymska: I. TYTUŁ — fioletowy, z pomarańczową krawędzią dolną */
function sekcja(numeral, tytul) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 300, after: 140 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: BRAND.orange, space: 4 } },
    children: [
      run(numeral + ".  ", { size: 26, bold: true, color: BRAND.orange }),
      run(tytul.toUpperCase(), { size: 24, bold: true, color: BRAND.purple }),
    ],
  });
}

/* Podsekcja */
const podsekcja = (tytul) =>
  new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 200, after: 90 },
    children: [run(tytul, { size: 21, bold: true, color: BRAND.purple })],
  });

/* Etykieta pomocnicza (UPPERCASE, pomarańczowa) */
const etykieta = (text, o = {}) =>
  new Paragraph({
    spacing: { before: o.before ?? 120, after: o.after ?? 50 },
    children: [run(text.toUpperCase(), { size: 15, bold: true, color: BRAND.orange })],
  });

/* ---- pola do wypełnienia --------------------------------------------- */
/* Linia do wpisu: "Etykieta: ______________" (linia = dolna krawędź paragrafu) */
const poleLinia = (label, o = {}) =>
  new Paragraph({
    spacing: { before: o.before ?? 140, after: o.after ?? 40 },
    border: { bottom: { style: BorderStyle.DOTTED, size: 6, color: BRAND.rule, space: 6 } },
    children: [run(label ? label + ": " : "", { size: 17, bold: true, color: BRAND.muted })],
  });

/* n pustych linii do odręcznego wypełnienia */
function linie(n = 3, o = {}) {
  const out = [];
  for (let i = 0; i < n; i++) {
    out.push(
      new Paragraph({
        spacing: { before: i === 0 ? (o.before ?? 60) : 0, after: o.gap ?? 150 },
        border: { bottom: { style: BorderStyle.DOTTED, size: 6, color: BRAND.rule, space: 6 } },
        children: [],
      })
    );
  }
  return out;
}

/* Pole opisowe z etykietą + linie */
const poleOpisowe = (label, n = 3, o = {}) => [etykieta(label, o), ...linie(n, o)];

/* Kratka wyboru */
const KRATKA = "□";
const kratki = (opcje, o = {}) =>
  opcje.map((t) =>
    new Paragraph({
      spacing: { before: 0, after: o.after ?? 70 },
      indent: { left: o.indent ?? 180 },
      children: [
        run(KRATKA + "   ", { size: 22, color: BRAND.orange }),
        run(t, { size: o.size || 19, color: BRAND.ink }),
      ],
    })
  );

/* Kratki w jednym wierszu, np. TAK / NIE / NIE DOTYCZY */
const kratkiWiersz = (opcje, o = {}) =>
  new Paragraph({
    spacing: { before: o.before ?? 60, after: o.after ?? 90 },
    indent: { left: o.indent ?? 180 },
    children: opcje.flatMap((t, i) => [
      run((i ? "      " : "") + KRATKA + "  ", { size: 21, color: BRAND.orange }),
      run(t, { size: o.size || 19, color: BRAND.ink }),
    ]),
  });

/* Lista punktowana (bez ręcznych bulletów — przez numbering) */
const punkt = (text, reference = "dot", o = {}) =>
  new Paragraph({
    numbering: { reference, level: 0 },
    spacing: { before: 0, after: o.after ?? 70, line: 264 },
    children: [run(text, { size: o.size || 19, color: o.color || BRAND.ink, bold: o.bold, italic: o.italic })],
  });

const NUMEROWANIE = {
  config: [
    {
      reference: "dot",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "▪", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 540, hanging: 300 } }, run: { color: BRAND.purple, bold: true } },
      }],
    },
    {
      reference: "check",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "●", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 540, hanging: 300 } }, run: { color: BRAND.green, bold: true } },
      }],
    },
    {
      reference: "law",
      levels: [{
        level: 0, format: LevelFormat.BULLET, text: "§", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 540, hanging: 300 } }, run: { color: BRAND.amber, bold: true } },
      }],
    },
    {
      reference: "num",
      levels: [{
        level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 540, hanging: 300 } }, run: { color: BRAND.orange, bold: true } },
      }],
    },
  ],
};

/* ---- tabele ----------------------------------------------------------- */
const cell = (text, o = {}) =>
  new TableCell({
    width: { size: o.width, type: WidthType.DXA },
    columnSpan: o.span || undefined,
    rowSpan: o.rowSpan || undefined,
    shading: o.bg ? { fill: o.bg, type: ShadingType.CLEAR, color: "auto" } : undefined,
    margins: { top: o.padTop ?? 90, bottom: o.padBottom ?? 90, left: 130, right: 130 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: BRAND.rule },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: BRAND.rule },
      left: { style: BorderStyle.SINGLE, size: 4, color: BRAND.rule },
      right: { style: BorderStyle.SINGLE, size: 4, color: BRAND.rule },
    },
    verticalAlign: o.vAlign || "top",
    children: Array.isArray(text)
      ? text
      : [
          new Paragraph({
            spacing: { before: 0, after: 0, line: 252 },
            alignment: o.align || AlignmentType.LEFT,
            children: [run(text, {
              size: o.size || 17, bold: o.bold, italic: o.italic,
              color: o.color || BRAND.ink, caps: o.caps,
            })],
          }),
        ],
  });

const naglowekKom = (text, width, o = {}) =>
  cell(text, { width, bg: BRAND.purple, color: BRAND.white, bold: true, size: o.size || 15, caps: true, align: o.align, span: o.span });

const tabela = (rows, widths) =>
  new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows,
  });

/* Tabela z pustymi wierszami do wypełnienia */
function tabelaDoWypelnienia(naglowki, widths, pusteWierszy = 5, wysokosc = 260) {
  const rows = [new TableRow({
    tableHeader: true,
    children: naglowki.map((h, i) => naglowekKom(h, widths[i])),
  })];
  for (let r = 0; r < pusteWierszy; r++) {
    rows.push(new TableRow({
      children: widths.map((w, i) =>
        cell("", { width: w, padTop: wysokosc / 2, padBottom: wysokosc / 2, bg: r % 2 ? BRAND.paper : undefined })
      ),
    }));
  }
  return tabela(rows, widths);
}

/* Wiersz etykieta | pole do wpisu */
const wierszPola = (label, widths, o = {}) =>
  new TableRow({
    children: [
      cell(label, { width: widths[0], bg: BRAND.purpleMist, bold: true, size: 16, color: BRAND.purple, caps: true }),
      cell(o.value || "", { width: widths[1], span: o.span, padTop: o.pad ?? 110, padBottom: o.pad ?? 110 }),
    ],
  });

/* ---- pudełka tematyczne ---------------------------------------------- */
function pudelko(tekst, o = {}) {
  const linie = Array.isArray(tekst) ? tekst : [tekst];
  return linie.map((t, i) =>
    new Paragraph({
      spacing: { before: i === 0 ? (o.before ?? 120) : 0, after: i === linie.length - 1 ? (o.after ?? 140) : 60, line: 264 },
      shading: { fill: o.bg || BRAND.purpleMist, type: ShadingType.CLEAR, color: "auto" },
      border: { left: { style: BorderStyle.SINGLE, size: 24, color: o.accent || BRAND.orange, space: 10 } },
      indent: { left: 60, right: 60 },
      children: [run(t, { size: o.size || 18, italic: o.italic !== false, color: o.color || BRAND.purple, bold: o.bold })],
    })
  );
}

/* Blok podstawy prawnej */
function podstawaPrawna(pozycje, o = {}) {
  return [
    etykieta("Podstawa prawna", { before: o.before ?? 200 }),
    ...pozycje.map((t) =>
      new Paragraph({
        numbering: { reference: "law", level: 0 },
        spacing: { before: 0, after: 60, line: 252 },
        children: [run(t, { size: 15, color: BRAND.amber })],
      })
    ),
  ];
}

/* ---- podpisy ---------------------------------------------------------- */
function komPodpisu(rola, width, span) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    columnSpan: span || undefined,
    margins: { top: 900, bottom: 80, left: 100, right: 100 },
    borders: {
      top: { style: BorderStyle.SINGLE, size: 6, color: BRAND.ink },
      left: { style: BorderStyle.NIL },
      right: { style: BorderStyle.NIL },
      bottom: { style: BorderStyle.NIL },
    },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: [run(rola, { size: 15, bold: true, italic: true, color: BRAND.purple })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, children: [run("podpis i data", { size: 12, color: BRAND.muted })] }),
    ],
  });
}

function blokPodpisow(role, o = {}) {
  const szer = Math.floor(CONTENT_W / role.length);
  const widths = role.map((_, i) => (i === role.length - 1 ? CONTENT_W - szer * (role.length - 1) : szer));
  return [
    spacer(o.before ?? 260),
    new Table({
      width: { size: CONTENT_W, type: WidthType.DXA },
      columnWidths: widths,
      rows: [new TableRow({ children: role.map((r, i) => komPodpisu(r, widths[i])) })],
    }),
  ];
}

/* ---- nagłówek i stopka strony ---------------------------------------- */
function naglowekStrony({ modul, kodDruku }) {
  return new Header({
    children: [
      new Paragraph({
        spacing: { before: 0, after: 0 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 8, color: BRAND.purple, space: 4 } },
        tabStops: [{ type: TabStopType.RIGHT, position: TAB_RIGHT }],
        children: [
          run("EduPlaner2026-MJ-PCTP", { size: 15, bold: true, color: BRAND.purple }),
          run("  ·  ", { size: 15, color: BRAND.rule }),
          run(modul, { size: 15, bold: true, color: BRAND.orange, caps: true }),
          run("\t"),
          run("Druk ", { size: 13, color: BRAND.muted }),
          run(kodDruku, { size: 13, bold: true, color: BRAND.purple }),
        ],
      }),
    ],
  });
}

function stopkaStrony({ tytul }) {
  return new Footer({
    children: [
      new Paragraph({
        spacing: { before: 60, after: 0 },
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: BRAND.rule, space: 4 } },
        tabStops: [{ type: TabStopType.RIGHT, position: TAB_RIGHT }],
        children: [
          run(tytul, { size: 12, color: BRAND.muted }),
          run("   ·   ", { size: 12, color: BRAND.rule }),
          run("Dokument wewnętrzny · RODO", { size: 12, color: BRAND.muted }),
          run("\t"),
          run("Strona ", { size: 12, color: BRAND.muted }),
          new TextRun({ children: [PageNumber.CURRENT], font: F, size: 12, bold: true, color: BRAND.orange }),
          run(" z ", { size: 12, color: BRAND.muted }),
          new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F, size: 12, bold: true, color: BRAND.purple }),
        ],
      }),
    ],
  });
}

/* ---- złożenie dokumentu ---------------------------------------------- */
function dokument({ modul, kodDruku, tytul, children }) {
  return new Document({
    creator: "EduPlaner2026-MJ-PCTP",
    title: tytul,
    description: "Druk nadzoru pedagogicznego · PCTP Koszalin",
    numbering: NUMEROWANIE,
    styles: {
      default: {
        document: { run: { font: F, size: 20, color: BRAND.ink } },
      },
    },
    sections: [{
      properties: { page: { size: { width: PAGE.width, height: PAGE.height }, margin: MAR } },
      headers: { default: naglowekStrony({ modul, kodDruku }) },
      footers: { default: stopkaStrony({ tytul }) },
      children,
    }],
  });
}

const nowaStrona = () => new Paragraph({ spacing: { before: 0, after: 0 }, children: [new PageBreak()] });

module.exports = {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, HeadingLevel,
  BRAND, F, PAGE, MAR, CONTENT_W, TAB_RIGHT,
  run, para, spacer, divider, blokTytulowy, sekcja, podsekcja, etykieta,
  poleLinia, linie, poleOpisowe, kratki, kratkiWiersz, punkt, KRATKA,
  cell, naglowekKom, tabela, tabelaDoWypelnienia, wierszPola,
  pudelko, podstawaPrawna, komPodpisu, blokPodpisow, dokument, nowaStrona,
};
