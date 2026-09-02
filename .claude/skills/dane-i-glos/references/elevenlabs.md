# ElevenLabs — co trzeba wiedzieć

## Dwie drogi dostępu

**1. Złącze (connector) w Claude** — narzędzia `mcp__ElevenLabs__*` pojawiają się wtedy
w sesji. Jeśli je widzisz, używaj ich; nie potrzeba wtedy klucza API ani skryptu.
Złącze włącza się na claude.ai → Ustawienia → Złącza (Connectors) → ElevenLabs,
a następnie w danym czacie w panelu złączy.

**2. Skrypt REST** (`scripts/elevenlabs_tts.py`) — działa zawsze, wymaga tylko klucza:

```bash
export ELEVENLABS_API_KEY="sk_..."
export ELEVENLABS_VOICE_ID="..."      # opcjonalnie, żeby nie podawać przy każdym wywołaniu
```

Klucz generuje się na elevenlabs.io → ikona profilu → **API Keys**. Przy tworzeniu klucza
zaznacz uprawnienie **text_to_speech** (bez niego API zwraca 403). Klucz trzymaj wyłącznie
w zmiennej środowiskowej — nigdy w pliku w repozytorium, w scenariuszu ani w treści rozmowy.

## Modele

| model_id | Kiedy | Uwagi |
|---|---|---|
| `eleven_multilingual_v2` | stabilna wymowa, obsługuje `<break>` | **na klonach potrafi brzmieć płasko i „robotycznie"** przy długich, informacyjnych tekstach |
| `eleven_v3` | **domyślny dla szkoleń i narracji jej głosem** | znaczniki emocji w nawiasach kwadratowych, wolniejszy, droższy — ale to on ratuje intonację |
| `eleven_turbo_v2_5` | gdy liczy się czas | niższa latencja, przyjmuje `language_code` |
| `eleven_flash_v2_5` | najszybszy, najtańszy | do długich, „roboczych" nagrań |

**Gdy nagranie brzmi jak robot, najpierw zmień model, a dopiero potem ustawienia.**
Sprawdzone na tym koncie: ten sam klon czytający ten sam tekst brzmi płasko na
`eleven_multilingual_v2`, a naturalnie na `eleven_v3` ze znacznikiem stylu na początku
akapitu, np. `[ciepło, spokojnie, jak do koleżanki w pokoju nauczycielskim]`.
Znacznik dotyczy całego dalszego fragmentu i **nie jest czytany na głos**.
Model zapamiętuje się raz: `skonfiguruj_glos.py --model eleven_v3`.

Polski jest obsługiwany przez wszystkie cztery. Przy modelach `*_v2_5` warto podać
`--jezyk pl`, żeby wymusić polską wymowę przy tekstach z nazwami obcymi.

## Formaty wyjściowe (`--format`)

`mp3_44100_128` (domyślny, dobry kompromis) · `mp3_44100_192` (wyższa jakość, plan Creator+)
· `mp3_22050_32` (najmniejszy plik) · `pcm_44100` (do dalszej obróbki w montażu)
· `ulaw_8000` (telefonia).

## Limity

- **Jedno zapytanie**: do ok. 5000 znaków dla `eleven_multilingual_v2` (skrypt tnie na
  fragmenty po ~2400 znaków z zapasem i zachowuje ciągłość przez `previous_text`/`next_text`).
- **Znaki z planu** zużywają się przy każdym wywołaniu, także nieudanym generowaniu
  odsłuchanym i odrzuconym. Dlatego **zawsze pokaż scenariusz do akceptacji przed generowaniem**,
  a przy dużych tekstach uruchom najpierw `--suchy-bieg`.
- **Równoległość**: darmowy plan pozwala na 2 równoczesne zapytania, płatne na więcej.
  Skrypt celowo generuje fragmenty po kolei.

## Ustawienia głosu

| Parametr | Zakres | Efekt |
|---|---|---|
| `--stability` | 0.0–1.0 | niżej = więcej emocji i zmienności; wyżej = spokojniej i przewidywalniej. Do raportów 0.5–0.7 |
| `--similarity` | 0.0–1.0 | wierność oryginalnej barwie głosu; 0.75 to dobry punkt startu |
| `--style` | 0.0–1.0 | wzmocnienie manieryzmów; powyżej 0.5 bywa karykaturalne |
| `--speed` | 0.7–1.2 | 1.0 to naturalne tempo; do treści urzędowych 0.95 |

Do materiałów informacyjnych i raportów: `--stability 0.6 --similarity 0.75 --style 0.0`.

## Napisy SRT

`--srt napisy.srt` używa końcówki `/with-timestamps`, która oprócz audio zwraca znaczniki
czasu **każdego znaku**. Skrypt składa z nich linie łamane na końcach zdań, więc napisy
są zsynchronizowane z rzeczywistym nagraniem, a nie szacowane z liczby słów.

## Kody błędów

| Kod | Znaczenie | Co zrobić |
|---|---|---|
| 401 | zły lub pusty klucz | sprawdź `echo $ELEVENLABS_API_KEY` |
| 403 | klucz bez uprawnienia | włącz `text_to_speech` przy kluczu na elevenlabs.io |
| 404 | nie ma takiego `voice_id` | uruchom `--glosy` |
| 422 | błędne parametry | zwykle zły `model_id` albo za długi tekst |
| 429 | wyczerpany limit | poczekaj albo skróć tekst |

## Sklejanie fragmentów

Skrypt łączy fragmenty MP3 bajtowo — odtwarzacze radzą sobie z tym bez problemu.
Jeśli plik ma trafić do montażu wideo, wygeneruj `--format pcm_44100` i złóż ścieżkę
w programie do montażu, gdzie masz kontrolę nad przejściami.
