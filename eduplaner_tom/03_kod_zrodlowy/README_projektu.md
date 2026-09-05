# Kod źródłowy modułu teorii umysłu

Jedno źródło treści, cztery produkty. Nic nie jest wpisywane ręcznie w dwóch miejscach.

```
dane_zrodlowe.py ──► eksport_json.py ──► 01_dane_json/*.json   ← to się wpina do aplikacji
                                              │
                                              ├─► build_tabela.py     ──► TOM-T (HTML)
                                              ├─► build_cele_tom.py  ──► TOM-C (HTML)
                                              └─► nagrania_glos.py    ──► manifest + MP3
```

## `dane_zrodlowe.py` — jedyne miejsce, w które wchodzi poprawka autorki

| stała | co opisuje |
|---|---|
| `MODUL` | metryka modułu, podstawa merytoryczna i prawna, `zasada_modulu` |
| `KOMPONENTY` | 5 komponentów karty ToM: ICF, podstawa programowa, norma rozwojowa, `zasada_tom` |
| `PROGI` | pasma wyniku komponentu (0–10) → kryterium i horyzont dla druku TOM-C |
| `POZIOMY` | p3 / p2 / p1 z kryterium, horyzontem i warunkami |
| `WERSJE` | A / B / C — wiek, czas zajęć, forma, cykl, język poleceń |
| `PRZELICZNIK` | opis skali: 5 komponentów × 5 pozycji × skala 0–2 |
| `WSKAZNIKI` | 25 rekordów merytorycznych — cała treść modułu |

Rekord wskaźnika:

```python
{
  "nr": "IV.4", "komponent": "IV", "pozycja": 4,
  "wskaznik": "…",                       # zdanie z teorii umysłu
  "krok_mentalizacji": "…",              # SEDNO — odpowiednik zachowania zastępczego z FBA
  "opis_kroku": "…",
  "cele": {"A": {"p3","p2","p1"}, "B": {...}, "C": {...}},   # 9 krótkich zdań do tabeli
  "konspekt": {
     "tytul", "metody"[5], "rodzaj_zajec", "wskazowka",
     "modyfikacje": {"p3","p2","p1"},    # drugi wiersz sekcji VI; pierwszy to cel z tabeli
     "warianty": {"A": {"podtytul", "cel_ter", "smart"{S..T}, "kryterium_obs",
                        "pomoce"[5], "przebieg"[5×(N,D)]}, "B": …, "C": …},
  },
  "pomoc": {"nazwa", "co_przygotowac"[5], "trzy_kroki_uzycia"[3],
            "wskazowka_dla_doroslego", "opis_zdjecia",
            "polecenia": {"A","B","C"}},  # teksty nagrywane głosem autorki
  "arkusz": {"tytul", "wstep_dla_doroslego", "karty"[4], "pasek_kolejnosci"[3]},
  "zalecenia"[3], "dostosowania"[3], "uwaga_rozwojowa",
  "obserwacja": {"cel" ze znacznikami, "co_obserwowac", "ile_sytuacji", "smart"{S..T}},
}
```

Dodanie wskaźnika to jeden rekord: 9 celów SMART, 3 konspekty, 1 pomoc, 3 polecenia,
3 nagrania i 1 arkusz powstają z niego automatycznie.

`symbol: None` w karcie arkusza znaczy **pole celowo puste** — miejsce na własny symbol
dziecka z jego tablicy AAC. Eksport liczy takie pola i zapisuje w `biblioteka_symboli`.

`HISTORYJKI` na końcu pliku to osobny słownik, kluczowany numerem wskaźnika. Dostają w nim
wpis tylko te wskaźniki, których pomoc naprawdę wymaga obrazków — tam, gdzie w
`co_przygotowac` stoi historyjka, drabina, listwa albo pasek skali. Pole `rodzaj` decyduje
o układzie na wydruku:

| rodzaj | układ | przykład |
|---|---|---|
| `historyjka` | pola numerowane, czyta się w prawo | Sally-Anne w czterech polach |
| `rozgalezienie` | początek → dwa zakończenia, wiersz na historię | to samo pragnienie, spełnione i nie |
| `listwa` | trzy pola scenariusza zabawy | garnek → mieszanie → talerz |
| `drabina` | pola jedno nad drugim, **od dołu w górę** | szczeble oswajania jedzenia |
| `skala` | pola obok siebie, bez numerów | cicho / w sam raz / za głośno |

Rysunki są **bez tekstu**: polskie podpisy stoją w danych i składa je dokument. Dzięki temu
poprawka słowa nie wymaga przerysowania obrazka — a generator obrazu i tak nie postawiłby
polskiego napisu poprawnie. Wskaźnik z historyjką dostaje w kartach pracy **drugą stronę A4**.


## Skąd bierze się kryterium

**Druk TOM-T** — z poziomu wsparcia:

| poziom | warunki | kryterium | horyzont |
|---|---|---|---|
| III | dorosły obok, podpowiedź wizualna i modelowanie | 3 z 5 | 4 tygodni |
| II | podpowiedź obrazkowa, dziecko wykonuje samo | 4 z 5 | 8 tygodni |
| I | bez podpowiedzi, w sytuacji z rówieśnikami | 4 z 5 | 12 tygodni |

**Druk TOM-C** — z wyniku komponentu u konkretnego dziecka (0–10; tu im wyżej, tym lepiej):
0–3 → priorytet (4 z 5, 4 tygodnie), 4–7 → wymaga wsparcia (4 z 5, 8 tygodni), 8–10 → zasób
(3 z 5, 12 tygodni). Dlatego cel w tym druku niesie znaczniki `{proba}`,
`{horyzont_dopelniacz}` i `{horyzont_miejscownik}`, podstawiane dopiero przy składaniu
dokumentu dla dziecka albo w aplikacji.

## Druk TOM-T — co robi JavaScript

* zakładki wersji wiekowych (widoczna jest jedna — druk to trzy kartki poziome, nie dziewięć);
* kliknięcie w komórkę celu otwiera konspekt tego wskaźnika i tej wersji, wyróżniając
  kliknięty poziom w sekcji I i VI;
* **cel edukacyjny w konspekcie czytany jest z komórki tabeli w chwili otwarcia** —
  konspekt nie ma własnej kopii celu i nie może się z nią rozjechać;
* druk jednego konspektu (A4 pionowo) i całego zeszytu 21 konspektów danej wersji;
* przycisk „+” w komórce otwiera formularz własnego konspektu; rekord zapisuje się
  w `localStorage` pod kluczem `eduplaner2026.moje-konspekty-tom.v1`, w kształcie
  z `wlasne_konspekty_kontrakt.json`. Gdy magazyn jest zablokowany albo pełny, komunikat
  mówi, co z tym zrobić — sam „błąd zapisu" nauczycielce nic nie daje.

W odróżnieniu od druku FBA-T ten edytor **nie przyjmuje własnych zdjęć ani nagrań**:
w tym module zdjęcia pomocy i nagrania trzyma `04_media/`, poza dokumentem.

## Skrypty

```bash
python3 eksport_json.py               # zapis do 01_dane_json/
python3 eksport_json.py --sprawdz     # tylko liczby rekordów, bez zapisu
python3 build_tabela.py               # TOM-T: tabela 189 celów + 63 konspekty
python3 build_cele_tom.py            # TOM-C: 7 stron A4 do wypełnienia
python3 build_cele_tom.py --uczen "…" --grupa "…" --wyniki 8,6,3,1,2
python3 nagrania_glos.py --manifest   # manifest 75 nagrań
python3 nagrania_glos.py --suchy-bieg # liczba znaków do syntezy, nic nie wysyła
python3 nagrania_glos.py --generuj    # MP3 głosem autorki (wymaga dwóch zmiennych)
```

Zależności: wyłącznie biblioteka standardowa Pythona 3.10+. `nagrania_glos.py` korzysta
z `ffmpeg`, jeśli jest w systemie (przekodowanie do 40 kbps mono); bez niego zostawia
format źródłowy i mówi o tym w wyjściu.

## Kontrola spójności

```bash
python3 eksport_json.py --sprawdz
# oczekiwane: 25 · 225 · 75 · 25 pomocy + 75 nagrań · 25 arkuszy
```

`dane_zrodlowe.py` kończy się asercją liczby wskaźników, a eksport przewraca się na
brakującym polu rekordu — obie rzeczy są celowe: lepiej, żeby budowa stanęła, niż żeby
do aplikacji trafił cel bez strategii sensorycznej.
