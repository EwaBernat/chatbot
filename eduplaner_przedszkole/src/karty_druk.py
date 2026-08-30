# -*- coding: utf-8 -*-
"""Materiały do wydruku wymagane przez konspekty — karty, plansze, historyjki.

Karta pomocy (`pomoce_a`, `pomoce_b`) mówi nauczycielowi, JAK pomoc ma wyglądać
i jak jej użyć. Część konspektów wymaga jednak samego materiału: kart do
wycięcia, planszy z piktogramami, historyjki obrazkowej. Opis wtedy nie
wystarcza — nauczyciel ma to wydrukować i wyciąć, a nie odtwarzać z fotografii.

Ten moduł trzyma takie arkusze: A4 z siatką kart, linia cięcia dookoła każdej,
numeracja tam, gdzie kolejność ma znaczenie. Przy druku każdy arkusz zaczyna
nową stronę (reguła `.zal + .zal` w arkuszu stylów banku).

Rejestr jest kluczowany numerem konspektu, tak samo jak `POMOCE` — `build.py`
dokłada arkusze do sekcji VII tego konspektu, bez zmian w generatorze.
"""

import base64
from pathlib import Path

_KORZEN = Path(__file__).resolve().parent.parent


def _obraz(katalog, kod):
    dane = base64.b64encode((_KORZEN / "assets" / katalog / f"k_{kod}.jpg").read_bytes()).decode()
    return f"data:image/jpeg;base64,{dane}"


# nr konspektu → lista arkuszy; arkusz = (tytuł, wstęp, katalog, kolumny, [(kod, podpis)])
ARKUSZE = {
 "D2-06": [(
   "Karty-zaproszenia",
   "Wydrukuj, wytnij po linii i naklej na sztywniejszy karton. Miś wręcza dziecku jedną kartę, "
   "dziecko idzie z nią do stolika, na którym czeka ta właśnie zabawa. Po zabawie karta wraca "
   "do koszyka. Zestaw obejmuje sześć zabaw — wybierz te, które faktycznie masz przygotowane "
   "w sali, i drukuj po dwa egzemplarze każdej, żeby starczyło na wybór z dwóch.",
   "karty_a", 3,
   [("d2_06_klocki",    "Klocki"),
    ("d2_06_ukladanka", "Układanka"),
    ("d2_06_rysowanie", "Rysowanie"),
    ("d2_06_lalki",     "Kącik lalek"),
    ("d2_06_auta",      "Samochody"),
    ("d2_06_ksiazki",   "Książeczki")]),
 ],
}


def _kody(nry=None):
    """Kody obrazków w rejestrze, z katalogiem, bez powtórzeń.

    `nry` zawęża do wskazanych konspektów — zeszyt jednej grupy wiekowej nie ma
    po co nieść materiałów z pozostałych.
    """
    widziane = {}
    for nr, arkusze in ARKUSZE.items():
        if nry is not None and nr not in nry:
            continue
        for _, _, katalog, _, karty in arkusze:
            for kod, _ in karty:
                widziane[kod] = katalog
    return widziane


def style_kart(nry=None):
    """Obrazki osadzone raz, w klasach CSS — arkusz może się powtarzać."""
    regu = "\n".join(f'.kd-{kod}{{background-image:url({_obraz(kat, kod)})}}'
                     for kod, kat in sorted(_kody(nry).items()))
    return f"<style>{regu}</style>" if regu else ""


def arkusz(nr, tytul, wstep, kolumny, karty, numer, ile, esc):
    kafle = "\n".join(f'''      <figure class="kafel kwadrat">
        <span class="obraz kd-{kod}" role="img" aria-label="{esc(podpis)}"></span>
        <figcaption>{esc(podpis)}</figcaption>
        <span class="linia-ciecia" aria-hidden="true"></span>
      </figure>''' for kod, podpis in karty)
    return f'''<section class="zal" data-poziom="p1">
  <header class="zal-head">
    <span class="mark" role="img" aria-label="Logo PCTP"></span>
    <div>
      <div class="zal-w">EduPlaner 2026</div>
      <div class="zal-s">Materiał do wydruku {numer} z {ile} · konspekt {esc(nr)}</div>
    </div>
    <span class="zal-pill p1">do wycięcia</span>
  </header>
  <div class="zal-tytul">
    <span class="zal-kp">Wydrukuj i wytnij</span>
    <h3>{esc(tytul)}</h3>
  </div>
  <p class="kkurs">{esc(wstep)}</p>
  <div class="zal-siatka k{kolumny}">
{kafle}
  </div>
  <div class="zal-stopka">
    <span><b>Konspekt {esc(nr)}</b> · materiał do wydruku</span>
    <span class="mono">EduPlaner 2026 · PCTP · druk KC-5</span>
  </div>
</section>'''


def karty_dla(nr, esc):
    """Arkusze do wydruku dla konspektu o tym numerze albo pusty string."""
    arkusze = ARKUSZE.get(nr)
    if not arkusze:
        return ""
    ile = len(arkusze)
    return "\n".join(
        arkusz(nr, tytul, wstep, kolumny, karty, i, ile, esc)
        for i, (tytul, wstep, katalog, kolumny, karty) in enumerate(arkusze, 1))


def ma_karty(nr):
    return nr in ARKUSZE
