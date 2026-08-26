# Twój głos — jak go sklonować raz, a używać zawsze

To etap jednorazowy. Po nim `voice_id` wpisujesz do zmiennej środowiskowej i każde następne
nagranie brzmi Twoim głosem.

**Klonuj wyłącznie własny głos** albo głos osoby, która wyraziła na to wyraźną zgodę.
ElevenLabs przy niektórych planach wymaga dodatkowej weryfikacji — nagrania zdania
potwierdzającego — i skrypt powie Ci o tym po utworzeniu głosu.

## Ile materiału

| Długość łącznie | Efekt |
|---|---|
| poniżej 1 minuty | klon płaski, słychać „robota" na dłuższych zdaniach |
| 1–2 minuty | działa, brzmi rozpoznawalnie, ale intonacja bywa monotonna |
| **3 minuty** | **punkt docelowy dla Instant Voice Cloning** |
| 30 minut i więcej | dopiero to ma sens dla Professional Voice Cloning (osobny, wolniejszy proces) |

Więcej materiału nie zawsze znaczy lepiej: **10 minut czystego nagrania bije 30 minut
z pogłosem i szumem**. Jakość źródła decyduje bardziej niż długość.

## Jak nagrać

- **Cicho**: pokój z zasłonami, dywanem, meblami. Bez klimatyzacji, lodówki, wentylatora
  w laptopie. Puste pomieszczenie z gołymi ścianami daje pogłos, którego nie da się usunąć.
- **Blisko, ale nie za blisko**: 15–20 cm od mikrofonu, lekko z boku, żeby „p" i „b"
  nie uderzały w membranę.
- **Jednym sprzętem**: całość na tym samym mikrofonie, w tym samym miejscu. Sklejka nagrań
  z telefonu i z laptopa daje klon, który zmienia barwę w połowie zdania.
- **Bez muzyki, bez drugiej osoby, bez efektów.** Żadnej normalizacji, kompresji ani
  „poprawiania" przed wysłaniem — ElevenLabs woli surowy materiał.
- **Format**: WAV 44,1 kHz mono albo MP3 128 kb/s i wyżej. Łącznie do 10 MB
  (skrypt sprawdza to za Ciebie).

## Co czytać

Czytaj **tak, jak będziesz mówić w gotowych materiałach** — jeśli narracja ma być spokojna
i rzeczowa, nagraj spokojnie i rzeczowo. Klon odtwarza sposób mówienia z próbki, nie tylko barwę.

Czytaj **po polsku**. Klon zbudowany z angielskiego nagrania będzie miał kłopot z „ś", „ć",
„ż", „dź" i z polskim akcentem wyrazowym.

Dobry materiał źródłowy masz już pod ręką: fragment własnego raportu, opis programu,
kilka akapitów z WOPF albo z IPET-u. Tekst rzeczowy działa lepiej niż wiersz czy zabawny
felieton, bo narracja z danych też będzie rzeczowa.

Nagraj **3–5 osobnych plików po 40–60 sekund**, a nie jeden ciągły. Łatwiej odrzucić
jeden nieudany fragment niż wycinać go z całości.

## Krok po kroku

```bash
export ELEVENLABS_API_KEY="..."          # potrzebne uprawnienie voices_write

# 1. Sprawdź nagrania — nic nie zostanie wysłane
python3 scripts/elevenlabs_klon_glosu.py --sprawdz-nagrania probki/*.wav

# 2. Sklonuj
python3 scripts/elevenlabs_klon_glosu.py "Ewa - narracja PL" probki/*.wav \
        --opis "Spokojna, rzeczowa narracja po polsku do raportów i materiałów PCTP"

# 3. Zapisz voice_id na stałe (dopisz do ~/.bashrc, żeby przetrwało restart)
export ELEVENLABS_VOICE_ID="<voice_id z kroku 2>"

# 4. Posłuchaj próbki, zanim zrobisz cokolwiek dużego
python3 scripts/elevenlabs_tts.py narracja.txt -o proba.mp3
```

`--odszum` prosi ElevenLabs o usunięcie szumu tła. Używaj tylko wtedy, gdy nagranie
naprawdę szumi — na czystym materiale potrafi zabrać część barwy głosu.

`--moje-glosy` wypisuje wszystkie Twoje własne (nie-gotowe) głosy z konta, gdyby `voice_id`
gdzieś się zawieruszył.

## Kiedy klon brzmi źle

| Objaw | Przyczyna | Naprawa |
|---|---|---|
| brzmi jak przez telefon | próbki z kompresją lub z telefonu | nagraj ponownie lepszym mikrofonem |
| „pływa" barwa | nagrania z różnych sprzętów lub miejsc | jedna sesja, jeden mikrofon |
| monotonny, bez emocji | próbki czytane bez wyrazu | nagraj tak, jak chcesz brzmieć |
| gubi polskie głoski | próbki po angielsku albo za krótkie | dograj polski materiał do 3 minut |
| syczy na „s" i „sz" | mikrofon za blisko, na wprost ust | odsuń się, mów lekko z boku |

Zamiast walczyć ustawieniami `--stability` i `--similarity` w `elevenlabs_tts.py`,
najpierw popraw próbki i sklonuj głos ponownie. Ustawienia korygują drobiazgi; złe
źródło poprawi tylko nowe nagranie.

## Po co to całej ścieżce

Sklonowany głos jest wspólnym punktem obu wyjść skilla:

- **audio** — `elevenlabs_tts.py` czyta scenariusz Twoim głosem,
- **film** — to samo MP3 idzie do `heygen_awatar.py --audio`, więc awatar mówi
  Twoim głosem, a nie głosem z konta HeyGen.

Dlatego ten etap robi się raz, a zwraca się przy każdym następnym materiale.
