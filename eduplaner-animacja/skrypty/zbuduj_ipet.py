# -*- coding: utf-8 -*-
"""Buduje druk IPET (przedszkole, dziecko z orzeczeniem) wg wzoru EduPlaner 2026 · PCTP — 40 stron
+ 2 strony podstawy prawnej (Strażnik prawa). Ten sam system graficzny co druk WOPF (Mulish, ramka, metryczka).
Użycie:  python3 skrypty/zbuduj_ipet.py            -> public/ipet.html (pusty druk, do animacji: data-k na polach)
         python3 skrypty/zbuduj_ipet.py --wypelnij -> out/ipet/IPET_2026_Zofia_Lewandowska_wypelniony.html
"""
import sys, os, json, html, re
TU = os.path.dirname(os.path.abspath(__file__)); KAT = os.path.dirname(TU)
sys.path.insert(0, TU)
from ipet_dane import D
WYP = '--wypelnij' in sys.argv
SCR = os.environ.get('IPET_SCRATCH', '/tmp/claude-0/-home-user-chatbot/71b0dfe1-b753-5beb-8412-40de3cbd7ec1/scratchpad/ipet')
BASE_CSS = open(os.path.join(SCR, 'wopf_base.css'), encoding='utf-8').read()
FONT_CSS = open(os.path.join(SCR, 'mulish_embed.css'), encoding='utf-8').read()

# publikatory wg skryptu szkolenia (wyd. 2 po audycie z 5.09.2026) — Strażnik prawa
KS = 'rozp. MEN z 9.08.2017 r. w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym (t.j. Dz.U. 2020 poz. 1309)'
KSs = 'rozp. MEN z 9.08.2017 r. (t.j. Dz.U. 2020 poz. 1309)'
PP = 'rozp. MEN z 9.08.2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej w publicznych przedszkolach, szkołach i placówkach (t.j. Dz.U. 2023 poz. 1798)'
PPs = 'rozp. MEN z 9.08.2017 r. w sprawie pomocy pp (t.j. Dz.U. 2023 poz. 1798)'
PO = 'ustawa z 14.12.2016 r. — Prawo oświatowe (t.j. Dz.U. 2026 poz. 820)'
PPR = 'rozp. ME z 11.03.2026 r. w sprawie podstawy programowej wychowania przedszkolnego (Dz.U. 2026 poz. 378)'
ORZ = 'rozp. ME z 2.03.2026 r. w sprawie orzeczeń i opinii wydawanych przez zespoły orzekające działające w publicznych poradniach psychologiczno-pedagogicznych (Dz.U. 2026 poz. 428)'
DOK = 'rozp. MEN z 25.08.2017 r. w sprawie sposobu prowadzenia przez publiczne przedszkola, szkoły i placówki dokumentacji przebiegu nauczania (t.j. Dz.U. 2024 poz. 50)'

CSS_IPET = r"""
.pbody .blk:has(> .pair){flex:0 0 auto}
.pbody .blk:has(> .ta){flex:0 0 auto}
.pbody .blk.grow{flex:1 1 auto;display:flex;flex-direction:column}
.pbody .blk.grow>.ta{flex:1}
.pbody .blk.grow>.pair{flex:1}
.pbody .blk.grow>.pair .ta{height:auto}
.ta .ed{font-size:9.6px;color:#2f2a3e;line-height:1.5;white-space:pre-wrap}
.ta .ph{font-size:9.2px;color:#9a94ad;font-style:italic}
.fields .fv .ph{color:#9a94ad;font-weight:400;font-style:italic;font-size:9.4px}
.fields .f.acc{border-left:4.5px solid #E8450A;background:#fff;grid-column:1/-1}
.fields .f.wide{grid-column:1/-1}
.fields .fv{font-weight:700;font-size:9.9px;line-height:1.4}
.fields .fv.small{font-size:9px}
.fields .f.gray .fv{color:#8a8498;font-weight:700}
.checks .c{font-size:9.5px;padding:4px 8px}
.checks .c.on,.checks .c:has(.bx.on){border-color:#E8450A;background:#fff8f3}
.pills .p:has(.bx.on){border-color:#E8450A;background:#fff8f3}
.faces .fc.on{border-color:#E8450A;background:#fff8f3;box-shadow:0 0 0 2px #fbd9c6}
.checks.c1{grid-template-columns:1fr}
.checks.c3{grid-template-columns:1fr 1fr 1fr}
.bx.on{background:#E8450A;border-color:#E8450A;position:relative}
.bx.on::after{content:'✓';color:#fff;font-size:8.5px;font-weight:800;position:absolute;left:1px;top:-3px;line-height:1.4}
.sec .n.sq{border-radius:50%}
.sec h2{font-size:11.8px}
.sec .n{font-size:9px}
.sec.small h2{font-size:10.5px}
.subhead{font-size:8.4px;margin:5px 0 3px}
.subhead.red{color:#c0392b}.subhead.red::before{background:#c0392b}
.subhead.blue{color:#2B5FA0}.subhead.blue::before{background:#2B5FA0}
.subhead.green{color:#0D7D5C}.subhead.green::before{background:#0D7D5C}
.subhead.purple{color:#2D1B69}.subhead.purple::before{background:#2D1B69}
.subhead.amber{color:#C47A10}.subhead.amber::before{background:#C47A10}
.subhead .lvls{margin-left:auto;display:flex;align-items:center;gap:4px;font-size:7px;color:#6f6a7d;text-transform:uppercase;letter-spacing:.5px}
.lc{width:14px;height:14px;border-radius:50%;border:1.6px solid;font-size:7.3px;font-weight:800;display:inline-flex;align-items:center;justify-content:center;background:#fff}
.lc.g{border-color:#0D7D5C;color:#0D7D5C}.lc.a{border-color:#C47A10;color:#C47A10}.lc.r{border-color:#c0392b;color:#c0392b}
.lc.on.g{background:#0D7D5C;color:#fff}.lc.on.a{background:#C47A10;color:#fff}.lc.on.r{background:#c0392b;color:#fff}
.sfera{display:flex;align-items:center;gap:10px;background:linear-gradient(120deg,#2D1B69,#4A2FA0);color:#fff;border-radius:11px;padding:6px 12px;box-shadow:0 3px 10px rgba(45,27,105,.28)}
.sfera .sn{width:20px;height:20px;border-radius:50%;background:#E8450A;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:10px;flex:0 0 auto}
.sfera .st{font-size:12.5px;font-weight:800}
.tools{background:#fff3ec;border:1px solid #f4c9ae;border-radius:9px;padding:5px 10px;font-size:7.9px;color:#3d384c;line-height:1.5}
.tools b{color:#E8450A}
.wynik{display:flex;gap:10px;align-items:center;background:#efeaf9;border:1px solid #ddd3f1;border-radius:10px;padding:6px 10px;margin:4px 0}
.wynik .wl{font-size:6.8px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;color:#2D1B69;width:34px;line-height:1.3;flex:0 0 auto}
.wynik .wt{flex:1;font-size:8.8px;color:#2f2a3e;line-height:1.45}
.wynik .wt b{color:#2D1B69}
.wchip{flex:0 0 auto;border-radius:12px;padding:3px 10px;font-size:7.6px;font-weight:800;letter-spacing:.3px;border:1.3px solid}
.wchip.I{background:#eef8f3;border-color:#9fd3ba;color:#0D7D5C}.wchip.II{background:#fff8e6;border-color:#f0cf7a;color:#C47A10}.wchip.III,.wchip.on{background:#fdecea;border-color:#f0a3a3;color:#c0392b}
.lvl3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}
.lvl3 .lvl{padding:6px 9px}
.lvl3 .lvl-t{font-size:7.8px;margin-bottom:3px}
.lvl3 .lvl-x{font-size:8.4px;line-height:1.42}
.lvl.g{background:#eef8f3;border-color:#9fd3ba}.lvl.a{background:#fff8e6;border-color:#f0cf7a}.lvl.r{background:#fdecea;border-color:#f0a3a3}
.lvl.g .lvl-t{color:#0D7D5C}.lvl.a .lvl-t{color:#C47A10}.lvl.r .lvl-t{color:#c0392b}
.lvl-n{width:14px;height:14px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:7.3px;font-weight:800;color:#fff}
.lvl.g .lvl-n{background:#0D7D5C}.lvl.a .lvl-n{background:#C47A10}.lvl.r .lvl-n{background:#c0392b}
.smart{border:1.5px solid #f0b48a;border-radius:11px;padding:6px 11px 7px;background:#fff7f2}
.smart .sh{display:flex;align-items:center;gap:6px;font-size:8.2px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:#E8450A;margin-bottom:3px}
.smart .sh .ch{margin-left:auto;display:flex;gap:3px}
.smart .sh .ch span{width:14px;height:14px;border-radius:50%;border:1.4px solid #E8450A;color:#E8450A;font-size:7px;font-weight:800;display:inline-flex;align-items:center;justify-content:center;background:#fff}
.smart .lead2{font-size:7.6px;color:#8a8498;margin-bottom:2px}
.smart .g{display:flex;gap:6px;font-size:8.9px;color:#2f2a3e;line-height:1.45;margin:2px 0}
.smart .g::before{content:'';width:6px;height:6px;border-radius:50%;background:#E8450A;flex:0 0 auto;margin-top:5px}
.smart .g b{color:#2D1B69}
.smart .ln{height:14px;border-bottom:1.2px dotted #b5a8d8}
.mini-ta{border:1px solid #cfc2e8;border-radius:10px;background:#fff;padding:5px 10px;font-size:9px;color:#2f2a3e;line-height:1.45;box-shadow:0 2px 6px rgba(45,27,105,.10)}
.mini-ta .tl{font-size:7.8px;font-weight:800;letter-spacing:.5px;text-transform:uppercase;color:#2D1B69;margin-bottom:2px}
.pch{display:inline-flex;align-items:center;border:1.2px solid #8f80c8;color:#2D1B69;border-radius:9px;padding:0 6px;font-size:6.6px;font-weight:800;background:#f3eefb;white-space:nowrap;line-height:1.7}
.zal{display:inline-block;background:#fff3ec;color:#E8450A;border-radius:8px;padding:0 5px;font-size:6.6px;font-weight:800;border:1px solid #f4c9ae;white-space:nowrap;line-height:1.7}
.nowe{display:inline-block;border:1.2px solid #f0b48a;color:#E8450A;border-radius:10px;padding:0 7px;font-size:6.6px;font-weight:800;background:#fff7f2;white-space:nowrap;line-height:1.8}
.nbox{display:flex;gap:10px;align-items:center;background:#fff7f2;border:1px solid #f4c9ae;border-radius:10px;padding:6px 12px;font-size:8.6px;color:#3d384c;line-height:1.45}
.nbox .nl{border:1.4px solid #E8450A;border-radius:12px;padding:3px 8px;font-size:7px;font-weight:800;color:#E8450A;text-align:center;line-height:1.2;flex:0 0 auto;background:#fff}
.pills{display:flex;flex-wrap:wrap;gap:5px}
.pills .p{display:flex;align-items:center;gap:6px;border:1.3px solid #cfc2e8;border-radius:14px;padding:3px 10px 3px 6px;font-size:8.8px;color:#3d384c;background:#f9f7fd}
.pills .p.on{border-color:#E8450A;background:#fff8f3}
.bx{width:11px;height:11px;flex:0 0 auto;border:1.7px solid #6C4CC4;border-radius:3.5px;background:#fff;display:inline-block;vertical-align:middle}
.faces{display:flex;gap:6px}
.faces .fc{flex:1;text-align:center;border:1.3px solid #cfc2e8;border-radius:10px;padding:5px 4px;background:#f9f7fd;font-size:8.4px;color:#3d384c;font-weight:700}
.faces .fc .em{font-size:17px;line-height:1.2;display:block}
.faces .fc.on{border-color:#E8450A;background:#fff8f3;box-shadow:0 0 0 2px #fbd9c6}
.col4{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:6px}
.col4 .card{border:1px solid #cfc2e8;border-radius:10px;padding:6px 8px;background:#fff;box-shadow:0 2px 6px rgba(45,27,105,.08)}
.col4 .card .ct{font-size:8.2px;font-weight:800;color:#2D1B69;margin-bottom:4px;letter-spacing:.3px;border-bottom:1.5px solid #E8450A;padding-bottom:3px}
.col4 .checks{grid-template-columns:1fr;gap:3px}
.col4 .checks .c{font-size:8px;padding:3px 6px}
.steps3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}
.steps3 .s3{border:1px solid #ddd3f1;border-radius:10px;padding:6px 9px;background:#f6f3fc}
.steps3 .s3 .sn{width:18px;height:18px;border-radius:50%;background:#E8450A;color:#fff;font-weight:800;font-size:9px;display:inline-flex;align-items:center;justify-content:center;margin-bottom:3px}
.steps3 .s3 .st{font-size:7.8px;font-weight:800;text-transform:uppercase;letter-spacing:.5px;color:#2D1B69;margin-bottom:2px}
.steps3 .s3 p{margin:0;font-size:8.4px;color:#3d384c;line-height:1.45}
table.tb td{font-size:9px;padding:4.5px 7px;vertical-align:top}
table.tb th{font-size:7.8px;padding:5px 7px}
table.tb td.nr{vertical-align:middle}
table.tb td .ph{color:#9a94ad;font-style:italic}
table.tb td.gray{color:#8a8498}
table.tb td b.p{color:#2D1B69}
table.tb.small td{font-size:8.3px;padding:3.5px 6px}
table.tb.xs td{font-size:7.8px;padding:2.5px 6px}
table.tb.kk td{font-size:8.2px;padding:4px 7px}
table.tb.kk td.pod{color:#E8450A;font-weight:800;white-space:nowrap}
table.tb.kk td.gdzie{color:#8a8498;font-size:7.6px}
table.tb td .bxc{display:flex;justify-content:center}
.pfoot .l{color:#8a8498}
.sign2{display:flex;gap:16mm;margin:5mm 4mm 1mm}
.sign2>div{flex:1;font-size:7.2px;color:#5a5470;font-weight:800;letter-spacing:.6px;text-transform:uppercase}
.sign2 .sl{border-bottom:1.4px solid #8f86ad;height:9mm;margin-bottom:4px}
.rodo p{margin:0 0 5px;font-size:9.6px;color:#2f2a3e;line-height:1.55}
.rodo p b{color:#2D1B69}
.legal{font-size:7.1px}
.legal.big{font-size:8.2px;color:#3d384c;border-top:none;padding-top:0}
.legal b.o{color:#E8450A}
.req{border:1px solid #cfc2e8;border-radius:9px;background:#fff;padding:3px 8px;margin-bottom:3px;box-shadow:0 1px 4px rgba(45,27,105,.08)}
.req .rt{display:flex;gap:8px;align-items:baseline;font-size:8.6px;font-weight:800;color:#2D1B69}
.req .rt .pod{color:#E8450A;white-space:nowrap}
.req .rt .ok{margin-left:auto;font-size:7px;color:#0D7D5C;border:1.2px solid #9fd3ba;border-radius:9px;padding:0 6px;background:#eef8f3;white-space:nowrap}
.req .rq{font-size:7.8px;color:#3d384c;line-height:1.4;margin-top:0}
.req .rq i{color:#5a5470}
.req .rw{font-size:7.6px;color:#8a8498;margin-top:1px}
.pmeta .mv{font-size:9.4px}
.itoolbar{display:none}
"""

# ---------------- pomocnicze ----------------
def esc(s): return html.escape(str(s), quote=False)
PAGES = []
def V(key, default=''):
    """wartość z danych (tryb wypełniony) albo pusta"""
    if not WYP: return ''
    v = D.get(key, default)
    return v if v is not None else ''
def ON(setkey, i):
    return WYP and i in D.get(setkey, set())
def fv(key, ph='', small=False, k=None):
    """pole .fv — wartość albo placeholder; data-k do animacji"""
    val = V(key)
    kk = f' data-k="{k or key}"'
    cls = 'fv small' if small else 'fv'
    if val: return f'<div class="{cls}"{kk}>{esc(val)}</div>'
    return f'<div class="{cls}"{kk}>' + (f'<span class="ph">{esc(ph)}</span>' if ph else '&nbsp;') + '</div>'
def field(label, key, ph='', cls='', small=False, k=None):
    return f'<div class="f {cls}"><div class="fl">{esc(label)}</div>{fv(key, ph, small, k)}</div>'
def fields(items):
    return '<div class="fields">' + ''.join(items) + '</div>'
def bx(on, k=None):
    return f'<span class="bx{" on" if on else ""}"{(" data-k=%s" % json.dumps(k)) if k else ""}></span>'
def checks(items, setkey=None, on=None, cols=2, prefix=None, kfmt=None):
    cl = {1:'checks c1',2:'checks',3:'checks c3'}[cols]
    out = []
    for i, t in enumerate(items):
        o = (on(i) if on else ON(setkey, i))
        k = (kfmt(i) if kfmt else (f'{setkey}:{i}' if setkey else None))
        out.append(f'<div class="c{" on" if o else ""}">{bx(o, k)}<span>{t}</span></div>')
    return f'<div class="{cl}">' + ''.join(out) + '</div>'
def sec(n, title, tag=None, small=False, sq=False):
    t = f'<span class="tag">{esc(tag)}</span>' if tag else ''
    return f'<div class="sec{" small" if small else ""}"><span class="n{" sq" if sq else ""}">{n}</span><h2>{title}</h2><span class="rl"></span>{t}</div>'
def subhead(text, color='purple', extra=''):
    return f'<div class="subhead {color}">{text}{extra}</div>'
def blk(inner, cls=''): return f'<div class="blk {cls}">{inner}</div>'
def ta(title, key=None, lines=3, ph='', grow=False, k=None):
    val = V(key) if key else ''
    if val: body = f'<div class="ed" data-k="{k or key}">{esc(val)}</div>'
    elif ph: body = f'<div class="ed" data-k="{k or key}"><span class="ph">{esc(ph)}</span></div>' + ''.join('<div class="ln"></div>' for _ in range(max(lines-1,0)))
    else: body = f'<div class="ed" data-k="{k or key}"></div>' + ''.join('<div class="ln"></div>' for _ in range(lines))
    return blk(f'<div class="ta"><div class="tl">{title}</div>{body}</div>', 'grow' if grow else '')
def legal(text, big=False, label='Podstawa prawna'):
    return blk(f'<div class="legal{" big" if big else ""}"><b>{label}.</b> {text}</div>')
def note(text): return blk(f'<div class="note">{text}</div>')
def lead(title, text): return blk(f'<div class="lead"><b class="tl">{title}</b><p>{text}</p></div>')
def howto(mini, text): return blk(f'<div class="howto"><div class="mini">{mini}</div><p>{text}</p></div>')
def kick(text): return f'<div class="tt-kick"><span>{text}</span></div>'
def h1(text): return f'<div class="tt-h1">{text}</div>'
def tsub(text): return f'<div class="tt-sub"><span class="dots"></span><span class="tx">{text}</span><span class="dots"></span></div>'
def table(heads, rows, cls='tb', widths=None):
    th = ''.join('<th' + ((' style="width:%s"' % widths[i]) if widths and widths[i] else '') + '>' + h + '</th>' for i, h in enumerate(heads))
    trs = ''.join('<tr>' + ''.join(c if c.startswith('<td') else f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return blk(f'<table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table>')
def nr(i): return f'<td class="nr">{i}</td>'
def cell(val, ph='', k=None, cls=''):
    kk = f' data-k="{k}"' if k else ''
    if val: return f'<td class="{cls}"{kk}>{esc(val)}</td>'
    return f'<td class="{cls}"{kk}>' + (f'<span class="ph">{esc(ph)}</span>' if ph else '') + '</td>'
def chip(level, k=None):
    return f'<span class="wchip {level}"{(" data-k=%s" % json.dumps(k)) if k else ""}>{ {"I":"Poziom I — wsparcie minimalne","II":"Poziom II — wsparcie umiarkowane","III":"Poziom III — wsparcie znaczne"}[level] }</span>'
def lvls(on, n=0):
    return '<span class="lvls">Poziom wsparcia:' + ''.join(f'<span class="lc {c}{" on" if on==l else ""}" data-k="sf{n}:lvl:{l}">{l}</span>' for l, c in (('I','g'),('II','a'),('III','r'))) + '</span>'
def pch(sym, t): return f'<span class="pch">{sym} {t}</span>'
P1, P2, P3 = pch('▲','P1'), pch('■','P2'), pch('●','P3')
def zalc(n): return f'<span class="zal">★ Zał. {n}</span>'

def page(sub, foot, body):
    PAGES.append((sub, foot, body))

# ============================================================ STRONY
def s01():
    b = kick('Karta IPET (przedszkole) · kształcenie specjalne · z orzeczeniem')
    b += tsub('IPET · kształcenie specjalne · ocena funkcjonalna · ICF · przedszkole')
    b += h1('Indywidualny Program<br>Edukacyjno-Terapeutyczny')
    b += tsub('synteza zintegrowana · dziecko z orzeczeniem')
    b += blk(f'<div class="lead" style="border-left:none;border-radius:11px"><p>Dokument opracowywany dla <b>dziecka objętego wychowaniem przedszkolnym</b>, posiadającego <b>orzeczenie o potrzebie kształcenia specjalnego</b>. Stanowi <b>syntezę wszystkich obserwacji</b> (KPOF → obserwacje pogłębione) w logiczną całość, bez powielania. Określa zakres i sposób dostosowania wymagań, zintegrowane działania nauczycieli i specjalistów oraz formy pomocy. Podstawa prawna: art. 127 {PO}; § 6 {KS}; {PPR}.</p></div>')
    b += blk('<div class="nbox"><span class="nl">✦ NOWE<br>26/27</span><span>tym znaczkiem oznaczono elementy nowego modelu (ICF / KPOF, poziomy wsparcia, „Mój głos") od roku szk. 2026/27. Rozliczenie wymogów rozporządzenia — karta kontrolna i wykaz wymagań na końcu dokumentu.</span></div>')
    b += blk(sec('I', 'Dane dziecka'))
    b += blk(fields([field('Imię i nazwisko', 'imie'), field('Data urodzenia', 'ur'),
                     field('Grupa / oddział', 'grupa_pelna'), field('Rok szkolny', 'rok', cls='gray'),
                     field('Numer dokumentu / uwagi ważne do', 'nr_dok', small=True), field('Przedszkole / placówka', 'placowka', small=True),
                     field('Podstawa wydania orzeczenia (np. autyzm, niepełnosprawność sprzężona)', 'podst_orz', small=True), field('Numer i data orzeczenia / poradnia (PPP)', 'nr_orz', small=True),
                     field('Podstawa objęcia wsparciem (orzeczenie / diagnoza)', 'podst_wsp', cls='acc', small=True)]))
    page('IPET · dane dziecka', 'IPET · dane', b)

def s02():
    b = blk(f'<div class="sec"><span class="n">★</span><h2 style="text-transform:none;font-size:13px">Mój głos — perspektywa dziecka</h2><span class="rl"></span><span class="nowe">✦ NOWE 26/27</span></div>')
    b += howto('Jak nauczyciel pozyskuje głos dziecka?', 'Perspektywę dziecka poznaje się nie tylko przez rozmowę. Nauczyciel obserwuje dziecko w naturalnych sytuacjach (co wybiera, co je cieszy, czego unika), zadaje proste pytania dostosowane do jego możliwości, korzysta z obrazków, piktogramów i kart wyboru, a przy ograniczonej mowie — z komunikacji wspomagającej i alternatywnej (AAC: PECS, MAKATON, tablice). Głos dziecka odczytuje też z gestu, mimiki, zabawy i rysunku oraz z informacji od rodziców. Zapisujemy autentyczną perspektywę dziecka — jego słowami lub przez wskazanie.')
    b += blk(subhead('Sposób pozyskania głosu dziecka — zaznacz zastosowane'))
    b += blk(checks(['Rozmowa dostosowana do możliwości dziecka','Obserwacja w naturalnych sytuacjach','Wybór z obrazków / piktogramów / kart wyboru','Komunikacja wspomagająca i alternatywna (AAC)','Odczytanie z gestu, mimiki, zabawy, rysunku','Informacje od rodziców / opiekunów','Skala buziek / termometr emocji','Wskazanie „tak / nie" na symbolach'], 'glos_sposob'))
    b += ta('Moje mocne strony i supermoce', 'glos_mocne', 4, grow=True)
    b += ta('Z czym mam największą trudność w przedszkolu?', 'glos_trudnosc', 4, grow=True)
    b += ta('Preferowany sposób komunikacji dziecka (mowa · AAC · gesty · obrazki) i wskazówki do rozmowy', 'glos_komunikacja', 4, grow=True)
    b += note('Sekcja wypełniana z udziałem dziecka, dostosowana do jego możliwości komunikacyjnych.')
    page('Mój głos — perspektywa dziecka', 'Mój głos', b)

def s03():
    b = kick('Mój głos — perspektywa dziecka · uzupełnienie')
    b += note('Uzupełnienie perspektywy dziecka — zapisywane jego słowami lub przez wskazanie na obrazkach / symbolach. Pola wypełnia nauczyciel wspólnie z dzieckiem, w tempie i formie dostosowanej do jego możliwości.')
    b += ta('Co lubię (osoby, zabawy, miejsca)', 'glos_lubie', 3, grow=True)
    b += ta('Czego nie lubię / co mnie denerwuje', 'glos_nielubie', 3, grow=True)
    b += ta('Moje ulubione zabawy i czynności w przedszkolu', 'glos_zabawy', 3, grow=True)
    b += blk(subhead('Co mi najbardziej pomaga w przedszkolu?'))
    items = ['cisza','czas','ruch','piktogramy','praca na komputerze','przerwy','wsparcie nauczyciela','przewidywalny plan dnia']
    b += blk('<div class="pills">' + ''.join(f'<span class="p{" on" if (WYP and t in D["glos_pomaga"]) else ""}">{bx(WYP and t in D["glos_pomaga"], "glos_pomaga:"+t)}{t}</span>' for t in items) + '</div>')
    b += ta('Inne — co jeszcze mi pomaga?', 'glos_inne', 2)
    b += blk(subhead('Jak się dziś czuję? — wskaż buźkę'))
    fz = [('😄','Super'),('🙂','Dobrze'),('😐','Tak sobie'),('🙁','Słabo'),('😢','Źle')]
    b += blk('<div class="faces">' + ''.join(f'<div class="fc{" on" if (WYP and D["glos_buzka"]==l) else ""}" data-k="glos_buzka:{l}"><span class="em">{e}</span>{l}</div>' for e, l in fz) + '</div>')
    b += ta('Moje marzenie / czego bym chciał(a)', 'glos_marzenie', 2, grow=True)
    b += legal('Uwzględnienie perspektywy dziecka wspiera indywidualizację i podmiotowe traktowanie dziecka zgodnie z modelem ICF; „Mój głos" to element nowego modelu 2026/27.', label='Podstawa')
    page('Mój głos — uzupełnienie', 'Mój głos', b)

def s04():
    b = kick('Część I · WOPF wg ICF')
    b += note('Ocena obejmuje mocne strony, system motywacji, bariery i obserwacje funkcjonalne, uporządkowane zgodnie z Międzynarodową Klasyfikacją Funkcjonowania (ICF).')
    b += blk(sec('1', 'Mocne strony, predyspozycje, zainteresowania i uzdolnienia'))
    b += blk(checks(['Dobra pamięć wzrokowa i spostrzegawczość','Zdolności manualne i plastyczne','Zainteresowania przyrodnicze i techniczne','Wysoka sprawność fizyczna i sportowa','Umiejętność logicznego myślenia','Empatia i chęć niesienia pomocy innym','Zainteresowanie technologiami cyfrowymi','Dobra orientacja w przestrzeni','Zdolności muzyczne i poczucie rytmu','Łatwość nawiązywania kontaktów'], 'mocne'))
    b += ta('Inne / dodatkowe mocne strony', 'mocne_inne', 2)
    b += blk(sec('2', 'System motywacji dziecka (na podstawie mocnych stron)'))
    b += blk(checks(['System żetonowy (punkty / naklejki)','Kontrakt behawioralny (zasady i nagrody)','Wzmocnienia pozytywne (pochwały)','Tablica wyboru nagród (autonomia)','System „First-Then" (najpierw zadanie, potem nagroda)','Wykorzystanie zainteresowań jako nagroda','Przerwy na relaksację jako wzmocnienie','Funkcja pomocnika nauczyciela'], 'motyw'))
    b += ta('Inne / uwagi do systemu motywacji', 'motyw_inne', 2)
    page('WOPFU — mocne strony i motywacja', 'WOPFU · 1–2', b)

def s05():
    b = blk(sec('3', 'Przyczyny niepowodzeń edukacyjnych · trudności i bariery'))
    b += blk(checks(['Trudności z koncentracją uwagi','Niska samoocena i lęk przed porażką','Trudności w rozumieniu poleceń złożonych','Problemy z grafomotoryką i tempem pisania','Trudności w relacjach rówieśniczych','Bariery komunikacyjne (mowa, język)','Nadwrażliwość sensoryczna (hałas, światło)','Trudności w planowaniu i organizacji pracy','Niska motywacja do wysiłku','Trudności w radzeniu sobie z emocjami'], 'bariery'))
    b += ta('Inne / dodatkowe', 'bariery_inne', 2)
    b += legal(f'<b>Przyczyny niepowodzeń i bariery.</b> WOPF uwzględnia „występujące trudności w funkcjonowaniu dziecka (…) oraz, w zależności od potrzeb, zakres i charakter wsparcia ze strony nauczycieli, specjalistów (…) lub przyczyny niepowodzeń edukacyjnych albo trudności w funkcjonowaniu dziecka, w tym bariery i ograniczenia utrudniające funkcjonowanie i uczestnictwo dziecka w życiu przedszkola" — § 6 ust. 10 {KSs}.')
    b += blk(sec('4', 'Obserwacja ABC — analiza zachowania'))
    b += howto('Czym jest obserwacja ABC?', 'Metoda funkcjonalnej analizy zachowania — pozwala zrozumieć przyczynę i cel zachowania trudnego, a nie tylko je oceniać. Notujemy trzy elementy: A — poprzednik, B — zachowanie (opis faktów, bez ocen), C — następstwo (reakcja otoczenia, która zachowanie podtrzymuje lub wygasza). Cel: rozpoznać funkcję i nauczyć zachowania zastępczego (model pozytywnego wsparcia — PBS).')
    A = ['Polecenie nauczyciela','Zmiana aktywności','Hałas w sali','Trudne zadanie','Brak uwagi dorosłego','Odmowa prośby','Przerwa / czas wolny','Interakcja z rówieśnikiem']
    B = ['Krzyk / hałasowanie','Odmowa wykonania zadania','Agresja słowna / fizyczna','Ucieczka z miejsca pracy','Niszczenie przedmiotów','Autoagresja','Płacz / wycofanie','Ignorowanie poleceń']
    C = ['Upomnienie słowne','Przerwanie zadania','Odesłanie do wyciszenia','Utrata przywileju','Pomoc w wykonaniu zadania','Ignorowanie zachowania','Kontakt z rodzicem','Pochwała za uspokojenie']
    col = lambda t, items, key, color: f'<div class="pc"><div><div class="subhead {color}" style="margin-top:2px">{t}</div>{checks(items, key, cols=1)}</div></div>'
    b += blk('<div class="pair">' + col('A · Poprzednik', A, 'abcA', 'blue') + col('B · Zachowanie', B, 'abcB', 'red') + col('C · Konsekwencja', C, 'abcC', 'green') + '</div>')
    page('WOPFU — bariery i obserwacja ABC', 'WOPFU · 3–4', b)

OBSZARY = ['Uczenie się i stosowanie wiedzy','Ogólne zadania i obowiązki','Porozumiewanie się i mowa','Motoryka i poruszanie się','Dbanie o siebie i samoobsługa','Życie domowe','Wzajemne kontakty i relacje','Edukacja i zabawa','Życie w grupie i społeczności']
def s06():
    b = kick('Część II · IPET')
    b += blk(sec('1', 'Podsumowanie obszarów KPOF'))
    rows = []
    for i, o in enumerate(OBSZARY):
        d = D['kpof'][i] if WYP else None
        rows.append([nr(i+1), f'<td><b class="p">{o}</b></td>',
                     cell(d[0]+' / 5' if d else '', 'np. 14/20', f'kpof:{i}:0', 'gray' if not d else ''),
                     cell(d[1] if d else '', 'K, N, R…', f'kpof:{i}:1', 'gray' if not d else ''),
                     cell(d[2] if d else '', 'W / Ś / K', f'kpof:{i}:2', 'gray' if not d else ''),
                     cell(d[3] if d else '', 'I / II / III', f'kpof:{i}:3', 'gray' if not d else '')])
    b += table(['Lp.','Obszar funkcjonowania','Pkt (średnia)','Ocen.','Etap','Poziom'], rows, widths=[None,None,'22mm','20mm','18mm','18mm'])
    p = V('kpof_poziom')
    b += blk('<div style="display:flex;align-items:center;gap:8px;font-size:8.6px;font-weight:800;color:#2D1B69"><span>Rekomendowany ogólny poziom wsparcia:</span>' + ''.join(f'<span class="c" style="display:inline-flex;gap:6px;align-items:center;border:1.3px solid {"#E8450A" if p==l else "#cfc2e8"};border-radius:8px;padding:3px 9px;font-weight:700;color:#3d384c">{bx(p==l, "kpof_poziom:"+l)}Poziom {l}</span>' for l in ('I','II','III')) + '</div>')
    b += legal(f'Średnie z KPOF (skala 1–5) przeniesione z WOPF z 25.09.2026 (sekcja V). Kwalifikacja poziomów: średnia ≥ 3,0 — Poziom I; 2,0–2,9 — Poziom II; &lt; 2,0 — Poziom III (Model Szkolnej Oceny Funkcjonalnej, MEN 2024). Ocen.: N — nauczyciel, R — rodzic, S — specjalista; etap: W — wstępna, Ś — śródroczna, K — końcowa. Wielospecjalistyczna ocena poziomu funkcjonowania poprzedza opracowanie programu — § 6 ust. 4 {KSs}.')
    page('Podsumowanie obszarów KPOF', 'IPET · KPOF', b)

ZORZ = {1:('1 · Organizacja kształcenia i warunki edukacyjne',['Kształcenie w oddziale ogólnodostępnym / integracyjnym z dodatkowym wsparciem','Wsparcie nauczyciela współorganizującego kształcenie (autyzm, niepełnosprawność sprzężona)','Zajęcia rewalidacyjne w wymiarze wynikającym z przepisów (min. 2 godz. tyg.)','Zmniejszona liczebność grupy / stałe, ustalone miejsce w sali','Stały, przewidywalny plan dnia i uprzedzanie o zmianach','Dostosowanie czasu pracy — krótkie zadania, przerwy na regenerację','Strefa wyciszenia / miejsce odpoczynku sensorycznego','Ograniczenie nadmiaru bodźców (hałas, światło, dekoracje)']),
        2:('2 · Zajęcia specjalistyczne i terapia',['Terapia logopedyczna / rozwijanie komunikacji','Zajęcia rozwijające kompetencje emocjonalno-społeczne (TUS)','Terapia integracji sensorycznej (SI)','Terapia ręki i usprawnianie motoryki','Zajęcia korekcyjno-kompensacyjne','Wsparcie psychologiczne','Zajęcia rozwijające umiejętności uczenia się i funkcje poznawcze','Fizjoterapia / rehabilitacja ruchowa (wg potrzeb)']),
        3:('3 · Metody i formy pracy',['Metody oparte na pozytywnych wzmocnieniach (PBS) i systemie żetonowym','Praca na konkretach, stopniowanie trudności, metoda małych kroków','Wsparcie wizualne: piktogramy, plan „co teraz / co potem", historyjki społeczne','Komunikacja wspomagająca i alternatywna (AAC — PECS, MAKATON) wg potrzeb','Model ABC / analiza funkcjonalna trudnych zachowań','Uczenie wielozmysłowe i naprzemienność aktywności','Instrukcje krótkie, jednoznaczne, poparte pokazem (modelowanie)','Częste sprawdzanie zrozumienia i pozytywna informacja zwrotna']),
        4:('4 · Komunikacja, samodzielność i rozwój emocjonalno-społeczny',['Rozwijanie komunikacji funkcjonalnej i inicjowania kontaktu','Trening samoobsługi i samodzielności w czynnościach dnia (TFC)','Nauka rozpoznawania i nazywania emocji oraz strategii samoregulacji','Trening umiejętności społecznych — czekanie na kolej, współdziałanie','Nauka zasad i norm społecznych na konkretnych sytuacjach','Wzmacnianie mocnych stron, zainteresowań i motywacji dziecka']),
        5:('5 · Współpraca z rodzicami i środowiskiem',['Ujednolicenie oddziaływań przedszkole–dom (wspólne zasady i strategie)','Instruktaż i wsparcie dla rodziców, materiały do pracy w domu','Bieżąca wymiana informacji o postępach i trudnościach','Współpraca z poradnią psychologiczno-pedagogiczną i specjalistami','Koordynacja działań zespołu (nauczyciele i specjaliści)','Współpraca z lekarzem / terapeutami prowadzącymi (wg potrzeb)']),
        6:('6 · Monitorowanie i ewaluacja',['Okresowa wielospecjalistyczna ocena efektywności (min. 2× w roku)','Monitorowanie postępów według celów SMART','Modyfikacja IPET zależnie od postępów dziecka','Dokumentowanie realizacji zajęć (dziennik, karty obserwacji)','Ocena gotowości szkolnej i przygotowanie do przejścia do szkoły','Włączenie dziecka i rodziców w ocenę i planowanie wsparcia'])}
def grupa_checks(dct, key, g, color):
    t, items = dct[g]
    on = lambda i: WYP and i in D[key].get(g, set())
    return blk(subhead(t, color)) + blk(checks(items, on=on, kfmt=lambda i: f'{key}:{g}:{i}'))

def s07():
    b = kick('Zalecenia z orzeczenia do IPET · przedszkole · dziecko z orzeczeniem')
    b += h1('Zalecenia z orzeczenia do IPET') + tsub('do wyboru — zgodne z orzeczeniem o potrzebie kształcenia specjalnego')
    b += note('Gotowy bank zaleceń do wyboru — zaznacz te, które wynikają z orzeczenia i odpowiadają potrzebom dziecka, a następnie przenieś je do tabeli 2 (sposób realizacji uzupełnij indywidualnie). Zaznaczone zalecenia muszą być zgodne z treścią orzeczenia o potrzebie kształcenia specjalnego.')
    b += blk(f'<div class="tools"><b>Podstawa.</b> Zalecenia realizowane są w IPET na podstawie orzeczenia — § 5–6 {KSs}; formy pomocy psychologiczno-pedagogicznej — {PPs}.</div>')
    b += grupa_checks(ZORZ, 'zorz', 1, 'purple') + grupa_checks(ZORZ, 'zorz', 2, 'blue') + grupa_checks(ZORZ, 'zorz', 3, 'green')
    page('Zalecenia z orzeczenia do IPET (1/2)', 'IPET · zalecenia', b)
def s08():
    b = kick('Zalecenia z orzeczenia do IPET · c.d.')
    b += grupa_checks(ZORZ, 'zorz', 4, 'amber') + grupa_checks(ZORZ, 'zorz', 5, 'purple') + grupa_checks(ZORZ, 'zorz', 6, 'red')
    b += blk(sec('7', 'Zalecenia dodatkowe / indywidualne'))
    b += ta('Wpisz zalecenia specyficzne dla dziecka, niewymienione powyżej — zgodnie z orzeczeniem i potrzebami.', 'zorz_dod', 4, grow=True)
    b += legal('Powyższy katalog ma charakter pomocniczy i do wyboru. O doborze zaleceń decyduje zespół na podstawie orzeczenia o potrzebie kształcenia specjalnego, opinii oraz wielospecjalistycznej oceny poziomu funkcjonowania dziecka. Zakres, formy i wymiar wsparcia ustala dyrektor przedszkola.', label='Uwaga')
    page('Zalecenia z orzeczenia do IPET (2/2)', 'IPET · zalecenia', b)

def s09():
    b = blk(sec('2', 'Zalecenia z orzeczenia o potrzebie kształcenia specjalnego i sposób realizacji'))
    rows = []
    zt = D['zorz_tab'] if WYP else [('Włączenie dziecka i rodziców w ocenę i planowanie wsparcia','Uwzględnianie „głosu dziecka" (część „Mój głos") i opinii rodziców w planowaniu celów i ocenie efektywności.')]
    n = max(len(zt), 4)
    for i in range(n):
        z = zt[i] if i < len(zt) else ('','')
        rows.append([nr(i+1), cell(z[0], 'Zalecenie (treść z orzeczenia)', f'zorz_tab:{i}:0', 'gray' if not WYP else ''), cell(z[1], 'Sposób realizacji w przedszkolu / placówce', f'zorz_tab:{i}:1', 'gray' if not WYP else '')])
    b += table(['Lp.','Zalecenie (treść z orzeczenia)','Sposób realizacji w przedszkolu / placówce'], rows, widths=[None,'44%',None])
    b += blk(sec('3', 'Zalecenia z opinii psychologiczno-pedagogicznej i sposób realizacji'))
    rows = []
    zo = D['zopin_tab'] if WYP else []
    for i in range(4):
        z = zo[i] if i < len(zo) else ('','')
        rows.append([nr(i+1), cell(z[0], 'Zalecenie (treść z opinii PPP)', f'zopin_tab:{i}:0'), cell(z[1], 'Sposób realizacji', f'zopin_tab:{i}:1')])
    b += table(['Lp.','Zalecenie (treść z opinii PPP)','Sposób realizacji'], rows, widths=[None,'44%',None])
    b += legal(f'Zespół opracowuje program po dokonaniu wielospecjalistycznej oceny poziomu funkcjonowania dziecka, uwzględniając diagnozę i wnioski sformułowane na jej podstawie oraz zalecenia zawarte w orzeczeniu o potrzebie kształcenia specjalnego — § 6 ust. 4 {KSs}. Opinia poradni — {ORZ}.')
    page('Zalecenia z orzeczenia i opinii PPP', 'IPET · zalecenia', b)

ZWOPF = {1:('1 · Sfera poznawcza — uczenie się i edukacja',['Wydłużać czas na wykonanie zadania i dzielić je na etapy (małe kroki)','Pracować na konkretach i materiale poglądowym, wielozmysłowo','Wspierać uwagę i pamięć — krótkie zadania, powtórzenia, przypomnienia','Stosować wsparcie wizualne (plan aktywności, piktogramy, wzory)','Sprawdzać zrozumienie i dawać pozytywną informację zwrotną','Wykorzystywać zainteresowania dziecka do budowania motywacji']),
         2:('2 · Sfera emocjonalno-społeczna',['Uczyć rozpoznawania i nazywania emocji oraz strategii samoregulacji','Trenować umiejętności społeczne — czekanie na kolej, współdziałanie','Stosować wspólny system motywacyjny i pozytywne wzmocnienia','Reagować jednolicie na trudne zachowania (model ABC / PBS)','Zapewnić strefę wyciszenia i wsparcie w sytuacjach trudnych','Wzmacniać relacje z rówieśnikami i poczucie przynależności do grupy']),
         3:('3 · Sfera funkcjonowania motorycznego',['Usprawniać motorykę małą, chwyt i grafomotorykę (terapia ręki)','Wspierać motorykę dużą — równowagę, koordynację, planowanie ruchu','Dostosować pomoce (nakładki na kredki, nożyczki, podpórki)','Zapewnić przerwy ruchowe i aktywność naprzemienną','Stosować ćwiczenia stabilizacji posturalnej','Włączyć elementy integracji sensorycznej wg potrzeb']),
         4:('4 · Sfera mowy i komunikacji',['Rozwijać komunikację funkcjonalną i inicjowanie kontaktu','Wprowadzać komunikację wspomagającą i alternatywną (AAC — PECS, MAKATON) wg potrzeb','Modelować wypowiedzi i dawać czas na odpowiedź','Wspierać rozumienie poleceń (krótkie, jednoznaczne, poparte pokazem)','Współpracować z logopedą i przenosić ćwiczenia do grupy','Wspierać słuch fonematyczny i wzbogacać słownictwo']),
         5:('5 · Sfera samodzielności — dbanie o siebie',['Trenować samoobsługę i czynności dnia codziennego małymi krokami','Stosować plany wizualne czynności (ubieranie, jedzenie, higiena)','Stopniowo zmniejszać wsparcie („wygaszanie podpowiedzi")','Uczyć w sytuacjach naturalnych i utrwalać rutyny','Wzmacniać każdą próbę samodzielności','Współpracować z rodzicami w ujednoliceniu wymagań']),
         6:('6 · Sfera ogólnych zadań i zabawy',['Wspierać podejmowanie i kończenie zadań (rutyny, plany)','Rozwijać zabawę — od równoległej do wspólnej i tematycznej','Uczyć radzenia sobie ze zmianą i elastyczności','Stosować przewidywalny rytm dnia i uprzedzać o zmianach','Wspierać przenoszenie umiejętności między sytuacjami (transfer)','Rozwijać wytrwałość i odporność na trudności (małe wyzwania)'])}
def s10():
    b = kick('Zalecenia do wyboru z WOPF · zgodne z obserwacją KPOF i obserwacją pogłębioną')
    b += h1('Zalecenia do wyboru z WOPF') + tsub('do wyboru — zgodne z obserwacją KPOF oraz obserwacją pogłębioną')
    b += note('Bank zaleceń wynikających z wielospecjalistycznej oceny poziomu funkcjonowania (WOPF) — z obserwacji KPOF oraz obserwacji pogłębionej. Zaznacz zalecenia odpowiadające rozpoznanym mocnym stronom i trudnościom dziecka w poszczególnych sferach; przenieś wybrane do celów SMART i dostosowań.')
    b += blk('<div class="tools"><b>Skąd te zalecenia?</b> Wynikają z obserwacji funkcjonalnej dziecka (KPOF) i obserwacji pogłębionej ujętych w WOPF — nie z orzeczenia. Uzupełniają zalecenia z orzeczenia o praktyczne wskazania zespołu do codziennej pracy.</div>')
    b += grupa_checks(ZWOPF, 'zwopf', 1, 'purple') + grupa_checks(ZWOPF, 'zwopf', 2, 'red') + grupa_checks(ZWOPF, 'zwopf', 3, 'green')
    page('Zalecenia do wyboru z WOPF (1/2)', 'IPET · zalecenia WOPF', b)
def s11():
    b = kick('Zalecenia do wyboru z WOPF · c.d.')
    b += grupa_checks(ZWOPF, 'zwopf', 4, 'blue') + grupa_checks(ZWOPF, 'zwopf', 5, 'amber') + grupa_checks(ZWOPF, 'zwopf', 6, 'purple')
    b += blk(sec('7', 'Zalecenia z WOPF — dodatkowe / indywidualne'))
    b += ta('Wpisz zalecenia wynikające z obserwacji KPOF i pogłębionej, specyficzne dla dziecka, niewymienione powyżej.', 'zwopf_dod', 4, grow=True)
    b += legal(f'Wielospecjalistyczna ocena poziomu funkcjonowania dziecka (WOPF) oraz uwzględnienie jej wyników w IPET — § 6 ust. 4 i 9 {KSs}. Zalecenia z WOPF wynikają z obserwacji zespołu i uzupełniają zalecenia z orzeczenia.', label='Podstawa')
    page('Zalecenia do wyboru z WOPF (2/2)', 'IPET · zalecenia WOPF', b)
def s12():
    b = kick('Zalecenia z WOPF do IPET · zestawienie wybranych')
    b += h1('Zalecenia z WOPF — zestawienie') + tsub('wybrane z katalogu WOPF — zgodne z obserwacją KPOF i pogłębioną')
    b += note('Zalecenia wybrane z katalogu WOPF (sfery funkcjonowania). W wersji interaktywnej wskakują tu automatycznie po zaznaczeniu w katalogu; „sposób realizacji / sfera" uzupełnij indywidualnie. W wersji papierowej wpisz wybrane zalecenia ręcznie.')
    zt = D['zwopf_tab'] if WYP else [('Wydłużać czas na wykonanie zadania i dzielić je na etapy (małe kroki)','Sfera 1: dodatkowy czas i podział zadania na etapy (metoda małych kroków) — w zajęciach grupowych i programie „Funkcje poznawcze"; realizują nauczyciel grupy i pedagog.'),('Pracować na konkretach i materiale poglądowym, wielozmysłowo','Sfera 1: praca na materiale poglądowym i wielozmysłowo — w każdej aktywności oraz na zajęciach rozwijających funkcje poznawcze.')]
    rows = [[nr(i+1), cell(z[0], '', f'zwopf_tab:{i}:0'), cell(z[1], '', f'zwopf_tab:{i}:1', 'gray' if not WYP else '')] for i, z in enumerate(zt)]
    b += table(['Lp.','Zalecenie (z WOPF)','Sposób realizacji / sfera'], rows, cls='tb small', widths=[None,'40%',None])
    b += legal(f'Zalecenia z wielospecjalistycznej oceny poziomu funkcjonowania (WOPF) — § 6 ust. 4 i 9 {KSs}. Wynikają z obserwacji zespołu (KPOF, obserwacja pogłębiona) i uzupełniają zalecenia z orzeczenia.', label='Podstawa')
    page('Zalecenia z WOPF — zestawienie', 'IPET · zalecenia WOPF', b)

SFERY = {
 1:dict(t='Sfera 1 — Poznawcze (uczenie się, edukacja)', sub='Poznawcze', tools='KPOF (obsz. I, VIII) · obserwacja uwagi, pamięci i myślenia · analiza wytworów (rysunki, układanki) · Profil biopsychospołeczny (ICF) · Mocne strony dziecka &nbsp;·&nbsp; <b>Kody ICF:</b> d110–d179 · d820 · b140 (uwaga) · b144 (pamięć) · b164 (f. wykonawcze) · b1720 (myślenie)',
   trud=['Spostrzeganie','Uwaga i koncentracja','Pamięć','Myślenie i wnioskowanie','Umiejętności wykonawcze','Tempo uczenia się'],
   wynik_ph='Obszar „Uczenie się i stosowanie wiedzy" — wynik niski 6/20 pkt (średnia 1,50 · skala 1–5), co odpowiada kwalifikacji:', chip_ph='III',
   lv=['Dziecko pracuje w większości samodzielnie; potrzebuje okazjonalnych wskazówek, przypomnień i sprawdzenia efektu pracy.','Funkcje częściowo obniżone — realizuje zadania z dodatkowym czasem, podziałem na etapy, wsparciem wizualnym i przypomnieniami.','Funkcje znacznie ograniczone — pracuje krok po kroku ze stałym wsparciem dorosłego, na konkretach, z pomocą „ręka na rękę".'],
   motyw_ph='System żetonowy, wykorzystanie zainteresowań dziecka jako nagrody, pochwała opisowa.',
   cele_ph=[('Cel terapeutyczny','w sytuacjach wymagających skupienia uwagi wzrokowej (na osobie, nowym obiekcie, sytuacji) dziecko wykona zadanie z częściową pomocą dorosłego w 4 na 5 prób (stan wyjściowy: wymaga stałego wsparcia).'),('Cel edukacyjny','dziecko rozwiąże zadanie podzielone na etapy, korzystając ze wsparcia wizualnego, poprawnie w 4 na 5 prób w okresie ewaluacyjnym.')],
   zint_ph='Wszyscy nauczyciele stosują krótkie, jednoznaczne polecenia, dzielą materiał na mniejsze partie, dają dodatkowy czas i wsparcie wizualne oraz utrwalają kluczowe treści.',
   metody=['Praca na konkretach i wielozmysłowa','Ćwiczenia uwagi i pamięci','Stopniowanie trudności i powtórki','Mapy myśli i notatki'], formy=['Indywidualna (1:1)','Mała grupa','Z całą grupą','Współpraca przedszkole–dom'],
   pomoce_ph='Karty pracy, plansze edukacyjne, materiały manipulacyjne, gry dydaktyczne, programy multimedialne, mapy myśli.'),
 2:dict(t='Sfera 2 — Emocjonalno-społeczne (kontakty, społeczność)', sub='Emocjonalno-społeczne', tools='KPOF (obsz. VII, IX) · Karta obserwacji Teorii umysłu (ToM, przedszkole) · Karta analizy i wsparcia zachowania (ABC/FBA/MPS) · obserwacja zabawy i relacji &nbsp;·&nbsp; <b>Kody ICF:</b> d710–d770 · b152 (f. emocji) · b1251 (przystosowanie) · d250 (kontrola zachowania) · b1801 (empatia/ToM) · d910–d950',
   trud=['Rozpoznawanie i nazywanie emocji','Regulacja emocji i samokontrola','Naprzemienność / czekanie na kolej','Współdziałanie z rówieśnikami','Relacje i kontakty','Empatia i teoria umysłu'],
   wynik_ph='Obszar „Wzajemne kontakty i związki" — wynik przeciętny 10/20 pkt (średnia 2,50 · skala 1–5), co odpowiada kwalifikacji:', chip_ph='II',
   lv=['Nawiązuje kontakt i reguluje emocje w większości sytuacji; potrzebuje okazjonalnego przypomnienia zasad.','Funkcje częściowo obniżone — współdziała i reguluje emocje z podpowiedzią, wsparciem wizualnym i wcześniej wyćwiczoną strategią.','Funkcje znacznie ograniczone — wymaga stałej obecności dorosłego, mediacji w relacjach i pomocy „krok po kroku" w sytuacjach społecznych.'],
   motyw_ph='Wzmocnienia pozytywne, system „First-Then", funkcja pomocnika nauczyciela.',
   cele_ph=[('Cel terapeutyczny','w sytuacji narastającego napięcia dziecko zastosuje wyćwiczoną strategię wyciszenia (np. „termometr emocji") z podpowiedzią dorosłego w 7 na 10 sytuacji.'),('Cel społeczny','podczas zadania w parze dziecko poczeka na swoją kolej i odpowie na inicjatywę rówieśnika w 7 na 10 prób. Pomiar: obserwacja na zajęciach i karta postępów.')],
   zint_ph='Zespół stosuje jednolity system motywacyjny i spójne reagowanie na zachowania trudne (model ABC/FBA); prowadzi trening umiejętności społecznych i wzmocnienia pozytywne.',
   metody=['Trening umiejętności społecznych, emocjonalnych i komunikacyjnych (TUS / TUE / TUK)','Modelowanie i odgrywanie ról (drama)','Historyjki społeczne','„Termometr emocji" i techniki regulacji'], formy=['W grupie','W parach','Indywidualna (1:1)','Strefa wyciszenia'],
   pomoce_ph='Karty emocji, „termometr emocji", historyjki społeczne, plansze zasad, kącik wyciszenia.'),
 3:dict(t='Sfera 3 — Funkcjonowanie motoryczne', sub='Motoryczne', tools='KPOF (obsz. IV) · Profil sensoryczny dziecka (model Dunn) · obserwacja motoryki małej i dużej · ćwiczenia grafomotoryczne i terapia ręki &nbsp;·&nbsp; <b>Kody ICF:</b> d440–d455 · b760 (kontrola ruchów) · b147 (praksja) · b156 (percepcja) · b235 (przedsionek) · d170 (pisanie)',
   trud=['Napięcie mięśniowe / posturalne','Koordynacja ruchowa','Koordynacja obustronna i oko–ręka','Praksja — planowanie ruchu','Motoryka mała i chwyt','Grafomotoryka i pisanie'],
   wynik_ph='Obszar „Motoryka i poruszanie się" — wynik przeciętny 11/20 pkt (średnia 2,75 · skala 1–5), co odpowiada kwalifikacji:', chip_ph='II',
   lv=['Sprawność motoryczna w normie w większości zadań; potrzebuje okazjonalnej korekty chwytu lub tempa.','Funkcje częściowo obniżone — pisze i wykonuje ćwiczenia manualne z dostosowaniami (nakładka, liniatura, dodatkowy czas).','Funkcje znacznie ograniczone — wymaga stałej pomocy fizycznej, sprzętu specjalistycznego i pracy „ręka na rękę".'],
   motyw_ph='Docenianie wysiłku i postępu, przerwy ruchowe jako wzmocnienie.',
   cele_ph=[('Cel terapeutyczny','dziecko wykona ćwiczenie grafomotoryczne z prawidłowym chwytem narzędzia (z nakładką) w 7 na 10 prób.'),('Cel edukacyjny','dziecko przepisze krótki tekst w wyznaczonej liniaturze, mieszcząc litery, w 7 na 10 prób. Pomiar: obserwacja na zajęciach i karta postępów.')],
   zint_ph='Nauczyciele zapewniają dostosowania (nakładki, liniatura, możliwość pisania na komputerze), przerwy ruchowe i bezpieczne modyfikacje ćwiczeń.',
   metody=['Ćwiczenia grafomotoryczne i manualne','Terapia ręki','Zabawy ruchowe i przerwy sensoryczne','Integracja sensoryczna (SI)'], formy=['Indywidualna (1:1)','Mała grupa','Przerwy sensoryczno-ruchowe','Z asystą'],
   pomoce_ph='Nakładki na przybory, liniatura powiększona, masy plastyczne, sprzęt do terapii ręki, sorter, przybory do chwytu.'),
 4:dict(t='Sfera 4 — Mowa i komunikacja', sub='Mowa i komunikacja', tools='KPOF (obsz. III) · Kwestionariusz mowy i komunikacji (logopedyczny, przedszkole) · obserwacja słuchu fonematycznego · obserwacja komunikacji i wskazań do AAC &nbsp;·&nbsp; <b>Kody ICF:</b> d310–d360 · b320 (artykulacja) · b1560 (słuch fonematyczny) · b16700/b16710 (język) · d3350 (narracja)',
   trud=['Rozumienie mowy','Przetwarzanie słuchowe / fonematyczne','Artykulacja i wymowa','Słownictwo i gramatyka — język','Budowanie wypowiedzi / narracja','Komunikacja wspomagająca / AAC'],
   wynik_ph='Obszar „Porozumiewanie się" — wynik obniżony 9/20 pkt (średnia 2,25 · skala 1–5), co odpowiada kwalifikacji:', chip_ph='II',
   lv=['Komunikuje potrzeby i rozumie polecenia w większości sytuacji; potrzebuje okazjonalnego powtórzenia lub uproszczenia.','Funkcje częściowo obniżone — komunikuje się z podpowiedzią, wsparciem wizualnym i wydłużonym czasem na wypowiedź.','Funkcje znacznie ograniczone — porozumiewa się głównie przez AAC (PECS, piktogramy) ze stałym wsparciem dorosłego.'],
   motyw_ph='Pochwała za każdą próbę komunikacji, tablica wyboru, obrazkowe wzmocnienia.',
   cele_ph=[('Cel komunikacyjny','dziecko zgłosi potrzebę lub prośbę, korzystając z mowy lub AAC (PECS / piktogram), samodzielnie w 7 na 10 sytuacji.'),('Cel edukacyjny','dziecko ułoży 3–4-wyrazową wypowiedź na temat obrazka z podpowiedzią wizualną w 7 na 10 prób. Pomiar: obserwacja i karta postępów.')],
   zint_ph='Nauczyciele ujednolicają sposób wydawania poleceń, stosują wsparcie wizualne i AAC, wydłużają czas na wypowiedź; logopeda prowadzi terapię mowy.',
   metody=['Ćwiczenia logopedyczne','Modelowanie wypowiedzi','Komunikacja wspomagająca (AAC / PECS)','Ćwiczenia słuchu fonematycznego'], formy=['Terapia 1:1','Mała grupa','Wsparcie w przedszkolu','Współpraca z logopedą'],
   pomoce_ph='Tablice i karty AAC / PECS, piktogramy, lustro logopedyczne, obrazki sytuacyjne, aplikacje komunikacyjne.'),
 5:dict(t='Sfera 5 — Samodzielność (dbanie o siebie)', sub='Samodzielność', tools='KPOF (obsz. V, VI) · obserwacja funkcjonalna samoobsługi · Profil biopsychospołeczny i sensoryczny · wywiad z rodzicem &nbsp;·&nbsp; <b>Kody ICF:</b> d510–d570 · b164 (planowanie) · b1252 (impulsywność) · d230 (rutyna) · b134 (sen/energia)',
   trud=['Higiena i dbanie o siebie','Ubieranie się','Jedzenie','Samodzielność i zaradność','Organizacja rzeczy','Bezpieczeństwo'],
   wynik_ph='Obszar „Dbanie o siebie i samoobsługa" — wynik przeciętny 10/20 pkt (średnia 2,50 · skala 1–5), co odpowiada kwalifikacji:', chip_ph='II',
   lv=['Wykonuje czynności samoobsługowe samodzielnie; potrzebuje okazjonalnego przypomnienia kolejności.','Funkcje częściowo obniżone — realizuje czynności według planu wizualnego, z częściową pomocą i przypomnieniami.','Funkcje znacznie ograniczone — wymaga stałej asysty dorosłego i prowadzenia „krok po kroku" w większości czynności.'],
   motyw_ph='Tablica osiągnięć, nagroda za samodzielność, autonomia w wyborze.',
   cele_ph=[('Cel terapeutyczny','w sytuacjach dbania o higienę osobistą dziecko wykona czynność (np. mycie rąk, porządkowanie miejsca) według planu wizualnego z częściową pomocą w 4 na 5 prób. Pomiar: karta monitoringu samodzielności.')],
   zint_ph='Zespół stosuje stałą, przewidywalną rutynę i plan wizualny czynności, stopniowo wycofuje pomoc i wzmacnia samodzielność.',
   metody=['Trening samodzielności metodą małych kroków','Plany wizualne czynności','Modelowanie i instruktaż','Nauka w sytuacjach naturalnych'], formy=['Indywidualna (1:1)','W sytuacjach naturalnych','Z asystą','Współpraca przedszkole–dom'],
   pomoce_ph='Plany wizualne czynności, piktogramy krok po kroku, tablica osiągnięć, materiały do treningu samodzielności.'),
 6:dict(t='Sfera 6 — Ogólne zadania i zabawa', sub='Ogólne zadania i zabawa', tools='KPOF (obsz. II, VIII) · obserwacja funkcji wykonawczych · Karta analizy zachowania (ABC — organizacja, samokontrola) · wywiad z rodzicem &nbsp;·&nbsp; <b>Kody ICF:</b> d210–d250 · d610–d660 · b1641 (organizacja) · b1643 (elastyczność) · d240 (radzenie ze stresem) · d160 (uwaga w zadaniu)',
   trud=['Rozpoczynanie zadania','Zadania złożone','Organizacja i rutyna','Radzenie sobie ze stresem','Planowanie / f. wykonawcze','Życie domowe'],
   wynik_ph='Obszar „Ogólne zadania i obowiązki" — wynik niski 8/20 pkt (średnia 2,00 · skala 1–5), co odpowiada kwalifikacji:', chip_ph='III',
   lv=['Rozpoczyna i kończy zadania samodzielnie; potrzebuje okazjonalnego przypomnienia o kolejnych krokach.','Funkcje częściowo obniżone — realizuje zadania według checklisty, z dodatkowym czasem i przypomnieniami.','Funkcje znacznie ograniczone — pracuje krok po kroku ze stałym wsparciem dorosłego, na konkretach i z pomocą „ręka na rękę".'],
   motyw_ph='Checklisty z nagrodą za ukończenie, kontrakt behawioralny, przerwy.',
   cele_ph=[('Cel terapeutyczny','w sytuacjach wymagających utrzymania porządku w otoczeniu dziecko wykona zadanie (rozpoczęcie–realizacja–zakończenie) według checklisty z częściową pomocą dorosłego w 4 na 5 prób. Pomiar: karta postępów.')],
   zint_ph='Nauczyciele dostarczają checklisty i plan dnia, przypominają o kolejnych krokach, wspierają w organizacji pracy i radzeniu sobie ze zmianą.',
   metody=['Planowanie krok po kroku (checklisty)','Trening funkcji wykonawczych','Instruktaż i przypomnienia','Organizacja warsztatu pracy'], formy=['Indywidualna (1:1)','Mała grupa','Z całą grupą','Współpraca przedszkole–dom'],
   pomoce_ph='Checklisty i plan dnia, planery, timery / klepsydry, karty „co teraz / co potem", organizery.'),
}
def s_smart(n):
    S = SFERY[n]; Z = D['sfery'][n] if WYP else None
    b = ''
    if n == 1: b += blk(sec('4', 'Cele edukacyjne i terapeutyczne (SMART) — sfery funkcjonowania'))
    else: b += kick(f'Cele SMART — sfera {n}')
    b += blk(f'<div class="sfera"><span class="sn">{n}</span><span class="st">{S["t"]}</span></div>')
    b += blk(f'<div class="tools"><b>Narzędzia oceny i obserwacji:</b> {S["tools"]}</div>')
    lv = Z['poziom'] if Z else None
    b += blk(subhead('Trudności i bariery — zaznacz występujące', 'red', lvls(lv, n)))
    b += blk(checks(S['trud'], on=lambda i: bool(Z) and i in Z['trud'], kfmt=lambda i: f'sf{n}:trud:{i}'))
    wt = Z['wynik'] if Z else S['wynik_ph']; ch = lv if Z else S['chip_ph']
    b += blk(f'<div class="wynik"><span class="wl">Wynik diagnozy</span><span class="wt" data-k="sf{n}:wynik">{esc(wt)}</span>{chip(ch, f"sf{n}:chip")}</div>')
    b += blk(subhead('Charakterystyka trudności wg poziomu wsparcia', 'red'))
    b += blk('<div class="lvl3">' + ''.join(f'<div class="lvl {c}"><div class="lvl-t"><span class="lvl-n">{l}</span>{t}</div><div class="lvl-x">{x}</div></div>' for (l, c, t), x in zip((('I','g','Wsparcie minimalne'),('II','a','Wsparcie umiarkowane'),('III','r','Wsparcie znaczne')), S['lv'])) + '</div>')
    b += blk(subhead('System motywacji — oparty na mocnych stronach', 'green'))
    b += blk(f'<div class="mini-ta" data-k="sf{n}:motyw">{esc(Z["motyw"] if Z else S["motyw_ph"])}</div>')
    cele = Z['cele'] if Z else S['cele_ph']
    b += blk('<div class="smart"><div class="sh">Cel SMART — wynika z trudności<span class="ch">' + ''.join(f'<span>{c}</span>' for c in 'SMART') + '</span></div><div class="lead2">Cele do IPET na okres do najbliższej ewaluacji okresowej:</div>' + ''.join(f'<div class="g" data-k="sf{n}:cel:{i}"><span><b>{esc(t)}:</b> {esc(x)}</span></div>' for i, (t, x) in enumerate(cele)) + '</div>')
    b += blk(subhead('Zintegrowane działania nauczycieli i specjalistów', 'purple'))
    b += blk(f'<div class="mini-ta" data-k="sf{n}:zint">{esc(Z["zint"] if Z else S["zint_ph"])}</div>')
    b += blk('<div class="pair"><div class="pc"><div>' + subhead('Metody pracy — zaznacz', 'red') + checks(S['metody'], on=lambda i: bool(Z) and i in Z['metody'], cols=1, kfmt=lambda i: f'sf{n}:met:{i}') + '</div></div><div class="pc"><div>' + subhead('Formy pracy — zaznacz', 'blue') + checks(S['formy'], on=lambda i: bool(Z) and i in Z['formy'], cols=1, kfmt=lambda i: f'sf{n}:for:{i}') + '</div></div></div>')
    b += blk(f'<div style="display:flex;gap:8px;align-items:baseline;font-size:7.8px;font-weight:800;letter-spacing:.6px;text-transform:uppercase;color:#2D1B69"><span>Inne — własne</span><span style="flex:1;border-bottom:1.2px dotted #b5a8d8;font-weight:400;text-transform:none;letter-spacing:0;font-size:8.8px;color:#2f2a3e" data-k="sf{n}:inne">{esc(Z["inne"]) if Z else "&nbsp;"}</span></div>')
    b += blk(subhead('Proponowane pomoce dydaktyczne', 'purple'))
    b += blk(f'<div class="mini-ta" data-k="sf{n}:pomoce">{esc(Z["pomoce"] if Z else S["pomoce_ph"])}</div>')
    page(f'Cel SMART · sfera {n} · {S["sub"]}', 'IPET · cele SMART', b)

def s_real(n):
    S = SFERY[n]; R = D['real'][n] if WYP else None
    b = blk(f'<div class="sfera"><span class="sn">{n}</span><span class="st">{S["t"]} — realizacja zaleceń</span></div>')
    b += note('Zapisz, jak w obrębie tej sfery realizowane są zalecenia — z orzeczenia, z opinii poradni psychologiczno-pedagogicznej oraz z WOPF (obserwacja KPOF i pogłębiona). Wpisz zalecenia dotyczące tej sfery i konkretne działania.')
    def tab(title, color, key, ph, rows_data):
        rows = []
        for i in range(3):
            z = rows_data[i] if rows_data and i < len(rows_data) else ('','')
            rows.append([nr(i+1), cell(z[0], ph, f'r{n}:{key}:{i}:0'), cell(z[1], 'Sposób realizacji / działania w sferze', f'r{n}:{key}:{i}:1')])
        return blk(subhead(title, color)) + table(['Lp.','Zalecenie (dot. sfery)','Sposób realizacji / działania w sferze'], rows, widths=[None,'44%',None])
    b += tab('Realizacja zaleceń z orzeczenia — w tej sferze', 'purple', 'orz', 'Zalecenie z orzeczenia', R['orz'] if R else None)
    opin = [('nie dotyczy — brak odrębnej opinii PPP (dziecko z orzeczeniem)','—')] if R else None
    b += tab('Realizacja zaleceń z opinii poradni psychologiczno-pedagogicznej (PPP)', 'blue', 'opin', 'Zalecenie z opinii PPP', opin)
    b += tab('Realizacja zaleceń z WOPF (obserwacja KPOF i pogłębiona)', 'green', 'wopf', 'Zalecenie z WOPF', R['wopf'] if R else None)
    b += blk(f'<div class="ta"><div class="tl">Uwagi do realizacji w tej sferze · osoby odpowiedzialne · terminy</div><div class="ed" data-k="r{n}:uwagi">{esc(R["uwagi"]) if R else ""}</div>{"" if R else "<div class=ln></div>"}</div>')
    b += blk(subhead('Załącznik — wybrany program dla tej sfery', 'purple'))
    b += blk('<div class="tools"><b>Do tej sfery dołączono wybrany program</b> (rewalidacyjny lub z pomocy psychologiczno-pedagogicznej) — zaznacz rodzaj, wpisz nazwę oraz numer załącznika. Program stanowi załącznik do IPET.</div>')
    zl = R['zal'] if R else ('','','','')
    b += blk(checks(['Program rewalidacyjny','Program z pomocy psychologiczno-pedagogicznej'], on=lambda i: (zl[0]=='rew' and i==0) or (zl[0]=='pp' and i==1), kfmt=lambda i: f'r{n}:zal:{i}'))
    b += blk(f'<div class="fields" style="grid-template-columns:2fr 1fr 1.4fr"><div class="f"><div class="fl">Nazwa wybranego programu</div><div class="fv small" data-k="r{n}:zal:nazwa">{esc(zl[1]) or "&nbsp;"}</div></div><div class="f"><div class="fl">Nr załącznika</div><div class="fv small" data-k="r{n}:zal:nr">{esc(zl[2]) or "&nbsp;"}</div></div><div class="f"><div class="fl">Realizator / wymiar godzin</div><div class="fv small" data-k="r{n}:zal:real">{esc(zl[3]) or "&nbsp;"}</div></div></div>')
    if n == 2:
        b += blk(subhead('Cele SMART załączonych programów — 3 progr. · 18 celów', 'amber'))
        pc = D['progcele'] if WYP else [('P1 · Teoria umysłu i empatia — Zał. 1',[]),('P2 · Zachowanie: model ABC i FBA — Zał. 2',[]),('P3 · Kompetencje społeczno-emocjonalne — Zał. 3',[])]
        b += blk('<div class="col4" style="grid-template-columns:1fr 1fr 1fr">' + ''.join(f'<div class="card"><div class="ct">{esc(t)}</div>' + (''.join(f'<div style="font-size:7.9px;color:#2f2a3e;line-height:1.4;margin-bottom:2px">✓ {esc(c)}</div>' for c in cs) if cs else '<div style="font-size:7.6px;color:#9a94ad;font-style:italic">cele wybrane z programu — zaznacz na karcie sfery 2</div>') + '</div>' for t, cs in pc) + '</div>')
    b += legal(f'IPET uwzględnia zalecenia zawarte w orzeczeniu i opinii poradni oraz wyniki wielospecjalistycznej oceny poziomu funkcjonowania (WOPF) — § 5–6 {KSs}. Wybrany program (rewalidacyjny / pomocy pp) stanowi załącznik do IPET; realizacja zaleceń w podziale na sfery zapewnia spójność edukacji i terapii.', label='Podstawa')
    page(f'Sfera {n} · realizacja zaleceń', 'IPET · realizacja zaleceń', b)

def s25():
    b = blk(sec('4 a', 'Zintegrowane działania nauczycieli i specjalistów'))
    b += note('Ogólny opis spójnych, wspólnych działań całego zespołu — tak, aby edukacja i terapia tworzyły jedną całość przez cały dzień w przedszkolu. Szczegółowe działania w każdej sferze ujęto w kartach celów SMART (sfery 1–6).')
    b += blk('<div class="tools"><b>Na czym polegają zintegrowane działania?</b> To wspólny cel, jednolite strategie i spójna komunikacja całego zespołu. Każdy dorosły stosuje te same zasady, ten sam system motywacyjny i te same pomoce — dziecko doświadcza przewidywalnego, spójnego wsparcia w każdej sytuacji.</div>')
    b += blk(subhead('Wspólne, spójne zasady całego zespołu — zaznacz', 'purple'))
    b += blk(checks(['Jednolity system poleceń (krótkie, jednoznaczne)','Wspólny system motywacyjny i te same nagrody','Spójne reagowanie na trudne zachowania (model ABC / PBS)','Wsparcie wizualne: plan dnia, piktogramy „co teraz / co potem"','Wspólny system komunikacji / AAC (PECS, MAKATON)','Stałe rutyny, uprzedzanie o zmianach, strefa wyciszenia','Ujednolicenie strategii przedszkole–dom','Bieżąca wymiana informacji i koordynacja zespołu'], 'zint_wspolne'))
    b += blk('<div class="pair"><div class="pc"><div>' + subhead('Nauczyciele — w grupie i bieżąca praca', 'blue') + checks(['Stosują dostosowania i strategie na wszystkich zajęciach','Dzielą zadania na etapy, dają dodatkowy czas','Wzmacniają mocne strony i motywację dziecka','Spójnie reagują na sytuacje trudne'], 'zint_naucz', cols=1) + '</div></div><div class="pc"><div>' + subhead('Specjaliści — zajęcia specjalistyczne', 'green') + checks(['Prowadzą zajęcia rewalidacyjne i terapeutyczne','Przekazują zespołowi skuteczne techniki','Wspierają komunikację (AAC) i regulację emocji','Monitorują postępy i modyfikują wsparcie'], 'zint_spec', cols=1) + '</div></div></div>')
    b += ta('Nadrzędny wspólny cel i spójne strategie zespołu na rok szkolny', 'zint_cel', 6, grow=True)
    b += legal(f'<b>Zintegrowane działania.</b> Zintegrowane działania nauczycieli i specjalistów prowadzących zajęcia z dzieckiem, ukierunkowane na poprawę jego funkcjonowania — w tym, w zależności od potrzeb, na komunikowanie się z otoczeniem z użyciem AAC — to obowiązkowy element IPET — § 6 ust. 1 pkt 2 {KS}; realizacja programu przez nauczycieli i specjalistów — § 5.')
    page('IPET · zintegrowane działania', 'IPET · zintegrowane', b)
Z4B = [('Wspólna organizacja dnia i przestrzeni',['Utrzymują stały, przewidywalny plan dnia i te same rutyny','Uprzedzają o zmianach i przejściach („co teraz / co potem")','Zapewniają stałe miejsce dziecka i dostęp do strefy wyciszenia','Ograniczają nadmiar bodźców (hałas, światło, dekoracje)']),
       ('Jednolita komunikacja z dzieckiem',['Stosują krótkie, jednoznaczne polecenia w ten sam sposób','Wspierają wypowiedzi wizualnie (piktogramy, gesty, AAC)','Dają czas na przetworzenie informacji i odpowiedź','Sprawdzają zrozumienie i modelują poprawne wypowiedzi']),
       ('Wspólne strategie uczenia i dostosowań',['Dzielą zadania na etapy — metoda małych kroków, dodatkowy czas','Pracują na konkretach i materiałach poglądowych','Uczą wielozmysłowo; naprzemiennie aktywność i odpoczynek','Stosują te same dostosowania na wszystkich zajęciach']),
       ('Spójne wspieranie zachowań i emocji',['Reagują jednolicie na trudne zachowania (model ABC / PBS)','Wspólny system motywacyjny i te same nagrody (żetony, pochwała)','Uczą i przypominają strategie samoregulacji („STOP – oddech – nazwij")','Wzmacniają mocne strony, zainteresowania i motywację dziecka']),
       ('Samodzielność i włączanie w grupę',['Wdrażają trening samoobsługi i czynności dnia małymi krokami','Wspierają współdziałanie, czekanie na kolej, wspólną zabawę','Stopniowo zmniejszają wsparcie („wygaszanie podpowiedzi")','Włączają dziecko w życie grupy z rówieśnikami']),
       ('Współpraca ze specjalistami i rodzicami',['Na bieżąco wymieniają informacje o postępach i trudnościach','Przenoszą techniki specjalistów do codziennej pracy w grupie','Ujednolicają oddziaływania przedszkole–dom (wspólne zasady)','Wspólnie monitorują cele SMART i modyfikują wsparcie'])]
def s26():
    b = kick('IPET · zintegrowane działania nauczycieli')
    b += blk(sec('4 b', 'Zintegrowane działania nauczycieli — szczegółowo'))
    b += note('Konkretne, spójne działania, które wszyscy nauczyciele pracujący z dzieckiem stosują jednakowo przez cały dzień w przedszkolu — tak, aby dziecko doświadczało jednego, przewidywalnego sposobu wsparcia. Zaznacz te, które obowiązują w danym roku szkolnym.')
    cols = ['purple','blue','green','red','amber','purple']
    for g, (t, items) in enumerate(Z4B):
        b += blk(subhead(t, cols[g])) + blk(checks(items, on=lambda i, g=g: WYP and i in D['zint4b'].get(g, set()), kfmt=lambda i, g=g: f'z4b:{g}:{i}'))
    b += ta('Uzgodnienia dodatkowe zespołu nauczycieli', 'zint4b_uwagi', 3, grow=True)
    b += legal(f'Zintegrowane działania nauczycieli i specjalistów pracujących z dzieckiem to obowiązkowy element IPET — § 6 ust. 1 pkt 2 {KSs}.')
    page('IPET · zintegrowane działania nauczycieli', 'IPET · zintegrowane', b)

def s27():
    b = kick('Zakres i sposób dostosowania programu wychowania przedszkolnego')
    b += blk(sec('5', 'Zakres i sposób dostosowania programu wychowania przedszkolnego — projektowanie uniwersalne'))
    b += blk('<div class="pair"><div class="pc"><div>' + subhead('Metody i formy pracy', 'purple') + checks(['Wydłużony / dodatkowy czas na zadanie','Polecenia krótkie, jednoznaczne, poparte pokazem','Podział zadania na etapy (metoda małych kroków)','Różne formy aktywności i prezentowania osiągnięć dziecka','Indywidualizacja tempa i zakresu','Praca na konkretach i materiałach poglądowych','Stałe, dobre miejsce dziecka'], 'dost_met', cols=1) + '</div></div><div class="pc"><div>' + subhead('Środowisko i technologie', 'blue') + checks(['Text-to-Speech / Speech-to-Text','Systemy wizualne / AAC','Strefa wyciszenia / słuchawki wygłuszające','Ograniczenie dystraktorów','Plany aktywności i piktogramy','Dostosowanie stanowiska pracy'], 'dost_srod', cols=1) + '</div></div></div>')
    b += ta('Inne dostosowania / komentarz zespołu', 'dost_inne', 3)
    b += blk(sec('5 b', 'Dostosowanie warunków organizacji kształcenia (pkt 7)', small=True))
    b += blk(checks(['Dostosowanie sali i kącików (oświetlenie, akustyka, strefy)','Sprzęt specjalistyczny (sprzęt do pozycjonowania, FM, pętla)','Technologie i pomoce wspomagające (AAC, programy, obrazki)','Materiały w wersji dostępnej (powiększenie, kontrast, dotyk, audio)','Dostosowanie rytmu dnia i planu aktywności','Likwidacja barier architektonicznych i sensorycznych'], 'dost5b'))
    b += blk(sec('5 c', 'Przygotowanie do nauki w szkole — gotowość szkolna', small=True))
    b += blk(checks(['Wspomaganie rozwoju i przygotowanie do nauki w szkole','Diagnoza gotowości szkolnej (obserwacja)','Rozpoznanie predyspozycji, uzdolnień i zainteresowań','Rozwijanie umiejętności potrzebnych w szkole (samodzielność, uwaga)','Współpraca z rodzicami i poradnią w planowaniu ścieżki','Przekazanie informacji o dziecku do szkoły (za zgodą rodziców)'], 'dost5c'))
    b += legal(f'<b>Dostosowanie wymagań.</b> IPET określa „zakres i sposób dostosowania programu wychowania przedszkolnego do indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych dziecka, w szczególności przez zastosowanie odpowiednich metod i form pracy z dzieckiem" — § 6 ust. 1 pkt 1 {KSs}; dostosowanie warunków organizacji kształcenia, w tym technologie wspomagające — § 6 ust. 1 pkt 7. W wychowaniu przedszkolnym nie stosuje się ocen ani wymagań edukacyjnych w rozumieniu szkolnym — dostosowuje się realizację podstawy programowej wychowania przedszkolnego ({PPR}, obowiązuje od 1.09.2026).')
    page('Zakres i sposób dostosowania programu wychowania przedszkolnego', 'IPET · dostosowania', b)

REW = [('Trening umiejętności społecznych (TUS)','Psycholog'),('Trening umiejętności emocjonalnych (TUE)','Psycholog / pedagog'),('Trening umiejętności komunikacyjnych (TUK)','Logopeda / pedagog'),('Trening Funkcjonowania Codziennego (TFC)','Oligofrenopedagog'),('Trening orientacji przestrzennej i poruszania','Tyflopedagog'),('Rozwijanie komunikowania się (AAC)','Logopeda'),('Trening rozwoju sensorycznego (SI)','Terapeuta SI'),('Trening rozwoju funkcji poznawczych','Pedagog spec.'),('Gimnastyka korekcyjna','Nauczyciel WF'),('Logopedia rewalidacyjna','Logopeda'),('Terapia ręki','Terapeuta ped.')]
PROGS = [(P1,'Program rewalidacyjny 1 — „Teoria umysłu i empatia" (ToM)',1),(P2,'Program rewalidacyjny 2 — „Zachowanie: model ABC i ocena funkcjonalna (FBA)"',2),(P3,'Program rewalidacyjny 3 — „Kompetencje społeczno-emocjonalne"',3)]
def zaj_table(items, key, progs=False):
    rows = []
    for i, (name, real) in enumerate(items):
        d = D[key].get(i) if WYP else None
        rows.append([f'<td class="nr" style="font-size:9px">{bx(bool(d), f"{key}:{i}")}</td>', f'<td>{name}</td>', cell(d[0] if d else '', '…', f'{key}:{i}:h', 'gray' if not d else ''), cell(d[1] if d else 'Rok szk. 26/27', '', f'{key}:{i}:o', 'gray' if not d else ''), cell(d[2] if d else real, '', f'{key}:{i}:r', 'gray' if not d else '')])
    if progs:
        for j, (sym, name, z) in enumerate(PROGS):
            i = len(items) + j; d = D[key].get(i) if WYP else ('2 × 30 min','Rok szk. 26/27','Nauczyciel-terapeuta')
            rows.append([f'<td class="nr" style="font-size:9px">{bx(True, f"{key}:{i}")}</td>', f'<td>{sym} <b class="p">{name}</b> {zalc(z)}</td>', cell(d[0], '', f'{key}:{i}:h'), cell(d[1], '', f'{key}:{i}:o'), cell(d[2], '', f'{key}:{i}:r')])
    return table(['✓','Rodzaj zajęć','h/tydz.','Okres','Realizator'], rows, widths=['8mm',None,'26mm','26mm','36mm'])
def s28():
    b = blk(sec('6 A', 'Formy wsparcia — zajęcia rewalidacyjne'))
    b += zaj_table(REW, 'rew', progs=True)
    b += legal(f'<b>Zajęcia rewalidacyjne.</b> „W ramach zajęć rewalidacyjnych w programie należy uwzględnić w szczególności rozwijanie umiejętności komunikacyjnych przez: naukę orientacji przestrzennej i poruszania się oraz naukę systemu Braille\'a lub innych alternatywnych metod komunikacji — w przypadku dziecka niewidomego; naukę języka migowego lub innych alternatywnych metod komunikacji (AAC) — w przypadku dziecka z autyzmem, w tym z zespołem Aspergera; zajęcia rozwijające umiejętności społeczne, w tym umiejętności komunikacyjne" — § 6 ust. 2 {KS}. Zajęcia rewalidacyjne jako element programu — § 6 ust. 1 pkt 5.')
    page('Formy wsparcia — zajęcia rewalidacyjne', 'IPET · rewalidacja', b)
PPZ = [('Zajęcia korekcyjno-kompensacyjne','Terapeuta ped.'),('Zajęcia logopedyczne','Logopeda'),('Rozwijające kompetencje emocjonalno-społeczne','Pedagog / Psycholog'),('Zajęcia wspomagające rozwój','Naucz. wych. przedsz.'),('Zajęcia rozwijające uzdolnienia','Nauczyciel / specjalista'),('Zajęcia rozwijające umiejętność uczenia się i gotowość szkolną','Nauczyciel / specjalista'),('Zindywidualizowana ścieżka realizacji przygotowania przedszkolnego','Nauczyciel / specjalista'),('Warsztaty dla rodziców / konsultacje','Specjaliści'),('Terapia pedagogiczna','Terapeuta ped.'),('Socjoterapia','Socjoterapeuta')]
def s29():
    b = blk(sec('6 B', 'Formy pomocy psychologiczno-pedagogicznej'))
    b += zaj_table(PPZ, 'pp')
    b += legal(f'<b>Pomoc psychologiczno-pedagogiczna.</b> „Pomoc psychologiczno-pedagogiczna w przedszkolu, szkole i placówce jest udzielana w trakcie bieżącej pracy z dzieckiem oraz przez zintegrowane działania nauczycieli i specjalistów, a także w formie: zajęć rozwijających uzdolnienia; zajęć rozwijających umiejętności uczenia się; zajęć wspomagających rozwój; zajęć specjalistycznych, korekcyjno-kompensacyjnych, logopedycznych, rozwijających kompetencje emocjonalno-społeczne oraz innych zajęć o charakterze terapeutycznym; zajęć związanych z wyborem kierunku kształcenia i zawodu; zindywidualizowanej ścieżki kształcenia; porad i konsultacji; warsztatów" — § 6 {PP}. Formy, okres i wymiar godzin pomocy pp w IPET — § 6 ust. 1 pkt 3 {KSs}; wymiar ustala dyrektor. Wymiar jednostki: 45 min.')
    page('Formy pomocy psychologiczno-pedagogicznej', 'IPET · pomoc pp', b)

def s30():
    b = blk(sec('7', 'Wsparcie dodatkowe — nauczyciel współorganizujący / asystent'))
    def tn(label, key, hkey, hlabel):
        v = V(key)
        return f'<div class="f" style="display:flex;gap:8px;align-items:center"><span style="flex:1;font-size:9.6px;font-weight:700;color:#2b2540">{label}</span>' + ''.join(f'<span class="c" style="display:inline-flex;gap:5px;align-items:center;font-size:9px;border:1.3px solid {"#E8450A" if v==o else "#cfc2e8"};border-radius:8px;padding:2px 8px;background:#fff">{bx(v==o, key+":"+o)}{o}</span>' for o in ('Tak','Nie')) + f'</div><div class="f"><div class="fl">{hlabel}</div>{fv(hkey, "I / II / III" if hkey=="poziom_wsp" else "", small=True)}</div>'
    b += blk('<div class="fields">' + tn('Nauczyciel współorganizujący kształcenie', 'nw', 'nw_h', 'Wymiar (h/tydz.)') + tn('Pomoc asystenta dziecka', 'asyst', 'poziom_wsp', 'Poziom wsparcia') + '</div>')
    b += blk(sec('8', 'Szczegółowe uzasadnienie wsparcia osobowego (kody ICF)'))
    b += blk('<div class="tools"><b>Kody ICF:</b> e330 (osoby wspierające), d160 (uwaga), d240 (stres), d710/d720 (interakcje), d250 (zachowanie), d570 (bezpieczeństwo), d310/d330 (komunikacja), d820 (edukacja).</div>')
    rows = []
    for i in range(3):
        r = D['icf'][i] if WYP else ('','','','')
        rows.append([cell(r[0], 'np. e330', f'icf:{i}:0', 'gray' if not WYP else ''), cell(r[1], '…', f'icf:{i}:1'), cell(r[2], '…', f'icf:{i}:2'), cell(r[3], '…', f'icf:{i}:3')])
    b += table(['Kod ICF','Bariera bezpieczeństwa','Bariera edukacyjna','Bariera w relacjach'], rows, cls='tb small', widths=['18mm',None,None,None])
    b += blk(sec('9', 'Działania wspierające rodziców i współpracę'))
    b += blk(checks(['Konsultacje i porady ze specjalistami','Instruktaż do pracy i utrwalania w domu','Warsztaty / szkolenia (pedagogizacja rodziców)','Wsparcie w kontakcie z poradnią PPP i instytucjami','Pomoc w rozumieniu orzeczenia i dokumentacji','Wsparcie emocjonalne i informacyjne','Udział w spotkaniach zespołu i współtworzeniu IPET','Ujednolicenie strategii i systemu nagród przedszkole–dom'], 'rodzice'))
    b += legal(f'<b>Współpraca z rodzicami.</b> IPET określa „działania wspierające rodziców dziecka oraz — w zależności od potrzeb — zakres współdziałania z poradniami psychologiczno-pedagogicznymi, placówkami doskonalenia nauczycieli, organizacjami pozarządowymi oraz innymi instytucjami" — § 6 ust. 1 pkt 4 oraz zakres współpracy nauczycieli i specjalistów z rodzicami — pkt 6 {KSs}. Nauczyciel współorganizujący kształcenie dla dziecka z autyzmem — § 7 ust. 2. Rodzice mają prawo uczestniczyć w opracowaniu i modyfikacji programu oraz w ocenach; dyrektor zawiadamia ich pisemnie o terminie spotkania zespołu; otrzymują kopię WOPF i IPET — § 6 rozporządzenia (prawa rodziców).')
    page('Wsparcie osobowe i współpraca z rodzicami', 'IPET · wsparcie', b)
def s31():
    b = blk(sec('10', 'Plan współpracy międzysektorowej'))
    C = [('Szkoła / placówka',['Realizacja IPET i dostosowań na wszystkich zajęciach','Zajęcia rewalidacyjne i pomoc pp','Monitorowanie postępów i dokumentacja','Spójne reagowanie na zachowania trudne','Współpraca nauczycieli i specjalistów']),
         ('Rodzina',['Udział w pracach zespołu i współtworzeniu IPET','Utrwalanie umiejętności w domu','Stały kontakt z nauczycielem grupy / koordynatorem','Ujednolicenie strategii i systemu nagród','Zgody i wymiana informacji']),
         ('Dziecko',['Udział w wyznaczaniu celów („Mój głos")','Korzystanie z dostosowań i strategii','Samoocena postępów','Udział w zajęciach specjalistycznych','Rozwijanie mocnych stron i zainteresowań']),
         ('Podmioty zewnętrzne (PPP, JST, NGO, służba zdrowia)',['Konsultacje z poradnią PPP','Współpraca ze SCWEW / PDN','Wsparcie organizacji pozarządowych (NGO)','Współpraca ze służbą zdrowia','Działania organu prowadzącego (JST)'])]
    b += blk('<div class="col4">' + ''.join(f'<div class="card"><div class="ct">{t}</div>{checks(items, on=lambda i, g=g: WYP and i in D["wsp"].get(g, set()), cols=1, kfmt=lambda i, g=g: f"wsp:{g}:{i}")}</div>' for g, (t, items) in enumerate(C)) + '</div>')
    b += ta('Ustalenia planu współpracy — kto, co, kiedy', 'wsp_ust', 8, grow=True, ph='' )
    b += legal(f'Zakres współdziałania z poradniami psychologiczno-pedagogicznymi, placówkami doskonalenia nauczycieli, organizacjami pozarządowymi oraz innymi instytucjami i podmiotami działającymi na rzecz rodziny, dzieci i młodzieży — § 6 ust. 1 pkt 4 {KSs}. Plan współpracy międzysektorowej — element nowego modelu 2026/27 (✦ NOWE).')
    page('Plan współpracy międzysektorowej', 'IPET · współpraca', b)

def s32():
    b = kick('Część III · zespół, zatwierdzenie i ewaluacja')
    b += blk(sec('1', 'Skład zespołu opracowującego IPET i WOPF'))
    Z = [('Koordynator zespołu','koordynacja WOPFU i IPET, zwoływanie spotkań'),('Nauczyciel prowadzący grupę','obserwacja w grupie, spójność działań'),('Pedagog specjalny','zajęcia rewalidacyjne, dobór dostosowań'),('Psycholog','diagnoza emocjonalno-społeczna, wsparcie'),('Logopeda / neurologopeda','zajęcia logopedyczne, komunikacja / AAC'),('Nauczyciel wychowania przedszkolnego','realizacja podstawy programowej z dostosowaniami'),('Terapeuta SI / rehabilitant','terapia zgodnie ze specjalnością'),('Inna funkcja — wpisz','zakres działań w zespole')]
    rows = []
    for i, (f, zk) in enumerate(Z):
        d = D['zespol'][i] if WYP else None
        rows.append([nr(i+1), f'<td><b class="p">{esc(d[0]) if d else f}</b></td>', cell(d[1] if d else '', '[imię i nazwisko]', f'zespol:{i}:1'), cell(d[2] if d else zk, '', f'zespol:{i}:2', 'gray' if not d else ''), '<td class="gray"><span class="ph">podpis</span></td>'])
    b += table(['Lp.','Funkcja w zespole','Imię i nazwisko','Zakres działań w zespole','Podpis'], rows, cls='tb small', widths=[None,'30mm','34mm',None,'20mm'])
    b += blk(sec('2', 'Otrzymanie kopii i zgoda rodziców / opiekunów prawnych'))
    b += blk('<div class="howto"><p style="font-style:italic">„Potwierdzam udział w spotkaniach zespołu oraz odbiór kopii niniejszego programu IPET wraz z arkuszem WOPF. Zostałam/em poinformowany/a o celach, formach wsparcia oraz prawie do wglądu w dokumentację."</p></div>')
    b += blk(f'<div class="sign2"><div><div class="sl" style="display:flex;align-items:flex-end;font-size:9px;font-weight:700;color:#2b2540;text-transform:none;letter-spacing:0" data-k="miejsce">{esc(V("miejsce"))}</div>Miejscowość i data</div><div><div class="sl"></div>Podpis rodzica / opiekuna</div></div>')
    b += blk(sec('3', 'Okresowa wielospecjalistyczna ocena efektywności (ewaluacja)'))
    b += blk('<div class="fields" style="grid-template-columns:1fr"><div class="f"><div class="fl">Data oceny</div>' + fv('ewal_data', 'dd.mm.rrrr', small=True) + '</div></div>')
    b += blk('<div class="checks c3"><div class="c" style="border-left:3px solid #0D7D5C"><span class="bx" data-k="ewal:0"></span><span>W pełni</span></div><div class="c" style="border-left:3px solid #C47A10"><span class="bx" data-k="ewal:1"></span><span>Częściowo</span></div><div class="c" style="border-left:3px solid #c0392b"><span class="bx" data-k="ewal:2"></span><span>Brak</span></div></div>')
    b += ta('Wnioski i rekomendacje (modyfikacje)', 'ewal_wnioski', 3, grow=True)
    b += legal(f'<b>Okresowa ocena efektywności.</b> „Zespół co najmniej dwa razy w roku szkolnym dokonuje okresowej wielospecjalistycznej oceny poziomu funkcjonowania dziecka, uwzględniając ocenę efektywności programu (…) oraz, w miarę potrzeb, dokonuje modyfikacji programu" — § 6 {KSs} (ocena okresowa); w skład zespołu wchodzą nauczyciele i specjaliści prowadzący zajęcia z dzieckiem — § 6 ust. 3; pracę zespołu koordynuje wychowawca lub inna osoba wyznaczona przez dyrektora.')
    page('Zespół, zgoda rodziców i ewaluacja', 'Część III', b)

ZALS = ['Harmonogram i zakres ewaluacji','Dostosowania z podziałem na obszary podstawy programowej','Szczegółowy plan pracy z rodzicami','Realizacja celów z orzeczenia, KPOF oraz innych','Protokół z posiedzenia zespołu (rekomendacja poziomu wsparcia)','Program zajęć rozwijających kompetencje emocjonalno-społeczne','Program zajęć wspomagających rozwój','Program i tematyka warsztatów oraz konsultacji dla rodziców','Program zajęć logopedycznych','Program rewalidacji — Trening Umiejętności Społecznych (TUS)','Program rewalidacji — Trening Umiejętności Emocjonalnych (TUE)','Program rewalidacji — Trening Umiejętności Komunikacyjnych (TUK)','Program rewalidacji — Trening Funkcjonowania Codziennego (TFC)','Program rewalidacji — Trening orientacji przestrzennej i poruszania się','Program rewalidacji — Rozwijanie komunikowania się (AAC)','Program rewalidacji — Trening rozwoju sensorycznego i motorycznego (SI)','Program rewalidacji — Trening rozwoju funkcji poznawczych','Program rewalidacji — Gimnastyka korekcyjna','Program rewalidacji — Logopedia rewalidacyjna','Program rewalidacji — Terapia ręki']
def s33():
    b = blk(sec('4', 'Załączniki do IPET'))
    rows = []
    for i, z in enumerate(ZALS):
        d = D['zal'].get(i) if WYP else None
        rows.append([nr(i+1), f'<td>{z}</td>', cell(d or '', '…', f'zal:{i}', 'gray' if not d else '')])
    for j, (sym, name, zn) in enumerate(PROGS):
        rows.append([nr(len(ZALS)+j+1), f'<td>{sym} <b class="p">{name}</b> <span class="zal">★ w bazie</span></td>', f'<td>{esc(D["zal_p"][j]) if WYP else f"Zał. {zn} · ……………"}</td>'])
    b += table(['Lp.','Rodzaj załącznika','Numer / data'], rows, cls='tb small', widths=[None,None,'52mm'])
    b += blk(subhead('Programy dołączone z bazy — otwórz', 'purple'))
    b += note('Program dołączony przyciskiem sam wpisuje się do wykazu załączników do IPET — z nazwą, numerem załącznika i odsyłaczem „otwórz". Odznaczenie czyści wiersz.')
    b += blk('<div class="col4" style="grid-template-columns:1fr 1fr 1fr">' + ''.join(f'<div class="card"><div class="ct">★ P{j+1} · {t}</div><div style="font-size:8px;color:#3d384c">{name}</div></div>' for j, (t, (sym, name, zn)) in enumerate(zip(['Teoria umysłu i empatia','Zachowanie: model ABC i FBA','Kompetencje społeczno-emocjonalne'], PROGS))) + '</div>')
    b += legal('Programy są wbudowane w ten plik — otwierają się w oknie na wierzchu, bez żadnych plików obok. „Dołącz" wpisuje program do wykazu załączników do IPET i do zestawienia wybranych zajęć. Puste wiersze — wpisz dodatkowe załączniki dołączone do programu.', label='Uwaga')
    b += blk('<div class="sign2" style="margin-top:2mm"><div><div class="sl"></div>Podpis koordynatora</div><div></div></div>')
    page('Załączniki do IPET', 'Załączniki', b)

def s34():
    b = kick('Część IV · załączniki — dobór programów do wyników WOPF')
    b += h1('Dobór programów do wyników WOPF') + tsub('na podstawie wyników WOPF podłącz pasujące programy z bazy')
    b += note('Mapa łączy sfery funkcjonowania z WOPF z pasującymi rodzajami programów. Na kolejnych stronach zaznacz w katalogach programy odpowiadające rozpoznanym potrzebom dziecka — pozycje oznaczone „★ w bazie" mają dołączony gotowy program (otwierany przyciskiem w wersji interaktywnej).')
    M = [('Sfera 1 — Poznawcze (uczenie się)','Funkcje poznawcze','—'),('Sfera 2 — Emocjonalno-społeczne','Kompetencje emocjonalno-społeczne (TUS) · Teoria umysłu (ToM)','<span class="zal">✦ w bazie</span>'),('Sfera 3 — Motoryczna','Motoryka i terapia ręki · Rozwój motoryki dużej · Integracja sensoryczna (SI)','—'),('Sfera 4 — Mowa i komunikacja','Logopedia / komunikacja (w tym AAC)','—'),('Sfera 5 — Samodzielność','Trening funkcjonowania codziennego (TFC)','—'),('Sfera 6 — Ogólne zadania i zabawa','Funkcje poznawcze · TUS · TFC','—')]
    b += table(['Sfera funkcjonowania (WOPF)','Pasujące rodzaje programów','Program w bazie'], [[f'<td><b class="p">{a}</b></td>', f'<td>{c}</td>', f'<td style="text-align:center">{d}</td>'] for a, c, d in M], widths=['50mm',None,'24mm'])
    b += note('Programy pomocy pp dobiera się analogicznie do rozpoznanych potrzeb (korekcyjno-kompensacyjne, dydaktyczno-wyrównawcze, logopedyczne, emocjonalno-społeczne i inne). Dostosowania — wg indywidualnych potrzeb dziecka.')
    b += blk(subhead('Jak podłączyć programy — 3 kroki', 'purple'))
    b += blk('<div class="steps3">' + ''.join(f'<div class="s3"><span class="sn">{i+1}</span><div class="st">{t}</div><p>{x}</p></div>' for i, (t, x) in enumerate([('Odczytaj wyniki WOPF','Sprawdź, które sfery funkcjonowania są obniżone (poziom wsparcia II / III) — one wyznaczają potrzeby.'),('Dobierz programy z katalogu','Na kolejnych stronach zaznacz pasujące programy rewalidacyjne i pomocy pp oraz dostosowania — wskoczą do tabel zestawienia.'),('Podłącz program z bazy','Pozycje „★ w bazie" (np. TUS, dydaktyczno-wyrównawcze) mają gotowy program — otwierasz go przyciskiem i dołączasz jako załącznik do IPET.')])) + '</div>')
    b += legal(f'Programy rewalidacyjne — § 6 ust. 1 pkt 5 i ust. 2 {KSs}; pomoc psychologiczno-pedagogiczna — § 6 {PPs}. Dobór programów wynika z wielospecjalistycznej oceny poziomu funkcjonowania (WOPF) — § 6 ust. 4 i 9 rozp. o kształceniu specjalnym. Program stanowi załącznik do IPET.')
    page('Dobór programów do wyników WOPF', 'IPET · dobór programów', b)
def s35():
    b = kick('Katalog programów rewalidacyjnych · zaznacz rodzaj')
    b += h1('Katalog programów rewalidacyjnych') + tsub('do wyboru — dziecko z orzeczeniem')
    b += note('Zaznacz rodzaj programu rewalidacyjnego — w wersji interaktywnej wskoczy do tabeli „Programy rewalidacyjne". Program oznaczony „★ w bazie" ma dołączony gotowy dokument.')
    b += blk(f'<div class="tools"><b>Podstawa.</b> § 6 ust. 1 pkt 5 i ust. 2 {KSs}.</div>')
    b += blk(checks(['Kompetencje emocjonalno-społeczne (TUS) <span class="zal">★ w bazie</span>','Teoria umysłu (ToM) <span class="zal">★ w bazie</span>','Motoryka i terapia ręki','Rozwój motoryki dużej','Funkcje poznawcze','Integracja sensoryczna (SI)','Logopedia / komunikacja','Trening funkcjonowania codziennego (TFC)'], 'kat_rew'))
    b += blk(subhead('Programy z bazy dla tego katalogu', 'purple'))
    b += note('Zaznaczenie pozycji „Teoria umysłu (ToM)" lub „Kompetencje emocjonalno-społeczne (TUS)" w katalogu powyżej dołącza program automatycznie — działa też w drugą stronę.')
    b += blk('<div class="col4" style="grid-template-columns:1fr 1fr 1fr">' + ''.join(f'<div class="card"><div class="ct">★ P{j+1} · {t}</div><div style="font-size:8px;color:#3d384c">{name}</div></div>' for j, (t, (sym, name, zn)) in enumerate(zip(['Teoria umysłu i empatia','Zachowanie: model ABC i FBA','Kompetencje społeczno-emocjonalne'], PROGS))) + '</div>')
    b += legal('Programy są wbudowane w ten plik — otwierają się w oknie na wierzchu, bez żadnych plików obok. „Dołącz" wpisuje program do wykazu załączników do IPET i do zestawienia wybranych zajęć.', label='Uwaga')
    page('Katalog programów rewalidacyjnych', 'IPET · rodzaj programu', b)
def s36():
    b = kick('Katalog programów pomocy psychologiczno-pedagogicznej · zaznacz rodzaj')
    b += h1('Katalog programów pomocy PPP') + tsub('do wyboru — także bez orzeczenia')
    b += note('Zaznacz rodzaj programu pomocy psychologiczno-pedagogicznej — wskoczy do tabeli „Programy pomocy PPP".')
    b += blk(f'<div class="tools"><b>Podstawa.</b> § 6 {PP}.</div>')
    b += blk(checks(['Korekcyjno-kompensacyjne','Dydaktyczno-wyrównawcze <span class="zal">★ w bazie</span>','Rozwijające umiejętność uczenia się','Kompetencje emocjonalno-społeczne (PP)','Terapeutyczne / socjoterapeutyczne','Logopedyczne (pomoc PP)','Rozwijające uzdolnienia'], 'kat_pp'))
    page('Katalog programów pomocy PPP', 'IPET · rodzaj programu', b)
KDOST = [('Metody i formy pracy',['Wydłużony / dodatkowy czas pracy','Podział zadania na etapy (metoda małych kroków)','Instrukcje krótkie, jednoznaczne, poparte pokazem','Praca na konkretach i materiałach poglądowych','Indywidualizacja tempa i zakresu','Naprzemienność aktywności i odpoczynku']),
         ('Warunki i organizacja',['Stałe, dobre miejsce dziecka w sali','Zmniejszenie liczebności grupy','Stały, przewidywalny plan dnia','Uprzedzanie o zmianach i przejściach','Strefa wyciszenia / miejsce odpoczynku','Przerwy sensoryczne / ruchowe']),
         ('Środowisko i pomoce',['Wsparcie wizualne (piktogramy, plan „co teraz / co potem")','Komunikacja wspomagająca i alternatywna (AAC — PECS, MAKATON)','Ograniczenie nadmiaru bodźców (hałas, światło, dekoracje)','Materiały w wersji dostępnej (powiększenie, kontrast, audio)','Technologie wspomagające (TTS / STT, aplikacje)','Dostosowanie stanowiska pracy']),
         ('Wsparcie i sposób sprawdzania',['Wsparcie nauczyciela współorganizującego / asystenta','Częste sprawdzanie zrozumienia i informacja zwrotna','Alternatywne formy prezentowania wiedzy (ustnie, obrazkowo)','Pomoc „ręka na rękę" wg potrzeb','System żetonowy i wzmocnienia pozytywne','Dostosowanie wymagań do możliwości dziecka'])]
def s37():
    b = kick('Katalog dostosowań · zaznacz rodzaj')
    b += h1('Katalog dostosowań') + tsub('do wyboru — wg potrzeb dziecka')
    b += note('Zaznacz dostosowania — wskoczą do tabeli „Dostosowania — wybrane".')
    for g, (t, items) in enumerate(KDOST):
        b += blk(subhead(t, ['purple','blue','green','red'][g])) + blk(checks(items, on=lambda i, g=g: WYP and i in D['kat_dost'].get(g, set()), kfmt=lambda i, g=g: f'kdost:{g}:{i}'))
    page('Katalog dostosowań', 'IPET · rodzaj programu', b)
def s38():
    b = kick('Rodzaj programu i dostosowań · zestawienie wybranych')
    b += h1('Rodzaj programu i dostosowań') + tsub('wybór z katalogów — programy wskakują tu po zaznaczeniu')
    b += blk('<div class="tools"><b>Programy z bazy.</b> Pozycje oznaczone „★ program w bazie" (TUS, Dydaktyczno-wyrównawcze) mają dołączony gotowy program — w wersji interaktywnej otwierasz go przyciskiem „Otwórz program (PDF)".</div>')
    b += blk(sec('A', 'Programy rewalidacyjne — wybrane', small=True))
    rows = [[nr(j+1), f'<td>{sym} <b class="p">{name}</b> {zalc(zn)}</td>', f'<td>{esc(D["rew"][11+j][0]) + " tyg. · " + esc(D["rew"][11+j][2]) if WYP else "2 × 30 min tyg. · nauczyciel-terapeuta"}</td>'] for j, (sym, name, zn) in enumerate(PROGS)]
    b += table(['Lp.','Rodzaj programu rewalidacyjnego','Wymiar (h/tydz.) · realizator'], rows, cls='tb small', widths=[None,None,'52mm'])
    b += blk(subhead('Synchronizacja dokumentu — stan bieżący', 'green'))
    b += blk('<div class="legal" style="border-top:none;padding-top:0">Wykorzystane: <b>P1</b> · Teoria umysłu i empatia (Zał. 1) · <b>P2</b> · Zachowanie: model ABC i FBA (Zał. 2) · <b>P3</b> · Kompetencje społeczno-emocjonalne (Zał. 3). Zaznaczone w: katalogu programów rewalidacyjnych (str. 35) · wykazie załączników do IPET (str. 33) · zestawieniu „Programy rewalidacyjne — wybrane" (str. 38) · formach wsparcia — zajęcia rewalidacyjne (str. 28) · celach SMART sfery 2 (str. 15–16) · karcie kontrolnej (str. 40).</div>')
    b += blk(subhead('Przypisanie do programów — legenda dokumentu', 'amber'))
    b += blk('<div class="tools" style="font-size:7px;padding:3px 8px"><b>Dlaczego w tej kolejności — P1:</b> Sekwencja rozwojowa teorii umysłu: najpierw wspólne pole uwagi i emocje (C1, C2), dopiero potem pragnienia, perspektywa i fałszywe przekonanie (C3–C5), a na końcu empatia i zabawa w udawanie (C6). Nie stawia się celu na przekonania, gdy dziecko nie rozpoznaje emocji — cel byłby nieosiągalny.</div>')
    b += blk('<div class="legal" style="border-top:none;padding-top:0"><b>Kolejność pracy w sferze:</b> ① trudności i bariery → ② wynik KPOF i poziom wsparcia → ③ dołączenie programu → ④ wybór celów SMART z programu → ⑤ wpisanie celów i uzupełnienie liczb w nawiasach → ⑥ wymiar godzin, realizator i ewaluacja. Każdy krok wynika z poprzedniego: bez trudności nie ma celu, bez poziomu wsparcia nie ma kryterium, bez programu nie ma sekwencji rozwojowej.</div>')
    leg = [(P1,'Program rewalidacyjny 1 — „Teoria umysłu i empatia" (ToM) — Zał. 1','ToM 19.09.2026: rozpoznawanie emocji 1/2, przyjmowanie perspektywy 0/2 · KPOF VII 1,6 (Poziom III)' if WYP else 'dołączony ręcznie, poza wskazaniem z wyników','C1, C2 (str. 16)' if WYP else 'żaden — zaznacz je na str. 15'),
           (P2,'Program rewalidacyjny 2 — „Zachowanie: model ABC i ocena funkcjonalna (FBA)" — Zał. 2','wypełniony arkusz ABC — ocena pogłębiona (12 zapisów, funkcja: uwaga + komunikat 13/15) · średnia KPOF VII 1,6 — wynik obniżony' if WYP else 'wypełniony arkusz ABC — ocena pogłębiona (7 zaznaczeń) · średnia KPOF 2,50 — wynik obniżony','C1, C2 (str. 16)' if WYP else 'żaden — zaznacz je na str. 15'),
           (P3,'Program rewalidacyjny 3 — „Kompetencje społeczno-emocjonalne" — Zał. 3','KPOF IX 2,5 (Poziom II) · komunikacja w grupie 3/10 · zabawa równoległa' if WYP else 'dołączony ręcznie, poza wskazaniem z wyników','C1, C2 (str. 16)' if WYP else 'żaden — zaznacz je na str. 15')]
    b += blk(''.join(f'<div class="legal" style="border-top:1px solid #eee9f6;padding:3px 0"><span style="display:inline-block;width:14mm">{s}</span><b>{n}</b><br><span style="padding-left:14mm">Podstawa wskazania z oceny: {p}</span><br><span style="padding-left:14mm">Cele przeniesione do sfery 2: {c} &nbsp;·&nbsp; dostępnych w programie: 6 · znacznik na str. 15 · 16 · 28 · 33 · 35 · 38 · 40</span></div>' for s, n, p, c in leg))
    b += blk(sec('B', 'Programy pomocy psychologiczno-pedagogicznej — wybrane', small=True))
    pp = D['progpp'] if WYP else [('Kompetencje emocjonalno-społeczne (PP)','')]
    b += table(['Lp.','Rodzaj programu (pomoc PP)','Wymiar (h/tydz.) · realizator'], [[nr(i+1), f'<td><b class="p">{esc(a)}</b></td>', cell(c, '', f'progpp:{i}')] for i, (a, c) in enumerate(pp)], cls='tb small', widths=[None,None,'52mm'])
    b += blk(sec('C', 'Dostosowania — wybrane', small=True))
    dw = D['dost_wyb'] if WYP else []
    rows = [[nr(i+1), cell(a, '', f'dostw:{i}:0'), cell(c, '', f'dostw:{i}:1')] for i, (a, c) in enumerate(dw)] or [[nr(1), '<td></td>', '<td></td>']]
    b += table(['Lp.','Dostosowanie','Zakres / uwagi'], rows, cls='tb xs', widths=[None,'50%',None])
    page('Rodzaj programu i dostosowań — zestawienie', 'IPET · rodzaj programu', b)

def s39():
    b = blk(sec('RODO', 'Klauzula informacyjna (RODO)'))
    P = [('Administrator danych.','Administratorem danych osobowych jest przedszkole / placówka, do której uczęszcza dziecko, reprezentowana przez dyrektora.'),('Inspektor ochrony danych (IOD).','Kontakt z inspektorem ochrony danych: [adres e-mail / dane kontaktowe IOD].'),('Cel i podstawa prawna.','Dane przetwarzane są w celu realizacji zadań dydaktycznych, wychowawczych i opiekuńczych oraz organizacji kształcenia specjalnego i pomocy psychologiczno-pedagogicznej — na podstawie art. 6 ust. 1 lit. c i e oraz art. 9 ust. 2 lit. g RODO w związku z ustawą — Prawo oświatowe (t.j. Dz.U. 2026 poz. 820) (obowiązek prawny administratora).'),('Kategorie danych.','Dokument zawiera dane szczególnej kategorii (dane o zdrowiu, orzeczenia), o których mowa w art. 9 RODO.'),('Odbiorcy danych.','Dane mogą być udostępniane wyłącznie podmiotom uprawnionym na podstawie przepisów prawa (m.in. poradnia psychologiczno-pedagogiczna, organ prowadzący, organ nadzoru).'),('Okres przechowywania.','Dane przechowywane są przez okres wychowania przedszkolnego dziecka oraz przez czas wymagany przepisami o archiwizacji dokumentacji przebiegu nauczania (t.j. Dz.U. 2024 poz. 50).'),('Prawa osób.','Przysługuje prawo dostępu do danych, ich sprostowania i ograniczenia przetwarzania oraz prawo wniesienia skargi do Prezesa Urzędu Ochrony Danych Osobowych; prawo do usunięcia danych nie przysługuje w zakresie, w jakim przetwarzanie jest niezbędne do wypełnienia obowiązku prawnego (art. 17 ust. 3 lit. b RODO).'),('Bezpieczeństwo.','Dokument zawiera dane wrażliwe i jest przechowywany w sposób uniemożliwiający dostęp osobom nieupoważnionym.')]
    b += blk('<div class="lead rodo" style="border-left-width:4.5px">' + ''.join(f'<p><b>{a}</b> {t}</p>' for a, t in P) + '</div>')
    b += blk('<div style="flex:1"></div>')
    b += note('IPET 2026 · WOPFU (ICF) · Wzór · EduPlaner 2026 · PCTP')
    page('Klauzula informacyjna RODO', 'RODO', b)

def s40():
    b = kick('Rozliczenie wymogów rozporządzenia')
    b += blk(sec('5', 'Karta kontrolna — czy IPET zawiera wszystkie wymagane elementy?'))
    b += note(f'Przed zatwierdzeniem programu zespół sprawdza i odhacza każdy wymóg § 6 {KSs}. Wiersze ze znaczkiem „nowe 26/27" to elementy nowego modelu oceny funkcjonalnej — wykraczają ponad minimum prawne. Pełne brzmienie wymagań — str. 41–42.')
    K = [('§ 6 ust. 1 pkt 1','Zakres i sposób dostosowania programu wychowania przedszkolnego (metody i formy pracy)','Cz. II · sekcja 5 · str. 27'),
         ('§ 6 ust. 1 pkt 2','Zintegrowane działania nauczycieli i specjalistów (w tym AAC, działania rewalidacyjne)','Sekcje 4a–4b · str. 25–26 · sfery 1–6 · str. 13–24'),
         ('§ 6 ust. 1 pkt 3','Formy i okres udzielania pomocy pp oraz wymiar godzin','Sekcja 6B · str. 29'),
         ('§ 6 ust. 1 pkt 4','Działania wspierające rodziców + współdziałanie z poradniami i podmiotami','Sekcje 9–10 · str. 30–31'),
         ('§ 6 ust. 1 pkt 5','Zajęcia rewalidacyjne (resocjalizacyjne, socjoterapeutyczne) i inne zajęcia odpowiednie do potrzeb',f'Sekcja 6A · str. 28 {P1} {P2} {P3}'),
         ('§ 6 ust. 1 pkt 6','Zakres współpracy nauczycieli i specjalistów z rodzicami','Sekcja 9 · str. 30'),
         ('§ 6 ust. 1 pkt 7','Dostosowanie warunków organizacji kształcenia + technologie wspomagające','Sekcja 5b · str. 27'),
         ('§ 6 ust. 1 pkt 8','Wybrane zajęcia realizowane indywidualnie lub w grupie do 5 dzieci (wg potrzeb)','Sekcja 6A · str. 28 (rewalidacja 1:1) · WOPF sekcja XVI'),
         ('§ 6 ust. 2','Autyzm / zespół Aspergera: AAC oraz zajęcia rozwijające umiejętności społeczne i komunikacyjne',f'Sekcja 6A · str. 28 {P1} {P2} {P3} · sfera 4 · str. 19'),
         ('§ 7 ust. 2','Nauczyciel współorganizujący kształcenie (autyzm) — z uzasadnieniem','Sekcje 7–8 · str. 30'),
         ('§ 6 ust. 4','Program po WOPF, z uwzględnieniem diagnozy i wniosków oraz zaleceń z orzeczenia','Str. 6, 9, 12 · WOPF z 25.09.2026'),
         ('§ 6 ust. 5','Termin opracowania: do 30 IX albo 30 dni od złożenia orzeczenia','Str. 1 (data) · Cz. III · str. 32'),
         ('§ 6 (ocena)','WOPF i okresowa ocena efektywności co najmniej 2× w roku szkolnym','Cz. I · str. 4–6 i Cz. III · str. 32'),
         ('§ 6 (rodzice)','Prawa rodziców: udział w pracach, pisemne zawiadomienie o spotkaniach, kopia WOPF i IPET','Cz. III · str. 32')]
    rows = [[f'<td class="pod">{p}</td>', f'<td>{t}</td>', f'<td class="gdzie">{g}</td>', f'<td><div class="bxc">{bx(WYP, f"kk:{i}")}</div></td>'] for i, (p, t, g) in enumerate(K)]
    NEW = [('„Mój głos" — perspektywa i udział dziecka','str. 2–3'),('Ocena funkcjonalna KPOF / ICF i poziomy wsparcia I–III','str. 6, 13–23'),('Projektowanie uniwersalne (UDL) w dostosowaniach','str. 27'),('Plan współpracy międzysektorowej','str. 31')]
    rows += [[f'<td class="pod" style="color:#C47A10">nowy model</td>', f'<td>{t} <span class="nowe">✦ NOWE 26/27</span></td>', f'<td class="gdzie">{g}</td>', f'<td><div class="bxc">{bx(WYP, f"kk:n{i}")}</div></td>'] for i, (t, g) in enumerate(NEW)]
    b += table(['Podstawa','Wymagany element programu','Gdzie w dokumencie','Ujęte'], rows, cls='tb kk', widths=['22mm',None,'46mm','11mm'])
    b += blk(sec('6', 'Podsumowanie weryfikacji — braki i terminy', small=True))
    rows = []
    for i in range(4):
        d = D['braki'][i] if WYP and i < len(D['braki']) else None
        rows.append([nr(i+1), cell(d[0] if d else '', 'czego jeszcze nie ma…', f'braki:{i}:0'), cell(d[1] if d else '', 'dd.mm.rrrr', f'braki:{i}:1'), cell(d[2] if d else '', 'kto', f'braki:{i}:2'), f'<td><span style="display:inline-flex;gap:5px;align-items:center">{bx(bool(d and d[3]), f"braki:{i}:3")} wykonano</span></td>'])
    b += table(['Lp.','Stwierdzony brak / element do uzupełnienia','Termin wykonania','Odpowiedzialny','Status'], rows, cls='tb small', widths=[None,None,'24mm','30mm','22mm'])
    b += blk(f'<div class="sign2"><div><div class="sl" style="display:flex;align-items:flex-end;font-size:9px;font-weight:700;color:#2b2540;text-transform:none;letter-spacing:0" data-k="weryf_data">{esc(V("weryf_data"))}</div>Data weryfikacji</div><div><div class="sl"></div>Podpis koordynatora zespołu</div></div>')
    page('Karta kontrolna zgodności IPET', 'Karta kontrolna', b)

def s41():
    b = kick('Podstawa prawna · co musi zawierać IPET · Strażnik prawa')
    b += h1('Wymagana zawartość IPET') + tsub('§ 6 rozporządzenia MEN z 9.08.2017 r. · t.j. Dz.U. 2020 poz. 1309')
    b += note(f'Źródło publikatorów: skrypt szkolenia EduPlaner 2026 dla przedszkoli, wydanie 2 po audycie podstaw prawnych z 5.09.2026 (część 1 i 6). W dokumencie dziecka cytuj wyłącznie obowiązujący tekst jednolity. Podstawa opracowania programu: art. 127 {PO} oraz {KS}.')
    R = [('§ 6 ust. 1 pkt 1','zakres i sposób dostosowania <i>odpowiednio programu wychowania przedszkolnego</i> oraz wymagań edukacyjnych do indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych dziecka, w szczególności przez zastosowanie odpowiednich metod i form pracy z dzieckiem','sekcja 5 · str. 27 · katalog dostosowań str. 37–38'),
         ('§ 6 ust. 1 pkt 2','zintegrowane działania nauczycieli i specjalistów prowadzących zajęcia z dzieckiem, ukierunkowane na poprawę funkcjonowania dziecka, w tym — w zależności od potrzeb — na komunikowanie się dziecka z otoczeniem z użyciem wspomagających i alternatywnych metod komunikacji (AAC), oraz wzmacnianie jego uczestnictwa w życiu przedszkolnym; w przypadku dziecka niepełnosprawnego — działania o charakterze rewalidacyjnym','sekcje 4a–4b · str. 25–26 · karty sfer 1–6 · str. 13–24'),
         ('§ 6 ust. 1 pkt 3','formy i okres udzielania dziecku pomocy psychologiczno-pedagogicznej oraz wymiar godzin, w którym poszczególne formy pomocy będą realizowane, ustalone przez dyrektora zgodnie z przepisami o pomocy psychologiczno-pedagogicznej (t.j. Dz.U. 2023 poz. 1798)','sekcja 6B · str. 29'),
         ('§ 6 ust. 1 pkt 4','działania wspierające rodziców dziecka oraz — w zależności od potrzeb — zakres współdziałania z poradniami psychologiczno-pedagogicznymi, w tym poradniami specjalistycznymi, placówkami doskonalenia nauczycieli, organizacjami pozarządowymi, innymi instytucjami oraz podmiotami działającymi na rzecz rodziny, dzieci i młodzieży','sekcje 9–10 · str. 30–31'),
         ('§ 6 ust. 1 pkt 5','zajęcia rewalidacyjne, resocjalizacyjne i socjoterapeutyczne oraz inne zajęcia odpowiednie ze względu na indywidualne potrzeby rozwojowe i edukacyjne oraz możliwości psychofizyczne dziecka','sekcja 6A · str. 28 · programy P1–P3 (zał. 1–3)'),
         ('§ 6 ust. 1 pkt 6','zakres współpracy nauczycieli i specjalistów z rodzicami dziecka w realizacji przez przedszkole zadań wymienionych w § 5 (realizacja zaleceń z orzeczenia, warunki, zajęcia specjalistyczne, integracja, przygotowanie do samodzielności)','sekcja 9 · str. 30 · plan współpracy str. 31'),
         ('§ 6 ust. 1 pkt 7','w przypadku dzieci niepełnosprawnych — w zależności od potrzeb — rodzaj i sposób dostosowania warunków organizacji kształcenia do rodzaju niepełnosprawności dziecka, w tym w zakresie wykorzystywania technologii wspomagających to kształcenie','sekcja 5b · str. 27'),
         ('§ 6 ust. 1 pkt 8','w zależności od indywidualnych potrzeb rozwojowych i edukacyjnych oraz możliwości psychofizycznych dziecka wskazanych w orzeczeniu lub wynikających z wielospecjalistycznej oceny — wybrane zajęcia wychowania przedszkolnego, które są realizowane indywidualnie z dzieckiem lub w grupie liczącej do 5 dzieci','sekcja 6A · str. 28 · WOPF sekcja XVI'),
         ('§ 6 ust. 2','w ramach zajęć rewalidacyjnych w programie należy uwzględnić w szczególności rozwijanie umiejętności komunikacyjnych — w przypadku dziecka z autyzmem, w tym z zespołem Aspergera: naukę alternatywnych metod komunikacji (AAC) oraz zajęcia rozwijające umiejętności społeczne, w tym umiejętności komunikacyjne','sekcja 6A · str. 28 · sfery 2 i 4 · str. 15, 19'),
         ('§ 6 ust. 3','program opracowuje zespół, który tworzą nauczyciele i specjaliści prowadzący zajęcia z dzieckiem; pracę zespołu koordynuje wychowawca grupy albo nauczyciel lub specjalista wyznaczony przez dyrektora','Cz. III sekcja 1 · str. 32'),
         ('§ 6 ust. 4','zespół opracowuje program po dokonaniu wielospecjalistycznej oceny poziomu funkcjonowania dziecka, uwzględniając diagnozę i wnioski sformułowane na jej podstawie oraz zalecenia zawarte w orzeczeniu o potrzebie kształcenia specjalnego, we współpracy — w zależności od potrzeb — z poradnią psychologiczno-pedagogiczną','str. 6, 9, 12 · WOPF z 25.09.2026'),
         ('§ 6 ust. 5','program opracowuje się na okres, na jaki zostało wydane orzeczenie, nie dłuższy jednak niż etap edukacyjny — w terminie do dnia 30 września roku szkolnego, w którym dziecko rozpoczyna wychowanie przedszkolne, albo 30 dni od dnia złożenia w przedszkolu orzeczenia','str. 1 · data 30.09.2026 (orzeczenie z 12.05.2026)'),
         ('§ 6 — ocena okresowa','zespół co najmniej dwa razy w roku szkolnym dokonuje okresowej wielospecjalistycznej oceny poziomu funkcjonowania dziecka, uwzględniając ocenę efektywności programu, oraz w miarę potrzeb dokonuje modyfikacji programu (w skrypcie: „bezpieczny zapis: § 6 rozporządzenia bez numeru ustępu")','Cz. III sekcja 3 · str. 32 · terminy 29.01.2027, 18.06.2027'),
         ('§ 6 — prawa rodziców','rodzice dziecka mają prawo uczestniczyć w spotkaniach zespołu, a także w opracowaniu i modyfikacji programu oraz dokonywaniu ocen; dyrektor zawiadamia pisemnie rodziców o terminie każdego spotkania zespołu i możliwości uczestniczenia w tym spotkaniu; rodzice otrzymują kopię wielospecjalistycznej oceny oraz programu','Cz. III sekcja 2 · str. 32 · sekcja 9 · str. 30'),
         ('§ 7 ust. 2','w przedszkolach ogólnodostępnych, w których kształceniem specjalnym są objęte dzieci posiadające orzeczenie wydane ze względu na autyzm, w tym zespół Aspergera, lub niepełnosprawności sprzężone, zatrudnia się dodatkowo nauczycieli posiadających kwalifikacje z zakresu pedagogiki specjalnej w celu współorganizowania kształcenia (albo specjalistów / pomoc nauczyciela)','sekcje 7–8 · str. 30')]
    b += blk(''.join(f'<div class="req"><div class="rt"><span class="pod">{p}</span><span>{t.split(" ")[0][0].upper()+t.split(" ")[0][1:]} {" ".join(t.split(" ")[1:])}</span><span class="ok">✓ ujęte: {g}</span></div></div>'.replace('<span>'+t.split(" ")[0][0].upper()+t.split(" ")[0][1:]+' '+" ".join(t.split(" ")[1:])+'</span>', f'<span class="rq" style="font-weight:400">{t}</span>') for p, t, g in R))
    page('Podstawa prawna — wymagana zawartość IPET', 'Podstawa prawna · § 6', b)

def s42():
    b = kick('Strażnik prawa · weryfikacja publikatorów użytych w druku IPET')
    b += h1('Strażnik prawa — IPET') + tsub('weryfikacja wg skryptu szkolenia · wyd. 2 po audycie z 5.09.2026')
    rows = [('Kształcenie specjalne (WOPF, IPET, zajęcia rewalidacyjne, nauczyciel współorganizujący)','rozp. MEN z 9.08.2017 r.','t.j. Dz.U. 2020 poz. 1309 — § 5, § 6 ust. 1 pkt 1–8, ust. 2–5, ocena okresowa i prawa rodziców, § 7 ust. 2','✓ zgodne'),
            ('Pomoc psychologiczno-pedagogiczna (formy, okres, wymiar godzin — pkt 3)','rozp. MEN z 9.08.2017 r.','t.j. Dz.U. 2023 poz. 1798 — § 6 (formy pomocy), § 20 (rozpoznawanie potrzeb, ocena efektywności)','✓ zgodne'),
            ('Prawo oświatowe (art. 127 — kształcenie specjalne; art. 47 ust. 1 pkt 5)','ustawa z 14.12.2016 r.','t.j. Dz.U. 2026 poz. 820','✓ zgodne'),
            ('Podstawa programowa wychowania przedszkolnego (dostosowanie realizacji, 9 obszarów osiągnięć)','rozp. ME z 11.03.2026 r.','Dz.U. 2026 poz. 378 — obowiązuje od 1.09.2026 (zmiana Dz.U. 2026 poz. 958 nie dotyczy zał. nr 1)','✓ zgodne'),
            ('Orzeczenia i opinie zespołów orzekających (opinia o funkcjonowaniu dziecka — 10 dni)','rozp. ME z 2.03.2026 r.','Dz.U. 2026 poz. 428 — od 14.04.2026; uchyliło rozp. MEN z 7.09.2017 r. (t.j. 2023 poz. 2061 — nie cytować)','✓ zgodne'),
            ('Dokumentacja przebiegu nauczania (dziennik zajęć rewalidacyjnych, archiwizacja)','rozp. MEN z 25.08.2017 r.','t.j. Dz.U. 2024 poz. 50','✓ zgodne'),
            ('RODO — art. 5 ust. 1 lit. c, art. 6 ust. 1 lit. c i e, art. 9 ust. 2 lit. g, art. 17 ust. 3 lit. b','rozp. (UE) 2016/679','zgodnie ze skryptem (część 3)','✓ zgodne'),
            ('Cele SMART','—','skrypt (część 6): nazwa SMART nie pada w rozporządzeniu; wymagana jest ocena efektywności, a cel z kryterium jest najprostszym narzędziem tej oceny — „nazwa dowolna, mierzalność konieczna"','✓ zgodne'),
            ('Numeracja ustępów § 6 dot. oceny okresowej i praw rodziców','—','skrypt (uwaga redakcyjna): sprawdź w ogłoszonym tekście jednolitym; w druku użyto zapisu „§ 6 rozporządzenia" bez numeru ustępu','⚠ zapis ostrożny'),
            ('Wzór IPET (PDF, wersja z 2026) cytował: Dz.U. 2017 poz. 1578 · 2017 poz. 1591 · 2024 poz. 737 · 2017 poz. 356','—','w tym druku zastąpiono tekstami jednolitymi / aktami z 2026 r. wg skryptu (zob. wiersze wyżej)','✓ poprawiono')]
    b += table(['Zakres / akt prawny','Akt','Publikator i zakres wg skryptu (wyd. 2 po audycie)','Status'], [[f'<td><b class="p">{a}</b></td>', f'<td>{x}</td>', f'<td>{c}</td>', f'<td style="white-space:nowrap;color:{"#0D7D5C" if s.startswith("✓") else "#C47A10"};font-weight:800">{s}</td>'] for a, x, c, s in rows], cls='tb small', widths=['52mm','30mm',None,'20mm'])
    b += blk(subhead('Terminy i zasady z rozporządzenia — do sprawdzenia przy zatwierdzaniu', 'amber'))
    b += blk('<div class="lead" style="border-left-color:#C47A10"><p><b>Termin IPET:</b> do 30 września (dziecko rozpoczynające wychowanie przedszkolne z orzeczeniem) albo 30 dni od złożenia orzeczenia w przedszkolu. <b>Ocena okresowa:</b> co najmniej dwa razy w roku szkolnym (tu: 29.01.2027 i 18.06.2027). <b>Rodzice:</b> pisemne zawiadomienie o każdym spotkaniu zespołu, prawo udziału, kopia WOPF i IPET. <b>Autyzm:</b> obowiązkowo AAC i zajęcia rozwijające umiejętności społeczne (§ 6 ust. 2) oraz nauczyciel współorganizujący (§ 7 ust. 2). <b>Wymiar godzin</b> pomocy pp i rewalidacji ustala dyrektor w arkuszu organizacji. <b>Pełna nazwa</b> w dokumencie do teczki: „wielospecjalistyczna ocena poziomu funkcjonowania" i „indywidualny program edukacyjno-terapeutyczny" — skróty tylko w pracy zespołu.</p></div>')
    b += legal('Weryfikację wykonano wyłącznie wobec skryptu szkolenia dostarczonego przez autorkę (wydanie 2 po audycie podstaw prawnych z 5.09.2026). Karta Nauczyciela i ustawa z 28.07.2023 r. (Dz.U. 2023 poz. 1606) nie są cytowane w tym druku. Przed użyciem druku w kolejnym roku szkolnym sprawdź aktualność publikatorów w ISAP.', label='Zastrzeżenie')
    page('Strażnik prawa — IPET', 'Strażnik prawa', b)

# ============================================================ składanie
def zloz():
    s01(); s02(); s03(); s04(); s05(); s06(); s07(); s08(); s09(); s10(); s11(); s12()
    for n in (1,2,3,4,5,6): s_smart(n); s_real(n)
    s25(); s26(); s27(); s28(); s29(); s30(); s31(); s32(); s33(); s34(); s35(); s36(); s37(); s38(); s39(); s40(); s41(); s42()
    N = len(PAGES); out = []
    for i, (sub, foot, body) in enumerate(PAGES, 1):
        meta = (f'<div class="pmeta"><div class="m"><span class="ml">Dotyczy dziecka</span><span class="mv" data-k="meta:0">{esc(V("imie")) or "&nbsp;"}</span></div>'
                f'<div class="m sm"><span class="ml">Grupa</span><span class="mv" data-k="meta:1">{esc(V("grupa")) or "&nbsp;"}</span></div>'
                f'<div class="m sm"><span class="ml">Data</span><span class="mv" data-k="meta:2">{esc(V("data")) or "&nbsp;"}</span><span class="mr">r.</span></div></div>')
        head = (f'<div class="phead"><div class="logo">PCTP</div><div class="bl"><div class="t1">EduPlaner 2026</div><div class="t2">{esc(sub)}</div></div>'
                f'<div class="br"><span class="kodchip">IPET · 2026</span><div class="t3">dokument IPET · 2026</div></div></div>')
        foot_h = f'<div class="pfoot"><span class="l">EduPlaner 2026 · PCTP</span><span class="r"><b>Strona {i} z {N}</b> · {esc(foot)}</span></div>'
        out.append(f'<div class="page" id="str{i}"><div class="frame"></div><div class="inner">{head}{meta}<div class="pbody">{body}</div>{foot_h}</div></div>')
    title = 'IPET przedszkole z orzeczeniem 2026' + (' — Zofia Lewandowska' if WYP else ' — druk') + ' — EduPlaner 2026 — PCTP'
    doc = ('<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><title>' + esc(title) + '</title><style>' + FONT_CSS + '\n' + BASE_CSS + CSS_IPET +
           '</style></head><body>' + ''.join(out) + '</body></html>')
    return doc, N

if __name__ == '__main__':
    doc, N = zloz()
    if WYP:
        os.makedirs(os.path.join(KAT, 'out/ipet'), exist_ok=True)
        p = os.path.join(KAT, 'out/ipet/IPET_2026_Zofia_Lewandowska_wypelniony.html')
    else:
        p = os.path.join(KAT, 'public/ipet.html')
    open(p, 'w', encoding='utf-8').write(doc)
    print('zapisano', p, '| stron:', N, '| rozmiar:', len(doc))
