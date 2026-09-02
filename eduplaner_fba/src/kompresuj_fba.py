# -*- coding: utf-8 -*-
"""Kompresja mediów FBA: PNG → k_<kod>.jpg, MP3 → 40 kbps mono.

Ilustracje wchodzą do dokumentu jako data-URI, więc waga ma znaczenie:
surowy PNG z modelu ma ponad megabajt, a po skompresowaniu do JPG 900 px
zostaje z tego około 90 kB przy tej samej jakości na ekranie i w druku A4.

Skrypt **pomija pliki już przetworzone** — po poprawieniu obrazka trzeba
skasować stary `k_*.jpg`, inaczej dokument dalej pokaże poprzednią wersję.
Ta sama pułapka kosztowała już jedną rundę w banku KPOF.

    python3 src/kompresuj_fba.py [--od-nowa]
"""

import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image

# ffmpeg nie jest w obrazie jako polecenie systemowe — bierzemy binarkę
# z `imageio_ffmpeg`, tak samo jak robi to bank KPOF.
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

KOR = Path(__file__).resolve().parent.parent
OBRAZY = KOR / "assets" / "pomoce_fba"
AUDIO = KOR / "assets" / "audio_fba"
SZEROKOSC = 900


def obrazy(od_nowa=False):
    zrobione, pominiete = 0, 0
    for png in sorted(OBRAZY.glob("*.png")):
        cel = png.with_name(f"k_{png.stem}.jpg")
        if cel.exists() and not od_nowa:
            pominiete += 1
            continue
        im = Image.open(png).convert("RGB")
        if im.width > SZEROKOSC:
            im = im.resize((SZEROKOSC, round(im.height * SZEROKOSC / im.width)), Image.LANCZOS)
        im.save(cel, "JPEG", quality=84, optimize=True, progressive=True)
        zrobione += 1
    return zrobione, pominiete


def nagrania(od_nowa=False):
    """MP3 z ElevenLabs → 40 kbps mono; oryginał zostaje jako `*.orig.mp3`."""
    zrobione, pominiete = 0, 0
    for mp3 in sorted(AUDIO.glob("*.mp3")):
        if mp3.name.endswith(".orig.mp3"):
            continue
        orig = mp3.with_suffix(".orig.mp3")
        if orig.exists() and not od_nowa:
            pominiete += 1
            continue
        mp3.rename(orig)
        subprocess.run([FFMPEG, "-y", "-loglevel", "error", "-i", str(orig),
                        "-ac", "1", "-b:a", "40k", str(mp3)], check=True)
        zrobione += 1
    return zrobione, pominiete


if __name__ == "__main__":
    od_nowa = "--od-nowa" in sys.argv
    zo, po = obrazy(od_nowa)
    print(f"ilustracje: {zo} przetworzonych, {po} pominiętych")
    if AUDIO.exists():
        zn, pn = nagrania(od_nowa)
        print(f"nagrania:   {zn} przetworzonych, {pn} pominiętych")
