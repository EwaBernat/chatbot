# Strażnik wyglądu druku

**Pilnuje:** każda kartka A4 wygląda tak samo — rama, typografia, elementy, zapełnienie.
**Podstawa w kodzie:** `shared/druki/SzablonDruku.tsx` · `shared/ui/print/print-paginacja.ts` ·
`shared/ui/druk2026/*.css` (4000 linii, 287 klas).
**Zakres:** 78 druków przedszkola w sześciu modułach.
**Sprawdzono:** 2026-08-22 — pokrycia z zwiadu E19, liczone **po grafie importów**, nie po tekście.

> Ten dokument jest pisany tak, żeby dało się sprawdzić druk **bez otwierania kodu**. Nazwy klas
> stoją w ostatniej kolumnie jako rozstrzygnięcie techniczne, nie jako treść reguły.

---

## 1. Rama — druk daje środek, resztę niesie szablon

Druk podaje `sekcje` i `nazwaKartki`. Nagłówek, listwa tożsamości, pasek narzędzi, stopka
i podpis „Opracowała…" **przychodzą z szablonu**. Wspólną ramę dziedziczy **78/78 druków** — A4,
nagłówek, metryka, stopka i fizyka PDF mają jeden punkt sterowania.

- **W1** Druk nie renderuje własnego nagłówka, stopki ani podpisu.
- **W2** Druk **nie liczy stron** — robi to silnik i sam podaje „Strona X z Z".
- **W3** Szablon nie przyjmuje: kompaktowej stopki, własnego renderu strumienia, własnej numeracji.
- **W4** Pomoc ekranowa idzie przez sloty nad kartką — zawsze `no-print`, poza treścią.
- **W5** Metryczka zaraz po tytule i podstawie prawnej; podpis pod kartką; **we wnętrzu druku
  nazwiska autorki nie ma** — miejsce podpisu opisuje rola albo sam wyraz „Podpis".
- **W6** Data wpisywana ręcznie ma kalendarz; data z kartoteki nie.

## 2. Typografia — drabina, którą trzyma kod

| Element | Rozmiar | Gdzie |
|---|---|---|
| Tytuł druku | **24 px**, interlinia 1,14 | jedyny duży element na kartce |
| Wprowadzenie pod tytułem | 12 px, interlinia 1,55 | |
| Tytuł sekcji | **12,5 px**, grubość 800, wersaliki | plus numer w plakietce |
| Tytuł grupy | 11,5 px, grubość 800 | wewnątrz sekcji |
| **Treść robocza** | **10,6 px** | komórki tabel, pola, proza drobna — **najczęstszy rozmiar na kartce** |
| Etykiety, chipy, klauzule | 9 px | drugi co do częstości |
| Stopka i podpis | 8,5 px | |

⚠️ **Dwa sprostowania wobec poprzedniej wersji tego dokumentu** (znalezione w zwiadzie E19,
potwierdzone w kodzie 2026-08-22):

| Było napisane | Jest naprawdę |
|---|---|
| „treść 12 px" | **treść robocza to 10,6 px** — 12 px ma wprowadzenie i część nagłówków |
| „nic poniżej 9 px w treści" | **nieprawda**: cztery widgety (etykieta i jednostka KPI, cel importowany, przypis półrocza) mają **8 px**, stopka 8,5 px, a motyw dodatkowy schodzi do 6,8 i 6,6 px |

**Reguła zastępcza dla dolnego progu:** zamiast zakazu obowiązuje **zamknięta lista wyjątków**.
Rozmiar poniżej 9 px wolno mieć wyłącznie tym elementom, które są tu wymienione; nowy element
poniżej 9 px jest naruszeniem, dopóki nie trafi na listę wraz z powodem.

### Kolory kartki

| Rola | Wartość |
|---|---|
| Teksty, tytuły, nagłówki | `#2D1B69` fiolet |
| **Plakietka numeru sekcji — domyślnie** | **`#E8450A` pomarańcz** |
| Ramka pól i zaznaczeń | `#cbc0e7` — **świętość kanonu, wygrywa nad wzorem** |
| Powierzchnia pola | `#FAF9FD` |
| Zebra tabeli | `#faf7f2` |
| Separatory | `#e9e7f7` / `#e4e1ec` |
| Opisy pomocnicze | `#6f6a7d` |

⚠️ **Trzecie sprostowanie:** poprzednia wersja mówiła, że numery sekcji są fioletowe. **Domyślnie
są pomarańczowe**; fiolet, czerwień, błękit i zieleń wchodzą dopiero z jawnym wariantem sekcji.
Pomyłka wzięła się z opisu tokena w kodzie — komentarz mówił jedno, wartość drugie.

Kartka jest **biała**. Kolor modułu na nią nie wchodzi.

## 3. Dualizm — dwie warstwy, każda z własnym prawem

**Warstwa 1 — struktura zbierania, z materiału.** Checkbox zostaje checkboxem, skala skalą.

**Warstwa 2 — wynik i wykres, obowiązkowe także wtedy, gdy materiał ich nie ma.**

| Co druk zbiera | Wynik | Wykres |
|---|---|---|
| skale 1–5 | średnia + kwalifikacja wg progów 4,0 / 3,0 / 2,0 | słupki + radar + szybki odczyt |
| zaznaczenia | udział zaznaczonych w grupie (np. 12 z 19) | słupki + radar po grupach |
| zdarzenia i funkcje | rozkład, funkcja dominująca | wykres rozkładu |

⚠️ „Materiał nie ma wykresu" **nie jest** powodem, żeby go nie zrobić.

## 4. Układ kartki — czego nie lubimy

Kartka A4 ma **1123 px** przy 96 dpi; próg treści silnik liczy na żywo.

- **U1 · Nie lubimy pustych kartek.** Kartka inna niż ostatnia wypełniona w mniej niż **⅔** jest
  podejrzana. Silnik zwraca zajętość każdej kartki — to liczba do sprawdzenia, nie wrażenie.
- **U2 · Nie lubimy tytułu na końcu kartki.** Nagłówek schodzi na następną kartkę **razem**
  z pierwszym blokiem treści. Sekcja bez tej flagi to naruszenie — mechanizm istnieje, ale
  zadziała tylko, gdy druk go użyje.
- **U3 · Zero przepełnień.** Blok wyższy niż kartka trzeba pociąć.
- **U4 · Ostatnia kartka może być niepełna** — jedyny dopuszczalny luz.
- **U5 · Nie dosypujemy treści dla zapełnienia.** Pustkę likwiduje lepsze cięcie sekcji.

## 5. Elementy kartki

### 5.1. Tabele — **68/78 druków**

Wspólna tabela: **fioletowy nagłówek, biały tekst, cienka kratka, kremowy co drugi wiersz**.

| Cecha | Wartość |
|---|---|
| szerokość | pełna |
| ramka | 1 px, fiolet |
| nagłówek | 10,6 px, grubość 700 |
| komórka | 10,6 px |
| zebra | `#faf7f2` |
| kolumna „Lp." | wąska, wyśrodkowana, pomarańczowa |

⚠️ **Wariant „mały" nie ma dziś mniejszej czcionki** — nazwa opisuje zamiar, nie wygląd.
Wariant „kompaktowy" zmniejsza tylko odstępy wewnętrzne, nie tekst.

**15 druków używa wyłącznie surowej tabeli**, poza wspólnym komponentem — patrz wyjątki.

### 5.2. Pola — **61/78 druków**

| Element | Jak wygląda | Pokrycie |
|---|---|---:|
| Kafel pola | jasne tło, jasnofioletowa ramka, mała etykieta nad wartością | 61/78 |
| Pole tekstowe | sama wartość, bez ozdobników | 61/78 |
| Lista wyboru | na ekranie kontrolka, **w PDF sam wybrany tekst** | 27/78 |
| Wartość stała | wartość bez udawania kontrolki | 3/78 |
| Chipy | edytor na ekranie, czysty tekst w PDF | 2/78 |

Siatka pól ma domyślnie **dwie kolumny**; warianty to jedna, trzy albo pełna szerokość.
Pole wielolinijkowe ma pojemność 1–5 wierszy. **Na ekranie nadmiar się przewija, w PDF musi być
widoczna cała treść** — repaginacja po tej rozbudowie jest dozwolona i oczekiwana.

Miejscowość i data stoją obok siebie i czytają się jako jeden ciąg.

### 5.3. Zaznaczenia i skale — **37/78 druków**

⚠️ **Kod utrzymuje dwa różne checkboxy**: fioletowy kafel **16 px** (7 druków) i pomarańczowa
opcja **13 px** (30 druków). To jest realna niespójność do rozstrzygnięcia — albo strażnik opisze
role obu, albo trzeba je ujednolicić.

Skale punktowe ma 8/78 druków, klocki wyniku 19/78, chipy statusu 14/78.

### 5.4. Ramki i wyróżnienia — **62/78 druków**

Callout, nota i blok „Podstawa prawna". Tony kolorów: fioletowy, pomarańczowy, czerwony, błękitny,
zielony, bursztynowy — każdy z własnym tłem i linią. Sam blok podstawy prawnej dociera do 55/78.

### 5.5. Nagłówki — **76/78 druków**

Sekcja: numer w plakietce + tytuł wersalikami. Dwa druki mają własną warstwę poza tą rodziną.

### 5.6. Przyciski i kontrolki

Na papierze **nie ma nic klikalnego**. Kontrolki dodawania i usuwania wierszy, selektory i modale
są **wyłącznie ekranowe** — w PDF zostaje sama wartość.

⚠️ Przycisk „Dodaj" stoi dziś **po lewej**, mimo że opis w kodzie mówi „po prawej".

### 5.7. Odstępy

Wartości, po których poznaje się, że blok „nie leży tak jak reszta":

| Miejsce | Odstęp |
|---|---|
| między fragmentami treści | 2 px |
| sekcja | 8 px nad i pod |
| pola w siatce | 4 px |
| kafle zaznaczeń | 4 px |
| opcje na liście | 6 px |
| tabela | 6 px nad, 10 px pod |
| blok podpisów | 16 px nad, 34 px między kolumnami |
| blok wyniku | 6 px nad, 12 px pod |

⚠️ **Odstępu niewidocznego dla pomiaru nie dokładamy.** Cień i obrys nie zmieniają mierzonej
wysokości — jeżeli blok ma zająć więcej miejsca, robi to marginesem, nie efektem. Inaczej silnik
policzy kartkę inaczej, niż wygląda.

## 6. Ekran kontra PDF

To jest źródło najczęstszych niespodzianek, więc reguła jest jedna: **PDF pokazuje treść, nie narzędzia**.

| Na ekranie | W PDF |
|---|---|
| lista wyboru jako kontrolka | sam wybrany tekst |
| edytor chipów | czysty tekst |
| przyciski dodawania i usuwania | nic |
| przewijane pole wielolinijkowe | **cała treść**, z repaginacją |
| zaokrąglenia i cienie kontrolek | płaska kratka |

## 7. Motyw dodatkowy

Dostępny w **78/78 druków**, ale działa **wyłącznie po świadomym wyborze**. Zmienia nie tylko
ozdobniki: przestawia skalę tekstu, tabele, pola i zebrę, a najdrobniejsze elementy schodzi
do 6,8 i 6,6 px. Druk oceniany w tym motywie to **inny wygląd** — porównuj z tym samym motywem.

## 8. Jak sprawdzać

**Obecność szablonu i komponentów sprawdza się po grafie importów, nigdy po tekście jednego pliku.**
Zwiad E19 przeszedł ścieżkę `trasa → korzeń widoku → barrel → graf importów → komponent` dla
wszystkich 78 tras. Sonda naiwna daje fałszywe alarmy wszędzie tam, gdzie druk dziedziczy przez
wspólny widok — na przykład 12 konspektów.

Liczby kartek i zajętości **nie zmierzysz w oknie w tle** — wyłącznie headless.

## 9. Czego ten strażnik nie sprawdza

Treści kartki (`straznik-merytoryki`) · zapisu pól (`straznik-danych`) · skąd biorą się wartości
(`straznik-synchronizacji`) · wyglądu aplikacji (`straznik-powloki`) · przepisów (`straznik-prawo`).

## 10. Wyjątki

| Co | Ile | Powód | Stan |
|---|---:|---|---|
| Druki wyłącznie na surowej tabeli | **15/78** | dwanaście konspektów plus dwa druki zespołu i jeden dyrektorski | **dług do rozstrzygnięcia**: migracja albo zatwierdzony wyjątek |
| Druki z własnym arkuszem CSS | **5/78** | od 119 do 166 linii każdy | nie usuwać bez porównania wizualnego |
| Konspekty na osobnym arkuszu | **12/78** | 910 linii wspólnych dla rodziny | dziedziczą ramę przez wspólny widok — **nie jest to naruszenie** |
| Prototyp typografii | **1/78** | podnosi tytuł sekcji do 12,5 px | jedyna realna zmiana, jaką wykonuje |
| Dwa systemy checkboxów | 7/78 i 30/78 | historyczny podział | **do ujednolicenia albo opisania ról** |
| Dwa druki poza rodziną nagłówków | 2/78 | własna warstwa | dług |

## 10a. Kiedy druk przechodzi

Lista do odhaczenia przy odbiorze — **ostatni punkt jest najważniejszy**:

- używa wspólnej ramy i **nie liczy sam stron**;
- każdy widoczny element ma wariant z tego dokumentu **albo jawny wyjątek**;
- nie tworzy lokalnego duplikatu wspólnego widgetu;
- kontrolki ekranowe **nie trafiają do PDF**;
- zaznaczenia i wartości **zostają** w PDF;
- każde pole pokazuje w PDF **pełną treść** — bez przewijania i bez ucięcia;
- kolory i typografia wynikają z kanonu albo z wybranego motywu;
- nie ma przepełnień, samotnego nagłówka ani pustej ostatniej strony;
- ekran i PDF sprawdzone headless **na danych granicznych** — długi tekst, maksimum wierszy;
- **Ewa potrafi opisać zgodność bez znajomości nazw klas.**

Wynik negatywny podaje: **druk · element · regułę · zrzut ekranu albo PDF · pomiar**.
Samo „wygląda inaczej" nie jest zgłoszeniem.

## 11. Sonda

Do przerobienia: `smoke-probe-uklad-kartek.mjs`, `smoke-druk.mjs`.
**Brakuje kontroli zajętości kartek (U1), flagi nagłówka (U2) oraz adopcji wspólnej tabeli (§5.1).**
