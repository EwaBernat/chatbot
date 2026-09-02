# Karta pomocy dydaktycznej — wzór KC-4

25 pomocy, po jednej na wskaźnik, w sekcji VII konspektu. Każda ma **zdjęcie
poglądowe**, listę „co przygotować", **trzy kroki użycia**, wskazówkę dla
dorosłego i **polecenie dla dziecka nagrane jej głosem** — 75 nagrań, po jednym
na wskaźnik i wersję wiekową.

## Struktura

```python
# src/pomoce_fba.py
POMOCE["I.1"] = (nazwa, [co przygotować], [trzy kroki], wskazówka, opis_zdjęcia)
POLECENIA[("I.1", "A")] = "Weź jedną rzecz z pudełka i połóż ją przed sobą."
```

Pliki mediów: `assets/pomoce_fba/k_<kod>.jpg` i `assets/audio_fba/<wersja><kod>.mp3`,
gdzie `kod("I.1")` daje `i_1`. Czyli `ai_1.mp3` to polecenie I.1 dla wersji A.

Karta bez zdjęcia dostaje pole zastępcze, bez nagrania — wyłączony przycisk.
Dokument buduje się poprawnie na każdym etapie kompletowania mediów, więc braku
nie widać. Wyłapuje go `karta_pomocy.braki()` i `sprawdz_fba.py`.

## Trzy kroki są dla dorosłego, polecenie dla dziecka

To najczęstsza pomyłka przy dopisywaniu. Trzy kroki mówią **nauczycielowi**, co
ma zrobić („Rozłóż zadanie na trzy pudełka i odsuń dwa poza zasięg wzroku
dziecka"). Polecenie mówi **dziecku**, w drugiej osobie, i to ono idzie do
nagrania („Weź jedną rzecz z pudełka i połóż ją przed sobą"). Nagranie
z instrukcją dla nauczyciela jest bezużyteczne — dziecko go nie zrozumie,
a nauczyciel i tak czyta kroki obok.

## Słowa, których przedszkolak nie rozumie

Polecenie pisz **prostymi, krótkimi zdaniami**. Nie używaj słów, które są
terminami dla dorosłego:

| zamiast | napisz |
|---|---|
| wybierz swoją strategię | zrób to, co ci pomaga · wybierz jeden sposób |
| kiedy usłyszysz sygnał | kiedy usłyszysz gwizdek · kiedy zadzwoni dzwonek |
| popatrz na instrukcję | popatrz na kartkę |
| kiedy zauważysz swój sygnał | kiedy poczujesz, że robi się trudno |
| licznik dojdzie do końca | zadzwoni minutnik |
| pokaż na termometrze | pokaż, jaki masz teraz kolor |
| wybierz dwie techniki | wybierz dwa sposoby pracy |

Jedno zdanie = jedna czynność; dwa krótkie zdania są lepsze niż jedno długie ze
spójnikiem. Nazwy przedmiotów stojących na stoliku (*minutnik*, *klepsydra*,
*pudełko*) zostają — dziecko uczy się ich jak każdego innego słowa.

Sprawdź to **przed nagraniem**. Poprawka po nagraniu kosztuje drugie nagranie,
a `sprawdz_fba.py` wypisuje polecenia z trudnymi słowami właśnie po to, żeby
zdążyć — razem z napisami na kartach do wycięcia, bo te dziecko też czyta
(`references/konspekt.md`, sekcja *Arkusz*). Poprawka napisu jest tania: nie jest
nagrany, więc kosztuje samą przebudowę dokumentu.

## Nagranie

Tylko jej sklonowanym głosem: `voice_id jq4ZUryuBeDqmtkKtBZ4`, model `eleven_v3`.
Rejestr aktorski jest ten sam co w całym projekcie:

| miejsce | wskazówka |
|---|---|
| otwarcie | `[warmly, smiling, telling a story to a small child]` |
| rozwinięcie | `[gently]` |
| domknięcie | `[with a smile]` |
| fragment smutny | zamiast dwóch ostatnich: `[gently, a little sad]`, `[softly]` |

Polecenie na kartę to jedno zdanie, więc wystarczy sam tag otwarcia. Tekst mówiony
ma być **czystą prozą**: bez wielokropków, bez sylabizowania, bez wtrąceń typu
„o tak". Ciepło daje wskazówka aktorska, nie interpunkcja — nagrania robione „na
wielokropkach" brzmią sztucznie i zostały odrzucone. Model
`eleven_multilingual_v2` czyta jej teksty lektorsko; do materiałów dla dzieci
tylko `eleven_v3`.

Po pobraniu z ElevenLabs zapisz plik jako `<wersja><kod>.mp3` i skompresuj:

```bash
python3 src/kompresuj_fba.py       # MP3 → 40 kbps mono, oryginał jako *.orig.mp3
```

Skrypt **pomija pliki, które mają już `*.orig.mp3`**. Po wgraniu nowej wersji
nagrania skasuj stary oryginał, inaczej kompresja przejdzie obok i dokument
zostanie ze starym dźwiękiem. Ta pułapka kosztowała już jedną rundę.

Nagrania są **danymi biometrycznymi** — `*.mp3` jest w `.gitignore` i tak zostaje.
Gdy pakujesz komplet dla kogoś z zewnątrz, powiedz jej o tym wprost.

## Zdjęcie pomocy

Generujemy modelem `gemini-2.5-flash-image`, w tej samej pastelowej konwencji co
ilustracje banku KPOF. Obrazek **z tekstem odrzucamy** — napis na pomocy dla
trzylatka nic nie znaczy, a model chętnie dopisuje angielskie słowa. Prompt
formułuj pozytywnie („każda karta jest pusta: jej powierzchnia to jeden
jednolity, jasny kolor"), bo zakaz „no text" działa gorzej niż opis tego, co ma
być.

```bash
python3 src/kompresuj_fba.py       # PNG → k_*.jpg, 900 px, jakość 84
```

Ta sama pułapka: po poprawieniu obrazka skasuj stary `k_*.jpg`.

## Sprawdzenie na koniec

```bash
python3 ../.claude/skills/cele-fba-pbs/scripts/sprawdz_fba.py
```

A gdy chcesz mieć pewność, że w nagraniu jest to, co miało być — przepisz je
z powrotem na tekst (`creative_transcribe_audio`) i porównaj z `POLECENIA`.
Wyłapuje to dwie rzeczy naraz: pomylony plik i wskazówkę aktorską wypowiedzianą
na głos zamiast zagraną.
