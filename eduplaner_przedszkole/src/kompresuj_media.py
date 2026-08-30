#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kompresja mediów do osadzenia w banku celów — uruchamiana po każdej partii.

Media trafiają do HTML jako data-URI, więc każdy kilobajt liczy się podwójnie
(base64 dodaje jedną trzecią). Bez tego kroku 42 pomoce dydaktyczne wysadziłyby
limit rozmiaru dokumentu.

Co robi:
  * MP3  → 40 kbps mono 24 kHz. Mowa, nie muzyka. Niżej nie schodzimy:
           to jej własny głos i ciepło w nim ma być słyszalne. Oryginał
           zostaje obok jako `*.orig.mp3` (poza repozytorium).
  * PNG  → `k_*.jpg` 760 px, jakość 76, progresywny. Zdjęcia pomocy są
           oglądane, nie drukowane w rozdzielczości fotograficznej — przy
           760 px symbole na kartach są nadal czytelne, a plik waży jedną
           trzecią tego, co przy 900 px.
  * MP4  → H.264 CRF 30, 960 px, dźwięk 48 kbps. Na razie nieużywane,
           ale gdyby doszły filmy, przechodzą tą samą drogą.

Pliki już przetworzone są pomijane, więc skrypt można puszczać po każdej partii.
Uruchomienie: python3 src/kompresuj_media.py
Przeliczenie wszystkiego od nowa z oryginałów (po zmianie ustawień):
             python3 src/kompresuj_media.py --przelicz
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import imageio_ffmpeg
from PIL import Image

KORZEN = Path(__file__).resolve().parent.parent
PRZELICZ = "--przelicz" in sys.argv
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

KATALOGI_AUDIO = ["assets/audio_a", "assets/audio_b", "assets/audio_c1"]
KATALOGI_FOTO = ["assets/pomoce_a", "assets/pomoce_b"]
KATALOGI_WIDEO = ["assets/wideo"]

SZEROKOSC_FOTO = 760
JAKOSC_FOTO = 76
BITRATE_AUDIO = "40k"


def kb(sciezka: Path) -> float:
    return sciezka.stat().st_size / 1024


def kompresuj_audio() -> tuple[int, float, float]:
    ile = przed = po = 0
    for katalog in KATALOGI_AUDIO:
        for plik in sorted((KORZEN / katalog).glob("*.mp3")):
            if plik.name.endswith(".orig.mp3"):
                continue
            oryginal = plik.with_suffix(".orig.mp3")
            if oryginal.exists():
                if not PRZELICZ:            # już przetworzony
                    continue
                plik.unlink()               # przeliczamy od nowa z oryginału
            else:
                plik.rename(oryginal)
            subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(oryginal),
                            "-ac", "1", "-b:a", BITRATE_AUDIO, "-ar", "24000", str(plik)],
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
            if kadr.exists() and not PRZELICZ:
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
