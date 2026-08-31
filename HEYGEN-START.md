# HeyGen — Twój agent do filmów (Twój głos, Twoja twarz)

Ten plik to instrukcja uruchomienia. Skille HeyGen są już w repozytorium — brakuje
tylko klucza API i **uruchomienia Claude Code lokalnie**, bo sesja webowa nie ma
dostępu do serwerów HeyGen (szczegóły niżej).

## Twoja droga — lista kontrolna

Ustalenia: **złącze HeyGen (MCP, bez klucza API)** + **głos sklonowany w ElevenLabs**.

- [ ] 1. Dodaj złącze HeyGen w ustawieniach Claude i zaloguj się przez OAuth (krok 1)
- [ ] 2. **Nie ustawiaj `HEYGEN_API_KEY`** — wyłączyłby złącze (krok 1)
- [ ] 3. Utwórz awatara ze swojej twarzy + nagraj zgodę na wizerunek (krok 3b)
- [ ] 4. Wklej `Group ID` do [`AVATAR-EWA.md`](AVATAR-EWA.md) (krok 4)
- [ ] 5. Pierwszy film: ElevenLabs robi MP3, HeyGen animuje usta (krok 5)

Głos masz już sklonowany w ElevenLabs (`Ewa-głos_do skils`) i przetestowany —
krok 3a możesz pominąć, jest tam na wypadek, gdybyś kiedyś klonowała od nowa.

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

## Uwaga o sesji webowej

Kontener, w którym działa Claude Code na web, ma politykę ruchu wychodzącego
blokującą (403) wszystkie domeny HeyGen i ElevenLabs — `api.heygen.com`,
`static.heygen.ai`, `app.heygen.com`, `api.elevenlabs.io`. Dlatego **droga przez
CLI i klucz API działa wyłącznie na Twoim komputerze.**

**Uwaga — nie każde złącze to omija.** Rozstrzyga, kto nawiązuje połączenie:

| Sposób dodania | Kto łączy się z serwerem | W sesji webowej |
|---|---|---|
| Złącze w ustawieniach claude.ai | infrastruktura Claude | **działa** — tak nagraliśmy Twój głos w ElevenLabs |
| `claude mcp add` / `.mcp.json` | ten kontener | **nie działa** — 403 z polityki sieci |

Dlatego `claude mcp add --transport http heygen ...` jest poleceniem **na Twój
komputer**. Wpisane tutaj zapisze konfigurację, ale serwer i tak będzie nieosiągalny.
W sesji webowej jedyną drogą jest złącze dodane w ustawieniach konta.

## Krok 1 — złącze HeyGen (bez klucza API)

To jest droga zalecana przez samego HeyGena i lepsza dla Ciebie z trzech powodów:
**nie potrzeba klucza**, **nie potrzeba instalować CLI**, a **rozliczenie idzie
z Twojego obecnego planu HeyGen**, nie z osobnej puli kredytów API.

**W repozytorium jest już gotowa konfiguracja** — plik `.mcp.json` w katalogu
głównym wpisuje serwer `heygen`. Uruchamiając Claude Code w tym repozytorium
lokalnie, dostaniesz pytanie o zgodę na ten serwer; potwierdzasz i logujesz się
przez OAuth. Nic więcej.

Gdybyś chciała mieć HeyGena we **wszystkich** projektach, a nie tylko w tym:

```bash
claude mcp add --transport http -s user heygen https://mcp.heygen.com/mcp/v1/
```

`-s user` zapisuje do konfiguracji użytkownika, więc serwer jest widoczny wszędzie.
Bez tego przełącznika trafia tylko do bieżącego projektu.

**W przeglądarce** (claude.ai, także Claude Code na web) to samo robi się klikając:
[claude.ai/customize/connectors](https://claude.ai/customize/connectors) →
**Dodaj niestandardowe złącze** → nazwa `HeyGen`, adres `https://mcp.heygen.com/mcp/v1/`
→ **Połącz** → logowanie do HeyGen.

Po połączeniu Twoje awatary i głosy z konta HeyGen są dostępne dla agenta.

Z dokumentacji HeyGen wprost: złącze działa **na wszystkich planach**, nie kosztuje
dodatkowo ponad plan, a Twoje własne awatary i głosy są przez nie dostępne.

### ⛔ Nie ustawiaj `HEYGEN_API_KEY`

To najważniejsza rzecz na tej stronie. Skille HeyGen wybierają drogę według drabinki:

```
wtyczka → CLI (gdy jest HEYGEN_API_KEY) → MCP → CLI
```

**Ustawiony `HEYGEN_API_KEY` zwiera obwód i wyłącza wykrywanie MCP.** Skill pójdzie
wtedy przez CLI i zacznie zjadać osobne kredyty API zamiast Twojego planu.
Jeśli klucz już gdzieś ustawiłaś, usuń go:

```bash
unset HEYGEN_API_KEY
# i skasuj linijkę z ~/.zshrc, jeśli tam trafiła
```

### Kiedy klucz API mimo wszystko ma sens

Tylko jeśli chcesz uruchamiać **skrypty z `dane-i-glos`** (`heygen_awatar.py`) —
one gadają z API bezpośrednio i złącza nie widzą. Wtedy klucz bierzesz z
[panelu API HeyGen](https://app.heygen.com/home?from=&nav=API), a sprawdzasz tak:

```bash
curl -X GET "https://api.heygen.com/v3/users/me" -H "X-Api-Key: TWÓJ_KLUCZ"
```

`200` = klucz ważny; pole `billing_type` (`wallet`, `subscription`, `usage_based`)
pokaże model rozliczeń. `401` = zły klucz.

**Ale nie da się mieć obu naraz w jednej sesji.** Klucz w środowisku zawsze wygra
ze złączem. Wybierz jedno: złącze (zalecane) albo klucz do skryptów.

### Klucz ElevenLabs

Ten jest potrzebny tylko lokalnie, do skryptów `dane-i-glos`. W sesji webowej
głos robi złącze ElevenLabs, które już masz podłączone.

```bash
export ELEVENLABS_API_KEY="sk_..."    # elevenlabs.io → profil → API Keys
```

## Krok 2 — co dostajesz przez złącze

Złącze daje agentowi komplet narzędzi HeyGen. Najważniejsze dla Ciebie:

| Narzędzie | Do czego |
|---|---|
| `create_avatar` | awatar ze zdjęcia, nagrania (`digital_twin`) albo opisu |
| `create_avatar_consent` | zwraca link do nagrania zgody na wizerunek — **ważny 24 h** |
| `create_video` | film z awatara; **przyjmuje gotowe audio do synchronizacji ust** |
| `create_lipsync` | podmienia ścieżkę dźwiękową w istniejącym filmie |
| `list_avatar_groups`, `list_avatar_looks` | Twoje awatary i ich warianty |
| `create_video_translation` | dubbing na inne języki z klonowaniem głosu |

**To pierwsze i trzecie razem oznaczają, że cała Twoja droga da się przejść przez
złącza, bez instalowania czegokolwiek:** ElevenLabs robi MP3 Twoim głosem,
`create_video` bierze to MP3 i animuje do niego usta awatara.

Skrypty z `dane-i-glos` i CLI HeyGen zostają jako droga zapasowa — przydadzą się,
gdy będziesz chciała robić wszystko lokalnie albo automatem, bez rozmowy z agentem.

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

> **Rekomendacja.** Do materiałów, które mają Cię reprezentować publicznie —
> reklama EduPlaner, filmy dla dyrektorów, seria dla rodziców — najlepszy efekt
> daje **Professional Voice Cloning (PVC)** w ElevenLabs. Zacznij dziś od Instant
> Voice Cloning (IVC): masz go od ręki, sprawdzisz całą drogę na prawdziwym
> nagraniu. Kiedy będziesz wiedziała, że to działa, dograj materiał na PVC —
> `ELEVENLABS_VOICE_ID` podmieniasz na nowe i **nic więcej się nie zmienia**.

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

|  | Instant (IVC) | Professional (PVC) |
|---|---|---|
| Materiał | 1–3 minuty | 30 minut – 3 godziny |
| Czas oczekiwania | sekundy | kilka godzin |
| Jakość po polsku | dobra, słychać drobne potknięcia | najbliżej oryginału |
| Jak uruchomić | skryptem, powyżej | aplikacja webowa ElevenLabs |
| Weryfikacja tożsamości | czasem | zawsze |

PVC konfiguruje się **w aplikacji webowej**, nie skryptem — wymaga nagrania zdania
potwierdzającego tożsamość, czego nie da się przejść przez API. Gdy klon PVC już
powstanie, jego `voice_id` wpisujesz w to samo miejsce (`ELEVENLABS_VOICE_ID`)
i cała reszta drogi działa bez zmian.

Więcej — jak nagrywać, ile materiału, jakie błędy najbardziej psują klon —
w `.claude/skills/dane-i-glos/references/klon_glosu.md`.

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

> **Rekomendacja.** Skoro ma być **Twój wygląd** i ma wyglądać profesjonalnie —
> nagraj krótkie wideo i wybierz `digital_twin`. Zdjęcie daje statyczną twarz,
> nagranie oddaje też Twoją mimikę i sposób trzymania głowy, a to właśnie po tym
> widz poznaje, że to naprawdę Ty. Różnica jest wyraźnie większa niż przy głosie.

Nagranie: jedna scena, patrzysz w obiektyw, mówisz normalnym tempem, równe światło
z przodu (okno albo lampa), spokojne jednolite tło, telefon na statywie lub podpórce.
Kilkadziesiąt sekund wystarczy.

Zdjęcie (`photo`), jeśli wolisz zacząć szybciej: JPEG/PNG, minimum 512×512,
twarz na wprost, dobre światło, ostra i nieprzycięta.

Materiał trzymaj lokalnie — skill wgra go do HeyGen dopiero na Twoją wyraźną prośbę.
`.gitignore` wyklucza już `*.wav` i `*.m4a`; nagranie wideo i zdjęcie trzymaj poza
repozytorium albo dopisz je do `.gitignore`.

## Gdzie co wkleić

Jedno miejsce na wszystkie identyfikatory: **[`AVATAR-EWA.md`](AVATAR-EWA.md)**
w katalogu głównym repozytorium. Skille `heygen-video` i `heygen-translate`
czytają ten plik same — dlatego „zrób film ze mną" wystarczy za konfigurację.

### Linki do HeyGen

| Co | Gdzie | Co stamtąd bierzesz |
|---|---|---|
| **Awatary** — tworzenie ze zdjęcia lub nagrania, podgląd, edycja | [app.heygen.com/avatars](https://app.heygen.com/avatars) | **Group ID** i `look_id` → sekcja `## HeyGen` |
| **Klonowanie głosu** (gdybyś chciała też w HeyGen) | tamże, zakładka **Voices** | `voice_id` → `Voice ID` |
| **Klucz API** | [panel API](https://app.heygen.com/home?from=&nav=API) — tam też podgląd zużycia | `HEYGEN_API_KEY` → `~/.zshrc` |
| **Kredyty i plan** | [app.heygen.com/billing](https://app.heygen.com/billing) | tylko podgląd — sprawdź przed renderem |

Adresy panelu API i `/billing` są potwierdzone w dokumentacji HeyGen.
Ścieżkę do awatarów HeyGen czasem przestawia — jeśli link nie trafi, wejdź na
[app.heygen.com](https://app.heygen.com) i szukaj **Avatars** w menu bocznym.

### Tworzenie awatara ze zdjęcia — krok po kroku

1. [app.heygen.com/avatars](https://app.heygen.com/avatars) → **Create Avatar**.
2. Wybierz tworzenie z **materiału własnego** (Photo Avatar / Avatar ze zdjęcia),
   nie z opisu tekstowego — opis dałby postać wygenerowaną, nie Ciebie.
3. Wgraj **zdjęcie** (JPEG/PNG, min. 512×512, twarz na wprost, dobre światło)
   albo **krótkie nagranie wideo** — nagranie daje wierniejszy efekt, bo oddaje mimikę.
4. HeyGen poprosi o **nagranie zgody na wykorzystanie wizerunku**. To wymóg prawny,
   nie da się go pominąć ani zrobić przez API — musisz przejść przez aplikację.
5. Po przetworzeniu otwórz gotowego awatara i skopiuj **Avatar Group ID**.
6. Wklej je do `AVATAR-EWA.md` w polu `Group ID`.

Sprawdzenie z terminala, że API widzi awatara:

```bash
heygen avatar list --ownership private
```

### To samo bez klikania

Ze złączem HeyGen skill `heygen-avatar` zrobi to z poziomu rozmowy i sam zapisze
identyfikatory do pliku. Nagranie **zgody na wizerunek** i tak przechodzisz sama
w przeglądarce — ale nawet link do niej agent potrafi wygenerować
(`create_avatar_consent`). Uwaga: **ten link jest ważny 24 godziny** i tylko na
jedno udane przesłanie. Jeśli nie nagrasz w tym czasie, poproś o nowy.

### Pobranie i modyfikacja gotowego awatara

Awatara **nie pobiera się jako plik** — zostaje na koncie HeyGen, a Ty odwołujesz się
do niego przez `group_id`. Pobierasz gotowe filmy, nie samego awatara.

„Modyfikacja" oznacza w praktyce **dodanie nowego wyglądu (look) do tej samej postaci** —
inny strój, inne tło, inne kadrowanie — przy zachowaniu tożsamości:

```bash
heygen avatar looks list --group-id <group_id>     # co już masz
```

Nowy look tworzysz w aplikacji albo prosząc Claude Code: *„dodaj mojemu awatarowi
wersję w pionie"*. Skill użyje trybu z `avatar_group_id`, więc powstanie wariant
tej samej postaci, a nie nowa osoba.

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
