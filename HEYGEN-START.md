# HeyGen — Twój agent do filmów (Twój głos, Twoja twarz)

Ten plik to instrukcja uruchomienia. Skille HeyGen są już w repozytorium — brakuje
tylko klucza API i **uruchomienia Claude Code lokalnie**, bo sesja webowa nie ma
dostępu do serwerów HeyGen (szczegóły niżej).

## Twoja droga — lista kontrolna

Wybrane ustalenia: **Claude Code lokalnie** + **głos sklonowany w ElevenLabs**.

- [ ] 1. Klucz HeyGen z `app.heygen.com` → `export HEYGEN_API_KEY` w `~/.zshrc` (krok 1)
- [ ] 2. Klucz ElevenLabs → `export ELEVENLABS_API_KEY` tamże (krok 1)
- [ ] 3. Sklonuj to repozytorium u siebie i otwórz w nim Claude Code
- [ ] 4. Zainstaluj CLI HeyGen, sprawdź `heygen --version` (krok 2)
- [ ] 5. Nagraj ok. 3 minut próbek po polsku i sklonuj głos w ElevenLabs (krok 3a)
- [ ] 6. Przygotuj zdjęcie portretowe albo krótkie nagranie wideo (krok 3b)
- [ ] 7. W Claude Code: „stwórz mój awatar — moja twarz" (krok 3)
- [ ] 8. Pierwszy film: ElevenLabs robi MP3, HeyGen animuje usta (krok 5)

Kroki 5 i 6 możesz robić równolegle.

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

## Krok 1 — klucze API

Potrzebne są dwa: HeyGen (twarz i render) oraz ElevenLabs (głos).

1. **HeyGen:** [app.heygen.com/api](https://app.heygen.com/api) → **Settings → API → New Key**.
   Klucz pokazuje się **tylko raz** — skopiuj go zanim zamkniesz okno.
2. **ElevenLabs:** [elevenlabs.io](https://elevenlabs.io) → profil → **API Keys**.
3. Wpisz oba do profilu powłoki (`~/.zshrc` albo `~/.bashrc`):

   ```bash
   export HEYGEN_API_KEY="hg_..."
   export ELEVENLABS_API_KEY="sk_..."
   ```

4. `source ~/.zshrc` (albo nowe okno terminala) i **restart Claude Code** —
   agent dziedziczy zmienne z powłoki rodzica, samo `source` w innym oknie nie wystarczy.

Klucza **nie wklejaj do czatu ani do repozytorium**. `.env` jest w `.gitignore`,
ale zmienna środowiskowa jest bezpieczniejsza.

HeyGen API rozlicza się w kredytach (pay-as-you-go, bez darmowego progu) — Avatar V
to ok. 6 kredytów za minutę wygenerowanego wideo. Sprawdź stan konta na
[app.heygen.com/billing](https://app.heygen.com/billing) zanim zaczniesz.
ElevenLabs liczy znaki tekstu; `elevenlabs_tts.py --limity` pokaże plan i pozostały limit.

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
wygląd, głos, potwierdzenie promptu. **Przed wygenerowaniem awatara jest gate —
nic się nie tworzy i żaden kredyt nie schodzi, dopóki nie zatwierdzisz.**

Gdy skill zapyta o głos, powiedz mu, że **narracja idzie z ElevenLabs**. Wybierz
dowolny sensowny głos polski z katalogu HeyGen — trafi do pliku awatara jako
zapasowy i posłuży tylko wtedy, gdybyś kiedyś zrobiła film prosto z `heygen-video`.
Na Twojej drodze awatar dostaje gotowe MP3 i tego głosu nie użyje.

### Krok 3a — Twój głos w ElevenLabs

Masz do tego gotowe skrypty w skillu `dane-i-glos`. Najpierw sprawdź, co daje Twój plan
(czy ma Instant Voice Cloning):

```bash
export ELEVENLABS_API_KEY="..."
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_tts.py --limity
```

Nagraj ok. **3 minut czystej mowy po polsku**, w 3–5 plikach — bez pogłosu, bez szumu
tła, w tempie i tonie, jakich chcesz używać w filmach. Potem:

```bash
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_klon_glosu.py --sprawdz-nagrania probki/*.wav
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_klon_glosu.py "Ewa - narracja PL" probki/*.wav
export ELEVENLABS_VOICE_ID="<voice_id>"
```

Szczegóły — ile materiału, jak nagrywać, kiedy warto Professional Voice Cloning zamiast
Instant — są w `.claude/skills/dane-i-glos/references/klon_glosu.md`.

**Nagrania wzorcowe trzymaj u siebie na dysku.** To jedyny materiał, z którego można
odtworzyć głos w dowolnej usłudze; klon w chmurze jest zawsze przywiązany do platformy.
`.gitignore` w tym repozytorium już wyklucza `*.wav` i `*.m4a` — nagrania nie trafią
przypadkiem do gita.

**Klonuj wyłącznie własny głos** albo głos osoby, która wyraziła wyraźną zgodę.

### Krok 3b — Twoja twarz

| Materiał | Typ | Efekt |
|---|---|---|
| zdjęcie portretowe | `photo` | cyfrowy bliźniak z fotografii |
| krótkie nagranie wideo | `digital_twin` | najwierniejszy, oddaje też mimikę |
| sam opis słowny | `prompt` | postać wygenerowana przez AI (nie Ty) |

Skoro ma być **Twój wygląd**, wybierz `photo` albo `digital_twin`.
Wymagania dla zdjęcia: JPEG/PNG, minimum 512×512, twarz na wprost, dobre światło.

Zdjęcie trzymaj lokalnie — skill wgra je do HeyGen dopiero na Twoją wyraźną prośbę.

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

Na Twojej drodze film powstaje w dwóch krokach: ElevenLabs robi ścieżkę dźwiękową,
HeyGen animuje do niej usta awatara.

```bash
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_tts.py narracja.txt -o glos.mp3 --srt napisy.srt
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --audio glos.mp3 \
        --avatar-id "$HEYGEN_AVATAR_ID" --czekaj -o film.mp4
```

W praktyce nie wpisujesz tego ręcznie — wystarczy poprosić Claude Code:

```
zrób film ze mną o EduPlaner 2026, narracja moim głosem z ElevenLabs
```

Skill `dane-i-glos` prowadzi tę drogę od danych albo scenariusza aż po `film.mp4`
i napisy `.srt`.

### Kiedy który skill

| Chcę | Droga | Czyj głos |
|---|---|---|
| film moim głosem | `dane-i-glos`: ElevenLabs → `heygen_awatar.py --audio` | **Twój klon z ElevenLabs** |
| szybki film, głos z katalogu | skill `heygen-video` (Video Agent v3) | głos HeyGen |
| dubbing gotowego filmu | skill `heygen-translate` | Twój głos, sklonowany z tego filmu |

`heygen-video` **nie przyjmuje gotowego MP3** — zawsze czyta tekst głosem z konta HeyGen.
Dlatego Twoja główna trasa idzie przez `heygen_awatar.py --audio`, a `heygen-video`
zostaje na wypadek, gdy zależy na czasie, a nie na brzmieniu.

`heygen-translate` działa na gotowym pliku wideo, więc jest obojętne, jak powstała
ścieżka dźwiękowa — klonuje głos z filmu i dopasowuje ruch ust do nowego języka.

## Test dymny (opcjonalny, ok. 0,5 kredytu)

```bash
echo "HeyGen działa, można nagrywać." > test.txt
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_tts.py test.txt -o test.mp3
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --audio test.mp3 \
        --avatar-id "$HEYGEN_AVATAR_ID" --czekaj -o test.mp4
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
