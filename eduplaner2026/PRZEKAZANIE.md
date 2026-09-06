# Przekazanie — eduplaner2026.pl

Notatka dla osoby, która przejmuje serwis i buduje z niego sklep.
Stan na 3 września 2026, gałąź `claude/website-analysis-design-a4nffd`.

**Jeżeli pracujesz z Claude Code, wszystko to jest też w dwóch skillach**
i włącza się samo, gdy dotykasz tego projektu:

| Skill | Do czego |
|---|---|
| `eduplaner-sklep` | budowa tego serwisu: dokładanie pozycji, backend, wdrożenie |
| `straznik-strony` | zasady dla stron sprzedażowych w Polsce + dwa kontrolery |

Dwie komendy, którymi kończy się każda zmiana:

```bash
node ../.claude/skills/straznik-strony/scripts/gotowosc.js .            # puste miejsca, brakujące pliki
node ../.claude/skills/straznik-strony/scripts/straznik.js index.html   # kontrast, dostępność, prawo
node ../.claude/skills/straznik-strony/scripts/straznik.js index.html --ciemny
```

Stan docelowy: zero blokad i zero błędów w obu trybach.

Oferta w jednym pliku PDF — do maila, do wydruku na spotkanie:

```bash
node pdf_strony.js                      # eduplaner2026-strona.pdf, A4
node pdf_strony.js --wyjscie oferta.pdf --poziomo
```

## Czym to jest dzisiaj

Jedna statyczna strona sprzedażowa (`index.html`), bez frameworka, bez kroku budowania.
Cały HTML, CSS i JavaScript siedzą w jednym pliku. Do tego trzy podstrony prawne,
narzędzie autorki do filmów i katalog broszur w PDF.

```
index.html                    strona główna — wszystko w jednym pliku
regulamin.html                projekt regulaminu (do zatwierdzenia przez prawnika)
polityka-prywatnosci.html     projekt polityki prywatności
formularz-odstapienia.html    wzór oświadczenia
panel-filmow.html             narzędzie autorki: dodawanie nagrań bez kodu
img/                          zrzuty i zdjęcia (.webp do publikacji, .jpg jako źródła)
broszury/                     publikacje: źródło HTML + złożony PDF
build_single.py               skleja index.html z obrazami w jeden plik do wysyłki
ANALIZA.md                    historia decyzji projektowych
```

## Trzy tablice danych — tu jest cała treść oferty

Wszystko, co się zmienia, siedzi w trzech tablicach w `index.html`.
Nie ma potrzeby dotykać HTML-a sekcji.

| Tablica | Co opisuje | Kluczowe pola |
|---|---|---|
| `OFERTA` | szkolenia, broszury, pomoce dydaktyczne | `id`, `typ`, `polecane`, `tytul`, `opis`, `punkty`, `spec`, `ceny`, `netto`, `tagi`, `okladka` |
| `FILMY` | nagrania w sekcji „Zobacz w działaniu" | `id`, `glowny`, `tytul`, `czas`, `url` |
| `EKRANY` | zrzuty aplikacji w sekcji „Siedem ekranów" | `plik`, `tytul`, `opis` |

Zasady, które trzyma kod:

- **Trzy na stronie, reszta w katalogu.** Sekcja pokazuje najwyżej `NA_STRONIE = 3`
  pozycje z `polecane: true`. Nadmiar wchodzi do okna katalogu przez kafelek „Pełny katalog".
- **Pusta kategoria znika.** Kategoria bez pozycji chowa swoją sekcję i swój link w menu
  (dziś tak działa `#pomoce`).
- **Pusty adres = „wkrótce".** Film bez `url` jest nieklikalny zamiast prowadzić donikąd.
  To samo dotyczy `LINKS.facebook` i `LINKS.blog`.
- **Katalog ma wyszukiwarkę, filtry po `tagi` i doładowywanie po `NA_RAZ = 24` pozycje.**
  Działa po stronie przeglądarki, sensownie do mniej więcej dwustu pozycji.

## Adresy w oknach

Katalog i karty pozycji mają własne adresy — da się je linkować w mailu i na Facebooku:

```
#katalog-szkolenie      katalog szkoleń
#katalog-broszura       katalog broszur
#katalog-pomoc          katalog pomocy dydaktycznych
#pozycja-br-echolalia   karta jednej pozycji (identyfikator z pola id)
```

To jest proteza. Docelowo mają to być prawdziwe adresy `/broszury/echolalia`,
bo treść za krzyżykiem nie istnieje dla wyszukiwarki.

## Czego nie ma i trzeba zbudować

Formularz zamówienia **nie ma backendu**. Składa treść wiadomości i otwiera program
pocztowy przez `mailto:`. Na telefonie bez skonfigurowanej poczty zamówienie przepada
po cichu. To pierwsza rzecz do wymiany.

| Obszar | Stan | Do zrobienia |
|---|---|---|
| Koszyk | brak — jedna pozycja na raz | wiele pozycji w jednym zamówieniu |
| Płatności | brak | bramka dla osób prywatnych; faktura przelewowa dla placówek zostaje |
| Zapis zamówień | brak | baza + numer zamówienia + potwierdzenie mailem |
| Dostarczanie plików | ręcznie mailem | wygasające linki (72 h / 5 pobrań) |
| Znak wodny w PDF | brak | generowany przy pobraniu: nabywca, data, numer zamówienia |
| Adresy produktowe | hash | routing `/broszury/<slug>`, mapa witryny |
| Wysyłka towarów | brak | koszty, formy dostawy, adres w zamówieniu, czas realizacji |
| Omnibus | nie dotyczy | przy pierwszej promocji: najniższa cena z 30 dni |
| Baner cookies | nie dotyczy | konieczny, zanim wejdzie analityka lub piksel |

## Co już jest zrobione po stronie zgodności

- Przycisk kończący zamówienie brzmi **„Zamawiam z obowiązkiem zapłaty"**;
  przy bezpłatnym pokazie zmienia się na „Umów pokaz".
- **Akceptacja regulaminu** — checkbox wymagany, niezaznaczony domyślnie, blokuje wysyłkę.
- **Zgoda na dostarczenie przed upływem terminu odstąpienia** — pokazuje się tylko
  osobie prywatnej i tylko przy pozycji płatnej. Treść zmienia się zależnie od tego,
  czy pozycja jest plikiem (`data-rodzaj="plik"`), czy usługą (`"usluga"`).
  Placówka kupująca na fakturę tej zgody nie widzi, bo prawo odstąpienia jej nie dotyczy.
- Obie zgody trafiają do treści zamówienia, więc zostaje ślad.
- Stopka: dane sprzedawcy, linki do regulaminu, polityki, formularza odstąpienia
  i nota o prawach autorskich.

## Faktury: czy trzeba kupować program

**Nie trzeba.** Ministerstwo Finansów udostępnia bezpłatnie Aplikację Podatnika
KSeF (przeglądarkowa), e-mikrofirmę i aplikację mobilną. Wystawiają, odbierają
i przechowują faktury ustrukturyzowane. Przy kilkudziesięciu fakturach rocznie
to wystarcza w zupełności.

Jednorazowo trzeba załatwić uwierzytelnienie w KSeF — profil zaufany, podpis
kwalifikowany albo certyfikat — i przy okazji nadać uprawnienia księgowej.

Program płatny (Fakturownia, wFirma, iFirma, inFakt) kupuje się nie z powodu
przepisów, tylko dla trzech rzeczy: **API** (bez niego sklep nie ma się z czym
połączyć i automatyczne fakturowanie jest niemożliwe), szablonów faktur
odnawianych co rok oraz wspólnej pracy z księgową.

Kolejność: najpierw zapytać księgową, czego używa — bardzo często ma już program
z KSeF i API, więc wystarczy dostęp. Do czasu powstania backendu wystarcza
darmowe narzędzie MF. Abonament wykupuje się dopiero razem z integracją.

Do potwierdzenia u księgowej, bo terminy KSeF były przesuwane: od kiedy dokładnie
obowiązuje wystawianie w KSeF i czy sprzedaż osobom prywatnym w ogóle przez niego
idzie (obowiązek dotyczy obrotu między firmami).

## Formularz zamówienia: nabywca i odbiorca

Placówka zamawiająca podaje **dwa komplety danych**, bo w samorządzie to dwa różne
podmioty: fakturę wystawia się na organ prowadzący (gmina, powiat) z jego NIP-em,
a szkoła jest odbiorcą. Faktura wystawiona na szkołę z NIP-em gminy wraca do korekty
i płatność stoi. Gdy placówka rozlicza się sama, wystarczy zaznaczyć checkbox
„Placówka rozlicza się sama" — drugi blok znika, a w zamówieniu pojawia się adnotacja
„ten sam podmiot co nabywca".

W wiadomości z zamówieniem dane przychodzą w stałym układzie: NABYWCA (faktura),
potem ODBIORCA (placówka). Dzięki temu wystawienie faktury w programie księgowym
to przeklejenie, nie przepisywanie.

## Do uzupełnienia przez właścicielkę

Miejsca oznaczone w dokumentach prawnych jako `do uzupełnienia` oraz w stopce
na pomarańczowo:

- ~~NIP, REGON, adres rejestrowy~~ — wpisane 6 września 2026:
  Mirosława Ewa Jurczyszyn prowadząca działalność gospodarczą pod firmą
  Pomorskie Centrum Terapii Pedagogicznej Mirosława Ewa Jurczyszyn (CEIDG),
  ul. Żołnierzy 8 Dywizji 13, 75-692 Koszalin, NIP 6691051752, REGON 330231014
- nazwa banku i numer konta do przelewu (umowa § 5, regulamin)
- nazwa operatora płatności (regulamin § 5) — jedyna brakująca dana sprzedażowa
- ~~godziny kontaktu~~ 10:00–14:00 w dni robocze · ~~terminy dostarczenia~~ 1 dzień
  roboczy · ~~koszt dostawy~~ nie występuje, cała oferta jest do pobrania
- data wejścia w życie regulaminu

Poza tym: adresy nagrań (przez `panel-filmow.html`), adresy Facebooka i bloga
(`LINKS` w `index.html`), zdjęcie autorki (`img/autorka.jpg`).

## Uwagi techniczne

- Obrazy są w WebP, 46–102 KB, wymiary 1600×1000 (zrzuty) i 1200×750 (zdjęcia sal).
  Pliki `.jpg` w `img/` to źródła — na serwer idą tylko `.webp` i `og.jpg`.
- `build_single.py` wbudowuje obrazy w jeden plik HTML; ostrzega, gdy któraś ścieżka
  została niewbudowana. Przydatny do wysyłki podglądu, nie do wdrożenia.
- Strona nie ładuje żadnej analityki ani pikseli. Jedyne zasoby zewnętrzne to Google Fonts.
- Sprawdzone: brak przewijania w poziomie przy 390, 768 i 1440 px; brak błędów JavaScriptu;
  zero martwych odnośników.

## Czego nie należy robić

- Nie wstawiać pozycji do `OFERTA`, których nie ma w sprzedaży. Cztery przykładowe
  broszury zostały z tego powodu usunięte i zastąpione prawdziwymi.
- Nie zmieniać palety na białe tło z granatem. Fiolet `#2D1B69` z pomarańczem `#E8450A`
  jest w aplikacji, broszurach i dokumentach WOPF.
- Nie publikować dokumentów prawnych bez sprawdzenia przez prawnika — to projekty.
