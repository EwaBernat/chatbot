# Plan szkolenia EduPlaner 2026 — pliki na stronę

Dwa gotowe pliki do wgrania na stronę internetową:

| Plik | Zawartość |
|---|---|
| `przedszkole.html` | Plan szkolenia + moduł warsztatowy, ścieżka przedszkolna (6 modułów, KPOF) |
| `szkola.html` | Plan szkolenia + moduł warsztatowy, ścieżka szkolna (7 modułów, KSzOF) |

Każdy plik jest **samodzielny**: cały układ, style i mechanika ćwiczeń są w środku.
Jedyne, co strona pobiera z zewnątrz, to kroje pisma z Google Fonts — bez internetu
strona nadal działa, tylko pokaże pismo systemowe.

## Jak wgrać

1. Skopiuj oba pliki na serwer, np. do katalogu `szkolenia/`.
2. Linki do podania nauczycielom:
   - `https://twoja-domena.pl/szkolenia/przedszkole.html`
   - `https://twoja-domena.pl/szkolenia/szkola.html`
3. Kotwice: `#plan` otwiera plan szkolenia, `#warsztat` — moduł warsztatowy.
   Przydaje się do linku „przejdź do ćwiczeń” pod filmem.

**WordPress:** wgraj pliki przez FTP albo menedżer plików (nie przez bibliotekę
mediów, która nie przyjmuje HTML) i podlinkuj. Wklejenie całego pliku do edytora
strony nie zadziała — edytor usunie style i skrypt.

**Osadzenie w istniejącej podstronie:** `<iframe src="szkolenia/szkola.html"
style="width:100%;height:90vh;border:0"></iframe>`.

## Co robi moduł warsztatowy

Po projekcji każdego modułu filmowego uczestnicy przechodzą na zakładkę
**Warsztat** i wykonują ćwiczenie przypisane do tego modułu: licznik czasu bloku,
pola odpowiedzi, kalkulatory (średnia KPOF, przeliczenie obszaru KSzOF na skalę
0–20 i sten z tabeli norm), kreator celu mierzalnego, karta decyzyjna z regułami
przekierowania oraz quizy sprawdzające z uzasadnieniem przy każdej pozycji.

Klucz odpowiedzi odsłania prowadzący przyciskiem **Pokaż klucz i omówienie**.

Odpowiedzi zapisują się w pamięci przeglądarki uczestnika (`localStorage`) —
nie trafiają na serwer i nie są widoczne dla nikogo innego. Na dole strony jest
„Podsumowanie warsztatu” do skopiowania, a wydruk strony daje wypełnioną kartę pracy.

## Zmiany w treści

Plikiem źródłowym jest `index.html` (obie ścieżki w jednym, do podglądu).
Po zmianie treści przebuduj pliki:

```bash
python3 plan-szkolenia/build.py
```

Skrypt usuwa z każdego pliku treść drugiej ścieżki, wyłącza przełącznik ścieżek
i dokłada nagłówek dokumentu z deklaracją kodowania UTF-8.

## Źródła treści

- *Skrypt dla nauczycieli — PRZEDSZKOLE*, wydanie 2 po audycie podstaw prawnych.
- *Skrypt dla nauczycieli — SZKOŁA PODSTAWOWA, EduPlaner 2026* (64 strony, 18 druków).

Podstawy prawne przepisano ze skryptów bez zmian. Przed wpisaniem publikatora do
dokumentu dziecka lub ucznia sprawdź go w Internetowym Systemie Aktów Prawnych —
teksty jednolite bywają ogłaszane w trakcie roku szkolnego.
