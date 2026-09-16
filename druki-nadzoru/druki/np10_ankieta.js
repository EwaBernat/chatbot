const S = require("../styl.js");
const W = require("../wspolne.js");
const { TableRow } = require("docx");
const C = S.CONTENT_W;

/* tabela pytań zamkniętych ze skalą 4-stopniową + "nie wiem" */
function tabelaSkali(n, etykiety) {
  const wP = 4200, wS = 1020, wNw = C - wP - 4 * wS;
  const w = [wP, wS, wS, wS, wS, wNw];
  const rows = [new TableRow({ tableHeader: true, children: [
    S.naglowekKom("Stwierdzenie", w[0]),
    ...etykiety.map((e, i) => S.naglowekKom(e, w[i + 1], { align: S.AlignmentType.CENTER })),
  ]})];
  for (let i = 1; i <= n; i++)
    rows.push(new TableRow({ children: [
      S.cell(i + ".", { width: w[0], size: 16, color: S.BRAND.muted, padTop: 135, padBottom: 135, bg: i % 2 ? undefined : S.BRAND.paper }),
      ...[1, 2, 3, 4, 5].map((c) => S.cell(S.KRATKA, {
        width: w[c], align: S.AlignmentType.CENTER, size: 19, color: S.BRAND.orange,
        vAlign: "center", bg: i % 2 ? undefined : S.BRAND.paper,
      })),
    ]}));
  return S.tabela(rows, w);
}

module.exports = {
  kod: "NP-10",
  plik: "NP-10_Ewaluacja_wewnetrzna_kwestionariusz_ankiety.docx",
  tytul: "Ewaluacja wewnętrzna — kwestionariusz ankiety",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Ewaluacja wewnętrzna · narzędzie badawcze",
      tytul: "Kwestionariusz ankiety",
      podtytul: "wzór do wypełnienia treścią badania  ·  wersja dla dorosłych i wersja uproszczona dla uczniów",
    }));

    d.push(W.metryczka2([
      ["Przedmiot ewaluacji", "Rok szkolny"],
      ["Termin badania", "Osoba odpowiedzialna"],
    ]));

    d.push(S.etykieta("Adresat ankiety"));
    d.push(S.kratkiWiersz(["nauczyciele", "specjaliści", "rodzice", "uczniowie", "pracownicy niepedagogiczni"]));

    d.push(...S.pudelko([
      "Ankieta jest anonimowa. Wyniki będą przedstawione wyłącznie zbiorczo i posłużą do doskonalenia pracy placówki.",
      "Przy każdym stwierdzeniu zaznacz jedną odpowiedź. Jeżeli stwierdzenie Cię nie dotyczy, zaznacz „nie wiem”.",
    ], { before: 120 }));

    /* I */
    d.push(S.sekcja("I", "Instrukcja i cel badania — uzupełnia zespół ewaluacyjny"));
    d.push(...S.linie(3));

    /* II */
    d.push(S.sekcja("II", "Pytania zamknięte"));
    d.push(S.para("Wpisz treść stwierdzeń w kolumnie pierwszej przed powieleniem ankiety.", { size: 14, italic: true, color: S.BRAND.muted, after: 90 }));
    d.push(tabelaSkali(12, ["zdecydowanie tak", "raczej tak", "raczej nie", "zdecydowanie nie", "nie wiem"]));

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Pytania otwarte"));
    d.push(S.etykieta("Pytanie 1"));
    d.push(...S.linie(4));
    d.push(S.etykieta("Pytanie 2"));
    d.push(...S.linie(4));
    d.push(S.etykieta("Pytanie 3 — co warto zmienić"));
    d.push(...S.linie(4));

    /* IV */
    d.push(S.sekcja("IV", "Metryczka respondenta (nieobowiązkowa)"));
    d.push(S.kratkiWiersz(["staż pracy do 5 lat", "6–15 lat", "powyżej 15 lat"]));
    d.push(S.kratkiWiersz(["nauczyciel zajęć edukacyjnych", "specjalista", "nauczyciel współorganizujący", "wychowawca"]));
    d.push(S.poleLinia("Etap edukacyjny / oddział (jeśli nie narusza anonimowości)"));

    /* V */
    d.push(S.nowaStrona());
    d.push(S.sekcja("V", "Wersja uproszczona dla uczniów"));
    d.push(...S.pudelko(
      "Wersję uproszczoną stosuj u uczniów z niepełnosprawnością intelektualną, trudnościami w czytaniu lub korzystających z AAC. Pytania czytaj na głos, jedno naraz, i zaznaczaj odpowiedź wskazaną przez ucznia. Kolumny możesz dodatkowo oznaczyć piktogramami używanymi w placówce.",
      { bg: S.BRAND.orangeMist, accent: S.BRAND.orange, color: S.BRAND.ink, size: 15, before: 60 }
    ));
    {
      const wP = 5600, wS = Math.floor((C - 5600) / 3);
      const w = [wP, wS, wS, C - 5600 - 2 * wS];
      const rows = [new TableRow({ tableHeader: true, children: [
        S.naglowekKom("Pytanie do ucznia", w[0]),
        S.naglowekKom("TAK", w[1], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("CZASEM", w[2], { align: S.AlignmentType.CENTER }),
        S.naglowekKom("NIE", w[3], { align: S.AlignmentType.CENTER }),
      ]})];
      const pyt = [
        "Lubię przychodzić do szkoły.",
        "W szkole czuję się bezpiecznie.",
        "Nauczyciel pomaga mi, kiedy czegoś nie umiem.",
        "Wiem, czego uczę się na zajęciach.",
        "Mam w szkole kogoś, komu mogę powiedzieć o kłopocie.",
        "",
        "",
      ];
      pyt.forEach((p, i) => rows.push(new TableRow({ children: [
        S.cell(p, { width: w[0], size: 18, padTop: 150, padBottom: 150, bg: i % 2 ? S.BRAND.paper : undefined }),
        ...[1, 2, 3].map((c) => S.cell(S.KRATKA, {
          width: w[c], align: S.AlignmentType.CENTER, size: 22, color: S.BRAND.orange,
          vAlign: "center", bg: i % 2 ? S.BRAND.paper : undefined,
        })),
      ]})));
      d.push(S.tabela(rows, w));
    }
    d.push(S.poleLinia("Sposób udzielenia odpowiedzi (samodzielnie / wskazanie / AAC / z pomocą osoby dorosłej)"));

    /* VI */
    d.push(S.sekcja("VI", "Zestawienie zbiorcze wyników — wypełnia zespół"));
    d.push(W.pustaTabelaLp(
      ["Nr", "Stwierdzenie", "Zdec. tak", "Raczej tak", "Raczej nie", "Zdec. nie", "Nie wiem"],
      [520, 3600, 1130, 1130, 1130, 1130, C - 8640], 6, 110
    ));
    d.push(S.poleLinia("Liczba rozdanych ankiet / liczba zwróconych / zwrotność w %"));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.rodo]));
    d.push(...S.blokPodpisow(["Kierownik zespołu ewaluacyjnego", "Dyrektor placówki"]));
    return d;
  },
};
