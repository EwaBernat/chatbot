# -*- coding: utf-8 -*-
"""Własne konspekty nauczycielki — dopisywane wprost do celu SMART w banku.

Bank ma 178 gotowych konspektów, ale każda grupa jest inna i prędzej czy później
trzeba napisać własny scenariusz. Ten moduł dokłada do banku edytor: przy każdej
komórce z celem SMART jest przycisk **+**, który otwiera formularz o dokładnie
takiej samej strukturze co konspekt gotowy (I cel · II pomoce · III metody ·
IV–V realizacja · przebieg N/D · VI modyfikacje · wskazówka). Zapisany konspekt
otwiera się i drukuje tak samo jak gotowy — ta sama karta, ten sam druk KC-3 A4.

Konspekt jest **przypisany do celu**, nie do dokumentu: pamięta wersję wiekową,
numer twierdzenia i poziom wsparcia, z którego wyszedł. Dzięki temu wraca
dokładnie tam, gdzie nauczycielka go szukała, a cel edukacyjny bierze się wprost
z banku — nie przepisuje się go ręcznie i nie da się go rozjechać z arkuszem KPOF.

Gdzie to siedzi
---------------
Dane trzymamy w `localStorage` przeglądarki pod kluczem `KLUCZ`. To świadomy
wybór: bank jest jednym plikiem HTML otwieranym z dysku, bez serwera i bez konta,
więc nie ma dokąd wysłać danych — a przeglądarka pamięta je między otwarciami
pliku i przeżywa przebudowę banku (klucz nie zależy od nazwy pliku).

Czego `localStorage` nie zrobi: nie przeniesie konspektów na drugi komputer,
do innej przeglądarki ani przez tryb prywatny. Dlatego panel ma **zapis kopii
do pliku JSON i wczytanie jej z powrotem** — to jest właściwa droga przenoszenia
i archiwizacji, a nie dodatek. Panel mówi o tym wprost, zamiast zostawiać
nauczycielkę z fałszywym poczuciem, że „zapisało się".

Gdy przeglądarka blokuje `localStorage` (tryb prywatny, wyłączone dane witryn),
edytor **nadal działa** — konspekty żyją w pamięci karty i można je zapisać do
pliku. Panel pokazuje wtedy ostrzeżenie zamiast udawać, że wszystko gra.

Uwagi do składania
------------------
* `STYL` idzie do arkusza dokumentu, `SZKIELET` raz na dokument (dwa okna:
  podgląd i edytor), `panel()` raz na wersję wiekową, `SKRYPT` na koniec ciała.
* Okno podglądu jest zwykłym `.kmodal`, więc dziedziczy wszystko: zamykanie
  Escape'em, kliknięciem w tło i regułę druku `html.print-konspekt`. Edytor
  celowo nim **nie** jest — Escape nie może kasować niezapisanego formularza.
"""

KLUCZ = "eduplaner2026.moje-konspekty.v1"

# ——— arkusz stylów ————————————————————————————————————————————————————————
STYL = """
/* ——— własne konspekty ——— */
td.g{position:relative}
@media screen{td.g .cel{padding-right:17px}}
/* Plus jest widoczny zawsze, tylko przygaszony. Na hoverze byłby nie do
   znalezienia na tablecie, a wcześniej w tym projekcie już raz przepadła
   funkcja schowana pod najechaniem myszą. */
.mk-add{position:absolute; top:3px; right:3px; width:20px; height:20px; padding:0;
  display:grid; place-items:center; border:1px solid var(--line); border-radius:6px;
  background:var(--paper); color:var(--muted); font:700 13px/1 inherit; cursor:pointer;
  opacity:.4; transition:opacity .12s; z-index:2}
td.g:hover .mk-add,td.g:focus-within .mk-add,.mk-add:focus-visible{opacity:1}
.mk-add:hover{border-color:var(--accent); color:var(--accent); background:var(--paper); opacity:1}
td.g.mk-ma .mk-add{opacity:1; border-color:var(--accent); color:var(--accent);
  background:var(--paper); font-size:11px}
.mk-panel{margin:18px 0 4px; border:1px solid var(--line); border-radius:12px;
  background:var(--paper); overflow:hidden}
.mk-panel > summary{list-style:none; cursor:pointer; padding:10px 16px;
  background:var(--strong); color:var(--on-strong); font:700 12.5px/1.4 inherit;
  letter-spacing:.02em; display:flex; align-items:center; gap:10px}
.mk-panel > summary::-webkit-details-marker{display:none}
.mk-panel > summary .ile{margin-left:auto; font-weight:600; opacity:.85; font-size:11px}
.mk-panel[open] > summary .rozwin,.mk-panel:not([open]) > summary .zwin{display:none}
.mk-tresc{padding:14px 16px 16px}
.mk-info{margin:0 0 12px; font-size:11.5px; line-height:1.65; color:var(--muted)}
.mk-info b{color:var(--ink)}
.mk-ostrz{margin:0 0 12px; padding:9px 12px; border-radius:8px; font-size:11.5px;
  line-height:1.6; background:var(--p2-bg); border:1px solid var(--p2-br); color:var(--text)}
.mk-ostrz b{color:var(--p2)}
.mk-narzedzia{display:flex; flex-wrap:wrap; gap:8px; margin:0 0 14px}
.mk-lista{display:grid; grid-template-columns:repeat(auto-fill,minmax(252px,1fr)); gap:7px}
.mk-poz{display:flex; align-items:center; gap:9px; min-height:42px; padding:7px 11px;
  border:1px solid var(--line); border-radius:9px; background:var(--paper);
  font:600 11.5px/1.35 inherit; color:var(--ink); text-align:left; cursor:pointer}
.mk-poz:hover{border-color:var(--accent); color:var(--accent)}
.mk-poz b{flex:0 0 46px; font:700 10px/1 "JetBrains Mono",ui-monospace,"Courier New",monospace;
  color:var(--muted); letter-spacing:.02em}
.mk-poz:hover b{color:var(--accent)}
.mk-poz .tyt{flex:1 1 auto}
.mk-poz .lvl{flex:0 0 auto; width:18px; height:18px; border-radius:50%;
  display:grid; place-items:center; font:700 9px/1 inherit; color:#fff}
.mk-poz .lvl.p3{background:var(--p3)} .mk-poz .lvl.p2{background:var(--p2)}
.mk-poz .lvl.p1{background:var(--p1)}
.mk-pusto{margin:0; font-size:11.5px; color:var(--muted); font-style:italic}

/* edytor — własne okno, bo Escape nie może kasować niezapisanej pracy */
.mkmodal{position:fixed; inset:0; z-index:70; display:none; overflow:auto;
  background:rgba(20,14,45,.62); padding:22px 16px}
.mkmodal.open{display:block}
.mkcard{max-width:940px; margin:0 auto; background:var(--paper); border-radius:14px;
  padding:22px 24px 20px; box-shadow:0 18px 60px rgba(20,14,45,.35)}
.mk-head{display:flex; align-items:baseline; gap:12px; padding-bottom:10px;
  border-bottom:2px solid var(--strong); margin-bottom:14px}
.mk-head h3{margin:0; font-size:19px; color:var(--strong)}
.mk-head .skad{margin-left:auto; font-size:11px; color:var(--muted); text-align:right;
  line-height:1.5}
.mk-cel{margin:0 0 16px; padding:11px 13px; border-radius:9px; background:var(--soft);
  border:1px solid var(--line); font-size:11.5px; line-height:1.65}
.mk-cel .lab{display:block; font-weight:700; color:var(--strong); font-size:10px;
  letter-spacing:.08em; text-transform:uppercase; margin-bottom:4px}
.mk-pola{display:grid; grid-template-columns:1fr 1fr; gap:12px 16px}
.mk-pole{display:flex; flex-direction:column; gap:4px}
.mk-pole.szer{grid-column:1/-1}
.mk-pole label{font:700 10px/1.3 inherit; letter-spacing:.07em; text-transform:uppercase;
  color:var(--strong)}
.mk-pole .podp{font:400 10.5px/1.5 inherit; text-transform:none; letter-spacing:0;
  color:var(--muted)}
.mk-pole input,.mk-pole textarea,.mk-pole select{font:400 12px/1.6 inherit; color:var(--text);
  padding:7px 9px; border:1px solid var(--line); border-radius:7px; background:var(--paper);
  width:100%; box-sizing:border-box; resize:vertical}
.mk-pole input:focus,.mk-pole textarea:focus,.mk-pole select:focus{outline:2px solid var(--accent);
  outline-offset:1px; border-color:var(--accent)}
.mk-grupa{grid-column:1/-1; margin:8px 0 0; padding-top:10px; border-top:1px solid var(--line);
  font:700 10px/1.3 inherit; letter-spacing:.08em; text-transform:uppercase; color:var(--accent)}
.mk-prz{grid-column:1/-1; display:flex; flex-direction:column; gap:7px}
.mk-prz-w{display:grid; grid-template-columns:22px 1fr 1fr 26px; gap:8px; align-items:start}
.mk-prz-w .nr{padding-top:8px; font:700 11px/1 "JetBrains Mono",ui-monospace,monospace;
  color:var(--muted); text-align:right}
.mk-prz-w textarea{min-height:52px}
.mk-usun-w{align-self:start; margin-top:4px; width:24px; height:24px; padding:0; border-radius:6px;
  border:1px solid var(--line); background:var(--paper); color:var(--muted); cursor:pointer;
  font:600 13px/1 inherit}
.mk-usun-w:hover{border-color:var(--p3); color:var(--p3)}
.mk-stopka{display:flex; flex-wrap:wrap; gap:9px; align-items:center;
  margin-top:18px; padding-top:14px; border-top:1px solid var(--line)}
.mk-stopka .rozdziel{margin-left:auto}
.mk-blad{margin:10px 0 0; padding:8px 11px; border-radius:7px; font-size:11.5px;
  background:var(--p3-bg); border:1px solid var(--p3-br); color:var(--p3); display:none}
.mk-blad.jest{display:block}
@media (max-width:760px){.mk-pola{grid-template-columns:1fr}
  .mk-prz-w{grid-template-columns:20px 1fr 24px}
  .mk-prz-w textarea:last-of-type{grid-column:2}}
@media print{.mk-add,.mk-panel,.mkmodal{display:none !important}}
"""

# ——— dwa okna, raz na dokument ————————————————————————————————————————————
SZKIELET = """
<div class="kmodal" id="mk-widok" role="dialog" aria-modal="true" aria-label="Mój konspekt">
  <div class="kcard" id="mk-widok-tresc"></div>
</div>
<div class="mkmodal" id="mk-edytor" role="dialog" aria-modal="true" aria-label="Edytor własnego konspektu">
  <div class="mkcard">
    <div class="mk-head">
      <h3 id="mk-edytor-tytul">Nowy konspekt własny</h3>
      <div class="skad" id="mk-edytor-skad"></div>
    </div>
    <div class="mk-cel" id="mk-edytor-cel"></div>
    <form id="mk-form" class="mk-pola" autocomplete="off">
      <div class="mk-pole szer"><label for="mk-tytul">Tytuł zajęć <span class="podp">— pole wymagane</span></label>
        <input id="mk-tytul" name="tytul" maxlength="90" required></div>
      <div class="mk-pole szer"><label for="mk-podtytul">Czego dotyczy <span class="podp">— jedno zdanie pod tytułem</span></label>
        <input id="mk-podtytul" name="podtytul" maxlength="140"></div>
      <div class="mk-pole"><label for="mk-czas">Czas</label>
        <input id="mk-czas" name="czas" maxlength="30" placeholder="20 min"></div>
      <div class="mk-pole"><label for="mk-forma">Forma</label>
        <input id="mk-forma" name="forma" maxlength="60" placeholder="mała grupa (4–6 dzieci)"></div>
      <div class="mk-pole"><label for="mk-cykl">Cykl</label>
        <input id="mk-cykl" name="cykl" maxlength="40" placeholder="3× w tygodniu"></div>
      <div class="mk-pole"><label for="mk-poziom">Poziom wsparcia</label>
        <select id="mk-poziom" name="poziom">
          <option value="p3">Poziom III · ewaluacja 4 tygodnie</option>
          <option value="p2">Poziom II · ewaluacja 8 tygodni</option>
          <option value="p1">Poziom I · ewaluacja 12 tygodni</option>
        </select></div>

      <div class="mk-grupa">I · Cel terapeutyczny</div>
      <div class="mk-pole szer"><label for="mk-ter">Cel terapeutyczny
        <span class="podp">— co dziecko zrobi, w ilu próbach i w jakim czasie</span></label>
        <textarea id="mk-ter" name="ter" rows="3"></textarea></div>
      <div class="mk-pole szer"><label for="mk-kryt">Kryterium — czym mierzysz</label>
        <input id="mk-kryt" name="kryt" maxlength="160" placeholder="arkusz obserwacji · 5 prób w tygodniu"></div>

      <div class="mk-grupa">II–V · Pomoce, metody, rodzaj zajęć</div>
      <div class="mk-pole"><label for="mk-pomoce">Pomoce dydaktyczne <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mk-pomoce" name="pomoce" rows="5"></textarea></div>
      <div class="mk-pole"><label for="mk-metody">Metody i formy działań <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mk-metody" name="metody" rows="5"></textarea></div>
      <div class="mk-pole szer"><label for="mk-rodzaj">Rodzaj zajęć</label>
        <input id="mk-rodzaj" name="rodzaj" maxlength="120"
          placeholder="Zajęcia wspierające funkcje poznawcze / pomoc p-p"></div>

      <div class="mk-grupa">Przebieg zajęć — czynność nauczyciela (N) i reakcja dziecka (D)</div>
      <div class="mk-prz" id="mk-przebieg"></div>
      <div class="mk-pole szer"><button type="button" class="chipbtn" id="mk-dodaj-wiersz">+ Dodaj krok</button></div>

      <div class="mk-grupa">VI · Modyfikacja przy ocenie żółtej / czerwonej / zielonej</div>
      <div class="mk-pole"><label for="mk-mod3">Poziom III · czerwona <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mk-mod3" name="mod3" rows="4"></textarea></div>
      <div class="mk-pole"><label for="mk-mod2">Poziom II · żółta <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mk-mod2" name="mod2" rows="4"></textarea></div>
      <div class="mk-pole szer"><label for="mk-mod1">Poziom I · zielona — rozszerzenie <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mk-mod1" name="mod1" rows="3"></textarea></div>
      <div class="mk-pole szer"><label for="mk-wsk">Wskazówka dla prowadzącego</label>
        <textarea id="mk-wsk" name="wskazowka" rows="2"></textarea></div>
    </form>
    <p class="mk-blad" id="mk-blad"></p>
    <div class="mk-stopka">
      <button type="button" class="chipbtn" id="mk-anuluj">Anuluj</button>
      <button type="button" class="chipbtn rozdziel" id="mk-usun" style="border-color:var(--p3-br); color:var(--p3)">Usuń konspekt</button>
      <button type="button" class="chipbtn" id="mk-zapisz"
        style="background:var(--strong); border-color:var(--strong); color:var(--on-strong)">Zapisz konspekt</button>
    </div>
  </div>
</div>
<input type="file" id="mk-plik" accept="application/json,.json" hidden>
"""


def panel(kod_wersji):
    """Panel „Moje konspekty" dla jednej wersji wiekowej — wypełnia go skrypt."""
    return f"""  <details class="mk-panel" data-mk-panel="{kod_wersji}">
    <summary>Moje konspekty<span class="rozwin"> — kliknij, aby rozwinąć</span>
<span class="zwin"> — kliknij, aby zwinąć</span><span class="ile" data-mk-ile>0</span></summary>
    <div class="mk-tresc">
      <p class="mk-ostrz" data-mk-ostrz hidden></p>
      <p class="mk-info">Własny konspekt dopisujesz <b>plusem w komórce z celem</b> — najedź myszą
      na dowolny cel SMART w tabeli poniżej i kliknij <b>+</b> w jego prawym górnym rogu.
      Konspekt zostaje przy tym celu i otwiera się tak samo jak gotowy, razem z drukiem A4.
      Zapisuje się <b>w tej przeglądarce</b>, więc żeby przenieść go na inny komputer albo
      mieć kopię — zapisz plik JSON poniżej.</p>
      <div class="mk-narzedzia">
        <button type="button" class="chipbtn" data-mk-eksport>Zapisz kopię do pliku (JSON)</button>
        <button type="button" class="chipbtn" data-mk-import>Wczytaj kopię z pliku</button>
      </div>
      <div class="mk-lista" data-mk-lista></div>
      <p class="mk-pusto" data-mk-pusto>Nie masz jeszcze własnych konspektów w tej wersji.</p>
    </div>
  </details>"""


# ——— skrypt ————————————————————————————————————————————————————————————————
SKRYPT = """
/* Własne konspekty nauczycielki — dopisywane do celu SMART.
   Całość w jednym domknięciu; zdarzenia obsługujemy delegacją, bo pozycje
   panelu i przyciski w karcie konspektu powstają dopiero w trakcie pracy. */
(function(){
  const KLUCZ='__KLUCZ__';
  const LVLROM={p3:'III',p2:'II',p1:'I'};
  const LVLNAZWA={p3:'Poziom III',p2:'Poziom II',p1:'Poziom I'};
  const LVLTYG={p3:'4 tyg.',p2:'8 tyg.',p1:'12 tyg.'};
  let pamiec=null;          // kopia robocza, gdy localStorage jest zablokowany
  let edytowany=null;       // rekord w edycji albo null przy nowym konspekcie
  let kontekstBiezacy=null; // cel, z którego wyszedł otwarty formularz

  const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const linie=s=>String(s||'').split('\\n').map(x=>x.trim()).filter(Boolean);

  function magazynDziala(){
    try{const k='__mk_test__'; localStorage.setItem(k,'1'); localStorage.removeItem(k); return true;}
    catch(e){return false;}
  }
  const MAGAZYN=magazynDziala();

  function wczytaj(){
    if(!MAGAZYN) return pamiec||(pamiec=[]);
    try{const s=localStorage.getItem(KLUCZ); const t=s?JSON.parse(s):[]; return Array.isArray(t)?t:[];}
    catch(e){return [];}
  }
  function zapisz(lista){
    if(!MAGAZYN){pamiec=lista; return true;}
    try{localStorage.setItem(KLUCZ,JSON.stringify(lista)); return true;}
    catch(e){pamiec=lista; return false;}
  }
  const noweId=()=>'mk'+Date.now().toString(36)+Math.random().toString(36).slice(2,7);

  /* Kontekst celu, z którego wychodzi konspekt — czytamy go z wiersza tabeli,
     zamiast powtarzać cały bank w osobnym obiekcie JS. */
  function kontekst(td){
    const tr=td.closest('tr'), vers=td.closest('.vers'), sek=td.closest('section.sec');
    const poziom=['p3','p2','p1'].find(p=>td.classList.contains(p))||'p2';
    return {
      wersja: vers?vers.dataset.v:'',
      nr: parseInt((tr.querySelector('td.lp')||{}).textContent,10)||0,
      poziom,
      twierdzenie: ((tr.querySelector('td.tw')||{}).firstChild||{}).textContent||'',
      icf: ((tr.querySelector('td.icf .kod')||{}).textContent||'').trim(),
      pp: ((tr.querySelector('td.pp .kod')||{}).textContent||'').trim(),
      obszar: sek?((sek.querySelector('.sec-h h2')||{}).textContent||'').trim():'',
      rzym: sek?((sek.querySelector('.sec-h .sq')||{}).textContent||'').trim():'',
      etykieta: vers?((vers.querySelector('.vband h2')||{}).textContent||'').replace(/^Wersja .\\s*·\\s*/,''):''
    };
  }
  /* Cel z banku dla wybranego poziomu — bierzemy go zawsze na świeżo z tabeli,
     żeby konspekt nie zaczął żyć własną wersją celu po poprawce w banku. */
  function celZBanku(k,poziom){
    const vers=document.querySelector('.vers[data-v="'+CSS.escape(k.wersja)+'"]');
    if(!vers) return '';
    const tr=[...vers.querySelectorAll('tbody tr')].find(r=>
      parseInt((r.querySelector('td.lp')||{}).textContent,10)===k.nr);
    if(!tr) return '';
    const td=tr.querySelector('td.'+(poziom||k.poziom)+' .cel');
    return td?td.textContent.trim():'';
  }

  /* ——— podgląd konspektu ——— */
  function widok(k){
    const cel=celZBanku(k,k.poziom);
    const li=t=>t.map(x=>'<li>'+esc(x)+'</li>').join('');
    const prz=(k.przebieg||[]).map((p,i)=>
      '<tr><td class="lp">'+(i+1)+'</td><td>'+esc(p[0])+'</td><td>'+esc(p[1])+'</td></tr>').join('');
    const pusty='<li style="color:var(--muted); font-style:italic">— nie wypełniono</li>';
    return `
    <button class="kclose" data-close="mk-widok" aria-label="Zamknij konspekt" title="Zamknij (Esc)">✕</button>
    <div class="khead">
      <span class="mark" role="img" aria-label="Logo PCTP"></span>
      <div>
        <div class="kw">EduPlaner 2026</div>
        <div class="ks">Konspekt własny · ${esc(k.obszar)} · ${esc(k.etykieta)} · wersja ${esc(k.wersja)} · twierdzenie ${k.nr}</div>
      </div>
      <span class="kpill">Mój konspekt</span>
    </div>
    <div class="kmeta kdziecko" style="grid-template-columns:1.5fr 1fr 1fr; margin:12px 0 0">
      <div class="field"><b>Dotyczy dziecka</b><span class="dots"></span></div>
      <div class="field"><b>Grupa</b><span class="dots"></span></div>
      <div class="field"><b>Data</b><span class="dots"></span></div>
    </div>
    <div class="ktitle">
      <span class="kp">Konspekt zajęć · druk KC-3 · opracowanie własne</span>
      <div class="ksfera">${esc(k.rzym)} ${esc(k.obszar)} · ICF ${esc(k.icf)} · PP ${esc(k.pp)}</div>
      <h3>${esc(k.tytul)}</h3>
      <div class="kpod">${esc(k.podtytul||'')}</div>
    </div>
    <div class="kmeta">
      <div class="field"><b>Czas</b><span class="val">${esc(k.czas||'—')}</span></div>
      <div class="field"><b>Forma</b><span class="val">${esc(k.forma||'—')}</span></div>
      <div class="field"><b>Cykl</b><span class="val">${esc(k.cykl||'—')}</span></div>
      <div class="field"><b>Poziom wsparcia</b><span class="lvl ${k.poziom}">${LVLROM[k.poziom]}</span></div>
    </div>
    <div class="ksec"><span class="sq">I</span><h4>Cel SMART</h4><span class="line"></span></div>
    <div class="kcele">
      <div class="kcel edu"><div class="kchead">Cel edukacyjny — z banku KC-1 · ${LVLNAZWA[k.poziom]}</div>
        <div class="kvar on" data-lvl="${k.poziom}">
          <div class="ktresc">${esc(cel)}</div>
          <div class="kkryt"><b>Twierdzenie ${k.nr}:</b> ${esc(k.twierdzenie)} · horyzont ${LVLTYG[k.poziom]}</div>
        </div>
      </div>
      <div class="kcel ter"><div class="kchead">Cel terapeutyczny</div>
        <div class="ktresc">${esc(k.ter||'—')}</div>
        <div class="kkryt"><b>Kryterium:</b> ${esc(k.kryt||'—')}</div>
      </div>
    </div>
    <div class="kdwie">
      <div><div class="ksec"><span class="sq">II</span><h4>Pomoce dydaktyczne</h4><span class="line"></span></div>
        <ul class="klista">${(k.pomoce||[]).length?li(k.pomoce):pusty}</ul></div>
      <div><div class="ksec"><span class="sq">III</span><h4>Metody i formy działań</h4><span class="line"></span></div>
        <ul class="klista">${(k.metody||[]).length?li(k.metody):pusty}</ul></div>
    </div>
    <div class="kdwie" style="align-items:end">
      <div><div class="ksec"><span class="sq">IV</span><h4>Sposób realizacji</h4><span class="line"></span></div>
        <div class="krodzaj" style="font-style:italic">Tabela poniżej ↓</div></div>
      <div><div class="ksec"><span class="sq">V</span><h4>Rodzaj zajęć</h4><span class="line"></span></div>
        <div class="krodzaj">${esc(k.rodzaj||'—')}</div></div>
    </div>
    <p class="kkurs">Konkretne czynności nauczyciela (N) i odpowiadające im oczekiwane reakcje i umiejętności dziecka (D).</p>
    <div class="tablewrap"><table class="ktab">
      <thead><tr><th class="c-lp">Lp.</th><th style="width:47%">Czynności nauczyciela (N)</th>
        <th>Oczekiwane reakcje i umiejętności dziecka (D)</th></tr></thead>
      <tbody>${prz||'<tr><td class="lp">1</td><td>—</td><td>—</td></tr>'}</tbody>
    </table></div>
    <div class="ksec"><span class="sq">VI</span><h4>Modyfikacja przy ocenie żółtej / czerwonej</h4><span class="line"></span></div>
    <div class="kmods">
      <div class="kmod m2 ${k.poziom==='p2'?'aktywny':''}"><b>Poziom II · Żółta</b>
        <ul class="klista">${(k.mod2||[]).length?li(k.mod2):pusty}</ul></div>
      <div class="kmod m3 ${k.poziom==='p3'?'aktywny':''}"><b>Poziom III · Czerwona</b>
        <ul class="klista">${(k.mod3||[]).length?li(k.mod3):pusty}</ul></div>
      <div class="kmod m1 ${k.poziom==='p1'?'aktywny':''}"><b>Poziom I · Zielona</b>
        <ul class="klista">${(k.mod1||[]).length?li(k.mod1):pusty}</ul></div>
    </div>
    <div class="kwsk"><b>Wskazówka dla prowadzącego:</b> ${esc(k.wskazowka||'—')}</div>
    <div class="kfoot">
      <button class="chipbtn zamknij" data-close="mk-widok">✕ Zamknij i wróć do tabeli</button>
      <button class="chipbtn" data-mk-edytuj="${k.id}">Edytuj konspekt</button>
      <button class="chipbtn" style="background:var(--strong); border-color:var(--strong); color:var(--on-strong)"
        data-mk-drukuj>Drukuj konspekt A4</button>
    </div>
    <p class="kesc">zamkniesz też klawiszem <b>Esc</b> lub kliknięciem w ciemne tło poza kartą</p>`;
  }

  function pokazKonspekt(id){
    const k=wczytaj().find(x=>x.id===id); if(!k) return;
    // Gotowy konspekt tej komórki mógł zostać otwarty wcześniej; dwa otwarte
    // okna naraz wyszłyby na wydruku jako dwa konspekty pod rząd.
    document.querySelectorAll('.kmodal.open').forEach(m=>m.classList.remove('open'));
    document.getElementById('mk-widok-tresc').innerHTML=widok(k);
    const m=document.getElementById('mk-widok');
    m.classList.add('open'); document.body.style.overflow='hidden';
    const b=m.querySelector('.kclose'); if(b) b.focus();
  }

  /* ——— edytor ——— */
  function wierszPrzebiegu(n,d){
    const box=document.getElementById('mk-przebieg');
    const w=document.createElement('div'); w.className='mk-prz-w';
    w.innerHTML='<span class="nr"></span>'
      +'<textarea placeholder="N — co robi nauczyciel" data-n></textarea>'
      +'<textarea placeholder="D — co robi dziecko" data-d></textarea>'
      +'<button type="button" class="mk-usun-w" title="Usuń ten krok" aria-label="Usuń krok">×</button>';
    w.querySelector('[data-n]').value=n||'';
    w.querySelector('[data-d]').value=d||'';
    box.appendChild(w); numeruj();
  }
  const numeruj=()=>[...document.querySelectorAll('#mk-przebieg .mk-prz-w')]
      .forEach((w,i)=>w.querySelector('.nr').textContent=(i+1)+'.');

  function otworzEdytor(dane,k){
    edytowany=dane||null;
    const ctx=dane||k;
    kontekstBiezacy=ctx;
    document.getElementById('mk-edytor-tytul').textContent=dane?'Edytuj własny konspekt':'Nowy konspekt własny';
    document.getElementById('mk-edytor-skad').innerHTML=
      'wersja '+esc(ctx.wersja)+' · twierdzenie '+ctx.nr+'<br>ICF '+esc(ctx.icf)+' · PP '+esc(ctx.pp);
    const f=id=>document.getElementById(id);
    f('mk-tytul').value=dane?dane.tytul||'':'';
    f('mk-podtytul').value=dane?dane.podtytul||'':'';
    f('mk-czas').value=dane?dane.czas||'':'20 min';
    f('mk-forma').value=dane?dane.forma||'':'';
    f('mk-cykl').value=dane?dane.cykl||'':'';
    f('mk-poziom').value=(dane?dane.poziom:k.poziom)||'p2';
    f('mk-ter').value=dane?dane.ter||'':'';
    f('mk-kryt').value=dane?dane.kryt||'':'';
    f('mk-pomoce').value=dane?(dane.pomoce||[]).join('\\n'):'';
    f('mk-metody').value=dane?(dane.metody||[]).join('\\n'):'';
    f('mk-rodzaj').value=dane?dane.rodzaj||'':'';
    f('mk-mod3').value=dane?(dane.mod3||[]).join('\\n'):'';
    f('mk-mod2').value=dane?(dane.mod2||[]).join('\\n'):'';
    f('mk-mod1').value=dane?(dane.mod1||[]).join('\\n'):'';
    f('mk-wsk').value=dane?dane.wskazowka||'':'';
    document.getElementById('mk-przebieg').innerHTML='';
    const kroki=(dane&&dane.przebieg&&dane.przebieg.length)?dane.przebieg:[['','' ],['',''],['','']];
    kroki.forEach(p=>wierszPrzebiegu(p[0],p[1]));
    document.getElementById('mk-usun').style.display=dane?'':'none';
    document.getElementById('mk-blad').classList.remove('jest');
    odswiezCelWEdytorze(ctx);
    document.getElementById('mk-edytor').classList.add('open');
    document.body.style.overflow='hidden';
    f('mk-tytul').focus();
  }
  function odswiezCelWEdytorze(ctx){
    const poz=document.getElementById('mk-poziom').value;
    document.getElementById('mk-edytor-cel').innerHTML=
      '<span class="lab">Cel edukacyjny z banku · '+LVLNAZWA[poz]+'</span>'
      +esc(celZBanku(ctx,poz))
      +'<br><span style="color:var(--muted)">Twierdzenie '+ctx.nr+': '+esc(ctx.twierdzenie)+'</span>';
  }
  function zamknijEdytor(){
    document.getElementById('mk-edytor').classList.remove('open');
    if(!document.querySelector('.kmodal.open')) document.body.style.overflow='';
    edytowany=null; kontekstBiezacy=null;
  }

  function zbierz(ctx){
    const v=id=>document.getElementById(id).value.trim();
    const przebieg=[...document.querySelectorAll('#mk-przebieg .mk-prz-w')]
      .map(w=>[w.querySelector('[data-n]').value.trim(), w.querySelector('[data-d]').value.trim()])
      .filter(p=>p[0]||p[1]);
    return {
      id: ctx.id||noweId(),
      wersja: ctx.wersja, nr: ctx.nr, poziom: v('mk-poziom'),
      twierdzenie: ctx.twierdzenie, icf: ctx.icf, pp: ctx.pp,
      obszar: ctx.obszar, rzym: ctx.rzym, etykieta: ctx.etykieta,
      tytul: v('mk-tytul'), podtytul: v('mk-podtytul'),
      czas: v('mk-czas'), forma: v('mk-forma'), cykl: v('mk-cykl'),
      ter: v('mk-ter'), kryt: v('mk-kryt'),
      pomoce: linie(v('mk-pomoce')), metody: linie(v('mk-metody')), rodzaj: v('mk-rodzaj'),
      przebieg, mod3: linie(v('mk-mod3')), mod2: linie(v('mk-mod2')), mod1: linie(v('mk-mod1')),
      wskazowka: v('mk-wsk'),
      utworzono: ctx.utworzono||new Date().toISOString(),
      zmieniono: new Date().toISOString()
    };
  }
  function blad(t){
    const b=document.getElementById('mk-blad'); b.textContent=t; b.classList.add('jest');
  }

  /* ——— panele i oznaczenia w tabeli ——— */
  function odswiez(){
    const lista=wczytaj();
    document.querySelectorAll('td.g.mk-ma').forEach(td=>{
      td.classList.remove('mk-ma');
      const b=td.querySelector('.mk-add'); if(b){b.textContent='+'; b.title='Dodaj własny konspekt do tego celu';}
    });
    lista.forEach(k=>{
      const vers=document.querySelector('.vers[data-v="'+CSS.escape(k.wersja)+'"]'); if(!vers) return;
      const tr=[...vers.querySelectorAll('tbody tr')].find(r=>
        parseInt((r.querySelector('td.lp')||{}).textContent,10)===k.nr);
      if(!tr) return;
      const td=tr.querySelector('td.g.'+k.poziom); if(!td) return;
      td.classList.add('mk-ma');
      const b=td.querySelector('.mk-add');
      if(b){b.textContent='✎'; b.title='Mój konspekt: '+k.tytul;}
    });
    document.querySelectorAll('[data-mk-panel]').forEach(p=>{
      const w=p.dataset.mkPanel, moje=lista.filter(k=>k.wersja===w);
      p.querySelector('[data-mk-ile]').textContent=
        moje.length?(moje.length+(moje.length===1?' konspekt własny':' konspektów własnych')):'brak';
      const box=p.querySelector('[data-mk-lista]');
      box.innerHTML=moje.map(k=>
        '<button type="button" class="mk-poz" data-mk-otworz="'+k.id+'">'
        +'<b>tw. '+k.nr+'</b><span class="tyt">'+esc(k.tytul)+'</span>'
        +'<span class="lvl '+k.poziom+'">'+LVLROM[k.poziom]+'</span></button>').join('');
      p.querySelector('[data-mk-pusto]').hidden=moje.length>0;
      const o=p.querySelector('[data-mk-ostrz]');
      if(!MAGAZYN){
        o.hidden=false;
        o.innerHTML='<b>Ta przeglądarka nie pozwala zapisać danych witryny</b> (tryb prywatny albo '
          +'wyłączone dane lokalne). Konspekty będą działać do zamknięcia karty — zapisz je do pliku JSON, '
          +'zanim ją zamkniesz.';
      } else o.hidden=true;
    });
  }

  /* ——— kopia do pliku ——— */
  function eksport(){
    const lista=wczytaj();
    if(!lista.length){alert('Nie masz jeszcze żadnego własnego konspektu do zapisania.'); return;}
    const dane={dokument:'EduPlaner 2026 · moje konspekty', wersjaZapisu:1,
                zapisano:new Date().toISOString(), konspekty:lista};
    const b=new Blob([JSON.stringify(dane,null,2)],{type:'application/json'});
    const a=document.createElement('a');
    a.href=URL.createObjectURL(b);
    a.download='moje_konspekty_EduPlaner2026_'+new Date().toISOString().slice(0,10)+'.json';
    document.body.appendChild(a); a.click();
    setTimeout(()=>{URL.revokeObjectURL(a.href); a.remove();},1000);
  }
  function importuj(plik){
    const r=new FileReader();
    r.onload=()=>{
      let dane;
      try{dane=JSON.parse(r.result);}catch(e){alert('To nie jest plik z konspektami — nie udało się go odczytać.'); return;}
      const nowe=Array.isArray(dane)?dane:(dane&&Array.isArray(dane.konspekty)?dane.konspekty:null);
      if(!nowe){alert('W tym pliku nie ma konspektów.'); return;}
      const lista=wczytaj(), wg={}; lista.forEach(k=>wg[k.id]=k);
      let dodane=0, zastapione=0;
      nowe.forEach(k=>{
        if(!k||!k.id||!k.tytul) return;
        if(wg[k.id]) zastapione++; else dodane++;
        wg[k.id]=k;
      });
      zapisz(Object.values(wg)); odswiez();
      alert('Wczytano kopię: '+dodane+' nowych, '+zastapione+' zaktualizowanych.');
    };
    r.readAsText(plik);
  }

  /* ——— zdarzenia ——— */
  /* Plus łapiemy w fazie przechwytywania. Komórka z gotowym konspektem ma
     własny nasłuch kliknięcia wpięty wprost w `td`; nasłuch delegowany na
     `document` w fazie bąbelkowania odpaliłby się już po nim i `stopPropagation`
     przyszedłby za późno — otwierały się dwa konspekty naraz i tyle samo
     wychodziło z drukarki. */
  document.addEventListener('click',e=>{
    const dod=e.target.closest('.mk-add'); if(!dod) return;
    e.preventDefault(); e.stopPropagation();
    const td=dod.closest('td.g'), k=kontekst(td);
    const moj=wczytaj().find(x=>x.wersja===k.wersja&&x.nr===k.nr&&x.poziom===k.poziom);
    if(moj) pokazKonspekt(moj.id); else otworzEdytor(null,k);
  },true);
  document.addEventListener('click',e=>{
    const otw=e.target.closest('[data-mk-otworz]');
    if(otw){pokazKonspekt(otw.dataset.mkOtworz); return;}
    const edy=e.target.closest('[data-mk-edytuj]');
    if(edy){
      const k=wczytaj().find(x=>x.id===edy.dataset.mkEdytuj);
      if(k){document.getElementById('mk-widok').classList.remove('open'); otworzEdytor(k,k);}
      return;
    }
    if(e.target.closest('[data-mk-drukuj]')){
      document.documentElement.classList.add('print-konspekt');
      const gotowe=()=>{document.documentElement.classList.remove('print-konspekt');
                        window.removeEventListener('afterprint',gotowe);};
      window.addEventListener('afterprint',gotowe);
      window.print();
      return;
    }
    if(e.target.closest('[data-mk-eksport]')){eksport(); return;}
    if(e.target.closest('[data-mk-import]')){document.getElementById('mk-plik').click(); return;}
    if(e.target.closest('.mk-usun-w')){
      const w=e.target.closest('.mk-prz-w');
      if(document.querySelectorAll('#mk-przebieg .mk-prz-w').length>1){w.remove(); numeruj();}
      else{w.querySelectorAll('textarea').forEach(t=>t.value='');}
      return;
    }
  });
  document.getElementById('mk-dodaj-wiersz').addEventListener('click',()=>wierszPrzebiegu('',''));
  document.getElementById('mk-poziom').addEventListener('change',()=>{
    if(kontekstBiezacy) odswiezCelWEdytorze(kontekstBiezacy);
  });

  document.getElementById('mk-anuluj').addEventListener('click',()=>{
    if(confirm('Zamknąć edytor bez zapisania zmian?')) zamknijEdytor();
  });
  document.getElementById('mk-zapisz').addEventListener('click',()=>{
    const k=zbierz(kontekstBiezacy||{});
    if(!k.tytul){blad('Konspekt musi mieć tytuł — bez niego nie znajdziesz go później na liście.');
      document.getElementById('mk-tytul').focus(); return;}
    const lista=wczytaj().filter(x=>x.id!==k.id);
    lista.push(k);
    const ok=zapisz(lista);
    zamknijEdytor(); odswiez();
    if(!ok) alert('Konspekt jest gotowy, ale przeglądarka nie pozwoliła go zapisać na stałe. '
                 +'Zapisz kopię do pliku JSON, zanim zamkniesz kartę.');
    pokazKonspekt(k.id);
  });
  document.getElementById('mk-usun').addEventListener('click',()=>{
    const ctx=edytowany; if(!ctx) return;
    if(!confirm('Usunąć konspekt „'+ctx.tytul+'"? Tej operacji nie da się cofnąć.')) return;
    zapisz(wczytaj().filter(x=>x.id!==ctx.id));
    zamknijEdytor(); odswiez();
  });
  document.getElementById('mk-plik').addEventListener('change',e=>{
    if(e.target.files&&e.target.files[0]) importuj(e.target.files[0]);
    e.target.value='';
  });

  odswiez();
})();
"""


def skrypt():
    return SKRYPT.replace("__KLUCZ__", KLUCZ)
