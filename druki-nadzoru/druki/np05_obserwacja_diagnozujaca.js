const S = require("../styl.js");
const W = require("../wspolne.js");
const C = S.CONTENT_W;

module.exports = {
  kod: "NP-05",
  plik: "NP-05_Arkusz_obserwacji_diagnozujacej.docx",
  tytul: "Arkusz obserwacji diagnozującej",
  build() {
    const d = [];

    d.push(...S.blokTytulowy({
      kicker: "Obserwacja · diagnoza osiągnięć uczniów",
      tytul: "Arkusz obserwacji diagnozującej",
      podtytul: "obserwacja nastawiona na sprawdzenie, w jakim stopniu uczniowie opanowali zaplanowaną umiejętność",
    }));

    d.push(...S.pudelko(
      "Obserwacja diagnozująca odpowiada na pytanie o efekt: co uczniowie potrafią po zajęciach. Nauczyciel przed zajęciami wskazuje sprawdzaną umiejętność i sposób jej sprawdzenia, a obserwujący zbiera dane o wynikach uczniów, nie tylko o działaniach nauczyciela.",
      { before: 60 }
    ));

    d.push(W.metryczka2([
      ["Nauczyciel prowadzący", "Data i godzina"],
      ["Zajęcia / przedmiot", "Oddział / grupa"],
      ["Liczba uczniów obecnych / wpisanych", "Obserwujący"],
    ]));

    /* I */
    d.push(S.sekcja("I", "Ustalenia przed obserwacją"));
    d.push(S.etykieta("Wypełnia nauczyciel wspólnie z dyrektorem przed zajęciami"));
    {
      const w = [3000, C - 3000];
      d.push(S.tabela([
        S.wierszPola("Sprawdzana umiejętność ucznia", w, { pad: 150 }),
        S.wierszPola("Kryterium sukcesu (co uznajemy za opanowanie)", w, { pad: 150 }),
        S.wierszPola("Sposób sprawdzenia podczas zajęć", w, { pad: 150 }),
        S.wierszPola("Uczniowie objęci dostosowaniem kryterium (IPET)", w, { pad: 150 }),
        S.wierszPola("Przewidywany wynik (prognoza nauczyciela)", w, { pad: 150 }),
      ], w));
    }

    /* II */
    d.push(S.sekcja("II", "Zebrane dane o wynikach uczniów"));
    d.push(S.para("Wpisz inicjały lub kod ucznia. Poziom: S — samodzielnie, P — z podpowiedzią słowną, F — z pomocą fizyczną / prowadzeniem, N — nie wykonał.", { size: 15, italic: true, color: S.BRAND.muted, after: 90 }));
    {
      const w = [520, 2100, 1500, 1500, C - 5620];
      const rows = [new (require("docx").TableRow)({
        tableHeader: true,
        children: [
          S.naglowekKom("Lp.", w[0]), S.naglowekKom("Uczeń (kod)", w[1]),
          S.naglowekKom("Poziom wykonania", w[2]), S.naglowekKom("Kryterium osiągnięte (T/N)", w[3]),
          S.naglowekKom("Obserwacje, zastosowane wsparcie", w[4]),
        ],
      })];
      for (let i = 1; i <= 10; i++)
        rows.push(new (require("docx").TableRow)({
          children: w.map((ww, j) => S.cell(j === 0 ? String(i) : "", {
            width: ww, align: j === 0 ? S.AlignmentType.CENTER : undefined,
            bold: j === 0, color: j === 0 ? S.BRAND.orange : undefined,
            padTop: 120, padBottom: 120, bg: i % 2 ? undefined : S.BRAND.paper,
          })),
        }));
      d.push(S.tabela(rows, w));
    }

    /* III */
    d.push(S.nowaStrona());
    d.push(S.sekcja("III", "Ocena procesu prowadzącego do wyniku"));
    d.push(W.tabelaKryteriow("Kryterium", [
      "Zadania sprawdzające rzeczywiście badały zaplanowaną umiejętność.",
      "Kryterium sukcesu było znane uczniom i sformułowane w zrozumiały sposób.",
      "Kryterium zostało zindywidualizowane dla uczniów objętych IPET.",
      "Nauczyciel zbierał dane o postępach w trakcie zajęć, nie tylko na koniec.",
      "Uczniowie, którzy nie osiągnęli kryterium, otrzymali wsparcie w trakcie zajęć.",
      "Nauczyciel wyciągnął wnioski z wyników i zapowiedział dalszą pracę.",
    ]));
    d.push(W.legendaSkali());

    /* IV */
    d.push(S.sekcja("IV", "Wynik diagnozy"));
    {
      const w = [4400, 1700, C - 6100];
      d.push(S.tabela([
        S.wierszPola("Liczba uczniów, którzy osiągnęli kryterium", [4400, C - 4400], { pad: 120 }),
        S.wierszPola("Liczba uczniów, którzy osiągnęli kryterium częściowo", [4400, C - 4400], { pad: 120 }),
        S.wierszPola("Liczba uczniów, którzy nie osiągnęli kryterium", [4400, C - 4400], { pad: 120 }),
        S.wierszPola("Zgodność z prognozą nauczyciela", [4400, C - 4400], { pad: 120 }),
      ], [4400, C - 4400]));
    }
    d.push(...S.poleOpisowe("Interpretacja wyniku — co dane mówią o skuteczności zajęć", 4));

    /* V */
    d.push(S.sekcja("V", "Wnioski i dalsze działania"));
    d.push(...S.poleOpisowe("Wnioski nauczyciela (samoocena po zajęciach)", 3));
    d.push(S.etykieta("Ustalenia z dyrektorem"));
    d.push(W.pustaTabelaLp(["Lp.", "Ustalenie / zalecenie", "Termin", "Sposób sprawdzenia"], [520, 4700, 1900, C - 7120], 4));

    d.push(...W.podstawy([W.P.prawoOswiatowe, W.P.nadzor, W.P.ksztalcenieSpecjalne]));
    d.push(...W.klauzula());
    d.push(...S.blokPodpisow(["Obserwujący", "Nauczyciel — zapoznałam/em się"]));
    return d;
  },
};
