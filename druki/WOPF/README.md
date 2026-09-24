# WOPF — Wielospecjalistyczna Ocena Poziomu Funkcjonowania

Karta scalająca ekosystemu **EduPlaner2026-MJ-PCTP**: nie ocenia ucznia od
nowa, tylko zbiera w jednym miejscu wyniki, które powstały wcześniej w innych
drukach (KSzOF, karta ABC/FBA, ToM, kwestionariusz mowy, profil sensoryczny,
profil biopsychospołeczny). Wspólna marka i konstrukcja z serii `ToM/` —
wzorem jest `klasy_1-3`.

## Status: 22 strony — komplet, do potwierdzenia

| Plik | Opis |
|---|---|
| `WOPF_karta_oceny.html` | źródło — wszystkie 22 strony |
| `WOPF_karta_oceny.pdf` | pełny wydruk (headless Chromium, druk A4) |

Pierwotnie zbudowane jako 27 stron 1:1 z oryginalnym PDF-em autorki;
zmniejszone do 23 po tym, jak autorka poprosiła o przeniesienie kilku
sekcji na wcześniejsze strony z wolnym miejscem i o usunięcie panelu
synchronizacji oraz obu podsumowujących stron sekcji V — „wynik ogólny/
synteza wg poziomów” i „Vb — synteza opisowa” (patrz „Co jest w środku” i
historia commitów) — reszta treści identyczna, inny układ i mniej stron.
Potem do 24: autorka poprosiła o dwa nowe punkty zaraz przy wynikach
KSzOF — sekcję Vc „Czynniki kontekstowe wg ICF” (zmieściła się jeszcze na
str. 5) i sekcję Vd „Indywidualne potrzeby rozwojowe — na podstawie
dodatkowych obserwacji” (już nie zmieściła się — dostała własną str. 6).
Na koniec z powrotem w dół do 22: autorka poprosiła o usunięcie w całości
osadzonej „Opinii zespołu ds. wsparcia" (dawne str. 22–23, dokument do
wydania na zewnątrz) — zniknęła razem z jej dwiema stronami, a sekcje
XXIV–XXVI (podpisy, załączniki, RODO) przesunęły się o 2 strony w górę.
**To przy okazji rozwiązuje dualizm skali KSzOF** opisywany wcześniej w
„Do potwierdzenia": skoro jedyne miejsce z alternatywną skalą 1–5 zniknęło,
sekcja V (steny 1–10) jest teraz jedyną skalą KSzOF w całym dokumencie.

Zbudowane partiami po kilka stron, każda partia renderowana i zweryfikowana
wizualnie względem oryginalnego 27-stronicowego PDF-a autorki. Kompletne,
ale — jak cała reszta serii ToM — jeszcze **nieprzeniesione do
`Zatwierdzone/`**, bo zawiera punkty wymagające Twojej decyzji (patrz niżej).

## Co jest w środku

- **Str. 1** — tytuł, sekcja I „Dane ucznia" (10 pól, bez danych zbędnych —
  RODO), sekcja Ia „Ścieżka dokumentacyjna i rodzaj oceny" (Ścieżka A z
  orzeczeniem → IPET / Ścieżka B bez orzeczenia → PWES, 4 rodzaje oceny) i
  „Tryb postępowania" (3 pola: współpraca z poradnią, zawiadomienie
  rodziców, obecność rodzica) — wszystko przeniesione tu ze strony 2 na
  prośbę autorki, żeby cały „setup" oceny (dane, ścieżka, rodzaj, tryb) był
  widoczny na jednej stronie.
- **Str. 2** — sekcja II „Zespół specjalistów" (tabela 8 ról) i sekcja III
  „Mapa dokumentów źródłowych" (11 druków źródłowych i sekcja, do której
  trafia ich wynik — „zasada jednego źródła") — obie na pełną szerokość
  strony, bez sztucznie rozciągniętych wierszy (patrz błąd konstrukcyjny
  niżej). Mapa dokumentów przeniesiona tu ze swojej dawnej osobnej strony
  na prośbę autorki, bo obok tabeli zespołu było dość wolnego miejsca.
- **Str. 3** — sytuacje szkolne objęte obserwacją, zakres i czas obserwacji
  (pole „Czas objęty obserwacją od / do" — dwa osobne kafelki zamiast
  jednego pola „od–do"), sekcja IV „Informacje medyczne". Na dole strony —
  „Przyjmowane leki i sposób podania" oraz „Zalecenia i przeciwwskazania (w
  tym dieta)" obok siebie w jednym rzędzie, a „Postępowanie w sytuacji
  nagłej" w drugim rzędzie pod nimi (dawniej rozrzucone na dwóch stronach
  jako statyczny tekst) — wszystkie trzy jako w pełni edytowalne karty
  (`.ta`/`.ed`, ta sama konstrukcja co karty celów SMART).
- **Str. 4** — sekcja V „Wyniki oceny funkcjonalnej KSzOF" — tytuł
  bezpośrednio nad tabelą 9 obszarów ICF z **edytowalnymi stenami (1–10)**,
  opis wyników **generowany automatycznie** z wpisanych stenów, wykres
  słupkowy + mapa radarowa (9 osi). Panel synchronizacji druków (`.synbox`)
  oraz pola „zastosowany wariant/liczba twierdzeń/data" usunięte na prośbę
  autorki — nic nie stoi już między tytułem a tabelą.
- **Str. 5** — sekcja Va „Charakterystyka obszarów — mocne strony i
  trudności" — w pełni edytowalna tabela 9 obszarów, bezpośrednio po
  wynikach ilościowych. Zaraz pod nią sekcja Vb „Zakres i charakter
  wsparcia" (6 pozycji: kto wspiera ucznia) — dodana wcześniej na prośbę
  autorki, tą samą treścią co sekcja XIV dalej w dokumencie (str. 12),
  tylko od razu tutaj, obok wyników KSzOF. Na dole strony nowa sekcja Vc
  „Czynniki kontekstowe wg ICF" — dwie krótkie grupy: czynniki
  środowiskowe (przykłady, pełny wykaz w sekcji X na str. 10) i czynniki
  osobowe (ICF ich nie koduje, ale je uwzględnia — tu w ogóle nowa treść,
  nigdzie indziej w dokumencie nieopisana). Grupy skrócone do 2 pozycji
  każda, żeby zmieścić się na tej samej stronie co Va/Vb. **Uwaga:**
  sekcja Vb to świadome powtórzenie sekcji XIV w dwóch miejscach — do
  potwierdzenia, czy oba mają zostać.
- **Str. 6** — nowa sekcja Vd „Indywidualne potrzeby rozwojowe — na
  podstawie dodatkowych obserwacji": tabela 4 wierszy (Zachowania trudne —
  analiza ABC/FBA, Profil sensoryczny, Kwestionariusz rozwoju mowy, Profil
  ToM), każdy wiersz z edytowalną komórką na charakterystykę dodatkowego
  obszaru. Dodana na wyraźną prośbę autorki; nie zmieściła się już na str.
  5, więc dostała własną stronę — stąd dużo wolnego miejsca pod tabelą
  (naturalny efekt, nie błąd, ten sam wzorzec co reszta dokumentu po
  usunięciu pouczeń). **Uwaga:** te same 4 narzędzia są opisane
  szczegółowo dalej — ABC/FBA w sekcji VI (str. 7), ToM w sekcji VII (str.
  8), mowa w sekcji VIII (str. 8-9), profil sensoryczny w sekcji IX (str.
  9) — do potwierdzenia, czy Vd ma być krótkim podglądem tych czterech
  sekcji (jak Vb dla XIV), czy jest zbędny, skoro te same informacje
  pojawiają się dalej w pełnej formie.
- **Str. 7** — sekcja VI „Zachowanie — funkcje zachowań trudnych" (transfer
  z karty ABC/FBA). Dawna sekcja Vb „Opis wyników oceny funkcjonalnej —
  synteza opisowa" (4 punkty, jak i wcześniej usunięta strona „Wynik
  ogólny / reguła nadrzędna / synteza wg poziomów") usunięta w całości na
  prośbę autorki — sekcja V kończy się teraz na tabelach Va/Vb/Vc.
- **Str. 8** — plan pozytywnego wsparcia (PBS), nota o Standardach Ochrony
  Małoletnich, sekcja VII „Poznanie społeczne — teoria umysłu" (transfer z
  ToM), sekcja VIII „Mowa i komunikacja" (transfer z kwestionariusza mowy).
- **Str. 9** — sposób porozumiewania się, kierunki terapii logopedycznej,
  sekcja IX „Przetwarzanie sensoryczne" (transfer z profilu sensorycznego,
  model Dunn).
- **Str. 10** — wnioski sensoryczne, sekcja X „Kontekst biopsychospołeczny"
  (12 czynników środowiskowych ICF), ułatwienia/bariery/dobrostan, nagłówek
  sekcji XI.
- **Str. 11** — sekcja XI „Całościowy obraz funkcjonowania" (tabela synteza
  8 obszarów), sekcja XII „Indywidualne potrzeby rozwojowe i edukacyjne" —
  jej 3 puste pola („Indywidualne potrzeby rozwojowe i edukacyjne",
  „Mocne strony i możliwości psychofizyczne", „Zainteresowania,
  uzdolnienia...") dostały widoczną kropkowaną linię, tak jak puste
  komórki tabel — wcześniej wyglądały jak zwykłe puste miejsce, a nie pole
  do wypełnienia, mimo że były edytowalne (`contenteditable`) od początku.
- **Str. 12** — sekcja XIII „Przyczyny niepowodzeń edukacyjnych, bariery i
  ograniczenia", sekcja XIV „Zakres i charakter wsparcia", nagłówek XV.
- **Str. 13** — tabela metod pracy wg obszaru/przedmiotu, „Metody stosowane
  w pracy z uczniem" (16 pozycji — 2 zaznaczone jako przykład, tak jak w
  oryginale), „Formy organizacyjne pracy".
- **Str. 14** — sekcja XVI „Zakres i sposób dostosowania wymagań
  edukacyjnych" (4 kanały), dostosowanie sprawdzania wiedzy, dostosowanie
  warunków egzaminu ósmoklasisty.
- **Str. 15** — sekcja XVII „Rekomendowane zajęcia i programy
  terapeutyczne" — rewalidacja / pomoc psychologiczno-pedagogiczna, tabela
  programów terapeutycznych.
- **Str. 16** — sekcja XVIII „Zintegrowane działania nauczycieli i
  specjalistów", wspólne strategie.
- **Str. 17** — sekcja XIX „Współpraca z rodzicami i współpraca
  międzysektorowa" — tabela zobowiązań, formy współpracy, instytucje.
- **Str. 18** — sekcja XX „Decyzja posiedzenia zespołu" (rekomendowany
  poziom wsparcia), sekcja XXI „Cele SMART" — tabela + 2 karty przykładowe
  (`ta-smart-e`/`ta-smart-t`, ta sama konstrukcja co w ToM).
- **Str. 19** — sekcja XXII „Ocena efektywności udzielanego wsparcia" —
  tabela 8 zakresów × 3 pomiary (start/półrocze/koniec roku).
- **Str. 20–21** — sekcja XXIII „Przeniesienie informacji — do IPET albo do
  PWES" (tabela 9 wierszy, dwie kolumny ścieżek), priorytety na najbliższe
  półrocze.
- **Str. 22** — sekcja XXIV „Podpisy zespołu ds. WOPF" (7 podpisów), sekcja
  XXV „Wykaz załączników" (12 pozycji), sekcja XXVI „Klauzula informacyjna
  RODO i ważność dokumentu" — dawniej str. 24, teraz od razu po sekcji
  XXIII, bo „Opinia zespołu" (dawne str. 22–23) została usunięta w całości
  na wyraźną prośbę autorki (był to samodzielny, 2-stronicowy dokument
  osadzony wewnątrz WOPF, oznaczony „dokument do wydania na zewnątrz" —
  do poradni pp, z własnym tytułem w stylu strony 1, własną metryczką i 6
  ponumerowanymi punktami).

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
pozytywnego wsparcia PBS, hipoteza funkcjonalna) — to nie są „pouczenia",
tylko wypełniona treść, taka sama jak wiersz w tabeli.

Efekt uboczny: każda strona zyskała sporo wolnej przestrzeni (część stron
ma teraz nawet pół strony pustego miejsca pod treścią) — to naturalna
konsekwencja usunięcia tekstu, a nie błąd. Numeracja stron i sekcji
(I–XXVI) pozostała bez zmian.

Dodatkowo usunięta ramka „Karta scalająca — WOPF szkolny · jeden druk, dwie
ścieżki" na str. 1 (opisowy akapit o tym, czym jest WOPF) — z tego samego
powodu, ta sama kategoria „informacji/wyjaśnień", tylko nie wychwycona przy
pierwszym przejściu, bo nie miała stylu `.howto` ani „Podstawa prawna".

## Interaktywność

Tylko sekcja V (wyniki KSzOF) ma pełne przeliczanie automatyczne — to
jedyna sekcja, w której WOPF prezentuje liczby (steny), więc tylko tu ma to
sens. Wpisanie stenu 1–10 w dowolnym z 9 wierszy tabeli automatycznie:
poziom wsparcia w tym samym wierszu (kolor + etykieta Poziom I/II/III),
słupek i punkt na mapie radarowej, opis wyników pod tabelą (zamraża się po
pierwszej ręcznej poprawce — ten sam wzorzec co `#autoOpis` w ToM). Pozostałe sekcje to pola
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
budowanej dla WOPF. Ten sam efekt (tym razem jako absurdalnie wysokie
wiersze, nie znikający wiersz) dotknął też tabelę „Zespół specjalistów" na
str. 2, gdy po przeniesieniu ścieżki dokumentacyjnej na str. 1 zrobiła się
z niej jedyny większy blok na stronie — naprawione tak samo (wiersze mają
teraz naturalną, zwartą wysokość), tabela zostaje na pełną szerokość
strony.

Drugi, mniejszy przypadek tej samej rodziny problemów: puste pola
`contenteditable` bez żadnej treści (np. 3 pola sekcji XII) nie miały
żadnego wizualnego znaku, że są do wypełnienia — wyglądały jak zwykła
pusta przestrzeń, identycznie jak np. już wypełniona notatka „Hipoteza
funkcjonalna" wygląda, gdy jest pusta. Naprawione dodaniem tej samej
kropkowanej linii, jaką puste komórki tabel już miały (`:empty::after`),
tylko jako nowa, celowo wąsko wyselekcjonowana klasa (`.note.blankfill`),
żeby nie zmieniać wyglądu pozostałych, już wypełnionych notatek w reszcie
dokumentu.

## Do potwierdzenia przez autorkę

- ~~Dwie różne skale KSzOF w tym samym dokumencie~~ — **rozwiązane**:
  usunięcie „Opinii zespołu" (patrz wyżej) usunęło też jedyne miejsce,
  które używało alternatywnej skali średnia 1–5. Sekcja V (str. 4, skala
  sten 1–10 — realna skala z Twoich kwestionariuszy KSzOF_I-III/IV-VI w
  `druki/Zatwierdzone/`) jest teraz jedynym miejscem w WOPF, które podaje
  liczby KSzOF.
- **Sekcja Vb i sekcja XIV — to samo pytanie „zakres i charakter wsparcia"
  w dwóch miejscach (str. 5 i str. 12).** Dodane na wyraźną prośbę zaraz po
  charakterystyce obszarów KSzOF, tą samą treścią co już istniejąca sekcja
  XIV dalej w dokumencie. Zostawiam obie — do potwierdzenia, czy to
  zamierzone powtórzenie (np. Vb jako pierwsza, szybka ocena tuż po KSzOF,
  a XIV jako ostateczna decyzja przy planowaniu IPET/PWES), czy któraś ma
  zniknąć.
- **Sekcja Vc a sekcja X — czynniki środowiskowe wg ICF, znowu w dwóch
  miejscach (str. 5 i str. 10).** Ten sam wzorzec co Vb/XIV: Vc daje krótki
  podgląd (2 pozycje, przykładowe) tuż przy wynikach KSzOF, a pełny wykaz
  (12 pozycji z kodami ICF) zostaje w sekcji X. Część Vc o czynnikach
  *osobowych* jest natomiast całkiem nowa — nie duplikuje niczego, bo ICF
  wprawdzie nie klasyfikuje czynników osobowych kodem, ale wymienia je jako
  drugą (obok środowiskowych) kategorię czynników kontekstowych.
- **Sekcja Vd — tabela 4 dodatkowych obserwacji (str. 6) — czy to podgląd
  czy powtórka.** Zawiera po jednym wierszu na: analizę ABC/FBA, profil
  sensoryczny, kwestionariusz mowy, profil ToM — te same cztery narzędzia
  są potem opisane szczegółowo w sekcjach VI–IX (str. 7–9). Dodana na
  wyraźną prośbę tuż po sekcji V, ale w przeciwieństwie do Vb/Vc nie ma tu
  jeszcze żadnej treści do przepisania z oryginalnego PDF-u — komórki
  wynikowe są puste, do wypełnienia przez zespół. Do potwierdzenia: czy ma
  zostać jako szybkie podsumowanie „co jeszcze obserwowaliśmy" zaraz przy
  KSzOF, czy to zbędne powtórzenie nagłówków sekcji VI–IX.
- **Sekcja VII, komponenty ToM (K1–K5)**: oryginalny PDF autorki używa
  innego zestawu komponentów („Świadomość emocji własnych", „Rozpoznawanie
  emocji innych", „Przyjmowanie perspektywy", „Rozumienie intencji", „Język
  niedosłowny") niż którykolwiek z trzech gotowych wariantów ToM w tym
  repozytorium (klasy 1-3/4-6/7-8 mają inne, bardziej rozbudowane nazwy
  komponentów). Przepisane tu **dosłownie z oryginału WOPF** — wymaga
  Twojej decyzji, czy to osobny, uproszczony zestaw K1–K5, czy pomyłka do
  poprawienia.
- Żaden z czterech wariantów ToM ani WOPF nie jest jeszcze przeniesiony do
  `Zatwierdzone/` — czeka na Twoje potwierdzenie powyższych punktów.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 22 fizyczne strony, żadna nie ucina treści
(sprawdzone programowo — margines do stopki dodatni na każdej stronie),
zero błędów JS, interaktywność sekcji V przetestowana.
