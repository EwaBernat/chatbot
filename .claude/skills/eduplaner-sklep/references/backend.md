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
  nabywca          placówka: nazwa, adres, NIP organu prowadzącego · osoba: imię, nazwisko, adres
  odbiorca         nazwa i adres placówki, gdy inny niż nabywca (samorząd — patrz „Faktura")
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

## Faktura po złożeniu zamówienia

Pytanie brzmi „czy faktura wystawi się sama". Odpowiedź: **fakturę wystawia
program księgowy, nie ta strona** — a strona podaje mu dane. Nie odwrotnie.

Powód jest prawny, nie techniczny. Faktura dla placówki to od 2026 r. faktura
ustrukturyzowana w KSeF. Numer nadaje jej Ministerstwo Finansów w momencie
przyjęcia, a nie sklep w momencie zamówienia. Sklep, który „generuje fakturę PDF"
i wysyła ją mailem, wystawia dokument, który w świetle przepisów fakturą nie jest.

### Droga, którą polecam

```
formularz  →  serwer sklepu           →  program księgowy (API)  →  KSeF
              zapisuje zamówienie         tworzy fakturę             nadaje numer
              liczy kwoty z katalogu      wysyła do KSeF             i datę doręczenia
                        ↓                                                 ↓
              e-mail: potwierdzenie zamówienia            e-mail: faktura + numer KSeF
              (od razu, zawsze)                           (gdy KSeF potwierdzi)
```

Program księgowy z API i obsługą KSeF (Fakturownia, wFirma, iFirma, inFakt —
wybór należy do księgowej, nie do programisty) robi całą trudną część: numerację,
JPK, KSeF, archiwum. Integracja to jedno wywołanie API na zamówienie.

**Nie buduj własnego integratora KSeF.** Uwierzytelnienie certyfikatem albo
tokenem, sesje, schematy FA(3), obsługa odrzuceń, tryb awaryjny przy niedostępności
systemu — to miesiące pracy i stałe utrzymanie po każdej zmianie schematu.
Jednoosobowa działalność sprzedająca kilkadziesiąt subskrypcji rocznie nie ma
z czego tego utrzymywać.

**Dwa e-maile, nie jeden.** Potwierdzenie zamówienia idzie natychmiast i zawsze —
to wymóg trwałego nośnika i jedyna rzecz, którą klient dostaje od razu. Faktura
idzie osobno, gdy wróci numer KSeF. Kto połączy jedno z drugim, ten przy awarii
KSeF nie wyśle nawet potwierdzenia.

### Czego formularz jeszcze nie zbiera

Automat wystawi poprawną fakturę tylko z kompletu danych. Dziś formularz ma
**jedno pole „Nazwa placówki (nabywca na fakturze)" i jeden NIP** — a umowa
subskrypcji rozróżnia dwa podmioty:

| Rola | Kto to jest | Co idzie na fakturę |
|---|---|---|
| Nabywca | organ prowadzący (gmina, powiat, osoba prowadząca) | nazwa, adres, **NIP nabywcy** |
| Odbiorca | szkoła lub przedszkole | nazwa i adres placówki, bez NIP |

W samorządzie to prawie zawsze dwa różne podmioty. Faktura wystawiona na szkołę
z NIP-em gminy — albo odwrotnie — wraca do korekty i płatność stoi. Zanim
fakturowanie się zautomatyzuje, formularz musi zbierać oba komplety, z podpowiedzią
„jeśli placówka rozlicza się sama, wpisz te same dane".

Placówka może też wymagać faktury przez **PEF** (Platforma Elektronicznego
Fakturowania) — to osobny kanał od KSeF i osobne pole w zamówieniu: numer PEPPOL
albo identyfikator jednostki.

### Osoba prywatna to inny przypadek

KSeF obejmuje obrót między firmami. Sprzedaż broszury nauczycielowi jako
konsumentowi jest poza nim: dokument wystawia się zwykłą drogą i wysyła mailem,
a faktura należy się na żądanie zgłoszone w terminie z ustawy o VAT. W praktyce
prościej wystawiać ją każdemu — pole „chcę fakturę" i tak trzeba obsłużyć, a przy
cenie 30 zł spór o to nikomu się nie opłaca.

### Co da się zrobić dziś, bez backendu

Formularz składa gotową treść zamówienia. Wystarczy, że będzie zawierał wszystkie
pola faktury w stałej kolejności — wtedy wystawienie dokumentu w programie
księgowym to przeklejenie, nie przepisywanie. To nie jest automat, ale usuwa
najczęstszy błąd: fakturę z literówką w nazwie gminy.

## Numer licencji

Każda subskrypcja dostaje własny numer. Bez niego nie da się odpowiedzieć na
pytanie „czy ta szkoła ma ważną licencję i do kiedy" — a to pytanie przychodzi
przy przedłużeniu, przy reklamacji i przy kontroli.

Schemat: **`EP/0001/2026`** — kolejny numer w roku, rok wydania. Ten sam wzór co
w zaświadczeniach ze szkoleń, więc właścicielka nie musi pamiętać dwóch.

Numer wędruje przez trzy miejsca i wszędzie musi być ten sam:

1. **wiadomość z kluczem aktywacyjnym** — numer licencji, data wydania, data ważności;
2. **protokół zdawczo-odbiorczy** (Załącznik nr 1 do umowy) — tabela w punkcie 3,
   podpisana przez dyrektora; to jedyny dokument wiążący numer z placówką i datą;
3. **baza po stronie serwera**, gdy powstanie:

```
licencja
  numer          EP/0001/2026 — kolejny, niepowtarzalny
  zamowienie     numer zamówienia, z którego wynika
  placowka       nazwa i adres odbiorcy (nie nabywcy — patrz „Faktura")
  klucz          skrót klucza aktywacyjnego, nigdy sam klucz jawnie
  wydana         data przekazania klucza
  wazna_do       dzień poprzedzający pierwszą rocznicę wydania
  status         aktywna → wygasla → przedluzona
```

Data wygaśnięcia liczy się **od wydania klucza**, nie od podpisania umowy ani od
zapłaty — tak stanowi § 2 umowy. Kto policzy ją inaczej, ten skróci albo wydłuży
licencję o kilka tygodni i nie będzie umiał tego obronić.

Przypomnienie o przedłużeniu wysyła się na 30 dni przed wygaśnięciem. Rok szkolny
kończy się w czerwcu, a licencje wydane we wrześniu wygasają w środku wakacji —
bez przypomnienia szkoła zorientuje się dopiero 1 września, gdy program przestanie
generować dokumenty.

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
