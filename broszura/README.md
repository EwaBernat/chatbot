# Kolorowy Świat Emocji

**Seria „Świat Kolorów" · część 1**

Zeszyt do zajęć rozwijających kompetencje emocjonalne i społeczne,
dostosowany do potrzeb młodzieży ze spektrum autyzmu. Sprawdzi się
na zajęciach rewalidacyjnych, w pomocy psychologiczno-pedagogicznej,
w terapii indywidualnej i w małej grupie, a także w pracy w domu.

56 numerowanych stron A4 plus okładka. Pięć emocji, pięć kolorów,
gra planszowa do wycięcia. Materiał gotowy do druku i do sprzedaży.

Wydawca: **Pomorskie Centrum Terapii Pedagogicznej (PCTP), Koszalin**.
Autorka: Mirosława Ewa Jurczyszyn, pedagog specjalny.
kontakt@eduplaner2026.pl · [usunięto] · www.eduplaner2026.pl

## Co jest w środku

| Strony | Zawartość |
|---|---|
| okładka | tytuł, pasek pięciu kolorów, miejsce na imię |
| 1 | o tym zeszycie |
| 2 | **spis treści** |
| 3–7 | instrukcja dla nastolatka, instrukcja dla dorosłego, bohaterowie, mapa kolorów, słowniczek |
| 8–15 | **Żółty — Radość** |
| 16–23 | **Niebieski — Smutek** |
| 24–31 | **Czerwony — Złość** |
| 32–39 | **Różowy — Wstyd** |
| 40–47 | **Szary — Lęk** |
| 48 | moja paleta emocji |
| 49–52 | **gra „Ścieżka Kolorów”** — zasady, plansza, dwa arkusze kart do wycięcia |
| 53 | **karty emocji** — twarze do wycięcia |
| 54–56 | plan na trudny dzień, gdy jest bardzo trudno, dyplom |
| 57 | **zapowiedź części 2** — sześć nowych kolorów |
| 58 | strona wydawcy |

Spis treści na stronie 2 wylicza się sam — numery biorą się z faktycznego
składu, więc nie rozjadą się po dopisaniu albo usunięciu stron.
Na każdej stronie w stopce jest logo PCTP, nazwa firmy i numer strony.

Każdy rozdział ma **zawsze ten sam układ ośmiu stron** — przewidywalność jest
tu elementem terapeutycznym, nie ozdobnikiem:

1. Kolor — otwarcie rozdziału
2. Co to jest ta emocja (proste zdania + ciekawostka)
3. Jak wygląda w ciele (twarz / ciało / w środku)
4. Kiedy to czuję (lista z kratkami do zaznaczenia)
5. Opowiadanie o Rajmundzie
6. Pytania do opowiadania (8 pytań + linie do pisania)
7. Zadania na trzech poziomach trudności
8. Moja strona (termometr emocji, rysunek, własne zdjęcie)

## Gra „Ścieżka Kolorów”

Planszówka dla 2–4 osób na stronach 49–52. Potrzebne: kostka, pionki
(wystarczą guziki) i talia 24 kart wyciętych ze stron 51–52.

Gracze idą po 30 polach w pięciu kolorach. Na każdym polu mówi się jedno
zdanie o emocji w tym kolorze; sześć pól z gwiazdką każe wziąć kartę.
Karty są trzech rodzajów, każdy w swoim kolorze i z własną ikoną:
**Sytuacja** (fiolet — nazwij kolor), **Pokaż** (pomarańcz — odegraj emocję
mimiką), **Opowiedz** (złoto — podziel się swoim doświadczeniem).
Rodzaje są przemieszane, więc na obu arkuszach są wszystkie trzy.

Obowiązuje zasada „pas”: każdy może nie odpowiadać, bez tłumaczenia się.
Na stronie z planszą są też wersja łatwiejsza i trudniejsza.

Treść kart i zasad zmienia się w `tresc.py` — zmienne `GRA_KARTY`,
`GRA_ZASADY`, `GRA_POTRZEBNE`.

## Jak otworzyć i wydrukować

1. Otwórz `kolorowy-swiat-emocji.html` w przeglądarce (dwuklik).
2. Wydrukuj: **Ctrl+P** (Mac: Cmd+P).
3. W oknie druku ustaw:
   - format **A4**, orientacja **pionowa**,
   - marginesy **Brak / None**,
   - **zaznacz** „Grafika tła” / „Background graphics” — bez tego znikną kolory,
   - skala **100 %**.
4. Aby zrobić PDF, wybierz „Zapisz jako PDF” zamiast drukarki.

Arkusze kart (strony 51–52) warto wydrukować na grubszym papierze
albo nakleić na karton — będą dłużej służyć.

Plik jest samowystarczalny: kroje pisma i wszystkie zdjęcia są w nim osadzone.
Działa bez internetu i można go wysłać jednym załącznikiem.

## Karty emocji (strona 53)

Pięć kart z twarzami Rajmunda — po jednej na każdą emocję z tego zeszytu —
plus szósta karta „Nie wiem jeszcze”. Służą jako pomoc komunikacyjna: gdy
trudno powiedzieć słowami, nastolatek pokazuje kartę.

## Zapowiedź części 2 (strona 57)

Sześć kolorów zapowiadających kolejny zeszyt, każdy z twarzą i krótkim opisem:

| Kolor | Emocja |
|---|---|
| zielony | spokój |
| pomarańczowy | ekscytacja |
| fioletowy | duma |
| biały | ulga |
| brązowy | znudzenie |
| czarny | samotność |

To propozycja przypisania emocji do kolorów — zmienia się ją w `tresc.py`
w liście `CZESC_2` (nazwa emocji, kolor HEX, opis i nazwa pliku ze zdjęciem).

## Zdjęcia

Zdjęcia leżą w dwóch katalogach:

- `zdjecia/` — oryginały (duże pliki, źródło),
- `zdjecia-gotowe/` — wersje zmniejszone, które trafiają do broszury.

**Żeby podmienić dowolne zdjęcie na swoje:** wrzuć plik do `zdjecia/`
pod tą samą nazwą (PNG lub JPG), a potem uruchom:

```bash
python3 broszura/przygotuj_zdjecia.py
python3 broszura/generuj.py
```

Nazwy miejsc na zdjęcia:

| Nazwa pliku | Gdzie trafia |
|---|---|
| `okladka` | okładka |
| `wstep-tytulowa` | strona o zeszycie |
| `wstep-korzystac` | instrukcja dla nastolatka |
| `wstep-poznaj` | Poznaj Rajmunda |
| `wstep-slowniczek` | słowniczek |
| `01-…` … `05-…` | rozdziały: 01 żółty, 02 niebieski, 03 czerwony, 04 różowy, 05 szary |
| `…-otwarcie` | strona otwierająca rozdział |
| `…-co_to` | strona „Co to jest…” |
| `…-cialo` | strona „Jak wygląda…” |
| `…-kiedy` | strona „Kiedy czuję…” |
| `…-opowiadanie` | opowiadanie |
| `…-zadania` | zadania |
| `koniec` | strona zamykająca |

Miejsce na stronie „Moja strona” celowo zostaje puste — tam nastolatek
wkleja własne zdjęcie.

Jeśli jakiegoś pliku brakuje, broszura sama wstawia w to miejsce ramkę
z opisem, jakie zdjęcie tu pasuje. Nic się nie psuje.

## Zmiana treści

Cała treść — opisy emocji, opowiadania, pytania, zadania, kolory — siedzi
w jednym pliku `tresc.py`. Popraw tekst tam i uruchom `generuj.py`.
Układ stron dopasuje się sam.

Kolory rozdziałów też są w `tresc.py`:

| | kolor | emocja | HEX |
|---|---|---|---|
| 01 | żółty | radość | `#F2B21A` |
| 02 | niebieski | smutek | `#2E6FB7` |
| 03 | czerwony | złość | `#D33B2C` |
| 04 | różowy | wstyd | `#E0619B` |
| 05 | szary | lęk | `#6E7681` |

Kolory marki PCTP: fiolet `#2D1B69` (okładka, dyplom, stopka, logo)
i pomarańcz `#E8450A` (akcent w logo).

Nazwy emocji mają w `tresc.py` pole `rodzaj` — `"m"` albo `"ż"`. Stąd bierze
się poprawna odmiana: „Mój smutek”, ale „Moja radość”.

## Typografia

- Nagłówki: **Nunito** (700/800/900)
- Tekst: **Atkinson Hyperlegible** — krój zaprojektowany przez Braille Institute
  specjalnie pod czytelność; litery, które łatwo pomylić (l, I, 1, O, 0), różnią
  się kształtem. Stąd wybór dla tej grupy odbiorców.
- Tekst nie jest justowany, wiersze są krótkie, interlinia szeroka.

Oba kroje są osadzone w pliku HTML — nie trzeba ich instalować.

## Dane wydawcy

Stopka redakcyjna jest kompletna — nie ma w niej pól do uzupełnienia.
Wszystkie dane siedzą w stałej `FIRMA` w `generuj.py`: nazwa, miasto,
autorka, e-mail, telefon, adres strony i oznaczenie wydania.
Oznaczenie serii — `SERIA`, `CZESC`, `PRZEZNACZENIE`, `DOSTOSOWANIE`
i `GDZIE_WYKORZYSTAC` — jest w `tresc.py`. Kolejna część serii wymaga
zmiany `CZESC` i tytułu.

Gdybyś kiedyś chciała dodać ISBN albo adres pocztowy, dopisz wiersz
w funkcji `stopka_wydawcy()`; funkcja `_pole()` sama pokaże znacznik
do uzupełnienia, dopóki wartość jest pusta.

Logo PCTP — okrągła tarcza z kwiatem i napisem PCTP — jest odrysowane jako
wektor w funkcji `_znak()` w `generuj.py`. Dzięki temu jest ostre w każdym
rozmiarze i nie obciąża pliku. Dwa warianty: `LOGO` (mała tarcza bez napisu,
do stopki i okładki) oraz `LOGO_DUZE` (z gradientem i napisem, na stronie
wydawcy). Jeśli wolisz wstawić oryginalny plik, podmień `LOGO` na
`<img src="data:image/png;base64,...">`.

Dane wydawcy siedzą w stałej `FIRMA` w `generuj.py` — nazwa, miasto, autorka,
e-mail, telefon i nazwa serii.

Na stronie „Gdy jest bardzo trudno” nie ma numerów telefonów — są tam puste
pola, które nastolatek wypełnia sam razem z dorosłym. Jeśli chcesz podać
konkretne numery wsparcia, dopisz je w `generuj.py` w funkcji
`gdy_bardzo_trudno()`.

## Pliki

```
broszura/
├── kolorowy-swiat-emocji.html   ← gotowa broszura (otwórz i drukuj)
├── artefakt.html                ← ta sama treść do publikacji online
├── tresc.py                     ← cała treść i kolory
├── generuj.py                   ← układ stron, style, generator
├── fonty.py                     ← osadzone kroje pisma
├── pobierz_fonty.py             ← pobiera kroje (uruchamiane raz)
├── przygotuj_zdjecia.py         ← zmniejsza zdjęcia do druku
├── zdjecia/                     ← oryginały
└── zdjecia-gotowe/              ← wersje wstawiane do broszury
```

Przebudowa całości po dowolnej zmianie:

```bash
python3 broszura/przygotuj_zdjecia.py
python3 broszura/generuj.py
```
