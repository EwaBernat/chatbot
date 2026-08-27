# -*- coding: utf-8 -*-
import re, subprocess, base64, io
UA="Mozilla/5.0 (Windows NT 6.1; rv:27.0) Gecko/20100101 Firefox/27.0"
def pobierz(u,b=False):
    r=subprocess.run(['curl','-sS','--max-time','60','-A',UA,u],capture_output=True)
    if r.returncode: raise RuntimeError(u)
    return r.stdout if b else r.stdout.decode('utf-8')

ZAPYTANIA=["Fraunces:ital,wght@0,400;0,500;0,600;0,700;0,900;1,400",
           "DM+Sans:wght@400;500;700",
           "JetBrains+Mono:wght@400;500;700"]
pole=lambda b,k:(re.search(k+r':\s*([^;]+);',b) or [None,''])[1].strip()

wyjscie=[]; bajty=0; opis=[]
for q in ZAPYTANIA:
    css=pobierz("https://fonts.googleapis.com/css2?family=%s&display=swap"%q)
    for blok in re.findall(r'@font-face\s*\{[^}]*\}',css):
        m=re.search(r'url\((https://[^)]+)\)',blok)
        if not m: continue
        rodz,styl,waga = pole(blok,'font-family'),pole(blok,'font-style'),pole(blok,'font-weight')
        dane=pobierz(m.group(1),True); bajty+=len(dane)
        opis.append('%s %s %s — %.0f kB'%(rodz,styl,waga,len(dane)/1024))
        wyjscie.append("@font-face{font-family:%s;font-style:%s;font-weight:%s;font-display:block;"
                       "src:url(data:font/woff;base64,%s) format('woff');}"
                       %(rodz,styl,waga,base64.b64encode(dane).decode()))
io.open('fonty_statyczne.css','w',encoding='utf-8').write('\n'.join(wyjscie)+'\n')
for o in opis: print('  ',o)
print('RAZEM: %d plików · %.0f kB surowo · %.0f kB w CSS'%(len(wyjscie),bajty/1024,sum(len(x) for x in wyjscie)/1024))
