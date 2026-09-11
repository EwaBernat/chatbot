# Złącze MCP HeyGen — podłączenie i diagnostyka

## Co to daje

Serwer MCP HeyGen wpuszcza do sesji **Video Agenta** — usługę, która z opisu w języku
naturalnym pisze scenariusz, dobiera awatara, składa sceny i renderuje film. Gotowe materiały
lądują na app.heygen.com → **Projects**.

To co innego niż złącze **HyperFrames by HeyGen**, które bywa podłączone w tej samej sesji:
HyperFrames buduje filmy z kodu HTML, **nie sięga po Twoje awatary ani Twój głos**, a jego
`compose` i `render_video` są wyłączone dla agentów działających z terminala. Do awatara służy
albo złącze opisane tutaj, albo API HeyGen (`scripts/heygen_awatar.py` w skillu `dane-i-glos`).

## Wymagania

- Claude Code (CLI, aplikacja lub wersja na stronie),
- Node.js — potrzebny do rozwiązania serwera MCP,
- konto HeyGen z dostępem do Video Agenta.

## Dodanie serwera

W terminalu (**nie** wewnątrz sesji Claude Code):

```bash
claude mcp add --transport http heygen https://mcp.heygen.com/mcp/v1/
```

Żeby złącze było dostępne we wszystkich projektach, a nie tylko w bieżącym katalogu:

```bash
claude mcp add --transport http -s user heygen https://mcp.heygen.com/mcp/v1/
```

| Zasięg | Flaga | Plik konfiguracji | Gdzie działa |
|---|---|---|---|
| lokalny (domyślny) | brak | `.mcp.json` w katalogu projektu | tylko ten projekt |
| użytkownika | `-s user` | `~/.claude.json` | wszystkie projekty |

Zasięg lokalny zapisuje wpis do `.mcp.json` w repozytorium — ten plik jest wersjonowany,
więc złącze pojawi się też u innych osób pracujących na tym repozytorium. Klucza to nie
dotyczy: logowanie jest przez OAuth, w `.mcp.json` nie ląduje żaden sekret.

Ręczna droga — wpis w `~/.claude.json` i restart Claude Code:

```json
{
  "mcpServers": {
    "heygen": {
      "type": "http",
      "url": "https://mcp.heygen.com/mcp/v1/"
    }
  }
}
```

## Logowanie

Przy pierwszym użyciu Claude Code poprosi o autoryzację. W sesji: `/mcp` → `heygen` →
logowanie w przeglądarce (OAuth) → zgoda na dostęp.

## Sprawdzenie połączenia

```bash
claude mcp list        # z terminala
```

albo `/mcp` w sesji. Szukasz wpisu `heygen` ze statusem `connected`. W tej samej sesji
narzędzia widać po przedrostku `mcp__heygen__`.

## Kiedy złącze nie działa

| Objaw | Przyczyna | Co zrobić |
|---|---|---|
| Brak `heygen` na liście | serwer dodany w innym zasięgu | `claude mcp list` w tym katalogu; dodaj z `-s user` |
| Status inny niż `connected` | wygasła autoryzacja | `/mcp` → zaloguj ponownie |
| Narzędzia są, ale nie ma awatara | Video Agent dobrał postać z galerii | nazwij awatara w promptcie — `references/prompt-agenta.md` |
| Nic się nie renderuje | brak kredytów albo dostępu do Video Agenta | sprawdź plan na app.heygen.com |
| Serwer dodany, ale sesja go nie widzi | konfiguracja zmieniona po starcie sesji | zrestartuj Claude Code |

Blokada sieciowa środowiska (`403` przy `curl`) **nie dotyczy złącza** — wywołania MCP idą
spoza kontenera. Jeśli w tej samej sesji `curl https://api.heygen.com/` zwraca `000`,
a złącze działa, to nie jest sprzeczność: to dwie różne drogi do tej samej usługi.

## Prompty HeyGen (opcjonalnie)

HeyGen publikuje własne wskazówki do budowania promptów: <https://github.com/heygen-com/skills>
(`SKILL.md`, `references/prompt-optimizer.md`, `references/video-agent.md`). Warto je wczytać
przy dłuższych, scenowanych materiałach. Do krótkiej wypowiedzi do kamery wystarcza szablon
z `references/prompt-agenta.md` — i tak nadpisuje on wybór awatara, czego same wskazówki
HeyGen nie robią.
