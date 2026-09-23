# ToM — Karta oceny Teorii Umysłu — klasy VII–VIII

Arkusz obserwacji Teorii Umysłu (ToM) dla klas VII–VIII szkoły podstawowej,
ekosystem **EduPlaner2026-MJ-PCTP**. Ta sama seria co `klasy_1-3/` i
`klasy_4-6/` — wspólna marka, wspólny układ, treść dopasowana do wieku.

## Pliki

| Plik | Opis |
|---|---|
| `ToM_karta_oceny.html` | źródło — zredukowane z oryginału 11-stronicowego (patrz niżej) |
| `ToM_karta_oceny.pdf` | wydruk wygenerowany z powyższego HTML (headless Chromium, druk A4) |

## Status: 8 stron (było 11) — zredukowane na wzór klasy 1-3

Oryginał przysłany przez autorkę miał 11 stron. Na jej prośbę zredukowane do
wzoru strukturalnego z `klasy_1-3/` (tam druk ma 7 stron) — bez zmiany
**żadnego** tekstu obserwacji, zaleceń ani celów SMART dla żadnej z 5
umiejętności (Subtelne stany umysłu, Perspektywa społeczna, Sarkazm i
aluzja, Mentalizowanie wyższego rzędu, Faux pas i reputacja) — te są celowo
różne niż w klasie 1-3 i zostają nietknięte.

**Usunięte w całości** (nie ma tego wcale we wzorze klasy 1-3):
- cały cykl re-ewaluacji — tabela „Postęp wg komponentów”, „Wnioski i
  decyzja”, „Nowe zalecenia po ewaluacji” (dawne str. 8 (część)–9),
- sekcja „Synchronizacja druków — przeniesienie wyników” z WOPF (dawne
  str. 10–11).

Podpis prowadzącego i podstawa prawna (dawna końcówka str. 10) zostały
przeniesione na koniec obecnej strony 8 zamiast zostawać na osobnej,
prawie pustej stronie.

**Nie zredukowane do 7 stron, tylko do 8** — dalsze skrócenie wymagałoby
skracania samego tekstu klinicznego (5 opisów umiejętności na str. 6–7),
a to już nie jest zmiana układu, tylko treści — do decyzji autorki.

## Logo PCTP

Nagłówek każdej strony miał okrągły fioletowy placeholder z samym tekstem
„PCTP". Podmieniony na to samo prawdziwe logo (kwiat lawendy + napis PCTP,
`logo-lawenda.webp` z korzenia repo), które klasa 1-3 ma od dawna i które
klasa 4-6 dostała w tym samym kroku — teraz identyczne w całej serii ToM.
To jedyna dotąd zrobiona poprawka konstrukcji dla tego wariantu; kółeczka,
konstrukcja tabeli obserwacji, strona 1 i strony 4-6 czekają jeszcze na te
same poprawki, które klasa 4-6 ma już za sobą (patrz jego README).

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 8 fizycznych stron, żadna nie ucina treści.
