# -*- coding: utf-8 -*-
"""Konspekty do funkcji III — uwaga (wskaźniki III.1–III.5).

Wspólny mianownik: **uwaga dana z wyprzedzeniem jest tańsza niż odzyskiwana po
wybuchu.** Dziecko o tej funkcji nie „robi na złość” — prosi o kontakt jedyną
drogą, która działa szybko. Konspekt daje drogę szybszą i pewniejszą (ręka,
karta, gest), a na zachowanie trudne zostawia reakcję minimalną. Obie zmiany
muszą wejść naraz: sama minimalna reakcja bez nowej drogi to odcięcie dziecka.
"""

RDZEN = {
 "III.1": dict(
  tytul="Kartka, kiedy nauczyciel jest zajęty",
  icf="d240·d710", pp="2.11·1.6",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["nauka czekania z widocznym końcem, nie „chwileczkę”",
          "karta prośby o pomoc zamiast wołania i podchodzenia",
          "odpowiedź dorosłego zawsze po tym samym czasie",
          "stopniowe wydłużanie czasu czekania",
          "wzmocnienie za czekanie, nie tylko za wykonane zadanie"],
  pomoce=["karta „potrzebuję pomocy” w stałym miejscu stolika",
          "klepsydra albo licznik pokazujący czas czekania",
          "zadanie „w międzyczasie”, które można robić, czekając",
          "karta z zapisem, ile razy dziecko doczekało"],
  wskazowka="Podejdź dokładnie wtedy, kiedy obiecałeś. Jedno spóźnienie o dwie minuty uczy "
            "dziecko, że karta nie działa, a wołanie działa — i wraca wołanie, tylko głośniejsze.",
  ter_kryt="Rejestr ABC — kolumna A: dorosły zajęty innym dzieckiem · wszystkie takie sytuacje.",
  R="Nauczyciel bywa zajęty na każdych zajęciach; tego warunku nie da się z sali usunąć.",
  mod=("nauczyciel zostaje w zasięgu wzroku i potwierdza spojrzeniem, że widzi kartę",
       "dziecko kładzie kartę samo i czeka przy stoliku",
       "dziecko czeka do końca rozmowy dorosłego z innym dzieckiem"),
  arkusz=dict(
   tytul="Karty do zajęć „Kartka, kiedy nauczyciel jest zajęty”",
   wstep="Wytnij karty. Karta „potrzebuję pomocy” leży na stoliku dziecka przez całe "
         "zajęcia, w tym samym rogu. Symbole wklej z biblioteki EduPlaner.",
   karty=[("Potrzebuję pomocy", "symbol prośby o pomoc — karta główna"),
          ("Czekam", "symbol czekania: klepsydra albo zegar"),
          ("W międzyczasie", "symbol zadania, które robię, czekając"),
          ("Już idę", "symbol dla dorosłego: potwierdzenie, że widzi kartę")],
   pasek=["kładę kartę", "czekam", "dostaję pomoc"])),

 "III.2": dict(
  tytul="Ręka w górę zamiast hałasu",
  icf="d335·d710", pp="2.11·1.5",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["komunikacja funkcjonalna: podniesiona ręka jako droga do uwagi",
          "reakcja natychmiastowa na rękę, minimalna na zachowanie trudne",
          "uwaga pozytywna za zachowania pożądane, nie tylko za prośbę",
          "podpowiedź wyprzedzająca przy pierwszych sygnałach szukania kontaktu",
          "plan wzmocnień spójny u wszystkich dorosłych w sali"],
  pomoce=["karta z symbolem podniesionej ręki przy stoliku",
          "żetony za skorzystanie z ręki zamiast zachowania trudnego",
          "tablica z zapisem, ile razy dziecko zostało zauważone",
          "sygnał zwrotny dorosłego: skinienie głową"],
  wskazowka="Minimalna reakcja na zachowanie trudne działa tylko wtedy, gdy nowa droga "
            "naprawdę działa. Jeśli ręka bywa niezauważona, dziecko wróci do zachowania — "
            "i będzie miało rację, bo tamto działało zawsze.",
  ter_kryt="Rejestr ABC — którą drogą dziecko uzyskało uwagę · wszystkie sytuacje kontaktu.",
  R="To zachowanie zastępcze o tej samej funkcji: uwaga dorosłego, tylko inną drogą.",
  mod=("nauczyciel przypomina gest, unosząc własną rękę jako model",
       "dziecko podnosi rękę samo i czeka na skinienie",
       "dziecko prosi słowami i czeka na przerwę w zajęciach"),
  arkusz=dict(
   tytul="Karty do zajęć „Ręka w górę zamiast hałasu”",
   wstep="Wytnij karty i tabelkę żetonów. Żeton dziecko dostaje za skorzystanie z ręki, "
         "a nie za brak zachowania trudnego — nagradzamy to, co ma się pojawić, nie to, "
         "czego ma nie być.",
   karty=[("Ręka w górę", "symbol podniesionej ręki"),
          ("Widzę cię", "symbol skinienia — odpowiedź dorosłego"),
          ("Czekam chwilę", "symbol krótkiego czekania po zgłoszeniu"),
          ("Mój żeton", "pole na żeton za skorzystanie z ręki")],
   pasek=["podnoszę rękę", "dostaję skinienie", "rozmawiamy"])),

 "III.3": dict(
  tytul="Moja kolej w rundzie",
  icf="d350·d710", pp="3.1·1.6",
  rodzaj="Zajęcia rozwijające kompetencje społeczne · realizacja planu PBS",
  metody=["runda z przedmiotem mówiącego: głos ma ten, kto trzyma",
          "gwarantowana kolej dla każdego dziecka",
          "krótkie wypowiedzi, żeby czekanie było policzalne",
          "nazywanie słuchania jako czynności, nie jako grzeczności",
          "wzmocnienie za wysłuchanie poprzednika, nie tylko za własną wypowiedź"],
  pomoce=["maskotka albo kamień mówiącego, przekazywany w kręgu",
          "karta kolejności z symbolami dzieci",
          "pasek „mówię — słucham” do trzymania przy sobie",
          "krótki temat rundy, ten sam dla wszystkich"],
  wskazowka="Runda ma gwarantować głos każdemu — dopiero wtedy przestaje opłacać się "
            "zdobywanie go hałasem. Dziecko pominięte raz w rundzie wraca do zachowania, "
            "które nigdy nie zawiodło.",
  ter_kryt="Karta zajęć grupowych — zgłoszenia i wejścia w słowo · wszystkie zajęcia grupowe.",
  R="Praca w grupie wraca codziennie — na dywanie, przy stolikach i na spacerze.",
  mod=("dziecko dostaje maskotkę jako pierwsze i mówi jedno słowo",
       "dziecko czeka na swoją kolej z podpowiedzią wzrokową nauczyciela",
       "dziecko prowadzi rundę i podaje głos kolejnym osobom"),
  arkusz=dict(
   tytul="Karty do zajęć „Moja kolej w rundzie”",
   wstep="Wytnij karty i pasek. Pasek „mówię — słucham” dziecko trzyma przy sobie "
         "w czasie rundy i przesuwa znacznik. Symbole wklej z biblioteki EduPlaner.",
   karty=[("Mówię", "symbol mówienia — trzymam maskotkę"),
          ("Słucham", "symbol słuchania — patrzę na mówiącego"),
          ("Moja kolej", "symbol kolejki z zaznaczonym miejscem dziecka"),
          ("Koniec rundy", "symbol zakończenia — maskotka wraca do nauczyciela")],
   pasek=["słucham", "moja kolej", "słucham dalej"])),

 "III.4": dict(
  tytul="Dwie minuty tylko dla mnie",
  icf="d710·d230", pp="1.2·2.11",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["uwaga „z wyprzedzeniem”: kontakt zanim pojawi się zachowanie",
          "stała pora rozmowy, wpisana w plan dnia",
          "zakończenie rozmowy sygnałem, nie negocjacją",
          "zapowiedź następnej rozmowy przy zakończeniu tej",
          "uwaga pozytywna w trakcie zajęć, krótka i częsta"],
  pomoce=["plan dnia z zaznaczoną porą rozmowy",
          "minutnik dwuminutowy na czas rozmowy",
          "karta „następna rozmowa” z porą dnia",
          "kącik rozmowy: dwa krzesła osobno od grupy"],
  wskazowka="Rozmowa z wyprzedzeniem musi się odbyć także w dniu, w którym dziecko "
            "zachowuje się dobrze — zwłaszcza wtedy. Rozmowa dawana tylko po trudnym dniu "
            "uczy, że trudny dzień jest drogą do rozmowy.",
  ter_kryt="Plan zajęć — odhaczenie rozmowy i powrotu do zadania · wszystkie zajęcia.",
  R="Uwaga dana z góry kosztuje dwie minuty; odzyskiwanie kontaktu po wybuchu kosztuje zajęcia.",
  mod=("nauczyciel prowadzi rozmowę przy stoliku dziecka, bez odchodzenia od grupy",
       "dziecko korzysta z rozmowy i wraca do zadania po sygnale",
       "dziecko samo umawia porę rozmowy i dotrzymuje umowy"),
  arkusz=dict(
   tytul="Karty do zajęć „Dwie minuty tylko dla mnie”",
   wstep="Wytnij karty i wklej je w plan dnia dziecka. Karta „następna rozmowa” zostaje "
         "u dziecka po zakończeniu tej — widoczna zapowiedź działa lepiej niż obietnica "
         "powiedziana raz.",
   karty=[("Rozmowa", "symbol rozmowy: dwa krzesła, dwie osoby"),
          ("Dwie minuty", "symbol minutnika ustawionego na czas rozmowy"),
          ("Wracam do zadania", "symbol powrotu na miejsce"),
          ("Następna rozmowa", "symbol pory dnia, o której będzie następna")],
   pasek=["rozmawiam", "sygnał", "wracam"])),

 "III.5": dict(
  tytul="Umówiony znak",
  icf="d335·d710", pp="3.5·2.11",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["gest ustalony z dzieckiem, krótszy niż podejście",
          "odpowiedź dorosłego natychmiastowa i widoczna: skinienie",
          "uczenie pokazywania własnej pracy w umówionym momencie",
          "nazywanie potrzeby wprost: „chcę, żebyś zobaczył”",
          "minimalna reakcja na sprawdzanie zachowaniem trudnym"],
  pomoce=["karta z rysunkiem umówionego gestu",
          "tabliczka „zobacz, co zrobiłem” do postawienia na stoliku",
          "kącik prezentacji prac, oglądany o stałej porze",
          "żetony za skorzystanie z gestu"],
  wskazowka="Sprawdzanie reakcji dorosłego to prośba o kontakt, nie prowokacja. Nazwij "
            "ją dziecku wprost i daj krótszą drogę — inaczej zostanie przy tej, którą zna, "
            "bo tamta zawsze przynosi spojrzenie.",
  ter_kryt="Rejestr ABC — czy przed zachowaniem pojawił się gest · wszystkie obserwowane sytuacje.",
  R="Kontakt wzrokowy z dorosłym to potrzeba, którą da się zaspokoić w pół sekundy.",
  mod=("nauczyciel modeluje gest i odpowiada na każdy, nawet niepełny",
       "dziecko unosi dłoń samo i czeka na skinienie",
       "dziecko mówi wprost, czego chce: pochwały, spojrzenia albo pomocy"),
  arkusz=dict(
   tytul="Karty do zajęć „Umówiony znak”",
   wstep="Wytnij karty. Gest ustal z dzieckiem i narysuj go na karcie razem z nim — "
         "znak wymyślony wspólnie działa lepiej niż narzucony. Symbole pozostałych kart "
         "wklej z biblioteki EduPlaner.",
   karty=[("Mój znak", "miejsce na rysunek umówionego gestu"),
          ("Widzę cię", "symbol skinienia dorosłego"),
          ("Zobacz, co zrobiłem", "symbol pokazywania własnej pracy"),
          ("Poczekam", "symbol krótkiego czekania na spojrzenie")],
   pasek=["daję znak", "dostaję skinienie", "pracuję dalej"])),
}

WARIANTY = {
 # ——— III.11 · czekanie na uwagę —————————————————————————————————————
 ("III.1", "A"): dict(
  podtytul="Czekanie 30 sekund z kartą „czekam” przy zajętym dorosłym",
  ter="Dziecko poczeka 30 sekund przy dorosłym zajętym innym dzieckiem, trzymając kartę "
      "„czekam”, zamiast wołać albo ciągnąć za rękę.",
  S="Trzyma kartę i zostaje przy stoliku przez czas klepsydry.",
  A="Karta w dłoni daje dziecku co robić w czasie, który wcześniej był pusty.",
  pomoc_wiek="mała klepsydra 30-sekundowa podawana razem z kartą",
  przebieg=[
   ("N — pokazuje kartę „czekam” i klepsydrę, nazywa obie.",
    "D — trzyma kartę i ogląda klepsydrę."),
   ("N — zajmuje się przez chwilę innym dzieckiem, zostając w zasięgu wzroku.",
    "D — widzi, że nauczyciel jest zajęty."),
   ("N — gdy dziecko woła, podaje kartę i odwraca klepsydrę.",
    "D — bierze kartę i patrzy na klepsydrę."),
   ("N — podchodzi dokładnie po przesypaniu klepsydry.",
    "D — czeka do końca, trzymając kartę."),
   ("N — nazywa: „czekałeś i przyszedłem”, i zajmuje się dzieckiem.",
    "D — pokazuje, o co mu chodziło.")]),
 ("III.1", "B"): dict(
  podtytul="Położenie karty „potrzebuję pomocy” i czekanie dwie minuty",
  ter="Dziecko położy na stoliku kartę „potrzebuję pomocy” i poczeka dwie minuty, "
      "nie odchodząc od stolika.",
  S="Kładzie kartę i zostaje przy zadaniu do podejścia nauczyciela.",
  A="Karta działa bez mówienia i bez wstawania — nie przerywa pracy innym dzieciom.",
  pomoc_wiek="karta „potrzebuję pomocy” w stałym rogu stolika",
  przebieg=[
   ("N — przypomina, gdzie leży karta i po jakim czasie podchodzi.",
    "D — sprawdza miejsce karty."),
   ("N — daje zadanie z jednym trudniejszym miejscem.",
    "D — pracuje do momentu, w którym potrzebuje pomocy."),
   ("N — jest zajęty innym dzieckiem i nie patrzy w stronę stolika.",
    "D — kładzie kartę zamiast wołać."),
   ("N — podchodzi po dwóch minutach, dokładnie jak obiecał.",
    "D — czeka przy stoliku, zajmując się zadaniem."),
   ("N — pomaga i zaznacza na karcie dziecka udane czekanie.",
    "D — kończy zadanie z pomocą.")]),
 ("III.1", "C"): dict(
  podtytul="Czekanie do końca rozmowy nauczyciela z innym dzieckiem",
  ter="Dziecko poczeka do końca rozmowy nauczyciela z innym dzieckiem, nie przerywając "
      "jej, i w tym czasie zrobi kolejny krok swojego zadania.",
  S="Nie wchodzi w rozmowę i pracuje dalej, dopóki nauczyciel nie skończy.",
  A="Zadanie „w międzyczasie” daje zajęcie na czas czekania, które nie ma stałej długości.",
  pomoc_wiek="karta „w międzyczasie” z jednym krokiem zadania do zrobienia",
  przebieg=[
   ("N — umawia się z dzieckiem: „gdy rozmawiam, robisz kolejny krok”.",
    "D — powtarza umowę własnymi słowami."),
   ("N — rozmawia z innym dzieckiem przez kilka minut.",
    "D — pracuje i nie przerywa rozmowy."),
   ("N — obserwuje kątem oka, czy dziecko wytrzymuje.",
    "D — kładzie kartę prośby, jeśli potrzebuje pomocy."),
   ("N — kończy rozmowę i podchodzi do dziecka.",
    "D — mówi, o co chciało zapytać."),
   ("N — pyta, co udało się zrobić w czasie czekania.",
    "D — pokazuje wykonany krok zadania.")]),

 # ——— III.12 · akceptowalna prośba o uwagę —————————————————————————————
 ("III.2", "A"): dict(
  podtytul="Dotknięcie ramienia nauczyciela zamiast krzyku",
  ter="Dziecko dotknie ramienia nauczyciela, żeby zwrócić na siebie uwagę, zamiast "
      "krzyczeć albo rzucać przedmiotem.",
  S="Podchodzi i dotyka ramienia dorosłego.",
  A="Gest dotykowy jest dla trzylatka prostszy niż podniesiona ręka i czekanie.",
  pomoc_wiek="ćwiczenie gestu w zabawie: „obudź misia dotknięciem”",
  przebieg=[
   ("N — pokazuje gest na maskotce i prosi dziecko o powtórzenie.",
    "D — dotyka ramienia maskotki i nauczyciela."),
   ("N — bawi się z dzieckiem, potem odwraca się do innego zajęcia.",
    "D — chce zwrócić na siebie uwagę."),
   ("N — czeka na gest, nie reagując na hałas.",
    "D — dotyka ramienia nauczyciela."),
   ("N — odwraca się natychmiast i nazywa: „dotknąłeś, jestem”.",
    "D — pokazuje, czego chciało."),
   ("N — powtarza sytuację jeszcze dwa razy w czasie zajęć.",
    "D — używa gestu w kolejnych sytuacjach.")]),
 ("III.2", "B"): dict(
  podtytul="Podniesienie ręki i czekanie na skinienie nauczyciela",
  ter="Dziecko podniesie rękę samo i poczeka na skinienie nauczyciela, zamiast zaczepiać "
      "inne dzieci albo hałasować.",
  S="Podnosi rękę i trzyma ją do skinienia dorosłego.",
  A="Skinienie jest natychmiastową odpowiedzią, choć pomoc przychodzi chwilę później.",
  pomoc_wiek="żetony za skorzystanie z ręki, zbierane na tabliczce",
  przebieg=[
   ("N — ustala z grupą: ręka w górę, potem skinienie, potem podejście.",
    "D — ćwiczy gest w zabawie."),
   ("N — prowadzi zajęcia grupowe i pracuje z innymi dziećmi.",
    "D — potrzebuje kontaktu i podnosi rękę."),
   ("N — kiwa głową natychmiast, choć podchodzi po chwili.",
    "D — opuszcza rękę i czeka."),
   ("N — podchodzi i daje żeton za skorzystanie z ręki.",
    "D — bierze żeton i mówi, o co chodziło."),
   ("N — na zachowanie trudne reaguje krótko, bez rozmowy.",
    "D — wraca do ręki jako drogi szybszej.")]),
 ("III.2", "C"): dict(
  podtytul="Prośba o uwagę słowami i nazwanie, w czym potrzebna pomoc",
  ter="Dziecko poprosi o uwagę słowami i powie, w czym potrzebuje pomocy, zamiast "
      "zwracać ją na siebie zachowaniem trudnym.",
  S="Mówi pełnym zdaniem, czego potrzebuje, i czeka na odpowiedź.",
  A="Nazwana potrzeba skraca rozmowę — dorosły wie od razu, o co chodzi.",
  pomoc_wiek="karta zdań: „potrzebuję pomocy przy…”, „chcę pokazać…”",
  przebieg=[
   ("N — omawia trzy zdania z karty i ćwiczy je z dziećmi.",
    "D — powtarza zdania i wybiera swoje."),
   ("N — prowadzi zajęcia i jest zajęty grupą.",
    "D — potrzebuje kontaktu w trakcie pracy."),
   ("N — czeka na zgłoszenie słowne, nie reaguje na zaczepki.",
    "D — mówi pełnym zdaniem, czego potrzebuje."),
   ("N — odpowiada na treść prośby, nie na sam fakt zgłoszenia.",
    "D — dostaje pomoc albo umówioną porę rozmowy."),
   ("N — po zajęciach pyta, które zdanie było najłatwiejsze.",
    "D — wybiera zdanie do używania na co dzień.")]),

 # ——— III.13 · wypowiedź w swojej kolejce ——————————————————————————————
 ("III.3", "A"): dict(
  podtytul="Jedno słowo w rundzie z maskotką mówiącego",
  ter="Dziecko powie jedno słowo w rundzie, gdy dostanie do ręki maskotkę mówiącego, "
      "i odda ją dalej.",
  S="Mówi jedno słowo trzymając maskotkę i przekazuje ją sąsiadowi.",
  A="Maskotka pokazuje, czyja jest kolej — zasada jest widoczna, nie tylko słyszana.",
  pomoc_wiek="duża maskotka przekazywana z rąk do rąk",
  forma="grupa na dywanie (4–6 dzieci)",
  przebieg=[
   ("N — pokazuje maskotkę i mówi: „głos ma ten, kto trzyma”.",
    "D — dotyka maskotki i patrzy na trzymającego."),
   ("N — zaczyna rundę od siebie i mówi jedno słowo.",
    "D — słucha i czeka."),
   ("N — podaje maskotkę dziecku jako drugiemu w kolejności.",
    "D — bierze maskotkę i mówi jedno słowo."),
   ("N — prosi o przekazanie maskotki dalej.",
    "D — oddaje maskotkę sąsiadowi."),
   ("N — kończy rundę i nazywa: „każdy powiedział, każdy słuchał”.",
    "D — oddaje maskotkę nauczycielowi.")]),
 ("III.3", "B"): dict(
  podtytul="Czekanie na swoją kolej bez wchodzenia w słowo",
  ter="Dziecko poczeka na swoją kolej w rundzie i nie wejdzie w słowo innym dzieciom, "
      "a potem powie zdanie na temat rundy.",
  S="Milczy w czasie cudzych wypowiedzi i mówi w swojej kolejce.",
  A="Karta kolejności pokazuje, ile osób jest przed nim — czekanie ma widoczny koniec.",
  pomoc_wiek="karta kolejności z symbolami dzieci w kręgu",
  forma="grupa na dywanie (5–6 dzieci)",
  przebieg=[
   ("N — układa karty kolejności i pokazuje, które miejsce ma dziecko.",
    "D — liczy, ile osób mówi przed nim."),
   ("N — rozpoczyna rundę i pilnuje kolejności.",
    "D — słucha wypowiedzi poprzedników."),
   ("N — daje podpowiedź wzrokową, gdy dziecko zaczyna wchodzić w słowo.",
    "D — powstrzymuje się i czeka dalej."),
   ("N — podaje maskotkę w kolejce dziecka.",
    "D — mówi zdanie na temat rundy."),
   ("N — nazywa oba osiągnięcia: wypowiedź i wysłuchanie innych.",
    "D — przekazuje głos dalej.")]),
 ("III.3", "C"): dict(
  podtytul="Wypowiedź na forum grupy z odniesieniem do słów innego dziecka",
  ter="Dziecko wypowie się na forum grupy w swojej kolejce i odniesie się do tego, "
      "co powiedziało inne dziecko.",
  S="Mówi w kolejce i nawiązuje do wcześniejszej wypowiedzi kolegi.",
  A="Zadanie „powiedz, co powiedział poprzednik” daje powód do słuchania, a nie tylko nakaz.",
  pomoc_wiek="karta „nawiązuję”: „zgadzam się z…”, „ja mam inaczej niż…”",
  forma="grupa (6–8 dzieci)",
  przebieg=[
   ("N — zapowiada rundę i zadanie: każdy nawiązuje do poprzednika.",
    "D — powtarza zasadę własnymi słowami."),
   ("N — prowadzi rundę i pilnuje, żeby nikt nie wchodził w słowo.",
    "D — słucha poprzednika i przygotowuje nawiązanie."),
   ("N — podaje głos dziecku w jego kolejce.",
    "D — mówi, do czego się odnosi, i wypowiada swoje zdanie."),
   ("N — pyta grupę, czy nawiązanie pasowało do wypowiedzi.",
    "D — przyjmuje informację zwrotną od dzieci."),
   ("N — kończy rundę i pyta, czyja wypowiedź była najciekawsza i dlaczego.",
    "D — nazywa czyjąś wypowiedź i uzasadnia wybór.")]),

 # ——— III.14 · uwaga „z wyprzedzeniem” ————————————————————————————————
 ("III.4", "A"): dict(
  podtytul="Minuta uwagi na powitanie i przejście do zabawy",
  ter="Dziecko skorzysta z minuty uwagi na powitanie i przejdzie do zabawy razem "
      "z dorosłym, bez zatrzymywania go przy sobie.",
  S="Rozmawia albo bawi się minutę z dorosłym i idzie z nim do zabawy w grupie.",
  A="Uwaga dana na wejściu zaspokaja potrzebę, zanim dziecko zacznie jej szukać.",
  pomoc_wiek="stały rytuał powitania: przybicie piątki i jedno pytanie",
  przebieg=[
   ("N — wita dziecko przy drzwiach osobno od reszty grupy.",
    "D — przybija piątkę i odpowiada na pytanie."),
   ("N — poświęca dziecku minutę pełnej uwagi, bez rozmów z innymi.",
    "D — opowiada albo pokazuje, co przyniosło."),
   ("N — zapowiada koniec: „jeszcze jedna rzecz i idziemy do zabawy”.",
    "D — kończy opowiadanie."),
   ("N — idzie z dzieckiem do wybranego kącika i zostaje chwilę.",
    "D — zaczyna zabawę w kąciku."),
   ("N — odchodzi, mówiąc, kiedy wróci: „przyjdę po śniadaniu”.",
    "D — bawi się dalej po odejściu dorosłego.")]),
 ("III.4", "B"): dict(
  podtytul="Dwie minuty rozmowy na starcie zajęć i powrót do zadania",
  ter="Dziecko skorzysta z dwóch minut rozmowy na początku zajęć i wróci do zadania "
      "po sygnale minutnika.",
  S="Rozmawia dwie minuty i wraca na miejsce po sygnale, bez przedłużania.",
  A="Zapowiedziana pora i minutnik sprawiają, że koniec rozmowy nie jest odrzuceniem.",
  pomoc_wiek="minutnik dwuminutowy stawiany między dzieckiem a nauczycielem",
  przebieg=[
   ("N — pokazuje na planie dnia, kiedy będzie rozmowa.",
    "D — wie, o której porze dostanie rozmowę."),
   ("N — siada z dzieckiem i nastawia minutnik.",
    "D — opowiada o tym, co dla niego ważne."),
   ("N — słucha bez przerywania i bez zadań w tle.",
    "D — korzysta z całej rozmowy."),
   ("N — po sygnale kończy i zapowiada następną rozmowę.",
    "D — wraca do zadania po sygnale."),
   ("N — w trakcie zajęć daje krótkie sygnały uwagi pozytywnej.",
    "D — pracuje, dostając uwagę bez zachowania trudnego.")]),
 ("III.4", "C"): dict(
  podtytul="Umówienie pory rozmowy i dotrzymanie umowy",
  ter="Dziecko umówi się z nauczycielem na porę rozmowy i dotrzyma tej umowy, "
      "nie przerywając zajęć wcześniej.",
  S="Ustala porę, zapisuje ją i czeka do umówionego momentu.",
  A="Zapisana umowa jest widoczna dla obu stron — dziecko wie, że rozmowa na pewno będzie.",
  pomoc_wiek="karta umowy z porą rozmowy, podpisana przez dziecko i nauczyciela",
  przebieg=[
   ("N — rano pyta, kiedy dziecko chce porozmawiać, i pokazuje plan dnia.",
    "D — wybiera porę i zaznacza ją na karcie."),
   ("N — podpisuje umowę razem z dzieckiem.",
    "D — podpisuje albo stawia swój znak."),
   ("N — prowadzi zajęcia; nie zaczyna rozmowy przed czasem.",
    "D — czeka do umówionej pory, pracując z grupą."),
   ("N — o umówionej porze przerywa swoje zajęcie i siada z dzieckiem.",
    "D — rozmawia w umówionym czasie."),
   ("N — pyta, czy pora była dobra i kiedy umawiamy się jutro.",
    "D — proponuje porę na następny dzień.")]),

 # ——— III.15 · umówiony gest zamiast sprawdzania ————————————————————————
 ("III.5", "A"): dict(
  podtytul="Szukanie wzrokiem i pokazanie karty zamiast rzucenia zabawką",
  ter="Dziecko poszuka wzrokiem nauczyciela i pokaże kartę, zamiast rzucić zabawką, "
      "żeby dorosły zareagował.",
  S="Patrzy na nauczyciela i podnosi kartę.",
  A="Karta w ręce daje dziecku coś do zrobienia zamiast sięgania po przedmiot.",
  pomoc_wiek="mała karta ze znakiem, przyczepiona do stolika na rzepie",
  przebieg=[
   ("N — pokazuje kartę i ćwiczy z dzieckiem podnoszenie jej w zabawie.",
    "D — podnosi kartę na sygnał zabawy."),
   ("N — bawi się z dzieckiem, potem odwraca się do innego dziecka.",
    "D — szuka wzrokiem nauczyciela."),
   ("N — reaguje spojrzeniem tylko na podniesioną kartę.",
    "D — podnosi kartę zamiast rzucić zabawką."),
   ("N — natychmiast patrzy i uśmiecha się do dziecka.",
    "D — pokazuje, co robi albo czego chce."),
   ("N — powtarza sytuację, oddalając się na dłużej.",
    "D — używa karty także przy dłuższym oddaleniu dorosłego.")]),
 ("III.5", "B"): dict(
  podtytul="Uniesienie dłoni i czekanie na odpowiedź dorosłego",
  ter="Dziecko uniesie dłoń samo i poczeka na odpowiedź dorosłego, zamiast sprawdzać "
      "jego reakcję zachowaniem trudnym.",
  S="Unosi dłoń i czeka do skinienia, nie robiąc nic w międzyczasie.",
  A="Gest jest krótszy niż podejście i nie przerywa pracy innym dzieciom.",
  pomoc_wiek="karta z rysunkiem gestu ustalonego wspólnie z dzieckiem",
  przebieg=[
   ("N — ustala z dzieckiem gest i rysuje go razem z nim na karcie.",
    "D — proponuje gest i rysuje go."),
   ("N — ćwiczy gest w zabawie kilka razy.",
    "D — używa gestu i dostaje natychmiastowe skinienie."),
   ("N — prowadzi zajęcia i pracuje z innymi dziećmi.",
    "D — unosi dłoń, gdy chce sprawdzić, czy dorosły patrzy."),
   ("N — odpowiada skinieniem w ciągu kilku sekund.",
    "D — opuszcza dłoń i pracuje dalej."),
   ("N — zapisuje w rejestrze, czy przed zachowaniem pojawił się gest.",
    "D — używa gestu kolejny raz w czasie zajęć.")]),
 ("III.5", "C"): dict(
  podtytul="Powiedzenie wprost, że chce się pochwały albo uwagi",
  ter="Dziecko powie wprost, że chce pochwały albo uwagi, zamiast sprawdzać reakcję "
      "dorosłego zachowaniem trudnym.",
  S="Mówi zdaniem, czego chce: „chcę, żebyś zobaczył”, „chcę pochwały”.",
  A="Nazwanie potrzeby wprost jest szybsze niż jej sprawdzanie i nie kosztuje zajęć.",
  pomoc_wiek="karta trzech zdań o potrzebie kontaktu, ćwiczonych w parach",
  przebieg=[
   ("N — omawia trzy zdania i ćwiczy je w parach z dziećmi.",
    "D — mówi zdania koledze i słyszy je od niego."),
   ("N — pyta, kiedy najczęściej chce się być zauważonym.",
    "D — nazywa swoje sytuacje: po skończonej pracy, przy trudnym zadaniu."),
   ("N — prowadzi zajęcia bez komentowania zachowań szukających uwagi.",
    "D — mówi wprost, czego chce, zamiast sprawdzać reakcję."),
   ("N — odpowiada na treść: ogląda pracę albo chwali konkret.",
    "D — przyjmuje pochwałę i wraca do zajęć."),
   ("N — po zajęciach pyta, czy powiedzenie wprost było trudne.",
    "D — ocenia i wybiera zdanie na następne zajęcia.")]),
}
