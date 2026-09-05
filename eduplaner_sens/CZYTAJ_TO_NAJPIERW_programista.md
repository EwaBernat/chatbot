# Moduł Profil sensoryczny — EduPlaner 2026

Autorka treści: **mgr Mirosława Ewa Jurczyszyn**, pedagog specjalny, PCTP Koszalin.

Trzecia część ekosystemu EduPlaner, obok banku celów SMART KPOF i modułu ABC/FBA.
Bank KPOF opisuje, **co dziecko ma umieć**. Moduł ABC/FBA — **co dziecko robi zamiast
zachowania trudnego**. Ten moduł opisuje, **co dziecko robi, gdy bodziec jest za silny
albo za słaby** — i to jest jego cała idea, więc zaczynam od niej.

Struktura plików, nazwy pól i układ druków są **takie same jak w module ABC/FBA** —
aplikacja czyta oba moduły tym samym kodem.

## Rzecz, której nie wolno zgubić przy wpinaniu

Cele w tym module opisują **strategię sensoryczną**: to, co dziecko robi, gdy układ
nerwowy dostaje za dużo albo za mało bodźca. Dieta sensoryczna nie usuwa objawu — daje
dziecku sposób, żeby samo zadbało o siebie.

„Nie będzie zatykał uszu" **nie jest** celem z tego modułu.
„Założy słuchawki wygłuszające, zanim hałas w szatni go przeciąży" — jest.

Każdy wskaźnik niesie pole `strategia_sensoryczna` — odpowiednik `zachowanie_zastepcze`
z modułu FBA. Jeżeli aplikacja pokazuje cel bez niego, gubi to, po co ten moduł powstał.

## Od czego zacząć

**Wpina się `01_dane_json`. HTML jest wzorcem docelowym, nie źródłem.**

Dokumenty HTML pokazują, jak materiał ma wyglądać u nauczyciela — są kompletne i można
je otworzyć z dysku, bez serwera. Ale treść wyjęta z HTML-a nigdy się już nie
zsynchronizuje z poprawkami autorki. JSON eksportuje się jednym poleceniem.

## Co jest w paczce

```
01_dane_json/          ← TO SIĘ WPINA
02_gotowe_dokumenty/   ← tak ma wyglądać efekt
03_kod_zrodlowy/       ← jak to powstaje; README_projektu.md ma szczegóły
04_media/              ← zdjęcia, nagrania i symbole
```

### `01_dane_json` — siedem plików

| plik | co niesie |
|---|---|
| `cele_sens_obserwacja.json` | 21 celów do obserwacji pogłębionej (druk SENS-C) + progi punktacji zmysłów |
| `cele_sens_poziomy.json` | 189 celów: 21 wskaźników × 3 wersje wiekowe × 3 poziomy wsparcia (druk SENS-T) |
| `konspekty_sens.json` | 63 konspekty zajęć w pełnej strukturze druku KC-3 |
| `pomoce_sens.json` | 21 kart pomocy dydaktycznych + 63 polecenia dla dziecka |
| `materialy_do_druku.json` | 21 arkuszy A4 do wycięcia + mapowanie na bibliotekę symboli |
| `nagrania_sens.json` | manifest 63 nagrań głosem autorki (buduje `nagrania_glos.py`) |
| `wlasne_konspekty_kontrakt.json` | kształt rekordu, w którym nauczycielka zapisuje własne scenariusze |

### Skąd bierze się 21 wskaźników

Z druku obserwacji: **7 zmysłów × 3 sektory objawów**, numerowane jak funkcje w FBA —
`I.1` … `VII.3`. Sektor to kierunek zaburzenia modulacji, nie odcień tego samego
problemu: nadwrażliwość i podwrażliwość wymagają **przeciwnych** działań.

| zmysł | ICF | wskaźniki |
|---|---|---|
| I Wzrok | b210 | I.1 nadwrażliwość · I.2 podwrażliwość · I.3 biały szum |
| II Słuch | b230 | II.1 · II.2 · II.3 |
| III Dotyk | b265 | III.1 · III.2 · III.3 |
| IV Smak | b250 | IV.1 · IV.2 · IV.3 |
| V Węch | b255 | V.1 · V.2 · V.3 |
| VI Propriocepcja | b760 | VI.1 · VI.2 · VI.3 |
| VII Równowaga | b235 | VII.1 · VII.2 · VII.3 |

### Ścieżki do mediów

Wszystkie ścieżki w JSON liczone są od katalogu **`04_media/`**, tak jak w FBA:

```
04_media/eduplaner_sens/assets/pomoce_sens/k_vi_2.jpg
04_media/eduplaner_sens/assets/audio_sens/ai_1.mp3
04_media/eduplaner_przedszkole/assets/symbole/k_za_glosno.jpg
```

Symbole leżą w katalogu **banku KPOF** i to nie jest bałagan, tylko wymóg merytoryczny:
dziecko korzystające z komunikacji obrazkowej musi widzieć **ten sam obrazek** na karcie
z zajęć, na tablicy AAC i w planie dnia. Jeśli wpinasz kilka modułów, biblioteka symboli
ma zostać **jedna**. `plik_symbolu: null` to **pole celowo puste** — miejsce na własny
symbol dziecka.

## Cztery rzeczy, które łatwo zrobić źle

**1. Kryterium i horyzont nie są stałe.** W druku SENS-C wynikają z sumy punktów danego
zmysłu u konkretnego dziecka (tabela `progi`, pole `od_punktow`), w SENS-T — z poziomu
wsparcia (`poziomy_wsparcia`). W polu `cel` druku SENS-C zostały znaczniki `{proba}`,
`{horyzont_dopelniacz}` i `{horyzont_miejscownik}`. Horyzont jest w trzech formach
gramatycznych, bo wchodzi w trzy różne zdania — użycie jednej dawało w druku dla rodzica
„weryfikacja po 4 tygodni".

Kryterium na Poziomie I zostaje **4 z 5**, a nie rośnie do 5 z 5: rośnie trudność samego
zachowania, nie liczba prób.

**2. Cel edukacyjny konspektu nie jest w konspekcie.** Konspekt czyta go na żywo
z `cele_sens_poziomy.json` — pole `cel_edukacyjny_zrodlo` mówi, gdzie dokładnie
(`zmysly[VI].wskazniki[VI.2].cele[B]`). W druku SENS-T robi to JavaScript: po kliknięciu
w komórkę tabeli konspekt czyta jej treść z DOM, a nie z własnej kopii. Skopiowanie celu
do rekordu konspektu zadziała raz i rozjedzie się przy pierwszej poprawce autorki.

**3. Jeden konspekt obsługuje trzy poziomy wsparcia.** Konspektów jest 63, nie 189:
21 wskaźników × 3 wersje wiekowe. Poziom zmienia **sekcję VI** (modyfikacje), nie
przebieg zajęć — dokładnie jak w FBA.

**4. Kto co czyta, decyduje o języku.** Dwa rodzaje tekstu, których nie wolno zamienić
miejscami:

* `polecenie_dla_dziecka`, `etykieta_dla_dziecka` — mówi się to **dziecku**, krótkimi
  zdaniami, bez trudnych słów. To jest tekst nagrany głosem autorki.
* `trzy_kroki_uzycia`, `wskazowka_dla_doroslego`, `co_przygotowac`, `opis_dla_doroslego`,
  `wstep_dla_doroslego`, `zasada_si` — czyta **nauczyciel**; trudne słowa są tam na miejscu.

W druku widać to kolorem: ramka pomarańczowa to tekst dla dziecka, fioletowa — dla dorosłego.

**Do tego pole `bezpieczenstwo` nie jest ozdobnikiem.** Kocyk obciążeniowy ma limit 10%
masy ciała i nie wolno go używać podczas snu; brak reakcji na imię wymaga badania słuchu
przed pracą sensoryczną; wąski repertuar pokarmowy bywa zaburzeniem karmienia. Cel
z propriocepcji albo równowagi ma się pokazywać razem z tym polem.

## Druki w `02_gotowe_dokumenty`

| plik | co to jest |
|---|---|
| `Tabela_celow_SENS_wiek_poziom.html` | druk SENS-T — zakładki wersji wiekowych, jedna tabela 189 celów, kliknięcie w cel otwiera konspekt z wyróżnionym poziomem; edytor własnych konspektów |
| `Cele_SMART_SENS_obserwacja_poglebiona.html` | druk SENS-C — 9 stron A4: wprowadzenie, 7 zmysłów po trzy cele, ewaluacja |

Druk SENS-T zapisuje własne konspekty nauczycielki w pamięci przeglądarki pod kluczem
`eduplaner2026.moje-konspekty-sens.v1`, w kształcie z `wlasne_konspekty_kontrakt.json`.

## Nagrania — dane biometryczne

63 pliki w `04_media/eduplaner_sens/assets/audio_sens/` to **sklonowany głos autorki**.
Głos jest daną biometryczną: nie publikuj tych plików ani nie używaj ich poza uzgodnionym
zastosowaniem w aplikacji. Nagrania mają 40 kbps mono — tyle wystarcza na głośnik tabletu
w sali.

Nagrywa się **wyłącznie** teksty `polecenie_dla_dziecka` (63 sztuki: 21 pomocy × 3 wersje
wiekowe). Instrukcji dla nauczyciela się nie nagrywa. Skrypt `nagrania_glos.py` celowo
nie ma głosu domyślnego — brak `ELEVENLABS_VOICE_ID` zatrzymuje pracę, zamiast podstawić
cudzy głos.

## Jak przebudować dokumenty i JSON

```bash
cd eduplaner_sens
python3 03_kod_zrodlowy/eksport_json.py        # świeży JSON (sześć plików)
python3 03_kod_zrodlowy/build_tabela.py        # druk SENS-T z konspektami i edytorem
python3 03_kod_zrodlowy/build_cele_sens.py     # druk SENS-C (formularz)
python3 03_kod_zrodlowy/nagrania_glos.py --manifest
```

Druk SENS-C składa się też dla konkretnego dziecka:

```bash
python3 03_kod_zrodlowy/build_cele_sens.py --uczen "…" --grupa "…" --wyniki 9,17,14,6,4,19,15
```

`--wyniki` to sumy siedmiu zmysłów z druku obserwacji (0–24 każda, w kolejności druku);
z nich biorą się kryterium i horyzont każdego celu. **Dokumenty z nazwiskiem dziecka nie
wchodzą do repozytorium** — zapisują się z prefiksem `uczen_`, który jest w `.gitignore`.

## Skala materiału

189 celów SMART · 21 celów do obserwacji · 63 konspekty zajęć · 21 pomocy dydaktycznych ·
63 polecenia dla dziecka z nagraniami · 21 arkuszy A4 do wycięcia · 147 pól symboli
z biblioteki wspólnej z bankiem KPOF.

Pytania o treść merytoryczną — do autorki. Pytania o strukturę danych —
`03_kod_zrodlowy/README_projektu.md`.
