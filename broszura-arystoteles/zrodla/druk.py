import re,subprocess,base64,os,sys
import os
TU = os.path.dirname(os.path.abspath(__file__))
WYJSCIE = os.path.dirname(TU)
CACHE = os.path.join(TU, 'fonty')
os.chdir(os.path.dirname(TU.rstrip('/')) or '.')
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
frag=open('broszura.html',encoding='utf-8').read()
title=frag.split('<title>')[1].split('</title>')[0]
styles=frag.split('<style>',1)[1].split('</style>')[0]
body=frag.split('</style>',1)[1].strip()
href=re.search(r'href="(https://fonts\.googleapis\.com[^"]+)"',frag).group(1).replace('&amp;','&')
CACHE=os.path.join(TU,'fonty')
os.makedirs(CACHE,exist_ok=True)
css_p=os.path.join(CACHE,'gf.css')
if not os.path.exists(css_p):
    subprocess.run(['curl','-sS','--max-time','40','-A',UA,'-o',css_p,href],check=True)
css=open(css_p,encoding='utf-8').read()
faces=[]
for subset,blk in re.findall(r'/\*\s*([\w\-]+)\s*\*/\s*(@font-face\s*\{.*?\})',css,re.S):
    if subset not in ('latin','latin-ext'): continue
    url=re.search(r'url\((https://[^)]+\.woff2)\)',blk).group(1)
    n=os.path.join(CACHE,url.rsplit('/',1)[-1])
    if not os.path.exists(n): subprocess.run(['curl','-sS','--max-time','40','-o',n,url],check=True)
    faces.append(re.sub(r'url\(https://[^)]+\.woff2\)','url(data:font/woff2;base64,%s)'%base64.b64encode(open(n,'rb').read()).decode(),blk))
assert len(faces)>=8, len(faces)
doc=('<!doctype html>\n<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
 f'<title>{title}</title>\n<style>\n/* kroje osadzone w pliku */\n'+"\n".join(faces)+"\n"+styles+
 '</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n')
open('do-druku.html','w',encoding='utf-8').write(doc)
print('krojów osadzonych:',len(faces),'| do-druku.html: %.0f KB'%(len(doc.encode())/1024))

# --- wersja kontrolna z pomiarem przepełnienia
check=doc.replace('</body>','''<div id="raport" style="display:none"></div>
<script>
addEventListener('load',function(){setTimeout(function(){
 var out=[];
 document.querySelectorAll('.strona').forEach(function(s){
   var nr=s.dataset.nr, c=s.querySelector('.strona-tresc');
   var el=c||s;
   var over=el.scrollHeight-el.clientHeight;
   var fill=c?Math.round(100*c.scrollHeight/c.clientHeight):100;
   if(over>1||fill<45) out.push(nr+':over='+over+',fill='+fill);
 });
 document.title='RAPORT|'+(out.join(';')||'OK');
},400);});
</script></body>''')
open(os.path.join(TU,'check.html'),'w',encoding='utf-8').write(check)
