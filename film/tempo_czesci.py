#!/usr/bin/env python3
"""Współczynniki atempo wyrównujące tempo mówienia w częściach nagrania.

Użycie: python3 film/tempo_czesci.py czesc1.mp3 czesc2.mp3 ...  → po jednej liczbie na wiersz
Gdy liczba części = liczba akapitów narracji po intro (16), tempo każdej części liczy się
jako znaki akapitu / sekundy mowy, a współczynnik = tempo docelowe (mediana) / tempo części,
ograniczony do 0,85–1,18, żeby głos brzmiał naturalnie. W innym wypadku wypisuje 1.0.
"""
import re
import subprocess
import sys
from pathlib import Path
from statistics import median

TU = Path(__file__).resolve().parent


def ffmpeg_exe():
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return "ffmpeg"


def sekundy_mowy(ff, plik):
    """Długość pliku bez ciszy na końcu (tak liczy się tempo)."""
    out = subprocess.run(
        [ff, "-i", str(plik), "-af", "areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    h, mi, s = re.findall(r"time=(\d+):(\d+):([\d.]+)", out)[-1]
    return int(h) * 3600 + int(mi) * 60 + float(s)


def main():
    pliki = sys.argv[1:]
    tekst = (TU / "narracja.txt").read_text(encoding="utf-8").strip()
    ak = [a.strip() for a in re.split(r"\n\s*\n", tekst) if a.strip()][1:]
    if len(pliki) != len(ak):
        print("\n".join("1.0" for _ in pliki))
        print(f"tempo: {len(pliki)} części ≠ {len(ak)} akapitów – bez wyrównania", file=sys.stderr)
        return
    ff = ffmpeg_exe()
    tempa = [len(re.sub(r"\s+", "", a)) / sekundy_mowy(ff, p) for a, p in zip(ak, pliki)]
    cel = median(tempa)
    for t in tempa:
        print(f"{min(1.18, max(0.85, cel / t)):.4f}")
    print(f"tempo: {min(tempa):.1f}–{max(tempa):.1f} zn/s, cel {cel:.1f} zn/s", file=sys.stderr)


if __name__ == "__main__":
    main()
