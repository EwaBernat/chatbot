#!/usr/bin/env python3
"""
Dopasowuje jedno długie nagranie lektorskie do slajdów filmu.

Wejście
  --dane      src/dane/<czesc>.json   (pola: n, tytul, narracja, audio)
  --srt       transkrypcja nagrania z czasem (SRT)
  --audio     surowe nagranie (m4a/mp3/wav/mp4)
  --wyjscie   katalog na pocięte kwestie (public/audio/<czesc>)

Co robi
  1. Zamienia transkrypcję w strumień słów z przybliżonym czasem każdego słowa.
  2. Dla każdej kwestii szuka w tym strumieniu jej początku — po pierwszych
     słowach scenariusza. Gdy fragment został nagrany kilka razy, wygrywa
     PODEJŚCIE OSTATNIE, więc nieudane starty same wypadają z materiału.
  3. Dosuwa cięcia do najbliższej ciszy, żeby nie uciąć słowa ani nie zostawić
     ogona z następnego zdania.
  4. Czyści dźwięk i zapisuje po jednym pliku na slajd.
  5. Wpisuje do pliku danych napisy z prawdziwym czasem — dzięki temu w filmie
     tekst pojawia się dokładnie ze słowem, które pada.

Wywołanie
  python3 dopasuj-glos.py --dane src/dane/czesc1.json --srt glos/czesc1.srt \
                          --audio nagranie.m4a --wyjscie public/audio/czesc1
"""
import argparse, json, re, subprocess, unicodedata
from difflib import SequenceMatcher
from pathlib import Path

FILTR = ('highpass=f=85,'                       # dudnienie pomieszczenia
         'afftdn=nf=-25,'                       # szum tła
         'acompressor=threshold=-21dB:ratio=3:attack=12:release=260:makeup=2,'
         'loudnorm=I=-16:TP=-1.5:LRA=11')       # równa głośność w całym filmie


def norm(s):
    # ł nie ma formy rozkładalnej, więc podmieniamy je ręcznie — bez tego
    # „zupełności” rozpada się na dwa człony i psuje dopasowanie
    s = s.lower().replace('ł', 'l')
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9 ]', ' ', s).split()


def sekundy(t):
    g, m, reszta = t.split(':')
    s, ms = reszta.split(',')
    return int(g) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def wczytaj_srt(p):
    out = []
    for blok in re.split(r'\n\s*\n', Path(p).read_text(encoding='utf-8').strip()):
        linie = blok.strip().split('\n')
        if len(linie) < 3:
            continue
        od, do = linie[1].split(' --> ')
        out.append({'od': sekundy(od), 'do': sekundy(do), 'tekst': ' '.join(linie[2:]).strip()})
    return out


def strumien_slow(cues):
    """Każde słowo dostaje czas proporcjonalny do swojej pozycji w napisie."""
    slowa = []
    for i, c in enumerate(cues):
        czesci = c['tekst'].split()
        if not czesci:
            continue
        krok = (c['do'] - c['od']) / len(czesci)
        for j, w in enumerate(czesci):
            n = norm(w)
            if n:
                slowa.append({'w': n[0], 'czas': c['od'] + j * krok, 'cue': i})
    return slowa


def znajdz_start(slowa, wzorzec, od_indeksu):
    """Zwraca indeks najlepszego (i najpóźniejszego równie dobrego) dopasowania."""
    dl = len(wzorzec)
    najlepszy, wynik = None, 0.0
    for i in range(od_indeksu, max(od_indeksu, len(slowa) - dl) + 1):
        okno = [s['w'] for s in slowa[i:i + dl]]
        r = SequenceMatcher(None, wzorzec, okno).ratio()
        if r > wynik + 1e-9:
            wynik, najlepszy = r, i
        elif abs(r - wynik) < 1e-9 and r >= 0.72:
            najlepszy = i          # remis → bierzemy późniejsze podejście
    return (najlepszy, wynik) if wynik >= 0.55 else (None, wynik)


def wczytaj_cisze(audio, prog='-34dB', minimum=0.30):
    wynik = subprocess.run(
        ['ffmpeg', '-hide_banner', '-i', str(audio), '-af',
         f'silencedetect=noise={prog}:d={minimum}', '-f', 'null', '-'],
        capture_output=True, text=True).stderr
    cisze, start = [], None
    for linia in wynik.split('\n'):
        m = re.search(r'silence_start: ([0-9.]+)', linia)
        if m:
            start = float(m.group(1))
        m = re.search(r'silence_end: ([0-9.]+)', linia)
        if m and start is not None:
            cisze.append((start, float(m.group(1))))
            start = None
    return cisze


def dosun_start(t, cisze, luz=1.4):
    najlepsze = t - 0.18
    for a, b in cisze:
        if t - luz <= b <= t + 0.05:
            najlepsze = max(a + 0.05, b - 0.15)
    return max(0.0, najlepsze)


def dosun_koniec(t, cisze, luz=1.4):
    najlepsze = t + 0.28
    for a, b in cisze:
        if t - 0.05 <= a <= t + luz:
            return min(b - 0.05, a + 0.35)
    return najlepsze


def scal_napisy(cues, od, do):
    """Łączy napisy w całe zdania — inaczej linia urywa się w środku frazy."""
    napisy, bufor = [], None
    for c in cues:
        pokrycie = min(c['do'], do) - max(c['od'], od)
        if pokrycie <= 0 or pokrycie < 0.5 * (c['do'] - c['od']):
            continue
        if bufor is None:
            bufor = {'t': c['tekst'], 'od': c['od'], 'do': c['do']}
        elif len(bufor['t']) + len(c['tekst']) > 130:
            napisy.append(bufor)
            bufor = {'t': c['tekst'], 'od': c['od'], 'do': c['do']}
        else:
            bufor['t'] = (bufor['t'] + ' ' + c['tekst']).strip()
            bufor['do'] = c['do']
        if bufor and bufor['t'].rstrip().endswith(('.', '!', '?', ':', '”', '…')) and len(bufor['t']) >= 45:
            napisy.append(bufor)
            bufor = None
    if bufor:
        if napisy and len(bufor['t']) < 28:
            napisy[-1]['t'] += ' ' + bufor['t']
            napisy[-1]['do'] = bufor['do']
        else:
            napisy.append(bufor)
    return [{'t': n['t'], 'od': round(n['od'] - od, 2), 'do': round(n['do'] - od, 2)} for n in napisy]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dane', required=True)
    ap.add_argument('--srt', required=True)
    ap.add_argument('--audio', required=True)
    ap.add_argument('--wyjscie', required=True)
    ap.add_argument('--slow-wzorca', type=int, default=6,
                    help='ile pierwszych słów kwestii służy do odnalezienia jej w nagraniu')
    ap.add_argument('--bez-ciecia', action='store_true', help='tylko policz granice, nie zapisuj plików')
    a = ap.parse_args()

    dane = json.loads(Path(a.dane).read_text(encoding='utf-8'))
    cues = wczytaj_srt(a.srt)
    slowa = strumien_slow(cues)
    cisze = wczytaj_cisze(a.audio)
    wyjscie = Path(a.wyjscie)
    wyjscie.mkdir(parents=True, exist_ok=True)

    # 1. znajdź początek i koniec każdej kwestii
    surowe, konce, kursor = [], [], 0
    for s in dane:
        slowa_kwestii = norm(s['narracja'])
        idx, jakosc = znajdz_start(slowa, slowa_kwestii[:a.slow_wzorca], kursor)
        if idx is None:
            print(f'  ! kwestia {s["n"]:02d}: nie znalazłam w nagraniu (dopasowanie {jakosc:.2f})')
            surowe.append(None); konce.append(None)
            continue
        surowe.append(slowa[idx]['czas'])
        # koniec: ostatnie słowa tej samej kwestii, szukane od jej początku
        ogon = slowa_kwestii[-5:]
        kidx, kjakosc = znajdz_start(slowa, ogon, idx + max(2, len(slowa_kwestii) // 3))
        # koniec bierzemy z napisu, w którym padło ostatnie słowo kwestii —
        # dzięki temu nieudane podejście nagrane zaraz potem zostaje poza kadrem
        if kidx is not None:
            ostatnie = slowa[min(kidx + len(ogon) - 1, len(slowa) - 1)]
            konce.append(cues[ostatnie['cue']]['do'])
        else:
            konce.append(None)
        kursor = idx + max(3, a.slow_wzorca // 2)

    koniec_nagrania = cues[-1]['do'] if cues else 0
    starty = [dosun_start(t, cisze) if t is not None else None for t in surowe]

    # 2. potnij
    for i, s in enumerate(dane):
        if starty[i] is None:
            continue
        nastepny = next((t for t in starty[i + 1:] if t is not None), koniec_nagrania + 0.4)
        od = starty[i]
        kandydat = konce[i] + 0.25 if konce[i] else nastepny - 0.35
        do = min(dosun_koniec(min(kandydat, nastepny - 0.35), cisze), nastepny - 0.05)
        plik = wyjscie / f'{s["n"]:02d}.mp3'
        if not a.bez_ciecia:
            subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
                            '-ss', f'{od:.3f}', '-to', f'{do:.3f}', '-i', str(a.audio),
                            '-af', FILTR, '-ac', '1', '-ar', '48000', '-b:a', '128k', str(plik)],
                           check=True)
        s['napisy'] = scal_napisy(cues, od, do)
        if s['napisy']:
            s['narracja'] = ' '.join(n['t'] for n in s['napisy'])
        print(f'{s["n"]:02d}  {od:7.2f} → {do:7.2f}  ({do - od:5.2f} s)  {s["napisy"][0]["t"][:46] if s["napisy"] else ""}')

    Path(a.dane).write_text(json.dumps(dane, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'\nZapisano napisy z czasem nagrania do {a.dane}')


main()
