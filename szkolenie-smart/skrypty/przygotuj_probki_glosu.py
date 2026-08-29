#!/usr/bin/env python3
"""Robi z gotowych filmów materiał do sklonowania głosu w ElevenLabs.

Zamiast nagrywać próbki od nowa, wrzuć tu filmy, które już masz — webinary,
klipy, nagrania zajęć. Skrypt wyciąga z nich ścieżkę dźwiękową, wycina ciszę
i przerwy, dzieli mowę na fragmenty i zapisuje je w formacie, którego
ElevenLabs oczekuje: WAV 44,1 kHz mono, bez obróbki.

Świadomie NIE normalizuje i nie kompresuje dźwięku — ElevenLabs woli materiał
surowy, a „poprawiony" daje klon o spłaszczonej dynamice.

Na koniec skrypt mówi, ile czystej mowy uzbierało się łącznie i czy to wystarczy:
poniżej minuty klon brzmi płasko, trzy minuty to cel dla Instant Voice Cloning,
a trzydzieści minut i więcej otwiera drogę do Professional Voice Cloning.

Użycie:
    python3 skrypty/przygotuj_probki_glosu.py film1.mp4 film2.mp4 -o probki/
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

CZESTOTLIWOSC = 44100
PROG_CISZY_DB = -35          # poniżej tego poziomu uznajemy fragment za ciszę
MIN_CISZA = 0.5              # sekundy — krótsze przerwy zostają, to oddech
MIN_FRAGMENT = 4.0           # sekundy — krótsze fragmenty nie niosą intonacji
MAKS_FRAGMENT = 45.0         # sekundy — dłuższe tniemy, łatwiej je potem odrzucić
CEL_SEKUND = 180             # trzy minuty — cel dla Instant Voice Cloning


def znajdz_ffmpeg() -> str:
    """ffmpeg z PATH, a gdy go nie ma — ten dołączony do pakietu imageio-ffmpeg."""
    z_path = shutil.which("ffmpeg")
    if z_path:
        return z_path
    try:
        import imageio_ffmpeg
    except ImportError:
        print("Brak ffmpeg. Zainstaluj go w systemie albo: pip install imageio-ffmpeg")
        raise SystemExit(2)
    return imageio_ffmpeg.get_ffmpeg_exe()


def uruchom(ff: str, args: list[str]) -> str:
    wynik = subprocess.run([ff, "-hide_banner", *args], capture_output=True, text=True)
    return wynik.stderr


def do_wav(ff: str, zrodlo: Path, cel: Path) -> None:
    uruchom(ff, ["-y", "-loglevel", "error", "-i", str(zrodlo),
                 "-vn", "-ac", "1", "-ar", str(CZESTOTLIWOSC), "-c:a", "pcm_s16le", str(cel)])
    if not cel.exists():
        print(f"  ✕ nie udało się wyciągnąć dźwięku z {zrodlo.name}")


def dlugosc(ff: str, plik: Path) -> float:
    for linia in uruchom(ff, ["-i", str(plik)]).splitlines():
        m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", linia)
        if m:
            g, mi, s = m.groups()
            return int(g) * 3600 + int(mi) * 60 + float(s)
    return 0.0


def glosnosc(ff: str, plik: Path) -> tuple[float, float]:
    wyjscie = uruchom(ff, ["-i", str(plik), "-af", "volumedetect", "-f", "null", "-"])
    srednia = maks = 0.0
    for linia in wyjscie.splitlines():
        if "mean_volume:" in linia:
            srednia = float(linia.split("mean_volume:")[1].split("dB")[0])
        if "max_volume:" in linia:
            maks = float(linia.split("max_volume:")[1].split("dB")[0])
    return srednia, maks


def odcinki_mowy(ff: str, plik: Path, calosc: float) -> list[tuple[float, float]]:
    """Zwraca przedziały mowy — to, co zostaje po wycięciu wykrytej ciszy."""
    wyjscie = uruchom(ff, ["-i", str(plik),
                           "-af", f"silencedetect=noise={PROG_CISZY_DB}dB:d={MIN_CISZA}",
                           "-f", "null", "-"])
    ciszа: list[list[float]] = []
    for linia in wyjscie.splitlines():
        if "silence_start:" in linia:
            ciszа.append([float(linia.split("silence_start:")[1].strip()), calosc])
        elif "silence_end:" in linia and ciszа:
            ciszа[-1][1] = float(linia.split("silence_end:")[1].split("|")[0].strip())

    mowa: list[tuple[float, float]] = []
    kursor = 0.0
    for od, do_ in ciszа:
        if od - kursor >= MIN_FRAGMENT:
            mowa.append((kursor, od))
        kursor = do_
    if calosc - kursor >= MIN_FRAGMENT:
        mowa.append((kursor, calosc))
    return mowa or [(0.0, calosc)]


def potnij(przedzialy: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Dzieli zbyt długie przedziały, żeby żaden plik nie przekraczał limitu."""
    wynik = []
    for od, do_ in przedzialy:
        kursor = od
        while do_ - kursor > MAKS_FRAGMENT:
            wynik.append((kursor, kursor + MAKS_FRAGMENT))
            kursor += MAKS_FRAGMENT
        if do_ - kursor >= MIN_FRAGMENT:
            wynik.append((kursor, do_))
    return wynik


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pliki", nargs="+", type=Path, help="filmy albo nagrania audio")
    ap.add_argument("-o", "--katalog", type=Path, default=Path("probki-glosu"),
                    help="katalog na gotowe próbki (domyślnie probki-glosu/)")
    args = ap.parse_args()

    ff = znajdz_ffmpeg()
    args.katalog.mkdir(parents=True, exist_ok=True)
    roboczy = args.katalog / ".roboczy.wav"

    numer = 0
    uzbierane = 0.0
    for zrodlo in args.pliki:
        if not zrodlo.exists():
            print(f"✕ nie ma pliku {zrodlo}")
            continue

        print(f"\n{zrodlo.name}")
        do_wav(ff, zrodlo, roboczy)
        if not roboczy.exists():
            continue

        calosc = dlugosc(ff, roboczy)
        srednia, maks = glosnosc(ff, roboczy)
        print(f"  długość {calosc:.1f} s · średnia {srednia:.1f} dB · szczyt {maks:.1f} dB")
        if maks > -1.0:
            print("  ⚠ dźwięk przesterowany — klon odziedziczy zniekształcenie")
        if srednia < -40:
            print("  ⚠ nagranie bardzo ciche — sprawdź, czy mowa nie tonie w szumie")

        for od, do_ in potnij(odcinki_mowy(ff, roboczy, calosc)):
            numer += 1
            cel = args.katalog / f"probka-{numer:02d}.wav"
            uruchom(ff, ["-y", "-loglevel", "error", "-i", str(roboczy),
                         "-ss", f"{od:.3f}", "-to", f"{do_:.3f}",
                         "-ac", "1", "-ar", str(CZESTOTLIWOSC), "-c:a", "pcm_s16le", str(cel)])
            uzbierane += do_ - od
            print(f"  → {cel.name}  ({do_ - od:.1f} s)")

    roboczy.unlink(missing_ok=True)

    minuty, sekundy = divmod(uzbierane, 60)
    print(f"\nRazem czystej mowy: {int(minuty)} min {sekundy:04.1f} s w {numer} plikach")
    print(f"Katalog: {args.katalog}")
    if uzbierane < 60:
        print("\n⚠ To za mało. Poniżej minuty klon brzmi płasko i mechanicznie —")
        print("  dokładnie tak, jak nieudane klony. Dorzuć kolejne filmy.")
    elif uzbierane < CEL_SEKUND:
        print(f"\n⚠ Działa, ale do celu brakuje {(CEL_SEKUND - uzbierane) / 60:.1f} min.")
        print("  Przy tej długości intonacja klonu bywa monotonna.")
    elif uzbierane < 1800:
        print("\n✓ Wystarczy na dobry Instant Voice Clone.")
        print("  Na Professional Voice Cloning potrzeba 30 minut i więcej.")
    else:
        print("\n✓ Starczy nawet na Professional Voice Cloning.")
    print("\nWrzuć te pliki na https://elevenlabs.io/app/voice-lab → Add a new voice.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
