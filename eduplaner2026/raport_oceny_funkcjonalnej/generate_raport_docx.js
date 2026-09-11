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
  P([ run('  OPINIA PRZEDSZKOLA / SZKOŁY · DLA ZESPOŁU ORZEKAJĄCEGO · DLA RODZICA  ', { size:14, bold:true, color:C.white, bg:C.orange, spacing:12 }) ], { align:AlignmentType.CENTER, before:120, after:200 }),
  P([ run('OCENA FUNKCJONALNA · ICF · PRZEDSZKOLE · SZKOŁA', { size:15, color:C.purple, spacing:50 }) ], { align:AlignmentType.CENTER, after:120 }),
  P([ run('Raport Oceny', { size:56, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:0, line:640, lineRule:'exact' }),
  P([ run('Funkcjonalnej', { size:56, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:140, line:640, lineRule:'exact' }),
  P([ run('OBSERWACJA WSTĘPNA I POGŁĘBIONA · OBSZARY ICF', { size:15, bold:true, color:C.orange, spacing:44 }) ], { align:AlignmentType.CENTER, after:260 }),
  P([ run('z dnia  ', { size:20, color:C.muted }), run('………………………………………………', { size:20, color:'B6A6DF' }) ], { align:AlignmentType.CENTER, after:300 }),

  // zespół
  box([
    label('Opracowany przez Zespół w składzie'),
    tbl([Math.floor((CW-480)/2), Math.floor((CW-480)/2)], [0,1,2].map(r => row([0,1].map(c => {
      const n = r*2+c+1, w = Math.floor((CW-480)/2);
      return cell(P([ run(n+'.', { bold:true, color:C.orange, size:20 }), run('  ' + '.'.repeat(58), { size:16, color:'B6A6DF' }) ], { after:0 }), { width:w, borders:noBorders, margins:{ top:70, bottom:70, left:0, right:200 } });
    }))))
  ], C.orange),
  empty(180),

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
  empty(220),

  // zawartość raportu
  P([ run('■ ', { size:14, color:C.purple }), run('ZAWARTOŚĆ RAPORTU', { size:13, bold:true, color:C.purple, spacing:14 }) ], { after:100 }),
  tbl([3302,3302,3302], [ row([
    ['1','Metryczka bazowa','dane dziecka, wariant wsparcia, podstawa formalna, zdrowie i farmakoterapia'],
    ['2','Obserwacja wstępna','procedura wrześniowej obserwacji Kwestionariuszem Oceny Funkcjonalnej w obszarach ICF'],
    ['3','Obserwacja pogłębiona','wskazania i narzędzia: ABC, Profil Biopsychospołeczny, Profil Sensoryczny, mowa i AAC, ToM']
  ].map(t => cell([
    P([ run(t[0], { size:32, bold:true, color:C.orange }) ], { after:40 }),
    P([ run(t[1], { size:19, bold:true, color:C.purple }) ], { after:50 }),
    P([ run(t[2], { size:15, color:C.muted }) ], { after:0, line:250 })
  ], { width:3302, borders:{ top:{ style:BorderStyle.SINGLE, size:24, color:C.orange }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:140, bottom:150, left:180, right:180 } })) ) ]),
  empty(200),
  P(['ICF','KSzOF','ABC','Profil Sensoryczny','AAC','ToM'].flatMap((t,i)=>[ run('  '+t+'  ', { size:14, bold:true, color:[C.purple,C.orange,C.purple,C.purple,C.purple,C.orange][i], bg:[C.lav,C.orangeMist,C.white,C.lav,C.white,C.orangeMist][i] }), run('   ', { size:14 }) ]), { align:AlignmentType.CENTER, after:0 }),
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

const sigCell = (role, width, span) => new TableCell({
  width:{ size:width, type:WidthType.DXA }, columnSpan: span,
  margins:{ top:560, bottom:40, left:220, right:220 }, borders:noBorders,
  children:[
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{ before:0, after:0 }, border:{ top:{ style:BorderStyle.SINGLE, size:6, color:C.purple, space:5 } }, children:[ run(role, { size:16, bold:true, color:C.purple }) ] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{ before:10, after:0 }, children:[ run('podpis i data', { size:12, color:C.muted }) ] })
  ]
});
const SGW = Math.floor(CW/3);
const sigs = tbl([SGW,SGW,SGW], [
  row([ sigCell('Koordynator Zespołu',SGW), sigCell('Dyrektor placówki',SGW), sigCell('Specjalista',SGW) ]),
  row([ sigCell('Rodzic / opiekun prawny – zapoznałam/em się z raportem', SGW*3, 3) ])
]);

// =============== STOPKA ===============
const footerPara = new Paragraph({
  spacing:{ before:60, after:0 }, border:{ top:{ style:BorderStyle.SINGLE, size:4, color:C.line2, space:4 } },
  tabStops:[{ type:TabStopType.RIGHT, position:CW }],
  children:[ run('EduPlaner 2026 · PCTP', { size:12, color:C.muted }), run('   ·   RODO · Dokument poufny', { size:12, color:C.muted }), run('\t'), run('Strona ', { size:12, color:C.muted }), new TextRun({ children:[PageNumber.CURRENT], font:FONT, size:12, bold:true, color:C.orange }), run(' z ', { size:12, color:C.muted }), new TextRun({ children:[PageNumber.TOTAL_PAGES], font:FONT, size:12, bold:true, color:C.purple }), run(' · Raport Oceny Funkcjonalnej', { size:12, color:C.muted }) ]
});

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
  empty(120),
  tbl([CW], [ row([ cell(P([ run('Informacja dla rodzica. ', { size:17, bold:true, color:C.orange }), run('Niniejszy raport stanowi opinię placówki o funkcjonowaniu dziecka i jest przekazywany rodzicowi oraz zespołowi orzekającemu poradni. Wyniki obserwacji służą zaplanowaniu wsparcia, a nie ocenie dziecka. Zachęcamy do rozmowy z Zespołem o każdej części dokumentu.', { size:17 }) ], { after:0, line:270 }), { width:CW, bg:C.paper, borders:{ top:ln(C.line2), bottom:ln(C.line2), left:ln(C.line2), right:ln(C.line2) }, margins:{ top:120, bottom:120, left:220, right:220 } }) ]) ]),
  empty(60),
  sigs
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
