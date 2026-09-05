# Kod źródłowy modułu profilu sensorycznego

Jedno źródło treści, cztery produkty. Nic nie jest wpisywane ręcznie w dwóch miejscach.

```
dane_zrodlowe.py ──┬─► eksport_json.py ──► 01_dane_json/*.json   ← to się wpina do aplikacji
                   │                            │
                   │                            ├─► build_tabela.py     ──► SENS-T (HTML)
                   │                            ├─► build_cele_sens.py  ──► SENS-C (HTML)
                   │                            └─► nagrania_glos.py    ──► manifest + MP3
                   └─ wspolne_html.py (oprawa graficzna obu druków)
```

## `dane_zrodlowe.py` — jedyne miejsce, w które wchodzi poprawka autorki

Stałe:

| nazwa | co opisuje |
|---|---|
| `MODUL` | metryka modułu, podstawa merytoryczna i prawna, `zasada_modulu` |
| `ZMYSLY` | 7 zmysłów z druku obserwacji, z numeracją rzymską i kodem ICF |
| `SEKTORY` | 3 sektory objawów: nadwrażliwość · podwrażliwość · biały szum |
| `POZIOMY` | 3 poziomy wsparcia (III → I), z opisem roli dorosłego |
| `WIEK` | 3 wersje wiekowe: 3–4 lata, 5 lat, 6 lat |
| `PROGI` | pasma sumy zmysłu (0–24) → kryterium i horyzont dla druku SENS-C |
| `KRYTERIA_POZIOMOW` | kryterium i horyzont dla druku SENS-T (z poziomu wsparcia) |
| `WSKAZNIKI` | 21 rekordów merytorycznych — cała treść modułu |

Rekord wskaźnika (skrót; komplet pól sprawdza `eksport_json.py` przy budowie):

```python
{
  "id": "SENS-04", "kod": "SLU-NAD", "zmysl": "sluch", "sektor": "nadwrazliwosc",
  "nazwa": "…",
  "objawy": [...],                 # zdania przepisane z druku obserwacji
  "opis_dla_doroslego": "…",
  "strategia_sensoryczna": "…",    # SEDNO — bez tego cel traci sens
  "sygnal_dziecka": "…",
  "kontekst": "…",                 # S w SMART: gdzie i kiedy
  "czynnosc": {"3-4": "…", "5": "…", "6": "…"},
  "wskaznik_obserwacji": "…",      # M w SMART: co liczymy
  "dieta_sensoryczna": [...], "dostosowania": [...],
  "pomoc": {"nazwa", "opis_dla_doroslego", "trzy_kroki_uzycia",
            "wskazowka_dla_doroslego", "etykieta_dla_dziecka",
            "polecenia": {"III": "…", "II": "…", "I": "…"}},   # teksty nagrywane
  "instrukcja_slowna": {"III": "…", "II": "…", "I": "…"},      # czyta dorosły
  "konspekt": {...}, "arkusz": {...}, "ryzyko": "…",
}
```

Dodanie wskaźnika to jeden rekord: 9 celów SMART, 3 konspekty, 1 pomoc, 3 polecenia,
3 nagrania i 1 arkusz powstają z niego automatycznie.

## Jak składa się cel SMART

**Druk SENS-T** (`cele_sens_poziomy.json`) — zdanie budowane z czterech pól:

```
{kontekst}, dziecko {czynnosc[wiek]}, {wsparcie[poziom]},
w {kryterium[poziom]} obserwowanych sytuacji, w ciągu {horyzont[poziom]}
(weryfikacja po {horyzont_miejscownik}).
```

Obok gotowego zdania rekord niesie rozbiór `smart` na pola S · M · A · R · T — aplikacja
może pokazać albo zdanie, albo tabelkę, bez ponownego parsowania tekstu.

**Druk SENS-C** (`cele_sens_obserwacja.json`) — zdanie zostaje ze znacznikami
`{proba}`, `{horyzont_dopelniacz}`, `{horyzont_miejscownik}`, bo kryterium zależy od
punktacji konkretnego dziecka. Podstawia je `build_cele_sens.py --wyniki` albo aplikacja,
korzystając z tabeli `progi`.

## Skrypty

```bash
python3 eksport_json.py               # zapis do 01_dane_json/
python3 eksport_json.py --sprawdz     # tylko liczby rekordów, bez zapisu
python3 build_tabela.py               # SENS-T: 22 strony, filtr zmysł/poziom/wiek, notatki
python3 build_cele_sens.py            # SENS-C: 8 stron, formularz do wypełnienia
python3 build_cele_sens.py --uczen "…" --grupa "…" --wyniki 9,17,14,6,4,19,15
python3 nagrania_glos.py --manifest   # manifest 63 nagrań
python3 nagrania_glos.py --suchy-bieg # liczba znaków do syntezy, nic nie wysyła
python3 nagrania_glos.py --generuj    # MP3 głosem autorki (wymaga dwóch zmiennych)
```

Zależności: wyłącznie biblioteka standardowa Pythona 3.10+. `nagrania_glos.py` używa
`ffmpeg`, jeśli jest w systemie (przekodowanie do 40 kbps mono); bez niego zostawia
format źródłowy i mówi o tym w wyjściu.

## Kontrola spójności

Po każdej zmianie w `dane_zrodlowe.py`:

```bash
python3 eksport_json.py --sprawdz
# oczekiwane: 21 · 189 · 63 · 21 pomocy + 63 polecenia · 21 arkuszy
```

`dane_zrodlowe.py` kończy się asercją liczby wskaźników, a `eksport_json.py` przewraca
się na brakującym polu rekordu — obie rzeczy są celowe: lepiej, żeby budowa stanęła,
niż żeby do aplikacji trafił cel bez strategii sensorycznej.
