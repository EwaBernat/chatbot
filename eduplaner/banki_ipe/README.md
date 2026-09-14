# Bank rozwiązań do IPE — forma EduPlaner2026-MJ-PCTP

Cztery banki kart celu IPE (obszary ICF 1–4) przeniesione z pierwotnych PDF-ów
(skład LaTeX) do formy zgodnej z marką **EduPlaner2026-MJ-PCTP**.

## Co się zmieniło

| | Pierwotne PDF-y | Ta wersja |
|---|---|---|
| Kolory | czarno-biały druk | fiolet `#2D1B69` + pomarańcz `#E8450A` + kolory funkcjonalne |
| Font | Noto Sans | Arial (zgodnie ze standardem dokumentów PCTP) |
| Strona tytułowa | brak | okładka z metryką dokumentu (liczba kart, kody ICF, wersja, data wydruku) |
| Lista kontrolna | zwykła lista numerowana | tabela z kolumną **TAK / NIE** do odhaczania + zasada PCTP |
| Spis kart | brak | tabela: karta, kod ICF, umiejętność, osoba odpowiedzialna |
| Karta celu | jedna zbita tabela | 8 numerowanych sekcji rzymskich z paskami sekcji |
| Poziomy wsparcia | „1. / 2. / 3.” w tekście | kolorowe plakietki: Znaczne (czerwień), Umiarkowane (amber), Niskie (zieleń) |
| Kroki realizacji | „Krok 1: …” w akapicie | tabela z plakietkami KROK 1–4 |
| Osoba / ewaluacja | jeden wiersz | tabela z miejscem na podpis i wynik ewaluacji |
| Nagłówek / stopka | numer strony | brand + obszar + kody ICF; stopka z autorką i paginacją „x z y” |
| Format | A4 | A4, marginesy 1440×1080×1440×1080 DXA (standard PCTP) |

**Treść merytoryczna jest niezmieniona** — wszystkie pytania listy kontrolnej,
problemy, cele SMART, poziomy wsparcia, pomoce, metody, dostosowania, UDL,
kroki operacjonalizacji, osoby odpowiedzialne i terminy ewaluacji przeniesiono
1:1 (usunięto tylko dzielenie wyrazów wymuszone składem LaTeX).

## Zawartość

| Obszar | Kody ICF | Karty celu | Pytania listy kontrolnej |
|---|---|---|---|
| 1 · Uczenie się i stosowanie wiedzy | d110–d177 | 14 | 16 |
| 2 · Ogólne zadania i obowiązki | d210–d299 | 6 | 16 |
| 3 · Komunikacja i porozumiewanie się | d310–d350 | 5 | 15 |
| 4 · Mobilność i motoryka | d410–d499 | 2 | 16 |

## Struktura każdego dokumentu

1. **Okładka** — tytuł, obszar, kody ICF, etap, instrukcja, metryka
2. **Lista kontrolna** — kluczowe pytania diagnostyczne z kolumną TAK/NIE
3. **Spis kart celu** — do wyboru stron przed drukiem
4. **Karty celu** (po jednej na stronę), każda w ośmiu sekcjach:
   I. Problem / trudność · II. Cel szczegółowy (S.M.A.R.T.) ·
   III. Strategia i poziomy wsparcia · IV. Pomoce dydaktyczne i metody ·
   V. Dostosowania / UDL · VI. Operacjonalizacja ·
   VII. Osoba odpowiedzialna · VIII. Ewaluacja / termin

## Generowanie

```bash
npm install docx           # jednorazowo
node generate_bank.js      # wszystkie cztery obszary
node generate_bank.js 2 4  # wybrane obszary
```

Dokumenty trafiają do `out/`. Treść jest w `data/obszar1.js` … `data/obszar4.js` —
edycja danych wystarcza, układ i marka są w generatorze.

Walidacja po generacji:

```bash
python3 /mnt/skills/public/docx/scripts/office/validate.py out/Bank_IPE_Obszar1_*.docx
```

## Pliki

```
banki_ipe/
├── generate_bank.js          generator (marka, układ, sekcje)
├── data/obszar{1..4}.js      treść kart celu i list kontrolnych
└── out/                      gotowe dokumenty .docx
```

Opracowanie treści: mgr Mirosława Jurczyszyn · PCTP Koszalin
