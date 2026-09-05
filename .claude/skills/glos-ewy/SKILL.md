---
name: glos-ewy
description: >-
  Nagrywa narrację, wstawki lektorskie, wersje audio broszur i odcinki podkastu głosem
  Mirosławy Ewy Jurczyszyn — jej sklonowanym głosem z ElevenLabs, w intonacji osoby
  prowadzącej szkolenie. Trzyma zapamiętany voice_id, wskazówki aktorskie, zasady zapisu
  liczb pod polskiego lektora i wyrównanie głośności. Użyj ZAWSZE, gdy pada „przywołaj
  agenta głosu Ewy", „agent głosu", „dodaj mój głos", „nagraj to moim głosem", „lektor",
  „narracja", „voice-over", „udźwiękowij", „dogranie do filmu", „wstawka do modułu",
  „audio do broszury", „podkast", „odcinek", „wersja mówiona" — a także gdy powstaje
  materiał EduPlaner albo PCTP mający mieć ścieżkę dźwiękową: szkolenie, moduł filmowy,
  broszura, poradnik, ulotka, podkast. Bez dostępu do jej głosu oddaje sam tekst narracji
  i zatrzymuje się — NIGDY nie nagrywa cudzym głosem. NIE używaj do filmu z awatarem
  HeyGen: tam ustawienia trzyma skill film-glos.
---

# Głos Ewy

Ten skill istnieje po to, żeby każde nagranie firmowane nazwiskiem Mirosławy Ewy
Jurczyszyn brzmiało nią i pasowało do materiału, do którego trafia. Trzyma trzy rzeczy,
które za każdym razem trzeba by odtwarzać od zera: **który to głos**, **jak pisać, żeby
zabrzmiał jak na szkoleniu**, i **jak dopasować go do materiału, do którego trafia** —
szkolenia, broszury albo podkastu.

## Zasada nadrzędna: tylko jej głos

Materiał firmowany jej nazwiskiem ma brzmieć nią. Głos zastępczy podważa wiarygodność
materiału i nie jest tym, o co prosiła — nawet „na próbę" i „żeby zobaczyć, jak działa".

Jeżeli nie da się sięgnąć po jej głos: zrób wszystko, co nie wymaga dźwięku (tekst
narracji, podział na fragmenty, punkty cięcia), oddaj to i powiedz wprost, czego zabrakło.
To pełnoprawny wynik. Nie proponuj zastępstwa.

## Zapamiętany głos

| | |
|---|---|
| **voice_id** | `jq4ZUryuBeDqmtkKtBZ4` |
| **nazwa na koncie** | „Ewa-głos_do skils " |
| **opis autorki** | „intonacja pasuje do prowadzenia szkoleń i wykładów" |
| **język** | polski, klon (`category: cloned`) |

Zapasowe klony na tym samym koncie: `D0Yz6dyyxHOodq3Zqi45` („Ewa1"),
`MxdHRlURUZPVY5h2NiXH` („Ewa2"). Domyślnie bierz pierwszy — został nagrany właśnie
pod szkolenia.

Gdyby `voice_id` przestał działać, znajdź go po nazwie: `creative_list_voices` z frazą
„Ewa". Nie zgaduj identyfikatora i nie bierz głosu gotowego (premade) — te mówią po polsku
z obcym akcentem.

## Którędy iść po dźwięk

W kontenerze Claude Code na stronie sieć wychodząca jest zablokowana, więc **skrypty REST
nie zadziałają** (`api.elevenlabs.io` odpowiada 403 z pośrednika). Działa natomiast
złącze — wywołania idą spoza kontenera:

| Droga | Stan |
|---|---|
| `mcp__ElevenLabs__creative_*` | **działa** — tędy generuj |
| `mcp__elevenlabs__*` (text_to_speech, voice_clone) | zwraca 403 |
| skrypty z `dane-i-glos/scripts/` | nie działają z kontenera, działają na komputerze autorki |
| pobranie gotowego MP3 z `storage.googleapis.com` | **działa** — zwykłym `curl` |

Procedura przez złącze:

```
creative_generate_speech(
   voice_id = "jq4ZUryuBeDqmtkKtBZ4",
   model_id = "eleven_v3",          # patrz niżej
   generations_count = 1,           # domyślne 4 to czterokrotny koszt
   prompt = <tekst TTS>)
→ creative_get_flow_run_status(flow_id, session_ids)  aż all_completed
→ curl -o <id>.mp3 "<media[].url>"
```

Przy dłuższej serii warto raz puścić `estimate_only: true` na najdłuższym fragmencie
i podać autorce koszt, zanim ruszysz. Orientacyjnie: minuta narracji to około 900–1000
kredytów, czyli mniej więcej 15 centów.

Wszystkie fragmenty jednego materiału trzymaj na **jednym przepływie** — przekazuj ten sam
`flow_id`. Autorka ma wtedy komplet w jednym miejscu na swoim płótnie.

## Który model

**`eleven_v3` — domyślnie do materiałów szkoleniowych.** Przyjmuje wskazówki aktorskie
w nawiasach kwadratowych i sam różnicuje tempo: przyspiesza tam, gdzie treść jest znana,
zwalnia przy numerze pozycji Dziennika Ustaw. To właśnie daje wrażenie, że ktoś mówi,
a nie czyta.

**`eleven_multilingual_v2` — gdy zależy na przewidywalności.** Czyta równo i bez
niespodzianek. Dobre do krótkich, czysto informacyjnych wstawek albo wtedy, gdy nagranie
musi wejść w z góry zadany czas.

Wskazówki aktorskie działają tylko w `eleven_v3`. W `multilingual_v2` zostaną przeczytane
na głos — a tego nikt nie chce usłyszeć.

## Dwie wersje tekstu, nigdy jedna

To jest najczęstsza pułapka. Tekst do TTS i tekst na pasek napisów to **dwa różne pola**:

- **`narracja`** — czysta, bez znaczników. Idzie na napisy, do transkrypcji, do skryptu
  dla nauczycieli, do druku.
- **`narracja_tts`** — ta sama treść plus wskazówki aktorskie, myślniki i wielokropki.
  Idzie wyłącznie do ElevenLabs.

Słowa muszą być identyczne w obu wersjach — inaczej napis przestanie się zgadzać z tym,
co słychać. Różnić je mają tylko znaczniki i interpunkcja pauzowa.

## Jak pisać pod jej głos

**Liczby zapisuj słowami, tak jak się je czyta.** To nie jest kosmetyka — silnik czyta
cyfry po polsku niepewnie, a numer publikatora przeczytany z cyfr brzmi jak dyktando:

| Nie tak | Tak |
|---|---|
| Dz.U. 2023 poz. 1120 | Dziennik Ustaw pozycja tysiąc sto dwadzieścia |
| § 7 ust. 3 | paragraf siódmy ustęp trzeci |
| 14.04.2026 | czternastego kwietnia dwa tysiące dwudziestego szóstego roku |
| t.j. Dz.U. 2020 poz. 1309 | tekst jednolity, Dziennik Ustaw pozycja tysiąc trzysta dziewięć |

**Tempo odniesienia: około 107 słów na minutę.** Zmierzone na jej istniejących modułach
(5753 słowa na 53 minuty 57 sekund, odchylenie między modułami 102–113). Przydaje się,
gdy trzeba oszacować długość nagrania przed wygenerowaniem — mnóż liczbę słów przez
0,56 sekundy i dodaj pół sekundy oddechu.

**Jedno zdanie to jedna myśl.** Akapit to jeden oddech — w `eleven_v3` pusta linia
naprawdę robi pauzę.

**Myślnik i wielokropek to narzędzia, nie ozdoby.** Myślnik przed puentą zdania
(„Bez tego kompletu — leku nie podajemy"), wielokropek przed numerem albo przy
wyliczaniu („pozycja... tysiąc sto dwadzieścia").

## Słownik wskazówek aktorskich

Sprawdzone na jej materiale, po jednej na akapit — więcej brzmi teatralnie:

| Znacznik | Kiedy | Przykład użycia |
|---|---|---|
| `[warmly]` | wejście w temat, zwrot do sali | „[warmly] Jedno uzupełnienie do tego rozporządzenia." |
| `[thoughtfully]` | tłumaczenie, dlaczego coś jest ważne | „[thoughtfully] Powiedzmy też wyraźnie, co to rozporządzenie zrobiło…" |
| `[emphatically]` | rzecz, której nie wolno przeoczyć | „[emphatically] Ten publikator przestał być aktualny." |
| `[deliberately]` | wyliczanie, dyktowanie kroków | „[deliberately] Chodzi o trzy dokumenty." |
| `[reassuring]` | zdjęcie niepokoju z sali | „[reassuring] W naszym załączniku nie zmienia się nic." |

Dobra kompozycja dłuższej wstawki: ciepłe wejście → spokojne wyjaśnienie → mocny akcent
na sedno → ciepłe domknięcie. Tak mówi ktoś, kto stoi przed radą pedagogiczną, a nie
ktoś, kto czyta rozporządzenie.

## Trzy rodzaje materiału

Głos jest jeden, ale sposób mówienia dobiera się do formy. Ustal rodzaj, zanim napiszesz
pierwsze zdanie — przepisany później tekst i tak trzeba nagrać od nowa.

| | szkolenie / film | broszura | podkast |
|---|---|---|---|
| długość jednego nagrania | 20–90 s (wstawka), scena do 2 min | 2–8 min, całość działu | 8–25 min, odcinek |
| tempo | ~107 słów/min | ~100 słów/min (wolniej, słuchacz nie ma obrazu) | ~112 słów/min (swobodniej) |
| model | `eleven_v3` | `eleven_v3` | `eleven_v3` |
| wskazówki aktorskie | jedna na akapit | jedna na sekcję, oszczędnie | dwie–trzy na blok, żywiej |
| dzielenie na pliki | jeden plik na wstawkę | jeden plik na rozdział broszury | jeden plik na blok, sklejane na końcu |
| cel głośności | zmierzony z filmu docelowego | `--cel -20.7` | `--cel -16.0` (norma podkastowa) |

### Szkolenia i filmy

Wstawka wchodzi w środek gotowego modułu, więc liczy się przede wszystkim **szew**:
zaczyna się i kończy pełnym zdaniem, nie wchodzi w połowie myśli i ma tę samą głośność,
co materiał wokół. Kompozycja dłuższej wstawki: ciepłe wejście → spokojne wyjaśnienie →
mocny akcent na sedno → ciepłe domknięcie.

Nie zapowiadaj samej siebie („teraz powiem o…") — w filmie robi to plansza. Cała procedura
wklejenia w gotowy film: [`references/montaz-wstawek.md`](./references/montaz-wstawek.md).

Film z awatarem to **inna ścieżka** — tam mówi awatar HeyGen ustawieniami ze skilla
skill `film-glos` (repo EduPlaner 2026). Ten skill obsługuje dźwięk samodzielny: wstawki
lektorskie, narrację do plansz, materiał bez prezenterki w kadrze.

### Broszury

Wersja mówiona broszury powstaje **z gotowej, zatwierdzonej treści** — tej samej, którą
Ewa przyjęła w PDF-ie. Obowiązuje ta sama twarda zasada, co w skillu
skill `broszury` (repo EduPlaner 2026): **treść przepisujesz 1:1**, bez skracania i bez
„poprawiania stylu". Wolno Ci zrobić tylko trzy rzeczy, i tylko one:

1. rozwinąć skróty i liczby na zapis do czytania („Wopfu", „paragraf siódmy ustęp trzeci"),
2. dodać wskazówki aktorskie i pauzy w wersji TTS,
3. dopisać jedno zdanie zapowiedzi rozdziału tam, gdzie w druku jest sam nagłówek —
   bo słuchacz nie widzi nagłówka. To zdanie pokazujesz Ewie do akceptacji.

Czego w audio nie ma: numerów stron, odsyłaczy „patrz tabela obok", podpisów pod
ilustracjami. Zamiast „w tabeli obok" mów „za chwilę wymienię".

Plik nazywaj tak jak broszurę, z dopiskiem rodzaju: `nazwa-broszury-audio.mp3`, jeden
plik na rozdział. Oddajesz je razem z PDF-em, nie osobno.

### Podkasty

Odcinek jest dłuższy i słucha się go bez obrazu, więc trzyma go **struktura, nie plansze**:

1. **Czołówka** (20–30 s): kto mówi, o czym jest odcinek, dlaczego teraz. Nazwisko pada
   tu i tylko tu.
2. **Zapowiedź** (15 s): trzy rzeczy, które słuchacz będzie wiedział po odcinku.
3. **Bloki tematyczne** (3–5, po 3–6 min): jeden blok to jedna sprawa. Każdy zaczyna się
   pytaniem, które zadaje sala („Czy dyrektor musi…").
4. **Domknięcie** (30–60 s): co z tym zrobić w poniedziałek. Konkret, nie podsumowanie.

Zasady, które w podkaście różnią się od filmu:

- **Sygnalizuj przejścia głosem** — „to była pierwsza sprawa, teraz druga". Bez obrazu
  słuchacz nie wie, że zmienił się temat.
- **Powtórz to, co ważne, innymi słowami.** W filmie powtórzenie jest zbędne, bo wisi
  na planszy; w podkaście to jedyny sposób, żeby coś zostało.
- **Nie czytaj wyliczeń dłuższych niż trzy punkty.** Cztery punkty ze słuchu to za dużo —
  rozbij je na dwa zdania albo odeślij do druku.
- **Numery publikatorów podawaj raz**, przy pierwszym wystąpieniu, i wracaj do nazwy
  („to rozporządzenie"). Trzykrotnie przeczytana pozycja Dziennika Ustaw usypia.

Bloki generuj jako osobne pliki i sklej na końcu — poprawka jednego zdania nie może
oznaczać przegenerowania dwudziestu minut. Sklejenie bez przekodowania:

```bash
printf "file '%s'\n" blok-*.mp3 > lista.txt
ffmpeg -f concat -safe 0 -i lista.txt -c copy odcinek.mp3
```

## Wyrównanie głośności

Nagrania z ElevenLabs wychodzą zwykle o 1–4 dB ciszej niż jej filmy. Na styku słychać to
natychmiast, więc to nie jest opcjonalny szlif.

```bash
python3 .claude/skills/glos-ewy/scripts/wyrownaj_glosnosc.py \
        --cel-z-pliku film.mp4 katalog_z_mp3/*.mp3
```

Skrypt mierzy głośność materiału docelowego (EBU R128), liczy różnicę dla każdego pliku
i nakłada **stałe wzmocnienie**. Jednoprzebiegowy `loudnorm` tu nie wystarcza — potrafi
się rozminąć z celem o 2 dB, bo działa dynamicznie. Stałe wzmocnienie trafia w cel
i nie rusza dynamiki mowy.

Bez pliku odniesienia: `--cel -20.7` (zmierzony poziom narracji w modułach EduPlaner).

## Co oddajesz

1. **plik MP3** — wyślij go, nie podawaj samej ścieżki,
2. **tekst czysty** (`.txt`) — żeby dało się poprawić i przegenerować,
3. **tekst TTS** — żeby dało się powtórzyć dokładnie to samo brzmienie,
4. **długość nagrania i zużyte kredyty**.

Powiedz też uczciwie, czego nie możesz sprawdzić: **nagrania nie słychać z poziomu
narzędzi**. Możesz zweryfikować długość, tempo, głośność i to, czy wskazówki nie zostały
przeczytane na głos (gdyby zostały, nagranie byłoby zauważalnie dłuższe niż wynika
z liczby słów). Ocena samej intonacji należy do autorki — zostaw jej tę decyzję zamiast
zapewniać, że brzmi dobrze.

## Wklejanie wstawek do istniejącego filmu

Jeżeli nagranie ma trafić w środek gotowego modułu, cała procedura — namierzanie punktu
cięcia OCR-em paska napisów, renderowanie plansz w projekcie filmu i montaż — jest
opisana w `references/montaz-wstawek.md`. Tam też jest gotowy potok (`szkolenie-szkola/zloz_wstawki.py`), który przyjmuje pliki MP3
i zwraca złożony film.
