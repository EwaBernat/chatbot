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
.kd-tab{width:100%;min-width:0;table-layout:fixed;border-collapse:collapse;margin:14px 0 4px;font-size:13px}
.kd-tab th,.kd-tab td{border:1px solid #9BB7CE;padding:9px 8px;text-align:left;vertical-align:top}
.kd-tab th{background:#EAF2F8;font-weight:700;color:#1F4468}
.kd-tab td.pusto{height:34px}
.kd-tab tr td:first-child{font-weight:600;color:#1F4468}
.kd-tab th:first-child{width:26%}
.kd-tab th,.kd-tab td{word-wrap:break-word}
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
