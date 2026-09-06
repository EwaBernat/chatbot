# Awatar HeyGen w filmie szkolnym — co jest gotowe, czego brakuje

Film obsługuje ujęcia z **awatarem HeyGen**: gdy w `public/awatar/` leży plik
`<id ujęcia>.mp4`, w lewym dolnym rogu kadru pojawia się okienko z prezenterką,
równo z paskiem napisów. Awatar niesie własny dźwięk, więc w takim ujęciu
projekt **nie dokłada** ścieżki lektora z ElevenLabs.

## Czego nie dało się zrobić z tego kontenera

Sieć wychodząca do `api.heygen.com` jest zablokowana przez pośrednika
(`connect_rejected`, decyzja polityki organizacji), a w środowisku nie ma klucza
`HEYGEN_API_KEY`. **Nagrań z awatarem nie da się więc tutaj wygenerować.**
Poniżej jest komplet danych do wygenerowania ich tam, gdzie HeyGen jest dostępny —
na komputerze autorki albo w sesji z dostępem do klucza.

## Ustawienia — te same, co w całej serii

Za brzmienie awatara odpowiada skill `film-glos` z repozytorium EduPlaner 2026
(patrz `.claude/skills/film-glos/SKILL.md`). Zatwierdzony wzorzec:

```json
{
  "voice_id": "b5b298088c384ea9bc935c384ae774f5",
  "speed": 1,
  "engine_settings": {
    "engine_type": "elevenlabs",
    "model": "eleven_multilingual_v2",
    "stability": 0.5,
    "similarity_boost": 0.75,
    "style": 0,
    "use_speaker_boost": true
  }
}
```

**Look dla filmu szkolnego:** portret w niebieskiej koszuli (ten ze strony PCTP),
do utworzenia w grupie `47a9b51a8cc14a4ba3603dd9b2635505` — ta grupa generuje bez
dodatkowej zgody. Grupa `8633e16f…` (cyfrowy bliźniak, looki podcastowe) wymaga
kliknięcia zgody na wizerunek w aplikacji HeyGen, inaczej API odrzuca żądanie
komunikatem `avatar_consent_required`.

**Jeden look na cały film.** Prezenterka nie zmienia scenerii między ujęciami.

## Które ujęcia warto nagrać awatarem

Awatar nie musi być w każdym ujęciu — w serii przedszkolnej mówi tam, gdzie zwraca
się do sali, a plansze niosą resztę. Propozycja dla modułu 1:

| Ujęcie | Dlaczego akurat to |
|---|---|
| `S1-01` | powitanie — jedyne miejsce, gdzie pada nazwisko prowadzącej |
| `S1-02` | zapowiedź modułu, zwrot do rady pedagogicznej |
| `S1-18` | „sedno całego szkolenia" — mocny akcent, lepiej wybrzmiewa twarzą |
| `S1-27` | domknięcie i zaproszenie do modułu drugiego |

Pozostałe ujęcia zostają na głosie lektorskim z ElevenLabs — tak jak w modułach
przedszkolnych.

## Skróty w tekście dla awatara

HeyGen czyta wersaliki litera po literze, więc tekst **wysyłany do HeyGena** zapisujemy
inaczej niż na planszy: `Wopf`, `Wopfu`, `Ipet`, `Pews`, `Kszof`, `Men`, `Smart`.
Na planszach i w napisach zostają prawidłowe wersaliki — zmiana dotyczy wyłącznie
tekstu dla lektora.

Teksty ujęć są w `src/scenariusz.json` w polu `narracja` (czysty tekst, bez znaczników
aktorskich — te z pola `narracjaTts` są wyłącznie dla ElevenLabs i **nie idą** do HeyGena).

## Jak wstawić gotowe nagrania

1. Wygeneruj ujęcia w HeyGenie z ustawieniami wyżej, format 16:9.
2. Zapisz je jako `public/awatar/S1-01.mp4`, `public/awatar/S1-02.mp4` i tak dalej —
   nazwa pliku musi być identyczna z `id` ujęcia.
3. Dopisz `"awatar": "S1-01.mp4"` przy tym ujęciu w `zbuduj_scenariusz.py`
   (albo bezpośrednio w `src/scenariusz.json` do jednorazowej próby).
4. Render. Okienko z awatarem pojawi się samo, a ścieżka lektora w tym ujęciu zamilknie.

**Uwaga na długość.** Nagranie z HeyGena będzie miało inną długość niż nagranie
z ElevenLabs — po podmianie przelicz czasy scen (`python3 zbuduj_scenariusz.py`
mierzy MP3; dla ujęć z awatarem ustaw `sekundy` z długości MP4).
