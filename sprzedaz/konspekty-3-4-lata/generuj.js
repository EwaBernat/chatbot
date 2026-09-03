/* Skład konspektów do Worda.  Treść: dane.js
   node generuj.js  →  Konspekty-Kolorowy-Swiat-Emocji-3-4-lata.docx        */

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  WidthType, AlignmentType, BorderStyle, ShadingType, ShadingType: ST,
  PageBreak, HeadingLevel, Header, Footer, PageNumber, LevelFormat,
  VerticalAlign, TabStopType,
} = require("docx");

const { BRAND, KOLORY_EMOCJI, POZIOMY, KONSPEKTY } = require("./dane.js");

const FONT = "Arial";
const SZER = 9638;              // szerokość kolumny tekstu w DXA
const BEZ_KRAWEDZI = {
  top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
  right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
};
const linia = (kolor = BRAND.linia, rozmiar = 4) => ({
  style: BorderStyle.SINGLE, size: rozmiar, color: kolor,
});

/* ── drobne cegiełki ──────────────────────────────────────────────────── */
const t = (text, o = {}) => new TextRun({
  text, font: FONT, size: o.size || 19, bold: o.bold, italics: o.italics,
  color: o.color || BRAND.atrament, allCaps: o.caps, characterSpacing: o.spacing,
});

const p = (runs, o = {}) => new Paragraph({
  children: Array.isArray(runs) ? runs : [runs],
  alignment: o.align, spacing: { before: o.przed || 0, after: o.po == null ? 90 : o.po, line: o.line || 264 },
  indent: o.wciecie ? { left: o.wciecie } : undefined,
  border: o.border,
  shading: o.tlo ? { type: ST.CLEAR, fill: o.tlo, color: "auto" } : undefined,
  keepNext: o.trzymaj,
});

const pusty = (po = 120) => new Paragraph({ children: [], spacing: { after: po } });

const nadtytul = (txt, kolor = BRAND.pomarancz) => p(
  t(txt, { size: 16, bold: true, color: kolor, caps: true, spacing: 30 }),
  { po: 60, trzymaj: true });

const h1 = (txt) => p(t(txt, { size: 34, bold: true, color: BRAND.fiolet }),
  { po: 60, trzymaj: true, przed: 0 });

const h2 = (txt, kolor = BRAND.fiolet) => p(
  t(txt, { size: 24, bold: true, color: kolor }),
  { przed: 260, po: 100, trzymaj: true });

const h3 = (txt) => p(t(txt, { size: 20, bold: true, color: BRAND.fiolet }),
  { przed: 180, po: 60, trzymaj: true });

const lead = (txt) => p(t(txt, { size: 20, color: "3D3652" }), { po: 160, line: 288 });

const kula = (txt, kolor = BRAND.pomarancz) => new Paragraph({
  children: [t("▪  ", { color: kolor, bold: true }), ...(Array.isArray(txt) ? txt : [t(txt)])],
  spacing: { after: 60, line: 264 }, indent: { left: 200, hanging: 200 },
});

const kreska = (kolor = BRAND.pomarancz) => new Paragraph({
  children: [], spacing: { after: 140 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 18, color: kolor, space: 1 } },
});

/* komórka tabeli */
const kom = (dzieci, o = {}) => new TableCell({
  width: { size: o.szer, type: WidthType.DXA },
  shading: o.tlo ? { type: ST.CLEAR, fill: o.tlo, color: "auto" } : undefined,
  margins: { top: 80, bottom: 80, left: 110, right: 110 },
  verticalAlign: o.pion || VerticalAlign.TOP,
  columnSpan: o.span,
  borders: o.borders,
  children: Array.isArray(dzieci) ? dzieci : [dzieci],
});

const naglowekKom = (txt, szer, tlo = BRAND.fiolet) => kom(
  p(t(txt, { size: 15, bold: true, color: "FFFFFF", caps: true, spacing: 20 }), { po: 0 }),
  { szer, tlo });

const tabela = (wiersze, kolumny) => new Table({
  columnWidths: kolumny,
  width: { size: SZER, type: WidthType.DXA },
  borders: {
    top: linia(), bottom: linia(), left: linia(), right: linia(),
    insideHorizontal: linia(), insideVertical: linia(),
  },
  rows: wiersze,
});

/* ── strona tytułowa ──────────────────────────────────────────────────── */
function stronaTytulowa() {
  const pasek = new Table({
    columnWidths: [1928, 1928, 1928, 1927, 1927],
    width: { size: SZER, type: WidthType.DXA },
    borders: { top: linia("FFFFFF", 1), bottom: linia("FFFFFF", 1), left: linia("FFFFFF", 1), right: linia("FFFFFF", 1), insideHorizontal: linia("FFFFFF", 1), insideVertical: linia("FFFFFF", 8) },
    rows: [new TableRow({
      children: [
        ["Radość", "F2B21A", "8A6203"], ["Smutek", "2E6FB7", "FFFFFF"],
        ["Złość", "D33B2C", "FFFFFF"], ["Wstyd", "E0619B", "FFFFFF"],
        ["Strach", "6E7681", "FFFFFF"],
      ].map(([nazwa, tlo, kol], i) => kom(
        p(t(nazwa, { size: 20, bold: true, color: kol }), { align: AlignmentType.CENTER, po: 0 }),
        { szer: i < 3 ? 1928 : 1927, tlo })),
    })],
  });

  return [
    pusty(600),
    nadtytul("Świat Kolorów · przedszkole · część 1"),
    p(t("Kolorowy Świat Emocji", { size: 60, bold: true, color: BRAND.fiolet }), { po: 20 }),
    p(t("Konspekty zajęć dla dzieci 3–4 lata", { size: 38, bold: true, color: BRAND.pomarancz }), { po: 200 }),
    kreska(),
    lead("Siedem konspektów zajęć rozwijających kompetencje emocjonalne i społeczne, z kompletem 21 celów SMART przypisanych do trzech poziomów wsparcia — gotowych do przeniesienia do IPET-u."),
    pusty(300),
    pasek,
    pusty(500),
    tabela([
      new TableRow({ children: [
        kom([p(t("W dokumencie", { size: 15, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 40 }),
             p(t("7 konspektów · 21 celów SMART", { size: 20, bold: true, color: BRAND.fiolet }), { po: 0 })],
            { szer: 3213, tlo: BRAND.tloFiolet, borders: BEZ_KRAWEDZI }),
        kom([p(t("Grupa wiekowa", { size: 15, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 40 }),
             p(t("3–4 lata · przedszkole", { size: 20, bold: true, color: BRAND.fiolet }), { po: 0 })],
            { szer: 3213, tlo: BRAND.tloFiolet, borders: BEZ_KRAWEDZI }),
        kom([p(t("Czas jednych zajęć", { size: 15, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 40 }),
             p(t("20 minut (nr 7 — 25 min)", { size: 20, bold: true, color: BRAND.fiolet }), { po: 0 })],
            { szer: 3212, tlo: BRAND.tloFiolet, borders: BEZ_KRAWEDZI }),
      ]}),
    ], [3213, 3213, 3212]),
    pusty(700),
    p(t("Autorka: Mirosława Ewa Jurczyszyn, pedagog specjalny", { size: 19, bold: true }), { po: 40 }),
    p(t("Pomorskie Centrum Terapii Pedagogicznej, Koszalin · EduPlaner 2026", { size: 18, color: BRAND.szept }), { po: 40 }),
    p(t("kontakt@eduplaner2026.pl · [ telefon ] · www.eduplaner2026.pl", { size: 18, color: BRAND.szept }), { po: 0 }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

/* ── I. Jak korzystać ─────────────────────────────────────────────────── */
function jakKorzystac() {
  const zasady = [
    ["Dwadzieścia minut, nie więcej", "Trzylatek utrzymuje uwagę w zorganizowanej aktywności około 15–20 minut. Konspekty są napisane na ten czas i nie warto ich wydłużać — lepiej powtórzyć zajęcia w kolejnym tygodniu."],
    ["Jeden kolor na tydzień", "Cały cykl to 12 tygodni: tydzień wprowadzający, po dwa tygodnie na każdy kolor i tydzień podsumowujący. Emocja potrzebuje powtórzeń, nie tempa."],
    ["Ta sama kolejność za każdym razem", "Każdy konspekt ma pięć etapów w stałym porządku: rytuał powitania, wprowadzenie, część główna, ruch, domknięcie. Przewidywalność jest tu narzędziem terapeutycznym."],
    ["Miś Kolorek zamiast Rajmunda", "W wersji dla nastolatka bohaterem jest siedemnastoletni Rajmund. Dla trzylatka jego rolę przejmuje Miś Kolorek, który zmienia chustkę razem z emocją."],
    ["Kolor jest odpowiedzią", "Podanie karty w kolorze jest pełnoprawną odpowiedzią. Dziecko, które jeszcze nie mówi albo nie chce mówić, uczestniczy w zajęciach tak samo jak pozostałe."],
    ["Nie ma dobrych i złych odpowiedzi", "Nie poprawiamy nazwy emocji, nie porównujemy dzieci, nie wymagamy dokończenia zadania. Zasada „pas” obowiązuje na każdych zajęciach."],
  ];

  return [
    nadtytul("Część I"),
    h1("Jak korzystać z konspektów"),
    kreska(),
    lead("Sześć zasad, na których stoi cały cykl. Każdy konspekt jest napisany tak, żeby dało się go poprowadzić bez wcześniejszego przygotowania — wystarczy przeczytać przebieg zajęć i przygotować środki dydaktyczne."),
    ...zasady.flatMap(([tytul, opis]) => [
      p([t(tytul + " — ", { bold: true, color: BRAND.fiolet }), t(opis)], { po: 130, line: 276 }),
    ]),
    h2("Ramowy plan cyklu"),
    tabela([
      new TableRow({ tableHeader: true, children: [
        naglowekKom("Tydzień", 1400), naglowekKom("Konspekt", 3400),
        naglowekKom("Kolor i emocja", 2400), naglowekKom("Co domykamy", 2438),
      ]}),
      ...[
        ["1", "Konspekt 1 — Pięć kolorów", "wszystkie pięć", "wspólny kod grupy"],
        ["2–3", "Konspekt 2 — Żółty dzień", "żółty · radość", "rozpoznawanie radości"],
        ["4–5", "Konspekt 3 — Niebieski Miś", "niebieski · smutek", "proszenie o wsparcie"],
        ["6–7", "Konspekt 4 — Czerwony Miś", "czerwony · złość", "sygnał STOP i oddech"],
        ["8–9", "Konspekt 5 — Różowy Miś", "różowy · wstyd", "bezpieczeństwo po pomyłce"],
        ["10–11", "Konspekt 6 — Szary Miś", "szary · strach", "plan obrazkowy"],
        ["12", "Konspekt 7 — Paleta i gra", "wszystkie pięć", "ewaluacja celów SMART"],
      ].map(([tydz, konsp, kol, dom], i) => new TableRow({ children: [
        kom(p(t(tydz, { bold: true, size: 18, color: BRAND.pomarancz }), { po: 0 }), { szer: 1400, tlo: i % 2 ? BRAND.tloFiolet : undefined }),
        kom(p(t(konsp, { size: 18 }), { po: 0 }), { szer: 3400, tlo: i % 2 ? BRAND.tloFiolet : undefined }),
        kom(p(t(kol, { size: 18 }), { po: 0 }), { szer: 2400, tlo: i % 2 ? BRAND.tloFiolet : undefined }),
        kom(p(t(dom, { size: 18 }), { po: 0 }), { szer: 2438, tlo: i % 2 ? BRAND.tloFiolet : undefined }),
      ]})),
    ], [1400, 3400, 2400, 2438]),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

/* ── II. Poziomy wsparcia ─────────────────────────────────────────────── */
function poziomyWsparcia() {
  const bloki = POZIOMY.flatMap((poz) => [
    h2(poz.nazwa),
    p(t(poz.kto, { size: 19, color: "3D3652" }), { po: 100, line: 276 }),
    p(t("Formy realizacji", { size: 15, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 60 }),
    ...poz.formy.map((f) => kula(t(f, { size: 18 }))),
    p([t("Podstawa prawna:  ", { size: 16, bold: true, color: BRAND.bezowy, caps: true, spacing: 20 }),
       t(poz.podstawa, { size: 16, color: BRAND.szept })],
      { po: 200, tlo: BRAND.tloFiolet, wciecie: 0 }),
  ]);

  return [
    nadtytul("Część II"),
    h1("Trzy poziomy wsparcia"),
    kreska(),
    lead("Ten sam konspekt realizuje troje dzieci o różnych potrzebach — i każde z nich ma inny cel. Poziom wsparcia nie zmienia tematu zajęć; zmienia kryterium osiągnięcia i ilość podpowiedzi wpisaną w cel."),
    p([t("Zasada zapisu: ", { bold: true, color: BRAND.fiolet }),
       t("im wyższy poziom wsparcia, tym więcej podpowiedzi w treści celu i niższe kryterium samodzielności. Cel na poziomie III nie jest „gorszy” — jest realny dla dziecka, które potrzebuje dorosłego obok.")],
      { po: 200, line: 276 }),
    ...bloki,
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

/* ── III. Zbiorcza tabela celów SMART ─────────────────────────────────── */
function zbiorczaSmart() {
  const wiersze = [
    new TableRow({ tableHeader: true, children: [
      naglowekKom("Nr", 620), naglowekKom("Poz.", 620), naglowekKom("KSzOF · ICF", 1700),
      naglowekKom("Cel SMART", 4600), naglowekKom("Kryterium", 2098),
    ]}),
  ];
  KONSPEKTY.forEach((k) => {
    k.smart.forEach((s, i) => {
      const tlo = k.nr % 2 ? undefined : BRAND.tloFiolet;
      wiersze.push(new TableRow({ children: [
        kom(i === 0 ? p(t(String(k.nr), { bold: true, size: 18, color: BRAND.pomarancz }), { po: 0 }) : p(t(""), { po: 0 }), { szer: 620, tlo }),
        kom(p(t(s.poziom, { bold: true, size: 18, color: BRAND.fiolet }), { po: 0 }), { szer: 620, tlo }),
        kom([p(t(`KSzOF ${s.kszof}`, { size: 15, bold: true, color: BRAND.szept }), { po: 20 }),
             p(t(s.icf, { size: 15, color: BRAND.bezowy }), { po: 0 })], { szer: 1700, tlo }),
        kom(p(t(s.cel, { size: 16 }), { po: 0, line: 240 }), { szer: 4600, tlo }),
        kom(p(t(s.kryterium, { size: 15, color: BRAND.zielony }), { po: 0, line: 240 }), { szer: 2098, tlo }),
      ]}));
    });
  });

  return [
    nadtytul("Część III"),
    h1("Wszystkie 21 celów SMART"),
    kreska(),
    lead("Komplet celów z siedmiu konspektów, w układzie do przeniesienia wprost do sekcji III IPET-u (cele edukacyjno-terapeutyczne KSzOF + ICF). Pełne brzmienie każdego celu wraz z formą realizacji i podstawą prawną znajduje się przy odpowiednim konspekcie."),
    tabela(wiersze, [620, 620, 1700, 4600, 2098]),
    pusty(160),
    p([t("Jak to przenieść do IPET-u:  ", { bold: true, size: 17, color: BRAND.fiolet }),
       t("wybierz cele z poziomu, na który dziecko zostało zakwalifikowane w sekcji II. Kolumna „KSzOF · ICF” odpowiada polom obszaru i kodu w tabeli celów. Kryterium wpisz do kolumny ewaluacji.", { size: 17 })],
      { tlo: BRAND.tloPomarancz, po: 0, line: 264 }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

/* ── IV. Pojedynczy konspekt ──────────────────────────────────────────── */
function konspekt(k) {
  const kol = KOLORY_EMOCJI[k.kolor];

  const metryczka = tabela([
    new TableRow({ children: [
      kom([p(t("Grupa wiekowa", { size: 14, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 20 }),
           p(t("3–4 lata", { size: 18, bold: true }), { po: 0 })], { szer: 2410, tlo: BRAND.tloFiolet }),
      kom([p(t("Czas", { size: 14, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 20 }),
           p(t(k.czas, { size: 18, bold: true }), { po: 0 })], { szer: 2410, tlo: BRAND.tloFiolet }),
      kom([p(t("Kolor przewodni", { size: 14, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 20 }),
           p(t(kol.nazwa, { size: 18, bold: true, color: kol.hex }), { po: 0 })], { szer: 2410, tlo: BRAND.tloFiolet }),
      kom([p(t("Data / grupa", { size: 14, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 20 }),
           p(t("......................................", { size: 18, color: BRAND.szept }), { po: 0 })], { szer: 2408, tlo: BRAND.tloFiolet }),
    ]}),
  ], [2410, 2410, 2410, 2408]);

  const tabelaSmart = tabela([
    new TableRow({ tableHeader: true, children: [
      naglowekKom("Poziom", 900), naglowekKom("Obszar KSzOF · ICF", 1900),
      naglowekKom("Cel SMART", 3900), naglowekKom("Forma realizacji i kryterium", 2938),
    ]}),
    ...k.smart.map((s) => new TableRow({ children: [
      kom([p(t(s.poziom, { size: 26, bold: true, color: BRAND.pomarancz }), { po: 10, align: AlignmentType.CENTER }),
           p(t("poziom", { size: 13, color: BRAND.szept, caps: true }), { po: 0, align: AlignmentType.CENTER })],
          { szer: 900, tlo: BRAND.tloPomarancz }),
      kom([p(t(s.obszar, { size: 16, bold: true, color: BRAND.fiolet }), { po: 30, line: 232 }),
           p(t(`KSzOF ${s.kszof}`, { size: 15, color: BRAND.szept }), { po: 20 }),
           p(t("ICF " + s.icf, { size: 15, color: BRAND.bezowy }), { po: 0 })], { szer: 1900 }),
      kom(p(t(s.cel, { size: 17 }), { po: 0, line: 248 }), { szer: 3900 }),
      kom([p(t(s.forma, { size: 15 }), { po: 50, line: 232 }),
           p([t("Kryterium: ", { size: 15, bold: true, color: BRAND.zielony }), t(s.kryterium, { size: 15, color: BRAND.zielony })], { po: 40, line: 232 }),
           p(t(s.podstawa, { size: 14, color: BRAND.bezowy }), { po: 0 })], { szer: 2938 }),
    ]})),
  ], [900, 1900, 3900, 2938]);

  const tabelaPrzebiegu = tabela([
    new TableRow({ tableHeader: true, children: [
      naglowekKom("Czas", 900), naglowekKom("Etap", 2100),
      naglowekKom("Czynności nauczyciela", 3400), naglowekKom("Czynności dziecka", 3238),
    ]}),
    ...k.przebieg.map((e, i) => new TableRow({ children: [
      kom(p(t(e.czas, { size: 16, bold: true, color: BRAND.pomarancz }), { po: 0 }), { szer: 900, tlo: i % 2 ? BRAND.tloFiolet : undefined }),
      kom(p(t(e.etap, { size: 16, bold: true, color: BRAND.fiolet }), { po: 0, line: 232 }), { szer: 2100, tlo: i % 2 ? BRAND.tloFiolet : undefined }),
      kom(p(t(e.n, { size: 16 }), { po: 0, line: 240 }), { szer: 3400, tlo: i % 2 ? BRAND.tloFiolet : undefined }),
      kom(p(t(e.d, { size: 16 }), { po: 0, line: 240 }), { szer: 3238, tlo: i % 2 ? BRAND.tloFiolet : undefined }),
    ]})),
  ], [900, 2100, 3400, 3238]);

  const dwieKolumny = (lewyTyt, lewe, prawyTyt, prawe) => tabela([
    new TableRow({ children: [
      kom([p(t(lewyTyt, { size: 15, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 60 }),
           ...lewe.map((x) => kula(t(x, { size: 17 })))], { szer: 4819, borders: BEZ_KRAWEDZI }),
      kom([p(t(prawyTyt, { size: 15, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 60 }),
           ...prawe.map((x) => kula(t(x, { size: 17 })))], { szer: 4819, borders: BEZ_KRAWEDZI }),
    ]}),
  ], [4819, 4819]);

  return [
    nadtytul(`Konspekt ${k.nr} · ${k.podtytul}`, kol.hex === "2D1B69" ? BRAND.pomarancz : kol.hex),
    h1(k.temat),
    kreska(kol.hex),
    metryczka,
    pusty(180),

    h2("Cel ogólny"),
    p(t(k.celOgolny, { size: 19, color: "3D3652" }), { po: 140, line: 276 }),

    h2("Cele operacyjne"),
    p(t("Dziecko:", { size: 17, bold: true, color: BRAND.szept }), { po: 60 }),
    ...k.celeOperacyjne.map((c) => kula(t(c, { size: 18 }), kol.hex)),

    h2("Cele SMART według poziomu wsparcia"),
    tabelaSmart,
    pusty(180),

    h2("Metody, formy i środki"),
    dwieKolumny("Metody pracy", k.metody, "Formy pracy", k.formy),
    pusty(120),
    p(t("Środki dydaktyczne", { size: 15, bold: true, color: BRAND.szept, caps: true, spacing: 20 }), { po: 60 }),
    ...k.srodki.map((s) => kula(t(s, { size: 17 }), kol.hex)),

    h2("Przebieg zajęć"),
    tabelaPrzebiegu,
    pusty(180),

    h2("Dostosowania dla dzieci z różnymi potrzebami"),
    ...k.dostosowania.map((d) => {
      const [grupa, ...reszta] = d.split(" — ");
      return kula([t(grupa + " — ", { size: 17, bold: true, color: BRAND.fiolet }), t(reszta.join(" — "), { size: 17 })], kol.hex);
    }),

    h2("Ewaluacja zajęć — pytania dla prowadzącego"),
    ...k.ewaluacja.map((e) => kula(t(e, { size: 17 }), BRAND.zielony)),

    h2("Podstawa programowa wychowania przedszkolnego"),
    ...k.podstawaProgramowa.map((x) => kula(t(x, { size: 16, color: BRAND.szept }), BRAND.bezowy)),

    pusty(140),
    tabela([
      new TableRow({ children: [
        kom([p(t("Notatka dla prowadzącego", { size: 15, bold: true, color: BRAND.pomarancz, caps: true, spacing: 20 }), { po: 60 }),
             p(t(k.notatka, { size: 18 }), { po: 0, line: 264 })],
            { szer: SZER, tlo: BRAND.tloPomarancz, borders: BEZ_KRAWEDZI }),
      ]}),
    ], [SZER]),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

/* ── V. Karta obserwacji ──────────────────────────────────────────────── */
function kartaObserwacji() {
  const kropki = (n = 46) => "." .repeat(n);
  const wiersze = [
    new TableRow({ tableHeader: true, children: [
      naglowekKom("Konspekt", 1500), naglowekKom("Poziom", 900), naglowekKom("Cel SMART — skrót", 3600),
      naglowekKom("Data", 1100), naglowekKom("Wynik (np. 4/5)", 1300), naglowekKom("Uwagi", 1238),
    ]}),
  ];
  KONSPEKTY.forEach((k) => {
    k.smart.forEach((s, i) => {
      const skrot = s.cel.split(" ").slice(0, 14).join(" ") + "…";
      const tlo = k.nr % 2 ? undefined : BRAND.tloFiolet;
      wiersze.push(new TableRow({ children: [
        kom(i === 0 ? p(t(`${k.nr}. ${k.podtytul.split(" · ")[0]}`, { size: 15, bold: true, color: BRAND.fiolet }), { po: 0, line: 232 }) : p(t(""), { po: 0 }), { szer: 1500, tlo }),
        kom(p(t(s.poziom, { size: 16, bold: true, color: BRAND.pomarancz }), { po: 0, align: AlignmentType.CENTER }), { szer: 900, tlo }),
        kom(p(t(skrot, { size: 14 }), { po: 0, line: 224 }), { szer: 3600, tlo }),
        kom(p(t("", { size: 15 }), { po: 0 }), { szer: 1100, tlo }),
        kom(p(t("", { size: 15 }), { po: 0 }), { szer: 1300, tlo }),
        kom(p(t("", { size: 15 }), { po: 0 }), { szer: 1238, tlo }),
      ]}));
    });
  });

  return [
    nadtytul("Część V"),
    h1("Karta obserwacji i ewaluacji celów"),
    kreska(),
    lead("Do wydruku dla każdego dziecka objętego IPET-em. Wypełnia się na bieżąco, po zajęciach. Wypełniona karta jest gotowym załącznikiem do oceny efektywności programu (sekcja VIII IPET-u)."),
    p([t("Imię i nazwisko dziecka: ", { bold: true, size: 18 }), t(kropki(40), { color: BRAND.szept })], { po: 80 }),
    p([t("Grupa: ", { bold: true, size: 18 }), t(kropki(18), { color: BRAND.szept }),
       t("     Poziom wsparcia wg IPET: ", { bold: true, size: 18 }), t("  I  /  II  /  III  ", { bold: true, size: 18, color: BRAND.pomarancz })], { po: 80 }),
    p([t("Okres obserwacji: ", { bold: true, size: 18 }), t(kropki(34), { color: BRAND.szept })], { po: 200 }),
    tabela(wiersze, [1500, 900, 3600, 1100, 1300, 1238]),
    pusty(200),
    p([t("Wniosek do ewaluacji IPET: ", { bold: true, size: 18, color: BRAND.fiolet })], { po: 60 }),
    ...[1, 2, 3].map(() => p(t(kropki(96), { color: BRAND.linia }), { po: 120 })),
    pusty(160),
    p([t("Podpis prowadzącego: ", { size: 17 }), t(kropki(30), { color: BRAND.szept }),
       t("      Data: ", { size: 17 }), t(kropki(18), { color: BRAND.szept })], { po: 0 }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

/* ── VI. Podstawa prawna ──────────────────────────────────────────────── */
function podstawaPrawna() {
  const akty = [
    ["Podstawa programowa wychowania przedszkolnego", "Rozporządzenie Ministra Edukacji Narodowej z dnia 14 lutego 2017 r. w sprawie podstawy programowej wychowania przedszkolnego oraz kształcenia ogólnego — załącznik nr 1. Numeracja obszarów i punktów przywoływana w konspektach pochodzi z tego załącznika."],
    ["Kształcenie specjalne i poziomy wsparcia", "Rozporządzenie Ministra Edukacji Narodowej w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym — § 6 i § 7 (formy wsparcia, IPET, zajęcia rewalidacyjne)."],
    ["Pomoc psychologiczno-pedagogiczna", "Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej w publicznych przedszkolach, szkołach i placówkach — § 6 (formy pomocy, zajęcia specjalistyczne)."],
    ["Klasyfikacja funkcjonowania", "Międzynarodowa Klasyfikacja Funkcjonowania, Niepełnosprawności i Zdrowia (ICF, WHO) — kody d i b przywoływane przy celach. Obszary KSzOF 1–9 zgodnie ze standardem oceny funkcjonalnej stosowanym w ekosystemie EduPlaner 2026."],
  ];
  return [
    nadtytul("Część VI"),
    h1("Podstawa prawna i źródła"),
    kreska(),
    ...akty.flatMap(([tyt, tresc]) => [
      h3(tyt),
      p(t(tresc, { size: 17, color: "3D3652" }), { po: 120, line: 264 }),
    ]),
    pusty(200),
    tabela([
      new TableRow({ children: [
        kom([p(t("Zastrzeżenie", { size: 15, bold: true, color: BRAND.czerwony, caps: true, spacing: 20 }), { po: 60 }),
             p(t("Konspekty są materiałem edukacyjnym i metodycznym. Cele SMART wymagają dostosowania do konkretnego dziecka na podstawie wielospecjalistycznej oceny poziomu funkcjonowania (WOPF). Materiał nie zastępuje diagnozy ani terapii prowadzonej przez specjalistę.", { size: 17 }), { po: 0, line: 264 })],
            { szer: SZER, tlo: BRAND.tloPomarancz, borders: BEZ_KRAWEDZI }),
      ]}),
    ], [SZER]),
    pusty(400),
    p(t("Mirosława Ewa Jurczyszyn · Pomorskie Centrum Terapii Pedagogicznej, Koszalin · EduPlaner 2026", { size: 16, color: BRAND.szept }), { align: AlignmentType.CENTER, po: 0 }),
  ];
}

/* ── dokument ─────────────────────────────────────────────────────────── */
const doc = new Document({
  creator: "Mirosława Ewa Jurczyszyn",
  title: "Kolorowy Świat Emocji — konspekty dla dzieci 3–4 lata",
  description: "Siedem konspektów zajęć z 21 celami SMART dla trzech poziomów wsparcia. PCTP Koszalin.",
  styles: { default: { document: { run: { font: FONT, size: 19, color: BRAND.atrament } } } },
  sections: [{
    properties: { page: { margin: { top: 1134, right: 1134, bottom: 1021, left: 1134 } } },
    headers: { default: new Header({ children: [
      p([t("KOLOROWY ŚWIAT EMOCJI · KONSPEKTY 3–4 LATA", { size: 14, bold: true, color: BRAND.fiolet, spacing: 30 }),
         t("\t\tPCTP KOSZALIN", { size: 14, bold: true, color: BRAND.szept, spacing: 30 })],
        { po: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: BRAND.linia, space: 4 } } }),
    ]})},
    footers: { default: new Footer({ children: [
      new Paragraph({
        alignment: AlignmentType.RIGHT, spacing: { before: 60 },
        border: { top: { style: BorderStyle.SINGLE, size: 6, color: BRAND.linia, space: 6 } },
        children: [new TextRun({ text: "", font: FONT, size: 15 }),
                   new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 17, bold: true, color: BRAND.fiolet })],
      }),
    ]})},
    children: [
      ...stronaTytulowa(),
      ...jakKorzystac(),
      ...poziomyWsparcia(),
      ...zbiorczaSmart(),
      ...KONSPEKTY.flatMap(konspekt),
      ...kartaObserwacji(),
      ...podstawaPrawna(),
    ],
  }],
});

const wyjscie = path.join(__dirname, "Konspekty-Kolorowy-Swiat-Emocji-3-4-lata.docx");
Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(wyjscie, buf);
  console.log("Zapisano:", path.basename(wyjscie), (buf.length / 1024).toFixed(0) + " KB");
  console.log("Konspektów:", KONSPEKTY.length, "· celów SMART:", KONSPEKTY.reduce((a, k) => a + k.smart.length, 0));
});
