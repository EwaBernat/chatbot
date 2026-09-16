const S = require("../styl.js");
const W = require("../wspolne.js");
const { TableRow } = require("docx");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-13",
  plik: "NP-13_Protokol_rady_pedagogicznej_wyniki_nadzoru.docx",
  tytul: "Protokół rady pedagogicznej — wyniki i wnioski z nadzoru",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Rada pedagogiczna · przedstawienie wyników nadzoru",
      tytul: "Protokół posiedzenia rady pedagogicznej",
      podtytul: "przedstawienie wyników i wniosków ze sprawowanego nadzoru pedagogicznego",
    }));

    d.push(W.metryczka2([
      ["Placówka", "Rok szkolny"],
      ["Data posiedzenia", "Numer protokołu"],
      ["Przewodniczący posiedzenia", "Protokolant"],
      ["Liczba członków rady", "Liczba obecnych / kworum"],
    ]));

    /* I */
    d.push(S.sekcja("I", "Porządek obrad w zakresie nadzoru pedagogicznego"));
    d.push(S.punkt("Przedstawienie wyników i wniosków ze sprawowanego nadzoru pedagogicznego.", "num"));
    d.push(S.punkt("Przedstawienie raportu z ewaluacji wewnętrznej.", "num"));
    d.push(S.punkt("Dyskusja członków rady pedagogicznej.", "num"));
    d.push(S.punkt("Ustalenie sposobu wykorzystania wyników nadzoru do doskonalenia pracy placówki.", "num"));
    d.push(S.punkt("Inne punkty: ......................................................................................", "num"));

    /* II */
    d.push(S.sekcja("II", "Przedstawione wyniki i wnioski"));
    d.push(S.etykieta("Zakres przedstawionej informacji — zaznacz"));
    d.push(...S.kratki([
      "sprawozdanie z nadzoru pedagogicznego (druk NP-02)",
      "raport z ewaluacji wewnętrznej (druk NP-11)",
      "informacja o wynikach kontroli przestrzegania przepisów prawa",
      "informacja o obserwacjach zajęć",
      "informacja o działalności placówki",
    ]));
    d.push(S.etykieta("Streszczenie przedstawionych wyników i wniosków"));
    d.push(...S.linie(6));

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Przebieg dyskusji"));
    d.push(W.pustaTabelaLp(["Lp.", "Osoba zabierająca głos", "Treść wypowiedzi / zgłoszony wniosek"], [520, 2600, C - 3120], 6, 150));

    /* IV */
    d.push(S.sekcja("IV", "Ustalenia rady pedagogicznej"));
    d.push(W.pustaTabelaLp(
      ["Lp.", "Treść ustalenia / uchwały", "Nr uchwały", "Za", "Przeciw", "Wstrzym."],
      [520, 4600, 1500, 1050, 1050, C - 8720], 4, 130
    ));

    /* V */
    d.push(S.sekcja("V", "Zadania przyjęte do realizacji"));
    d.push(W.pustaTabelaLp(
      ["Lp.", "Zadanie wynikające z wniosków nadzoru", "Odpowiedzialny", "Termin", "Sposób sprawdzenia"],
      [520, 3400, 1900, 1300, C - 7120], 5
    ));

    /* VI */
    d.push(S.sekcja("VI", "Załączniki do protokołu"));
    d.push(...S.kratki([
      "sprawozdanie dyrektora z nadzoru pedagogicznego",
      "raport z ewaluacji wewnętrznej",
      "lista obecności członków rady pedagogicznej",
      "treść podjętych uchwał",
      "inne: ...............................................................................................",
    ]));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.radaPed, W.P.nadzor, W.P.sprawozdanieTermin]));
    d.push(...S.blokPodpisow(["Przewodniczący rady pedagogicznej", "Protokolant"]));

    /* Załącznik — lista obecności */
    d.push(S.nowaStrona());
    d.push(...S.blokTytulowy({
      kicker: "Załącznik do protokołu",
      tytul: "Lista obecności członków rady pedagogicznej",
      podtytul: "posiedzenie w dniu ..................................  ·  protokół nr ..................................",
    }));
    {
      const w = [640, 4300, C - 640 - 4300];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Lp.", w[0]), S.naglowekKom("Imię i nazwisko", w[1]), S.naglowekKom("Podpis", w[2]),
      ]})];
      for (let i = 1; i <= 22; i++)
        rows.push(new TableRow({ children: w.map((ww, j) =>
          S.cell(j === 0 ? String(i) : "", {
            width: ww, align: j === 0 ? S.AlignmentType.CENTER : undefined,
            bold: j === 0, color: j === 0 ? S.BRAND.orange : undefined,
            padTop: 115, padBottom: 115, bg: i % 2 ? undefined : S.BRAND.paper,
          })
        )}));
      d.push(S.tabela(rows, w));
    }
    return d;
  },
};
