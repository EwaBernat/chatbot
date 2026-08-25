---
name: mala-filozofia-broszura
description: 'Tworzy kompletną broszurę serii „Mała Filozofia" — 60-stronicową makietę A4 dla młodzieży w spektrum autyzmu: opowiadanie o filozofie w dwunastu rozdziałach (dokładnie 450 zdań), 60 pytań, infografiki, znak serii, znak wydawcy PCTP i załącznik z grą planszową (plansza, dwie kostki do sklejenia, karty, żetony). Na wyjściu HTML do publikacji, HTML z osadzonymi krojami i gotowy PDF do druku. Użyj ZAWSZE, gdy pojawia się prośba o kolejny tom serii „Mała Filozofia", o broszurę albo książeczkę o filozofie (Platon, Sokrates, Epiktet, Marek Aureliusz, Diogenes, Hypatia i inni), o materiał o emocjach dla młodzieży z autyzmem lub spektrum, o broszurę z pytaniami do samodzielnej pracy, o grę planszową o emocjach, a także przy hasłach „450 zdań", „60 pytań", „12 spotkań", „dwanaście emocji", „makieta A4 do druku", „broszura PCTP", „tom drugi", „nowy tom". Wyzwalaj też przy prośbach o poprawki w istniejącej broszurze serii: dopisanie rozdziału, wymianę cytatów, podmianę logo, nową grę, przeliczenie paginacji.'
---

# Broszura serii „Mała Filozofia"

## Co to jest

Seria książeczek, w których młodzież w spektrum autyzmu poznaje jednego filozofa i przez
jego myśli uczy się nazywać własne emocje. Każdy tom ma tę samą, przewidywalną budowę —
i to jest jego najważniejsza cecha, nie ozdobnik. Czytelnik, który przeszedł tom pierwszy,
otwiera drugi i od razu wie, gdzie co jest.

Tom pierwszy — „Spotkanie z Arystotelesem" — leży w `assets/tresc-arystoteles.json`.
To kompletny, działający przykład. Zajrzyj do niego przy każdej wątpliwości: łatwiej
zobaczyć, jak wygląda dobre zdanie z sekcji „Emocja", niż przeczytać o tym regułę.

## Jak to działa

Skład jest w skryptach, treść w jednym pliku JSON. Dzięki temu nowy tom to praca
pisarska i redakcyjna, a nie dłubanie w kodzie. Nigdy nie edytuj HTML-a ręcznie —
przy następnym uruchomieniu `build.py` zmiany znikną.

```
python3 scripts/build.py   tresc.json  [katalog]   # składa broszura.html
python3 scripts/druk.py                [katalog]   # osadza kroje → do-druku.html + PDF
python3 scripts/sprawdz.py tresc.json  [katalog]   # kontrola treści i łamania stron
```

Uruchamiaj `sprawdz.py` po każdej zmianie treści. Makieta ma sztywne strony 210×297 mm,
więc nadmiar tekstu nie przenosi się na następną stronę — zostaje ucięty po cichu.
Skrypt mierzy każdą z 60 stron w przeglądarce i mówi, która się przelewa i o ile.

## Kontrakt serii

Te liczby nie są ozdobne — na nich opiera się paginacja. Zmiana którejkolwiek rozsypuje
makietę, a `sprawdz.py` ją zablokuje.

| Element | Ile | Dlaczego akurat tyle |
|---|---|---|
| Rozdziałów | 12 | 3 strony na rozdział = 36 stron środka |
| Zdań w rozdziale | 14 + 10 + 7 + 6 = 37 | tyle mieści się na trzech stronach bez ścisku |
| Zdań we wstępie | 6 | 12 × 37 + 6 = **450 zdań** |
| Pytań | 5 na rozdział = **60** | numeracja biegnie ciągiem 1–60 przez całą książeczkę |
| Stron | 60 | 15 arkuszy — oprawa zeszytowa wymaga wielokrotności 4 |

Jedno zdanie w JSON-ie to naprawdę jedno zdanie. Dwa sklejone w jednym wpisie psują
rytm akapitów (składane po 3–4) i `sprawdz.py` je zgłosi.

### Rytm rozdziału

| Strona | Zawartość |
|---|---|
| A | otwarcie (numer, tytuł, emocja) · ilustracja · **① Scena** — 14 zdań |
| B | cytat filozofa · **② Myśl** — 10 zdań · **③ Emocja** — 7 zdań |
| C | **④ W Twoim życiu** — 6 zdań · **⑤ Pięć pytań** · miejsce na własną odpowiedź |

Rozdział, który ma w danych tabelę (`tabela`), oddaje jej miejsce linii do pisania
na stronie C. Obie rzeczy naraz się nie mieszczą.

## Jak pisać

To najtrudniejsza część i decyduje o wartości broszury. Zanim napiszesz pierwsze zdanie,
przeczytaj `references/pisanie-tekstu.md` — są tam reguły języka, budowa każdej sekcji
i przykłady zdań dobrych i złych. W skrócie, żeby mieć to przed oczami:

- **Dosłownie.** Bez ironii, bez przenośni bez wyjaśnienia, bez pytań podchwytliwych.
- **Emocje przez własne ciało**, nie przez cudzą mimikę: „ściśnięty żołądek", a nie
  „widzisz, że ktoś jest smutny". Rozpoznawanie uczuć zaczyna się od sygnałów z siebie.
- **Bez form zakładających płeć** albo w obu wariantach: „chciał lub chciała".
- **Krótkie zdania**, jedna myśl w zdaniu, do jakichś 145 znaków.
- **Szczególne zainteresowania są zaletą**, nie objawem. Tom pierwszy mówi to wprost
  w rozdziale o ośmiornicy i to jest jeden z najważniejszych fragmentów całej serii.

## Wybór filozofa i dwunastu emocji

Zacznij od emocji, nie od biografii. Wybierz dwanaście uczuć, które naprawdę spotykają
nastolatka w ciągu roku szkolnego, ułóż je od najłatwiejszych do najtrudniejszych,
a dopiero potem szukaj w życiu filozofa scen, które do nich pasują. Odwrotna kolejność
daje suchy życiorys z doklejonymi emocjami.

Tom pierwszy prowadzi tak: ciekawość → niepewność → napięcie sporu → zachwyt → duma →
ulga → strach → zniechęcenie → samotność → gniew → nadzieja → smutek i wdzięczność.
Zaczyna się lekko, najtrudniejsze rzeczy są w środku, a kończy się na czymś, co daje siłę.
Ten łuk warto powtórzyć.

Sceny mają być **prawdziwe**: daty, miejsca, tytuły dzieł, znane anegdoty. Dialogi wolno
dopisać — trzeba to tylko uczciwie zaznaczyć w nocie o cytatach na stronie 50. Podobnie
z cytatami: rozdziel te z zachowanych dzieł od tych tylko przypisywanych. Broszura idzie
do sprzedaży, więc rzetelność źródeł chroni wydawcę.

## Struktura pliku z treścią

Pełny opis każdego pola: `references/struktura-danych.md`. Najszybsza droga do nowego tomu:

```bash
cp assets/tresc-arystoteles.json tresc-platon.json   # i przepisz treść
```

Kopiowanie działającego tomu jest lepsze niż start z pustego szablonu
(`assets/tresc-szablon.json`), bo od razu widać oczekiwaną długość i ton każdego pola.

## Ilustracje

Rysunki są w danych, jako kod SVG w polu `svg` każdego rozdziału. Osiem infografik
generują skrypty z danych (oś czasu, termometr, karta emocji, plansza, kostki, żetony) —
tych nie trzeba rysować. Do narysowania zostają sceny rodzajowe, po jednej na rozdział.

Zasady, żeby pasowały do reszty:

- `viewBox="0 0 640 190"` dla scen, płaska grafika liniowa, bez cieni i gradientów.
- Kolory **wyłącznie** przez zmienne: `var(--morze)`, `var(--szafran)`, `var(--oliwka)`,
  `var(--glina)`, `var(--papier-2)`, `var(--karta)`, `var(--linia)`, `var(--atrament)`.
  Wpisany na sztywno kolor rozjedzie się z paletą, a nieistniejąca zmienna daje czarne tło.
- Grubości kresek 3–4, zaokrąglone końce. Podpisy w SVG minimum 15 jednostek.
- Zawsze `role="img"` i `aria-label` — to jedyny opis rysunku dla kogoś, kto go nie widzi.

Infografiki rozdziałowe (jak waga złotego środka) trzymaj też w polu `svg`, ale dodaj
`fig_etykieta` — wtedy dostają pełną szerokość kolumny zamiast wyśrodkowanej winiety.

## Gra w załączniku

Osiem stron na końcu (52–59). Mechanika jest wspólna dla całej serii i nie wymaga zmian:
kostka miary łączy ruch z nauką o właściwej mierze, kostka emocji obsługuje pola z wieńcem,
karty zadają pytania. Do napisania zostaje dwanaście kart (`gra.karty`) i sześć ścian
kostki emocji (`gra.kostka_emocji`).

Gra jest **kooperacyjna i to jest projektowa decyzja, nie przeoczenie**: nikt nie wygrywa,
„pas" jest ruchem zgodnym z zasadami, a pole PRZERWA to pełnoprawny ruch. Rywalizacja
i presja czasu wykluczyłyby część odbiorców, dla których ta broszura powstaje.
Jeśli ktoś prosi o punktację i zwycięzcę — powiedz, dlaczego jej tu nie ma, i zaproponuj
wariant, w którym każdy zbiera własne listki bez porównywania.

## Znaki

`assets/logo/` zawiera znak serii („Mała Filozofia" — pytajnik w otwartym wieńcu, wersje
kolorowa i mono, pozioma i pionowa, napis w krzywych) oraz znak wydawcy PCTP.
`build.py` wciąga je z tego katalogu i zamienia kolory serii na tokeny palety.
Podmiana logo = nadpisanie pliku pod tą samą nazwą i ponowny build.

Znak PCTP w `assets/logo/pctp-logo.svg` jest **odrysowaniem**, nie oryginałem.
Przed drukiem trzeba go podmienić na plik od wydawcy — warto o tym przypomnieć.

## Druk

Szczegóły w `references/sklad-i-druk.md`. Najważniejsze: A4, marginesy lustrzane
24/18 mm, tekst Atkinson Hyperlegible 12 pt, papier matowy 120–150 g, spady 3 mm
dodaje drukarnia. Strony do wycinania (plansza, kostki, karty) proszą się o 170–200 g —
warto zaproponować dodruk samego załącznika na grubszym papierze.

## Kiedy coś nie gra

| Objaw | Przyczyna | Co zrobić |
|---|---|---|
| „Strona N przelewa się o X px" | za dużo treści na sztywnej stronie | skróć zdania w tej sekcji albo zmniejsz grafikę (`max-width` w `styl.css`) |
| Czarne tło ilustracji | SVG używa zmiennej, której nie ma w palecie | sprawdź nazwy `var(--…)` — lista w `references/sklad-i-druk.md` |
| PDF bez właściwych krojów | Chromium nie objął kroju zmiennego | używaj tylko Alegreya Sans i Atkinson Hyperlegible — są statyczne |
| „Pobrano tylko N krojów" | Google Fonts oddało TTF zamiast woff2 | to kwestia nagłówka UA w `druk.py`; sprawdź połączenie |
| Liczba stron ≠ 60 | zmieniona liczba rozdziałów lub stron dodatków | oprawa zeszytowa wymaga wielokrotności 4 — dodaj lub ujmij strony notatek |

## Czego nie zmieniać bez rozmowy z zamawiającym

Stopień pisma poniżej 12 pt, justowanie tekstu, emocje opisane cudzą mimiką, rywalizacja
w grze, zmienna kolejność sekcji w rozdziale. To nie są decyzje estetyczne, tylko
dostępnościowe — każda z nich odcina część odbiorców, dla których ta seria istnieje.
