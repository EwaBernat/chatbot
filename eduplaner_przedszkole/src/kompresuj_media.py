#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kompresja mediów do osadzenia w banku celów — uruchamiana po każdej partii.

Media trafiają do HTML jako data-URI, więc każdy kilobajt liczy się podwójnie
(base64 dodaje jedną trzecią). Bez tego kroku 42 pomoce dydaktyczne wysadziłyby
limit rozmiaru dokumentu.

Co robi:
  * MP3  → 48 kbps mono 24 kHz. Mowa, nie muzyka — różnicy nie słychać,
           a plik chudnie do jednej trzeciej. Oryginał zostaje obok jako
           `*.orig.mp3` (poza repozytorium, patrz .gitignore).
  * PNG  → `k_*.jpg` 900 px, jakość 82, progresywny. To fotografie pomocy,
           więc JPEG bije PNG piętnastokrotnie.
  * MP4  → H.264 CRF 30, 960 px, dźwięk 48 kbps. Na razie nieużywane,
           ale gdyby doszły filmy, przechodzą tą samą drogą.

Pliki już przetworzone są pomijane, więc skrypt można puszczać po każdej partii.
Uruchomienie: python3 src/kompresuj_media.py
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image

KORZEN = Path(__file__).resolve().parent.parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

KATALOGI_AUDIO = ["assets/audio_a", "assets/audio_b", "assets/audio_c1"]
KATALOGI_FOTO = ["assets/pomoce_a", "assets/pomoce_b"]
KATALOGI_WIDEO = ["assets/wideo"]

SZEROKOSC_FOTO = 900
JAKOSC_FOTO = 82


def kb(sciezka: Path) -> float:
    return sciezka.stat().st_size / 1024


def kompresuj_audio() -> tuple[int, float, float]:
    ile = przed = po = 0
    for katalog in KATALOGI_AUDIO:
        for plik in sorted((KORZEN / katalog).glob("*.mp3")):
            if plik.name.endswith(".orig.mp3"):
                continue
            oryginal = plik.with_suffix(".orig.mp3")
            if oryginal.exists():           # już przetworzony
                continue
            plik.rename(oryginal)
            subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(oryginal),
                            "-ac", "1", "-b:a", "48k", "-ar", "24000", str(plik)],
                           check=True)
            ile += 1
            przed += kb(oryginal)
            po += kb(plik)
    return ile, przed, po


def kompresuj_foto() -> tuple[int, float, float]:
    ile = przed = po = 0
    for katalog in KATALOGI_FOTO:
        for plik in sorted((KORZEN / katalog).glob("*.png")):
            if plik.name.startswith("k_"):
                continue
            kadr = plik.with_name("k_" + plik.stem + ".jpg")
            if kadr.exists():
                continue
            obraz = Image.open(plik).convert("RGB")
            wysokosc = round(SZEROKOSC_FOTO * obraz.size[1] / obraz.size[0])
            obraz = obraz.resize((SZEROKOSC_FOTO, wysokosc), Image.LANCZOS)
            obraz.save(kadr, "JPEG", quality=JAKOSC_FOTO, optimize=True, progressive=True)
            ile += 1
            przed += kb(plik)
            po += kb(kadr)
    return ile, przed, po


def kompresuj_wideo() -> tuple[int, float, float]:
    ile = przed = po = 0
    for katalog in KATALOGI_WIDEO:
        sciezka = KORZEN / katalog
        if not sciezka.exists():
            continue
        for plik in sorted(sciezka.glob("*.mp4")):
            if plik.name.startswith("k_"):
                continue
            kadr = plik.with_name("k_" + plik.name)
            if kadr.exists():
                continue
            subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(plik),
                            "-vf", "scale=960:-2", "-c:v", "libx264", "-crf", "30",
                            "-preset", "slow", "-c:a", "aac", "-b:a", "48k",
                            "-movflags", "+faststart", str(kadr)], check=True)
            ile += 1
            przed += kb(plik)
            po += kb(kadr)
    return ile, przed, po


def main() -> int:
    razem_przed = razem_po = 0.0
    for nazwa, funkcja in (("nagrań", kompresuj_audio),
                           ("zdjęć", kompresuj_foto),
                           ("filmów", kompresuj_wideo)):
        ile, przed, po = funkcja()
        razem_przed += przed
        razem_po += po
        if ile:
            print(f"  {nazwa:<8} {ile:>3} · {przed/1024:.2f} MB → {po/1024:.2f} MB "
                  f"({po/przed*100:.0f}%)")
        else:
            print(f"  {nazwa:<8}   — nic nowego")
    if razem_przed:
        print(f"\nrazem: {razem_przed/1024:.2f} MB → {razem_po/1024:.2f} MB "
              f"(zaoszczędzone {(razem_przed-razem_po)/1024:.2f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
