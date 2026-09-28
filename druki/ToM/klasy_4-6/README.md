# ToM — Karta oceny Teorii Umysłu — klasy IV–VI

Arkusz obserwacji Teorii Umysłu (ToM) dla klas IV–VI szkoły podstawowej,
ekosystem **EduPlaner2026-MJ-PCTP**. Ta sama seria co `klasy_1-3/` i
`klasy_7-8/` — wspólna marka, wspólny układ, treść dopasowana do wieku.

## Pliki

| Plik | Opis |
|---|---|
| `ToM_karta_oceny.html` | źródło — zredukowane z oryginału 11-stronicowego (patrz niżej) |
| `ToM_karta_oceny.pdf` | wydruk wygenerowany z powyższego HTML (headless Chromium, druk A4) |

## Status: 7 stron (było 11) — dokładnie tyle, co klasa 1-3

Oryginał przysłany przez autorkę miał 11 stron. Na jej prośbę zredukowane do
wzoru strukturalnego z `klasy_1-3/` (tam druk ma 7 stron) — bez zmiany
**żadnego** tekstu obserwacji, zaleceń ani celów SMART dla żadnej z 5
umiejętności (Rozpoznawanie emocji mieszanych, Decentracja, Ironia i
podtekst, Fałszywe przekonanie II rzędu, Faux pas) — te są celowo różne niż
w klasie 1-3 i zostają nietknięte.

**Usunięte w całości** (nie ma tego wcale we wzorze klasy 1-3):
- cały cykl re-ewaluacji — tabela „Postęp wg komponentów”, „Wnioski i
  decyzja”, „Nowe zalecenia po ewaluacji” (dawne str. 8 (część)–9),
- sekcja „Synchronizacja druków — przeniesienie wyników” z WOPF (dawne
  str. 10–11).

Podpis prowadzącego i podstawa prawna (dawna końcówka str. 10) zostały
przeniesione na koniec obecnej strony 8 zamiast zostawać na osobnej,
prawie pustej stronie.

Po drodze było 8, potem 9 stron — zanim wszystkie sekcje zostały dopasowane
do wzoru, klasa 4-6 miała chwilowo 3 dodatkowe strony ze szczegółowym
opisem każdego z 5 komponentów osobno (poziom funkcjonowania, zalecenia,
cel SMART, podstawa prawna — dawne str. 7-9), których klasa 1-3 nie ma
wcale. Na wyraźną prośbę autorki („zrób według wzoru klasy 1-3 a daj dane
z klas 4-6") te 3 strony zostały **usunięte**, a w ich miejsce jedna nowa
strona 7 „Zastosowanie ToM w ocenie ABC i FBA" — dokładnie jak w klasie
1-3. Efekt: **7 stron, tak jak klasa 1-3**, żadnej dodatkowej. Za to
przybyły 2 strony, których klasa 4-6 wcześniej nie miała wcale, obie na
wzór klasy 1-3: „Cele SMART" (str. 5) i „Proponowane formy wsparcia"
(str. 6) — patrz sekcje niżej.

**Co dokładnie zniknęło wraz z dawnymi stronami 7-9** (żeby było jasne, a
nie tylko "przenumerowane"): tabela „VI Poziom rozwoju Teorii umysłu —
norma rozwojowa a obecne funkcjonowanie" (klasa 1-3 nie ma takiej tabeli
wcale) — to realnie usunięte, nie ma tego nigdzie indziej. Nie zniknęły
natomiast: podpis prowadzącego (jest już na str. 5, w bloku podpisów Cele
SMART, tak jak w klasie 1-3), naukowa podstawa narzędzia — cytowania
Wellman i Liu / Baron-Cohen / Perner / Premack i Woodruff są od dawna w
sekcji „Więcej" na str. 1, dokładnie tak jak w klasie 1-3 — **i** opisowe
akapity „Zalecenia do pracy" dla każdego z 5 komponentów osobno (konkretne
pomysły na ćwiczenia w klasie), dopisane z powrotem do tej samej sekcji
„Więcej" jako nowy blok „Zalecenia do pracy — wg komponentu", żeby nie
przepadły na dobre.

Uwaga: sekcja „Więcej" (`<details class="rozwijak no-print">`) jest
**ekranowa** — widoczna po rozwinięciu w przeglądarce, ale nie drukuje się
(sprawdzone: żadne z tych 9 akapitów, łącznie z nowymi „Zalecenia do
pracy", nie pojawia się w wygenerowanym PDF) — tak samo działa u wzoru w
klasie 1-3. Więc druk zostaje dokładnie 7-stronicowy, a zalecenia są
dostępne do odczytania/skopiowania w interaktywnej wersji HTML, nie na
wydruku dla ucznia.

## Strona 1 przebudowana na wzór klasy 1-3 — ⚠️ do potwierdzenia

Na prośbę autorki strona 1 ma teraz dokładnie tę samą kolejność sekcji co
`klasy_1-3/`: metryczka (2 pola) → tytuł → „Czym jest ToM” → skala →
„Więcej” (ukryte przy druku, jak w 1-3) → nagłówek „Arkusz obserwacji” →
tabela „Zastosowanie ToM w KSzOF”.

Metryczka: usunięte 2 zduplikowane pola („Imię i nazwisko”, „Klasa/oddział”
— powtarzały dane już wpisywane w nagłówku strony), zostały te same 2 pola
co w 1-3.

## Konstrukcja tabeli obserwacji — przebudowana na wzór klasy 1-3

Prawdziwa różnica nie była w kolorze kółek, tylko w konstrukcji: strony 2-3
miały **osobną tabelę na każdy z 5 obszarów** (własny nagłówek z nazwą
obszaru, a podsumowanie — suma/średnia/poziom — w osobnym kolorowym boksie
pod tabelą). Wzór klasy 1-3 ma **jedną ciągłą tabelę** na stronę, z ogólnym
nagłówkiem („Wskaźnik obserwacji"), a granice obszarów to wiersze-nagłówki
*wewnątrz* tej samej tabeli (fioletowe tło, numer + nazwa obszaru +
podsumowanie w jednej linii).

Przebudowane 1:1 na ten wzór (`table.qtable`, `tr.area-row`/`.arow`/`.anum`/
`.atitle`/`.asten`, `.ocena[data-area]` zamiast osobnych tabel `table.rt` +
`.asum`) — CSS skopiowane z `klasy_1-3`. Wszystkie 25 pozycji i 5 obszarów
zachowane bez zmian treści, tylko przeniesione do nowej konstrukcji.

Mechanizm liczenia (`areaStats`) przepisany na dopasowywanie po atrybucie
`data-area` (jak w 1-3) zamiast po tym, w której osobnej tabeli coś się
znajduje — bogatsze funkcje klasy 4-6 (wykres słupkowy, mapa radarowa,
automatyczny opis wyników na str. 5) zostały nietknięte i nadal działają:
sprawdzone testem interaktywnym (zaznaczenie ocen → poprawne przeliczenie
sumy/średniej/poziomu w nagłówku obszaru → poprawne zasilenie wykresu i
opisu wyników), zero błędów JS.

## Kółeczka oceny 0/1/2 — przebudowane na wzór klasy 1-3

Oryginał miał kółeczka na stałe pokolorowane (czerwony/żółty/zielony
zaszyty w każdej opcji przez `style="border-color:..."`) i skrypt
uruchamiany przy **każdym wczytaniu strony**, który automatycznie zaznaczał
przykładowe oceny (`window.addEventListener("load", ...)` + tablica
`EXAMPLE`) — więc plik nigdy nie ładował się naprawdę pusty. Wzór klasy 1-3
nie ma nic z tego: kółeczka są neutralnie szare i kolorują się dopiero po
kliknięciu (przez klasy CSS `.sel.v0/v1/v2`), a strona ładuje się pusta.

Zmiana: te same klasy CSS co w klasie 1-3 (`td.oc i.sel`, `.v0/v1/v2`),
`data-v="0/1/2"` zamiast koloru w stylu inline, i usunięty routine
auto-zaznaczania przy starcie. Mechanizm liczenia wyników (sumy, średnie,
wykresy) — nietknięty, dalej działa identycznie, tylko teraz liczy od zera
zamiast od przykładowych danych. Sprawdzone: brak błędów JS, wykresy
poprawnie pokazują pusty stan (0 słupków, pusty radar) zamiast się wywalać.

**Tabela „Zastosowanie ToM w KSzOF (klasy IV–VI)” — nowa, zbudowana teraz.**
1-3 miała gotową tabelę TUE/TUS/TUK dla swojego KSzOF; dla klas 4-6 takiej
nie było. Zbudowana od podstaw na bazie **rzeczywistej** treści
`druki/Zatwierdzone/KSzOF_IV-VI/` (52 pozycje, 9 obszarów, kody ICF) —
każdy z 5 komponentów ToM dopasowany do tematycznie najbliższych pozycji
KSzOF IV-VI. To dopasowanie tematyczne jest interpretacją, nie jedynym
możliwym przyporządkowaniem — **wymaga sprawdzenia przez autorkę**, w
odróżnieniu od reszty pliku, która jest przeniesieniem istniejącej treści.

## Strony 4 i 5 — przebudowane na wzór klasy 1-3

Pierwsza wersja strony „IV Wynik i priorytety" różniła się od wzoru na dwa
niezależne sposoby, poprawione w dwóch kolejnych przejściach:

**1. Konstrukcja wykresu i tabeli.** Wykres był wizualnie inny niż wzór
(wysoki `viewBox`, siatka co 1 pkt, dekoracyjne ramki pod słupkami, zbędny
wstępny akapit i notka pod spodem), a tabela barier miała 8 wierszy: po
jednym na każdy z 5 komponentów (I–V) plus „Zasoby", „Profil ogólny" i
„Rekomendacje" — inny podział niż wzór klasy 1-3, który dzieli tabelę wg
**kategorii treningu** (Profil ToM ogólny / TUE / TUS / TUK / Rekomendacje
ogólne), nie wg numeru komponentu. Poprawione:
- wykres przebudowany 1:1 na konstrukcję z klasy 1-3: ten sam `viewBox`,
  te same proporcje słupków, siatka tylko na 0/5/10 z przerywaną linią na
  połowie, etykiety I–V i nazwy komponentów w SVG, bez wstępnego akapitu.
  Mechanizm liczenia (`updateCharts()`, atrybuty `data-top/bot/max` na
  `<svg>`) — nietknięty, słupki nadal kolorują się wg poziomu i liczą z
  tych samych ocen co tabela obserwacji;
- automatyczny opis wyników dostał stałe miejsce — boks `#autoOpis` (styl
  `.note`, jak `#priorytety` w klasie 1-3) tuż pod wykresem, zamiast być
  doklejanym przez skrypt gdzie indziej, gdy żaden statyczny element o tym
  `id` nie istniał (wcześniej lądował obok tabeli „Wynik na komponent" na
  stronie 3);
- tabela „Profil komponentów — katalog barier i trudności" przebudowana na
  te same 5 wierszy/kategorii co w klasie 1-3 (Profil ToM ogólny / TUE /
  TUS / TUK / Rekomendacje ogólne), `id="tab-profil"` jak we wzorze. TUE
  (trening emocjonalny) zbudowany z opisu komponentu I, TUS (społeczny) z
  komponentów II i V, TUK (komunikacyjny) z komponentów III i IV. W chwili
  budowania tej tabeli pełny opis każdego komponentu osobno („Aktualny
  poziom funkcjonowania") wciąż istniał na dawnych stronach 6–8 — było to
  więc przegrupowanie w skrócie, a nie utrata treści. Te strony zostały
  później usunięte na wyraźną prośbę autorki (patrz „Status" wyżej) — więc
  dziś ta tabela na str. 4 jest jedynym miejscem, gdzie ten opis w ogóle
  występuje.

**2. Rozmiar tabel pod wykresem.** Niezależnie od podziału na kategorie,
same komórki tabeli były znacznie większe/szersze niż we wzorze — bo
klasie 4-6 brakowało całego bloku CSS, który klasa 1-3 ma pod koniec
arkusza stylów i który: (a) blokuje flex-owe rozciąganie `.blk`/`table.tb`
na całą wysokość strony (`flex:0 0 auto!important;height:auto!important`),
(b) zmniejsza padding komórek (`3.6px 7px` zamiast `5.5px 8px`) i
zagęszcza `line-height`, (c) ustawia dokładną wysokość wiersza `#tab-profil`
(48px). Bez tego bloku tabela rozciągała się na wolną przestrzeń strony i
każdy wiersz robił się nienaturalnie wysoki. Skopiowany 1:1 z klasy 1-3 —
dotyczy każdej tabeli `table.tb`/`table.qtable` i każdego wykresu w `.ta`
w całym pliku, nie tylko tej jednej.

Dzięki krótszej (5 zamiast 8 wierszy), węższej tabeli wykres i tabela znowu
mieszczą się razem na jednej stronie 4 — dokładnie tak jak w klasie 1-3 —
więc osobna strona na samą tabelę już niepotrzebna.

**Strona 5 — nowa: „V Cele SMART"**, dokładnie wg wzoru klasy 1-3: cel
główny, tabela `#tab-smart` (Lp./cel/pilny/termin/odpowiedzialny), przyciski
„Zasugeruj cele wg wyników" i „+ Dodaj cel", pola „Termin przeglądu"/„Osoba
koordynująca", podpisy. Wcześniej klasa 4-6 nie miała takiej strony wcale.
Tabela wypełniona 5 gotowymi celami — po jednym na komponent, przepisane
słowo w słowo z „Cel SMART" na dawnych stronach 6–8, w chwili budowania tej
tabeli wciąż obecnych osobno (to był wtedy skrót/podgląd, nie zastąpienie).
Po usunięciu tamtych stron (patrz „Status" wyżej) ta tabela na str. 5 jest
jedynym miejscem, gdzie te cele SMART w ogóle występują. Cel główny to nowe
zdanie łączące wszystkie 5 komponentów w jeden ogólny cel, na wzór klasy
1-3 — **do sprawdzenia przez autorkę**, w odróżnieniu od reszty tabeli,
która jest przeniesieniem istniejącej treści.
Przyciski działają naprawdę: `zasugerujCele()` i `dodajCelSmart()`
przeniesione 1:1 z klasy 1-3 (są w pełni ogólne — nie odwołują się do
niczego specyficznego dla klasy 1-3 — więc zadziałały bez żadnych zmian na
danych klasy 4-6).

Sprawdzone testem interaktywnym po obu przejściach: zaznaczenie ocen →
poprawne sumy w tabeli obserwacji → poprawny wykres → poprawny automatyczny
opis wyników → „Zasugeruj cele" poprawnie układa tabelę wg pozycji
ocenionych nisko, zero błędów JS.

## Strona 6 — nowa: „VI Proponowane formy wsparcia"

Klasa 4-6 nie miała odpowiednika tej strony wcale. Dodana wg dokładnie tego
samego wzoru co klasa 1-3: tabela ścieżek A (uczeń z orzeczeniem — zajęcia
rewalidacyjne) / B (uczeń z opinią PPP — pomoc psychologiczno-pedagogiczna)
z podstawą prawną, potem „Wybór realizowanego programu" (tabela z
checkboxami: program rewalidacyjny / program PPP) i notka o tym, że o
wyborze decyduje dokument ucznia i zespół specjalistów, nie karta ToM.

Treść przepisana słowo w słowo z klasy 1-3, bez żadnej zmiany — to opis
polskiego prawa oświatowego (rozporządzenia MEN z 9.08.2017 r.), identyczny
niezależnie od wieku ucznia, więc nie ma tu nic specyficznego dla klasy 1-3
do „przetłumaczenia" na klasy 4-6.

## Strona 7 — nowa: „VII Zastosowanie ToM w ocenie ABC i FBA" (zastępuje dawne strony 7-9)

Ostatnia strona klasy 1-3 to tabela 8 funkcji zachowania (Ucieczka /
Unikanie / Uzyskanie / Dostęp / Stymulacja sensoryczna / Regulacja emocji /
Regulacja komunikacyjna / Wielofunkcyjne) — dla każdej: definicja
operacyjna i jej związek z deficytami teorii umysłu. Ten sam checkbox +
`<details>` co przy tabeli KSzOF na str. 1 (wzorowany na mechanizmie już
działającym w tym pliku, nie na CSS-owym mechanizmie klasy 1-3 — oba dają
ten sam efekt na wydruku).

„Funkcja zachowania" i „Definicja operacyjna" to ogólna metodyka ABC/FBA,
identyczna niezależnie od wieku — przepisana bez zmian. Trzecia kolumna
(„Związek z deficytami teorii umysłu") w klasie 1-3 odwołuje się do jej 5
komponentów — tu przepisana na nowo pod komponenty klasy 4-6 (np.
„Regulacja emocji" → komponent I „Rozpoznawanie emocji mieszanych", zamiast
ogólnego „nazywanie emocji" z klasy 1-3; „Ucieczka"/"Unikanie" → odczytanie
podtekstu/ironii i przyjęcie cudzej perspektywy, komponenty II-III).
Pozostałe dwie funkcje (Stymulacja sensoryczna, Wielofunkcyjne) są z natury
ogólne i zostały bez zmian.

To zastępuje dawne strony 7-9 — co dokładnie z nich zniknęło, opisane w
sekcji „Status" na górze tego pliku.

## Logo PCTP

Nagłówek każdej strony miał okrągły fioletowy placeholder z samym tekstem
„PCTP" (`background:#2D1B69` + tekst), podczas gdy klasa 1-3 od dawna ma tam
prawdziwe logo — fioletowe kółko z ikoną kwiatu lawendy i napisem PCTP,
zaszyte jako obrazek `background-image` (base64 PNG) w CSS. Podmienione na
dokładnie to samo osadzenie (ta sama grafika, ten sam PNG) — teraz identyczne
w całej serii ToM, klasy 1-3/4-6/7-8. To ten sam plik, który autorka wgrała
do repo jako `logo-lawenda.webp`.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 7 fizycznych stron, żadna nie ucina treści.
