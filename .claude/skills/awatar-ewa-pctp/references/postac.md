# Karta postaci — Ewa PCTP

Źródło: film „Agent Ewa — EduPlaner 2026 Intro" (1080p, 13 s), awatar HeyGen utworzony
przez użytkowniczkę. Wzorzec obrazu: `assets/ewa_kadr.jpg`, gesty: `assets/ewa_gesty.jpg`.

## Kim jest

Ewa PCTP to filmowe wcielenie autorki EduPlaner 2026 z Pomorskiego Centrum Terapii
Pedagogicznej w Koszalinie. W materiałach występuje jako **prowadząca**: wita, prowadzi
przez treść, podsumowuje, zaprasza. Mówi w pierwszej osobie, po polsku, własnym głosem.

Rola w materiale: gospodyni, nie lektor. Ewa zwraca się do konkretnego odbiorcy
(dyrektor, nauczyciel, rodzic), a nie „do widza". Zaczyna od ulgi i sensu, nie od
przepisów; obietnicę podpiera konkretem (ton marki z `eduplaner-reklama/references/marka.md`).

## Wygląd (nie zmieniaj)

| Element | Opis |
|---|---|
| Sylwetka | kobieta w wieku dojrzałym, wyprostowana, zwrócona do widza, lekki uśmiech |
| Włosy | siwo-popielate, gładko zaczesane do tyłu, spięte nisko (niski kucyk/kok) |
| Okulary | prostokątne, w cienkiej ciemnej oprawce z jaśniejszym dołem |
| Twarz | delikatny makijaż, spokojny wyraz, spojrzenie prosto w obiektyw |
| Marynarka | głęboki fioletowo-granatowy (zmierzony ok. `#241645`), dopasowana, jeden guzik |
| Bluzka | kremowo-biała, satynowa, dekolt w V, bez wzoru |
| Dodatki | cienki złoty łańcuszek, małe kolczyki, zegarek na nadgarstku |

Kolor marynarki jest w rodzinie fioletu marki (`#2D1B69`). To zaleta na jasnych i
pomarańczowych tłach, a pułapka na czystym fiolecie: postać zlewa się dołem. Na fiolecie
marki dawaj jasny element pod nią albo za nią (pasek, plansza, tekst), albo pomarańczowy
akcent u dołu kadru.

## Kadr (plan)

- **Plan amerykański / półzbliżenie**: od bioder w górę, postać ucięta dolną krawędzią
  kadru — nie „wisi" w powietrzu, stoi na krawędzi.
- W kadrze 16:9 (1920×1080) zajmuje ok. **40 % szerokości** (piksele ~600–1350),
  czubek głowy ~6 % od górnej krawędzi. Oś ciała lekko w prawo od środka.
- Postać stoi frontalnie, tułów minimalnie skręcony, głowa do widza.
- W układzie „w rogu" postać skalowana proporcjonalnie (`wstaw_ewe.py --uklad rog`,
  42 % wysokości kadru), w kółku kadrowana do kwadratu wokół głowy i ramion.

Nie stosuj zbliżeń na samą twarz (HeyGen `closeUp`) — zmienia proporcje, a widz zna Ewę
z planu amerykańskiego. Wyjątek: pion 9:16 pod Reels, gdzie `--pion` zostawia cały plan,
tylko węższy.

## Gest i mimika

- Dłonie na wysokości pasa, spokojna gestykulacja: otwarta dłoń, lekkie podkreślenie
  słowa, ręce wracają do pozycji spoczynkowej. Bez zamaszystych ruchów.
- Drobne skinienia głowy w rytmie zdań, uśmiech w powitaniu i na zakończenie.
- Postać nie chodzi, nie odwraca się, nie wskazuje poza kadr — treść obok niej
  (plansza, ekran aplikacji) pokazuje się sama.

Awatar HeyGen wykonuje gesty sam; scenariusz nie musi ich opisywać. Jeśli w prośbie
pojawia się „niech pokaże ręką na ekran", odpowiedz, że awatar tego nie zrobi wiarygodnie,
i zaproponuj cięcie na ekran zamiast gestu.

## Głos i tekst

- Głos: **wyłącznie** klon użytkowniczki z ElevenLabs (`dane-i-glos`, etap 0 i 4a).
  Tempo ok. 150 słów na minutę, liczby słownie, zdania do 20 słów
  (`dane-i-glos/references/narracja.md`).
- Ton: ciepły, spokojny, profesjonalny, wspólnotowy. Bez presji sprzedażowej, bez żargonu.
- Powitanie wzorcowe (z `eduplaner-reklama/references/heygen.md`):
  „Dzień dobry. Nazywam się Mirosława Jurczyszyn. Stworzyłam EduPlaner 2026 — cyfrową
  przestrzeń, w której cała dokumentacja przedszkola i szkoły jest w jednym miejscu…"
- Scena Ewy trwa **14–22 s na jeden ekran** (35–55 słów). Dłuższy tekst → tnij na sceny,
  między którymi zmienia się plansza.

Tekstu intro z pliku źródłowego skill nie transkrybował (w środowisku zdalnym nie było
dostępu do modelu). Jeśli potrzebny jest dokładny tekst intro, przepisz go z nagrania
(`mcp__ElevenLabs__creative_transcribe_audio` albo `mcp__elevenlabs__speech_to_text`)
i dopisz tutaj — to nagranie 13 s, koszt pomijalny, ale wymaga zgody użytkowniczki.

## Parametry techniczne wzorca

| Parametr | Wartość |
|---|---|
| Rozdzielczość | 1920×1080, 16:9, 25 kl/s |
| Obraz | H.264 (Main), yuv420p, ok. 4,7 Mb/s |
| Dźwięk | AAC, 48 kHz, stereo, 126 kb/s |
| Tło źródła | szachownica podglądu (eksport „transparent" spłaszczony do MP4) |
| Czas | 13,0 s |
| Prostokąt postaci | x 602–1353, y 66–1079 (w kadrze 1920×1080) |

Wycięta postać w `assets/`: `ewa_pctp.png` (772×1026, RGBA, kadr z 6. sekundy)
i `ewa_pctp_intro.webm` (VP9 + alfa, 1920×1080, z oryginalnym dźwiękiem intro).

## Czego nie robić

- Nie generuj Ewy w innym narzędziu (obraz, wideo, „w stylu"). Tylko awatar HeyGen
  utworzony przez nią.
- Nie zmieniaj stroju, fryzury, okularów, koloru marynarki — także „żeby pasowało do tła".
- Nie skaluj postaci nieproporcjonalnie i nie odbijaj lustrzanie (zegarek i przedziałek
  zdradzają odbicie).
- Nie dawaj Ewie cudzego głosu, także „tymczasowo".
- Nie wstawiaj Ewy na ekrany z danymi uczniów — awatar promuje aplikację i prowadzi
  szkolenia, nie prezentuje dokumentacji konkretnego dziecka.
