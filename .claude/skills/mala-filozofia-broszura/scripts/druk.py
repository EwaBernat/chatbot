# -*- coding: utf-8 -*-
"""Osadza kroje w pliku i renderuje PDF.

    python3 scripts/druk.py [katalog_z_broszura.html]

Powstają dwa pliki: do-druku.html (samodzielny, działa bez internetu)
oraz PDF nazwany tytułem broszury. Kroje pobierane są raz i cache'owane
w scripts/fonty/, więc kolejne uruchomienia działają offline.
"""
import base64, os, re, shutil, subprocess, sys

TU = os.path.dirname(os.path.abspath(__file__))
KAT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
CACHE = os.path.join(TU, 'fonty')
UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/120.0.0.0 Safari/537.36')   # starsze UA dostaje TTF zamiast woff2

def przegladarka():
    kandydaci = ['google-chrome', 'chromium', 'chromium-browser', 'chrome']
    for k in kandydaci:
        s = shutil.which(k)
        if s: return s
    import glob
    for wzor in ['/opt/pw-browsers/chromium-*/chrome-linux/chrome',
                 '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
                 os.path.expanduser('~/.cache/ms-playwright/chromium-*/chrome-linux/chrome')]:
        t = sorted(glob.glob(wzor))
        if t: return t[-1]
    return None

def main():
    frag = open(os.path.join(KAT, 'broszura.html'), encoding='utf-8').read()
    tytul = frag.split('<title>')[1].split('</title>')[0]
    styl = frag.split('<style>', 1)[1].split('</style>')[0]
    body = frag.split('</style>', 1)[1].strip()
    href = re.search(r'href="(https://fonts\.googleapis\.com[^"]+)"', frag).group(1).replace('&amp;', '&')

    os.makedirs(CACHE, exist_ok=True)
    css_p = os.path.join(CACHE, 'gf.css')
    if not os.path.exists(css_p):
        subprocess.run(['curl', '-sS', '--max-time', '40', '-A', UA, '-o', css_p, href], check=True)
    css = open(css_p, encoding='utf-8').read()
    faces = []
    for subset, blk in re.findall(r'/\*\s*([\w\-]+)\s*\*/\s*(@font-face\s*\{.*?\})', css, re.S):
        if subset not in ('latin', 'latin-ext'):
            continue
        url = re.search(r'url\((https://[^)]+\.woff2)\)', blk).group(1)
        plik = os.path.join(CACHE, url.rsplit('/', 1)[-1])
        if not os.path.exists(plik):
            subprocess.run(['curl', '-sS', '--max-time', '40', '-o', plik, url], check=True)
        b64 = base64.b64encode(open(plik, 'rb').read()).decode()
        faces.append(re.sub(r'url\(https://[^)]+\.woff2\)', 'url(data:font/woff2;base64,%s)' % b64, blk))
    if len(faces) < 8:
        raise SystemExit('Pobrano tylko %d krojów — sprawdź połączenie i nagłówek UA.' % len(faces))

    doc = ('<!doctype html>\n<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
           '<title>%s</title>\n<style>\n/* kroje osadzone w pliku */\n%s\n%s</style>\n</head>\n'
           '<body>\n%s\n</body>\n</html>\n' % (tytul, '\n'.join(faces), styl, body))
    wy = os.path.join(KAT, 'do-druku.html')
    open(wy, 'w', encoding='utf-8').write(doc)
    print('do-druku.html — %d krojów osadzonych, %.0f kB' % (len(faces), len(doc.encode()) / 1024))

    ch = przegladarka()
    if not ch:
        print('Nie znalazłem przeglądarki. Otwórz do-druku.html i wybierz Drukuj → Zapisz jako PDF '
              '(A4, marginesy: brak, grafika tła włączona).')
        return
    pdf = os.path.join(KAT, re.sub(r'[^\w\-]+', '-', tytul).strip('-') + '.pdf')
    subprocess.run([ch, '--headless', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
                    '--print-to-pdf=' + pdf, '--virtual-time-budget=35000', 'file://' + wy],
                   check=True, capture_output=True)
    d = open(pdf, 'rb').read()
    print('%s — %d stron, %.1f MB' % (os.path.basename(pdf),
                                      len(re.findall(rb'/Type\s*/Page[^s]', d)), len(d) / 1048576))

if __name__ == '__main__':
    main()
