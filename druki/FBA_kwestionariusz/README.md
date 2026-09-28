# Kwestionariusz funkcji zachowania (FBA · 0–3)

Funkcjonalna ocena zachowania (Functional Behavior Assessment) — kwestionariusz
rozpoznający, jaką funkcję pełni zachowanie trudne ucznia (ucieczka/unikanie,
przeciążenie sensoryczne, uwaga, dostęp do rzeczy, regulacja emocji), jako
podstawa hipotezy funkcji i planu pozytywnego wsparcia (PBS). Wspólna marka i
konstrukcja z serii `WOPF/`, `ToM/`, `Profil_biopsychospoleczny/`,
`Profil_sensoryczny/`, `Dziennik_ABC/`.

## Skąd ten druk — ujednolicenie dwóch przesłanych plików

Przesłałaś dwa pliki tego samego narzędzia:

- **`Funkcjonalna_ocena_zachowania_FBA - 0-3.html`** — kompletne, w pełni
  działające źródło (25 pozycji + kody ICF, klikalne kółka 0–3, auto-sumowanie
  na funkcję, wykresy słupkowy i radarowy, hipoteza funkcji, synteza,
  monitorowanie), ale w **innym systemie szablonów** (`<section class="sheet
  roomy itempage/autofill">`, 8 stron, własny CSS) niż reszta serii, z płaskim
  tekstowym „PCTP" zamiast prawdziwego loga.
- **`FBA_0-3_-_mowa.pdf`** — to samo narzędzie, ta sama treść i ta sama
  demo-uczennica (Zofia Lewandowska, III A), ale już w **wspólnym systemie
  PCTP** (`.page`/`.phead`/`.pmeta`/`.pbody`/`.pfoot`), 10 stron, z prawdziwym
  logo — bez dołączonego źródła HTML (nazwa pliku „mowa" najwyraźniej nie
  pasuje do treści — to FBA, nie ocena mowy; nie ruszałam tego, to tylko nazwa
  pliku, nie treść).

„Ujednolicenie" oznaczało: przebudować `.html` na wspólny system rodziny
(dokładnie ten sam, co pokazywał `.pdf`), zachowując **całą** działającą
logikę interaktywną ze źródła — bez zgadywania na nowo.

## Co zachowane 1:1 ze źródła

- **Wszystkie 25 pozycji kwestionariusza** (5 funkcji × 5 pozycji) — treść i
  kolejność dokładnie jak w `.html`.
- **Kody ICF** przy każdej funkcji (np. `b1304 · d2402` dla Ucieczki).
- **Automatyczne sumowanie i ranga** — w odróżnieniu od Profilu sensorycznego
  w tej samej serii, **nie zamieniłam tego na wpis ręczny**, bo formuła jest
  w źródle w pełni udokumentowana i przejrzysta: suma ocen 0–3 z 5 pozycji na
  funkcję (0–15 pkt), progi z legendy (11–15 wyraźna funkcja, 6–10
  umiarkowana, 0–5 nieistotna) — to nie jest niewiadomego pochodzenia wzór, to
  prosta, jawna suma. Kliknięcie kółka 0–3 przy dowolnej pozycji przelicza na
  żywo: Σ przy nagłówku funkcji w arkuszu, tabelę Punktacji, plakietkę w
  karcie syntezy, wykres słupkowy, mapę radarową i „Funkcję dominującą".
- **Cała treść Syntezy** (charakterystyka + zalecenia PBS + cel SMART + tor/
  rodzaj zajęć) dla wszystkich 5 funkcji, słowo w słowo.
- **Podstawa prawna** — łącznie z cytatem „Standardy Ochrony Małoletnich
  (Dz.U. 2023 poz. 1606)", którego nie ma w innych drukach tej serii (dodany
  tu, bo dotyczy bezpośrednio postępowania z zachowaniami trudnymi).

## Co zmienione przy przebudowie

- **System szablonów** — z `<section class="sheet roomy/autofill">` na
  `.page`/`.phead`/`.pmeta`/`.pbody`/`.pfoot` (`base_css.html`), z prawdziwym
  logo PCTP (zaszytym już we wspólnym pliku CSS) zamiast tekstowego „PCTP".
- **8 stron → 4 strony.** Test w innym systemie mieścił średnio 1–1,5 funkcji
  na stronę; w nowym, bardziej przestronnym nagłówku rodziny (phead+pmeta)
  to zostawiało 280–600px pustego miejsca na niektórych stronach. Scaliłam:
  wszystkie 25 pozycji kwestionariusza na 2 stronach (3 funkcje + 2 funkcje),
  Punktacja + Hipoteza funkcji na jednej stronie (jak w oryginalnym układzie
  autorki), Wykres na jednej, Synteza + Monitorowanie na jednej. Treść bez
  zmian — wyłącznie gęstszy układ.
- **Naprawiony brakujący fragment.** W przesłanym `.html` synteza funkcji V
  (Regulacja emocjonalna) była upchnięta na tej samej stronie co sekcja
  Monitorowanie, mimo że nagłówek strony sugerował osobną „część 3 z 3" — tu
  każda z 5 kart syntezy ma swoje w pełni czytelne miejsce.
- **Naprawiony błąd w kolorowych plakietkach syntezy.** W trakcie testowania
  interaktywności znalazłam błąd, którego przesłany plik jeszcze nie miał
  ujawnionego: JS ustawiał tło plakietki na pełny kolor (czerwony/pomarańczowy/
  zielony), ale nie zmieniał koloru tekstu — po kliknięciu jakiegokolwiek
  kółka oceny tekst plakietki („15/15 · Wyraźna funkcja") stawał się
  niewidoczny (tego samego koloru co tło). Poprawione — plakietka zawsze ma
  biały tekst na kolorowym tle, statycznie i po każdym przeliczeniu.
- **Dodana synchronizacja metryczki między stronami** (`syncMeta`) — bez niej
  pola „Dotyczy ucznia/Klasa/Data" trzeba by wpisywać osobno na każdej z 4
  stron. Sprawdzone działanie: wpisanie imienia na str. 1 pojawia się od razu
  na str. 2–4.

## Struktura (4 strony)

| Strona | Zawartość |
|---|---|
| str. 1 | Tytuł, „O narzędziu", Metryczka (I), Arkusz kwestionariusza (II) — skala ocen + funkcje I–III (15 pozycji) |
| str. 2 | dokończenie arkusza — funkcje IV–V (10 pozycji), Punktacja i ranga (III), Hipoteza funkcji i kierunek PBS (IV) + podpisy + podstawa prawna |
| str. 3 | Wykres profilu (V) — słupkowy + radarowy + szybki odczyt + suma wszystkich funkcji |
| str. 4 | Synteza — charakterystyka/zalecenia/cel SMART dla 5 funkcji (VI), Monitorowanie i ewaluacja planu PBS (VII) + podpisy |

## Zweryfikowane

- Brak przepełnień stron (margines do stopki 6–59px na wszystkich 4 stronach)
  i brak nadmiaru pustego miejsca.
- Zero błędów JS w konsoli.
- Interaktywność sprawdzona automatycznie: kliknięcie kółka oceny poprawnie
  przelicza sumę funkcji, rangę, plakietkę w Syntezie, wysokość słupka
  wykresu i „Sumę wszystkich funkcji"; checkbox w Monitorowaniu przełącza się;
  pola metryczki są edytowalne i synchronizują się między stronami.

Dokument nie jest jeszcze przeniesiony do `Zatwierdzone/` — czeka na Twoje
potwierdzenie punktów wyżej, zwłaszcza podziału na 4 strony (w miejsce 8/10)
i decyzji o zachowaniu automatycznego sumowania.
