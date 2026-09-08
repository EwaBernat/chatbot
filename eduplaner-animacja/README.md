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

## Film 3 — Obserwacja pogłębiona na ORYGINALNYCH drukach (`PogPromo`)

Treść z części 5 skryptu szkolenia: kiedy uruchamiamy obserwację pogłębioną (sześć reguł
przekierowania, karta decyzyjna), dlaczego obserwacja, a nie diagnoza (granica kompetencji),
cztery narzędzia, profil biopsychospołeczny, czego się dowiadujemy i podstawa prawna.

Druki PDF (ABC, profil sensoryczny, ToM, profil biopsychospołeczny) są wyrenderowane 1:1
do `public/pog/*.png` (150 dpi), a podświetlenia stoją na współrzędnych z PDF
(`public/pog/kotwice.json`, wyszukane po tekście przez PyMuPDF). Komponent
`src/pog/DrukPdf.tsx` prowadzi po nich kamerę. Karta rozwoju mowy (HTML) jest wypełniana
„na żywo” przez `OryginalnyDruk` (wartości z przykładu w skrypcie: 8 · 6 · 3).

```bash
python3 skrypty/wyrownaj.py pog       # public/pog-narracja.mp3 + pog-scenariusz.txt → public/pog.json
npx remotion render PogPromo out/eduplaner-pog.mp4
```

## Film 4 — WOPF wypełniony na ORYGINALNYM arkuszu (`WopfPromo`) + Strażnik prawa

Jeden plik danych `public/wopf-dane.json` (151 kroków: metryczka, ścieżka A z orzeczeniem
i zaleceniami poradni, zespół, mapa dokumentów, średnie KPOF, wyniki obserwacji pogłębionej,
potrzeby, przyczyny, zakres wsparcia, zajęcia, decyzja, przeniesienie do IPET, opinia) zasila
dwie rzeczy:

1. `node skrypty/wypelnij_wopf.mjs` — wypełnia oryginalny arkusz w prawdziwej przeglądarce
   (własny skrypt arkusza liczy poziomy, wykresy i opisy) i zapisuje
   `out/wopf/WOPF_2026_Zofia_Lewandowska_wypelniony.html` oraz `.pdf` (A4). Style, linie
   i ramki druku pozostają nietknięte.
2. `WopfPromo` — animacja, w której te same kroki wpisują się w druk klatka po klatce
   (`src/kpof/OryginalnyDruk.tsx`, kroki typu `dane`, wspólny tłumacz kroków
   `skrypty/wopf_resolver.js` ≡ `src/kpof/wopfResolver.ts`).

Bez nagrania (limit ElevenLabs) czasy napisów liczy `python3 skrypty/napisy_z_tekstu.py wopf`;
po dograniu głosu do `public/wopf-narracja.mp3` wystarczy `python3 skrypty/wyrownaj.py wopf`
i wpisać `"audio": "wopf-narracja.mp3"` w `public/wopf.json`.

**Strażnik prawa** — każdy akt cytowany w druku sprawdzony wobec skryptu szkolenia (wyd. 2 po
audycie z 5.09.2026): tabela w `public/wopf-straznik-prawa.md` i scena w filmie.

## Film 5 — IPET na ORYGINALNYM druku (`IpetPromo`) + wymagana zawartość § 6

Druk IPET (42 strony: 40 wg wzoru autorki + 2 strony podstawy prawnej) buduje
`python3 skrypty/zbuduj_ipet.py` → `public/ipet.html` (pusty, z atrybutami `data-k` na każdym
polu — po nich animacja wpisuje dane) oraz `python3 skrypty/zbuduj_ipet.py --wypelnij` →
`out/ipet/IPET_2026_Zofia_Lewandowska_wypelniony.html`. Dane dziecka: `skrypty/ipet_dane.py`
(z `public/wopf-dane.json`, KPOF, karty ABC·FBA, ToM, kwestionariusza mowy, profilu sensorycznego).
PDF i zrzuty stron: `node skrypty/drukuj_pdf.mjs <html> <pdf> [katalog_png]`.

Kroki animacji: `public/ipet-kroki.json` (fazy → okna czasu zdań w `src/ipet/IpetPromo.tsx`);
narracja `public/ipet-narracja.mp3` (klon głosu autorki, eleven_v3), wyrównanie
`python3 skrypty/wyrownaj.py ipet` → `public/ipet.json`; render `bash out/finalizuj_ipet.sh`.

Podstawa prawna: strona 41 druku = § 6 ust. 1 pkt 1–8, ust. 2–5, ocena okresowa, prawa rodziców,
§ 7 ust. 2 (t.j. Dz.U. 2020 poz. 1309); strona 42 i `public/ipet-straznik-prawa.md` = Strażnik prawa.
Wzór autorki cytował pierwotne publikatory z 2017 r. — w druku zastąpiono je wg skryptu (wyd. 2 po audycie).
