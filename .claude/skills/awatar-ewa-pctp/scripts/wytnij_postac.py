#!/usr/bin/env python3
"""Wycina sama postac Ewy z klipu — bez tla — do pliku z przezroczystoscia.

Radzi sobie z trzema rodzajami tla:
  * szachownica z podgladu HeyGen (jasne kwadraty; tak wyglada eksport „transparent" w MP4),
  * jednolity kolor (zielony, niebieski, fiolet marki...),
  * prawdziwy kanal alfa (WebM/MOV) — wtedy tylko przepakowuje.

Wyniki (dowolne z nich, domyslnie WebM + PNG):
  --webm   klip VP9 z alfa (do wstaw_ewe.py, Remotion, HyperFrames, DaVinci)
  --mov    klip ProRes 4444 z alfa (Premiere, Final Cut, Keynote, PowerPoint na Macu)
  --png    jeden kadr PNG z przezroczystoscia (prezentacje, plansze, miniatury)
  --sekwencja  katalog z PNG-ami klatka po klatce

Zaleznosci: ffmpeg (systemowy albo `pip install imageio-ffmpeg`), numpy, opencv-python-headless.

Przyklady:
    python3 wytnij_postac.py intro.mp4                             # auto: szachownica albo kolor
    python3 wytnij_postac.py intro.mp4 --png ewa.png --czas 6      # sam kadr PNG z 6. sekundy
    python3 wytnij_postac.py ewa_zielona.mp4 --tlo "#00FF00" --webm ewa.webm --mov ewa.mov
    python3 wytnij_postac.py intro.mp4 --podglad podglad.jpg       # sprawdz maske przed renderem
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import cv2
    import numpy as np
except ImportError:
    raise SystemExit("Potrzebne: pip install numpy opencv-python-headless")


# --- srodowisko ------------------------------------------------------------

def znajdz_ffmpeg() -> str:
    if szukany := shutil.which("ffmpeg"):
        return szukany
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        raise SystemExit("Brak ffmpeg. Zainstaluj systemowy ffmpeg albo: pip install imageio-ffmpeg")


def ma_alfe(ffmpeg: str, plik: Path) -> bool:
    tekst = subprocess.run([ffmpeg, "-hide_banner", "-i", str(plik)],
                           capture_output=True, text=True).stderr
    return any(f in tekst for f in ("yuva420p", "yuva444p", "rgba", "argb", "bgra", "gbrap")) \
        or "alpha_mode" in tekst


def kolor_bgr(tekst: str) -> np.ndarray:
    t = tekst.strip().lstrip("#")
    if t.lower().startswith("0x"):
        t = t[2:]
    if len(t) != 6:
        raise SystemExit(f"Kolor `{tekst}` — podaj #RRGGBB.")
    r, g, b = int(t[0:2], 16), int(t[2:4], 16), int(t[4:6], 16)
    return np.array([b, g, r], dtype=np.float32)


# --- model tla -------------------------------------------------------------

def obszar_brzegowy(klatka: np.ndarray) -> np.ndarray:
    """Piksele, w ktorych na pewno nie ma postaci: boki i gora kadru."""
    h, w = klatka.shape[:2]
    bok = max(8, int(w * 0.12))
    gora = max(4, int(h * 0.04))
    czesci = [klatka[:, :bok].reshape(-1, 3), klatka[:, w - bok:].reshape(-1, 3),
              klatka[:gora, :].reshape(-1, 3)]
    return np.concatenate(czesci).astype(np.float32)


def kolory_tla(piksele: np.ndarray) -> list[np.ndarray]:
    """Dwa najczestsze kolory tla (szachownica) albo jeden (jednolite tlo)."""
    probka = piksele[np.random.default_rng(0).choice(len(piksele), min(len(piksele), 20000),
                                                     replace=False)]
    kryteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.5)
    _, etykiety, srodki = cv2.kmeans(probka, 2, None, kryteria, 3, cv2.KMEANS_PP_CENTERS)
    udzialy = np.bincount(etykiety.ravel(), minlength=2) / len(etykiety)
    if np.abs(srodki[0] - srodki[1]).max() < 6 or udzialy.min() < 0.15:
        return [probka.mean(axis=0)]
    return [srodki[0], srodki[1]]


def odleglosc_od_tla(klatka: np.ndarray, kolory: list[np.ndarray]) -> np.ndarray:
    k = klatka.astype(np.float32)
    odl = [np.abs(k - c).max(axis=2) for c in kolory]
    return np.minimum.reduce(odl) if len(odl) > 1 else odl[0]


def maska_alfa(klatka: np.ndarray, kolory: list[np.ndarray], prog_dol: float,
               prog_gora: float, piorko: float) -> np.ndarray:
    """Alfa 0..1: miekka na krawedzi, pelna w srodku postaci (dziury zalane)."""
    odl = odleglosc_od_tla(klatka, kolory)
    miekka = np.clip((odl - prog_dol) / max(prog_gora - prog_dol, 1e-3), 0.0, 1.0)

    twarda = (miekka > 0.5).astype(np.uint8)
    # drobne smieci tla precz, potem zalej dziury (bluzka w kolorze tla itp.)
    twarda = cv2.morphologyEx(twarda, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    h, w = twarda.shape
    wypelnienie = twarda.copy()
    ramka = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(wypelnienie, ramka, (0, 0), 1)            # zalej tlo od rogu
    for x in (w - 1,):
        if wypelnienie[0, x] == 0:
            cv2.floodFill(wypelnienie, ramka, (x, 0), 1)
    dziury = (wypelnienie == 0).astype(np.uint8)              # co nie jest tlem ani postacia
    zalane = np.clip(twarda + dziury, 0, 1)

    # zostaw tylko duze skladowe (postac), reszta to szum
    n, etykiety, staty, _ = cv2.connectedComponentsWithStats(zalane, connectivity=8)
    if n > 1:
        pola = staty[1:, cv2.CC_STAT_AREA]
        prog_pola = max(pola.max() * 0.02, 400)
        zostaw = np.isin(etykiety, [i + 1 for i, p in enumerate(pola) if p >= prog_pola])
        zalane = zalane * zostaw.astype(np.uint8)

    alfa = zalane.astype(np.float32)
    if piorko > 0:
        # piorko: rozmycie twardej maski daje miekka krawedz o szerokosci ok. 2*piorko px
        alfa = cv2.GaussianBlur(alfa, (0, 0), piorko)
    return alfa


def usun_kolor_tla_z_krawedzi(klatka: np.ndarray, alfa: np.ndarray,
                              kolory: list[np.ndarray]) -> np.ndarray:
    """Na polprzezroczystej krawedzi odejmuje domieszke tla (despill)."""
    k = klatka.astype(np.float32)
    tlo = np.mean(kolory, axis=0)
    a = np.clip(alfa, 0.05, 1.0)[..., None]
    czysta = (k - tlo * (1 - a)) / a
    krawedz = (alfa > 0.05) & (alfa < 0.98)
    wynik = k.copy()
    wynik[krawedz] = czysta[krawedz]
    return np.clip(wynik, 0, 255).astype(np.uint8)


# --- wejscie / wyjscie -----------------------------------------------------

def klatki(plik: Path, od_sekundy: float | None = None):
    cap = cv2.VideoCapture(str(plik))
    if not cap.isOpened():
        raise SystemExit(f"Nie moge otworzyc {plik} (OpenCV bez obslugi tego formatu?).")
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    if od_sekundy:
        cap.set(cv2.CAP_PROP_POS_MSEC, od_sekundy * 1000)
    try:
        while True:
            ok, klatka = cap.read()
            if not ok:
                break
            yield fps, n, klatka
    finally:
        cap.release()


def koder_ffmpeg(ffmpeg: str, rodzaj: str, wyjscie: Path, w: int, h: int, fps: float,
                 audio: Path | None) -> subprocess.Popen:
    cmd = [ffmpeg, "-hide_banner", "-loglevel", "error", "-y",
           "-f", "rawvideo", "-pix_fmt", "bgra", "-s", f"{w}x{h}", "-r", f"{fps:.3f}", "-i", "-"]
    if audio:
        cmd += ["-i", str(audio), "-map", "0:v", "-map", "1:a?", "-c:a"]
        cmd += ["libopus", "-b:a", "128k"] if rodzaj == "webm" else ["pcm_s16le"]
    if rodzaj == "webm":
        cmd += ["-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-auto-alt-ref", "0",
                "-b:v", "0", "-crf", "24", "-row-mt", "1", "-deadline", "good", "-cpu-used", "2"]
    else:
        cmd += ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le"]
    cmd += ["-shortest", str(wyjscie)]
    return subprocess.Popen(cmd, stdin=subprocess.PIPE)


def przepakuj_z_alfa(ffmpeg: str, plik: Path, a) -> int:
    print("Klip ma juz kanal alfa — tylko przepakowuje.", file=sys.stderr)
    dekoder = ["-c:v", "libvpx-vp9"] if plik.suffix.lower() == ".webm" else []
    if a.webm and a.webm.resolve() != plik.resolve():
        subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-y", *dekoder, "-i", str(plik),
                        "-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-auto-alt-ref", "0",
                        "-b:v", "0", "-crf", "24", "-c:a", "libopus", str(a.webm)], check=True)
    if a.mov:
        subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-y", *dekoder, "-i", str(plik),
                        "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le",
                        "-c:a", "pcm_s16le", str(a.mov)], check=True)
    if a.png:
        subprocess.run([ffmpeg, "-hide_banner", "-loglevel", "error", "-y", *dekoder,
                        "-ss", str(a.czas), "-i", str(plik), "-frames:v", "1",
                        "-pix_fmt", "rgba", str(a.png)], check=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Wytnij sama postac Ewy z klipu (przezroczyste tlo).")
    ap.add_argument("klip", type=Path)
    ap.add_argument("--tlo", default="auto",
                    help="auto (domyslnie), szachownica albo kolor #RRGGBB")
    ap.add_argument("--webm", type=Path, nargs="?", const=Path("ewa.webm"),
                    help="zapisz WebM z alfa (domyslna nazwa ewa.webm)")
    ap.add_argument("--mov", type=Path, nargs="?", const=Path("ewa.mov"),
                    help="zapisz MOV ProRes 4444 z alfa")
    ap.add_argument("--png", type=Path, nargs="?", const=Path("ewa.png"),
                    help="zapisz jeden kadr PNG z alfa")
    ap.add_argument("--sekwencja", type=Path, help="katalog na PNG klatka po klatce")
    ap.add_argument("--czas", type=float, default=None,
                    help="sekunda, z ktorej wziac kadr do --png (domyslnie srodek klipu)")
    ap.add_argument("--bez-dzwieku", dest="bez_dzwieku", action="store_true")
    ap.add_argument("--prog-dol", type=float, default=10.0, help="ponizej: na pewno tlo")
    ap.add_argument("--prog-gora", type=float, default=34.0, help="powyzej: na pewno postac")
    ap.add_argument("--piorko", type=float, default=1.2, help="miekkosc krawedzi w px (0 = brak)")
    ap.add_argument("--podglad", type=Path, help="zapisz JPG z maska nalozona na kadr i zakoncz")
    ap.add_argument("--przytnij", action="store_true",
                    help="przytnij kadr do prostokata postaci (mniejsze pliki, do prezentacji)")
    a = ap.parse_args()

    if not a.klip.exists():
        print(f"Nie ma pliku: {a.klip}", file=sys.stderr)
        return 1
    if not (a.webm or a.mov or a.png or a.sekwencja or a.podglad):
        a.webm, a.png = Path("ewa.webm"), Path("ewa.png")
    ffmpeg = znajdz_ffmpeg()

    if a.tlo == "auto" and ma_alfe(ffmpeg, a.klip):
        if a.czas is None:
            a.czas = 0
        return przepakuj_z_alfa(ffmpeg, a.klip, a)

    kolory: list[np.ndarray] | None = None
    if a.tlo not in ("auto", "szachownica"):
        kolory = [kolor_bgr(a.tlo)]

    audio = None if a.bez_dzwieku else a.klip
    kodery: dict[str, subprocess.Popen] = {}
    if a.sekwencja:
        a.sekwencja.mkdir(parents=True, exist_ok=True)

    obszar = None                                             # prostokat postaci przy --przytnij
    n_klatek, fps = 0, 25.0
    czas_png = a.czas
    zapisano_png = False
    tylko_png = bool(a.png) and not (a.webm or a.mov or a.sekwencja or a.podglad)
    if tylko_png and a.czas:
        n_klatek = int(a.czas * 25)                       # przyblizenie tylko do komunikatow
    for fps, n_wszystkich, klatka in klatki(a.klip, a.czas if tylko_png else None):
        h, w = klatka.shape[:2]
        if kolory is None:
            kolory = kolory_tla(obszar_brzegowy(klatka))
            opis = " / ".join("#%02X%02X%02X" % (int(c[2]), int(c[1]), int(c[0])) for c in kolory)
            print(f"Tlo: {'szachownica' if len(kolory) == 2 else 'jednolite'} ({opis})",
                  file=sys.stderr)
        if czas_png is None:
            czas_png = (n_wszystkich / fps) / 2 if n_wszystkich else 0

        alfa = maska_alfa(klatka, kolory, a.prog_dol, a.prog_gora, a.piorko)
        kolor = usun_kolor_tla_z_krawedzi(klatka, alfa, kolory)

        if a.podglad:
            zielone = np.zeros_like(klatka); zielone[:] = (0, 200, 0)
            a3 = alfa[..., None]
            podglad = (kolor * a3 + zielone * (1 - a3)).astype(np.uint8)
            cv2.imwrite(str(a.podglad), podglad, [cv2.IMWRITE_JPEG_QUALITY, 90])
            print(f"Podglad: {a.podglad} (zielone = przezroczyste). Popraw --prog-dol/--prog-gora "
                  f"jesli maska gubi postac albo zostawia tlo.", file=sys.stderr)
            return 0

        if a.przytnij and obszar is None:
            ys, xs = np.where(alfa > 0.02)
            if len(xs):
                m = 8
                obszar = (max(xs.min() - m, 0), max(ys.min() - m, 0),
                          min(xs.max() + m, w - 1), min(ys.max() + m, h - 1))
                x0, y0, x1, y1 = obszar
                x1 -= (x1 - x0 + 1) % 2; y1 -= (y1 - y0 + 1) % 2   # parzyste wymiary dla koderow
                obszar = (x0, y0, x1, y1)
        bgra = np.dstack([kolor, (alfa * 255).astype(np.uint8)])
        if obszar:
            x0, y0, x1, y1 = obszar
            bgra = bgra[y0:y1 + 1, x0:x1 + 1]
        hh, ww = bgra.shape[:2]

        if not kodery:
            if a.webm:
                kodery["webm"] = koder_ffmpeg(ffmpeg, "webm", a.webm, ww, hh, fps, audio)
            if a.mov:
                kodery["mov"] = koder_ffmpeg(ffmpeg, "mov", a.mov, ww, hh, fps, audio)
        for k in kodery.values():
            k.stdin.write(bgra.tobytes())
        if a.sekwencja:
            cv2.imwrite(str(a.sekwencja / f"ewa_{n_klatek:05d}.png"), bgra)
        if a.png and not zapisano_png and (tylko_png or n_klatek / fps >= czas_png):
            cv2.imwrite(str(a.png), bgra)
            zapisano_png = True
            if not (kodery or a.sekwencja):
                n_klatek += 1
                break                                     # sam kadr — nie ma po co czytac reszty
        n_klatek += 1
        if n_klatek % 50 == 0:
            print(f"  klatka {n_klatek}/{n_wszystkich or '?'}", file=sys.stderr)

    if a.png and not zapisano_png and n_klatek:
        cv2.imwrite(str(a.png), bgra)
    for nazwa, k in kodery.items():
        k.stdin.close()
        if k.wait() != 0:
            print(f"ffmpeg nie zapisal pliku {nazwa}.", file=sys.stderr)
            return 2

    print(f"Gotowe: {n_klatek} klatek, {n_klatek / fps:.1f} s"
          + (f", przyciete do {ww}x{hh}" if obszar else ""), file=sys.stderr)
    for etykieta, sciezka in (("WebM z alfa", a.webm), ("MOV ProRes 4444", a.mov), ("PNG", a.png)):
        if sciezka and sciezka.exists():
            print(f"  {etykieta:<16} {sciezka} ({sciezka.stat().st_size / 1_048_576:.1f} MB)",
                  file=sys.stderr)
    if a.sekwencja:
        print(f"  sekwencja PNG    {a.sekwencja}/ ({n_klatek} plikow)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
