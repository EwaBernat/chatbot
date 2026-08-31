# Rytm, pauzy i ciepło — sprawdzony przepis na nagranie

Ustalone na prawdziwym materiale (spot EduPlaner 2026, głos „Ewa-głos_do skils",
sierpień 2026), po trzech podejściach i odsłuchu przez użytkowniczkę. To nie są
domysły — każdy punkt naprawia usterkę, którą było słychać.

## Dwie usterki i co je naprawiło

**1. „Robotycznie, płasko."** Model `eleven_multilingual_v2` czyta równo i bezpiecznie —
poprawnie, ale bez emocji. Naprawa: **`eleven_v3` ze znacznikami reżyserii**.

**2. „Mówię za szybko, po »Dzień dobry« musi być pauza, a nie katarynka."**
Sama kropka wewnątrz akapitu nie robi oddechu, a lista rozdzielona przecinkami
brzmi mechanicznie. Naprawa: **przerwa akapitu i kropki zamiast przecinków**.

## Przepis

### 1. Model: `eleven_v3`

Jedyny, który czyta polecenia w nawiasach kwadratowych i ich **nie wypowiada**.
Generuje wolniej niż `multilingual_v2` (1–2 min na minutę nagrania) — generuj
partiami, nie pojedynczo.

### 2. Jedno zdanie = jeden akapit

To najważniejsza zasada rytmu. **Przerwa akapitu (pusta linia) daje realną pauzę.
Kropka wewnątrz akapitu — nie.**

```
[warmly] Dzień dobry.

[warmly] Stworzyłam EduPlaner 2026 — cyfrową szafę, w której cała
dokumentacja przedszkola i szkoły jest w jednym miejscu.
```

Powitanie, pointa i wezwanie do działania **zawsze** stoją w osobnym akapicie.

### 3. Wyliczenia rozbijaj kropkami, nie przecinkami

```
źle:   Metryczka, WOPF, plan wsparcia, realizacja, ewaluacja.
dobrze: Metryczka. WOPF. Plan wsparcia. Realizacja. Ewaluacja.
```

Przecinki w liście to właśnie ta katarynka. Kropki dają każdemu członowi własny
oddech i brzmią jak wyliczanie z namysłem, a nie odczyt z kartki.

### 4. Znaczniki reżyserii — po jednym na akapit

| Znacznik | Gdzie |
|---|---|
| `[warmly]` | powitanie, zdania mówione w pierwszej osobie |
| `[calm]` | części opisowe, wyliczenia modułów |
| `[sincerely]` | emocjonalne serce materiału |
| `[slowly]` | pointy, które mają wybrzmieć |
| `[encouraging]` | zaproszenie, wezwanie do działania |

Zmieniaj je między sekcjami. Jeden znacznik powtarzany wszędzie daje ten sam
monotonny efekt, przed którym ma chronić.

### 5. Parametry (tylko lokalnie, przez `elevenlabs_tts.py`)

```bash
python3 scripts/elevenlabs_tts.py narracja-v3.txt -o glos.mp3 --srt napisy.srt \
        --model eleven_v3 --stability 0.35 --style 0.45 --speed 0.95
```

- **`--stability 0.35` — najważniejszy.** Domyślne `0.5` daje płaskość. Niżej =
  szerszy zakres emocji. Poniżej `0.3` głos zaczyna „pływać" i gubić spójność.
- `--style 0.45` — wzmacnia charakterystykę oryginału.
- `--speed 0.95` — lekkie zwolnienie. Nie schodź poniżej `0.9`, robi się ospale.

Zdalne złącze `creative_generate_speech` **tych suwaków nie ma** — daje tylko model
i głos. Dlatego przy dopracowywaniu brzmienia pracuj lokalnie skryptem.

## Czego nie robić

- **Nie rozbijaj tekstu wielokropkami** dla pauz. ElevenLabs czyta je jako pauzy
  w przypadkowych miejscach. Od tego są akapity i kropki.
- **Nie mieszaj plików.** Tekst ze znacznikami trzymaj osobno (`narracja-v3.txt`);
  `eleven_multilingual_v2` przeczytałby `[warmly]` na głos. Wersja czysta
  (`narracja.txt`) zostaje dla modeli bez obsługi znaczników.

## Dwie rzeczy do sprawdzenia po pierwszym odsłuchu

| Zapis | Ryzyko | Zamiennik |
|---|---|---|
| skrótowce (**WOPF**, IPET, KSzOF) | czytane jak wyraz zamiast literowane | `wu o pe ef` |
| liczby (**2026**) | zły przypadek albo cyfry po kolei | `dwa tysiące dwadzieścia sześć` |

Poprawiasz plik tekstowy i generujesz audio od nowa. Render wideo robisz dopiero,
gdy dźwięk jest dobry — kredyty HeyGen schodzą za render, nie za odsłuch.

## Długość: mierz, nie licz

Przelicznik „słów na minutę" zawodzi na klonie. Ten sam tekst (119 słów), ten sam
głos i model dał ujęcia od **62,4 s do 70,2 s** — rozrzut siedmiu sekund.

Dlatego: **generuj 2–3 ujęcia i wybierz najkrótsze**, zamiast skracać tekst.
To tańsze i nie kosztuje treści.
