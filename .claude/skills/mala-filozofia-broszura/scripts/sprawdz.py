# -*- coding: utf-8 -*-
"""Kontrola broszury przed drukiem.

    python3 scripts/sprawdz.py tresc.json [katalog_z_broszura.html]

Sprawdza dwie rzeczy, których nie widać gołym okiem:
 1. czy treść trzyma kontrakt serii (450 zdań, 60 pytań, podziały 14/10/7/6),
 2. czy któraś z 60 stron nie przelewa się poza kolumnę — makieta ma sztywne
    strony, więc nadmiar tekstu zostaje ucięty po cichu zamiast przenieść się dalej.
"""
import json, os, re, subprocess, sys

TU = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TU)

WYMAGANE = {'scena': 14, 'mysl': 10, 'emocja': 7, 'zycie': 6}
bledy, ostrzezenia = [], []

def sprawdz_tresc(sciezka):
    D = json.load(open(sciezka, encoding='utf-8'))
    roz = D['rozdzialy']
    if len(roz) != 12:
        bledy.append('Rozdziałów: %d, powinno być 12.' % len(roz))
    suma, pytan = len(D['wstep']['zdania']), 0
    if len(D['wstep']['zdania']) != 6:
        bledy.append('Wstęp ma %d zdań, powinien mieć 6.' % len(D['wstep']['zdania']))
    numery = []
    for r in roz:
        for klucz, ile in WYMAGANE.items():
            n = len(r.get(klucz, []))
            suma += n
            if n != ile:
                bledy.append('Rozdział %s — sekcja „%s” ma %d zdań, powinna mieć %d.'
                             % (r.get('nr', '?'), klucz, n, ile))
        p = r.get('pytania', [])
        pytan += len(p)
        if len(p) != 5:
            bledy.append('Rozdział %s ma %d pytań, powinien mieć 5.' % (r.get('nr', '?'), len(p)))
        numery += [int(a) for a, _ in p]
        for klucz in ('scena', 'mysl', 'emocja', 'zycie'):
            for z in r.get(klucz, []):
                goly = re.sub(r'<[^>]+>', '', z)
                if len(re.findall(r'[.!?](?:\s|$)', goly.replace('p.n.e.', 'X'))) > 1:
                    ostrzezenia.append('Rozdział %s, „%s”: „%s…” wygląda na dwa zdania w jednym wpisie.'
                                       % (r['nr'], klucz, goly[:52]))
                if len(goly) > 145:
                    ostrzezenia.append('Rozdział %s, „%s”: zdanie ma %d znaków — rozważ skrócenie.'
                                       % (r['nr'], klucz, len(goly)))
    if suma != 450:
        bledy.append('Zdań opowiadania: %d, kontrakt serii mówi 450.' % suma)
    if pytan != 60:
        bledy.append('Pytań: %d, powinno być 60.' % pytan)
    if numery != list(range(1, 61)):
        bledy.append('Pytania nie są ponumerowane ciągiem 1–60.')
    for pole in ('hasla', 'slownik', 'nota'):
        if not D.get(pole):
            bledy.append('Brakuje sekcji „%s”.' % pole)
    if len(D.get('hasla', [])) != 12:
        bledy.append('Haseł: %d, powinno być 12.' % len(D.get('hasla', [])))
    g = D.get('gra', {})
    if len(g.get('karty', [])) != 12:
        bledy.append('Kart gry: %d, powinno być 12.' % len(g.get('karty', [])))
    if len(g.get('kostka_emocji', [])) != 6:
        bledy.append('Kostka emocji ma %d ścian, powinna mieć 6.' % len(g.get('kostka_emocji', [])))
    if len(g.get('plansza_emocje', [])) != 12:
        bledy.append('Plansza potrzebuje 12 nazw emocji, jest %d.' % len(g.get('plansza_emocje', [])))
    print('Treść: %d zdań opowiadania, %d pytań, %d rozdziałów.' % (suma, pytan, len(roz)))

def sprawdz_lamanie(kat):
    import druk
    plik = os.path.join(kat, 'do-druku.html')
    if not os.path.exists(plik):
        ostrzezenia.append('Brak do-druku.html — uruchom najpierw druk.py, żeby sprawdzić łamanie.')
        return
    ch = druk.przegladarka()
    if not ch:
        ostrzezenia.append('Nie znalazłem przeglądarki — łamanie stron niesprawdzone.')
        return
    doc = open(plik, encoding='utf-8').read()
    test = doc.replace('</body>', '''<script>addEventListener('load',function(){setTimeout(function(){
var o=[];document.querySelectorAll('.strona').forEach(function(s){
var c=s.querySelector('.strona-tresc');var el=c||s;var over=el.scrollHeight-el.clientHeight;
if(over>1) o.push(s.dataset.nr+':'+over);});
document.title='RAPORT|'+(o.join(' ')||'OK');},600);});</script></body>''')
    tmp = os.path.join(kat, '.kontrola.html')
    open(tmp, 'w', encoding='utf-8').write(test)
    r = subprocess.run([ch, '--headless', '--disable-gpu', '--no-sandbox', '--window-size=1400,1000',
                        '--virtual-time-budget=20000', '--dump-dom', 'file://' + tmp],
                       capture_output=True, text=True)
    os.remove(tmp)
    m = re.search(r'<title>RAPORT\|([^<]*)', r.stdout)
    if not m:
        ostrzezenia.append('Nie udało się odczytać raportu łamania.')
        return
    wynik = m.group(1)
    if wynik == 'OK':
        print('Łamanie stron: wszystkie 60 stron mieści się w kolumnie.')
    else:
        for wpis in wynik.split():
            nr, ile = wpis.split(':')
            bledy.append('Strona %s przelewa się o %s px (~%.0f mm). Skróć tekst albo zmniejsz grafikę.'
                         % (nr, ile, int(ile) / 3.78))

def main():
    sciezka = sys.argv[1] if len(sys.argv) > 1 else os.path.join(TU, '..', 'assets', 'tresc-arystoteles.json')
    kat = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(sciezka))
    sprawdz_tresc(sciezka)
    sprawdz_lamanie(kat)
    if ostrzezenia:
        print('\nDo sprawdzenia (%d):' % len(ostrzezenia))
        for o in ostrzezenia[:12]:
            print('  ·', o)
        if len(ostrzezenia) > 12:
            print('  · … i %d więcej' % (len(ostrzezenia) - 12))
    if bledy:
        print('\nBŁĘDY (%d):' % len(bledy))
        for b in bledy:
            print('  ✗', b)
        sys.exit(1)
    print('\nWszystko się zgadza.')

if __name__ == '__main__':
    main()
