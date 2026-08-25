# Skład, paleta i przygotowanie do druku

## Dlaczego strony są sztywne

Każda strona to blok 210 × 297 mm — nie tekst, który sam się leje przez strony.
Podgląd na ekranie jest więc dokładnie tym, co wyjdzie z drukarki, a łamanie
nie zależy od ustawień przeglądarki. Cena tego rozwiązania: nadmiar tekstu nie
przenosi się dalej, tylko zostaje ucięty po cichu. Dlatego `sprawdz.py` mierzy
każdą stronę i zgłasza przelanie w pikselach i milimetrach.

## Paginacja — 60 stron

| Strony | Zawartość |
|---|---|
| 1 | Okładka |
| 2 | Strona tytułowa |
| 3 | Strona redakcyjna |
| 4 | Spis treści |
| 5–8 | Wstęp · pięć części rozdziału · oś czasu · termometr emocji |
| 9–44 | Dwanaście rozdziałów, po 3 strony |
| 45–46 | Dwanaście zdań na dwanaście emocji |
| 47 | Moja karta emocji |
| 48 | Słowniczek |
| 49 | Jak pracować z broszurą (dla dorosłych) |
| 50 | Nota o cytatach |
| 51 | Moje notatki |
| 52–59 | Załącznik: gra |
| 60 | Tylna okładka |

Numeracja w stopce biegnie od strony 4 do 59, przy zewnętrznej krawędzi: na stronach
nieparzystych po prawej, na parzystych po lewej. Okładki i strony tytułowe pagin nie mają.
Żywa pagina u góry: znak serii i tytuł na jednej krawędzi, numer i tytuł rozdziału na drugiej.

Liczba stron musi dzielić się przez 4 (oprawa zeszytowa). Jeśli zmieniasz liczbę
rozdziałów albo dodatków, dołóż lub ujmij strony notatek, żeby wyjść na wielokrotność 4.

## Marginesy i kolumna

Lustrzane: 24 mm przy grzbiecie, 18 mm od zewnątrz, 15 mm góra, 13 mm dół.
Kolumna tekstu 152 mm, czyli około 66 znaków w wierszu.

## Typografia

| Rola | Krój | Stopień |
|---|---|---|
| Tekst główny | Atkinson Hyperlegible Regular | 12 pt / interlinia 1,62 |
| Nagłówki, liczby | Alegreya Sans ExtraBold | 1,1–3,5 em |
| Pagina, etykiety | Alegreya Sans Medium, kapitaliki z rozstrzeleniem | 0,62–0,8 em |

Oba kroje są statyczne. To nie przypadek: Chromium w trybie bezgłowym potrafi nie
osadzić kroju zmiennego w PDF-ie i tekst po cichu spada na krój zastępczy.
Jeśli sięgasz po inny krój, sprawdź w wygenerowanym PDF-ie, czy naprawdę tam jest.

Tekst jest **wyrównany do lewej, nie justowany**. Justowanie robi nierówne odstępy
między słowami, a te utrudniają czytanie osobom z trudnościami w czytaniu.

Skład sam poprawia typografię polską: wiąże twardą spacją wyrazy jednoliterowe
(`a i o u w z`), zamienia pauzę na półpauzę i skleja wielokropek. Robi to wyłącznie
w tekście — wnętrze `<svg>` omija, bo twarda spacja w danych ścieżki zepsułaby rysunek.

## Paleta

| Zmienna | HEX | Rola |
|---|---|---|
| `--papier` | `#F7F4EC` | tło stron |
| `--papier-cien`, `--papier-2` | `#EDE8DC` | plansze ilustracji, kafle |
| `--karta` | `#F7F4EC` | tło wewnątrz rysunków |
| `--atrament` | `#1F2E33` | tekst |
| `--atrament-2` | `#55666A` | tekst drugoplanowy |
| `--atrament-3` | `#8A9698` | podpisy, etykiety |
| `--morze`, `--morze-jasne` | `#1E5A6B`, `#E2ECEE` | kolor wiodący |
| `--szafran`, `--szafran-tlo` | `#B07E13`, `#F7EED8` | akcent, sekcja „W Twoim życiu" |
| `--oliwka`, `--oliwka-tlo` | `#5C7A49`, `#E9EEE1` | sekcja „Emocja" |
| `--glina`, `--glina-tlo` | `#A2563A`, `#F6E7E0` | sekcja „Pięć pytań" |
| `--linia`, `--linia-cienka` | `#D3CCBB`, `#E3DDCF` | kreski, ramki |

Każda z czterech sekcji rozdziału ma własny kolor **i własny kształt** — wypełnienie,
pasek z lewej, obwódka. Dzięki temu rozpoznaje się je także na wydruku czarno-białym
i przy zaburzeniach widzenia barw.

Ilustracje odwołują się wyłącznie do tych zmiennych. Kolor wpisany na sztywno
rozjedzie się z paletą, a odwołanie do zmiennej, której nie ma, daje czarne wypełnienie —
to najczęstsza przyczyna „czarnego prostokąta" zamiast rysunku.

## Druk

- **Format:** A4 pionowo, druk dwustronny, 60 stron.
- **Spady:** plik jest bez spadów; do offsetu drukarnia dodaje 3 mm z każdej strony i pasery.
- **Papier:** offset lub matowa kreda 120–150 g. Matowy nie odbija światła i mniej męczy wzrok.
- **Załącznik (54–58):** plansza, kostki i karty proszą się o 170–200 g. Warto
  zaproponować dodruk samego załącznika na grubszym papierze.
- **Okładka:** karton 250–300 g, folia matowa.
- **Bez lakieru UV** na stronach do zapisywania: 45–47, 51, 54–59.
- **Oprawa:** zeszytowa (60 stron = 15 arkuszy) albo klejona.

## Podgląd na ekranie

`broszura.html` można opublikować jako stronę — kartki wyświetlają się jedna pod drugą
na ciemniejszym tle, jak w podglądzie PDF. Na wąskich ekranach makieta skaluje się
przez `zoom`, żeby mieściła się w oknie. Kartki zawsze zostają jasne, także gdy widz
ma ciemny motyw: broszura jest odwzorowaniem druku, nie interfejsem.
