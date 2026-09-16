const S = require("../styl.js");
const W = require("../wspolne.js");
const { TableRow } = require("docx");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-09",
  plik: "NP-09_Ewaluacja_wewnetrzna_projekt_i_harmonogram.docx",
  tytul: "Ewaluacja wewnętrzna — projekt i harmonogram",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Ewaluacja wewnętrzna · planowanie badania",
      tytul: "Projekt ewaluacji wewnętrznej",
      podtytul: "przedmiot, pytania kluczowe, narzędzia i harmonogram  ·  rok szkolny ................ / ................",
    }));

    d.push(W.metryczka2([
      ["Placówka", "Rok szkolny"],
      ["Przedmiot ewaluacji", "Kierownik zespołu"],
    ]));

    /* I */
    d.push(S.sekcja("I", "Przedmiot i uzasadnienie wyboru"));
    d.push(...S.poleOpisowe("Przedmiot ewaluacji", 2));
    d.push(S.etykieta("Dlaczego ten obszar — źródło wyboru"));
    d.push(...S.kratki([
      "wnioski z nadzoru pedagogicznego za poprzedni rok szkolny",
      "wnioski z obserwacji zajęć i kontroli dokumentacji",
      "potrzeby zgłoszone przez nauczycieli, rodziców lub uczniów",
      "kierunki polityki oświatowej państwa",
      "zmiana organizacyjna w placówce (nowe oddziały, nowa kadra, nowe zajęcia)",
      "inne: ..............................................................................................................",
    ]));

    /* II */
    d.push(S.sekcja("II", "Cele ewaluacji"));
    d.push(...S.poleOpisowe("Cel główny", 2));
    d.push(...S.poleOpisowe("Cele szczegółowe", 3));

    /* III */
    d.push(S.sekcja("III", "Pytania kluczowe, kryteria i wskaźniki"));
    d.push(W.pustaTabelaLp(
      ["Lp.", "Pytanie kluczowe", "Kryterium — co uznamy za dobry wynik", "Wskaźnik / dane"],
      [520, 3400, 3100, C - 7020], 5, 160
    ));

    /* IV */
    d.push(S.nowaStrona());
    d.push(S.sekcja("IV", "Metody, narzędzia i próba badawcza"));
    {
      const w = [2100, 2100, 2100, 1200, C - 7500];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Metoda", w[0]), S.naglowekKom("Narzędzie", w[1]),
        S.naglowekKom("Respondenci / źródło", w[2]), S.naglowekKom("Liczba", w[3]),
        S.naglowekKom("Termin i odpowiedzialny", w[4]),
      ]})];
      const start = [
        ["Ankieta", "Kwestionariusz (druk NP-10)", "Nauczyciele", "", ""],
        ["Ankieta", "Kwestionariusz (druk NP-10)", "Rodzice", "", ""],
        ["Analiza dokumentów", "Arkusz analizy", "IPET, WOPF, dzienniki", "", ""],
        ["Wywiad", "Dyspozycje do wywiadu", "Specjaliści", "", ""],
        ["Obserwacja", "Arkusz obserwacji", "Zajęcia", "", ""],
      ];
      start.forEach((r, i) => rows.push(new TableRow({ children: r.map((t, j) =>
        S.cell(t, { width: w[j], size: 16, padTop: 120, padBottom: 120, bg: i % 2 ? S.BRAND.paper : undefined })
      )})));
      for (let i = 0; i < 2; i++) rows.push(new TableRow({ children: w.map((ww) => S.cell("", { width: ww, padTop: 130, padBottom: 130 })) }));
      d.push(S.tabela(rows, w));
    }
    d.push(S.para("Wiersze wstępne są propozycją — skreśl lub zastąp metodami właściwymi dla swojego badania.", { size: 14, italic: true, color: S.BRAND.muted }));

    d.push(...S.pudelko(
      "W placówce kształcenia specjalnego dobierz narzędzia także do możliwości uczniów: wersja ankiety z symbolami lub skalą obrazkową, wywiad wspierany AAC, obserwacja zamiast kwestionariusza.",
      { bg: S.BRAND.orangeMist, accent: S.BRAND.orange, color: S.BRAND.ink, size: 15 }
    ));

    /* V */
    d.push(S.sekcja("V", "Harmonogram ewaluacji"));
    {
      const w = [2900, 3300, 1600, C - 7800];
      const etapy = [
        "Opracowanie projektu ewaluacji",
        "Opracowanie i konsultacja narzędzi",
        "Zbieranie danych",
        "Analiza i opracowanie wyników",
        "Sporządzenie raportu",
        "Prezentacja radzie pedagogicznej",
        "Wdrożenie wniosków i monitorowanie",
      ];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Etap", w[0]), S.naglowekKom("Zadania szczegółowe", w[1]),
        S.naglowekKom("Termin", w[2]), S.naglowekKom("Odpowiedzialny", w[3]),
      ]})];
      etapy.forEach((e, i) => rows.push(new TableRow({ children: [
        S.cell(e, { width: w[0], size: 16, bold: true, color: S.BRAND.purple, bg: i % 2 ? S.BRAND.paper : undefined, padTop: 130, padBottom: 130 }),
        S.cell("", { width: w[1], bg: i % 2 ? S.BRAND.paper : undefined, padTop: 130, padBottom: 130 }),
        S.cell("", { width: w[2], bg: i % 2 ? S.BRAND.paper : undefined, padTop: 130, padBottom: 130 }),
        S.cell("", { width: w[3], bg: i % 2 ? S.BRAND.paper : undefined, padTop: 130, padBottom: 130 }),
      ]})));
      d.push(S.tabela(rows, w));
    }

    /* VI */
    d.push(S.nowaStrona());
    d.push(S.sekcja("VI", "Zespół ewaluacyjny"));
    d.push(W.pustaTabelaLp(["Lp.", "Imię i nazwisko", "Funkcja w placówce", "Zadania w badaniu"], [520, 2600, 2400, C - 5520], 5));

    /* VII */
    d.push(S.sekcja("VII", "Upowszechnienie i wykorzystanie wyników"));
    d.push(S.etykieta("Sposób przedstawienia wyników"));
    d.push(...S.kratki([
      "raport przedstawiony radzie pedagogicznej — termin: ...........................",
      "informacja dla rodziców (zebranie, strona internetowa, tablica)",
      "informacja dla uczniów w formie dostosowanej do ich możliwości",
      "wnioski wpisane do planu nadzoru na kolejny rok szkolny",
    ]));
    d.push(S.poleLinia("Sposób monitorowania wdrożenia wniosków"));
    d.push(...S.linie(2));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor]));
    d.push(...S.blokPodpisow(["Dyrektor placówki", "Kierownik zespołu ewaluacyjnego"]));
    return d;
  },
};
