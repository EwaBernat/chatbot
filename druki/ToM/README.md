# ToM — Karta oceny Teorii Umysłu

Arkusz obserwacji Teorii Umysłu (ToM) dla klas I–III szkoły podstawowej,
ekosystem **EduPlaner2026-MJ-PCTP**. 5 komponentów, 25 pozycji, skala 0–2,
kody ICF przy każdej pozycji.

## Pliki

| Plik | Opis |
|---|---|
| `ToM_karta_oceny.html` | źródło — dokładnie plik przesłany przez autorkę, bez żadnej zmiany |
| `ToM_karta_oceny.pdf` | wydruk wygenerowany z powyższego HTML (headless Chromium, druk A4) |

## ⚠️ Plik jest niekompletny — status: w trakcie, NIE zatwierdzone

Stopka na **każdej** z 6 stron pliku mówi wprost „Strona X **z 11**” — czyli
dokument w zamyśle ma 11 stron. Fizycznie w HTML są tylko `.page`
dla stron 1–6 (potwierdzone też liczbą stron w wygenerowanym PDF: dokładnie
6). **Strony 7–11 nie istnieją w tym pliku.**

Co jest, a czego brakuje:

- str. 1 — metryczka i wstęp do arkusza,
- str. 2 — komponenty I–III (pozycje 1–15),
- str. 3 — komponenty IV–V (pozycje 16–25),
- str. 4–5 — (obecne w pliku, jeszcze nie zweryfikowane szczegółowo),
- str. 6 — proponowane formy wsparcia i wybór programu,
- **str. 7–11 — brak.**

Nie domyślano się i nie dopisano zawartości brakujących stron — to plik
kliniczny/prawny, więc uzupełnienie wymaga oryginału, nie zgadywania.

## Jak powstał PDF

`ToM_karta_oceny.html` ma wbudowany układ pod druk (`@page{size:A4}` +
`@media print`). PDF obok niego to dokładnie to, co wyszłoby z **Ctrl+P →
Zapisz jako PDF** w przeglądarce — wygenerowany tu automatycznie (headless
Chromium, `print_background` + `prefer_css_page_size`), bez ingerencji w
HTML. Sprawdzone: 6 stron w PDF = 6 sekcji `.page` w HTML, rozmiar strony
zgodny z A4.

## Do zrobienia

Potrzebna kompletna, 11-stronicowa wersja tego pliku, zanim trafi do
`Zatwierdzone/`.
