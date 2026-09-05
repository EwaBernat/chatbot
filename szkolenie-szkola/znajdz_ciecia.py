# -*- coding: utf-8 -*-
"""Namierza dokładny moment startu akapitu, odczytując pasek napisów (OCR)."""
import json, os, re, subprocess, sys, unicodedata, difflib

U = '/root/.claude/uploads/4a888e06-1ddb-5c84-9532-6fdda53e415b'
PLIKI = {'M1': f'{U}/37274bcd-M1.mp4', 'M3': f'{U}/98476188-M3.mp4', 'M4': f'{U}/c05a701f-M4.mp4'}
CROP = 'crop=1500:120:210:895,scale=iw*2:ih*2'


def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9 ]', ' ', s).split()


def ocr(mod, t):
    png = f'/tmp/_f.png'
    subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.2f}', '-i', PLIKI[mod],
                    '-frames:v', '1', '-vf', CROP, '-q:v', '2', png, '-y'], check=True)
    r = subprocess.run(['tesseract', png, 'stdout', '-l', 'pol', '--psm', '6'],
                       capture_output=True, text=True)
    txt = [l for l in r.stdout.split('\n') if 'PCTP' not in l and 'EduPlaner' not in l]
    return ' '.join(txt).strip()


def dopasuj(tekst, akapity):
    """Który akapit najlepiej pasuje do odczytanego paska?"""
    w = norm(tekst)
    if len(w) < 3:
        return None, 0.0
    naj, wynik = None, 0.0
    for nr, tresc in akapity:
        a = norm(tresc)
        s = difflib.SequenceMatcher(None, w, a).find_longest_match(0, len(w), 0, len(a)).size
        s = s / max(1, len(w))
        if s > wynik:
            naj, wynik = nr, s
    return naj, wynik


def szukaj(mod, cel, pred, akapity, promien=28):
    """Najwcześniejszy moment, w którym pasek pokazuje akapit `cel`."""
    krok, znalezione = 2.0, None
    t = max(0.5, pred - promien)
    while t <= pred + promien:
        nr, sc = dopasuj(ocr(mod, t), akapity)
        if nr == cel and sc > 0.45:
            znalezione = t
            break
        t += krok
    if znalezione is None:
        return None
    lo, hi = znalezione - krok, znalezione            # zawężenie do 0,2 s
    while hi - lo > 0.2:
        mid = (lo + hi) / 2
        nr, sc = dopasuj(ocr(mod, mid), akapity)
        if nr == cel and sc > 0.45:
            hi = mid
        else:
            lo = mid
    return round(hi, 2)


def main():
    al = json.load(open('alignment.json', encoding='utf-8'))
    CUTS = {'M1': ['08', '12', '21', '25'], 'M3': ['12', '16'], 'M4': ['08']}
    wynik = {}
    for mod, want in CUTS.items():
        ak = [(r['nr'], r['tekst']) for r in al[mod]['plansze']]
        pelne = {r['nr']: r for r in al[mod]['plansze']}
        wynik[mod] = {}
        for nr in want:
            nast = '%02d' % (int(nr) + 1)
            pred = pelne[nr]['koniec_s']
            t = szukaj(mod, nast, pred, ak)
            wynik[mod][nr] = t
            mm = f'{int(t)//60}:{int(t)%60:04.1f}' if t else '—'
            print(f'{mod} po akapicie {nr}: start akapitu {nast} = {t} s ({mm})   '
                  f'[szacunek ze słów: {pred:.1f} s]', flush=True)
    json.dump(wynik, open('cutpoints.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
