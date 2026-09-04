const G = require('./gen.js');
const { Paragraph, AlignmentType, BorderStyle, t, p, H1, H2, H3, bullet, numItem, spacer,
        pageBreak, box, table, tableIn, modul, straznik, cw, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));

add(pageBreak());

/* ============ M2 ICF ============ */
add(modul('M2', 'ICF — czym jest i dlaczego stał się językiem dokumentacji', '45 min',
  'zrozumieć zmianę paradygmatu i nauczyć się opisywać dziecko funkcjonalnie'));
add(spacer(120));

add(H2('2.1  Czym jest ICF — definicja, którą podajemy radzie'));
add(p([t('ICF ', { bold: true }), t('(ang. International Classification of Functioning, Disability and Health; pol. '), t('Międzynarodowa Klasyfikacja Funkcjonowania, Niepełnosprawności i Zdrowia', { bold: true }), t(') to klasyfikacja przyjęta przez Światową Organizację Zdrowia (WHO) w 2001 r., należąca — obok ICD, klasyfikacji chorób — do tak zwanej rodziny klasyfikacji WHO. Dla dzieci i młodzieży opracowano wersję rozszerzoną ')  , t('ICF-CY', { bold: true }), t(' (Children and Youth, 2007), uwzględniającą zmienność rozwojową i rolę środowiska wychowawczego.')]));
add(p([t('Jedno zdanie do zapamiętania: ', { bold: true, color: ORANGE }), t('ICD odpowiada na pytanie „co dziecku dolega”, ICF odpowiada na pytanie „jak dziecko funkcjonuje w swoim środowisku”. Dokumentacja przedszkolna odpowiada wyłącznie na to drugie pytanie.')]));

add(spacer(120));
add(H2('2.2  Zmiana paradygmatu — dlaczego to nie jest kosmetyka'));
add(table(['Kryterium', 'Model biomedyczny (dotychczasowy nawyk)', 'Model biopsychospołeczny (ICF)'], [
  ['Pytanie wyjściowe', 'Co jest z dzieckiem nie tak?', 'Co dziecko robi, w jakich warunkach i czego potrzebuje, żeby uczestniczyć?'],
  ['Źródło trudności', 'W dziecku — deficyt, zaburzenie, brak.', 'W relacji między możliwościami dziecka a wymaganiami i zasobami środowiska.'],
  ['Rola przedszkola', 'Wskazać objawy i odesłać do specjalisty.', 'Opisać funkcjonowanie, usunąć bariery, wzmocnić ułatwienia — i dopiero wtedy, z danymi, odesłać.'],
  ['Zapis w dokumencie', '„Chłopiec nie potrafi się skupić, przeszkadza w zajęciach.”', '„W zajęciach grupowych przy stoliku utrzymuje uwagę ok. 4 minut; przy zadaniu ruchowym w małej grupie — ok. 12 minut. Skupienie wydłuża się przy uprzedzeniu o zmianie i pracy w parze (ułatwienie); skraca przy hałasie w sali (bariera).”'],
  ['Co z tego wynika', 'Nic, co nauczyciel może zrobić jutro.', 'Konkretne dostosowanie, mierzalny cel i wskaźnik do ewaluacji.'],
], [1500, 2900, CONTENT - 1500 - 2900], { boldCol0: true }));

add(spacer(160));
add(H2('2.3  Budowa klasyfikacji — pięć elementów, które wystarczy znać'));
add(p('Nauczyciel przedszkola nie koduje w ICF. Musi natomiast rozumieć jego strukturę, żeby czytać dokumenty z poradni i pisać własne tym samym językiem.'));
add(spacer(80));
add(table(['Symbol', 'Komponent', 'Co opisuje', 'Przykład z przedszkola'], [
  ['b', 'Funkcje ciała', 'Funkcje fizjologiczne i psychiczne organizmu.', 'b140 funkcje uwagi, b167 funkcje językowe, b235 funkcje przedsionkowe.'],
  ['s', 'Struktury ciała', 'Anatomiczne części ciała.', 's260 struktura ucha wewnętrznego.'],
  ['d', 'Aktywność i uczestniczenie', 'Wykonywanie zadań oraz angażowanie się w sytuacje życiowe. To jest domena przedszkola.', 'd160 skupianie uwagi, d330 mówienie, d550 jedzenie, d710 podstawowe kontakty międzyludzkie.'],
  ['e', 'Czynniki środowiskowe', 'Fizyczne, społeczne i postawy otoczenia — działające jako BARIERY albo UŁATWIENIA.', 'e310 najbliższa rodzina, e330 osoby na stanowiskach władzy (nauczyciel), e250 dźwięk (hałas w szatni), e125 produkty wspomagające komunikację (AAC).'],
  ['—', 'Czynniki osobowe', 'Wiek, temperament, doświadczenia. W ICF nieklasyfikowane, ale opisywane.', 'Dziecko dwujęzyczne, po długiej hospitalizacji, najmłodsze w grupie.'],
], [800, 2000, 3000, CONTENT - 800 - 2000 - 3000], { boldCol0: true }));

add(spacer(160));
add(box('CZYNNIKI ŚRODOWISKOWE — NAJCZĘŚCIEJ POMIJANY ELEMENT', [
  p('W dokumentacji przedszkolnej komponent „e” bywa pomijany zupełnie, a to on niesie największą wartość praktyczną. Jeżeli zapiszemy, że hałas w sali jest barierą, a zapowiedź zmiany aktywności — ułatwieniem, to mamy gotową treść dostosowania w IPET. Opis samych trudności dziecka nie generuje żadnego działania; opis barier i ułatwień generuje je natychmiast. Prowadzący prosi zespół, by przy każdym omawianym dziecku wskazał minimum jedną barierę i jedno ułatwienie po stronie środowiska.'),
], { fill: LIGHTO, bar: ORANGE }));

add(pageBreak());
add(H2('2.4  Dziewięć obszarów „d” — mapa, na której zbudowano KPOF'));
add(p('Arkusze KPOF są zorganizowane dokładnie według dziewięciu rozdziałów komponentu „Aktywność i uczestniczenie”. Dzięki temu wynik z arkusza przekłada się wprost na język WOPF i na język poradni.'));
add(spacer(80));
add(table(['Kod', 'Obszar ICF', 'Co obserwujemy w przedszkolu', 'Przykładowe kody szczegółowe'], [
  ['d1', 'Uczenie się i stosowanie wiedzy', 'Patrzenie i słuchanie, naśladowanie, uwaga, porównywanie i sortowanie, rozwiązywanie problemów.', 'd110–d115, d130, d137, d160, d175'],
  ['d2', 'Ogólne zadania i wymagania', 'Podejmowanie i kończenie zadania, rytm dnia, zasady, radzenie sobie ze stresem i zmianą.', 'd210, d220, d230, d240'],
  ['d3', 'Porozumiewanie się', 'Rozumienie poleceń, komunikaty werbalne i pozawerbalne, mówienie, rozmowa, AAC.', 'd310, d315, d330, d335, d350'],
  ['d4', 'Poruszanie się', 'Motoryka duża i mała, zmiana pozycji, chwyt, manipulowanie, koordynacja.', 'd410, d440, d445, d450, d455'],
  ['d5', 'Dbanie o siebie', 'Ubieranie, jedzenie, toaleta, higiena, sygnalizowanie potrzeb, dbałość o zdrowie.', 'd510, d520, d530, d540, d550, d570'],
  ['d6', 'Życie domowe', 'Czynności użyteczne: porządkowanie, drobne prace, dbanie o przedmioty. W KPOF obszar OPISOWY.', 'd630, d640, d650'],
  ['d7', 'Wzajemne kontakty i związki międzyludzkie', 'Kontakt z dorosłym i rówieśnikiem, współdziałanie, konflikt, przyjaźń.', 'd710, d720, d730, d750'],
  ['d8', 'Główne obszary życia', 'Dla przedszkolaka: edukacja przedszkolna i zabawa — zabawa tematyczna, konstrukcyjna, udział w zajęciach.', 'd815, d820, d880'],
  ['d9', 'Życie społeczne, lokalne i obywatelskie', 'Uroczystości, spacery i wyjścia, zabawa na powietrzu, odbiór kultury.', 'd910, d920, d9202'],
], [700, 2500, 3400, CONTENT - 700 - 2500 - 3400], { boldCol0: true }));

add(spacer(150));
add(box('DWIE RAMY, KTÓRYCH NIE WOLNO POMYLIĆ', [
  p([t('Obszary arkusza d1–d9 (ICF) i obszary nowej podstawy programowej 1–9 (społeczny, osobisty, językowy, matematyczny, przyrodniczy, techniczny, cyfrowy, artystyczny, ruchowy) to ')  , t('dwie różne ramy', { bold: true }), t('. Zbieżność liczby dziewięć jest przypadkowa. W kolumnie „ICF · PP” arkusza KPOF zapis przed kropką odsyła do ICF, zapis po skrócie „PP” — do podstawy programowej. Prowadzący musi to powiedzieć wprost, bo jest to najczęstsze nieporozumienie przy pierwszym kontakcie z arkuszem.')]),
], { fill: LIGHT, bar: PURPLE }));

add(spacer(150));
add(H2('2.5  Kwalifikatory ICF a skala KPOF — dlaczego liczby idą w przeciwną stronę'));
add(p([t('W oryginalnej klasyfikacji ICF stosuje się kwalifikator nasilenia problemu w skali od 0 do 4, gdzie 0 oznacza brak trudności, a 4 — trudność skrajną (dodatkowo 8 — nieokreślona, 9 — nie dotyczy). Skala rosnąca opisuje zatem rosnący ')  , t('problem', { bold: true }), t('.')]));
add(p([t('KPOF świadomie odwraca ten kierunek: 1 oznacza poważną trudność, a 5 — samodzielne i pewne wykonywanie czynności. Powód jest metodyczny, nie techniczny: ')  , t('narzędzie ma opisywać zasoby, a nie stopień uszkodzenia', { bold: true }), t('. Wysoki wynik to mocna strona dziecka, którą wykorzystujemy jako dźwignię przy budowaniu celów. Ta różnica musi paść na szkoleniu, bo zespół czytający równolegle dokument z poradni (skala 0–4 rosnąca) i własny arkusz (skala 1–5 malejąca) bez tego wyjaśnienia wyciągnie wnioski odwrotne do prawdziwych.')]));

add(spacer(160));
add(cw('PRZEKŁAD NA JĘZYK FUNKCJONALNY  ·  15 min  ·  pary', [
  p('Prowadzący rozdaje listę zdań zapisanych językiem potocznym lub deficytowym. Zadaniem par jest przepisanie każdego zdania tak, by zawierało: (a) obserwowalne zachowanie, (b) sytuację, w której występuje, (c) poziom wsparcia, (d) barierę lub ułatwienie po stronie środowiska.'),
]));
add(spacer(100));
add(table(['Zapis do poprawy', 'Poprawny zapis funkcjonalny (klucz dla prowadzącego)'], [
    ['Dziecko jest niesamodzielne.', 'W szatni zakłada samodzielnie spodnie i buty na rzepy; przy zapięciach guzikowych i suwaku potrzebuje rozpoczęcia czynności przez dorosłego. Samodzielność rośnie, gdy ubiera się przy własnym oznaczonym miejscu (ułatwienie), maleje przy pośpiechu całej grupy (bariera).'],
    ['Nie mówi.', 'Nie buduje zdań; komunikuje potrzeby gestem, wokalizacją i podaniem przedmiotu, konsekwentnie i czytelnie dla znanych dorosłych. Rozumie proste polecenia indywidualne. Wskazana próba wprowadzenia wsparcia komunikacji obrazkowej (AAC).'],
    ['Jest agresywny.', 'W sytuacjach oczekiwania w kolejce i odbierania zabawki uderza rówieśnika otwartą dłonią — w ostatnich dwóch tygodniach pięć zdarzeń, wszystkie przed obiadem. Nie występuje w zabawie swobodnej na powietrzu ani w małej grupie z dorosłym.'],
    ['Ma problemy sensoryczne.', 'Zakrywa uszy i wychodzi z sali przy odkurzaczu i głośnej muzyce; odmawia potraw o konsystencji papkowatej; poszukuje intensywnego ruchu — wielokrotnie wspina się i zeskakuje. Wymaga pogłębionej obserwacji sensorycznej i konsultacji specjalisty.'],
    ['Nie bawi się z dziećmi.', 'Bawi się obok rówieśników, obserwuje ich zabawę, nie podejmuje wspólnej roli. Nawiązuje kontakt, gdy dorosły wprowadza go do zabawy w parze i nadaje mu konkretne zadanie. W zabawie tematycznej nie przyjmuje roli „na niby”.'],
], [3200, CONTENT - 3200]));
add(spacer(120));
add(box('PODSUMOWANIE PROWADZĄCEGO', [
  p('Każdy poprawiony zapis nadaje się do wklejenia do WOPF i do informacji dla poradni. Każdy zapis z lewej kolumny nadaje się wyłącznie do wyrzucenia. Różnica między nimi to jest cała reforma dokumentacji w jednym zdaniu.'),
], { fill: LIGHT, bar: PURPLE }));

add(pageBreak());

/* ============ M3 METRYCZKA ============ */
add(modul('M3', 'Metryczka dziecka — pierwszy dokument września', '25 min',
  'uzasadnić metryczkę i przećwiczyć jej wypełnienie bez zbierania danych nadmiarowych'));
add(spacer(120));

add(H2('3.1  Zasadność — po co nam metryczka?'));
add(p('Metryczka nie jest dokumentem, który ktoś od nas wymaga z nazwy. Jest dokumentem, który wymyśliliśmy sobie sami, żeby przestać tracić czas. Uzasadnienie podajemy radzie w pięciu punktach — i w tej kolejności.'));
add(spacer(60));
add(table(['#', 'Argument', 'Na czym polega'], [
  ['1', 'Jedno miejsce zamiast siedmiu',
   'Dane dziecka i rodziców, upoważnienia do odbioru, kontakty alarmowe, informacje o zdrowiu i wykaz dokumentacji wsparcia znajdują się fizycznie w jednym dokumencie. Nauczyciel na zastępstwie nie szuka po segregatorach.'],
  ['2', 'Bezpieczeństwo dziecka tu i teraz',
   'Sekcje IV (osoby upoważnione), V (kontakt w nagłych wypadkach) i VI (zdrowie, alergie, leki, procedury postępowania) to jedyne informacje, które muszą być dostępne w ciągu kilkunastu sekund. Metryczka jest dokumentem operacyjnym, nie archiwalnym.'],
  ['3', 'Punkt wyjścia dla pomocy psychologiczno-pedagogicznej',
   'Sekcja VII (objęcie wsparciem i dokumentacja specjalna) daje natychmiastową odpowiedź na pytanie, czy dziecko ma orzeczenie, opinię, WWRD, IPET — od kiedy i na jakiej podstawie (rodzaj niepełnosprawności, schorzenie). To ta informacja uruchamia zegar 30 dni na opracowanie IPET.'],
  ['4', 'Ślad współpracy z rodzicem',
   'Sekcja XI (rejestr kontaktów i ustaleń) jest dowodem, że przedszkole informowało, konsultowało i ustalało. W sytuacji spornej to jedyny dokument, który to potwierdza.'],
  ['5', 'Zgodność z RODO',
   'Klauzula informacyjna z art. 13 RODO wraz z podpisem rodzica jest wpisana w dokument. Nie krąży osobną kartką, która ginie.'],
], [500, 2600, CONTENT - 500 - 2600], { boldCol0: true }));

add(spacer(160));
add(H2('3.2  Trzy błędy, które popełniamy przy metryczce'));
add(bullet([t('Zbieramy dane, których nie potrzebujemy. ', { bold: true }), t('Zasada minimalizacji z RODO obowiązuje także nas. Jeżeli nie umiemy powiedzieć, do jakiego zadania przedszkola potrzebujemy danej informacji, nie wpisujemy jej do druku. Dlatego w metryczce nie wpisujemy numeru PESEL — jest już w księdze dzieci i nie powielamy go w kolejnym dokumencie. Wpisujemy natomiast to, co wpływa na funkcjonowanie dziecka w placówce: datę urodzenia, imiona i nazwiska rodziców z kontaktem, podstawę wydania orzeczenia (rodzaj niepełnosprawności, schorzenie), choroby przewlekłe i ostrzeżenia z nimi związane (np. astma, cukrzyca) oraz przyjmowane leki.')]));
add(bullet([t('Wypełniamy raz we wrześniu i nie aktualizujemy. ', { bold: true }), t('Numer telefonu i lista osób upoważnionych zmieniają się w ciągu roku. Ustalamy zasadę: aktualizacja przy każdej zmianie zgłoszonej przez rodzica, z datą; poprzedni wpis zostaje w dokumentacji z datą wykreślenia — tak, jak przewiduje to sam druk.')]));
add(bullet([t('Trzymamy metryczkę tam, gdzie sięgnie każdy. ', { bold: true }), t('Dokument zawiera dane o zdrowiu — kategoria szczególna z art. 9 RODO. Miejsce przechowywania i osobę odpowiedzialną wskazuje zarządzenie dyrektora.')]));

add(spacer(160));
add(cw('METRYCZKA W 12 MINUT  ·  praca indywidualna + omówienie', [
  p([t('Zadanie: ', { bold: true }), t('każdy nauczyciel wypełnia metryczkę dla jednego dziecka ze swojej grupy — sekcje I, II, VI i VII. Sekcje III–V wypełnia się z rodzicem, więc na szkoleniu tylko je omawiamy.')]),
  p([t('Kontrola: ', { bold: true }), t('po wypełnieniu każdy zamienia się arkuszem z sąsiadem i sprawdza dwie rzeczy — czy w sekcji VI jest napisane nie tylko CO dziecku dolega, ale też CO ROBI NAUCZYCIEL w sytuacji nagłej, oraz czy w sekcji VII wpisano daty dokumentów, a nie samo „tak”.')]),
  p([t('Najczęstszy błąd do wychwycenia: ', { bold: true }), t('w rubryce „zalecenia dotyczące postępowania” pojawia się „zgodnie z zaleceniami lekarza”. To zapis pusty. Musi być napisane: kto podaje lek, na jakiej podstawie (zaświadczenie lekarskie i pisemna zgoda rodziców), gdzie lek jest przechowywany i kogo powiadamiamy w jakiej kolejności.')]),
]));

module.exports = C;
