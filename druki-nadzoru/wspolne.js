/* ============================================================================
 * wspolne.js — elementy powtarzalne wszystkich druków nadzoru
 * ========================================================================== */
const S = require("./styl.js");
const { TableRow } = require("docx");

const MODUL = "Nadzór pedagogiczny";

/* ---- podstawy prawne (teksty do cytowania w drukach) ------------------ */
const P = {
  prawoOswiatowe:
    "Ustawa z dnia 14 grudnia 2016 r. — Prawo oświatowe, art. 55–60 (nadzór pedagogiczny) oraz art. 68 ust. 1 pkt 2 (dyrektor sprawuje nadzór pedagogiczny).",
  nadzor:
    "Rozporządzenie Ministra Edukacji Narodowej z dnia 25 sierpnia 2017 r. w sprawie nadzoru pedagogicznego (ze zm.) — formy nadzoru dyrektora: ewaluacja wewnętrzna, kontrola przestrzegania przepisów prawa, wspomaganie nauczycieli, monitorowanie pracy szkoły.",
  planTermin:
    "Rozporządzenie w sprawie nadzoru pedagogicznego — plan nadzoru dyrektor przedstawia radzie pedagogicznej w terminie do 15 września roku szkolnego, którego dotyczy plan.",
  sprawozdanieTermin:
    "Rozporządzenie w sprawie nadzoru pedagogicznego — wyniki i wnioski ze sprawowanego nadzoru dyrektor przedstawia radzie pedagogicznej w terminie do 31 sierpnia.",
  radaPed:
    "Ustawa — Prawo oświatowe, art. 69 ust. 7: dyrektor przedstawia radzie pedagogicznej, nie rzadziej niż dwa razy w roku szkolnym, ogólne wnioski ze sprawowanego nadzoru pedagogicznego oraz informacje o działalności szkoły.",
  ksztalcenieSpecjalne:
    "Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym (ze zm.) — IPET, WOPF, zajęcia rewalidacyjne.",
  pomocPP:
    "Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej w publicznych przedszkolach, szkołach i placówkach (ze zm.).",
  dokumentacja:
    "Rozporządzenie Ministra Edukacji Narodowej z dnia 25 sierpnia 2017 r. w sprawie sposobu prowadzenia przez publiczne przedszkola, szkoły i placówki dokumentacji przebiegu nauczania, działalności wychowawczej i opiekuńczej oraz rodzajów tej dokumentacji (ze zm.).",
  kartaNauczyciela:
    "Ustawa z dnia 26 stycznia 1982 r. — Karta Nauczyciela, art. 6, 6a i 7 (obowiązki nauczyciela, ocena pracy, zadania dyrektora).",
  ocenaPracy:
    "Rozporządzenie Ministra Edukacji i Nauki z dnia 25 sierpnia 2022 r. w sprawie oceny pracy nauczycieli (ze zm.) — kryteria obowiązkowe i dodatkowe.",
  bhp:
    "Rozporządzenie Ministra Edukacji Narodowej i Sportu z dnia 31 grudnia 2002 r. w sprawie bezpieczeństwa i higieny w publicznych i niepublicznych szkołach i placówkach (ze zm.).",
  rodo:
    "Rozporządzenie Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. (RODO) — dane zawarte w druku są danymi osobowymi, w tym danymi o stanie zdrowia ucznia.",
  uwaga:
    "Uwaga: przed wdrożeniem druku zweryfikuj aktualny tekst jednolity przywołanych aktów prawnych (Dz.U.) oraz zapisy statutu placówki.",
};

const podstawy = (poz, o = {}) => S.podstawaPrawna([...poz, P.uwaga], o);

/* ---- metryczka: tabela dwukolumnowa etykieta | pole ------------------- */
function metryczka(pozycje) {
  const W = [2900, S.CONTENT_W - 2900];
  return S.tabela(
    pozycje.map((label) => S.wierszPola(label, W)),
    W
  );
}

/* metryczka dwukolumnowa (4 pola w 2 kolumnach) — oszczędza miejsce */
function metryczka2(pary) {
  const w = [2300, 2573, 2300, 2573];
  const rows = pary.map(([a, b]) =>
    new TableRow({
      children: [
        S.cell(a, { width: w[0], bg: S.BRAND.purpleMist, bold: true, size: 15, color: S.BRAND.purple, caps: true }),
        S.cell("", { width: w[1], padTop: 105, padBottom: 105 }),
        S.cell(b || "", { width: w[2], bg: b ? S.BRAND.purpleMist : undefined, bold: true, size: 15, color: S.BRAND.purple, caps: true }),
        S.cell("", { width: w[3], padTop: 105, padBottom: 105 }),
      ],
    })
  );
  return S.tabela(rows, w);
}

/* ---- skala ocen stosowana w arkuszach obserwacji ---------------------- */
const SKALA = ["A — w pełni", "B — w znacznym stopniu", "C — częściowo", "D — nie zaobserwowano", "nd."];

/* tabela kryteriów z kolumnami skali A–D + nd. */
function tabelaKryteriow(naglowekKryterium, kryteria) {
  const wK = 5306;
  const wS = 800; // 5 kolumn skali = 4000
  const w = [wK, wS, wS, wS, wS, S.CONTENT_W - wK - 4 * wS];
  const rows = [
    new TableRow({
      tableHeader: true,
      children: [
        S.naglowekKom(naglowekKryterium, w[0]),
        S.naglowekKom("A", w[1], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("B", w[2], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("C", w[3], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("D", w[4], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("nd.", w[5], { align: S.AlignmentType.CENTER }),
      ],
    }),
  ];
  kryteria.forEach((k, i) => {
    rows.push(
      new TableRow({
        children: [
          S.cell(k, { width: w[0], size: 17, bg: i % 2 ? S.BRAND.paper : undefined }),
          ...[1, 2, 3, 4, 5].map((c) =>
            S.cell(S.KRATKA, {
              width: w[c], align: S.AlignmentType.CENTER, size: 20,
              color: S.BRAND.orange, bg: i % 2 ? S.BRAND.paper : undefined, vAlign: "center",
            })
          ),
        ],
      })
    );
  });
  return S.tabela(rows, w);
}

/* legenda skali pod tabelą kryteriów */
const legendaSkali = () =>
  S.para(
    "Skala: A — spełnione w pełni · B — spełnione w znacznym stopniu · C — spełnione częściowo · D — nie zaobserwowano · nd. — nie dotyczy",
    { size: 14, italic: true, color: S.BRAND.muted, before: 70, after: 120 }
  );

/* ---- klauzula RODO na końcu druku ------------------------------------ */
const klauzula = (tekst) =>
  S.pudelko(
    tekst ||
      "Druk zawiera dane osobowe. Przechowuj go w dokumentacji nadzoru pedagogicznego prowadzonej przez dyrektora, udostępniaj wyłącznie osobom upoważnionym, zgodnie z polityką ochrony danych osobowych placówki (RODO).",
    { bg: S.BRAND.orangeMist, accent: S.BRAND.amber, color: S.BRAND.ink, size: 15, before: 200 }
  );


/* ---- tabela z pustymi wierszami (skrót używany w drukach) ------------- */
function pustaTabela(naglowki, w, n = 5, pad = 140) {
  const rows = [new TableRow({ tableHeader: true, children: naglowki.map((h, i) => S.naglowekKom(h, w[i])) })];
  for (let i = 0; i < n; i++)
    rows.push(new TableRow({
      children: w.map((ww, j) =>
        S.cell("", { width: ww, padTop: pad, padBottom: pad, bg: i % 2 ? S.BRAND.paper : undefined })
      ),
    }));
  return S.tabela(rows, w);
}

/* tabela z pustymi wierszami i numeracją w pierwszej kolumnie */
function pustaTabelaLp(naglowki, w, n = 5, pad = 140) {
  const rows = [new TableRow({ tableHeader: true, children: naglowki.map((h, i) => S.naglowekKom(h, w[i])) })];
  for (let i = 1; i <= n; i++)
    rows.push(new TableRow({
      children: w.map((ww, j) =>
        S.cell(j === 0 ? String(i) : "", {
          width: ww, align: j === 0 ? S.AlignmentType.CENTER : undefined,
          bold: j === 0, color: j === 0 ? S.BRAND.orange : undefined,
          padTop: pad, padBottom: pad, bg: i % 2 ? undefined : S.BRAND.paper,
        })
      ),
    }));
  return S.tabela(rows, w);
}


/* ---- tabela kontrolna TAK / NIE / ND z miejscem na uwagi -------------- */
function tabelaKontrolna(pozycje, o = {}) {
  const wLp = 520, wEl = o.wEl || 4500, wTak = 620, wNie = 620, wNd = 620;
  const wUw = S.CONTENT_W - wLp - wEl - wTak - wNie - wNd;
  const w = [wLp, wEl, wTak, wNie, wNd, wUw];
  const rows = [
    new TableRow({
      tableHeader: true,
      children: [
        S.naglowekKom("Lp.", w[0]),
        S.naglowekKom(o.naglowek || "Sprawdzany element", w[1]),
        S.naglowekKom("Tak", w[2], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("Nie", w[3], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("nd.", w[4], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("Uwagi", w[5]),
      ],
    }),
  ];
  let lp = 0;
  pozycje.forEach((poz) => {
    if (typeof poz === "object" && poz.grupa) {
      rows.push(new TableRow({
        children: [
          S.cell(poz.grupa.toUpperCase(), {
            width: S.CONTENT_W, span: 6, bg: S.BRAND.purpleMist,
            bold: true, size: 15, color: S.BRAND.purple, padTop: 70, padBottom: 70,
          }),
        ],
      }));
      return;
    }
    lp += 1;
    const bg = lp % 2 ? undefined : S.BRAND.paper;
    rows.push(new TableRow({
      children: [
        S.cell(String(lp), { width: w[0], align: S.AlignmentType.CENTER, bold: true, color: S.BRAND.orange, bg, padTop: 95, padBottom: 95 }),
        S.cell(poz, { width: w[1], size: 16, bg, padTop: 95, padBottom: 95 }),
        S.cell(S.KRATKA, { width: w[2], align: S.AlignmentType.CENTER, size: 19, color: S.BRAND.orange, bg, vAlign: "center" }),
        S.cell(S.KRATKA, { width: w[3], align: S.AlignmentType.CENTER, size: 19, color: S.BRAND.orange, bg, vAlign: "center" }),
        S.cell(S.KRATKA, { width: w[4], align: S.AlignmentType.CENTER, size: 19, color: S.BRAND.orange, bg, vAlign: "center" }),
        S.cell("", { width: w[5], bg }),
      ],
    }));
  });
  return S.tabela(rows, w);
}

module.exports = { MODUL, tabelaKontrolna, pustaTabela, pustaTabelaLp, P, podstawy, metryczka, metryczka2, SKALA, tabelaKryteriow, legendaSkali, klauzula };
