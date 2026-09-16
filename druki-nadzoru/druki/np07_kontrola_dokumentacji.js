const S = require("../styl.js");
const W = require("../wspolne.js");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-07",
  plik: "NP-07_Arkusz_kontroli_dokumentacji_przebiegu_nauczania.docx",
  tytul: "Arkusz kontroli dokumentacji przebiegu nauczania",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Kontrola przestrzegania przepisów prawa",
      tytul: "Arkusz kontroli dokumentacji przebiegu nauczania",
      podtytul: "dzienniki zajęć, dokumentacja pomocy psychologiczno-pedagogicznej i dokumentacja ucznia",
    }));

    d.push(W.metryczka2([
      ["Kontrolujący", "Data kontroli"],
      ["Nauczyciel / oddział objęty kontrolą", "Okres objęty kontrolą"],
      ["Rodzaj kontroli (planowa / doraźna / sprawdzająca)", "Podstawa (plan nadzoru / polecenie)"],
    ]));

    /* I */
    d.push(S.sekcja("I", "Zakres kontroli"));
    d.push(W.tabelaKontrolna([
      { grupa: "Dziennik zajęć oddziału" },
      "Wpisy tematów zajęć są dokonywane systematycznie i zgodne z realizowanym programem.",
      "Odnotowano obecność uczniów na każdych zajęciach.",
      "Oceny bieżące są wystawiane systematycznie, zgodnie z zasadami oceniania w statucie.",
      "Odnotowano kontakty z rodzicami (zebrania, konsultacje, informacje o postępach).",
      "Dane uczniów i oddziału są kompletne i aktualne.",
      "Realizacja podstawy programowej jest udokumentowana (rozliczenie godzin).",
      { grupa: "Dzienniki zajęć rewalidacyjnych, specjalistycznych i pomocy p-p" },
      "Prowadzony jest odrębny dziennik dla każdego rodzaju zajęć.",
      "Dziennik zawiera listę uczestników, tematy i obecność na zajęciach.",
      "Odnotowane są informacje o postępach i efektach udzielanej pomocy.",
      "Wymiar zrealizowanych godzin jest zgodny z arkuszem organizacji i zaleceniami orzeczeń.",
      "W razie odwołania zajęć odnotowano przyczynę i sposób odpracowania.",
      { grupa: "Dokumentacja ucznia objętego kształceniem specjalnym" },
      "Teczka ucznia zawiera aktualne orzeczenie o potrzebie kształcenia specjalnego.",
      "W teczce znajduje się aktualny IPET i wielospecjalistyczna ocena poziomu funkcjonowania.",
      "Zgromadzone są zgody i oświadczenia rodziców wymagane przepisami.",
      "Dokumentacja jest przechowywana w sposób zabezpieczający dane osobowe.",
      { grupa: "Pozostała dokumentacja" },
      "Arkusze ocen są prowadzone i uzupełniane zgodnie z przepisami.",
      "Księga uczniów / księga ewidencji jest aktualna.",
      "Protokoły zespołów nauczycieli i specjalistów są sporządzone i podpisane.",
      "Dokumentacja badań i czynności uzupełniających jest prowadzona przez specjalistów.",
    ], { wEl: 5100 }));

    /* II */
    d.push(S.nowaStrona());
    d.push(S.sekcja("II", "Ustalenia kontroli"));
    d.push(...S.poleOpisowe("Stan faktyczny — co stwierdzono", 5));
    d.push(S.etykieta("Stwierdzone uchybienia"));
    d.push(S.kratkiWiersz(["nie stwierdzono uchybień", "stwierdzono uchybienia — wykaz poniżej"]));
    d.push(W.pustaTabelaLp(
      ["Lp.", "Uchybienie", "Naruszony przepis", "Zalecenie", "Termin usunięcia"],
      [520, 2900, 1900, 2600, C - 7920], 5
    ));

    /* III */
    d.push(S.sekcja("III", "Potwierdzenie usunięcia uchybień"));
    d.push(W.pustaTabela(
      ["Zalecenie", "Data sprawdzenia", "Usunięto (Tak / Nie)", "Uwagi"],
      [3600, 1700, 1700, C - 7000], 4
    ));

    /* IV */
    d.push(S.sekcja("IV", "Wnioski z kontroli"));
    d.push(...S.poleOpisowe("Wnioski do wykorzystania w pracy placówki", 3));
    d.push(...S.poleOpisowe("Potrzeby wspomagania wynikające z kontroli", 2));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.dokumentacja, W.P.ksztalcenieSpecjalne, W.P.rodo]));
    d.push(...W.klauzula());
    d.push(...S.blokPodpisow(["Kontrolujący", "Nauczyciel — zapoznałam/em się"]));
    return d;
  },
};
