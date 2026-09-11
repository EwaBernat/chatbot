const fs = require('fs');
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, LevelFormat, HeadingLevel, BorderStyle, WidthType,
  ShadingType, PageBreak, TabStopType, Header, Footer, PageNumber, VerticalAlign
} = require('docx');

const FONT = 'Arial';
const COLOR = { purple:'2D1B69', orange:'E8450A', green:'0D7D5C', red:'B8350D', amber:'C47A10', teal:'2B6E6E',
  muted:'6B6378', rule:'D8D2C5', paper:'FBF9F4', ink:'1A1530', purpleMist:'F3F1FB', orangeMist:'FEF0E8', tealMist:'E4F0F0', greenMist:'E6F4EF' };
const A4 = { width: 11906, height: 16838 };
const MARGINS = { top: 1440, right: 1080, bottom: 1440, left: 1080 };
const CW = 9746;

const run = (text, o={}) => new TextRun({ text, font: FONT, size: o.size||20, bold: !!o.bold, italics: !!o.italic, color: o.color||COLOR.ink, allCaps: !!o.caps, characterSpacing: o.spacing });
const para = (text, o={}) => new Paragraph({ spacing:{ before:o.before||0, after:o.after??120, line:o.line||280, lineRule:o.lineRule }, alignment:o.align||AlignmentType.LEFT, keepNext:o.keepNext, children:[ run(text, o) ] });
const runs = (children, o={}) => new Paragraph({ spacing:{ before:o.before||0, after:o.after??120, line:o.line||280 }, alignment:o.align||AlignmentType.LEFT, children });
const empty = (after=0) => new Paragraph({ spacing:{before:0, after}, children:[] });
const NOB = { style: BorderStyle.NIL };
const noBorders = { top:NOB, bottom:NOB, left:NOB, right:NOB };
const thin = { style: BorderStyle.SINGLE, size: 4, color: COLOR.rule };
const thinBorders = { top:thin, bottom:thin, left:thin, right:thin };

const cell = (children, o={}) => new TableCell({
  width:{ size:o.width, type:WidthType.DXA },
  shading: o.bg ? { fill:o.bg, type:ShadingType.CLEAR, color:'auto' } : undefined,
  margins: o.margins || { top:120, bottom:120, left:160, right:160 },
  borders: o.borders || thinBorders,
  verticalAlign: o.vAlign || VerticalAlign.TOP,
  columnSpan: o.span,
  children: Array.isArray(children) ? children : [children]
});
const tcell = (text, o={}) => cell(new Paragraph({ spacing:{before:0,after:0,line:260}, alignment:o.align||AlignmentType.LEFT, children:[run(text,{size:o.size||18, bold:o.bold, italic:o.italic, color:o.color, caps:o.caps})] }), o);

// ---- nagłówek sekcji: "1  Metryczka bazowa" z linią purpurową ----
const section = (n, title) => new Paragraph({
  spacing:{ before:360, after:200 }, keepNext:true,
  border:{ bottom:{ style:BorderStyle.SINGLE, size:12, color:COLOR.purple, space:4 } },
  children:[ run(n+'  ', {size:36, bold:true, color:COLOR.orange}), run(title, {size:28, bold:true, color:COLOR.purple}) ]
});

// ---- pudełko: tło purpurowe + lewa krawędź pomarańczowa ----
const boxPara = (children, o={}) => new Paragraph({
  spacing:{ before:o.before||0, after:o.after??0, line:300 },
  shading:{ fill:o.bg||COLOR.purpleMist, type:ShadingType.CLEAR, color:'auto' },
  border:{ left:{ style:BorderStyle.SINGLE, size:24, color:o.edge||COLOR.orange, space:10 } },
  indent:{ left:60, right:60 },
  children
});

const ph = (t) => run(t, { italic:true, color:COLOR.muted, size:18 });
const checkbox = (labelRuns) => new Paragraph({ spacing:{before:40,after:40,line:260}, children:[ run('☐  ', {size:22, color:COLOR.purple}), ...labelRuns ] });

// =============== OKŁADKA ===============
const cover = [
  // logo + marka
  new Table({ width:{size:CW,type:WidthType.DXA}, columnWidths:[900, CW-900], rows:[ new TableRow({ children:[
    cell(new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:0}, children:[run('E',{size:40,bold:true,color:'FFFFFF'})] }), { width:900, bg:COLOR.purple, borders:noBorders, vAlign:VerticalAlign.CENTER, margins:{top:160,bottom:160,left:100,right:100} }),
    cell([
      new Paragraph({ spacing:{before:0,after:20}, children:[run('EduPlaner 2026',{size:30,bold:true,color:COLOR.purple})] }),
      new Paragraph({ spacing:{before:0,after:0}, children:[run('PCTP KOSZALIN  ·  EDUPLANER2026-MJ-PCTP',{size:14,color:COLOR.muted})] })
    ], { width:CW-900, borders:noBorders, vAlign:VerticalAlign.CENTER, margins:{top:0,bottom:0,left:200,right:0} })
  ]}) ]}),
  empty(360),
  new Paragraph({ spacing:{before:0,after:240}, border:{ left:{ style:BorderStyle.SINGLE, size:24, color:COLOR.orange, space:10 } }, children:[ run('DOKUMENT DLA RODZICA I ZESPOŁU ORZEKAJĄCEGO', {size:16, bold:true, color:COLOR.orange, spacing:20}) ] }),
  para('Raport Oceny', { size:64, bold:true, color:COLOR.purple, after:0, line:760, lineRule:'exact' }),
  para('Funkcjonalnej', { size:64, bold:true, color:COLOR.purple, after:160, line:760, lineRule:'exact' }),
  para('opinia przedszkola / szkoły o funkcjonowaniu dziecka w obszarach ICF', { size:24, color:COLOR.ink, after:360 }),
  runs([ run('z dnia  ', {color:COLOR.muted}), run('………………………………………………', {color:COLOR.muted}) ], { after:420 }),

  // zespół
  new Table({ width:{size:CW,type:WidthType.DXA}, columnWidths:[CW], rows:[ new TableRow({ children:[ cell([
    new Paragraph({ spacing:{before:0,after:140}, children:[run('Opracowany przez Zespół w składzie', {size:24,bold:true,color:COLOR.purple})] }),
    new Table({ width:{size:CW-500,type:WidthType.DXA}, columnWidths:[(CW-500)/2,(CW-500)/2], rows:[0,1,2].map(r => new TableRow({ children:[0,1].map(c => {
      const n = r*2+c+1;
      return cell(new Paragraph({ spacing:{before:60,after:60}, tabStops:[{type:TabStopType.RIGHT, position:(CW-500)/2-300, leader:'dot'}], children:[ run(n+'.  ', {bold:true,color:COLOR.orange,size:20}), run('\t', {color:COLOR.muted}) ] }), { width:(CW-500)/2, borders:noBorders, bg:COLOR.purpleMist, margins:{top:40,bottom:40,left:80,right:80} });
    }) })) })
  ], { width:CW, bg:COLOR.purpleMist, borders:{ ...noBorders, left:{ style:BorderStyle.SINGLE, size:36, color:COLOR.orange } }, margins:{top:240,bottom:240,left:300,right:240} }) ]}) ]}),
  empty(320),

  // podstawa prawna
  new Table({ width:{size:CW,type:WidthType.DXA}, columnWidths:[800, CW-800], rows:[ new TableRow({ children:[
    cell(new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:0}, children:[run('§',{size:44,bold:true,color:COLOR.orange})] }), { width:800, bg:COLOR.paper, borders:{ top:thin, bottom:thin, left:thin, right:NOB }, vAlign:VerticalAlign.TOP, margins:{top:240,bottom:200,left:100,right:100} }),
    cell([
      new Paragraph({ spacing:{before:0,after:100}, children:[run('Podstawa prawna',{size:24,bold:true,color:COLOR.purple})] }),
      new Paragraph({ spacing:{before:0,after:0,line:290}, alignment:AlignmentType.JUSTIFIED, children:[
        run('Zgodnie z Rozporządzeniem Ministra Edukacji z dnia 2 marca 2026 r. w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające działające w publicznych poradniach psychologiczno-pedagogicznych ', {size:18}),
        run('(Dz. U. z 2026 r. poz. 428)', {size:18, bold:true, color:COLOR.purple}),
        run(', a w szczególności wchodzącymi w życie z dniem 1 września 2026 r. przepisami ', {size:18}),
        run('§ 7 ust. 6 i ust. 7', {size:18, bold:true, color:COLOR.purple}),
        run(', opinia przedszkola/szkoły wydawana dla zespołu poradni (i przekazywana rodzicowi) musi mieć ściśle określoną strukturę opartą na obszarach ICF: odrębnych dla dziecka w wieku przedszkolnym oraz dla ucznia szkoły.', {size:18})
      ] })
    ], { width:CW-800, bg:COLOR.paper, borders:{ top:thin, bottom:thin, right:thin, left:NOB }, margins:{top:200,bottom:200,left:100,right:240} })
  ]}) ]}),
  empty(240),

  // zawartość raportu
  para('ZAWARTOŚĆ RAPORTU', { size:14, bold:true, color:COLOR.muted, after:120, spacing:20 }),
  new Table({ width:{size:CW,type:WidthType.DXA}, columnWidths:[3150,3150,3446], rows:[ new TableRow({ children:[
    ['1','Metryczka bazowa','dane dziecka, wariant wsparcia, podstawa formalna, zdrowie i farmakoterapia'],
    ['2','Obserwacja wstępna','procedura wrześniowej obserwacji Kwestionariuszem Oceny Funkcjonalnej w obszarach ICF'],
    ['3','Obserwacja pogłębiona','wskazania i narzędzia: ABC, Profil Biopsychospołeczny, Profil Sensoryczny, mowa i AAC, ToM']
  ].map((t,i) => cell([
    new Paragraph({ spacing:{before:0,after:40}, children:[run(t[0],{size:36,bold:true,color:COLOR.orange})] }),
    new Paragraph({ spacing:{before:0,after:60}, children:[run(t[1],{size:20,bold:true,color:COLOR.purple})] }),
    new Paragraph({ spacing:{before:0,after:0,line:250}, children:[run(t[2],{size:16,color:COLOR.muted})] })
  ], { width:[3150,3150,3446][i], borders:{ top:{style:BorderStyle.SINGLE,size:36,color:COLOR.orange}, bottom:thin, left:thin, right:thin }, margins:{top:160,bottom:160,left:180,right:180} })) }) ]}),
  empty(200),
  runs(['ICF','KSzOF','ABC','Profil Sensoryczny','AAC','ToM'].flatMap((t,i)=>[ run(' '+t+' ', {size:16, bold:true, color:[COLOR.purple,COLOR.orange,COLOR.green,COLOR.teal,COLOR.purple,COLOR.orange][i]}), run('   ', {size:16}) ]), { after:0 }),
  new Paragraph({ children:[ new PageBreak() ] })
];

// =============== SEKCJA 1 · METRYCZKA ===============
const LW = 3000, RW = CW-LW;
const metaRow = (label, valueChildren, shade) => new TableRow({ children:[
  tcell(label, { width:LW, bg:COLOR.purple, color:'FFFFFF', bold:true, size:15, caps:true }),
  cell(valueChildren, { width:RW, bg: shade ? COLOR.paper : 'FFFFFF' })
]});
const vp = (children) => new Paragraph({ spacing:{before:0,after:0,line:270}, children });
const meta = new Table({ width:{size:CW,type:WidthType.DXA}, columnWidths:[LW,RW], rows:[
  metaRow('Imię i nazwisko', vp([ph('[Imię i Nazwisko dziecka / ucznia]')])),
  metaRow('Data urodzenia', vp([ph('[Data urodzenia]')]), true),
  metaRow('Placówka / Oddział', vp([ph('[Nazwa przedszkola / szkoły, grupa / klasa]')])),
  metaRow('Wariant wsparcia', [
    checkbox([ run('Wariant A', {bold:true,color:COLOR.purple,size:18}), run(' – wsparcie na podstawie orzeczenia o potrzebie kształcenia specjalnego', {size:18}) ]),
    checkbox([ run('Wariant B', {bold:true,color:COLOR.purple,size:18}), run(' – wsparcie w ramach pomocy psychologiczno-pedagogicznej (bez orzeczenia)', {size:18}) ])
  ], true),
  metaRow('Jednostka / Podstawa formalna', vp([ run('Na podstawie dołączonego dokumentu: ',{size:18}), ph('[Orzeczenie / Opinia]'), run(' nr ',{size:18}), ph('[Numer]'), run(' z dnia ',{size:18}), ph('[Data]'), run(', wydanego przez: ',{size:18}), ph('[Nazwa Poradni]'), run(', z uwagi na: ',{size:18}), ph('[np. autyzm, w tym zespół Aspergera / niepełnosprawność ruchowa / inne]') ])),
  metaRow('Schorzenia przewlekłe', [
    checkbox([ run('Brak', {size:18}) ]),
    checkbox([ run('Występują: ', {size:18}), ph('[np. cukrzyca, astma, epilepsja]') ])
  ], true),
  metaRow('Farmakoterapia i wskazania lekarza', vp([ run('Zgodnie ze wskazaniami lekarza dziecko/uczeń ',{size:18}), run('stale / doraźnie',{size:18,bold:true}), run(' przyjmuje leki: ',{size:18}), ph('[Nazwa leków, zalecenia postępowania / Nie dotyczy]') ]))
]});

// =============== SEKCJA 2 · PROCEDURA ===============
const steps = [
  ['①','Zgłoszenie','zgłaszane trudności w funkcjonowaniu oraz wniosek rodzica'],
  ['②','Dokumentacja','posiadana opinia / orzeczenie poradni psychologiczno-pedagogicznej'],
  ['③','Obserwacja · wrzesień','Kwestionariusz Przedszkolnej / Szkolnej Oceny Funkcjonalnej'],
  ['④','Analiza ICF','obszary zgodne z Międzynarodową Klasyfikacją Funkcjonowania']
];
const SW = Math.floor(CW/4);
const flow = new Table({ width:{size:SW*4,type:WidthType.DXA}, columnWidths:[SW,SW,SW,SW], rows:[ new TableRow({ children: steps.map(s => cell([
  new Paragraph({ spacing:{before:0,after:40}, children:[run(s[0],{size:34,bold:true,color:COLOR.orange})] }),
  new Paragraph({ spacing:{before:0,after:60}, children:[run(s[1],{size:18,bold:true,color:COLOR.purple})] }),
  new Paragraph({ spacing:{before:0,after:0,line:240}, children:[run(s[2],{size:15,color:COLOR.muted})] })
], { width:SW, margins:{top:140,bottom:140,left:140,right:140} })) }) ]});

const icfRow = new Table({ width:{size:CW,type:WidthType.DXA}, columnWidths:[1949,1949,1949,1949,1950], rows:[ new TableRow({ children:[
  ['Funkcje ciała','b'],['Struktury ciała','s'],['Aktywność i uczestnictwo','d'],['Czynniki środowiskowe','e'],['Czynniki osobowe','—']
].map((t,i) => cell([
  new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:20}, children:[run(t[0],{size:15,bold:true,color:COLOR.purple})] }),
  new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:0}, children:[run(t[1],{size:14,color:COLOR.muted})] })
], { width: i===4?1950:1949, bg:COLOR.paper, borders:{ top:{style:BorderStyle.DASHED,size:4,color:COLOR.rule}, bottom:{style:BorderStyle.DASHED,size:4,color:COLOR.rule}, left:{style:BorderStyle.DASHED,size:4,color:COLOR.rule}, right:{style:BorderStyle.DASHED,size:4,color:COLOR.rule} }, margins:{top:120,bottom:120,left:80,right:80}, vAlign:VerticalAlign.CENTER })) }) ]});

// =============== SEKCJA 3 · NARZĘDZIA ===============
const toolCell = (tag, title, desc, color, width, extra=[]) => cell([
  new Paragraph({ spacing:{before:0,after:40}, children:[run(tag.toUpperCase(),{size:13,bold:true,color, spacing:15})] }),
  new Paragraph({ spacing:{before:0,after:80,line:250}, children:[run(title,{size:21,bold:true,color:COLOR.purple})] }),
  new Paragraph({ spacing:{before:0,after:0,line:255}, children:[run(desc,{size:17})] }),
  ...extra
], { width, borders:{ top:{style:BorderStyle.SINGLE,size:36,color}, bottom:thin, left:thin, right:thin }, margins:{top:160,bottom:180,left:180,right:180} });

const HW = CW/2;
const abcRow = new Table({ width:{size:CW-360,type:WidthType.DXA}, columnWidths:[3128,3128,3130], rows:[ new TableRow({ children:[
  ['A','bodźce wyzwalające'],['B','forma zachowania'],['C','funkcja i skutki podtrzymujące']
].map((t,i) => cell([
  new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:20}, children:[run(t[0],{size:28,bold:true,color:COLOR.red})] }),
  new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:0}, children:[run(t[1],{size:15,bold:true,color:COLOR.red})] })
], { width:[3128,3128,3130][i], bg:COLOR.orangeMist, borders:{ top:NOB, bottom:NOB, left:{style:BorderStyle.SINGLE,size:24,color:'FFFFFF'}, right:{style:BorderStyle.SINGLE,size:24,color:'FFFFFF'} }, margins:{top:100,bottom:100,left:60,right:60} })) }) ]});

const tools = [
  new Table({ width:{size:CW,type:WidthType.DXA}, columnWidths:[CW], rows:[ new TableRow({ children:[
    toolCell('Zachowania trudne','Arkusz Obserwacji Behawioralnej ABC','Zastosowany z uwagi na występowanie zachowań trudnych – identyfikacja bodźców wyzwalających, formy zachowania oraz funkcji i skutków podtrzymujących.', COLOR.red, CW, [ empty(120), abcRow ])
  ]}) ]}),
  empty(160),
  new Table({ width:{size:CW,type:WidthType.DXA}, columnWidths:[HW,HW], rows:[
    new TableRow({ children:[
      toolCell('Całościowy obraz','Profil Biopsychospołeczny','Ujęcie funkcjonowania dziecka w wymiarze biologicznym, psychologicznym i społecznym – zgodnie z modelem ICF.', COLOR.purple, HW),
      toolCell('Przetwarzanie bodźców','Profil Sensoryczny','Ocena reaktywności sensorycznej (nadwrażliwości, podwrażliwości, poszukiwania stymulacji) i wpływu bodźców środowiskowych na dysregulację dziecka.', COLOR.teal, HW)
    ]}),
    new TableRow({ children:[
      toolCell('Komunikacja','Arkusz Oceny Rozwoju Mowy i Komunikacji','Zastosowany w związku ze specyficznymi trudnościami w nadawaniu i rozumieniu mowy, echolaliami lub potrzebą wdrożenia / rozwijania AAC.', COLOR.orange, HW),
      toolCell('Funkcje poznawcze i społeczne','Arkusz Poziomu Rozwoju Teorii Umysłu (ToM)','Zbadanie poziomu rozumienia stanów mentalnych, intencji, perspektywy i emocji innych osób w sytuacjach społecznych.', COLOR.green, HW)
    ]})
  ]})
];

// =============== PODPISY ===============
const sigCell = (role, width, span) => new TableCell({
  width:{ size:width, type:WidthType.DXA }, columnSpan: span,
  margins:{ top:900, bottom:80, left:200, right:200 },
  borders:noBorders,
  children:[
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:0,after:0}, border:{ top:{ style:BorderStyle.SINGLE, size:8, color:COLOR.ink, space:6 } }, children:[run(role,{size:16,italic:true,bold:true,color:COLOR.purple})] }),
    new Paragraph({ alignment:AlignmentType.CENTER, spacing:{before:20,after:0}, children:[run('podpis i data',{size:12,color:COLOR.muted})] })
  ]
});
const SGW = Math.floor(CW/3);
const sigs = new Table({ width:{size:SGW*3,type:WidthType.DXA}, columnWidths:[SGW,SGW,SGW], rows:[
  new TableRow({ children:[ sigCell('Koordynator Zespołu',SGW), sigCell('Dyrektor placówki',SGW), sigCell('Specjalista',SGW) ] }),
  new TableRow({ children:[ sigCell('Rodzic / opiekun prawny – zapoznałam/em się z raportem', SGW*3, 3) ] })
]});

// =============== HEADER / FOOTER ===============
const headerPara = new Paragraph({
  spacing:{before:0,after:0}, border:{ bottom:{ style:BorderStyle.SINGLE, size:8, color:COLOR.purple, space:4 } },
  tabStops:[{ type:TabStopType.RIGHT, position:9740 }],
  children:[ run('EduPlaner2026-MJ-PCTP',{size:16,bold:true,color:COLOR.purple}), run('  ·  ',{size:16,color:COLOR.rule}), run('RAPORT OCENY FUNKCJONALNEJ',{size:16,bold:true,color:COLOR.orange}), run('\t'), run('Dziecko / uczeń: ',{size:14,color:COLOR.muted}), run('…………………………',{size:14,italic:true,color:COLOR.purple}) ]
});
const footerPara = new Paragraph({
  spacing:{before:60,after:0}, border:{ top:{ style:BorderStyle.SINGLE, size:4, color:COLOR.rule, space:4 } },
  tabStops:[{ type:TabStopType.RIGHT, position:9740 }],
  children:[ run('Raport Oceny Funkcjonalnej · EduPlaner 2026',{size:12,color:COLOR.muted}), run('   ·   ',{size:12,color:COLOR.rule}), run('RODO · Dokument poufny',{size:12,color:COLOR.muted}), run('\t'), run('Strona ',{size:12,color:COLOR.muted}), new TextRun({ children:[PageNumber.CURRENT], font:FONT, size:12, bold:true, color:COLOR.orange }), run(' z ',{size:12,color:COLOR.muted}), new TextRun({ children:[PageNumber.TOTAL_PAGES], font:FONT, size:12, bold:true, color:COLOR.purple }) ]
});
const coverFooter = new Paragraph({
  spacing:{before:0,after:0}, border:{ top:{ style:BorderStyle.SINGLE, size:4, color:COLOR.rule, space:4 } },
  tabStops:[{ type:TabStopType.RIGHT, position:9740 }],
  children:[ run('Karta Funkcjonalna · rok szkolny 2026/2027',{size:12,color:COLOR.muted}), run('\t'), run('RODO · Dokument poufny',{size:12,color:COLOR.muted}) ]
});

// =============== DOKUMENT ===============
const children = [
  ...cover,
  section('1','Metryczka bazowa'),
  meta,
  section('2','Podstawa i procedura obserwacji wstępnej'),
  flow,
  empty(200),
  boxPara([ run('Z uwagi na zgłaszane trudności w funkcjonowaniu, wniosek rodzica oraz posiadaną dokumentację (w tym opinię/orzeczenie poradni), w placówce przeprowadzono ',{size:19,color:COLOR.purple}), run('we wrześniu',{size:19,bold:true,color:COLOR.orange}), run(' obserwację poziomu funkcjonowania z wykorzystaniem ',{size:19,color:COLOR.purple}), run('Kwestionariusza Przedszkolnej / Szkolnej Oceny Funkcjonalnej',{size:19,bold:true,color:COLOR.orange}), run(', analizującego funkcjonowanie w obszarach zgodnych z Międzynarodową Klasyfikacją Funkcjonowania, Niepełnosprawności i Zdrowia (ICF).',{size:19,color:COLOR.purple}) ], { before:0, after:0 }),
  empty(220),
  icfRow,
  new Paragraph({ children:[ new PageBreak() ] }),
  section('3','Wskazania do obserwacji pogłębionej i zastosowane narzędzia'),
  runs([ run('W związku ze zidentyfikowanymi w toku oceny wstępnej trudnościami w funkcjonowaniu – w szczególności w zakresie ',{size:19}), run('trudnych zachowań',{size:19,bold:true}), run(', ',{size:19}), run('rozwoju funkcji poznawczych',{size:19,bold:true}), run(', ',{size:19}), run('przetwarzania bodźców',{size:19,bold:true}), run(' oraz ',{size:19}), run('komunikacji',{size:19,bold:true}), run(' – przeprowadzono obserwację pogłębioną z wykorzystaniem następujących narzędzi specjalistycznych:',{size:19}) ], { after:200, line:290, align:AlignmentType.JUSTIFIED }),
  ...tools,
  empty(240),
  boxPara([ run('Informacja dla rodzica. ',{size:18,bold:true,color:COLOR.orange}), run('Niniejszy raport stanowi opinię placówki o funkcjonowaniu dziecka i jest przekazywany rodzicowi oraz zespołowi orzekającemu poradni. Wyniki obserwacji służą zaplanowaniu wsparcia, a nie ocenie dziecka. Zachęcamy do rozmowy z Zespołem o każdej części dokumentu.',{size:18}) ], { bg:COLOR.orangeMist, edge:COLOR.orange }),
  empty(200),
  sigs
];

const doc = new Document({
  creator: 'EduPlaner2026-MJ-PCTP', title: 'Raport Oceny Funkcjonalnej', description: 'Opinia przedszkola/szkoły dla zespołu orzekającego i rodzica (obszary ICF)',
  styles:{ default:{ document:{ run:{ font:FONT, size:20, color:COLOR.ink } } } },
  sections:[{
    properties:{ titlePage:true, page:{ size:A4, margin:MARGINS } },
    headers:{ first: new Header({ children:[ empty() ] }), default: new Header({ children:[ headerPara ] }) },
    footers:{ first: new Footer({ children:[ coverFooter ] }), default: new Footer({ children:[ footerPara ] }) },
    children
  }]
});
Packer.toBuffer(doc).then(buf => { fs.writeFileSync(process.argv[2], buf); console.log('OK', buf.length); });
