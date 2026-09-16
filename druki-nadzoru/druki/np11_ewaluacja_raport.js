const S = require("../styl.js");
const W = require("../wspolne.js");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-11",
  plik: "NP-11_Raport_z_ewaluacji_wewnetrznej.docx",
  tytul: "Raport z ewaluacji wewnętrznej",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Ewaluacja wewnętrzna · raport",
      tytul: "Raport z ewaluacji wewnętrznej",
      podtytul: "wyniki badania, wnioski i rekomendacje  ·  rok szkolny ................ / ................",
    }));

    d.push(W.metryczka2([
      ["Placówka", "Rok szkolny"],
      ["Przedmiot ewaluacji", "Termin badania"],
      ["Kierownik zespołu", "Data sporządzenia raportu"],
    ]));

    /* I */
    d.push(S.sekcja("I", "Opis ewaluacji"));
    d.push(...S.poleOpisowe("Przedmiot i cel ewaluacji", 3));
    d.push(S.etykieta("Pytania kluczowe i kryteria"));
    d.push(W.pustaTabelaLp(["Lp.", "Pytanie kluczowe", "Kryterium"], [520, 4600, C - 5120], 4));

    /* II */
    d.push(S.sekcja("II", "Organizacja badania"));
    d.push(W.pustaTabela(
      ["Metoda i narzędzie", "Respondenci / źródło", "Liczba objętych badaniem", "Zwrotność / kompletność"],
      [2800, 2500, 2200, C - 7500], 5
    ));
    d.push(S.poleLinia("Ograniczenia badania (co obniża pewność wniosków)"));
    d.push(...S.linie(2));

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Wyniki — odpowiedzi na pytania kluczowe"));
    [1, 2, 3].forEach((n) => {
      d.push(S.podsekcja("Pytanie kluczowe nr " + n));
      d.push(S.etykieta("Zebrane dane (liczby, cytaty, ustalenia z dokumentów)"));
      d.push(...S.linie(4));
      d.push(S.etykieta("Interpretacja — co z tych danych wynika"));
      d.push(...S.linie(3));
      d.push(S.etykieta("Czy kryterium zostało spełnione"));
      d.push(S.kratkiWiersz(["tak", "częściowo", "nie"]));
    });

    /* IV */
    d.push(S.nowaStrona());
    d.push(S.sekcja("IV", "Mocne strony i obszary wymagające poprawy"));
    {
      const w = [Math.floor(C / 2), C - Math.floor(C / 2)];
      const { TableRow } = require("docx");
      const rows = [
        new TableRow({ tableHeader: true, children: [
          S.naglowekKom("Mocne strony potwierdzone danymi", w[0]),
          S.naglowekKom("Obszary wymagające poprawy", w[1]),
        ]}),
        new TableRow({ children: [
          S.cell("", { width: w[0], padTop: 900, padBottom: 900 }),
          S.cell("", { width: w[1], padTop: 900, padBottom: 900 }),
        ]}),
      ];
      d.push(S.tabela(rows, w));
    }

    /* V */
    d.push(S.sekcja("V", "Wnioski i rekomendacje"));
    d.push(W.pustaTabelaLp(
      ["Lp.", "Wniosek", "Rekomendacja — konkretne działanie", "Odpowiedzialny", "Termin"],
      [520, 3000, 3200, 1600, C - 8320], 6
    ));

    /* VI */
    d.push(S.sekcja("VI", "Upowszechnienie wyników"));
    d.push(...S.kratki([
      "przedstawienie raportu radzie pedagogicznej — data: ..............................",
      "informacja dla rodziców — forma i data: ................................................",
      "informacja dla uczniów w formie dostosowanej do ich możliwości",
      "publikacja na stronie internetowej placówki",
      "przekazanie wniosków organowi prowadzącemu (jeśli dotyczy)",
    ]));

    /* VII */
    d.push(S.sekcja("VII", "Wykorzystanie wyników"));
    d.push(S.poleLinia("Które rekomendacje wchodzą do planu nadzoru na kolejny rok szkolny"));
    d.push(...S.linie(3));
    d.push(S.poleLinia("Sposób i termin monitorowania wdrożenia"));
    d.push(...S.linie(2));

    /* VIII */
    d.push(S.sekcja("VIII", "Załączniki"));
    d.push(...S.kratki([
      "wzory zastosowanych narzędzi badawczych",
      "zestawienia zbiorcze odpowiedzi",
      "wykresy i tabele wyników",
      "inne: ...............................................................................................",
    ]));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.radaPed, W.P.rodo]));
    d.push(...S.blokPodpisow(["Kierownik zespołu ewaluacyjnego", "Członkowie zespołu", "Dyrektor placówki"]));
    return d;
  },
};
