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
| Tło sali, znak PCTP, ikony obszarów, okno awatara, napisy | `src/elementy/` |
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

**2. Awatar** → `public/awatar.mp4`

Wejdź do HeyGen, wybierz swojego awatara i wygeneruj film z gotowego
`public/narracja.mp3` (usta idą za Twoim głosem, nie za cudzym):

```bash
export HEYGEN_API_KEY="..."
python3 ~/.claude/skills/dane-i-glos/scripts/heygen_awatar.py --awatary
python3 ~/.claude/skills/dane-i-glos/scripts/heygen_awatar.py \
        --audio public/narracja.mp3 --avatar-id <twoje_id> \
        --tlo "#2D1B69" --czekaj -o public/awatar.mp4
```

Film składa się także **bez** tych dwóch plików — wtedy w rogu jest ramka
z napisem „miejsce na awatar”, a obraz leci bez dźwięku. Nic nie trzeba
przestawiać: gdy pliki pojawią się w `public/`, wchodzą do montażu same.

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

Pełny render (ok. 17 400 klatek) trwa w tym środowisku około godziny.
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
