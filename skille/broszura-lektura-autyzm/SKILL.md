---
name: broszura-lektura-autyzm
description: >-
  Generator broszury-adaptacji lektury szkolnej dla uczniów ze spektrum autyzmu — jeden plik HTML
  gotowy do druku A4: rozdział na 3 stronach, słowniki pojęć i przenośni, tabele emocji,
  wnioskowanie przyczyna-skutek, ocena sytuacji, teoria umysłu w 5 etapach, pytania na dwóch
  poziomach, ćwiczenia, gra planszowa i scenariusz przedstawienia. Użyj ZAWSZE, gdy użytkownik
  prosi o adaptację, dostosowanie, uproszczenie lub streszczenie lektury dla ucznia albo klasy ze
  spektrum autyzmu lub z zespołem Aspergera, o tekst łatwy do czytania (ETR) z lektury, materiał
  na rewalidację albo TUS z omawianej książki, broszurę lub zeszyt ćwiczeń do lektury, karty pracy
  z lektury pod kątem emocji i teorii umysłu, scenariusz przedstawienia z lektury dla uczniów ze
  specjalnymi potrzebami — a także gdy podaje sam tytuł lektury i grupę, na przykład Mały Książę
  dla klasy VIII ze spektrum. Wyzwalaj też przy hasłach adaptacja lektury, ETR, teoria umysłu do
  lektury, emocje bohaterów dla ucznia z autyzmem.
---

# Broszura-adaptacja lektury dla uczniów ze spektrum autyzmu

Ten skill produkuje **jeden samodzielny plik HTML** złożony na A4 — do druku albo do PDF-a.
Wzorcem jest gotowa broszura „Mały Książę moim bohaterem — podróż emocjonalna”
(107 stron, PCTP). Pełny przykład danych: `assets/maly-ksiaze.json`.

Wartość tego materiału nie leży w uproszczeniu treści, tylko w **odsłonięciu tego, co
literatura zwykle ukrywa**: intencji postaci, ukrytych uczuć, drugiego znaczenia przenośni,
łańcucha przyczyn i skutków. Uczeń ze spektrum zwykle rozumie fabułę — gubi się w tym,
czego trzeba się domyślić. Cała metoda polega na tym, żeby domyślanie się zamienić
w widoczną, nazwaną, ćwiczoną umiejętność.

## Jak to działa

Treść lektury opisujesz w pliku JSON. Skrypt składa z niego HTML: layout, typografię,
ilustracje wektorowe, numerację stron i spis treści dostajesz gotowe.

```bash
python scripts/zloz_broszure.py dane.json --out broszura.html
python scripts/sprawdz_sklad.py broszura.html --dopasuj-linie linie.json --pdf broszura.pdf
python scripts/zloz_broszure.py dane.json --out broszura.html --linie linie.json \
       --fragment artifact.html
```

`--skala 1.15` daje **druk powiększony** (tekst główny 13,1 pt zamiast 11,4 pt) — przydatny
uczniom z trudnościami wzrokowymi i młodszym. Skalowane są tylko wartości w punktach; siatka
i marginesy zostają w milimetrach, więc proporcje A4 się nie zmieniają. Po każdej zmianie skali
przelicz linie na notatki, bo dopasowanie z poprzedniej skali przestaje pasować.

Trzeci krok (ponowny skład z `linie.json`) dopasowuje liczbę linii na notatki do wolnego
miejsca na każdej stronie — bez tego dolna jedna trzecia strony bywa pusta.

## Kolejność pracy

**1. Ustal, czego dotyczy materiał.** Potrzebujesz: tytułu i autora lektury, wieku i etapu
edukacyjnego uczniów, oraz danych wydawcy (placówka, autorka opracowania, kontakt).
Jeśli użytkownik podał tylko tytuł — zapytaj o resztę jednym pytaniem, nie serią.

**2. Podziel lekturę na rozdziały.** Zwykle jeden rozdział broszury = jeden rozdział
oryginału. Przy powieściach o wielu krótkich rozdziałach łącz je w spójne sceny; przy
powieściach o kilku długich — dziel na sceny. Docelowo **12–30 rozdziałów**. Zawsze
zachowaj oryginalną numerację w opisie miejsca, żeby dało się wrócić do książki.

**3. Napisz treść** według `references/metoda.md`. To jest właściwa praca — reszta to skład.

**4. Złóż, sprawdź, popraw.** `sprawdz_sklad.py` mówi wprost, która sekcja przekracza A4.
Nie oddawaj materiału, w którym PDF ma więcej stron niż sekcji — to znaczy, że treść
rozlewa się na puste arkusze.

**5. Oddaj plik.** Powiedz, jak drukować: Ctrl+P → A4, marginesy **brak**, zaznaczona
**grafika tła**.

## Budowa rozdziału — trzy strony, zawsze te same

Przewidywalność układu jest tu narzędziem, nie ozdobą. Uczeń, który wie, że tabela emocji
zawsze jest na drugiej stronie, nie zużywa uwagi na szukanie jej.

| Strona | Zawiera |
|---|---|
| **1 · Historia i słowa** | co się wydarzyło (numerowane zdania) · kto występuje · ilustracja · słowniczek trudnych pojęć |
| **2 · Emocje i wnioski** | tabela emocji · zależności między postaciami · pary przyczyna ➜ skutek |
| **3 · Ocena i myślenie** | ocena sytuacji · ćwiczenie teorii umysłu (etap E1–E5) · pytania łatwiejsze i trudniejsze · linie na notatki |

## Pięć etapów teorii umysłu

Każdy rozdział dostaje ćwiczenie oznaczone etapem. **Rozkładaj etapy przez całą broszurę,
rosnąco, ale nie sztywno** — etap ma wynikać z tego, co dana scena faktycznie pokazuje.
Scena, w której ktoś ukrywa uczucia, to naturalne E5, choćby wypadła w rozdziale trzecim.

| Etap | Pytanie | Kiedy pasuje |
|---|---|---|
| **E1** | Co widzę — a co widzi ktoś inny? | dwie osoby patrzą na to samo i wiedzą co innego |
| **E2** | Co ktoś czuje? | emocja czytelna z twarzy, ciała, głosu, zachowania |
| **E3** | Czego ktoś chce? | pragnienie i wynikające z niego uczucie |
| **E4** | Co ktoś myśli? | przekonania, także fałszywe — ktoś działa zgodnie z tym, w co wierzy |
| **E5** | Co on myśli, że ja myślę? | przenośnia, ironia, ukrywanie uczuć, dwa znaczenia jednego zdania |

Ćwiczenie pisz jako **ponumerowane kroki (①②③…)**, nie jako pytanie otwarte. Ostatni krok
niech odnosi się do życia ucznia albo prosi o dokończenie zdania — to zamyka transfer.

## Sygnalizator oceny sytuacji

Ocena zaczyna się od słowa **ZIELONE**, **ŻÓŁTE** albo **CZERWONE** — skrypt czyta pierwsze
słowo i dobiera kolor bloku.

- **ZIELONE** — nikomu nie stała się krzywda, tak można postępować
- **ŻÓŁTE** — były dobre powody, ale dało się to zrobić lepiej
- **CZERWONE** — ktoś został skrzywdzony albo naraża się na niebezpieczeństwo

**Żółty powinien przeważać.** Sytuacje społeczne rzadko są zerojedynkowe, a materiał, w którym
wszystko jest czarne albo białe, uczy fałszywego obrazu świata. Po ocenie zawsze dopisz,
co dałoby się zrobić inaczej — sama etykieta niczego nie uczy.

## Zasady pisania treści

Pełne omówienie z przykładami: **`references/metoda.md`** — przeczytaj przed pisaniem
pierwszego rozdziału. Skrót:

- **Jedno zdanie = jedna informacja.** Bez zdań wielokrotnie złożonych.
- **Emocja z sygnałem ciała.** Nie „był smutny”, tylko „ogląda zachód 44 razy i nie chce rozmawiać”.
  To sygnał ma być wskazówką, po której uczeń rozpozna emocję u żywej osoby.
- **Przenośnia z dwoma znaczeniami.** Podaj dosłowne i ukryte, nigdy nie kasuj dosłownego —
  dosłowne rozumienie nie jest błędem do poprawienia, tylko punktem wyjścia.
- **Wnioski jako pary.** Przyczyna i skutek osobno, w tej kolejności, krótko.
- **Pytania na dwóch poziomach.** Łatwiejsze: odpowiedź jest wprost w streszczeniu (sprawdź to!).
  Trudniejsze: trzeba połączyć fakty, ocenić albo odnieść do siebie.
- **Tytuły i zdania pytające kończ znakiem zapytania.**
- **Trudne tematy nazywaj wprost.** Śmierć, przemoc, uzależnienie opisane przenośnią są dla
  ucznia ze spektrum trudniejsze niż nazwane spokojnie i wprost. Dopisz odesłanie do zaufanej
  osoby dorosłej i wypełnij `meta.uwaga_trudne_tematy`, żeby nauczyciel wiedział wcześniej.

## Części poza rozdziałami

**Karty postaci (C)** — 4–8 kart: kim jest, jak się zachowuje, po co jest w książce.
Czytane przed lekturą i w razie zgubienia się.

**Ćwiczenia (D)** — 6–10 zestawów, każdy z celem, czasem, formą pracy i **konkretnym
dostosowaniem**. Dostosowanie to nie ogólnik typu „dostosuj do możliwości ucznia”, tylko
rzecz do zrobienia: bank gotowych zdań do wyboru zamiast pisania od zera, dwa kolory
papieru zamiast instrukcji słownej, trzy karty do wyboru zamiast losowania.

**Gra (E)** — plansza 30 pól (rysuje się sama) i cztery talie po 8 kart: emocje, wnioski,
ocena sytuacji, „co on myśli?”. **Nikt nie odpada, nie ma zadań na czas, wynik liczy się
wspólnie dla klasy** — rywalizacja przenosi uwagę z zadania na porażkę.

**Kolejność części trzyma tematy razem.** Wszystko o grze (zasady, instrukcja, talie kart,
plansza do wydruku) idzie jednym ciągiem w części E; wszystko o przedstawieniu (obsada, zasady
dostosowania, program, rekwizyty, sceny) — jednym ciągiem w części F. Nie wynoś planszy do
załączników tylko dlatego, że jest do wycięcia: prowadzący szuka jej tam, gdzie czytał o grze.
W części G zostają wyłącznie materiały ogólne — termometr, krążki oceny, karty miejsc.

**Zakończenie podpisuje autorka.** Po cytacie i akapitach idzie blok pożegnania: znak wydawcy,
kilka zdań do czytelnika, duże inicjały autorki i jej nazwisko. Danych wydawcy nie powtarzaj —
są już w metryczce na stronie 2.

**Metryczka wydawnicza** to zawsze **druga strona**, zaraz po okładce, a spis treści idzie
po niej. Zawiera dane wydawcy, kartę broszury (tytuł, źródło, odbiorcy, zastosowanie, format,
objętość, wydanie), notę o ilustracjach, prawa i instrukcję druku. Nauczyciel, który dostaje
plik bez kontekstu, musi w dwóch sekundach wiedzieć, co trzyma i od kogo.

**Gra (E)** wymaga instrukcji, nie samych zasad. Poza planszą i taliami opisz: co przygotować,
jak rozłożyć stół, przebieg jednej kolejki krok po kroku, co znaczy każdy kolor pola i jak przy
nim odpowiadać, co robi dorosły, co zrobić, gdy uczeń nie umie odpowiedzieć, oraz warianty
(krótszy, jeden na jeden, cała klasa, bez kostki). Same zasady zostawiają prowadzącego
z pytaniem „to jak w to właściwie grać?" — a to jego niepewność przenosi się na uczniów.

**Załączniki (G)** — materiały do wycięcia i powieszenia: plansza do gry na całą stronę
(do druku w A3), termometr emocji do wycięcia wraz ze wskaźnikiem, krążki oceny sytuacji oraz karty miejsc
z lektury (po 4 na stronę, z pytaniem na odwrocie treści). Włącza je klucz `zalaczniki` w danych.
Karty warto tworzyć dla miejsc albo etapów podróży bohatera — dają się układać w kolejności,
co samo w sobie jest ćwiczeniem rozumienia fabuły.

**Scenariusz (F)** — 6–10 scen. Kwestie maksymalnie dwuzdaniowe, powtórzenia celowe,
role bez tekstu (chór, tło, zespół techniczny) wypisane jako pełnoprawne. Do tego zasady
dostosowania i plan prób. Skalowalność obsady jest wymogiem, nie udogodnieniem: scenariusz
ma działać dla klasy dwunasto- i trzydziestoosobowej.

## Ilustracje

Biblioteka gotowych rysunków wektorowych jest w `scripts/broszura/svg.py`; spis nazw
i sposób dopisania własnych: **`references/ilustracje.md`**.

- `rozdzial.ikona` — okrągła ikonka w nagłówku (obowiązkowa, użyj najbliższej z listy)
- `rozdzial.ilustracja` — duży rysunek na stronie 1 (opcjonalny; **8–10 na całą broszurę**,
  przy kluczowych scenach — nie przy każdym rozdziale, bo przestają cokolwiek znaczyć)
- `meta.okladka_svg` — rysunek okładki; do nowej lektury napisz własny i wklej jako
  inline SVG. Kontrakt: `viewBox="0 0 420 300"`, ciemne tło, `preserveAspectRatio="xMidYMax slice"`.
- `rozdzial.obraz` i `meta.okladka_obraz` — **gotowe zdjęcia** (PNG/JPEG/WebP), ścieżki względem
  pliku JSON albo katalogu z `--grafiki`. Osadzane w HTML jako `data:` URI, więc broszura zostaje
  jednym plikiem — ale rośnie o ok. 1⁄3 rozmiaru zdjęć, więc najpierw je zmniejsz (ok. 1600 px).

Wykresy narzędziowe (termometr, schody teorii umysłu, plansza, scena) są niezależne od
lektury i rysują się same.

## Pułapki składu

Te trzy rzeczy psuły skład najczęściej — nie próbuj ich „uprościć”:

1. **SVG w `<figure>` musi mieć pudełko proporcji** (`padding-bottom` w procentach, SVG
   pozycjonowany absolutnie). Przy `height:auto` silnik druku gubi wysokość i rozbija stronę
   na dwa arkusze. Robi to funkcja `fig()` — używaj jej.
2. **Breakpoint mobilny musi być `@media screen and (max-width:800px)`.** Bez `screen`
   odpala się przy druku (arkusz A4 to ~793 px), zwija dwie kolumny w jedną i podwaja liczbę stron.
3. **Sekcja nie może przekroczyć 292 mm** (A4 minus zapas na zaokrąglenia silnika druku). `sprawdz_sklad.py` to wykryje; skróć treść,
   zmniejsz ilustrację albo przenieś blok na następną stronę. Marginesy w druku muszą być
   identyczne jak na ekranie — inaczej pomiar kłamie.

## Format danych

Pełny opis pól z przykładem rozdziału: **`references/dane.md`**.
Działający komplet: **`assets/maly-ksiaze.json`** (27 rozdziałów) — najszybszą drogą do
nowej lektury jest skopiowanie go i podmiana treści, bo od razu widać oczekiwaną głębokość
każdego pola.
