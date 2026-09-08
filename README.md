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

## 📋 Czynności nauczycieli w ramach wynagrodzenia

W `dokumenty/` znajduje się wykaz czynności nauczycieli realizowanych w ramach czasu pracy
i ustalonego wynagrodzenia (art. 42 ust. 2 Karty Nauczyciela), przygotowany dla PCTP Koszalin
na rok szkolny 2026/2027:

- `czynnosci-nauczycieli-w-ramach-wynagrodzenia.docx` — wersja Word do druku i podpisu
  (strona tytułowa z logo, 7 rozdziałów, wzór przydziału czynności i lista kontrolna specjalisty),
- `czynnosci-nauczycieli-w-ramach-wynagrodzenia.pdf` — ta sama treść jako PDF,
- `czynnosci-nauczycieli-w-ramach-wynagrodzenia.md` — wersja tekstowa do czytania w GitHubie
  i do wklejenia do bazy wiedzy chatbota,
- `generuj_czynnosci_docx.js` — generator pliku Word (instrukcja w nagłówku skryptu).

Ten wykaz jest napisany dla reżimu Karty Nauczyciela (pensum, art. 42) i służy jako odniesienie.

### Szkoła specjalna — nauczyciele na Kodeksie pracy, 6 godzin dziennie

Tabela porównawcza czynności **nauczyciela edukacji wczesnoszkolnej (kl. I–III)** i **nauczyciela
przedmiotów (kl. IV–VIII)** w szkole podstawowej specjalnej, dla nauczycieli zatrudnionych na podstawie
Kodeksu pracy w wymiarze 6 godzin dziennie (bez pensum i godzin ponadwymiarowych z Karty Nauczyciela):

- `czynnosci-nauczycieli-szkoly-specjalnej.docx` / `.pdf` — A4 poziomo: ramy zatrudnienia,
  62 czynności w 11 obszarach z oznaczeniem, kto je wykonuje, przykładowy rozkład 6-godzinnego dnia
  i kalendarz roku szkolnego,
- `czynnosci-nauczycieli-szkoly-specjalnej.md` — ta sama treść w Markdownie,
- `generuj_tabela_szkola_specjalna.js` — generator obu plików (`node ... logo.png plik.docx plik.md`).

### Druk „Zakres czynności i obowiązków” — nauczyciel edukacji wczesnoszkolnej

Gotowy do podpisu druk dla konkretnych nauczycieli (Kodeks pracy, 30 godzin tygodniowo): dane
stanowiska, 47 obowiązków z podstawą prawną w tabeli, miejsce na czynności przydzielone indywidualnie,
zakres odpowiedzialności, oświadczenie i podpisy. Jeden plik zawiera osobny egzemplarz dla każdej osoby.

- `druk-zakres-czynnosci-edukacja-wczesnoszkolna.docx` / `.pdf` — egzemplarze dla Karoliny P. i Karoliny B.,
- `generuj_druk_edukacja_wczesnoszkolna.js` — generator; nazwiska podaje się jako argumenty:
  `node dokumenty/generuj_druk_edukacja_wczesnoszkolna.js logo.png plik.docx "Imię Nazwisko" "Imię Nazwisko"`.

### Druk „Zakres czynności i obowiązków” — język angielski, informatyka, wychowanie fizyczne

Ten sam układ druku dla nauczyciela przedmiotów w szkole specjalnej (Kodeks pracy, 30 godzin
tygodniowo): obowiązki wspólne plus osobne bloki dla języka obcego (w tym egzamin ósmoklasisty),
pracowni komputerowej i bezpieczeństwa cyfrowego oraz wychowania fizycznego (BHP na zajęciach
ruchowych, zwolnienia lekarskie, ocenianie wysiłku).

- `druk-zakres-czynnosci-angielski-informatyka-wf.docx` / `.pdf` — egzemplarz dla Kacpra K.,
- `generuj_druk_angielski_informatyka_wf.js` — generator; nazwiska jako argumenty, jak wyżej.

### Druk „Zakres czynności i obowiązków” — matematyka, przyroda, biologia, wychowawstwo, rewalidacja

Druk dla nauczycielki przedmiotów matematyczno-przyrodniczych, która jest wychowawczynią klasy VI
i prowadzi zajęcia rewalidacyjne (Kodeks pracy, 30 godzin tygodniowo): obowiązki wspólne oraz bloki
dla matematyki, przyrody i biologii (BHP doświadczeń), zajęć rewalidacyjnych (program, dziennik,
60-minutowa godzina) i wychowawstwa (koordynacja IPET, ocena zachowania, dokumentacja oddziału).

- `druk-zakres-czynnosci-matematyka-przyroda-biologia.docx` / `.pdf` — egzemplarz dla Agaty
  (nazwisko do uzupełnienia),
- `generuj_druk_matematyka_przyroda_biologia.js` — generator; nazwiska jako argumenty, jak wyżej.

### Druk „Zakres czynności i obowiązków” — matematyka i wychowawstwo klasy VI c

Druk dla drugiej nauczycielki matematyki, wychowawczyni klasy VI c (Kodeks pracy, pełny etat
30 godzin tygodniowo): obowiązki wspólne, blok matematyki (w tym pracownia i egzamin ósmoklasisty)
oraz blok wychowawstwa (koordynacja IPET i WOPF, ocena zachowania, dokumentacja oddziału).

- `druk-zakres-czynnosci-matematyka-wychowawstwo-6c.docx` / `.pdf` — egzemplarz dla Moniki
  (nazwisko do uzupełnienia),
- `generuj_druk_matematyka_wychowawstwo.js` — generator; nazwiska jako argumenty, jak wyżej.

### Druk „Zakres czynności i obowiązków” — język polski, wychowawstwo klasy IV, rewalidacja logopedyczna

Druk dla nauczyciela języka polskiego, wychowawcy klasy IV, prowadzącego zajęcia rewalidacyjne
o charakterze logopedycznym (Kodeks pracy, 30 godzin tygodniowo): obowiązki wspólne oraz bloki
języka polskiego (czytanie ze zrozumieniem, lektury dostosowane, egzamin ósmoklasisty), logopedii
(diagnoza, program terapii, AAC, higiena zajęć, dziennik) i wychowawstwa klasy IV (adaptacja po
klasie III, koordynacja IPET i WOPF, ocena zachowania).

- `druk-zakres-czynnosci-jezyk-polski-wychowawstwo-4-logopedia.docx` / `.pdf` — egzemplarz
  z pustym polem na imię i nazwisko,
- `generuj_druk_jezyk_polski_logopedia.js` — generator; nazwiska jako argumenty, jak wyżej.

### Druk „Zakres czynności i obowiązków” — pedagog szkolny i nauczyciel współorganizujący (klasa III)

Druk dla osoby łączącej dwie role w jednym etacie (Kodeks pracy, 30 godzin tygodniowo z podziałem
godzin między role): pedagog szkolny (diagnoza i pomoc psychologiczno-pedagogiczna, profilaktyka,
interwencja, standardy ochrony małoletnich, Niebieska Karta, dziennik pedagoga) oraz nauczyciel
współorganizujący kształcenie w oddziale klasy III (zadania z § 7 rozporządzenia o kształceniu
specjalnym, wsparcie uczniów z orzeczeniem, udział w IPET i WOPF).

- `druk-zakres-czynnosci-pedagog-wspolorganizujacy-3.docx` / `.pdf` — egzemplarz dla Sary
  (nazwisko do uzupełnienia),
- `generuj_druk_pedagog_wspolorganizujacy.js` — generator; nazwiska jako argumenty, jak wyżej.

Wykaz ma charakter pomocniczy: przed wdrożeniem trzeba go dopasować do statutu placówki,
regulaminu wynagradzania organu prowadzącego i aktualnego tekstu jednolitego ustawy.
