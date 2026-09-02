# Film szkoleniowy „Cele SMART w przedszkolu”

Komplet materiałów do nagrania szkolenia dla nauczycieli przedszkola, zbudowany
**na podstawie broszury PCTP Koszalin** „Cele SMART w przedszkolu” (sygn. **SMART-P1**,
stan prawny 28 sierpnia 2026 r.), autorstwa pedagoga specjalnego mgr Mirosławy Ewy Jurczyszyn.

Przykład przewodni — ten sam co w broszurze: konspekt **TUE-1 „Termometr napięcia”**
(sfera integracji społeczno-emocjonalnej i samoregulacji, ICF b1521).

## Co tu jest

| Plik | Co to jest |
|---|---|
| `scenariusz_filmu.md` | scenariusz produkcyjny — 16 scen, ok. 19 minut: plansza + tekst na ekranie + narracja + wskazówki |
| `narracja.txt` | **czysty** tekst narracji (bez nagłówków), liczby zapisane słowami — gotowy dla lektora albo silnika mowy |
| `narracja_ze_scenami.txt` | ta sama narracja z podziałem na sceny — do redakcji, nie do nagrania |
| `zrodla.md` | zaplecze merytoryczne: skąd pochodzi SMART, formuła zdania, progi ewaluacji i kody ICF |
| `plansze/*.png` | 17 gotowych plansz w kolorach marki (14 w 16:9 + konspekt A4 do wydruku) |
| `plansze/*.html` | źródła plansz — poprawiasz tekst i renderujesz ponownie |
| `zbuduj_plansze.py` | generator plansz (headless Chromium, działa bez internetu) |
| `plansze/logo-pctp.webp` | logo PCTP — w nagłówku każdej planszy, duże na karcie tytułowej i końcowej |
| `zbuduj_scenariusz.py` | generator scenariusza i pliku narracji z jednej listy scen |
| `zbuduj_animacje.py` | generator gotowego filmu: ujęcia, najazdy kamery na omawiany element, narracja bez pośpiechu |

## Plansze

| Plik | Scena filmu | Zawartość |
|---|---|---|
| `000_karta_tytulowa.png` | — | **karta tytułowa** filmu: tytuł, autorka, sygnatura, stan prawny |
| `001_plan_szkolenia.png` | 0 | **plan szkolenia** — powitanie i zapowiedź obu części |
| `00_tytul.png` | 1 | otwarcie: cel-życzenie kontra cel-narzędzie |
| `12_dlaczego_teraz.png` | 2 | uzasadnienie: nowa podstawa, wrzesień, ocena efektywności |
| `01_zyczenie_narzedzie.png` | 3 | §1 — zasada trzech osób |
| `02_piec_liter.png` | 4 | §2 — S M A R T: pytanie, przykład, pułapka |
| `03_szesc_krokow.png` | 5 | §3 — od obserwacji do zapisu |
| `04_formula_zdania.png` | 6 | §4 — **wpisywanie celu**: siedem pól formularza |
| `05_bank_czasownikow.png` | 7 | §5 — czasowniki, które widać, i pułapki |
| `06_termometr_rozbior.png` | 8 | §6 — rozbiór celu wzorcowego + karta obserwacji |
| `07_dziewiec_obszarow.png` | 9 | §7 — gotowy cel na każdy z dziewięciu obszarów |
| `08_ewaluacja.png` | 10 | §8 — zielony, żółty, czerwony |
| `09_checklista.png` | 11 | §9 — dziesięć pytań i pięć poprawek |
| `10_podstawa_prawna.png` | 12 | §10 — pięć aktów i co z nich wynika |
| `10b_czy_obowiazkowe.png` | 14 | §10 — **czy cel SMART jest obowiązkowy**: co przepisy nakazują, a czego nie |
| `10c_stare_nowe.png` | 13 | §10 — **stare i nowe rozporządzenie**: 2017 poz. 356 → 2026 poz. 378, i co się nie zmieniło |
| `11_zrodla.png` | 15 | skąd się wzięły te cele — Doran, Mager, Kiresuk, Locke i Latham, WHO, IDEA |
| `13_final.png` | 16 | zakończenie i kontakt |
| `14_konspekt_tue1.png` | 8 (wstawka) | **konspekt zajęć A4** z wpisanym celem SMART i kartą obserwacji do wydruku |

## Jak to przebudować

Treść zmieniasz w jednym miejscu i generujesz od nowa — nic nie edytujesz ręcznie w PNG:

```bash
python3 zbuduj_plansze.py        # HTML + PNG wszystkich plansz
python3 zbuduj_plansze.py --tylko-html   # bez renderowania
python3 zbuduj_scenariusz.py     # scenariusz_filmu.md + narracja.txt
```

Skrypt plansz używa przeglądarki dostępnej lokalnie
(`/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell`).
Na innym komputerze podmień ścieżkę w stałej `CHROM` na własnego Chrome'a lub Chromium.

Kolorów marki nie zmieniaj bez potrzeby: fiolet `#2D1B69` jest tekstem i tłem plansz tytułowych,
pomarańcz `#E8450A` to akcent, zielony `#0D7D5C` oznacza zapis poprawny, czerwony `#B8350D` — błędny.
Ten kod kolorystyczny powtarza się na wszystkich planszach i niesie znaczenie.

## Logo

`plansze/logo-pctp.webp` to kopia `logo-lawenda.webp` z katalogu głównego repozytorium.
Leży obok plansz, bo odwołania w HTML są względne — zrzut z innego katalogu wyszedłby
bez logo, tak samo jak bez arkusza stylów. Podmiana logo to podmiana tego jednego pliku
i ponowne uruchomienie `zbuduj_plansze.py`.

## Czego tu nie ma — i dlaczego

**Nie ma pliku MP3 ani MP4.** Film firmowany nazwiskiem autorki ma brzmieć jej głosem,
a skill nie ma zapamiętanego jej głosu (`~/.config/dane-i-glos/konfiguracja.json` nie istnieje).
Nagranie cudzym głosem — także „na próbę” — podważa wiarygodność materiału, więc nie powstaje.

Dodatkowo w tym środowisku polityka sieciowa blokuje połączenia do `api.elevenlabs.io`
i `api.heygen.com` (proxy zwraca 403), więc skrypty głosowe i tak nie mogłyby się połączyć.

Żeby dokończyć film, potrzebny jest jeden z dwóch kroków — oba wykonuje się poza tym kontenerem:

```bash
# raz na zawsze: zapamiętanie własnego głosu (3 min czystego nagrania po polsku)
python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py nagranie.mp4 --nazwa "Ewa - narracja PL"

# potem: głos + napisy z gotowego tekstu narracji
python3 .claude/skills/dane-i-glos/scripts/elevenlabs_tts.py \
        materialy/cele-smart-w-przedszkolu/narracja.txt -o narracja.mp3 --srt napisy.srt
```

**Nie ma też wersji z awatarem HeyGen.** Wymaga ona klucza `HEYGEN_API_KEY` oraz połączenia
z `api.heygen.com`; w tym środowisku klucza nie ma, a polityka sieciowa i tak blokuje ten host
(proxy zwraca 403). Złącze HyperFrames nie sięga po awatary z konta — robi filmy z HTML.
Ścieżka do awatara prowadzi więc przez własny komputer:

```bash
export HEYGEN_API_KEY="..."                                  # app.heygen.com → Settings → API
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --awatary
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py \
        --audio narracja.mp3 --avatar-id <id> --tlo "#2D1B69" --czekaj -o awatar.mp4
```

Wariant `--audio` jest właściwy: awatar mówi wtedy tym samym nagraniem, które słychać w filmie,
a nie innym głosem z HeyGen.

Alternatywnie: nagraj narrację samodzielnie z pliku `narracja.txt` — tekst jest przygotowany
pod czytanie na głos (zdania do 20 słów, liczby zapisane słowami, pauzy w miejscach pustych linii).

## Jak powstaje gotowy film

```bash
python3 zbuduj_animacje.py <katalog_z_nagraniami> -o film.mp4
python3 zbuduj_animacje.py <katalog> -o proba.mp4 --segmenty 4,5   # tylko wybrane
```

Katalog ma zawierać nagrania `s0.mp3` … `s6.mp3` — po jednym na segment, akapit na ujęcie.
Generator stoi na trzech zasadach:

1. **Obraz nadąża za słowem.** Nagranie tnie się na ujęcia tam, gdzie kończy się akapit
   narracji, a między ujęciami wstawiana jest cisza. Żadne zdanie nie zaczyna się, zanim
   obraz nie usiądzie — nic nie jest przyspieszane.
2. **Kamera pokazuje to, o czym mowa.** Ujęcie wskazuje selektor CSS; pozycję elementu
   mierzy przeglądarka (`--dump-dom`), a kadr dojeżdża do niego płynnie przez `zoompan`.
   Współrzędnych nie wpisujemy ręcznie — poprawiona plansza sama przesuwa kadr.
3. **Jedno źródło treści.** Stany planszy powstają przez wstrzyknięcie CSS do gotowego
   HTML-a, więc tekst nie jest duplikowany.

Film w pełnej jakości potrafi przekroczyć limity załączników w komunikatorach —
plansze kompresują się jednak bardzo dobrze, więc `--lekka-kopia` zapisuje obok
mocno skompresowaną wersję do wysłania, praktycznie bez straty czytelności tekstu.

Film otwiera i zamyka **karta w ciszy** — segment bez narracji, opisany w `SEGMENTY`
przez `{"plansza": …, "trwanie": 6.5}` zamiast listy ujęć. Dostaje delikatny najazd
oraz łagodne wejście i wyjście z czerni, żeby widz zdążył przeczytać tytuł, zanim
zacznie się mówienie.

Granice ujęć w segmentach 1–3 są wpisane jako sekundy; w segmentach 4–6 wyznacza je
automatycznie najdłuższe pauzy w nagraniu. Podgląd pauz:

```bash
ffmpeg -i s4.mp3 -af silencedetect=noise=-32dB:d=0.28 -f null /dev/null
```
