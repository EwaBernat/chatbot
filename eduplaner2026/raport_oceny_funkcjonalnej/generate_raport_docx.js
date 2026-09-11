// Raport Oceny Funkcjonalnej · EduPlaner 2026 (PCTP Koszalin)
// Styl graficzny wg wzoru IPET: biały papier, lawendowe pola, fiolet w akcentach, pomarańczowe plakietki.
// Użycie: npm i docx@9 && node generate_raport_docx.js Raport_Oceny_Funkcjonalnej.docx
const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, WidthType, ShadingType, PageBreak, TabStopType,
  Header, Footer, PageNumber, VerticalAlign
} = require('docx');

const FONT = 'Arial';
const C = { purple:'2D1B69', orange:'E74509', green:'2E7D45', red:'BF382A', blue:'2D6BB3',
  ink:'1A1530', muted:'6B6378', lavText:'7D6FB0', lav:'EFE9F9', lav2:'FAFAFF', line:'D9D0F0', line2:'E3E1EC',
  paper:'FAF6F1', orangeMist:'FDECE3', white:'FFFFFF' };
const A4 = { width: 11906, height: 16838 };
const MARGINS = { top: 1100, right: 1000, bottom: 1250, left: 1000 };
const CW = 11906 - 2000; // 9906

const run = (text, o={}) => new TextRun({ text, font: FONT, size: o.size||20, bold: !!o.bold, italics: !!o.italic, color: o.color||C.ink, allCaps: !!o.caps, characterSpacing: o.spacing, shading: o.bg ? { fill:o.bg, type:ShadingType.CLEAR, color:'auto' } : undefined });
const P = (children, o={}) => new Paragraph({ spacing:{ before:o.before||0, after:o.after??120, line:o.line||276, lineRule:o.lineRule }, alignment:o.align||AlignmentType.LEFT, keepNext:o.keepNext, children });
const empty = (after=0) => new Paragraph({ spacing:{before:0, after}, children:[] });
const NOB = { style: BorderStyle.NIL };
const noBorders = { top:NOB, bottom:NOB, left:NOB, right:NOB };
const ln = (color=C.line, size=4) => ({ style: BorderStyle.SINGLE, size, color });
const lineBorders = { top:ln(), bottom:ln(), left:ln(), right:ln() };

const cell = (children, o={}) => new TableCell({
  width:{ size:o.width, type:WidthType.DXA },
  shading: o.bg ? { fill:o.bg, type:ShadingType.CLEAR, color:'auto' } : undefined,
  margins: o.margins || { top:120, bottom:120, left:180, right:180 },
  borders: o.borders || lineBorders,
  verticalAlign: o.vAlign || VerticalAlign.TOP,
  columnSpan: o.span,
  children: Array.isArray(children) ? children : [children]
});
const tbl = (widths, rows, o={}) => new Table({ width:{ size: widths.reduce((a,b)=>a+b,0), type:WidthType.DXA }, columnWidths: widths, alignment:o.align, rows });
const row = (cells) => new TableRow({ children: cells, cantSplit:true });
const ph = (t) => run(t, { italic:true, color:C.muted, size:18 });
const label = (t, o={}) => P([ run(t, { size:o.size||13, bold:true, color:o.color||C.purple, caps:true, spacing:o.spacing??12 }) ], { after:o.after??60 });

// ---- pudełko wzór IPET: obrys lawendowy + kolorowa lewa krawędź ----
const box = (children, edge=C.orange, o={}) => tbl([CW], [ row([ cell(children, { width:CW, bg:o.bg||C.white, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:32, color:edge } }, margins:{ top:130, bottom:130, left:240, right:240 } }) ]) ]);

// ---- nagłówek strony (wzór IPET) ----
const pageHeader = (caption) => [
  tbl([700, 6200, 3006], [ row([
    cell(P([ run('PCTP', { size:12, bold:true, color:C.white }) ], { align:AlignmentType.CENTER, after:0 }), { width:700, bg:C.purple, borders:noBorders, vAlign:VerticalAlign.CENTER, margins:{ top:120, bottom:120, left:40, right:40 } }),
    cell([ P([ run('EduPlaner 2026', { size:26, bold:true, color:C.purple }) ], { after:20 }), P([ run(caption, { size:12, color:C.muted, caps:true, spacing:14 }) ], { after:0 }) ], { width:6200, borders:noBorders, vAlign:VerticalAlign.CENTER, margins:{ top:0, bottom:0, left:160, right:0 } }),
    cell([ P([ run('  RAPORT · 2026  ', { size:13, bold:true, color:C.white, bg:C.orange, spacing:10 }) ], { align:AlignmentType.RIGHT, after:60 }), P([ run('DOKUMENT DLA RODZICA · 2026', { size:11, color:C.muted, spacing:14 }) ], { align:AlignmentType.RIGHT, after:0 }) ], { width:3006, borders:noBorders, vAlign:VerticalAlign.CENTER, margins:{ top:0, bottom:0, left:0, right:0 } })
  ]) ]),
  new Paragraph({ spacing:{ before:60, after:160 }, border:{ bottom:{ style:BorderStyle.SINGLE, size:12, color:C.purple, space:1 } }, children:[] }),
  // lawendowe pola
  tbl([3900, 2900, 2906], [ row([
    ['DOTYCZY DZIECKA', 3900], ['GRUPA / KLASA', 2900], ['DATA', 2906]
  ].map(([t,w]) => cell(P([ run(t, { size:12, bold:true, color:C.lavText, spacing:14 }), run('  ' + '.'.repeat(w===3900?52:30), { size:14, color:'B6A6DF' }), run(t==='DATA'?'  r.':'', { size:14, color:C.muted }) ], { after:0 }), { width:w, bg:C.lav, borders:{ top:ln(C.white,12), bottom:ln(C.white,12), left:ln(C.white,12), right:ln(C.white,12) }, margins:{ top:110, bottom:110, left:180, right:120 } })) ) ]),
  empty(120)
];

// ---- nagłówek sekcji: pomarańczowy numer + fiolet + linia ----
const section = (n, title) => new Paragraph({
  spacing:{ before:200, after:140 }, keepNext:true,
  border:{ bottom:{ style:BorderStyle.SINGLE, size:4, color:C.line, space:6 } },
  children:[ run(' '+n+' ', { size:20, bold:true, color:C.white, bg:C.orange }), run('   ', { size:20 }), run(title.toUpperCase(), { size:22, bold:true, color:C.purple, spacing:10 }) ]
});

// =============== STRONA 1 · OKŁADKA ===============
const cover = [
  ...pageHeader('Raport Oceny Funkcjonalnej · Okładka'),
  P([ run('  OPINIA PRZEDSZKOLA / SZKOŁY · DLA ZESPOŁU ORZEKAJĄCEGO · DLA RODZICA  ', { size:14, bold:true, color:C.white, bg:C.orange, spacing:12 }) ], { align:AlignmentType.CENTER, before:40, after:120 }),
  P([ run('OCENA FUNKCJONALNA · ICF · PRZEDSZKOLE · SZKOŁA', { size:15, color:C.purple, spacing:50 }) ], { align:AlignmentType.CENTER, after:60 }),
  P([ run('Raport Oceny Funkcjonalnej', { size:52, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:80, line:600, lineRule:'exact' }),
  P([ run('OBSERWACJA WSTĘPNA I POGŁĘBIONA · OBSZARY ICF', { size:15, bold:true, color:C.orange, spacing:44 }) ], { align:AlignmentType.CENTER, after:140 }),
  P([ run('z dnia  ', { size:20, color:C.muted }), run('………………………………………………', { size:20, color:'B6A6DF' }) ], { align:AlignmentType.CENTER, after:160 }),

  // zespół
  box([
    label('Opracowany przez Zespół w składzie'),
    tbl([Math.floor((CW-480)/2), Math.floor((CW-480)/2)], [0,1,2].map(r => row([0,1].map(c => {
      const n = r*2+c+1, w = Math.floor((CW-480)/2);
      return cell(P([ run(n+'.', { bold:true, color:C.orange, size:20 }), run('  ' + '.'.repeat(58), { size:16, color:'B6A6DF' }) ], { after:0 }), { width:w, borders:noBorders, margins:{ top:40, bottom:40, left:0, right:200 } });
    }))))
  ], C.orange),
  empty(100),

  // podstawa prawna
  box([
    tbl([700, CW-480-700], [ row([
      cell(P([ run('§', { size:40, bold:true, color:C.orange }) ], { align:AlignmentType.CENTER, after:0 }), { width:700, bg:C.lav, borders:noBorders, vAlign:VerticalAlign.TOP, margins:{ top:80, bottom:80, left:40, right:40 } }),
      cell([
        label('Podstawa prawna'),
        P([
          run('Zgodnie z Rozporządzeniem Ministra Edukacji z dnia 2 marca 2026 r. w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające działające w publicznych poradniach psychologiczno-pedagogicznych ', { size:18 }),
          run('(Dz. U. z 2026 r. poz. 428)', { size:18, bold:true, color:C.purple }),
          run(', a w szczególności wchodzącymi w życie z dniem 1 września 2026 r. przepisami ', { size:18 }),
          run('§ 7 ust. 6 i ust. 7', { size:18, bold:true, color:C.purple }),
          run(', opinia przedszkola/szkoły wydawana dla zespołu poradni (i przekazywana rodzicowi) musi mieć ściśle określoną strukturę opartą na obszarach ICF: odrębnych dla dziecka w wieku przedszkolnym oraz dla ucznia szkoły.', { size:18 })
        ], { align:AlignmentType.JUSTIFIED, after:0, line:290 })
      ], { width:CW-480-700, borders:noBorders, margins:{ top:0, bottom:0, left:200, right:0 } })
    ]) ])
  ], C.purple, { bg:C.lav2 }),
  empty(120),

  // zawartość raportu (z raport_data.json)
  ...(() => {
    const T = JSON.parse(require('fs').readFileSync(require('path').join(__dirname,'raport_data.json'),'utf8')).toc;
    const out = [];
    const head = (t) => P([ run('■ ', { size:14, color:C.purple }), run(t.toUpperCase(), { size:12, bold:true, color:C.purple, spacing:14 }) ], { after:70 });
    out.push(head(T.I.title));
    out.push(tbl([3302,3302,3302], [ row(T.I.items.map(t => cell([ P([ run(t[0], { size:26, bold:true, color:C.orange }) ], { after:20 }), P([ run(t[1], { size:17, bold:true, color:C.purple }) ], { after:30 }), P([ run(t[2], { size:13, color:C.muted }) ], { after:0, line:230 }) ], { width:3302, borders:{ top:{ style:BorderStyle.SINGLE, size:24, color:C.orange }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:90, left:160, right:160 } }))) ]));
    for (const part of ['II','III']) {
      out.push(empty(80)); out.push(head(T[part].title));
      const n = T[part].items.length, w = Math.floor(CW/n), ws = T[part].items.map((_,i) => i===n-1 ? CW-w*(n-1) : w);
      out.push(tbl(ws, [ row(T[part].items.map((t,i) => cell([ P([ run(t[0], { size:22, bold:true, color:C.orange }) ], { after:10 }), P([ run(t[1], { size:12, bold:true, color:C.purple }) ], { after:0, line:210 }) ], { width:ws[i], borders:{ top:{ style:BorderStyle.SINGLE, size:24, color:C.orange }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:60, bottom:70, left:90, right:60 } }))) ]));
    }
    return out;
  })(),
  new Paragraph({ children:[ new PageBreak() ] })
];

// =============== STRONA 2 · METRYCZKA + PROCEDURA ===============
const LW = 3000, RW = CW-LW;
const vp = (children) => P(children, { after:0, line:270 });
const checkbox = (children) => P([ run('☐  ', { size:22, color:'B6A6DF' }), ...children ], { before:30, after:30, line:260 });
const metaRow = (lbl, valueChildren) => row([
  cell(P([ run(lbl, { size:13, bold:true, color:C.purple, caps:true, spacing:10 }) ], { after:0 }), { width:LW, bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:100, bottom:100, left:180, right:120 } }),
  cell(valueChildren, { width:RW, borders:{ top:ln(C.line2), bottom:ln(C.line2), left:ln(C.line2), right:ln() }, margins:{ top:90, bottom:90, left:180, right:180 } })
]);
const meta = tbl([LW,RW], [
  metaRow('Imię i nazwisko', vp([ ph('[Imię i Nazwisko dziecka / ucznia]') ])),
  metaRow('Data urodzenia', vp([ ph('[Data urodzenia]') ])),
  metaRow('Placówka / Oddział', vp([ ph('[Nazwa przedszkola / szkoły, grupa / klasa]') ])),
  metaRow('Wariant wsparcia', [
    checkbox([ run('Wariant A', { bold:true, color:C.purple, size:18 }), run(' – wsparcie na podstawie orzeczenia o potrzebie kształcenia specjalnego', { size:18 }) ]),
    checkbox([ run('Wariant B', { bold:true, color:C.purple, size:18 }), run(' – wsparcie w ramach pomocy psychologiczno-pedagogicznej (bez orzeczenia)', { size:18 }) ])
  ]),
  metaRow('Jednostka / Podstawa formalna', vp([ run('Na podstawie dołączonego dokumentu: ', { size:18 }), ph('[Orzeczenie / Opinia]'), run(' nr ', { size:18 }), ph('[Numer]'), run(' z dnia ', { size:18 }), ph('[Data]'), run(', wydanego przez: ', { size:18 }), ph('[Nazwa Poradni]'), run(', z uwagi na: ', { size:18 }), ph('[np. autyzm, w tym zespół Aspergera / niepełnosprawność ruchowa / inne]') ])),
  metaRow('Schorzenia przewlekłe', [
    checkbox([ run('Brak', { size:18 }) ]),
    checkbox([ run('Występują: ', { size:18 }), ph('[np. cukrzyca, astma, epilepsja]') ])
  ]),
  metaRow('Farmakoterapia i wskazania lekarza', vp([ run('Zgodnie ze wskazaniami lekarza dziecko/uczeń ', { size:18 }), run('stale / doraźnie', { size:18, bold:true }), run(' przyjmuje leki: ', { size:18 }), ph('[Nazwa leków, zalecenia postępowania / Nie dotyczy]') ]))
]);

const steps = [
  ['1','Zgłoszenie','zgłaszane trudności w funkcjonowaniu oraz wniosek rodzica'],
  ['2','Dokumentacja','posiadana opinia / orzeczenie poradni psychologiczno-pedagogicznej'],
  ['3','Obserwacja · wrzesień','Kwestionariusz Przedszkolnej / Szkolnej Oceny Funkcjonalnej'],
  ['4','Analiza ICF','obszary zgodne z Międzynarodową Klasyfikacją Funkcjonowania']
];
const SW = Math.floor(CW/4);
const flow = tbl([SW,SW,SW,SW], [ row(steps.map(s => cell([
  P([ run(' '+s[0]+' ', { size:18, bold:true, color:C.orange, bg:C.lav }) ], { after:60 }),
  P([ run(s[1], { size:17, bold:true, color:C.purple }) ], { after:50 }),
  P([ run(s[2], { size:15, color:C.muted }) ], { after:0, line:240 })
], { width:SW, margins:{ top:100, bottom:100, left:150, right:150 } }))) ]);

const icfRow = tbl([1981,1981,1981,1981,1982], [ row([
  ['Funkcje ciała','b'],['Struktury ciała','s'],['Aktywność i uczestnictwo','d'],['Czynniki środowiskowe','e'],['Czynniki osobowe','—']
].map((t,i) => cell([
  P([ run(t[0], { size:15, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:20 }),
  P([ run(t[1], { size:14, bold:true, color:C.lavText }) ], { align:AlignmentType.CENTER, after:0 })
], { width:i===4?1982:1981, bg:C.lav, borders:{ top:ln(C.white,12), bottom:ln(C.white,12), left:ln(C.white,12), right:ln(C.white,12) }, margins:{ top:110, bottom:110, left:80, right:80 }, vAlign:VerticalAlign.CENTER }))) ]);

// =============== STRONA 3 · NARZĘDZIA ===============
const toolCell = (tag, title, desc, color, width, extra=[]) => cell([
  P([ run(tag.toUpperCase(), { size:13, bold:true, color, spacing:14 }) ], { after:40 }),
  P([ run(title, { size:20, bold:true, color:C.purple }) ], { after:70, line:250 }),
  P([ run(desc, { size:17 }) ], { after:0, line:255 }),
  ...extra
], { width, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:32, color } }, margins:{ top:120, bottom:130, left:220, right:180 } });

const HW = CW/2;
const abcRow = tbl([3100,3100,3100], [ row([
  ['A','bodźce wyzwalające'],['B','forma zachowania'],['C','funkcja i skutki podtrzymujące']
].map(t => cell([
  P([ run(t[0], { size:26, bold:true, color:C.red }) ], { align:AlignmentType.CENTER, after:10 }),
  P([ run(t[1], { size:15, bold:true, color:C.red }) ], { align:AlignmentType.CENTER, after:0 })
], { width:3100, bg:C.orangeMist, borders:{ top:NOB, bottom:NOB, left:ln(C.white,24), right:ln(C.white,24) }, margins:{ top:90, bottom:90, left:60, right:60 } }))) ]);

const tools = [
  tbl([CW], [ row([ toolCell('Zachowania trudne','Arkusz Obserwacji Behawioralnej ABC','Zastosowany z uwagi na występowanie zachowań trudnych – identyfikacja bodźców wyzwalających, formy zachowania oraz funkcji i skutków podtrzymujących.', C.red, CW, [ empty(110), abcRow ]) ]) ]),
  empty(100),
  tbl([HW,HW], [
    row([
      toolCell('Całościowy obraz','Profil Biopsychospołeczny','Ujęcie funkcjonowania dziecka w wymiarze biologicznym, psychologicznym i społecznym – zgodnie z modelem ICF.', C.purple, HW),
      toolCell('Przetwarzanie bodźców','Profil Sensoryczny','Ocena reaktywności sensorycznej (nadwrażliwości, podwrażliwości, poszukiwania stymulacji) i wpływu bodźców środowiskowych na dysregulację dziecka.', C.blue, HW)
    ]),
    row([
      toolCell('Komunikacja','Arkusz Oceny Rozwoju Mowy i Komunikacji','Zastosowany w związku ze specyficznymi trudnościami w nadawaniu i rozumieniu mowy, echolaliami lub potrzebą wdrożenia / rozwijania AAC.', C.orange, HW),
      toolCell('Funkcje poznawcze i społeczne','Arkusz Poziomu Rozwoju Teorii Umysłu (ToM)','Zbadanie poziomu rozumienia stanów mentalnych, intencji, perspektywy i emocji innych osób w sytuacjach społecznych.', C.green, HW)
    ])
  ])
];

const sigCell = (role, width, span, top=300) => new TableCell({
  width:{ size:width, type:WidthType.DXA }, columnSpan: span,
  margins:{ top, bottom:20, left:220, right:220 }, borders:noBorders,
  children:[
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{ before:0, after:0 }, border:{ top:{ style:BorderStyle.SINGLE, size:6, color:C.purple, space:5 } }, children:[ run(role, { size:16, bold:true, color:C.purple }) ] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{ before:10, after:0 }, children:[ run('podpis i data', { size:12, color:C.muted }) ] })
  ]
});
const SGW = Math.floor(CW/3);
const sigs = tbl([SGW,SGW,SGW], [
  row([ sigCell('Koordynator Zespołu',SGW), sigCell('Dyrektor placówki',SGW), sigCell('Specjalista',SGW) ]),
  row([ sigCell('Rodzic / opiekun prawny – zapoznałam/em się z raportem', SGW*3, 3, 180) ])
]);

// =============== STOPKA ===============
const footerPara = new Paragraph({
  spacing:{ before:60, after:0 }, border:{ top:{ style:BorderStyle.SINGLE, size:4, color:C.line2, space:4 } },
  tabStops:[{ type:TabStopType.RIGHT, position:CW }],
  children:[ run('EduPlaner 2026 · PCTP', { size:12, color:C.muted }), run('   ·   RODO · Dokument poufny', { size:12, color:C.muted }), run('\t'), run('Strona ', { size:12, color:C.muted }), new TextRun({ children:[PageNumber.CURRENT], font:FONT, size:12, bold:true, color:C.orange }), run(' z ', { size:12, color:C.muted }), new TextRun({ children:[PageNumber.TOTAL_PAGES], font:FONT, size:12, bold:true, color:C.purple }), run(' · Raport Oceny Funkcjonalnej', { size:12, color:C.muted }) ]
});


// =============== CZĘŚĆ II–III · DANE Z raport_data.json ===============
const path = require('path');
const D = JSON.parse(fs.readFileSync(path.join(__dirname, 'raport_data.json'), 'utf8'));
const pb = () => new Paragraph({ pageBreakBefore:true, spacing:{ before:0, after:0, line:20, lineRule:'exact' }, children:[ run('', { size:2 }) ] });
const gridHead = (cols, widths, colors=[]) => row(cols.map((t,i) => cell(P([ run(t, { size:13, bold:true, color:colors[i]||C.purple, caps:true, spacing:10 }) ], { after:0 }), { width:widths[i], bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:100, bottom:100, left:140, right:120 } })));
const gcell = (children, width, o={}) => cell(Array.isArray(children)?children:[children], { width, bg:o.bg, borders:{ top:ln(C.line2), bottom:ln(C.line2), right:ln(C.line2), left: o.edge ? { style:BorderStyle.SINGLE, size:24, color:o.edge } : ln(C.line2) }, margins:{ top:o.pad??70, bottom:o.pad??70, left:140, right:120 } });
const txt = (t, o={}) => P([ run(t, { size:o.size||16, bold:o.bold, color:o.color, italic:o.italic }) ], { after:0, line:o.size&&o.size<15?230:250 });
const bullets = (items, mark='•', color=C.orange) => items.map(t => new Paragraph({ spacing:{ before:0, after:40, line:245 }, indent:{ left:200, hanging:200 }, children:[ run(mark+'  ', { size:16, color, bold:true }), run(t, { size:16 }) ] }));
const lead2 = (ref, t) => P([ ...(ref ? [run(ref+' ', { size:16, bold:true, color:C.purple })] : []), run(t, { size:16, color:C.muted }) ], { after:140, line:260, align:AlignmentType.JUSTIFIED });
const sub9 = (tag, title, note, color) => new Paragraph({ spacing:{ before:140, after:90 }, keepNext:true, children:[ run(' '+tag+' ', { size:16, bold:true, color:C.white, bg:color }), run('   '+title, { size:18, bold:true, color:C.purple }), run(note ? '   · '+note : '', { size:14, color:C.muted }) ] });
const bandW = (part, title, sub) => [
  P([ run('  RAPORT OCENY FUNKCJONALNEJ DZIECKA / UCZNIA · CZĘŚĆ '+part+'  ', { size:13, bold:true, color:C.white, bg: part==='III' ? C.purple : C.orange, spacing:10 }) ], { align:AlignmentType.CENTER, after:120 }),
  P([ run(title, { size:28, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:60, line:300 }),
  P([ run(sub.toUpperCase(), { size:12, bold:true, color:C.orange, spacing:30 }) ], { align:AlignmentType.CENTER, after:60 })
];
const chk = (on) => run(on ? '☑  ' : '☐  ', { size:20, color: on ? C.orange : 'B6A6DF' });
const labelP = (t) => P([ run(t, { size:13, bold:true, color:C.purple, caps:true, spacing:12 }) ], { before:60, after:60 });
const simpleTable = (heads, widths, rows, o={}) => tbl(widths, [ gridHead(heads, widths, o.headColors), ...rows.map(r => row(r.map((c,i) => gcell(Array.isArray(c)?c:txt(c, { size:15, bold: i===0 || (o.boldCols||[]).includes(i), color: (i===0 || (o.purpleCols||[]).includes(i)) ? C.purple : C.ink }), widths[i], { edge: i===0 ? o.edge : undefined, pad:o.pad })))) ]);
const statTile = (l, v, sub, width, top=C.orange) => cell([
  P([ run(l, { size:12, bold:true, color:C.lavText, spacing:12 }) ], { after:30 }),
  P([ run(v, { size:24, bold:true, color:C.purple }), run(sub ? '  '+sub : '', { size:14, color:C.muted }) ], { after:0 })
], { width, borders:{ top:{ style:BorderStyle.SINGLE, size:24, color:top }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:70, bottom:70, left:160, right:120 } });
const parentBox = (t) => tbl([CW], [ row([ cell(P([ run('Informacja dla rodzica. ', { size:17, bold:true, color:C.orange }), run(t, { size:17 }) ], { after:0, line:270 }), { width:CW, bg:C.paper, borders:{ top:ln(C.line2), bottom:ln(C.line2), left:ln(C.line2), right:ln(C.line2) }, margins:{ top:120, bottom:120, left:220, right:220 } }) ]) ]);
const LVL = { 1:{ bg:'E6F4EC', fg:C.green }, 2:{ bg:'FBF1DC', fg:'9A6A0A' }, 3:{ bg:'FBE6E3', fg:C.red } };
const half = Math.floor(CW/2);

// ---- 4 ----
const s4 = D.s4, W4 = [1900, 4003, 4003];
const part4 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Funkcjonowanie w placówce'),
  ...bandW('II','Wyniki oceny funkcjonalnej','obserwacja · wyniki liczbowe · arkusze · głos dziecka · analiza · decyzja Zespołu'),
  section('4', s4.title), lead2(s4.ref, s4.lead),
  tbl(W4, [ gridHead(['Obszar obserwacji','✓ Mocne strony, zasoby i uzdolnienia','▸ Trudności, ograniczenia i bariery'], W4, [C.purple, C.green, C.red]),
    ...s4.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W4[0]), gcell(txt(r[1]), W4[1], { edge:C.green }), gcell(txt(r[2]), W4[2], { edge:C.red }) ])) ]) ];

// ---- 5 ----
const s5 = D.s5, W5 = [600, 2500, 1500, 800, 1700, 2806], SWT = Math.floor(CW/4);
const part5 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Wyniki liczbowe'),
  section('5', s5.title), lead2(s5.ref, s5.lead),
  tbl([CW], [ row([ cell(P([ run('NARZĘDZIE BAZOWE:  ', { size:12, bold:true, color:C.lavText, spacing:12 }), chk(false), run('Przedszkole · KPOF', { size:16, bold:true, color:C.purple }), run('  (bez stenów)', { size:14, color:C.muted }), run('        ', { size:16 }), chk(false), run('Szkoła · KSzOF', { size:16, bold:true, color:C.purple }), run('  (ze stenami)', { size:14, color:C.muted }) ], { after:0 }), { width:CW, bg:C.lav, borders:noBorders, margins:{ top:70, bottom:70, left:180, right:180 } }) ]) ]),
  empty(60),
  tbl([SWT,SWT,SWT,SWT], [ row([ statTile('NARZĘDZIE BAZOWE','KPOF / KSzOF','',SWT), statTile('PUNKTY SUROWE',s5.punkty,'/ '+s5.punktyMax+' pkt',SWT), statTile('ŚREDNIA','Śr: '+s5.srednia,'w skali 0–5',SWT), statTile('OGÓLNY POZIOM WSPARCIA',s5.poziom,s5.poziomOpis,SWT,C.amber) ]) ]),
  empty(80),
  tbl(W5, [ gridHead(['Kod','Domena ICF','Punkty / śr.','Sten (KSzOF)','Poziom wsparcia','Wskaźnik funkcjonalny'], W5),
    ...s5.dom.map(d => row([ gcell(txt(d[0], { bold:true, color:C.orange }), W5[0]), gcell(txt(d[1], { bold:true }), W5[1]), gcell(txt('Śr: '+String(d[2]).replace('.',',')+' ('+d[3]+' pkt)'), W5[2]), gcell(txt('Sten '+d[4]), W5[3]), gcell(P([ run(' Poziom '+d[5]+' · '+d[6]+' ', { size:14, bold:true, color:LVL[d[5]].fg, bg:LVL[d[5]].bg }) ], { after:0 }), W5[4]), gcell(txt(d[7]), W5[5]) ])) ]),
  P([ run('Poziom 1 · Niski', { size:13, bold:true, color:LVL[1].fg, bg:LVL[1].bg }), run('    ', { size:13 }), run('Poziom 2 · Średni', { size:13, bold:true, color:LVL[2].fg, bg:LVL[2].bg }), run('    ', { size:13 }), run('Poziom 3 · Wysoki', { size:13, bold:true, color:LVL[3].fg, bg:LVL[3].bg }) ], { align:AlignmentType.RIGHT, before:100, after:0 }),
  P([ run('Zasada: ', { size:13, bold:true, color:C.purple }), run('KPOF (przedszkole) nie posiada norm stenowych – kolumnę „Sten” pozostawia się pustą; interpretacja na podstawie punktów, średniej i poziomu wsparcia. KSzOF (szkoła) – steny wyłącznie w kolumnie „Sten” dla domen. Średniej nigdy nie opisuje się stenem.', { size:13, color:C.muted }) ], { before:80, after:0, line:250, align:AlignmentType.JUSTIFIED }) ];

// ---- 6 ----
const s6 = D.s6, CC = { red:C.red, blue:C.blue, purple:C.purple, orange:C.orange, green:C.green };
const part6 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Wyniki arkuszy specjalistycznych'), section('6', s6.title),
  ...s6.cards.flatMap(([c, title, parts, rec]) => [
    tbl([CW], [ row([ cell([
      P([ run(title, { size:18, bold:true, color:C.purple }) ], { after:50 }),
      P(parts.map(pt => run(pt[0], { size:16, bold:!!pt[1], color: pt[1] ? CC[c] : C.ink })), { after: rec ? 50 : 0, line:255, align:AlignmentType.JUSTIFIED }),
      ...(rec ? [ P([ run('Zalecenie: ', { size:16, bold:true, color:C.orange }), run(rec, { size:16, color:C.purple }) ], { after:0 }) ] : [])
    ], { width:CW, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:32, color:CC[c] } }, margins:{ top:110, bottom:120, left:220, right:180 } }) ]) ]), empty(90) ]) ];

// ---- 7 Mój głos ----
const s7 = D.s7;
const cbGrid = (items) => tbl([half, half], (() => { const rows=[]; for (let i=0;i<items.length;i+=2) rows.push(row([0,1].map(j => { const it=items[i+j]; return cell(it ? P([ chk(it[1]), run(it[0], { size:15 }) ], { after:0 }) : empty(), { width:half, borders:noBorders, margins:{ top:30, bottom:30, left:0, right:100 } }); }))); return rows; })());
const moodCols = ['2E9D52','7EB800','DFA22E','E77309','BF382A'];
const part7 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Mój głos'), section('7', s7.title), lead2('', s7.lead),
  labelP('Sposób pozyskania głosu dziecka – zaznaczono'), cbGrid(s7.sposoby), empty(80),
  tbl([half, half], [ row([0,1].map(i => { const [c,t,v]=s7.pola[i]; return cell([ labelP(t), P([ run(v, { size:16, italic:true }) ], { after:0, line:250 }) ], { width:half, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:24, color:CC[c] } }, margins:{ top:60, bottom:100, left:200, right:160 } }); })), row([2,3].map(i => { const [c,t,v]=s7.pola[i]; return cell([ labelP(t), P([ run(v, { size:16, italic:true }) ], { after:0, line:250 }) ], { width:half, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:24, color:CC[c] } }, margins:{ top:60, bottom:100, left:200, right:160 } }); })) ]),
  empty(80), labelP('Co mi najbardziej pomaga – zaznaczono'), cbGrid(s7.pomaga), empty(60),
  labelP('Jak się dziś czuję – wskazanie dziecka'),
  P(s7.nastroj.flatMap((n,i) => [ run('   ', { size:20, bg:moodCols[i] }), run((i===s7.nastrojWybor ? ' ☑ ' : '  ')+n+'      ', { size:15, bold: i===s7.nastrojWybor, color: i===s7.nastrojWybor ? C.orange : C.muted }) ]), { after:120 }),
  box([ labelP('Preferowany sposób komunikacji dziecka i wskazówki do rozmowy'), P([ run(s7.komunikacja, { size:16 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.blue),
  P([ run('Podstawa. ', { size:13, bold:true, color:C.purple }), run(s7.podstawa, { size:13, color:C.muted }) ], { before:80, after:0 }) ];

// ---- 8 ----
const s8 = D.s8, W8 = [2000, 4300, 3606];
const part8 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Działania dotychczas podjęte'), section('8', s8.title), lead2(s8.ref, s8.lead),
  tbl(W8, [ gridHead(['Rodzaj wsparcia','Zakres wdrożonych działań i metody','Efektywność i obserwowane zmiany'], W8, [C.purple, C.purple, C.green]),
    ...s8.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W8[0]), gcell(txt(r[1]), W8[1]), gcell(txt(r[2]), W8[2], { edge:C.green }) ])) ]),
  empty(140), parentBox('Wyniki z sekcji 4–8 są podstawą analizy (sekcja 9) i decyzji Zespołu o poziomie wsparcia (sekcja 10). Część III opisuje, jak placówka zorganizuje wsparcie w tym roku szkolnym.') ];

// ---- 9 ----
const s9 = D.s9, W6 = [1900, 3900, 4106];
const part9 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Analiza jakościowa'), section('9', s9.title), lead2('', s9.lead),
  tbl(W6, [ gridHead(['Domena ICF','Opis funkcjonowania i bariery','Kierunki pracy w IPE (metody / dostosowania)'], W6, [C.purple, C.purple, C.orange]),
    ...s9.rows.map(r => row([ gcell([ txt(r[1], { bold:true, color:C.purple }), txt(r[0], { size:14, color:C.orange, bold:true }) ], W6[0]), gcell(txt(r[2]), W6[1]), gcell(bullets(r[3]), W6[2]) ])) ]) ];

// ---- 10 ----
const s10 = D.s10, TW = Math.floor(CW/3);
const part10 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Decyzja Zespołu'), section('10', s10.title), lead2('', s10.lead),
  tbl([TW,TW,TW], [ row(s10.poziomy.map(([k,t,d,on]) => cell([ P([ chk(on), run(t, { size:16, bold:true, color:C.purple }) ], { after:40 }), P([ run(d, { size:14, color:C.muted }) ], { after:0, line:240 }) ], { width:TW, bg: on ? C.orangeMist : C.white, borders:{ top:ln(on?C.orange:C.line), bottom:ln(on?C.orange:C.line), left:ln(on?C.orange:C.line), right:ln(on?C.orange:C.line) }, margins:{ top:110, bottom:110, left:160, right:140 } }))) ]),
  empty(120), box([ labelP('Uzasadnienie decyzji Zespołu'), P([ run(s10.uzasadnienie, { size:16 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.orange), empty(100),
  tbl([SWT,SWT,SWT,SWT], [ row(s10.wymiar.map(([k,v]) => cell([ P([ run(k.toUpperCase(), { size:12, bold:true, color:C.lavText, spacing:12 }) ], { after:30 }), P([ run(v, { size:15, bold:true, color:C.purple }) ], { after:0, line:240 }) ], { width:SWT, bg:C.lav, borders:{ top:ln(C.white,12), bottom:ln(C.white,12), left:ln(C.white,12), right:ln(C.white,12) }, margins:{ top:90, bottom:90, left:140, right:100 } }))) ]),
  empty(100), P([ run('Data posiedzenia Zespołu: ', { size:15, bold:true, color:C.purple }), ph(s10.dataDecyzji), run('   ·   '+s10.zgodaRodzica+'   ·   ', { size:15, color:C.muted }), run('Podpisy Zespołu i rodzica: ', { size:15, bold:true, color:C.purple }), run('na końcu dokumentu (sekcja 16).', { size:15, color:C.muted }) ], { after:0, line:260 }) ];

// ---- 11 ----
const s11 = D.s11, W11 = [2400, CW-2400];
const kvTable = (rows, h1, h2) => tbl(W11, [ gridHead([h1,h2], W11), ...rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W11[0]), gcell(txt(r[1]), W11[1]) ])) ]);
const part11 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część III · Dostosowanie programu'),
  ...bandW('III','Program wsparcia i organizacja','dostosowania · zintegrowane działania · zajęcia · dodatkowa osoba · rodzice i poradnia · ocena efektywności'),
  section('11', s11.title),
  P([ run('Dostosowania wynikają z analizy jakościowej (sekcja 9) i decyzji o poziomie wsparcia (sekcja 10). Dotyczą:  ', { size:16, color:C.muted }), chk(false), run('programu wychowania przedszkolnego    ', { size:16, bold:true, color:C.purple }), chk(false), run('podstawy programowej kształcenia ogólnego (szkoła)', { size:16, bold:true, color:C.purple }) ], { after:120, line:260 }),
  sub9('A', s11.A.title, '', C.orange), kvTable(s11.A.rows, 'Zakres', 'Sposób dostosowania'),
  pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część III · Organizacja i technologie'),
  sub9('B', s11.B.title, '', C.blue), kvTable(s11.B.rows, 'Obszar organizacji', 'Sposób dostosowania'),
  sub9('C', s11.C.title, '', C.purple), kvTable(s11.C.rows, 'Obszar', 'Narzędzia i sposób wykorzystania') ];

// ---- 12 ----
const s12 = D.s12, W12 = [1800, 3000, 3000, 2106];
const part12 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część III · Zintegrowane działania'), section('12', s12.title), lead2('', s12.lead),
  tbl(W12, [ gridHead(['Wspólny cel','Nauczyciel / wychowawca (codziennie w grupie)','Specjaliści (zajęcia)','Sposób koordynacji'], W12),
    ...s12.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W12[0]), gcell(txt(r[1]), W12[1]), gcell(txt(r[2]), W12[2]), gcell(txt(r[3]), W12[3]) ])) ]),
  empty(120), box([ P([ run('Koordynacja. ', { size:16, bold:true, color:C.orange }), run(s12.koordynacja, { size:16 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.orange, { bg:C.lav2 }) ];

// ---- 13 ----
const s13 = D.s13, WZ = [3000, 2800, 1500, 1300, 1306], WP = [2500, 1900, 1250, 1550, 1450, 1256], WM = [400, 3300, 3300, 1500, 1406];
const zajTable = (rows, edge, sumLabel, sumVal, sumSub) => tbl(WZ, [ gridHead(['Rodzaj zajęć','Zakres / cel','Prowadzący','Forma','Wymiar tyg.'], WZ),
  ...rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:15 }), WZ[0], { edge, pad:50 }), gcell(txt(r[1], { size:15 }), WZ[1], { pad:50 }), gcell(txt(r[2], { bold:true, color:C.purple, size:15 }), WZ[2], { pad:50 }), gcell(txt(r[3], { size:15 }), WZ[3], { pad:50 }), gcell([ txt(r[4], { bold:true, color:C.purple, size:15 }), txt(r[5], { size:12, color:C.muted }) ], WZ[4], { pad:50 }) ])),
  row([ cell(txt(sumLabel, { bold:true, color:C.purple, size:15 }), { width:WZ[0]+WZ[1]+WZ[2]+WZ[3], span:4, bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:80, left:140, right:120 } }), cell([ txt(sumVal, { bold:true, color:C.purple, size:15 }), txt(sumSub, { size:12, color:C.muted }) ], { width:WZ[4], bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:80, left:140, right:120 } }) ]) ]);
const pppTable = tbl(WP, [ gridHead(['Forma pomocy','Cel','Prowadzący','Forma i miejsce','Czas i termin','Okres udzielania'], WP),
  ...s13.ppp.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:13 }), WP[0], { edge:C.blue, pad:40 }), gcell(txt(r[1], { size:13 }), WP[1], { pad:40 }), gcell(txt(r[2], { bold:true, color:C.purple, size:13 }), WP[2], { pad:40 }), gcell(txt(r[3], { size:13 }), WP[3], { pad:40 }), gcell(txt(r[4], { bold:true, color:C.purple, size:13 }), WP[4], { pad:40 }), gcell(txt(r[5], { size:13 }), WP[5], { pad:40 }) ])),
  row([ cell(txt('Razem pomoc psychologiczno-pedagogiczna', { bold:true, color:C.purple, size:15 }), { width:CW-WP[5], span:5, bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:80, left:140, right:120 } }), cell([ txt(s13.sumPpp[0], { bold:true, color:C.purple, size:15 }), txt(s13.sumPpp[1], { size:12, color:C.muted }) ], { width:WP[5], bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:80, left:140, right:120 } }) ]) ]);
const statusCell = (w) => gcell(['wdrożone','w trakcie','planowane'].map(t => P([ run('☐ ', { size:15, color:'B6A6DF' }), run(t, { size:12, color:C.muted }) ], { after:0, line:220 })), w);
const part13 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część III · Zajęcia: rewalidacja i PPP'), section('13', s13.title), lead2('', s13.lead),
  tbl([half, CW-half], [ row([ statTile('A · ZAJĘCIA REWALIDACYJNE · RAZEM', s13.sumRew[0], '= '+s13.sumRew[1]+' · '+s13.sumRew[2], half), statTile('B · POMOC PSYCHOLOGICZNO-PEDAGOGICZNA · RAZEM', s13.sumPpp[0], '= '+s13.sumPpp[1]+' · '+s13.sumPpp[2], CW-half, C.blue) ]) ]),
  sub9('A','Zajęcia rewalidacyjne przydzielone dziecku / uczniowi','kształcenie specjalne · na podstawie orzeczenia', C.orange), zajTable(s13.rew, C.orange, 'Razem zajęcia rewalidacyjne', s13.sumRew[0], s13.sumRew[1]),
  sub9('B','Zajęcia z zakresu pomocy psychologiczno-pedagogicznej','forma · czas · termin · okres udzielania · miejsce', C.blue), pppTable,
  pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część III · Realizacja zaleceń poradni'),
  P([ run('Uwaga: ', { size:13, bold:true, color:C.purple }), run(s13.uwaga, { size:13, color:C.muted }) ], { after:60 }),
  sub9('C','Zalecenia poradni i miejsce ich realizacji w programie','każde zalecenie wskazuje sekcję, w której jest realizowane', C.purple),
  P([ run('Orzeczenie / opinia nr ', { size:16, color:C.muted }), ph(D.meta.nrOrzeczenia), run(' z dnia ', { size:16, color:C.muted }), ph(D.meta.dataOrzeczenia), run('.', { size:16, color:C.muted }) ], { after:100 }),
  tbl(WM, [ gridHead(['Lp.','Zalecenie poradni (z orzeczenia / opinii)','Sposób realizacji w placówce','Gdzie w raporcie','Status'], WM, [C.purple, C.purple, C.orange, C.purple, C.purple]),
    ...s13.mapa.map((z,i) => row([ gcell(txt(String(i+1), { bold:true, color:C.orange, size:15 }), WM[0]), gcell(txt(z[0], { bold:true, size:15 }), WM[1]), gcell(txt(z[1], { size:15 }), WM[2]), gcell(P([ run(' '+z[2]+' ', { size:13, bold:true, color:C.orange, bg:C.orangeMist }) ], { after:0 }), WM[3]), statusCell(WM[4]) ])) ]) ];

// ---- 14 ----
const s14 = D.s14;
const part14 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część III · Dodatkowa osoba'), section('14', s14.title),
  P(s14.rodzaj.flatMap(([t,on]) => [ chk(on), run(t+'      ', { size:15, bold:true, color:C.purple }) ]), { after:120 }),
  tbl([Math.floor(CW/3), CW-Math.floor(CW/3)], [ row([ cell([ P([ run('WYMIAR I SYTUACJE', { size:12, bold:true, color:C.lavText, spacing:12 }) ], { after:30 }), P([ run(s14.wymiar, { size:15, bold:true, color:C.purple }) ], { after:0, line:240 }) ], { width:Math.floor(CW/3), bg:C.lav, borders:noBorders, margins:{ top:90, bottom:90, left:140, right:100 } }), cell([ P([ run('PODSTAWA PRAWNA I FORMALNA', { size:12, bold:true, color:C.lavText, spacing:12 }) ], { after:30 }), P([ run(s14.podstawa, { size:14, color:C.purple }) ], { after:0, line:240 }) ], { width:CW-Math.floor(CW/3), bg:C.lav, borders:{ top:NOB, bottom:NOB, right:NOB, left:ln(C.white,12) }, margins:{ top:90, bottom:90, left:140, right:100 } }) ]) ]),
  empty(120), box([ labelP('Uzasadnienie wynikające z oceny funkcjonalnej'), P([ run(s14.uzasadnienie, { size:16 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.orange), empty(100),
  box([ labelP('Zadania dodatkowej osoby'), ...bullets(s14.zadania, '✓', C.green) ], C.green), empty(100),
  box([ P([ run('Ocena zasadności. ', { size:16, bold:true, color:C.orange }), run(s14.ocena, { size:16 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.orange, { bg:C.lav2 }) ];

// ---- 15 ----
const s15 = D.s15, W15 = [2200, 3700, 2000, 2006];
const part15 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część III · Współpraca z rodzicami i poradnią'), section('15', s15.title),
  sub9('A', s15.A.title, '', C.orange), simpleTable(['Forma współpracy','Zakres','Odpowiedzialny','Częstotliwość'], W15, s15.A.rows, { purpleCols:[2], boldCols:[2], pad:50 }),
  sub9('B', s15.B.title, '', C.green), box([ ...bullets(s15.B.items, '✓', C.green) ], C.green),
  sub9('C', s15.C.title, '', C.purple), simpleTable(['Działanie','Zakres / cel','Kto','Termin'], W15, s15.C.rows, { purpleCols:[2], boldCols:[2], pad:50 }) ];

// ---- 16 + podpisy ----
const s16 = D.s16, W16 = [1600, 3500, 2300, 1400, 1106], STC = { 'wykonano':LVL[1], 'w trakcie':LVL[2], 'planowane':{ bg:C.lav, fg:C.purple } };
const part16 = [ pb(), ...pageHeader('Raport Oceny Funkcjonalnej · Część III · Ocena efektywności · podpisy'), section('16', s16.title), lead2('', s16.lead),
  tbl(W16, [ gridHead(['Termin','Zakres oceny','Narzędzia','Odpowiedzialny','Status'], W16),
    ...s16.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:15 }), W16[0]), gcell(txt(r[1], { size:15 }), W16[1]), gcell(txt(r[2], { size:15 }), W16[2]), gcell(txt(r[3], { size:15 }), W16[3]), gcell(P([ run(' '+r[4]+' ', { size:13, bold:true, color:STC[r[4]].fg, bg:STC[r[4]].bg }) ], { after:0 }), W16[4]) ])) ]),
  empty(140), parentBox('Niniejszy raport stanowi opinię placówki o funkcjonowaniu dziecka i jest przekazywany rodzicowi oraz zespołowi orzekającemu poradni. Wyniki obserwacji służą zaplanowaniu wsparcia, a nie ocenie dziecka. Zachęcamy do rozmowy z Zespołem o każdej części dokumentu.'),
  empty(60), sigs ];

const part2 = [ ...part4, ...part5, ...part6, ...part7, ...part8, ...part9, ...part10, ...part11, ...part12, ...part13, ...part14, ...part15, ...part16 ];

const children = [
  ...cover,
  ...pageHeader('Raport Oceny Funkcjonalnej · Metryczka i obserwacja wstępna'),
  section('1','Metryczka bazowa'),
  meta,
  section('2','Podstawa i procedura obserwacji wstępnej'),
  flow,
  empty(100),
  box([ P([ run('Z uwagi na zgłaszane trudności w funkcjonowaniu, wniosek rodzica oraz posiadaną dokumentację (w tym opinię/orzeczenie poradni), w placówce przeprowadzono ', { size:18 }), run('we wrześniu', { size:18, bold:true, color:C.orange }), run(' obserwację poziomu funkcjonowania z wykorzystaniem ', { size:18 }), run('Kwestionariusza Przedszkolnej / Szkolnej Oceny Funkcjonalnej', { size:18, bold:true, color:C.orange }), run(', analizującego funkcjonowanie w obszarach zgodnych z Międzynarodową Klasyfikacją Funkcjonowania, Niepełnosprawności i Zdrowia (ICF).', { size:18 }) ], { align:AlignmentType.JUSTIFIED, after:0, line:290 }) ], C.orange, { bg:C.lav2 }),
  empty(120),
  icfRow,
  new Paragraph({ children:[ new PageBreak() ] }),
  ...pageHeader('Raport Oceny Funkcjonalnej · Obserwacja pogłębiona'),
  section('3','Wskazania do obserwacji pogłębionej i zastosowane narzędzia'),
  P([ run('W związku ze zidentyfikowanymi w toku oceny wstępnej trudnościami w funkcjonowaniu – w szczególności w zakresie ', { size:18 }), run('trudnych zachowań', { size:18, bold:true, color:C.purple }), run(', ', { size:18 }), run('rozwoju funkcji poznawczych', { size:18, bold:true, color:C.purple }), run(', ', { size:18 }), run('przetwarzania bodźców', { size:18, bold:true, color:C.purple }), run(' oraz ', { size:18 }), run('komunikacji', { size:18, bold:true, color:C.purple }), run(' – przeprowadzono obserwację pogłębioną z wykorzystaniem następujących narzędzi specjalistycznych:', { size:18 }) ], { after:180, line:290, align:AlignmentType.JUSTIFIED }),
  ...tools,
  ...part2
];

const doc = new Document({
  creator: 'EduPlaner2026-MJ-PCTP', title: 'Raport Oceny Funkcjonalnej', description: 'Opinia przedszkola/szkoły dla zespołu orzekającego i rodzica (obszary ICF)',
  styles:{ default:{ document:{ run:{ font:FONT, size:20, color:C.ink } } } },
  sections:[{
    properties:{ page:{ size:A4, margin:MARGINS } },
    footers:{ default: new Footer({ children:[ footerPara ] }) },
    children
  }]
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(process.argv[2] || 'Raport_Oceny_Funkcjonalnej.docx', buf); console.log('OK', buf.length); });
