#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wyrównuje głośność nagrań lektorskich do poziomu materiału, do którego trafiają.

Nagrania z ElevenLabs bywają o 1–4 dB cichsze niż gotowy film. Na styku słychać to
od razu. Skrypt mierzy głośność (EBU R128), liczy różnicę i nakłada STAŁE wzmocnienie —
inaczej niż jednoprzebiegowy loudnorm, który działa dynamicznie i potrafi rozminąć się
z celem o 2 dB.

    # cel odczytany z filmu, do którego wklejamy wstawki
    python3 wyrownaj_glosnosc.py --cel-z-pliku M1.mp4 audio/*.mp3

    # cel podany wprost (−20,7 LUFS to poziom narracji w modułach EduPlaner)
    python3 wyrownaj_glosnosc.py --cel -20.7 audio/*.mp3

Oryginały lądują w podkatalogu `oryg/`, żeby dało się wrócić.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys


def lufs(sciezka):
    """Głośność scalona wg EBU R128."""
    r = subprocess.run(
        ['ffmpeg', '-hide_banner', '-nostats', '-i', sciezka,
         '-af', 'ebur128=framelog=quiet', '-f', 'null', '-'],
        capture_output=True, text=True)
    m = re.search(r'Summary:.*?I:\s*(-?\d+\.?\d*)\s*LUFS', r.stderr, re.S)
    if not m:
        raise SystemExit(f'Nie udało się zmierzyć głośności: {sciezka}')
    return float(m.group(1))


def main():
    ap = argparse.ArgumentParser(description='Wyrównanie głośności nagrań do materiału docelowego.')
    ap.add_argument('pliki', nargs='+', help='nagrania do wyrównania (mp3, wav, m4a)')
    g = ap.add_mutually_exclusive_group()
    g.add_argument('--cel', type=float, help='docelowa głośność w LUFS')
    g.add_argument('--cel-z-pliku', help='zmierz cel z tego pliku (film albo nagranie wzorcowe)')
    ap.add_argument('--tolerancja', type=float, default=0.3,
                    help='pomijaj pliki mieszczące się w tylu dB od celu (domyślnie 0,3)')
    a = ap.parse_args()

    if a.cel_z_pliku:
        cel = lufs(a.cel_z_pliku)
        print(f'Cel odczytany z {os.path.basename(a.cel_z_pliku)}: {cel:.1f} LUFS\n')
    else:
        cel = a.cel if a.cel is not None else -20.7
        print(f'Cel: {cel:.1f} LUFS\n')

    print(f'{"plik":<14}{"przed":>9}{"korekta":>10}{"po":>9}')
    print('-' * 42)
    for p in a.pliki:
        if not os.path.exists(p):
            print(f'{os.path.basename(p):<14}  — brak pliku, pomijam')
            continue
        katalog = os.path.dirname(os.path.abspath(p))
        nazwa = os.path.basename(p)
        zapas = os.path.join(katalog, 'oryg')
        os.makedirs(zapas, exist_ok=True)
        zrodlo = os.path.join(zapas, nazwa)
        if not os.path.exists(zrodlo):
            shutil.copy2(p, zrodlo)

        przed = lufs(zrodlo)
        korekta = cel - przed
        if abs(korekta) < a.tolerancja:
            print(f'{nazwa:<14}{przed:>8.1f} {"—":>9} {przed:>8.1f}   (w tolerancji)')
            continue
        subprocess.run(
            ['ffmpeg', '-v', 'error', '-i', zrodlo, '-af', f'volume={korekta:.2f}dB',
             '-c:a', 'libmp3lame', '-b:a', '192k', '-ar', '48000', p, '-y'], check=True)
        print(f'{nazwa:<14}{przed:>8.1f} {korekta:>+8.1f} dB {lufs(p):>8.1f}')

    print(f'\nOryginały zachowane w podkatalogu oryg/.')


if __name__ == '__main__':
    main()
