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

  // zawartość raportu
  P([ run('■ ', { size:14, color:C.purple }), run('CZĘŚĆ I · PODSTAWA, METRYCZKA I NARZĘDZIA', { size:12, bold:true, color:C.purple, spacing:14 }) ], { after:80 }),
  tbl([3302,3302,3302], [ row([
    ['1','Metryczka bazowa','dane dziecka, wariant wsparcia, podstawa formalna, zdrowie i farmakoterapia'],
    ['2','Obserwacja wstępna','procedura wrześniowej obserwacji Kwestionariuszem Oceny Funkcjonalnej w obszarach ICF'],
    ['3','Obserwacja pogłębiona','wskazania i narzędzia: ABC, Profil Biopsychospołeczny, Profil Sensoryczny, mowa i AAC, ToM']
  ].map(t => cell([
    P([ run(t[0], { size:28, bold:true, color:C.orange }) ], { after:30 }),
    P([ run(t[1], { size:18, bold:true, color:C.purple }) ], { after:40 }),
    P([ run(t[2], { size:14, color:C.muted }) ], { after:0, line:240 })
  ], { width:3302, borders:{ top:{ style:BorderStyle.SINGLE, size:24, color:C.orange }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:90, bottom:100, left:160, right:160 } })) ) ]),
  empty(90),
  P([ run('■ ', { size:14, color:C.purple }), run('CZĘŚĆ II · WYNIKI ILOŚCIOWE I JAKOŚCIOWE, OCENA POGŁĘBIONA, KIERUNKI WSPARCIA W IPE', { size:12, bold:true, color:C.purple, spacing:14 }) ], { after:80 }),
  tbl([1981,1981,1981,1981,1982], [ row([
    ['4','Funkcjonowanie w placówce','mocne strony, uzdolnienia i trudności'],
    ['5','Wyniki liczbowe','KPOF / KSzOF w 9 domenach ICF'],
    ['6','Analiza jakościowa','opis barier i zalecenia do IPE'],
    ['7','Obserwacja pogłębiona','wyniki arkuszy specjalistycznych'],
    ['8','Podjęte działania','zakres wsparcia i efektywność']
  ].map((t,i) => cell([
    P([ run(t[0], { size:26, bold:true, color:C.orange }) ], { after:30 }),
    P([ run(t[1], { size:16, bold:true, color:C.purple }) ], { after:40, line:230 }),
    P([ run(t[2], { size:13, color:C.muted }) ], { after:0, line:230 })
  ], { width:i===4?1982:1981, borders:{ top:{ style:BorderStyle.SINGLE, size:24, color:C.orange }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:80, bottom:90, left:130, right:110 } })) ) ]),
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


// =============== CZĘŚĆ II · WYNIKI ARKUSZY ===============
const gridHead = (cols, widths, colors=[]) => row(cols.map((t,i) => cell(P([ run(t, { size:13, bold:true, color:colors[i]||C.purple, caps:true, spacing:10 }) ], { after:0 }), { width:widths[i], bg:C.lav, borders:{ top:ln(), bottom:ln(), left:ln(), right:ln() }, margins:{ top:100, bottom:100, left:140, right:120 } })));
const gcell = (children, width, o={}) => cell(Array.isArray(children)?children:[children], { width, bg:o.bg, borders:{ top:ln(C.line2), bottom:ln(C.line2), right:ln(C.line2), left: o.edge ? { style:BorderStyle.SINGLE, size:24, color:o.edge } : ln(C.line2) }, margins:{ top:100, bottom:100, left:140, right:120 } });
const txt = (t, o={}) => P([ run(t, { size:o.size||16, bold:o.bold, color:o.color }) ], { after:0, line:250 });
const bullets = (items) => items.map(t => new Paragraph({ spacing:{ before:0, after:40, line:245 }, indent:{ left:200, hanging:200 }, children:[ run('•  ', { size:16, color:C.orange, bold:true }), run(t, { size:16 }) ] }));
const lead2 = (ref, t) => P([ ...(ref ? [run(ref+' ', { size:16, bold:true, color:C.purple })] : []), run(t, { size:16, color:C.muted }) ], { after:140, line:260, align:AlignmentType.JUSTIFIED });

const rows4 = [
 ['Aktywność poznawcza i uczenie się','Bardzo dobra pamięć wzrokowa; szybkie zapamiętywanie schematów graficznych; wąskie, ale głębokie zainteresowania tematyczne; wysoka motywacja do pracy z ulubionymi pomocami dydaktycznymi.','Trudności z przerzutnością i podzielnością uwagi; szybka męczliwość przy instrukcjach wieloetapowych; problem z uogólnianiem (generalizacją) wiedzy; wymagane stałe tempo i pomoce wizualne.'],
 ['Komunikacja i porozumiewanie się','Prawidłowe rozumienie prostych, jednoznacznych komunikatów słownych wspartych gestem; sygnalizowanie podstawowych potrzeb fizjologicznych.','Dosłowne rozumienie wypowiedzi (trudność z metaforą i żartem); echolalie odroczone; trudności w inicjowaniu dialogu i naprzemienności wypowiedzi w grupie rówieśniczej; potrzeba wsparcia AAC.'],
 ['Relacje społeczne i emocje','Chęć przebywania w pobliżu grupy; pozytywna reakcja na stałych, przewidywalnych dorosłych; przestrzeganie czytelnych zasad wizualnych.','Trudności w odczytywaniu emocji i intencji innych (słaba teoria umysłu); niska tolerancja frustracji w sytuacjach przegranej lub nagłej zmiany; tendencja do wycofywania się lub zachowań trudnych.'],
 ['Motoryka i sprawność fizyczna','Sprawność w zakresie motoryki dużej (bieganie, wspinanie się); chętne uczestnictwo w zabawach ruchowych w otwartej przestrzeni.','Obniżona precyzja motoryki małej i koordynacji wzrokowo-ruchowej; nieprawidłowy chwyt pisarski / narzędzi; wzmożone lub obniżone napięcie posturalne; męczliwość ręki wiodącej.'],
 ['Samoobsługa i autonomia','Samodzielność w zakresie podstawowych nawyków higienicznych i toaletowych; znajomość własnej szafki i osobistych przyborów.','Opór sensoryczny przy myciu rąk (wrażliwość na fakturę mydła/wodę); wybiórczość pokarmowa; problem z ubieraniem odzieży wierzchniej ze skomplikowanymi zapięciami; potrzeba nadzoru dorosłego.']
];
const W4 = [1900, 4003, 4003];
const table4 = tbl(W4, [ gridHead(['Obszar obserwacji','✓ Mocne strony, zasoby i uzdolnienia','▸ Trudności, ograniczenia i bariery'], W4, [C.purple, C.green, C.red]),
  ...rows4.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W4[0]), gcell(txt(r[1]), W4[1], { edge:C.green }), gcell(txt(r[2]), W4[2], { edge:C.red }) ])) ]);

const dom = [
 ['d1','Uczenie się i stosowanie wiedzy','2,4','12','4',2,'Średni','Wymaga podziału zadań na etapy i wsparcia wizualnego.'],
 ['d2','Ogólne zadania i wymagania','1,8','9','3',3,'Wysoki','Brak elastyczności, silny stres przy nagłych zmianach.'],
 ['d3','Komunikacja i porozumiewanie się','2,0','10','4',2,'Średni','Echolalie, konieczność wdrażania schematów AAC.'],
 ['d4','Poruszanie się i motoryka','3,2','16','6',1,'Niski','Ogólna motoryka dobra; obniżona grafomotoryka.'],
 ['d5','Dbanie o siebie i samoobsługa','2,2','11','4',2,'Średni','Wybiórczość sensoryczna przy posiłkach i toalecie.'],
 ['d6','Życie domowe / Obowiązki placówki','2,8','14','5',1,'Niski','Sprząta kącik zabaw po bezpośrednim przypomnieniu.'],
 ['d7','Relacje i kontakty międzyludzkie','1,6','8','3',3,'Wysoki','Bariery w interakcjach rówieśniczych, konflikty, wycofanie.'],
 ['d8','Główne dziedziny życia (Edukacja)','2,0','10','4',2,'Średni','Wymaga dostosowania metod i stałego nadzoru nauczyciela.'],
 ['d9','Życie społecznościowe i obywatelskie','1,8','9','3',3,'Wysoki','Trudność w uczestnictwie w apelach i wyjściach zbiorowych.']
];
const LVL = { 1:{ bg:'E6F4EC', fg:C.green }, 2:{ bg:'FBF1DC', fg:'9A6A0A' }, 3:{ bg:'FBE6E3', fg:C.red } };
const W5 = [600, 2500, 1500, 800, 1700, 2806];
const statTile = (l, v, sub, width, top=C.orange) => cell([
  P([ run(l, { size:12, bold:true, color:C.lavText, spacing:12 }) ], { after:40 }),
  P([ run(v, { size:26, bold:true, color:C.purple }), run(sub ? '  '+sub : '', { size:15, color:C.muted }) ], { after:0 })
], { width, borders:{ top:{ style:BorderStyle.SINGLE, size:24, color:top }, bottom:ln(), left:ln(), right:ln() }, margins:{ top:110, bottom:120, left:160, right:120 } });
const SWT = Math.floor(CW/4);
const stats5 = tbl([SWT,SWT,SWT,SWT], [ row([ statTile('NARZĘDZIE BAZOWE','KPOF','/ KSzOF',SWT), statTile('PUNKTY SUROWE','68','/ 180 pkt',SWT), statTile('ŚREDNIA / STEN','Śr: 2,1','· Sten 4',SWT), statTile('OGÓLNY POZIOM WSPARCIA','Poziom 2','(Umiarkowany)',SWT,C.amber) ]) ]);
const table5 = tbl(W5, [ gridHead(['Kod','Domena ICF','Punkty / śr.','Sten','Poziom wsparcia','Wskaźnik funkcjonalny'], W5),
  ...dom.map(d => row([
    gcell(txt(d[0], { bold:true, color:C.orange }), W5[0]),
    gcell(txt(d[1], { bold:true }), W5[1]),
    gcell(txt('Śr: '+d[2]+' ('+d[3]+' pkt)'), W5[2]),
    gcell(txt('Sten '+d[4]), W5[3]),
    gcell(P([ run(' Poziom '+d[5]+' · '+d[6]+' ', { size:14, bold:true, color:LVL[d[5]].fg, bg:LVL[d[5]].bg }) ], { after:0 }), W5[4]),
    gcell(txt(d[7]), W5[5])
  ])) ]);
const legend5 = P([ run('Poziom 1 · Niski', { size:13, bold:true, color:LVL[1].fg, bg:LVL[1].bg }), run('    ', { size:13 }), run('Poziom 2 · Średni', { size:13, bold:true, color:LVL[2].fg, bg:LVL[2].bg }), run('    ', { size:13 }), run('Poziom 3 · Wysoki', { size:13, bold:true, color:LVL[3].fg, bg:LVL[3].bg }) ], { align:AlignmentType.RIGHT, before:100, after:0 });

const rows6 = [
 ['Uczenie się i stosowanie wiedzy','d1, d2','Dziecko/uczeń przyswaja wiedzę głównie kanałem wzrokowym. Występuje trudność w samodzielnej organizacji pracy, rozumieniu poleceń złożonych oraz transferze wiedzy. Przebodźcowanie powoduje dekoncentrację i rezygnację z zadania.',['Wprowadzenie planów aktywności w formie piktogramów / checklist.','Dzielenie instrukcji na pojedyncze, sekwencyjne kroki.','Stosowanie pomocy sensorycznych (stoper, zegar time-timer).','Wydłużenie czasu na realizację zadań pisemnych i wykonawczych.']],
 ['Komunikacja i porozumiewanie się','d3','Wypowiedzi cechują się trudnościami pragmatycznymi, obecnością echolalii oraz dosłownością interpretacji. W chwilach przeciążenia emocjonalnego następuje mutyzm wybiórczy lub krzyk zamiast komunikacji intencjonalnej.',['Wdrożenie tablic wyboru i skryptów dialogowych AAC.','Unikanie metafor, sarkazmu, dwuznaczności w komunikatach personelu.','Trening komunikacji funkcjonalnej (FCT – sygnalizowanie: „chcę przerwę”, „nie rozumiem”).','Indywidualna terapia logopedyczna/neurologopedyczna (2x w tyg.).']],
 ['Relacje i interakcje międzyludzkie','d7, d9','Trudności w inicjowaniu i podtrzymywaniu zabawy naprzemiennej. Brak umiejętności rozpoznawania sygnałów niewerbalnych wysyłanych przez rówieśników. Częste nieporozumienia prowadzące do zachowań oporowych.',['Udział w Treningu Umiejętności Społecznych (TUS) w małej grupie.','Modelowanie zachowań prospołecznych z wykorzystaniem Historyjek Społecznych (Social Stories).','Asystowanie w zabawach grupowych na zasadzie rówieśnika-mentora.','Jasne, wizualne zasady panujące w klasie/grupie.']],
 ['Dbanie o siebie i motoryka','d4, d5, d6','Samoobsługa zaburzona przez silne reakcje nadwrażliwości na bodźce dotykowe (ubrania, mokre ręce) i zapachowe. Spowolniona koordynacja ruchowa i trudności z planowaniem motorycznym (dyspraksja).',['Dostosowanie przyborów (nakładki ergonomiczne na ołówki, nożyczki sprężynowe).','Stała kolejność czynności toaletowych wsparta paskiem wizualnym.','Indywidualne ćwiczenia rewalidacyjne ukierunkowane na motorykę małą i dużą.']]
];
const W6 = [1900, 3900, 4106];
const table6 = tbl(W6, [ gridHead(['Domena ICF','Opis funkcjonowania i bariery','Zalecenia do IPE (metody / dostosowania)'], W6, [C.purple, C.purple, C.orange]),
  ...rows6.map(r => row([ gcell([ txt(r[0], { bold:true, color:C.purple }), txt(r[1], { size:14, color:C.orange, bold:true }) ], W6[0]), gcell(txt(r[2]), W6[1]), gcell(bullets(r[3]), W6[2]) ])) ]);

const res7 = [
 [C.red,'Arkusz Obserwacji Behawioralnej ABC',[['Zidentyfikowano '],['14 epizodów',1],[' zachowań trudnych. '],['Bodźce wyzwalające (A): ',1],['trudne polecenia pisemne, hałas, niespodziewane przejścia między aktywnościami. '],['Topografia zachowania (B): ',1],['głośny krzyk, odmowa zejścia z dywanu, odpychanie kart pracy. '],['Funkcja (C): ',1],['ucieczka przed przeciążeniem sensorycznym / zadaniem trudnym poznawczo.']],'protokół wyprzedzający i nauka komunikatu zastępczego.'],
 [C.blue,'Profil Sensoryczny (Kwestionariusz Przetwarzania)',[['Reaktywność mieszana. '],['Układ słuchowy',1],[' – silna nadwrażliwość na nagłe dźwięki i gwar korytarza (zalecane słuchawki); '],['układ dotykowy',1],[' – obronność dotykowa na faktury klejące i mokre; '],['układ proprioceptywny i przedsionkowy',1],[' – poszukiwanie stymulacji dociskowej i ruchowej (huśtanie, kołysanie się).']],null],
 [C.purple,'Profil Biopsychospołeczny',[['Uwarunkowania biologiczne: ',1],['spektrum autyzmu, zaburzenia snu wpływają na zmęczenie poranne. '],['Uwarunkowania psychologiczne: ',1],['silny lęk przed zmianą schematu, sztywność poznawcza. '],['Czynniki środowiskowe: ',1],['wysokie zaangażowanie rodziny, pozytywna reakcja na stałą kadrę.']],null],
 [C.orange,'Arkusz Oceny Rozwoju Mowy i Komunikacji',[['Zasób słownika biernego w normie wiekowej; wąski zasób czynny w sytuacjach swobodnych. Występują '],['echolalie natychmiastowe',1],[' i trudności pragmatyczne (brak intonacji, trudność w podtrzymaniu dialogu).']],'schematy dialogowe i piktogramy wspierające.'],
 [C.green,'Arkusz Poziomu Rozwoju Teorii Umysłu (ToM)',[['Poziom rozwoju ToM '],['poniżej normy wiekowej',1],['. Trudność w zadaniach z fałszywym przekonaniem (False Belief Task) oraz w rozpoznawaniu perspektywy i intencji innych osób. Trudności te generują konflikty rówieśnicze przez błędną interpretację zachowań kolegów.']],null]
];
const resCards = res7.flatMap(([color, title, parts, rec]) => [
  tbl([CW], [ row([ cell([
    P([ run(title, { size:18, bold:true, color:C.purple }) ], { after:50 }),
    P(parts.map(pt => run(pt[0], { size:16, bold:!!pt[1], color: pt[1] ? color : C.ink })), { after: rec ? 50 : 0, line:255, align:AlignmentType.JUSTIFIED }),
    ...(rec ? [ P([ run('Zalecenie: ', { size:16, bold:true, color:C.orange }), run(rec, { size:16, color:C.purple }) ], { after:0 }) ] : [])
  ], { width:CW, borders:{ top:ln(), bottom:ln(), right:ln(), left:{ style:BorderStyle.SINGLE, size:32, color } }, margins:{ top:110, bottom:120, left:220, right:180 } }) ]) ]),
  empty(90)
]);

const rows8 = [
 ['Dostosowania środowiskowe i dydaktyczne','Wyznaczenie strefy wyciszenia w sali; zredukowanie bodźców wzrokowych na tablicach ściennych; zastosowanie słuchawek wygłuszających podczas pracy stolikowej; wprowadzenie indywidualnego planu dnia na rzepy.','Spadek liczby epizodów trudnych zachowań o ok. 40%; wydłużenie czasu skupienia na pojedynczym zadaniu z 3 do 8 minut.'],
 ['Pomoc psychologiczno-pedagogiczna i rewalidacja','Zajęcia rozwijające kompetencje emocjonalno-społeczne (TUS – 1x w tyg.); indywidualne zajęcia logopedyczne (1x w tyg.); ćwiczenia integracji sensorycznej (SI) na sali gimnastycznej.','Lepsze tolerowanie obecności innych dzieci w trakcie zajęć kierowanych; pierwsze próby proszenia o przerwę za pomocą gestu/piktogramu.'],
 ['Współpraca z domem rodzinnym','Cotygodniowe konsultacje z rodzicami; zeszyt korespondencji dom-placówka; ujednolicenie systemu komunikatów i nagród behawioralnych.','Wysoka spójność w reakcjach dorosłych na zachowania trudne; wzrost poczucia bezpieczeństwa u dziecka.']
];
const W8 = [2000, 4300, 3606];
const table8 = tbl(W8, [ gridHead(['Rodzaj wsparcia','Zakres wdrożonych działań i metody','Efektywność i obserwowane zmiany'], W8, [C.purple, C.purple, C.green]),
  ...rows8.map(r => row([ gcell(txt(r[0], { bold:true, color:C.purple }), W8[0]), gcell(txt(r[1]), W8[1]), gcell(txt(r[2]), W8[2], { edge:C.green }) ])) ]);

const parentBox = tbl([CW], [ row([ cell(P([ run('Informacja dla rodzica. ', { size:17, bold:true, color:C.orange }), run('Niniejszy raport stanowi opinię placówki o funkcjonowaniu dziecka i jest przekazywany rodzicowi oraz zespołowi orzekającemu poradni. Wyniki obserwacji służą zaplanowaniu wsparcia, a nie ocenie dziecka. Zachęcamy do rozmowy z Zespołem o każdej części dokumentu.', { size:17 }) ], { after:0, line:270 }), { width:CW, bg:C.paper, borders:{ top:ln(C.line2), bottom:ln(C.line2), left:ln(C.line2), right:ln(C.line2) }, margins:{ top:120, bottom:120, left:220, right:220 } }) ]) ]);

const part2 = [
  new Paragraph({ children:[ new PageBreak() ] }),
  ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Funkcjonowanie w placówce'),
  P([ run('  RAPORT OCENY FUNKCJONALNEJ DZIECKA / UCZNIA · CZĘŚĆ II  ', { size:13, bold:true, color:C.white, bg:C.orange, spacing:10 }) ], { align:AlignmentType.CENTER, after:120 }),
  P([ run('Wyniki ilościowe i jakościowe, ocena pogłębiona oraz kierunki wsparcia w IPE', { size:28, bold:true, color:C.purple }) ], { align:AlignmentType.CENTER, after:60, line:300 }),
  P([ run('WYNIKI POSZCZEGÓLNYCH ARKUSZY OBSERWACJI · § 7 UST. 6', { size:13, bold:true, color:C.orange, spacing:36 }) ], { align:AlignmentType.CENTER, after:60 }),
  section('4','Informacja o funkcjonowaniu w placówce – trudności, mocne strony i uzdolnienia'),
  lead2('§ 7 ust. 6 pkt 3.','Syntetyczne zestawienie potencjału rozwojowego oraz barier zidentyfikowanych w toku codziennej aktywności przez nauczycieli, wychowawców i specjalistów prowadzących zajęcia z dzieckiem/uczniem:'),
  table4,
  new Paragraph({ children:[ new PageBreak() ] }),
  ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Wyniki liczbowe'),
  section('5','Aktualna wielospecjalistyczna ocena poziomu funkcjonowania – wyniki liczbowe'),
  lead2('§ 7 ust. 6 pkt 4.','Zestawienie parametrów ilościowych uzyskanych z narzędzia bazowego (KPOF dla przedszkola / KSzOF dla szkoły) w 9 obszarach Międzynarodowej Klasyfikacji ICF:'),
  stats5,
  empty(140),
  table5,
  legend5,
  new Paragraph({ children:[ new PageBreak() ] }),
  ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Analiza jakościowa'),
  section('6','Analiza jakościowa obszarów obserwacji oraz zalecenia do IPE'),
  lead2('','Szczegółowa diagnoza funkcjonalna powiązana bezpośrednio ze sformułowanymi rekomendacjami do Indywidualnego Programu Edukacyjnego (IPE):'),
  table6,
  new Paragraph({ children:[ new PageBreak() ] }),
  ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Obserwacja pogłębiona'),
  section('7','Wyniki obserwacji pogłębionej (narzędzia specjalistyczne)'),
  ...resCards,
  new Paragraph({ children:[ new PageBreak() ] }),
  ...pageHeader('Raport Oceny Funkcjonalnej · Część II · Podjęte działania i podpisy'),
  section('8','Informacja o działaniach podjętych w celu poprawy funkcjonowania'),
  lead2('§ 7 ust. 6 pkt 6.',''),
  table8,
  empty(140),
  parentBox,
  empty(60),
  sigs
];

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
