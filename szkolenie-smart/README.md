# Cele SMART w przedszkolu — szkolenie wideo

Film szkoleniowy dla nauczycieli przedszkola, zbudowany w Remotion na podstawie
broszury **„Cele SMART w przedszkolu"** (sygn. SMART-P1, ekosystem
EduPlaner2026-MJ-PCTP, opracowanie: mgr Mirosława Ewa Jurczyszyn).

Kadr 1920×1080 dzieli się na dwie kolumny:

- **lewa (660 px)** — panel prowadzącej: wideo awatara z `public/awatar.mp4`,
  a gdy pliku nie ma — plansza zastępcza w kolorach marki,
- **prawa** — ekran omawiający treść: 18 plansz idących po kolei za narracją,
  z paskiem rozdziału, kropkami postępu i napisami.

Dźwiękiem jest jedno MP3 z narracją (`public/narracja.mp3`). Długość filmu
bierze się z długości tego nagrania — poprawiona narracja sama zmienia film.

## Struktura

```
public/narracja.txt      tekst narracji — 18 akapitów, po jednym na planszę
public/narracja.mp3      nagranie narracji (głos Ewy, ElevenLabs)
public/awatar.mp4        wideo awatara do lewej kolumny (opcjonalne)
src/scenariusz.json      treść plansz + czasy scen + napisy (generowany)
skrypty/zbuduj_scenariusz.py   buduje scenariusz.json z narracji
src/sceny/               jedenaście typów plansz
src/marka.ts             paleta PCTP z opisem ról kolorów
```

## Jak zmienić treść

1. Popraw akapit w `public/narracja.txt` (liczba akapitów musi zostać równa
   liczbie plansz — skrypt sprawdza to i odmawia, gdy się rozjadą).
2. Popraw treść odpowiedniej planszy w `skrypty/zbuduj_scenariusz.py`.
3. Przegeneruj narrację i przelicz czasy:

```bash
python3 skrypty/zbuduj_scenariusz.py --mp3-sekundy <długość nowego MP3>
```

Bez `--mp3-sekundy` skrypt przyjmuje tempo 150 słów na minutę, więc projekt
renderuje się także zanim powstanie nagranie.

## Podgląd i render

```bash
npm install
npm run studio                  # podgląd w przeglądarce
npm run build                   # out/szkolenie-cele-smart.mp4
```

W kontenerze bez przeglądarki dodaj wskazanie starego trybu headless:

```bash
npx remotion render Szkolenie out/szkolenie-cele-smart.mp4 \
  --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
```

## Awatar z HeyGen

`avatar_id` awatara prowadzącej: **`e4a9d389aba342708a6b5db8b425743f`**

Lewa kolumna kadru ma 660 × 1080 px, czyli proporcje bliskie pionowi 9:16 —
dlatego awatara renderuj pionowo, a nie poziomo. Film wchodzi do panelu przez
`object-fit: cover`, więc kadr poziomy zostałby przycięty po bokach.

HeyGen nie jest osiągalny z sesji Claude Code na stronie (proxy odrzuca
`api.heygen.com`), więc to polecenie uruchamia się **na własnym komputerze**,
z kluczem API w zmiennej środowiskowej:

```bash
export HEYGEN_API_KEY="..."          # app.heygen.com → Settings → API

# Awatar mówi Twoim głosem: gotowe MP3 steruje ustami
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py \
  --audio szkolenie-smart/public/narracja.mp3 \
  --avatar-id e4a9d389aba342708a6b5db8b425743f \
  --szerokosc 1080 --wysokosc 1920 \
  --tlo "#2D1B69" \
  --czekaj -o szkolenie-smart/public/awatar.mp4
```

Sprawdź najpierw `--suchy-bieg`: pokaże zapytanie bez zużycia kredytów.
Bez `--czekaj` dostajesz sam `video_id`, a status sprawdzasz później przez
`--status <video_id>`.

Napisów w HeyGen nie wypalaj (`--napisy`) — film ma własne, składane z narracji,
i te da się jeszcze poprawić.

## Kolory

Paleta i role kolorów są opisane w `src/marka.ts`. Ciemny fiolet `#2D1B69`
niesie tekst i tło panelu prowadzącej, jaśniejszy `#5B3FA8` — wypełnienia,
a pomarańcz `#E8450A` jest zarezerwowany dla tego, co wymaga uwagi: pułapek,
błędnych zapisów i strefy czerwonej. Zielony i żółty pojawiają się tylko tam,
gdzie kolor jest treścią (termometr, sygnalizacja) i zawsze mają podpis słowny,
więc plansze czyta się także w skali szarości.
