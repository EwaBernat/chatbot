// Generator druku "Zakres czynności i obowiązków pedagoga szkolnego i nauczyciela
// współorganizującego kształcenie w oddziale klasy III szkoły specjalnej" – osobny egzemplarz
// dla każdej osoby (Kodeks pracy, 30 godzin tygodniowo).
// Uruchomienie (z katalogu głównego repozytorium):
//   npm install docx sharp
//   node -e "require('sharp')('logo-lawenda.webp').png().toFile('logo.png')"
//   node dokumenty/generuj_druk_pedagog_wspolorganizujacy.js logo.png dokumenty/druk-zakres-czynnosci-pedagog-wspolorganizujacy-3.docx "Sara ………………"
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber, TabStopType, VerticalAlign,
} = require("docx");

const [,, LOGO = "logo.png", OUT = "druk.docx", ...NAUCZYCIELE] = process.argv;
if (NAUCZYCIELE.length === 0) NAUCZYCIELE.push("Sara ………………");

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
    w("Przestrzeganie ustalonego czasu pracy: 30 godzin tygodniowo według rozkładu czasu pracy, z podziałem na zadania pedagoga i pracę w oddziale klasy III; potwierdzanie obecności; praca poza rozkładem wyłącznie na polecenie pracodawcy.", "art. 100 § 2 pkt 1, art. 129 i art. 149 Kodeksu pracy; regulamin pracy"),
    w("Przestrzeganie przepisów oraz zasad bezpieczeństwa i higieny pracy i przepisów przeciwpożarowych; udział w szkoleniach BHP; poddawanie się wstępnym, okresowym i kontrolnym badaniom lekarskim.", "art. 100 § 2 pkt 3, art. 211 i art. 229 Kodeksu pracy"),
    w("Zachowanie w tajemnicy informacji o uczniach, ich rodzinach, sytuacji prawnej i stanie zdrowia, w tym informacji uzyskanych w toku diagnoz i interwencji; przetwarzanie danych osobowych, także danych szczególnej kategorii, wyłącznie w zakresie upoważnienia i zgodnie z RODO oraz polityką ochrony danych szkoły.", "art. 100 § 2 pkt 4 i 5 Kodeksu pracy; art. 9 RODO (rozporządzenie UE 2016/679); polityka ochrony danych szkoły"),

    "II. Pedagog szkolny – diagnoza i pomoc psychologiczno-pedagogiczna",
    w("Diagnozowanie indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych uczniów w celu określenia mocnych stron, predyspozycji, zainteresowań i uzdolnień oraz przyczyn niepowodzeń edukacyjnych lub trudności w funkcjonowaniu, w tym barier i ograniczeń utrudniających uczestnictwo w życiu szkoły.", "§ 24 pkt 1 rozporządzenia MEN w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej (9.08.2017 r.), stosowany odpowiednio w szkole niepublicznej; statut szkoły"),
    w("Diagnozowanie sytuacji wychowawczych w szkole w celu rozwiązywania problemów wychowawczych ograniczających aktywne i pełne uczestnictwo ucznia w życiu szkoły; obserwacje w oddziałach, rozmowy z uczniami, nauczycielami i rodzicami.", "§ 24 pkt 2 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej"),
    w("Udzielanie uczniom pomocy psychologiczno-pedagogicznej w formach odpowiednich do rozpoznanych potrzeb: porady i konsultacje, zajęcia rozwijające kompetencje emocjonalno-społeczne, warsztaty, rozmowy wspierające, praca indywidualna z uczniem w kryzysie.", "§ 24 pkt 3 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej; § 6 tego rozporządzenia (formy pomocy)"),
    w("Wspieranie nauczycieli, wychowawców i specjalistów w rozpoznawaniu potrzeb uczniów, udzielaniu pomocy psychologiczno-pedagogicznej oraz w doborze metod i strategii pracy z uczniem, w tym z uczniem z zachowaniami trudnymi; opracowywanie planów wsparcia pozytywnego zachowania.", "§ 24 pkt 7–8 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej"),
    w("Pomoc rodzicom i nauczycielom w rozpoznawaniu i rozwijaniu indywidualnych możliwości, predyspozycji i uzdolnień uczniów; porady i konsultacje dla rodziców w terminie ustalonym w rozkładzie czasu pracy.", "§ 24 pkt 7 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej; statut szkoły"),
    w("Koordynowanie, na przydział dyrektora, organizacji pomocy psychologiczno-pedagogicznej w szkole: ewidencja uczniów objętych pomocą, wnioski i informacje dla rodziców, ocena efektywności udzielanej pomocy przed zakończeniem każdego okresu, współpraca z wychowawcami.", "§ 20 i § 22–23 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej; statut szkoły"),
    w("Współpraca z poradnią psychologiczno-pedagogiczną: przygotowywanie opinii szkoły o uczniu, wspieranie rodziców w składaniu wniosków o orzeczenia i opinie, wdrażanie zaleceń poradni; analiza orzeczeń i opinii nowych uczniów.", "rozporządzenie MEN w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające (7.09.2017 r.); statut szkoły"),
    w("Udział w zespołach opracowujących IPET jako specjalista: wkład do wielospecjalistycznej oceny poziomu funkcjonowania ucznia (WOPF) w zakresie funkcjonowania emocjonalno-społecznego i sytuacji wychowawczej, udział w spotkaniach zespołów, wnioski do modyfikacji IPET.", "§ 6 rozporządzenia MEN w sprawie warunków organizowania kształcenia specjalnego (9.08.2017 r.)"),

    "III. Pedagog szkolny – profilaktyka, interwencja, ochrona dziecka",
    w("Udział w diagnozie potrzeb rozwojowych uczniów, czynników chroniących i czynników ryzyka w środowisku szkolnym oraz w opracowaniu i ewaluacji programu wychowawczo-profilaktycznego szkoły.", "art. 26 ust. 2 Prawa oświatowego"),
    w("Podejmowanie działań z zakresu profilaktyki uzależnień, przemocy rówieśniczej, cyberprzemocy i innych problemów dzieci i młodzieży: zajęcia profilaktyczne dostosowane do uczniów z niepełnosprawnością intelektualną, programy rekomendowane, współpraca z instytucjami.", "§ 24 pkt 4 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej; rozporządzenie MEN w sprawie zakresu i form działalności wychowawczej, edukacyjnej, informacyjnej i profilaktycznej (18.08.2015 r.)"),
    w("Minimalizowanie skutków zaburzeń rozwojowych, zapobieganie zaburzeniom zachowania oraz inicjowanie różnych form pomocy w środowisku szkolnym i pozaszkolnym uczniów.", "§ 24 pkt 5 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej"),
    w("Inicjowanie i prowadzenie działań mediacyjnych i interwencyjnych w sytuacjach kryzysowych (konflikty, przemoc, zagrożenie zdrowia lub życia, samookaleczenia, kryzys w rodzinie) zgodnie z procedurami szkoły; sporządzanie notatek z interwencji.", "§ 24 pkt 6 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej; procedury szkolne"),
    w("Znajomość, stosowanie i – jeśli wyznaczy dyrektor – koordynowanie standardów ochrony małoletnich: przyjmowanie zgłoszeń, prowadzenie rejestru interwencji, plan wsparcia dziecka, szkolenie pracowników, coroczny przegląd standardów.", "art. 22b–22c ustawy o przeciwdziałaniu zagrożeniom przestępczością na tle seksualnym i ochronie małoletnich"),
    w("Rozpoznawanie przemocy domowej wobec uczniów, wszczynanie procedury „Niebieskie Karty” (wypełnienie formularza A), udział w grupach diagnostyczno-pomocowych oraz zawiadamianie sądu rodzinnego, prokuratury lub policji w przypadkach wymaganych prawem.", "art. 9d ustawy o przeciwdziałaniu przemocy domowej; rozporządzenie Rady Ministrów w sprawie procedury „Niebieskie Karty” (6.09.2023 r.); art. 304 § 2 KPK; art. 572 KPC"),
    w("Monitorowanie realizacji obowiązku szkolnego i frekwencji uczniów we współpracy z wychowawcami; działania wobec uczniów nieuczęszczających do szkoły, informowanie dyrektora, kontakt z rodzicami i instytucjami.", "art. 41–42 Prawa oświatowego; statut szkoły"),
    w("Rozpoznawanie sytuacji materialnej i rodzinnej uczniów oraz inicjowanie pomocy: dożywianie, stypendia i zasiłki szkolne, wyprawka, współpraca z ośrodkiem pomocy społecznej, powiatowym centrum pomocy rodzinie, asystentami rodziny i kuratorami.", "art. 90b–90e ustawy o systemie oświaty (pomoc materialna); ustawa o pomocy społecznej; statut szkoły"),

    "IV. Pedagog szkolny – współpraca z rodzicami, nauczycielami i instytucjami",
    w("Prowadzenie konsultacji dla rodziców i uczniów w stałym terminie podanym do wiadomości; udział w zebraniach z rodzicami na zaproszenie wychowawców; pedagogizacja rodziców (spotkania, materiały).", "statut szkoły; rozporządzenie w sprawie pomocy psychologiczno-pedagogicznej"),
    w("Współpraca z sądem rodzinnym i kuratorami sądowymi, policją, ośrodkiem pomocy społecznej, powiatowym centrum pomocy rodzinie, zespołem interdyscyplinarnym, ochroną zdrowia, poradniami specjalistycznymi i organizacjami pozarządowymi; udzielanie informacji o uczniach wyłącznie w trybie i zakresie przewidzianym prawem.", "statut szkoły; przepisy szczególne; RODO"),
    w("Udział w zebraniach rady pedagogicznej, przedstawianie radzie analiz sytuacji wychowawczej i informacji o realizacji pomocy psychologiczno-pedagogicznej; praca w zespole wychowawczym, zespole specjalistów i zespołach zadaniowych.", "art. 69–73 Prawa oświatowego (w zakresie przewidzianym statutem szkoły niepublicznej); statut szkoły"),
    w("Prowadzenie szkoleń i konsultacji dla nauczycieli z zakresu pracy z uczniem z niepełnosprawnością intelektualną, zachowań trudnych, interwencji kryzysowej i ochrony małoletnich, na przydział dyrektora.", "§ 24 pkt 8 rozporządzenia w sprawie pomocy psychologiczno-pedagogicznej; statut szkoły"),

    "V. Nauczyciel współorganizujący kształcenie w oddziale klasy III",
    w("Prowadzenie wspólnie z nauczycielem edukacji wczesnoszkolnej zajęć edukacyjnych oraz wspólna realizacja zintegrowanych działań i zajęć określonych w IPET uczniów wskazanych w przydziale; udział we wszystkich zajęciach oddziału w godzinach ustalonych w rozkładzie czasu pracy.", "§ 7 ust. 7 pkt 1 rozporządzenia MEN w sprawie warunków organizowania kształcenia specjalnego (9.08.2017 r.)"),
    w("Prowadzenie wspólnie z nauczycielem oddziału pracy wychowawczej z uczniami; wsparcie uczniów w regulacji emocji, relacjach z rówieśnikami, przestrzeganiu zasad i uczestnictwie w życiu klasy.", "§ 7 ust. 7 pkt 2 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Uczestniczenie w zajęciach prowadzonych przez innych nauczycieli (religia, język obcy, wychowanie fizyczne, zajęcia specjalistyczne) w zakresie wynikającym z potrzeb uczniów oraz z rozkładu czasu pracy.", "§ 7 ust. 7 pkt 3 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Udzielanie nauczycielom prowadzącym zajęcia pomocy w doborze form i metod pracy z uczniami z orzeczeniem: dostosowanie materiałów, kart pracy i poleceń, przygotowanie pomocy wizualnych i materiałów w symbolach AAC, planowanie wspólnych lekcji.", "§ 7 ust. 7 pkt 4 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Prowadzenie zajęć rewalidacyjnych lub innych zajęć odpowiednich ze względu na potrzeby uczniów, jeśli zostały przydzielone w planie, zgodnie z posiadanymi kwalifikacjami.", "§ 7 ust. 7 pkt 5 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Bezpośrednie wspieranie uczniów objętych orzeczeniem w czasie zajęć i przerw: kierowanie uwagi, dzielenie zadań na etapy, wydłużanie czasu, wspomaganie komunikacji (AAC), pomoc w czynnościach samoobsługowych i przemieszczaniu się, zapobieganie zachowaniom trudnym i reagowanie na nie zgodnie z IPET.", "§ 5 i § 6 rozporządzenia w sprawie kształcenia specjalnego; IPET"),
    w("Udział w zespole ds. IPET uczniów oddziału klasy III: współopracowanie IPET, prowadzenie obserwacji i wkład do WOPF co najmniej dwa razy w roku, ocena efektywności i modyfikacja programu, udział w spotkaniach z rodzicami.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Współpraca z pomocą nauczyciela zatrudnioną w oddziale, ze specjalistami szkoły i z rodzicami uczniów w zakresie jednolitych strategii pracy i przenoszenia efektów terapii do zajęć; bieżące informowanie rodziców o funkcjonowaniu dziecka w uzgodnieniu z nauczycielem oddziału.", "§ 7 rozporządzenia w sprawie organizacji publicznych szkół i przedszkoli (28.02.2019 r.), stosowany odpowiednio; statut szkoły"),
    w("Dokumentowanie pracy w oddziale: wpisy w dzienniku lekcyjnym oddziału jako nauczyciel współprowadzący, arkusze obserwacji uczniów, dokumentacja realizacji IPET, sprawozdania półroczne i roczne.", "rozporządzenie MEN w sprawie dokumentacji przebiegu nauczania (25.08.2017 r.); statut szkoły"),

    "VI. Opieka i bezpieczeństwo uczniów",
    w("Sprawowanie opieki nad uczniami oddziału klasy III w czasie zajęć, przerw, posiłków i czynności higienicznych wspólnie z nauczycielem oddziału; pełnienie dyżurów według harmonogramu w pozostałym czasie; aktywny nadzór i reagowanie na zagrożenia.", "§ 2, § 13–14 rozporządzenia MENiS w sprawie bezpieczeństwa i higieny w szkołach (31.12.2002 r.); statut szkoły"),
    w("Niezwłoczne zgłaszanie dyrektorowi zagrożeń oraz każdego wypadku ucznia; udzielenie pierwszej pomocy; udział w szkoleniu z pierwszej pomocy.", "§ 21 i § 40–41 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach"),
    w("Opieka nad uczniami w czasie wyjść, wycieczek i uroczystości jako opiekun lub kierownik wycieczki; realizacja obowiązków kierownika lub opiekuna.", "rozporządzenie MEN w sprawie krajoznawstwa i turystyki (25.05.2018 r.)"),
    w("Znajomość stanu zdrowia uczniów oddziału (leki, epilepsja, dieta, alergie, zaopatrzenie ortopedyczne) i współpraca z pielęgniarką szkolną.", "art. 21 ustawy o opiece zdrowotnej nad uczniami (12.04.2019 r.); procedury szkolne"),

    "VII. Dokumentacja pedagoga",
    w("Prowadzenie dziennika pedagoga: tygodniowy rozkład zajęć, zajęcia i czynności przeprowadzone w poszczególnych dniach, kontakty z osobami i instytucjami, imiona i nazwiska uczniów objętych różnymi formami pomocy.", "§ 18 rozporządzenia MEN w sprawie dokumentacji przebiegu nauczania (25.08.2017 r.)"),
    w("Prowadzenie dokumentacji badań i czynności uzupełniających, notatek z interwencji i rozmów, ewidencji uczniów objętych pomocą psychologiczno-pedagogiczną, dokumentacji procedury „Niebieskie Karty” i rejestru zgłoszeń ze standardów ochrony małoletnich; przechowywanie zgodnie z instrukcją kancelaryjną i RODO.", "§ 19 rozporządzenia w sprawie dokumentacji przebiegu nauczania; ustawa o ochronie małoletnich; polityka ochrony danych"),
    w("Opracowanie rocznego planu pracy pedagoga oraz sprawozdań półrocznych i rocznych z pracy pedagoga i z pracy w oddziale klasy III; sporządzanie opinii o uczniach dla poradni, sądu i innych uprawnionych instytucji po akceptacji dyrektora.", "statut szkoły; przepisy szczególne"),

    "VIII. Przygotowanie do zajęć i doskonalenie zawodowe",
    w("Przygotowanie zajęć, warsztatów i materiałów profilaktycznych oraz pomocy do pracy w oddziale (materiały dostosowane, symbole AAC, plany aktywności, wzmocnienia) – w czasie przewidzianym na to w rozkładzie czasu pracy.", "art. 128 Kodeksu pracy; rozkład czasu pracy"),
    w("Doskonalenie zawodowe zgodnie z potrzebami szkoły: interwencja kryzysowa, ochrona małoletnich i procedura „Niebieskie Karty”, praca z uczniem z autyzmem i niepełnosprawnością intelektualną, pozytywne wspieranie zachowań, AAC; realizacja ścieżki awansu zawodowego. Szkolenie na polecenie pracodawcy jest czasem pracy.", "art. 6 pkt 3 i 3a oraz art. 9a–9h Karty Nauczyciela (przez art. 91b KN); art. 94¹³ Kodeksu pracy"),
    w("Dzielenie się wiedzą: zajęcia otwarte, konsultacje koleżeńskie, wsparcie nauczyciela początkującego lub praktykanta na przydział dyrektora; udział w promocji szkoły i dniach otwartych.", "art. 9ca Karty Nauczyciela (stosowany na podstawie art. 91b KN); statut szkoły"),
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
        new Paragraph({ spacing: { after: 0 }, children: [run("pedagoga szkolnego i nauczyciela współorganizującego kształcenie w oddziale klasy III szkoły specjalnej · rok szkolny " + ROK, { size: 19, color: POMARANCZ })] }),
      ] }),
    ] })],
  });

  const dane = tabela(null, [
    ["Imię i nazwisko", nazwisko],
    ["Stanowisko", "pedagog szkolny w szkole podstawowej specjalnej oraz nauczyciel współorganizujący kształcenie uczniów w oddziale klasy III"],
    ["Podział wymiaru między role", "zadania pedagoga szkolnego: ……… godzin tygodniowo   praca w oddziale klasy III jako nauczyciel współorganizujący: ……… godzin tygodniowo   (razem 30 godzin; podział ustala dyrektor w rozkładzie czasu pracy i może go zmienić stosownie do potrzeb uczniów)"],
    ["Oddział i uczniowie", "oddział klasy III: ………   uczniowie objęci wsparciem nauczyciela współorganizującego (orzeczenia): ……………………………   nauczyciel prowadzący oddział: ………………………"],
    ["Podstawa zatrudnienia", "umowa o pracę – Kodeks pracy; z Karty Nauczyciela stosuje się przepisy wskazane w art. 91b ust. 2 (m.in. art. 6, art. 9–9i, art. 75–85z)"],
    ["Wymiar i rozkład czasu pracy", "30 godzin tygodniowo (6 godzin dziennie od poniedziałku do piątku) według rozkładu czasu pracy ustalonego przez dyrektora; w tym czasie: praca w oddziale klasy III, zajęcia i konsultacje pedagoga, diagnozy, interwencje, spotkania zespołów, dokumentacja, kontakt z rodzicami i instytucjami; 15-minutowa przerwa wliczana do czasu pracy (art. 134 KP)"],
    ["Bezpośredni przełożony", "dyrektor szkoły"],
    ["Gabinet i funkcje", "gabinet pedagoga:  ☐ TAK   ☐ NIE      osoba odpowiedzialna za standardy ochrony małoletnich lub przyjmowanie zgłoszeń:  ☐ TAK   ☐ NIE      koordynator pomocy psychologiczno-pedagogicznej w szkole:  ☐ TAK   ☐ NIE"],
    ["Zastępstwo w czasie nieobecności", "…………………………………………………………………………"],
    ["Wymagane kwalifikacje", "kwalifikacje do zajmowania stanowiska pedagoga (studia z pedagogiki lub inne wskazane w rozporządzeniu) oraz kwalifikacje z zakresu pedagogiki specjalnej odpowiedniej do niepełnosprawności uczniów – wymagane dla nauczyciela współorganizującego kształcenie (rozporządzenie MEN z 1.08.2017 r. w sprawie kwalifikacji); szkolenie BHP i z pierwszej pomocy; aktualne orzeczenie lekarskie o braku przeciwwskazań; niekaralność sprawdzona w Rejestrze Sprawców Przestępstw na Tle Seksualnym (art. 21 ustawy o ochronie małoletnich) oraz w KRK; kwalifikacje jak dla szkół publicznych (art. 14 ust. 3 pkt 6 Prawa oświatowego)"],
  ], [3000, 7160], { boldCol: 0 });

  const indyw = tabela(["Lp.", "Czynność przydzielona indywidualnie", "Termin / wymiar", "Uwagi"],
    [1, 2, 3, 4, 5].map((i) => [String(i), "", "", ""]), [480, 5480, 2100, 2100]);

  const odpow = tabela(["Zakres odpowiedzialności", "Podstawa"], [
    ["Za życie, zdrowie i bezpieczeństwo uczniów powierzonych opiece w czasie zajęć i czynności organizowanych przez szkołę.", "art. 6 pkt 1 KN; rozporządzenie w sprawie bezpieczeństwa i higieny w szkołach"],
    ["Za rzetelność diagnoz, adekwatność udzielanej pomocy psychologiczno-pedagogicznej i terminowość działań interwencyjnych oraz procedur ochrony dziecka.", "rozporządzenie w sprawie pomocy psychologiczno-pedagogicznej; ustawa o ochronie małoletnich; ustawa o przeciwdziałaniu przemocy domowej"],
    ["Za realizację IPET uczniów objętych wsparciem w oddziale klasy III i współpracę z nauczycielem oddziału.", "§ 6–7 rozporządzenia w sprawie kształcenia specjalnego"],
    ["Za prawidłowe i terminowe prowadzenie dokumentacji pedagoga oraz ochronę danych osobowych, w tym danych szczególnej kategorii.", "rozporządzenie w sprawie dokumentacji przebiegu nauczania; RODO"],
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
    new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 60, line: 260 }, keepNext: true, children: [run("Potwierdzam zapoznanie się z zakresem czynności i obowiązków, przyjmuję go do wiadomości i stosowania oraz zobowiązuję się do wykonywania pracy zgodnie z nim, regulaminem pracy, statutem szkoły i obowiązującymi przepisami. Zakres czynności sporządzono w dwóch jednobrzmiących egzemplarzach: jeden dla pracownika, drugi do akt osobowych (część B).", { size: 18 })] }),
    new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 0, line: 260 }, keepNext: true, children: [run("Zakres czynności stanowi uszczegółowienie rodzaju pracy określonego w umowie o pracę (art. 29 § 1 i art. 94 pkt 1 Kodeksu pracy). Zmiana zakresu w granicach umówionego rodzaju pracy nie wymaga wypowiedzenia zmieniającego.", { size: 17, color: SZARY })] }),
    podpisy,
  ];
}

// ---------- dokument ----------
const logo = fs.readFileSync(LOGO);
const naglowek = new Header({ children: [new Paragraph({
  tabStops: [{ type: TabStopType.RIGHT, position: SZER }], border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: FIOLET, space: 4 } }, spacing: { after: 160 },
  children: [new ImageRun({ type: "png", data: logo, transformation: { width: 22, height: 22 } }), run("   " + PLACOWKA, { size: 15, color: SZARY }), run("\tZakres czynności – pedagog szkolny, współorganizujący kl. III – " + ROK, { size: 15, color: FIOLET })],
})] });
const stopka = new Footer({ children: [new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 80 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: POMARANCZ, space: 4 } },
  children: [run("Strona ", { size: 15, color: SZARY }), new TextRun({ children: [PageNumber.CURRENT], font: F, size: 15, color: SZARY }), run("   •   zatrudnienie na podstawie Kodeksu pracy, 30 godzin tygodniowo   •   stan prawny: wrzesień 2026 r.", { size: 15, color: SZARY })],
})] });

const children = [];
NAUCZYCIELE.forEach((n, i) => children.push(...egzemplarz(n, logo, i === 0)));

const doc = new Document({
  creator: PLACOWKA, title: "Zakres czynności pedagoga szkolnego i nauczyciela współorganizującego " + ROK,
  styles: { default: { document: { run: { font: F, size: 18 } } } },
  sections: [{ properties: { page: { margin: { top: 900, bottom: 850, left: 1000, right: 1000 } } }, headers: { default: naglowek }, footers: { default: stopka }, children }],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log("zapisano", OUT, buf.length, "B", "egzemplarze:", NAUCZYCIELE.join(", ")); });
