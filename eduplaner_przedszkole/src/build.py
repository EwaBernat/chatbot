# -*- coding: utf-8 -*-
"""Generator dokumentu: Bank celów SMART KPOF (EduPlaner 2026 · PCTP)."""
import html, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dane_34, dane_5, dane_6

WERSJE = [dane_34, dane_5, dane_6]

POZIOMY = [
    ("p3", "III", "Poziom III", "poniżej 2,0", "nasilona trudność", "4 tygodnie",
     "pełne wsparcie dorosłego, modelowanie, warunki uproszczone"),
    ("p2", "II", "Poziom II", "2,0 – 2,9", "trudność", "8 tygodni",
     "wsparcie częściowe: podpowiedź wzrokowa, plan obrazkowy, przypomnienie"),
    ("p1", "I", "Poziom I", "3,0 – 3,9", "w granicach oczekiwań", "12 tygodni",
     "samodzielność i przeniesienie umiejętności na nową sytuację"),
]

CSS = """
:root{
  --ink:#2D1B69; --ink-soft:#4A3A8C; --accent:#E8450A; --accent-soft:#FDEDE6;
  --p3:#B8350D; --p3-bg:#FBEAE5; --p2:#C47A10; --p2-bg:#FBF2E1; --p1:#0D7D5C; --p1-bg:#E5F3ED;
  --zas:#2B6E6E; --zas-bg:#E6F0F0;
  --icf:#C1121F; --icf-bg:#FCEAEA; --pp:#12408A; --pp-bg:#E7EEFA;
  --paper:#FAF9FC; --card:#FFFFFF; --line:#E3DFEE; --line-soft:#EFECF6;
  --text:#241C3D; --muted:#6C6489; --band:#F3F0FA;
  --shadow:0 1px 2px rgba(45,27,105,.06), 0 8px 24px -18px rgba(45,27,105,.35);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ink:#C9BCF5; --ink-soft:#A99BE0; --accent:#FF7A45; --accent-soft:#3A2216;
    --p3:#FF9A7A; --p3-bg:#3A211A; --p2:#F0BC63; --p2-bg:#382C15; --p1:#5FD3A8; --p1-bg:#16332A;
    --zas:#7FCFCF; --zas-bg:#153030;
    --icf:#FF8F8F; --icf-bg:#3B1D1D; --pp:#8FBEFF; --pp-bg:#132840;
    --paper:#15121F; --card:#1D1830; --line:#332B4D; --line-soft:#272040;
    --text:#EDE9F8; --muted:#A79FC2; --band:#231D3A;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -20px rgba(0,0,0,.9);
  }
}
:root[data-theme="dark"]{
  --ink:#C9BCF5; --ink-soft:#A99BE0; --accent:#FF7A45; --accent-soft:#3A2216;
  --p3:#FF9A7A; --p3-bg:#3A211A; --p2:#F0BC63; --p2-bg:#382C15; --p1:#5FD3A8; --p1-bg:#16332A;
  --zas:#7FCFCF; --zas-bg:#153030;
  --icf:#FF8F8F; --icf-bg:#3B1D1D; --pp:#8FBEFF; --pp-bg:#132840;
  --paper:#15121F; --card:#1D1830; --line:#332B4D; --line-soft:#272040;
  --text:#EDE9F8; --muted:#A79FC2; --band:#231D3A;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -20px rgba(0,0,0,.9);
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--paper); color:var(--text);
  font-family:"DM Sans","Segoe UI",Arial,sans-serif; font-size:15px; line-height:1.55;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:1120px; margin:0 auto; padding:0 28px 96px}
h1,h2,h3,h4{font-family:Fraunces,Georgia,"Times New Roman",serif; text-wrap:balance; margin:0}
.mono{font-family:"JetBrains Mono",ui-monospace,"Courier New",monospace}

/* ---------- masthead ---------- */
.masthead{padding:52px 0 28px; border-bottom:3px solid var(--ink); position:relative}
.masthead::after{content:""; position:absolute; left:58%; right:0; bottom:-3px; height:3px; background:var(--accent)}
.brandline{display:flex; align-items:center; gap:14px; margin-bottom:26px}
.mark{width:42px; height:42px; border-radius:50%; background:var(--ink); color:#fff; display:grid; place-items:center;
  font-size:10px; font-weight:700; letter-spacing:.06em; font-family:"DM Sans",Arial,sans-serif; flex:none}
.brandname{font-family:Fraunces,Georgia,serif; font-size:21px; font-weight:600; color:var(--ink); line-height:1.1}
.brandsub{font-size:10.5px; letter-spacing:.19em; text-transform:uppercase; color:var(--muted); margin-top:3px}
.eyebrow{font-size:11px; letter-spacing:.22em; text-transform:uppercase; color:var(--accent); font-weight:700}
h1{font-size:clamp(34px,5.2vw,54px); font-weight:600; line-height:1.04; letter-spacing:-.02em; color:var(--ink); margin:14px 0 0}
.lede{max-width:62ch; margin-top:18px; font-size:16.5px; color:var(--text)}
.metastrip{display:flex; flex-wrap:wrap; gap:10px 34px; margin-top:26px; padding-top:20px; border-top:1px solid var(--line)}
.metastrip div{font-size:12.5px; color:var(--muted)}
.metastrip b{display:block; font-size:10.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--ink-soft); font-weight:700; margin-bottom:3px}

/* ---------- panels ---------- */
.panel{background:var(--card); border:1px solid var(--line); border-radius:3px; box-shadow:var(--shadow); margin-top:26px}
.panel-h{display:flex; align-items:baseline; gap:12px; padding:16px 22px; border-bottom:1px solid var(--line-soft)}
.panel-h h2{font-size:19px; font-weight:600; color:var(--ink)}
.panel-h span{font-size:11px; letter-spacing:.16em; text-transform:uppercase; color:var(--muted)}
.panel-b{padding:20px 22px}
.smartgrid{display:grid; grid-template-columns:repeat(auto-fit,minmax(180px,1fr)); gap:0; border-top:1px solid var(--line-soft)}
.smartgrid > div{padding:16px 20px; border-right:1px solid var(--line-soft)}
.smartgrid > div:last-child{border-right:none}
.smartgrid .letter{font-family:Fraunces,Georgia,serif; font-size:30px; font-weight:600; color:var(--accent); line-height:1}
.smartgrid .lbl{font-size:11px; letter-spacing:.14em; text-transform:uppercase; color:var(--ink-soft); font-weight:700; margin:8px 0 6px}
.smartgrid p{margin:0; font-size:13px; color:var(--muted); line-height:1.5}

table.progi{width:100%; border-collapse:separate; border-spacing:0; font-size:13.5px; min-width:720px}
table.progi th{text-align:left; font-size:10px; letter-spacing:.16em; text-transform:uppercase; color:#fff;
  background:var(--ink); padding:11px 14px; font-weight:700; white-space:nowrap}
table.progi th:first-child{padding-left:20px}
table.progi td{padding:14px; border-bottom:1px solid var(--line-soft); vertical-align:middle}
table.progi td.mono{white-space:nowrap; font-size:12.5px}
table.progi td:first-child{padding-left:16px; border-left:4px solid transparent}
table.progi tbody tr:nth-child(odd) td{background:var(--band)}
table.progi tbody tr:last-child td{border-bottom:none}
table.progi tr.r-zas td:first-child{border-left-color:var(--zas)}
table.progi tr.r-p1 td:first-child{border-left-color:var(--p1)}
table.progi tr.r-p2 td:first-child{border-left-color:var(--p2)}
table.progi tr.r-p3 td:first-child{border-left-color:var(--p3)}
.pill{display:inline-flex; align-items:center; gap:7px; padding:6px 11px; border-radius:999px; font:700 12.5px/1 "DM Sans",Arial,sans-serif; white-space:nowrap}
.pill.zas{color:var(--zas); background:var(--zas-bg)}
.pill.p1{color:var(--p1); background:var(--p1-bg)}
.pill.p2{color:var(--p2); background:var(--p2-bg)}
.pill.p3{color:var(--p3); background:var(--p3-bg)}
.hz-cell{font-family:"JetBrains Mono",monospace; font-size:12px; color:var(--ink-soft); background:var(--accent-soft);
  padding:5px 9px; border-radius:2px; display:inline-block; white-space:nowrap}

/* legenda kolorów kodów */
.legend{display:flex; flex-wrap:wrap; gap:10px 22px; padding:14px 22px; border-top:1px solid var(--line-soft); background:var(--band)}
.legend span{display:inline-flex; align-items:center; gap:8px; font-size:12px; color:var(--muted)}
.legend i{width:22px; height:11px; border-radius:2px; display:inline-block; font-style:normal}
.legend .l-icf{background:var(--icf-bg); border-left:3px solid var(--icf)}
.legend .l-pp{background:var(--pp-bg); border-left:3px solid var(--pp)}
.legend .l-wiek{background:var(--accent)}
.lvltag{display:inline-flex; align-items:center; gap:7px; font-weight:700; font-size:12.5px; white-space:nowrap}
.dot{width:9px; height:9px; border-radius:50%; flex:none}
.n-p3{color:var(--p3)} .d-p3{background:var(--p3)}
.n-p2{color:var(--p2)} .d-p2{background:var(--p2)}
.n-p1{color:var(--p1)} .d-p1{background:var(--p1)}
.n-zas{color:var(--zas)} .d-zas{background:var(--zas)}
.rule{display:flex; gap:14px; padding:16px 20px; background:var(--accent-soft); border-left:4px solid var(--accent); font-size:13.5px}
.rule b{color:var(--accent)}

/* ---------- toolbar ---------- */
.toolbar{position:sticky; top:0; z-index:20; background:var(--paper); border-bottom:1px solid var(--line);
  padding:12px 0; margin-top:34px; display:flex; flex-wrap:wrap; gap:10px 18px; align-items:center}
.tabs{display:flex; gap:6px}
.tab{border:1px solid var(--line); background:var(--card); color:var(--ink); padding:9px 15px; border-radius:2px;
  font:600 13px/1 "DM Sans",Arial,sans-serif; cursor:pointer; display:flex; align-items:center; gap:8px}
.tab:hover{border-color:var(--ink-soft)}
.tab[aria-selected="true"]{background:var(--ink); color:#fff; border-color:var(--ink)}
.tab .kod{font-family:"JetBrains Mono",monospace; font-size:11px; opacity:.7}
.filters{display:flex; gap:6px; align-items:center; margin-left:auto}
.filters .lab{font-size:10.5px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); font-weight:700}
.chipbtn{border:1px solid var(--line); background:var(--card); color:var(--muted); padding:7px 11px; border-radius:2px;
  font:700 11.5px/1 "DM Sans",Arial,sans-serif; cursor:pointer; letter-spacing:.06em}
.chipbtn[aria-pressed="true"]{background:var(--ink); border-color:var(--ink); color:#fff}
input[type="search"]{border:1px solid var(--line); background:var(--card); color:var(--text); padding:8px 11px;
  border-radius:2px; font:400 13px/1.2 "DM Sans",Arial,sans-serif; width:190px}
input[type="search"]:focus, .tab:focus-visible, .chipbtn:focus-visible, .navlink:focus-visible
  {outline:2px solid var(--accent); outline-offset:2px}

/* ---------- version ---------- */
.vhead{display:flex; flex-wrap:wrap; gap:18px 40px; align-items:flex-end; padding:30px 0 22px; border-bottom:1px solid var(--line)}
.vhead h2{font-size:30px; font-weight:600; color:var(--ink); letter-spacing:-.01em}
.vhead .vdesc{max-width:58ch; font-size:14px; color:var(--muted); margin-top:8px}
.counts{display:flex; gap:26px; margin-left:auto}
.counts div{text-align:right}
.counts .num{font-family:Fraunces,Georgia,serif; font-size:27px; color:var(--accent); line-height:1}
.counts .cl{font-size:10px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin-top:4px}
.areanav{display:flex; flex-wrap:wrap; gap:6px; padding:16px 0 6px}
.navlink{text-decoration:none; border:1px solid var(--line); color:var(--ink-soft); padding:6px 10px; border-radius:2px;
  font:700 11.5px/1 "DM Sans",Arial,sans-serif}
.navlink:hover{border-color:var(--accent); color:var(--accent)}

/* ---------- area ---------- */
.area{margin-top:40px; scroll-margin-top:80px}
.area-h{display:flex; align-items:center; gap:14px; background:var(--ink); color:#fff; padding:13px 18px; border-radius:2px}
.rom{background:var(--accent); color:#fff; font:700 13px/1 "DM Sans",Arial,sans-serif; padding:7px 9px; border-radius:2px; min-width:38px; text-align:center}
.area-h h3{font-size:17px; font-weight:600; letter-spacing:.01em; flex:1}
.area-h .code{font-family:"JetBrains Mono",monospace; font-size:11.5px; opacity:.8; white-space:nowrap;
  border-left:1px solid rgba(255,255,255,.28); padding-left:14px}
.wiek{display:inline-flex; align-items:center; gap:6px; font:700 10px/1 "DM Sans",Arial,sans-serif;
  letter-spacing:.15em; text-transform:uppercase; color:#fff; background:var(--accent); padding:6px 9px;
  border-radius:2px; white-space:nowrap}
.wiek .w-kod{font-family:"JetBrains Mono",monospace; letter-spacing:.04em; opacity:.85}
.wiek.ghost{background:transparent; color:var(--accent); border:1px solid var(--accent); padding:4px 7px; font-size:9.5px}
.zasob{display:flex; gap:12px; margin-top:10px; padding:13px 18px; background:var(--zas-bg); border-left:4px solid var(--zas);
  font-size:13px; color:var(--text)}
.zasob b{color:var(--zas); font-size:10.5px; letter-spacing:.14em; text-transform:uppercase; display:block; margin-bottom:3px}

/* ---------- item ---------- */
.item{background:var(--card); border:1px solid var(--line); border-radius:2px; margin-top:14px; box-shadow:var(--shadow);
  break-inside:avoid; page-break-inside:avoid}
.item-h{display:flex; gap:14px; align-items:flex-start; padding:14px 18px; background:var(--band); border-bottom:1px solid var(--line-soft)}
.nr{font-family:Fraunces,Georgia,serif; font-size:22px; font-weight:600; color:var(--accent); line-height:1.1; min-width:30px}
.stmt{flex:1; font-size:14.5px; font-weight:500; color:var(--ink); line-height:1.4}
.stmt .src{display:flex; flex-wrap:wrap; align-items:center; gap:8px; font-size:10px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--muted); font-weight:700; margin-bottom:6px}
.codeblock{display:flex; flex-direction:column; gap:5px; align-items:stretch; align-self:center; flex:none}
.code-icf,.code-pp{font-family:"JetBrains Mono",monospace; font-size:11.5px; font-weight:700; padding:6px 10px;
  border-radius:2px; white-space:nowrap; display:flex; align-items:baseline; gap:8px; justify-content:space-between}
.code-icf{color:var(--icf); background:var(--icf-bg); border-left:3px solid var(--icf)}
.code-pp{color:var(--pp); background:var(--pp-bg); border-left:3px solid var(--pp)}
.code-icf em,.code-pp em{font-family:"DM Sans",Arial,sans-serif; font-style:normal; font-size:9px;
  letter-spacing:.14em; text-transform:uppercase; opacity:.75; font-weight:700}
.goal{display:grid; grid-template-columns:120px 1fr; gap:0; border-bottom:1px solid var(--line-soft)}
.goal:last-of-type{border-bottom:none}
.goal .side{padding:14px 16px; border-right:3px solid transparent}
.goal .side .lv{font:700 12.5px/1 "DM Sans",Arial,sans-serif; display:block}
.goal .side .hz{font-family:"JetBrains Mono",monospace; font-size:10.5px; color:var(--muted); margin-top:6px; display:block}
.goal .body{padding:14px 18px 14px 16px; font-size:14px}
.goal.p3 .side{background:var(--p3-bg); border-right-color:var(--p3)} .goal.p3 .lv{color:var(--p3)}
.goal.p2 .side{background:var(--p2-bg); border-right-color:var(--p2)} .goal.p2 .lv{color:var(--p2)}
.goal.p1 .side{background:var(--p1-bg); border-right-color:var(--p1)} .goal.p1 .lv{color:var(--p1)}
.miara{padding:11px 18px; background:var(--band); font-family:"JetBrains Mono",monospace; font-size:11px; color:var(--muted);
  border-top:1px solid var(--line-soft)}
.miara b{color:var(--ink-soft); letter-spacing:.1em; text-transform:uppercase; font-size:10px; font-family:"DM Sans",Arial,sans-serif}
.hidden{display:none !important}
.nores{padding:40px 0; text-align:center; color:var(--muted); font-size:14px}

footer{margin-top:64px; padding-top:26px; border-top:3px solid var(--ink); font-size:12.5px; color:var(--muted)}
footer .fgrid{display:grid; grid-template-columns:repeat(auto-fit,minmax(230px,1fr)); gap:24px}
footer b{display:block; font-size:10.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--ink-soft); margin-bottom:5px}
footer .sig{margin-top:24px; padding-top:16px; border-top:1px solid var(--line); display:flex; flex-wrap:wrap; gap:8px 20px; justify-content:space-between}

@media (max-width:720px){
  .wrap{padding:0 16px 60px}
  .goal{grid-template-columns:1fr}
  .goal .side{border-right:none; border-left:3px solid transparent; display:flex; gap:12px; align-items:baseline; padding:10px 16px}
  .goal.p3 .side{border-left-color:var(--p3)} .goal.p2 .side{border-left-color:var(--p2)} .goal.p1 .side{border-left-color:var(--p1)}
  .goal .side .hz{margin-top:0}
  .counts{margin-left:0}
  .item-h{flex-wrap:wrap}
  .codeblock{flex-direction:row; width:100%}
  .filters{margin-left:0; flex-wrap:wrap}
}
@media (prefers-reduced-motion:reduce){*{animation:none !important; transition:none !important}}

@page{size:A4; margin:14mm 12mm 16mm}
@media print{
  body{background:#fff; font-size:10.5pt}
  .toolbar,.areanav{display:none !important}
  .wrap{max-width:none; padding:0}
  .panel,.item{box-shadow:none}
  .area{break-before:auto}
  .area-h{-webkit-print-color-adjust:exact; print-color-adjust:exact}
  *{-webkit-print-color-adjust:exact; print-color-adjust:exact}
  .vers{display:block !important}
  .vers + .vers{break-before:page; page-break-before:always}
  .smartgrid{grid-template-columns:repeat(5,1fr)}
  .area-h,.zasob{break-after:avoid; page-break-after:avoid}
  .goal{break-inside:avoid; page-break-inside:avoid}
  .masthead{padding-top:0}
  h1{font-size:26pt}
}
"""

JS = """
const tabs=[...document.querySelectorAll('.tab')];
const vers=[...document.querySelectorAll('.vers')];
function pokazWersje(kod){
  tabs.forEach(t=>t.setAttribute('aria-selected', String(t.dataset.v===kod)));
  vers.forEach(v=>v.classList.toggle('hidden', v.dataset.v!==kod));
  filtruj();
}
tabs.forEach(t=>t.addEventListener('click',()=>pokazWersje(t.dataset.v)));

const lvlBtns=[...document.querySelectorAll('.chipbtn[data-lvl]')];
let aktywne=new Set(['p3','p2','p1']);
lvlBtns.forEach(b=>b.addEventListener('click',()=>{
  const l=b.dataset.lvl;
  if(aktywne.has(l) && aktywne.size>1) aktywne.delete(l); else aktywne.add(l);
  lvlBtns.forEach(x=>x.setAttribute('aria-pressed', String(aktywne.has(x.dataset.lvl))));
  document.querySelectorAll('.goal').forEach(g=>{
    g.classList.toggle('hidden', !aktywne.has(g.dataset.lvl));
  });
}));

const szukaj=document.getElementById('szukaj');
function filtruj(){
  const q=(szukaj.value||'').trim().toLowerCase();
  document.querySelectorAll('.vers:not(.hidden)').forEach(v=>{
    let widoczne=0;
    v.querySelectorAll('.area').forEach(a=>{
      let n=0;
      a.querySelectorAll('.item').forEach(it=>{
        const ok = !q || it.dataset.szukaj.includes(q);
        it.classList.toggle('hidden', !ok);
        if(ok) n++;
      });
      a.classList.toggle('hidden', n===0);
      widoczne+=n;
    });
    v.querySelector('.nores').classList.toggle('hidden', widoczne>0);
  });
}
szukaj.addEventListener('input',filtruj);
document.getElementById('drukuj').addEventListener('click',()=>window.print());
"""

def esc(s): return html.escape(str(s), quote=False)

def render_item(it, w):
    goals = [("p3", it["g3"]), ("p2", it["g2"]), ("p1", it["g1"])]
    rows = []
    for kod, tekst in goals:
        meta = next(p for p in POZIOMY if p[0] == kod)
        rows.append(f"""      <div class="goal {kod}" data-lvl="{kod}">
        <div class="side"><span class="lv">{esc(meta[2])}</span><span class="hz">ewaluacja: {esc(meta[5])}</span></div>
        <div class="body">{esc(tekst)}</div>
      </div>""")
    pp = it["pp"][3:] if it["pp"].startswith("PP ") else it["pp"]
    szukaj = " ".join([it["t"], it["g3"], it["g2"], it["g1"], it["icf"], it["pp"],
                       w["etykieta"], "wersja " + w["kod"]]).lower()
    return f"""    <article class="item" data-szukaj="{esc(szukaj)}">
      <div class="item-h">
        <div class="nr">{it['n']}</div>
        <div class="stmt">
          <span class="src">Twierdzenie KPOF nr {it['n']}<span class="wiek ghost">{esc(w['etykieta'])} · wersja {w['kod']}</span></span>
          {esc(it['t'])}
        </div>
        <div class="codeblock">
          <span class="code-icf"><em>ICF</em>{esc(it['icf'])}</span>
          <span class="code-pp"><em>Podstawa</em>{esc(pp)}</span>
        </div>
      </div>
{chr(10).join(rows)}
      <div class="miara"><b>Miara / narzędzie:</b> {esc(it['m'])}</div>
    </article>"""

def render_area(a, w):
    items = "\n".join(render_item(i, w) for i in a["items"])
    aid = f"{w['kod']}-{a['icf']}-{a['rom']}"
    return f"""  <section class="area" id="{aid}">
    <div class="area-h">
      <span class="rom">{a['rom']}</span>
      <h3>{esc(a['name'])}</h3>
      <span class="wiek">{esc(w['etykieta'])}<span class="w-kod">wersja {w['kod']}</span></span>
      <span class="code">{a['icf']} · Σ {a['pts']} pkt</span>
    </div>
    <div class="zasob"><div><b>Zasób 4,0–5,0 · dźwignia</b>{esc(a['zasob'])}</div></div>
{items}
  </section>"""

def render_wersja(mod, aktywna):
    w = mod.WERSJA
    n_tw = sum(len(a["items"]) for a in mod.AREAS)
    areas = "\n".join(render_area(a, w) for a in mod.AREAS)
    nav = "\n".join(
        f'      <a class="navlink" href="#{w["kod"]}-{a["icf"]}-{a["rom"]}">{a["rom"]} · {esc(a["name"].split(" (")[0])}</a>'
        for a in mod.AREAS)
    cls = "vers" if aktywna else "vers hidden"
    return f"""<div class="{cls}" data-v="{w['kod']}">
  <div class="vhead">
    <div>
      <div class="eyebrow">Wersja {w['kod']} · {esc(w['zakres'])}</div>
      <h2>Cele SMART dla dzieci {esc(w['etykieta'])}</h2>
      <p class="vdesc">{esc(w['opis'])}</p>
    </div>
    <div class="counts">
      <div><div class="num">{len(mod.AREAS)}</div><div class="cl">obszary ICF</div></div>
      <div><div class="num">{n_tw}</div><div class="cl">twierdzenia</div></div>
      <div><div class="num">{n_tw*3}</div><div class="cl">cele SMART</div></div>
    </div>
  </div>
  <nav class="areanav" aria-label="Obszary — wersja {w['kod']}">
{nav}
  </nav>
  <p class="nores hidden">Brak twierdzeń pasujących do wyszukiwania.</p>
{areas}
</div>"""

def build():
    dzis = datetime.date.today().strftime("%d.%m.%Y")
    razem_tw = sum(sum(len(a["items"]) for a in m.AREAS) for m in WERSJE)
    smart = [
        ("S", "Konkretny", "Zachowanie wprost z twierdzenia KPOF — obserwowalne w sali, nie „poprawa funkcjonowania”."),
        ("M", "Mierzalny", "Kryterium liczbowe: ile z ilu prób, przez ile minut, w ilu dniach tygodnia."),
        ("A", "Osiągalny", "Poziom wsparcia dobrany do wyniku obszaru — o jeden krok powyżej tego, co dziecko robi dziś."),
        ("R", "Istotny", "Każdy cel ma kod ICF (d1–d9) i punkt podstawy programowej — ta sama para co w WOPF i IPET."),
        ("T", "Określony w czasie", "Horyzont wynika z poziomu: III — 4 tygodnie, II — 8 tygodni, I — 12 tygodni."),
    ]
    smart_html = "\n".join(
        f'      <div><div class="letter">{L}</div><div class="lbl">{esc(n)}</div><p>{esc(o)}</p></div>'
        for L, n, o in smart)
    progi_rows = [
        ('zas', 'Zasób', '4,0 – 5,0', 'mocna strona',
         'Nie piszemy celu naprawczego. Zasób staje się dźwignią: dziecko dostaje rolę w grupie, '
         'która wykorzystuje tę umiejętność do pracy nad obszarem słabszym.', '—'),
    ]
    rows = [f"""      <tr class="r-{k}">
        <td><span class="pill {k}"><span class="dot d-{k}"></span>{esc(nazwa)}</span></td>
        <td class="mono">{esc(prog)}</td>
        <td>{esc(opis)}</td>
        <td>{esc(dzial)}</td>
        <td><span class="hz-cell">{esc(hor)}</span></td>
      </tr>""" for k, nazwa, prog, opis, dzial, hor in progi_rows]
    for kod, rz, nazwa, prog, opis, hor, dzial in POZIOMY[::-1]:
        rows.append(f"""      <tr class="r-{kod}">
        <td><span class="pill {kod}"><span class="dot d-{kod}"></span>{esc(nazwa)}</span></td>
        <td class="mono">{esc(prog)}</td>
        <td>{esc(opis)}</td>
        <td>{esc(dzial)}</td>
        <td><span class="hz-cell">{esc(hor)}</span></td>
      </tr>""")
    wersje_html = "\n".join(render_wersja(m, i == 0) for i, m in enumerate(WERSJE))
    tabs = "\n".join(
        f'      <button class="tab" role="tab" data-v="{m.WERSJA["kod"]}" '
        f'aria-selected="{"true" if i==0 else "false"}">{esc(m.WERSJA["etykieta"])}'
        f'<span class="kod">wersja {m.WERSJA["kod"]}</span></button>'
        for i, m in enumerate(WERSJE))

    return f"""<title>Bank Celów SMART KPOF</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,400&family=Fraunces:opsz,wght@9..144,500;9..144,600&family=JetBrains+Mono:wght@400;700&display=swap">
<style>{CSS}</style>
<div class="wrap">

<header class="masthead">
  <div class="brandline">
    <div class="mark">PCTP</div>
    <div>
      <div class="brandname">EduPlaner 2026</div>
      <div class="brandsub">Pomorskie Centrum Terapii Pedagogicznej · Koszalin</div>
    </div>
  </div>
  <div class="eyebrow">KPOF → cele SMART → IPET / PEWS</div>
  <h1>Bank celów SMART<br>do Przedszkolnej Oceny Funkcjonalnej</h1>
  <p class="lede">Do każdego z {razem_tw} twierdzeń kwestionariusza KPOF przypisano trzy gotowe cele — po jednym
  na każdy poziom wsparcia. Wynik obszaru z arkusza wskazuje wiersz, który wpisujemy do IPET lub PEWS;
  kod ICF i punkt podstawy programowej wędrują razem z celem, więc dokumentacja pozostaje spójna.</p>
  <div class="metastrip">
    <div><b>Narzędzie źródłowe</b>KPOF · wersje A / B / C · 9 obszarów ICF (d1–d9)</div>
    <div><b>Ramy</b>Podstawa programowa wychowania przedszkolnego · ICF (WHO)</div>
    <div><b>Autorka</b>pedagog specjalny mgr Mirosława Ewa Jurczyszyn</div>
    <div><b>Wygenerowano</b>{dzis}</div>
  </div>
</header>

<section class="panel">
  <div class="panel-h"><h2>Anatomia celu</h2><span>jak czytać każdy wiersz</span></div>
  <div class="smartgrid">
{smart_html}
  </div>
  <div class="legend">
    <span><i class="l-icf"></i>Kod <b style="color:var(--icf)">ICF</b> — czerwony (d1–d9, klasyfikacja WHO)</span>
    <span><i class="l-pp"></i>Punkt <b style="color:var(--pp)">podstawy programowej</b> — niebieski</span>
    <span><i class="l-wiek"></i>Wersja wiekowa arkusza — pomarańczowy znacznik przy każdym obszarze i twierdzeniu</span>
  </div>
</section>

<section class="panel">
  <div class="panel-h"><h2>Od wyniku KPOF do celu</h2><span>progi kryterialne arkusza</span></div>
  <div style="overflow-x:auto">
  <table class="progi">
    <thead><tr><th>Kwalifikacja</th><th>Średnia</th><th>Znaczenie</th><th>Co robimy w celu</th><th>Horyzont</th></tr></thead>
    <tbody>
{chr(10).join(rows)}
    </tbody>
  </table>
  </div>
  <div class="rule"><div><b>Reguła nadrzędna.</b> Każde pojedyncze twierdzenie ocenione na 1 lub 2 — niezależnie od
  średniej obszaru — podlega analizie jakościowej zespołu. Dla takiego twierdzenia bierzemy cel z wiersza Poziom III,
  nawet gdy cały obszar wypadł na Poziomie I. Ocen różnych osób (rodzic · nauczyciel · specjalista) nie uśredniamy
  mechanicznie — profile omawiamy obok siebie na spotkaniu zespołu.</div></div>
</section>

<div class="toolbar">
  <div class="tabs" role="tablist" aria-label="Wersja arkusza">
{tabs}
  </div>
  <div class="filters">
    <span class="lab">Poziomy</span>
    <button class="chipbtn" data-lvl="p3" aria-pressed="true">III</button>
    <button class="chipbtn" data-lvl="p2" aria-pressed="true">II</button>
    <button class="chipbtn" data-lvl="p1" aria-pressed="true">I</button>
    <label for="szukaj" class="lab">Szukaj</label>
    <input type="search" id="szukaj" placeholder="np. emocje, kolejka, chwyt">
    <button class="chipbtn" id="drukuj">Drukuj A4</button>
  </div>
</div>

{wersje_html}

<footer>
  <div class="fgrid">
    <div><b>Podstawa prawna</b>Rozporządzenie MEN z 9 sierpnia 2017 r. w sprawie warunków organizowania kształcenia,
      wychowania i opieki dla dzieci i młodzieży niepełnosprawnych · podstawa programowa wychowania przedszkolnego.</div>
    <div><b>Status dokumentu</b>Bank celów, nie gotowy IPET. Cel wybrany dla dziecka wymaga indywidualizacji: wpisania
      imienia, warunków sali i terminu ewaluacji ustalonego przez zespół.</div>
    <div><b>Ewaluacja</b>Ocena postępu na koniec horyzontu: cel osiągnięty · częściowo · niezrealizowany.
      Cel niezrealizowany dwukrotnie kierujemy do modułu pogłębiającego i WOPF.</div>
    <div><b>Powiązanie z dokumentacją</b>Kod ICF i punkt podstawy przy każdym celu są tożsame z kolumną ICF · PP
      arkusza KPOF — pozwalają wkleić cel do IPET lub PEWS bez ponownego opisywania.</div>
  </div>
  <div class="sig">
    <span>EduPlaner 2026 · PCTP · pedagog specjalny mgr Mirosława Ewa Jurczyszyn</span>
    <span class="mono">{razem_tw} twierdzeń · {razem_tw*3} celów SMART · 3 wersje wiekowe</span>
  </div>
</footer>

</div>
<script>{JS}</script>
"""

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "Bank_celow_SMART_KPOF.html")
    open(out, "w", encoding="utf-8").write(build())
    print("zapisano:", out, os.path.getsize(out), "B")
