# -*- coding: utf-8 -*-
"""Pomoce dydaktyczne do konspektów wersji B (5 lat).

Ta sama karta co w wersji A, ale pomoce są trudniejsze: więcej kroków po
stronie dziecka, więcej materiału do wyboru, więcej sytuacji, w których to
dziecko prowadzi zabawę, a nauczyciel tylko przygotowuje warunki.

Układ karty i osadzanie mediów: `pomoce_karta`.
"""

from pomoce_karta import Zestaw

# kod → (nr konspektu, tytuł pomocy, [co przygotować], [trzy kroki], tekst nagrania, wskazówka)
POMOCE = {
 "b1_01": ("B1-01", "Detektywi opowieści",
   ["opowiadania pięciominutowe z wyraźną akcją i jednym zwrotem",
    "lupy detektywistyczne — po jednej na dziecko",
    "karty historyjki obrazkowej, cztery sceny, do ułożenia po czytaniu",
    "odznaki „detektyw opowieści” z filcu",
    "tablica z czterema pytaniami w obrazkach: kto, gdzie, co się stało, dlaczego"],
   ["Rozdaj lupy i odznaki, zapowiedz, że po czytaniu będą pytania.",
    "Czytaj całość, ale zatrzymaj się tuż przed rozwiązaniem akcji.",
    "Po czytaniu dziecko układa cztery sceny i odpowiada na dwa pytania z tablicy."],
   "Dziś jesteśmy detektywami opowieści. Słuchaj uważnie, bo potem zapytam, co się wydarzyło. Weź lupę i szukaj śladów w obrazkach.",
   "Zatrzymaj czytanie tuż przed rozwiązaniem akcji — pięciolatek, który sam próbuje zgadnąć zakończenie, słucha reszty opowiadania inaczej niż ten, któremu wszystko podano."),

 "b1_02": ("B1-02", "Fabryka rytmów",
   ["klocki logiczne różniące się kolorem, kształtem i wielkością",
    "dwie obręcze do segregowania",
    "paski do układania rytmów, długie na co najmniej osiem elementów",
    "taśma produkcyjna z szarego papieru — scenografia fabryki",
    "karty zamówień z wzorem rytmu do odtworzenia"],
   ["Dziecko segreguje klocki do obręczy według jednej cechy i nazywa kryterium.",
    "Zmień kryterium i poproś o przesegregowanie tego samego zbioru.",
    "Podaj kartę zamówienia; dziecko układa rytm dwuelementowy do końca paska."],
   "Nasza fabryka przyjmuje zamówienie. Najpierw poukładaj klocki do obręczy i powiedz mi, dlaczego tak. Potem ułóż rytm z karty, aż do końca paska.",
   "Poproś o nazwanie kryterium — dziecko, które powie „bo są okrągłe”, myśli o cesze; dziecko, które tylko układa, może kopiować układ sąsiada."),

 "b1_03": ("B1-03", "Sklep pod piątką",
   ["kącik sklepowy: drewniane owoce i warzywa, dwa koszyki",
    "listy zakupów z kropkami zamiast cyfr",
    "kasa i żetony do płacenia",
    "trzy płytkie tacki do układania liczonych elementów",
    "kartoniki z cyframi od jednego do dziesięciu"],
   ["Dziecko bierze listę i odczytuje z niej liczbę kropek.",
    "Przekłada towar na tackę po jednym, licząc na głos.",
    "Podaje wynik bez ponownego liczenia i dokłada kartonik z cyfrą."],
   "Otwieramy nasz sklep. Popatrz na listę i przekładaj owoce na tackę, po jednym. Na końcu powiedz mi, ile ich jest.",
   "Tacka rozwiązuje najczęstszy błąd — dziecko liczące w kupce wraca do tych samych przedmiotów; przekładanie po jednym wymusza zasadę jeden do jednego."),

 "b1_04": ("B1-04", "Kwadrans badacza",
   ["licznik kroków z pięcioma polami do zakrywania",
    "zadania wieloetapowe: mozaika, sekwencja, sortowanie",
    "klepsydra dziesięciominutowa, ustawiona w polu widzenia",
    "karta „skończone” do podpisania przez dziecko",
    "słuchawki wygłuszające dostępne bez pytania"],
   ["Pokaż licznik i policzcie razem, ile kroków ma dzisiejsze zadanie.",
    "Po każdym ukończonym kroku dziecko samo zakrywa jedno pole.",
    "Po ostatnim polu podpisujecie kartę „skończone” i odkładacie pracę."],
   "Zaczynamy kwadrans badacza. Popatrz na licznik: masz pięć kroków do zrobienia. Po każdym kroku zakryj jedno pole i pracuj dalej.",
   "Licznik pokazujący, ile zostało, działa lepiej niż zegar odmierzający czas — pięciolatek nie czuje minut, ale doskonale widzi, że zostały dwa pola."),

 "b1_05": ("B1-05", "Polowanie na litery",
   ["karty z pojedynczymi literami i cyframi, duże i wyraźne",
    "litery rozwieszone w sali: na drzwiach, pudełkach, półkach",
    "kartoniki z imionami dzieci",
    "stemple z literami i poduszka do stemplowania",
    "masa plastyczna do lepienia kształtów liter"],
   ["Dziecko bierze kartonik ze swoim imieniem i wybiera z niego jedną literę.",
    "Szuka takiej samej litery w sali i przynosi kartę do stolika.",
    "Utrwala znalezioną literę: odbija stempel albo lepi ją z masy."],
   "Idziemy na polowanie na litery. Weź kartonik ze swoim imieniem i poszukaj takiej samej litery w sali. Kiedy znajdziesz, przynieś ją do mnie.",
   "Zacznij od liter imienia — to jedyny napis, który pięciolatek uważa za naprawdę swój, i właśnie przy nim najszybciej odkrywa, że znaki coś znaczą."),

}


ZESTAW = Zestaw(POMOCE, "pomoce_b", "audio_b", "5 lat")
