#!/usr/bin/env python3
"""
Tnie jedno długie nagranie lektorskie na osobne pliki dla każdego slajdu.

Wejście:  nagranie-oryginal.m4a  +  glos/transkrypcja-<czesc>.srt  +  glos/cisze.txt
Wyjście:  public/audio/<czesc>/01.mp3 … 25.mp3 (+ intro.mp3)
          oraz napisy z prawdziwym czasem, wpisane do src/dane/<czesc>.json

Granice kwestii wynikają z transkrypcji, a punkty cięcia są dosuwane do
najbliższej ciszy — dzięki temu żadne słowo nie jest ucięte, a nieudane
podejścia (powtórzone fragmenty) po prostu wypadają z materiału.
"""
import json, re, subprocess, sys
from pathlib import Path

KAT = Path(__file__).resolve().parent.parent
CZESC = sys.argv[1] if len(sys.argv) > 1 else 'czesc1'
ZRODLO = KAT / (sys.argv[2] if len(sys.argv) > 2 else 'glos/nagranie-studio.m4a')

# zakresy numerów napisów przypadające na kolejne slajdy (od 1 do 25)
ZAKRESY = {
 'czesc1': [(2,4),(5,9),(10,13),(14,18),(19,21),(22,26),(27,31),(32,38),(39,42),(43,47),
            (48,52),(53,55),(56,60),(61,64),(65,71),(72,77),(78,82),(83,86),(87,91),(92,95),
            (96,98),(99,102),(103,110),(111,115),(116,123)],
}
INTRO = {'czesc1': (1,1)}   # zapowiedź czytana przed pierwszym slajdem

def sekundy(t):
    g,m,reszta = t.split(':')
    s,ms = reszta.split(',')
    return int(g)*3600 + int(m)*60 + int(s) + int(ms)/1000

def wczytaj_srt(p):
    bloki = re.split(r'\n\s*\n', p.read_text(encoding='utf-8').strip())
    out = {}
    for b in bloki:
        linie = b.strip().split('\n')
        if len(linie) < 3: continue
        nr = int(linie[0])
        od, do = linie[1].split(' --> ')
        out[nr] = {'od': sekundy(od), 'do': sekundy(do), 'tekst': ' '.join(linie[2:]).strip()}
    return out

def wczytaj_cisze(p):
    cisze, start = [], None
    for linia in p.read_text(encoding='utf-8').split('\n'):
        if linia.startswith('S '): start = float(linia[2:])
        elif linia.startswith('E ') and start is not None:
            cisze.append((start, float(linia[2:]))); start = None
    return cisze

def dosun_start(t, cisze, luz=1.4):
    """Cofa początek do końca ciszy tuż przed mową — z odrobiną powietrza."""
    najlepsze = t - 0.18
    for a, b in cisze:
        if t - luz <= b <= t + 0.05:
            najlepsze = max(a + 0.05, b - 0.15)
    return max(0, najlepsze)

def dosun_koniec(t, cisze, luz=1.4):
    """Przesuwa koniec w głąb ciszy po ostatnim słowie."""
    najlepsze = t + 0.28
    for a, b in cisze:
        if t - 0.05 <= a <= t + luz:
            najlepsze = min(b - 0.05, a + 0.35)
            break
    return najlepsze

# Źródłem jest nagranie po Descript Studio Sound (szum tła spadł z -56 dB do
# -75 dB, znikło pogłosowe „pudło” pokoju). Studio Sound nie zmienia jednak
# barwy — nagranie z telefonu pozostaje ciemne i „zamulone”:
# pasmo 2–8 kHz, które decyduje o zrozumiałości spółgłosek, leży 13–15 dB
# niżej niż niskie średnie. Dlatego zamiast mocnego odszumiania (które
# dodatkowo tłumiło górę) obniżamy mulisty zakres i podnosimy obecność.
FILTR = ('highpass=f=90,'                        # dudnienie i stukot stołu
         'equalizer=f=300:t=q:w=1.0:g=-4.5,'     # odmulenie
         'equalizer=f=1900:t=q:w=0.8:g=5,'       # zrozumiałość
         'equalizer=f=3400:t=q:w=0.9:g=5,'       # wyrazistość spółgłosek
         'treble=g=5:f=8000:width_type=q:w=0.7,' # powietrze
         'deesser=i=0.35,'                       # syczące „s” po podbiciu góry
         'acompressor=threshold=-20dB:ratio=2.6:attack=15:release=250:makeup=2,'
         'alimiter=limit=0.94,'
         'loudnorm=I=-16:TP=-1.5:LRA=9')         # równa głośność w całym filmie

def tnij(od, do, cel):
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y',
                    '-ss', f'{od:.3f}', '-to', f'{do:.3f}', '-i', str(ZRODLO),
                    '-af', FILTR, '-ac','1','-ar','48000','-c:a','pcm_s16le', str(cel)], check=True)

def main():
    srt = wczytaj_srt(KAT / 'glos' / f'transkrypcja-{CZESC}.srt')
    cisze = wczytaj_cisze(KAT / 'glos' / 'cisze.txt')
    dane = json.loads((KAT / 'src' / 'dane' / f'{CZESC}.json').read_text(encoding='utf-8'))
    wyjscie = KAT / 'public' / 'audio' / CZESC
    wyjscie.mkdir(parents=True, exist_ok=True)

    if CZESC in INTRO:
        a, b = INTRO[CZESC]
        od = dosun_start(srt[a]['od'], cisze); do = dosun_koniec(srt[b]['do'], cisze)
        tnij(od, do, wyjscie / 'intro.wav')
        print(f'intro          {od:7.2f} → {do:7.2f}  ({do-od:5.2f} s)  {srt[a]["tekst"][:40]}')

    zakresy = ZAKRESY[CZESC]
    starty = [dosun_start(srt[a]['od'], cisze) for a, _ in zakresy]

    for i, (a, b) in enumerate(zakresy, start=1):
        od = starty[i-1]
        do = dosun_koniec(srt[b]['do'], cisze)
        # kwestie nie mogą na siebie zachodzić — tam, gdzie zdania płyną bez pauzy,
        # cięcie wypada tuż przed pierwszym słowem następnej kwestii
        if i < len(zakresy):
            do = min(do, starty[i] - 0.05)
        plik = wyjscie / f'{i:02d}.wav'
        tnij(od, do, plik)

        # napisy scalamy do pełnych zdań — inaczej linia urywa się w środku frazy
        napisy, bufor = [], None
        for nr in range(a, b + 1):
            c = srt[nr]
            if bufor is None:
                bufor = {'t': c['tekst'], 'od': c['od'], 'do': c['do']}
            else:
                bufor['t'] = (bufor['t'] + ' ' + c['tekst']).strip()
                bufor['do'] = c['do']
            zamkniete = bufor['t'].rstrip().endswith(('.', '!', '?', ':', '”', '…'))
            if (zamkniete and len(bufor['t']) >= 45) or len(bufor['t']) >= 135:
                napisy.append(bufor); bufor = None
        if bufor is not None:
            if napisy and len(bufor['t']) < 28:
                napisy[-1]['t'] += ' ' + bufor['t']
                napisy[-1]['do'] = bufor['do']
            else:
                napisy.append(bufor)
        napisy = [{'t': n['t'], 'od': round(n['od'] - od, 2), 'do': round(n['do'] - od, 2)} for n in napisy]
        dane[i-1]['napisy'] = napisy
        dane[i-1]['narracja'] = ' '.join(c['t'] for c in napisy)
        print(f'{i:02d}  {plik.name}  {od:7.2f} → {do:7.2f}  ({do-od:5.2f} s)  {napisy[0]["t"][:40]}')

    (KAT / 'src' / 'dane' / f'{CZESC}.json').write_text(
        json.dumps(dane, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'\nZaktualizowano src/dane/{CZESC}.json — napisy mają teraz czas z nagrania.')

main()
