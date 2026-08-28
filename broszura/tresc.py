# -*- coding: utf-8 -*-
"""
Kolorowy Świat Emocji — cała treść broszury w jednym miejscu.

Chcesz coś zmienić? Popraw tekst TUTAJ, a potem uruchom:
    python3 broszura/generuj.py
Plik broszura/kolorowy-swiat-emocji.html zbuduje się od nowa.
"""

TYTUL = "Kolorowy Świat Emocji"
PODTYTUL = "Zeszyt ćwiczeń dla nastolatka"
OPIS_OKLADKA = "Pięć kolorów. Pięć emocji. Jeden Ty."

# ── seria i przeznaczenie ────────────────────────────────────────────────────
SERIA = "Świat Kolorów"
CZESC = "Część 1"
PRZEZNACZENIE = ("Zeszyt do zajęć rozwijających kompetencje emocjonalne "
                 "i społeczne")
DOSTOSOWANIE = "Dostosowany do potrzeb młodzieży ze spektrum autyzmu"

GDZIE_WYKORZYSTAC = [
    "Na zajęciach rewalidacyjnych.",
    "Na zajęciach z pomocy psychologiczno-pedagogicznej.",
    "W terapii indywidualnej i w pracy w małej grupie.",
    "W domu — razem z rodzicem albo samodzielnie.",
]

# ── Kolory rozdziałów ────────────────────────────────────────────────────────
# hex      – pełny kolor emocji (duże plamy, okładki rozdziałów)
# ink      – ten sam kolor przyciemniony, bezpieczny dla tekstu na bieli
# tint     – bardzo jasne tło pod ramki i callouty
# tint2    – nieco mocniejszy odcień pod paski i chipy
# txt      – kolor napisu kładzionego wprost na pełnym kolorze emocji
# rodzaj   – rodzaj gramatyczny nazwy emocji: "m" (mój smutek) albo "ż" (moja radość)

ROZDZIALY = [
    # ═══════════════════════════════════════════════════════════════════════
    {
        "nr": "01",
        "kolor": "Żółty",
        "emocja": "Radość",
        "rodzaj": "ż",
        "hex": "#F2B21A",
        "txt": "#3D2800",
        "ink": "#8A5D00",
        "tint": "#FEF7E2",
        "tint2": "#FBE7B0",
        "haslo": "Żółty mówi: dobrze mi.",
        "otwarcie": "Radość to uczucie, że jest dobrze. Ma kolor słońca.",

        "co_to": [
            "Radość to uczucie, że jest dobrze.",
            "Czujesz ją, kiedy dzieje się coś miłego.",
            "Radość jest lekka. Ciało robi się swobodne.",
            "Radość bywa cicha albo głośna. Obie są prawdziwe.",
            "Radość czasem trwa chwilę. To normalne.",
            "Radość dzielona z kimś rośnie.",
        ],
        "mysl": "Radość nie musi być głośna. Cicha radość też się liczy.",
        "ciekawostka": "Kolor żółty pierwszy przyciąga wzrok. Dlatego żółte są taksówki, "
                       "kamizelki odblaskowe i znaki drogowe. Radość działa podobnie — "
                       "inni widzą ją na Twojej twarzy szybciej niż Ty sam.",

        "twarz": [
            "Kąciki ust idą do góry.",
            "Oczy robią się węższe i błyszczą.",
            "Policzki unoszą się.",
            "Brwi są rozluźnione.",
        ],
        "cialo": [
            "Ramiona opadają swobodnie.",
            "Ruchy są szybsze i lżejsze.",
            "Ręce się otwierają.",
            "Chce Ci się ruszać: skakać, klaskać, tańczyć.",
        ],
        "srodku": [
            "W klatce piersiowej robi się ciepło.",
            "Oddech jest spokojny.",
            "Masz więcej energii.",
            "Głos brzmi wyżej i głośniej.",
        ],

        "kiedy": [
            "Kiedy ktoś bliski się do Ciebie uśmiecha.",
            "Kiedy robisz to, co lubisz: rysujesz, grasz, składasz, czytasz.",
            "Kiedy słuchasz swojej ulubionej piosenki.",
            "Kiedy udało Ci się coś trudnego.",
            "Kiedy jesteś na dworze i świeci słońce.",
            "Kiedy przytulasz swojego zwierzaka.",
            "Kiedy dowiadujesz się czegoś nowego o swoim ulubionym temacie.",
            "Kiedy ktoś powie: „dobrze to zrobiłeś”.",
        ],

        "opowiadanie_tytul": "Żółty piknik",
        "opowiadanie": [
            "Był sobotni ranek. Rajmund włożył żółtą koszulkę. Zawsze zakłada ją, "
            "kiedy chce, żeby dzień był dobry.",
            "W parku czekała Maja. Rozłożyli koc pod dużym drzewem. Maja przyniosła "
            "winogrona i sok. Rajmund przyniósł głośnik.",
            "Puścili piosenkę, którą oboje znają na pamięć. Rajmund poczuł ciepło "
            "w klatce piersiowej. Ramiona same mu opadły. Zauważył, że się uśmiecha.",
            "— Dobrze mi teraz — powiedział głośno. Sam się zdziwił, że to powiedział.",
            "— Mnie też — odpowiedziała Maja.",
            "Potem wzięli kartkę. Napisali na niej wszystko, co ich dzisiaj ucieszyło. "
            "Wyszło jedenaście rzeczy. Rajmund pokolorował kartkę na żółto.",
            "Wieczorem powiesił ją nad biurkiem. Pomyślał, że kiedy przyjdzie gorszy "
            "dzień, spojrzy na tę kartkę i przypomni sobie, że radość naprawdę była.",
        ],
        "pytania": [
            "Po czym Rajmund poznał, że czuje radość? Wypisz dwa znaki z ciała.",
            "Co takiego zrobiła Maja, że Rajmundowi było dobrze?",
            "Rajmund powiedział na głos: „Dobrze mi teraz”. Czy Tobie łatwo tak powiedzieć? Dlaczego?",
            "Po co Rajmund powiesił żółtą kartkę nad biurkiem?",
            "Wypisz trzy rzeczy, które Ty wpisałbyś na taką kartkę.",
            "Czy radość musi być głośna? Uzasadnij.",
            "Co w tym opowiadaniu jest podobne do Twojego dobrego dnia?",
            "Gdyby Twoja radość miała odcień żółtego — byłby jasny czy ciemny? Dlaczego?",
        ],
        "zadania_latwe": [
            "Znajdź w domu trzy żółte przedmioty. Ustaw je obok siebie.",
            "Napisz jedno zdanie: dzisiaj ucieszyło mnie ______.",
            "Zrób zdjęcie czegoś, co Cię dzisiaj ucieszyło.",
        ],
        "zadania_srednie": [
            "Zrób listę pięciu rzeczy, które kojarzą Ci się z radością. Przy każdej dopisz dlaczego.",
            "Wybierz bohatera filmu albo gry, który często jest radosny. Opisz, po czym to poznajesz.",
            "Ułóż playlistę „żółtą” — pięć utworów, przy których jest Ci dobrze.",
        ],
        "zadania_smiale": [
            "Zrób kolaż radości: wytnij zdjęcia z gazet, dodaj rysunki, podpisz każdy element.",
            "Napisz krótkie opowiadanie o kimś, kto znajduje radość w drobnej rzeczy.",
            "Powiedz jednej osobie, co Cię dzisiaj ucieszyło. Zapisz, jak zareagowała.",
        ],
        "pomaga_tytul": "Jak zatrzymać radość na dłużej?",
        "pomaga": [
            "Nazwij ją: powiedz w myślach „to jest radość”.",
            "Zatrzymaj ją: zrób zdjęcie albo zapisz jedno zdanie.",
            "Podziel się nią: powiedz komuś, co się stało.",
            "Wróć do niej wieczorem: przypomnij sobie ten moment przed snem.",
        ],
        "zdjecia": {
            "otwarcie": "Duże, jasne zdjęcie: pole słoneczników albo słońce prześwitujące przez liście. "
                        "Ciepłe światło, dużo żółci, brak twarzy — sam kolor i nastrój.",
            "co_to": "Dwa zdjęcia obok siebie: (1) żółty balon na tle nieba, (2) miska cytryn na stole. "
                     "Ten sam odcień żółtego, spokojne tło.",
            "cialo": "Trzy zdjęcia portretowe nastolatka z widocznym uśmiechem: twarz z bliska, "
                     "cała sylwetka w ruchu, dłonie uniesione w geście radości. Naturalne, nie pozowane.",
            "kiedy": "Cztery małe zdjęcia sytuacyjne: słuchawki na uszach, pies liżący rękę, "
                     "rysowanie w szkicowniku, wschód słońca za oknem.",
            "opowiadanie": "Dwa zdjęcia: (1) koc piknikowy z owocami widziany z góry, "
                           "(2) żółta kartka z napisami przypięta nad biurkiem.",
            "moja_strona": "Miejsce na Twoje własne zdjęcie albo wydruk — coś, co Cię cieszy.",
        },
    },

    # ═══════════════════════════════════════════════════════════════════════
    {
        "nr": "02",
        "kolor": "Niebieski",
        "emocja": "Smutek",
        "rodzaj": "m",
        "hex": "#2E6FB7",
        "txt": "#FFFFFF",
        "ink": "#1B4A7E",
        "tint": "#EAF2FB",
        "tint2": "#C6DCF3",
        "haslo": "Niebieski mówi: coś mnie boli w środku.",
        "otwarcie": "Smutek to uczucie ciężkie i wolne. Ma kolor deszczowego nieba.",

        "co_to": [
            "Smutek to uczucie, że czegoś brakuje.",
            "Przychodzi po stracie, po zawodzie, po rozstaniu.",
            "Smutek jest ciężki. Ciało robi się wolniejsze.",
            "Smutek nie jest zły. Mówi Ci, co było dla Ciebie ważne.",
            "Smutek mija. Zawsze mija, choć czasem powoli.",
            "W smutku wolno prosić o pomoc.",
        ],
        "mysl": "Smutek nie jest błędem. To znak, że coś było dla Ciebie ważne.",
        "ciekawostka": "Ludzie na całym świecie rysują smutek na niebiesko — tak samo w Polsce, "
                       "w Japonii i w Brazylii. Po angielsku smutna muzyka nazywa się „blues”, "
                       "czyli po prostu „błękity”.",

        "twarz": [
            "Kąciki ust opadają w dół.",
            "Powieki są cięższe, oczy patrzą w dół.",
            "Brwi ściągają się do środka.",
            "Twarz jest mniej ruchliwa.",
        ],
        "cialo": [
            "Ramiona i plecy się garbią.",
            "Ruchy są wolniejsze.",
            "Ręce trzymasz blisko ciała.",
            "Trudniej Ci patrzeć komuś w oczy.",
        ],
        "srodku": [
            "W klatce piersiowej robi się ciężko.",
            "Gardło się ściska.",
            "Masz mniej siły i ochoty.",
            "Możesz jeść mniej albo więcej niż zwykle.",
        ],

        "kiedy": [
            "Kiedy oglądasz zdjęcia z wakacji, które już się skończyły.",
            "Kiedy koledzy bawią się razem, a Ty stoisz obok.",
            "Kiedy dostajesz gorszą ocenę, niż się starałeś.",
            "Kiedy ktoś bliski wyjeżdża albo choruje.",
            "Kiedy coś ulubionego się zepsuje albo zgubi.",
            "Kiedy kończą się wakacje.",
            "Kiedy słuchasz smutnej piosenki.",
            "Kiedy plan się zmienia i nic nie możesz zrobić.",
        ],

        "opowiadanie_tytul": "Niebieska koszulka",
        "opowiadanie": [
            "Rajmund ma niebieską koszulkę. Zakłada ją w gorsze dni. Mówi, że wtedy "
            "koszulka jest jak tarcza.",
            "Tamtej środy padał deszcz. W szkole nikt do niego nie zagadał. "
            "Rajmund siedział przy oknie i patrzył na krople spływające po szybie.",
            "W klatce piersiowej miał ciężar. Ramiona same mu opadły. Pomyślał: "
            "„To jest smutek. Czuję go teraz”.",
            "Po lekcjach nie poszedł od razu do domu. Wszedł do parku i usiadł na ławce. "
            "Deszcz zmoczył mu włosy, ale to nie przeszkadzało.",
            "Wyjął kartkę i narysował dużą niebieską chmurę. Pod nią napisał trzy zdania "
            "o tym, co było dzisiaj trudne.",
            "Wtedy podeszła Maja z parasolem. Nic nie pytała. Po prostu usiadła obok.",
            "— Mogę zobaczyć? — spytała po chwili.",
            "Rajmund pokazał jej rysunek. Maja powiedziała: — U mnie taki dzień był w piątek.",
            "Ciężar nie zniknął od razu. Ale zrobił się mniejszy. Rajmund zrozumiał coś "
            "ważnego: smutek nie znika od tego, że go chowamy. Znika od tego, "
            "że ktoś przy nas usiądzie.",
        ],
        "pytania": [
            "Po czym Rajmund poznał, że czuje smutek? Wypisz trzy znaki.",
            "Dlaczego Rajmund zakłada niebieską koszulkę w gorsze dni?",
            "Rajmund powiedział sobie w myślach: „To jest smutek”. Po co to zrobił?",
            "Co pomogło Rajmundowi bardziej: rysunek czy obecność Mai? Uzasadnij.",
            "Maja nic nie pytała, tylko usiadła obok. Czy to była dobra pomoc? Dlaczego?",
            "Napisz jedno zdanie, które chciałbyś usłyszeć od kogoś, gdy jest Ci smutno.",
            "Co Ty rysujesz albo robisz, kiedy jest Ci ciężko?",
            "Kogo mógłbyś poprosić, żeby po prostu przy Tobie usiadł?",
        ],
        "zadania_latwe": [
            "Znajdź w pokoju coś niebieskiego. Weź to do ręki i policz do dziesięciu.",
            "Dokończ zdanie: dziś było mi smutno, kiedy ______.",
            "Narysuj niebieską chmurę. W środku napisz jedno słowo.",
        ],
        "zadania_srednie": [
            "Przez tydzień zapisuj jedną smutną chwilę dziennie. Na końcu przeczytaj wszystko naraz.",
            "Znajdź piosenkę, która pasuje do smutku. Napisz, co w niej jest niebieskiego.",
            "Wypisz trzy rzeczy, które pomagają Ci, gdy jest Ci źle. Powieś listę w widocznym miejscu.",
        ],
        "zadania_smiale": [
            "Napisz krótki wiersz o niebieskim kolorze. Nie musi się rymować.",
            "Namaluj obraz „mój smutek” tylko w odcieniach niebieskiego.",
            "Powiedz jednej zaufanej osobie: „Dzisiaj jest mi smutno”. Zapisz, co się potem stało.",
        ],
        "pomaga_tytul": "Co robić, gdy jest ciężko?",
        "pomaga": [
            "Nazwij to: „To jest smutek. Czuję go teraz”.",
            "Zwolnij: usiądź, napij się wody, oddychaj wolniej.",
            "Wypuść to: narysuj, napisz, posłuchaj muzyki.",
            "Nie zostawaj sam: napisz albo powiedz jednej osobie.",
        ],
        "zdjecia": {
            "otwarcie": "Duże zdjęcie: krople deszczu na szybie, za nią rozmyte światła. "
                        "Chłodne, spokojne, granatowo-błękitne.",
            "co_to": "Dwa zdjęcia: (1) zachmurzone niebo nad wodą, (2) pusta ławka w parku po deszczu.",
            "cialo": "Trzy zdjęcia: nastolatek siedzący ze zgarbionymi plecami (od tyłu, bez twarzy), "
                     "dłonie splecione na kolanach, spojrzenie skierowane w dół. Delikatnie, bez dramatyzowania.",
            "kiedy": "Cztery małe zdjęcia: stare zdjęcia z wakacji na stole, plecak w przedpokoju, "
                     "puste boisko, kalendarz z zaznaczonym dniem.",
            "opowiadanie": "Dwa zdjęcia: (1) mokra ławka w parku i parasol, "
                           "(2) kartka z narysowaną niebieską chmurą.",
            "moja_strona": "Miejsce na Twoje zdjęcie: coś niebieskiego, co ma dla Ciebie znaczenie.",
        },
    },

    # ═══════════════════════════════════════════════════════════════════════
    {
        "nr": "03",
        "kolor": "Czerwony",
        "emocja": "Złość",
        "rodzaj": "ż",
        "hex": "#D33B2C",
        "txt": "#FFFFFF",
        "ink": "#992418",
        "tint": "#FDECEA",
        "tint2": "#F8C9C3",
        "haslo": "Czerwony mówi: coś jest nie w porządku.",
        "otwarcie": "Złość to uczucie mocne i szybkie. Ma kolor ognia i znaku STOP.",

        "co_to": [
            "Złość to uczucie, że ktoś przekroczył Twoją granicę.",
            "Przychodzi szybko i jest mocna.",
            "Złość daje energię. Ciało napina się do działania.",
            "Złość mówi coś ważnego: „to mi nie pasuje”.",
            "Złość wolno czuć. Nie wolno nią krzywdzić.",
            "Złość da się wypuścić bezpiecznie.",
        ],
        "mysl": "Złość wolno czuć. Krzywdzić nie wolno. To dwie różne sprawy.",
        "ciekawostka": "Czerwony to na całym świecie kolor ostrzeżenia: znak STOP, "
                       "przycisk alarmowy, czerwona kartka. Złość działa tak samo — "
                       "to alarm, że coś wymaga Twojej uwagi.",

        "twarz": [
            "Brwi ściągają się w dół i do środka.",
            "Usta się zaciskają albo otwierają w krzyku.",
            "Twarz i uszy robią się czerwone.",
            "Wzrok wbija się w jeden punkt.",
        ],
        "cialo": [
            "Dłonie zaciskają się w pięści.",
            "Ramiona i szczęka się napinają.",
            "Ruchy są gwałtowne.",
            "Chce Ci się krzyczeć, uderzyć, wyjść.",
        ],
        "srodku": [
            "Serce bije szybciej.",
            "Robi się gorąco, zwłaszcza na twarzy.",
            "Oddech przyspiesza i się skraca.",
            "Trudniej myśleć spokojnie.",
        ],

        "kiedy": [
            "Kiedy ktoś zabiera Twoją rzecz bez pytania.",
            "Kiedy ktoś się z Ciebie śmieje.",
            "Kiedy plan zmienia się nagle i nikt Cię nie uprzedził.",
            "Kiedy coś nie działa mimo wielu prób.",
            "Kiedy ktoś Ci przerywa albo nie słucha.",
            "Kiedy jest za głośno, za jasno, za tłoczno.",
            "Kiedy ktoś oskarża Cię niesprawiedliwie.",
            "Kiedy jesteś zmęczony i głodny — wtedy złość przychodzi łatwiej.",
        ],

        "opowiadanie_tytul": "Czerwone światło",
        "opowiadanie": [
            "Rajmund budował model przez trzy tygodnie. Stał na półce, prawie skończony.",
            "W czwartek wrócił do domu i zobaczył, że model leży rozbity na podłodze. "
            "Obok stał młodszy kuzyn.",
            "Rajmundowi zrobiło się gorąco na twarzy. Serce zaczęło walić. "
            "Dłonie same zacisnęły się w pięści.",
            "W głowie miał jedno zdanie: „Zaraz nakrzyczę”.",
            "Ale zamiast tego zrobił cztery rzeczy, których nauczył się wcześniej.",
            "Raz: powiedział w myślach STOP. Dwa: policzył cztery wdechy i sześć wydechów. "
            "Trzy: wyszedł na balkon na dwie minuty. Cztery: wrócił i powiedział zdanie, "
            "które wcześniej sobie przygotował.",
            "— Jestem bardzo zły. To był mój model. Nie chcę teraz rozmawiać. "
            "Porozmawiamy za godzinę.",
            "Kuzyn się rozpłakał. Ciocia przeprosiła. Model dało się skleić — nie cały, ale prawie.",
            "Wieczorem Rajmund pomyślał: złość była tak samo duża jak zawsze. "
            "Ale pierwszy raz nikt przez nią nie ucierpiał. To była różnica.",
        ],
        "pytania": [
            "Po czym Rajmund poznał, że czuje złość? Wypisz trzy znaki z ciała.",
            "Dlaczego Rajmund miał prawo się zezłościć?",
            "Wypisz po kolei cztery kroki, które zrobił Rajmund.",
            "Co by się stało, gdyby Rajmund od razu nakrzyczał? Wypisz dwa skutki.",
            "Rajmund powiedział: „Nie chcę teraz rozmawiać. Porozmawiamy za godzinę”. Po co?",
            "Rajmund miał zdanie przygotowane wcześniej. Ułóż swoje własne takie zdanie.",
            "Gdzie Ty możesz pójść na dwie minuty, gdy zrobi się gorąco?",
            "Czy złość zniknęła? Co się właściwie zmieniło?",
        ],
        "zadania_latwe": [
            "Zaciśnij pięści i policz do pięciu. Potem rozluźnij dłonie. Powtórz trzy razy.",
            "Dokończ zdanie: najbardziej złości mnie, kiedy ______.",
            "Znajdź w domu trzy czerwone rzeczy, które ostrzegają albo zatrzymują.",
        ],
        "zadania_srednie": [
            "Narysuj termometr złości od 1 do 10. Zaznacz, przy której liczbie musisz odejść.",
            "Wypisz trzy miejsca, w których możesz bezpiecznie ochłonąć.",
            "Napisz swoje zdanie granicy: „Nie zgadzam się, żeby ______”.",
        ],
        "zadania_smiale": [
            "Narysuj obraz „moja złość” samą czerwienią. Użyj mocnych, szybkich pociągnięć.",
            "Opisz sytuację, w której Twoja złość pomogła Ci obronić coś ważnego.",
            "Ustal z bliską osobą wspólny znak, który znaczy: „potrzebuję przerwy”.",
        ],
        "pomaga_tytul": "Cztery kroki, gdy robi się gorąco",
        "pomaga": [
            "STOP — powiedz to słowo w myślach. Nic nie rób przez chwilę.",
            "ODDECH — cztery liczby wdech, sześć liczb wydech. Trzy razy.",
            "ODEJDŹ — wyjdź na dwie minuty w umówione miejsce.",
            "POWIEDZ — użyj swojego przygotowanego zdania. Bez wyzwisk.",
        ],
        "zdjecia": {
            "otwarcie": "Duże zdjęcie: czerwone światło sygnalizacji na ciemnym tle "
                        "albo zbliżenie na płomień. Mocne, kontrastowe.",
            "co_to": "Dwa zdjęcia: (1) znak STOP, (2) czerwony przycisk alarmowy. "
                     "Motyw ostrzeżenia, nie agresji.",
            "cialo": "Trzy zdjęcia: zaciśnięta pięść, napięte ramiona (sylwetka od tyłu), "
                     "zbliżenie na ściągnięte brwi. Bez scen przemocy.",
            "kiedy": "Cztery małe zdjęcia: rozlana szklanka, tłum w korytarzu, "
                     "zepsuty sprzęt, zatłoczony autobus.",
            "opowiadanie": "Dwa zdjęcia: (1) rozbity model albo klocki na podłodze, "
                           "(2) balkon i widok na miasto — miejsce na ochłonięcie.",
            "moja_strona": "Miejsce na Twoje zdjęcie: Twoje miejsce na ochłonięcie.",
        },
    },

    # ═══════════════════════════════════════════════════════════════════════
    {
        "nr": "04",
        "kolor": "Różowy",
        "emocja": "Wstyd",
        "rodzaj": "m",
        "hex": "#E0619B",
        "txt": "#3F0B25",
        "ink": "#A62D68",
        "tint": "#FDEDF4",
        "tint2": "#F8CBDF",
        "haslo": "Różowy mówi: chcę się schować.",
        "otwarcie": "Wstyd to uczucie gorące i ciasne. Ma kolor rumieńca na policzkach.",

        "co_to": [
            "Wstyd to uczucie, że ktoś zobaczył mnie z gorszej strony.",
            "Robi się gorąco na twarzy. Chcesz zniknąć.",
            "Wstyd przychodzi zwykle przy ludziach.",
            "Wstyd mówi: zależy mi na tym, co inni pomyślą.",
            "Wstyd nie znaczy, że jesteś zły. Znaczy, że coś poszło nie tak.",
            "Wstyd mija szybciej, gdy powiesz o nim komuś zaufanemu.",
        ],
        "mysl": "Zawstydziłem się. To znaczy, że mi zależy. To nie znaczy, że jestem gorszy.",
        "ciekawostka": "Rumieniec to jedyna reakcja ciała, której nie da się zrobić na zamówienie. "
                       "Nie da się zaczerwienić na komendę. Dlatego rumieniec jest zawsze prawdziwy.",

        "twarz": [
            "Policzki i uszy robią się różowe albo czerwone.",
            "Wzrok ucieka w dół lub w bok.",
            "Głowa się pochyla.",
            "Uśmiech bywa niepewny, krótki.",
        ],
        "cialo": [
            "Ramiona podnoszą się do uszu.",
            "Ręce zasłaniają twarz albo krzyżują się na piersi.",
            "Robisz się mniejszy, cofasz się o krok.",
            "Ruchy stają się nerwowe.",
        ],
        "srodku": [
            "Na twarzy robi się gorąco.",
            "Serce przyspiesza.",
            "Głos robi się cichszy albo drży.",
            "W brzuchu ściska.",
        ],

        "kiedy": [
            "Kiedy pomylisz się przy całej klasie.",
            "Kiedy ktoś przeczyta na głos coś Twojego.",
            "Kiedy potkniesz się na korytarzu.",
            "Kiedy powiesz coś głośniej, niż chciałeś.",
            "Kiedy ktoś skomentuje Twój wygląd albo ubranie.",
            "Kiedy zapomnisz czyjegoś imienia.",
            "Kiedy zachowasz się inaczej, niż wszyscy wokół.",
            "Kiedy ktoś nagrywa Cię bez pytania.",
        ],

        "opowiadanie_tytul": "Różowe uszy",
        "opowiadanie": [
            "We wtorek Rajmund odpowiadał przy tablicy. Pomylił dwie daty. Ktoś z tyłu klasy "
            "parsknął śmiechem.",
            "Rajmund poczuł, jak twarz robi mu się gorąca. Uszy piekły. Wzrok sam uciekł w dół.",
            "W głowie miał jedno: „Chcę zniknąć”. Ramiona podniosły mu się do uszu.",
            "Usiadł. Przez resztę lekcji nie odezwał się ani razu. Wydawało mu się, że wszyscy "
            "na niego patrzą.",
            "Na przerwie podeszła Maja. — Widziałam — powiedziała. — Mnie to samo było w październiku. "
            "Pomyliłam się w wierszu. Płakałam w toalecie.",
            "Rajmund spojrzał na nią zdziwiony. Nie wiedział o tym.",
            "— I co potem? — zapytał.",
            "— Potem był piątek. I nikt już o tym nie pamiętał — wzruszyła ramionami Maja.",
            "Rajmund policzył w myślach do dziesięciu. Gorąco na twarzy zaczęło schodzić.",
            "Powiedział sobie zdanie, którego nauczył go terapeuta: „Zawstydziłem się. "
            "To minie. To nie mówi o tym, kim jestem”.",
            "W czwartek zgłosił się do odpowiedzi jeszcze raz. Ręka trochę mu drżała. "
            "Ale ją podniósł.",
        ],
        "pytania": [
            "Po czym Rajmund poznał, że czuje wstyd? Wypisz trzy znaki z ciała.",
            "Co Rajmund pomyślał w pierwszej chwili? Zapisz to zdanie.",
            "Dlaczego rozmowa z Mają pomogła? Co takiego Maja powiedziała?",
            "Maja powiedziała: „nikt już o tym nie pamiętał”. Czy to prawda również u Ciebie?",
            "Zapisz zdanie, którego nauczył się Rajmund. Powiedz je na głos.",
            "Dlaczego podniesienie ręki w czwartek było dla Rajmunda odważne?",
            "Napisz o sytuacji, w której Ty się zawstydziłeś. Ile dni później to przestało być ważne?",
            "Komu mógłbyś powiedzieć o swoim wstydzie? Wpisz jedno imię.",
        ],
        "zadania_latwe": [
            "Połóż dłonie na policzkach. Sprawdź, czy są ciepłe, czy chłodne.",
            "Dokończ zdanie: wstydzę się, kiedy ______.",
            "Powiedz na głos: „To minie”. Powtórz trzy razy.",
        ],
        "zadania_srednie": [
            "Przez tydzień zapisuj sytuacje, w których poczułeś wstyd. Zaznacz, ile trwał.",
            "Wypisz trzy rzeczy, których się wstydziłeś rok temu, a dziś już nie.",
            "Napisz swoje zdanie ratunkowe na chwilę wstydu. Naucz się go na pamięć.",
        ],
        "zadania_smiale": [
            "Zrób kolaż w odcieniach różu: co pomaga Ci wrócić do siebie po wstydzie.",
            "Opowiedz zaufanej osobie o jednej wstydliwej sytuacji. Zapisz, jak zareagowała.",
            "Zrób coś, czego trochę się wstydzisz, ale chcesz: zgłoś się, zapytaj, zaproś.",
        ],
        "pomaga_tytul": "Co robić, gdy robi się gorąco na twarzy?",
        "pomaga": [
            "Oddychaj: wdech nosem, długi wydech ustami. Pięć razy.",
            "Powiedz w myślach: „Zawstydziłem się. To minie”.",
            "Sprawdź fakty: czy naprawdę wszyscy patrzą? Policz, ilu.",
            "Powiedz o tym jednej zaufanej osobie. Wstyd nie znosi bycia wypowiedzianym.",
        ],
        "zdjecia": {
            "otwarcie": "Duże zdjęcie: kwiat wiśni albo róża w miękkim świetle, "
                        "delikatny róż. Spokojne, ciepłe, nie słodkie.",
            "co_to": "Dwa zdjęcia: (1) różowe niebo o zachodzie, (2) dłonie zasłaniające twarz "
                     "(bez widocznych oczu). Delikatnie, z szacunkiem.",
            "cialo": "Trzy zdjęcia: uniesione ramiona, wzrok skierowany w bok, "
                     "sylwetka odwrócona plecami do grupy. Nikogo nie ośmieszamy.",
            "kiedy": "Cztery małe zdjęcia: tablica w klasie, mikrofon, telefon nagrywający, "
                     "korytarz szkolny pełen ludzi.",
            "opowiadanie": "Dwa zdjęcia: (1) tablica i kreda z bliska, "
                           "(2) dwie osoby rozmawiające na parapecie na przerwie.",
            "moja_strona": "Miejsce na Twoje zdjęcie: osoba albo miejsce, przy którym nie musisz udawać.",
        },
    },

    # ═══════════════════════════════════════════════════════════════════════
    {
        "nr": "05",
        "kolor": "Szary",
        "emocja": "Lęk",
        "rodzaj": "m",
        "hex": "#6E7681",
        "txt": "#FFFFFF",
        "ink": "#454B54",
        "tint": "#F1F2F4",
        "tint2": "#DBDEE2",
        "haslo": "Szary mówi: boję się tego, co będzie.",
        "otwarcie": "Lęk to uczucie napięte i czujne. Ma kolor mgły, przez którą nic nie widać.",

        "co_to": [
            "Lęk to uczucie, że stanie się coś złego.",
            "Dotyczy przyszłości: tego, co dopiero będzie.",
            "Lęk stawia ciało w gotowości. Napina mięśnie.",
            "Lęk chce Cię chronić. Czasem ostrzega za mocno.",
            "Lęk rośnie, gdy nie wiesz, co się wydarzy.",
            "Lęk maleje, gdy dostaniesz konkretną informację i plan.",
        ],
        "mysl": "Lęk to nie przepowiednia. To tylko myśl, która przyszła do głowy.",
        "ciekawostka": "Słowa lęk, strach i panika oznaczają podobne uczucie, ale różnej siły. "
                       "Strach dotyczy czegoś konkretnego, tu i teraz. Lęk dotyczy tego, "
                       "co może się dopiero wydarzyć. Panika to bardzo mocny lęk, który przychodzi nagle.",

        "twarz": [
            "Oczy szeroko otwarte, wzrok skacze.",
            "Brwi unoszą się i ściągają.",
            "Usta lekko otwarte albo mocno zaciśnięte.",
            "Trudno utrzymać kontakt wzrokowy.",
        ],
        "cialo": [
            "Ramiona podnoszą się i sztywnieją.",
            "Nogi chcą uciekać, stopy się przestępują.",
            "Ręce bawią się czymś, drżą albo się pocą.",
            "Chcesz wyjść, schować się, zniknąć w tłumie.",
        ],
        "srodku": [
            "Serce bije szybko i mocno.",
            "W brzuchu ściska, jakby były w nim motyle.",
            "W ustach robi się sucho.",
            "Oddech jest płytki i szybki.",
        ],

        "kiedy": [
            "Kiedy jutro jest klasówka albo wystąpienie.",
            "Kiedy nie wiesz, co się będzie działo.",
            "Kiedy plan dnia się zmienia bez uprzedzenia.",
            "Kiedy masz iść w nowe miejsce, którego nie znasz.",
            "Kiedy słyszysz nieznany, głośny dźwięk.",
            "Kiedy myślisz o przyszłości: szkoła, praca, samodzielność.",
            "Kiedy ktoś bliski długo nie odpisuje.",
            "Kiedy jest za dużo bodźców naraz.",
        ],

        "opowiadanie_tytul": "Szara mgła",
        "opowiadanie": [
            "W niedzielę wieczorem Rajmund założył szarą koszulkę. W poniedziałek "
            "klasa jechała na wycieczkę. Rajmund nigdy tam nie był.",
            "Leżał w łóżku i patrzył w sufit. W głowie kręciło się jedno pytanie za drugim. "
            "A jeśli zgubię grupę? A jeśli będzie za głośno? A jeśli nikt nie usiądzie ze mną w autokarze?",
            "Serce biło mu szybko. W brzuchu ściskało. W ustach było sucho.",
            "Wstał i zrobił coś, czego nauczył się na terapii. Rozejrzał się po pokoju "
            "i wymienił po kolei: pięć rzeczy, które widzi. Cztery, które słyszy. Trzy, których "
            "może dotknąć. Dwa zapachy. Jeden smak.",
            "Kiedy skończył, oddech był wolniejszy.",
            "Potem wziął kartkę i podzielił ją na dwie kolumny. W lewej napisał: „Czego się boję”. "
            "W prawej: „Co mogę z tym zrobić”.",
            "Boję się, że zgubię grupę — poproszę panią o numer telefonu i będę trzymał się Mai.",
            "Boję się hałasu — zabiorę słuchawki wygłuszające.",
            "Boję się, że nikt ze mną nie usiądzie — napiszę wieczorem do Mai i umówimy miejsce.",
            "Napisał do Mai. Odpisała po minucie: „Trzecia ławka od tyłu. Zajmę”.",
            "Mgła nie zniknęła całkiem. Ale zrobiła się cieńsza. Rajmund zasnął o dwudziestej drugiej.",
            "We wtorek wrócił z wycieczki zmęczony i zadowolony. Zapisał w zeszycie jedno zdanie: "
            "„Bałem się dziewięciu rzeczy. Wydarzyła się jedna. Poradziłem sobie”.",
        ],
        "pytania": [
            "Czego dokładnie bał się Rajmund? Wypisz trzy rzeczy.",
            "Po czym poznał lęk w ciele? Wypisz trzy znaki.",
            "Opisz ćwiczenie 5–4–3–2–1 własnymi słowami.",
            "Jak nazywały się dwie kolumny na kartce Rajmunda?",
            "Wybierz jedną swoją obawę i dopisz do niej kolumnę „Co mogę z tym zrobić”.",
            "Dlaczego wiadomość od Mai tak bardzo pomogła?",
            "Rajmund napisał: „Bałem się dziewięciu rzeczy. Wydarzyła się jedna”. Co to znaczy?",
            "Co Ty możesz przygotować dzień wcześniej, żeby lęk był mniejszy?",
        ],
        "zadania_latwe": [
            "Zrób ćwiczenie 5–4–3–2–1 tu i teraz. Wypisz to, co zauważyłeś.",
            "Dokończ zdanie: boję się, że ______.",
            "Znajdź w otoczeniu pięć szarych rzeczy. Nazwij je po kolei.",
        ],
        "zadania_srednie": [
            "Zrób tabelę z dwiema kolumnami: „Czego się boję” i „Co mogę z tym zrobić”.",
            "Napisz listę pytań, które chcesz zadać przed nową sytuacją. Zadaj je komuś dorosłemu.",
            "Zrób swoją torbę spokoju: słuchawki, butelka wody, ulubiony przedmiot, kartka z planem.",
        ],
        "zadania_smiale": [
            "Narysuj swój lęk jako szarą postać. Potem dorysuj, co ją zmniejsza.",
            "Zaplanuj krok po kroku nową sytuację, której się boisz. Rozpisz ją na godziny.",
            "Zrób pierwszy mały krok w kierunku tego, czego się boisz. Zapisz, jak poszło.",
        ],
        "pomaga_tytul": "Co robić, gdy lęk rośnie?",
        "pomaga": [
            "5–4–3–2–1: wymień 5 rzeczy widzianych, 4 słyszane, 3 dotykane, 2 zapachy, 1 smak.",
            "Oddychaj wolniej: wdech na 4, wydech na 6. Powtórz sześć razy.",
            "Zdobądź informację: zapytaj, co dokładnie się wydarzy i o której godzinie.",
            "Zrób plan: zapisz jedną rzecz, którą możesz przygotować już dzisiaj.",
        ],
        "zdjecia": {
            "otwarcie": "Duże zdjęcie: gęsta mgła nad drogą albo nad jeziorem. "
                        "Cicho, spokojnie, bez grozy.",
            "co_to": "Dwa zdjęcia: (1) mgła między drzewami, (2) zamglona szyba autobusu.",
            "cialo": "Trzy zdjęcia: dłonie splecione nerwowo, uniesione ramiona, "
                     "stopy na krawędzi chodnika. Bez przerysowanego strachu.",
            "kiedy": "Cztery małe zdjęcia: pusta sala z ławkami, zegar, autokar wycieczkowy, "
                     "telefon z nieodczytaną wiadomością.",
            "opowiadanie": "Dwa zdjęcia: (1) kartka podzielona na dwie kolumny, "
                           "(2) słuchawki wygłuszające i spakowany plecak.",
            "moja_strona": "Miejsce na Twoje zdjęcie: co jest w Twojej torbie spokoju.",
        },
    },
]

# ── Słowniczek trudnych słów ─────────────────────────────────────────────────
SLOWNICZEK = [
    ("Emocja", "Uczucie, które pojawia się w Tobie samo. Nie wybierasz go. Możesz wybrać, co z nim zrobisz."),
    ("Eksplorowanie", "Odkrywanie i badanie czegoś po kawałku. W tym zeszycie eksplorujesz swoje emocje — "
                      "sprawdzasz, jak wyglądają, kiedy przychodzą i co Ci pomaga."),
    ("Kontekst", "Wszystko, co dzieje się dookoła jakiejś sytuacji. Kontekst pomaga zrozumieć, "
                 "co dane słowo albo zachowanie naprawdę znaczy."),
    ("Empatia", "Zauważenie, co czuje druga osoba, i potraktowanie tego poważnie. "
                "Nie musisz czuć tego samego."),
    ("Samoświadomość", "Wiedza o tym, co się w Tobie dzieje: co czujesz, czego potrzebujesz, "
                       "gdzie masz granicę."),
    ("Refleksja", "Zatrzymanie się i spokojne pomyślenie o tym, co się wydarzyło."),
    ("Granica", "Linia, za którą coś przestaje być dla Ciebie w porządku. "
                "Masz prawo powiedzieć, gdzie ona jest."),
    ("Regulacja", "Sposoby, którymi pomagasz sobie wrócić do spokoju — oddech, ruch, cisza, przerwa."),
]

# ── Osoby w opowiadaniach ────────────────────────────────────────────────────
POSTACIE = [
    ("Rajmund", "17 lat", "Główny bohater. Lubi modele, mapy i porządek. Emocje widzi jako kolory. "
                          "Uczy się je nazywać."),
    ("Maja", "17 lat", "Przyjaciółka Rajmunda z klasy. Nie zasypuje pytaniami. Potrafi po prostu usiąść obok."),
    ("Kuzyn Franek", "7 lat", "Bywa u Rajmunda w czwartki. Czasem coś zepsuje. Nie robi tego złośliwie."),
    ("Pani Zofia", "nauczycielka", "Uczy Rajmunda. Uprzedza o zmianach w planie, bo wie, że to ważne."),
]


# ── Gra: Ścieżka Kolorów ─────────────────────────────────────────────────────
GRA_TYTUL = "Ścieżka Kolorów"
GRA_PODTYTUL = "Gra o emocjach dla 2–4 osób"

GRA_POTRZEBNE = [
    "Plansza z następnej strony.",
    "Talia kart — wytnij ją z dwóch kolejnych stron.",
    "Jedna kostka do gry.",
    "Pionek dla każdego gracza. Może być guzik albo moneta.",
]

GRA_ZASADY = [
    ("Ustawcie pionki na polu START",
     "Zaczyna ten, kto ostatni się dziś roześmiał."),
    ("Rzuć kostką i przesuń pionek",
     "Idziesz po kolei, zgodnie z numerami pól."),
    ("Sprawdź kolor pola",
     "Powiedz jednym zdaniem, kiedy ostatnio czułeś tę emocję. "
     "Żółty to radość, niebieski smutek, czerwony złość, "
     "różowy wstyd, szary lęk."),
    ("Pole z gwiazdką? Weź kartę",
     "Przeczytaj ją na głos i zrób to, co na niej napisano."),
    ("Kolejka przechodzi dalej",
     "Nikt nie ocenia odpowiedzi. Nie ma dobrych i złych."),
    ("Gra kończy się, gdy wszyscy dojdą do METY",
     "Pierwszy na mecie wygrywa, ale gramy do końca — "
     "bo chodzi o rozmowę, nie o wyścig."),
]

GRA_ZASADA_STOP = (
    "Zawsze możesz powiedzieć „pas”. Wtedy nie odpowiadasz i przesuwasz się "
    "dalej. Nie musisz tego tłumaczyć. Nikt nie pyta dlaczego."
)

# karty: (rodzaj, treść)
GRA_KARTY = [
    ("Sytuacja", "Ktoś zabrał Twoją rzecz bez pytania. Jaki to kolor?"),
    ("Sytuacja", "Dostałeś ocenę lepszą, niż się spodziewałeś. Jaki to kolor?"),
    ("Sytuacja", "Jutro jedziesz w miejsce, którego nie znasz. Jaki to kolor?"),
    ("Sytuacja", "Pomyliłeś się przy całej klasie. Jaki to kolor?"),
    ("Sytuacja", "Twój przyjaciel się wyprowadza. Jaki to kolor?"),
    ("Sytuacja", "Coś nie działa mimo dziesiątej próby. Jaki to kolor?"),
    ("Sytuacja", "Ktoś powiedział, że dobrze Ci poszło. Jaki to kolor?"),
    ("Sytuacja", "Plan dnia zmienił się bez uprzedzenia. Jaki to kolor?"),
    ("Sytuacja", "Ktoś nagrał Cię telefonem bez pytania. Jaki to kolor?"),
    ("Sytuacja", "Wracasz do domu po dobrym dniu. Jaki to kolor?"),
    ("Sytuacja", "W stołówce jest bardzo głośno i tłoczno. Jaki to kolor?"),
    ("Sytuacja", "Nikt nie usiadł obok Ciebie w autobusie. Jaki to kolor?"),
    ("Pokaż", "Pokaż samą twarzą radość. Inni zgadują, co to za emocja."),
    ("Pokaż", "Pokaż złość — ale bez słów i bez dotykania nikogo."),
    ("Pokaż", "Pokaż lęk. Zwróć uwagę na ramiona i dłonie."),
    ("Pokaż", "Pokaż smutek. Zwróć uwagę na plecy i wzrok."),
    ("Pokaż", "Pokaż wstyd. Co robi Twoja głowa?"),
    ("Pokaż", "Pokaż emocję, którą sam wybierzesz. Inni zgadują."),
    ("Opowiedz", "Opowiedz o czymś, co ostatnio Cię ucieszyło."),
    ("Opowiedz", "Opowiedz, co Cię uspokaja, gdy jest za dużo bodźców."),
    ("Opowiedz", "Opowiedz o kimś, kto potrafi Cię wysłuchać."),
    ("Opowiedz", "Opowiedz, po czym poznajesz, że ktoś obok jest smutny."),
    ("Opowiedz", "Opowiedz o czymś, czego bałeś się rok temu, a dziś już nie."),
    ("Opowiedz", "Powiedz jednej osobie przy stole coś miłego."),
]
