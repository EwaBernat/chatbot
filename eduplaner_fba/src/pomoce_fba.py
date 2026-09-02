# -*- coding: utf-8 -*-
"""Karty pomocy dydaktycznej do konspektów FBA — wzór druku KC-4 z banku KPOF.

Karta pomocy siedzi w sekcji VII konspektu, pod przyciskiem „Pokaż pomoc
i posłuchaj polecenia" — tam jej szuka nauczyciel i tam ma być. Zawiera zdjęcie
poglądowe gotowej pomocy, listę „co przygotować", trzy kroki użycia, wskazówkę
i **polecenie dla dziecka nagrane jej własnym głosem**.

Jedna karta na wskaźnik (25), bo pomoc dydaktyczna to ten sam przedmiot we
wszystkich trzech wersjach wiekowych — karta przerwy, termometr emocji, licznik
zadań. **Polecenie jest osobne dla każdego wieku** (75 nagrań): trzylatek słyszy
„Weź jeden klocek", a sześciolatek „Powiedz, od czego zaczynasz". To samo
narzędzie, inne zadanie.

Nagrania: wyłącznie jej sklonowany głos `jq4ZUryuBeDqmtkKtBZ4`, model
`eleven_v3`, rejestr z pamięci projektu — `[warmly, smiling, telling a story to
a small child]` na otwarcie. Tekst mówiony jest czystą prozą: pełne zdania, bez
wielokropków i bez sylabizowania. Ciepło daje wskazówka aktorska, nie interpunkcja.

Pliki mediów: `assets/pomoce_fba/k_<kod>.jpg` (zdjęcie) i
`assets/audio_fba/<wersja><kod>.mp3` (polecenie), gdzie kod to numer wskaźnika
małymi literami z podkreśleniem: `i_1`, `iii_4`, `v_5`.

Karta bez zdjęcia albo bez nagrania **nie psuje budowania** — dostaje pole
zastępcze, a przycisk odtwarzania znika. Dlatego kompletność sprawdza
`sprawdz_pomoce.py`, a nie oglądanie dokumentu.
"""


def kod(wskaznik):
    """`I.1` → `i_1` — nazwa plików mediów tej karty."""
    return wskaznik.lower().replace(".", "_")


# wskaźnik → (nazwa pomocy, co przygotować, trzy kroki, wskazówka, opis zdjęcia)
POMOCE = {
 "I.1": ("Pudełka pierwszego kroku",
   ["trzy przezroczyste pudełka albo tacki, ustawione w rzędzie",
    "zadanie rozłożone na trzy części, po jednej w każdym pudełku",
    "karta „pierwszy krok” z polem na symbol jednej czynności",
    "karta „najpierw — potem” z dwoma polami",
    "minutnik piaskowy na jedną minutę"],
   ["Rozłóż zadanie na trzy pudełka i odsuń dwa poza zasięg wzroku dziecka.",
    "Pokaż kartę „najpierw — potem” i pozwól dziecku wskazać, co będzie potem.",
    "Podaj kartę pierwszego kroku i odwróć minutnik — od tego momentu milcz."],
   "Milczenie po podaniu karty jest częścią pomocy. Każde kolejne ponaglenie "
   "przesuwa uwagę dziecka z zadania na ciebie.",
   "three shallow transparent boxes in a row, each holding one part of a simple "
   "sorting task, a small picture card and a one-minute sand timer beside them"),

 "I.2": ("Licznik trzech poleceń",
   ["podstawka z trzema krążkami do zdejmowania",
    "trzy karty poleceń z polem na symbol czynności",
    "koszyk „zrobione” na wykonane zadania",
    "karta „przerwa” w zasięgu ręki dziecka"],
   ["Ustaw licznik przy dziecku i policzcie razem krążki: „trzy rzeczy i koniec”.",
    "Po każdym wykonanym poleceniu dziecko samo zdejmuje jeden krążek.",
    "Gdy zniknie ostatni krążek, kończysz zajęcia — nawet jeśli zostało dużo czasu."],
   "Nie dokładaj czwartego polecenia po zdjęciu ostatniego krążka. Licznik działa "
   "tylko dopóki jest prawdziwy.",
   "a small wooden stand with three round tokens on pegs, three blank picture "
   "cards and an empty basket on a table"),

 "I.3": ("Karta „wracam” i minutnik przerwy",
   ["karta „wracam” — kładziona na przerwanym zadaniu",
    "minutnik wizualny albo piaskowy na trzy minuty",
    "podkładka z zaznaczonym miejscem zadania",
    "koszyk „do dokończenia” z jedną częścią zadania"],
   ["Przed przerwą połóż razem z dzieckiem kartę „wracam” na jego zadaniu.",
    "Nastaw minutnik i zostaw zadanie dokładnie tak, jak leżało.",
    "Po sygnale czekaj przy stoliku — nie idź po dziecko do kącika."],
   "Nie sprzątaj zadania w czasie przerwy. Zniknięcie zadania uczy dziecka, "
   "że przerwa jest sposobem na jego skasowanie.",
   "a small card lying on an unfinished puzzle, a visual countdown timer and "
   "a basket with one puzzle piece, on a light wooden table"),

 "I.4": ("Trzy koperty serii",
   ["trzy koperty oznaczone numerami jeden, dwa i trzy",
    "dwa zadania pewne, które dziecko wykonuje bez pomocy",
    "jedno zadanie o stopień trudniejsze — trudniejsze, nie dłuższe",
    "karta „poradzę sobie” z polem na znak dziecka"],
   ["Pokaż trzy koperty i powiedz wprost, że trzecia jest trudniejsza.",
    "Nie pomagaj przy dwóch pierwszych, nawet gdy dziecko zwalnia.",
    "Po otwarciu trzeciej koperty połóż obok kartę „poradzę sobie”."],
   "Trudne zadanie ma być trudniejsze, a nie dłuższe. Wydłużone łatwe dziecko "
   "rozpozna od razu i seria straci sens.",
   "three numbered paper envelopes in a row, a simple threading task and "
   "a harder pattern task laid out beside them, plus a small blank card"),

 "I.5": ("Karta przerwy",
   ["jedna karta „przerwa” — zawsze ta sama, w stałym rogu stolika",
    "wykaz trzech rzeczy dozwolonych w czasie przerwy",
    "minutnik przerwy na trzy minuty",
    "karta „wracam” do położenia na zadaniu"],
   ["Połóż kartę w tym samym miejscu i pokaż dziecku, gdzie leży.",
    "Na początku daj przerwę natychmiast po każdej prośbie, nawet dziesiątej.",
    "Dopiero gdy prośba działa pewnie, wydłużaj pracę przed przerwą."],
   "Prośba musi być szybsza i pewniejsza od krzyku. Jedna odmowa przerwy po "
   "prośbie cofa naukę o tydzień.",
   "a single laminated card with a pause symbol lying in the corner of a table, "
   "a small sand timer and a strip with three small pictures beside it"),

 "II.1": ("Pudełko regulacyjne",
   ["płaskie pudełko przy stoliku dziecka, zawsze w tym samym miejscu",
    "gniotek, kolczasta piłeczka i kawałek materiału o wyraźnej fakturze",
    "taśma elastyczna zawiązana na nogach krzesła",
    "podkładka z polem „tu odkładam”"],
   ["Pokaż zawartość pudełka i powiedz, że można brać bez pytania.",
    "Nie komentuj sięgnięcia w trakcie pracy — komentarz przerywa zadanie.",
    "Po skończonym zadaniu wskaż pole „tu odkładam”."],
   "Nie zabieraj przedmiotu regulacyjnego za karę. Odebrany gniotek nie kończy "
   "potrzeby — wraca autostymulacja, którą właśnie zamieniliśmy.",
   "a shallow open box on a table holding a squeeze ball, a spiky sensory ball "
   "and a piece of textured fabric, with a wide elastic band beside it"),

 "II.2": ("Karta diety sensorycznej",
   ["karta z trzema polami wrażeń: ruch, ucisk, cisza",
    "po dwie propozycje form w każdym polu, dostępne w sali",
    "buźki „pomogło” i „nie pomogło” do zaznaczania",
    "pisak sucho ścieralny"],
   ["Omów trzy pola i pokaż przy każdym prawdziwą formę z sali.",
    "W momencie przeciążenia podsuń kartę i milcz — nie podpowiadaj wyboru.",
    "Po skorzystaniu z formy zaznaczcie razem, czy pomogła."],
   "Nie wpisuj na kartę formy, której nie ma w sali. Karta z formą niedostępną "
   "uczy dziecko, że wskazywanie nic nie daje.",
   "a laminated chart divided into three labelled sections with small pictogram "
   "cards, two smiley face stickers and a dry-erase marker on a table"),

 "II.3": ("Plan przerw sensorycznych",
   ["pasek planu dnia z zaznaczonymi porami przerw",
    "minutnik z sygnałem dźwiękowym, ten sam każdego dnia",
    "stałe miejsce przerwy, zawsze przygotowane",
    "karta odhaczania z czterema polami"],
   ["Rano pokaż na pasku, ile przerw jest dziś zaplanowanych.",
    "Nastaw minutnik i po sygnale nic nie mów — sygnał ma wystarczyć.",
    "Po przerwie dziecko samo odhacza pole na swojej karcie."],
   "Przerwa ma wyprzedzać zachowanie. Dana po wybuchu wygląda tak samo, "
   "a uczy czegoś przeciwnego.",
   "a paper day-plan strip with small picture cards, a kitchen timer and "
   "a checklist card with four empty boxes on a light table"),

 "II.4": ("Tacka „skończyłem”",
   ["tacka z trzema gotowymi zajęciami dla dziecka, które skończyło wcześniej",
    "lista trzech aktywności z symbolami, powieszona przy stoliku",
    "minutnik na pięć minut",
    "koszyk na materiały do odłożenia"],
   ["Przygotuj tackę przed zajęciami, nie w momencie, gdy dziecko skończy.",
    "Nie proponuj zajęcia — wskaż wzrokiem listę i pozwól wybrać.",
    "Po pięciu minutach poproś o odłożenie materiałów do koszyka."],
   "Puste minuty po zadaniu to najbardziej ryzykowny moment dnia. Zajęcie "
   "wymyślane na miejscu przychodzi zawsze o minutę za późno.",
   "a wooden tray holding three small ready activities: a lacing card, a shape "
   "puzzle and a stack of picture cards, with a timer beside it"),

 "II.5": ("Karta „stop — zamiana”",
   ["karta z dwoma polami: znak stop i forma zastępcza",
    "forma zastępcza dająca to samo wrażenie, uzgodniona z terapeutą SI",
    "ustalony z dzieckiem sygnał dotykowy",
    "stoper do mierzenia czasu od sygnału"],
   ["Ustal sygnał w spokojnym momencie dnia i przećwicz go w zabawie.",
    "W trakcie autostymulacji pokaż kartę z odległości, bez mówienia.",
    "Podaj formę zastępczą do ręki i zmierz czas od sygnału."],
   "Nie przytrzymuj dziecka i nie zabieraj przedmiotu siłą. Przerwanie siłą "
   "kończy zachowanie na minutę i psuje relację na tydzień.",
   "a two-part laminated card showing a stop sign and a sensory toy, with "
   "a textured chewy tube and a stopwatch on a table"),

 "III.1": ("Karta „potrzebuję pomocy” i klepsydra",
   ["karta „potrzebuję pomocy” w stałym rogu stolika",
    "klepsydra albo licznik pokazujący, ile trwa czekanie",
    "zadanie „w międzyczasie”, które można robić, czekając",
    "karta zapisu z polami na udane czekania"],
   ["Umów się z dzieckiem, po jakim czasie podchodzisz, i pokaż ten czas na klepsydrze.",
    "Gdy dziecko woła, wskaż kartę zamiast odpowiadać słowami.",
    "Podejdź dokładnie po umówionym czasie, także wtedy, gdy dziecko czeka spokojnie."],
   "Jedno spóźnienie o dwie minuty uczy dziecko, że karta nie działa, a wołanie "
   "działa — i wraca wołanie, tylko głośniejsze.",
   "a small laminated help card lying on a table corner, a sand timer and "
   "a simple threading activity in a tray beside them"),

 "III.2": ("Tabliczka żetonowa za podniesioną rękę",
   ["karta z symbolem podniesionej ręki przy stoliku dziecka",
    "tabliczka na pięć żetonów i żetony w pojemniczku",
    "ustalony sygnał zwrotny dorosłego: skinienie głową",
    "lista nagród możliwych po zebraniu żetonów"],
   ["Ustal z grupą kolejność: ręka w górę, skinienie, potem podejście.",
    "Odpowiadaj skinieniem natychmiast, nawet gdy podejdziesz dopiero za chwilę.",
    "Żeton daj za skorzystanie z ręki, nie za brak zachowania trudnego."],
   "Minimalna reakcja na zachowanie trudne działa tylko wtedy, gdy ręka naprawdę "
   "działa. Niezauważona ręka wraca jako krzyk.",
   "a small token board with five round tokens, a card showing a raised hand "
   "pictogram and a little pot of tokens on a table"),

 "III.3": ("Maskotka mówiącego i karta kolejności",
   ["maskotka albo gładki kamień przekazywany w kręgu",
    "karta kolejności z symbolami dzieci",
    "pasek „mówię — słucham” ze znacznikiem",
    "krótki temat rundy, ten sam dla wszystkich"],
   ["Ułóż karty kolejności i pokaż dziecku, które miejsce ma w rundzie.",
    "Głos ma tylko ten, kto trzyma maskotkę — także ty.",
    "Nazwij oba osiągnięcia: własną wypowiedź i wysłuchanie poprzednika."],
   "Runda ma gwarantować głos każdemu. Dziecko pominięte raz wraca do zachowania, "
   "które nigdy nie zawiodło.",
   "a soft toy and a smooth painted stone on a rug, with a row of small "
   "photo-style picture cards showing children in order"),

 "III.4": ("Plan dnia z porą rozmowy",
   ["plan dnia z zaznaczoną porą rozmowy z dzieckiem",
    "minutnik dwuminutowy na czas rozmowy",
    "karta „następna rozmowa” z symbolem pory dnia",
    "dwa krzesła odsunięte od grupy"],
   ["Rano pokaż na planie, kiedy będzie rozmowa, i zostaw kartę u dziecka.",
    "W czasie rozmowy nie rób nic innego — bez zadań w tle i bez telefonu.",
    "Kończ rozmowę sygnałem minutnika, a nie zdaniem „to na razie tyle”."],
   "Rozmowa ma się odbyć także w dniu, w którym dziecko zachowuje się dobrze — "
   "zwłaszcza wtedy. Rozmowa tylko po trudnym dniu uczy, że trudny dzień jest do niej drogą.",
   "a day-plan strip with picture cards, one card marked with a small clock, "
   "a two-minute sand timer and two small chairs in the background"),

 "III.5": ("Karta umówionego znaku",
   ["karta z rysunkiem gestu ustalonego wspólnie z dzieckiem",
    "tabliczka „zobacz, co zrobiłem” do postawienia na stoliku",
    "miejsce na prace dzieci, oglądane o stałej porze",
    "żetony za skorzystanie z gestu"],
   ["Ustal gest razem z dzieckiem i narysujcie go wspólnie na karcie.",
    "Odpowiadaj na każdy gest, także niepełny — najpierw pewność, potem dokładność.",
    "Pokaż, kiedy oglądacie prace, żeby czekanie miało koniec."],
   "Sprawdzanie reakcji dorosłego to prośba o kontakt, nie prowokacja. Nazwij "
   "ją wprost i daj krótszą drogę.",
   "a hand-drawn card showing a raised palm gesture, a small standing sign and "
   "a few children's drawings pinned on a board"),

 "IV.1": ("Karty „nie teraz” i dwie alternatywy",
   ["karta „nie teraz” z polem na porę, kiedy będzie można",
    "dwie karty alternatyw zawsze dostępnych bez pytania",
    "buźki do nazwania emocji po odmowie",
    "kącik z aktywnościami dostępnymi od ręki"],
   ["Rano pokaż, co jest dostępne zawsze, i gdzie tego szukać.",
    "Odmawiaj jednym zdaniem i pokazuj obie alternatywy w tej samej chwili.",
    "Nie wracaj do tematu odmowy i nie tłumacz jej drugi raz."],
   "Tłumaczenie powtórzone trzeci raz dziecko czyta jako wahanie i wraca do "
   "naciskania — bo czasem to działa.",
   "three laminated cards laid side by side: one with a crossed-out symbol and "
   "two showing simple play activities, with two smiley cards below"),

 "IV.2": ("Minutnik zakończenia zabawy",
   ["minutnik wizualny stawiany przy dziecku",
    "karta „jeszcze dwie minuty” z symbolem czasu",
    "półka albo pudełko z zaznaczonym konturem przedmiotu",
    "karta „wróci jutro” z symbolem następnego dnia"],
   ["Pokaż półkę z konturem i dopasujcie razem przedmiot do jego miejsca.",
    "Zapowiedz koniec dwie minuty wcześniej, nie w chwili zabierania.",
    "Po sygnale nic nie mów i nie podchodź — sygnał ma wystarczyć."],
   "Nie zabieraj przedmiotu z ręki. Zabranie zamienia zakończenie w stratę "
   "i uczy dziecko pilnować przedmiotu przed dorosłym.",
   "a visual countdown timer beside a wooden toy, and a shelf with a painted "
   "outline showing where the toy belongs"),

 "IV.3": ("Karty prośby o przedmiot",
   ["karty z obrazkami rzeczy, o które dziecko dopomina się najczęściej",
    "karta zwrotu „poproszę o…” z pustym polem na symbol",
    "koszyk wymiany: przedmiot za kartę",
    "żetony za prośbę zamiast zabrania"],
   ["Wybierz do kart rzeczy, o które dziecko naprawdę prosi, nie te z zestawu.",
    "Na początku wydawaj przedmiot po każdej prośbie, także dziesiątej.",
    "Dopiero gdy prośba działa pewnie, ucz czekania i przyjmowania odmowy."],
   "Prośba musi być pewniejsza niż wyrwanie. Odmowa wydana po pierwszej udanej "
   "prośbie cofa naukę do punktu wyjścia.",
   "four picture cards showing a ball, a toy car, a book and crayons, laid next "
   "to a sentence-strip card with an empty slot, and a small basket"),

 "IV.4": ("Licznik czekania",
   ["wizualny licznik czasu albo klepsydra",
    "karta „dostanę o…” z polem na porę dnia",
    "pudełko z krótkim zadaniem na czas czekania",
    "karta zapisu udanych czekań"],
   ["Umów porę i zapisz ją razem z dzieckiem na karcie — to umowa, nie obietnica.",
    "Podaj zadanie na czas czekania od razu, zanim pojawi się złość.",
    "Wydaj przedmiot dokładnie o umówionej porze, co do minuty."],
   "Jedno przesunięcie terminu kosztuje więcej niż dziesięć udanych czekań.",
   "a visual countdown timer, a small card with a clock face and a tray holding "
   "a short posting activity on a light table"),

 "IV.5": ("Pudełko „w międzyczasie”",
   ["pudełko z trzema krótkimi, pewnymi zadaniami",
    "karta z symbolem atrakcji, na którą dziecko czeka",
    "pasek czasu pokazujący, ile zostało do startu",
    "tabliczka żetonowa"],
   ["Przygotuj pudełko przed oczekiwaniem, nie w jego trakcie.",
    "Pokaż na pasku, ile czasu zostało, i pozwól wybrać zadanie z pudełka.",
    "Żeton wydaj zaraz po zakończeniu oczekiwania, przed samą atrakcją."],
   "Oczekiwanie na atrakcję jest trudniejsze niż nuda — bodziec jest już w zasięgu "
   "wzroku. Zadanie musi być krótkie i pewne, inaczej samo stanie się frustracją.",
   "an open box holding three small quick activities, a picture card of a "
   "playground and a paper time-strip with a marker on a table"),

 "V.1": ("Plan dnia z kartą zmiany",
   ["plan dnia z kartami do przekładania, na wysokości wzroku dziecka",
    "karta „zmiana” — jedna, zawsze ta sama",
    "minutnik do odliczania ostatnich minut aktywności",
    "buźki do nazwania reakcji na zmianę"],
   ["Podejdź z dzieckiem do planu i pokaż kartę, która się zmienia.",
    "Wyjmij starą kartę razem z dzieckiem i wstawcie kartę zmiany.",
    "Odliczaj do przejścia: pięć minut, dwie minuty, teraz."],
   "Uprzedzaj także o zmianach na lepsze. Dziecko o tej funkcji reaguje na samą "
   "zmianę, nie na jej treść.",
   "a wall day-plan with removable picture cards, one card being lifted out, "
   "a card with an arrow symbol and a sand timer below"),

 "V.2": ("Termometr emocji",
   ["termometr z trzema polami: zielonym, żółtym i czerwonym",
    "karty strategii przypisane do pola żółtego",
    "małe lusterko do rozpoznawania własnej miny",
    "karta zapisu wskazań z całego dnia"],
   ["Omów trzy kolory i pokaż przy żółtym, co dokładnie można zrobić.",
    "Sprawdzajcie termometr także w spokojnych momentach dnia.",
    "Po wskazaniu koloru przypomnij strategie, nie wybieraj za dziecko."],
   "Narzędzie używane wyłącznie w napięciu dziecko odbiera jako zapowiedź kłopotów "
   "i przestaje po nie sięgać dokładnie wtedy, gdy jest potrzebne.",
   "a vertical three-part card coloured green, yellow and red with a movable "
   "arrow, two small strategy cards and a round hand mirror on a table"),

 "V.3": ("Kącik wyciszenia",
   ["wydzielone miejsce w sali: koc, poduszka, słuchawki wygłuszające",
    "karta wejścia kładziona przy wejściu do kącika",
    "minutnik pięciominutowy w kąciku",
    "karta trzech form wyciszenia do wyboru"],
   ["Pokaż kącik w spokojnym momencie i posiedź tam z dzieckiem.",
    "Nie wchodź do kącika, gdy dziecko z niego korzysta, i nie zagaduj.",
    "Zapisz w rejestrze, kto zainicjował wyjście: dziecko czy dorosły."],
   "Kącik nie może być miejscem, do którego się kogoś odsyła. Jeśli raz posłuży "
   "za karę, dziecko przestanie z niego korzystać samo.",
   "a cosy corner with a floor cushion, a weighted blanket and ear defenders, "
   "a small timer on a low shelf and a card holder by the entrance"),

 "V.4": ("Karta powrotu do grupy",
   ["karta „moje miejsce” z symbolem konkretnego miejsca w sali",
    "skrócona wersja zadania przygotowana przed wyjściem dziecka",
    "minutnik odmierzający czas na powrót",
    "karta naprawy z trzema krokami do wyboru"],
   ["Przed wyjściem dziecka zostaw na jego miejscu skróconą wersję zadania.",
    "Po sygnale czekaj przy grupie — nie idź po dziecko do kącika.",
    "Wróć do rozmowy o zdarzeniu dopiero po zajęciach."],
   "Rozmowa w napięciu kończy się drugim wybuchem. Pierwsze minuty po powrocie "
   "są na wrócenie, nie na omawianie.",
   "a card showing a child's place at a table, a short worksheet with only two "
   "tasks left, a sand timer and a small card with three simple pictures"),

 "V.5": ("Czerwona karta i sygnały ciała",
   ["czerwona karta w stałym miejscu przy dziecku, na rzepie",
    "karta trzech sygnałów ciała, uzupełniana razem z dzieckiem",
    "plan reakcji: co robimy natychmiast po czerwonej karcie",
    "rejestr ABC z kolumną „sygnał dziecka”"],
   ["Nazwijcie razem sygnały ciała dziecka i zapiszcie je na karcie.",
    "Przypnij czerwoną kartę tam, gdzie dziecko sięgnie po nią bez wstawania.",
    "Po pokazaniu karty przerwij to, co robisz, i podejdź natychmiast."],
   "Sygnał, na który dorosły odpowiada „za chwilę”, przestaje być używany po dwóch "
   "takich chwilach — a wtedy zostaje tylko wybuch.",
   "a plain red laminated card attached with a velcro strip to the edge of a "
   "table, next to a small card with three simple body-signal drawings"),
}

# (wskaźnik, wersja) → polecenie dla dziecka, czytane jej głosem
POLECENIA = {
 ("I.1", "A"): "Popatrz, tu jest twoje pudełko. Weź z niego jedną rzecz i połóż ją przed sobą.",
 ("I.1", "B"): "Popatrz na kartę i pokaż mi, od czego zaczynasz. Potem zrób ten pierwszy krok.",
 ("I.1", "C"): "Wybierz, od którego kroku zaczynasz, i powiedz mi o tym. Potem możesz zaczynać.",
 ("I.2", "A"): "Popatrz na obrazek. Zrób to, co widzisz, a potem zdejmij jeden krążek.",
 ("I.2", "B"): "Mamy trzy rzeczy do zrobienia i koniec. Zrób pierwszą i zdejmij krążek.",
 ("I.2", "C"): "Posłuchaj trzech poleceń, a potem zrób je po kolei i odhacz każde na kartce.",
 ("I.3", "A"): "Idziesz na przerwę. Połóż tę kartę na swoim zadaniu, żeby na ciebie poczekało.",
 ("I.3", "B"): "Po przerwie wracasz do stolika i kończysz tę część, którą razem zaznaczyliśmy.",
 ("I.3", "C"): "Powiedz, ile minut przerwy potrzebujesz, i ustaw sobie minutnik.",
 ("I.4", "A"): "Zrób dwa łatwe zadania, a potem spróbuj trzeciego. Będę siedzieć obok ciebie.",
 ("I.4", "B"): "Otwórz pierwszą kopertę. Trzecia jest trudniejsza, więc poproś mnie o pomoc, jeśli będzie ci potrzebna.",
 ("I.4", "C"): "Ułóż zadania w takiej kolejności, jaką wybierzesz, i powiedz mi, dlaczego tak.",
 ("I.5", "A"): "Tu leży karta przerwy. Kiedy zrobi się trudno, podaj mi ją, a zrobimy przerwę.",
 ("I.5", "B"): "Karta przerwy leży w rogu stolika. Pokaż mi ją, zanim będzie za trudno.",
 ("I.5", "C"): "Kiedy potrzebujesz przerwy, powiedz mi o tym i umówimy się, ile będzie trwała.",
 ("II.1", "A"): "Kiedy ręce chcą się ruszać, weź gniotek z pudełka i mocno go ściśnij.",
 ("II.1", "B"): "Pudełko stoi przy tobie. Możesz z niego brać, kiedy potrzebujesz, i pracować dalej.",
 ("II.1", "C"): "Wybierz z pudełka to, czego teraz potrzebujesz, i powiedz mi, dlaczego akurat tego.",
 ("II.2", "A"): "Pokaż mi na obrazkach, czy chcesz się kołysać, czy ściskać.",
 ("II.2", "B"): "Wskaż na karcie, czego teraz potrzebujesz, i wybierz jedną rzecz z tego pola.",
 ("II.2", "C"): "Powiedz, czego potrzebujesz, i wybierz taki sposób, który nie przeszkodzi innym dzieciom.",
 ("II.3", "A"): "Kiedy usłyszysz dzwonek, idziemy razem do kącika na przerwę.",
 ("II.3", "B"): "Kiedy zadzwoni minutnik, idziesz sam na przerwę i wracasz, kiedy się skończy.",
 ("II.3", "C"): "Zaznacz na swoim planie, kiedy dziś zrobisz przerwy, i skorzystaj z nich w tym czasie.",
 ("II.4", "A"): "Skończyłeś zadanie. Wybierz jedną z tych dwóch zabawek i pobaw się przy stoliku.",
 ("II.4", "B"): "Kiedy skończysz wcześniej, wybierz coś z listy i zajmij się tym przez pięć minut.",
 ("II.4", "C"): "Wymyśl, czym się zajmiesz, kiedy skończysz wcześniej, i doprowadź to do końca.",
 ("II.5", "A"): "Kiedy poczujesz moją rękę, przestań i weź ode mnie tę zabawkę.",
 ("II.5", "B"): "Kiedy zobaczysz kartę, skończ i weź to, co leży obok ciebie.",
 ("II.5", "C"): "Kiedy zauważysz, że znowu to robisz, weź swoją zamianę albo poproś mnie o pomoc.",

 ("III.1", "A"): "Kiedy jestem zajęta, trzymaj tę kartę i poczekaj. Przyjdę do ciebie, kiedy piasek się przesypie.",
 ("III.1", "B"): "Kiedy potrzebujesz pomocy, połóż tę kartę na stoliku i poczekaj przy swoim zadaniu.",
 ("III.1", "C"): "Kiedy rozmawiam z innym dzieckiem, zrób w tym czasie kolejny krok swojego zadania.",
 ("III.2", "A"): "Kiedy chcesz mnie zawołać, dotknij mojego ramienia, a od razu się odwrócę.",
 ("III.2", "B"): "Kiedy potrzebujesz mnie, podnieś rękę i poczekaj, aż kiwnę do ciebie głową.",
 ("III.2", "C"): "Powiedz mi, w czym potrzebujesz pomocy, a przyjdę do ciebie, kiedy skończę z kolegą.",
 ("III.3", "A"): "Kiedy dostaniesz misia, powiedz jedno słowo, a potem podaj misia dalej.",
 ("III.3", "B"): "Poczekaj na swoją kolej, a kiedy przyjdzie, powiedz nam swoje zdanie.",
 ("III.3", "C"): "Posłuchaj, co powie dziecko przed tobą, a potem powiedz, co o tym myślisz.",
 ("III.4", "A"): "Teraz mamy chwilę tylko dla nas, a potem idziemy razem do zabawy.",
 ("III.4", "B"): "Mamy dwie minuty na rozmowę. Kiedy zadzwoni minutnik, wracasz do swojego zadania.",
 ("III.4", "C"): "Wybierz porę, o której dziś porozmawiamy, i zaznacz ją na swoim planie.",
 ("III.5", "A"): "Kiedy chcesz, żebym na ciebie spojrzała, podnieś tę kartę do góry.",
 ("III.5", "B"): "Kiedy chcesz mi coś pokazać, unieś dłoń i poczekaj, aż kiwnę do ciebie głową.",
 ("III.5", "C"): "Powiedz mi wprost, kiedy chcesz, żebym zobaczyła twoją pracę.",
 ("IV.1", "A"): "Teraz nie możesz tego wziąć. Wybierz jedną z tych dwóch zabawek.",
 ("IV.1", "B"): "Tego dziś nie możemy wziąć. Popatrz na te dwie karty i wybierz, czym się zajmiesz.",
 ("IV.1", "C"): "Kiedy usłyszysz „nie teraz”, zapytaj mnie, kiedy będziesz mógł to dostać.",
 ("IV.2", "A"): "Kiedy zadzwoni minutnik, oddasz mi zabawkę do ręki.",
 ("IV.2", "B"): "Masz jeszcze dwie minuty. Po sygnale odłóż zabawkę na jej miejsce na półce.",
 ("IV.2", "C"): "Ustaw minutnik na tyle minut, ile chcesz się bawić, i skończ, kiedy zadzwoni.",
 ("IV.3", "A"): "Kiedy czegoś chcesz, podaj mi kartę z obrazkiem, a ci to dam.",
 ("IV.3", "B"): "Kiedy czegoś potrzebujesz, powiedz „poproszę o” i poczekaj chwilę na odpowiedź.",
 ("IV.3", "C"): "Poproś kolegę o tę rzecz i umówcie się, kiedy mu ją oddasz.",
 ("IV.4", "A"): "Trzymaj tę kartę i poczekaj. Kiedy piasek się przesypie, dostaniesz to, o co prosisz.",
 ("IV.4", "B"): "Dostaniesz to, kiedy licznik dojdzie do końca. W tym czasie zrób zadanie z pudełka.",
 ("IV.4", "C"): "Umówmy się, o której porze to dostaniesz, i zaznaczmy tę porę na planie.",
 ("IV.5", "A"): "Poczekamy razem na naszą zabawę. Weź tę zabawkę i pobaw się przez ten czas.",
 ("IV.5", "B"): "Zanim się zacznie, wybierz jedno zadanie z pudełka i zrób je do sygnału.",
 ("IV.5", "C"): "Zaplanuj, czym zajmiesz się w czasie czekania, i doprowadź to do końca.",
 ("V.1", "A"): "Popatrz na ten obrazek. Za chwilę idziemy robić coś nowego, razem.",
 ("V.1", "B"): "Popatrz na plan. Ta karta się zmienia, więc teraz będziemy robić coś innego.",
 ("V.1", "C"): "Plan się zmienił. Powiedz mi, na kiedy przełożymy to, co miało być teraz.",
 ("V.2", "A"): "Pokaż mi, którą buźkę teraz czujesz.",
 ("V.2", "B"): "Pokaż na termometrze, jaki masz teraz kolor, a potem wybierz, co ci pomoże.",
 ("V.2", "C"): "Powiedz, co czujesz i dlaczego, a potem wybierz swoją strategię.",
 ("V.3", "A"): "Chodźmy razem do kącika. Posiedzimy tam chwilę, aż zrobi się ciszej.",
 ("V.3", "B"): "Kiedy jest za głośno, idź do kącika i zostań tam, dopóki minutnik nie zadzwoni.",
 ("V.3", "C"): "Kiedy zrobi się za dużo, weź trzy oddechy przy stoliku albo idź do kącika.",
 ("V.4", "A"): "Wracamy do dzieci. Popatrz, tu jest twoje miejsce.",
 ("V.4", "B"): "Wracaj na swoje miejsce i dokończ to, co zostało z twojego zadania.",
 ("V.4", "C"): "Wróć do nas, a potem wybierz, jak naprawisz to, co się wydarzyło.",
 ("V.5", "A"): "Kiedy zaczynasz się złościć, weź tę czerwoną kartę i pokaż mi ją.",
 ("V.5", "B"): "Pokaż mi czerwoną kartę wtedy, kiedy poczujesz, że robi się trudno.",
 ("V.5", "C"): "Kiedy zauważysz swój sygnał, powiedz mi o nim i skorzystaj ze swojej strategii.",
}
