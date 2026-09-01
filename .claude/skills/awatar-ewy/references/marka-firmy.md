# Karta firmy — dane do stopek i plansz

Jedno miejsce na wszystko, co pojawia się w kadrze końcowym. Dzięki temu dziesiąty film
ma ten sam adres co pierwszy.

⚠️ Pozycje oznaczone `<do uzupełnienia>` **nie są znane**. Nie zgaduj ich i nie pomijaj
po cichu — wstaw w materiale widoczne miejsce i powiedz o brakach. Zły adres strony
w filmie, który idzie do dyrektorów, kosztuje więcej niż jedno pytanie.

## Autorka

- **Imię i nazwisko:** Mirosława Ewa Jurczyszyn
- **Tytuł:** mgr
- **Funkcja:** pedagog specjalny
- **Zapis w stopce:** `mgr Mirosława Ewa Jurczyszyn · pedagog specjalny`

W scenie otwierającej podpis idzie w dwóch wierszach — nazwisko białe półtłuste,
funkcja pod spodem mniejsza i pomarańczowa. **Nie każ awatarowi wypowiadać własnego
imienia i tytułu** — widz to czyta, a wypowiedzenie zjada pięć sekund i brzmi jak
prezentacja na konferencji.

## Firma

- **Pełna nazwa:** Pomorskie Centrum Terapii Pedagogicznej
- **Nazwa skrócona (stopki, wąskie kadry):** PCTP Koszalin
- **Skrót w logo:** PCTP
- **Adres:** `<do uzupełnienia — jeśli ma się pojawiać w materiałach>`

W stopce pełnego materiału (`wyklad`, `spot`) używaj **pełnej nazwy**. Skrótu
„PCTP Koszalin" tylko tam, gdzie brakuje miejsca — pełna nazwa mówi, czym firma
jest, skrót wymaga, żeby widz już wiedział.

## Kontakt

- **E-mail:** kontakt@eduplaner2026.pl
- **Telefon:** 662 888 403 — potwierdzony przez właścicielkę do użytku w materiałach.
  Numer bywa usuwany przez automatyczne czyszczenie danych osobowych; jeśli w plikach
  pojawi się `[usunięto]`, przywróć go stąd.
- **Strona internetowa:** `<do uzupełnienia — będzie wkrótce>`
- **Link do zamówienia (główne CTA):** `<do uzupełnienia — link albo QR>`

## Produkt

- **Nazwa:** EduPlaner 2026
- **Czym jest:** cyfrowa aplikacja gromadząca dokumentację placówki edukacyjnej
- **Metafora:** „cyfrowa szafa"
- **Hasła-klamry:** „Mniej dokumentów. Więcej edukacji." · „Cyfrowa szafa dla Twojej
  placówki" · „Odzyskaj czas dla dziecka i dla siebie" · „Otwarty projekt — współtwórz
  go z nami"

Pełny opis produktu, moduły i ton marki:
`.claude/skills/eduplaner-reklama/references/marka.md`.

## Identyfikacja wizualna

| Element | Wartość | Gdzie |
|---|---|---|
| Fiolet | `#2D1B69` | tło, nagłówki |
| Fiolet ciemny | `#1a0f42` | gradient |
| Pomarańcz | `#E8450A` | akcent, CTA, aktywny element |
| Font | Arial | wszędzie |
| Lawenda | `#D6CBEC` | strój i tło postaci `herbatka` (materiały dla rodziców) |
| Font zastępczy | Liberation Sans | środowiska bez Ariala — metrycznie zgodny, poprawne polskie znaki |

Lawenda nie jest dodatkiem — te odcienie są już na bocznych płatkach logo PCTP.
Dlatego strój dla rodziców w lawendzie zamyka klamrę: logo, bluzka i tło z jednej
rodziny. Jest przy tym dość jasna, żeby sylwetka odcinała się od ciemnego tła,
i dość chłodna, żeby nie kłócić się z pomarańczowym akcentem.

### Logo

**Znak:** okrągła pieczęć — fioletowe koło z jaśniejszą obwódką, w środku stylizowany
kwiat (trzy pomarańczowe płatki w górze, dwa fioletowe po bokach, biały środek, złota
łodyga rozchodząca się w trzy odnogi), pod nim **PCTP** białą szryftą szeryfową.

**Pliki — logo jest już w repozytorium. Nie proś właścicielki o wgranie go ponownie.**

| Ścieżka | Do czego |
|---|---|
| `.claude/skills/awatar-ewy/assets/logo-pctp.png` | **wzorzec skilla** — 1200×1200, RGBA, przezroczyste tło |
| `assets/logo-pctp.png` | kopia robocza, z której czyta `reklama/build_plansze.py` |

Gdyby kopia robocza gdzieś zniknęła, odtwórz ją jednym poleceniem:

```bash
cp .claude/skills/awatar-ewy/assets/logo-pctp.png assets/logo-pctp.png
```

Ten sam znak leży też w innych gałęziach repozytorium — m.in.
`.claude/skills/pctp-marka/assets/logo-pctp.png` (ten sam plik) oraz
`logo-pctp-znak.png` (sam kwiat, bez pieczęci i napisu).

⚠️ **Zanim poprosisz o wgranie jakiejkolwiek grafiki, przeszukaj repozytorium —
razem z gałęziami.** Ta lekcja kosztowała kilka rund rozmowy: logo leżało
w repozytorium od początku, na innej gałęzi, a ja prosiłem o wysyłanie go raz
za razem. Obrazek wklejony w rozmowie **widzę, ale nie ląduje na dysku** — więc
dopóki nie ma go w `git`, nie ma go wcale.

```bash
for b in $(git branch -r --format='%(refname:short)'); do
  git ls-tree -r "$b" | grep -iE "logo|\.png$|\.svg$"
done | awk '{print $3, $4}' | sort -u
```

Wynik daje hasze blobów — plik wyciąga się bez przełączania gałęzi:

```bash
git cat-file blob <hasz> > assets/logo-pctp.png
```

Logo jest **okrągłe i ciemnofioletowe**, więc na tle marki `#2D1B69` prawie znika.
Kładź je na jasnym polu albo z delikatną białą obwódką — nigdy wprost na fiolecie.
W planszach robi to reguła `.logo` w `build_plansze.py`: biały krążek
`rgba(255,255,255,.94)` z pięciopikselowym marginesem i cieniem. Bez niego
w kadrze zostaje sam kwiat, bez konturu pieczęci.

Gdyby pliku zabrakło, `build_plansze.py` cofa się do napisu **EDU**PLANER **2026**
w lewym górnym rogu i wraca do logo automatycznie — bez zmian w kodzie.

## Skład stopki według postaci

| Postać | Co w stopce |
|---|---|
| `wyklad` | pełna: firma · podpis · e-mail · strona |
| `warsztat` | skrócona: podpis · e-mail |
| `konsultacja` | minimalna: e-mail |
| `maks` | **żadnej** — dziecko nie jest odbiorcą kontaktu firmowego |
| `spot` | pełna + QR do zamówienia |
| `herbatka` | lekka: podpis · strona (bez telefonu, bez QR) |

## Wzorzec ekranu końcowego (spot)

```
            EduPlaner 2026
     Mniej dokumentów. Więcej edukacji.

        [QR / link do zamówienia]

  mgr Mirosława Ewa Jurczyszyn · pedagog specjalny
     kontakt@eduplaner2026.pl · <strona>
```

Hasło i QR pomarańczowe na fiolecie. Ekran zostaje 2 sekundy po ostatnim słowie,
w ciszy — widz potrzebuje chwili, żeby przepisać adres.

## Czego nie robić

- **Bez presji.** Nigdy „ostatnia szansa", „promocja kończy się", „tylko dziś".
  Odbiorcami są zapracowani profesjonaliści; nacisk odbiera wiarygodność szybciej,
  niż cokolwiek ją buduje.
- **Kontakt po wartości, nie zamiast niej.** Dane pojawiają się na końcu, gdy widz
  już wie, po co miałby zadzwonić.
- **Nie zmyślaj danych produktu.** Wszystko, czego nie ma tutaj ani w `marka.md`
  skilla `eduplaner-reklama`, dopytaj.
