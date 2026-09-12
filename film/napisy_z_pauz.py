#!/usr/bin/env python3
"""Dopasowuje sceny filmu do nagrania narracji (Twój głos z ElevenLabs).

Wejście:  film/narracja.mp3 (nagranie akapitów 2–17 z film/narracja.txt, bez intro Ewy)
Wyjście:  film/out/napisy.srt  → kopie: film/napisy.srt, film/remotion/public/napisy.srt

Jak: ffmpeg silencedetect wykrywa pauzy w nagraniu; spośród nich wybieramy 15 granic tak,
aby położenie każdej było jak najbliżej proporcji długości akapitów (liczba słów), a dłuższe
pauzy miały pierwszeństwo. Każdy akapit dzielimy na zdania i rozkładamy je w czasie
akapitu proporcjonalnie do liczby słów. Czasy liczone od początku narracja.mp3 (bez intro –
film sam dodaje 13 s intro przy wczytaniu).

Użycie: python3 film/napisy_z_pauz.py [--mp3 film/narracja.mp3] [--noise -35dB] [--min-pauza 0.35]
"""
import argparse
import re
import shutil
import subprocess
from pathlib import Path

TU = Path(__file__).resolve().parent


def ffmpeg_exe() -> str:
    try:
        import imageio_ffmpeg  # pakiet imageio_ffmpeg dostarcza ffmpeg bez instalacji systemowej
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return shutil.which("ffmpeg") or "ffmpeg"


def wykryj_pauzy(ff: str, mp3: Path, noise: str, min_pauza: float):
    out = subprocess.run(
        [ff, "-hide_banner", "-i", str(mp3), "-af", f"silencedetect=noise={noise}:d={min_pauza}", "-f", "null", "-"],
        capture_output=True, text=True,
    ).stderr
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.?\d*)", out)
    dur = int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])
    starty = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    konce = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    pauzy = list(zip(starty, konce))  # (początek ciszy, koniec ciszy)
    if len(konce) < len(starty):  # cisza do końca pliku
        pauzy.append((starty[-1], dur))
    return dur, pauzy


def akapity_narracji() -> list[str]:
    tekst = (TU / "narracja.txt").read_text(encoding="utf-8").strip()
    ak = [a.strip() for a in re.split(r"\n\s*\n", tekst) if a.strip()]
    return ak[1:]  # akapit 1 to intro Ewy (gotowy klip), nagranie zaczyna się od akapitu 2


def zdania(akapit: str) -> list[str]:
    return [z.strip() for z in re.split(r"(?<=[.!?…])\s+", akapit) if z.strip()]


def wybierz_granice(pauzy, cele, mowa_od, mowa_do):
    """Monotoniczne przypisanie 15 celów do pauz (programowanie dynamiczne, koszt = odległość / (1 + długość pauzy))."""
    kand = [(a, b) for a, b in pauzy if a > mowa_od + 0.5 and b < mowa_do - 0.5]
    n, k = len(kand), len(cele)
    if n < k:
        raise SystemExit(f"za mało pauz ({n}) na {k} granic – zmniejsz --min-pauza albo podnieś --noise")
    INF = float("inf")
    koszt = [[abs((a + b) / 2 - c) / (1.0 + (b - a)) for c in cele] for a, b in kand]
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    wyb = [[False] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 0.0
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            pomin = dp[i - 1][j]
            wez = dp[i - 1][j - 1] + koszt[i - 1][j - 1]
            if wez < pomin:
                dp[i][j], wyb[i][j] = wez, True
            else:
                dp[i][j] = pomin
    granice, i, j = [], n, k
    while j > 0:
        if wyb[i][j]:
            a, b = kand[i - 1]
            granice.append(b - min(0.15, (b - a) / 3))  # scena rusza tuż przed pierwszym słowem
            j -= 1
        i -= 1
    return sorted(granice)


def srt_czas(t: float) -> str:
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mp3", default=str(TU / "narracja.mp3"))
    ap.add_argument("--noise", default="-35dB")
    ap.add_argument("--min-pauza", type=float, default=0.35)
    a = ap.parse_args()
    ff = ffmpeg_exe()
    mp3 = Path(a.mp3)
    dur, pauzy = wykryj_pauzy(ff, mp3, a.noise, a.min_pauza)
    ak = akapity_narracji()
    if len(ak) != 16:
        raise SystemExit(f"oczekuję 16 akapitów po intro, jest {len(ak)}")
    # mowa zaczyna się po ciszy na początku i kończy przed ciszą na końcu
    mowa_od = pauzy[0][1] if pauzy and pauzy[0][0] < 0.05 else 0.0
    mowa_do = pauzy[-1][0] if pauzy and pauzy[-1][1] >= dur - 0.05 else dur
    wagi = [len(x.split()) for x in ak]
    suma = sum(wagi)
    cele, s = [], 0
    for w in wagi[:-1]:
        s += w
        cele.append(mowa_od + (mowa_do - mowa_od) * s / suma)
    granice = wybierz_granice(pauzy, cele, mowa_od, mowa_do)
    brzegi = [mowa_od] + granice + [dur]

    cues = []
    for i, akapit in enumerate(ak):
        t0, t1 = brzegi[i], brzegi[i + 1]
        koniec_mowy = t1 - (0.25 if i + 1 < len(ak) else 0.0)
        zd = zdania(akapit)
        w = [len(z.split()) for z in zd]
        t = t0
        for z, wz in zip(zd, w):
            d = (koniec_mowy - t0) * wz / sum(w)
            cues.append((t, t + d, z))
            t += d
    out = TU / "out" / "napisy.srt"
    out.parent.mkdir(exist_ok=True)
    out.write_text(
        "".join(f"{n}\n{srt_czas(a)} --> {srt_czas(b)}\n{txt}\n\n" for n, (a, b, txt) in enumerate(cues, 1)),
        encoding="utf-8",
    )
    for kopia in (TU / "napisy.srt", TU / "remotion" / "public" / "napisy.srt"):
        kopia.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(out, kopia)

    print(f"nagranie: {dur:.1f} s, pauz ≥{a.min_pauza}s: {len(pauzy)}, mowa {mowa_od:.2f}–{mowa_do:.2f} s")
    print(f"{'akapit':>6} {'start':>7} {'koniec':>7} {'czas':>6} {'cel':>7} {'słów':>5}  początek")
    for i, akapit in enumerate(ak):
        cel = cele[i - 1] if i else mowa_od
        print(f"{i + 2:>6} {brzegi[i]:7.2f} {brzegi[i + 1]:7.2f} {brzegi[i + 1] - brzegi[i]:6.1f} {cel:7.2f} {wagi[i]:>5}  {akapit[:48]}")
    print(f"zapisano {out} ({len(cues)} napisów) + kopie film/napisy.srt, film/remotion/public/napisy.srt")


if __name__ == "__main__":
    main()
