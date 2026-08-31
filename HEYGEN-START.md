# HeyGen — Twój agent do filmów (Twój głos, Twoja twarz)

Ten plik to instrukcja uruchomienia. Skille HeyGen są już w repozytorium — brakuje
tylko klucza API i **uruchomienia Claude Code lokalnie**, bo sesja webowa nie ma
dostępu do serwerów HeyGen (szczegóły niżej).

## Co jest zainstalowane

W `.claude/skills/` leżą trzy oficjalne skille HeyGen (wersja 3.2.0, z
[github.com/heygen-com/skills](https://github.com/heygen-com/skills)):

| Skill | Do czego |
|---|---|
| `heygen-avatar` | tworzy Twój awatar — twarz + głos, zapisuje do `AVATAR-<IMIĘ>.md` |
| `heygen-video` | robi filmy z awatarem (pipeline Video Agent v3, Frame Check, kadrowanie) |
| `heygen-translate` | dubbinguje gotowy film na inny język z zachowaniem Twojego głosu i lip-sync |

Obok stoi Twój wcześniejszy skill `dane-i-glos` — on prowadzi drogę
**dane → scenariusz → głos ElevenLabs → film**. Nowe skille HeyGen są komplementarne:
odpowiadają za tożsamość awatara i produkcję wideo.

## ⚠️ Dlaczego nie da się tego dokończyć w sesji webowej

Claude Code na web działa w kontenerze z polityką ruchu wychodzącego, która
**blokuje wszystkie domeny HeyGen** (403 na poziomie bramy):

```
static.heygen.ai   → 403    (instalator CLI)
api.heygen.com     → 403
mcp.heygen.com     → 403
app.heygen.com     → 403
upload.heygen.com  → 403
resource.heygen.com→ 403
api.elevenlabs.io  → 403
```

Nie da się tego obejść z wnętrza sesji — to polityka organizacji, nie błąd.
Dlatego **awatara tworzysz z Claude Code uruchomionego na własnym komputerze**
(desktop albo terminal). Repozytorium z tymi skillami wystarczy sklonować.

Alternatywa: poprosić administratora o dopuszczenie tych domen dla środowiska
Claude Code on the web ([ustawienia dostępu](https://claude.ai/admin-settings/claude-tag)).

## Krok 1 — klucz API

1. Wejdź na [app.heygen.com/api](https://app.heygen.com/api) → **Settings → API → New Key**.
2. **Klucz pokazuje się tylko raz** — skopiuj go zanim zamkniesz okno.
3. Wpisz do swojego profilu powłoki (`~/.zshrc` albo `~/.bashrc`):

   ```bash
   export HEYGEN_API_KEY="hg_..."
   ```

4. `source ~/.zshrc` (albo nowe okno terminala) i **restart Claude Code** —
   agent dziedziczy zmienne z powłoki rodzica, samo `source` w innym oknie nie wystarczy.

Klucza **nie wklejaj do czatu ani do repozytorium**. `.env` jest w `.gitignore`,
ale zmienna środowiskowa jest bezpieczniejsza.

HeyGen API rozlicza się w kredytach (pay-as-you-go, bez darmowego progu) — Avatar V
to ok. 6 kredytów za minutę wygenerowanego wideo. Sprawdź stan konta na
[app.heygen.com/billing](https://app.heygen.com/billing) zanim zaczniesz.

## Krok 2 — transport

Skille rozmawiają z HeyGen przez CLI albo przez MCP. Nigdy przez `curl` do `api.heygen.com`.

**CLI (najprostsze):**

```bash
curl -fsSL https://static.heygen.ai/cli/install.sh | bash
heygen auth login          # albo po prostu zostaw HEYGEN_API_KEY w środowisku
heygen --version           # musi zwrócić 0
```

**MCP (alternatywa):** podłącz serwer `https://mcp.heygen.com/mcp/v1/` w ustawieniach
Claude Code. Uwaga: **ustawiony `HEYGEN_API_KEY` wyłącza wykrywanie MCP** — skill wybiera
wtedy CLI. Jeśli chcesz rozliczać się kredytami planu (a nie API), nie ustawiaj klucza.

> Podłączone w tej sesji złącze **HyperFrames by HeyGen** to *inny* produkt — buduje
> filmy z kodu HTML i nie ma dostępu do awatarów ani do sklonowanego głosu.
> Do awatara potrzebne jest CLI albo MCP HeyGen.

## Krok 3 — Twój awatar

W Claude Code (lokalnie) napisz po prostu:

```
stwórz mój awatar — moja twarz i mój głos
```

Skill `heygen-avatar` poprowadzi rozmowę fazami, po jednym–dwóch pytaniach:
wygląd, głos, potwierdzenie promptu, wybór głosu. **Przed wygenerowaniem awatara
jest gate — nic się nie tworzy i żaden kredyt nie schodzi, dopóki nie zatwierdzisz.**

### Twoja twarz — trzy drogi

| Materiał | Typ | Efekt |
|---|---|---|
| zdjęcie portretowe | `photo` | cyfrowy bliźniak z fotografii |
| krótkie nagranie wideo | `digital_twin` | najwierniejszy, oddaje też mimikę |
| sam opis słowny | `prompt` | postać wygenerowana przez AI (nie Ty) |

Skoro ma być **Twój wygląd**, wybierz `photo` albo `digital_twin`.
Wymagania dla zdjęcia: JPEG/PNG, minimum 512×512, twarz na wprost, dobre światło.

Zdjęcie trzymaj lokalnie — skill wgra je do HeyGen dopiero na Twoją wyraźną prośbę.

### Twój głos — dwie drogi

Skill `heygen-avatar` sam **nie klonuje głosu** — potrafi tylko dobrać głos
z katalogu HeyGen (`design_voice` / `list_voices`). Żeby awatar mówił *Twoim* głosem:

1. **Klon w HeyGen** — sklonuj głos w aplikacji `app.heygen.com` (Voice Cloning).
   Potem pojawi się jako głos prywatny i skill go znajdzie:
   ```bash
   heygen voice list --type private
   ```
   Jego `voice_id` wpisujesz do sekcji `## HeyGen` w pliku `AVATAR-<IMIĘ>.md`.
   Klon zostaje w HeyGen — API nie pozwala go pobrać ani przenieść.

2. **Klon w ElevenLabs** — masz do tego gotowy skrypt w skillu `dane-i-glos`:
   ```bash
   python3 .claude/skills/dane-i-glos/scripts/elevenlabs_klon_glosu.py "Ewa - narracja PL" probki/*.wav
   ```
   Wtedy generujesz MP3 osobno i podajesz je HeyGenowi jako ścieżkę audio
   (`scripts/heygen_awatar.py --audio glos.mp3`). Daje pełną kontrolę nad brzmieniem
   i dokładne napisy SRT, kosztem jednego kroku więcej.

Jeśli chcesz mieć swój głos po obu stronach — sklonuj go dwa razy, z tych samych
nagrań wzorcowych. Nagrania trzymaj u siebie na dysku, to jedyny materiał,
z którego można głos odtworzyć gdziekolwiek.

**Klonuj wyłącznie własny głos** albo głos osoby, która wyraziła wyraźną zgodę.

## Krok 4 — pliki awatara

Po udanym utworzeniu skill zapisuje w katalogu głównym repozytorium:

```
AVATAR-<IMIĘ>.md      ← plik kanoniczny: wygląd, głos, group_id, voice_id
AVATAR-USER.md        ← dowiązanie symboliczne na plik powyżej
```

`heygen-video` czyta te pliki automatycznie — dlatego „zrób film ze mną" wystarczy
za całą konfigurację. **Nie twórz `AVATAR-*.md` ręcznie przed pierwszym uruchomieniem
skilla** — plik z pustą sekcją HeyGen sprawia, że skill pomija rozmowę o wyglądzie
i przechodzi od razu do generowania.

Uwaga: `group_id` jest stabilne i to jego się trzymasz. `look_id` są ulotne —
zawsze rozwiązuj je świeżo przez `heygen avatar looks list --group-id <id>`.

## Krok 5 — filmy

```
zrób 30-sekundowy film ze mną, w którym opowiadam o EduPlaner 2026
przetłumacz ten film na angielski i niemiecki
```

`heygen-video` sam dobiera kadr, proporcje, prompt i długość.
`heygen-translate` zachowuje Twoją twarz i głos w innym języku, z lip-syncem.

## Test dymny (opcjonalny, ok. 0,5 kredytu)

```
zrób 5-sekundowy klip testowy moim awatarem: "HeyGen działa, można nagrywać"
```

Jeśli nie zadziała, w kolejności: (1) `HEYGEN_API_KEY` nie widoczny w procesie agenta —
restart Claude Code, nie tylko `source`; (2) brak kredytów; (3) `heygen --version`
nie zwraca 0.

## Aktualizacja skilli

```bash
git clone --depth 1 https://github.com/heygen-com/skills.git /tmp/heygen-skills
cp -r /tmp/heygen-skills/heygen-{avatar,video,translate} .claude/skills/
```

Zainstalowana wersja: patrz `.claude/skills/.heygen-skills-version`.
