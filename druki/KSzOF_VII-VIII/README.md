# KSzOF — sfery VII–VIII — kwestionariusz

Kwestionariusz Szkolnej Oceny Funkcjonalnej (KSzOF) dla klas VII–VIII, ekosystem
**EduPlaner2026-MJ-PCTP** · Pomorskie Centrum Terapii Pedagogicznej.

Zbudowany na wzór już zatwierdzonych `Zatwierdzone/KSzOF_I-III/` i
`Zatwierdzone/KSzOF_IV-VI/` — ta sama struktura (9 obszarów ICF, skala 1–5,
ocena 270°, wykres/radar, załącznik wg poziomów), tylko pozycje dopasowane do
starszych uczniów (50 pozycji zamiast 52). **Nie jest jeszcze zatwierdzony** —
czeka w tym folderze do potwierdzenia, tak jak reszta prac w toku.

## Pliki

| Plik | Opis |
|---|---|
| `KSzOF_VII-VIII_interaktywny.html` | wersja do wypełniania na ekranie — samodzielny plik, otwórz w przeglądarce |
| `KSzOF_VII-VIII_pelny.pdf` | gotowy wydruk A4 |

## Jak powstaje PDF

Plik HTML ma wbudowany układ pod druk (`@page{size:A4}` + `@media print`).
W przeglądarce: **Ctrl+P → Zapisz jako PDF** — tak jak w I-III i IV-VI, HTML
jest jedynym źródłem prawdy, bez osobnego generatora.

## Zapisywanie odpowiedzi

Przycisk „Zapisz" w wersji interaktywnej trzyma dane w `localStorage`
przeglądarki. Odpowiedzi zostają wyłącznie na tym urządzeniu/w tej
przeglądarce — nie synchronizują się z żadną bazą ani z aplikacją.

## Skąd te dane i co poprawiono

Treść (50 pozycji, 9 obszarów, kody ICF) pochodzi z przesłanego przez
autorkę pliku `EduPlaner2026_KSzOF_VIIVIII_kwestionariusz_pelny_2.pdf`.
Audyt porównał każdą pozycję z odpowiednikiem w `KSzOF_IV-VI` (najbliższy
wzorzec wiekowo) i znalazł 4 kody ICF, które wyglądały na „przeklejone" z
sąsiedniej pozycji zamiast zachować własny — poprawione w tej wersji:

| Obszar | Pozycja | Było | Poprawiono na |
|---|---|---|---|
| I | 2. „Rozpoznaje i interpretuje treść prezentowaną graficznie" | d115 (Słuchanie) | **d110** (Patrzenie) |
| I | 5. „Opisuje sytuacje, uczucia i zachowania" | d170 (Pisanie) | **d133** |
| I | 12. „Wybiera aktywności spośród kilku możliwości" | d175 (Rozwiązywanie problemów) | **d177** (Podejmowanie decyzji) |
| V | 31. „Podejmuje aktywności prozdrowotne" | d510 (Mycie się) | **d570** (Dbanie o zdrowie) |

Pozostałe 46 pozycji miały kody spójne z `KSzOF_IV-VI`. Arytmetyka (50 × 5 pkt
= zgodne sumy Σ na obszar, 250 pkt łącznie) i format strony były już
poprawne w przesłanym pliku — zweryfikowane niezależnie i bez zmian.

## Zweryfikowane

Programowy pomiar poziomego przelewania (0 elementów) i wizualna kontrola
wszystkich 6 stron — bez ucinania, bez zachodzenia na siebie treści.
