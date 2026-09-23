# ToM — Karta oceny Teorii Umysłu

Arkusz obserwacji Teorii Umysłu (ToM) dla klas I–III szkoły podstawowej,
ekosystem **EduPlaner2026-MJ-PCTP**. 5 komponentów, 25 pozycji, skala 0–2,
kody ICF przy każdej pozycji.

## Pliki

| Plik | Opis |
|---|---|
| `ToM_karta_oceny.html` | źródło — plik przesłany przez autorkę, z jedną poprawką układu (patrz niżej) |
| `ToM_karta_oceny.pdf` | wydruk wygenerowany z powyższego HTML (headless Chromium, druk A4) |

## ⚠️ Plik jest niekompletny — status: w trakcie, NIE zatwierdzone

Stopka na **każdej** stronie pliku mówi wprost „Strona X **z 11**” — czyli
dokument w zamyśle ma 11 stron. Fizycznie w HTML jest obecnie 7 z nich
(potwierdzone liczbą stron w PDF). **Strony 8–11 nie istnieją w tym pliku.**

Co jest, a czego brakuje:

- str. 1 — metryczka, wstęp do arkusza, tabela „Zastosowanie ToM w KSzOF”,
- str. 2 — komponenty I–III (pozycje 1–15),
- str. 3 — komponenty IV–V (pozycje 16–25),
- str. 4–6 — wynik i priorytety, cele SMART, proponowane formy wsparcia,
- str. 7 — zastosowanie ToM w ocenie ABC i FBA (8 funkcji zachowania),
- **str. 8–11 — brak.**

Nie zgadywano i nie dopisano zawartości brakujących stron — to plik
kliniczny/prawny, więc uzupełnienie wymaga oryginału, nie zgadywania.

## Poprawka układu — puste miejsce na str. 1 i 7 (bez zmiany treści/stylu)

Strony 1 i 7 kończyły się na nagłówku sekcji i zostawiały większość strony
pustą przy druku. Powód: dokument ma dwie sekcje w całości gotowe („Zastosowanie
ToM w KSzOF” na str. 1, „Zastosowanie ToM w ocenie ABC i FBA" na str. 7),
domyślnie ukryte przy druku za checkboxem „Dołącz do wydruku” (myślane jako
opcjonalny dodatek w wersji interaktywnej na ekranie).

Jedyna zmiana: oba checkboxy (`id="drukuj-zast"`, `id="drukuj-abcfba"`)
ustawione domyślnie jako zaznaczone (`checked`), a ich sekcje (`<details
open>`) domyślnie rozwinięte — więc obie tabele drukują się od razu, tak jak
się już w pliku znajdowały. Żadna czcionka, kolor, rozmiar ani treść nie
zostały zmienione — pełny diff to dwa dodane atrybuty HTML na stronę
(`git log` w tym repo pokazuje dokładnie te dwie linie). Zweryfikowane
renderem: obie strony teraz w pełni zapełnione, bez białych plam, bez
przelania na dodatkową stronę (nadal 7 stron w PDF).

Drobny kosmetyczny efekt uboczny: przy nagłówkach obu odkrytych sekcji
pojawia się mała strzałka ▲ (domyślny znacznik przeglądarki dla elementu
`<summary>`) — funkcjonalnie bez znaczenia na papierze, ale nie usunięto go
bez pytania, żeby nie robić więcej zmian niż proszono.

## Jak powstał PDF

`ToM_karta_oceny.html` ma wbudowany układ pod druk (`@page{size:A4}` +
`@media print`). PDF obok niego to dokładnie to, co wyszłoby z **Ctrl+P →
Zapisz jako PDF** w przeglądarce — wygenerowany tu automatycznie (headless
Chromium, `print_background` + `prefer_css_page_size`), bez ingerencji w
resztę HTML. Sprawdzone przy każdej rewizji: liczba stron w PDF = liczba
sekcji `.page` w HTML, rozmiar strony zgodny z A4, każda strona obejrzana
jako obraz przed uznaniem za gotową.

## Do zrobienia

1. Zdecydować, czy usunąć znacznik ▲ przy odkrytych sekcjach.
2. Skompletować brakujące strony 8–11 — potrzebny oryginał, nie domysł.
3. Dopiero potem przenieść do `Zatwierdzone/`.
