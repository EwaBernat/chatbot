# WOPF — Wielospecjalistyczna Ocena Poziomu Funkcjonowania

Karta scalająca ekosystemu **EduPlaner2026-MJ-PCTP**: nie ocenia ucznia od
nowa, tylko zbiera w jednym miejscu wyniki, które powstały wcześniej w innych
drukach (KSzOF, karta ABC/FBA, ToM, kwestionariusz mowy, profil sensoryczny,
profil biopsychospołeczny). Wspólna marka i konstrukcja z serii `ToM/` —
wzorem jest `klasy_1-3`.

## Status: 27 z 27 stron — komplet, do potwierdzenia

| Plik | Opis |
|---|---|
| `WOPF_karta_oceny.html` | źródło — wszystkie 27 stron |
| `WOPF_karta_oceny.pdf` | pełny wydruk (headless Chromium, druk A4) |

Zbudowane partiami po kilka stron, każda partia renderowana i zweryfikowana
wizualnie względem oryginalnego 27-stronicowego PDF-a autorki. Kompletne,
ale — jak cała reszta serii ToM — jeszcze **nieprzeniesione do
`Zatwierdzone/`**, bo zawiera punkty wymagające Twojej decyzji (patrz niżej).

## Co jest w środku

- **Str. 1** — tytuł, „Karta scalająca", sekcja I „Dane ucznia" (10 pól, bez
  danych zbędnych — RODO).
- **Str. 2** — sekcja Ia „Ścieżka dokumentacyjna" (Ścieżka A z orzeczeniem →
  IPET / Ścieżka B bez orzeczenia → PWES), rodzaj oceny, sekcja II „Zespół
  specjalistów" (tabela 8 ról).
- **Str. 3** — sekcja III „Mapa dokumentów źródłowych" (11 druków źródłowych
  i sekcja, do której trafia ich wynik — „zasada jednego źródła").
- **Str. 4** — sytuacje szkolne objęte obserwacją, zakres i czas obserwacji,
  sekcja IV „Informacje medyczne".
- **Str. 5–9** — sekcja V „Wyniki oceny funkcjonalnej KSzOF": panel
  synchronizacji druków (`.synbox`), tabela 9 obszarów ICF z **edytowalnymi
  stenami (1–10)**, wykres słupkowy + mapa radarowa (nowa, zbudowana dla
  WOPF — 9 osi), opis wyników **generowany automatycznie** z wpisanych
  stenów, sekcja Va (charakterystyka jakościowa 9 obszarów) i Vb (synteza
  opisowa, 4 punkty).
- **Str. 10** — sekcja VI „Zachowanie — funkcje zachowań trudnych" (transfer
  z karty ABC/FBA).
- **Str. 11** — plan pozytywnego wsparcia (PBS), nota o Standardach Ochrony
  Małoletnich, sekcja VII „Poznanie społeczne — teoria umysłu" (transfer z
  ToM), sekcja VIII „Mowa i komunikacja" (transfer z kwestionariusza mowy).
- **Str. 12** — sposób porozumiewania się, kierunki terapii logopedycznej,
  sekcja IX „Przetwarzanie sensoryczne" (transfer z profilu sensorycznego,
  model Dunn).
- **Str. 13** — wnioski sensoryczne, sekcja X „Kontekst biopsychospołeczny"
  (12 czynników środowiskowych ICF), ułatwienia/bariery/dobrostan, nagłówek
  sekcji XI.
- **Str. 14** — sekcja XI „Całościowy obraz funkcjonowania" (tabela synteza
  8 obszarów), sekcja XII „Indywidualne potrzeby rozwojowe i edukacyjne".
- **Str. 15** — sekcja XIII „Przyczyny niepowodzeń edukacyjnych, bariery i
  ograniczenia", sekcja XIV „Zakres i charakter wsparcia", nagłówek XV.
- **Str. 16** — tabela metod pracy wg obszaru/przedmiotu, „Metody stosowane
  w pracy z uczniem" (16 pozycji — 2 zaznaczone jako przykład, tak jak w
  oryginale), „Formy organizacyjne pracy".
- **Str. 17** — sekcja XVI „Zakres i sposób dostosowania wymagań
  edukacyjnych" (4 kanały), dostosowanie sprawdzania wiedzy, dostosowanie
  warunków egzaminu ósmoklasisty.
- **Str. 18** — sekcja XVII „Rekomendowane zajęcia i programy
  terapeutyczne" — rewalidacja / pomoc psychologiczno-pedagogiczna, tabela
  programów terapeutycznych.
- **Str. 19** — sekcja XVIII „Zintegrowane działania nauczycieli i
  specjalistów", wspólne strategie.
- **Str. 20** — sekcja XIX „Współpraca z rodzicami i współpraca
  międzysektorowa" — tabela zobowiązań, formy współpracy, instytucje.
- **Str. 21** — sekcja XX „Decyzja posiedzenia zespołu" (rekomendowany
  poziom wsparcia), sekcja XXI „Cele SMART" — tabela + 2 karty przykładowe
  (`ta-smart-e`/`ta-smart-t`, ta sama konstrukcja co w ToM).
- **Str. 22** — sekcja XXII „Ocena efektywności udzielanego wsparcia" —
  tabela 8 zakresów × 3 pomiary (start/półrocze/koniec roku).
- **Str. 23–24** — sekcja XXIII „Przeniesienie informacji — do IPET albo do
  PWES" (tabela 9 wierszy, dwie kolumny ścieżek), priorytety na najbliższe
  półrocze.
- **Str. 25–26** — **„Opinia zespołu ds. wsparcia o funkcjonowaniu ucznia"**
  — samodzielny, 2-stronicowy dokument osadzony wewnątrz WOPF, oznaczony
  „dokument do wydania na zewnątrz" (do poradni pp). Własny tytuł w stylu
  strony 1 (`.tt-kick`/`.tt-h1`), własna metryczka, 6 ponumerowanych
  punktów, miejsce na podpisy koordynatora i dyrektora.
- **Str. 27** — sekcja XXIV „Podpisy zespołu ds. WOPF" (7 podpisów), sekcja
  XXV „Wykaz załączników" (12 pozycji), sekcja XXVI „Klauzula informacyjna
  RODO i ważność dokumentu".

## Pouczenia prawne i wyjaśnienia — usunięte

Na wyraźną prośbę autorki usunięte zostały wszystkie ramki „Podstawa
prawna" (cytowania przepisów) oraz wszystkie boksy „✍ Jak wypełnić"
(instrukcje wypełniania) na wszystkich 27 stronach — zajmowały dużo miejsca
przy niewielkiej wartości użytkowej dla kogoś, kto już wie, jak z druku
korzystać. Usunięte też pojedyncze notki czysto wyjaśniające bez
konkretnych danych o uczniu (np. „legenda" profilu sensorycznego, „granica
dostosowania", „sprawdzian celu SMART"). **Zostały** notatki, które są
faktyczną treścią kliniczną/proceduralną dotyczącą konkretnego ucznia albo
konkretnej procedury szkoły (np. procedura na wypadek sytuacji nagłej, plan
pozytywnego wsparcia PBS, hipoteza funkcjonalna, wnioski sekcji „Opinia
zespołu") — to nie są „pouczenia", tylko wypełniona treść, taka sama jak
wiersz w tabeli.

Efekt uboczny: każda strona zyskała sporo wolnej przestrzeni (część stron
ma teraz nawet pół strony pustego miejsca pod treścią) — to naturalna
konsekwencja usunięcia tekstu, a nie błąd. Numeracja stron i sekcji
(I–XXVI) pozostała bez zmian.

## Interaktywność

Tylko sekcja V (wyniki KSzOF) ma pełne przeliczanie automatyczne — to
jedyna sekcja, w której WOPF prezentuje liczby (steny), więc tylko tu ma to
sens. Wpisanie stenu 1–10 w dowolnym z 9 wierszy tabeli automatycznie:
poziom wsparcia w tym samym wierszu (kolor + etykieta Poziom I/II/III),
słupek i punkt na mapie radarowej, średnia ogólna i poziom wsparcia na
stronie 7, opis wyników pod tabelą (zamraża się po pierwszej ręcznej
poprawce — ten sam wzorzec co `#autoOpis` w ToM). Pozostałe sekcje to pola
i tabele do ręcznego wypełnienia — WOPF tylko *rejestruje* to, co przenosi
się z innych druków, nie przelicza tego samodzielnie.

## Znaleziony i naprawiony błąd konstrukcyjny

Współdzielony arkusz stylów (ten sam co w całej serii ToM) ma regułę, która
automatycznie rozciąga JEDYNĄ tabelę na stronie na 100% wysokości karty
(`flex:1 1 auto;height:100%`), żeby wiersze ładnie wypełniały pustą
przestrzeń. Na stronach, gdzie po tabeli jest jeszcze dużo innej treści, ta
reguła konfliktowała z `table-layout:fixed` i powodowała, że **ostatni
wiersz tabeli był rysowany, ale zasłaniany przez następny blok**
(niewidoczny mimo poprawnej pozycji w DOM). Naprawione przez jawne
wyłączenie tego rozciągania (`flex:0 0 auto;height:auto`) na każdej tabeli
budowanej dla WOPF.

## Do potwierdzenia przez autorkę

- **Dwie różne skale KSzOF w tym samym dokumencie — to jest ten „dualizm",
  o który prosiłaś na sprawdzić.** Sekcja V (str. 5–9) używa skali
  **sten 1–10** (średnia 5 → Poziom II) — to realna skala z Twoich
  kwestionariuszy KSzOF_I-III/IV-VI (`druki/Zatwierdzone/`). Ale „Opinia
  zespołu" (str. 25, punkt 2) w tym samym oryginalnym PDF-ie opisuje **tę
  samą ocenę** zupełnie inną skalą: **średnia 1–5** z progami 4,0–5,0
  zasób / 3,0–3,9 poziom I / 2,0–2,9 poziom II / poniżej 2,0 poziom III
  (przykładowa średnia 2,79, obszar I = 4,20 itd.) — inne liczby, inny
  podział na poziomy, a nawet nieco inna kolejność obszarów w opisie.
  Przepisane tu **dosłownie z oryginału, każde w swojej sekcji** — nie
  ujednoliciłam tego samodzielnie, bo nie wiem, która skala ma zostać: czy
  „Opinia zespołu" to starszy fragment sprzed przejścia na steny (wtedy do
  przeliczenia), czy to sekcja, która celowo używa innej, prostszej skali
  do komunikacji z poradnią.
- **Sekcja VII, komponenty ToM (K1–K5)**: oryginalny PDF autorki używa
  innego zestawu komponentów („Świadomość emocji własnych", „Rozpoznawanie
  emocji innych", „Przyjmowanie perspektywy", „Rozumienie intencji", „Język
  niedosłowny") niż którykolwiek z trzech gotowych wariantów ToM w tym
  repozytorium (klasy 1-3/4-6/7-8 mają inne, bardziej rozbudowane nazwy
  komponentów). Przepisane tu **dosłownie z oryginału WOPF** — wymaga
  Twojej decyzji, czy to osobny, uproszczony zestaw K1–K5, czy pomyłka do
  poprawienia.
- **„Opinia zespołu" (str. 25–26)** — potwierdzone, że to NIE jest błąd
  składu PDF-u, tylko celowy, samodzielny dokument do wydania na zewnątrz,
  osadzony przed podpisami WOPF. Zostawione dokładnie w tym miejscu i w tej
  formie.
- Żaden z czterech wariantów ToM ani WOPF nie jest jeszcze przeniesiony do
  `Zatwierdzone/` — czeka na Twoje potwierdzenie powyższych punktów.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 27 fizycznych stron, żadna nie ucina treści
(sprawdzone programowo — margines do stopki dodatni na każdej stronie),
zero błędów JS, interaktywność sekcji V przetestowana.
