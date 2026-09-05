# Moduł Teoria umysłu (ToM) — EduPlaner 2026

Autorka treści: **mgr Mirosława Ewa Jurczyszyn**, pedagog specjalny, PCTP Koszalin.

Czwarta część ekosystemu EduPlaner, obok banku celów SMART KPOF, modułu ABC/FBA
i banku profilu sensorycznego. Bank KPOF opisuje, **co dziecko ma umieć**. ABC/FBA —
**co dziecko robi zamiast zachowania trudnego**. Profil sensoryczny — **co robi, gdy
bodziec jest za silny albo za słaby**. Ten moduł opisuje, **co dziecko robi albo mówi,
po czym widać, że uwzględniło cudzą perspektywę**.

Struktura plików, nazwy pól i układ druków są **takie same jak w module ABC/FBA
i w banku sensorycznym** — aplikacja czyta wszystkie moduły tym samym kodem.

## Rzecz, której nie wolno zgubić przy wpinaniu

Cele w tym module opisują **krok mentalizacji, który widać**. Rozumienia nie da się
zaobserwować ani policzyć w arkuszu obserwacji.

„Zrozumie, że inni myślą inaczej” **nie jest** celem z tego modułu.
„Wskaże koszyk, w którym Ala będzie szukać piłki, choć samo wie, że piłka jest
w pudełku” — jest.

Każdy wskaźnik niesie pole `krok_mentalizacji` — odpowiednik `zachowanie_zastepcze`
z FBA i `strategia_sensoryczna` z banku sensorycznego. Cel bez niego wraca do opisu
stanu wewnętrznego, którego nikt nie policzy.

## Od czego zacząć

**Wpina się `01_dane_json`. HTML jest wzorcem docelowym, nie źródłem.**

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
| `cele_tom_obserwacja.json` | 25 celów do obserwacji pogłębionej (druk TOM-C) + progi punktacji komponentów |
| `cele_tom_poziomy.json` | 225 celów: 25 wskaźników × 3 wersje wiekowe × 3 poziomy wsparcia (druk TOM-T) |
| `konspekty_tom.json` | 75 konspektów zajęć w pełnej strukturze druku KC-3 |
| `pomoce_tom.json` | 25 kart pomocy dydaktycznych + 75 poleceń dla dziecka |
| `materialy_do_druku.json` | 25 arkuszy A4 do wycięcia + mapowanie na bibliotekę symboli |
| `nagrania_tom.json` | manifest 75 nagrań głosem autorki (buduje `nagrania_glos.py`) |
| `wlasne_konspekty_kontrakt.json` | kształt rekordu, w którym nauczycielka zapisuje własne scenariusze |

### Skąd bierze się 25 wskaźników

Z karty obserwacji ToM: **5 komponentów × 5 pozycji**, numerowane `I.1` … `V.5`.

| komponent | ICF | norma rozwojowa | wskaźniki |
|---|---|---|---|
| I Rozpoznawanie i nazywanie emocji | b152 · b1521 | 2–4 r.ż. | I.1 … I.5 |
| II Różne pragnienia i upodobania | b1560 · d7104 | ok. 3 r.ż. | II.1 … II.5 |
| III Zabawa „na niby” i udawanie | b1640 · d880 | 2–4 r.ż. | III.1 … III.5 |
| IV Różne przekonania i fałszywe przekonanie | b1641 · d710 | 3–5 r.ż. | IV.1 … IV.5 |
| V Ukryte emocje i intencje | b1641 · d740 | 3–6 r.ż. | V.1 … V.5 |

### Ścieżki do mediów

Wszystkie ścieżki w JSON liczone są od katalogu **`04_media/`**:

```
04_media/eduplaner_tom/assets/pomoce_tom/k_iv_4.jpg
04_media/eduplaner_tom/assets/audio_tom/biv_4.mp3
04_media/eduplaner_przedszkole/assets/symbole/k_emocja_radosc.jpg
```

Symbole leżą w katalogu **banku KPOF** — biblioteka symboli ma zostać **jedna** dla
wszystkich modułów. `plik_symbolu: null` to **pole celowo puste**, na własny symbol dziecka.

## Pięć rzeczy, które łatwo zrobić źle

**1. Skala idzie w drugą stronę niż w profilu sensorycznym.** Tu **im wyżej, tym lepiej**:
wynik komponentu 0–10, gdzie 8–10 to zasób, 4–7 wymaga wsparcia, a 0–3 to priorytet.
W tabeli `progi` pole `od_punktow` czyta się jak w FBA (od najwyższego), ale znaczenie
pasm jest odwrotne. Pomylenie kierunku daje plan pracy nad mocnymi stronami dziecka.

**2. Kryterium i horyzont nie są stałe.** W druku TOM-C wynikają z wyniku komponentu
(tabela `progi`), w TOM-T — z poziomu wsparcia. W polu `cel` druku TOM-C zostały
znaczniki `{proba}`, `{horyzont_dopelniacz}` i `{horyzont_miejscownik}`. Horyzont jest
w trzech formach gramatycznych, bo wchodzi w trzy różne zdania.

**3. Kolejność wskaźników jest rozwojowa i nie da się jej przeskoczyć.** Sekwencja
Wellmana i Liu: różne pragnienia (II) → różne przekonania (IV.1) → dostęp do wiedzy
(IV.2) → fałszywe przekonanie (IV.3, IV.4) → ukryte emocje (V.1). Cel z IV.4 ustawiony
u dziecka, które nie ma IV.1, uczy zgadywania. Każdy wskaźnik niesie pole
`uwaga_rozwojowa` z typowym wiekiem — aplikacja ma je pokazywać razem z celem.

**4. Cel edukacyjny konspektu nie jest w konspekcie.** Konspekt czyta go na żywo
z `cele_tom_poziomy.json` — pole `cel_edukacyjny_zrodlo` mówi, gdzie dokładnie
(`komponenty[IV].wskazniki[IV.4].cele[B]`). W druku TOM-T robi to JavaScript: po
kliknięciu w komórkę tabeli konspekt czyta jej treść z DOM, a nie z własnej kopii.

**5. Kto co czyta, decyduje o języku.** `polecenie_dla_dziecka` i `etykieta_dla_dziecka`
mówi się **dziecku** — to teksty nagrane głosem autorki. `trzy_kroki_uzycia`,
`wskazowka_dla_doroslego`, `co_przygotowac`, `zasada_tom` czyta **nauczyciel**.
W druku widać to kolorem ramki.

## Druki w `02_gotowe_dokumenty`

| plik | co to jest |
|---|---|
| `Tabela_celow_TOM_wiek_poziom.html` | druk TOM-T — zakładki wersji wiekowych, jedna tabela 225 celów, kliknięcie w cel otwiera konspekt z wyróżnionym poziomem; edytor własnych konspektów |
| `Cele_SMART_TOM_obserwacja_poglebiona.html` | druk TOM-C — 7 stron A4: wprowadzenie z normą rozwojową i progami, pięć stron komponentów po pięć celów, ewaluacja |

Własne konspekty nauczycielki zapisują się w pamięci przeglądarki pod kluczem
`eduplaner2026.moje-konspekty-tom.v1`, w kształcie z `wlasne_konspekty_kontrakt.json`.

## Nagrania — dane biometryczne

75 plików w `04_media/eduplaner_tom/assets/audio_tom/` to **sklonowany głos autorki**.
Głos jest daną biometryczną: nie publikuj tych plików ani nie używaj poza uzgodnionym
zastosowaniem w aplikacji. Nagrywa się wyłącznie `polecenie_dla_dziecka` (25 pomocy ×
3 wersje wiekowe). Skrypt `nagrania_glos.py` nie ma głosu domyślnego — brak
`ELEVENLABS_VOICE_ID` zatrzymuje pracę, zamiast podstawić cudzy głos.

## Jak przebudować dokumenty i JSON

```bash
cd eduplaner_tom
python3 03_kod_zrodlowy/eksport_json.py        # świeży JSON (sześć plików)
python3 03_kod_zrodlowy/build_tabela.py        # druk TOM-T z konspektami i edytorem
python3 03_kod_zrodlowy/build_cele_tom.py      # druk TOM-C (formularz)
python3 03_kod_zrodlowy/nagrania_glos.py --manifest
```

Druk TOM-C składa się też dla konkretnego dziecka:

```bash
python3 03_kod_zrodlowy/build_cele_tom.py --uczen "…" --grupa "…" --wyniki 8,6,3,1,2
```

`--wyniki` to wyniki pięciu komponentów z karty obserwacji (0–10 każdy, w kolejności
karty). **Dokumenty z nazwiskiem dziecka nie wchodzą do repozytorium** — zapisują się
z prefiksem `uczen_`, który jest w `.gitignore`.

## Skala materiału

225 celów SMART · 25 celów do obserwacji · 75 konspektów zajęć · 25 pomocy dydaktycznych ·
75 poleceń dla dziecka z nagraniami · 25 arkuszy A4 do wycięcia · 175 pól symboli
z biblioteki wspólnej z bankiem KPOF.

Pytania o treść merytoryczną — do autorki. Pytania o strukturę danych —
`03_kod_zrodlowy/README_projektu.md`.

## Zdjęcia, karty pracy i głos (aktualizacja)

W konspekcie, w sekcji **VII Materiały do wydruku**, karta pomocy ma teraz
zdjęcie gotowej pomocy. Zdjęcie jest wklejone w dokument (base64, jedna reguła
CSS na plik), więc konspekt drukuje się razem ze zdjęciem także wtedy, gdy plik
HTML otworzy się bez katalogu `04_media`. Układ konspektu (I–VII) nie zmienił się.

`build_karty_pracy.py` generuje osobny druk **Karty_pracy_TOM.html** — jedna
strona A4 na wskaźnik, karty 9 × 9 cm z liniami cięcia, pasek kolejności,
zdjęcie pomocy i wszystkie trzy polecenia dla dziecka.

    python3 03_kod_zrodlowy/build_karty_pracy.py

**Głos.** Nagrania poleceń leżą w `04_media/.../audio_tom/`.
Dokument domyślnie tylko je linkuje — dzięki temu wersja w repozytorium nie
zawiera sklonowanego głosu autorki (dana biometryczna, patrz `.gitignore`).
Żeby zrobić sobie plik grający z pendrive'a, bez katalogu mediów:

    python3 03_kod_zrodlowy/build_tabela.py --z-glosem
    python3 03_kod_zrodlowy/build_karty_pracy.py --z-glosem

Takiego pliku nie commituje się do repozytorium.
