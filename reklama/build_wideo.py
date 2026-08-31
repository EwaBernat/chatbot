#!/usr/bin/env python3
"""Sklada spot EduPlaner 2026: plansze PNG + narracja MP3 -> MP4 1920x1080.

Czasy plansz pochodza z build_plansze.py i sa dopasowane do sciezki glosowej.
Uruchomienie:  python3 reklama/build_wideo.py [plik_audio.mp3] [wyjscie.mp4]
"""
import shutil
import subprocess
import sys
from pathlib import Path

from build_plansze import PLANSZE

KATALOG = Path(__file__).parent
PLANSZE_DIR = KATALOG / "plansze"
PRZEJSCIE = 0.6          # dlugosc xfade w sekundach
FPS = 30


def ffmpeg() -> str:
    """Pelny ffmpeg z PATH, a w razie braku — ten z pakietu imageio-ffmpeg.

    Nie uzywamy ffmpeg dolaczonego do Playwrighta: to okrojony build (tylko VP8/WebM),
    bez libx264, AAC i filtra xfade, ktorych ten montaz potrzebuje.
    """
    znaleziony = shutil.which("ffmpeg")
    if znaleziony:
        return znaleziony
    try:
        import imageio_ffmpeg
    except ImportError:
        raise SystemExit("Brak ffmpeg. Zainstaluj: pip install imageio-ffmpeg")
    return imageio_ffmpeg.get_ffmpeg_exe()


def main() -> int:
    audio = Path(sys.argv[1]) if len(sys.argv) > 1 else KATALOG / "cieply-wersja-1.mp3"
    wyjscie = Path(sys.argv[2]) if len(sys.argv) > 2 else KATALOG / "eduplaner-spot-60s.mp4"
    if not audio.exists():
        raise SystemExit(f"Brak pliku audio: {audio}")

    # xfade zjada (N-1) * PRZEJSCIE z laczna dlugosci — oddajemy to kazdej planszy
    # poza ostatnia, zeby obraz nie skonczyl sie przed narracja.
    czasy = [czas + PRZEJSCIE for _, czas, _ in PLANSZE[:-1]] + [PLANSZE[-1][1]]
    n = len(czasy)

    wejscia = []
    for (nazwa, _, _), czas in zip(PLANSZE, czasy):
        wejscia += ["-loop", "1", "-t", f"{czas:.3f}", "-i", str(PLANSZE_DIR / f"{nazwa}.png")]
    wejscia += ["-i", str(audio)]

    filtr = [f"[{i}:v]fps={FPS},format=yuv420p,setsar=1[v{i}]" for i in range(n)]
    biezacy, przesuniecie = "[v0]", 0.0
    for i in range(1, n):
        przesuniecie += czasy[i - 1] - PRZEJSCIE
        etykieta = f"[x{i}]"
        filtr.append(f"{biezacy}[v{i}]xfade=transition=fade:"
                     f"duration={PRZEJSCIE}:offset={przesuniecie:.3f}{etykieta}")
        biezacy = etykieta
    dlugosc = sum(czasy) - (n - 1) * PRZEJSCIE
    filtr.append(f"{biezacy}fade=t=in:st=0:d=0.5,"
                 f"fade=t=out:st={dlugosc - 1.0:.3f}:d=1.0[out]")

    polecenie = [
        ffmpeg(), "-y", *wejscia,
        "-filter_complex", ";".join(filtr),
        "-map", "[out]", "-map", f"{n}:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest", str(wyjscie),
    ]
    print(f"Obraz: {dlugosc:.1f} s · plansz: {n} · audio: {audio.name}")
    wynik = subprocess.run(polecenie, capture_output=True, text=True)
    if wynik.returncode != 0:
        print(wynik.stderr[-2500:])
        return wynik.returncode
    print(f"Gotowe: {wyjscie}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
