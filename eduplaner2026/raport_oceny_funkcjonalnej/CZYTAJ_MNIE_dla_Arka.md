# EduPlaner 2026 · Ocena Funkcjonalna – paczka dla programisty

Autorka koncepcji: Mirosława Ewa Jurczyszyn (PCTP Koszalin). Stan na 12.09.2026.

## Co jest w paczce

| Folder | Zawartość |
|---|---|
| `01_PDF_do_druku/` | 3 gotowe PDF-y: raport całościowy (ocena + IPET + opinia), sama ocena funkcjonalna (WOPF + opinia), sam IPET |
| `02_Word_edytowalne/` | te same 3 raporty w DOCX + osobna „Opinia o funkcjonowaniu dziecka/ucznia” dla poradni |
| `03_Aplikacja_HTML/` | jeden plik HTML: podgląd, przełącznik rodzaju dokumentu (całościowy / ocena / IPET), przełącznik edycji (01/02/03), przełącznik KPOF/KSzOF, druk A4 z przeglądarki |
| `04_Zrodla_i_generatory/` | `raport_data.json` (jedyne źródło treści), `build_html.py` + `styles.css` + `part1_pages.html` (HTML), `generate_raport_docx.js` (Word), `ZASADY_dokumentow_CLAUDE.md` (wszystkie reguły merytoryczne i graficzne ustalone z autorką) |
| `05_Podstawy_prawne/` | oryginał rozp. ME z 2.03.2026 (Dz. U. 2026 poz. 428) – § 7 to opinia placówki, § 8 to ocena zespołu poradni |

## Jak przebudować

```bash
cd 04_Zrodla_i_generatory
pip install --user pymupdf            # tylko do podglądu, opcjonalnie
npm install                           # docx@9
python3 build_html.py                 # -> Raport_Oceny_Funkcjonalnej.html
# PDF (Chromium, druk ciągły, numeracja w marginesie przez @page margin boxes – wymaga Chrome/Chromium >= 131):
chrome --headless --no-pdf-header-footer --print-to-pdf=Raport_pelny.pdf "file://$PWD/Raport_Oceny_Funkcjonalnej.html#tryb=pelny"
chrome --headless --no-pdf-header-footer --print-to-pdf=Raport_ocena.pdf "file://$PWD/Raport_Oceny_Funkcjonalnej.html#tryb=ocena"
chrome --headless --no-pdf-header-footer --print-to-pdf=Raport_ipet.pdf  "file://$PWD/Raport_Oceny_Funkcjonalnej.html#tryb=ipet"
# Word:
npm run docx:pelny && npm run docx:ocena && npm run docx:ipet && npm run docx:opinia
```

Parametry URL w HTML: `#tryb=pelny|ocena|ipet&ed=01|02|03`. Wybory zapisują się w `localStorage`
(`rof_tryb`, `rof_ed`, `rof_tool_v1` = KPOF/KSzOF).

## Zasady, których nie wolno naruszyć (skrót – pełna lista w ZASADY_dokumentow_CLAUDE.md)

1. **Bez reklam** w drukach dla rodziców i poradni: nagłówek = nazwa placówki; dopuszczalny tylko maleńki znak w stopce.
2. **Czcionka 11 pt, jednolita**, tabele też 11 pt; brak pustych stron (druk ciągły).
3. **KPOF** = przedszkole (bez stenów), **KSzOF** = szkoła (steny tylko w kolumnie domen, nigdy przy średniej).
4. Sekcja 4: obszary ICF dokładnie wg § 7 ust. 7 – przedszkole 5, uczeń 7 (tabele A/B).
5. Opinia dla poradni: 7 elementów § 7 ust. 6 w tej kolejności; treści z § 8 tylko jako „informacje uzupełniające”.
6. Sekcja 9 = cele (CO), Część III = metody (JAK). Bez dublowania treści.
7. Trzy edycje w roku (01 wrzesień, 02 styczeń, 03 czerwiec) i trzy rodzaje dokumentu.

## Dane przykładowe

Wszystkie dane dziecka, wyniki, zajęcia i terminy w `raport_data.json` są przykładowe (dziecko ze spektrum autyzmu) i służą do nadpisania danymi z aplikacji.
