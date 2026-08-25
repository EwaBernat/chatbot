# Szablon broszury A4 — wzór

Kompletny, gotowy do druku wzór broszury: **9 stron A4**, krój **Mulish**, wszystkie
elementy typograficzne, których broszura potrzebuje. Podmieniasz tylko teksty i zdjęcia.

## Pliki

| Plik | Do czego służy |
|---|---|
| `szablon-broszury-A4.html` | **Plik roboczy** — tu edytujesz treść. Fonty pobiera z Google Fonts. |
| `szablon-broszury-A4-druk.html` | Wersja z **osadzonymi fontami** — działa bez internetu, z niej powstaje PDF. Generowana automatycznie. |
| `Broszura-szablon-A4.pdf` | **Gotowy PDF** do druku i podglądu (9 stron A4). |
| `zbuduj-pdf.sh` | Przebudowuje PDF po zmianach w szablonie. |
| `narzedzia/osadz-fonty.py` | Wstawia fonty do wersji do druku (wywoływane przez `zbuduj-pdf.sh`). |
| `narzedzia/mulish-osadzony.css` | Mulish (latin + latin-ext) zakodowany w base64. |

## Jak zrobić z tego własną broszurę

1. Otwórz `szablon-broszury-A4.html` w przeglądarce — zobaczysz wszystkie strony jedna pod drugą.
2. Edytuj plik w dowolnym edytorze tekstu: podmieniasz treść między znacznikami, nie ruszasz klas CSS.
3. Wstawiasz zdjęcia: każdą ramkę `<div class="zdjecie-ramka …">…</div>` zastępujesz zwykłym
   `<img src="zdjecia/moje-zdjecie.jpg" style="width:100%;height:55mm;object-fit:cover;border-radius:1.5mm">`.
4. Eksport do PDF:
   - **Bez terminala:** otwórz `szablon-broszury-A4-druk.html` → `Ctrl + P` → *Zapisz jako PDF*,
     rozmiar **A4**, marginesy **Brak**, zaznacz **Grafika tła**.
   - **Z terminala:** `./zbuduj-pdf.sh`

## Struktura — co jest na której stronie

| Str. | Rola | Elementy |
|---|---|---|
| 1 | **Okładka** | pełny spad, podwójna złota ramka, miejsce na logo i zdjęcie okładkowe, tytuł, podtytuł, autor |
| 2 | **Przedmowa** | metryczka wydawnicza w ramce podwójnej, dwie kolumny, inicjał, ramka „Jak korzystać”, cytat, **stopka** |
| 3 | **Spis treści** | numeracja, linie wiodące, opisy rozdziałów, ramka-skrót, miejsce na zdjęcie |
| 4 | **Wstęp** | lead, zdjęcie na pełną szerokość z podpisem, dwie kolumny, pasek trzech liczb |
| 5 | **Rozdział 02** | dwie kolumny z linią międzyłamową, inicjał, podświetlenia, ramki (info / szałwia / ostrzegawcza), cytat |
| 6 | **Rozdział 03** | galeria 3 zdjęć, cytat na pełną szerokość, zestawienie „przed / po”, statystyki, ramka wniosku |
| 7 | **Rozdział 04** | lista kroków 01–05, tabela porównawcza, lista kontrolna, ramki „zacznij / czego unikać”, ozdobnik z kropek |
| 8 | **Słowo od autora** | narożniki ozdobne, portret autora, ramka podwójna z hasłem, podpis odręczny, pole na notatki, podziękowania i źródła, **stopka końcowa** |
| 9 | **Tył okładki** | hasło zamykające, dane kontaktowe, przycisk CTA, miejsce na kod QR, nota copyright |

## Paleta

| Rola | Kolor | HEX |
|---|---|---|
| Wiodący | granat | `#16233F` |
| Uzupełniający | atrament | `#24365E` |
| Akcent główny | złoto | `#C8963E` |
| Akcent jasny | złoto jasne | `#E7C783` |
| Akcent drugi | szałwia | `#6E8F7D` |
| Akcent alarmowy | rdza | `#B4552F` |
| Tło stron | krem | `#FBF8F2` |
| Tekst | grafit | `#2A2E38` |

Kolory zmieniasz w **jednym miejscu** — w bloku `:root` na początku pliku. Zmiana `--zloto`
przebudowuje wszystkie ozdobniki, ramki i podświetlenia w całej broszurze.

## Typografia

Cała broszura używa **Mulish** — humanistycznego bezszeryfowego kroju o dużej wysokości x,
który dobrze się czyta w długim tekście i elegancko wygląda w wersalikach nagłówków.

- Tytuł okładki: 40 pt / waga 900
- Nagłówki rozdziałów: 19 pt / waga 800
- Śródtytuły: 12,5 pt / waga 700
- Tekst ciągły: 10,5 pt / interlinia 1,62
- Podpisy i mikrotekst: 7,8–8,5 pt

## Klasy, z których budujesz strony

**Układ:** `kolumny-2`, `kolumny-3`, `kolumny-linia` (linia między łamami),
`pelna-szerokosc` (element przez oba łamy), `bez-lamania`.

**Ramki:** `ramka`, `ramka--akcent`, `ramka--szalwia`, `ramka--uwaga`, `ramka--granat`,
`ramka--cien`, `ramka--podwojna`.

**Podświetlenia:** `podswietl` (zakreślacz), `podswietl--mieta`, `podswietl--marker`
(pasek pod linią pisma), `podswietl--pelne` (biały tekst na granacie), `wyroznik`.

**Ozdobniki:** `ozdobnik-linia` z `romb`, `linia-zlota`, `kropki`, `naroznik` (`lg`/`pg`/`ld`/`pd`).

**Zdjęcia:** `zdjecie` + `zdjecie-ramka` z klasą wysokości `h-30`…`h-85`, `podpis-zdjecia`,
`galeria galeria--2`, `galeria galeria--3`.

**Pozostałe:** `spis`, `tabela`, `statystyki`/`stat`, `lista`, `lista--ptaszki`, `kroki`,
`cytat`, `notatki`, `podpis`, `stopka`, `zywa-pagina`, `inicjal`.

## Druk

- Format netto **210 × 297 mm**, marginesy treści **18 mm**, stopka **26 mm** od dołu.
- Do drukarni dodaj **spad 3 mm** z każdej strony (netto 216 × 303 mm) — elementy schodzące
  do krawędzi (okładka, tył) muszą wychodzić poza linię cięcia.
- Trzymaj tekst **min. 5 mm** od linii cięcia.
- Zdjęcia: **300 dpi**, przestrzeń **CMYK** (Coated FOGRA39 dla papieru powlekanego).
- Objętość 8 stron + okładka dzieli się przez 4 — przy oprawie zeszytowej to warunek konieczny.
- Papier: środek 120–150 g/m², okładka 250–300 g/m², matowa folia podnosi kontrast granatu.
