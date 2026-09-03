---
name: eduplaner-sklep
description: Praca nad serwisem sprzedażowym eduplaner2026.pl (PCTP Koszalin) — dokładanie pozycji do oferty, budowa brakującego backendu sklepu i wdrożenie strony na serwer. Uruchamiaj ZAWSZE przy zadaniach dotyczących tego serwisu: „dodaj broszurę / szkolenie / pomoc dydaktyczną do oferty", „zmień cenę", „podłącz formularz zamówienia", „koszyk", „płatności online", „Przelewy24 / Stripe", „zapis zamówień", „wygasające linki do pobrania", „znak wodny w PDF", „adresy produktowe zamiast hasha", „wystaw stronę na serwer", „publikacja", „domena", „co jeszcze trzeba zrobić przed sprzedażą". Wyzwalaj także przy pytaniach o strukturę tego kodu: OFERTA, FILMY, EKRANY, build_single.py, panel filmów. Nie używaj do samych dokumentów edukacyjnych (WOPF, IPET, Baza Uczniów) — te obsługują skille eduplaner-pctp i ipet-raport-pctp.
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

## Mapa projektu

```
index.html                  cała strona: HTML + CSS + JS w jednym pliku, bez frameworka
regulamin.html              projekt regulaminu (czeka na prawnika)
polityka-prywatnosci.html   projekt polityki
formularz-odstapienia.html  wzór oświadczenia
panel-filmow.html           narzędzie autorki: dodaje nagrania bez kodu
broszury/                   publikacje: źródło HTML + złożony PDF
img/                        .webp na serwer, .jpg to źródła, og.jpg do social mediów
build_single.py             skleja stronę z obrazami w jeden plik (podgląd, nie wdrożenie)
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
| Koszyk | jedna pozycja na raz | wiele pozycji w jednym zamówieniu |
| Dostarczanie plików | ręcznie mailem | linki wygasające (72 h / 5 pobrań) |
| Znak wodny w PDF | brak | przy pobraniu: nabywca, data, numer zamówienia |
| Adresy produktowe | `#pozycja-<id>` | `/broszury/<slug>`, mapa witryny |
| Wysyłka towarów | brak | koszty, formy dostawy, adres, czas realizacji |
| Baner cookies | niepotrzebny | konieczny, zanim wejdzie analityka albo piksel |

Kontrakty punktów końcowych, model zamówienia, przebieg płatności, znak wodny
i obowiązki RODO — `references/backend.md`.

**Kolejność, którą polecam:** zapis zamówień i potwierdzenie mailem (bez tego
sprzedaż jest dziurawa) → płatności online → linki wygasające i znak wodny →
koszyk → adresy produktowe. Koszyk jest niżej, niż podpowiada odruch: przy
ofercie kilkunastu pozycji ludzie i tak kupują po jednej.

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

## Czego brakuje po stronie właścicielki

Kontroler `gotowosc.js` wypisze to za każdym razem; tu jest pełna lista przyczyn:

- NIP, REGON, pełny adres rejestrowy → stopka i wszystkie trzy dokumenty
- termin płatności faktury, nazwa operatora płatności → regulamin § 5
- terminy dostarczenia plików i wysyłki, koszt dostawy → regulamin § 6
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
