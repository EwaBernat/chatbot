# -*- coding: utf-8 -*-
"""Materiały do wydruku wymagane przez konspekty — karty, paski, tablice.

Karta pomocy (`pomoce_a`, `pomoce_b`) mówi nauczycielowi, JAK pomoc ma wyglądać
i jak jej użyć. Część konspektów wymaga jednak samego materiału: kart do
wycięcia, planszy z piktogramami, tablicy do wypełnienia. Opis wtedy nie
wystarcza — nauczyciel ma to wydrukować, a nie odtwarzać z fotografii.

Arkusze składamy z biblioteki symboli (`symbole.py`), nie z rysunków robionych
pod jeden konspekt. Dzięki temu „proszę o pomoc” wygląda tak samo na tablicy
AAC, w planie dnia i na breloku — a to warunek, żeby symbol działał jak słowo.

Pięć rodzajów arkusza pokrywa wszystko, o co proszą konspekty:

  karty    siatka kart do wycięcia, linia cięcia dookoła każdej
  pasek    sekwencja z numerami — plan dnia, kolejność ubierania, kroki mycia
  tablica  komplet symboli w jednej ramce, do powieszenia bez rozcinania
  tabela   arkusz do wypełniania — dyżury, samoocena, rozliczenie tygodnia
  pola     puste pola z etykietami — karta projektu, umowa, karta próby
  etykiety karteczki z polem koloru i podpisem — pojemniki, znaczki dzieci

Trzy ostatnie nie potrzebują rysunków wcale i są w konspektach większością.

Rejestr jest kluczowany numerem konspektu, tak samo jak `POMOCE` — `build.py`
dokłada arkusze do sekcji VII, bez zmian w generatorze. Arkusz, którego symbole
nie są jeszcze narysowane, jest pomijany, więc dokumenty budują się poprawnie
na każdym etapie pracy.
"""

import base64

from symbole import KATALOG, SYMBOLE, jest, podpis

# nr konspektu → lista arkuszy (dict: tytul, wstep, rodzaj, …)
ARKUSZE = {
 "D2-06": [dict(
   tytul="Karty-zaproszenia",
   wstep="Wydrukuj, wytnij po linii i naklej na sztywniejszy karton. Miś wręcza dziecku jedną "
         "kartę, dziecko idzie z nią do stolika, na którym czeka ta właśnie zabawa. Po zabawie "
         "karta wraca do koszyka. Drukuj po dwa egzemplarze każdej, żeby starczyło na wybór "
         "z dwóch, i zostaw tylko te zabawy, które faktycznie masz przygotowane w sali.",
   rodzaj="karty", kolumny=3,
   symbole=["zabawa_klocki", "zabawa_ukladanka", "zabawa_rysowanie",
            "zabawa_lalki", "zabawa_auta", "zabawa_ksiazki"]),
 ],
 "D2-08": [dict(
   tytul="Pociąg dnia — wagony",
   wstep="Jedenaście wagonów całego dnia. Wytnij tylko te, które są w Waszym rytmie, i ułóż "
         "je w pasek od lewej do prawej na wysokości oczu dziecka. Zdjęty wagon znaczy "
         "„to już było” — dziecko samo je zdejmuje, bo to właśnie ta czynność uczy planu.",
   rodzaj="pasek",
   symbole=["dzien_przyjscie", "dzien_powitanie", "dzien_sniadanie", "dzien_zajecia",
            "dzien_zabawa", "dzien_sprzatanie", "dzien_spacer", "dzien_obiad",
            "dzien_lezakowanie", "dzien_podwieczorek", "dzien_powrot"]),
 ],

 "D8-34": [dict(
   tytul="Plan dnia do wycięcia",
   wstep="Te same jedenaście symboli w wersji do rozcięcia na osobne karty. Naklej na karton "
         "i zabezpiecz folią — plan dnia jest dotykany codziennie i bez tego rozpada się "
         "w dwa tygodnie. Zostaw z tyłu rzep, żeby kolejność dało się zmienić w dniu, "
         "w którym coś wypada.",
   rodzaj="karty", kolumny=4,
   symbole=["dzien_przyjscie", "dzien_powitanie", "dzien_sniadanie", "dzien_zajecia",
            "dzien_zabawa", "dzien_sprzatanie", "dzien_spacer", "dzien_obiad",
            "dzien_lezakowanie", "dzien_podwieczorek", "dzien_powrot"]),
 ],

 "B2-07": [dict(
   tytul="Plan dnia z ruchomym wskaźnikiem",
   wstep="Wydrukuj, wytnij i powieś w pasku. Wskaźnik zrób ze strzałki z kartonu na spinaczu — "
         "dziecko przesuwa go samo po każdej zmianie. O to chodzi w tym konspekcie: nie o to, "
         "żeby wiedziało, co będzie, tylko żeby samo zaznaczyło, że jedno się skończyło.",
   rodzaj="karty", kolumny=4,
   symbole=["dzien_przyjscie", "dzien_powitanie", "dzien_sniadanie", "dzien_zajecia",
            "dzien_zabawa", "dzien_sprzatanie", "dzien_spacer", "dzien_obiad",
            "dzien_lezakowanie", "dzien_podwieczorek", "dzien_powrot"]),
  dict(
   tytul="Karta „co robię, gdy skończę”",
   kp="Wydrukuj i powieś",
   wstep="Trzy zajęcia, które dziecko może zacząć samo, bez pytania. Wpisz te, które naprawdę "
         "są dostępne w sali — pusta obietnica na tej karcie kosztuje więcej niż jej brak. "
         "Zostaw czwarte pole puste i dopisz razem z dzieckiem to, co samo wybierze.",
   rodzaj="pola",
   pola=[("Mogę wziąć", 70), ("Mogę pójść do", 70),
         ("Mogę poprosić o", 70), ("Wymyśliliśmy razem", 70)]),
 ],

 "B1-04": [dict(
   tytul="Karta „skończone”",
   kp="Wydrukuj na tydzień",
   wstep="Jedna karta na dziecko na tydzień. Dziecko samo stawia znak w kolumnie dnia, "
         "kiedy skończy zadanie — podpis nauczyciela tylko potwierdza. Kolumna „co było "
         "trudne” jest ważniejsza niż liczba znaków; to z niej wynika, co zmienić w zadaniu.",
   rodzaj="tabela",
   naglowki=["Dzień", "Zadanie", "Skończone", "Co było trudne"],
   wiersze=["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]),
 ],

 "B6-27": [dict(
   tytul="Karta dyżurnego z samooceną",
   kp="Wydrukuj na tydzień",
   wstep="Dyżurny sam zaznacza uśmiech, kreskę albo smutną minę przy swoim zadaniu. "
         "Nie oceniaj tego zapisu — jest po to, żeby dziecko zobaczyło własną pracę, "
         "a nie żeby dostało za nią stopień. Rozmowa o różnicy zdań jest tu całą lekcją.",
   rodzaj="tabela",
   naglowki=["Dyżur", "Kto dziś", "Jak mi poszło", "Uwagi"],
   wiersze=["stołowy", "przyrodniczy", "biblioteczny", "porządkowy", ""]),
 ],

 "C6-27": [dict(
   tytul="Rozliczenie tygodniowe dyżurów",
   kp="Wydrukuj na tydzień",
   wstep="Podsumowanie na koniec tygodnia, prowadzone przez same dzieci. Kolumna „co "
         "poprawimy” ma zostać wypełniona zanim ustalicie dyżury na kolejny tydzień — "
         "inaczej rozliczenie zamienia się w sprawozdanie i przestaje cokolwiek zmieniać.",
   rodzaj="tabela",
   naglowki=["Dyżur", "Kto pełnił", "Co się udało", "Co poprawimy"],
   wiersze=["poniedziałek", "wtorek", "środa", "czwartek", "piątek", ""]),
 ],

 "U4-16": [dict(
   tytul="Siatka do wykresu grupy",
   kp="Wydrukuj w formacie A3",
   wstep="Każde dziecko wkleja jeden kwadracik nad swoją odpowiedzią — słupek rośnie na "
         "oczach grupy i nie trzeba go tłumaczyć. Wpisz pytanie tygodnia w nagłówku "
         "pierwszej kolumny, a odpowiedzi w kolejnych. Cztery odpowiedzi to maksimum, "
         "przy pięciu wykres przestaje być czytelny dla pięciolatka.",
   rodzaj="tabela",
   naglowki=["Pytanie tygodnia", "Odpowiedź 1", "Odpowiedź 2", "Odpowiedź 3"],
   wiersze=["", "", "", "", "", "", ""]),
 ],
 "D7-32": [dict(
   tytul="Lusterko emocji — karty",
   wstep="Zacznij od dwóch: radości i złości. Reszta czeka, aż te dwie będą rozpoznawane "
         "bez wahania — komplet ośmiu min na starcie sprawia, że dziecko zgaduje zamiast "
         "rozpoznawać. Wytnij, naklej na karton i trzymaj przy lustrze; dziecko wybiera "
         "kartę, robi tę minę do lustra i porównuje.",
   rodzaj="karty", kolumny=4,
   symbole=["emocja_radosc", "emocja_zlosc", "emocja_smutek", "emocja_spokoj"]),
 ],

 "B3-15": [dict(
   tytul="Karty pantomimy — emocje",
   wstep="Osiem min do pokazania bez słowa. Dziecko losuje kartę, pokazuje miną i postawą, "
         "reszta zgaduje. Karty trzymaj obrazkiem do dołu — podglądanie zamienia zabawę "
         "w czytanie podpisu. Osiem to komplet na całą grupę; do pierwszych prób wybierz cztery.",
   rodzaj="karty", kolumny=4,
   symbole=["emocja_radosc", "emocja_zlosc", "emocja_smutek", "emocja_strach",
            "emocja_spokoj", "emocja_zdziwienie", "emocja_duma", "emocja_zmeczenie"]),
 ],

 "U3-11": [dict(
   tytul="Karty emocji do odpowiedzi po angielsku",
   kp="Wydrukuj i powieś przy drzwiach",
   wstep="Cztery odpowiedzi na pytanie „how are you?”. Dziecko pokazuje kartę i mówi słowo — "
         "wskazanie wystarczy, słowo dochodzi później. Podpisz karty po angielsku ręcznie "
         "przy dziecku; własnoręczny podpis wiąże obrazek ze słowem mocniej niż druk.",
   rodzaj="tablica", kolumny=4,
   symbole=["emocja_radosc", "emocja_smutek", "emocja_zmeczenie", "emocja_spokoj"]),
 ],

 "U8-45": [dict(
   tytul="Karty nastrojów do muzyki",
   wstep="Dziecko słucha fragmentu i kładzie kartę, która pasuje do nastroju. Nie ma tu "
         "odpowiedzi błędnych — jeśli dwoje dzieci wybierze inne karty do tego samego "
         "utworu, to jest właśnie materiał na rozmowę, a nie pomyłka do poprawienia.",
   rodzaj="karty", kolumny=3,
   symbole=["emocja_radosc", "emocja_smutek", "emocja_spokoj",
            "emocja_zlosc", "emocja_zdziwienie", "emocja_zmeczenie"]),
 ],
 "D5-22": [dict(
   tytul="Kroki mycia rąk",
   kp="Wydrukuj i powieś nad umywalką",
   wstep="Konspekt liczy cztery kroki, tutaj są pokazane jako pięć: spłukiwanie i wycieranie "
         "rozdzielono, bo to właśnie na przejściu między nimi dziecko najczęściej odchodzi "
         "od umywalki z mokrymi rękami. Jeśli w Waszej łazience te dwie czynności zlewają "
         "się w jedną, wytnij ostatnie dwa kafle i sklej obok siebie jako jeden krok. "
         "Powieś na wysokości oczu dziecka, nie dorosłego.",
   rodzaj="pasek",
   symbole=["myje_woda", "myje_mydlo", "myje_pocieram", "myje_splukuje", "myje_wycieram"]),
 ],

 "B5-21": [dict(
   tytul="Instrukcja mycia rąk nad umywalką",
   kp="Wydrukuj i powieś nad umywalką",
   wstep="Ta sama pięciostopniowa instrukcja co w młodszej grupie, w jednej ramce do "
         "powieszenia bez rozcinania. Symbole są te same celowo — dziecko, które przeszło "
         "z grupy młodszej, rozpoznaje je bez uczenia się od nowa.",
   rodzaj="tablica", kolumny=5,
   symbole=["myje_woda", "myje_mydlo", "myje_pocieram", "myje_splukuje", "myje_wycieram"]),
 ],

 "D5-21": [dict(
   tytul="Plan toalety — trzy kroki",
   kp="Wydrukuj i powieś w toalecie",
   wstep="Trzy kroki, ani jednego więcej. Pełna sekwencja z rozbieraniem i ubieraniem "
         "przytłacza dziecko, które dopiero uczy się sygnału na czas; te trzy obrazki "
         "domykają to, o co dziecko najczęściej się potyka — wyjście z toalety bez "
         "spłukania i bez umycia rąk.",
   rodzaj="pasek",
   symbole=["toaleta_siusiu", "toaleta_spluczka", "toaleta_rece"]),
  dict(
   tytul="Symbol toalety na brelok",
   wstep="Ten sam obrazek co pierwszy kafel planu, do wycięcia i przypięcia przy dziecku. "
         "Dziecko pokazuje go, zanim zdąży powiedzieć — i o to chodzi: sygnał ma wyprzedzić "
         "słowo. Wydrukuj dwa, jeden zawsze ginie.",
   rodzaj="karty", kolumny=3,
   symbole=["toaleta_siusiu"]),
 ],

 "C5-23": [dict(
   tytul="Piktogramy rutyn higienicznych",
   kp="Wydrukuj i powieś w łazience",
   wstep="Komplet ośmiu obrazków: pięć kroków mycia rąk i trzy kroki toalety. Sześciolatek "
         "zna już te czynności — tablica nie uczy ich od nowa, tylko daje punkt odniesienia "
         "przy rozmowie o tym, co się pomija, kiedy się śpieszy.",
   rodzaj="tablica", kolumny=4,
   symbole=["myje_woda", "myje_mydlo", "myje_pocieram", "myje_splukuje",
            "myje_wycieram", "toaleta_siusiu", "toaleta_spluczka", "toaleta_rece"]),
 ],
 "D3-12": [dict(
   tytul="Tablica AAC — cztery pola",
   kp="Wydrukuj i powieś przy dziecku",
   wstep="Cztery prośby, od których zaczyna się komunikacja obrazkowa: pić, jeść, toaleta, "
         "pomoc. Cztery, nie osiem — tablica rozbudowuje się dopiero wtedy, gdy dziecko "
         "korzysta ze wszystkich czterech pól z własnej inicjatywy. Powieś tam, gdzie "
         "dziecko realnie przebywa, nie na drzwiach sali.",
   rodzaj="tablica", kolumny=4,
   symbole=["prosze_pic", "prosze_jesc", "prosze_toaleta", "prosze_pomoc"]),
  dict(
   tytul="Symbole na brelok",
   wstep="Te same cztery symbole do wycięcia i wpięcia na kółko przy dziecku. Tablica wisi "
         "w jednym miejscu, brelok idzie na spacer i do ogrodu — a prośba o pomoc najczęściej "
         "przychodzi właśnie tam, gdzie tablicy nie ma. Wydrukuj dwa komplety.",
   rodzaj="karty", kolumny=4,
   symbole=["prosze_pic", "prosze_jesc", "prosze_toaleta", "prosze_pomoc"]),
 ],

 "D5-25": [dict(
   tytul="Termometr samopoczucia — tablica sygnałów",
   kp="Wydrukuj i powieś nisko",
   wstep="Cztery stany, które dziecko najczęściej odczuwa, zanim potrafi je nazwać: "
         "zmęczenie, głód, ból i potrzeba ruchu. Wskazanie karty jest pełnoprawną "
         "odpowiedzią — nie domagaj się słowa, bo dziecko wtedy przestaje wskazywać.",
   rodzaj="tablica", kolumny=4,
   symbole=["emocja_zmeczenie", "prosze_jesc", "prosze_boli", "prosze_ruch"]),
  dict(
   tytul="Symbol „odpoczynek” na brelok",
   wstep="Karta, którą dziecko pokazuje, kiedy ma dość. Uszanuj ją bez negocjacji przez "
         "pierwsze tygodnie — symbol, po którym i tak trzeba zostać w kole, przestaje "
         "być używany po trzech razach.",
   rodzaj="karty", kolumny=3,
   symbole=["prosze_odpoczynek", "prosze_cisza"]),
 ],

 "D3-11": [dict(
   tytul="Obrazki czynności — weź, połóż, daj",
   wstep="Trzy polecenia w jednym przedmiocie: ta sama czerwona kostka na wszystkich "
         "trzech kartach. Zmienia się tylko czynność, więc dziecko nie zgaduje po obrazku, "
         "co ma zrobić — musi odczytać samo działanie. Do zabawy weź prawdziwą kostkę "
         "w tym samym kolorze.",
   rodzaj="karty", kolumny=3,
   symbole=["polecenie_wez", "polecenie_poloz", "polecenie_daj"]),
 ],

 "D3-15": [dict(
   tytul="Gesty na kartach — stop i chodź",
   wstep="Dwa gesty, które dziecko musi odczytać z ręki dorosłego, zanim zrozumie polecenie "
         "słowne. Pokaż gest, potem kartę — nigdy odwrotnie; karta ma potwierdzać to, "
         "co dziecko właśnie zobaczyło na Twojej dłoni.",
   rodzaj="karty", kolumny=2,
   symbole=["gest_stop", "gest_chodz"]),
 ],

 "B3-13": [dict(
   tytul="Piktogram „słucham — mówię”",
   kp="Wydrukuj i połóż na stoliku",
   wstep="Dwie karty kładzione na środku stolika. Kto mówi, ma przed sobą kartę „mówię”; "
         "reszta ma „słucham”. Karty wędrują między dziećmi po każdej wypowiedzi — samo "
         "ich przekładanie uczy zmiany ról lepiej niż przypominanie.",
   rodzaj="karty", kolumny=2,
   symbole=["gest_mowie", "gest_slucham"]),
 ],

 "B2-08": [dict(
   tytul="Karty strategii czekania",
   wstep="Trzy rzeczy, które można robić, czekając na swoją kolej: czekać spokojnie, "
         "oddychać, klaskać koledze. Czekanie jest tu czynnością, a nie brakiem czynności "
         "— i to jest cała różnica dla dziecka, które czekać nie umie.",
   rodzaj="karty", kolumny=3,
   symbole=["gest_czekam", "emocja_spokoj", "gest_brawo"]),
 ],
 # ——— obszar I ————————————————————————————————————————————————————
 "D1-04": [dict(
   tytul="Dachy do kolorowych domków",
   wstep="Wytnij i naklej na pudełka — czerwony dach na jedno, niebieski na drugie. "
         "Kolor ma być duży i jednolity; drobny znaczek w rogu pudełka trzylatek gubi "
         "z odległości wyciągniętej ręki. Zacznij od dwóch kolorów, trzeci dokładaj "
         "dopiero wtedy, gdy te dwa idą bezbłędnie.",
   rodzaj="etykiety", kolumny=2,
   etykiety=[("Czerwony domek", "#E8695A"), ("Niebieski domek", "#7FA8C9"),
             ("Żółty domek", "#F0C862"), ("Zielony domek", "#8FB79A")]),
 ],

 "D1-05": [dict(
   tytul="Karta „próbowałem sam”",
   kp="Wydrukuj na tydzień",
   wstep="Jedna karta na dziecko. Liczy się próba, nie powodzenie — dziecko stawia znak "
         "za samo sięgnięcie po pudełko, nawet jeśli go nie otworzyło. Kolumna „co pomogło” "
         "jest dla Pani, nie dla dziecka: po tygodniu widać z niej, które wsparcie można "
         "już wycofać.",
   rodzaj="tabela",
   naglowki=["Dzień", "Próbowałem sam", "Poprosiłem o pomoc", "Co pomogło"],
   wiersze=["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]),
 ],

 # ——— obszar II (uzupełnienie) ————————————————————————————————————
 "D2-07": [dict(
   tytul="Pasek „najpierw — potem”",
   kp="Wydrukuj i powieś przy stoliku",
   wstep="Dwa kroki, nigdy więcej. Na lewym polu to, co trzeba zrobić, na prawym to, "
         "co będzie potem. Trzylatek nie wytrzyma trzeciego pola — a dwa pola wystarczą, "
         "żeby „potem” przestało być groźbą i stało się obietnicą, którą widać.",
   rodzaj="pasek",
   symbole=["dzien_zajecia", "dzien_zabawa"]),
  dict(
   tytul="Pasek trzech kroków",
   wstep="Wersja dla dziecka, które radzi sobie z dwoma polami. Dokładaj trzecie dopiero "
         "wtedy, gdy dwa kroki idą bez przypominania przez cały tydzień.",
   rodzaj="pasek",
   symbole=["dzien_zajecia", "dzien_sprzatanie", "dzien_zabawa"]),
 ],

 "D2-10": [dict(
   tytul="Karta „idę na wyspę”",
   wstep="Karta, którą dziecko bierze samo, idąc w kąt wyciszenia. Nie odsyłaj dziecka "
         "z tą kartą — wtedy wyspa staje się karą i przestaje działać. Ma być wybierana, "
         "nie przydzielana. Wydrukuj dwie: jedną przy dziecku, jedną na wyspie.",
   rodzaj="karty", kolumny=2,
   symbole=["prosze_cisza", "emocja_spokoj"]),
 ],

 # ——— obszar III (uzupełnienie) ———————————————————————————————————
 "D3-13": [dict(
   tytul="Duże obrazki z jedną czynnością",
   wstep="Sześć obrazków, na każdym jedna czynność i nic poza nią. Dziecko mówi, co widzi — "
         "od jednego słowa („pije”) do zdania („chłopiec pije wodę”). Nie podpowiadaj "
         "zdania; podnoś poprzeczkę dopiero, gdy samo doda drugie słowo.",
   rodzaj="karty", kolumny=3,
   symbole=["prosze_pic", "myje_pocieram", "dzien_sprzatanie",
            "dzien_spacer", "dzien_lezakowanie", "dzien_zabawa"]),
 ],

 # ——— obszar IV ————————————————————————————————————————————————————
 "D4-18": [dict(
   tytul="Znaczniki odległości",
   wstep="Wytnij i połóż na podłodze jako kolejne przystanki dla piłki. Zaczynajcie od "
         "zielonego, blisko; czerwony dokładaj dopiero, gdy zielony wychodzi za każdym "
         "razem. Odległość rośnie kolorami, nie centymetrami — dziecko widzi wtedy postęp, "
         "zamiast go tylko słyszeć.",
   rodzaj="etykiety", kolumny=4,
   etykiety=[("Blisko", "#8FB79A"), ("Dalej", "#F0C862"),
             ("Jeszcze dalej", "#E0A05C"), ("Najdalej", "#E8695A")]),
 ],

 # ——— obszar VI ————————————————————————————————————————————————————
 "D6-26": [dict(
   tytul="Etykiety na pojemniki",
   wstep="Ten sam obrazek na pojemniku i na półce, na której pojemnik stoi. Dziecko odkłada "
         "wtedy zabawkę bez pytania, bo dopasowuje obrazek do obrazka, a nie zapamiętuje "
         "miejsce. Wydrukuj po dwa egzemplarze każdej — jeden na pojemnik, drugi na półkę.",
   rodzaj="karty", kolumny=3,
   symbole=["zabawa_klocki", "zabawa_ukladanka", "zabawa_lalki",
            "zabawa_auta", "zabawa_ksiazki", "zabawa_rysowanie"]),
 ],

 # ——— obszar VII ———————————————————————————————————————————————————
 "D7-29": [dict(
   tytul="Karta rund",
   kp="Wydrukuj na tydzień",
   wstep="Zapis, ile rund dziecko wytrzymało w zabawie z podawaniem. Zaznaczaj po zajęciach, "
         "nie w ich trakcie — notowanie przy dziecku przerywa dokładnie to, co mierzysz. "
         "Trzy rundy pod rząd przez tydzień to sygnał, żeby wydłużyć zabawę.",
   rodzaj="tabela",
   naglowki=["Dzień", "Ile rund", "Kto był obok", "Co przerwało"],
   wiersze=["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]),
 ],

 "D7-31": [dict(
   tytul="Mostek do przedszkola — trzy kroki",
   kp="Wydrukuj i powieś przy szatni",
   wstep="Ten sam rytuał każdego ranka, w tej samej kolejności. Powieś go w szatni, "
         "na wysokości oczu dziecka, i przechodźcie po nim palcem, zanim rodzic wyjdzie. "
         "Rytuał działa dlatego, że się nie zmienia — nie skracaj go w dni, kiedy się śpieszy.",
   rodzaj="pasek",
   symbole=["dzien_przyjscie", "dzien_powitanie", "dzien_zabawa"]),
 ],

 "D7-33": [dict(
   tytul="Karta POMOC",
   wstep="Jedna karta, jedno słowo. Dziecko podaje ją Pani zamiast płaczu albo szarpania "
         "za rękaw. Przez pierwsze dni reaguj na nią natychmiast i bez warunków — karta, "
         "po której trzeba jeszcze poczekać, przestaje być używana. Wydrukuj kilka: jedna "
         "przy dziecku, jedna w szatni, jedna w łazience.",
   rodzaj="karty", kolumny=2,
   symbole=["prosze_pomoc", "gest_stop"]),
 ],

 # ——— obszar VIII (uzupełnienie) ——————————————————————————————————
 "D8-36": [dict(
   tytul="Znaczki dzieci na poduszki",
   wstep="Każde dziecko dostaje swój kolor i trzyma go przez cały rok — ten sam znaczek "
         "na poduszce, w szatni i na kubku. Znaczek, który się zmienia, przestaje znaczyć "
         "„moje miejsce”. Dopisz imiona ręcznie przy dziecku.",
   rodzaj="etykiety", kolumny=4,
   etykiety=[("", "#E8695A"), ("", "#7FA8C9"), ("", "#8FB79A"), ("", "#F0C862"),
             ("", "#C9A0C0"), ("", "#E0A05C"), ("", "#8FA9B7"), ("", "#D2B48C")]),
  dict(
   tytul="Plan zajęcia z trzech obrazków",
   kp="Wydrukuj i powieś przy dywaniku",
   wstep="Trzy gotowe obrazki na jedno zajęcie: siadamy w kole, pracujemy przy stoliku, "
         "bawimy się. Powieś je przy dywaniku i przejdźcie po nich palcem, zanim usiądziecie. "
         "Trzylatek, który wie, że po pracy jest zabawa, siada na dywanik bez wyprowadzania "
         "za rękę.",
   rodzaj="pasek",
   symbole=["dzien_powitanie", "dzien_zajecia", "dzien_zabawa"]),
 ],

 "D8-37": [dict(
   tytul="Tabliczki do podpisania budowli",
   wstep="Dziecko dyktuje, Pani pisze — i to jest cała rzecz: dziecko widzi, że jego słowo "
         "zostaje. Postaw tabliczkę przy budowli i zostaw ją do końca dnia, żeby rodzic "
         "przeczytał ją przy dziecku.",
   rodzaj="pola",
   pola=[("To zbudował", 60), ("To jest", 60), ("Opowiedział o tym tak", 90)]),
 ],

 # ——— obszar IX ————————————————————————————————————————————————————
 "D9-39": [dict(
   tytul="Plan uroczystości w obrazkach",
   kp="Wydrukuj i powieś dzień wcześniej",
   wstep="Trzy obrazki w kolejności z konspektu: piosenka, laurka, poczęstunek. Pokaż "
         "dziecku plan dzień wcześniej i przejdźcie po nim palcem — dla trzylatka "
         "uroczystość jest przede wszystkim dniem, w którym wszystko wygląda inaczej, "
         "i to ta zmiana, a nie hałas, najczęściej go przeciąża.",
   rodzaj="pasek",
   symbole=["swieto_wystep", "zabawa_rysowanie", "dzien_podwieczorek"]),
 ],

 "D9-40": [dict(
   tytul="Karta par na spacer",
   kp="Wydrukuj przed wyjściem",
   wstep="Pary ustalone przed wyjściem, nie w drzwiach. Dziecko, które wie, z kim idzie, "
         "nie musi tego wywalczyć na schodach. Kolumna „zmiana” jest po to, żeby zapisać, "
         "kto z kim nie może iść — i żeby nie trzeba było tego odkrywać dwa razy.",
   rodzaj="tabela",
   naglowki=["Para", "Kto", "Z kim", "Zmiana"],
   wiersze=["1", "2", "3", "4", "5", "6"]),
 ],

 "D9-42": [dict(
   tytul="Dwa obrazki do wyboru po czytaniu",
   wstep="Po przeczytaniu dziecko wskazuje jedną z dwóch kart. To pierwsza forma opinii, "
         "na jaką trzylatka stać — i pełnoprawna. Nie dopytuj „dlaczego”, dopóki dziecko "
         "samo nie zacznie dodawać słowa; pytanie o powód zamyka wskazywanie.",
   rodzaj="karty", kolumny=2,
   symbole=["emocja_radosc", "emocja_smutek"]),
 ],
 "D5-24": [dict(
   tytul="Kolejność ubierania",
   kp="Wydrukuj i powieś w szatni",
   wstep="Siedem kroków w kolejności, która wybacza błędy: najpierw to, co idzie od dołu. "
         "Dziecko, które zaczyna od butów, nie założy już spodni — a przy takim planie "
         "nie musi tego odkrywać co dzień od nowa. Wytnij tylko te części, które dziecko "
         "faktycznie zakłada danego dnia, i ułóż je od lewej.",
   rodzaj="pasek",
   symbole=["ubior_majtki", "ubior_skarpetki", "ubior_spodnie", "ubior_koszulka",
            "ubior_sweter", "ubior_kurtka", "ubior_buty"]),
  dict(
   tytul="Części garderoby do wycięcia",
   wstep="Te same siedem obrazków w wersji do rozcięcia. Dziecko układa z nich kolejność "
         "samo, zanim zacznie się ubierać — układanie planu jest osobnym ćwiczeniem "
         "i warto dać mu chwilę, zamiast robić to w biegu przy wyjściu na dwór.",
   rodzaj="karty", kolumny=4,
   symbole=["ubior_majtki", "ubior_skarpetki", "ubior_spodnie", "ubior_koszulka",
            "ubior_sweter", "ubior_kurtka", "ubior_buty"]),
 ],

 "D2-09": [dict(
   tytul="Nasze trzy zasady",
   kp="Wydrukuj i powieś nisko",
   wstep="Trzy zasady, wszystkie powiedziane wprost, co robimy — nie czego nie wolno. "
         "„Nie krzyczymy” nie mówi trzylatkowi, co ma zrobić zamiast; „mówimy spokojnie” "
         "mówi. Powieś na wysokości oczu dziecka i wskazuj obrazek zamiast przypominać "
         "słowami.",
   rodzaj="tablica", kolumny=3,
   symbole=["gest_mowie", "dzien_zabawa", "dzien_sprzatanie"]),
 ],

 "D7-30": [dict(
   tytul="Tablica podań",
   kp="Wydrukuj na tydzień",
   wstep="Zapis, komu dziecko podało misia i ile razy. Wypełniaj po zajęciach — chodzi "
         "o to, żeby zobaczyć, czy krąg dzieci, do których dziecko podaje, się poszerza. "
         "Jeśli przez tydzień jest to wciąż ta sama jedna osoba, posadź obok kogoś nowego, "
         "zamiast zachęcać słowami.",
   rodzaj="tabela",
   naglowki=["Dzień", "Komu podał", "Ile razy", "Czy patrzył w oczy"],
   wiersze=["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]),
 ],
 "D4-20": [dict(
   tytul="Karty-obrazki ruchów",
   wstep="Sześć ruchów do losowania przy muzyce. Karta zastępuje polecenie słowne, więc "
         "dziecko, które nie nadąża za instrukcją, i tak wie, co robić. Zaczynajcie od "
         "trzech kart; przy sześciu trzylatek przestaje wybierać, a zaczyna powtarzać "
         "ostatnią.",
   rodzaj="karty", kolumny=3,
   symbole=["ruch_bieg", "ruch_skok", "ruch_czworaki",
            "ruch_wspinanie", "ruch_rzut", "ruch_rownowaga"]),
 ],
 "D3-14": [dict(
   tytul="Ściany kostki pytań",
   wstep="Trzy pytania, po dwie ściany każde — wydrukuj dwa egzemplarze arkusza i naklej "
         "na sześcian z kartonu, tak żeby każde pytanie wypadało dwa razy. Przy trzech "
         "pytaniach na sześciu ścianach dziecko trafia w znajomy symbol za każdym rzutem "
         "i nie zniechęca się do zabawy.",
   rodzaj="karty", kolumny=3,
   symbole=["pytanie_kto", "pytanie_co", "pytanie_gdzie"]),
  dict(
   tytul="Ilustracje sytuacyjne do pytań",
   wstep="Sześć scen, w których widać osobę, czynność i miejsce naraz — o to chodzi, żeby "
         "na każde z trzech pytań dało się odpowiedzieć z tego samego obrazka. Kładź jeden "
         "obrazek i rzucajcie kostką kilka razy pod rząd; zmiana obrazka przy każdym rzucie "
         "gubi to, czego konspekt uczy.",
   rodzaj="karty", kolumny=3,
   symbole=["dzien_sniadanie", "dzien_zabawa", "dzien_spacer",
            "dzien_sprzatanie", "dzien_zajecia", "dzien_powitanie"]),
 ],

 "D6-27": [dict(
   tytul="Tabliczka szatni — kapcie, kubek, worek",
   kp="Wydrukuj i powieś w szatni",
   wstep="Trzy rzeczy, które dziecko ma znaleźć i odłożyć samo. Ten sam obrazek powtórz "
         "na półce, na haczyku i na kubku — dziecko dopasowuje wtedy obrazek do obrazka "
         "i nie musi pamiętać miejsca. To jest cała mechanika tego konspektu.",
   rodzaj="tablica", kolumny=3,
   symbole=["przedmiot_kapcie", "przedmiot_kubek", "przedmiot_worek"]),
  dict(
   tytul="Znaczki rozpoznawcze dzieci",
   wstep="Jeden kolor na dziecko, ten sam przez cały rok i w każdym miejscu: półka, "
         "haczyk, kubek, poduszka. Znaczek, który się zmienia albo jest inny w szatni "
         "niż w sali, przestaje znaczyć „moje”. Dopisz imiona ręcznie.",
   rodzaj="etykiety", kolumny=4,
   etykiety=[("", "#E8695A"), ("", "#7FA8C9"), ("", "#8FB79A"), ("", "#F0C862"),
             ("", "#C9A0C0"), ("", "#E0A05C"), ("", "#8FA9B7"), ("", "#D2B48C")]),
 ],

 "D6-28": [dict(
   tytul="Plan dyżuru: serwetki, potem kubki",
   kp="Wydrukuj i powieś przy stolikach",
   wstep="Dwa kroki w stałej kolejności. Serwetki idą pierwsze, bo są lekkie i płaskie — "
         "kubek postawiony na gołym stole trzeba potem podnieść, żeby wsunąć serwetkę, "
         "a to dla trzylatka jeden ruch za dużo. Trzeci krok dokładaj dopiero po dwóch "
         "tygodniach bez przypominania.",
   rodzaj="pasek",
   symbole=["przedmiot_serwetka", "przedmiot_kubek"]),
 ],

 "D9-41": [dict(
   tytul="Zasady placu zabaw",
   kp="Wydrukuj i powieś przy wyjściu",
   wstep="Trzy zasady pokazane jako czynności, nie zakazy. Przejdźcie po tablicy przed "
         "każdym wyjściem — przypomnienie przy drzwiach działa, przypomnienie krzyczane "
         "z drugiego końca placu już nie. Zasady dotyczą zjeżdżalni, bo tam dzieje się "
         "większość zderzeń.",
   rodzaj="tablica", kolumny=3,
   symbole=["plac_schodki", "gest_czekam", "plac_zjezdzalnia"]),
 ],
 "D1-02": [dict(
   tytul="Naklejki-łapki małpki",
   wstep="Łapki do wycięcia i naklejenia tam, gdzie dziecko ma stanąć albo położyć rękę. "
         "Trzylatek naśladuje ruch łatwiej, gdy widzi, dokąd ma trafić — łapka na podłodze "
         "robi za polecenie, którego nie trzeba powtarzać. Wydrukuj kilka arkuszy, bo "
         "naklejone na podłodze zużywają się w tydzień.",
   rodzaj="karty", kolumny=3,
   symbole=["slad_lapka", "slad_stopa_lewa", "slad_stopa_prawa"]),
 ],

 "D1-03": [dict(
   tytul="Żetony-diamenty",
   wstep="Diament za każdą minutę wytrzymaną przy klepsydrze. Wytnij i naklejaj na kartę "
         "dziecka od razu, przy nim — żeton wręczony po zajęciach nie łączy się już "
         "z tym, co dziecko zrobiło. Wydrukuj dwa arkusze na tydzień.",
   rodzaj="karty", kolumny=4,
   symbole=["zeton_diament"]),
  dict(
   tytul="Karta skarbów dziecka",
   kp="Wydrukuj na tydzień",
   wstep="Miejsce na naklejane diamenty, jedna karta na dziecko. Kolumna „ile minut” jest "
         "ważniejsza od liczby żetonów — to z niej widać, czy czas czekania rośnie, "
         "czy stoi w miejscu.",
   rodzaj="tabela",
   naglowki=["Dzień", "Ile minut", "Diamenty", "Co pomogło"],
   wiersze=["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]),
 ],

 "D4-16": [dict(
   tytul="Zwierzęta na ścieżkę",
   wstep="Cztery zwierzęta, cztery sposoby poruszania się: zając skacze, lis biegnie, "
         "niedźwiedź idzie na czworakach, żaba skacze z przysiadu. Połóż karty wzdłuż "
         "ścieżki — dziecko zmienia ruch przy każdej karcie i nie musi pamiętać instrukcji.",
   rodzaj="karty", kolumny=4,
   symbole=["zwierze_zajac", "zwierze_lis", "zwierze_niedzwiedz", "zwierze_zaba"]),
  dict(
   tytul="Ślady na podłogę",
   wstep="Łapki i stopy do wycięcia i rozłożenia jako ścieżka. Rozstaw je na tyle blisko, "
         "żeby dziecko trafiało bez wysiłku — ścieżka, z której się spada, przestaje "
         "zachęcać po dwóch próbach. Odległość zwiększaj dopiero, gdy przechodzi ją "
         "bez patrzenia pod nogi.",
   rodzaj="karty", kolumny=3,
   symbole=["slad_lapka", "slad_stopa_lewa", "slad_stopa_prawa"]),
 ],

 "D4-17": [dict(
   tytul="Stópki na schodki",
   wstep="Lewa i prawa stopa do naklejenia na kolejne stopnie, na przemian. Dziecko stawia "
         "wtedy nogi naprzemiennie, zamiast dostawiać drugą do pierwszej — i o to chodzi "
         "w tym konspekcie. Wydrukuj tyle par, ile macie stopni, i naklej blisko krawędzi, "
         "żeby dziecko widziało je patrząc w dół.",
   rodzaj="karty", kolumny=2,
   symbole=["slad_stopa_lewa", "slad_stopa_prawa"]),
 ],

 "D8-35": [dict(
   tytul="Zdjęcia ról na ścianę kącika",
   kp="Wydrukuj i powieś w kąciku",
   wstep="Cztery role do powieszenia tam, gdzie się je odgrywa: kucharz przy kuchence, "
         "kierowca przy garażu. Obrazek na ścianie podpowiada rolę dziecku, które nie "
         "wymyśli jej samo, a reszcie mówi, kim ono teraz jest — bez tego zabawa "
         "w role rozpada się po minucie.",
   rodzaj="tablica", kolumny=4,
   symbole=["zawod_kucharz", "zawod_kierowca", "zabawa_lalki", "zabawa_auta"]),
 ],

 "D8-38": [dict(
   tytul="Obrazek zasady zabawy",
   kp="Wydrukuj i połóż na środku koła",
   wstep="Trzy obrazki na środek chusty: czekam na swoją kolej, słucham sygnału, "
         "bawimy się razem. Połóż je tam, gdzie wszyscy je widzą, i wskazuj zamiast "
         "przerywać zabawę słowami.",
   rodzaj="tablica", kolumny=3,
   symbole=["gest_czekam", "gest_slucham", "dzien_zabawa"]),
  dict(
   tytul="Znaczniki miejsc w kole",
   wstep="Kolorowe krążki pod stopy, żeby każde dziecko wiedziało, gdzie usiąść. "
         "Ten sam kolor co znaczek dziecka w szatni — wtedy nie trzeba tłumaczyć, "
         "które miejsce jest czyje.",
   rodzaj="etykiety", kolumny=4,
   etykiety=[("", "#E8695A"), ("", "#7FA8C9"), ("", "#8FB79A"), ("", "#F0C862"),
             ("", "#C9A0C0"), ("", "#E0A05C"), ("", "#8FA9B7"), ("", "#D2B48C")]),
 ],
 "C1-01": [dict(
   tytul="Kartoniki łączników",
   kp="Wydrukuj i wytnij",
   wstep="Cztery słowa, które zamieniają wyliczankę zdarzeń w opowieść. Dziecko kładzie "
         "kartonik przed każdym zdaniem i mówi od niego. Czwarty — „dlatego” — dokładaj "
         "dopiero wtedy, gdy trzy pierwsze wchodzą bez przypominania; to on jest tu "
         "właściwym celem.",
   rodzaj="etykiety", kolumny=4,
   etykiety=[("NAJPIERW", "#8FB79A"), ("POTEM", "#7FA8C9"),
             ("NA KOŃCU", "#F0C862"), ("DLATEGO", "#E8695A")]),
 ],

 "C1-04": [dict(
   tytul="Karty cyfr 1–10",
   kp="Wydrukuj i wytnij",
   wstep="Cyfry do dokładania po przeliczeniu, nie zamiast niego. Dziecko najpierw odlicza "
         "żetony, dopiero potem kładzie kartę z cyfrą — w tej kolejności cyfra opisuje "
         "czynność, a nie ją zastępuje.",
   rodzaj="etykiety", kolumny=5,
   etykiety=[("1", "#8FB79A"), ("2", "#7FA8C9"), ("3", "#F0C862"), ("4", "#E8695A"),
             ("5", "#C9A0C0"), ("6", "#8FB79A"), ("7", "#7FA8C9"), ("8", "#F0C862"),
             ("9", "#E8695A"), ("10", "#C9A0C0")]),
 ],

 "C2-06": [dict(
   tytul="Tablica planu — trzy pola",
   kp="Wydrukuj w formacie A3",
   wstep="Trzy pola na etapy zadania i miejsce na klips przy każdym. Dziecko układa plan "
         "przed rozpoczęciem pracy i odhacza etapy samo. Nie wpisuj etapów za dziecko — "
         "wtedy plan wraca do Pani głowy, a miał zostać w jego.",
   rodzaj="pola",
   pola=[("Krok 1 — najpierw", 120), ("Krok 2 — potem", 120), ("Krok 3 — na końcu", 120)]),
 ],

 "C2-09": [dict(
   tytul="Karty dni tygodnia",
   kp="Wydrukuj i powieś przy kalendarzu",
   wstep="Siedem kart w stałych kolorach — ten sam kolor dnia przez cały rok. Sześciolatek "
         "zapamiętuje kolejność szybciej po kolorze niż po nazwie, a nazwa dochodzi sama "
         "przy codziennym wskazywaniu.",
   rodzaj="etykiety", kolumny=4,
   etykiety=[("PONIEDZIAŁEK", "#E8695A"), ("WTOREK", "#E0A05C"), ("ŚRODA", "#F0C862"),
             ("CZWARTEK", "#8FB79A"), ("PIĄTEK", "#7FA8C9"), ("SOBOTA", "#C9A0C0"),
             ("NIEDZIELA", "#8FA9B7")]),
  dict(
   tytul="Oś czasu — wczoraj, dziś, jutro",
   wstep="Trzy pola do wypełniania codziennie: zdjęcie z wczoraj, plan na dziś, zapowiedź "
         "na jutro. Bez zdjęcia z wczoraj „wczoraj” zostaje dla dziecka słowem, a nie "
         "wspomnieniem — to pole jest tu najważniejsze.",
   rodzaj="pola",
   pola=[("Wczoraj", 110), ("Dziś", 110), ("Jutro", 110)]),
 ],

 "C3-14": [dict(
   tytul="Tabliczki do głosowania",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Tak i nie na jednym kartoniku, po obu stronach — dziecko obraca tabliczkę zamiast "
         "wybierać z dwóch. Głosowanie odbywa się przed rozmową, a nie po niej: chodzi "
         "o zdanie własne, nie o powtórzenie po koledze.",
   rodzaj="etykiety", kolumny=2,
   etykiety=[("TAK", "#8FB79A"), ("NIE", "#E8695A")]),
  dict(
   tytul="Tablica argumentów",
   kp="Wydrukuj w formacie A3",
   wstep="Dwie kolumny na argumenty za i przeciw, zapisywane przez Panią w trakcie debaty. "
         "Przeczytajcie je na koniec w całości — sześciolatek wtedy słyszy, że obie strony "
         "miały powody, i to jest cała nauka z tego konspektu.",
   rodzaj="tabela",
   naglowki=["Temat debaty", "Argumenty za", "Argumenty przeciw"],
   wiersze=["", "", "", "", "", ""]),
 ],

 "C7-33": [dict(
   tytul="Karty sposobów pomagania",
   wstep="Trzy sposoby do wyboru: podpowiem, podam, pocieszę. Dziecko wybiera kartę, zanim "
         "zacznie pomagać — sam wybór jest tu ćwiczeniem, bo bez niego sześciolatek pomaga "
         "przez zrobienie za kolegę.",
   rodzaj="karty", kolumny=3,
   symbole=["gest_mowie", "polecenie_daj", "prosze_pomoc"]),
 ],

 "C8-37": [dict(
   tytul="Tablica reguł w obrazkach",
   kp="Wydrukuj i powieś przy stole do gry",
   wstep="Trzy reguły, do których odwołuje się sędzia-dziecko: czekam na kolej, słucham "
         "rozstrzygnięcia, gratuluję. Wskazywanie tablicy zamiast własnego zdania jest "
         "warunkiem, żeby dziecko-sędzia było w ogóle słuchane.",
   rodzaj="tablica", kolumny=3,
   symbole=["gest_czekam", "gest_slucham", "gest_brawo"]),
  dict(
   tytul="Tabela turniejowa",
   kp="Wydrukuj na turniej",
   wstep="Kolumna „fair play” jest tu ważniejsza od kolumny z wynikiem i tak ją traktujcie "
         "przy podsumowaniu. Medale przyznają dzieci, nie Pani.",
   rodzaj="tabela",
   naglowki=["Zespół", "Gra", "Wynik", "Fair play"],
   wiersze=["", "", "", "", "", ""]),
 ],

 "C9-43": [dict(
   tytul="Etykiety na pojemniki do segregacji",
   kp="Wydrukuj i naklej na pojemniki",
   wstep="Kolory frakcji zgodne z systemem krajowym — ten sam, który dziecko widzi w domu "
         "i na ulicy. Etykieta w przedszkolu w innym kolorze niż w domu uczy dwóch "
         "sprzecznych rzeczy naraz.",
   rodzaj="etykiety", kolumny=4,
   etykiety=[("PAPIER", "#7FA8C9"), ("SZKŁO", "#8FB79A"),
             ("METALE I TWORZYWA", "#F0C862"), ("BIO", "#8B6B4A")]),
  dict(
   tytul="Karta zużycia wody",
   kp="Wydrukuj na tydzień",
   wstep="Zapis odczytów z licznika przy umywalce. Liczba robi tu całą robotę — rozmowa "
         "o oszczędzaniu bez odczytu jest dla sześciolatka apelem, a z odczytem staje się "
         "obserwacją.",
   rodzaj="tabela",
   naglowki=["Dzień", "Odczyt rano", "Odczyt po południu", "Co zmieniliśmy"],
   wiersze=["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]),
 ],

 # ——— szóstki: materiał do pozostałych konspektów ————————————————————
 "C1-02": [dict(
   tytul="Karta czytania sylabami",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Kolumny wypełnia dziecko, nie Pani. Sylaby wpisujemy dopiero po ich odczytaniu, "
         "a cały wyraz na końcu — w tej kolejności zapis jest zapamiętaniem tego, co "
         "dziecko właśnie przeczytało, a nie ściągawką, z której czyta.",
   rodzaj="tabela",
   naglowki=["Obrazek", "Pierwsza sylaba", "Druga sylaba", "Cały wyraz"],
   wiersze=["", "", "", "", "", ""]),
 ],

 "C1-03": [dict(
   tytul="Karta trzech faktur litery",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Ta sama litera trzy razy, za każdym razem inaczej: palcem w piasku, mazakiem po "
         "folii, ołówkiem w liniaturze. Kolumny odhaczamy dopiero po wykonaniu, a nie "
         "z góry — dziecko ma widzieć, że droga do liniatury prowadzi przez rękę.",
   rodzaj="tabela",
   naglowki=["Litera", "Palcem w piasku", "Po folii", "W liniaturze"],
   wiersze=["a", "e", "o", "m", "t", "l", "i", "u"]),
 ],

 "C1-05": [dict(
   tytul="Karta hipotezy",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Kolumnę „jak myślę” wypełniamy przed pomiarem i nie zmieniamy jej potem — to jest "
         "cała treść tego konspektu. Rozbieżność między przypuszczeniem a wynikiem nie jest "
         "błędem dziecka, tylko momentem, w którym uczy się sprawdzać.",
   rodzaj="tabela",
   naglowki=["Przedmiot", "Jak myślę", "Wynik pomiaru", "Czy się zgadzało"],
   wiersze=["", "", "", "", ""]),
 ],

 "C2-07": [dict(
   tytul="Kartoniki sygnałowe do cichej pracy",
   kp="Wydrukuj po komplecie na dziecko",
   wstep="Trzy kartoniki, które dziecko stawia przy sobie zamiast wołać. Zielony znaczy "
         "„pracuję”, żółty „utknąłem, poczekam”, niebieski „skończyłem”. Warunek działania "
         "jest jeden: przy żółtym Pani podchodzi, a nie odpowiada z drugiego końca sali.",
   rodzaj="etykiety", kolumny=3,
   etykiety=[("PRACUJĘ SAM", "#8FB79A"), ("POTRZEBUJĘ POMOCY", "#F0C862"),
             ("SKOŃCZYŁEM", "#7FA8C9")]),
 ],

 "C2-08": [dict(
   tytul="Karta dobrego gracza",
   kp="Wydrukuj i powieś przy grach",
   wstep="Cztery pola do wypełnienia raz, wspólnie, i powieszenia przy półce z grami. "
         "Ostatnie pole — o tym, co czuję po przegranej — wypełnia każde dziecko samo "
         "i to ono jest tu materiałem do rozmowy, nie trzy pierwsze.",
   rodzaj="pola",
   pola=[("Gram do końca, bo", 70), ("Wygranemu mówię", 70),
         ("Kiedy przegram, mogę", 70), ("Po przegranej czuję", 80)]),
 ],

 "C2-10": [dict(
   tytul="Karty strategii na trudne",
   kp="Wydrukuj, wytnij i włóż do skrzynki",
   wstep="Cztery wyjścia z sytuacji „nie umiem”. Dziecko wyciąga kartę samo, kiedy utknie — "
         "nie podpowiadamy której. Wybór strategii jest tu ćwiczeniem, a nie ozdobą: "
         "dopiero on zamienia bezradność w decyzję.",
   rodzaj="etykiety", kolumny=2,
   etykiety=[("ODETCHNIJ GŁĘBOKO", "#7FA8C9"), ("ZRÓB PRZERWĘ", "#8FB79A"),
             ("POPROŚ O POMOC", "#F0C862"), ("PODZIEL NA CZĘŚCI", "#C9A0C0")]),
 ],

 "C3-11": [dict(
   tytul="Karta obserwacji mowy",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Arkusz do prowadzenia przez cały rok, jedna kolumna na etap: głoska sama, "
         "w wyrazie, w zdaniu. Nie przeskakujemy kolumn — głoska poprawna w izolacji, "
         "a znikająca w zdaniu, to normalna kolejność, nie regres.",
   rodzaj="tabela",
   naglowki=["Głoska", "Sama", "W wyrazie", "W zdaniu"],
   wiersze=["sz", "ż", "cz", "dż", "r", "l", "s", "z", "c"]),
 ],

 "C3-12": [dict(
   tytul="Karta analizy głoskowej",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Pod każdym obrazkiem tyle kratek, ile dziecko usłyszy głosek — kładzie w nich "
         "żetony, zanim cokolwiek zapisze. Liczba żetonów jest odpowiedzią; zapis przychodzi "
         "później i nie jest tu wcale konieczny.",
   rodzaj="tabela",
   naglowki=["Obrazek", "Ile głosek", "Pierwsza", "Ostatnia"],
   wiersze=["", "", "", "", "", ""]),
 ],

 "C3-13": [dict(
   tytul="Mapa bajki — cztery pola",
   kp="Wydrukuj w formacie A3",
   wstep="Cztery pola na cztery zdania opowieści. Dziecko rysuje albo dyktuje po jednym "
         "zdaniu do pola — nie więcej, bo ograniczenie do jednego zdania jest tu całym "
         "ćwiczeniem. Drugie opowiadanie tej samej bajki idzie na drugi arkusz.",
   rodzaj="pola",
   pola=[("Kto i gdzie", 95), ("Co się stało", 95),
         ("Co zrobił bohater", 95), ("Jak się skończyło", 95)]),
 ],

 "C3-15": [dict(
   tytul="Karty poleceń po angielsku",
   kp="Wydrukuj, wytnij i pokaż maskotce",
   wstep="Sześć poleceń, które dziecko wykonuje ruchem, nie tłumaczy. Karta jest dla Pani, "
         "nie dla dziecka — pokazujemy ją maskotce, a dziecko reaguje na usłyszane zdanie. "
         "Odpowiedzią jest ruch; powtarzanie słów jest dobrowolne.",
   rodzaj="etykiety", kolumny=3,
   etykiety=[("STAND UP", "#8FB79A"), ("SIT DOWN", "#7FA8C9"), ("CLAP YOUR HANDS", "#F0C862"),
             ("JUMP", "#E8695A"), ("TURN AROUND", "#C9A0C0"), ("LISTEN", "#8FA9B7")]),
 ],

 "C4-16": [dict(
   tytul="Karty ćwiczeń naprzemiennych",
   kp="Wydrukuj, wytnij i włóż do woreczka",
   wstep="Sześć ćwiczeń do losowania. Dziecko wyciąga kartę i wykonuje ruch bez pokazywania "
         "przez dorosłego — nazwa ma wystarczyć. Do momentu, w którym wystarcza, pokazujemy "
         "razem, ale nazwę wypowiadamy zawsze pierwszą.",
   rodzaj="karty", kolumny=3,
   symbole=["ruch_bieg", "ruch_skok", "ruch_rownowaga",
            "ruch_czworaki", "ruch_rzut", "ruch_wspinanie"]),
 ],

 "C4-17": [dict(
   tytul="Trzy rzeczy przy stoliku",
   kp="Wydrukuj i powieś nad stolikami",
   wstep="Trzy hasła zamiast upominania. Kiedy dziecko siedzi krzywo, wskazujemy tablicę "
         "i milczymy — sprawdzenie własnej pozycji jest tym, czego się uczy. Komentarz "
         "słowny zabiera mu tę pracę.",
   rodzaj="etykiety", kolumny=3,
   etykiety=[("STOPY NA PODŁODZE", "#8FB79A"), ("PLECY PROSTE", "#7FA8C9"),
             ("OBIE RĘCE NA STOLE", "#F0C862")]),
 ],

 "C4-18": [dict(
   tytul="Karta nacisku ołówka",
   kp="Wydrukuj i podłóż kalkę",
   wstep="Pod arkusz wkładamy kalkę. Po skończeniu oglądamy odbicie razem z dzieckiem: "
         "przebite miejsca to za mocno, ledwo widoczne — za słabo. Kalka mówi to lepiej "
         "niż Pani, bo dziecko widzi ślad własnej ręki, a nie słyszy ocenę.",
   rodzaj="tabela",
   naglowki=["Ćwiczenie", "Za mocno", "W sam raz", "Za słabo"],
   wiersze=["kreski pionowe", "kreski poziome", "fale", "pętelki", "szlaczek", "mój podpis"]),
 ],

 "C4-19": [dict(
   tytul="Karty zapięć do ćwiczenia",
   kp="Wydrukuj, wytnij i powieś przy szatni",
   wstep="Kolejność ćwiczenia jest tu ważniejsza niż same karty: najpierw na tablicy, "
         "potem na cudzym bucie, na końcu na własnej kurtce. Karty pokazują, o którą część "
         "ubrania chodzi — samo zapinanie ćwiczy się na rzeczach, nie na obrazku.",
   rodzaj="karty", kolumny=3,
   symbole=["ubior_kurtka", "ubior_buty", "ubior_sweter",
            "ubior_koszulka", "ubior_spodnie", "ubior_skarpetki"]),
 ],

 "C4-20": [dict(
   tytul="Karty nastroju muzyki",
   kp="Wydrukuj, wytnij i rozłóż na dywanie",
   wstep="Sześć określeń, którymi dziecko nazywa to, co słyszy, zanim zacznie się ruszać. "
         "Nie ma tu odpowiedzi poprawnej — jeśli dwoje dzieci wskaże różne karty przy tym "
         "samym utworze, to jest właśnie to, o co chodzi.",
   rodzaj="etykiety", kolumny=3,
   etykiety=[("SZYBKO", "#E8695A"), ("WOLNO", "#7FA8C9"), ("GŁOŚNO", "#E0A05C"),
             ("CICHO", "#8FA9B7"), ("WESOŁO", "#F0C862"), ("SPOKOJNIE", "#8FB79A")]),
 ],

 "C5-21": [dict(
   tytul="Kolejność ubierania — pasek",
   kp="Wydrukuj i powieś w szatni nisko",
   wstep="Siedem kroków w stałej kolejności, na wysokości oczu dziecka. Pasek zastępuje "
         "podpowiedź słowną: zamiast mówić „teraz spodnie”, wskazujemy pasek. Dziecko "
         "sprawdza kolejny obrazek samo i to jest cała samodzielność, o którą tu chodzi.",
   rodzaj="pasek",
   symbole=["ubior_majtki", "ubior_skarpetki", "ubior_koszulka", "ubior_spodnie",
            "ubior_sweter", "ubior_buty", "ubior_kurtka"]),
 ],

 "C5-22": [dict(
   tytul="Tablica przy stole",
   kp="Wydrukuj i powieś przy półmiskach",
   wstep="Cztery symbole tego, co dziecko robi przy stole samo. Ten sam obrazek co na "
         "tablicy AAC i w planie dnia — dziecko korzystające z komunikacji obrazkowej ma "
         "widzieć wszędzie ten sam znak, inaczej przestaje on być słowem.",
   rodzaj="tablica", kolumny=4,
   symbole=["przedmiot_kubek", "przedmiot_serwetka", "prosze_jesc", "prosze_pic"]),
 ],

 "C5-24": [dict(
   tytul="Cztery kroki przy przejściu",
   kp="Wydrukuj i powieś przy drzwiach",
   wstep="Cztery hasła powtarzane przed każdym wyjściem, zawsze w tej samej kolejności. "
         "Powtarzamy je razem z dzieckiem także wtedy, gdy zna je na pamięć — automatyzm "
         "jest tu celem, a nie znudzeniem.",
   rodzaj="etykiety", kolumny=2,
   etykiety=[("ZATRZYMAJ SIĘ", "#E8695A"), ("POPATRZ W LEWO", "#F0C862"),
             ("POPATRZ W PRAWO", "#8FB79A"), ("POSŁUCHAJ", "#7FA8C9")]),
 ],

 "C5-25": [dict(
   tytul="Skala pięciu poziomów",
   kp="Wydrukuj i powieś przy kąciku wyciszenia",
   wstep="Pięć stopni od spokoju do wybuchu, z miejscem na własne słowa dziecka przy każdym. "
         "Nazwy z arkusza zamieniamy na te, których dziecko naprawdę używa — skala działa "
         "wtedy, gdy jest jego, a nie nasza.",
   rodzaj="etykiety", kolumny=1,
   etykiety=[("1 · Jest mi spokojnie", "#8FB79A"), ("2 · Coś mnie zaczyna złościć", "#7FA8C9"),
             ("3 · Jest mi trudno", "#F0C862"), ("4 · Zaraz wybuchnę", "#E0A05C"),
             ("5 · Nie panuję nad sobą", "#E8695A")]),
  dict(
   tytul="Karta „jak mówię nie”",
   wstep="Trzy zdania odmowy do przećwiczenia na scenkach, wpisane słowami dziecka. "
         "Ćwiczymy sam ton i postawę, nie treść — dziecko, które umie powiedzieć „nie chcę”, "
         "ale mówi to szeptem w podłogę, jeszcze nie umie odmówić.",
   rodzaj="pola",
   pola=[("Kiedy nie chcę, mówię", 75), ("Kiedy ktoś nie przestaje, mówię", 75),
         ("Idę wtedy do", 65)]),
 ],

 "C6-26": [dict(
   tytul="Karta nakrycia stolika",
   kp="Wydrukuj po jednej na dyżurnego",
   wstep="Dyżurny najpierw liczy miejsca, dopiero potem nosi naczynia. Wpisanie liczby "
         "przed pracą zamienia to zadanie z noszenia w liczenie — po to jest ta karta. "
         "Sprawdzenie na końcu robi dziecko, nie Pani.",
   rodzaj="pola",
   pola=[("Ile jest miejsc przy stoliku", 60), ("Ile talerzy", 60),
         ("Ile kubków", 60), ("Ile sztućców", 60)]),
 ],

 "C6-28": [dict(
   tytul="Karta przeglądu półki",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Pięć rzeczy do sprawdzenia samodzielnie, po zdjęciu wzorcowym. Kolumnę zaznacza "
         "dziecko — także wtedy, gdy Pani widzi inaczej. Rozbieżność jest materiałem do "
         "rozmowy, a nie powodem do poprawienia zaznaczenia.",
   rodzaj="tabela",
   naglowki=["Co sprawdzam", "Już tak", "Jeszcze nie"],
   wiersze=["rzeczy są na swoim miejscu", "nic nie leży na podłodze",
            "pudełka są zamknięte", "mój znaczek widać", "półka jest wytarta"]),
 ],

 "C6-29": [dict(
   tytul="Dziennik obserwacji rośliny",
   kp="Wydrukuj na cały miesiąc",
   wstep="Jedna linijka na dzień, prowadzona przez dziecko. Kolumna z wysokością ma sens "
         "dopiero po kilku tygodniach — wtedy dziecko samo widzi, że liczby rosną, i to "
         "jest odkrycie, którego nie da się zastąpić opowiedzeniem.",
   rodzaj="tabela",
   naglowki=["Data", "Ile wody", "Wysokość", "Co zauważyłem"],
   wiersze=["", "", "", "", "", "", "", ""]),
 ],

 "C7-30": [dict(
   tytul="Karta propozycji do rady",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Dziecko wypełnia kartę przed radą, nie w jej trakcie — inaczej mówi to, co "
         "usłyszało od poprzednika. Ostatnie pole wypełniamy wspólnie po liczeniu głosów, "
         "także przy propozycjach, które przepadły.",
   rodzaj="pola",
   pola=[("Mój pomysł", 80), ("Dlaczego to dobry pomysł", 80),
         ("Kto może przy tym pomóc", 60), ("Ile dostał głosów", 50)]),
 ],

 "C7-31": [dict(
   tytul="Kodeks naszej grupy",
   kp="Wydrukuj w formacie A3",
   wstep="Pięć pustych zasad i miejsce na znak każdego dziecka. Zasady wpisujemy słowami "
         "dzieci, nawet niezgrabnymi — kodeks przepisany na dorosły język przestaje być ich "
         "i po tygodniu nikt się na niego nie powołuje.",
   rodzaj="pola",
   pola=[("Zasada pierwsza", 60), ("Zasada druga", 60), ("Zasada trzecia", 60),
         ("Zasada czwarta", 60), ("Zasada piąta", 60),
         ("Podpisujemy się pod tym", 110)]),
 ],

 "C7-32": [dict(
   tytul="Przeprosiny w trzech krokach",
   kp="Wydrukuj i powieś w kąciku naprawy",
   wstep="Trzy pola, z których trzecie jest tym właściwym. Przeprosiny bez naprawy dziecko "
         "szybko odkrywa jako formułkę kończącą sprawę bez kosztu — dlatego pole „jak to "
         "naprawię” zostawiamy największe i nie odpuszczamy go.",
   rodzaj="pola",
   pola=[("Zrobiłem", 70), ("Przez to poczułeś", 70), ("Naprawię to tak", 100)]),
 ],

 "C7-34": [dict(
   tytul="Karty zachowań do posortowania",
   kp="Wydrukuj, wytnij i wymieszaj",
   wstep="Sześć kart do rozdzielenia na dwie kupki. Po posortowaniu wracamy do kupki "
         "raniącej i przy każdej karcie pytamy, jak to naprawić — bez tego kroku ćwiczenie "
         "zostawia dziecku poczucie winy i nic poza tym.",
   rodzaj="etykiety", kolumny=3,
   etykiety=[("POMOGŁEM", "#8FB79A"), ("POCIESZYŁEM", "#8FB79A"),
             ("ZAPROSIŁEM DO ZABAWY", "#8FB79A"), ("WYŚMIAŁEM", "#E8695A"),
             ("NIE WPUŚCIŁEM DO GRY", "#E8695A"), ("PRZEZWAŁEM", "#E8695A")]),
 ],

 "C8-35": [dict(
   tytul="Karta ról w zespole",
   kp="Wydrukuj po jednej na zespół",
   wstep="Role rozdzielają dzieci między sobą, przed pracą i na piśmie. Przy sporze "
         "wskazujemy kartę zamiast rozstrzygać — uzgodnienie jest tu zadaniem, a nie "
         "przeszkodą przed zadaniem.",
   rodzaj="pola",
   pola=[("Kto pilnuje czasu", 60), ("Kto przynosi materiały", 60),
         ("Kto zapisuje ustalenia", 60), ("Kto opowie o naszej pracy", 60)]),
 ],

 "C8-36": [dict(
   tytul="Karta ukończenia pracy",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Pierwsze pole wypełniamy przed rozpoczęciem — bez niego „skończone” znaczy "
         "„znudziło mi się” i nie ma o czym rozmawiać przy samoocenie. Dwa pozostałe "
         "dziecko wypełnia samo, po odłożeniu pracy.",
   rodzaj="pola",
   pola=[("Po czym poznam, że skończone (wpisz przed pracą)", 70),
         ("Jak mi poszło", 55), ("Z tego fragmentu jestem dumny", 80)]),
 ],

 "C8-38": [dict(
   tytul="Metki cenowe do sklepu",
   kp="Wydrukuj, wytnij i przyczep do towarów",
   wstep="Ceny do dziesięciu złotych, w kwotach, które da się odliczyć prawdziwymi monetami. "
         "Nie podnosimy cen powyżej dziesięciu — liczenie przestaje wtedy być liczeniem, "
         "a zaczyna zgadywaniem.",
   rodzaj="etykiety", kolumny=4,
   etykiety=[("1 zł", "#8FB79A"), ("2 zł", "#7FA8C9"), ("3 zł", "#F0C862"),
             ("4 zł", "#E0A05C"), ("5 zł", "#E8695A"), ("6 zł", "#C9A0C0"),
             ("7 zł", "#8FA9B7"), ("10 zł", "#8FB79A")]),
 ],

 "C8-39": [dict(
   tytul="Karta małego badacza",
   kp="Wydrukuj po jednej na odkrycie",
   wstep="Pytanie w pierwszym polu ma pochodzić od dziecka i zostać zapisane wcześniej, "
         "na tablicy pytań grupy. Ostatnie pole jest tu najważniejsze: odkrycie, po którym "
         "nie pojawia się nowe pytanie, zwykle nie było szukaniem.",
   rodzaj="pola",
   pola=[("Moje pytanie", 70), ("Gdzie szukałem", 60),
         ("Czego się dowiedziałem", 95), ("Teraz chcę wiedzieć", 70)]),
 ],

 "C9-40": [dict(
   tytul="Plansza kręgów przynależności",
   kp="Wydrukuj w formacie A3",
   wstep="Cztery pola od siebie na zewnątrz. W pierwsze dziecko wkleja własne zdjęcie, "
         "w drugie zdjęcie rodziny przyniesione z domu — zdjęcia dostarczone przez "
         "przedszkole zamieniają osobistą planszę w ćwiczenie z pojęć.",
   rodzaj="pola",
   pola=[("Ja", 90), ("Moja rodzina", 90), ("Moja grupa", 90), ("Moja miejscowość", 90)]),
 ],

 "C9-41": [dict(
   tytul="Karta poznawania kraju",
   kp="Wydrukuj i powieś nisko",
   wstep="Wypełniamy od dołu do góry: najpierw nasza miejscowość, dopiero na końcu symbole "
         "państwa. Sześciolatek buduje pojęcie kraju z miejsc, które zna; zaczynanie od "
         "godła daje słowo bez treści.",
   rodzaj="tabela",
   naglowki=["Symbol", "Jak wygląda albo brzmi", "Kiedy go widzimy"],
   wiersze=["nasza miejscowość", "stolica", "flaga", "godło", "hymn"]),
 ],

 "C9-42": [dict(
   tytul="Legitymacja przedszkolaka",
   kp="Wydrukuj po jednej na dziecko",
   wstep="Dane wpisuje dziecko, na tyle, na ile potrafi. Ostatnie pole jest ważniejsze niż "
         "trzy pierwsze: dziecko, które umie wyrecytować adres, ale nie ma przećwiczonego "
         "„nie powiem”, poda go pierwszej osobie, która zapyta pewnym głosem.",
   rodzaj="pola",
   pola=[("Imię", 55), ("Nazwisko", 55), ("Miejscowość", 55),
         ("Dane mogę podać tylko", 80)]),
 ],

 "C9-44": [dict(
   tytul="Karta zawodu",
   kp="Wydrukuj po jednej na gościa",
   wstep="Wypełniana po wizycie rodzica, nie przed. Ostatnia kolumna — co ten zawód robi "
         "dla nas — jest tą, która zamienia obrazek w czyjąś pracę; pozostałe trzy da się "
         "wypełnić z karty obrazkowej i niewiele z tego wynika.",
   rodzaj="tabela",
   naglowki=["Zawód", "Czym pracuje", "Gdzie pracuje", "Co robi dla nas"],
   wiersze=["", "", "", "", "", ""]),
 ],
}


def _obraz(kod):
    dane = base64.b64encode((KATALOG / f"k_{kod}.jpg").read_bytes()).decode()
    return f"data:image/jpeg;base64,{dane}"


def _symbole_arkusza(a):
    return a.get("symbole", [])


def _gotowy(a):
    """Arkusz wchodzi do dokumentu dopiero, gdy wszystkie jego symbole istnieją."""
    return all(jest(k) for k in _symbole_arkusza(a))


def _arkusze(nr):
    return [a for a in ARKUSZE.get(nr, []) if _gotowy(a)]


def _kody(nry=None):
    """Kody symboli użytych w rejestrze, bez powtórzeń.

    `nry` zawęża do wskazanych konspektów — zeszyt jednej grupy wiekowej nie ma
    po co nieść materiałów z pozostałych.
    """
    uzyte = set()
    for nr in ARKUSZE:
        if nry is not None and nr not in nry:
            continue
        for a in _arkusze(nr):
            uzyte.update(_symbole_arkusza(a))
    return sorted(uzyte)


UKLAD = """
.kd-pasek{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0 4px}
.kd-pasek .kafel{flex:1 1 150px;max-width:200px;position:relative}
.kd-krok{position:absolute;top:6px;left:6px;width:24px;height:24px;border-radius:50%;
 background:#2E5E8E;color:#FFF;font:700 13px/24px system-ui,sans-serif;text-align:center}
.kd-tablica{border:2px solid #2E5E8E;border-radius:12px;padding:14px;margin:14px 0 4px;
 background:#FFF;display:grid;gap:12px}
/* Tablicy się nie rozcina, więc kafle nie mogą nosić przerywanej linii cięcia —
   inaczej arkusz sam sobie przeczy. */
.kd-tablica .kafel{border:1.5px solid #DCE7F0}
.kd-tab{width:100%;min-width:0;table-layout:fixed;border-collapse:collapse;margin:14px 0 4px;font-size:13px}
.kd-tab th,.kd-tab td{border:1px solid #9BB7CE;padding:9px 8px;text-align:left;vertical-align:top}
.kd-tab th{background:#EAF2F8;font-weight:700;color:#1F4468}
.kd-tab td.pusto{height:34px}
.kd-tab tr td:first-child{font-weight:600;color:#1F4468}
.kd-tab th:first-child{width:26%}
.kd-tab th,.kd-tab td{word-wrap:break-word}
.kd-etyk{display:grid;gap:12px;margin:14px 0 4px}
.kd-etyk .et{border:2px dashed #E4B9D2;border-radius:14px;overflow:hidden;background:#FFF}
.kd-etyk .et .pas{display:block;height:52px}
.kd-etyk .et b{display:block;padding:9px 8px;text-align:center;font-size:14px;color:#1F4468}
@media print{.kd-etyk .et .pas{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.kd-pola{display:grid;gap:12px;margin:14px 0 4px}
.kd-pole{border:1.5px solid #9BB7CE;border-radius:10px;padding:8px 10px;background:#FFF}
.kd-pole b{display:block;font-size:12px;color:#1F4468;letter-spacing:.02em}
.kd-linie{background-image:repeating-linear-gradient(#FFF 0 25px,#DCE7F0 25px 26px)}
@media print{.kd-tab th{background:#EAF2F8 !important;-webkit-print-color-adjust:exact}}
"""


def style_kart(nry=None):
    """Obrazki osadzone raz, w klasach CSS — ten sam symbol wraca w wielu arkuszach."""
    regu = "\n".join(f".kd-{kod}{{background-image:url({_obraz(kod)})}}" for kod in _kody(nry))
    return f"<style>{UKLAD}{regu}</style>"


def _kafel(kod, esc, ciecie=True, krok=None):
    numer = f'<span class="kd-krok">{krok}</span>' if krok else ""
    linia = '<span class="linia-ciecia" aria-hidden="true"></span>' if ciecie else ""
    tytul = esc(podpis(kod))
    return (f'<figure class="kafel kwadrat">{numer}'
            f'<span class="obraz kd-{kod}" role="img" aria-label="{tytul}"></span>'
            f'<figcaption>{tytul}</figcaption>{linia}</figure>')


def _tresc(a, esc):
    rodzaj = a["rodzaj"]
    if rodzaj == "karty":
        kafle = "\n".join(_kafel(k, esc) for k in a["symbole"])
        return f'<div class="zal-siatka k{a.get("kolumny", 3)}">{kafle}</div>'
    if rodzaj == "pasek":
        kafle = "\n".join(_kafel(k, esc, krok=i) for i, k in enumerate(a["symbole"], 1))
        return f'<div class="kd-pasek">{kafle}</div>'
    if rodzaj == "tablica":
        kafle = "\n".join(_kafel(k, esc, ciecie=False) for k in a["symbole"])
        kol = a.get("kolumny", 2)
        return (f'<div class="kd-tablica" style="grid-template-columns:repeat({kol},1fr)">'
                f'{kafle}</div>')
    if rodzaj == "tabela":
        glowa = "".join(f"<th>{esc(n)}</th>" for n in a["naglowki"])
        puste = len(a["naglowki"]) - 1
        wiersze = "".join(
            "<tr>" + (f"<td>{esc(w)}</td>" if w else '<td class="pusto"></td>')
            + '<td class="pusto"></td>' * puste + "</tr>"
            for w in a["wiersze"])
        return f'<table class="kd-tab"><thead><tr>{glowa}</tr></thead><tbody>{wiersze}</tbody></table>'
    if rodzaj == "etykiety":
        kol = a.get("kolumny", 3)
        karty = "".join(
            f'<div class="et"><span class="pas" style="background:{barwa}"></span>'
            f"<b>{esc(tekst)}</b></div>" for tekst, barwa in a["etykiety"])
        return (f'<div class="kd-etyk" style="grid-template-columns:repeat({kol},1fr)">'
                f"{karty}</div>")
    if rodzaj == "pola":
        pola = "".join(
            f'<div class="kd-pole kd-linie" style="min-height:{wys}px">'
            f"<b>{esc(etykieta)}</b></div>" for etykieta, wys in a["pola"])
        return f'<div class="kd-pola">{pola}</div>'
    raise ValueError(f"nieznany rodzaj arkusza: {rodzaj}")


def arkusz(nr, a, numer, ile, esc):
    return f'''<section class="zal" data-poziom="p1">
  <header class="zal-head">
    <span class="mark" role="img" aria-label="Logo PCTP"></span>
    <div>
      <div class="zal-w">EduPlaner 2026</div>
      <div class="zal-s">Materiał do wydruku {numer} z {ile} · konspekt {esc(nr)}</div>
    </div>
    <span class="zal-pill p1">do wydruku</span>
  </header>
  <div class="zal-tytul">
    <span class="zal-kp">{esc(a.get("kp", "Wydrukuj i wytnij"))}</span>
    <h3>{esc(a["tytul"])}</h3>
  </div>
  <p class="kkurs">{esc(a["wstep"])}</p>
  {_tresc(a, esc)}
  <div class="zal-stopka">
    <span><b>Konspekt {esc(nr)}</b> · materiał do wydruku</span>
    <span class="mono">EduPlaner 2026 · PCTP · druk KC-5</span>
  </div>
</section>'''


def karty_dla(nr, esc):
    """Arkusze do wydruku dla konspektu o tym numerze albo pusty string."""
    gotowe = _arkusze(nr)
    return "\n".join(arkusz(nr, a, i, len(gotowe), esc)
                     for i, a in enumerate(gotowe, 1))


def ma_karty(nr):
    return bool(_arkusze(nr))


def stan():
    """Ile arkuszy czeka na symbole — do raportu po przebudowie."""
    gotowych = sum(len(_arkusze(nr)) for nr in ARKUSZE)
    wszystkich = sum(len(v) for v in ARKUSZE.values())
    return gotowych, wszystkich, len([k for k in SYMBOLE if jest(k)]), len(SYMBOLE)
