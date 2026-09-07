// Generator dokumentu "Czynności nauczycieli w ramach wynagrodzenia" (PCTP Koszalin).
// Uruchomienie (z katalogu głównego repozytorium):
//   npm install docx sharp
//   node -e "require('sharp')('logo-lawenda.webp').png().toFile('logo.png')"
//   node dokumenty/generuj_czynnosci_docx.js logo.png dokumenty/czynnosci-nauczycieli-w-ramach-wynagrodzenia.docx
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, HeadingLevel, ShadingType, BorderStyle, ImageRun, Header, Footer,
  PageNumber, LevelFormat, TabStopType, VerticalAlign,
} = require("docx");

const [,, LOGO = "logo.png", OUT = "czynnosci.docx"] = process.argv;

const FIOLET = "2D1B69";
const POMARANCZ = "E8450A";
const SZARY = "555555";
const JASNY2 = "FBEFE9";     // delikatny pomarańcz
const F = "Arial";

// ---------- pomocnicze ----------
const run = (text, o = {}) => new TextRun({ text, font: F, size: o.size || 20, bold: o.bold, italics: o.italics, color: o.color });
const p = (text, o = {}) => new Paragraph({
  alignment: o.align || AlignmentType.JUSTIFIED,
  spacing: { after: o.after ?? 100, before: o.before ?? 0, line: 276 },
  children: Array.isArray(text) ? text : [run(text, o)],
});
const h1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, spacing: { before: 320, after: 140 }, children: [run(t, { size: 28, bold: true, color: FIOLET })] });
const h2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 220, after: 100 }, children: [run(t, { size: 23, bold: true, color: POMARANCZ })] });
const bullet = (children, level = 0) => new Paragraph({
  numbering: { reference: "punkty", level }, spacing: { after: 60, line: 276 }, alignment: AlignmentType.JUSTIFIED,
  children: Array.isArray(children) ? children : [run(children)],
});
const numbered = (children, ref) => new Paragraph({
  numbering: { reference: ref, level: 0 }, spacing: { after: 60, line: 276 }, alignment: AlignmentType.JUSTIFIED,
  children: Array.isArray(children) ? children : [run(children)],
});
const cyt = (text) => new Paragraph({
  alignment: AlignmentType.JUSTIFIED, spacing: { after: 100, line: 276 }, indent: { left: 400, right: 400 },
  border: { left: { style: BorderStyle.SINGLE, size: 18, color: POMARANCZ, space: 8 } },
  shading: { type: ShadingType.CLEAR, fill: "FAF8FD", color: "auto" },
  children: [run(text, { italics: true, size: 19, color: "333333" })],
});
const uwaga = (label, text) => {
  const b = { style: BorderStyle.SINGLE, size: 6, color: POMARANCZ };
  return new Table({
    width: { size: 10160, type: WidthType.DXA }, columnWidths: [10160],
    rows: [new TableRow({ children: [new TableCell({
      width: { size: 10160, type: WidthType.DXA }, borders: { top: b, left: b, bottom: b, right: b },
      shading: { type: ShadingType.CLEAR, fill: JASNY2, color: "auto" }, margins: { top: 100, bottom: 100, left: 160, right: 160 },
      children: [new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 0, line: 276 },
        children: [run(label + " ", { bold: true, color: POMARANCZ, size: 19 }), run(text, { size: 19 })] })],
    })] })],
  });
};

const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: "BFB8D6" };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };

function cell(content, width, o = {}) {
  const paras = (Array.isArray(content) ? content : [content]).map((c) =>
    c instanceof Paragraph ? c : new Paragraph({
      alignment: o.align || AlignmentType.LEFT, spacing: { after: 40, line: 260 },
      children: [run(String(c), { size: o.size || 18, bold: o.bold, color: o.color })],
    }));
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, borders, verticalAlign: o.valign || VerticalAlign.TOP,
    margins: { top: 60, bottom: 60, left: 90, right: 90 },
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined,
    children: paras,
  });
}
function tabela(naglowki, wiersze, szer, o = {}) {
  const head = new TableRow({ tableHeader: true, children: naglowki.map((n, i) => cell(n, szer[i], { bold: true, color: "FFFFFF", fill: FIOLET, size: 18 })) });
  const rows = wiersze.map((w, ri) => new TableRow({
    cantSplit: true,
    children: w.map((c, i) => cell(c, szer[i], { fill: o.zebra && ri % 2 === 1 ? "F7F5FB" : undefined, size: o.size, bold: o.boldCol === i, valign: o.valign })),
  }));
  return new Table({ width: { size: szer.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: szer, rows: [head, ...rows] });
}
const odstep = (n = 80) => new Paragraph({ spacing: { after: n }, children: [] });

// ---------- treść ----------
const ROK = "2026/2027";
const PLACOWKA = "Pomorskie Centrum Terapii Pedagogicznej w Koszalinie";

const logo = fs.readFileSync(LOGO);

// Strona tytułowa
const tytul = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 1400, after: 200 }, children: [new ImageRun({ type: "png", data: logo, transformation: { width: 150, height: 150 } })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 }, children: [run(PLACOWKA, { size: 24, color: SZARY })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 500, after: 120 }, children: [run("CZYNNOŚCI NAUCZYCIELI", { size: 44, bold: true, color: FIOLET })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 120 }, children: [run("realizowane w ramach czasu pracy", { size: 30, color: FIOLET })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 }, children: [run("i ustalonego wynagrodzenia", { size: 30, color: FIOLET })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 }, border: { top: { style: BorderStyle.SINGLE, size: 12, color: POMARANCZ, space: 10 } }, children: [run("Wykaz i zasady przydziału zgodnie z art. 42 ust. 2 ustawy z dnia 26 stycznia 1982 r. – Karta Nauczyciela", { size: 22, color: SZARY })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 600, after: 60 }, children: [run("Rok szkolny " + ROK, { size: 26, bold: true, color: POMARANCZ })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [run("Dokument wewnętrzny dla dyrektora, wychowawców, nauczycieli i specjalistów", { size: 20, color: SZARY })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 1800, after: 0 }, children: [run("Stan prawny: wrzesień 2026 r.", { size: 18, color: SZARY })] }),
];

// 1. Cel i zakres
const s1 = [
  h1("1. Cel i zakres dokumentu"),
  p("Dokument porządkuje, jakie zajęcia i czynności nauczyciel wykonuje w ramach obowiązującego go czasu pracy oraz wynagrodzenia zasadniczego, a które z zadań są wynagradzane odrębnie. Służy dyrektorowi do sporządzenia przydziału czynności na rok szkolny, a nauczycielom do jasnego rozgraniczenia obowiązków."),
  p("Wykaz obejmuje trzy grupy czynności wymienione w art. 42 ust. 2 Karty Nauczyciela, uzupełnione o zadania wynikające z przepisów o kształceniu specjalnym i pomocy psychologiczno-pedagogicznej, które w placówce terapeutycznej mają szczególne znaczenie."),
  odstep(40),
  uwaga("Zastrzeżenie.", "Wykaz ma charakter pomocniczy i nie zastępuje statutu, regulaminu wynagradzania organu prowadzącego ani umowy o pracę. W placówkach niepublicznych Karta Nauczyciela stosowana jest w zakresie określonym w art. 91b, a zakres obowiązków ustala statut i umowa o pracę. Przed wdrożeniem wykaz należy dostosować do własnego statutu i uchwał organu prowadzącego oraz zweryfikować z aktualnym tekstem jednolitym ustawy."),
];

// 2. Podstawa prawna
const s2 = [
  h1("2. Podstawa prawna"),
  numbered([run("Ustawa z dnia 26 stycznia 1982 r. – Karta Nauczyciela", { bold: true }), run(" (t.j. Dz. U. z 2024 r. poz. 986 ze zm.) – w szczególności: art. 6 (obowiązki nauczyciela), art. 30 (składniki wynagrodzenia), art. 34–34a (dodatki), art. 35 (godziny ponadwymiarowe i doraźne zastępstwa), art. 42 ust. 1–3, 7 i 7a (czas pracy, pensum, ewidencja), art. 42c ust. 3 (praca w dniu wolnym).")], "pp"),
  numbered([run("Ustawa z dnia 14 grudnia 2016 r. – Prawo oświatowe", { bold: true }), run(" (t.j. Dz. U. z 2024 r. poz. 737 ze zm.) – art. 68 (zadania dyrektora), art. 98 i 102 (statut), art. 127 (kształcenie specjalne).")], "pp"),
  numbered([run("Rozporządzenie MEN z dnia 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym", { bold: true }), run(" (t.j. Dz. U. z 2020 r. poz. 1309) – zespół opracowujący IPET, wielospecjalistyczna ocena poziomu funkcjonowania (WOPF), zajęcia rewalidacyjne.")], "pp"),
  numbered([run("Rozporządzenie MEN z dnia 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej", { bold: true }), run(" (t.j. Dz. U. z 2023 r. poz. 1798) – zajęcia specjalistyczne, zadania nauczycieli i specjalistów.")], "pp"),
  numbered([run("Rozporządzenie MEN z dnia 25 sierpnia 2017 r. w sprawie sposobu prowadzenia dokumentacji przebiegu nauczania", { bold: true }), run(" (Dz. U. z 2017 r. poz. 1646 ze zm.) – dzienniki, arkusze ocen, dokumentacja zajęć.")], "pp"),
  numbered([run("Rozporządzenie MENiS z dnia 31 grudnia 2002 r. w sprawie bezpieczeństwa i higieny w publicznych i niepublicznych szkołach i placówkach", { bold: true }), run(" (t.j. Dz. U. z 2020 r. poz. 1604) – dyżury i opieka nad uczniami.")], "pp"),
  numbered([run("Rozporządzenie MEN z dnia 25 maja 2018 r. w sprawie warunków i sposobu organizowania krajoznawstwa i turystyki", { bold: true }), run(" (Dz. U. z 2018 r. poz. 1055) – wycieczki i wyjścia.")], "pp"),
  numbered([run("Rozporządzenie MENiS z dnia 31 stycznia 2005 r. w sprawie wysokości minimalnych stawek wynagrodzenia zasadniczego nauczycieli", { bold: true }), run(" (t.j. Dz. U. z 2014 r. poz. 416 ze zm.) – minimalne stawki, wykaz prac trudnych i uciążliwych.")], "pp"),
  numbered([run("Regulamin wynagradzania nauczycieli", { bold: true }), run(" uchwalony przez organ prowadzący (art. 30 ust. 6 Karty Nauczyciela) oraz statut placówki – wysokość dodatków, szczegółowy katalog zadań statutowych.")], "pp"),
];

// 3. Zasada ogólna
const s3 = [
  h1("3. Zasada ogólna: 40 godzin tygodniowo w trzech grupach czynności"),
  p("Czas pracy nauczyciela zatrudnionego w pełnym wymiarze nie może przekraczać 40 godzin tygodniowo (art. 42 ust. 1). W ramach tego czasu i w ramach ustalonego wynagrodzenia nauczyciel realizuje trzy grupy zadań:"),
  cyt("Art. 42 ust. 2. W ramach czasu pracy, o którym mowa w ust. 1, oraz ustalonego wynagrodzenia nauczyciel obowiązany jest realizować: 1) zajęcia dydaktyczne, wychowawcze i opiekuńcze, prowadzone bezpośrednio z uczniami lub wychowankami albo na ich rzecz, w wymiarze określonym w ust. 3 lub ustalonym na podstawie ust. 4a albo ust. 7; 2) inne zajęcia i czynności wynikające z zadań statutowych szkoły, w tym zajęcia opiekuńcze i wychowawcze uwzględniające potrzeby i zainteresowania uczniów; 3) zajęcia i czynności związane z przygotowaniem się do zajęć, samokształceniem i doskonaleniem zawodowym."),
  odstep(40),
  tabela(
    ["Grupa", "Co obejmuje", "Wymiar", "Ewidencja"],
    [
      [["I. Pensum", "art. 42 ust. 2 pkt 1"], "Zajęcia dydaktyczne, wychowawcze i opiekuńcze prowadzone bezpośrednio z uczniami lub wychowankami albo na ich rzecz.", "Tygodniowy obowiązkowy wymiar godzin zajęć (art. 42 ust. 3 i 7), np. 18, 20, 22, 25 godzin.", "Rejestrowane i rozliczane w okresach tygodniowych w dziennikach lekcyjnych lub dziennikach zajęć (art. 42 ust. 7a)."],
      [["II. Zadania statutowe", "art. 42 ust. 2 pkt 2"], "Inne zajęcia i czynności wynikające z zadań statutowych placówki, w tym zajęcia opiekuńcze i wychowawcze uwzględniające potrzeby i zainteresowania uczniów oraz godzina dostępności.", "Bez sztywnego wymiaru godzinowego; przydziela dyrektor. Łącznie z pensum i grupą III nie więcej niż 40 godzin tygodniowo.", "Ustawa nie nakazuje ewidencji godzinowej. Dyrektor może wymagać harmonogramu (np. dyżurów, godzin dostępności) i sprawozdania."],
      [["III. Przygotowanie i rozwój", "art. 42 ust. 2 pkt 3"], "Przygotowanie się do zajęć, samokształcenie i doskonalenie zawodowe.", "Bez wymiaru godzinowego; nauczyciel organizuje ten czas samodzielnie, także poza placówką.", "Nie podlega ewidencji. Udział w szkoleniach dokumentuje się zaświadczeniami."],
    ],
    [1900, 3300, 2400, 2560], { zebra: true, boldCol: 0 }
  ),
  odstep(120),
  p([run("Wniosek praktyczny. ", { bold: true, color: FIOLET }), run("Wynagrodzenie zasadnicze obejmuje wszystkie trzy grupy łącznie. Za czynności z grupy II i III nie przysługuje odrębna zapłata, o ile przepis szczególny nie stanowi inaczej (np. dodatek funkcyjny za wychowawstwo). Odrębnie płatne są wyłącznie godziny ponadwymiarowe i doraźne zastępstwa, czyli zajęcia z grupy I przydzielone powyżej pensum (art. 35).")]),
];

// 4. Pensum
const s4 = [
  h1("4. Tygodniowy obowiązkowy wymiar zajęć (pensum) – orientacyjnie"),
  p("Pensum wyznacza granicę między zajęciami wynagradzanymi w ramach wynagrodzenia zasadniczego a godzinami ponadwymiarowymi. Poniższe wartości wynikają z art. 42 ust. 3 i ust. 7 Karty Nauczyciela; dla stanowisk ustalanych przez organ prowadzący obowiązuje jego uchwała."),
  tabela(
    ["Stanowisko", "Pensum tygodniowe", "Podstawa"],
    [
      ["Nauczyciele przedszkoli (grupy dzieci młodszych)", "25 godzin", "art. 42 ust. 3"],
      ["Nauczyciele przedszkoli pracujący z grupami dzieci 6-letnich", "22 godziny", "art. 42 ust. 3"],
      ["Nauczyciele przedszkoli specjalnych, szkół podstawowych i ponadpodstawowych, w tym specjalnych", "18 godzin", "art. 42 ust. 3"],
      ["Wychowawcy świetlic szkolnych", "26 godzin", "art. 42 ust. 3"],
      ["Nauczyciele bibliotekarze", "30 godzin", "art. 42 ust. 3"],
      ["Wychowawcy w specjalnych ośrodkach szkolno-wychowawczych, internatach, młodzieżowych ośrodkach wychowawczych i socjoterapii", "24 godziny", "art. 42 ust. 3"],
      ["Nauczyciele poradni psychologiczno-pedagogicznych", "20 godzin", "art. 42 ust. 3"],
      ["Pedagog, pedagog specjalny, psycholog, logopeda, terapeuta pedagogiczny, doradca zawodowy (poza poradnią)", "ustala organ prowadzący, nie więcej niż 22 godziny", "art. 42 ust. 7 pkt 3 lit. b"],
      ["Nauczyciel współorganizujący kształcenie (tzw. nauczyciel wspomagający) z kwalifikacjami z pedagogiki specjalnej", "ustala organ prowadzący, nie więcej niż 20 godzin", "art. 42 ust. 7 pkt 3 lit. c"],
      ["Nauczyciel łączący stanowiska o różnym pensum", "iloraz łącznej liczby godzin i sumy części etatów", "art. 42 ust. 5c"],
    ],
    [5000, 2800, 2360], { zebra: true }
  ),
  odstep(100),
  uwaga("Długość godziny zajęć.", "Godzina lekcyjna trwa 45 minut, godzina zajęć w przedszkolu 60 minut, godzina zajęć rewalidacyjnych 60 minut, a zajęcia specjalistyczne pomocy psychologiczno-pedagogicznej 45 minut, z możliwością dzielenia czasu w uzasadnionych przypadkach. Godzina dostępności trwa 60 minut."),
];

// 5. Wykaz czynności – Grupa I
const GI = [
  ["1", "Zajęcia edukacyjne zgodnie z planem nauczania (lekcje, zajęcia w oddziale przedszkolnym, zajęcia edukacyjne w szkole specjalnej).", "Nauczyciele przedmiotów, wychowania przedszkolnego, edukacji wczesnoszkolnej", "Wymiar wg pensum; ewidencja w dzienniku."],
  ["2", "Zajęcia rewalidacyjne dla uczniów z orzeczeniem o potrzebie kształcenia specjalnego (m.in. korekcyjne, usprawniające, rozwijające komunikację, orientację przestrzenną, terapia SI wg kwalifikacji).", "Nauczyciele i specjaliści z kwalifikacjami z pedagogiki specjalnej", "Wynikają z IPET; wymiar określa arkusz organizacji."],
  ["3", "Zajęcia specjalistyczne pomocy psychologiczno-pedagogicznej: korekcyjno-kompensacyjne, logopedyczne, rozwijające kompetencje emocjonalno-społeczne, inne o charakterze terapeutycznym.", "Specjaliści, nauczyciele z kwalifikacjami", "Zaliczane do pensum; nie mogą być przydzielane jako zadanie statutowe (art. 42 ust. 2d)."],
  ["4", "Zajęcia dydaktyczno-wyrównawcze, rozwijające uzdolnienia, rozwijające umiejętności uczenia się, zindywidualizowana ścieżka kształcenia, porady i konsultacje dla uczniów.", "Nauczyciele, specjaliści", "Formy pomocy psychologiczno-pedagogicznej; w pensum lub jako godziny ponadwymiarowe."],
  ["5", "Zajęcia rewalidacyjno-wychowawcze dla dzieci z niepełnosprawnością intelektualną w stopniu głębokim oraz zajęcia wczesnego wspomagania rozwoju dziecka (WWRD).", "Nauczyciele i specjaliści wg kwalifikacji", "Wymiar wynika z opinii lub orzeczenia i arkusza organizacji."],
  ["6", "Indywidualne nauczanie, indywidualne obowiązkowe roczne przygotowanie przedszkolne, zajęcia indywidualne z uczniem w placówce.", "Nauczyciele wskazani przez dyrektora", "Godziny w pensum lub ponadwymiarowe."],
  ["7", "Praca nauczyciela współorganizującego kształcenie w oddziale: udział w zajęciach, praca z uczniem z orzeczeniem, wsparcie nauczyciela prowadzącego.", "Nauczyciel współorganizujący (wspomagający)", "Cały wymiar pensum realizowany w oddziale."],
  ["8", "Diagnoza, badania, konsultacje i interwencje prowadzone bezpośrednio z uczniem lub na jego rzecz przez pedagoga, pedagoga specjalnego, psychologa, logopedę, terapeutę pedagogicznego.", "Specjaliści", "Zadania z rozporządzenia o pomocy psychologiczno-pedagogicznej realizowane w pensum specjalisty."],
  ["9", "Zajęcia opiekuńczo-wychowawcze w świetlicy oraz zajęcia z uczniami w bibliotece.", "Wychowawcy świetlicy, nauczyciele bibliotekarze", "W pensum tych stanowisk; dla pozostałych nauczycieli tylko jako godziny ponadwymiarowe."],
  ["10", "Udział w przeprowadzaniu części ustnej egzaminu maturalnego.", "Nauczyciele szkół ponadpodstawowych", "art. 42 ust. 2b pkt 1"],
  ["11", "Zajęcia na kwalifikacyjnych kursach zawodowych.", "Nauczyciele kształcenia zawodowego", "art. 42 ust. 2c"],
];

const GII = [
  // [obszar, czynności]
  ["A. Opieka i bezpieczeństwo", [
    "Dyżury nauczycielskie przed zajęciami, w czasie przerw i po zajęciach zgodnie z harmonogramem dyżurów.",
    "Opieka nad uczniami w czasie uroczystości, apeli, imprez placówki, konkursów, zawodów, wyjść i wycieczek (kierownik lub opiekun wycieczki).",
    "Sprawowanie opieki nad uczniami dowożonymi w czasie oczekiwania na zajęcia lub odjazd, jeśli statut tak stanowi.",
    "Zapoznanie uczniów z regulaminami, zasadami bezpieczeństwa i procedurami obowiązującymi w placówce; reagowanie na sytuacje zagrożenia zgodnie z procedurami.",
    "Pełnienie funkcji wychowawcy oddziału: prowadzenie spraw wychowawczych, dokumentacji oddziału, koordynowanie pomocy dla uczniów.",
  ]],
  ["B. Współpraca z rodzicami i opiekunami", [
    "Godzina dostępności: 1 godzina tygodniowo (przy zatrudnieniu poniżej 1/2 etatu – 1 godzina na 2 tygodnie), w której nauczyciel prowadzi konsultacje dla uczniów, wychowanków lub rodziców (art. 42 ust. 2f). Przy pensum poniżej 6 godzin tygodniowo wymiar ustala dyrektor (art. 42 ust. 2g).",
    "Zebrania z rodzicami, konsultacje indywidualne, dni otwarte; informowanie o postępach, trudnościach i zachowaniu ucznia.",
    "Bieżąca komunikacja z rodzicami (dziennik elektroniczny, kontakt telefoniczny, spotkania) oraz uzgadnianie form wsparcia dziecka.",
    "Udział rodziców w spotkaniach zespołu ds. IPET: zawiadamianie, omawianie WOPF i programu, odbieranie kopii dokumentów przez rodziców.",
    "Współdziałanie z rodzicami w realizacji zaleceń orzeczeń i opinii poradni.",
  ]],
  ["C. Praca zespołowa i rada pedagogiczna", [
    "Udział w zebraniach rady pedagogicznej oraz realizacja jej uchwał; udział w szkoleniowych radach pedagogicznych.",
    "Praca w zespołach nauczycieli: przedmiotowych, wychowawczych, zadaniowych, ds. ewaluacji, ds. pomocy psychologiczno-pedagogicznej.",
    "Udział w zespole opracowującym IPET: opracowanie programu w terminie 30 dni od otrzymania orzeczenia lub do 30 września, dokonywanie WOPF co najmniej dwa razy w roku szkolnym, ocena efektywności i modyfikacja IPET, spotkania zespołu co najmniej dwa razy w roku (rozporządzenie o kształceniu specjalnym).",
    "Planowanie i koordynowanie pomocy psychologiczno-pedagogicznej dla ucznia (wychowawca, specjalista wyznaczony przez dyrektora), rozpoznawanie potrzeb i możliwości uczniów.",
    "Współpraca z poradnią psychologiczno-pedagogiczną, placówkami doskonalenia, ośrodkami terapii, instytucjami pomocy społecznej i ochrony zdrowia oraz innymi podmiotami działającymi na rzecz dziecka.",
    "Współpraca nauczyciela współorganizującego z nauczycielami prowadzącymi zajęcia i specjalistami: dobór form i metod, dostosowania, wspólne planowanie.",
  ]],
  ["D. Dokumentacja i planowanie pracy", [
    "Prowadzenie dzienników lekcyjnych i dzienników zajęć (w tym zajęć rewalidacyjnych, specjalistycznych i innych form pomocy), arkuszy ocen, dokumentacji wychowawcy.",
    "Prowadzenie dokumentacji kształcenia specjalnego: IPET, WOPF, karty obserwacji, dokumentacja badań i czynności uzupełniających specjalistów.",
    "Opracowanie planów pracy, rozkładów materiału lub planów wynikowych, programów zajęć rewalidacyjnych i specjalistycznych, wymagań edukacyjnych i dostosowań.",
    "Ocenianie bieżące, klasyfikacyjne i opisowe, sporządzanie ocen i opinii o uczniu, informacji dla poradni i innych instytucji na wniosek dyrektora.",
    "Udział w tworzeniu i realizacji programu wychowawczo-profilaktycznego, planu pracy placówki, ewaluacji wewnętrznej, sprawozdań semestralnych i rocznych.",
  ]],
  ["E. Egzaminy, klasyfikacja, rekrutacja", [
    "Udział w komisjach egzaminu ósmoklasisty, egzaminu zawodowego, egzaminu potwierdzającego kwalifikacje w zawodzie oraz egzaminu maturalnego, z wyjątkiem części ustnej (art. 42 ust. 2b pkt 2).",
    "Udział w egzaminach klasyfikacyjnych, poprawkowych i sprawdzianach wiadomości; praca w komisjach powoływanych przez dyrektora.",
    "Udział w pracach komisji rekrutacyjnej, stypendialnej i innych komisji wewnętrznych powołanych przez dyrektora.",
  ]],
  ["F. Organizacja życia placówki", [
    "Organizowanie i prowadzenie uroczystości, apeli, konkursów, projektów edukacyjnych, wystaw prac, dni tematycznych, spotkań integracyjnych z udziałem rodziców.",
    "Zajęcia opiekuńcze i wychowawcze uwzględniające potrzeby i zainteresowania uczniów (koła zainteresowań, zajęcia rozwijające) w wymiarze ustalonym przez dyrektora, z wyłączeniem zajęć świetlicowych i zajęć pomocy psychologiczno-pedagogicznej (art. 42 ust. 2d).",
    "Opieka nad samorządem uczniowskim, wolontariatem, organizacjami i projektami uczniowskimi.",
    "Opieka nad przydzieloną salą, pracownią, gabinetem terapeutycznym, pomocami dydaktycznymi i sprzętem; udział w inwentaryzacji; dbałość o estetykę i bezpieczeństwo pomieszczeń.",
    "Udział w promocji placówki: dni otwarte, materiały informacyjne, prowadzenie działań przydzielonych przez dyrektora zgodnie ze statutem.",
  ]],
  ["G. Wsparcie innych nauczycieli", [
    "Pełnienie funkcji mentora nauczyciela początkującego lub opieka nad praktykami studenckimi, jeśli nie jest to wynagradzane dodatkiem funkcyjnym na podstawie regulaminu wynagradzania.",
    "Prowadzenie zajęć otwartych i lekcji koleżeńskich, dzielenie się wiedzą w ramach wewnątrzszkolnego doskonalenia nauczycieli.",
    "Doraźna pomoc koleżeńska w opiece nad uczniami w sytuacjach nagłych, zgodnie z poleceniem dyrektora.",
  ]],
];

const GIII = [
  ["Przygotowanie się do zajęć", [
    "Planowanie zajęć, opracowywanie scenariuszy, kart pracy, pomocy dydaktycznych i terapeutycznych, w tym dostosowanych do potrzeb uczniów z orzeczeniami.",
    "Sprawdzanie i ocenianie prac uczniów, analiza wyników, przygotowanie informacji zwrotnej.",
    "Przygotowanie sali, sprzętu i materiałów do zajęć; przygotowanie diagnoz i narzędzi używanych przez specjalistów.",
  ]],
  ["Samokształcenie", [
    "Śledzenie zmian w przepisach prawa oświatowego i podstawach programowych.",
    "Studiowanie literatury fachowej, nowych metod terapii i nauczania, narzędzi cyfrowych.",
    "Dążenie do pełni własnego rozwoju osobowego (art. 6 pkt 3 Karty Nauczyciela).",
  ]],
  ["Doskonalenie zawodowe", [
    "Doskonalenie zawodowe zgodnie z potrzebami placówki (art. 6 pkt 3a): udział w szkoleniach rady pedagogicznej, kursach, warsztatach, konferencjach, sieciach współpracy.",
    "Realizacja planu rozwoju zawodowego i przygotowanie do awansu zawodowego; udział w obserwacjach i rozmowach z mentorem.",
    "Udział w studiach podyplomowych i kursach kwalifikacyjnych, jeśli wynika to z potrzeb placówki i zostało uzgodnione z dyrektorem.",
  ]],
];

const s5 = [
  h1("5. Wykaz czynności realizowanych w ramach wynagrodzenia"),
  h2("Grupa I – zajęcia w ramach pensum (art. 42 ust. 2 pkt 1)"),
  p("Zajęcia prowadzone bezpośrednio z uczniami lub wychowankami albo na ich rzecz. To one są liczone w godzinach, ewidencjonowane w dziennikach i stanowią punkt odniesienia dla godzin ponadwymiarowych."),
  tabela(["Lp.", "Rodzaj zajęć", "Kto realizuje", "Uwagi"], GI, [600, 4700, 2400, 2460], { zebra: true }),
  odstep(100),
  uwaga("Ważne.", "Zajęcia świetlicowe oraz zajęcia z zakresu pomocy psychologiczno-pedagogicznej nie mogą być przydzielane jako inne zajęcia statutowe (art. 42 ust. 2d). Jeśli nauczyciel prowadzi je poza swoim pensum, są to godziny ponadwymiarowe płatne na zasadach z art. 35."),
  h2("Grupa II – inne zajęcia i czynności wynikające z zadań statutowych (art. 42 ust. 2 pkt 2)"),
  p("Czynności z tej grupy przydziela dyrektor. Nie są liczone w godzinach ani dodatkowo płatne, muszą jednak mieścić się w 40-godzinnym tygodniu pracy i wynikać ze statutu placówki. Poniższy katalog należy dopasować do zapisów własnego statutu."),
];
for (const [obszar, lista] of GII) {
  s5.push(new Paragraph({ spacing: { before: 160, after: 60 }, children: [run(obszar, { bold: true, color: FIOLET, size: 21 })] }));
  for (const l of lista) s5.push(bullet(l));
}
s5.push(h2("Grupa III – przygotowanie do zajęć, samokształcenie i doskonalenie (art. 42 ust. 2 pkt 3)"));
s5.push(p("Czas na te czynności nauczyciel organizuje samodzielnie, także poza placówką. Nie podlega on ewidencji, ale stanowi część 40-godzinnego tygodnia pracy i jest objęty wynagrodzeniem zasadniczym."));
for (const [obszar, lista] of GIII) {
  s5.push(new Paragraph({ spacing: { before: 160, after: 60 }, children: [run(obszar, { bold: true, color: FIOLET, size: 21 })] }));
  for (const l of lista) s5.push(bullet(l));
}

// 6. Poza wynagrodzeniem zasadniczym
const s6 = [
  h1("6. Czynności wynagradzane odrębnie lub poza stosunkiem pracy"),
  p("Poniższe zadania nie mieszczą się w wynagrodzeniu zasadniczym. Ich przydzielenie wymaga odpowiedniego składnika wynagrodzenia albo odrębnej umowy."),
  tabela(
    ["Czynność", "Forma wynagrodzenia", "Podstawa"],
    [
      ["Godziny ponadwymiarowe – zajęcia z grupy I przydzielone powyżej pensum (do 1/4 pensum, za zgodą nauczyciela do 1/2).", "Wynagrodzenie za każdą zrealizowaną godzinę, według stawki osobistego zaszeregowania.", "art. 35 ust. 1 i 3"],
      ["Doraźne zastępstwa za nieobecnego nauczyciela.", "Wynagrodzenie za każdą godzinę zastępstwa.", "art. 35 ust. 2a i 3"],
      ["Sprawowanie funkcji wychowawcy klasy.", "Dodatek funkcyjny nie niższy niż 300 zł miesięcznie.", "art. 34a"],
      ["Funkcje kierownicze, mentor nauczyciela początkującego, opiekun praktyk (jeśli regulamin tak stanowi).", "Dodatek funkcyjny w wysokości z regulaminu wynagradzania.", "art. 30 ust. 6, regulamin"],
      ["Praca w trudnych lub uciążliwych warunkach, np. zajęcia rewalidacyjno-wychowawcze, praca w szkołach i przedszkolach specjalnych, indywidualne nauczanie dziecka z niepełnosprawnością.", "Dodatek za warunki pracy w wysokości z regulaminu wynagradzania.", "art. 34, rozporządzenie z 31.01.2005 r."],
      ["Praca w dniu wolnym od pracy (np. wycieczka, zawody, festyn w sobotę).", "Inny dzień wolny; w szczególnie uzasadnionych przypadkach odrębne wynagrodzenie.", "art. 42c ust. 3"],
      ["Sprawdzanie prac egzaminacyjnych jako egzaminator OKE.", "Umowa cywilnoprawna z okręgową komisją egzaminacyjną.", "poza stosunkiem pracy"],
      ["Zajęcia finansowane z projektów zewnętrznych, zajęcia komercyjne, zajęcia dodatkowe na zlecenie organu prowadzącego poza arkuszem organizacji.", "Odrębna umowa lub godziny ponadwymiarowe, zgodnie z warunkami projektu.", "umowa, regulamin projektu"],
      ["Szczególne osiągnięcia dydaktyczne, wychowawcze i opiekuńcze.", "Nagroda dyrektora lub organu prowadzącego; dodatek motywacyjny.", "art. 49, art. 30 ust. 1 pkt 2"],
    ],
    [4600, 3300, 2260], { zebra: true }
  ),
];

// 7. Zasady przydziału
const s7 = [
  h1("7. Zasady przydzielania i dokumentowania czynności"),
  numbered("Dyrektor ustala przydział zajęć z grupy I w arkuszu organizacji na rok szkolny, a przydział czynności z grupy II przedstawia radzie pedagogicznej na zebraniu rozpoczynającym rok szkolny; każdy nauczyciel otrzymuje pisemny przydział czynności (załącznik nr 1).", "zas"),
  numbered("Czynności statutowe rozdziela się równomiernie, z uwzględnieniem wymiaru zatrudnienia, stanowiska, kwalifikacji i obciążenia zajęciami z grupy I; nauczycielowi zatrudnionemu w niepełnym wymiarze przydziela się je proporcjonalnie.", "zas"),
  numbered("Suma zajęć z grupy I, czynności statutowych, godziny dostępności i czasu na przygotowanie nie może przekroczyć 40 godzin tygodniowo; dyrektor rozpatruje uwagi nauczyciela o nadmiernym obciążeniu.", "zas"),
  numbered("Godziny dostępności nauczyciel realizuje według harmonogramu podanego do wiadomości rodziców i uczniów; termin i forma (stacjonarnie, zdalnie) są uzgadniane z dyrektorem odpowiednio do potrzeb.", "zas"),
  numbered("Zajęcia z grupy I są rejestrowane w dziennikach w okresach tygodniowych (art. 42 ust. 7a). Czynności z grupy II i III nie wymagają ewidencji godzinowej; dyrektor może wymagać harmonogramu dyżurów, wykazu zebrań i sprawozdania z realizacji przydzielonych zadań na koniec półrocza i roku.", "zas"),
  numbered("Zadania zespołu ds. IPET i WOPF są dokumentowane zgodnie z rozporządzeniem o kształceniu specjalnym: kopię IPET i WOPF otrzymują rodzice, a terminy spotkań zespołu odnotowuje się w dokumentacji ucznia.", "zas"),
  numbered("Zadania wykraczające poza wykaz i statut nauczyciel podejmuje dobrowolnie, po uzgodnieniu z dyrektorem, a jeśli są to zajęcia z grupy I powyżej pensum – jako godziny ponadwymiarowe.", "zas"),
  numbered("Przydział czynności może być zmieniony w ciągu roku szkolnego w związku ze zmianą organizacji pracy, długotrwałą nieobecnością nauczyciela lub zmianą potrzeb uczniów; zmianę potwierdza się na piśmie.", "zas"),
];

// Załącznik 1 – wzór przydziału
function wierszPrzydzialu(lp, czynnosc, grupa) {
  return [lp, czynnosc, grupa, "", ""];
}
const zal1 = [
  new Paragraph({ pageBreakBefore: true, alignment: AlignmentType.RIGHT, spacing: { after: 60 }, children: [run("Załącznik nr 1", { bold: true, color: POMARANCZ })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [run("PRZYDZIAŁ CZYNNOŚCI NAUCZYCIELA", { bold: true, size: 26, color: FIOLET })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: [run("w ramach czasu pracy i ustalonego wynagrodzenia (art. 42 ust. 2 Karty Nauczyciela) – rok szkolny " + ROK, { size: 19, color: SZARY })] }),
  tabela(
    ["Pole", "Treść"],
    [
      ["Imię i nazwisko nauczyciela", ""],
      ["Stanowisko / stopień awansu", ""],
      ["Wymiar zatrudnienia", "……… / ……… etatu"],
      ["Tygodniowy obowiązkowy wymiar zajęć (pensum)", "……… godzin"],
      ["Przydzielone godziny ponadwymiarowe", "……… godzin (płatne odrębnie, art. 35)"],
      ["Wychowawstwo oddziału", "TAK / NIE – oddział: ………"],
    ],
    [4200, 5960], { boldCol: 0 }
  ),
  odstep(140),
  new Paragraph({ spacing: { before: 100, after: 80 }, children: [run("I. Zajęcia w ramach pensum (art. 42 ust. 2 pkt 1)", { bold: true, color: FIOLET })] }),
  tabela(
    ["Lp.", "Rodzaj zajęć", "Oddział / uczeń", "Godz. tyg.", "Uwagi"],
    [1, 2, 3, 4, 5, 6].map((i) => [String(i), "", "", "", ""]),
    [600, 4200, 2500, 1100, 1760]
  ),
  odstep(140),
  new Paragraph({ spacing: { before: 100, after: 80 }, children: [run("II. Czynności statutowe (art. 42 ust. 2 pkt 2)", { bold: true, color: FIOLET })] }),
  tabela(
    ["Lp.", "Czynność", "Obszar", "Termin / wymiar", "Uwagi"],
    [
      wierszPrzydzialu("1", "Godzina dostępności (konsultacje dla uczniów i rodziców)", "B", ),
      wierszPrzydzialu("2", "Dyżury według harmonogramu", "A"),
      wierszPrzydzialu("3", "Zebrania i konsultacje z rodzicami", "B"),
      wierszPrzydzialu("4", "Udział w zebraniach rady pedagogicznej i zespołach", "C"),
      wierszPrzydzialu("5", "Zespół ds. IPET / WOPF – uczniowie: ………", "C"),
      wierszPrzydzialu("6", "Prowadzenie dokumentacji (dzienniki, IPET, WOPF, plany)", "D"),
      wierszPrzydzialu("7", "Opieka nad salą / gabinetem / pomocami", "F"),
      wierszPrzydzialu("8", "Organizacja uroczystości, konkursu, projektu: ………", "F"),
      wierszPrzydzialu("9", "Udział w komisjach: ………", "E"),
      wierszPrzydzialu("10", "Inne wynikające ze statutu: ………", ""),
      wierszPrzydzialu("11", "", ""),
      wierszPrzydzialu("12", "", ""),
    ],
    [600, 4200, 900, 2400, 2060]
  ),
  odstep(140),
  new Paragraph({ spacing: { before: 100, after: 80 }, children: [run("III. Doskonalenie zawodowe planowane na rok szkolny (art. 42 ust. 2 pkt 3)", { bold: true, color: FIOLET })] }),
  tabela(["Lp.", "Forma doskonalenia", "Organizator / termin", "Uwagi"], [1, 2, 3].map((i) => [String(i), "", "", ""]), [600, 4600, 2900, 2060]),
  odstep(200),
  p("Oświadczam, że zapoznałam/zapoznałem się z przydziałem czynności na rok szkolny " + ROK + " oraz z wykazem czynności realizowanych w ramach wynagrodzenia.", { size: 19 }),
  odstep(300),
  new Table({
    width: { size: 10160, type: WidthType.DXA }, columnWidths: [5080, 5080],
    rows: [new TableRow({ children: [
      new TableCell({ width: { size: 5080, type: WidthType.DXA }, borders: { top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" } }, children: [
        new Paragraph({ alignment: AlignmentType.CENTER, children: [run("………………………………………………", { size: 18 })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, children: [run("data i podpis nauczyciela", { size: 17, color: SZARY })] }),
      ] }),
      new TableCell({ width: { size: 5080, type: WidthType.DXA }, borders: { top: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, left: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" }, right: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" } }, children: [
        new Paragraph({ alignment: AlignmentType.CENTER, children: [run("………………………………………………", { size: 18 })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, children: [run("data i podpis dyrektora", { size: 17, color: SZARY })] }),
      ] }),
    ] })],
  }),
];

// Załącznik 2 – lista kontrolna dla nauczyciela specjalisty i współorganizującego
const zal2 = [
  new Paragraph({ pageBreakBefore: true, alignment: AlignmentType.RIGHT, spacing: { after: 60 }, children: [run("Załącznik nr 2", { bold: true, color: POMARANCZ })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 }, children: [run("LISTA KONTROLNA – NAUCZYCIEL SPECJALISTA I NAUCZYCIEL WSPÓŁORGANIZUJĄCY", { bold: true, size: 24, color: FIOLET })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 }, children: [run("Zadania w ramach wynagrodzenia w placówce realizującej kształcenie specjalne i terapię", { size: 19, color: SZARY })] }),
  tabela(
    ["Zadanie", "Termin", "Grupa", "Zrobione"],
    [
      ["Udział w opracowaniu IPET dla każdego ucznia z orzeczeniem", "do 30 września lub 30 dni od orzeczenia", "II", "☐"],
      ["Wielospecjalistyczna ocena poziomu funkcjonowania (WOPF)", "co najmniej 2 razy w roku", "II", "☐"],
      ["Spotkania zespołu ds. IPET z udziałem rodziców", "co najmniej 2 razy w roku", "II", "☐"],
      ["Ocena efektywności pomocy psychologiczno-pedagogicznej i wnioski do dalszej pracy", "przed zakończeniem każdego okresu", "II", "☐"],
      ["Zajęcia rewalidacyjne i specjalistyczne zgodnie z arkuszem organizacji", "cały rok, ewidencja w dzienniku", "I", "☐"],
      ["Diagnoza potrzeb i możliwości uczniów, obserwacja w oddziale", "wrzesień i na bieżąco", "I", "☐"],
      ["Dostosowanie wymagań edukacyjnych i materiałów do potrzeb uczniów", "na bieżąco", "III", "☐"],
      ["Konsultacje dla rodziców w godzinie dostępności", "co tydzień według harmonogramu", "II", "☐"],
      ["Współpraca z poradnią psychologiczno-pedagogiczną i innymi instytucjami", "według potrzeb", "II", "☐"],
      ["Prowadzenie dziennika zajęć specjalisty i dokumentacji badań", "na bieżąco", "II", "☐"],
      ["Wsparcie nauczycieli i wychowawców w pracy z uczniem z orzeczeniem", "na bieżąco", "II", "☐"],
      ["Udział w szkoleniach z zakresu metod terapii i pedagogiki specjalnej", "zgodnie z planem doskonalenia", "III", "☐"],
      ["Sprawozdanie z realizacji zadań dla dyrektora", "koniec półrocza i roku", "II", "☐"],
    ],
    [4700, 2900, 900, 1660], { zebra: true }
  ),
  odstep(200),
  uwaga("Granica pensum.", "Wszystkie zajęcia prowadzone bezpośrednio z uczniem przez specjalistę mieszczą się w jego pensum (nie więcej niż 22 godziny, dla nauczyciela współorganizującego nie więcej niż 20). Zajęcia przydzielone ponad ten wymiar są godzinami ponadwymiarowymi. Nie wolno przydzielać zajęć pomocy psychologiczno-pedagogicznej jako czynności statutowych (art. 42 ust. 2d)."),
];

// ---------- dokument ----------
const naglowek = new Header({
  children: [new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: 10160 }],
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: FIOLET, space: 4 } }, spacing: { after: 200 },
    children: [
      new ImageRun({ type: "png", data: logo, transformation: { width: 26, height: 26 } }),
      run("   " + PLACOWKA, { size: 16, color: SZARY }),
      run("\tCzynności nauczycieli w ramach wynagrodzenia – " + ROK, { size: 16, color: FIOLET }),
    ],
  })],
});
const stopka = new Footer({
  children: [new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 100 },
    border: { top: { style: BorderStyle.SINGLE, size: 6, color: POMARANCZ, space: 4 } },
    children: [run("Strona ", { size: 16, color: SZARY }), new TextRun({ children: [PageNumber.CURRENT], font: F, size: 16, color: SZARY }), run("   •   podstawa: art. 42 ust. 2 ustawy – Karta Nauczyciela", { size: 16, color: SZARY })],
  })],
});

const doc = new Document({
  creator: PLACOWKA,
  title: "Czynności nauczycieli w ramach wynagrodzenia " + ROK,
  styles: {
    default: { document: { run: { font: F, size: 20 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: F, size: 28, bold: true, color: FIOLET }, paragraph: { spacing: { before: 320, after: 140 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: F, size: 23, bold: true, color: POMARANCZ }, paragraph: { spacing: { before: 220, after: 100 }, outlineLevel: 1 } },
    ],
  },
  numbering: {
    config: [
      { reference: "punkty", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { run: { color: POMARANCZ, bold: true }, paragraph: { indent: { left: 560, hanging: 280 } } } }] },
      { reference: "pp", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 560, hanging: 360 } } } }] },
      { reference: "zas", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 560, hanging: 360 } } } }] },
    ],
  },
  sections: [
    { properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 } } }, children: tytul },
    { properties: { page: { margin: { top: 1134, bottom: 1134, left: 1134, right: 1134 }, pageNumbers: { start: 1 } } }, headers: { default: naglowek }, footers: { default: stopka },
      children: [...s1, ...s2, ...s3, ...s4, ...s5, ...s6, ...s7, ...zal1, ...zal2] },
  ],
});

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log("zapisano", OUT, buf.length, "B"); });
