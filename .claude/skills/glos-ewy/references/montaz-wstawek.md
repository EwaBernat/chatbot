# Wklejanie wstawek do gotowego modułu filmu

Procedura sprawdzona na modułach M1, M3 i M4 szkolenia przedszkolnego (5 września 2026 r.).

## 1. Znajdź punkt cięcia co do sekundy

Filmy EduPlaner mają u dołu pasek napisów, który odsłania wypowiadany tekst. To najlepszy
zegar, jaki jest w materiale — pokazuje dokładnie, w którym miejscu narracji jesteśmy.

```bash
# klatka z paska napisów w danej sekundzie
ffmpeg -v error -ss <sekunda> -i film.mp4 -frames:v 1 \
       -vf "crop=1500:120:210:895,scale=iw*2:ih*2" -q:v 2 klatka.png -y
tesseract klatka.png stdout -l pol --psm 6
```

Mając transkrypcję modułu, oszacuj czas końca akapitu z udziału słów
(słowa do tego akapitu ÷ wszystkie słowa × długość filmu), a potem zawęź przedział
odczytami paska. Skrypt `szkolenie-szkola/znajdz_ciecia.py` robi to automatycznie:
przeszukuje okno ±28 s co 2 s, dopasowuje odczyt do akapitów i domyka do 0,2 s.

**Kontrola:** granice akapitów zwykle pokrywają się ze zmianą planszy. Wykryjesz je tak:

```bash
ffmpeg -hide_banner -nostats -i film.mp4 \
  -filter:v "crop=1920:420:0:300,select='gt(scene,0.05)',showinfo" -an -f null - 2>&1 \
  | grep -oE "pts_time:[0-9.]+"
```

Uwaga na dwie rzeczy, które kosztowały czas przy pierwszym podejściu: `-v error` wycisza
`showinfo` i `silencedetect` (trzeba `-hide_banner -nostats`), a wycinek musi obejmować
sam obszar tytułu — pełna klatka zmienia się cały czas przez ruchomy pasek napisów.

## 2. Zrób planszę w projekcie filmu

Zmierzone z oryginału: tło `#FCFCFA`, pasek górny `#E8450C` (8 px), etykieta modułu
`#968B9F` w prawym górnym rogu (wersaliki, odstęp 3,2 px), kreska `#E34919`, tytuł
`#2D1B69`, pasek napisów od 388 do 1535 px w poziomie i od 922 do 1026 px w pionie,
stopka `#C4C9CE`. Szablon HTML i renderer: `szkolenie-szkola/plansza.py` (Chromium
przez Playwright, 1920×1080).

## 3. Złóż

```bash
python3 szkolenie-szkola/zloz_wstawki.py \
        --audio katalog_z_mp3 --zrodla katalog_z_mp4 --wyjscie gotowe/
```

Potok dzieli film w punkcie cięcia, buduje wstawkę (plansza + pasek napisów przewijany
porcjami po ~11 słów, proporcjonalnie do długości nagrania) i skleja całość w parametrach
oryginału: 1920×1080, 30 kl./s, H.264, AAC 48 kHz stereo. Brakującego nagrania nie
zastępuje ciszą — pomija wstawkę i mówi, której brakuje.

**Licząc czasy w gotowym filmie pamiętaj o przesunięciu:** druga wstawka w module trafia
na `punkt_cięcia + długość pierwszej wstawki`. Łatwo się na tym pomylić przy sprawdzaniu
styków.

## 4. Sprawdź styki

Odczytaj pasek napisów tuż przed cięciem, w środku wstawki i po powrocie do filmu.
Poprawny styk wygląda tak: ostatnie zdanie akapitu → wstawka → film wraca **dokładnie**
w słowie, w którym został przecięty. Sprawdź też głośność obu stron (`ebur128`) —
różnica powyżej 1 dB jest słyszalna.
