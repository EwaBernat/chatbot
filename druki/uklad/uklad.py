# -*- coding: utf-8 -*-
import json,os,shutil,sys,re
sys.path.insert(0,'/tmp/bud'); from rejestr import zbuduj
R=zbuduj(); ZR='/home/user/chatbot/druki'; CEL='/tmp/bud/pakiet'
shutil.rmtree(CEL,ignore_errors=True)
TR=str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ','acelnoszzACELNOSZZ')
BEZP=lambda s: re.sub(r'_+','_',re.sub(r'[^A-Za-z0-9_.-]','_',s.translate(TR))).strip('_')

for k in R['kaciki']:
    kk=k['klucz']; baza=os.path.join(CEL,kk); src=os.path.join(ZR,kk)
    man=json.load(open(os.path.join(src,'MANIFEST.json'),encoding='utf-8'))
    STR={d['sygnatura']:(d['plik'],d['strona_od'],d['strona_do']) for d in man['druki']}
    def wez(nazwa_pliku,kat,prefiks):
        os.makedirs(kat,exist_ok=True); w=[]
        for ext,pod in (('.html',''),('.pdf',''),('.docx','word')):
            p=os.path.join(src,pod,nazwa_pliku+ext)
            if os.path.exists(p): shutil.copy2(p,os.path.join(kat,BEZP(prefiks)+ext)); w.append(ext)
        return w
    st=os.path.join(baza,'00_START'); os.makedirs(st)
    for f in ['MANIFEST.json','README.md','README_DLA_ARKA.md','POPRAWKI_2026-08-31.md']:
        if os.path.exists(os.path.join(src,f)): shutil.copy2(os.path.join(src,f),st)
    json.dump(R,open(os.path.join(st,'rejestr-kacikow.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    kr=k['kolejnosc']; w=kr[0]['pozycja']
    kat=os.path.join(baza,'01_WYKAZ_OBOWIAZKOW')
    wez(w['plik'],kat,('K-1_' if w.get('sygn') else '')+w['tytul'])
    if w.get('indeks'): wez(w['indeks'],kat,'00_Indeks_kacika')
    t=kr[1]['pozycja']
    wez(t['plik'],os.path.join(baza,'02_PODZIAL_WG_TERMINOW'),(t['sygn'][0]+'_' if t.get('sygn') else '')+t['tytul'])
    os.makedirs(os.path.join(baza,'03_PODZIAL_WG_RODZAJOW_CZYNNOSCI'),exist_ok=True)
    # ——— plik trafia do kafla, w którym leży jego PIERWSZY druk (najniższa strona_od)
    wlasciciel={}
    for f in k['kafelki']:
        for d in f['druki']:
            p=d['plik']; so=STR.get(d['sygnatura'],(p,999,999))[1]
            if p not in wlasciciel or so<wlasciciel[p][1]: wlasciciel[p]=(f['klucz'],so,d)
    for f in k['kafelki']:
        kat=os.path.join(baza,'04_DRUKI',f"{f['nr']:02d}_{BEZP(f['nazwa'])}")
        os.makedirs(kat,exist_ok=True); goscie=[]
        for d in f['druki']:
            wl=wlasciciel[d['plik']]
            if wl[0]==f['klucz']:
                if wl[2]['sygnatura']==d['sygnatura']:
                    wez(d['plik'],kat,f"{d['nr']:02d}_{d['sygnatura']}_{d['nazwa'][:44]}")
            else:
                gk=wl[0]
                gn=next(x for x in k['kafelki'] if x['klucz']==gk)
                a,b=STR.get(d['sygnatura'],('',0,0))[1:]
                goscie.append(f"  {d['sygnatura']:5s} {d['nazwa'][:56]:56s} → kafel {gn['nr']:02d} {gn['nazwa']}, strony {a}–{b}")
        lin=[f"KAFEL {f['nr']:02d} · {f['nazwa']}",'='*70,f['opis'],'','DRUKI W TYM KAFLU:']
        for d in f['druki']:
            a,b=STR.get(d['sygnatura'],('',0,0))[1:]
            lin.append(f"  {d['nr']:02d}. {d['sygnatura']:5s} {d['nazwa'][:58]:58s} strony {a}–{b}")
        if goscie:
            lin+=['','UWAGA — te druki leżą fizycznie w innym kafelku, bo dzielą plik z drukiem stamtąd.',
                  'W aplikacji trasa prowadzi wprost do druku (plik + zakres stron), nie do pliku:','']+goscie
        open(os.path.join(kat,'_CO_JEST_W_TYM_KAFLU.txt'),'w',encoding='utf-8').write('\n'.join(lin)+'\n')
    gw=os.path.join(src,'word')
    if os.path.isdir(gw):
        g=os.path.join(baza,'05_GENERATOR_WORD'); os.makedirs(g,exist_ok=True)
        for f in ['parsuj.py','gen.js']:
            if os.path.exists(os.path.join(gw,f)): shutil.copy2(os.path.join(gw,f),g)
    n=len([1 for r_,d_,f_ in os.walk(baza) for x in f_])
    print(f'{kk:20s} kafelków {len(k["kafelki"])} · plików {n}')
