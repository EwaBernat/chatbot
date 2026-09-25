# Profil sensoryczny (model Dunn) — obserwacja modulacji sensorycznej, 7 zmysłów

Narzędzie obserwacyjne do oceny modulacji sensorycznej ucznia w 7 zmysłach
(wzrok, słuch, dotyk, smak, węch, propriocepcja, równowaga), oparte na
modelu Dunn (1997, 2014) i teorii integracji sensorycznej Ayres. Wspólna
marka i konstrukcja z serii `WOPF/` i `ToM/`.

## Test modulacji: strony za rzadko wypełnione — poprawione (3 zmysły na stronę)

Zwróciłaś uwagę, że strony testu (poprzednio po 2 zmysły, 16 pozycji) miały
za dużo pustego miejsca u dołu — margines do stopki dochodził do 337–378px.
Przełożyłam test na **3 zmysły na stronę** (Wzrok/Słuch/Dotyk, potem
Smak/Węch/Propriocepcja, Równowaga zostaje razem z Sekcją V jak wcześniej) —
strony testu zajęte teraz w większości wysokości karty (margines spadł do
56–98px), a cały dokument skrócił się dodatkowo o jedną stronę: **9 → 8
stron**. Treść bez zmian — te same 56 pozycji, tylko gęściej rozłożone.

## Przebudowa na wspólny system PCTP — „taki sam styl jak ToM"

Przesłałaś plik zbudowany w **innym systemie szablonów** niż reszta serii —
`<section class="sheet roomy autofill">` z własnym, osobnym CSS (16 stron,
naturalnie łamiących się w druku), zamiast wspólnego `.page`/`.phead`/
`.pmeta`/`.pbody`/`.pfoot` używanego w WOPF, ToM i Profilu
biopsychospołecznym. Poprosiłaś o ułożenie „w takim samym stylu jak ToM",
z charakterystyką w zwartej tabelce — „ma być jednolicie". Przebudowałam
cały dokument na wspólny system (ta sama czcionka, kolory, nagłówki sekcji,
tabele), zachowując całą treść: 56 pozycji testu, całą syntezę/zalecenia/
cele SMART, całą podstawę prawną.

**Charakterystyka jako tabelka w kształcie ToM (str. 4).** Oryginalna str. 8
miała 7 osobnych, rozlewających się kart — nagłówek zmysłu + duże puste pole
tekstowe na kartę, każda karta na swojej wysokości. Zamieniłam to na jedną
zwartą tabelkę w dokładnie tym samym kształcie, co tabele ToM w WOPF
(`obs_table`: **Nazwa (kierunek) | Wynik | Wniosek/opis**) — tu: **Zmysł
(kierunek) | Nasilenie (0–10) i poziom | Charakterystyka / obserwowane
zachowania**. 7 wierszy, jedna strona zamiast rozlanych pól.

**Synteza (charakterystyka + zalecenia + cel SMART) skrócona z 4 stron do
1 (str. 7).** Oryginał miał osobną stronę „część 1 z 4" … „część 4 z 4" na
7 zmysłów (po ok. 2 na stronę), z dużym odstępem między polami. Każdy zmysł
ma teraz zwartą kartę (nagłówek + kolorowy plakietka wyniku + trzy zdania:
Charakterystyka / Zalecenia / Cel SMART + pola Tor zajęć / Rodzaj zajęć) —
cała treść z oryginału zachowana słowo w słowo, tylko bez zbędnych odstępów.

**Wynik: 16 stron → 8 stron**, cała treść zachowana:

| Nowa strona | Zawartość |
|---|---|
| str. 1 | Tytuł, Metryczka (I), Struktura narzędzia (II), Procedura badania (III), kierunek modulacji, kontekst obserwacji, podstawa prawna |
| str. 2–3 | Test modulacji sensorycznej (IV) — 56 pozycji, po 3 zmysły na stronie |
| str. 4 | dokończenie testu (Równowaga) + Wyniki — wrażliwość zmysłów (V) — **tabelka w stylu ToM** |
| str. 5 | Wykres profilu (VI) — słupki + mapa radarowa + szybki odczyt |
| str. 6 | Zalecenia — dieta sensoryczna |
| str. 7 | Synteza — charakterystyka, zalecenia, cele SMART (karty, wszystkie 7 zmysłów) |
| str. 8 | Ewaluacja + Wnioski i decyzja |

## Do potwierdzenia przez autorkę

- **Automatyczne przeliczanie nasilenia z testu — zmienione na ręczne
  wpisanie.** Twój oryginał obiecywał, że wynik i kierunek każdego zmysłu
  „wypełniają się automatycznie z testu" (56 klikalnych kółek 0–3
  sumujących się per sektor). Nie znalazłam w przesłanym pliku
  udokumentowanego wzoru tej sumy (np. czy to suma trzech pozycji sektora,
  czy inaczej ważona), a WOPF w tej samej serii **wprost zaleca nie
  wyliczać nowego wyniku bez podstawy metodologicznej** („Nie obliczaj
  średniej ze stenów jako nowego wyniku narzędzia bez podstawy
  metodologicznej" — Sekcja V WOPF). Żeby nie zgadywać formuły, zrobiłam
  test modulacji (str. 2–4) jako zwykłe pozycje do oceny 0–3 (edytowalne
  pole, nie klikalne kółko), a **nasilenie 0–10 w Sekcji V wpisuje się
  ręcznie** — dokładnie tak samo, jak steny KSzOF w WOPF. Wpisanie liczby
  w Sekcji V od razu przelicza poziom, wykres słupkowy, mapę radarową i
  szybki odczyt (sprawdzone: zmiana wyniku Słuchu z 6 na 9 poprawnie
  przeliczyła poziom, wysokość słupka i tabelę szybkiego odczytu). Jeśli
  wolisz odtworzyć oryginalne automatyczne sumowanie z klikalnych kółek —
  podaj dokładny wzór (który sektor wygrywa przy remisie, czy suma czy
  średnia, czy jest skalowana), a dopiszę to jednym ruchem.
- **Kierunek modulacji (↑/↓/↔/●) w Sekcji V — też ręczny, nie wyliczany**
  z tego samego powodu (brak udokumentowanej reguły „co przy remisie
  sektorów"). Domyślne wartości demo (Wzrok ●, Słuch ↑, Dotyk ↑, Smak ●,
  Węch ●, Propriocepcja ↓, Równowaga ●) odpowiadają dokładnie Twojemu
  przykładowi (Zofia Lewandowska).
- **Dane przykładowe.** Wpisałam Twoje wyniki demo (1, 6, 5, 1, 1, 6, 3) do
  Sekcji V i wykresu, żeby dokument otwierał się z działającym,
  kolorowym przykładem — tak jak reszta serii. 56 pozycji samego testu
  zostawiłam puste (w oryginale też były puste — to pole robocze).
- Dokument nie jest jeszcze przeniesiony do `Zatwierdzone/`.
