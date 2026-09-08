# -*- coding: utf-8 -*-
"""Buduje public/kpof-cele.html — druk KPOF-T: tabela celów SMART do twierdzeń KPOF (3 wersje wiekowe × 3 poziomy
wsparcia) + kreator własnego celu (formuła ze skryptu, część 6) + „Moje cele” (pamięć przeglądarki).
Styl jak w tabeli celów ToM autorki (druk TOM-T). Użycie: python3 skrypty/zbuduj_kpof_cele.py"""
import os, sys, json, html, re
TU = os.path.dirname(os.path.abspath(__file__)); KAT = os.path.dirname(TU); sys.path.insert(0, TU)
from kpof_cele_dane import OBSZARY, WSPARCIE, KRYT, WERSJE
SCR = os.environ.get('IPET_SCRATCH', '/tmp/claude-0/-home-user-chatbot/71b0dfe1-b753-5beb-8412-40de3cbd7ec1/scratchpad/ipet')
FONT = open(os.path.join(SCR, 'mulish_embed.css'), encoding='utf-8').read()
TW = json.load(open(os.path.join(os.path.dirname(SCR), 'kpof_twierdzenia.json'), encoding='utf-8'))
esc = lambda s: html.escape(str(s), quote=True)

def cel(obszar, krok, syt, lvl):
    w = WSPARCIE[obszar][{'p3':0,'p2':1,'p1':2}[lvl]]
    k = krok[0].upper() + krok[1:]
    return f'{k} — {syt}, {w}'

CSS = r"""
:root{--fiolet:#2D1B69;--fiolet-2:#5a4a94;--fiolet-tlo:#efeaf9;--fiolet-linia:#d9d0f0;--pomarancz:#E8450A;--pomarancz-tlo:#fdece4;--pomarancz-linia:#f3cdbd;--ink:#2b2733;--szary:#6f6a7d;--paper:#fff;--linia:#e4e1ec;--zebra:#faf7f2;--p1:#1f8a5b;--p1-tlo:#eaf6f0;--p1-linia:#bfe3d1;--p2:#c8811b;--p2-tlo:#fbf3e3;--p2-linia:#eed6a8;--p3:#c0392b;--p3-tlo:#fbebe9;--p3-linia:#f0c3bd;--morski:#2F8F8A}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:#e9e7ef;color:var(--ink);padding:18px 12px;font-family:'Mulish','Segoe UI',Candara,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.ark{max-width:1180px;margin:0 auto;background:var(--paper);border-radius:14px;padding:22px 26px 18px;box-shadow:0 8px 34px rgba(45,27,105,.15)}
.head{display:flex;align-items:center;gap:13px;margin-bottom:14px}
.mark{width:40px;height:40px;border-radius:50%;background:var(--fiolet);border:2px solid #cfc4ea;display:flex;align-items:center;justify-content:center;color:#fff;font-size:9px;font-weight:800;letter-spacing:.4px;flex:0 0 auto}
.mark::after{content:"PCTP"}
.head h1{font-size:19px;margin:0;color:var(--fiolet);letter-spacing:.2px}
.head .sub{font-size:9.5px;color:var(--szary);letter-spacing:.6px;text-transform:uppercase;font-weight:700;margin-top:2px}
.head .prawa{margin-left:auto;text-align:right}
.head .prawa b{display:inline-block;background:var(--pomarancz);color:#fff;font-size:11px;padding:5px 13px;border-radius:20px}
.head .prawa span{display:block;font-size:8.5px;color:var(--szary);letter-spacing:.9px;margin-top:4px;text-transform:uppercase}
.kreska{height:3px;border-radius:3px;margin-bottom:14px;background:linear-gradient(90deg,var(--fiolet) 0%,var(--fiolet) 55%,var(--pomarancz) 55%,var(--pomarancz) 100%)}
.tyt{margin-bottom:14px}
.pigula{display:inline-block;background:var(--fiolet);color:#fff;font-size:12px;font-weight:800;padding:6px 15px;border-radius:20px}
.tyt p{margin:8px 0 0;font-size:12px;line-height:1.6;max-width:80ch;color:#413c4d}
.zakladki{display:flex;gap:8px;margin:14px 0 12px;flex-wrap:wrap;align-items:center}
.tab{border:1px solid var(--fiolet-linia);background:var(--paper);color:var(--ink);border-radius:999px;padding:8px 18px;font:600 12px/1.25 inherit;cursor:pointer;text-align:left}
.tab .w{display:block;font-size:8.5px;letter-spacing:.8px;text-transform:uppercase;color:var(--szary);font-weight:800}
.tab[aria-selected="true"]{background:var(--fiolet);border-color:var(--fiolet);color:#fff}
.tab[aria-selected="true"] .w{color:#cfc4ea}
.legenda{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:12px}
.leg{border-radius:10px;padding:9px 12px;font-size:10.5px;line-height:1.45;border:1px solid}
.leg b{display:flex;align-items:center;gap:6px;font-size:11px;margin-bottom:3px}
.leg b i{width:10px;height:10px;border-radius:3px;display:inline-block}
.leg .kryt{font-size:9.5px;color:var(--szary);margin-top:3px}
.leg.l3{background:var(--p3-tlo);border-color:var(--p3-linia);color:var(--p3)}.leg.l2{background:var(--p2-tlo);border-color:var(--p2-linia);color:var(--p2)}.leg.l1{background:var(--p1-tlo);border-color:var(--p1-linia);color:var(--p1)}
.leg.l3 b i{background:var(--p3)}.leg.l2 b i{background:var(--p2)}.leg.l1 b i{background:var(--p1)}
.uwaga{background:var(--pomarancz-tlo);border:1px solid var(--pomarancz-linia);border-radius:10px;padding:10px 14px;font-size:11px;line-height:1.6;margin-bottom:14px}
.uwaga b{color:var(--fiolet)}
.sciezka{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:14px}
.krok{border:1px solid var(--fiolet-linia);border-radius:10px;padding:9px 11px;background:#fbfaff;font-size:10.5px;line-height:1.5}
.krok .n{display:inline-flex;width:20px;height:20px;border-radius:50%;background:var(--pomarancz);color:#fff;font-weight:800;font-size:10px;align-items:center;justify-content:center;margin-bottom:4px}
.krok b{display:block;color:var(--fiolet);font-size:10.5px;margin-bottom:2px}
.formula{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:14px}
.formula .f{border-radius:999px;padding:5px 12px;font-size:10.5px;font-weight:700;border:1.4px solid}
.formula .f.s{border-color:var(--fiolet);color:var(--fiolet);background:var(--fiolet-tlo)}
.formula .f.m{border-color:var(--pomarancz);color:var(--pomarancz);background:var(--pomarancz-tlo)}
.formula .f.a{border-color:var(--p2);color:var(--p2);background:var(--p2-tlo)}
.formula .f.r{border-color:var(--p1);color:var(--p1);background:var(--p1-tlo)}
.formula .f.t{border-color:var(--morski);color:var(--morski);background:#e3f3f2}
.formula .lit{font-size:9px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:var(--szary);margin-right:2px}
.chipbtn{border:1px solid var(--fiolet-linia);background:#fff;color:var(--fiolet);border-radius:999px;padding:6px 13px;font:700 10.5px/1 inherit;cursor:pointer}
.chipbtn.mocny{background:var(--fiolet);color:#fff;border-color:var(--fiolet)}
.chipbtn.pom{background:var(--pomarancz);color:#fff;border-color:var(--pomarancz)}
table{width:100%;border-collapse:collapse;font-size:10.5px}
caption.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
thead th{background:var(--fiolet);color:#fff;font-size:9px;letter-spacing:.6px;text-transform:uppercase;padding:7px 8px;text-align:left;font-weight:800;border-right:1px solid rgba(255,255,255,.18)}
thead th.p3{background:var(--p3)}thead th.p2{background:var(--p2)}thead th.p1{background:var(--p1)}
tr.wband th{background:var(--fiolet-2);font-size:9.5px;text-transform:none;letter-spacing:.3px}
tr.pas td{background:var(--fiolet-tlo);color:var(--fiolet);font-weight:800;font-size:10.5px;padding:6px 9px;border-top:2px solid var(--fiolet-linia)}
tr.pas .li{font-weight:600;color:var(--szary);font-size:9px;margin-left:8px}
td{border-bottom:1px solid var(--linia);padding:7px 9px;vertical-align:top;line-height:1.45}
td.nr{font-weight:800;color:var(--fiolet);font-size:10px}
td.wsk b{display:block;font-weight:700;margin-bottom:3px}
td.wsk span{display:block;color:var(--szary);font-size:9.5px}
td.wsk .kzn{color:var(--pomarancz);font-weight:700;margin-top:3px}
td.g{position:relative;cursor:pointer}
td.g:hover,td.g.on{background:var(--pomarancz-tlo)}
td.g.on{box-shadow:inset 0 0 0 2px var(--pomarancz)}
td.g .tresc{display:block;padding-right:16px}
td.g .ram{display:inline-block;margin-top:5px;font-size:8.5px;font-weight:700;padding:2px 7px;border-radius:9px;border:1px solid}
td.g[data-lvl="p3"] .ram{background:var(--p3-tlo);color:var(--p3);border-color:var(--p3-linia)}
td.g[data-lvl="p2"] .ram{background:var(--p2-tlo);color:var(--p2);border-color:var(--p2-linia)}
td.g[data-lvl="p1"] .ram{background:var(--p1-tlo);color:var(--p1);border-color:var(--p1-linia)}
.mkt-add{position:absolute;top:5px;right:5px;width:17px;height:17px;border-radius:50%;border:1px solid var(--fiolet-linia);background:#fff;color:var(--fiolet);font:800 11px/1 inherit;cursor:pointer;opacity:0;transition:opacity .12s}
td.g:hover .mkt-add,.mkt-add:focus{opacity:1}
.moje{margin:12px 0;border:1px solid var(--fiolet-linia);border-radius:10px;background:#fbfaff;padding:10px 14px}
.moje h4{margin:0 0 6px;font-size:10px;letter-spacing:.7px;text-transform:uppercase;color:var(--fiolet)}
.moje .pusto{font-size:10px;color:var(--szary)}
.mcel{display:flex;gap:10px;align-items:flex-start;border:1px solid var(--linia);background:#fff;border-radius:8px;padding:7px 10px;margin-bottom:6px;font-size:10.5px;line-height:1.45}
.mcel .mn{background:var(--fiolet);color:#fff;font-size:8px;font-weight:800;padding:1px 6px;border-radius:9px;white-space:nowrap}
.mcel .mt{flex:1}
.mcel .mp{font-size:9px;color:var(--szary);display:block;margin-top:2px}
.mcel button{border:none;background:none;color:var(--szary);cursor:pointer;font:inherit;font-size:9.5px}
.stopka{margin-top:16px;padding-top:10px;border-top:1px solid var(--linia);display:flex;justify-content:space-between;font-size:9.5px;color:var(--szary);flex-wrap:wrap;gap:6px}
/* kreator */
.kmodal{display:none;position:fixed;inset:0;background:rgba(45,27,105,.45);z-index:50;align-items:flex-start;justify-content:center;padding:30px 12px;overflow:auto}
.kmodal.open,.kmodal.on{display:flex}
.kcard{background:#fff;border-radius:14px;max-width:1000px;width:100%;padding:18px 22px 16px;position:relative;box-shadow:0 20px 60px rgba(45,27,105,.35)}
.kclose{position:absolute;top:10px;right:12px;border:none;background:var(--fiolet-tlo);color:var(--fiolet);width:30px;height:30px;border-radius:50%;cursor:pointer;font:800 14px/1 inherit}
.khead{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.khead .kw{font-weight:800;color:var(--fiolet);font-size:14px}
.khead .ks{font-size:9.5px;color:var(--szary);text-transform:uppercase;letter-spacing:.5px}
.kpill{margin-left:auto;background:var(--pomarancz);color:#fff;font-size:9.5px;font-weight:800;padding:4px 11px;border-radius:999px}
.kkrok{background:var(--fiolet-tlo);border-radius:9px;padding:8px 12px;font-size:10.5px;line-height:1.5;margin-bottom:10px}
.kkrok b{color:var(--fiolet)}
.kkrok span{display:block;color:var(--szary);font-size:9.5px;margin-top:2px}
.kgrid{display:grid;grid-template-columns:1fr 1fr;gap:9px 12px;margin-bottom:10px}
.kgrid label{display:block;font-size:9px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:var(--szary)}
.kgrid label.full{grid-column:1/-1}
.kgrid .ed{text-transform:none;letter-spacing:0;font-weight:400;margin-top:3px;border:1px solid var(--fiolet-linia);border-radius:8px;padding:6px 9px;font-size:11px;line-height:1.45;min-height:30px;background:#fff;outline:none;color:var(--ink);font-family:inherit;width:100%}
.kgrid .ed:focus{border-color:var(--pomarancz);box-shadow:0 0 0 2px var(--pomarancz-tlo)}
.kgrid .ed:empty::before{content:attr(data-ph);color:#a8a3b8;font-style:italic}
.lvlsel{display:flex;gap:6px;margin-top:3px}
.lvlsel button{text-transform:none;letter-spacing:0;flex:1;border:1.4px solid var(--linia);background:#fff;border-radius:8px;padding:6px 4px;font:700 10px/1.2 inherit;cursor:pointer;color:var(--szary)}
.lvlsel button.on[data-l="p3"]{border-color:var(--p3);color:var(--p3);background:var(--p3-tlo)}
.lvlsel button.on[data-l="p2"]{border-color:var(--p2);color:var(--p2);background:var(--p2-tlo)}
.lvlsel button.on[data-l="p1"]{border-color:var(--p1);color:var(--p1);background:var(--p1-tlo)}
.podglad{border:2px solid var(--pomarancz);border-radius:11px;padding:10px 14px;background:var(--pomarancz-tlo);margin-bottom:10px}
.podglad .pt{font-size:9px;font-weight:800;letter-spacing:.7px;text-transform:uppercase;color:var(--pomarancz);margin-bottom:4px}
.podglad .zd{font-size:13px;line-height:1.55;color:var(--ink)}
.podglad .zd b{color:var(--fiolet)}
.smartck{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin-bottom:10px}
.smartck div{border:1px solid var(--linia);border-radius:8px;padding:6px 8px;font-size:9.5px;line-height:1.35;color:var(--szary);background:#fff}
.smartck div b{display:block;font-size:12px;color:var(--szary)}
.smartck div.ok{border-color:var(--p1-linia);background:var(--p1-tlo);color:var(--p1)}
.smartck div.ok b{color:var(--p1)}
.fprzyciski{display:flex;gap:8px;justify-content:flex-end;align-items:center;flex-wrap:wrap}
.fprzyciski .komunikat{margin-right:auto;font-size:9.5px;color:var(--szary)}
.fbtn{border:1px solid var(--fiolet-linia);background:#fff;color:var(--fiolet);border-radius:999px;padding:7px 15px;font:700 10.5px/1 inherit;cursor:pointer}
.fbtn.mocny{background:var(--fiolet);color:#fff;border-color:var(--fiolet)}
.fbtn.pom{background:var(--pomarancz);color:#fff;border-color:var(--pomarancz)}
.zrodla{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:12px}
.zr{border-radius:10px;padding:9px 12px;font-size:10.5px;line-height:1.5;border:1px solid var(--fiolet-linia);background:#fbfaff}
.zr b{display:block;color:var(--fiolet);margin-bottom:2px}
.prawo{font-size:9.5px;color:var(--szary);line-height:1.55;border-top:1px solid var(--linia);padding-top:8px;margin-top:10px}
.prawo b{color:var(--fiolet)}
@media print{body{background:#fff;padding:0}.ark{box-shadow:none;max-width:none;border-radius:0}.kmodal{display:none!important}.tab,.chipbtn,.mkt-add,.mcel button{display:none!important}@page{size:A4 landscape;margin:10mm}.wersja[hidden]{display:none}}
"""

JS = r"""
document.querySelectorAll('.tab').forEach(t=>t.addEventListener('click',()=>{const w=t.dataset.wersja;document.querySelectorAll('.tab').forEach(x=>x.setAttribute('aria-selected',String(x.dataset.wersja===w)));document.querySelectorAll('.wersja').forEach(s=>{s.hidden=s.dataset.wersja!==w;});}));
document.querySelectorAll('.wersja').forEach((s,i)=>{s.hidden=i!==0;});
const POZ={p3:{n:'Poziom III',k:'3 z 5',h:'4 tygodnie',t:28},p2:{n:'Poziom II',k:'4 z 5',h:'8 tygodni',t:56},p1:{n:'Poziom I',k:'4 z 5',h:'12 tygodni',t:84}};
const KLUCZ='eduplaner2026.moje-cele-kpof.v1';
const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function wczytaj(){try{const s=localStorage.getItem(KLUCZ);const t=s?JSON.parse(s):[];return Array.isArray(t)?t:[];}catch(e){return window.__moje||[];}}
function zapisz(l){try{localStorage.setItem(KLUCZ,JSON.stringify(l));}catch(e){window.__moje=l;}}
function dataPlus(dni){const d=new Date();d.setDate(d.getDate()+dni);return String(d.getDate()).padStart(2,'0')+'.'+String(d.getMonth()+1).padStart(2,'0')+'.'+d.getFullYear();}
const M=document.getElementById('kreator');
const pole=n=>M.querySelector('[data-p="'+n+'"]');
let ctx={};
function otworzKreator(k){
  ctx=k||{};
  M.querySelector('.ks').textContent=k.nr?('twierdzenie '+k.nr+' · obszar '+k.obszar+' · '+k.obszarNazwa+' · wersja '+k.wersja+' · '+k.wiek):'cel własny — z obserwacji pogłębionej albo zalecenia';
  M.querySelector('.kkrok b').textContent=k.tresc?('Twierdzenie KPOF: '+k.tresc):'Bez twierdzenia KPOF — wpisz zachowanie z obserwacji lub zalecenia';
  M.querySelector('.kkrok span').textContent=k.kod?('kod ICF · podstawa programowa: '+k.kod+' · źródło: ocena KPOF 1–2 → priorytet, obszar czerwony/żółty → wsparcie'):'źródło: karta ABC, ToM, kwestionariusz mowy, profil sensoryczny albo zalecenie z orzeczenia / WOPF';
  pole('dziecko').textContent=k.dziecko||'';
  pole('syt').textContent=k.syt||'';
  pole('zach').textContent=k.krok||'';
  pole('wsp').textContent=k.wsp||'';
  pole('pomiar').textContent=k.pomiar||'';
  pole('zrodlo').textContent=k.zrodlo||(k.nr?('KPOF, twierdzenie '+k.nr+' — ocena '+(k.ocena||'…')+' / 5'):'');
  ustawPoziom(k.lvl||'p2', !k.wsp);
  M.classList.add('open'); document.body.style.overflow='hidden';
}
function ustawPoziom(l, ustawKryt){
  ctx.lvl=l;
  M.querySelectorAll('.lvlsel button').forEach(b=>b.classList.toggle('on',b.dataset.l===l));
  if(ustawKryt!==false){pole('kryt').textContent=POZ[l].k+' sytuacji';pole('data').textContent=dataPlus(POZ[l].t)+' ('+POZ[l].h+')';}
  if(ctx.obszar&&ctx.wspTab&&(ustawKryt!==false)){pole('wsp').textContent=ctx.wspTab[l];}
  podglad();
}
function podglad(){
  const g=n=>(pole(n).textContent||'').trim();
  const d=g('dziecko')||'Dziecko', s=g('syt'), z=g('zach'), k=g('kryt'), w=g('wsp'), t=g('data'), p=g('pomiar');
  let zd='<b>'+esc(d)+'</b>';
  if(s) zd+=' '+esc(s)+',';
  zd+=' '+(z?esc(z):'<i style="color:#a8a3b8">[obserwowalne zachowanie]</i>');
  if(k) zd+=' w <b>'+esc(k)+'</b>';
  if(w) zd+=', '+esc(w);
  if(t) zd+=', do <b>'+esc(t)+'</b>';
  zd+='.'+(p?' Pomiar: '+esc(p)+'.':'');
  M.querySelector('.podglad .zd').innerHTML=zd;
  const ck={S:!!(s&&z),M:/\d\s*z\s*\d/.test(k),A:!!ctx.lvl,R:!!g('zrodlo'),T:/\d{2}\.\d{2}\.\d{4}/.test(t)};
  M.querySelectorAll('.smartck div').forEach(x=>x.classList.toggle('ok',!!ck[x.dataset.s]));
}
window.kpofRecompute=podglad;
M.addEventListener('input',podglad);
M.querySelectorAll('.lvlsel button').forEach(b=>b.addEventListener('click',()=>ustawPoziom(b.dataset.l)));
function tekstCelu(){const g=n=>(pole(n).textContent||'').trim();return (g('dziecko')||'Dziecko')+(g('syt')?' '+g('syt')+',':'')+' '+g('zach')+(g('kryt')?' w '+g('kryt'):'')+(g('wsp')?', '+g('wsp'):'')+(g('data')?', do '+g('data'):'')+'.'+(g('pomiar')?' Pomiar: '+g('pomiar')+'.':'');}
document.addEventListener('click',ev=>{
  const dodaj=ev.target.closest('.mkt-add');
  if(dodaj){ev.stopPropagation();const td=dodaj.closest('td.g');const k=kontekst(td);dodajCel({wersja:k.wersja,nr:k.nr,lvl:k.lvl,tekst:td.querySelector('.tresc').textContent+' — '+td.querySelector('.ram').textContent,pomiar:k.pomiar});rysuj(k.wersja);return;}
  const td=ev.target.closest('td.g');
  if(td){otworzKreator(kontekst(td));return;}
  if(ev.target.closest('[data-kreator]')){const w=document.querySelector('.tab[aria-selected="true"]').dataset.wersja;otworzKreator({wersja:w,wiek:document.querySelector('.tab[aria-selected="true"]').textContent.trim().slice(-8),lvl:'p2'});return;}
  if(ev.target.closest('[data-zamknij]')||ev.target===M){zamknij();return;}
  if(ev.target.closest('[data-zapisz]')){dodajCel({wersja:ctx.wersja||document.querySelector('.tab[aria-selected="true"]').dataset.wersja,nr:ctx.nr||'własny',lvl:ctx.lvl,tekst:tekstCelu(),pomiar:''});rysuj(ctx.wersja||document.querySelector('.tab[aria-selected="true"]').dataset.wersja);zamknij();return;}
  if(ev.target.closest('[data-kopiuj]')){navigator.clipboard&&navigator.clipboard.writeText(tekstCelu());ev.target.textContent='Skopiowano ✓';setTimeout(()=>ev.target.textContent='Kopiuj do IPET',1500);return;}
  if(ev.target.closest('[data-drukuj]')){window.print();return;}
  const us=ev.target.closest('[data-usun]');
  if(us){const l=wczytaj().filter(x=>x.id!==us.dataset.usun);zapisz(l);document.querySelectorAll('.wersja').forEach(s=>rysuj(s.dataset.wersja));return;}
});
document.addEventListener('keydown',ev=>{if(ev.key==='Escape')zamknij();});
function zamknij(){M.classList.remove('open');M.classList.remove('on');document.body.style.overflow='';}
function kontekst(td){const tr=td.closest('tr');return {wersja:td.dataset.wersja,wiek:td.dataset.wiek,nr:tr.dataset.nr,obszar:tr.dataset.obszar,obszarNazwa:tr.dataset.obszarNazwa,tresc:tr.dataset.tresc,kod:tr.dataset.kod,krok:tr.dataset.krok,syt:tr.dataset.syt,pomiar:tr.dataset.pomiar,lvl:td.dataset.lvl,wspTab:JSON.parse(tr.dataset.wsp)};}
function dodajCel(c){const l=wczytaj();c.id='c'+Date.now().toString(36);c.data=new Date().toISOString().slice(0,10);l.push(c);zapisz(l);}
function rysuj(w){const cel=document.querySelector('[data-moje="'+w+'"]');if(!cel)return;const m=wczytaj().filter(r=>r.wersja===w);cel.innerHTML='<h4>Moje cele · wersja '+w+' · '+m.length+'</h4>'+(m.length?m.map(r=>'<div class="mcel"><span class="mn">'+esc(r.nr)+' · '+esc((POZ[r.lvl]||{}).n||'')+'</span><span class="mt">'+esc(r.tekst)+'<span class="mp">zapisano '+esc(r.data)+(r.pomiar?' · pomiar: '+esc(r.pomiar):'')+'</span></span><button type="button" data-usun="'+r.id+'">usuń</button></div>').join('')+'<button type="button" class="chipbtn" data-drukuj>Drukuj moje cele (A4)</button>':'<div class="pusto">Jeszcze pusto — kliknij „+” przy celu w tabeli albo zapisz cel z kreatora.</div>');}
['A','B','C'].forEach(rysuj);
"""

def tabela(w, wiek, dane):
    tw = TW[w]; out = []
    aktualny = None
    for t in tw:
        nr = t['nr']; ob = t['obszar']
        if ob not in dane: pass
        krok, syt, pomiar = dane[nr]
        if ob != aktualny:
            aktualny = ob
            n_ob = sum(1 for x in tw if x['obszar'] == ob)
            out.append(f'<tr class="pas"><td colspan="5">Obszar {ob} · {esc(OBSZARY[ob])}<span class="li">{n_ob} twierdzeń · poziom zmienia warunki wsparcia, nie krok</span></td></tr>')
        attrs = f'data-nr="{nr}" data-obszar="{ob}" data-obszar-nazwa="{esc(OBSZARY[ob])}" data-tresc="{esc(t["tresc"])}" data-kod="{esc(t["kod"])}" data-krok="{esc(krok)}" data-syt="{esc(syt)}" data-pomiar="{esc(pomiar)}" data-wsp="{esc(json.dumps({"p3":WSPARCIE[ob][0],"p2":WSPARCIE[ob][1],"p1":WSPARCIE[ob][2]}, ensure_ascii=False))}"'
        cells = ''
        for lvl in ('p3','p2','p1'):
            k, h = KRYT[lvl]
            cells += f'<td class="g" data-lvl="{lvl}" data-wersja="{w}" data-wiek="{esc(wiek)}" tabindex="0" role="button" title="Otwórz kreator celu z tą treścią"><span class="tresc">{esc(cel(ob, krok, syt, lvl))}</span><span class="ram">{k} · {h}</span><button class="mkt-add" type="button" title="Dodaj do moich celów" aria-label="Dodaj do moich celów">+</button></td>'
        out.append(f'<tr {attrs}><td class="nr">{nr}</td><td class="wsk"><b>{esc(t["tresc"])}</b><span>krok obserwowalny: {esc(krok)}</span><span>{esc(t["kod"])} · pomiar: {esc(pomiar)}</span><span class="kzn">sytuacja: {esc(syt)}</span></td>{cells}</tr>')
    return ''.join(out)

def zloz():
    sekcje = ''
    razem = 0
    for w, (wiek, dane) in WERSJE.items():
        n = len(TW[w]); razem += n * 3
        sekcje += f'''<section class="wersja" id="w-{w}" data-wersja="{w}">
<div class="moje" data-moje="{w}"></div>
<table><colgroup><col style="width:5%"><col style="width:29%"><col style="width:22%"><col style="width:22%"><col style="width:22%"></colgroup>
<caption class="sr-only">Cele SMART · KPOF · wersja {w} · {esc(wiek)}</caption>
<thead><tr class="wband"><th colspan="5">EduPlaner 2026 · druk KPOF-T · cele SMART do twierdzeń Kwestionariusza Przedszkolnej Oceny Funkcjonalnej <b>wersja {w} · {esc(wiek)} · {n} twierdzeń</b></th></tr>
<tr><th>Nr</th><th>Twierdzenie KPOF · krok obserwowalny · ICF · PP</th><th class="p3">Poziom III</th><th class="p2">Poziom II</th><th class="p1">Poziom I</th></tr></thead>
<tbody>{tabela(w, wiek, dane)}</tbody></table></section>'''
    doc = f'''<!DOCTYPE html><html lang="pl"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tabela celów SMART · KPOF (przedszkole) — EduPlaner 2026 · PCTP</title><style>{FONT}\n{CSS}</style></head><body>
<div class="ark">
<div class="head"><span class="mark" role="img" aria-label="Logo PCTP"></span><div><h1>EduPlaner 2026</h1><div class="sub">KPOF · tabela celów SMART · wiek i poziom wsparcia · kreator własnego celu</div></div><div class="prawa"><b>KPOF · WOPF · IPET</b><span>narzędzie · druk KPOF-T</span></div></div>
<div class="kreska"></div>
<div class="tyt"><span class="pigula">{razem} celów SMART</span><p>130 twierdzeń Kwestionariusza Przedszkolnej Oceny Funkcjonalnej — dziewięć obszarów ICF, trzy wersje wiekowe — × trzy poziomy wsparcia. Wiersz mówi, <b>co dziecko zrobi albo powie, po czym widać, że twierdzenie się spełnia</b>; kolumna — ile przy tym dostaje podpory. Kliknięcie w cel otwiera <b>kreator celu</b>, który składa zdanie według jednej formuły ze skryptu szkolenia i sprawdza pięć liter SMART. Cel wpisujesz do IPET w brzmieniu z kreatora albo z komórki, z kryterium i horyzontem z nagłówka kolumny.</p></div>
<div class="sciezka">
<div class="krok"><span class="n">1</span><b>Odczytaj KPOF</b>twierdzenie ocenione na 1 lub 2 podlega osobnej analizie niezależnie od średniej (reguła nadrzędna); obszar czerwony to priorytet, żółty — wsparcie</div>
<div class="krok"><span class="n">2</span><b>Dołóż zalecenie</b>z orzeczenia, z opinii poradni albo z WOPF (obserwacja pogłębiona: ABC, ToM, mowa, profil sensoryczny) — cel musi z niego wynikać</div>
<div class="krok"><span class="n">3</span><b>Wybierz poziom</b>Poziom III — dorosły obok i podpora; II — podpowiedź w zasięgu; I — bez podpowiedzi. Osiągalny = jeden krok od tego, co dziecko robi dziś</div>
<div class="krok"><span class="n">4</span><b>Zapisz i zaplanuj pomiar</b>kryterium z celu jest gotowym wskaźnikiem ewaluacji: po pomiarze zamykasz cel, kontynuujesz, modyfikujesz albo idziesz do rodziców i poradni</div>
</div>
<div class="formula"><span class="lit">Formuła celu (skrypt, część 6):</span><span class="f s">Dziecko, w konkretnej sytuacji</span><span class="f s">wykona obserwowalne zachowanie</span><span class="f m">w N z M prób</span><span class="f a">przy określonym wsparciu</span><span class="f t">do określonej daty</span><span class="f r">z określonym sposobem pomiaru</span><button type="button" class="chipbtn pom" data-kreator>✎ Kreator własnego celu</button></div>
<div class="zakladki" role="tablist" aria-label="Wersje wiekowe"><button type="button" class="tab" role="tab" data-wersja="A" aria-selected="true"><span class="w">wersja A</span>3–4 lata</button><button type="button" class="tab" role="tab" data-wersja="B" aria-selected="false"><span class="w">wersja B</span>5 lat</button><button type="button" class="tab" role="tab" data-wersja="C" aria-selected="false"><span class="w">wersja C</span>6 lat</button></div>
<div class="legenda"><div class="leg l3"><b><i aria-hidden="true"></i>Poziom III</b>dorosły obok, podpowiedź wizualna i modelowanie, zadanie wykonywane razem<div class="kryt">kryterium 3 z 5 sytuacji · weryfikacja po 4 tygodniach</div></div><div class="leg l2"><b><i aria-hidden="true"></i>Poziom II</b>podpowiedź obrazkowa w zasięgu, dziecko wykonuje zadanie samo po pytaniu dorosłego<div class="kryt">kryterium 4 z 5 sytuacji · weryfikacja po 8 tygodniach</div></div><div class="leg l1"><b><i aria-hidden="true"></i>Poziom I</b>bez podpowiedzi obrazkowej, w naturalnej sytuacji z rówieśnikami<div class="kryt">kryterium 4 z 5 sytuacji · weryfikacja po 12 tygodniach</div></div></div>
<div class="uwaga"><b>Poziom zmienia warunki, nie krok.</b> Na każdym poziomie dziecko wykonuje to samo zachowanie z twierdzenia KPOF — tylko z inną ilością podpory. Kryterium na Poziomie I zostaje <b>4 z 5</b>, nie rośnie do 5 z 5: „za każdym razem” to w przedszkolu cel nie do osiągnięcia. <br><br><b>Cel opisuje zachowanie, które widać</b> — dwie różne osoby, patrząc na to samo dziecko, ocenią je tak samo. „Rozwijanie samodzielności” wyraża intencję, ale nie mówi, co ma się wydarzyć ani po czym poznamy, że się wydarzyło. „Zosia podczas przygotowania do wyjścia na dwór założy samodzielnie buty na rzepy w czterech z pięciu kolejnych dni, przy najwyżej jednej podpowiedzi słownej, do 19 grudnia; pomiar: karta obserwacji szatni” — jest celem.</div>
<div class="zrodla"><div class="zr"><b>Skąd cel z tabeli</b>twierdzenie KPOF ocenione na 1–2 albo obszar z profilu na czerwono/żółto → wiersz tabeli → kolumna według poziomu wsparcia z WOPF</div><div class="zr"><b>Skąd cel własny</b>zalecenie z orzeczenia lub opinii, wynik karty ABC (zachowanie zastępcze), ToM (tabela TOM-T), kwestionariusza mowy, profilu sensorycznego → kreator: zachowanie + sytuacja + kryterium + wsparcie + data + pomiar</div><div class="zr"><b>Dokąd trafia</b>karta sfery w IPET (cele SMART), plan pomocy pp (ścieżka B), karta ewaluacji: wartość osiągnięta i jedna z czterech decyzji zespołu</div></div>
{sekcje}
<div class="prawo"><b>Podstawa (wg skryptu szkolenia, wyd. 2 po audycie z 5.09.2026):</b> nazwa SMART nie pada w rozporządzeniu; wymagana jest ocena efektywności — § 6 rozp. MEN z 9.08.2017 r. w sprawie kształcenia specjalnego (t.j. Dz.U. 2020 poz. 1309): wielospecjalistyczna ocena co najmniej dwa razy w roku szkolnym; § 20 rozp. MEN z 9.08.2017 r. w sprawie pomocy psychologiczno-pedagogicznej (t.j. Dz.U. 2023 poz. 1798): nauczyciele i specjaliści oceniają efektywność udzielanej pomocy. Ocenić efektywność można tylko wtedy, gdy cel ma kryterium — „nazwa jest dowolna, mierzalność jest konieczna”. Twierdzenia KPOF odsyłają do podstawy programowej wychowania przedszkolnego (rozp. ME z 11.03.2026 r., Dz.U. 2026 poz. 378) i kodów ICF (WHO 2001).</div>
<div class="stopka"><span>EduPlaner 2026 · PCTP · pedagog specjalny <b>mgr Mirosława Ewa Jurczyszyn</b></span><span>druk KPOF-T · tabela drukuje się poziomo · {razem} celów · kreator celu · Moje cele w pamięci przeglądarki</span></div>
</div>
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
