# Ilustracje

Wszystkie rysunki są wektorami SVG generowanymi przez `scripts/broszura/svg.py` i osadzanymi
w pliku HTML. Nie ma zewnętrznych obrazów — broszura zostaje jednym plikiem, a rysunki
skalują się bez pikselizacji w druku.

## Paleta

Zieleń od `#06281E` (najciemniejsza) do `#E8F5EF` (tło), akcenty: złoto `#E3B23C`,
róż `#D96D8B`, piasek `#F3E7C9`. Słownik `svg.C` — używaj go zamiast wpisywać kolory ręcznie.

## Ikony rozdziałów — `rozdzial.ikona`

Okrągła ikonka w nagłówku, obowiązkowa. Dostępne nazwy:

`plane` `sheep` `question` `asteroid` `baobab` `sun` `thorn` `rose` `volcano` `crown`
`hat` `bottle` `coins` `lamp` `book` `earth` `snake` `flower3` `echo` `garden` `fox`
`train` `pill` `walk` `well` `star` `letter`

Mimo pochodzenia z „Małego Księcia” większość jest ogólna i przenosi się na inne lektury:
`crown` (władza), `coins` (pieniądze), `book` (nauka, dokument), `train` (podróż),
`letter` (list, wiadomość), `walk` (wędrówka), `lamp` (praca, czuwanie), `bottle`
(uzależnienie), `star` (marzenie, finał), `question` (zagadka), `earth` (świat, miasto),
`garden` (dom, ogród), `well` (nadzieja, znalezienie), `sun` (upływ czasu).

Nie znajdujesz odpowiednika? Weź najbliższą znaczeniowo — spójność ikon w całej broszurze
jest ważniejsza niż dosłowność pojedynczej.

## Duże ilustracje — `rozdzial.ilustracja`

Rysunek na stronie 1 rozdziału, `viewBox="0 0 200 160"`. Gotowe funkcje:

`sheep_box` `baobabs` `sunsets` `rose` `fox` `snake` `rose_garden` `well` `stars_laugh`

**Daj 8–10 na całą broszurę**, przy kluczowych scenach. Ilustracja przy każdym rozdziale
przestaje cokolwiek znaczyć i wypycha treść na kolejną stronę.

## Grafiki narzędziowe — rysują się same

`thermometer` (termometr emocji — wersja zwarta do części B), `thermometer_cut` (ten sam
termometr do wycięcia, z osobnym paskiem wskaźników), `tom_ladder` (schody teorii umysłu),
`board` (plansza gry 30 pól), `stage` (scena teatralna), `logo_pctp` (logo wydawcy).
Są niezależne od lektury.

Termometr opisuje każdy stopień na cztery niezależne sposoby: kolorem, wysokością słupka,
miną i liczbą kropek. Uczeń, który nie czyta, korzysta z trzech ostatnich — słowo jest wtedy
podpowiedzią dla dorosłego. Nie usuwaj żadnego z tych czterech kanałów.

## Sceny — rysunek zamiast zdjęcia

Nazwy kończące się na `_scena` to płaskie rysunki w proporcji 200×96. Silnik nadaje im
klasę `scena` i szerokość 80 mm (zamiast 54 mm dla rysunków kwadratowych) — inaczej gubią się
na stronie. Gdy strona jest pełna, ustaw w rozdziale `"ilustracja_waska": true`, a scena
wróci do 54 mm.

Sceny rozdziałowe: `boa_kapelusz_scena` (rysunek nr 1 i nr 2), `samolot_scena` (awaria
na pustyni), `asteroida_scena` (planeta i liczby), `kwiat3_scena` (kwiat o trzech płatkach),
`noc_pustynia_scena` (nocna wędrówka), `gwiazdy_smiech_scena` (gwiazdy, które się śmieją).

Sceny na karty (działają też w rozdziałach): `geograf_scena`, `ziemia_scena`,
`studnia_scena`, `gora_echo_scena`, `sklep_pigulki_scena`.

## Sceny na karty do wycięcia

`geograf_scena`, `ziemia_scena`, `studnia_scena`, `gora_echo_scena`, `sklep_pigulki_scena`
— rysowane w proporcji paska karty (viewBox 200×96), płaskim rysunkiem, nie akwarelą.
Używaj ich dla kart, dla których nie ma zdjęcia: karta z samą ikoną na tle planety wygląda
przy fotografiach jak brak, a nie jak wybór. Postacie rysuj z profilu (`_postac_profil`)
— przy tej wielkości twarz na wprost robi się nieczytelna.

## Zdjęcia i grafiki rastrowe

Oprócz rysunków wektorowych można wstawiać gotowe pliki: **PNG, JPEG, WebP, GIF, SVG**.

- `meta.okladka_obraz` — zdjęcie na okładkę (przycinane do pasa u góry strony)
- `rozdzial.obraz` — zdjęcie zamiast rysunku wektorowego na stronie 1 rozdziału

```json
"meta":  { "okladka_obraz": "grafiki/okladka.png" },
"rozdzialy": [ { "nr": 2, "obraz": "grafiki/pustynia.jpg" } ]
```

Ścieżki są względne wobec katalogu pliku JSON albo wobec katalogu podanego w `--grafiki`.
Pole `obraz` ma pierwszeństwo przed `ilustracja` — dzięki temu można podmienić pojedynczy
rysunek na zdjęcie, nie ruszając reszty danych.

Obrazy trafiają do HTML jako `data:` URI, żeby broszura pozostała jednym plikiem. Ma to cenę:
**plik rośnie o mniej więcej 1⁄3 rozmiaru zdjęcia**. Przy kilkunastu zdjęciach warto je najpierw
zmniejszyć — do druku A4 wystarcza szerokość około 1600 px, a na okładkę 2000 px.

Proporcje czytane są z nagłówka pliku, bez żadnej biblioteki (`scripts/broszura/obrazy.py`).
Jeśli formatu nie da się zmierzyć, skład zatrzymuje się z czytelnym błędem — to celowe,
bo brakująca proporcja rozjeżdża stronę przy druku.

**Prawa do grafik.** Do materiału firmowanego przez placówkę używaj wyłącznie zdjęć własnych,
z domeny publicznej, na wolnej licencji albo wygenerowanych przez siebie. Rysunki samego
Saint-Exupéry'ego są w Polsce w domenie publicznej od 2015 roku (70 lat od śmierci autora),
ale współczesne ilustracje innych artystów już nie.

## Własny rysunek

Wstaw inline SVG bezpośrednio w pole `ilustracja` albo `okladka_svg`.

**Ilustracja rozdziału** — `viewBox="0 0 200 160"`, jasne tło `#E8F5EF` albo ciemne `#0B3D2E`,
płaska grafika bez cieni, grubość konturu 2–2.6.

Domyślną okładką (gdy `meta.okladka_svg` jest puste) jest `cover_neutral` — otwarta książka
z unoszącymi się gwiazdami, niezwiązana z żadną lekturą. To poprawny zapas, ale nie docelowa
okładka: do konkretnej książki napisz własny rysunek. `cover` to okładka „Małego Księcia” —
nie używaj jej do innej lektury.

**Okładka** — `viewBox="0 0 420 300"`, ciemne tło, atrybut
`preserveAspectRatio="xMidYMax slice"` (skład kadruje ją do pasa ~47% wysokości strony,
więc kompozycja musi trzymać się dolnej części). Dodaj `role="img"` i `aria-label`.

Zawsze podaj `viewBox` — z niego liczone są proporcje pudełka. Bez tego strona rozjedzie się
przy druku.

## Dopisanie funkcji do biblioteki

Dopisz funkcję w `svg.py` zwracającą string z `<svg viewBox=...>` i użyj jej nazwy w JSON-ie.
Nowe ikony dodaje się do słownika `P` wewnątrz `icon()` — każda to jedno koło `r="30"`
w `viewBox="0 0 64 64"` plus prosty znak w środku.
