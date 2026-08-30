# Jak pisać pod polskiego lektora

Tekst czytany rządzi się innymi prawami niż tekst czytany oczami. Słuchacz nie może cofnąć
wzroku, nie widzi tabeli, nie zna kontekstu. Poniższe zasady wynikają wprost z tych ograniczeń.

## Tempo i długość

| Długość nagrania | Liczba słów | Kiedy |
|---|---|---|
| 30 s | ~75 | wstawka do rolki, jedna liczba |
| 60 s | ~150 | podsumowanie dla rodziców, post |
| 90 s | ~225 | raport dla dyrekcji |
| 3 min | ~450 | omówienie całego zestawu danych |
| powyżej 5 min | ~750+ | tylko gdy słuchacz ma powód słuchać do końca |

Licz słowa przed generowaniem. Jeśli użytkowniczka podała czas trwania, dopasuj tekst do
tabeli powyżej, zamiast generować i sprawdzać po fakcie.

## Liczby zapisuj tak, jak się je czyta

Silniki TTS czytają polskie liczebniki niepewnie — zwłaszcza odmianę przez przypadki,
ułamki dziesiętne i daty. Rozpisuj je słowami w scenariuszu:

| Zamiast | Napisz |
|---|---|
| `87,5%` | osiemdziesiąt siedem i pół procent |
| `2026` (rok) | dwa tysiące dwudziesty szósty |
| `1 240 zł` | tysiąc dwieście czterdzieści złotych |
| `3/4` | trzy czwarte |
| `12 uczniów` | dwunastu uczniów |
| `nr 5` | numer piąty |
| `godz. 8:30` | ósma trzydzieści |
| `ok. 2×` | około dwa razy |

Zaokrąglaj bez litości: „osiemdziesiąt siedem i pół procent" słucha się dobrze,
„osiemdziesiąt siedem przecinek czterdzieści osiem procent" — nie. Dokładna wartość zostaje
w pliku z danymi, do którego słuchacz zawsze może zajrzeć.

## Zdania

- **Maksymalnie 20 słów.** Dłuższe rozbij na dwa.
- **Jedna myśl na zdanie.** Bez wtrąceń w nawiasach i myślnikach.
- **Szyk prosty**: podmiot, orzeczenie, dopełnienie. Bez inwersji „literackiej".
- **Strona czynna**: „zespół objął wsparciem dwanaścioro dzieci", nie „dwanaścioro dzieci
  zostało objętych wsparciem".
- **Bez skrótów** czytanych literami, jeśli nie są powszechne: rozpisz „Poradnia
  Psychologiczno-Pedagogiczna", nie „PPP".

## Czego nigdy nie pisać

- odwołań wizualnych: „jak widać w tabeli", „poniższy wykres", „w kolumnie trzeciej",
- zapisów technicznych: `NULL`, `n/d`, nazw kolumn z podkreśleniami,
- liczb, których nie ma w profilu danych — żadnych szacunków „mniej więcej",
- pytań retorycznych piętrowo („Czy to dużo? A może mało? Zobaczmy."),
- wyliczeń dłuższych niż trzy elementy — słuchacz zapamięta najwyżej trzy.

## Struktura, która działa

1. **Haczyk** (1 zdanie) — najmocniejsza liczba albo najważniejszy wniosek, od razu.
2. **Kontekst** (2–3 zdania) — czego dotyczą dane, z jakiego okresu, ilu osób.
3. **Kluczowe liczby** (3–5 zdań) — po jednej liczbie na zdanie, od najważniejszej.
4. **Wniosek** (1–2 zdania) — co z tego wynika i co dalej.

Przykład (dane: 24 uczniów, średnia frekwencja 91,3%, 3 uczniów poniżej 70%):

> Frekwencja w tej grupie wynosi ponad dziewięćdziesiąt procent.
>
> Dane obejmują dwadzieścioro czworo uczniów w pierwszym półroczu.
> Liczyliśmy obecność na wszystkich zajęciach specjalistycznych.
>
> Średnia frekwencja to dziewięćdziesiąt jeden procent.
> Troje uczniów opuściło ponad trzydzieści procent zajęć.
> To ta sama trójka, która w listopadzie zmieniła grupę.
>
> Warto porozmawiać z rodzicami tych trojga dzieci przed feriami.

## Pauzy i oddech

Pusta linia w scenariuszu to naturalna pauza — używaj jej między sekcjami.
Dla precyzyjnej kontroli wstaw `<break time="0.7s" />` (modele `eleven_v3`
i `eleven_multilingual_v2`). Nie przekraczaj trzech sekund i nie stawiaj więcej niż
jednej pauzy na akapit — nagromadzone brzmią sztucznie.

## Ton pod odbiorcę

| Odbiorca | Ton | Czego unikać |
|---|---|---|
| dyrekcja | rzeczowy, wnioski na początku | emocji, opisu metody |
| rodzice | ciepły, konkretny, bez żargonu | terminów diagnostycznych, porównań między dziećmi |
| zespół | roboczy, szczegółowy | ogólników, „ładnych" podsumowań |
| własne notatki | skrótowy, hasłowy | pełnych zdań grzecznościowych |

## Zanim wygenerujesz audio

Przeczytaj scenariusz na głos w myślach. Jeśli gdziekolwiek zabraknie ci oddechu
albo potkniesz się na liczbie — popraw tekst, nie ustawienia głosu.

## Rejestr dla materiałów dla dzieci — wzorzec zaakceptowany

Wypracowany przy historyjce obrazkowej „Jak rośnie kwiatek" (konspekt C1-01,
6 lat) i przyjęty jako obowiązujący dla wszystkich nagrań dla dzieci.

Model: **`eleven_v3`**. `eleven_multilingual_v2` czyta te teksty lektorsko —
poprawnie, ale bez ciepła; do dzieci się nie nadaje.

Wskazówki aktorskie w nawiasach kwadratowych, ten sam zestaw w każdej ścieżce:

| miejsce w ścieżce | wskazówka |
|---|---|
| otwarcie | `[warmly, smiling, telling a story to a small child]` |
| rozwinięcie | `[gently]` |
| domknięcie | `[with a smile]` |
| fragment smutny | zamiast dwóch ostatnich: `[gently, a little sad]`, `[softly]` |

### Czysta proza — najważniejsza zasada

Tekst mówiony to pełne zdania. **Bez** wielokropków, **bez** sylabizowania
(„po-wo-lut-ku"), **bez** wtrąceń typu „o tak". Pierwsza wersja nagrań powstała
właśnie tak — z ciepłem wymuszanym interpunkcją — i została odrzucona jako
sztuczna. Ciepło daje wskazówka aktorska, nie zapis.

```
✗ Wsypała ziemię i ostrożniutko... o tak... włożyła nasionko.
✓ Wsypała do doniczki ziemię i ostrożnie włożyła nasionko do środka.
```

### Struktura nagrania do historyjki obrazkowej

Osobna ścieżka na każdy element, nie jedno długie nagranie — nauczycielka
odtwarza sceny pojedynczo albo w sekwencji:

1. wprowadzenie — zaproszenie do słuchania i zapowiedź zadania
2. po jednej ścieżce na scenę (2–3 zdania, 11–15 s)
3. zakończenie — pytania otwarte sprawdzające rozumienie przyczyny i skutku
