# -*- coding: utf-8 -*-
"""Konspekty do funkcji IV — dostęp do przedmiotu / aktywności (wskaźniki IV.1–IV.5).

Wspólny mianownik: **przedmiot nie pojawia się po zachowaniu trudnym.** Wydany
raz „dla świętego spokoju” uczy dokładnie tego, co próbujemy zmienić. Dziecko
dostaje szybszą drogę — prośbę — i uczy się czekać na to, czego nie może dostać
od razu; odmowa zostaje odmową, ale zawsze z alternatywą.
"""

RDZEN = {
 "IV.1": dict(
  tytul="Nie teraz — a co zamiast",
  icf="d240·d720", pp="1.4·2.10",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["odmowa zawsze z dwiema alternatywami",
          "krótkie uzasadnienie odmowy, jedno zdanie, raz",
          "nazwanie emocji dziecka przy odmowie",
          "brak negocjacji po zachowaniu trudnym",
          "wzmocnienie za przyjęcie odmowy, nie tylko za spokój"],
  pomoce=["dwie karty alternatyw pokazywane razem z odmową",
          "karta „nie teraz” z symbolem pory, kiedy będzie można",
          "kącik z aktywnościami zawsze dostępnymi bez pytania",
          "buźki do nazwania emocji po odmowie"],
  wskazowka="Odmowa ma być jedna i krótka. Tłumaczenie powtórzone trzeci raz dziecko czyta "
            "jako wahanie i wraca do naciskania — bo czasem to działa. Zamiast tłumaczyć "
            "dłużej, pokaż dwie rzeczy, które można zrobić teraz.",
  ter_kryt="Rejestr ABC — kolumna A: odmowa dorosłego · wszystkie odmowy w tygodniu.",
  R="Odmowa jest nieusuwalną częścią dnia w grupie — dziecko potrzebuje na nią sposobu.",
  mod=("nauczyciel podaje dwie alternatywy do rąk i zostaje przy dziecku",
       "dziecko wybiera z dwóch propozycji samo i zajmuje się wybraną",
       "dziecko pyta, kiedy będzie mogło dostać to, o co prosiło"),
  arkusz=dict(
   tytul="Karty do zajęć „Nie teraz — a co zamiast”",
   wstep="Wytnij karty. Karty alternatyw pokazuj razem z odmową, nie po niej — dziecko "
         "ma zobaczyć wyjście w tej samej chwili, w której słyszy „nie”. Symbole wklej "
         "z biblioteki EduPlaner.",
   karty=[("Nie teraz", "symbol odmowy z miejscem na porę, kiedy będzie można"),
          ("Mogę to", "symbol pierwszej alternatywy"),
          ("Albo to", "symbol drugiej alternatywy"),
          ("Jak się czuję", "buźki: złość, smutek, spokój")],
   pasek=["słyszę „nie”", "wybieram", "robię"])),

 "IV.2": dict(
  tytul="Jeszcze dwie minuty i oddaję",
  icf="d230·d720", pp="1.3·2.10",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["zapowiedź końca zabawy zamiast zabierania przedmiotu",
          "sygnał niezależny od dorosłego: minutnik",
          "stałe miejsce odkładania przedmiotu",
          "ta sama procedura u wszystkich dorosłych w sali",
          "wzmocnienie za oddanie, nie za samo zakończenie zabawy"],
  pomoce=["minutnik wizualny stawiany przy dziecku",
          "karta „jeszcze dwie minuty” z symbolem czasu",
          "półka albo pudełko z zaznaczonym miejscem przedmiotu",
          "karta „wróci jutro” z symbolem następnego dnia"],
  wskazowka="Nie zabieraj przedmiotu z ręki. Zabranie zamienia zakończenie w stratę i uczy "
            "dziecko pilnować przedmiotu przed dorosłym. Zapowiedź plus sygnał robi z tego "
            "koniec zabawy, a nie odebranie.",
  ter_kryt="Rejestr ABC — zapowiedź, sygnał, reakcja · wszystkie zakończenia aktywności.",
  R="Zabieranie bez uprzedzenia było wyzwalaczem — usunięcie go zmienia poprzednik, nie dziecko.",
  mod=("nauczyciel podstawia dłoń albo pudełko i czeka na oddanie",
       "dziecko odkłada przedmiot na wyznaczone miejsce po sygnale",
       "dziecko samo ustawia minutnik na koniec zabawy"),
  arkusz=dict(
   tytul="Karty do zajęć „Jeszcze dwie minuty i oddaję”",
   wstep="Wytnij karty i pasek. Kartę „jeszcze dwie minuty” pokazuj razem z nastawieniem "
         "minutnika — to samo dziecko widzi i słyszy. Symbole wklej z biblioteki EduPlaner.",
   karty=[("Jeszcze dwie minuty", "symbol minutnika z zapowiedzią końca"),
          ("Koniec", "symbol sygnału końca zabawy"),
          ("Tu odkładam", "symbol miejsca, na które wraca przedmiot"),
          ("Wróci jutro", "symbol następnego dnia")],
   pasek=["gram", "zapowiedź", "odkładam"])),

 "IV.3": dict(
  tytul="Poproszę o to",
  icf="d335·d710", pp="1.5·3.1",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["nauka komunikacji funkcjonalnej: prośba zamiast zabierania",
          "reakcja szybka na prośbę, brak reakcji na wyrywanie",
          "ten sam zwrot u wszystkich dorosłych",
          "modelowanie prośby przez dorosłego i przez inne dzieci",
          "prośba ćwiczona najpierw o rzeczy łatwe do wydania"],
  pomoce=["karty przedmiotów najczęściej pożądanych przez dziecko",
          "karta zwrotu „poproszę o…” z miejscem na symbol",
          "koszyk wymiany: przedmiot za kartę",
          "żetony za prośbę zamiast zabrania"],
  wskazowka="Na początku wydawaj przedmiot po każdej prośbie, nawet dziesiątej. Prośba musi "
            "być pewniejsza niż wyrwanie — dopiero gdy działa, można zacząć uczyć czekania "
            "i przyjmowania odmowy.",
  ter_kryt="Rejestr ABC — którą drogą dziecko uzyskało przedmiot · wszystkie sytuacje.",
  R="Prośba pełni tę samą funkcję co wyrwanie i przynosi to samo, tylko szybciej.",
  mod=("nauczyciel podaje kartę przedmiotu do ręki i modeluje gest podania",
       "dziecko pokazuje kartę albo mówi „proszę” samo",
       "dziecko prosi pełnym zwrotem i przyjmuje także odpowiedź odmowną"),
  arkusz=dict(
   tytul="Karty do zajęć „Poproszę o to”",
   wstep="Wytnij karty przedmiotów. Wklej symbole rzeczy, o które dziecko naprawdę "
         "najczęściej się dopomina — karta z przedmiotem nieużywanym nie zostanie użyta "
         "w momencie, w którym jest potrzebna.",
   karty=[("Poproszę o…", "karta zwrotu z pustym polem na symbol przedmiotu"),
          ("Przedmiot 1", "symbol rzeczy najczęściej pożądanej"),
          ("Przedmiot 2", "symbol drugiej rzeczy"),
          ("Dziękuję", "symbol podziękowania po otrzymaniu")],
   pasek=["proszę", "czekam", "dostaję"])),

 "IV.4": dict(
  tytul="Czekam z licznikiem",
  icf="d240·b152", pp="2.10·2.6",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["odraczanie gratyfikacji z widocznym końcem",
          "czekanie wypełnione zajęciem, nie puste",
          "stopniowe wydłużanie czasu odroczenia",
          "dotrzymywanie terminu co do sekundy",
          "wzmocnienie za doczekanie, osobno od samego przedmiotu"],
  pomoce=["wizualny licznik czasu (klepsydra albo timer)",
          "karta „dostanę o…” z symbolem pory",
          "pudełko z zadaniem na czas czekania",
          "karta zapisu udanych czekań"],
  wskazowka="Dotrzymuj terminu co do minuty, także wtedy, gdy dziecko czeka spokojnie "
            "i wygląda, jakby zapomniało. Jedno przesunięcie terminu kosztuje więcej niż "
            "dziesięć udanych czekań.",
  ter_kryt="Karta odroczeń — czas czekania i wynik · 5 odroczeń w tygodniu.",
  R="Czekanie jest warunkiem funkcjonowania w grupie, w której jest jedna huśtawka i dwadzieścia dzieci.",
  mod=("nauczyciel czeka razem z dzieckiem i odlicza z nim czas",
       "dziecko czeka z licznikiem, zajmując się czymś innym",
       "dziecko czeka bez licznika, do umówionej pory dnia"),
  arkusz=dict(
   tytul="Karty do zajęć „Czekam z licznikiem”",
   wstep="Wytnij karty i pasek czekania. Na karcie „dostanę o…” zaznacz porę razem "
         "z dzieckiem — zapisany termin jest umową, a nie obietnicą. Symbole wklej "
         "z biblioteki EduPlaner.",
   karty=[("Chcę to", "symbol przedmiotu, na który dziecko czeka"),
          ("Dostanę o…", "symbol pory dnia z miejscem na zaznaczenie"),
          ("W tym czasie", "symbol zajęcia na czas czekania"),
          ("Doczekałem", "pole na znak po udanym czekaniu")],
   pasek=["proszę", "czekam", "dostaję"])),

 "IV.5": dict(
  tytul="Co robię, zanim się zacznie",
  icf="d210·d230", pp="2.1·2.6",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["zadanie „w międzyczasie” przygotowane przed oczekiwaniem",
          "żeton za wypełnione oczekiwanie",
          "widoczna informacja, ile czasu zostało",
          "wybór zajęcia przez dziecko spośród przygotowanych",
          "wzmocnienie natychmiast po zakończeniu oczekiwania"],
  pomoce=["pudełko „w międzyczasie” z trzema krótkimi zadaniami",
          "karta z symbolem atrakcji, na którą dziecko czeka",
          "pasek czasu pokazujący, ile zostało do startu",
          "tabliczka żetonowa"],
  wskazowka="Oczekiwanie na coś atrakcyjnego jest trudniejsze niż zwykła nuda — bodziec "
            "jest już w zasięgu wzroku. Zadanie „w międzyczasie” musi być krótkie i pewne, "
            "inaczej samo stanie się kolejnym źródłem frustracji.",
  ter_kryt="Karta żetonowa — żeton za czynność w międzyczasie · wszystkie sytuacje oczekiwania.",
  R="Oczekiwanie na atrakcję wraca przy każdym wyjściu, wycieczce i podziale na grupy.",
  mod=("nauczyciel podaje zadanie do ręki i zostaje z dzieckiem",
       "dziecko bierze zadanie z pudełka samo i wykonuje je do sygnału",
       "dziecko planuje, czym zajmie się w czasie czekania, i realizuje plan"),
  arkusz=dict(
   tytul="Karty do zajęć „Co robię, zanim się zacznie”",
   wstep="Wytnij karty i pasek czasu. Zadania „w międzyczasie” przygotuj wcześniej "
         "i trzymaj w jednym pudełku — szukanie zajęcia w momencie oczekiwania przychodzi "
         "zawsze o minutę za późno.",
   karty=[("Czekam na", "symbol atrakcji, na którą dziecko czeka"),
          ("W międzyczasie 1", "symbol pierwszego krótkiego zadania"),
          ("W międzyczasie 2", "symbol drugiego zadania"),
          ("Mój żeton", "pole na żeton za wypełnione oczekiwanie")],
   pasek=["dużo czasu", "trochę czasu", "zaczynamy"])),
}

WARIANTY = {
 # ——— IV.16 · przyjęcie odmowy ————————————————————————————————————————
 ("IV.1", "A"): dict(
  podtytul="Wybór jednej z dwóch zabawek podanych po odmowie",
  ter="Dziecko wybierze jedną z dwóch zabawek podanych zaraz po odmowie i zajmie się nią, "
      "zostając przy dorosłym.",
  S="Bierze jedną z dwóch podanych zabawek i bawi się nią.",
  A="Dwie zabawki podane w tej samej chwili co odmowa dają wyjście, zanim narośnie złość.",
  pomoc_wiek="dwie zabawki trzymane w rękach dorosłego w momencie odmowy",
  przebieg=[
   ("N — przygotowuje dwie atrakcyjne zabawki poza wzrokiem dziecka.",
    "D — bawi się w kąciku."),
   ("N — odmawia rzeczy, o którą dziecko prosi, jednym zdaniem.",
    "D — słyszy odmowę."),
   ("N — natychmiast pokazuje dwie zabawki, po jednej w każdej ręce.",
    "D — patrzy na obie zabawki."),
   ("N — czeka bez powtarzania odmowy.",
    "D — bierze jedną z zabawek."),
   ("N — zostaje przy dziecku i nazywa: „nie mogłeś tamtego, wybrałeś to”.",
    "D — bawi się wybraną zabawką.")]),
 ("IV.1", "B"): dict(
  podtytul="Samodzielny wybór alternatywy po odmowie",
  ter="Dziecko przyjmie odmowę i wybierze jedną z dwóch alternatyw samo, bez krzyku "
      "i zabierania przedmiotu innemu dziecku.",
  S="Wskazuje wybraną alternatywę i zaczyna się nią zajmować.",
  A="Karty alternatyw wiszą w kąciku — dziecko wie, że wybór istnieje, zanim usłyszy „nie”.",
  pomoc_wiek="dwie karty alternatyw pokazywane razem z odmową",
  przebieg=[
   ("N — rano pokazuje karty rzeczy dostępnych zawsze, bez pytania.",
    "D — nazywa te rzeczy i wie, gdzie leżą."),
   ("N — odmawia prośby dziecka jednym zdaniem, bez tłumaczenia po raz drugi.",
    "D — słyszy odmowę i reaguje emocją."),
   ("N — nazywa emocję dziecka i pokazuje dwie karty alternatyw.",
    "D — patrzy na karty i wybiera jedną."),
   ("N — nie wraca do tematu odmowy i nie negocjuje.",
    "D — zajmuje się wybraną alternatywą."),
   ("N — po zajęciach zaznacza z dzieckiem, jak poszło przyjęcie odmowy.",
    "D — zaznacza buźkę na swojej karcie.")]),
 ("IV.1", "C"): dict(
  podtytul="Pytanie o to, kiedy będzie można dostać rzecz, o którą prosiło",
  ter="Dziecko przyjmie odmowę i zapyta, kiedy będzie mogło dostać to, o co prosiło, "
      "zamiast naciskać albo zabierać.",
  S="Pyta o termin i przyjmuje odpowiedź, zajmując się czymś innym.",
  A="Pytanie o termin zamienia odmowę „nigdy” w odmowę „nie teraz”, którą da się znieść.",
  pomoc_wiek="karta z pytaniami: „kiedy będę mógł…?”, „co mogę teraz?”",
  przebieg=[
   ("N — ćwiczy z dziećmi dwa pytania z karty w scenkach.",
    "D — zadaje oba pytania w scence."),
   ("N — w czasie zajęć odmawia prośby dziecka i podaje powód raz.",
    "D — przyjmuje odmowę bez naciskania."),
   ("N — czeka, nie proponując alternatywy od razu.",
    "D — pyta, kiedy będzie mogło dostać tę rzecz."),
   ("N — podaje konkretną porę i zapisuje ją na karcie.",
    "D — zaznacza porę i wybiera zajęcie na teraz."),
   ("N — dotrzymuje terminu i wraca do sprawy o podanej porze.",
    "D — dostaje rzecz o umówionej porze.")]),

 # ——— IV.17 · oddanie przedmiotu po zapowiedzi —————————————————————————
 ("IV.2", "A"): dict(
  podtytul="Oddanie zabawki do ręki nauczyciela po sygnale minutnika",
  ter="Dziecko odda zabawkę do ręki nauczyciela po zapowiedzi i sygnale minutnika, "
      "bez wyrywania i rzucania.",
  S="Wkłada zabawkę w podstawioną dłoń dorosłego.",
  A="Podstawiona dłoń pokazuje, co zrobić — sam sygnał jeszcze tego nie mówi.",
  pomoc_wiek="minutnik z dużym, wyraźnym sygnałem dźwiękowym",
  przebieg=[
   ("N — pokazuje minutnik i mówi: „gdy zadzwoni, oddajemy”.",
    "D — ogląda minutnik i bawi się dalej."),
   ("N — nastawia minutnik i odsuwa się.",
    "D — bawi się zabawką."),
   ("N — na minutę przed sygnałem pokazuje kartę „jeszcze chwila”.",
    "D — widzi zapowiedź i kończy zabawę."),
   ("N — po sygnale podstawia otwartą dłoń i czeka.",
    "D — wkłada zabawkę w dłoń nauczyciela."),
   ("N — nazywa: „oddałeś”, i pokazuje, gdzie zabawka będzie czekać.",
    "D — patrzy na miejsce, na które wraca zabawka.")]),
 ("IV.2", "B"): dict(
  podtytul="Odłożenie przedmiotu na wyznaczone miejsce po sygnale",
  ter="Dziecko odda przedmiot po zapowiedzi „jeszcze dwie minuty” i sygnale minutnika, "
      "odkładając go na wyznaczone miejsce bez przypominania.",
  S="Odkłada przedmiot na półkę albo do pudełka po sygnale.",
  A="Stałe miejsce odkładania robi z zakończenia czynność, a nie stratę.",
  pomoc_wiek="półka z zaznaczonym konturem przedmiotu",
  przebieg=[
   ("N — pokazuje półkę z konturem i mówi, że tam wraca przedmiot.",
    "D — dopasowuje przedmiot do konturu."),
   ("N — nastawia minutnik i zapowiada dwie minuty przed końcem.",
    "D — korzysta z pozostałego czasu."),
   ("N — po sygnale nic nie mówi i nie podchodzi.",
    "D — kończy zabawę i wstaje."),
   ("N — obserwuje, czy przedmiot trafia na miejsce.",
    "D — odkłada przedmiot na wyznaczone miejsce."),
   ("N — zaznacza udane oddanie na karcie dziecka.",
    "D — zaznacza swój znak i przechodzi do kolejnej aktywności.")]),
 ("IV.2", "C"): dict(
  podtytul="Samodzielne ustawienie minutnika na koniec zabawy",
  ter="Dziecko samo ustawi minutnik na koniec zabawy i dotrzyma tego czasu, "
      "odkładając przedmiot bez przypominania.",
  S="Ustawia czas, kończy zabawę po sygnale i odkłada przedmiot.",
  A="Czas ustawiony przez dziecko jest jego umową, nie decyzją dorosłego.",
  pomoc_wiek="minutnik obsługiwany przez dziecko i karta umowy o czasie",
  przebieg=[
   ("N — pyta, ile minut zabawy dziecko potrzebuje, w granicach do dziesięciu.",
    "D — podaje czas i ustawia minutnik."),
   ("N — zapisuje umowę na karcie i odchodzi.",
    "D — bawi się przez ustawiony czas."),
   ("N — nie przypomina o zbliżającym się końcu.",
    "D — obserwuje minutnik i kończy zabawę."),
   ("N — obserwuje z boku, czy przedmiot trafia na miejsce.",
    "D — odkłada przedmiot i wraca do grupy."),
   ("N — pyta, czy ustawiony czas był dobry.",
    "D — ocenia i proponuje czas na następny raz.")]),

 # ——— IV.18 · prośba o przedmiot ————————————————————————————————————
 ("IV.3", "A"): dict(
  podtytul="Podanie karty z obrazkiem zamiast wyrywania przedmiotu",
  ter="Dziecko poda kartę z obrazkiem przedmiotu, żeby go dostać, zamiast wyrywać "
      "przedmiot z rąk kolegi albo dorosłego.",
  S="Bierze kartę przedmiotu i podaje ją dorosłemu.",
  A="Karta jest szybsza niż wyrwanie, jeśli dorosły wydaje przedmiot natychmiast.",
  pomoc_wiek="karty z obrazkami trzech najbardziej pożądanych przedmiotów",
  przebieg=[
   ("N — kładzie trzy karty przedmiotów w zasięgu dziecka.",
    "D — ogląda karty i przedmioty."),
   ("N — trzyma pożądany przedmiot w widocznym miejscu.",
    "D — sięga po przedmiot albo po kartę."),
   ("N — przy sięgnięciu po przedmiot podaje kartę do ręki dziecka.",
    "D — bierze kartę i podaje ją nauczycielowi."),
   ("N — wydaje przedmiot natychmiast po otrzymaniu karty.",
    "D — dostaje przedmiot i bawi się nim."),
   ("N — powtarza wymianę kilka razy w czasie zajęć.",
    "D — używa karty w kolejnych sytuacjach.")]),
 ("IV.3", "B"): dict(
  podtytul="Prośba pełnym zwrotem „poproszę o…”",
  ter="Dziecko poprosi o przedmiot pełnym zwrotem „poproszę o…” i poczeka na odpowiedź, "
      "zamiast zabierać przedmiot.",
  S="Mówi pełny zwrot i czeka z rękami przy sobie.",
  A="Ten sam zwrot u wszystkich dorosłych sprawia, że prośba działa w całej sali.",
  pomoc_wiek="karta zwrotu z pustym polem na symbol przedmiotu",
  przebieg=[
   ("N — ćwiczy zwrot w zabawie z maskotką: „poproszę o klocek”.",
    "D — powtarza zwrot i dostaje przedmiot od maskotki."),
   ("N — organizuje zabawę, w której potrzebne przedmioty ma jedno dziecko.",
    "D — potrzebuje przedmiotu od kolegi albo od dorosłego."),
   ("N — czeka na prośbę, nie reaguje na sięganie po przedmiot.",
    "D — mówi pełny zwrot i czeka."),
   ("N — wydaje przedmiot od razu i nazywa: „poprosiłeś i dostałeś”.",
    "D — bierze przedmiot i włącza się w zabawę."),
   ("N — zaznacza prośbę na karcie żetonowej.",
    "D — dostaje żeton za prośbę.")]),
 ("IV.3", "C"): dict(
  podtytul="Prośba do kolegi i umowa o oddaniu przedmiotu",
  ter="Dziecko poprosi kolegę o przedmiot i umówi się z nim, kiedy go odda, zamiast "
      "zabierać albo czekać w milczeniu.",
  S="Prosi kolegę, ustala czas oddania i dotrzymuje umowy.",
  A="Umowa z kolegą przenosi prośbę z relacji z dorosłym na relację z dzieckiem.",
  pomoc_wiek="karta umowy między dziećmi z miejscem na dwa znaki",
  przebieg=[
   ("N — omawia z dziećmi, jak prosić kolegę i jak umawiać się na oddanie.",
    "D — ćwiczy prośbę i umowę w parze."),
   ("N — organizuje zabawę z jednym atrakcyjnym przedmiotem na grupę.",
    "D — chce dostać przedmiot od kolegi."),
   ("N — nie pośredniczy, obserwuje z boku.",
    "D — prosi kolegę i proponuje czas oddania."),
   ("N — pomaga zapisać umowę na karcie, jeśli dzieci tego potrzebują.",
    "D — zaznacza umowę razem z kolegą."),
   ("N — pyta po zabawie, czy umowa została dotrzymana.",
    "D — ocenia umowę i mówi, co poprawi następnym razem.")]),

 # ——— IV.19 · czekanie na przedmiot ————————————————————————————————
 ("IV.4", "A"): dict(
  podtytul="Czekanie 30 sekund z kartą „czekam”",
  ter="Dziecko poczeka 30 sekund na przedmiot, trzymając kartę „czekam”, zamiast "
      "wyrywać go albo płakać.",
  S="Trzyma kartę do końca odliczania i przyjmuje przedmiot.",
  A="Klepsydra pokazuje koniec czekania — czas przestaje być nieznany.",
  pomoc_wiek="klepsydra 30-sekundowa stawiana przed dzieckiem",
  przebieg=[
   ("N — pokazuje przedmiot i kartę „czekam”, nazywa obie rzeczy.",
    "D — patrzy na przedmiot i bierze kartę."),
   ("N — odwraca klepsydrę i trzyma przedmiot w widocznym miejscu.",
    "D — trzyma kartę i patrzy na klepsydrę."),
   ("N — nie oddaje przedmiotu przed końcem, także przy płaczu.",
    "D — czeka do końca odliczania."),
   ("N — po przesypaniu klepsydry wydaje przedmiot.",
    "D — dostaje przedmiot i bawi się nim."),
   ("N — nazywa: „czekałeś i dostałeś”, i powtarza ćwiczenie.",
    "D — czeka drugi raz w tych samych zajęciach.")]),
 ("IV.4", "B"): dict(
  podtytul="Czekanie trzech minut z wizualnym licznikiem",
  ter="Dziecko poczeka trzy minuty na przedmiot, korzystając z wizualnego licznika, "
      "i zajmie się w tym czasie czymś innym.",
  S="Zostaje przy stoliku przez czas licznika i zajmuje się zadaniem.",
  A="Zajęcie na czas czekania zamienia puste minuty w policzalne zadanie.",
  pomoc_wiek="licznik wizualny i pudełko z krótkim zadaniem na czas czekania",
  przebieg=[
   ("N — umawia się: „dostaniesz, gdy licznik dojdzie do końca”.",
    "D — patrzy na licznik i przyjmuje umowę."),
   ("N — podaje pudełko z zadaniem na czas czekania.",
    "D — bierze zadanie i zaczyna je."),
   ("N — nie skraca ani nie wydłuża czasu.",
    "D — pracuje i sprawdza licznik."),
   ("N — po sygnale wydaje przedmiot od razu.",
    "D — dostaje przedmiot."),
   ("N — zaznacza udane czekanie na karcie odroczeń.",
    "D — zaznacza swój znak.")]),
 ("IV.4", "C"): dict(
  podtytul="Czekanie do umówionej pory dnia, bez licznika",
  ter="Dziecko umówi się z nauczycielem, kiedy dostanie przedmiot, i doczeka do tej pory "
      "bez przypominania i naciskania.",
  S="Ustala porę, zajmuje się zajęciami i wraca po przedmiot o umówionym czasie.",
  A="Zapisana pora na planie dnia zastępuje licznik, którego dziecko już nie potrzebuje.",
  pomoc_wiek="plan dnia z zaznaczoną porą, o której dziecko dostanie przedmiot",
  przebieg=[
   ("N — pyta, o której porze dnia dziecko chce dostać przedmiot.",
    "D — wybiera porę i zaznacza ją na planie."),
   ("N — zapisuje umowę i odkłada przedmiot w widocznym miejscu.",
    "D — widzi przedmiot i wie, kiedy go dostanie."),
   ("N — prowadzi zajęcia i nie wraca do tematu.",
    "D — uczestniczy w zajęciach, nie dopominając się."),
   ("N — o umówionej porze przypomina o umowie.",
    "D — przychodzi po przedmiot o umówionym czasie."),
   ("N — pyta, czy czekanie było trudne i co pomagało.",
    "D — nazywa, co pomogło mu doczekać.")]),

 # ——— IV.20 · czynność „w międzyczasie” ——————————————————————————————
 ("IV.5", "A"): dict(
  podtytul="Zajęcie się zabawką podaną na czas czekania na atrakcję",
  ter="Dziecko zajmie się zabawką podaną na czas czekania na atrakcję i zostanie "
      "przy niej do sygnału rozpoczęcia.",
  S="Bierze podaną zabawkę i bawi się nią do sygnału.",
  A="Zabawka w rękach wypełnia czas, w którym atrakcja jest już widoczna, ale niedostępna.",
  pomoc_wiek="dwie zabawki „na czekanie”, używane tylko w tych sytuacjach",
  przebieg=[
   ("N — zapowiada atrakcję i pokazuje, ile czasu zostało na pasku.",
    "D — widzi atrakcję i pasek czasu."),
   ("N — podaje zabawkę „na czekanie”.",
    "D — bierze zabawkę i zaczyna się nią bawić."),
   ("N — zostaje przy dziecku i bawi się razem z nim.",
    "D — bawi się przez czas oczekiwania."),
   ("N — przesuwa znacznik na pasku czasu.",
    "D — patrzy, ile zostało do startu."),
   ("N — daje sygnał rozpoczęcia atrakcji.",
    "D — odkłada zabawkę i przechodzi do atrakcji.")]),
 ("IV.5", "B"): dict(
  podtytul="Zadanie z pudełka „w międzyczasie” i żeton za wypełnione czekanie",
  ter="Dziecko wykona zadanie z pudełka „w międzyczasie” w czasie oczekiwania na atrakcyjną "
      "aktywność i dostanie za to żeton.",
  S="Bierze zadanie z pudełka, wykonuje je i odkłada przed startem atrakcji.",
  A="Żeton łączy czekanie z nagrodą, zamiast zostawiać je jako karę za bycie pierwszym.",
  pomoc_wiek="pudełko z trzema krótkimi zadaniami i tabliczka żetonowa",
  przebieg=[
   ("N — zapowiada atrakcję i pokazuje pudełko „w międzyczasie”.",
    "D — wybiera jedno zadanie z pudełka."),
   ("N — nastawia pasek czasu do startu atrakcji.",
    "D — zaczyna wykonywać zadanie."),
   ("N — nie przypomina i nie ponagla.",
    "D — pracuje nad zadaniem do sygnału."),
   ("N — po sygnale zbiera zadania i wydaje żeton.",
    "D — odkłada zadanie i bierze żeton."),
   ("N — rozpoczyna atrakcję zaraz po żetonie.",
    "D — przechodzi do atrakcji.")]),
 ("IV.5", "C"): dict(
  podtytul="Własny plan na czas oczekiwania i jego realizacja",
  ter="Dziecko zaplanuje, czym zajmie się w czasie czekania na atrakcję, i wykona "
      "ten plan do sygnału rozpoczęcia.",
  S="Zapisuje albo mówi swój plan i realizuje go do końca oczekiwania.",
  A="Własny plan trzyma uwagę dłużej niż zadanie przydzielone przez dorosłego.",
  pomoc_wiek="kartka planu: „w czasie czekania zrobię…” z trzema polami",
  przebieg=[
   ("N — zapowiada atrakcję i mówi, ile czasu zostało.",
    "D — planuje, czym się zajmie, i zapisuje to."),
   ("N — pyta, czy plan da się wykonać w tym czasie.",
    "D — skraca albo poszerza plan."),
   ("N — nie ingeruje w czasie oczekiwania.",
    "D — realizuje swój plan."),
   ("N — po sygnale pyta, ile z planu udało się zrobić.",
    "D — pokazuje wykonaną część planu."),
   ("N — rozpoczyna atrakcję i wraca do planu po jej zakończeniu.",
    "D — kończy niedokończoną część planu albo zapisuje ją na jutro.")]),
}
