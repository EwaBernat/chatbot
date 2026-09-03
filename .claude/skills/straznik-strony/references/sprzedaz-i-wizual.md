# Sprzedaż, wizualność, czytelność

## Co blokuje zakup — w kolejności ważności

**1. Brak ceny.** „Na zapytanie" przy produkcie za kilkadziesiąt złotych to nie
strategia, tylko utrata klienta. Kupujący instytucjonalny planuje budżet z wyprzedzeniem
i potrzebuje kwoty, żeby wpisać pozycję do planu finansowego. Bez niej odkłada decyzję,
czyli jej nie podejmuje. Jeśli cena naprawdę zależy od zakresu, podaj widełki
albo cenę wyjściową: „od 1 490 zł". Cisza jest najgorszą z możliwych odpowiedzi.

**2. Brak dowodu, że ktoś tego używa.** Kupujący nie ocenia produktu, tylko ryzyko
własnej decyzji. Trzy zdania z nazwą placówki i funkcją osoby robią więcej niż
cała sekcja opisu funkcji. Opinia anonimowa jest gorsza niż jej brak, bo wygląda
na wymyśloną.

**3. Nieodpowiedziane pytanie o ryzyko.** Co z moimi danymi. Co, jeśli zespół tego
nie użyje. Co po roku — czy odzyskam dokumenty. Kto to wdroży. Te pytania padają
zawsze; strona, która ich nie dotyka, zostawia je do rozstrzygnięcia po stronie
„nie kupuję".

**4. Obietnica bez liczby.** „Oszczędzasz czas" nie sprzedaje.
„3 godziny w arkuszach, 40 minut w programie — przy dwudziestu uczniach to około
45 godzin pracy zespołu w roku" sprzedaje, bo daje się przełożyć na etat i budżet.

**5. Za dużo wezwań do działania.** Trzynaście pomarańczowych przycisków znaczy
tyle samo co zero. Jedno główne wezwanie na sekcję, reszta cichsza.

**6. Elementy, które nie działają.** Przycisk prowadzący donikąd, „wkrótce"
w sześciu miejscach, licznik pokazujący liczbę, której nie ma. Pusty stan opisany
wprost buduje więcej zaufania niż atrapa.

## Ceny

Cena brutto dużą liczbą — tyle klient zapłaci. Netto i VAT mniejszym drukiem pod
spodem — tego potrzebuje księgowość. Odwrotna kolejność jest błędem: instytucja,
która nie odlicza VAT, zaplanuje za mało i poczuje się wprowadzona w błąd
przy fakturze.

Przy konsumencie cena brutto jest wymagana. Przy ofercie tylko dla firm można podać
netto, ale VAT trzeba wskazać.

## Architektura oferty przy rosnącym katalogu

Strona główna sprzedaje jedną rzecz. Kiedy dochodzą materiały poboczne, obowiązuje
zasada: **stała liczba pozycji na stronie, reszta w katalogu.**

Trzy pozycje w sekcji plus wejście do katalogu. Wtedy strona ma tę samą długość
przy pięciu i przy stu pozycjach, a uwaga zostaje na produkcie głównym.
Katalog przy większej liczbie pozycji potrzebuje wyszukiwarki, filtrów i doładowywania
po około 24 pozycje — inaczej przeglądarka na telefonie przestaje odpowiadać.

Każda pozycja powinna mieć własny adres. Treść dostępna tylko po kliknięciu
w oknie nie istnieje dla wyszukiwarki, a przy katalogu treści cyfrowych to długi ogon
zapytań odpowiada za większość sprzedaży.

## Karty produktów

Karta w siatce: okładka, adresat, tytuł, cena, przycisk. Opis, spis treści i dane
techniczne — po kliknięciu. Karta z pełnym opisem wygląda na bogatszą, a w praktyce
wydłuża sekcję trzykrotnie i sprawia, że nikt nie czyta żadnej.

## Wizualnie

**Nie każdy blok jest kartą.** Ramka, tło, zaokrąglenie i cień mówią „osobny obiekt".
Kiedy wszystko ma ten sam cień i to samo zaokrąglenie, hierarchia znika i strona
robi się płaska mimo wysiłku włożonego w cienie.

**Powtarzalne elementy komponuj jako jeden obiekt.** Karty w rzędzie mają te same
krawędzie, ten sam wewnętrzny odstęp i ten sam element w tym samym miejscu.
Liczbę kolumn dobierz do liczby elementów, żeby nie zostawał pusty slot.

**Jeden rytm przez dziesięć sekcji usypia.** Jeśli każda sekcja to „nagłówek po lewej,
lead po prawej, siatka kart pod spodem", po trzeciej oko przestaje się zatrzymywać.
Zmiana rytmu — jedna wielka liczba, jeden cytat, jedna sekcja bez kart — działa
jak akapit w tekście.

**Paleta marki nie jest do negocjacji bez powodu.** Jeśli kolory żyją już
w aplikacji, drukach i materiałach, zmiana ich na stronie rozspójnia całość.
Zasady kontrastu i przestrzeni stosuj do palety, którą marka ma — nie odwrotnie.

## Czytelność

- Tekst ciągły od 16 px, interlinia od 1,5.
- Wiersz 45–80 znaków. Powyżej oko gubi początek następnego wiersza, poniżej łamie
  co trzy słowa. Obie skrajności męczą tak samo, choć wyglądają na przeciwieństwa.
- Akapit do pięciu wierszy.
- Nagłówek mówi, co jest w sekcji.
- Na ciemnym tle: interlinia wyżej niż na jasnym, tekst o pół stopnia większy,
  kontrast wysoki, ale nie maksymalny.

## Wydajność

- Obrazy w WebP, 80–120 KB, wymiary dopasowane do miejsca wyświetlania.
  Obraz 1600 px wyświetlany na 400 px to trzykrotnie za dużo danych nawet
  przy dwukrotnej gęstości ekranu.
- `loading="lazy"` dla wszystkiego poniżej pierwszego ekranu.
- Brak przewijania w poziomie przy 390, 768 i 1440 px.
- Szerokie elementy — tabele, kod, diagramy — przewijają się we własnym kontenerze,
  nie ciągną za sobą całej strony.
