# Druk IPET 2026 · WOPF (ICF) — wersja przedszkolna

Druk (pusty formularz do wypełniania) Indywidualnego Programu Edukacyjno-Terapeutycznego
w formacie Word — 21 stron A4, odwzorowanie druku `ipetprz_druk.pdf`.
Ekosystem **EduPlaner2026-MJ-PCTP** · Pomorskie Centrum Terapii Pedagogicznej.

## Pliki

| Plik | Opis |
|---|---|
| `IPET_2026_druk_przedszkole.docx` | druk do wypełniania i druku (Word / LibreOffice) |
| `IPET_2026_druk_przedszkole.pdf`  | podgląd wydruku (21 stron A4) |
| `generate_ipet_druk.js`           | generator — pojedyncze źródło prawdy dla druku |

## Układ 21 stron

| Str. | Zawartość | Str. | Zawartość |
|---|---|---|---|
| 1 | Część wstępna — dane osoby uczącej się | 12 | Cel SMART · sfera 6 — ogólne zadania i zabawa |
| 2 | „Mój głos” — perspektywa dziecka ✦ | 13 | Dostosowania 5 / 5b / 5c (UDL) ✦ |
| 3 | WOPFU 1–2 — mocne strony i motywacja | 14 | 6A — zajęcia rewalidacyjne |
| 4 | WOPFU 3–4 — bariery i obserwacja ABC | 15 | 6B — pomoc psychologiczno-pedagogiczna |
| 5 | Podsumowanie obszarów KPOF ✦ | 16 | 7–9 — wsparcie osobowe, kody ICF, rodzice |
| 6 | Zalecenia z orzeczenia i opinii PPP | 17 | 10 — plan współpracy międzysektorowej ✦ |
| 7 | Cel SMART · sfera 1 — poznawcze | 18 | Część III — zespół, zgoda rodziców, ewaluacja |
| 8 | Cel SMART · sfera 2 — emocjonalno-społeczne | 19 | Załączniki do IPET |
| 9 | Cel SMART · sfera 3 — motoryczne | 20 | Klauzula informacyjna RODO |
| 10 | Cel SMART · sfera 4 — mowa i komunikacja | 21 | Karta kontrolna zgodności z § 6 |
| 11 | Cel SMART · sfera 5 — samodzielność | | |

✦ — elementy nowego modelu 26/27 (ICF / KPOF, poziomy wsparcia I–III, „Mój głos”, UDL).

## Generowanie

```bash
npm install -g docx
NODE_PATH=$(npm root -g) node generate_ipet_druk.js IPET_2026_druk_przedszkole.docx
```

Podgląd PDF i kontrola paginacji (dokument musi mieć dokładnie 21 stron):

```bash
soffice --headless --convert-to pdf --outdir . IPET_2026_druk_przedszkole.docx
pdfinfo IPET_2026_druk_przedszkole.pdf | grep ^Pages
```

## Modyfikacja druku

Treść stała druku (listy pól wyboru, charakterystyki poziomów wsparcia I–III, kody ICF,
podstawy prawne) znajduje się w generatorze:

- sfery 1–6 — tablica `SFERY` (jeden obiekt na stronę 7–12),
- pozostałe strony — funkcje `page01()` … `page21()`,
- marka PCTP (fiolet `#2D1B69`, pomarańcz `#E8450A`, Arial, A4) — stała `BRAND`.

Po każdej zmianie należy ponownie wygenerować plik i sprawdzić liczbę stron —
strony sfer są najgęstsze i najłatwiej je przepełnić.

## Podstawa prawna

Art. 127 ustawy z 14 grudnia 2016 r. — Prawo oświatowe; rozporządzenie MEN z 9 sierpnia
2017 r. w sprawie kształcenia specjalnego (Dz.U. 2017 poz. 1578, ze zm.); rozporządzenie
MEN z 9 sierpnia 2017 r. o pomocy psychologiczno-pedagogicznej (Dz.U. 2017 poz. 1591,
ze zm.); podstawa programowa wychowania przedszkolnego (Dz.U. 2017 poz. 356, ze zm.).
