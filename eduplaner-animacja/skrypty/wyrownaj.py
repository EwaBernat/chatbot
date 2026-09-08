#!/usr/bin/env python3
"""Dopasowuje zdania narracji do nagrania i składa public/film.json.

Wykrywa pauzy w MP3 (ffmpeg silencedetect), a potem programowaniem dynamicznym
przypisuje kolejne zdania do kolejnych odcinków mowy tak, żeby tempo (sekundy
na sylabę) było jak najrówniejsze. Granice scen i napisów wychodzą z nagrania,
nie z ręcznych szacunków.

Użycie (z katalogu eduplaner-animacja):
    python3 skrypty/wyrownaj.py            # public/narracja.mp3 + scenariusz → public/film.json
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

KATALOG = Path(__file__).resolve().parent.parent
MP3 = KATALOG / "public" / "narracja.mp3"
SCENARIUSZ = KATALOG / "public" / "scenariusz-narracji.txt"
FILM = KATALOG / "public" / "film.json"
FFMPEG = KATALOG / "node_modules" / "@remotion" / "compositor-linux-x64-gnu" / "ffmpeg"
FFPROBE = FFMPEG.with_name("ffprobe")

# Scena → zakres zdań (indeksy w kolejności czytania) i nazwane znaczniki (indeks zdania).
SCENY = [
    ("intro", 0, 2, {"szafa": 1, "nazwa": 2}),
    ("ekran", 3, 6, {"wyliczanka": 5, "klik": 6}),
    ("druk1", 7, 11, {"placowka": 9, "zasila": 11}),
    ("druk2", 12, 14, {"karta": 13, "klik": 14}),
    ("druk3", 15, 18, {"tabela": 16, "zrodla": 17}),
    ("druk4", 19, 22, {"dostepnosc": 20, "gotowe": 21}),
    ("final", 23, 28, {"hasla": 24, "czas": 25, "nazwa": 26, "prawo": 28}),
]


def zdania(tekst: str) -> list[str]:
    """Dzieli tekst na zdania; trzyma razem krótkie okrzyki typu „Szybciej… spokojniej… pewniej."."""
    czysty = re.sub(r"\[[^\]]*\]\s*", "", tekst)  # znaczniki reżyserskie dla eleven_v3
    czysty = re.sub(r"\s+", " ", czysty).strip()
    kawalki = re.split(r"(?<=[.!?])\s+(?=[A-ZĄĆĘŁŃÓŚŹŻ])", czysty)
    wynik: list[str] = []
    for k in kawalki:
        # „Mniej dokumentów. Więcej edukacji." — sklej dwuwyrazowe hasła w jeden napis
        if wynik and len(k.split()) <= 2 and len(wynik[-1].split()) <= 2:
            wynik[-1] += " " + k
        else:
            wynik.append(k)
    return wynik


def sylaby(s: str) -> float:
    s = s.replace("EduPlaner", "eduplaner").replace(" A ", " aa ").replace(" B ", " be ")
    n = len(re.findall(r"[aeiouyąęó]", s.lower()))
    return n + s.count(".") * 0.8 + s.count(",") * 0.4 + s.count(":") * 0.4 + s.count("…") * 1.2 + s.count("–") * 0.5 + s.count("?") * 0.8


def odcinki_mowy() -> tuple[list[tuple[float, float]], float]:
    dl = float(subprocess.run([FFPROBE, "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", MP3], capture_output=True, text=True, check=True).stdout)
    log = subprocess.run([FFMPEG, "-hide_banner", "-i", MP3, "-af", "silencedetect=noise=-32dB:d=0.15", "-f", "null", "-"], capture_output=True, text=True).stderr
    cisze = [(float(m.group(1)) - float(m.group(2)), float(m.group(1))) for m in re.finditer(r"silence_end: ([0-9.]+) \| silence_duration: ([0-9.]+)", log)]
    odc, prev = [], 0.0
    for start, end in cisze:
        if start - prev > 0.05:
            odc.append((prev, start))
        prev = end
    if dl - prev > 0.05:
        odc.append((prev, dl))
    return odc, dl


def dopasuj(zd: list[str], odc: list[tuple[float, float]]) -> list[tuple[float, float, str]]:
    w = [sylaby(z) for z in zd]
    S, N = len(odc), len(zd)
    if S < N:
        raise SystemExit(f"Za mało pauz w nagraniu ({S}) na {N} zdań — obniż próg ciszy.")
    tempo = sum(e - b for b, e in odc) / sum(w)
    INF = float("inf")
    dp = [[INF] * (S + 1) for _ in range(N + 1)]
    par = [[-1] * (S + 1) for _ in range(N + 1)]
    dp[0][0] = 0.0
    for i in range(1, N + 1):
        for j in range(i, S + 1):
            for k in range(i - 1, j):
                if dp[i - 1][k] == INF:
                    continue
                dur = odc[j - 1][1] - odc[k][0]
                c = dp[i - 1][k] + (dur / w[i - 1] - tempo) ** 2 * w[i - 1]
                if c < dp[i][j]:
                    dp[i][j], par[i][j] = c, k
    j, out = S, []
    for i in range(N, 0, -1):
        k = par[i][j]
        out.append((odc[k][0], odc[j - 1][1], zd[i - 1]))
        j = k
    return out[::-1]


def main() -> None:
    zd = zdania(SCENARIUSZ.read_text(encoding="utf-8"))
    odc, dl = odcinki_mowy()
    wyr = dopasuj(zd, odc)
    ostatni = max(i for _, _, i, _ in SCENY)
    if len(zd) != ostatni + 1:
        for i, z in enumerate(zd):
            print(f"{i:2d} {z}")
        raise SystemExit(f"Scenariusz ma {len(zd)} zdań, a mapa scen oczekuje {ostatni + 1}. Popraw SCENY w tym skrypcie.")
    for (a, b, z) in wyr:
        print(f"{a:6.2f} {b:6.2f} {(b - a) / sylaby(z):.3f} s/syl  {z}")
    napisy = [{"odSek": round(a, 2), "doSek": round(b + 0.15, 2), "tekst": z} for a, b, z in wyr]
    sceny = []
    for n, (id_, od, do, zn) in enumerate(SCENY):
        start = 0.0 if n == 0 else round((wyr[od][0] + wyr[od - 1][1]) / 2, 2)  # w środku pauzy
        koniec = round(dl, 2) if n == len(SCENY) - 1 else round((wyr[do][1] + wyr[do + 1][0]) / 2, 2)
        sceny.append({"id": id_, "odSek": start, "doSek": koniec, "znaczniki": {k: round(wyr[v][0], 2) for k, v in zn.items()}})
    FILM.write_text(json.dumps({"audio": "narracja.mp3", "napisy": napisy, "sceny": sceny}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nZapisano {FILM} — {len(napisy)} napisów, {len(sceny)} scen, {dl:.1f} s")


if __name__ == "__main__":
    main()
