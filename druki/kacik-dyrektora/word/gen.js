const fs = require('fs');
const path = require('path');
const D = require('docx');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, ShadingType, BorderStyle, AlignmentType, HeadingLevel,
  PageBreak, Header, Footer, PageNumber, VerticalAlign, TabStopType
} = D;

/* ——— marka PCTP ——— */
const FIOLET = '2D1B69', POMARANCZ = 'E8450A', RAMKA = 'D9CFEE',
      POLE = 'F6F3FB', WIERSZ = 'FAF7F2', SZARY = '6B6B7B', KROPKI = 'B3A1D8',
      ZAZN = 'FDECE4', FIOLET2 = '4A3E7A';
const FONT = 'Arial';
const SZER = 9638;                                   // szerokość kolumny tekstu w DXA (A4 - marginesy)
const KROPKA = '·';

const brak = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
const zadnych = { top: brak, bottom: brak, left: brak, right: brak,
                  insideHorizontal: brak, insideVertical: brak };
const cienka = (c = RAMKA) => ({ style: BorderStyle.SINGLE, size: 4, color: c });

function T(t, o = {}) {
  return new TextRun({ text: t, font: FONT, size: o.size || 16, bold: !!o.bold,
    color: o.color || '221A3D', italics: !!o.italics, allCaps: !!o.caps,
    characterSpacing: o.spacing || 0 });
}
function biegi(tresc, o = {}) {              // [{t,b}] -> TextRun[]
  return tresc.map(r => T(r.t, Object.assign({}, o, { bold: r.b || o.bold })));
}
function P(dzieci, o = {}) {
  return new Paragraph({
    children: Array.isArray(dzieci) ? dzieci : [dzieci],
    alignment: o.align, spacing: { before: o.przed || 0, after: o.po === undefined ? 60 : o.po,
      line: o.linia || 240 },
    indent: o.wciecie ? { left: o.wciecie } : undefined,
    border: o.border, shading: o.tlo ? { type: ShadingType.CLEAR, fill: o.tlo } : undefined,
    keepNext: !!o.zNastepnym
  });
}
function komorka(dzieci, o = {}) {
  return new TableCell({
    children: Array.isArray(dzieci) ? dzieci : [dzieci],
    width: { size: o.w, type: WidthType.DXA },
    shading: o.tlo ? { type: ShadingType.CLEAR, fill: o.tlo } : undefined,
    margins: { top: o.mt === undefined ? 60 : o.mt, bottom: o.mb === undefined ? 60 : o.mb, left: 90, right: 90 },
    verticalAlign: o.vc ? VerticalAlign.CENTER : undefined,
    columnSpan: o.span, borders: o.bez ? zadnych : undefined
  });
}
function tabela(wiersze, szerokosci, o = {}) {
  return new Table({
    rows: wiersze, columnWidths: szerokosci,
    width: { size: szerokosci.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    borders: o.bez ? zadnych : {
      top: cienka(), bottom: cienka(), left: cienka(), right: cienka(),
      insideHorizontal: cienka(), insideVertical: cienka()
    }
  });
}
function rozdziel(caly, wagi) {              // rozdziel szerokość wg wag, suma = caly
  const s = wagi.reduce((a, b) => a + b, 0);
  const w = wagi.map(x => Math.floor(caly * x / s));
  w[w.length - 1] += caly - w.reduce((a, b) => a + b, 0);
  return w;
}
const KROPKI_LINIA = '.'.repeat(200);
function liniaDoWpisania(szerDxa) {          // pole do wypełnienia: kropkowana linia
  return new Paragraph({
    children: [T(' ', { size: 15 })],
    spacing: { before: 20, after: 20, line: 240 },
    border: { bottom: { style: BorderStyle.DOTTED, size: 6, color: KROPKI } }
  });
}

/* ——— bloki ——— */
function bSekcja(b) {
  const kolor = b.pom ? POMARANCZ : FIOLET;
  const t = tabela([new TableRow({ children: [
    komorka(P([T(b.nr, { bold: true, size: 15, color: 'FFFFFF' })],
             { align: AlignmentType.CENTER, po: 0 }),
            { w: 400, tlo: kolor, vc: true, mt: 40, mb: 40 }),
    komorka(P([T(' ' + b.tytul.toUpperCase(), { bold: true, size: 20, color: FIOLET, spacing: 6 }),
               ...(b.tag ? [T('   ' + b.tag, { size: 13, color: POMARANCZ, bold: true })] : [])],
             { po: 0 }), { w: SZER - 400, vc: true, bez: true })
  ]})], [400, SZER - 400], { bez: true });
  return [P([T('')], { po: 40 }), t, P([T('')], { po: 60 })];
}
function bPole(b, szer) {
  const dzieci = [P([T(b.etykieta.toUpperCase(), { bold: true, size: 13, color: FIOLET, spacing: 8 })], { po: b.hint ? 20 : 40 })];
  if (b.hint) dzieci.push(P([T(b.hint, { size: 13, color: SZARY })], { po: 40 }));
  for (let i = 0; i < (b.linii || 1); i++) dzieci.push(liniaDoWpisania());
  return tabela([new TableRow({ children: [komorka(dzieci, { w: szer, tlo: POLE })] })],
                [szer], {});
}
function bSiatka(b) {
  const w = rozdziel(SZER, b.pola.map(() => 1));
  const kom = b.pola.map((p, i) => {
    const wewn = [P([T(p.etykieta.toUpperCase(), { bold: true, size: 13, color: FIOLET, spacing: 8 })], { po: 40 })];
    for (let j = 0; j < (p.linii || 1); j++) wewn.push(liniaDoWpisania());
    return komorka(wewn, { w: w[i], tlo: POLE });
  });
  return tabela([new TableRow({ children: kom })], w, {});
}
function bTabela(b) {
  const n = b.glowa.length || (b.wiersze[0] || []).length;
  if (!n) return null;
  let wagi = b.glowa.map(g => g.w ? g.w.v : 0);
  if (!wagi.length || wagi.every(x => !x)) wagi = new Array(n).fill(1);
  else { const sr = wagi.filter(Boolean).reduce((a, c) => a + c, 0) / wagi.filter(Boolean).length;
         wagi = wagi.map(x => x || sr); }
  const w = rozdziel(SZER, wagi);
  const wiersze = [];
  if (b.glowa.length) wiersze.push(new TableRow({ tableHeader: true, children: b.glowa.map((g, i) =>
    komorka(P([T(g.t.toUpperCase(), { bold: true, size: 13, color: 'FFFFFF', spacing: 6 })], { po: 0 }),
            { w: w[i], tlo: FIOLET, vc: true, mt: 80, mb: 80 })) }));
  b.wiersze.forEach((r, ri) => {
    const tlo = ri % 2 ? WIERSZ : undefined;
    wiersze.push(new TableRow({ children: r.map((c, i) => {
      let dzieci;
      if (c.rodzaj === 'lp')      dzieci = P([T(c.t, { bold: true, size: 14, color: POMARANCZ })], { align: AlignmentType.CENTER, po: 0 });
      else if (c.rodzaj === 'klucz') dzieci = P([T(c.t, { bold: true, size: 14, color: FIOLET })], { po: 0 });
      else if (c.rodzaj === 'ocena') dzieci = P([T(c.t, { size: 14, color: FIOLET2, spacing: 10 })], { align: AlignmentType.CENTER, po: 0 });
      else if (c.rodzaj === 'kratka') dzieci = P([T('☐', { size: 22, color: KROPKI })], { align: AlignmentType.CENTER, po: 0 });
      else if (c.rodzaj === 'puste') dzieci = new Paragraph({ children: [T(' ', { size: 14 })], spacing: { before: 20, after: 20 },
                                        border: { bottom: { style: BorderStyle.DOTTED, size: 6, color: KROPKI } } });
      else dzieci = P([T(c.t, { size: 14 })], { po: 0 });
      return komorka(dzieci, { w: w[i], tlo, vc: true, mt: 70, mb: 70 });
    }) }));
  });
  return tabela(wiersze, w, {});
}
function bWybory(b) {
  const kol = b.kol === 1 ? 1 : b.kol === 3 ? 3 : 2;
  const w = rozdziel(SZER, new Array(kol).fill(1));
  const wiersze = [];
  for (let i = 0; i < b.opcje.length; i += kol) {
    const kom = [];
    for (let j = 0; j < kol; j++) {
      const o = b.opcje[i + j];
      kom.push(komorka(o === undefined ? P([T('')], { po: 0 })
        : P([T('☐  ', { size: 20, color: POMARANCZ }), T(o, { size: 14 })], { po: 0 }),
        { w: w[j], tlo: o === undefined ? undefined : POLE, vc: true, mt: 80, mb: 80 }));
    }
    wiersze.push(new TableRow({ children: kom }));
  }
  return tabela(wiersze, w, {});
}
function bRamka(b, tlo, kolorPaska, rozmiar) {
  return tabela([new TableRow({ children: [
    komorka(P([T(' ')], { po: 0 }), { w: 60, tlo: kolorPaska, bez: true }),
    komorka(P(biegi(b.tresc, { size: rozmiar || 13 }), { po: 0, linia: 260 }), { w: SZER - 60, tlo, bez: true })
  ]})], [60, SZER - 60], { bez: true });
}
function bPodpisy(b) {
  const w = rozdziel(SZER, b.opisy.map(() => 1));
  return [P([T('')], { po: 240 }),
    tabela([new TableRow({ children: b.opisy.map((o, i) => komorka([
      new Paragraph({ children: [T(' ', { size: 12 })], spacing: { after: 40 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: FIOLET2 } } }),
      P([T(o, { size: 13, color: SZARY })], { align: AlignmentType.CENTER, po: 0 })
    ], { w: w[i], bez: true, mt: 0 })) })], w, { bez: true })];
}
function bMiesiace(b) {
  const w = rozdziel(SZER, [1, 1]);
  const wiersze = [];
  for (let i = 0; i < b.bloki.length; i += 2) {
    const kom = [];
    for (let j = 0; j < 2; j++) {
      const m = b.bloki[i + j];
      if (!m) { kom.push(komorka(P([T('')], { po: 0 }), { w: w[j], bez: true })); continue; }
      const d = [P([T(m.naglowek.toUpperCase(), { bold: true, size: 12, color: POMARANCZ, spacing: 10 })], { po: 20 }),
                 P([T(m.termin, { bold: true, size: 17, color: FIOLET })], { po: 60 })];
      m.punkty.forEach(pk => d.push(P([T('☐  ', { size: 15, color: KROPKI }), ...biegi(pk, { size: 13 })], { po: 30, linia: 240 })));
      kom.push(komorka(d, { w: w[j], tlo: POLE, mt: 100, mb: 100 }));
    }
    wiersze.push(new TableRow({ children: kom }));
  }
  return tabela(wiersze, w, {});
}
function bBlokDyr(b) {
  const wewn = [tabela([new TableRow({ children: [
      komorka(P([T(b.znak, { bold: true, size: 13, color: 'FFFFFF' })], { align: AlignmentType.CENTER, po: 0 }),
              { w: 400, tlo: POMARANCZ, vc: true, mt: 40, mb: 40 }),
      komorka(P([T(' ' + b.tytul.toUpperCase(), { bold: true, size: 17, color: POMARANCZ, spacing: 6 })], { po: 0 }),
              { w: SZER - 700, vc: true, bez: true })
    ]})], [400, SZER - 700], { bez: true }), P([T('')], { po: 60 })];
  b.tresc.forEach(x => { const e = element(x); if (e) wewn.push(...(Array.isArray(e) ? e : [e])); });
  return tabela([new TableRow({ children: [komorka(wewn, { w: SZER, tlo: 'FEF6F2', mt: 120, mb: 120 })] })],
                [SZER], {});
}
function bKarty(b) {
  const w = rozdziel(SZER, b.karty.map(() => 1));
  return tabela([new TableRow({ children: b.karty.map((k, i) => komorka([
    P([T(k.duza, { bold: true, size: 22, color: FIOLET })], { align: AlignmentType.CENTER, po: 20 }),
    P([T(k.opis.toUpperCase(), { bold: true, size: 12, color: POMARANCZ, spacing: 8 })], { align: AlignmentType.CENTER, po: 0 })
  ], { w: w[i], tlo: POLE, mt: 100, mb: 100 })) })], w, {});
}
function bKafle(b) {
  const w = rozdziel(SZER, b.kafle.map(() => 1));
  return tabela([new TableRow({ children: b.kafle.map((k, i) => komorka([
    P([T(k.nag.toUpperCase(), { bold: true, size: 12, color: POMARANCZ, spacing: 8 })], { po: 20 }),
    P([T(k.tresc, { bold: true, size: 14, color: FIOLET })], { po: k.uwaga ? 20 : 0 }),
    ...(k.uwaga ? [P([T(k.uwaga, { size: 12, color: SZARY })], { po: 0 })] : [])
  ], { w: w[i], tlo: POLE, mt: 90, mb: 90 })) })], w, {});
}

function element(b) {
  switch (b.typ) {
    case 'sekcja':      return bSekcja(b);
    case 'wstep':       return P(biegi(b.tresc, { size: 14, color: FIOLET2 }), { wciecie: 400, po: 120, linia: 260 });
    case 'prawna':      return bRamka(b, POLE, FIOLET, 12);
    case 'legenda':     return bRamka(b, POLE, KROPKI, 12);
    case 'info':        return bRamka(b, 'F3EFFA', FIOLET, 13);
    case 'pole':        return bPole(b, SZER);
    case 'siatka':      return bSiatka(b);
    case 'tabela':      return bTabela(b);
    case 'wybor-tytul': return P([T('■  ', { size: 12, color: POMARANCZ }),
                                  T(b.tytul.toUpperCase(), { bold: true, size: 13, color: FIOLET, spacing: 8 })], { przed: 100, po: 60 });
    case 'wybory':      return bWybory(b);
    case 'podpisy':     return bPodpisy(b);
    case 'blok-dyr':    return bBlokDyr(b);
    case 'miesiace':    return bMiesiace(b);
    case 'karty':       return bKarty(b);
    case 'kafle':       return bKafle(b);
    default:            return null;
  }
}

/* ——— strona tytułowa druku ——— */
function naglowekDruku(s) {
  const out = [];
  out.push(tabela([new TableRow({ children: [
    komorka([P([T('EduPlaner 2026', { bold: true, size: 26, color: FIOLET })], { po: 20 }),
             P([T('KĄCIK DYREKTORA · PRZEDSZKOLE', { bold: true, size: 12, color: SZARY, spacing: 12 })], { po: 0 })],
            { w: Math.floor(SZER * 0.62), bez: true, mt: 0 }),
    komorka([P([T('  ' + (s.wstega ? 'DOKUMENT WSPARCIA · 2026' : ''), { bold: true, size: 11, color: SZARY, spacing: 12 })],
              { align: AlignmentType.RIGHT, po: 0 })],
            { w: SZER - Math.floor(SZER * 0.62), bez: true, vc: true, mt: 0 })
  ]})], [Math.floor(SZER * 0.62), SZER - Math.floor(SZER * 0.62)], { bez: true }));
  out.push(tabela([new TableRow({ children: [
    komorka(P([T(' ', { size: 6 })], { po: 0 }), { w: Math.floor(SZER * 0.55), tlo: FIOLET, bez: true, mt: 0, mb: 0 }),
    komorka(P([T(' ', { size: 6 })], { po: 0 }), { w: SZER - Math.floor(SZER * 0.55), tlo: POMARANCZ, bez: true, mt: 0, mb: 0 })
  ]})], [Math.floor(SZER * 0.55), SZER - Math.floor(SZER * 0.55)], { bez: true }));
  out.push(P([T('')], { po: 120 }));
  const mw = rozdziel(SZER, [2.2, 1.5, 1.3]);
  out.push(tabela([new TableRow({ children: [
    ['PRZEDSZKOLE', ''], ['DYREKTOR', ''], ['ROK SZKOLNY', '2026 / 2027']
  ].map(([et, wa], i) => komorka([
    P([T(et, { bold: true, size: 12, color: FIOLET, spacing: 10 })], { po: 30 }),
    wa ? P([T(wa, { size: 17, color: FIOLET, bold: true })], { po: 0 }) : liniaDoWpisania()
  ], { w: mw[i], tlo: POLE, mt: 90, mb: 90 })) })], mw, {}));
  out.push(P([T('')], { po: 160 }));
  if (s.wstega) out.push(tabela([new TableRow({ children: [komorka(
    P([T(s.wstega.toUpperCase(), { bold: true, size: 13, color: 'FFFFFF', spacing: 10 })],
      { align: AlignmentType.CENTER, po: 0 }), { w: SZER, tlo: POMARANCZ, mt: 80, mb: 80 })] })], [SZER], { bez: true }));
  out.push(P([T(s.tytul, { bold: true, size: 40, color: FIOLET, spacing: 4 })],
             { align: AlignmentType.CENTER, przed: 200, po: 60 }));
  if (s.podtytul) out.push(P([T(s.podtytul, { bold: true, size: 21, color: POMARANCZ })],
                             { align: AlignmentType.CENTER, po: 80 }));
  if (s.kody) out.push(P([T(s.kody, { bold: true, size: 15, color: FIOLET, spacing: 40 })],
                         { align: AlignmentType.CENTER, po: 220,
                           border: { top: { style: BorderStyle.SINGLE, size: 4, color: POMARANCZ },
                                     bottom: { style: BorderStyle.SINGLE, size: 4, color: POMARANCZ } } }));
  return out;
}

/* ——— budowa dokumentu ——— */
function zbuduj(d) {
  const dzieci = [];
  d.strony.forEach((s, i) => {
    if (i) dzieci.push(new Paragraph({ children: [new PageBreak()] }));
    if (s.tytul) dzieci.push(...naglowekDruku(s));
    s.bloki.forEach(b => {
      const e = element(b);
      if (!e) return;
      (Array.isArray(e) ? e : [e]).forEach(x => dzieci.push(x));
      if (x_potrzebuje_odstepu(b)) dzieci.push(P([T('')], { po: 80 }));
    });
  });
  return new Document({
    creator: 'EduPlaner 2026 · PCTP', title: d.tytul, description: 'Kącik dyrektora · przedszkole',
    styles: { default: { document: { run: { font: FONT, size: 16, color: '221A3D' },
                                     paragraph: { spacing: { line: 260 } } } } },
    sections: [{
      properties: { page: { margin: { top: 850, right: 850, bottom: 850, left: 850 } } },
      headers: { default: new Header({ children: [ new Paragraph({
        children: [T('EduPlaner 2026 ' + KROPKA + ' Kącik dyrektora ' + KROPKA + ' przedszkole', { size: 12, color: SZARY, spacing: 8 })],
        alignment: AlignmentType.RIGHT, spacing: { after: 0 },
        border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: RAMKA } } }) ] }) },
      footers: { default: new Footer({ children: [ new Paragraph({
        children: [ T('EduPlaner 2026 ' + KROPKA + ' PCTP ' + KROPKA + ' pedagog specjalny', { size: 12, color: SZARY }),
                    new TextRun({ children: ['\t', 'Strona ', PageNumber.CURRENT, ' z ', PageNumber.TOTAL_PAGES],
                                  font: FONT, size: 12, color: SZARY, bold: true }) ],
        tabStops: [{ type: TabStopType.RIGHT, position: SZER }],
        spacing: { before: 0 },
        border: { top: { style: BorderStyle.SINGLE, size: 4, color: RAMKA } } }) ] }) },
      children: dzieci
    }]
  });
}
function x_potrzebuje_odstepu(b) {
  return ['tabela','pole','siatka','wybory','prawna','legenda','info','blok-dyr','miesiace','karty','kafle'].includes(b.typ);
}

/* ——— main ——— */
const dane = JSON.parse(fs.readFileSync('druki.json', 'utf8'));
const wyj = process.argv[2] || 'out';
fs.mkdirSync(wyj, { recursive: true });
const tylko = process.argv[3];
(async () => {
  for (const k of Object.keys(dane)) {
    if (tylko && k !== tylko) continue;
    const buf = await Packer.toBuffer(zbuduj(dane[k]));
    fs.writeFileSync(path.join(wyj, k + '.docx'), buf);
    console.log('  +', k + '.docx', (buf.length / 1024).toFixed(0) + ' KB');
  }
})();
