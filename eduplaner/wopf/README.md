# WOPF — arkusz przedszkolny (Word) · EduPlaner 2026 · PCTP

Generator dokumentu `EduPlaner2026_WOPF_arkusz.docx` — wersja Word arkusza interaktywnego
„Wielospecjalistyczna Ocena Poziomu Funkcjonowania (WOPF)”, w stylu marki EduPlaner 2026
(fiolet #2D1B69, pomarańcz #E8450A, Arial, A4).

## Uruchomienie

```bash
npm install docx@9
node build.js ../EduPlaner2026_WOPF_arkusz.docx
python3 fix_borders.py ../EduPlaner2026_WOPF_arkusz.docx
```

`fix_borders.py` porządkuje kolejność krawędzi w `<w:pBdr>` (biblioteka docx zapisuje je
niezgodnie z kolejnością wymaganą przez schemat OOXML).

## Pliki

| Plik | Zawartość |
|---|---|
| `lib.js` | Helpery stylu: nagłówek/stopka, sekcje, ramki, pola, tabele, wykres, podpisy |
| `content1.js` | Strona tytułowa oraz sekcje I – VI |
| `content2.js` | Sekcje VII – XXI wraz z opinią zespołu i klauzulą RODO |
| `build.js` | Złożenie dokumentu (A4, marginesy, nagłówek, stopka z paginacją) |
