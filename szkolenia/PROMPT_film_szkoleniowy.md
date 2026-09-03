# Prompt: 2-godzinne szkolenie rady pedagogicznej jako film

Gotowy do wklejenia w nowej sesji Claude Code. Materiał źródłowy:
`szkolenia/Scenariusz_szkolenia_dokumentacja_przedszkolna_2026-2027.docx`
(54 strony, po audycie Strażnika Prawa) oraz druki: Metryczka i KPOF A/B/C.

---

## TREŚĆ PROMPTU

> Zrób film szkoleniowy dla rady pedagogicznej przedszkola na podstawie pliku
> `szkolenia/Scenariusz_szkolenia_dokumentacja_przedszkolna_2026-2027.docx`
> z tego repozytorium. Użyj skilla **dane-i-glos**: narracja moim sklonowanym
> głosem z ElevenLabs, obraz w Remotion. Marka PCTP.
>
> **ZANIM COKOLWIEK ZACZNIESZ — ETAP 0.** Skill nie ma jeszcze zapamiętanego
> mojego głosu. Sprawdź `skonfiguruj_glos.py --pokaz`. Jeżeli nadal pusto,
> zatrzymaj się i powiedz mi, ile nagrań mam dostarczyć — nie generuj ani
> jednej sekundy dźwięku cudzym głosem i nie renderuj filmu bez mojego głosu.
> Do czasu, aż dam nagrania, rób wszystko, co głosu nie wymaga: scenariusze
> narracji, sceny, animacje druków, ilustracje.
>
> **STRUKTURA — sześć modułów, film około 50 minut, szkolenie 120 minut.**
> Film nie ma trwać dwóch godzin. Dwie godziny trwa szkolenie: film przeplatany
> ćwiczeniami na sali. Rozpisz agendę 120 minut i powiedz, kiedy prowadzący
> zatrzymuje odtwarzanie.
>
> | Moduł | Temat | Czas filmu |
> |---|---|---|
> | M1 | Podstawa prawna — co było, a co jest od 1 września 2026 | 9 min |
> | M2 | Jakie dokumenty tworzymy i jak jeden wynika z drugiego | 6 min |
> | M3 | Metryczka — jak ją stworzyć i jak wypełniać | 7 min |
> | M4 | KPOF — budowa, skala, liczenie wyniku, odczyt profilu | 12 min |
> | M5 | Obserwacja pogłębiona: ABC, profil sensoryczny, ToM | 7 min |
> | M6 | WOPF → IPET → cele SMART → ewaluacja → poradnia | 9 min |
>
> Kolejność jest obowiązkowa: **najpierw prawo, potem jakie dokumenty
> powstaną, potem jak je tworzyć, na końcu jak je wypełniać.** Nie zaczynaj
> od druku.
>
> **NOWE SCENY REMOTION — szablon skilla ich nie ma, napisz je.** Istniejące
> typy (`tytul`, `liczba`, `wykres`, `wniosek`) nie wystarczą. Dodaj do
> `src/sceny/` i rozszerz `typy.ts`:
>
> - `Przepis.tsx` — karta aktu prawnego: sygnatura Dz.U., tytuł, status,
>   data wejścia w życie. Wjeżdża jak pieczęć, sygnatura pojawia się ostatnia.
> - `Porownanie.tsx` — dwie kolumny „było / jest", odsłaniane po kolei,
>   prawa strona podświetlana pomarańczem dopiero po lewej.
> - `Sciezka.tsx` — sześć przystanków obiegu dokumentów, strzałki rysowane
>   po kolei, aktywny przystanek powiększony.
> - `Druk.tsx` — **animacja wypełniania druku**, najważniejsza scena filmu.
>   Tło: prawdziwa strona druku jako PNG. Na wierzchu ramka podświetlająca
>   pole i tekst dopisujący się znak po znaku, w rytmie narracji.
>   Props: `{obraz, pola: [{x, y, szer, wys, tekst, odSek, doSek}]}`.
> - `Profil.tsx` — profil KPOF d1–d9: dziewięć słupków, próg 2,0 i 3,0
>   jako linie, słupki poniżej progu w kolorze uwagi, podpisy obszarów.
> - `CelSMART.tsx` — cel życzeniowy przekreślany, w jego miejsce wjeżdża
>   cel SMART, a pod nim zapalają się kolejno litery S-M-A-R-T.
> - `Ilustracja.tsx` — ilustracja pełnoekranowa z podpisem, tekst na płaszczyźnie
>   przyciemnienia, nigdy wprost na grafice.
>
> **DRUKI DO ANIMACJI — przygotuj je z prawdziwych plików.** Weź Metryczkę
> i KPOF A/B/C, przekonwertuj przez `soffice --convert-to pdf`, potem
> `pdftoppm -r 150 -jpeg`, i użyj tych stron jako tła scen `Druk`.
> Zanimuj co najmniej: metryczkę sekcje I, VI i VII; arkusz KPOF —
> zaznaczanie ocen 1–5 i N w kilku twierdzeniach; podsumowanie KPOF —
> liczenie średniej obszaru; kartę celu SMART; kartę ewaluacji.
> Dane w animacjach mają być **fikcyjne** — żadnego prawdziwego dziecka.
>
> **ILUSTRACJE.** Wygeneruj je (`creative_generate_image` z ElevenLabs),
> nie bierz zdjęć stockowych bez licencji. Styl jeden dla całego filmu:
> spokojne, jasne, płaskie ilustracje wnętrza przedszkola i pracy zespołu,
> paleta zgodna z marką, bez rozpoznawalnych twarzy dzieci. Po jednej
> ilustracji otwierającej każdy moduł.
>
> **PALETY NIE ZMIENIAJ.** `marka.ts` przeszedł sześć testów dostępności:
> `#2D1B69` to tekst, `#5B3FA8` to wypełnienie słupków, `#E8450A` wyłącznie
> wartość wymagająca uwagi i zawsze z podpisem. Nie rób pomarańcza „kolejną
> serią" i nie używaj ciemnego fioletu jako wypełnienia.
>
> **NARRACJA.** Zasady z `references/narracja.md`: 150 słów na minutę, jedno
> zdanie jedna myśl, maksimum 20 słów, bez „jak widać na slajdzie". Liczby
> i sygnatury zapisuj tak, jak się je czyta: „Dziennik Ustaw z dwa tysiące
> dwudziestego szóstego roku, pozycja czterysta dwadzieścia osiem",
> „czternastego kwietnia dwa tysiące dwudziestego szóstego roku",
> „paragraf siódmy ustęp szósty i siódmy". Inaczej lektor przeczyta to źle,
> a w filmie błędu się nie poprawi jednym kliknięciem.
> Scenariusz każdego modułu **pokaż mi do akceptacji przed generowaniem
> dźwięku** — poprawka w tekście kosztuje sekundę, przegenerowanie zużywa limit.
>
> **STRAŻNIK PRAWA — obowiązuje też w filmie.** Narracja nie może wypowiedzieć
> żadnej sygnatury, daty ani statusu spoza Załącznika Z1 zaudytowanego
> scenariusza. W szczególności: rozporządzenie Dz.U. 2026 poz. 428 weszło
> w życie **14 kwietnia 2026**, a przepisy dotyczące przedszkola — § 7 ust. 6
> i 7 oraz § 8 — **1 września 2026**. Akty uchylone (Dz.U. 2017 poz. 356
> i poz. 1743) mogą paść wyłącznie w module M1 jako stan poprzedni, zawsze
> z datą utraty mocy. Zanim wygenerujesz dźwięk, zestaw wszystkie powołania
> z narracji z tabelą Z1 i pokaż mi tę listę.
>
> **RENDER.** Renderuj moduł po module, osobne kompozycje, nie jeden plik
> na 50 minut. W kontenerze bez przeglądarki dodaj `--browser-executable`
> wskazujący `headless_shell`. Po każdym module pokaż mi klatkę kontrolną,
> zanim pójdziesz dalej.
>
> **ODDAJ:** sześć plików MP4, sześć plików MP3 z narracją, sześć plików SRT
> z napisami, teksty narracji w `.txt` do poprawek, agendę 120 minut w Wordzie
> w stylu istniejącego scenariusza oraz projekt Remotion w repozytorium,
> żebym mogła poprawić dowolną scenę i przerenderować sama. Podaj czas trwania
> każdego modułu i zużycie znaków ElevenLabs. Wszystko commituj na gałąź
> `claude/film-szkoleniowy-przedszkole`.

---

## Zanim to uruchomisz — trzy rzeczy

**1. Głos.** Skill nie ma zapamiętanego głosu (`skonfiguruj_glos.py --pokaz`
→ pusto). Bez tego nie powstanie ani dźwięk, ani film — skill odmawia
i kończy się kodem 4. Potrzeba około 3 minut czystego nagrania po polsku
w 3–5 plikach. Klonowanie uruchamiaj **na własnym komputerze** albo przez
złącze MCP ElevenLabs: skrypty skilla łączą się z kontenera, a polityka
sieciowa sesji zdalnej to blokuje (403).

**2. Dlaczego film ma 50 minut, a nie 120.** Dwie godziny narracji to około
18 000 słów i ponad 110 000 znaków ElevenLabs, a render to 216 000 klatek.
Rada i tak nie ogląda dwóch godzin filmu bez przerwy. Film 50 minut plus
ćwiczenia na sali daje pełne dwie godziny szkolenia i mieści się w limitach.

**3. Czego szablon skilla jeszcze nie ma.** Remotion w skillu zna cztery typy
scen: `tytul`, `liczba`, `wykres`, `wniosek`. Animacji wypełniania druku,
kart przepisów ani porównania „było / jest" trzeba dopisać — prompt to zamawia
wprost, bo bez tego dostaniesz film z samymi słupkami.
