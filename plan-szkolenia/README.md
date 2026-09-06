# Plan szkolenia EduPlaner 2026 — pliki na stronę

Dwa gotowe pliki do wgrania na stronę internetową:

| Plik | Zawartość |
|---|---|
| `przedszkole.html` | Plan szkolenia, ścieżka przedszkolna (6 modułów, KPOF) — **Wariant A: projekcja** |
| `szkola.html` | Plan szkolenia, ścieżka szkolna (7 modułów, KSzOF) — **Wariant A: projekcja** |

Kolorystyka wzięta z logo PCTP: fiolet pola `#55377D`, lawenda obręczy `#E7DAF3`,
pomarańcz płatków `#EA7A35` (w tekście przyciemniony do `#C0561A`, żeby trzymał
kontrast), złoto łodyg `#CBA242` w kresce pod nagłówkiem. Logo jest wbudowane
w plik jako obraz w treści — nie trzeba go wgrywać osobno.

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

## Wariant A — co jest na stronie

Strona prowadzi projekcję: cele szkolenia, program modułów z timecodami,
**porządek projekcji** (który moduł, jaki plik, od której minuty, co uczestnik
z niego wynosi), wskazówki na przed projekcją / przerwę / po projekcji,
podstawy prawne, materiały i kalendarz dokumentacji na rok szkolny.

Pliki nie zawierają skryptu — to czysty HTML ze stylami. Nic się nie zepsuje
na serwerze i nie ma czego blokować.

## Moduł warsztatowy — na później

Interaktywne ćwiczenia do każdego modułu (kalkulator KPOF, przeliczanie KSzOF
na skalę 0–20 i steny, kreator celu mierzalnego, karta decyzyjna z regułami
przekierowania, quizy z kluczem) są gotowe w pliku źródłowym `index.html`.
Żeby dołożyć je do plików na stronę, zmień w `build.py` wartość `'wariant': 'A'`
na `'wariant': 'AB'` i przebuduj.

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
