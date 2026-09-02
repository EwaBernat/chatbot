#!/usr/bin/env python3
"""Składa animowaną próbkę filmu: plansze budują się w rytm pauz w narracji.

Zasada: nie animujemy „na oko". Z nagrania wyciągamy pauzy (`silencedetect`),
a punkty, w których na planszy pojawia się kolejny element, są wpisane jako
sekundy odczytane z tej listy. Dzięki temu obraz zmienia się między zdaniami,
a nie w ich środku.

Kolejne stany planszy powstają przez wstrzyknięcie CSS do gotowego pliku HTML
(`visibility:hidden` / `opacity`), więc nie ma drugiej kopii treści do
utrzymywania — plansza pozostaje jednym źródłem prawdy.

    python3 zbuduj_animacje.py <katalog_z_mp3> [-o probka.mp4]

Katalog musi zawierać s1.mp3, s2.mp3, s3.mp3 (narracja trzech segmentów).
Podgląd pauz w nagraniu:
    ffmpeg -i s1.mp3 -af silencedetect=noise=-32dB:d=0.28 -f null /dev/null
"""
from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys

KAT = pathlib.Path(__file__).parent
PLANSZE = KAT / "plansze"
CHROM = "/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell"
PRZEJSCIE = 0.30      # długość przenikania między stanami planszy
PRZERWA = 0.65        # cisza między segmentami

def ukryj(*selektory: str) -> str:
    return "".join(f"{s}{{visibility:hidden}}" for s in selektory) if selektory else ""

def podswietl(nr: int | None) -> str:
    """Przygasza wszystkie karty obszarów; podaną (1-9) zostawia w pełni widoczną."""
    css = ".o{opacity:.15;transition:none}"
    return css if nr is None else css + f".obszary .o:nth-child({nr}){{opacity:1}}"

# Segment = (nagranie, plansza, [(sekunda, css_stanu)])
# Sekundy pochodzą z silencedetect — patrz docstring.
SEGMENTY = [
 ("s1.mp3", "00_tytul.html", [
   (0.00,  ukryj(".tyt-box.zle", ".tyt-strzalka", ".tyt-box.ok", ".tyt-chipy", ".tyt-aut")),
   (0.80,  ukryj(".tyt-box.zle .tyt-box-uw", ".tyt-strzalka", ".tyt-box.ok", ".tyt-chipy", ".tyt-aut")),
   (9.49,  ukryj(".tyt-strzalka", ".tyt-box.ok", ".tyt-chipy", ".tyt-aut")),
   (22.39, ukryj(".tyt-box.ok", ".tyt-chipy", ".tyt-aut")),
   (22.95, ukryj(".tyt-ptaszki", ".tyt-chipy", ".tyt-aut")),
   (33.14, ukryj(".tyt-chipy", ".tyt-aut")),
   (36.83, ukryj()),
 ]),
 ("s2.mp3", "04_formula_zdania.html", [
   (0.00,  ukryj(".formularz > div:nth-child(n+2)", ".prawa")),
   (6.50,  ukryj(".formularz > div:nth-child(n+3)", ".prawa")),
   (7.62,  ukryj(".formularz > div:nth-child(n+4)", ".prawa")),
   (9.44,  ukryj(".formularz > div:nth-child(n+5)", ".prawa")),
   (10.72, ukryj(".formularz > div:nth-child(n+6)", ".prawa")),
   (14.46, ukryj(".formularz > div:nth-child(n+7)", ".prawa")),
   (15.71, ukryj(".formularz > div:nth-child(n+8)", ".prawa")),
   (17.56, ukryj(".formularz > div:nth-child(n+9)", ".prawa")),
   (22.20, ukryj(".prawa .pom-blok", ".prawa .zrodlo")),
   (48.87, ukryj()),
 ]),
 ("s3.mp3", "07_dziewiec_obszarow.html", [
   (0.00,  podswietl(None)),
   (6.76,  podswietl(1)),   # obszar społeczny
   (18.68, podswietl(9)),   # obszar ruchowy
   (27.02, podswietl(2)),   # obszar osobisty
   (39.82, ""),             # wszystkie w pełni
 ]),
]

def trwanie(plik: pathlib.Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(plik)], check=True, capture_output=True, text=True)
    return float(out.stdout.strip())

def zrzut(html: pathlib.Path, css: str, wyjscie: pathlib.Path) -> None:
    tresc = html.read_text(encoding="utf-8")
    znacznik = f'<style id="stan-animacji">{css}</style></head>'
    tresc = tresc.replace("</head>", znacznik, 1)
    # Plik tymczasowy musi lezec OBOK planszy: odwolanie do wspolne.css jest wzgledne,
    # wiec zrzut z innego katalogu wyszedlby bez stylow.
    tymczas = html.with_name(f".stan-{wyjscie.stem}.html")
    tymczas.write_text(tresc, encoding="utf-8")
    subprocess.run([CHROM, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--window-size=1920,1080", f"--screenshot={wyjscie}", f"file://{tymczas.resolve()}"],
                   check=True, capture_output=True)
    tymczas.unlink()

def zbuduj_segment(nr: int, audio: pathlib.Path, html: pathlib.Path,
                   stany: list[tuple[float, str]], roboczy: pathlib.Path) -> pathlib.Path:
    dlugosc = trwanie(audio) + PRZERWA
    klatki, wejscia, filtry = [], [], []
    for i, (sekunda, css) in enumerate(stany):
        png = roboczy / f"seg{nr}_stan{i}.png"
        zrzut(html, css, png)
        nastepna = stany[i + 1][0] if i + 1 < len(stany) else dlugosc
        d = (nastepna - sekunda) + (PRZEJSCIE if i + 1 < len(stany) else 0.0)
        klatki.append((png, round(d, 3)))

    for png, d in klatki:
        wejscia += ["-loop", "1", "-t", str(d), "-i", str(png)]
    wejscia += ["-i", str(audio)]

    biezacy, przesuniecie = "[0:v]", 0.0
    for i in range(1, len(klatki)):
        przesuniecie = (przesuniecie + klatki[i - 1][1] - PRZEJSCIE) if i > 1 else (klatki[0][1] - PRZEJSCIE)
        etykieta = f"[x{i}]"
        filtry.append(f"{biezacy}[{i}:v]xfade=transition=fade:duration={PRZEJSCIE}:"
                      f"offset={round(przesuniecie, 3)}{etykieta}")
        biezacy = etykieta
    filtry.append(f"{biezacy}zoompan=z='min(1.0+0.00004*on,1.035)':d=1:"
                  f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps=30,"
                  f"fade=t=in:st=0:d=0.5,format=yuv420p[v]")
    filtry.append(f"[{len(klatki)}:a]adelay=120|120,apad[a]")

    wynik = roboczy / f"segment{nr}.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", *wejscia,
                    "-filter_complex", ";".join(filtry), "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-r", "30", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "1",
                    "-t", str(round(dlugosc, 3)), str(wynik)], check=True)
    print(f"segment {nr}: {len(klatki)} stanów, {dlugosc:.1f} s")
    return wynik

def main() -> int:
    ap = argparse.ArgumentParser(description="Animowana próbka filmu z gotowych plansz i narracji.")
    ap.add_argument("katalog", type=pathlib.Path, help="katalog z s1.mp3, s2.mp3, s3.mp3")
    ap.add_argument("-o", "--output", type=pathlib.Path, default=pathlib.Path("probka_animowana.mp4"))
    a = ap.parse_args()

    roboczy = a.katalog / "robocze"
    roboczy.mkdir(exist_ok=True)
    czesci = []
    for nr, (audio, plansza, stany) in enumerate(SEGMENTY, start=1):
        sciezka_audio = a.katalog / audio
        if not sciezka_audio.exists():
            print(f"Brak nagrania: {sciezka_audio}", file=sys.stderr)
            return 1
        czesci.append(zbuduj_segment(nr, sciezka_audio, PLANSZE / plansza, stany, roboczy))

    lista = roboczy / "lista.txt"
    lista.write_text("".join(f"file '{p.resolve()}'\n" for p in czesci), encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lista), "-c", "copy", str(a.output)], check=True)
    print(f"\nGotowe: {a.output} ({trwanie(a.output):.1f} s)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
