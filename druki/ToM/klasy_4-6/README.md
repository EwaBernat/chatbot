# ToM — Karta oceny Teorii Umysłu — klasy IV–VI

Arkusz obserwacji Teorii Umysłu (ToM) dla klas IV–VI szkoły podstawowej,
ekosystem **EduPlaner2026-MJ-PCTP**. Ta sama seria co `klasy_1-3/` i
`klasy_7-8/` — wspólna marka, wspólny układ, treść dopasowana do wieku.

## Pliki

| Plik | Opis |
|---|---|
| `ToM_karta_oceny.html` | źródło — zredukowane z oryginału 11-stronicowego (patrz niżej) |
| `ToM_karta_oceny.pdf` | wydruk wygenerowany z powyższego HTML (headless Chromium, druk A4) |

## Status: 8 stron (było 11) — zredukowane na wzór klasy 1-3

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

**Nie zredukowane do 7 stron** — dalsze skrócenie wymagałoby skracania
samego tekstu klinicznego (5 opisów umiejętności), a to już nie jest zmiana
układu, tylko treści — do decyzji autorki. Za to strona 5 przybyła: nowa
„Cele SMART" na wzór klasy 1-3, której klasa 4-6 wcześniej nie miała wcale
(patrz sekcja „Strony 4 i 5" niżej).

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
  komponentów II i V, TUK (komunikacyjny) z komponentów III i IV —
  dokładny opis każdego komponentu osobno zostaje bez zmian tam, gdzie już
  był (str. 6–8, patrz niżej) — to jest przegrupowanie tego samego
  materiału w skrócie na stronie 4, nie utrata treści.

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
słowo w słowo z „Cel SMART" na obecnych stronach 6–8 (tam też zostają,
nietknięte — to jest skrót/podgląd, nie zastąpienie). Cel główny to nowe
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

Strony 6, 7, 8 to dawne strony 5, 6, 7 (szczegółowy opis każdego z 5
komponentów: poziom funkcjonowania, zalecenia, cel SMART, podstawa prawna) —
przeniesione bez żadnej zmiany treści, tylko przenumerowane.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 8 fizycznych stron, żadna nie ucina treści.
