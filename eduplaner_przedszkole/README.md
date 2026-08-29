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
| `Bank_celow_SMART_KPOF.pdf` | wersja do druku (31 stron A4 **poziomo**, wszystkie trzy wersje wiekowe) |
| `src/dane_34.py`, `src/dane_5.py`, `src/dane_6.py` | bank celów jako dane (obszary, twierdzenia, cele, miary) |
| `src/build.py` | generator druku KC-1 (HTML) |
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
