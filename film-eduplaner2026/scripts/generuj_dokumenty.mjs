/**
 * Generuje dokumenty produkcyjne filmu z JEDNEGO źródła prawdy (../scenariusz.json):
 *   1. EduPlaner2026_Storyboard_HeyGen.docx  — tabela: scena · ekran · tekst awatara · animacja
 *   2. EduPlaner2026_Narracja.docx           — czysty tekst do wklejenia w HeyGen → Script
 *   3. SCENARIUSZ_3MIN.md                    — scenariusz do czytania i poprawiania
 *
 * Uruchomienie:  cd scripts && npm install && node generuj_dokumenty.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  AlignmentType, BorderStyle, Document, Packer, PageOrientation, Paragraph,
  ShadingType, Table, TableCell, TableRow, TextRun, WidthType,
} from 'docx';

const tu = path.dirname(fileURLToPath(import.meta.url));
const katalog = path.join(tu, '..');
const S = JSON.parse(fs.readFileSync(path.join(katalog, 'scenariusz.json'), 'utf8'));

const FIOLET = '2D1B69';
const POMARANCZ = 'E8450A';
const FONT = 'Arial';
const W = { S: 1500, E: 3900, A: 6100, U: 2938 };
const SUMA = W.S + W.E + W.A + W.U;

const run = (o) => new TextRun({ font: FONT, ...o });
const P = (children, opt = {}) => new Paragraph({ children, ...opt });
const mmss = (s) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`;

const komorkaNaglowka = (t, w) =>
  new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: FIOLET },
    margins: { top: 80, bottom: 80, left: 120, right: 120 },
    children: [P([run({ text: t, bold: true, color: 'FFFFFF', size: 22 })])],
  });

const komorka = (akapity, w, fill) =>
  new TableCell({
    width: { size: w, type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, fill } : undefined,
    margins: { top: 100, bottom: 100, left: 120, right: 120 },
    children: akapity,
  });

/* ---------- 1. STORYBOARD ---------- */
const wiersze = S.sceny.map((s) => {
  const scena = komorka(
    [
      P([run({ text: String(s.nr), bold: true, color: POMARANCZ, size: 30 })]),
      P([run({ text: s.tytul, bold: true, color: FIOLET, size: 18 })], { spacing: { before: 40 } }),
      P([run({ text: `${mmss(s.od)}–${mmss(s.od + s.czas)}`, color: '444444', size: 17 })], {
        spacing: { before: 40 },
      }),
      P([run({ text: `${s.czas} s`, color: '444444', size: 17 })]),
    ],
    W.S,
    'F3EEFF',
  );

  const ekranAkapity = [
    P([run({ text: s.podpis ?? s.tytul, bold: true, size: 19, color: '222222' })], {
      spacing: { after: 60 },
    }),
    ...(s.zrzuty.length
      ? s.zrzuty.map((z) =>
          P([run({ text: `• zrzuty/${z}`, size: 17, color: '444444' })], { spacing: { after: 30 } }),
        )
      : [P([run({ text: '• plansza generowana w Remotion (bez zrzutu)', size: 17, color: '444444' })])]),
  ];

  const mowi = komorka(
    [P([run({ text: `„${s.narracja}”`, size: 20, color: '222222' })], { spacing: { line: 264 } })],
    W.A,
  );

  const uklad = komorka(
    [
      P([run({ text: s.heygen, size: 17, color: FIOLET, bold: true })], { spacing: { after: 80 } }),
      ...s.animacja.map((a) =>
        P([run({ text: `– ${a}`, size: 16, color: '444444' })], { spacing: { after: 40 } }),
      ),
    ],
    W.U,
  );

  return new TableRow({ children: [scena, komorka(ekranAkapity, W.E), mowi, uklad] });
});

const tabela = new Table({
  width: { size: SUMA, type: WidthType.DXA },
  columnWidths: [W.S, W.E, W.A, W.U],
  rows: [
    new TableRow({
      tableHeader: true,
      children: [
        komorkaNaglowka('Scena / czas', W.S),
        komorkaNaglowka('Na ekranie (duży kadr)', W.E),
        komorkaNaglowka('Awatar mówi (wklej do HeyGen → Script)', W.A),
        komorkaNaglowka('Układ awatara i animacja', W.U),
      ],
    }),
    ...wiersze,
  ],
});

const kroki = [
  '1. Nowy projekt wideo w HeyGen, format poziomy 16:9.',
  '2. Awatar: zakładka Avatars → Photo Avatar / Avatar ze zdjęcia. HeyGen poprosi o krótkie nagranie zgody na wizerunek — to normalne i robi to Pani samodzielnie w aplikacji.',
  '3. Głos: ciepły polski głos AI (ustaw język: polski). Alternatywnie klonowanie głosu w HeyGen.',
  '4. Dla każdej sceny wgraj wskazany zrzut z katalogu zrzuty/ jako duży kadr i zmniejsz awatara do prawego dolnego rogu.',
  '5. W polu Script wklej tekst z kolumny „Awatar mówi” (albo z pliku EduPlaner2026_Narracja.docx).',
  '6. Sceny 1 i 10 (powitanie, zaproszenie): awatar duży — to spina film ciepłą klamrą.',
  '7. Delikatne przejścia i ściszona muzyka. Render MP4 1920 × 1080.',
  'Wariant w pełni animowany: zamiast wgrywać zrzuty osobno, wyrenderuj obraz filmu w Remotion (katalog remotion/), a w HeyGen dołóż tylko awatara w rogu.',
];

const dzieci = [
  P([run({ text: 'EDU', bold: true, color: FIOLET, size: 34 }), run({ text: 'PLANER 2026', bold: true, color: POMARANCZ, size: 34 })]),
  P([run({ text: `Storyboard: ${S.tytul}`, bold: true, color: FIOLET, size: 32 })], { spacing: { before: 100, after: 80 } }),
  P([run({ text: `${S.podtytul} · ${S.sceny.length} scen · prawdziwe zrzuty druków EduPlaner 2026`, italics: true, color: '444444', size: 20 })], { spacing: { after: 60 } }),
  P([run({ text: S.uwaga_o_danych, italics: true, color: POMARANCZ, size: 19 })], { spacing: { after: 200 } }),
  tabela,
  P([run({ text: 'Jak złożyć to w HeyGen — krok po kroku', bold: true, color: FIOLET, size: 26 })], {
    spacing: { before: 300, after: 120 },
    border: { bottom: { color: POMARANCZ, style: BorderStyle.SINGLE, size: 12, space: 6 } },
  }),
  ...kroki.map((k) => P([run({ text: k, size: 21, color: '222222' })], { spacing: { after: 90 } })),
  P(
    [
      run({ text: 'Kontakt na ekran końcowy: ', bold: true, size: 22, color: FIOLET }),
      run({ text: 'kontakt@eduplaner2026.pl · 662 888 403', size: 22, color: '222222' }),
    ],
    { spacing: { before: 160 } },
  ),
];

const storyboard = new Document({
  styles: { default: { document: { run: { font: FONT } } } },
  sections: [
    {
      properties: {
        page: { size: { orientation: PageOrientation.LANDSCAPE }, margin: { top: 900, bottom: 900, left: 1000, right: 1000 } },
      },
      children: dzieci,
    },
  ],
});

/* ---------- 2. NARRACJA ---------- */
const narracjaDzieci = [
  P([run({ text: 'EDU', bold: true, color: FIOLET, size: 32 }), run({ text: 'PLANER 2026', bold: true, color: POMARANCZ, size: 32 })]),
  P([run({ text: 'Tekst narracji do HeyGen / lektora', bold: true, color: FIOLET, size: 30 })], { spacing: { before: 100, after: 60 } }),
  P([run({ text: `${S.tytul} · ${S.podtytul}`, italics: true, color: '444444', size: 20 })], { spacing: { after: 60 } }),
  P([run({ text: 'Tekst jest czysty — bez znaczników pauz, bo HeyGen czyta wszystko dosłownie. Każdą scenę wklej w osobne pole Script.', italics: true, color: '444444', size: 19 })], { spacing: { after: 220 } }),
];

let slowaRazem = 0;
for (const s of S.sceny) {
  const slowa = s.narracja.split(/\s+/).length;
  slowaRazem += slowa;
  narracjaDzieci.push(
    P(
      [
        run({ text: `SCENA ${s.nr} · ${s.tytul}`, bold: true, color: FIOLET, size: 24 }),
        run({ text: `   ${mmss(s.od)}–${mmss(s.od + s.czas)} · ${s.czas} s · ${slowa} słów`, color: POMARANCZ, size: 19 }),
      ],
      { spacing: { before: 220, after: 80 } },
    ),
  );
  narracjaDzieci.push(P([run({ text: s.narracja, size: 24, color: '222222' })], { spacing: { line: 320 } }));
}
narracjaDzieci.push(
  P([run({ text: `Razem: ${slowaRazem} słów na ${S.sceny.at(-1).od + S.sceny.at(-1).czas} sekund (tempo ok. ${(slowaRazem / (S.sceny.at(-1).od + S.sceny.at(-1).czas)).toFixed(1)} słowa/s — spokojne, lektorskie).`, italics: true, color: FIOLET, size: 20 })], { spacing: { before: 300 } }),
);

const narracja = new Document({
  styles: { default: { document: { run: { font: FONT } } } },
  sections: [{ properties: { page: { margin: { top: 1200, bottom: 1200, left: 1200, right: 1200 } } }, children: narracjaDzieci }],
});

/* ---------- 3. SCENARIUSZ MD ---------- */
const md = [];
md.push(`# ${S.tytul}`, '', `**${S.podtytul}**`, '', `> ${S.uwaga_o_danych}`, '');
md.push('| Scena | Czas | Na ekranie | Narracja (słów) |', '|---|---|---|---|');
for (const s of S.sceny) {
  md.push(
    `| ${s.nr}. ${s.tytul} | ${mmss(s.od)}–${mmss(s.od + s.czas)} (${s.czas} s) | ${s.podpis ?? 'plansza'} | ${s.narracja.split(/\s+/).length} |`,
  );
}
md.push('');
for (const s of S.sceny) {
  md.push(`## ${s.nr}. ${s.tytul} — ${mmss(s.od)}–${mmss(s.od + s.czas)} (${s.czas} s)`, '');
  md.push('**Na ekranie:** ' + (s.podpis ?? 'plansza generowana w Remotion'), '');
  if (s.zrzuty.length) {
    md.push('**Prawdziwe zrzuty:**');
    s.zrzuty.forEach((z) => md.push(`- \`zrzuty/${z}\``));
    md.push('');
  }
  md.push('**Animacja:**');
  s.animacja.forEach((a) => md.push(`- ${a}`));
  md.push('');
  md.push('**Narracja (awatar / lektor):**', '', `> ${s.narracja}`, '');
  md.push(`**Układ w HeyGen:** ${s.heygen}`, '');
  if (s.lista) {
    md.push('**Lista na ekranie:**');
    s.lista.forEach((l) => md.push(`- ✔ ${l}`));
    md.push('');
  }
  if (s.plansza) {
    md.push(`**Plansza:** nadtytuł „${s.plansza.nadtytul}” · tytuł „${s.plansza.tytul.replace(/\n/g, ' / ')}” · hasło „${s.plansza.haslo}”`, '');
  }
}

/* ---------- ZAPIS ---------- */
const wyjscie = path.join(katalog, 'storyboard');
fs.mkdirSync(wyjscie, { recursive: true });
Packer.toBuffer(storyboard).then((b) => {
  fs.writeFileSync(path.join(wyjscie, 'EduPlaner2026_Storyboard_HeyGen.docx'), b);
  console.log('✓ storyboard/EduPlaner2026_Storyboard_HeyGen.docx');
});
Packer.toBuffer(narracja).then((b) => {
  fs.writeFileSync(path.join(wyjscie, 'EduPlaner2026_Narracja.docx'), b);
  console.log('✓ storyboard/EduPlaner2026_Narracja.docx');
});
fs.writeFileSync(path.join(katalog, 'SCENARIUSZ_3MIN.md'), md.join('\n'));
console.log('✓ SCENARIUSZ_3MIN.md');
