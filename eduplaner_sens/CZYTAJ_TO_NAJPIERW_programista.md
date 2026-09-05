# Moduł Profil sensoryczny — EduPlaner 2026

Autorka treści: **mgr Mirosława Ewa Jurczyszyn**, pedagog specjalny, PCTP Koszalin.

To trzecia część ekosystemu EduPlaner, obok banku celów SMART KPOF i modułu ABC/FBA.
Bank KPOF opisuje, **co dziecko ma umieć**. Moduł ABC/FBA — **co dziecko robi zamiast
zachowania trudnego**. Ten moduł opisuje, **co dziecko robi, żeby poradzić sobie
z bodźcem** — i to jest jego cała idea, więc zaczynam od niej, zanim przejdę do plików.

## Rzecz, której nie wolno zgubić przy wpinaniu

Cele w tym module opisują **strategię sensoryczną**: to, co dziecko robi, gdy bodziec
jest za silny albo za słaby. Dieta sensoryczna nie usuwa objawu — daje dziecku sposób,
żeby samo zadbało o swój układ nerwowy.

„Nie będzie zatykał uszu" **nie jest** celem z tego modułu.
„Założy słuchawki wygłuszające, zanim hałas w szatni go przeciąży" — jest.

Każdy wskaźnik niesie pole `strategia_sensoryczna`. Jeżeli aplikacja pokazuje cel
bez niego, gubi to, po co ten moduł powstał.

## Od czego zacząć

**Wpina się `01_dane_json`. HTML jest wzorcem docelowym, nie źródłem.**

To najważniejsze zdanie w tym pliku. Dokumenty HTML pokazują, jak materiał ma wyglądać
u nauczyciela — są kompletne i można je otworzyć z dysku, bez serwera. Ale treść wyjęta
z HTML-a nigdy się już nie zsynchronizuje z poprawkami autorki. JSON eksportuje się
jednym poleceniem i jest przeznaczony do maszyny.

## Co jest w paczce

```
01_dane_json/          ← TO SIĘ WPINA
02_gotowe_dokumenty/   ← tak ma wyglądać efekt (HTML do druku)
03_kod_zrodlowy/       ← jak to powstaje; README_projektu.md ma szczegóły
04_media/              ← zdjęcia, nagrania i symbole
```

### `01_dane_json` — siedem plików

| plik | co niesie |
|---|---|
| `cele_sens_obserwacja.json` | 21 celów do obserwacji pogłębionej (druk SENS-C) + progi punktacji zmysłów |
| `cele_sens_poziomy.json` | 189 celów: 21 wskaźników × 3 poziomy wsparcia × 3 wersje wiekowe (druk SENS-T) |
| `konspekty_sens.json` | 63 konspekty zajęć w pełnej strukturze druku KC-3 |
| `pomoce_sens.json` | 21 kart pomocy dydaktycznych + 63 polecenia dla dziecka i instrukcje słowne dorosłego |
| `materialy_do_druku.json` | 21 arkuszy A4 do wycięcia + mapowanie na bibliotekę symboli |
| `nagrania_sens.json` | manifest 63 nagrań głosem autorki (buduje `nagrania_glos.py`) |
| `wlasne_konspekty_kontrakt.json` | kształt rekordu, w którym nauczycielka zapisuje własne scenariusze |

### Skąd bierze się 21 wskaźników

Z druku obserwacji: **7 zmysłów × 3 sektory objawów**. Sektor to kierunek zaburzenia
modulacji, a nie odcień tego samego problemu — nadwrażliwość i podwrażliwość wymagają
**przeciwnych** działań. Wzrok, słuch, dotyk, smak, węch, propriocepcja i równowaga,
każdy w sektorach: nadwrażliwość · podwrażliwość · biały szum.

### Ścieżki do mediów

Wszystkie ścieżki w JSON liczone są od katalogu **`04_media/`**:

```
04_media/eduplaner_sens/assets/pomoce_sens/p_01.jpg
04_media/eduplaner_sens/assets/audio_sens/as_01_III.mp3
04_media/eduplaner_przedszkole/assets/symbole/k_za_glosno.jpg
```

Symbole leżą w katalogu **banku KPOF** i to nie jest bałagan, tylko wymóg merytoryczny:
dziecko korzystające z komunikacji obrazkowej musi widzieć **ten sam obrazek** na karcie
z zajęć, na tablicy AAC i w planie dnia. Symbol, który zmienia wygląd między materiałami,
przestaje być dla niego słowem. Jeśli wpinasz kilka modułów, biblioteka symboli ma
zostać **jedna**.

## Cztery rzeczy, które łatwo zrobić źle

**1. Kryterium i horyzont nie są stałe.** W druku SENS-C wynikają z sumy punktów danego
zmysłu u konkretnego dziecka (tabela `progi`), w SENS-T — z poziomu wsparcia
(tabela `kryteria_poziomow`). W polu `cel` druku SENS-C zostały znaczniki `{proba}`,
`{horyzont_dopelniacz}` i `{horyzont_miejscownik}` do podstawienia. Horyzont jest
w trzech formach gramatycznych, bo wchodzi w trzy różne zdania — użycie jednej dawało
w druku dla rodzica „weryfikacja po 4 tygodni".

Kryterium na Poziomie I zostaje **4 z 5**, a nie rośnie do 5 z 5: rośnie trudność samego
zachowania, nie liczba prób. „Za każdym razem" to w przedszkolu cel nie do osiągnięcia.

**2. Cel edukacyjny konspektu nie jest w konspekcie.** Konspekt czyta go na żywo
z `cele_sens_poziomy.json` — pole `cel_edukacyjny_zrodlo` mówi, gdzie dokładnie
(niesie wzór identyfikatora i trzy gotowe identyfikatory, po jednym na wersję wiekową).
Skopiowanie celu do rekordu konspektu zadziała raz i rozjedzie się przy pierwszej
poprawce autorki.

**3. Kto co czyta, decyduje o języku.** W kartach pomocy, na arkuszach i w celach są dwa
rodzaje tekstu i nie wolno ich zamienić miejscami:

* `polecenie_dla_dziecka`, `etykieta_dla_dziecka` — mówi się to **dziecku**, krótkimi
  zdaniami, bez trudnych słów. To jest tekst nagrany głosem autorki.
* `instrukcja_slowna_doroslego`, `trzy_kroki_uzycia`, `wskazowka_dla_doroslego`,
  `opis_dla_doroslego`, `wstep_dla_doroslego` — czyta **nauczyciel**; trudne słowa są
  tam na miejscu.

W druku widać to kolorem: ramka pomarańczowa to tekst dla dziecka, fioletowa — dla
dorosłego. Aplikacja ma utrzymać ten rozdział, także w widoku mobilnym.

**4. Pole `ryzyko` nie jest ozdobnikiem.** Kocyk obciążeniowy ma limit 10% masy ciała
i nie wolno go używać podczas snu; brak reakcji na imię wymaga badania słuchu przed
pracą sensoryczną; wąski repertuar pokarmowy bywa zaburzeniem karmienia, nie kaprysem.
Jeżeli aplikacja pokazuje cel z propriocepcji lub równowagi, ma pokazać też `ryzyko`.

## Nagrania — dane biometryczne

63 pliki w `04_media/eduplaner_sens/assets/audio_sens/` to **sklonowany głos autorki**.
Głos jest daną biometryczną: nie publikuj tych plików ani nie używaj ich poza uzgodnionym
zastosowaniem w aplikacji. Nagrania mają 40 kbps mono — tyle wystarcza na głośnik tabletu
w sali i utrzymuje dokument w rozsądnej wadze.

Nagrywa się **wyłącznie** teksty `polecenie_dla_dziecka` (63 sztuki: 21 pomocy × 3 poziomy
wsparcia). Instrukcji słownych dorosłego się nie nagrywa.

Skrypt `nagrania_glos.py` celowo nie ma głosu domyślnego — brak `ELEVENLABS_VOICE_ID`
zatrzymuje pracę, zamiast podstawić w to miejsce cudzy głos.

## Jak przebudować dokumenty i JSON

```bash
cd eduplaner_sens
python3 03_kod_zrodlowy/eksport_json.py        # świeży JSON (siedem plików)
python3 03_kod_zrodlowy/build_tabela.py        # druk SENS-T z konspektami i filtrem
python3 03_kod_zrodlowy/build_cele_sens.py     # druk SENS-C (formularz)
python3 03_kod_zrodlowy/nagrania_glos.py --manifest
```

Druk SENS-C składa się też dla konkretnego dziecka:

```bash
python3 03_kod_zrodlowy/build_cele_sens.py --uczen "…" --grupa "…" --wyniki 9,17,14,6,4,19,15
```

`--wyniki` to sumy siedmiu zmysłów z druku obserwacji (0–24 każda, w kolejności druku:
wzrok, słuch, dotyk, smak, węch, propriocepcja, równowaga); z nich biorą się kryterium
i horyzont każdego celu. **Dokumenty z nazwiskiem dziecka nie wchodzą do repozytorium** —
to dane osobowe; zapisują się z prefiksem `uczen_`, który jest w `.gitignore`.

## Skala materiału

189 celów SMART · 21 celów do obserwacji · 63 konspekty zajęć · 21 pomocy dydaktycznych ·
63 polecenia dla dziecka z nagraniami · 63 instrukcje słowne dorosłego · 21 arkuszy A4
do wycięcia · 63 symbole z biblioteki wspólnej z bankiem KPOF.

Pytania o treść merytoryczną — do autorki. Pytania o strukturę danych —
`03_kod_zrodlowy/README_projektu.md` opisuje, co skąd się bierze.
