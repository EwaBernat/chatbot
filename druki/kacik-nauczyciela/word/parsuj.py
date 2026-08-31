# -*- coding: utf-8 -*-
"""HTML druku PCTP -> JSON dla generatora .docx"""
import json, re, sys, glob, os
from bs4 import BeautifulSoup, NavigableString, Tag

def tekst(el):
    return re.sub(r'\s+', ' ', el.get_text(' ', strip=True)).strip()

def bogaty(el):
    """zwraca listę [{t:tekst, b:bool}] zachowując pogrubienia"""
    out = []
    def idz(n, pogr):
        if isinstance(n, NavigableString):
            s = re.sub(r'\s+', ' ', str(n))
            if s.strip() or (out and s == ' '):
                out.append({'t': s, 'b': pogr})
            return
        p = pogr or n.name in ('b', 'strong')
        for c in n.children:
            idz(c, p)
    idz(el, False)
    # scal sąsiednie o tym samym pogrubieniu
    scal = []
    for r in out:
        if scal and scal[-1]['b'] == r['b']:
            scal[-1]['t'] += r['t']
        else:
            scal.append(dict(r))
    for r in scal:
        r['t'] = re.sub(r'\s+', ' ', r['t'])
    return [r for r in scal if r['t'].strip()] or [{'t': tekst(el), 'b': False}]

def szer(th):
    m = re.search(r'width:\s*([\d.]+)(mm|%)', th.get('style', '') or '')
    if not m: return None
    return {'v': float(m.group(1)), 'j': m.group(2)}

def blok(el):
    k = el.get('class', [])
    if 'sekcja' in k:
        num = el.find('span', class_='numer')
        h2 = el.find('h2')
        tag = el.find('span', class_='tag')
        return {'typ':'sekcja', 'nr': tekst(num) if num else '',
                'pom': bool(num and 'pom' in num.get('class', [])),
                'tytul': tekst(h2) if h2 else '', 'tag': tekst(tag) if tag else ''}
    if 'wstep' in k:
        return {'typ':'wstep', 'tresc': bogaty(el)}
    if 'prawna' in k:
        return {'typ':'prawna', 'tresc': bogaty(el)}
    if 'legenda' in k:
        return {'typ':'legenda', 'tresc': bogaty(el)}
    if 'info' in k:
        return {'typ':'info', 'tresc': bogaty(el)}
    if 'pole' in k:
        et = el.find('span', class_='etykieta')
        hint = el.find('div', class_='tresc')
        lin = el.find('div', class_='linijki')
        return {'typ':'pole', 'etykieta': tekst(et) if et else '',
                'hint': tekst(hint) if hint else '',
                'linii': len(lin.find_all('div', recursive=False)) if lin else 1}
    if 'siatka2' in k or 'siatka3' in k:
        return {'typ':'siatka', 'kol': 2 if 'siatka2' in k else 3,
                'pola': [blok(p) for p in el.find_all('div', class_='pole', recursive=False)]}
    if el.name == 'table':
        glowa = [{'t': tekst(th), 'w': szer(th)} for th in el.select('thead th')]
        wiersze = []
        for tr in el.select('tbody tr'):
            kom = []
            for td in tr.find_all('td', recursive=False):
                kl = td.get('class', [])
                kom.append({'t': tekst(td),
                            'rodzaj': ('lp' if 'lp' in kl else 'klucz' if 'klucz' in kl
                                       else 'ocena' if 'ocena' in kl else 'kratka' if 'kratka' in kl
                                       else 'puste' if 'puste' in kl else 'zwykla')})
            wiersze.append(kom)
        return {'typ':'tabela', 'glowa': glowa, 'wiersze': wiersze}
    if 'wybor-tytul' in k:
        return {'typ':'wybor-tytul', 'tytul': tekst(el)}
    if 'wybory' in k:
        return {'typ':'wybory', 'opcje': [tekst(w) for w in el.find_all('div', class_='wybor')],
                'kol': 3 if any('w3' in w.get('class', []) for w in el.find_all('div', class_='wybor')) else
                       1 if any('pelny' in w.get('class', []) for w in el.find_all('div', class_='wybor')) else 2}
    if 'podpisy' in k:
        return {'typ':'podpisy', 'opisy': [tekst(o) for o in el.select('.podpis .opis')]}
    if 'blok-dyr' in k:
        znak = el.find('span', class_='znak'); h3 = el.find('h3')
        naglowek = el.find('div', class_='naglowek-bloku')
        wewn = [b for b in (blok(c) for c in el.children
                            if isinstance(c, Tag) and c is not naglowek) if b]
        return {'typ':'blok-dyr', 'znak': tekst(znak) if znak else '',
                'tytul': tekst(h3) if h3 else '', 'tresc': wewn}
    if 'miesiace' in k:
        bl = []
        for m in el.find_all('div', class_='blok-mies'):
            bl.append({'naglowek': tekst(m.find('h4')) if m.find('h4') else '',
                       'termin': tekst(m.find('div', class_='termin')) if m.find('div', class_='termin') else '',
                       'punkty': [bogaty(li) for li in m.find_all('li')]})
        return {'typ':'miesiace', 'bloki': bl}
    if 'karty' in k:
        return {'typ':'karty', 'karty': [{'duza': tekst(kk.find('div', class_='duza')),
                                          'opis': tekst(kk.find('div', class_='opis'))}
                                         for kk in el.find_all('div', class_='karta')]}
    if 'kafle' in k:
        return {'typ':'kafle', 'kafle': [{'nag': tekst(x.find('div', class_='naglowek-kafla')),
                                          'tresc': tekst(x.find('div', class_='tresc-kafla')),
                                          'uwaga': tekst(x.find('div', class_='uwaga')) if x.find('div', class_='uwaga') else ''}
                                         for x in el.find_all('div', class_='kafel')]}
    # ——— układy własne kącika nauczyciela ———
    if 'cele' in k:
        c = []
        for x in el.find_all('div', class_='cel'):
            g = x.find('div', class_='cel-glowa'); h3 = x.find('h3')
            c.append({'znak': tekst(x.find('span', class_='znak')) if x.find('span', class_='znak') else '',
                      'tytul': tekst(h3) if h3 else '',
                      'pig': tekst(x.find('span', class_='pig')) if x.find('span', class_='pig') else '',
                      'mini': tekst(x.find('span', class_='mini')) if x.find('span', class_='mini') else '',
                      'smart': [{'l': tekst(w.find('b')), 'op': tekst(w.find('i'))}
                                for w in x.select('.smart-w')],
                      'kryt': tekst(x.find('div', class_='kryt')) if x.find('div', class_='kryt') else ''})
        return {'typ':'cele', 'cele': c}
    if 'klamra-blok' in k:
        return {'typ':'smart', 'wiersze': [{'l': tekst(w.find('b')), 'op': tekst(w.find('i'))}
                                           for w in el.select('.smart-w')]}
    if 'zle-dobrze' in k:
        z = el.find('div', class_='zle'); d = el.find('div', class_='dobrze')
        def rozbij(x):
            if not x: return {'etyk':'', 'tresc':''}
            e = x.find('span', class_='etyk')
            et = tekst(e) if e else ''
            return {'etyk': et, 'tresc': tekst(x).replace(et, '', 1).strip()}
        return {'typ':'zle-dobrze', 'zle': rozbij(z), 'dobrze': rozbij(d)}
    if 'argumenty' in k:
        return {'typ':'argumenty', 'arg': [{'tytul': tekst(a.find('b')) if a.find('b') else '',
                                            'tresc': bogaty(a.find('p')) if a.find('p') else []}
                                           for a in el.find_all('div', class_='arg')]}
    if 'formula' in k:
        return {'typ':'formula', 'czlony': [{'b': tekst(c.find('b')) if c.find('b') else '',
                                             'i': tekst(c.find('i')) if c.find('i') else ''}
                                            for c in el.find_all('div', class_='czlon')]}
    if 'chipsy' in k:
        return {'typ':'chipsy', 'chipy': [tekst(c) for c in el.find_all('div', class_='chip')]}
    if 'wsk' in k:
        return {'typ':'wsk', 'tresc': tekst(el)}
    if 'kons-wstega' in k or 'kons-etyk' in k or 'kons-sfera' in k:
        t = tekst(el)
        return {'typ':'wstep', 'tresc':[{'t': t, 'b': 'kons-wstega' in k}]} if t else None
    if 'duo' in k:
        kol = []
        for kolumna in el.find_all('div', recursive=False):
            bl = []
            for c in kolumna.children:
                if isinstance(c, Tag):
                    b = blok(c)
                    if b: bl.append(b)
            kol.append(bl)
        return {'typ':'duo', 'kolumny': kol}
    return None

def parsuj(sciezka):
    z = BeautifulSoup(open(sciezka, encoding='utf-8').read(), 'lxml')
    tytul_dok = z.title.string if z.title else os.path.basename(sciezka)
    strony = []
    for sec in z.select('section.page'):
        s = {'tytul': None, 'podtytul': None, 'wstega': None, 'kody': None, 'bloki': []}
        t = sec.find('div', class_='tytul')
        if t:
            s['tytul'] = tekst(t)
            pod = sec.find('div', class_='podtytul');  s['podtytul'] = tekst(pod) if pod else ''
            ws = sec.find('div', class_='wstega');     s['wstega'] = tekst(ws) if ws else ''
            kd = sec.select_one('.kody .tresc');       s['kody'] = tekst(kd) if kd else ''
        st = sec.find('div', class_='stopka')
        s['stopka'] = tekst(st.find_all('span')[-1]) if st else ''
        for c in sec.children:
            if not isinstance(c, Tag): continue
            kl = c.get('class', [])
            if any(x in kl for x in ('naglowek','belka','metryczka','wstega','tytul','podtytul','kody','stopka')): continue
            b = blok(c)
            if b: s['bloki'].append(b)
        strony.append(s)
    return {'plik': os.path.basename(sciezka)[:-5], 'tytul': tytul_dok, 'strony': strony}

if __name__ == '__main__':
    wy = {}
    for f in sorted(glob.glob(sys.argv[1])):
        if os.path.basename(f).startswith('INDEKS'): continue
        d = parsuj(f)
        wy[d['plik']] = d
        n = sum(len(s['bloki']) for s in d['strony'])
        print('%-46s %2d stron, %3d bloków' % (d['plik'][:46], len(d['strony']), n))
    json.dump(wy, open('druki.json','w',encoding='utf-8'), ensure_ascii=False)
    print('\nzapisano druki.json')
