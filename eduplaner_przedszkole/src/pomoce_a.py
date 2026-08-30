# -*- coding: utf-8 -*-
"""Pomoce dydaktyczne do konspektów wersji A (3–4 lata).

Każda pomoc to jedna karta A4 dla nauczyciela: zdjęcie poglądowe „tak ma to
wyglądać", lista rzeczy do przygotowania, trzy kroki użycia i — tam, gdzie
konspekt tego potrzebuje — nagrane polecenie dla dziecka głosem nauczycielki.

Zdjęcia są ilustracjami poglądowymi, nie fotografiami konkretnych produktów:
pokazują układ i charakter pomocy, żeby nauczyciel wiedział, co skompletować.

Osadzanie: obrazy jako JPEG w klasach CSS (każdy raz), nagrania jako <audio>
z data-URI. Rejestr POMOCE_A jest kluczowany numerem konspektu, a build.py
dołącza kartę do modalu tego konspektu.
"""

import base64
from pathlib import Path

_KORZEN = Path(__file__).resolve().parent.parent
_FOTO = _KORZEN / "assets" / "pomoce_a"
_AUDIO = _KORZEN / "assets" / "audio_a"


def _foto(kod):
    dane = base64.b64encode((_FOTO / f"k_{kod}.jpg").read_bytes()).decode()
    return f"data:image/jpeg;base64,{dane}"


def _dzwiek(kod):
    dane = base64.b64encode((_AUDIO / f"{kod}.mp3").read_bytes()).decode()
    return f"data:audio/mpeg;base64,{dane}"


# kod → (nr konspektu, tytuł pomocy, [co przygotować], [trzy kroki], tekst nagrania, wskazówka)
POMOCE = {
 "d1_01": ("D1-01", "Czarodziejski woreczek",
   ["błyszczący woreczek ze sznurkiem ściągającym, nieprzezroczysty",
    "5 drobiazgów o wyraźnie różnej fakturze: szyszka, pompon, gładki koralik, tektura falista, muszla",
    "mały dzwoneczek — sygnał otwarcia woreczka",
    "płaska taca, na której leżą przedmioty przed schowaniem"],
   ["Pokaż dziecku wszystkie przedmioty na tacy i nazwij każdy razem z nim.",
    "Schowaj jeden do woreczka przy dziecku, zadzwoń dzwoneczkiem.",
    "Dziecko wkłada rączkę i zgaduje po dotyku, zanim zajrzy."],
   "Mam tu czarodziejski woreczek. Włóż do niego rączkę i poszukaj czegoś w środku. Nie zaglądaj — najpierw sprawdź paluszkami, co to jest.",
   "Faktury muszą się wyraźnie różnić. Dwa gładkie przedmioty w jednym woreczku to dla trzylatka zagadka nie do rozwiązania."),

 "d1_02": ("D1-02", "Małpka robi to, co ja",
   ["pacynka-małpka na rękę, z wyraźną buzią",
    "bębenek albo tamburyn do wystukiwania rytmu",
    "arkusz naklejek z łapką małpki — do oznaczania udanych prób",
    "lustro w sali, żeby dziecko widziało swój ruch"],
   ["Załóż pacynkę i wykonaj nią jeden prosty ruch: klaśnięcie, tupnięcie.",
    "Poproś dziecko, żeby zrobiło to samo — najpierw razem z tobą.",
    "Za każdą udaną próbę dziecko przykleja sobie łapkę małpki."],
   "To jest małpka. Małpka bardzo lubi, kiedy ktoś robi tak samo jak ona. Popatrz na nią uważnie i zrób to samo.",
   "Pacynka działa lepiej niż polecenie wprost — dziecko naśladuje zabawkę chętniej niż dorosłego i nie czuje się oceniane."),

 "d1_03": ("D1-03", "Klepsydra skarbów",
   ["klepsydra dwuminutowa, najlepiej z kolorowym piaskiem",
    "drewniane pudełko na „skarb dnia” z zamykaną pokrywką",
    "żetony w kształcie diamentów — po jednym za każde przeczekane odwrócenie",
    "parawan albo kącik za regałem, gdzie skarb czeka niewidoczny"],
   ["Pokaż skarb, schowaj go do pudełka i odwróć klepsydrę.",
    "Bawcie się czymś innym, dopóki piasek się nie przesypie.",
    "Po przesypaniu otwórzcie pudełko razem i dodajcie żeton."],
   "Odwracam klepsydrę. Kiedy piasek przesypie się na dół, otworzymy pudełko ze skarbem. A my w tym czasie się pobawimy.",
   "Klepsydra musi być widoczna przez cały czas. Czekanie z sygnałem, który widać, jest dla trzylatka zupełnie inną sytuacją niż czekanie w ciemno."),

 "d1_04": ("D1-04", "Kolorowe domki",
   ["dwa kartonowe domki z wyraźnie różnymi dachami — żółtym i zielonym",
    "klocki dokładnie w tych dwóch kolorach, po 4–5 sztuk",
    "dwa pluszaki w tych samych kolorach — mieszkańcy domków",
    "lniany woreczek do losowania klocków"],
   ["Przedstaw mieszkańców: żółtego i zielonego misia w swoich domkach.",
    "Dziecko losuje klocek z woreczka i niesie go do właściwego domku.",
    "Na koniec razem sprawdźcie, czy każdy klocek trafił do siebie."],
   "Zobacz, mamy dwa domki. W żółtym domku mieszkają żółte rzeczy, a w zielonym zielone. Zanieś klocek do jego domku.",
   "Zacznij od dwóch kolorów, nie od czterech. Trzeci kolor dodaj dopiero wtedy, gdy sortowanie na dwa idzie bez zastanowienia."),

 "d1_05": ("D1-05", "Pudełko z niespodzianką",
   ["cztery pojemniki o różnych zamknięciach: pokrywka, zamek błyskawiczny, zakrętka, kokardka",
    "drobne niespodzianki do środka — po jednej na pojemnik",
    "karta „próbowałem sam” z czterema polami na naklejki",
    "mata antypoślizgowa, żeby pojemnik nie uciekał"],
   ["Ustaw pojemniki w rzędzie, od najłatwiejszego do najtrudniejszego.",
    "Dziecko otwiera po kolei — pomagaj dopiero po jego trzeciej próbie.",
    "Za każdy otwarty samodzielnie pojemnik naklejka na kartę."],
   "W każdym pudełku czeka niespodzianka. Ale każde otwiera się inaczej. Spróbuj sam, a ja poczekam.",
   "Odczekaj trzy próby, zanim pomożesz. To najtrudniejsza część tych zajęć — dla dorosłego, nie dla dziecka."),

 "d2_06": ("D2-06", "Zaproszenie od misia",
   ["pacynka-miś, która „zaprasza” do zabawy",
    "karty-zaproszenia ze zdjęciem konkretnej zabawy z sali",
    "dwa stoliki z gotowymi zestawami, żeby zaproszenie od razu dało się przyjąć",
    "koszyk na wykorzystane zaproszenia"],
   ["Miś podchodzi do dziecka i wręcza kartę ze zdjęciem zabawy.",
    "Dziecko ogląda zdjęcie i idzie do stolika, który na nim widzi.",
    "Po zabawie wrzuca zaproszenie do koszyka — zabawa ma domknięcie."],
   "Miś ma dla ciebie zaproszenie. Zobacz, co jest na obrazku. Chodź, pobawimy się w to razem.",
   "Zdjęcie na karcie musi pokazywać zestaw dokładnie tak, jak stoi na stoliku. Rysunek albo inne ujęcie i trzylatek nie rozpozna, o co chodzi."),

 "d2_07": ("D2-07", "Dwa kroki do końca",
   ["paski z planem obrazkowym — dwa albo trzy okienka, nie więcej",
    "klipsy albo żetony do odhaczania zrobionych kroków",
    "zadania trzyetapowe: nawlekanie, przesypywanie, prosta układanka",
    "pudełko „skończone” z otwieranym wiekiem"],
   ["Pokaż pasek i nazwij razem z dzieckiem, co jest pierwsze.",
    "Po każdym kroku dziecko przypina klips na okienku.",
    "Gotową pracę wkłada do pudełka „skończone”."],
   "Popatrz na nasz plan. Najpierw robimy to, a potem to. Kiedy skończysz, odkładamy pracę do pudełka.",
   "Pudełko „skończone” jest ważniejsze, niż wygląda. Trzylatek potrzebuje fizycznego znaku, że praca się zamknęła — inaczej wraca do niej albo nie może odejść."),

 "d2_08": ("D2-08", "Pociąg dnia",
   ["plan dnia w kształcie pociągu, zawieszony na wysokości wzroku dziecka",
    "zdjęcia aktywności w okienkach wagonów — z waszej sali, nie z internetu",
    "magnetyczna lokomotywka pokazująca, gdzie jesteśmy teraz",
    "dzwonek albo grzechotka jako sygnał zmiany",
    "klepsydra minutowa — „ostatnia chwila” przed przejściem"],
   ["Rano przejdźcie pociąg od początku i nazwijcie wagony.",
    "Przy każdej zmianie przesuń lokomotywkę i zadzwoń.",
    "Minutę przed zmianą odwróć klepsydrę i uprzedź."],
   "Nasz pociąg jedzie przez cały dzień. Teraz jesteśmy tutaj, a zaraz pojedziemy dalej. Zobacz, co będzie następne.",
   "Zdjęcia muszą być z waszej sali. Dziecko rozpoznaje swoje miejsce i swoje zabawki, nie ilustrację przedszkola w ogóle."),

 "d2_09": ("D2-09", "Nasze trzy zasady",
   ["trzy piktogramy zasad na tablicy — dokładnie trzy, nie więcej",
    "gest przypisany każdej zasadzie, ten sam za każdym razem",
    "pacynka „Zapominalski”, która zasady łamie",
    "zielone żetony „udało się”",
    "zdjęcia dzieci z grupy przestrzegających zasad"],
   ["Wprowadź zasady po jednej, każdą z własnym gestem.",
    "Pacynka łamie zasadę — dzieci ją poprawiają i pokazują gest.",
    "Za przestrzeganie w ciągu dnia dziecko dostaje zielony żeton."],
   "Mamy w sali trzy zasady. Popatrz na obrazki i pokaż je razem ze mną. Kiedy ci się uda, dostajesz zielony żeton.",
   "Niech to pacynka łamie zasady, nie dziecko. Poprawianie Zapominalskiego uczy tego samego, ale bez wstydu."),

 "d2_10": ("D2-10", "Wyspa spokoju",
   ["stały kącik z poduszką i kocem — zawsze w tym samym miejscu",
    "dwa, trzy przedmioty kojące: gniotek, butelka sensoryczna",
    "karta z obrazkiem „idę na wyspę”, dostępna dla dziecka",
    "piktogram oddechu: wąchamy kwiatek, dmuchamy świeczkę"],
   ["Pokaż wyspę, gdy dziecko jest spokojne — nie w środku kryzysu.",
    "W trudnej chwili nazwij emocję i zaproponuj wyspę, nie każ.",
    "Usiądź obok i oddychajcie razem według piktogramu."],
   "Widzę, że jest ci teraz trudno. Chodź ze mną na wyspę spokoju. Powąchamy kwiatek i zdmuchniemy świeczkę. Poczekam z tobą.",
   "Wyspa nigdy nie może być karą ani miejscem zsyłki. W chwili, w której stanie się „idź się uspokoić”, przestaje działać."),

 "d3_11": ("D3-11", "Zrób to, o co proszę",
   ["cztery przedmioty codzienne: kubek, łyżka, miś, klocek",
    "koszyk „skrzynia zadań”",
    "obrazki trzech czynności: weź, połóż, daj",
    "pacynka, która czasem wydaje polecenia zamiast dorosłego"],
   ["Nazwij przedmioty razem z dzieckiem, zanim zaczniesz prosić.",
    "Wydaj jedno krótkie polecenie i poczekaj bez powtarzania.",
    "Podziękuj konkretnie: „podałeś mi misia, dziękuję”."],
   "Mam prośbę. Podaj mi proszę misia. Dziękuję, bardzo mi pomogłeś.",
   "Nie powtarzaj polecenia od razu. Trzylatek potrzebuje kilku sekund na przetworzenie — powtórka zaczyna proces od nowa."),

 "d3_12": ("D3-12", "Powiem, czego chcę",
   ["tablica AAC czteropolowa: pić, jeść, toaleta, pomoc",
    "brelok z tymi samymi symbolami — zawsze przy dziecku",
    "kubek, jabłko i symbol toalety jako konkrety obok tablicy",
    "zdjęcia sytuacji, w których symbole się przydają"],
   ["Powieś tablicę tam, gdzie potrzeba naprawdę powstaje: przy stole, przy drzwiach.",
    "Modeluj: sam pokazuj symbol, mówiąc, czego chcesz.",
    "Na każde wskazanie reaguj natychmiast — symbol musi działać."],
   "Chcesz mi coś powiedzieć? Pokaż na tablicy, czego potrzebujesz. Już wiem. Zaraz to przyniosę.",
   "Reaguj na wskazanie zawsze, nawet gdy wiesz, że dziecko nie jest głodne. Symbol, który czasem nie działa, przestaje być używany."),

 "d3_13": ("D3-13", "Zdanie z obrazka",
   ["duże obrazki, na każdym jedna wyraźna czynność",
    "paski do układania zdania — trzy pola: kto, co robi, gdzie",
    "pacynka „ciekawska”, która dopytuje",
    "telefon albo dyktafon do nagrania próbki mowy"],
   ["Pokaż obrazek i zapytaj najpierw: kto tu jest?",
    "Dołóż drugie pytanie: co robi? Ułóż odpowiedzi na paskach.",
    "Poproś o całe zdanie i nagraj je — nagranie pokazuje postęp."],
   "Popatrz na obrazek. Kto tu jest i co robi? Powiedz mi całym zdaniem.",
   "Nagrywaj co dwa tygodnie to samo zdanie. Postępu w mowie nie widać z dnia na dzień, ale w nagraniach sprzed miesiąca słychać go wyraźnie."),

 "d3_14": ("D3-14", "Kto? Co? Gdzie?",
   ["kostka z trzema symbolami pytań: postać, przedmiot, domek",
    "ilustracje sytuacyjne z kilkoma postaciami i przedmiotami",
    "zdjęcia dzieci z grupy i zdjęcia sali",
    "pacynka zadająca pytania zamiast dorosłego"],
   ["Rzuć kostką i nazwij, jakie pytanie wypadło.",
    "Dziecko szuka odpowiedzi na ilustracji i pokazuje palcem.",
    "Dopiero potem poproś o słowo — najpierw wskazanie, potem nazwa."],
   "Rzucamy kostką. Wypadło pytanie: kto tu jest? Poszukaj na obrazku i mi pokaż.",
   "Zaczynaj od zdjęć waszej grupy. „Kto to?” przy znajomej twarzy jest pytaniem o wiele łatwiejszym niż przy obcej ilustracji."),

 "d3_15": ("D3-15", "Twarze i gesty",
   ["cztery duże karty z wyrazistymi minami: wesoła, smutna, zdziwiona, spokojna",
    "dwie karty z gestami: dłoń „stop” i gest „chodź”",
    "lusterko, w którym dziecko widzi własną minę",
    "zdjęcia sytuacji z sali pasujących do każdej miny"],
   ["Pokaż kartę i nazwij minę, potem zrób ją razem z dzieckiem.",
    "Dziecko szuka tej samej miny u siebie w lusterku.",
    "Połącz minę z sytuacją: „kiedy tak wyglądasz, to znaczy, że…”."],
   "Popatrz na te buzie. Ta jest wesoła, a ta smutna. Pokaż mi wesołą buzię w lusterku.",
   "Zacznij od dwóch min, nie od czterech. Wesoła i smutna muszą być pewne, zanim dojdzie zdziwienie."),
}


def style_pomocy():
    """Zdjęcia osadzone raz, w klasach CSS — karta może się powtarzać."""
    regu = "\n".join(f'.pf-{k}{{background-image:url({_foto(k)})}}' for k in POMOCE)
    return f"<style>{regu}</style>"


def audio_pomocy():
    return "".join(f'<audio id="pa-{k}" preload="none" src="{_dzwiek(k)}"></audio>'
                   for k in POMOCE)


def karta(kod, esc):
    nr, tytul, przygotuj, kroki, tekst, wskaz = POMOCE[kod]
    lista = "\n".join(f'      <li>{esc(x)}</li>' for x in przygotuj)
    krok = "\n".join(f'      <li><span class="pk-n">{i}</span>{esc(x)}</li>'
                     for i, x in enumerate(kroki, 1))
    return f'''<section class="zal pomoc" data-poziom="p1">
  <header class="zal-head">
    <span class="mark" role="img" aria-label="Logo PCTP"></span>
    <div>
      <div class="zal-w">EduPlaner 2026</div>
      <div class="zal-s">Pomoc dydaktyczna · konspekt {esc(nr)} · 3–4 lata</div>
    </div>
    <span class="zal-pill p1">druk KC-4</span>
  </header>
  <div class="zal-tytul">
    <span class="zal-kp">Tak ma wyglądać ta pomoc</span>
    <h3>{esc(tytul)}</h3>
  </div>
  <div class="pf pf-{kod}" role="img" aria-label="Zdjęcie poglądowe pomocy: {esc(tytul)}"></div>
  <div class="pomoc-dwie">
    <div><h4 class="pomoc-h">Co przygotować</h4>
    <ul class="klista pomoc-lista">
{lista}
    </ul></div>
    <div><h4 class="pomoc-h">Jak użyć — trzy kroki</h4>
    <ol class="pomoc-kroki">
{krok}
    </ol></div>
  </div>
  <div class="pomoc-glos">
    <button type="button" class="au-btn" data-au="pa-{kod}"
      aria-label="Posłuchaj polecenia"><span aria-hidden="true">▶</span> Posłuchaj polecenia</button>
    <p class="pomoc-tekst">„{esc(tekst)}"</p>
  </div>
  <div class="callout rule pomoc-wsk"><span class="cap">Wskazówka</span>{esc(wskaz)}</div>
  <div class="zal-stopka">
    <span><b>Konspekt {esc(nr)}</b> · pomoc dydaktyczna</span>
    <span class="mono">EduPlaner 2026 · PCTP · druk KC-4</span>
  </div>
</section>'''


def pomoce_dla(nr, esc):
    """Zwraca kartę pomocy dla konspektu o tym numerze albo pusty string."""
    for kod, dane in POMOCE.items():
        if dane[0] == nr:
            return karta(kod, esc)
    return ""
