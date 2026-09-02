# Karty pomocy dydaktycznej — treść, zdjęcie, nagranie

Karta pomocy to druk **KC-4**: jedna strona A4 przy konspekcie, w sekcji VII
(„Pokaż pomoc i posłuchaj polecenia”). Tam ich szuka nauczyciel i tam mają być.
Osobne zeszyty (`Pomoce_dydaktyczne_*.html`) to **dodatkowa** droga do druku
całego kompletu naraz, nie zamiennik.

## Gdzie dopisać

`src/pomoce_a.py` (3–4 lata), `pomoce_b.py` (5 lat), `pomoce_c.py` (6 lat),
`pomoce_u.py` (uzupełnienia). Wpis w słowniku `POMOCE`:

```python
"d1_01": ("D1-01", "Czarodziejski woreczek",
  # co przygotować — 4–5 pozycji, konkretnie, z materiałem i liczbą
  ["błyszczący woreczek ze sznurkiem ściągającym, nieprzezroczysty",
   "5 drobiazgów o wyraźnie różnej fakturze: szyszka, pompon, gładki koralik…",
   "mały dzwoneczek — sygnał otwarcia woreczka"],
  # trzy kroki użycia — dokładnie trzy, w kolejności
  ["Pokaż dziecku wszystkie przedmioty na tacy i nazwij każdy razem z nim.",
   "Schowaj jeden do woreczka przy dziecku, zadzwoń dzwoneczkiem.",
   "Dziecko wkłada rączkę i zgaduje po dotyku, zanim zajrzy."],
  # polecenie DO DZIECKA — to jest tekst, który przeczyta jej głos
  "Mam tu czarodziejski woreczek. Włóż do niego rączkę i poszukaj czegoś w środku.",
  # wskazówka dla nauczyciela
  "Nie podpowiadaj nazwy. Cisza po pytaniu jest częścią zadania."),
```

Klucz słownika (`d1_01`) jest nazwą plików mediów: `assets/pomoce_a/k_d1_01.jpg`
i `assets/audio_a/d1_01.mp3`. Musi być małymi literami, z podkreśleniem.

## Zdjęcie poglądowe

Pokazuje **jak ma wyglądać gotowa pomoc**, nie dziecko przy zabawie. Nauczyciel
patrzy na nie, kompletując materiały, więc na zdjęciu ma być dokładnie to, co
wymieniono w „co przygotować”, ułożone czytelnie na jednolitym tle.

Generuj `creative_generate_image`, model `gemini-2.5-flash-image`. Sprawdzony wzór:

> Photograph of preschool teaching aid materials laid out on a light wooden table,
> top-down view, soft daylight, neutral background. Items: `<lista z „co przygotować”>`.
> Everything clearly visible and separated. No people, no hands, no text, no labels.

Po pobraniu: `python3 src/kompresuj_media.py` (PNG → `k_*.jpg`, 760 px). Skrypt
**pomija pliki już przetworzone** — po poprawieniu zdjęcia skasuj stary
`k_*.jpg`, inaczej dokument dalej pokaże poprzednią wersję.

## Nagranie — tylko jej głosem

```
voice_id  jq4ZUryuBeDqmtkKtBZ4      (w panelu ElevenLabs: „Ewa-głos_do skils”)
model     eleven_v3
```

Zapasowe klony tego samego głosu: `D0Yz6dyyxHOodq3Zqi45`, `MxdHRlURUZPVY5h2NiXH` —
tylko gdy sama poprosi o zmianę brzmienia. **Nigdy nie nagrywaj jej materiałów
cudzym głosem.** Gdy głos jest niedostępny, oddaj sam tekst polecenia i zatrzymaj
się; nie podstawiaj głosu premade „do podglądu”.

Model `eleven_multilingual_v2` czyta jej teksty lektorsko — do materiałów dla
dzieci używaj `eleven_v3`.

### Rejestr — wypracowany i zaakceptowany wzorzec

| miejsce | wskazówka aktorska |
|---|---|
| otwarcie | `[warmly, smiling, telling a story to a small child]` |
| rozwinięcie | `[gently]` |
| domknięcie | `[with a smile]` |
| fragment smutny | zamiast dwóch ostatnich: `[gently, a little sad]`, `[softly]` |

Tekst mówiony ma być **czystą prozą**: pełne zdania, bez wielokropków, bez
sylabizowania („po-wo-lut-ku”), bez wtrąceń typu „o tak”. Ciepło daje wskazówka
aktorska, nie interpunkcja — nagrania robione „na wielokropkach” brzmią sztucznie
i zostały odrzucone.

Polecenie do dziecka to jedno–dwa zdania. Mówi, co dziecko ma zrobić, nie co
nauczyciel zamierza osiągnąć.

### Słowa, których przedszkolak nie rozumie

Polecenie pisz **prostymi, krótkimi zdaniami**. Nie używaj słów, które są
terminami dla dorosłego: *strategia*, *sygnał*, *instrukcja*, *sekwencja*,
*komunikat*, *procedura*, *technika*, *regulacja*. Nazwij to, co dziecko widzi
i słyszy w sali:

| zamiast | napisz |
|---|---|
| wybierz swoją strategię | wybierz jeden sposób · zrób to, co ci pomaga |
| kiedy usłyszysz sygnał | kiedy usłyszysz gwizdek · kiedy zadzwoni dzwonek |
| popatrz na instrukcję | popatrz na kartkę |
| kiedy zauważysz swój sygnał | kiedy poczujesz, że robi się trudno |
| licznik dojdzie do końca | zadzwoni minutnik |
| pokaż na termometrze | pokaż, jaki masz teraz kolor |

Jedno zdanie = jedna czynność. Dwa krótkie zdania są lepsze niż jedno długie
ze spójnikiem. Nazwy przedmiotów, które stoją na stoliku i dziecko ich dotyka
(*minutnik*, *klepsydra*, *pudełko*), zostają — dziecko uczy się ich jak każdego
innego słowa. Trudne słowa zostają tam, gdzie czyta je dorosły: w celu SMART,
w metodach, w trzech krokach użycia i we wskazówce dla prowadzącego.

## Kontrola

`sprawdz_bank.py` wypisuje karty bez zdjęcia i bez nagrania. Karta bez mediów nie
psuje budowania — dostaje pole zastępcze i znika przycisk odtwarzania. Właśnie
dlatego trzeba to sprawdzać skryptem, a nie oglądaniem dokumentu.

Nie wyjmuj kart z banku „dla rozmiaru”. Sprawdzone pomiarem: bank z kompletem
kart waży 12,3 MB i rysuje się w 348 ms; wolne otwieranie brało się z blokującego
arkusza fontów, nie z wagi pliku.
