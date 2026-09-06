# Backend sklepu — co ma robić i czego nie wolno mu zrobić

Dziś backendu nie ma. Formularz składa treść wiadomości i otwiera program pocztowy.
Ten plik opisuje, co go zastąpi. Technologia jest dowolna — zasady nie.

## Zasada pierwsza: cenę zna serwer

W HTML-u przy każdej pozycji stoi `data-price`. To jest **etykieta dla człowieka**,
nie źródło prawdy. Przeglądarka pozwala ją podmienić w trzy sekundy.

Serwer ma własny katalog pozycji (ta sama treść co `OFERTA`, tylko po swojej
stronie) i liczy kwotę wyłącznie z niego. Z formularza przyjmuje **identyfikatory
i ilości**, nigdy kwoty.

Ta sama zasada dotyczy uprawnień: pole „kupuję jako placówka" to deklaracja, nie
dowód. Aplikacji nie wolno sprzedać osobie prywatnej — sprawdza to serwer, nie
`disabled` na liście wyboru.

## Model zamówienia

Minimum, które trzeba zapisać, żeby zamówienie było umową, a nie mailem:

```
zamowienie
  numer            2026/09/0001 — kolejny, niepowtarzalny, widoczny dla klienta
  utworzone        znacznik czasu
  kupujacy         inst | person
  pozycje[]        { id, nazwa, ilosc, cenaNetto, vat, cenaBrutto }  ← z katalogu serwera
  kwoty            netto, vat, brutto (suma policzona na serwerze)
  dane             placówka: nazwa, adres, NIP · osoba: imię i nazwisko, adres do faktury
  kontakt          e-mail, telefon
  zgody[]          { rodzaj, tresc, znacznikCzasu }  ← pełna treść, nie samo „true"
  status           nowe → oplacone → zrealizowane → anulowane
  platnosc         { typ: faktura|online, identyfikatorOperatora, status }
```

**Zgody zapisuj z treścią**, którą klient widział, i z datą. Za dwa lata nikt nie
odtworzy, jak brzmiał checkbox we wrześniu 2026 — a to jest dowód w sporze
o odstąpienie od umowy.

## Punkty końcowe

```
POST /api/zamowienie
  {pozycje:[{id,ilosc}], kupujacy, dane, kontakt, zgody:{regulamin, cyfrowa?}, uwagi}
  → 201 {numer, kwoty, platnosc:{typ, url?}}
  → 400 gdy: brak zgody na regulamin, pozycja nieznana,
             osoba prywatna zamawia pozycję tylko dla placówek,
             konsument zamawia treść cyfrową bez zgody z art. 38

POST /api/platnosc/webhook          ← wywołuje operator, nie przeglądarka
  weryfikacja podpisu → status „oplacone" → wydanie dostępu i wysyłka maila
  ma być idempotentny: operator potrafi wysłać to samo dwa razy

GET  /pobierz/<token>
  token jednorazowy, ważny 72 h, najwyżej 5 pobrań
  odpowiedź: PDF ze znakiem wodnym, generowany przy pobraniu
  po wyczerpaniu: strona z informacją i przyciskiem „poproś o nowy link"
```

Potwierdzenie zamówienia idzie mailem **zawsze**, także przy fakturze przelewowej.
Zawiera: numer, pozycje, kwoty, treść obu zgód, pouczenie o odstąpieniu oraz
regulamin i politykę w załączniku lub pod trwałym adresem. To jest wymóg
„trwałego nośnika", nie uprzejmość.

## Płatności

- **Placówka** płaci fakturą przelewową z odroczonym terminem. Tak działa dziś
  i tak ma zostać — księgowość szkoły nie zapłaci kartą.
- **Osoba prywatna** płaci online: BLIK, karta, szybki przelew. Operator do wyboru
  właścicielki (Przelewy24, Tpay, Stripe); nazwę trzeba wpisać w regulamin § 5.
- Klucze operatora **tylko po stronie serwera**, w zmiennych środowiskowych.
  Nigdy w pliku, który pobiera przeglądarka. `gotowosc.js` to sprawdza.
- Dostęp otwierasz po potwierdzeniu z webhooka, nie po powrocie użytkownika na
  stronę „dziękujemy" — ten powrót da się sfałszować adresem.

## Pliki płatne: linki i znak wodny

Broszury to PDF-y, które kosztują 30–50 zł. Bez zabezpieczenia pierwszy kupujący
rozsyła plik całej radzie pedagogicznej i sprzedaż się kończy.

- **Link wygasający**: token losowy, 72 godziny, najwyżej 5 pobrań, powiązany
  z numerem zamówienia. Nigdy stały adres pliku w publicznym katalogu.
- **Znak wodny generowany przy pobraniu**: imię i nazwisko lub nazwa placówki,
  adres e-mail, numer zamówienia, data. W stopce każdej strony, dyskretnie —
  ma nie psuć wydruku do pracy z dzieckiem, a jednocześnie mówić wprost, czyj
  to egzemplarz.
- Licencja z regulaminu § 7: osoba prywatna drukuje na własny użytek zawodowy,
  placówka na potrzeby swojego zespołu. Znak wodny ma to przypominać, nie straszyć.

## Zaświadczenie tylko dla tych, którzy naprawdę byli

Zaświadczenie ma wartość dokładnie tak długo, jak długo znaczy, że ktoś odbył
szkolenie. Sam zakup nie jest udziałem — a przy nagraniu „odtworzone" nie jest
tym samym co „obejrzane". Warunek trzeba **mierzyć i zapisać**, zanim system
wystawi dokument.

**Szkolenie na żywo:**

- Raport uczestnictwa z platformy (Zoom, Teams, Meet) daje czas wejścia i wyjścia.
  Próg: udział w co najmniej 80% czasu.
- Kod obecności podawany na wizji dwa lub trzy razy, w losowych momentach,
  wpisywany przez uczestnika w formularzu. Kto wyszedł po dziesięciu minutach,
  nie zdobędzie kompletu.
- Ankieta po szkoleniu jako warunek wydania dokumentu. Przy okazji zbiera opinie,
  które można — za zgodą — pokazać na stronie.

**Nagranie:**

- Postęp odtwarzania zapisywany na serwerze (sygnał co 15 s), próg 90% materiału.
  Liczy się czas obejrzany, nie czas otwartej karty.
- Przewijanie do przodu zablokowane przy pierwszym odtworzeniu; cofanie wolne.
- Pytania kontrolne wplecione w nagranie co kilkanaście minut — jedyny sposób,
  by odróżnić oglądanie od puszczenia filmu w tle.
- Test końcowy: kilka pytań, próg zaliczenia, dwa podejścia.
- Jedno konto = jedna sesja naraz, znak wodny z adresem e-mail na obrazie.

**Zapis w bazie** (bez tego nie ma czego udowodnić przy kontroli ani przy sporze):

```
uczestnictwo
  zamowienie, uczestnik, szkolenie
  obecnosc      { procentCzasu, kodyObecnosci[], zrodlo: 'zoom'|'kody' }
  nagranie      { procentObejrzany, ostatniSygnal }
  test          { wynik, podejscia, dataZaliczenia }
  zaswiadczenie { numer, dataWydania, plik }
```

**Zanim to wejdzie w życie**, warunek musi być napisany tam, gdzie uczestnik go
przeczyta przed zapłatą: w opisie szkolenia, w regulaminie i w potwierdzeniu
zamówienia. Dziś strona obiecuje w pytaniach, że *każdy uczestnik dostaje
zaświadczenie imienne* — wprowadzenie progu bez zmiany tego zdania byłoby
obietnicą złamaną po fakcie.

**Co działa już teraz, bez backendu:** kod obecności podany na żywo plus krótka
ankieta, a potem wydruk kompletu zaświadczeń w `zaswiadczenia.html`. To narzędzie
drukuje też listę wydanych dokumentów z miejscem na podpis odbioru — razem
z raportem z platformy jest to komplet dowodów uczestnictwa.

## Koszyk

Dziś jedna pozycja na raz i to nie jest dramat: przy kilkunastu pozycjach ludzie
kupują pojedynczo. Gdy koszyk powstanie, dwie rzeczy muszą się zgadzać:

- **Rodzaje pozycji mieszają się w jednym zamówieniu** — plik, usługa i towar mają
  różne terminy dostarczenia i różne zasady odstąpienia. Podsumowanie musi pokazać
  je osobno, a zgoda z art. 38 dotyczy tylko treści cyfrowych w tym koszyku.
- **Placówka i osoba prywatna mają różne katalogi.** Aplikacja znika z koszyka
  osoby prywatnej, nie jest w nim wyszarzona.

## RODO w praktyce

- Zbieraj tylko to, co potrzebne do umowy i faktury. Pole „telefon" zostaje
  opcjonalne.
- Retencja: dane z faktur trzymają się przez okres wymagany przepisami
  podatkowymi, korespondencja krócej. Wpisz konkretne terminy do polityki
  prywatności — dziś stoją tam puste miejsca.
- Operator płatności i firma hostująca to **podmioty przetwarzające**: z każdym
  trzeba mieć umowę powierzenia. Ich lista wchodzi do polityki prywatności.
- Rejestr czynności przetwarzania — obowiązek administratora, czyli PCTP.
- Dane uczniów **nie przechodzą przez ten sklep w ogóle**. Aplikacja stoi na
  serwerze placówki i to jest w komunikacji obietnica, nie chwyt marketingowy.
  Nie wolno zbudować niczego, co tę obietnicę łamie — żadnej „chmurowej kopii
  dokumentacji", żadnej telemetrii z treścią WOPF-ów.

## Adresy produktowe

`#pozycja-br-emocje` → `/broszury/kolorowy-swiat-emocji`. Do tego mapa witryny,
`og:image` per pozycja i dane strukturalne `Product` z ceną. Dopiero wtedy broszura
ma szansę pojawić się w wynikach wyszukiwania — dziś nie ma żadnej.

Stare adresy z haszem zostaw jako przekierowania: krążą w mailach.

## Czego nie budować

- Kont użytkowników. Nikt nie chce zakładać konta, żeby kupić PDF za 30 zł.
  Zamówienie identyfikuje numer i e-mail.
- Analityki „na wszelki wypadek". Każdy skrypt śledzący wymusza baner cookies,
  którego dziś nie ma i którego strona nie potrzebuje.
- Chatbota, karuzeli i wyskakujących okien z rabatem. Strona sprzedaje narzędzie
  dla dyrektorów placówek publicznych; te elementy obniżają wiarygodność.
