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
const MARGINS = { top: 1100, right: 850, bottom: 1100, left: 850, header: 500, footer: 500 };

const CW = 11906 - 1700; // 10206

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
const ph = (t) => run(t, { italic:true, color:C.muted, size:24 });
const label = (t, o={}) => P([ run(t, { size:o.size||13, bold:true, color:o.color||C.purple, caps:true, spacing:o.spacing??12 }) ], { after:o.after??60 });

// ---- pudełko wzór IPET: obrys lawendowy + kolorowa lewa krawędź ----
const box = (children, edge=C.orange, o={}) => tbl([CW], [ row([ cell(children, { width:CW, bg:o.bg||C.white, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:32, color:edge } }, margins:{ top:130, bottom:130, left:240, right:240 } }) ]) ]);

// ---- nagłówek strony (wzór IPET) ----
const pageHeader = (caption) => [
  tbl([700, 6200, 3006], [ row([
    cell(P([ run('§', { size:24, bold:true, color:C.white }) ], { align:AlignmentType.CENTER, after:0 }), { width:700, bg:C.purple, borders:noBorders, vAlign:VerticalAlign.CENTER, margins:{ top:120, bottom:120, left:40, right:40 } }),
    cell([ P([ run('[Nazwa przedszkola / szkoły]', { size:28, bold:true, color:C.purple }) ], { after:20 }), P([ run(caption, { size:20, color:C.muted, caps:true, spacing:12 }) ], { after:0 }) ], { width:6200, borders:noBorders, vAlign:VerticalAlign.CENTER, margins:{ top:0, bottom:0, left:160, right:0 } }),
    cell([ P([ run('  OCENA FUNKCJONALNA · 2026  ', { size:20, bold:true, color:C.white, bg:C.orange, spacing:8 }) ], { align:AlignmentType.RIGHT, after:60 }), P([ run('DOKUMENT DLA RODZICA I PORADNI', { size:20, color:C.muted, spacing:10 }) ], { align:AlignmentType.RIGHT, after:0 }) ], { width:3006, borders:noBorders, vAlign:VerticalAlign.CENTER, margins:{ top:0, bottom:0, left:0, right:0 } })
  ]) ]),
  new Paragraph({ spacing:{ before:60, after:160 }, border:{ bottom:{ style:BorderStyle.SINGLE, size:24, color:C.purple, space:1 } }, children:[] }),
  // lawendowe pola
  tbl([3900, 2900, 2906], [ row([
    ['DOTYCZY DZIECKA', 3900], ['GRUPA / KLASA', 2900], ['DATA', 2906]
  ].map(([t,w]) => cell(P([ run(t, { size:24, bold:true, color:C.lavText, spacing:12 }), run('  ' + '.'.repeat(w===3900?40:22), { size:24, color:'B6A6DF' }), run(t==='DATA'?'  r.':'', { size:24, color:C.muted }) ], { after:0 }), { width:w, bg:C.lav, borders:{ top:ln(C.white,12), bottom:ln(C.white,12), left:ln(C.white,12), right:ln(C.white,12) }, margins:{ top:110, bottom:110, left:180, right:120 } })) ) ]),
  empty(120)
];

// ---- nagłówek sekcji: pomarańczowy numer + fiolet + linia ----
const section = (n, title) => new Paragraph({
  spacing:{ before:200, after:140 }, keepNext:true,
  border:{ bottom:{ style:BorderStyle.SINGLE, size:24, color:C.line, space:6 } },
  children:[ run(' '+n+' ', { size:24, bold:true, color:C.white, bg:C.orange }), run('   ', { size:24 }), run(title.toUpperCase(), { size:24, bold:true, color:C.purple, spacing:10 }) ]
});

// =============== STRONA 1 · OKŁADKA ===============
const cover = [
  ...pageHeader('Ocena Funkcjonalna · Okładka'),
  P([ run('  OPINIA PRZEDSZKOLA / SZKOŁY · DLA ZESPOŁU ORZEKAJĄCEGO · DLA RODZICA  ', { size:24, bold:true, color:C.white, bg:C.orange, spacing:12 }) ], { align:AlignmentType.CENTER, before:40, after:120 }),
  P([ run('OBSERWACJA WSTĘPNA I POGŁĘBIONA · ICF · PRZEDSZKOLE · SZKOŁA', { size:24, color:C.purple, spacing:50 }) ], { align:AlignmentType.CENTER, after:60 }),
  P([ run('Ocena Funkcjonalna', { size:52, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:80, line:600, lineRule:'exact' }),
  P([ run('RAPORT – PODSUMOWANIE WOPF I IPET · OBSZARY ICF', { size:24, bold:true, color:C.orange, spacing:44 }) ], { align:AlignmentType.CENTER, after:140 }),
  P([ run('z dnia  ', { size:24, color:C.muted }), run('………………………………………………', { size:24, color:'B6A6DF' }) ], { align:AlignmentType.CENTER, after:160 }),

  // zespół
  box([
    label('Opracowany przez Zespół w składzie'),
    tbl([Math.floor((CW-480)/2), Math.floor((CW-480)/2)], [0,1,2].map(r => row([0,1].map(c => {
      const n = r*2+c+1, w = Math.floor((CW-480)/2);
      return cell(P([ run(n+'.', { bold:true, color:C.orange, size:24 }), run('  ' + '.'.repeat(58), { size:24, color:'B6A6DF' }) ], { after:0 }), { width:w, borders:noBorders, margins:{ top:40, bottom:40, left:0, right:200 } });
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
          run('Zgodnie z Rozporządzeniem Ministra Edukacji z dnia 2 marca 2026 r. w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające działające w publicznych poradniach psychologiczno-pedagogicznych ', { size:24 }),
          run('(Dz. U. z 2026 r. poz. 428)', { size:24, bold:true, color:C.purple }),
          run(', a w szczególności wchodzącymi w życie z dniem 1 września 2026 r. przepisami ', { size:24 }),
          run('§ 7 ust. 6 i ust. 7', { size:24, bold:true, color:C.purple }),
          run(', opinia przedszkola/szkoły wydawana dla zespołu poradni (i przekazywana rodzicowi) musi mieć ściśle określoną strukturę opartą na obszarach ICF: odrębnych dla dziecka w wieku przedszkolnym oraz dla ucznia szkoły.', { size:24 })
        ], { align:AlignmentType.JUSTIFIED, after:0, line:290 })
      ], { width:CW-480-700, borders:noBorders, margins:{ top:0, bottom:0, left:200, right:0 } })
    ]) ])
  ], C.purple, { bg:C.lav2 }),
  empty(120),

  new Paragraph({ children:[ new PageBreak() ] })
];

// =============== STRONA 2 · METRYCZKA + PROCEDURA ===============
const LW = 3000, RW = CW-LW;
const vp = (children) => P(children, { after:0, line:270 });
const checkbox = (children) => P([ run('☐  ', { size:24, color:'B6A6DF' }), ...children ], { before:30, after:30, line:260 });
const metaRow = (lbl, valueChildren) => row([
  cell(P([ run(lbl, { size:24, bold:true, color:C.purple, caps:true, spacing:10 }) ], { after:0 }), { width:LW, bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:100, bottom:100, left:180, right:120 } }),
  cell(valueChildren, { width:RW, borders:{ top:ln(C.line2), bottom:ln(C.line2), left:ln(C.line2), right:ln() }, margins:{ top:90, bottom:90, left:180, right:180 } })
]);
const meta = tbl([LW,RW], [
  metaRow('Imię i nazwisko', vp([ ph('[Imię i Nazwisko dziecka / ucznia]') ])),
  metaRow('Data urodzenia', vp([ ph('[Data urodzenia]') ])),
  metaRow('Placówka / Oddział', vp([ ph('[Nazwa przedszkola / szkoły, grupa / klasa]') ])),
  metaRow('Wariant wsparcia', [
    checkbox([ run('Wariant A', { bold:true, color:C.purple, size:24 }), run(' – wsparcie na podstawie orzeczenia o potrzebie kształcenia specjalnego', { size:24 }) ]),
    checkbox([ run('Wariant B', { bold:true, color:C.purple, size:24 }), run(' – wsparcie w ramach pomocy psychologiczno-pedagogicznej (bez orzeczenia)', { size:24 }) ])
  ]),
  metaRow('Jednostka / Podstawa formalna', vp([ run('Na podstawie dołączonego dokumentu: ', { size:24 }), ph('[Orzeczenie / Opinia]'), run(' nr ', { size:24 }), ph('[Numer]'), run(' z dnia ', { size:24 }), ph('[Data]'), run(', wydanego przez: ', { size:24 }), ph('[Nazwa Poradni]'), run(', z uwagi na: ', { size:24 }), ph('[np. autyzm, w tym zespół Aspergera / niepełnosprawność ruchowa / inne]') ])),
  metaRow('Schorzenia przewlekłe', [
    checkbox([ run('Brak', { size:24 }) ]),
    checkbox([ run('Występują: ', { size:24 }), ph('[np. cukrzyca, astma, epilepsja]') ])
  ]),
  metaRow('Farmakoterapia i wskazania lekarza', vp([ run('Zgodnie ze wskazaniami lekarza dziecko/uczeń ', { size:24 }), run('stale / doraźnie', { size:24, bold:true }), run(' przyjmuje leki: ', { size:24 }), ph('[Nazwa leków, zalecenia postępowania / Nie dotyczy]') ]))
]);

const steps = [
  ['1','Zgłoszenie','zgłaszane trudności w funkcjonowaniu oraz wniosek rodzica'],
  ['2','Dokumentacja','posiadana opinia / orzeczenie poradni psychologiczno-pedagogicznej'],
  ['3','Obserwacja · wrzesień','KPOF (przedszkole) lub KSzOF (szkoła) – 9 domen ICF'],
  ['4','Analiza ICF','obszary zgodne z Międzynarodową Klasyfikacją Funkcjonowania']
];
const SW = Math.floor(CW/4);
const flow = tbl([SW,SW,SW,SW], [ row(steps.map(s => cell([
  P([ run(' '+s[0]+' ', { size:24, bold:true, color:C.orange, bg:C.lav }) ], { after:60 }),
  P([ run(s[1], { size:24, bold:true, color:C.purple }) ], { after:50 }),
  P([ run(s[2], { size:24, color:C.muted }) ], { after:0, line:240 })
], { width:SW, margins:{ top:100, bottom:100, left:150, right:150 } }))) ]);

const icfRow = tbl([1981,1981,1981,1981,1982], [ row([
  ['Funkcje ciała','b'],['Struktury ciała','s'],['Aktywność i uczestnictwo','d'],['Czynniki środowiskowe','e'],['Czynniki osobowe','—']
].map((t,i) => cell([
  P([ run(t[0], { size:24, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:20 }),
  P([ run(t[1], { size:24, bold:true, color:C.lavText }) ], { align:AlignmentType.CENTER, after:0 })
], { width:i===4?1982:1981, bg:C.lav, borders:{ top:ln(C.white,12), bottom:ln(C.white,12), left:ln(C.white,12), right:ln(C.white,12) }, margins:{ top:110, bottom:110, left:80, right:80 }, vAlign:VerticalAlign.CENTER }))) ]);

// =============== STRONA 3 · NARZĘDZIA ===============
const toolCell = (tag, title, desc, color, width, extra=[]) => cell([
  P([ run(tag.toUpperCase(), { size:24, bold:true, color, spacing:14 }) ], { after:40 }),
  P([ run(title, { size:24, bold:true, color:C.purple }) ], { after:70, line:250 }),
  P([ run(desc, { size:24 }) ], { after:0, line:255 }),
  ...extra
], { width, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:32, color } }, margins:{ top:120, bottom:130, left:220, right:180 } });

const HW = CW/2;
const abcRow = tbl([3100,3100,3100], [ row([
  ['A','bodźce wyzwalające'],['B','forma zachowania'],['C','funkcja i skutki podtrzymujące']
].map(t => cell([
  P([ run(t[0], { size:28, bold:true, color:C.red }) ], { align:AlignmentType.CENTER, after:10 }),
  P([ run(t[1], { size:24, bold:true, color:C.red }) ], { align:AlignmentType.CENTER, after:0 })
], { width:3100, bg:C.orangeMist, borders:{ top:NOB, bottom:NOB, left:ln(C.white,24), right:ln(C.white,24) }, margins:{ top:90, bottom:90, left:60, right:60 } }))) ]);

const tools = [
  tbl([CW], [ row([ toolCell('1 · Całościowy obraz','Profil Biopsychospołeczny','Ujęcie funkcjonowania dziecka w wymiarze biologicznym, psychologicznym i społecznym – zgodnie z modelem ICF; punkt wyjścia do interpretacji pozostałych arkuszy.', C.purple, CW) ]) ]),
  empty(100),
  tbl([CW], [ row([ toolCell('2 · Zachowania trudne','Arkusz Obserwacji Behawioralnej ABC','Zastosowany z uwagi na występowanie zachowań trudnych – identyfikacja bodźców wyzwalających, formy zachowania oraz funkcji i skutków podtrzymujących.', C.red, CW, [ empty(110), abcRow ]) ]) ]),
  empty(100),
  tbl([HW,HW], [
    row([
      toolCell('3 · Przetwarzanie bodźców','Profil Sensoryczny','Ocena reaktywności sensorycznej (nadwrażliwości, podwrażliwości, poszukiwania stymulacji) i wpływu bodźców środowiskowych na dysregulację dziecka.', C.blue, HW),
      toolCell('4 · Komunikacja','Arkusz Oceny Rozwoju Mowy i Komunikacji','Zastosowany w związku ze specyficznymi trudnościami w nadawaniu i rozumieniu mowy, echolaliami lub potrzebą wdrożenia / rozwijania AAC.', C.orange, HW)
    ])
  ]),
  empty(100),
  tbl([CW], [ row([ toolCell('5 · Funkcje poznawcze i społeczne','Arkusz Poziomu Rozwoju Teorii Umysłu (ToM)','Zbadanie poziomu rozumienia stanów mentalnych, intencji, perspektywy i emocji innych osób w sytuacjach społecznych.', C.green, CW) ]) ])
];

const sigCell = (role, width, span, top=300) => new TableCell({
  width:{ size:width, type:WidthType.DXA }, columnSpan: span,
  margins:{ top, bottom:20, left:220, right:220 }, borders:noBorders,
  children:[
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{ before:0, after:0 }, border:{ top:{ style:BorderStyle.SINGLE, size:24, color:C.purple, space:5 } }, children:[ run(role, { size:24, bold:true, color:C.purple }) ] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{ before:10, after:0 }, children:[ run('podpis i data', { size:24, color:C.muted }) ] })
  ]
});
const SGW = Math.floor(CW/3);
const sigs = tbl([SGW,SGW,SGW], [
  row([ sigCell('Koordynator Zespołu',SGW), sigCell('Dyrektor placówki',SGW), sigCell('Specjalista',SGW) ]),
  row([ sigCell('Rodzic / opiekun prawny – zapoznałam/em się z raportem', SGW*3, 3, 180) ])
]);

// =============== STOPKA ===============
const footerPara = new Paragraph({
  spacing:{ before:60, after:0 }, border:{ top:{ style:BorderStyle.SINGLE, size:24, color:C.line2, space:4 } },
  tabStops:[{ type:TabStopType.RIGHT, position:CW }],
  children:[ run('[Nazwa placówki] · dokument poufny (RODO)', { size:24, color:C.muted }), run('   · sporządzono w EduPlaner 2026', { size:24, color:'B6A6DF' }), run('\t'), run('Strona ', { size:24, color:C.muted }), new TextRun({ children:[PageNumber.CURRENT], font:FONT, size:24, bold:true, color:C.orange }), run(' z ', { size:24, color:C.muted }), new TextRun({ children:[PageNumber.TOTAL_PAGES], font:FONT, size:24, bold:true, color:C.purple }), run(' · Ocena Funkcjonalna', { size:24, color:C.muted }) ]
});


// =============== CZĘŚĆ II–III · DANE Z raport_data.json ===============
const lawP = (law) => law ? P([ run(' § Podstawa prawna: '+law+' ', { size:24, bold:true, color:C.purple, bg:C.lav }) ], { before:0, after:120 }) : empty(0);
const secL = (n, title, law) => [ section(n, title), lawP(law) ];
const path = require('path');
const D = JSON.parse(fs.readFileSync(path.join(__dirname, 'raport_data.json'), 'utf8'));
const pb = () => new Paragraph({ pageBreakBefore:true, spacing:{ before:0, after:0, line:20, lineRule:'exact' }, children:[ run('', { size:24 }) ] });
const gridHead = (cols, widths, colors=[]) => row(cols.map((t,i) => cell(P([ run(t, { size:24, bold:true, color:colors[i]||C.purple, caps:true, spacing:10 }) ], { after:0 }), { width:widths[i], bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:100, bottom:100, left:140, right:120 } })));
const gcell = (children, width, o={}) => cell(Array.isArray(children)?children:[children], { width, bg:o.bg, borders:{ top:ln(C.line2), bottom:ln(C.line2), right:ln(C.line2), left: o.edge ? { style:BorderStyle.SINGLE, size:28, color:o.edge } : ln(C.line2) }, margins:{ top:o.pad??70, bottom:o.pad??70, left:140, right:120 } });
const txt = (t, o={}) => P([ run(t, { size:o.size||24, bold:o.bold, color:o.color, italic:o.italic }) ], { after:0, line:270 });
const bullets = (items, mark='•', color=C.orange) => items.map(t => new Paragraph({ spacing:{ before:0, after:40, line:245 }, indent:{ left:200, hanging:200 }, children:[ run(mark+'  ', { size:24, color, bold:true }), run(t, { size:24 }) ] }));
const lead2 = (ref, t) => P([ ...(ref ? [run(ref+' ', { size:24, bold:true, color:C.purple })] : []), run(t, { size:24, color:C.muted }) ], { after:140, line:260, align:AlignmentType.JUSTIFIED });
const sub9 = (tag, title, note, color) => new Paragraph({ spacing:{ before:140, after:90 }, keepNext:true, children:[ run(' '+tag+' ', { size:24, bold:true, color:C.white, bg:color }), run('   '+title, { size:24, bold:true, color:C.purple }), run(note ? '   · '+note : '', { size:24, color:C.muted }) ] });
const bandW = (part, title, sub) => [
  P([ run('  OCENA FUNKCJONALNA DZIECKA / UCZNIA · PODSUMOWANIE WOPF I IPET · CZĘŚĆ '+part+'  ', { size:24, bold:true, color:C.white, bg: part==='III' ? C.purple : C.orange, spacing:10 }) ], { align:AlignmentType.CENTER, after:120 }),
  P([ run(title, { size:28, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:60, line:300 }),
  P([ run(sub.toUpperCase(), { size:24, bold:true, color:C.orange, spacing:30 }) ], { align:AlignmentType.CENTER, after:60 })
];
const chk = (on) => run(on ? '☑  ' : '☐  ', { size:24, color: on ? C.orange : 'B6A6DF' });
const labelP = (t) => P([ run(t, { size:24, bold:true, color:C.purple, caps:true, spacing:12 }) ], { before:60, after:60 });
const simpleTable = (heads, widths, rows, o={}) => tbl(widths, [ gridHead(heads, widths, o.headColors), ...rows.map(r => row(r.map((c,i) => gcell(Array.isArray(c)?c:txt(c, { size:24, bold: i===0 || (o.boldCols||[]).includes(i), color: (i===0 || (o.purpleCols||[]).includes(i)) ? C.purple : C.ink }), widths[i], { edge: i===0 ? o.edge : undefined, pad:o.pad })))) ]);
const statTile = (l, v, sub, width, top=C.orange) => cell([
  P([ run(l, { size:24, bold:true, color:C.lavText, spacing:12 }) ], { after:30 }),
  P([ run(v, { size:28, bold:true, color:C.purple }), run(sub ? '  '+sub : '', { size:24, color:C.muted }) ], { after:0 })
], { width, borders:{ top:{ style:BorderStyle.SINGLE, size:28, color:top }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:70, bottom:70, left:160, right:120 } });
const parentBox = (t) => tbl([CW], [ row([ cell(P([ run('Informacja dla rodzica. ', { size:24, bold:true, color:C.orange }), run(t, { size:24 }) ], { after:0, line:270 }), { width:CW, bg:C.paper, borders:{ top:ln(C.line2), bottom:ln(C.line2), left:ln(C.line2), right:ln(C.line2) }, margins:{ top:120, bottom:120, left:220, right:220 } }) ]) ]);
const LVL = { 1:{ bg:'E6F4EC', fg:C.green }, 2:{ bg:'FBF1DC', fg:'9A6A0A' }, 3:{ bg:'FBE6E3', fg:C.red } };
const half = Math.floor(CW/2);

// ---- 4 ----
const s4 = D.s4, W4 = [1900, 4003, 4003];
const t4 = (rows) => tbl(W4, [ gridHead(['Obszar (ICF)','✓ Mocne strony, zasoby i uzdolnienia','▸ Trudności, ograniczenia i bariery'], W4, [C.purple, C.green, C.red]),
    ...rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:24 }), W4[0], { pad:60 }), gcell(txt(r[1], { size:24 }), W4[1], { edge:C.green, pad:60 }), gcell(txt(r[2], { size:24 }), W4[2], { edge:C.red, pad:60 }) ])) ]);
const part4 = [ empty(480),
  ...bandW('II','Wyniki oceny funkcjonalnej','obserwacja · wyniki liczbowe · arkusze · głos dziecka · analiza · decyzja Zespołu'),
  ...secL('4', s4.title, s4.law), lead2(s4.ref, s4.lead),
  sub9('A', s4.titleA, 'wypełnić dla dziecka w przedszkolu', C.orange), t4(s4.rows),
  empty(360),
  section('4', s4.title+' · cd.'),
  sub9('B', s4.titleB, 'wypełnić dla ucznia szkoły', C.blue), t4(s4.rowsSzkola) ];

// ---- 5 ----
const s5 = D.s5, W5 = [600, 2500, 1500, 800, 1700, 2806], SWT = Math.floor(CW/4);
const part5 = [ empty(360),
  ...secL('5', s5.title, s5.law), lead2(s5.ref, s5.lead),
  tbl([CW], [ row([ cell(P([ run('NARZĘDZIE BAZOWE:  ', { size:24, bold:true, color:C.lavText, spacing:12 }), chk(false), run('Przedszkole · KPOF', { size:24, bold:true, color:C.purple }), run('  (bez stenów)', { size:24, color:C.muted }), run('        ', { size:24 }), chk(false), run('Szkoła · KSzOF', { size:24, bold:true, color:C.purple }), run('  (ze stenami)', { size:24, color:C.muted }) ], { after:0 }), { width:CW, bg:C.lav, borders:noBorders, margins:{ top:70, bottom:70, left:180, right:180 } }) ]) ]),
  empty(60),
  tbl([SWT,SWT,SWT,SWT], [ row([ statTile('NARZĘDZIE BAZOWE','KPOF / KSzOF','',SWT), statTile('PUNKTY SUROWE',s5.punkty,'/ '+s5.punktyMax+' pkt',SWT), statTile('ŚREDNIA','Śr: '+s5.srednia,'w skali 0–5',SWT), statTile('OGÓLNY POZIOM WSPARCIA',s5.poziom,s5.poziomOpis,SWT,C.amber) ]) ]),
  empty(80),
  tbl(W5, [ gridHead(['Kod','Domena ICF','Punkty / śr.','Sten (KSzOF)','Poziom wsparcia','Wskaźnik funkcjonalny'], W5),
    ...s5.dom.map(d => row([ gcell(txt(d[0], { bold:true, color:C.orange }), W5[0]), gcell(txt(d[1], { bold:true }), W5[1]), gcell(txt('Śr: '+String(d[2]).replace('.',',')+' ('+d[3]+' pkt)'), W5[2]), gcell(txt('Sten '+d[4]), W5[3]), gcell(P([ run(' Poziom '+d[5]+' · '+d[6]+' ', { size:24, bold:true, color:LVL[d[5]].fg, bg:LVL[d[5]].bg }) ], { after:0 }), W5[4]), gcell(txt(d[7]), W5[5]) ])) ]),
  P([ run('Poziom 1 · Niski', { size:24, bold:true, color:LVL[1].fg, bg:LVL[1].bg }), run('    ', { size:24 }), run('Poziom 2 · Średni', { size:24, bold:true, color:LVL[2].fg, bg:LVL[2].bg }), run('    ', { size:24 }), run('Poziom 3 · Wysoki', { size:24, bold:true, color:LVL[3].fg, bg:LVL[3].bg }) ], { align:AlignmentType.RIGHT, before:100, after:0 }),
  P([ run('Zasada: ', { size:24, bold:true, color:C.purple }), run('KPOF (przedszkole) nie posiada norm stenowych – kolumnę „Sten” pozostawia się pustą; interpretacja na podstawie punktów, średniej i poziomu wsparcia. KSzOF (szkoła) – steny wyłącznie w kolumnie „Sten” dla domen. Średniej nigdy nie opisuje się stenem.', { size:24, color:C.muted }) ], { before:80, after:0, line:250, align:AlignmentType.JUSTIFIED }) ];

// ---- 6 ----
const s6 = D.s6, CC = { red:C.red, blue:C.blue, purple:C.purple, orange:C.orange, green:C.green };
const part6 = [ empty(360), ...secL('6', s6.title, s6.law), lead2('', s6.lead),
  ...s6.cards.flatMap(([c, title, parts, rec]) => [
    tbl([CW], [ row([ cell([
      P([ run(title, { size:24, bold:true, color:C.purple }) ], { after:50 }),
      P(parts.map(pt => run(pt[0], { size:24, bold:!!pt[1], color: pt[1] ? CC[c] : C.ink })), { after: rec ? 50 : 0, line:255, align:AlignmentType.JUSTIFIED }),
      ...(rec ? [ P([ run('Zalecenie: ', { size:24, bold:true, color:C.orange }), run(rec, { size:24, color:C.purple }) ], { after:0 }) ] : [])
    ], { width:CW, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:32, color:CC[c] } }, margins:{ top:110, bottom:120, left:220, right:180 } }) ]) ]), empty(90) ]) ];

// ---- 7 Mój głos ----
const s7 = D.s7;
const cbGrid = (items) => tbl([half, half], (() => { const rows=[]; for (let i=0;i<items.length;i+=2) rows.push(row([0,1].map(j => { const it=items[i+j]; return cell(it ? P([ chk(it[1]), run(it[0], { size:24 }) ], { after:0 }) : empty(), { width:half, borders:noBorders, margins:{ top:15, bottom:15, left:0, right:100 } }); }))); return rows; })());
const moodCols = ['2E9D52','7EB800','DFA22E','E77309','BF382A'];
const part7 = [ empty(360), ...secL('7', s7.title, s7.law), lead2('', s7.lead),
  labelP('Sposób pozyskania głosu dziecka – zaznaczono'), cbGrid(s7.sposoby), empty(80),
  tbl([half, half], [ row([0,1].map(i => { const [c,t,v]=s7.pola[i]; return cell([ labelP(t), P([ run(v, { size:24, italic:true }) ], { after:0, line:250 }) ], { width:half, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:28, color:CC[c] } }, margins:{ top:60, bottom:100, left:200, right:160 } }); })), row([2,3].map(i => { const [c,t,v]=s7.pola[i]; return cell([ labelP(t), P([ run(v, { size:24, italic:true }) ], { after:0, line:250 }) ], { width:half, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:28, color:CC[c] } }, margins:{ top:60, bottom:100, left:200, right:160 } }); })) ]),
  empty(80), labelP('Co mi najbardziej pomaga – zaznaczono'), cbGrid(s7.pomaga), empty(60),
  labelP('Jak się dziś czuję – wskazanie dziecka'),
  P(s7.nastroj.flatMap((n,i) => [ run('   ', { size:24, bg:moodCols[i] }), run((i===s7.nastrojWybor ? ' ☑ ' : '  ')+n+'      ', { size:24, bold: i===s7.nastrojWybor, color: i===s7.nastrojWybor ? C.orange : C.muted }) ]), { after:120 }),
  box([ labelP('Preferowany sposób komunikacji dziecka i wskazówki do rozmowy'), P([ run(s7.komunikacja, { size:24 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.blue),
  P([ run('Podstawa. ', { size:24, bold:true, color:C.purple }), run(s7.podstawa, { size:24, color:C.muted }) ], { before:80, after:0 }) ];

// ---- 8 ----
const s8 = D.s8, W8 = [2000, 4300, 3606];
const part8 = [ empty(360), ...secL('8', s8.title, s8.law), lead2(s8.ref, s8.lead),
  tbl(W8, [ gridHead(['Rodzaj wsparcia','Zakres wdrożonych działań i metody','Efektywność i obserwowane zmiany'], W8, [C.purple, C.purple, C.green]),
    ...s8.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W8[0]), gcell(txt(r[1]), W8[1]), gcell(txt(r[2]), W8[2], { edge:C.green }) ])) ]),
  empty(140), parentBox('Wyniki z sekcji 4–8 są podstawą analizy (sekcja 9) i decyzji Zespołu o poziomie wsparcia (sekcja 10). Część III opisuje, jak placówka zorganizuje wsparcie w tym roku szkolnym.') ];

// ---- 9 ----
const s9 = D.s9, W6 = [1900, 3900, 4106];
const part9 = [ empty(360), ...secL('9', s9.title, s9.law), lead2('', s9.lead),
  tbl(W6, [ gridHead(['Domena ICF','Opis funkcjonowania i bariery','Cel na rok szkolny – co ma się zmienić'], W6, [C.purple, C.purple, C.orange]),
    ...s9.rows.map(r => row([ gcell([ txt(r[1], { bold:true, color:C.purple }), txt(r[0], { size:24, color:C.orange, bold:true }) ], W6[0]), gcell(txt(r[2]), W6[1]), gcell(bullets(r[3], '✓', C.green), W6[2]) ])) ]) ];

// ---- 10 ----
const s10 = D.s10, TW = Math.floor(CW/3);
const part10 = [ empty(360), ...secL('10', s10.title, s10.law), lead2('', s10.lead),
  sub9('A','Poziom wsparcia ustalony przez Zespół','',C.orange),
  tbl([TW,TW,TW], [ row(s10.poziomy.map(([k,t,d,on]) => cell([ P([ chk(on), run(t, { size:24, bold:true, color:C.purple }) ], { after:40 }), P([ run(d, { size:24, color:C.muted }) ], { after:0, line:240 }) ], { width:TW, bg: on ? C.orangeMist : C.white, borders:{ top:ln(on?C.orange:C.line), bottom:ln(on?C.orange:C.line), left:ln(on?C.orange:C.line), right:ln(on?C.orange:C.line) }, margins:{ top:80, bottom:80, left:160, right:140 } }))) ]),
  empty(60), box([ labelP('Uzasadnienie decyzji Zespołu'), P([ run(s10.uzasadnienie, { size:24 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.orange), empty(60),
  tbl([SWT,SWT,SWT,SWT], [ row(s10.wymiar.map(([k,v]) => cell([ P([ run(k.toUpperCase(), { size:24, bold:true, color:C.lavText, spacing:12 }) ], { after:30 }), P([ run(v, { size:24, bold:true, color:C.purple }) ], { after:0, line:240 }) ], { width:SWT, bg:C.lav, borders:{ top:ln(C.white,12), bottom:ln(C.white,12), left:ln(C.white,12), right:ln(C.white,12) }, margins:{ top:90, bottom:90, left:140, right:100 } }))) ]),
  sub9('B','Rekomendacje placówki dla zespołu orzekającego poradni','',C.blue),
  lead2('', s10.rekomendacje.lead),
  cbGrid(s10.rekomendacje.items), empty(40),
  box([ P([ run('Uzasadnienie rekomendacji. ', { size:24, bold:true, color:C.orange }), run(s10.rekomendacje.uzasadnienie, { size:24 }) ], { after:0, line:250, align:AlignmentType.JUSTIFIED }) ], C.blue, { bg:C.lav2 }),
  empty(60), P([ run('Data posiedzenia Zespołu: ', { size:24, bold:true, color:C.purple }), ph(s10.dataDecyzji), run('   ·   '+s10.zgodaRodzica+'   ·   ', { size:24, color:C.muted }), run('Podpisy Zespołu i rodzica: ', { size:24, bold:true, color:C.purple }), run('na końcu dokumentu (sekcja 16).', { size:24, color:C.muted }) ], { after:0, line:260 }) ];

// ---- 11 ----
const s11 = D.s11, W11 = [2400, CW-2400];
const kvTable = (rows, h1, h2) => tbl(W11, [ gridHead([h1,h2], W11), ...rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W11[0]), gcell(txt(r[1]), W11[1]) ])) ]);
const part11 = [ empty(480),
  ...bandW('III','Program wsparcia i organizacja','dostosowania · zintegrowane działania · zajęcia · dodatkowa osoba · rodzice i poradnia · ocena efektywności'),
  ...secL('11', s11.title, s11.law),
  P([ run('Dostosowania wynikają z analizy jakościowej (sekcja 9) i decyzji o poziomie wsparcia (sekcja 10). Dotyczą:  ', { size:24, color:C.muted }), chk(false), run('programu wychowania przedszkolnego    ', { size:24, bold:true, color:C.purple }), chk(false), run('podstawy programowej kształcenia ogólnego (szkoła)', { size:24, bold:true, color:C.purple }) ], { after:120, line:260 }),
  sub9('A', s11.A.title, '', C.orange), kvTable(s11.A.rows, 'Zakres', 'Sposób dostosowania'),
  empty(360),
  sub9('B', s11.B.title, '', C.blue), kvTable(s11.B.rows, 'Obszar organizacji', 'Sposób dostosowania'),
  sub9('C', s11.C.title, '', C.purple), kvTable(s11.C.rows, 'Obszar', 'Narzędzia i sposób wykorzystania') ];

// ---- 12 ----
const s12 = D.s12, W12 = [1800, 3000, 3000, 2106];
const part12 = [ empty(360), ...secL('12', s12.title, s12.law), lead2('', s12.lead),
  tbl(W12, [ gridHead(['Wspólny cel','Nauczyciel / wychowawca (codziennie w grupie)','Specjaliści (zajęcia)','Sposób koordynacji'], W12),
    ...s12.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W12[0]), gcell(txt(r[1]), W12[1]), gcell(txt(r[2]), W12[2]), gcell(txt(r[3]), W12[3]) ])) ]),
  empty(120), box([ P([ run('Koordynacja. ', { size:24, bold:true, color:C.orange }), run(s12.koordynacja, { size:24 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.orange, { bg:C.lav2 }) ];

// ---- 13 ----
const s13 = D.s13, WZ = [3000, 2800, 1500, 1300, 1306], WP = [2500, 1900, 1250, 1550, 1450, 1256], WM = [400, 3300, 3300, 1500, 1406];
const zajTable = (rows, edge, sumLabel, sumVal, sumSub) => tbl(WZ, [ gridHead(['Rodzaj zajęć','Zakres / cel','Prowadzący','Forma','Wymiar tyg.'], WZ),
  ...rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:24 }), WZ[0], { edge, pad:50 }), gcell(txt(r[1], { size:24 }), WZ[1], { pad:50 }), gcell(txt(r[2], { bold:true, color:C.purple, size:24 }), WZ[2], { pad:50 }), gcell(txt(r[3], { size:24 }), WZ[3], { pad:50 }), gcell([ txt(r[4], { bold:true, color:C.purple, size:24 }), txt(r[5], { size:24, color:C.muted }) ], WZ[4], { pad:50 }) ])),
  row([ cell(txt(sumLabel, { bold:true, color:C.purple, size:24 }), { width:WZ[0]+WZ[1]+WZ[2]+WZ[3], span:4, bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:80, left:140, right:120 } }), cell([ txt(sumVal, { bold:true, color:C.purple, size:24 }), txt(sumSub, { size:24, color:C.muted }) ], { width:WZ[4], bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:80, left:140, right:120 } }) ]) ]);
const pppTable = tbl(WP, [ gridHead(['Forma pomocy','Cel','Prowadzący','Forma i miejsce','Czas i termin','Okres udzielania'], WP),
  ...s13.ppp.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:24 }), WP[0], { edge:C.blue, pad:40 }), gcell(txt(r[1], { size:24 }), WP[1], { pad:40 }), gcell(txt(r[2], { bold:true, color:C.purple, size:24 }), WP[2], { pad:40 }), gcell(txt(r[3], { size:24 }), WP[3], { pad:40 }), gcell(txt(r[4], { bold:true, color:C.purple, size:24 }), WP[4], { pad:40 }), gcell(txt(r[5], { size:24 }), WP[5], { pad:40 }) ])),
  row([ cell(txt('Razem pomoc psychologiczno-pedagogiczna', { bold:true, color:C.purple, size:24 }), { width:CW-WP[5], span:5, bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:80, left:140, right:120 } }), cell([ txt(s13.sumPpp[0], { bold:true, color:C.purple, size:24 }), txt(s13.sumPpp[1], { size:24, color:C.muted }) ], { width:WP[5], bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:80, left:140, right:120 } }) ]) ]);
const statusCell = (w) => gcell(['wdrożone','w trakcie','planowane'].map(t => P([ run('☐ ', { size:24, color:'B6A6DF' }), run(t, { size:24, color:C.muted }) ], { after:0, line:220 })), w);
const part13 = [ empty(360), ...secL('13', s13.title, s13.law), lead2('', s13.lead),
  tbl([half, CW-half], [ row([ statTile('A · ZAJĘCIA REWALIDACYJNE · RAZEM', s13.sumRew[0], '= '+s13.sumRew[1]+' · '+s13.sumRew[2], half), statTile('B · POMOC PSYCHOLOGICZNO-PEDAGOGICZNA · RAZEM', s13.sumPpp[0], '= '+s13.sumPpp[1]+' · '+s13.sumPpp[2], CW-half, C.blue) ]) ]),
  sub9('A','Zajęcia rewalidacyjne przydzielone dziecku / uczniowi','kształcenie specjalne · na podstawie orzeczenia', C.orange), zajTable(s13.rew, C.orange, 'Razem zajęcia rewalidacyjne', s13.sumRew[0], s13.sumRew[1]),
  empty(360),
  sub9('B','Zajęcia z zakresu pomocy psychologiczno-pedagogicznej','forma · czas · termin · okres udzielania · miejsce', C.blue), pppTable,
  empty(360),
  P([ run('Uwaga: ', { size:24, bold:true, color:C.purple }), run(s13.uwaga, { size:24, color:C.muted }) ], { after:60 }),
  sub9('C','Zalecenia poradni i miejsce ich realizacji w programie','każde zalecenie wskazuje sekcję, w której jest realizowane', C.purple),
  P([ run('Orzeczenie / opinia nr ', { size:24, color:C.muted }), ph(D.meta.nrOrzeczenia), run(' z dnia ', { size:24, color:C.muted }), ph(D.meta.dataOrzeczenia), run('.', { size:24, color:C.muted }) ], { after:100 }),
  tbl(WM, [ gridHead(['Lp.','Zalecenie poradni (z orzeczenia / opinii)','Sposób realizacji w placówce','Gdzie w raporcie','Status'], WM, [C.purple, C.purple, C.orange, C.purple, C.purple]),
    ...s13.mapa.map((z,i) => row([ gcell(txt(String(i+1), { bold:true, color:C.orange, size:24 }), WM[0]), gcell(txt(z[0], { bold:true, size:24 }), WM[1]), gcell(txt(z[1], { size:24 }), WM[2]), gcell(P([ run(' '+z[2]+' ', { size:24, bold:true, color:C.orange, bg:C.orangeMist }) ], { after:0 }), WM[3]), statusCell(WM[4]) ])) ]) ];

// ---- 14 ----
const s14 = D.s14;
const part14 = [ empty(360), ...secL('14', s14.title, s14.law),
  P(s14.rodzaj.flatMap(([t,on]) => [ chk(on), run(t+'      ', { size:24, bold:true, color:C.purple }) ]), { after:120 }),
  tbl([Math.floor(CW/3), CW-Math.floor(CW/3)], [ row([ cell([ P([ run('WYMIAR I SYTUACJE', { size:24, bold:true, color:C.lavText, spacing:12 }) ], { after:30 }), P([ run(s14.wymiar, { size:24, bold:true, color:C.purple }) ], { after:0, line:240 }) ], { width:Math.floor(CW/3), bg:C.lav, borders:noBorders, margins:{ top:90, bottom:90, left:140, right:100 } }), cell([ P([ run('PODSTAWA PRAWNA I FORMALNA', { size:24, bold:true, color:C.lavText, spacing:12 }) ], { after:30 }), P([ run(s14.podstawa, { size:24, color:C.purple }) ], { after:0, line:240 }) ], { width:CW-Math.floor(CW/3), bg:C.lav, borders:{ top:NOB, bottom:NOB, right:NOB, left:ln(C.white,12) }, margins:{ top:90, bottom:90, left:140, right:100 } }) ]) ]),
  empty(120), box([ labelP('Uzasadnienie wynikające z oceny funkcjonalnej'), P([ run(s14.uzasadnienie, { size:24 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.orange), empty(100),
  box([ labelP('Zadania dodatkowej osoby'), ...bullets(s14.zadania, '✓', C.green) ], C.green), empty(100),
  box([ P([ run('Ocena zasadności. ', { size:24, bold:true, color:C.orange }), run(s14.ocena, { size:24 }) ], { after:0, line:260, align:AlignmentType.JUSTIFIED }) ], C.orange, { bg:C.lav2 }),
  P([ run('Wariant B: ', { size:24, bold:true, color:C.purple }), run(s14.wariantNote, { size:24, color:C.muted }) ], { before:80, after:0 }) ];

// ---- 15 ----
const s15 = D.s15, W15 = [2200, 3700, 2000, 2006];
const part15 = [ empty(360), ...secL('15', s15.title, s15.law),
  sub9('A', s15.A.title, '', C.orange), simpleTable(['Forma współpracy','Zakres','Odpowiedzialny','Częstotliwość'], W15, s15.A.rows, { purpleCols:[2], boldCols:[2], pad:50 }),
  sub9('B', s15.B.title, '', C.green), box([ ...bullets(s15.B.items, '✓', C.green) ], C.green),
  sub9('C', s15.C.title, '', C.purple), simpleTable(['Działanie','Zakres / cel','Kto','Termin'], W15, s15.C.rows, { purpleCols:[2], boldCols:[2], pad:50 }) ];

// ---- 16 + podpisy ----
const s16 = D.s16, W16 = [1600, 3500, 2300, 1400, 1106], STC = { 'wykonano':LVL[1], 'w trakcie':LVL[2], 'planowane':{ bg:C.lav, fg:C.purple } };
const part16 = [ empty(360), ...secL('16', s16.title, s16.law), lead2('', s16.lead),
  tbl(W16, [ gridHead(['Termin','Zakres oceny','Narzędzia','Odpowiedzialny','Status'], W16),
    ...s16.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:24 }), W16[0]), gcell(txt(r[1], { size:24 }), W16[1]), gcell(txt(r[2], { size:24 }), W16[2]), gcell(txt(r[3], { size:24 }), W16[3]), gcell(P([ run(' '+r[4]+' ', { size:24, bold:true, color:STC[r[4]].fg, bg:STC[r[4]].bg }) ], { after:0 }), W16[4]) ])) ]),
  empty(140), parentBox('Niniejszy raport stanowi opinię placówki o funkcjonowaniu dziecka i jest przekazywany rodzicowi oraz zespołowi orzekającemu poradni. Wyniki obserwacji służą zaplanowaniu wsparcia, a nie ocenie dziecka. Zachęcamy do rozmowy z Zespołem o każdej części dokumentu.'),
  empty(60), sigs ];

const part2 = [ ...part4, ...part5, ...part6, ...part7, ...part8, ...part9, ...part10, ...part11, ...part12, ...part13, ...part14, ...part15, ...part16 ];

const PR = D.prawo, WV = D.warianty, WL = [3300, 1300, 5306], WW = [900, 4200, 2300, 2506];
const okTxt = (v) => txt(v, { size:24, bold: v.startsWith('✓')||v.startsWith('—'), color: v.startsWith('✓') ? C.green : (v.startsWith('—') ? C.red : C.ink) });
const lawPage = [
  ...pageHeader('Ocena Funkcjonalna · Zawartość raportu · jak czytać · dwa warianty'),
  section('≡', 'Zawartość raportu'),
  ...(() => {
    const T = JSON.parse(require('fs').readFileSync(require('path').join(__dirname,'raport_data.json'),'utf8')).toc;
    const out = [];
    const head = (t) => P([ run('■ ', { size:24, color:C.purple }), run(t.toUpperCase(), { size:24, bold:true, color:C.purple, spacing:14 }) ], { after:70 });
    out.push(head(T.I.title));
    out.push(tbl([3302,3302,3302], [ row(T.I.items.map(t => cell([ P([ run(t[0], { size:28, bold:true, color:C.orange }) ], { after:20 }), P([ run(t[1], { size:24, bold:true, color:C.purple }) ], { after:30 }), P([ run(t[2], { size:24, color:C.muted }) ], { after:0, line:230 }) ], { width:3302, borders:{ top:{ style:BorderStyle.SINGLE, size:28, color:C.orange }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:90, left:160, right:160 } }))) ]));
    for (const part of ['II','III']) {
      out.push(empty(80)); out.push(head(T[part].title));
      const n = T[part].items.length, w = Math.floor(CW/n), ws = T[part].items.map((_,i) => i===n-1 ? CW-w*(n-1) : w);
      out.push(tbl(ws, [ row(T[part].items.map((t,i) => cell([ P([ run(t[0], { size:24, bold:true, color:C.orange }) ], { after:10 }), P([ run(t[1], { size:24, bold:true, color:C.purple }) ], { after:0, line:210 }) ], { width:ws[i], borders:{ top:{ style:BorderStyle.SINGLE, size:28, color:C.orange }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:60, bottom:70, left:90, right:60 } }))) ]));
    }
    return out;
  })(),
  section('?', 'Jak czytać ten raport'),
  lead2('', 'Pięć kroków od obserwacji do oceny efektów. Część I–II to opinia placówki, którą otrzymuje rodzic i zespół orzekający poradni. Część III to organizacja wsparcia w placówce – co, kto, kiedy i ile.'),
  tbl([1981,1981,1981,1981,1982], [ row(PR.jakczytac.map((k,i) => cell([ P([ run('CZĘŚĆ '+k[0], { size:24, bold:true, color:C.orange, spacing:12 }) ], { after:20 }), P([ run(k[1], { size:24, bold:true, color:C.purple }) ], { after:30 }), P([ run(k[2], { size:24, color:C.muted }) ], { after:0, line:220 }) ], { width: i===4?1982:1981, margins:{ top:80, bottom:80, left:120, right:100 } }))) ]),
  section('A/B', WV.title), lead2('', WV.lead),
  tbl([half, CW-half], [ row([
    cell(P([ run(' A ', { size:24, bold:true, color:C.white, bg:C.orange }), run('  '+WV.A, { size:24 }) ], { after:0, line:250 }), { width:half, margins:{ top:100, bottom:100, left:160, right:140 } }),
    cell(P([ run(' B ', { size:24, bold:true, color:C.white, bg:C.blue }), run('  '+WV.B, { size:24 }) ], { after:0, line:250 }), { width:CW-half, margins:{ top:100, bottom:100, left:160, right:140 } })
  ]) ]),
  empty(100),
  tbl(WW, [ gridHead(['Sekcje','Zakres','Wariant A · z orzeczeniem','Wariant B · bez orzeczenia'], WW),
    ...WV.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.orange, size:24 }), WW[0], { pad:45 }), gcell(txt(r[1], { size:24 }), WW[1], { pad:45 }), gcell(okTxt(r[2]), WW[2], { pad:45 }), gcell(okTxt(r[3]), WW[3], { pad:45 }) ])) ]),
  empty(360),
  section('§', PR.title), lead2('', PR.lead),
  tbl(WL, [ gridHead(['Akt prawny','Publikacja','Zakres zastosowania w raporcie'], WL),
    ...PR.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:24 }), WL[0], { pad:50 }), gcell(txt(r[1], { bold:true, color:C.orange, size:24 }), WL[1], { pad:50 }), gcell(P([ run(r[2]+'  ', { size:24 }), run(' '+r[3]+' ', { size:24, bold:true, color:C.orange, bg:C.orangeMist }) ], { after:0, line:230 }), WL[2], { pad:50 }) ])) ]),
  empty(120), parentBox('Numery paragrafów wskazują, z jakiego przepisu wynika każda część raportu. Przy każdej sekcji 4–16 znajduje się plakietka „§ Podstawa prawna”.'),
  empty(360)
];


// =============== ZAŁĄCZNIK · OPINIA dla zespołu orzekającego ===============
const OP = D.opinia, PL = D.placowka;
const opHead = () => [ tbl([half, CW-half], [ row([
    cell([ P([ run(PL.nazwa, { size:24, bold:true, color:C.purple }) ], { after:20 }), P([ run(PL.adres, { size:24, color:C.muted }) ], { after:20 }), P([ run('(pieczęć placówki)', { size:24, color:C.muted }) ], { after:0 }) ], { width:half, borders:{ top:{ style:BorderStyle.DASHED, size:24, color:C.line }, bottom:{ style:BorderStyle.DASHED, size:24, color:C.line }, left:{ style:BorderStyle.DASHED, size:24, color:C.line }, right:{ style:BorderStyle.DASHED, size:24, color:C.line } }, margins:{ top:120, bottom:120, left:180, right:180 } }),
    cell([ P([ run(PL.miejscowosc+', dnia ………………………', { size:24, color:C.muted }) ], { align:AlignmentType.RIGHT, after:40 }), P([ run('Znak sprawy: ………………………', { size:24, color:C.muted }) ], { align:AlignmentType.RIGHT, after:40 }), P([ run('Zespół orzekający: [Nazwa Poradni Psychologiczno-Pedagogicznej]', { size:24, color:C.muted }) ], { align:AlignmentType.RIGHT, after:0 }) ], { width:CW-half, borders:noBorders, margins:{ top:60, bottom:60, left:200, right:0 } })
  ]) ]), empty(160) ];
const opSec = (n, t) => new Paragraph({ spacing:{ before:180, after:100 }, keepNext:true, border:{ bottom:{ style:BorderStyle.SINGLE, size:24, color:C.line, space:4 } }, children:[ run(n+'  ', { size:24, bold:true, color:C.orange }), run(t.toUpperCase(), { size:24, bold:true, color:C.purple, spacing:8 }) ] });
const opKV = (rows) => tbl([3000, CW-3000], rows.map(([k,v]) => row([ gcell(txt(k, { bold:true, color:C.purple, size:24 }), 3000, { bg:C.lav2, pad:55 }), gcell(txt(v.replace(/☐/g,'☐'), { size:24 }), CW-3000, { pad:55 }) ])));
const WO = [2100, 3000, 3000, 1806];
const opICF = (rows) => tbl(WO, [ gridHead(['Obszar (ICF)','Mocne strony i uzdolnienia','Trudności','Poziom potrzeby wsparcia'], WO, [C.purple, C.green, C.red, C.purple]),
  ...rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:24 }), WO[0], { bg:C.lav2, pad:45 }), gcell(txt(r[1], { size:24 }), WO[1], { pad:45 }), gcell(txt(r[2], { size:24 }), WO[2], { pad:45 }), gcell(txt(r[3], { bold:true, color:C.purple, size:24 }), WO[3], { pad:45 }) ])) ]);
const opBul = (items, color=C.orange) => items.map(x => new Paragraph({ spacing:{ before:0, after:40, line:245 }, indent:{ left:220, hanging:220 }, children:[ run('•  ', { size:24, color, bold:true }), run(x, { size:24 }) ] }));
const WI = [2100, 3600, 1600, 2606];
const opinionPages = [
  pb(), ...opHead(),
  P([ run(OP.title, { size:40, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:40, line:480, lineRule:'exact' }),
  P([ run(OP.sub.toUpperCase(), { size:24, bold:true, color:C.orange, spacing:30 }) ], { align:AlignmentType.CENTER, after:140 }),
  tbl([CW], [ row([ cell([ P([ run('Podstawa prawna: ', { size:24, bold:true, color:C.purple }), run(OP.podstawa, { size:24, color:C.muted }) ], { after:40, line:240, align:AlignmentType.JUSTIFIED }), P([ run('Tryb: ', { size:24, bold:true, color:C.purple }), run(OP.procedura, { size:24, color:C.muted }) ], { after:0, line:240, align:AlignmentType.JUSTIFIED }) ], { width:CW, margins:{ top:100, bottom:100, left:180, right:180 } }) ]) ]),
  opSec('1.', 'Data wydania opinii i dane dziecka / ucznia (§ 7 ust. 6 pkt 1–2)'), opKV(OP.dane),
  opSec('2.', OP.podstawaOpinii.title), opKV(OP.podstawaOpinii.rows),
  empty(360),
  opSec('3.', OP.II.title), lead2('', OP.II.lead),
  sub9('A', OP.II.titleA, '', C.orange), opICF(OP.II.rows),
  empty(360),
  opSec('3.', OP.II.title+' · cd.'),
  sub9('B', OP.II.titleB, '', C.blue), opICF(OP.II.rowsSzkola),
  P([ run(OP.II.wynik, { size:24, bold:true, color:C.purple }) ], { before:80, after:0 }),
  opSec('4.', OP.III.title), ...opBul(OP.III.items),
  empty(360),
  opSec('5.', OP.zal.title), ...OP.zal.items.map(([t,on]) => P([ chk(on), run(t, { size:24 }) ], { after:40 })),
  opSec('6.', OP.IV.title),
  tbl(WI, [ gridHead(['Działanie / forma pomocy','Zakres i wymiar','Okres udzielania','Efekty'], WI), ...OP.IV.rows.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple, size:24 }), WI[0], { bg:C.lav2, pad:50 }), gcell(txt(r[1], { size:24 }), WI[1], { pad:50 }), gcell(txt(r[2], { size:24 }), WI[2], { pad:50 }), gcell(txt(r[3], { size:24 }), WI[3], { pad:50 }) ])) ]),
  opSec('7.', OP.VI.title), ...opBul(OP.VI.dalsza, C.green),
  empty(360),
  opSec('8.', OP.uzup.title), lead2('', OP.uzup.lead),
  P([ run(OP.uzup.funkcje, { size:24 }) ], { after:100, line:240, align:AlignmentType.JUSTIFIED }),
  tbl([half, CW-half], [ gridHead(['Ułatwienia w środowisku placówki (co pomaga)','Bariery (co utrudnia)'], [half, CW-half], [C.green, C.red]), row([ gcell(opBul(OP.uzup.ulatwienia, C.green), half, { pad:60 }), gcell(opBul(OP.uzup.bariery, C.red), CW-half, { pad:60 }) ]) ]),
  P([ run('Informacje od dziecka i rodziców (§ 8 ust. 3 pkt 1 i 3): ', { size:24, bold:true, color:C.purple }), run(OP.uzup.glos, { size:24 }) ], { before:80, after:60, line:240, align:AlignmentType.JUSTIFIED }),
  sub9('!', OP.uzup.rekTitle, '', C.blue), cbGrid(OP.VI.items.map(([t,on]) => [t,on])),
  P([ run('Uzasadnienie: ', { size:24, bold:true, color:C.purple }), run(OP.VI.uzasadnienie, { size:24 }) ], { before:40, after:0, line:240, align:AlignmentType.JUSTIFIED }),
  opSec('9.', OP.podpisy.osoby),
  tbl([half, CW-half], (() => { const rows=[]; for (let i=0;i<OP.sporzadzili.length;i+=2) rows.push(row([0,1].map(j => { const it=OP.sporzadzili[i+j]; return cell(it ? [ P([ run(it[0]+': ', { size:24, bold:true, color:C.purple }), run(it[1], { size:24 }) ], { after:10 }), P([ run('podpis: ………………………………………', { size:24, color:C.muted }) ], { after:0 }) ] : [empty()], { width:half, borders:noBorders, margins:{ top:40, bottom:40, left:0, right:200 } }); }))); return rows; })()),
  tbl([Math.floor(CW/2), CW-Math.floor(CW/2)], [ row([ sigCell(OP.podpisy.dyrektor+' · podpis i pieczęć · data', Math.floor(CW/2), undefined, 360), cell([ P([ run(OP.podpisy.kopia, { size:24, color:C.muted }) ], { after:0, line:240 }) ], { width:CW-Math.floor(CW/2), borders:noBorders, vAlign:VerticalAlign.BOTTOM, margins:{ top:360, bottom:20, left:220, right:120 } }) ]) ]),
  P([ run(OP.zalaczniki+' Opinia zawiera dane dotyczące zdrowia (art. 9 RODO) – dokument poufny.', { size:24, color:C.muted }) ], { before:100, after:0, line:240, border:{ top:{ style:BorderStyle.DASHED, size:24, color:C.line, space:6 } } })
];
const runHeader = (left, right) => new Header({ children:[ new Paragraph({ spacing:{ before:0, after:0 }, border:{ bottom:{ style:BorderStyle.SINGLE, size:4, color:C.line, space:4 } }, tabStops:[{ type:TabStopType.RIGHT, position:CW }], children:[ run(left, { size:16, color:C.lavText }), run('\t'), run(right, { size:16, color:C.lavText }) ] }) ] });
const opinionFooter = new Paragraph({
  spacing:{ before:60, after:0 }, border:{ top:{ style:BorderStyle.SINGLE, size:24, color:C.line2, space:4 } },
  tabStops:[{ type:TabStopType.RIGHT, position:CW }],
  children:[ run('Załącznik – opinia o funkcjonowaniu dziecka / ucznia · dokument poufny (RODO)', { size:24, color:C.muted }), run('\t'), run('Strona ', { size:24, color:C.muted }), new TextRun({ children:[PageNumber.CURRENT], font:FONT, size:24, bold:true, color:C.orange }), run(' z ', { size:24, color:C.muted }), new TextRun({ children:[PageNumber.TOTAL_PAGES], font:FONT, size:24, bold:true, color:C.purple }) ]
});

const children = [
  ...cover,
  ...lawPage,
  section('1','Metryczka bazowa'),
  meta,
  section('2','Podstawa i procedura obserwacji wstępnej'),
  flow,
  empty(100),
  box([ P([ run('Z uwagi na zgłaszane trudności w funkcjonowaniu, wniosek rodzica oraz posiadaną dokumentację (w tym opinię/orzeczenie poradni), w placówce przeprowadzono ', { size:24 }), run('we wrześniu', { size:24, bold:true, color:C.orange }), run(' obserwację poziomu funkcjonowania z wykorzystaniem ', { size:24 }), run('Kwestionariusza Przedszkolnej Oceny Funkcjonalnej (KPOF) – przedszkole – lub Kwestionariusza Szkolnej Oceny Funkcjonalnej (KSzOF) – szkoła', { size:24, bold:true, color:C.orange }), run(', analizującego funkcjonowanie w obszarach zgodnych z Międzynarodową Klasyfikacją Funkcjonowania, Niepełnosprawności i Zdrowia (ICF).', { size:24 }) ], { align:AlignmentType.JUSTIFIED, after:0, line:290 }) ], C.orange, { bg:C.lav2 }),
  empty(120),
  icfRow,
  empty(360),
  section('3','Wskazania do obserwacji pogłębionej i zastosowane narzędzia'),
  P([ run('W związku ze zidentyfikowanymi w toku oceny wstępnej trudnościami w funkcjonowaniu – w szczególności w zakresie ', { size:24 }), run('trudnych zachowań', { size:24, bold:true, color:C.purple }), run(', ', { size:24 }), run('rozwoju funkcji poznawczych', { size:24, bold:true, color:C.purple }), run(', ', { size:24 }), run('przetwarzania bodźców', { size:24, bold:true, color:C.purple }), run(' oraz ', { size:24 }), run('komunikacji', { size:24, bold:true, color:C.purple }), run(' – przeprowadzono obserwację pogłębioną z wykorzystaniem następujących narzędzi specjalistycznych:', { size:24 }) ], { after:180, line:290, align:AlignmentType.JUSTIFIED }),
  ...tools,
  ...part2
];

const ONLY_OPINIA = process.argv.includes('--opinia');
const opinionSection = {
  properties:{ page:{ size:A4, margin:MARGINS }, type: ONLY_OPINIA ? undefined : 'nextPage' },
  headers:{ default: runHeader('Opinia o funkcjonowaniu dziecka / ucznia – załącznik', '[Imię i nazwisko dziecka / ucznia]') },
  footers:{ default: new Footer({ children:[ opinionFooter ] }) },
  children: ONLY_OPINIA ? opinionPages.slice(1) : opinionPages.slice(1)
};
const doc = new Document({
  creator: 'EduPlaner2026-MJ-PCTP', title: ONLY_OPINIA ? 'Opinia o funkcjonowaniu dziecka / ucznia' : 'Ocena Funkcjonalna – podsumowanie WOPF i IPET', description: 'Opinia przedszkola/szkoły dla zespołu orzekającego i rodzica (obszary ICF)',
  styles:{ default:{ document:{ run:{ font:FONT, size:24, color:C.ink } } } },
  sections: ONLY_OPINIA ? [ opinionSection ] : [ {
    properties:{ page:{ size:A4, margin:MARGINS } },
    headers:{ default: runHeader('[Nazwa placówki] · Ocena Funkcjonalna – WOPF i IPET', 'Dziecko: ………………………  Grupa: ………') },
    footers:{ default: new Footer({ children:[ footerPara ] }) },
    children
  }, opinionSection ]
});
const outName = process.argv.find(a => a.endsWith('.docx')) || (ONLY_OPINIA ? 'Opinia_dla_poradni.docx' : 'Raport_Oceny_Funkcjonalnej.docx');
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(outName, buf); console.log('OK', outName, buf.length); });
