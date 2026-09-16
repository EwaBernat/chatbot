const S = require("../styl.js");
const W = require("../wspolne.js");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-12",
  plik: "NP-12_Karta_wspomagania_i_doskonalenia_nauczyciela.docx",
  tytul: "Karta wspomagania i doskonalenia nauczyciela",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Wspomaganie · forma nadzoru",
      tytul: "Karta wspomagania i doskonalenia nauczyciela",
      podtytul: "diagnoza potrzeb, indywidualny plan rozwoju i jego podsumowanie  ·  rok szkolny ................ / ................",
    }));

    d.push(W.metryczka2([
      ["Nauczyciel", "Stopień awansu zawodowego"],
      ["Prowadzone zajęcia / stanowisko", "Staż pracy"],
      ["Opiekun / mentor (jeśli wyznaczono)", "Data sporządzenia karty"],
    ]));

    /* I */
    d.push(S.sekcja("I", "Diagnoza potrzeb rozwojowych"));
    d.push(S.etykieta("Źródła diagnozy — zaznacz wykorzystane"));
    d.push(...S.kratki([
      "obserwacja zajęć (druki NP-03 / NP-04 / NP-05) — data: ............................",
      "rozmowa pohospitacyjna (druk NP-06)",
      "samoocena nauczyciela",
      "wnioski z kontroli dokumentacji (druk NP-07 / NP-08)",
      "wnioski z ewaluacji wewnętrznej (druk NP-11)",
      "wnioski z oceny pracy",
      "zgłoszenie własne nauczyciela",
    ]));
    {
      const w = [Math.floor(C / 2), C - Math.floor(C / 2)];
      const { TableRow } = require("docx");
      d.push(S.tabela([
        new TableRow({ tableHeader: true, children: [
          S.naglowekKom("Mocne strony warsztatu", w[0]),
          S.naglowekKom("Zdiagnozowane potrzeby", w[1]),
        ]}),
        new TableRow({ children: [
          S.cell("", { width: w[0], padTop: 800, padBottom: 800 }),
          S.cell("", { width: w[1], padTop: 800, padBottom: 800 }),
        ]}),
      ], w));
    }

    /* II */
    d.push(S.sekcja("II", "Indywidualny plan rozwoju na rok szkolny"));
    d.push(W.pustaTabelaLp(
      ["Lp.", "Cel rozwojowy", "Działanie nauczyciela", "Wsparcie ze strony placówki", "Termin", "Wskaźnik osiągnięcia"],
      [520, 2100, 2100, 2100, 1100, C - 7920], 5, 160
    ));
    d.push(...S.pudelko(
      "Cel rozwojowy zapisz tak, by dało się sprawdzić jego osiągnięcie: nie „doskonalenie warsztatu”, lecz np. „stosuję wizualny plan dnia w każdej jednostce zajęć; sprawdzenie: obserwacja w marcu”.",
      { before: 120 }
    ));

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Zrealizowane formy doskonalenia i wspomagania"));
    d.push(W.pustaTabelaLp(
      ["Lp.", "Forma", "Temat", "Organizator", "Data", "Liczba godzin"],
      [520, 1900, 2800, 2000, 1300, C - 8520], 7, 120
    ));
    d.push(S.etykieta("Formy wspomagania zapewnione przez placówkę"));
    d.push(...S.kratki([
      "szkoleniowa rada pedagogiczna",
      "obserwacja koleżeńska / lekcja otwarta",
      "mentoring lub opieka nauczyciela doświadczonego",
      "konsultacje ze specjalistami placówki",
      "udostępnienie materiałów, pomocy, literatury",
      "sfinansowanie lub dofinansowanie doskonalenia zewnętrznego",
      "zmiana organizacji pracy (przydział zajęć, warunki, wsparcie w oddziale)",
    ]));

    /* IV */
    d.push(S.sekcja("IV", "Wykorzystanie zdobytej wiedzy w praktyce"));
    d.push(...S.poleOpisowe("Co zmieniło się w pracy nauczyciela — konkretne przykłady", 4));
    d.push(...S.poleOpisowe("Dzielenie się wiedzą z innymi nauczycielami (formy, terminy)", 3));

    /* V */
    d.push(S.sekcja("V", "Podsumowanie roczne"));
    {
      const w = [4600, 1600, C - 6200];
      const { TableRow } = require("docx");
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Cel rozwojowy z planu", w[0]),
        S.naglowekKom("Osiągnięty (T / Cz / N)", w[1]),
        S.naglowekKom("Dowód / uzasadnienie", w[2]),
      ]})];
      for (let i = 0; i < 5; i++)
        rows.push(new TableRow({ children: w.map((ww) => S.cell("", { width: ww, padTop: 150, padBottom: 150, bg: i % 2 ? S.BRAND.paper : undefined })) }));
      d.push(S.tabela(rows, w));
    }
    d.push(...S.poleOpisowe("Wnioski dyrektora i kierunki wspomagania na kolejny rok", 3));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.kartaNauczyciela]));
    d.push(...W.klauzula());
    d.push(...S.blokPodpisow(["Dyrektor placówki", "Nauczyciel"]));
    return d;
  },
};
