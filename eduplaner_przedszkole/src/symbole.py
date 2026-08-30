# -*- coding: utf-8 -*-
"""Biblioteka symboli obrazkowych — wspólna dla wszystkich wersji i konspektów.

Konspekty proszą o materiał do wydruku 243 razy, ale nie o 243 różne komplety.
„Mycie rąk", „plan dnia", „proszę o pomoc", „radość" wracają w wersji A, B, C
i U. Rysowanie ich osobno dla każdego konspektu byłoby nie tylko marnotrawstwem
miejsca — byłoby błędem merytorycznym. Dziecko korzystające z komunikacji
obrazkowej musi widzieć TEN SAM symbol pomocy na tablicy AAC, w planie dnia
i na breloku; symbol, który zmienia wygląd między materiałami, przestaje być
słowem.

Dlatego symbol powstaje raz, leży tutaj pod swoim kodem, a arkusze w
`karty_druk.py` tylko się do niego odwołują. Plik obrazu:
`assets/symbole/k_<kod>.jpg` (skadrowany przez `kompresuj_media.py`).

Symbol jeszcze nienarysowany po prostu nie ma pliku — `karty_druk.py` pomija
wtedy arkusz, więc dokumenty budują się poprawnie na każdym etapie pracy.
Podpis jest tym, co dziecko i nauczyciel widzą pod obrazkiem; `opis` to
instrukcja dla modelu rysującego i nie trafia do dokumentu.

Karty emocji rysujemy z jawnym zastrzeżeniem: **to samo dziecko na każdej
karcie** (krótkie jasne włosy, brzoskwiniowa skóra, zielona koszulka) i **skóra
nigdy nie przyjmuje koloru emocji**. Pierwsze podejście dało czerwoną twarz przy
złości i zieloną przy zdziwieniu — na karcie emocji kolor twarzy staje się wtedy
wskazówką zamiast miny, a kart nie da się ze sobą porównać. Dziecko zestawia te
twarze między sobą, więc różnić je ma wyłącznie wyraz.
"""

from pathlib import Path

KATALOG = Path(__file__).resolve().parent.parent / "assets" / "symbole"

# kod → (podpis na karcie, opis dla modelu rysującego)
SYMBOLE = {
 # ——— zabawy i kąciki ———————————————————————————————————————————————
 "zabawa_klocki":    ("Klocki", "a stack of wooden building blocks"),
 "zabawa_ukladanka": ("Układanka", "four jigsaw puzzle pieces"),
 "zabawa_rysowanie": ("Rysowanie", "a child's drawing of a sun with crayons beside it"),
 "zabawa_lalki":     ("Kącik lalek", "a rag doll standing next to a toy pram"),
 "zabawa_auta":      ("Samochody", "two toy cars on a small ramp"),
 "zabawa_ksiazki":   ("Książeczki", "an open picture book and a closed book"),

 # ——— plan dnia ————————————————————————————————————————————————————
 "dzien_przyjscie":   ("Przychodzę", "a child waving goodbye at a nursery door, hanging up a coat"),
 "dzien_powitanie":   ("Powitanie w kole", "three children sitting in a circle on a rug, waving"),
 "dzien_sniadanie":   ("Śniadanie", "a bowl of porridge, a slice of bread and a mug on a table"),
 "dzien_zajecia":     ("Zajęcia", "a child at a table with paper and crayons, a teacher pointing"),
 "dzien_zabawa":      ("Zabawa dowolna", "two children playing with blocks and a toy car on a rug"),
 "dzien_sprzatanie":  ("Sprzątanie", "a child putting toys into a storage box"),
 "dzien_spacer":      ("Spacer", "two children in jackets walking outdoors holding hands"),
 "dzien_obiad":       ("Obiad", "a plate of soup with a spoon and a glass of water"),
 "dzien_lezakowanie": ("Leżakowanie", "a child asleep on a small cot under a blanket"),
 "dzien_podwieczorek":("Podwieczorek", "an apple, a yoghurt cup and a mug of tea"),
 "dzien_powrot":      ("Idę do domu", "a child holding a parent's hand walking out of a door"),

 # ——— emocje ———————————————————————————————————————————————————————
 "emocja_radosc":     ("Radość", "a child's face, broad happy smile, bright eyes"),
 "emocja_zlosc":      ("Złość", "a child's face, angry, furrowed brows, mouth turned down"),
 "emocja_smutek":     ("Smutek", "a child's face, sad, one tear on the cheek"),
 "emocja_strach":     ("Strach", "a child's face, frightened, wide eyes, hands near the cheeks"),
 "emocja_spokoj":     ("Spokój", "a child's face, calm and relaxed, eyes gently closed, faint smile"),
 "emocja_zdziwienie": ("Zdziwienie", "a child's face, surprised, raised eyebrows, round open mouth"),
 "emocja_duma":       ("Duma", "a child's face smiling with the chin lifted, hands on hips"),
 "emocja_zmeczenie":  ("Zmęczenie", "a child's face yawning, one hand rubbing an eye"),

 # ——— prośby (tablica AAC) —————————————————————————————————————————
 "prosze_pic":        ("Chcę pić", "a mug of water with a drinking straw"),
 "prosze_jesc":       ("Chcę jeść", "a plate with a fork and a spoon beside it"),
 "prosze_toaleta":    ("Toaleta", "a toilet bowl with the lid open"),
 "prosze_pomoc":      ("Pomocy", "an open raised hand of an adult next to a smaller child's hand"),
 "prosze_odpoczynek": ("Odpoczynek", "a cushion and a folded blanket on the floor"),
 "prosze_boli":       ("Boli mnie", "a child pointing at a plaster on the knee"),
 "prosze_ruch":       ("Chcę pobiegać", "a child running with arms swinging"),
 "prosze_cisza":      ("Chcę być sam", "a child sitting alone in a quiet reading corner"),

 # ——— gesty i polecenia —————————————————————————————————————————————
 "gest_stop":         ("Stop", "an open palm held up facing forward, stop gesture"),
 "gest_chodz":        ("Chodź", "a hand beckoning with the index finger, come here gesture"),
 "gest_slucham":      ("Słucham", "a child cupping a hand behind the ear, listening"),
 "gest_mowie":        ("Mówię", "a child speaking with a small speech bubble by the mouth"),
 "gest_czekam":       ("Czekam", "a child sitting with hands folded in the lap, waiting"),
 "gest_brawo":        ("Brawo", "two hands clapping together"),
 "polecenie_wez":     ("Weź", "a hand picking up a small red cube from a table"),
 "polecenie_poloz":   ("Połóż", "a hand placing a red cube down onto a table"),
 "polecenie_daj":     ("Daj mi", "a hand passing a red cube to another open hand"),
 "polecenie_otworz":  ("Otwórz", "a hand opening the lid of a box"),
 "polecenie_zamknij": ("Zamknij", "a hand closing the lid of a box"),

 # ——— mycie rąk, toaleta, ubieranie ————————————————————————————————
 "myje_woda":      ("Odkręcam wodę", "a hand turning a tap on, water running into a basin"),
 "myje_mydlo":     ("Biorę mydło", "a hand under a soap dispenser, a drop of soap falling"),
 "myje_pocieram":  ("Pocieram ręce", "two soapy hands rubbing together with foam"),
 "myje_splukuje":  ("Spłukuję", "two hands under running water from a tap"),
 "myje_wycieram":  ("Wycieram ręce", "two hands drying on a hanging towel"),
 "toaleta_siusiu": ("Siusiam", "a toilet bowl with a small step stool in front of it"),
 "toaleta_spluczka":("Spuszczam wodę", "a hand pressing the flush button on a cistern"),
 "toaleta_rece":   ("Myję ręce", "two hands under running water at a low basin"),
 "ubior_majtki":   ("Majtki", "a pair of children's underpants"),
 "ubior_spodnie":  ("Spodnie", "a pair of children's trousers"),
 "ubior_skarpetki":("Skarpetki", "a pair of children's socks"),
 "ubior_koszulka": ("Koszulka", "a child's short-sleeved t-shirt"),
 "ubior_sweter":   ("Sweter", "a child's knitted jumper"),
 "ubior_kurtka":   ("Kurtka", "a child's zip-up jacket"),
 "ubior_buty":     ("Buty", "a pair of children's shoes with laces"),

 # ——— strategie radzenia sobie —————————————————————————————————————
 "strategia_oddech":  ("Oddycham", "a child smelling a flower held in one hand, cheeks relaxed"),
 "strategia_przerwa": ("Robię przerwę", "a child sitting in a quiet corner with a cushion"),
 "strategia_pomoc":   ("Proszę o pomoc", "a child raising a hand towards a teacher"),
 "strategia_czesci":  ("Dzielę na części", "a large task card split into three smaller numbered cards"),
 "strategia_woda":    ("Piję wodę", "a child drinking from a mug"),
 "strategia_ruch":    ("Rozruszam się", "a child jumping with arms raised"),

 # ——— pogoda ———————————————————————————————————————————————————————
 "pogoda_slonce": ("Słonecznie", "a bright sun with rays"),
 "pogoda_chmury": ("Pochmurno", "two grey and white clouds"),
 "pogoda_deszcz": ("Deszcz", "a cloud with raindrops falling"),
 "pogoda_snieg":  ("Śnieg", "a cloud with snowflakes falling"),
 "pogoda_wiatr":  ("Wietrznie", "a bare tree bending with curved wind lines"),
 "pogoda_mroz":   ("Mróz", "a thermometer showing a low temperature next to a snowflake"),

 # ——— ruch —————————————————————————————————————————————————————————
 "ruch_bieg":       ("Biegnę", "a child running"),
 "ruch_skok":       ("Skaczę", "a child jumping with both feet off the ground"),
 "ruch_czworaki":   ("Czworakuję", "a child crawling on hands and knees"),
 "ruch_wspinanie":  ("Wspinam się", "a child climbing a small ladder"),
 "ruch_rzut":       ("Rzucam", "a child throwing a ball"),
 "ruch_rownowaga":  ("Idę po linii", "a child walking along a low balance beam with arms out"),

 # ——— techniki plastyczne ——————————————————————————————————————————
 "technika_wydzieranka": ("Wydzieranka", "torn coloured paper pieces glued into a shape"),
 "technika_stempel":     ("Stempel", "a potato stamp printing a shape onto paper"),
 "technika_kolaz":       ("Kolaż", "paper, fabric and buttons glued onto a sheet"),
 "technika_malowanie":   ("Malowanie", "a paintbrush and a palette of paints"),
 "technika_lepienie":    ("Lepienie", "hands shaping a ball of modelling clay"),

 # ——— instytucje i zawody ——————————————————————————————————————————
 "miejsce_przedszkole": ("Przedszkole", "a small nursery building with a playground"),
 "miejsce_przychodnia": ("Przychodnia", "a clinic building with a cross sign"),
 "miejsce_poczta":      ("Poczta", "a post office building with a letter box"),
 "miejsce_straz":       ("Straż pożarna", "a fire station with a fire engine"),
 "miejsce_biblioteka":  ("Biblioteka", "a library building with shelves of books seen through a window"),
 "miejsce_sklep":       ("Sklep", "a small grocery shop with fruit crates outside"),
 "zawod_lekarz":     ("Lekarz", "a doctor holding a stethoscope"),
 "zawod_strazak":    ("Strażak", "a firefighter in a helmet holding a hose"),
 "zawod_kucharz":    ("Kucharz", "a cook in a white hat stirring a pot"),
 "zawod_nauczyciel": ("Nauczyciel", "a teacher pointing at a board"),
 "zawod_listonosz":  ("Listonosz", "a postal worker with a bag of letters"),
 "zawod_budowlaniec":("Budowlaniec", "a builder in a hard hat with a trowel"),
 "zawod_ogrodnik":   ("Ogrodnik", "a gardener with a watering can"),
 "zawod_kierowca":   ("Kierowca", "a bus driver at a steering wheel"),

 # ——— ślady, żetony, znaczniki na podłogę ——————————————————————
 "slad_stopa_lewa":  ("Lewa stopa", "outline of a bare left foot seen from above"),
 "slad_stopa_prawa": ("Prawa stopa", "outline of a bare right foot seen from above"),
 "slad_lapka":       ("Łapka", "an animal paw print, one pad with four toe pads"),
 "zeton_diament":    ("Diament", "a simple cut diamond gem seen from the front"),

 # ——— zwierzęta leśne ——————————————————————————————————————————
 "zwierze_zajac":      ("Zając", "a friendly hare sitting upright, long ears"),
 "zwierze_lis":        ("Lis", "a friendly fox standing, bushy tail"),
 "zwierze_niedzwiedz": ("Niedźwiedź", "a friendly brown bear on all fours"),
 "zwierze_zaba":       ("Żaba", "a friendly green frog sitting"),

 # ——— uroczystości —————————————————————————————————————————————
 "swieto_wystep": ("Występ", "three children singing on a small stage under bunting"),

 # ——— przedmioty dyżurów i szatni ——————————————————————————————
 "przedmiot_kapcie":   ("Kapcie", "a pair of small soft indoor slippers"),
 "przedmiot_kubek":    ("Kubek", "a single child's mug with a handle"),
 "przedmiot_worek":    ("Worek", "a drawstring cloth bag for gym kit"),
 "przedmiot_serwetka": ("Serwetki", "a small stack of folded paper napkins"),

 # ——— zasady placu zabaw ——————————————————————————————————————————
 "plac_schodki":     ("Wchodzę po schodkach", "a child climbing the steps of a slide, holding the rail"),
 "plac_zjezdzalnia": ("Zjeżdżam nogami w dół", "a child sitting upright on a slide, feet pointing down the slope"),

 # ——— pytania —————————————————————————————————————————————————————
 "pytanie_kto":      ("Kto?", "a question mark next to the silhouette of a person's head"),
 "pytanie_co":       ("Co się stało?", "a question mark next to a spilled cup"),
 "pytanie_gdzie":    ("Gdzie?", "a question mark next to a map location pin"),
 "pytanie_kiedy":    ("Kiedy?", "a question mark next to a clock face"),
 "pytanie_dlaczego": ("Dlaczego?", "a large question mark with a thinking child beside it"),

 # ——— pogoda i pory roku (kalendarz pogody, wyprawy sezonowe) ————————
 "pogoda_slonce":    ("Słonecznie", "a bright smiling sun in a clear sky"),
 "pogoda_chmury":    ("Pochmurno", "two soft grey clouds, no rain"),
 "pogoda_deszcz":    ("Deszcz", "a cloud with blue raindrops falling"),
 "pogoda_snieg":     ("Śnieg", "a cloud with white snowflakes falling"),
 "pogoda_wiatr":     ("Wiatr", "a bending tree with curved wind lines"),
 "pogoda_burza":     ("Burza", "a dark cloud with a yellow lightning bolt"),
 "pora_wiosna":      ("Wiosna", "a tree with fresh green leaves and small blossoms"),
 "pora_lato":        ("Lato", "a tree in full green leaf under a bright sun"),
 "pora_jesien":      ("Jesień", "a tree with orange leaves, some falling"),
 "pora_zima":        ("Zima", "a bare tree with snow on its branches"),

 # ——— instytucje w okolicy —————————————————————————————————————————
 "miejsce_przedszkole": ("Przedszkole", "a friendly low building with a playground slide beside it"),
 "miejsce_przychodnia": ("Przychodnia", "a building with a medical cross sign above the door"),
 "miejsce_poczta":      ("Poczta", "a building with a post box and an envelope sign"),
 "miejsce_straz":       ("Straż pożarna", "a fire station building with a red fire engine in front"),
 "miejsce_biblioteka":  ("Biblioteka", "a building with a large open book sign above the door"),
 "miejsce_sklep":       ("Sklep", "a small shop building with an awning and a shopping basket"),

 # ——— zawody (kącik zawodów, spotkania z rodzicami) ————————————————
 "zawod_lekarz":     ("Lekarz", "a doctor in a white coat with a stethoscope"),
 "zawod_budowlaniec":("Budowlaniec", "a builder in a yellow hard hat holding a trowel"),
 "zawod_nauczyciel": ("Nauczyciel", "a teacher standing beside a board, holding a book"),
 "zawod_strazak":    ("Strażak", "a firefighter in a helmet holding a hose"),
 "zawod_ogrodnik":   ("Ogrodnik", "a gardener with a watering can beside a potted plant"),

 # ——— urządzenia cyfrowe (obszar cyfrowy) —————————————————————————
 "cyfrowe_telefon":  ("Telefon", "a simple mobile phone with a blank screen"),
 "cyfrowe_aparat":   ("Aparat", "a compact photo camera with a lens"),
 "cyfrowe_tablet":   ("Tablet", "a tablet with a blank screen lying flat"),
 "cyfrowe_radio":    ("Radio", "a small portable radio with a speaker grille and antenna"),

 # ——— segregacja odpadów ———————————————————————————————————————————
 "odpad_papier":     ("Papier", "a blue bin with folded newspaper and cardboard beside it"),
 "odpad_plastik":    ("Plastik", "a yellow bin with a plastic bottle beside it"),
 "odpad_szklo":      ("Szkło", "a green bin with a glass jar beside it"),
 "odpad_bio":        ("Bio", "a brown bin with an apple core and leaves beside it"),

 # ——— instrumenty (orkiestra przedszkolna) ————————————————————————
 "instrument_beben": ("Bębenek", "a small hand drum with two wooden beaters"),
 "instrument_grzechotka": ("Grzechotka", "a wooden maraca shaker"),
 "instrument_dzwonki":("Dzwonki", "a set of small hand bells on a wooden handle"),
 "instrument_trojkat":("Trójkąt", "a metal triangle with its striker"),

 # ——— zakupy i sklepik ——————————————————————————————————————————————
 "zakupy_chleb":     ("Chleb", "a loaf of bread"),
 "zakupy_mleko":     ("Mleko", "a carton of milk"),
 "zakupy_jablko":    ("Jabłko", "a red apple with a green leaf"),
 "zakupy_marchewka": ("Marchewka", "an orange carrot with green top"),
 "zakupy_ser":       ("Ser", "a wedge of yellow cheese"),
 "zakupy_woda":      ("Woda", "a bottle of water"),

 # ——— etapy budowy domu ————————————————————————————————————————————
 "budowa_fundament": ("Fundamenty", "a rectangular concrete foundation dug into the ground"),
 "budowa_mury":      ("Mury", "brick walls of a house being built, no roof yet"),
 "budowa_dach":      ("Dach", "a house with its roof beams and tiles going on"),
 "budowa_gotowy":    ("Gotowy dom", "a finished small house with windows, door and roof"),

 # ——— narzędzia w warsztacie ————————————————————————————————————————
 "narzedzie_mlotek": ("Młotek", "a small hammer"),
 "narzedzie_srubokret":("Śrubokręt", "a screwdriver"),
 "narzedzie_nozyczki":("Nożyczki", "a pair of child safety scissors"),
 "narzedzie_klej":   ("Klej", "a glue stick with its cap off"),

 # ——— komunikacja i droga ——————————————————————————————————————————
 "droga_przejscie":  ("Przejście dla pieszych", "a zebra crossing on a road, seen from the side"),
 "droga_sygnalizacja":("Sygnalizacja", "a pedestrian traffic light showing red and green"),
 "droga_przystanek": ("Przystanek", "a bus stop sign with a small shelter"),
 "droga_autobus":    ("Autobus", "a city bus seen from the side"),

 # ——— przyroda: łańcuch zależności i środowiska ————————————————————
 "przyroda_roslina": ("Roślina", "a green plant with leaves growing from soil"),
 "przyroda_owad":    ("Owad", "a ladybird on a leaf"),
 "przyroda_ptak":    ("Ptak", "a small brown bird perched on a branch"),
 "przyroda_ryba":    ("Ryba", "a fish swimming, seen from the side"),
 "srodowisko_las":   ("Las", "a group of green trees with a forest floor"),
 "srodowisko_pustynia":("Pustynia", "sand dunes with a cactus under a hot sun"),
 "srodowisko_lod":   ("Kraina lodu", "an ice floe with snow under a pale sky"),

 # ——— postawa i czynności ———————————————————————————————————————————
 "postawa_stolik":   ("Prosto przy stoliku",
                      "a child sitting correctly at a table: feet flat on the floor, "
                      "straight back, both hands on the table top, seen from the side"),
 "umiem_ukladam":    ("Układam", "a child completing a jigsaw puzzle at a table"),
 "umiem_spiewam":    ("Śpiewam", "a child singing with an open mouth and music notes"),
 "umiem_biegam":     ("Biegam", "a child running happily"),
 "umiem_pomagam":    ("Pomagam", "a child handing a toy to another child"),
}


def podpis(kod):
    return SYMBOLE[kod][0]


def opis(kod):
    return SYMBOLE[kod][1]


def jest(kod):
    """Czy symbol jest już narysowany i skadrowany."""
    return (KATALOG / f"k_{kod}.jpg").exists()


def brakujace():
    return [k for k in SYMBOLE if not jest(k)]
