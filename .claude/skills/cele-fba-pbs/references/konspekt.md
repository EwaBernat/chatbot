# Konspekt zajęć — wzór KC-3

75 konspektów: **25 wskaźników × 3 wersje wiekowe**. Jeden konspekt obsługuje
**trzy poziomy wsparcia** — poziom zmienia sekcję VI, nie scenariusz. To nie jest
oszczędność: nauczyciel prowadzi te same zajęcia i modyfikuje je w biegu, kiedy
widzi, że dziecko nie daje rady.

## Rdzeń i wariant

Treść leży w pięciu modułach po jednym na funkcję (`konspekty_fba_1.py` …
`_5.py`), a `konspekty_fba.py` je scala.

**`RDZEN[nr]`** — wspólne dla trzech wersji wiekowych:

| pole | co to |
|---|---|
| `tytul` | tytuł zajęć, ten sam w A, B i C |
| `icf`, `pp` | kod ICF i punkt podstawy 2026 |
| `rodzaj` | rodzaj zajęć (sekcja V) |
| `metody`, `pomoce` | listy do sekcji II i III |
| `wskazowka` | jedno zdanie dla prowadzącego |
| `ter_kryt` | kryterium celu terapeutycznego |
| `R` | rozpisanie SMART celu terapeutycznego |
| `mod` | modyfikacje dla p3 / p2 / p1 (sekcja VI) |
| `arkusz` | materiał do wydruku |

**`WARIANTY[(nr, wersja)]`** — to, co wynika z wieku: `podtytul`, `ter` (cel
terapeutyczny), `S`, `A`, `pomoc_wiek` i `przebieg` — pięć par N/D.

Ten podział ma sens praktyczny: poprawka w metodzie wchodzi raz i dotyczy trzech
wersji, a przebieg zajęć trzylatka i sześciolatka i tak musi być inny.

## Przebieg N/D

Pięć par: co robi **nauczyciel (N)** i jaka jest oczekiwana **reakcja dziecka
(D)**. Nie „dziecko powinno" — to, co da się zobaczyć i policzyć. Kolumna D jest
tym, na co potem patrzy arkusz obserwacji, więc czasownik ma być obserwowalny:
*poda kartę*, *usiądzie*, *powie „poproszę"* — nie *zrozumie*, *będzie gotowe*.

## Jak konspekt się otwiera

* **kliknięciem celu w tabeli** — pokazuje ten jeden poziom, wyróżnia jego
  modyfikację;
* **z wykazu nad tabelą** — pokazuje wszystkie trzy cele i wszystkie modyfikacje,
  bo nauczyciel nie kliknął żadnej komórki.

Wykaz układamy **siatką z podziałem na funkcje**, nie rzędem pigułek: pigułka ma
szerokość swojego tytułu, więc kolumny nie trzymają pionu. Wykaz schowany pod
szarą belką nauczyciel przeoczy — to już raz zdarzyło się w tym projekcie,
dlatego pasek rozwijania jest w kolorze akcentu.

Cel edukacyjny konspekt czyta **na żywo z tabeli**, do trzech wariantów `.kvar`
wypełnianych przy starcie dokumentu. Wypełnianie przy starcie, a nie przy
kliknięciu, jest konieczne: bez tego wydruk całego zeszytu wychodził z pustym
celem i etykietą „Poziom III" przy każdym konspekcie.

## Arkusz — materiał do wycięcia

Sekcja VII, druga kartka konspektu. Siedem rodzajów: `karty` (do wycięcia),
`pasek` (sekwencja z numerami), `tablica` (bez rozcinania), `tabela` (do
wypełniania), `pola` (puste pola z etykietami), `etykiety` (karteczki z polem
koloru), `sciezki` (pasy do przecięcia albo szlaczki).

Symbole biorą się z **biblioteki banku KPOF** — `symbole_fba.py` mapuje karty
i paski na jej kody. Symbol nienarysowany nie ma pliku, a arkusz go używający
jest po cichu pomijany; `sprawdz_fba.py` to wyłapuje. Gdy brakuje symbolu,
dorysuj go **do biblioteki KPOF**, nie do tego modułu — inaczej dziecko zobaczy
w planie dnia inny obrazek niż na karcie z zajęć i symbol przestanie być słowem.

Arkusz `tabela` musi mieć `min-width:0`: tabela celów ma `min-width:1080px`
i bez tego wyjątku arkusz ucieka poza krawędź strony.

## Druk

Konspekty drukują się **pionowo**, mimo że tabela wokół nich jest pozioma
(`@page kon`). Scenariusz na jednej kartce, karta pomocy i arkusz na następnych.
Przycisk w wykazie drukuje cały zeszyt wersji — 25 konspektów.

```bash
node src/zmierz_konspekty.mjs
```

Budżet **1091 px** przy skali 0.96. Skala to zapas na fonty: pomiar leci na
Arialu (bez sieci), DM Sans jest odrobinę wyższy. Przekroczenie budżetu nie
zgłasza błędu — konspekt pęka w pół tabeli przebiegu.

Zeszyty muszą **cofać u siebie** regułę `@media print{.kmodal{display:none}}`,
inaczej cały zeszyt wychodzi z drukarki jako jedna pusta strona.

## Po dopisaniu konspektu

```bash
python3 src/build_tabela.py
node src/zmierz_konspekty.mjs
python3 ../.claude/skills/cele-fba-pbs/scripts/sprawdz_fba.py
```

Numeracja wskaźników w modułach treści musi zgadzać się z tabelą (`I.1`–`V.5`,
per funkcja). Rozjazd — konspekty numerowane ciągiem 1–25 zamiast per funkcja —
kosztował już jedno skryptowe przenumerowanie pięciu plików.
