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

## 🎭 Skille HeyGen — Twój awatar i Twoje filmy

W `.claude/skills/` stoją trzy oficjalne skille HeyGen (`heygen-avatar`, `heygen-video`,
`heygen-translate`): awatar z Twoją twarzą i głosem, produkcja filmów i dubbing na inne języki.

**Zanim zaczniesz, przeczytaj [`HEYGEN-START.md`](HEYGEN-START.md)** — klucz API, transport
(CLI/MCP), drogi klonowania głosu i wyjaśnienie, dlaczego awatara trzeba utworzyć
z Claude Code uruchomionego lokalnie, a nie z sesji webowej.

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
