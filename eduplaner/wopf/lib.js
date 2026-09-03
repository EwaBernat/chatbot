const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, PageBreak,
  TabStopType, Header, Footer, PageNumber, VerticalAlign
} = require('docx');

const FONT = 'Arial';
const CW = 9746;                 // szerokość kolumny tekstu (DXA)
const C = {
  purple:'2D1B69', purpleMid:'6C4CC4', orange:'E8450A',
  ink:'2B2733', muted:'6F6A7D', soft:'8A7FB0',
  mist:'EFEAF9', mist2:'F6F3FC', paper:'FBFAFF',
  line:'DDD3F1', rule:'CFC2E8', dot:'A294CC', orangeMist:'FFF7F2'
};
const NIL = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const NOB = { top: NIL, left: NIL, bottom: NIL, right: NIL };
const bd = (color, size=4, style=BorderStyle.SINGLE) => ({ style, size, color });

// kolejność krawędzi wymagana przez schemat OOXML: top, left, bottom, right
const ordBorder = (b) => {
  const out = {};
  ['top', 'left', 'bottom', 'right'].forEach(k => { if (b[k]) out[k] = b[k]; });
  return out;
};

const run = (t, o={}) => new TextRun({
  text: t, font: FONT, size: o.size || 20, bold: !!o.bold, italics: !!o.italic,
  color: o.color || C.ink, allCaps: !!o.caps, characterSpacing: o.spacing
});

const P = (children, o={}) => new Paragraph({
  spacing: { before: o.before ?? 0, after: o.after ?? 100, line: o.line || 260 },
  alignment: o.align || AlignmentType.LEFT,
  ...(o.shading ? { shading: { fill: o.shading, type: ShadingType.CLEAR, color: 'auto' } } : {}),
  ...(o.border ? { border: ordBorder(o.border) } : {}),
  ...(o.indent ? { indent: o.indent } : {}),
  ...(o.keepNext ? { keepNext: true } : {}),
  children
});

const text = (t, o={}) => P([run(t, o)], o);

/* ---------- nagłówek / stopka strony ---------- */
const pageHeader = new Header({ children: [
  new Paragraph({
    spacing: { before: 0, after: 40, line: 240 },
    tabStops: [{ type: TabStopType.RIGHT, position: CW }],
    border: { bottom: bd(C.purple, 8) },
    children: [
      run('PCTP', { size: 15, bold: true, color: 'FFFFFF' }),
      run('  ', { size: 15 }),
      run('EduPlaner 2026', { size: 19, bold: true, color: C.purple }),
      run('   ·   ', { size: 15, color: C.line }),
      run('WOPF · przedszkole', { size: 14, bold: true, color: C.soft, caps: true }),
      run('\t'),
      run('  WOPF  ', { size: 15, bold: true, color: 'FFFFFF' }),
      run('   ocena zintegrowana · dokument scalający · 2026', { size: 13, bold: true, color: C.soft })
    ]
  })
]});

const pageFooter = new Footer({ children: [
  new Paragraph({
    spacing: { before: 60, after: 0 },
    tabStops: [{ type: TabStopType.RIGHT, position: CW }],
    border: { top: bd(C.line, 6) },
    children: [
      run('EduPlaner 2026 · PCTP · przedszkole', { size: 13, color: C.muted }),
      run('\t'),
      run('Strona ', { size: 13, color: C.muted }),
      new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 13, bold: true, color: C.orange }),
      run(' · WOPF', { size: 13, bold: true, color: C.purple })
    ]
  })
]});

/* ---------- bloki treści ---------- */

// Nagłówek sekcji: numer rzymski w pomarańczowym kaflu + tytuł + tag
function section(num, title, tag) {
  const cells = [
    new TableCell({
      width: { size: 760, type: WidthType.DXA },
      shading: { fill: C.orange, type: ShadingType.CLEAR, color: 'auto' },
      margins: { top: 70, left: 60, bottom: 70, right: 60 },
      borders: NOB, verticalAlign: VerticalAlign.CENTER,
      children: [P([run(num, { size: 20, bold: true, color: 'FFFFFF' })], { align: AlignmentType.CENTER, after: 0 })]
    }),
    new TableCell({
      width: { size: tag ? 5400 : CW - 760, type: WidthType.DXA },
      margins: { top: 70, left: 160, bottom: 40, right: 80 },
      borders: { top: NIL, left: NIL, bottom: bd(C.line, 8), right: NIL }, verticalAlign: VerticalAlign.CENTER,
      children: [P([run(title, { size: 22, bold: true, color: C.purple, caps: true })], { after: 0 })]
    })
  ];
  if (tag) cells.push(new TableCell({
    width: { size: CW - 760 - 5400, type: WidthType.DXA },
    margins: { top: 70, left: 80, bottom: 40, right: 40 },
    borders: { top: NIL, left: NIL, bottom: bd(C.line, 8), right: NIL }, verticalAlign: VerticalAlign.CENTER,
    children: [P([run(tag, { size: 14, bold: true, color: C.orange, italic: true })], { align: AlignmentType.RIGHT, after: 0 })]
  }));
  return [
    new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: cells.map(c => c.options?.width?.size), rows: [new TableRow({ children: cells })] }),
    text('', { size: 6, after: 60 })
  ];
}

// Podtytuł z pomarańczowym kwadracikiem
const subhead = (t) => text('■  ' + t, { size: 17, bold: true, color: C.purple, caps: true, before: 120, after: 60 });

// Ramka „Jak wypełnić"
function howto(body, title='Jak wypełnić') {
  return [
    P([run('✍  ' + title, { size: 14, bold: true, color: C.purpleMid, caps: true })],
      { shading: C.mist2, border: { top: bd(C.line, 4), left: bd(C.line, 4), right: bd(C.line, 4) }, after: 20, before: 60 }),
    P([run(body, { size: 17, color: '3D384C' })],
      { shading: C.mist2, border: { bottom: bd(C.line, 4), left: bd(C.line, 4), right: bd(C.line, 4) }, after: 140 })
  ];
}

// Ramka wiodąca (lead) — biała z pomarańczową krawędzią
function lead(title, body) {
  return [
    P([run(title, { size: 24, bold: true, color: C.purple })],
      { border: { left: bd(C.orange, 24), top: bd(C.line, 4), right: bd(C.line, 4) }, after: 30, before: 80 }),
    P([run(body, { size: 18, color: '3D384C' })],
      { border: { left: bd(C.orange, 24), bottom: bd(C.line, 4), right: bd(C.line, 4) }, after: 140 })
  ];
}

// Ramka podstawy prawnej
function legal(body, label='Podstawa prawna') {
  return [
    P([
      run(label + ': ', { size: 14, bold: true, color: C.orange, caps: true }),
      run(body, { size: 14, color: C.muted })
    ], { shading: C.mist2, border: { left: bd(C.purple, 18), top: bd(C.line, 4), right: bd(C.line, 4), bottom: bd(C.line, 4) },
         before: 100, after: 160, line: 220 })
  ];
}

// Notka wyróżniona (reguła, ochrona dziecka, uwaga)
function note(title, body, color=C.orange) {
  return [
    P([
      run(title + ' ', { size: 16, bold: true, color }),
      run(body, { size: 16, color: '3D384C' })
    ], { shading: C.orangeMist, border: { left: bd(color, 18), top: bd(C.line, 4), right: bd(C.line, 4), bottom: bd(C.line, 4) },
         before: 80, after: 140, line: 240 })
  ];
}

// Linia kropkowana do wpisania
const dotline = (o={}) => P([run(o.value || '', { size: 19, bold: true, color: C.purple })], {
  border: { bottom: bd(C.dot, 6, BorderStyle.DOTTED) }, after: o.after ?? 90, before: o.before ?? 40
});

// Pole opisowe (rubryka z liniami)
function ta(title, opts={}) {
  const lines = opts.lines ?? 5;
  const out = [P([run(title, { size: 15, bold: true, color: C.purple, caps: true })],
    { border: { top: bd(C.rule, 4), left: bd(C.rule, 4), right: bd(C.rule, 4) }, shading: C.mist, after: 40, before: 80, keepNext: true })];
  if (opts.hint) out.push(P([run(opts.hint, { size: 16, italic: true, color: '4A4360' })],
    { border: { left: bd(C.rule, 4), right: bd(C.rule, 4) }, after: 60 }));
  for (let i = 0; i < lines; i++) {
    out.push(P([run('', { size: 18 })], {
      border: { bottom: bd(C.dot, 6, BorderStyle.DOTTED), left: bd(C.rule, 4), right: bd(C.rule, 4) },
      after: i === lines - 1 ? 0 : 80, before: 60
    }));
  }
  out.push(P([run('', { size: 4 })], { border: { bottom: bd(C.rule, 4), left: bd(C.rule, 4), right: bd(C.rule, 4) }, after: 150 }));
  return out;
}

// Siatka pól metryczkowych (2 kolumny)
function fields(items, cols=2) {
  const w = Math.floor(CW / cols);
  const rows = [];
  for (let i = 0; i < items.length; i += cols) {
    const chunk = items.slice(i, i + cols);
    while (chunk.length < cols) chunk.push(null);
    rows.push(new TableRow({ children: chunk.map(f => new TableCell({
      width: { size: w, type: WidthType.DXA },
      shading: f ? { fill: C.mist, type: ShadingType.CLEAR, color: 'auto' } : undefined,
      margins: { top: 130, left: 140, bottom: 110, right: 140 },
      borders: f ? { top: bd(C.line, 4), left: bd(C.line, 4), bottom: bd(C.line, 4), right: bd(C.line, 4) } : NOB,
      children: f ? [
        P([run(f.label, { size: 14, bold: true, color: C.purpleMid, caps: true })], { after: 20 }),
        P([run(f.value || '', { size: 19, bold: true, color: C.purple })],
          { border: { bottom: bd(C.dot, 6, BorderStyle.DOTTED) }, before: 70, after: f.hint ? 30 : 0 }),
        ...(f.hint ? [P([run(f.hint, { size: 13, italic: true, color: C.muted })], { after: 0 })] : [])
      ] : [P([run('')], { after: 0 })]
    })) }));
  }
  return [new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: Array(cols).fill(w), rows }),
          text('', { size: 8, after: 100 })];
}

// Lista pól wyboru
function checks(items, cols=2) {
  const w = Math.floor(CW / cols);
  const rows = [];
  for (let i = 0; i < items.length; i += cols) {
    const chunk = items.slice(i, i + cols);
    while (chunk.length < cols) chunk.push(null);
    rows.push(new TableRow({ children: chunk.map(t => new TableCell({
      width: { size: w, type: WidthType.DXA },
      shading: t ? { fill: 'F9F7FD', type: ShadingType.CLEAR, color: 'auto' } : undefined,
      margins: { top: 90, left: 120, bottom: 90, right: 120 },
      borders: t ? { top: bd(C.rule, 4), left: bd(C.rule, 4), bottom: bd(C.rule, 4), right: bd(C.rule, 4) } : NOB,
      children: [P(t ? [run('□   ', { size: 22, bold: true, color: C.purpleMid }), run(t, { size: 17, color: '3D384C' })] : [run('')], { after: 0, line: 240 })]
    })) }));
  }
  return [new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: Array(cols).fill(w), rows }),
          text('', { size: 8, after: 100 })];
}

// Tabela danych
function table(head, rows, widths, opts={}) {
  const hdr = new TableRow({
    tableHeader: true,
    children: head.map((h, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      shading: { fill: C.purple, type: ShadingType.CLEAR, color: 'auto' },
      margins: { top: 90, left: 120, bottom: 90, right: 120 },
      borders: { top: bd(C.purple, 6), left: bd('FFFFFF', 4), bottom: bd(C.purple, 6), right: bd('FFFFFF', 4) },
      verticalAlign: VerticalAlign.CENTER,
      children: [P([run(h, { size: 15, bold: true, color: 'FFFFFF', caps: true })],
        { align: (opts.center||[]).includes(i) ? AlignmentType.CENTER : AlignmentType.LEFT, after: 0, line: 220 })]
    }))
  });
  const body = rows.map((r, ri) => new TableRow({
    height: opts.rowHeight ? { value: opts.rowHeight, rule: 'atLeast' } : undefined,
    children: r.map((cellText, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      shading: { fill: ri % 2 ? C.paper : 'FFFFFF', type: ShadingType.CLEAR, color: 'auto' },
      margins: { top: 80, left: 120, bottom: 80, right: 120 },
      borders: { top: bd(C.rule, 4), left: bd(C.line, 4), bottom: bd(C.rule, 4), right: bd(C.line, 4) },
      verticalAlign: VerticalAlign.CENTER,
      children: [P([run(cellText, {
        size: i === 0 && opts.nrCol !== false ? 18 : 17,
        bold: i === 0 && opts.nrCol !== false,
        color: i === 0 && opts.nrCol !== false ? C.orange : C.ink
      })], { align: (opts.center||[]).includes(i) ? AlignmentType.CENTER : AlignmentType.LEFT, after: 0, line: 230 })]
    }))
  }));
  return [new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: widths, rows: [hdr, ...body] }),
          text('', { size: 8, after: 120 })];
}

// Legenda skali (kolorowe kafle)
function scale(items) {
  const w = Math.floor(CW / items.length);
  return [new Table({
    width: { size: CW, type: WidthType.DXA }, columnWidths: Array(items.length).fill(w),
    rows: [new TableRow({ children: items.map(it => new TableCell({
      width: { size: w, type: WidthType.DXA },
      shading: { fill: it.bg, type: ShadingType.CLEAR, color: 'auto' },
      margins: { top: 80, left: 90, bottom: 80, right: 90 },
      borders: { top: bd(it.bg, 4), left: bd('FFFFFF', 8), bottom: bd(it.bg, 4), right: bd('FFFFFF', 8) },
      verticalAlign: VerticalAlign.CENTER,
      children: [
        P([run(it.k, { size: 17, bold: true, color: it.fg })], { align: AlignmentType.CENTER, after: 20, line: 220 }),
        P([run(it.v, { size: 13, color: it.fg })], { align: AlignmentType.CENTER, after: 0, line: 210 })
      ]
    })) })]
  }), text('', { size: 8, after: 120 })];
}

// Wykres słupkowy profilu (bez grafiki — komórki tabeli)
function bars(items, opts={}) {
  const labW = 3400, valW = 700, barMax = CW - labW - valW;
  const rows = items.map(it => {
    const v = it.value == null ? 0 : it.value;
    const fill = Math.max(30, Math.round((v / 5) * barMax));
    const rest = barMax - fill;
    const cells = [
      new TableCell({ width: { size: labW, type: WidthType.DXA }, borders: NOB, margins: { top: 40, left: 40, bottom: 40, right: 100 },
        verticalAlign: VerticalAlign.CENTER,
        children: [P([run(it.label, { size: 15, bold: true, color: C.purple })], { after: 0, line: 210 })] }),
      new TableCell({ width: { size: valW, type: WidthType.DXA }, borders: NOB, margins: { top: 40, left: 20, bottom: 40, right: 60 },
        verticalAlign: VerticalAlign.CENTER,
        children: [P([run(v ? String(v).replace('.', ',') : '—', { size: 16, bold: true, color: C.orange })], { align: AlignmentType.CENTER, after: 0 })] }),
      new TableCell({ width: { size: fill, type: WidthType.DXA },
        shading: { fill: v >= 3 ? '6C4CC4' : C.orange, type: ShadingType.CLEAR, color: 'auto' },
        borders: { top: bd('FFFFFF', 6), left: bd('FFFFFF', 4), bottom: bd('FFFFFF', 6), right: bd('FFFFFF', 4) },
        margins: { top: 40, left: 0, bottom: 40, right: 0 },
        children: [P([run('', { size: 12 })], { after: 0 })] })
    ];
    if (rest > 40) cells.push(new TableCell({ width: { size: rest, type: WidthType.DXA },
      shading: { fill: C.mist, type: ShadingType.CLEAR, color: 'auto' },
      borders: { top: bd('FFFFFF', 6), left: bd('FFFFFF', 4), bottom: bd('FFFFFF', 6), right: bd('FFFFFF', 4) },
      margins: { top: 40, left: 0, bottom: 40, right: 0 },
      children: [P([run('', { size: 12 })], { after: 0 })] }));
    return new TableRow({ children: cells });
  });
  return [
    text(opts.title || 'Profil funkcjonalny KPOF — średnia w obszarach (skala 1–5)',
      { size: 15, bold: true, color: C.purple, caps: true, before: 80, after: 60 }),
    new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: [labW, valW, barMax], rows }),
    text('', { size: 8, after: 100 })
  ];
}

// Miejsca na podpisy
function signatures(roles, cols=2) {
  const w = Math.floor(CW / cols);
  const rows = [];
  for (let i = 0; i < roles.length; i += cols) {
    const chunk = roles.slice(i, i + cols);
    while (chunk.length < cols) chunk.push(null);
    rows.push(new TableRow({ children: chunk.map(r => new TableCell({
      width: { size: w, type: WidthType.DXA },
      margins: { top: 900, left: 140, bottom: 100, right: 140 },
      borders: { top: NIL, left: NIL, bottom: NIL, right: NIL },
      children: r ? [
        P([run('', { size: 10 })], { border: { bottom: bd(C.dot, 8, BorderStyle.DOTTED) }, after: 40 }),
        P([run(r, { size: 15, bold: true, color: C.purple })], { align: AlignmentType.CENTER, after: 10 }),
        P([run('podpis i data', { size: 12, italic: true, color: C.muted })], { align: AlignmentType.CENTER, after: 0 })
      ] : [P([run('')], { after: 0 })]
    })) }));
  }
  return [new Table({ width: { size: CW, type: WidthType.DXA }, columnWidths: Array(cols).fill(w), rows }),
          text('', { size: 8, after: 100 })];
}

const brk = () => new Paragraph({ children: [new PageBreak()] });

module.exports = { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, VerticalAlign,
  FONT, CW, C, NOB, NIL, bd, run, P, text, pageHeader, pageFooter,
  section, subhead, howto, lead, legal, note, dotline, ta, fields, checks, table, scale, bars, signatures, brk };
