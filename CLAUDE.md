# Pamięć projektu

## Głos użytkowniczki (narracja PL)

Mirosława Ewa Jurczyszyn ma **własny sklonowany głos** w ElevenLabs i to nim —
i wyłącznie nim — nagrywamy narrację do jej materiałów.

```
voice_id  jq4ZUryuBeDqmtkKtBZ4
nazwa     Ewa - narracja PL (PCTP)   (w panelu ElevenLabs: „Ewa-głos_do skils”)
model     eleven_v3
```

Zapasowe klony tego samego głosu: `D0Yz6dyyxHOodq3Zqi45` (Ewa1),
`MxdHRlURUZPVY5h2NiXH` (Ewa2) — używaj tylko, gdy poprosi o zmianę brzmienia.

**Nigdy nie nagrywaj jej materiałów cudzym głosem.** Gdy głos jest niedostępny,
oddaj sam scenariusz i zatrzymaj się — nie podstawiaj głosu premade.

### Rejestr narracji — wypracowany i zaakceptowany wzorzec

Ten sam zestaw wskazówek aktorskich w każdej ścieżce:

| miejsce | wskazówka |
|---|---|
| otwarcie | `[warmly, smiling, telling a story to a small child]` |
| rozwinięcie | `[gently]` |
| domknięcie | `[with a smile]` |
| fragment smutny | zamiast dwóch ostatnich: `[gently, a little sad]`, `[softly]` |

Tekst mówiony ma być **czystą prozą** — pełne zdania, bez wielokropków, bez
sylabizowania („po-wo-lut-ku”), bez wtrąceń typu „o tak”. Ciepło daje wskazówka
aktorska, nie interpunkcja; nagrania robione „na wielokropkach” brzmią sztucznie
i zostały odrzucone. Model `eleven_multilingual_v2` czyta jej teksty
lektorsko — do materiałów dla dzieci używaj `eleven_v3`.

### Skąd to brać

* skill **`dane-i-glos`** — pełny łańcuch dane → scenariusz → MP3 + SRT → wideo;
  pamięta ten `voice_id` na stałe (`scripts/konfiguracja.py`, `PAMIEC_TRWALA`)
* podgląd tego, co skill pamięta:
  `python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py --pokaz`
* zmiana głosu: `... skonfiguruj_glos.py --voice-id <nowy> --nazwa "..."`
* narzędzia MCP ElevenLabs: `creative_generate_speech` z tym `voice_id`
* klucz API tylko w zmiennej `ELEVENLABS_API_KEY` — nigdy w repozytorium

## Podstawa programowa wychowania przedszkolnego (obowiązująca)

**Rozporządzenie Ministra Edukacji z 11 marca 2026 r.** (Dz. U. 2026 poz. 378),
w życie **1 września 2026 r.** Zastąpiło cztery dotychczasowe obszary rozwoju
(fizyczny, emocjonalny, społeczny, poznawczy) **dziewięcioma obszarami osiągnięć
dziecka**:

| nr | obszar | nr | obszar | nr | obszar |
|---|---|---|---|---|---|
| 1 | społeczny | 4 | matematyczny | 7 | cyfrowy |
| 2 | osobisty | 5 | przyrodniczy | 8 | artystyczny |
| 3 | językowy | 6 | techniczny | 9 | ruchowy |

Zapis punktu: `obszar.punkt` (np. `3.5`). Poza tym występują kody `DE-R`
(doświadczenie edukacyjne realizowane co najmniej raz w roku), `WSR` (warunki
i sposób realizacji) oraz `Zad.` (zadanie przedszkola).

Struktura załącznika nr 1 (zweryfikowana w oryginale
`eduplaner_przedszkole/podstawa_2026/podsawa.pdf`): cele wychowania przedszkolnego ·
I. Kompetencje fundamentalne · II. Kompetencje przekrojowe · III. Sprawczość ·
**IV. Zadania przedszkola** (16 pozycji) · **Osiągnięcia dziecka** (9 obszarów,
**113 punktów**) · **doświadczenia edukacyjne** (dwie listy) ·
**Warunki i sposób realizacji** (11 pozycji).

Liczba punktów w obszarach: 1 — 20, 2 — 12, 3 — 21, 4 — 15, 5 — 12, 6 — 9, 7 — 5,
8 — 8, 9 — 11.

**Doświadczenia edukacyjne** leżą zaraz za obszarem ruchowym, wprowadzone akapitem,
nie nagłówkiem — łatwo je przeoczyć i wciągnąć do obszaru 9 przy parsowaniu:

* „Dziecko **co najmniej raz w roku szkolnym**" — 7 pozycji, kody `DE-R.1`–`DE-R.7`
* „Dziecko **przynajmniej raz w trakcie edukacji przedszkolnej**" — 4 pozycje,
  arkusze KPOF jeszcze ich nie kodują

Punkt ciężkości przesunięty z tego, co dziecko ma umieć, na to, jak działa
i funkcjonuje — kompetencje fundamentalne i przekrojowe, sprawczość, dobrostan.
Dziewięć obszarów to mapa do planowania, nie plan zajęć: jedna dobrze
zaprojektowana sytuacja edukacyjna uruchamia zwykle kilka naraz.

**To jest obowiązująca podstawa — nie odwołuj się do rozporządzenia z 14 lutego
2017 r.** Oryginał leży w repozytorium (`podstawa_2026/podsawa.pdf`, 365 stron,
tekst wyciągalny) — sprawdzaj w nim, zamiast zgadywać.

Miejsce w kodzie: `OBSZAR_PP_NAZWY` w `monitoring_podstawy()`
(`eduplaner_przedszkole/src/build.py`) — jedno źródło dla legendy i kolumny tabeli.

## Materiały przedszkolne

`eduplaner_przedszkole/` — bank celów SMART KPOF (130 twierdzeń, wersje A/B/C),
wersja U z 48 celami uzupełniającymi domykającymi podstawę do 113/113,
130 konspektów, pomoce dydaktyczne. Szczegóły: `eduplaner_przedszkole/README.md`.

**Konspekty otwiera się ze spisu** na górze każdej wersji (numer, tytuł,
kropka = ma pomoc) albo kliknięciem komórki z celem w tabeli. Spis dodany,
bo bez niego konspektów nie dało się znaleźć.

**Pomoce dydaktyczne siedzą w konspektach** — sekcja VII modalu, przycisk
„Pokaż pomoc i posłuchaj polecenia”. Tam ich szuka nauczyciel i tam mają być.
Osobne zeszyty (`Pomoce_dydaktyczne_3-4_lata.html`, `..._5_lat.html` i ich PDF-y)
są **dodatkową drogą do druku** całego kompletu naraz, nie zamiennikiem.

Nie wyjmuj kart z banku dla rozmiaru. Sprawdzone pomiarem: bank z wszystkimi
86 kartami waży 12,3 MB i rysuje się w 348 ms. Wolne otwieranie brało się
z blokującego arkusza fontów, nie z wagi pliku.

Treść kart: `src/pomoce_a.py`, `src/pomoce_b.py`, `src/pomoce_c.py`; układ i osadzanie
mediów: `src/pomoce_karta.py`; generator zeszytów do druku: `src/build_pomoce.py`.

Obszar **techniczny (U6)** i **cyfrowy (U7)** mają własne karty pomocy w `src/pomoce_u.py`
— 14 kart ze zdjęciem i poleceniem jej głosem. Reszta wersji U (obszary 1–5, 8, 9)
ma na razie same arkusze do wydruku.

Cztery zestawy: 42 + 44 + 44 + 14 = 144 karty, każda ze zdjęciem poglądowym
(`assets/pomoce_<x>/k_<kod>.jpg`) i nagranym poleceniem jej głosem
(`assets/audio_<x>/<kod>.mp3`). Karta bez zdjęcia albo bez nagrania nie psuje budowania —
`Zestaw.braki()` pokazuje, czego brakuje, a karta dostaje pole zastępcze.

Każdy ze 130 konspektów A/B/C ma też arkusz do wydruku (`karty_druk.ARKUSZE`).
Zeszyty pomocy drukują się do A4 pionowo, po jednej karcie na stronę:
`node src/generuj_pomoce_pdf.mjs` (playwright leży w `/opt/node22/lib/node_modules` —
dowiąż go na czas uruchomienia i skasuj dowiązanie, żeby nie trafiło do repozytorium).

Arkusz fontów w każdym dokumencie ładujemy **nieblokująco**
(`media="print" onload="this.media='all'"`) — inaczej przy niedostępnym CDN
przeglądarka trzyma biały ekran kilkanaście sekund.

Twierdzenia z arkuszy KPOF i cele uzupełniające trzymamy **osobno** — wymyślonych
celów nie dopisujemy do jej kwestionariuszy.

**Materiały do wydruku** (`src/karty_druk.py`) składamy z **biblioteki symboli**
(`src/symbole.py`, obrazy w `assets/symbole/`), nie z rysunków robionych pod jeden
konspekt. Konspekty proszą o materiał 243 razy, ale to wciąż ten sam słownik: plan
dnia, mycie rąk, emocje, prośby AAC wracają w wersji A, B, C i U. Dziecko korzystające
z komunikacji obrazkowej musi widzieć **ten sam** symbol pomocy na tablicy AAC,
w planie dnia i na breloku — symbol, który zmienia wygląd między materiałami,
przestaje być słowem. Symbol nienarysowany nie ma pliku, a arkusz go używający jest
pomijany, więc dokumenty budują się poprawnie na każdym etapie.

Siedem rodzajów arkusza: `karty` (do wycięcia), `pasek` (sekwencja z numerami),
`tablica` (bez rozcinania), `tabela` (do wypełniania), `pola` (puste pola
z etykietami), `etykiety` (karteczki z polem koloru), `sciezki` (pasy do przecięcia
albo szlaczki do obrysowania, rysowane wzorem SVG). Cztery ostatnie nie potrzebują
rysunków i są w konspektach większością.

**Każdy ze 178 konspektów ma materiał do wydruku** — 204 arkusze. Wszystkie mieszczą
się na jednej stronie A4 pionowo; pilnują tego `_kolumny()` (dokłada kolumn, gdy
kafle nie wchodzą) i `_rozciag()` (rozciąga pola, gdy zostaje pusta kartka).
Budżet strony: szerokość druku 726 px, na siatkę zostaje 745 px po nagłówku arkusza.
Po zmianie układu arkusza sprawdź pomiarem, czy nic nie wyszło poza stronę.

Arkusz `tabela` musi mieć `min-width:0` — tabela banku celów ma `min-width:1080px`
i bez tego wyjątku arkusz ucieka poza krawędź strony.

Bank drukuje się **poziomo** (tabela z trzema poziomami obok siebie), ale arkusze
i karty pomocy mają własną stronę pionową: `@page arkusz{size:A4 portrait}` plus
`.zal{page:arkusz}`. Zeszyty konspektów muszą cofać u siebie regułę banku
`@media print{.kmodal{display:none}}` — bez tego cały zeszyt wychodził z drukarki
jako jedna pusta strona.

**Wykaz konspektów** układamy siatką `minmax(232px,1fr)` z podziałem na obszary,
nie rzędem pigułek — pigułka miała szerokość swojego tytułu, więc kolumny nie
trzymały pionu. Rozwija się kliknięciem (i w banku, i w zeszytach), a pasek
rozwijania jest w kolorze akcentu `--accent`; nagłówki obszarów też. Wykaz
schowany pod szarą belką nauczyciel przeoczy — to już raz zdarzyło się w tym
projekcie.

Ilustracje do konspektów generujemy modelem `gemini-2.5-flash-image`
(`creative_generate_image`) — spójny styl książeczkowy, pastelowa paleta,
ta sama bohaterka w całej historyjce.
