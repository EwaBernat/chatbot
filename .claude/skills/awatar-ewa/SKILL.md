---
name: awatar-ewa
description: Robi filmy, w których mówi awatar Ewy w HeyGen — od pomysłu albo gotowego tekstu do pliku MP4: scenariusz po polsku, jej awatar, jej głos, render i odbiór gotowego materiału. Dwie drogi: złącze MCP HeyGen (Video Agent, prompt w języku naturalnym) oraz skrypt REST z pełną kontrolą nad kadrem, tłem i formatem. NIGDY nie generuje filmu cudzym awatarem ani cudzym głosem — bez zapamiętanego awatara oddaje scenariusz i zatrzymuje się. Użyj ZAWSZE, gdy prosi o: „film z moim awatarem", „nagraj to moją twarzą", „awatar Ewa", „spot z awatarem", „wiadomość wideo do rodziców", „powitanie na stronę", „przerób ten tekst na film", „wersja pionowa na Reels", „popraw scenariusz i wygeneruj jeszcze raz". Wyzwalaj przy hasłach: HeyGen, Video Agent, awatar, talking photo, Instant Avatar, mcp.heygen.com, render awatara, lipsync. NIE używaj do filmów z samymi wykresami (skill dane-i-glos, etap 4c) ani do filmów budowanych z HTML (złącze HyperFrames).
---

# Awatar Ewy w HeyGen

Skill prowadzi jedną drogę: **zamówienie → scenariusz → akceptacja → render → plik**.
Twarz i głos są ustalone raz, na starcie, i nie zmieniają się między materiałami: to ma być
zawsze ten sam człowiek na ekranie.

## Zasada nadrzędna: jej awatar i jej głos

**Nigdy nie generuj filmu cudzym awatarem ani cudzym głosem.** Materiał firmowany jej
nazwiskiem ma pokazywać ją — obca twarz z galerii HeyGen podważa wiarygodność materiału
i nie jest tym, o co prosiła.

To jest realne ryzyko, nie teoria: **Video Agent w HeyGen sam dobiera awatara**, gdy prompt
tego nie przesądza, i wybiera wtedy postać z galerii. Dlatego w każdym promptcie do agenta
nazwij jej awatara wprost, a w skrypcie REST podaj `avatar_id` (skrypt bierze go z pamięci).

Gdy skill nie ma zapamiętanego jej awatara:

1. **Zrób wszystko, co nie wymaga renderu** — ustal zamówienie, napisz scenariusz, dobierz
   długość i format. To realna wartość i nie czeka na nic.
2. **Zatrzymaj się przed generowaniem.** Oddaj scenariusz i powiedz wprost, czego brakuje
   (etap 0 zajmuje jedno polecenie).
3. **Nie proponuj zastępstwa** „na razie", „do podglądu" ani „żeby zobaczyć, jak to wygląda".
   Każdy render kosztuje kredyty, a film z obcą twarzą i tak pójdzie do kosza.

To samo dotyczy głosu. Awatar mówiący cudzym głosem to ten sam problem, tylko słychać go
przez całą minutę.

## Etap 0 — Kim jest awatar (jednorazowo)

```bash
python3 .claude/skills/awatar-ewa/scripts/skonfiguruj_awatara.py --pokaz
```

Jeśli skill pamięta awatara i głos — nic więcej nie rób, skrypty same ich użyją. Jeśli nie:

```bash
export HEYGEN_API_KEY="..."        # app.heygen.com → Settings → Subscriptions & API
python3 .../skonfiguruj_awatara.py                    # szuka „Ewa" wśród awatarów i głosów
python3 .../skonfiguruj_awatara.py --szukaj "Ewa PL"  # gdy nazwa jest inna
python3 .../skonfiguruj_awatara.py --tylko-pokaz-konto # wypisuje wszystko, nic nie zapisuje
```

Przy jednym trafieniu skrypt zapisuje `avatar_id` i `voice_id` w pamięci skilla
(`~/.config/dane-i-glos/konfiguracja.json` — poza repozytorium, wspólna ze skillem
`dane-i-glos`). Przy kilku kandydatach **nie zgaduje** — wypisuje ich i czeka na
`--awatar-id <id>`. Kluczy API ten plik nie przyjmuje.

Nie ma jeszcze awatara na koncie HeyGen? Instant Avatar powstaje z 2–5 minut nagrania wideo
(app.heygen.com → Avatars → Create Instant Avatar); zdjęcie mówiące (talking photo) wystarcza
na krótkie materiały i też jest tu obsługiwane. `--zapomnij` czyści pamięć, nie ruszając konta.

## Którą drogą renderować

| | **A. Złącze MCP (Video Agent)** | **B. Skrypt REST** |
|---|---|---|
| Sterowanie | prompt w języku naturalnym | parametry wiersza poleceń |
| Kto pisze scenariusz | agent HeyGen (albo Ty w promptcie) | Ty, plik `.txt` |
| Kontrola kadru, tła, formatu | pośrednia, przez opis | pełna (`--styl`, `--tlo`, wymiary) |
| Wybór awatara | **trzeba nazwać w promptcie** | z pamięci skilla, bez pytania |
| Głos z ElevenLabs | nie | tak (`--audio`) |
| Gdzie ląduje film | Projects na app.heygen.com | plik MP4 na dysku |
| Sieć w tej sesji | działa (połączenie spoza kontenera) | bywa zablokowana — patrz niżej |
| Konfiguracja | `claude mcp add …` + OAuth | `HEYGEN_API_KEY` |

Reguła kciuka: **scena, plansze, montaż i „zrób z tego ładny materiał" → A**;
**stały format, jej głos z ElevenLabs, powtarzalny render → B**.

## Oficjalne skille HeyGen w tym repozytorium

W `.claude/skills/` leżą też trzy skille od HeyGen (MIT, wersja 3.2.0): `heygen-video`
(render przez Video Agent v3), `heygen-avatar` (tworzenie awatara) i `heygen-translate`
(dubbing z zachowaniem twarzy i głosu). Podział pracy jest taki:

- **Ten skill decyduje, kto mówi i co mówi.** Zasada nadrzędna, ustalenie zamówienia,
  scenariusz po polsku i akceptacja przed renderem — to zostaje tutaj.
- **`heygen-video` wykonuje render**, gdy w sesji jest złącze MCP, CLI `heygen` albo wtyczka
  OpenClaw. Prowadzi Frame Check, dobór ujęcia i rozmowę z Video Agentem lepiej niż surowe
  API. Wywołaj go po akceptacji scenariusza i przekaż mu gotowy tekst.
- **`heygen-avatar` zakłada awatara**, gdy konto go jeszcze nie ma. Zapisuje tożsamość do
  pliku `AVATAR-<IMIE>.md` w katalogu głównym — `heygen-video` czyta go przed katalogiem
  HeyGen, więc taki plik jest drugą (obok pamięci tego skilla) kotwicą tożsamości.

Uwaga o wersjach API: `heygen-video` **zakazuje** wywołań `POST /v2/video/generate`, z których
korzysta `heygen_awatar.py` — HeyGen uznaje v2 za przestarzałe. Dlatego skrypt REST (etap 3b)
jest teraz **drogą zapasową**: na wypadek, gdy nie ma ani MCP, ani CLI, albo gdy potrzebujesz
awatara mówiącego głosem z ElevenLabs, czego oficjalne skille nie obsługują.

Trzecia droga bywa właściwsza: materiał o **liczbach** (raport, frekwencja, wyniki) prowadzi
skill `dane-i-glos` — tam narracja powstaje z profilu danych, więc film nie zmyśli żadnej
liczby. Tutaj wracasz na etapie renderu.

## Etap 1 — Ustal zamówienie, zanim napiszesz zdanie

Zapytaj o to, czego nie widać w prośbie (jednym pytaniem, nie ankietą):

- **Do kogo** — rodzice, dyrekcja, nauczyciele, klienci, ona sama?
- **Po co** — informacja, zaproszenie, instrukcja, promocja?
- **Jak długo** — 30 s (≈75 słów), 60 s (≈150 słów), 90 s (≈225 słów)?
- **Gdzie trafi** — strona i YouTube (poziom 1920×1080), Reels, TikTok i Stories
  (pion 1080×1920), prezentacja (awatar w rogu, `--styl circle`)?
- **Co ma się stać po obejrzeniu** — jedno konkretne wezwanie na koniec.

Bez odpowiedzi przyjmij: 60 s, poziom, ton rzeczowy i uprzejmy — i **powiedz, co przyjęłaś**.

## Etap 2 — Scenariusz i akceptacja

Pełne zasady: `references/scenariusz.md`. Skrót:

- **Tempo**: ok. 150 słów na minutę po polsku. Licz słowa, nie znaki.
- **Liczby i skróty zapisuj tak, jak się je czyta**: `87,5%` → „osiemdziesiąt siedem i pół
  procent", `IPET` → „i-pet" albo pełna nazwa. Silnik czyta polskie cyfry niepewnie.
- **Mówisz do jednej osoby, prosto w kamerę.** „Państwo" albo „Ty" — konsekwentnie.
- **Jedno zdanie = jedna myśl**, do 20 słów. Pauzy nową linią.
- **Struktura**: haczyk (1 zdanie) → sedno (3–5) → wezwanie (1).

Zapisz scenariusz do `.txt` i **pokaż go do akceptacji przed renderem**. Poprawka w tekście
kosztuje sekundę, przegenerowanie filmu — kredyty HeyGen. To także moment, w którym ona
decyduje, co jej twarz powie: awatar wygląda jak ona, więc treść musi być jej.

## Etap 3a — Render przez złącze MCP (Video Agent)

Sprawdź, czy w sesji są narzędzia `mcp__heygen__*`. Jeśli ich nie ma, złącze trzeba dodać
raz — pełna instrukcja i diagnostyka: `references/mcp.md`:

```bash
claude mcp add --transport http heygen https://mcp.heygen.com/mcp/v1/   # w terminalu
claude mcp add --transport http -s user heygen https://mcp.heygen.com/mcp/v1/  # wszystkie projekty
```

Potem `/mcp` w Claude Code → logowanie OAuth w przeglądarce → `heygen` ze statusem
`connected`. Droga bez złącza MCP — CLI HeyGen, które `heygen-video` obsługuje tak samo:

```bash
curl -fsSL https://static.heygen.ai/cli/install.sh | bash
heygen auth login
```

Mając którąkolwiek z nich, **oddaj render skillowi `heygen-video`** wraz z zaakceptowanym
tekstem — i przypilnuj, żeby wybór awatara nie wrócił do galerii. Prompt budujesz tak samo:

Prompt do agenta buduj według `references/prompt-agenta.md` — szablon i przykłady. Trzy rzeczy
muszą w nim być zawsze:

1. **awatar po nazwie** („użyj mojego awatara **Ewa**, nie dobieraj postaci z galerii"),
2. **język polski** wprost — inaczej agent potrafi przełączyć się na angielski,
3. **gotowy scenariusz** z etapu 2 jako treść wypowiedzi, a nie temat do rozwinięcia.

Gotowy film ląduje na app.heygen.com → **Projects**. Podaj jej link, a nie tylko informację,
że render ruszył.

## Etap 3b — Render przez API (droga zapasowa, pełna kontrola)

Sięgaj po nią, gdy nie ma ani złącza MCP, ani CLI `heygen`, albo gdy awatar ma mówić głosem
z ElevenLabs (etap 3c). Skrypt woła `POST /v2/video/generate`, które HeyGen uznaje za
przestarzałe — działa, ale pomija Frame Check i korektę kadru z pipeline'u v3.

```bash
export HEYGEN_API_KEY="..."
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py narracja.txt \
        --tytul "Zaproszenie na zebranie" --czekaj -o film.mp4
```

`avatar_id` i `voice_id` idą z pamięci z etapu 0 — nie podawaj ich, jeśli nie zmieniasz
domyślnych. Przydatne: `--tlo "#2D1B69"`, `--styl circle`, `--szerokosc 1080 --wysokosc 1920`
(pion), `--napisy` (wypala napisy — nieodwracalnie), `--suchy-bieg` (podgląd zapytania bez
kredytów), `--status <video_id>` (sprawdzenie renderu później).

Render trwa zwykle 2–6 minut na minutę materiału. Parametry, kredyty i kody błędów:
`.claude/skills/dane-i-glos/references/heygen.md`.

## Etap 3c — Awatar mówiący jej głosem z ElevenLabs

Gdy jej klon głosu jest w ElevenLabs, a nie w HeyGen — najpierw dźwięk, potem obraz:

```bash
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_tts.py narracja.txt -o glos.mp3 --srt napisy.srt
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --audio glos.mp3 --czekaj -o film.mp4
```

MP3 steruje ustami awatara, więc brzmienie jest w całości z ElevenLabs (pauzy, tempo,
stabilność), a napisy z `--srt` są dokładniejsze niż wypalane przez HeyGen.
Klon głosu z HeyGen **zostaje w HeyGen** — nie da się go przenieść i odwrotnie.

## Etap 4 — Obejrzyj, zanim oddasz

Render kończy się plikiem, nie sukcesem. Sprawdź:

- **twarz i głos są jej** — jeśli nie, film nie wychodzi z tej sesji,
- **wymowa liczb, skrótów i nazw własnych** — najczęstsze źródło wpadki,
- **długość** zgodna z zamówieniem (±10 s) i **format kadru** zgodny z miejscem publikacji,
- **napisy**, jeśli materiał idzie na social media (dźwięk bywa wyłączony).

Oddaj komplet: film (wyślij plik albo link do Projects), tekst scenariusza `.txt` do poprawek,
napisy `.srt`, jeśli powstały. Podaj, co się zużyło — kredyty HeyGen, znaki ElevenLabs.
Coś się nie udało? Powiedz, co i dlaczego, zamiast oddawać po cichu niepełny zestaw.

## Zanim uruchomisz skrypty — sprawdź, czy sieć przepuszcza

W środowiskach zdalnych (Claude Code na stronie, kontenery CI) polityka sieciowa często
blokuje wyjście do api.heygen.com. Skrypty zwracają wtedy `403`, co łatwo pomylić ze złym
kluczem:

```bash
curl -sS -o /dev/null -w "%{http_code}\n" --max-time 10 https://api.heygen.com/
```

`000` z `CONNECT tunnel failed, response 403` to **blokada środowiska**, nie problem z kluczem.
Złącze MCP działa mimo niej (łączy się spoza kontenera), skrypty nie. Nie powtarzaj wywołań
po odmowie polityki — zgłoś ją i zaproponuj uruchomienie skryptów na jej komputerze.

## Klucze i wizerunek

Klucz API trzymaj wyłącznie w zmiennej środowiskowej — nigdy w pliku w repozytorium ani
w treści rozmowy. Awatar jest jej wizerunkiem: renderuj wyłącznie scenariusz, który
zaakceptowała, i nie dokładaj do niego zdań „od siebie" po akceptacji.

## Materiały

- `references/mcp.md` — dodanie złącza HeyGen, OAuth, zasięgi, diagnostyka połączenia
- `references/prompt-agenta.md` — szablon promptu do Video Agenta i gotowe przykłady
- `references/scenariusz.md` — zasady pisania pod awatara po polsku, wzorce i długości
- `scripts/skonfiguruj_awatara.py` — pamięć skilla: awatar i głos HeyGen
- `.claude/skills/dane-i-glos/scripts/heygen_awatar.py` — render przez API
- `.claude/skills/dane-i-glos/references/heygen.md` — API, kredyty, kody błędów
- `.claude/skills/heygen-video/` — oficjalny skill HeyGen: render przez Video Agent v3
- `.claude/skills/heygen-avatar/` — zakładanie awatara i plik tożsamości `AVATAR-<IMIE>.md`
- `.claude/skills/heygen-translate/` — dubbing gotowego filmu na inny język
