# HeyGen — Twój awatar i Twój głos

## Po co to w tym skillu

ElevenLabs daje **głos**. HeyGen daje **twarz mówiącą tym głosem**. Jeśli materiał ma trafić
na spotkanie z rodzicami, na stronę albo na social media, awatar niesie więcej niż sam dźwięk.

## Czego to złącze nie zrobi

Podłączone w tej sesji złącze **HyperFrames by HeyGen** buduje filmy z kodu HTML — nie ma
dostępu do Twoich awatarów ani do Twojego sklonowanego głosu. Do tego służy zwykłe API HeyGen
i skrypt `scripts/heygen_awatar.py`. Dodatkowo `compose` i `render_video` z HyperFrames są
wyłączone dla agentów działających z terminala, więc nie licz na nie w Claude Code.

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
