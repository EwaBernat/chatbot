const S = require("../styl.js");
const W = require("../wspolne.js");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-06",
  plik: "NP-06_Karta_pohospitacyjna_rozmowa_po_obserwacji.docx",
  tytul: "Karta pohospitacyjna — rozmowa po obserwacji",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Obserwacja · rozmowa poobserwacyjna",
      tytul: "Karta pohospitacyjna",
      podtytul: "rozmowa dyrektora z nauczycielem po obserwacji zajęć  ·  ustalenia, zalecenia, wsparcie",
    }));

    d.push(W.metryczka2([
      ["Nauczyciel", "Data obserwacji"],
      ["Rodzaj obserwowanych zajęć", "Data rozmowy"],
      ["Numer arkusza obserwacji", "Prowadzący rozmowę"],
    ]));

    /* I */
    d.push(S.sekcja("I", "Samoocena nauczyciela"));
    d.push(S.etykieta("Co się udało — zdaniem nauczyciela"));
    d.push(...S.linie(3));
    d.push(S.etykieta("Co zrobiłabym / zrobiłbym inaczej"));
    d.push(...S.linie(3));
    d.push(S.etykieta("Czy cel zajęć został osiągnięty"));
    d.push(S.kratkiWiersz(["tak", "częściowo", "nie"]));
    d.push(...S.linie(2));

    /* II */
    d.push(S.sekcja("II", "Informacja zwrotna dyrektora"));
    d.push(S.etykieta("Mocne strony pracy nauczyciela"));
    d.push(...S.linie(4));
    d.push(S.etykieta("Obszary wymagające zmiany — konkretne zachowania, nie cechy"));
    d.push(...S.linie(4));

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Ustalenia i zalecenia"));
    d.push(W.pustaTabelaLp(
      ["Lp.", "Ustalenie / zalecenie", "Oczekiwany efekt", "Termin", "Sposób sprawdzenia"],
      [520, 3200, 2600, 1400, C - 7720], 5
    ));

    /* IV */
    d.push(S.sekcja("IV", "Wsparcie ze strony placówki"));
    d.push(S.etykieta("Formy wspomagania uzgodnione z nauczycielem"));
    d.push(...S.kratki([
      "szkolenie wewnętrzne lub zewnętrzne — temat: ......................................................",
      "obserwacja koleżeńska u nauczyciela: ..................................................................",
      "lekcja otwarta prowadzona przez nauczyciela",
      "konsultacje ze specjalistą placówki (psycholog / logopeda / terapeuta SI)",
      "mentoring — opiekun: ..........................................................................................",
      "literatura, materiały, pomoce dydaktyczne: ..........................................................",
      "modyfikacja przydziału zajęć lub warunków pracy",
    ]));
    d.push(S.poleLinia("Termin kolejnej obserwacji lub spotkania kontrolnego"));

    /* V */
    d.push(S.sekcja("V", "Stanowisko nauczyciela"));
    d.push(S.kratkiWiersz(["przyjmuję ustalenia bez uwag", "zgłaszam uwagi — treść poniżej"]));
    d.push(...S.linie(3));

    d.push(...S.pudelko(
      "Kartę sporządź w dwóch egzemplarzach: jeden dla nauczyciela, jeden do dokumentacji nadzoru pedagogicznego. Ustalenia z tej karty wykorzystaj przy planowaniu wspomagania (druk NP-12) oraz w sprawozdaniu rocznym (druk NP-02).",
      { before: 160 }
    ));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.kartaNauczyciela]));
    d.push(...W.klauzula());
    d.push(...S.blokPodpisow(["Dyrektor / obserwujący", "Nauczyciel"]));
    return d;
  },
};
