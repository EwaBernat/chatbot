#!/usr/bin/env python3
"""Sklada spot EduPlaner 2026: plansze PNG + narracja MP3 -> MP4.

Czasy plansz pochodza z build_plansze.py i sa dopasowane do sciezki glosowej,
wiec oba formaty maja identyczny montaz — tylko inny kadr.

Uruchomienie:
    python3 reklama/build_wideo.py                     # poziom, glos domyslny
    python3 reklama/build_wideo.py pion
    python3 reklama/build_wideo.py pion cieply-wersja-3.mp3
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

from build_plansze import CZASY, FORMATY

KATALOG = Path(__file__).parent
DOMYSLNE_AUDIO = KATALOG / "glos-bezosobowy.mp3"
OGON = 1.5               # ile sekundy ekran koncowy zostaje po ostatnim slowie
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


def dlugosc_audio(sciezka: Path) -> float | None:
    """Dlugosc nagrania w sekundach, odczytana z naglowka przez ffmpeg.

    Nie uzywamy ffprobe — build z imageio-ffmpeg go nie zawiera. ffmpeg bez
    wyjscia konczy sie bledem, ale zdazy wypisac Duration na stderr.
    """
    wynik = subprocess.run([ffmpeg(), "-hide_banner", "-i", str(sciezka)],
                           capture_output=True, text=True)
    trafienie = re.search(r"Duration: (\d+):(\d+):(\d+\.?\d*)", wynik.stderr)
    if not trafienie:
        return None
    g, m, s = trafienie.groups()
    return int(g) * 3600 + int(m) * 60 + float(s)


def main() -> int:
    format_nazwa = sys.argv[1] if len(sys.argv) > 1 else "poziom"
    if format_nazwa not in FORMATY:
        raise SystemExit(f"Nieznany format: {format_nazwa}. Dostępne: {', '.join(FORMATY)}")
    f = FORMATY[format_nazwa]

    audio = Path(sys.argv[2]) if len(sys.argv) > 2 else DOMYSLNE_AUDIO
    if not audio.is_absolute():
        audio = KATALOG / audio
    if not audio.exists():
        raise SystemExit(f"Brak pliku audio: {audio}")
    if not f["katalog"].exists():
        raise SystemExit(f"Brak plansz. Uruchom najpierw: python3 build_plansze.py {format_nazwa}")

    przyrostek = "" if format_nazwa == "poziom" else "-pion"
    wyjscie = KATALOG / f"eduplaner-spot-60s{przyrostek}.mp4"

    # xfade zjada (N-1) * PRZEJSCIE z lacznej dlugosci — oddajemy to kazdej planszy
    # poza ostatnia, zeby obraz nie skonczyl sie przed narracja.
    czasy = [czas + PRZEJSCIE for _, czas in CZASY[:-1]] + [CZASY[-1][1]]
    n = len(czasy)

    # Obraz musi byc dluzszy od narracji, inaczej -shortest utnie ostatnie slowa.
    # Roznice dokladamy do ostatniej planszy: ekran koncowy i tak ma wybrzmiec
    # w ciszy, wiec wydluzenie go niczego nie psuje.
    trwanie_audio = dlugosc_audio(audio)
    if trwanie_audio:
        obraz = sum(czasy) - (n - 1) * PRZEJSCIE
        brakuje = trwanie_audio + OGON - obraz
        if brakuje > 0:
            czasy[-1] += brakuje
            print(f"  audio {trwanie_audio:.1f} s — ostatnia plansza dłuższa o {brakuje:.1f} s")

    wejscia = []
    for (nazwa, _), czas in zip(CZASY, czasy):
        wejscia += ["-loop", "1", "-t", f"{czas:.3f}", "-i", str(f["katalog"] / f"{nazwa}.png")]
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
    print(f"{format_nazwa} {f['w']}x{f['h']} · obraz {dlugosc:.1f} s · "
          f"plansz {n} · audio {audio.name}")
    wynik = subprocess.run(polecenie, capture_output=True, text=True)
    if wynik.returncode != 0:
        print(wynik.stderr[-2500:])
        return wynik.returncode
    print(f"Gotowe: {wyjscie}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
