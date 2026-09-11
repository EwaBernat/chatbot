---
name: awatar-ewa
description: Awatar „Ewa PCTP" — filmowe wcielenie użytkowniczki (autorki EduPlaner 2026) do filmów, plansz, prezentacji i szkoleń, zawsze z jej własnym awatarem HeyGen i jej własnym głosem. Karta postaci, gotowa wycięta postać (PNG, WebM z alfą), pamięć awatara i skrypty — render nowej sceny w HeyGen (MCP, CLI, REST z głosem z ElevenLabs), wycinanie z tła, nakładanie na plansze i filmy, wstawianie do PPTX. NIGDY nie renderuje cudzym awatarem ani głosem. Użyj ZAWSZE przy „film z moim awatarem", „nagraj to moją twarzą", „Ewa niech to powie", „wstaw Ewę", „awatar w rogu", „pobierz samą postać", „wytnij mnie z tła", „intro z Ewą", „powitanie na stronę", „wersja pionowa na Reels", „Ewa PCTP", „Agent Ewa" oraz gdy wgrywa film z awatarem HeyGen. Hasła — awatar, postać, HeyGen, Video Agent, lipsync, przezroczyste tło, WebM, prezentacja z awatarem.
---

# Awatar „Ewa PCTP"

Jedna postać, jeden wygląd, jeden głos. Ewa PCTP to filmowe wcielenie użytkowniczki:
awatar HeyGen z jej twarzą, mówiący jej sklonowanym głosem. Skill prowadzi dwie rzeczy
naraz: **kto mówi i jak wygląda** (karta postaci, wycięta postać, pamięć awatara)
oraz **jak powstaje materiał** (render w HeyGen, nałożenie na planszę, slajd, film).

Karta postaci: `references/postac.md` — przeczytaj, zanim opiszesz Ewę w scenariuszu
albo zlecisz jej nową scenę. Tekst intro (wzorzec rejestru): `assets/intro_tekst.txt`.

## Zasady nadrzędne

1. **Tylko jej awatar.** Ewa powstaje wyłącznie z awatara, który użytkowniczka sama
   utworzyła w HeyGen (zgoda na wizerunek). Video Agent w HeyGen **sam dobiera postać
   z galerii**, gdy prompt tego nie przesądza — dlatego w każdym promptcie nazwij jej
   awatara wprost, a w skrypcie REST podaj `avatar_id` (skrypt bierze go z pamięci).
   Nigdy nie generuj jej twarzy innym narzędziem.
2. **Tylko jej głos.** Klon z ElevenLabs albo jej głos z konta HeyGen. Bez zapamiętanego
   głosu: napisz scenariusz, przygotuj plansze, ale **nie renderuj** i nie proponuj
   głosu zastępczego „na razie".
3. **Jeden wygląd.** Ten sam strój, fryzura, okulary i kadr z karty postaci. Nie zmieniaj
   koloru marynarki pod tło, nie kadruj inaczej, nie odbijaj lustrzanie.
4. **Marka.** Fiolet `#2D1B69`, pomarańcz `#E8450A`, Arial. Marynarka Ewy jest w odcieniu
   fioletu marki: na czystym fiolecie postać zlewa się dołem — dawaj jasny akcent.

Gdy skill nie ma zapamiętanego awatara: zrób wszystko, co nie wymaga renderu
(zamówienie, scenariusz, plansze), zatrzymaj się przed generowaniem i powiedz wprost,
czego brakuje. Każdy render kosztuje kredyty, a film z obcą twarzą idzie do kosza.

## Co skill ma od ręki (bez żadnego API)

| Plik | Co to jest | Do czego |
|---|---|---|
| `assets/ewa_pctp.png` | wycięta postać, 772×1026 px, przezroczyste tło | slajdy, plansze, miniatury, strona |
| `assets/ewa_pctp_intro.webm` | intro (13 s) z kanałem alfa, z oryginalnym dźwiękiem | wstawka wideo, czołówka szkolenia |
| `assets/intro_tekst.txt` | „Dzień dobry. Mam na imię Ewa i będę Twoją przewodniczką…" | wzorzec rejestru |
| `assets/ewa_kadr.jpg`, `assets/ewa_gesty.jpg` | kadr wzorcowy i cztery klatki gestów | wzorzec wyglądu i ruchu |

Prośba „daj mi samą postać" = wyślij `assets/ewa_pctp.png` (i `.webm`, jeśli chce ruch).
Nic nie trzeba renderować.

## Kiedy co uruchomić

| Prośba | Droga |
|---|---|
| „Pobierz / daj mi samą postać" | wyślij pliki z `assets/` |
| „Zapamiętaj mojego awatara" | **0** `scripts/skonfiguruj_awatara.py` albo `scripts/zapamietaj_awatara.py --avatar-id <id>` |
| „Ewa niech powie…", „film z moim awatarem", „powitanie", „wiadomość wideo" | **A** zamówienie → scenariusz → akceptacja → render |
| „Wytnij Ewę z tego filmu" | `scripts/wytnij_postac.py film.mp4` → `ewa.webm` + `ewa.png` |
| „Wstaw Ewę na planszę / ekran aplikacji / do filmu" | **B** `scripts/wstaw_ewe.py` |
| „Ewa w rogu prezentacji", „awatar na slajdach" | **C** `scripts/ewa_do_prezentacji.py` |
| „Intro z Ewą" | `assets/ewa_pctp_intro.webm` → `wstaw_ewe.py --tlo plansza.png` |

Zależności skryptów (jednorazowo): `pip install -r requirements.txt` (numpy, opencv,
imageio-ffmpeg, python-pptx). Systemowego ffmpeg nie trzeba.

## Etap 0 — Kim jest awatar (jednorazowo)

```bash
python3 scripts/skonfiguruj_awatara.py --pokaz
```

Jeśli skill pamięta awatara — nic więcej nie rób. Jeśli nie, trzy sposoby zdobycia
identyfikatora:

```bash
# 1. przez API (klucz: app.heygen.com → Settings → Subscriptions & API)
export HEYGEN_API_KEY="..."
python3 scripts/skonfiguruj_awatara.py                    # szuka „Ewa" wśród awatarów i głosów
python3 scripts/skonfiguruj_awatara.py --szukaj "Ewa PL"  # gdy nazwa jest inna

# 2. przez CLI HeyGen (bez klucza, po `heygen auth login`)
heygen avatar list --ownership private --limit 50
python3 scripts/zapamietaj_awatara.py --avatar-id <id> --nazwa "Ewa PCTP"

# 3. z aplikacji HeyGen: ID awatara z okna szczegółów albo adresu strony → jak w 2.
```

Pamięć: `~/.config/dane-i-glos/konfiguracja.json` (poza repozytorium, bez kluczy API).
Leży na komputerze, na którym uruchamiasz skrypty — w środowisku zdalnym znika po sesji.
Przy kilku kandydatach skrypt **nie zgaduje** — wypisuje ich i czeka na `--awatar-id`.
`heygen voice list` i głos HeyGen są potrzebne tylko wtedy, gdy Ewa ma mówić głosem
z konta HeyGen; z klonem w ElevenLabs wystarczy sam `avatar_id`.

## Droga A — nowa scena: zamówienie → scenariusz → akceptacja → render

**Zamówienie** (jednym pytaniem, nie ankietą): do kogo, po co, jak długo (30 s ≈ 75 słów,
60 s ≈ 150, 90 s ≈ 225), gdzie trafi (poziom 1920×1080, pion 1080×1920, róg prezentacji),
co ma się stać po obejrzeniu. Bez odpowiedzi przyjmij 60 s, poziom, ton rzeczowy — i powiedz,
co przyjęłaś.

**Scenariusz** według `references/scenariusz.md`: 150 słów na minutę, liczby i skróty
słownie, jedno zdanie = jedna myśl (do 20 słów), pauzy nową linią, haczyk → sedno →
wezwanie. Pisz w rejestrze intro: imię, rola („przewodniczka po systemie"), zaproszenie,
temat. **Pokaż scenariusz do akceptacji przed renderem** — poprawka tekstu jest darmowa,
render kosztuje kredyty.

**Render** — trzy transporty, wybierz po cichu i nie narracjonuj wyboru:

| | Złącze MCP HeyGen (Video Agent) | CLI `heygen` | Skrypt REST `scripts/heygen_awatar.py` |
|---|---|---|---|
| Sterowanie | prompt (`references/prompt-agenta.md`) | `heygen video-agent create` | parametry wiersza poleceń |
| Wybór awatara | **nazwać w promptcie** | `--avatar-id` | z pamięci, bez pytania |
| Głos z ElevenLabs | nie | nie | tak (`--audio glos.mp3`) |
| Kontrola kadru, tła | pośrednia | `--orientation` | pełna (`--styl`, `--tlo`, wymiary) |
| Kiedy | scena, montaż, „zrób ładny materiał" | u siebie, bez klucza | stały format, jej głos z ElevenLabs |

Złącze MCP: `claude mcp add --transport http -s user heygen https://mcp.heygen.com/mcp/v1/`,
potem logowanie OAuth (`references/mcp.md`). CLI: `curl -fsSL https://static.heygen.ai/cli/install.sh | bash`,
`heygen auth login`; `--wait --timeout 45m`, bo domyślne 20 minut bywa za krótkie
(`references/lokalnie.md`). Skrypt REST woła API v2, które HeyGen uznaje za przestarzałe —
to droga zapasowa, ale jedyna z głosem z ElevenLabs:

```bash
python3 scripts/elevenlabs_tts.py narracja.txt -o glos.mp3 --srt napisy.srt   # jej klon głosu
python3 scripts/heygen_awatar.py --audio glos.mp3 --tlo "#00FF00" --czekaj -o ewa_zielona.mp4
python3 scripts/heygen_awatar.py narracja.txt --czekaj -o film.mp4             # głos z konta HeyGen
```

**Tło renderu**: gdy Ewa ma potem trafić na planszę, slajd albo do kompozycji, zamów
**jednolite zielone tło** (`--tlo "#00FF00"`; w promptcie: „tło jednolite, czysta zieleń
#00FF00, bez gradientu") albo eksport WebM z przezroczystością. Fiolet marki jako tło
wyklucza późniejsze wycięcie — marynarka Ewy ma ten sam odcień.

Sieć: w środowiskach zdalnych `api.heygen.com` i `api.elevenlabs.io` bywają zablokowane
(`403` z proxy — to blokada, nie zły klucz). Złącza MCP działają mimo tego. Zrób wtedy
wszystko, co nie wymaga API, a render zostaw na komputer użytkowniczki.

## Wycinanie — sama postać z klipu

```bash
python3 scripts/wytnij_postac.py film.mp4                              # auto: szachownica albo kolor
python3 scripts/wytnij_postac.py film.mp4 --podglad podglad.jpg        # sprawdź maskę przed renderem
python3 scripts/wytnij_postac.py ewa_zielona.mp4 --tlo "#00FF00" --webm ewa.webm --png ewa.png
python3 scripts/wytnij_postac.py film.mp4 --png ewa.png --czas 6 --przytnij   # sam kadr, 2 s
```

Rozpoznaje szachownicę z podglądu HeyGen (eksport „transparent" spłaszczony do MP4),
jednolity kolor i prawdziwą alfę (wtedy tylko przepakowuje). Wyjścia: `--webm` (VP9 + alfa),
`--mov` (ProRes 4444, duży), `--png`, `--sekwencja`. Szczegóły i strojenie progów:
`references/produkcja.md`.

## Droga B — Ewa w filmie (plansza, ekran aplikacji, kolor marki)

```bash
python3 scripts/wstaw_ewe.py ewa.webm --sprawdz                                   # czy klip ma alfę
python3 scripts/wstaw_ewe.py ewa.webm -o film.mp4                                 # pełny kadr, fiolet marki
python3 scripts/wstaw_ewe.py ewa.webm --tlo plansza.png --uklad rog -o film.mp4    # Ewa mała w rogu
python3 scripts/wstaw_ewe.py ewa.webm --tlo plansza.png --uklad rog --kolo         # w kółku (webinar)
python3 scripts/wstaw_ewe.py ewa.webm --tlo ekran_aplikacji.mp4 --uklad lewa       # Ewa z lewej, treść z prawej
python3 scripts/wstaw_ewe.py ewa.webm --pion --uklad pelny                         # 1080×1920 pod Reels
python3 scripts/wstaw_ewe.py ewa.webm --audio glos.mp3 --napisy napisy.srt         # własny dźwięk + napisy
```

Układy: `pelny` (cała wysokość, środek), `rog` (42 %, prawy dolny), `lewa` / `prawa`
(90 %, przy krawędzi). Bez alfy w klipie: `--klucz "#00FF00"`. Powitanie i pożegnanie —
Ewa duża; omawianie ekranów — Ewa mała w rogu, żeby nie zasłaniać treści.

## Droga C — Ewa w prezentacji (PPTX)

```bash
python3 scripts/ewa_do_prezentacji.py szkolenie.pptx --obraz assets/ewa_pctp.png --slajdy 1,8 --pozycja prawa
python3 scripts/wstaw_ewe.py ewa.webm --tlo "#2D1B69" -o ewa_wstep.mp4      # PowerPoint nie gra wideo z alfą
python3 scripts/ewa_do_prezentacji.py szkolenie.pptx --klip 1=ewa_wstep.mp4 --klip 9=ewa_final.mp4 --pozycja srodek
```

Pozycje: `rog` (6 cm), `lewa` / `prawa` (11 cm), `srodek` (14 cm, dół slajdu). Klip
startuje po kliknięciu; automatyczny start ustawia się w PowerPoint (Odtwarzanie → Start:
Automatycznie) — powiedz to przy oddawaniu pliku.

## Remotion

W repozytorium `chatbot` szablon filmu z danych (`dane-i-glos/assets/remotion`) ma komponent
`Awatar`; Ewę dodaje się tam przełącznikiem `--awatar ewa.webm --awatar-uklad rog` przy
składaniu projektu. Ten pakiet nie zawiera szablonu — potrzebuje repozytorium.

## Oddawanie pracy

Wyślij pliki, nie ścieżki: film MP4 albo prezentację PPTX, a przy wycinaniu `ewa.png`
i `ewa.webm`. Podaj czas trwania, układ i to, co się zużyło (kredyty HeyGen, znaki
ElevenLabs). Bez identyfikatorów sesji i surowych odpowiedzi API w rozmowie. Materiał,
w którym Ewa mówi cudzym głosem albo ma cudzą twarz, nie istnieje — nie oddawaj go.

## Materiały

- `references/postac.md` — karta postaci: wygląd, strój, kadr, gest, ton, tekst intro
- `references/scenariusz.md` — zasady tekstu pod awatara
- `references/prompt-agenta.md` — szablon promptu do Video Agenta (awatar nazwany wprost)
- `references/mcp.md` — podłączenie złącza MCP HeyGen i diagnostyka
- `references/lokalnie.md` — uruchomienie na własnym komputerze krok po kroku (CLI)
- `references/produkcja.md` — eksport z HeyGen, kluczowanie, alfa, prezentacje, kody błędów
- `scripts/` — `skonfiguruj_awatara.py`, `zapamietaj_awatara.py`, `heygen_awatar.py`,
  `elevenlabs_tts.py`, `wytnij_postac.py`, `wstaw_ewe.py`, `ewa_do_prezentacji.py`
- `assets/` — gotowa postać (PNG, WebM z alfą), tekst intro, kadry wzorcowe
