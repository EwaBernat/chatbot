# Moduł FBA/PBS — EduPlaner 2026

Autorka treści: **mgr Mirosława Ewa Jurczyszyn**, pedagog specjalny, PCTP Koszalin.

To druga część ekosystemu EduPlaner, obok banku celów SMART KPOF. Bank opisuje,
**co dziecko ma umieć**. Ten moduł opisuje, **co dziecko robi zamiast zachowania
trudnego** — i to jest jego cała idea, więc zaczynam od niej, zanim przejdę do
plików.

## Rzecz, której nie wolno zgubić przy wpinaniu

Cele w tym module opisują **zachowanie zastępcze**: inną drogę do tej samej
potrzeby, którą dziecko załatwia zachowaniem trudnym. Plan PBS nie odbiera
dziecku funkcji — uczy innego sposobu, żeby ją zaspokoić.

„Nie będzie uciekał od stolika" **nie jest** celem z tego modułu.
„Poprosi o przerwę kartą, zanim wyjdzie od stolika" — jest.

Każdy wskaźnik niesie pole `zachowanie_zastepcze`. Jeżeli aplikacja pokazuje cel
bez niego, gubi to, po co ten moduł powstał.

## Od czego zacząć

**Wpina się `01_dane_json`. HTML jest wzorcem docelowym, nie źródłem.**

To najważniejsze zdanie w tym pliku. Dokumenty HTML pokazują, jak materiał ma
wyglądać u nauczyciela — są kompletne i można je otworzyć z dysku, bez serwera.
Ale treść wyjęta z HTML-a nigdy się już nie zsynchronizuje z poprawkami autorki.
JSON eksportuje się jednym poleceniem i jest przeznaczony do maszyny.

## Co jest w paczce

```
01_dane_json/          ← TO SIĘ WPINA
02_gotowe_dokumenty/   ← tak ma wyglądać efekt (HTML + PDF)
03_kod_zrodlowy/       ← jak to powstaje; README_projektu.md ma szczegóły
04_media/              ← zdjęcia, nagrania i symbole
```

### `01_dane_json` — sześć plików

| plik | co niesie |
|---|---|
| `cele_fba_obserwacja.json` | 25 celów do obserwacji pogłębionej (druk FBA-C) + progi punktacji funkcji |
| `cele_fba_poziomy.json` | 225 celów: 25 wskaźników × 3 poziomy wsparcia × 3 wersje wiekowe (druk FBA-T) |
| `konspekty_fba.json` | 75 konspektów zajęć w pełnej strukturze druku KC-3 |
| `pomoce_fba.json` | 25 kart pomocy dydaktycznych + 75 poleceń dla dziecka |
| `materialy_do_druku.json` | 25 arkuszy A4 do wycięcia + mapowanie na bibliotekę symboli |
| `wlasne_konspekty_kontrakt.json` | kształt rekordu, w którym nauczycielka zapisuje własne scenariusze |

### Ścieżki do mediów

Wszystkie ścieżki w JSON liczone są od katalogu **`04_media/`**:

```
04_media/eduplaner_fba/assets/pomoce_fba/k_i_1.jpg
04_media/eduplaner_fba/assets/audio_fba/ai_1.mp3
04_media/eduplaner_przedszkole/assets/symbole/k_postawa_stolik.jpg
```

Symbole leżą w katalogu **banku KPOF** i to nie jest bałagan, tylko wymóg
merytoryczny: dziecko korzystające z komunikacji obrazkowej musi widzieć **ten
sam obrazek** na karcie z zajęć, na tablicy AAC i w planie dnia. Symbol, który
zmienia wygląd między materiałami, przestaje być dla niego słowem. Jeśli wpinasz
oba moduły, biblioteka symboli ma zostać **jedna**.

## Trzy rzeczy, które łatwo zrobić źle

**1. Kryterium i horyzont nie są stałe.** W druku FBA-C wynikają z punktacji danej
funkcji u konkretnego dziecka (tabela `progi`), w FBA-T — z poziomu wsparcia.
W polu `cel` druku FBA-C zostały znaczniki `{proba}` i `{horyzont}` do
podstawienia. Horyzont jest w trzech formach gramatycznych, bo wchodzi w trzy
różne zdania — użycie jednej dawało w druku dla rodzica „weryfikacja po
4 tygodni".

Kryterium na Poziomie I zostaje **4 z 5**, a nie rośnie do 5 z 5: rośnie trudność
samego zachowania, nie liczba prób. „Za każdym razem" to w przedszkolu cel nie do
osiągnięcia.

**2. Cel edukacyjny konspektu nie jest w konspekcie.** Konspekt czyta go na żywo
z `cele_fba_poziomy.json` — pole `cel_edukacyjny_zrodlo` mówi, gdzie dokładnie.
Skopiowanie celu do rekordu konspektu zadziała raz i rozjedzie się przy pierwszej
poprawce autorki.

**3. Kto co czyta, decyduje o języku.** W kartach pomocy i na arkuszach są dwa
rodzaje tekstu i nie wolno ich zamienić miejscami:

* `polecenie_dla_dziecka`, `etykieta_dla_dziecka` — mówi się to **dziecku**,
  krótkimi zdaniami, bez trudnych słów. To jest tekst nagrany głosem autorki.
* `trzy_kroki_uzycia`, `wskazowka_dla_doroslego`, `opis_dla_doroslego`,
  `wstep_dla_doroslego` — czyta **nauczyciel**; trudne słowa są tam na miejscu.

## Nagrania — dane biometryczne

75 plików w `04_media/eduplaner_fba/assets/audio_fba/` to **sklonowany głos
autorki**. Głos jest daną biometryczną: nie publikuj tych plików ani nie używaj
ich poza uzgodnionym zastosowaniem w aplikacji. Nagrania mają 40 kbps mono —
tyle wystarcza na głośnik tabletu w sali i utrzymuje dokument w rozsądnej wadze.

## Jak przebudować dokumenty i JSON

```bash
cd eduplaner_fba
python3 src/build_tabela.py        # druk FBA-T z konspektami i edytorem
python3 src/build_cele_fba.py      # druk FBA-C (formularz albo dla ucznia)
python3 src/eksport_json.py        # świeży JSON
node    src/do_pdf.mjs             # PDF-y
```

Druk FBA-C składa się też dla konkretnego dziecka:

```bash
python3 src/build_cele_fba.py --uczen "…" --klasa "…" --wyniki 7,8,13,7,13
```

`--wyniki` to punktacja pięciu funkcji z kwestionariusza; z niej biorą się
kryterium i horyzont każdego celu. **Dokumenty z nazwiskiem dziecka nie wchodzą
do repozytorium** — to dane osobowe.

## Skala materiału

225 celów SMART · 75 konspektów zajęć · 25 pomocy dydaktycznych · 75 nagrań ·
25 arkuszy A4 do wycięcia · 172 symbole z biblioteki wspólnej z bankiem KPOF.

Pytania o treść merytoryczną — do autorki. Pytania o strukturę danych —
`03_kod_zrodlowy/README_projektu.md` opisuje, co skąd się bierze.
