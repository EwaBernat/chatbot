# Kwestionariusz oceny rozwoju mowy — klasy I–III

Narzędzie logopedyczne uzupełniające PCTP do wielospecjalistycznej oceny
poziomu funkcjonowania (WOPF) — 25 pozycji w 5 działach rozwoju komunikacji
(aparat artykulacyjny, artykulacja i słuch fonematyczny, rozumienie mowy,
mowa czynna, komunikacja i pragmatyka), oceniane w skali 1–5 i przeliczane
automatycznie na skalę stenową 1–10. Wspólna marka i konstrukcja z serią
`WOPF/`, `ToM/`, `FBA_kwestionariusz/` — trzy warianty wiekowe (`klasy_1-3/`,
`klasy_4-6/`, `klasy_7-8/`), analogicznie do `ToM/`.

## Skąd ten druk

Przesłałaś `kwest_mowy_1_3.html` — kompletne, działające źródło (klikalne
kółka oceny 1–5, automatyczne przeliczanie na sten wg udokumentowanej
formuły percentylowej, wykresy słupkowy i radarowy, wnioski, cele SMART,
plan terapii, podstawa prawna z bibliografią logopedyczną), ale w **innym
systemie szablonów** (`<section class="sheet roomy itempage/autofill">`,
5 stron, własny CSS) niż reszta serii, z płaskim tekstowym „PCTP" zamiast
prawdziwego loga. Przebudowany na wspólny system PCTP
(`.page`/`.phead`/`.pmeta`/`.pbody`/`.pfoot`, `base_css.html`), z prawdziwym
logo, zachowując całą treść i logikę.

## Formuła stenowa — zachowana automatyczna

Wynik działu (suma 5 pozycji × 1–5 = 5–25 pkt) przelicza się na sten 1–10
wg tej samej formuły procentylowej, co już używana w KSzOF/WOPF w tej samej
serii (progi 30,77% i 68,27% rozkładu normalnego) — w pełni udokumentowana
w źródle, więc **zostaje automatyczna** (w odróżnieniu od Profilu
sensorycznego w tej samej sesji, gdzie brak udokumentowanej formuły
wymusił wpis ręczny). Kliknięcie kółka 1–5 przy dowolnej pozycji przelicza
na żywo: Σ przy nagłówku działu, wiersz w tabeli „Szybki odczyt", wysokość
słupka i punkt na mapie radarowej oraz „Wynik ogólny".

## Poprawione błędy ze źródła

Weryfikując treść znalazłam dwa niezamierzone błędy w przesłanym pliku —
poprawione tutaj, nie odtworzone:

- **Podwójna numeracja sekcji „VI".** Źródło numerowało sekcje rzymskimi
  cyframi w poprzek wszystkich stron, ale strona z celami terapii
  zaczynała się od „VI" (tak samo jak poprzedzająca ją sekcja „Działy
  wymagające terapii"), zamiast kontynuować na „VII". Tutaj numeracja jest
  ciągła: I–IX bez powtórzeń.
- **Klasa SMART bez CSS.** Ramka „Cele SMART" w źródle używała klas
  (`.smart`, `.smart-h`, `.goal`…) zdefiniowanych tylko w starym systemie
  szablonów — po przeniesieniu do wspólnego `base_css.html` (który ich nie
  ma) renderowała się jako zwykły, niesformatowany tekst. Dodałam brakujący
  CSS w stylu rodziny (pomarańczowa ramka, plakietki S-M-A-R-T).

## Co zmienione przy przebudowie strukturalnej

**5 stron → 4 strony**, cała treść zachowana. Test w starym systemie
mieścił średnio 2–3 działy na stronę; w bardziej przestronnym nagłówku
rodziny (phead+pmeta) to zostawiało nawet 600px pustego miejsca na
niektórych stronach. Po drodze natrafiłam też na ten sam błąd co przy FBA:
elementy `.ta` (karty z wykresem) automatycznie rozciągają się, żeby
wypełnić puste miejsce na stronie — bez jawnego `flex:0 0 auto` to
ukrywało prawdziwą wysokość treści (karta z wykresem słupkowym/radarowym
rozciągała się niewidocznie, zostawiając pustą przestrzeń w środku swojej
własnej ramki zamiast na dole strony). Naprawione przez jawne wyłączenie
tego rozciągania na obu wykresach, po czym dopiero poprawnie rozłożyłam
treść:

| Nowa strona | Zawartość |
|---|---|
| str. 1 | Tytuł, etap/źródło informacji, Metryczka (I), Arkusz kwestionariusza (II) — skala + działy I–III (15 pozycji) |
| str. 2 | dokończenie arkusza — działy IV–V (10 pozycji), Wykres słupkowy (III) + szybki odczyt + wynik ogólny + progi |
| str. 3 | Mapa radarowa (III c.d.) + opis merytoryczny, Podsumowanie działów (IV), Mocne strony (V), Działy wymagające terapii (VI) |
| str. 4 | Wskazanie do diagnozy pogłębionej + powiązanie z WOPF/IPET, Cele SMART (VII), Formy terapii (VIII), Ćwiczenia i dostosowania (IX), ewaluacja, podpisy, podstawa prawna |

## Zweryfikowane

- Brak przepełnień i brak nadmiaru pustego miejsca (margines do stopki
  9–86px na wszystkich 4 stronach).
- Zero błędów JS w konsoli.
- Interaktywność sprawdzona automatycznie: kliknięcie kółka oceny poprawnie
  przelicza sumę, sten i poziom działu (sprawdzone na żywym przykładzie:
  10→13 pkt poprawnie dało sten 3→5, Poziom III→II), plakietkę w tabeli
  arkusza, wysokość słupka wykresu i „Wynik ogólny"; checkbox i radio
  (etap/źródło informacji) przełączają się poprawnie; pola metryczki
  synchronizują się między wszystkimi 4 stronami.

Dokument nie jest jeszcze przeniesiony do `Zatwierdzone/` — czeka na Twoje
potwierdzenie punktów wyżej.
