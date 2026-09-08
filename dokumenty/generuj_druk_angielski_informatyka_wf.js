// Generator druku "Zakres czynności i obowiązków nauczyciela języka angielskiego, informatyki
// i wychowania fizycznego w szkole specjalnej" – osobny egzemplarz dla każdego nauczyciela
// (Kodeks pracy, 30 godzin tygodniowo).
// Uruchomienie (z katalogu głównego repozytorium):
//   npm install docx sharp
//   node -e "require('sharp')('logo-lawenda.webp').png().toFile('logo.png')"
//   node dokumenty/generuj_druk_angielski_informatyka_wf.js logo.png dokumenty/druk-zakres-czynnosci-angielski-informatyka-wf.docx "Kacper K."
const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType,
  AlignmentType, ShadingType, BorderStyle, ImageRun, Header, Footer, PageNumber, TabStopType, VerticalAlign,
} = require("docx");

const [,, LOGO = "logo.png", OUT = "druk.docx", ...NAUCZYCIELE] = process.argv;
if (NAUCZYCIELE.length === 0) NAUCZYCIELE.push("Kacper K.");

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

    "II. Dydaktyka – obowiązki wspólne dla wszystkich nauczanych przedmiotów",
    w("Prowadzenie lekcji języka angielskiego, informatyki i wychowania fizycznego w oddziałach wskazanych w planie lekcji, zgodnie z planem nauczania i podstawą programową kształcenia ogólnego dostosowaną do potrzeb uczniów z niepełnosprawnością intelektualną w stopniu lekkim; w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną – zajęć z odrębnej podstawy programowej.", "art. 14 ust. 3 i art. 127 Prawa oświatowego; rozporządzenie MEN w sprawie podstawy programowej (14.02.2017 r.); rozporządzenie MEN w sprawie ramowych planów nauczania (3.04.2019 r.)"),
    w("Punktualne rozpoczynanie i kończenie lekcji (45 minut), przestrzeganie planu lekcji i dzwonków ustalonych przez dyrektora; przejmowanie i przekazywanie oddziału między lekcjami tak, aby uczniowie nie pozostawali bez opieki.", "§ 4 rozporządzenia w sprawie ramowych planów nauczania; statut szkoły"),
    w("Wybór lub opracowanie programu nauczania każdego przedmiotu dostosowanego do potrzeb i możliwości uczniów oddziału oraz przedstawienie go dyrektorowi do dopuszczenia.", "art. 22a ustawy o systemie oświaty"),
    w("Dostosowanie metod, form, środków dydaktycznych, tempa pracy i sposobu sprawdzania wiedzy do zaleceń orzeczeń i IPET: instrukcje krótkie i obrazkowe, praca na konkretach, wydłużony czas, dzielenie zadań na etapy, komunikacja alternatywna i wspomagająca (AAC) u uczniów niemówiących.", "§ 6 rozporządzenia MEN w sprawie warunków organizowania kształcenia specjalnego (9.08.2017 r.)"),
    w("Współpraca z pomocą nauczyciela obecną na lekcji (podział zadań, wsparcie uczniów wymagających stałej pomocy) oraz z wychowawcą oddziału w sprawach organizacyjnych i wychowawczych.", "§ 7 rozporządzenia MEN w sprawie organizacji publicznych szkół i przedszkoli (28.02.2019 r.), stosowany odpowiednio; statut szkoły"),
    w("Prowadzenie innych zajęć przydzielonych w planie lekcji zgodnie z posiadanymi kwalifikacjami (np. zajęcia rewalidacyjne, zajęcia sportowe, koło językowe lub informatyczne).", "§ 5 rozporządzenia w sprawie kształcenia specjalnego; rozporządzenie MEN w sprawie kwalifikacji nauczycieli (1.08.2017 r.)"),

    "III. Język angielski",
    w("Nauczanie języka angielskiego jako języka obcego nowożytnego z naciskiem na komunikację, słownictwo funkcjonalne i sytuacje z życia codziennego; metody multisensoryczne, wizualne i powtórzeniowe; rozwijanie sprawności w tempie dostosowanym do ucznia.", "podstawa programowa języka obcego nowożytnego (wersja dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim); IPET"),
    w("Opracowanie i stosowanie przedmiotowych zasad oceniania oraz wymagań edukacyjnych z języka angielskiego dostosowanych do IPET każdego ucznia; poinformowanie o nich uczniów i rodziców na początku roku szkolnego.", "art. 44b ust. 8–9 ustawy o systemie oświaty"),
    w("Wnioskowanie do dyrektora o zwolnienie ucznia z nauki drugiego języka obcego, gdy orzeczenie lub opinia poradni to uzasadnia, oraz realizacja zaleceń zwolnienia.", "§ 6 rozporządzenia MEN w sprawie oceniania, klasyfikowania i promowania (22.02.2019 r.)"),
    w("Przygotowanie uczniów klasy VIII z niepełnosprawnością intelektualną w stopniu lekkim do egzaminu ósmoklasisty z języka angielskiego: realizacja wymagań egzaminacyjnych, arkusze próbne, informacja dla rady pedagogicznej o dostosowaniach (arkusz dostosowany, wydłużony czas, odtwarzanie nagrań w dostosowany sposób).", "art. 44zw ustawy o systemie oświaty; rozporządzenie MEN w sprawie egzaminu ósmoklasisty; komunikat dyrektora CKE o dostosowaniach"),
    w("Udział w zespołach nadzorujących egzamin ósmoklasisty na powołanie dyrektora, w czasie pracy; przestrzeganie procedur egzaminacyjnych.", "rozporządzenie MEN w sprawie egzaminu ósmoklasisty; procedury CKE"),
    w("Organizowanie konkursów i wydarzeń językowych (Europejski Dzień Języków, konkursy słownikowe), udział uczniów w konkursach zewnętrznych dostosowanych do ich możliwości.", "statut szkoły; plan pracy szkoły"),

    "IV. Informatyka",
    w("Prowadzenie zajęć informatyki w pracowni komputerowej: obsługa komputera i urządzeń, bezpieczne korzystanie z internetu, programy użytkowe, elementy programowania wizualnego, w tempie i zakresie dostosowanym do możliwości uczniów; w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną – elementy technologii informacyjnej wspierające komunikację i kreatywność.", "podstawa programowa informatyki (wersja dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim); podstawa programowa dla uczniów z niepełnosprawnością umiarkowaną lub znaczną"),
    w("Wprowadzenie regulaminu pracowni komputerowej i egzekwowanie zasad bezpieczeństwa: sprawdzenie stanu sprzętu i instalacji przed zajęciami, zgłaszanie usterek, zakaz samodzielnego ingerowania uczniów w instalacje.", "§ 2 i § 13 rozporządzenia MENiS w sprawie bezpieczeństwa i higieny w szkołach (31.12.2002 r.); regulamin pracowni"),
    w("Edukacja w zakresie bezpieczeństwa cyfrowego i profilaktyki cyberprzemocy: zasady ochrony danych i wizerunku, kontakty w sieci, zgłaszanie zagrożeń; stosowanie filtrów i zabezpieczeń chroniących uczniów przed treściami szkodliwymi.", "art. 27 Prawa oświatowego; program wychowawczo-profilaktyczny; standardy ochrony małoletnich"),
    w("Dobór i konfigurowanie technologii wspomagających dla uczniów z niepełnosprawnością (klawiatury i myszy alternatywne, oprogramowanie AAC, powiększenie, syntezator mowy) we współpracy ze specjalistami i zespołem ds. IPET.", "§ 5 i § 6 rozporządzenia w sprawie kształcenia specjalnego; IPET"),
    w("Opieka nad pracownią komputerową, sprzętem i oprogramowaniem: prowadzenie ewidencji, zgłaszanie potrzeb, dbałość o legalność oprogramowania i aktualizacje, udział w inwentaryzacji; odpowiedzialność materialna za mienie powierzone na piśmie.", "art. 124 Kodeksu pracy; ustawa o prawie autorskim i prawach pokrewnych; statut szkoły"),
    w("Wsparcie techniczne innych nauczycieli w wykorzystaniu technologii informacyjnej w zajęciach oraz w prowadzeniu dziennika elektronicznego – w zakresie przydzielonym przez dyrektora.", "statut szkoły; przydział czynności"),

    "V. Wychowanie fizyczne",
    w("Prowadzenie wychowania fizycznego zgodnie z podstawą programową: rozwijanie sprawności, umiejętności ruchowych, gier zespołowych, edukacji zdrowotnej; dostosowanie ćwiczeń do rodzaju niepełnosprawności, sprawności i stanu zdrowia każdego ucznia; ćwiczenia korekcyjne i rozwijające motorykę w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną.", "podstawa programowa wychowania fizycznego; § 31 ust. 2 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach (dostosowanie stopnia trudności i intensywności ćwiczeń)"),
    w("Sprawdzenie przed każdymi zajęciami stanu technicznego sali gimnastycznej, boiska, urządzeń i sprzętu sportowego; niedopuszczanie do używania sprzętu uszkodzonego; zgłaszanie usterek dyrektorowi.", "§ 31 ust. 6 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach"),
    w("Zapoznanie uczniów z zasadami bezpiecznego uczestnictwa w zajęciach ruchowych i z regulaminem sali gimnastycznej i boiska w formie dostosowanej do ich możliwości; nadzór nad uczniami w szatni i w drodze na boisko.", "§ 31 ust. 1, 3 i 4 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach"),
    w("Uwzględnianie opinii lekarza o ograniczonych możliwościach wykonywania określonych ćwiczeń oraz decyzji dyrektora o zwolnieniu ucznia z zajęć; zapewnienie opieki uczniom zwolnionym lub niećwiczącym obecnym na zajęciach.", "§ 4 i § 5 rozporządzenia MEN w sprawie oceniania, klasyfikowania i promowania (22.02.2019 r.)"),
    w("Ocenianie wychowania fizycznego z uwzględnieniem przede wszystkim wysiłku wkładanego przez ucznia, systematyczności udziału w zajęciach oraz aktywności na rzecz sportu szkolnego i kultury fizycznej.", "§ 9 rozporządzenia MEN w sprawie oceniania, klasyfikowania i promowania (22.02.2019 r.)"),
    w("Udzielanie pierwszej pomocy i posiadanie aktualnego przeszkolenia w tym zakresie; znajomość stanu zdrowia uczniów istotnego dla wysiłku fizycznego (epilepsja, wady serca, zaopatrzenie ortopedyczne) i współpraca z pielęgniarką szkolną.", "§ 21 i § 40 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach; art. 21 ustawy o opiece zdrowotnej nad uczniami"),
    w("Organizowanie szkolnych zawodów, Dnia Sportu, rozgrywek i udziału uczniów w zawodach zewnętrznych (m.in. Olimpiady Specjalne); prowadzenie zajęć sportowych przydzielonych przez dyrektora; opieka nad uczniami w czasie zawodów i wyjazdów sportowych.", "rozporządzenie MEN w sprawie krajoznawstwa i turystyki (25.05.2018 r.); statut szkoły"),
    w("Opieka nad salą gimnastyczną, magazynem sprzętu sportowego i boiskiem: ewidencja sprzętu, zgłaszanie potrzeb, udział w inwentaryzacji; odpowiedzialność materialna za mienie powierzone na piśmie.", "art. 124 Kodeksu pracy; statut szkoły"),

    "VI. Kształcenie specjalne: IPET, WOPF, zespół",
    w("Udział w zespołach opracowujących indywidualne programy edukacyjno-terapeutyczne (IPET) uczniów każdego oddziału, w którym nauczyciel uczy; wkład w części dotyczącej nauczanych przedmiotów; opracowanie IPET do 30 września lub w ciągu 30 dni od otrzymania orzeczenia.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego (zespół, terminy opracowania IPET)"),
    w("Wkład do wielospecjalistycznej oceny poziomu funkcjonowania ucznia (WOPF) co najmniej dwa razy w roku szkolnym w zakresie funkcjonowania na lekcjach języka angielskiego, informatyki i wychowania fizycznego; udział w ocenie efektywności i modyfikacji IPET; udział w spotkaniach zespołu.", "§ 6 rozporządzenia w sprawie kształcenia specjalnego (WOPF, ocena efektywności, spotkania zespołu)"),
    w("Realizacja zaleceń zawartych w orzeczeniu o potrzebie kształcenia specjalnego oraz w IPET na każdej lekcji; prowadzenie obserwacji do WOPF.", "§ 5 i § 6 rozporządzenia w sprawie kształcenia specjalnego"),
    w("Rozpoznawanie indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych uczniów; współpraca ze specjalistami szkoły (psycholog, pedagog, pedagog specjalny, logopeda, rehabilitant) i z poradnią psychologiczno-pedagogiczną.", "rozporządzenie MEN w sprawie pomocy psychologiczno-pedagogicznej (9.08.2017 r.), stosowane odpowiednio; statut szkoły"),

    "VII. Wychowanie, opieka i bezpieczeństwo uczniów",
    w("Pełnienie funkcji wychowawcy oddziału, jeśli została powierzona: prowadzenie zajęć z wychowawcą, spraw wychowawczych i dokumentacji oddziału, koordynowanie zespołu ds. IPET oddziału, ustalanie oceny zachowania, kontakt z rodzicami.", "art. 26 Prawa oświatowego; art. 44h ustawy o systemie oświaty; statut szkoły"),
    w("Pełnienie dyżurów przed lekcjami, w czasie przerw i po lekcjach według harmonogramu dyżurów (korytarze, szatnia, stołówka, boisko, przystanek dowozu); aktywny nadzór i reagowanie na zagrożenia.", "§ 14 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach; statut szkoły"),
    w("Sprawdzenie przed zajęciami stanu sali i sprzętu; niezwłoczne zgłaszanie dyrektorowi zagrożeń oraz każdego wypadku ucznia; udzielenie pierwszej pomocy.", "§ 2, § 13 i § 40–41 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach"),
    w("Opieka nad uczniami w czasie wyjść, wycieczek, zawodów, uroczystości jako opiekun lub kierownik wycieczki; realizacja obowiązków kierownika lub opiekuna.", "rozporządzenie MEN w sprawie krajoznawstwa i turystyki (25.05.2018 r.)"),
    w("Znajomość i stosowanie standardów ochrony małoletnich obowiązujących w szkole; reagowanie na przemoc wobec dziecka, uruchamianie procedury „Niebieskie Karty” i zawiadamianie właściwych organów w przypadkach wymaganych prawem.", "art. 22b–22c ustawy o przeciwdziałaniu zagrożeniom przestępczością na tle seksualnym i ochronie małoletnich; art. 9d ustawy o przeciwdziałaniu przemocy domowej; art. 304 § 2 KPK"),
    w("Realizacja programu wychowawczo-profilaktycznego w ramach nauczanych przedmiotów (edukacja zdrowotna, bezpieczeństwo cyfrowe, zasady fair play, współpraca w grupie); zapobieganie zachowaniom trudnym i reagowanie na nie zgodnie z procedurami szkoły i strategiami z IPET.", "art. 26 Prawa oświatowego; IPET; procedury szkolne"),

    "VIII. Ocenianie, klasyfikacja i egzaminy",
    w("Ocenianie bieżące z nauczanych przedmiotów: stopnie w skali 1–6 w oddziałach dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim, oceny opisowe w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną oraz w klasach I–III; jawność ocen i ich uzasadnianie.", "art. 44e i art. 44i ust. 1 i 7 ustawy o systemie oświaty"),
    w("Ustalanie śródrocznych i rocznych ocen klasyfikacyjnych z języka angielskiego, informatyki i wychowania fizycznego; informowanie uczniów i rodziców o przewidywanych ocenach w terminie określonym w statucie; udział w klasyfikacji i uchwałach rady pedagogicznej o promowaniu.", "art. 44f–44o ustawy o systemie oświaty"),
    w("Udział w egzaminach klasyfikacyjnych, poprawkowych i sprawdzianach wiadomości w komisjach powołanych przez dyrektora.", "art. 44l–44n ustawy o systemie oświaty"),
    w("Wpisywanie ocen do dzienników i arkuszy ocen; jako wychowawca – wypełnianie świadectw i arkuszy ocen oddziału.", "rozporządzenie MEN w sprawie świadectw, dyplomów państwowych i innych druków; rozporządzenie w sprawie dokumentacji przebiegu nauczania"),

    "IX. Współpraca z rodzicami",
    w("Prowadzenie konsultacji dla rodziców i uczniów w terminie ustalonym w rozkładzie czasu pracy; udział w zebraniach z rodzicami; komunikacja przez dziennik elektroniczny.", "statut szkoły"),
    w("Informowanie rodziców o postępach, trudnościach i zachowaniu ucznia na lekcjach nauczanych przedmiotów; uzgadnianie form wsparcia i ćwiczeń w domu (słownictwo, aktywność ruchowa, bezpieczne korzystanie z komputera).", "art. 44e i 44g ustawy o systemie oświaty; IPET"),
    w("Zbieranie zgód rodziców wymaganych przy zawodach, wyjazdach sportowych, konkursach i publikacji prac uczniów; ich przechowywanie zgodnie z zasadami ochrony danych.", "statut szkoły; RODO"),

    "X. Praca zespołowa i współpraca z instytucjami",
    w("Udział w zebraniach rady pedagogicznej, realizacja jej uchwał; praca w zespole przedmiotowym, zespole wychowawców i zespołach zadaniowych powołanych przez dyrektora.", "art. 69–73 Prawa oświatowego (w zakresie przewidzianym statutem szkoły niepublicznej); statut szkoły"),
    w("Współpraca z klubami i związkami sportowymi, organizacjami sportu osób z niepełnosprawnością, poradnią psychologiczno-pedagogiczną oraz instytucjami wspierającymi ucznia; udział w promocji szkoły i dniach otwartych na przydział dyrektora.", "statut szkoły"),
    w("Dzielenie się wiedzą: zajęcia otwarte, lekcje koleżeńskie, wsparcie nauczyciela początkującego lub praktykanta na przydział dyrektora.", "art. 9ca Karty Nauczyciela (stosowany na podstawie art. 91b KN); statut szkoły"),

    "XI. Dokumentacja",
    w("Prowadzenie wpisów w dziennikach lekcyjnych każdego oddziału: tematy, frekwencja, oceny; prowadzenie dzienników innych zajęć przydzielonych; jako wychowawca – dokumentacji oddziału.", "art. 14 ust. 3 pkt 5 Prawa oświatowego; rozporządzenie MEN w sprawie dokumentacji przebiegu nauczania (25.08.2017 r.)"),
    w("Opracowanie planów wynikowych (rozkładów materiału) każdego przedmiotu dla każdego oddziału, przedmiotowych zasad oceniania, dostosowań wymagań dla uczniów; sprawozdania półroczne i roczne z realizacji przedmiotów i zadań przydzielonych.", "statut szkoły"),
    w("Prowadzenie dokumentacji wypadków, zawodów i wyjazdów sportowych (karty wycieczki, listy uczestników, zgody), regulaminów pracowni i sali gimnastycznej oraz ewidencji sprzętu.", "rozporządzenie w sprawie bezpieczeństwa i higieny w szkołach; rozporządzenie w sprawie krajoznawstwa i turystyki; statut szkoły"),

    "XII. Przygotowanie do zajęć i doskonalenie zawodowe",
    w("Przygotowanie lekcji, materiałów dostosowanych (karty pracy, materiały wizualne, zestawy ćwiczeń, zadania o różnym poziomie trudności), pracowni i sprzętu; sprawdzanie prac uczniów – w czasie przewidzianym na to w rozkładzie czasu pracy.", "art. 128 Kodeksu pracy; rozkład czasu pracy"),
    w("Doskonalenie zawodowe zgodnie z potrzebami szkoły: szkolenia rady pedagogicznej, kursy z dydaktyki przedmiotów dla uczniów z niepełnosprawnością intelektualną, technologii wspomagających, adaptowanej aktywności fizycznej; okresowe szkolenia z pierwszej pomocy; realizacja ścieżki awansu zawodowego. Szkolenie na polecenie pracodawcy jest czasem pracy.", "art. 6 pkt 3 i 3a oraz art. 9a–9h Karty Nauczyciela (przez art. 91b KN); art. 94¹³ Kodeksu pracy"),
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
        new Paragraph({ spacing: { after: 0 }, children: [run("nauczyciela języka angielskiego, informatyki i wychowania fizycznego w szkole specjalnej · rok szkolny " + ROK, { size: 19, color: POMARANCZ })] }),
      ] }),
    ] })],
  });

  const dane = tabela(null, [
    ["Imię i nazwisko", nazwisko],
    ["Stanowisko", "nauczyciel przedmiotów w szkole podstawowej specjalnej: język angielski, informatyka, wychowanie fizyczne"],
    ["Nauczane przedmioty i klasy", "język angielski: klasy ………   informatyka: klasy ………   wychowanie fizyczne: klasy ………   (oddziały dla uczniów z niepełnosprawnością intelektualną w stopniu lekkim; w oddziałach dla uczniów z niepełnosprawnością umiarkowaną lub znaczną – wychowanie fizyczne oraz elementy technologii informacyjnej w zajęciach rozwijających kreatywność i komunikowanie się)"],
    ["Podstawa zatrudnienia", "umowa o pracę – Kodeks pracy; z Karty Nauczyciela stosuje się przepisy wskazane w art. 91b ust. 2 (m.in. art. 6, art. 9–9i, art. 75–85z)"],
    ["Wymiar i rozkład czasu pracy", "30 godzin tygodniowo (6 godzin dziennie od poniedziałku do piątku) według rozkładu czasu pracy ustalonego przez dyrektora; w tym czasie: lekcje według planu, dyżury, dokumentacja, zebrania, konsultacje, przygotowanie zajęć i pracowni; 15-minutowa przerwa wliczana do czasu pracy (art. 134 KP)"],
    ["Bezpośredni przełożony", "dyrektor szkoły"],
    ["Wychowawstwo / pracownie", "wychowawstwo oddziału: ………………   ☐ TAK   ☐ NIE      opieka nad pracownią komputerową:  ☐ TAK   ☐ NIE      opieka nad salą gimnastyczną i sprzętem sportowym:  ☐ TAK   ☐ NIE"],
    ["Zastępstwo w czasie nieobecności", "…………………………………………………………………………"],
    ["Wymagane kwalifikacje", "kwalifikacje do nauczania każdego z przedmiotów (język angielski, informatyka, wychowanie fizyczne) oraz z zakresu pedagogiki specjalnej odpowiedniej do niepełnosprawności uczniów (rozporządzenie MEN z 1.08.2017 r.); szkolenie BHP i z pierwszej pomocy (obowiązkowe dla prowadzących wychowanie fizyczne); aktualne orzeczenie lekarskie o braku przeciwwskazań; niekaralność sprawdzona w Rejestrze Sprawców Przestępstw na Tle Seksualnym (art. 21 ustawy o ochronie małoletnich) oraz w KRK; kwalifikacje jak dla szkół publicznych (art. 14 ust. 3 pkt 6 Prawa oświatowego)"],
  ], [3000, 7160], { boldCol: 0 });

  const indyw = tabela(["Lp.", "Czynność przydzielona indywidualnie", "Termin / wymiar", "Uwagi"],
    [1, 2, 3, 4, 5].map((i) => [String(i), "", "", ""]), [480, 5480, 2100, 2100]);

  const odpow = tabela(["Zakres odpowiedzialności", "Podstawa"], [
    ["Za życie, zdrowie i bezpieczeństwo uczniów powierzonych opiece w czasie zajęć i czynności organizowanych przez szkołę.", "art. 6 pkt 1 KN; rozporządzenie w sprawie bezpieczeństwa i higieny w szkołach"],
    ["Za realizację podstawy programowej, IPET i zaleceń orzeczeń oraz za rzetelność oceniania.", "przepisy oświatowe wskazane w tabeli obowiązków"],
    ["Za prawidłowe i terminowe prowadzenie dokumentacji oraz ochronę danych osobowych.", "rozporządzenie w sprawie dokumentacji przebiegu nauczania; RODO"],
    ["Za stan i bezpieczne używanie sprzętu w pracowni komputerowej, sali gimnastycznej i na boisku w czasie prowadzonych zajęć oraz za mienie powierzone na piśmie.", "§ 31 rozporządzenia w sprawie bezpieczeństwa i higieny w szkołach; art. 124 Kodeksu pracy"],
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
    new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 60, line: 260 }, children: [run("Potwierdzam zapoznanie się z zakresem czynności i obowiązków, przyjmuję go do wiadomości i stosowania oraz zobowiązuję się do wykonywania pracy zgodnie z nim, regulaminem pracy, statutem szkoły i obowiązującymi przepisami. Zakres czynności sporządzono w dwóch jednobrzmiących egzemplarzach: jeden dla pracownika, drugi do akt osobowych (część B).", { size: 18 })] }),
    new Paragraph({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 0, line: 260 }, children: [run("Zakres czynności stanowi uszczegółowienie rodzaju pracy określonego w umowie o pracę (art. 29 § 1 i art. 94 pkt 1 Kodeksu pracy). Zmiana zakresu w granicach umówionego rodzaju pracy nie wymaga wypowiedzenia zmieniającego.", { size: 17, color: SZARY })] }),
    podpisy,
  ];
}

// ---------- dokument ----------
const logo = fs.readFileSync(LOGO);
const naglowek = new Header({ children: [new Paragraph({
  tabStops: [{ type: TabStopType.RIGHT, position: SZER }], border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: FIOLET, space: 4 } }, spacing: { after: 160 },
  children: [new ImageRun({ type: "png", data: logo, transformation: { width: 22, height: 22 } }), run("   " + PLACOWKA, { size: 15, color: SZARY }), run("\tZakres czynności – język angielski, informatyka, wychowanie fizyczne – " + ROK, { size: 15, color: FIOLET })],
})] });
const stopka = new Footer({ children: [new Paragraph({
  alignment: AlignmentType.CENTER, spacing: { before: 80 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: POMARANCZ, space: 4 } },
  children: [run("Strona ", { size: 15, color: SZARY }), new TextRun({ children: [PageNumber.CURRENT], font: F, size: 15, color: SZARY }), run("   •   zatrudnienie na podstawie Kodeksu pracy, 30 godzin tygodniowo   •   stan prawny: wrzesień 2026 r.", { size: 15, color: SZARY })],
})] });

const children = [];
NAUCZYCIELE.forEach((n, i) => children.push(...egzemplarz(n, logo, i === 0)));

const doc = new Document({
  creator: PLACOWKA, title: "Zakres czynności nauczyciela języka angielskiego, informatyki i wychowania fizycznego " + ROK,
  styles: { default: { document: { run: { font: F, size: 18 } } } },
  sections: [{ properties: { page: { margin: { top: 900, bottom: 850, left: 1000, right: 1000 } } }, headers: { default: naglowek }, footers: { default: stopka }, children }],
});
Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(OUT, buf); console.log("zapisano", OUT, buf.length, "B", "egzemplarze:", NAUCZYCIELE.join(", ")); });
