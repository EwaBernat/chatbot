# -*- coding: utf-8 -*-
"""Konspekty do funkcji II — sensoryczne / autostymulacja (wskaźniki II.1–II.5).

Wspólny mianownik: **autostymulacji nie zabieramy, tylko zamieniamy.** Zachowanie
dostarcza dziecku wrażenia, którego naprawdę potrzebuje; samo „nie rób tak” zostawia
je z potrzebą i bez sposobu. Konspekt daje formę zastępczą, która daje to samo
wrażenie i nie przeszkadza w grupie — a przy planowaniu współpracujemy z terapeutą SI.
"""

RDZEN = {
 "II.1": dict(
  tytul="Coś do rąk, kiedy trzeba",
  icf="b147·d240", pp="9.3·2.12",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · elementy diety sensorycznej",
  metody=["dieta sensoryczna: stały zestaw akceptowalnych źródeł wrażeń",
          "przedmiot regulacyjny dostępny bez proszenia",
          "uczenie odkładania przedmiotu po skończonym zadaniu",
          "próbki czasowe zamiast ciągłej obserwacji",
          "współpraca z terapeutą SI przy doborze bodźca"],
  pomoce=["pudełko regulacyjne przy stoliku: gniotek, kolczasta piłeczka, kawałek futerka",
          "taśma elastyczna zawiązana na nogach krzesła",
          "podkładka z polem „tu odkładam”, gdy kończę",
          "zadanie do pracy samodzielnej na 10 minut"],
  wskazowka="Nie zabieraj przedmiotu regulacyjnego za karę i nie odbieraj go, gdy dziecko "
            "pracuje. Odebrany gniotek nie kończy potrzeby — wraca wtedy autostymulacja, "
            "którą właśnie zamieniliśmy.",
  ter_kryt="Arkusz próbek czasowych — co 10 minut pracy samodzielnej · 10 odcinków w tygodniu.",
  R="Praca samodzielna to najdłuższy odcinek dnia bez dorosłego obok — tam potrzeba wraca najmocniej.",
  mod=("nauczyciel podaje przedmiot do ręki przy pierwszych oznakach pobudzenia",
       "pudełko regulacyjne stoi przy stoliku, dziecko sięga po nie samo",
       "dziecko wybiera przedmiot na cały dzień i odkłada go po każdym zadaniu"),
  arkusz=dict(
   tytul="Karty do zajęć „Coś do rąk, kiedy trzeba”",
   wstep="Wytnij karty i przyklej je na pudełku regulacyjnym oraz na podkładce dziecka. "
         "W pola wklej zdjęcia albo symbole konkretnych przedmiotów z biblioteki "
         "EduPlaner — dziecko ma poznać swój przedmiot, nie kategorię.",
   karty=[("Ściskam", "symbol gniotka albo piłeczki"),
          ("Ciągnę", "symbol taśmy elastycznej przy krześle"),
          ("Dotykam", "symbol materiału o wyraźnej fakturze"),
          ("Odkładam", "symbol miejsca, w którym przedmiot czeka po zadaniu")],
   pasek=["biorę", "pracuję", "odkładam"])),

 "II.2": dict(
  tytul="Czego mi teraz trzeba",
  icf="b156·d335", pp="9.10·2.10",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · elementy diety sensorycznej",
  metody=["nazywanie wrażeń trzema kategoriami: ruch, ucisk, cisza",
          "wybór z dwóch propozycji zamiast pytania otwartego",
          "sprawdzanie po fakcie, czy wybrana forma pomogła",
          "karta diety sensorycznej jako stały punkt odniesienia",
          "modelowanie: dorosły też nazywa, czego potrzebuje"],
  pomoce=["karta diety sensorycznej z trzema polami wrażeń",
          "po dwie propozycje form w każdym polu",
          "kącik z materiałami do każdego z trzech wrażeń",
          "buźki „pomogło / nie pomogło” do zaznaczania po formie"],
  wskazowka="Pytanie „czego chcesz?” jest za szerokie i najczęściej kończy się milczeniem. "
            "Pokaż dwie karty i pozwól wybrać — wybór z dwóch jest odpowiedzią, na którą "
            "dziecko stać także wtedy, gdy jest pobudzone.",
  ter_kryt="Karta diety sensorycznej — zapis wyboru i formy · wszystkie przerwy sensoryczne.",
  R="Nazwane wrażenie da się zaspokoić inaczej niż zachowaniem trudnym.",
  mod=("nauczyciel pokazuje dwa obrazki i prosi o wskazanie jednego",
       "dziecko wskazuje wrażenie na karcie i wybiera formę samo",
       "dziecko planuje z nauczycielem, które wrażenia dostanie w ciągu dnia"),
  arkusz=dict(
   tytul="Karta diety sensorycznej do zajęć „Czego mi teraz trzeba”",
   wstep="Wytnij karty wrażeń i powieś je na wysokości wzroku dziecka. W pola wklej "
         "symbole form, które są u was naprawdę dostępne — karta z formą, której nie ma "
         "w sali, uczy dziecko, że wskazywanie nic nie daje.",
   karty=[("Ruch", "symbol huśtania, skakania albo chodzenia"),
          ("Ucisk", "symbol koca obciążeniowego, poduszki, mocnego przytulenia"),
          ("Cisza", "symbol słuchawek albo kącika wyciszenia"),
          ("Pomogło?", "dwie buźki do zaznaczenia po skorzystaniu z formy")],
   pasek=["wskazuję", "korzystam", "sprawdzam"])),

 "II.3": dict(
  tytul="Przerwa, zanim będzie za dużo",
  icf="d230·d240", pp="9.10·2.12",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · elementy diety sensorycznej",
  metody=["przerwa zaplanowana, nie ratunkowa — przed narastaniem, nie po",
          "sygnał czasu zamiast decyzji dorosłego",
          "stałe miejsce i stała forma przerwy",
          "odhaczanie przerwy na planie dnia",
          "stopniowe przekazywanie dziecku decyzji o momencie przerwy"],
  pomoce=["minutnik z sygnałem dźwiękowym, ten sam każdego dnia",
          "plan dnia z zaznaczonymi przerwami sensorycznymi",
          "stałe miejsce przerwy, zawsze przygotowane",
          "karta „odhaczam przerwę” z polami na cztery przerwy"],
  wskazowka="Przerwa ma wyprzedzać zachowanie, nie następować po nim. Przerwa dana po "
            "wybuchu wygląda tak samo, a uczy czegoś przeciwnego — że wybuch jest drogą "
            "do przerwy.",
  ter_kryt="Plan przerw — odhaczenie przerwy wziętej samodzielnie · 4 przerwy dziennie.",
  R="Przerwa uprzedzająca kosztuje trzy minuty; przerywanie zachowania kosztuje pół dnia.",
  mod=("nauczyciel prowadzi dziecko do miejsca przerwy po sygnale",
       "dziecko idzie samo po sygnale minutnika, bez przypominania",
       "dziecko planuje przerwy na swoim planie dnia i pilnuje ich samo"),
  arkusz=dict(
   tytul="Plan przerw do zajęć „Przerwa, zanim będzie za dużo”",
   wstep="Wytnij karty i pasek przerw. Pasek zostaje przy dziecku na cały dzień — "
         "odhaczona przerwa jest widocznym dowodem, że plan działa. Symbole wklej "
         "z biblioteki EduPlaner.",
   karty=[("Przerwa 1", "symbol pory dnia: po śniadaniu"),
          ("Przerwa 2", "symbol pory dnia: przed zajęciami"),
          ("Przerwa 3", "symbol pory dnia: po obiedzie"),
          ("Moje miejsce", "symbol miejsca, w którym odbywa się przerwa")],
   pasek=["sygnał", "idę", "odhaczam"])),

 "II.4": dict(
  tytul="Skończyłem — i co teraz",
  icf="d210·d920", pp="2.1·2.5",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["wybór z trzech zamiast pustej przestrzeni po zadaniu",
          "zajęcie „po skończeniu” przygotowane wcześniej, nie wymyślane na miejscu",
          "wzmocnienie za zajęcie się czymś samodzielnie",
          "wydłużanie czasu samodzielnego zajęcia",
          "uczenie sprzątania miejsca po zajęciu"],
  pomoce=["tacka „skończyłem” z trzema gotowymi zajęciami",
          "lista trzech aktywności z symbolami przy stoliku",
          "minutnik na pięć minut samodzielnego zajęcia",
          "koszyk na materiały do odłożenia po skończeniu"],
  wskazowka="Puste minuty po zadaniu to nie jest chwila odpoczynku dla nauczyciela, tylko "
            "najbardziej ryzykowny moment dnia. Zajęcie „po skończeniu” ma być gotowe, zanim "
            "dziecko skończy — wymyślane na miejscu przychodzi zwykle o minutę za późno.",
  ter_kryt="Rejestr ABC — kolumna A: koniec zadania przed czasem · wszystkie sytuacje oczekiwania.",
  R="Nuda jest wyzwalaczem tak samo policzalnym jak polecenie — i tak samo da się ją zaplanować.",
  mod=("nauczyciel podaje dwie zabawki do wyboru zaraz po skończonym zadaniu",
       "dziecko wybiera z tacki „skończyłem” samo i pracuje pięć minut",
       "dziecko proponuje własne zajęcie i doprowadza je do końca"),
  arkusz=dict(
   tytul="Karty do zajęć „Skończyłem — i co teraz”",
   wstep="Wytnij karty i powieś je przy stoliku dziecka. Wklej symbole zajęć, które są "
         "w sali naprawdę dostępne bez pytania dorosłego — lista z zajęciem wymagającym "
         "zgody nie działa w momencie, w którym jest potrzebna.",
   karty=[("Wybór 1", "symbol pierwszego zajęcia po skończonej pracy"),
          ("Wybór 2", "symbol drugiego zajęcia"),
          ("Wybór 3", "symbol trzeciego zajęcia"),
          ("Sprzątam", "symbol odłożenia materiałów na miejsce")],
   pasek=["kończę", "wybieram", "zajmuję się"])),

 "II.5": dict(
  tytul="Stop i zamiana",
  icf="b147·d230", pp="9.3·2.12",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · elementy diety sensorycznej",
  metody=["sygnał wzrokowo-dotykowy zamiast polecenia słownego",
          "zamiana na formę dającą to samo wrażenie",
          "stały czas na zakończenie: 30 sekund od sygnału",
          "brak konfrontacji: nie przytrzymujemy, nie zabieramy siłą",
          "uczenie samodzielnego zauważania: „robię to znowu”"],
  pomoce=["karta „stop — zamiana” z dwoma polami",
          "forma zastępcza dająca to samo wrażenie, przygotowana wcześniej",
          "delikatny sygnał dotykowy ustalony z dzieckiem",
          "stoper do mierzenia czasu od sygnału do zakończenia"],
  wskazowka="Słowa w trakcie autostymulacji zwykle nie docierają — dlatego sygnał jest "
            "wzrokowo-dotykowy. Nie przytrzymuj dziecka i nie zabieraj przedmiotu siłą: "
            "przerwanie siłą kończy zachowanie na minutę i psuje relację na tydzień.",
  ter_kryt="Rejestr ABC — czas od sygnału do zakończenia · wszystkie sygnały w tygodniu.",
  R="Zamiana daje dziecku to samo wrażenie w formie, która nie wyklucza go z grupy.",
  mod=("nauczyciel kładzie dłoń na dłoni dziecka i podaje formę zastępczą",
       "sam sygnał wzrokowy, forma zastępcza leży w zasięgu ręki",
       "dziecko samo zauważa autostymulację i sięga po formę zastępczą"),
  arkusz=dict(
   tytul="Karty do zajęć „Stop i zamiana”",
   wstep="Wytnij kartę sygnału i karty form zastępczych. Forma zastępcza musi dawać to "
         "samo wrażenie co zachowanie, które zamieniamy — dobierz ją z terapeutą SI "
         "i wklej jej symbol z biblioteki EduPlaner.",
   karty=[("Stop", "symbol zatrzymania — ten sam gest, ten sam obrazek"),
          ("Zamiana", "symbol formy zastępczej dającej to samo wrażenie"),
          ("Ruch", "symbol formy ruchowej, gdy zachowanie daje ruch"),
          ("Dźwięk", "symbol formy dźwiękowej, gdy zachowanie daje dźwięk")],
   pasek=["widzę sygnał", "kończę", "biorę zamianę"])),
}

WARIANTY = {
 # ——— II.6 · korzystanie z przedmiotu do regulacji ——————————————————————
 ("II.1", "A"): dict(
  podtytul="Ściskanie gniotka podanego przez nauczyciela zamiast machania rękami",
  ter="Dziecko weźmie gniotek podany przez nauczyciela i ściśnie go zamiast machać rękami, "
      "zostając przy swoim zadaniu.",
  S="Bierze gniotek do ręki i ściska go, nie odchodząc od stolika.",
  A="Przedmiot podany w momencie pobudzenia trafia wcześniej niż polecenie słowne.",
  pomoc_wiek="gniotek podawany do ręki przy pierwszych oznakach pobudzenia",
  przebieg=[
   ("N — kładzie pudełko regulacyjne przy stoliku i pokazuje, co w nim jest.",
    "D — ogląda i dotyka przedmiotów z pudełka."),
   ("N — daje dziecku znane, krótkie zadanie przy stoliku.",
    "D — pracuje przy stoliku przez kilka minut."),
   ("N — przy pierwszych oznakach pobudzenia podaje gniotek do ręki.",
    "D — bierze gniotek i ściska go."),
   ("N — nazywa: „ściskasz, kiedy ręce chcą się ruszać”, i nie odbiera przedmiotu.",
    "D — trzyma gniotek i wraca wzrokiem do zadania."),
   ("N — po zadaniu pokazuje pole „tu odkładam”.",
    "D — odkłada gniotek na wskazane miejsce.")]),
 ("II.1", "B"): dict(
  podtytul="Samodzielne sięgnięcie po przedmiot regulacyjny w czasie pracy",
  ter="Dziecko sięgnie po taśmę albo gniotek samo w czasie pracy przy stoliku, "
      "nie przerywając zadania.",
  S="Sięga po przedmiot z pudełka i pracuje dalej z przedmiotem w ręce albo pod stopami.",
  A="Pudełko stoi w zasięgu ręki — sięgnięcie nie wymaga pytania ani wstawania.",
  pomoc_wiek="pudełko regulacyjne stojące w stałym miejscu przy stoliku dziecka",
  przebieg=[
   ("N — przypomina, co jest w pudełku i że można brać bez pytania.",
    "D — sprawdza zawartość pudełka."),
   ("N — daje zadanie na dziesięć minut pracy samodzielnej.",
    "D — zaczyna pracę przy stoliku."),
   ("N — obserwuje z boku, nie proponuje przedmiotu.",
    "D — sięga po gniotek albo napina taśmę, gdy poczuje potrzebę."),
   ("N — nie komentuje sięgnięcia, żeby nie przerywać pracy.",
    "D — pracuje dalej, korzystając z przedmiotu."),
   ("N — po zadaniu pyta, co pomogło: taśma czy gniotek.",
    "D — nazywa, co wybrało, i odkłada przedmiot na miejsce.")]),
 ("II.1", "C"): dict(
  podtytul="Wybór formy regulacji i uzasadnienie wyboru",
  ter="Dziecko wybierze formę regulacji, powie, dlaczego akurat tej potrzebuje, "
      "i wróci do zadania po skorzystaniu z niej.",
  S="Nazywa wybraną formę i powód, korzysta z niej i wraca do pracy.",
  A="Nazwany powód pozwala dobrać formę do potrzeby, zamiast sięgać po pierwszą z brzegu.",
  pomoc_wiek="karta z czterema formami regulacji i miejscem na powód wyboru",
  przebieg=[
   ("N — pokazuje kartę czterech form i prosi o wybór jednej.",
    "D — wybiera formę i wskazuje ją na karcie."),
   ("N — pyta: „dlaczego akurat ta?”.",
    "D — uzasadnia wybór: „bo ręce mi się ruszają”, „bo jest głośno”."),
   ("N — pozwala skorzystać z formy przez ustalony czas.",
    "D — korzysta z wybranej formy."),
   ("N — pyta po czasie, czy pomogło, i zaznacza odpowiedź na karcie.",
    "D — ocenia skuteczność formy i zaznacza buźkę."),
   ("N — wraca z dzieckiem do przerwanego zadania.",
    "D — kończy zadanie i odkłada materiał regulacyjny.")]),

 # ——— II.7 · nazwanie potrzeby sensorycznej ————————————————————————————
 ("II.2", "A"): dict(
  podtytul="Wskazanie na dwóch obrazkach, czego potrzebują ręce i ciało",
  ter="Dziecko wskaże na dwóch obrazkach, czy chce się kołysać, czy ściskać, "
      "i skorzysta z wybranej formy.",
  S="Wskazuje palcem jeden z dwóch obrazków i idzie do wybranej formy.",
  A="Wybór z dwóch jest odpowiedzią, na którą dziecko stać także wtedy, gdy jest pobudzone.",
  pomoc_wiek="dwa duże obrazki: kołysanie i ściskanie",
  przebieg=[
   ("N — pokazuje dwa obrazki i nazywa oba: „kołysanie”, „ściskanie”.",
    "D — ogląda obrazki i dotyka ich."),
   ("N — pokazuje przy każdym obrazku prawdziwą formę: koc i gniotek.",
    "D — próbuje obu form po kolei."),
   ("N — przy pobudzeniu pokazuje oba obrazki i czeka.",
    "D — wskazuje jeden z obrazków."),
   ("N — daje formę zgodną ze wskazaniem, bez zmieniania wyboru dziecka.",
    "D — korzysta z wybranej formy przez chwilę."),
   ("N — nazywa, co się stało: „chciałeś ściskać i ściskałeś”.",
    "D — odkłada formę i wraca do zabawy.")]),
 ("II.2", "B"): dict(
  podtytul="Wskazanie wrażenia na karcie diety sensorycznej i wybór formy",
  ter="Dziecko wskaże wrażenie na karcie diety sensorycznej samo i wybierze jedną "
      "z dwóch form z tego pola.",
  S="Wskazuje pole na karcie i wybiera formę z tego samego pola.",
  A="Karta ma po dwie propozycje w każdym polu — wybór jest realny, a nie pozorny.",
  pomoc_wiek="karta diety sensorycznej z trzema polami po dwie formy",
  przebieg=[
   ("N — omawia trzy pola karty: ruch, ucisk, cisza.",
    "D — nazywa formy w każdym polu."),
   ("N — prowadzi zajęcia z hałasem albo ruchem, które męczą dziecko.",
    "D — uczestniczy w zajęciach do pierwszych sygnałów przeciążenia."),
   ("N — podsuwa kartę i milczy.",
    "D — wskazuje pole wrażenia, którego potrzebuje."),
   ("N — pokazuje dwie formy z tego pola.",
    "D — wybiera jedną i korzysta z niej."),
   ("N — po powrocie zaznacza z dzieckiem, czy forma pomogła.",
    "D — zaznacza buźkę i wraca do zajęć.")]),
 ("II.2", "C"): dict(
  podtytul="Wybór formy, która nie przeszkadza innym dzieciom",
  ter="Dziecko nazwie potrzebę i wybierze formę, która nie przeszkadza innym dzieciom "
      "w czasie trwających zajęć.",
  S="Nazywa potrzebę słowami i wybiera formę cichą albo wykonywaną przy stoliku.",
  A="Podział form na „przy stoliku” i „poza salą” daje wybór pasujący do sytuacji.",
  pomoc_wiek="karta z podziałem form: przy stoliku · poza salą",
  przebieg=[
   ("N — dzieli z dziećmi formy na te przy stoliku i te poza salą.",
    "D — przyporządkowuje formy do dwóch grup."),
   ("N — pyta, kiedy można skorzystać z której grupy.",
    "D — mówi, że w czasie zajęć wybiera formę przy stoliku."),
   ("N — prowadzi zajęcia grupowe i obserwuje sygnały przeciążenia.",
    "D — nazywa swoją potrzebę słowami w trakcie zajęć."),
   ("N — przypomina o podziale form, nie wskazując konkretnej.",
    "D — wybiera formę przy stoliku i korzysta z niej cicho."),
   ("N — po zajęciach pyta, czy forma wystarczyła.",
    "D — ocenia i mówi, czego potrzebowałoby następnym razem.")]),

 # ——— II.8 · zaplanowana przerwa sensoryczna ———————————————————————————
 ("II.3", "A"): dict(
  podtytul="Wyjście na przerwę sensoryczną po sygnale minutnika",
  ter="Dziecko pójdzie do kącika wyciszenia po sygnale minutnika, prowadzone przez "
      "dorosłego, i zostanie tam przez czas przerwy.",
  S="Wstaje po sygnale i idzie z dorosłym do kącika przerwy.",
  A="Sygnał jest zawsze taki sam — dziecko rozpoznaje go, zanim zrozumie słowa.",
  pomoc_wiek="ten sam dzwonek albo grzechotka jako sygnał przerwy",
  przebieg=[
   ("N — pokazuje minutnik i zapowiada: „gdy zadzwoni, idziemy na przerwę”.",
    "D — ogląda minutnik i miejsce przerwy."),
   ("N — prowadzi zajęcia, minutnik stoi w widocznym miejscu.",
    "D — uczestniczy w zajęciach."),
   ("N — po sygnale wstaje i podaje dziecku rękę.",
    "D — wstaje i idzie do kącika przerwy."),
   ("N — zostaje z dzieckiem i nie rozmawia w czasie przerwy.",
    "D — korzysta z przerwy w ustalonym miejscu."),
   ("N — po przerwie odhacza ją na pasku przy dziecku.",
    "D — odhacza przerwę i wraca do grupy.")]),
 ("II.3", "B"): dict(
  podtytul="Samodzielne skorzystanie z zaplanowanej przerwy po sygnale",
  ter="Dziecko skorzysta z zaplanowanej przerwy sensorycznej po sygnale minutnika, "
      "bez przypominania dorosłego.",
  S="Po sygnale samo wstaje i idzie na przerwę do ustalonego miejsca.",
  A="Miejsce przerwy jest zawsze przygotowane — nie trzeba prosić ani czekać na zgodę.",
  pomoc_wiek="stałe, zawsze gotowe miejsce przerwy w sali",
  przebieg=[
   ("N — na początku dnia pokazuje przerwy zaznaczone na planie dnia.",
    "D — liczy przerwy i mówi, kiedy będzie pierwsza."),
   ("N — nastawia minutnik i wraca do zajęć.",
    "D — pracuje z grupą."),
   ("N — po sygnale nie mówi nic i nie patrzy na dziecko.",
    "D — wstaje samo i idzie na przerwę."),
   ("N — obserwuje z boku, ile trwa przerwa.",
    "D — korzysta z przerwy i wraca po jej zakończeniu."),
   ("N — odhacza przerwę razem z dzieckiem na jego pasku.",
    "D — zaznacza przerwę i włącza się do zajęć.")]),
 ("II.3", "C"): dict(
  podtytul="Planowanie własnych przerw na planie dnia",
  ter="Dziecko zaplanuje przerwy na swoim planie dnia i skorzysta z nich zgodnie "
      "z planem, bez przypominania.",
  S="Zaznacza pory przerw na planie i bierze je w zaplanowanych momentach.",
  A="Plan zrobiony rano przez dziecko jest jego decyzją, nie poleceniem nauczyciela.",
  pomoc_wiek="własny plan dnia dziecka z pustymi polami na przerwy",
  przebieg=[
   ("N — rano pokazuje plan dnia i pyta, gdzie warto wpisać przerwy.",
    "D — zaznacza dwie albo trzy pory przerw na swoim planie."),
   ("N — pyta, po czym pozna, że pora na przerwę.",
    "D — nazywa sygnał: koniec zajęć, hałas, zmęczone ręce."),
   ("N — prowadzi dzień bez przypominania o przerwach.",
    "D — bierze przerwę w zaplanowanym momencie."),
   ("N — notuje, które przerwy zostały wzięte i o której.",
    "D — korzysta z przerw i wraca do zajęć samo."),
   ("N — pod koniec dnia porównuje z dzieckiem plan z tym, co się wydarzyło.",
    "D — ocenia swój plan i poprawia go na jutro.")]),

 # ——— II.9 · zajęcie się czymś w wolnej chwili —————————————————————————
 ("II.4", "A"): dict(
  podtytul="Wybór zabawki z dwóch podanych po skończonym zadaniu",
  ter="Dziecko wybierze zabawkę z dwóch podanych zaraz po skończeniu zadania "
      "i zajmie się nią przy stoliku.",
  S="Wskazuje jedną z dwóch zabawek i bawi się nią przy stoliku.",
  A="Dwie zabawki podane od razu wypełniają moment, który wcześniej był pusty.",
  pomoc_wiek="dwie zabawki przygotowane przed zajęciami, poza wzrokiem dziecka",
  przebieg=[
   ("N — przed zajęciami chowa dwie zabawki pod stolikiem.",
    "D — pracuje nad zadaniem, nie widząc zabawek."),
   ("N — w momencie skończenia zadania wyjmuje obie zabawki.",
    "D — patrzy na obie zabawki."),
   ("N — trzyma je na wysokości wzroku i czeka.",
    "D — wskazuje albo bierze jedną z nich."),
   ("N — odkłada drugą i zostaje przy dziecku.",
    "D — bawi się wybraną zabawką przez dwie minuty."),
   ("N — pokazuje koszyk i kończy zabawę sygnałem.",
    "D — odkłada zabawkę do koszyka.")]),
 ("II.4", "B"): dict(
  podtytul="Wybór zajęcia z listy „gdy skończę wcześniej”",
  ter="Dziecko wybierze zajęcie z listy trzech aktywności „gdy skończę wcześniej” "
      "i zajmie się nim przez pięć minut.",
  S="Wybiera z listy i pracuje przy wybranym zajęciu do sygnału.",
  A="Lista wisi przy stoliku — wybór jest z trzech znanych rzeczy, nie z całej sali.",
  pomoc_wiek="lista trzech aktywności z symbolami, powieszona przy stoliku",
  przebieg=[
   ("N — rano omawia listę trzech aktywności i pokazuje, gdzie leżą materiały.",
    "D — nazywa trzy aktywności z listy."),
   ("N — daje zadanie, które część dzieci skończy wcześniej.",
    "D — kończy zadanie przed resztą grupy."),
   ("N — nie proponuje nic, tylko wskazuje wzrokiem listę.",
    "D — wybiera aktywność z listy i bierze materiały."),
   ("N — nastawia minutnik na pięć minut i wraca do grupy.",
    "D — pracuje przy wybranej aktywności."),
   ("N — po sygnale prosi o odłożenie materiałów.",
    "D — sprząta i wraca do wspólnej części zajęć.")]),
 ("II.4", "C"): dict(
  podtytul="Własna propozycja zajęcia na czas oczekiwania",
  ter="Dziecko zaproponuje własne zajęcie na czas oczekiwania i doprowadzi je "
      "do końca, nie przeszkadzając pracującym dzieciom.",
  S="Nazywa swoje zajęcie, wykonuje je do końca i sprząta po sobie.",
  A="Własna propozycja utrzymuje uwagę dłużej niż zajęcie przydzielone przez dorosłego.",
  pomoc_wiek="zeszyt „moje pomysły na wolny czas” prowadzony przez dziecko",
  przebieg=[
   ("N — pyta rano, co dziecko chciałoby robić, gdy skończy wcześniej.",
    "D — zapisuje albo rysuje swój pomysł w zeszycie."),
   ("N — ustala z dzieckiem, czego ten pomysł wymaga i czy nie zakłóci zajęć.",
    "D — dostosowuje pomysł: ciszej, przy stoliku, bez pomocy dorosłego."),
   ("N — prowadzi zajęcia i nie przypomina o pomyśle.",
    "D — po skończeniu zadania bierze się za swój pomysł."),
   ("N — obserwuje, ile trwa zajęcie i czy dziecko je kończy.",
    "D — doprowadza zajęcie do końca."),
   ("N — pyta, czy pomysł się sprawdził i co zapisze na jutro.",
    "D — ocenia pomysł i zapisuje kolejny.")]),

 # ——— II.10 · zamiana na formę zastępczą ——————————————————————————————
 ("II.5", "A"): dict(
  podtytul="Zakończenie autostymulacji po dłoni nauczyciela i zamiana na zabawkę",
  ter="Dziecko przerwie kręcenie się albo machanie, gdy nauczyciel położy dłoń na jego "
      "dłoni i poda formę zastępczą, i weźmie tę formę.",
  S="Zatrzymuje ruch i bierze podaną formę zastępczą.",
  A="Dotyk i przedmiot działają wtedy, gdy słowa w trakcie autostymulacji nie docierają.",
  pomoc_wiek="forma zastępcza trzymana przez nauczyciela w zasięgu ręki dziecka",
  przebieg=[
   ("N — przygotowuje formę zastępczą dającą to samo wrażenie.",
    "D — zna tę formę z wcześniejszych zajęć."),
   ("N — obserwuje i czeka na początek autostymulacji.",
    "D — zaczyna machać rękami albo kręcić przedmiotem."),
   ("N — podchodzi, kładzie dłoń na dłoni dziecka i nie mówi nic.",
    "D — zatrzymuje ruch."),
   ("N — podaje formę zastępczą do drugiej ręki.",
    "D — bierze formę i korzysta z niej."),
   ("N — zostaje obok przez chwilę i nazywa: „to samo, tylko tak wolno”.",
    "D — korzysta z formy i wraca do zabawy.")]),
 ("II.5", "B"): dict(
  podtytul="Zakończenie autostymulacji w 30 sekund od sygnału",
  ter="Dziecko zakończy autostymulację w ciągu 30 sekund od sygnału wzrokowego "
      "i weźmie formę zastępczą leżącą w zasięgu ręki.",
  S="Po sygnale kończy zachowanie i sięga po formę zastępczą samo.",
  A="Sygnał wzrokowy nie przerywa zajęć grupy i nie zawstydza dziecka przed innymi.",
  pomoc_wiek="karta „stop — zamiana” pokazywana z odległości",
  przebieg=[
   ("N — ustala z dzieckiem sygnał: pokazana karta „stop — zamiana”.",
    "D — powtarza, co robi po zobaczeniu karty."),
   ("N — kładzie formę zastępczą w zasięgu ręki dziecka.",
    "D — sprawdza, gdzie leży forma."),
   ("N — po rozpoczęciu autostymulacji pokazuje kartę z odległości.",
    "D — widzi kartę i kończy zachowanie."),
   ("N — mierzy czas od sygnału do zakończenia.",
    "D — sięga po formę zastępczą w ciągu 30 sekund."),
   ("N — zapisuje czas w rejestrze i nie komentuje przy grupie.",
    "D — korzysta z formy i wraca do zajęć.")]),
 ("II.5", "C"): dict(
  podtytul="Samodzielne zauważenie autostymulacji i zamiana bez sygnału",
  ter="Dziecko zamieni autostymulację na formę zastępczą, gdy samo to zauważy, "
      "albo powie, że trudno mu przestać, i poprosi o pomoc.",
  S="Kończy zachowanie z własnej inicjatywy albo prosi o pomoc w zamianie.",
  A="Nazwanie „robię to znowu” jest umiejętnością do wyćwiczenia, nie kwestią chęci.",
  pomoc_wiek="karta „zauważam u siebie” z trzema sygnałami ciała",
  przebieg=[
   ("N — omawia z dzieckiem, po czym pozna u siebie początek zachowania.",
    "D — nazywa swoje trzy sygnały i zaznacza je na karcie."),
   ("N — prowadzi zajęcia i nie daje sygnału z zewnątrz.",
    "D — pracuje i obserwuje siebie."),
   ("N — obserwuje, czy dziecko zauważa zachowanie samo.",
    "D — zauważa i sięga po formę zastępczą albo prosi o pomoc."),
   ("N — reaguje na prośbę o pomoc bez oceniania.",
    "D — korzysta z formy zastępczej."),
   ("N — po zajęciach pyta, który sygnał był pierwszy.",
    "D — nazywa sygnał i zapisuje go na swojej karcie.")]),
}
