#!/usr/bin/env python3
"""Wstawia postac Ewy (klip awatara) do filmu — na tlo marki, plansze albo ekran aplikacji.

Bierze klip z Ewa (najlepiej z kanalem alfa: WebM/VP9 albo MOV/ProRes 4444 z HeyGen)
i naklada go na tlo: kolor marki, obraz (plansza PNG/JPG) albo film (ekran aplikacji).
Klip na jednolitym tle (np. zielonym) mozna wyciac kluczem chrominancji (--klucz).

Zaleznosci: ffmpeg (systemowy albo `pip install imageio-ffmpeg`); poza tym biblioteka standardowa.

Przyklady:
    python3 wstaw_ewe.py ewa.webm -o film.mp4                         # pelny kadr, tlo fiolet marki
    python3 wstaw_ewe.py ewa.webm --tlo plansza.png --uklad rog        # Ewa w prawym dolnym rogu
    python3 wstaw_ewe.py ewa.webm --tlo plansza.png --uklad rog --kolo # ...w kolku, jak w webinarze
    python3 wstaw_ewe.py ewa.mov  --tlo ekran.mp4  --uklad lewa        # Ewa z lewej, tresc po prawej
    python3 wstaw_ewe.py ewa_zielona.mp4 --klucz "#00FF00" --tlo "#2D1B69"
    python3 wstaw_ewe.py ewa.webm --sprawdz                            # czy klip ma kanal alfa
"""

from __future__ import annotations

import argparse
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path

FIOLET_MARKI = "#2D1B69"
OBRAZY = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
FORMATY_Z_ALFA = ("yuva", "rgba", "argb", "bgra", "abgr", "gbrap", "ya8", "ya16", "pal8")

# skala = wysokosc Ewy jako ulamek wysokosci filmu; margines w px przy 1080p
UKLADY = {
    "pelny": {"skala": 1.00, "opis": "Ewa na srodku, cala wysokosc kadru"},
    "rog":   {"skala": 0.42, "opis": "Ewa mala w prawym dolnym rogu, tresc na calym ekranie"},
    "lewa":  {"skala": 0.90, "opis": "Ewa z lewej, prawa czesc ekranu na tresc"},
    "prawa": {"skala": 0.90, "opis": "Ewa z prawej, lewa czesc ekranu na tresc"},
}


# --- srodowisko ------------------------------------------------------------

def znajdz_ffmpeg() -> str:
    if szukany := shutil.which("ffmpeg"):
        return szukany
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        raise SystemExit(
            "Brak ffmpeg. Zainstaluj systemowy ffmpeg albo: pip install imageio-ffmpeg"
        )


def informacje(ffmpeg: str, plik: Path) -> str:
    """Zwraca naglowek `ffmpeg -i` (ffprobe nie zawsze jest pod reka)."""
    wynik = subprocess.run([ffmpeg, "-hide_banner", "-i", str(plik)],
                           capture_output=True, text=True)
    return wynik.stderr


def opisz_klip(ffmpeg: str, plik: Path) -> dict:
    tekst = informacje(ffmpeg, plik)
    wideo = re.search(r"Stream #\d+:\d+.*?: Video: (\w+).*?, (\w+)[\s(,].*?(\d{2,5})x(\d{2,5})", tekst)
    czas = re.search(r"Duration: (\d+):(\d+):(\d+\.?\d*)", tekst)
    opis = {
        "kodek": wideo.group(1) if wideo else "?",
        "pix_fmt": wideo.group(2) if wideo else "?",
        "szerokosc": int(wideo.group(3)) if wideo else 0,
        "wysokosc": int(wideo.group(4)) if wideo else 0,
        "audio": "Audio:" in tekst,
        "czas": (int(czas.group(1)) * 3600 + int(czas.group(2)) * 60 + float(czas.group(3)))
        if czas else 0.0,
    }
    opis["alfa"] = opis["pix_fmt"].startswith(FORMATY_Z_ALFA)
    if plik.suffix.lower() == ".webm" and opis["kodek"] in ("vp8", "vp9"):
        # naglowek nie mowi o alfie w WebM — rozstrzyga znacznik alpha_mode
        opis["alfa"] = opis["alfa"] or ("alpha_mode" in tekst and re.search(r"alpha_mode\s*:\s*1", tekst) is not None)
    return opis


def sprawdz(ffmpeg: str, plik: Path) -> int:
    o = opisz_klip(ffmpeg, plik)
    print(f"{plik.name}: {o['kodek']} {o['pix_fmt']} {o['szerokosc']}x{o['wysokosc']}, "
          f"{o['czas']:.1f} s, dzwiek: {'tak' if o['audio'] else 'nie'}")
    if o["alfa"]:
        print("Kanal alfa: TAK — klip mozna nalozyc bezposrednio na dowolne tlo.")
        return 0
    print("Kanal alfa: NIE — tlo klipu jest wpalone w obraz.\n"
          "  Jesli tlo jest jednolite (zielone, niebieskie, fiolet marki): podaj --klucz \"#RRGGBB\".\n"
          "  Jesli to szachownica z podgladu: wyeksportuj klip ponownie z HeyGen jako WebM\n"
          "  z przezroczystym tlem (Export -> WebM -> Transparent background).")
    return 3


# --- budowa polecenia ------------------------------------------------------

def kolor(tekst: str) -> str:
    """`#2D1B69` -> `0x2D1B69` (ffmpeg nie lubi krzyzyka w wyrazeniach filtrow)."""
    t = tekst.strip()
    if re.fullmatch(r"#?[0-9a-fA-F]{6}", t):
        return "0x" + t.lstrip("#").upper()
    return t                                            # nazwa koloru, np. green


def wejscie_tla(a, ffmpeg: str) -> tuple[list[str], str | None]:
    """Zwraca argumenty ffmpeg dla tla i (ewentualnie) ostrzezenie."""
    tlo = a.tlo
    sciezka = Path(tlo)
    if sciezka.exists():
        if sciezka.suffix.lower() in OBRAZY:
            return ["-loop", "1", "-framerate", str(a.fps), "-i", str(sciezka)], None
        return ["-stream_loop", "-1", "-i", str(sciezka)], None
    if re.fullmatch(r"#?[0-9a-fA-F]{6}|[a-zA-Z]+", tlo):
        zrodlo = f"color=c={kolor(tlo)}:s={a.szerokosc}x{a.wysokosc}:r={a.fps}"
        return ["-f", "lavfi", "-i", zrodlo], None
    raise SystemExit(f"Nie rozumiem tla `{tlo}`: podaj kolor #RRGGBB, obraz albo film.")


def wejscie_awatara(a) -> list[str]:
    args: list[str] = []
    if a.awatar.suffix.lower() == ".webm":
        # wbudowany dekoder VP9 gubi alfe; libvpx ja zachowuje
        args += ["-c:v", "libvpx-vp9" if not a.vp8 else "libvpx"]
    return args + ["-i", str(a.awatar)]


def filtr(a, ma_alfe: bool) -> str:
    W, H = a.szerokosc, a.wysokosc
    m = a.margines
    h_ewy = int(round(H * a.skala))
    if h_ewy % 2:
        h_ewy += 1

    # tlo: dopasuj do kadru bez znieksztalcen (skaluj i przytnij)
    tlo = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
           f"crop={W}:{H},setsar=1,format=yuv420p[tlo]")

    # Ewa: klucz albo alfa, potem skala; kolko wycina kwadrat wokol glowy
    kroki = ["format=rgba"]
    if a.klucz:
        kroki.append(f"chromakey=color={kolor(a.klucz)}:similarity={a.podobienstwo}:blend={a.mieszanie}")
        if a.klucz.lower() in ("green", "#00ff00", "0x00ff00", "00ff00"):
            kroki.append("despill=type=green")
        elif a.klucz.lower() in ("blue", "#0000ff", "0x0000ff", "0000ff"):
            kroki.append("despill=type=blue")
    if a.kolo:
        kroki.append("crop='min(iw,ih)':'min(iw,ih)':'(iw-min(iw,ih))/2':0")
        kroki.append(f"scale={h_ewy}:{h_ewy}")
        kroki.append("geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)'"
                     ":a='if(lte((X-W/2)*(X-W/2)+(Y-H/2)*(Y-H/2),(W/2)*(W/2)),alpha(X,Y),0)'")
    else:
        kroki.append(f"scale=-2:{h_ewy}")
    ewa = "[1:v]" + ",".join(kroki) + "[ewa]"

    if a.uklad == "pelny":
        x, y = "(W-w)/2", "H-h"
    elif a.uklad == "rog":
        x, y = f"W-w-{m}", f"H-h-{m}"
    elif a.uklad == "lewa":
        x, y = f"{m}", "H-h"
    else:                                               # prawa
        x, y = f"W-w-{m}", "H-h"
    if a.kolo:
        y = f"H-h-{m}"                                  # kolko nie stoi na krawedzi
    if a.x is not None:
        x = str(a.x)
    if a.y is not None:
        y = str(a.y)

    nakladka = f"[tlo][ewa]overlay=x={x}:y={y}:shortest=1:format=auto[v0]"
    czesci = [tlo, ewa, nakladka]
    ostatni = "[v0]"
    if a.napisy:
        styl = "FontName=DejaVu Sans,FontSize=20,PrimaryColour=&H00FFFFFF,OutlineColour=&H80000000,Outline=1,MarginV=40"
        sciezka = str(a.napisy).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
        czesci.append(f"{ostatni}subtitles='{sciezka}':force_style='{styl}'[v1]")
        ostatni = "[v1]"
    czesci.append(f"{ostatni}format=yuv420p[v]")
    return ";".join(czesci)


def polecenie(a, ffmpeg: str, klip: dict) -> list[str]:
    cmd = [ffmpeg, "-hide_banner", "-loglevel", "error", "-stats", "-y"]
    tlo_args, _ = wejscie_tla(a, ffmpeg)
    cmd += tlo_args                                     # wejscie 0: tlo
    cmd += wejscie_awatara(a)                           # wejscie 1: Ewa
    if a.audio:
        cmd += ["-i", str(a.audio)]                     # wejscie 2: osobny dzwiek
    cmd += ["-filter_complex", filtr(a, klip["alfa"]), "-map", "[v]"]
    if a.audio:
        cmd += ["-map", "2:a"]
    elif not a.bez_dzwieku and klip["audio"]:
        cmd += ["-map", "1:a"]
    cmd += ["-c:v", "libx264", "-preset", a.preset, "-crf", str(a.crf),
            "-r", str(a.fps), "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
            "-movflags", "+faststart", "-shortest", str(a.output)]
    return cmd


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Wstaw postac Ewy (klip awatara) do filmu. Skill awatar-ewa-pctp.")
    ap.add_argument("awatar", type=Path, help="klip z Ewa (WebM/MOV z alfa albo MP4 na jednolitym tle)")
    ap.add_argument("-o", "--output", type=Path, default=Path("ewa_film.mp4"))
    ap.add_argument("--tlo", default=FIOLET_MARKI,
                    help=f"kolor #RRGGBB, obraz (plansza) albo film; domyslnie fiolet marki {FIOLET_MARKI}")
    ap.add_argument("--uklad", choices=UKLADY, default="pelny",
                    help="; ".join(f"{k}: {v['opis']}" for k, v in UKLADY.items()))
    ap.add_argument("--kolo", action="store_true", help="Ewa w kolku (kadr wokol glowy)")
    ap.add_argument("--skala", type=float, help="wysokosc Ewy jako ulamek wysokosci filmu (domyslnie wg ukladu)")
    ap.add_argument("--margines", type=int, default=48, help="odstep od krawedzi w px")
    ap.add_argument("--x", type=int, help="reczna pozycja X lewego gornego rogu Ewy")
    ap.add_argument("--y", type=int, help="reczna pozycja Y lewego gornego rogu Ewy")
    ap.add_argument("--szerokosc", type=int, default=1920)
    ap.add_argument("--wysokosc", type=int, default=1080)
    ap.add_argument("--pion", action="store_true", help="1080x1920 pod Reels / TikTok")
    ap.add_argument("--fps", type=int, default=25)
    ap.add_argument("--klucz", help="kolor tla do wyciecia (klucz chrominancji), np. \"#00FF00\"")
    ap.add_argument("--podobienstwo", type=float, default=0.18, help="tolerancja klucza 0-1")
    ap.add_argument("--mieszanie", type=float, default=0.08, help="miekkosc krawedzi klucza 0-1")
    ap.add_argument("--vp8", action="store_true", help="klip WebM jest w VP8, nie VP9")
    ap.add_argument("--audio", type=Path, help="osobna sciezka dzwiekowa (np. MP3 z ElevenLabs)")
    ap.add_argument("--bez-dzwieku", dest="bez_dzwieku", action="store_true")
    ap.add_argument("--napisy", type=Path, help="plik SRT do wypalenia w obrazie")
    ap.add_argument("--crf", type=int, default=18)
    ap.add_argument("--preset", default="medium")
    ap.add_argument("--sprawdz", action="store_true", help="tylko sprawdz klip (alfa, czas) i zakoncz")
    ap.add_argument("--suchy-bieg", dest="suchy", action="store_true",
                    help="pokaz polecenie ffmpeg bez uruchamiania")
    a = ap.parse_args()

    ffmpeg = znajdz_ffmpeg()
    if not a.awatar.exists():
        print(f"Nie ma pliku: {a.awatar}", file=sys.stderr)
        return 1
    if a.sprawdz:
        return sprawdz(ffmpeg, a.awatar)
    if a.pion:
        a.szerokosc, a.wysokosc = 1080, 1920
    if a.skala is None:
        a.skala = UKLADY[a.uklad]["skala"]
    if a.kolo and a.uklad == "pelny":
        a.uklad = "rog"
    if a.audio and not a.audio.exists():
        print(f"Nie ma pliku audio: {a.audio}", file=sys.stderr)
        return 1
    if a.napisy and not a.napisy.exists():
        print(f"Nie ma pliku z napisami: {a.napisy}", file=sys.stderr)
        return 1

    klip = opisz_klip(ffmpeg, a.awatar)
    if not klip["alfa"] and not a.klucz:
        print("Uwaga: klip nie ma kanalu alfa i nie podano --klucz — Ewa zostanie wklejona\n"
              "       jako prostokat razem ze swoim tlem. Sprawdz: --sprawdz", file=sys.stderr)
    if klip["kodek"] not in ("vp8", "vp9") and a.awatar.suffix.lower() == ".webm":
        print("Uwaga: WebM bez VP8/VP9 — alfa moze nie zostac odczytana.", file=sys.stderr)

    cmd = polecenie(a, ffmpeg, klip)
    if a.suchy:
        print(" ".join(shlex.quote(c) for c in cmd))
        return 0

    print(f"Uklad: {a.uklad}{' (kolko)' if a.kolo else ''}, kadr {a.szerokosc}x{a.wysokosc}, "
          f"tlo: {a.tlo}, Ewa: {klip['czas']:.1f} s", file=sys.stderr)
    wynik = subprocess.run(cmd)
    if wynik.returncode != 0 or not a.output.exists():
        print("ffmpeg nie zbudowal filmu — patrz komunikaty wyzej.", file=sys.stderr)
        return 2
    print(f"Film: {a.output} ({a.output.stat().st_size / 1_048_576:.1f} MB)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
