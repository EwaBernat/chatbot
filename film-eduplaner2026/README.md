# Film „Dlaczego warto mieć EduPlaner 2026" — 3 minuty

Komplet materiałów produkcyjnych: scenariusz, prawdziwe zrzuty druków i modułów,
storyboard do HeyGen, tekst narracji oraz gotowy projekt animacji w Remotion.

**Wszystkie dane ucznia na zrzutach są przykładowe (Jan Kowalski — postać fikcyjna).**
Zrzuty pochodzą z prawdziwych druków i prawdziwej aplikacji, nie z makiet.

## Co jest w tym katalogu

| Ścieżka | Co to jest |
|---|---|
| `scenariusz.json` | **Jedno źródło prawdy** — 10 scen: czasy, zrzuty, animacje, narracja, układ awatara |
| `SCENARIUSZ_3MIN.md` | Scenariusz do czytania i poprawiania (generowany z JSON) |
| `storyboard/EduPlaner2026_Storyboard_HeyGen.docx` | Tabela: scena · ekran · tekst awatara · animacja (A4 poziomo) |
| `storyboard/EduPlaner2026_Narracja.docx` | Czysty tekst narracji do wklejenia w HeyGen → Script |
| `druki/` | Prawdziwe druki źródłowe: WOPF, IPET, Raport Ucznia (.docx), Baza Uczniów (.xlsx), aplikacja HTML |
| `druki/pdf/` | Te same druki w PDF (z nich powstały zrzuty stron) |
| `zrzuty/` | 78 zrzutów: 39 stron A4 druków + ekrany aplikacji (1920 × 1080 @ 1.5×) |
| `remotion/` | Projekt animacji — składa film z prawdziwych zrzutów |
| `scripts/generuj_dokumenty.mjs` | Generator storyboardu, narracji i pliku MD ze `scenariusz.json` |

## Skąd wzięły się zrzuty (żeby dały się odtworzyć)

1. **Druki A4** — wygenerowane skillami `eduplaner-pctp` i `ipet-raport-pctp`
   (WOPF 11 stron, IPET 7 stron, Raport Ucznia 5 stron, Baza Uczniów 16 stron),
   przekonwertowane do PDF i wyrenderowane do PNG po 2× skali.
2. **Ekrany aplikacji** — skill `eduplaner-zajecia-ipet` zbudował połączoną aplikację
   (11 zakładek roboczych + ⑫ Druk IPET), a przeglądarka bezobsługowa przeszła przez
   wszystkie zakładki i zrobiła jednakowe zrzuty.
3. **Ekrany „wypełnione" (`*b`, `*c`, `*d`)** — dodatkowe przejście, w którym w zakładce
   ① oceniono wszystkie 9 wymiarów KSzOF (skala 1–5), wygenerowano cele z ocen WOPF
   i dodano 5 pozycji do programu ucznia. Dzięki temu na ekranie nie ma pustych formularzy
   ani ostrzeżeń „brak ocen WOPF", a druk IPET pokazuje cele ciągnięte na żywo z modułu.

Zrzuty najważniejsze dla filmu:

- `zajecia_01_obserwacje_wopf.png` — wybór osoby, miejsca i narzędzia obserwacji
- `zajecia_01b_oceny_wypelnione.png` — wypełniona tabela oceny 1–5, 9/9 wymiarów
- `zajecia_02b_cele_z_ocen.png` — cele SMART z plakietką „WYGENEROWANY Z WOPF"
- `zajecia_04b_program_wypelniony.png` — program ucznia z realnymi ćwiczeniami
- `zajecia_12b_druk_ipet_gora.png` — okładka druku IPET wewnątrz aplikacji
- `zajecia_12d_druk_ipet_PELNY.png` — cały arkusz A4 IPET (wysoki obraz do przewijania)
- `druk_IPET_Plan_s03.png` — strona z sekcją III (tabela celów) — serce sceny 5
- `druk_WOPF_Raport_s01…s11.png`, `druk_Raport_Ucznia_s01…s05.png`, `druk_Baza_Uczniow_s01…s16.png`

## Ścieżka A — animacja w Remotion (film bez awatara)

```bash
cd remotion
npm install
npm start                 # podgląd w przeglądarce (Remotion Studio)
npm run render            # MP4 1920 × 1080, 30 fps, 3:00 → out/EduPlaner2026_3min.mp4
```

`npm start` i `npm run render` same kopiują zrzuty z `../zrzuty` do `public/zrzuty`.
W kontenerze bez własnej przeglądarki dodaj `--browser-executable=<ścieżka do chrome>`.

Podłożenie narracji:

1. Wgraj plik audio do `remotion/public/` (np. `narracja.mp3`).
2. `npm run render-glos` (czyta `props-glos.json`) albo w Studio ustaw prop `glos`.
3. Jeśli głos jest dłuższy/krótszy niż 180 s — popraw pola `czas` i `od` w `scenariusz.json`
   i uruchom `node scripts/generuj_dokumenty.mjs`, żeby storyboard i narracja się zgadzały.

Gdzie wziąć głos:
- **HeyGen** — ciepły polski głos AI (najprościej, bez nagrywania),
- **ElevenLabs** — Pani własny, sklonowany głos (obsługuje to skill `dane-i-glos`;
  wymaga wcześniejszej konfiguracji Pani głosu — bez tego nie tworzymy nagrania).

## Ścieżka B — film z awatarem w HeyGen

Awatara z Pani twarzy tworzy się **wyłącznie w aplikacji HeyGen** (wymagane krótkie
nagranie zgody na wizerunek) — żadne narzędzie nie zrobi tego za Panią.

1. Nowy projekt wideo 16:9.
2. Avatars → Photo Avatar / Avatar ze zdjęcia (nagranie zgody).
3. Głos: ciepły polski głos AI, język polski.
4. Dla każdej sceny z `storyboard/EduPlaner2026_Storyboard_HeyGen.docx`: wgraj wskazany
   zrzut jako duży kadr, awatara zmniejsz do prawego dolnego rogu.
5. W polu „Script" wklej tekst z kolumny „Awatar mówi".
6. Sceny 1 i 10 (powitanie, zaproszenie) — awatar duży, to spina film klamrą.
7. Przejścia, ściszona muzyka, render MP4.

**Wariant najlepszy z obu:** wyrenderuj obraz w Remotion (ścieżka A, bez głosu),
wgraj MP4 do HeyGen jako tło i dołóż tylko awatara w rogu.

## Struktura filmu (10 scen, 180 s)

| # | Scena | Czas | Na ekranie |
|---|---|---|---|
| 1 | Powitanie | 0:00–0:18 | plansza marki |
| 2 | Obserwacja i ocena WOPF | 0:18–0:38 | moduł: wybór + tabela ocen 1–5 |
| 3 | Gotowy druk WOPF | 0:38–0:56 | 11 stron A4 jak talia kart |
| 4 | Cele SMART z biblioteki | 0:56–1:16 | cele z WOPF, biblioteka 120 pozycji, program |
| 5 | **IPET na żywo** | 1:16–1:36 | cele lecą z modułu do sekcji III druku |
| 6 | Raport dla rodzica | 1:36–1:52 | 5 stron syntezy w wachlarzu |
| 7 | Baza Uczniów | 1:52–2:10 | rejestr xlsx, widok dyrektora |
| 8 | Ewaluacja i otwarty projekt | 2:10–2:30 | ewaluacja, dopisywanie własnych treści |
| 9 | Co składa się na subskrypcję | 2:30–2:46 | lista sześciu punktów |
| 10 | Zaproszenie | 2:46–3:00 | CTA, kontakt, miejsce na kod QR |

## Krótsze wersje (do zrobienia z tego samego materiału)

- **Spot 30 s:** scena 1 (skrócona) + scena 5 + scena 10.
- **Post / karuzela:** hasła ze scen 3, 5, 6 + plansza subskrypcji.
- **Wersja pionowa 9:16:** w `remotion/src/Root.tsx` dołóż drugą kompozycję
  1080 × 1920 i w scenach typu „ekran" zamień `objectFit: cover` na kadrowanie do środka.

## Marka

Fiolet `#2D1B69`, ciemny fiolet `#1a0f42`, pomarańcz `#E8450A`, font Arial, 16:9.
Kontakt na ekranie końcowym: kontakt@eduplaner2026.pl · 662 888 403.
Główne wezwanie do działania: **formularz analizy potrzeb** (link/QR wstawia autorka).
