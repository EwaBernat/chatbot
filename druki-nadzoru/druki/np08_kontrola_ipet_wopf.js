const S = require("../styl.js");
const W = require("../wspolne.js");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-08",
  plik: "NP-08_Arkusz_kontroli_realizacji_IPET_i_WOPF.docx",
  tytul: "Arkusz kontroli realizacji IPET i WOPF",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Kontrola · kształcenie specjalne",
      tytul: "Arkusz kontroli realizacji IPET i WOPF",
      podtytul: "indywidualny program edukacyjno-terapeutyczny i wielospecjalistyczna ocena poziomu funkcjonowania ucznia",
    }));

    d.push(W.metryczka2([
      ["Uczeń (imię i nazwisko lub kod)", "Oddział"],
      ["Numer i data orzeczenia", "Okres obowiązywania orzeczenia"],
      ["Koordynator zespołu / wychowawca", "Data kontroli"],
    ]));

    /* I */
    d.push(S.sekcja("I", "Terminowość i tryb opracowania"));
    d.push(W.tabelaKontrolna([
      "IPET opracowano w terminie wynikającym z przepisów (do 30 września albo w ciągu 30 dni od złożenia orzeczenia).",
      "Program opracował zespół nauczycieli i specjalistów pracujących z uczniem.",
      "Spotkania zespołu są udokumentowane (protokół, lista obecności).",
      "Rodzice zostali zawiadomieni o terminie spotkania zespołu i mogli w nim uczestniczyć.",
      "Rodzice otrzymali kopię IPET oraz kopię wielospecjalistycznej oceny.",
      "IPET obowiązuje na okres wskazany w orzeczeniu, nie dłuższy niż etap edukacyjny.",
    ], { wEl: 5100 }));

    /* II */
    d.push(S.sekcja("II", "Kompletność IPET"));
    d.push(W.tabelaKontrolna([
      "Zakres i sposób dostosowania wymagań edukacyjnych do potrzeb i możliwości ucznia.",
      "Zintegrowane działania nauczycieli i specjalistów (w tym o charakterze rewalidacyjnym).",
      "Formy i okres udzielania pomocy psychologiczno-pedagogicznej oraz wymiar godzin.",
      "Działania wspierające rodziców oraz zakres współpracy z instytucjami.",
      "Zajęcia rewalidacyjne, resocjalizacyjne lub socjoterapeutyczne — rodzaj i wymiar.",
      "Rodzaj i sposób dostosowania warunków przeprowadzania egzaminu (jeśli dotyczy).",
      "Wybrane zajęcia edukacyjne realizowane indywidualnie lub w grupie do 5 osób (jeśli dotyczy).",
      "Cele są sformułowane w sposób mierzalny (kryterium osiągnięcia, termin).",
      "Zalecenia z orzeczenia mają odzwierciedlenie w zapisach programu.",
    ], { wEl: 5100 }));

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Wielospecjalistyczna ocena poziomu funkcjonowania (WOPF)"));
    d.push(W.tabelaKontrolna([
      "Ocenę przeprowadzono co najmniej dwa razy w roku szkolnym.",
      "Ocena zawiera indywidualne potrzeby rozwojowe i edukacyjne ucznia.",
      "Ocena zawiera mocne strony, predyspozycje, zainteresowania i uzdolnienia ucznia.",
      "Opisano przyczyny niepowodzeń edukacyjnych i trudności w funkcjonowaniu.",
      "Uwzględniono bariery i ograniczenia utrudniające funkcjonowanie i uczestnictwo ucznia.",
      "Wnioski z oceny przełożono na modyfikację IPET.",
    ], { wEl: 5100 }));

    /* IV */
    d.push(S.sekcja("IV", "Realizacja zajęć wynikających z orzeczenia"));
    d.push(W.pustaTabela(
      ["Rodzaj zajęć", "Wymiar zalecony / tygodniowo", "Wymiar zrealizowany", "Prowadzący", "Zgodność (T/N)"],
      [2900, 1900, 1700, 2000, C - 8500], 6
    ));
    d.push(S.para("Różnice w realizacji wymiaru godzin opisz w sekcji V wraz z przyczyną i sposobem wyrównania.", { size: 14, italic: true, color: S.BRAND.muted }));

    /* V */
    d.push(S.sekcja("V", "Ustalenia i zalecenia"));
    d.push(...S.poleOpisowe("Stan faktyczny", 4));
    d.push(W.pustaTabelaLp(["Lp.", "Uchybienie / obszar do poprawy", "Zalecenie", "Termin", "Odpowiedzialny"], [520, 2900, 2900, 1400, C - 7720], 4));

    d.push(...S.pudelko(
      "Jeżeli kontrola wykaże potrzebę zmiany programu, zwołaj zespół i dokonaj modyfikacji IPET — zmiana wymaga udokumentowania i poinformowania rodziców.",
      { bg: S.BRAND.orangeMist, accent: S.BRAND.orange, color: S.BRAND.ink, size: 15 }
    ));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.ksztalcenieSpecjalne, W.P.pomocPP, W.P.rodo]));
    d.push(...W.klauzula(
      "Druk zawiera dane osobowe ucznia, w tym dane o stanie zdrowia — kategorię szczególną danych. Przechowuj go w dokumentacji nadzoru z zachowaniem zasad ochrony danych obowiązujących w placówce."
    ));
    d.push(...S.blokPodpisow(["Kontrolujący", "Koordynator zespołu"]));
    return d;
  },
};
