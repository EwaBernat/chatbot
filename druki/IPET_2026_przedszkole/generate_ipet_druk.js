/* ============================================================================
 * generate_ipet_druk.js
 * DRUK — Indywidualny Program Edukacyjno-Terapeutyczny (IPET 2026 · WOPF/ICF)
 * Wersja przedszkolna · 21 stron A4 · pusty formularz do wypełniania
 * Ekosystem EduPlaner2026-MJ-PCTP · Pomorskie Centrum Terapii Pedagogicznej
 * ----------------------------------------------------------------------------
 * Użycie:  node generate_ipet_druk.js [plik_wyjsciowy.docx]
 * ========================================================================== */

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Footer, AlignmentType, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageNumber, PageBreak, TabStopType, TabStopPosition,
} = require("docx");

const OUT_PATH = process.argv[2]
  ? path.resolve(process.argv[2])
  : path.resolve(process.cwd(), "IPET_2026_druk_przedszkole.docx");

/* ---- marka PCTP ------------------------------------------------------- */
const BRAND = {
  purple:  "2D1B69",
  orange:  "E8450A",
  green:   "0D7D5C",
  red:     "B8350D",
  teal:    "2B6E6E",
  amber:   "C47A10",
  ink:     "1A1A2E",
  mute:    "5B5B72",
  paperLt: "F4F2FA",
  paperOr: "FDF1EC",
  line:    "D9D5E8",
  white:   "FFFFFF",
};

/* ---- wymiary A4 ------------------------------------------------------- */
const PAGE_W = 11906, PAGE_H = 16838;
const MAR = { top: 780, right: 780, bottom: 700, left: 780 };
const CW = PAGE_W - MAR.left - MAR.right;   // 10346 DXA

const F = "Arial";
const BOX = "□";   // □ pole wyboru

/* ---- typografia ------------------------------------------------------- */
function r(text, o = {}) {
  return new TextRun({
    text: String(text), font: F, size: o.size || 18,
    bold: !!o.bold, italics: !!o.italics, color: o.color || BRAND.ink,
    allCaps: !!o.caps, characterSpacing: o.cs,
  });
}
function p(text, o = {}) {
  return new Paragraph({
    alignment: o.align || AlignmentType.LEFT,
    spacing: { before: o.before ?? 0, after: o.after ?? 70, line: o.line || 250 },
    indent: o.indent ? { left: o.indent } : undefined,
    children: Array.isArray(text) ? text : [r(text, o)],
  });
}
const spacer = (h = 80) => new Paragraph({ spacing: { after: h }, children: [] });

/* ---- obramowania ------------------------------------------------------ */
const thin = { style: BorderStyle.SINGLE, size: 2, color: BRAND.line };
const allThin = { top: thin, bottom: thin, left: thin, right: thin };
const noB = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const noBorders = { top: noB, bottom: noB, left: noB, right: noB,
  insideHorizontal: noB, insideVertical: noB };

/* ---- komórki i tabele ------------------------------------------------- */
function cellPara(text, o = {}) {
  return new Paragraph({
    alignment: o.align || AlignmentType.LEFT,
    spacing: { after: o.after ?? 0, before: o.before ?? 0, line: o.line || 240 },
    children: Array.isArray(text) ? text
      : [r(text, { size: o.size || 16, bold: o.bold, italics: o.italics,
                   color: o.color, cs: o.cs })],
  });
}
function td(content, w, o = {}) {
  const kids = Array.isArray(content) && content[0] instanceof Paragraph
    ? content : [cellPara(content, o)];
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    columnSpan: o.span,
    rowSpan: o.rowSpan,
    borders: o.borders || allThin,
    verticalAlign: o.valign || VerticalAlign.CENTER,
    shading: { fill: o.fill || BRAND.white, type: ShadingType.CLEAR, color: "auto" },
    margins: o.margins || { top: 60, bottom: 60, left: 100, right: 100 },
    children: kids,
  });
}
function th(text, w, o = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    columnSpan: o.span,
    borders: allThin,
    verticalAlign: VerticalAlign.CENTER,
    shading: { fill: o.fill || BRAND.purple, type: ShadingType.CLEAR, color: "auto" },
    margins: { top: 66, bottom: 66, left: 100, right: 100 },
    children: [new Paragraph({
      alignment: o.align || AlignmentType.LEFT,
      spacing: { line: 240 },
      children: [r(text, { size: o.size || 14, bold: true, color: BRAND.white, cs: 6 })] })],
  });
}
function table(colW, rows, o = {}) {
  return new Table({
    width: { size: colW.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: colW,
    borders: o.borders,
    rows,
  });
}

/* ---- pasek nagłówka strony (marka + tytuł + zakładka) ----------------- */
function pageBand(title, tag) {
  const wL = Math.round(CW * 0.66), wR = CW - wL;
  return table([wL, wR], [
    new TableRow({ children: [
      new TableCell({
        width: { size: wL, type: WidthType.DXA },
        borders: { top: noB, left: noB, bottom: noB, right: noB },
        shading: { fill: BRAND.purple, type: ShadingType.CLEAR, color: "auto" },
        margins: { top: 90, bottom: 90, left: 160, right: 100 },
        verticalAlign: VerticalAlign.CENTER,
        children: [
          new Paragraph({ spacing: { after: 20, line: 220 }, children: [
            r("PCTP", { size: 14, bold: true, color: BRAND.orange, cs: 20 }),
            r("   EduPlaner 2026", { size: 14, bold: true, color: BRAND.white, cs: 14 }),
          ] }),
          new Paragraph({ spacing: { line: 240 }, children: [
            r(title, { size: 19, bold: true, color: BRAND.white, cs: 4 }) ] }),
        ],
      }),
      new TableCell({
        width: { size: wR, type: WidthType.DXA },
        borders: { top: noB, left: noB, bottom: noB, right: noB },
        shading: { fill: BRAND.orange, type: ShadingType.CLEAR, color: "auto" },
        margins: { top: 90, bottom: 90, left: 120, right: 160 },
        verticalAlign: VerticalAlign.CENTER,
        children: [
          new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 20, line: 220 },
            children: [r(tag, { size: 16, bold: true, color: BRAND.white, cs: 6 })] }),
          new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { line: 220 },
            children: [r("IPET 2026 · WOPF", { size: 12, color: BRAND.white, cs: 8 })] }),
        ],
      }),
    ] }),
  ]);
}

/* ---- pasek identyfikacyjny dziecka ------------------------------------ */
function childStrip() {
  const w = [1500, 3200, 900, 2100, 800, CW - 1500 - 3200 - 900 - 2100 - 800];
  const lbl = (t) => cellPara(t, { size: 12, bold: true, color: BRAND.mute, cs: 8 });
  const fld = () => cellPara("", { size: 16 });
  const mk = (t, i) => new TableCell({
    width: { size: w[i], type: WidthType.DXA },
    borders: { top: noB, left: noB, right: noB,
      bottom: { style: BorderStyle.SINGLE, size: 4,
        color: (i % 2 === 1) ? BRAND.line : "FFFFFF" } },
    margins: { top: 70, bottom: 40, left: 40, right: 60 },
    verticalAlign: VerticalAlign.BOTTOM,
    children: [t === null ? fld() : lbl(t)],
  });
  return table(w, [ new TableRow({ children: [
    mk("DOTYCZY DZIECKA", 0), mk(null, 1),
    mk("GRUPA", 2), mk(null, 3),
    mk("DATA", 4), mk(null, 5),
  ] }) ], { borders: noBorders });
}

/* ---- tytuły i etykiety ------------------------------------------------ */
function partTitle(text) {
  return new Paragraph({
    spacing: { before: 200, after: 90 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 10, color: BRAND.orange, space: 4 } },
    children: [r(text, { size: 17, bold: true, color: BRAND.purple, cs: 14 })],
  });
}
function numHead(num, text, color) {
  return new Paragraph({
    spacing: { before: 180, after: 90 },
    children: [
      r(String(num) + "  ", { size: 19, bold: true, color: color || BRAND.orange }),
      r(text, { size: 17, bold: true, color: BRAND.purple, cs: 4 }),
    ],
  });
}
function label(text, o = {}) {
  return new Paragraph({
    spacing: { before: o.before ?? 130, after: o.after ?? 60 },
    children: [r(text, { size: 12, bold: true, color: o.color || BRAND.purple, cs: 10 })],
  });
}
function note(text) {
  return p([r(text, { size: 13, italics: true, color: BRAND.mute })], { after: 90, line: 230 });
}
function legal(head, text) {
  return new Table({
    width: { size: CW, type: WidthType.DXA }, columnWidths: [CW],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: CW, type: WidthType.DXA },
      borders: { top: noB, bottom: noB, right: noB,
        left: { style: BorderStyle.SINGLE, size: 16, color: BRAND.amber } },
      shading: { fill: "FDF8EE", type: ShadingType.CLEAR, color: "auto" },
      margins: { top: 90, bottom: 90, left: 160, right: 140 },
      children: [ new Paragraph({ spacing: { line: 220 }, children: [
        r("§ " + head + " ", { size: 12, bold: true, color: BRAND.amber }),
        r(text, { size: 12, italics: true, color: BRAND.mute }),
      ] }) ],
    })] })],
  });
}

/* ---- puste pole do wpisania (ramka z liniami) ------------------------- */
function fillBox(lines = 2, o = {}) {
  const kids = [];
  for (let i = 0; i < lines; i++) {
    kids.push(new Paragraph({
      spacing: { before: o.gap ?? 150, after: 0, line: 240 },
      border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: BRAND.line, space: 2 } },
      children: [r("", { size: 16 })] }));
    // separator bez krawędzi — zapobiega scaleniu sąsiednich linii przez Word
    kids.push(new Paragraph({ spacing: { before: 0, after: 0, line: 20 },
      children: [r("", { size: 2 })] }));
  }
  return new Table({
    width: { size: o.width || CW, type: WidthType.DXA },
    columnWidths: [o.width || CW],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: o.width || CW, type: WidthType.DXA },
      borders: allThin,
      shading: { fill: o.fill || BRAND.white, type: ShadingType.CLEAR, color: "auto" },
      margins: { top: 40, bottom: 60, left: 120, right: 120 },
      children: kids,
    })] })],
  });
}

/* ---- puste linie do pisania (wewnątrz komórki) ------------------------ */
function blankLines(n, o = {}) {
  const kids = [];
  for (let i = 0; i < n; i++) {
    kids.push(new Paragraph({
      spacing: { before: i === 0 ? 0 : (o.gap ?? 140), after: 0, line: 240 },
      border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: BRAND.line, space: 2 } },
      children: [r("", { size: o.size || 15 })] }));
    if (i < n - 1) kids.push(new Paragraph({ spacing: { before: 0, after: 0, line: 20 },
      children: [r("", { size: 2 })] }));
  }
  return kids;
}

/* ---- pole etykieta + miejsce na wpis (siatka danych) ------------------ */
function fieldCell(labelText, w, o = {}) {
  return new TableCell({
    width: { size: w, type: WidthType.DXA },
    columnSpan: o.span,
    borders: allThin,
    verticalAlign: VerticalAlign.TOP,
    shading: { fill: BRAND.white, type: ShadingType.CLEAR, color: "auto" },
    margins: { top: 70, bottom: 90, left: 110, right: 110 },
    children: [
      new Paragraph({ spacing: { after: 40, line: 220 },
        children: [r(labelText, { size: 11, bold: true, color: BRAND.mute, cs: 8 })] }),
      new Paragraph({ spacing: { after: o.pad ?? 60, line: 240 },
        border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: BRAND.line, space: 2 } },
        children: [r("", { size: 16 })] }),
    ],
  });
}

/* ---- siatka pól wyboru (□ etykieta) ----------------------------------- */
function checkGrid(items, cols = 2, o = {}) {
  const w = [];
  for (let i = 0; i < cols; i++) w.push(Math.floor((o.width || CW) / cols));
  const rows = [];
  for (let i = 0; i < items.length; i += cols) {
    const cells = [];
    for (let c = 0; c < cols; c++) {
      const it = items[i + c];
      cells.push(new TableCell({
        width: { size: w[c], type: WidthType.DXA },
        borders: noBorders,
        verticalAlign: VerticalAlign.TOP,
        margins: { top: 26, bottom: 26, left: 30, right: 90 },
        children: [ new Paragraph({ spacing: { line: 230 }, children:
          (it === undefined || it === "") ? [r("", { size: o.size || 15 })] : [
            r(BOX + "  ", { size: o.size ? o.size + 2 : 18, color: BRAND.orange, bold: true }),
            r(it, { size: o.size || 15, color: BRAND.ink }),
          ] }) ],
      }));
    }
    rows.push(new TableRow({ children: cells }));
  }
  return table(w, rows, { borders: noBorders });
}

/* ---- karta z tytułem i zawartością (jasne tło) ------------------------ */
function panel(children, o = {}) {
  return new Table({
    width: { size: o.width || CW, type: WidthType.DXA },
    columnWidths: [o.width || CW],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: o.width || CW, type: WidthType.DXA },
      borders: o.edge === false ? allThin : { top: noB, bottom: noB, right: noB,
        left: { style: BorderStyle.SINGLE, size: 18, color: o.edgeColor || BRAND.orange } },
      shading: { fill: o.fill || BRAND.paperLt, type: ShadingType.CLEAR, color: "auto" },
      margins: o.pad === "tight"
        ? { top: 70, bottom: 70, left: 170, right: 150 }
        : { top: 100, bottom: 100, left: 170, right: 150 },
      children: children,
    })] })],
  });
}

/* ---- panel z tytułem w środku (kompaktowy) ---------------------------- */
function panelTitled(title, text, o = {}) {
  return panel([
    new Paragraph({ spacing: { after: 50, line: 220 },
      children: [r(title, { size: 11, bold: true, color: o.titleColor || BRAND.purple, cs: 10 })] }),
    new Paragraph({ spacing: { after: 0, line: 230 },
      children: [r(text, { size: 14, color: BRAND.ink })] }),
  ], { fill: o.fill, edgeColor: o.edgeColor, pad: "tight" });
}

const brk = () => new Paragraph({ children: [new PageBreak()] });

/* ---- szkielet strony -------------------------------------------------- */
function page(title, tag, children, last) {
  const out = [pageBand(title, tag), childStrip(), spacer(40), ...children];
  if (!last) out.push(brk());
  return out;
}

/* ============================================================================
 * STRONA 1 — CZĘŚĆ WSTĘPNA · DANE OSOBY UCZĄCEJ SIĘ
 * ========================================================================== */
function page01() {
  return page("CZĘŚĆ WSTĘPNA — DANE OSOBY UCZĄCEJ SIĘ", "Część wstępna", [
    spacer(220),

    /* --- TYTUŁ GŁÓWNY — wyśrodkowany, wersaliki (standard druków PCTP) --- */
    p([r("IPET 2026 · WOPF (ICF) · STANDARD 2026", { size: 15, bold: true, color: BRAND.orange, cs: 16 })],
      { align: AlignmentType.CENTER, after: 180 }),
    p([r("INDYWIDUALNY PROGRAM", { size: 52, bold: true, color: BRAND.purple })],
      { align: AlignmentType.CENTER, after: 40, line: 560 }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 0, line: 560 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 22, color: BRAND.orange, space: 10 } },
      children: [r("EDUKACYJNO-TERAPEUTYCZNY", { size: 52, bold: true, color: BRAND.purple })],
    }),
    p([r("SYNTEZA ZINTEGROWANA  ·  WERSJA PRZEDSZKOLNA", { size: 19, color: BRAND.orange, cs: 10 })],
      { align: AlignmentType.CENTER, before: 150, after: 240 }),

    panel([
      p([r("Dokument opracowywany dla dziecka objętego wychowaniem przedszkolnym, posiadającego orzeczenie o potrzebie kształcenia specjalnego. Stanowi syntezę wszystkich obserwacji (KPOF → obserwacje pogłębione) w logiczną całość, bez powielania. Określa zakres i sposób dostosowania wymagań, zintegrowane działania nauczycieli i specjalistów oraz formy pomocy.",
        { size: 14, color: BRAND.ink })], { after: 80, line: 250 }),
      p([r("Podstawa prawna: ", { size: 13, bold: true, color: BRAND.amber }),
         r("art. 127 ustawy z 14 grudnia 2016 r. — Prawo oświatowe; rozporządzenie MEN z 9 sierpnia 2017 r. w sprawie kształcenia specjalnego (Dz.U. 2017 poz. 1578, ze zm.); podstawa programowa wychowania przedszkolnego (Rozp. MEN z 14.02.2017 r., Dz.U. 2017 poz. 356, ze zm.).",
        { size: 13, italics: true, color: BRAND.mute })], { after: 0, line: 240 }),
    ]),
    spacer(120),
    panel([
      p([r("✦ NOWE 26/27  ", { size: 13, bold: true, color: BRAND.orange, cs: 6 }),
         r("tym znaczkiem oznaczono elementy nowego modelu (ICF / KPOF, poziomy wsparcia, „Mój głos”) od roku szk. 2026/27. Rozliczenie wymogów rozporządzenia — karta kontrolna, str. 21.",
        { size: 13, color: BRAND.mute })], { after: 0, line: 240 }),
    ], { fill: BRAND.paperOr, edgeColor: BRAND.red }),

    numHead("I", "DANE OSOBY UCZĄCEJ SIĘ"),
    table([Math.floor(CW / 2), Math.ceil(CW / 2)], [
      new TableRow({ children: [
        fieldCell("IMIĘ I NAZWISKO", Math.floor(CW / 2)),
        fieldCell("DATA URODZENIA", Math.ceil(CW / 2)) ] }),
      new TableRow({ children: [
        fieldCell("GRUPA / ODDZIAŁ", Math.floor(CW / 2)),
        fieldCell("ROK SZKOLNY", Math.ceil(CW / 2)) ] }),
      new TableRow({ children: [
        fieldCell("SZKOŁA / PLACÓWKA", CW, { span: 2 }) ] }),
      new TableRow({ children: [
        fieldCell("PODSTAWA WYDANIA ORZECZENIA (NP. AUTYZM, NIEPEŁNOSPRAWNOŚĆ SPRZĘŻONA)", CW, { span: 2 }) ] }),
      new TableRow({ children: [
        fieldCell("NUMER I DATA ORZECZENIA / PORADNIA (PPP)", Math.floor(CW / 2)),
        fieldCell("PODSTAWA OBJĘCIA WSPARCIEM (ORZECZENIE / DIAGNOZA)", Math.ceil(CW / 2)) ] }),
      new TableRow({ children: [
        fieldCell("NUMER DOKUMENTU / UWAGI WAŻNE", CW, { span: 2, pad: 260 }) ] }),
    ]),
  ]);
}

/* ============================================================================
 * STRONA 2 — MÓJ GŁOS
 * ========================================================================== */
function page02() {
  return page("MÓJ GŁOS — PERSPEKTYWA DZIECKA", "Mój głos", [
    new Paragraph({ spacing: { before: 140, after: 60 }, children: [
      r("★  Mój głos — perspektywa dziecka", { size: 20, bold: true, color: BRAND.purple }),
      r("    ✦ NOWE 26/27", { size: 12, bold: true, color: BRAND.orange, cs: 6 }) ] }),
    note("Sekcja wypełniana z udziałem dziecka, dostosowana do jego możliwości komunikacyjnych."),
    label("MOJE MOCNE STRONY I SUPERMOCE"),
    fillBox(3),
    label("Z CZYM MAM NAJWIĘKSZĄ TRUDNOŚĆ W PRZEDSZKOLU?"),
    fillBox(3),
    label("CO MI NAJBARDZIEJ POMAGA W PRZEDSZKOLU?"),
    checkGrid(["cisza", "czas", "ruch", "piktogramy",
               "praca na komputerze", "przerwy", "wsparcie nauczyciela", ""], 4, { size: 15 }),
    label("INNE — CO JESZCZE MI POMAGA?"),
    fillBox(3),
  ]);
}

/* ============================================================================
 * STRONA 3 — WOPFU 1–2
 * ========================================================================== */
function page03() {
  return page("WOPFU — MOCNE STRONY I MOTYWACJA", "WOPFU · 1–2", [
    partTitle("CZĘŚĆ I · WOPF WG ICF"),
    note("Ocena obejmuje mocne strony, system motywacji, bariery i obserwacje funkcjonalne, uporządkowane zgodnie z Międzynarodową Klasyfikacją Funkcjonowania (ICF)."),
    numHead(1, "MOCNE STRONY, PREDYSPOZYCJE, ZAINTERESOWANIA I UZDOLNIENIA"),
    checkGrid([
      "Dobra pamięć wzrokowa i spostrzegawczość", "Zdolności manualne i plastyczne",
      "Zainteresowania przyrodnicze i techniczne", "Wysoka sprawność fizyczna i sportowa",
      "Umiejętność logicznego myślenia", "Empatia i chęć niesienia pomocy innym",
      "Zainteresowanie technologiami cyfrowymi", "Dobra orientacja w przestrzeni",
      "Zdolności muzyczne i poczucie rytmu", "Łatwość nawiązywania kontaktów",
    ], 2),
    label("INNE / DODATKOWE MOCNE STRONY"),
    fillBox(2),
    numHead(2, "SYSTEM MOTYWACJI DZIECKA (NA PODSTAWIE MOCNYCH STRON)"),
    checkGrid([
      "System żetonowy (punkty / naklejki)", "Kontrakt behawioralny (zasady i nagrody)",
      "Wzmocnienia pozytywne (pochwały)", "Tablica wyboru nagród (autonomia)",
      "System „First-Then” (najpierw zadanie, potem nagroda)", "Wykorzystanie zainteresowań jako nagroda",
      "Przerwy na relaksację jako wzmocnienie", "Funkcja pomocnika nauczyciela",
    ], 2),
    label("INNE / UWAGI DO SYSTEMU MOTYWACJI"),
    fillBox(2),
  ]);
}

/* ============================================================================
 * STRONA 4 — WOPFU 3–4 (bariery + ABC)
 * ========================================================================== */
function page04() {
  const cols = [
    { t: "A · Poprzednik", c: BRAND.purple, items: ["Polecenie nauczyciela", "Zmiana aktywności",
      "Hałas w sali", "Trudne zadanie", "Brak uwagi dorosłego", "Odmowa prośby",
      "Przerwa / czas wolny", "Interakcja z rówieśnikiem"] },
    { t: "B · Zachowanie", c: BRAND.red, items: ["Krzyk / hałasowanie", "Odmowa wykonania zadania",
      "Agresja słowna / fizyczna", "Ucieczka z miejsca pracy", "Niszczenie przedmiotów",
      "Autoagresja", "Płacz / wycofanie", "Ignorowanie poleceń"] },
    { t: "C · Konsekwencja", c: BRAND.teal, items: ["Upomnienie słowne", "Przerwanie zadania",
      "Odesłanie do wyciszenia", "Utrata przywileju", "Pomoc w wykonaniu zadania",
      "Ignorowanie zachowania", "Kontakt z rodzicem", "Pochwała za uspokojenie"] },
  ];
  const cw = Math.floor(CW / 3);
  const abc = table([cw, cw, CW - 2 * cw], [
    new TableRow({ children: cols.map((c, i) => new TableCell({
      width: { size: i === 2 ? CW - 2 * cw : cw, type: WidthType.DXA },
      borders: allThin, shading: { fill: c.c, type: ShadingType.CLEAR, color: "auto" },
      margins: { top: 60, bottom: 60, left: 110, right: 110 },
      children: [cellPara(c.t, { size: 15, bold: true, color: BRAND.white, cs: 4 })] })) }),
    new TableRow({ children: cols.map((c, i) => new TableCell({
      width: { size: i === 2 ? CW - 2 * cw : cw, type: WidthType.DXA },
      borders: allThin, verticalAlign: VerticalAlign.TOP,
      margins: { top: 70, bottom: 70, left: 90, right: 90 },
      children: c.items.map((it) => new Paragraph({ spacing: { after: 46, line: 230 }, children: [
        r(BOX + "  ", { size: 17, bold: true, color: c.c }),
        r(it, { size: 14 }) ] })) })) }),
  ]);

  return page("WOPFU — BARIERY I OBSERWACJA ABC", "WOPFU · 3–4", [
    numHead(3, "PRZYCZYNY NIEPOWODZEŃ EDUKACYJNYCH · TRUDNOŚCI I BARIERY"),
    checkGrid([
      "Trudności z koncentracją uwagi", "Niska samoocena i lęk przed porażką",
      "Trudności w rozumieniu poleceń złożonych", "Problemy z grafomotoryką i tempem pisania",
      "Trudności w relacjach rówieśniczych", "Bariery komunikacyjne (mowa, język)",
      "Nadwrażliwość sensoryczna (hałas, światło)", "Trudności w planowaniu i organizacji pracy",
      "Niska motywacja do wysiłku", "Trudności w radzeniu sobie z emocjami",
    ], 2),
    label("INNE / DODATKOWE"),
    fillBox(2),
    spacer(60),
    legal("PODSTAWA PRAWNA — PRZYCZYNY NIEPOWODZEŃ I BARIERY.",
      "WOPF uwzględnia „występujące trudności w funkcjonowaniu dziecka (…) oraz, w zależności od potrzeb, zakres i charakter wsparcia ze strony nauczycieli, specjalistów (…) lub przyczyny niepowodzeń edukacyjnych albo trudności w funkcjonowaniu dziecka, w tym bariery i ograniczenia utrudniające funkcjonowanie i uczestnictwo dziecka w życiu przedszkola” — § 6 ust. 1 pkt 1 rozporządzenia MEN z 9 sierpnia 2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.)."),
    numHead(4, "OBSERWACJA ABC — ANALIZA ZACHOWANIA"),
    panel([ p([
      r("Czym jest obserwacja ABC?  ", { size: 13, bold: true, color: BRAND.purple }),
      r("Metoda funkcjonalnej analizy zachowania — pozwala zrozumieć przyczynę i cel zachowania trudnego, a nie tylko je oceniać. Notujemy trzy elementy: A — poprzednik, B — zachowanie (opis faktów, bez ocen), C — następstwo (reakcja otoczenia, która zachowanie podtrzymuje lub wygasza). Cel: rozpoznać funkcję i nauczyć zachowania zastępczego (model pozytywnego wsparcia — PBS).",
        { size: 13, color: BRAND.mute }) ], { after: 0, line: 240 }) ],
      { fill: BRAND.paperOr, edgeColor: BRAND.red }),
    spacer(80),
    abc,
  ]);
}

/* ============================================================================
 * STRONA 5 — PODSUMOWANIE OBSZARÓW KPOF
 * ========================================================================== */
function page05() {
  const obszary = [
    "Uczenie się i stosowanie wiedzy", "Ogólne zadania i obowiązki",
    "Porozumiewanie się i mowa", "Motoryka i poruszanie się",
    "Dbanie o siebie i samoobsługa", "Życie domowe",
    "Wzajemne kontakty i relacje", "Edukacja i zabawa",
    "Życie w grupie i społeczności",
  ];
  const w = [620, CW - 620 - 1350 - 1900 - 1750, 1350, 1900, 1750];
  const rows = [ new TableRow({ tableHeader: true, children: [
    th("LP.", w[0]), th("OBSZAR FUNKCJONOWANIA", w[1]), th("PKT", w[2]),
    th("OCEN. / ETAP", w[3]), th("POZIOM WSPARCIA", w[4]) ] }) ];
  obszary.forEach((o, i) => {
    rows.push(new TableRow({ children: [
      td(String(i + 1), w[0], { align: AlignmentType.CENTER, bold: true, color: BRAND.orange,
        fill: i % 2 ? BRAND.paperLt : BRAND.white }),
      td(o, w[1], { size: 15, fill: i % 2 ? BRAND.paperLt : BRAND.white }),
      td("……… / 20", w[2], { align: AlignmentType.CENTER, size: 14, color: BRAND.mute,
        fill: i % 2 ? BRAND.paperLt : BRAND.white }),
      td("K · N · R · …", w[3], { align: AlignmentType.CENTER, size: 14, color: BRAND.mute,
        fill: i % 2 ? BRAND.paperLt : BRAND.white }),
      td([ new Paragraph({ alignment: AlignmentType.CENTER, spacing: { line: 230 }, children: [
        r(BOX + " I    ", { size: 15, bold: true, color: BRAND.orange }),
        r(BOX + " II    ", { size: 15, bold: true, color: BRAND.orange }),
        r(BOX + " III", { size: 15, bold: true, color: BRAND.orange }) ] }) ],
        w[4], { fill: i % 2 ? BRAND.paperLt : BRAND.white }),
    ] }));
  });

  return page("PODSUMOWANIE OBSZARÓW KPOF", "IPET · KPOF", [
    partTitle("CZĘŚĆ II · IPET"),
    numHead(1, "PODSUMOWANIE OBSZARÓW KPOF"),
    note("Skala punktowa 0–20 dla każdego obszaru. Kolumna „OCEN. / ETAP” — poziom wykonania (K — kontynuacja, N — nowa umiejętność, R — rozwinięcie) oraz etap: W — wstępny, Ś — średni, K — końcowy."),
    table(w, rows),
    spacer(160),
    panel([ new Paragraph({ spacing: { line: 250 }, children: [
      r("Rekomendowany ogólny poziom wsparcia:     ", { size: 16, bold: true, color: BRAND.purple }),
      r(BOX + "  Poziom I        ", { size: 18, bold: true, color: BRAND.orange }),
      r(BOX + "  Poziom II        ", { size: 18, bold: true, color: BRAND.orange }),
      r(BOX + "  Poziom III", { size: 18, bold: true, color: BRAND.orange }) ] }) ]),
    spacer(120),
    label("UZASADNIENIE REKOMENDACJI POZIOMU WSPARCIA"),
    fillBox(3),
  ]);
}

/* ============================================================================
 * STRONA 6 — ZALECENIA
 * ========================================================================== */
function page06() {
  function recTable(h1, h2) {
    const w = [620, Math.floor((CW - 620) / 2), CW - 620 - Math.floor((CW - 620) / 2)];
    const rows = [ new TableRow({ tableHeader: true,
      children: [th("LP.", w[0]), th(h1, w[1]), th(h2, w[2])] }) ];
    for (let i = 1; i <= 5; i++) {
      rows.push(new TableRow({ children: [
        td(String(i), w[0], { align: AlignmentType.CENTER, bold: true, color: BRAND.orange,
          fill: i % 2 === 0 ? BRAND.paperLt : BRAND.white }),
        td(blankLines(2), w[1], { fill: i % 2 === 0 ? BRAND.paperLt : BRAND.white }),
        td(blankLines(2), w[2], { fill: i % 2 === 0 ? BRAND.paperLt : BRAND.white }),
      ] }));
    }
    return table(w, rows);
  }
  return page("ZALECENIA Z ORZECZENIA I OPINII PPP", "IPET · zalecenia", [
    numHead(2, "ZALECENIA Z ORZECZENIA O POTRZEBIE KSZTAŁCENIA SPECJALNEGO I SPOSÓB REALIZACJI"),
    recTable("ZALECENIE (TREŚĆ Z ORZECZENIA)", "SPOSÓB REALIZACJI W SZKOLE / PLACÓWCE"),
    numHead(3, "ZALECENIA Z OPINII PSYCHOLOGICZNO-PEDAGOGICZNEJ I SPOSÓB REALIZACJI"),
    recTable("ZALECENIE (TREŚĆ Z OPINII PPP)", "SPOSÓB REALIZACJI"),
  ]);
}

/* ============================================================================
 * STRONY 7–12 — CELE SMART · SFERY 1–6
 * ========================================================================== */
const SFERY = [
  {
    nr: 1, nazwa: "Poznawcze (uczenie się, edukacja)",
    narzedzia: "KPOF (obsz. I, VIII) · obserwacja uwagi, pamięci i myślenia · analiza wytworów (rysunki, układanki) · Profil biopsychospołeczny (ICF) · Mocne strony dziecka",
    icf: "d110–d179 · d820 · b140 (uwaga) · b144 (pamięć) · b164 (f. wykonawcze) · b1720 (myślenie)",
    trudnosci: ["Spostrzeganie", "Uwaga i koncentracja", "Pamięć", "Myślenie i wnioskowanie",
                "Umiejętności wykonawcze", "Tempo uczenia się"],
    obszar: "Uczenie się i stosowanie wiedzy",
    poziomy: [
      "Dziecko pracuje w większości samodzielnie; potrzebuje okazjonalnych wskazówek, przypomnień i sprawdzenia efektu pracy.",
      "Funkcje częściowo obniżone — realizuje zadania z dodatkowym czasem, podziałem na etapy, wsparciem wizualnym i przypomnieniami.",
      "Funkcje znacznie ograniczone — pracuje krok po kroku ze stałym wsparciem dorosłego, na konkretach, z pomocą „ręka na rękę”.",
    ],
    motywacja: "System żetonowy, wykorzystanie zainteresowań dziecka jako nagrody, pochwała opisowa.",
    dzialania: "Wszyscy nauczyciele stosują krótkie, jednoznaczne polecenia, dzielą materiał na mniejsze partie, dają dodatkowy czas i wsparcie wizualne oraz utrwalają kluczowe treści.",
    metody: ["Praca na konkretach i wielozmysłowa", "Ćwiczenia uwagi i pamięci",
             "Stopniowanie trudności i powtórki", "Mapy myśli i notatki"],
    formy: ["Indywidualna (1:1)", "Mała grupa", "Z całą grupą", "Współpraca szkoła–dom"],
    pomoce: "Karty pracy, plansze edukacyjne, materiały manipulacyjne, gry dydaktyczne, programy multimedialne, mapy myśli.",
  },
  {
    nr: 2, nazwa: "Emocjonalno-społeczne (kontakty, społeczność)",
    narzedzia: "KPOF (obsz. VII, IX) · Karta obserwacji Teorii umysłu (ToM, przedszkole) · Karta analizy i wsparcia zachowania (ABC/FBA/MPS) · obserwacja zabawy i relacji",
    icf: "d710–d770 · b152 (f. emocji) · b1251 (przystosowanie) · d250 (kontrola zachowania) · b1801 (empatia/ToM) · d910–d950",
    trudnosci: ["Rozpoznawanie i nazywanie emocji", "Regulacja emocji i samokontrola",
                "Naprzemienność / czekanie na kolej", "Współdziałanie z rówieśnikami",
                "Relacje i kontakty", "Empatia i teoria umysłu"],
    obszar: "Wzajemne kontakty i związki",
    poziomy: [
      "Nawiązuje kontakt i reguluje emocje w większości sytuacji; potrzebuje okazjonalnego przypomnienia zasad.",
      "Funkcje częściowo obniżone — współdziała i reguluje emocje z podpowiedzią, wsparciem wizualnym i wcześniej wyćwiczoną strategią.",
      "Funkcje znacznie ograniczone — wymaga stałej obecności dorosłego, mediacji w relacjach i pomocy „krok po kroku” w sytuacjach społecznych.",
    ],
    motywacja: "Wzmocnienia pozytywne, system „First-Then”, funkcja pomocnika nauczyciela.",
    dzialania: "Zespół stosuje jednolity system motywacyjny i spójne reagowanie na zachowania trudne (model ABC/FBA); prowadzi trening umiejętności społecznych i wzmocnienia pozytywne.",
    metody: ["Trening umiejętności społecznych, emocjonalnych i komunikacyjnych (TUS / TUE / TUK)",
             "Modelowanie i odgrywanie ról (drama)", "Historyjki społeczne",
             "„Termometr emocji” i techniki regulacji"],
    formy: ["W grupie", "W parach", "Indywidualna (1:1)", "Strefa wyciszenia"],
    pomoce: "Karty emocji, „termometr emocji”, historyjki społeczne, plansze zasad, kącik wyciszenia.",
  },
  {
    nr: 3, nazwa: "Funkcjonowanie motoryczne",
    narzedzia: "KPOF (obsz. IV) · Profil sensoryczny dziecka (model Dunn) · obserwacja motoryki małej i dużej · ćwiczenia grafomotoryczne i terapia ręki",
    icf: "d440–d455 · b760 (kontrola ruchów) · b147 (praksja) · b156 (percepcja) · b235 (przedsionek) · d170 (pisanie)",
    trudnosci: ["Napięcie mięśniowe / posturalne", "Koordynacja ruchowa",
                "Koordynacja obustronna i oko–ręka", "Praksja — planowanie ruchu",
                "Motoryka mała i chwyt", "Grafomotoryka i pisanie"],
    obszar: "Motoryka i poruszanie się",
    poziomy: [
      "Sprawność motoryczna w normie w większości zadań; potrzebuje okazjonalnej korekty chwytu lub tempa.",
      "Funkcje częściowo obniżone — pisze i wykonuje ćwiczenia manualne z dostosowaniami (nakładka, liniatura, dodatkowy czas).",
      "Funkcje znacznie ograniczone — wymaga stałej pomocy fizycznej, sprzętu specjalistycznego i pracy „ręka na rękę”.",
    ],
    motywacja: "Docenianie wysiłku i postępu, przerwy ruchowe jako wzmocnienie.",
    dzialania: "Nauczyciele zapewniają dostosowania (nakładki, liniatura, możliwość pisania na komputerze), przerwy ruchowe i bezpieczne modyfikacje ćwiczeń.",
    metody: ["Ćwiczenia grafomotoryczne i manualne", "Terapia ręki",
             "Zabawy ruchowe i przerwy sensoryczne", "Integracja sensoryczna (SI)"],
    formy: ["Indywidualna (1:1)", "Mała grupa", "Przerwy sensoryczno-ruchowe", "Z asystą"],
    pomoce: "Nakładki na przybory, liniatura powiększona, masy plastyczne, sprzęt do terapii ręki, sorter, przybory do chwytu.",
  },
  {
    nr: 4, nazwa: "Mowa i komunikacja",
    narzedzia: "KPOF (obsz. III) · Kwestionariusz mowy i komunikacji (logopedyczny, przedszkole) · obserwacja słuchu fonematycznego · obserwacja komunikacji i wskazań do AAC",
    icf: "d310–d360 · b320 (artykulacja) · b1560 (słuch fonematyczny) · b16700/b16710 (język) · d3350 (narracja)",
    trudnosci: ["Rozumienie mowy", "Przetwarzanie słuchowe / fonematyczne",
                "Artykulacja i wymowa", "Słownictwo i gramatyka — język",
                "Budowanie wypowiedzi / narracja", "Komunikacja wspomagająca / AAC"],
    obszar: "Porozumiewanie się",
    poziomy: [
      "Komunikuje potrzeby i rozumie polecenia w większości sytuacji; potrzebuje okazjonalnego powtórzenia lub uproszczenia.",
      "Funkcje częściowo obniżone — komunikuje się z podpowiedzią, wsparciem wizualnym i wydłużonym czasem na wypowiedź.",
      "Funkcje znacznie ograniczone — porozumiewa się głównie przez AAC (PECS, piktogramy) ze stałym wsparciem dorosłego.",
    ],
    motywacja: "Pochwała za każdą próbę komunikacji, tablica wyboru, obrazkowe wzmocnienia.",
    dzialania: "Nauczyciele ujednolicają sposób wydawania poleceń, stosują wsparcie wizualne i AAC, wydłużają czas na wypowiedź; logopeda prowadzi terapię mowy.",
    metody: ["Ćwiczenia logopedyczne", "Modelowanie wypowiedzi",
             "Komunikacja wspomagająca (AAC / PECS)", "Ćwiczenia słuchu fonematycznego"],
    formy: ["Terapia 1:1", "Mała grupa", "Wsparcie w przedszkolu", "Współpraca z logopedą"],
    pomoce: "Tablice i karty AAC / PECS, piktogramy, lustro logopedyczne, obrazki sytuacyjne, aplikacje komunikacyjne.",
  },
  {
    nr: 5, nazwa: "Samodzielność (dbanie o siebie)",
    narzedzia: "KPOF (obsz. V, VI) · obserwacja funkcjonalna samoobsługi · Profil biopsychospołeczny i sensoryczny · wywiad z rodzicem",
    icf: "d510–d570 · b164 (planowanie) · b1252 (impulsywność) · d230 (rutyna) · b134 (sen/energia)",
    trudnosci: ["Higiena i dbanie o siebie", "Ubieranie się", "Jedzenie",
                "Samodzielność i zaradność", "Organizacja rzeczy", "Bezpieczeństwo"],
    obszar: "Dbanie o siebie i samoobsługa",
    poziomy: [
      "Wykonuje czynności samoobsługowe samodzielnie; potrzebuje okazjonalnego przypomnienia kolejności.",
      "Funkcje częściowo obniżone — realizuje czynności według planu wizualnego, z częściową pomocą i przypomnieniami.",
      "Funkcje znacznie ograniczone — wymaga stałej asysty dorosłego i prowadzenia „krok po kroku” w większości czynności.",
    ],
    motywacja: "Tablica osiągnięć, nagroda za samodzielność, autonomia w wyborze.",
    dzialania: "Zespół stosuje stałą, przewidywalną rutynę i plan wizualny czynności, stopniowo wycofuje pomoc i wzmacnia samodzielność.",
    metody: ["Trening samodzielności metodą małych kroków", "Plany wizualne czynności",
             "Modelowanie i instruktaż", "Nauka w sytuacjach naturalnych"],
    formy: ["Indywidualna (1:1)", "W sytuacjach naturalnych", "Z asystą", "Współpraca szkoła–dom"],
    pomoce: "Plany wizualne czynności, piktogramy krok po kroku, tablica osiągnięć, materiały do treningu samodzielności.",
  },
  {
    nr: 6, nazwa: "Ogólne zadania i zabawa",
    narzedzia: "KPOF (obsz. II, VIII) · obserwacja funkcji wykonawczych · Karta analizy zachowania (ABC — organizacja, samokontrola) · wywiad z rodzicem",
    icf: "d210–d250 · d610–d660 · b1641 (organizacja) · b1643 (elastyczność) · d240 (radzenie ze stresem) · d160 (uwaga w zadaniu)",
    trudnosci: ["Rozpoczynanie zadania", "Zadania złożone", "Organizacja i rutyna",
                "Radzenie sobie ze stresem", "Planowanie / f. wykonawcze", "Życie domowe"],
    obszar: "Ogólne zadania i obowiązki",
    poziomy: [
      "Rozpoczyna i kończy zadania samodzielnie; potrzebuje okazjonalnego przypomnienia o kolejnych krokach.",
      "Funkcje częściowo obniżone — realizuje zadania według checklisty, z dodatkowym czasem i przypomnieniami.",
      "Funkcje znacznie ograniczone — pracuje krok po kroku ze stałym wsparciem dorosłego, na konkretach i z pomocą „ręka na rękę”.",
    ],
    motywacja: "Checklisty z nagrodą za ukończenie, kontrakt behawioralny, przerwy.",
    dzialania: "Nauczyciele dostarczają checklisty i plan dnia, przypominają o kolejnych krokach, wspierają w organizacji pracy i radzeniu sobie ze zmianą.",
    metody: ["Planowanie krok po kroku (checklisty)", "Trening funkcji wykonawczych",
             "Instruktaż i przypomnienia", "Organizacja warsztatu pracy"],
    formy: ["Indywidualna (1:1)", "Mała grupa", "Z całą grupą", "Współpraca szkoła–dom"],
    pomoce: "Checklisty i plan dnia, planery, timery / klepsydry, karty „co teraz / co potem”, organizery.",
  },
];

function metaLine(head, text, color) {
  return p([ r(head + " ", { size: 12, bold: true, color: color || BRAND.purple }),
             r(text, { size: 12, color: BRAND.mute }) ], { after: 30, line: 215 });
}

function pageSfera(s, idx) {
  const first = idx === 0;
  const out = [];

  if (first) {
    out.push(numHead(4, "CELE EDUKACYJNE I TERAPEUTYCZNE (SMART) — SFERY FUNKCJONOWANIA"));
    out.push(note("Sześć sfer wg ICF / KPOF — każda na osobnej stronie. SMART = Specyficzny · Mierzalny · Atrakcyjny/osiągalny · Realny/istotny · Terminowy."));
  } else {
    out.push(partTitle("CELE SMART — SFERA " + s.nr));
  }

  out.push(new Paragraph({ spacing: { before: 120, after: 70 }, children: [
    r(String(s.nr) + "  ", { size: 20, bold: true, color: BRAND.orange }),
    r("Sfera " + s.nr + " — " + s.nazwa, { size: 18, bold: true, color: BRAND.purple }) ] }));
  out.push(metaLine("Narzędzia oceny i obserwacji:", s.narzedzia));
  out.push(metaLine("Kody ICF:", s.icf, BRAND.teal));
  out.push(spacer(40));

  /* trudności + poziom wsparcia */
  const wT = [CW - 2600, 2600];
  out.push(table(wT, [
    new TableRow({ children: [
      th("TRUDNOŚCI I BARIERY — ZAZNACZ WYSTĘPUJĄCE", wT[0]),
      new TableCell({ width: { size: wT[1], type: WidthType.DXA },
        borders: allThin, verticalAlign: VerticalAlign.CENTER,
        shading: { fill: BRAND.orange, type: ShadingType.CLEAR, color: "auto" },
        margins: { top: 66, bottom: 66, left: 100, right: 100 },
        children: [ new Paragraph({ alignment: AlignmentType.CENTER, spacing: { line: 230 }, children: [
          r("POZIOM WSPARCIA:  ", { size: 13, bold: true, color: BRAND.white, cs: 4 }),
          r(BOX + " I  " + BOX + " II  " + BOX + " III", { size: 15, bold: true, color: BRAND.white }) ] }) ] }),
    ] }),
    new TableRow({ children: [
      new TableCell({ width: { size: CW, type: WidthType.DXA }, columnSpan: 2,
        borders: allThin, margins: { top: 45, bottom: 45, left: 90, right: 90 },
        children: [ checkGrid(s.trudnosci, 2, { size: 15, width: CW - 200 }) ] }),
    ] }),
  ]));
  out.push(spacer(60));

  /* wynik diagnozy */
  const wD = [1500, CW - 1500];
  out.push(table(wD, [ new TableRow({ children: [
    new TableCell({ width: { size: wD[0], type: WidthType.DXA }, borders: allThin,
      verticalAlign: VerticalAlign.CENTER,
      shading: { fill: BRAND.purple, type: ShadingType.CLEAR, color: "auto" },
      margins: { top: 70, bottom: 70, left: 100, right: 100 },
      children: [ cellPara("WYNIK DIAGNOZY", { size: 13, bold: true, color: BRAND.white, cs: 6,
        align: AlignmentType.CENTER }) ] }),
    new TableCell({ width: { size: wD[1], type: WidthType.DXA }, borders: allThin,
      shading: { fill: BRAND.paperLt, type: ShadingType.CLEAR, color: "auto" },
      margins: { top: 80, bottom: 80, left: 130, right: 130 },
      children: [
        new Paragraph({ spacing: { after: 70, line: 240 }, children: [
          r("Obszar „" + s.obszar + "” — wynik ", { size: 14 }),
          r("…………………………  ……… / 20 pkt", { size: 14, bold: true, color: BRAND.mute }),
          r("  (sten ……), co odpowiada kwalifikacji:", { size: 14 }) ] }),
        new Paragraph({ spacing: { line: 240 }, children: [
          r(BOX + " Poziom I — wsparcie minimalne      ", { size: 15, bold: true, color: BRAND.orange }),
          r(BOX + " Poziom II — umiarkowane      ", { size: 15, bold: true, color: BRAND.orange }),
          r(BOX + " Poziom III — znaczne", { size: 15, bold: true, color: BRAND.orange }) ] }),
      ] }),
  ] }) ]));
  out.push(spacer(50));

  /* charakterystyka poziomów I / II / III */
  out.push(label("CHARAKTERYSTYKA TRUDNOŚCI WG POZIOMU WSPARCIA", { before: 20, after: 50 }));
  const wP = Math.floor(CW / 3);
  const nazwyP = ["I  WSPARCIE MINIMALNE", "II  WSPARCIE UMIARKOWANE", "III  WSPARCIE ZNACZNE"];
  const kolP = [BRAND.green, BRAND.amber, BRAND.red];
  out.push(table([wP, wP, CW - 2 * wP], [
    new TableRow({ children: nazwyP.map((n, i) => new TableCell({
      width: { size: i === 2 ? CW - 2 * wP : wP, type: WidthType.DXA },
      borders: allThin, shading: { fill: kolP[i], type: ShadingType.CLEAR, color: "auto" },
      margins: { top: 50, bottom: 50, left: 100, right: 100 },
      children: [cellPara(n, { size: 12, bold: true, color: BRAND.white, cs: 4 })] })) }),
    new TableRow({ children: s.poziomy.map((t, i) => new TableCell({
      width: { size: i === 2 ? CW - 2 * wP : wP, type: WidthType.DXA },
      borders: allThin, verticalAlign: VerticalAlign.TOP,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [cellPara(t, { size: 12, color: BRAND.ink, line: 220 })] })) }),
  ]));
  out.push(spacer(50));

  /* system motywacji */
  out.push(panelTitled("SYSTEM MOTYWACJI — OPARTY NA MOCNYCH STRONACH", s.motywacja));
  out.push(spacer(50));

  /* cel SMART */
  const wS = [CW - 1900, 1900];
  out.push(table(wS, [ new TableRow({ children: [
    th("CEL SMART — WYNIKA Z TRUDNOŚCI (kryterium mierzalne + sposób pomiaru)", wS[0], { fill: BRAND.green }),
    new TableCell({ width: { size: wS[1], type: WidthType.DXA }, borders: allThin,
      shading: { fill: BRAND.green, type: ShadingType.CLEAR, color: "auto" },
      verticalAlign: VerticalAlign.CENTER,
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [ cellPara("S    M    A    R    T", { size: 14, bold: true,
        color: BRAND.white, cs: 20, align: AlignmentType.CENTER }) ] }),
  ] }) ]));
  out.push(fillBox(3));
  out.push(spacer(50));

  /* zintegrowane działania */
  out.push(panelTitled("ZINTEGROWANE DZIAŁANIA NAUCZYCIELI I SPECJALISTÓW", s.dzialania,
    { fill: BRAND.paperOr, edgeColor: BRAND.red, titleColor: BRAND.red }));
  out.push(spacer(50));

  /* metody + formy */
  const wM = Math.floor(CW / 2);
  out.push(table([wM, CW - wM], [
    new TableRow({ children: [
      th("METODY PRACY — ZAZNACZ", wM), th("FORMY PRACY — ZAZNACZ", CW - wM) ] }),
    new TableRow({ children: [
      new TableCell({ width: { size: wM, type: WidthType.DXA }, borders: allThin,
        verticalAlign: VerticalAlign.TOP, margins: { top: 50, bottom: 50, left: 90, right: 90 },
        children: [ checkGrid(s.metody, 1, { size: 14, width: wM - 180 }) ] }),
      new TableCell({ width: { size: CW - wM, type: WidthType.DXA }, borders: allThin,
        verticalAlign: VerticalAlign.TOP, margins: { top: 50, bottom: 50, left: 90, right: 90 },
        children: [ checkGrid(s.formy, 1, { size: 14, width: CW - wM - 180 }) ] }),
    ] }),
    new TableRow({ children: [
      new TableCell({ width: { size: CW, type: WidthType.DXA }, columnSpan: 2, borders: allThin,
        margins: { top: 50, bottom: 60, left: 110, right: 110 },
        children: [
          new Paragraph({ spacing: { after: 30, line: 210 }, children: [
            r("INNE — WŁASNE", { size: 11, bold: true, color: BRAND.mute, cs: 8 })] }),
          ...blankLines(1, { size: 15 }) ] }),
    ] }),
  ]));
  out.push(spacer(50));

  out.push(panelTitled("PROPONOWANE POMOCE DYDAKTYCZNE", s.pomoce));

  const tytul = first ? "CEL SMART · SFERA 1 · POZNAWCZE" : "CEL SMART · SFERA " + s.nr;
  return page(tytul, "IPET · cele SMART", out);
}

/* ============================================================================
 * STRONA 13 — DOSTOSOWANIA (5, 5b, 5c)
 * ========================================================================== */
function page13() {
  const wM = Math.floor(CW / 2);
  const dwaBoki = (t1, i1, t2, i2) => table([wM, CW - wM], [
    new TableRow({ children: [th(t1, wM), th(t2, CW - wM)] }),
    new TableRow({ children: [
      new TableCell({ width: { size: wM, type: WidthType.DXA }, borders: allThin,
        verticalAlign: VerticalAlign.TOP, margins: { top: 70, bottom: 70, left: 90, right: 90 },
        children: [checkGrid(i1, 1, { size: 15, width: wM - 180 })] }),
      new TableCell({ width: { size: CW - wM, type: WidthType.DXA }, borders: allThin,
        verticalAlign: VerticalAlign.TOP, margins: { top: 70, bottom: 70, left: 90, right: 90 },
        children: [checkGrid(i2, 1, { size: 15, width: CW - wM - 180 })] }),
    ] }),
  ]);

  return page("ZAKRES I SPOSÓB DOSTOSOWANIA WYMAGAŃ", "IPET · dostosowania", [
    numHead(5, "ZAKRES I SPOSÓB DOSTOSOWANIA WYMAGAŃ — PROJEKTOWANIE UNIWERSALNE"),
    dwaBoki(
      "METODY I FORMY PRACY",
      ["Wydłużony czas pracy", "Instrukcje krokowe", "Dostosowanie progów ocen",
       "Alternatywne formy sprawdzania wiedzy", "Indywidualizacja tempa pracy",
       "Praca na konkretach i materiałach poglądowych", "Miejsce w pierwszej ławce"],
      "ŚRODOWISKO I TECHNOLOGIE",
      ["Text-to-Speech / Speech-to-Text", "Systemy wizualne / AAC",
       "Strefa wyciszenia / słuchawki wygłuszające", "Ograniczenie dystraktorów",
       "Plany aktywności i piktogramy", "Dostosowanie stanowiska pracy", ""]),
    label("INNE DOSTOSOWANIA / KOMENTARZ ZESPOŁU"),
    fillBox(2),

    numHead("5 b", "DOSTOSOWANIE WARUNKÓW ORGANIZACJI KSZTAŁCENIA (PKT 7)"),
    checkGrid([
      "Dostosowanie sali i kącików (oświetlenie, akustyka, strefy)",
      "Sprzęt specjalistyczny (sprzęt do pozycjonowania, FM, pętla)",
      "Technologie i pomoce wspomagające (AAC, programy, obrazki)",
      "Materiały w wersji dostępnej (powiększenie, kontrast, dotyk, audio)",
      "Dostosowanie rytmu dnia i planu aktywności",
      "Likwidacja barier architektonicznych i sensorycznych",
    ], 2, { size: 15 }),

    numHead("5 c", "PRZYGOTOWANIE DO NAUKI W SZKOLE — GOTOWOŚĆ SZKOLNA (PKT 8)"),
    checkGrid([
      "Wspomaganie rozwoju i przygotowanie do nauki w szkole",
      "Diagnoza gotowości szkolnej (obserwacja)",
      "Rozpoznanie predyspozycji, uzdolnień i zainteresowań",
      "Rozwijanie umiejętności potrzebnych w szkole (samodzielność, uwaga)",
      "Współpraca z rodzicami i poradnią w planowaniu ścieżki",
      "Przekazanie informacji o dziecku do szkoły (za zgodą rodziców)",
    ], 2, { size: 15 }),
    spacer(100),
    legal("PODSTAWA PRAWNA — DOSTOSOWANIE WYMAGAŃ.",
      "IPET określa „zakres i sposób dostosowania (…) wymagań edukacyjnych (…) do indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych dziecka, w szczególności przez zastosowanie odpowiednich metod i form pracy z dzieckiem” — § 6 ust. 1 pkt 1 rozporządzenia MEN z 9 sierpnia 2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.). Dostosowanie wymagań do indywidualnych potrzeb — art. 44b ust. 8 pkt 1 ustawy o systemie oświaty oraz rozporządzenie w sprawie podstawy programowej kształcenia ogólnego."),
  ]);
}

/* ============================================================================
 * STRONY 14–15 — FORMY WSPARCIA (rewalidacja / pomoc pp)
 * ========================================================================== */
function tabelaZajec(pozycje) {
  const w = [560, CW - 560 - 1150 - 1700 - 2350, 1150, 1700, 2350];
  const rows = [ new TableRow({ tableHeader: true, children: [
    th("✓", w[0], { align: AlignmentType.CENTER }), th("RODZAJ ZAJĘĆ", w[1]),
    th("H/TYDZ.", w[2], { align: AlignmentType.CENTER }), th("OKRES", w[3]),
    th("REALIZATOR", w[4]) ] }) ];
  pozycje.forEach((z, i) => {
    const fill = i % 2 ? BRAND.paperLt : BRAND.white;
    rows.push(new TableRow({ children: [
      td(BOX, w[0], { align: AlignmentType.CENTER, size: 18, bold: true, color: BRAND.orange, fill }),
      td(z[0], w[1], { size: 14, fill }),
      td("………", w[2], { align: AlignmentType.CENTER, size: 14, color: BRAND.mute, fill }),
      td(z[1] || "Rok szk. ……… / ………", w[3], { size: 13, color: BRAND.mute, fill }),
      td(z[2], w[4], { size: 13, color: BRAND.mute, fill }),
    ] }));
  });
  return table(w, rows);
}

function page14() {
  return page("FORMY WSPARCIA — ZAJĘCIA REWALIDACYJNE", "IPET · rewalidacja", [
    numHead("6 A", "FORMY WSPARCIA — ZAJĘCIA REWALIDACYJNE"),
    tabelaZajec([
      ["Trening umiejętności społecznych (TUS)", "", "Psycholog"],
      ["Trening umiejętności emocjonalnych (TUE)", "", "Psycholog / pedagog"],
      ["Trening umiejętności komunikacyjnych (TUK)", "", "Logopeda / pedagog"],
      ["Trening Funkcjonowania Codziennego (TFC)", "", "Oligofrenopedagog"],
      ["Trening orientacji przestrzennej i poruszania się", "", "Tyflopedagog"],
      ["Rozwijanie komunikowania się (AAC)", "", "Logopeda"],
      ["Trening rozwoju sensorycznego (SI)", "", "Terapeuta SI"],
      ["Trening rozwoju funkcji poznawczych", "", "Pedagog spec."],
      ["Gimnastyka korekcyjna", "", "Nauczyciel WF"],
      ["Logopedia rewalidacyjna", "", "Logopeda"],
      ["Terapia ręki", "", "Terapeuta ped."],
      ["Inne — wpisz", "", "…"],
    ]),
    spacer(120),
    legal("PODSTAWA PRAWNA — ZAJĘCIA REWALIDACYJNE.",
      "„W ramach zajęć rewalidacyjnych w programie należy uwzględnić w szczególności rozwijanie umiejętności komunikacyjnych przez: naukę orientacji przestrzennej i poruszania się oraz naukę systemu Braille’a lub innych alternatywnych metod komunikacji — w przypadku dziecka niewidomego; naukę języka migowego lub innych alternatywnych metod komunikacji (AAC) — w przypadku dziecka z autyzmem, w tym z zespołem Aspergera; zajęcia rozwijające umiejętności społeczne, w tym umiejętności komunikacyjne” — § 6 ust. 2 rozporządzenia MEN z 9 sierpnia 2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.)."),
  ]);
}

function page15() {
  return page("FORMY POMOCY PSYCHOLOGICZNO-PEDAGOGICZNEJ", "IPET · pomoc pp", [
    numHead("6 B", "FORMY POMOCY PSYCHOLOGICZNO-PEDAGOGICZNEJ"),
    tabelaZajec([
      ["Zajęcia korekcyjno-kompensacyjne", "", "Terapeuta ped."],
      ["Zajęcia logopedyczne", "", "Logopeda"],
      ["Rozwijające kompetencje emocjonalno-społeczne", "", "Pedagog / Psycholog"],
      ["Zajęcia wspomagające rozwój", "", "Naucz. wych. przedsz."],
      ["Zajęcia rozwijające uzdolnienia", "", "Nauczyciel / specjalista"],
      ["Zajęcia rozwijające umiejętność uczenia się i gotowość szkolną", "", "Nauczyciel / specjalista"],
      ["Zindywidualizowana ścieżka realizacji przygotowania przedszkolnego", "", "Nauczyciel / specjalista"],
      ["Warsztaty dla rodziców / konsultacje", "", "Specjaliści"],
      ["Terapia pedagogiczna", "", "Terapeuta ped."],
      ["Socjoterapia", "", "Socjoterapeuta"],
      ["Inne — wpisz", "", "…"],
    ]),
    spacer(120),
    legal("PODSTAWA PRAWNA — POMOC PSYCHOLOGICZNO-PEDAGOGICZNA.",
      "„Pomoc psychologiczno-pedagogiczna w przedszkolu, szkole i placówce jest udzielana w trakcie bieżącej pracy z dzieckiem oraz przez zintegrowane działania nauczycieli i specjalistów, a także w formie: zajęć rozwijających uzdolnienia; zajęć rozwijających umiejętności uczenia się; zajęć wspomagających rozwój; zajęć specjalistycznych, korekcyjno-kompensacyjnych, logopedycznych, rozwijających kompetencje emocjonalno-społeczne oraz innych zajęć o charakterze terapeutycznym; zajęć związanych z wyborem kierunku kształcenia i zawodu; zindywidualizowanej ścieżki kształcenia; porad i konsultacji; warsztatów” — § 6 rozporządzenia MEN z 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej (Dz.U. 2017 poz. 1591, z późn. zm.). Wymiar jednostki: 45 min."),
  ]);
}

/* ============================================================================
 * STRONA 16 — WSPARCIE OSOBOWE I WSPÓŁPRACA Z RODZICAMI
 * ========================================================================== */
function page16() {
  const wA = Math.floor(CW / 3);
  const boxTak = (tytul) => new TableCell({
    width: { size: wA, type: WidthType.DXA }, borders: allThin,
    verticalAlign: VerticalAlign.TOP, margins: { top: 80, bottom: 80, left: 110, right: 110 },
    children: [
      cellPara(tytul, { size: 13, bold: true, color: BRAND.purple }),
      new Paragraph({ spacing: { before: 80, line: 240 }, children: [
        r(BOX + "  Tak        ", { size: 16, bold: true, color: BRAND.orange }),
        r(BOX + "  Nie", { size: 16, bold: true, color: BRAND.orange }) ] }),
    ] });

  const wI = [1500, Math.floor((CW - 1500) / 3), Math.floor((CW - 1500) / 3),
              CW - 1500 - 2 * Math.floor((CW - 1500) / 3)];
  const icfRows = [ new TableRow({ tableHeader: true, children: [
    th("KOD ICF", wI[0]), th("BARIERA BEZPIECZEŃSTWA", wI[1]),
    th("BARIERA EDUKACYJNA", wI[2]), th("BARIERA W RELACJACH", wI[3]) ] }) ];
  for (let i = 0; i < 4; i++) {
    const fill = i % 2 ? BRAND.paperLt : BRAND.white;
    icfRows.push(new TableRow({ children: [
      td(blankLines(1), wI[0], { fill }), td(blankLines(1), wI[1], { fill }),
      td(blankLines(1), wI[2], { fill }), td(blankLines(1), wI[3], { fill }) ] }));
  }

  return page("WSPARCIE OSOBOWE I WSPÓŁPRACA Z RODZICAMI", "IPET · wsparcie", [
    numHead(7, "WSPARCIE DODATKOWE — NAUCZYCIEL WSPÓŁORGANIZUJĄCY / ASYSTENT"),
    table([wA, wA, CW - 2 * wA], [ new TableRow({ children: [
      boxTak("Nauczyciel współorganizujący kształcenie"),
      boxTak("Pomoc asystenta dziecka"),
      new TableCell({ width: { size: CW - 2 * wA, type: WidthType.DXA }, borders: allThin,
        verticalAlign: VerticalAlign.TOP, margins: { top: 80, bottom: 80, left: 110, right: 110 },
        children: [
          cellPara("WYMIAR (H/TYDZ.) / POZIOM WSPARCIA", { size: 11, bold: true, color: BRAND.mute, cs: 8 }),
          new Paragraph({ spacing: { before: 80, line: 240 }, children: [
            r("……… h/tydz.        ", { size: 14, color: BRAND.mute }),
            r(BOX + " I  " + BOX + " II  " + BOX + " III", { size: 15, bold: true, color: BRAND.orange }) ] }),
        ] }),
    ] }) ]),

    numHead(8, "SZCZEGÓŁOWE UZASADNIENIE WSPARCIA OSOBOWEGO (KODY ICF)"),
    metaLine("Kody ICF:", "e330 (osoby wspierające), d160 (uwaga), d240 (stres), d710/d720 (interakcje), d250 (zachowanie), d570 (bezpieczeństwo), d310/d330 (komunikacja), d820 (edukacja).", BRAND.teal),
    spacer(50),
    table(wI, icfRows),

    numHead(9, "DZIAŁANIA WSPIERAJĄCE RODZICÓW I WSPÓŁPRACĘ"),
    checkGrid([
      "Konsultacje i porady ze specjalistami", "Instruktaż do pracy i utrwalania w domu",
      "Warsztaty / szkolenia (pedagogizacja rodziców)", "Wsparcie w kontakcie z poradnią PPP i instytucjami",
      "Pomoc w rozumieniu orzeczenia i dokumentacji", "Wsparcie emocjonalne i informacyjne",
      "Udział w spotkaniach zespołu i współtworzeniu IPET", "Ujednolicenie strategii i systemu nagród szkoła–dom",
    ], 2, { size: 15 }),
    spacer(80),
    legal("PODSTAWA PRAWNA — WSPÓŁPRACA Z RODZICAMI.",
      "IPET określa „działania wspierające rodziców dziecka oraz — w zależności od potrzeb — zakres współdziałania z poradniami psychologiczno-pedagogicznymi, placówkami doskonalenia nauczycieli, organizacjami pozarządowymi oraz innymi instytucjami” — § 6 ust. 1 pkt 4 i pkt 6 rozporządzenia MEN z 9 sierpnia 2017 r. (Dz.U. 2017 poz. 1578). Rodzice mają prawo uczestniczyć w opracowaniu i modyfikacji programu oraz w ocenach — § 6 ust. 11; o terminie każdego spotkania zespołu zawiadamia ich dyrektor — § 6 ust. 12; otrzymują kopię WOPF i IPET — § 6 ust. 13."),
  ]);
}

/* ============================================================================
 * STRONA 17 — PLAN WSPÓŁPRACY MIĘDZYSEKTOROWEJ
 * ========================================================================== */
function page17() {
  const bloki = [
    { t: "Szkoła / placówka", c: BRAND.purple, i: [
      "Realizacja IPET i dostosowań na wszystkich zajęciach", "Zajęcia rewalidacyjne i pomoc pp",
      "Monitorowanie postępów i dokumentacja", "Spójne reagowanie na zachowania trudne",
      "Współpraca nauczycieli i specjalistów"] },
    { t: "Rodzina", c: BRAND.orange, i: [
      "Udział w pracach zespołu i współtworzeniu IPET", "Utrwalanie umiejętności w domu",
      "Stały kontakt z wychowawcą / koordynatorem", "Ujednolicenie strategii i systemu nagród",
      "Zgody i wymiana informacji"] },
    { t: "Dziecko", c: BRAND.green, i: [
      "Udział w wyznaczaniu celów („Mój głos”)", "Korzystanie z dostosowań i strategii",
      "Samoocena postępów", "Udział w zajęciach specjalistycznych",
      "Rozwijanie mocnych stron i zainteresowań"] },
    { t: "Podmioty zewnętrzne (PPP, JST, NGO, służba zdrowia)", c: BRAND.teal, i: [
      "Konsultacje z poradnią PPP", "Współpraca ze SCWEW / PDN",
      "Wsparcie organizacji pozarządowych (NGO)", "Współpraca ze służbą zdrowia",
      "Działania organu prowadzącego (JST)"] },
  ];
  const w = Math.floor(CW / 2);
  const mk = (b, width) => new TableCell({
    width: { size: width, type: WidthType.DXA }, borders: allThin,
    verticalAlign: VerticalAlign.TOP, margins: { top: 0, bottom: 0, left: 0, right: 0 },
    children: [
      new Paragraph({ spacing: { after: 0, line: 240 }, shading: { fill: b.c, type: ShadingType.CLEAR, color: "auto" },
        indent: { left: 110, right: 110 },
        children: [r(" " + b.t, { size: 14, bold: true, color: BRAND.white })] }),
      new Paragraph({ spacing: { after: 40 }, children: [] }),
      checkGrid(b.i, 1, { size: 14, width: width - 260 }),
      new Paragraph({ spacing: { after: 60 }, children: [] }),
    ] });

  return page("PLAN WSPÓŁPRACY MIĘDZYSEKTOROWEJ", "IPET · współpraca", [
    numHead(10, "PLAN WSPÓŁPRACY MIĘDZYSEKTOROWEJ"),
    note("Zaznacz działania realizowane przez poszczególnych partnerów. Plan wskazuje podział zadań pomiędzy placówkę, rodzinę, dziecko oraz podmioty zewnętrzne."),
    spacer(60),
    table([w, CW - w], [
      new TableRow({ children: [mk(bloki[0], w), mk(bloki[1], CW - w)] }),
      new TableRow({ children: [mk(bloki[2], w), mk(bloki[3], CW - w)] }),
    ]),
    label("USTALENIA DODATKOWE / OSOBY ODPOWIEDZIALNE I TERMINY"),
    fillBox(4),
  ]);
}

/* ============================================================================
 * STRONA 18 — CZĘŚĆ III: ZESPÓŁ, ZGODA RODZICÓW, EWALUACJA
 * ========================================================================== */
function page18() {
  const w = [520, 2350, 2400, CW - 520 - 2350 - 2400 - 2100, 2100];
  const funkcje = [
    ["Koordynator zespołu", "koordynacja WOPFU i IPET, zwoływanie spotkań"],
    ["Wychowawca grupy", "obserwacja w grupie, spójność działań"],
    ["Pedagog specjalny", "zajęcia rewalidacyjne, dobór dostosowań"],
    ["Psycholog", "diagnoza emocjonalno-społeczna, wsparcie"],
    ["Logopeda / neurologopeda", "zajęcia logopedyczne, komunikacja / AAC"],
    ["Nauczyciel wychowania przedszkolnego", "zajęcia dydaktyczno-wyrównawcze"],
    ["Terapeuta SI / rehabilitant", "terapia zgodnie ze specjalnością"],
    ["Inna funkcja — wpisz", "zakres działań w zespole"],
  ];
  const rows = [ new TableRow({ tableHeader: true, children: [
    th("LP.", w[0], { align: AlignmentType.CENTER }), th("FUNKCJA W ZESPOLE", w[1]),
    th("IMIĘ I NAZWISKO", w[2]), th("ZAKRES DZIAŁAŃ W ZESPOLE", w[3]), th("PODPIS", w[4]) ] }) ];
  funkcje.forEach((f, i) => {
    const fill = i % 2 ? BRAND.paperLt : BRAND.white;
    rows.push(new TableRow({ children: [
      td(String(i + 1), w[0], { align: AlignmentType.CENTER, bold: true, color: BRAND.orange, fill }),
      td(f[0], w[1], { size: 13, fill }),
      td(blankLines(1, { size: 13 }), w[2], { fill }),
      td(f[1], w[3], { size: 12, color: BRAND.mute, fill }),
      td(blankLines(1, { size: 13 }), w[4], { fill }),
    ] }));
  });

  const wZ = Math.floor(CW / 2);
  return page("ZESPÓŁ, ZGODA RODZICÓW I EWALUACJA", "Część III", [
    partTitle("CZĘŚĆ III · ZESPÓŁ, ZATWIERDZENIE I EWALUACJA"),
    numHead(1, "SKŁAD ZESPOŁU OPRACOWUJĄCEGO IPET I WOPF"),
    table(w, rows),

    numHead(2, "OTRZYMANIE KOPII I ZGODA RODZICÓW / OPIEKUNÓW PRAWNYCH"),
    panel([ p([r("„Potwierdzam udział w spotkaniach zespołu oraz odbiór kopii niniejszego programu IPET wraz z arkuszem WOPF. Zostałam/em poinformowany/a o celach, formach wsparcia oraz prawie do wglądu w dokumentację.”",
      { size: 14, italics: true, color: BRAND.ink })], { after: 0, line: 240 }) ],
      { fill: BRAND.paperOr, edgeColor: BRAND.red }),
    spacer(60),
    table([wZ, CW - wZ], [ new TableRow({ children: [
      new TableCell({ width: { size: wZ, type: WidthType.DXA }, borders: allThin,
        margins: { top: 80, bottom: 90, left: 110, right: 110 },
        children: [ cellPara("MIEJSCOWOŚĆ I DATA", { size: 11, bold: true, color: BRAND.mute, cs: 8 }),
          new Paragraph({ spacing: { before: 180, line: 240 },
            border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: BRAND.line, space: 2 } },
            children: [r("", { size: 15 })] }) ] }),
      new TableCell({ width: { size: CW - wZ, type: WidthType.DXA }, borders: allThin,
        margins: { top: 80, bottom: 90, left: 110, right: 110 },
        children: [ cellPara("PODPIS RODZICA / OPIEKUNA", { size: 11, bold: true, color: BRAND.mute, cs: 8 }),
          new Paragraph({ spacing: { before: 180, line: 240 },
            border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: BRAND.line, space: 2 } },
            children: [r("", { size: 15 })] }) ] }),
    ] }) ]),

    numHead(3, "OKRESOWA WIELOSPECJALISTYCZNA OCENA EFEKTYWNOŚCI (EWALUACJA)"),
    new Paragraph({ spacing: { after: 90, line: 250 }, children: [
      r("DATA OCENY:  …… . …… . ………        ", { size: 14, bold: true, color: BRAND.purple }),
      r("Stopień realizacji celów:   ", { size: 14, color: BRAND.ink }),
      r(BOX + " W pełni     " + BOX + " Częściowo     " + BOX + " Brak", { size: 16, bold: true, color: BRAND.orange }) ] }),
    label("WNIOSKI I REKOMENDACJE (MODYFIKACJE)", { before: 40 }),
    fillBox(3),
    spacer(80),
    legal("PODSTAWA PRAWNA — OKRESOWA OCENA EFEKTYWNOŚCI.",
      "„Zespół co najmniej dwa razy w roku szkolnym dokonuje okresowej wielospecjalistycznej oceny poziomu funkcjonowania dziecka, uwzględniając ocenę efektywności programu (…) oraz, w miarę potrzeb, dokonuje modyfikacji programu” — § 6 ust. 9 rozporządzenia MEN z 9 sierpnia 2017 r. (Dz.U. 2017 poz. 1578, z późn. zm.)."),
  ]);
}

/* ============================================================================
 * STRONA 19 — ZAŁĄCZNIKI
 * ========================================================================== */
function page19() {
  const zal = [
    "Harmonogram i zakres ewaluacji",
    "Dostosowania z podziałem na przedmioty i okresowym sprawdzaniem",
    "Szczegółowy plan pracy z rodzicami",
    "Realizacja celów z orzeczenia, KPOF oraz innych",
    "Protokół z posiedzenia zespołu (rekomendacja poziomu wsparcia)",
    "Program zajęć rozwijających kompetencje emocjonalno-społeczne",
    "Program zajęć wspomagających rozwój",
    "Program i tematyka warsztatów oraz konsultacji dla rodziców",
    "Program zajęć logopedycznych",
    "Program rewalidacji — Trening Umiejętności Społecznych (TUS)",
    "Program rewalidacji — Trening Umiejętności Emocjonalnych (TUE)",
    "Program rewalidacji — Trening Umiejętności Komunikacyjnych (TUK)",
    "Program rewalidacji — Trening Funkcjonowania Codziennego (TFC)",
    "Program rewalidacji — Trening orientacji przestrzennej i poruszania się",
    "Program rewalidacji — Rozwijanie komunikowania się (AAC)",
    "Program rewalidacji — Trening rozwoju sensorycznego i motorycznego (SI)",
    "Program rewalidacji — Trening rozwoju funkcji poznawczych",
    "Program rewalidacji — Gimnastyka korekcyjna",
    "Program rewalidacji — Logopedia rewalidacyjna",
    "Program rewalidacji — Terapia ręki",
    "", "",
  ];
  const w = [560, 520, CW - 560 - 520 - 2600, 2600];
  const rows = [ new TableRow({ tableHeader: true, children: [
    th("LP.", w[0], { align: AlignmentType.CENTER }), th("✓", w[1], { align: AlignmentType.CENTER }),
    th("RODZAJ ZAŁĄCZNIKA", w[2]), th("NUMER / DATA", w[3]) ] }) ];
  zal.forEach((z, i) => {
    const fill = i % 2 ? BRAND.paperLt : BRAND.white;
    rows.push(new TableRow({ children: [
      td(String(i + 1), w[0], { align: AlignmentType.CENTER, bold: true, size: 13, color: BRAND.orange, fill }),
      td(BOX, w[1], { align: AlignmentType.CENTER, size: 16, bold: true, color: BRAND.orange, fill }),
      z ? td(z, w[2], { size: 13, fill }) : td(blankLines(1, { size: 13 }), w[2], { fill }),
      td(blankLines(1, { size: 13 }), w[3], { fill }),
    ] }));
  });

  return page("ZAŁĄCZNIKI DO IPET", "Załączniki", [
    numHead(4, "ZAŁĄCZNIKI DO IPET"),
    note("Zaznacz załączniki dołączone do programu i wpisz ich numer oraz datę. Puste wiersze — wpisz dodatkowe załączniki."),
    table(w, rows),
  ]);
}

/* ============================================================================
 * STRONA 20 — RODO
 * ========================================================================== */
function page20() {
  const pkt = [
    ["Administrator danych.", "Administratorem danych osobowych jest szkoła / placówka, do której uczęszcza dziecko, reprezentowana przez dyrektora."],
    ["Inspektor ochrony danych (IOD).", "Kontakt z inspektorem ochrony danych: [adres e-mail / dane kontaktowe IOD]."],
    ["Cel i podstawa prawna.", "Dane przetwarzane są w celu realizacji zadań dydaktycznych, wychowawczych i opiekuńczych oraz organizacji kształcenia specjalnego i pomocy psychologiczno-pedagogicznej — na podstawie art. 6 ust. 1 lit. c i e oraz art. 9 ust. 2 lit. g RODO w związku z ustawą — Prawo oświatowe (obowiązek prawny administratora)."],
    ["Kategorie danych.", "Dokument zawiera dane szczególnej kategorii (dane o zdrowiu, orzeczenia), o których mowa w art. 9 RODO."],
    ["Odbiorcy danych.", "Dane mogą być udostępniane wyłącznie podmiotom uprawnionym na podstawie przepisów prawa (m.in. poradnia psychologiczno-pedagogiczna, organ prowadzący, organ nadzoru)."],
    ["Okres przechowywania.", "Dane przechowywane są przez okres nauki dziecka oraz przez czas wymagany przepisami o archiwizacji dokumentacji przebiegu nauczania."],
    ["Prawa osób.", "Przysługuje prawo dostępu do danych, ich sprostowania i ograniczenia przetwarzania oraz prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych; prawo do usunięcia danych nie przysługuje w zakresie, w jakim przetwarzanie jest niezbędne do wypełnienia obowiązku prawnego (art. 17 ust. 3 lit. b RODO)."],
    ["Bezpieczeństwo.", "Dokument zawiera dane wrażliwe i jest przechowywany w sposób uniemożliwiający dostęp osobom nieupoważnionym."],
  ];
  const kids = [];
  pkt.forEach((x, i) => {
    kids.push(new Paragraph({ spacing: { after: i === pkt.length - 1 ? 0 : 130, line: 240 }, children: [
      r(x[0] + "  ", { size: 14, bold: true, color: BRAND.purple }),
      r(x[1], { size: 14, color: BRAND.ink }) ] }));
  });

  return page("KLAUZULA INFORMACYJNA RODO", "RODO", [
    new Paragraph({ spacing: { before: 160, after: 100 }, children: [
      r("RODO   ", { size: 15, bold: true, color: BRAND.orange, cs: 14 }),
      r("KLAUZULA INFORMACYJNA (RODO)", { size: 18, bold: true, color: BRAND.purple, cs: 4 }) ] }),
    panel(kids),
    spacer(180),
    p([r("IPET 2026 · WOPFU (ICF) · Wzór · EduPlaner 2026", { size: 13, bold: true,
      color: BRAND.mute, cs: 10 })], { align: AlignmentType.CENTER }),
  ]);
}

/* ============================================================================
 * STRONA 21 — KARTA KONTROLNA
 * ========================================================================== */
function page21() {
  const wym = [
    ["§ 6 ust. 1 pkt 1", "Zakres i sposób dostosowania wymagań edukacyjnych (metody i formy pracy)", "Cz. II · sekcja 5 · str. 13"],
    ["§ 6 ust. 1 pkt 2", "Zintegrowane działania nauczycieli i specjalistów", "Sfery 1–6 · str. 7–12"],
    ["§ 6 ust. 1 pkt 3", "Formy i okres udzielania pomocy pp oraz wymiar godzin", "Sekcja 6B · str. 15"],
    ["§ 6 ust. 1 pkt 4", "Działania wspierające rodziców + współdziałanie z poradniami i podmiotami", "Sekcja 9 · str. 16"],
    ["§ 6 ust. 1 pkt 5", "Zajęcia rewalidacyjne (socjoterapeutyczne) i przygotowanie do szkoły", "Sekcje 6A i 5c · str. 13–14"],
    ["§ 6 ust. 1 pkt 6", "Zakres współpracy nauczycieli i specjalistów z rodzicami", "Sekcja 9 · str. 16"],
    ["§ 6 ust. 1 pkt 7", "Dostosowanie warunków organizacji kształcenia + technologie wspomagające", "Sekcja 5b · str. 13"],
    ["§ 6 ust. 1 pkt 8", "Wsparcie dodatkowo zatrudnionej kadry ze szczegółowym uzasadnieniem", "Sekcje 7–8 · str. 16"],
    ["§ 6 ust. 2", "Autyzm / zespół Aspergera: zajęcia rozwijające umiejętności społeczne i komunikacyjne", "Sekcja 6A · str. 14"],
    ["§ 6 ust. 5", "Termin opracowania: do 30 IX albo 30 dni od złożenia orzeczenia", "Cz. III · zespół · str. 18"],
    ["§ 6 ust. 9", "WOPF i okresowa ocena efektywności co najmniej 2× w roku szkolnym", "Cz. I · str. 3–4 i Cz. III · str. 18"],
    ["§ 6 ust. 11–13", "Prawa rodziców: udział w pracach, zawiadomienie o spotkaniach, kopia WOPFU i IPET", "Cz. III · str. 18"],
    ["nowy model", "„Mój głos” — perspektywa i udział dziecka  ✦ NOWE 26/27", "str. 2"],
    ["nowy model", "Ocena funkcjonalna KPOF / ICF i poziomy wsparcia I–III  ✦ NOWE 26/27", "str. 5, 7–12"],
    ["nowy model", "Projektowanie uniwersalne (UDL) w dostosowaniach  ✦ NOWE 26/27", "str. 13"],
    ["nowy model", "Plan współpracy międzysektorowej  ✦ NOWE 26/27", "str. 17"],
  ];
  const w = [1700, CW - 1700 - 2500 - 800, 2500, 800];
  const rows = [ new TableRow({ tableHeader: true, children: [
    th("PODSTAWA", w[0]), th("WYMAGANY ELEMENT PROGRAMU", w[1]),
    th("GDZIE W DOKUMENCIE", w[2]), th("UJĘTE", w[3], { align: AlignmentType.CENTER }) ] }) ];
  wym.forEach((x, i) => {
    const nowy = x[0] === "nowy model";
    const fill = nowy ? BRAND.paperOr : (i % 2 ? BRAND.paperLt : BRAND.white);
    rows.push(new TableRow({ children: [
      td(x[0], w[0], { size: 12, bold: true, color: nowy ? BRAND.red : BRAND.amber, fill }),
      td(x[1], w[1], { size: 12, fill }),
      td(x[2], w[2], { size: 12, color: BRAND.mute, fill }),
      td(BOX, w[3], { align: AlignmentType.CENTER, size: 17, bold: true, color: BRAND.orange, fill }),
    ] }));
  });

  const wB = [560, CW - 560 - 1700 - 2200 - 1500, 1700, 2200, 1500];
  const brakiRows = [ new TableRow({ tableHeader: true, children: [
    th("LP.", wB[0], { align: AlignmentType.CENTER }),
    th("STWIERDZONY BRAK / ELEMENT DO UZUPEŁNIENIA", wB[1]),
    th("TERMIN WYKONANIA", wB[2]), th("ODPOWIEDZIALNY", wB[3]),
    th("STATUS", wB[4], { align: AlignmentType.CENTER }) ] }) ];
  for (let i = 1; i <= 4; i++) {
    const fill = i % 2 === 0 ? BRAND.paperLt : BRAND.white;
    brakiRows.push(new TableRow({ children: [
      td(String(i), wB[0], { align: AlignmentType.CENTER, bold: true, color: BRAND.orange, fill }),
      td(blankLines(1, { size: 13 }), wB[1], { fill }),
      td(blankLines(1, { size: 13 }), wB[2], { fill }),
      td(blankLines(1, { size: 13 }), wB[3], { fill }),
      td(BOX + " wykonano", wB[4], { align: AlignmentType.CENTER, size: 13, color: BRAND.orange, bold: true, fill }),
    ] }));
  }

  const wS2 = Math.floor(CW / 2);
  return page("KARTA KONTROLNA ZGODNOŚCI IPET", "Karta kontrolna", [
    partTitle("ROZLICZENIE WYMOGÓW ROZPORZĄDZENIA"),
    numHead(5, "KARTA KONTROLNA — CZY IPET ZAWIERA WSZYSTKIE WYMAGANE ELEMENTY?"),
    note("Przed zatwierdzeniem programu zespół sprawdza i odhacza każdy wymóg § 6 rozporządzenia MEN z 9 VIII 2017 r. (Dz.U. poz. 1578 ze zm.). Wiersze ze znaczkiem „nowe 26/27” to elementy nowego modelu oceny funkcjonalnej — wykraczają ponad minimum prawne."),
    table(w, rows),
    numHead(6, "PODSUMOWANIE WERYFIKACJI — BRAKI I TERMINY"),
    table(wB, brakiRows),
    spacer(140),
    table([wS2, CW - wS2], [ new TableRow({ children: [
      new TableCell({ width: { size: wS2, type: WidthType.DXA }, borders: allThin,
        margins: { top: 80, bottom: 90, left: 110, right: 110 },
        children: [ cellPara("DATA WERYFIKACJI", { size: 11, bold: true, color: BRAND.mute, cs: 8 }),
          new Paragraph({ spacing: { before: 170, line: 240 },
            border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: BRAND.line, space: 2 } },
            children: [r("", { size: 15 })] }) ] }),
      new TableCell({ width: { size: CW - wS2, type: WidthType.DXA }, borders: allThin,
        margins: { top: 80, bottom: 90, left: 110, right: 110 },
        children: [ cellPara("PODPIS KOORDYNATORA ZESPOŁU", { size: 11, bold: true, color: BRAND.mute, cs: 8 }),
          new Paragraph({ spacing: { before: 170, line: 240 },
            border: { bottom: { style: BorderStyle.DOTTED, size: 4, color: BRAND.line, space: 2 } },
            children: [r("", { size: 15 })] }) ] }),
    ] }) ]),
  ], true);
}

/* ============================================================================
 * STOPKA
 * ========================================================================== */
function makeFooter() {
  return new Footer({ children: [ new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
    border: { top: { style: BorderStyle.SINGLE, size: 6, color: BRAND.line, space: 5 } },
    spacing: { before: 50, line: 220 },
    children: [
      r("EduPlaner 2026 · PCTP · pedagog specjalny mgr Mirosława Ewa Jurczyszyn", { size: 12, color: BRAND.mute }),
      r("\tStrona ", { size: 12, color: BRAND.mute }),
      new TextRun({ children: [PageNumber.CURRENT], font: F, size: 12, bold: true, color: BRAND.purple }),
      r(" z ", { size: 12, color: BRAND.mute }),
      new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F, size: 12, color: BRAND.mute }),
    ] }) ] });
}

/* ============================================================================
 * MONTAŻ DOKUMENTU
 * ========================================================================== */
const body = [
  ...page01(), ...page02(), ...page03(), ...page04(), ...page05(), ...page06(),
  ...SFERY.flatMap((s, i) => pageSfera(s, i)),
  ...page13(), ...page14(), ...page15(), ...page16(), ...page17(),
  ...page18(), ...page19(), ...page20(), ...page21(),
];

const doc = new Document({
  creator: "EduPlaner 2026 · PCTP Koszalin",
  title: "IPET 2026 · WOPF (ICF) — druk (wersja przedszkolna)",
  description: "Druk IPET 2026 · WOPF/ICF · 21 stron · ekosystem EduPlaner2026-MJ-PCTP",
  styles: { default: { document: { run: { font: F, size: 18, color: BRAND.ink } } } },
  sections: [{
    properties: { page: { size: { width: PAGE_W, height: PAGE_H }, margin: MAR } },
    footers: { default: makeFooter() },
    children: body,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(OUT_PATH, buf);
  console.log("✓ Zapisano: " + OUT_PATH + "  (" + (buf.length / 1024).toFixed(1) + " KB)");
});
