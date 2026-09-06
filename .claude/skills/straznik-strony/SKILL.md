---
name: straznik-strony
description: Strażnik zasad dla stron sprzedażowych i sklepów w Polsce — sprawdza i poprawia stronę pod kątem prawnym (regulamin, RODO, prawo konsumenckie, Omnibus, cookies), dostępności WCAG, czytelności, wizualnym, sprzedażowym i bezpieczeństwa. Uruchamiaj ZAWSZE, gdy użytkownik prosi o audyt strony, sprawdzenie zgodności, „czy strona jest OK", „czego brakuje na stronie", RODO na stronie, regulamin sklepu, politykę prywatności, dostępność, WCAG, zgodność z prawem konsumenckim, przygotowanie strony do sprzedaży albo do wdrożenia. Wyzwalaj także przy: audyt UX, sprawdź stopkę, checkout, koszyk, zgody w formularzu, prawo odstąpienia, treści cyfrowe, znak wodny PDF, Core Web Vitals, kontrast, alt, meta tagi. Używaj również wtedy, gdy budujesz nową stronę sprzedażową od zera — wtedy zasady służą jako specyfikacja, a nie jako kontrola po fakcie.
---

# Strażnik strony

Zestaw zasad plus automatyczny kontroler. Zasady mówią, jak strona ma wyglądać;
kontroler sprawdza, czy tak wygląda, i wypisuje, czego brakuje.

## Kiedy czego użyć

**Budujesz stronę** → przeczytaj zasady niżej, zbuduj według nich, na koniec uruchom kontroler.
**Audytujesz cudzą stronę** → uruchom kontroler, potem przeczytaj referencje do tych obszarów,
które zgłosił, i dopiero wtedy pisz raport. Kontroler łapie to, co mierzalne;
reszta wymaga oceny.

## Dwa kontrolery

Jeden ogląda stronę oczami przeglądarki, drugi czyta pliki źródłowe.
Przed publikacją uruchamiaj **oba** — łapią zupełnie różne rzeczy.

```bash
node scripts/straznik.js <ścieżka-lub-URL> [--json] [--tylko bledy] [--ciemny]
node scripts/gotowosc.js <katalog> [--json]
```

**`straznik.js`** renderuje stronę (wymaga Playwrighta) przy trzech szerokościach
(390, 768, 1440 px): liczy kontrast, mierzy długość wiersza, waży obrazy, czyta
formularze, sprawdza nagłówki, cele dotykowe i wymogi prawa konsumenckiego.
Uruchom go dwa razy — bez przełącznika i z `--ciemny` — bo tryb ciemny potrafi
mieć własne, zupełnie inne błędy kontrastu.

**`gotowosc.js`** nie potrzebuje przeglądarki. Czyta wszystkie pliki `.html`
w katalogu i szuka tego, czego nie widać na gotowej stronie: pustych miejsc
w dokumentach prawnych, oznaczeń „do uzupełnienia", banerów „projekt dokumentu",
odnośników do plików, których nie ma, formularzy bez `action`, kluczy i haseł
w kodzie, obrazów, których nikt nie używa. Zwraca **BLOKADY** — rzeczy, przy
których publikacja jest przedwczesna.

**Narzędzie wewnętrzne to nie sklep.** Panel do wgrywania filmów albo wydruku
zaświadczeń nie ma stopki z NIP-em, nie sprzedaje i nie ma się indeksować.
Taka strona deklaruje to sama:

```html
<meta name="straznik" content="narzedzie">
```

Kontroler pomija wtedy prawo handlowe, SEO i sprzedaż, a sprawdza to, co dotyczy
każdej strony: czytelność, dostępność, kontrast, wygląd i błędy skryptu.

Oba zwracają trzy poziomy:

| Poziom | Znaczenie | Co zrobić |
|---|---|---|
| **BŁĄD** | narusza prawo albo psuje sprzedaż | poprawić przed publikacją |
| **OSTRZEŻENIE** | działa, ale szkodzi | poprawić, gdy tylko się da |
| **DO UZUPEŁNIENIA** | brakuje danych, których kod nie wymyśli | zapytać właściciela |

Kod wyjścia: `0` gdy czysto, `1` gdy są błędy albo blokady. Nadaje się do CI
i na hak `pre-push`.

**Czego kontroler nie sprawdzi:** czy treść regulaminu pasuje do tego, co naprawdę
sprzedajesz; czy zdjęcia mają licencję; czy opinie są prawdziwe; czy cena ma sens.
To zawsze zostaje do oceny człowieka — i tak trzeba to napisać w raporcie,
zamiast udawać, że zielony wynik oznacza zgodność.

## Zasada nadrzędna: nie udawaj, że coś jest

Najgorszy błąd, jaki może popełnić strona, to obiecywać rzecz, której nie ma:
przycisk „Kup" prowadzący donikąd, „Wszystkie broszury (3)", gdy są trzy,
opinia bez autora, cena „na zapytanie" przy pliku PDF za 30 zł, regulamin
skopiowany z innego sklepu.

Pusty stan opisany wprost („Profil startuje wkrótce", sekcja ukryta do czasu,
aż będzie treść) buduje więcej zaufania niż atrapa. Przy każdym elemencie pytaj:
**czy to działa naprawdę?** Jeśli nie — ukryj albo napisz, że jeszcze nie działa.

## Zasady w sześciu obszarach

Poniżej skrót. Szczegóły — z brzmieniem klauzul, progami i wyjątkami —
w plikach `references/`, czytaj je, gdy pracujesz nad danym obszarem.

### 1. Prawo → `references/prawo.md`

Sprzedaż w Polsce wymaga trzech dokumentów i kilku elementów w interfejsie.

- **Regulamin, polityka prywatności, formularz odstąpienia** — jako podstrony,
  z linkami w stopce, dostępne przed zakupem, nie po.
- **Dane sprzedawcy**: nazwa, adres rejestrowy, NIP, REGON, e-mail i **telefon**.
  Telefon jest obowiązkowy, nie opcjonalny.
- **Przycisk kończący zamówienie** musi jednoznacznie mówić o zapłacie:
  „Zamawiam z obowiązkiem zapłaty". „Wyślij", „Dalej", „Zamawiam" — za mało.
- **Zgody jako osobne checkboxy, niezaznaczone domyślnie.** Nigdy jedna zbiorcza
  zgoda na wszystko. Zgoda marketingowa zawsze osobno od akceptacji regulaminu.
- **Treści cyfrowe**: bez zgody na dostarczenie przed upływem terminu odstąpienia
  klient ma 14 dni na zwrot także po pobraniu pliku. Ta zgoda dotyczy konsumenta;
  firmy kupującej w ramach działalności zawodowej nie dotyczy — i nie należy jej
  tą zgodą straszyć.
- **Reklamacje**: 14 dni na odpowiedź. Brak odpowiedzi = uznanie reklamacji.
- **Omnibus**: przy każdej obniżce najniższa cena z 30 dni przed obniżką.
  Przy opiniach — informacja, czy i jak są weryfikowane.
- **Produkt nie dla wszystkich**: jeśli czegoś nie sprzedajesz konsumentom
  (bo kupuje to instytucja na fakturę), napisz to w regulaminie, powiedz na stronie
  i **sprawdź po stronie serwera**. Wyszarzona pozycja na liście nie jest
  zabezpieczeniem — jest podpowiedzią.
- **Sprzedaż instytucji na umowę**: gdy kupującym jest szkoła albo organ prowadzący,
  wzór umowy i protokół odbioru mają być do wglądu **przed** zamówieniem, a nie
  dopiero po. Umowa licencyjna rządzi się prawem autorskim, nie przepisami
  o sprzedaży rzeczy: są w niej uprawnienia, których nie wolno wyłączyć (art. 75
  ust. 2 i 3), fakturowanie przez KSeF i miejsce na podpis księgowego. Szczegóły
  w `references/prawo.md`, rozdziały 9–12.
- **Cookies**: baner jest potrzebny dopiero wtedy, gdy strona ładuje analitykę
  lub marketing. Strona bez skryptów śledzących nie potrzebuje banera i lepiej
  napisać to wprost, niż dokładać okienko dla ozdoby.

### 2. Dostępność → `references/dostepnosc.md`

Strona placówki edukacyjnej trafia do osób, które same pracują z niepełnosprawnością.
Niedostępna strona jest w tym kontekście podwójnie kosztowna.

- Jeden `h1`, hierarchia nagłówków bez przeskoków.
- Każdy obraz niosący treść ma `alt` opisujący treść, nie plik. Obraz dekoracyjny: `alt=""`.
- Każde pole formularza ma etykietę powiązaną z polem, nie sam placeholder.
- Kontrast tekstu: **4,5:1** dla zwykłego, **3:1** dla dużego (od 24 px albo 19 px pogrubione).
- Fokus klawiatury widoczny na każdym elemencie interaktywnym.
- Cel dotykowy co najmniej **24×24 px**, w praktyce dąż do 44 px.
- Wszystko, co da się kliknąć, da się obsłużyć klawiaturą; okna zamyka Escape.
- `prefers-reduced-motion` wyłącza animacje.
- Kolor nigdy nie jest jedynym nośnikiem informacji.

### 3. Czytelność

- Tekst ciągły **od 16 px**, interlinia **od 1,5**.
- Długość wiersza **45–80 znaków**. Powyżej oko gubi początek następnego wiersza;
  poniżej łamie co trzy słowa — obie skrajności męczą tak samo.
- Nagłówek mówi, co jest w sekcji, a nie jest hasłem reklamowym.
- Akapit do pięciu wierszy. Listy zamiast ścian tekstu.
- Na ciemnym tle: nie używaj czystej bieli na czystej czerni. Kontrast powyżej
  mniej więcej 12:1 sprawia, że jasne litery rozlewają się na ciemnym.
  Wysokie nasycenie w paśmie niebiesko-fioletowym dodatkowo rozmywa krawędzie liter.

### 4. Wizualnie → `references/sprzedaz-i-wizual.md`

- **Nie każdy blok jest kartą.** Ramka, tło, zaokrąglenie i cień mówią „osobny obiekt".
  Gdy wszystko ma ten sam cień, hierarchia znika.
- Powtarzalne elementy w rzędzie mają te same krawędzie, odstępy i wysokość.
- Jeden rytm przez dziesięć sekcji usypia. Zmień go tam, gdzie treść tego wymaga.
- Nie zmieniaj palety marki bez powodu. Spójność z aplikacją, drukami i broszurami
  jest warta więcej niż zgodność z cudzym przykładem kolorów.
- Obrazy: WebP, **80–120 KB**, wymiary dopasowane do miejsca wyświetlania,
  `loading="lazy"` poniżej pierwszego ekranu.
- Brak przewijania w poziomie przy 390, 768 i 1440 px.

### 5. Sprzedaż → `references/sprzedaz-i-wizual.md`

- **Cena musi być widoczna.** „Na zapytanie" przy produkcie za kilkadziesiąt złotych
  to nie jest strategia, tylko utrata klienta. Kupujący instytucjonalny potrzebuje
  kwoty do planu finansowego; bez niej odkłada decyzję, czyli jej nie podejmuje.
- Cena brutto dużą liczbą, netto plus VAT pod spodem. Konsument musi widzieć kwotę,
  którą zapłaci; księgowość potrzebuje rozbicia.
- Dowód, że ktoś tego używa: nazwa placówki, funkcja osoby, konkret.
  Anonimowa opinia „świetny program!" jest gorsza niż brak opinii.
- Odpowiedz na pytania o ryzyko: co z moimi danymi, co gdy zespół tego nie użyje,
  co po roku, czy odzyskam dokumenty.
- Jedno główne wezwanie do działania na sekcję. Trzynaście pomarańczowych przycisków
  na stronie znaczy tyle samo co zero.
- Obietnicę mierz liczbą. „Oszczędzasz czas" nie sprzedaje; „3 godziny w arkuszach,
  40 minut w programie" sprzedaje.

### 6. Bezpieczeństwo i dane

- Dane osobowe zbieraj tylko te, które są potrzebne do wykonania umowy.
- Formularz przez `mailto:` nie jest formularzem: na telefonie bez skonfigurowanej
  poczty zamówienie przepada po cichu, bez śladu i bez potwierdzenia.
- Pliki płatne: unikalne, wygasające linki do pobrania i znak wodny z danymi nabywcy.
  Statyczna strona tego nie zrobi — wymaga serwera; napisz to wprost zamiast obiecywać.
- Skrypty zewnętrzne tylko z zaufanych źródeł i tylko takie, które są potrzebne.
  Każdy dodatkowy skrypt to nowy powód, żeby potrzebować banera cookies.
- Nigdy nie umieszczaj w kodzie strony kluczy, haseł ani tokenów.

## Jak pisać raport z audytu

Kolejność ma znaczenie: najpierw wniosek, potem dowody.

1. **Jedno zdanie werdyktu.** Jeśli strona nie ma czegoś podstawowego — na przykład
   koszyka, choć ma sprzedawać — powiedz to na początku, zamiast prowadzić przez
   listę drobiazgów do tego samego wniosku na końcu.
2. **Liczby zamiast wrażeń.** Nie „mało cen", tylko „16 pozycji z ceną »na zapytanie«,
   zero kwot". Liczba jest sprawdzalna i trudniej ją zignorować.
3. **Konsekwencja przy każdym braku.** Nie „brak checkboxa", tylko „bez tej zgody
   klient może pobrać plik i zażądać zwrotu przez 14 dni".
4. **Podział na to, co poprawisz teraz, i to, co wymaga systemu.** Nie mieszaj
   „dodaj tag og:" z „zbuduj bramkę płatności" na jednej liście.
5. **Zastrzeżenie na końcu, raz.** Audyt techniczny to nie opinia prawna;
   dokumenty przed publikacją sprawdza prawnik, stawki VAT — księgowa.
   Napisz to raz, jasno, i nie powtarzaj przy każdym punkcie.
