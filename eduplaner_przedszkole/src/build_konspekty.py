# -*- coding: utf-8 -*-
"""Konspekty jako osobny zeszyt na każdą grupę wiekową.

Po co: w banku konspekt otwiera się kliknięciem — świetnie przy planowaniu
przy komputerze, bezużytecznie, gdy chce się mieć konspekty pod ręką albo
wydrukować komplet. Dotąd istniały tylko jako 27 osobnych PDF-ów (obszar ×
wiek), czyli w praktyce nie do znalezienia.

Zeszyt zawiera komplet konspektów jednej wersji, w kolejności obszarów,
każdy z pomocą dydaktyczną w sekcji VII. Jest samowystarczalny — zdjęcia
i nagrania siedzą w środku.

Uruchomienie: python3 src/build_konspekty.py
"""

import datetime
import os

from build import (CSS, LOGO_URI, KONSPEKTY, WERSJE, esc,
                   render_konspekty_modale, style_pomocy, audio_pomocy)
from karty_druk import ma_karty, style_kart

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLIKI = {"A": "Konspekty_3-4_lata.html", "B": "Konspekty_5_lat.html",
         "C": "Konspekty_6_lat.html",    "U": "Konspekty_uzupelnienia.html"}

# Wersje, które mają pomoce dydaktyczne — tylko ich media osadzamy w zeszycie.
# Wersje spoza słownika dostają pustą listę, czyli żadnych mediów pomocy.
WIEK_POMOCY = {"A": ["3–4 lata"], "B": ["5 lat"]}

# Modale konspektów pokazujemy statycznie, jeden pod drugim. Te same reguły
# stosuje bank przy druku (html.print-konspekt) — tutaj obowiązują na stałe.
CSS_DOK = """
@page{size:A4 portrait; margin:9mm}
body{background:var(--paper)}
.zeszyt{max-width:960px; margin:0 auto; padding:26px 18px 60px}
.kmodal{position:static; display:block; background:none; padding:0; overflow:visible; inset:auto}
.kcard{box-shadow:none; max-width:none; margin:0 0 30px; border:1px solid var(--line)}
.kclose,.kfoot,.kesc{display:none !important}
.kvar{display:flex !important; flex-direction:column}          /* wszystkie trzy poziomy wsparcia */
.zal-strefa{display:block !important}
.zal-akcje{display:none !important}
.kmodal + .kmodal{break-before:page; page-break-before:always}
.spis{display:flex; flex-wrap:wrap; gap:7px; margin:18px 0 6px}
.spis a{text-decoration:none; border:1px solid var(--line); border-radius:999px; padding:6px 13px;
  color:var(--ink); background:#FFF; font:700 11px/1 "DM Sans",Arial,sans-serif}
.spis a:hover{border-color:var(--accent); color:var(--accent)}
.spis a b{color:var(--violet); margin-right:5px}
.spis a:hover b{color:var(--accent)}
.spis a .ma{color:var(--accent); font-size:9px; vertical-align:2px; margin-left:5px}
.spis-legenda{font-size:12px; color:var(--muted); margin:2px 0 0}
.spis-legenda i{color:var(--accent); font-style:normal; font-size:9px; vertical-align:2px}
.wstep{max-width:62ch; color:var(--muted); font-size:13px; line-height:1.65; margin:10px 0 0}
@media print{
  .spis,.wstep,.dochead,.twotone{display:none !important}
  .zeszyt{max-width:none; padding:0}
  .kcard{border:none; margin:0}
  .au-btn{display:none !important}
}
"""

JS_DOK = """
/* Odtwarzanie polecenia z karty pomocy — jedna ścieżka naraz, druk wycisza. */
(function(){
  let biezacy=null;
  const swiec=(id,wl)=>document.querySelectorAll(`.au-btn[data-au="${id}"]`)
                              .forEach(b=>b.classList.toggle('gra',wl));
  function stop(){
    if(biezacy){biezacy.pause(); biezacy.currentTime=0; swiec(biezacy.id,false);}
    biezacy=null;
  }
  document.querySelectorAll('.au-btn').forEach(b=>b.addEventListener('click',()=>{
    const id=b.dataset.au;
    if(biezacy&&biezacy.id===id&&!biezacy.paused){stop(); return;}
    stop();
    const a=document.getElementById(id); if(!a) return;
    biezacy=a; swiec(id,true); a.currentTime=0; a.play().catch(()=>{});
    a.onended=()=>{swiec(id,false); biezacy=null;};
  }));
  window.addEventListener('beforeprint',stop);
  document.addEventListener('keydown',e=>{if(e.key==='Escape') stop();});
})();
"""


def dokument(mod):
    w = mod.WERSJA
    dzis = datetime.date.today().strftime("%d.%m.%Y")

    nry = {K["nr"] for (wk, _), K in KONSPEKTY.items() if wk == w["kod"]}
    spis, ile = [], 0
    for a in mod.AREAS:
        for it in a["items"]:
            K = KONSPEKTY.get((w["kod"], it["n"]))
            if not K:
                continue
            ile += 1
            # kropka w spisie: konspekt niesie materiał do wydruku. Bez niej
            # nauczyciel musi otwierać kolejne konspekty, żeby sprawdzić, gdzie
            # coś jest — a to była pierwsza rzecz, o którą pytano po dodaniu arkuszy.
            znak = ' <span class="ma" title="ma materiał do wydruku">●</span>' if ma_karty(K["nr"]) else ""
            spis.append(f'  <a href="#kon-{w["kod"]}-{it["n"]}">'
                        f'<b>{esc(K["nr"])}</b>{esc(K["tytul"])}{znak}</a>')

    z_materialem = sum(1 for (wk, _), K in KONSPEKTY.items()
                       if wk == w["kod"] and ma_karty(K["nr"]))
    zdanie_o_pomocach = (
        "W sekcji VII znajdziesz kartę pomocy dydaktycznej ze zdjęciem i poleceniem "
        "nagranym głosem nauczycielki, a przy części konspektów także arkusze "
        "do wydrukowania i wycięcia."
        if WIEK_POMOCY.get(w["kod"]) else
        "Konspekty z kropką w spisie mają w sekcji VII gotowy materiał do wydruku.")

    # W banku konspekt pokazuje jeden poziom — ten, który nauczyciel kliknął
    # w tabeli. Zeszyt pokazuje wszystkie trzy naraz, więc nagłówek o „klikniętym
    # poziomie" byłby tu mylący. Podmieniamy go na opis zgodny z tym, co widać.
    tresc = render_konspekty_modale(w["kod"]).replace(
        "Cel edukacyjny — z banku KC-1, wg klikniętego poziomu",
        "Cel edukacyjny — z banku KC-1 · trzy poziomy wsparcia")

    return f"""<title>Konspekty zajęć · {esc(w['etykieta'])}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" media="print" onload="this.media='all'"
      href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;700&display=swap">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;700&display=swap"></noscript>
<style>:root{{--logo:url({LOGO_URI})}}
{CSS}
{CSS_DOK}</style>
{style_pomocy(WIEK_POMOCY.get(w['kod'], []))}{audio_pomocy(WIEK_POMOCY.get(w['kod'], []))}{style_kart(nry)}

<div class="zeszyt">
<div class="dochead">
  <span class="mark" role="img" aria-label="Logo PCTP"></span>
  <div>
    <div class="wordmark">EduPlaner 2026</div>
    <div class="wordsub">Konspekty zajęć ·<br>{esc(w['etykieta'])}</div>
  </div>
  <div class="right">
    <span class="badge">Nauczyciel · zespół</span>
    <div class="badge-sub">Druk KC-3 · {dzis}</div>
  </div>
</div>
<div class="twotone"><i></i><i></i></div>

<p class="wstep">{ile} konspektów — komplet dla tej grupy wiekowej, w kolejności obszarów.
Każdy pokazuje wszystkie trzy poziomy wsparcia naraz. {zdanie_o_pomocach}
Przy druku każdy konspekt zaczyna nową stronę A4.</p>

<nav class="spis" aria-label="Spis konspektów">
{chr(10).join(spis)}
</nav>
<p class="spis-legenda"><i>●</i> — konspekt ma w sekcji VII gotowy materiał do wydruku
({z_materialem} z {ile}).</p>

{tresc}

<div class="docfoot">
  <span>EduPlaner 2026 · Konspekty zajęć · {esc(w['etykieta'])}</span>
  <span class="mono">PCTP Koszalin · druk KC-3</span>
</div>
</div>
<script>{JS_DOK}</script>
"""


if __name__ == "__main__":
    for mod in WERSJE:
        kod = mod.WERSJA["kod"]
        if kod not in PLIKI:
            continue
        sciezka = os.path.join(KORZEN, PLIKI[kod])
        open(sciezka, "w", encoding="utf-8").write(dokument(mod))
        print(f"zapisano: {PLIKI[kod]} · {os.path.getsize(sciezka)/1024/1024:.2f} MB")
