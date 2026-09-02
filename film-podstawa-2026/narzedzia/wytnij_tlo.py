#!/usr/bin/env python3
"""Wycina szachownicę z klatek awatara i zapisuje film z kanałem alfa.

HeyGen wyeksportował awatara „z przezroczystością", ale w kodeku bez alfy —
przezroczystość jest wypalona w pikselach jako szara szachownica. Zwykły klucz
luminancji tu nie zadziała: bluzka ma luminancję 251, szachownica 250.

Dlatego tło rozpoznajemy inaczej: piksel jest tłem, gdy jest jasny i neutralny
ORAZ należy do obszaru stykającego się z krawędzią kadru. Bluzka jest zamknięta
marynarką, więc krawędzi nie dotyka i zostaje nietknięta — biała, taka jak jest.
"""
import subprocess, sys, argparse
import numpy as np
from scipy import ndimage
import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def maska_tla(ramka, prog_jasnosci=226, prog_neutralnosci=10):
    """Zwraca maskę logiczną: True tam, gdzie jest szachownica."""
    r = ramka[:, :, 0].astype(np.int16)
    g = ramka[:, :, 1].astype(np.int16)
    b = ramka[:, :, 2].astype(np.int16)
    jasny = np.minimum(np.minimum(r, g), b) >= prog_jasnosci
    neutralny = (np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b)) <= prog_neutralnosci
    kandydat = jasny & neutralny

    etykiety, ile = ndimage.label(kandydat)
    if ile == 0:
        return np.zeros(kandydat.shape, bool)

    # zostawiamy tylko obszary dotykające krawędzi kadru
    brzeg = np.concatenate([
        etykiety[0, :], etykiety[-1, :], etykiety[:, 0], etykiety[:, -1]
    ])
    zewnetrzne = np.unique(brzeg)
    zewnetrzne = zewnetrzne[zewnetrzne > 0]
    tlo = np.isin(etykiety, zewnetrzne)

    # Kompresja zostawia w tle pojedyncze plamki, które nie mieszczą się w progu
    # neutralności i przetrwałyby jako drobne wyspy. Zostawiamy tylko duże
    # obszary pierwszego planu — sylwetkę.
    plan, ile_planu = ndimage.label(~tlo)
    if ile_planu > 1:
        wielkosci = np.bincount(plan.ravel())
        wielkosci[0] = 0
        prog = 0.005 * tlo.size
        duze = np.where(wielkosci >= prog)[0]
        tlo = ~np.isin(plan, duze)
    return tlo


def alfa_z_maski(tlo, wtopienie=1.1, sciagniecie=1):
    """Maska -> gładka alfa 0..255 z lekko ściągniętą, wygładzoną krawędzią."""
    alfa = (~tlo).astype(np.float32)
    if sciagniecie:
        # ściągamy krawędź o piksel, żeby nie został jasny halo po szachownicy
        alfa = ndimage.grey_erosion(alfa, size=(2 * sciagniecie + 1, 2 * sciagniecie + 1))
    if wtopienie:
        alfa = ndimage.gaussian_filter(alfa, wtopienie)
    return np.clip(alfa * 255.0, 0, 255).astype(np.uint8)


def main():
    p = argparse.ArgumentParser()
    p.add_argument('wejscie')
    p.add_argument('wyjscie')
    p.add_argument('--szerokosc', type=int, default=1920)
    p.add_argument('--wysokosc', type=int, default=1080)
    p.add_argument('--fps', default='25')
    p.add_argument('--klatki', type=int, default=0, help='0 = całość')
    p.add_argument('--podglad', help='zapisz pierwszą klatkę jako PNG i zakończ')
    args = p.parse_args()

    w, h = args.szerokosc, args.wysokosc
    rozmiar = w * h * 3

    czytaj = subprocess.Popen(
        [FFMPEG, '-v', 'error', '-i', args.wejscie,
         '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
        stdout=subprocess.PIPE)

    if args.podglad:
        from PIL import Image
        surowa = czytaj.stdout.read(rozmiar)
        ramka = np.frombuffer(surowa, np.uint8).reshape(h, w, 3)
        alfa = alfa_z_maski(maska_tla(ramka))
        Image.fromarray(np.dstack([ramka, alfa])).save(args.podglad)
        czytaj.kill()
        print('podgląd:', args.podglad)
        return

    zapisz = subprocess.Popen(
        [FFMPEG, '-y', '-v', 'error',
         '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{w}x{h}', '-r', args.fps, '-i', '-',
         '-i', args.wejscie,
         '-map', '0:v', '-map', '1:a?',
         '-c:v', 'libvpx-vp9', '-pix_fmt', 'yuva420p',
         '-b:v', '0', '-crf', '30', '-row-mt', '1', '-cpu-used', '4',
         '-c:a', 'libopus', '-b:a', '128k',
         args.wyjscie],
        stdin=subprocess.PIPE)

    n = 0
    while True:
        surowa = czytaj.stdout.read(rozmiar)
        if len(surowa) < rozmiar:
            break
        ramka = np.frombuffer(surowa, np.uint8).reshape(h, w, 3)
        alfa = alfa_z_maski(maska_tla(ramka))
        # tam, gdzie alfa jest zerowa, zerujemy też kolor — mniej danych do skompresowania
        rgba = np.dstack([ramka, alfa])
        zapisz.stdin.write(rgba.tobytes())
        n += 1
        if n % 25 == 0:
            print(f'  {n} klatek', file=sys.stderr, flush=True)
        if args.klatki and n >= args.klatki:
            break

    zapisz.stdin.close()
    zapisz.wait()
    czytaj.kill()
    print(f'Gotowe: {args.wyjscie} ({n} klatek)')


if __name__ == '__main__':
    main()
