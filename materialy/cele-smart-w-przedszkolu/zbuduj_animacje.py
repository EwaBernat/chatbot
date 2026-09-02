#!/usr/bin/env python3
"""Składa film z gotowych plansz: ujęcia, najazdy kamery i narracja bez pośpiechu.

Trzy zasady, na których to stoi:

1. **Obraz nadąża za słowem.** Nagranie tnie się na ujęcia dokładnie tam, gdzie
   kończy się akapit narracji, a między ujęciami wstawiana jest cisza (`PRZERWA`).
   Dzięki temu żadne zdanie nie zaczyna się, zanim obraz nie usiądzie.
2. **Kamera pokazuje to, o czym mowa.** Ujęcie może wskazać selektor CSS —
   pozycję elementu mierzy przeglądarka, a kadr dojeżdża do niego płynnie.
3. **Jedno źródło treści.** Stany planszy powstają przez wstrzyknięcie CSS do
   gotowego HTML-a; nie ma drugiej kopii tekstu do utrzymywania.

    python3 zbuduj_animacje.py <katalog_z_mp3> -o film.mp4
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess
import sys

KAT = pathlib.Path(__file__).parent
PLANSZE = KAT / "plansze"
CHROM = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"

SZER, WYS = 1920, 1080
SKALA = 2                 # renderujemy kadr z zapasem, żeby najazd nie miękł
PRZEJSCIE = 0.35          # przenikanie między ujęciami
PRZERWA = 0.55            # cisza doklejana na końcu każdego ujęcia
NAJAZD = 1.5              # ile trwa dojazd kamery do omawianego elementu
MARGINES = 46             # oddech wokół elementu, w pikselach planszy
MIN_SZER = 980            # nie przybliżamy bardziej — tekst zaczyna się rozmywać


def ukryj(*selektory: str) -> str:
    return "".join(f"{s}{{visibility:hidden}}" for s in selektory)


def przygas(nr: int | None) -> str:
    css = ".o{opacity:.15}"
    return css if nr is None else css + f".obszary .o:nth-child({nr}){{opacity:1}}"


# ── film: segment = nagranie + plansza + ujęcia ─────────────────────────────
# „od" to sekunda w nagraniu, w której ujęcie się zaczyna (koniec poprzedniego
# akapitu). Podgląd pauz: ffmpeg -i s1.mp3 -af silencedetect=noise=-32dB:d=0.28 -f null -
SEGMENTY = [
 {"audio": "s1.mp3", "plansza": "00_tytul.html", "ujecia": [
   (0.00,  ukryj(".tyt-box.zle", ".tyt-strzalka", ".tyt-box.ok", ".tyt-chipy", ".tyt-aut"), None),
   (0.80,  ukryj(".tyt-box.zle .tyt-box-uw", ".tyt-strzalka", ".tyt-box.ok", ".tyt-chipy", ".tyt-aut"), ".tyt-box.zle"),
   (9.49,  ukryj(".tyt-strzalka", ".tyt-box.ok", ".tyt-chipy", ".tyt-aut"), ".tyt-box.zle"),
   (22.39, ukryj(".tyt-box.ok", ".tyt-chipy", ".tyt-aut"), None),
   (22.95, ukryj(".tyt-ptaszki", ".tyt-chipy", ".tyt-aut"), ".tyt-box.ok"),
   (33.14, ukryj(".tyt-chipy", ".tyt-aut"), ".tyt-box.ok"),
   (36.83, "", None),
 ]},
 {"audio": "s2.mp3", "plansza": "04_formula_zdania.html", "ujecia": [
   (0.00,  ukryj(".formularz > div:nth-child(n+2)", ".prawa"), None),
   (6.50,  ukryj(".formularz > div:nth-child(n+3)", ".prawa"), ".formularz"),
   (7.62,  ukryj(".formularz > div:nth-child(n+4)", ".prawa"), ".formularz"),
   (9.44,  ukryj(".formularz > div:nth-child(n+5)", ".prawa"), ".formularz"),
   (10.72, ukryj(".formularz > div:nth-child(n+6)", ".prawa"), ".formularz"),
   (14.46, ukryj(".formularz > div:nth-child(n+7)", ".prawa"), ".formularz"),
   (15.71, ukryj(".formularz > div:nth-child(n+8)", ".prawa"), ".formularz"),
   (17.56, ukryj(".formularz > div:nth-child(n+9)", ".prawa"), ".formularz"),
   (22.20, ukryj(".prawa .pom-blok", ".prawa .zrodlo"), ".prawa .ok-blok"),
   (48.87, "", None),
 ]},
 {"audio": "s3.mp3", "plansza": "07_dziewiec_obszarow.html", "ujecia": [
   (0.00,  przygas(None), None),
   (6.76,  przygas(1), ".obszary .o:nth-child(1)"),
   (18.68, przygas(9), ".obszary .o:nth-child(9)"),
   (27.02, przygas(2), ".obszary .o:nth-child(2)"),
   (39.82, "", None),
 ]},
 {"audio": "s4.mp3", "plansza": "10b_czy_obowiazkowe.html", "ujecia": [
   (None, "", None),
   (None, "", ".zle-blok"),
   (None, "", ".ok-blok"),
   (None, "", ".pom-blok"),
 ]},
 {"audio": "s5.mp3", "plansza": "10c_stare_nowe.html", "ujecia": [
   (None, "", None),
   (None, "", "#porownanie .stare"),
   (None, "", "#porownanie .nowe"),
   (None, "", "#bezzmian"),
   (None, "", ".ostrzezenie"),
 ]},
 {"audio": "s6.mp3", "plansza": "10_podstawa_prawna.html", "ujecia": [
   (None, "", None),
   (None, "", "table.akty tr:nth-child(3)"),
   (None, "", "table.akty tr:nth-child(4)"),
   (None, "", ".pom-blok"),
 ]},
]


# ── narzędzia ──────────────────────────────────────────────────────────────

def przebieg(polecenie: list[str]) -> subprocess.CompletedProcess:
    wynik = subprocess.run(polecenie, capture_output=True, text=True)
    if wynik.returncode != 0:
        raise SystemExit(f"Polecenie zakonczylo sie bledem {wynik.returncode}:\n"
                         f"{wynik.stderr.strip()[-2000:]}")
    return wynik


def trwanie(plik: pathlib.Path) -> float:
    out = przebieg(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                    "-of", "csv=p=0", str(plik)])
    return float(out.stdout.strip())


def ciszy(plik: pathlib.Path, prog_db: int = -32, min_dl: float = 0.28) -> list[tuple[float, float]]:
    """Zwraca listę (koniec_ciszy, długość_ciszy) — kandydatów na granice ujęć."""
    proc = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(plik),
                           "-af", f"silencedetect=noise={prog_db}dB:d={min_dl}",
                           "-f", "null", "/dev/null"], capture_output=True, text=True)
    konce = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", proc.stderr)]
    dlugosci = [float(x) for x in re.findall(r"silence_duration: ([0-9.]+)", proc.stderr)]
    return list(zip(konce, dlugosci))


def granice_akapitow(plik: pathlib.Path, ile: int) -> list[float]:
    """Najdłuższe przerwy w nagraniu = granice akapitów, czyli początki ujęć."""
    kandydaci = ciszy(plik)
    if len(kandydaci) < ile:
        raise SystemExit(f"{plik.name}: znalazłem {len(kandydaci)} pauz, a potrzeba {ile}.")
    najdluzsze = sorted(kandydaci, key=lambda k: -k[1])[:ile]
    return [0.0] + sorted(k[0] for k in najdluzsze)


def zmierz(html: pathlib.Path, selektory: list[str]) -> dict[str, list[float]]:
    """Pyta przeglądarkę o położenie elementów — nie zgadujemy współrzędnych."""
    if not selektory:
        return {}
    skrypt = ("<script>window.addEventListener('load',function(){var o={};var s="
              + json.dumps(selektory)
              + ";s.forEach(function(q){var e=document.querySelector(q);if(e){var r="
              + "e.getBoundingClientRect();o[q]=[r.x,r.y,r.width,r.height];}});"
              + "var d=document.createElement('div');d.id='RECTS';"
              + "d.textContent=JSON.stringify(o);document.body.appendChild(d);});</script></body>")
    tymczas = html.with_name(f".pomiar-{html.stem}.html")
    tymczas.write_text(html.read_text(encoding="utf-8").replace("</body>", skrypt, 1), encoding="utf-8")
    try:
        proc = subprocess.run([CHROM, "--headless", "--disable-gpu", "--no-sandbox",
                               f"--window-size={SZER},{WYS}", "--virtual-time-budget=3000",
                               "--dump-dom", f"file://{tymczas.resolve()}"],
                              capture_output=True, text=True)
        m = re.search(r'id="RECTS">(.*?)</div>', proc.stdout, re.S)
        if not m:
            raise SystemExit(f"Nie udało się zmierzyć elementów w {html.name}.")
        return json.loads(m.group(1))
    finally:
        tymczas.unlink(missing_ok=True)


def kadr(prostokat: list[float] | None) -> tuple[float, float, float, float]:
    """Zamienia prostokąt elementu na kadr 16:9 z marginesem, zmieszczony w planszy."""
    if prostokat is None:
        return 0.0, 0.0, float(SZER), float(WYS)
    x, y, w, h = prostokat
    x, y, w, h = x - MARGINES, y - MARGINES, w + 2 * MARGINES, h + 2 * MARGINES
    szer = max(w, h * SZER / WYS, MIN_SZER)
    wys = szer * WYS / SZER
    sx = x + w / 2 - szer / 2
    sy = y + h / 2 - wys / 2
    szer, wys = min(szer, SZER), min(wys, WYS)
    sx = min(max(sx, 0.0), SZER - szer)
    sy = min(max(sy, 0.0), WYS - wys)
    return sx, sy, szer, wys


def zrzut(html: pathlib.Path, css: str, wyjscie: pathlib.Path) -> None:
    tresc = html.read_text(encoding="utf-8").replace(
        "</head>", f'<style id="stan">{css}</style></head>', 1)
    # Plik tymczasowy musi leżeć obok planszy — wspolne.css jest wskazane względnie.
    tymczas = html.with_name(f".stan-{wyjscie.stem}.html")
    tymczas.write_text(tresc, encoding="utf-8")
    try:
        przebieg([CHROM, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                  f"--window-size={SZER},{WYS}", f"--screenshot={wyjscie}",
                  f"file://{tymczas.resolve()}"])
    finally:
        tymczas.unlink(missing_ok=True)


# `crop` przelicza szerokość i wysokość tylko raz, przy konfiguracji filtra,
# więc płynny najazd robimy przez `zoompan` — tam zmienna `on` (numer klatki)
# jest przeliczana dla każdej klatki z osobna.
KLATKI = 30


def dojazd(od: float, do: float) -> str:
    """Płynny dojazd (bez szarpnięcia na starcie i na końcu) w NAJAZD sekund."""
    postep = f"(1-cos(PI*min(on/{NAJAZD * KLATKI:.0f},1)))/2"
    return f"({od:.2f}+({do:.2f}-{od:.2f})*{postep})"


def filtr_kamery(od: tuple, do: tuple) -> str:
    """zoompan: okno o szerokości `iw/z` w punkcie (x, y), przeskalowane do 1920x1080."""
    szerokosc = dojazd(od[2] * SKALA, do[2] * SKALA)
    return (f"zoompan=z='{SZER * SKALA}/{szerokosc}'"
            f":x='{dojazd(od[0] * SKALA, do[0] * SKALA)}'"
            f":y='{dojazd(od[1] * SKALA, do[1] * SKALA)}'"
            f":d=1:s={SZER}x{WYS}:fps={KLATKI}")


def zbuduj_segment(nr: int, segment: dict, katalog: pathlib.Path,
                   roboczy: pathlib.Path) -> pathlib.Path:
    audio = katalog / segment["audio"]
    html = PLANSZE / segment["plansza"]
    ujecia = segment["ujecia"]

    starty = [u[0] for u in ujecia]
    if any(s is None for s in starty):
        starty = granice_akapitow(audio, len(ujecia) - 1)
    dlugosc_audio = trwanie(audio)
    granice = starty + [dlugosc_audio]

    prostokaty = zmierz(html, sorted({u[2] for u in ujecia if u[2]}))

    wejscia: list[str] = []
    filtry: list[str] = []
    poprzedni = kadr(None)
    dlugosci: list[float] = []

    for i, (_, css, cel) in enumerate(ujecia):
        png = roboczy / f"seg{nr}_uj{i}.png"
        zrzut(html, css, png)
        biezacy = kadr(prostokaty.get(cel) if cel else None)
        d = round(granice[i + 1] - granice[i] + PRZERWA + (PRZEJSCIE if i + 1 < len(ujecia) else 0.0), 3)
        dlugosci.append(d)
        wejscia += ["-loop", "1", "-framerate", str(KLATKI), "-t", str(d), "-i", str(png)]
        filtry.append(f"[{i}:v]scale={SZER * SKALA}:{WYS * SKALA}:flags=lanczos,"
                      f"{filtr_kamery(poprzedni, biezacy)},setsar=1[v{i}]")
        poprzedni = biezacy

    biezacy_slad, przesuniecie = "[v0]", 0.0
    for i in range(1, len(ujecia)):
        przesuniecie += dlugosci[i - 1] - PRZEJSCIE
        etykieta = f"[x{i}]"
        filtry.append(f"{biezacy_slad}[v{i}]xfade=transition=fade:duration={PRZEJSCIE}:"
                      f"offset={round(przesuniecie, 3)}{etykieta}")
        biezacy_slad = etykieta
    filtry.append(f"{biezacy_slad}fade=t=in:st=0:d=0.5,format=yuv420p[v]")

    n = len(ujecia)
    for i in range(n):
        filtry.append(f"[{n}:a]atrim=start={granice[i]}:end={granice[i + 1]},"
                      f"asetpts=PTS-STARTPTS,apad=pad_dur={PRZERWA + 0.05}[a{i}]")
    filtry.append("".join(f"[a{i}]" for i in range(n)) + f"concat=n={n}:v=0:a=1[a]")

    wejscia += ["-i", str(audio)]
    wynik = roboczy / f"segment{nr}.mp4"
    przebieg(["ffmpeg", "-y", "-v", "error", *wejscia, "-filter_complex", ";".join(filtry),
              "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
              "-pix_fmt", "yuv420p", "-r", str(KLATKI), "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
              "-ac", "1", "-shortest", str(wynik)])
    print(f"segment {nr} ({segment['plansza']}): {n} ujęć, {trwanie(wynik):.1f} s")
    return wynik


def main() -> int:
    ap = argparse.ArgumentParser(description="Film szkoleniowy z plansz, najazdów i narracji.")
    ap.add_argument("katalog", type=pathlib.Path, help="katalog z nagraniami s1.mp3 … s6.mp3")
    ap.add_argument("-o", "--output", type=pathlib.Path, default=pathlib.Path("film.mp4"))
    ap.add_argument("--segmenty", help="np. 4,5,6 — zbuduj tylko wybrane")
    ap.add_argument("--lekka-kopia", action="store_true",
                    help="obok filmu zapisz mocno skompresowaną kopię do wysłania "
                         "(plansze kompresują się świetnie, więc jakość prawie nie cierpi)")
    a = ap.parse_args()

    wybrane = {int(x) for x in a.segmenty.split(",")} if a.segmenty else None
    roboczy = a.katalog / "robocze"
    roboczy.mkdir(exist_ok=True)

    czesci = []
    for nr, segment in enumerate(SEGMENTY, start=1):
        if wybrane and nr not in wybrane:
            continue
        if not (a.katalog / segment["audio"]).exists():
            print(f"Pomijam segment {nr}: brak {segment['audio']}", file=sys.stderr)
            continue
        czesci.append(zbuduj_segment(nr, segment, a.katalog, roboczy))

    if not czesci:
        print("Nie zbudowano żadnego segmentu.", file=sys.stderr)
        return 1
    lista = roboczy / "lista.txt"
    lista.write_text("".join(f"file '{p.resolve()}'\n" for p in czesci), encoding="utf-8")
    przebieg(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
              "-i", str(lista), "-c", "copy", str(a.output)])
    print(f"\nGotowe: {a.output} ({trwanie(a.output):.1f} s, "
          f"{a.output.stat().st_size / 1_048_576:.1f} MB)")

    if a.lekka_kopia:
        lekka = a.output.with_name(a.output.stem + "_lekki.mp4")
        przebieg(["ffmpeg", "-y", "-v", "error", "-i", str(a.output),
                  "-c:v", "libx264", "-preset", "slow", "-crf", "30", "-tune", "stillimage",
                  "-pix_fmt", "yuv420p", "-movflags", "+faststart",
                  "-c:a", "aac", "-b:a", "96k", "-ac", "1", str(lekka)])
        print(f"Lekka kopia: {lekka} ({lekka.stat().st_size / 1_048_576:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
