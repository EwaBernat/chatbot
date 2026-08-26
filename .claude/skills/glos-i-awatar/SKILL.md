---
name: glos-i-awatar
description: >-
  Podkłada głos Mirosławy Ewy Jurczyszyn i jej awatara pod filmy szkoleniowe,
  webinary, podkasty i nagrania z pokazem ekranu. Użyj ZAWSZE, gdy autorka
  prosi o: „dodaj mój głos”, „użyj mojego głosu”, „lektor do tego filmu”,
  „dopasuj nagranie do slajdów”, „popraw i wyczyść ten głos”, „potnij nagranie
  na slajdy”, „napisy w rytm mojego głosu”, a także gdy wgrywa jedno długie
  nagranie (WhatsApp, dyktafon, m4a/mp3/mp4) do materiału, który ma kilka
  slajdów lub scen. Wyzwalaj również przy prośbach o awatara na ekranie:
  „moja twarz w kółeczku po prawej”, „układ pół na pół przy pokazywaniu
  ekranu”, „awatar w rogu slajdu”, „gadająca głowa do podkastu”, „plakietka
  z nazwiskiem na wstępie filmu”. NIE używaj do samego pisania scenariusza
  ani do składania prezentacji — to robi skill szkolenie-html-16-9; ten skill
  wchodzi dopiero wtedy, gdy w grę wchodzi dźwięk albo wizerunek prowadzącej.
---

# Głos i awatar prowadzącej

Dwie rzeczy, które zamieniają nieme slajdy w materiał z człowiekiem: **ścieżka
lektorska pocięta na slajdy** oraz **awatar w kadrze**. Oba elementy wpinają się
w projekt Remotion (`film-szkolenie/`), który składa filmy z prezentacji.

## Zasada nadrzędna

Autorka nagrywa **raz, w jednym ciągu** — czyta cały scenariusz od początku do
końca. Nigdy nie proś jej o 25 osobnych plików, jeśli można pociąć jedno
nagranie; to różnica między dziesięcioma minutami pracy a godziną.
Wszystko poniżej służy temu, żeby jedno długie nagranie samo trafiło na
właściwe slajdy.

## Ścieżka lektorska — cztery kroki

1. **Transkrypcja z czasem.** Wyślij nagranie do Descriptu i pobierz SRT.
   Dokładny przepis: `references/glos.md`.
2. **Korekta tekstu.** Popraw w SRT przejęzyczenia, powtórzenia, nazwiska i
   interpunkcję. Napisy w filmie biorą tekst stąd, więc to jedyne miejsce, gdzie
   da się naprawić potknięcie bez ponownego nagrywania. Błędy zmieniające sens
   (zła nazwa metody, złe słowo w definicji) wypisz autorce — one wymagają
   dogrania jednej kwestii.
3. **Cięcie i czyszczenie.**
   ```bash
   python3 scripts/dopasuj-glos.py \
     --dane src/dane/czesc1.json --srt glos/czesc1.srt \
     --audio nagranie.m4a --wyjscie public/audio/czesc1
   ```
   Skrypt sam znajduje granice kwestii, **pomija nieudane podejścia** (gdy coś
   zostało nagrane dwa razy, wygrywa ostatnia wersja), dosuwa cięcia do ciszy,
   czyści dźwięk i wyrównuje głośność do −16 LUFS.
4. **Przeliczenie i render.** `node scripts/oblicz-czas.mjs` ustawia długość
   każdego slajdu pod nagranie, potem `npx remotion render …`.

Po tym kroku napisy w filmie chodzą w rytm głosu — mają czas wzięty wprost z
nagrania, a nie wyliczony z długości tekstu.

## Awatar w kadrze

Trzy układy, wszystkie w `assets/Awatar.tsx` — skopiuj plik do `src/` projektu:

- **kółko po prawej** — slajd niesie treść, prowadząca komentuje;
- **pół ekranu** — rozmowa, podkast, omawianie czegoś na ekranie;
- **pełny kadr** — powitanie i zakończenie, z plakietką „Mirosława Ewa
  Jurczyszyn · PCTP Koszalin”.

Rozmiary, pozycje, jak nagrać materiał i jak zapętlić krótkie ujęcie:
`references/awatar.md`.

Projektując slajdy pod film z kółkiem, zostaw **prawy dolny narożnik wolny** —
albo przenieś awatara na `pozycja="prawy-gora"`.

## Podpis autorki

Każdy materiał — film, prezentacja, scenariusz — kończy się planszą albo linijką:
**Mirosława Ewa Jurczyszyn · PCTP Koszalin**. Na filmach z awatarem nazwisko
pojawia się dodatkowo na plakietce w pierwszym ujęciu.

## Częste pułapki

- **Nagranie bez pauz.** Jeśli autorka czytała bez przerw między kwestiami,
  skrypt tnie po dopasowaniu słów, ale cięcia bywają ciasne. Wtedy poproś o
  2–3 sekundy ciszy między kwestiami przy następnym nagraniu.
- **Zmiana pomieszczenia w połowie.** Słychać przeskok barwy. Lepiej dograć
  całą część od nowa niż łączyć dwa pomieszczenia.
- **Awatar 16:9 w układzie pół na pół.** Kadr jest wąski i wysoki — materiał
  poziomy przycina się do samej twarzy. Do tego układu nagrywaj pionowo.
- **Kółko mniejsze niż 260 px** przy 1920×1080 — twarz przestaje być czytelna
  na rzutniku.
- **Muzyka pod lektorem.** Jeśli dokładasz podkład, zejdź do −28 dB i włącz
  `sidechaincompress`, inaczej głos ginie w mowie ciszej wypowiadanej.
