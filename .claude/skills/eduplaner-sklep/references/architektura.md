# Jak zbudowana jest strona

Jeden plik `index.html`: HTML, CSS i JavaScript razem. Bez frameworka, bez kroku
budowania, bez zależności poza Google Fonts. Otwiera się z dysku podwójnym
kliknięciem i działa — to jest cecha, nie zaniedbanie. Właścicielka ma podglądać
zmiany bez uruchamiania serwera.

## Trzy tablice danych

Cała zmienna treść siedzi w trzech tablicach. Sekcje HTML są puste — wypełnia je
skrypt. Dodawanie pozycji nie wymaga dotykania znaczników.

### `OFERTA` — szkolenia, broszury, pomoce dydaktyczne

```js
{
  "id": "br-emocje",            // unikalne i stabilne; trafia do adresu #pozycja-br-emocje
  "typ": "broszura",            // szkolenie | broszura | pomoc
  "polecane": true,             // czy może stanąć na stronie (widoczne najwyżej 3)
  "hot": false,                 // wyróżniona ramka
  "badge": "Najlepszy start",   // wstążka nad kartą; pusta = brak
  "okladka": {
    "wariant": "emocje",        // klasa CSS wariantu okładki; pusta = domyślny
    "ser": "Świat kolorów · Część 1",   // linia nad tytułem
    "ttl": "Kolorowy Świat Emocji",     // tytuł na okładce
    "sub": "Pięć kolorów. Pięć emocji.",// podtytuł
    "pasy": [["#E8B426","Radość"]]      // kolorowe paski z podpisem; pusta tablica = brak
  },
  "fmt": "Zeszyt ucznia",       // linia nad tytułem karty
  "tytul": "Kolorowy Świat Emocji",
  "opis": "Jedno–dwa zdania. Widoczne w oknie szczegółów, nie na karcie.",
  "punkty": ["…", "…"],         // do trzech; skrót treści
  "spec": "PDF · 24 strony · A4",   // dane techniczne; przy szkoleniu pierwszy
                                    // człon przed „·" to czas, trafia do plakietki
  "ceny": [["Cała rada","1500 zł","brutto · do 20 osób · faktura"]],
                                // [etykieta, kwota, podpis]; jedna albo dwie pozycje
  "netto": "1219,51 zł netto + 280,49 zł VAT 23%",
  "tagi": ["WOPF","Rada pedagogiczna"],   // filtry w katalogu
  "cta": "Kup broszurę",        // napis na przycisku
  "primary": false,             // przycisk pomarańczowy zamiast obrysowanego
  "buyer": "",                  // inst | person | puste — kim ustawić kupującego po kliknięciu
  "wiecej": []                  // dodatkowe akapity w oknie szczegółów
}
```

Szkolenie ma dodatkowo:

```js
  "poziom": "podstawowy",       // podstawowy | rozszerzony | wdrożeniowy
  "tryb": "otwarte",            // otwarte (są terminy) | na zamówienie (tylko dla rady)
  "dlaKogo": "Nauczyciele, specjaliści i dyrektorzy…",
  "program": ["…","…"],         // numerowany program; zastępuje punkty w oknie
  "zawiera": ["Nagranie dostępne 30 dni"],   // co uczestnik dostaje po szkoleniu
  "zaswiadczenie": true
```

Dwie rzeczy, które łatwo pomylić:

- **`program` to przebieg zajęć, `zawiera` to co zostaje po zajęciach.** „Nagranie
  dostępne 30 dni" nie jest punktem programu. Raz już tak było i wyglądało źle.
- **`tryb: "na zamówienie"` oznacza, że pozycji nie kupi osoba prywatna.** Taka
  pozycja ma jedną cenę (dla rady) i `data-person="0"` w formularzu. Zgadzać się
  muszą obie rzeczy naraz.

### `FILMY` — nagrania w sekcji „Zobacz w działaniu"

```js
{ "id":"sp", "glowny":false, "etykieta":"", "numer":"SP", "czas":"2:29",
  "tytul":"…", "naglowek":"", "opis":"…", "url":"" }
```

Pusty `url` = kafelek nieklikalny z podpisem „wkrótce", zamiast odnośnika donikąd.
Właścicielka wypełnia to przez `panel-filmow.html` — narzędzie generuje gotową
tablicę do wklejenia. Nie każ jej edytować `index.html` ręcznie.

### `EKRANY` — zrzuty aplikacji

```js
{ plik:"img/app-wopf.webp", tytul:"WOPF — ocena funkcjonalna", opis:"…" }
```

`build_single.py` wbudowuje te ścieżki w plik podglądu, więc format zapisu
(`plik:"img/…"`) musi zostać, jak jest — skrypt szuka go wyrażeniem regularnym
i ostrzega, gdy któraś ścieżka nie została wbudowana.

### `LINKS`

```js
var LINKS = { facebook: '', blog: '' };
```

Puste = odnośniki są wyłączone i podpisane „wkrótce". Wpisanie adresu włącza je
w całym serwisie naraz.

## Stałe, które sterują wielkością strony

```js
var NA_STRONIE = 3;   // ile pozycji kategorii stoi na stronie
var NA_RAZ     = 24;  // ile pozycji katalog dokłada po kliknięciu „Wczytaj więcej"
```

Reszta pozycji mieszka w oknie katalogu, do którego prowadzi kafelek „Pełny katalog"
— czwarta komórka w siatce. Dzięki temu strona nie rośnie wraz z ofertą i nie
odciąga uwagi od aplikacji, która jest głównym produktem.

**Pusta kategoria znika**: sekcja i jej link w menu chowają się same. Tak działa
dziś `#pomoce` — nie ma pomocy dydaktycznych, więc nie ma sekcji.

## Adresy okien

Katalog i karta pozycji mają własne adresy, więc da się je wysłać mailem:

```
#katalog-szkolenie      #katalog-broszura      #katalog-pomoc
#pozycja-<id>           karta jednej pozycji
```

To proteza. Docelowo `/broszury/<slug>` — treść za krzyżykiem nie istnieje dla
wyszukiwarki, więc dziś żadna broszura nie ma szans na wynik w Google.

Przy przebudowie na prawdziwe adresy zachowaj stare hasze jako przekierowania:
właścicielka rozesłała je już w mailach.

## Motyw jasny i ciemny — trzy stany, nie dwa

Każdy kolor definiuje się **trzy razy**:

```css
:root { --ink:#221B3A; }                                   /* jasny, zawsze */
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) { --ink:#EDE9F7; }        /* ciemny z systemu */
}
:root[data-theme="dark"] { --ink:#EDE9F7; }                /* ciemny z przełącznika */
```

Kolor zdefiniowany tylko w bloku `@media` nie zadziała po przełączeniu ręcznym.
Kolor zdefiniowany tylko w `[data-theme]` nie zadziała u kogoś, kto ma ciemny
system i nie dotknął przełącznika. Trzeba wszystkie trzy.

Osobne zmienne na tekst i na tło, nawet gdy w trybie jasnym mają tę samą wartość:
`--plum` maluje powierzchnie, `--plum-text` pisze po nich. Zlanie ich w jedną
zmienną dało kiedyś 23 elementy o kontraście 1,4:1 w trybie ciemnym.

## Pułapki, które już raz zepsuły tę stronę

Każda z nich kosztowała godzinę szukania. Wszystkie są w kodzie do dziś możliwe.

1. **Kolizja nazw klas.** `.stage` było naraz sceną nagłówka i kartą etapu
   edukacyjnego. Pseudoelement nagłówka zamalował całą sekcję etapów na ciemno
   i tekst zniknął. Scena nazywa się teraz `.hero-stage`. Zanim dodasz klasę,
   sprawdź, czy nazwa nie jest już zajęta gdzie indziej.
2. **Reguły CSS zawężone do jednego rodzica.** `.offer .meta` nie działa w oknie
   szczegółów, bo tam nie ma `.offer`. Efektem był sklejony tekst i czarne koło
   (nieoprawiony SVG rozdmuchany do 300 px). Klasy używane w kilku miejscach
   opisuj bez prefiksu rodzica: `.meta`, `.netto`, `.zasw`.
3. **Delegacja zdarzeń w jednym miejscu.** Kliknięcia `[data-katalog]`, `[data-poz]`,
   `[data-order]`, `[data-video]` obsługuje jeden nasłuch na dokumencie. Przy
   przepisywaniu bloku łatwo skasować połowę obsługi i nie zauważyć — okna po
   prostu przestają się otwierać.
4. **Zamykanie okien.** `Escape`, kliknięcie w tło, przycisk „Zamknij" i przycisk
   „wstecz" przeglądarki muszą prowadzić do tego samego stanu, a adres z haszem
   ma po zamknięciu zniknąć (`history.replaceState`). Fokus jest uwięziony
   w oknie tabulatorem, dopóki okno jest otwarte.
5. **Skrypty w Pythonie zapisujące plik na końcu.** Jeżeli asercja w środku
   przerwie skrypt, wszystkie wcześniejsze zmiany przepadają bez śladu. Zapisuj
   po każdej sensownej porcji albo pracuj na kopii.

## Obrazy

WebP, 46–102 KB, 1600×1000 dla zrzutów i 1200×750 dla zdjęć sal. Pliki `.jpg`
w `img/` to źródła i **nie idą na serwer** — na serwer idą `.webp` oraz `og.jpg`
(podgląd w mediach społecznościowych wymaga JPEG-a).

`loading="lazy"` na wszystkim poniżej pierwszego ekranu. Wymiary `width` i `height`
w znaczniku, żeby strona nie skakała podczas wczytywania.
