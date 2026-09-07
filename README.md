# 💬 Chatbot template

A simple Streamlit app that shows how to build a chatbot using OpenAI's GPT-3.5.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-template.streamlit.app/)

### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```

---

## 🎙️ Skill `dane-i-glos` — dane zamienione w nagranie

W `.claude/skills/dane-i-glos/` znajduje się skill, który prowadzi jedną drogę:
**dane → liczby → scenariusz → głos → twarz**.

Ścieżka domyślna: sklonowany głos w ElevenLabs steruje ustami awatara HeyGen, więc to samo
MP3 jest i nagraniem audio, i ścieżką dźwiękową filmu.

0. **Twój głos** — jednorazowo, potem tylko z niego korzystasz:

   ```bash
   export ELEVENLABS_API_KEY="..."
   python3 .claude/skills/dane-i-glos/scripts/elevenlabs_klon_glosu.py --sprawdz-nagrania probki/*.wav
   python3 .claude/skills/dane-i-glos/scripts/elevenlabs_klon_glosu.py "Ewa - narracja PL" probki/*.wav
   export ELEVENLABS_VOICE_ID="<voice_id>"
   ```

   Potrzeba ok. 3 minut czystego nagrania po polsku, w 3–5 plikach. Zasady nagrywania:
   `references/klon_glosu.md`. `--sprawdz-nagrania` niczego nie wysyła.

1. **Profil danych** — rzetelne liczby z pliku, żeby narracja nic nie zmyśliła:

   ```bash
   python3 .claude/skills/dane-i-glos/scripts/dane_do_narracji.py dane.xlsx --grupuj klasa --agreguj wynik
   ```

   Obsługuje `.csv`, `.tsv`, `.xlsx`, `.json`, `.jsonl`; rozumie polski zapis liczb
   (`87,5%`, `1 240 zł`) i polskie formaty dat.

2. **Scenariusz lektorski** — Claude pisze go według `references/narracja.md`
   (tempo 150 słów/min, liczby rozpisane słowami, zdania do 20 słów).

3. **Głos z ElevenLabs**:

   ```bash
   export ELEVENLABS_API_KEY="..."
   python3 .claude/skills/dane-i-glos/scripts/elevenlabs_tts.py narracja.txt -o raport.mp3 --srt napisy.srt
   ```

   `--glosy` wypisuje głosy z konta, `--suchy-bieg` liczy znaki bez zużywania limitu.

4. **Film z wykresami (Remotion)** — gdy materiał ma pokazywać liczby, nie twarz:

   ```bash
   python3 .claude/skills/dane-i-glos/scripts/dane_do_narracji.py dane.csv \
           --grupuj klasa --agreguj frekwencja_proc --json > profil.json
   python3 .claude/skills/dane-i-glos/scripts/przygotuj_remotion.py ~/moj-film \
           --profil profil.json --narracja narracja.txt --audio raport.mp3 --napisy napisy.srt
   cd ~/moj-film && npm install && npx remotion render RaportWideo out/film.mp4
   ```

   Granice scen są dosuwane do końców napisów, więc obraz zmienia się między zdaniami.
   Długość filmu bierze się z długości MP3. Paleta przeszła walidator dostępności —
   szczegóły w `assets/remotion/README.md`.

5. **Twarz i Twój głos z HeyGen** — film z awatarem:

   ```bash
   export HEYGEN_API_KEY="..."
   python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --awatary
   python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --glosy --jezyk polish
   python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --audio raport.mp3 \
           --avatar-id <id> --tlo "#2D1B69" --czekaj -o film.mp4
   ```

   `--audio` karmi awatara MP3 z punktu 3, więc awatar mówi **Twoim** sklonowanym głosem —
   to droga domyślna. Zapasowo `--voice-id` każe HeyGen przeczytać scenariusz głosem
   z konta HeyGen (gdy nie masz jeszcze klonu w ElevenLabs).

---

## 🧑‍🏫 Skill `awatar-ewa-pctp` — postać Ewy do filmów i prezentacji

W `.claude/skills/awatar-ewa-pctp/` jest postać **Ewa PCTP** — awatar HeyGen autorki,
gotowy do wywołania w filmach i prezentacjach, zawsze z jej własnym głosem z `dane-i-glos`.

Skill ma od ręki wyciętą postać (bez API): `assets/ewa_pctp.png` (przezroczyste tło)
i `assets/ewa_pctp_intro.webm` (intro z kanałem alfa). Kartę postaci — wygląd, kadr,
strój, ton — opisuje `references/postac.md`.

```bash
pip install -r .claude/skills/awatar-ewa-pctp/requirements.txt
S=.claude/skills/awatar-ewa-pctp/scripts

# sama postać z dowolnego klipu HeyGen (szachownica, zielone tło albo alfa)
python3 $S/wytnij_postac.py intro.mp4 --webm ewa.webm --png ewa.png --czas 6

# Ewa w filmie: na kolorze marki, planszy albo ekranie aplikacji
python3 $S/wstaw_ewe.py ewa.webm -o film.mp4
python3 $S/wstaw_ewe.py ewa.webm --tlo plansza.png --uklad rog --kolo -o film.mp4

# Ewa w prezentacji: obraz na slajdach albo mówiący klip
python3 $S/ewa_do_prezentacji.py szkolenie.pptx --obraz ewa.png --slajdy 1,8 --pozycja prawa
python3 $S/ewa_do_prezentacji.py szkolenie.pptx --klip 1=ewa_wstep.mp4 --pozycja srodek

# Ewa w filmie Remotion z wykresami (tylko na życzenie)
python3 .claude/skills/dane-i-glos/scripts/przygotuj_remotion.py ~/moj-film --profil profil.json \
        --narracja narracja.txt --audio glos.mp3 --awatar ewa.webm --awatar-uklad rog

# pamięć awatara HeyGen (ta sama co głos ElevenLabs, poza repozytorium)
python3 $S/zapamietaj_awatara.py --avatar-id <id> --nazwa "Ewa PCTP"
```

Pakiet do wgrania na claude.ai (jeden samodzielny Skill „awatar-ewa" z postacią, renderem
i skryptami): `python3 .claude/skills/awatar-ewa-pctp/scripts/spakuj_skill.py ~/pakiety`
daje `awatar-ewa.skill` (ok. 5 MB; `--bez-webm` ok. 1,5 MB). Wgranie: Ustawienia →
Możliwości → Skills → Prześlij plik.

Podział ról: `awatar-ewa` **renderuje** film, w którym Ewa mówi (MCP HeyGen, CLI, REST);
`awatar-ewa-pctp` trzyma **postać** i wstawia ją tam, gdzie ma się pojawić. Oba piszą do
jednej pamięci awatara. Uruchomienie u siebie krok po kroku: `.claude/skills/awatar-ewa/references/lokalnie.md`.

Nowa scena z Ewą głosem z ElevenLabs: scenariusz → `elevenlabs_tts.py` (jej klon głosu) →
`heygen_awatar.py --audio glos.mp3 --tlo "#00FF00"` → `wytnij_postac.py --tlo "#00FF00"` →
`wstaw_ewe.py` albo `ewa_do_prezentacji.py`. Zielone tło, bo fiolet marki wyciąłby
marynarkę Ewy.

### Złącze ElevenLabs

`.mcp.json` w katalogu głównym podłącza serwer MCP ElevenLabs do sesji Claude Code
w tym repozytorium. Wymaga tylko klucza w środowisku:

```bash
export ELEVENLABS_API_KEY="sk_..."   # elevenlabs.io → profil → API Keys (uprawnienie text_to_speech)
```

W aplikacji claude.ai to samo złącze włącza się w **Ustawienia → Złącza → ElevenLabs**,
a potem w panelu złączy danego czatu.

Złącze **HyperFrames by HeyGen** buduje filmy z HTML i **nie sięga po Twoje awatary** —
do awatara i sklonowanego głosu służy `HEYGEN_API_KEY` oraz `scripts/heygen_awatar.py`.

Klucz API trzymaj wyłącznie w zmiennej środowiskowej — `.gitignore` blokuje `.env`,
a wygenerowane `*.mp3`, `*.srt` i `narracja*.txt` nie trafiają do repozytorium.

---

## 🎬 Skill `awatar-ewa` — film, w którym mówi Twój awatar

W `.claude/skills/awatar-ewa/` leży skill do materiałów z awatarem HeyGen:
**zamówienie → scenariusz → akceptacja → render → plik**. Twarz i głos ustalasz raz;
skill nigdy nie renderuje filmu cudzym awatarem ani cudzym głosem.

1. **Kim jest awatar** — jednorazowo, potem tylko z tego korzystasz:

   ```bash
   export HEYGEN_API_KEY="..."          # app.heygen.com → Settings → Subscriptions & API
   python3 .claude/skills/awatar-ewa/scripts/skonfiguruj_awatara.py            # szuka „Ewa"
   python3 .claude/skills/awatar-ewa/scripts/skonfiguruj_awatara.py --pokaz
   ```

   Skrypt zapisuje `avatar_id` i `voice_id` w tej samej pamięci co `dane-i-glos`
   (`~/.config/dane-i-glos/konfiguracja.json`, poza repozytorium). Przy kilku pasujących
   awatarach nie zgaduje — wypisuje kandydatów i czeka na `--awatar-id`.

2. **Złącze MCP HeyGen** — Video Agent pisze scenariusz, składa sceny i renderuje:

   ```bash
   claude mcp add --transport http -s user heygen https://mcp.heygen.com/mcp/v1/
   ```

   Potem `/mcp` w Claude Code i logowanie OAuth. Prompt zawsze nazywa awatara po imieniu —
   bez tego agent dobiera postać z galerii. Szablon: `references/prompt-agenta.md`,
   podłączenie i diagnostyka: `references/mcp.md`.

3. **Render przez API** — gdy potrzebujesz kadru, tła i formatu co do piksela:

   ```bash
   python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py narracja.txt --czekaj -o film.mp4
   ```

   Awatar i głos idą z pamięci z punktu 1. Materiał o liczbach prowadzi skill `dane-i-glos`
   (profil danych → narracja → głos → awatar).
