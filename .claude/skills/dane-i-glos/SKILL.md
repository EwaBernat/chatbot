---
name: dane-i-glos
description: Zamienia dane (CSV, XLSX, JSON, tabela w czacie) w gotowe nagranie po polsku — rzetelna analiza liczb, scenariusz narracji, a na końcu głos użytkowniczki z ElevenLabs (MP3 + napisy SRT), film z animowanymi wykresami (Remotion) albo film z jej awatarem HeyGen. NIGDY nie tworzy nagrania cudzym głosem — bez jej zapamiętanego głosu oddaje sam scenariusz i zatrzymuje się. Użyj ZAWSZE, gdy prosi o: „udźwiękowij te dane", „przeczytaj mi ten raport", „zrób lektora do tych wyników", „narracja z tabeli", „audio podsumowanie", „wersja do słuchania", „głos do prezentacji", „film z danych", „wideo z wykresami", „animacja danych", „film z awatarem", „nagraj to moim głosem", a także gdy prosi o sklonowanie albo skonfigurowanie swojego głosu. Wyzwalaj przy hasłach: ElevenLabs, HeyGen, Remotion, awatar, TTS, lektor, narracja, voice-over, napisy SRT, klon głosu, mój głos, wykres w filmie. NIE używaj do samej analizy danych bez audio.
---

# Dane i głos

Skill prowadzi jedną drogę: **dane → liczby → scenariusz → głos → obraz**, gdzie obrazem
jest animowany wykres (Remotion), twarz awatara (HeyGen) albo jedno i drugie.
Każdy etap opiera się na poprzednim, więc narracja nigdy nie zawiera liczby, której nie ma
w pliku źródłowym.

## Zasada nadrzędna: tylko jej głos

**Nigdy nie twórz nagrania ani filmu cudzym głosem.** Materiał firmowany nazwiskiem
użytkowniczki ma brzmieć nią — głos zastępczy podważa wiarygodność materiału i nie jest
tym, o co prosiła.

Gdy skill nie ma zapamiętanego jej głosu:

1. **Zrób wszystko, co nie wymaga głosu** — profil danych, wybór historii, scenariusz
   narracji. To realna wartość i nie czeka na nic.
2. **Zatrzymaj się przed generowaniem dźwięku.** Oddaj scenariusz i powiedz wprost,
   czego brakuje.
3. **Nie proponuj zastępstwa** „na razie", „do podglądu" ani „żeby zobaczyć, jak działa".
   Ona odrzuciła tę drogę.

`elevenlabs_tts.py` sam tego pilnuje: bez zapamiętanego głosu **odmawia** i kończy się
kodem 4. Nie ma głosu domyślnego. Obejście `--obcy-glos` istnieje wyłącznie na jej
wyraźne, świeże polecenie — nigdy z własnej inicjatywy.

To samo dotyczy filmu: skoro dźwięk nie powstaje, nie renderuj też wideo.
Film z cudzą narracją to ten sam problem, tylko większy.

## Ścieżka domyślna

**Klon głosu w ElevenLabs → awatar HeyGen.** Sklonowany głos jest wspólnym punktem obu
wyjść: to samo MP3 służy za nagranie audio i za ścieżkę dźwiękową awatara. Dlatego przy
każdym materiale z głosem użytkowniczki idź tą drogą, chyba że poprosi inaczej:

```
dane → profil liczb → scenariusz → ElevenLabs (jej voice_id) → MP3 + SRT → HeyGen --audio → MP4
```

Wyjątek: gdy `ELEVENLABS_VOICE_ID` nie jest ustawione i użytkowniczka nie chce teraz
klonować głosu — wtedy film robi HeyGen własnym głosem z jej konta (etap 4b, wariant A).

## Kiedy co uruchomić

| Prośba | Etapy |
|---|---|
| „Nagraj to moim głosem, z moją twarzą" | 0 → 1 → 2 → 3 → 4a → 4b (`--audio`) → 5 **← domyślna** |
| „Zrób audio z tych danych" | 0 → 1 → 2 → 3 → 4a → 5 |
| „Zrób film z awatarem o tych danych" | 0 → 1 → 2 → 3 → 4a → 4b (`--audio`) → 5 |
| „Zrób film, ale bez klonowania głosu" | 1 → 2 → 3 → 4b (wariant A) → 5 |
| „Zrób film z wykresami, bez awatara" | 1 → 2 → 3 → 4a → 4c → 5 |
| „Film z wykresami i z awatarem w rogu" | 1 → 2 → 3 → 4a → 4c → 4b → 5 |
| „Napisz scenariusz lektorski, resztę zrobię sama" | 1 → 2 → 3 |
| „Przeczytaj ten gotowy tekst" | 4a → 5 (pomiń analizę) |
| „Dodaj napisy do nagrania" | 4a z `--srt` |

Etap 0 robi się **raz**. Przy kolejnych materiałach `ELEVENLABS_VOICE_ID` już jest
ustawione i etap przeskakujesz bez pytania.

## Etap 0 — Głos użytkowniczki (jednorazowo)

Sprawdź, czy skill ma już zapamiętany głos:

```bash
python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py --pokaz
```

Jeśli pamięta — nic więcej nie rób, wszystkie skrypty same go użyją. Jeśli nie,
jedno polecenie załatwia całość (przyjmuje też film, sam wyciągnie z niego dźwięk):

```bash
python3 .../skonfiguruj_glos.py nagranie.mp4 --nazwa "Ewa - narracja PL"
```

**Gdy głos jest już sklonowany na koncie ElevenLabs** — a tak bywa najczęściej, bo
użytkowniczka klonuje go w aplikacji — nie klonuj go drugi raz. Wystarczy zapamiętać
istniejący identyfikator; nic nie zostaje wysłane i nie ubywa miejsc na głosy:

```bash
python3 .../skonfiguruj_glos.py --zapamietaj <voice_id> --nazwa "Ewa - narracja PL"
```

`voice_id` znajdziesz przez `elevenlabs_tts.py --glosy`, a gdy skrypty nie mają dostępu
do sieci — przez złącze MCP: `creative_list_voices`. Jej głosy to te z kategorii `cloned`
i języka `pl`; `premade` i `professional` to głosy cudze.

Skrypt wyciąga dźwięk, sprawdza próbki, klonuje głos i **zapisuje `voice_id`
w pamięci skilla** (`~/.config/dane-i-glos/konfiguracja.json`) — poza repozytorium,
bo do repozytorium trafiać nie powinien. Kluczy API ten plik nie przyjmuje.

`--tylko-sprawdz` sprawdza nagrania bez wysyłania czegokolwiek. `--zapomnij` czyści
pamięć, nie ruszając ani nagrań, ani głosu na koncie ElevenLabs.

Ręczna droga, gdy potrzebujesz kontroli nad każdym krokiem:

```bash
python3 .../elevenlabs_klon_glosu.py --moje-glosy
```

- **Jest** → zapamiętaj `voice_id`, przejdź dalej. Gotowe głosy premade (Bella, Alice,
  Matilda) to **nie** jest jej głos — mówią po polsku z obcym akcentem.
- **Nie ma** → zaproponuj sklonowanie i wyjaśnij, co to daje: naturalną polszczyznę
  w audio **oraz** awatara mówiącego jej głosem zamiast cudzego. Potrzeba około
  3 minut czystego nagrania po polsku, w 3–5 plikach.

```bash
python3 .../elevenlabs_klon_glosu.py --sprawdz-nagrania probki/*.wav   # nic nie wysyła
python3 .../elevenlabs_klon_glosu.py "Ewa - narracja PL" probki/*.wav
export ELEVENLABS_VOICE_ID="<voice_id>"
```

Zasady nagrywania, wymagania jakościowe i diagnostyka złego brzmienia:
`references/klon_glosu.md`. Klonuj wyłącznie jej własny głos.

Jeśli nie chce teraz klonować — nie blokuj pracy. Zrób materiał głosem gotowym albo
głosem z HeyGen i powiedz, czym to się różni.

## Zanim cokolwiek uruchomisz — sprawdź, czy sieć przepuszcza

W środowiskach zdalnych (Claude Code na stronie, kontenery CI) polityka sieciowa często
blokuje wychodzące połączenia do usług zewnętrznych. Skrypty zwracają wtedy `403`, co
łatwo pomylić ze złym kluczem API. Sprawdź to jednym poleceniem:

```bash
curl -sS -o /dev/null -w "%{http_code}\n" --max-time 10 https://api.elevenlabs.io/
curl -sS -o /dev/null -w "%{http_code}\n" --max-time 10 https://api.heygen.com/
```

`000` z komunikatem `CONNECT tunnel failed, response 403` oznacza **blokadę sieciową**,
nie problem z kluczem. Diagnoza wprost: `curl -sS "$HTTPS_PROXY/__agentproxy/status"`
pokazuje ostatnie odrzucenia z nazwami hostów.

Co wtedy działa, a co nie:

| Droga | Przy zablokowanej sieci |
|---|---|
| Złącza MCP w Claude (np. ElevenLabs) | **działają** — wywołania idą spoza kontenera |
| Skrypty z tego skilla | **nie działają** — łączą się z kontenera |
| Wszystko na własnym komputerze | **działa** — brak takiej blokady |

Nie powtarzaj wywołań po odmowie polityki — zgłoś ją użytkowniczce i zaproponuj
uruchomienie skryptów lokalnie albo zmianę polityki sieciowej środowiska.

## Etap 1 — Wczytaj dane i policz, zanim cokolwiek napiszesz

Nigdy nie opisuj danych z pamięci ani „na oko" z podglądu pliku. Uruchom profiler:

```bash
python3 .claude/skills/dane-i-glos/scripts/dane_do_narracji.py <plik> --profil
```

Skrypt przyjmuje `.csv`, `.tsv`, `.xlsx`, `.json`, `.jsonl` i zwraca w Markdown:
liczbę wierszy i kolumn, typ każdej kolumny, braki danych, sumy/średnie/min/maks dla liczb,
najczęstsze wartości dla kategorii oraz zakres dat. To jest **jedyne źródło liczb** dla narracji.

Przydatne przełączniki:

- `--kolumny nazwa,druga` — zawęź profil do wybranych kolumn
- `--grupuj klasa --agreguj wynik` — przekrój (średnia i liczebność w grupach)
- `--arkusz "Nazwa"` — konkretny arkusz z XLSX (domyślnie pierwszy)
- `--json` — profil jako JSON, gdy potrzebujesz go dalej przetworzyć

Jeśli plik jest pusty, ma same nagłówki albo kolumna liczbowa okazuje się tekstem —
powiedz to wprost użytkowniczce i zapytaj, zanim zbudujesz narrację na wątpliwych danych.

## Etap 2 — Wybierz historię, nie wszystkie liczby

Nagranie to nie arkusz odczytany na głos. Z profilu wybierz **3–5 faktów**, które niosą sens:
największa zmiana, wartość odstająca, wynik zbiorczy, wyraźny trend, coś zaskakującego.
Resztę pomiń — zostaje w pliku, do którego słuchacz zawsze może zajrzeć.

Zapytaj o odbiorcę, jeśli nie wynika z rozmowy: **dyrekcja, rodzice, zespół, sama autorka**?
Ten wybór zmienia ton, długość i to, które liczby są ważne.

## Etap 3 — Napisz scenariusz lektorski

Pełne zasady stylu: `references/narracja.md` — przeczytaj przed pisaniem pierwszego zdania.
Skrót najważniejszych reguł:

- **Tempo**: ok. 150 słów na minutę po polsku. 60 s ≈ 150 słów, 90 s ≈ 225 słów.
- **Liczby zapisuj słowami tak, jak się je czyta**: `87,5%` → „osiemdziesiąt siedem i pół procent",
  `2026` → „dwa tysiące dwudziesty szósty". Silnik TTS czyta cyfry po polsku niepewnie.
- **Jedno zdanie = jedna myśl.** Maksymalnie 20 słów. Bez wtrąceń w nawiasach.
- **Bez elementów wizualnych**: żadnego „jak widać w tabeli", „poniższy wykres".
- **Struktura**: haczyk (1 zdanie) → kontekst (2–3) → kluczowe liczby (3–5) → wniosek (1–2).

Zapisz scenariusz do pliku `.txt` (np. `narracja.txt`) i **pokaż go użytkowniczce do akceptacji
przed generowaniem**. Poprawka w tekście kosztuje sekundę; przegenerowanie nagrania zużywa
znaki z limitu ElevenLabs, a filmu — kredyty HeyGen.

Pauzy zaznaczaj nową linią lub `<break time="0.7s" />` (modele `eleven_v3`
i `eleven_multilingual_v2`).

## Etap 4a — Głos (ElevenLabs)

**Najpierw sprawdź, czy w sesji są narzędzia `mcp__ElevenLabs__creative_*`.** Jeśli tak:
`creative_list_voices` po `voice_id`, potem `creative_generate_speech`, a wynik odbierasz
przez `creative_get_flow_run_status`. Jeśli narzędzi nie ma, użyj skryptu REST:

```bash
export ELEVENLABS_API_KEY="..."          # elevenlabs.io → profil → API Keys
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_tts.py narracja.txt -o raport.mp3
```

Najczęstsze przełączniki:

- `--voice-id <id>` — zwykle zbędne: skrypt bierze głos z pamięci skilla.
  Kolejność: `--voice-id` > `ELEVENLABS_VOICE_ID` > pamięć skilla > głos zapasowy.
  Gdy pamięć jest pusta, skrypt **ostrzega**, że mówi cudzym głosem
- `--glosy` — wypisz wszystkie głosy z konta i ich `voice_id`
- `--model eleven_v3` — domyślny dla narracji szkoleniowej; skrypt bierze go z pamięci
  skilla, tak samo jak głos. `eleven_multilingual_v2` na klonie brzmi płasko —
  szczegóły i znaczniki stylu: `references/elevenlabs.md`
- `--srt napisy.srt` — napisy z rzeczywistymi znacznikami czasu z ElevenLabs
- `--stability 0.6 --similarity 0.75 --speed 1.0` — barwa i tempo
- `--suchy-bieg` — policz znaki bez wywołania API

Skrypt sam dzieli długi tekst na fragmenty poniżej limitu znaków, zachowuje ciągłość brzmienia
(`previous_text`/`next_text`) i skleja wynik w jeden plik MP3.

**Uwaga o polskim brzmieniu**: głosy premade mówią po polsku z obcym akcentem. Naturalną
polszczyznę daje wyłącznie klon z etapu 0 — dlatego to on jest domyślny.

**Gdy usłyszysz „głos robota"** — nie zmieniaj od razu głosu ani nie klonuj go ponownie.
Najpierw sprawdź model: ten sam klon na `eleven_multilingual_v2` czyta płasko, a na
`eleven_v3` ze znacznikiem stylu w nawiasie kwadratowym na początku akapitu brzmi
naturalnie. Dopiero gdy to nie pomoże, wróć do jakości próbek (`references/klon_glosu.md`).

Szczegóły API, modele, limity i kody błędów: `references/elevenlabs.md`.

## Etap 4b — Twarz i Twój głos (HeyGen)

Złącze HyperFrames **nie sięga po Twoje awatary** — robi filmy z HTML. Do awatara służy
API HeyGen i skrypt:

```bash
export HEYGEN_API_KEY="..."                             # app.heygen.com → Settings → API
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --awatary
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --glosy --jezyk polish
```

Dopiero mając `avatar_id` generuj film. Dwie drogi — **domyślna jest B**:

```bash
# B (domyślna). Awatar mówi jej klonem głosu: MP3 z etapu 4a steruje ustami
python3 .../heygen_awatar.py --audio raport.mp3 --avatar-id <id> --czekaj -o film.mp4

# A (zapasowa). HeyGen sam czyta scenariusz głosem z jej konta HeyGen
python3 .../heygen_awatar.py narracja.txt --avatar-id <id> --voice-id <id> --czekaj -o film.mp4
```

Wariant A wybieraj tylko wtedy, gdy nie ma klonu w ElevenLabs, a w HeyGen jest jej głos —
albo gdy sama o to poprosi. W wariancie B napisy bierz z `--srt` z etapu 4a: są dokładniejsze
niż wypalane `--napisy` i da się je poprawić.

Przydatne: `--tlo "#2D1B69"` (fiolet PCTP), `--styl circle`, `--szerokosc 1080 --wysokosc 1920`
(pion pod Reels), `--napisy` (wypala napisy w obrazie), `--suchy-bieg` (podgląd zapytania bez
zużycia kredytów), `--status <video_id>` (sprawdzenie renderu później).

Render trwa zwykle 2–6 minut na minutę materiału. Bez `--czekaj` dostajesz sam `video_id`.
Szczegóły, kredyty i kody błędów: `references/heygen.md`.

Klucza API **nigdy** nie wpisuj do pliku w repozytorium ani do treści rozmowy — tylko zmienna
środowiskowa.

## Etap 4c — Film z danych (Remotion)

Gdy materiał ma pokazywać **liczby**, a nie twarz — animowany wykres niesie więcej niż
awatar. Remotion sam nie syntezuje mowy: dźwięk bierze z MP3 z etapu 4a, a napisy
z pliku SRT. Dlatego etap 4a musi być zrobiony pierwszy.

```bash
python3 .../dane_do_narracji.py dane.csv --grupuj klasa --agreguj frekwencja_proc --json > profil.json
python3 .../elevenlabs_tts.py narracja.txt -o narracja.mp3 --srt napisy.srt
python3 .../przygotuj_remotion.py ~/moj-film --profil profil.json --narracja narracja.txt \
        --audio narracja.mp3 --napisy napisy.srt --tytul "Frekwencja — I półrocze"
cd ~/moj-film && npm install && npx remotion render RaportWideo out/film.mp4
```

Skrypt buduje sceny z akapitów narracji i **dosuwa granice scen do końców napisów**,
więc obraz zmienia się między zdaniami, nie w ich środku. Długość filmu bierze się
z długości MP3 — poprawiona narracja sama zmienia długość filmu.

Zanim wyrenderujesz, **otwórz `public/film.json` i sprawdź treść scen**: tytuł, główną
liczbę i podpisy. Skrypt wypełnia je zachowawczo, bo nie zna kontekstu.

Typy scen (`--typy`, po jednym na akapit): `tytul`, `liczba`, `wykres`, `wniosek`.
Wykres bierze słupki z sekcji `grupy` profilu, więc profiler musi być uruchomiony
z `--grupuj` i `--agreguj`.

**Kolorów nie zmieniaj bez walidacji.** Paleta w `assets/remotion/src/marka.ts` przeszła
sześć testów dostępności; ciemny fiolet marki jest tam tekstem, nie wypełnieniem słupka,
bo jako wypełnienie nie przechodzi. Pomarańcz jest zarezerwowany dla wartości wymagającej
uwagi i zawsze towarzyszy mu podpis. Szczegóły: `assets/remotion/README.md`.

W kontenerze bez przeglądarki dodaj `--browser-executable` wskazujący `headless_shell` —
Remotion używa starego trybu headless, którego nowe Chrome nie ma.

## Etap 5 — Oddaj komplet

Dostarcz użytkowniczce wszystko, co powstało, i wymień to jawnie:

1. **plik audio** (`.mp3`) lub **film** (`.mp4`) — wyślij go, nie tylko wspomnij ścieżkę.
   Jeśli powstał bez jej głosu — **nie oddawaj go wcale**, patrz zasada nadrzędna,
2. **tekst narracji** (`.txt`) — żeby mogła poprawić i przegenerować,
3. **napisy** (`.srt`) — jeśli materiał pójdzie pod wideo.

Podaj czas trwania i to, co się zużyło: liczbę znaków ElevenLabs albo kredyty HeyGen.
Jeśli któryś etap się nie udał — powiedz który i dlaczego, zamiast oddawać niekompletny
zestaw po cichu.

## Materiały

- `references/klon_glosu.md` — jak nagrać próbki i sklonować głos (etap 0)
- `references/narracja.md` — zasady pisania pod polskiego lektora, wzorce zdań, przykłady
- `references/elevenlabs.md` — API, modele, limity, głosy, rozwiązywanie błędów
- `references/heygen.md` — awatary, klon głosu, kredyty, dwie drogi głosu, kody błędów
- `assets/remotion/` — szablon filmu (React + Remotion), z opisem palety i renderu
- `assets/przyklad_dane.csv` — dane testowe do sprawdzenia całej ścieżki
