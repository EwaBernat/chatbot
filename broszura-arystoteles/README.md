# Spotkanie z Arystotelesem — seria „Mała Filozofia”, tom 1

Broszura edukacyjna dla młodzieży w spektrum autyzmu. Opowiadanie o życiu i ideach
Arystotelesa, prowadzące przez dwanaście emocji, z pytaniami do samodzielnej pracy.

**Format:** makieta książkowa A4, **60 stron**, druk dwustronny, oprawa zeszytowa
(60 = 15 arkuszy, liczba podzielna przez 4).

## Pliki

| Plik | Do czego służy |
|---|---|
| `broszura.html` | Wersja źródłowa (publikacja online). Kroje z Google Fonts. |
| `do-druku.html` | Wersja samodzielna: kroje osadzone w pliku, działa bez internetu. |
| `Spotkanie-z-Arystotelesem.pdf` | Gotowy plik do druku — A4, 60 stron. |
| `zrodla/` | Skrypty składu: treść w JSON + arkusz stylów + generator + grafiki gry. |
| `logo/` | Znak wydawcy PCTP i znak serii „Mała Filozofia” — SVG + PNG, opis w `logo/README.md`. |

Ponowne wygenerowanie całości:

```
python3 zrodla/build.py     # składa broszura.html z tresc.json + styl.css
python3 zrodla/druk.py      # osadza kroje → do-druku.html
# potem: otwórz do-druku.html w przeglądarce → Drukuj → Zapisz jako PDF (A4, marginesy: brak)
```

## Zawartość

- **450 zdań** opowiadania — liczba pilnowana przez skrypt składu.
- **60 pytań** — po 5 na rozdział, numerowane ciągiem 1–60.
- **8 infografik** + 7 ilustracji scenicznych (wektorowe SVG).
- Karta emocji do wycięcia, słowniczek, strona notatek, strona dla dorosłych.
- **Załącznik: gra planszowa** „Emocje według Arystotelesa” — plansza, dwie kostki
  do sklejenia, dwanaście kart z pytaniami, żetony, wersja dla jednej osoby.

## Paginacja

| Strony | Zawartość |
|---|---|
| 1 | Okładka |
| 2 | Strona tytułowa |
| 3 | Strona redakcyjna (metryka, ISBN, licencje krojów) |
| 4 | **Spis treści** z numerami stron |
| 5–8 | Wstęp: jak czytać · pięć części rozdziału · oś czasu życia · termometr emocji |
| 9–44 | Dwanaście spotkań, po 3 strony każde |
| 45–46 | Dwanaście zdań na dwanaście emocji (do wycięcia) |
| 47 | Moja karta emocji |
| 48 | Słowniczek |
| 49 | Jak pracować z broszurą (dla dorosłych) |
| 50 | Nota o cytatach i źródłach |
| 51 | Moje notatki |
| 52–59 | **Załącznik: gra „Emocje według Arystotelesa”** |
| 60 | Tylna okładka |

### Załącznik — gra

| Strona | Zawartość |
|---|---|
| 52 | O grze: dla kogo, ile osób, co potrzebujesz, co wytniesz |
| 53 | Zasady krok po kroku + zasady wsparcia |
| 54 | Plansza — dwadzieścia pól, z opisem trzech rodzajów pól |
| 55 | Kostka miary — siatka do wycięcia i sklejenia |
| 56 | Kostka emocji — siatka do wycięcia + osiemnaście żetonów |
| 57–58 | Dwanaście kart z pytaniami do wycięcia |
| 59 | Wersja dla jednej osoby + tabela do wypełnienia |

Gra jest **kooperacyjna: nikt nie wygrywa i nikt nie przegrywa**. „Pas” jest ruchem
zgodnym z zasadami i nie kosztuje nic. Kostka miary łączy ruch z nauką o złotym środku
ze spotkania siódmego: liczba mówi, o ile pól idziesz, a słowo — czy emocji było
za mało, właściwa miara, czy za dużo.

**Numeracja stron** biegnie w stopce od strony 4 do 51, przy zewnętrznej krawędzi
(na stronach nieparzystych po prawej, na parzystych po lewej). Okładki i strony
tytułowe pagin nie mają — tak jak w książce.

**Żywa pagina** (nagłówek): tytuł serii na jednej krawędzi, numer i tytuł bieżącego
rozdziału na drugiej.

### Rytm rozdziału — zawsze te same trzy strony

| Strona | Zawartość |
|---|---|
| A | Otwarcie (numer, tytuł, emocja) · ilustracja lub infografika · **① Scena** (14 zdań) |
| B | Cytat Arystotelesa · **② Myśl** (10 zdań) · **③ Emocja** (7 zdań) |
| C | **④ W Twoim życiu** (6 zdań) · **⑤ Pięć pytań** · miejsce na własną odpowiedź |

### Dwanaście spotkań

| Nr | Tytuł | Emocja | Strona |
|---|---|---|---|
| 1 | Chłopiec w domu lekarza | ciekawość | 9 |
| 2 | Pierwszy dzień w Atenach | niepewność | 12 |
| 3 | Nie zgadzam się z nauczycielem | napięcie sporu | 15 |
| 4 | Ośmiornica w porcie Lesbos | zachwyt | 18 |
| 5 | Lekcja dla trudnego ucznia | duma | 21 |
| 6 | Szkoła, w której się chodzi | ulga | 24 |
| 7 | Waga w środku | strach | 27 |
| 8 | Sto razy to samo | zniechęcenie | 30 |
| 9 | Trzy rodzaje przyjaciół | samotność | 33 |
| 10 | Gniew, który ma miarę | gniew | 36 |
| 11 | Jedna jaskółka | nadzieja | 39 |
| 12 | Ostatnia droga do Chalkis | smutek i wdzięczność | 42 |

## Znaki

- **PCTP** — znak wydawcy. Okładka (dół), strona tytułowa, strona redakcyjna, tylna okładka.
  Wersja w repozytorium jest **odrysowaniem** z przesłanego obrazka; przed drukiem
  podmień `logo/pctp-logo.svg` na oryginał (szczegóły w `logo/README.md`).
- **Mała Filozofia** — znak serii: pytajnik w otwartym wieńcu oliwnym. Okładka (góra),
  strona tytułowa, żywa pagina każdej strony rozdziału, tylna okładka. Dostępny
  w wersji kolorowej i jednokolorowej, poziomej i pionowej; napis zamieniony na krzywe.

## Skład i typografia

**Strony o stałym rozmiarze.** Każda strona to blok 210 × 297 mm — to, co widać
na ekranie, jest dokładnie tym, co wyjdzie z drukarki. Łamanie nie zależy od
ustawień przeglądarki. Skrypt kontrolny sprawdza każdą z 52 stron pod kątem
przepełnienia kolumny (obecnie: zero przepełnień).

**Marginesy lustrzane:** 24 mm przy grzbiecie, 18 mm od zewnątrz, 15 mm góra,
13 mm dół. Kolumna tekstu 152 mm ≈ 66 znaków w wierszu.

**Kroje i stopnie pisma**

| Rola | Krój | Stopień |
|---|---|---|
| Tekst główny | Atkinson Hyperlegible Regular | 12 pt / interlinia 1,62 |
| Nagłówki i liczby | Alegreya Sans ExtraBold | 1,1–3,5 em |
| Żywa pagina, etykiety | Alegreya Sans Medium, kapitaliki z rozstrzeleniem | 0,62–0,8 em |

**Poprawki typografii polskiej** (wykonywane automatycznie przy składzie):

- twarde spacje po wyrazach jednoliterowych (`a i o u w z`) — bez sierotek na końcach
  wierszy; w tym wydaniu jest ich 581,
- półpauza `–` zamiast pauzy `—` (norma polska),
- wielokropek jako jeden znak `…`,
- cudzysłowy drukarskie „ ",
- **tekst wyrównany do lewej, nie justowany** — justowanie tworzy nierówne odstępy
  między słowami, co utrudnia czytanie osobom z trudnościami w czytaniu,
- akapity po 3–4 zdania zamiast zdania w osobnej linii.

**Paleta**

| Rola | HEX | Gdzie |
|---|---|---|
| Papier | `#F7F4EC` | tło stron |
| Papier – cień | `#EDE8DC` | plansze ilustracji, karty |
| Atrament | `#1F2E33` | tekst |
| Morze egejskie | `#1E5A6B` | nagłówki, numery, cytaty |
| Szafran | `#B07E13` | linie akcentu, sekcja „W Twoim życiu” |
| Oliwka | `#5C7A49` | sekcja „Emocja” |
| Glina | `#A2563A` | sekcja „Pięć pytań” |

Każda z części rozdziału ma własny kolor **i własny kształt** (wypełnienie, pasek
z lewej, obwódka) — rozpoznaje się je także na wydruku czarno-białym.

## Dostępność dla czytelnika w spektrum

- Atkinson Hyperlegible (Braille Institute) — krój o łatwo rozróżnialnych literach,
  z przekreślonym zerem, 12 pt (powyżej typowego stopnia książkowego).
- Tło kość słoniowa zamiast bieli, tekst grafitowy zamiast czerni — mniej odbić
  i mniej twardego kontrastu.
- Struktura pięciu kroków powtarza się identycznie w każdym rozdziale.
- Emocje opisane przez **sygnały z własnego ciała**, nie przez mimikę innych osób.
- Język dosłowny: bez ironii, bez przenośni bez wyjaśnienia, bez pytań podchwytliwych.
- Formy gramatyczne neutralne płciowo albo podane w obu wariantach.
- Skala 0–10 wprowadzona raz (str. 8) i używana konsekwentnie.

## Przygotowanie do druku

- **Spady:** do offsetu dodaj 3 mm z każdej strony i pasery (plik jest bez spadów).
- **Papier:** offset lub matowa kreda 120–150 g. Matowy nie odbija światła.
- **Okładka:** karton 250–300 g, folia matowa.
- **Oprawa:** zeszytowa (60 stron = 15 arkuszy) albo klejona.
- Strony 45–47, 51 oraz **54–58** są przeznaczone do wycinania i zapisywania —
  nie umieszczaj na nich lakieru UV.
- Strony 54–58 (plansza, kostki, karty) najlepiej wypadną na papierze **170–200 g**;
  jeśli cała broszura idzie na 120–150 g, rozważ dodruk załącznika na grubszym papierze.

## Odtworzenie w Canvie lub InDesignie

1. Canva → szablon **„Educational Workbook A4”**.
2. Ustaw w Zestawie marki kolory z tabeli powyżej i oba kroje (są w bibliotece Canvy).
3. Przenoś strona po stronie — makieta w `do-druku.html` pokazuje docelowy układ 1:1.
4. Grafiki: prawy przycisk na ilustracji → zapisz obraz, albo wklej kod SVG
   bezpośrednio do InDesigna lub Illustratora.
5. Nie zmniejszaj stopnia pisma poniżej 12 pt — to element dostępności, nie estetyki.

## Nota o cytatach

Cytaty w rozdziałach 1, 4, 6, 7, 8, 9, 10 i 11 pochodzą z zachowanych dzieł
Arystotelesa („Metafizyka”, „O częściach zwierząt”, „Etyka nikomachejska”)
w uproszczonym przekładzie. Zdania z rozdziałów 2, 3, 5 i 12 to myśli przypisywane
mu przez późniejszych autorów — zaznaczono to pod każdym z nich i na stronie 50.
Sceny są opowiadaniem: fakty biograficzne są prawdziwe, dialogi napisano na potrzeby
tej broszury.

## Licencje krojów

Atkinson Hyperlegible — SIL OFL 1.1, Braille Institute of America.
Alegreya Sans — SIL OFL 1.1, Huerta Tipográfica.
Oba można legalnie osadzać w plikach i wykorzystywać komercyjnie.
