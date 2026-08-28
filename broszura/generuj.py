# -*- coding: utf-8 -*-
"""
Generator broszury "Kolorowy Świat Emocji".

Uruchom:  python3 broszura/generuj.py
Powstaną: broszura/kolorowy-swiat-emocji.html   (pełny plik do druku i PDF)
          broszura/artefakt.html                (wersja do publikacji online)
"""
import base64
import os
import sys
import html

BAZA = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BAZA)
import tresc  # noqa: E402
try:
    from fonty import CSS_FONTY
except ImportError:  # brak osadzonych krojów — uruchom pobierz_fonty.py
    CSS_FONTY = ""

# ── dane wydawcy (marka PCTP) ────────────────────────────────────────────────
FIRMA = {
    "skrot": "PCTP",
    "nazwa": "Pomorskie Centrum Terapii Pedagogicznej",
    "miasto": "Koszalin",
    "autorka": "mgr Mirosława Ewa Jurczyszyn",
    "ekosystem": "EduPlaner2026-MJ-PCTP",
}

LOGO = (
    '<svg class="logo" viewBox="0 0 24 24" role="img" aria-label="PCTP">'
    '<rect width="24" height="24" fill="#2D1B69"/>'
    '<rect x="5" y="6" width="14" height="2.6" fill="#FFFFFF"/>'
    '<rect x="5" y="10.7" width="10" height="2.6" fill="#FFFFFF"/>'
    '<rect x="5" y="15.4" width="6" height="2.6" fill="#FFFFFF"/>'
    '<circle cx="17.4" cy="16.7" r="2.4" fill="#E8450A"/>'
    "</svg>"
)


def stopka_marki(nr=None):
    numer = f'<span class="st-nr">{nr}</span>' if nr is not None else ""
    return (
        '<footer class="page-stopka">'
        f'{LOGO}<span class="st-nazwa"><b>{e(FIRMA["skrot"])}</b> '
        f'{e(FIRMA["nazwa"])} · {e(FIRMA["miasto"])}</span>'
        f'<span class="st-kropki"></span>{numer}</footer>'
    )


# ── licznik stron ────────────────────────────────────────────────────────────
_stan = {"nr": 0}
_numery = {}          # id strony → numer, potrzebne do spisu treści


def _numer():
    _stan["nr"] += 1
    return _stan["nr"]


def e(t):
    return html.escape(str(t), quote=False)


def odmien(r, forma):
    """Dopasowuje zaimek do rodzaju nazwy emocji: mój smutek, ale moja radość."""
    formy = {
        "moj":   ("Mój", "Moja"),
        "swoj":  ("swój", "swoją"),
        "jego":  ("go", "jej"),
    }
    meski, zenski = formy[forma]
    return meski if r["rodzaj"] == "m" else zenski


# ── elementy powtarzalne ─────────────────────────────────────────────────────

APARAT = (
    '<svg class="ph-ikona" viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M4 7h3.2l1.4-2h6.8l1.4 2H20a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V8a1 1 0 0 1 1-1z"/>'
    '<circle cx="12" cy="13" r="3.6"/></svg>'
)


GOTOWE = os.path.join(BAZA, "zdjecia-gotowe")
_pamiec = {}


def wczytaj(plik):
    """Zwraca zdjęcie jako data URI albo None, jeśli pliku jeszcze nie ma."""
    if plik in _pamiec:
        return _pamiec[plik]
    sciezka = os.path.join(GOTOWE, plik + ".jpg")
    wynik = None
    if os.path.exists(sciezka):
        with open(sciezka, "rb") as f:
            wynik = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("ascii")
    _pamiec[plik] = wynik
    return wynik


def zdjecie(opis, wysokosc="52mm", etykieta="MIEJSCE NA ZDJĘCIE", plik=None):
    dane = wczytaj(plik) if plik else None
    if dane:
        return (
            f'<figure class="photo photo-ma" style="--ph-h:{wysokosc}">'
            f'<img src="{dane}" alt="{e(opis)}" loading="lazy"></figure>'
        )
    return (
        f'<figure class="photo" style="--ph-h:{wysokosc}">'
        f'{APARAT}<span class="ph-etykieta">{e(etykieta)}</span>'
        f'<figcaption class="ph-opis">{e(opis)}</figcaption></figure>'
    )


def linie(ile=3, etykieta=None):
    lab = f'<span class="lines-lab">{e(etykieta)}</span>' if etykieta else ""
    return f'<div class="lines" style="--n:{ile}">{lab}</div>'


def ramka_rysunek(podpis, wysokosc="70mm"):
    return (
        f'<div class="draw" style="--dr-h:{wysokosc}">'
        f'<span class="draw-lab">{e(podpis)}</span></div>'
    )


def karta(tytul, srodek, klasa=""):
    """Karta w stylu próbnika farb: kolorowa zakładka nad polem treści."""
    return (
        f'<section class="chipcard {klasa}">'
        f'<h3 class="chipcard-tab">{e(tytul)}</h3>'
        f'<div class="chipcard-body">{srodek}</div></section>'
    )


def lista(pozycje, klasa="tick"):
    li = "".join(f"<li>{e(p)}</li>" for p in pozycje)
    return f'<ul class="{klasa}">{li}</ul>'


def strona(zawartosc, r=None, klasa="", naglowek=True, pid=None):
    nr = _numer()
    if pid:
        _numery[pid] = nr
    if r:
        styl = (f'style="--c:{r["hex"]};--ink:{r["ink"]};--txt:{r["txt"]};'
                f'--tint:{r["tint"]};--tint2:{r["tint2"]}"')
        eyebrow = f'{r["nr"]} · {r["kolor"].upper()} — {r["emocja"].upper()}'
    else:
        styl = ""
        eyebrow = "KOLOROWY ŚWIAT EMOCJI"
    head = (
        f'<header class="page-head"><span class="ph-ch">{e(eyebrow)}</span></header>'
    ) if naglowek else ""
    return (f'<article class="page {klasa}" {styl}>{head}'
            f'<div class="page-body">{zawartosc}</div>{stopka_marki(nr)}</article>')


# ── STRONY WSTĘPNE ───────────────────────────────────────────────────────────

def okladka():
    chipy = "".join(
        f'<span class="cover-chip" style="background:{r["hex"]};color:{r["txt"]}">'
        f'<b>{e(r["emocja"])}</b><i>{e(r["kolor"])}</i></span>'
        for r in tresc.ROZDZIALY
    )
    return (
        '<article class="page cover">'
        '<div class="cover-top">'
        '<span class="cover-eyebrow">Zeszyt terapeutyczny dla nastolatka</span>'
        f'<h1 class="cover-title">{e(tresc.TYTUL)}</h1>'
        f'<p class="cover-sub">{e(tresc.OPIS_OKLADKA)}</p>'
        '</div>'
        f'<div class="cover-chips">{chipy}</div>'
        + zdjecie(
            "Zdjęcie na okładkę: pięć plam farby albo pięć kolorowych próbników "
            "ułożonych obok siebie na jasnym tle. Kolory zgodne z paskiem powyżej. "
            "Bez twarzy — kolor jest bohaterem okładki.",
            "78mm", "ZDJĘCIE OKŁADKOWE", plik="okladka")
        + '<div class="cover-foot">'
        '<span>Rozpoznawanie emocji · Ćwiczenia · Opowiadania</span>'
        '<span class="cover-imie">Ten zeszyt należy do: <i class="dot"></i></span>'
        '</div></article>'
    )


def strona_tytulowa():
    tresc_ = (
        '<span class="eyebrow">O tym zeszycie</span>'
        f'<h2 class="h-big">{e(tresc.TYTUL)}</h2>'
        f'<p class="lead">{e(tresc.PODTYTUL)}. Pięć emocji, pięć kolorów, '
        'ta sama droga za każdym razem.</p>'
        + karta("Dla kogo", lista([
            "Dla nastolatka w spektrum autyzmu.",
            "Dla każdego, komu trudno nazwać to, co czuje.",
            "Do pracy samodzielnej, z rodzicem albo z terapeutą.",
        ]))
        + karta("Co znajdziesz w środku", lista([
            "Pięć rozdziałów — każdy o jednej emocji i jej kolorze.",
            "Opis emocji prostymi zdaniami.",
            "Mapę ciała: po czym poznasz emocję u siebie i u innych.",
            "Opowiadanie o Rajmundzie i pytania do niego.",
            "Zadania na trzech poziomach trudności.",
            "Własną stronę na rysunek, notatkę i zdjęcie.",
        ]))
        + '<div class="two">'
        + karta("Ile to zajmuje", '<p class="p">Jeden rozdział to osiem stron. '
                'Możesz przejść je w jeden dzień albo rozłożyć na tydzień. '
                'Nie ma limitu czasu. Nie ma ocen.</p>')
        + karta("Czego tu nie ma", '<p class="p">Nie ma dobrych i złych odpowiedzi. '
                'Nie ma emocji zakazanych. Nie ma sprawdzianu na końcu.</p>')
        + '</div>'
        + zdjecie("Zdjęcie: zeszyt otwarty na kolorowej stronie, obok kredki albo pisaki "
                  "w pięciu kolorach broszury. Ujęcie z góry, jasne tło.", "48mm",
                  plik="wstep-tytulowa")
    )
    return strona(tresc_, pid="wstep-tytulowa")


def jak_korzystac_ty():
    kroki = "".join(
        f'<li class="krok"><span class="krok-nr">{i}</span>'
        f'<div><b>{e(t)}</b><p class="p">{e(o)}</p></div></li>'
        for i, (t, o) in enumerate([
            ("Wybierz kolor", "Otwórz rozdział, który pasuje do dzisiaj. "
                              "Nie musisz iść po kolei."),
            ("Przeczytaj opis", "Zdania są krótkie. Możesz czytać po jednym."),
            ("Sprawdź ciało", "Zobacz mapę ciała. Poszukaj tych znaków u siebie."),
            ("Przeczytaj opowiadanie", "Rajmund przeżywa to samo, co Ty."),
            ("Odpowiedz na pytania", "Pisz krótko. Jedno zdanie wystarczy."),
            ("Zrób jedno zadanie", "Jedno. Nie wszystkie. Wybierz swój poziom."),
            ("Wypełnij swoją stronę", "To jedyna strona, która będzie tylko Twoja."),
        ], start=1)
    )
    tresc_ = (
        '<span class="eyebrow">Instrukcja</span>'
        '<h2 class="h-big">Jak korzystać z zeszytu</h2>'
        '<p class="lead">Siedem kroków. Zawsze takich samych, w każdym rozdziale.</p>'
        f'<ol class="kroki">{kroki}</ol>'
        + karta("Zasady", lista([
            "Możesz przerwać w dowolnym momencie.",
            "Możesz wrócić do tej samej strony wiele razy.",
            "Możesz nie odpowiadać na pytanie, które jest za trudne.",
            "Możesz poprosić o pomoc. To nie jest oszukiwanie.",
        ], "tick"), "wide")
        + zdjecie("Zdjęcie: dłonie nastolatka piszącego w zeszycie, ołówek, "
                  "kolorowe zakładki. Bez twarzy, ciepłe światło.", "40mm",
                  plik="wstep-korzystac")
    )
    return strona(tresc_, pid="wstep-korzystac")


def jak_korzystac_doroslego():
    tresc_ = (
        '<span class="eyebrow">Dla rodzica, nauczyciela i terapeuty</span>'
        '<h2 class="h-big">Jak towarzyszyć</h2>'
        '<p class="lead">Ten zeszyt działa najlepiej wtedy, gdy dorosły jest obok, '
        'ale nie ocenia.</p>'
        '<div class="two">'
        + karta("Rób", lista([
            "Czytaj razem na głos, jeśli o to poprosi.",
            "Zostaw czas na ciszę po pytaniu.",
            "Przyjmij każdą odpowiedź bez poprawiania.",
            "Zapowiadaj z góry, ile dzisiaj zrobicie.",
            "Wracaj do rozdziału, który był trudny.",
        ]))
        + karta("Unikaj", lista([
            "Poprawiania nazwy emocji („to nie złość, tylko…”).",
            "Zmuszania do wypełnienia całej strony.",
            "Porównywania z rówieśnikami.",
            "Zaskakiwania zmianą planu.",
            "Traktowania zeszytu jak sprawdzianu.",
        ], "cross"))
        + '</div>'
        + karta("Kiedy szukać wsparcia specjalisty", lista([
            "Gdy jedna emocja utrzymuje się przez wiele tygodni.",
            "Gdy nastolatek unika większości sytuacji społecznych.",
            "Gdy pojawia się samookaleczanie albo myśli o śmierci.",
            "Gdy lęk uniemożliwia chodzenie do szkoły.",
        ]), "wide")
        + karta("Trzy pytania na dobry początek",
                '<p class="p">Zadaj je przed pierwszym rozdziałem. Zapisz odpowiedzi.</p>'
                + linie(1, "1. Który kolor lubisz najbardziej i dlaczego?")
                + linie(1, "2. Po czym poznam, że masz dzisiaj gorszy dzień?")
                + linie(1, "3. Co Ci pomaga, gdy jest za dużo bodźców?"), "wide")
        + '<p class="mini">Ten zeszyt jest materiałem edukacyjnym i pomocą w pracy '
          'nad rozpoznawaniem emocji. Nie zastępuje diagnozy ani terapii.</p>'
    )
    return strona(tresc_, pid="wstep-doroslego")


def spis_tresci():
    def nr(pid):
        return _numery.get(pid, "")

    wstep = [
        ("O tym zeszycie", "wstep-tytulowa"),
        ("Jak korzystać z zeszytu", "wstep-korzystac"),
        ("Jak towarzyszyć — dla dorosłego", "wstep-doroslego"),
        ("Poznaj Rajmunda", "wstep-poznaj"),
        ("Pięć kolorów", "wstep-mapa"),
        ("Słowniczek trudnych słów", "wstep-slowniczek"),
    ]
    koniec = [
        ("Moja paleta emocji", "kon-paleta"),
        ("Gra „Ścieżka Kolorów” — zasady", "gra-zasady"),
        ("Gra — plansza", "gra-plansza"),
        ("Gra — karty do wycięcia", "gra-karty1"),
        ("Mój plan na trudny dzień", "kon-plan"),
        ("Gdy jest bardzo trudno", "kon-pomoc"),
        ("Dyplom", "kon-dyplom"),
        ("O wydawcy", "kon-wydawca"),
    ]

    def wiersze(pozycje):
        return "".join(
            f'<li class="sp-w"><span class="sp-t">{e(t)}</span>'
            '<span class="sp-kropki"></span>'
            f'<span class="sp-nr">{nr(pid)}</span></li>'
            for t, pid in pozycje
        )

    rozdzialy = ""
    for r in tresc.ROZDZIALY:
        rozdzialy += (
            f'<li class="sp-w sp-roz" style="--c:{r["hex"]};--ink:{r["ink"]}">'
            '<span class="sp-chip"></span>'
            f'<span class="sp-t"><b>{e(r["nr"])} · {e(r["emocja"])}</b>'
            f'<i>kolor {e(r["kolor"].lower())} · opowiadanie na str. '
            f'{nr("r" + r["nr"] + "-opowiadanie")}</i></span>'
            '<span class="sp-kropki"></span>'
            f'<span class="sp-nr">{nr("r" + r["nr"] + "-otwarcie")}</span></li>'
        )

    tresc_ = (
        '<span class="eyebrow">Spis treści</span>'
        '<h2 class="h-big">Co jest w środku</h2>'
        '<p class="lead">Nie musisz iść po kolei — otwórz ten kolor, '
        'który pasuje do dzisiaj.</p>'
        '<div class="sp-grupa"><h3 class="sp-naglowek">Zanim zaczniesz</h3>'
        f'<ol class="spis">{wiersze(wstep)}</ol></div>'
        '<div class="sp-grupa"><h3 class="sp-naglowek">Pięć kolorów emocji</h3>'
        f'<ol class="spis">{rozdzialy}</ol></div>'
        '<div class="sp-grupa"><h3 class="sp-naglowek">Na koniec</h3>'
        f'<ol class="spis">{wiersze(koniec)}</ol></div>'
    )
    return strona(tresc_, klasa="strona-spis")


def poznaj_bohaterow():
    karty = "".join(
        f'<div class="osoba"><div class="osoba-awatar">{e(imie[0])}</div>'
        f'<div><b>{e(imie)}</b><span class="osoba-meta">{e(wiek)}</span>'
        f'<p class="p">{e(o)}</p></div></div>'
        for imie, wiek, o in tresc.POSTACIE
    )
    tresc_ = (
        '<span class="eyebrow">Bohaterowie</span>'
        '<h2 class="h-big">Poznaj Rajmunda</h2>'
        '<p class="lead">Rajmund ma siedemnaście lat. Emocje widzi jako kolory. '
        'W każdym rozdziale przeżywa jedną z nich — tak jak Ty.</p>'
        + zdjecie("Zdjęcie: nastolatek przy biurku pełnym modeli i map, w ciepłym świetle. "
                  "Ujęcie z boku, spokojne. Może być też sama scenografia, bez osoby.", "48mm",
                  plik="wstep-poznaj")
        + f'<div class="osoby">{karty}</div>'
        + karta("A Ty?",
                linie(1, "Mam na imię:")
                + linie(1, "Najbardziej lubię:")
                + linie(1, "Po czym poznasz, że jest mi dobrze:"), "wide")
    )
    return strona(tresc_, pid="wstep-poznaj")


def mapa_kolorow():
    wiersze = "".join(
        f'<div class="mapa-w" style="--c:{r["hex"]};--tint:{r["tint"]};--ink:{r["ink"]}">'
        f'<span class="mapa-chip">{e(r["nr"])}</span>'
        f'<div class="mapa-txt"><b>{e(r["emocja"])}</b>'
        f'<span class="mapa-kolor">{e(r["kolor"])}</span>'
        f'<p class="p">{e(r["haslo"])}</p></div>'
        f'<span class="mapa-str">str. '
        f'{_numery.get("r" + r["nr"] + "-otwarcie", "")}</span></div>'
        for r in tresc.ROZDZIALY
    )
    tresc_ = (
        '<span class="eyebrow">Spis treści</span>'
        '<h2 class="h-big">Pięć kolorów</h2>'
        '<p class="lead">Każdy kolor to jedna emocja. Każdy rozdział ma osiem stron '
        'i zawsze ten sam porządek.</p>'
        f'<div class="mapa">{wiersze}</div>'
        + karta("Ten sam porządek w każdym rozdziale", lista([
            "1. Kolor — otwarcie rozdziału",
            "2. Co to za emocja",
            "3. Jak wygląda w ciele",
            "4. Kiedy to czuję",
            "5. Opowiadanie o Rajmundzie",
            "6. Pytania do opowiadania",
            "7. Zadania dla Ciebie",
            "8. Moja strona",
        ], "plain"), "wide")
    )
    return strona(tresc_, pid="wstep-mapa")


def slowniczek():
    poz = "".join(
        f'<div class="slowo"><b>{e(s)}</b><p class="p">{e(d)}</p></div>'
        for s, d in tresc.SLOWNICZEK
    )
    tresc_ = (
        '<span class="eyebrow">Trudne słowa</span>'
        '<h2 class="h-big">Słowniczek</h2>'
        '<p class="lead">Osiem słów, które pojawią się w tym zeszycie. '
        'Możesz tu wracać zawsze, gdy któreś umknie.</p>'
        f'<div class="slowa">{poz}</div>'
        + karta("Twoje trudne słowo",
                '<p class="p">Znalazłeś w zeszycie słowo, którego nie rozumiesz? '
                'Zapisz je tutaj i zapytaj kogoś dorosłego, co znaczy.</p>' + linie(2), "wide")
        + zdjecie("Zdjęcie: otwarty słownik albo notes z zakreślonymi słowami, "
                  "ujęcie z góry, spokojne światło.", "28mm", plik="wstep-slowniczek")
    )
    return strona(tresc_, pid="wstep-slowniczek")


# ── STRONY ROZDZIAŁU ─────────────────────────────────────────────────────────

def r_otwarcie(r):
    nr = _numer()
    _numery["r" + r["nr"] + "-otwarcie"] = nr
    return (
        f'<article class="page rozdzial-otw" '
        f'style="--c:{r["hex"]};--ink:{r["ink"]};--txt:{r["txt"]};'
        f'--tint:{r["tint"]};--tint2:{r["tint2"]}">'
        '<div class="rot-plama">'
        f'<span class="rot-nr">{e(r["nr"])}</span>'
        f'<h2 class="rot-emocja">{e(r["emocja"])}</h2>'
        f'<span class="rot-kolor">kolor {e(r["kolor"].lower())}</span>'
        '</div>'
        '<div class="rot-dol">'
        f'<p class="rot-haslo">{e(r["haslo"])}</p>'
        f'<p class="rot-lead">{e(r["otwarcie"])}</p>'
        + zdjecie(r["zdjecia"]["otwarcie"], "58mm", plik=f'{r["nr"]}-otwarcie')
        + '<div class="rot-stopka">'
        f'<span class="rot-hex">{e(r["hex"])}</span>'
        '</div>' + stopka_marki(nr) + '</div></article>'
    )


def r_co_to(r):
    z = "".join(
        f'<li><span class="zd-nr">{i}</span>{e(t)}</li>'
        for i, t in enumerate(r["co_to"], start=1)
    )
    tresc_ = (
        f'<span class="eyebrow">Krok 2 — poznaj emocję</span>'
        f'<h2 class="h-big">Co to jest {e(r["emocja"].lower())}?</h2>'
        f'<ol class="zdania">{z}</ol>'
        f'<blockquote class="mysl">{e(r["mysl"])}</blockquote>'
        '<div class="two">'
        + zdjecie(r["zdjecia"]["co_to"], "46mm", plik=f'{r["nr"]}-co_to')
        + karta("Ciekawostka", f'<p class="p">{e(r["ciekawostka"])}</p>')
        + '</div>'
        + karta("Sprawdź siebie", 
                '<p class="p">Dokończ zdanie własnymi słowami:</p>'
                f'<p class="p"><b>Dla mnie {e(r["emocja"].lower())} to…</b></p>' + linie(2), "wide")
    )
    return strona(tresc_, r)


def r_cialo(r):
    kol = (
        karta("Twarz", lista(r["twarz"]))
        + karta("Ciało", lista(r["cialo"]))
        + karta("W środku", lista(r["srodku"]))
    )
    tresc_ = (
        '<span class="eyebrow">Krok 3 — mapa ciała</span>'
        f'<h2 class="h-big">Jak wygląda {e(r["emocja"].lower())}</h2>'
        '<p class="lead">Emocję widać. U siebie i u innych. '
        'Oto trzy miejsca, w których jej szukać.</p>'
        f'<div class="trzy">{kol}</div>'
        + zdjecie(r["zdjecia"]["cialo"], "48mm", "MIEJSCE NA 3 ZDJĘCIA",
                  plik=f'{r["nr"]}-cialo')
        + karta("Zaznacz to, co znasz u siebie",
                '<p class="p">Wróć do trzech kart powyżej. Podkreśl ołówkiem każdy znak, '
                'który zauważyłeś kiedyś u siebie. Ile ich wyszło?</p>'
                + linie(1, "Liczba podkreślonych znaków:"), "wide")
    )
    return strona(tresc_, r)


def r_kiedy(r):
    poz = "".join(
        f'<li class="kiedy-p"><span class="kiedy-box"></span>{e(t)}</li>'
        for t in r["kiedy"]
    )
    tresc_ = (
        '<span class="eyebrow">Krok 4 — moje sytuacje</span>'
        f'<h2 class="h-big">Kiedy czuję {e(r["emocja"].lower())}</h2>'
        '<p class="lead">Zaznacz kwadracik przy każdej sytuacji, która zdarza się Tobie.</p>'
        f'<ul class="kiedy">{poz}</ul>'
        + zdjecie(r["zdjecia"]["kiedy"], "42mm", "MIEJSCE NA 4 MAŁE ZDJĘCIA",
                  plik=f'{r["nr"]}-kiedy')
        + karta("Dopisz swoje",
                '<p class="p">Twoje sytuacje, których nie ma na liście:</p>' + linie(3), "wide")
    )
    return strona(tresc_, r)


def r_opowiadanie(r):
    akapity = "".join(f'<p class="op-p">{e(a)}</p>' for a in r["opowiadanie"])
    waga = sum(len(a) for a in r["opowiadanie"]) + 90 * len(r["opowiadanie"])
    dlugie = waga > 1900
    sredni = 1500 < waga <= 1900
    wys = "33mm" if (dlugie or sredni) else "44mm"
    gesto = " op-gesty" if dlugie else ""
    tresc_ = (
        '<span class="eyebrow">Krok 5 — opowiadanie</span>'
        f'<h2 class="h-big">{e(r["opowiadanie_tytul"])}</h2>'
        + zdjecie(r["zdjecia"]["opowiadanie"], wys, "MIEJSCE NA 2 ZDJĘCIA",
                  plik=f'{r["nr"]}-opowiadanie')
        + f'<div class="opowiadanie{gesto}">{akapity}</div>'
        + ("" if dlugie else karta(
            "Zanim przewrócisz stronę",
            '<p class="p">Zaznacz ołówkiem zdanie, które najbardziej Cię poruszyło. '
            'Potem zapisz, dlaczego właśnie to.</p>' + linie(1 if sredni else 2), "wide"))
    )
    return strona(tresc_, r, "strona-opow", pid=f'r{r["nr"]}-opowiadanie')


def r_pytania(r):
    poz = "".join(
        f'<li class="pyt"><span class="pyt-nr">{i}</span>'
        f'<div class="pyt-tresc"><p class="pyt-t">{e(p)}</p>{linie(2)}</div></li>'
        for i, p in enumerate(r["pytania"], start=1)
    )
    tresc_ = (
        '<span class="eyebrow">Krok 6 — pytania do pracy</span>'
        '<h2 class="h-big">Pomyśl i zapisz</h2>'
        '<p class="lead">Odpowiadaj krótko. Jedno zdanie wystarczy. '
        'Nie ma złych odpowiedzi.</p>'
        f'<ol class="pytania">{poz}</ol>'
    )
    return strona(tresc_, r, "strona-pytania")


def r_zadania(r):
    def blok(tytul, opis, poz, poziom):
        li = "".join(f'<li>{e(p)}</li>' for p in poz)
        kropki = "".join(
            f'<i class="kropka {"on" if i <= poziom else ""}"></i>' for i in range(1, 4)
        )
        return (
            f'<section class="zad"><header class="zad-head">'
            f'<span class="zad-poziom">{kropki}</span>'
            f'<b>{e(tytul)}</b><span class="zad-opis">{e(opis)}</span></header>'
            f'<ul class="tick">{li}</ul></section>'
        )

    tresc_ = (
        '<span class="eyebrow">Krok 7 — zadania</span>'
        '<h2 class="h-big">Zadania dla Ciebie</h2>'
        '<p class="lead">Wybierz jedno. Nie musisz robić wszystkich. '
        'Poziom wybierasz sam.</p>'
        + blok("Na rozgrzewkę", "5 minut", r["zadania_latwe"], 1)
        + blok("Na spokojnie", "20 minut", r["zadania_srednie"], 2)
        + blok("Śmiały krok", "dłużej niż jeden dzień", r["zadania_smiale"], 3)
        + '<div class="two">'
        + karta("Wybieram zadanie numer", linie(1) + '<p class="p">Zrobię je do:</p>' + linie(1))
        + zdjecie(f'Zdjęcie do rozdziału: przedmiot albo scena w kolorze '
                  f'{r["kolor"].lower()[:-1]}ym, związana z jednym z zadań powyżej.',
                  "44mm", plik=f'{r["nr"]}-zadania')
        + '</div>'
        + karta("Zrobiłem dzisiaj", linie(2), "wide")
    )
    return strona(tresc_, r, "strona-zadania")


def r_moja_strona(r):
    skala = "".join(
        f'<span class="term-p" style="--o:{0.2 * i:.2f}"><i>{i}</i></span>'
        for i in range(1, 6)
    )
    poz = "".join(f'<li>{e(p)}</li>' for p in r["pomaga"])
    tresc_ = (
        '<span class="eyebrow">Krok 8 — tylko Twoja strona</span>'
        f'<h2 class="h-big">{odmien(r, "moj")} {e(r["emocja"].lower())}</h2>'
        + karta(f'Ile {odmien(r, "jego")} dzisiaj było?',
                '<p class="p">Zakreśl liczbę. 1 — prawie wcale. 5 — bardzo dużo.</p>'
                f'<div class="term">{skala}</div>', "wide")
        + '<div class="two">'
        + karta(r["pomaga_tytul"], f'<ol class="numer">{poz}</ol>')
        + karta("Co pomaga mnie", '<p class="p">Wpisz swoje sposoby:</p>' + linie(4))
        + '</div>'
        + '<div class="two">'
        + ramka_rysunek(
            f'Narysuj tutaj {odmien(r, "swoj")} {r["emocja"].lower()}', "58mm")
        + zdjecie(r["zdjecia"]["moja_strona"], "58mm", "WKLEJ SWOJE ZDJĘCIE")
        + '</div>'
    )
    return strona(tresc_, r, "strona-moja")


# ── GRA: ŚCIEŻKA KOLORÓW ─────────────────────────────────────────────────────

def gra_zasady():
    potrzebne = "".join(f"<li>{e(x)}</li>" for x in tresc.GRA_POTRZEBNE)
    kroki = "".join(
        f'<li class="krok"><span class="krok-nr">{i}</span>'
        f'<div><b>{e(t)}</b><p class="p">{e(o)}</p></div></li>'
        for i, (t, o) in enumerate(tresc.GRA_ZASADY, start=1)
    )
    tresc_ = (
        '<span class="eyebrow">Gra</span>'
        f'<h2 class="h-big">{e(tresc.GRA_TYTUL)}</h2>'
        f'<p class="lead">{e(tresc.GRA_PODTYTUL)}. Przejdźcie razem przez pięć kolorów '
        'i porozmawiajcie o tym, co każdy z nich znaczy u Was.</p>'
        + karta("Co jest potrzebne", f'<ul class="tick">{potrzebne}</ul>', "wide")
        + f'<ol class="kroki">{kroki}</ol>'
        + '<blockquote class="mysl mysl-grzbiet">'
        f'{e(tresc.GRA_ZASADA_STOP)}</blockquote>'
    )
    return strona(tresc_, klasa="strona-gra", pid="gra-zasady")


def gra_plansza():
    """Plansza: 30 pól ułożonych wężem, sześć pól z gwiazdką."""
    # gwiazdki rozłożone tak, by wypadły na każdym z pięciu kolorów
    Z_GWIAZDKA = {6, 10, 12, 18, 21, 24}
    kolory = [(r["hex"], r["ink"], r["txt"], r["emocja"]) for r in tresc.ROZDZIALY]
    pola = []
    for nr in range(1, 31):
        hexc, ink, txt, emocja = kolory[(nr - 1) % 5]
        gwiazdka = nr in Z_GWIAZDKA
        etykieta = "START" if nr == 1 else ("META" if nr == 30 else str(nr))
        klasa = "pole" + (" pole-krancowe" if nr in (1, 30) else "")
        pola.append(
            f'<div class="{klasa}" style="--c:{hexc};--txt:{txt}" '
            f'aria-label="pole {nr}, {emocja}">'
            f'<span class="pole-nr">{etykieta}</span>'
            + ('<span class="pole-gwiazdka">\u2605</span>' if gwiazdka else "")
            + "</div>"
        )
    # wąż: co drugi rząd odwrócony
    rzedy = []
    for i in range(0, 30, 6):
        wiersz = pola[i:i + 6]
        if (i // 6) % 2 == 1:
            wiersz = list(reversed(wiersz))
        rzedy.append('<div class="plansza-rzad">' + "".join(wiersz) + "</div>")

    legenda = "".join(
        f'<span class="leg-poz"><i style="background:{r["hex"]}"></i>{e(r["emocja"])}</span>'
        for r in tresc.ROZDZIALY
    )
    tresc_ = (
        '<span class="eyebrow">Gra — plansza</span>'
        f'<h2 class="h-big">{e(tresc.GRA_TYTUL)}</h2>'
        '<p class="lead">Idźcie po numerach. Na każdym polu powiedzcie jedno zdanie '
        'o emocji w tym kolorze.</p>'
        f'<div class="plansza">{"".join(rzedy)}</div>'
        f'<div class="legenda">{legenda}'
        '<span class="leg-poz"><i class="leg-gwiazdka">\u2605</i>weź kartę</span></div>'
        + '<div class="two">'
        + karta("Wersja łatwiejsza",
                '<p class="p">Zamiast opowiadać, wystarczy nazwać kolor i emocję. '
                'Karty odkładacie na bok.</p>')
        + karta("Wersja trudniejsza",
                '<p class="p">Na każdym polu dodajcie, po czym inni poznaliby po Was '
                'tę emocję — co robi twarz, ciało, głos.</p>')
        + '</div>'
    )
    return strona(tresc_, klasa="strona-plansza", pid="gra-plansza")


def gra_karty(od, do, numer_arkusza):
    karty = "".join(
        f'<div class="karta"><span class="karta-typ">{e(rodzaj)}</span>'
        f'<p class="karta-tresc">{e(tekst)}</p>'
        f'<span class="karta-stopka">{e(tresc.GRA_TYTUL)}</span></div>'
        for rodzaj, tekst in tresc.GRA_KARTY[od:do]
    )
    tresc_ = (
        f'<span class="eyebrow">Gra — karty {numer_arkusza} z 2</span>'
        '<h2 class="h-big">Karty do wycięcia</h2>'
        '<p class="lead">Wytnij wzdłuż linii. Potasuj i połóż obok planszy '
        'napisem do dołu.</p>'
        f'<div class="karty">{karty}</div>'
    )
    return strona(tresc_, klasa="strona-karty",
                  pid=f"gra-karty{numer_arkusza}")


# ── STRONY KOŃCOWE ───────────────────────────────────────────────────────────

def paleta_koncowa():
    wiersze = "".join(
        f'<div class="pal-w" style="--c:{r["hex"]};--tint:{r["tint"]};--ink:{r["ink"]}">'
        f'<span class="pal-chip"></span>'
        f'<div class="pal-txt"><b>{e(r["emocja"])}</b>'
        f'<span class="pal-lab">Mój znak, po którym ją poznaję:</span>'
        f'{linie(1)}</div></div>'
        for r in tresc.ROZDZIALY
    )
    tresc_ = (
        '<span class="eyebrow">Podsumowanie</span>'
        '<h2 class="h-big">Moja paleta emocji</h2>'
        '<p class="lead">Przeszedłeś pięć kolorów. Zbierz je teraz w jednym miejscu. '
        'Przy każdej emocji wpisz jeden znak, po którym poznajesz ją u siebie.</p>'
        f'<div class="paleta">{wiersze}</div>'
        + karta("Który kolor był najtrudniejszy?", linie(2), "wide")
    )
    return strona(tresc_, pid="kon-paleta")


def plan_trudny_dzien():
    kroki = "".join(
        f'<li class="krok"><span class="krok-nr">{i}</span>'
        f'<div><b>{e(t)}</b><p class="p">{e(o)}</p></div></li>'
        for i, (t, o) in enumerate([
            ("Zatrzymaj się", "Przerwij to, co robisz. Usiądź, jeśli możesz."),
            ("Nazwij kolor", "Który to kolor? Żółty, niebieski, czerwony, różowy czy szary?"),
            ("Oddychaj", "Wdech na 4. Wydech na 6. Sześć razy."),
            ("Zrób jedną rzecz z listy", "Twoje sposoby są zapisane na stronach „Moja strona”."),
            ("Powiedz komuś", "Jedno zdanie wystarczy: „Mam dzisiaj ______ dzień”."),
        ], start=1)
    )
    tresc_ = (
        '<span class="eyebrow">Do wyrwania i powieszenia</span>'
        '<h2 class="h-big">Mój plan na trudny dzień</h2>'
        '<p class="lead">Pięć kroków. Zawsze w tej samej kolejności. '
        'Powieś tę stronę tam, gdzie ją zobaczysz.</p>'
        f'<ol class="kroki">{kroki}</ol>'
        + karta("Trzy osoby, do których mogę się odezwać",
                '<div class="osoby-3">'
                f'<div><span class="os-lab">Imię</span>{linie(1)}<span class="os-lab">Telefon</span>{linie(1)}</div>'
                f'<div><span class="os-lab">Imię</span>{linie(1)}<span class="os-lab">Telefon</span>{linie(1)}</div>'
                f'<div><span class="os-lab">Imię</span>{linie(1)}<span class="os-lab">Telefon</span>{linie(1)}</div>'
                '</div>', "wide")
        + '<div class="two">'
        + karta("Mój sygnał, że potrzebuję przerwy",
                '<p class="p">Umów go z bliskimi. Może to być słowo, gest albo kartka.</p>'
                + linie(2))
        + karta("Moje miejsce na ochłonięcie",
                '<p class="p">Gdzie idę, gdy muszę wyjść z sytuacji?</p>' + linie(2))
        + '</div>'
    )
    return strona(tresc_, pid="kon-plan")


def gdy_bardzo_trudno():
    tresc_ = (
        '<span class="eyebrow">Ważne</span>'
        '<h2 class="h-big">Gdy jest bardzo trudno</h2>'
        '<p class="lead">Czasem emocja jest za duża, żeby poradzić sobie samemu. '
        'Wtedy prosi się o pomoc. To nie jest słabość. To jest właściwy krok.</p>'
        + karta("Powiedz dorosłemu, gdy…", lista([
            "smutek trwa dłużej niż dwa tygodnie,",
            "boisz się iść do szkoły,",
            "myślisz o zrobieniu sobie krzywdy,",
            "nie chce Ci się już nic, co wcześniej lubiłeś.",
        ]), "wide")
        + karta("Moje kontakty na trudny czas",
                '<p class="p">Wpisz je teraz, kiedy jest spokojnie. '
                'W trudnej chwili nie będzie czasu szukać.</p>'
                '<div class="kontakty">'
                f'<div><span class="os-lab">Osoba dorosła, której ufam</span>{linie(1)}'
                f'<span class="os-lab">Telefon</span>{linie(1)}</div>'
                f'<div><span class="os-lab">Pedagog albo psycholog szkolny</span>{linie(1)}'
                f'<span class="os-lab">Telefon</span>{linie(1)}</div>'
                f'<div><span class="os-lab">Mój terapeuta</span>{linie(1)}'
                f'<span class="os-lab">Telefon</span>{linie(1)}</div>'
                f'<div><span class="os-lab">Telefon zaufania w moim kraju</span>{linie(1)}'
                f'<span class="os-lab">Numer</span>{linie(1)}</div>'
                '</div>', "wide")
        + karta("Zdanie, którym mogę poprosić o pomoc",
                '<p class="p">Ułóż je teraz, na spokojnie. Wtedy łatwiej będzie je powiedzieć '
                'w trudnej chwili. Na przykład: „Potrzebuję pomocy. Nie daję rady sam”.</p>'
                + linie(2), "wide")
    )
    return strona(tresc_, pid="kon-pomoc")


def _dyplom_nr():
    nr = _numer()
    _numery["kon-dyplom"] = nr
    return nr


def dyplom():
    return (
        '<article class="page dyplom">'
        '<div class="dyp-ramka">'
        '<div class="dyp-pasek">'
        + "".join(f'<span style="background:{r["hex"]}"></span>' for r in tresc.ROZDZIALY)
        + '</div>'
        '<div class="dyp-srodek">'
        '<span class="dyp-eyebrow">Dyplom ukończenia</span>'
        '<h2 class="dyp-h">Kolorowy Świat Emocji</h2>'
        '<p class="dyp-p">Ten dyplom otrzymuje</p>'
        '<div class="dyp-pole"><div class="dyp-linia"></div>'
        '<span class="dyp-lab">imię i nazwisko</span></div>'
        '<p class="dyp-p dyp-za">za przejście przez pięć kolorów emocji, '
        'za odwagę w nazywaniu tego, co czuje, i za wytrwałość.</p>'
        '<div class="dyp-podpisy">'
        '<div class="dyp-pole"><div class="dyp-linia mini-l"></div>'
        '<span class="dyp-lab">data</span></div>'
        '<div class="dyp-pole"><div class="dyp-linia mini-l"></div>'
        '<span class="dyp-lab">podpis</span></div>'
        '</div></div></div>'
        + stopka_marki(_dyplom_nr()) + '</article>'
    )


def stopka_wydawcy():
    tresc_ = (
        '<span class="eyebrow">Na koniec</span>'
        '<h2 class="h-big">Kolory zostają</h2>'
        '<p class="lead">Zeszyt się skończył, ale emocje przychodzą dalej. '
        'Teraz masz dla nich nazwy i kolory. To wystarczy, żeby zacząć.</p>'
        + karta("Co dalej", lista([
            "Wróć do rozdziału, który był najtrudniejszy.",
            "Powieś „Plan na trudny dzień” w widocznym miejscu.",
            "Raz w tygodniu zaznacz na palecie, który kolor był największy.",
            "Pokaż komuś zaufanemu swoją stronę z rysunkiem.",
        ]), "wide")
        + zdjecie("Zdjęcie zamykające: pięć kolorowych plam farby zlewających się w tęczę "
                  "albo paleta malarska z pięcioma kolorami broszury.", "30mm",
                  plik="koniec")
        + '<div class="wydawca">'
        + LOGO
        + f'<div class="wyd-txt"><b>{e(FIRMA["skrot"])}</b>'
        f'<span>{e(FIRMA["nazwa"])}</span>'
        f'<span>{e(FIRMA["miasto"])}</span></div></div>'
        + '<div class="kolofon">'
        '<div class="kol-poz"><span class="kol-lab">Tytuł</span>'
        '<b>Kolorowy Świat Emocji — zeszyt ćwiczeń dla nastolatka</b></div>'
        + f'<div class="kol-poz"><span class="kol-lab">Autorka</span>'
        f'<b>{e(FIRMA["autorka"])}</b></div>'
        f'<div class="kol-poz"><span class="kol-lab">Wydawca</span>'
        f'<b>{e(FIRMA["nazwa"])}, {e(FIRMA["miasto"])}</b></div>'
        f'<div class="kol-poz"><span class="kol-lab">Seria</span>'
        f'<b>{e(FIRMA["ekosystem"])}</b></div>'
        + '<div class="kol-poz"><span class="kol-lab">Kontakt</span>'
        '<b class="uzup">[ e-mail · telefon · strona www ]</b></div>'
        '<div class="kol-poz"><span class="kol-lab">Adres</span>'
        '<b class="uzup">[ ulica, kod pocztowy ]</b></div>'
        '<div class="kol-poz"><span class="kol-lab">Wydanie</span>'
        '<b class="uzup">[ pierwsze · rok ]</b></div>'
        '<div class="kol-poz"><span class="kol-lab">ISBN</span>'
        '<b class="uzup">[ numer, jeśli będzie ]</b></div>'
        '</div>'
        '<p class="mini">Wszelkie prawa zastrzeżone. Kopiowanie i rozpowszechnianie '
        'całości lub fragmentów bez zgody wydawcy jest zabronione. '
        'Zakup uprawnia do wydruku egzemplarza dla jednego ucznia.</p>'
        '<p class="mini">Materiał edukacyjny i pomocniczy. '
        'Nie zastępuje diagnozy ani terapii prowadzonej przez specjalistę.</p>'
    )
    return strona(tresc_, pid="kon-wydawca")


# ── CSS ──────────────────────────────────────────────────────────────────────

CSS = """
:root{
  --papier:#FFFFFF;
  --biurko:#EFE9DE;
  --atrament:#241F2E;
  --atrament-2:#5A5368;
  --atrament-3:#8B8399;
  --wlos:#E5E0EA;
  --linia:#BDB4CC;
  --grzbiet:#2D1B69;
  --grzbiet-jasny:#EFEBF8;
  --akcent:#E8450A;
  --c:#2D1B69; --ink:#241553; --txt:#FFFFFF; --tint:#EFEBF8; --tint2:#D3C9EC;
  --font-h:"Nunito","Trebuchet MS",sans-serif;
  --font-t:"Atkinson Hyperlegible","Verdana",sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:var(--biurko);color:var(--atrament);
  font-family:var(--font-t);font-size:11.4pt;line-height:1.68;
  -webkit-font-smoothing:antialiased}
p{margin:0}

/* ── strona ─────────────────────────────────────────── */
.page{position:relative;width:210mm;height:297mm;background:var(--papier);
  margin:0 auto 8mm;padding:13mm 16mm 9mm;overflow:hidden;
  display:flex;flex-direction:column;
  box-shadow:0 2px 24px rgba(36,31,46,.16)}
.page-body{flex:1;display:flex;flex-direction:column;gap:4.4mm;min-height:0}
.page-head{display:flex;justify-content:space-between;align-items:baseline;
  padding-bottom:2.5mm;margin-bottom:4.6mm;border-bottom:1.5px solid var(--tint2)}
.ph-ch{font-family:var(--font-h);font-weight:800;font-size:8.4pt;
  letter-spacing:.13em;color:var(--ink)}
.ph-nr{font-family:var(--font-h);font-weight:900;font-size:12pt;color:var(--c)}

/* ── stopka z marką ─────────────────────────────────── */
.page-stopka{display:flex;align-items:center;gap:2.6mm;margin-top:3.4mm;
  padding-top:2mm;border-top:.8px solid var(--wlos);
  font-size:7.8pt;letter-spacing:.03em;color:var(--atrament-3)}
.logo{width:4.8mm;height:4.8mm;flex:0 0 auto;display:block}
.st-nazwa{flex:1;min-width:0}
.page-stopka{align-items:center}
.st-nazwa b{font-family:var(--font-h);font-weight:900;color:var(--grzbiet);
  letter-spacing:.06em;margin-right:1.5mm}
.st-kropki{flex:0 0 auto;width:8mm}
.st-nr{font-family:var(--font-h);font-weight:900;font-size:12pt;
  color:var(--grzbiet);font-variant-numeric:tabular-nums;
  min-width:8mm;text-align:right}
.rozdzial-otw .st-nr{color:var(--ink)}
.rozdzial-otw .page-stopka{margin-top:3mm;border-top-color:var(--tint2)}
.dyplom .page-stopka{position:absolute;left:15mm;right:15mm;bottom:5mm;
  margin:0;border:0}
.dyp-nr{display:none}

/* ── spis treści ────────────────────────────────────── */
.sp-grupa{display:flex;flex-direction:column;gap:1.4mm}
.sp-naglowek{font-family:var(--font-h);font-weight:800;font-size:9pt;
  letter-spacing:.15em;text-transform:uppercase;color:var(--grzbiet);
  margin:0;padding-bottom:1.4mm;border-bottom:2px solid var(--grzbiet-jasny)}
.spis{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.sp-w{display:flex;align-items:baseline;gap:2.5mm;padding:1mm 0;
  border-bottom:.6px solid var(--wlos)}
.sp-w:last-child{border-bottom:0}
.sp-t{font-size:10.4pt;line-height:1.3}
.sp-kropki{flex:1;border-bottom:1px dotted var(--atrament-3);
  transform:translateY(-1mm);min-width:6mm}
.sp-nr{font-family:var(--font-h);font-weight:900;font-size:11pt;
  color:var(--grzbiet);font-variant-numeric:tabular-nums;min-width:7mm;
  text-align:right}
.sp-roz{align-items:center;padding:1.5mm 0}
.sp-chip{width:5mm;height:5mm;background:var(--c);flex:0 0 auto;
  box-shadow:inset 0 0 0 .8px rgba(0,0,0,.12)}
.sp-roz .sp-t{display:flex;flex-direction:column;gap:.4mm}
.sp-roz .sp-t b{font-family:var(--font-h);font-weight:900;font-size:12.4pt;
  color:var(--ink)}
.sp-roz .sp-t i{font-style:normal;font-size:8.8pt;color:var(--atrament-3)}
.sp-roz .sp-nr{color:var(--ink)}
.strona-spis .page-body{gap:2.6mm}
.strona-spis .lead{font-size:11.4pt}

/* ── blok wydawcy ───────────────────────────────────── */
.wydawca{display:flex;align-items:center;gap:4mm}
.wydawca .logo{width:14mm;height:14mm}
.wyd-txt{display:flex;flex-direction:column;line-height:1.35}
.wyd-txt b{font-family:var(--font-h);font-weight:900;font-size:15pt;
  color:var(--grzbiet);letter-spacing:.08em}
.wyd-txt span{font-size:9.6pt;color:var(--atrament-2)}

/* ── typografia ─────────────────────────────────────── */
.eyebrow{font-family:var(--font-h);font-weight:800;font-size:8.6pt;
  letter-spacing:.15em;text-transform:uppercase;color:var(--c)}
.h-big{font-family:var(--font-h);font-weight:900;font-size:25pt;line-height:1.1;
  margin:1mm 0 0;color:var(--atrament);text-wrap:balance;letter-spacing:-.01em}
.lead{font-size:12.2pt;line-height:1.6;color:var(--atrament-2);max-width:150mm}
.p{font-size:11pt;line-height:1.62}
.mini{font-size:9.2pt;line-height:1.55;color:var(--atrament-3)}

/* ── karta w stylu próbnika farb ────────────────────── */
.chipcard{display:flex;flex-direction:column;align-items:flex-start;flex:0 0 auto;min-width:0}
.chipcard-body{flex:1}
.two>*,.trzy>*{min-width:0}
.chipcard-tab{font-family:var(--font-h);font-weight:800;font-size:9.6pt;
  letter-spacing:.06em;text-transform:uppercase;color:#fff;background:var(--ink);
  margin:0;padding:1.6mm 5mm 1.4mm}
.chipcard-body{width:100%;background:var(--tint);
  border:.6px solid color-mix(in srgb,var(--ink) 45%,transparent);
  box-shadow:inset 0 0 0 1.2px #fff,inset 0 0 0 1.9px var(--tint2);
  padding:4.4mm 5.4mm;display:flex;flex-direction:column;gap:2.5mm}
.two{display:grid;grid-template-columns:1fr 1fr;gap:5mm;align-items:stretch}
.trzy{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;align-items:stretch}
.wide{width:100%}

/* ── listy ──────────────────────────────────────────── */
ul.tick,ul.cross,ul.plain{list-style:none;margin:0;padding:0;
  display:flex;flex-direction:column;gap:1.8mm}
ul.tick li,ul.cross li{position:relative;padding-left:7mm;font-size:10.8pt;line-height:1.55}
ul.tick li::before{content:"";position:absolute;left:0;top:2.2mm;width:3.4mm;height:1.9mm;
  border-left:2px solid var(--ink);border-bottom:2px solid var(--ink);
  transform:rotate(-45deg)}
ul.cross li::before{content:"×";position:absolute;left:.6mm;top:-.2mm;
  font-family:var(--font-h);font-weight:900;font-size:13pt;color:var(--ink)}
ul.plain li{font-size:10.8pt}
ol.numer{margin:0;padding-left:6mm;display:flex;flex-direction:column;gap:1.8mm;
  font-size:10.8pt;line-height:1.55}
ol.numer::marker{font-weight:700}

.zdania{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2.6mm}
.zdania li{display:flex;gap:4mm;align-items:baseline;font-size:12.6pt;line-height:1.5}
.zd-nr{flex:0 0 8mm;height:8mm;display:grid;place-items:center;background:var(--tint);
  border:1.5px solid var(--c);color:var(--ink);font-family:var(--font-h);
  font-weight:900;font-size:10pt;align-self:flex-start}

.mysl{margin:0;padding:4mm 6mm;background:var(--ink);color:#fff;
  box-shadow:inset 0 0 0 1px rgba(255,255,255,.28),inset 0 0 0 2.4px var(--ink);
  font-family:var(--font-h);font-weight:800;font-size:13pt;line-height:1.42;
  text-wrap:balance}

/* ── kroki ──────────────────────────────────────────── */
.kroki{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:3mm}
.krok{display:flex;gap:4.5mm;align-items:flex-start}
.krok-nr{flex:0 0 9mm;height:9mm;display:grid;place-items:center;
  background:var(--ink);color:#fff;font-family:var(--font-h);font-weight:900;font-size:11pt}
.krok b{font-family:var(--font-h);font-weight:800;font-size:12pt;display:block}

/* ── zdjęcia ────────────────────────────────────────── */
.photo{position:relative;margin:0;min-height:var(--ph-h,50mm);width:100%;
  background:var(--tint);border:2px dashed var(--c);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:1.6mm;padding:4mm 6mm;text-align:center;flex:0 0 auto;min-width:0}
.photo-ma{border:0;padding:0;background:none;overflow:hidden;
  height:var(--ph-h,50mm);display:block}
.photo-ma img{width:100%;height:100%;object-fit:cover;display:block}
.ph-ikona{width:9mm;height:9mm;fill:none;stroke:var(--c);stroke-width:1.5;
  stroke-linejoin:round;opacity:.85}
.ph-etykieta{font-family:var(--font-h);font-weight:900;font-size:8.4pt;
  letter-spacing:.16em;color:var(--ink)}
.ph-opis{font-size:9.4pt;line-height:1.5;color:var(--atrament-2);max-width:110mm}

/* ── linie do pisania ───────────────────────────────── */
.lines{width:100%}
.lines-lab{display:block;font-size:9.4pt;color:var(--atrament-2);margin-bottom:1mm}
.lines::after{content:"";display:block;width:100%;height:calc(var(--n,3) * 8mm);
  background-image:repeating-linear-gradient(to bottom,
    transparent 0,transparent 7.3mm,var(--linia) 7.3mm,var(--linia) 7.6mm)}
.draw{border:2px solid var(--tint2);background:
  radial-gradient(circle at 1px 1px,var(--tint2) 1px,transparent 0) 0 0/5mm 5mm;
  min-height:var(--dr-h,60mm);position:relative;flex:0 0 auto;min-width:0}
.draw-lab{position:absolute;left:0;top:0;background:var(--ink);color:#fff;
  font-family:var(--font-h);font-weight:800;font-size:8.6pt;letter-spacing:.08em;
  padding:1.4mm 4mm;text-transform:uppercase}

/* ── strona: kiedy czuję ────────────────────────────── */
.kiedy{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:2.4mm}
.kiedy-p{display:flex;gap:4mm;align-items:flex-start;font-size:11.6pt;line-height:1.5}
.kiedy-box{flex:0 0 6mm;height:6mm;border:2px solid var(--c);background:#fff;margin-top:.6mm}

/* ── pytania ────────────────────────────────────────── */
.pytania{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:3.4mm}
.pyt{display:flex;gap:4mm;align-items:flex-start}
.pyt-nr{flex:0 0 7.5mm;height:7.5mm;display:grid;place-items:center;background:var(--tint);
  border:1.5px solid var(--c);color:var(--ink);font-family:var(--font-h);
  font-weight:900;font-size:9.6pt}
.pyt-tresc{flex:1;min-width:0}
.pyt-t{font-size:11pt;line-height:1.45;font-weight:700;margin-bottom:1mm}
.strona-pytania .lines::after{height:calc(var(--n,2) * 7.4mm);
  background-image:repeating-linear-gradient(to bottom,
    transparent 0,transparent 6.8mm,var(--linia) 6.8mm,var(--linia) 7.1mm)}

/* ── zadania ────────────────────────────────────────── */
.zad{border-top:2.5px solid var(--c);padding-top:2.6mm;
  display:flex;flex-direction:column;gap:2.2mm}
.zad-head{display:flex;align-items:baseline;gap:3mm;flex-wrap:wrap}
.zad-head b{font-family:var(--font-h);font-weight:900;font-size:13pt}
.zad-opis{font-size:9.4pt;color:var(--atrament-3);letter-spacing:.04em}
.zad-poziom{display:inline-flex;gap:1.2mm;align-items:center}
.kropka{width:2.8mm;height:2.8mm;border:1.5px solid var(--c);border-radius:50%;display:block}
.kropka.on{background:var(--c)}

/* ── termometr ──────────────────────────────────────── */
.term{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm}
.term-p{height:15mm;display:grid;place-items:center;border:1.5px solid var(--c);
  background:color-mix(in srgb,var(--c) calc(var(--o) * 100%),#fff)}
.term-p i{font-style:normal;font-family:var(--font-h);font-weight:900;font-size:14pt;
  color:var(--ink);mix-blend-mode:multiply}

/* ── otwarcie rozdziału ─────────────────────────────── */
.rozdzial-otw{padding:0;display:flex;flex-direction:column}
.rot-plama{background:var(--c);color:var(--txt);padding:22mm 16mm 16mm;
  display:flex;flex-direction:column;gap:1mm}
.rot-nr{font-family:var(--font-h);font-weight:900;font-size:13pt;letter-spacing:.2em;
  opacity:.8}
.rot-emocja{font-family:var(--font-h);font-weight:900;font-size:58pt;line-height:.95;
  margin:1mm 0 0;letter-spacing:-.02em}
.rot-kolor{font-family:var(--font-h);font-weight:700;font-size:14pt;opacity:.9}
.rot-dol{flex:1;padding:9mm 16mm 11mm;display:flex;flex-direction:column;gap:5mm;
  min-height:0}
.rot-stopka{display:flex;justify-content:flex-end;align-items:baseline;
  border-top:1.5px solid var(--tint2);padding-top:3mm;margin-top:auto}
.rot-dol .photo,.rot-dol .photo-ma{flex:1 1 auto;height:auto;min-height:58mm}
.rot-haslo{font-family:var(--font-h);font-weight:900;font-size:19pt;line-height:1.25;
  color:var(--ink);text-wrap:balance}
.rot-lead{font-size:12.4pt;line-height:1.6;color:var(--atrament-2)}
.rot-hex{font-family:var(--font-h);font-weight:800;font-size:9pt;
  letter-spacing:.14em;color:var(--atrament-3)}

/* ── okładka ────────────────────────────────────────── */
.cover{background:var(--grzbiet);color:#fff;padding:18mm 16mm 14mm;
  display:flex;flex-direction:column;gap:7mm}
.cover-eyebrow{font-family:var(--font-h);font-weight:800;font-size:10pt;
  letter-spacing:.2em;text-transform:uppercase;color:#C9B6F2}
.cover-title{font-family:var(--font-h);font-weight:900;font-size:52pt;line-height:.98;
  margin:3mm 0 0;letter-spacing:-.02em;text-wrap:balance}
.cover-sub{font-size:15pt;line-height:1.45;color:#DCD0F7;margin-top:4mm;max-width:130mm}
.cover-chips{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm}
.cover-chip{padding:5mm 3mm 4mm;display:flex;flex-direction:column;gap:.5mm;
  text-align:center}
.cover-chip b{font-family:var(--font-h);font-weight:900;font-size:12pt}
.cover-chip i{font-style:normal;font-size:8.6pt;letter-spacing:.08em;opacity:.72}
.cover .photo{border-color:#7B5FBE;background:#41287A}
.cover .photo,.cover .photo-ma{flex:1 1 auto;height:auto;min-height:78mm}
.cover-foot{margin-top:auto}
.cover .ph-ikona{stroke:#C9B6F2}
.cover .ph-etykieta{color:#C9B6F2}
.cover .ph-opis{color:#CFC1EE}
.cover-foot{display:flex;justify-content:space-between;align-items:flex-end;
  gap:6mm;border-top:1.5px solid #6B4FB0;padding-top:4mm;font-size:10pt;color:#DCD0F7}
.cover-imie{display:flex;align-items:baseline;gap:3mm;white-space:nowrap}
.cover-imie .dot{display:block;width:48mm;border-bottom:1.5px dotted #A18BDE}

/* ── mapa kolorów ───────────────────────────────────── */
.mapa{display:flex;flex-direction:column;gap:3mm}
.mapa-w{display:flex;align-items:center;gap:5mm;background:var(--tint);
  border-left:6mm solid var(--c);padding:3.5mm 5mm}
.mapa-chip{font-family:var(--font-h);font-weight:900;font-size:15pt;color:var(--ink)}
.mapa-txt{flex:1;min-width:0}
.mapa-txt b{font-family:var(--font-h);font-weight:900;font-size:14pt;margin-right:3mm}
.mapa-kolor{font-size:9.6pt;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
.mapa-str{font-family:var(--font-h);font-weight:800;font-size:9.6pt;color:var(--atrament-3);
  white-space:nowrap}

/* ── bohaterowie, słowniczek ────────────────────────── */
.osoby{display:flex;flex-direction:column;gap:3.5mm}
.osoba{display:flex;gap:4.5mm;align-items:flex-start;border-bottom:1.5px solid var(--wlos);
  padding-bottom:3.5mm}
.osoba:last-child{border-bottom:0}
.osoba-awatar{flex:0 0 12mm;height:12mm;display:grid;place-items:center;
  background:var(--grzbiet-jasny);border:1.5px solid var(--grzbiet);
  font-family:var(--font-h);font-weight:900;font-size:16pt;color:var(--grzbiet)}
.osoba b{font-family:var(--font-h);font-weight:900;font-size:12.6pt;margin-right:3mm}
.osoba-meta{font-size:9.4pt;color:var(--atrament-3);letter-spacing:.06em}
.slowa{display:grid;grid-template-columns:1fr 1fr;gap:4mm 6mm}
.slowo b{font-family:var(--font-h);font-weight:900;font-size:12.4pt;color:var(--grzbiet);
  display:block;margin-bottom:.8mm}

/* ── opowiadanie ────────────────────────────────────── */
.opowiadanie{display:flex;flex-direction:column;gap:2.6mm}
.op-p{font-size:12pt;line-height:1.68;max-width:158mm}
.op-gesty .op-p{font-size:11.2pt;line-height:1.58}
.op-gesty{gap:2.1mm}
.op-p:first-child::first-letter{font-family:var(--font-h);font-weight:900;
  font-size:30pt;line-height:.86;float:left;margin:1mm 2.5mm 0 0;color:var(--c)}

/* ── paleta końcowa, plan, pomoc ────────────────────── */
.paleta{display:flex;flex-direction:column;gap:3mm}
.pal-w{display:flex;gap:5mm;align-items:flex-start;background:var(--tint);padding:3.5mm 5mm}
.pal-chip{flex:0 0 12mm;height:12mm;background:var(--c)}
.pal-txt{flex:1;min-width:0}
.pal-txt b{font-family:var(--font-h);font-weight:900;font-size:13pt;color:var(--ink)}
.pal-lab{display:block;font-size:9.4pt;color:var(--atrament-2);margin:.4mm 0 .8mm}
.osoby-3{display:grid;grid-template-columns:repeat(3,1fr);gap:5mm}
.os-lab{display:block;font-size:9pt;letter-spacing:.08em;text-transform:uppercase;
  color:var(--atrament-3);margin-top:1.5mm}
.kontakty{display:grid;grid-template-columns:1fr 1fr;gap:2mm 8mm}

/* ── gra: plansza i karty ───────────────────────────── */
.mysl-grzbiet{background:var(--grzbiet)}
.plansza{display:flex;flex-direction:column;gap:2.5mm}
.plansza-rzad{display:grid;grid-template-columns:repeat(6,1fr);gap:2.5mm}
.pole{position:relative;aspect-ratio:1;background:var(--c);color:var(--txt);
  display:grid;place-items:center}
.pole-nr{font-family:var(--font-h);font-weight:900;font-size:15pt}
.pole-krancowe .pole-nr{font-size:9.5pt;letter-spacing:.08em}
.pole-gwiazdka{position:absolute;right:1.6mm;bottom:1mm;font-size:9pt;opacity:.9}
.legenda{display:flex;flex-wrap:wrap;gap:2.5mm 6mm;align-items:center;
  border-top:1.5px solid var(--wlos);padding-top:3mm}
.leg-poz{display:inline-flex;align-items:center;gap:2mm;font-size:10pt}
.leg-poz i{width:5mm;height:5mm;display:block;font-style:normal}
.leg-gwiazdka{display:grid!important;place-items:center;background:var(--atrament);
  color:#fff;font-size:7pt}
.karty{display:grid;grid-template-columns:repeat(3,1fr);gap:0}
.karta{border:1.2px dashed var(--atrament-3);padding:5mm 4.5mm;min-height:44mm;
  display:flex;flex-direction:column;gap:2.5mm;margin:-0.6px 0 0 -0.6px}
.karta-typ{font-family:var(--font-h);font-weight:900;font-size:8pt;
  letter-spacing:.16em;text-transform:uppercase;color:var(--grzbiet)}
.karta-tresc{font-size:10.6pt;line-height:1.5;flex:1}
.karta-stopka{font-size:7.4pt;letter-spacing:.1em;text-transform:uppercase;
  color:var(--atrament-3)}
.strona-karty .page-body{gap:4mm}

/* ── dyplom ─────────────────────────────────────────── */
.dyplom{padding:15mm;display:flex}
.dyp-ramka{flex:1;border:2.5px solid var(--grzbiet);display:flex;flex-direction:column}
.dyp-pasek{display:grid;grid-template-columns:repeat(5,1fr);height:12mm}
.dyp-pasek span{display:block}
.dyp-srodek{flex:1;padding:20mm 18mm 16mm;display:flex;flex-direction:column;
  align-items:center;text-align:center;gap:6mm}
.dyp-eyebrow{font-family:var(--font-h);font-weight:800;font-size:10pt;letter-spacing:.24em;
  text-transform:uppercase;color:var(--grzbiet)}
.dyp-h{font-family:var(--font-h);font-weight:900;font-size:32pt;line-height:1.05;margin:0;
  color:var(--atrament);text-wrap:balance}
.dyp-p{font-size:12pt;line-height:1.6;color:var(--atrament-2);max-width:118mm}
.dyp-za{margin-top:2mm}
.dyp-pole{display:flex;flex-direction:column;align-items:center;gap:1.5mm}
.dyp-linia{width:120mm;border-bottom:1.5px solid var(--atrament);height:14mm}
.dyp-linia.mini-l{width:52mm;height:11mm}
.dyp-lab{font-size:8.8pt;letter-spacing:.16em;text-transform:uppercase;
  color:var(--atrament-3)}
.dyp-podpisy{display:flex;gap:14mm;margin-top:auto}
.dyp-nr{position:absolute;left:15mm;bottom:9mm}

/* ── kolofon ────────────────────────────────────────── */
.kolofon{display:grid;grid-template-columns:1fr 1fr;gap:2.2mm 6mm;
  border-top:2px solid var(--wlos);border-bottom:2px solid var(--wlos);padding:3mm 0}
.kol-lab{display:block;font-size:8.6pt;letter-spacing:.14em;text-transform:uppercase;
  color:var(--atrament-3)}
.kol-poz b{font-family:var(--font-h);font-weight:800;font-size:11pt}
.uzup{color:var(--grzbiet)}

/* ── druk ───────────────────────────────────────────── */
@media print{
  @page{size:A4 portrait;margin:0}
  body{background:#fff}
  .page{margin:0;box-shadow:none;break-after:page;page-break-after:always}
  .page:last-child{break-after:auto;page-break-after:auto}
  .photo,.draw,.term-p,.chipcard-tab,.mysl,.krok-nr,.cover,.rot-plama,
  .pal-chip,.dyp-chipy span,.cover-chip,.pole,.leg-poz i,.dyp-pasek span,
  .logo,.logo rect,.logo circle,.sp-chip,.chipcard-body{
    -webkit-print-color-adjust:exact;print-color-adjust:exact}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""


# ── składanie dokumentu ──────────────────────────────────────────────────────

def _zloz():
    """Składa wszystkie strony. Wołane dwa razy: pierwszy przebieg zbiera
    numery stron, drugi wstawia je do spisu treści i mapy kolorów."""
    _stan["nr"] = 0
    strony = [
        okladka(),
        strona_tytulowa(),
        spis_tresci(),
        jak_korzystac_ty(),
        jak_korzystac_doroslego(),
        poznaj_bohaterow(),
        mapa_kolorow(),
        slowniczek(),
    ]
    for r in tresc.ROZDZIALY:
        strony += [
            r_otwarcie(r), r_co_to(r), r_cialo(r), r_kiedy(r),
            r_opowiadanie(r), r_pytania(r), r_zadania(r), r_moja_strona(r),
        ]
    strony += [
        paleta_koncowa(),
        gra_zasady(),
        gra_plansza(),
        gra_karty(0, 12, 1),
        gra_karty(12, 24, 2),
        plan_trudny_dzien(),
        gdy_bardzo_trudno(),
        dyplom(),
        stopka_wydawcy(),
    ]

    return strony


def zbuduj():
    _zloz()             # przebieg 1: zbiera numery stron
    strony = _zloz()    # przebieg 2: spis treści i mapa mają już numery

    # kroje pobierane z sieci tylko wtedy, gdy nie ma osadzonych
    zapas = (
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
        'family=Atkinson+Hyperlegible:wght@400;700&'
        'family=Nunito:wght@700;800;900&display=swap">\n'
    ) if not CSS_FONTY else ""

    glowa = (
        f"<title>{e(tresc.TYTUL)}</title>\n"
        f"{zapas}"
        f"<style>{CSS_FONTY}\n{CSS}</style>"
    )
    cialo = "\n".join(strony)

    pelny = (
        '<!doctype html>\n<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<meta name="description" content="Zeszyt terapeutyczny dla nastolatka: '
        'pięć emocji, pięć kolorów, ćwiczenia i opowiadania.">\n'
        f"{glowa}\n</head>\n<body>\n{cialo}\n</body>\n</html>\n"
    )
    artefakt = f"{glowa}\n{cialo}\n"

    with open(os.path.join(BAZA, "kolorowy-swiat-emocji.html"), "w", encoding="utf-8") as f:
        f.write(pelny)
    with open(os.path.join(BAZA, "artefakt.html"), "w", encoding="utf-8") as f:
        f.write(artefakt)

    return _stan["nr"]


if __name__ == "__main__":
    ile = zbuduj()
    print(f"Gotowe. Stron w broszurze: {ile}")
