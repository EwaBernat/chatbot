# eduplaner2026.pl — audyt i nowy projekt

Analiza na podstawie zrzutów strony (wrzesień 2026). Nowy projekt: `index.html` w tym katalogu.

## Co jest nie tak w obecnej wersji

### Hierarchia i treść
1. **Nagłówek hero ma pięć wierszy** i dwa kolory o tej samej wielkości. Czarne „Ocena funkcjonalna WOPF i IPET / PEWS” i fioletowe „— wszystko w jednym miejscu…” konkurują ze sobą; oko nie wie, co jest tytułem.
2. **Akapit pod nagłówkiem ma dziewięć linijek.** To treść z ulotki, nie z hero. Skróty (WOPF, KSzOF, ICF, ToM) pojawiają się, zanim ktoś je wyjaśnił.
3. **Liczby w kafelkach są niejasne lub sprzeczne.** Plakietka mówi „3 moduły edukacyjne”, kafelek „10 modułów w jednym ekranie”. „1 → 2” i „0 dokumentów pisanych od zera” wymagają domyślania się. Zero jako duża liczba czyta się negatywnie.
4. **Główne wezwanie do działania nie jest w hero.** „Złóż zamówienie” siedzi tylko w menu; w hero jest sam biały przycisk „Zobacz, jak to działa”.
5. **Opis sekcji Filmy nie zgadza się z zawartością.** Tekst mówi „wprowadzenie i trzy moduły po kolei”, a poniżej jest sześć filmów: wprowadzenie, „Szkoła podstawowa” i bloki A–D.

### Nawigacja
6. **Osiem pozycji w menu plus przycisk** to za dużo; linki są cienkie i jasnofioletowe na kremie, słabo widoczne.
7. **Pasek standardów (STANDARD WOPF · KSZOF · …) jest przyklejony pod nagłówkiem.** Razem zabierają ok. 150 px wysokości ekranu na stałe, a pasek wygląda jak drugie menu, choć niczego nie otwiera.
8. **Logo i nazwa są za duże** (ok. 80 px) w stosunku do reszty nagłówka.

### Obraz i tło
9. **Zdjęcie stockowe kobiety z laptopem** nie pokazuje produktu; ekran laptopa jest nieczytelny. Różowy prostokąt-cień przesunięty pod zdjęciem wygląda na błąd, a obraz siedzi niżej niż tekst.
10. **Siatka linii w tle plus poświaty gradientowe** dają wizualny szum, który przebija przez karty.
11. **Duży film ma na środku szary półprzezroczysty prostokąt** zasłaniający twarz prowadzącej. Wygląda na niedokończony element (podpis lub podgląd) i psuje najważniejszy kadr strony.
12. **Krzyżyki w rogach kart (znaczniki cięcia)** to gadżet z programu graficznego, nie element interfejsu.

### Karty filmów
13. Przycisk odtwarzania zasłania twarz na każdej miniaturze; tekst na miniaturach ma 6–8 px i jest nieczytelny.
14. Pięć kart w siatce trzykolumnowej zostawia pusty slot w drugim rzędzie.
15. Kategorie mieszają porządki: „Szkoła podstawowa” obok „Szkolenie · Blok A”.
16. Przycisk „Obejrzyj film na YouTube” dubluje przycisk odtwarzania tuż nad nim.

### Spójność
17. Przycisk w menu ma twardy, przesunięty cień (styl 3D), reszta strony używa miękkich cieni.
18. Paleta rozrasta się do sześciu tintów (krem, róż, lawenda, fiolet, pomarańcz, szary), zamiast trzymać się marki: fiolet `#2D1B69` + pomarańcz `#E8450A`.
19. Cienka waga fontu w akapitach na kremowym tle daje słaby kontrast.

## Co zmienia nowy projekt

- **Jeden tytuł, jedna myśl.** „Ocena funkcjonalna i IPET w jednym miejscu.” Dwa zdania leadu, dwa przyciski obok siebie (zamówienie + film), trzy liczby w jednym rzędzie z jasnymi podpisami.
- **Makieta aplikacji zamiast zdjęcia stockowego.** Ekran WOPF z dziewięcioma obszarami KSzOF, skalą 1–5, stenem i poziomem wsparcia — czyli to, co produkt naprawdę robi. Plakietka „IPET · druk A4 gotowy” pokazuje efekt.
- **Nawigacja 5 pozycji + przycisk**, nagłówek 72 px, pasek standardów jako spokojny rząd chipów pod hero (nieprzyklejony).
- **Filmy: jeden wyróżniony + lista pięciu.** Rozwiązuje pusty slot, porządkuje taksonomię (SP, A, B, C, D), czasy trwania w kolumnie, suma minut pod listą.
- **Ścieżka ucznia jako ponumerowany proces** na ciemnym fiolecie. Numeracja ma sens, bo kolejność jest częścią treści.
- **Etapy jako trzy równe karty** plus jeden pasek modułów wspólnych.
- **Cennik przejrzysty**: karta subskrypcji i lista „co składa się na cenę” (z materiałów marki), bez presji sprzedażowej.
- **Typografia:** Bricolage Grotesque (nagłówki) + IBM Plex Sans (tekst), oba z polskimi znakami; liczby tabelaryczne.
- **Tryb ciemny i jasny** z jednego zestawu tokenów; brak poziomego przewijania; widoczny fokus klawiatury.

## Wersja sprzedażowa (aktualna)

Po uwagach: strona ma sprzedawać aplikację, a szkolenia i broszury mają ją wspierać.
Kolejność sekcji prowadzi od problemu do zamówienia:

1. Hero z realnym terminem (rok szkolny 2026/2027), dwa przyciski: „Zamów dla placówki” i „Umów pokaz”.
2. „Co się zmieniło” — dotychczas kontra od 2026/27, czyli dlaczego placówka musi to mieć.
3. Aplikacja: ścieżka ucznia w pięciu krokach i dziesięć modułów.
4. Porównanie „Arkusze czy aplikacja” w tabeli.
5. Etapy, bezpłatne filmy jako wejście do szkoleń.
6. Szkolenia i broszury z dwiema cenami: placówka (faktura) i osoba indywidualna (online).
7. „Jak kupujesz”: dwie drogi zakupu w trzech krokach każda.
8. Cennik w trzech kolumnach z aplikacją jako główną ofertą.
9. Autorka, FAQ przed zakupem.
10. Formularz „Zamów w 2 minuty”: przełącznik placówka / osoba, wybór pozycji, podsumowanie i przycisk.
    Każdy przycisk „Zamów”, „Kup”, „Zapisz się” na stronie ustawia w formularzu właściwą pozycję.

Formularz bez backendu składa gotową wiadomość e-mail z treścią zamówienia.
Do wdrożenia: podłączenie do własnego endpointu lub Formspree i bramki płatności
(Przelewy24 / Stripe) dla osób indywidualnych.

## Jak podmienić zrzuty ekranu na własne

Strona czyta obrazy z katalogu `img/`. Wystarczy wgrać pliki o tych nazwach (JPG, najlepiej 1280×800 px lub 1920×1200 px, kadr od góry ekranu):

| Plik | Gdzie się pokazuje |
|---|---|
| `img/ekran-obserwacje-wopf.jpg` | hero (główna ramka), taśma ekranów, galeria |
| `img/ekran-druk-ipet.jpg` | hero (druk za ramką), taśma, galeria |
| `img/ekran-karta-start.jpg` | taśma ekranów |
| `img/ekran-karta-wopf.jpg` | taśma, galeria |
| `img/ekran-baza.jpg` | taśma, galeria |
| `img/autorka.jpg` | portret autorki (proporcje 4:5); bez pliku pokazują się inicjały |

Po podmianie uruchom `python3 build_single.py`, a w `dist/eduplaner2026.html` powstanie
wersja jednoplikowa z wbudowanymi obrazami (do wysyłki lub podglądu). Do wdrożenia na serwer
wystarczy wgrać `index.html` razem z katalogiem `img/`.

## Prawdziwe ekrany aplikacji

Hero i sekcja „Aplikacja” pokazują rzeczywiste zrzuty z aplikacji EduPlaner 2026
(Moduł Realizacji Zajęć z drukiem IPET oraz Karta Funkcjonalna WOPF), wyrenderowane
z plików w skillach `eduplaner-zajecia-ipet` i `eduplaner-pctp` z przykładowym uczniem
Janem Kowalskim. Zrzuty są w katalogu `img/`; `index.html` odwołuje się do nich ścieżką, a `build_single.py` składa wersję jednoplikową.

## Do uzupełnienia przed wdrożeniem

Miejsca oznaczone w `index.html` komentarzem `TODO`:
- linki do filmów w YouTube (sześć adresów),
- zdjęcie autorki (proporcje 4:5) w miejsce bloku z inicjałami,
- jeśli chcesz, zrzuty z produkcyjnej wersji aplikacji w miejsce obecnych (te same miejsca w hero i galerii),
- ceny: subskrypcja roczna, każde szkolenie i każda broszura, osobno dla placówki i osoby indywidualnej,
- prawdziwe tytuły broszur i formaty szkoleń (obecne są przykładowe),
- backend formularza i bramka płatności online,
- opisy modułu przedszkolnego i ponadpodstawowego — w projekcie są ogólne, warto je doprecyzować pod realny zakres.
