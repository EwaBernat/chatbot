# -*- coding: utf-8 -*-
"""
Wkleja wstawki lektorskie do modułów filmu (M1, M3, M4) w punktach cięcia
namierzonych OCR-em na pasku napisów.

    python3 zloz_wstawki.py --audio katalog_z_mp3 --zrodla katalog_z_mp4 --wyjscie gotowe/

Dla każdej wstawki potrzebny jest plik <id>.mp3 (np. M1_1.mp3) nagrany głosem
autorki. Bez niego skrypt pomija wstawkę i mówi o tym wprost — nie podstawia
cudzego głosu ani ciszy.
"""
import argparse, asyncio, json, math, os, shutil, subprocess, sys, tempfile

FPS = 30
W, H = 1920, 1080
SLOW_NA_PASEK = 11          # ile słów mieści się w dolnym pasku napisów


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def dlugosc(plik):
    r = sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'csv=p=0', plik])
    return float(r.stdout.strip())


def paski(tekst):
    """Dzieli narrację na porcje mieszczące się w pasku napisów."""
    slowa, out, buf = tekst.split(), [], []
    for w in slowa:
        buf.append(w)
        if len(buf) >= SLOW_NA_PASEK and w.endswith(('.', ',', ':', '?', '!')):
            out.append(' '.join(buf)); buf = []
        elif len(buf) >= SLOW_NA_PASEK + 5:
            out.append(' '.join(buf)); buf = []
    if buf:
        out.append(' '.join(buf))
    return out


def segment_wstawki(w, modul_etykieta, mp3, katalog):
    """Buduje wideo wstawki: plansza + przewijany pasek napisów + głos."""
    czas = dlugosc(mp3)
    porcje = paski(w['narracja'])
    wagi = [len(p.split()) for p in porcje]
    suma = sum(wagi)
    zadania, trwania = [], []
    for i, (p, waga) in enumerate(zip(porcje, wagi)):
        zadania.append({'modul': modul_etykieta, 'tytul': w['tytul'],
                        'punkty': w['punkty'], 'napis': p, 'plik': f'{w["id"]}_{i:02d}.png'})
        trwania.append(czas * waga / suma)
    import plansza
    asyncio.run(plansza.renderuj(zadania, katalog))

    lista = os.path.join(katalog, f'{w["id"]}.txt')
    with open(lista, 'w', encoding='utf-8') as f:
        for z, d in zip(zadania, trwania):
            f.write(f"file '{os.path.abspath(os.path.join(katalog, z['plik']))}'\nduration {d:.3f}\n")
        f.write(f"file '{os.path.abspath(os.path.join(katalog, zadania[-1]['plik']))}'\n")

    out = os.path.join(katalog, f'{w["id"]}.mp4')
    sh(['ffmpeg', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lista, '-i', mp3,
        '-c:v', 'libx264', '-preset', 'medium', '-crf', '23', '-pix_fmt', 'yuv420p',
        '-r', str(FPS), '-vf', f'scale={W}:{H},format=yuv420p',
        '-c:a', 'aac', '-b:a', '128k', '-ar', '48000', '-ac', '2',
        '-shortest', '-movflags', '+faststart', out, '-y'])
    return out, czas


def fragment(zrodlo, od, do, plik):
    cmd = ['ffmpeg', '-v', 'error', '-i', zrodlo, '-ss', f'{od:.3f}']
    if do is not None:
        cmd += ['-to', f'{do:.3f}']
    cmd += ['-c:v', 'libx264', '-preset', 'medium', '-crf', '23', '-pix_fmt', 'yuv420p',
            '-r', str(FPS), '-vf', f'scale={W}:{H},format=yuv420p',
            '-c:a', 'aac', '-b:a', '128k', '-ar', '48000', '-ac', '2',
            '-movflags', '+faststart', plik, '-y']
    sh(cmd)
    return plik


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', default='wstawki_manifest.json')
    ap.add_argument('--audio', required=True, help='katalog z plikami <id>.mp3')
    ap.add_argument('--zrodla', required=True, help='katalog z M1.mp4, M3.mp4, M4.mp4')
    ap.add_argument('--wyjscie', default='gotowe')
    ap.add_argument('--roboczy', default=None)
    a = ap.parse_args()

    man = json.load(open(a.manifest, encoding='utf-8'))
    os.makedirs(a.wyjscie, exist_ok=True)
    rob = a.roboczy or tempfile.mkdtemp(prefix='wstawki_')
    os.makedirs(rob, exist_ok=True)

    braki = []
    for mod, meta in man['zrodla'].items():
        zrodlo = os.path.join(a.zrodla, meta['plik'])
        if not os.path.exists(zrodlo):
            print(f'[{mod}] BRAK PLIKU ŹRÓDŁOWEGO: {zrodlo}'); continue
        wstawki = sorted([w for w in man['wstawki'] if w['modul'] == mod],
                         key=lambda x: x['ciecie_s'])
        gotowe, pominiete = [], []
        for w in wstawki:
            mp3 = os.path.join(a.audio, f'{w["id"]}.mp3')
            if os.path.exists(mp3):
                gotowe.append((w, mp3))
            else:
                pominiete.append(w['id']); braki.append(w['id'])
        if pominiete:
            print(f'[{mod}] brak nagrań: {", ".join(pominiete)} — te wstawki pomijam')
        if not gotowe:
            print(f'[{mod}] nic do wklejenia, film zostaje bez zmian'); continue

        czesci, poprzedni = [], 0.0
        for i, (w, mp3) in enumerate(gotowe):
            czesci.append(fragment(zrodlo, poprzedni, w['ciecie_s'],
                                   os.path.join(rob, f'{mod}_baza{i}.mp4')))
            seg, dl = segment_wstawki(w, meta['modul'], mp3, rob)
            czesci.append(seg)
            print(f'  + {w["id"]} @ {w["ciecie_s"]:.2f}s  ({dl:.1f}s materiału)')
            poprzedni = w['ciecie_s']
        czesci.append(fragment(zrodlo, poprzedni, None,
                               os.path.join(rob, f'{mod}_baza_koniec.mp4')))

        lista = os.path.join(rob, f'{mod}_concat.txt')
        with open(lista, 'w', encoding='utf-8') as f:
            for c in czesci:
                f.write(f"file '{os.path.abspath(c)}'\n")
        out = os.path.join(a.wyjscie, f'{mod}_po_audycie.mp4')
        sh(['ffmpeg', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', lista,
            '-c', 'copy', '-movflags', '+faststart', out, '-y'])
        print(f'[{mod}] {meta["dlugosc"]:.1f}s → {dlugosc(out):.1f}s   {out}')

    if braki:
        print('\nNIE ZŁOŻONO w całości — brakuje nagrań: ' + ', '.join(braki))
        print('Nagrania muszą być głosem autorki. Skrypt nie podstawia innego głosu.')


if __name__ == '__main__':
    main()
