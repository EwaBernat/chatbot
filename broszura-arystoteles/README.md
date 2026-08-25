# Spotkanie z Arystotelesem — seria „Mała Filozofia”, tom 1

Broszura edukacyjna dla młodzieży w spektrum autyzmu. Opowiadanie o życiu i ideach
Arystotelesa, prowadzące przez dwanaście emocji, z pytaniami do samodzielnej pracy.

## Pliki

| Plik | Do czego służy |
|---|---|
| `broszura.html` | Wersja źródłowa (do publikacji online / jako Artifact). Kroje ładowane z Google Fonts. |
| `do-druku.html` | Wersja samodzielna: kroje osadzone w pliku, działa bez internetu. Z niej powstaje PDF. |
| `Spotkanie-z-Arystotelesem.pdf` | Gotowy plik do druku — A4, 44 strony. |

Aby wygenerować PDF ponownie: otwórz `do-druku.html` w przeglądarce → Drukuj → Zapisz jako PDF
(format A4, marginesy domyślne, grafika tła włączona).

## Zawartość

- **450 zdań** opowiadania — dokładnie tyle, w akapitach po jednym zdaniu.
- **60 pytań** — po 5 na każdy z 12 rozdziałów, numerowane ciągiem 1–60.
- **8 infografik** + 12 ilustracji rozdziałowych (wektorowe SVG, skalują się bez utraty jakości).
- 12 haseł Arystotelesa, karta emocji do wycięcia, słowniczek, nota o cytatach.

### Struktura rozdziału (stała, nigdy się nie zmienia)

1. **Scena** — 14 zdań opowiadania z życia Arystotelesa.
2. **Myśl Arystotelesa** — 10 zdań; wcześniej cytat w ramce.
3. **Emocja** — 7 zdań; nazwa emocji + opis sygnałów z ciała.
4. **W Twoim życiu** — 6 zdań; zwykła, codzienna sytuacja.
5. **Pięć pytań** — bez ocen, bez złych odpowiedzi.

### Dwanaście spotkań

| Nr | Tytuł | Emocja | Pytania |
|---|---|---|---|
| 1 | Chłopiec w domu lekarza | ciekawość | 1–5 |
| 2 | Pierwszy dzień w Atenach | niepewność | 6–10 |
| 3 | Nie zgadzam się z nauczycielem | napięcie sporu | 11–15 |
| 4 | Ośmiornica w porcie Lesbos | zachwyt | 16–20 |
| 5 | Lekcja dla trudnego ucznia | duma | 21–25 |
| 6 | Szkoła, w której się chodzi | ulga | 26–30 |
| 7 | Waga w środku | strach | 31–35 |
| 8 | Sto razy to samo | zniechęcenie | 36–40 |
| 9 | Trzy rodzaje przyjaciół | samotność | 41–45 |
| 10 | Gniew, który ma miarę | gniew | 46–50 |
| 11 | Jedna jaskółka | nadzieja | 51–55 |
| 12 | Ostatnia droga do Chalkis | smutek i wdzięczność | 56–60 |

## Decyzje projektowe (i dlaczego takie)

**Dostępność dla czytelnika w spektrum**
- Krój tekstu: **Atkinson Hyperlegible** — zaprojektowany przez Braille Institute dla osób
  z trudnościami w czytaniu; litery o łatwo rozróżnialnych kształtach, przekreślone zero.
- Wielkość: **12,8 pt** w druku, interlinia 1,65 — powyżej typowej broszury.
- **Jedno zdanie w jednym akapicie** — oko nie gubi wiersza, można zatrzymać się w dowolnym miejscu.
- Tło **kość słoniowa #EFEBE2**, nie biel — mniej odbija światło, mniej męczy wzrok.
- Tekst **#1F2E33**, nie czysta czerń — niższy kontrast twardy, nadal ponad WCAG AAA.
- Język dosłowny: bez ironii, bez przenośni bez wyjaśnienia, bez pytań podchwytliwych.
- Emocje opisane przez **sygnały z własnego ciała**, nie przez mimikę innych osób.
- Formy gramatyczne neutralne płciowo albo podane w obu wariantach.
- Powtarzalna struktura pięciu kroków — czytelnik zawsze wie, co będzie dalej.

**Typografia**
- Nagłówki: **Alegreya Sans ExtraBold** (humanistyczny, ciepły, o literackim rodowodzie).
- Tekst: **Atkinson Hyperlegible Regular / Bold**.
- Obydwa kroje są darmowe (SIL Open Font License) i dostępne w Google Fonts oraz w Canvie.

**Paleta**

| Rola | HEX | Gdzie |
|---|---|---|
| Papier (kamień) | `#EFEBE2` | tło całości |
| Karta | `#F8F6F0` | tło rozdziałów |
| Atrament | `#1F2E33` | tekst |
| Morze egejskie | `#1E5A6B` | kolor wiodący, numery rozdziałów, cytaty |
| Szafran | `#C8901E` | akcent, sekcja „W Twoim życiu” |
| Oliwka | `#63804F` | sekcja „Emocja” |
| Glina | `#B0603F` | sekcja „Pięć pytań” |

Każda z czterech sekcji rozdziału ma własny kolor i własny kształt ramki
(pełna / kreskowana / pasek z lewej / obwódka) — rozpoznaje się je także bez czytania nagłówka
i po wydruku czarno-białym.

## Przygotowanie do druku

- **Format:** A4 pionowo, druk dwustronny, 44 strony.
- **Marginesy:** 15 mm boczne, 14 mm górny, 16 mm dolny.
- **Spady:** do offsetu dodaj 3 mm z każdej strony + pasery.
- **Papier:** offset lub matowa kreda 120–150 g. Matowy nie odbija światła.
- **Oprawa:** zeszytowa (zszywki) albo klejona; przy zeszytowej liczba stron musi być
  wielokrotnością 4 — dodaj stronę redakcyjną lub pustą stronę na notatki.
- **Okładka:** karton 250–300 g, folia matowa.

## Odtworzenie w Canvie / InDesignie

1. Canva → szablon **„Educational Brochure A4”** albo **„Workbook A4”**.
2. Ustaw w Zestawie marki kolory z tabeli powyżej i oba kroje (są w bibliotece Canvy).
3. Przenieś rozdziały pojedynczo — jeden rozdział to jedna lub dwie strony.
4. Infografiki: eksportuj z `do-druku.html` (prawy przycisk na grafice → zapisz obraz)
   albo wklej kod SVG bezpośrednio w InDesignie / Illustratorze.
5. Nie zmniejszaj stopnia pisma poniżej 12 pt — to element dostępności, nie estetyki.

## Nota o cytatach

Zdania z rozdziałów 1, 4, 6, 7, 8, 9, 10 i 11 pochodzą z zachowanych dzieł Arystotelesa
(„Metafizyka”, „O częściach zwierząt”, „Etyka nikomachejska”) w uproszczonym przekładzie.
Zdania z rozdziałów 2, 3, 5 i 12 to myśli przypisywane mu przez późniejszych autorów —
zaznaczono to pod każdym z nich. Sceny są opowiadaniem: fakty biograficzne są prawdziwe,
dialogi napisano na potrzeby tej broszury.

## Licencje krojów

Atkinson Hyperlegible — SIL OFL 1.1, Braille Institute of America.
Alegreya Sans — SIL OFL 1.1, Huerta Tipográfica.
Oba można legalnie osadzać w plikach i wykorzystywać komercyjnie.
