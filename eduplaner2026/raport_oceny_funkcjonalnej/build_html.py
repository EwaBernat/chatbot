#!/usr/bin/env python3
# Buduje Raport_Oceny_Funkcjonalnej.html z: styles.css + part1_pages.html + raport_data.json
import json, re, html
D = json.load(open('raport_data.json', encoding='utf-8'))
CSS = open('styles.css', encoding='utf-8').read()
P1 = open('part1_pages.html', encoding='utf-8').read()

EXTRA_CSS = '''
  /* ---- rozszerzenia: części II–III ---- */
  .partband.p3 .badge{background:var(--purple)}
  .cbl{display:grid;grid-template-columns:1fr 1fr;gap:5px 14px;font-size:10.5px;margin:6px 0 10px}
  .cbl span{display:flex;align-items:center;gap:7px}
  .cbl .cb{margin:0}
  .cb.on{background:var(--orange);border-color:var(--orange);position:relative}
  .cb.on::after{content:"";position:absolute;left:4px;top:1px;width:4px;height:8px;border:solid #fff;border-width:0 2px 2px 0;transform:rotate(45deg)}
  .voice{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:8px 0}
  .voice .box{padding:8px 12px 10px} .voice .box p{margin:0;font-size:11px;line-height:1.5;font-style:italic;color:var(--ink)}
  .voice .box.wide{grid-column:1/-1}
  .mood{display:flex;gap:14px;align-items:center;margin:6px 0 10px;font-size:9.5px;color:var(--muted)}
  .mood div{display:flex;flex-direction:column;align-items:center;gap:3px}
  .mood i{width:20px;height:20px;border-radius:50%;display:block;border:2px solid transparent}
  .mood .sel i{outline:2px solid var(--orange);outline-offset:2px}
  .lvlbox{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:8px 0 12px}
  .lvlbox > div{border:1px solid var(--line);border-radius:8px;padding:10px 12px;display:grid;grid-template-columns:18px 1fr;gap:8px;align-items:start}
  .lvlbox > div.sel{background:var(--orangeMist);border-color:var(--orange)}
  .lvlbox h4{margin:0 0 3px;font-size:11.5px;color:var(--purple);font-weight:800}
  .lvlbox p{margin:0;font-size:10px;color:var(--muted);line-height:1.4}
  .kv{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:8px 0}
  .kv div{background:var(--lav);border-radius:8px;padding:8px 10px}
  .kv .l{font-size:8px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--lav-text)}
  .kv .v{font-size:11px;font-weight:800;color:var(--purple);margin-top:2px;line-height:1.3}
  .just{text-align:justify;font-size:11px;line-height:1.6;margin:6px 0}
  ul.tick{margin:4px 0 0;padding-left:0;list-style:none;font-size:11px;line-height:1.5}
  ul.tick li{padding-left:16px;position:relative;margin-bottom:3px}
  ul.tick li::before{content:"✓";position:absolute;left:0;color:var(--green);font-weight:800}
  .status-pill{display:inline-block;font-size:9px;font-weight:800;padding:2px 8px;border-radius:999px;white-space:nowrap}
  .status-pill.done{background:#E6F4EC;color:var(--green)} .status-pill.now{background:#FBF1DC;color:#9A6A0A} .status-pill.plan{background:var(--lav);color:var(--purple)}
  .ref-pill{display:inline-block;font-size:9px;font-weight:800;color:var(--orange);background:var(--orangeMist);padding:2px 7px;border-radius:4px;white-space:nowrap}
  .signbox{border:1px dashed var(--line);border-radius:8px;padding:8px 12px;font-size:10.5px;color:var(--muted);margin-top:8px}
  .signbox b{color:var(--purple)}
  table.grid.small td{font-size:9.6px;padding:6px 8px;line-height:1.4} table.grid.small th{padding:6px 8px}
  table.grid.tight td{padding:6px 9px}
  .hours.tight .stat{padding:6px 10px} .hours.tight .stat .v{font-size:14px}
  .varbox{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:8px 0 10px}
  .varbox > div{border:1px solid var(--line);border-radius:8px;padding:9px 12px;font-size:10.5px;line-height:1.5;display:grid;grid-template-columns:22px 1fr;gap:8px;align-items:start}
  .varbox .tag9{font-size:10px;padding:2px 0;width:22px;text-align:center;border-radius:4px;color:#fff;font-weight:800}
  .varbox b{color:var(--purple)}
  table.grid td.ok{color:var(--green);font-weight:800} table.grid td.no{color:var(--red);font-weight:800}
  .rek{display:grid;grid-template-columns:1fr 1fr;gap:5px 14px;font-size:10.5px;margin:6px 0 8px}
  .rek span{display:flex;align-items:flex-start;gap:7px}
  .lawref{display:inline-block;font-size:9px;font-weight:700;color:var(--purple);background:var(--lav);border-radius:4px;padding:3px 9px;margin:-6px 0 10px}
  table.grid td.act{font-weight:800;color:var(--purple)} table.grid td.dz{white-space:nowrap;color:var(--orange);font-weight:800;font-size:9.5px}
  .flow5{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin:8px 0 12px}
  .flow5 > div{border:1px solid var(--line);border-radius:8px;padding:8px 10px;position:relative}
  .flow5 .p{font-size:8px;font-weight:800;letter-spacing:.12em;color:var(--orange)}
  .flow5 h4{margin:2px 0 2px;font-size:11px;color:var(--purple);font-weight:800}
  .flow5 p{margin:0;font-size:9.5px;color:var(--muted);line-height:1.35}
  .flow5 > div:not(:last-child)::after{content:"›";position:absolute;right:-8px;top:36%;color:var(--orange);font-weight:800;background:#fff}
'''

pages = []  # list of (name, inner_html)
def hdr(cap):
    return f'''  <div class="hdr">
    <div class="l"><div class="logo">PCTP</div><div><div class="name">EduPlaner 2026</div><div class="cap">Raport Oceny Funkcjonalnej · {cap}</div></div></div>
    <div class="r"><span class="pill">Raport · 2026</span><div class="cap">Dokument dla rodzica · 2026</div></div>
  </div>
  <div class="fields">
    <div class="field"><label>Dotyczy dziecka</label><span></span></div>
    <div class="field"><label>Grupa / klasa</label><span></span></div>
    <div class="field"><label>Data</label><span></span><i class="r">r.</i></div>
  </div>
'''
def sec(n, title, law=None): return f'  <div class="sec"><span class="n">{n}</span><h2>{title}</h2></div>\n'+(f'  <div class="lawref">§ Podstawa prawna: {law}</div>\n' if law else '')
def sub(tag, title, note='', color='var(--orange)'):
    return f'  <div class="sub9" style="--c:{color}"><span class="tag9">{tag}</span><h3>{title}</h3>{"<small>· "+note+"</small>" if note else ""}</div>\n'
def lead(ref, text): return f'  <p class="lead2">{("<b>"+ref+"</b> ") if ref else ""}{text}</p>\n'
def cb(on=False): return f'<i class="cb{" on" if on else ""}"></i>'
def status(): return '<div class="st"><span><i class="cb"></i>wdrożone</span><span><i class="cb"></i>w trakcie</span><span><i class="cb"></i>planowane</span></div>'
def page(name, cap, body, cls='', pid=''):
    pages.append((name, f'<section class="page {cls}"{(" id="+chr(34)+pid+chr(34)) if pid else ""}>\n'+hdr(cap)+body))
def band(part, h, sub_):
    cls = ' p3' if part=='III' else ''
    return f'''  <div class="partband{cls}">
    <span class="badge">Raport Oceny Funkcjonalnej dziecka / ucznia · Część {part}</span>
    <h2>{h}</h2>
    <div class="sub">{sub_}</div>
  </div>
'''

# ---------- 4 ----------
s=D['s4']; b=band('II','Wyniki oceny funkcjonalnej','obserwacja w placówce · wyniki liczbowe · arkusze specjalistyczne · głos dziecka · analiza · decyzja Zespołu')
b+=sec(4, s['title'], s.get('law'))+lead(s['ref'],s['lead'])
b+='  <table class="grid">\n    <tr><th>Obszar obserwacji</th><th class="plus">✓ Mocne strony, zasoby i uzdolnienia</th><th class="minus">▸ Trudności, ograniczenia i bariery</th></tr>\n'
b+=''.join(f'    <tr><td class="area">{a}</td><td class="plus">{x}</td><td class="minus">{y}</td></tr>\n' for a,x,y in s['rows'])+'  </table>\n'
page('Funkcjonowanie','Część II · Funkcjonowanie w placówce',b)

# ---------- 5 ----------
s=D['s5']; b=sec(5, s['title'], s.get('law'))+lead(s['ref'],s['lead'])
b+='''  <div class="switch">
    <span class="t">Narzędzie bazowe</span>
    <label><input type="radio" name="tool" value="kpof"> Przedszkole · KPOF <small>· bez stenów</small></label>
    <label><input type="radio" name="tool" value="kszof" checked> Szkoła · KSzOF <small>· ze stenami</small></label>
  </div>
'''
b+=f'''  <div class="stats">
    <div class="stat"><div class="l">Narzędzie bazowe</div><div class="v"><span class="only-kpof">KPOF <small>przedszkole</small></span><span class="only-kszof">KSzOF <small>szkoła</small></span></div></div>
    <div class="stat"><div class="l">Punkty surowe</div><div class="v">{s['punkty']} <small>/ {s['punktyMax']} pkt</small></div></div>
    <div class="stat"><div class="l">Średnia</div><div class="v">Śr: {s['srednia']} <small>w skali 0–5</small></div></div>
    <div class="stat warn"><div class="l">Ogólny poziom wsparcia</div><div class="v">{s['poziom']} <small>{s['poziomOpis']}</small></div></div>
  </div>
  <table class="grid">
    <tr><th>Kod</th><th>Domena ICF</th><th>Punkty / śr.</th><th class="sten">Sten <small style="font-weight:600">(KSzOF)</small></th><th>Poziom wsparcia</th><th>Wskaźnik funkcjonalny</th></tr>
'''
for k,n,sr,pk,st,lv,ln,w in s['dom']:
    b+=f'    <tr><td class="code">{k}</td><td><b>{n}</b></td><td class="num"><div class="meter"><i style="--w:{int(sr/5*100)}%"></i><span>Śr: {str(sr).replace(".",",")} ({pk} pkt)</span></div></td><td class="num sten">Sten {st}</td><td><span class="lvl l{lv}">Poziom {lv} · {ln}</span></td><td>{w}</td></tr>\n'
b+=f'''  </table>
  <div class="legend"><span>Pasek: średnia w skali 0–5</span><span><span class="lvl l1">Poziom 1 · Niski</span></span><span><span class="lvl l2">Poziom 2 · Średni</span></span><span><span class="lvl l3">Poziom 3 · Wysoki</span></span></div>
  <p class="stnote"><b>Zasada:</b> <span class="only-kpof">{s['zasadaKpof']}</span><span class="only-kszof">{s['zasadaKszof']}</span></p>
'''
page('Wyniki liczbowe','Część II · Wyniki liczbowe',b,'kszof','sek5')

# ---------- 6 ----------
s=D['s6']; b=sec(6, s['title'], s.get('law'))+lead('',s['lead'])
for c,t,parts,rec in s['cards']:
    txt=''.join((f'<b>{x}</b>' if bold else x) for x,bold in parts)
    b+=f'  <div class="res" style="--c:var(--{c})"><h4>{t}</h4><p>{txt}</p>'+(f'<div class="rec"><b>Zalecenie:</b> {rec}</div>' if rec else '')+'</div>\n'
page('Wyniki arkuszy','Część II · Wyniki arkuszy specjalistycznych',b)

# ---------- 7 Mój głos ----------
s=D['s7']; b=sec(7, s['title'], s.get('law'))+lead('',s['lead'])
b+='  <div class="lbl" style="font-size:8.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--purple)">Sposób pozyskania głosu dziecka – zaznaczono</div>\n  <div class="cbl">'+''.join(f'<span>{cb(on)}{t}</span>' for t,on in s['sposoby'])+'</div>\n'
b+='  <div class="voice">\n'+''.join(f'    <div class="box{" wide" if i==3 else ""}" style="--c:var(--{c})"><div class="lbl">{t}</div><p>{v}</p></div>\n' for i,(c,t,v) in enumerate(s['pola']))+'  </div>\n'
b+='  <div class="lbl" style="font-size:8.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--purple)">Co mi najbardziej pomaga – zaznaczono</div>\n  <div class="cbl">'+''.join(f'<span>{cb(on)}{t}</span>' for t,on in s['pomaga'])+'</div>\n'
cols=['#2E9D52','#7EB800','#DFA22E','#E77309','#BF382A']
b+='  <div class="lbl" style="font-size:8.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--purple)">Jak się dziś czuję – wskazanie dziecka</div>\n  <div class="mood">'+''.join(f'<div class="{"sel" if i==s["nastrojWybor"] else ""}"><i style="background:{cols[i]}"></i>{n}</div>' for i,n in enumerate(s['nastroj']))+'</div>\n'
b+=f'  <div class="box" style="--c:var(--blue)"><div class="lbl">Preferowany sposób komunikacji dziecka i wskazówki do rozmowy</div><p class="just" style="margin:0">{s["komunikacja"]}</p></div>\n'
b+=f'  <p class="stnote"><b>Podstawa.</b> {s["podstawa"]}</p>\n'
page('Mój głos','Część II · Mój głos',b)

# ---------- 8 ----------
s=D['s8']; b=sec(8, s['title'], s.get('law'))+lead(s['ref'],s['lead'])
b+='  <table class="grid">\n    <tr><th>Rodzaj wsparcia</th><th>Zakres wdrożonych działań i metody</th><th class="plus">Efektywność i obserwowane zmiany</th></tr>\n'
b+=''.join(f'    <tr><td class="area">{a}</td><td>{x}</td><td class="plus">{y}</td></tr>\n' for a,x,y in s['rows'])+'  </table>\n'
b+='  <div class="parent"><b>Informacja dla rodzica.</b> Wyniki z sekcji 4–8 są podstawą analizy (sekcja 9) i decyzji Zespołu o poziomie wsparcia (sekcja 10). Część III opisuje, jak placówka zorganizuje wsparcie w tym roku szkolnym.</div>\n'
page('Podjęte działania','Część II · Działania dotychczas podjęte',b)

# ---------- 9 (2 strony) ----------
s=D['s9']
thead='  <table class="grid">\n    <tr><th>Domena ICF</th><th>Opis funkcjonowania i bariery</th><th style="color:var(--orange)">Cel na rok szkolny – co ma się zmienić</th></tr>\n'
def rows9(sel): return ''.join(f'    <tr><td class="area">{n}<br><span style="color:var(--orange);font-size:9px">{k}</span></td><td>{d}</td><td><ul class="tick" style="margin:0">'+''.join(f'<li>{x}</li>' for x in r)+'</ul></td></tr>\n' for k,n,d,r in sel)
page('Analiza d1–d5','Część II · Analiza jakościowa', sec(9, s['title'], s.get('law'))+lead('',s['lead'])+thead+rows9(s['rows'][:5])+'  </table>\n')
page('Analiza d6–d9','Część II · Analiza jakościowa · cd.', sec(9,s['title']+' · cd.')+thead+rows9(s['rows'][5:])+'  </table>\n')

# ---------- 10 decyzja ----------
s=D['s10']; b=sec(10, s['title'], s.get('law'))+lead('',s['lead'])
b+=sub('A','Poziom wsparcia ustalony przez Zespół','')+'  <div class="lvlbox">\n'+''.join(f'    <div class="{"sel" if on else ""}">{cb(on)}<div><h4>{t}</h4><p>{d}</p></div></div>\n' for k,t,d,on in s['poziomy'])+'  </div>\n'
b+=f'  <div class="box" style="--c:var(--orange)"><div class="lbl">Uzasadnienie decyzji Zespołu</div><p class="just" style="margin:0">{s["uzasadnienie"]}</p></div>\n'
b+='  <div class="kv">'+''.join(f'<div><div class="l">{k}</div><div class="v">{v}</div></div>' for k,v in s['wymiar'])+'</div>\n'
rk=s['rekomendacje']
b+=sub('B','Rekomendacje placówki dla zespołu orzekającego poradni','',"var(--blue)")+f'  <p class="lead2" style="margin-bottom:4px">{rk["lead"]}</p>\n'
b+='  <div class="rek">'+''.join(f'<span>{cb(on)}<span>{t}</span></span>' for t,on in rk['items'])+'</div>\n'
b+=f'  <div class="note" style="margin:0 0 8px"><b>Uzasadnienie rekomendacji.</b> {rk["uzasadnienie"]}</div>\n'
b+=f'  <div class="signbox"><b>Data posiedzenia Zespołu:</b> <span class="ph">{s["dataDecyzji"]}</span> &nbsp;·&nbsp; {s["zgodaRodzica"]} &nbsp;·&nbsp; <b>Podpisy Zespołu i rodzica:</b> na końcu dokumentu (sekcja 16).</div>\n'
page('Decyzja Zespołu','Część II · Decyzja Zespołu',b)

# ---------- 11 dostosowania (2 strony: A | B+C) ----------
s=D['s11']
def kvtable(rows, c1='Zakres', c2='Sposób dostosowania'):
    return f'  <table class="grid">\n    <tr><th style="width:24%">{c1}</th><th>{c2}</th></tr>\n'+''.join(f'    <tr><td class="area">{a}</td><td>{x}</td></tr>\n' for a,x in rows)+'  </table>\n'
b=band('III','Program wsparcia i organizacja','dostosowania · zintegrowane działania · zajęcia · dodatkowa osoba · rodzice i poradnia · ocena efektywności')
b+=sec(11, s['title'], s.get('law'))+lead('',s['lead'].replace('☐',cb()))
b+=sub('A',s['A']['title'])+kvtable(s['A']['rows'])
page('Dostosowanie programu','Część III · Dostosowanie programu',b)
b=sub('B',s['B']['title'],'',"var(--blue)")+kvtable(s['B']['rows'],'Obszar organizacji','Sposób dostosowania')
b+=sub('C',s['C']['title'],'',"var(--purple)")+kvtable(s['C']['rows'],'Obszar','Narzędzia i sposób wykorzystania')
page('Organizacja i technologie','Część III · Organizacja i technologie',b)

# ---------- 12 ----------
s=D['s12']; b=sec(12, s['title'], s.get('law'))+lead('',s['lead'])
b+='  <table class="grid">\n    <tr><th style="width:18%">Wspólny cel</th><th>Nauczyciel / wychowawca (codziennie w grupie)</th><th>Specjaliści (zajęcia)</th><th style="width:20%">Sposób koordynacji</th></tr>\n'
b+=''.join(f'    <tr><td class="area">{a}</td><td>{x}</td><td>{y}</td><td>{z}</td></tr>\n' for a,x,y,z in s['rows'])+'  </table>\n'
b+=f'  <div class="note" style="margin-top:10px"><b>Koordynacja.</b> {s["koordynacja"]}</div>\n'
page('Zintegrowane działania','Część III · Zintegrowane działania',b)

# ---------- 13 (2 strony: A+B | C) ----------
s=D['s13']; b=sec(13, s['title'], s.get('law'))+lead('',s['lead'])
b+=f'''  <div class="hours tight">
    <div class="stat"><div class="l">A · Zajęcia rewalidacyjne · razem</div><div class="v">{s['sumRew'][0]} <small>= {s['sumRew'][1]} · {s['sumRew'][2]}</small></div></div>
    <div class="stat b"><div class="l">B · Pomoc psychologiczno-pedagogiczna · razem</div><div class="v">{s['sumPpp'][0]} <small>= {s['sumPpp'][1]} · {s['sumPpp'][2]}</small></div></div>
  </div>
'''
b+=sub('A','Zajęcia rewalidacyjne przydzielone dziecku / uczniowi','kształcenie specjalne · na podstawie orzeczenia')
b+='  <table class="grid rew tight">\n    <tr><th style="width:31%">Rodzaj zajęć</th><th style="width:29%">Zakres / cel</th><th style="width:15%">Prowadzący</th><th style="width:12%">Forma</th><th>Wymiar tyg.</th></tr>\n'
b+=''.join(f'    <tr><td class="area">{r[0]}</td><td>{r[1]}</td><td style="color:var(--purple);font-weight:700">{r[2]}</td><td>{r[3]}</td><td class="time">{r[4]}<small>{r[5]}</small></td></tr>\n' for r in s['rew'])
b+=f'    <tr class="sum"><td colspan="4">Razem zajęcia rewalidacyjne</td><td class="time">{s["sumRew"][0]}<small>{s["sumRew"][1]}</small></td></tr>\n  </table>\n'
page('Zajęcia: rewalidacja','Część III · Zajęcia: rewalidacja',b)
b=sub('B','Zajęcia z zakresu pomocy psychologiczno-pedagogicznej','forma · czas · termin · okres udzielania · miejsce',"var(--blue)")
b+='  <table class="grid ppp tight">\n    <tr><th style="width:22%">Forma pomocy</th><th style="width:27%">Cel</th><th style="width:12%">Prowadzący</th><th style="width:14%">Forma i miejsce</th><th style="width:12%">Czas i termin</th><th>Okres udzielania</th></tr>\n'
b+=''.join(f'    <tr><td class="area">{r[0]}</td><td>{r[1]}</td><td style="color:var(--purple);font-weight:700">{r[2]}</td><td>{r[3]}</td><td class="time" style="white-space:normal">{r[4]}</td><td>{r[5]}</td></tr>\n' for r in s['ppp'])
b+=f'    <tr class="sum"><td colspan="5">Razem pomoc psychologiczno-pedagogiczna</td><td class="time">{s["sumPpp"][0]}<small>{s["sumPpp"][1]}</small></td></tr>\n  </table>\n'
page('Zajęcia: PPP','Część III · Zajęcia: pomoc psychologiczno-pedagogiczna',b)
b=sub('C','Zalecenia poradni i miejsce ich realizacji w programie','każde zalecenie wskazuje sekcję, w której jest realizowane',"var(--purple)")
b+=f'  <p class="lead2">Orzeczenie / opinia nr <span class="ph">{D["meta"]["nrOrzeczenia"]}</span> z dnia <span class="ph">{D["meta"]["dataOrzeczenia"]}</span>. <i>Uwaga: {s["uwaga"]}</i></p>\n'
b+='  <table class="grid">\n    <tr><th style="width:24px">Lp.</th><th>Zalecenie poradni (z orzeczenia / opinii)</th><th style="color:var(--orange)">Sposób realizacji w placówce</th><th style="width:14%">Gdzie w raporcie</th><th style="width:13%">Status</th></tr>\n'
b+=''.join(f'    <tr><td class="code">{i+1}</td><td><b>{a}</b></td><td>{x}</td><td><span class="ref-pill">{r}</span></td><td>{status()}</td></tr>\n' for i,(a,x,r) in enumerate(s['mapa']))+'  </table>\n'
page('Zalecenia poradni','Część III · Realizacja zaleceń poradni',b)

# ---------- 14 ----------
s=D['s14']; b=sec(14, s['title'], s.get('law'))
b+='  <div class="cbl" style="grid-template-columns:1fr 1fr 1fr">'+''.join(f'<span>{cb(on)}<b>{t}</b></span>' for t,on in s['rodzaj'])+'</div>\n'
b+='  <div class="kv" style="grid-template-columns:1fr 2fr"><div><div class="l">Wymiar i sytuacje</div><div class="v">'+s['wymiar']+'</div></div><div><div class="l">Podstawa prawna i formalna</div><div class="v" style="font-weight:600">'+s['podstawa']+'</div></div></div>\n'
b+=f'  <div class="box" style="--c:var(--orange)"><div class="lbl">Uzasadnienie wynikające z oceny funkcjonalnej</div><p class="just" style="margin:0">{s["uzasadnienie"]}</p></div>\n'
b+='  <div class="box" style="--c:var(--green);margin-top:10px"><div class="lbl">Zadania dodatkowej osoby</div><ul class="tick">'+''.join(f'<li>{x}</li>' for x in s['zadania'])+'</ul></div>\n'
b+=f'  <div class="note" style="margin-top:10px"><b>Ocena zasadności.</b> {s["ocena"]}</div>\n'
b+=f'  <p class="stnote"><b>Wariant B:</b> {s["wariantNote"]}</p>\n'
page('Dodatkowa osoba','Część III · Dodatkowa osoba',b)

# ---------- 15 ----------
s=D['s15']; b=sec(15, s['title'], s.get('law'))
b+=sub('A',s['A']['title'])+'  <table class="grid">\n    <tr><th style="width:22%">Forma współpracy</th><th>Zakres</th><th style="width:20%">Odpowiedzialny</th><th style="width:20%">Częstotliwość</th></tr>\n'
b+=''.join(f'    <tr><td class="area">{a}</td><td>{x}</td><td style="color:var(--purple);font-weight:700">{y}</td><td>{z}</td></tr>\n' for a,x,y,z in s['A']['rows'])+'  </table>\n'
b+=sub('B',s['B']['title'],'',"var(--green)")+'  <div class="box" style="--c:var(--green)"><ul class="tick" style="margin:0">'+''.join(f'<li>{x}</li>' for x in s['B']['items'])+'</ul></div>\n'
b+=sub('C',s['C']['title'],'',"var(--purple)")+'  <table class="grid">\n    <tr><th style="width:24%">Działanie</th><th>Zakres / cel</th><th style="width:20%">Kto</th><th style="width:20%">Termin</th></tr>\n'
b+=''.join(f'    <tr><td class="area">{a}</td><td>{x}</td><td style="color:var(--purple);font-weight:700">{y}</td><td>{z}</td></tr>\n' for a,x,y,z in s['C']['rows'])+'  </table>\n'
page('Rodzice i poradnia','Część III · Współpraca z rodzicami i poradnią',b)

# ---------- 16 + podpisy ----------
s=D['s16']; b=sec(16, s['title'], s.get('law'))+lead('',s['lead'])
stc={'wykonano':'done','w trakcie':'now','planowane':'plan'}
b+='  <table class="grid">\n    <tr><th style="width:16%">Termin</th><th>Zakres oceny</th><th style="width:24%">Narzędzia</th><th style="width:16%">Odpowiedzialny</th><th style="width:11%">Status</th></tr>\n'
b+=''.join(f'    <tr><td class="area">{a}</td><td>{x}</td><td>{y}</td><td>{z}</td><td><span class="status-pill {stc[st]}">{st}</span></td></tr>\n' for a,x,y,z,st in s['rows'])+'  </table>\n'
b+='''  <div class="parent" style="margin-top:12px"><b>Informacja dla rodzica.</b> Niniejszy raport stanowi opinię placówki o funkcjonowaniu dziecka i jest przekazywany rodzicowi oraz zespołowi orzekającemu poradni. Wyniki obserwacji służą zaplanowaniu wsparcia, a nie ocenie dziecka. Zachęcamy do rozmowy z Zespołem o każdej części dokumentu.</div>
  <div class="sigs">
    <div class="sig">Koordynator Zespołu<small>podpis i data</small></div>
    <div class="sig">Dyrektor placówki<small>podpis i data</small></div>
    <div class="sig">Specjalista<small>podpis i data</small></div>
    <div class="sig wide">Rodzic / opiekun prawny – zapoznałam/em się z raportem i uczestniczyłam/em w ustaleniu poziomu wsparcia<small>podpis i data</small></div>
  </div>
'''
page('Ocena efektywności i podpisy','Część III · Ocena efektywności · podpisy',b)

# ---------- strona 2: jak czytać + warianty; strona 3: podstawy prawne ----------
pr=D['prawo']; wv=D['warianty']
def okcell(v):
    if v.startswith('✓'): return f'<td class="ok">{v}</td>'
    if v.startswith('—'): return f'<td class="no">{v}</td>'
    return f'<td>{v}</td>'
lp2='<section class="page">\n'+hdr('Jak czytać raport · dwa warianty')+'''
  <div class="sec"><span class="n">?</span><h2>Jak czytać ten raport</h2></div>
  <p class="lead2">Pięć kroków od obserwacji do oceny efektów. <b>Część I–II</b> to opinia placówki, którą otrzymuje rodzic i zespół orzekający poradni. <b>Część III</b> to organizacja wsparcia w placówce – co, kto, kiedy i ile.</p>
  <div class="flow5">'''+''.join(f'<div><div class="p">CZĘŚĆ {p}</div><h4>{h}</h4><p>{t}</p></div>' for p,h,t in pr['jakczytac'])+'''</div>
  <div class="sec" style="margin-top:18px"><span class="n">A/B</span><h2>'''+wv['title']+'''</h2></div>
  <p class="lead2">'''+wv['lead']+'''</p>
  <div class="varbox">
    <div><span class="tag9" style="background:var(--orange)">A</span><div>'''+wv['A'].replace('Wariant A ·','<b>Wariant A</b> ·')+'''</div></div>
    <div><span class="tag9" style="background:var(--blue)">B</span><div>'''+wv['B'].replace('Wariant B ·','<b>Wariant B</b> ·')+'''</div></div>
  </div>
  <table class="grid small">
    <tr><th style="width:9%">Sekcje</th><th>Zakres</th><th style="width:22%">Wariant A · z orzeczeniem</th><th style="width:26%">Wariant B · bez orzeczenia</th></tr>
'''+''.join(f'    <tr><td class="code">{a}</td><td>{b}</td>{okcell(c)}{okcell(d)}</tr>\n' for a,b,c,d in wv['rows'])+'''  </table>
'''
lp3='<section class="page">\n'+hdr('Podstawy prawne')+'''
  <div class="sec"><span class="n">§</span><h2>'''+pr['title']+'''</h2></div>
  <p class="lead2">'''+pr['lead']+'''</p>
  <table class="grid">
    <tr><th style="width:30%">Akt prawny</th><th style="width:11%">Publikacja</th><th>Zakres zastosowania w raporcie</th><th style="width:12%">Sekcje</th></tr>
'''+''.join(f'    <tr><td class="act">{a}</td><td class="dz">{b}</td><td>{c}</td><td><span class="ref-pill">{d}</span></td></tr>\n' for a,b,c,d in pr['rows'])+'''  </table>
  <div class="parent" style="margin-top:12px"><b>Dla rodzica.</b> Numery paragrafów wskazują, z jakiego przepisu wynika każda część raportu. Przy każdej sekcji 4–16 znajduje się plakietka „§ Podstawa prawna”.</div>
'''
# ---------- składanie ----------
TOTAL = 5 + len(pages)
toc = D['toc']
tochtml = '  <div class="toc">\n    <h5>'+toc['I']['title']+'</h5>\n'+''.join(f'    <div><div class="k">{n}</div><h4>{t}</h4><p>{d}</p></div>\n' for n,t,d in toc['I']['items'])+'  </div>\n'
for part in ('II','III'):
    tochtml += f'  <div class="toc" style="grid-template-columns:repeat(7,1fr);margin-top:8px">\n    <h5>{toc[part]["title"]}</h5>\n'
    tochtml += ''.join(f'    <div style="padding:7px 8px 6px"><div class="k" style="font-size:16px">{n}</div><h4 style="font-size:9.5px;margin:3px 0 0">{t}</h4></div>\n' for n,t in toc[part]['items'])+'  </div>\n'
p1 = P1.replace('{{TOTAL}}', str(TOTAL)).replace('{{TOC}}\n', tochtml).replace('Strona <b>3</b> z','Strona <b>5</b> z').replace('Strona <b>2</b> z','Strona <b>4</b> z')
cut = p1.index('<!-- ======================= STRONA 2')
p1 = p1[:cut] + lp2 + f'  <div class="footer"><span>EduPlaner 2026 · PCTP</span><span>Strona <b>2</b> z {TOTAL} · Jak czytać · warianty</span></div>\n</section>\n\n' + lp3 + f'  <div class="footer"><span>EduPlaner 2026 · PCTP</span><span>Strona <b>3</b> z {TOTAL} · Podstawy prawne</span></div>\n</section>\n\n' + p1[cut:]
body = p1
for i,(name,inner) in enumerate(pages):
    n = 6+i
    body += inner + f'  <div class="footer"><span>EduPlaner 2026 · PCTP</span><span>Strona <b>{n}</b> z {TOTAL} · {name}</span></div>\n</section>\n\n'

JS='''<script>
(function(){
  var sec=document.getElementById('sek5'); if(!sec) return;
  var KEY='rof_tool_v1';
  function apply(v){ sec.classList.toggle('kpof', v==='kpof'); sec.classList.toggle('kszof', v!=='kpof');
    var r=sec.querySelector('input[value="'+v+'"]'); if(r) r.checked=true; }
  var saved=null; try{ saved=localStorage.getItem(KEY); }catch(e){}
  apply(saved==='kpof'?'kpof':'kszof');
  sec.querySelectorAll('input[name="tool"]').forEach(function(i){ i.addEventListener('change',function(){ apply(i.value); try{ localStorage.setItem(KEY,i.value); }catch(e){} }); });
})();
</script>'''
HEAD = '''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Raport Oceny Funkcjonalnej · EduPlaner 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Mulish:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
'''
css = CSS.replace('\n  @media screen and (max-width:760px){', EXTRA_CSS+'\n  @media screen and (max-width:760px){',1)
css = css.replace('.fields,.team ol,.tools,.flow,.toc,.stats,.hours{grid-template-columns:1fr}','.fields,.team ol,.tools,.flow,.toc,.stats,.hours,.voice,.lvlbox,.kv,.cbl,.flow5{grid-template-columns:1fr !important}')
out = HEAD+css+'\n</style>\n</head>\n<body>\n\n'+body+JS+'\n</body>\n</html>\n'
open('Raport_Oceny_Funkcjonalnej.html','w',encoding='utf-8').write(out)
print('pages', TOTAL)
