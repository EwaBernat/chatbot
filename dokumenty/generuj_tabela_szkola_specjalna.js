// Generator: "Czynności nauczycieli szkoły specjalnej" – tabela porównawcza
// nauczyciel edukacji wczesnoszkolnej (kl. I–III) / nauczyciel przedmiotów (kl. IV–VIII),
// dla nauczycieli zatrudnionych na podstawie Kodeksu pracy w wymiarze 6 godzin dziennie.
// Uruchomienie (z katalogu głównego repozytorium):
//   npm install docx sharp
//   node -e "require('sharp')('logo-lawenda.webp').png().toFile('logo.png')"
//   node dokumenty/generuj_tabela_szkola_specjalna.js logo.png dokumenty/czynnosci-nauczycieli-szkoly-specjalnej.docx [plik.md]
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, HeadingLevel, ShadingType, BorderStyle, ImageRun, Header, Footer,
  PageNumber, TabStopType, VerticalAlign, PageOrientation,
} = require("docx");

const [,, LOGO = "logo.png", OUT = "szkola-specjalna.docx", OUT_MD] = process.argv;

const FIOLET = "2D1B69";
const POMARANCZ = "E8450A";
const SZARY = "555555";
const JASNY2 = "FBEFE9";
const F = "Arial";
const ROK = "2026/2027";
const PLACOWKA = "Pomorskie Centrum Terapii Pedagogicznej w Koszalinie";
const SZER = 15140; // szerokość użyteczna A4 poziomo przy marginesach 850 DXA

// ---------- pomocnicze ----------
const run = (text, o = {}) => new TextRun({ text, font: F, size: o.size || 19, bold: o.bold, italics: o.italics, color: o.color });
const p = (text, o = {}) => new Paragraph({
  alignment: o.align || AlignmentType.JUSTIFIED, spacing: { after: o.after ?? 100, before: o.before ?? 0, line: 270 },
  children: Array.isArray(text) ? text : [run(text, o)],
});
const h1 = (t, pb = false) => new Paragraph({ heading: HeadingLevel.HEADING_1, pageBreakBefore: pb, spacing: { before: 280, after: 120 }, children: [run(t, { size: 26, bold: true, color: FIOLET })] });
const odstep = (n = 80) => new Paragraph({ spacing: { after: n }, children: [] });
const uwaga = (label, text) => {
  const b = { style: BorderStyle.SINGLE, size: 6, color: POMARANCZ };
  return new Table({
    width: { size: SZER, type: WidthType.DXA }, columnWidths: [SZER],
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({
      width: { size: SZER, type: WidthType.DXA }, borders: { top: b, left: b, bottom: b, right: b },
      shading: { type: ShadingType.CLEAR, fill: JASNY2, color: "auto" }, margins: { top: 90, bottom: 90, left: 160, right: 160 },
      children: [new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 0, line: 270 },
        children: [run(label + " ", { bold: true, color: POMARANCZ, size: 18 }), run(text, { size: 18 })] })],
    })] })],
  });
};

const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: "BFB8D6" };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };
const BEZ = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const bezRamek = { top: BEZ, bottom: BEZ, left: BEZ, right: BEZ };

// Treść komórki: string, tablica stringów (akapity) albo Paragraph.
// Prefiksy: "● " robi, "◐ " zależnie od przydziału, "— " nie dotyczy – symbol dostaje kolor.
function cellParas(content, o) {
  return (Array.isArray(content) ? content : [content]).map((c) => {
    if (c instanceof Paragraph) return c;
    const s = String(c);
    const m = s.match(/^([●◐—])\s?(.*)$/s);
    const children = m
      ? [run(m[1] + " ", { size: o.size || 17, bold: true, color: m[1] === "●" ? POMARANCZ : m[1] === "◐" ? "8A6FD1" : "999999" }), run(m[2], { size: o.size || 17, bold: o.bold, color: o.color })]
      : [run(s, { size: o.size || 17, bold: o.bold, color: o.color })];
    return new Paragraph({ alignment: o.align || AlignmentType.LEFT, spacing: { after: 30, line: 250 }, keepNext: o.keepNext, children });
  });
}
function cell(content, width, o = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, borders: o.borders || borders, verticalAlign: o.valign || VerticalAlign.TOP,
    margins: { top: 50, bottom: 50, left: 80, right: 80 }, columnSpan: o.span,
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined,
    children: cellParas(content, o),
  });
}
function naglowekWiersz(naglowki, szer) {
  return new TableRow({ tableHeader: true, children: naglowki.map((n, i) => cell(n, szer[i], { bold: true, color: "FFFFFF", fill: FIOLET, size: 17, valign: VerticalAlign.CENTER })) });
}
function sekcjaWiersz(tytul, szer) {
  return new TableRow({ cantSplit: true, children: [cell(tytul, szer.reduce((a, b) => a + b, 0), { span: szer.length, bold: true, color: FIOLET, fill: "EDE8F7", size: 18, keepNext: true })] });
}
function tabela(naglowki, wiersze, szer, o = {}) {
  let zi = 0;
  const rows = wiersze.map((w) => {
    if (typeof w === "string") { zi = 0; return sekcjaWiersz(w, szer); }
    const fill = o.zebra && zi++ % 2 === 1 ? "F7F5FB" : undefined;
    return new TableRow({ cantSplit: true, children: w.map((c, i) => cell(c, szer[i], { fill, bold: o.boldCol === i, size: o.size, align: o.center && o.center.includes(i) ? AlignmentType.CENTER : undefined })) });
  });
  return new Table({ width: { size: szer.reduce((a, b) => a + b, 0), type: WidthType.DXA }, columnWidths: szer, rows: [naglowekWiersz(naglowki, szer), ...rows] });
}

const logo = fs.readFileSync(LOGO);

// ---------- nagłówek dokumentu ----------
const naglowekDok = [
  new Table({
    width: { size: SZER, type: WidthType.DXA }, columnWidths: [1300, SZER - 1300],
    rows: [new TableRow({ children: [
      new TableCell({ width: { size: 1300, type: WidthType.DXA }, borders: bezRamek, verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({ alignment: AlignmentType.LEFT, children: [new ImageRun({ type: "png", data: logo, transformation: { width: 72, height: 72 } })] })] }),
      new TableCell({ width: { size: SZER - 1300, type: WidthType.DXA }, borders: bezRamek, verticalAlign: VerticalAlign.CENTER,
        children: [
          new Paragraph({ spacing: { after: 40 }, children: [run(PLACOWKA, { size: 18, color: SZARY })] }),
          new Paragraph({ spacing: { after: 40 }, children: [run("CZYNNOŚCI NAUCZYCIELI SZKOŁY SPECJALNEJ", { size: 32, bold: true, color: FIOLET })] }),
          new Paragraph({ spacing: { after: 0 }, children: [run("Tabela porównawcza: nauczyciel edukacji wczesnoszkolnej (klasy I–III) i nauczyciel przedmiotów (klasy IV–VIII) · zatrudnienie na podstawie Kodeksu pracy, 6 godzin dziennie · rok szkolny " + ROK, { size: 19, color: POMARANCZ })] }),
        ] }),
    ] })],
  }),
  new Paragraph({ spacing: { after: 120 }, border: { bottom: { style: BorderStyle.SINGLE, size: 10, color: POMARANCZ, space: 4 } }, children: [] }),
  p("Tabela zbiera wszystkie zajęcia i czynności, które nauczyciele szkoły podstawowej specjalnej wykonują w ramach umówionego czasu pracy i wynagrodzenia, oraz te, które są płatne odrębnie. Nauczyciele są zatrudnieni na podstawie umowy o pracę według Kodeksu pracy, w wymiarze 6 godzin dziennie (30 godzin tygodniowo). Oznacza to, że nie stosuje się pensum, godzin ponadwymiarowych ani podziału czasu pracy z art. 42 Karty Nauczyciela: każda czynność – zajęcia z uczniami, przygotowanie, dokumentacja, zebrania, kontakt z rodzicami – jest pracą w rozumieniu Kodeksu pracy, mieści się w 6-godzinnym dniu i podlega ewidencji czasu pracy. Dla każdej czynności pokazano, jak wygląda ona u nauczyciela edukacji wczesnoszkolnej, a jak u nauczyciela przedmiotów. Dotyczy oddziałów dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim (podstawa programowa ogólna, dostosowana) oraz umiarkowanym lub znacznym (odrębna podstawa programowa), a także oddziałów dla uczniów z autyzmem i z niepełnosprawnościami sprzężonymi."),
  new Table({
    width: { size: SZER, type: WidthType.DXA }, columnWidths: [3785, 3785, 3785, 3785],
    rows: [new TableRow({ children: [
      cell(["● robi", "czynność należy do obowiązków na tym stanowisku"], 3785, { fill: "FBEFE9", size: 17 }),
      cell(["◐ zależnie od przydziału", "wykonuje, jeśli dyrektor przydzieli albo gdy wynika z typu oddziału lub kwalifikacji"], 3785, { fill: "F3F0FA", size: 17 }),
      cell(["— nie dotyczy", "czynność nie występuje na tym stanowisku"], 3785, { fill: "F5F5F5", size: 17 }),
      cell(["Rodzaj czasu pracy: Z zajęcia z uczniami · O organizacja, dokumentacja, współpraca · P przygotowanie i doskonalenie", "wszystkie w 6-godzinnym dniu pracy; „odrębnie” = poza wynagrodzeniem zasadniczym"], 3785, { fill: "EDE8F7", size: 17 }),
    ] })],
  }),
];

// ---------- Tabela A: ramy zatrudnienia ----------
const SZ_A = [3000, 6070, 6070];
const profil = [
  ["Podstawa zatrudnienia", "Umowa o pracę na podstawie Kodeksu pracy; zakres obowiązków ustala pracodawca (art. 94 pkt 1 KP), regulamin pracy i statut szkoły. Z Karty Nauczyciela stosuje się tylko przepisy wskazane w art. 91b ust. 2 KN (m.in. art. 6 – obowiązki nauczyciela, art. 9–9i – awans zawodowy, art. 75–85z – odpowiedzialność dyscyplinarna).", "Tak samo."],
  ["Czas pracy", "6 godzin dziennie, 30 godzin tygodniowo, według rozkładu czasu pracy ustalonego przez pracodawcę (art. 129 KP). W tym czasie mieszczą się zajęcia z uczniami, opieka, przygotowanie, dokumentacja, zebrania i kontakt z rodzicami. Czas pracy jest ewidencjonowany (art. 149 KP). Przy 6-godzinnym dniu przysługuje 15-minutowa przerwa wliczana do czasu pracy (art. 134 KP).", "Tak samo. Liczbę lekcji i dyżurów w 6-godzinnym dniu ustala dyrektor w planie lekcji i rozkładzie czasu pracy tak, aby pozostał czas na przygotowanie i dokumentację."],
  ["Praca ponad wymiar", "Praca ponad 6 godzin dziennie jest dopuszczalna tylko na polecenie pracodawcy i jest ewidencjonowana. Praca powyżej 8 godzin dziennie lub przeciętnie 40 godzin tygodniowo to praca w godzinach nadliczbowych z dodatkiem 50% lub 100% (art. 151–151¹ KP). Przy zatrudnieniu w niepełnym wymiarze umowa powinna określać próg, powyżej którego przysługuje dodatek jak za nadgodziny (art. 151 § 5 KP).", "Tak samo."],
  ["Etap i klasy", "Klasy I–III (I etap edukacyjny). W oddziałach dla uczniów z niepełnosprawnością intelektualną w stopniu umiarkowanym lub znacznym: etap I odrębnej podstawy programowej.", "Klasy IV–VIII (II etap edukacyjny). W oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną nauczyciel prowadzi zajęcia (funkcjonowanie osobiste i społeczne, rozwijające komunikowanie się, rozwijające kreatywność, wychowanie fizyczne), a nie przedmioty."],
  ["Kwalifikacje", "Studia z pedagogiki specjalnej lub studia nauczycielskie plus kwalifikacje z pedagogiki specjalnej odpowiedniej do niepełnosprawności uczniów (rozporządzenie MEN z 1.08.2017 r. w sprawie kwalifikacji).", "Kwalifikacje do nauczania przedmiotu plus kwalifikacje z pedagogiki specjalnej odpowiedniej do niepełnosprawności uczniów (to samo rozporządzenie)."],
  ["Organizacja zajęć", "Jeden nauczyciel prowadzi zintegrowane zajęcia edukacyjne w jednym oddziale i sam ustala podział czasu oraz przerwy według potrzeb uczniów, w granicach rozkładu czasu pracy.", "Nauczyciel prowadzi jeden lub kilka przedmiotów w kilku oddziałach według planu lekcji ustalonego przez dyrektora; lekcja 45 minut."],
  ["Liczebność oddziału", "Do 16 uczniów (niepełnosprawność intelektualna lekka), do 8 (umiarkowana lub znaczna), do 4 (autyzm, sprzężenia); w klasach I–IV oddziałów dla uczniów z niepełnosprawnością umiarkowaną, znaczną, ruchową, autyzmem i sprzężeniami zatrudnia się pomoc nauczyciela.", "Te same limity liczebności. Pomoc nauczyciela w klasie IV, w klasach V–VIII według decyzji organu prowadzącego."],
  ["Ocenianie", "Ocena opisowa: bieżąca, śródroczna i roczna z zajęć edukacyjnych i zachowania (art. 44i ustawy o systemie oświaty).", "Oceny w skali 1–6 w oddziałach dla uczniów z niepełnosprawnością lekką; oceny opisowe w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną."],
  ["Egzamin ósmoklasisty", "Nie dotyczy.", "Uczniowie z niepełnosprawnością lekką przystępują z dostosowaniami (arkusz dostosowany, wydłużony czas); uczniowie z niepełnosprawnością umiarkowaną lub znaczną nie przystępują."],
  ["Wychowawstwo", "Z reguły wychowawca własnego oddziału przez cały etap. Dodatek za wychowawstwo tylko wtedy, gdy przewiduje go regulamin wynagradzania pracodawcy (art. 34a KN nie ma zastosowania).", "Wychowawca jednego oddziału na przydział dyrektora; godzina zajęć z wychowawcą w planie lekcji. Dodatek jak obok."],
  ["Charakter dnia pracy", "Stała obecność z jednym oddziałem: zajęcia, przerwy, posiłki, samoobsługa, szatnia, przekazanie uczniów rodzicom lub opiekunom dowozu; przerwa 15 minut wymaga zastępstwa (pomoc nauczyciela, drugi nauczyciel).", "Zmiana oddziałów co lekcję, dyżury na przerwach według harmonogramu, praca w pracowni przedmiotowej, udział w zespołach ds. IPET każdego oddziału, w którym uczy."],
  ["Urlop", "Urlop wypoczynkowy według Kodeksu pracy: 20 lub 26 dni (art. 154 KP), udzielany zgodnie z planem urlopów, zwykle w czasie ferii letnich i zimowych.", "Tak samo."],
];

// ---------- Tabela B: czynności ----------
const SZ_B = [520, 3300, 3900, 3900, 950, 2570];
const NAG_B = ["Lp.", "Czynność", "Nauczyciel edukacji wczesnoszkolnej (kl. I–III)", "Nauczyciel przedmiotów (kl. IV–VIII)", "Czas", "Podstawa / uwagi"];
let lp = 0;
const w = (czynnosc, ew, prz, czas, podst) => [String(++lp), czynnosc, ew, prz, czas, podst];
const czynnosci = [
  "1. Dydaktyka i realizacja podstawy programowej",
  w("Prowadzenie zajęć edukacyjnych zgodnie z planem nauczania i podstawą programową kształcenia specjalnego.",
    "● Wszystkie edukacje zintegrowane (polonistyczna, matematyczna, przyrodnicza, społeczna, plastyczna, techniczna, muzyczna, informatyczna, wychowanie fizyczne, jeśli nie przydzielono innemu nauczycielowi) w jednym oddziale.",
    "● Jeden lub kilka przedmiotów (np. język polski, matematyka, przyroda, historia, technika) w kilku oddziałach; w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną – zajęcia z odrębnej podstawy programowej.",
    "Z", "art. 14 ust. 3 Prawa oświatowego (szkoła niepubliczna realizuje wymiar zajęć nie niższy niż w ramowym planie); rozporządzenie o podstawie programowej"),
  w("Ustalanie podziału czasu zajęć i przerw.",
    "● Nauczyciel sam dzieli czas na poszczególne edukacje i ustala przerwy według potrzeb i możliwości uczniów, w granicach rozkładu czasu pracy.",
    "— Plan lekcji i dzwonki ustala dyrektor; nauczyciel realizuje plan.",
    "Z", "ramowe plany nauczania (klasy I–III); rozkład czasu pracy – art. 129 KP"),
  w("Wybór lub opracowanie programu nauczania, dostosowanie go do możliwości uczniów i wniosek do dyrektora o dopuszczenie.",
    "● Program edukacji wczesnoszkolnej dostosowany do oddziału.",
    "● Program przedmiotu dostosowany do każdego oddziału, w którym uczy.",
    "P", "art. 22a ustawy o systemie oświaty; statut szkoły"),
  w("Dostosowanie metod, form, środków i tempa pracy do zaleceń IPET oraz stosowanie metod pedagogiki specjalnej.",
    "● Metoda ośrodków pracy, Metoda Dobrego Startu, ruch rozwijający W. Sherborne, elementy integracji sensorycznej, komunikacja alternatywna i wspomagająca (AAC), nauka czytania i pisania metodami specjalnymi.",
    "● Teksty uproszczone, instrukcje obrazkowe, metody aktywizujące i praktyczne, praca na konkretach, AAC, wydłużony czas, dzielenie zadań na etapy, sprawdziany dostosowane.",
    "Z / P", "rozporządzenie o kształceniu specjalnym § 6"),
  w("Kierowanie pracą pomocy nauczyciela w czasie zajęć i opieki.",
    "● Codziennie: podział zadań, instruktaż, wspólna opieka w czasie zajęć, posiłków i czynności samoobsługowych.",
    "◐ W klasie IV zawsze; w klasach V–VIII, gdy organ prowadzący zatrudnił pomoc nauczyciela.",
    "Z", "rozporządzenie o organizacji publicznych szkół (stosowane odpowiednio); statut"),
  w("Kształtowanie samoobsługi, higieny i umiejętności praktycznych.",
    "● Codzienny trening: ubieranie, toaleta, higiena, jedzenie, porządek w miejscu pracy, poruszanie się po szkole.",
    "◐ W ramach przedmiotu lub zajęć (technika, zajęcia kulinarne, funkcjonowanie osobiste i społeczne), trening umiejętności społecznych: sklep, urząd, komunikacja miejska.",
    "Z", "podstawa programowa kształcenia specjalnego"),
  w("Orientacja zawodowa i doradztwo zawodowe.",
    "● Orientacja zawodowa włączona w zajęcia (poznawanie zawodów, zabawy tematyczne).",
    "● Treści doradztwa w przedmiotach; wychowawca klas VII–VIII współpracuje z doradcą zawodowym i pomaga rodzinie wybrać szkołę ponadpodstawową (branżowa specjalna, przysposabiająca do pracy).",
    "Z / O", "rozporządzenie o doradztwie zawodowym"),
  w("Indywidualne nauczanie ucznia w domu lub zajęcia indywidualne w szkole.",
    "◐ Na polecenie dyrektora, w ramach rozkładu czasu pracy.",
    "◐ Na polecenie dyrektora, w ramach rozkładu czasu pracy.",
    "Z", "rozporządzenie o indywidualnym nauczaniu"),

  "2. Kształcenie specjalne: IPET, WOPF, rewalidacja",
  w("Udział w zespole opracowującym IPET dla każdego ucznia oddziału.",
    "● Wychowawca zwykle koordynuje zespół dla całego oddziału i pisze IPET z wkładem specjalistów.",
    "● Członek zespołów dla każdego oddziału, w którym uczy (często kilkanaście zespołów); wkład w części przedmiotowej; jako wychowawca koordynuje zespół swojego oddziału.",
    "O", "rozporządzenie o kształceniu specjalnym § 6; IPET do 30 września lub 30 dni od otrzymania orzeczenia"),
  w("Wielospecjalistyczna ocena poziomu funkcjonowania ucznia (WOPF) co najmniej dwa razy w roku.",
    "● Pełna ocena we wszystkich sferach (poznawcza, komunikacja, motoryka, samoobsługa, emocje, zachowanie) – nauczyciel obserwuje ucznia przez cały dzień.",
    "● Wkład w zakresie funkcjonowania na lekcjach przedmiotu; wychowawca scala oceny nauczycieli i specjalistów.",
    "O", "rozporządzenie o kształceniu specjalnym § 6 ust. 9–10"),
  w("Prowadzenie zajęć rewalidacyjnych zgodnie z kwalifikacjami.",
    "◐ Np. usprawnianie technik szkolnych, terapia ręki, rozwijanie komunikacji (AAC), orientacja przestrzenna, trening umiejętności społecznych.",
    "◐ Np. usprawnianie funkcji poznawczych, rozwijanie kompetencji społecznych, alternatywne metody komunikacji, zajęcia korekcyjne ruchowe (przy kwalifikacjach).",
    "Z", "wymiar rewalidacji według planu nauczania szkoły; przydział w planie lekcji"),
  w("Realizacja zaleceń orzeczenia o potrzebie kształcenia specjalnego i IPET; ocena efektywności i modyfikacja programu.",
    "● Na bieżąco, we wszystkich zajęciach i czynnościach opiekuńczych.",
    "● Na lekcjach przedmiotu; wnioski do modyfikacji IPET w zakresie przedmiotu.",
    "Z / O", "rozporządzenie o kształceniu specjalnym"),
  w("Opinia zespołu w sprawie wydłużenia etapu edukacyjnego (o jeden rok).",
    "● Na zakończenie klasy III: opinia zespołu, wniosek do rady pedagogicznej, zgoda rodziców.",
    "● Na zakończenie klasy VIII: opinia zespołu, wniosek do rady pedagogicznej, zgoda rodziców.",
    "O", "rozporządzenie o ramowych planach nauczania § 5; decyzja rady pedagogicznej do końca lutego"),
  w("Praca z uczniem niemówiącym: wprowadzanie i używanie komunikacji alternatywnej i wspomagającej (AAC) we wszystkich sytuacjach.",
    "● Budowanie systemu komunikacji (piktogramy, gesty, książka komunikacyjna, urządzenia), nauka rodziców.",
    "● Używanie systemu komunikacji ucznia na lekcjach, materiały w symbolach, współpraca z logopedą.",
    "Z / O", "IPET, rozporządzenie o kształceniu specjalnym"),

  "3. Wychowanie, opieka i bezpieczeństwo",
  w("Pełnienie funkcji wychowawcy oddziału.",
    "● Zwykle własny oddział przez klasy I–III: sprawy wychowawcze, dokumentacja oddziału, kontakt z rodzicami, koordynowanie pomocy.",
    "◐ Wychowawca jednego oddziału klas IV–VIII na przydział dyrektora: zajęcia z wychowawcą, dokumentacja oddziału, ocena zachowania, świadectwa.",
    "Z / O", "statut szkoły; dodatek – tylko jeśli przewiduje go regulamin wynagradzania"),
  w("Opieka nad uczniami w czasie zajęć i przerw.",
    "● Ciągła: nauczyciel nie zostawia oddziału, przerwy spędza z uczniami, nadzoruje posiłki, toaletę, szatnię; własną 15-minutową przerwę odbiera po przekazaniu opieki.",
    "● Dyżury według harmonogramu: korytarze, stołówka, szatnia, boisko, przystanek dowozu.",
    "Z", "rozporządzenie o bezpieczeństwie i higienie w szkołach; art. 134 KP"),
  w("Odbiór uczniów rano i przekazanie rodzicom lub opiekunom dowozu po zajęciach.",
    "● Codziennie, według listy osób upoważnionych.",
    "◐ Według harmonogramu dyżurów lub jako wychowawca.",
    "Z", "statut szkoły, procedury"),
  w("Opieka w czasie wyjść, wycieczek, zawodów, turnusów, zielonej szkoły.",
    "● Kierownik lub opiekun; wyjścia edukacyjne w najbliższe otoczenie (park, sklep, biblioteka).",
    "● Kierownik lub opiekun wycieczek przedmiotowych, zawodów sportowych (m.in. Olimpiady Specjalne), wyjazdów klas starszych.",
    "Z", "rozporządzenie o krajoznawstwie i turystyce; czas wycieczki ponad 6 godzin rozlicza się według Kodeksu pracy (polecenie pracodawcy)"),
  w("Realizacja programu wychowawczo-profilaktycznego i treningu umiejętności społecznych.",
    "● Codzienne sytuacje: zasady, emocje, współpraca w grupie, bezpieczeństwo.",
    "● Zajęcia z wychowawcą, tematy w przedmiotach, profilaktyka uzależnień i cyberprzemocy, edukacja seksualna dostosowana, przygotowanie do dorosłości.",
    "Z", "art. 26 Prawa oświatowego"),
  w("Zapobieganie zachowaniom trudnym i reagowanie na nie; plan wsparcia pozytywnego zachowania.",
    "● Obserwacja, analiza ABC, strategie wyprzedzające, współpraca z psychologiem i rodzicami.",
    "● Stosowanie strategii z IPET na lekcjach, jednolite reagowanie, notatki z incydentów.",
    "Z / O", "procedury szkolne, IPET"),
  w("Znajomość stanu zdrowia uczniów: leki, epilepsja, dieta, alergie, zaopatrzenie ortopedyczne; współpraca z pielęgniarką szkolną.",
    "● Codziennie, przy posiłkach i czynnościach pielęgnacyjnych.",
    "● Na lekcjach i dyżurach; wychowawca zbiera informacje od rodziców.",
    "O", "procedury szkolne; ustawa o opiece zdrowotnej nad uczniami"),
  w("Zapoznanie uczniów z regulaminami i procedurami, ewakuacja, pierwsza pomoc.",
    "● W formie dostosowanej (obrazki, ćwiczenia praktyczne).",
    "● Na początku roku i przed każdą sytuacją szczególną (pracownia, wycieczka).",
    "Z", "rozporządzenie o bezpieczeństwie i higienie"),

  "4. Pomoc psychologiczno-pedagogiczna",
  w("Rozpoznawanie potrzeb rozwojowych, edukacyjnych i możliwości ucznia; obserwacja pedagogiczna.",
    "● Ciągła obserwacja we wszystkich sferach; diagnoza gotowości i umiejętności na starcie klasy I.",
    "● Obserwacja na lekcjach, analiza wyników z przedmiotu.",
    "Z / O", "statut szkoły; rozporządzenie o pomocy psychologiczno-pedagogicznej stosowane odpowiednio"),
  w("Prowadzenie zajęć specjalistycznych (korekcyjno-kompensacyjne, logopedyczne, rozwijające kompetencje emocjonalno-społeczne).",
    "◐ Przy kwalifikacjach, w planie lekcji i rozkładzie czasu pracy.",
    "◐ Przy kwalifikacjach, w planie lekcji i rozkładzie czasu pracy.",
    "Z", "statut szkoły"),
  w("Zajęcia dydaktyczno-wyrównawcze, rozwijające uzdolnienia i zainteresowania.",
    "◐ Na przydział dyrektora.",
    "◐ Na przydział dyrektora (koła przedmiotowe, sportowe, artystyczne).",
    "Z", "statut szkoły"),
  w("Współpraca ze specjalistami szkoły: psycholog, pedagog, pedagog specjalny, logopeda, rehabilitant, terapeuta SI.",
    "● Codzienna wymiana informacji, wspólne strategie, przenoszenie efektów terapii do zajęć.",
    "● Konsultacje, udział w spotkaniach zespołu, stosowanie zaleceń na lekcjach.",
    "O", "statut szkoły"),

  "5. Ocenianie, klasyfikacja i egzaminy",
  w("Opracowanie wymagań edukacyjnych dostosowanych do IPET i poinformowanie o nich uczniów i rodziców na początku roku.",
    "● Dla zajęć zintegrowanych, w formie zrozumiałej dla rodziców.",
    "● Dla każdego przedmiotu i oddziału (przedmiotowe zasady oceniania).",
    "O / P", "art. 44b ustawy o systemie oświaty"),
  w("Ocenianie bieżące.",
    "● Ocena opisowa, informacja zwrotna, symbole i wzmocnienia dostosowane do ucznia.",
    "● Stopnie 1–6 w oddziałach dla uczniów z niepełnosprawnością lekką; ocena opisowa w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną.",
    "Z / P", "art. 44i ustawy o systemie oświaty"),
  w("Klasyfikacja śródroczna i roczna, ocena zachowania.",
    "● Opisowa ocena klasyfikacyjna z zajęć i zachowania.",
    "● Oceny klasyfikacyjne z przedmiotu; wychowawca ustala ocenę zachowania po zasięgnięciu opinii nauczycieli, uczniów i ocenianego ucznia; o promocji ucznia z niepełnosprawnością umiarkowaną lub znaczną postanawia rada pedagogiczna z uwzględnieniem IPET.",
    "O", "art. 44f–44o ustawy o systemie oświaty"),
  w("Egzamin ósmoklasisty: przygotowanie uczniów, dostosowania, udział w zespołach nadzorujących.",
    "— Nie dotyczy.",
    "● Nauczyciele języka polskiego, matematyki i języka obcego przygotowują uczniów z niepełnosprawnością lekką; rada pedagogiczna wskazuje dostosowania (do 20 listopada); udział w zespołach nadzorujących na powołanie dyrektora, w czasie pracy.",
    "Z / O", "art. 44zw ustawy o systemie oświaty; rozporządzenie o egzaminie ósmoklasisty"),
  w("Egzaminy klasyfikacyjne, poprawkowe, sprawdziany wiadomości w komisjach.",
    "◐ Rzadko; na powołanie dyrektora.",
    "◐ Na powołanie dyrektora.",
    "O", "art. 44l–44n ustawy o systemie oświaty"),
  w("Świadectwa, arkusze ocen, informacja o wynikach.",
    "● Świadectwo opisowe i arkusz ocen własnego oddziału.",
    "● Nauczyciele przedmiotów wpisują oceny; wychowawca wypełnia świadectwa i arkusze ocen.",
    "O", "rozporządzenie o świadectwach; rozporządzenie o dokumentacji przebiegu nauczania"),

  "6. Współpraca z rodzicami i opiekunami",
  w("Konsultacje dla uczniów i rodziców w stałym terminie.",
    "● W wymiarze i terminie ustalonym przez dyrektora w rozkładzie czasu pracy (np. 1 godzina tygodniowo).",
    "● W wymiarze i terminie ustalonym przez dyrektora w rozkładzie czasu pracy (np. 1 godzina tygodniowo).",
    "O", "statut szkoły; godzina dostępności z art. 42 ust. 2f KN nie obowiązuje w szkole niepublicznej"),
  w("Zebrania, konsultacje, bieżąca komunikacja.",
    "● Codzienny kontakt: zeszyt korespondencji lub dziennik elektroniczny, rozmowy przy odbiorze ucznia, zebrania oddziału.",
    "● Zebrania i konsultacje wychowawcy; konsultacje przedmiotowe; dziennik elektroniczny.",
    "O", "statut szkoły; zebrania popołudniowe planuje się w rozkładzie czasu pracy"),
  w("Udział rodziców w pracach zespołu ds. IPET: zawiadamianie, omawianie WOPF i programu, przekazanie kopii dokumentów.",
    "● Jako wychowawca.",
    "◐ Jako wychowawca; jako nauczyciel przedmiotu uczestniczy w spotkaniu.",
    "O", "rozporządzenie o kształceniu specjalnym § 6 ust. 11–12"),
  w("Instruktaż dla rodziców: ćwiczenia w domu, system komunikacji AAC, jednolite zasady wobec zachowań trudnych.",
    "● Regularnie, także pokazowo w czasie zajęć otwartych.",
    "◐ W zakresie przedmiotu i strategii z IPET.",
    "O", "IPET"),
  w("Zgody i oświadczenia rodziców: wycieczki, wizerunek, badania, odbiór ucznia, leki.",
    "● Jako wychowawca.",
    "◐ Jako wychowawca lub kierownik wycieczki.",
    "O", "statut, procedury, RODO"),

  "7. Praca zespołowa, rada pedagogiczna, instytucje",
  w("Udział w zebraniach rady pedagogicznej i realizacja jej uchwał.",
    "● Zebrania klasyfikacyjne, plenarne, szkoleniowe – w czasie pracy lub jako czas pracy poza rozkładem na polecenie pracodawcy.",
    "● Zebrania klasyfikacyjne, plenarne, szkoleniowe – jak obok.",
    "O", "statut szkoły (rada pedagogiczna w szkole niepublicznej, jeśli statut ją przewiduje)"),
  w("Praca w zespołach nauczycieli.",
    "● Zespół edukacji wczesnoszkolnej, zespół wychowawczy, zespoły ds. IPET, zespół ds. ewaluacji lub programu wychowawczo-profilaktycznego.",
    "● Zespół przedmiotowy, zespół wychowawców klas IV–VIII, zespoły ds. IPET, zespół ds. egzaminu ósmoklasisty.",
    "O", "statut szkoły"),
  w("Współpraca z instytucjami: poradnia psychologiczno-pedagogiczna, ośrodek pomocy społecznej, powiatowe centrum pomocy rodzinie, sąd rodzinny i kurator, policja, ochrona zdrowia, ośrodki rehabilitacji.",
    "● Przy przyjęciu ucznia: współpraca z przedszkolem, wczesnym wspomaganiem rozwoju, poradnią.",
    "● Przy przejściu po klasie VIII: współpraca ze szkołami ponadpodstawowymi specjalnymi, warsztatami terapii zajęciowej, doradcą zawodowym.",
    "O", "statut; ustawa o przeciwdziałaniu przemocy domowej (Niebieska Karta)"),
  w("Mentor nauczyciela początkującego, opiekun praktyk studenckich, zajęcia otwarte i lekcje koleżeńskie.",
    "◐ Na przydział dyrektora.",
    "◐ Na przydział dyrektora.",
    "O", "art. 9ca KN (awans zawodowy stosowany w szkole niepublicznej – art. 91b KN); dodatek, jeśli regulamin tak stanowi"),

  "8. Dokumentacja",
  w("Dziennik lekcyjny (elektroniczny lub papierowy).",
    "● Jeden dziennik oddziału: tematy wszystkich edukacji, frekwencja, ocena opisowa, kontakty z rodzicami.",
    "● Wpisy tematów, frekwencji i ocen w dziennikach każdego oddziału, w którym uczy; wychowawca prowadzi część oddziałową.",
    "O", "rozporządzenie o dokumentacji przebiegu nauczania (szkoły niepubliczne – art. 172 ust. 2 pkt 4 Prawa oświatowego)"),
  w("Dziennik zajęć rewalidacyjnych i specjalistycznych.",
    "◐ Dla prowadzonych zajęć.",
    "◐ Dla prowadzonych zajęć.",
    "O", "rozporządzenie o dokumentacji przebiegu nauczania § 11"),
  w("Dokumentacja kształcenia specjalnego: IPET, WOPF, arkusze obserwacji, teczka ucznia.",
    "● Pełna dokumentacja uczniów swojego oddziału.",
    "● Wkład przedmiotowy; jako wychowawca prowadzi teczki uczniów oddziału.",
    "O", "rozporządzenie o kształceniu specjalnym"),
  w("Plany pracy: rozkład materiału lub plan wynikowy, plan pracy wychowawcy, plan zajęć rewalidacyjnych.",
    "● Zintegrowany plan pracy oddziału na rok, plan wychowawcy.",
    "● Plan wynikowy każdego przedmiotu dla każdego oddziału, plan pracy wychowawcy (jeśli jest wychowawcą).",
    "P", "statut szkoły"),
  w("Arkusze ocen, świadectwa, księga ewidencji uczniów (na zlecenie dyrektora), zaświadczenia.",
    "● Jako wychowawca.",
    "◐ Jako wychowawca.",
    "O", "rozporządzenie o dokumentacji przebiegu nauczania"),
  w("Sprawozdania półroczne i roczne, ewaluacja wewnętrzna, notatki służbowe, dokumentacja wypadków.",
    "● Sprawozdanie z pracy oddziału i realizacji IPET.",
    "● Sprawozdanie z realizacji przedmiotu i zadań przydzielonych; wychowawca dodatkowo z pracy wychowawczej.",
    "O", "statut szkoły; rozporządzenie o bezpieczeństwie i higienie (wypadki)"),
  w("Potwierdzanie obecności i czasu pracy zgodnie z zasadami pracodawcy (lista obecności, system elektroniczny).",
    "● Codziennie.",
    "● Codziennie.",
    "O", "art. 149 KP; regulamin pracy"),

  "9. Organizacja życia szkoły",
  w("Uroczystości, apele, imprezy szkolne.",
    "● Pasowanie na ucznia, Dzień Babci i Dziadka, jasełka, Dzień Rodziny, festyny; przygotowanie występów dostosowanych do możliwości uczniów.",
    "● Akademie okolicznościowe, Dzień Edukacji Narodowej, dyskoteki, pożegnanie klasy VIII, Dzień Godności Osób z Niepełnosprawnością Intelektualną.",
    "Z / O", "statut, plan pracy szkoły"),
  w("Konkursy, zawody, projekty, wystawy.",
    "● Konkursy plastyczne i recytatorskie, wystawy prac, projekty klasowe.",
    "● Konkursy przedmiotowe i artystyczne, zawody sportowe (Olimpiady Specjalne, paraolimpiady szkolne), projekty edukacyjne i społeczne.",
    "Z / O", "statut, plan pracy szkoły"),
  w("Opieka nad salą, pracownią, pomocami i sprzętem; inwentaryzacja; estetyka i bezpieczeństwo pomieszczeń.",
    "● Stała sala oddziału: kąciki tematyczne, kącik relaksu, pomoce manipulacyjne, dekoracje sezonowe.",
    "● Pracownia przedmiotowa: regulamin, pomoce dydaktyczne, sprzęt komputerowy, narzędzia.",
    "O", "statut szkoły; odpowiedzialność za mienie – art. 124 KP tylko przy powierzeniu na piśmie"),
  w("Opieka nad samorządem uczniowskim, wolontariatem, organizacjami uczniowskimi, kroniką, gazetką, stroną internetową.",
    "◐ Mały samorząd klas I–III.",
    "◐ Na przydział dyrektora.",
    "O", "statut szkoły"),
  w("Promocja szkoły i rekrutacja: dni otwarte, spotkania z rodzicami kandydatów, komisja rekrutacyjna.",
    "● Prezentacja pracy klas I–III rodzicom kandydatów, współpraca z poradniami kierującymi uczniów.",
    "◐ Na przydział dyrektora.",
    "O", "statut szkoły"),

  "10. Przygotowanie do zajęć, samokształcenie, doskonalenie",
  w("Przygotowanie zajęć i pomocy dydaktycznych.",
    "● Duża liczba pomocy manipulacyjnych, sensorycznych, kart pracy i materiałów w symbolach AAC; przygotowanie kącików i sali. Czas na to planuje się w 6-godzinnym dniu (np. 1 godzina po zajęciach z oddziałem).",
    "● Uproszczone teksty, karty pracy, prezentacje, doświadczenia, materiały w symbolach; wersje zadań na różnych poziomach dla jednego oddziału. Czas na to planuje się w 6-godzinnym dniu (np. godzina bez lekcji).",
    "P", "praca w rozumieniu art. 128 KP – w rozkładzie czasu pracy"),
  w("Sprawdzanie prac uczniów, analiza postępów, informacja zwrotna.",
    "● Głównie ocena opisowa postępów, portfolio ucznia.",
    "● Sprawdziany dostosowane, prace domowe, analiza wyników próbnych egzaminów.",
    "P", "jak wyżej"),
  w("Samokształcenie: pedagogika specjalna, metody terapii, prawo oświatowe, nowe technologie.",
    "● Metody wczesnej edukacji specjalnej, AAC, integracja sensoryczna, terapia ręki.",
    "● Dydaktyka przedmiotu dla uczniów z niepełnosprawnością intelektualną, dostosowania egzaminacyjne, technologie wspomagające.",
    "P", "art. 6 pkt 3 KN (stosowany przez art. 91b KN); art. 17 i 94 pkt 6 KP – ułatwianie podnoszenia kwalifikacji"),
  w("Doskonalenie zawodowe zgodnie z potrzebami szkoły; awans zawodowy.",
    "● Szkolenia rady pedagogicznej, kursy, konferencje, sieci współpracy; realizacja planu rozwoju zawodowego. Szkolenie na polecenie pracodawcy jest czasem pracy (art. 94¹³ KP).",
    "● Szkolenia rady pedagogicznej, kursy, konferencje, sieci współpracy; realizacja planu rozwoju zawodowego. Szkolenie na polecenie pracodawcy jest czasem pracy (art. 94¹³ KP).",
    "P", "art. 6 pkt 3a, art. 9a–9h KN (przez art. 91b KN); art. 103¹–103⁶ KP"),

  "11. Czynności wynagradzane odrębnie (poza wynagrodzeniem zasadniczym)",
  w("Praca ponad 6 godzin dziennie na polecenie pracodawcy (zebranie popołudniowe, wycieczka, uroczystość, zastępstwo).",
    "◐ Do 8 godzin dziennie: wynagrodzenie za dodatkowe godziny (z dodatkiem, jeśli umowa ustala próg według art. 151 § 5 KP); powyżej 8 godzin lub przeciętnie 40 tygodniowo: godziny nadliczbowe z dodatkiem 50% lub 100% albo czas wolny.",
    "◐ Tak samo.",
    "odrębnie", "art. 151–151³ KP; regulamin wynagradzania"),
  w("Praca w sobotę, niedzielę lub święto (wycieczka, zawody, festyn, dzień otwarty).",
    "◐ Inny dzień wolny w tym samym okresie rozliczeniowym albo wynagrodzenie z dodatkiem 100%.",
    "◐ Tak samo.",
    "odrębnie", "art. 151¹¹ KP; art. 151¹ § 1 pkt 1 KP"),
  w("Dodatek za wychowawstwo, za warunki pracy, za funkcje (mentor, opiekun praktyk, kierownik wycieczki).",
    "◐ Tylko jeśli przewiduje je regulamin wynagradzania lub umowa o pracę; przepisy Karty Nauczyciela o dodatkach (art. 30, 34, 34a) nie mają zastosowania.",
    "◐ Tak samo.",
    "odrębnie", "art. 77² KP; regulamin wynagradzania pracodawcy"),
  w("Sprawdzanie prac egzaminu ósmoklasisty jako egzaminator OKE.",
    "— Nie dotyczy.",
    "◐ Umowa cywilnoprawna z okręgową komisją egzaminacyjną.",
    "odrębnie", "poza stosunkiem pracy"),
  w("Zajęcia finansowane z projektów zewnętrznych, zajęcia komercyjne, terapia dla osób spoza szkoły.",
    "◐ Odrębna umowa (o pracę lub cywilnoprawna) albo rozszerzenie wymiaru w umowie.",
    "◐ Tak samo.",
    "odrębnie", "umowa, regulamin projektu"),
];

// ---------- Tabela C: przykładowy rozkład 6-godzinnego dnia ----------
const SZ_C = [1500, 6820, 6820];
const dzien = [
  ["7:45–8:00", "Odbiór uczniów od rodziców i opiekunów dowozu, szatnia, sprawdzenie zeszytów korespondencji, przekazanie informacji pomocy nauczyciela.", "Przygotowanie pracowni, dyżur przy wejściu lub w szatni według harmonogramu."],
  ["8:00–10:30", "Zajęcia zintegrowane z oddziałem (edukacja polonistyczna, matematyczna, przyrodnicza), przerwy ustalane przez nauczyciela, drugie śniadanie, czynności samoobsługowe.", "Lekcje 1–3 w różnych oddziałach (3 × 45 minut) z przerwami; dyżur na jednej przerwie."],
  ["10:30–10:45", "Przerwa nauczyciela (15 minut, art. 134 KP) po przekazaniu opieki pomocy nauczyciela lub drugiemu nauczycielowi.", "Przerwa nauczyciela (15 minut, art. 134 KP)."],
  ["10:45–12:30", "Zajęcia zintegrowane (edukacja plastyczna, techniczna, muzyczna, ruch), zajęcia rewalidacyjne lub trening umiejętności społecznych, obiad z oddziałem.", "Lekcje 4–5 (2 × 45 minut), dyżur w stołówce lub na korytarzu, zajęcia rewalidacyjne albo zajęcia z wychowawcą."],
  ["12:30–12:45", "Przekazanie uczniów rodzicom lub opiekunom dowozu, informacje dla rodziców, wpisy w zeszytach korespondencji.", "Przekazanie uczniów po ostatniej lekcji (jeśli wychowawca) lub dyżur przy dowozie."],
  ["12:45–13:45", "Dokumentacja (dziennik, IPET, WOPF, ocena opisowa), przygotowanie pomocy na następny dzień, kontakt telefoniczny z rodzicami, spotkanie zespołu lub konsultacje ze specjalistami. Raz w tygodniu: konsultacje dla rodziców.", "Dokumentacja (dzienniki oddziałów, plany wynikowe), sprawdzanie prac, przygotowanie materiałów, udział w zespole ds. IPET, konsultacje dla rodziców raz w tygodniu."],
  ["Poza rozkładem", "Zebranie z rodzicami, rada pedagogiczna, uroczystość popołudniowa: na polecenie pracodawcy, ewidencjonowane i rozliczane według tabeli B pkt 11 albo planowane w rozkładzie w zamian za krótszy inny dzień.", "Tak samo."],
];

// ---------- Tabela D: kalendarz ----------
const SZ_D = [1600, 6770, 6770];
const kalendarz = [
  ["Sierpień", "Powrót z urlopu według planu urlopów; rada plenarna, przydział czynności, przygotowanie sali, plan pracy oddziału, analiza orzeczeń nowych uczniów, spotkanie z rodzicami klasy I.", "Rada plenarna, przydział czynności i wychowawstw, egzaminy poprawkowe, plany wynikowe, przygotowanie pracowni."],
  ["Wrzesień", "Diagnoza wstępna uczniów, zebranie z rodzicami, wymagania edukacyjne, IPET do 30 września, harmonogram konsultacji dla rodziców, zgody rodziców, adaptacja klasy I.", "Zebrania wychowawców, wymagania przedmiotowe, IPET do 30 września (udział w zespołach), harmonogram dyżurów i konsultacji, deklaracje językowe do egzaminu ósmoklasisty."],
  ["Październik", "Pasowanie na ucznia, Dzień Edukacji Narodowej, zajęcia otwarte dla rodziców.", "Dzień Edukacji Narodowej, konkursy przedmiotowe, wnioski rodziców o dostosowania egzaminu ósmoklasisty (zaświadczenia do 15 października)."],
  ["Listopad", "Andrzejki, akcje charytatywne, obserwacje do WOPF.", "Rada pedagogiczna wskazuje dostosowania egzaminu ósmoklasisty (do 20 listopada), informacja dla rodziców uczniów klasy VIII."],
  ["Grudzień", "Jasełka, mikołajki, spotkanie wigilijne z rodzicami, WOPF śródroczna w przygotowaniu.", "Próbny egzamin ósmoklasisty, jasełka, WOPF śródroczna w przygotowaniu."],
  ["Styczeń", "WOPF i ocena efektywności IPET, klasyfikacja śródroczna (ocena opisowa), zebrania z rodzicami, Dzień Babci i Dziadka.", "WOPF i ocena efektywności IPET, klasyfikacja śródroczna, rada klasyfikacyjna, zebrania z rodzicami."],
  ["Luty", "Opinia zespołu i decyzja rady pedagogicznej w sprawie wydłużenia etapu (klasa III) do końca lutego; ferie zimowe (urlop według planu); bal karnawałowy.", "Opinia zespołu i decyzja rady pedagogicznej w sprawie wydłużenia etapu (klasa VIII) do końca lutego; ferie zimowe (urlop według planu)."],
  ["Marzec", "Dni otwarte, rekrutacja do klasy I, spotkania z rodzicami kandydatów, Dzień Wiosny.", "Dni otwarte, doradztwo zawodowe dla klas VII–VIII, spotkania ze szkołami ponadpodstawowymi specjalnymi."],
  ["Kwiecień", "Wielkanoc w klasie, wyjścia edukacyjne, aktualizacja IPET.", "Próbne egzaminy, przygotowanie sal egzaminacyjnych, aktualizacja IPET."],
  ["Maj", "Dzień Rodziny, Dzień Godności Osób z Niepełnosprawnością Intelektualną (5 maja), wycieczki, Olimpiady Specjalne.", "Egzamin ósmoklasisty (zespoły nadzorujące), Dzień Godności, wycieczki, zawody sportowe."],
  ["Czerwiec", "WOPF końcowa, klasyfikacja roczna (ocena opisowa), świadectwa i arkusze ocen, sprawozdanie, zakończenie roku, przekazanie informacji o uczniach klasy III wychowawcy klasy IV.", "WOPF końcowa, klasyfikacja roczna, rada klasyfikacyjna, świadectwa i arkusze ocen, sprawozdania, pożegnanie klasy VIII, wnioski do szkół ponadpodstawowych."],
  ["Lipiec", "Urlop wypoczynkowy według planu urlopów (Kodeks pracy, 20 lub 26 dni w roku); poza urlopem – praca w rozkładzie czasu pracy (prace organizacyjne, dokumentacja, rekrutacja).", "Urlop wypoczynkowy według planu urlopów; poza urlopem – praca w rozkładzie czasu pracy (egzaminy poprawkowe, prace organizacyjne)."],
];

// ---------- dokument ----------
const naglowek = new Header({ children: [new Paragraph({
  tabStops: [{ type: TabStopType.RIGHT, position: SZER }], border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: FIOLET, space: 4 } }, spacing: { after: 160 },
  children: [new ImageRun({ type: "png", data: logo, transformation: { width: 24, height: 24 } }), run("   " + PLACOWKA, { size: 15, color: SZARY }), run("\tCzynności nauczycieli szkoły specjalnej – Kodeks pracy, 6 godzin dziennie – " + ROK, { size: 15, color: FIOLET })],
})] });
const stopka = new Footer({ children: [new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 80 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: POMARANCZ, space: 4 } },
  children: [run("Strona ", { size: 15, color: SZARY }), new TextRun({ children: [PageNumber.CURRENT], font: F, size: 15, color: SZARY }), run("   •   ● robi   ◐ zależnie od przydziału   — nie dotyczy   •   Z zajęcia z uczniami · O organizacja i dokumentacja · P przygotowanie i doskonalenie", { size: 15, color: SZARY })],
})] });

const tresc = [
  ...naglowekDok,
  h1("A. Ramy zatrudnienia i różnice między stanowiskami"),
  tabela(["Cecha", "Nauczyciel edukacji wczesnoszkolnej (kl. I–III)", "Nauczyciel przedmiotów (kl. IV–VIII)"], profil, SZ_A, { zebra: true, boldCol: 0 }),
  odstep(120),
  uwaga("Dlaczego Kodeks pracy, a nie Karta Nauczyciela.", "W szkole niepublicznej czas pracy, wynagrodzenie i urlop nauczycieli reguluje Kodeks pracy, umowa o pracę, regulamin pracy i regulamin wynagradzania. Z Karty Nauczyciela stosuje się wyłącznie przepisy wymienione w art. 91b ust. 2: obowiązki nauczyciela (art. 6), awans zawodowy (art. 9–9i), ochrona i odpowiedzialność dyscyplinarna (art. 63, 75–85z) oraz kilka uprawnień socjalnych. Nie obowiązują: pensum i 40-godzinny tydzień z art. 42, godziny ponadwymiarowe z art. 35, dodatki z art. 30–34a, godzina dostępności z art. 42 ust. 2f ani urlop w wymiarze ferii z art. 64. Przepisy oświatowe o kształceniu specjalnym, ocenianiu, egzaminach, dokumentacji i bezpieczeństwie obowiązują tak jak w szkole publicznej."),
  h1("B. Wykaz czynności z podziałem na stanowiska"),
  tabela(NAG_B, czynnosci, SZ_B, { zebra: true, center: [0, 4] }),
  odstep(120),
  uwaga("Zasada łączna.", "Wszystkie czynności oznaczone Z, O i P są pracą w rozumieniu art. 128 Kodeksu pracy: wykonuje się je w 6-godzinnym dniu pracy według rozkładu ustalonego przez dyrektora i wpisuje do ewidencji czasu pracy. Praca poza rozkładem wymaga polecenia pracodawcy i jest rozliczana według punktu 11. Zajęcia z uczniami (Z) planuje się tak, aby w każdym dniu pozostał czas na czynności O i P; orientacyjnie 4–4,5 godziny zajęć i opieki oraz 1,5–2 godziny na dokumentację, przygotowanie i współpracę. Wykaz należy dopasować do statutu szkoły, regulaminu pracy i regulaminu wynagradzania."),
  h1("C. Przykładowy rozkład 6-godzinnego dnia pracy", true),
  p("Rozkład ustala pracodawca na co najmniej miesiąc i przekazuje nauczycielowi co najmniej tydzień przed rozpoczęciem pracy (art. 129 § 3 KP). Poniższy układ pokazuje, jak zmieścić wszystkie grupy czynności w 6 godzinach; godziny są przykładowe."),
  tabela(["Godziny", "Nauczyciel edukacji wczesnoszkolnej (kl. I–III)", "Nauczyciel przedmiotów (kl. IV–VIII)"], dzien, SZ_C, { zebra: true, boldCol: 0 }),
  h1("D. Kalendarz czynności w roku szkolnym"),
  tabela(["Miesiąc", "Nauczyciel edukacji wczesnoszkolnej (kl. I–III)", "Nauczyciel przedmiotów (kl. IV–VIII)"], kalendarz, SZ_D, { zebra: true, boldCol: 0 }),
  odstep(120),
  uwaga("Podstawa prawna.", "Kodeks pracy (art. 17, 77², 94, 94¹³, 103¹–103⁶, 124, 128–129, 134, 149, 151–151¹¹, 152–154); ustawa – Karta Nauczyciela w zakresie art. 91b ust. 2 (art. 6, 9–9i, 63, 75–85z); ustawa o systemie oświaty (art. 22a, 44b–44o, 44zw); Prawo oświatowe (art. 14, 26, 127, 172); rozporządzenia MEN: o kształceniu specjalnym (9.08.2017), o ramowych planach nauczania (3.04.2019), o dokumentacji przebiegu nauczania (25.08.2017), o kwalifikacjach nauczycieli (1.08.2017), o egzaminie ósmoklasisty, o świadectwach, o bezpieczeństwie i higienie (31.12.2002), o krajoznawstwie i turystyce (25.05.2018), o doradztwie zawodowym; statut szkoły, regulamin pracy, regulamin wynagradzania, umowy o pracę."),
];

const doc = new Document({
  creator: PLACOWKA, title: "Czynności nauczycieli szkoły specjalnej " + ROK,
  styles: {
    default: { document: { run: { font: F, size: 19 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { font: F, size: 26, bold: true, color: FIOLET }, paragraph: { spacing: { before: 280, after: 120 }, outlineLevel: 0 } },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE }, margin: { top: 900, bottom: 850, left: 850, right: 850 } } },
    headers: { default: naglowek }, footers: { default: stopka }, children: tresc,
  }],
});


// ---------- wersja Markdown (ta sama treść) ----------
function md() {
  const esc = (t) => String(t).replace(/\|/g, "\\|").replace(/\n/g, " ");
  const tab = (nag, rows) => [`| ${nag.join(" | ")} |`, `|${nag.map(() => "---").join("|")}|`,
    ...rows.map((r) => typeof r === "string" ? `| **${esc(r)}** |${" |".repeat(nag.length - 1)}` : `| ${r.map(esc).join(" | ")} |`)].join("\n");
  return [
    `# Czynności nauczycieli szkoły specjalnej`,
    ``,
    `**${PLACOWKA} · rok szkolny ${ROK}**`,
    `Tabela porównawcza: nauczyciel edukacji wczesnoszkolnej (klasy I–III) i nauczyciel przedmiotów (klasy IV–VIII). Nauczyciele zatrudnieni na podstawie Kodeksu pracy, 6 godzin dziennie (30 godzin tygodniowo).`,
    ``,
    `Wersja do druku: \`czynnosci-nauczycieli-szkoly-specjalnej.docx\` (A4 poziomo; generator: \`generuj_tabela_szkola_specjalna.js\`).`,
    ``,
    `Tabela zbiera wszystkie zajęcia i czynności, które nauczyciele szkoły podstawowej specjalnej wykonują w ramach umówionego czasu pracy i wynagrodzenia, oraz te, które są płatne odrębnie. Nie stosuje się pensum, godzin ponadwymiarowych ani podziału czasu pracy z art. 42 Karty Nauczyciela: każda czynność – zajęcia z uczniami, przygotowanie, dokumentacja, zebrania, kontakt z rodzicami – jest pracą w rozumieniu Kodeksu pracy, mieści się w 6-godzinnym dniu i podlega ewidencji czasu pracy. Dotyczy oddziałów dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim (podstawa programowa ogólna, dostosowana) oraz umiarkowanym lub znacznym (odrębna podstawa programowa), a także oddziałów dla uczniów z autyzmem i z niepełnosprawnościami sprzężonymi.`,
    ``,
    `**Legenda:** ● robi · ◐ zależnie od przydziału, typu oddziału lub kwalifikacji · — nie dotyczy. **Czas:** Z zajęcia z uczniami · O organizacja, dokumentacja, współpraca · P przygotowanie i doskonalenie (wszystkie w 6-godzinnym dniu pracy); „odrębnie” = poza wynagrodzeniem zasadniczym.`,
    ``,
    `## A. Ramy zatrudnienia i różnice między stanowiskami`,
    ``,
    tab(["Cecha", "Nauczyciel edukacji wczesnoszkolnej (kl. I–III)", "Nauczyciel przedmiotów (kl. IV–VIII)"], profil.map((r) => [`**${r[0]}**`, r[1], r[2]])),
    ``,
    `> **Dlaczego Kodeks pracy, a nie Karta Nauczyciela.** W szkole niepublicznej czas pracy, wynagrodzenie i urlop nauczycieli reguluje Kodeks pracy, umowa o pracę, regulamin pracy i regulamin wynagradzania. Z Karty Nauczyciela stosuje się wyłącznie przepisy wymienione w art. 91b ust. 2: obowiązki nauczyciela (art. 6), awans zawodowy (art. 9–9i), ochrona i odpowiedzialność dyscyplinarna (art. 63, 75–85z) oraz kilka uprawnień socjalnych. Nie obowiązują: pensum i 40-godzinny tydzień z art. 42, godziny ponadwymiarowe z art. 35, dodatki z art. 30–34a, godzina dostępności z art. 42 ust. 2f ani urlop w wymiarze ferii z art. 64. Przepisy oświatowe o kształceniu specjalnym, ocenianiu, egzaminach, dokumentacji i bezpieczeństwie obowiązują tak jak w szkole publicznej.`,
    ``,
    `## B. Wykaz czynności z podziałem na stanowiska`,
    ``,
    tab(NAG_B, czynnosci),
    ``,
    `> **Zasada łączna.** Wszystkie czynności oznaczone Z, O i P są pracą w rozumieniu art. 128 Kodeksu pracy: wykonuje się je w 6-godzinnym dniu pracy według rozkładu ustalonego przez dyrektora i wpisuje do ewidencji czasu pracy. Praca poza rozkładem wymaga polecenia pracodawcy i jest rozliczana według punktu 11. Zajęcia z uczniami (Z) planuje się tak, aby w każdym dniu pozostał czas na czynności O i P; orientacyjnie 4–4,5 godziny zajęć i opieki oraz 1,5–2 godziny na dokumentację, przygotowanie i współpracę. Wykaz należy dopasować do statutu szkoły, regulaminu pracy i regulaminu wynagradzania.`,
    ``,
    `## C. Przykładowy rozkład 6-godzinnego dnia pracy`,
    ``,
    `Rozkład ustala pracodawca na co najmniej miesiąc i przekazuje nauczycielowi co najmniej tydzień przed rozpoczęciem pracy (art. 129 § 3 KP). Godziny są przykładowe.`,
    ``,
    tab(["Godziny", "Nauczyciel edukacji wczesnoszkolnej (kl. I–III)", "Nauczyciel przedmiotów (kl. IV–VIII)"], dzien.map((r) => [`**${r[0]}**`, r[1], r[2]])),
    ``,
    `## D. Kalendarz czynności w roku szkolnym`,
    ``,
    tab(["Miesiąc", "Nauczyciel edukacji wczesnoszkolnej (kl. I–III)", "Nauczyciel przedmiotów (kl. IV–VIII)"], kalendarz.map((r) => [`**${r[0]}**`, r[1], r[2]])),
    ``,
    `> **Podstawa prawna.** Kodeks pracy (art. 17, 77², 94, 94¹³, 103¹–103⁶, 124, 128–129, 134, 149, 151–151¹¹, 152–154); ustawa – Karta Nauczyciela w zakresie art. 91b ust. 2 (art. 6, 9–9i, 63, 75–85z); ustawa o systemie oświaty (art. 22a, 44b–44o, 44zw); Prawo oświatowe (art. 14, 26, 127, 172); rozporządzenia MEN: o kształceniu specjalnym (9.08.2017), o ramowych planach nauczania (3.04.2019), o dokumentacji przebiegu nauczania (25.08.2017), o kwalifikacjach nauczycieli (1.08.2017), o egzaminie ósmoklasisty, o świadectwach, o bezpieczeństwie i higienie (31.12.2002), o krajoznawstwie i turystyce (25.05.2018), o doradztwie zawodowym; statut szkoły, regulamin pracy, regulamin wynagradzania, umowy o pracę.`,
    ``,
  ].join("\n");
}
if (OUT_MD) { fs.writeFileSync(OUT_MD, md()); console.log("zapisano", OUT_MD); }

Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log("zapisano", OUT, buf.length, "B"); });
