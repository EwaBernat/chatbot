# -*- coding: utf-8 -*-
"""Cele SMART do 25 wskaźników z kwestionariusza funkcji zachowania (ABC / FBA).

Kwestionariusz FBA ma pięć funkcji po pięć obserwowanych wskaźników. Każdy
wskaźnik oceniony na 2 albo 3 to deficyt: sytuacja, w której uczeń nie ma
jeszcze zachowania zastępczego pełniącego tę samą funkcję. Ten moduł trzyma do
każdego z nich jeden cel SMART napisany tak jak cele terapeutyczne w banku
konspektów: obserwowalne zachowanie, liczba i horyzont.

Dlaczego jeden cel na wskaźnik, a nie jeden na funkcję. Karta FBA ma już pięć
celów — po jednym na funkcję. Są dobre jako kierunek planu PBS, ale zbyt szerokie
na obserwację pogłębioną: „skorzysta z ustalonej strategii wyciszenia" nie mówi,
w której z pięciu sytuacji napięcia mierzymy postęp. Cele z tego modułu rozpisują
tamte pięć na konkretne wyzwalacze z kwestionariusza, więc każdy da się policzyć
w rejestrze ABC.

Kryterium i horyzont **nie są wpisane w treść celu** — wynikają z punktacji
funkcji u konkretnego ucznia, tak samo jak w banku horyzont wynika z poziomu
wsparcia (III — 4 tygodnie, II — 8, I — 12):

    10–15 pkt · dominująca   →  8 z 10 sytuacji · 4 tygodnie
     5–9  pkt · istotna      →  7 z 10 sytuacji · 8 tygodni
     0–4  pkt · słaba        →  6 z 10 sytuacji · 12 tygodni

Funkcja dominująca dostaje najkrótszy horyzont nie dlatego, że jest łatwiejsza,
tylko dlatego, że jest priorytetem planu — sprawdzamy ją najczęściej.

Zapis `{proba}` i `{horyzont}` w treści celu podstawia `build_cele_fba.py`.
"""

# ——— skala kwestionariusza → kryterium i horyzont ————————————————————————
# Horyzont w trzech formach, bo wchodzi w trzy różne zdania: „w ciągu 4 tygodni",
# „weryfikacja po 4 tygodniach", „4 tygodnie" na plakietce. Jedna forma dla
# wszystkich trzech dawała „po 4 tygodni" — druk, który idzie do rodzica.
PROGI = [
    (10, "Dominująca", "8 z 10", "4 tygodni",  "4 tygodniach",  "4 tygodnie",  "priorytet planu PBS"),
    (5,  "Istotna",    "7 z 10", "8 tygodni",  "8 tygodniach",  "8 tygodni",   "do uwzględnienia"),
    (0,  "Słaba",      "6 z 10", "12 tygodni", "12 tygodniach", "12 tygodni",  "drugorzędna"),
]


def ocena(wynik):
    """Ocena funkcji dla punktacji 0–15.

    Zwraca `(nazwa, próby, horyzont dopełniacz, horyzont miejscownik,
    horyzont mianownik, znaczenie dla planu)`.
    """
    for prog, *reszta in PROGI:
        if wynik >= prog:
            return tuple(reszta)
    raise ValueError(wynik)


# ——— pięć funkcji, po pięć wskaźników ————————————————————————————————————
FUNKCJE = [
 dict(rzym="I", nazwa="Ucieczka / unikanie", skrot="Ucieczka",
      opis="Zachowanie nasila się przy trudnych i nielubianych zadaniach, "
           "a wygasa po ich odpuszczeniu.",
      pbs="Nie zwalniamy z zadania po zachowaniu trudnym — inaczej wzmacniamy "
          "ucieczkę. Zamiast tego: krótsze partie, stopniowanie trudności "
          "i przerwa „na prośbę”.",
      wskazniki=[
  dict(deficyt="Zachowanie pojawia się, gdy uczennica ma wykonać trudne lub nielubiane zadanie.",
       cel="Uczennica rozpocznie trudne zadanie w ciągu 1 minuty od polecenia, korzystając "
           "z karty „zacznij od jednego kroku”, w {proba} sytuacji, w ciągu {horyzont}.",
       smart=[("S", "Bierze przybory i wykonuje pierwszy krok zadania."),
              ("M", "1 minuta od polecenia; {proba} sytuacji."),
              ("A", "Karta zdejmuje decyzję, od czego zacząć."),
              ("R", "Rozpoczęcie jest warunkiem korzystania z lekcji."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — kolumna A: polecenie zadania pisemnego.",
       ile="10 poleceń w tygodniu"),
  dict(deficyt="Zachowanie nasila się przy poleceniach lub wymaganiach.",
       cel="Uczennica wykona polecenie po jednokrotnym powtórzeniu i zapowiedzi „za dwie minuty "
           "kończymy”, bez zachowania trudnego, w {proba} poleceń, w ciągu {horyzont}.",
       smart=[("S", "Wykonuje polecenie bez odmowy, krzyku i wyjścia z ławki."),
              ("M", "Jedno powtórzenie; {proba} poleceń."),
              ("A", "Zapowiedź czasu uprzedza o końcu, nie zaskakuje."),
              ("R", "Polecenia wracają na każdej lekcji, u każdego dorosłego."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr poleceń — liczymy wykonane po pierwszym powtórzeniu.",
       ile="10 poleceń w tygodniu"),
  dict(deficyt="Po zachowaniu uczennica zostaje zwolniona z zadania lub wyprowadzona.",
       cel="Uczennica wróci do przerwanego zadania po trzyminutowej przerwie i wykona ustaloną, "
           "skróconą część, w {proba} przerw, w ciągu {horyzont}.",
       smart=[("S", "Wraca do ławki i kończy uzgodnioną część zadania."),
              ("M", "3 minuty przerwy; {proba} przerw."),
              ("A", "Skrócona część jest wykonalna po wzburzeniu."),
              ("R", "Powrót do zadania przerywa błędne koło ucieczki."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — kolumna C: co następuje po przerwie.",
       ile="każda przerwa w tygodniu"),
  dict(deficyt="Zachowanie rzadziej występuje, gdy zadanie jest łatwe lub atrakcyjne.",
       cel="Uczennica podejmie zadanie trudniejsze ustawione po dwóch łatwych (zasada „dwa łatwe, "
           "jedno trudne”), w {proba} serii, w ciągu {horyzont}.",
       smart=[("S", "Zaczyna trzecie, trudniejsze zadanie w serii."),
              ("M", "Serie 2 + 1; {proba} serii."),
              ("A", "Dwa sukcesy z rzędu budują gotowość na trudność."),
              ("R", "Trudniejszych zadań nie da się z lekcji usunąć."),
              ("T", "Weryfikacja po {po}.")],
       obs="Karta serii zadań — zaznaczamy podjęcie trzeciego.",
       ile="5 serii w tygodniu"),
  dict(deficyt="Po „odpuszczeniu” zadania zachowanie ustaje — ucieczka działa.",
       cel="Uczennica poprosi o przerwę kartą „przerwa” albo słowami, zamiast przerywać zadanie "
           "zachowaniem trudnym, w {proba} sytuacji narastania oporu, w ciągu {horyzont}.",
       smart=[("S", "Podnosi kartę „przerwa” albo mówi: „potrzebuję przerwy”."),
              ("M", "{proba} sytuacji narastania oporu."),
              ("A", "Karta leży na ławce przez całą lekcję."),
              ("R", "Prośba o przerwę pełni tę samą funkcję, co ucieczka."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — czy przed zachowaniem pojawiła się prośba.",
       ile="wszystkie sytuacje oporu"),
      ]),
 dict(rzym="II", nazwa="Sensoryczne / autostymulacja", skrot="Sensoryczne",
      opis="Zachowanie pojawia się także w samotności, dostarcza wrażeń i trudno je przerwać.",
      pbs="Zaplanowane przerwy sensoryczne i akceptowalne źródła stymulacji (dieta sensoryczna), "
          "nauka sygnalizowania potrzeby regulacji, współpraca z terapeutą SI.",
      wskazniki=[
  dict(deficyt="Zachowanie pojawia się także, gdy uczennica jest sama.",
       cel="Uczennica sięgnie po ustalony przedmiot do regulacji (gniotek, taśma na nodze krzesła) "
           "podczas pracy samodzielnej, w {proba} dziesięciominutowych odcinków pracy, w ciągu {horyzont}.",
       smart=[("S", "Sięga po przedmiot z ustalonego miejsca i wraca do zadania."),
              ("M", "Odcinki po 10 minut; {proba} odcinków."),
              ("A", "Przedmiot jest w zasięgu ręki, bez proszenia."),
              ("R", "Praca samodzielna to najdłuższy odcinek dnia bez dorosłego."),
              ("T", "Weryfikacja po {po}.")],
       obs="Arkusz próbek czasowych — co 10 minut pracy samodzielnej.",
       ile="10 odcinków w tygodniu"),
  dict(deficyt="Zachowanie wydaje się dostarczać przyjemnych wrażeń (ruch, dźwięk, dotyk).",
       cel="Uczennica wskaże na karcie diety sensorycznej, jakiego wrażenia potrzebuje (ruch, ucisk, "
           "dźwięk), i skorzysta z odpowiadającej mu formy, w {proba} przerw sensorycznych, w ciągu {horyzont}.",
       smart=[("S", "Wskazuje pole na karcie i wybiera formę z tego pola."),
              ("M", "Trzy rodzaje wrażeń; {proba} przerw."),
              ("A", "Karta ma po dwie propozycje na każde wrażenie."),
              ("R", "Nazwane wrażenie można zaspokoić inaczej niż zachowaniem trudnym."),
              ("T", "Weryfikacja po {po}.")],
       obs="Karta diety sensorycznej — zapis wyboru i formy.",
       ile="wszystkie przerwy sensoryczne"),
  dict(deficyt="Zachowanie występuje niezależnie od reakcji otoczenia.",
       cel="Uczennica skorzysta z zaplanowanej przerwy sensorycznej po sygnale minutnika, bez "
           "przypominania dorosłego, w {proba} zaplanowanych przerw, w ciągu {horyzont}.",
       smart=[("S", "Po sygnale wstaje i idzie do miejsca przerwy."),
              ("M", "{proba} zaplanowanych przerw, bez przypomnienia."),
              ("A", "Minutnik stoi na ławce, sygnał jest ten sam co dzień."),
              ("R", "Przerwa uprzedzająca jest tańsza niż przerywanie zachowania."),
              ("T", "Weryfikacja po {po}.")],
       obs="Plan przerw — odhaczenie przerwy wziętej samodzielnie.",
       ile="4 przerwy dziennie"),
  dict(deficyt="Zachowanie nasila się przy nudzie lub braku aktywności.",
       cel="Uczennica wybierze zajęcie z listy trzech aktywności „gdy skończę wcześniej” i zajmie się "
           "nim przez 5 minut, w {proba} sytuacji oczekiwania, w ciągu {horyzont}.",
       smart=[("S", "Wybiera z listy i pracuje przy wybranym zajęciu."),
              ("M", "5 minut; {proba} sytuacji oczekiwania."),
              ("A", "Lista wisi przy ławce, wybór jest z trzech, nie z wielu."),
              ("R", "Puste minuty po zadaniu wracają na każdej lekcji."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — kolumna A: koniec zadania przed czasem.",
       ile="wszystkie sytuacje oczekiwania"),
  dict(deficyt="Zachowanie trudno przerwać uwagą lub poleceniem.",
       cel="Uczennica zakończy autostymulację w ciągu 30 sekund od umówionego sygnału („stop — zamiana”) "
           "i przejdzie do formy zastępczej, w {proba} sygnałów, w ciągu {horyzont}.",
       smart=[("S", "Odkłada to, czym się stymuluje, i bierze formę zastępczą."),
              ("M", "30 sekund od sygnału; {proba} sygnałów."),
              ("A", "Sygnał jest wzrokowo-dotykowy, nie słowny — słowa nie docierają."),
              ("R", "Przerwanie bez konfrontacji chroni relację z dorosłym."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — czas od sygnału do zakończenia.",
       ile="wszystkie sygnały w tygodniu"),
      ]),
 dict(rzym="III", nazwa="Uwaga", skrot="Uwaga",
      opis="Zachowanie pojawia się, gdy dorosły jest zajęty, przynosi uwagę (upomnienie) "
           "i nasila się przy publiczności.",
      pbs="Uwaga „z wyprzedzeniem” i pozytywna za zachowania pożądane, nauka właściwego sposobu "
          "proszenia o uwagę, minimalna reakcja na zachowanie trudne, spójny plan wzmocnień.",
      wskazniki=[
  dict(deficyt="Zachowanie pojawia się, gdy dorosły zajmuje się czymś innym.",
       cel="Uczennica położy na ławce kartę „potrzebuję pomocy” i poczeka 2 minuty, gdy nauczyciel "
           "zajmuje się kimś innym, w {proba} sytuacji, w ciągu {horyzont}.",
       smart=[("S", "Kładzie kartę i zostaje przy ławce do podejścia dorosłego."),
              ("M", "2 minuty czekania; {proba} sytuacji."),
              ("A", "Karta działa bez mówienia i bez podchodzenia do nauczyciela."),
              ("R", "Nauczyciel bywa zajęty na każdej lekcji — tego nie da się usunąć."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — kolumna A: dorosły zajęty innym uczniem.",
       ile="wszystkie takie sytuacje"),
  dict(deficyt="Po zachowaniu uczennica otrzymuje uwagę (upomnienie, rozmowę).",
       cel="Uczennica poprosi o uwagę dorosłego przez podniesienie ręki, zamiast zachowaniem trudnym, "
           "w {proba} sytuacji potrzeby kontaktu, w ciągu {horyzont}.",
       smart=[("S", "Podnosi rękę i czeka na podejście albo skinienie."),
              ("M", "{proba} sytuacji potrzeby kontaktu."),
              ("A", "Dorosły odpowiada na rękę od razu, na zachowanie trudne — minimalnie."),
              ("R", "To zachowanie zastępcze o tej samej funkcji: uwaga."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — którą drogą uczennica uzyskała uwagę.",
       ile="wszystkie sytuacje kontaktu"),
  dict(deficyt="Zachowanie nasila się w grupie lub przy publiczności.",
       cel="Uczennica zgłosi się do wypowiedzi w ustalonym momencie zajęć („runda”), nie przerywając "
           "innym, w {proba} zajęć grupowych, w ciągu {horyzont}.",
       smart=[("S", "Mówi w swojej kolejce w rundzie, bez wchodzenia w słowo."),
              ("M", "{proba} zajęć grupowych."),
              ("A", "Runda gwarantuje jej głos — nie musi go zdobywać."),
              ("R", "Praca w grupie to codzienna forma zajęć w klasie III."),
              ("T", "Weryfikacja po {po}.")],
       obs="Karta zajęć grupowych — zgłoszenia i wejścia w słowo.",
       ile="wszystkie zajęcia grupowe"),
  dict(deficyt="Zachowanie ustaje, gdy uczennica dostanie indywidualną uwagę.",
       cel="Uczennica skorzysta z zaplanowanych 2 minut uwagi „z wyprzedzeniem” na początku lekcji "
           "i wróci do zadania po sygnale, w {proba} lekcji, w ciągu {horyzont}.",
       smart=[("S", "Rozmawia 2 minuty i po sygnale siada do zadania."),
              ("M", "2 minuty na starcie; {proba} lekcji."),
              ("A", "Uwaga dana z góry jest tańsza niż odzyskiwana po wybuchu."),
              ("R", "Zapobiega zachowaniu, zamiast na nie reagować."),
              ("T", "Weryfikacja po {po}.")],
       obs="Plan lekcji — odhaczenie rozmowy i powrotu do zadania.",
       ile="wszystkie lekcje"),
  dict(deficyt="Uczennica patrzy na reakcję dorosłego w trakcie zachowania.",
       cel="Uczennica nawiąże kontakt z dorosłym umówionym gestem (uniesiona dłoń), zamiast sprawdzać "
           "jego reakcję zachowaniem trudnym, w {proba} obserwowanych sytuacji, w ciągu {horyzont}.",
       smart=[("S", "Unosi dłoń i czeka na skinienie dorosłego."),
              ("M", "{proba} obserwowanych sytuacji."),
              ("A", "Gest jest krótszy niż podejście i nie przerywa lekcji."),
              ("R", "Sprawdzanie reakcji to prośba o kontakt, nie prowokacja."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — czy przed zachowaniem pojawił się gest.",
       ile="wszystkie obserwowane sytuacje"),
      ]),
 dict(rzym="IV", nazwa="Dostęp do przedmiotu / aktywności", skrot="Dostęp",
      opis="Zachowanie nasila się przy odmowie lub zabraniu przedmiotu, a wygasa po jego uzyskaniu.",
      pbs="Nauka proszenia i czekania (odraczanie gratyfikacji), jasne zasady dostępu, system żetonowy; "
          "przedmiotu nie wydajemy bezpośrednio po zachowaniu trudnym.",
      wskazniki=[
  dict(deficyt="Zachowanie pojawia się, gdy uczennica nie może dostać tego, czego chce.",
       cel="Uczennica przyjmie odmowę i wybierze jedną z dwóch zaproponowanych alternatyw, "
           "w {proba} odmów, w ciągu {horyzont}.",
       smart=[("S", "Wskazuje jedną z dwóch propozycji i zajmuje się nią."),
              ("M", "Dwie alternatywy; {proba} odmów."),
              ("A", "Wybór zostawia jej sprawczość mimo odmowy."),
              ("R", "Odmowa jest nieusuwalną częścią dnia w szkole."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — kolumna A: odmowa dorosłego.",
       ile="wszystkie odmowy"),
  dict(deficyt="Zachowanie nasila się przy odmowie lub zabraniu przedmiotu.",
       cel="Uczennica odda przedmiot po zapowiedzi „jeszcze dwie minuty” i sygnale minutnika, "
           "w {proba} sytuacji kończenia aktywności, w ciągu {horyzont}.",
       smart=[("S", "Odkłada przedmiot na ustalone miejsce po sygnale."),
              ("M", "2 minuty zapowiedzi; {proba} sytuacji."),
              ("A", "Zapowiedź zamienia zabranie w zakończenie."),
              ("R", "Zabieranie przedmiotu bez uprzedzenia było wyzwalaczem."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — zapowiedź, sygnał, reakcja.",
       ile="wszystkie zakończenia aktywności"),
  dict(deficyt="Po zachowaniu uczennica otrzymuje pożądany przedmiot lub aktywność.",
       cel="Uczennica poprosi o przedmiot pełnym zwrotem („poproszę o…”), zamiast sięgać po niego "
           "zachowaniem trudnym, w {proba} sytuacji, w ciągu {horyzont}.",
       smart=[("S", "Mówi „poproszę o…” i czeka na odpowiedź."),
              ("M", "{proba} sytuacji, w których czegoś chce."),
              ("A", "Zwrot jest krótki i ten sam u wszystkich dorosłych."),
              ("R", "Prośba pełni tę samą funkcję, co zachowanie trudne."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — którą drogą uczennica uzyskała przedmiot.",
       ile="wszystkie sytuacje"),
  dict(deficyt="Zachowanie ustaje, gdy uczennica dostanie to, czego chciała.",
       cel="Uczennica poczeka na przedmiot 3 minuty, korzystając z wizualnego licznika, "
           "w {proba} sytuacji odroczenia, w ciągu {horyzont}.",
       smart=[("S", "Zostaje przy swojej ławce do końca odliczania."),
              ("M", "3 minuty; {proba} sytuacji odroczenia."),
              ("A", "Licznik pokazuje koniec czekania — czas przestaje być nieznany."),
              ("R", "Czekanie jest warunkiem pracy w grupie 25 osób."),
              ("T", "Weryfikacja po {po}.")],
       obs="Karta odroczeń — czas czekania i wynik.",
       ile="5 odroczeń w tygodniu"),
  dict(deficyt="Zachowanie występuje przy oczekiwaniu na coś atrakcyjnego.",
       cel="Uczennica wykona ustaloną czynność „w międzyczasie” (zadanie z żetonem) w czasie "
           "oczekiwania na atrakcyjną aktywność, w {proba} sytuacji oczekiwania, w ciągu {horyzont}.",
       smart=[("S", "Bierze zadanie z pudełka i pracuje przy nim do sygnału."),
              ("M", "{proba} sytuacji oczekiwania."),
              ("A", "Żeton łączy czekanie z nagrodą, nie z pustką."),
              ("R", "Oczekiwanie na atrakcję wraca przy każdej wycieczce i przerwie."),
              ("T", "Weryfikacja po {po}.")],
       obs="Karta żetonowa — żeton za czynność w międzyczasie.",
       ile="wszystkie sytuacje oczekiwania"),
      ]),
 dict(rzym="V", nazwa="Regulacja emocji / napięcie", skrot="Regulacja emocji",
      opis="Zachowanie wybucha przy zmianie lub przeciążeniu, z objawami napięcia, "
           "i jest trudne do przewidzenia.",
      pbs="Przewidywalność (plan dnia, uprzedzanie zmian), strefa wyciszenia i strategie regulacji "
          "(oddech, przerwa), wsparcie dorosłego przy pierwszych sygnałach napięcia.",
      wskazniki=[
  dict(deficyt="Zachowanie pojawia się przy zmianie, niespodziance lub przeciążeniu.",
       cel="Uczennica przejdzie do zmienionej aktywności po uprzedzeniu i pokazaniu zmiany na planie "
           "dnia, bez zachowania trudnego, w {proba} zapowiedzianych zmian, w ciągu {horyzont}.",
       smart=[("S", "Ogląda zmianę na planie i przechodzi do nowej aktywności."),
              ("M", "{proba} zapowiedzianych zmian."),
              ("A", "Plan dnia wisi na wysokości jej wzroku, karty się przekładają."),
              ("R", "Zmiana planu w szkole jest nie do uniknięcia."),
              ("T", "Weryfikacja po {po}.")],
       obs="Plan dnia — zapis zmiany i reakcji.",
       ile="wszystkie zmiany planu"),
  dict(deficyt="Zachowaniu towarzyszą objawy napięcia (płacz, pobudzenie).",
       cel="Uczennica nazwie swoje napięcie na termometrze emocji (zielony — żółty — czerwony) "
           "przy pierwszych objawach, w {proba} sytuacji, w ciągu {horyzont}.",
       smart=[("S", "Wskazuje kolor na termometrze i mówi, co czuje."),
              ("M", "Trzy poziomy; {proba} sytuacji napięcia."),
              ("A", "Termometr leży na ławce, wskazanie nie wymaga słów."),
              ("R", "Nazwane napięcie daje się obniżyć, zanim wybuchnie."),
              ("T", "Weryfikacja po {po}.")],
       obs="Termometr emocji — zapis wskazań w ciągu dnia.",
       ile="wszystkie sytuacje napięcia"),
  dict(deficyt="Zachowanie występuje w sytuacjach stresu lub przebodźcowania.",
       cel="Uczennica skorzysta ze strefy wyciszenia przez 5 minut, na własną prośbę albo propozycję "
           "dorosłego, w {proba} sytuacji przebodźcowania, w ciągu {horyzont}.",
       smart=[("S", "Idzie do strefy i zostaje tam do końca odliczania."),
              ("M", "5 minut; {proba} sytuacji przebodźcowania."),
              ("A", "Strefa jest w sali, wejście nie wymaga zgody za każdym razem."),
              ("R", "Wyjście z bodźców przerywa narastanie, zanim dojdzie do wybuchu."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr strefy wyciszenia — kto zainicjował i jak długo.",
       ile="wszystkie sytuacje przebodźcowania"),
  dict(deficyt="Zachowanie ustaje po wyciszeniu lub odzyskaniu równowagi.",
       cel="Uczennica wróci do zajęć w ciągu 5 minut od zakończenia strategii wyciszenia, "
           "w {proba} sytuacji, w ciągu {horyzont}.",
       smart=[("S", "Wraca do ławki i podejmuje bieżące zadanie."),
              ("M", "5 minut od końca strategii; {proba} sytuacji."),
              ("A", "Po powrocie dostaje zadanie skrócone, nie zaległe w całości."),
              ("R", "Bez powrotu wyciszenie staje się ucieczką z lekcji."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr strefy wyciszenia — czas powrotu do zajęć.",
       ile="wszystkie wyciszenia"),
  dict(deficyt="Zachowanie jest trudne do przewidzenia, wybucha nagle.",
       cel="Uczennica zasygnalizuje czerwoną kartą pierwszy sygnał napięcia, zanim dojdzie do wybuchu, "
           "w {proba} obserwowanych narastań, w ciągu {horyzont}.",
       smart=[("S", "Podnosi czerwoną kartę przed wybuchem, nie po nim."),
              ("M", "{proba} obserwowanych narastań napięcia."),
              ("A", "Karta jest zawsze w tym samym miejscu ławki."),
              ("R", "To jedyny cel, który skraca fazę nagłego wybuchu."),
              ("T", "Weryfikacja po {po}.")],
       obs="Rejestr ABC — sygnał ucznia przed zachowaniem (tak/nie).",
       ile="wszystkie narastania napięcia"),
      ]),
]
