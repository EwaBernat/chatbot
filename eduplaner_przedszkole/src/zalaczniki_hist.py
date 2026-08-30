# -*- coding: utf-8 -*-
"""Historyjki obrazkowe do konspektów B1-01 i C7-32.

Dwie opowieści w tym samym stylu ilustracji, w którym powstała historyjka
„Jak rośnie kwiatek" do konspektu C1-01 (`zalacznik_c1.py`): pastelowa paleta,
cienki brązowy kontur, ci sami bohaterowie na wszystkich pięciu scenach.
Sceny są rastrowe i wchodzą do dokumentu jako data-URI, więc bank i zeszyty
zostają samodzielnymi plikami.

Dlaczego osobny moduł, a nie trzeci `zalacznik_*.py`: karta A4, pasek odsłuchu
i gradacja poziomów są dla każdej historyjki takie same — różni się tylko
treść. Trzy prawie identyczne pliki rozjeżdżałyby się przy pierwszej poprawce
układu.

**Prefiksy są tu obowiązkowe.** W banku wszystkie historyjki siedzą w jednym
dokumencie, więc klasy scen (`.b1s1`) i identyfikatory nagrań (`b1au0`) muszą
się różnić między opowieściami. Bez prefiksu druga historyjka podmieniałaby
obrazki i dźwięki pierwszej.

Sekwencje dla poziomów wsparcia — tak samo jak w C1-01:
    Poziom III · 3 obrazki  — problem i rozwiązanie
    Poziom II  · 4 obrazki  — z przyczyną zdarzenia
    Poziom I   · 5 obrazków — pełny łuk narracyjny

Narracja: jej własny sklonowany głos (`jq4ZUryuBeDqmtkKtBZ4`, model
`eleven_v3`), rejestr zgodny z pamięcią projektu — ciepłe otwarcie, spokojne
rozwinięcie, `[gently, a little sad]` na scenie smutnej, uśmiech w domknięciu.
Tekst mówiony jest czystą prozą, bez wielokropków i sylabizowania.
"""

import base64
from pathlib import Path

_ASSETS = Path(__file__).resolve().parent.parent / "assets"


# ——— treść obu historyjek ————————————————————————————————————————————————
HISTORYJKI = {
    "b1": dict(
        konspekt="B1-01", nazwa_konspektu="Detektywi opowieści", wiek="5 lat",
        tytul="Zgubiony klucz",
        kadry="hist_b1", audio="audio_b1",
        wstep="Wytnij obrazki wzdłuż linii i rozsyp je na dywanie. Przeczytaj albo "
              "odtwórz opowiadanie, a potem poproś dziecko o ułożenie kolejności "
              "i opowiedzenie historii własnymi słowami.",
        polecenie="Ułóż obrazki po kolei i opowiedz, co się wydarzyło. Kto zgubił kluczyk?",
        sceny={
            1: "Miś ma kluczyk do swojej skrzynki",
            2: "Kluczyk wypada z kieszeni na trawę",
            3: "Skrzynka zamknięta — miś jest smutny",
            4: "Zajączek przynosi zgubiony kluczyk",
            5: "Skrzynka otwarta — miś dziękuje",
        },
        podpisy_p3={1: "Miś ma kluczyk",
                    3: "Kluczyk zginął — miś jest smutny",
                    5: "Kluczyk się znalazł — miś się cieszy"},
        podpisy_p2={1: "Miś ma kluczyk",
                    2: "Kluczyk wypada z kieszeni",
                    3: "Miś jest smutny",
                    5: "Miś otwiera skrzynkę"},
        czasy={0: 11.5, 1: 12.4, 2: 12.1, 3: 11.0, 4: 7.5, 5: 11.8, 6: 11.4},
    ),
    "c7": dict(
        konspekt="C7-32", nazwa_konspektu="Konsekwencje moich wyborów", wiek="6 lat",
        tytul="Wieża Zosi",
        kadry="hist_c7", audio="audio_c7",
        wstep="Wytnij obrazki wzdłuż linii i rozsyp je na dywanie. Po wysłuchaniu "
              "opowiadania dziecko układa kolejność i nazywa, co Kuba zrobił, co "
              "poczuła Zosia i jak to naprawił — trzy kroki schematu przeprosin.",
        polecenie="Ułóż obrazki po kolei i powiedz, co Kuba zrobił, co poczuła Zosia i jak to naprawił.",
        sceny={
            1: "Zosia i Kuba budują wieżę",
            2: "Kuba wyciąga klocek — wieża się rozsypuje",
            3: "Zosia płacze, Kuba spuszcza głowę",
            4: "Kuba mówi, co zrobił, i pyta, jak naprawić",
            5: "Budują wieżę razem jeszcze raz",
        },
        podpisy_p3={1: "Budują wieżę razem",
                    3: "Wieża się rozsypała — Zosia jest smutna",
                    5: "Budują ją jeszcze raz, razem"},
        podpisy_p2={1: "Budują wieżę razem",
                    2: "Wieża się rozsypuje",
                    3: "Zosia jest smutna",
                    5: "Naprawiają to razem"},
        czasy={0: 12.0, 1: 8.7, 2: 10.0, 3: 10.4, 4: 12.8, 5: 10.0, 6: 17.8},
    ),
}

# Pliki narracji: 0 to wprowadzenie, 1–5 sceny, 6 pytania otwarte na koniec.
PLIKI = {0: "naracja_00_wstep.mp3", 6: "naracja_06_pytania.mp3"}
PLIKI.update({n: f"naracja_{n:02d}.mp3" for n in range(1, 6)})

# Trzy sekwencje — te same numery scen w obu historyjkach.
SEKWENCJE = {"p3": (1, 3, 5), "p2": (1, 2, 3, 5), "p1": (1, 2, 3, 4, 5)}
POZIOMY = {"p3": "Poziom III", "p2": "Poziom II", "p1": "Poziom I"}
ZALACZNIKI = {"p3": "Z1", "p2": "Z2", "p1": "Z3"}


def _obraz(h, nr):
    dane = (_ASSETS / h["kadry"] / f"kadr_{nr:02d}.png").read_bytes()
    return f"data:image/png;base64,{base64.b64encode(dane).decode()}"


def _dzwiek(h, nr):
    dane = (_ASSETS / h["audio"] / PLIKI[nr]).read_bytes()
    return f"data:audio/mpeg;base64,{base64.b64encode(dane).decode()}"


def _style(pre, h):
    """Pięć scen osadzonych dokładnie raz, w klasach CSS.

    Ta sama scena wraca na trzech kartach; w atrybucie `src` trafiłaby do pliku
    trzykrotnie, a przy pięciu scenach to półtora megabajta na darmo.
    """
    regu = "\n".join(f".{pre}s{n}{{background-image:url({_obraz(h, n)})}}" for n in h["sceny"])
    return f"<style>{regu}</style>"


def _audio(pre, h):
    return "".join(f'<audio id="{pre}au{n}" preload="none" src="{_dzwiek(h, n)}"></audio>'
                   for n in PLIKI)


def _podpisy(h, poziom):
    if poziom == "p1":
        return h["sceny"]
    return h["podpisy_p3"] if poziom == "p3" else h["podpisy_p2"]


def _karta(pre, h, poziom):
    nry = SEKWENCJE[poziom]
    podpisy = _podpisy(h, poziom)
    n = len(nry)
    kol = 2 if n <= 4 else 3
    seq = ",".join([f"{pre}au0"] + [f"{pre}au{x}" for x in nry] + [f"{pre}au6"])
    minuty = round((h["czasy"][0] + sum(h["czasy"][x] for x in nry) + h["czasy"][6]) / 60 * 2) / 2
    czas = f"{minuty:g} min".replace(".", ",")
    kafle = []
    for i, x in enumerate(nry, 1):
        podpis = podpisy[x]
        kafle.append(f'''      <figure class="kafel">
        <span class="numer">{i}</span>
        <span class="obraz {pre}s{x}" role="img" aria-label="{podpis}"></span>
        <button type="button" class="au-btn" data-au="{pre}au{x}"
          aria-label="Posłuchaj: {podpis}"><span aria-hidden="true">▶</span> Posłuchaj</button>
        <figcaption>{podpis}</figcaption>
        <span class="linia-ciecia" aria-hidden="true"></span>
      </figure>''')
    return f'''<section class="zal" data-poziom="{poziom}">
  <header class="zal-head">
    <span class="mark" role="img" aria-label="Logo PCTP"></span>
    <div>
      <div class="zal-w">EduPlaner 2026</div>
      <div class="zal-s">Załącznik {ZALACZNIKI[poziom]} · konspekt {h["konspekt"]} · {h["nazwa_konspektu"]} · {h["wiek"]}</div>
    </div>
    <span class="zal-pill {poziom}">{POZIOMY[poziom]} · {n} obrazki</span>
  </header>
  <div class="zal-tytul">
    <span class="zal-kp">Pomoc dydaktyczna · historyjka obrazkowa</span>
    <h3>{h["tytul"]}</h3>
    <p>{h["wstep"]}</p>
  </div>
  <div class="au-pasek">
    <button type="button" class="au-all" data-au-seq="{seq}">
      <span aria-hidden="true">▶</span> Odtwórz całą historyjkę</button>
    <button type="button" class="au-stop">Zatrzymaj</button>
    <span class="au-info">narracja głosem nauczycielki · {czas}</span>
  </div>
  <div class="zal-siatka k{kol}">
{chr(10).join(kafle)}
  </div>
  <div class="zal-stopka">
    <span><b>Polecenie dla dziecka:</b> „{h["polecenie"]}”</span>
    <span class="mono">EduPlaner 2026 · PCTP · druk KC-3 · załącznik {ZALACZNIKI[poziom]}</span>
  </div>
</section>'''


def historyjka(pre):
    """Trzy karty A4 jednej historyjki — po jednej na poziom wsparcia."""
    h = HISTORYJKI[pre]
    return (_style(pre, h) + _audio(pre, h)
            + "".join(_karta(pre, h, p) for p in ("p3", "p2", "p1")))


# Konspekt → historyjka. Build sięga tu jednym wywołaniem, zamiast trzymać
# łańcuch warunków przy składaniu sekcji VII.
DLA_KONSPEKTU = {"B1-01": "b1", "C7-32": "c7"}


def zalaczniki_dla(nr):
    """Historyjka konspektu `nr` albo pusty ciąg, gdy konspekt jej nie ma."""
    pre = DLA_KONSPEKTU.get(nr)
    return historyjka(pre) if pre else ""
