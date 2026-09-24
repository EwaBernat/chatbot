# Druki — dokumenty i formularze PCTP

Jedno miejsce na wszystkie oficjalne druki i kwestionariusze ekosystemu
**EduPlaner2026-MJ-PCTP** · Pomorskie Centrum Terapii Pedagogicznej. Każdy
dokument ma własny podfolder ze źródłem, gotowym PDF-em i opisem.

## Foldery: zatwierdzone vs w trakcie

`Zatwierdzone/` — druki, które zostały przejrzane i potwierdzone, gotowe do
użycia bez zastrzeżeń. Wszystko poza tym folderem to praca w toku: szukane,
sprawdzane albo czekające na potwierdzenie. Gdy kolejny druk zostanie
potwierdzony, przenosimy go do `Zatwierdzone/` (`git mv`, bez zmiany treści).

## Spis druków

| Dokument | Zakres | Pliki | Status |
|---|---|---|---|
| [`Zatwierdzone/Metryczka_dziecka/`](Zatwierdzone/Metryczka_dziecka/README.md) | karta podstawowych danych dziecka | html | ✅ zatwierdzone (szkoła) |
| [`Zatwierdzone/KSzOF_I-III/`](Zatwierdzone/KSzOF_I-III/README.md) | kwestionariusz funkcjonowania, sfery I–III | html + pdf | ✅ zatwierdzone |
| [`Zatwierdzone/KSzOF_IV-VI/`](Zatwierdzone/KSzOF_IV-VI/README.md) | kwestionariusz funkcjonowania, sfery IV–VI | html + pdf | ✅ zatwierdzone |
| [`ToM/klasy_1-3/`](ToM/klasy_1-3/README.md) | Karta oceny Teorii Umysłu, klasy I–III | html + pdf | ⚠️ niekompletny — 7 z 11 stron |
| [`ToM/klasy_4-6/`](ToM/klasy_4-6/README.md) | Karta oceny Teorii Umysłu, klasy IV–VI | html + pdf | zredukowane 11→8 stron wg wzoru klasy 1-3 — do potwierdzenia |
| [`ToM/klasy_7-8/`](ToM/klasy_7-8/README.md) | Karta oceny Teorii Umysłu, klasy VII–VIII | html + pdf | zredukowane 11→8 stron wg wzoru klasy 1-3 — do potwierdzenia |
| [`WOPF/`](WOPF/README.md) | Wielospecjalistyczna Ocena Poziomu Funkcjonowania — karta scalająca | html + pdf | komplet, 21 stron — do potwierdzenia (kilka punktów, patrz README) |
| IPET — klasa 1-3 | szkoła podstawowa, klasy 1-3 | — | do dodania — szukane w repozytorium, jeszcze nie znalezione |

Wersja IPET dla przedszkola została celowo usunięta z tego projektu —
projekt obejmuje wyłącznie druki dla szkoły.

## Konwencja folderu

Każdy druk to osobny podfolder `druki/<Nazwa_Druku>/` zawierający:

- **źródło** — plik HTML (samodzielny, z CSS pod druk `@page{size:A4}`) albo
  generator (np. `generate_ipet_druk.js` + biblioteka `docx`) — zawsze jedno
  źródło prawdy, z którego da się odtworzyć PDF,
- **gotowy PDF** — wersja do wydruku,
- **`README.md`** — co to za dokument, jak z niego korzystać, jak odtworzyć PDF.

## Wersjonowanie

Wersje to historia gita, nie osobne pliki `_v2_final.docx`. Każda zmiana to
commit z opisem *dlaczego*. Duża rewizja dokumentu (np. inny rok szkolny)
dostaje nowy folder obok starego (`IPET_2026_...` → `IPET_2027_...`) —
stary zostaje jako archiwum, nic nie ginie.

**Zasada dla nowych druków: gotowy dokument scalamy do `main` od razu.**
Dotąd każdy druk/broszura powstawał na osobnej gałęzi i tam zostawał —
`main` nie miał żadnego z nich. Ten folder ma to zmienić.

## Jak dodać kolejny druk

1. Nowy podfolder `druki/<Nazwa>/`.
2. Źródło (HTML albo generator) + wygenerowany z niego PDF.
3. `README.md` w podfolderze + wpis w tabeli powyżej.
4. Do dokumentów pedagogicznych PCTP (WOPF, IPET, Raport Ucznia, Baza
   Uczniów) użyj gotowych skilli — `eduplaner-pctp` albo `ipet-raport-pctp` —
   zamiast pisać generator od zera; do podglądu/wydruku żywego wewnątrz
   aplikacji — `eduplaner-clean-print-ui`.

## Znany dług techniczny (świadomie nieruszany w tym porządkowaniu)

Nic z poniższego nie zostało zmienione teraz, żeby nie ryzykować zepsucia
już dobrze wyglądających PDF-ów — to propozycje na osobny, następny krok:

1. **Marka powielona w kilku plikach.** Kolory PCTP (fiolet `#2D1B69`,
   pomarańcz `#E8450A`) i czcionka Mulish są zaszyte niezależnie w
   `Metryczka_dziecka.html`, `KSzOF_I-III_interaktywny.html`,
   `KSzOF_IV-VI_interaktywny.html` i we wszystkich trzech wariantach
   `ToM_karta_oceny.html` (klasy 1-3, 4-6, 7-8) — pierwsze ~270 linii CSS są
   bajt w bajt takie same w obu KSzOF. Zmiana koloru dziś wymaga edycji w
   kilku miejscach naraz. Da się to bezpiecznie wydzielić do jednego
   wspólnego pliku marki i podmienić z wizualną weryfikacją każdej strony
   przed i po.
2. **Zapis tylko lokalny.** Interaktywne kwestionariusze i metryczka
   trzymają odpowiedzi w `localStorage` przeglądarki — nie idą do żadnej
   bazy ani do aplikacji. Jeśli mają się realnie łączyć z danymi w aplikacji
   (a nie być tylko narzędziem do wypełnienia i wydruku), to osobna decyzja
   projektowa — inny zakres niż samo porządkowanie plików.
3. **IPET dla klas 1-3 jeszcze nie tutaj.** Powstał w osobnej sesji —
   trzeba go odnaleźć w repozytorium i przenieść do tego folderu.
