# -*- coding: utf-8 -*-
"""Pomoce dydaktyczne — osobny dokument na każdą grupę wiekową.

Dlaczego osobno: karty pomocy niosą zdjęcie i nagranie, więc to one ważą.
Wszystkie w jednym pliku z bankiem celów dawały dokument, który długo się
otwiera i ledwo mieści się w limitach wysyłki. Rozdzielone: bank jest lekki
i chodzi płynnie, a nauczyciel bierze tylko ten zeszyt pomocy, który dotyczy
jego grupy — i tak drukuje karty osobno (druk KC-4).

Każdy dokument jest samowystarczalny: zdjęcia i nagrania siedzą w środku,
więc działa bez internetu i bez folderu z plikami obok.

Uruchomienie: python3 src/build_pomoce.py
"""

import datetime
import importlib
import os

from build import CSS, LOGO_URI, esc          # ten sam arkusz stylów co bank
import pomoce_a                               # noqa: F401 — rejestruje zestaw 3–4 lata
import pomoce_b                               # noqa: F401 — rejestruje zestaw 5 lat
from pomoce_karta import ZESTAWY

KORZEN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Zestaw → (nazwa pliku, moduły konspektów, z których bierzemy obszar i temat)
DOKUMENTY = {
    "3–4 lata": ("Pomoce_dydaktyczne_3-4_lata.html", "konspekty_34_d%d"),
    "5 lat":    ("Pomoce_dydaktyczne_5_lat.html",    "konspekty_5_d%d"),
}

# Karta jest portretowa (A4 pionowo) — bank drukuje się poziomo, więc
# nadpisujemy to tutaj, po wspólnym arkuszu stylów.
CSS_DOK = """
@page{size:A4 portrait; margin:10mm}
body{background:var(--paper)}
.zeszyt{max-width:920px; margin:0 auto; padding:26px 18px 60px}
.zal{margin-top:26px}
.obszar-tyt{margin:34px 0 0; font:700 13px/1.3 "DM Sans",Arial,sans-serif;
  letter-spacing:.14em; text-transform:uppercase; color:var(--violet)}
.spis{display:flex; flex-wrap:wrap; gap:7px; margin:18px 0 6px}
.spis a{text-decoration:none; border:1px solid var(--line); border-radius:999px;
  padding:6px 13px; color:var(--ink); background:#FFF;
  font:700 11px/1 "DM Sans",Arial,sans-serif}
.spis a:hover{border-color:var(--accent); color:var(--accent)}
.wstep{max-width:60ch; color:var(--muted); font-size:13px; line-height:1.65; margin:10px 0 0}
@media print{
  .spis,.wstep,.dochead,.twotone,.obszar-tyt{display:none !important}
  .zeszyt{max-width:none; padding:0}
  .zal{margin-top:0; border:none; border-radius:0; padding:0}
}
"""

JS_DOK = """
/* Odtwarzanie polecenia — jedna ścieżka naraz, druk wycisza. */
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


def obszary_konspektow(wzor):
    """nr konspektu → nazwa obszaru, wzięta wprost z pola `sfera` konspektu."""
    mapa = {}
    for i in range(1, 10):
        modul = importlib.import_module(wzor % i)
        for klucz, wartosc in vars(modul).items():
            if not (klucz.startswith("KONSPEKTY") and isinstance(wartosc, dict)):
                continue
            for kon in wartosc.values():
                mapa[kon["nr"]] = kon["sfera"].split("·")[0].strip()
    return mapa


def dokument(zestaw, wzor_konspektow):
    dzis = datetime.date.today().strftime("%d.%m.%Y")
    obszary = obszary_konspektow(wzor_konspektow)

    # Karty w kolejności numerów konspektów, pogrupowane obszarami.
    kody = sorted(zestaw.pomoce, key=lambda k: zestaw.pomoce[k][0])
    czesci, spis, poprzedni = [], [], None
    for kod in kody:
        nr, tytul = zestaw.pomoce[kod][0], zestaw.pomoce[kod][1]
        obszar = obszary.get(nr, "")
        if obszar != poprzedni:
            kotwica = "o" + obszar.split()[0] if obszar else "o"
            czesci.append(f'<h2 class="obszar-tyt" id="{kotwica}">{esc(obszar)}</h2>')
            spis.append(f'<a href="#{kotwica}">{esc(obszar)}</a>')
            poprzedni = obszar
        czesci.append(zestaw.karta(kod, esc))

    return f"""<title>Pomoce dydaktyczne · {esc(zestaw.wiek)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" media="print" onload="this.media='all'"
      href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;700&display=swap">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=JetBrains+Mono:wght@400;700&display=swap"></noscript>
<style>:root{{--logo:url({LOGO_URI})}}
{CSS}
{CSS_DOK}</style>
<style>{zestaw.style()}</style>
{zestaw.audio_tagi()}

<div class="zeszyt">
<div class="dochead">
  <span class="mark" role="img" aria-label="Logo PCTP"></span>
  <div>
    <div class="wordmark">EduPlaner 2026</div>
    <div class="wordsub">Pomoce dydaktyczne ·<br>{esc(zestaw.wiek)}</div>
  </div>
  <div class="right">
    <span class="badge">Nauczyciel · zespół</span>
    <div class="badge-sub">Druk KC-4 · {dzis}</div>
  </div>
</div>
<div class="twotone"><i></i><i></i></div>

<p class="wstep">{len(kody)} kart — po jednej do każdego konspektu dla tej grupy wiekowej.
Każda pokazuje, jak pomoc ma wyglądać, co przygotować i jak jej użyć w trzech krokach.
Przycisk „Posłuchaj polecenia” odtwarza zdanie nagrane głosem nauczycielki; przy druku
przycisk znika, a każda karta wychodzi na osobnej stronie A4.</p>

<nav class="spis" aria-label="Skocz do obszaru">
{chr(10).join('  ' + s for s in spis)}
</nav>

{chr(10).join(czesci)}

<div class="docfoot">
  <span>EduPlaner 2026 · Pomoce dydaktyczne · {esc(zestaw.wiek)}</span>
  <span class="mono">PCTP Koszalin · druk KC-4</span>
</div>
</div>
<script>{JS_DOK}</script>
"""


if __name__ == "__main__":
    for zestaw in ZESTAWY:
        if zestaw.wiek not in DOKUMENTY or not zestaw.pomoce:
            continue
        nazwa, wzor = DOKUMENTY[zestaw.wiek]
        sciezka = os.path.join(KORZEN, nazwa)
        open(sciezka, "w", encoding="utf-8").write(dokument(zestaw, wzor))
        print(f"zapisano: {nazwa} · {len(zestaw.pomoce)} kart · "
              f"{os.path.getsize(sciezka)/1024/1024:.2f} MB")
