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
  z nazwiskiem na wstępie filmu”. Wyzwalaj także przy syntezie mowy:
  „wygeneruj narrację w ElevenLabs”, „przeczytaj to moim głosem”, „głos jest
  robotyczny”, „za szybko / za wolno na początku”, „dodaj ciepła i emocji” —
  wtedy prowadzi Cię `references/styl-narracji.md`. NIE używaj do samego pisania scenariusza
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
3. **Studio Sound.** Zanim cokolwiek potniesz, przepuść całe nagranie przez
   Descript Studio Sound (MCP: `import_media` → `prompt_project_agent`
   „apply Studio Sound at 100%, no cuts” → `publish_project` jako Audio).
   Na nagraniu z telefonu szum tła spada z −56 dB do −75 dB i znika pogłos
   pokoju. **Zaznacz w promcie, że agent ma niczego nie wycinać** — inaczej
   sam skróci pauzy i rozjedzie się z transkrypcją. Długość pliku po
   publikacji musi się zgadzać co do dziesiątej sekundy z oryginałem.
4. **Cięcie i korekcja barwy.**
   ```bash
   python3 scripts/dopasuj-glos.py \
     --dane src/dane/czesc1.json --srt glos/czesc1.srt \
     --audio glos/nagranie-studio.m4a --wyjscie public/audio/czesc1
   ```
   Skrypt sam znajduje granice kwestii, **pomija nieudane podejścia** (gdy coś
   zostało nagrane dwa razy, wygrywa ostatnia wersja), dosuwa cięcia do ciszy
   i wyrównuje głośność do −16 LUFS. Zapisuje **WAV, nie MP3** — dwa stratne
   kodowania pod rząd słychać jak „szklaną” górę.
5. **Przeliczenie i render.** `node scripts/oblicz-czas.mjs` ustawia długość
   każdego slajdu pod nagranie, potem `npx remotion render …`.

Po tym kroku napisy w filmie chodzą w rytm głosu — mają czas wzięty wprost z
nagrania, a nie wyliczony z długości tekstu.

## Dlaczego sam Studio Sound nie wystarcza

Studio Sound czyści tło, ale **nie zmienia barwy**. Nagranie z telefonu jest
ciemne: pasmo 2–8 kHz, które niesie spółgłoski, leży 13–15 dB niżej niż niskie
średnie — i właśnie to słychać jako „niewyraźny, zamulony” głos. Dlatego
`dopasuj-glos.py` po Studio Sound robi jeszcze korekcję barwy:

| co | po co |
|---|---|
| `highpass 90 Hz` | dudnienie, stukot stołu |
| `−4,5 dB @ 300 Hz` | odmulenie — usuwa „pudło” |
| `+5 dB @ 1,9 kHz` i `+5 dB @ 3,4 kHz` | zrozumiałość i wyrazistość spółgłosek |
| `treble +5 dB @ 8 kHz` | powietrze, wrażenie bliskości |
| `deesser 0,35` | syczące „s”, które budzi się po podbiciu góry |
| `acompressor 2.6:1` + `alimiter` | równa dynamika bez pompowania |
| `loudnorm −16 LUFS` | ta sama głośność w całym filmie |

Efekt na tej samej próbce: różnica 500 Hz ↔ 4 kHz spada z 13,6 dB do 5,7 dB.

**Czego nie robić:** mocnego `afftdn` (np. `nf=-25`). Odszumianie zjada górę i
pogłębia dokładnie ten problem, który próbujesz naprawić. Po Studio Sound
odszumiacz jest już niepotrzebny.

## Próbka głosu do klonowania

`assets/probka-glosu.mp3` — 98 sekund czystej mowy autorki (cztery kwestie z
nagrania cz. I, po Studio Sound i korekcji, −18 LUFS). Tyle wystarcza do
klonowania głosu w ElevenLabs (Instant Voice Clone) albo HeyGen. Plik
**celowo nie trafia do repozytorium** — publiczna próbka głosu to gotowy
materiał do podszycia się pod autorkę. Trzymamy go lokalnie i w paczce `.skill`.

Gdy dojdzie klon głosu, kolejne części nagrywają się z tekstu — bez czytania.

## Klon głosu w ElevenLabs — jakość klonu = jakość próbki

Autorka ma w ElevenLabs dwa klony: **Ewa1** (`D0Yz6dyyxHOodq3Zqi45`) i **Ewa2**
(`MxdHRlURUZPVY5h2NiXH`). Oba brzmią zniekształcone i **nie brzmią jak ona** —
bo powstały z surowego nagrania telefonem: ciemnego, z szumem tła −56 dB i
zapadniętym pasmem 2–8 kHz. Instant Voice Clone kopiuje to, co dostanie, razem
z wadami toru nagraniowego.

**Zanim zamówisz syntezę, sprawdź, z czego zrobiony jest klon.** Klon z czystej
próbki (`assets/probka-glosu.mp3` — po Studio Sound i korekcji barwy) brzmi
zupełnie inaczej niż klon z pliku prosto z WhatsAppa.

MCP ElevenLabs w tej konfiguracji **nie ma narzędzia do tworzenia klonów** —
są tylko `creative_generate_speech`, `creative_list_voices`, generowanie obrazu
i wideo. Nowy klon autorka musi założyć sama w aplikacji; my dostarczamy próbkę.

Koszt syntezy dla porównania: ok. 196 kredytów (≈ 0,03 USD) na 19 sekund mowy,
czyli ok. 5 tys. kredytów na 10-minutowy film.

## Narracja z syntezy — styl zatwierdzony

Gdy część szkolenia powstaje z tekstu, a nie z nagrania, obowiązuje jeden
wzorzec brzmienia, zaakceptowany przez autorkę. Pełny przepis:
**`references/styl-narracji.md`** — przeczytaj go, zanim wygenerujesz
pierwszy blok.

W skrócie:

- model **`eleven_v3`**, głos „Ewa-głos_do skils" (`jq4ZUryuBeDqmtkKtBZ4`);
  `eleven_multilingual_v2` brzmi robotycznie i został odrzucony;
- 3–5 **polskich znaczników reżyserskich** w nawiasach kwadratowych na blok,
  dobranych do treści: `[spokojnie, z namysłem]` przy definicji,
  `[z naciskiem]` przy zasadzie, `[stanowczo]` przy przestrodze,
  `[łagodnie]` przy zastrzeżeniu, `[ciepło, podsumowująco]` przy planie;
- **reguła wstępu:** sam tytuł w normalnym tempie (ok. 0,58 s na słowo),
  cała reszta wolno i z namysłem. Gdy model nie trafi — nie generuj od nowa,
  tylko przyspiesz sam początek przez `atempo` 1,2–1,4 i sklej;
- pauzy rób interpunkcją, **nigdy wielokropkami** — wielokropek każe modelowi
  wlec każde słowo;
- po syntezie obowiązkowy lekki łańcuch korekcyjny do −14 LUFS / −1,2 dBTP
  (ten z `dane-i-glos`, nie mocny łańcuch telefoniczny), potem
  `node scripts/oblicz-czas.mjs`.

Długość bloku trzymaj w przedziale **35–75 s**. Dłuższy tekst dziel na dwa
slajdy, zamiast przyspieszać lektora.

## Awatar w kadrze

**Trzy awatary** — pełna specyfikacja w `assets/awatary.json`, w tym gotowe
prompty do HeyGen:

| awatar | strój i scena | domyślny układ | do czego |
|---|---|---|---|
| `eduplaner` | niebieska koszula, tło lawendowe | kółko, prawy dół | materiały marki EduPlaner 2026 |
| `rada` | marynarka, prowadząca przy biurku | pół ekranu, prawa | szkolenia dla rady pedagogicznej |
| `warsztaty` | czerwona bluzka, książka w dłoni, flipchart | kółko, prawy góra | warsztaty i ćwiczenia dla kadry |

Stała garderoba to nie kaprys: widz rozpoznaje rodzaj materiału w pierwszej
sekundzie, zanim przeczyta tytuł.

**Trzy układy kadru** w `assets/Awatar.tsx` — skopiuj plik do `src/` projektu:

- **kółko** (232 px, prawy dolny lub górny narożnik) — slajd niesie treść,
  prowadząca komentuje;
- **pół ekranu** — rozmowa, podkast, omawianie czegoś na ekranie;
- **pełny kadr** — powitanie i zakończenie, z plakietką „Mirosława Ewa
  Jurczyszyn · PCTP Koszalin”.

Dopóki w `public/awatar/` nie ma nagrania, komponent rysuje monogram w kole —
film renderuje się poprawnie, tylko bez twarzy. Materiał wgrywa się jako
`public/awatar/<id>.mp4` (pętla 8–15 s, mówienie do kamery) albo `<id>.png`.

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
