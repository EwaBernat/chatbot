# Grafiki do broszury

Wrzuć tu pliki graficzne (PNG, JPEG, WebP). Nazwy bez polskich znaków i spacji,
np. `okladka.png`, `rozdzial-21-lis.jpg`.

Najprościej przez przeglądarkę — nie trzeba niczego instalować:
**https://github.com/EwaBernat/chatbot/upload/claude/maly-ksiaze-autyzm-broszura-o9x00t/broszury/maly-ksiaze/grafiki**
przeciągnij pliki, potem zielony przycisk **Commit changes** na dole.

## Jak podpiąć grafikę do broszury

W pliku `skille/broszura-lektura-autyzm/assets/maly-ksiaze.json`:

```json
"meta": { "okladka_obraz": "grafiki/okladka.png" }
```

a przy wybranym rozdziale:

```json
{ "nr": 21, "obraz": "grafiki/rozdzial-21-lis.jpg" }
```

Potem skład:

```bash
python3 skille/broszura-lektura-autyzm/scripts/zloz_broszure.py \
        skille/broszura-lektura-autyzm/assets/maly-ksiaze.json \
        --out broszury/maly-ksiaze/maly-ksiaze-broszura.html \
        --skala 1.15 --grafiki broszury/maly-ksiaze \
        --linie skille/broszura-lektura-autyzm/assets/maly-ksiaze-linie.json
```

## Rozmiar

Grafiki są wklejane do środka pliku HTML, żeby broszura pozostała jednym dokumentem.
Plik rośnie o mniej więcej jedną trzecią rozmiaru zdjęć — przed wgraniem warto je zmniejszyć
do szerokości ok. 1600 px (okładka 2000 px).

## Akwarele scen (arkusz `akwarela-4.jpg`)

Arkusz z pięcioma scenami został pocięty na osobne pliki i przypisany do rozdziałów:

| plik | rozdział |
|---|---|
| `roza-pod-kloszem.jpg` | 9 · Pożegnanie, które przyszło za późno |
| `waz-na-pustyni.jpg` | 17 · Wąż — pierwsze spotkanie |
| `ogrod-roz.jpg` | 20 · Ogród pięciu tysięcy róż |
| `lis-i-ksiaze.jpg` | 21 · Lis i sekret oswajania |
| `zwrotniczy.jpg` | 22 · Zwrotniczy — pociągi, które gdzieś pędzą |

## Akwarele rozdziałów (arkusze `akwarela-5/6/7.jpg`)

| plik | rozdział / karta |
|---|---|
| `r01-boa.jpg` | 1 · Rysunek, którego nikt nie rozumiał |
| `r03-samolot.jpg` | 3 · Pytania bez odpowiedzi |
| `r04-asteroida.jpg` | 4 · Planeta B-612 |
| `r05-baobaby.jpg` | 5 · Baobaby |
| `r15-geograf.jpg` | 15 · Planeta Geografa |
| `r16-ziemia.jpg` | 16 · Ziemia — planeta pełna ludzi |
| `r18-kwiat.jpg` | 18 · Kwiat o trzech płatkach |
| `r19-echo.jpg` | 19 · Góra i echo + karta „Góra i echo" |
| `r23-sklep.jpg` | 23 · Kupiec i pigułki |
| `r24-noc.jpg` | 24 · Ósmy dzień |
| `r26-pozegnanie.jpg` | 26 · Pożegnanie i gwiazdy |
| `r27-szesc-lat.jpg` | 27 · Sześć lat później |
| `karta-geograf.jpg` | karta „Planeta Geografa" |
| `karta-ziemia.jpg` | karta „Ziemia" |
| `karta-kupiec.jpg` | karta „Sklep z pigułkami" |

Cztery kadry poprawiono: z rozdziału 1 usunięto angielski podpis, w rozdziale 19
„Yeloo!" zmieniono na „Halo!", a szyldy „THIRST QUENCHING PILLS" w rozdziale 23
i na karcie kupca na „PIGUŁKI NA PRAGNIENIE".

## Akwarele dosłane później (`akwarela-8/9/10.jpg`)

| plik | rozdział / karta |
|---|---|
| `r25-studnia.jpg` | 25 · Studnia + karta „Studnia na pustyni" |
| `r02-baranek.jpg` | 2 · Awaria na pustyni i dziwna prośba |
| `r06-zachody.jpg` | 6 · Czterdzieści cztery zachody słońca |

W `r02-baranek.jpg` poprawiono dymek: w oryginale było „narysuj mi mi baranka”.

Wciąż bez zdjęcia: **rozdział 7 — Kłótnia o kolce** (jest tam rysunek `kolce_scena`).
