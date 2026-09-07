# Produkcja — skąd wziąć klip Ewy i jak go użyć

## Trzy źródła klipu

| Źródło | Jak wygląda | Co z nim zrobić |
|---|---|---|
| Eksport z aplikacji HeyGen **WebM, przezroczyste tło** | prawdziwy kanał alfa (VP9 `yuva420p`) | `wytnij_postac.py` tylko przepakowuje; `wstaw_ewe.py` używa od razu |
| Eksport z aplikacji HeyGen **MP4 „transparent"** | szachownica wpalona w obraz (tak wygląda intro źródłowe) | `wytnij_postac.py film.mp4` — wykrywa szachownicę i wycina |
| Render przez API (`heygen_awatar.py --tlo "#00FF00"`) | jednolite zielone tło | `wytnij_postac.py film.mp4 --tlo "#00FF00"` |

Zielony, nie fiolet: marynarka Ewy (`#241645`) leży blisko fioletu marki (`#2D1B69`);
klucz na fiolecie wycina ją razem z tłem. Niebieski też odpada (oprawki okularów, cienie
marynarki). `#00FF00` nie występuje nigdzie w postaci.

Przezroczysty eksport WebM jest w HeyGen dostępny w planach płatnych; jeśli konto go
nie ma, droga przez API z zielonym tłem daje ten sam wynik.

## Jak działa wycinanie (`wytnij_postac.py`)

1. Z boków i góry kadru (tam nigdy nie ma postaci) skrypt uczy się koloru tła:
   dwa kolory → szachownica, jeden → tło jednolite. `--tlo "#RRGGBB"` narzuca kolor.
2. Piksel jest tłem, gdy leży blisko któregoś z tych kolorów (`--prog-dol`, domyślnie 10),
   postacią — gdy daleko (`--prog-gora`, 34). Pomiędzy: półprzezroczysty.
3. Dziury w środku postaci (biała bluzka na białym polu szachownicy) są zalewane,
   drobne plamki tła usuwane, zostaje tylko duża składowa — postać.
4. Krawędź dostaje piórko (`--piorko` 1,2 px) i odjęcie domieszki tła (despill).

Zanim zrenderujesz cały klip, obejrzyj maskę: `--podglad podglad.jpg` (zielone =
przezroczyste). Gdy maska gubi jasne włosy — obniż `--prog-gora` do ~24; gdy zostawia
kawałki szachownicy — podnieś `--prog-dol` do ~14. Zwykle domyślne wartości wystarczą.

Wyjścia i ich zastosowanie:

| Przełącznik | Format | Gdzie działa |
|---|---|---|
| `--webm` | VP9 + alfa, ~4 MB / 13 s | `wstaw_ewe.py`, Remotion, HyperFrames, przeglądarki, DaVinci, CapCut |
| `--mov` | ProRes 4444 + alfa, ~35 MB / s | Premiere, Final Cut, After Effects, Keynote; **duży** |
| `--png` | jeden kadr RGBA | prezentacje, plansze, strona, miniatury |
| `--sekwencja katalog/` | PNG klatka po klatce | programy, które nie czytają WebM z alfą |
| `--przytnij` | j.w., ale kadr obcięty do postaci | mniejsze pliki do prezentacji |

Czas: ok. 0,4 s na klatkę 1080p przy pełnym renderze (13 s klipu ≈ 2–3 min);
sam kadr `--png --czas 6` trwa 2 s, bo skrypt przeskakuje do tej sekundy.

## Nakładanie (`wstaw_ewe.py`)

Wejścia: tło (kolor `#RRGGBB`, obraz PNG/JPG, film MP4) i klip Ewy. Tło jest skalowane
i przycinane do kadru wyjściowego bez zniekształceń; film w tle zapętla się, obraz stoi.
Długość wyniku = długość klipu Ewy (`overlay=shortest=1`).

WebM z alfą wymaga dekodera `libvpx-vp9` — skrypt dodaje go sam. Wbudowany dekoder
ffmpeg czyta VP9, ale **gubi kanał alfa** (postać dostaje czarne tło). Jeśli robisz własne
polecenie ffmpeg, pamiętaj o `-c:v libvpx-vp9` przed `-i ewa.webm`.

Kółko (`--kolo`): kadr przycięty do kwadratu wokół głowy i ramion, maska kołowa, domyślnie
w prawym dolnym rogu z marginesem — jak w webinarach ze skilla `eduplaner-reklama`.

Napisy (`--napisy napisy.srt`): wypalane w obrazie fontem DejaVu Sans (polskie znaki),
biały tekst z ciemną obwódką, 40 px od dołu. Do social mediów; do YouTube lepiej dołączyć
SRT osobno.

Dźwięk: domyślnie z klipu Ewy (tam jest jej głos). `--audio glos.mp3` podmienia ścieżkę,
`--bez-dzwieku` ją usuwa (np. gdy muzyka i głos dojdą w montażu).

## Prezentacje (`ewa_do_prezentacji.py`)

PowerPoint odtwarza MP4 (H.264 + AAC), ale nie obsługuje przezroczystości w wideo.
Dlatego mówiąca Ewa na slajdzie to klip zbudowany **na tle w kolorze slajdu**
(`wstaw_ewe.py --tlo "#2D1B69"`) — wtapia się w tło. Na slajdzie z gradientem albo
zdjęciem użyj obrazu PNG (nieruchoma Ewa) i osobnego MP3 z narracją.

Rozmiar slajdu skrypt czyta z pliku (16:9 i 4:3 działają). Pozycje liczone są od dołu
slajdu, jak w filmie: Ewa „stoi" na dolnej krawędzi.

Klip wstawiony przez python-pptx startuje po kliknięciu; automatyczny start ustawia się
w PowerPoint (Odtwarzanie → Start: Automatycznie). Keynote i Google Slides importują
taki plik, ale Google Slides nie odtwarza osadzonego wideo — tam trzeba podlinkować
klip z Dysku.

## Błędy, które wyglądają jak coś innego

| Objaw | Przyczyna | Co zrobić |
|---|---|---|
| Ewa ma czarne tło mimo WebM z alfą | dekoder bez alfy | `-c:v libvpx-vp9` przed `-i` (skrypt robi to sam) |
| Ewa z fioletową poświatą na krawędzi | klucz na fiolecie | renderuj na zielonym, kluczuj zielony |
| Bluzka „dziurawa" po wycięciu | tło szachownicy = kolor bluzki, dziura dotyka krawędzi | `--prog-gora 24`, sprawdź `--podglad` |
| `403` z proxy przy HeyGen / ElevenLabs | blokada sieciowa środowiska, nie klucz | zrób resztę bez API, render na komputerze użytkowniczki |
| `Nie moge otworzyc` w `wytnij_postac.py` | OpenCV nie czyta tego kontenera | `ffmpeg -i plik -c:v libx264 plik.mp4` i ponownie |
| PowerPoint: „nie można odtworzyć multimediów" | kodek inny niż H.264/AAC | `wstaw_ewe.py` zawsze daje H.264 + AAC; sprawdź źródło |
