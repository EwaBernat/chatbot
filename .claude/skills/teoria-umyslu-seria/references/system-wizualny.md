# System wizualny serii

Wszystkie wartości są już zapisane w `assets/szablon.html`. Ten plik wyjaśnia,
**dlaczego** są takie, żebyś przy rozbudowie nie zepsuł spójności serii.

## Paleta

Trzy filary mają stałe kolory i to jest nośnik informacji, nie dekoracja — czytelniczka
po samym kolorze paska rozpoznaje, o którym filarze mowa. Nie zamieniaj ich rolami.

| Rola | Zmienna | Nasycony | Pastelowe tło | Obramowanie |
|---|---|---|---|---|
| TUE — emocje | `--tue` | `#C4547A` | `--tue-soft` `#FBE7EE` | `--tue-mid` `#F2C9D8` |
| TUK — przekonania | `--tuk` | `#6553A8` | `--tuk-soft` `#EBE5F8` | `--tuk-mid` `#D3C8EE` |
| TUS — działanie | `--tus` | `#0E8B78` | `--tus-soft` `#DDF0EC` | `--tus-mid` `#B5DED6` |
| Akcent / ostrzeżenie | `--gold` | `#A07A0A` | `--gold-soft` `#FBF1D6` | `--gold-mid` `#F0DFA6` |

Tekst: `--ink` `#2E2A3B`, `--ink2` `#57516B`, `--muted` `#8B849D`.
Papier: `--paper` `#FFFFFF`, tło ekranu `--ground` `#EFE9E2`, linie `--line` `#E7DFD5`.

**Czwórka nasyconych kolorów przeszła walidację** pod kątem kontrastu do podłoża
i rozróżnialności przy daltonizmie (protanopia, deuteranopia, tritanopia). Jeśli dokładasz
piąty kolor serii na wykresie — przewaliduj zestaw, zamiast dobierać na oko.
Kolejność sąsiedztwa ma znaczenie: sprawdzony porządek na wykresie kołowym to
różowy → złoty → fioletowy → zielony.

## Typografia

- **Fraunces** — nagłówki, liczby na wykresach kołowych, numery kroków. Szeryfowy krój
  o miękkim rysunku: nadaje materiałowi ton poradnika, a nie ulotki reklamowej.
- **Nunito Sans** — tekst ciągły, tabele, etykiety. Wysoka czytelność przy 8–9 pt,
  a przy tej gęstości treści schodzimy nisko.
- Oba kroje są **osadzone w pliku jako base64** (podzbiory latin + latin-ext, ok. 660 KB).
  Dzięki temu broszura drukuje się identycznie bez internetu — w szkole to nie jest luksus.

### Skala pisma — obowiązująca od wydania 3 części 2B

Pierwsze wydania serii były składane za drobno; autorka zgłosiła, że **trudno się to czyta**.
Skala została podniesiona o ok. 16% dla tekstu poniżej 10 pt i o 10% dla 10–14 pt.
**To jest obecny standard serii — nie wracaj do poprzednich wartości, nawet gdy strona
nie chce się zmieścić.** Gdy treści jest za dużo, dodaje się stronę, a nie zmniejsza pismo.

| Element | Selektor | Wielkość |
|---|---|---|
| tekst ciągły | `body` | **11 pt** / interlinia 1,42 |
| lead pod nagłówkiem | `.lead` | 11,1 pt |
| tabele | `table` | 9,5 pt |
| tabela spotkań | `.spotk` | 9,2 pt |
| karty ćwiczeń i scenariuszy | `.ex__body` | 9,5 pt |
| opowiadania | `.opow` | 10,2 pt |
| etykiety wersalikowe | `.kicker`, `.ex__body b` | 8–9,3 pt |
| najdrobniejszy dopuszczalny tekst | — | **7,7 pt** (nigdy mniej) |
| nagłówek strony | `.h-sec` | 17,2 pt |
| tytuł okładki | `.cover__title` | 33,3 pt |

Miejsce odzyskuje się **na strukturze, nie na piśmie**: `padding` strony 12/12/8 mm,
odstęp `.page__body` 7 px, `.card` 7px 10px, `.grid` 7 px. Gdy to nie wystarcza,
oznacz stronę klasą `.page--zw` (zagęszczenie lokalne: mniejsze odstępy i wyściółki,
bez ruszania stopnia pisma) albo przenieś blok na nową stronę.

## Wzmocnienia wprowadzone w wydaniu 3

- **Tabele.** Nagłówki w `--ink` (nie `--ink2`), kreska pod nagłówkiem 2 px,
  linie wierszy `#E4DBD0`, pas naprzemienny `#F8F2EA`. Tabela nie dostaje ramki
  zewnętrznej — stoi w karcie, która już ją ma.
- **Karty scenariuszy `.ex`.** Ramka 1,6 px w kolorze modułu z delikatnym cieniem,
  kreska 1,4 px pod nagłówkiem, tytuł 12,2 pt w kolorze modułu, numer w wypełnionym
  kaflu (biała cyfra na kolorze), etykiety `CEL / MATERIAŁY / PRZEBIEG` w kolorze modułu.
  Kolor podaje się przez `--rail` w klasach `.ex--tue`, `.ex--tuk`, `.ex--tus`.
- **Opowiadania `.opow`.** Tło i ramka w kolorze modułu (`.opow--tue/tuk/tus`),
  lewa krawędź 4 px, tytuł w kolorze modułu, a blok pytań `.pyt` na **białym** tle,
  żeby odciął się od podświetlonego opowiadania.

## Siatka strony

`.page` = 210 × 297 mm, `padding: 12mm 12mm 8mm`. Pole treści ≈ 186 × 277 mm.
`.page__body` to kolumna flex z odstępem 7 px; stopka `.page__foot` przykleja się do dołu.

W druku `.page` dostaje `height: 296.4 mm` i `overflow: hidden` — o 0,6 mm mniej niż arkusz,
bo równe 297 mm powodowało, że zaokrąglenie subpikselowe wypychało co drugą stronę na pustą
kartkę (18 stron drukowało się jako 35).

Układy: `.g2`, `.g3`, `.g-2-1` (szersza lewa), `.g-1-2` (szersza prawa).
Poniżej 820 px szerokości ekranu wszystko przechodzi w jedną kolumnę — to tryb podglądu
na telefonie, nieistotny dla druku, ale **psuje pomiary**, jeśli mierzysz w wąskim oknie.

## Pułapka, która kosztowała najwięcej: kolizje nazw klas

Arkusz jest wspólny dla całego dokumentu, więc krótka nazwa klasy użyta w nowym komponencie
potrafi odziedziczyć style z zupełnie innego miejsca. W części 1 komórki tabeli dostały klasę
`ex` — tę samą, co karty ćwiczeń — i przejęły po nich ramkę oraz `display:flex`,
przez co w tabeli pojawiły się prostokąty nie wiadomo skąd.

Zanim nazwiesz nową klasę, sprawdź, czy nie jest zajęta:

```bash
grep -o 'class="[^"]*"' broszura.html | tr ' ' '\n' | sort -u | head -60
```

Zajęte i mające własne style: `page`, `cover`, `card`, `callout`, `ex`, `tag`, `grid`,
`legend`, `toc`, `poz`, `czesc`, `karta`, `box`, `sc`, `nt`, `lp`, `nm`, `grp`, `it`,
`alt`, `suma`, `linia`, `pole`, `wynik`, `podpis`, `krok`, `dok`, `blad`, `seria`, `skroty`.

## Elementy stałe serii

- **Logo PCTP** — symbol SVG `#pctp` w `<defs>` na początku pliku, wstawiany przez
  `<svg><use href="#pctp"></use></svg>`. Fioletowy krążek z kwiatem i napisem PCTP.
- **Grafika okładki** — trzy pastelowe kule w kolorach filarów, schodzące ku dołowi
  jak dymki myśli. Kule wychodzą poza prawą krawędź (`right: -10mm`), co daje okładce
  oddech i wrażenie kadru, a nie naklejki.
- **Pasek serii** — `.seria` z etykietą „Seria: Teoria umysłu" i plakietką numeru części.
- **Stopka bieżąca** — po lewej temat strony, po prawej numer w kroju Fraunces.

## Wykresy i grafiki SVG — pułapka skali

Tekst w SVG skaluje się razem z grafiką. Jeśli `viewBox` jest szerszy niż miejsce,
w którym grafika faktycznie ląduje, wszystkie podpisy zmaleją proporcjonalnie —
`font-size="11"` w `viewBox="0 0 640 …"` renderowanym na szerokości 372 px daje
realne **6,4 px ≈ 4,8 pt**, czyli tekst nieczytelny w druku.

**Zasada:** projektuj `viewBox` w skali 1:1 ze szerokością renderowania.
Zmierz ją najpierw w przeglądarce:

```js
document.querySelector('svg.chart').getBoundingClientRect().width
```

Typowe szerokości przy marginesie strony 12 mm (obszar treści ≈ 703 px):
- pełna szerokość strony — ok. 700 px
- kolumna `g-2-1` (szersza) — ok. 372 px w karcie `.fig-card`
- kolumna `g2` — ok. 344 px

Przy skali 1:1 stosuj: podpisy wierszy `font-size="12"`, etykiety w słupkach `"11"`,
opisy pomocnicze `"10"` (≈ 9, 8,3 i 7,5 pt).

## Karta wykresu `.fig-card`

Wykres nigdy nie stoi „goły" na stronie — otacza go karta w tym samym języku,
co pozostałe bloki:

```css
.fig-card{background:#fff; border:1.4px solid var(--line); border-radius:14px;
  padding:9px 13px 10px; gap:7px;
  box-shadow:0 1px 0 rgba(46,42,59,.04), 0 5px 13px rgba(46,42,59,.05)}
.fig-card .fig-title{display:block; padding-bottom:6px; border-bottom:1px solid var(--line2)}
.fig-card figcaption{border-top:1px dashed var(--line); padding-top:6px; margin-top:1px}
```

Same słupki dostają własną ramkę (tor): zaokrąglony `rect` z `fill="#FCF9F5"`
i `stroke="#D9CFC2" stroke-width="1.4"`, a segmenty wstawione do środka
z odstępem 4 px. Przy wykresie skumulowanym do 100% tor jest zasłonięty
przez segmenty — dlatego liczy się właśnie ten 4-pikselowy margines,
bo to on tworzy widoczną rameczkę.
