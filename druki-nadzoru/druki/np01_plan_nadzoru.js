const S = require("../styl.js");
const W = require("../wspolne.js");
const { TableRow } = require("docx");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-01",
  plik: "NP-01_Plan_nadzoru_pedagogicznego.docx",
  tytul: "Plan nadzoru pedagogicznego",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Planowanie · dyrektor szkoły",
      tytul: "Plan nadzoru pedagogicznego",
      podtytul: "na rok szkolny ................ / ................  ·  szkoła specjalna / placówka kształcenia specjalnego",
    }));

    d.push(W.metryczka2([
      ["Placówka", "Rok szkolny"],
      ["Dyrektor", "Wicedyrektor / osoba wspierająca"],
      ["Data przedstawienia radzie pedagogicznej", "Nr protokołu rady pedagogicznej"],
    ]));
    d.push(...S.pudelko(
      "Plan przedstaw radzie pedagogicznej do 15 września roku szkolnego, którego dotyczy. Plan obejmuje cztery formy nadzoru: ewaluację wewnętrzną, kontrolę przestrzegania przepisów prawa, wspomaganie nauczycieli i monitorowanie pracy placówki.",
      { before: 140 }
    ));

    /* I */
    d.push(S.sekcja("I", "Cele nadzoru w roku szkolnym"));
    d.push(...S.poleOpisowe("Cel główny", 2));
    d.push(S.etykieta("Cele szczegółowe — zaznacz i uzupełnij"));
    d.push(...S.kratki([
      "Podniesienie jakości kształcenia specjalnego i skuteczności realizacji IPET.",
      "Doskonalenie wielospecjalistycznej oceny poziomu funkcjonowania ucznia (WOPF) i jej wykorzystania.",
      "Zwiększenie skuteczności zajęć rewalidacyjnych i specjalistycznych.",
      "Poprawa współpracy z rodzicami i instytucjami wspierającymi.",
      "Bezpieczeństwo uczniów i respektowanie norm społecznych.",
      "Realizacja kierunków polityki oświatowej państwa ustalonych przez ministra.",
    ]));
    d.push(...S.linie(2));

    /* II */
    d.push(S.sekcja("II", "Wnioski z nadzoru za poprzedni rok szkolny przyjęte do realizacji"));
    {
      const w = [640, 4200, 3106, 1800];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Lp.", w[0]), S.naglowekKom("Wniosek z poprzedniego roku", w[1]),
        S.naglowekKom("Sposób uwzględnienia w tym planie", w[2]), S.naglowekKom("Odpowiedzialny", w[3]),
      ]})];
      for (let i = 1; i <= 4; i++) rows.push(new TableRow({ children: [
        S.cell(String(i), { width: w[0], align: S.AlignmentType.CENTER, bold: true, color: S.BRAND.orange, padTop: 150, padBottom: 150 }),
        S.cell("", { width: w[1], padTop: 150, padBottom: 150 }),
        S.cell("", { width: w[2], padTop: 150, padBottom: 150 }),
        S.cell("", { width: w[3], padTop: 150, padBottom: 150 }),
      ]}));
      d.push(S.tabela(rows, w));
    }

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Ewaluacja wewnętrzna"));
    {
      const w = [3000, C - 3000];
      const pola = [
        "Przedmiot ewaluacji", "Cel ewaluacji", "Pytania kluczowe", "Kryteria ewaluacji",
        "Metody i narzędzia", "Próba badawcza (kto / ile osób)", "Zespół ewaluacyjny",
        "Termin przeprowadzenia", "Termin przedstawienia raportu",
      ];
      d.push(S.tabela(pola.map((p) => S.wierszPola(p, w, { pad: 150 })), w));
    }
    d.push(...S.pudelko(
      "W szkole specjalnej przedmiotem ewaluacji może być m.in.: skuteczność celów SMART w IPET, wykorzystanie WOPF w planowaniu zajęć, spójność oddziaływań zespołu, współpraca z rodzicami, adaptacja ucznia nowo przyjętego.",
      { bg: S.BRAND.orangeMist, accent: S.BRAND.orange, color: S.BRAND.ink, size: 15 }
    ));

    /* IV */
    d.push(S.sekcja("IV", "Kontrola przestrzegania przepisów prawa"));
    {
      const w = [520, 3200, 2400, 1900, 1726];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Lp.", w[0]), S.naglowekKom("Tematyka kontroli", w[1]),
        S.naglowekKom("Zakres / dokumentacja", w[2]), S.naglowekKom("Kto objęty kontrolą", w[3]),
        S.naglowekKom("Termin", w[4]),
      ]})];
      const przyklady = [
        ["Prowadzenie dzienników zajęć i dokumentacji przebiegu nauczania", "Dzienniki lekcyjne, dzienniki zajęć specjalistycznych", "", "", ],
        ["Zgodność IPET z orzeczeniem o potrzebie kształcenia specjalnego", "IPET, WOPF, orzeczenia", "", ""],
        ["Realizacja godzin zajęć rewalidacyjnych i pomocy p-p", "Arkusz organizacji, dzienniki", "", ""],
      ];
      przyklady.forEach((p, i) => rows.push(new TableRow({ children: [
        S.cell(String(i + 1), { width: w[0], align: S.AlignmentType.CENTER, bold: true, color: S.BRAND.orange, padTop: 130, padBottom: 130 }),
        S.cell(p[0], { width: w[1], size: 16, padTop: 130, padBottom: 130 }),
        S.cell(p[1], { width: w[2], size: 16, padTop: 130, padBottom: 130 }),
        S.cell("", { width: w[3], padTop: 130, padBottom: 130 }),
        S.cell("", { width: w[4], padTop: 130, padBottom: 130 }),
      ]})));
      for (let i = 4; i <= 7; i++) rows.push(new TableRow({ children: w.map((ww, j) =>
        S.cell(j === 0 ? String(i) : "", { width: ww, align: j === 0 ? S.AlignmentType.CENTER : undefined, bold: j === 0, color: j === 0 ? S.BRAND.orange : undefined, padTop: 130, padBottom: 130, bg: S.BRAND.paper })
      )}));
      d.push(S.tabela(rows, w));
    }
    d.push(S.para("Wiersze 1–3 to propozycje typowe dla kształcenia specjalnego — skreśl lub zastąp własną tematyką.", { size: 14, italic: true, color: S.BRAND.muted, after: 60 }));

    /* V */
    d.push(S.nowaStrona());
    d.push(S.sekcja("V", "Plan obserwacji zajęć"));
    {
      const w = [520, 2300, 2300, 2500, 2126];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Lp.", w[0]), S.naglowekKom("Nauczyciel", w[1]), S.naglowekKom("Rodzaj zajęć", w[2]),
        S.naglowekKom("Cel obserwacji / tematyka", w[3]), S.naglowekKom("Termin i druk", w[4]),
      ]})];
      for (let i = 1; i <= 10; i++) rows.push(new TableRow({ children: w.map((ww, j) =>
        S.cell(j === 0 ? String(i) : "", { width: ww, align: j === 0 ? S.AlignmentType.CENTER : undefined, bold: j === 0, color: j === 0 ? S.BRAND.orange : undefined, padTop: 125, padBottom: 125, bg: i % 2 ? undefined : S.BRAND.paper })
      )}));
      d.push(S.tabela(rows, w));
    }
    d.push(S.para("Druki obserwacji: NP-03 (zajęcia dydaktyczne), NP-04 (zajęcia rewalidacyjne i specjalistyczne), NP-05 (obserwacja diagnozująca), NP-06 (rozmowa pohospitacyjna).", { size: 14, italic: true, color: S.BRAND.muted }));

    /* VI */
    d.push(S.sekcja("VI", "Wspomaganie nauczycieli"));
    {
      const w = [2400, 2600, 2400, 2346];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Zdiagnozowana potrzeba", w[0]), S.naglowekKom("Planowane działanie rozwojowe", w[1]),
        S.naglowekKom("Forma (szkolenie / narada / mentoring)", w[2]), S.naglowekKom("Termin i odpowiedzialny", w[3]),
      ]})];
      for (let i = 0; i < 5; i++) rows.push(new TableRow({ children: w.map((ww) =>
        S.cell("", { width: ww, padTop: 150, padBottom: 150, bg: i % 2 ? S.BRAND.paper : undefined })
      )}));
      d.push(S.tabela(rows, w));
    }
    d.push(S.etykieta("Sposób diagnozy potrzeb rozwojowych nauczycieli"));
    d.push(...S.kratki(["ankieta wśród nauczycieli", "wnioski z obserwacji zajęć", "wnioski z ewaluacji wewnętrznej", "rozmowy indywidualne", "wnioski z oceny pracy", "inne: ......................................"]));

    /* VII */
    d.push(S.nowaStrona());
    d.push(S.sekcja("VII", "Monitorowanie pracy placówki"));
    {
      const w = [2600, 2500, 2300, 2346];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Obszar monitorowania", w[0]), S.naglowekKom("Wskaźnik / dane zbierane", w[1]),
        S.naglowekKom("Sposób i źródło danych", w[2]), S.naglowekKom("Częstotliwość i odpowiedzialny", w[3]),
      ]})];
      const start = [
        ["Realizacja podstawy programowej i godzin zajęć", "% zrealizowanych godzin", "Dzienniki, zestawienia", ""],
        ["Frekwencja uczniów", "Średnia frekwencja w oddziałach", "Dziennik elektroniczny", ""],
        ["Realizacja zaleceń z orzeczeń", "Liczba uczniów z pełną realizacją zaleceń", "IPET, arkusz organizacji", ""],
      ];
      start.forEach((r, i) => rows.push(new TableRow({ children: r.map((t, j) =>
        S.cell(t, { width: w[j], size: 16, padTop: 130, padBottom: 130, bg: i % 2 ? S.BRAND.paper : undefined })
      )})));
      for (let i = 0; i < 3; i++) rows.push(new TableRow({ children: w.map((ww) =>
        S.cell("", { width: ww, padTop: 140, padBottom: 140 })
      )}));
      d.push(S.tabela(rows, w));
    }

    /* VIII */
    d.push(S.sekcja("VIII", "Harmonogram roczny"));
    {
      const w = [1500, C - 1500];
      const mies = ["IX", "X", "XI", "XII", "I", "II", "III", "IV", "V", "VI", "VII–VIII"];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Miesiąc", w[0]), S.naglowekKom("Zadania nadzoru (ewaluacja · kontrola · obserwacje · wspomaganie · monitorowanie)", w[1]),
      ]})];
      mies.forEach((m, i) => rows.push(new TableRow({ children: [
        S.cell(m, { width: w[0], align: S.AlignmentType.CENTER, bold: true, color: S.BRAND.purple, size: 18, vAlign: "center", bg: S.BRAND.purpleMist, padTop: 120, padBottom: 120 }),
        S.cell("", { width: w[1], padTop: 120, padBottom: 120, bg: i % 2 ? S.BRAND.paper : undefined }),
      ]})));
      d.push(S.tabela(rows, w));
    }

    /* IX */
    d.push(S.sekcja("IX", "Przedstawienie planu i zmiany"));
    d.push(S.poleLinia("Data przedstawienia planu radzie pedagogicznej"));
    d.push(S.poleLinia("Zmiany wprowadzone w trakcie roku szkolnego (data, zakres, powód)"));
    d.push(...S.linie(2));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.planTermin, W.P.ksztalcenieSpecjalne]));
    d.push(...S.blokPodpisow(["Dyrektor placówki", "Przewodniczący zespołu ewaluacyjnego"]));
    return d;
  },
};
