# -*- coding: utf-8 -*-
"""Przykładowy konspekt zajęć do tabeli FBA-T — wzór druku KC-3 z banku KPOF.

Ten sam układ, co konspekty w banku celów SMART: nagłówek z metryką dziecka,
sekcje I–VII, tabela przebiegu w parach „czynność nauczyciela (N) / oczekiwana
reakcja dziecka (D)", trzy modyfikacje w kolorach oceny i materiał do wydruku.
Nauczyciel czyta konspekty seriami, więc identyczna kolejność sekcji jest tu
ważniejsza niż pomysłowość układu — oko wie, gdzie szukać przebiegu.

Konspekt siedzi przy komórce tak jak w banku: klika się cel w wierszu I.1
wersji A, a otwiera się scenariusz z **wyróżnionym klikniętym poziomem**.
Cel edukacyjny czyta się **na żywo z tabeli**, nie kopiuje do konspektu —
po poprawce w `dane_poziomy.py` konspekt nie zaczyna żyć własną wersją celu.

Wskaźnik I.1 („zachowanie pojawia się, gdy dziecko ma wykonać trudne lub
nielubiane zadanie") wybrany jako pierwszy, bo to najczęstszy wyzwalacz
w arkuszu ABC i zarazem ten, przy którym najłatwiej wzmocnić ucieczkę:
zwolnienie z zadania po zachowaniu trudnym uczy, że zachowanie działa.

Materiał do wydruku jest w rodzaju `pola` — puste ramki z etykietami, bez
rysunków. To nie jest brak: symbol do tych kart **bierze się z biblioteki
EduPlaner**, żeby dziecko widziało ten sam obrazek tu, na tablicy AAC i w planie
dnia. Symbol dorysowany pod jeden konspekt przestaje być słowem.
"""

import html

KONSPEKT = dict(
    wersja="A", wiek="3–4 lata", wskaznik="I.1", funkcja="I · Ucieczka / unikanie",
    nr="FBA A-I.1",
    tytul="Jeden krok i już zaczynam",
    podtytul="Rozpoczynanie trudnego zadania z kartą pierwszego kroku",
    sfera="FUNKCJA I · UCIECZKA / UNIKANIE · zachowanie zastępcze: rozpoczęcie zadania "
          "(ICF d210·d240 · PP 2.6·2.11)",
    czas="15 min", forma="para z nauczycielem albo mała grupa (3 dzieci)", cykl="4× w tygodniu",
    rodzaj="Zajęcia rozwijające kompetencje emocjonalno-społeczne · realizacja planu PBS",

    ter="Dziecko weźmie do ręki pierwszy element trudnego zadania w ciągu minuty od podania "
        "karty pierwszego kroku, bez odchodzenia od stolika, w 3 z 5 sytuacji, w ciągu 4 tygodni.",
    ter_smart=[
        ("S", "Bierze pierwszy element i kładzie go przed sobą — to widać, nie trzeba oceniać chęci."),
        ("M", "Minuta od podania karty; 3 z 5 sytuacji."),
        ("A", "Karta pokazuje jedną czynność, nie całe zadanie — dziecko nie musi ogarniać całości."),
        ("R", "Ucieczka zaczyna się przed pierwszym ruchem; kto zaczął, zwykle kończy."),
        ("T", "Ewaluacja po 4 tygodniach (Poziom III)."),
    ],
    ter_kryt="Rejestr ABC — kolumna A: podanie trudnego zadania · 5 sytuacji w tygodniu.",

    pomoce=[
        "karta „pierwszy krok” — jedno pole na symbol czynności (arkusz poniżej)",
        "karta „najpierw — potem” z symbolem zadania i symbolem zabawy",
        "karta „przerwa” w zasięgu ręki dziecka przez całe zajęcia",
        "zadanie rozłożone na trzy pojemniki, po jednym elemencie w każdym",
        "minutnik piaskowy (1 minuta) — czas widoczny, nie odliczany słowem",
    ],
    metody=[
        "podanie zadania w częściach (rozłożenie na pojemniki)",
        "podpowiedź wzrokowa zamiast ponaglania słownego",
        "wzmocnienie za podjęcie, nie za wynik",
        "wygaszanie ucieczki: zadanie zostaje na stoliku także po zachowaniu trudnym",
        "modelowanie pierwszego ruchu przez nauczyciela",
    ],
    przebieg=[
        ("N — kładzie przed dzieckiem kartę „najpierw — potem” i nazywa oba symbole.",
         "D — patrzy na kartę i wskazuje symbol zabawy, która będzie potem."),
        ("N — stawia trzy pojemniki i odsuwa dwa, zostawiając pierwszy.",
         "D — widzi jedną czynność zamiast całego zadania."),
        ("N — podaje kartę „pierwszy krok” i odwraca minutnik.",
         "D — bierze pierwszy element do ręki w czasie minutnika."),
        ("N — nazywa to, co dziecko zrobiło: „zacząłeś”, i przysuwa drugi pojemnik.",
         "D — sięga po kolejny element bez nowego polecenia."),
        ("N — po ostatnim pojemniku pokazuje symbol zabawy z karty „potem”.",
         "D — kończy zadanie i przechodzi do zabawy, którą wcześniej wskazało."),
    ],
    mod3=[
        "nauczyciel bierze pierwszy element razem z dzieckiem, ręka na ręce",
        "jeden pojemnik zamiast trzech — zadanie skrócone do jednej czynności",
        "minutnik odłożony: liczy się podjęcie, nie czas",
    ],
    mod2=[
        "karta pierwszego kroku leży na stoliku, nie jest podawana do ręki",
        "trzy pojemniki widoczne od początku, odsuwane po kolei",
    ],
    mod1=[
        "dziecko samo układa kolejność pojemników przed startem",
        "polecenie słowne bez karty; karta zostaje w zasięgu na wypadek trudności",
        "dwa zadania po sobie: łatwe i trudne, bez przerwy między nimi",
    ],
    wskazowka="Nie zabieraj zadania po zachowaniu trudnym i nie kończ zajęć wcześniej — "
              "to jest dokładnie ta nagroda, której zachowanie szuka. Zadanie zostaje na stoliku, "
              "a dziecko dostaje przerwę na prośbę, nie za krzyk.",
)

# ——— materiał do wydruku ———————————————————————————————————————————————
# Rodzaj `pola`: puste ramki z etykietami. Symbol wkleja się z biblioteki
# EduPlaner — ten sam, który dziecko widzi na tablicy AAC i w planie dnia.
ARKUSZ = dict(
    tytul="Karty do zajęć „Jeden krok i już zaczynam”",
    wstep="Wytnij karty wzdłuż linii. W puste pola wklej symbole z biblioteki EduPlaner — "
          "te same, których dziecko używa na tablicy AAC i w planie dnia. Symbol, który "
          "zmienia wygląd między materiałami, przestaje być dla dziecka słowem.",
    karty=[
        ("Najpierw", "symbol zadania — ten, który dziecko ma wykonać"),
        ("Potem", "symbol zabawy albo aktywności po zadaniu"),
        ("Pierwszy krok", "symbol jednej czynności: weź, włóż, połóż"),
        ("Przerwa", "symbol przerwy — leży przy dziecku przez całe zajęcia"),
    ],
    pasek=["1 · biorę", "2 · wkładam", "3 · gotowe"],
)


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
.ktitle{margin:14px 0 12px}
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

/* arkusz do wydruku — rodzaj „pola”: ramki z etykietami, symbol z biblioteki */
.zal{border-top:2px dashed var(--line-2); margin-top:16px; padding-top:14px}
.zal-head{display:flex; align-items:center; gap:10px; margin-bottom:9px}
.zal-head .kp{background:var(--accent); color:var(--on-accent); border-radius:999px; padding:4px 12px;
  font:700 9px/1 "DM Sans",Arial,sans-serif; letter-spacing:.1em; text-transform:uppercase}
.zal h4{margin:0; font-size:14px; color:var(--ink)}
.zal-wstep{font-size:10.5px; color:var(--szary); line-height:1.5; margin:0 0 11px}
.zal-siatka{display:grid; grid-template-columns:1fr 1fr; gap:11px}
.zal-karta{border:2px dashed var(--line-2); border-radius:10px; padding:11px 12px 13px; text-align:center}
.zal-karta .pole{height:118px; border:1px solid var(--line); border-radius:8px; background:var(--soft);
  display:grid; place-items:center; color:var(--szary); font-size:9px; letter-spacing:.08em;
  text-transform:uppercase; padding:0 10px; margin-bottom:8px}
.zal-karta b{display:block; font-size:15px; color:var(--ink); letter-spacing:.04em}
.zal-karta span{font-size:9px; color:var(--szary)}
.zal-pasek{display:grid; grid-template-columns:repeat(3,1fr); gap:9px; margin-top:11px}
.zal-pasek div{border:2px dashed var(--line-2); border-radius:10px; padding:9px; text-align:center}
.zal-pasek .pole{height:74px; border:1px solid var(--line); border-radius:8px; background:var(--soft); margin-bottom:6px}
.zal-pasek b{font-size:11px; color:var(--ink)}
"""

SKRYPT = """
/* Konspekt otwiera się z komórki celu — tak jak w banku KPOF. Cel edukacyjny
   czytamy z tabeli na żywo: poprawka w danych nie zostawia w konspekcie
   nieaktualnej kopii celu. */
(function(){
  const modal = document.getElementById('kon-fba-1');
  if (!modal) return;
  const POZ = {p3:'Poziom III', p2:'Poziom II', p1:'Poziom I'};

  function pokaz(lvl){
    const kom = document.querySelectorAll('#w-A tr[data-wsk="I.1"] td.g');
    const kol = {p3:0, p2:1, p1:2}[lvl] ?? 0;
    const c = kom[kol];
    modal.querySelector('#kon-cel').textContent = c ? c.querySelector('.tresc').textContent : '';
    modal.querySelector('#kon-kryt').textContent = c ? c.querySelector('.ram').textContent : '';
    modal.querySelector('#kon-poz').textContent = POZ[lvl];
    modal.querySelector('#kon-poz').className = 'klvl ' + lvl;
    modal.querySelectorAll('.kmod').forEach(m => m.classList.toggle('wyb', m.dataset.mod === lvl));
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    modal.querySelector('.kclose').focus();
  }
  function zamknij(){ modal.classList.remove('open'); document.body.style.overflow = ''; }

  /* Faza przechwytywania: komórka ma własny nasłuch, a delegacja na dokumencie
     w fazie bąbelkowania odpalałaby się po nim. */
  document.addEventListener('click', e => {
    const td = e.target.closest('td.g.haskon');
    if (td) { e.preventDefault(); pokaz(td.dataset.lvl); return; }
    if (e.target.closest('[data-zamknij]') || e.target === modal) zamknij();
  }, true);
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && modal.classList.contains('open')) zamknij();
    const td = e.target.closest && e.target.closest('td.g.haskon');
    if (td && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); pokaz(td.dataset.lvl); }
  });
  modal.querySelector('[data-druk]').addEventListener('click', () => {
    document.documentElement.classList.add('print-konspekt');
    const gotowe = () => { document.documentElement.classList.remove('print-konspekt');
      window.removeEventListener('afterprint', gotowe); };
    window.addEventListener('afterprint', gotowe);
    window.print();
  });
})();
"""


def _arkusz():
    karty = "".join(
        f'<div class="zal-karta"><div class="pole">miejsce na symbol<br>z biblioteki EduPlaner</div>'
        f'<b>{_e(t)}</b><span>{_e(o)}</span></div>' for t, o in ARKUSZ["karty"])
    pasek = "".join(f'<div><div class="pole"></div><b>{_e(x)}</b></div>' for x in ARKUSZ["pasek"])
    return f'''    <section class="zal">
      <div class="zal-head"><span class="kp">Materiał do wydruku · A4</span><h4>{_e(ARKUSZ["tytul"])}</h4></div>
      <p class="zal-wstep">{_e(ARKUSZ["wstep"])}</p>
      <div class="zal-siatka">{karty}</div>
      <div class="zal-pasek">{pasek}</div>
    </section>'''


def modal():
    K = KONSPEKT
    ter = "".join(f'<li><b>{L}</b><span>{_e(t)}</span></li>' for L, t in K["ter_smart"])
    pom = "".join(f'<li>{_e(x)}</li>' for x in K["pomoce"])
    met = "".join(f'<li>{_e(x)}</li>' for x in K["metody"])
    prz = "".join(f'<tr><td class="lp">{i}</td><td>{_e(n)}</td><td>{_e(d)}</td></tr>'
                  for i, (n, d) in enumerate(K["przebieg"], 1))
    mods = ""
    for kod, klasa, etykieta in (("p3", "m3", "Poziom III · Czerwona"),
                                 ("p2", "m2", "Poziom II · Żółta"),
                                 ("p1", "m1", "Poziom I · Zielona")):
        li = "".join(f'<li>{_e(x)}</li>' for x in K[{"p3": "mod3", "p2": "mod2", "p1": "mod1"}[kod]])
        mods += f'<div class="kmod {klasa}" data-mod="{kod}"><b>{etykieta}</b><ul class="klista">{li}</ul></div>'
    return f'''<div class="kmodal" id="kon-fba-1" role="dialog" aria-modal="true"
  aria-label="Konspekt zajęć: {_e(K["tytul"])}">
  <div class="kcard">
    <button class="kclose" data-zamknij aria-label="Zamknij konspekt" title="Zamknij (Esc)">✕</button>
    <div class="khead">
      <span class="mark">PCTP</span>
      <div>
        <div class="kw">EduPlaner 2026</div>
        <div class="ks">Konspekt · funkcja {_e(K["funkcja"])} · wersja {K["wersja"]} · {_e(K["wiek"])}
          · wskaźnik {K["wskaznik"]}</div>
      </div>
      <span class="kpill">Konspekt {_e(K["nr"])}</span>
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
      <div class="field"><b>Poziom wsparcia</b><span class="klvl p3" id="kon-poz">Poziom III</span></div>
    </div>

    <div class="ksec"><span class="sq">I</span><h4>Cel SMART</h4><span class="line"></span></div>
    <div class="kcele">
      <div class="kcel edu">
        <div class="kchead">Cel edukacyjny — z tabeli FBA-T, wg klikniętego poziomu</div>
        <div class="ktresc" id="kon-cel"></div>
        <div class="kkryt"><b>Kryterium:</b> <span id="kon-kryt"></span></div>
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
    <p class="kkurs">Cztery karty i pasek kolejności, A4 pionowo. Symbole wkleja się z biblioteki
      EduPlaner — te same, których dziecko używa na tablicy AAC i w planie dnia.</p>
{_arkusz()}

    <div class="kfoot">
      <button class="chipbtn" data-zamknij>✕ Zamknij i wróć do tabeli</button>
      <button class="chipbtn mocny" data-druk>Drukuj konspekt A4</button>
    </div>
    <p class="kesc">zamkniesz też klawiszem <b>Esc</b> albo kliknięciem w tło poza kartą</p>
  </div>
</div>'''
