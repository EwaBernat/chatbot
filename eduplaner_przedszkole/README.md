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
| `Bank_celow_SMART_KPOF.html` | dokument roboczy: zakładki wersji, filtr poziomów, wyszukiwarka, druk A4 |
| `Bank_celow_SMART_KPOF.pdf` | wersja do druku (77 stron A4, wszystkie trzy wersje wiekowe) |
| `src/dane_34.py`, `src/dane_5.py`, `src/dane_6.py` | bank celów jako dane (obszary, twierdzenia, cele, miary) |
| `src/build.py` | generator dokumentu HTML |

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
