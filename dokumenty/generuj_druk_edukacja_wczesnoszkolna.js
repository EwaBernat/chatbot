// Generator druku "Zakres czynności i obowiązków nauczyciela edukacji wczesnoszkolnej
// w szkole specjalnej" – osobny egzemplarz dla każdego nauczyciela (Kodeks pracy, 30 godzin tygodniowo).
// Uruchomienie (z katalogu głównego repozytorium):
//   npm install docx sharp
//   node -e "require('sharp')('logo-lawenda.webp').png().toFile('logo.png')"
//   node dokumenty/generuj_druk_edukacja_wczesnoszkolna.js logo.png dokumenty/druk-zakres-czynnosci-edukacja-wczesnoszkolna.docx "Karolina P." "Karolina B."
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber, TabStopType, VerticalAlign,
} = require("docx");

const [,, LOGO = "logo.png", OUT = "druk.docx", ...NAUCZYCIELE] = process.argv;
if (NAUCZYCIELE.length === 0) NAUCZYCIELE.push("Karolina P.", "Karolina B.");

const FIOLET = "2D1B69";
const POMARANCZ = "E8450A";
const SZARY = "555555";
const F = "Arial";
const ROK = "2026/2027";
const PLACOWKA = "Pomorskie Centrum Terapii Pedagogicznej w Koszalinie";
const SZKOLA = "Szkoła Podstawowa Specjalna";
const SZER = 10160;

// ---------- pomocnicze ----------
const run = (text, o = {}) => new TextRun({ text, font: F, size: o.size || 18, bold: o.bold, italics: o.italics, color: o.color });
const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: "BFB8D6" };
const borders = { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder };
const BEZ = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const bezRamek = { top: BEZ, bottom: BEZ, left: BEZ, right: BEZ };

function cell(content, width, o = {}) {
  const paras = (Array.isArray(content) ? content : [content]).map((c) => c instanceof Paragraph ? c : new Paragraph({
    alignment: o.align || AlignmentType.LEFT, spacing: { after: 30, line: 250 }, keepNext: o.keepNext,
    children: [run(String(c), { size: o.size || 17, bold: o.bold, color: o.color })],
  }));
  return new TableCell({
    width: { size: width, type: WidthType.DXA }, borders: o.borders || borders, verticalAlign: o.valign || VerticalAlign.TOP,
    margins: { top: 50, bottom: 50, left: 80, right: 80 }, columnSpan: o.span,
    shading: o.fill ? { type: ShadingType.CLEAR, fill: o.fill, color: "auto" } : undefined, children: paras,
  });
}
function tabela(naglowki, wiersze, szer, o = {}) {
  const suma = szer.reduce((a, b) => a + b, 0);
  const rows = [];
  if (naglowki) rows.push(new TableRow({ tableHeader: true, children: naglowki.map((n, i) => cell(n, szer[i], { bold: true, color: "FFFFFF", fill: FIOLET, valign: VerticalAlign.CENTER })) }));
  let zi = 0;
  for (const w of wiersze) {
    if (typeof w === "string") { zi = 0; rows.push(new TableRow({ cantSplit: true, children: [cell(w, suma, { span: szer.length, bold: true, color: FIOLET, fill: "EDE8F7", size: 18, keepNext: true })] })); continue; }
    const fill = o.zebra && zi++ % 2 === 1 ? "F7F5FB" : undefined;
    rows.push(new TableRow({ cantSplit: true, children: w.map((c, i) => cell(c, szer[i], { fill, bold: o.boldCol === i, align: o.center && o.center.includes(i) ? AlignmentType.CENTER : undefined, size: o.size })) }));
  }
  return new Table({ width: { size: suma, type: WidthType.DXA }, columnWidths: szer, rows });
}
const odstep = (n = 80) => new Paragraph({ spacing: { after: n }, children: [] });
const tytulSekcji = (t) => new Paragraph({ spacing: { before: 200, after: 80 }, keepNext: true, children: [run(t, { size: 20, bold: true, color: FIOLET })] });

// ---------- treść wspólna: obowiązki ----------
const SZ = [480, 6480, 3200];
let lp = 0;
const w = (czynnosc, podstawa) => [String(++lp), czynnosc, podstawa];
function obowiazki() {
  lp = 0;
  return [
    "I. Obowiązki ogólne nauczyciela i pracownika",
    w("Rzetelna realizacja zadań związanych z powierzonym stanowiskiem oraz podstawowymi funkcjami szkoły: dydaktyczną, wychowawczą i opiekuńczą, w tym zadań związanych z zapewnieniem bezpieczeństwa uczniom w czasie zajęć organizowanych przez szkołę.", "art. 6 pkt 1 Karty Nauczyciela (stosowany na podstawie art. 91b ust. 2 KN)"),
    w("Wspieranie każdego ucznia w jego rozwoju; kształcenie i wychowywanie w poszanowaniu Konstytucji RP, w atmosferze wolności sumienia i szacunku dla każdego człowieka; dbałość o kształtowanie postaw moralnych i obywatelskich.", "art. 6 pkt 2, 4 i 5 Karty Nauczyciela"),
    w("Sumienne i staranne wykonywanie pracy, stosowanie się do poleceń przełożonych dotyczących pracy, przestrzeganie regulaminu pracy, ustalonego porządku i zasad współżycia społecznego, dbałość o dobro zakładu pracy i ochrona jego mienia.", "art. 100 § 1 i § 2 pkt 2, 4 i 6 Kodeksu pracy"),
    w("Przestrzeganie ustalonego czasu pracy: 30 godzin tygodniowo według rozkładu czasu pracy; potwierdzanie obecności; praca poza rozkładem wyłącznie na polecenie pracodawcy.", "art. 100 § 2 pkt 1, art. 129 i art. 149 Kodeksu pracy; regulamin pracy"),
    w("Przestrzeganie przepisów oraz zasad bezpieczeństwa i higieny pracy i przepisów przeciwpożarowych; udział w szkoleniach BHP; poddawanie się wstępnym, okresowym i kontrolnym badaniom lekarskim.", "art. 100 § 2 pkt 3, art. 211 i art. 229 Kodeksu pracy"),
    w("Zachowanie w tajemnicy informacji o uczniach, ich rodzinach i stanie zdrowia; przetwarzanie danych osobowych wyłącznie w zakresie upoważnienia i zgodnie z RODO oraz polityką ochrony danych szkoły.", "art. 100 § 2 pkt 4 i 5 Kodeksu pracy; RODO (rozporządzenie UE 2016/679); polityka ochrony danych szkoły"),

    "II. Dydaktyka i realizacja podstawy programowej",
    w("Prowadzenie zintegrowanych zajęć edukacyjnych w klasach I–III (edukacja polonistyczna, matematyczna, przyrodnicza, społeczna, plastyczna, techniczna, muzyczna, informatyczna, wychowanie fizyczne – o ile nie przydzielono innemu nauczycielowi) zgodnie z planem nauczania i podstawą programową; w oddziałach dla uczniów z niepełnosprawnością intelektualną w stopniu umiarkowanym lub znacznym – zajęć z odrębnej podstawy programowej.", "art. 14 ust. 3 i art. 127 Prawa oświatowego; rozporządzenie MEN w sprawie podstawy programowej (14.02.2017 r.)"),
    w("Samodzielne ustalanie podziału czasu zajęć na poszczególne edukacje oraz przerw według potrzeb i możliwości uczniów, w granicach rozkładu czasu pracy i planu dnia szkoły.", "rozporządzenie MEN w sprawie ramowych planów nauczania (3.04.2019 r.)"),
    w("Wybór lub opracowanie programu nauczania dostosowanego do potrzeb i możliwości uczniów oddziału oraz przedstawienie go dyrektorowi do dopuszczenia.", "art. 22a ustawy o systemie oświaty"),
    w("Dostosowanie metod, form, środków dydaktycznych i tempa pracy do zaleceń orzeczeń i IPET; stosowanie metod pedagogiki specjalnej (m.in. metoda ośrodków pracy, Metoda Dobrego Startu, ruch rozwijający W. Sherborne, elementy integracji sensorycznej, komunikacja alternatywna i wspomagająca AAC).", "§ 6 rozporządzenia MEN w sprawie warunków organizowania kształcenia specjalnego (9.08.2017 r.)"),
    w("Kształtowanie samoobsługi, higieny i umiejętności praktycznych uczniów (ubieranie, toaleta, spożywanie posiłków, porządek, poruszanie się po szkole) oraz orientacji zawodowej dostosowanej do wieku.", "podstawa programowa kształcenia specjalnego; rozporządzenie MEN w sprawie doradztwa zawodowego (12.02.2019 r.)"),
    w("Kierowanie pracą pomocy nauczyciela w czasie zajęć, posiłków i czynności opiekuńczych: podział zadań, instruktaż, wspólna realizacja IPET.", "§ 7 rozporządzenia MEN w sprawie organizacji publicznych szkół i przedszkoli (28.02.2019 r.), stosowany odpowiednio; statut szkoły"),
    w("Prowadzenie zajęć rewalidacyjnych i innych zajęć przydzielonych w planie lekcji zgodnie z posiadanymi kwalifikacjami.", "§ 5 rozporządzenia w sprawie kształcenia specjalnego; rozporządzenie MEN w sprawie kwalifikacji nauczycieli (1.08.2017 r.)"),

    "III. Kształcenie specjalne: IPET, WOPF, zespół",
    w("Udział w zespole opracowującym indywidualny program edukacyjno-terapeutyczny (IPET) dla każdego ucznia oddziału; jako wychowawca – koordynowanie pracy zespołu; opracowanie IPET do 30 września lub w ciągu 30 dni od otrzymania orzeczenia.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego (zespół, terminy opracowania IPET)"),
    w("Dokonywanie wielospecjalistycznej oceny poziomu funkcjonowania ucznia (WOPF) co najmniej dwa razy w roku szkolnym, ocena efektywności programu i jego modyfikacja; spotkania zespołu co najmniej dwa razy w roku.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego (WOPF, ocena efektywności, spotkania zespołu)"),
    w("Realizacja zaleceń zawartych w orzeczeniu o potrzebie kształcenia specjalnego oraz w IPET we wszystkich zajęciach i czynnościach opiekuńczych; prowadzenie obserwacji do WOPF.", "§ 5 i § 6 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Zawiadamianie rodziców o spotkaniach zespołu, umożliwienie im udziału, przekazanie kopii IPET i WOPF.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego (udział rodziców, kopie IPET i WOPF)"),
    w("Przygotowanie opinii zespołu w sprawie wydłużenia etapu edukacyjnego ucznia klasy III i wniosku do rady pedagogicznej (decyzja do końca lutego) po uzyskaniu zgody rodziców.", "§ 5 rozporządzenia w sprawie ramowych planów nauczania"),
    w("Rozpoznawanie indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych uczniów; współpraca ze specjalistami szkoły (psycholog, pedagog, pedagog specjalny, logopeda, rehabilitant) i z poradnią psychologiczno-pedagogiczną.", "rozporządzenie MEN w sprawie pomocy psychologiczno-pedagogicznej (9.08.2017 r.), stosowane odpowiednio; statut szkoły"),

    "IV. Wychowanie, opieka i bezpieczeństwo uczniów",
    w("Pełnienie funkcji wychowawcy oddziału: prowadzenie spraw wychowawczych, dokumentacji oddziału, koordynowanie pomocy dla uczniów, realizacja programu wychowawczo-profilaktycznego.", "art. 26 Prawa oświatowego; statut szkoły"),
    w("Ciągła opieka nad oddziałem w czasie zajęć, przerw, posiłków, czynności higienicznych i w szatni; niepozostawianie uczniów bez opieki; przekazanie opieki innej osobie na czas własnej przerwy.", "§ 2, § 13 i § 14 rozporządzenia MENiS w sprawie bezpieczeństwa i higieny w szkołach (31.12.2002 r.); art. 134 Kodeksu pracy"),
    w("Odbiór uczniów od rodziców lub opiekunów dowozu przed zajęciami i przekazanie ich po zajęciach wyłącznie osobom upoważnionym.", "statut szkoły; procedury wewnętrzne"),
    w("Sprawdzenie przed zajęciami stanu sali i sprzętu; niezwłoczne zgłaszanie dyrektorowi zagrożeń oraz każdego wypadku ucznia; udzielenie pierwszej pomocy; udział w szkoleniu z pierwszej pomocy.", "§ 2, § 13–14 i § 40–41 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach; § 21 tego rozporządzenia (szkolenie z pierwszej pomocy)"),
    w("Opieka nad uczniami w czasie wyjść, wycieczek, uroczystości i zawodów jako opiekun lub kierownik wycieczki; realizacja obowiązków kierownika lub opiekuna.", "rozporządzenie MEN w sprawie krajoznawstwa i turystyki (25.05.2018 r.)"),
    w("Znajomość i stosowanie standardów ochrony małoletnich obowiązujących w szkole; reagowanie na przemoc wobec dziecka, uruchamianie procedury „Niebieskie Karty” i zawiadamianie właściwych organów w przypadkach wymaganych prawem.", "art. 22b–22c ustawy o przeciwdziałaniu zagrożeniom przestępczością na tle seksualnym i ochronie małoletnich; art. 9d ustawy o przeciwdziałaniu przemocy domowej; art. 304 § 2 KPK"),
    w("Zapobieganie zachowaniom trudnym i reagowanie na nie zgodnie z procedurami szkoły i strategiami z IPET; dokumentowanie incydentów.", "IPET; procedury szkolne"),
    w("Znajomość stanu zdrowia uczniów (leki, epilepsja, dieta, alergie, zaopatrzenie ortopedyczne) i współpraca z pielęgniarką szkolną; podawanie leków wyłącznie na zasadach uzgodnionych z rodzicami i dyrektorem.", "art. 21 ustawy o opiece zdrowotnej nad uczniami (12.04.2019 r.)"),
    w("Zapoznanie uczniów z zasadami bezpieczeństwa, regulaminami i drogą ewakuacji w formie dostosowanej do ich możliwości; udział w próbnych ewakuacjach.", "rozporządzenie w sprawie bezpieczeństwa i higieny w szkołach"),

    "V. Ocenianie i klasyfikacja",
    w("Opracowanie wymagań edukacyjnych dostosowanych do IPET oraz poinformowanie uczniów i rodziców na początku roku szkolnego o wymaganiach, sposobach sprawdzania osiągnięć i warunkach oceniania zachowania.", "art. 44b ust. 8–9 ustawy o systemie oświaty"),
    w("Ocenianie bieżące w formie opisowej oraz ustalanie śródrocznej i rocznej opisowej oceny klasyfikacyjnej z zajęć edukacyjnych i zachowania; informacja zwrotna dla ucznia i rodziców.", "art. 44i ust. 1 i 7 oraz art. 44e ust. 2–3 ustawy o systemie oświaty"),
    w("Udział w klasyfikacji i w podejmowaniu przez radę pedagogiczną uchwał o promowaniu uczniów, w tym uczniów z niepełnosprawnością intelektualną w stopniu umiarkowanym lub znacznym z uwzględnieniem IPET.", "art. 44f–44o ustawy o systemie oświaty"),
    w("Wypełnianie świadectw opisowych i arkuszy ocen uczniów oddziału.", "rozporządzenie MEN w sprawie świadectw, dyplomów państwowych i innych druków; rozporządzenie w sprawie dokumentacji przebiegu nauczania"),

    "VI. Współpraca z rodzicami",
    w("Prowadzenie konsultacji dla rodziców i uczniów w terminie ustalonym w rozkładzie czasu pracy; organizowanie zebrań oddziału; codzienna komunikacja (zeszyt korespondencji, dziennik elektroniczny, rozmowy przy odbiorze ucznia).", "statut szkoły"),
    w("Informowanie rodziców o postępach, trudnościach, zachowaniu i stanie zdrowia dziecka; uzgadnianie form wsparcia; instruktaż do pracy w domu i do używania systemu komunikacji AAC.", "art. 44e i 44g ustawy o systemie oświaty; IPET"),
    w("Zbieranie zgód i oświadczeń rodziców (odbiór ucznia, wycieczki, wizerunek, badania, leki) i ich przechowywanie zgodnie z zasadami ochrony danych.", "statut szkoły; RODO"),

    "VII. Praca zespołowa i współpraca z instytucjami",
    w("Udział w zebraniach rady pedagogicznej, realizacja jej uchwał; praca w zespole edukacji wczesnoszkolnej, zespole wychowawczym i zespołach zadaniowych powołanych przez dyrektora.", "art. 69–73 Prawa oświatowego (w zakresie przewidzianym statutem szkoły niepublicznej); statut szkoły"),
    w("Współpraca z poradnią psychologiczno-pedagogiczną, ośrodkiem pomocy społecznej, powiatowym centrum pomocy rodzinie, sądem rodzinnym i kuratorem, ochroną zdrowia, przedszkolem i zespołem wczesnego wspomagania rozwoju przy przyjęciu ucznia.", "statut szkoły; rozporządzenie w sprawie pomocy psychologiczno-pedagogicznej"),
    w("Dzielenie się wiedzą: zajęcia otwarte, lekcje koleżeńskie, wsparcie nauczyciela początkującego lub praktykanta na przydział dyrektora.", "art. 9ca Karty Nauczyciela (stosowany na podstawie art. 91b KN); statut szkoły"),

    "VIII. Dokumentacja",
    w("Prowadzenie dziennika lekcyjnego oddziału: tematy zajęć, frekwencja, oceny opisowe, kontakty z rodzicami; dzienników zajęć rewalidacyjnych i innych prowadzonych zajęć.", "art. 14 ust. 3 pkt 5 Prawa oświatowego; rozporządzenie MEN w sprawie dokumentacji przebiegu nauczania (25.08.2017 r.)"),
    w("Prowadzenie dokumentacji kształcenia specjalnego uczniów oddziału: IPET, WOPF, arkusze obserwacji, teczki uczniów; przechowywanie zgodnie z instrukcją kancelaryjną i RODO.", "rozporządzenie w sprawie kształcenia specjalnego; statut szkoły"),
    w("Opracowanie rocznego planu pracy oddziału (rozkład materiału) i planu pracy wychowawcy; sprawozdania półroczne i roczne z pracy oddziału i realizacji IPET.", "statut szkoły"),
    w("Sporządzanie opinii o uczniu na wniosek rodziców, poradni, sądu lub innych uprawnionych instytucji, po akceptacji dyrektora.", "statut szkoły; przepisy szczególne"),

    "IX. Organizacja życia szkoły i mienie",
    w("Organizowanie uroczystości, konkursów, wyjść i imprez oddziału oraz udział w uroczystościach szkolnych zgodnie z planem pracy szkoły; udział w dniach otwartych i rekrutacji na przydział dyrektora.", "statut szkoły; plan pracy szkoły"),
    w("Opieka nad salą oddziału, pomocami dydaktycznymi i sprzętem; dbałość o estetykę i bezpieczeństwo pomieszczenia; udział w inwentaryzacji; odpowiedzialność materialna za mienie powierzone na piśmie.", "art. 124 Kodeksu pracy; statut szkoły"),

    "X. Przygotowanie do zajęć i doskonalenie zawodowe",
    w("Przygotowanie zajęć, pomocy dydaktycznych i terapeutycznych, kart pracy i materiałów w symbolach AAC; sprawdzanie i analiza prac uczniów – w czasie przewidzianym na to w rozkładzie czasu pracy.", "art. 128 Kodeksu pracy; rozkład czasu pracy"),
    w("Doskonalenie zawodowe zgodnie z potrzebami szkoły (szkolenia rady pedagogicznej, kursy z zakresu pedagogiki specjalnej, AAC, integracji sensorycznej); udział w szkoleniach zleconych przez pracodawcę w czasie pracy; realizacja ścieżki awansu zawodowego.", "art. 6 pkt 3 i 3a oraz art. 9a–9h Karty Nauczyciela (przez art. 91b KN); art. 94¹³ Kodeksu pracy"),
    w("Wykonywanie innych czynności zleconych przez dyrektora, wynikających ze statutu i organizacji pracy szkoły, zgodnych z kwalifikacjami i rodzajem umówionej pracy.", "art. 100 § 1 Kodeksu pracy; statut szkoły"),
  ];
}

// ---------- egzemplarz dla jednego nauczyciela ----------
function egzemplarz(nazwisko, logo, pierwszy) {
  const naglowekDok = new Table({
    width: { size: SZER, type: WidthType.DXA }, columnWidths: [1100, SZER - 1100],
    rows: [new TableRow({ children: [
      new TableCell({ width: { size: 1100, type: WidthType.DXA }, borders: bezRamek, verticalAlign: VerticalAlign.CENTER, children: [new Paragraph({ children: [new ImageRun({ type: "png", data: logo, transformation: { width: 64, height: 64 } })] })] }),
      new TableCell({ width: { size: SZER - 1100, type: WidthType.DXA }, borders: bezRamek, verticalAlign: VerticalAlign.CENTER, children: [
        new Paragraph({ spacing: { after: 30 }, children: [run(PLACOWKA + " · " + SZKOLA, { size: 17, color: SZARY })] }),
        new Paragraph({ spacing: { after: 30 }, children: [run("ZAKRES CZYNNOŚCI I OBOWIĄZKÓW", { size: 28, bold: true, color: FIOLET })] }),
        new Paragraph({ spacing: { after: 0 }, children: [run("nauczyciela edukacji wczesnoszkolnej w szkole specjalnej · rok szkolny " + ROK, { size: 19, color: POMARANCZ })] }),
      ] }),
    ] })],
  });

  const dane = tabela(null, [
    ["Imię i nazwisko", nazwisko],
    ["Stanowisko", "nauczyciel edukacji wczesnoszkolnej (klasy I–III) w szkole podstawowej specjalnej"],
    ["Podstawa zatrudnienia", "umowa o pracę – Kodeks pracy; z Karty Nauczyciela stosuje się przepisy wskazane w art. 91b ust. 2 (m.in. art. 6, art. 9–9i, art. 75–85z)"],
    ["Wymiar i rozkład czasu pracy", "30 godzin tygodniowo (6 godzin dziennie od poniedziałku do piątku) według rozkładu czasu pracy ustalonego przez dyrektora; w tym czasie: zajęcia z uczniami i opieka, dokumentacja, zebrania, konsultacje, przygotowanie do zajęć; 15-minutowa przerwa wliczana do czasu pracy (art. 134 KP)"],
    ["Bezpośredni przełożony", "dyrektor szkoły"],
    ["Oddział / wychowawstwo", "oddział: ………………………………   wychowawstwo:  ☐ TAK   ☐ NIE"],
    ["Zastępstwo w czasie nieobecności", "…………………………………………………………………………"],
    ["Wymagane kwalifikacje", "kwalifikacje do nauczania w klasach I–III oraz z zakresu pedagogiki specjalnej odpowiedniej do niepełnosprawności uczniów (rozporządzenie MEN z 1.08.2017 r.); szkolenie BHP i z pierwszej pomocy; aktualne orzeczenie lekarskie o braku przeciwwskazań; niekaralność sprawdzona w Rejestrze Sprawców Przestępstw na Tle Seksualnym (art. 21 ustawy o ochronie małoletnich) oraz w KRK; kwalifikacje jak dla szkół publicznych (art. 14 ust. 3 pkt 6 Prawa oświatowego)"],
  ], [3000, 7160], { boldCol: 0 });

  const indyw = tabela(["Lp.", "Czynność przydzielona indywidualnie", "Termin / wymiar", "Uwagi"],
    [1, 2, 3, 4, 5].map((i) => [String(i), "", "", ""]), [480, 5480, 2100, 2100]);

  const odpow = tabela(["Zakres odpowiedzialności", "Podstawa"], [
    ["Za życie, zdrowie i bezpieczeństwo uczniów powierzonych opiece w czasie zajęć i czynności organizowanych przez szkołę.", "art. 6 pkt 1 KN; rozporządzenie w sprawie bezpieczeństwa i higieny w szkołach"],
    ["Za realizację podstawy programowej, IPET i zaleceń orzeczeń oraz za rzetelność oceniania.", "przepisy oświatowe wskazane w tabeli obowiązków"],
    ["Za prawidłowe i terminowe prowadzenie dokumentacji oraz ochronę danych osobowych.", "rozporządzenie w sprawie dokumentacji przebiegu nauczania; RODO"],
    ["Za mienie powierzone na piśmie oraz za przestrzeganie czasu pracy, regulaminu pracy i przepisów BHP.", "art. 100, 114, 124 i 211 Kodeksu pracy"],
    ["Odpowiedzialność porządkowa i dyscyplinarna za uchybienia obowiązkom.", "art. 108 Kodeksu pracy; art. 75–85z Karty Nauczyciela (przez art. 91b KN)"],
  ], [6960, 3200], { zebra: true });

  const podpisy = new Table({
    width: { size: SZER, type: WidthType.DXA }, columnWidths: [5080, 5080],
    rows: [new TableRow({ cantSplit: true, children: [
      new TableCell({ width: { size: 5080, type: WidthType.DXA }, borders: bezRamek, children: [
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400 }, children: [run("………………………………………………", { size: 18 })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, children: [run("data i podpis dyrektora", { size: 16, color: SZARY })] }),
      ] }),
      new TableCell({ width: { size: 5080, type: WidthType.DXA }, borders: bezRamek, children: [
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400 }, children: [run("………………………………………………", { size: 18 })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, children: [run("data i podpis nauczyciela: " + nazwisko, { size: 16, color: SZARY })] }),
      ] }),
    ] })],
  });

  return [
    ...(pierwszy ? [] : [new Paragraph({ pageBreakBefore: true, spacing: { after: 0 }, children: [run("", { size: 2 })] })]),
    naglowekDok,
    new Paragraph({ spacing: { after: 100 }, border: { bottom: { style: BorderStyle.SINGLE, size: 10, color: POMARANCZ, space: 4 } }, children: [] }),
    tytulSekcji("1. Dane stanowiska"),
    dane,
    tytulSekcji("2. Czynności i obowiązki wynikające z przepisów prawa i statutu szkoły"),
    tabela(["Lp.", "Czynność / obowiązek", "Podstawa prawna"], obowiazki(), SZ, { zebra: true, center: [0] }),
    tytulSekcji("3. Czynności przydzielone indywidualnie na rok szkolny " + ROK),
    indyw,
    tytulSekcji("4. Zakres odpowiedzialności"),
    odpow,
    tytulSekcji("5. Oświadczenie"),
    new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 60, line: 260 }, children: [run("Potwierdzam zapoznanie się z zakresem czynności i obowiązków, przyjmuję go do wiadomości i stosowania oraz zobowiązuję się do wykonywania pracy zgodnie z nim, regulaminem pracy, statutem szkoły i obowiązującymi przepisami. Zakres czynności sporządzono w dwóch jednobrzmiących egzemplarzach: jeden dla pracownika, drugi do akt osobowych (część B).", { size: 18 })] }),
    new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 0, line: 260 }, children: [run("Zakres czynności stanowi uszczegółowienie rodzaju pracy określonego w umowie o pracę (art. 29 § 1 i art. 94 pkt 1 Kodeksu pracy). Zmiana zakresu w granicach umówionego rodzaju pracy nie wymaga wypowiedzenia zmieniającego.", { size: 17, color: SZARY })] }),
    podpisy,
  ];
}

// ---------- dokument ----------
const logo = fs.readFileSync(LOGO);
const naglowek = new Header({ children: [new Paragraph({
  tabStops: [{ type: TabStopType.RIGHT, position: SZER }], border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: FIOLET, space: 4 } }, spacing: { after: 160 },
  children: [new ImageRun({ type: "png", data: logo, transformation: { width: 22, height: 22 } }), run("   " + PLACOWKA, { size: 15, color: SZARY }), run("\tZakres czynności – nauczyciel edukacji wczesnoszkolnej – " + ROK, { size: 15, color: FIOLET })],
})] });
const stopka = new Footer({ children: [new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 80 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: POMARANCZ, space: 4 } },
  children: [run("Strona ", { size: 15, color: SZARY }), new TextRun({ children: [PageNumber.CURRENT], font: F, size: 15, color: SZARY }), run("   •   zatrudnienie na podstawie Kodeksu pracy, 30 godzin tygodniowo   •   stan prawny: wrzesień 2026 r.", { size: 15, color: SZARY })],
})] });

const children = [];
NAUCZYCIELE.forEach((n, i) => children.push(...egzemplarz(n, logo, i === 0)));

const doc = new Document({
  creator: PLACOWKA, title: "Zakres czynności nauczyciela edukacji wczesnoszkolnej " + ROK,
  styles: { default: { document: { run: { font: F, size: 18 } } } },
  sections: [{ properties: { page: { margin: { top: 900, bottom: 850, left: 1000, right: 1000 } } }, headers: { default: naglowek }, footers: { default: stopka }, children }],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log("zapisano", OUT, buf.length, "B", "egzemplarze:", NAUCZYCIELE.join(", ")); });
