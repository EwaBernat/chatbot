# ToM — Karta oceny Teorii Umysłu — klasy IV–VI

Arkusz obserwacji Teorii Umysłu (ToM) dla klas IV–VI szkoły podstawowej,
ekosystem **EduPlaner2026-MJ-PCTP**. Ta sama seria co `klasy_1-3/` i
`klasy_7-8/` — wspólna marka, wspólny układ, treść dopasowana do wieku.

## Pliki

| Plik | Opis |
|---|---|
| `ToM_karta_oceny.html` | źródło — zredukowane z oryginału 11-stronicowego (patrz niżej) |
| `ToM_karta_oceny.pdf` | wydruk wygenerowany z powyższego HTML (headless Chromium, druk A4) |

## Status: 8 stron (było 11) — zredukowane na wzór klasy 1-3

Oryginał przysłany przez autorkę miał 11 stron. Na jej prośbę zredukowane do
wzoru strukturalnego z `klasy_1-3/` (tam druk ma 7 stron) — bez zmiany
**żadnego** tekstu obserwacji, zaleceń ani celów SMART dla żadnej z 5
umiejętności (Rozpoznawanie emocji mieszanych, Decentracja, Ironia i
podtekst, Fałszywe przekonanie II rzędu, Faux pas) — te są celowo różne niż
w klasie 1-3 i zostają nietknięte.

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

## Strona 1 przebudowana na wzór klasy 1-3 — ⚠️ do potwierdzenia

Na prośbę autorki strona 1 ma teraz dokładnie tę samą kolejność sekcji co
`klasy_1-3/`: metryczka (2 pola) → tytuł → „Czym jest ToM” → skala →
„Więcej” (ukryte przy druku, jak w 1-3) → nagłówek „Arkusz obserwacji” →
tabela „Zastosowanie ToM w KSzOF”.

Metryczka: usunięte 2 zduplikowane pola („Imię i nazwisko”, „Klasa/oddział”
— powtarzały dane już wpisywane w nagłówku strony), zostały te same 2 pola
co w 1-3.

**Tabela „Zastosowanie ToM w KSzOF (klasy IV–VI)” — nowa, zbudowana teraz.**
1-3 miała gotową tabelę TUE/TUS/TUK dla swojego KSzOF; dla klas 4-6 takiej
nie było. Zbudowana od podstaw na bazie **rzeczywistej** treści
`druki/Zatwierdzone/KSzOF_IV-VI/` (52 pozycje, 9 obszarów, kody ICF) —
każdy z 5 komponentów ToM dopasowany do tematycznie najbliższych pozycji
KSzOF IV-VI. To dopasowanie tematyczne jest interpretacją, nie jedynym
możliwym przyporządkowaniem — **wymaga sprawdzenia przez autorkę**, w
odróżnieniu od reszty pliku, która jest przeniesieniem istniejącej treści.

## Jak powstał PDF

Tak jak reszta serii: `@page{size:A4}` + `@media print` w HTML, PDF to
odpowiednik **Ctrl+P → Zapisz jako PDF**, wygenerowany tu automatycznie
(headless Chromium, `print_background` + `prefer_css_page_size`).
Zweryfikowane renderem: 8 fizycznych stron, żadna nie ucina treści.
