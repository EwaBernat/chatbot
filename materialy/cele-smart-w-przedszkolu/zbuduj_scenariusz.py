#!/usr/bin/env python3
"""Generuje scenariusz filmu szkoleniowego i czysty tekst narracji.

Jedno źródło prawdy: lista SCENY poniżej. Z niej powstają dwa pliki:
  scenariusz_filmu.md — scenariusz produkcyjny (obraz + tekst na ekranie + narracja)
  narracja.txt        — sam tekst do lektora / TTS, liczby zapisane słowami

    python3 zbuduj_scenariusz.py
"""
import pathlib, re

KAT = pathlib.Path(__file__).parent

# (nr, tytuł sceny, plansza, czas_s, [teksty na ekranie], narracja)
SCENY = [
("1","Otwarcie — dwa zdania, które robią różnicę","plansze/00_tytul.png",50,
 ["Cele SMART w przedszkolu","Zobaczyć · policzyć · obronić"],
 """Dziecko będzie lepiej radziło sobie z emocjami i stanie się spokojniejsze.

Tak brzmi cel, który spotykam w co drugiej dokumentacji. Brzmi dobrze. I nie da się go sprawdzić.
Za pół roku nikt — łącznie z autorką tego zapisu — nie odpowie, czy się udało.

A teraz to samo, inaczej. Dziecko rozpozna narastające napięcie i zastosuje oddech cztery — cztery — cztery,
w czterech na pięć sytuacji trudnych, do końca semestru.

Drugie zdanie mówi, co robić w poniedziałek rano. Pierwsze nie mówi nic.
Przez najbliższy kwadrans pokażę, jak przejść od pierwszego zdania do drugiego."""),

("2","Dlaczego akurat teraz","plansze/12_dlaczego_teraz.png",80,
 ["Nowa podstawa · wrzesień · ocena efektywności"],
 """Dlaczego mówimy o tym akurat teraz? Zbiegły się trzy rzeczy.

Pierwsza. Pierwszego września dwa tysiące dwudziestego szóstego roku weszła w życie nowa podstawa programowa
wychowania przedszkolnego. Osiągnięcia dziecka opisuje się w niej w dziewięciu obszarach zamiast czterech.
Cel napisany w starym układzie nie wskaże właściwego obszaru ani numeru osiągnięcia.

Druga. Wrzesień to miesiąc, w którym zapada zapis na cały rok. Programy dla dzieci z orzeczeniami powstają teraz.
Obserwacja wstępna trwa właśnie w tych tygodniach. Cel wpisany źle we wrześniu jest potem kopiowany przez dwanaście miesięcy.

Trzecia. Ocena efektywności udzielanej pomocy to obowiązek, nie dobra wola.
Zespół co najmniej dwa razy w roku ocenia poziom funkcjonowania dziecka i skuteczność programu.
Pierwszy przegląd wypada zwykle na przełomie semestrów.
Policzy się wtedy tylko to, co ma miarę wpisaną dziś."""),

("3","Cel-życzenie kontra cel-narzędzie","plansze/01_zyczenie_narzedzie.png",80,
 ["§1 · Po co","Zasada trzech osób"],
 """Cel w dokumentacji ma trzech odbiorców.

Dziecko — przez to, co robisz z nim codziennie. Rodzica — który musi zrozumieć, nad czym pracujecie.
I zespół, który dwa razy w roku ma ocenić, czy to zadziałało.

Cel-życzenie brzmi: dziecko będzie spokojniejsze. Nie wiadomo, co dokładnie ma zrobić, ile razy, w jakiej sytuacji
ani do kiedy. Słowo „spokojniejsze” to interpretacja dorosłego, a nie zachowanie dziecka.

Cel-narzędzie brzmi inaczej. Rozpozna, zastosuje — to widać. Cztery na pięć — to policzysz.
Sytuacje trudne — wiadomo, kiedy obserwować. Do końca semestru — wiadomo, kiedy podsumować.

Jest prosty test. Nazywam go zasadą trzech osób.
Gdyby jutro zastąpiła Cię inna nauczycielka, czy z samego zapisu celu wiedziałaby, co robić i co liczyć?
Jeśli tak — cel jest dobry. Jeśli musiałaby dopytywać — cel jest jeszcze życzeniem."""),

("4","Pięć liter, pięć pytań kontrolnych","plansze/02_piec_liter.png",115,
 ["§2 · Anatomia","S · M · A · R · T"],
 """SMART to nie ozdobnik w tabelce. To pięć filtrów, przez które przepuszczasz jedno zdanie.
Każda litera ma jedno pytanie kontrolne.

S jak skonkretyzowany. Pytanie: czy to zachowanie da się zobaczyć albo usłyszeć?
Czy dwie różne osoby opiszą je tak samo? Pułapka: „poprawi zachowanie”. To Twoja ocena, nie czynność dziecka.

M jak mierzalny. Pytanie: ile razy, na ile okazji, czym to policzę?
Kartą obserwacji, żetonami, listą. Pułapka: „często”, „zazwyczaj”, „znacząco częściej”. Tego nie da się policzyć.

A jak osiągalny. Pytanie: czy to jeden krok dalej niż to, co dziecko potrafi dziś?
Czy mieści się w przyznanym poziomie wsparcia? Pułapka: cel trzy piętra nad punktem wyjścia.
Efekt jest zawsze ten sam — dziecko przez pół roku nie doświadcza sukcesu, a Ty piszesz „cel niezrealizowany”.

R jak istotny. Pytanie: czy osiągnięcie tego celu realnie ułatwi dziecku dzień w przedszkolu?
Czy wynika z wielospecjalistycznej oceny i z orzeczenia? Pułapka: cel skopiowany z internetu
albo z zeszłorocznego programu innego dziecka.

T jak określony w czasie. Pytanie: do kiedy? I równie ważne — kiedy zajrzę do celu po drodze,
żeby zdążyć go zmodyfikować? Pułapka: „w ciągu roku szkolnego”, bez punktu kontrolnego.
Orientujesz się w maju, że nic się nie działo."""),

("5","Sześć kroków od obserwacji do zapisu","plansze/03_szesc_krokow.png",115,
 ["§3 · Skrypt","Najpierw patrzysz i liczysz, potem piszesz"],
 """Kolejność ma znaczenie. Cel nie powstaje przy biurku, tylko na dywanie.

Krok pierwszy: zobacz i nazwij zachowanie. Przez około dwa tygodnie zapisuj, co dokładnie się dzieje.
Bez ocen i bez przyczyn. Zapytaj siebie: gdybym nagrała to kamerą, co widać na nagraniu?
Zamiast „złości się” zapisujesz: zaciska pięści, oddycha szybciej, odwraca się od stołu.
Zbierz też sytuacje, w których dziecku się udaje.

Krok drugi: zmierz punkt wyjścia. Policz, jak jest teraz. Bez tej liczby nie ustawisz sensownego kryterium
ani później nie wykażesz postępu. Na pięć trudnych sytuacji — w ilu dziecko poradziło sobie dziś?
Powiedzmy, że w jednej, i to tylko z podpowiedzią dorosłego.

Krok trzeci: wybierz czasownik, który widać. To serce całego celu.
Wskaże, nazwie, poprosi, zastosuje, poda, wybierze — tak. Zrozumie, poczuje, będzie wiedziało — nie.
Sprawdzian jest jeden: czy mogę postawić kreskę w chwili, gdy to się stanie?

Krok czwarty: dopisz miarę i kryterium. Liczba, plus z ilu prób, plus w jakim okresie.
Dobra zasada dla przedszkola: kryterium ustaw o jeden, dwa punkty powyżej punktu wyjścia. Nie na maksimum.
Punkt wyjścia jeden na pięć oznacza realne kryterium trzy albo cztery na pięć. Nie pięć na pięć.

Krok piąty: ustal warunki i poziom wsparcia. Ten sam cel znaczy co innego przy pełnej podpowiedzi,
a co innego przy samodzielności. Napisz wprost: samodzielnie, po jednej podpowiedzi słownej, albo z pomocą gestu.
Dodaj, gdzie i kiedy: w sali, w ogrodzie, przy posiłku.

Krok szósty: wyznacz termin i sposób sprawdzenia. Data końcowa plus punkt kontrolny w połowie drogi.
Wpisz narzędzie: karta obserwacji, arkusz zliczeń, wpis w dzienniku.
I pamiętaj: termin celu nie może wykraczać poza okres, na jaki opracowano program."""),

("6","Formuła zdania — tak wpisujesz cel","plansze/04_formula_zdania.png",100,
 ["§4 · Formuła","Siedem pól, jedno zdanie"],
 """Jeśli masz zapisać cel już, dziś, na jutro — użyj formuły. Siedem pól, wypełniasz po kolei.

Pole pierwsze: kto. Dziecko albo imię.
Pole drugie: w jakiej sytuacji — gdzie i kiedy to obserwujesz.
Pole trzecie: z jakim wsparciem — samodzielnie czy z podpowiedzią.
Pole czwarte: co zrobi — czasownik, który widać, plus co konkretnie.
Pole piąte: miara — ile na ile prób.
Pole szóste: termin — do kiedy.
Pole siódme: sprawdzenie — czym to potwierdzisz.

A teraz to samo, wypełnione. Dziecko, w sytuacjach trudnych w sali i w ogrodzie,
samodzielnie, bez podpowiedzi słownej dorosłego, rozpozna narastające napięcie na termometrze
i zastosuje strategię wyciszenia, w czterech na pięć obserwowanych sytuacji, do końca pierwszego semestru,
co potwierdzi zapis w karcie obserwacji.

Jedno zdanie. Siedem informacji. Zero miejsca na domysły.

Na koniec zrób test głośnego czytania. Przeczytaj cel rodzicowi i zapytaj:
co konkretnie zobaczy Pani u dziecka w grudniu, jeśli nam się uda?
Jeśli rodzic odpowie jednym zdaniem — cel jest zrozumiały. Jeśli milknie — wróć do kroku trzeciego."""),

("7","Bank czasowników","plansze/05_bank_czasownikow.png",70,
 ["§5 · Słownik","Czasownik przesądza o mierzalności"],
 """Najkrótsza droga do dobrego celu prowadzi przez dobry czasownik.

Po jednej stronie są czasowniki, przy których postawisz kreskę na karcie obserwacji.
Wskaże. Nazwie. Poda. Powtórzy. Zastosuje. Wybierze. Ułoży. Poprosi. Zgłosi. Podejdzie. Odłoży. Poczeka. Zapyta.

Po drugiej stronie są czasowniki-pułapki. One dzieją się w głowie dziecka i nie da się ich zmierzyć.
Zrozumie. Poczuje. Uświadomi sobie. Polubi. Nauczy się. Poprawi. Wzmocni. Rozwinie.

Naprawa jest prosta. Zadaj sobie pytanie: po czym poznam, że dziecko to zrozumiało?
I wpisz właśnie tę odpowiedź.

„Zrozumie zasadę” zamienia się w: poda zasadę własnymi słowami lub wskaże ją na obrazku.
„Rozpozna emocje” zamienia się w: wskaże na planszy kolor odpowiadający swojemu napięciu.
„Poprosi o pomoc, gdy poczuje złość” zamienia się w: użyje umówionego gestu albo zdania „potrzebuję przerwy”."""),

("8","Rozbiór celu wzorcowego i konspekt","plansze/06_termometr_rozbior.png",115,
 ["§6 · Wzorzec","Termometr napięcia · ICF b1521"],
 """Weźmy teraz cel wzorcowy i przepuśćmy go przez wszystkie pięć filtrów.
To cel z konspektu „Termometr napięcia”, załącznika do programu.

S — dwie obserwowalne czynności. Rozpozna, czyli wskazuje poziom na termometrze.
I zastosuje, czyli wykonuje oddech cztery — cztery — cztery. Obie widać z drugiego końca sali.

M — cztery na pięć sytuacji trudnych, liczone w karcie obserwacji. Jedna kreska to jedna sytuacja.

A — cel opisany dla poziomu pierwszego, z gotową modyfikacją dla poziomu drugiego i trzeciego.
Skala od jednego do sześciu jest w zasięgu przedszkolaka, bo opiera się na kolorze i sygnale z ciała,
a nie na nazywaniu emocji.

R — sfera integracji społeczno-emocjonalnej i samoregulacji. W klasyfikacji funkcjonowania to kod be tysiąc pięćset dwadzieścia jeden.
Wychwycenie strefy żółtej to moment, w którym strategia jeszcze działa. To realna różnica między trudną chwilą a wybuchem.

T — do końca semestru, przy pracy ciągłej w ciągu dnia.

Zwróć uwagę na jedną rzecz, bo to najbardziej ekonomiczne rozwiązanie w całej tej historii.
Plansza termometru jest jednocześnie pomocą dydaktyczną i narzędziem zbierania danych.
Termometr wraca w realnych sytuacjach, a nie tylko na zajęciach — dlatego dane zbierają się same.

Tak wygląda ten cel wpisany do konspektu. Ten sam zapis, słowo w słowo,
trafia do karty obserwacji i do sekcji trzeciej programu. Trzy różne sformułowania tego samego celu
to w praktyce trzy różne cele."""),

("9","Dziewięć obszarów nowej podstawy","plansze/07_dziewiec_obszarow.png",85,
 ["§7 · Bank celów","Obszar + numer osiągnięcia"],
 """Nowa podstawa porządkuje osiągnięcia dziecka w dziewięciu obszarach.
Społecznym, osobistym, językowym, matematycznym, przyrodniczym, technicznym, cyfrowym, artystycznym i ruchowym.

Do każdego obszaru da się napisać gotowy cel. Trzy przykłady.

Obszar społeczny. Punkt wyjścia: dziecko wchodzi do zabawy, zabierając zabawkę, a o pozwolenie pyta
w jednej na pięć sytuacji. Cel: dołączy do zabawy rówieśników, używając umówionego zwrotu,
samodzielnie, w czterech na pięć obserwowanych sytuacji zabawy swobodnej, do końca pierwszego semestru.

Obszar ruchowy. Punkt wyjścia: utrzymuje równowagę na jednej nodze przez około dwie sekundy.
Cel: utrzyma równowagę przez pięć sekund, samodzielnie, w czterech na pięć prób, do końca kwietnia.
Mierzysz stoperem, raz w tygodniu.

Obszar cyfrowy. Cel: wskaże na obrazkach trzy urządzenia i powie własnymi słowami, do czego każde służy,
samodzielnie, w czterech na pięć prób, do końca marca.

Zwróć uwagę, że przy każdym celu jest punkt wyjścia i narzędzie pomiaru. Bez nich cel jest tylko ładnym zdaniem.

I jeszcze jedno, bardzo praktyczne. W dokumentacji dopisz obok obszaru konkretne osiągnięcie
z załącznika do rozporządzenia, razem z jego numerem. Obszar mówi, gdzie pracujesz.
Numer osiągnięcia mówi, co dokładnie realizujesz — i to on obroni cel przed zespołem i organem nadzoru."""),

("10","Zielony, żółty, czerwony","plansze/08_ewaluacja.png",90,
 ["§8 · Ewaluacja","Co zrobić z celem po punkcie kontrolnym"],
 """Przychodzi punkt kontrolny. Siadasz z kartą obserwacji. Są trzy możliwe światła.

Zielone, czyli cztery albo pięć na pięć. Cel osiągnięty — zapisz to konkretnie, z liczbą.
Podnieś poprzeczkę w stronę generalizacji: inne miejsce, inna osoba dorosła, większa grupa.
Nowy cel buduj od tego, co dziecko już robi. Nie zaczynaj od zera.

Żółte, czyli dwa albo trzy na pięć. Uwaga — cel zostaje. Zmieniasz drogę do niego.
Zmniejsz krok i tempo. Dołóż podpowiedź: wzór, gest, początek odpowiedzi. Wydłuż czas. Zwiększ liczbę prób.

Czerwone, czyli zero albo jeden na pięć. Cofnij cel o etap, do poziomu, na którym dziecko odnosi sukces.
Uprość zadanie, zmień kanał — obraz albo gest zamiast słowa.
Zweryfikuj poziom wsparcia i sam zapis celu. Rozważ konsultację zespołu.

I najważniejsze zdanie tej części. Cel, który nie działa, nie jest porażką dziecka. Jest informacją dla zespołu.

Ewaluację zapisz w trzech zdaniach. Pierwsze — liczba: w okresie od września do stycznia
odnotowano cztery na pięć sytuacji. Drugie — warunki: samodzielnie, bez podpowiedzi, w sali i w ogrodzie.
Trzecie — wniosek i decyzja: cel osiągnięty, przechodzimy do generalizacji.
Taki zapis jest zarazem oceną efektywności udzielanej pomocy i materiałem do wielospecjalistycznej oceny poziomu funkcjonowania."""),

("11","Checklista przed wpisaniem celu","plansze/09_checklista.png",70,
 ["§9 · Kontrola","Dziesięć pytań · pięć poprawek"],
 """Zanim wpiszesz cel do dokumentu, przejdź dziesięć pytań. Jeśli na któreś odpowiadasz „nie” — wracasz o krok.

Czy cel opisuje czynność dziecka, a nie działanie nauczyciela ani stan emocjonalny?
Czy czasownik pochodzi z listy tych, które widać? Czy jest liczba: ile razy, na ile prób?
Czy znam punkt wyjścia, a kryterium jest od niego wyższe o jeden, dwa kroki — nie o pięć?
Czy napisane jest, ile wsparcia dziecko może dostać? Czy wiadomo, gdzie i kiedy obserwuję?
Czy jest termin i punkt kontrolny w połowie okresu? Czy wpisane jest narzędzie pomiaru?
Czy cel wynika z wielospecjalistycznej oceny i z orzeczenia, a nie z gotowego wzoru?
I ostatnie: czy inna nauczycielka, czytając sam cel, wie, co robić w poniedziałek?

Na koniec pięć poprawek, które w praktyce załatwiają większość przypadków.

„Dziecko będzie chętniej uczestniczyć w zajęciach grupowych” zamienia się w:
dołączy do zabawy w kole i pozostanie w niej przez co najmniej pięć minut, w trzech na pięć zajęć w tygodniu.

„Nauczyciel będzie wspierał dziecko w rozpoznawaniu emocji” zamienia się w:
dziecko wskaże na planszy kolor odpowiadający swojemu napięciu, w czterech na pięć sytuacji trudnych.
Zwróć uwagę na zmianę podmiotu — cel opisuje dziecko, nie dorosłego."""),

("12","Podstawa prawna","plansze/10_podstawa_prawna.png",90,
 ["§10 · Prawo","Pięć aktów"],
 """Cel SMART nie jest wymysłem metodyków. To praktyczna odpowiedź na to, czego przepisy wymagają od dokumentacji.
Rozpoznania potrzeb, zaplanowania działań i oceny ich efektywności. Pięć aktów, na które możesz się powołać.

Prawo oświatowe. Przedszkole ma dostosowywać treści, metody i organizację nauczania do możliwości psychofizycznych
dziecka oraz zapewniać pomoc psychologiczno-pedagogiczną. Dostosowanie musi być opisane konkretnie.

Rozporządzenie o pomocy psychologiczno-pedagogicznej. Nakłada obowiązek obserwacji pedagogicznej
nastawionej na wczesne rozpoznanie dysharmonii rozwojowych oraz oceny efektywności udzielanej pomocy
wraz z wnioskami do dalszej pracy. Bez liczby w celu nie da się tej oceny sporządzić.

Rozporządzenie o warunkach organizowania kształcenia dzieci niepełnosprawnych — to konstytucja programu.
Zespół co najmniej dwa razy w roku szkolnym dokonuje okresowej wielospecjalistycznej oceny poziomu funkcjonowania,
uwzględniając ocenę efektywności programu, i w miarę potrzeb ten program modyfikuje.

Rozporządzenie o wczesnym wspomaganiu rozwoju. Ta sama logika: cel, działanie, sprawdzenie, modyfikacja.

I nowa podstawa programowa, obowiązująca od pierwszego września dwa tysiące dwudziestego szóstego roku.
To ona wprowadza dziewięć obszarów w miejsce czterech.

W rubryce „podstawa prawna” wystarczy jedna linia. Paragraf szósty przy celach i ewaluacji programu,
paragraf dwudziesty przy obserwacji pedagogicznej i ocenie efektywności pomocy.
Przed oddaniem dokumentacji sprawdź aktualny tekst jednolity — pozycje tekstów jednolitych
zmieniają się częściej niż same przepisy."""),

("13","Stare i nowe rozporządzenie","plansze/10c_stare_nowe.png",90,
 ["§10 · Zmiana podstawy","2017 poz. 356 → 2026 poz. 378"],
 """Skoro mowa o przepisach — pierwszego września zmieniła się podstawa programowa wychowania przedszkolnego.
Zobaczmy dokładnie, co się zmieniło, a co zostało po staremu.

Po lewej stan do trzydziestego pierwszego sierpnia dwa tysiące dwudziestego szóstego roku.
Rozporządzenie z czternastego lutego dwa tysiące siedemnastego roku, pozycja trzysta pięćdziesiąt sześć.
Osiągnięcia dziecka opisywano w czterech obszarach rozwoju: fizycznym, emocjonalnym, społecznym i poznawczym.
Cel odnosił się do obszaru rozwoju dziecka.

Po prawej stan od pierwszego września. Rozporządzenie Ministra Edukacji z jedenastego marca
dwa tysiące dwudziestego szóstego roku, pozycja trzysta siedemdziesiąt osiem.
Obszarów jest teraz dziewięć: społeczny, osobisty, językowy, matematyczny, przyrodniczy,
techniczny, cyfrowy, artystyczny i ruchowy.
I praktyczna wskazówka — w dokumentacji wskazuj obszar oraz numer osiągnięcia z załącznika.
To ten numer obroni cel przed zespołem i organem nadzoru.

A teraz to, co się nie zmieniło, i to jest dobra wiadomość.
Obowiązek mierzalności celu nie płynie z podstawy programowej, tylko z dwóch innych rozporządzeń —
o kształceniu specjalnym i o pomocy psychologiczno-pedagogicznej. Te obowiązują dalej.
Zmiana podstawy ich nie ruszyła.
Zmienił się wyłącznie adres obszaru, do którego cel przypisujesz. Z czterech na dziewięć.

Jedno zastrzeżenie, żeby uniknąć wpadki. Numery tekstów jednolitych sprawdź w bazie ISAP,
zanim je zacytujesz w dokumencie.
Rozporządzenia bywają nowelizowane częściej, niż zmienia się ich treść merytoryczna."""),

("14","Czy cel SMART jest obowiązkowy","plansze/10b_czy_obowiazkowe.png",95,
 ["§10 · Pytanie z sali","Formuła — nie. Miara — tak."],
 """To pytanie pada na każdym szkoleniu, więc odpowiem na nie wprost. Czy cel SMART jest obowiązkowy?

Sama formuła — nie. I dobrze o tym wiedzieć, zanim ktoś zapyta.
Słowo „SMART” nie pada w rozporządzeniach, które regulują program edukacyjno-terapeutyczny
i pomoc psychologiczno-pedagogiczną. Żaden przepis nie narzuca formuły zdania
ani kolejności siedmiu pól. Co więcej — w katalogu tego, co określa program edukacyjno-terapeutyczny,
same cele nie są wymienione jako odrębny element. Ten katalog mówi o zakresie i sposobie dostosowania,
o zintegrowanych działaniach nauczycieli i specjalistów, o formach i okresie pomocy, o zajęciach rewalidacyjnych.
Nikt nie zakwestionuje Twojego celu dlatego, że nie ma w nim akronimu.

Ale teraz druga strona. Obowiązkowa jest ocena efektywności.
Nauczyciele i specjaliści udzielający pomocy oceniają jej efektywność i formułują wnioski dotyczące dalszych działań.
To paragraf dwudziesty, ustęp dziewiąty rozporządzenia o pomocy psychologiczno-pedagogicznej.

Obowiązkowa jest też okresowa wielospecjalistyczna ocena poziomu funkcjonowania.
Zespół dokonuje jej co najmniej dwa razy w roku szkolnym, uwzględniając ocenę efektywności programu,
i w miarę potrzeb ten program modyfikuje. To paragraf szósty, ustęp dziewiąty rozporządzenia o kształceniu specjalnym.

I tu jest całe sedno. Przepis nie mówi „napisz cel SMART”. Przepis mówi „oceń efektywność”.
A efektywności celu bez miary nie da się ocenić. Miara jest więc wymuszona funkcjonalnie, choć nie literalnie.

Jeśli ktoś zapyta, dlaczego tak piszesz cele, odpowiedź brzmi:
nie realizuję metodyki, tylko obowiązek oceny efektywności. SMART jest po prostu najprostszą znaną techniką,
która pozwala ten obowiązek wykonać."""),

("15","Skąd się wzięły te cele i skąd ten pomysł","plansze/11_zrodla.png",95,
 ["Źródła","Doran · Mager · Kiresuk · Locke i Latham · WHO · IDEA"],
 """Zostaje pytanie, które warto sobie zadać: skąd to wszystko właściwie pochodzi.
SMART w przedszkolu ma cztery korzenie i żaden z nich nie jest przedszkolny.

Korzeń pierwszy — zarządzanie. Skrót SMART pojawił się w tysiąc dziewięćset osiemdziesiątym pierwszym roku,
w artykule George'a Dorana w czasopiśmie „Management Review”. Ciekawostka: u Dorana litera A oznaczała
„przypisany komuś”, a R — „realny przy danych zasobach”. Doran od razu zastrzegł, że nie każdy cel musi spełniać
wszystkie pięć kryteriów. SMART miał być listą kontrolną, a nie gorsetem.

Korzeń drugi — dydaktyka. Dwadzieścia lat wcześniej, w tysiąc dziewięćset sześćdziesiątym drugim roku,
Robert Mager opisał cel dydaktyczny jako zdanie złożone z trzech części: zachowania, warunków i kryterium.
To dokładnie te same pola, które wypełniasz w naszej formule.

Korzeń trzeci — psychologia motywacji. Edwin Locke i Gary Latham podsumowali trzydzieści pięć lat badań
nad wyznaczaniem celów. Wniosek jest jednoznaczny: cele konkretne i wymagające dają wyraźnie lepsze wyniki
niż zachęta „postaraj się najlepiej, jak umiesz”. To empiryczna odpowiedź na pytanie, dlaczego „będzie spokojniejsze” nie działa.

Korzeń czwarty — ewaluacja. Thomas Kiresuk i Robert Sherman opisali skalowanie osiągania celu.
Ich reguła jest prosta: skalę wyników ustalasz z góry, zanim zaczniesz pracę.
Stąd bierze się logika zielonego, żółtego i czerwonego światła.

Do tego dwa filary z zewnątrz. Klasyfikacja funkcjonowania Światowej Organizacji Zdrowia w wersji dla dzieci
daje wspólny język, który rozumie logopeda, psycholog i lekarz.
A amerykańskie prawo oświatowe od lat wymaga w programie mierzalnych celów rocznych i opisu, jak postęp będzie mierzony.
Cel uznaje się tam za mierzalny, gdy ma cztery elementy: termin, warunki, zachowanie i kryterium.
Ten sam zestaw, co w naszej formule.

Innymi słowy: nie wymyślamy niczego nowego. Korzystamy z czegoś, co sprawdza się od kilkudziesięciu lat."""),

("16","Zakończenie — trzy rzeczy do zrobienia","plansze/13_final.png",60,
 ["Mniej dokumentów. Więcej edukacji."],
 """Zostawiam Cię z trzema rzeczami do zrobienia.

Dziś: weź jeden cel z bieżącej dokumentacji i przepisz go formułą siedmiu pól.

Do piątku: zmierz punkt wyjścia u jednego dziecka. Pięć sytuacji, pięć kresek. Nic więcej.

Za osiem tygodni: usiądź z kartą obserwacji i sprawdź, jakie masz światło. Zielone, żółte czy czerwone.

Jedno zdanie z miarą zastępuje pół strony ogólników — i jako jedyne przechodzi przez ewaluację.

Mniej dokumentów. Więcej edukacji."""),
]

def slowa_pl(n):
    """Poprawna odmiana rzeczownika 'slowo' po liczbie."""
    if n == 1:
        return "1 slowo".replace("slowo", "słowo")
    r100, r10 = n % 100, n % 10
    if r10 in (2, 3, 4) and r100 not in (12, 13, 14):
        return f"{n} słowa"
    return f"{n} słów"


def czas_sceny(tekst):
    """Czas sceny liczony z tekstu: ok. 150 slow na minute po polsku, zaokraglone do 5 s."""
    return max(20, round(len(tekst.split()) * 0.4 / 5) * 5)


def main():
    # --- narracja.txt — czysty tekst do lektora / TTS ---
    # Bez naglowkow i komentarzy: skrypty mowy czytaja plik doslownie,
    # wiec kazda linia opisowa zostalaby wypowiedziana na glos.
    czysta = "\n\n".join(t.strip() for *_, t in SCENY) + "\n"
    (KAT / "narracja.txt").write_text(czysta, encoding="utf-8")

    # --- narracja_ze_scenami.txt — ta sama tresc z podzialem na sceny (do pracy, nie do TTS) ---
    n = ["# Narracja z podziałem na sceny — do redakcji, NIE do lektora.",
         "# Do nagrania używaj pliku narracja.txt (bez nagłówków).",
         "# Liczby zapisane słowami — silnik mowy czyta je wtedy poprawnie po polsku.",
         "# Pusta linia = naturalna pauza oddechowa.", ""]
    for nr, tyt, _, _, _, tekst in SCENY:
        n.append(f"### Scena {nr} — {tyt}")
        n.append("")
        n.append(tekst.strip())
        n.append("")
    (KAT / "narracja_ze_scenami.txt").write_text("\n".join(n), encoding="utf-8")

    # --- scenariusz_filmu.md ---
    slow = sum(len(t.split()) for *_, t in SCENY)
    czas = sum(czas_sceny(t) for *_, t in SCENY)
    m = [f"""# Scenariusz filmu szkoleniowego — „Cele SMART w przedszkolu”

**Materiał:** szkolenie dla nauczycieli przedszkola
**Podstawa treści:** broszura PCTP Koszalin „Cele SMART w przedszkolu”, sygn. **SMART-P1**, stan prawny **28 sierpnia 2026 r.**
**Przykład przewodni:** konspekt **TUE-1 „Termometr napięcia”** (sfera integracji społeczno-emocjonalnej, ICF b1521)
**Opracowanie:** pedagog specjalny mgr Mirosława Ewa Jurczyszyn · ekosystem EduPlaner2026-MJ-PCTP

| Parametr | Wartość |
|---|---|
| Liczba scen | {len(SCENY)} |
| Szacowany czas | ok. {czas // 60} min {czas % 60} s |
| Liczba słów narracji | {slow} |
| Tempo | ok. 150 słów/min (polski lektor) |
| Format obrazu | 16:9, 1920 × 1080 px (konspekt: A4, 1240 × 1754 px) |
| Marka | fiolet `#2D1B69` + pomarańcz `#E8450A`, Arial |

---

## Jak czytać ten scenariusz

Każda scena ma cztery elementy: **plansza** (gotowy plik PNG), **tekst na ekranie**,
**narracja** (dokładnie ten tekst, który czyta lektor) i **wskazówki realizacyjne**.
Tekst narracji jest jednocześnie w osobnym pliku `narracja.txt` — do wklejenia w lektora AI albo do nagrania.

Liczby w narracji są **zapisane słowami** („cztery na pięć”, a nie „4/5”), bo silniki mowy
czytają polskie liczebniki niepewnie. Pusta linia oznacza naturalną pauzę.

---
"""]
    for nr, tyt, plansza, _sek, ekran, tekst in SCENY:
        slowa = len(tekst.split())
        sek = czas_sceny(tekst)
        m.append(f"""## Scena {nr} · {tyt}

**Czas:** ok. {sek} s ({slowa_pl(slowa)}) · **Plansza:** `{plansza}`

**Tekst na ekranie:** {" · ".join(ekran)}

**Narracja:**

> {chr(10).join('> ' + w if w else '>' for w in tekst.strip().split(chr(10)))[2:]}

---
""")
    m.append("""## Wskazówki realizacyjne

**Montaż.** Plansza zmienia się między zdaniami, nigdy w ich środku. Najprościej: docinaj obraz
do pauz (pustych linii) w `narracja.txt`. Scena 8 ma dwie plansze — po rozbiorze celu wchodzi
konspekt A4 (`plansze/14_konspekt_tue1.png`) jako pełnoekranowe ujęcie z powolnym najazdem na blok celu.

**Tempo.** 150 słów na minutę. Jeśli nagranie wyjdzie dłuższe, skracaj scenę 5 i 13 — mają najwięcej treści
do samodzielnego doczytania w broszurze.

**Napisy.** Materiał jest po polsku i pełen terminów prawnych — napisy są obowiązkowe, nie opcjonalne.
Generuj je razem z dźwiękiem (plik `.srt` ze znacznikami czasu), nie dopisuj ręcznie.

**Głos.** Film ma być firmowany nazwiskiem autorki, więc narrację czyta **jej głos** — nagrany albo sklonowany
z jej własnych próbek. Nagranie cudzym głosem, także „na próbę”, podważa wiarygodność materiału.

**Wersja krótka (spot 90 s).** Sceny 1 + 6 + 14, bez zmian w tekście. Daje kompletny przekaz:
problem → formuła → wezwanie do działania.

---

## Pliki

| Plik | Co to jest |
|---|---|
| `scenariusz_filmu.md` | ten dokument — scenariusz produkcyjny |
| `narracja.txt` | **czysty** tekst narracji — bez nagłówków, gotowy dla lektora / silnika mowy |
| `narracja_ze_scenami.txt` | ta sama narracja z podziałem na sceny — do redakcji, nie do nagrania |
| `plansze/*.png` | 15 plansz w kolorach marki (14 w 16:9 + konspekt A4) |
| `plansze/*.html` | źródła plansz — edytujesz tekst i renderujesz ponownie |
| `zbuduj_plansze.py` | generator plansz (headless Chromium, bez internetu) |
| `zbuduj_scenariusz.py` | generator tego scenariusza i pliku narracji |
| `zrodla.md` | pełne opisy bibliograficzne źródeł ze sceny 13 |
""")
    (KAT / "scenariusz_filmu.md").write_text("\n".join(m), encoding="utf-8")
    print(f"scenariusz_filmu.md — {len(SCENY)} scen, {slow} słów, ok. {czas//60} min {czas%60} s")
    print("narracja.txt · narracja_ze_scenami.txt")

if __name__ == "__main__":
    main()
