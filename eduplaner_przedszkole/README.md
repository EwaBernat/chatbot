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
`ICF #C1121F` · `Podstawa #1B3FA0` · `Zasób #2B6E6E`.

Typografia: DM Sans (całość) + JetBrains Mono (kody ICF, podstawa, miary).
Zaokrąglenia 7–9 px, jak w drukach WOPF i KPOF.
