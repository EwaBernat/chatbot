---
name: cele-fba-pbs
description: 'Rozbudowa modułu FBA/PBS dla przedszkola (EduPlaner 2026, PCTP Koszalin, autorka Mirosława Ewa Jurczyszyn) — cele SMART do wskaźników kwestionariusza funkcji zachowania, konspekty zajęć KC-3, karty pomocy KC-4 z poleceniem nagranym jej głosem, arkusze A4 do wycięcia i edytor własnych konspektów nauczycielki. Użyj ZAWSZE, gdy prosi o: „dopisz cel do wskaźnika", „napisz konspekt do funkcji ucieczki", „uzupełnij pomoce do FBA", „nagraj polecenia", „przebuduj tabelę", „wydrukuj konspekty", „zrób druk dla ucznia z FBA", a także przy hasłach: FBA, ABC, PBS, zachowanie zastępcze, funkcja zachowania, analiza funkcjonalna, druk FBA-C, druk FBA-T, wskaźnik I.1–V.5, ucieczka, uwaga, dostęp, sensoryczne, tabela celów wiek × poziom wsparcia. NIE używaj do banku celów SMART KPOF (twierdzenia, wersje A/B/C/U, podstawa 2026) — ten obsługuje skill bank-celow-smart; ani do WOPF, IPET, Bazy Uczniów i Raportu Ucznia — te obsługują eduplaner-pctp i ipet-raport-pctp.'
---

# Moduł FBA/PBS — rozbudowa

`eduplaner_fba/` to dalszy ciąg jej karty ABC / FBA. Tamta kończy się pięcioma
celami SMART — po jednym na funkcję zachowania. Ten moduł rozpisuje je na
**25 wskaźników × 3 poziomy wsparcia × 3 wersje wiekowe = 225 celów**, dokłada
**75 konspektów zajęć**, **25 pomocy dydaktycznych z 75 nagraniami jej głosem**,
**25 arkuszy A4 do wycięcia** (każdy drukowany w trzech wersjach) i edytor, w którym nauczycielka dopisuje własne
scenariusze.

Trzy druki, każdy jednym plikiem HTML otwieranym z dysku — bez serwera, bez konta,
z mediami w środku jako `data:` URI:

| druk | plik | co to jest |
|---|---|---|
| **FBA-C** | `Cele_SMART_FBA_obserwacja_poglebiona.html` | 25 celów do obserwacji pogłębionej, 8 stron A4 pionowo, kryterium i horyzont z punktacji funkcji u konkretnego ucznia |
| **FBA-T** | `Tabela_celow_FBA_wiek_poziom.html` | 225 celów w układzie banku KPOF: zakładki wersji, wiersz na wskaźnik, trzy kolumny poziomów; w środku 75 konspektów i edytor własnych |
| **zeszyty** | `Konspekty_FBA_A|B|C.pdf` | 25 konspektów jednej wersji wiekowej — 75 stron, bo każdy zajmuje trzy: scenariusz, karta pomocy, arkusz |

Ten skill prowadzi rozbudowę tak, żeby nowy element wszedł do dokumentu naprawdę.
Moduł ma tę samą nieoczywistą cechę co bank KPOF: **brak nie wysypuje budowania.**
Karta bez zdjęcia dostaje pole zastępcze, karta bez nagrania — wyłączony przycisk,
arkusz z nienarysowanym symbolem jest po cichu pomijany. Nauczyciel dowie się przy
drukarce, w sali, przy dziecku. Dlatego sprawdzamy pomiarem, zamiast zakładać.

## Zanim cokolwiek dopiszesz

```bash
python3 .claude/skills/cele-fba-pbs/scripts/sprawdz_fba.py
```

Wypisuje stan całości: cele per funkcja, konspekty, pomoce bez zdjęcia albo bez
nagrania, polecenia z trudnymi słowami, symbole czekające na rysunek. Kończy się
kodem 1, gdy znalazł brak. Uruchom **przed** pracą i **po** niej.

## Cztery zasady, których nie wolno złamać

**1. Cel opisuje zachowanie zastępcze, nie brak zachowania trudnego.** Plan PBS
uczy **innej drogi do tej samej funkcji** — ucieczki, uwagi, dostępu, regulacji —
a nie odbiera dziecku funkcji. „Nie będzie uciekał od stolika" to nie jest cel
z tego modułu; „poprosi o przerwę kartą, zanim wyjdzie od stolika" — jest. Przy
dopisywaniu czegokolwiek zapytaj siebie: *jaką potrzebę dziecko tym załatwia?*
Jeśli nie umiesz odpowiedzieć, cel jest z innego druku.

**2. Nagrania tylko jej własnym, sklonowanym głosem.** `voice_id
jq4ZUryuBeDqmtkKtBZ4`, model `eleven_v3`. Materiał firmowany jej nazwiskiem ma
brzmieć nią. Gdy głos jest niedostępny — oddaj sam tekst polecenia i zatrzymaj
się; nie podstawiaj głosu premade „na próbę". Rejestr aktorski: `references/pomoce.md`.

**3. Do dziecka mów prosto.** Polecenie na karcie pomocy i etykieta na arkuszu to
teksty, które **usłyszy albo przeczyta przedszkolak**: krótkie zdania, bez słów
typu *strategia*, *sygnał*, *instrukcja*, *sekwencja*, *procedura*, *technika*.
Zamiast nich to, co dziecko widzi i robi: *sposób*, *kartka*, *gwizdek*, *co ci
pomaga*, *kiedy robi się trudno*. Trudne słowa zostają tam, gdzie czyta je
**dorosły** — w celu SMART, w metodach, w trzech krokach użycia i we wskazówce.
Sprawdź to **przed nagraniem**: poprawka po nagraniu kosztuje drugie nagranie.
Tabela zamienników: `references/pomoce.md`.

**4. Jeden symbol = jeden plik, używany wszędzie tak samo.** Arkusze FBA biorą
symbole z **biblioteki banku KPOF** (`eduplaner_przedszkole/assets/symbole`), nie
z własnego zbioru. Dziecko korzystające z komunikacji obrazkowej musi widzieć ten
sam obrazek tu, na tablicy AAC i w planie dnia. Nigdy nie rysuj drugiego
„podobnego" symbolu pod jeden konspekt — dopisz istniejący albo dołóż nowy do
wspólnej biblioteki.

## Skąd biorą się kryterium i horyzont

Nie z podręcznika — z tego, co wyszło u konkretnego dziecka. To jest sedno obu
druków i najczęstsze miejsce, w którym można je zepsuć, dopisując „ładniejszą"
liczbę.

**FBA-C — z punktacji funkcji w kwestionariuszu:**

| punkty | ocena funkcji | kryterium | horyzont |
|---|---|---|---|
| 10–15 | dominująca | 8 z 10 sytuacji | 4 tygodnie |
| 5–9 | istotna | 7 z 10 sytuacji | 8 tygodni |
| 0–4 | słaba | 6 z 10 sytuacji | 12 tygodni |

Funkcja dominująca ma **najkrótszy** horyzont nie dlatego, że jest łatwiejsza,
tylko dlatego, że jest priorytetem planu — sprawdzamy ją najczęściej.

**FBA-T — z poziomu wsparcia:**

| poziom | warunki | kryterium | horyzont |
|---|---|---|---|
| III | podpora dorosłego, pomoc podana do ręki | 3 z 5 | 4 tygodnie |
| II | pomoc w zasięgu, dziecko sięga po nią samo | 4 z 5 | 8 tygodni |
| I | bez pomocy przedmiotowej, zachowanie trudniejsze | 4 z 5 | 12 tygodni |

Na Poziomie I kryterium **nie rośnie do 5 z 5**: rośnie trudność samego
zachowania, nie liczba prób. „Za każdym razem" to w przedszkolu cel nie do
osiągnięcia — psuje ewaluację, zamiast ją domykać.

Horyzont trzymamy w **trzech formach gramatycznych** (`4 tygodni` · `4 tygodniach`
· `4 tygodnie`), bo wchodzi w trzy różne zdania. Jedna forma dawała „weryfikacja
po 4 tygodni" w druku, który idzie do rodzica.

## Co gdzie leży

```
eduplaner_fba/
  src/dane_fba.py          25 celów do obserwacji pogłębionej + progi punktacji
  src/dane_poziomy.py      225 celów: wskaźnik × poziom × wersja wiekowa
  src/build_cele_fba.py    składanie druku FBA-C
  src/build_tabela.py      składanie druku FBA-T (tabela + konspekty + edytor)
  src/konspekty_fba_1..5.py  treść konspektów, moduł na funkcję zachowania
  src/konspekty_fba.py     scalanie: rdzeń + wariant wiekowy + dane z tabeli
  src/konspekt_fba.py      renderowanie konspektu, wykazu i arkusza (wzór KC-3)
  src/pomoce_fba.py        25 pomocy + 75 poleceń dla dziecka
  src/karta_pomocy.py      renderowanie karty pomocy z nagraniem (wzór KC-4)
  src/symbole_fba.py       mapowanie kart i pasków na bibliotekę symboli KPOF
  src/moje_konspekty_fba.py  edytor własnych konspektów nauczycielki
  src/kompresuj_fba.py     PNG → k_*.jpg 900 px, MP3 → 40 kbps mono
  src/zmierz_konspekty.mjs   pomiar: czy konspekt mieści się na kartce
  src/zmierz_strony.mjs    pomiar stron druku FBA-C
  src/logo.py              logo PCTP w nagłówkach
  src/pobierz.sh           pobieranie nagrań z ElevenLabs po parach „kod URL”
  src/do_pdf.mjs           wydruk druków i trzech zeszytów do PDF
  assets/pomoce_fba/       zdjęcia pomocy dydaktycznych
  assets/audio_fba/        75 nagrań poleceń jej głosem (poza repozytorium)
```

## Ścieżki rozbudowy

Wybierz to, o co prosi, i przeczytaj odpowiedni plik z `references/` **zanim**
zaczniesz pisać treść — każdy niesie wzór, ograniczenia i pułapki, które w tym
projekcie już raz kosztowały przebudowę.

| Prośba | Przeczytaj | Potem |
|---|---|---|
| „dopisz cel do wskaźnika", „zmień kryterium" | `references/cele.md` | przebuduj oba druki |
| „napisz konspekt", „popraw przebieg zajęć" | `references/konspekt.md` | pomiar `zmierz_konspekty.mjs` |
| „brakuje pomocy", „nagraj polecenia" | `references/pomoce.md` | zdjęcie + nagranie + kompresja |
| „brakuje materiału do wycięcia" | `references/konspekt.md` (sekcja *Arkusz*) | ewentualnie nowy symbol w banku KPOF |
| „popraw edytor własnych konspektów" | `references/edytor.md` | test w Chromium, nie oglądanie |
| „zrób druk dla ucznia Zosi" | niżej, sekcja *Druk dla konkretnego dziecka* | plik **poza** repozytorium |

## Pętla robocza

```bash
cd eduplaner_fba
# 1. treść — dopisz w odpowiednim module w src/
# 2. media — jeśli doszły nowe zdjęcia albo nagrania
python3 src/kompresuj_fba.py
# 3. przebuduj druki
python3 src/build_tabela.py && python3 src/build_cele_fba.py
# 4. sprawdź spójność
python3 ../.claude/skills/cele-fba-pbs/scripts/sprawdz_fba.py
# 5. sprawdź druk — dwa pomiary, bo są dwa druki
node src/zmierz_konspekty.mjs   # 75 konspektów, budżet 1091 px
node src/zmierz_strony.mjs      # 8 stron FBA-C, budżet 726 × 1054 px
# 6. PDF-y (tabela + trzy zeszyty), gdy prosi o pliki do druku
node src/do_pdf.mjs
```

Kroku 5 nie da się zastąpić oglądaniem. Konspekt, który wyjdzie poza stronę, nie
zgłasza błędu — pęka w pół tabeli przebiegu, co widać dopiero przy drukarce.
Budżet: **1091 px** treści przy skali druku 0.96.

Symbole na arkuszach biorą się z banku KPOF ścieżką **względną, trzy poziomy
w górę** (`symbole_fba.BIBLIOTEKA`). Budowanie druku spoza układu repozytorium —
z kopii modułu, z innego katalogu — **po cichu gubi wszystkie symbole**: dokument
składa się, jest o ponad megabajt lżejszy i niczego nie zgłasza. Jeśli budujesz
gdzie indziej, porównaj wagę pliku z tą w repozytorium.

`kompresuj_fba.py` **pomija pliki już przetworzone**: po poprawieniu zdjęcia albo
nagrania skasuj `k_*.jpg` bądź `*.orig.mp3`, inaczej dokument dalej pokaże
poprzednią wersję. Ta pułapka kosztowała już rundę w obu modułach.

Skrypty `.mjs` **same znajdują playwrighta** (mają fallback na
`/opt/node22/lib/node_modules`), więc uruchamiaj je wprost. Dowiązanie rób tylko
wtedy, gdy skrypt zgłosi „Nie znalazłem playwrighta" — albo gdy piszesz **własny**
jednorazowy pomiar, bo zwykłe `require('playwright')` z katalogu modułu nie
zadziała. Wtedy koniecznie **skasuj dowiązanie** po pracy, żeby nie trafiło do
repozytorium:

```bash
mkdir -p node_modules && ln -sfn /opt/node22/lib/node_modules/playwright node_modules/playwright
# ... własny pomiar ...
rm -f node_modules/playwright && rmdir node_modules
```

## Kontrola bez dotykania plików

Gdy prosi o samo sprawdzenie („czy wszystko jest kompletne", „czy się drukuje"),
nie przebudowuj dokumentów — kroki 1–3 pętli nadpisują pliki w repozytorium.
Sam `sprawdz_fba.py` i oba pomiary czytają, niczego nie zapisując, i to wystarcza
do odpowiedzi.

`build_tabela.py` nie ma `--wyjscie` i zawsze pisze w miejsce (jedyny wyjątek to
`build_cele_fba.py`). Gdy naprawdę potrzebujesz sprawdzić, czy dokument jest
aktualny wobec `src/`, skopiuj **cały katalog modułu** obok `eduplaner_przedszkole`
— inaczej zgubisz symbole, jak wyżej — i porównaj sumy kontrolne.

## Druk dla konkretnego dziecka

FBA-C składa się jako formularz albo jako gotowy druk z nazwiskiem i punktacją:

```bash
python3 src/build_cele_fba.py \
  --uczen "Zofia Lewandowska" --klasa "grupa 5-latków" --data 2026-09-15 \
  --wyniki 7,8,13,7,13 --wyjscie /poza/repozytorium/Zofia_FBA-C.html
```

`--wyniki` to punktacja pięciu funkcji z kwestionariusza; z niej biorą się
kryterium i horyzont każdego celu. **Dokument z nazwiskiem nie wchodzi do
repozytorium** (`eduplaner_fba/.gitignore`) — nazwisko i punktacja to dane osobowe
dziecka. Zapisuj go poza katalogiem projektu i powiedz jej, gdzie leży.

## Kiedy pytać, a kiedy działać

Rozbudowa treści merytorycznej to jej dziedzina. Sam dopisuj to, co wynika wprost
z tego, co już jest: brakujący arkusz do istniejącego konspektu, kartę pomocy
według wzoru sąsiednich, brakujące nagranie do istniejącego polecenia. Zapytaj,
zanim: zmienisz kryterium albo horyzont, dopiszesz nowy wskaźnik, przypiszesz
konspekt do innej funkcji zachowania.

Gdy znajdziesz brak, o który nie pytała — powiedz o nim i **uzupełnij**, zamiast
tylko raportować. W tym module brakujące elementy nie zgłaszają się same. Wyjątek:
gdy prosi o samą kontrolę, raportuj i **nie dotykaj plików** — inaczej odda jej
odpowiedź razem ze zmianami, o które nie prosiła.

## Sprawdzanie efektu oczami

Druki są wizualne, a Playwright jest w obrazie. Po większej zmianie zrób zrzut
i **obejrzyj go**, zanim powiesz, że gotowe. Zrzut ekranu wklejony w odpowiedź
**nie dociera do użytkowniczki** — pliki wysyłaj narzędziem do wysyłania plików,
nie linkiem w treści.

Przy zmianach w edytorze własnych konspektów oglądanie nie wystarcza: kliknięcia,
zapis i wydruk trzeba przeklikać skryptem. Wzór testu i lista pułapek:
`references/edytor.md`.
