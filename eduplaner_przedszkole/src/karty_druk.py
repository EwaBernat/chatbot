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
   kp="Wydrukuj i narysuj sama",
   wstep="Trzy puste pola na jedno zajęcie: co robimy najpierw, potem i na końcu. "
         "Narysuj w nich prosty szkic przy dziecku, zanim zaczniecie — rysowanie na oczach "
         "dziecka działa lepiej niż gotowy obrazek, bo dziecko widzi, jak plan powstaje.",
   rodzaj="pola",
   pola=[("Najpierw", 110), ("Potem", 110), ("Na końcu", 110)]),
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
   kp="Wydrukuj i narysuj sama",
   wstep="Cztery puste pola do wypełnienia pod konkretne święto. Pokaż dziecku plan dzień "
         "wcześniej i przejdźcie po nim palcem — dla trzylatka uroczystość jest przede "
         "wszystkim dniem, w którym wszystko wygląda inaczej, i to właśnie ta zmiana, "
         "a nie hałas, najczęściej go przeciąża.",
   rodzaj="pola",
   pola=[("Najpierw", 100), ("Potem", 100), ("Potem", 100), ("Na końcu", 100)]),
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
