# -*- coding: utf-8 -*-
"""Konspekty do funkcji V — regulacja emocji / napięcie (wskaźniki V.1–V.5).

Wspólny mianownik: **pracujemy przed wybuchem, nie po nim.** Po wybuchu nie ma
już czego uczyć — jest opieka i bezpieczeństwo. Wszystkie pięć konspektów celuje
w fazę narastania: uprzedzenie zmiany, nazwanie napięcia, wyjście z bodźców,
powrót i sygnał ostrzegawczy. Dlatego ćwiczymy je w dniach spokojnych, nie
w trudnych — umiejętność wyćwiczona w spokoju bywa dostępna w napięciu,
odwrotnie nigdy.
"""

RDZEN = {
 "V.1": dict(
  tytul="Zmiana, o której wiem wcześniej",
  icf="d230·d240", pp="2.12·1.4",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["uprzedzanie zmiany zanim nastąpi, nie w jej trakcie",
          "pokazanie zmiany na planie dnia, nie tylko powiedzenie",
          "odliczanie do zmiany: pięć minut, dwie minuty, teraz",
          "ta sama procedura przy każdej zmianie, także drobnej",
          "nazywanie emocji wobec zmiany bez nakłaniania do zgody"],
  pomoce=["plan dnia z kartami do przekładania, na wysokości wzroku dziecka",
          "karta „zmiana” do wstawienia w plan",
          "minutnik do odliczania ostatnich minut aktywności",
          "buźki do nazwania reakcji na zmianę"],
  wskazowka="Uprzedzaj także o zmianach na lepsze. Dziecko o tej funkcji reaguje na samą "
            "zmianę, nie na jej treść — niezapowiedziana wycieczka bywa dla niego tak samo "
            "trudna jak niezapowiedziane sprzątanie.",
  ter_kryt="Plan dnia — zapis zmiany i reakcji · wszystkie zmiany planu w tygodniu.",
  R="Zmiana planu w przedszkolu jest nie do uniknięcia — da się ją tylko zapowiedzieć.",
  mod=("nauczyciel przechodzi razem z dzieckiem i pokazuje zmianę na planie",
       "dziecko przechodzi po samej zapowiedzi słownej",
       "dziecko proponuje, jak przestawić plan po zmianie"),
  arkusz=dict(
   tytul="Karty do zajęć „Zmiana, o której wiem wcześniej”",
   wstep="Wytnij karty i wpinaj je w plan dnia dziecka. Karta „zmiana” ma być jedna "
         "i zawsze ta sama — dziecko rozpoznaje ją szybciej niż zdanie, które słyszy. "
         "Symbole wklej z biblioteki EduPlaner.",
   karty=[("Zmiana", "symbol zmiany — karta wstawiana w plan dnia"),
          ("Za pięć minut", "symbol odliczania: zostało pięć minut"),
          ("Teraz to", "symbol nowej aktywności"),
          ("Jak się czuję", "buźki do zaznaczenia po zmianie")],
   pasek=["wiem wcześniej", "odliczam", "przechodzę"])),

 "V.2": dict(
  tytul="Termometr, zanim zrobi się czerwono",
  icf="b152·d335", pp="2.9·9.10",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["trzy poziomy zamiast wielu nazw emocji: zielony, żółty, czerwony",
          "nazywanie stanu ciała, nie tylko emocji",
          "termometr sprawdzany w spokoju, nie tylko w napięciu",
          "modelowanie: dorosły też pokazuje swój kolor",
          "łączenie koloru ze strategią: żółty ma swoje wyjście"],
  pomoce=["termometr emocji z trzema polami, leżący na stoliku dziecka",
          "karty strategii przypisane do żółtego pola",
          "lustro do rozpoznawania własnej miny",
          "karta zapisu wskazań z całego dnia"],
  wskazowka="Sprawdzaj termometr także wtedy, gdy jest zielono. Narzędzie używane wyłącznie "
            "w napięciu dziecko odbiera jako zapowiedź kłopotów i przestaje po nie sięgać "
            "dokładnie wtedy, gdy jest potrzebne.",
  ter_kryt="Termometr emocji — zapis wskazań w ciągu dnia · wszystkie sytuacje napięcia.",
  R="Nazwane napięcie da się obniżyć; nienazwane rośnie do wybuchu.",
  mod=("nauczyciel pyta o kolor i pokazuje dwa pola do wyboru",
       "dziecko wskazuje kolor samo przy pierwszych objawach",
       "dziecko nazywa emocję i jej powód, potem wybiera strategię"),
  arkusz=dict(
   tytul="Termometr emocji do zajęć „Zanim zrobi się czerwono”",
   wstep="Wytnij termometr i karty. Termometr zostaje na stoliku dziecka na stałe. "
         "W pola przy kolorze żółtym wklej symbole strategii, które u was działają — "
         "kolor bez wyjścia jest tylko etykietą.",
   karty=[("Zielony", "symbol spokoju — mogę pracować"),
          ("Żółty", "symbol napięcia — potrzebuję strategii"),
          ("Czerwony", "symbol wybuchu — potrzebuję pomocy dorosłego"),
          ("Moja strategia", "symbol tego, co pomaga przy żółtym")],
   pasek=["sprawdzam", "nazywam", "wybieram strategię"])),

 "V.3": dict(
  tytul="Kącik, w którym robi się ciszej",
  icf="d240·b152", pp="2.12·9.10",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["wyjście z bodźców jako strategia, nie jako kara",
          "kącik dostępny bez proszenia za każdym razem",
          "stały zestaw form wyciszenia w kąciku",
          "czas wyciszenia widoczny, zakończenie własne albo po sygnale",
          "ćwiczenie korzystania z kącika w dniach spokojnych"],
  pomoce=["kącik wyciszenia w sali: koc, poduszka, słuchawki wygłuszające",
          "karta wejścia do kącika, kładziona przy wejściu",
          "minutnik pięciominutowy w kąciku",
          "karta trzech form wyciszenia do wyboru"],
  wskazowka="Kącik wyciszenia nie może być miejscem, do którego się kogoś odsyła. Jeśli raz "
            "posłuży za karę, dziecko przestanie z niego korzystać samo — a właśnie o to "
            "samodzielne korzystanie w tym celu chodzi.",
  ter_kryt="Rejestr kącika wyciszenia — kto zainicjował i jak długo · wszystkie sytuacje przebodźcowania.",
  R="Wyjście z bodźców przerywa narastanie, zanim dojdzie do wybuchu.",
  mod=("nauczyciel proponuje kącik i idzie tam razem z dzieckiem",
       "dziecko korzysta z kącika na własną prośbę",
       "dziecko wybiera strategię przy stoliku, bez wychodzenia z zajęć"),
  arkusz=dict(
   tytul="Karty do zajęć „Kącik, w którym robi się ciszej”",
   wstep="Wytnij karty i powieś je w kąciku wyciszenia. Formy na kartach mają być "
         "naprawdę dostępne w tym kąciku — karta z formą, której tam nie ma, uczy dziecko, "
         "że kącik nie działa. Symbole wklej z biblioteki EduPlaner.",
   karty=[("Idę do kącika", "symbol wejścia — karta kładziona przy wejściu"),
          ("Oddech", "symbol ćwiczenia oddechowego"),
          ("Ciężki koc", "symbol ucisku"),
          ("Cisza", "symbol słuchawek wygłuszających")],
   pasek=["wchodzę", "wyciszam się", "wychodzę"])),

 "V.4": dict(
  tytul="Wracam do grupy",
  icf="d230·d240", pp="2.12·2.6",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["powrót w ustalonym czasie, nie „gdy będzie gotowe”",
          "zadanie po powrocie skrócone, nie zaległe w całości",
          "brak rozmowy o zdarzeniu bezpośrednio po powrocie",
          "naprawa relacji jako osobny krok, po uspokojeniu",
          "wzmocnienie za powrót, osobno od wzmocnienia za pracę"],
  pomoce=["minutnik odmierzający czas na powrót",
          "karta „wracam” z symbolem miejsca w grupie",
          "skrócona wersja zadania przygotowana wcześniej",
          "karta naprawy: przeprosiny albo posprzątanie"],
  wskazowka="Nie omawiaj zdarzenia w pierwszych minutach po powrocie. Rozmowa w napięciu "
            "kończy się drugim wybuchem — wróć do niej po zajęciach, gdy dziecko jest "
            "w stanie o tym myśleć.",
  ter_kryt="Rejestr kącika wyciszenia — czas powrotu do zajęć · wszystkie wyciszenia.",
  R="Bez powrotu wyciszenie zamienia się w ucieczkę z zajęć — i przestaje być strategią.",
  mod=("nauczyciel wraca z dzieckiem i siada obok na czas pierwszego zadania",
       "dziecko wraca po sygnale i dokańcza zadanie przerwane przed wyjściem",
       "dziecko wraca samo i naprawia to, co się wydarzyło"),
  arkusz=dict(
   tytul="Karty do zajęć „Wracam do grupy”",
   wstep="Wytnij karty. Karta „moje miejsce” wskazuje, dokąd dziecko wraca — powrót do "
         "konkretnego miejsca jest łatwiejszy niż powrót „do grupy”. Symbole wklej "
         "z biblioteki EduPlaner.",
   karty=[("Wracam", "symbol powrotu z kącika"),
          ("Moje miejsce", "symbol konkretnego miejsca w sali"),
          ("Kończę zadanie", "symbol skróconej części zadania"),
          ("Naprawiam", "symbol przeprosin albo posprzątania")],
   pasek=["kończę wyciszenie", "wracam", "kończę zadanie"])),

 "V.5": dict(
  tytul="Czerwona karta, zanim wybuchnie",
  icf="b152·d335", pp="2.9·2.12",
  rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",
  metody=["rozpoznawanie własnych sygnałów ostrzegawczych ciała",
          "sygnalizowanie napięcia zanim urośnie",
          "natychmiastowa reakcja dorosłego na sygnał dziecka",
          "ćwiczenie sygnału w spokoju, nie w napięciu",
          "zapis sygnałów w rejestrze ABC jako poprzednika"],
  pomoce=["czerwona karta w stałym miejscu przy dziecku",
          "karta trzech sygnałów ciała, uzupełniana z dzieckiem",
          "plan reakcji: co robimy natychmiast po czerwonej karcie",
          "rejestr ABC z kolumną „sygnał dziecka”"],
  wskazowka="Po czerwonej karcie reaguj natychmiast, przerywając to, co robisz. Sygnał, "
            "na który dorosły odpowiada „za chwilę”, przestaje być używany po dwóch takich "
            "chwilach — a wtedy zostaje tylko wybuch.",
  ter_kryt="Rejestr ABC — sygnał dziecka przed zachowaniem (tak/nie) · wszystkie narastania napięcia.",
  R="To jedyny cel, który skraca fazę nagłego wybuchu — reszta pracuje po niej.",
  mod=("nauczyciel podaje czerwoną kartę, gdy zauważy sygnały u dziecka",
       "dziecko sięga po kartę samo, zanim dojdzie do wybuchu",
       "dziecko nazywa sygnał słowami i samo używa strategii"),
  arkusz=dict(
   tytul="Karty do zajęć „Czerwona karta, zanim wybuchnie”",
   wstep="Wytnij czerwoną kartę i karty sygnałów. Sygnały ciała uzupełnij razem "
         "z dzieckiem — to mają być jego sygnały, nie lista z podręcznika. Symbole "
         "pozostałych kart wklej z biblioteki EduPlaner.",
   karty=[("Czerwona karta", "duże czerwone pole — sygnał dziecka do dorosłego"),
          ("Sygnał 1", "miejsce na pierwszy sygnał ciała dziecka"),
          ("Sygnał 2", "miejsce na drugi sygnał"),
          ("Co robimy", "symbol reakcji dorosłego: podejście, przerwa, kącik")],
   pasek=["zauważam", "pokazuję kartę", "dostaję pomoc"])),
}

WARIANTY = {
 # ——— V.21 · przejście do zmienionej aktywności ————————————————————————
 ("V.1", "A"): dict(
  podtytul="Przejście do nowej aktywności za dorosłym, po pokazaniu obrazka zmiany",
  ter="Dziecko przejdzie do nowej aktywności za dorosłym, po pokazaniu obrazka zmiany, "
      "bez płaczu i rzucania się na podłogę.",
  S="Wstaje i idzie za dorosłym do nowej aktywności.",
  A="Obrazek pokazuje zmianę wcześniej, niż zdąży ją poczuć jako zaskoczenie.",
  pomoc_wiek="duży obrazek nowej aktywności pokazywany przed zmianą",
  przebieg=[
   ("N — na dwie minuty przed zmianą pokazuje obrazek nowej aktywności.",
    "D — patrzy na obrazek i kończy zabawę."),
   ("N — odlicza: „jeszcze dwa razy i idziemy”.",
    "D — kończy dwa ostatnie ruchy zabawy."),
   ("N — podaje rękę i pokazuje kierunek.",
    "D — wstaje i idzie za dorosłym."),
   ("N — w nowym miejscu pokazuje, co dziecko będzie robić.",
    "D — zaczyna nową aktywność."),
   ("N — nazywa, co się stało: „była zmiana i poszedłeś”.",
    "D — bierze udział w nowej aktywności.")]),
 ("V.1", "B"): dict(
  podtytul="Przejście po przełożeniu karty na planie dnia",
  ter="Dziecko przejdzie do zmienionej aktywności po uprzedzeniu i przełożeniu karty "
      "na planie dnia, bez zachowania trudnego.",
  S="Ogląda zmianę na planie i przechodzi do nowej aktywności w ciągu minuty.",
  A="Plan pokazuje, że zmiana jest częścią dnia, a nie jego zerwaniem.",
  pomoc_wiek="plan dnia z kartami do przekładania, na wysokości wzroku dziecka",
  przebieg=[
   ("N — podchodzi do planu z dzieckiem i pokazuje kartę, która się zmienia.",
    "D — patrzy na plan i nazywa starą aktywność."),
   ("N — wyjmuje starą kartę i wstawia kartę zmiany.",
    "D — przekłada kartę razem z nauczycielem."),
   ("N — mówi, co będzie zamiast, i wstawia nową kartę.",
    "D — nazywa nową aktywność."),
   ("N — odlicza dwie minuty do przejścia.",
    "D — kończy to, co robiło."),
   ("N — przechodzi z grupą i sprawdza, czy dziecko idzie.",
    "D — przechodzi do nowej aktywności.")]),
 ("V.1", "C"): dict(
  podtytul="Propozycja, jak przestawić plan po zmianie",
  ter="Dziecko przyjmie zmianę planu i zaproponuje, jak przestawić resztę dnia, "
      "a potem przejdzie do nowej aktywności.",
  S="Mówi, co przesunąć i na kiedy, i przechodzi do nowej aktywności.",
  A="Współdecydowanie o reszcie dnia oddaje dziecku sprawczość, której zmiana mu odebrała.",
  pomoc_wiek="ruchome karty planu dnia, które dziecko może samo przestawiać",
  przebieg=[
   ("N — informuje o zmianie i mówi, czego nie da się przesunąć.",
    "D — słucha i patrzy na plan."),
   ("N — pyta: „co zrobimy z tym, co miało być teraz?”.",
    "D — proponuje, na kiedy przesunąć aktywność."),
   ("N — przyjmuje propozycję albo tłumaczy, dlaczego się nie da.",
    "D — przestawia karty na planie."),
   ("N — przechodzi z grupą do nowej aktywności.",
    "D — przechodzi razem z grupą."),
   ("N — pod koniec dnia sprawdza z dzieckiem, czy przesunięcie się udało.",
    "D — ocenia swoją propozycję.")]),

 # ——— V.22 · nazwanie napięcia ————————————————————————————————————
 ("V.2", "A"): dict(
  podtytul="Wskazanie buźki pokazującej, jak się czuję",
  ter="Dziecko wskaże buźkę pokazującą, jak się czuje, z dwóch podanych, "
      "przy pierwszych objawach napięcia.",
  S="Wskazuje palcem jedną z dwóch buziek.",
  A="Wybór z dwóch buziek jest odpowiedzią możliwą także wtedy, gdy słowa już nie przychodzą.",
  pomoc_wiek="dwie duże buźki: spokojna i zła",
  przebieg=[
   ("N — pokazuje dwie buźki i nazywa je w zabawie z lustrem.",
    "D — robi obie miny i wskazuje odpowiadające im buźki."),
   ("N — w ciągu dnia pyta o buźkę także w spokojnych momentach.",
    "D — wskazuje spokojną buźkę."),
   ("N — przy pierwszych oznakach napięcia pokazuje obie buźki.",
    "D — wskazuje buźkę złą."),
   ("N — nazywa: „jesteś zły”, i proponuje jedną strategię.",
    "D — korzysta z zaproponowanej strategii."),
   ("N — po uspokojeniu pyta jeszcze raz o buźkę.",
    "D — wskazuje buźkę spokojną.")]),
 ("V.2", "B"): dict(
  podtytul="Samodzielne wskazanie koloru na termometrze emocji",
  ter="Dziecko wskaże kolor na termometrze emocji samo, przy pierwszych objawach napięcia, "
      "i wybierze strategię z pola żółtego.",
  S="Wskazuje kolor i sięga po jedną ze strategii przypisanych do żółtego.",
  A="Termometr leży na stoliku — wskazanie nie wymaga wołania ani wychodzenia.",
  pomoc_wiek="termometr emocji z trzema kolorami leżący przy dziecku",
  przebieg=[
   ("N — omawia trzy kolory i przypisane do nich strategie.",
    "D — nazywa kolory i strategie."),
   ("N — sprawdza kolor razem z dzieckiem trzy razy w ciągu spokojnego dnia.",
    "D — wskazuje kolor i mówi, po czym go poznaje."),
   ("N — przy zajęciach trudniejszych obserwuje i nie pyta.",
    "D — wskazuje kolor żółty przy pierwszych objawach napięcia."),
   ("N — potwierdza i przypomina o strategiach z żółtego pola.",
    "D — wybiera strategię i korzysta z niej."),
   ("N — zapisuje wskazanie w karcie dnia.",
    "D — wraca do zajęć.")]),
 ("V.2", "C"): dict(
  podtytul="Nazwanie emocji i jej powodu",
  ter="Dziecko nazwie emocję i jej powód zdaniem „złoszczę się, bo…”, przy pierwszych "
      "objawach napięcia, i wybierze strategię.",
  S="Mówi pełne zdanie o emocji i powodzie, a potem wybiera strategię.",
  A="Nazwany powód pozwala usunąć wyzwalacz, a nie tylko obniżyć napięcie.",
  pomoc_wiek="karta zdań: „złoszczę się, bo…”, „boję się, bo…”, „jest mi smutno, bo…”",
  przebieg=[
   ("N — ćwiczy z dziećmi zdania o emocjach na przykładach z bajki.",
    "D — kończy zdania za bohatera."),
   ("N — pyta dzieci o ich własne przykłady z ostatniego tygodnia.",
    "D — podaje swój przykład i kończy zdanie."),
   ("N — w czasie zajęć obserwuje sygnały napięcia.",
    "D — mówi zdanie o swojej emocji i powodzie."),
   ("N — nazywa powód i pyta, co pomoże.",
    "D — wybiera strategię i korzysta z niej."),
   ("N — po zajęciach zapisuje z dzieckiem powód w rejestrze.",
    "D — nazywa, co wywołało napięcie.")]),

 # ——— V.23 · strefa wyciszenia ————————————————————————————————————
 ("V.3", "A"): dict(
  podtytul="Wyjście do kącika wyciszenia prowadzone za rękę",
  ter="Dziecko pójdzie do kącika wyciszenia prowadzone za rękę i zostanie tam minutę, "
      "gdy w sali zrobi się głośno.",
  S="Idzie z dorosłym do kącika i zostaje tam przez czas minutnika.",
  A="Prowadzenie za rękę pokazuje drogę, której dziecko nie zapamięta w napięciu.",
  pomoc_wiek="kącik z jedną formą wyciszenia: kocem albo poduszką",
  przebieg=[
   ("N — pokazuje kącik w spokojnym momencie dnia i siada tam z dzieckiem.",
    "D — ogląda kącik i próbuje koca."),
   ("N — w hałaśliwym momencie proponuje kącik i podaje rękę.",
    "D — idzie z dorosłym do kącika."),
   ("N — zostaje z dzieckiem, nie rozmawia, nie tłumaczy.",
    "D — siedzi w kąciku pod kocem."),
   ("N — po minucie pyta gestem, czy wracamy.",
    "D — pokazuje, czy chce zostać, czy wrócić."),
   ("N — wraca z dzieckiem do grupy.",
    "D — włącza się w zabawę.")]),
 ("V.3", "B"): dict(
  podtytul="Skorzystanie z kącika na własną prośbę, przez pięć minut",
  ter="Dziecko skorzysta z kącika wyciszenia na własną prośbę przez pięć minut, "
      "kładąc kartę wejścia i wracając po sygnale.",
  S="Kładzie kartę, idzie do kącika i wraca po minutniku.",
  A="Kącik jest dostępny bez pytania — prośba nie wymaga zgody dorosłego.",
  pomoc_wiek="karta wejścia do kącika i minutnik pięciominutowy w kąciku",
  przebieg=[
   ("N — przypomina, że z kącika można skorzystać zawsze, bez pytania.",
    "D — sprawdza, gdzie leży karta wejścia."),
   ("N — prowadzi zajęcia z bodźcami: muzyką, ruchem, hałasem.",
    "D — uczestniczy i obserwuje własne napięcie."),
   ("N — nie proponuje kącika, obserwuje z boku.",
    "D — kładzie kartę i idzie do kącika."),
   ("N — nie wchodzi do kącika i nie zagaduje.",
    "D — korzysta z wybranej formy wyciszenia."),
   ("N — po powrocie zapisuje w rejestrze, kto zainicjował wyjście.",
    "D — wraca do zajęć po sygnale minutnika.")]),
 ("V.3", "C"): dict(
  podtytul="Strategia oddechowa przy stoliku, bez wychodzenia z zajęć",
  ter="Dziecko skorzysta ze strategii oddechowej przy stoliku, bez wychodzenia z zajęć, "
      "gdy poczuje przeciążenie.",
  S="Wykonuje ćwiczenie oddechowe na miejscu i wraca do zadania.",
  A="Strategia przy stoliku pozwala zostać z grupą — wyjście przestaje być jedynym wyjściem.",
  pomoc_wiek="karta trzech oddechów z rysunkiem: świeczka, kwiat, balon",
  przebieg=[
   ("N — uczy trzech ćwiczeń oddechowych w spokojnej części dnia.",
    "D — ćwiczy wszystkie trzy i wybiera swoje."),
   ("N — kładzie kartę oddechów na stoliku dziecka.",
    "D — wie, gdzie leży karta."),
   ("N — prowadzi zajęcia i obserwuje sygnały przeciążenia.",
    "D — sięga po kartę i wykonuje oddech przy stoliku."),
   ("N — nie komentuje przy grupie, daje dziecku czas.",
    "D — kończy ćwiczenie i wraca do zadania."),
   ("N — po zajęciach pyta, czy oddech wystarczył, czy potrzebny był kącik.",
    "D — ocenia strategię i wybiera ją na następny raz.")]),

 # ——— V.24 · powrót do zajęć ——————————————————————————————————————
 ("V.4", "A"): dict(
  podtytul="Powrót do grupy za dorosłym po wyciszeniu",
  ter="Dziecko wróci do grupy za dorosłym po wyciszeniu i włączy się w zabawę, "
      "bez ponownego wychodzenia.",
  S="Wstaje z kącika i idzie z dorosłym do grupy.",
  A="Powrót z dorosłym jest łatwiejszy niż wejście do grupy w pojedynkę.",
  pomoc_wiek="karta „moje miejsce” z symbolem miejsca w kręgu",
  przebieg=[
   ("N — po wyciszeniu podchodzi i pokazuje kartę „moje miejsce”.",
    "D — patrzy na kartę."),
   ("N — podaje rękę i czeka bez ponaglania.",
    "D — wstaje z kącika."),
   ("N — idzie z dzieckiem do jego miejsca w grupie.",
    "D — siada na swoim miejscu."),
   ("N — podaje dziecku zabawkę albo materiał, żeby miało co robić.",
    "D — włącza się w zabawę."),
   ("N — nie wraca do tematu zdarzenia przed zajęciami.",
    "D — bawi się z grupą.")]),
 ("V.4", "B"): dict(
  podtytul="Powrót w ciągu trzech minut i dokończenie przerwanego zadania",
  ter="Dziecko wróci do zajęć w ciągu trzech minut od zakończenia wyciszenia "
      "i dokończy zadanie przerwane przed wyjściem.",
  S="Wraca na miejsce i pracuje nad zadaniem przerwanym wcześniej.",
  A="Skrócone zadanie przygotowane wcześniej jest wykonalne zaraz po napięciu.",
  pomoc_wiek="skrócona wersja zadania odłożona na miejscu dziecka",
  przebieg=[
   ("N — przed wyjściem dziecka zostawia na stoliku skróconą wersję zadania.",
    "D — korzysta z wyciszenia w kąciku."),
   ("N — po sygnale minutnika czeka przy grupie, nie idzie po dziecko.",
    "D — kończy wyciszenie i wstaje."),
   ("N — wita krótko, bez omawiania zdarzenia.",
    "D — wraca na swoje miejsce."),
   ("N — pokazuje skróconą wersję zadania.",
    "D — dokańcza skrócone zadanie."),
   ("N — po zajęciach wraca z dzieckiem do tego, co się wydarzyło.",
    "D — opowiada o zdarzeniu, gdy jest już spokojne.")]),
 ("V.4", "C"): dict(
  podtytul="Powrót do zajęć i naprawa tego, co się wydarzyło",
  ter="Dziecko wróci do zajęć po wyciszeniu i naprawi to, co się wydarzyło — przeprosi "
      "albo posprząta — bez przypominania dorosłego.",
  S="Wraca, wykonuje krok naprawy i włącza się w zajęcia.",
  A="Karta naprawy pokazuje trzy możliwe kroki — dziecko nie musi ich wymyślać w napięciu.",
  pomoc_wiek="karta naprawy z trzema krokami do wyboru",
  przebieg=[
   ("N — po wyciszeniu pokazuje kartę naprawy z trzema krokami.",
    "D — wybiera krok: przeproszę, posprzątam, naprawię."),
   ("N — nie żąda przeprosin, jeśli dziecko wybiera inny krok.",
    "D — wykonuje wybrany krok naprawy."),
   ("N — towarzyszy przy naprawie, nie mówiąc za dziecko.",
    "D — rozmawia z kolegą albo sprząta."),
   ("N — wraca z dzieckiem do zajęć.",
    "D — włącza się w zajęcia."),
   ("N — po zajęciach rozmawia o tym, co pomogło się uspokoić.",
    "D — nazywa strategię, która zadziałała.")]),

 # ——— V.25 · sygnał przed wybuchem ————————————————————————————————
 ("V.5", "A"): dict(
  podtytul="Pokazanie czerwonej karty podanej przez dorosłego",
  ter="Dziecko pokaże czerwoną kartę podaną przez dorosłego, gdy zaczyna się złościć, "
      "zamiast krzyczeć albo rzucać przedmiotem.",
  S="Bierze czerwoną kartę i podnosi ją albo podaje dorosłemu.",
  A="Karta podana w pierwszej chwili napięcia daje dziecku ruch inny niż uderzenie.",
  pomoc_wiek="czerwona karta trzymana przez dorosłego w zasięgu wzroku dziecka",
  przebieg=[
   ("N — pokazuje czerwoną kartę w spokoju i mówi, co się po niej dzieje.",
    "D — ogląda kartę i próbuje ją podnieść."),
   ("N — ćwiczy sytuację na niby: „miś się złości, pokazuje kartę”.",
    "D — pokazuje kartę za misia i dostaje pomoc."),
   ("N — obserwuje dziecko i przy pierwszych sygnałach podaje kartę.",
    "D — bierze kartę i podnosi ją."),
   ("N — reaguje natychmiast: przerywa zajęcie i podchodzi.",
    "D — dostaje pomoc, zanim dojdzie do wybuchu."),
   ("N — zapisuje w rejestrze, że pojawił się sygnał.",
    "D — korzysta ze strategii i wraca do zabawy.")]),
 ("V.5", "B"): dict(
  podtytul="Samodzielne sięgnięcie po czerwoną kartę przed wybuchem",
  ter="Dziecko pokaże czerwoną kartę samo, zanim dojdzie do wybuchu, i skorzysta "
      "z zaproponowanej strategii.",
  S="Sięga po kartę z własnej inicjatywy i pokazuje ją dorosłemu.",
  A="Karta leży w tym samym miejscu przez cały dzień — nie trzeba jej szukać w napięciu.",
  pomoc_wiek="czerwona karta w stałym miejscu przy dziecku, na rzepie",
  przebieg=[
   ("N — omawia z dzieckiem, po czym pozna u siebie narastanie złości.",
    "D — nazywa dwa swoje sygnały i zaznacza je na karcie."),
   ("N — przypina czerwoną kartę w stałym miejscu.",
    "D — sprawdza, gdzie karta jest."),
   ("N — prowadzi zajęcia i nie podaje karty sam.",
    "D — sięga po kartę przy pierwszym sygnale."),
   ("N — reaguje natychmiast i proponuje dwie strategie.",
    "D — wybiera strategię i korzysta z niej."),
   ("N — zapisuje sygnał i strategię w rejestrze ABC.",
    "D — wraca do zajęć.")]),
 ("V.5", "C"): dict(
  podtytul="Rozpoznanie własnego sygnału i użycie strategii bez pomocy",
  ter="Dziecko rozpozna swój sygnał ostrzegawczy i samo użyje strategii, zanim dojdzie "
      "do wybuchu, informując dorosłego, co robi.",
  S="Nazywa sygnał, wybiera strategię i mówi dorosłemu, z czego korzysta.",
  A="Własna lista sygnałów i strategii sprawia, że dziecko nie potrzebuje dorosłego, żeby zacząć.",
  pomoc_wiek="osobista karta „moje sygnały i moje strategie” prowadzona przez dziecko",
  przebieg=[
   ("N — pomaga dziecku zapisać trzy sygnały ciała i trzy strategie.",
    "D — zapisuje albo rysuje swoje sygnały i strategie."),
   ("N — omawia, którą strategię wybrać przy którym sygnale.",
    "D — łączy sygnały ze strategiami na swojej karcie."),
   ("N — prowadzi zajęcia i nie reaguje na wczesne sygnały.",
    "D — rozpoznaje sygnał i mówi, z czego skorzysta."),
   ("N — potwierdza wybór i nie przejmuje kontroli.",
    "D — używa strategii samodzielnie."),
   ("N — po zajęciach sprawdza z dzieckiem, czy strategia zadziałała.",
    "D — ocenia strategię i poprawia swoją kartę.")]),
}
