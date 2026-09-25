# Profil biopsychospołeczny ucznia — obserwacja zasobów, barier i ułatwiaczy (model ICF)

Arkusz obserwacyjny do samodzielnego wypełnienia przez nauczyciela/specjalistę:
zaznaczane czynniki w czterech obszarach modelu ICF (biologiczny, środowiskowy,
psychologiczny, społeczny), uzupełniające WOPF/KSzOF o obraz zasobów, barier i
ułatwiaczy w otoczeniu ucznia. Wspólna marka i konstrukcja z serii `WOPF/` i
`ToM/`.

## Maksymalne skrócenie: 3 strony → 1 strona, prawdziwe logo, układ „2+1 rzędów"

Przesłałaś oryginalny plik (`EduPlaner2026_Profil_biopsychospoleczny_szkola_podstawowa_1.html`,
3 strony) i poprosiłaś o maksymalne skrócenie druku przy zachowaniu treści,
dodanie logo i ułożenie treści bardzo oszczędnie w 2 lub 3 rzędach. Wynik:
**1 strona A4**, cała treść oryginału zachowana (wszystkie 48 pozycji
checkbox, wszystkie pola metryczki, cały tekst syntezy, cała podstawa
prawna) — nic nie zostało wycięte, tylko przełożone na gęstszy układ.

**Prawdziwe logo PCTP.** Poprzedni `.logo` był czystym CSS — fioletowe kółko
z wpisanym tekstem „PCTP", bez żadnego obrazka. Zamieniłam je na Twoje
przesłane logo (kwiat + „PCTP" na fioletowym tle), zakodowane jako PNG
base64 bezpośrednio w CSS — dokładnie ten sam obrazek i technika, co już
działa w `ToM/klasy_4-6` i `ToM/klasy_7-8`, więc plik zostaje w pełni
samodzielny (bez zewnętrznych plików graficznych).

**Układ „2+1 rzędów":**
- **Rząd 1:** Sekcja II (Czynniki biologiczne, 19 pozycji w 4 podsekcjach) i
  Sekcja III (Czynniki środowiskowe, 14 pozycji w 3 podsekcjach) — obok
  siebie, każda jako osobna karta.
- **Rząd 2:** Sekcja IV (Czynniki psychologiczne, 8 pozycji) i Sekcja V
  (Czynniki społeczne, 7 pozycji) — też obok siebie.
- **Rząd 3:** Sekcja VI (Synteza — Zasoby / Bariery / Ułatwiacze) — 3 pełne
  akapity z oryginału, teraz w 3 kolumnach obok siebie zamiast pod sobą.

W każdej karcie obszaru checkboxy stoją w 2 kolumnach (poprzednio 2 kolumny
na pełną szerokość strony — teraz 2 kolumny w połowie szerokości karty),
więc gęstość na papierze jest znacznie wyższa, ale każda pozycja zachowuje
identyczne brzmienie co w oryginale.

**Co zostało skrócone/scalone (bez utraty informacji):**
- Trzy oddzielne bloki wstępu („Jak wypełnić", „O narzędziu", „Podstawa
  programowa") połączone w jeden zwarty pasek — ta sama treść, jedno
  opakowanie zamiast trzech osobnych ramek z własnym marginesem.
- Metryczka: górny pasek strony ma już „Dotyczy ucznia" / „Klasa" / „Data",
  więc w Sekcji I zostały tylko 4 pola, które się z nim nie pokrywają (data
  urodzenia, wychowawca/oceniający, źródła, okres obserwacji) — pola „imię i
  nazwisko" oraz „klasa/oddział" nie zniknęły, tylko nie proszą o to samo
  drugi raz.

**Interaktywność bez zmian.** Zaznaczanie checkboxów (`selBx`) i
synchronizacja metryczki między stronami (`syncMeta` — teraz właściwie
nieaktywna, bo strona jest jedna, ale zostawiona na wypadek przyszłego
rozszerzenia) działają tak samo jak w oryginale. Reszta wspólnego silnika
JS z oryginalnego pliku (przeliczanie punktacji, wykresy radarowe/słupkowe,
transfer wyników do WOPF przez schowek) nie została przeniesiona — w tym
konkretnym dokumencie (czysta lista checkboxów, bez tabel punktowanych) nie
była nigdzie wywoływana, więc jej brak niczego nie zmienia w działaniu ani
w treści druku; usunięcie tych ok. 450 linii martwego kodu też mieści się w
„maksymalnym skróceniu".

Zweryfikowane: brak przelewania na stronie (margines do stopki +60px),
zero błędów JS, wszystkie 48 checkboxów oraz pola tekstowe sprawdzone jako
faktycznie klikalne/edytowalne (nie tylko wizualnie), porównane z oryginałem
pozycja po pozycji.

Jeszcze nie przeniesiony do `Zatwierdzone/` — czeka na Twoje potwierdzenie.
