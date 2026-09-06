---
name: eduplaner-sklep
description: Praca nad serwisem sprzedażowym eduplaner2026.pl (PCTP Koszalin) — oferta, umowa subskrypcji, backend sklepu i wdrożenie. Uruchamiaj ZAWSZE przy zadaniach dotyczących tego serwisu: „dodaj broszurę / szkolenie / pomoc dydaktyczną do oferty", „zmień cenę", „podłącz formularz zamówienia", „koszyk", „płatności online", „Przelewy24 / Stripe", „zapis zamówień", „wystaw stronę na serwer", „publikacja", „domena", „co jeszcze trzeba zrobić przed sprzedażą". Wyzwalaj także przy: umowa subskrypcji, protokół zdawczo-odbiorczy, numer licencji, klucz aktywacyjny, faktura, KSeF, wFirma, nabywca i odbiorca faktury, biała lista VAT, dane rejestrowe PCTP, zabezpieczenie broszur i nagrań, znak wodny w PDF, wygasające linki do pobrania, ochrona filmów przed pobraniem, adresy produktowe zamiast hasza. Wyzwalaj przy pytaniach o strukturę tego kodu: OFERTA, FILMY, EKRANY, build_single.py, panel filmów. Nie używaj do samych dokumentów edukacyjnych (WOPF, IPET, Baza Uczniów) — te obsługują skille eduplaner-pctp i ipet-raport-pctp.
---

# EduPlaner 2026 — serwis sprzedażowy

Notatka dla osoby, która przejmuje `eduplaner2026/` i dokłada do niego resztę:
backend sklepu, wdrożenie, kolejne pozycje w ofercie.

Właścicielka: Mirosława Ewa Jurczyszyn, PCTP Koszalin. Nie programuje — każda zmiana,
która wymaga od niej edycji kodu, jest zmianą źle zrobioną. Wszystko, co ma zmieniać
sama, ma mieć narzędzie (tak działa dziś `panel-filmow.html`).

## Zanim cokolwiek zmienisz i zanim cokolwiek wyślesz

Trzy komendy. Pierwsza czyta pliki, dwie kolejne renderują stronę w przeglądarce.

```bash
node ../.claude/skills/straznik-strony/scripts/gotowosc.js .          # puste miejsca, brakujące pliki
node ../.claude/skills/straznik-strony/scripts/straznik.js index.html # kontrast, dostępność, prawo
node ../.claude/skills/straznik-strony/scripts/straznik.js index.html --ciemny
```

Obie kończą się kodem `1`, gdy jest blokada — nadają się do CI i do haka przed
wysyłką. Stan, do którego wracasz po każdej zmianie: **zero błędów w obu trybach**.
Regulamin, politykę prywatności i formularz odstąpienia sprawdzaj tym samym
skryptem, osobno — to też są strony.

Zasady, których pilnuje kontroler, opisuje skill `straznik-strony`. Czytaj je,
zanim zaczniesz dyskutować z jego wynikiem.

Do tego jest `pdf_strony.js` — składa całą stronę w jeden PDF, z tekstem
zostającym tekstem. Przed drukiem przewija stronę (obrazy wczytują się leniwie),
wyciąga pozycje z okien katalogów do sekcji, rozkłada wycieczkę po ekranach na
wszystkie zrzuty i rozwija pytania, więc PDF zawiera całą ofertę, a nie trzy
pozycje z dziesięciu:

```bash
node pdf_strony.js                                 # A4, tryb jasny
node pdf_strony.js --wyjscie oferta.pdf --poziomo  # kartka pozioma
node pdf_strony.js --bez-katalogow                 # tylko to, co widać na stronie
```

## Mapa projektu

```
index.html                  cała strona: HTML + CSS + JS w jednym pliku, bez frameworka
regulamin.html              projekt regulaminu (czeka na prawnika)
polityka-prywatnosci.html   projekt polityki
formularz-odstapienia.html  wzór oświadczenia
umowa-subskrypcji.html      umowa dla placówki + Załącznik nr 1 (protokół zdawczo-odbiorczy)
panel-filmow.html           narzędzie autorki: dodaje nagrania bez kodu
zaswiadczenia.html          narzędzie autorki: zaświadczenia, rejestr, materiały, zadania
broszury/                   publikacje: źródło HTML + złożony PDF
broszury/.bezplatne         lista plików, które wolno trzymać jawnie — reszta to blokada
img/                        .webp na serwer, .jpg to źródła, og.jpg do social mediów
build_single.py             skleja stronę z obrazami w jeden plik (podgląd, nie wdrożenie)
pdf_strony.js               składa całą stronę w jeden PDF do wysłania dyrektorowi
PRZEKAZANIE.md              ta sama treść dla człowieka, który nie czyta skilli
ANALIZA.md                  historia decyzji projektowych — czytaj, zanim coś cofniesz
```

Szczegóły budowy — tablice danych, routing okien, motyw jasny i ciemny, pułapki,
które już raz zepsuły stronę — w `references/architektura.md`. **Przeczytaj ten plik
przed pierwszą zmianą w `index.html`.**

## Najczęstsza zmiana: nowa pozycja w ofercie

Cała treść oferty siedzi w tablicy `OFERTA` w `index.html`. Dołożenie broszury,
szkolenia albo pomocy dydaktycznej to **cztery miejsca**, nie jedno:

1. **Obiekt w `OFERTA`** — pełny schemat pól w `references/architektura.md`.
   `id` musi być unikalne i stabilne: trafia do adresu `#pozycja-<id>`, który
   właścicielka wysyła mailem i wkleja na Facebooku. Zmiana `id` psuje te linki.
2. **`<option>` w formularzu zamówienia** — z `data-rodzaj` (`plik` / `usluga` /
   `towar` / `bezplatne`), `data-inst`, `data-person` i `data-price`.
   Szkolenia mają dwie ceny, więc dodatkowo `data-price-osoba`.

   Sam formularz rozróżnia **nabywcę** (na kogo faktura — w samorządzie gmina)
   i **odbiorcę** (placówka pracująca w programie). Checkbox `#odb-ten-sam` chowa
   drugi blok, gdy placówka rozlicza się sama. Nie scalaj tych pól z powrotem:
   faktura wystawiona na szkołę z NIP-em gminy wraca do korekty. Szczegóły
   w `references/backend.md`, rozdział „Faktura po złożeniu zamówienia".
3. **`polecane: true`**, jeśli ma stać na stronie. Sekcja pokazuje najwyżej trzy
   pozycje (`NA_STRONIE`), reszta mieszka w katalogu pod kafelkiem „Pełny katalog".
4. **Kontrolery** — obie komendy wyżej.

Czego nie robić: nie wstawiaj pozycji, której nie ma w sprzedaży. Cztery zmyślone
broszury zostały z tego powodu skasowane i zastąpione prawdziwymi. Atrapa w ofercie
kosztuje więcej zaufania niż krótsza oferta.

## Czego nie ma i co trzeba dobudować

Formularz zamówienia **nie ma backendu**: składa treść wiadomości i otwiera program
pocztowy przez `mailto:`. Na telefonie bez skonfigurowanej poczty zamówienie przepada
po cichu, bez śladu i bez potwierdzenia. To pierwsza rzecz do wymiany.

| Obszar | Stan dzisiaj | Do zrobienia |
|---|---|---|
| Zapis zamówień | brak | baza, numer zamówienia, potwierdzenie mailem |
| Płatności | brak | bramka dla osób prywatnych; faktura przelewowa dla placówek zostaje |
| Fakturowanie | ręcznie | dane z zamówienia do programu księgowego przez API; KSeF wystawia program, nie sklep |
| Koszyk | jedna pozycja na raz | wiele pozycji w jednym zamówieniu |
| Dostarczanie plików | ręcznie mailem | linki wygasające (72 h / 5 pobrań) — `references/zabezpieczenia.md` |
| Znak wodny w PDF | brak | przy pobraniu: nabywca, data, numer zamówienia |
| Nagrania płatnych szkoleń | brak | hosting z podpisanym adresem, blokadą domeny i znakiem wodnym widza |
| Adresy produktowe | `#pozycja-<id>` | `/broszury/<slug>`, mapa witryny |
| Wysyłka towarów | nie dotyczy | cała oferta jest do pobrania; gdyby doszedł towar, wraca § 6 regulaminu |
| Baner cookies | niepotrzebny | konieczny, zanim wejdzie analityka albo piksel |

Kontrakty punktów końcowych, model zamówienia, przebieg płatności, znak wodny
i obowiązki RODO — `references/backend.md`.

Zabezpieczenie broszur i nagrań — co da się zrobić, czego nie da się zrobić
i czego nie wolno obiecać klientowi — `references/zabezpieczenia.md`. **Przeczytaj
ten plik, zanim wgrasz na serwer pierwszą płatną broszurę albo nagranie szkolenia.**

**Kolejność, którą polecam:** zapis zamówień i potwierdzenie mailem → płatności
online dla osób prywatnych → przypomnienia o przedłużeniu → linki wygasające
i znak wodny → koszyk → adresy produktowe.

Kolejność wynika z wad dzisiejszego modelu, wypisanych od najkosztowniejszej:

1. **Zamówienie może przepaść bez śladu.** `mailto:` na telefonie bez
   skonfigurowanej poczty nie robi nic — dyrektor klika, nie widzi błędu, właścicielka
   nie dostaje maila. Drugi skutek: zgody na regulamin nigdzie się nie zapisują,
   więc w sporze o odstąpienie nie ma dowodu, co klient widział.
2. **Od zamówienia do dostępu mija 3–5 tygodni**: faktura → księgowość gminy →
   14 dni terminu → księgowanie → klucz. Zamówienie z 1 września daje dostęp koło
   25 września, a kupują we wrześniu, bo wtedy robi się WOPF-y. To konsekwencja
   reguły „klucz po wpłacie" i reguła zostaje — ale łagodzi się ją wersją
   demonstracyjną na czas oczekiwania i sprzedażą w czerwcu, gdy placówki planują
   budżet. **Nie łagodzi się jej wydaniem klucza przed zapłatą.**
3. **Faktura tworzy przychód w PIT, także niezapłacona.** VAT jest bezpieczny,
   bo usługę wykonuje się po wpłacie; podatek dochodowy nie. Lekarstwem jest
   kasowy PIT — decyzja księgowego, nie programisty.
4. **Osoba prywatna praktycznie nie kupi broszury za 30 zł**, skoro musi napisać
   maila, czekać na fakturę i zrobić przelew. To zakup impulsowy: albo domyka się
   BLIK-iem w minutę, albo nie domyka wcale. Ta część oferty nie sprzedaje się
   dziś z powodu formy płatności, nie ceny.
5. **Jedna pozycja na jedno zamówienie** — szkoła biorąca aplikację, dwa szkolenia
   i broszury wysyła trzy zamówienia i generuje trzy faktury dla tej samej
   księgowości, która ma zapłacić.
6. **Nic nie przypomina o przedłużeniu.** Licencja wygasa po 12 miesiącach cicho,
   a wydana we wrześniu wygasa w wakacje. To najtańszy przychód, jaki ta firma
   może mieć, i dziś wycieka bez śladu. Dlatego przypomnienia stoją w kolejności
   wyżej niż koszyk.
7. **Broszury bez znaku wodnego i linku wygasającego** — pierwsza sprzedaż
   w placówce bywa ostatnią. Patrz `references/zabezpieczenia.md`.

Koszyk jest nisko, niżej niż podpowiada odruch: przy ofercie kilkunastu pozycji
ludzie i tak kupują po jednej.

## Reguły, które muszą przetrwać każdą przebudowę

Te rzeczy są dziś zrobione zgodnie z prawem konsumenckim. Przepisując checkout,
przenieś je **wszystkie** — utrata którejkolwiek to nie jest regres wizualny,
tylko naruszenie:

- Przycisk kończący zamówienie brzmi **„Zamawiam z obowiązkiem zapłaty"**
  (przy bezpłatnym pokazie zmienia się na „Umów pokaz").
- Zgody to **osobne checkboxy, niezaznaczone domyślnie**. Nigdy jedna zbiorcza.
- Zgoda na dostarczenie treści cyfrowej przed upływem terminu odstąpienia
  pokazuje się **tylko konsumentowi** i tylko przy pozycji płatnej. Placówki
  kupującej na fakturę nie dotyczy i nie wolno jej tą zgodą straszyć.
- Treść obu zgód zapisuje się razem z zamówieniem — to jest dowód.
- **Ceny liczy serwer**, z własnego katalogu. `data-price` w HTML jest etykietą
  dla człowieka; kto ufa cenie z formularza, ten sprzedaje aplikację za 1 zł.
- **Aplikacja jest wyłącznie dla placówek.** Osoba prywatna kupuje szkolenia,
  broszury i pomoce. Pilnuje tego formularz, mówi o tym strona w sześciu miejscach
  i § 4 regulaminu. Backend musi to sprawdzić po swojej stronie, nie ufając polu.
- Ceny podawane brutto, z rozbiciem netto + VAT. Stawka 23% na wszystko, co dziś
  jest w ofercie. Stawki potwierdza księgowa, nie kod.
- **Klucz aktywacyjny wychodzi wyłącznie po zaksięgowaniu wpłaty. Bez wyjątków.**
  Umowa § 5 ust. 6 mówi to wprost; wcześniejsza wersja dopuszczała wydanie klucza
  po podpisaniu, przed zapłatą — właścicielka kazała ten zapis usunąć i **nie wolno
  go przywracać**, ani w umowie, ani w kodzie. Powód jest podwójny: wydanie klucza
  jest wykonaniem usługi, więc VAT staje się należny (przy 20 subskrypcjach to
  14 211,40 zł przed otrzymaniem pieniędzy), a data wydania klucza rozpoczyna
  bieg 12-miesięcznej licencji, więc dwa możliwe momenty wydania robią z niej
  kwestię sporną. Backend nie może mieć ścieżki „wydaj dostęp przed płatnością",
  także w trybie testowym na produkcji.
- **Każda licencja ma numer** w schemacie `EP/0001/2026`, ten sam w wiadomości
  z kluczem, w protokole zdawczo-odbiorczym i w bazie. Szczegóły w
  `references/backend.md`, rozdział „Numer licencji".

## Czego brakuje po stronie właścicielki

Kontroler `gotowosc.js` wypisze to za każdym razem; tu jest pełna lista przyczyn:

- ~~NIP, REGON, adres rejestrowy~~ — podane: Mirosława Ewa Jurczyszyn prowadząca
  działalność pod firmą Pomorskie Centrum Terapii Pedagogicznej, CEIDG,
  ul. Żołnierzy 8 Dywizji 13, 75-692 Koszalin, NIP 6691051752, REGON 330231014.
  Sprzedawcą jest **jednoosobowa działalność**, nie spółka cywilna o tej samej
  nazwie, która figuruje w rejestrach pod innym numerem — w umowie stroną jest
  osoba fizyczna działająca pod firmą, nie „Centrum".
- ~~nazwa banku i numer konta~~ — Erste Bank, numer podany; we wzorze umowy
  publikowanym na stronie zostaje **celowo puste miejsce**, numer trafia tylko
  do egzemplarza wysyłanego placówce i na fakturę. Rachunek jest na białej liście,
  co umowa § 5 stwierdza wprost.
- nazwa operatora płatności → regulamin § 5
- ~~terminy dostarczenia, koszt dostawy~~ — cała oferta jest elektroniczna:
  link do pobrania w ciągu 1 dnia roboczego, **bez kosztów dostawy**. Gdyby
  kiedyś doszedł towar wysyłany pocztą, wraca § 6 regulaminu, koszt dostawy
  przy cenie i inne zasady odstąpienia.
- data wejścia regulaminu w życie
- `img/hero-biurko.webp`, `img/autorka.webp`
- adresy nagrań (przez `panel-filmow.html`), adres Facebooka i bloga (`LINKS`)
- akceptacja prawnika dla trzech dokumentów — dopiero po niej zdejmuje się
  pomarańczowy baner „projekt dokumentu"

Do czasu, aż to przyjdzie, **strona nie może zostać opublikowana jako sklep**.
Może działać jako wizytówka z formularzem kontaktowym — to jest osobna decyzja
właścicielki, nie techniczna.

## Jak pracować z tym repozytorium

- Gałąź: `claude/website-analysis-design-a4nffd`. Nie push do `main` bez zgody.
- Commit opisuje skutek dla strony, nie nazwy funkcji.
- Po każdej zmianie w `index.html`: `python3 build_single.py` odświeża podgląd
  w `dist/` i ostrzega, gdy któraś ścieżka do obrazu nie została wbudowana.
- Zmieniasz coś, co dotyczy sprzedaży albo prawa → dopisz to w `PRZEKAZANIE.md`.
  Ten plik czyta właścicielka i on ma być zawsze prawdziwy.

Wdrożenie na serwer, kopie zapasowe, domena, HTTPS i to, co musi się zgadzać
z obietnicą „dane zostają na serwerze placówki" — `references/wdrozenie.md`.
