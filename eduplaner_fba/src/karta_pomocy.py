# -*- coding: utf-8 -*-
"""Karta pomocy dydaktycznej w sekcji VII konspektu — wzór druku KC-4.

Nauczyciel szuka pomocy w konspekcie, pod przyciskiem „Pokaż pomoc i posłuchaj
polecenia" — i tam ma ją znaleźć. Karta niesie ilustrację poglądową gotowej
pomocy, listę „co przygotować", trzy kroki użycia, wskazówkę i **polecenie dla
dziecka nagrane jej własnym głosem**.

Media wchodzą jako `data:` URI, więc dokument zostaje jednym plikiem, który
działa u nauczycielki bez internetu. Ilustracja jest wspólna dla trzech wersji
wiekowych (jedna pomoc = jedno zdjęcie), nagranie jest osobne dla każdego wieku.

**Brak nie psuje budowania.** Karta bez ilustracji dostaje pole zastępcze,
a karta bez nagrania traci przycisk odtwarzania — dokument składa się dalej
i wygląda dobrze. Właśnie dlatego kompletność sprawdza `sprawdz_pomoce.py`,
a nie oglądanie dokumentu.
"""

import base64
import html
from pathlib import Path

import pomoce_fba as PF

KOR = Path(__file__).resolve().parent.parent
OBRAZY = KOR / "assets" / "pomoce_fba"
AUDIO = KOR / "assets" / "audio_fba"


def _e(t):
    return html.escape(str(t), quote=False)


def obraz(nr):
    p = OBRAZY / f"k_{PF.kod(nr)}.jpg"
    if not p.exists():
        return ""
    return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()


def dzwiek(nr, wersja):
    p = AUDIO / f"{wersja.lower()}{PF.kod(nr)}.mp3"
    if not p.exists():
        return ""
    return "data:audio/mpeg;base64," + base64.b64encode(p.read_bytes()).decode()


def braki():
    """(bez ilustracji, bez nagrania) — do kontroli kompletności."""
    import konspekty_fba as KF
    bez_obrazu = sorted({nr for nr, _w in KF.klucze() if not obraz(nr)})
    bez_audio = [(nr, w) for nr, w in KF.klucze() if not dzwiek(nr, w)]
    return bez_obrazu, bez_audio


STYL = """
/* Karta pomocy — druk KC-4 w sekcji VII konspektu. */
.pom{border:1px solid var(--line); border-radius:12px; overflow:hidden; margin-top:10px}
.pom-head{display:flex; align-items:center; gap:11px; background:var(--soft); padding:9px 13px;
  border-bottom:1px solid var(--line)}
.pom-head .kp{background:var(--accent); color:var(--on-accent); border-radius:999px; padding:4px 12px;
  font:700 8.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase}
.pom-head h5{margin:0; font-size:14px; color:var(--ink)}
.pom-head .wiek{margin-left:auto; font-size:9px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--szary)}
.pom-ciało{display:grid; grid-template-columns:1.15fr 1fr; gap:0}
.pom-foto{background:var(--soft); background-size:cover; background-position:center; min-height:210px}
.pom-foto.brak{display:grid; place-items:center; color:var(--szary); font-size:10px;
  letter-spacing:.08em; text-transform:uppercase; text-align:center; padding:0 18px}
.pom-tresc{padding:11px 14px 13px}
.pom-tresc h6{margin:0 0 4px; font-size:9px; letter-spacing:.11em; text-transform:uppercase;
  color:var(--accent)}
.pom-tresc ul,.pom-tresc ol{margin:0 0 9px; padding-left:17px; font-size:10px; line-height:1.45}
.pom-tresc ol{counter-reset:krok}
.pom-glos{display:flex; align-items:center; gap:11px; background:var(--field); border-radius:9px;
  padding:9px 12px; margin-top:2px}
.pom-glos .tekst{font-size:11px; line-height:1.45; color:var(--ink)}
.pom-glos .tekst b{display:block; font-size:8.5px; letter-spacing:.1em; text-transform:uppercase;
  color:var(--szary); margin-bottom:2px}
.pom-play{flex:0 0 auto; border:1px solid var(--accent); background:var(--accent);
  color:var(--on-accent); border-radius:999px; width:38px; height:38px; cursor:pointer;
  font-size:13px; line-height:1}
.pom-play:disabled{background:var(--paper); color:var(--szary); border-color:var(--line); cursor:default}
.pom-wsk{border-top:1px dashed var(--line); padding:8px 14px 10px; font-size:10px; line-height:1.45;
  color:var(--szary)}
.pom-wsk b{color:var(--ink)}
@media print{
  .pom{break-inside:avoid}
  .pom-play{display:none}
}
"""

SKRYPT = """
/* Odtwarzanie polecenia jej głosem. Jedno nagranie naraz: dwa naraz w sali
   przedszkolnej to hałas, którego dziecko nie rozdzieli. */
(function(){
  let gra = null;
  document.addEventListener('click', e => {
    const b = e.target.closest('.pom-play');
    if (!b || !b.dataset.src) return;
    if (gra) { gra.pause(); gra.currentTime = 0; }
    if (b.dataset.gra === '1') { b.dataset.gra = ''; b.textContent = '▶'; gra = null; return; }
    document.querySelectorAll('.pom-play').forEach(x => { x.dataset.gra = ''; x.textContent = '▶'; });
    gra = new Audio(b.dataset.src);
    b.dataset.gra = '1'; b.textContent = '■';
    gra.onended = () => { b.dataset.gra = ''; b.textContent = '▶'; gra = null; };
    gra.play();
  });
})();
"""


def karta(nr, wersja, wiek):
    """Karta pomocy do konspektu (wskaźnik `nr`, wersja wiekowa `wersja`)."""
    nazwa, przygotuj, kroki, wskazowka, _opis = PF.POMOCE[nr]
    src = obraz(nr)
    foto = (f'<div class="pom-foto" style="background-image:url({src})" role="img"'
            f' aria-label="Pomoc dydaktyczna: {_e(nazwa)}"></div>' if src else
            '<div class="pom-foto brak">zdjęcie poglądowe<br>jeszcze nie powstało</div>')
    mp3 = dzwiek(nr, wersja)
    polecenie = PF.POLECENIA[(nr, wersja)]
    przycisk = (f'<button type="button" class="pom-play" data-src="{mp3}"'
                f' aria-label="Posłuchaj polecenia jej głosem">▶</button>' if mp3 else
                '<button type="button" class="pom-play" disabled'
                ' title="Nagranie jeszcze nie powstało">▶</button>')
    return f'''    <section class="pom">
      <div class="pom-head"><span class="kp">Pomoc dydaktyczna · druk KC-4</span>
        <h5>{_e(nazwa)}</h5><span class="wiek">{_e(wiek)}</span></div>
      <div class="pom-ciało">
        {foto}
        <div class="pom-tresc">
          <h6>Co przygotować</h6>
          <ul>{"".join(f"<li>{_e(x)}</li>" for x in przygotuj)}</ul>
          <h6>Jak użyć — trzy kroki</h6>
          <ol>{"".join(f"<li>{_e(x)}</li>" for x in kroki)}</ol>
          <div class="pom-glos">
            {przycisk}
            <span class="tekst"><b>Polecenie dla dziecka · jej głosem</b>„{_e(polecenie)}”</span>
          </div>
        </div>
      </div>
      <div class="pom-wsk"><b>Wskazówka:</b> {_e(wskazowka)}</div>
    </section>'''
