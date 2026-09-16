const S = require("../styl.js");
const W = require("../wspolne.js");
const { TableRow } = require("docx");
const C = S.CONTENT_W;

const pustaTabela = (naglowki, w, n, pad = 140) => {
  const rows = [new TableRow({ tableHeader: true, children: naglowki.map((h, i) => S.naglowekKom(h, w[i])) })];
  for (let i = 0; i < n; i++)
    rows.push(new TableRow({ children: w.map((ww) => S.cell("", { width: ww, padTop: pad, padBottom: pad, bg: i % 2 ? S.BRAND.paper : undefined })) }));
  return S.tabela(rows, w);
};

module.exports = {
  kod: "NP-02",
  plik: "NP-02_Sprawozdanie_z_nadzoru_pedagogicznego.docx",
  tytul: "Sprawozdanie dyrektora z nadzoru pedagogicznego",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Podsumowanie · dyrektor szkoły",
      tytul: "Sprawozdanie z nadzoru pedagogicznego",
      podtytul: "wyniki, wnioski i rekomendacje ze sprawowanego nadzoru  ·  rok szkolny ................ / ................",
    }));

    d.push(W.metryczka2([
      ["Placówka", "Rok szkolny"],
      ["Dyrektor", "Data sporządzenia"],
      ["Data przedstawienia radzie pedagogicznej", "Nr protokołu rady pedagogicznej"],
    ]));

    d.push(S.etykieta("Okres objęty sprawozdaniem"));
    d.push(S.kratkiWiersz(["I półrocze", "II półrocze", "cały rok szkolny"]));

    d.push(...S.pudelko(
      "Wyniki i wnioski ze sprawowanego nadzoru pedagogicznego przedstaw radzie pedagogicznej do 31 sierpnia. Ogólne wnioski z nadzoru przedstawiaj radzie nie rzadziej niż dwa razy w roku szkolnym.",
      { before: 140 }
    ));

    /* I */
    d.push(S.sekcja("I", "Stopień realizacji planu nadzoru"));
    d.push(pustaTabela(
      ["Zadanie zaplanowane w planie nadzoru", "Termin planowany", "Zrealizowano (T / N / częściowo)", "Uwagi i przyczyny odstępstw"],
      [3300, 1600, 1900, 2946], 6
    ));

    /* II */
    d.push(S.sekcja("II", "Ewaluacja wewnętrzna — wyniki"));
    d.push(S.poleLinia("Przedmiot ewaluacji"));
    d.push(S.poleLinia("Metody i narzędzia, wielkość próby"));
    d.push(...S.poleOpisowe("Najważniejsze ustalenia (odpowiedzi na pytania kluczowe)", 5));
    d.push(...S.poleOpisowe("Mocne strony placówki potwierdzone badaniem", 3));
    d.push(...S.poleOpisowe("Obszary wymagające poprawy", 3));

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Kontrola przestrzegania przepisów prawa — ustalenia"));
    d.push(pustaTabela(
      ["Tematyka kontroli", "Zakres / kto objęty", "Ustalenia", "Zalecenia i termin wykonania"],
      [2400, 2100, 2700, 2546], 5
    ));
    d.push(S.etykieta("Realizacja zaleceń wydanych w poprzednim okresie"));
    d.push(S.kratkiWiersz(["wszystkie zrealizowane", "zrealizowane częściowo", "niezrealizowane — opis poniżej"]));
    d.push(...S.linie(2));

    /* IV */
    d.push(S.sekcja("IV", "Obserwacje zajęć — synteza"));
    {
      const w = [4400, 1500, 1500, C - 7400];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Rodzaj obserwowanych zajęć", w[0]),
        S.naglowekKom("Plan", w[1], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("Wykonanie", w[2], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("Liczba nauczycieli", w[3], { align: S.AlignmentType.CENTER }),
      ]})];
      ["Zajęcia dydaktyczne (edukacyjne)", "Zajęcia rewalidacyjne", "Zajęcia specjalistyczne pomocy p-p", "Zajęcia z zakresu WWR / zespołowe", "Obserwacje diagnozujące", "Razem"].forEach((t, i, arr) =>
        rows.push(new TableRow({ children: [
          S.cell(t, { width: w[0], size: 17, bold: i === arr.length - 1, color: i === arr.length - 1 ? S.BRAND.purple : undefined, bg: i === arr.length - 1 ? S.BRAND.purpleMist : (i % 2 ? S.BRAND.paper : undefined), padTop: 110, padBottom: 110 }),
          ...[1, 2, 3].map((c) => S.cell("", { width: w[c], bg: i === arr.length - 1 ? S.BRAND.purpleMist : (i % 2 ? S.BRAND.paper : undefined), padTop: 110, padBottom: 110 })),
        ]}))
      );
      d.push(S.tabela(rows, w));
    }
    d.push(...S.poleOpisowe("Powtarzające się mocne strony warsztatu nauczycieli", 3));
    d.push(...S.poleOpisowe("Powtarzające się trudności i potrzeby wsparcia", 3));

    /* V */
    d.push(S.nowaStrona());
    d.push(S.sekcja("V", "Wspomaganie nauczycieli — zrealizowane działania"));
    d.push(pustaTabela(
      ["Forma wspomagania", "Temat", "Liczba uczestników", "Efekt / wykorzystanie w pracy"],
      [2200, 2700, 1500, 3346], 5
    ));

    /* VI */
    d.push(S.sekcja("VI", "Monitorowanie pracy placówki — dane"));
    d.push(pustaTabela(
      ["Obszar monitorowany", "Wskaźnik", "Wartość / wynik", "Komentarz"],
      [2600, 2300, 1700, 3146], 5
    ));

    /* VII */
    d.push(S.sekcja("VII", "Realizacja zadań specyficznych dla kształcenia specjalnego"));
    d.push(S.etykieta("Zaznacz stan realizacji i uzupełnij dane liczbowe"));
    d.push(...S.kratki([
      "Dla wszystkich uczniów z orzeczeniem opracowano IPET w wymaganym terminie — liczba IPET: ..............",
      "Przeprowadzono WOPF co najmniej dwa razy w roku szkolnym — liczba ocen: ..............",
      "Zrealizowano wymiar zajęć rewalidacyjnych wynikający z arkusza organizacji — % realizacji: ..............",
      "Zalecenia z orzeczeń zostały uwzględnione w IPET i w organizacji zajęć.",
      "Rodzice otrzymali informację o wielospecjalistycznej ocenie i mogli uczestniczyć w spotkaniach zespołu.",
      "Dokonano modyfikacji IPET wynikających z oceny efektywności — liczba modyfikacji: ..............",
    ]));
    d.push(...S.linie(2));

    /* VIII */
    d.push(S.nowaStrona());
    d.push(S.sekcja("VIII", "Wnioski i rekomendacje"));
    d.push(pustaTabela(
      ["Lp.", "Wniosek z nadzoru", "Rekomendacja — co zmieniamy", "Odpowiedzialny", "Termin"],
      [520, 3100, 3100, 1600, 1426], 6
    ));
    d.push(...S.pudelko(
      "Wnioski zapisz jako stwierdzenia faktu wynikające z zebranych danych, a rekomendacje jako konkretne działania z odpowiedzialnym i terminem. Rekomendacje przenieś do planu nadzoru na kolejny rok szkolny (druk NP-01, sekcja II).",
      { bg: S.BRAND.orangeMist, accent: S.BRAND.orange, color: S.BRAND.ink, size: 15 }
    ));

    /* IX */
    d.push(S.sekcja("IX", "Rekomendacje do planu na kolejny rok szkolny"));
    d.push(...S.poleOpisowe("Proponowany przedmiot ewaluacji wewnętrznej", 2));
    d.push(...S.poleOpisowe("Proponowana tematyka kontroli", 2));
    d.push(...S.poleOpisowe("Priorytety wspomagania i doskonalenia nauczycieli", 2));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.sprawozdanieTermin, W.P.radaPed, W.P.ksztalcenieSpecjalne]));
    d.push(...S.blokPodpisow(["Dyrektor placówki", "Przewodniczący rady pedagogicznej"]));
    return d;
  },
};
