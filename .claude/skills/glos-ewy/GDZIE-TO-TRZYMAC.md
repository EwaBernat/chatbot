# Gdzie trzymać agenta i skill głosu Ewy

Krótka odpowiedź: **skill zapisz na koncie** (jeden klik), a **agenta skopiuj do katalogu
osobistego** (jedno polecenie). Wtedy oba są w każdym projekcie i każdej sesji.

## Trzy miejsca — i czym się różnią

| Miejsce | Widoczność | Kiedy używać |
|---|---|---|
| **konto claude.ai** (`Save skill`) | wszędzie, w każdej sesji i projekcie, także po zmianie komputera | **to jest właściwe miejsce dla tego skilla** |
| `~/.claude/agents/` i `~/.claude/skills/` | wszystkie projekty na tym komputerze | dla agenta — nie da się go zapisać na koncie |
| `.claude/agents/` i `.claude/skills/` w repozytorium | tylko ten projekt | rzeczy związane z jednym repozytorium |

Dziś głos Ewy leży w trzecim miejscu — w repozytorium `chatbot`. Dlatego widać go tylko
wtedy, gdy pracujesz w tym repozytorium. To jest cała przyczyna kłopotu ze znalezieniem.

## Skill — jeden klik

Weź plik `glos-ewy.skill` i kliknij **Save skill** na karcie pliku. Skill trafia na konto
i od tej pory pojawia się sam, w każdej rozmowie, po frazie „przywołaj agenta głosu Ewy"
albo pod skrótem `/glos-ewy`. Nie trzeba niczego kopiować ani pamiętać, gdzie leży.

## Agent — jedno polecenie

Agentów nie da się zapisać na koncie, więc kopiujemy plik do katalogu osobistego na swoim
komputerze:

```bash
mkdir -p ~/.claude/agents
cp .claude/agents/glos-ewy.md ~/.claude/agents/
```

Od następnego uruchomienia Claude Code agent `glos-ewy` jest widoczny w każdym projekcie.

## Sprawdzenie, czy się udało

- Skill: wpisz `/glos-ewy` — powinien się podpowiedzieć.
- Agent: powiedz „przywołaj agenta głosu Ewy".

Jeżeli któreś nie działa od razu, zamknij i otwórz sesję — lista agentów wczytuje się
przy starcie.

## Jeśli wolisz mieć wszystko w jednym miejscu na dysku

```bash
mkdir -p ~/.claude/agents ~/.claude/skills
cp .claude/agents/glos-ewy.md ~/.claude/agents/
cp -r .claude/skills/glos-ewy ~/.claude/skills/
```

Ta droga działa bez konta, ale tylko na tym komputerze — po przesiadce na inny trzeba
powtórzyć. Zapis na koncie tego nie wymaga.
