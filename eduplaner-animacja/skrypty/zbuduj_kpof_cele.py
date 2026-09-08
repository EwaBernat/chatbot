# -*- coding: utf-8 -*-
"""Buduje public/kpof-cele.html — druk KPOF-T: tabela celów SMART do 130 twierdzeń KPOF (3 wersje wiekowe × 3 poziomy
wsparcia) z KONSPEKTEM zajęć (druk KC-3) do każdego twierdzenia, kreatorem własnego celu i „Moimi celami”.
Wygląd i logika jak w tabeli celów ToM autorki (druk TOM-T). Użycie: python3 skrypty/zbuduj_kpof_cele.py"""
import os, sys, json, html, re
TU = os.path.dirname(os.path.abspath(__file__)); KAT = os.path.dirname(TU); sys.path.insert(0, TU)
from kpof_cele_dane import OBSZARY, WSPARCIE, KRYT, WERSJE
from kpof_konspekty_A import K as KA
from kpof_konspekty_B import K as KB
from kpof_konspekty_C import K as KC
KON = {'A': KA, 'B': KB, 'C': KC}
SCR = os.environ.get('IPET_SCRATCH', '/tmp/claude-0/-home-user-chatbot/71b0dfe1-b753-5beb-8412-40de3cbd7ec1/scratchpad/ipet')
FONT = open(os.path.join(SCR, 'mulish_embed.css'), encoding='utf-8').read()
TW = json.load(open(os.path.join(os.path.dirname(SCR), 'kpof_twierdzenia.json'), encoding='utf-8'))
# CSS autorki (druk TOM-T) bez osadzonych plików — te same klasy konspektu, tabeli i legendy
TOM_CSS = open(os.path.join(os.path.dirname(SCR), 'tom_style.css'), encoding='utf-8').read()
TOM_CSS = re.sub(r'@font-face\s*\{.*?\}', '', TOM_CSS, flags=re.S)
TOM_CSS = re.sub(r'url\((["\']?)data:[^)]*?\1\)', 'none', TOM_CSS, flags=re.S)
esc = lambda s: html.escape(str(s), quote=True)
META = {'A': ('10 min', 'para z nauczycielem', '4× w tygodniu'), 'B': ('15 min', 'mała grupa (3–4 dzieci)', '3× w tygodniu'), 'C': ('20 min', 'mała grupa (4–6 dzieci)', '3× w tygodniu')}
LVL = {'p3': ('Poziom III', 3), 'p2': ('Poziom II', 2), 'p1': ('Poziom I', 1)}

EXTRA_CSS = r"""
/* --- KPOF-T: uzupełnienia do stylu TOM-T --- */
.sciezka{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:12px}
.krok{border:1px solid var(--fiolet-linia);border-radius:10px;padding:9px 11px;background:#fbfaff;font-size:10.5px;line-height:1.5}
.krok .n{display:inline-flex;width:20px;height:20px;border-radius:50%;background:var(--pomarancz);color:#fff;font-weight:800;font-size:10px;align-items:center;justify-content:center;margin-bottom:4px}
.krok b{display:block;color:var(--fiolet);font-size:10.5px;margin-bottom:2px}
.formula{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:12px}
.formula .f{border-radius:999px;padding:5px 12px;font-size:10.5px;font-weight:700;border:1.4px solid}
.formula .f.s{border-color:var(--fiolet);color:var(--fiolet);background:var(--fiolet-tlo)}.formula .f.m{border-color:var(--pomarancz);color:var(--pomarancz);background:var(--pomarancz-tlo)}.formula .f.a{border-color:var(--p2);color:var(--p2);background:var(--p2-tlo)}.formula .f.r{border-color:var(--p1);color:var(--p1);background:var(--p1-tlo)}.formula .f.t{border-color:#2F8F8A;color:#2F8F8A;background:#e3f3f2}
.formula .lit{font-size:9px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:var(--szary);margin-right:2px}
.chipbtn.pom{background:var(--pomarancz);color:#fff;border-color:var(--pomarancz);font-size:10.5px;padding:6px 13px}
td.g.on{background:var(--pomarancz-tlo);box-shadow:inset 0 0 0 2px var(--pomarancz)}
td.wsk .kzn2{display:block;color:var(--szary);font-size:9px}
.moje{margin:10px 0 12px;border:1px solid var(--fiolet-linia);border-radius:10px;background:#fbfaff;padding:9px 14px}
.moje h4{margin:0 0 6px;font-size:10px;letter-spacing:.7px;text-transform:uppercase;color:var(--fiolet)}
.moje .pusto{font-size:10px;color:var(--szary)}
.mcel{display:flex;gap:10px;align-items:flex-start;border:1px solid var(--linia);background:#fff;border-radius:8px;padding:7px 10px;margin-bottom:6px;font-size:10.5px;line-height:1.45}
.mcel .mn{background:var(--fiolet);color:#fff;font-size:8px;font-weight:800;padding:1px 6px;border-radius:9px;white-space:nowrap}
.mcel .mt{flex:1}.mcel .mp{font-size:9px;color:var(--szary);display:block;margin-top:2px}
.mcel button{border:none;background:none;color:var(--szary);cursor:pointer;font:inherit;font-size:9.5px}
.prawo{font-size:9.5px;color:var(--szary);line-height:1.55;border-top:1px solid var(--linia);padding-top:8px;margin-top:10px}.prawo b{color:var(--fiolet)}
/* kreator celu */
#kreator .kcard{max-width:960px}
.kgrid{display:grid;grid-template-columns:1fr 1fr;gap:9px 12px;margin-bottom:10px}
.kgrid label{display:block;font-size:9px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:var(--szary)}
.kgrid label.full{grid-column:1/-1}
.kgrid .ed{margin-top:3px;border:1px solid var(--fiolet-linia);border-radius:8px;padding:6px 9px;font-size:11px;line-height:1.45;min-height:30px;background:#fff;outline:none;color:var(--ink);font-family:inherit;width:100%;text-transform:none;letter-spacing:0;font-weight:400}
.kgrid .ed:focus{border-color:var(--pomarancz);box-shadow:0 0 0 2px var(--pomarancz-tlo)}
.kgrid .ed:empty::before{content:attr(data-ph);color:#a8a3b8;font-style:italic}
.lvlsel{display:flex;gap:6px;margin-top:3px}
.lvlsel button{flex:1;border:1.4px solid var(--linia);background:#fff;border-radius:8px;padding:6px 4px;font:700 10px/1.2 inherit;cursor:pointer;color:var(--szary);text-transform:none;letter-spacing:0}
.lvlsel button.on[data-l="p3"]{border-color:var(--p3);color:var(--p3);background:var(--p3-tlo)}.lvlsel button.on[data-l="p2"]{border-color:var(--p2);color:var(--p2);background:var(--p2-tlo)}.lvlsel button.on[data-l="p1"]{border-color:var(--p1);color:var(--p1);background:var(--p1-tlo)}
.podglad{border:2px solid var(--pomarancz);border-radius:11px;padding:10px 14px;background:var(--pomarancz-tlo);margin-bottom:10px}
.podglad .pt{font-size:9px;font-weight:800;letter-spacing:.7px;text-transform:uppercase;color:var(--pomarancz);margin-bottom:4px}
.podglad .zd{font-size:13px;line-height:1.55;color:var(--ink)}.podglad .zd b{color:var(--fiolet)}
.smartck{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin-bottom:10px}
.smartck div{border:1px solid var(--linia);border-radius:8px;padding:6px 8px;font-size:9.5px;line-height:1.35;color:var(--szary);background:#fff}
.smartck div b{display:block;font-size:12px;color:var(--szary)}
.smartck div.ok{border-color:var(--p1-linia);background:var(--p1-tlo);color:var(--p1)}.smartck div.ok b{color:var(--p1)}
.kmodal.on{display:block}
@media print{.kreatorbtn,.moje button,.chipbtn{display:none!important}}
"""

def wsk_row(w, wiek, t, k):
    nr = t['nr']; ob = t['obszar']
    cells = ''
    for lvl, cel in zip(('p3', 'p2', 'p1'), k['cele']):
        kr, h = KRYT[lvl]
        cells += (f'<td class="g" data-kon="kon-{w}-{nr}" data-lvl="{lvl}" data-wersja="{w}" data-wiek="{esc(wiek)}" data-wsk="{nr}" tabindex="0" role="button" title="Otwórz konspekt zajęć do tego celu">'
                  f'<span class="tresc">{esc(cel)}</span><span class="ram">{kr} · {h}</span>'
                  f'<button class="mkt-add" type="button" title="Dodaj do moich celów" aria-label="Dodaj do moich celów">+</button></td>')
    ctx = {"obszar": ob, "obszarNazwa": OBSZARY[ob], "tresc": t['tresc'], "kod": t['kod'], "krok": k.get('krok', ''), "syt": k.get('syt', ''), "pomiar": k.get('pomiar', ''),
           "wsp": {"p3": WSPARCIE[ob][0], "p2": WSPARCIE[ob][1], "p1": WSPARCIE[ob][2]}}
    return (f'<tr data-wsk="{nr}" data-nr="{nr}" data-obszar="{ob}" data-ctx="{esc(json.dumps(ctx, ensure_ascii=False))}">'
            f'<td class="nr">{nr}</td><td class="wsk"><b>{esc(t["tresc"])}</b><span>krok obserwowalny: {esc(k["krok"])}</span>'
            f'<span>{esc(t["kod"])} · pomiar: {esc(k["pomiar"])}</span><span class="kzn">konspekt: {esc(k["temat"])}</span></td>{cells}</tr>')

def tabela(w, wiek):
    tw = TW[w]; dane = WERSJE[w][1]; out = []; aktualny = None
    for t in tw:
        nr = t['nr']; ob = t['obszar']
        krok, syt, pomiar = dane[nr]
        k = dict(KON[w][nr]); k.update(krok=krok, syt=syt, pomiar=pomiar)
        if ob != aktualny:
            aktualny = ob
            n_ob = sum(1 for x in tw if x['obszar'] == ob)
            out.append(f'<tr class="pas"><td colspan="5">Obszar {ob} · {esc(OBSZARY[ob])}<span class="li">{n_ob} twierdzeń · ICF {esc(t["kod"].split(" · ")[0])}…</span></td></tr>')
        out.append(wsk_row(w, wiek, t, k))
    return ''.join(out)

def konspekt(w, wiek, t, k):
    nr = t['nr']; ob = t['obszar']; czas, forma, cykl = META[w]
    kvars = ''.join(f'<div class="kvar" data-lvl="{lvl}"><span class="kvlvl {lvl}">{LVL[lvl][0]}</span><div class="ktresc kon-cel"></div><div class="kkryt"><b>Kryterium:</b> <span class="kon-kryt"></span></div></div>' for lvl in ('p3', 'p2', 'p1'))
    smart = [('S', f'Zachowanie widać i da się policzyć: {k["krok"]}.'), ('M', f'Kryterium z klikniętego poziomu wsparcia — liczymy sytuacje w tygodniu; pomiar: {k["pomiar"]}.'),
             ('A', 'Poziom wsparcia to jeden krok od tego, co dziecko robi dziś — nie obniżamy kryterium, zmieniamy warunki.'),
             ('R', f'Wynika z twierdzenia {nr} KPOF ({t["kod"]}) — zwiększa uczestnictwo w obszarze „{OBSZARY[ob]}”.'), ('T', 'Ewaluacja w horyzoncie poziomu: 4, 8 albo 12 tygodni; wynik wpisujemy do karty ewaluacji.')]
    li = lambda a: ''.join(f'<li>{esc(x)}</li>' for x in a)
    prz = ''.join(f'<tr><td class="lp">{i+1}</td><td>{esc(a)}</td><td>{esc(b)}</td></tr>' for i, (a, b) in enumerate(k['przebieg']))
    mody = {
        'p3': [f'dorosły obok — {WSPARCIE[ob][0]}', 'modelowanie i podpowiedź obrazkowa przed każdą próbą; pomoc fizyczna tylko przy nowej czynności', 'krótsza sytuacja, mniej bodźców; kryterium 3 z 5 sytuacji, sprawdzamy po 4 tygodniach'],
        'p2': [f'{WSPARCIE[ob][1][0].upper() + WSPARCIE[ob][1][1:]}', 'dorosły zadaje jedno pytanie lub wskazuje obrazek i czeka 5–7 sekund; nie modeluje', 'kryterium 4 z 5 sytuacji, sprawdzamy po 8 tygodniach'],
        'p1': [f'{WSPARCIE[ob][2][0].upper() + WSPARCIE[ob][2][1:]}', 'dorosły obserwuje z boku i notuje; podpowiedź tylko po nieudanej próbie', 'kryterium 4 z 5 sytuacji (nie 5 z 5), sprawdzamy po 12 tygodniach']}
    mod = lambda l: f'<div class="kmod m{LVL[l][1]}" data-mod="{l}"><b>{LVL[l][0]}</b><ul class="klista">{li(mody[l])}</ul></div>'
    return f'''<div class="kmodal" id="kon-{w}-{nr}" data-wersja="{w}" data-wsk="{nr}" role="dialog" aria-modal="true" aria-label="Konspekt zajęć: {esc(k["temat"])}"><div class="kcard">
<button class="kclose" data-zamknij aria-label="Zamknij konspekt" title="Zamknij (Esc)">✕</button>
<div class="khead"><span class="mark" role="img" aria-label="Logo PCTP"></span><div><div class="kw">EduPlaner 2026</div><div class="ks">Konspekt · obszar {ob} · {esc(OBSZARY[ob])} · twierdzenie {nr} · wersja {w} · {esc(wiek)}</div></div><span class="kpill">Konspekt KPOF {w}-{nr}</span></div>
<div class="kmeta" style="grid-template-columns:1.6fr 1fr 1fr"><div class="field"><b>Dotyczy dziecka</b><span class="dots"></span></div><div class="field"><b>Grupa</b><span class="dots"></span></div><div class="field"><b>Data</b><span class="dots"></span></div></div>
<div class="ktitle"><span class="kp">Konspekt zajęć · druk KC-3</span><div class="ksfera">OBSZAR {ob} · {esc(OBSZARY[ob].upper())} · twierdzenie {nr}: {esc(t["tresc"])} · krok obserwowalny: {esc(k["krok"])} ({esc(t["kod"])})</div><h3>{esc(k["temat"])}</h3><div class="kpod">{esc(k["pod"])}</div></div>
<div class="kmeta"><div class="field"><b>Czas</b>{czas}</div><div class="field"><b>Forma</b>{forma}</div><div class="field"><b>Cykl</b>{cykl}</div><div class="field"><b>Poziom wsparcia</b><span class="kon-poz">wszystkie trzy</span></div></div>
<div class="kkrok"><b>Krok obserwowalny:</b> {esc(k["krok"])}<span>Sytuacja: {esc(k["syt"])}. Pomiar: {esc(k["pomiar"])}. Dziecko wykonuje ten sam krok na każdym poziomie — zmienia się tylko ilość podpory.</span></div>
<div class="ksec"><span class="sq">I</span><h4>Cel SMART</h4><span class="line"></span></div>
<div class="kcele"><div class="kcel edu"><div class="kchead">Cel edukacyjny — z tabeli KPOF-T, wg klikniętego poziomu</div>{kvars}</div>
<div class="kcel ter"><div class="kchead">Cel terapeutyczny</div><div class="ktresc">Dziecko {esc(k["krok"])} — {esc(k["syt"])}, w warunkach wybranego poziomu wsparcia.</div><ul class="ksmart">{''.join(f'<li><b>{a}</b><span>{esc(b)}</span></li>' for a, b in smart)}</ul><div class="kkryt"><b>Kryterium:</b> {esc(k["pomiar"])} — 5 prób w tygodniu, w naturalnych sytuacjach.</div></div></div>
<div class="kdwie"><div><div class="ksec"><span class="sq">II</span><h4>Pomoce dydaktyczne</h4><span class="line"></span></div><ul class="klista">{li(k["pomoce"])}</ul></div>
<div><div class="ksec"><span class="sq">III</span><h4>Metody i formy działań</h4><span class="line"></span></div><ul class="klista">{li(k["metody"])}</ul></div></div>
<div class="kdwie" style="align-items:end"><div><div class="ksec"><span class="sq">IV</span><h4>Sposób realizacji</h4><span class="line"></span></div><div class="krodzaj" style="font-style:italic">Tabela poniżej ↓</div></div>
<div><div class="ksec"><span class="sq">V</span><h4>Rodzaj zajęć</h4><span class="line"></span></div><div class="krodzaj">{esc(k["rodzaj"])}</div></div></div>
<p class="kkurs">Konkretne czynności nauczyciela (N) i odpowiadające im oczekiwane reakcje i umiejętności dziecka (D).</p>
<table class="ktab"><thead><tr><th style="width:26px">Lp.</th><th style="width:47%">Czynności nauczyciela (N)</th><th>Oczekiwane reakcje i umiejętności dziecka (D)</th></tr></thead><tbody>{prz}</tbody></table>
<div class="ksec"><span class="sq">VI</span><h4>Modyfikacja według poziomu wsparcia</h4><span class="line"></span></div>
<p class="kkurs">Poziom zmienia warunki, nie krok. Kliknięty poziom jest wyróżniony; przy sukcesie w dwóch kolejnych tygodniach przechodzimy poziom wyżej, przy braku postępu upraszczamy sytuację, nie kryterium.</p>
<div class="kmods">{mod('p3')}{mod('p2')}{mod('p1')}</div>
<div class="kwsk"><b>Wskazówka dla prowadzącego:</b> cel edukacyjny czytaj z tabeli (w brzmieniu komórki), cel terapeutyczny opisuje ten sam krok w języku obserwacji. Jeśli dziecko nie wykonuje kroku na Poziomie III w 3 z 5 sytuacji, wróć do modelowania i skróć sytuację — nie obniżaj kryterium. Wynik pomiaru wpisz do karty ewaluacji i podejmij jedną z czterech decyzji zespołu.</div>
<div class="fprzyciski"><span class="komunikat">EduPlaner 2026 · PCTP · druk KC-3 · {esc(k["temat"])}</span><button type="button" class="fbtn kreatorbtn" data-kreator-z="kon-{w}-{nr}">✎ Kreator celu z tego poziomu</button><button type="button" class="fbtn" data-drukuj-konspekt>Drukuj konspekt (A4)</button><button type="button" class="fbtn mocny" data-zamknij>Zamknij</button></div>
</div></div>'''

def spis(w, wiek):
    tw = TW[w]; dane = WERSJE[w][1]; out = []; aktualny = None
    for t in tw:
        ob = t['obszar']; nr = t['nr']; k = KON[w][nr]
        if ob != aktualny:
            if aktualny: out.append('</div></div>')
            aktualny = ob
            out.append(f'<div class="kgrupa"><h4>Obszar {ob} · {esc(OBSZARY[ob])}</h4><div class="ksiatka">')
        out.append(f'<button type="button" class="kbtn" data-kon="kon-{w}-{nr}" data-wersja="{w}" data-wsk="{nr}" data-lvl="p2"><span class="knr">{nr}</span><b>{esc(k["temat"])}</b><span class="kzast">{esc(dane[nr][0])}</span></button>')
    out.append('</div></div>')
    return ''.join(out)

JS = r"""
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',()=>{const w=t.dataset.wersja;document.querySelectorAll('.tab').forEach(x=>x.setAttribute('aria-selected',String(x.dataset.wersja===w)));document.querySelectorAll('.wersja').forEach(s=>{s.hidden=s.dataset.wersja!==w;});}));
document.querySelectorAll('.wersja').forEach((s,i)=>{s.hidden=i!==0;});
const POZ={p3:{n:'Poziom III',k:'3 z 5',h:'4 tygodnie',t:28},p2:{n:'Poziom II',k:'4 z 5',h:'8 tygodni',t:56},p1:{n:'Poziom I',k:'4 z 5',h:'12 tygodni',t:84}};
const KLUCZ='eduplaner2026.moje-cele-kpof.v2';
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function zTabeli(w,nr,lvl){const td=document.querySelector('#w-'+w+' tr[data-wsk="'+nr+'"] td.g[data-lvl="'+lvl+'"]');if(!td)return{cel:'',ram:''};return{cel:td.querySelector('.tresc').textContent,ram:td.querySelector('.ram').textContent};}
function otworz(id,lvl){const m=document.getElementById(id);if(!m)return;const w=m.dataset.wersja,nr=m.dataset.wsk;
  m.querySelectorAll('.kvar').forEach(v=>{const t=zTabeli(w,nr,v.dataset.lvl);v.querySelector('.kon-cel').textContent=t.cel;v.querySelector('.kon-kryt').textContent=t.ram;v.classList.toggle('wyb',!!lvl&&v.dataset.lvl===lvl);});
  m.querySelectorAll('.kmod').forEach(k=>k.classList.toggle('wyb',k.dataset.mod===lvl));
  const p=m.querySelector('.kon-poz');if(p)p.textContent=lvl?POZ[lvl].n:'wszystkie trzy';
  m.dataset.lvl=lvl||'';m.classList.add('open');document.body.style.overflow='hidden';}
function zamknij(){document.querySelectorAll('.kmodal.open,.kmodal.on').forEach(m=>{m.classList.remove('open');m.classList.remove('on');});document.body.style.overflow='';}
function drukujKonspekt(){document.documentElement.classList.add('druk-konspektu');window.print();setTimeout(()=>document.documentElement.classList.remove('druk-konspektu'),400);}
function drukujZeszyt(w){const mod=[...document.querySelectorAll('.kmodal[data-wersja="'+w+'"]')];mod.forEach(m=>{m.classList.add('open');m.querySelectorAll('.kvar').forEach(v=>{const t=zTabeli(w,m.dataset.wsk,v.dataset.lvl);v.querySelector('.kon-cel').textContent=t.cel;v.querySelector('.kon-kryt').textContent=t.ram;});});document.documentElement.classList.add('druk-konspektu');window.print();setTimeout(()=>{document.documentElement.classList.remove('druk-konspektu');zamknij();},400);}
/* kreator celu */
const M=document.getElementById('kreator');const pole=n=>M.querySelector('[data-p="'+n+'"]');let ctx={};
function ctxZ(tr){const c=JSON.parse(tr.dataset.ctx);c.nr=tr.dataset.nr;c.wersja=tr.closest('.wersja').dataset.wersja;c.wiek=document.querySelector('.tab[data-wersja="'+c.wersja+'"]').textContent.trim().slice(-8);return c;}
function dataPlus(d){const x=new Date();x.setDate(x.getDate()+d);return String(x.getDate()).padStart(2,'0')+'.'+String(x.getMonth()+1).padStart(2,'0')+'.'+x.getFullYear();}
function otworzKreator(k){ctx=k||{};
  M.querySelector('.ks').textContent=k.nr?('twierdzenie '+k.nr+' · obszar '+k.obszar+' · '+k.obszarNazwa+' · wersja '+k.wersja+' · '+k.wiek):'cel własny — z obserwacji pogłębionej albo zalecenia';
  M.querySelector('.kkrok b').textContent=k.tresc?('Twierdzenie KPOF: '+k.tresc):'Bez twierdzenia KPOF — wpisz zachowanie z obserwacji lub zalecenia';
  M.querySelector('.kkrok span').textContent=k.kod?('kod ICF · podstawa programowa: '+k.kod+' · źródło: ocena KPOF 1–2 → priorytet; obszar czerwony/żółty → wsparcie'):'źródło: karta ABC, ToM, kwestionariusz mowy, profil sensoryczny albo zalecenie z orzeczenia / WOPF';
  pole('dziecko').textContent=k.dziecko||'';pole('syt').textContent=k.syt||'';pole('zach').textContent=k.krok||'';pole('wsp').textContent='';pole('pomiar').textContent=k.pomiar||'';
  pole('zrodlo').textContent=k.nr?('KPOF, twierdzenie '+k.nr+' ('+k.kod+') — ocena … / 5'):'';
  ustawPoziom(k.lvl||'p2');M.classList.add('open');document.body.style.overflow='hidden';}
function ustawPoziom(l){ctx.lvl=l;M.querySelectorAll('.lvlsel button').forEach(b=>b.classList.toggle('on',b.dataset.l===l));pole('kryt').textContent=POZ[l].k+' sytuacji';pole('data').textContent=dataPlus(POZ[l].t)+' ('+POZ[l].h+')';if(ctx.wsp)pole('wsp').textContent=ctx.wsp[l];podglad();}
function podglad(){const g=n=>(pole(n).textContent||'').trim();const d=g('dziecko')||'Dziecko',s=g('syt'),z=g('zach'),k=g('kryt'),w=g('wsp'),t=g('data'),p=g('pomiar');
  let zd='<b>'+esc(d)+'</b>';if(s)zd+=' '+esc(s)+',';zd+=' '+(z?esc(z):'<i style="color:#a8a3b8">[obserwowalne zachowanie]</i>');if(k)zd+=' w <b>'+esc(k)+'</b>';if(w)zd+=', '+esc(w);if(t)zd+=', do <b>'+esc(t)+'</b>';zd+='.'+(p?' Pomiar: '+esc(p)+'.':'');
  M.querySelector('.podglad .zd').innerHTML=zd;const ck={S:!!(s&&z),M:/\d\s*z\s*\d/.test(k),A:!!ctx.lvl,R:!!g('zrodlo'),T:/\d{2}\.\d{2}\.\d{4}/.test(t)};M.querySelectorAll('.smartck div').forEach(x=>x.classList.toggle('ok',!!ck[x.dataset.s]));}
window.kpofRecompute=podglad;M.addEventListener('input',podglad);M.querySelectorAll('.lvlsel button').forEach(b=>b.addEventListener('click',()=>ustawPoziom(b.dataset.l)));
function tekstCelu(){const g=n=>(pole(n).textContent||'').trim();return (g('dziecko')||'Dziecko')+(g('syt')?' '+g('syt')+',':'')+' '+g('zach')+(g('kryt')?' w '+g('kryt'):'')+(g('wsp')?', '+g('wsp'):'')+(g('data')?', do '+g('data'):'')+'.'+(g('pomiar')?' Pomiar: '+g('pomiar')+'.':'');}
/* moje cele */
function wczytaj(){try{const s=localStorage.getItem(KLUCZ);const t=s?JSON.parse(s):[];return Array.isArray(t)?t:[];}catch(e){return window.__moje||[];}}
function zapisz(l){try{localStorage.setItem(KLUCZ,JSON.stringify(l));}catch(e){window.__moje=l;}}
function dodajCel(c){const l=wczytaj();c.id='c'+Date.now().toString(36);c.data=new Date().toISOString().slice(0,10);l.push(c);zapisz(l);}
function rysuj(w){const cel=document.querySelector('[data-moje="'+w+'"]');if(!cel)return;const m=wczytaj().filter(r=>r.wersja===w);cel.innerHTML='<h4>Moje cele · wersja '+w+' · '+m.length+'</h4>'+(m.length?m.map(r=>'<div class="mcel"><span class="mn">'+esc(r.nr)+' · '+esc((POZ[r.lvl]||{}).n||'')+'</span><span class="mt">'+esc(r.tekst)+'<span class="mp">zapisano '+esc(r.data)+(r.pomiar?' · pomiar: '+esc(r.pomiar):'')+'</span></span><button type="button" data-usun="'+r.id+'">usuń</button></div>').join('')+'<button type="button" class="chipbtn" data-drukuj>Drukuj moje cele (A4)</button>':'<div class="pusto">Jeszcze pusto — kliknij „+” przy celu w tabeli albo zapisz cel z kreatora.</div>');}
['A','B','C'].forEach(rysuj);
document.addEventListener('click',ev=>{
  const dodaj=ev.target.closest('.mkt-add');
  if(dodaj){ev.stopPropagation();const td=dodaj.closest('td.g');const tr=td.closest('tr');const c=ctxZ(tr);dodajCel({wersja:c.wersja,nr:c.nr,lvl:td.dataset.lvl,tekst:td.querySelector('.tresc').textContent+' — '+td.querySelector('.ram').textContent,pomiar:c.pomiar});rysuj(c.wersja);dodaj.textContent='✓';setTimeout(()=>dodaj.textContent='+',900);return;}
  const td=ev.target.closest('td.g');if(td){otworz(td.dataset.kon,td.dataset.lvl);return;}
  const kb=ev.target.closest('.kbtn');if(kb){otworz(kb.dataset.kon,null);return;}
  const kz=ev.target.closest('[data-kreator-z]');if(kz){const m=document.getElementById(kz.dataset.kreatorZ);const tr=document.querySelector('#w-'+m.dataset.wersja+' tr[data-wsk="'+m.dataset.wsk+'"]');const c=ctxZ(tr);c.lvl=m.dataset.lvl||'p2';zamknij();otworzKreator(c);return;}
  if(ev.target.closest('[data-kreator]')){const w=document.querySelector('.tab[aria-selected="true"]').dataset.wersja;otworzKreator({wersja:w,wiek:document.querySelector('.tab[aria-selected="true"]').textContent.trim().slice(-8),lvl:'p2'});return;}
  if(ev.target.closest('[data-zamknij]')||ev.target.classList.contains('kmodal')){zamknij();return;}
  if(ev.target.closest('[data-drukuj-konspekt]')){drukujKonspekt();return;}
  const zesz=ev.target.closest('[data-zeszyt]');if(zesz){drukujZeszyt(zesz.dataset.zeszyt);return;}
  if(ev.target.closest('[data-zapisz]')){const w=ctx.wersja||document.querySelector('.tab[aria-selected="true"]').dataset.wersja;dodajCel({wersja:w,nr:ctx.nr||'własny',lvl:ctx.lvl,tekst:tekstCelu(),pomiar:''});rysuj(w);zamknij();return;}
  if(ev.target.closest('[data-kopiuj]')){navigator.clipboard&&navigator.clipboard.writeText(tekstCelu());ev.target.textContent='Skopiowano ✓';setTimeout(()=>ev.target.textContent='Kopiuj do IPET',1500);return;}
  if(ev.target.closest('[data-drukuj]')){window.print();return;}
  const us=ev.target.closest('[data-usun]');if(us){zapisz(wczytaj().filter(x=>x.id!==us.dataset.usun));['A','B','C'].forEach(rysuj);return;}
});
document.addEventListener('keydown',ev=>{if(ev.key==='Escape')zamknij();if(ev.key==='Enter'&&ev.target.matches('td.g'))otworz(ev.target.dataset.kon,ev.target.dataset.lvl);});
"""

def zloz():
    sekcje = ''; modale = ''; razem = 0
    for w, (wiek, dane) in WERSJE.items():
        tw = TW[w]; n = len(tw); razem += n * 3
        for t in tw:
            k = dict(KON[w][t['nr']]); krok, syt, pomiar = dane[t['nr']]; k.update(krok=krok, syt=syt, pomiar=pomiar)
            modale += konspekt(w, wiek, t, k)
        sekcje += f'''<section class="wersja" id="w-{w}" data-wersja="{w}">
<details class="kspis"><summary>Wykaz konspektów · {n} scenariuszy zajęć do tej wersji wiekowej</summary><div class="kspis-tresc"><p class="kspis-info">Konspekt otwiera też kliknięcie celu w tabeli — otwarty scenariusz ma wtedy wyróżniony ten poziom wsparcia, w który kliknięto. <button type="button" class="chipbtn mocny" data-zeszyt="{w}">Drukuj wszystkie {n} konspektów (A4)</button></p>{spis(w, wiek)}</div></details>
<div class="moje" data-moje="{w}"></div>
<table><colgroup><col style="width:5%"><col style="width:29%"><col style="width:22%"><col style="width:22%"><col style="width:22%"></colgroup>
<caption class="sr-only">Cele SMART · KPOF · wersja {w} · {esc(wiek)}</caption>
<thead><tr class="wband"><th colspan="5">EduPlaner 2026 · druk KPOF-T · cele SMART do twierdzeń Kwestionariusza Przedszkolnej Oceny Funkcjonalnej <b>wersja {w} · {esc(wiek)} · {n} twierdzeń · {n} konspektów</b></th></tr>
<tr><th>Nr</th><th>Twierdzenie KPOF · krok obserwowalny · ICF · PP · konspekt</th><th class="p3">Poziom III</th><th class="p2">Poziom II</th><th class="p1">Poziom I</th></tr></thead>
<tbody>{tabela(w, wiek)}</tbody></table></section>'''
    doc = f'''<!DOCTYPE html><html lang="pl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tabela celów SMART · KPOF (przedszkole) — EduPlaner 2026 · PCTP</title><style>{FONT}\n{TOM_CSS}\n{EXTRA_CSS}</style></head><body>
<div class="ark">
<div class="head"><span class="mark" role="img" aria-label="Logo PCTP"></span><div><h1>EduPlaner 2026</h1><div class="sub">KPOF · tabela celów SMART · wiek i poziom wsparcia · konspekty · kreator celu</div></div><div class="prawa"><b>KPOF · WOPF · IPET</b><span>narzędzie · druk KPOF-T</span></div></div>
<div class="kreska"></div>
<div class="tyt"><span class="pigula">{razem} celów SMART · 130 konspektów</span><p>130 twierdzeń Kwestionariusza Przedszkolnej Oceny Funkcjonalnej — dziewięć obszarów ICF, trzy wersje wiekowe — × trzy poziomy wsparcia. Wiersz mówi, <b>co dziecko zrobi albo powie, po czym widać, że twierdzenie się spełnia</b>; kolumna — ile przy tym dostaje podpory. Kliknięcie w cel otwiera <b>konspekt zajęć</b> (druk KC-3) z wyróżnionym tym poziomem; z konspektu przechodzisz do <b>kreatora celu</b>, który składa zdanie według formuły ze skryptu i sprawdza pięć liter SMART.</p></div>
<div class="zakladki" role="tablist" aria-label="Wersje wiekowe"><button type="button" class="tab" role="tab" data-wersja="A" aria-selected="true"><span class="w">wersja A</span>3–4 lata</button><button type="button" class="tab" role="tab" data-wersja="B" aria-selected="false"><span class="w">wersja B</span>5 lat</button><button type="button" class="tab" role="tab" data-wersja="C" aria-selected="false"><span class="w">wersja C</span>6 lat</button><button type="button" class="chipbtn pom" data-kreator style="margin-left:auto">✎ Kreator własnego celu</button></div>
<div class="legenda"><div class="leg l3"><b><i aria-hidden="true"></i>Poziom III</b>dorosły obok, podpowiedź wizualna i modelowanie, zadanie wykonywane razem<div class="kryt">kryterium 3 z 5 sytuacji · weryfikacja po 4 tygodniach</div></div><div class="leg l2"><b><i aria-hidden="true"></i>Poziom II</b>podpowiedź obrazkowa w zasięgu, dziecko wykonuje zadanie samo po pytaniu dorosłego<div class="kryt">kryterium 4 z 5 sytuacji · weryfikacja po 8 tygodniach</div></div><div class="leg l1"><b><i aria-hidden="true"></i>Poziom I</b>bez podpowiedzi obrazkowej, w naturalnej sytuacji z rówieśnikami<div class="kryt">kryterium 4 z 5 sytuacji · weryfikacja po 12 tygodniach</div></div></div>
<div class="uwaga"><b>Poziom zmienia warunki, nie krok.</b> Na każdym poziomie dziecko wykonuje to samo zachowanie z twierdzenia KPOF — tylko z inną ilością podpory. Cel przepisujemy do IPET w brzmieniu z komórki i dokładamy kryterium oraz horyzont z nagłówka kolumny. Kryterium na Poziomie I zostaje <b>4 z 5</b>, nie rośnie do 5 z 5: „za każdym razem” to w przedszkolu cel nie do osiągnięcia i psuje ewaluację.<br><br><b>Skąd cel:</b> twierdzenie ocenione na 1 lub 2 podlega osobnej analizie niezależnie od średniej (reguła nadrzędna); obszar czerwony to priorytet, żółty — wsparcie. Cel musi wynikać z oceny i z zalecenia (orzeczenie, opinia, WOPF). Zapis „rozwijanie samodzielności” wyraża intencję, ale nie mówi, co ma się wydarzyć — cel z tej tabeli mówi.</div>
<div class="formula"><span class="lit">Formuła celu (skrypt, część 6):</span><span class="f s">Dziecko, w konkretnej sytuacji</span><span class="f s">wykona obserwowalne zachowanie</span><span class="f m">w N z M prób</span><span class="f a">przy określonym wsparciu</span><span class="f t">do określonej daty</span><span class="f r">z określonym sposobem pomiaru</span></div>
{sekcje}
<div class="prawo"><b>Podstawa (wg skryptu szkolenia, wyd. 2 po audycie z 5.09.2026):</b> nazwa SMART nie pada w rozporządzeniu; wymagana jest ocena efektywności — § 6 rozp. MEN z 9.08.2017 r. w sprawie kształcenia specjalnego (t.j. Dz.U. 2020 poz. 1309): wielospecjalistyczna ocena co najmniej dwa razy w roku szkolnym; § 20 rozp. MEN z 9.08.2017 r. w sprawie pomocy psychologiczno-pedagogicznej (t.j. Dz.U. 2023 poz. 1798): nauczyciele i specjaliści oceniają efektywność udzielanej pomocy. Twierdzenia KPOF odsyłają do podstawy programowej wychowania przedszkolnego (rozp. ME z 11.03.2026 r., Dz.U. 2026 poz. 378) i kodów ICF (WHO 2001).</div>
<div class="stopka"><span>EduPlaner 2026 · PCTP · pedagog specjalny <b>mgr Mirosława Ewa Jurczyszyn</b></span><span>druk KPOF-T · tabela drukuje się poziomo · {razem} celów · 130 konspektów · kreator celu</span></div>
</div>
{modale}
<div class="kmodal" id="kreator" role="dialog" aria-modal="true" aria-label="Kreator celu SMART"><div class="kcard">
<button class="kclose" data-zamknij aria-label="Zamknij" title="Zamknij (Esc)">✕</button>
<div class="khead"><span class="mark" role="img" aria-label="Logo PCTP"></span><div><div class="kw">Kreator celu SMART</div><div class="ks"></div></div><span class="kpill">druk KC-1 · formuła ze skryptu</span></div>
<div class="kkrok"><b></b><span></span></div>
<div class="kgrid">
<label>Dziecko (imię)<div class="ed" contenteditable="true" spellcheck="false" data-p="dziecko" data-ph="np. Zosia"></div></label>
<label>Poziom wsparcia (A — osiągalny: jeden krok od dziś)<div class="lvlsel"><button type="button" data-l="p3">Poziom III<br><small>dorosły obok</small></button><button type="button" data-l="p2">Poziom II<br><small>podpowiedź w zasięgu</small></button><button type="button" data-l="p1">Poziom I<br><small>bez podpowiedzi</small></button></div></label>
<label class="full">S — w jakiej sytuacji<div class="ed" contenteditable="true" spellcheck="false" data-p="syt" data-ph="np. podczas przygotowania do wyjścia na dwór"></div></label>
<label class="full">S — jakie obserwowalne zachowanie (co zrobi albo powie)<div class="ed" contenteditable="true" spellcheck="false" data-p="zach" data-ph="np. założy samodzielnie buty na rzepy"></div></label>
<label>M — ile razy z ilu prób<div class="ed" contenteditable="true" spellcheck="false" data-p="kryt" data-ph="np. 4 z 5 kolejnych dni"></div></label>
<label>M — przy jakim wsparciu<div class="ed" contenteditable="true" spellcheck="false" data-p="wsp" data-ph="np. przy najwyżej jednej podpowiedzi słownej"></div></label>
<label>T — do kiedy (data ewaluacji)<div class="ed" contenteditable="true" spellcheck="false" data-p="data" data-ph="dd.mm.rrrr"></div></label>
<label>Pomiar — czym sprawdzimy<div class="ed" contenteditable="true" spellcheck="false" data-p="pomiar" data-ph="np. karta obserwacji szatni"></div></label>
<label class="full">R — z czego wynika (twierdzenie KPOF, zalecenie, karta obserwacji)<div class="ed" contenteditable="true" spellcheck="false" data-p="zrodlo" data-ph="np. KPOF twierdzenie 24 — ocena 2 / 5; zalecenie z orzeczenia: trening samoobsługi"></div></label>
</div>
<div class="podglad"><div class="pt">Cel do wpisania w IPET — składa się sam</div><div class="zd"></div></div>
<div class="smartck"><div data-s="S"><b>S</b>konkretny: zachowanie i sytuacja</div><div data-s="M"><b>M</b>mierzalny: ile z ilu prób, przy jakim wsparciu</div><div data-s="A"><b>A</b>osiągalny: poziom wsparcia = jeden krok od dziś</div><div data-s="R"><b>R</b>istotny: wynika z oceny, zwiększa uczestnictwo</div><div data-s="T"><b>T</b>określony w czasie: do kiedy, kiedy sprawdzamy</div></div>
<div class="fprzyciski"><span class="komunikat">Cel zapisuje się w pamięci tej przeglądarki („Moje cele”).</span><button type="button" class="fbtn" data-kopiuj>Kopiuj do IPET</button><button type="button" class="fbtn" data-drukuj>Drukuj</button><button type="button" class="fbtn mocny" data-zapisz>Zapisz do moich celów</button></div>
</div></div>
<script>{JS}</script></body></html>'''
    return doc, razem

if __name__ == '__main__':
    doc, n = zloz()
    p = os.path.join(KAT, 'public/kpof-cele.html')
    open(p, 'w', encoding='utf-8').write(doc)
    print('zapisano', p, '| celów:', n, '| rozmiar:', len(doc))
