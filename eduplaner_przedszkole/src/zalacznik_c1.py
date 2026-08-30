# -*- coding: utf-8 -*-
"""Załączniki do konspektu C1-01 „Warsztat historyjek" (wersja C · 6 lat).

Historyjka obrazkowa „Jak rośnie kwiatek" — pięć scen w jednym, spójnym stylu
ilustracji książeczkowej (pastelowa paleta „cukierkowa", ta sama bohaterka na
każdym obrazku). Sceny są ilustracjami rastrowymi osadzonymi w pliku HTML jako
data-URI, dzięki czemu bank celów pozostaje jednym samodzielnym dokumentem.

Sekwencje dla poszczególnych poziomów wsparcia:
    Poziom III · 3 obrazki  — sadzę · kiełkuje · zakwitło
    Poziom II  · 4 obrazki  — + podlewanie
    Poziom I   · 5 obrazków — pełny łuk narracyjny z problemem i rozwiązaniem
"""

import base64
from pathlib import Path

_KADRY = Path(__file__).resolve().parent.parent / "assets" / "hist_c1"


def _obraz(nr):
    """Zwraca scenę nr jako data-URI (PNG, 640 px)."""
    dane = base64.b64encode((_KADRY / f"kadr_{nr:02d}.png").read_bytes()).decode()
    return f"data:image/png;base64,{dane}"


def style_scen():
    """Arkusz z pięcioma scenami — każda osadzona dokładnie raz.

    Sceny powtarzają się na trzech kartach (Z1/Z2/Z3), więc trzymamy je
    w klasach CSS zamiast w atrybutach src — inaczej ten sam obrazek trafiłby
    do pliku nawet cztery razy.
    """
    regu = "\n".join(f'.sc{n}{{background-image:url({_obraz(n)})}}' for n in SCENY)
    return f"<style>{regu}</style>"


# Sceny — numer pliku, podpis roboczy dla nauczyciela
SCENY = {
    1: "Zasadziłam nasionko w doniczce",
    2: "Wyrósł mały, zielony pęd",
    3: "Zapomniałam podlać — roślinka zwiędła",
    4: "Podlewam ją i stawiam w słońcu",
    5: "Roślinka odżyła i zakwitła",
}

PODPISY_P3 = {1: "Sadzę nasionko", 2: "Rośnie zielony pęd", 5: "Wyrósł piękny kwiat"}
PODPISY_P2 = {1: "Sadzę nasionko", 2: "Wyrósł mały pęd",
              4: "Podlewam roślinkę", 5: "Zakwitł kwiat — cieszę się"}


def historyjka_p3():
    """Poziom III — 3 obrazki, prosty ciąg przyczynowo-skutkowy."""
    return [(PODPISY_P3[n], n) for n in (1, 2, 5)]


def historyjka_p2():
    """Poziom II — 4 obrazki, z czynnością opiekuńczą pośrodku."""
    return [(PODPISY_P2[n], n) for n in (1, 2, 4, 5)]


def historyjka_p1():
    """Poziom I — 5 obrazków, pełna narracja: problem → działanie → rozwiązanie."""
    return [(SCENY[n], n) for n in (1, 2, 3, 4, 5)]


# ---------------------------------------------------------------- karty A4
def karta_a4(poziom, kod_poziomu, obrazki, nr_zal):
    """Jedna strona A4 z historyjką do wycięcia (styl cukierkowy, marka EduPlaner)."""
    n = len(obrazki)
    kol = 2 if n <= 4 else 3
    kafle = []
    for i, (podpis, nr) in enumerate(obrazki, 1):
        kafle.append(f'''      <figure class="kafel">
        <span class="numer">{i}</span>
        <span class="obraz sc{nr}" role="img" aria-label="{podpis}"></span>
        <figcaption>{podpis}</figcaption>
        <span class="linia-ciecia" aria-hidden="true"></span>
      </figure>''')
    return f'''<section class="zal" data-poziom="{kod_poziomu}">
  <header class="zal-head">
    <span class="mark" role="img" aria-label="Logo PCTP"></span>
    <div>
      <div class="zal-w">EduPlaner 2026</div>
      <div class="zal-s">Załącznik {nr_zal} · konspekt C1-01 · Warsztat historyjek · 6 lat</div>
    </div>
    <span class="zal-pill {kod_poziomu}">{poziom} · {n} obrazki</span>
  </header>
  <div class="zal-tytul">
    <span class="zal-kp">Pomoc dydaktyczna · historyjka obrazkowa</span>
    <h3>Jak rośnie kwiatek</h3>
    <p>Wytnij obrazki wzdłuż linii, rozsyp je na dywanie i poproś dziecko o ułożenie kolejności.
    Podpisy zostaw przy obrazkach albo odetnij — zależnie od tego, czy dziecko już czyta.</p>
  </div>
  <div class="zal-siatka k{kol}">
{chr(10).join(kafle)}
  </div>
  <div class="zal-stopka">
    <span><b>Polecenie dla dziecka:</b> „Ułóż obrazki po kolei i opowiedz, co się wydarzyło.”</span>
    <span class="mono">EduPlaner 2026 · PCTP · druk KC-3 · załącznik {nr_zal}</span>
  </div>
</section>'''


def zalaczniki_c1():
    return (style_scen() +
            karta_a4("Poziom III", "p3", historyjka_p3(), "Z1") +
            karta_a4("Poziom II", "p2", historyjka_p2(), "Z2") +
            karta_a4("Poziom I", "p1", historyjka_p1(), "Z3"))
