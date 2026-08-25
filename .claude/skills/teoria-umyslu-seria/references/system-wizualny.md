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

Wielkości: tekst 9,5 pt / interlinia 1,42; tabele 8,2 pt; karty ćwiczeń 8,3 pt;
nagłówek strony `h-sec` 16,5 pt; tytuł okładki 32 pt.

## Siatka strony

`.page` = 210 × 297 mm, `padding: 13mm 13mm 9mm`. Pole treści ≈ 184 × 275 mm.
`.page__body` to kolumna flex z odstępem 9 px; stopka `.page__foot` przykleja się do dołu.

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
