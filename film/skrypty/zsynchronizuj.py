#!/usr/bin/env python3
"""Synchronizacja narracji z nagraniem.

Wejście:
  narracja.txt     — akapity oddzielone pustą linią (jeden akapit = jeden „takt” narracji)
  transkrypt.json  — lista słów z czasem: [{"text": "...", "start": s, "end": s}, ...]
                     (ElevenLabs Scribe; można podać kilka plików i przesunięcia)
  sceny.json       — plik Remotion z listą scen; każda scena ma pole "akapit": numer
                     pierwszego akapitu, od którego zaczyna się scena (1-based)

Wyjście:
  napisy.srt       — napisy pocięte na frazy 6–10 słów, z rzeczywistymi czasami
  sceny.json       — ten sam plik z uzupełnionymi odSek/doSek (granice na początkach akapitów)

Dopasowanie akapit → czas: szukamy w transkrypcie pierwszych 3 słów akapitu
(znormalizowanych), zaczynając od miejsca, gdzie skończył się poprzedni akapit.
"""
from __future__ import annotations
import argparse, json, re, sys, unicodedata
from pathlib import Path


def norm(w: str) -> str:
    w = unicodedata.normalize('NFKD', w.lower())
    return re.sub(r'[^a-ząćęłńóśźż0-9]', '', w)


def wczytaj_slowa(pliki: list[str], przesuniecia: list[float]) -> list[dict]:
    slowa = []
    for p, off in zip(pliki, przesuniecia):
        dane = json.loads(Path(p).read_text(encoding='utf-8'))
        lista = dane.get('words') or dane.get('slowa') or dane
        for w in lista:
            t = w.get('text') or w.get('word') or ''
            if w.get('type', 'word') != 'word' or not norm(t):
                continue
            slowa.append({'t': t, 'n': norm(t), 'od': float(w['start']) + off, 'do': float(w['end']) + off})
    return slowa


def akapity(txt: str) -> list[list[str]]:
    bloki = [b.strip() for b in re.split(r'\n\s*\n', txt) if b.strip()]
    return [[norm(x) for x in re.findall(r"[\wąćęłńóśźż'-]+", b, re.I) if norm(x)] for b in bloki]


def znajdz(slowa: list[dict], wzor: list[str], od: int) -> int | None:
    k = min(3, len(wzor))
    for i in range(od, len(slowa) - k + 1):
        if all(slowa[i + j]['n'] == wzor[j] for j in range(k)):
            return i
    # łagodniej: dwa pierwsze słowa
    for i in range(od, len(slowa) - 1):
        if slowa[i]['n'] == wzor[0] and slowa[i + 1]['n'] == wzor[1 if len(wzor) > 1 else 0]:
            return i
    return None


def srt_czas(s: float) -> str:
    h = int(s // 3600); m = int(s % 3600 // 60); sec = s % 60
    return f"{h:02d}:{m:02d}:{int(sec):02d},{int(round((sec - int(sec)) * 1000)):03d}"


def buduj_srt(slowa: list[dict], maks=9, przerwa=0.9) -> str:
    bloki, biez = [], []
    for w in slowa:
        if biez and (len(biez) >= maks or w['od'] - biez[-1]['do'] > przerwa or biez[-1]['t'].endswith(('.', '?', '!', ':'))):
            bloki.append(biez); biez = []
        biez.append(w)
    if biez: bloki.append(biez)
    out = []
    for i, b in enumerate(bloki, 1):
        tekst = ' '.join(x['t'] for x in b)
        out.append(f"{i}\n{srt_czas(b[0]['od'])} --> {srt_czas(b[-1]['do'] + 0.15)}\n{tekst}\n")
    return '\n'.join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--narracja', required=True)
    ap.add_argument('--transkrypt', nargs='+', required=True)
    ap.add_argument('--przesuniecie', nargs='*', type=float, default=[])
    ap.add_argument('--sceny', required=True)
    ap.add_argument('--srt', required=True)
    ap.add_argument('--koniec', type=float, help='długość nagrania w s (domyślnie koniec ostatniego słowa + 1 s)')
    a = ap.parse_args()

    offs = a.przesuniecie + [0.0] * (len(a.transkrypt) - len(a.przesuniecie))
    slowa = wczytaj_slowa(a.transkrypt, offs)
    if not slowa:
        sys.exit('brak słów w transkrypcie')
    aka = akapity(Path(a.narracja).read_text(encoding='utf-8'))

    czasy, kursor = [], 0
    for i, ak in enumerate(aka, 1):
        if not ak:
            czasy.append(None); continue
        idx = znajdz(slowa, ak, kursor)
        if idx is None:
            print(f"UWAGA: akapit {i} nie znaleziony ({' '.join(ak[:3])}) — interpoluję", file=sys.stderr)
            czasy.append(None)
        else:
            czasy.append(slowa[idx]['od']); kursor = idx + max(1, len(ak) - 2)
    # interpolacja braków
    for i, c in enumerate(czasy):
        if c is None:
            prev = next((czasy[j] for j in range(i - 1, -1, -1) if czasy[j] is not None), 0.0)
            nxt = next((czasy[j] for j in range(i + 1, len(czasy)) if czasy[j] is not None), slowa[-1]['do'])
            czasy[i] = (prev + nxt) / 2
    koniec = a.koniec or (slowa[-1]['do'] + 1.0)

    sceny = json.loads(Path(a.sceny).read_text(encoding='utf-8'))
    lista = sceny['sceny']
    for k, sc in enumerate(lista):
        ak = sc.get('akapit')
        if ak:
            sc['odSek'] = round(max(0.0, czasy[ak - 1] - 0.25), 2)
    for k, sc in enumerate(lista):
        if k + 1 < len(lista):
            sc['doSek'] = lista[k + 1]['odSek']
        else:
            sc['doSek'] = round(koniec, 2)
    lista[0]['odSek'] = 0.0
    Path(a.sceny).write_text(json.dumps(sceny, ensure_ascii=False, indent=2), encoding='utf-8')
    Path(a.srt).write_text(buduj_srt(slowa), encoding='utf-8')
    print(f"akapitów: {len(aka)} · słów: {len(slowa)} · koniec: {koniec:.1f}s · scen: {len(lista)}")
    for i, c in enumerate(czasy, 1):
        print(f"  akapit {i:2d} → {c:7.2f}s")


if __name__ == '__main__':
    main()
