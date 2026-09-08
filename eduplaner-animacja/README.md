# EduPlaner 2026 — animacja „Metryczka” (Remotion)

Film reklamowy 1920×1080 pokazujący moduł **Metryczka**: ekran główny modułu, cztery strony
druku metryczki wypełniające się same (sekcje I–X), ścieżkę dziecka i podstawę prawną metryczki (bez wezwania „dołącz do projektu” — to trafi na koniec po analizie wszystkich druków).
Narracja: sklonowany głos autorki (ElevenLabs, model `eleven_v3`), sceny i napisy są
dopasowane do nagrania automatycznie.

## Uruchomienie

```bash
npm install
npx remotion studio                      # podgląd na żywo
npm run render                           # out/eduplaner-promo.mp4
```

W kontenerze bez własnej przeglądarki dodaj:
`--browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell`.

## Skąd co się bierze

| Element | Źródło |
|---|---|
| długość filmu | długość `public/narracja.mp3` |
| granice scen i napisy | `public/film.json` — składa go `skrypty/wyrownaj.py` z pauz w nagraniu |
| tekst narracji | `public/scenariusz-narracji.txt` |
| momenty animacji (kliknięcie, „zasila”, stempel) | `znaczniki` w `film.json` = początek zdania, w którym pada fraza |

## Zmiana narracji

1. Popraw `public/scenariusz-narracji.txt` (znaczniki `[warmly]` są tylko dla eleven_v3).
2. Wygeneruj nowe MP3 tym samym głosem i zapisz jako `public/narracja.mp3`.
3. `python3 skrypty/wyrownaj.py` — jeśli zmieniła się liczba zdań, popraw mapę `SCENY` w skrypcie.
4. `npm run render`.

## Sceny

`Intro` → `EkranGlowny` (8 kart modułu, kursor klika „Druk metryczki dziecka”) → `Druk1` (I–II, pola
wpisują się same, panel „zasila cały system”) → `Druk2` (III–V, wybór ścieżki A) → `Druk3` (VI–VII,
wychowawca trafia do tabeli) → `Druk4` (VIII–X, stempel „teczka gotowa”) → `Final` (ścieżka, hasła, CTA).

Marka: fiolet `#2D1B69`, pomarańcz `#E8450A`, morski `#2F8F8A` (ekran modułu), Arial.

## Film 2 — KPOF na ORYGINALNYM druku (`KpofPromo`)

Kompozycja `KpofPromo` nie odwzorowuje druku — wczytuje prawdziwy plik `public/kpof_3_4.html`
(Kwestionariusz Przedszkolnej Oceny Funkcjonalnej, wersja A) i uruchamia jego własny skrypt
liczący wyniki. Komponent `src/kpof/OryginalnyDruk.tsx` klatka po klatce „obsługuje” druk jak
użytkownik: klika kółka ocen 1–5/N, zaznacza pola, wpisuje tekst, a kamera jedzie po arkuszu
A4 do miejsc, o których mówi narracja. Sumy, średnie, poziomy, wykres słupkowy i mapa radarowa
liczą się z oryginalnego skryptu druku. Oceny (`OCENY` w `src/kpof/KpofPromo.tsx`) są dobrane
tak, żeby profil pokazał wszystkie kolory: zasób, Poziom I, II i III.

```bash
python3 skrypty/wyrownaj.py kpof      # public/kpof-narracja.mp3 + kpof-scenariusz.txt → public/kpof.json
npx remotion render KpofPromo out/eduplaner-kpof.mp4
```

Harmonogram scen (kliknięcia, kamera, wykresy) liczy się z czasów zdań w `public/kpof.json`
(indeksy zdań w `zbudujHarmonogram`). Wersje B (5 lat) i C (6 lat) leżą w `public/` — wystarczy
zmienić `plik` w `kpof.json`. Zakończenie: podstawa prawna części KPOF wg skryptu szkolenia
(wydanie 2 po audycie).
