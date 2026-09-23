# ToM — Karta oceny Teorii Umysłu — klasy IV–VI

Arkusz obserwacji Teorii Umysłu (ToM) dla klas IV–VI szkoły podstawowej,
ekosystem **EduPlaner2026-MJ-PCTP**. Ta sama seria co `klasy_1-3/` i
`klasy_7-8/` — wspólna marka, wspólny układ, treść dopasowana do wieku.

## Pliki

| Plik | Opis |
|---|---|
| `ToM_karta_oceny.html` | źródło — dokładnie plik przesłany przez autorkę, bez żadnej zmiany |
| `ToM_karta_oceny.pdf` | wydruk wygenerowany z powyższego HTML (headless Chromium, druk A4) |

## Status: ✅ kompletny (11 z 11 stron) — do potwierdzenia przez autorkę

W przeciwieństwie do wersji dla klas I–III, ten plik **nie ma** mechanizmu
ukrywania gotowej treści za checkboxem „Dołącz do wydruku” — sprawdzone
(`grep 'id="drukuj-'` nie znajduje nic). Stopka na wszystkich 11 stronach
zgadza się z liczbą stron w PDF.

Sprawdzone wizualnie (wszystkie strony, kontakt-sheet + pełna rozdzielczość
dla stron budzących wątpliwości): puste miejsca, które widać na stronach
4, 10 i 11, to celowe pola do wypełnienia (przykładowy szary tekst do
nadpisania własnym opisem, albo miejsce na notatki zespołu) — nie błąd
układu. Żadna strona nie ucina treści.

## Jak powstał PDF

`ToM_karta_oceny.html` ma wbudowany układ pod druk (`@page{size:A4}` +
`@media print`). PDF to dokładnie to, co wyszłoby z **Ctrl+P → Zapisz jako
PDF** w przeglądarce — wygenerowany tu automatycznie (headless Chromium,
`print_background` + `prefer_css_page_size`), bez ingerencji w HTML.
