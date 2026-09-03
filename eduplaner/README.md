# EduPlaner 2026 · PCTP — druki Word

Generatory dokumentów Word w identyfikacji EduPlaner 2026 (fiolet `#2D1B69`, pomarańcz `#E8450A`, Arial, A4):

| Dokument | Generator | Źródło |
|---|---|---|
| `EduPlaner2026_WOPF_arkusz.docx` — Wielospecjalistyczna Ocena Poziomu Funkcjonowania, arkusz przedszkolny (sekcje I–XXI) | `wopf/` | arkusz interaktywny HTML |
| `EduPlaner2026_IPET_druk.docx` — Indywidualny Program Edukacyjno-Terapeutyczny z WOPFU (ICF), druk szkolny (sekcje I–XXIX, trzy części) | `ipet/` | druk PDF |
| `Metryczka_dziecka_przedszkole_2026.docx` — Metryczka dziecka, karta danych i dokumentacji (sekcje I–XI + RODO) | `metryczka/` | formularz PDF |

## Uruchomienie

```bash
npm install docx@9          # w katalogu eduplaner/
node wopf/build.js EduPlaner2026_WOPF_arkusz.docx
node ipet/build.js EduPlaner2026_IPET_druk.docx
node metryczka/build.js Metryczka_dziecka_przedszkole_2026.docx
python3 fix_borders.py EduPlaner2026_WOPF_arkusz.docx
python3 fix_borders.py EduPlaner2026_IPET_druk.docx
python3 fix_borders.py Metryczka_dziecka_przedszkole_2026.docx
```

`fix_borders.py` porządkuje kolejność krawędzi w `<w:pBdr>` — biblioteka `docx` zapisuje je
niezgodnie z kolejnością wymaganą przez schemat OOXML (top, left, bottom, right).

Walidacja: `python3 /mnt/skills/public/docx/scripts/office/validate.py <plik.docx>` — wszystkie pliki
przechodzą walidację.

## Pliki

| Plik | Zawartość |
|---|---|
| `lib.js` | Wspólna biblioteka stylu: nagłówek i stopka z paginacją, banery części, nagłówki sekcji, ramki „Jak wypełnić" i podstawy prawnej, notki, pola metryczkowe, pola wyboru, tabele, legendy skal, wykres profilu, rubryki opisowe, miejsca na podpisy |
| `wopf/content1.js`, `wopf/content2.js` | Treść arkusza WOPF (strona tytułowa, sekcje I–XXI) |
| `ipet/content1.js` | IPET: strona tytułowa, sekcje I–IX (część I — ocena) |
| `ipet/content2.js` | IPET: sfery 1–6, sekcje X–XV (helper `sfera()`) |
| `ipet/content3.js` | IPET: sekcje XVI–XXIX (część II i III) |
| `metryczka/content.js` | Metryczka: sekcje I–XI, zgody, rejestr kontaktów i klauzula RODO |
| `*/build.js` | Złożenie dokumentu — A4, marginesy, nagłówek i stopka |
