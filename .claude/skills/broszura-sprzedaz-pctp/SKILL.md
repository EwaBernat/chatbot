---
name: broszura-sprzedaz-pctp
description: "Przygotowuje broszurę lub poradnik PCTP Koszalin do SPRZEDAŻY — składa PDF wierny wersji HTML (osadzone kroje marki, poprawne marginesy A4, metadane, zakładki nawigacyjne), dokłada stronę licencyjną, próbkę bezpłatną, załączniki do druku, okładkę jako obraz oraz egzemplarze imienne ze znakiem wodnym, a na końcu proponuje cenę. Użyj ZAWSZE, gdy Mirosława Jurczyszyn mówi: „przygotuj broszurę do sprzedaży\", „popraw PDF\", „PDF wygląda inaczej niż HTML\", „PDF ma złe marginesy\", „brakuje fontów w PDF\", „zrób próbkę\", „wyznacz cenę broszurki\", „znak wodny\", „licencja do broszury\", „czego brakuje w broszurze\", a także gdy prosi o eksport gotowej broszury HTML do pliku PDF, o wersję do druku albo o materiały na stronę sprzedażową. Wyzwalaj również przy diagnozie samego PDF-u: ucięte marginesy, złe kroje pisma, nadmiarowe puste strony, nieklikalny spis treści."
---

# Broszura PCTP do sprzedaży

Ten skill zamienia gotową broszurę w HTML w komplet plików, które da się sprzedać:
poprawny PDF, próbkę, załączniki i egzemplarze imienne. Powstał z realnej pracy nad
poradnikiem o echolalii, więc zawiera rozwiązania konkretnych problemów, które przy
tym wyszły — a które przy składaniu PDF-u z HTML wracają za każdym razem.

Źródłem prawdy jest **jeden plik HTML** ze stronami A4 (`<div class="page">`).
Wszystko inne z niego wynika, więc poprawki wprowadzaj w HTML-u, nigdy w PDF-ie.

## Zanim zaczniesz

Sprawdź, czego brakuje w środowisku:

```bash
python3 -c "import pymupdf" 2>/dev/null || pip install --quiet pymupdf
node -e "require('playwright')" 2>/dev/null || npm install --silent playwright
```

Ścieżkę do przeglądarki podaj w `CHROMIUM_PATH`, jeśli nie leży w domyślnym miejscu.

## Przebieg

Kolejność ma znaczenie — każdy krok zakłada, że poprzedni się udał.

### 1. Sprawdź układ przed składaniem

```bash
node scripts/sprawdz_uklad.js broszura.html
```

Zwraca liczbę stron oraz listę stron pustych, przepełnionych, bez stopki
i niezgodności numeracji ze spisem treści. **Nie składaj PDF-u, dopóki wynik nie
jest czysty** — poprawianie tego później oznacza powtarzanie wszystkich kroków.

Gdy strony są przepełnione albo mają wielkie luki, użyj `scripts/przepakuj.js OD DO`,
który ciasno rozkłada bloki w podanym zakresie stron, pilnując, by nagłówek nie
został sam na dole. Po każdej zmianie liczby stron uruchom `scripts/numeruj.js` —
przelicza numery w stopkach i w spisie treści na podstawie faktycznego układu.

### 2. Zbuduj wersję do druku

```bash
python3 scripts/osadz_fonty.py broszura.html Broszura_DRUK.html "Pełny tytuł publikacji"
```

Skrypt pobiera **statyczne** kroje marki (Fraunces, DM Sans, JetBrains Mono),
osadza je w pliku jako `data:` URI, usuwa odwołania do Google Fonts i ogranicza
reguły wąskiego ekranu do `@media screen`. Powstaje plik samowystarczalny —
wygląda tak samo bez dostępu do sieci.

Dwie rzeczy, które ten krok naprawia, opisuje `references/pulapki_pdf.md`.
Przeczytaj ten plik, jeśli PDF mimo wszystko odbiega od wersji ekranowej —
zawiera cztery gotowe sprawdzenia diagnostyczne w kolejności od najczęstszej
przyczyny.

### 3. Złóż PDF

```bash
node scripts/zloz_pdf.js Broszura_DRUK.html Broszura_DRUK.pdf
```

Skrypt czeka na `document.fonts.ready` i przerywa pracę, jeśli żaden krój się
nie załadował — lepiej dostać błąd niż odkryć podmianę fontów po wysłaniu pliku
klientowi.

### 4. Zweryfikuj PDF, zanim pójdzie dalej

To jedyny moment, w którym łatwo wychwycić błędy niewidoczne w HTML-u:

```python
import pymupdf
d = pymupdf.open('Broszura_DRUK.pdf'); MM = 72/25.4
print('stron:', d.page_count)                       # ma się zgadzać z liczbą .page
for n in (1, 5, 20):
    w = d[n].get_text('words')
    print('str %d — góra %.1f mm, boki %.1f mm'
          % (n+1, min(x[1] for x in w)/MM, min(x[0] for x in w)/MM))
print('kroje:', sorted({f[3] for n in range(d.page_count) for f in d[n].get_fonts()}))
```

Marginesy muszą odpowiadać `padding` strony w CSS. Nazwy w rodzaju
`LiberationSerif` przy tekście ciągłym oznaczają, że krok 2 się nie powiódł.

### 5. Zbuduj komplet sprzedażowy

```bash
node scripts/struktura.js Broszura_DRUK.html      # mapa rozdziałów na strony
python3 scripts/zbuduj_sprzedaz.py Broszura_DRUK.pdf
```

Powstają: PDF główny z metadanymi i zakładkami nawigacyjnymi, próbka bezpłatna,
załączniki do druku wycięte jako osobne pliki A4, okładka jako obraz oraz zrzuty
stron na stronę sprzedażową.

Wycinanie załączników opiera się na wyszukaniu frazy występującej **wyłącznie**
na docelowej stronie. Frazy typu tytuł materiału trafiają najpierw do spisu treści —
dlatego szukaj po treści wnętrza (np. „Możliwe wartości" zamiast „Arkusz obserwacji").

### 6. Egzemplarze imienne

```bash
python3 scripts/znak_wodny.py "Anna Kowalska · anna@szkola.pl" "indywidualna" 2026-09-01
```

Dyskretna linia w stopce z danymi nabywcy i powtarzalnym numerem egzemplarza.
Nie utrudnia czytania ani druku, a pozwala ustalić źródło pliku udostępnionego
niezgodnie z licencją. Numer zanotuj przy zamówieniu.

## Strona licencyjna

Płatna publikacja potrzebuje osobnej strony z prawami autorskimi — nie wystarczy
zdanie na okładce. Wzór, który się sprawdził, ma pięć elementów: nota `©`
z rokiem i nazwiskiem, dane wydania i ISBN, dwie kolumny „co wolno / czego nie
wolno", opis rodzajów licencji oraz informacja o znaku wodnym.

Miejsca do uzupełnienia przez autorkę (e-mail, ISBN) oznaczaj widocznie —
klasa `.doUzup` w broszurze o echolalii renderuje je jako pomarańczową plakietkę,
której nie da się przeoczyć przed publikacją. Nie wstawiaj w to miejsce danych
osobowych bez wyraźnej zgody — publikacja trafia do obcych ludzi.

## Cena i braki

Gdy autorka pyta o cenę albo o to, czego jeszcze brakuje, przeczytaj
`references/gotowosc_handlowa.md`. Zawiera listę podzieloną na elementy
**blokujące sprzedaż** i **podnoszące cenę** (to różna pilność, więc nie mieszaj
ich w jednej liście) oraz widełki cenowe z punktami odniesienia z polskiego rynku.

Cenę podawaj jako konkretną liczbę z uzasadnieniem, nie jako przedział „to zależy".
Autorka potrzebuje decyzji, którą może wpisać w sklepie.

## Czego nie robić

**Nie poprawiaj PDF-u ręcznie.** Każda poprawka treści wraca do HTML-a, po czym
powtarzasz kroki 2–5. PDF jest produktem, nie źródłem.

**Nie zakładaj, że skoro wygląda dobrze na zrzucie ekranu, to PDF też jest dobry.**
Zrzuty robi ta sama przeglądarka w trybie ekranu — nie wykryją ani podmiany
krojów, ani reguły mobilnej działającej przy druku. Sprawdzenie z kroku 4 zajmuje
kilkanaście sekund i wychwytuje jedno i drugie.

**Nie dodawaj zdjęć bez ustalenia praw.** Do publikacji płatnej potrzebne są
własne fotografie, licencja komercyjna albo pisemna zgoda na wizerunek —
przy dzieciach od rodzica lub opiekuna. Grafiki wektorowe rysowane kodem tego
problemu nie mają i dlatego są domyślnym wyborem w tej serii.
