# Bank celów SMART · KPOF (EduPlaner 2026 · PCTP)

Zestaw gotowych celów SMART do Kwestionariusza Przedszkolnej Oceny Funkcjonalnej (KPOF),
do wykorzystania w IPET i PEWS.

- **130 twierdzeń** KPOF w 3 wersjach wiekowych (A 3–4 lata · B 5 lat · C 6 lat)
- **390 celów** — po jednym na każdy poziom wsparcia (III / II / I) dla każdego twierdzenia
- każdy cel niesie kod **ICF (d1–d9)** i punkt **podstawy programowej** z arkusza KPOF
- obszary z wynikiem 4,0–5,0 (Zasób) opisane jako **dźwignia**, nie jako cel naprawczy

## Pliki

| Plik | Opis |
|---|---|
| `Bank_celow_SMART_KPOF.html` | druk KC-1: układ tabelaryczny (styl Kącika Dyrektora), zakładki wersji, filtr kolumn, wyszukiwarka |
| `Bank_celow_SMART_KPOF.pdf` | wersja do druku (39 stron A4 **poziomo**: bank KC-1 + konspekt KC-2) |
| `src/dane_34.py`, `src/dane_5.py`, `src/dane_6.py` | bank celów jako dane (obszary, twierdzenia, cele, miary) |
| `Konspekty_KC3_ObszarVII_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru VII (3–4 lata), A4 pionowo |
| `Konspekty_KC3_ObszarI_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru I (3–4 lata), A4 pionowo |
| `Konspekty_KC3_ObszarII_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru II (3–4 lata) |
| `Konspekty_KC3_ObszarIII_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru III (3–4 lata) |
| `Konspekty_KC3_ObszarIV_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru IV (3–4 lata) |
| `Konspekty_KC3_ObszarV_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru V (3–4 lata) |
| `Konspekty_KC3_ObszarVI_3-4lata.pdf` | 3 konspekty KC-3 dla obszaru VI (3–4 lata) |
| `Konspekty_KC3_ObszarVIII_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru VIII (3–4 lata) |
| `Konspekty_KC3_ObszarIX_3-4lata.pdf` | 4 konspekty KC-3 dla obszaru IX (3–4 lata) |
| `src/build.py` | generator druku KC-1 (HTML) |
| `src/konspekty_34_d7.py` | dane konspektów KC-3: obszar VII, wersja A |
| `src/konspekty_34_d1.py` | dane konspektów KC-3: obszar I, wersja A |
| `src/konspekty_34_d2.py` | dane konspektów KC-3: obszar II, wersja A |
| `src/konspekty_34_d3.py` | dane konspektów KC-3: obszar III, wersja A |
| `src/konspekty_34_d4.py` | dane konspektów KC-3: obszar IV, wersja A |
| `src/konspekty_34_d5.py` | dane konspektów KC-3: obszar V, wersja A |
| `src/konspekty_34_d6.py` | dane konspektów KC-3: obszar VI, wersja A |
| `src/konspekty_34_d8.py` | dane konspektów KC-3: obszar VIII, wersja A |
| `src/konspekty_34_d9.py` | dane konspektów KC-3: obszar IX, wersja A |
| `src/build_karty.py.bak` | poprzedni generator w układzie kart |

## Generowanie

```bash
python3 src/build.py          # → Bank_celow_SMART_KPOF.html
```

## Konwencja celu

| Poziom | Średnia KPOF | Wsparcie w celu | Horyzont ewaluacji |
|---|---|---|---|
| Zasób | 4,0–5,0 | rola w grupie wykorzystująca mocną stronę | — |
| Poziom I | 3,0–3,9 | samodzielność i przeniesienie na nową sytuację | 12 tygodni |
| Poziom II | 2,0–2,9 | wsparcie częściowe (plan obrazkowy, przypomnienie) | 8 tygodni |
| Poziom III | poniżej 2,0 | pełne wsparcie, modelowanie, warunki uproszczone | 4 tygodnie |

Reguła nadrzędna: twierdzenie ocenione na 1 lub 2 bierze cel z wiersza **Poziom III**,
niezależnie od średniej całego obszaru.

Marka: EduPlaner2026-MJ-PCTP · pedagog specjalny mgr Mirosława Ewa Jurczyszyn

## Układ druku KC-1

Jedna tabela na obszar ICF, kolumny:

`Lp.` · `Twierdzenie KPOF + miara` · `ICF` (czerwony) · `Podstawa` (niebieski) ·
`Poziom III` · `Poziom II` · `Poziom I`

Trzy poziomy stoją obok siebie, więc widać progresję wymagań w jednym rzucie oka.
Nad każdą tabelą — w druku na każdej stronie — powtarza się pasek identyfikacyjny
z wersją wiekową i nazwą obszaru. Druk: A4 poziomo.

## Paleta EduPlaner 2026 (odczytana z druku WOPF przedszkolnego)

| Rola | Hex |
|---|---|
| Głęboki fiolet — tytuły, pasek identyfikacyjny, koło PCTP | `#2D1B69` |
| Indygo — pasek nagłówka tabeli, pas wersji | `#4F3AA8` |
| Fiolet akcentowy — etykiety uppercase, ikony, obwódki | `#6C4CC4` |
| Pomarańcz — pastylki, kwadraty sekcji, wyróżnienia | `#E8450A` |
| Tło pól i kart | `#EFEAF9` |
| Tło callout / legendy | `#F6F3FC` |
| Wiersz parzysty tabeli | `#F4F0FD` |
| Wiersz nieparzysty | `#FEFDFF` |
| Linia / ramka | `#E3DCF5` |
| Tekst treści | `#2F2A3E` |
| Tekst drugorzędny, stopka | `#8A8498` |

Kolory funkcyjne (poziomy wsparcia i kody) — używane oszczędnie, jako kropka
i 3-pikselowe podkreślenie w nagłówku kolumny oraz bardzo jasne tło kolumny:
`Poziom III #C2410C` · `Poziom II #9A6B08` · `Poziom I #0F7B5A` ·
`ICF #C1121F` · `Podstawa #4F3AA8` (indygo marki — w drukach EduPlanera nie ma czystego błękitu) · `Zasób #2B6E6E`.

Typografia: DM Sans (całość) + JetBrains Mono (kody ICF, podstawa, miary).
Zaokrąglenia 7–9 px, jak w drukach WOPF i KPOF.

## Druk KC-2 — konspekt zajęć

Konspekt nie powiela celów: cytuje je z banku po numerze twierdzenia
(`KC-1 / B / 8`) wraz z kodem ICF i punktem podstawy programowej, więc zapis
w dzienniku, w IPET i w arkuszu KPOF mówi tym samym kodem. Sekcje druku:

1. **Cele z banku KC-1** — numer, ICF, podstawa, poziom wsparcia, treść, miara
2. **Przebieg zajęć** — etap · czas · czynności nauczyciela · czynności dzieci · pomoce
3. **Dostosowania wg poziomu wsparcia** — ta sama aktywność na trzech progach wymagań
4. **Ewaluacja** — kryterium sukcesu, próg, wynik do zaznaczenia, uwagi zespołu, podpisy

W repozytorium konspekt jest wzorem wypełnionym (zabawa „Wieża po kolei",
wersja B, 5-latki) — pola nadpisuje się własną treścią.

## Druk KC-3 — konspekty klikane z banku

W tabeli banku cele obszaru VII (wersja A) są klikalne — znacznik „▸ konspekt".
Kliknięcie celu wybranego poziomu otwiera konspekt w układzie wzoru
„Termometr uwagi": cel edukacyjny cytowany z banku dla klikniętego poziomu
(z automatycznym rozbiciem S/M/A/R/T z danych), cel terapeutyczny, pomoce,
metody, tabela czynności N/D, modyfikacje przy braku postępu, wskazówka.
Konspekt drukuje się osobno na A4 pionowo przyciskiem w oknie.

Konspekty obszaru VII · 3–4 lata: Latarnia uwagi (29) · Podaj misia (30) ·
Mostek do przedszkola (31) · Lusterko emocji (32) · Czarodziejskie słowo POMOC (33).

Konspekty obszaru I · 3–4 lata: Czarodziejski woreczek (1) · Małpka robi to,
co ja (2) · Klepsydra skarbów (3) · Kolorowe domki (4) · Pudełko z niespodzianką (5).

### Pokrycie konspektami — wersja A (3–4 lata)

| Obszar | Konspekty |
|---|---|
| I Uczenie się | Czarodziejski woreczek · Małpka robi to, co ja · Klepsydra skarbów · Kolorowe domki · Pudełko z niespodzianką |
| II Ogólne zadania | Zaproszenie od misia · Dwa kroki do końca · Pociąg dnia · Nasze trzy zasady · Wyspa spokoju |
| IV Poruszanie się | Ścieżka leśnych zwierząt · Schodki do chmurki · Piłka wędrowniczka · Wieża i korale · Muzyczne pociągi |
| VI Życie domowe | Sprzątanie z piosenką · Każda rzecz ma swój dom · Mali pomocnicy |
| VII Wzajemne kontakty | Latarnia uwagi · Podaj misia · Mostek do przedszkola · Lusterko emocji · Czarodziejskie słowo POMOC |
| VIII Główne obszary życia | Moje miejsce w grupie · Kącik lalek i garaż · Dywanik zajęć · Budowniczowie · Bawimy się razem |

Razem **42 konspekty pod 126 klikalnymi celami** — komplet dla wersji A (3–4 lata):
każde twierdzenie kwestionariusza ma własny konspekt zajęć.
