# -*- coding: utf-8 -*-
"""Skład broszury-adaptacji lektury. Wejście: słownik z danymi (JSON), wyjście: HTML.

Podział na strony jest tu decyzją projektową, nie przypadkiem: rozdział zawsze zajmuje
trzy strony w tej samej kolejności, bo przewidywalność układu zdejmuje z ucznia
konieczność uczenia się strony od nowa przy każdym rozdziale.
"""
import html, re
from . import svg as S
from . import obrazy

E = html.escape

C_ZG = "#1F8A63"
TOM_NAZWY = {
    1: ("E1", "Co widzę — a co widzi ktoś inny?"),
    2: ("E2", "Co ktoś czuje?"),
    3: ("E3", "Czego ktoś chce?"),
    4: ("E4", "Co ktoś myśli?"),
    5: ("E5", "Co on myśli, że ja myślę?"),
}
CZESCI = ["Historia i słowa", "Emocje i wnioski", "Ocena i myślenie"]


# ---------------------------------------------------------------- pomocnicze
def fig(svgstr, extra="", cap=""):
    """Figura z ilustracją.

    Proporcje wymusza pudełko `padding-bottom`, a SVG jest w nim pozycjonowany
    absolutnie. Bez tego silnik druku gubi wysokość SVG i rozbija stronę na dwa
    arkusze — to był najbardziej uporczywy błąd składu, więc nie upraszczaj tego
    do `height:auto`.
    """
    m = re.search(r'viewBox="0 0 ([0-9.]+) ([0-9.]+)"', svgstr)
    pb = (float(m.group(2)) / float(m.group(1)) * 100) if m else 75.0
    caphtml = f"<figcaption>{E(cap)}</figcaption>" if cap else ""
    kl = ("ilu " + extra).strip()
    return (f'<figure class="{kl}"><div class="ilu-box" style="padding-bottom:{pb:.3f}%">'
            f'{svgstr}</div>{caphtml}</figure>')


def fig_obraz(klasa, w, h, extra="", cap="", kadr=""):
    """Figura ze zdjęciem. Proporcje bierzemy z nagłówka pliku — patrz obrazy.py."""
    pb = h / w * 100
    caphtml = f"<figcaption>{E(cap)}</figcaption>" if cap else ""
    kl = ("ilu ilu-foto " + extra).strip()
    # Zdjęcie w pionie nie może być kadrowane do wąskiego paska karty — obcięłoby
    # to, co na nim najważniejsze. Oznaczamy je, a arkusz stylów pokazuje je w całości.
    # Zdjęcie znacznie wyższe albo znacznie szersze od paska karty pokazujemy
    # w całości — kadrowanie „na wypełnienie" zjadłoby z niego to, co istotne.
    pion = " foto-pion" if h > w * 1.05 else (" foto-pas" if w > h * 2.6 else "")
    # `kadr` decyduje, która część zdjęcia zostaje widoczna, gdy karta przycina
    # je do wąskiego paska. Bez tego środek kadru ucina to, co najważniejsze —
    # latarnię latarnika, koronę króla, kapelusz próżnego.
    poz = f";background-position:{kadr}" if kadr else ""
    return (f'<figure class="{kl}"><div class="ilu-box foto-tlo{pion} {klasa}" '
            f'style="padding-bottom:{pb:.3f}%{poz}"></div>{caphtml}</figure>')


def rysunek(nazwa):
    """Zamienia nazwę ilustracji na SVG. Przyjmuje też gotowy SVG (zaczyna się od '<svg')."""
    if not nazwa:
        return ""
    if nazwa.lstrip().startswith("<svg"):
        return nazwa
    fn = getattr(S, nazwa, None)
    return fn() if callable(fn) else ""


def skala(poziom):
    kropki = "".join(f'<i class="{"on" if i <= poziom else ""}"></i>' for i in range(1, 6))
    return f'<span class="skala" title="natężenie {poziom} z 5">{kropki}</span>'


def kolor_oceny(txt):
    t = (txt or "").upper()
    if t.startswith("ZIELONE"):
        return "zielone", "✔"
    if t.startswith("CZERWONE"):
        return "czerwone", "✖"
    return "zolte", "!"


# ---------------------------------------------------------------- klasa składu
class Broszura:
    def __init__(self, dane, linie=None, katalog_grafik=None):
        self.d = dane
        self.katalog_grafik = katalog_grafik
        # Ten sam obraz bywa użyty kilka razy (karta planety i ilustracja rozdziału).
        # Trzymamy go w pliku raz, jako klasę CSS, zamiast powtarzać data URI.
        self._obrazy = {}
        self.meta = dane["meta"]
        self.w = dane["wydawca"]
        self.R = dane["rozdzialy"]
        self.linie = linie or {}
        self.tytul_biezacy = f'{self.meta["tytul"]} {self.meta.get("podtytul_okladki","")}'.strip()

    def obraz_klasa(self, plik):
        """Rejestruje obraz i zwraca (nazwa klasy CSS, szerokość, wysokość)."""
        if plik not in self._obrazy:
            uri, w, h = obrazy.osadz(plik, self.katalog_grafik)
            self._obrazy[plik] = (f"foto{len(self._obrazy) + 1}", uri, w, h)
        kl, _, w, h = self._obrazy[plik]
        return kl, w, h

    def style_obrazow(self):
        """Arkusz z wszystkimi obrazami — wywołaj dopiero po złożeniu sekcji."""
        if not self._obrazy:
            return ""
        reguly = "".join(f".{kl}{{background-image:url({uri})}}"
                         for kl, uri, _, _ in self._obrazy.values())
        return f"<style>{reguly}</style>"

    def logo_css(self):
        """Logo z pliku wstawiamy raz, jako tło w CSS.

        Znak wraca w stopce każdej strony — gdyby był osobnym `<img>`, ten sam
        obraz powtórzyłby się w pliku ponad sto razy. Jako tło jest zdefiniowany
        jeden raz i tylko do niego się odwołujemy.
        """
        plik = self.w.get("logo_obraz")
        if not plik:
            return ""
        uri, _, _ = obrazy.osadz(plik, self.katalog_grafik)
        return ("<style>.logo-foto,.f-znak .mark-foto{background-image:url(" + uri + ")}</style>")

    def znak_stopki(self):
        return ('<span class="mark-foto"></span>' if self.w.get("logo_obraz")
                else S.logo_use())

    def logo_duze(self):
        if self.w.get("logo_obraz"):
            return '<div class="logo-foto" role="img" aria-label="Logo ' + E(self.w["organizacja"]) + '"></div>'
        return rysunek(self.w.get("logo_svg", "logo_pctp"))

    def ilustracja(self, zrodlo, extra="", cap=""):
        """Buduje figurę z danych. `obraz` (plik) ma pierwszeństwo przed `ilustracja` (wektor)."""
        waska, szeroka, kadr = False, False, ""
        if isinstance(zrodlo, dict):
            plik, wektor = zrodlo.get("obraz"), zrodlo.get("ilustracja")
            waska = bool(zrodlo.get("ilustracja_waska"))
            szeroka = bool(zrodlo.get("ilustracja_szeroka"))
            kadr = zrodlo.get("kadr", "")
        else:
            plik, wektor = None, zrodlo
        if plik:
            klasa, w, h = self.obraz_klasa(plik)
            if waska:
                extra = (extra + " waska").strip()
            elif szeroka:
                # rysunki z drobnymi podpisami (np. dwie perspektywy) muszą być większe,
                # inaczej uczeń nie odczyta etykiet
                extra = (extra + " szeroka").strip()
            return fig_obraz(klasa, w, h, extra, cap, kadr)
        rys = rysunek(wektor)
        if rys and not waska and isinstance(wektor, str) and wektor.endswith("_scena"):
            # Sceny są szerokie (200×96), więc znoszą większą szerokość niż
            # rysunki kwadratowe — inaczej gubią się na stronie.
            extra = (extra + " scena").strip()
        return fig(rys, extra, cap) if rys else ""

    # ---- stopki ----
    def stopka_ogolna(self):
        return (f'<footer class="r-foot"><span class="f-znak">{self.znak_stopki()}'
                f'<b>{E(self.w.get("skrot","")) }</b> · {E(self.tytul_biezacy)}</span>'
                f'<span class="f-srodek">{E(self.w["organizacja"])}</span>'
                f'<span class="f-nr"></span></footer>')

    def stopka_rozdzialu(self, nr, part):
        return (f'<footer class="r-foot"><span class="f-znak">{self.znak_stopki()}'
                f'<b>{E(self.w.get("skrot",""))}</b> · {E(self.tytul_biezacy)}</span>'
                f'<span class="f-srodek">rozdział {nr}/{len(self.R)} · część {part} z 3</span>'
                f'<span class="f-nr"></span></footer>')

    # ---- okładka ----
    def okladka(self):
        m, w = self.meta, self.w
        if m.get("okladka_obraz"):
            klasa, sz, wy = self.obraz_klasa(m["okladka_obraz"])
            okladka_grafika = (f'<div class="ok-box ok-box-foto foto-tlo {klasa}" '
                               f'style="padding-bottom:{min(wy / sz * 100, 40):.2f}%"></div>')
        else:
            okladka_grafika = ('<div class="ok-box">'
                               + rysunek(m.get("okladka_svg", "cover_neutral")) + "</div>")
        punkty = "".join(f"<li>{E(x)}</li>" for x in m.get("na_okladce", []))
        return f'''
<section class="page okladka" id="okladka">
  <div class="ok-tlo">{okladka_grafika}</div>
  <div class="ok-tresc">
    <div class="ok-logo">{self.logo_duze()}</div>
    <p class="ok-org">{E(w["organizacja"])}</p>
    <p class="ok-nad">{E(m.get("nadtytul","Adaptacja lektury dla młodzieży ze spektrum autyzmu"))}</p>
    <h1>{E(m["tytul"])}<br><span>{E(m.get("podtytul_okladki",""))}</span></h1>
    <p class="ok-pod">{E(m.get("haslo",""))}</p>
    <div class="ok-linia"></div>
    <ul class="ok-lista">{punkty}</ul>
  </div>
  <div class="ok-stopka">
    <p class="ok-autor">opracowanie: <b>{E(w["autorka"])}</b></p>
    <p class="ok-mail">{E(w["mail"])}</p>
    <p class="ok-zrodlo">{E(m.get("zrodlo",""))}</p>
  </div>
</section>'''

    # ---- spis treści ----
    # ---- metryczka wydawcy (zawsze strona 2) ----
    def metryczka_wydawcy(self):
        """Stopka wydawnicza. Zawsze druga strona — przed spisem treści."""
        m, w = self.meta, self.w
        karta = ([("Seria", f'{m["seria"]} · {m.get("tom", "")}'.strip(" ·"))] if m.get("seria") else []) + [
            ("Tytuł", f'{m["tytul"]} {m.get("podtytul_okladki", "")} — {m.get("haslo", "")}'.strip()),
            ("Na podstawie", m.get("zrodlo", "")),
            ("Odbiorcy", m.get("odbiorcy", "")),
            ("Zastosowanie", m.get("zastosowanie", "")),
            ("Format", "A4, {{STR:koniec}} stron; plik HTML i PDF, " + m.get("wydanie", "")),
        ]
        wiersze = "".join(f"<tr><td><b>{E(k)}</b></td><td>{E(v)}</td></tr>" for k, v in karta)
        kroki = "".join(f"<li>{E(x)}</li>" for x in m.get("druk", []))
        return f'''
<section class="page" id="metryczka">
  <h2 class="dzial-h">Metryczka wydawnicza</h2>
  <div class="metryczka duza">
    <div class="m-logo">{self.logo_duze()}</div>
    <div class="m-dane">
      <p class="m-org">{E(w["organizacja"])}</p>
      <p class="m-autor">opracowanie i redakcja: <b>{E(w["autorka"])}</b></p>
      <p class="m-mail"><span>kontakt</span> {E(w["mail"])}</p>
    </div>
  </div>
  <table class="tab-role szeroka metr-tab"><tbody>{wiersze}</tbody></table>
  <div class="uwaga jasna"><b>Ilustracje</b><br>{E(m.get("ilustracje_nota", ""))}</div>
  <div class="uwaga"><b>Prawa i wykorzystanie</b><br>{E(m.get("prawa", ""))}</div>
  <div class="gra-zasady"><h3>Jak wydrukować broszurę?</h3><ol class="dwie-kolumny">{kroki}</ol></div>
</section>'''

    def spis(self):
        wiersze = ""
        for r in self.R:
            etap = TOM_NAZWY[r["tom"]["etap"]][0]
            wiersze += (f'<li><a href="#r{r["nr"]}"><span class="s-nr">{r["nr"]}</span>'
                        f'<span class="s-tyt">{E(r["tytul"])}</span>'
                        f'<span class="s-etap">{etap}</span>'
                        f'<span class="s-str">{{{{STR:r{r["nr"]}}}}}</span></a></li>')
        czesci = "".join(
            f'<li><a href="#{i}"><span class="s-nr">{z}</span><span class="s-tyt">{t}</span>'
            f'<span class="s-str">{{{{STR:{i}}}}}</span></a></li>'
            for i, z, t in [
                ("metryczka", "·", "Metryczka wydawnicza i instrukcja druku"),
                ("jak-korzystac", "A", "Jak korzystać z broszury? Wskazówki dla nauczyciela i rodzica"),
                ("narzedzia", "B", "Trzy narzędzia: termometr, sygnalizator, drabina"),
                ("postacie", "C", "Karty postaci"),
                ("cwiczenia", "D", f'Ćwiczenia końcowe ({len(self.d.get("cwiczenia",[]))} zestawów)'),
                ("gra", "E", f'Gra „{self.d.get("gra",{}).get("nazwa","")}”'),
                ("scenariusz", "F", "Scenariusz przedstawienia szkolnego"),
            ])
        return f'''
<section class="page spis" id="spis">
  <h2 class="dzial-h">Spis treści</h2>
  <div class="spis-jedna">
    <div>
      <h3 class="spis-h">Części broszury <span class="spis-str-h">str.</span></h3>
      <ol class="spis-lista spis-czesci">{czesci}</ol>
      <div class="spis-info">
        <p><b>{len(self.R)} rozdziałów, każdy na trzech stronach.</b> Rytm jest zawsze taki sam, więc uczeń wie, czego się spodziewać:</p>
        <ol class="rytm">
          <li><b>Strona 1 — Historia i słowa.</b> Co się wydarzyło? Trudne pojęcia.</li>
          <li><b>Strona 2 — Emocje i wnioski.</b> Kto co czuje? Zależności między postaciami, przyczyna ➜ skutek.</li>
          <li><b>Strona 3 — Ocena i myślenie.</b> Czy to było w porządku? Teoria umysłu, pytania, notatki.</li>
        </ol>
        <p class="mini">Siedem stałych elementów rozdziału:</p>
        <ol class="siedem">
          <li>Co się wydarzyło?</li><li>Trudne słowa i pojęcia</li><li>Emocje</li>
          <li>Zależności między postaciami</li><li>Wyciąganie wniosków</li>
          <li>Ocena sytuacji</li><li>Teoria umysłu + pytania</li>
        </ol>
      </div>
    </div>
  </div>
</section>
<section class="page" id="spis2">
  <h2 class="dzial-h">Spis rozdziałów</h2>
  <p class="lead">Każdy rozdział zajmuje trzy strony. Litera <b>E1–E5</b> pokazuje, na którym etapie
  drabiny teorii umysłu jest ćwiczenie w tym rozdziale.</p>
  <p class="spis-legenda"><span>nr</span> numer rozdziału &nbsp;·&nbsp; <span>E1–E5</span> etap teorii umysłu
  &nbsp;·&nbsp; <span>str.</span> strona, na której zaczyna się rozdział</p>
  <ol class="spis-lista spis-rozdzialy dwie-kolumny">{wiersze}</ol>
</section>'''

    # ---- A. jak korzystać ----
    def jak_korzystac(self):
        u = self.meta.get("uwaga_trudne_tematy", "")
        uwaga = f'<div class="uwaga"><b>Ważna uwaga.</b> {E(u)}</div>' if u else ""
        return f'''
<section class="page" id="jak-korzystac">
  <h2 class="dzial-h"><span class="dzial-litera">A</span>Jak korzystać z broszury?</h2>
  <p class="lead">Ta broszura jest jednocześnie streszczeniem lektury i adaptacją. Można ją czytać zamiast oryginału,
  razem z oryginałem albo po nim. Nie trzeba robić wszystkiego — <b>lepiej zrobić trzy rozdziały dokładnie niż {len(self.R)} pobieżnie.</b></p>
  <div class="karty3">
    <div class="karta"><h3>Dla ucznia</h3><ul>
      <li>Czytaj po jednym rozdziale.</li>
      <li>Najpierw „Co się wydarzyło”. Potem reszta.</li>
      <li>Nie musisz odpowiadać na wszystkie pytania.</li>
      <li>Możesz odpowiadać ustnie, pisemnie, rysunkiem albo wskazując.</li>
      <li>Jeśli coś jest za trudne — powiedz o tym. To dobra informacja, nie porażka.</li></ul></div>
    <div class="karta"><h3>Dla nauczyciela</h3><ul>
      <li>Jeden rozdział = jedna jednostka lekcyjna. Nie łącz dwóch.</li>
      <li>Zawsze zapowiedz, ile części zrobicie dzisiaj.</li>
      <li>Zostaw 10 sekund ciszy po pytaniu. Nie skracaj tego czasu.</li>
      <li>Trudne pojęcia tłumacz przed czytaniem, nie po.</li>
      <li>Sprawdź wcześniej, które rozdziały poruszają trudne tematy.</li></ul></div>
    <div class="karta"><h3>Dla rodzica</h3><ul>
      <li>Czytajcie na głos, na zmianę zdaniami.</li>
      <li>Pytaj o emocje, nie o „morał”.</li>
      <li>Odpowiedź „nie wiem” jest dozwolona.</li>
      <li>Wracajcie do ulubionego rozdziału tyle razy, ile trzeba.</li>
      <li>Powtórzenie to nie strata czasu — to metoda.</li></ul></div>
  </div>
  <div class="uwaga jasna"><b>Zasada trzech stron.</b> Rozdział zawsze wygląda tak samo:
  strona 1 — historia i słowa, strona 2 — emocje i wnioski, strona 3 — myślenie i pytania.
  Przewidywalność układu jest tu narzędziem, nie ozdobą: uczeń nie musi za każdym razem uczyć się strony od nowa.</div>
</section>
<section class="page" id="jak-korzystac2">
  <h2 class="dzial-h"><span class="dzial-litera">A</span>Założenia adaptacji</h2>
  <p class="lead">Poniższe zasady zastosowano w każdym z {len(self.R)} rozdziałów. Warto je znać, zanim zacznie się pracę —
  i warto trzymać się ich, dopisując własne materiały.</p>
  <div class="zalozenia">
    <div><b>Krótkie zdania.</b> Jedno zdanie = jedna informacja. Bez zdań wielokrotnie złożonych.</div>
    <div><b>Stała struktura.</b> Siedem tych samych bloków w każdym rozdziale, zawsze w tej samej kolejności.</div>
    <div><b>Przenośnie tłumaczone wprost.</b> Podajemy oba znaczenia: dosłowne i ukryte. Dosłowne nie jest błędem.</div>
    <div><b>Emocje z sygnałami ciała.</b> Nie „był smutny”, tylko konkretne zachowanie, po którym to widać.</div>
    <div><b>Wnioskowanie krok po kroku.</b> Zawsze widoczna para: przyczyna ➜ skutek.</div>
    <div><b>Ocena bez pułapek.</b> Trzy kolory, a żółty jest pełnoprawną odpowiedzią. Świat rzadko jest zerojedynkowy.</div>
    <div><b>Teoria umysłu etapami.</b> Od „co widzę” do „co on myśli, że ja myślę” — zawsze z podanym etapem.</div>
    <div><b>Dwa poziomy pytań.</b> Zielone = odpowiedź jest w tekście. Niebieskie = trzeba wnioskować.</div>
    <div><b>Bez presji czasu.</b> Nigdzie w broszurze nie ma zadań na czas ani rywalizacji między uczniami.</div>
  </div>
  {uwaga}
</section>'''

    # ---- B. narzędzia ----
    def narzedzia(self):
        etapy_rozdz = {e: [] for e in range(1, 6)}
        for r in self.R:
            etapy_rozdz[r["tom"]["etap"]].append(str(r["nr"]))
        opisy = {
            1: "Perspektywa. Dwie osoby patrzą na to samo i widzą co innego, bo mają inną wiedzę.",
            2: "Rozpoznanie emocji po sygnałach: twarz, ciało, głos, zachowanie.",
            3: "Pragnienie i jego związek z uczuciem: dostał, czego chciał — cieszy się.",
            4: "Przekonania — także fałszywe. Ktoś może myśleć coś nieprawdziwego i działać zgodnie z tym.",
            5: "Drugie piętro: przenośnia, ironia, ukrywanie uczuć, dwa znaczenia jednego zdania.",
        }
        etapy = "".join(
            f'<li><b>{TOM_NAZWY[e][0]} · {E(TOM_NAZWY[e][1])}</b> {E(opisy[e])} '
            f'<span>rozdz. {", ".join(etapy_rozdz[e]) or "—"}</span></li>' for e in range(1, 6))
        return f'''
<section class="page" id="narzedzia">
  <h2 class="dzial-h"><span class="dzial-litera">B</span>Trzy narzędzia do całej broszury</h2>
  <p class="lead">Te trzy pomoce wracają w każdym rozdziale — warto wydrukować je osobno i powiesić w klasie.</p>
  <div class="narz">
    <div class="narz-box">
      <h3>1 · Termometr emocji — jak mocno?</h3>
      <p>Odpowiada na pytanie „jak mocno?”. Emocja nie jest tylko obecna albo nieobecna — ma natężenie.
      W tabelach emocji zieloną skalą zaznaczono siłę uczucia.</p>
      {fig(S.thermometer())}
    </div>
    <div class="narz-box">
      <h3>2 · Sygnalizator — czy to było w porządku?</h3>
      <p>Odpowiada na pytanie „czy to było w porządku?”. Uwaga: <b>żółty nie jest gorszą odpowiedzią</b> —
      w większości sytuacji społecznych to właśnie on jest poprawny.</p>
      <div class="sygn-lista">
        <div class="sy zielone"><span class="znak">✔</span><div><b>ZIELONE — w porządku</b><p>Nikomu nie stała się krzywda. Tak można postępować.</p></div></div>
        <div class="sy zolte"><span class="znak">!</span><div><b>ŻÓŁTE — to zależy</b><p>Były dobre powody, ale dało się to zrobić lepiej. Szukamy lepszego sposobu.</p></div></div>
        <div class="sy czerwone"><span class="znak">✖</span><div><b>CZERWONE — tak nie postępujemy</b><p>Ktoś został skrzywdzony albo naraża się na niebezpieczeństwo.</p></div></div>
      </div>
    </div>
  </div>
  <h3 class="pod-h">Kiedy sięgnąć po które narzędzie?</h3>
  <div class="kiedy">
    <div><b>Termometr</b><span>gdy uczeń nie wie, <i>jak mocno</i> coś czuje</span></div>
    <div><b>Sygnalizator</b><span>gdy uczeń widzi tylko dobrze albo źle</span></div>
    <div><b>Drabina</b><span>gdy ćwiczenie jest za trudne i trzeba zejść niżej</span></div>
  </div>
</section>
<section class="page" id="narzedzia2">
  <h2 class="dzial-h"><span class="dzial-litera">B</span>Drabina teorii umysłu</h2>
  <div class="narz-box szeroki">
    <h3>Pięć etapów — od najprostszego do najtrudniejszego</h3>
    <p>Teoria umysłu to umiejętność domyślania się, co druga osoba widzi, czuje, chce i myśli.
    Ćwiczy się ją stopniami — nie od razu na najwyższym poziomie. Każdy rozdział ma ćwiczenie oznaczone etapem <b>E1–E5</b>.</p>
    <div class="drabina">
      {fig(S.tom_ladder())}
      <ol class="etapy">{etapy}</ol>
    </div>
    <p class="mini">Jeśli uczeń nie radzi sobie z ćwiczeniem na etapie E4, wróć do rozdziału z etapem E2 lub E3.
    Kolejność etapów jest ważniejsza niż kolejność rozdziałów.</p>
  </div>
</section>'''

    # ---- C. postacie ----
    def _karty_postaci(self, lista):
        karty = ""
        for p in lista:
            karty += f'''<div class="postac">
        <div class="p-ico">{S.icon(p.get("ikona","star"), 60)}</div>
        <div class="p-tresc">
          <h3>{E(p["nazwa"])}</h3>
          <p class="p-kim">{E(p.get("kim",""))}</p>
          <p><b>Jak się zachowuje?</b> {E(p.get("zachowanie",""))}</p>
          <p><b>Po co jest w książce?</b> {E(p.get("rola",""))}</p>
        </div></div>'''
        return karty

    def postacie(self):
        P = self.d.get("postacie", [])
        grupy = [P[i:i + 4] for i in range(0, len(P), 4)] or [[]]
        out = []
        for i, g in enumerate(grupy):
            naglowek = ('<h2 class="dzial-h"><span class="dzial-litera">C</span>Kto jest kim? Karty postaci</h2>'
                        if i == 0 else
                        f'<h2 class="dzial-h"><span class="dzial-litera">C</span>Karty postaci '
                        f'<small class="cd">· ciąg dalszy ({i+1} z {len(grupy)})</small></h2>')
            lead = ('<p class="lead">Przeczytaj te karty przed rozpoczęciem lektury. '
                    'Wróć do nich, gdy zapomnisz, kto jest kim.</p>' if i == 0 else "")
            out.append(f'<section class="page" id="postacie{"" if i==0 else i+1}">'
                       f'{naglowek}{lead}<div class="postacie">{self._karty_postaci(g)}</div></section>')
        return "".join(out)

    # ---- rozdział: trzy strony ----
    def mini_head(self, r, part):
        return (f'<header class="r-head mini"><div class="r-nr"><span>ROZDZ.</span><b>{r["nr"]}</b></div>'
                f'<div class="r-tyt"><h2>{E(r["tytul"])}</h2>'
                f'<p class="r-miejsce">część {part} z 3 · {CZESCI[part-1]}</p></div>'
                f'<div class="r-ikona">{S.icon(r.get("ikona","star"), 52)}</div></header>')

    def rozdzial(self, r):
        nr = r["nr"]
        ilu = self.ilustracja(r)
        stresz = "".join(f"<li>{E(x)}</li>" for x in r["streszczenie"])
        postaci, chipy = [], ""
        for e in r["emocje"]:
            if e["kto"] not in postaci:
                postaci.append(e["kto"])
        chipy = "".join(f'<span class="chip">{E(k)}</span>' for k in postaci)
        slowka = "".join(f'<div class="slowo"><dt>{E(s["pojecie"])}</dt><dd>{E(s["wyjasnienie"])}</dd></div>'
                         for s in r["slowka"])
        emo = "".join(
            f'<tr><td class="kto">{E(e["kto"])}</td><td class="emo">{E(e["emocja"])}</td>'
            f'<td class="sygn">{E(e["sygnal"])}</td><td class="lvl">{skala(e["poziom"])}</td></tr>'
            for e in r["emocje"])
        wn = "".join(
            f'<li><span class="przycz">{E(x["przyczyna"])}</span>'
            f'<span class="strzalka" aria-hidden="true">➜</span>'
            f'<span class="skutek">{E(x["skutek"])}</span></li>' for x in r["wnioski"])
        kl, znak = kolor_oceny(r["ocena"]["odpowiedz"])
        etap, nazwa = TOM_NAZWY[r["tom"]["etap"]]
        tom_tresc = "".join(f"<p>{E(l)}</p>" for l in r["tom"]["tresc"].split("\n") if l.strip())
        lat = "".join(f"<li>{E(q)}</li>" for q in r["pytania_latwe"])
        tru = "".join(f"<li>{E(q)}</li>" for q in r["pytania_trudne"])
        ile_linii = self.linie.get(str(nr), self.linie.get(nr, 8))
        linie = "<i></i>" * ile_linii

        notatki = (f'<div class="notatki"><h3>Miejsce na notatki i własne pytania</h3>'
                   f'<div class="linie">{linie}</div></div>') if ile_linii else ""

        a = f'''
<section class="page rozdzial" id="r{nr}">
  <header class="r-head">
    <div class="r-nr"><span>ROZDZIAŁ</span><b>{nr}</b></div>
    <div class="r-tyt"><h2>{E(r["tytul"])}</h2><p class="r-miejsce">{E(r.get("miejsce",""))}</p></div>
    <div class="r-ikona">{S.icon(r.get("ikona","star"), 74)}</div>
  </header>
  <p class="r-mysl">„{E(r["mysl"])}”</p>
  <div class="blok blok-kto">
    <span class="kto-etykieta">Kto występuje?</span>
    <div class="chipy">{chipy}</div>
  </div>
  <div class="r-grid">
    <div class="kol-a">
      <div class="blok blok-stresz">
        <h3><span class="bi">📖</span>Co się wydarzyło?</h3>
        <ol class="stresz">{stresz}</ol>
      </div>
    </div>
    <div class="kol-b">
      {ilu}
      <div class="blok blok-slownik">
        <h3><span class="bi">🔑</span>Trudne słowa i pojęcia</h3>
        <dl class="slownik">{slowka}</dl>
      </div>
    </div>
  </div>
  {self.stopka_rozdzialu(nr, 1)}
</section>

<section class="page rozdzial" id="r{nr}b">
  {self.mini_head(r, 2)}
  <div class="blok blok-emo">
    <h3><span class="bi">💚</span>Emocje — kto, co czuje i po czym to poznasz?</h3>
    <table class="tab-emo">
      <thead><tr><th>Kto?</th><th>Jaka emocja?</th><th>Po czym to poznasz?</th><th>Jak mocno?</th></tr></thead>
      <tbody>{emo}</tbody>
    </table>
  </div>
  <div class="blok blok-zal">
    <h3><span class="bi">🔗</span>Zależności między postaciami</h3>
    <p>{E(r["zaleznosci"])}</p>
  </div>
  <div class="blok blok-wn">
    <h3><span class="bi">🧩</span>Wyciąganie wniosków — przyczyna i skutek</h3>
    <ul class="wnioski">{wn}</ul>
  </div>
  {self.stopka_rozdzialu(nr, 2)}
</section>

<section class="page rozdzial" id="r{nr}c">
  {self.mini_head(r, 3)}
  <div class="blok blok-ocena {kl}">
    <h3><span class="bi">🚦</span>Ocena sytuacji</h3>
    <p class="o-pyt">{E(r["ocena"]["pytanie"])}</p>
    <p class="o-odp"><span class="znak">{znak}</span>{E(r["ocena"]["odpowiedz"])}</p>
  </div>
  <div class="blok blok-tom">
    <h3><span class="etap">{etap}</span>Teoria umysłu — {E(nazwa)}</h3>
    <div class="tom-tresc">
      <p class="tom-tyt"><b>{E(r["tom"]["tytul"])}</b></p>
      {tom_tresc}
    </div>
  </div>
  <div class="pytania">
    <div class="pyt pyt-latwe">
      <h3><span class="bi">🟢</span>Pytania łatwiejsze <small>— odpowiedź jest wprost w tekście</small></h3>
      <ol>{lat}</ol>
    </div>
    <div class="pyt pyt-trudne">
      <h3><span class="bi">🔵</span>Pytania trudniejsze <small>— trzeba pomyśleć i połączyć fakty</small></h3>
      <ol>{tru}</ol>
    </div>
  </div>
  {notatki}
  {self.stopka_rozdzialu(nr, 3)}
</section>'''
        return a

    # ---- D. ćwiczenia (po 2 na stronę) ----
    def cwiczenia(self):
        C = self.d.get("cwiczenia", [])
        if not C:
            return ""
        grupy = [C[i:i + 2] for i in range(0, len(C), 2)]
        out = []
        for i, g in enumerate(grupy):
            naglowek = ('<h2 class="dzial-h"><span class="dzial-litera">D</span>Ćwiczenia końcowe</h2>'
                        if i == 0 else
                        f'<h2 class="dzial-h"><span class="dzial-litera">D</span>Ćwiczenia końcowe '
                        f'<small class="cd">· ciąg dalszy ({i+1} z {len(grupy)})</small></h2>')
            lead = (f'<p class="lead">{len(C)} zestawów do wykorzystania po przeczytaniu całości albo po większych partiach. '
                    'Każdy ma podany cel, czas i konkretne dostosowanie. '
                    '<b>Nie trzeba robić wszystkich — trzy zrobione dobrze znaczą więcej niż osiem po łebkach.</b></p>'
                    if i == 0 else "")
            ost = ('<div class="uwaga"><b>Jak sprawdzić, czy to działa?</b> Nie po tym, ile ćwiczeń uczeń wykonał, '
                   'tylko po tym, czy zaczyna sam mówić zdania typu „on chyba tak pomyślał, bo…”, '
                   '„ona się chyba bała, dlatego krzyknęła”. To jest właściwy wskaźnik postępu.</div>'
                   if i == len(grupy) - 1 else "")
            karty = ""
            for c in g:
                kroki = "".join(f"<li>{E(x)}</li>" for x in c["kroki"])
                karty += f'''<div class="cwicz">
                  <div class="c-head"><span class="c-nr">{c["nr"]}</span>
                    <div><h3>{E(c["tytul"])}</h3>
                    <p class="c-meta">{E(c["cel"])} · {E(c["czas"])} · {E(c["forma"])}</p></div></div>
                  <p class="c-opis">{E(c["opis"])}</p>
                  <ol class="c-kroki">{kroki}</ol>
                  <p class="c-dost"><b>Dostosowanie</b> — {E(c["dostosowanie"])}</p></div>'''
            out.append(f'<section class="page" id="cwiczenia{"" if i==0 else i+1}">'
                       f'{naglowek}{lead}<div class="cwiczenia">{karty}</div>{ost}</section>')
        return "".join(out)

    # ---- E. gra ----
    def gra_instrukcja(self, G):
        """Osobna strona: co przygotować, jak przebiega kolejka, co robi nauczyciel."""
        I = G.get("instrukcja")
        if not I:
            return ""
        przyg = "".join(f"<li>{E(x)}</li>" for x in I.get("co_przygotowac", []))
        kroki = "".join(f"<li>{E(x)}</li>" for x in I.get("przygotowanie", []))
        kolej = "".join(f"<li>{E(x)}</li>" for x in I.get("kolejka", []))
        kol = "".join(
            f'<tr><td><span class="kropka" style="background:{k["kolor"]}"></span>'
            f'<b>{E(k["talia"])}</b></td><td>{E(k["co_cwiczy"])}</td><td>{E(k["jak"])}</td></tr>'
            for k in I.get("kolory", []))
        naucz = "".join(f"<li>{E(x)}</li>" for x in I.get("rola_nauczyciela", []))
        trud = "".join(f"<li>{E(x)}</li>" for x in I.get("gdy_trudno", []))
        war = "".join(f'<div class="spec"><b>{E(x["nazwa"])}</b><p>{E(x["opis"])}</p></div>'
                      for x in I.get("warianty", []))
        return f'''
<section class="page" id="gra-instrukcja">
  <h2 class="dzial-h"><span class="dzial-litera">E</span>Jak przeprowadzić grę? Krok po kroku</h2>
  <div class="spekt-info">
    <div><span>Ile osób?</span><b>{E(I.get("ile_osob",""))}</b></div>
    <div><span>Ile czasu?</span><b>{E(I.get("ile_czasu",""))}</b></div>
  </div>
  <div class="kol-2">
    <div class="gra-zasady"><h3>Co przygotować?</h3><ul>{przyg}</ul></div>
    <div class="gra-zasady"><h3>Przygotowanie stołu</h3><ol>{kroki}</ol></div>
  </div>
</section>
<section class="page" id="gra-instrukcja2">
  <h2 class="dzial-h"><span class="dzial-litera">E</span>Przebieg kolejki i kolory pól</h2>
  <div class="gra-zasady"><h3>Przebieg jednej kolejki</h3><ol>{kolej}</ol></div>
  <h3 class="pod-h">Co oznacza kolor pola?</h3>
  <table class="tab-role szeroka tab-kolory"><thead><tr><th>Talia</th><th>Co ćwiczy?</th><th>Jak odpowiadać?</th></tr></thead>
  <tbody>{kol}</tbody></table>
</section>
<section class="page" id="gra-instrukcja3">
  <h2 class="dzial-h"><span class="dzial-litera">E</span>Rola dorosłego i warianty gry</h2>
  <div class="kol-2">
    <div class="gra-zasady"><h3>Co robi nauczyciel?</h3><ul>{naucz}</ul></div>
    <div class="gra-zasady"><h3>Gdy uczeń nie umie odpowiedzieć</h3><ul>{trud}</ul></div>
  </div>
  <h3 class="pod-h">Warianty gry</h3>
  <div class="specjalne">{war}</div>
  <div class="uwaga jasna"><b>Po co ta gra?</b> Każde pole to jedno z czterech pytań całej broszury:
  co czuje?, dlaczego tak się stało?, czy to było w porządku?, co on myśli? Uczeń odpowiada na nie
  kilkanaście razy w pół godziny — za każdym razem bez ryzyka, że przegra.</div>
</section>'''

    def gra(self):
        G = self.d.get("gra")
        if not G:
            return ""
        zasady = "".join(f"<li>{E(z)}</li>" for z in G["zasady"])
        tal = []
        for t in G["talie"]:
            kk = "".join(f"<li>{E(x)}</li>" for x in t["karty"])
            tal.append(f'<div class="talia"><h4><span class="kropka" style="background:{t["kolor"]}"></span>'
                       f'{E(t["nazwa"])}</h4><ol>{kk}</ol></div>')
        spec = "".join(f'<div class="spec"><b>{E(p["pole"])}</b><p>{E(p["opis"])}</p></div>'
                       for p in G.get("pola_specjalne", []))
        return f'''
<section class="page" id="gra">
  <h2 class="dzial-h"><span class="dzial-litera">E</span>Gra „{E(G["nazwa"])}”</h2>
  <p class="lead">{E(G.get("wstep",""))}</p>
  {fig(S.board(), "plansza", "Plansza — 30 pól ułożonych wężem. Przerysuj na duży arkusz albo wydrukuj tę stronę w formacie A3.")}
  <div class="gra-zasady"><h3>Jak grać? Zasady</h3><ol class="dwie-kolumny">{zasady}</ol></div>
</section>
{self.gra_instrukcja(G)}
<section class="page" id="gra2">
  <h2 class="dzial-h"><span class="dzial-litera">E</span>Karty zadań do gry</h2>
  <h3 class="pod-h">Talie 1 i 2 <small>— kolor talii = kolor pola na planszy</small></h3>
  <div class="talie">{"".join(tal[:2])}</div>
  <h3 class="pod-h">Pola specjalne</h3>
  <div class="specjalne">{spec}</div>
</section>
<section class="page" id="gra3">
  <h2 class="dzial-h"><span class="dzial-litera">E</span>Karty zadań <small class="cd">· talie 3 i 4</small></h2>
  <div class="talie">{"".join(tal[2:])}</div>
  <div class="gra-uwaga"><b>Dlaczego w tej grze nikt nie przegrywa?</b> Rywalizacja i presja czasu obciążają uczniów
  ze spektrum autyzmu tak mocno, że przestają myśleć o zadaniu, a zaczynają myśleć o porażce. Wspólny wynik klasy
  zamienia grę we współpracę — a ćwiczone umiejętności są społeczne, więc współpraca jest tu również treścią, nie tylko formą.</div>
</section>
<section class="page" id="gra-plansza">
  <h2 class="dzial-h"><span class="dzial-litera">E</span>Plansza do wydruku</h2>
  <p class="lead">Wydrukuj tę stronę osobno, najlepiej w formacie A3 i na grubszym papierze.
  Pionki mogą być guzikami albo nakrętkami — ważne, żeby każdy gracz rozpoznawał swój na pierwszy rzut oka.</p>
  {fig(S.board(), "plansza-duza")}
  <p class="mini">Kolor pola mówi, z której talii wziąć kartę zadania. Pola ciemne to pola specjalne —
  ich opisy znajdziesz dwie strony wcześniej.</p>
</section>'''

    # ---- F. scenariusz ----
    def scenariusz(self):
        SC = self.d.get("scenariusz")
        if not SC:
            return ""
        i = SC["info"]
        role = "".join(f'<tr><td><b>{E(x["rola"])}</b></td><td>{E(x["opis"])}</td></tr>' for x in SC["obsada"])
        zas = "".join(f"<li>{E(z)}</li>" for z in SC["zasady"])
        grupy = []
        nr = 0
        for g in SC.get("zasady_grupy", []):
            karty = ""
            for z in g["zasady"]:
                nr += 1
                karty += (f'<div class="zas-karta"><span class="zk-nr">{nr}</span>'
                          f'<b>{E(z["tytul"])}</b><p>{E(z["opis"])}</p></div>')
            grupy.append(f'<div class="zas-grupa" style="--zg:{g.get("kolor", C_ZG)}">'
                         f'<h3><span class="zg-ikona">{S.icon(g.get("ikona", "star"), 30)}</span>'
                         f'{E(g["nazwa"])}</h3><div class="zas-karty">{karty}</div></div>')
        # pierwsza grupa na stronie F-2, reszta na F-2b — komplet nie mieści się na jednym arkuszu
        grupy_zas_a = "".join(grupy[:2])
        grupy_zas_b = "".join(grupy[2:])
        rek = "".join(f"<li>{E(z)}</li>" for z in SC["rekwizyty"])
        prob = "".join(f'<tr><td><b>{E(p["nazwa"])}</b></td><td>{E(p["opis"])}</td></tr>' for p in SC["proby"])
        program = "".join(f'<li><b>{E(s["tytul"])}</b><span>{E(s["osoby"])}</span></li>' for s in SC["sceny"])
        out = [f'''
<section class="page" id="scenariusz">
  <h2 class="dzial-h"><span class="dzial-litera">F</span>Scenariusz przedstawienia</h2>
  <h3 class="podtytul-spekt">„{E(SC["tytul"])}”</h3>
  {fig(S.stage(), "maly")}
  <div class="spekt-info">
    <div><span>Czas trwania</span><b>{E(i["czas"])}</b></div>
    <div><span>Obsada</span><b>{E(i["obsada"])}</b></div>
    <div><span>Próby</span><b>{E(i["proby"])}</b></div>
    <div><span>Muzyka</span><b>{E(i["muzyka"])}</b></div>
  </div>
  <h3 class="pod-h">Kto gra? Obsada skalowalna</h3>
  <table class="tab-role szeroka"><tbody>{role}</tbody></table>
  <p class="mini">{E(SC.get("uwaga_obsada",""))}</p>
</section>

<section class="page" id="scenariusz2">
  <h2 class="dzial-h"><span class="dzial-litera">F</span>Zasady dostosowania</h2>
  <p class="lead">Przeczytaj tę stronę przed pierwszą próbą. Te zasady decydują o tym, czy uczniowie w ogóle wejdą na scenę.</p>
  {f'<div class="zas-grupy">{grupy_zas_a}</div>' if grupy_zas_a
    else f'<h3 class="pod-h">Jak dostosować przedstawienie?</h3><ol class="zas-spekt">{zas}</ol>'}
</section>

<section class="page" id="scenariusz2b">
  <h2 class="dzial-h"><span class="dzial-litera">F</span>Zasady dostosowania <small class="cd">· ciąg dalszy</small></h2>
  <div class="zas-grupy">{grupy_zas_b}</div>
  <div class="uwaga jasna"><b>Kto nie chce grać, ten też gra.</b> Zespół techniczny, sufler i osoba
  odpowiedzialna za rekwizyty to pełnoprawne role. Wpisz je do programu tak samo dużą czcionką
  jak role sceniczne — to nie jest gest kurtuazji, tylko warunek, żeby nikt nie został poza projektem.</div>
  <p class="mini">Powieś plan wizualny scen w miejscu prób i za kulisami. Uczniowie mają wtedy stale przed oczami
  informację, ile jeszcze zostało — to jedno z najskuteczniejszych dostosowań w całym projekcie.</p>
</section>

<section class="page" id="scenariusz3">
  <h2 class="dzial-h"><span class="dzial-litera">F</span>Program, rekwizyty i plan prób</h2>
  <h3 class="pod-h">Program przedstawienia — {len(SC["sceny"])} scen</h3>
  <ol class="program">{program}</ol>
</section>

<section class="page" id="scenariusz4">
  <h2 class="dzial-h"><span class="dzial-litera">F</span>Rekwizyty i plan prób</h2>
  <div class="spekt-2kol">
    <div><h3 class="pod-h">Rekwizyty</h3><ul class="rek">{rek}</ul></div>
    <div><h3 class="pod-h">Plan prób</h3><table class="tab-prob"><tbody>{prob}</tbody></table></div>
  </div>
</section>''']
        # sceny: pierwsze dwie razem, dalej po jednej - dłuższe sceny nie mieszczą się parami
        grupy = [[n] for n in range(1, len(SC["sceny"]) + 1)]
        for idx, grupa in enumerate(grupy):
            sceny = ""
            for sc in SC["sceny"]:
                if sc["nr"] not in grupa:
                    continue
                linie = "".join(
                    f'<div class="kwestia"><span class="kto">{E(k["kto"])}</span>'
                    f'<span class="tekst">{E(k["tekst"])}</span></div>' for k in sc["kwestie"])
                sceny += f'''<div class="scena">
                  <div class="s-head"><span class="s-nr">SCENA {sc["nr"]}</span><h4>{E(sc["tytul"])}</h4></div>
                  <p class="s-meta"><b>Miejsce:</b> {E(sc["miejsce"])} &nbsp;·&nbsp; <b>Osoby:</b> {E(sc["osoby"])}</p>
                  <div class="kwestie">{linie}</div>
                  <p class="s-wsk"><b>Wskazówka reżyserska</b> — {E(sc["wskazowka"])}</p></div>'''
            opis = ("sceny " + " i ".join(map(str, grupa))) if len(grupa) > 1 else f"scena {grupa[0]}"
            koncowka = ('<div class="uwaga"><b>Finał bez niespodzianek.</b> Po ostatnim zdaniu cały zespół — '
                        'łącznie z ekipą techniczną — ustawia się w rzędzie i kłania jednocześnie. Ustalcie to na '
                        'przedostatniej próbie i nie zmieniajcie. Wiedza o tym, co dokładnie stanie się na końcu, '
                        'jest dla wielu uczniów warunkiem tego, żeby w ogóle wejść na scenę.</div>'
                        if idx == len(grupy) - 1 else "")
            out.append(f'<section class="page" id="scenariusz-t{idx+1}">'
                       f'<h2 class="dzial-h"><span class="dzial-litera">F</span>Tekst przedstawienia '
                       f'<small class="cd">· {opis} z {len(SC["sceny"])}</small></h2>'
                       f'<div class="sceny">{sceny}</div>{koncowka}</section>')
        return "".join(out)


    # ---- G. załączniki do wycięcia ----
    def zalaczniki(self):
        Z = self.d.get("zalaczniki")
        if not Z:
            return ""
        out = []
        G = self.d.get("gra", {})

        if Z.get("termometr", True):
            out.append(f'''
<section class="page" id="zalaczniki" data-stary="zalacznik-termometr">
  <h2 class="dzial-h"><span class="dzial-litera">G</span>Załącznik 1 · Termometr emocji do wycięcia</h2>
  <p class="lead">Wytnij po linii przerywanej i naklej na sztywny papier. Wskaźnik „TERAZ”
  wytnij osobno i przypnij spinaczem z boku — uczeń przesuwa go w górę i w dół.</p>
  {fig(S.thermometer_cut(), "termometr-wyciecie")}
  <div class="uwaga jasna"><b>Dla ucznia, który nie czyta?</b> Każdy stopień jest opisany
  na cztery sposoby naraz: kolorem, wysokością słupka, miną i liczbą kropek — wystarczy jeden z nich.
  Uczeń może pokazać palcem minę albo policzyć kropki; słowo obok jest wtedy podpowiedzią dla dorosłego.
  <b>Jak pytać?</b> „Jak mocno?”, a nie „czy bardzo?” — pytanie zamknięte daje odpowiedź tak/nie,
  a termometr ma pokazać stopień.</div>
</section>''')

        if Z.get("sygnalizator", True):
            out.append('''
<section class="page" id="zalacznik-sygnalizator">
  <h2 class="dzial-h"><span class="dzial-litera">G</span>Załącznik 2 · Krążki do oceny sytuacji</h2>
  <p class="lead">Wytnij po jednym komplecie dla każdego ucznia. Krążki służą do ćwiczenia
  „Sygnalizator sytuacji” z części D, ale przydają się też w codziennych sytuacjach w klasie.</p>
  <div class="krazki">
    <div class="krazek zielony"><span class="znak">✔</span><b>ZIELONE</b><p>w porządku</p></div>
    <div class="krazek zolty"><span class="znak">!</span><b>ŻÓŁTE</b><p>to zależy</p></div>
    <div class="krazek czerwony"><span class="znak">✖</span><b>CZERWONE</b><p>tak nie postępujemy</p></div>
  </div>
  <div class="uwaga jasna"><b>Żółty jest najważniejszy.</b> To on wymaga myślenia i to on jest poprawny
  w większości sytuacji społecznych. Jeśli uczeń używa tylko zielonego i czerwonego, wracaj do pytania:
  „a czy były jakieś powody?”.</div>
</section>''')

        karty = Z.get("karty", [])
        if karty:
            grupy = [karty[i:i + 4] for i in range(0, len(karty), 4)]
            for i, g in enumerate(grupy):
                nr_z = 3 + (1 if Z.get("plansza", True) else 0) * 0 + 1 + i
                kk = ""
                for k in g:
                    kk += f'''<div class="karta-planeta">
                      <div class="kp-gora">{self.ilustracja(k) or fig(S.karta_planety(k.get("ikona","asteroid")))}</div>
                      <div class="kp-dol">
                        <h4>{E(k["nazwa"])}</h4>
                        <p class="kp-kto">{E(k.get("kto",""))}</p>
                        <p class="kp-opis">{E(k.get("opis",""))}</p>
                        <p class="kp-pyt">{E(k.get("pytanie",""))}</p>
                      </div></div>'''
                dod = "" if i == 0 else f' <small class="cd">· ciąg dalszy ({i+1} z {len(grupy)})</small>'
                lead = ('<p class="lead">Wytnij po liniach przerywanych i naklej na sztywny papier. '
                        'Karty służą do gry, do powtórki i do ustawiania kolejności podróży.</p>'
                        if i == 0 else "")
                out.append(f'<section class="page" id="zalacznik-karty{i+1}">'
                           f'<h2 class="dzial-h"><span class="dzial-litera">G</span>'
                           f'Załącznik 3 · Karty miejsc i spotkań{dod}</h2>{lead}'
                           f'<div class="karty-planet">{kk}</div></section>')
        return "".join(out)

    # ---- zakończenie + metryczka ----
    def zakonczenie(self):
        z = self.d.get("zakonczenie", {})
        m, w = self.meta, self.w
        akapity = "".join(f"<p>{E(a)}</p>" for a in z.get("akapity", []))
        inicjaly = w.get("inicjaly") or ".".join(x[0] for x in w["autorka"].split() if x) + "."
        pozegnanie = ""
        if z.get("pozegnanie"):
            pozegnanie = (
                f'<div class="pozegnanie">'
                f'<div class="poz-znak">{self.logo_duze()}</div>'
                f'<h3>{E(z.get("pozegnanie_naglowek", "Na pożegnanie"))}</h3>'
                f'<p class="poz-tekst">{E(z["pozegnanie"])}</p>'
                f'<div class="poz-serce">{S.serce()}</div>'
                f'<p class="poz-inicjaly">{E(inicjaly)}</p>'
                f'<p class="poz-imie">{E(w["autorka"])}</p>'
                f'<p class="poz-org">{E(w["organizacja"])} · {E(w["mail"])}</p></div>')
        return f'''
<section class="page konc" id="koniec">
  {self.ilustracja({"obraz": z.get("obraz")}, "konc-foto") if z.get("obraz") else fig(S.stars_laugh(), "mini")}
  <h2 class="dzial-h">Na koniec</h2>
  <blockquote class="cytat">„{E(z.get("cytat",""))}”<cite>{E(z.get("cytat_zrodlo",""))}</cite></blockquote>
  <div class="konc-tresc">{akapity}</div>
  {pozegnanie}
</section>'''
