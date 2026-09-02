# Film szkoleniowy · Nowa podstawa programowa wychowania przedszkolnego

Projekt Remotion na film ok. **9 minut 40 sekund**, 1920×1080, 30 kl./s.
Marka PCTP, znak EduPlaner 2026, tło ilustrowanej sali przedszkolnej,
miejsce na awatara i napisy.

## Co już jest

| Element | Stan |
|---|---|
| Scenariusz lektorski (18 scen, 1363 słowa) | `public/narracja.txt` |
| Montaż — czasy scen liczone ze scenariusza | `public/film.json` |
| Wszystkie plansze i animacje | `src/sceny/Sceny.tsx` |
| Tło sali, znak PCTP, ikony obszarów, awatar, napisy | `src/elementy/` |
| Powitanie — awatar mówi własnym dźwiękiem | `src/sceny/Powitanie.tsx` |
| Zdjęcie tła z awatara (przezroczystość) | `narzedzia/wytnij_tlo.py` |
| Podgląd pierwszych 40 sekund | `out/podglad-40s.mp4` |
| Klatki kontrolne z całego filmu | `podglad/` |

## Czego brakuje i skąd to wziąć

**1. Narracja Twoim głosem** → `public/narracja.mp3` + `public/napisy.srt`

Głos jest na Twoim koncie ElevenLabs — klon **„Ewa‑głos_do skils”**
(`jq4ZUryuBeDqmtkKtBZ4`), opisany jako pasujący do szkoleń i wykładów.
Masz tam też klony `Ewa1` i `Ewa2`, gdybyś wolała inne brzmienie.

Koszt całej narracji: **ok. 10 400 kredytów, czyli około 1,72 USD** (wycena
z ElevenLabs, bez generowania). Poprawka scenariusza i przegenerowanie
kosztują tyle samo, więc tekst warto przeczytać przed pierwszym uruchomieniem.

Na własnym komputerze:

```bash
export ELEVENLABS_API_KEY="..."
python3 ~/.claude/skills/dane-i-glos/scripts/elevenlabs_tts.py \
        public/narracja.txt -o public/narracja.mp3 \
        --voice-id jq4ZUryuBeDqmtkKtBZ4 --srt public/napisy.srt
python3 buduj_sceny.py --audio public/narracja.mp3   # dosuwa sceny do nagrania
```

**2. Awatar** → `public/awatar.webm`

Nagranie z HeyGen (`public/awatar-intro.mp4`) trzeba najpierw pozbawić tła:

```bash
python3 narzedzia/wytnij_tlo.py public/awatar-intro.mp4 public/awatar.webm
```

Skrypt zapisuje VP9 z kanałem alfa — Chromium, a więc i Remotion, odtwarza
go z przezroczystością, dzięki czemu postać stoi wprost na tle sali,
bez ramki i bez koła.

### Dlaczego to wymaga osobnego kroku

HeyGen wyeksportował awatara „z przezroczystością", ale do kodeka, który alfy
nie niesie (H.264, yuv420p). Przezroczystość jest w tym pliku **wypalona
w pikselach** jako szara szachownica. Zwykły klucz luminancji jej nie zdejmie:
szachownica ma luminancję ok. 250, a biała bluzka 251 — klucz wyciąłby bluzkę
razem z tłem.

Dlatego skrypt rozpoznaje tło inaczej. Piksel jest tłem, gdy jest jasny
i neutralny kolorystycznie **oraz** należy do obszaru stykającego się
z krawędzią kadru. Bluzka jest zamknięta marynarką, więc krawędzi nie dotyka
i zostaje nietknięta — biała, dokładnie taka jak w oryginale. Drobne wyspy
po kompresji odsiewa próg wielkości obszaru.

**Prościej będzie następnym razem:** jeśli w HeyGen wyeksportujesz awatara
do WebM/VP9 z alfą albo do MOV/ProRes 4444, przezroczystość przyjdzie gotowa
i ten krok odpada. Można też wyeksportować na jednolitym, nasyconym tle
(np. zieleni), które kluczuje się bez ryzyka dla bluzki.

### Gdzie awatar występuje w filmie

| Miejsce | Co widać | Dźwięk | Usta |
|---|---|---|---|
| Powitanie 0:00–0:13 | pełna sylwetka po prawej | własny dźwięk z `awatar.webm` | **zgadzają się** |
| Sceny 1–18 i plansza końcowa | kółeczko w prawym dolnym rogu | lektor z `narracja.mp3` | zależy od trybu (niżej) |

### Kółeczko ma dwa tryby i samo wybiera właściwy

**Tryb mówiący** — gdy w `public/` leży `awatar-lektor.mp4` (albo `.webm`):
postać w kółeczku mówi, a usta idą za lektorem, bo to jedno i to samo nagranie.

**Tryb nieruchomy** — gdy tego pliku nie ma: w kółeczku jest nieruchoma
sylwetka z `portret-alfa.png`, z bardzo wolnym najazdem, żeby kadr nie wyglądał
na zacięty. Tak jest teraz.

Powitalnego klipu (`awatar.webm`) w kółeczku **nie puszczamy w pętli**. Trwa
13 sekund i powstał do innego tekstu; pod jedenastominutową narracją poruszałby
ustami do słów, których nie ma — widz wychwytuje to natychmiast. Lepsza
nieruchoma postać niż postać kłamiąca ustami.

### Jak włączyć tryb mówiący

Wymaga HeyGena, a ten jest **niedostępny z tego środowiska** — polityka sieci
odrzuca połączenie do `api.heygen.com` (403 na CONNECT w bramie). Nie jest to
kwestia klucza: wyjście jest zamknięte. Podłączony konektor HyperFrames buduje
filmy z HTML i nie ma dostępu do Twoich awatarów ani sklonowanego głosu.

Na własnym komputerze, gdzie HeyGen jest osiągalny:

```bash
export HEYGEN_API_KEY="..."
python3 ~/.claude/skills/dane-i-glos/scripts/heygen_awatar.py --awatary

python3 ~/.claude/skills/dane-i-glos/scripts/heygen_awatar.py \
        --audio public/narracja.mp3 \
        --avatar-id <twoje_id> --styl normal --tlo "#2D1B69" \
        --czekaj -o public/awatar-lektor.mp4
```

**`--styl normal`, nie `circle`** — to ważne. Kółeczko wycina już
`src/elementy/Awatar.tsx`, a kadr liczy z wymiarów sylwetki zmierzonych
z `awatar.webm` (czubek głowy y=62, środek głowy x=963). Gotowy kadr kołowy
z HeyGena wszedłby w kółeczko drugi raz i te wymiary przestałyby pasować.
`--styl normal` daje ten sam kadr pełnoekranowy co nagranie powitalne, więc
pozycjonowanie zostaje poprawne.

Gdyby HeyGen mimo to skadrował inaczej, korekta to trzy stałe na górze
`AwatarRog`: `GLOWA_GORA`, `GLOWA_DOL`, `GLOWA_SRODEK_X`. Zmierzyć je można
tym samym sposobem, co poprzednio — z kanału alfa albo z klatki nagrania.

`--audio` jest tu kluczowe: awatar dostaje **gotowe** `narracja.mp3`, więc
mówi Twoim głosem z ElevenLabs i rusza ustami dokładnie do tego dźwięku.
Nagranie trwa 11 minut i 43 sekundy — sprawdź w HeyGenie limit długości
swojego planu, zanim uruchomisz render.

Plik wrzuć do `public/` i przerenderuj film. **Kod nie wymaga żadnej zmiany** —
`src/Root.tsx` sam wykrywa nazwę i przełącza kółeczko w tryb mówiący.

### Rozmiar i miejsce kółeczka

Stałe `SREDNICA`, `OBRAMOWANIE` i pozycja `right`/`bottom` w
`src/elementy/Awatar.tsx`. Kadr portretowy liczy się z rzeczywistych wymiarów
sylwetki zmierzonych z kanału alfa (czubek głowy y=62, broda y≈400, środek
głowy x=963), więc zmiana średnicy nie psuje kadrowania. Napisy i plansze
pełnoekranowe mają prawy margines 560 px, żeby tekst nie wchodził na kółeczko.

Klatkę do `portret-alfa.png` wybrano tak, żeby usta były zamknięte, a wyraz
twarzy ciepły — to klatka 144 (5,76 s):

```bash
ffmpeg -c:v libvpx-vp9 -i public/awatar.webm \
       -vf "select=eq(n\,144)" -vsync 0 -frames:v 1 \
       -pix_fmt rgba public/portret-alfa.png
```

## Render

```bash
npm install
npm start                       # studio — podgląd i przewijanie scena po scenie
npm run build                   # pełny film do out/film-podstawa-2026.mp4
```

W kontenerze bez zwykłej przeglądarki dodaj wskazanie na headless shell:

```bash
npx remotion render src/index.ts Film out/film.mp4 \
    --browser-executable /opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
```

Pełny render (21 486 klatek — 13,04 s powitania plus 703,16 s narracji) trwa
w tym środowisku ponad godzinę.
Podgląd fragmentu: dodaj `--frames=0-1200`.

## Jak to jest zbudowane

**Scenariusz jest źródłem czasów.** `buduj_sceny.py` czyta `public/narracja.txt`,
liczy słowa w każdej scenie (polski lektor — 150 słów na minutę), dokłada pauzę
na przejście i zapisuje montaż do `public/film.json`. Poprawka w tekście sama
przelicza długości scen — nie trzeba ręcznie pilnować, żeby obraz zmieniał się
razem ze zdaniem. Gdy pojawi się nagranie, `--audio` przeskalowuje wszystko do
jego rzeczywistej długości.

**Kolory obszarów to tinty jednego odcienia**, nie tęcza. Zieleń, bursztyn
i czerwień są w tym ekosystemie zarezerwowane dla poziomów realizacji celu
(osiągnięty / częściowo / brak) — użycie ich jako kolorów obszarów myliłoby
znaczenie.

**Tło sali jest rysowane wektorowo**, nie zdjęciem: brak problemu z licencją,
ostrość w każdej rozdzielczości i pełna kontrola nad tym, żeby nie walczyło
z tekstem. Woal nad tłem trzyma kontrast napisów niezależnie od tego, co pod nim.

## Uwaga merytoryczna

Treść opiera się na rozporządzeniu Ministra Edukacji z 11 marca 2026 r.
(Dz.U. 2026 poz. 378) i na potwierdzonym podziale na dziewięć obszarów.
**Scenariusz nie cytuje numerów konkretnych osiągnięć z załącznika nr 1** —
pełny tekst załącznika nie był dostępny do weryfikacji, a w materiale
szkoleniowym nie wolno podawać numerów „z pamięci”. Przed publikacją warto
zestawić scenariusz z załącznikiem i uzupełnić numery tam, gdzie mówisz
o konkretnych osiągnięciach.

Stan prawny: 1 września 2026 r.

## Dane kontaktowe na planszy końcowej

Historia repozytorium została wyczyszczona z numeru telefonu, więc plansza
końcowa pokazuje tylko stronę i e-mail. Miejsce na numer jest zaznaczone
komentarzem w `src/sceny/Sceny.tsx` (scena `Koniec`) — wystarczy dopisać
trzecią pozycję, jeśli numer ma wrócić.
