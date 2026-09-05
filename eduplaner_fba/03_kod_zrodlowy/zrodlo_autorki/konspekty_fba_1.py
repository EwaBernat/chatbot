# -*- coding: utf-8 -*-
"""Konspekty do funkcji I — ucieczka / unikanie (wskaźniki I.1–I.5).

Wspólny mianownik wszystkich pięciu: **zadanie nie znika po zachowaniu trudnym.**
Zwolnienie z zadania jest dokładnie tą nagrodą, której ucieczka szuka, więc
konspekt, który tego nie pilnuje, uczy dziecko, że zachowanie działa. Dziecko
dostaje wyjście — przerwę na prośbę — a nie zniknięcie zadania.
"""

RDZEN = {
 "I.1": dict(
  tytul="Jeden krok i już zaczynam",
  icf="d210·d240", pp="2.6·2.11",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["podanie zadania w częściach (rozłożenie na pojemniki)",
          "podpowiedź wzrokowa zamiast ponaglania słownego",
          "wzmocnienie za podjęcie, nie za wynik",
          "wygaszanie ucieczki: zadanie zostaje na stoliku także po zachowaniu trudnym",
          "modelowanie pierwszego ruchu przez nauczyciela"],
  pomoce=["karta „najpierw — potem” z symbolem zadania i symbolem zabawy",
          "karta „przerwa” w zasięgu ręki przez całe zajęcia",
          "zadanie rozłożone na trzy pojemniki, po jednym elemencie w każdym",
          "minutnik piaskowy (1 minuta) — czas widoczny, nie odliczany słowem"],
  wskazowka="Nie zabieraj zadania po zachowaniu trudnym i nie kończ zajęć wcześniej — "
            "to jest dokładnie ta nagroda, której zachowanie szuka. Zadanie zostaje "
            "na stoliku, a dziecko dostaje przerwę na prośbę, nie za krzyk.",
  ter_kryt="Rejestr ABC — kolumna A: podanie trudnego zadania · 5 sytuacji w tygodniu.",
  R="Ucieczka zaczyna się przed pierwszym ruchem; kto zaczął, zwykle kończy.",
  mod=("nauczyciel wykonuje pierwszy ruch razem z dzieckiem, ręka na ręce",
       "karta pierwszego kroku leży na stoliku, nie jest podawana do ręki",
       "dwa zadania po sobie: łatwe i trudne, bez przerwy między nimi"),
  arkusz=dict(
   tytul="Karty do zajęć „Jeden krok i już zaczynam”",
   wstep="Wytnij karty wzdłuż linii. W puste pola wklej symbole z biblioteki EduPlaner — "
         "te same, których dziecko używa na tablicy AAC i w planie dnia. Symbol, który "
         "zmienia wygląd między materiałami, przestaje być dla dziecka słowem.",
   karty=[("Najpierw", "symbol zadania — tego, które dziecko ma wykonać"),
          ("Potem", "symbol zabawy albo aktywności po zadaniu"),
          ("Pierwszy krok", "symbol jednej czynności: weź, włóż, połóż"),
          ("Przerwa", "symbol przerwy — leży przy dziecku przez całe zajęcia")],
   pasek=["1 · biorę", "2 · wkładam", "3 · gotowe"])),

 "I.2": dict(
  tytul="Słyszę, robię, kończę",
  icf="d210·d230", pp="1.6·2.6",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["polecenie krótkie, jedno na raz, z imieniem dziecka na początku",
          "zapowiedź końca („jeszcze dwie rzeczy i koniec”) zamiast otwartego czasu",
          "jedno powtórzenie polecenia, potem czekanie — bez ponaglania",
          "wzmocnienie natychmiast po wykonaniu, nie na koniec zajęć",
          "polecenia łatwe przed trudnym (rozpęd zgodą)"],
  pomoce=["licznik zadań: trzy krążki zdejmowane po każdym poleceniu",
          "karta „ile zostało” — pasek z polami do zakrywania",
          "koszyk z zadaniami wykonanymi — widoczny dowód postępu",
          "karta „przerwa” w zasięgu ręki"],
  wskazowka="Powtórz polecenie raz i przestań mówić. Każde kolejne powtórzenie jest dla "
            "dziecka uwagą, a nie informacją — po czterech powtórzeniach uczy się, że "
            "polecenie zaczyna obowiązywać dopiero przy piątym.",
  ter_kryt="Rejestr poleceń — liczone wykonane po pierwszym powtórzeniu · 10 poleceń w tygodniu.",
  R="Polecenia wracają na każdych zajęciach i u każdego dorosłego — tego nie da się obejść.",
  mod=("polecenie pokazane gestem i obrazkiem, nie tylko powiedziane",
       "licznik zadań widoczny od początku, zdejmowany przez dziecko",
       "seria trzech poleceń zapowiedziana naraz, bez przypominania między nimi"),
  arkusz=dict(
   tytul="Karty do zajęć „Słyszę, robię, kończę”",
   wstep="Wytnij karty i pasek. Krążki z paska zdejmuje dziecko po każdym wykonanym "
         "poleceniu — widzi wtedy, ile zostało, zamiast słyszeć „jeszcze chwilę”. "
         "Symbole wklej z biblioteki EduPlaner.",
   karty=[("Słucham", "symbol słuchania — dorosły mówi, dziecko patrzy"),
          ("Robię", "symbol czynności z polecenia"),
          ("Koniec", "symbol zakończenia — koszyk, ptaszek albo pusty stolik"),
          ("Przerwa", "symbol przerwy na prośbę")],
   pasek=["zostały 3", "zostały 2", "została 1"])),

 "I.3": dict(
  tytul="Przerwa i powrót",
  icf="d230·d240", pp="2.6·9.10",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["przerwa z widocznym końcem (minutnik), nie „aż się uspokoi”",
          "powrót do zadania w wersji skróconej, nie do całości",
          "zadanie zostawione na stoliku w tej samej pozycji",
          "opis zamiast oceny przy powrocie („wróciłeś, zostały dwa”)",
          "wzmocnienie za powrót, osobno od wzmocnienia za wykonanie"],
  pomoce=["minutnik piaskowy albo wizualny (3 minuty)",
          "karta „wracam” — kładziona na stoliku przed wyjściem na przerwę",
          "podkładka z zaznaczonym miejscem zadania, żeby stolik nie „zniknął”",
          "koszyk „do dokończenia” z jedną częścią zadania"],
  wskazowka="Nie sprzątaj zadania w czasie przerwy i nie zaczynaj po niej od nowa. "
            "Dziecko wraca do tego samego, skróconego kawałka — inaczej przerwa staje się "
            "sposobem na skasowanie zadania.",
  ter_kryt="Rejestr ABC — kolumna C: co następuje po przerwie · wszystkie przerwy w tygodniu.",
  R="Powrót przerywa błędne koło: przerwa przestaje być drogą do zniknięcia zadania.",
  mod=("nauczyciel wraca z dzieckiem i siada obok na czas dokończenia",
       "dziecko dostaje do dokończenia połowę tego, co zostało",
       "dziecko samo ustala długość przerwy i pilnuje minutnika"),
  arkusz=dict(
   tytul="Karty do zajęć „Przerwa i powrót”",
   wstep="Wytnij karty. Kartę „wracam” dziecko kładzie na swoim zadaniu, wychodząc "
         "na przerwę — to widoczna umowa, że zadanie na nie czeka. Symbole wklej "
         "z biblioteki EduPlaner.",
   karty=[("Przerwa", "symbol przerwy — miejsce, do którego dziecko idzie"),
          ("Wracam", "symbol powrotu — kładziony na zadaniu"),
          ("Dokończę", "symbol jednej części zadania do dokończenia"),
          ("Gotowe", "symbol zakończenia całości")],
   pasek=["idę na przerwę", "kończy się czas", "wracam do zadania"])),

 "I.4": dict(
  tytul="Dwa łatwe, jedno trudne",
  icf="d210·d220", pp="2.6·2.8",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["rozpęd zgodą: dwa zadania pewne przed jednym trudnym",
          "stopniowanie trudności w obrębie jednej serii",
          "nazywanie błędu jako etapu, nie jako porażki",
          "wzmocnienie za podjęcie trudnego, niezależnie od wyniku",
          "wybór dziecka między dwoma zadaniami o zbliżonej trudności"],
  pomoce=["trzy koperty oznaczone kolejnością serii",
          "karta „trudne — poradzę sobie” z miejscem na znak dziecka",
          "zestaw zadań łatwych, sprawdzonych, wykonywanych bez pomocy",
          "tabliczka z paskiem postępu serii"],
  wskazowka="Zadanie trudne w serii ma być naprawdę trudniejsze, nie dłuższe. Wydłużanie "
            "łatwego zadania dziecko rozpozna od razu i seria straci sens — trudność ma "
            "dotyczyć czynności, nie liczby powtórzeń.",
  ter_kryt="Karta serii zadań — zaznaczone podjęcie trzeciego · 5 serii w tygodniu.",
  R="Dwa sukcesy z rzędu budują gotowość na trudność — tego nie da się zastąpić zachętą.",
  mod=("nauczyciel wykonuje trudne zadanie razem z dzieckiem, krok po kroku",
       "dziecko widzi wszystkie trzy koperty od początku i wie, co będzie",
       "dziecko samo układa kolejność serii i uzasadnia wybór"),
  arkusz=dict(
   tytul="Karty do zajęć „Dwa łatwe, jedno trudne”",
   wstep="Wytnij karty i pasek serii. Na kartach zadań wklej symbole konkretnych "
         "czynności z biblioteki EduPlaner — dziecko ma widzieć, co go czeka, zanim "
         "usiądzie do stolika.",
   karty=[("Zadanie 1 · łatwe", "symbol czynności, którą dziecko umie na pewno"),
          ("Zadanie 2 · łatwe", "symbol drugiej czynności pewnej"),
          ("Zadanie 3 · trudne", "symbol czynności o stopień trudniejszej"),
          ("Poradzę sobie", "miejsce na znak dziecka po podjęciu trudnego zadania")],
   pasek=["1 · łatwe", "2 · łatwe", "3 · trudne"])),

 "I.5": dict(
  tytul="Karta przerwy zamiast ucieczki",
  icf="d335·d240", pp="2.10·2.11",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["nauka komunikacji funkcjonalnej: prośba zamiast zachowania",
          "reakcja natychmiastowa na prośbę — przerwa zawsze, gdy dziecko poprosi",
          "podpowiedź wyprzedzająca przy pierwszych sygnałach oporu",
          "wygaszanie: przerwa nie następuje po zachowaniu trudnym",
          "stopniowe wydłużanie pracy przed przerwą"],
  pomoce=["karta „przerwa” — jedna, zawsze w tym samym miejscu stolika",
          "wykaz trzech rzeczy, które wolno robić w czasie przerwy",
          "minutnik przerwy (3 minuty)",
          "karta „wracam” do położenia na zadaniu"],
  wskazowka="Na początku daj przerwę zawsze i natychmiast, nawet dziesięć razy na zajęciach. "
            "Prośba musi być szybsza i pewniejsza od krzyku, inaczej dziecko zostanie przy "
            "krzyku — dopiero potem wydłuża się pracę przed przerwą.",
  ter_kryt="Rejestr ABC — czy przed zachowaniem pojawiła się prośba · wszystkie sytuacje oporu.",
  R="Prośba o przerwę pełni tę samą funkcję co ucieczka, tylko jest akceptowalna.",
  mod=("nauczyciel podaje kartę do ręki przy pierwszych sygnałach zmęczenia",
       "karta leży na stoliku, dziecko sięga po nią samo",
       "dziecko prosi słowami i ustala z nauczycielem długość przerwy"),
  arkusz=dict(
   tytul="Karty do zajęć „Karta przerwy zamiast ucieczki”",
   wstep="Wytnij karty. Karta „przerwa” ma być jedna i ma leżeć zawsze w tym samym "
         "miejscu — dziecko musi wiedzieć, gdzie jej szukać, zanim zrobi się trudno. "
         "Symbole wklej z biblioteki EduPlaner.",
   karty=[("Przerwa", "symbol przerwy — karta główna, zawsze na stoliku"),
          ("Chcę odpocząć", "symbol odpoczynku: koc, poduszka, kącik"),
          ("Chcę się poruszać", "symbol ruchu: skakanie, chodzenie, huśtawka"),
          ("Wracam", "symbol powrotu do zadania")],
   pasek=["proszę o przerwę", "odpoczywam", "wracam"])),
}

WARIANTY = {
 # ——— I.1 · rozpoczęcie zadania ———————————————————————————————————————
 ("I.1", "A"): dict(
  podtytul="Rozpoczynanie trudnego zadania z kartą pierwszego kroku",
  ter="Dziecko weźmie do ręki pierwszy element trudnego zadania w ciągu minuty od podania "
      "karty pierwszego kroku, bez odchodzenia od stolika.",
  S="Bierze pierwszy element i kładzie go przed sobą — to widać, nie trzeba oceniać chęci.",
  A="Karta pokazuje jedną czynność, nie całe zadanie — dziecko nie musi ogarniać całości.",
  pomoc_wiek="karta „pierwszy krok” z jednym symbolem czynności (arkusz poniżej)",
  przebieg=[
   ("N — kładzie przed dzieckiem kartę „najpierw — potem” i nazywa oba symbole.",
    "D — patrzy na kartę i wskazuje symbol zabawy, która będzie potem."),
   ("N — stawia trzy pojemniki i odsuwa dwa, zostawiając pierwszy.",
    "D — widzi jedną czynność zamiast całego zadania."),
   ("N — podaje kartę „pierwszy krok” i odwraca minutnik.",
    "D — bierze pierwszy element do ręki w czasie minutnika."),
   ("N — nazywa to, co dziecko zrobiło: „zacząłeś”, i przysuwa drugi pojemnik.",
    "D — sięga po kolejny element bez nowego polecenia."),
   ("N — po ostatnim pojemniku pokazuje symbol zabawy z karty „potem”.",
    "D — kończy zadanie i przechodzi do zabawy, którą wcześniej wskazało.")]),
 ("I.1", "B"): dict(
  podtytul="Rozpoczynanie trudnego zadania po wskazaniu pierwszego kroku",
  ter="Dziecko rozpocznie trudne zadanie w ciągu minuty od polecenia i wykona dwa pierwsze "
      "kroki bez dodatkowej podpowiedzi.",
  S="Siada, bierze przybory i wykonuje dwa pierwsze kroki zadania.",
  A="Karta z rozpisanym zadaniem zdejmuje z dziecka decyzję, od czego zacząć.",
  pomoc_wiek="karta zadania rozpisana na trzy kroki, każdy w osobnym polu",
  przebieg=[
   ("N — pokazuje kartę zadania rozpisaną na trzy kroki i nazywa pierwszy.",
    "D — wskazuje palcem krok, od którego zaczyna."),
   ("N — kładzie przybory przy pierwszym kroku i odsuwa resztę.",
    "D — bierze przybory i zaczyna pierwszy krok."),
   ("N — milczy przez minutę, obserwuje, nie ponagla.",
    "D — pracuje samodzielnie nad pierwszym krokiem."),
   ("N — przysuwa materiał do drugiego kroku i odhacza pierwszy na karcie.",
    "D — przechodzi do drugiego kroku bez nowego polecenia."),
   ("N — pyta, co zostało do zrobienia, i pokazuje kartę.",
    "D — nazywa ostatni krok i podejmuje go albo prosi o pomoc.")]),
 ("I.1", "C"): dict(
  podtytul="Rozpoczynanie trudnego zadania od kroku wybranego przez dziecko",
  ter="Dziecko rozpocznie trudne zadanie w ciągu minuty, powie, co robi jako pierwsze, "
      "i doprowadzi zadanie do końca, prosząc o pomoc zamiast przerywać.",
  S="Nazywa pierwszy krok, wykonuje go i kończy zadanie albo prosi o pomoc.",
  A="Wybór między dwoma krokami daje dziecku sprawczość przy zadaniu, którego nie wybrało.",
  pomoc_wiek="dwie karty kroków do wyboru, obie prowadzące do tego samego celu",
  przebieg=[
   ("N — pokazuje zadanie w całości i dwie karty: dwa możliwe pierwsze kroki.",
    "D — wybiera jedną kartę i mówi, od czego zaczyna."),
   ("N — zapisuje wybór dziecka na tablicy albo kartce.",
    "D — widzi swój wybór zapisany i zaczyna pracę."),
   ("N — odchodzi na dwie minuty do innego dziecka.",
    "D — pracuje samodzielnie, bez dorosłego przy stoliku."),
   ("N — wraca i pyta: „co idzie dobrze, a gdzie potrzebujesz pomocy?”.",
    "D — nazywa trudność i prosi o konkretną pomoc zamiast przerywać."),
   ("N — po skończeniu pyta, czy wybrany krok był dobrym początkiem.",
    "D — ocenia swój wybór i mówi, jak zrobiłoby to następnym razem.")]),

 # ——— I.2 · wykonanie polecenia ————————————————————————————————————————
 ("I.2", "A"): dict(
  podtytul="Wykonanie polecenia pokazanego gestem i obrazkiem",
  ter="Dziecko wykona polecenie pokazane gestem i obrazkiem, przy dorosłym siedzącym obok, "
      "bez odchodzenia od stolika.",
  S="Wykonuje pokazaną czynność: podaje, wkłada albo odkłada wskazany przedmiot.",
  A="Gest i obrazek niosą polecenie wtedy, gdy same słowa jeszcze nie docierają.",
  pomoc_wiek="obrazkowe karty trzech poleceń: podaj, włóż, odłóż",
  przebieg=[
   ("N — mówi imię dziecka i czeka na kontakt wzrokowy.",
    "D — patrzy na nauczyciela."),
   ("N — pokazuje obrazek polecenia i wykonuje gest.",
    "D — patrzy na obrazek i na przedmiot, którego dotyczy."),
   ("N — czeka pięć sekund, nie powtarzając polecenia.",
    "D — wykonuje czynność albo sięga po przedmiot."),
   ("N — powtarza polecenie raz, jeśli nie było reakcji, i pomaga zacząć.",
    "D — wykonuje czynność z pomocą nauczyciela."),
   ("N — zdejmuje jeden krążek z licznika i nazywa, ile zostało.",
    "D — patrzy na licznik i bierze się za kolejne polecenie.")]),
 ("I.2", "B"): dict(
  podtytul="Wykonanie polecenia po jednym powtórzeniu, bez odchodzenia od stolika",
  ter="Dziecko wykona polecenie po jednym powtórzeniu i zapowiedzi „jeszcze dwie rzeczy "
      "i koniec”, bez odmowy i odchodzenia od stolika.",
  S="Zostaje przy stoliku i wykonuje polecenie po pierwszym powtórzeniu.",
  A="Zapowiedź liczby zadań zamienia otwarty czas w policzalny — widać koniec.",
  pomoc_wiek="licznik z trzema krążkami zdejmowanymi przez dziecko",
  przebieg=[
   ("N — zapowiada: „mamy trzy rzeczy do zrobienia i koniec”, kładzie licznik.",
    "D — liczy krążki i wie, ile zadań przed nim."),
   ("N — podaje pierwsze polecenie, krótkie, jedno zdanie.",
    "D — wykonuje polecenie i zdejmuje krążek."),
   ("N — podaje drugie polecenie i milczy przez pięć sekund.",
    "D — zaczyna wykonywać bez ponaglania."),
   ("N — powtarza polecenie raz, jeśli trzeba, i nie dodaje nic więcej.",
    "D — wykonuje polecenie po pierwszym powtórzeniu."),
   ("N — po ostatnim krążku nazywa, co dziecko zrobiło, i kończy zajęcia.",
    "D — odkłada licznik i przechodzi do wybranej zabawy.")]),
 ("I.2", "C"): dict(
  podtytul="Wykonanie serii poleceń zapowiedzianych naraz",
  ter="Dziecko wykona serię trzech poleceń zapowiedzianych naraz, bez przypominania "
      "między nimi, i powie na końcu, co zrobiło.",
  S="Wykonuje trzy polecenia po kolei, samo pilnując, które zostało.",
  A="Zapisany plan trzech poleceń zastępuje przypominanie przez dorosłego.",
  pomoc_wiek="kartka z trzema poleceniami do odhaczania przez dziecko",
  przebieg=[
   ("N — podaje trzy polecenia naraz i zapisuje je na kartce przy dziecku.",
    "D — powtarza je własnymi słowami."),
   ("N — odsuwa się i nie przypomina o kolejnych zadaniach.",
    "D — wykonuje pierwsze polecenie i odhacza je na kartce."),
   ("N — obserwuje, notuje, w którym miejscu pojawia się trudność.",
    "D — przechodzi do drugiego polecenia bez przypomnienia."),
   ("N — reaguje tylko wtedy, gdy dziecko prosi o pomoc.",
    "D — prosi o pomoc albo kończy trzecie polecenie samodzielnie."),
   ("N — pyta, które polecenie było najtrudniejsze i dlaczego.",
    "D — nazywa trudność i proponuje, co ułatwiłoby ją następnym razem.")]),

 # ——— I.3 · powrót do zadania po przerwie ——————————————————————————————
 ("I.3", "A"): dict(
  podtytul="Powrót do stolika po przerwie z sygnałem dźwiękowym",
  ter="Dziecko wróci do stolika po przerwie na sygnał dźwiękowy i dokończy jeden element "
      "zadania zaczętego przed przerwą.",
  S="Wraca do stolika i wkłada jeden element na miejsce.",
  A="Sygnał dźwiękowy kończy przerwę bez negocjacji — koniec nie zależy od dorosłego.",
  pomoc_wiek="dzwonek albo grzechotka jako stały sygnał końca przerwy",
  przebieg=[
   ("N — pokazuje kartę „przerwa” i kładzie na zadaniu kartę „wracam”.",
    "D — idzie do kącika przerwy."),
   ("N — odwraca minutnik trzyminutowy i zostawia go w widocznym miejscu.",
    "D — odpoczywa, widząc, ile czasu zostało."),
   ("N — daje sygnał dźwiękowy, ten sam co zawsze.",
    "D — wstaje i wraca do stolika."),
   ("N — pokazuje jeden element do dokończenia, resztę odsuwa.",
    "D — dokańcza ten jeden element."),
   ("N — nazywa powrót: „wróciłeś i skończyłeś”, i kończy zajęcia.",
    "D — odkłada materiał i wybiera zabawę.")]),
 ("I.3", "B"): dict(
  podtytul="Powrót po trzyminutowej przerwie i dokończenie ustalonej części",
  ter="Dziecko wróci do zadania po trzyminutowej przerwie i dokończy połowę tego, "
      "co zostało przed przerwą.",
  S="Wraca do stolika w czasie minuty od sygnału i pracuje nad ustaloną częścią.",
  A="Ustalona z góry część jest wykonalna po wzburzeniu — całość nie byłaby.",
  pomoc_wiek="podkładka z zaznaczoną częścią „do dokończenia po przerwie”",
  przebieg=[
   ("N — przed przerwą zaznacza na podkładce, co dziecko dokończy po powrocie.",
    "D — widzi zaznaczoną część i idzie na przerwę."),
   ("N — nastawia minutnik i nie komentuje zachowania z przed przerwy.",
    "D — korzysta z przerwy w ustalonym miejscu."),
   ("N — po sygnale czeka przy stoliku, nie idzie po dziecko.",
    "D — wraca samo do stolika."),
   ("N — pokazuje zaznaczoną część i milczy.",
    "D — dokańcza zaznaczoną część zadania."),
   ("N — odhacza zrobione i pyta, co zostaje na następny raz.",
    "D — nazywa, co zostało, i odkłada materiał na miejsce.")]),
 ("I.3", "C"): dict(
  podtytul="Powrót do zadania i nazwanie tego, co zostało",
  ter="Dziecko samo zdecyduje o końcu przerwy w umówionym czasie, wróci do zadania "
      "i powie, co zostało do zrobienia.",
  S="Kończy przerwę bez wołania i nazywa pozostałą część zadania.",
  A="Umowa o długości przerwy przed jej rozpoczęciem zamienia wyjście w plan, nie w ucieczkę.",
  pomoc_wiek="minutnik ustawiany przez dziecko i karta umowy o czasie przerwy",
  przebieg=[
   ("N — pyta, ile minut przerwy dziecko potrzebuje, i zapisuje umowę.",
    "D — podaje czas i ustawia minutnik."),
   ("N — nie przerywa przerwy, nawet gdy dziecko wygląda na gotowe.",
    "D — korzysta z całej przerwy albo wraca wcześniej."),
   ("N — czeka przy stoliku po sygnale minutnika.",
    "D — wraca do zadania w umówionym czasie."),
   ("N — pyta: „co zostało do zrobienia?”.",
    "D — nazywa pozostałą część i zaczyna od niej."),
   ("N — po skończeniu pyta, czy umówiony czas przerwy wystarczył.",
    "D — ocenia swój wybór i proponuje czas na następny raz.")]),

 # ——— I.4 · podjęcie trudniejszego zadania —————————————————————————————
 ("I.4", "A"): dict(
  podtytul="Podjęcie trudniejszego zadania po dwóch łatwych, z pomocą dorosłego",
  ter="Dziecko podejmie trudniejsze zadanie ułożone po dwóch łatwych, z pomocą dorosłego "
      "przy pierwszym ruchu.",
  S="Bierze materiał trzeciego zadania i wykonuje pierwszy ruch.",
  A="Dwa zadania pewne z rzędu budują gotowość, której samo zachęcanie nie daje.",
  pomoc_wiek="trzy tacki ustawione w kolejności, od lewej do prawej",
  przebieg=[
   ("N — ustawia trzy tacki w rzędzie i pokazuje, że zaczynamy od lewej.",
    "D — bierze materiał z pierwszej tacki."),
   ("N — nie pomaga przy zadaniach łatwych, tylko nazywa sukces.",
    "D — wykonuje dwa łatwe zadania samodzielnie."),
   ("N — przysuwa trzecią tackę i wykonuje pierwszy ruch razem z dzieckiem.",
    "D — podejmuje trudniejsze zadanie ręką prowadzoną przez nauczyciela."),
   ("N — cofa pomoc przy kolejnym ruchu i czeka.",
    "D — próbuje samodzielnie kolejnego ruchu."),
   ("N — kończy niezależnie od wyniku i nazywa podjęcie: „spróbowałeś trudnego”.",
    "D — odkłada materiał i przechodzi do zabawy.")]),
 ("I.4", "B"): dict(
  podtytul="Seria „dwa łatwe, jedno trudne” z prośbą o pomoc",
  ter="Dziecko wykona serię „dwa łatwe, jedno trudne”, prosząc o pomoc przy trudnym "
      "zamiast przerywać serię.",
  S="Kończy dwa łatwe zadania i podejmuje trudne, prosząc o pomoc, gdy jej potrzebuje.",
  A="Koperty z numerami pokazują, że po trudnym zadaniu seria się kończy — trudność ma koniec.",
  pomoc_wiek="trzy koperty z numerami serii i karta „poproszę o pomoc”",
  przebieg=[
   ("N — pokazuje trzy koperty i mówi, że trzecia jest trudniejsza.",
    "D — otwiera pierwszą kopertę."),
   ("N — obserwuje bez komentarza przy dwóch łatwych zadaniach.",
    "D — wykonuje dwa łatwe zadania i odkłada koperty."),
   ("N — kładzie kartę „poproszę o pomoc” przy trzeciej kopercie.",
    "D — otwiera trzecią kopertę i zaczyna trudne zadanie."),
   ("N — reaguje wyłącznie na prośbę dziecka, nie uprzedza jej.",
    "D — prosi o pomoc kartą albo słowami zamiast przerywać."),
   ("N — nazywa, co było trudne, i zaznacza serię jako zakończoną.",
    "D — mówi, która część była najtrudniejsza.")]),
 ("I.4", "C"): dict(
  podtytul="Planowanie własnej serii z zadaniem trudnym w środku",
  ter="Dziecko zaplanuje kolejność zadań tak, by trudne wypadło w środku serii, "
      "i wykona ułożony przez siebie plan.",
  S="Układa kolejność trzech zadań, uzasadnia ją i realizuje bez zmiany w trakcie.",
  A="Własny plan sprawia, że trudne zadanie jest wyborem dziecka, a nie decyzją dorosłego.",
  pomoc_wiek="paski z nazwami zadań do ułożenia w wybranej kolejności",
  przebieg=[
   ("N — rozkłada paski trzech zadań i mówi, które jest trudniejsze.",
    "D — układa paski w wybranej przez siebie kolejności."),
   ("N — pyta, dlaczego taka kolejność.",
    "D — uzasadnia wybór: „trudne w środku, bo…”."),
   ("N — odsuwa się i pozwala pracować bez podpowiedzi.",
    "D — wykonuje zadania w ustalonej kolejności."),
   ("N — nie pozwala zmienić kolejności w trakcie, przypomina o planie.",
    "D — trzyma się własnego planu także przy trudnym zadaniu."),
   ("N — pyta, czy plan się sprawdził i co zmieniłoby następnym razem.",
    "D — ocenia swój plan i proponuje inną kolejność albo tę samą.")]),

 # ——— I.5 · prośba o przerwę ————————————————————————————————————————
 ("I.5", "A"): dict(
  podtytul="Podanie karty „przerwa” zamiast odejścia od stolika",
  ter="Dziecko poda nauczycielowi kartę „przerwa”, gdy zrobi się trudno, zamiast odejść "
      "od stolika bez słowa.",
  S="Bierze kartę „przerwa” i podaje ją dorosłemu.",
  A="Karta działa bez mówienia — dziecko dostaje sposób, który już umie.",
  pomoc_wiek="jedna karta „przerwa” podawana do ręki przy pierwszych sygnałach oporu",
  przebieg=[
   ("N — kładzie kartę „przerwa” na stoliku i nazywa ją.",
    "D — dotyka karty i patrzy na kącik przerwy."),
   ("N — daje zadanie o znanej dziecku trudności.",
    "D — pracuje do pierwszych oznak zmęczenia."),
   ("N — przy pierwszym sygnale oporu podaje kartę do ręki dziecka.",
    "D — trzyma kartę i podaje ją nauczycielowi."),
   ("N — natychmiast daje przerwę i nazywa: „poprosiłeś, masz przerwę”.",
    "D — idzie na przerwę do ustalonego miejsca."),
   ("N — po przerwie wraca do zadania w skróconej wersji.",
    "D — wraca do stolika i kończy skrócone zadanie.")]),
 ("I.5", "B"): dict(
  podtytul="Samodzielne pokazanie karty przed przerwaniem zadania",
  ter="Dziecko pokaże kartę „przerwa” samo, zanim przerwie zadanie krzykiem albo "
      "odejściem od stolika.",
  S="Sięga po kartę leżącą na stoliku i pokazuje ją, zanim pojawi się zachowanie trudne.",
  A="Karta leży w tym samym miejscu przez całe zajęcia — dziecko nie musi jej szukać.",
  pomoc_wiek="karta „przerwa” w stałym rogu stolika, w zasięgu ręki dziecka",
  przebieg=[
   ("N — pokazuje, gdzie leży karta, i przypomina, że przerwa jest zawsze na prośbę.",
    "D — sprawdza, gdzie leży karta."),
   ("N — daje zadanie trudniejsze niż zwykle, o jeden stopień.",
    "D — pracuje i obserwuje własne zmęczenie."),
   ("N — nie uprzedza prośby, obserwuje i czeka.",
    "D — sięga po kartę i pokazuje ją, zanim przerwie zadanie."),
   ("N — daje przerwę od razu i nastawia minutnik.",
    "D — korzysta z przerwy i wraca po sygnale."),
   ("N — nazywa różnicę: „poprosiłeś, nie musiałeś krzyczeć”.",
    "D — kończy zadanie w wersji ustalonej przed przerwą.")]),
 ("I.5", "C"): dict(
  podtytul="Prośba o przerwę słowami i umowa o jej długości",
  ter="Dziecko poprosi o przerwę słowami, ustali z nauczycielem jej długość i wróci "
      "do zadania w umówionym czasie.",
  S="Mówi, że potrzebuje przerwy, podaje czas i dotrzymuje umowy.",
  A="Umowa o czasie zamienia przerwę w narzędzie dziecka, nie w decyzję dorosłego.",
  pomoc_wiek="karta umowy: „proszę o … minut przerwy” z miejscem na liczbę",
  przebieg=[
   ("N — przypomina, że przerwę można dostać na prośbę, i pokazuje kartę umowy.",
    "D — czyta kartę i wie, o co może poprosić."),
   ("N — daje zadanie wymagające wysiłku przez kilkanaście minut.",
    "D — pracuje i śledzi własne zmęczenie."),
   ("N — czeka na prośbę, nie proponuje przerwy sam.",
    "D — prosi słowami o przerwę i podaje jej długość."),
   ("N — zapisuje umowę i nastawia minutnik na podany czas.",
    "D — korzysta z przerwy i wraca w umówionym momencie."),
   ("N — pyta, czy ten czas wystarczył i kiedy najlepiej prosić o przerwę.",
    "D — ocenia swoją decyzję i planuje następną przerwę.")]),
}
