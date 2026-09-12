# Film „Ocena Funkcjonalna · jak powstaje raport”

Interaktywny film objaśniający druk **Ocena Funkcjonalna · podsumowanie WOPF i IPET · obszary ICF**
(EduPlaner 2026). Druk jest oryginalny i wypełnia się sam; narrację czyta autorka własnym głosem
(ElevenLabs), a jej awatar (HeyGen) prowadzi film. Render do MP4 robi Remotion.

```
film/
├── ocena_funkcjonalna_film.html   ← gotowy film (otwórz w przeglądarce)
├── build_film.py                  ← generator: oryginalny druk + silnik animacji + scenariusz scen
├── narracja.txt                   ← tekst lektorski (16 akapitów = 16 scen, liczby słownie)
├── awatar/                        ← postać Ewy PCTP i intro z jej głosem (ze skilla awatar-ewa)
├── SCENARIUSZ.md                  ← scenariusz: kadr, sceny, animacje, podstawa prawna, zdjęcia
├── generuj.sh                     ← potok: głos (ElevenLabs) → awatar (HeyGen) → MP4 (Remotion)
├── foto/*.webp                    ← 5 zdjęć scen (ElevenLabs, gpt-image-2)
├── zrodlo/…html                   ← oryginalny druk, z którego powstaje film
└── remotion/                      ← projekt Remotion (iframe z filmem + Audio + OffthreadVideo awatara)
```

## 1. Obejrzyj

Otwórz `ocena_funkcjonalna_film.html`. Jeśli obok leży `narracja.mp3` (Twój głos), wczytuje się samo –
kliknij „Odtwórz”. Bez pliku dźwięku film startuje sam, w ciszy z napisami (tempo ok. 150 słów/min). Spacja – odtwarzanie, strzałki – sceny, kliknięcie zdjęcia – podmiana.

## 2. Twój głos (ElevenLabs)

Skill `dane-i-glos` nie tworzy nagrań cudzym głosem. Na koncie ElevenLabs są trzy szybkie klony
(„Ewa-głos_do skils”, „Ewa1”, „Ewa2”) oraz profesjonalny klon „Głos bez tytułu” (`1tw3WuUEU1Wt8m68hw81`),
który nie jest jeszcze wytrenowany – po jego weryfikacji i treningu w ElevenLabs ustaw go jako głos narracji:
`export ELEVENLABS_VOICE_ID=1tw3WuUEU1Wt8m68hw81`. Zapamiętanie w skillu:

```bash
export ELEVENLABS_API_KEY="..."
python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py nagranie.mp4 --nazwa "Ewa - narracja PL"
bash film/generuj.sh glos          # → film/out/narracja.mp3 + napisy.srt
```

W filmie HTML wczytaj MP3 i SRT w kartach pod kadrem – sceny dopasują się do nagrania.

## 3. Twój awatar (HeyGen)

```bash
export HEYGEN_API_KEY="..."
python3 .claude/skills/dane-i-glos/scripts/heygen_awatar.py --awatary     # znajdź swój avatar_id
export HEYGEN_AVATAR_ID="..."
bash film/generuj.sh awatar        # usta do narracja.mp3 → film/out/awatar.mp4 (kadr circle, tło #2D1B69)
```

Wczytaj `awatar.mp4` w karcie „Twój awatar” – gra w kole i na pełnym ekranie (intro, zakończenie).

## 4. MP4 (Remotion)

```bash
bash film/generuj.sh remotion      # kopiuje film, zdjęcia, MP3, SRT, MP4 do remotion/public i renderuje
# albo ręcznie:
cd film/remotion && npm install && npx remotion studio      # podgląd z suwakiem czasu
npx remotion render OcenaFunkcjonalna ../out/film.mp4
```

Kompozycja `OcenaFunkcjonalna` otwiera film HTML w iframie z `?remotion=1&dur=<długość MP3>&srt=napisy.srt`
i na każdą klatkę woła `window.__film.seek(t)` – obraz jest deterministyczny, więc render jest
klatka po klatce bez utraty synchronizacji. Dźwięk dokłada `<Audio>`, awatar `<OffthreadVideo>`
w miejscu koła (pozycję podaje film przez `window.__film.awatarPos()`).

## 5. Zmiana treści

* narracja: edytuj `narracja.txt` (akapit = scena; liczby słownie), potem `python3 film/build_film.py`;
* sceny i animacje: lista `SCENY` w `build_film.py` (kroki: `kamera`, `wpisz`, `zaznacz`, `pokaz`,
  `pasek`, `licz`, `podpis`, `strona`; czasy w ułamkach sceny `f`, `fd`);
* dane przykładowe dziecka i placówki: słownik `D` w `build_film.py`;
* nowa wersja druku: podmień plik w `zrodlo/` i przebuduj.

Dziecko, placówka i Zespół są fikcyjne. Podstawa prawna: rozporządzenie ME z 2 marca 2026 r.
w sprawie orzeczeń i opinii (Dz. U. 2026 poz. 428), § 7 ust. 6–7 od 1 września 2026 r.,
Prawo oświatowe art. 127, rozp. MEN z 9.08.2017 (kształcenie specjalne, Dz. U. 2020 poz. 1309;
PPP, Dz. U. 2023 poz. 1798), rozp. ME z 11.03.2026 (podstawa programowa, poz. 378), ICF, RODO.
