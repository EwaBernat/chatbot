const G = require('./gen.js');
const { Paragraph, AlignmentType, BorderStyle, t, p, H1, H2, H3, bullet, numItem, spacer,
        pageBreak, box, table, tableIn, modul, straznik, cw, CONTENT, PURPLE, ORANGE, LIGHT, LIGHTO } = G;

const C = [];
const add = (...x) => x.forEach(e => C.push(e));

add(pageBreak());

/* ============ M4 KPOF BUDOWA ============ */
add(modul('M4', 'KPOF — budowa narzędzia, skala i siedem zasad obserwacji', '35 min',
  'przygotować zespół do samodzielnego, rzetelnego wypełnienia arkusza'));
add(spacer(120));

add(H2('4.1  Czym jest KPOF i czym nie jest'));
add(p([t('KPOF — ', { bold: true }), t('Kwestionariusz Przedszkolnej Oceny Funkcjonalnej', { bold: true }), t(' — to autorskie narzędzie kryterialne, zbudowane na nowej podstawie programowej wychowania przedszkolnego i na klasyfikacji ICF. Opisuje funkcjonowanie dziecka w dziewięciu obszarach ICF (d1–d9) w codziennych sytuacjach przedszkolnych i domowych.')]));
add(spacer(60));
add(H3('Co KPOF robi / czego KPOF nie robi'));
add(table(['KPOF JEST', 'KPOF NIE JEST'], [
    ['Uporządkowanym zapisem obserwacji nauczyciela, rodzica i specjalisty.', 'Diagnozą — nie zastępuje badania psychologicznego, logopedycznego ani lekarskiego.'],
    ['Narzędziem kryterialnym: porównujemy dziecko z oczekiwaniami rozwojowymi dla wieku.', 'Testem normalizowanym — nie ma norm centylowych ani ilorazów.'],
    ['Punktem wyjścia do decyzji zespołu: obserwować dalej, wesprzeć w przedszkolu, czy skierować do poradni.', 'Podstawą do postawienia dziecku etykiety ani do rozmowy z rodzicem o „podejrzeniu” czegokolwiek.'],
    ['Materiałem źródłowym do WOPF i do informacji o funkcjonowaniu dziecka dla poradni.', 'Dokumentem, który wysyłamy do poradni w oryginale zamiast informacji o funkcjonowaniu.'],
], [4680, 4680]));

add(spacer(150));
add(H2('4.2  Trzy wersje arkusza'));
add(table(['Wersja', 'Wiek', 'Liczba twierdzeń', 'Kiedy stosujemy'], [
  ['A', '3–4 lata', '42', 'Grupy najmłodsze. Pierwsze wypełnienie po zakończeniu okresu adaptacji, nie wcześniej niż w październiku.'],
  ['B', '5 lat', '44', 'Grupy pięciolatków. Wrzesień / październik.'],
  ['C', '6 lat', '44', 'Roczne przygotowanie przedszkolne. Wrzesień/październik — wynik zasila także informację o gotowości szkolnej.'],
], [1100, 1400, 1900, CONTENT - 1100 - 1400 - 1900], { boldCol0: true }));
add(spacer(80));
add(p([t('Zasada doboru: ', { bold: true }), t('decyduje wiek rozwojowy i sytuacja dziecka, nie sama metryka. Dziecko sześcioletnie z głęboką niepełnosprawnością sprzężoną obserwujemy wersją A — bo wersja C nie da nam żadnej użytecznej informacji poza serią jedynek. Wybór wersji odnotowujemy w arkuszu i uzasadniamy jednym zdaniem.')]));

add(spacer(150));
add(H2('4.3  Skala — sześć wartości, jedno zaznaczenie'));
add(table(['Ocena', 'Znaczenie', 'Kryterium rozstrzygające'], [
  ['1', 'Występuje w niewielkim stopniu — poważna trudność', 'Zachowanie nie pojawia się wcale lub szczątkowo, nawet przy pełnym wsparciu i modelowaniu.'],
  ['2', 'Rzadko / tylko z dużym wsparciem', 'Pojawia się sporadycznie i wyłącznie przy stałej, aktywnej pomocy dorosłego — prowadzeniu krok po kroku.'],
  ['3', 'Niesystematycznie / z częściowym wsparciem', 'Raz się udaje, raz nie; wymaga przypomnień, podpowiedzi słownej lub rozpoczęcia przez dorosłego. Umiejętność w trakcie kształtowania.'],
  ['4', 'Zwykle samodzielnie', 'W typowych sytuacjach dziecko radzi sobie bez pomocy; potknięcia tylko w sytuacjach nowych, trudnych lub przy zmęczeniu.'],
  ['5', 'Samodzielnie i pewnie', 'Zachowanie samodzielne, pewne i powtarzalne, także w sytuacjach nowych. Mocna strona — zasób do wykorzystania w celach.'],
  ['N', 'Brak możliwości obserwacji — pozycja pusta', 'Nie było okazji zaobserwować. N jest pełnoprawną odpowiedzią. NIE ZGADUJEMY. N nie obniża wyniku — twierdzeń z N nie wlicza się do średniej.'],
], [900, 2700, CONTENT - 900 - 2700], { boldCol0: true }));

add(spacer(140));
add(box('DLACZEGO „N” JEST NAJWAŻNIEJSZĄ OCENĄ W ARKUSZU', [
  p('Rodzic nie widzi dziecka podczas zajęć grupowych. Nauczyciel nie widzi dziecka przy porannym ubieraniu w domu. Każda ocena postawiona „na wyczucie” zamiast N zanieczyszcza wynik i może przesunąć dziecko o cały poziom wsparcia. Prowadzący powinien wprost powiedzieć zespołowi: postawienie dwudziestu N przez rodzica nie jest porażką narzędzia — jest informacją, których sytuacji rodzic nie obserwuje, i to też jest dana diagnostyczna.'),
], { fill: LIGHTO, bar: ORANGE }));

add(pageBreak());
add(H2('4.4  Siedem zasad rzetelnej obserwacji'));
add(p('Zasady są wydrukowane na ostatniej stronie każdego arkusza. Prowadzący omawia je po kolei, przy każdej pytając: „co się stanie, jeśli tej zasady nie dochowamy?”.'));
add(spacer(60));
add(table(['#', 'Zasada', 'Konsekwencja złamania'], [
  ['1', 'Wypełnij CAŁY arkusz — wszystkie obszary I–IX. Obszarów nie dzielimy między oceniających; każdy ocenia wszystko ze swojej perspektywy.',
   'Podzielony arkusz uniemożliwia porównanie perspektyw — tracimy najcenniejszą informację, czyli różnicę między domem a przedszkolem.'],
  ['2', 'Oceniaj na podstawie 2–4 tygodni obserwacji w codziennych sytuacjach — nie „z pamięci” i nie na podstawie jednego dnia.',
   'Ocena z jednego trudnego dnia zaniża profil; ocena z jednego udanego dnia go zawyża. Obie prowadzą do złej decyzji.'],
  ['3', 'Wypełniaj samodzielnie i niezależnie — nie konsultuj ocen z innymi przed spotkaniem zespołu.',
   'Uzgodnione wcześniej oceny dają jeden, uśredniony obraz zamiast trzech niezależnych perspektyw. Znika triangulacja.'],
  ['4', 'Oceniaj to, co dziecko ROBI, a nie to, co potrafiłoby „gdyby chciało”.',
   'Ocena potencjału zamiast zachowania to najczęstsza przyczyna zawyżonych wyników i spóźnionego wsparcia.'],
  ['5', 'Odnoś się do oczekiwań rozwojowych dla WIEKU dziecka — nie do dorosłego wzorca ani do rodzeństwa.',
   'Porównanie ze starszym rodzeństwem zaniża wynik; porównanie z młodszym — zawyża.'],
  ['6', 'Wpisuj obserwacje jakościowe — konkretne przykłady zachowań, zwłaszcza przy ocenach 1–2 i 5.',
   'Same liczby nie nadają się do przepisania do WOPF. Przykład zachowania — tak. Bez tego wracamy do obserwacji od nowa.'],
  ['7', 'Zwróć arkusz koordynatorowi w umówionym terminie; wyniki omawiamy wspólnie na spotkaniu zespołu z udziałem rodzica.',
   'Arkusz w szufladzie nie jest dokumentacją. Zespół bez rodzica nie jest zespołem, tylko naradą personelu.'],
], [500, 3600, CONTENT - 500 - 3600], { boldCol0: true }));

add(spacer(150));
add(H2('4.5  Triangulacja — trzy arkusze na to samo dziecko'));
add(p([t('Ten sam arkusz wypełniają niezależnie: ')  , t('nauczyciel (N), rodzic (R) i specjalista (S)', { bold: true }), t('. Na spotkaniu zespołu kładziemy trzy profile obok siebie i czytamy je równolegle. ')  , t('Ocen różnych osób nie uśrednia się mechanicznie', { bold: true }), t(' — rozbieżność nie jest błędem pomiaru, tylko informacją o tym, że dziecko funkcjonuje inaczej w różnych środowiskach.')]));
add(spacer(60));
add(table(['Wzorzec rozbieżności', 'Najczęstsza interpretacja', 'Co robimy'], [
  ['Dom wyżej niż przedszkole (R > N o ≥ 1,5 pkt)', 'Wymagania grupy, hałas, liczba bodźców, konieczność dzielenia uwagi dorosłego. Dziecko radzi sobie w warunkach jeden-na-jeden.', 'Szukamy barier środowiskowych w sali (komponent „e”), a nie kolejnych deficytów w dziecku.'],
  ['Przedszkole wyżej niż dom (N > R o ≥ 1,5 pkt)', 'Struktura i przewidywalny rytm dnia pomagają dziecku; w domu brak struktury albo inne oczekiwania.', 'Konsultacje i porady dla rodziców jako forma pomocy p-p; przenosimy do domu sprawdzone przedszkolne rutyny.'],
  ['Specjalista niżej niż nauczyciel', 'Specjalista widzi dziecko w sytuacji zadaniowej, nauczyciel — w swobodnej. Różnica dotyczy zwykle d1 i d2.', 'Sprawdzamy, czy trudność ujawnia się tylko przy zadaniu narzuconym — to informacja wprost do IPET.'],
  ['Zgodność wszystkich trzech na poziomie 1–2', 'Trudność jest stała, niezależna od środowiska.', 'Najsilniejsza przesłanka do modułu pogłębionego i do wystąpienia do poradni.'],
], [2500, 3300, CONTENT - 2500 - 3300], { boldCol0: true }));

add(pageBreak());

/* ============ M5 KPOF WARSZTAT ============ */
add(modul('M5', 'KPOF w praktyce — liczenie wyniku, odczyt profilu, kwalifikacja', '35 min',
  'nauczyć zespół policzyć wynik i podjąć na jego podstawie decyzję'));
add(spacer(120));

add(H2('5.1  Jak liczymy — trzy działania i jeden wyjątek'));
add(numItem([t('Średnia obszaru ', { bold: true }), t('= suma punktów w obszarze ÷ liczba twierdzeń ocenionych, ')  , t('bez pozycji oznaczonych N', { bold: true }), t('. Przykład: w obszarze III z pięciu twierdzeń oceniono cztery (jedno N), suma 11 pkt → 11 ÷ 4 = 2,75.')]));
add(numItem([t('Wynik ogólny ', { bold: true }), t('= średnia ze średnich obszarów. Nie liczymy go z sumy wszystkich punktów — obszary mają różną liczbę twierdzeń i taka suma zniekształciłaby profil.')]));
add(numItem([t('Wyjątek: ', { bold: true }), t('obszar VI (życie domowe, czynności użyteczne) ma charakter ')  , t('opisowy i nie wlicza się do wyniku ogólnego', { bold: true }), t(' — przedszkole obserwuje go w ograniczonym zakresie, więc jego uwzględnienie zaburzyłoby porównywalność.')]));
add(numItem([t('Kwalifikację odczytujemy z progów ', { bold: true }), t('— osobno dla każdego obszaru i osobno dla wyniku ogólnego.')]));

add(spacer(140));
add(H2('5.2  Progi kryterialne'));
add(table(['Średnia', 'Kwalifikacja', 'Działanie · poziom wsparcia'], [
  ['4,0 – 5,0', 'ZASÓB', 'Funkcjonowanie zgodne lub powyżej oczekiwań dla wieku — mocna strona. Wykorzystujemy jako dźwignię przy formułowaniu celów w słabszych obszarach.'],
  ['3,0 – 3,9', 'POZIOM I', 'W granicach oczekiwań — bieżąca praca wychowawczo-dydaktyczna i monitorowanie. Bez dodatkowej dokumentacji.'],
  ['2,0 – 2,9', 'POZIOM II', 'Trudność — działania wspierające w przedszkolu (pomoc p-p w trakcie bieżącej pracy i w formach zajęć) oraz moduł pogłębiający.'],
  ['poniżej 2,0', 'POZIOM III', 'Nasilona trudność — moduły pogłębiające, WOPF i konsultacja z poradnią psychologiczno-pedagogiczną.'],
], [1400, 1700, CONTENT - 1400 - 1700], { boldCol0: true }));

add(spacer(140));
add(box('REGUŁA NADRZĘDNA — NAJWAŻNIEJSZE ZDANIE CAŁEGO NARZĘDZIA', [
  p([t('Każde pojedyncze twierdzenie ocenione na 1 lub 2 — niezależnie od średniej obszaru — podlega analizie jakościowej zespołu i sprawdzeniu według reguł przekierowania do modułów pogłębiających.', { bold: true })]),
  p('Dziecko może mieć w obszarze III średnią 3,8 (Poziom I, „w normie”) i jednocześnie jedynkę przy twierdzeniu o komunikowaniu potrzeb. Średnia to zamaskuje. Reguła nadrzędna nie pozwala tego przeoczyć. Prowadzący powinien zatrzymać się na tym punkcie dłużej niż na jakimkolwiek innym w całym module — bo to jest miejsce, w którym narzędzie ratuje dziecko przed przeoczeniem.'),
], { fill: LIGHTO, bar: ORANGE }));

add(spacer(140));
add(H2('5.3  Odczyt profilu — wykres słupkowy i mapa radarowa'));
add(p('Wykres nie jest ozdobą. Jest jedynym miejscem, w którym w ciągu pięciu sekund widać kształt funkcjonowania dziecka. Czytamy go w trzech krokach:'));
add(bullet([t('Krok 1 — kolor. ', { bold: true }), t('Zielony: 4–5 (zasób) oraz 3–3,9 (Poziom I). Żółty: 2–2,9 (Poziom II). Czerwony: poniżej 2 (Poziom III).')]));
add(bullet([t('Krok 2 — kształt. ', { bold: true }), t('Profil płaski i niski oznacza globalne opóźnienie rozwoju — kierunek: poradnia. Profil poszarpany, z jednym–dwoma głębokimi wcięciami przy wysokiej reszcie, oznacza trudność wybiórczą — kierunek: konkretny moduł pogłębiony.')]));
add(bullet([t('Krok 3 — pojedyncze punkty. ', { bold: true }), t('Dopiero teraz wracamy do twierdzeń ocenionych na 1–2, także w obszarach zielonych (reguła nadrzędna).')]));

add(spacer(150));
add(cw('POLICZ I ZDECYDUJ  ·  20 min  ·  zespoły 3-osobowe', [
  p([t('Materiał: ', { bold: true }), t('prowadzący rozdaje trzy komplety wypełnionych arkuszy KPOF (kazusy A, B, C — przygotowane wcześniej, dane fikcyjne), po jednym komplecie na zespół. Każdy komplet zawiera arkusz nauczyciela i arkusz rodzica.')]),
  p([t('Zadanie w czterech krokach: ', { bold: true }), t('(1) policzyć średnie dziewięciu obszarów, pamiętając o pominięciu N i o wyłączeniu obszaru VI z wyniku ogólnego; (2) nanieść wynik na wykres; (3) porównać profil nauczyciela z profilem rodzica i nazwać rozbieżność; (4) sformułować jedno zdanie wniosku zespołu i wskazać poziom wsparcia.')]),
  p([t('Kazus A — profil poszarpany: ', { bold: true }), t('d1, d2, d4, d8 w granicach 3,4–4,2; d3 = 2,0; d7 = 1,8. Oczekiwany wniosek: trudność wybiórcza w komunikowaniu się i relacjach przy zachowanych zasobach poznawczych i ruchowych → moduł ToM, konsultacja logopedyczna, Poziom III w d7.')]),
  p([t('Kazus B — profil płaski i niski: ', { bold: true }), t('wszystkie obszary 1,8–2,4. Oczekiwany wniosek: trudność globalna → WOPF, wystąpienie do poradni za zgodą rodziców, Poziom III.')]),
  p([t('Kazus C — pułapka reguły nadrzędnej: ', { bold: true }), t('wszystkie obszary 3,2–4,5, wynik ogólny 3,8 (Poziom I), ale w obszarze V dwa twierdzenia ocenione na 1 (jedzenie, ubieranie) i duża rozbieżność N–R. Oczekiwany wniosek: mimo dobrego wyniku ogólnego uruchamiamy moduł sensoryczny. Zespół, który tego nie wychwyci, dostaje informację zwrotną — to najczęstszy błąd w praktyce.')]),
  p([t('Omówienie: ', { bold: true }), t('każdy zespół czyta swój wniosek na głos jednym zdaniem. Prowadzący zapisuje trzy wnioski na flipcharcie — posłużą jako materiał wejściowy do modułu M7 (cele SMART).')]),
]));

module.exports = C;
