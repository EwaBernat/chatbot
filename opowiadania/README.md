# Rajmund i Arystoteles — pakiet dla Maksymiliana

## Część pierwsza — życie i hasła Arystotelesa

| Plik | Co to jest |
|---|---|
| `Rajmund-i-Arystoteles-do-druku.pdf` | **Wersja do druku.** A4, 52 strony, 6 ilustracji, każdy rozdział na nowej stronie. |
| `rajmund-i-arystoteles.md` | Tekst źródłowy (37 rozdziałów, słowniczek 41 pojęć, 45 pytań). |
| `audio/scenariusz/` | 37 plików tekstowych — scenariusz do nagrania, po jednym na rozdział. |

## Część druga — w czym może mi pomóc filozofia

| Plik | Co to jest |
|---|---|
| `Rajmund-i-Arystoteles-czesc-2-do-druku.pdf` | **Wersja do druku.** A4, 41 stron, 5 ilustracji. |
| `rajmund-i-arystoteles-czesc-2.md` | Tekst źródłowy (31 rozdziałów, słowniczek 23 pojęć, 45 pytań). |
| `audio/scenariusz-czesc-2/` | 31 plików tekstowych — scenariusz do nagrania. |

Część druga odpowiada na pytanie Rajmunda: w czym filozofia może pomóc, gdy
zawodzi pamięć, gdy nie rozumie się pytań, gdy hałas boli, gdy lekki dotyk nie
dociera, gdy trudno odczytać cudze emocje i gdy ludzie mówią jedno, a robią drugie.

## Wspólne

| Plik | Co to jest |
|---|---|
| `obrazy/` | Jedenaście ilustracji (JPG, 1280×720). |
| `audio/README.md` | Jak nagrać audiobook **Twoim głosem** (czego brakuje i dwa polecenia). |
| `skrypty/zbuduj_pdf.py` | Buduje PDF-y na nowo po każdej zmianie tekstu. |
| `skrypty/przygotuj_scenariusz.py` | Dzieli opowiadanie na pliki do nagrania. |
| `skrypty/nagraj_audiobook.sh` | Nagrywa pliki MP3 + napisy SRT Twoim głosem. |

## Druk

Plik PDF jest gotowy do wydruku na A4. Marginesy 20–22 mm, czcionka 12,5 pkt,
interlinia 1,75, tekst wyrównany do lewej (bez justowania — łatwiej czytać).
Do zszycia albo wpięcia w segregator: druk jednostronny, wtedy pusta połowa
strony przy krótkich rozdziałach zostaje na notatki.

## Przebudowa PDF po zmianie tekstu

```bash
python3 opowiadania/skrypty/zbuduj_pdf.py            # obie części
python3 opowiadania/skrypty/zbuduj_pdf.py 2          # tylko część druga
```

## Audiobook

Zobacz `audio/README.md`. Nagranie czeka na próbkę Twojego głosu —
skill nie tworzy nagrań cudzym głosem.
