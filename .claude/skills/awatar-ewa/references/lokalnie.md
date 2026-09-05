# Uruchomienie u siebie na komputerze

Środowiska zdalne (Claude Code na stronie, kontenery) mają zablokowane wyjście do
`api.heygen.com`, a złącze MCP HeyGen nie jest tam podłączone. Na własnym komputerze nie ma
tej przeszkody. Poniżej najkrótsza droga od zera do gotowego filmu.

## 1. Pobierz gałąź ze skillami

```bash
cd <katalog z repozytorium chatbot>
git fetch origin claude/heygen-mcp-integration-mdxgab
git checkout claude/heygen-mcp-integration-mdxgab
```

W `.claude/skills/` masz wtedy `awatar-ewa` oraz oficjalne `heygen-video`, `heygen-avatar`
i `heygen-translate`.

## 2. Zainstaluj CLI HeyGen i zaloguj się

```bash
curl -fsSL https://static.heygen.ai/cli/install.sh | bash
heygen auth login          # logowanie w przeglądarce, zapisuje się w ~/.heygen/credentials
heygen auth status         # potwierdzenie, że jesteś zalogowana
```

CLI to droga zalecana: `heygen-video` prowadzi przez nie pipeline v3 (korekta kadru, dobór
ujęcia). Klucz API nie jest do tego potrzebny — logowanie wystarcza.

## 3. Znajdź swojego awatara i swój głos

```bash
heygen avatar list --ownership private --limit 50
heygen voice list
```

Szukaj nazw, które sama nadałaś przy tworzeniu Instant Avatara i klonowaniu głosu. Zapisz
`avatar_id` i `voice_id` — przydadzą się w kroku 4b. Pusta lista awatarów prywatnych znaczy,
że awatara jeszcze nie ma: wtedy zacznij od skilla `heygen-avatar` (2–5 minut nagrania wideo).

## 4a. Najprościej — poproś Claude Code

Uruchom Claude Code w katalogu repozytorium i napisz zwykłym zdaniem:

```
Zrób powitanie moim awatarem, wersja B — 15 sekund, pion, forma „Ty".
```

`awatar-ewa` przypilnuje tożsamości i scenariusza, `heygen-video` wykona render przez
Video Agenta. Skrypty same znajdą CLI.

## 4b. Albo jednym poleceniem, bez Claude'a

```bash
heygen video-agent create \
  --prompt "$(cat prompt-powitanie.txt)" \
  --avatar-id "<Twój avatar_id>" \
  --voice-id "<Twój voice_id>" \
  --orientation portrait \
  --wait --timeout 45m
```

`--wait` bez `--timeout 45m` potrafi przerwać czekanie w połowie renderu — domyślne 20 minut
bywa za krótkie. Bez `--wait` dostajesz `video_id` i sprawdzasz później:
`heygen video-agent get <id>`. Sesję obejrzysz na `https://app.heygen.com/video-agent/<session_id>`.

Treść `prompt-powitanie.txt` (wersja B, 15 s, pion):

```
Zrób film z moim awatarem w HeyGen.

AWATAR: użyj mojego awatara „Ewa" z mojego konta. Nie dobieraj postaci z galerii.
        Jeśli nie znajdziesz mojego awatara — zatrzymaj się i zapytaj.
GŁOS: mój głos z konta. Język: polski.
DŁUGOŚĆ: około 15 sekund. FORMAT: 9:16, pion. Kadr od pasa w górę.
TŁO: jednolite, spokojne. NAPISY: po polsku, duże, wypalone w obrazie.

TEKST DO WYPOWIEDZENIA (przeczytaj dokładnie ten tekst, nie dopisuj własnych zdań):
---
Cześć, tu Ewa.
Witam Cię u siebie.
Zaglądaj tu po materiały, które ułatwiają codzienną pracę.
Krótko, konkretnie, od razu do użycia — bez godzin przygotowań.
Jeśli czegoś potrzebujesz, napisz do mnie.
Zaczynamy.
---
```

## 5. Droga zapasowa — klucz API i skrypt REST

Gdy CLI nie wchodzi w grę albo awatar ma mówić głosem z ElevenLabs:

```bash
export HEYGEN_API_KEY="..."        # app.heygen.com → Settings → Subscriptions & API
python3 .claude/skills/awatar-ewa/scripts/skonfiguruj_awatara.py
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py powitanie.txt \
        --szerokosc 1080 --wysokosc 1920 --tytul "Powitanie" --czekaj -o powitanie.mp4
```

Skrypt woła API v2, które HeyGen uznaje za przestarzałe — pomija korektę kadru z pipeline'u
v3. Dlatego to droga zapasowa, nie pierwsza.

## Gdy coś nie działa

| Objaw | Co zrobić |
|---|---|
| `heygen: command not found` | otwórz nową powłokę albo dodaj katalog instalacji do `PATH` |
| Kod wyjścia 3 przy każdym poleceniu | wygasła sesja — `heygen auth login` |
| Pusta lista awatarów prywatnych | awatara nie ma na koncie — zacznij od `heygen-avatar` |
| Nie znam argumentów polecenia | `heygen <rzeczownik> <czasownik> --help` — to jest dokumentacja |
| Render czerwony albo pusty | `.claude/skills/heygen-video/references/troubleshooting.md` |
