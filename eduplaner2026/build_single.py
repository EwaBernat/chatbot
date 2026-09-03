#!/usr/bin/env python3
"""Składa index.html z obrazkami z katalogu img/ w jeden plik dist/eduplaner2026.html
(obrazy wbudowane jako data URI). Użycie: python3 build_single.py"""
import base64, mimetypes, os, re, sys
here=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(here,'index.html'),encoding='utf-8').read()
def inline(m):
    rel=m.group(1); path=os.path.join(here,rel)
    if not os.path.exists(path):
        print('brak pliku, zostawiam ścieżkę:',rel); return m.group(0)
    mime=mimetypes.guess_type(path)[0] or 'application/octet-stream'
    return 'src="data:%s;base64,%s"'%(mime,base64.b64encode(open(path,'rb').read()).decode())
out=re.sub(r'src="(img/[^"]+)"',inline,src)

def inline_js(m):
    rel=m.group(2); path=os.path.join(here,rel)
    if not os.path.exists(path):
        print('brak pliku, zostawiam ścieżkę:',rel); return m.group(0)
    mime=mimetypes.guess_type(path)[0] or 'application/octet-stream'
    return '%s"data:%s;base64,%s"'%(m.group(1),mime,base64.b64encode(open(path,'rb').read()).decode())
# ścieżki podane w danych JavaScriptu, np.  plik:"img/app-wopf.jpg"
out=re.sub(r'(plik:\s*)"(img/[^"]+)"',inline_js,out)

pozostale=re.findall(r'"(img/[^"]+)"',out)
if pozostale:
    print('UWAGA: nie wbudowano', len(pozostale),'ścieżek:', sorted(set(pozostale)))
os.makedirs(os.path.join(here,'dist'),exist_ok=True)
open(os.path.join(here,'dist','eduplaner2026.html'),'w',encoding='utf-8').write(out)
print('zapisano dist/eduplaner2026.html', len(out)//1024,'KB')
