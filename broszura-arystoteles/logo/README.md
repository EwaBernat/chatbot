# Znaki w broszurze

W broszurze pracują **dwa znaki** i pełnią różne role:

| Znak | Rola | Gdzie |
|---|---|---|
| **PCTP** | wydawca | okładka (dół), strona tytułowa, strona redakcyjna, tylna okładka |
| **Mała Filozofia** | seria | okładka (góra), strona tytułowa, żywa pagina każdej strony, tylna okładka |

---

# Znak wydawcy — PCTP

`pctp-logo.svg` · `pctp-logo.png`

> **Uwaga: to odrysowanie.** Plik nie trafił na dysk sesji, więc znak został odtworzony
> wektorowo z przesłanego obrazka: fioletowy krążek z jaśniejszą obwódką, kwiat
> o pięciu płatkach (dwa lawendowe, dwa łososiowe, jeden pomarańczowy), biały środek,
> złote łodyżki, napis PCTP krojem szeryfowym Tinos Bold zamienionym na krzywe.
> Kolory zostały pobrane z obrazka: `#3B2270`, `#4E3288`, `#A98FCB`, `#F0A268`,
> `#E8722C`, `#C6A02A`, `#F5EFE4`.
>
> **Przed drukiem podmień ten plik na oryginał** — nadpisz `logo/pctp-logo.svg`
> (albo wgraj `pctp-logo.png` w wysokiej rozdzielczości) i uruchom ponownie
> `python3 zrodla/build.py` oraz `python3 zrodla/druk.py`. Skład sam wciągnie nową wersję.
> Jeśli oryginał jest w innym formacie niż SVG, wystarczy zachować nazwę pliku.

Wielkość w broszurze: 14–20 mm średnicy. Na okładce i tylnej okładce znak stoi
obok pola na pełną nazwę, adres i stronę internetową — te miejsca zostały zostawione
puste do uzupełnienia.

---

# Znak serii „Mała Filozofia”

## Pliki

| Plik | Zastosowanie |
|---|---|
| `mala-filozofia-znak.svg` | Sam znak, kolorowy. Awatar, favikona, stempel na grzbiecie. |
| `mala-filozofia-znak-mono.svg` | Sam znak w jednym kolorze (`currentColor`). Tłok, grawer, druk 1-kolorowy. |
| `mala-filozofia-logo-poziome.svg` | Znak + napis obok. Wersja podstawowa. |
| `mala-filozofia-logo-poziome-mono.svg` | To samo, jednokolorowe. |
| `mala-filozofia-logo-pionowe.svg` | Znak nad napisem. Wąskie miejsca, media społecznościowe. |
| `*.png` | Wersje rastrowe z przezroczystym tłem (znak 512 px, logo 1200 px). |

Napis jest **zamieniony na krzywe** — pliki wyglądają tak samo na każdym komputerze,
bez instalowania krojów.

## Znaczenie

Pytajnik w otwartym wieńcu. Wieniec oliwny to Grecja i Arystoteles; przerwa u góry mówi,
że wieniec nie jest zamknięty — pytanie zostaje otwarte. Kropka pytajnika jest oliwką
w kolorze szafranu: to ten sam akcent, którym w broszurze oznaczone są sekcje
„W Twoim życiu”.

## Kolory

| Element | HEX | CMYK (orientacyjnie) |
|---|---|---|
| Wieniec i pytajnik | `#1E5A6B` | 82 / 47 / 38 / 24 |
| Kropka | `#B07E13` | 27 / 51 / 100 / 12 |
| Liście | `#5C7A49` | 65 / 33 / 84 / 20 |
| Napis „MAŁA” | `#1F2E33` | 78 / 57 / 51 / 51 |
| Napis „FILOZOFIA” | `#1E5A6B` | 82 / 47 / 38 / 24 |

## Zasady użycia

- **Pole ochronne:** dookoła znaku zostaw wolne miejsce równe średnicy kropki pytajnika.
- **Minimalny rozmiar:** znak 6 mm, logo poziome 25 mm szerokości. Poniżej tych wartości
  liście przy druku zlewają się w plamę — użyj wtedy wersji jednokolorowej.
- **Tło:** znak działa na jasnym tle papieru i na ciemnym (wersja mono dziedziczy kolor tekstu).
  Nie umieszczaj go na zdjęciu bez jednolitego podkładu.
- **Nie wolno:** rozciągać, zmieniać proporcji, obracać, dodawać cienia ani obrysu,
  zmieniać kolorów na spoza palety, rozdzielać znaku od napisu w wersji poziomej.

## Gdzie występuje w broszurze

Okładka (góra z lewej) · strona tytułowa (nad tytułem) · strona redakcyjna (przy metryce) ·
żywa pagina każdej strony rozdziału · tylna okładka.

## Podmiana plików

Wszystkie znaki wciąga skład z tego katalogu — wystarczy nadpisać plik, zachowując nazwę,
i uruchomić:

```
python3 zrodla/build.py
python3 zrodla/druk.py
```

`build.py` zamienia w plikach serii kolory `#1E5A6B`, `#B07E13`, `#5C7A49` i `#1F2E33`
na tokeny palety broszury; kolory spoza tej listy (czyli cała paleta PCTP) zostają
nietknięte. Powtarzające się identyfikatory w SVG są automatycznie numerowane,
więc ten sam plik można wstawić na kilku stronach bez konfliktu gradientów.
