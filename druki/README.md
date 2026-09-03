# Druki KPOF w Wordzie — EduPlaner 2026 · PCTP

Wersje `.docx` kwestionariuszy KPOF (Kwestionariusz Przedszkolnej Oceny
Funkcjonalnej), wygenerowane z oryginalnych druków HTML z zachowaniem
układu, typografii i kolorystyki marki.

| Plik | Wersja arkusza | Twierdzeń | Stron |
|---|---|---|---|
| `KPOF_3-4_lata.docx` | A (3–4 lata) | 42 | 8 |
| `KPOF_5_lat.docx` | B (5 lat) | 44 | 8 |
| `KPOF_6_lat.docx` | C (6 lat) | 44 | 8 |

## Zachowana identyfikacja wizualna

* fiolet `#2D1B69` i pomarańcz `#E8450A` (nagłówki, plakietki, belka działowa),
* pasek sekcji purpura/pomarańcz, plakietki `KPOF · …`, znaczniki `◆ d1 · Σ …`,
* skala ocen w kolorach oryginału: ① `#D93B30` · ② `#EE6C4D` · ③ `#EFC13B` ·
  ④ `#86C05A` · ⑤ `#2E9E52` · Ⓝ `#8B8698`,
* progi kryterialne (zasób / Poziom I / II / III) w barwach z arkusza,
* stopka z podpisem autorki na każdej stronie (numeracja „Strona X z 8").

Krój pisma: **Segoe UI** (drugi w kolejności w oryginalnym CSS, po niedostępnej
w Wordzie webfontowej rodzinie Mulish); podpis w stopce — **Segoe Script**
(odpowiednik Caveat).

## Różnice wobec wersji interaktywnej HTML

Druk Worda jest wersją do wypełniania ręcznego, więc elementy liczone przez
skrypt w HTML zastąpiono polami do uzupełnienia:

* sumy, średnie i kwalifikacje obszarów — kropkowane pola,
* „Szybki odczyt" — tabela z 9 obszarami i pustymi polami,
* wykres słupkowy — siatka 9 × (1–5) do naniesienia profilu ręcznie,
* mapa radarowa — ramka z adnotacją (generowana automatycznie tylko w HTML).

## Generator

`generator/render.py` przetwarza źródłowy plik HTML na `.docx`:

```bash
pip install python-docx
python generator/render.py KPOF_3_4.html KPOF_3-4_lata.docx
```

Moduły pomocnicze: `dom.py` (parser HTML) i `wordkit.py` (niskopoziomowe
OOXML — ramki, cieniowanie, szerokości kolumn).
