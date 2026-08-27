# Kolorowy Świat Emocji

Zeszyt ćwiczeń dla nastolatka — 52 strony A4, pięć emocji, pięć kolorów.
Materiał gotowy do druku i do sprzedaży.

## Co jest w środku

| Strony | Zawartość |
|---|---|
| okładka | tytuł, pasek pięciu kolorów, miejsce na imię |
| 1–6 | o zeszycie, instrukcja dla nastolatka, instrukcja dla dorosłego, bohaterowie, mapa kolorów, słowniczek |
| 7–14 | **Żółty — Radość** |
| 15–22 | **Niebieski — Smutek** |
| 23–30 | **Czerwony — Złość** |
| 31–38 | **Różowy — Wstyd** |
| 39–46 | **Szary — Lęk** |
| 47–51 | moja paleta emocji, plan na trudny dzień, gdy jest bardzo trudno, dyplom, strona wydawcy |

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

## Jak otworzyć i wydrukować

1. Otwórz `kolorowy-swiat-emocji.html` w przeglądarce (dwuklik).
2. Wydrukuj: **Ctrl+P** (Mac: Cmd+P).
3. W oknie druku ustaw:
   - format **A4**, orientacja **pionowa**,
   - marginesy **Brak / None**,
   - **zaznacz** „Grafika tła” / „Background graphics” — bez tego znikną kolory,
   - skala **100 %**.
4. Aby zrobić PDF, wybierz „Zapisz jako PDF” zamiast drukarki.

Plik jest samowystarczalny: kroje pisma i wszystkie zdjęcia są w nim osadzone.
Działa bez internetu i można go wysłać jednym załącznikiem.

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

Kolor grzbietu (okładka, dyplom): fiolet `#4A2E86`.

## Typografia

- Nagłówki: **Nunito** (700/800/900)
- Tekst: **Atkinson Hyperlegible** — krój zaprojektowany przez Braille Institute
  specjalnie pod czytelność; litery, które łatwo pomylić (l, I, 1, O, 0), różnią
  się kształtem. Stąd wybór dla tej grupy odbiorców.
- Tekst nie jest justowany, wiersze są krótkie, interlinia szeroka.

Oba kroje są osadzone w pliku HTML — nie trzeba ich instalować.

## Przed sprzedażą — do uzupełnienia

Na ostatniej stronie zostały pola w nawiasach kwadratowych: autorka, wydawca,
kontakt, wydanie, ISBN. Wpisz je w `generuj.py` w funkcji `stopka_wydawcy()`
albo bezpośrednio w gotowym HTML.

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
