# -*- coding: utf-8 -*-
import json,os,re,sys,html
sys.path.insert(0,'/tmp/bud'); from rejestr import zbuduj
R=zbuduj(); ZR='/home/user/chatbot/druki'
WZ={'kacik-dyrektora':(ZR+'/kacik-dyrektora/Kacik_Dyrektora_Kalendarz_PCTP.html','Kącik dyrektora ·<br>przewodnik','dyrektor · kolejność i kafelki'),
    'kacik-nauczyciela':(ZR+'/kacik-nauczyciela/Kacik_Nauczyciela_Checklista_Wychowawcy_PCTP.html','Kącik nauczyciela ·<br>przewodnik','nauczyciel · kolejność i kafelki')}
E=html.escape
for k in R['kaciki']:
    zr,opis_marki,plakietka=WZ[k['klucz']]
    s=open(zr,encoding='utf-8').read()
    head=s[:s.index('<body')]
    # nagłówek strony bierzemy 1:1 z istniejącego druku — wspólna rama
    m=re.search(r'<section class="page">\s*(<div class="naglowek">.*?</div>\s*<div class="belka"></div>)',s,re.S)
    nag=m.group(1)
    nag=re.sub(r'(<div class="marka-opis">).*?(</div>)',r'\1'+opis_marki+r'\2',nag,flags=re.S)
    nag=re.sub(r'(<span class="plakietka">).*?(</span>)',r'\1'+plakietka+r'\2',nag,flags=re.S)
    met=re.search(r'<div class="metryczka">.*?</div>\s*</div>',s,re.S)
    met=met.group(0) if met else ''
    KR=k['kolejnosc']
    o=[head,'<body>\n<section class="page">\n',nag,'\n',met,'\n']
    o.append(f'''  <div class="wstega"><span>{E(k['nazwa'])} · przedszkole · przewodnik · kolejność i podziały</span></div>
  <div class="tytul">JAK UŁOŻONY JEST TEN KĄCIK</div>
  <div class="podtytul">wykaz obowiązków → podział wg terminów → podział wg rodzajów czynności → druki</div>
  <div class="kody"><span class="kreska"></span><span class="tresc">PRZEWODNIK · {len(k['kafelki'])} KAFELKÓW · {k['drukow']} DRUKÓW</span><span class="kreska"></span></div>
  <div class="info"><b>Zasada porządku.</b> Kącik czyta się w czterech krokach i w tej samej kolejności układa się w katalogach oraz w aplikacji. Numer druku jest ciągły przez cały kącik — ten sam numer stoi w nazwie pliku, w rejestrze i na kaflu.</div>
  <div class="sekcja"><span class="numer pom">I</span><h2>Cztery kroki — kolejność obowiązująca</h2><span class="linia"></span></div>
  <table class="tab-mala">
    <thead><tr><th style="width:10mm">Krok</th><th style="width:62mm">Co to jest</th><th>Gdzie leży i co zawiera</th></tr></thead>
    <tbody>''')
    GDZ=['01_WYKAZ_OBOWIAZKOW','02_PODZIAL_WG_TERMINOW','03_PODZIAL_WG_RODZAJOW_CZYNNOSCI','04_DRUKI']
    for i,kr in enumerate(KR):
        p=kr['pozycja']
        tre=(E(p.get('tytul','')) + (' — '+E(p['opis']) if p.get('opis') else '')) if p.get('tytul') else \
            (f"{p.get('kafelkow','')} kafelków — rodzaje czynności, każdy z własnym zestawem druków" if kr['typ']=='kafelki'
             else f"{p.get('drukow','')} druków w kolejności kafelków, numeracja ciągła 01–{k['drukow']:02d}")
        o.append(f'      <tr><td class="lp">{kr["krok"]}</td><td class="klucz">{E(kr["nazwa"])}</td><td><b>{GDZ[i]}</b> · {tre}</td></tr>\n')
    o.append('    </tbody>\n  </table>\n')
    o.append(f'''  <div class="sekcja"><span class="numer">II</span><h2>Kafelki — podział według rodzajów czynności</h2><span class="linia"></span></div>
  <table class="tab-mala tab-zw">
    <thead><tr><th style="width:8mm">Nr</th><th style="width:54mm">Kafel</th><th style="width:26mm">Druki</th><th>Co obejmuje</th></tr></thead>
    <tbody>''')
    for f in k['kafelki']:
        nry=f"{f['druki'][0]['nr']:02d}–{f['druki'][-1]['nr']:02d}" if len(f['druki'])>1 else f"{f['druki'][0]['nr']:02d}"
        syg=' · '.join(d['sygnatura'] for d in f['druki'])
        o.append(f'      <tr><td class="lp">{f["nr"]}</td><td class="klucz">{f["ikona"]} {E(f["nazwa"])}</td>'
                 f'<td><b>{nry}</b><br><span style="font-size:6.2pt">{E(syg)}</span></td><td>{E(f["opis"])}</td></tr>\n')
    o.append('    </tbody>\n  </table>\n')
    # ——— strona 2+ : pełna lista druków, dzielona po 20 wierszy ———
    wiersze=[]
    for f in k['kafelki']:
        for d in f['druki']:
            wiersze.append(f'      <tr><td class="lp">{d["nr"]:02d}</td><td class="klucz">{d["sygnatura"]}</td>'
                     f'<td>{f["nr"]:02d} · {E(f["nazwa"][:26])}</td><td>{E(d["nazwa"])}</td></tr>\n')
    PACZ=[wiersze[i:i+20] for i in range(0,len(wiersze),20)]
    LACZ=1+len(PACZ)
    o.append(f'''  <div class="stopka"><span>EduPlaner 2026 · PCTP · pedagog specjalny</span>
    <span><b>Strona 1 z {LACZ}</b> · {E(k["nazwa"])} · przewodnik · kolejność i kafelki</span></div>
</section>
''')
    for i,pacz in enumerate(PACZ,1):
        o.append('<section class="page">\n'+nag+'\n'+met+'\n')
        rz='III' if i==1 else 'III'+' '*0
        o.append(f'''  <div class="sekcja"><span class="numer pom">III</span><h2>Pełna lista druków w kolejności{"" if len(PACZ)==1 else f" — część {i} z {len(PACZ)}"}</h2><span class="linia"></span></div>
  <table class="tab-mala tab-zw">
    <thead><tr><th style="width:8mm">Nr</th><th style="width:14mm">Sygn.</th><th style="width:36mm">Kafel</th><th>Nazwa druku</th></tr></thead>
    <tbody>''')
        o.append(''.join(pacz))
        o.append('    </tbody>\n  </table>\n')
        if i==len(PACZ):
            o.append('''  <div class="info"><b>Jeden plik, kilka druków.</b> Część druków dzieli plik HTML z sąsiadem — na przykład pięć druków nadzoru siedzi w jednym pliku. Na dysku plik leży w kafelku swojego <b>pierwszego</b> druku, a w każdym kafelku plik <b>_CO_JEST_W_TYM_KAFLU.txt</b> mówi, gdzie szukać pozostałych. W aplikacji trasa prowadzi wprost do druku — plik plus zakres stron — więc podziału na pliki użytkownik nie widzi.</div>\n''')
        o.append(f'''  <div class="stopka"><span>EduPlaner 2026 · PCTP · pedagog specjalny</span>
    <span><b>Strona {i+1} z {LACZ}</b> · {E(k["nazwa"])} · lista druków</span></div>
</section>
''')
    o.append('</body>\n</html>')
    cel=f"/tmp/bud/pakiet/{k['klucz']}/03_PODZIAL_WG_RODZAJOW_CZYNNOSCI/PRZEWODNIK_kolejnosc_i_kafelki.html"
    t=''.join(o)
    if '.tab-zw' not in t.split('<body')[0]:
        t=t.replace('  .tab-mala td{height:6.4mm}','  .tab-mala td{height:6.4mm}\n  .tab-zw td, .tab-zw th{padding:1.3mm 2.2mm}')
    open(cel,'w',encoding='utf-8').write(t)
    print('zapisano',cel.split('pakiet/')[1])
