# EduPlaner 2026 — strona sprzedażowa. Przekazanie

Cześć Arku.

W tym pakiecie jest cała strona eduplaner2026.pl: kod, dokumenty prawne, dwa
narzędzia dla właścicielki i komplet zasad, które trzeba znać, zanim się cokolwiek
zmieni. Właścicielka to **Mirosława Ewa Jurczyszyn, PCTP Koszalin** — nie programuje.
Każda zmiana, która wymaga od niej edycji kodu, jest zmianą źle zrobioną.

## Co zmieniło się w tej paczce (10 września 2026)

Jeżeli dostałeś wcześniejszą wersję, to jest różnica:

- **`umowa-subskrypcji.html` — nowy § 4 „Zakres odpowiedzialności za dokumentację".**
  Oznaczony **zieloną oprawą** z etykietą „Nowy zapis" i notatką dla Ciebie.
  Zieleń jest tymczasowa: po akceptacji prawnika usuwa się `<div class="nowe">`
  razem z etykietą i notatką, zostawiając nagłówek i listę. **Uwaga: paragrafy
  poniżej przesunęły się o jeden** (dawny § 4 → § 5, § 5 → § 6, § 6 → § 7,
  § 7 → § 8). Odwołania w dokumentacji zostały poprawione; odwołanie wewnętrzne
  do „§ 2 ust. 3 lit. c" jest nadal aktualne.
- **`index.html` — zdjęcie w hero.** `img/hero-biurko.webp` zastępuje makietę
  laptopa. Kiedy plik się wczyta, JS dokłada klasę `has-photo` na `.hero-stage`
  i makieta znika. Karta „Druk IPET gotowy do PDF" **musi zostać poza `.device`** —
  wewnątrz znikała razem z laptopem.
- **`index.html` — sekcja „Co się zmieniło" ma piąty wiersz** o opinii
  o funkcjonowaniu (obowiązek od 1 września 2026) i **przycisk `[data-przepis]`**,
  który otwiera okno z podstawą prawną. Treść okna jest w JS jako stała `TRESC`
  — tam się ją edytuje, nie w HTML.
- **Formularz zamówienia** zbiera komplet danych do faktury imiennej dla osoby
  prywatnej (imię i nazwisko, ulica, kod, miejscowość) i mówi wprost, że
  **gotówki nie przyjmujemy**. To warunek zwolnienia z kasy fiskalnej, nie
  preferencja — patrz reguła 3 niżej.
- **Nowy plik `zamowienie-osoba-prywatna.html`** — druk zamówienia dla konsumenta.
- **Ceny szkoleń:** „Obserwacja pogłębiona" trwa 1 godzinę i kosztuje 1000 zł
  brutto dla rady, „Teoria umysłu" też 1000 zł.

## Pierwsze pół godziny

```bash
cd eduplaner2026
python3 -m http.server 8000     # albo po prostu otwórz index.html w przeglądarce
```

Potem, zanim cokolwiek wyślesz:

```bash
node ../.claude/skills/straznik-strony/scripts/gotowosc.js .
node ../.claude/skills/straznik-strony/scripts/straznik.js index.html
node ../.claude/skills/straznik-strony/scripts/straznik.js index.html --ciemny
```

Pierwszy czyta pliki (puste miejsca, brakujące obrazy, płatne pliki pod stałym
adresem). Dwa kolejne renderują stronę w przeglądarce i sprawdzają kontrast,
dostępność i wymogi prawa konsumenckiego. Wymagają Playwrighta:
`npm i -D playwright && npx playwright install chromium`.

**Stan, do którego wracasz po każdej zmianie: zero błędów w obu trybach.**

## Co czytać i w jakiej kolejności

| Plik | Co w nim jest |
|---|---|
| `eduplaner2026/PRZEKAZANIE.md` | to samo co niżej, ale językiem właścicielki — czyta to ona |
| `.claude/skills/eduplaner-sklep/SKILL.md` | mapa projektu, reguły, których nie wolno zgubić |
| `…/references/architektura.md` | tablice danych, routing okien, motywy, pułapki — **przed pierwszą zmianą w `index.html`** |
| `…/references/backend.md` | model zamówienia, punkty końcowe, faktury, numer licencji, RODO |
| `…/references/zabezpieczenia.md` | ochrona broszur i nagrań — **przed wgraniem pierwszego płatnego pliku** |
| `…/references/wdrozenie.md` | serwer, domena, HTTPS, kopie |
| `eduplaner2026/ANALIZA.md` | historia decyzji projektowych — przeczytaj, zanim coś cofniesz |

## Jak to jest zbudowane

Jeden plik `index.html`: HTML, CSS i JavaScript razem, bez frameworka, bez kroku
budowania. Cała treść oferty siedzi w tablicy `OFERTA` w tym pliku. To nie jest
niedbałość, tylko decyzja: strona ma działać po skopiowaniu na dowolny hosting
i dać się poprawić bez `npm install`.

`build_single.py` wkleja obrazy w postaci `data:` i tworzy `dist/eduplaner2026.html`
— jeden plik do wysłania mailem. To podgląd, nie wdrożenie.

## Czego strona nie ma

**Formularz zamówienia nie ma backendu.** Składa treść wiadomości i otwiera
program pocztowy przez `mailto:`. Na telefonie bez skonfigurowanej poczty
zamówienie przepada bez śladu i bez potwierdzenia. To pierwsza rzecz do wymiany.

Kolejność, którą polecam: zapis zamówień i potwierdzenie mailem → płatności
online dla osób prywatnych → przypomnienia o przedłużeniu licencji → linki
wygasające i znak wodny w PDF → koszyk → adresy produktowe. Uzasadnienie
kolejności jest w `SKILL.md`.

## Pięć reguł, których nie wolno złamać

Wszystkie są dziś w kodzie zrobione zgodnie z prawem. Utrata którejkolwiek to nie
regres wizualny, tylko naruszenie albo utrata sprzedaży.

1. **Klucz aktywacyjny i pliki wychodzą wyłącznie po zaksięgowaniu wpłaty.**
   Bez wyjątków, także w trybie testowym na produkcji. Wcześniejsza wersja umowy
   dopuszczała wydanie klucza po podpisaniu — właścicielka kazała to usunąć.
   Powód jest podwójny: wydanie klucza to wykonanie usługi, więc VAT staje się
   należny przed otrzymaniem pieniędzy, a data wydania klucza rozpoczyna bieg
   12-miesięcznej licencji.
2. **Ceny liczy serwer, z własnego katalogu.** `data-price` w HTML to etykieta
   dla człowieka. Kto ufa cenie z formularza, ten sprzeda aplikację za 1 zł.
3. **Sprzedaż osobie prywatnej idzie wyłącznie przelewem albo bramką — nigdy
   gotówką.** To warunek zwolnienia z kasy fiskalnej. Nie buduj ścieżki
   „gotówka na miejscu"; tytuł płatności i raport bramki muszą nieść numer
   zamówienia, bo bez tego odpada warunek ewidencji.
4. **Zgody to osobne checkboxy, niezaznaczone domyślnie**, a ich treść zapisuje
   się razem z zamówieniem — to jedyny dowód w sporze o odstąpienie. Przycisk
   kończący zamówienie brzmi „Zamawiam z obowiązkiem zapłaty".
5. **Aplikacja jest wyłącznie dla placówek.** Osoba prywatna kupuje szkolenia,
   broszury i pomoce. Backend musi to sprawdzić po swojej stronie, nie ufając polu.

## Czego brakuje po stronie właścicielki

`gotowosc.js` wypisze to za każdym razem. Dziś: `img/hero-biurko.webp`,
`img/autorka.webp`, adresy nagrań, adres Facebooka i bloga, nazwa operatora
płatności, data wejścia regulaminu w życie oraz **akceptacja prawnika dla czterech
dokumentów** — dopóki jej nie ma, pomarańczowy baner „projekt dokumentu" zostaje.

**Do czasu, aż to przyjdzie, strona nie może zostać opublikowana jako sklep.**
Może działać jako wizytówka z formularzem kontaktowym — to decyzja właścicielki,
nie techniczna.

## Kontakt

Mirosława Ewa Jurczyszyn · kontakt@eduplaner2026.pl · 662 888 403
