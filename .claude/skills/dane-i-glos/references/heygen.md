# HeyGen — Twój awatar i Twój głos

## Po co to w tym skillu

ElevenLabs daje **głos**. HeyGen daje **twarz mówiącą tym głosem**. Jeśli materiał ma trafić
na spotkanie z rodzicami, na stronę albo na social media, awatar niesie więcej niż sam dźwięk.

## Czego to złącze nie zrobi

Podłączone w tej sesji złącze **HyperFrames by HeyGen** buduje filmy z kodu HTML — nie ma
dostępu do Twoich awatarów ani do Twojego sklonowanego głosu. Do tego służy zwykłe API HeyGen
i skrypt `scripts/heygen_awatar.py`. Dodatkowo `compose` i `render_video` z HyperFrames są
wyłączone dla agentów działających z terminala, więc nie licz na nie w Claude Code.

## Zakładka Apps (app.heygen.com/apps)

Obok edytora HeyGen ma katalog **Apps** — pojedyncze narzędzia wideo, każde uruchamiane
w przeglądarce, bez instalacji. To nie są zewnętrzne wtyczki: efekty lądują w tej samej
przestrzeni roboczej co filmy z edytora i ze skryptu, więc gotowy materiał można
przepuścić przez apkę i wrócić z nim do projektu.

Kafelki, które mają znaczenie dla tego skilla:

| Apka | Co robi | Kiedy się przydaje |
|---|---|---|
| **Avatar IV** | najnowsza generacja awatara mówiącego, najbardziej „korporacyjna" mimika | materiał dla dyrekcji i rodziców, gdzie twarz ma wyglądać poważnie i naturalnie |
| **Video Translate** | tłumaczy gotowy film na 175+ języków, zachowując głos i ruch ust | ta sama prezentacja EduPlanera po angielsku lub ukraińsku, bez nagrywania od nowa |
| **Upscale** | podbija obraz do 4K, odszumia, wyostrza, podnosi liczbę klatek | starsze nagranie, które ma pójść na duży ekran |
| **Highlights** | wycina z długiego nagrania najmocniejsze fragmenty | webinar albo rada pedagogiczna → kilka krótkich klipów |
| **Face Swap** | wstawia Twoją twarz w jeden z gotowych awatarów | gdy nie chcesz nagrywać własnego Instant Avatara |
| **UGC Video Generator / Video Agent** | krótkie pionowe filmy w stylu nagrania z telefonu, w wielu wariantach | promocja EduPlanera na Reels, TikToka i Shorts |

### Apps czy skrypt

| Sytuacja | Czym |
|---|---|
| film z narracji tego skilla — tło marki, format, ten sam awatar co zawsze | `scripts/heygen_awatar.py` |
| kilkanaście wariantów jednego materiału (inne dane, ten sam scenariusz) | skrypt w pętli; w Apps to klikanie od nowa |
| obróbka **gotowego** pliku: upscale, tłumaczenie, highlighty | Apps — skrypt tego nie robi, API pokrywa tylko część tych funkcji |
| jednorazowy test „zobaczmy, jak to wygląda" | Apps, szybciej niż pisanie wywołania |

Apki zużywają **te same kredyty** co render z API — także wtedy, gdy wynik odrzucisz.
Zużycie sprawdzisz w ustawieniach konta, w historii generowań.

Dwie uwagi na koniec. Po pierwsze, HeyGen dokłada i wycofuje apki częściej niż zmienia API,
więc powyższa lista jest punktem wyjścia, a nie spisem z natury — w razie wątpliwości
otwórz stronę i sprawdź, co masz w swoim planie. Po drugie, nie myl Apps z **App
Integrations** (Zapier, Make, Canva, Adobe Express, HubSpot, ChatGPT): tamto podłącza HeyGen
do innych narzędzi i automatyzuje wysyłkę, a nie generuje wideo w przeglądarce.

## Czego NIE da się przenieść

Klon głosu utworzony w HeyGen **zostaje w HeyGen**. API zwraca `voice_id`, którym awatar
mówi podczas renderu — nie zwraca modelu głosu ani plików, z których powstał. Nie da się go
pobrać, wyeksportować ani zaimportować do ElevenLabs. To ograniczenie HeyGen, nie tego skilla.

Jeśli chcesz mieć swój głos po obu stronach, są dwie drogi:

1. **Zostaw go w HeyGen** i rób nim filmy z awatarem — etap 4b, wariant A (`--voice-id`).
2. **Odtwórz go w ElevenLabs** z tych samych nagrań wzorcowych, których użyłaś w HeyGen
   (albo nowych) — `elevenlabs_klon_glosu.py`. Dopiero wtedy działa ścieżka domyślna,
   w której jedno MP3 obsługuje i audio, i awatara.

Nagrania wzorcowe trzymaj u siebie na dysku. To jedyny materiał, z którego można odtworzyć
głos w dowolnej usłudze; klon w chmurze jest zawsze przywiązany do jednej platformy.

## Klucz

```bash
export HEYGEN_API_KEY="..."
export HEYGEN_AVATAR_ID="..."     # opcjonalnie, żeby nie podawać za każdym razem
export HEYGEN_VOICE_ID="..."
```

Klucz: app.heygen.com → **Settings → Subscriptions & API** (albo Space Settings → API Token).
Trzymaj go wyłącznie w zmiennej środowiskowej.

## Pierwsze uruchomienie — znajdź swoje zasoby

```bash
python3 scripts/heygen_awatar.py --awatary              # Twoje awatary i zdjęcia mówiące
python3 scripts/heygen_awatar.py --glosy --jezyk polish # głosy polskie, w tym Twój klon
```

Twój własny awatar (Instant Avatar) i sklonowany głos mają nazwy, które sama im nadałaś —
szukaj ich po nazwie, nie po opisie. Zapisz oba identyfikatory do zmiennych środowiskowych,
żeby nie szukać ich za każdym razem.

## Dwie drogi głosu — którą wybrać

| | `--voice-id` (tekst czyta HeyGen) | `--audio` (gotowe MP3) |
|---|---|---|
| Kto mówi | głos z konta HeyGen, także Twój klon | dowolny głos, np. z ElevenLabs |
| Kroków | jeden | dwa (najpierw ElevenLabs) |
| Kontrola nad brzmieniem | ustawienia HeyGen | pełna: `--stability`, `--speed`, pauzy |
| Napisy SRT | z HeyGen (`--napisy` wypala w obrazie) | dokładne, z ElevenLabs |
| Kiedy | masz w HeyGen swój głos i chcesz szybko | chcesz dopracować brzmienie osobno |

Ścieżka dwuetapowa (najlepsza jakość dźwięku):

```bash
python3 scripts/elevenlabs_tts.py narracja.txt -o glos.mp3 --srt napisy.srt
python3 scripts/heygen_awatar.py --audio glos.mp3 --avatar-id "$HEYGEN_AVATAR_ID" \
        --tlo "#2D1B69" --czekaj -o film.mp4
```

## Parametry, które mają znaczenie

| Przełącznik | Do czego |
|---|---|
| `--styl normal / circle / closeUp` | kadr awatara; `circle` pasuje do rogu prezentacji |
| `--tlo "#2D1B69"` | kolor marki PCTP; przyjmuje też adres URL obrazu |
| `--szerokosc 1080 --wysokosc 1920` | pion pod Reels i TikToka (domyślnie 1920×1080) |
| `--napisy` | wypala napisy w obrazie — nieodwracalne, więc tylko pod social media |
| `--talking-photo-id` | zamiast awatara animuje Twoje zdjęcie |
| `--czekaj` | czeka na render i pobiera plik; bez tego dostajesz sam `video_id` |
| `--suchy-bieg` | pokazuje zapytanie bez wysyłania i bez zużywania kredytów |

## Czas renderu i kredyty

Render minutowego filmu trwa zwykle 2–6 minut; skrypt odpytuje o status co 10 sekund i po
30 minutach przerywa czekanie, podając `video_id` do późniejszego sprawdzenia:

```bash
python3 scripts/heygen_awatar.py --status <video_id>
```

Każde generowanie zużywa kredyty z planu — także film, który potem odrzucisz. Dlatego
scenariusz akceptujesz **przed** wysłaniem, a przy dłuższych materiałach najpierw
`--suchy-bieg`.

## Kody błędów

| Kod | Znaczenie | Co zrobić |
|---|---|---|
| 400 | złe `avatar_id` lub `voice_id` | `--awatary`, `--glosy` |
| 401 | zły klucz | sprawdź `echo $HEYGEN_API_KEY` |
| 402 | brak kredytów | doładuj plan albo skróć materiał |
| 429 | limit zapytań | odczekaj i powtórz |

Status `failed` po udanym wysłaniu zwykle oznacza tekst dłuższy niż limit planu albo
niedostępny adres tła — skrypt wypisuje wtedy treść błędu z HeyGen.

## Uwaga o wersji API

Skrypt korzysta z `POST /v2/video/generate`, `GET /v2/avatars`, `GET /v2/voices`,
`GET /v1/video_status.get` oraz `POST upload.heygen.com/v1/asset`. HeyGen zmienia API
częściej niż ElevenLabs — jeśli któreś wywołanie zacznie zwracać nieoczekiwany kształt
odpowiedzi, sprawdź docs.heygen.com i popraw ścieżkę w skrypcie. Pierwsze `--awatary`
jest najprostszym testem, czy klucz i wersja API działają.
