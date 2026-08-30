# Bank celów SMART · KPOF (EduPlaner 2026 · PCTP)

Zestaw gotowych celów SMART do Kwestionariusza Przedszkolnej Oceny Funkcjonalnej (KPOF),
do wykorzystania w IPET i PEWS.

- **130 twierdzeń** KPOF w 3 wersjach wiekowych (A 3–4 lata · B 5 lat · C 6 lat)
- **390 celów** — po jednym na każdy poziom wsparcia (III / II / I) dla każdego twierdzenia
- każdy cel niesie kod **ICF (d1–d9)** i punkt **podstawy programowej** z arkusza KPOF
- obszary z wynikiem 4,0–5,0 (Zasób) opisane jako **dźwignia**, nie jako cel naprawczy

## Pliki

| Plik | Opis |
|---|---|
| `Bank_celow_SMART_KPOF.html` | druk KC-1: układ tabelaryczny (styl Kącika Dyrektora), zakładki wersji, filtr kolumn, wyszukiwarka |
| `Bank_celow_SMART_KPOF.pdf` | wersja do druku (39 stron A4 **poziomo**: bank KC-1 + konspekt KC-2) |
| `src/dane_34.py`, `src/dane_5.py`, `src/dane_6.py` | bank celów jako dane (obszary, twierdzenia, cele, miary) |
| `Konspekty_KC3_ObszarVII_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru VII (3–4 lata), A4 pionowo |
| `Konspekty_KC3_ObszarI_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru I (3–4 lata), A4 pionowo |
| `Konspekty_KC3_ObszarII_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru II (3–4 lata) |
| `Konspekty_KC3_ObszarIII_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru III (3–4 lata) |
| `Konspekty_KC3_ObszarIV_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru IV (3–4 lata) |
| `Konspekty_KC3_ObszarV_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru V (3–4 lata) |
| `Konspekty_KC3_ObszarVI_3-4lata.pdf` | 3 konspekty KC-3 dla obszaru VI (3–4 lata) |
| `Konspekty_KC3_ObszarVIII_3-4lata.pdf` | 5 konspektów KC-3 dla obszaru VIII (3–4 lata) |
| `Konspekty_KC3_ObszarIX_3-4lata.pdf` | 4 konspekty KC-3 dla obszaru IX (3–4 lata) |
| `src/build.py` | generator druku KC-1 (HTML) |
| `src/konspekty_34_d7.py` | dane konspektów KC-3: obszar VII, wersja A |
| `src/konspekty_34_d1.py` | dane konspektów KC-3: obszar I, wersja A |
| `src/konspekty_34_d2.py` | dane konspektów KC-3: obszar II, wersja A |
| `src/konspekty_34_d3.py` | dane konspektów KC-3: obszar III, wersja A |
| `src/konspekty_34_d4.py` | dane konspektów KC-3: obszar IV, wersja A |
| `src/konspekty_34_d5.py` | dane konspektów KC-3: obszar V, wersja A |
| `src/konspekty_34_d6.py` | dane konspektów KC-3: obszar VI, wersja A |
| `src/konspekty_34_d8.py` | dane konspektów KC-3: obszar VIII, wersja A |
| `src/konspekty_34_d9.py` | dane konspektów KC-3: obszar IX, wersja A |
| `src/build_karty.py.bak` | poprzedni generator w układzie kart |

## Generowanie

```bash
python3 src/build.py          # → Bank_celow_SMART_KPOF.html
```

## Konwencja celu

| Poziom | Średnia KPOF | Wsparcie w celu | Horyzont ewaluacji |
|---|---|---|---|
| Zasób | 4,0–5,0 | rola w grupie wykorzystująca mocną stronę | — |
| Poziom I | 3,0–3,9 | samodzielność i przeniesienie na nową sytuację | 12 tygodni |
| Poziom II | 2,0–2,9 | wsparcie częściowe (plan obrazkowy, przypomnienie) | 8 tygodni |
| Poziom III | poniżej 2,0 | pełne wsparcie, modelowanie, warunki uproszczone | 4 tygodnie |

Reguła nadrzędna: twierdzenie ocenione na 1 lub 2 bierze cel z wiersza **Poziom III**,
niezależnie od średniej całego obszaru.

Marka: EduPlaner2026-MJ-PCTP · pedagog specjalny mgr Mirosława Ewa Jurczyszyn

## Układ druku KC-1

Jedna tabela na obszar ICF, kolumny:

`Lp.` · `Twierdzenie KPOF + miara` · `ICF` (czerwony) · `Podstawa` (niebieski) ·
`Poziom III` · `Poziom II` · `Poziom I`

Trzy poziomy stoją obok siebie, więc widać progresję wymagań w jednym rzucie oka.
Nad każdą tabelą — w druku na każdej stronie — powtarza się pasek identyfikacyjny
z wersją wiekową i nazwą obszaru. Druk: A4 poziomo.

## Paleta EduPlaner 2026 (odczytana z druku WOPF przedszkolnego)

| Rola | Hex |
|---|---|
| Głęboki fiolet — tytuły, pasek identyfikacyjny, koło PCTP | `#2D1B69` |
| Indygo — pasek nagłówka tabeli, pas wersji | `#4F3AA8` |
| Fiolet akcentowy — etykiety uppercase, ikony, obwódki | `#6C4CC4` |
| Pomarańcz — pastylki, kwadraty sekcji, wyróżnienia | `#E8450A` |
| Tło pól i kart | `#EFEAF9` |
| Tło callout / legendy | `#F6F3FC` |
| Wiersz parzysty tabeli | `#F4F0FD` |
| Wiersz nieparzysty | `#FEFDFF` |
| Linia / ramka | `#E3DCF5` |
| Tekst treści | `#2F2A3E` |
| Tekst drugorzędny, stopka | `#8A8498` |

Kolory funkcyjne (poziomy wsparcia i kody) — używane oszczędnie, jako kropka
i 3-pikselowe podkreślenie w nagłówku kolumny oraz bardzo jasne tło kolumny:
`Poziom III #C2410C` · `Poziom II #9A6B08` · `Poziom I #0F7B5A` ·
`ICF #C1121F` · `Podstawa #4F3AA8` (indygo marki — w drukach EduPlanera nie ma czystego błękitu) · `Zasób #2B6E6E`.

Typografia: DM Sans (całość) + JetBrains Mono (kody ICF, podstawa, miary).
Zaokrąglenia 7–9 px, jak w drukach WOPF i KPOF.

## Druk KC-2 — konspekt zajęć

Konspekt nie powiela celów: cytuje je z banku po numerze twierdzenia
(`KC-1 / B / 8`) wraz z kodem ICF i punktem podstawy programowej, więc zapis
w dzienniku, w IPET i w arkuszu KPOF mówi tym samym kodem. Sekcje druku:

1. **Cele z banku KC-1** — numer, ICF, podstawa, poziom wsparcia, treść, miara
2. **Przebieg zajęć** — etap · czas · czynności nauczyciela · czynności dzieci · pomoce
3. **Dostosowania wg poziomu wsparcia** — ta sama aktywność na trzech progach wymagań
4. **Ewaluacja** — kryterium sukcesu, próg, wynik do zaznaczenia, uwagi zespołu, podpisy

W repozytorium konspekt jest wzorem wypełnionym (zabawa „Wieża po kolei",
wersja B, 5-latki) — pola nadpisuje się własną treścią.

## Druk KC-3 — konspekty klikane z banku

W tabeli banku cele obszaru VII (wersja A) są klikalne — znacznik „▸ konspekt".
Kliknięcie celu wybranego poziomu otwiera konspekt w układzie wzoru
„Termometr uwagi": cel edukacyjny cytowany z banku dla klikniętego poziomu
(z automatycznym rozbiciem S/M/A/R/T z danych), cel terapeutyczny, pomoce,
metody, tabela czynności N/D, modyfikacje przy braku postępu, wskazówka.
Konspekt drukuje się osobno na A4 pionowo przyciskiem w oknie.

Konspekty obszaru VII · 3–4 lata: Latarnia uwagi (29) · Podaj misia (30) ·
Mostek do przedszkola (31) · Lusterko emocji (32) · Czarodziejskie słowo POMOC (33).

Konspekty obszaru I · 3–4 lata: Czarodziejski woreczek (1) · Małpka robi to,
co ja (2) · Klepsydra skarbów (3) · Kolorowe domki (4) · Pudełko z niespodzianką (5).

### Pokrycie konspektami — wersja A (3–4 lata)

| Obszar | Konspekty |
|---|---|
| I Uczenie się | Czarodziejski woreczek · Małpka robi to, co ja · Klepsydra skarbów · Kolorowe domki · Pudełko z niespodzianką |
| II Ogólne zadania | Zaproszenie od misia · Dwa kroki do końca · Pociąg dnia · Nasze trzy zasady · Wyspa spokoju |
| IV Poruszanie się | Ścieżka leśnych zwierząt · Schodki do chmurki · Piłka wędrowniczka · Wieża i korale · Muzyczne pociągi |
| VI Życie domowe | Sprzątanie z piosenką · Każda rzecz ma swój dom · Mali pomocnicy |
| VII Wzajemne kontakty | Latarnia uwagi · Podaj misia · Mostek do przedszkola · Lusterko emocji · Czarodziejskie słowo POMOC |
| VIII Główne obszary życia | Moje miejsce w grupie · Kącik lalek i garaż · Dywanik zajęć · Budowniczowie · Bawimy się razem |

Razem **42 konspekty pod 126 klikalnymi celami** — komplet dla wersji A (3–4 lata):
każde twierdzenie kwestionariusza ma własny konspekt zajęć.

## Wersja B (5 lat) — komplet konspektów

44 konspekty, wszystkie dziewięć obszarów:

| Obszar | Konspekty |
|---|---|
| I Uczenie się | Detektywi opowieści · Fabryka rytmów · Sklep pod piątką · Kwadrans badacza · Polowanie na litery |
| II Ogólne zadania | Instrukcja mistrza budowy · Most między zajęciami · Kolejka po skarb · Moje stanowisko pracy · Najpierw próbuję, potem proszę |
| III Porozumiewanie się | Radio Przedszkole · Kronika dnia · Rozmowa przy stoliku · Rymowana kuchnia · Teatr bez słów |
| IV Poruszanie się | Olimpiada czterech ruchów · Linoskoczkowie · Pracownia nożyczek · Szlaczki na ścianie · Laboratorium przelewania |
| V Dbanie o siebie | Detektyw czystych rąk · Wyścig z suwakiem · Restauracja pod dobrą łyżką · Strażnicy bezpieczeństwa · Barometr energii |
| VI Życie domowe | Zdjęcie przed i po · Dyżurni tygodnia · Umowa o zabawki · Pakowanie na wyprawę |
| VII Wzajemne kontakty | Zaproszenie do zabawy · Zespół z pomysłem · Słowa, które pomagają · Mapa uczuć · Trzy kroki zgody |
| VIII Główne obszary życia | Mój pomysł na zajęcia · Miasto z podziałem ról · Pracownia ulepszeń · Orkiestra przedszkolna · Polecenie dla całej grupy |
| IX Życie społeczne | Herb naszej grupy · Nasze przedstawienie · Wyprawa czterech pór roku · Widzowie i krytycy · To ja — imię i nazwisko |

Razem z wersją A: **86 konspektów pod 258 klikalnymi celami**.

## Monitoring podstawy programowej

Sekcja `#monitoring` zestawia wszystkie punkty PP, do których odwołują się twierdzenia KPOF:
punkt · obszar podstawy · wersje wiekowe · obszary ICF · czy istnieje konspekt.

**Stan prawny:** numeracja pochodzi z arkuszy KPOF opartych na podstawie programowej
z rozporządzenia MEN z 14 lutego 2017 r. Nowa podstawa — rozporządzenie Ministra Edukacji
z 11 marca 2026 r. (Dz. U. 2026 poz. 378), obowiązująca od 1 września 2026 r. — wprowadza
nowy podział obszarów. Przemapowanie wymaga aktualizacji kolumny `pp` w plikach `dane_*.py`;
monitoring, cele i konspekty przeliczą się automatycznie.

## Wersja C (6 lat) — komplet konspektów

44 konspekty podporządkowane gotowości szkolnej:

| Obszar | Konspekty |
|---|---|
| I Uczenie się | Warsztat historyjek · Sylabowa czytelnia · Litery w liniaturze · Kantorek liczb · Laboratorium hipotez |
| II Ogólne zadania | Plan w trzech krokach · Cicha godzina pracy · Klub dobrych przegranych · Wczoraj, dziś, jutro · Skrzynka strategii |
| III Porozumiewanie się | Wyraźnie i płynnie · Dźwiękowe puzzle · Bajkopisarze · Debata przedszkolna · English corner |
| IV Poruszanie się | Skrzyżowane ścieżki · Prosty kręgosłup przy stoliku · Mistrzowie ołówka · Szkoła zapinania · Ruch, który opowiada |
| V Dbanie o siebie | Gotowi w pięć minut · Sam nakładam, sam sprzątam · Zdrowie na talerzu · Bezpieczna droga · Moje granice |
| VI Życie domowe | Restauracja dyżurnych · Dyżury z rozliczeniem · Porządek w mojej przestrzeni · Ogrodnicy z kącika przyrody |
| VII Wzajemne kontakty | Rada grupy · Kodeks naszej grupy · Konsekwencje moich wyborów · Pogotowie pomocne · Przyjaźń i słowa, które ranią |
| VIII Główne obszary życia | Zespół projektowy · Skończone i pokazane · Turniej gier z regułami · Sklep z prawdziwą kasą · Mali badacze świata |
| IX Życie społeczne | Kręgi przynależności · Polska na mapie · Moje dane, moje bezpieczeństwo · Strażnicy planety · Kim będę, kim jestem |

## Stan całości

**130 konspektów pod 390 klikalnymi celami** — każde twierdzenie KPOF we wszystkich
trzech wersjach wiekowych ma własny scenariusz zajęć z wariantami dla trzech poziomów wsparcia.

| Wersja | Twierdzenia | Konspekty |
|---|---|---|
| A · 3–4 lata | 42 | 42 |
| B · 5 lat | 44 | 44 |
| C · 6 lat | 44 | 44 |

## Załączniki — pomoce dydaktyczne

Konspekt może mieć dołączone gotowe pomoce do wydruku. Pierwsza z nich:

`Zalaczniki_KC3_C1-01_Historyjki_6lat.pdf` — trzy historyjki obrazkowe
**„Jak rośnie kwiatek”** do konspektu C1-01 (Warsztat historyjek, 6 lat),
w gradacji odpowiadającej poziomom wsparcia:

| Załącznik | Poziom | Obrazki | Fabuła |
|---|---|---|---|
| Z1 | Poziom III | 3 | sadzę → podlewam → wyrósł kwiat |
| Z2 | Poziom II | 4 | nasionko → kiełek → podlewanie → kwitnienie |
| Z3 | Poziom I | 5 | z problemem: zapomniane podlewanie i naprawa sytuacji |

Rysunki są wektorowe (SVG generowane w `src/zalacznik_c1.py`), więc drukują się
ostro w każdej skali. Każda historyjka zajmuje jedną stronę A4; obrazki mają
numery, podpisy i przerywane ramki do wycięcia. W konspekcie C1-01 doszła
sekcja VII „Załączniki” z przyciskiem **Drukuj załączniki Z1–Z3 (A4)**.

## Pomoce dydaktyczne — ilustracje

Sceny historyjki obrazkowej „Jak rośnie kwiatek" (załączniki Z1–Z3 do konspektu
C1-01, wersja C · 6 lat) powstały w generatorze obrazów (model
`gemini-2.5-flash-image`) w jednym, spójnym stylu: ta sama bohaterka, ta sama
pastelowa paleta, białe tło wokół zaokrąglonej sceny.

* źródła 1344×768 px — `assets/hist_c1/hist_01..05.png`
* kadry do druku 640 px, paleta 96 kolorów — `assets/hist_c1/kadr_01..05.png`

Kadry są osadzane w HTML jako data-URI w klasach CSS `.sc1`–`.sc5`
(`src/zalacznik_c1.py`), dzięki czemu każdy obrazek trafia do pliku dokładnie
raz, mimo że powtarza się na trzech kartach.

Sekwencje: Poziom III — sceny 1, 2, 5 · Poziom II — 1, 2, 4, 5 ·
Poziom I — 1–5 (pełny łuk: problem → działanie → rozwiązanie).

Ponowne wygenerowanie PDF-u z załącznikami: `node src/generuj_zalaczniki_pdf.mjs`
(wymaga zainstalowanego pakietu `playwright`).

## Narracja (dubbing PL)

Historyjka „Jak rośnie kwiatek" ma pełną narrację po polsku, nagraną
sklonowanym głosem nauczycielki (ElevenLabs, głos `Ewa-głos_do skils`,
model `eleven_v3` — przyjmuje wskazówki aktorskie w nawiasach kwadratowych,
dzięki czemu ton jest bajkowy, a nie lektorski).

### Wzorzec rejestru — obowiązuje dla wszystkich nagrań

Ten sam zestaw wskazówek w każdej ścieżce, wypracowany i zaakceptowany
na wprowadzeniu do C1-01:

* otwarcie — `[warmly, smiling, telling a story to a small child]`
* rozwinięcie — `[gently]`
* domknięcie — `[with a smile]`
* scena smutna zamienia dwie ostatnie na `[gently, a little sad]` i `[softly]`

Tekst mówiony ma być czystą prozą: pełne zdania, bez wielokropków, bez
sylabizowania („po-wo-lut-ku"), bez wtrąceń typu „o tak". Efekt ciepła daje
wskazówka aktorska, nie interpunkcja — nagrania robione „na wielokropkach"
brzmią sztucznie. Przy nowych konspektach trzymamy ten sam wzorzec.

Siedem ścieżek w `assets/audio_c1/`: wprowadzenie, pięć scen, zakończenie
z pytaniami otwartymi. Teksty i czasy trwania trzyma słownik `NARRACJA`
w `src/zalacznik_c1.py` — to jedyne miejsce do edycji, jeśli nagrania
zostaną wymienione.

W HTML nagrania są osadzone jako `<audio>` z data-URI, po jednym elemencie
na ścieżkę (wspólne dla trzech kart). Każdy kafelek ma przycisk „Posłuchaj",
a pasek nad siatką odtwarza sceny danej karty po kolei — z wprowadzeniem
na początku i pytaniami na końcu — podświetlając obrazek aktualnie czytany.
Wydruk i klawisz Esc wyciszają narrację; w druku przyciski są ukryte.
