---
name: glos-ewy
description: Nagrywa narrację i wstawki lektorskie głosem Mirosławy Ewy Jurczyszyn — jej sklonowanym głosem z ElevenLabs, w intonacji osoby prowadzącej szkolenie. Trzyma zapamiętany voice_id, słownik wskazówek aktorskich, zasady zapisu liczb pod polskiego lektora i procedurę wyrównania głośności do istniejącego filmu. Użyj ZAWSZE, gdy pada „przywołaj agenta głosu Ewy", „agent głosu Ewy", „dodaj mój głos", „nagraj to moim głosem", „mój głos do tego szkolenia", „lektor", „narracja", „voice-over", „dogranie do filmu", „wstawka do modułu", „udźwiękowij" — a także wtedy, gdy powstaje materiał szkoleniowy EduPlaner albo PCTP, który ma mieć ścieżkę dźwiękową, nawet jeśli nikt nie powiedział wprost „głos". Skill NIGDY nie nagrywa cudzym głosem: bez dostępu do jej głosu oddaje sam tekst narracji i zatrzymuje się. NIE używaj do samej analizy danych ani do pisania scenariusza bez dźwięku — do tego służy skill dane-i-glos.
---

# Głos Ewy

Ten skill istnieje po to, żeby każde nagranie firmowane nazwiskiem Mirosławy Ewy
Jurczyszyn brzmiało nią i pasowało do materiału, do którego trafia. Trzyma trzy rzeczy,
które za każdym razem trzeba by odtwarzać od zera: **który to głos**, **jak pisać, żeby
zabrzmiał jak na szkoleniu**, i **jak dopasować go do istniejącego filmu**.

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
opisana w `references/montaz-wstawek.md`. Tam też jest gotowy potok
(`szkolenie-szkola/zloz_wstawki.py`), który przyjmuje pliki MP3 i zwraca złożony film.
