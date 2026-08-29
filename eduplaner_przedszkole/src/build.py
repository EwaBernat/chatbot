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
  --ink:#2D1B69; --ink-2:#4A3A8C; --accent:#E8450A;
  --p3:#B8350D; --p3-bg:#FBEDE8; --p2:#B07408; --p2-bg:#FCF4E3; --p1:#0D7D5C; --p1-bg:#E7F4EE;
  --zas:#2B6E6E; --zas-bg:#E8F1F1;
  --icf:#C1121F; --icf-bg:#FBE9E9; --pp:#12408A; --pp-bg:#E8EFFA;
  --paper:#FFFFFF; --field:#F2F0F9; --row:#FAF9FD; --band:#F3F1FA;
  --line:#DCD7EC; --line-2:#EAE6F4; --text:#1F1A33; --muted:#6C6489;
  --strong:#2D1B69; --on-strong:#FFFFFF; --on-accent:#FFFFFF;
  --h-p3:#B8350D; --h-p3-t:#FFFFFF; --h-p2:#B07408; --h-p2-t:#FFFFFF; --h-p1:#0D7D5C; --h-p1-t:#FFFFFF;
  --h-icf:#C1121F; --h-icf-t:#FFFFFF; --h-pp:#12408A; --h-pp-t:#FFFFFF;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ink:#BFAFF2; --ink-2:#A395DC; --accent:#FF7A45;
    --p3:#FF9E80; --p3-bg:#33201A; --p2:#EDBC63; --p2-bg:#322814; --p1:#5FD3A8; --p1-bg:#152F27;
    --zas:#7FCFCF; --zas-bg:#152C2C;
    --icf:#FF8F8F; --icf-bg:#341C1C; --pp:#8FBEFF; --pp-bg:#12253C;
    --paper:#16131F; --field:#221C36; --row:#1B1729; --band:#221C36;
    --line:#332B4D; --line-2:#2A2340; --text:#ECE8F7; --muted:#A79FC2;
    --strong:#2A2340; --on-strong:#ECE8F7; --on-accent:#2A1207;
    --h-p3:#3A211A; --h-p3-t:#FF9E80; --h-p2:#352A15; --h-p2-t:#EDBC63; --h-p1:#16332A; --h-p1-t:#5FD3A8;
    --h-icf:#3A1D1D; --h-icf-t:#FF8F8F; --h-pp:#132840; --h-pp-t:#8FBEFF;
  }
}
:root[data-theme="dark"]{
  --ink:#BFAFF2; --ink-2:#A395DC; --accent:#FF7A45;
  --p3:#FF9E80; --p3-bg:#33201A; --p2:#EDBC63; --p2-bg:#322814; --p1:#5FD3A8; --p1-bg:#152F27;
  --zas:#7FCFCF; --zas-bg:#152C2C;
  --icf:#FF8F8F; --icf-bg:#341C1C; --pp:#8FBEFF; --pp-bg:#12253C;
  --paper:#16131F; --field:#221C36; --row:#1B1729; --band:#221C36;
  --line:#332B4D; --line-2:#2A2340; --text:#ECE8F7; --muted:#A79FC2;
  --strong:#2A2340; --on-strong:#ECE8F7; --on-accent:#2A1207;
  --h-p3:#3A211A; --h-p3-t:#FF9E80; --h-p2:#352A15; --h-p2-t:#EDBC63; --h-p1:#16332A; --h-p1-t:#5FD3A8;
  --h-icf:#3A1D1D; --h-icf-t:#FF8F8F; --h-pp:#132840; --h-pp-t:#8FBEFF;
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
.wordmark{font-family:Fraunces,Georgia,serif; font-size:24px; font-weight:600; color:var(--ink); line-height:1}
.wordsub{font-size:9.5px; letter-spacing:.2em; text-transform:uppercase; color:var(--muted); font-weight:700; margin-top:6px; line-height:1.5}
.dochead .right{margin-left:auto; text-align:right}
.badge{display:inline-block; background:var(--accent); color:var(--on-accent); padding:7px 15px; border-radius:999px;
  font:700 10.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase}
.badge-sub{font-size:9.5px; letter-spacing:.18em; text-transform:uppercase; color:var(--muted); font-weight:700; margin-top:7px}
.twotone{height:7px; display:flex; margin-bottom:16px}
.twotone i{display:block; height:100%}
.twotone i:first-child{width:56%; background:var(--ink)}
.twotone i:last-child{width:44%; background:var(--accent)}

/* ---------- pola do wypełnienia ---------- */
.fields{display:grid; grid-template-columns:1.45fr 1.2fr 1fr .9fr; gap:12px; margin-bottom:26px}
.field{background:var(--field); border:1px solid var(--line-2); border-radius:5px; padding:11px 15px; display:flex;
  align-items:baseline; gap:10px; min-height:44px}
.field b{font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.16em; text-transform:uppercase; color:var(--ink-2); white-space:nowrap}
.field .dots{flex:1; border-bottom:1px dotted var(--ink-2); opacity:.55; height:12px}
.field .val{font-weight:600; color:var(--ink)}

/* ---------- tytuł druku ---------- */
.titleblock{text-align:center; margin-bottom:30px}
.pillrow{display:flex; justify-content:center; margin-bottom:16px}
.pill-title{background:var(--accent); color:var(--on-accent); padding:8px 20px; border-radius:999px;
  font:700 10.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.13em; text-transform:uppercase}
.titleblock h1{font:700 clamp(26px,3.6vw,38px)/1.1 "DM Sans",Arial,sans-serif; letter-spacing:.02em;
  text-transform:uppercase; color:var(--ink); margin:0}
.titleblock .sub{color:var(--accent); font-weight:700; font-size:15px; margin-top:10px}
.dashrow{display:flex; align-items:center; gap:16px; justify-content:center; margin-top:16px; color:var(--ink-2)}
.dashrow i{height:1px; background:var(--line); width:70px; display:block}
.dashrow span{font:700 10.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.22em; text-transform:uppercase}

/* ---------- sekcja ---------- */
.sec{margin-top:34px; scroll-margin-top:70px}
.sec-h{display:flex; align-items:center; gap:12px; margin-bottom:12px}
.sq{background:var(--accent); color:var(--on-accent); width:26px; height:26px; border-radius:4px; display:grid; place-items:center;
  font:700 11px/1 "DM Sans",Arial,sans-serif; flex:none}
.sq.sq-ink{background:var(--strong); color:var(--on-strong)}
.sec-h h2{font:700 15.5px/1.2 "DM Sans",Arial,sans-serif; letter-spacing:.09em; text-transform:uppercase; color:var(--ink); margin:0}
.sec-h .meta{font-family:"JetBrains Mono",monospace; font-size:10.5px; color:var(--muted); white-space:nowrap}
.sec-h .line{flex:1; height:1px; background:var(--line)}

/* ---------- tabela ---------- */
.tablewrap{overflow-x:auto; border:1px solid var(--line); border-radius:6px}
table{width:100%; border-collapse:collapse; min-width:1080px}
thead{display:table-header-group}
th{background:var(--strong); color:var(--on-strong); text-align:left; padding:10px 12px; vertical-align:middle;
  font:700 9.5px/1.25 "DM Sans",Arial,sans-serif; letter-spacing:.13em; text-transform:uppercase;
  border-right:1px solid rgba(255,255,255,.14)}
th:last-child{border-right:none}
th .hz{display:block; font-family:"JetBrains Mono",monospace; letter-spacing:.02em; font-size:9px; opacity:.72; margin-top:3px}
td{padding:10px 12px; border-bottom:1px solid var(--line-2); border-right:1px solid var(--line-2); vertical-align:top; font-size:12.5px; line-height:1.45}
td:last-child{border-right:none}
tbody tr:last-child td{border-bottom:none}
tbody tr:nth-child(even) td{background:var(--row)}
tbody tr:hover td{background:var(--band)}

.c-lp{width:38px} .c-tw{width:23%} .c-code{width:82px} .c-goal{width:18.5%}
td.lp{text-align:center; font-weight:700; color:var(--accent); background:var(--field) !important; font-size:14px; padding-top:11px}
td.tw{font-weight:500; color:var(--ink)}
td.tw .miara{display:block; margin-top:7px; font-family:"JetBrains Mono",monospace; font-size:9.5px; color:var(--muted); line-height:1.4}
td.tw .miara b{color:var(--ink-2); font-family:"DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase; font-size:9px}
td.icf{font-family:"JetBrains Mono",monospace; font-weight:700; font-size:11px; color:var(--icf); background:var(--icf-bg) !important; white-space:nowrap}
td.pp{font-family:"JetBrains Mono",monospace; font-weight:700; font-size:11px; color:var(--pp); background:var(--pp-bg) !important; white-space:nowrap}
td.g{font-size:12px}
th.h-p3{background:var(--h-p3); color:var(--h-p3-t)} th.h-p2{background:var(--h-p2); color:var(--h-p2-t)}
th.h-p1{background:var(--h-p1); color:var(--h-p1-t)}
th.h-icf{background:var(--h-icf); color:var(--h-icf-t)} th.h-pp{background:var(--h-pp); color:var(--h-pp-t)}
tbody tr td.p3{background:var(--p3-bg) !important} tbody tr td.p2{background:var(--p2-bg) !important}
tbody tr td.p1{background:var(--p1-bg) !important}

/* ---------- callout / zasób ---------- */
.callout{margin-top:12px; background:var(--band); border-left:4px solid var(--ink); padding:13px 17px; font-size:12.5px; border-radius:0 4px 4px 0}
.callout.zas{background:var(--zas-bg); border-left-color:var(--zas)}
.callout .cap{font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase; color:var(--zas); display:block; margin-bottom:5px}
.callout.rule{background:var(--p2-bg); border-left-color:var(--accent)}
.callout.rule .cap{color:var(--accent)}

/* ---------- legenda ---------- */
.legendbox{background:var(--field); border:1px solid var(--line-2); border-radius:6px; padding:16px 20px; font-size:12.5px; line-height:1.65}
.legendbox .k{font-weight:700; color:var(--ink)}
.legendbox .k-icf{color:var(--icf); font-family:"JetBrains Mono",monospace; font-weight:700}
.legendbox .k-pp{color:var(--pp); font-family:"JetBrains Mono",monospace; font-weight:700}

/* ---------- pasek narzędzi (tylko ekran) ---------- */
.toolbar{position:sticky; top:0; z-index:20; background:var(--paper); border-bottom:1px solid var(--line);
  padding:11px 0; margin-top:30px; display:flex; flex-wrap:wrap; gap:9px 16px; align-items:center}
.tab{border:1px solid var(--line); background:var(--paper); color:var(--ink); padding:8px 14px; border-radius:4px;
  font:700 12px/1 "DM Sans",Arial,sans-serif; cursor:pointer; display:flex; gap:7px; align-items:center}
.tab .kod{font-family:"JetBrains Mono",monospace; font-size:10px; opacity:.65}
.tab[aria-selected="true"]{background:var(--strong); color:var(--on-strong); border-color:var(--strong)}
.tools{margin-left:auto; display:flex; gap:7px; align-items:center; flex-wrap:wrap}
.tools .lab{font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase; color:var(--muted)}
.chipbtn{border:1px solid var(--line); background:var(--paper); color:var(--muted); padding:7px 10px; border-radius:4px;
  font:700 11px/1 "DM Sans",Arial,sans-serif; cursor:pointer; letter-spacing:.05em}
.chipbtn[aria-pressed="true"].b-p3{background:var(--h-p3); border-color:var(--h-p3); color:var(--h-p3-t)}
.chipbtn[aria-pressed="true"].b-p2{background:var(--h-p2); border-color:var(--h-p2); color:var(--h-p2-t)}
.chipbtn[aria-pressed="true"].b-p1{background:var(--h-p1); border-color:var(--h-p1); color:var(--h-p1-t)}
#drukuj{background:var(--strong); border-color:var(--strong); color:var(--on-strong)}
input[type="search"]{border:1px solid var(--line); background:var(--paper); color:var(--text); padding:8px 10px;
  border-radius:4px; font:400 12.5px/1.2 "DM Sans",Arial,sans-serif; width:180px}
input[type="search"]:focus,.tab:focus-visible,.chipbtn:focus-visible,.navlink:focus-visible{outline:2px solid var(--accent); outline-offset:2px}

/* ---------- nagłówek wersji ---------- */
.vband{display:flex; flex-wrap:wrap; align-items:center; gap:14px; background:var(--strong); color:var(--on-strong);
  padding:14px 20px; border-radius:6px; margin-top:30px}
.vband .vlet{background:var(--accent); color:var(--on-accent); width:34px; height:34px; border-radius:5px; display:grid; place-items:center;
  font:700 15px/1 "DM Sans",Arial,sans-serif}
.vband h2{font:700 16px/1.2 "DM Sans",Arial,sans-serif; letter-spacing:.09em; text-transform:uppercase; margin:0}
.vband .vmeta{margin-left:auto; display:flex; gap:22px; font-family:"JetBrains Mono",monospace; font-size:11px}
.vband .vmeta b{display:block; font-family:"DM Sans",Arial,sans-serif; font-size:9px; letter-spacing:.14em;
  text-transform:uppercase; opacity:.7; font-weight:700; margin-bottom:2px}
.vdesc{font-size:12.5px; color:var(--muted); margin:10px 0 0; max-width:100ch}
.areanav{display:flex; flex-wrap:wrap; gap:5px; margin-top:12px}
.navlink{text-decoration:none; border:1px solid var(--line); color:var(--ink-2); padding:5px 9px; border-radius:4px;
  font:700 10.5px/1 "DM Sans",Arial,sans-serif}
.navlink:hover{border-color:var(--accent); color:var(--accent)}

/* ---------- stopka ---------- */
.docfoot{margin-top:46px; padding-top:14px; border-top:1px solid var(--line); display:flex; flex-wrap:wrap;
  gap:8px 20px; justify-content:space-between; font-size:11px; color:var(--muted)}
.hidden{display:none !important}
.nores{padding:30px 0; text-align:center; color:var(--muted)}
.printhead,.printfoot{display:none}
tr.tbanner{display:none}
tr.tbanner th{background:var(--strong); color:var(--on-strong); font:700 6.4pt/1.3 "DM Sans",Arial,sans-serif;
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
  tr.tbanner{display:table-row}
  table{min-width:0; font-size:8.4pt}
  th{padding:5pt 6pt; font-size:6.6pt; letter-spacing:.1em}
  td{padding:5pt 6pt; font-size:8.2pt; line-height:1.35}
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
          <td class="icf">{esc(it['icf'])}</td>
          <td class="pp">{esc(pp)}</td>
          <td class="g p3 col-p3">{esc(it['g3'])}</td>
          <td class="g p2 col-p2">{esc(it['g2'])}</td>
          <td class="g p1 col-p1">{esc(it['g1'])}</td>
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
          <th class="c-code h-icf">ICF</th>
          <th class="c-code h-pp">Podstawa</th>
          <th class="c-goal h-p3 col-p3">Poziom III<span class="hz">ewaluacja 4 tyg.</span></th>
          <th class="c-goal h-p2 col-p2">Poziom II<span class="hz">ewaluacja 8 tyg.</span></th>
          <th class="c-goal h-p1 col-p1">Poziom I<span class="hz">ewaluacja 12 tyg.</span></th>
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
          <td class="mono" style="white-space:nowrap; font-weight:700; color:var(--ink-2)">{esc(hor)}</td>
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=Fraunces:opsz,wght@9..144,600&family=JetBrains+Mono:wght@400;700&display=swap">
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
