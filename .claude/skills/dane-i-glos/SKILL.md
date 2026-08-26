---
name: dane-i-glos
description: Zamienia dane (CSV, XLSX, JSON, tabela w czacie) w gotowe nagranie po polsku — najpierw rzetelna analiza liczb, potem scenariusz narracji, na końcu głos z ElevenLabs (MP3 + napisy SRT) albo film z Twoim awatarem i Twoim głosem z HeyGen (MP4). Użyj ZAWSZE, gdy użytkowniczka prosi o: „udźwiękowij te dane", „przeczytaj mi ten raport", „zrób lektora do tych wyników", „narracja z tabeli", „audio podsumowanie", „wersja do słuchania", „głos do prezentacji", „scenariusz lektorski z Excela", a także „film z awatarem", „awatar opowiada wyniki", „nagraj to moim głosem", „wideo z danych", „mówiąca głowa do raportu". Wyzwalaj przy hasłach: ElevenLabs, HeyGen, awatar, TTS, lektor, narracja, voice-over, mp3 z danych, napisy SRT, klon głosu, mój głos. Wyzwalaj też, gdy użytkowniczka wgrywa dane i mówi „z głosem", „na głos", „z moją twarzą", albo prosi o dźwięk lub film do materiału EduPlaner. NIE używaj do samej analizy danych bez audio ani do czytania tekstu, który nie pochodzi z danych.
---

# Dane i głos

Skill prowadzi jedną drogę: **dane → liczby → scenariusz → głos → (opcjonalnie) twarz**.
Każdy etap opiera się na poprzednim, więc narracja nigdy nie zawiera liczby, której nie ma
w pliku źródłowym.

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
| „Napisz scenariusz lektorski, resztę zrobię sama" | 1 → 2 → 3 |
| „Przeczytaj ten gotowy tekst" | 4a → 5 (pomiń analizę) |
| „Dodaj napisy do nagrania" | 4a z `--srt` |

Etap 0 robi się **raz**. Przy kolejnych materiałach `ELEVENLABS_VOICE_ID` już jest
ustawione i etap przeskakujesz bez pytania.

## Etap 0 — Głos użytkowniczki (jednorazowo)

Sprawdź, czy jest już sklonowany głos:

```bash
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_klon_glosu.py --moje-glosy
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

- `--voice-id <id>` — domyślnie bierze `ELEVENLABS_VOICE_ID`, czyli jej klon z etapu 0
- `--glosy` — wypisz wszystkie głosy z konta i ich `voice_id`
- `--model eleven_multilingual_v2` — domyślny, najlepszy dla polszczyzny
- `--srt napisy.srt` — napisy z rzeczywistymi znacznikami czasu z ElevenLabs
- `--stability 0.6 --similarity 0.75 --speed 1.0` — barwa i tempo
- `--suchy-bieg` — policz znaki bez wywołania API

Skrypt sam dzieli długi tekst na fragmenty poniżej limitu znaków, zachowuje ciągłość brzmienia
(`previous_text`/`next_text`) i skleja wynik w jeden plik MP3.

**Uwaga o polskim brzmieniu**: głosy premade mówią po polsku z obcym akcentem. Naturalną
polszczyznę daje wyłącznie klon z etapu 0 — dlatego to on jest domyślny.

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

## Etap 5 — Oddaj komplet

Dostarcz użytkowniczce wszystko, co powstało, i wymień to jawnie:

1. **plik audio** (`.mp3`) lub **film** (`.mp4`) — wyślij go, nie tylko wspomnij ścieżkę,
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
- `assets/przyklad_dane.csv` — dane testowe do sprawdzenia całej ścieżki
