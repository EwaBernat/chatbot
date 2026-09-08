// Generator druku "Zakres czynności i obowiązków nauczyciela języka polskiego, wychowawcy
// oddziału klasy IV, prowadzącego zajęcia rewalidacyjne o charakterze logopedycznym w szkole
// specjalnej" – osobny egzemplarz dla każdego nauczyciela (Kodeks pracy, 30 godzin tygodniowo).
// Uruchomienie (z katalogu głównego repozytorium):
//   npm install docx sharp
//   node -e "require('sharp')('logo-lawenda.webp').png().toFile('logo.png')"
//   node dokumenty/generuj_druk_jezyk_polski_logopedia.js logo.png dokumenty/druk-zakres-czynnosci-jezyk-polski-wychowawstwo-4-logopedia.docx "Imię Nazwisko"
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber, TabStopType, VerticalAlign,
} = require("docx");

const [,, LOGO = "logo.png", OUT = "druk.docx", ...NAUCZYCIELE] = process.argv;
if (NAUCZYCIELE.length === 0) NAUCZYCIELE.push("……………………………………");

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
    w("Prowadzenie lekcji języka polskiego w oddziałach wskazanych w planie lekcji, zgodnie z planem nauczania i podstawą programową kształcenia ogólnego dostosowaną do potrzeb uczniów z niepełnosprawnością intelektualną w stopniu lekkim; w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną – zajęć z odrębnej podstawy programowej.", "art. 14 ust. 3 i art. 127 Prawa oświatowego; rozporządzenie MEN w sprawie podstawy programowej (14.02.2017 r.); rozporządzenie MEN w sprawie ramowych planów nauczania (3.04.2019 r.)"),
    w("Punktualne rozpoczynanie i kończenie lekcji (45 minut), przestrzeganie planu lekcji i dzwonków ustalonych przez dyrektora; przejmowanie i przekazywanie oddziału między lekcjami tak, aby uczniowie nie pozostawali bez opieki.", "§ 4 rozporządzenia w sprawie ramowych planów nauczania; statut szkoły"),
    w("Wybór lub opracowanie programu nauczania języka polskiego dostosowanego do potrzeb i możliwości uczniów oddziału oraz przedstawienie go dyrektorowi do dopuszczenia.", "art. 22a ustawy o systemie oświaty"),
    w("Dostosowanie metod, form, środków dydaktycznych, tempa pracy i sposobu sprawdzania wiedzy do zaleceń orzeczeń i IPET: instrukcje krótkie i obrazkowe, praca na konkretach, wydłużony czas, dzielenie zadań na etapy, komunikacja alternatywna i wspomagająca (AAC) u uczniów niemówiących.", "§ 6 rozporządzenia MEN w sprawie warunków organizowania kształcenia specjalnego (9.08.2017 r.)"),
    w("Współpraca z pomocą nauczyciela obecną na lekcji (podział zadań, wsparcie uczniów wymagających stałej pomocy) oraz z wychowawcami innych oddziałów w sprawach organizacyjnych i wychowawczych.", "§ 7 rozporządzenia MEN w sprawie organizacji publicznych szkół i przedszkoli (28.02.2019 r.), stosowany odpowiednio; statut szkoły"),

    "III. Język polski",
    w("Nauczanie języka polskiego z naciskiem na komunikację, czytanie ze zrozumieniem, pisanie użytkowe (formularz, list, wiadomość, ogłoszenie), rozumienie poleceń i tekstów z życia codziennego; teksty uproszczone i wspomagane obrazem, wielokrotne powtarzanie, stopniowanie trudności; dobór lektur i ich fragmentów dostosowany do możliwości uczniów zgodnie z IPET.", "podstawa programowa języka polskiego (wersja dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim); IPET"),
    w("Opracowanie i stosowanie przedmiotowych zasad oceniania oraz wymagań edukacyjnych z języka polskiego dostosowanych do IPET każdego ucznia, w tym zasad oceniania prac pisemnych i ortografii z uwzględnieniem zaleceń orzeczeń; poinformowanie o nich uczniów i rodziców na początku roku szkolnego.", "art. 44b ust. 8–9 ustawy o systemie oświaty"),
    w("Przygotowanie uczniów klasy VIII z niepełnosprawnością intelektualną w stopniu lekkim do egzaminu ósmoklasisty z języka polskiego, jeśli nauczyciel uczy w tej klasie: realizacja wymagań egzaminacyjnych, arkusze próbne, informacja dla rady pedagogicznej o dostosowaniach (arkusz dostosowany, wydłużony czas, zasady oceniania z pominięciem błędów ortograficznych); udział w zespołach nadzorujących na powołanie dyrektora.", "art. 44zw ustawy o systemie oświaty; rozporządzenie MEN w sprawie egzaminu ósmoklasisty; komunikat dyrektora CKE o dostosowaniach"),
    w("Rozwijanie zainteresowań czytelniczych i kultury: współpraca z biblioteką szkolną i publiczną, wyjścia do teatru i kina, konkursy recytatorskie i czytelnicze, przygotowanie uczniów do wystąpień podczas uroczystości szkolnych; edukacja medialna dostosowana do możliwości uczniów.", "podstawa programowa języka polskiego; statut szkoły; plan pracy szkoły"),
    w("Opieka nad biblioteczką polonistyczną, pomocami dydaktycznymi i sprzętem: ewidencja, zgłaszanie potrzeb, udział w inwentaryzacji; odpowiedzialność materialna za mienie powierzone na piśmie.", "art. 124 Kodeksu pracy; statut szkoły"),

    "IV. Zajęcia rewalidacyjne o charakterze logopedycznym",
    w("Prowadzenie zajęć rewalidacyjnych o charakterze logopedycznym z uczniami wskazanymi w przydziale, zgodnie z zaleceniami orzeczenia i IPET: ćwiczenia oddechowe, fonacyjne, artykulacyjne, słuchu fonemowego, rozwijanie mowy czynnej i biernej, komunikacji i rozumienia; godzina zajęć rewalidacyjnych trwa 60 minut.", "§ 5 i § 6 rozporządzenia w sprawie kształcenia specjalnego; rozporządzenie w sprawie ramowych planów nauczania (czas trwania zajęć rewalidacyjnych)"),
    w("Przeprowadzenie na początku roku szkolnego przesiewowej diagnozy logopedycznej uczniów oraz pogłębionej diagnozy uczniów objętych zajęciami; opracowanie dla każdego ucznia programu terapii logopedycznej na podstawie orzeczenia, diagnozy, WOPF i IPET; ocena postępów i modyfikacja programu po każdej ocenie efektywności.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego; IPET; § 20 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej (zadania logopedy, stosowane odpowiednio)"),
    w("Wprowadzanie i rozwijanie komunikacji alternatywnej i wspomagającej (AAC) u uczniów niemówiących lub mówiących w ograniczonym zakresie: dobór systemu (gesty, symbole, książka komunikacyjna, urządzenia), nauka jego używania, przekazanie systemu nauczycielom i rodzicom.", "§ 5 i § 6 rozporządzenia w sprawie kształcenia specjalnego; IPET"),
    w("Prowadzenie dziennika zajęć rewalidacyjnych (logopedycznych): program, tematy, obecność, obserwacje i ocena postępów ucznia; dokumentacja diagnoz.", "§ 11 rozporządzenia MEN w sprawie dokumentacji przebiegu nauczania (25.08.2017 r.)"),
    w("Przekazywanie nauczycielom i rodzicom zaleceń do pracy z uczniem (ćwiczenia w domu, sposób komunikacji, wspieranie mowy na lekcjach); instruktaż i konsultacje; wskazywanie rodzicom potrzeby konsultacji specjalistycznych (laryngolog, ortodonta, audiolog, neurolog).", "§ 5 i § 6 rozporządzenia w sprawie kształcenia specjalnego; statut szkoły"),
    w("Zachowanie higieny zajęć logopedycznych: dezynfekcja lub jednorazowe użycie szpatułek i pomocy, czystość lusterek i sprzętu, wietrzenie gabinetu; bezpieczeństwo uczniów podczas ćwiczeń.", "rozporządzenie w sprawie bezpieczeństwa i higieny w szkołach; procedury sanitarne szkoły"),
    w("Współpraca z logopedą i innymi specjalistami szkoły, poradnią psychologiczno-pedagogiczną oraz zespołem wczesnego wspomagania rozwoju w zakresie spójnej terapii mowy ucznia.", "rozporządzenie w sprawie pomocy psychologiczno-pedagogicznej; statut szkoły"),

    "V. Wychowawstwo oddziału klasy IV",
    w("Prowadzenie zajęć z wychowawcą (1 godzina tygodniowo) zgodnie z programem wychowawczo-profilaktycznym szkoły i planem pracy wychowawcy: integracja zespołu, emocje, relacje, bezpieczeństwo, orientacja zawodowa, przygotowanie do samodzielności.", "rozporządzenie w sprawie ramowych planów nauczania; art. 26 Prawa oświatowego; rozporządzenie MEN w sprawie doradztwa zawodowego (12.02.2019 r.)"),
    w("Opieka nad adaptacją uczniów klasy IV do nauki w systemie przedmiotowym: przejęcie informacji o uczniach i dokumentacji od wychowawcy klasy III, uzgodnienie z nauczycielami przedmiotów jednolitych zasad i strategii z IPET, wsparcie uczniów w zmianach sal i nauczycieli, współpraca z pomocą nauczyciela zatrudnioną w oddziale.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego; § 7 rozporządzenia w sprawie organizacji publicznych szkół i przedszkoli (stosowany odpowiednio); statut szkoły"),
    w("Koordynowanie pracy zespołu ds. IPET każdego ucznia oddziału: zwoływanie spotkań, opracowanie IPET z wkładem nauczycieli i specjalistów, organizacja WOPF co najmniej dwa razy w roku, zawiadamianie rodziców, przekazanie im kopii IPET i WOPF.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego (zespół, terminy, udział rodziców)"),
    w("Rozpoznawanie sytuacji wychowawczej, rodzinnej i zdrowotnej uczniów oddziału; planowanie i koordynowanie pomocy psychologiczno-pedagogicznej dla uczniów oddziału; współpraca ze specjalistami szkoły i instytucjami.", "rozporządzenie MEN w sprawie pomocy psychologiczno-pedagogicznej (9.08.2017 r.), stosowane odpowiednio; statut szkoły"),
    w("Ustalanie śródrocznej i rocznej oceny klasyfikacyjnej zachowania uczniów oddziału po zasięgnięciu opinii nauczycieli, uczniów oddziału i ocenianego ucznia; informowanie uczniów i rodziców o przewidywanych ocenach w terminie określonym w statucie.", "art. 44g i art. 44h ustawy o systemie oświaty"),
    w("Prowadzenie dokumentacji oddziału: dziennik lekcyjny (część oddziałowa), arkusze ocen, świadectwa, teczki uczniów, zgody i oświadczenia rodziców, listy osób upoważnionych do odbioru uczniów, karta zdrowia i informacje o lekach.", "rozporządzenie w sprawie dokumentacji przebiegu nauczania; rozporządzenie w sprawie świadectw, dyplomów państwowych i innych druków; statut szkoły"),
    w("Organizowanie zebrań z rodzicami oddziału (co najmniej według harmonogramu szkoły), konsultacji indywidualnych i bieżącej komunikacji; przekazywanie informacji o postępach, frekwencji i zachowaniu; kontrola frekwencji i wyjaśnianie nieobecności.", "art. 44e ustawy o systemie oświaty; art. 41–42 Prawa oświatowego (obowiązek szkolny); statut szkoły"),
    w("Organizowanie życia oddziału: wycieczki, wyjścia, imprezy klasowe, udział oddziału w uroczystościach szkolnych, opieka nad salą oddziału; jako kierownik lub opiekun wycieczki – realizacja obowiązków z rozporządzenia.", "rozporządzenie MEN w sprawie krajoznawstwa i turystyki (25.05.2018 r.); statut szkoły"),
    w("Realizacja orientacji zawodowej w klasie IV w ramach zajęć z wychowawcą i wycieczek (poznawanie zawodów, samodzielność, zainteresowania) oraz informowanie rodziców o dalszej ścieżce edukacyjnej i możliwościach wsparcia.", "rozporządzenie MEN w sprawie doradztwa zawodowego (12.02.2019 r.); statut szkoły"),

    "VI. Kształcenie specjalne: IPET, WOPF, zespół (jako nauczyciel języka polskiego)",
    w("Udział w zespołach opracowujących IPET uczniów każdego oddziału, w którym nauczyciel uczy; wkład w części dotyczącej języka polskiego i komunikacji; opracowanie IPET do 30 września lub w ciągu 30 dni od otrzymania orzeczenia.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Wkład do wielospecjalistycznej oceny poziomu funkcjonowania ucznia (WOPF) co najmniej dwa razy w roku szkolnym w zakresie funkcjonowania na lekcjach i zajęciach logopedycznych (mowa, komunikacja, czytanie i pisanie); udział w ocenie efektywności i modyfikacji IPET.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Realizacja zaleceń zawartych w orzeczeniu o potrzebie kształcenia specjalnego oraz w IPET na każdej lekcji; prowadzenie obserwacji do WOPF; rozpoznawanie indywidualnych potrzeb i możliwości uczniów.", "§ 5 i § 6 rozporządzenia w sprawie kształcenia specjalnego; rozporządzenie w sprawie pomocy psychologiczno-pedagogicznej"),

    "VII. Opieka i bezpieczeństwo uczniów",
    w("Pełnienie dyżurów przed lekcjami, w czasie przerw i po lekcjach według harmonogramu dyżurów (korytarze, szatnia, stołówka, boisko, przystanek dowozu); aktywny nadzór i reagowanie na zagrożenia.", "§ 14 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach; statut szkoły"),
    w("Sprawdzenie przed zajęciami stanu sali i sprzętu; niezwłoczne zgłaszanie dyrektorowi zagrożeń oraz każdego wypadku ucznia; udzielenie pierwszej pomocy; udział w szkoleniu z pierwszej pomocy.", "§ 2, § 13, § 21 i § 40–41 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach"),
    w("Znajomość i stosowanie standardów ochrony małoletnich obowiązujących w szkole; reagowanie na przemoc wobec dziecka, uruchamianie procedury „Niebieskie Karty” i zawiadamianie właściwych organów w przypadkach wymaganych prawem.", "art. 22b–22c ustawy o przeciwdziałaniu zagrożeniom przestępczością na tle seksualnym i ochronie małoletnich; art. 9d ustawy o przeciwdziałaniu przemocy domowej; art. 304 § 2 KPK"),
    w("Zapobieganie zachowaniom trudnym i reagowanie na nie zgodnie z procedurami szkoły i strategiami z IPET; dokumentowanie incydentów; znajomość stanu zdrowia uczniów (leki, epilepsja, dieta, alergie) i współpraca z pielęgniarką szkolną.", "IPET; procedury szkolne; art. 21 ustawy o opiece zdrowotnej nad uczniami"),

    "VIII. Ocenianie, klasyfikacja i egzaminy",
    w("Ocenianie bieżące z języka polskiego: stopnie w skali 1–6 w oddziałach dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim, oceny opisowe w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną; jawność ocen i ich uzasadnianie; sprawdziany dostosowane do IPET.", "art. 44e i art. 44i ust. 7 ustawy o systemie oświaty"),
    w("Ustalanie śródrocznych i rocznych ocen klasyfikacyjnych z języka polskiego; udział w klasyfikacji i uchwałach rady pedagogicznej o promowaniu, w tym uczniów z niepełnosprawnością umiarkowaną lub znaczną z uwzględnieniem IPET.", "art. 44f–44o ustawy o systemie oświaty"),
    w("Udział w egzaminach klasyfikacyjnych, poprawkowych i sprawdzianach wiadomości w komisjach powołanych przez dyrektora.", "art. 44l–44n ustawy o systemie oświaty"),

    "IX. Współpraca z rodzicami (jako nauczyciel języka polskiego i logopeda)",
    w("Prowadzenie konsultacji dla rodziców i uczniów w terminie ustalonym w rozkładzie czasu pracy; udział w zebraniach; komunikacja przez dziennik elektroniczny; informowanie o postępach i trudnościach z języka polskiego oraz o efektach terapii logopedycznej; instruktaż do ćwiczeń logopedycznych w domu.", "art. 44e i 44g ustawy o systemie oświaty; IPET; statut szkoły"),

    "X. Praca zespołowa i współpraca z instytucjami",
    w("Udział w zebraniach rady pedagogicznej, realizacja jej uchwał; praca w zespole przedmiotowym humanistycznym, zespole specjalistów, zespole wychowawców klas IV–VIII i zespołach zadaniowych powołanych przez dyrektora.", "art. 69–73 Prawa oświatowego (w zakresie przewidzianym statutem szkoły niepublicznej); statut szkoły"),
    w("Współpraca z poradnią psychologiczno-pedagogiczną, ośrodkiem pomocy społecznej, powiatowym centrum pomocy rodzinie, sądem rodzinnym i kuratorem, ochroną zdrowia oraz innymi instytucjami wspierającymi uczniów oddziału.", "statut szkoły; rozporządzenie w sprawie pomocy psychologiczno-pedagogicznej"),
    w("Dzielenie się wiedzą: zajęcia otwarte, lekcje koleżeńskie, wsparcie nauczyciela początkującego lub praktykanta na przydział dyrektora; udział w promocji szkoły i dniach otwartych.", "art. 9ca Karty Nauczyciela (stosowany na podstawie art. 91b KN); statut szkoły"),

    "XI. Dokumentacja",
    w("Prowadzenie wpisów w dziennikach lekcyjnych każdego oddziału: tematy, frekwencja, oceny; dziennika zajęć rewalidacyjnych (logopedycznych); jako wychowawca – całości dokumentacji oddziału klasy IV.", "art. 14 ust. 3 pkt 5 Prawa oświatowego; rozporządzenie MEN w sprawie dokumentacji przebiegu nauczania (25.08.2017 r.)"),
    w("Opracowanie planów wynikowych (rozkładów materiału) języka polskiego dla każdego oddziału, przedmiotowych zasad oceniania, programów terapii logopedycznej, planu pracy wychowawcy; sprawozdania półroczne i roczne z realizacji przedmiotu, terapii logopedycznej i pracy wychowawczej.", "statut szkoły"),
    w("Sporządzanie opinii o uczniach oddziału na wniosek rodziców, poradni, sądu lub innych uprawnionych instytucji, po akceptacji dyrektora.", "statut szkoły; przepisy szczególne"),

    "XII. Przygotowanie do zajęć i doskonalenie zawodowe",
    w("Przygotowanie lekcji i zajęć logopedycznych, materiałów dostosowanych (teksty uproszczone, karty pracy, materiał obrazkowy, pomoce logopedyczne, zadania o różnym poziomie trudności); sprawdzanie prac uczniów – w czasie przewidzianym na to w rozkładzie czasu pracy.", "art. 128 Kodeksu pracy; rozkład czasu pracy"),
    w("Doskonalenie zawodowe zgodnie z potrzebami szkoły: szkolenia rady pedagogicznej, kursy z dydaktyki języka polskiego dla uczniów z niepełnosprawnością intelektualną, metod terapii logopedycznej, AAC, pracy wychowawczej; realizacja ścieżki awansu zawodowego. Szkolenie na polecenie pracodawcy jest czasem pracy.", "art. 6 pkt 3 i 3a oraz art. 9a–9h Karty Nauczyciela (przez art. 91b KN); art. 94¹³ Kodeksu pracy"),
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
        new Paragraph({ spacing: { after: 0 }, children: [run("nauczyciela języka polskiego, wychowawcy klasy IV, prowadzącego zajęcia rewalidacyjne o charakterze logopedycznym w szkole specjalnej · rok szkolny " + ROK, { size: 19, color: POMARANCZ })] }),
      ] }),
    ] })],
  });

  const dane = tabela(null, [
    ["Imię i nazwisko", nazwisko],
    ["Stanowisko", "nauczyciel języka polskiego w szkole podstawowej specjalnej; wychowawca oddziału klasy IV; nauczyciel prowadzący zajęcia rewalidacyjne o charakterze logopedycznym"],
    ["Nauczane przedmioty i klasy", "język polski: klasy ………………………   zajęcia rewalidacyjne o charakterze logopedycznym: uczniowie ……………………………   (oddziały dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim; w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną – treści polonistyczne w ramach zajęć rozwijających komunikowanie się i funkcjonowania osobistego i społecznego)"],
    ["Wychowawstwo", "oddział klasy IV – wychowawca; zajęcia z wychowawcą 1 godzina tygodniowo w planie lekcji; koordynowanie zespołu ds. IPET uczniów oddziału; opieka nad adaptacją uczniów po przejściu z edukacji wczesnoszkolnej"],
    ["Podstawa zatrudnienia", "umowa o pracę – Kodeks pracy; z Karty Nauczyciela stosuje się przepisy wskazane w art. 91b ust. 2 (m.in. art. 6, art. 9–9i, art. 75–85z)"],
    ["Wymiar i rozkład czasu pracy", "30 godzin tygodniowo (6 godzin dziennie od poniedziałku do piątku) według rozkładu czasu pracy ustalonego przez dyrektora; w tym czasie: lekcje i zajęcia logopedyczne według planu, dyżury, zadania wychowawcy, dokumentacja, zebrania, konsultacje, przygotowanie zajęć; 15-minutowa przerwa wliczana do czasu pracy (art. 134 KP)"],
    ["Bezpośredni przełożony", "dyrektor szkoły"],
    ["Pracownia", "opieka nad gabinetem logopedycznym i pomocami:  ☐ TAK   ☐ NIE      sala oddziału klasy IV:  ☐ TAK   ☐ NIE      biblioteczka polonistyczna:  ☐ TAK   ☐ NIE"],
    ["Zastępstwo w czasie nieobecności", "…………………………………………………………………………"],
    ["Wymagane kwalifikacje", "kwalifikacje do nauczania języka polskiego oraz z zakresu pedagogiki specjalnej odpowiedniej do niepełnosprawności uczniów; kwalifikacje z zakresu logopedii (studia lub studia podyplomowe) do prowadzenia zajęć rewalidacyjnych o charakterze logopedycznym (rozporządzenie MEN z 1.08.2017 r. w sprawie kwalifikacji); szkolenie BHP i z pierwszej pomocy; aktualne orzeczenie lekarskie o braku przeciwwskazań; niekaralność sprawdzona w Rejestrze Sprawców Przestępstw na Tle Seksualnym (art. 21 ustawy o ochronie małoletnich) oraz w KRK; kwalifikacje jak dla szkół publicznych (art. 14 ust. 3 pkt 6 Prawa oświatowego)"],
  ], [3000, 7160], { boldCol: 0 });

  const indyw = tabela(["Lp.", "Czynność przydzielona indywidualnie", "Termin / wymiar", "Uwagi"],
    [1, 2, 3, 4, 5].map((i) => [String(i), "", "", ""]), [480, 5480, 2100, 2100]);

  const odpow = tabela(["Zakres odpowiedzialności", "Podstawa"], [
    ["Za życie, zdrowie i bezpieczeństwo uczniów powierzonych opiece w czasie zajęć i czynności organizowanych przez szkołę.", "art. 6 pkt 1 KN; rozporządzenie w sprawie bezpieczeństwa i higieny w szkołach"],
    ["Za realizację podstawy programowej, IPET i zaleceń orzeczeń oraz za rzetelność oceniania.", "przepisy oświatowe wskazane w tabeli obowiązków"],
    ["Za prawidłowe i terminowe prowadzenie dokumentacji oraz ochronę danych osobowych.", "rozporządzenie w sprawie dokumentacji przebiegu nauczania; RODO"],
    ["Za higienę i bezpieczeństwo zajęć logopedycznych oraz za mienie powierzone na piśmie (gabinet, pomoce, sala oddziału).", "rozporządzenie w sprawie bezpieczeństwa i higieny w szkołach; art. 124 Kodeksu pracy"],
    ["Jako wychowawca – za terminowość IPET i WOPF uczniów oddziału, dokumentację oddziału i kontakt z rodzicami.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego; statut szkoły"],
    ["Za przestrzeganie czasu pracy, regulaminu pracy i przepisów BHP.", "art. 100, 114 i 211 Kodeksu pracy"],
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
    new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 60, line: 260 }, keepNext: true, children: [run("Potwierdzam zapoznanie się z zakresem czynności i obowiązków, przyjmuję go do wiadomości i stosowania oraz zobowiązuję się do wykonywania pracy zgodnie z nim, regulaminem pracy, statutem szkoły i obowiązującymi przepisami. Zakres czynności sporządzono w dwóch jednobrzmiących egzemplarzach: jeden dla pracownika, drugi do akt osobowych (część B).", { size: 18 })] }),
    new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 0, line: 260 }, keepNext: true, children: [run("Zakres czynności stanowi uszczegółowienie rodzaju pracy określonego w umowie o pracę (art. 29 § 1 i art. 94 pkt 1 Kodeksu pracy). Zmiana zakresu w granicach umówionego rodzaju pracy nie wymaga wypowiedzenia zmieniającego.", { size: 17, color: SZARY })] }),
    podpisy,
  ];
}

// ---------- dokument ----------
const logo = fs.readFileSync(LOGO);
const naglowek = new Header({ children: [new Paragraph({
  tabStops: [{ type: TabStopType.RIGHT, position: SZER }], border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: FIOLET, space: 4 } }, spacing: { after: 160 },
  children: [new ImageRun({ type: "png", data: logo, transformation: { width: 22, height: 22 } }), run("   " + PLACOWKA, { size: 15, color: SZARY }), run("\tZakres czynności – język polski, wychowawstwo klasy IV, logopedia – " + ROK, { size: 15, color: FIOLET })],
})] });
const stopka = new Footer({ children: [new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 80 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: POMARANCZ, space: 4 } },
  children: [run("Strona ", { size: 15, color: SZARY }), new TextRun({ children: [PageNumber.CURRENT], font: F, size: 15, color: SZARY }), run("   •   zatrudnienie na podstawie Kodeksu pracy, 30 godzin tygodniowo   •   stan prawny: wrzesień 2026 r.", { size: 15, color: SZARY })],
})] });

const children = [];
NAUCZYCIELE.forEach((n, i) => children.push(...egzemplarz(n, logo, i === 0)));

const doc = new Document({
  creator: PLACOWKA, title: "Zakres czynności nauczyciela języka polskiego, wychowawcy klasy IV " + ROK,
  styles: { default: { document: { run: { font: F, size: 18 } } } },
  sections: [{ properties: { page: { margin: { top: 900, bottom: 850, left: 1000, right: 1000 } } }, headers: { default: naglowek }, footers: { default: stopka }, children }],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log("zapisano", OUT, buf.length, "B", "egzemplarze:", NAUCZYCIELE.join(", ")); });
