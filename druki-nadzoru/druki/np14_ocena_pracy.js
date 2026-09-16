const S = require("../styl.js");
const W = require("../wspolne.js");
const { TableRow } = require("docx");
const C = S.CONTENT_W;

/* tabela kryteriów oceny pracy: kryterium | dowody | poziom | uwagi */
function tabelaOceny(kryteria, { numeruj = true } = {}) {
  const w = [520, 3500, 2700, 1400, C - 520 - 3500 - 2700 - 1400];
  const rows = [new TableRow({ tableHeader: true, children: [
    S.naglowekKom("Nr", w[0]),
    S.naglowekKom("Kryterium", w[1]),
    S.naglowekKom("Dowody i źródła ustaleń", w[2]),
    S.naglowekKom("Poziom spełnienia", w[3]),
    S.naglowekKom("Uwagi", w[4]),
  ]})];
  kryteria.forEach((k, i) => {
    const bg = i % 2 ? S.BRAND.paper : undefined;
    rows.push(new TableRow({ children: [
      S.cell(numeruj ? String(i + 1) : "", { width: w[0], align: S.AlignmentType.CENTER, bold: true, color: S.BRAND.orange, bg, padTop: 130, padBottom: 130 }),
      S.cell(k, { width: w[1], size: 16, bg, padTop: 130, padBottom: 130 }),
      S.cell("", { width: w[2], bg, padTop: 130, padBottom: 130 }),
      S.cell("", { width: w[3], bg, padTop: 130, padBottom: 130 }),
      S.cell("", { width: w[4], bg, padTop: 130, padBottom: 130 }),
    ]}));
  });
  return S.tabela(rows, w);
}

module.exports = {
  kod: "NP-14",
  plik: "NP-14_Karta_oceny_pracy_nauczyciela.docx",
  tytul: "Karta oceny pracy nauczyciela",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Wspomaganie · ocena pracy nauczyciela",
      tytul: "Karta oceny pracy nauczyciela",
      podtytul: "arkusz roboczy dyrektora — zbieranie dowodów, poziom spełniania kryteriów, projekt oceny",
    }));

    d.push(W.metryczka2([
      ["Nauczyciel", "Stopień awansu zawodowego"],
      ["Stanowisko / prowadzone zajęcia", "Staż pracy w placówce"],
      ["Data wszczęcia procedury", "Okres objęty oceną"],
    ]));

    d.push(S.etykieta("Tryb dokonania oceny"));
    d.push(...S.kratki([
      "z inicjatywy dyrektora placówki",
      "na wniosek nauczyciela",
      "na wniosek organu sprawującego nadzór pedagogiczny",
      "na wniosek organu prowadzącego",
      "na wniosek rady rodziców",
      "ocena obowiązkowa wynikająca z przepisów o awansie zawodowym",
    ]));

    d.push(...S.pudelko(
      "Ocena pracy nauczyciela nie jest formą nadzoru pedagogicznego, ale korzysta z ustaleń nadzoru: obserwacji zajęć, kontroli dokumentacji i danych o efektach pracy. Ten arkusz służy dyrektorowi do uporządkowania dowodów przed sporządzeniem karty oceny pracy na formularzu obowiązującym w placówce.",
      { before: 120 }
    ));

    /* I */
    d.push(S.sekcja("I", "Kryteria obowiązkowe"));
    d.push(tabelaOceny([
      "Poprawność merytoryczna i metodyczna prowadzonych zajęć dydaktycznych, wychowawczych i opiekuńczych.",
      "Dbałość o bezpieczne i higieniczne warunki nauki, wychowania i opieki.",
      "Znajomość praw dziecka, ich realizacja oraz kierowanie się dobrem ucznia i troską o jego zdrowie z poszanowaniem godności osobistej.",
      "Wspieranie każdego ucznia, w tym ucznia z niepełnosprawnością, w jego rozwoju oraz tworzenie warunków do aktywnego i pełnego uczestnictwa w życiu placówki i środowiska lokalnego.",
      "Kształtowanie u uczniów szacunku do drugiego człowieka, świadomości posiadanych praw oraz postaw obywatelskiej, patriotycznej i prospołecznej, w tym przez własny przykład.",
      "Współpraca z innymi nauczycielami.",
      "Przestrzeganie przepisów prawa z zakresu funkcjonowania placówki oraz wewnętrznych uregulowań obowiązujących w placówce.",
      "Poszerzanie wiedzy i doskonalenie umiejętności związanych z wykonywaną pracą, w tym w ramach doskonalenia zawodowego.",
      "Współpraca z rodzicami.",
    ]));
    d.push(S.para("Poziom spełnienia wpisz zgodnie ze skalą przyjętą w przepisach o ocenie pracy nauczycieli. Liczba i brzmienie kryteriów obowiązkowych zależą od stopnia awansu zawodowego — przed użyciem sprawdź aktualne rozporządzenie.", { size: 14, italic: true, color: S.BRAND.muted, before: 70 }));

    /* II */
    d.push(S.nowaStrona());
    d.push(S.sekcja("II", "Kryteria dodatkowe"));
    d.push(S.para("Wpisz wybrane kryteria dodatkowe: jedno wskazuje dyrektor, jedno nauczyciel — z wykazu zawartego w rozporządzeniu w sprawie oceny pracy nauczycieli.", { size: 16, color: S.BRAND.ink, after: 110 }));
    d.push(tabelaOceny(["", ""], { numeruj: false }));
    d.push(S.poleLinia("Kryterium wskazane przez dyrektora"));
    d.push(S.poleLinia("Kryterium wskazane przez nauczyciela"));

    /* III */
    d.push(S.sekcja("III", "Źródła informacji o pracy nauczyciela"));
    d.push(...S.kratki([
      "obserwacje zajęć przeprowadzone w okresie objętym oceną — liczba: ............",
      "kontrola dokumentacji przebiegu nauczania i dokumentacji zajęć specjalistycznych",
      "kontrola realizacji IPET i WOPF prowadzonych przez nauczyciela",
      "efekty pracy uczniów i ich postępy w stosunku do możliwości",
      "samoocena nauczyciela",
      "opinie i wnioski zespołów nauczycieli i specjalistów",
      "opinia rady rodziców (jeżeli została wydana)",
      "dokumentacja doskonalenia zawodowego (druk NP-12)",
    ]));

    /* IV */
    d.push(S.sekcja("IV", "Projekt oceny"));
    d.push(S.etykieta("Proponowana ocena pracy"));
    d.push(S.kratkiWiersz(["wyróżniająca", "bardzo dobra", "dobra", "negatywna"]));
    d.push(...S.poleOpisowe("Uzasadnienie — odniesienie do kryteriów i dowodów", 6));

    /* V */
    d.push(S.nowaStrona());
    d.push(S.sekcja("V", "Przebieg procedury"));
    {
      const w = [4600, C - 4600];
      d.push(S.tabela([
        S.wierszPola("Data powiadomienia nauczyciela o wszczęciu procedury", w, { pad: 120 }),
        S.wierszPola("Data wystąpienia o opinię rady rodziców", w, { pad: 120 }),
        S.wierszPola("Data zapoznania nauczyciela z projektem oceny", w, { pad: 120 }),
        S.wierszPola("Data zgłoszenia uwag przez nauczyciela", w, { pad: 120 }),
        S.wierszPola("Data ustalenia i doręczenia oceny pracy", w, { pad: 120 }),
      ], w));
    }
    d.push(S.etykieta("Uwagi i zastrzeżenia nauczyciela do projektu oceny"));
    d.push(...S.linie(4));

    d.push(...S.pudelko(
      "Pouczenie: od ustalonej oceny pracy nauczycielowi przysługuje odwołanie do organu sprawującego nadzór pedagogiczny, wniesione za pośrednictwem dyrektora placówki, w terminie 14 dni od dnia doręczenia oceny. Sprawdź aktualne brzmienie pouczenia w Karcie Nauczyciela przed wydaniem karty oceny.",
      { bg: S.BRAND.orangeMist, accent: S.BRAND.amber, color: S.BRAND.ink, size: 15, italic: false }
    ));

    d.push(...W.podstawy([W.P.kartaNauczyciela, W.P.ocenaPracy, W.P.prawoOswiatowe, W.P.nadzor, W.P.rodo]));
    d.push(...W.klauzula(
      "Karta zawiera dane osobowe nauczyciela i podlega ochronie. Przechowuj ją w aktach osobowych zgodnie z przepisami o dokumentacji pracowniczej i polityką ochrony danych placówki."
    ));
    d.push(...S.blokPodpisow(["Dyrektor placówki", "Nauczyciel — zapoznałam/em się"]));
    return d;
  },
};
