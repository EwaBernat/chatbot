# Kod źródłowy modułu profilu sensorycznego

Jedno źródło treści, cztery produkty. Nic nie jest wpisywane ręcznie w dwóch miejscach.

```
dane_zrodlowe.py ──► eksport_json.py ──► 01_dane_json/*.json   ← to się wpina do aplikacji
                                              │
                                              ├─► build_tabela.py     ──► SENS-T (HTML)
                                              ├─► build_cele_sens.py  ──► SENS-C (HTML)
                                              └─► nagrania_glos.py    ──► manifest + MP3
```

## `dane_zrodlowe.py` — jedyne miejsce, w które wchodzi poprawka autorki

| stała | co opisuje |
|---|---|
| `MODUL` | metryka modułu, podstawa merytoryczna i prawna, `zasada_modulu` |
| `ZMYSLY` | 7 zmysłów z druku obserwacji: ICF, punkty podstawy programowej, `zasada_si` |
| `SEKTORY` | 3 sektory objawów — trzy wskaźniki w każdym zmyśle |
| `POZIOMY` | p3 / p2 / p1 z kryterium, horyzontem i warunkami |
| `WERSJE` | A / B / C — wiek, czas zajęć, forma, cykl, język poleceń |
| `PROGI` | pasma punktacji zmysłu (0–24) → kryterium i horyzont dla druku SENS-C |
| `WSKAZNIKI` | 21 rekordów merytorycznych — cała treść modułu |

Rekord wskaźnika:

```python
{
  "nr": "II.1", "zmysl": "II", "sektor": 1,
  "wskaznik": "…",                       # zdanie z profilu sensorycznego
  "objawy": [...],                       # twierdzenia przepisane z druku obserwacji
  "strategia": "…",                      # SEDNO — odpowiednik zachowania zastępczego z FBA
  "opis_strategii": "…",
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
  "dieta_sensoryczna"[3], "dostosowania"[3], "ryzyko",
  "obserwacja": {"cel" ze znacznikami, "co_obserwowac", "ile_sytuacji", "smart"{S..T}},
}
```

Dodanie wskaźnika to jeden rekord: 9 celów SMART, 3 konspekty, 1 pomoc, 3 polecenia,
3 nagrania i 1 arkusz powstają z niego automatycznie.

`symbol: None` w karcie arkusza znaczy **pole celowo puste** — miejsce na własny symbol
dziecka z jego tablicy AAC. Eksport liczy takie pola i zapisuje w `biblioteka_symboli`.

## Skąd bierze się kryterium

**Druk SENS-T** — z poziomu wsparcia:

| poziom | warunki | kryterium | horyzont |
|---|---|---|---|
| III | dorosły obok, pomoc podana do ręki | 3 z 5 | 4 tygodni |
| II | pomoc w zasięgu, dziecko sięga samo | 4 z 5 | 8 tygodni |
| I | dziecko rozpoznaje potrzebę samo | 4 z 5 | 12 tygodni |

**Druk SENS-C** — z punktacji zmysłu u konkretnego dziecka (0–24): 13 pkt i więcej →
priorytet (4 z 5, 4 tygodnie), 6–12 → monitorowanie (4 z 5, 8 tygodni), 0–5 → zasób
(3 z 5, 12 tygodni). Dlatego cel w tym druku niesie znaczniki `{proba}`,
`{horyzont_dopelniacz}` i `{horyzont_miejscownik}`, podstawiane dopiero przy składaniu
dokumentu dla dziecka albo w aplikacji.

## Druk SENS-T — co robi JavaScript

* zakładki wersji wiekowych (widoczna jest jedna — druk to trzy kartki poziome, nie dziewięć);
* kliknięcie w komórkę celu otwiera konspekt tego wskaźnika i tej wersji, wyróżniając
  kliknięty poziom w sekcji I i VI;
* **cel edukacyjny w konspekcie czytany jest z komórki tabeli w chwili otwarcia** —
  konspekt nie ma własnej kopii celu i nie może się z nią rozjechać;
* druk jednego konspektu (A4 pionowo) i całego zeszytu 21 konspektów danej wersji;
* przycisk „+” w komórce otwiera formularz własnego konspektu; rekord zapisuje się
  w `localStorage` pod kluczem `eduplaner2026.moje-konspekty-sens.v1`, w kształcie
  z `wlasne_konspekty_kontrakt.json`. Gdy magazyn jest zablokowany albo pełny, komunikat
  mówi, co z tym zrobić — sam „błąd zapisu" nauczycielce nic nie daje.

W odróżnieniu od druku FBA-T ten edytor **nie przyjmuje własnych zdjęć ani nagrań**:
w tym module zdjęcia pomocy i nagrania trzyma `04_media/`, poza dokumentem.

## Skrypty

```bash
python3 eksport_json.py               # zapis do 01_dane_json/
python3 eksport_json.py --sprawdz     # tylko liczby rekordów, bez zapisu
python3 build_tabela.py               # SENS-T: tabela 189 celów + 63 konspekty
python3 build_cele_sens.py            # SENS-C: 9 stron A4 do wypełnienia
python3 build_cele_sens.py --uczen "…" --grupa "…" --wyniki 9,17,14,6,4,19,15
python3 nagrania_glos.py --manifest   # manifest 63 nagrań
python3 nagrania_glos.py --suchy-bieg # liczba znaków do syntezy, nic nie wysyła
python3 nagrania_glos.py --generuj    # MP3 głosem autorki (wymaga dwóch zmiennych)
```

Zależności: wyłącznie biblioteka standardowa Pythona 3.10+. `nagrania_glos.py` korzysta
z `ffmpeg`, jeśli jest w systemie (przekodowanie do 40 kbps mono); bez niego zostawia
format źródłowy i mówi o tym w wyjściu.

## Kontrola spójności

```bash
python3 eksport_json.py --sprawdz
# oczekiwane: 21 · 189 · 63 · 21 pomocy + 63 nagrania · 21 arkuszy
```

`dane_zrodlowe.py` kończy się asercją liczby wskaźników, a eksport przewraca się na
brakującym polu rekordu — obie rzeczy są celowe: lepiej, żeby budowa stanęła, niż żeby
do aplikacji trafił cel bez strategii sensorycznej.
