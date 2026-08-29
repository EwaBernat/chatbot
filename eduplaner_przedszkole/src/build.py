# -*- coding: utf-8 -*-
"""Generator druku KC-1: Bank celów SMART do KPOF — układ tabelaryczny
w stylu Kącika Dyrektora (EduPlaner 2026 · PCTP)."""
import html, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dane_34, dane_5, dane_6

WERSJE = [dane_34, dane_5, dane_6]

POZIOMY = [
    ("p3", "Poziom III", "poniżej 2,0", "nasilona trudność", "4 tyg.",
     "pełne wsparcie, modelowanie, warunki uproszczone"),
    ("p2", "Poziom II", "2,0 – 2,9", "trudność", "8 tyg.",
     "wsparcie częściowe: plan obrazkowy, podpowiedź, przypomnienie"),
    ("p1", "Poziom I", "3,0 – 3,9", "w granicach oczekiwań", "12 tyg.",
     "samodzielność i przeniesienie na nową sytuację"),
]

CSS = """
:root{
  --ink:#2D1B69; --indigo:#4F3AA8; --violet:#6C4CC4; --accent:#E8450A; --on-accent:#FFFFFF;
  --p3:#C2410C; --p3-bg:#FEF9F6; --p2:#9A6B08; --p2-bg:#FDFAF2; --p1:#0F7B5A; --p1-bg:#F5FAF8;
  --zas:#2B6E6E; --zas-bg:#EAF3F3;
  --icf:#C1121F; --icf-bg:#FFFFFF; --pp:#4F3AA8; --pp-bg:#FFFFFF;
  --p3-br:#EFCBBB; --p2-br:#E8D6AC; --p1-br:#BEDFD1; --icf-br:#EEC4C4; --pp-br:#CFC6EE;
  --paper:#FFFFFF; --field:#EFEAF9; --soft:#F6F3FC; --row:#FEFDFF; --row-alt:#F4F0FD;
  --line:#E3DCF5; --line-2:#EDE8F8; --text:#2F2A3E; --muted:#8A8498;
  --strong:#2D1B69; --on-strong:#FFFFFF;
  --h-p3:#4F3AA8; --h-p3-t:#FFFFFF; --h-p2:#4F3AA8; --h-p2-t:#FFFFFF; --h-p1:#4F3AA8; --h-p1-t:#FFFFFF;
  --h-icf:#4F3AA8; --h-icf-t:#FFFFFF; --h-pp:#4F3AA8; --h-pp-t:#FFFFFF;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ink:#C6B8F5; --indigo:#7C68D8; --violet:#A794E8; --accent:#FF7A45; --on-accent:#2A1207;
    --p3:#FFA07F; --p3-bg:#2F211C; --p2:#E7BB6B; --p2-bg:#2C2617; --p1:#63D3AA; --p1-bg:#16302A;
    --zas:#7FCFCF; --zas-bg:#152C2C;
    --icf:#FF8F8F; --icf-bg:#301C1C; --pp:#A794E8; --pp-bg:#241D42;
    --p3-br:#4A3228; --p2-br:#463A20; --p1-br:#22463A; --icf-br:#472A2A; --pp-br:#3A3167;
    --paper:#15121E; --field:#221C36; --soft:#1E1930; --row:#1A1628; --row-alt:#221C36;
    --line:#332B4D; --line-2:#2A2340; --text:#ECE8F7; --muted:#A79FC2;
    --strong:#2E2650; --on-strong:#EDE9FA;
    --h-p3:#2E2650; --h-p3-t:#EDE9FA; --h-p2:#2E2650; --h-p2-t:#EDE9FA; --h-p1:#2E2650; --h-p1-t:#EDE9FA;
    --h-icf:#2E2650; --h-icf-t:#EDE9FA; --h-pp:#2E2650; --h-pp-t:#EDE9FA;
  }
}
:root[data-theme="dark"]{
  --ink:#C6B8F5; --indigo:#7C68D8; --violet:#A794E8; --accent:#FF7A45; --on-accent:#2A1207;
  --p3:#FFA07F; --p3-bg:#2F211C; --p2:#E7BB6B; --p2-bg:#2C2617; --p1:#63D3AA; --p1-bg:#16302A;
  --zas:#7FCFCF; --zas-bg:#152C2C;
  --icf:#FF8F8F; --icf-bg:#301C1C; --pp:#A794E8; --pp-bg:#241D42;
    --p3-br:#4A3228; --p2-br:#463A20; --p1-br:#22463A; --icf-br:#472A2A; --pp-br:#3A3167;
  --paper:#15121E; --field:#221C36; --soft:#1E1930; --row:#1A1628; --row-alt:#221C36;
  --line:#332B4D; --line-2:#2A2340; --text:#ECE8F7; --muted:#A79FC2;
  --strong:#2E2650; --on-strong:#EDE9FA;
  --h-p3:#2E2650; --h-p3-t:#EDE9FA; --h-p2:#2E2650; --h-p2-t:#EDE9FA; --h-p1:#2E2650; --h-p1-t:#EDE9FA;
  --h-icf:#2E2650; --h-icf-t:#EDE9FA; --h-pp:#2E2650; --h-pp-t:#EDE9FA;
}
*{box-sizing:border-box}
body{margin:0; background:var(--paper); color:var(--text);
  font-family:"DM Sans",Arial,Helvetica,sans-serif; font-size:14px; line-height:1.5}
.sheet{max-width:1360px; margin:0 auto; padding:0 26px 80px}
.mono{font-family:"JetBrains Mono",ui-monospace,"Courier New",monospace}

/* ---------- nagłówek dokumentu (jak w Kąciku Dyrektora) ---------- */
.dochead{display:flex; align-items:flex-start; gap:16px; padding:26px 0 14px}
.mark{width:46px; height:46px; border-radius:50%; background:var(--strong); color:var(--on-strong); display:grid; place-items:center;
  font:700 10px/1 "DM Sans",Arial,sans-serif; letter-spacing:.06em; flex:none}
.wordmark{font:700 24px/1 "DM Sans",Arial,sans-serif; letter-spacing:-.01em; color:var(--ink)}
.wordsub{font-size:9.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--violet); font-weight:700; margin-top:6px; line-height:1.5}
.dochead .right{margin-left:auto; text-align:right}
.badge{display:inline-block; background:var(--accent); color:var(--on-accent); padding:7px 15px; border-radius:999px;
  font:700 10.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase}
.badge-sub{font-size:9.5px; letter-spacing:.18em; text-transform:uppercase; color:var(--muted); font-weight:700; margin-top:7px}
.twotone{height:3px; display:flex; margin-bottom:20px; border-radius:2px; overflow:hidden}
.twotone i{display:block; height:100%}
.twotone i:first-child{width:62%; background:var(--indigo)}
.twotone i:last-child{width:44%; background:var(--accent)}

/* ---------- pola do wypełnienia ---------- */
.fields{display:grid; grid-template-columns:1.45fr 1.2fr 1fr .9fr; gap:12px; margin-bottom:26px}
.field{background:var(--field); border:1px solid var(--line-2); border-radius:8px; padding:11px 15px; display:flex;
  align-items:baseline; gap:10px; min-height:44px}
.field b{font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.16em; text-transform:uppercase; color:var(--violet); white-space:nowrap}
.field .dots{flex:1; border-bottom:1px dotted var(--violet); opacity:.5; height:12px}
.field .val{font-weight:600; color:var(--ink)}

/* ---------- tytuł druku ---------- */
.titleblock{text-align:center; margin-bottom:30px}
.pillrow{display:flex; justify-content:center; margin-bottom:16px}
.pill-title{background:var(--accent); color:var(--on-accent); padding:8px 20px; border-radius:999px;
  font:700 10.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.13em; text-transform:uppercase}
.titleblock h1{font:700 clamp(27px,3.6vw,40px)/1.14 "DM Sans",Arial,sans-serif; letter-spacing:-.01em;
  color:var(--ink); margin:0}
.titleblock .sub{color:var(--accent); font-weight:700; font-size:15px; margin-top:10px}
.dashrow{display:flex; align-items:center; gap:16px; justify-content:center; margin-top:18px; color:var(--ink)}
.dashrow i{height:2px; width:74px; display:block; background:repeating-linear-gradient(90deg,var(--accent) 0 4px,transparent 4px 8px); opacity:.85}
.dashrow span{font:700 10.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.22em; text-transform:uppercase}

/* ---------- sekcja ---------- */
.sec{margin-top:34px; scroll-margin-top:70px}
.sec-h{display:flex; align-items:center; gap:12px; margin-bottom:12px}
.sq{background:var(--accent); color:var(--on-accent); width:26px; height:26px; border-radius:4px; display:grid; place-items:center;
  font:700 11px/1 "DM Sans",Arial,sans-serif; flex:none}
.sq.sq-ink{background:var(--ink); color:#FFFFFF}
.sec-h h2{font:700 15.5px/1.2 "DM Sans",Arial,sans-serif; letter-spacing:.08em; text-transform:uppercase; color:var(--ink); margin:0}
.sec-h .meta{font-family:"JetBrains Mono",monospace; font-size:10.5px; color:var(--muted); white-space:nowrap}
.sec-h .line{flex:1; height:1px; background:var(--line)}

/* ---------- tabela ---------- */
.tablewrap{overflow-x:auto; border:1px solid var(--line); border-radius:9px}
table{width:100%; border-collapse:collapse; min-width:1080px}
thead{display:table-header-group}
th{background:var(--strong); color:var(--on-strong); text-align:left; padding:10px 12px; vertical-align:middle;
  font:700 9.5px/1.25 "DM Sans",Arial,sans-serif; letter-spacing:.13em; text-transform:uppercase;
  border-right:1px solid rgba(255,255,255,.14)}
th:last-child{border-right:none}
th .hz{display:block; font-family:"JetBrains Mono",monospace; letter-spacing:.02em; font-size:9px; opacity:.72; margin-top:3px}
td{padding:9px 10px; border-bottom:1px solid var(--line-2); border-right:1px solid var(--line-2);
  vertical-align:top; font-size:12.5px; line-height:1.45}
td:last-child{border-right:none}
tbody tr:last-child td{border-bottom:none}
td.g{border-right:1px solid var(--line)}
td.g .cel{display:block}
td.icf .kod,td.pp .kod{display:inline-block}
td.tw .miara{border-top:1px solid var(--line-2); padding-top:6px}
tbody tr:nth-child(even) td{background:var(--paper)}
tbody tr:hover td.tw{background:var(--soft)}

.c-lp{width:38px} .c-tw{width:23%} .c-code{width:82px} .c-goal{width:18.5%}
td.lp{text-align:center; font-weight:700; color:var(--ink); background:var(--paper) !important; font-size:14px; padding-top:11px}
td.tw{font-weight:500; color:var(--ink)}
td.tw .miara{display:block; margin-top:8px; font-family:"JetBrains Mono",monospace; font-size:9.5px; color:var(--muted); line-height:1.4}
td.tw .miara b{color:var(--violet); font-family:"DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase; font-size:9px}
td.icf{font-family:"JetBrains Mono",monospace; font-weight:700; font-size:11px; color:var(--icf); background:var(--paper) !important; white-space:nowrap}
td.pp{font-family:"JetBrains Mono",monospace; font-weight:700; font-size:11px; color:var(--pp); background:var(--paper) !important; white-space:nowrap}
td.g{font-size:12px}
th.h-p3,th.h-p2,th.h-p1,th.h-icf,th.h-pp{background:var(--strong); color:var(--on-strong)}
th.h-p3{box-shadow:inset 0 -3px 0 var(--p3)} th.h-p2{box-shadow:inset 0 -3px 0 var(--p2)}
th.h-p1{box-shadow:inset 0 -3px 0 var(--p1)} th.h-icf{box-shadow:inset 0 -3px 0 var(--icf)}
th.h-pp{box-shadow:inset 0 -3px 0 var(--pp)}
th .kropka{display:inline-block; width:7px; height:7px; border-radius:50%; margin-right:6px; vertical-align:baseline}
th.h-p3 .kropka{background:var(--p3)} th.h-p2 .kropka{background:var(--p2)} th.h-p1 .kropka{background:var(--p1)}
th.h-icf .kropka{background:var(--icf)} th.h-pp .kropka{background:var(--pp)}
tbody tr td.p3{background:var(--p3-bg) !important; box-shadow:inset 3px 0 0 var(--p3-br)}
tbody tr td.p2{background:var(--p2-bg) !important; box-shadow:inset 3px 0 0 var(--p2-br)}
tbody tr td.p1{background:var(--p1-bg) !important; box-shadow:inset 3px 0 0 var(--p1-br)}

/* ---------- callout / zasób ---------- */
.callout{margin-top:12px; background:var(--soft); border-left:4px solid var(--violet); padding:13px 17px; font-size:12.5px; border-radius:0 8px 8px 0}
.callout.zas{background:var(--zas-bg); border-left-color:var(--zas)}
.callout .cap{font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase; color:var(--zas); display:block; margin-bottom:5px}
.callout.rule{background:#FFF7F2; border-left-color:var(--accent)}
.callout.rule .cap{color:var(--accent)}

/* ---------- legenda ---------- */
.legendbox{background:var(--soft); border:1px solid var(--line-2); border-radius:9px; padding:16px 20px; font-size:12.5px; line-height:1.65}
.legendbox .k{font-weight:700; color:var(--ink)}
.legendbox .kk{font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase; color:var(--violet); display:block; margin-bottom:7px}
.legendbox .k-icf{color:var(--icf); font-family:"JetBrains Mono",monospace; font-weight:700}
.legendbox .k-pp{color:var(--pp); font-family:"JetBrains Mono",monospace; font-weight:700}

/* ---------- pasek narzędzi (tylko ekran) ---------- */
.toolbar{position:sticky; top:0; z-index:20; background:var(--paper); border-bottom:1px solid var(--line);
  padding:11px 0; margin-top:30px; display:flex; flex-wrap:wrap; gap:9px 16px; align-items:center}
.tab{border:1px solid var(--line); background:var(--paper); color:var(--ink); padding:8px 14px; border-radius:7px;
  font:700 12px/1 "DM Sans",Arial,sans-serif; cursor:pointer; display:flex; gap:7px; align-items:center}
.tab .kod{font-family:"JetBrains Mono",monospace; font-size:10px; opacity:.65}
.tab[aria-selected="true"]{background:var(--strong); color:var(--on-strong); border-color:var(--strong)}
.tools{margin-left:auto; display:flex; gap:7px; align-items:center; flex-wrap:wrap}
.tools .lab{font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase; color:var(--muted)}
.chipbtn{border:1px solid var(--line); background:var(--paper); color:var(--violet); padding:7px 10px; border-radius:7px;
  font:700 11px/1 "DM Sans",Arial,sans-serif; cursor:pointer; letter-spacing:.05em}
.chipbtn[data-lvl]{display:inline-flex; align-items:center; gap:7px}
.chipbtn[data-lvl]::before{content:""; width:7px; height:7px; border-radius:50%}
.chipbtn.b-p3::before{background:var(--p3)} .chipbtn.b-p2::before{background:var(--p2)} .chipbtn.b-p1::before{background:var(--p1)}
.chipbtn[data-lvl][aria-pressed="true"]{background:var(--strong); border-color:var(--strong); color:var(--on-strong)}
.chipbtn.b-p3[aria-pressed="true"]{box-shadow:inset 0 -3px 0 var(--p3)}
.chipbtn.b-p2[aria-pressed="true"]{box-shadow:inset 0 -3px 0 var(--p2)}
.chipbtn.b-p1[aria-pressed="true"]{box-shadow:inset 0 -3px 0 var(--p1)}
.chipbtn[data-lvl][aria-pressed="false"]{opacity:.55}
#drukuj{background:var(--strong); border-color:var(--strong); color:var(--on-strong)}
input[type="search"]{border:1px solid var(--line); background:var(--paper); color:var(--text); padding:8px 10px;
  border-radius:7px; font:400 12.5px/1.2 "DM Sans",Arial,sans-serif; width:180px}
input[type="search"]:focus,.tab:focus-visible,.chipbtn:focus-visible,.navlink:focus-visible{outline:2px solid var(--accent); outline-offset:2px}

/* ---------- nagłówek wersji ---------- */
.vband{display:flex; flex-wrap:wrap; align-items:center; gap:14px; background:var(--strong); color:var(--on-strong);
  padding:14px 20px; border-radius:9px; margin-top:30px}
.vband .vlet{background:var(--accent); color:var(--on-accent); min-width:34px; height:34px; border-radius:6px;
  display:inline-flex; align-items:center; justify-content:center; padding:0 9px; white-space:nowrap;
  font:700 15px/1 "DM Sans",Arial,sans-serif; letter-spacing:.02em}
.vband h2{font:700 16px/1.2 "DM Sans",Arial,sans-serif; letter-spacing:.09em; text-transform:uppercase; margin:0}
.vband .vmeta{margin-left:auto; display:flex; gap:22px; font-family:"JetBrains Mono",monospace; font-size:11px}
.vband .vmeta b{display:block; font-family:"DM Sans",Arial,sans-serif; font-size:9px; letter-spacing:.14em;
  text-transform:uppercase; opacity:.7; font-weight:700; margin-bottom:2px}
.vdesc{font-size:12.5px; color:var(--muted); margin:10px 0 0; max-width:100ch}
.areanav{display:flex; flex-wrap:wrap; gap:5px; margin-top:12px}
.navlink{text-decoration:none; border:1px solid var(--line); color:var(--violet); padding:5px 9px; border-radius:6px;
  font:700 10.5px/1 "DM Sans",Arial,sans-serif}
.navlink:hover{border-color:var(--accent); color:var(--accent)}

/* ---------- stopka ---------- */
.docfoot{margin-top:46px; padding-top:14px; border-top:1px solid var(--line); display:flex; flex-wrap:wrap;
  gap:8px 20px; justify-content:space-between; font-size:11px; color:var(--muted)}
.opts{display:flex; flex-wrap:wrap; gap:6px}
.opt{display:inline-flex; align-items:center; gap:6px; border:1px solid var(--line); border-radius:6px;
  padding:4px 8px; font-size:11.5px; background:var(--paper); white-space:nowrap}
.opt i{width:11px; height:11px; border:1.5px solid var(--violet); border-radius:3px; display:block; flex:none}
.podpisy{display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-top:18px}
.podpis{border:1px solid var(--line); border-radius:8px; background:var(--field); padding:13px 15px 26px}
.podpis b{font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase; color:var(--violet); display:block; margin-bottom:22px}
.podpis .dots{display:block; border-bottom:1px dotted var(--violet); opacity:.5}
.notatka{border:1px dashed var(--line); border-radius:8px; background:var(--paper); min-height:54px; margin-top:10px}
.hidden{display:none !important}
.nores{padding:30px 0; text-align:center; color:var(--muted)}
.printhead,.printfoot{display:none}
tr.tbanner{display:none}
tr.tbanner th{background:var(--indigo); color:#FFFFFF; font:700 6.4pt/1.3 "DM Sans",Arial,sans-serif;
  letter-spacing:.13em; text-transform:uppercase; padding:4pt 6pt; border-bottom:2px solid var(--accent)}
tr.tbanner .bsep{color:var(--accent); padding:0 5px}

@media (max-width:820px){
  .sheet{padding:0 14px 60px}
  .fields{grid-template-columns:1fr 1fr}
  .vband .vmeta{margin-left:0; flex-wrap:wrap; gap:14px}
}
@media (prefers-reduced-motion:reduce){*{transition:none !important; animation:none !important}}

/* ---------- druk A4 poziomo ---------- */
@page{size:A4 landscape; margin:11mm 9mm 13mm}
@media print{
  body{background:#fff; font-size:8.6pt; color:#1F1A33}
  *{-webkit-print-color-adjust:exact; print-color-adjust:exact}
  .sheet{max-width:none; padding:0}
  .toolbar,.areanav,.printhead{display:none !important}
  .vers{display:block !important}
  .vers + .vers{break-before:page; page-break-before:always}
  #konspekt{break-before:page; page-break-before:always}
  .podpisy{break-inside:avoid}
  tr.tbanner{display:table-row}
  table{min-width:0; font-size:8.4pt}
  th{padding:5pt 6pt; font-size:6.6pt; letter-spacing:.1em}
  td{padding:4pt 5pt; font-size:8.2pt; line-height:1.35}
  td.tw .miara{font-size:6.4pt}
  td.icf,td.pp{font-size:7.6pt}
  .tablewrap{overflow:visible; border-radius:0}
  tr{break-inside:avoid; page-break-inside:avoid}
  .sec{margin-top:9mm; break-inside:auto}
  .sec-h{break-after:avoid; page-break-after:avoid}
  .vband{break-after:avoid; page-break-after:avoid}
  .callout{break-inside:avoid}
  .titleblock h1{font-size:22pt}
  .fields{margin-bottom:8mm}
  .docfoot{display:none}
}
"""

JS = """
const tabs=[...document.querySelectorAll('.tab')];
const vers=[...document.querySelectorAll('.vers')];
function pokaz(kod){
  tabs.forEach(t=>t.setAttribute('aria-selected',String(t.dataset.v===kod)));
  vers.forEach(v=>v.classList.toggle('hidden',v.dataset.v!==kod));
  filtruj();
}
tabs.forEach(t=>t.addEventListener('click',()=>pokaz(t.dataset.v)));

const lvlBtns=[...document.querySelectorAll('.chipbtn[data-lvl]')];
const aktywne=new Set(['p3','p2','p1']);
lvlBtns.forEach(b=>b.addEventListener('click',()=>{
  const l=b.dataset.lvl;
  if(aktywne.has(l)&&aktywne.size>1) aktywne.delete(l); else aktywne.add(l);
  lvlBtns.forEach(x=>x.setAttribute('aria-pressed',String(aktywne.has(x.dataset.lvl))));
  ['p3','p2','p1'].forEach(l2=>{
    document.querySelectorAll('.col-'+l2).forEach(c=>c.classList.toggle('hidden',!aktywne.has(l2)));
  });
}));

const szukaj=document.getElementById('szukaj');
function filtruj(){
  const q=(szukaj.value||'').trim().toLowerCase();
  document.querySelectorAll('.vers:not(.hidden)').forEach(v=>{
    let widoczne=0;
    v.querySelectorAll('.sec').forEach(s=>{
      let n=0;
      s.querySelectorAll('tbody tr').forEach(tr=>{
        const ok=!q||tr.dataset.szukaj.includes(q);
        tr.classList.toggle('hidden',!ok);
        if(ok) n++;
      });
      s.classList.toggle('hidden',n===0);
      widoczne+=n;
    });
    v.querySelector('.nores').classList.toggle('hidden',widoczne>0);
  });
}
szukaj.addEventListener('input',filtruj);
document.getElementById('drukuj').addEventListener('click',()=>window.print());
"""

def esc(s): return html.escape(str(s), quote=False)

def wiersz(it, w):
    pp = it["pp"][3:] if it["pp"].startswith("PP ") else it["pp"]
    szukaj = " ".join([it["t"], it["g3"], it["g2"], it["g1"], it["icf"], it["pp"],
                       w["etykieta"], "wersja " + w["kod"]]).lower()
    return f"""        <tr data-szukaj="{esc(szukaj)}">
          <td class="lp">{it['n']}</td>
          <td class="tw">{esc(it['t'])}<span class="miara"><b>Miara:</b> {esc(it['m'])}</span></td>
          <td class="icf"><span class="kod">{esc(it['icf'])}</span></td>
          <td class="pp"><span class="kod">{esc(pp)}</span></td>
          <td class="g p3 col-p3"><span class="cel">{esc(it['g3'])}</span></td>
          <td class="g p2 col-p2"><span class="cel">{esc(it['g2'])}</span></td>
          <td class="g p1 col-p1"><span class="cel">{esc(it['g1'])}</span></td>
        </tr>"""

def sekcja(a, w):
    rows = "\n".join(wiersz(i, w) for i in a["items"])
    aid = f"{w['kod']}-{a['icf']}-{a['rom']}"
    return f"""  <section class="sec" id="{aid}">
    <div class="sec-h">
      <span class="sq">{a['rom']}</span>
      <h2>{esc(a['name'])}</h2>
      <span class="line"></span>
      <span class="meta">{esc(w['etykieta'])} · wersja {w['kod']} · {a['icf']} · Σ {a['pts']} pkt</span>
    </div>
    <div class="tablewrap">
    <table>
      <thead>
        <tr class="tbanner"><th colspan="7">EduPlaner 2026 · druk KC-1 · bank celów SMART<span class="bsep">·</span>Wersja {w['kod']} · {esc(w['etykieta'])}<span class="bsep">·</span>Obszar {a['rom']} · {esc(a['name'])}<span class="bsep">·</span>ICF {a['icf']}</th></tr>
        <tr>
          <th class="c-lp">Lp.</th>
          <th class="c-tw">Twierdzenie KPOF · obserwowane zachowanie</th>
          <th class="c-code h-icf"><span class="kropka"></span>ICF</th>
          <th class="c-code h-pp"><span class="kropka"></span>Podstawa</th>
          <th class="c-goal h-p3 col-p3"><span class="kropka"></span>Poziom III<span class="hz">ewaluacja 4 tyg.</span></th>
          <th class="c-goal h-p2 col-p2"><span class="kropka"></span>Poziom II<span class="hz">ewaluacja 8 tyg.</span></th>
          <th class="c-goal h-p1 col-p1"><span class="kropka"></span>Poziom I<span class="hz">ewaluacja 12 tyg.</span></th>
        </tr>
      </thead>
      <tbody>
{rows}
      </tbody>
    </table>
    </div>
    <div class="callout zas"><span class="cap">Zasób 4,0–5,0 · dźwignia</span>{esc(a['zasob'])}</div>
  </section>"""

def wersja(mod, aktywna):
    w = mod.WERSJA
    n = sum(len(a["items"]) for a in mod.AREAS)
    secs = "\n".join(sekcja(a, w) for a in mod.AREAS)
    nav = "\n".join(
        f'    <a class="navlink" href="#{w["kod"]}-{a["icf"]}-{a["rom"]}">{a["rom"]} · {esc(a["name"].split(" (")[0])}</a>'
        for a in mod.AREAS)
    return f"""<div class="vers{'' if aktywna else ' hidden'}" data-v="{w['kod']}">
  <div class="vband">
    <span class="vlet">{w['kod']}</span>
    <h2>Wersja {w['kod']} · {esc(w['etykieta'])}</h2>
    <div class="vmeta">
      <span><b>Obszary ICF</b>{len(mod.AREAS)}</span>
      <span><b>Twierdzenia</b>{n}</span>
      <span><b>Cele SMART</b>{n*3}</span>
      <span><b>Zakres</b>d1–d9</span>
    </div>
  </div>
  <p class="vdesc">{esc(w['opis'])}</p>
  <nav class="areanav" aria-label="Obszary wersji {w['kod']}">
{nav}
  </nav>
  <p class="nores hidden">Brak twierdzeń pasujących do wyszukiwania.</p>
{secs}
</div>"""


def konspekt():
    """Druk KC-2 — konspekt zajęć spięty z bankiem celów KC-1 (przykład wypełniony)."""
    cele = [
        ("KC-1 / B / 8", "d240", "2.9·2.12", "p2", "Poziom II",
         "Poczeka na swoją kolej 2 minuty w zabawie z regułą, korzystając z wizualnej kolejki — w 3 z 5 sytuacji.",
         "zabawa z regułą · rejestr zachowań w kolejce"),
        ("KC-1 / B / 31", "d720", "1.2·1.3", "p2", "Poziom II",
         "Zgłosi 1 własny pomysł w pracy w parze i uzgodni podział materiału — w 3 z 5 zadań.",
         "karta pracy zespołowej · obserwacja"),
        ("KC-1 / B / 19", "d440", "9.6", "p1", "Poziom I",
         "Utrzyma prawidłowy chwyt przez całą pracę i zamaluje pole bez przedzierania kartki — w 3 z 5 prac.",
         "obserwacja chwytu · karta prac graficznych"),
    ]
    cele_rows = "\n".join(f"""        <tr>
          <td class="lp">{i}</td>
          <td class="tw"><b>{esc(nr)}</b><span class="miara"><b>Miara:</b> {esc(miara)}</span></td>
          <td class="icf"><span class="kod">{esc(icf)}</span></td>
          <td class="pp"><span class="kod">{esc(pp)}</span></td>
          <td class="g {kl}"><span class="cel"><b style="color:var(--{kl})">{esc(poz)}</b> — {esc(tresc)}</span></td>
        </tr>""" for i, (nr, icf, pp, kl, poz, tresc, miara) in enumerate(cele, 1))

    przebieg = [
        ("Powitanie", "5 min",
         "Krąg powitalny; pokazuje tablicę zasad i kartę „czekam na swoją kolej”; nazywa cel zajęć słowami dziecka.",
         "Siadają w kręgu, witają się imieniem sąsiada, wskazują swoje zdjęcie na karcie kolejki.",
         "tablica zasad · karty ze zdjęciami dzieci"),
        ("Część wstępna — rozgrzewka", "6 min",
         "Prowadzi zabawę ruchową „raz, dwa, trzy — buduje ten, kogo widzisz”; modeluje zatrzymanie na sygnał.",
         "Poruszają się po sali, zatrzymują na sygnał bębenka, sprawdzają, kto jest następny w kolejce.",
         "bębenek · klepsydra 2-minutowa"),
        ("Część główna — zadanie zespołowe", "14 min",
         "Dzieli dzieci na trójki, rozdaje po jednym zestawie klocków na zespół (celowy niedobór materiału); "
         "ustawia klepsydrę; wspiera uzgadnianie kolejności, nie rozstrzyga za dzieci.",
         "Budują wspólną wieżę: każde dokłada jeden klocek w swojej kolejce, w czasie oczekiwania trzyma "
         "kartę kolejki; uzgadniają, kto zaczyna i co budują.",
         "klocki (1 zestaw na 3 dzieci) · karty kolejki · klepsydra"),
        ("Prezentacja i nazwanie", "7 min",
         "Zaprasza zespoły do pokazania budowli; pyta: „co było trudne, gdy trzeba było poczekać?”; "
         "nazywa emocję czekania i strategię, której dziecko użyło.",
         "Pokazują wieżę, mówią jednym zdaniem, czyj był pomysł; nazywają, co czuły, czekając.",
         "koło emocji · zdjęcia budowli"),
        ("Podsumowanie i ewaluacja", "3 min",
         "Podsumowuje zasadę dnia; zaznacza w rejestrze, ile razy dziecko doczekało swojej kolei.",
         "Przyklejają żeton na tablicy „udało mi się poczekać”.",
         "rejestr obserwacji · żetony"),
    ]
    przebieg_rows = "\n".join(f"""        <tr>
          <td class="lp">{i}</td>
          <td class="tw"><b>{esc(etap)}</b><span class="miara"><b>Czas:</b> {esc(czas)}</span></td>
          <td class="g"><span class="cel">{esc(naucz)}</span></td>
          <td class="g"><span class="cel">{esc(dziec)}</span></td>
          <td>{esc(pomoce)}</td>
        </tr>""" for i, (etap, czas, naucz, dziec, pomoce) in enumerate(przebieg, 1))

    dost = [
        ("p3", "Poziom III",
         "Dziecko buduje w parze z dorosłym; kolejka skrócona do 2 osób, czas oczekiwania 30 sekund; "
         "dorosły podaje kartę kolejki do ręki i towarzyszy fizycznie.",
         "przedmiot do trzymania w czasie czekania · skrócona klepsydra 30 s"),
        ("p2", "Poziom II",
         "Zespół 3-osobowy, kolejka wizualna na stole, uprzedzenie „za chwilę Twoja kolej”; "
         "dorosły obok, wkracza tylko przy narastaniu napięcia.",
         "karta kolejki · klepsydra 2 min · umówiony gest wsparcia"),
        ("p1", "Poziom I",
         "Zespół sam ustala kolejność i zasadę podziału klocków; dziecko może pełnić rolę „strażnika kolejki” "
         "i przypominać zasadę innym w akceptowalnej formie.",
         "rola strażnika kolejki · samoocena na skali obrazkowej"),
    ]
    dost_rows = "\n".join(f"""        <tr>
          <td class="lp {kl}">{poz.split()[1]}</td>
          <td class="tw"><b style="color:var(--{kl})">{esc(poz)}</b></td>
          <td class="g {kl}"><span class="cel">{esc(opis)}</span></td>
          <td>{esc(pomoc)}</td>
        </tr>""" for kl, poz, opis, pomoc in dost)

    ewal = [
        ("KC-1 / B / 8", "Liczba sytuacji, w których dziecko doczekało swojej kolei bez reakcji zakłócającej", "3 z 5"),
        ("KC-1 / B / 31", "Zgłoszenie własnego pomysłu w zespole i uzgodnienie podziału materiału", "3 z 5"),
        ("KC-1 / B / 19", "Utrzymanie prawidłowego chwytu przez całą pracę graficzną", "3 z 5"),
    ]
    ewal_rows = "\n".join(f"""        <tr>
          <td class="lp">{i}</td>
          <td class="tw"><b>{esc(nr)}</b></td>
          <td>{esc(kryt)}</td>
          <td class="pp"><span class="kod">{esc(prog)}</span></td>
          <td><span class="opts"><span class="opt"><i></i>osiągnięty</span><span class="opt"><i></i>częściowo</span><span class="opt"><i></i>niezrealizowany</span></span></td>
        </tr>""" for i, (nr, kryt, prog) in enumerate(ewal, 1))

    return f"""<section class="sec" id="konspekt">
  <div class="vband">
    <span class="vlet">KC-2</span>
    <h2>Konspekt zajęć · druk KC-2</h2>
    <div class="vmeta">
      <span><b>Powiązanie</b>cele z druku KC-1</span>
      <span><b>Wersja KPOF</b>B · 5 lat</span>
      <span><b>Czas</b>35 minut</span>
      <span><b>Status</b>wzór wypełniony</span>
    </div>
  </div>
  <p class="vdesc">Konspekt nie powiela celów — cytuje je z banku po numerze twierdzenia, razem z kodem ICF
  i punktem podstawy programowej. Dzięki temu zapis w dzienniku, w IPET i w arkuszu KPOF mówi tym samym kodem.
  Poniżej wzór wypełniony; pola nadpisuje się własną treścią.</p>

  <div class="fields" style="grid-template-columns:1.6fr 1fr 1fr 1fr">
    <div class="field"><b>Temat</b><span class="val">„Wieża po kolei” — budowanie w zespole z regułą kolejki</span></div>
    <div class="field"><b>Grupa</b><span class="val">Biedronki · 5-latki</span></div>
    <div class="field"><b>Data</b><span class="dots"></span></div>
    <div class="field"><b>Prowadzący</b><span class="dots"></span></div>
  </div>

  <div class="sec-h" style="margin-top:24px"><span class="sq">1</span><h2>Cele z banku KC-1</h2><span class="line"></span>
    <span class="meta">numer twierdzenia · ICF · podstawa · poziom</span></div>
  <div class="tablewrap"><table>
    <thead><tr>
      <th class="c-lp">Lp.</th><th class="c-tw">Cel z banku · miara</th>
      <th class="c-code h-icf"><span class="kropka"></span>ICF</th>
      <th class="c-code h-pp"><span class="kropka"></span>Podstawa</th>
      <th>Poziom wsparcia i treść celu SMART</th>
    </tr></thead>
    <tbody>
{cele_rows}
    </tbody>
  </table></div>

  <div class="sec-h" style="margin-top:24px"><span class="sq">2</span><h2>Przebieg zajęć</h2><span class="line"></span>
    <span class="meta">5 etapów · 35 minut</span></div>
  <div class="tablewrap"><table>
    <thead><tr>
      <th class="c-lp">Lp.</th><th class="c-tw">Etap · czas</th>
      <th style="width:29%">Czynności nauczyciela</th>
      <th style="width:29%">Czynności dzieci</th>
      <th style="width:17%">Pomoce</th>
    </tr></thead>
    <tbody>
{przebieg_rows}
    </tbody>
  </table></div>
  <div class="callout"><span class="cap" style="color:var(--violet)">Metody i formy</span>
  <b>Metody:</b> zabawa z regułą · modelowanie · zadanie z celowym niedoborem materiału · wzmocnienie pozytywne ·
  nazywanie emocji. &nbsp;<b>Formy:</b> praca z całą grupą (krąg) · zespoły 3-osobowe · praca indywidualna przy stoliku.</div>

  <div class="sec-h" style="margin-top:24px"><span class="sq">3</span><h2>Dostosowania wg poziomu wsparcia</h2><span class="line"></span>
    <span class="meta">ta sama aktywność · trzy progi wymagań</span></div>
  <div class="tablewrap"><table>
    <thead><tr>
      <th class="c-lp">Poz.</th><th class="c-tw">Poziom</th>
      <th style="width:48%">Jak zmieniamy warunki zadania</th><th style="width:26%">Pomoce dodatkowe</th>
    </tr></thead>
    <tbody>
{dost_rows}
    </tbody>
  </table></div>

  <div class="sec-h" style="margin-top:24px"><span class="sq">4</span><h2>Ewaluacja zajęć</h2><span class="line"></span>
    <span class="meta">kryterium sukcesu → wynik</span></div>
  <div class="tablewrap"><table>
    <thead><tr>
      <th class="c-lp">Lp.</th><th class="c-tw">Cel</th><th style="width:38%">Kryterium sukcesu</th>
      <th class="c-code h-pp"><span class="kropka"></span>Próg</th><th style="width:27%">Wynik — zaznacz</th>
    </tr></thead>
    <tbody>
{ewal_rows}
    </tbody>
  </table></div>
  <div class="callout rule"><span class="cap">Uwagi zespołu · wnioski do kolejnych zajęć</span>
  <div class="notatka"></div></div>

  <div class="podpisy">
    <div class="podpis"><b>Prowadzący zajęcia</b><span class="dots"></span></div>
    <div class="podpis"><b>Specjalista wspierający</b><span class="dots"></span></div>
    <div class="podpis"><b>Data i podpis koordynatora</b><span class="dots"></span></div>
  </div>
</section>"""


def build():
    dzis = datetime.date.today().strftime("%d.%m.%Y")
    razem = sum(sum(len(a["items"]) for a in m.AREAS) for m in WERSJE)

    progi = [("zas", "Zasób", "4,0 – 5,0", "mocna strona",
              "Bez celu naprawczego — zasób staje się dźwignią: dziecko dostaje rolę w grupie, "
              "która wykorzystuje tę umiejętność do pracy nad obszarem słabszym.", "—")]
    for kod, nazwa, prog, znacz, hor, dzial in POZIOMY[::-1]:
        progi.append((kod, nazwa, prog, znacz, dzial, hor))
    progi_rows = "\n".join(f"""        <tr>
          <td class="lp {k}">{esc(nazwa[:1] if k=='zas' else nazwa.split()[1])}</td>
          <td class="tw"><b style="color:var(--{k})">{esc(nazwa)}</b></td>
          <td class="mono" style="white-space:nowrap; font-weight:700">{esc(prog)}</td>
          <td>{esc(znacz)}</td>
          <td>{esc(dzial)}</td>
          <td class="mono" style="white-space:nowrap; font-weight:700; color:var(--violet)">{esc(hor)}</td>
        </tr>""" for k, nazwa, prog, znacz, dzial, hor in progi)

    smart_rows = "\n".join(f"""        <tr>
          <td class="lp">{L}</td>
          <td class="tw"><b>{esc(n)}</b></td>
          <td colspan="4">{esc(o)}</td>
        </tr>""" for L, n, o in [
        ("S", "Konkretny (specific)", "Zachowanie wprost z twierdzenia KPOF — obserwowalne w sali, nigdy „poprawa funkcjonowania”."),
        ("M", "Mierzalny (measurable)", "Kryterium liczbowe w każdym celu: ile z ilu prób, przez ile minut, w ilu dniach tygodnia. Narzędzie pomiaru podane w kolumnie twierdzenia."),
        ("A", "Osiągalny (achievable)", "Poziom wsparcia dobrany do wyniku obszaru — cel stawiamy o jeden krok powyżej tego, co dziecko robi dziś."),
        ("R", "Istotny (relevant)", "Każdy cel niesie kod ICF i punkt podstawy programowej z arkusza KPOF — ta sama para trafia do WOPF i IPET."),
        ("T", "Określony w czasie (timed)", "Horyzont wynika z poziomu wsparcia: Poziom III — 4 tygodnie, Poziom II — 8 tygodni, Poziom I — 12 tygodni."),
    ])

    tabs = "\n".join(
        f'    <button class="tab" role="tab" data-v="{m.WERSJA["kod"]}" aria-selected="{"true" if i==0 else "false"}">'
        f'{esc(m.WERSJA["etykieta"])}<span class="kod">wersja {m.WERSJA["kod"]}</span></button>'
        for i, m in enumerate(WERSJE))
    wersje_html = "\n".join(wersja(m, i == 0) for i, m in enumerate(WERSJE))

    return f"""<title>Bank Celów SMART KPOF</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;700&display=swap">
<style>{CSS}</style>

<div class="sheet">

<div class="dochead">
  <span class="mark">PCTP</span>
  <div>
    <div class="wordmark">EduPlaner 2026</div>
    <div class="wordsub">Bank celów SMART ·<br>Przedszkolna Ocena Funkcjonalna</div>
  </div>
  <div class="right">
    <span class="badge">Nauczyciel · zespół</span>
    <div class="badge-sub">Dokument wsparcia · {dzis}</div>
  </div>
</div>
<div class="twotone"><i></i><i></i></div>

<div class="fields">
  <div class="field"><b>Przedszkole</b><span class="dots"></span></div>
  <div class="field"><b>Dziecko</b><span class="dots"></span></div>
  <div class="field"><b>Grupa</b><span class="dots"></span></div>
  <div class="field"><b>Rok szkolny</b><span class="val">2026 / 2027</span></div>
</div>

<div class="titleblock">
  <div class="pillrow"><span class="pill-title">KPOF · przedszkole · druk KC-1 · bank celów SMART</span></div>
  <h1>Bank celów SMART</h1>
  <div class="sub">trzy poziomy wsparcia dla każdego twierdzenia — z kodem ICF i punktem podstawy programowej</div>
  <div class="dashrow"><i></i><span>Druk KC-1 · twierdzenie · ICF · podstawa · poziom</span><i></i></div>
</div>

<section class="sec">
  <div class="sec-h"><span class="sq sq-ink">§</span><h2>Legenda dokumentu</h2><span class="line"></span></div>
  <div class="legendbox">
    <span class="k">KPOF</span> — Kwestionariusz Przedszkolnej Oceny Funkcjonalnej, narzędzie autorskie oparte na podstawie
    programowej wychowania przedszkolnego i klasyfikacji ICF (WHO). &nbsp;·&nbsp;
    <span class="k">Wersja A</span> — 3–4 lata, 42 twierdzenia &nbsp;·&nbsp;
    <span class="k">Wersja B</span> — 5 lat, 44 twierdzenia &nbsp;·&nbsp;
    <span class="k">Wersja C</span> — 6 lat, 44 twierdzenia. &nbsp;·&nbsp;
    <span class="k-icf">ICF</span> — kod klasyfikacji WHO (d1–d9), zapisany <b style="color:var(--icf)">czerwienią</b>; wspólny język
    z WOPF i IPET. &nbsp;·&nbsp;
    <span class="k-pp">Podstawa</span> — punkt podstawy programowej w zapisie <i>obszar.punkt</i>, zapisany
    <b style="color:var(--pp)">niebieskim</b>; obszary podstawy: 1 społeczny · 2 osobisty · 3 językowy · 4 matematyczny ·
    5 przyrodniczy · 6 techniczny · 7 cyfrowy · 8 artystyczny · 9 ruchowy. &nbsp;·&nbsp;
    <span class="k">DE-R</span> — doświadczenie edukacyjne realizowane co najmniej raz w roku &nbsp;·&nbsp;
    <span class="k">WSR</span> — warunki i sposób realizacji podstawy &nbsp;·&nbsp;
    <span class="k">Zad.</span> — zadanie przedszkola. &nbsp;·&nbsp;
    <span class="k">Miara</span> — narzędzie, którym zespół sprawdza realizację celu. &nbsp;·&nbsp;
    <span class="k">Obszar VI</span> (życie domowe) ma charakter opisowy i nie wlicza się do wyniku ogólnego.
  </div>
</section>

<section class="sec">
  <div class="sec-h"><span class="sq">A</span><h2>Anatomia celu — formuła SMART</h2><span class="line"></span>
    <span class="meta">5 warunków · każdy cel w tym druku</span></div>
  <div class="tablewrap">
  <table>
    <thead><tr>
      <th class="c-lp">Litera</th><th class="c-tw">Warunek</th><th colspan="4">Jak jest spełniony w tym banku celów</th>
    </tr></thead>
    <tbody>
{smart_rows}
    </tbody>
  </table>
  </div>
</section>

<section class="sec">
  <div class="sec-h"><span class="sq">B</span><h2>Od wyniku KPOF do celu — progi kryterialne</h2><span class="line"></span>
    <span class="meta">średnia obszaru → wiersz do wpisania</span></div>
  <div class="tablewrap">
  <table>
    <thead><tr>
      <th class="c-lp">Poz.</th><th class="c-tw">Kwalifikacja</th><th class="c-code">Średnia</th>
      <th>Znaczenie</th><th>Co robimy w celu</th><th class="c-code">Horyzont</th>
    </tr></thead>
    <tbody>
{progi_rows}
    </tbody>
  </table>
  </div>
  <div class="callout rule"><span class="cap">Reguła nadrzędna</span>Każde pojedyncze twierdzenie ocenione na 1 lub 2 — niezależnie od średniej
  obszaru — podlega analizie jakościowej zespołu i bierze cel z kolumny <b>Poziom III</b>, nawet gdy cały obszar wypadł na
  Poziomie I. Ocen rodzica, nauczyciela i specjalisty nie uśredniamy mechanicznie — profile omawiamy obok siebie na spotkaniu zespołu.</div>
</section>

<div class="toolbar">
{tabs}
  <div class="tools">
    <span class="lab">Kolumny</span>
    <button class="chipbtn b-p3" data-lvl="p3" aria-pressed="true">Poziom III</button>
    <button class="chipbtn b-p2" data-lvl="p2" aria-pressed="true">Poziom II</button>
    <button class="chipbtn b-p1" data-lvl="p1" aria-pressed="true">Poziom I</button>
    <label for="szukaj" class="lab">Szukaj</label>
    <input type="search" id="szukaj" placeholder="np. emocje, kolejka, chwyt">
    <button class="chipbtn" id="drukuj">Drukuj A4</button>
  </div>
</div>

{wersje_html}

{konspekt()}

<div class="docfoot">
  <span>EduPlaner 2026 · PCTP · pedagog specjalny mgr Mirosława Ewa Jurczyszyn</span>
  <span class="mono">Druk KC-1 · {razem} twierdzeń · {razem*3} celów SMART · wersje A / B / C</span>
</div>

</div>
<script>{JS}</script>
"""

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "Bank_celow_SMART_KPOF.html")
    open(out, "w", encoding="utf-8").write(build())
    print("zapisano:", out, os.path.getsize(out), "B")
