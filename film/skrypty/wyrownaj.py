#!/usr/bin/env python3
"""Wyrównanie narracji do nagrania na podstawie pauz.

Nie mamy sygnatur czasu słów, mamy za to nagranie i tekst. Lektor robi
wyraźne pauzy na końcach zdań i dłuższe między akapitami, więc:

1. ffmpeg silencedetect → lista pauz (początek, koniec, długość),
2. dla każdego zdania liczymy przewidywany koniec proporcjonalnie do liczby
   znaków (tempo lektora jest w przybliżeniu stałe),
3. koniec zdania przyciągamy do najbliższej pauzy w oknie ±okno sekund,
   rosnąco, bez cofania,
4. granica sceny = początek pierwszego zdania akapitu wskazanego w polu "akapit".

Wyjście: napisy.srt (zdanie = napis; długie zdania dzielone na frazy)
oraz uzupełnione odSek/doSek w pliku scen Remotion.

Użycie:
  wyrownaj.py --audio M1.mp3 --narracja M1.txt --sceny public/M1.json --srt public/audio/M1.srt
"""
from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path

FFMPEG = Path(__file__).resolve().parents[1] / 'remotion/node_modules/@remotion/compositor-linux-x64-gnu/ffmpeg'


def dlugosc(audio: str) -> float:
    out = subprocess.run([str(FFMPEG), '-i', audio], capture_output=True, text=True).stderr
    m = re.search(r'Duration: (\d+):(\d+):(\d+\.\d+)', out)
    return int(m[1]) * 3600 + int(m[2]) * 60 + float(m[3])


def pauzy(audio: str, prog='-32dB', min_d=0.28) -> list[tuple[float, float]]:
    out = subprocess.run(
        [str(FFMPEG), '-i', audio, '-af', f'silencedetect=noise={prog}:d={min_d}', '-f', 'null', '-'],
        capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]
    ends = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', out)]
    return list(zip(starts, ends[:len(starts)]))


def zdania(akapit: str) -> list[str]:
    # dzielimy po . ? ! oraz dwukropku kończącym myśl; zachowujemy znak
    czesci = re.split(r'(?<=[.?!])\s+', akapit.strip())
    return [c.strip() for c in czesci if c.strip()]


def frazy(zdanie: str, maks=11) -> list[str]:
    slowa = zdanie.split()
    if len(slowa) <= maks:
        return [zdanie]
    # dziel po przecinkach, jeśli są; inaczej równo
    kawalki, biez = [], []
    for w in slowa:
        biez.append(w)
        if (w.endswith(',') and len(biez) >= 5) or len(biez) >= maks:
            kawalki.append(' '.join(biez)); biez = []
    if biez:
        if kawalki and len(biez) < 3:
            kawalki[-1] += ' ' + ' '.join(biez)
        else:
            kawalki.append(' '.join(biez))
    return kawalki


def srt_t(s: float) -> str:
    h = int(s // 3600); m = int(s % 3600 // 60); sec = s % 60
    return f"{h:02d}:{m:02d}:{int(sec):02d},{int(round((sec - int(sec)) * 1000)) % 1000:03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--audio', required=True)
    ap.add_argument('--narracja', required=True)
    ap.add_argument('--sceny', required=True)
    ap.add_argument('--srt', required=True)
    ap.add_argument('--okno', type=float, default=2.2)
    ap.add_argument('--cisza-start', type=float, default=0.0, help='sekundy ciszy przed pierwszym słowem')
    a = ap.parse_args()

    calosc = dlugosc(a.audio)
    p = pauzy(a.audio)
    tekst = Path(a.narracja).read_text(encoding='utf-8')
    akapity = [b.strip() for b in re.split(r'\n\s*\n', tekst) if b.strip()]

    # lista zdań z przypisaniem do akapitu
    lista = []
    for ai, ak in enumerate(akapity, 1):
        for z in zdania(ak):
            lista.append({'akapit': ai, 'tekst': z, 'znaki': len(z)})
    suma = sum(z['znaki'] for z in lista)
    # przybliżony czas mówienia = całość minus suma pauz (pauzy dłuższe niż 0,28 s)
    czas_pauz = sum(e - s for s, e in p)
    mowa = calosc - czas_pauz - a.cisza_start
    tempo = mowa / suma  # s na znak

    # przewidywane końce zdań, potem przyciąganie do pauz
    t = a.cisza_start
    konce_pauz = [e for s, e in p]
    starty_pauz = [s for s, e in p]
    uzyte = 0
    for z in lista:
        z['od'] = t
        przew = t + z['znaki'] * tempo
        # najbliższa pauza zaczynająca się w oknie wokół przewidywanego końca, nie wcześniej niż ostatnio użyta
        kand = [(abs(starty_pauz[i] - przew), i) for i in range(uzyte, len(p)) if abs(starty_pauz[i] - przew) <= a.okno and starty_pauz[i] > t + 0.4]
        if kand:
            _, i = min(kand)
            z['do'] = starty_pauz[i]
            t = konce_pauz[i]
            uzyte = i + 1
        else:
            z['do'] = przew
            t = przew
    lista[-1]['do'] = min(lista[-1]['do'], calosc)

    # SRT
    out, n = [], 1
    for z in lista:
        fr = frazy(z['tekst'])
        dl = (z['do'] - z['od']) / max(1, sum(len(f) for f in fr))
        s = z['od']
        for f in fr:
            e = s + len(f) * dl
            out.append(f"{n}\n{srt_t(s)} --> {srt_t(max(s + 0.3, e))}\n{f}\n")
            n += 1; s = e
    Path(a.srt).write_text('\n'.join(out), encoding='utf-8')

    # sceny
    pocz = {}
    for z in lista:
        pocz.setdefault(z['akapit'], z['od'])
    sc = json.loads(Path(a.sceny).read_text(encoding='utf-8'))
    L = sc['sceny']
    for s_ in L:
        if 'akapit' in s_:
            s_['odSek'] = round(max(0.0, pocz.get(s_['akapit'], s_['odSek']) - 0.15), 2)
    L[0]['odSek'] = 0.0
    for i, s_ in enumerate(L):
        s_['doSek'] = L[i + 1]['odSek'] if i + 1 < len(L) else round(calosc, 2)
    Path(a.sceny).write_text(json.dumps(sc, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"nagranie {calosc:.1f}s · pauz {len(p)} · zdań {len(lista)} · tempo {1/tempo:.1f} zn/s · przyciągnięto {uzyte} końców")
    for ai in sorted(pocz):
        print(f"  akapit {ai:2d} → {pocz[ai]:7.2f}s")


if __name__ == '__main__':
    main()
