# Pamięć projektu

## Głos użytkowniczki (narracja PL)

Mirosława Ewa Jurczyszyn ma **własny sklonowany głos** w ElevenLabs i to nim —
i wyłącznie nim — nagrywamy narrację do jej materiałów.

```
voice_id  jq4ZUryuBeDqmtkKtBZ4
nazwa     Ewa - narracja PL (PCTP)   (w panelu ElevenLabs: „Ewa-głos_do skils”)
model     eleven_v3
```

Zapasowe klony tego samego głosu: `D0Yz6dyyxHOodq3Zqi45` (Ewa1),
`MxdHRlURUZPVY5h2NiXH` (Ewa2) — używaj tylko, gdy poprosi o zmianę brzmienia.

**Nigdy nie nagrywaj jej materiałów cudzym głosem.** Gdy głos jest niedostępny,
oddaj sam scenariusz i zatrzymaj się — nie podstawiaj głosu premade.

### Rejestr narracji — wypracowany i zaakceptowany wzorzec

Ten sam zestaw wskazówek aktorskich w każdej ścieżce:

| miejsce | wskazówka |
|---|---|
| otwarcie | `[warmly, smiling, telling a story to a small child]` |
| rozwinięcie | `[gently]` |
| domknięcie | `[with a smile]` |
| fragment smutny | zamiast dwóch ostatnich: `[gently, a little sad]`, `[softly]` |

Tekst mówiony ma być **czystą prozą** — pełne zdania, bez wielokropków, bez
sylabizowania („po-wo-lut-ku”), bez wtrąceń typu „o tak”. Ciepło daje wskazówka
aktorska, nie interpunkcja; nagrania robione „na wielokropkach” brzmią sztucznie
i zostały odrzucone. Model `eleven_multilingual_v2` czyta jej teksty
lektorsko — do materiałów dla dzieci używaj `eleven_v3`.

### Skąd to brać

* skill **`dane-i-glos`** — pełny łańcuch dane → scenariusz → MP3 + SRT → wideo;
  pamięta ten `voice_id` na stałe (`scripts/konfiguracja.py`, `PAMIEC_TRWALA`)
* podgląd tego, co skill pamięta:
  `python3 .claude/skills/dane-i-glos/scripts/skonfiguruj_glos.py --pokaz`
* zmiana głosu: `... skonfiguruj_glos.py --voice-id <nowy> --nazwa "..."`
* narzędzia MCP ElevenLabs: `creative_generate_speech` z tym `voice_id`
* klucz API tylko w zmiennej `ELEVENLABS_API_KEY` — nigdy w repozytorium

## Podstawa programowa wychowania przedszkolnego (obowiązująca)

**Rozporządzenie Ministra Edukacji z 11 marca 2026 r.** (Dz. U. 2026 poz. 378),
w życie **1 września 2026 r.** Zastąpiło cztery dotychczasowe obszary rozwoju
(fizyczny, emocjonalny, społeczny, poznawczy) **dziewięcioma obszarami osiągnięć
dziecka**:

| nr | obszar | nr | obszar | nr | obszar |
|---|---|---|---|---|---|
| 1 | społeczny | 4 | matematyczny | 7 | cyfrowy |
| 2 | osobisty | 5 | przyrodniczy | 8 | artystyczny |
| 3 | językowy | 6 | techniczny | 9 | ruchowy |

Zapis punktu: `obszar.punkt` (np. `3.5`). Poza tym występują kody `DE-R`
(doświadczenie edukacyjne realizowane co najmniej raz w roku), `WSR` (warunki
i sposób realizacji) oraz `Zad.` (zadanie przedszkola).

Punkt ciężkości przesunięty z tego, co dziecko ma umieć, na to, jak działa
i funkcjonuje — kompetencje fundamentalne i przekrojowe, sprawczość, dobrostan.
Dziewięć obszarów to mapa do planowania, nie plan zajęć: jedna dobrze
zaprojektowana sytuacja edukacyjna uruchamia zwykle kilka naraz.

**To jest obowiązująca podstawa — nie odwołuj się do rozporządzenia z 14 lutego
2017 r.** Nazwy obszarów potwierdzone z opracowań branżowych; dziennikustaw.gov.pl
i gov.pl są zablokowane przez proxy, więc numeracji punktów co do jednego nie
zweryfikowano — przy rozbieżności pyta się o załącznik do rozporządzenia.

Miejsce w kodzie: `OBSZAR_PP_NAZWY` w `monitoring_podstawy()`
(`eduplaner_przedszkole/src/build.py`) — jedno źródło dla legendy i kolumny tabeli.

## Materiały przedszkolne

`eduplaner_przedszkole/` — bank celów SMART KPOF, 130 konspektów, pomoce
dydaktyczne. Szczegóły: `eduplaner_przedszkole/README.md`.

Ilustracje do konspektów generujemy modelem `gemini-2.5-flash-image`
(`creative_generate_image`) — spójny styl książeczkowy, pastelowa paleta,
ta sama bohaterka w całej historyjce.
