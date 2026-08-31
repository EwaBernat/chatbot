# -*- coding: utf-8 -*-
import json,sys,html
sys.path.insert(0,'/tmp/bud'); from rejestr import zbuduj
R=zbuduj(); E=html.escape
D,N=R['kaciki']

def kafle(k):
    a=k['paleta']['akcent']; p=k['paleta']['pastel']; o=[]
    for f in k['kafelki']:
        syg=' · '.join(d['sygnatura'] for d in f['druki'])
        nry=f"{f['druki'][0]['nr']:02d}–{f['druki'][-1]['nr']:02d}" if len(f['druki'])>1 else f"{f['druki'][0]['nr']:02d}"
        o.append(f'''      <a class="kafel" href="#" style="--a:{a};--p:{p}">
        <div class="kafel-gora"><span class="kafel-ikona">{f['ikona']}</span><span class="kafel-nr">{nry}</span></div>
        <h3>{E(f['nazwa'])}</h3>
        <p>{E(f['opis'])}</p>
        <div class="kafel-syg">{E(syg)}</div>
      </a>''')
    return '\n'.join(o)

def podpozycje(k):
    o=[f'        <a class="pod" href="#">Wykaz obowiązków</a>',
       f'        <a class="pod" href="#">Kalendarz — terminy</a>']
    for f in k['kafelki']:
        o.append(f'        <a class="pod" href="#">{E(f["nazwa"])}</a>')
    return '\n'.join(o)

def tabela_kafli(k):
    o=[]
    for f in k['kafelki']:
        o.append(f'<tr><td class="c">{f["nr"]:02d}</td><td><b>{f["ikona"]} {E(f["nazwa"])}</b></td>'
                 f'<td><code>{k["trasa"]}/{f["klucz"]}</code></td><td class="c">{len(f["druki"])}</td>'
                 f'<td>{" · ".join(d["sygnatura"] for d in f["druki"])}</td></tr>')
    return '\n'.join(o)

HTML=f'''<meta charset="utf-8">
<title>Kąciki w aplikacji — wdrożenie</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:'Mulish',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;font-size:16px;
    background:#eeeef3;color:#2b2440;line-height:1.55;padding:32px 20px 64px}}
  .ramka{{max-width:1180px;margin:0 auto}}
  .naglowek{{background:linear-gradient(120deg,#3d2566 0%,#4b2d7a 58%,#e0522e 190%);color:#fff;
    border-radius:10px;padding:34px 38px;box-shadow:0 8px 30px rgba(30,20,60,.12)}}
  .naglowek .etyk{{font-size:12px;font-weight:800;letter-spacing:2px;text-transform:uppercase;opacity:.82}}
  .naglowek h1{{font-size:30px;font-weight:800;margin-top:8px;letter-spacing:-.2px}}
  .naglowek p{{margin-top:10px;opacity:.92;max-width:760px}}
  h2{{font-size:22px;font-weight:800;color:#3d2566;margin:38px 0 6px;letter-spacing:-.2px}}
  h2 .num{{display:inline-flex;width:30px;height:30px;border-radius:8px;background:#e0522e;color:#fff;
    font-size:14px;align-items:center;justify-content:center;margin-right:10px;vertical-align:2px}}
  .lead{{color:#5c5470;margin-bottom:18px;max-width:880px}}
  .karta{{background:#fff;border:1px solid #ececf2;border-radius:10px;padding:24px 26px;
    box-shadow:0 2px 10px rgba(30,20,60,.06);margin-bottom:16px}}
  table{{width:100%;border-collapse:collapse;font-size:14px}}
  th{{background:#faf9fb;color:#3d2566;font-weight:800;font-size:12px;letter-spacing:.6px;text-transform:uppercase;
    text-align:left;padding:10px 12px;border-bottom:2px solid #dcdce6}}
  td{{padding:9px 12px;border-bottom:1px solid #ececf2;vertical-align:top}}
  td.c{{text-align:center;font-weight:700;color:#e0522e}}
  code{{font-family:ui-monospace,'SF Mono',Menlo,monospace;font-size:13px;background:#f2f2f7;
    padding:2px 7px;border-radius:8px;color:#3d2566}}
  pre{{background:#2b2440;color:#eae6f3;border-radius:10px;padding:18px 20px;overflow-x:auto;font-size:13px;
    font-family:ui-monospace,'SF Mono',Menlo,monospace;line-height:1.6}}
  pre .k{{color:#f5a97f}} pre .s{{color:#a5d6a7}} pre .c{{color:#9a92b5}}
  .uwaga{{background:#fff6f2;border:1px solid #f6cdb9;border-left:4px solid #e0522e;border-radius:10px;
    padding:16px 20px;margin:14px 0}}
  .uwaga b{{color:#c0410f}}
  .ok{{background:#f1f8f2;border:1px solid #cbe5d0;border-left:4px solid #2E7D46;border-radius:10px;padding:16px 20px;margin:14px 0}}
  .ok b{{color:#2E7D46}}
  /* ——— podgląd powłoki ——— */
  .powloka{{display:grid;grid-template-columns:300px 1fr;border-radius:10px;overflow:hidden;
    box-shadow:0 8px 30px rgba(30,20,60,.12);background:#fff;margin-top:8px}}
  .sidebar{{background:linear-gradient(180deg,#4b2d7a,#3d2566);padding-bottom:8px;min-width:0}}
  .sb-glowa{{padding:22px 20px 18px;display:flex;align-items:center;gap:12px;
    border-bottom:1px solid rgba(255,255,255,.1)}}
  .sb-logo{{width:40px;height:40px;border-radius:8px;background:rgba(255,255,255,.12);display:flex;
    align-items:center;justify-content:center;font-size:19px}}
  .sb-nazwa{{color:#fff;font-size:16px;font-weight:800;line-height:1.2}}
  .sb-pod{{color:rgba(255,255,255,.75);font-size:12px;font-weight:700;letter-spacing:.6px}}
  .sb-lista{{padding:10px 10px 0}}
  .poz{{display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:8px;
    color:rgba(255,255,255,.75);font-size:16px;font-weight:600;cursor:default}}
  .poz .ik{{width:18px;text-align:center;font-size:15px;opacity:.85}}
  .poz.akt{{color:#fff;font-weight:700}}
  .poz .strz{{margin-left:auto;opacity:.6;font-size:12px}}
  .poz{{white-space:nowrap}}
  .poz.nowa{{padding-right:8px}}
  .poz.nowa{{color:#fff;font-weight:700}}
  .poz.nowa::after{{content:"NOWE";margin-left:auto;background:#e0522e;color:#fff;font-size:10px;
    font-weight:800;letter-spacing:.8px;padding:2px 7px;border-radius:8px}}
  .pod{{display:block;padding:8px 10px 8px 38px;border-radius:8px;color:rgba(255,255,255,.75);
    font-size:16px;font-weight:500;text-decoration:none;margin-bottom:1px}}
  .pod:first-child{{background:rgba(255,255,255,.14);color:#fff;font-weight:700}}
  .prawa{{background:#eeeef3;display:flex;flex-direction:column}}
  .head{{background:#faf9fb;border-bottom:1px solid #ececf2;padding:14px 22px;display:flex;
    align-items:center;gap:14px}}
  .head .tryb{{font-size:12px;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:#8b83a3}}
  .head .tyt{{font-size:16px;font-weight:800;color:#2b2440}}
  .head .szukaj{{margin-left:auto;background:#f2f2f7;border-radius:8px;height:35px;width:300px;
    display:flex;align-items:center;padding:0 12px;gap:8px;color:#9a92b5;font-size:14px;font-weight:500;
    white-space:nowrap;overflow:hidden}}
  .head .cta{{background:#e0522e;color:#fff;border-radius:8px;height:35px;display:flex;align-items:center;
    padding:0 16px;font-size:15px;font-weight:700}}
  .sub{{background:#faf9fb;border-bottom:1px solid #ececf2;padding:10px 22px;display:flex;gap:14px;
    align-items:center;font-size:14px;font-weight:600;color:#5b4f86}}
  .sub .sep{{width:1px;height:16px;background:#dcdce6}}
  .plansza{{padding:24px 22px 30px}}
  .siatka{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
  .kafel{{display:block;text-decoration:none;color:inherit;background:#fff;border-radius:10px;
    padding:18px 20px 16px;border:1px solid #ececf2;
    box-shadow:3px 2px 8px color-mix(in srgb,var(--a) 24%,transparent),
               3px 8px 20px color-mix(in srgb,var(--p) 18%,transparent),
               inset 0 1px 0 rgba(255,255,255,.67);
    transition:box-shadow .18s ease, transform .18s ease}}
  .kafel:hover{{transform:translateY(-2px);
    box-shadow:3px 2px 8px color-mix(in srgb,var(--a) 54%,transparent),
               3px 8px 20px color-mix(in srgb,var(--p) 58%,transparent),
               inset 1px 1px 0 color-mix(in srgb,var(--a) 7%,transparent)}}
  .kafel-gora{{display:flex;align-items:center;justify-content:space-between;margin-bottom:10px}}
  .kafel-ikona{{width:38px;height:38px;border-radius:8px;background:var(--p);display:flex;
    align-items:center;justify-content:center;font-size:19px}}
  .kafel-nr{{font-size:12px;font-weight:800;letter-spacing:.8px;color:#fff;background:var(--a);
    padding:3px 9px;border-radius:8px}}
  .kafel h3{{font-size:16px;font-weight:800;color:var(--a);margin-bottom:5px;line-height:1.25}}
  .kafel p{{font-size:13px;color:#6f6a7d;line-height:1.5;min-height:58px}}
  .kafel-syg{{margin-top:10px;padding-top:9px;border-top:1px solid #ececf2;font-size:11px;
    font-weight:700;letter-spacing:.5px;color:#9a92b5}}
  .kroki{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:6px}}
  .krok{{background:#fff;border:1px solid #ececf2;border-radius:10px;padding:16px 18px;
    box-shadow:0 2px 10px rgba(30,20,60,.06)}}
  .krok .n{{width:28px;height:28px;border-radius:8px;background:#3d2566;color:#fff;font-size:14px;
    font-weight:800;display:flex;align-items:center;justify-content:center;margin-bottom:10px}}
  .krok b{{display:block;font-size:15px;color:#3d2566;margin-bottom:4px}}
  .krok span{{font-size:13px;color:#6f6a7d}}
  .pary{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
  .prob{{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:700}}
  .kropka{{width:20px;height:20px;border-radius:6px;border:1px solid rgba(0,0,0,.08)}}
  footer{{margin-top:44px;padding-top:20px;border-top:1px solid #dcdce6;color:#8b83a3;font-size:13px}}
  @media(max-width:1000px){{.powloka{{grid-template-columns:1fr}}.siatka{{grid-template-columns:1fr 1fr}}
    .kroki,.pary{{grid-template-columns:1fr}}}}
</style>
<div class="ramka">
  <div class="naglowek">
    <div class="etyk">EduPlaner 2026 · PCTP Koszalin · dla Arka</div>
    <h1>Kącik dyrektora i kącik nauczyciela w aplikacji</h1>
    <p>Dwie odrębne pozycje menu, każda z własną stroną kafelkową. Ten dokument podaje kolejność,
       podział na kafelki, paletę, trasy i reguły, których nie wolno złamać przy wpinaniu.
       Wartości powłoki są zapisane w stylach tej strony — można je czytać wprost z kodu źródłowego.</p>
  </div>

  <h2><span class="num">1</span>Zasada porządku — cztery kroki w każdym kąciku</h2>
  <p class="lead">Ta sama kolejność obowiązuje w katalogach na dysku, w menu i na stronie kafelkowej.
     Numer druku jest ciągły przez cały kącik i nie zmienia się nigdy — stoi w nazwie pliku, w rejestrze i na kaflu.</p>
  <div class="kroki">
    <div class="krok"><div class="n">1</div><b>Wykaz obowiązków</b><span>Lista czynności — co dyrektor albo nauczyciel ma zrobić, z podstawą prawną przy każdej pozycji.</span></div>
    <div class="krok"><div class="n">2</div><b>Podział wg terminów</b><span>Te same czynności ułożone w kalendarzu roku — od września do sierpnia, z terminami twardymi.</span></div>
    <div class="krok"><div class="n">3</div><b>Podział wg rodzajów</b><span>Dziewięć kafelków w każdym kąciku — to jest strona kafelkowa w aplikacji.</span></div>
    <div class="krok"><div class="n">4</div><b>Druki</b><span>Załączniki w kolejności kafelków, numeracja ciągła. Trasa prowadzi wprost do druku.</span></div>
  </div>

  <h2><span class="num">2</span>Co dochodzi do menu</h2>
  <p class="lead">Dwie nowe pozycje główne. Obie mają po kilkanaście druków, więc obie prowadzą
     do <b>strony kafelkowej</b>, nie wprost do druku. Miejsce w kolejności: po <code>zespol</code>,
     przed pozycjami narzędziowymi — kąciki są materiałem referencyjnym dla roli, nie modułem danych dziecka.</p>
  <div class="powloka">
    <div class="sidebar">
      <div class="sb-glowa"><div class="sb-logo">🎓</div>
        <div><div class="sb-nazwa">EduPlaner 2026</div><div class="sb-pod">PCTP · KOSZALIN</div></div></div>
      <div class="sb-lista">
        <div class="poz"><span class="ik">▤</span>Panel główny</div>
        <div class="poz"><span class="ik">🗂</span>Kartoteka<span class="strz">›</span></div>
        <div class="poz"><span class="ik">📄</span>Metryczka<span class="strz">›</span></div>
        <div class="poz"><span class="ik">🧭</span>WOPF — ocena<span class="strz">›</span></div>
        <div class="poz"><span class="ik">🎯</span>IPET — program<span class="strz">›</span></div>
        <div class="poz"><span class="ik">▶</span>Realizacja<span class="strz">›</span></div>
        <div class="poz"><span class="ik">📊</span>Ewaluacja<span class="strz">›</span></div>
        <div class="poz"><span class="ik">👥</span>Zespół<span class="strz">›</span></div>
        <div class="poz nowa" style="margin-top:6px"><span class="ik">{D['paleta']['ikona']}</span>Kącik dyrektora</div>
{podpozycje(D)}
        <div class="poz nowa" style="margin-top:6px"><span class="ik">{N['paleta']['ikona']}</span>Kącik nauczyciela</div>
        <div class="poz" style="margin-top:6px"><span class="ik">📚</span>Baza wiedzy</div>
        <div class="poz"><span class="ik">🖨</span>Druki</div>
        <div class="poz"><span class="ik">⚙</span>Ustawienia</div>
      </div>
    </div>
    <div class="prawa">
      <div class="head"><span class="tryb">Podgląd</span><span class="tyt">Kącik dyrektora</span>
        <span class="szukaj">🔍 Szukaj druku — sygnatura, nazwa</span><span class="cta">Drukuj</span></div>
      <div class="sub"><span>‹ Wróć: Panel główny</span><span class="sep"></span><span>Kącik dyrektora</span>
        <span class="sep"></span><span style="color:#8b83a3;font-weight:600">9 kafelków · {D['drukow']} druków</span></div>
      <div class="plansza"><div class="siatka">
{kafle(D)}
      </div></div>
    </div>
  </div>

  <h2><span class="num">3</span>Strona kafelkowa kącika nauczyciela</h2>
  <p class="lead">Ten sam układ, własny akcent. Kafelki dziedziczą kolor rodzica — żaden kafel nie ma własnej palety.</p>
  <div class="powloka">
    <div class="sidebar">
      <div class="sb-glowa"><div class="sb-logo">🎓</div>
        <div><div class="sb-nazwa">EduPlaner 2026</div><div class="sb-pod">PCTP · KOSZALIN</div></div></div>
      <div class="sb-lista">
        <div class="poz nowa"><span class="ik">{N['paleta']['ikona']}</span>Kącik nauczyciela</div>
{podpozycje(N)}
      </div>
    </div>
    <div class="prawa">
      <div class="head"><span class="tryb">Podgląd</span><span class="tyt">Kącik nauczyciela</span>
        <span class="szukaj">🔍 Szukaj druku — sygnatura, nazwa</span><span class="cta">Drukuj</span></div>
      <div class="sub"><span>‹ Wróć: Panel główny</span><span class="sep"></span><span>Kącik nauczyciela</span>
        <span class="sep"></span><span style="color:#8b83a3;font-weight:600">9 kafelków · {N['drukow']} druków</span></div>
      <div class="plansza"><div class="siatka">
{kafle(N)}
      </div></div>
    </div>
  </div>

  <h2><span class="num">4</span>Paleta — dwie nowe pozycje do rejestru</h2>
  <p class="lead">Kąciki to nowe pozycje główne, więc potrzebują własnej pary akcent/pastel w
     <code>shared/landing/kolory-modulow.ts</code>. Wartości dobrane tak, żeby nie kolidowały z sześcioma
     istniejącymi modułami ani z pomarańczem akcji.</p>
  <div class="karta">
    <table>
      <thead><tr><th style="width:200px">Pozycja</th><th style="width:150px">Akcent</th><th style="width:150px">Pastel</th><th>Dlaczego ta</th></tr></thead>
      <tbody>
        <tr><td><b>{D['paleta']['ikona']} Kącik dyrektora</b></td>
            <td><span class="prob"><span class="kropka" style="background:{D['paleta']['akcent']}"></span><code>{D['paleta']['akcent']}</code></span></td>
            <td><span class="prob"><span class="kropka" style="background:{D['paleta']['pastel']}"></span><code>{D['paleta']['pastel']}</code></span></td>
            <td>Dolny ton gradientu sidebara — powaga zarządzania, rodzina marki, nie koliduje z fioletem WOPF.</td></tr>
        <tr><td><b>{N['paleta']['ikona']} Kącik nauczyciela</b></td>
            <td><span class="prob"><span class="kropka" style="background:{N['paleta']['akcent']}"></span><code>{N['paleta']['akcent']}</code></span></td>
            <td><span class="prob"><span class="kropka" style="background:{N['paleta']['pastel']}"></span><code>{N['paleta']['pastel']}</code></span></td>
            <td>Jedyna wolna rodzina w palecie — błękit. Odróżnia rolę nauczyciela od dyrektora na pierwszy rzut oka.</td></tr>
      </tbody>
    </table>
  </div>
  <div class="uwaga"><b>To wymaga wpisu u strażnika powłoki.</b> Reguła P6 mówi, że nowe podlandingi
     dziedziczą kolory rodzica i nie mają własnych palet. Kąciki nie są podlandingami — są nowymi pozycjami
     głównymi, więc para akcent/pastel jest tu konieczna. Zgodnie z zasadą „wyjątek zawsze z powodem i datą"
     trzeba to dopisać w sekcji wyjątków wraz z tymi dwoma wierszami. <b>Kafelki wewnątrz kącików palety
     nie mają</b> — dziedziczą akcent rodzica, dokładnie jak każe P6.</div>
  <div class="ok"><b>Efekt 3D bez zmian.</b> Kafelki używają dokładnie tych cieni, co reszta makiet —
     bazowy <code>3px 2px 8px akcent 24%</code> + <code>3px 8px 20px pastel 18%</code> + <code>inset 0 1px 0 biel 67%</code>,
     hover <code>54%</code> / <code>58%</code> / <code>inset 1px 1px 0 akcent 7%</code>. Można je zobaczyć na żywo —
     wystarczy najechać na kafel powyżej.</div>

  <h2><span class="num">5</span>Trasy — kącik dyrektora</h2>
  <div class="karta"><table>
    <thead><tr><th style="width:50px">Nr</th><th style="width:260px">Kafel</th><th style="width:300px">Trasa</th><th style="width:70px">Druki</th><th>Sygnatury</th></tr></thead>
    <tbody>
      <tr><td class="c">—</td><td><b>Wykaz obowiązków</b></td><td><code>{D['trasa']}/wykaz</code></td><td class="c">1</td><td>indeks kącika</td></tr>
      <tr><td class="c">—</td><td><b>Kalendarz — terminy</b></td><td><code>{D['trasa']}/terminy</code></td><td class="c">1</td><td>DK-1</td></tr>
{tabela_kafli(D)}
    </tbody></table></div>

  <h2><span class="num">6</span>Trasy — kącik nauczyciela</h2>
  <div class="karta"><table>
    <thead><tr><th style="width:50px">Nr</th><th style="width:260px">Kafel</th><th style="width:300px">Trasa</th><th style="width:70px">Druki</th><th>Sygnatury</th></tr></thead>
    <tbody>
      <tr><td class="c">—</td><td><b>Wykaz obowiązków</b></td><td><code>{N['trasa']}/wykaz</code></td><td class="c">1</td><td>K-1</td></tr>
      <tr><td class="c">—</td><td><b>Terminarz roku</b></td><td><code>{N['trasa']}/terminy</code></td><td class="c">1</td><td>K-1 · część terminowa</td></tr>
{tabela_kafli(N)}
    </tbody></table></div>

  <h2><span class="num">7</span>Rejestr maszynowy</h2>
  <p class="lead">Nie trzeba przepisywać nic z tej strony. Plik <code>rejestr-kacikow.json</code> leży
     w <code>00_START/</code> każdego kącika i zawiera całą strukturę: kolejność, kafelki, druki z numerami,
     nazwy plików i trasy.</p>
  <pre><span class="c">// 00_START/rejestr-kacikow.json — kształt</span>
{{
  <span class="k">"paleta"</span>: {{ <span class="k">"kacik-dyrektora"</span>: {{ <span class="k">"akcent"</span>: <span class="s">"{D['paleta']['akcent']}"</span>, <span class="k">"pastel"</span>: <span class="s">"{D['paleta']['pastel']}"</span> }}, … }},
  <span class="k">"kaciki"</span>: [{{
    <span class="k">"klucz"</span>: <span class="s">"kacik-dyrektora"</span>, <span class="k">"trasa"</span>: <span class="s">"/kacik-dyrektora"</span>, <span class="k">"drukow"</span>: {D['drukow']},
    <span class="k">"kolejnosc"</span>: [ {{krok 1 wykaz}}, {{krok 2 terminy}}, {{krok 3 kafelki}}, {{krok 4 druki}} ],
    <span class="k">"kafelki"</span>: [{{
      <span class="k">"nr"</span>: 1, <span class="k">"klucz"</span>: <span class="s">"planowanie"</span>, <span class="k">"trasa"</span>: <span class="s">"/kacik-dyrektora/planowanie"</span>,
      <span class="k">"druki"</span>: [{{ <span class="k">"nr"</span>: 1, <span class="k">"sygnatura"</span>: <span class="s">"DW-1"</span>, <span class="k">"plik"</span>: <span class="s">"Kacik_Dyrektora_Plan_Pracy_PCTP"</span>, … }}]
    }}, … ]
  }}, … ]
}}</pre>

  <h2><span class="num">8</span>Czego nie wolno złamać</h2>
  <div class="pary">
    <div class="karta">
      <b style="color:#3d2566;font-size:16px">Powłoka</b>
      <table style="margin-top:10px"><tbody>
        <tr><td style="width:44px"><b>P1</b></td><td>Etykieta menu dociągana do tytułu kafla, nigdy odwrotnie.</td></tr>
        <tr><td><b>P2</b></td><td>Pozycja z kilkoma drukami prowadzi do strony kafelkowej — obie tutaj tak mają.</td></tr>
        <tr><td><b>P3</b></td><td>Kolejność menu wyznacza hierarchię. Zmiana kolejności zmienia kierunek przepływu danych — to nie jest kosmetyka.</td></tr>
        <tr><td><b>P4</b></td><td>Każdy klucz kafla musi istnieć wśród podmodułów tego samego modułu.</td></tr>
        <tr><td><b>P6</b></td><td>Kafelki dziedziczą kolor rodzica — własnych palet nie mają.</td></tr>
        <tr><td><b>P8</b></td><td>Typografia ekranu to Mulish 16 px, etykiety 12 px — nie drobna skala z kartki.</td></tr>
      </tbody></table>
    </div>
    <div class="karta">
      <b style="color:#3d2566;font-size:16px">Druk i dane</b>
      <table style="margin-top:10px"><tbody>
        <tr><td style="width:44px"><b>W1</b></td><td>Druk nie renderuje własnego nagłówka, stopki ani podpisu — niesie je szablon.</td></tr>
        <tr><td><b>W2</b></td><td>Druk nie liczy stron. „Strona X z Y" podaje silnik.</td></tr>
        <tr><td><b>D1</b></td><td>Pola wyboru to dane, nie ozdoba widoku. Zaznaczenie żyjące tylko w stanie widoku jest naruszeniem.</td></tr>
        <tr><td><b>D2</b></td><td>Jeden druk = jeden wiersz, tożsamość to para <code>(recordId, druk)</code>.</td></tr>
        <tr><td><b>D4</b></td><td>Miernik kompletności to <code>[Wyczyść]</code> — sprawdzany w bazie, nie na ekranie.</td></tr>
      </tbody></table>
    </div>
  </div>
  <div class="uwaga"><b>Jedna wartość do sprawdzenia przed wdrożeniem.</b> Gradient sidebara użyty
     w podglądzie powyżej — <code>linear-gradient(180deg,#4b2d7a,#3d2566)</code> — pochodzi z KANON-UI,
     a strażnik powłoki mówi wprost, że <b>w kodzie ta wartość nie występuje</b>. Podgląd traktuj jako opis
     układu i intencji; konkretne wartości powłoki czytaj z <code>shared/menu/sidebar.css</code>
     i <code>styles/foundation/</code>. Konflikt rozstrzyga kod.</div>

  <h2><span class="num">9</span>Co dochodzi w kodzie</h2>
  <div class="karta"><table>
    <thead><tr><th style="width:330px">Plik</th><th>Co dopisać</th></tr></thead>
    <tbody>
      <tr><td><code>shared/rejestr/moduly.ts</code></td><td>Dwa moduły: <code>kacik-dyrektora</code> i <code>kacik-nauczyciela</code>, każdy z 9 podmodułami plus <code>wykaz</code> i <code>terminy</code>. Klucze podmodułów wprost z rejestru.</td></tr>
      <tr><td><code>rejestr/menu.ts</code></td><td>Dwie pozycje główne po <code>zespol</code>. Etykiety 1:1 z tytułami kafli.</td></tr>
      <tr><td><code>shared/landing/kolory-modulow.ts</code></td><td>Dwie pary akcent/pastel z sekcji 4.</td></tr>
      <tr><td><code>data/</code> · treść druków</td><td>{D['drukow']+N['drukow']} druków. Proza wzorcowa, podstawy prawne i legendy należą do <code>data/</code>, nie do bazy.</td></tr>
      <tr><td>warstwa danych druku</td><td>Każdy druk dostaje wiersz i zapis wszystkich pól, łącznie z zaznaczeniami i skalami.</td></tr>
      <tr><td>strażnicy — sekcja wyjątków</td><td>Wpis o dwóch nowych parach kolorów, z powodem i datą.</td></tr>
    </tbody>
  </table></div>

  <h2><span class="num">10</span>Dualizm — czego brakuje w drukach zbierających liczby</h2>
  <p class="lead">Reguła mówi: druk zbierający cokolwiek policzalnego dostaje wynik i wykres,
     <b>nawet gdy papier ich nie ma</b>. W obu kącikach są druki, które zbierają skale i zaznaczenia,
     a nie mają warstwy wyniku. To zadanie wdrożeniowe, nie poprawka w druku.</p>
  <div class="karta"><table>
    <thead><tr><th style="width:110px">Druk</th><th style="width:250px">Co zbiera</th><th>Wynik i wykres do dołożenia</th></tr></thead>
    <tbody>
      <tr><td><b>DN-4, DN-5</b></td><td>oceny w skali 1–4 w ośmiu obszarach</td><td>średnia z kwalifikacją wg progów, słupki i radar po obszarach</td></tr>
      <tr><td><b>DP-4</b></td><td>zaznaczenia efektywności pomocy</td><td>udział zaznaczonych w grupie, słupki po formach pomocy</td></tr>
      <tr><td><b>DB-3</b></td><td>ocena ryzyka M / Ś / D</td><td>rozkład ryzyka, wykaz pozycji „duże" na górze</td></tr>
      <tr><td><b>O-1, O-5</b></td><td>skale obserwacji i gotowości</td><td>profil obszarów, porównanie diagnozy wstępnej z końcową</td></tr>
      <tr><td><b>Z-3</b></td><td>ocena postępów</td><td>trajektoria w czasie dla dziecka</td></tr>
      <tr><td><b>B-4</b></td><td>zdarzenia i funkcje zachowania</td><td>rozkład zdarzeń, funkcja dominująca</td></tr>
    </tbody>
  </table></div>

  <footer>EduPlaner 2026 · PCTP Koszalin · autorka Mirosława Ewa Jurczyszyn ·
    dokument wdrożeniowy z 31 sierpnia 2026 r. · {D['drukow']+N['drukow']} druków w 18 kafelkach</footer>
</div>'''
open('/tmp/bud/WDROZENIE_KACIKI_W_APLIKACJI.html','w',encoding='utf-8').write(HTML)
print('zapisano · znaków',len(HTML))
