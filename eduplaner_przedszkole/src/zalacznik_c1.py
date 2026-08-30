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
_AUDIO = Path(__file__).resolve().parent.parent / "assets" / "audio_c1"

# Narracja nagrana głosem nauczycielki (klon PL). Klucz 0 to wprowadzenie,
# 1-5 to sceny, 6 to zakończenie z pytaniami otwartymi do dziecka.
NARRACJA = {
    0: ("naracja_00_wstep.mp3", "Usiądź sobie wygodnie… Opowiem ci historię o pewnej "
        "dziewczynce i o malutkim nasionku. A kiedy skończę — ułożysz obrazki po kolei "
        "i opowiesz mi ją swoimi słowami. Dobrze?"),
    1: ("naracja_01.mp3", "Ola dostała malutkie, brązowe nasionko. Wsypała do doniczki "
        "ziemię i ostrożniutko włożyła nasionko do środka. Przykryła je ziemią i "
        "szepnęła: rośnij."),
    2: ("naracja_02.mp3", "Minęło kilka dni. Pewnego ranka Ola zajrzała do doniczki — "
        "i aż pisnęła z radości! Z ziemi wyrósł mały, zielonutki pęd. A na nim dwa "
        "malutkie listki."),
    3: ("naracja_03.mp3", "Ale potem Ola bawiła się cały dzień i zupełnie zapomniała "
        "podlać roślinkę. Następnego ranka listki zwiesiły się smutno w dół. Ziemia "
        "była całkiem sucha. I Oli zrobiło się bardzo przykro."),
    4: ("naracja_04.mp3", "Ale Ola się nie poddała! Wzięła konewkę, nalała wody i "
        "powolutku podlała roślinkę. A potem przesunęła doniczkę tam, gdzie najmocniej "
        "świeciło słonko."),
    5: ("naracja_05.mp3", "I wiesz co? Już następnego dnia roślinka podniosła listki "
        "do góry. A po tygodniu rozwinął się na niej duży, różowy kwiat! Ola skakała "
        "z radości, a nad kwiatkiem fruwał kolorowy motyl."),
    6: ("naracja_06_pytania.mp3", "A teraz twoja kolej. Ułóż obrazki po kolei i opowiedz "
        "mi, co się wydarzyło. Powiedz — co się stało, kiedy Ola zapomniała podlać "
        "roślinkę? I jak myślisz… dlaczego roślinka znowu odżyła?"),
}


def _obraz(nr):
    """Zwraca scenę nr jako data-URI (PNG, 640 px)."""
    dane = base64.b64encode((_KADRY / f"kadr_{nr:02d}.png").read_bytes()).decode()
    return f"data:image/png;base64,{dane}"


def _dzwiek(nr):
    """Zwraca ścieżkę narracji nr jako data-URI (MP3)."""
    dane = base64.b64encode((_AUDIO / NARRACJA[nr][0]).read_bytes()).decode()
    return f"data:audio/mpeg;base64,{dane}"


def audio_scen():
    """Siedem elementów <audio> — po jednym na ścieżkę, wspólnych dla trzech kart."""
    return "".join(f'<audio id="au{n}" preload="none" src="{_dzwiek(n)}"></audio>'
                   for n in NARRACJA)


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

# Czas trwania nagrań w sekundach (z generatora mowy) — do etykiety na pasku.
CZASY = {0: 16.4, 1: 18.2, 2: 14.0, 3: 20.6, 4: 13.7, 5: 15.1, 6: 17.1}

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
    # Sekwencja odsłuchu: wprowadzenie, sceny tej karty, pytania na koniec.
    seq = ",".join(["au0"] + [f"au{nr}" for _, nr in obrazki] + ["au6"])
    minuty = round((CZASY[0] + sum(CZASY[nr] for _, nr in obrazki) + CZASY[6]) / 60 * 2) / 2
    czas = f"{minuty:g} min".replace(".", ",")
    kafle = []
    for i, (podpis, nr) in enumerate(obrazki, 1):
        kafle.append(f'''      <figure class="kafel">
        <span class="numer">{i}</span>
        <span class="obraz sc{nr}" role="img" aria-label="{podpis}"></span>
        <button type="button" class="au-btn" data-au="au{nr}"
          aria-label="Posłuchaj: {podpis}"><span aria-hidden="true">▶</span> Posłuchaj</button>
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
    <span><b>Polecenie dla dziecka:</b> „Ułóż obrazki po kolei i opowiedz, co się wydarzyło.”</span>
    <span class="mono">EduPlaner 2026 · PCTP · druk KC-3 · załącznik {nr_zal}</span>
  </div>
</section>'''


def zalaczniki_c1():
    return (style_scen() + audio_scen() +
            karta_a4("Poziom III", "p3", historyjka_p3(), "Z1") +
            karta_a4("Poziom II", "p2", historyjka_p2(), "Z2") +
            karta_a4("Poziom I", "p1", historyjka_p1(), "Z3"))
