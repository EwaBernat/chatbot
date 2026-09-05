# -*- coding: utf-8 -*-
"""Renderowanie konspektu zajęć do tabeli FBA-T — wzór druku KC-3 z banku KPOF.

Ten sam układ, co konspekty w banku celów SMART: nagłówek z metryką dziecka,
sekcje I–VII, tabela przebiegu w parach „czynność nauczyciela (N) / oczekiwana
reakcja dziecka (D)", trzy modyfikacje w kolorach oceny i materiał do wydruku.
Nauczyciel czyta konspekty seriami, więc identyczna kolejność sekcji jest tu
ważniejsza niż pomysłowość układu — oko wie, gdzie szukać przebiegu.

Treść wszystkich 75 konspektów leży w `konspekty_fba*.py`; ten moduł tylko ją
składa. Konspekt otwiera się kliknięciem celu w tabeli, a **cel edukacyjny
czyta się na żywo z klikniętej komórki** — po poprawce w `dane_poziomy.py`
konspekt nie zaczyna żyć własną wersją celu.

Materiał do wydruku jest w rodzaju `pola` — ramki z etykietami, bez rysunków.
To nie jest brak: symbol do tych kart **bierze się z biblioteki EduPlaner**,
żeby dziecko widziało ten sam obrazek tu, na tablicy AAC i w planie dnia.
Symbol dorysowany pod jeden konspekt przestaje być słowem.
"""

import base64
import html

import karta_pomocy as KP
import symbole_fba as SF
import konspekty_fba as KF


def _e(t):
    return html.escape(str(t), quote=False)


STYL = """
/* Konspekt w układzie druku KC-3 z banku — te same nazwy klas, żeby oba
   dokumenty wyglądały jak jeden komplet. */
.kmodal{position:fixed; inset:0; background:rgba(30,20,60,.55); z-index:60;
  overflow:auto; padding:28px 16px; display:none}
.kmodal.open{display:block}
.kcard{max-width:860px; margin:0 auto; background:var(--paper); border-radius:14px;
  padding:24px 28px 26px; position:relative; box-shadow:0 8px 40px rgba(30,20,60,.3)}
.kclose{position:absolute; top:14px; right:16px; border:1px solid var(--line-2);
  background:var(--paper); color:var(--ink); border-radius:8px; width:30px; height:30px; cursor:pointer}
.khead{display:flex; align-items:flex-start; gap:12px; border-bottom:2px solid var(--line-2);
  padding:0 40px 11px 0}   /* miejsce na krzyżyk zamykający — pigułka na niego wchodziła */
.khead .kw{font-size:14px; font-weight:700; color:var(--ink)}
.khead .ks{font-size:9.5px; letter-spacing:.13em; text-transform:uppercase; color:var(--szary); margin-top:3px}
.kpill{margin-left:auto; background:var(--ink); color:#fff; border-radius:999px; padding:6px 14px;
  font:700 10px/1 "DM Sans",Arial,sans-serif; letter-spacing:.08em; white-space:nowrap}
.kmeta{display:grid; grid-template-columns:repeat(4,1fr); gap:10px; margin:12px 0 0}
.kmeta .field{border-bottom:1px solid var(--line-2); padding:3px 2px 5px; font-size:10px}
.kmeta .field b{display:block; font-size:8.5px; letter-spacing:.12em; text-transform:uppercase;
  color:var(--szary); margin-bottom:2px}
.kmeta .field .val{font-size:11.5px; color:var(--ink); font-weight:600}
.kmeta .dots{display:block; border-bottom:1px dotted var(--line-2); height:13px}
.klvl{display:inline-block; border-radius:5px; padding:2px 9px; font:700 11px/1.5 "DM Sans",Arial,sans-serif}
.klvl.p3{background:var(--t3); color:var(--p3)} .klvl.p2{background:var(--t2); color:var(--p2)}
.klvl.p1{background:var(--t1); color:var(--p1)}
/* Blok tytułowy wyśrodkowany: pigułka druku, sfera, tytuł i podtytuł stoją
   w osi kartki. Sam tytuł wyśrodkowany przy pozostałych wyrównanych do lewej
   wyglądał na przesunięty przez pomyłkę. */
.ktitle{margin:14px 0 12px; text-align:center}
.ktitle .kp{display:inline-block; background:var(--accent); color:var(--on-accent); border-radius:999px;
  padding:5px 14px; font:700 9.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase}
.ktitle .ksfera{font-size:9.5px; letter-spacing:.1em; text-transform:uppercase; color:var(--szary); margin:8px 0 3px}
.ktitle h3{margin:0; font-size:19px; color:var(--ink)}
.ktitle .kpod{font-size:11.5px; color:var(--szary); margin-top:2px}
.ksec{display:flex; align-items:center; gap:9px; margin:14px 0 7px}
.ksec .sq{background:var(--accent); color:var(--on-accent); width:22px; height:22px; border-radius:4px;
  display:grid; place-items:center; font:700 10px/1 "DM Sans",Arial,sans-serif}
.ksec h4{margin:0; font-size:12px; color:var(--ink); letter-spacing:.06em; text-transform:uppercase}
.ksec .line{flex:1 1 auto; height:1px; background:var(--line)}
.kcele{display:grid; grid-template-columns:1fr 1fr; gap:11px}
.kcel{border:1px solid var(--line); border-radius:10px; padding:10px 12px}
.kcel.ter{border-left:4px solid var(--accent)}
.kchead{font-size:8.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--szary); margin-bottom:5px}
.ktresc{font-size:11.5px; line-height:1.5; color:var(--tekst)}
.ksmart{list-style:none; margin:7px 0 0; padding:0; display:grid; gap:3px}
.ksmart li{display:flex; gap:7px; font-size:9.5px; line-height:1.4}
.ksmart li b{flex:0 0 auto; width:15px; color:var(--accent)}
.kkryt{margin-top:6px; font-size:9.5px; color:var(--szary); border-top:1px dashed var(--line); padding-top:5px}
.kvar{display:none} .kvar.on{display:block}
.kvlvl{display:inline-block; font:700 8.5px/1 "DM Sans",Arial,sans-serif; letter-spacing:.1em;
  text-transform:uppercase; border-radius:4px; padding:3px 7px; margin-bottom:4px}
.kvlvl.p3{background:var(--t3); color:var(--p3)} .kvlvl.p2{background:var(--t2); color:var(--p2)}
.kvlvl.p1{background:var(--t1); color:var(--p1)}
.kcel.edu.jeden .kvlvl{display:none}
/* Konspekt otwarty bez wyboru poziomu (wydruk zeszytu, wykaz) pokazuje wszystkie
   trzy cele zamiast pustej ramki — tak samo jak konspekty w banku. */
.kcel.edu:not(:has(.kvar.on)) .kvar{display:block}
.kcel.edu:not(:has(.kvar.on)) .kvar + .kvar{border-top:1px dashed var(--line);
  margin-top:6px; padding-top:6px}
.kdwie{display:grid; grid-template-columns:1fr 1fr; gap:11px}
.klista{margin:0; padding-left:17px; font-size:10.5px; line-height:1.5}
.krodzaj{font-size:11px; color:var(--ink)}
.kkurs{font-size:10px; color:var(--szary); font-style:italic; margin:6px 0 5px}
table.ktab{width:100%; border-collapse:collapse; font-size:10.5px; table-layout:fixed}
table.ktab th{background:var(--field); font-size:8.5px; padding:6px 8px}
table.ktab td{padding:6px 8px; border:1px solid var(--line); vertical-align:top; line-height:1.4}
table.ktab td.lp{text-align:center; font-weight:700; color:var(--ink); width:26px}
.kmods{display:grid; grid-template-columns:repeat(3,1fr); gap:9px}
.kmod{border:1px solid var(--line); border-radius:9px; padding:8px 10px; font-size:10px}
.kmod b{display:block; font-size:9px; letter-spacing:.08em; text-transform:uppercase; margin-bottom:4px}
.kmod.m3{background:var(--t3); border-color:var(--r3)} .kmod.m3 b{color:var(--p3)}
.kmod.m2{background:var(--t2); border-color:var(--r2)} .kmod.m2 b{color:var(--p2)}
.kmod.m1{background:var(--t1); border-color:var(--r1)} .kmod.m1 b{color:var(--p1)}
.kmod.wyb{box-shadow:0 0 0 2px var(--ink) inset}
.kwsk{margin-top:12px; background:var(--soft); border-left:4px solid var(--violet);
  border-radius:0 8px 8px 0; padding:9px 13px; font-size:10.5px; line-height:1.5}
.kfoot{display:flex; gap:9px; margin-top:16px; flex-wrap:wrap}
.chipbtn{border:1px solid var(--line-2); background:var(--paper); color:var(--ink); border-radius:999px;
  padding:8px 16px; font:600 11px/1 "DM Sans",Arial,sans-serif; cursor:pointer}
.chipbtn.mocny{background:var(--ink); color:#fff; border-color:var(--ink)}
.kesc{font-size:9px; color:var(--szary); margin:7px 0 0}
.kspis-info{display:flex; align-items:center; gap:12px; margin:0 0 11px; font-size:10px;
  color:var(--szary); line-height:1.45}
.kspis-info .chipbtn{flex:0 0 auto}

/* arkusz do wydruku — rodzaj „pola”: ramki z etykietami, symbol z biblioteki */
.zal{border-top:2px dashed var(--line-2); margin-top:16px; padding-top:14px}
.zal-head{display:flex; align-items:center; gap:10px; margin-bottom:9px}
.zal-head .kp{background:var(--accent); color:var(--on-accent); border-radius:999px; padding:4px 12px;
  font:700 9px/1 "DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase}
.zal h4{margin:0; font-size:14px; color:var(--ink)}
.zal-wstep{font-size:10.5px; color:var(--szary); line-height:1.5; margin:0 0 11px}
.zal-siatka{display:grid; grid-template-columns:1fr 1fr; gap:11px}
.zal-karta{border:2px dashed var(--line-2); border-radius:10px; padding:11px 12px 13px; text-align:center}
.zal-karta .pole{height:118px; border:1px solid var(--line); border-radius:8px; background-color:var(--soft);
  display:grid; place-items:center; color:var(--szary); font-size:9px; letter-spacing:.08em;
  text-transform:uppercase; padding:0 10px; margin-bottom:8px}
/* Pole z symbolem z biblioteki: obrazek w całości, nie przycięty — dziecko ma
   rozpoznać ten sam znak, co na tablicy AAC. */
.pole.ma{background-color:var(--paper); background-repeat:no-repeat;
  background-position:center; background-size:contain; border-color:var(--line-2)}
.zal-karta b{display:block; font-size:15px; color:var(--ink); letter-spacing:.04em}
.zal-karta span{font-size:9px; color:var(--szary)}
.zal-pasek{display:grid; grid-template-columns:repeat(3,1fr); gap:9px; margin-top:11px}
.zal-pasek div{border:2px dashed var(--line-2); border-radius:10px; padding:9px; text-align:center}
.zal-pasek .pole{height:74px; border:1px solid var(--line); border-radius:8px; background-color:var(--soft);
  margin-bottom:6px; font-size:0}
.zal-pasek .pole.ma{background-color:var(--paper); background-repeat:no-repeat;
  background-position:center; background-size:contain}
.zal-pasek b{font-size:11px; color:var(--ink)}
"""

SKRYPT = """
/* Konspekty otwierają się z komórki celu — tak jak w banku KPOF. Cel edukacyjny
   czytamy z tabeli na żywo: poprawka w danych nie zostawia w konspekcie
   nieaktualnej kopii celu. */
(function(){
  const POZ = {p3:'Poziom III', p2:'Poziom II', p1:'Poziom I'};
  const otwarty = () => document.querySelector('.kmodal.open');

  /* Cele edukacyjne wpisujemy do wszystkich konspektów raz, przy starcie —
     dzięki temu wydruk całego zeszytu też je ma, a treść i tak pochodzi
     z tabeli, nie z kopii w konspekcie. */
  const KOL = {p3:0, p2:1, p1:2};
  function wypelnij(){
    for (const m of document.querySelectorAll('.kmodal')) {
      const kom = document.querySelectorAll(
        '#w-' + m.dataset.wersja + ' tr[data-wsk="' + m.dataset.wsk + '"] td.g');
      for (const v of m.querySelectorAll('.kvar')) {
        const c = kom[KOL[v.dataset.lvl]];
        if (!c) continue;
        v.querySelector('.kon-cel').textContent = c.querySelector('.tresc').textContent;
        v.querySelector('.kon-kryt').textContent = c.querySelector('.ram').textContent;
      }
    }
  }
  wypelnij();

  function pokaz(kid, lvl, wersja, wsk){
    const m = document.getElementById(kid);
    if (!m) return;
    m.querySelectorAll('.kvar').forEach(v => v.classList.toggle('on', v.dataset.lvl === lvl));
    m.querySelector('.kcel.edu').classList.add('jeden');
    const b = m.querySelector('.kon-poz');
    b.textContent = POZ[lvl]; b.className = 'klvl kon-poz ' + lvl;
    m.querySelectorAll('.kmod').forEach(x => x.classList.toggle('wyb', x.dataset.mod === lvl));
    zamknij();                       // dwa otwarte konspekty = dwa wydruki
    m.classList.add('open');
    document.body.style.overflow = 'hidden';
    m.querySelector('.kclose').focus();
  }
  /* Ze spisu konspekt otwiera się bez wybranego poziomu: nauczyciel nie kliknął
     żadnej komórki, więc pokazujemy wszystkie trzy cele i wszystkie modyfikacje. */
  function pokazBezPoziomu(kid){
    const m = document.getElementById(kid);
    if (!m) return;
    m.querySelectorAll('.kvar').forEach(v => v.classList.remove('on'));
    m.querySelector('.kcel.edu').classList.remove('jeden');
    const b = m.querySelector('.kon-poz');
    b.textContent = 'wszystkie trzy'; b.className = 'klvl kon-poz p2';
    m.querySelectorAll('.kmod').forEach(x => x.classList.remove('wyb'));
    zamknij();
    m.classList.add('open');
    document.body.style.overflow = 'hidden';
    m.querySelector('.kclose').focus();
  }

  function zamknij(){
    document.querySelectorAll('.kmodal.open').forEach(m => m.classList.remove('open'));
    document.body.style.overflow = '';
  }

  /* Faza przechwytywania: komórka ma własny nasłuch, a delegacja na dokumencie
     w fazie bąbelkowania odpalałaby się już po nim. */
  document.addEventListener('click', e => {
    const sp = e.target.closest('[data-spis]');
    if (sp) { e.preventDefault(); pokazBezPoziomu(sp.dataset.spis); return; }
    const td = e.target.closest('td.g[data-kon]');
    if (td) { e.preventDefault();
      pokaz(td.dataset.kon, td.dataset.lvl, td.dataset.wersja, td.dataset.wsk); return; }
    if (e.target.closest('[data-zamknij]') || e.target.classList.contains('kmodal')) zamknij();
  }, true);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && otwarty()) { zamknij(); return; }
    const td = e.target.closest && e.target.closest('td.g[data-kon]');
    if (td && (e.key === 'Enter' || e.key === ' ')) {
      e.preventDefault(); pokaz(td.dataset.kon, td.dataset.lvl, td.dataset.wersja, td.dataset.wsk);
    }
  });
  /* Wydruk całego zeszytu wersji: 25 konspektów, każdy na własnej kartce.
     Otwarty pojedynczy konspekt zamykamy, żeby nie wyszedł dwa razy. */
  document.addEventListener('click', e => {
    const z = e.target.closest('[data-zeszyt]');
    if (!z) return;
    zamknij();
    document.querySelectorAll('.kmodal[data-wersja="' + z.dataset.zeszyt + '"]').forEach(m => {
      m.querySelectorAll('.kvar').forEach(v => v.classList.remove('on'));
      m.querySelector('.kcel.edu').classList.remove('jeden');
      m.querySelectorAll('.kmod').forEach(x => x.classList.remove('wyb'));
      const b = m.querySelector('.kon-poz'); b.textContent = 'wszystkie trzy';
      b.className = 'klvl kon-poz p2';
    });
    document.documentElement.dataset.zeszyt = z.dataset.zeszyt;
    document.documentElement.classList.add('print-zeszyt');
    const gotowe = () => { document.documentElement.classList.remove('print-zeszyt');
      delete document.documentElement.dataset.zeszyt;
      window.removeEventListener('afterprint', gotowe); };
    window.addEventListener('afterprint', gotowe);
    window.print();
  });
  document.addEventListener('click', e => {
    if (!e.target.closest('[data-druk]')) return;
    document.documentElement.classList.add('print-konspekt');
    const gotowe = () => { document.documentElement.classList.remove('print-konspekt');
      window.removeEventListener('afterprint', gotowe); };
    window.addEventListener('afterprint', gotowe);
    window.print();
  });
})();
"""


def _obraz_symbolu(kod):
    """Pole karty: klasa symbolu albo prośba o wklejenie własnego.

    Obraz osadzamy raz, w arkuszu stylów (`style_symboli`), a nie w każdym
    polu z osobna: ten sam symbol wraca na kartach kilkunastu konspektów,
    a przy 525 polach dokument urósłby z 5 do 18 MB.
    """
    if not SF.plik(kod):
        return '<div class="pole">miejsce na symbol<br>z biblioteki EduPlaner</div>'
    return f'<div class="pole ma sym-{kod}" role="img" aria-label="Symbol"></div>'


def style_symboli():
    """Każdy użyty symbol osadzony dokładnie raz, jako klasa CSS."""
    kody = sorted({k for lista in list(SF.KARTY.values()) + list(SF.PASKI.values())
                   for k in lista if SF.plik(k)})
    regu = []
    for k in kody:
        dane = base64.b64encode(SF.plik(k).read_bytes()).decode()
        regu.append(f".sym-{k}{{background-image:url(data:image/jpeg;base64,{dane})}}")
    return "\n".join(regu)


def _arkusz(a, nr):
    kody = SF.KARTY.get(nr, [None] * 4)
    kodyp = SF.PASKI.get(nr, [None] * 3)
    karty = "".join(
        f'<div class="zal-karta">{_obraz_symbolu(kody[i] if i < len(kody) else None)}'
        f'<b>{_e(t)}</b><span>{_e(o)}</span></div>' for i, (t, o) in enumerate(a["karty"]))
    pasek = "".join(
        f'<div>{_obraz_symbolu(kodyp[i] if i < len(kodyp) else None)}<b>{_e(x)}</b></div>'
        for i, x in enumerate(a["pasek"]))
    return f'''    <section class="zal">
      <div class="zal-head"><span class="kp">Materiał do wydruku · A4</span><h4>{_e(a["tytul"])}</h4></div>
      <p class="zal-wstep">{_e(a["wstep"])}</p>
      <div class="zal-siatka">{karty}</div>
      <div class="zal-pasek">{pasek}</div>
    </section>'''


def modal(K):
    """Jeden konspekt — słownik z `konspekty_fba.konspekt()`."""
    ter = "".join(f'<li><b>{L}</b><span>{_e(t)}</span></li>' for L, t in K["ter_smart"])
    pom = "".join(f'<li>{_e(x)}</li>' for x in K["pomoce"])
    met = "".join(f'<li>{_e(x)}</li>' for x in K["metody"])
    prz = "".join(f'<tr><td class="lp">{i}</td><td>{_e(n)}</td><td>{_e(d)}</td></tr>'
                  for i, (n, d) in enumerate(K["przebieg"], 1))
    mods = ""
    for kod, klasa, etykieta in (("p3", "m3", "Poziom III · Czerwona"),
                                 ("p2", "m2", "Poziom II · Żółta"),
                                 ("p1", "m1", "Poziom I · Zielona")):
        li = "".join(f'<li>{_e(x)}</li>' for x in K["mody"][kod])
        mods += (f'<div class="kmod {klasa}" data-mod="{kod}"><b>{etykieta}</b>'
                 f'<ul class="klista">{li}</ul></div>')
    return f'''<div class="kmodal" id="{K["kid"]}" data-wersja="{K["wersja"]}" data-wsk="{K["nr"]}" role="dialog" aria-modal="true"
  aria-label="Konspekt zajęć: {_e(K["tytul"])}">
  <div class="kcard">
    <button class="kclose" data-zamknij aria-label="Zamknij konspekt" title="Zamknij (Esc)">✕</button>
    <div class="khead">
      <span class="mark" role="img" aria-label="Logo PCTP"></span>
      <div>
        <div class="kw">EduPlaner 2026</div>
        <div class="ks">Konspekt · funkcja {_e(K["funkcja"])} · wersja {K["wersja"]} · {_e(K["wiek"])}
          · wskaźnik {K["nr"]}</div>
      </div>
      <span class="kpill">Konspekt FBA {K["wersja"]}-{K["nr"]}</span>
    </div>
    <div class="kmeta" style="grid-template-columns:1.6fr 1fr 1fr">
      <div class="field"><b>Dotyczy dziecka</b><span class="dots"></span></div>
      <div class="field"><b>Grupa</b><span class="dots"></span></div>
      <div class="field"><b>Data</b><span class="dots"></span></div>
    </div>
    <div class="ktitle">
      <span class="kp">Konspekt zajęć · druk KC-3</span>
      <div class="ksfera">{_e(K["sfera"])}</div>
      <h3>{_e(K["tytul"])}</h3>
      <div class="kpod">{_e(K["podtytul"])}</div>
    </div>
    <div class="kmeta">
      <div class="field"><b>Czas</b><span class="val">{_e(K["czas"])}</span></div>
      <div class="field"><b>Forma</b><span class="val">{_e(K["forma"])}</span></div>
      <div class="field"><b>Cykl</b><span class="val">{_e(K["cykl"])}</span></div>
      <div class="field"><b>Poziom wsparcia</b><span class="klvl p2 kon-poz">wszystkie trzy</span></div>
    </div>

    <div class="ksec"><span class="sq">I</span><h4>Cel SMART</h4><span class="line"></span></div>
    <div class="kcele">
      <div class="kcel edu">
        <div class="kchead">Cel edukacyjny — z tabeli FBA-T, wg klikniętego poziomu</div>
        <div class="kvar" data-lvl="p3"><span class="kvlvl p3">Poziom III</span>
          <div class="ktresc kon-cel"></div>
          <div class="kkryt"><b>Kryterium:</b> <span class="kon-kryt"></span></div></div>
        <div class="kvar" data-lvl="p2"><span class="kvlvl p2">Poziom II</span>
          <div class="ktresc kon-cel"></div>
          <div class="kkryt"><b>Kryterium:</b> <span class="kon-kryt"></span></div></div>
        <div class="kvar" data-lvl="p1"><span class="kvlvl p1">Poziom I</span>
          <div class="ktresc kon-cel"></div>
          <div class="kkryt"><b>Kryterium:</b> <span class="kon-kryt"></span></div></div>
      </div>
      <div class="kcel ter">
        <div class="kchead">Cel terapeutyczny</div>
        <div class="ktresc">{_e(K["ter"])}</div>
        <ul class="ksmart">{ter}</ul>
        <div class="kkryt"><b>Kryterium:</b> {_e(K["ter_kryt"])}</div>
      </div>
    </div>

    <div class="kdwie">
      <div>
        <div class="ksec"><span class="sq">II</span><h4>Pomoce dydaktyczne</h4><span class="line"></span></div>
        <ul class="klista">{pom}</ul>
      </div>
      <div>
        <div class="ksec"><span class="sq">III</span><h4>Metody i formy działań</h4><span class="line"></span></div>
        <ul class="klista">{met}</ul>
      </div>
    </div>
    <div class="kdwie" style="align-items:end">
      <div>
        <div class="ksec"><span class="sq">IV</span><h4>Sposób realizacji</h4><span class="line"></span></div>
        <div class="krodzaj" style="font-style:italic">Tabela poniżej ↓</div>
      </div>
      <div>
        <div class="ksec"><span class="sq">V</span><h4>Rodzaj zajęć</h4><span class="line"></span></div>
        <div class="krodzaj">{_e(K["rodzaj"])}</div>
      </div>
    </div>
    <p class="kkurs">Konkretne czynności nauczyciela (N) i odpowiadające im oczekiwane reakcje
      i umiejętności dziecka (D).</p>
    <table class="ktab">
      <thead><tr><th style="width:26px">Lp.</th><th style="width:47%">Czynności nauczyciela (N)</th>
        <th>Oczekiwane reakcje i umiejętności dziecka (D)</th></tr></thead>
      <tbody>{prz}</tbody>
    </table>

    <div class="ksec"><span class="sq">VI</span><h4>Modyfikacja przy ocenie żółtej / czerwonej</h4>
      <span class="line"></span></div>
    <p class="kkurs">Modyfikację stosuje się, gdy brak progresu w dwóch kolejnych sesjach.
      Zielona — rozszerzenie przy pełnym sukcesie. Kliknięty poziom wyróżniony.</p>
    <div class="kmods">{mods}</div>
    <div class="kwsk"><b>Wskazówka dla prowadzącego:</b> {_e(K["wskazowka"])}</div>

    <div class="ksec"><span class="sq">VII</span><h4>Materiały do wydruku</h4><span class="line"></span>
      </div>
    <p class="kkurs">Karta pomocy z ilustracją i poleceniem nagranym jej głosem, a pod nią
      materiał do wycięcia — cztery karty i pasek kolejności, A4 pionowo.</p>
{KP.karta(K["nr"], K["wersja"], K["wiek"])}
{_arkusz(K["arkusz"], K["nr"])}

    <div class="kfoot">
      <button class="chipbtn" data-zamknij>✕ Zamknij i wróć do tabeli</button>
      <button class="chipbtn mocny" data-druk>Drukuj konspekt A4</button>
    </div>
    <p class="kesc">zamkniesz też klawiszem <b>Esc</b> albo kliknięciem w tło poza kartą</p>
  </div>
</div>'''


def modale():
    """Wszystkie 75 konspektów — po jednym modalu na parę (wskaźnik, wersja)."""
    return "\n".join(modal(KF.konspekt(nr, w)) for nr, w in KF.klucze())


def spis(wersja):
    """Wykaz konspektów wersji — rozwijany, z podziałem na funkcje.

    Bez wykazu konspektów po prostu się nie znajduje: żeby otworzyć konspekt,
    trzeba wiedzieć, że komórka jest klikalna. W banku ta lekcja kosztowała
    już jedną przebudowę.
    """
    grupy = []
    for rzym in ("I", "II", "III", "IV", "V"):
        poz = [(nr, w) for nr, w in KF.klucze() if w == wersja and nr.split(".")[0] == rzym]
        if not poz:
            continue
        nazwa = KF.FUNKCJA[poz[0][0]][1]
        kafle = "".join(
            f'<button type="button" class="kbtn" data-spis="{KF.kid(nr, w)}" '
            f'data-wersja="{w}" data-wsk="{nr}">'
            f'<span class="knr">{nr}</span><b>{_e(KF.RDZEN[nr]["tytul"])}</b>'
            f'<span class="kzast">{_e(KF.FUNKCJA[nr][2]["zastepcze"])}</span></button>'
            for nr, w in poz)
        grupy.append(f'<div class="kgrupa"><h4>Funkcja {rzym} · {_e(nazwa)}</h4>'
                     f'<div class="ksiatka">{kafle}</div></div>')
    ile = len([1 for nr, w in KF.klucze() if w == wersja])
    return (f'<details class="kspis"><summary>Wykaz konspektów · {ile} scenariuszy '
            f'zajęć do tej wersji wiekowej</summary><div class="kspis-tresc">'
            f'<p class="kspis-info">Konspekt otwiera też kliknięcie celu w tabeli — '
            f'otwarty scenariusz ma wtedy wyróżniony ten poziom wsparcia, w który '
            f'kliknięto.<button type="button" class="chipbtn mocny" data-zeszyt="{wersja}">'
            f'Drukuj wszystkie {ile} konspektów (A4)</button></p>'
            f'{"".join(grupy)}</div></details>')
