# Film szkoleniowy „Budowanie mostów społecznych"

Opracowanie: **Mirosława Ewa Jurczyszyn** · PCTP Koszalin

Zamienia prezentacje szkoleniowe w filmy 1920×1080 z narracją lektorską, napisami
i planszą autorską. Zbudowane na [Remotion](https://remotion.dev) — film składa się
z prawdziwych slajdów prezentacji, więc każda poprawka w prezentacji przekłada się
na film po jednym poleceniu.

## Co jest w środku

| Ścieżka | Zawartość |
|---|---|
| `src/dane/czesc1.json`, `czesc2.json` | narracja i nazwy plików dla każdego z 25 slajdów |
| `src/Film.tsx` | układ filmu: plansza tytułowa, slajdy, napisy, tor postępu, napisy końcowe |
| `public/slajdy/` | slajdy wyrenderowane z prezentacji do plików PNG (2×) |
| `public/audio/` | **tu wgrywasz swój głos** — `01.mp3`, `02.mp3`, … |
| `tekst-lektorski.md` | gotowy tekst do nagrania, fragment po fragmencie |
| `scripts/oblicz-czas.mjs` | mierzy nagrania i ustawia długość slajdów |
| `scripts/renderuj-slajdy.sh` | odświeża obrazy slajdów po zmianie prezentacji |

## Jak zrobić film ze swoim głosem

```bash
npm install                    # raz, na początku
# 1. nagraj fragmenty z tekst-lektorski.md i wrzuć do public/audio/czesc1/
npm run film1                  # Część I  → out/mosty-czesc1-przedszkole.mp4
npm run film2                  # Część II → out/mosty-czesc2-klasy1-3.mp4
```

`npm run film1` sam uruchamia pomiar nagrań, więc długość każdego slajdu dopasowuje
się do Twojego głosu. Brakujące nagrania nie blokują renderu — te slajdy przejdą
w ciszy, z czasem wyliczonym z długości tekstu.

Podgląd na żywo, z możliwością przewijania i podmiany nagrań:

```bash
npm run studio
```

## Po zmianie prezentacji

```bash
npm run slajdy1     # przerysowuje 25 obrazów Części I
npm run slajdy2     # to samo dla Części II
```

## Uwagi techniczne

- Kroje pisma (Figtree, Source Sans 3, podzbiór z polskimi znakami) leżą w
  `public/fonty` — film renderuje się identycznie bez dostępu do internetu.
- Jeśli w systemie jest już Chromium, wskaż go zmienną `REMOTION_CHROMIUM`,
  żeby Remotion nie pobierał własnej kopii:
  `REMOTION_CHROMIUM=/sciezka/do/chrome npm run film1`.
- Napisy pod slajdem zmieniają się zdanie po zdaniu, proporcjonalnie do długości
  tekstu — przy wgranym nagraniu trafiają w rytm mowy.
