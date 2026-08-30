# -*- coding: utf-8 -*-
"""Generator druku KC-1: Bank celów SMART do KPOF — układ tabelaryczny
w stylu Kącika Dyrektora (EduPlaner 2026 · PCTP)."""
import html, os, sys, datetime, base64
_LOGO_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "logo_pctp.jpg")
LOGO_URI = "data:image/jpeg;base64," + base64.b64encode(open(_LOGO_PATH, "rb").read()).decode()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dane_34, dane_5, dane_6, dane_uzup
from konspekty_34_d7 import KONSPEKTY
from konspekty_34_d1 import KONSPEKTY_D1
from konspekty_34_d2 import KONSPEKTY_D2
from konspekty_34_d3 import KONSPEKTY_D3
from konspekty_34_d5 import KONSPEKTY_D5
from konspekty_34_d9 import KONSPEKTY_D9
from konspekty_5_d1 import KONSPEKTY_5_D1
from konspekty_5_d2 import KONSPEKTY_5_D2
from konspekty_5_d3 import KONSPEKTY_5_D3
from konspekty_5_d4 import KONSPEKTY_5_D4
from konspekty_5_d5 import KONSPEKTY_5_D5
from konspekty_5_d6 import KONSPEKTY_5_D6
from konspekty_5_d7 import KONSPEKTY_5_D7
from konspekty_5_d8 import KONSPEKTY_5_D8
from konspekty_5_d9 import KONSPEKTY_5_D9
from konspekty_6_d1 import KONSPEKTY_6_D1
from konspekty_6_d2 import KONSPEKTY_6_D2
from konspekty_6_d3 import KONSPEKTY_6_D3
from konspekty_6_d4 import KONSPEKTY_6_D4
from konspekty_6_d5 import KONSPEKTY_6_D5
from konspekty_6_d6 import KONSPEKTY_6_D6
from konspekty_6_d7 import KONSPEKTY_6_D7
from konspekty_6_d8 import KONSPEKTY_6_D8
from konspekty_6_d9 import KONSPEKTY_6_D9
from zalacznik_c1 import zalaczniki_c1
import pomoce_a          # noqa: F401 — rejestruje zestaw pomocy 3–4 lata
import pomoce_b          # noqa: F401 — rejestruje zestaw pomocy 5 lat
import pomoce_a, pomoce_b, pomoce_c, pomoce_u  # noqa: F401 — rejestrują zestawy w pomoce_karta
from pomoce_karta import pomoce_dla, wskaz_pomoc, style_pomocy, audio_pomocy
from karty_druk import karty_dla, ma_karty, style_kart
from konspekty_34_d4 import KONSPEKTY_D4
from konspekty_34_d6 import KONSPEKTY_D6
from konspekty_34_d8 import KONSPEKTY_D8
from konspekty_u_o123 import KONSPEKTY_U_O123
from konspekty_u_o45 import KONSPEKTY_U_O45
from konspekty_u_o6789 import KONSPEKTY_U_O6789
KONSPEKTY = {**KONSPEKTY_D1, **KONSPEKTY_D2, **KONSPEKTY_D3, **KONSPEKTY_D4, **KONSPEKTY_D5,
             **KONSPEKTY_D6, **KONSPEKTY_D8, **KONSPEKTY_D9,
             **KONSPEKTY_5_D1, **KONSPEKTY_5_D2, **KONSPEKTY_5_D3, **KONSPEKTY_5_D4,
             **KONSPEKTY_5_D5, **KONSPEKTY_5_D6, **KONSPEKTY_5_D7, **KONSPEKTY_5_D8,
             **KONSPEKTY_5_D9,
             **KONSPEKTY_6_D1, **KONSPEKTY_6_D2, **KONSPEKTY_6_D3, **KONSPEKTY_6_D4,
             **KONSPEKTY_6_D5, **KONSPEKTY_6_D6, **KONSPEKTY_6_D7, **KONSPEKTY_6_D8,
             **KONSPEKTY_6_D9,
             **KONSPEKTY_U_O123, **KONSPEKTY_U_O45, **KONSPEKTY_U_O6789,
             **KONSPEKTY}

WERSJE = [dane_34, dane_5, dane_6, dane_uzup]

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
  --p3:#C42430; --p3-bg:#FDF4F4; --p2:#C29B00; --p2-bg:#FEFAE4; --p1:#0F7B5A; --p1-bg:#F5FAF8;
  --zas:#2B6E6E; --zas-bg:#EAF3F3;
  --icf:#C1121F; --icf-bg:#FFFFFF; --pp:#4F3AA8; --pp-bg:#FFFFFF;
  --p3-br:#F0C3C6; --p2-br:#EEDF9A; --p1-br:#BEDFD1; --icf-br:#EEC4C4; --pp-br:#CFC6EE;
  --paper:#FFFFFF; --field:#EFEAF9; --soft:#F6F3FC; --row:#FEFDFF; --row-alt:#F4F0FD;
  --line:#E3DCF5; --line-2:#EDE8F8; --rowline:#D3CAEB; --text:#2F2A3E; --muted:#8A8498;
  --strong:#2D1B69; --on-strong:#FFFFFF;
  --h-p3:#4F3AA8; --h-p3-t:#FFFFFF; --h-p2:#4F3AA8; --h-p2-t:#FFFFFF; --h-p1:#4F3AA8; --h-p1-t:#FFFFFF;
  --h-icf:#4F3AA8; --h-icf-t:#FFFFFF; --h-pp:#4F3AA8; --h-pp-t:#FFFFFF;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ink:#C6B8F5; --indigo:#7C68D8; --violet:#A794E8; --accent:#FF7A45; --on-accent:#2A1207;
    --p3:#FF9297; --p3-bg:#331D1F; --p2:#EDD35E; --p2-bg:#302B13; --p1:#63D3AA; --p1-bg:#16302A;
    --zas:#7FCFCF; --zas-bg:#152C2C;
    --icf:#FF8F8F; --icf-bg:#301C1C; --pp:#A794E8; --pp-bg:#241D42;
    --p3-br:#4E2A2D; --p2-br:#4C4318; --p1-br:#22463A; --icf-br:#472A2A; --pp-br:#3A3167;
    --paper:#15121E; --field:#221C36; --soft:#1E1930; --row:#1A1628; --row-alt:#221C36;
    --line:#332B4D; --line-2:#2A2340; --rowline:#453B68; --text:#ECE8F7; --muted:#A79FC2;
    --strong:#2E2650; --on-strong:#EDE9FA;
    --h-p3:#2E2650; --h-p3-t:#EDE9FA; --h-p2:#2E2650; --h-p2-t:#EDE9FA; --h-p1:#2E2650; --h-p1-t:#EDE9FA;
    --h-icf:#2E2650; --h-icf-t:#EDE9FA; --h-pp:#2E2650; --h-pp-t:#EDE9FA;
  }
}
:root[data-theme="dark"]{
  --ink:#C6B8F5; --indigo:#7C68D8; --violet:#A794E8; --accent:#FF7A45; --on-accent:#2A1207;
  --p3:#FF9297; --p3-bg:#331D1F; --p2:#EDD35E; --p2-bg:#302B13; --p1:#63D3AA; --p1-bg:#16302A;
  --zas:#7FCFCF; --zas-bg:#152C2C;
  --icf:#FF8F8F; --icf-bg:#301C1C; --pp:#A794E8; --pp-bg:#241D42;
    --p3-br:#4E2A2D; --p2-br:#4C4318; --p1-br:#22463A; --icf-br:#472A2A; --pp-br:#3A3167;
  --paper:#15121E; --field:#221C36; --soft:#1E1930; --row:#1A1628; --row-alt:#221C36;
  --line:#332B4D; --line-2:#2A2340; --rowline:#453B68; --text:#ECE8F7; --muted:#A79FC2;
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
.mark{width:46px; height:46px; border-radius:50%; flex:none; background:center/cover no-repeat; background-image:var(--logo)}
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
td{padding:9px 10px; border-bottom:1px solid var(--rowline); border-right:1px solid var(--line-2);
  vertical-align:top; font-size:12.5px; line-height:1.45}
td:last-child{border-right:none}

td.g{border-right:1px solid var(--line)}
td.g .cel{display:block}
td.icf .kod,td.pp .kod{display:inline-block}
td.tw .miara{border-top:1px solid var(--line-2); padding-top:6px}
tbody tr:nth-child(even) td{background:var(--paper)}
tbody tr:hover td.tw{background:var(--soft)}

.c-lp{width:38px} .c-tw{width:24%} .c-code{width:52px} .c-goal{width:19.5%}
td.lp{text-align:center; font-weight:700; color:var(--ink); background:var(--paper) !important; font-size:14px; padding-top:11px}
td.tw{font-weight:500; color:var(--ink)}
td.tw .miara{display:block; margin-top:8px; font-family:"JetBrains Mono",monospace; font-size:9.5px; color:var(--muted); line-height:1.4}
td.tw .miara b{color:var(--violet); font-family:"DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase; font-size:9px}
td.icf{font-family:"JetBrains Mono",monospace; font-weight:700; font-size:10px; color:var(--icf); background:var(--paper) !important; word-break:break-all; line-height:1.35}
td.pp{font-family:"JetBrains Mono",monospace; font-weight:700; font-size:10px; color:var(--pp); background:var(--paper) !important; word-break:break-word; line-height:1.35}
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

/* ---------- spis konspektów ---------- */
.kspis{margin:18px 0 4px; border:1px solid var(--line); border-radius:14px; background:#FFF; overflow:hidden}
.kspis{border-color:var(--accent)}
.kspis > summary{cursor:pointer; list-style:none; padding:14px 18px; display:flex; align-items:center; gap:10px;
  font:700 13px/1 "DM Sans",Arial,sans-serif; color:var(--on-accent); background:var(--accent);
  letter-spacing:.01em}
.kspis > summary:hover{filter:brightness(1.07)}
.kspis > summary .ile{color:var(--on-accent) !important; opacity:.86}
.kspis > summary .zwin{display:none}
.kspis[open] > summary .zwin{display:inline}
.kspis[open] > summary .rozwin{display:none}
.kspis > summary::-webkit-details-marker{display:none}
.kspis > summary::before{content:"▸"; color:var(--on-accent); font-size:14px}
.kspis[open] > summary::before{content:"▾"}
.kspis > summary .ile{margin-left:auto; font-weight:400; color:var(--muted); font-size:11.5px}
.kspis-tresc{padding:6px 18px 16px}
/* Obszary w kolorze akcentu, nie w fiolecie tekstu: w spisie na 44 pozycje
   nagłówek musi być pierwszą rzeczą, którą widać, inaczej pozycje zlewają się
   w jedną listę. */
.kspis-obszar{display:flex; align-items:center; gap:10px; margin:16px 0 8px;
  font:700 10.5px/1 "DM Sans",Arial,sans-serif;
  letter-spacing:.14em; text-transform:uppercase; color:var(--accent)}
.kspis-obszar::after{content:""; flex:1; height:2px; border-radius:2px;
  background:color-mix(in srgb, var(--accent) 28%, transparent)}
.kspis-obszar:first-child{margin-top:4px}
/* Spis w równej siatce, nie w rzędzie pigułek: pigułki miały szerokość swojego
   tytułu, więc kolumny nie trzymały się pionu i 44 pozycje wyglądały jak sypnięte
   na ekran. W siatce numer stoi zawsze w tym samym miejscu, a wzrok schodzi
   kolumną — po to jest spis. */
.kspis-lista{display:grid; grid-template-columns:repeat(auto-fill,minmax(232px,1fr)); gap:7px}
.kbtn{display:flex; align-items:center; gap:9px; min-height:42px;
  border:1px solid var(--line); background:#FFF; border-radius:10px; padding:8px 11px; cursor:pointer;
  font:500 11.5px/1.3 "DM Sans",Arial,sans-serif; color:var(--ink); text-align:left;
  transition:border-color .12s, box-shadow .12s}
.kbtn:hover{border-color:var(--accent); color:var(--accent); box-shadow:0 1px 6px rgba(232,69,10,.10)}
.kbtn b{flex:0 0 42px; font:700 10.5px/1 "JetBrains Mono",ui-monospace,"Courier New",monospace;
  color:var(--violet); letter-spacing:.02em}
.kbtn:hover b{color:var(--accent)}
.kbtn .tyt{flex:1 1 auto}
.kbtn .pom{flex:0 0 auto; margin-left:4px; color:var(--accent); font-weight:700; font-size:10px}

/* ---------- stopka ---------- */
.docfoot{margin-top:46px; padding-top:14px; border-top:1px solid var(--line); display:flex; flex-wrap:wrap;
  gap:8px 20px; justify-content:space-between; font-size:11px; color:var(--muted)}
/* ---------- załączniki: pomoce dydaktyczne ---------- */
.zal{background:#FFF; border:1px solid var(--line); border-radius:14px; padding:22px 24px 18px; margin-top:18px;
  break-inside:avoid; page-break-inside:avoid; page:arkusz}
.zal + .zal{break-before:page; page-break-before:always}
.zal-head{display:flex; align-items:center; gap:12px; border-bottom:2px solid var(--ink); padding-bottom:10px}
.zal-w{font:700 17px/1 "DM Sans",Arial,sans-serif; color:var(--ink)}
.zal-s{font-size:8.5px; letter-spacing:.16em; text-transform:uppercase; color:var(--violet); font-weight:700; margin-top:4px}
.zal-pill{margin-left:auto; border-radius:999px; padding:7px 14px; color:#fff;
  font:700 11px/1 "DM Sans",Arial,sans-serif; white-space:nowrap}
.zal-pill.p3{background:var(--p3)} .zal-pill.p2{background:var(--p2)} .zal-pill.p1{background:var(--p1)}
.zal-tytul{text-align:center; margin:16px 0 14px}
.zal-kp{display:inline-block; background:var(--accent); color:var(--on-accent); border-radius:999px; padding:5px 14px;
  font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.13em; text-transform:uppercase}
.zal-tytul h3{font:700 27px/1.1 "DM Sans",Arial,sans-serif; color:var(--ink); margin:9px 0 0}
.zal-tytul p{max-width:62ch; margin:8px auto 0; font-size:12px; color:var(--muted); line-height:1.5}
.zal-siatka{display:grid; gap:14px}
.zal-siatka.k2{grid-template-columns:1fr 1fr}
.zal-siatka.k3{grid-template-columns:1fr 1fr 1fr}
.kafel{position:relative; margin:0; background:#FFF; border:2px dashed #E4B9D2; border-radius:16px; padding:10px 10px 8px; text-align:center}
/* Bez skrótu `background` — zresetowałby background-image ustawiany przez klasy .sc1–.sc5. */
.kafel .obraz{display:block; width:100%; aspect-ratio:5/4; border-radius:11px;
  background-color:#FFF; background-position:center; background-size:contain; background-repeat:no-repeat;
  print-color-adjust:exact; -webkit-print-color-adjust:exact}
.kafel.kwadrat .obraz{aspect-ratio:1/1; background-color:#FFF}
.kafel figcaption{margin-top:8px; font:600 12px/1.35 "DM Sans",Arial,sans-serif; color:var(--ink)}
/* Odsłuch narracji — tylko na ekranie; w druku karta ma być czysta do wycięcia. */
.au-pasek{display:flex; flex-wrap:wrap; align-items:center; gap:10px; margin:0 0 14px;
  background:var(--soft); border:1px solid var(--line); border-radius:12px; padding:9px 12px}
.au-all,.au-stop,.au-btn{font:700 12px/1 "DM Sans",Arial,sans-serif; border-radius:999px;
  cursor:pointer; border:1px solid transparent; transition:background .15s,color .15s}
.au-all{background:var(--accent); color:var(--on-accent); padding:9px 16px}
.au-all:hover{filter:brightness(1.07)}
.au-stop{background:transparent; color:var(--muted); border-color:var(--line); padding:9px 14px}
.au-stop:hover{color:var(--ink); border-color:var(--rowline)}
.au-info{margin-left:auto; font-size:10.5px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--violet); font-weight:700}
.au-btn{display:inline-flex; align-items:center; gap:5px; margin-top:7px; padding:6px 12px;
  background:#FFF; color:var(--indigo); border-color:var(--line)}
.au-btn:hover{background:var(--field)}
.au-btn.gra,.au-all.gra{background:var(--indigo); color:#FFF; border-color:var(--indigo)}
/* Karta pomocy dydaktycznej — zdjęcie poglądowe i dwie kolumny opisu. */
.pf{display:block; width:100%; aspect-ratio:16/9; border-radius:14px; margin:4px 0 16px;
  background-color:var(--soft); background-position:center; background-size:cover;
  background-repeat:no-repeat; border:1px solid var(--line);
  print-color-adjust:exact; -webkit-print-color-adjust:exact}
.pomoc-dwie{display:grid; grid-template-columns:1fr 1fr; gap:14px 22px; margin-bottom:14px}
.pomoc-h{font:700 11px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase;
  color:var(--violet); margin:0 0 8px}
.pomoc-lista li{font-size:12.5px; line-height:1.5}
.pomoc-kroki{list-style:none; margin:0; padding:0; display:grid; gap:8px}
.pomoc-kroki li{display:grid; grid-template-columns:22px 1fr; gap:9px; align-items:start;
  font-size:12.5px; line-height:1.5}
.pk-n{width:20px; height:20px; border-radius:50%; background:var(--accent); color:#fff;
  display:grid; place-items:center; font:700 11px/1 "DM Sans",Arial,sans-serif; margin-top:1px}
.pomoc-glos{display:flex; align-items:center; gap:14px; background:var(--soft);
  border:1px solid var(--line); border-radius:12px; padding:11px 14px; margin-bottom:12px}
.pomoc-glos .au-btn{margin-top:0; flex:none}
.pomoc-tekst{margin:0; font-size:12.5px; line-height:1.5; color:var(--ink); font-style:italic}
.pomoc-wsk{margin-bottom:12px}
@media screen and (max-width:860px){ .pomoc-dwie{grid-template-columns:1fr} }
.kafel.gra{border-color:var(--accent)}
.kafel .numer{position:absolute; top:-11px; left:-11px; width:30px; height:30px; border-radius:50%;
  background:var(--accent); color:#fff; display:grid; place-items:center;
  font:700 14px/1 "DM Sans",Arial,sans-serif; box-shadow:0 2px 6px rgba(20,12,50,.2)}
.zal-stopka{display:flex; flex-wrap:wrap; gap:8px 18px; justify-content:space-between; align-items:center;
  margin-top:16px; padding-top:10px; border-top:1px solid var(--line); font-size:11px; color:var(--muted)}
.zal-stopka b{color:var(--ink)}
.zal-link{display:inline-flex; align-items:center; gap:8px; border:1px solid var(--accent); color:var(--accent);
  background:#FFF7F2; border-radius:8px; padding:8px 12px; font:700 11.5px/1 "DM Sans",Arial,sans-serif;
  cursor:pointer; margin-top:10px}
.zal-link:hover{background:var(--accent); color:var(--on-accent)}
.zal-akcje{display:flex; flex-wrap:wrap; gap:10px}
.zal-pokaz{border-color:var(--indigo); color:var(--indigo)}
.zal-pokaz:hover{background:var(--indigo); color:#FFF}
.zal-pokaz[aria-expanded="true"]{background:var(--indigo); color:#FFF}
.opts{display:flex; flex-wrap:wrap; gap:6px}
.opt{display:inline-flex; align-items:center; gap:6px; border:1px solid var(--line); border-radius:6px;
  padding:4px 8px; font-size:11.5px; background:var(--paper); white-space:nowrap}
.opt i{width:11px; height:11px; border:1.5px solid var(--violet); border-radius:3px; display:block; flex:none}
td.g.haskon{cursor:pointer; position:relative}
td.g.haskon .cel::after{content:"▸ konspekt"; display:block; margin-top:7px; font:700 9.5px/1 "DM Sans",Arial,sans-serif;
  letter-spacing:.12em; text-transform:uppercase; color:var(--accent)}
td.g.haskon:hover{background:var(--soft) !important}
td.g.haskon:focus-visible{outline:2px solid var(--accent); outline-offset:-2px}

/* ---------- modal konspektu (wg wzoru Termometr uwagi) ---------- */
.kmodal{position:fixed; inset:0; z-index:50; display:none; background:rgba(31,26,62,.55); overflow:auto; padding:26px 14px}
.kmodal.open{display:block}
.kcard{max-width:900px; margin:0 auto; background:var(--paper); border-radius:12px; box-shadow:0 22px 70px rgba(20,12,50,.45); padding:26px 30px 30px}
.khead{display:flex; align-items:center; gap:12px; border-bottom:2px solid var(--ink); padding-bottom:12px; position:relative}
.khead .mark{width:40px; height:40px}
.khead .kw{font:700 18px/1 "DM Sans",Arial,sans-serif; color:var(--ink)}
.khead .ks{font-size:8.5px; letter-spacing:.17em; text-transform:uppercase; color:var(--violet); font-weight:700; margin-top:4px}
.khead .kpill{margin-left:auto; background:var(--ink); color:#fff; border-radius:999px; padding:7px 15px; font:700 11px/1 "DM Sans",Arial,sans-serif}
.kclose{position:sticky; top:0; float:right; margin:-10px -14px 0 12px; z-index:5;
  width:40px; height:40px; border-radius:50%; border:2px solid var(--accent);
  background:var(--accent); color:var(--on-accent); font:700 17px/1 "DM Sans",Arial,sans-serif;
  cursor:pointer; display:grid; place-items:center; box-shadow:0 4px 14px rgba(20,12,50,.35)}
.kclose:hover{background:var(--paper); color:var(--accent)}
.kclose:focus-visible{outline:2px solid var(--ink); outline-offset:2px}
.kesc{clear:both; text-align:center; font-size:10.5px; color:var(--muted); margin-top:8px;
  letter-spacing:.08em}
.kesc b{color:var(--violet)}
.ktitle{text-align:center; margin:16px 0 6px}
.ktitle .kp{display:inline-block; background:var(--accent); color:var(--on-accent); border-radius:999px; padding:5px 13px;
  font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.13em; text-transform:uppercase}
.ktitle .ksfera{font:700 10px/1.4 "DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase; color:var(--indigo); margin-top:9px}
.ktitle h3{font:700 26px/1.1 "DM Sans",Arial,sans-serif; color:var(--ink); margin:7px 0 0}
.ktitle .kpod{font:700 10.5px/1.4 "DM Sans",Arial,sans-serif; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); margin-top:6px}
.kmeta{display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin:14px 0 4px}
.kmeta .field{min-height:38px; padding:8px 12px}
.kmeta .field .lvl{margin-left:auto; width:24px; height:24px; border-radius:50%; display:grid; place-items:center;
  font:700 11px/1 "DM Sans",Arial,sans-serif; color:#fff}
.kmeta .field .lvl.p3{background:var(--p3)} .kmeta .field .lvl.p2{background:var(--p2)} .kmeta .field .lvl.p1{background:var(--p1)}
.ksec{display:flex; align-items:center; gap:9px; margin:18px 0 9px}
.ksec .sq{width:22px; height:22px; font-size:10px}
.ksec h4{font:700 12.5px/1.2 "DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase; color:var(--ink); margin:0}
.ksec .line{flex:1; height:1px; background:var(--line)}
.kcele{display:grid; grid-template-columns:1fr 1fr; gap:12px}
.kcel{border:1px solid var(--line); border-radius:8px; overflow:hidden; display:flex; flex-direction:column}
.kcel .kchead{color:#fff; text-align:center; font:700 11px/1 "DM Sans",Arial,sans-serif; letter-spacing:.08em; padding:8px}
.kcel.edu .kchead{background:var(--ink)} .kcel.ter .kchead{background:var(--accent); color:var(--on-accent)}
.kcel .ktresc{padding:11px 13px; font-size:12.5px; font-weight:600; color:var(--ink); border-bottom:1px solid var(--line-2)}
.kcel ul.ksmart{list-style:none; margin:0; padding:9px 13px; display:grid; gap:5px; align-content:start}
.kcel ul.ksmart li{display:flex; gap:9px; font-size:11.5px; line-height:1.45}
.kcel ul.ksmart b{color:var(--accent); font-family:"JetBrains Mono",monospace; flex:none}
.kcel .kkryt{background:var(--field); padding:8px 13px; font-size:11px; border-top:1px solid var(--line-2); margin-top:auto}
.kcel .kkryt b{color:var(--violet); font-size:9.5px; letter-spacing:.12em; text-transform:uppercase}
.kvar{display:none} .kvar.on{display:flex; flex-direction:column; flex:1}
.kdwie{display:grid; grid-template-columns:1fr 1fr; gap:16px}
ul.klista{list-style:none; margin:0; padding:0; display:grid; gap:5px}
ul.klista-2{grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:5px 24px}
/* Kody i liczniki nie mogą się łamać — „DE-R” pękało na myślniku. */
ul.klista-2 b,ul.klista-2 .mono{white-space:nowrap}
ul.klista-2 li.slaby .mono{color:var(--p3); font-weight:700}

/* Monitoring podstawy — 79 wierszy rozwijanych dopiero na życzenie. */
details.rozwin{margin-top:16px}
details.rozwin > summary{list-style:none; cursor:pointer; display:flex; align-items:center;
  gap:12px; padding:12px 16px; border:1px solid var(--line); border-radius:12px;
  background:var(--soft); transition:border-color .15s,background .15s}
details.rozwin > summary::-webkit-details-marker{display:none}
details.rozwin > summary:hover{border-color:var(--indigo); background:var(--field)}
.rozwin-tyt{font:700 13.5px/1 "DM Sans",Arial,sans-serif; color:var(--ink)}
.rozwin-info{font-size:10.5px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--violet); font-weight:700}
.rozwin-strzalka{margin-left:auto; color:var(--indigo); font-size:15px; transition:transform .15s}
details.rozwin[open] > summary{border-color:var(--indigo); background:var(--field);
  border-bottom-left-radius:0; border-bottom-right-radius:0}
details.rozwin[open] .rozwin-strzalka{transform:rotate(180deg)}
details.rozwin[open] .tablewrap{border-top-left-radius:0; border-top-right-radius:0}
ul.klista li{display:flex; gap:8px; font-size:12px; line-height:1.45}
ul.klista li::before{content:"●"; color:var(--accent); font-size:8px; line-height:1.9; flex:none}
table.ktab{min-width:0}
table.ktab th{padding:8px 11px}
table.ktab td{padding:8px 11px; font-size:11.5px}
table.ktab td.lp{font-size:12px}
.kmods{display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px}
.kmod{border:1px solid; border-radius:8px; padding:11px 14px; font-size:11.5px}
.kmod.m2{border-color:var(--p2-br); background:var(--p2-bg)} .kmod.m3{border-color:var(--p3-br); background:var(--p3-bg)}
.kmod.m1{border-color:var(--p1-br); background:var(--p1-bg)}
.kmod b{display:block; margin-bottom:6px; font:700 11px/1 "DM Sans",Arial,sans-serif}
.kmod.m2 b{color:var(--p2)} .kmod.m3 b{color:var(--p3)} .kmod.m1 b{color:var(--p1)}
.kmod{position:relative}
.kmod.aktywny{outline:2px solid var(--ink); outline-offset:1px}
.kmod.aktywny::after{content:"WYBRANY POZIOM"; position:absolute; top:-9px; right:10px; background:var(--ink);
  color:#fff; font:700 8px/1 "DM Sans",Arial,sans-serif; letter-spacing:.14em; padding:4px 8px; border-radius:999px}
.krodzaj{border:1px solid var(--line); border-radius:7px; background:var(--paper); padding:9px 13px; font-size:12px; min-height:38px; display:flex; align-items:center}
.kkurs{font-style:italic; font-size:11px; color:var(--muted); margin:8px 0 6px}
.kwsk{margin-top:12px; border-left:4px solid var(--accent); background:var(--soft); border-radius:0 8px 8px 0; padding:10px 14px; font-size:11.5px}
.kwsk b{color:var(--accent)}
.kfoot{display:flex; gap:9px; justify-content:flex-end; margin-top:18px}
@media screen and (max-width:860px){ .kcele,.kdwie,.kmods,.kmeta{grid-template-columns:1fr} .kcard{padding:18px 14px} }

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

/* ---------- druk: tabela poziomo, materiały pionowo ----------
   Bank celów drukuje się w poziomie, bo tabela ma trzy poziomy wsparcia obok
   siebie. Karty pomocy i arkusze do wycięcia to jednak druki A4 pionowo —
   dziedziczona orientacja pozioma kładła kartę na boku i zostawiała pół strony
   pustej. Nazwana strona `arkusz` obraca tylko te sekcje. */
@page{size:A4 landscape; margin:11mm 9mm 13mm}
@page arkusz{size:A4 portrait; margin:10mm}
@media print{
  body{background:#fff; font-size:8.6pt; color:#1F1A33}
  *{-webkit-print-color-adjust:exact; print-color-adjust:exact}
  .sheet{max-width:none; padding:0}
  .toolbar,.areanav,.printhead,.kspis{display:none !important}
  .vers{display:block !important}
  .vers + .vers{break-before:page; page-break-before:always}
  #konspekt,#monitoring{break-before:page; page-break-before:always}
  .kmodal{display:none !important}
  td.g.haskon .cel::after{display:none}
  html.print-konspekt .sheet,html.print-konspekt .toolbar{display:none !important}
  html.print-konspekt .kmodal.open{display:block !important; position:static; background:none; padding:0; overflow:visible}
  /* Konspekt to dokument pionowy jak arkusze — poziomo dziedziczone po tabeli
     banku kładło go na boku i rozciągało kolumny celów na całą szerokość. */
  html.print-konspekt .kcard{box-shadow:none; max-width:none; padding:0; border-radius:0; page:arkusz}
  html.print-konspekt .kclose,html.print-konspekt .kfoot,html.print-konspekt .kesc{display:none}
  /* Sekcja VII bez treści zostawiała nagłówek i pustą stronę. Wydruk konspektu
     niesie więc komplet do zajęć: scenariusz, kartę pomocy i arkusze — każde
     na własnej stronie A4 pionowo. Przyciski ekranowe znikają. */
  html.print-konspekt .zal-strefa{display:block !important}
  html.print-konspekt .zal-akcje,html.print-konspekt .zal-link{display:none !important}
  /* Wskazówka dla prowadzącego rozcinała się między stronami w pół zdania. */
  html.print-konspekt .callout,html.print-zal .callout{break-inside:avoid; page-break-inside:avoid}
  /* Gdy nikt nie wybrał poziomu (konspekt otwarty ze spisu), drukujemy wszystkie
     trzy zamiast pustej ramki po celu edukacyjnym. */
  /* Konspekt otwarty ze spisu nie ma wybranego poziomu. Zamiast pustej ramki po
     celu edukacyjnym drukujemy wszystkie trzy — w układzie zeszytu: cel
     terapeutyczny na całą szerokość u góry, poziomy w rzędzie pod nim. Bez tego
     trzy poziomy wciskały się w jedną kolumnę na 90 px. */
  html.print-konspekt .kcel.edu:not(:has(.kvar.on)) .kvar{display:flex !important; flex-direction:column}
  html.print-konspekt .kcele:not(:has(.kvar.on)){grid-template-columns:1fr !important; gap:12px}
  html.print-konspekt .kcele:not(:has(.kvar.on)) .kcel.ter{order:-1}
  html.print-konspekt .kcele:not(:has(.kvar.on)) .kcel.edu{display:grid !important;
    grid-template-columns:repeat(3,1fr); gap:10px; align-items:start}
  html.print-konspekt .kcele:not(:has(.kvar.on)) .kcel.edu .kchead{grid-column:1/-1}
  html.print-konspekt .kcele:not(:has(.kvar.on)) .kcel.edu .kvar{border:1px solid var(--line);
    border-radius:10px; padding:2px 0 0}
  html.print-zal .sheet,html.print-zal .toolbar{display:none !important}
  html.print-zal .kmodal:not(.open){display:none !important}
  html.print-zal .kmodal.open{display:block !important; position:static; background:none; padding:0; overflow:visible}
  html.print-zal .kcard{padding:0; box-shadow:none; max-width:none; border-radius:0; page:arkusz}
  html.print-zal .kcard > *{display:none !important}
  html.print-zal .kcard > .zal-strefa{display:block !important}
  html.print-zal .zal-link,html.print-zal .zal-akcje{display:none !important}
  details.rozwin > summary{display:none}
  details.rozwin > *:not(summary){display:block !important}
  .zal{break-inside:avoid; page-break-inside:avoid}
  .au-pasek,.au-btn{display:none !important}
  html.print-konspekt{--void:0}
  html.print-konspekt .kvar{display:none} html.print-konspekt .kvar.on{display:flex}
  html.print-konspekt .kcele,html.print-konspekt .kdwie{grid-template-columns:1fr 1fr !important}
  html.print-konspekt .kmods{grid-template-columns:1fr 1fr 1fr !important}
  html.print-konspekt .kmeta{grid-template-columns:repeat(4,1fr) !important}
  html.print-konspekt .kmeta.kdziecko{grid-template-columns:1.5fr 1fr 1fr !important}
  html.print-konspekt body{font-size:8.5pt}
  html.print-konspekt .kcard{padding:0}
  html.print-konspekt .khead{padding-bottom:6pt}
  html.print-konspekt .khead .kw{font-size:13pt}
  html.print-konspekt .ktitle{margin:8pt 0 2pt}
  html.print-konspekt .ktitle h3{font-size:17pt; margin-top:3pt}
  html.print-konspekt .ktitle .kpod{font-size:7pt; margin-top:3pt}
  html.print-konspekt .ktitle .ksfera{font-size:7pt; margin-top:5pt}
  html.print-konspekt .kmeta{margin:7pt 0 2pt; gap:5pt}
  html.print-konspekt .kmeta .field{min-height:24pt; padding:4pt 8pt}
  html.print-konspekt .ksec{margin:8pt 0 5pt}
  html.print-konspekt .ksec h4{font-size:8.5pt}
  html.print-konspekt .ksec .sq{width:14pt; height:14pt; font-size:7pt}
  html.print-konspekt .kcele{gap:7pt}
  html.print-konspekt .kcel .ktresc{padding:6pt 8pt; font-size:8pt}
  html.print-konspekt .kcel .kchead{padding:4pt; font-size:7.5pt}
  html.print-konspekt .kcel ul.ksmart{padding:5pt 8pt; gap:2pt}
  html.print-konspekt .kcel ul.ksmart li{font-size:7.6pt; line-height:1.35}
  html.print-konspekt .kcel .kkryt{padding:4pt 8pt; font-size:7.2pt}
  html.print-konspekt ul.klista li{font-size:7.8pt; line-height:1.35}
  html.print-konspekt ul.klista{gap:2pt}
  html.print-konspekt .kdwie{gap:9pt}
  html.print-konspekt .krodzaj{padding:4pt 8pt; font-size:7.8pt; min-height:20pt}
  html.print-konspekt .kkurs{font-size:7pt; margin:4pt 0 3pt}
  html.print-konspekt table.ktab th{padding:4pt 6pt; font-size:6.4pt}
  html.print-konspekt table.ktab td{padding:3.5pt 6pt; font-size:7.8pt}
  html.print-konspekt .kmods{gap:7pt}
  html.print-konspekt .kmod{padding:6pt 8pt; font-size:7.6pt}
  html.print-konspekt .kmod b{font-size:7.4pt; margin-bottom:3pt}
  html.print-konspekt .kwsk{margin-top:5pt; padding:4pt 8pt; font-size:7.4pt}
  html.print-konspekt .ksec{margin:6pt 0 4pt}
  html.print-konspekt .ktitle{margin:6pt 0 2pt}
  html.print-konspekt .ktitle h3{font-size:16pt}
  html.print-konspekt .kmeta{margin:6pt 0 2pt}
  html.print-konspekt .kmeta .field{min-height:21pt; padding:3pt 8pt}
  html.print-konspekt .kcel .ktresc{padding:5pt 8pt}
  html.print-konspekt .kcel ul.ksmart{padding:4pt 8pt}
  html.print-konspekt .kmod{padding:5pt 8pt}
  html.print-konspekt table.ktab td{padding:3pt 6pt}
  html.print-konspekt .kkurs{margin:3pt 0 2pt}
  html.print-konspekt .kmod.aktywny::after{font-size:5.5pt; top:-6pt}
  html.print-konspekt .kcard,html.print-konspekt .kcele,html.print-konspekt .kmods,
  html.print-konspekt table.ktab tr{break-inside:avoid; page-break-inside:avoid}
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

const LVLROM={p3:'III',p2:'II',p1:'I'};
function otworzKonspekt(id,lvl){
  const m=document.getElementById(id); if(!m) return;
  m.querySelectorAll('.kvar').forEach(v=>v.classList.toggle('on',v.dataset.lvl===lvl));
  const b=m.querySelector('[data-lvlbadge]');
  b.className='lvl '+lvl; b.textContent=LVLROM[lvl];
  m.querySelectorAll('.kmod').forEach(x=>x.classList.toggle('aktywny',x.dataset.mod===lvl));
  m.classList.add('open'); document.body.style.overflow='hidden';
  m.querySelector('.kclose').focus();
}
function zamknijKonspekty(){
  document.querySelectorAll('.kmodal.open').forEach(m=>m.classList.remove('open'));
  document.body.style.overflow='';
}
document.querySelectorAll('.kbtn[data-kon]').forEach(b=>b.addEventListener('click',
  ()=>otworzKonspekt(b.dataset.kon, b.dataset.lvl2)));
document.querySelectorAll('td.haskon').forEach(td=>{
  const go=()=>otworzKonspekt(td.dataset.kon,td.dataset.lvl2);
  td.addEventListener('click',go);
  td.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();go();}});
});
document.querySelectorAll('[data-close]').forEach(b=>b.addEventListener('click',zamknijKonspekty));
document.querySelectorAll('.kmodal').forEach(m=>m.addEventListener('click',e=>{if(e.target===m)zamknijKonspekty();}));
document.addEventListener('keydown',e=>{if(e.key==='Escape')zamknijKonspekty();});
/* Odtwarzanie narracji do historyjki obrazkowej.
   Jedna ścieżka naraz; sekwencja przechodzi do kolejnego nagrania po zakończeniu
   poprzedniego, a kafelek aktualnie czytanej sceny dostaje obwódkę. */
(function(){
  let kolejka=[], krok=0, biezacy=null, zrodlo=null;
  const podswietl=(id,wl)=>{
    document.querySelectorAll(`.au-btn[data-au="${id}"]`).forEach(b=>{
      b.classList.toggle('gra',wl); b.closest('.kafel')?.classList.toggle('gra',wl);
    });
  };
  function stop(){
    if(biezacy){biezacy.pause(); biezacy.currentTime=0; podswietl(biezacy.id,false);}
    document.querySelectorAll('.au-all.gra').forEach(b=>b.classList.remove('gra'));
    biezacy=null; zrodlo=null; kolejka=[]; krok=0;
  }
  function graj(id){
    const a=document.getElementById(id); if(!a) return;
    if(biezacy&&biezacy!==a){biezacy.pause(); biezacy.currentTime=0; podswietl(biezacy.id,false);}
    biezacy=a; podswietl(id,true); a.currentTime=0;
    a.play().catch(()=>{});
    a.onended=()=>{
      podswietl(id,false);
      if(krok<kolejka.length){graj(kolejka[krok++]);}
      else{zrodlo?.classList.remove('gra'); zrodlo=null; biezacy=null;}
    };
  }
  document.querySelectorAll('.au-btn').forEach(b=>b.addEventListener('click',()=>{
    const id=b.dataset.au;
    if(biezacy&&biezacy.id===id&&!biezacy.paused){stop(); return;}
    stop(); graj(id);
  }));
  document.querySelectorAll('.au-all').forEach(b=>b.addEventListener('click',()=>{
    if(zrodlo===b){stop(); return;}
    stop(); zrodlo=b; b.classList.add('gra');
    kolejka=b.dataset.auSeq.split(','); krok=1; graj(kolejka[0]);
  }));
  document.querySelectorAll('.au-stop').forEach(b=>b.addEventListener('click',stop));
  /* Druk i zamknięcie konspektu wyciszają narrację. */
  window.addEventListener('beforeprint',stop);
  document.addEventListener('keydown',e=>{if(e.key==='Escape') stop();});
})();

/* Podgląd załączników na ekranie — bez tego karty (i przyciski odsłuchu)
   byłyby widoczne wyłącznie w chwili drukowania. */
document.querySelectorAll('[data-pokazzal]').forEach(b=>b.addEventListener('click',()=>{
  const strefa=document.getElementById(b.dataset.pokazzal).querySelector('.zal-strefa');
  if(!strefa) return;
  const widac=strefa.style.display==='block';
  strefa.style.display=widac?'none':'block';
  b.setAttribute('aria-expanded',String(!widac));
  b.textContent=widac?'Pokaż załączniki i posłuchaj narracji':'Ukryj załączniki';
  if(!widac) strefa.scrollIntoView({behavior:'smooth',block:'start'});
}));

document.querySelectorAll('[data-printzal]').forEach(b=>b.addEventListener('click',()=>{
  const strefa=document.getElementById(b.dataset.printzal).querySelector('.zal-strefa');
  strefa.style.display='block';
  document.documentElement.classList.add('print-zal');
  const done=()=>{document.documentElement.classList.remove('print-zal'); strefa.style.display='none';
    window.removeEventListener('afterprint',done);};
  window.addEventListener('afterprint',done);
  window.print();
}));
document.querySelectorAll('[data-printkon]').forEach(b=>b.addEventListener('click',()=>{
  document.documentElement.classList.add('print-konspekt');
  const done=()=>{document.documentElement.classList.remove('print-konspekt'); window.removeEventListener('afterprint',done);};
  window.addEventListener('afterprint',done);
  window.print();
}));
"""

def esc(s): return html.escape(str(s), quote=False)

def wiersz(it, w):
    pp = it["pp"][3:] if it["pp"].startswith("PP ") else it["pp"]
    kid = f"kon-{w['kod']}-{it['n']}" if (w["kod"], it["n"]) in KONSPEKTY else ""
    kattr = lambda lvl: (f' class="g {lvl} col-{lvl} haskon" tabindex="0" role="button" data-kon="{kid}" data-lvl2="{lvl}"'
                         if kid else f' class="g {lvl} col-{lvl}"')
    szukaj = " ".join([it["t"], it["g3"], it["g2"], it["g1"], it["icf"], it["pp"],
                       w["etykieta"], "wersja " + w["kod"]]).lower()
    return f"""        <tr data-szukaj="{esc(szukaj)}">
          <td class="lp">{it['n']}</td>
          <td class="tw">{esc(it['t'])}<span class="miara"><b>Miara:</b> {esc(it['m'])}</span></td>
          <td class="icf"><span class="kod">{esc(it['icf'])}</span></td>
          <td class="pp"><span class="kod">{esc(pp)}</span></td>
          <td{kattr('p3')}><span class="cel">{esc(it['g3'])}</span></td>
          <td{kattr('p2')}><span class="cel">{esc(it['g2'])}</span></td>
          <td{kattr('p1')}><span class="cel">{esc(it['g1'])}</span></td>
        </tr>"""

def sekcja(a, w):
    rows = "\n".join(wiersz(i, w) for i in a["items"])
    aid = f"{w['kod']}-{a['icf']}-{a['rom']}"
    # Wersja U nie pochodzi z arkuszy KPOF — nazwa kolumny i druku musi to mówić.
    uzup = w["kod"] == "U"
    naglowek_tw = ("Cel uzupełniający · obserwowane zachowanie" if uzup
                   else "Twierdzenie KPOF · obserwowane zachowanie")
    druk = "KC-1u" if uzup else "KC-1"
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
        <tr class="tbanner"><th colspan="7">EduPlaner 2026 · druk {druk} · bank celów SMART<span class="bsep">·</span>Wersja {w['kod']} · {esc(w['etykieta'])}<span class="bsep">·</span>Obszar {a['rom']} · {esc(a['name'])}<span class="bsep">·</span>ICF {a['icf']}</th></tr>
        <tr>
          <th class="c-lp">Lp.</th>
          <th class="c-tw">{naglowek_tw}</th>
          <th class="c-code h-icf">ICF</th>
          <th class="c-code h-pp">Podst.</th>
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

def spis_konspektow(mod, w):
    """Spis konspektów wersji — bez niego trzeba wiedzieć, że konspekt otwiera
    się kliknięciem komórki z celem. Każda pozycja otwiera modal wprost."""
    pozycje, ile = [], 0
    for a in mod.AREAS:
        w_obszarze = []
        for it in a["items"]:
            K = KONSPEKTY.get((w["kod"], it["n"]))
            if not K:
                continue
            ile += 1
            # kropka znaczy „konspekt ma gotowy materiał" — kartę pomocy albo arkusz
            # do wydruku. Wersja U nie ma kart pomocy, ale ma arkusze.
            tytul_znaku = ("ma pomoc dydaktyczną i materiał do wydruku"
                           if wskaz_pomoc(K["nr"]) and ma_karty(K["nr"])
                           else "ma pomoc dydaktyczną" if wskaz_pomoc(K["nr"])
                           else "ma materiał do wydruku")
            znak = (f'<span class="pom" title="{tytul_znaku}">●</span>'
                    if wskaz_pomoc(K["nr"]) or ma_karty(K["nr"]) else "")
            w_obszarze.append(
                f'      <button class="kbtn" type="button" data-kon="kon-{w["kod"]}-{it["n"]}" data-lvl2="p2">'
                f'<b>{esc(K["nr"])}</b><span class="tyt">{esc(K["tytul"])}</span>{znak}</button>')
        if w_obszarze:
            pozycje.append(f'    <div class="kspis-obszar">{a["rom"]} · {esc(a["name"].split(" (")[0])}</div>\n'
                           f'    <div class="kspis-lista">\n' + "\n".join(w_obszarze) + "\n    </div>")
    if not pozycje:
        return ""
    # Zwinięty, ale pasek jest w kolorze akcentu i mówi wprost, co się pod nim
    # kryje — spis chowany w szarej belce był wcześniej nie do znalezienia.
    return (f'  <details class="kspis">\n'
            f'    <summary>Wykaz konspektów<span class="rozwin"> — kliknij, aby rozwinąć</span>'
            f'<span class="zwin"> — kliknij, aby zwinąć</span>'
            f'<span class="ile">{ile} konspektów · ● z pomocą dydaktyczną</span></summary>\n'
            f'    <div class="kspis-tresc">\n' + "\n".join(pozycje) + "\n    </div>\n  </details>")


def wersja(mod, aktywna):
    w = mod.WERSJA
    n = sum(len(a["items"]) for a in mod.AREAS)
    secs = "\n".join(sekcja(a, w) for a in mod.AREAS)
    nav = "\n".join(
        f'    <a class="navlink" href="#{w["kod"]}-{a["icf"]}-{a["rom"]}">{a["rom"]} · {esc(a["name"].split(" (")[0])}</a>'
        for a in mod.AREAS)
    spis = spis_konspektow(mod, w)
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
{spis}
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
      <th class="c-code h-icf">ICF</th>
      <th class="c-code h-pp">Podst.</th>
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



def render_konspekty_modale(tylko_wersja=None):
    """Modale konspektów wg wzoru Termometr uwagi; warianty celu edukacyjnego per poziom.

    `tylko_wersja` zawęża wynik do jednej wersji wiekowej — korzysta z tego
    `build_konspekty.py`, żeby wydać konspekty jednej grupy jako osobny zeszyt.
    """
    def smart_edu(it, poz_kod):
        meta = next(p for p in POZIOMY if p[0] == poz_kod)
        cel = {"p3": it["g3"], "p2": it["g2"], "p1": it["g1"]}[poz_kod]
        m = cel.rsplit("— w ", 1)
        miern = ("w " + m[1]) if len(m) == 2 else it["m"]
        return [
            ("S", it["t"] + "."),
            ("M", miern.rstrip('.') + '.'),
            ("A", meta[5].capitalize() + "."),
            ("R", f"ICF {it['icf']} · PP {it['pp'].replace('PP ','')} — spójne z KPOF, WOPF i IPET."),
            ("T", f"Ewaluacja po {meta[4].replace('tyg.','tygodniach')} ({meta[1]})."),
        ], cel, meta
    out = []
    for (wk, nr), K in KONSPEKTY.items():
        if tylko_wersja and wk != tylko_wersja:
            continue
        mod = {m.WERSJA["kod"]: m for m in WERSJE}[wk]
        it = next(i for a in mod.AREAS for i in a["items"] if i["n"] == nr)
        wers = mod.WERSJA
        warianty = []
        for poz_kod in ("p3", "p2", "p1"):
            sm, cel, meta = smart_edu(it, poz_kod)
            sm_li = "\n".join(f'              <li><b>{L}</b><span>{esc(t)}</span></li>' for L, t in sm)
            warianty.append(f"""        <div class="kvar" data-lvl="{poz_kod}">
          <div class="ktresc">{esc(cel)}</div>
          <ul class="ksmart">
{sm_li}
          </ul>
          <div class="kkryt"><b>Kryterium:</b> {esc(it['m'])} · horyzont {esc(meta[4])}</div>
        </div>""")
        ter_li = "\n".join(f'              <li><b>{L}</b><span>{esc(t)}</span></li>' for L, t in K["ter_smart"])
        pom_li = "\n".join(f'        <li>{esc(x)}</li>' for x in K["pomoce"])
        if K["nr"] == "C1-01":
            pom_li += '\n        <li><b style="color:var(--accent)">Załączniki Z1–Z3 — gotowe historyjki do wydruku (poniżej)</b></li>' 
        met_li = "\n".join(f'        <li>{esc(x)}</li>' for x in K["metody"])
        prz = "\n".join(f"""        <tr><td class="lp">{i}</td><td>{esc(n)}</td><td>{esc(d)}</td></tr>"""
                        for i, (n, d) in enumerate(K["przebieg"], 1))
        m2 = "\n".join(f'          <li>{esc(x)}</li>' for x in K["mod2"])
        m3 = "\n".join(f'          <li>{esc(x)}</li>' for x in K["mod3"])
        m1 = "\n".join(f'          <li>{esc(x)}</li>' for x in K.get("mod1", []))
        kid = f"kon-{wk}-{nr}"
        zal = ""
        wsk = wskaz_pomoc(K["nr"])
        # Historyjki obrazkowe C1-01 dokładamy do strefy załączników, a nie zamiast
        # niej: ten konspekt ma też własną kartę pomocy i arkusz do wycięcia, a osobna
        # gałąź nadpisywała całą sekcję VII i jedno i drugie z niej znikało.
        extra = zalaczniki_c1() if K["nr"] == "C1-01" else ""
        if not wsk and ma_karty(K["nr"]):
            # Konspekt bez fotograficznej karty pomocy, ale z materiałem do wydruku.
            # Bez tej gałęzi arkusze wersji C i U znikały bez śladu — sekcja VII
            # renderowała się wyłącznie przy istniejącej karcie pomocy.
            zal = f"""    <div class="ksec"><span class="sq">VII</span><h4>Materiały do wydruku</h4><span class="line"></span>
      <span class="meta">arkusze A4 gotowe do wydrukowania</span></div>
    <p class="kkurs">Konspekt wymaga materiału, którego nie da się zastąpić opisem — kart do
    wycięcia, planszy albo arkusza do wypełniania. Wszystko, czego potrzeba, jest poniżej,
    w formacie A4. Każdy arkusz zaczyna przy druku nową stronę.</p>
    <div class="zal-akcje">
      <button class="zal-link zal-pokaz" data-pokazzal="{kid}" aria-expanded="false">Pokaż materiały do wydruku</button>
      <button class="zal-link" data-printzal="{kid}">Drukuj arkusze (A4)</button>
    </div>
    <div class="zal-strefa" style="display:none">
{karty_dla(K["nr"], esc)}
{extra}
    </div>
"""
        if wsk:
            pkod, ptytul, pwiek, pplik = wsk
            zal = f"""    <div class="ksec"><span class="sq">VII</span><h4>Pomoc dydaktyczna</h4><span class="line"></span>
      <span class="meta">zdjęcie poglądowe · polecenie głosem nauczycielki</span></div>
    <p class="kkurs">Jak ma wyglądać pomoc, co przygotować i jak jej użyć w trzech krokach.
    Karta jest gotowa do wydruku A4. Ten sam komplet kart dla całej grupy wiekowej
    zebrany jest w zeszycie <b>Pomoce dydaktyczne · {esc(pwiek)}</b>.{
    " Konspekt ma też gotowy materiał do wydrukowania i wycięcia — arkusze poniżej."
    if ma_karty(K["nr"]) else ""}{
    " Poniżej także trzy historyjki obrazkowe w gradacji trudności, po jednej na poziom wsparcia."
    if extra else ""}</p>
    <div class="zal-akcje">
      <button class="zal-link zal-pokaz" data-pokazzal="{kid}" aria-expanded="false">Pokaż pomoc i posłuchaj polecenia</button>
      <button class="zal-link" data-printzal="{kid}">Drukuj kartę pomocy (A4)</button>
    </div>
    <div class="zal-strefa" style="display:none">
{pomoce_dla(K["nr"], esc)}
{karty_dla(K["nr"], esc)}
{extra}
    </div>
"""
        out.append(f"""<div class="kmodal" id="{kid}" role="dialog" aria-modal="true" aria-label="Konspekt: {esc(K['tytul'])}">
  <div class="kcard">
    <button class="kclose" data-close="{kid}" aria-label="Zamknij konspekt" title="Zamknij (Esc)">✕</button>
    <div class="khead">
      <span class="mark" role="img" aria-label="Logo PCTP"></span>
      <div>
        <div class="kw">EduPlaner 2026</div>
        <div class="ks">Konspekt · {esc(K['sfera'].split('·')[0].strip())} · {esc(wers['etykieta'])} · wersja {wk} · twierdzenie {nr}</div>
      </div>
      <span class="kpill">Konspekt {esc(K['nr'])}</span>
    </div>
    <div class="kmeta kdziecko" style="grid-template-columns:1.5fr 1fr 1fr; margin:12px 0 0">
      <div class="field"><b>Dotyczy dziecka</b><span class="dots"></span></div>
      <div class="field"><b>Grupa</b><span class="dots"></span></div>
      <div class="field"><b>Data</b><span class="dots"></span></div>
    </div>
    <div class="ktitle">
      <span class="kp">Konspekt zajęć · druk KC-3</span>
      <div class="ksfera">{esc(K['sfera'])}</div>
      <h3>{esc(K['tytul'])}</h3>
      <div class="kpod">{esc(K['podtytul'])}</div>
    </div>
    <div class="kmeta">
      <div class="field"><b>Czas</b><span class="val">{esc(K['czas'])}</span></div>
      <div class="field"><b>Forma</b><span class="val">{esc(K['forma'])}</span></div>
      <div class="field"><b>Cykl</b><span class="val">{esc(K['cykl'])}</span></div>
      <div class="field"><b>Poziom wsparcia</b><span class="lvl p2" data-lvlbadge>II</span></div>
    </div>
    <div class="ksec"><span class="sq">I</span><h4>Cel SMART</h4><span class="line"></span></div>
    <div class="kcele">
      <div class="kcel edu"><div class="kchead">Cel edukacyjny — z banku KC-1, wg klikniętego poziomu</div>
{chr(10).join(warianty)}
      </div>
      <div class="kcel ter"><div class="kchead">Cel terapeutyczny</div>
        <div class="ktresc">{esc(K['ter'])}</div>
        <ul class="ksmart">
{ter_li}
        </ul>
        <div class="kkryt"><b>Kryterium:</b> {esc(K['ter_kryt'])}</div>
      </div>
    </div>
    <div class="kdwie">
      <div>
        <div class="ksec"><span class="sq">II</span><h4>Pomoce dydaktyczne</h4><span class="line"></span></div>
        <ul class="klista">
{pom_li}
        </ul>
      </div>
      <div>
        <div class="ksec"><span class="sq">III</span><h4>Metody i formy działań</h4><span class="line"></span></div>
        <ul class="klista">
{met_li}
        </ul>
      </div>
    </div>
    <div class="kdwie" style="align-items:end">
      <div>
        <div class="ksec"><span class="sq">IV</span><h4>Sposób realizacji</h4><span class="line"></span></div>
        <div class="krodzaj" style="font-style:italic">Tabela poniżej ↓</div>
      </div>
      <div>
        <div class="ksec"><span class="sq">V</span><h4>Rodzaj zajęć</h4><span class="line"></span></div>
        <div class="krodzaj">{esc(K['rodzaj'])}</div>
      </div>
    </div>
    <p class="kkurs">Konkretne czynności nauczyciela (N) i odpowiadające im oczekiwane reakcje i umiejętności dziecka (D).</p>
    <div class="tablewrap"><table class="ktab">
      <thead><tr><th class="c-lp">Lp.</th><th style="width:47%">Czynności nauczyciela (N)</th>
        <th>Oczekiwane reakcje i umiejętności dziecka (D)</th></tr></thead>
      <tbody>
{prz}
      </tbody>
    </table></div>
    <div class="ksec"><span class="sq">VI</span><h4>Modyfikacja przy ocenie żółtej / czerwonej</h4><span class="line"></span></div>
    <p class="kkurs">Modyfikację stosuje się, gdy brak progresu w dwóch kolejnych sesjach. Zielona — rozszerzenie przy pełnym sukcesie. Kliknięty poziom wyróżniony.</p>
    <div class="kmods">
      <div class="kmod m2" data-mod="p2"><b>Poziom II · Żółta</b><ul class="klista">
{m2}
      </ul></div>
      <div class="kmod m3" data-mod="p3"><b>Poziom III · Czerwona</b><ul class="klista">
{m3}
      </ul></div>
      <div class="kmod m1" data-mod="p1"><b>Poziom I · Zielona</b><ul class="klista">
{m1}
      </ul></div>
    </div>
    <div class="kwsk"><b>Wskazówka dla prowadzącego:</b> {esc(K['wskazowka'])}</div>
{zal}
    <div class="kfoot">
      <button class="chipbtn zamknij" data-close="{kid}">✕ Zamknij i wróć do tabeli</button>
      <button class="chipbtn" style="background:var(--strong); border-color:var(--strong); color:var(--on-strong)" data-printkon="{kid}">Drukuj konspekt A4</button>
    </div>
    <p class="kesc">zamkniesz też klawiszem <b>Esc</b> lub kliknięciem w ciemne tło poza kartą</p>
  </div>
</div>""")
    return "\n".join(out)



def monitoring_podstawy():
    """Monitoring realizacji podstawy programowej — punkty PP pokryte przez cele i konspekty."""
    # Jedno źródło nazw obszarów — legenda i kolumna tabeli muszą mówić to samo.
    # Wcześniej legenda opisywała cztery obszary rozwoju, a tabela grupowała punkty
    # w dziewięć, przez co „1" znaczyło w niej co innego niż w legendzie.
    OBSZAR_PP_NAZWY = {
        "1": "społeczny", "2": "osobisty", "3": "językowy", "4": "matematyczny",
        "5": "przyrodniczy", "6": "techniczny", "7": "cyfrowy", "8": "artystyczny", "9": "ruchowy",
    }
    OBSZARY_PP = {
        "DE-R": "doświadczenie edukacyjne — raz w roku szkolnym",
        "DE-P": "doświadczenie — raz w trakcie edukacji przedszkolnej",
        "WSR": "warunki i sposób realizacji",
        "Zad.": "zadanie przedszkola",
    }
    # Liczba punktów w każdym obszarze — policzona z załącznika nr 1 do
    # rozporządzenia (podstawa_2026/podsawa.pdf), razem 113 punktów osiągnięć.
    # Dzięki temu monitoring pokazuje pokrycie „17 z 20”, a nie samą liczbę
    # punktów, których bank przypadkiem dotyka.
    PP_2026_PUNKTY = {"1": 20, "2": 12, "3": 21, "4": 15, "5": 12,
                      "6": 9, "7": 5, "8": 8, "9": 11}
    PP_2026_RAZEM = sum(PP_2026_PUNKTY.values())
    # Poza punktami osiągnięć załącznik ma: 16 zadań przedszkola, 11 pozycji
    # warunków realizacji oraz doświadczenia edukacyjne w dwóch listach —
    # 7 pozycji „co najmniej raz w roku szkolnym” (kody DE-R) i 4 pozycje
    # „przynajmniej raz w trakcie edukacji przedszkolnej”, których arkusze
    # KPOF jeszcze nie kodują.
    PP_2026_POZA = {"Zad.": 16, "WSR": 11, "DE-R": 7, "DE-P": 4}
    DE_R_TRESC = {
        "DE-R.1": "jest odbiorcą sztuki — koncert, teatr, muzeum",
        "DE-R.2": "prowadzi i ilustruje obserwacje przyrody",
        "DE-R.3": "w grupie wysiewa i uprawia warzywa, zioła lub kwiaty",
        "DE-R.4": "w grupie przygotowuje wspólne wyjście i bierze w nim udział",
        "DE-R.5": "odgrywa uzgodnioną rolę w występie lub spotkaniu społeczności",
        "DE-R.6": "uczestniczy w wydarzeniu promującym zdrowy styl życia",
        "DE-R.7": "w grupie prezentuje wiedzę lub efekty wspólnych działań",
    }
    DE_P_TRESC = [
        "przez minimum 10 kolejnych dni tworzy własne zabawki z materiałów, w tym z odzysku",
        "w grupie przygotowuje makietę wybranej przestrzeni",
        "w grupie planuje i podejmuje działanie na rzecz innych",
        "planuje i robi w grupie zakupy w sklepie",
    ]
    # zbiór punktów PP z twierdzeń, z informacją gdzie występują
    rejestr = {}
    for mod in WERSJE:
        w = mod.WERSJA
        for a in mod.AREAS:
            for it in a["items"]:
                pp = it["pp"][3:] if it["pp"].startswith("PP ") else it["pp"]
                for punkt in pp.replace("·", " ").split():
                    rej = rejestr.setdefault(punkt, {"wersje": set(), "obszary": set(), "kon": 0})
                    rej["wersje"].add(w["kod"])
                    rej["obszary"].add(a["rom"])
                    if (w["kod"], it["n"]) in KONSPEKTY:
                        rej["kon"] += 1
    def sort_key(p):
        czesci = p.split(".")
        try:
            return (0, int(czesci[0]), int(czesci[1]) if len(czesci) > 1 else 0)
        except ValueError:
            return (1, 0, 0)
    wiersze = []
    for i, punkt in enumerate(sorted(rejestr, key=sort_key), 1):
        r = rejestr[punkt]
        grupa = punkt.split(".")[0]
        nazwa = OBSZAR_PP_NAZWY.get(grupa, "zapis szczególny")
        wersje = " · ".join(sorted(r["wersje"]))
        obszary = ", ".join(sorted(r["obszary"], key=lambda x: ["I","II","III","IV","V","VI","VII","VIII","IX"].index(x)))
        # Liczba konspektow, nie samo „konspekt": kazdy punkt jakis ma, wiec samo
        # slowo bylo w kazdym z 79 wierszy takie samo i niczego nie mowilo.
        stan = (f"{r['kon']} konspekt" + ("" if r["kon"] == 1 else
                "y" if 2 <= r["kon"] <= 4 else "ów")) if r["kon"] else "sam cel SMART"
        klasa = "p1" if r["kon"] else "p2"
        wiersze.append(f"""        <tr>
          <td class="lp">{i}</td>
          <td class="pp"><span class="kod">{esc(punkt)}</span></td>
          <td class="tw">{esc(nazwa.capitalize())}</td>
          <td class="mono" style="white-space:nowrap">{esc(wersje)}</td>
          <td>{esc(obszary)}</td>
          <td class="g {klasa}"><span class="cel">{esc(stan)}</span></td>
        </tr>""")
    n_pkt = len(rejestr)
    n_odw = sum(r["kon"] for r in rejestr.values())
    n_osiag = sum(1 for p in rejestr if p.split(".")[0] in PP_2026_PUNKTY)
    wersje_kody = " · ".join(m.WERSJA["kod"] for m in WERSJE)
    # Obszary pokryte słabiej niż w połowie — tam bank ma realne luki.
    cienkie = []
    for k, nazwa in OBSZAR_PP_NAZWY.items():
        ile = sum(1 for p in rejestr if p.split(".")[0] == k)
        if ile * 2 < PP_2026_PUNKTY[k]:
            cienkie.append(f'<b>{k}</b> {nazwa} ({ile} z {PP_2026_PUNKTY[k]})')
    brak_der = [k for k in DE_R_TRESC if k not in rejestr]
    # Legenda z liczba punktow w kazdej grupie — od razu widac, gdzie jest ich duzo.
    liczba_w_grupie = {}
    for punkt in rejestr:
        liczba_w_grupie[punkt.split(".")[0]] = liczba_w_grupie.get(punkt.split(".")[0], 0) + 1
    poz = []
    for kod, nazwa in OBSZAR_PP_NAZWY.items():
        ile, wszystkich = liczba_w_grupie.get(kod, 0), PP_2026_PUNKTY[kod]
        slaby = ' class="slaby"' if ile * 2 < wszystkich else ""
        poz.append(f'      <li{slaby}><b>{kod}</b> — obszar {esc(nazwa)} '
                   f'<span class="mono">({ile} z {wszystkich} pkt)</span></li>')
    for kod, opis in OBSZARY_PP.items():
        ile = liczba_w_grupie.get(kod.rstrip("."), 0)
        if ile:
            z_ilu = PP_2026_POZA.get(kod)
            licznik = f"({ile} z {z_ilu})" if z_ilu else f"({ile} — poza numeracją)"
            poz.append(f'      <li><b>{esc(kod)}</b> — {esc(opis)} '
                       f'<span class="mono">{licznik}</span></li>')
    obszary_html = "\n".join(poz)
    luki = []
    if cienkie:
        luki.append('Poniżej połowy punktów pokrywają obszary: ' + ", ".join(cienkie)
                    + '. To brak w twierdzeniach KPOF, z których wyrasta ten bank, '
                      'nie w podstawie — te obszary warto uzupełnić w kolejnej wersji arkuszy.')
    if brak_der:
        luki.append('Z siedmiu doświadczeń edukacyjnych „co najmniej raz w roku szkolnym” bank '
                    'nie obejmuje: ' + ", ".join(f'<b>{esc(k)}</b> — {esc(DE_R_TRESC[k])}'
                                                 for k in brak_der) + '.')
    brak_dep = [i for i in range(1, 5) if f"DE-P.{i}" not in rejestr]
    if brak_dep:
        luki.append('Z czterech doświadczeń „przynajmniej raz w trakcie edukacji przedszkolnej” '
                    'bank nie obejmuje: '
                    + "; ".join(esc(DE_P_TRESC[i - 1]) for i in brak_dep) + '.')
    luki_html = ("" if not luki else
        '  <div class="callout rule"><span class="cap">Do uzupełnienia</span>'
        + " ".join(f"<p style=\"margin:0 0 6px\">{t}</p>" for t in luki) + '</div>')
    return f"""<section class="sec" id="monitoring">
  <div class="vband">
    <span class="vlet">PP</span>
    <h2>Monitoring realizacji podstawy programowej</h2>
    <div class="vmeta">
      <span><b>Pokrycie osiągnięć</b>{n_osiag} z {PP_2026_RAZEM}</span>
      <span><b>Odwołań z konspektów</b>{n_odw}</span>
      <span><b>Wersje</b>{wersje_kody}</span>
      <span><b>Podstawa</b>Dz.U. 2026 poz. 378</span>
    </div>
  </div>
  <p class="vdesc">Zestawienie wszystkich punktów podstawy programowej wychowania przedszkolnego, do których
  odwołują się twierdzenia KPOF i cele z tego banku. Kolumna „Realizacja” pokazuje, iloma konspektami zajęć
  punkt jest pokryty — łącznie we wszystkich trzech wersjach wiekowych. Tabela służy do wykazania realizacji
  podstawy w dokumentacji nadzoru pedagogicznego.</p>
  <div class="callout rule"><span class="cap">Podstawa prawna</span>
  Tabela odwzorowuje <b>nową podstawę programową wychowania przedszkolnego</b> — rozporządzenie Ministra
  Edukacji z 11 marca 2026 r. (Dz. U. 2026 poz. 378), obowiązujące od 1 września 2026 r. Zastąpiła ona
  dotychczasowe cztery obszary rozwoju (fizyczny, emocjonalny, społeczny, poznawczy) <b>dziewięcioma
  obszarami osiągnięć dziecka</b>: społecznym, osobistym, językowym, matematycznym, przyrodniczym,
  technicznym, cyfrowym, artystycznym i ruchowym. Zapis <i>obszar.punkt</i> w kolumnie „Punkt” odpowiada
  tej numeracji i jest ten sam w arkuszach KPOF, w celach SMART i w konspektach.
  </div>
  <div class="callout"><span class="cap" style="color:var(--violet)">Grupy punktów w zapisie <i>obszar.punkt</i></span>
  <ul class="klista klista-2" style="margin-top:6px">
{obszary_html}
  </ul></div>
{luki_html}
  <details class="rozwin">
  <summary><span class="rozwin-tyt">Pokaż pełną tabelę monitoringu</span>
    <span class="rozwin-info">{n_pkt} wierszy · {n_osiag} z {PP_2026_RAZEM} punktów osiągnięć</span>
    <span class="rozwin-strzalka" aria-hidden="true">▾</span></summary>
  <div class="tablewrap"><table>
    <thead>
      <tr class="tbanner"><th colspan="6">EduPlaner 2026 · druk KC-1 · monitoring podstawy programowej<span class="bsep">·</span>Wszystkie wersje wiekowe<span class="bsep">·</span>Zapis obszar.punkt</th></tr>
      <tr>
        <th class="c-lp">Lp.</th>
        <th class="c-code h-pp">Punkt</th>
        <th class="c-tw">Obszar podstawy</th>
        <th class="c-code">Wersje</th>
        <th>Obszary ICF, w których punkt występuje</th>
        <th class="c-goal">Realizacja</th>
      </tr>
    </thead>
    <tbody>
{chr(10).join(wiersze)}
    </tbody>
  </table></div>
  </details>
  <div class="callout rule"><span class="cap">Jak korzystać</span>Liczba w kolumnie „Realizacja” mówi, ile
  konspektów pokrywa dany punkt — każdy z nich otwiera się kliknięciem w komórkę poziomu wsparcia w tabeli banku.
  Punkt opisany jako <b>sam cel SMART</b> jest pokryty celem, do którego konspekt powstanie w kolejnych wersjach
  druku. Wydruk zawiera całą tabelę niezależnie od tego, czy jest rozwinięta na ekranie.</div>
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
<link rel="stylesheet" media="print" onload="this.media='all'"
      href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;700&display=swap">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;700&display=swap"></noscript>
<style>:root{{--logo:url({LOGO_URI})}}
{CSS}</style>

<div class="sheet">

<div class="dochead">
  <span class="mark" role="img" aria-label="Logo PCTP"></span>
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

{monitoring_podstawy()}

{konspekt()}

<div class="docfoot">
  <span>EduPlaner 2026 · PCTP · pedagog specjalny mgr Mirosława Ewa Jurczyszyn</span>
  <span class="mono">Druk KC-1 · {razem} twierdzeń · {razem*3} celów SMART · wersje A / B / C</span>
</div>

</div>
{style_pomocy()}{audio_pomocy()}{style_kart()}
{render_konspekty_modale()}
<script>{JS}</script>
"""

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "Bank_celow_SMART_KPOF.html")
    open(out, "w", encoding="utf-8").write(build())
    print("zapisano:", out, os.path.getsize(out), "B")
