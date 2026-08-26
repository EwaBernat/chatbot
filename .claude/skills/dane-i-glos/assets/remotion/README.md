# Szablon filmu Remotion — skill `dane-i-glos`

Zamienia profil danych, narrację i napisy w film 1920×1080 w kolorach PCTP.
Nie edytuj tego katalogu ręcznie do pojedynczego filmu — złóż kopię skryptem:

```bash
python3 ../../scripts/przygotuj_remotion.py ~/moj-film \
        --profil profil.json --narracja narracja.txt \
        --audio narracja.mp3 --napisy napisy.srt \
        --tytul "Frekwencja — I półrocze"
```

Potem w powstałym katalogu:

```bash
npm install
npx remotion studio                          # podgląd na żywo, suwak czasu
npx remotion render RaportWideo out/film.mp4
```

## Co skąd się bierze

| Element filmu | Źródło |
|---|---|
| długość | długość pliku MP3 (`getAudioDurationInSeconds`) |
| granice scen | akapity narracji, dosunięte do końców napisów SRT |
| słupki wykresu | sekcja `grupy` z profilu (`--grupuj` + `--agreguj`) |
| napisy na ekranie | `napisy.srt` — znaczniki czasu z ElevenLabs |
| treść scen | `public/film.json` — plik do ręcznej poprawki |

Poprawianie treści: edytuj `public/film.json`. Poprawianie narracji: zmień
`narracja.txt`, przegeneruj MP3 i SRT, złóż projekt jeszcze raz — długość filmu
dopasuje się sama.

## Kolory

Paleta przeszła walidator dostępności (`dataviz/scripts/validate_palette.js`):

- `#2D1B69` — **tekst**. Jako wypełnienie słupka nie przechodzi (jasność 0,30
  przy paśmie 0,43–0,77), więc słupków nim nie malujemy.
- `#5B3FA8` — **słupki**. Jaśniejszy krok tego samego fioletu, przechodzi
  wszystkie sześć testów.
- `#E8450A` — **wyróżnienie**, zarezerwowane dla wartości wymagającej uwagi.
  Nigdy jako „kolejna seria". Zawsze z podpisem, żeby informacja nie zależała
  od samego koloru.

Separacja pary słupek/wyróżnienie: ΔE 26,4 przy protanopii, 33,7 przy widzeniu
normalnym. Zmieniając kolory, uruchom walidator ponownie.

Wykres ma jedną serię, więc **nie ma legendy** — tytuł nazywa to, co widać,
a każdy słupek ma etykietę wprost przy końcu.

## Render w kontenerze bez przeglądarki

Remotion używa starego trybu headless, którego nowe Chrome już nie ma. Wskaż
`headless_shell`:

```bash
npx remotion render RaportWideo out/film.mp4 \
  --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
```

## Typy scen

`tytul` · `liczba` (jedna wielka liczba) · `wykres` (słupki poziome) · `wniosek`.
Kolejność ustawia `--typy tytul,liczba,wykres,wniosek` — po jednym typie na
akapit narracji.
