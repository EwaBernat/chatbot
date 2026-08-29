# -*- coding: utf-8 -*-
"""Generator broszury: Sala, ktora uczy kazde dziecko."""
import base64, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_CSS = open(os.path.join(HERE, "base_css.txt"), encoding="utf-8").read()

BRAND = "SALA, KTÓRA UCZY KAŻDE DZIECKO · przestrzeń i dostępność w nowej podstawie"

_cache = {}
def img(name):
    """Zwraca data-URI zdjecia."""
    if name in _cache:
        return _cache[name]
    for p in (os.path.join(HERE, "img", name + ".jpg"), os.path.join(HERE, "new", name + ".jpg")):
        if os.path.exists(p):
            b = base64.b64encode(open(p, "rb").read()).decode()
            _cache[name] = "data:image/jpeg;base64," + b
            return _cache[name]
    raise SystemExit("brak zdjecia: " + name)

# ---------- ikony ----------
IC = {
"autyzm":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M7.5 8.5C5 8.5 3.2 10.2 3.2 12s1.8 3.5 4.3 3.5c2.8 0 3.7-3 5-3.5 1.3.5 2.2 3.5 5 3.5 2.5 0 4.3-1.7 4.3-3.5s-1.8-3.5-4.3-3.5c-2.8 0-3.7 3-5 3.5-1.3-.5-2.2-3.5-5-3.5z"/></svg>',
"ruch":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9.5" cy="15.5" r="4.7"/><path d="M9.5 15.5V5.5M9.5 5.5h3.2M9.5 10.5h5.5M15 10.5l3 6h2.5"/><circle cx="9.5" cy="5" r="1.4" fill="currentColor" stroke="none"/></svg>',
"intelekt":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M9 4h4v2.2a1.8 1.8 0 0 0 3.4 1 1.8 1.8 0 0 1 3.4 1c0 1.6-1.5 2-1.5 3.6a1.8 1.8 0 0 0 3.4 1V17h-4.2a1.8 1.8 0 0 0-1-3.4 1.8 1.8 0 0 1-1-3.4c-1.6 0-2 1.5-3.6 1.5A1.8 1.8 0 0 1 9 10V4z"/></svg>',
"adhd":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9.2"/><path d="M13 6.5 8.5 13h3l-1 4.5 5-6.7h-3.2z" fill="currentColor" stroke="none"/></svg>',
"sluch":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M8 9a4 4 0 1 1 8 0c0 2.4-2.6 3-2.6 5.4a1.9 1.9 0 0 1-3.8.2"/><path d="M11 19.5a1.6 1.6 0 0 0 3 0"/><path d="M18.5 5.5a7 7 0 0 1 0 9"/></svg>',
"wzrok":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M2.5 12S6 5.8 12 5.8 21.5 12 21.5 12 18 18.2 12 18.2 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3.1"/></svg>',
"sensor":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/><circle cx="12" cy="12" r="3.4"/></svg>',
"mowa":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M4 5.5h11.5a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2H9l-5 3.5v-3.5a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2z"/><path d="M7 9h6M7 11.6h4"/></svg>',
"zdrowie":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M20.4 7.4a4.6 4.6 0 0 0-8.4-2.5 4.6 4.6 0 0 0-8.4 2.5c0 5 8.4 11 8.4 11s8.4-6 8.4-11z"/><path d="M6.5 11.6h3l1.4-2.4 1.8 4 1.3-1.6h3.2"/></svg>',
"jezyk":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M3.2 12h17.6M12 3.1c2.4 2.5 3.6 5.6 3.6 8.9S14.4 18.4 12 20.9c-2.4-2.5-3.6-5.6-3.6-8.9S9.6 5.6 12 3.1z"/></svg>',
"lupa":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.3"/><path d="M15.2 15.2 20.5 20.5"/></svg>',
"tarcza":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 3 4.8 5.9v5.4c0 4.3 3 8.2 7.2 9.5 4.2-1.3 7.2-5.2 7.2-9.5V5.9L12 3z"/><path d="m8.8 12 2.3 2.3 4.1-4.6"/></svg>',
"ludzie":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="8.6" cy="8.4" r="3.1"/><circle cx="16.6" cy="9.4" r="2.4"/><path d="M3.2 19.4c0-3 2.4-5.2 5.4-5.2s5.4 2.2 5.4 5.2"/><path d="M15.4 14.6c2.7 0 5.4 1.5 5.4 4.8"/></svg>',
}

EXTRA_CSS = """
/* ====== czesc dostepnosciowa ====== */
.lvl-strip{display:flex;gap:3mm;margin:2mm 0 4mm;}
.lvl-strip .ls{flex:1;border-radius:4mm;padding:3mm 3.5mm;color:#fff;}
.lvl-strip .ls .lsn{font-family:'Quicksand';font-weight:700;font-size:8pt;letter-spacing:.08em;opacity:.9;}
.lvl-strip .ls .lst{font-family:'Quicksand';font-weight:700;font-size:10.4pt;line-height:1.15;margin-top:.8mm;}
.lvl-strip .ls .lsd{font-family:'Nunito';font-weight:600;font-size:7.6pt;line-height:1.3;margin-top:1.4mm;opacity:.95;}
.bg-l1{background:var(--mint-deep);} .bg-l2{background:var(--pink-deep);} .bg-l3{background:var(--purple-deep);}
.sf-l1{background:var(--mint-soft);} .sf-l2{background:var(--pink-soft);} .sf-l3{background:var(--purple-soft);}
.tx-l1{color:var(--mint-deep);} .tx-l2{color:var(--pink-deep);} .tx-l3{color:var(--purple-deep);}

.pyramid{display:flex;flex-direction:column;align-items:center;gap:2mm;margin:2mm 0 3mm;}
.pyr-row{border-radius:3mm;color:#fff;display:flex;align-items:center;justify-content:space-between;
  padding:2.6mm 4mm;font-family:'Nunito';font-weight:700;font-size:8.6pt;}
.pyr-row span.pw{font-family:'Quicksand';font-weight:700;font-size:9.4pt;opacity:.92;}

.big-num{font-family:'Quicksand';font-weight:700;font-size:30pt;line-height:1;color:#fff;
  width:22mm;height:22mm;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;}

.info-box{border-radius:4.5mm;padding:3.8mm 4.6mm;margin-bottom:3.2mm;}
.info-box .ib-title{font-family:'Quicksand';font-weight:700;font-size:10.6pt;margin:0 0 2mm;}
.info-box p, .info-box li{font-family:'Nunito';font-size:9.5pt;line-height:1.42;margin:0;}
.box-mint{background:var(--mint-soft);} .box-mint .ib-title{color:var(--mint-deep);}
.box-pink{background:var(--pink-soft);} .box-pink .ib-title{color:var(--pink-deep);}
.box-purple{background:var(--purple-soft);} .box-purple .ib-title{color:var(--purple-deep);}
.info-box ul{list-style:none;margin:0;padding:0;}
.info-box ul li{position:relative;padding-left:5mm;margin-bottom:1.7mm;}
.info-box ul li::before{content:'';position:absolute;left:0;top:1.9mm;width:2.4mm;height:2.4mm;border-radius:50%;background:currentColor;opacity:.55;}

.warn-box{border-left:2.4pt solid var(--pink-deep);background:var(--pink-soft);border-radius:0 4mm 4mm 0;
  padding:3.4mm 4.4mm;font-family:'Nunito';font-size:9.2pt;line-height:1.4;}
.warn-box strong{color:var(--pink-deep);font-weight:800;}

.three-lvl{display:grid;grid-template-columns:1fr 1fr 1fr;gap:2.6mm;margin:1mm 0 2.5mm;}
.tl-col{border-radius:4mm;padding:3.2mm 3.4mm;display:flex;flex-direction:column;gap:1.8mm;}
.tl-col .tlh{display:flex;align-items:center;gap:1.8mm;}
.tl-col .tlb{width:6.4mm;height:6.4mm;border-radius:50%;color:#fff;font-family:'Quicksand';font-weight:700;
  font-size:8pt;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.tl-col .tlt{font-family:'Quicksand';font-weight:700;font-size:9pt;line-height:1.12;}
.tl-col ul{list-style:none;margin:0;padding:0;}
.tl-col ul li{font-family:'Nunito';font-size:8.4pt;line-height:1.34;margin-bottom:1.7mm;padding-left:3.8mm;position:relative;}
.tl-col ul li::before{content:'▸';position:absolute;left:0;top:-0.2mm;font-size:7pt;opacity:.7;}

.def-head{display:flex;align-items:center;gap:4mm;margin-bottom:3mm;}
.def-head .dh-ic{width:15mm;height:15mm;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;flex-shrink:0;}
.def-head .dh-ic svg{width:8.4mm;height:8.4mm;}
.def-head h2{margin:0;font-family:'Quicksand';font-weight:700;font-size:20.5pt;color:var(--ink);line-height:1.1;}
.def-head .dh-sub{font-family:'Nunito';font-weight:700;font-size:9.2pt;color:var(--ink-soft);margin-top:1.2mm;}

.eq-row{display:flex;gap:4mm;align-items:stretch;margin-bottom:2.6mm;}
.eq-photo{border-radius:4.5mm;overflow:hidden;border:1.4pt solid var(--purple-deep);
  box-shadow:0 3px 10px rgba(107,75,161,.15);}
.eq-photo img{width:100%;height:100%;object-fit:cover;display:block;}

.wide-photo{border-radius:5mm;overflow:hidden;border:1.6pt solid var(--purple-deep);
  box-shadow:0 3px 12px rgba(107,75,161,.16);position:relative;}
.wide-photo img{width:100%;height:100%;object-fit:cover;display:block;}
.wide-photo .wcap{position:absolute;left:0;right:0;bottom:0;color:#fff;font-family:'Nunito';font-weight:700;
  font-size:7.8pt;padding:8mm 4mm 2.6mm;background:linear-gradient(0deg,rgba(57,43,77,.85),rgba(57,43,77,0));}

table.grid{width:100%;border-collapse:collapse;font-family:'Nunito';font-size:9pt;}
table.grid th{background:var(--purple-deep);color:#fff;text-align:left;padding:2.8mm 3.2mm;font-weight:700;font-size:8.6pt;}
table.grid td{padding:2.9mm 3.2mm;border-bottom:.7pt solid var(--line);vertical-align:top;line-height:1.34;}
table.grid tr:nth-child(even) td{background:var(--purple-soft);}
table.grid td.k{font-weight:800;color:var(--purple-deep);}
table.grid .c1{background:var(--mint-soft);} table.grid .c2{background:var(--pink-soft);}

table.sheet{width:100%;border-collapse:collapse;font-family:'Nunito';font-size:9pt;}
table.sheet th{background:var(--purple-deep);color:#fff;text-align:left;padding:2.8mm 3.2mm;font-weight:700;font-size:8.6pt;}
table.sheet td{padding:3.5mm 3.2mm;border:.7pt solid var(--line);vertical-align:middle;line-height:1.34;}
table.sheet td.q{width:60%;}
table.sheet td.tick{text-align:center;color:var(--ink-soft);font-size:11pt;letter-spacing:1.6mm;}
table.sheet td.note{background:#FCFAFF;}
.sheet-legend{font-family:'Nunito';font-size:8.4pt;color:var(--ink-soft);margin:2.6mm 0 3mm;display:flex;gap:6mm;flex-wrap:wrap;}
.sheet-legend b{color:var(--purple-deep);}

.field-line{border-bottom:.9pt dashed var(--line);height:6.5mm;}
.mini-head{font-family:'Quicksand';font-weight:700;font-size:10pt;color:var(--purple-deep);margin:0 0 1.8mm;}
.flow-steps{display:flex;flex-direction:column;gap:3mm;}
.flow-step{display:flex;gap:3mm;align-items:flex-start;}
.flow-step .fs-n{width:7.4mm;height:7.4mm;border-radius:50%;background:var(--purple-deep);color:#fff;flex-shrink:0;
  font-family:'Quicksand';font-weight:700;font-size:8.4pt;display:flex;align-items:center;justify-content:center;}
.flow-step .fs-t{font-family:'Nunito';font-size:9.5pt;line-height:1.4;}
.flow-step .fs-t strong{color:var(--purple-deep);font-weight:800;}
.legal-list{font-family:'Nunito';font-size:8.2pt;line-height:1.42;}
.legal-list li{margin-bottom:1.6mm;}
.legal-list strong{color:var(--purple-deep);}
"""

# ---------- szkielet strony ----------
def footer(n, total):
    return ('<div class="footer"><span class="fbrand">%s</span>'
            '<span class="pagenum">%02d / %d</span></div>' % (BRAND, n, total))

def page(n, total, inner, cls="", panel_style="padding-top:5mm;", panel_cls="panel"):
    return ('<section class="pdf-page %s" id="page-%d">\n'
            '  <div class="bleed-label">SALA, KTÓRA UCZY KAŻDE DZIECKO — strona robocza %02d — '
            'nie drukować tego paska</div>\n'
            '  <div class="%s" style="%s">%s%s</div>\n</section>\n'
            % (cls, n, n, panel_cls, panel_style, inner, footer(n, total)))

def deco(tone):
    return ('<div class="deco deco-%s deco-tr"></div><div class="deco deco-%s deco-bl"></div>' % (tone, tone))

def head(kicker, tone, title, subtitle=None, title_size=None):
    ts = ' style="font-size:%s;"' % title_size if title_size else ""
    s = ('%s<span class="kicker t-%s">%s</span>'
         '<h2 class="page-title"%s>%s</h2><span class="underline u-%s"></span>'
         % (deco(tone), tone, kicker, ts, title, tone))
    if subtitle:
        s += '<p class="page-subtitle">%s</p>' % subtitle
    return s

def photo(name, alt, caption=None, style="", cls="photo-filled"):
    cap = '<div class="photo-caption">%s</div>' % caption if caption else ""
    return ('<div class="%s" style="%s"><img src="%s" alt="%s">%s</div>'
            % (cls, style, img(name), alt, cap))

def wide_photo(name, alt, caption, style="flex:1;min-height:0;"):
    return ('<div class="wide-photo" style="%s"><img src="%s" alt="%s">'
            '<div class="wcap">%s</div></div>' % (style, img(name), alt, caption))

def lvl_strip(compact=False):
    d = [("POZIOM 1", "Projektowanie uniwersalne", "Dla wszystkich dzieci w grupie — bez diagnozy i bez wniosku.", "bg-l1"),
         ("POZIOM 2", "Dostosowania ukierunkowane", "Dla dzieci z rozpoznaną trudnością — pomoc psychologiczno-pedagogiczna.", "bg-l2"),
         ("POZIOM 3", "Wsparcie zindywidualizowane", "Dla dzieci z orzeczeniem o potrzebie kształcenia specjalnego — IPET.", "bg-l3")]
    out = '<div class="lvl-strip">'
    for n, t, o, bg in d:
        out += ('<div class="ls %s"><div class="lsn">%s</div><div class="lst">%s</div>%s</div>'
                % (bg, n, t, "" if compact else '<div class="lsd">%s</div>' % o))
    return out + "</div>"

def three_lvl(l1, l2, l3, titles=("Poziom 1 — dla wszystkich", "Poziom 2 — ukierunkowany", "Poziom 3 — indywidualny")):
    cols = [(l1, "sf-l1", "bg-l1", "tx-l1", "1", titles[0]),
            (l2, "sf-l2", "bg-l2", "tx-l2", "2", titles[1]),
            (l3, "sf-l3", "bg-l3", "tx-l3", "3", titles[2])]
    out = '<div class="three-lvl">'
    for items, soft, bg, tx, num, title in cols:
        li = "".join("<li>%s</li>" % i for i in items)
        out += ('<div class="tl-col %s"><div class="tlh"><div class="tlb %s">%s</div>'
                '<div class="tlt %s">%s</div></div><ul>%s</ul></div>' % (soft, bg, num, tx, title, li))
    return out + "</div>"

def info_box(title, items, tone="mint", text=None):
    body = "<p>%s</p>" % text if text else "<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in items)
    return ('<div class="info-box box-%s"><p class="ib-title">%s</p>%s</div>' % (tone, title, body))

def warn(text):
    return '<div class="warn-box"><strong>Częsty błąd:</strong> %s</div>' % text

def check_box(title, items):
    return ('<div class="check-box"><p class="cb-title">%s</p><ul class="check">%s</ul></div>'
            % (title, "".join("<li>%s</li>" % i for i in items)))

def nice_list(items, tone="purple"):
    return '<ul class="nice c-%s">%s</ul>' % (tone, "".join("<li>%s</li>" % i for i in items))

def adapt_mini(rows, title="Dostosowania w tej strefie"):
    tones = {"mint": "var(--mint-deep)", "pink": "var(--pink-deep)", "purple": "var(--purple-deep)"}
    out = '<div class="adapt-mini"><p class="am-title">%s</p><div class="adapt-mini-grid">' % title
    for ic, tone, name, desc in rows:
        out += ('<div class="adapt-mini-row"><div class="am-icon" style="background:%s;color:#fff;">%s</div>'
                '<div class="am-text"><strong>%s</strong>%s</div></div>' % (tones[tone], IC[ic], name, desc))
    return out + "</div></div>"

def zone_page(num, tone, title, intro, has_list, adapts, photo_name, photo_alt, photo_cap, extra_kicker=""):
    return ('%s<div class="zone-badge"><div class="zone-num z-%s">%02d</div><div>'
            '<span class="kicker t-%s" style="margin:0 0 1.5mm;">STREFA STAŁA</span>%s'
            '<h2 class="page-title" style="margin-top:1mm;font-size:20pt;">%s</h2></div></div>'
            '<div class="two-col"><div class="col-text" style="flex:1.45;">'
            '<div class="body-text"><p>%s</p></div>%s%s</div>'
            '<div class="col-photo" style="flex:1;align-items:flex-start;">%s</div></div>'
            % (deco(tone), tone, num, tone, extra_kicker, title, intro,
               check_box("Co warto mieć w tej strefie", has_list),
               adapt_mini(adapts), photo(photo_name, photo_alt, photo_cap)))

PAGES = []
def P(toc, color, fn):
    PAGES.append((toc, color, fn))

# ---------- 01 OKŁADKA ----------
def p_cover(n, total):
    return ('<span class="eyebrow">PRZEWODNIK DLA NAUCZYCIELI, SPECJALISTÓW I DYREKTORÓW PRZEDSZKOLI</span>'
            '<h1>Sala, która uczy<br>każde dziecko</h1>'
            '<p class="cov-sub">Jak urządzić salę przedszkolną zgodnie z nową podstawą programową '
            'i jednocześnie zapewnić dostępność dzieciom z różnymi deficytami — pięć stref, '
            'trzy poziomy wsparcia, projektowanie uniwersalne i gotowe arkusze monitoringu sali.</p>'
            '<div class="cov-photo cov-photo-has-img" style="height:142mm;"><div class="photo-filled cov-photo-filled" style="height:142mm;">'
            '<img src="%s" alt="Sala przedszkolna ze strefami aktywności"></div></div>'
            '<div class="cov-footer"><span class="pill">Wydanie 2026 · podstawa programowa + dostępność</span>'
            '<span class="pill">Format A4 · %d stron · gotowe do druku</span></div>' % (img("01"), total))

# ---------- SPIS TREŚCI ----------
def toc_page(part, n, total):
    items = [(i + 4, t, c) for i, (t, c, _) in enumerate(PAGES) if t]
    half = (len(items) + 1) // 2
    chunk = items[:half] if part == 1 else items[half:]
    rows = ""
    for num, title, color in chunk:
        rows += ('<div class="toc-item"><span class="tdot" style="background:var(--%s-deep)"></span>'
                 '<span class="ttitle">%s</span><span class="tnum">%02d</span></div>' % (color, title, num))
    extra = ""
    if part == 2:
        extra = ('<div class="two-col" style="flex:none;margin-top:5mm;gap:5mm;">'
                 '<div class="col-text">' +
                 info_box("Jak korzystać z przewodnika", [
                     "<b>Strony 04–19</b> — organizacja sali według nowej podstawy programowej",
                     "<b>Strony 20–29</b> — trzy poziomy wsparcia i projektowanie uniwersalne",
                     "<b>Strony 30–40</b> — dostosowania według konkretnych deficytów",
                     "<b>Strony 41–48</b> — monitoring sali, arkusze i plan wdrożenia"], "purple") +
                 '</div><div class="col-text">' +
                 info_box("Przewodnik w liczbach", [
                     "<b>5</b> stref stałych opisanych krok po kroku",
                     "<b>3</b> poziomy wsparcia z konkretnymi rozwiązaniami",
                     "<b>10</b> grup potrzeb i deficytów z gotowymi zapisami do dokumentacji",
                     "<b>4</b> narzędzia do skopiowania: 2 arkusze, karta obserwacji, plan naprawczy"], "mint") +
                 '</div></div>')
    if part == 1:
        extra = ('<div class="two-col" style="flex:none;margin-top:5mm;gap:5mm;"><div class="col-text">' +
                 info_box("Dla kogo jest ten przewodnik", [
                     "Nauczycieli wychowania przedszkolnego urządzających salę od nowa",
                     "Pedagogów specjalnych i nauczycieli wspomagających",
                     "Dyrektorów planujących zakupy i nadzór pedagogiczny",
                     "Zespołów opracowujących WOPFU i IPET"], "mint") +
                 '</div><div class="col-text">' +
                 info_box("Czego tu nie znajdziesz", [
                     "Gotowej listy zakupów bez odniesienia do potrzeb dzieci",
                     "Jednego „poprawnego” wyglądu sali dla wszystkich placówek",
                     "Zaleceń medycznych ani diagnostycznych",
                     "Rozwiązań wymagających remontu przed 1 września"], "pink") +
                 '</div></div>'
                 '<div class="legal-note" style="margin-top:4mm;">Przewodnik łączy dwie perspektywy: '
                 '<b>organizację sali według nowej podstawy programowej</b> oraz '
                 '<b>dostępność i dostosowania dla dzieci ze zróżnicowanymi potrzebami</b>. '
                 'Materiał ma charakter praktyczny i poglądowy — nie zastępuje lektury pełnych tekstów '
                 'aktów prawnych ani indywidualnych zaleceń poradni psychologiczno-pedagogicznej.</div>')
    return ('%s<span class="kicker t-purple">SPIS TREŚCI %d / 2</span>'
            '<h2 class="page-title">Co znajdziesz w tym przewodniku</h2>'
            '<span class="underline u-purple"></span><div class="toc-list">%s</div>%s'
            % (deco("purple"), part, rows, extra))

# ---------- CZĘŚĆ I ----------
P("Wstęp — przestrzeń jako trzeci nauczyciel", "purple", lambda n, t:
  head("WPROWADZENIE", "purple", "Przestrzeń jako trzeci nauczyciel",
       "Zanim dziecko usłyszy instrukcję, już „czyta” salę, w której się znalazło.") +
  '<div class="two-col"><div class="col-text body-text">'
  '<p>Sposób, w jaki urządzona jest sala, decyduje o tym, co dziecko może zrobić samodzielnie — '
  'bez pytania dorosłego o zgodę. Nowa podstawa programowa wychowania przedszkolnego stawia tę '
  'zależność wprost: sprawczość i samodzielność dziecka to nie dodatek do zajęć, tylko efekt '
  'codziennej organizacji przestrzeni.</p>'
  '<p>Ta sama przestrzeń decyduje też o tym, <strong>które dziecko może dołączyć do zabawy, '
  'a które zostaje z boku</strong>. Dlatego w tym przewodniku organizacja stref i dostępność '
  'to nie dwa osobne tematy, tylko jedna decyzja projektowa.</p>' +
  info_box("Przewodnik prowadzi Cię przez cztery kroki", [
      "Pięć stref stałych wymaganych w nowej podstawie programowej",
      "Trzy poziomy wsparcia — od projektowania uniwersalnego po IPET",
      "Dostosowania sali według konkretnych deficytów",
      "Monitoring sali — arkusze do wypełnienia i plan naprawczy"], "purple") +
  '</div><div class="col-photo">' +
  photo("02", "Sala ze strefami: bloki, strefa ciszy, twórczość",
        "Sala ze strefami: bloki, strefa ciszy, twórczość") + '</div></div>')

P("Nowa podstawa programowa w pigułce", "mint", lambda n, t:
  head("PODSTAWA PRAWNA · 1", "mint", "Nowe przepisy w pigułce") +
  '<div class="two-col" style="display:block;"><div class="col-text body-text">'
  '<p><strong>Rozporządzenie Ministra Edukacji z 11 marca 2026 r.</strong> w sprawie podstawy '
  'programowej wychowania przedszkolnego (Dz.U. 2026 poz. 378) wchodzi w życie '
  '<strong>1 września 2026 r.</strong> i obowiązuje wszystkie przedszkola, oddziały przedszkolne '
  'w szkołach podstawowych oraz inne formy wychowania przedszkolnego.</p>'
  '<p>Najważniejsza zmiana dla organizacji sali: dotychczasowe „stałe i czasowe kąciki '
  'zainteresowań” zastępuje pojęcie <strong>„stałych i czasowych stref”</strong> — szersze, '
  'bo obejmujące także przestrzeń poza budynkiem przedszkola.</p>' +
  check_box("Co realnie się zmienia", [
      "Nowe nazewnictwo: „strefa” zamiast „kącika”",
      "Zupełnie nowa, piąta strefa — umiejętności odpoczywania",
      "Strefy mogą działać poza salą i być wspólne dla kilku grup",
      "Nacisk na funkcję strefy, nie na jednolity wygląd",
      "Elastyczność — dopasowanie do metrażu, nie odwrotnie",
      "Codzienny pobyt na świeżym powietrzu jako element planu dnia"]) +
  '</div></div>' +
  '<div class="legal-note">Materiał ma charakter poglądowy i pomocniczy. Podstawą prawną pozostaje '
  'pełny tekst rozporządzenia oraz jego oficjalne komentarze publikowane przez Ministerstwo Edukacji '
  'i Ośrodek Rozwoju Edukacji.</div>')

P("Dostępność — druga podstawa prawna sali", "purple", lambda n, t:
  head("PODSTAWA PRAWNA · 2", "purple", "Dostępność — to też obowiązek, nie dobra wola",
       "Nowa podstawa programowa mówi, <b>co</b> ma być w sali. Przepisy o dostępności mówią, "
       "<b>dla kogo</b> to ma działać.") +
  '<div class="two-col"><div class="col-text">'
  '<div class="body-text"><p>Przedszkole jest podmiotem publicznym, a to znaczy, że ma obowiązek '
  'zapewnić dostępność <strong>architektoniczną, informacyjno-komunikacyjną i cyfrową</strong>. '
  'Dla sali przedszkolnej oznacza to trzy bardzo konkretne pytania: czy dziecko tam dojedzie, '
  'czy zrozumie, gdzie jest co, i czy dostanie informację w formie, którą odbiera.</p></div>' +
  '<ul class="legal-list nice c-purple">'
  '<li><strong>Ustawa z 19 lipca 2019 r.</strong> o zapewnianiu dostępności osobom ze szczególnymi '
  'potrzebami — minimalne wymagania w trzech obszarach dostępności.</li>'
  '<li><strong>Konwencja ONZ o prawach osób niepełnosprawnych</strong> (Dz.U. 2012 poz. 1169) — '
  'definicja projektowania uniwersalnego i prawo do edukacji włączającej.</li>'
  '<li><strong>Rozporządzenie MEN z 9 sierpnia 2017 r.</strong> o kształceniu specjalnym — '
  'WOPFU i IPET dla dzieci z orzeczeniem.</li>'
  '<li><strong>Rozporządzenie MEN z 9 sierpnia 2017 r.</strong> o pomocy psychologiczno-pedagogicznej — '
  'wsparcie bez orzeczenia, na podstawie rozpoznania nauczyciela.</li>'
  '<li><strong>Przepisy techniczno-budowlane i BHP</strong> — szerokości przejść, progi, '
  'oznaczenia, bezpieczne wyposażenie.</li></ul>' +
  '</div><div class="col-photo">' +
  photo("13", "Dziecko samodzielnie korzystające ze strefy przyrody",
        "Dostępność zaczyna się od układu mebli, nie od sprzętu") + '</div></div>' +
  '<div class="legal-note">Dostępności nie „załatwia się” jednym zakupem. To sposób planowania sali: '
  'najpierw rozwiązania działające dla wszystkich, potem dostosowania dla konkretnych dzieci.</div>')

P("Filozofia — dziecko jako aktywny twórca", "pink", lambda n, t:
  head("FILOZOFIA", "pink", "Dziecko jako aktywny twórca, nie odbiorca") +
  '<div class="two-col"><div class="col-text body-text">'
  '<p>Nowa podstawa programowa zakłada, że dziecko jest aktywnym uczestnikiem własnego procesu '
  'uczenia się — nie odbiorcą gotowych ćwiczeń. To mniej kart pracy, a więcej uczenia się przez '
  'doświadczenie i samodzielne działanie.</p>'
  '<p>Dobrze zaprojektowana sala wspiera cztery filary tej filozofii:</p>' +
  nice_list(["<strong>Samodzielność</strong> — dziecko sięga po materiały bez pomocy dorosłego",
             "<strong>Sprawczość</strong> — dziecko samo wybiera aktywność",
             "<strong>Doświadczenie</strong> — uczenie się przez działanie, nie instrukcję",
             "<strong>Dobrostan</strong> — prawo do odpoczynku jest tak samo ważne jak prawo do zabawy"], "pink") +
  '<div class="warn-box" style="margin-top:1mm;"><strong>Uwaga na pułapkę:</strong> sprawczość, '
  'która działa tylko dla dzieci sprawnych ruchowo, mówiących i bez trudności poznawczych, '
  'nie jest sprawczością — jest przywilejem części grupy.</div>' +
  '</div><div class="col-photo">' +
  photo("03", "Różnorodne aktywności wybierane samodzielnie",
        "Różnorodne aktywności wybierane samodzielnie") + '</div></div>')

P("5 pytań, zanim przestawisz pierwszy mebel", "purple", lambda n, t:
  head("ZANIM ZACZNIESZ", "purple", "5 pytań, zanim przestawisz pierwszy mebel",
       "Krótka lista kontrolna, która pomaga spojrzeć na salę oczami dziecka, nie kamery.") +
  '<div style="display:flex;gap:7mm;flex:1;min-height:0;"><div style="flex:1.05;" class="body-text">' +
  nice_list([
      "<strong>Czy materiały są na wysokości dziecka?</strong> — jeśli trzeba prosić dorosłego o podanie, strefa nie działa samodzielnie.",
      "<strong>Czy każde dziecko dojedzie i dosięgnie?</strong> — sprawdź przejścia i dostęp z pozycji siedzącej.",
      "<strong>Czy dziecko wie, co gdzie jest, bez czytania?</strong> — oznaczenia obrazkowe zamiast napisów.",
      "<strong>Czy strefa wspiera działanie, czy tylko dobrze wygląda na zdjęciu?</strong> — estetyka jest dodatkiem, nie celem.",
      "<strong>Czy wszystko musi być w jednej sali?</strong> — część stref może być wspólna dla kilku grup albo poza salą.",
  ], "purple") +
  '</div><div style="flex:.95;align-self:flex-start;border-radius:5mm;overflow:hidden;'
  'border:1.6pt solid var(--purple-deep);box-shadow:0 3px 12px rgba(107,75,161,.15);">'
  '<img src="%s" alt="Sala przedszkolna ze wszystkimi strefami" style="width:100%%;height:auto;display:block;">'
  '</div></div>' % img("04"))

# ---------- PIĘĆ STREF ----------
P("Strefa 1 — czytelnictwa", "purple", lambda n, t: zone_page(
    1, "purple", "Strefa czytelnictwa",
    "Strefa czytania powinna być przytulnym, spokojnym miejscem, dostępnym dla wszystkich dzieci. "
    "Warto uwzględnić książki w różnych formatach: z dużą czcionką, obrazkowe, dotykowe, "
    "a także opowiadania w języku obcym nowożytnym.",
    ["Niski regał — książki w zasięgu ręki dziecka",
     "Miękki dywan, poduchy i oparcie dla pleców",
     "Książki obrazkowe, dotykowe, z dużym drukiem",
     "Oznaczenie półek obrazkiem, nie napisem"],
    [("autyzm", "mint", "Spektrum autyzmu", " — stały układ półek, mniej bodźców na okładkach"),
     ("ruch", "pink", "Niepełnosprawność ruchowa", " — regał dostępny z pozycji siedzącej"),
     ("intelekt", "purple", "Niepełnosprawność intelektualna", " — proste historie obrazkowe, mało tekstu"),
     ("adhd", "pink", "ADHD", " — ograniczona liczba książek wyłożonych naraz"),
     ("wzrok", "purple", "Słaby wzrok", " — duży druk, kontrast, lampka punktowa"),
     ("sluch", "mint", "Niedosłuch", " — miejsce z dala od źródeł hałasu")],
    "05", "Cichy kącik czytelniczy w strefie czytelnictwa", "Cichy kącik czytelniczy"))

P("Strefa 2 — budowania i konstruowania", "mint", lambda n, t: zone_page(
    2, "mint", "Strefa budowania i konstruowania",
    "Ta strefa zapewnia dostęp do klocków, materiałów i narzędzi do majsterkowania oraz bezpieczne "
    "miejsce pracy. Zasady bezpiecznego korzystania z narzędzi nauczyciel ustala razem z dziećmi.",
    ["Klocki różnej wielkości, wagi i faktury",
     "Podstawowe, bezpieczne narzędzia do majsterkowania",
     "Stabilny blat i praca również na podłodze",
     "Półka na prace w toku — z oznaczeniem „nie sprzątać”"],
    [("autyzm", "mint", "Spektrum autyzmu", " — stałe miejsce każdego rodzaju klocków"),
     ("ruch", "pink", "Niepełnosprawność ruchowa", " — duże klocki, mata antypoślizgowa"),
     ("intelekt", "purple", "Niepełnosprawność intelektualna", " — instrukcje obrazkowe krok po kroku"),
     ("adhd", "pink", "ADHD", " — mniejsza liczba elementów w jednym pojemniku"),
     ("sensor", "purple", "Nadwrażliwość słuchowa", " — wykładzina lub mata wyciszająca hałas klocków"),
     ("wzrok", "mint", "Słaby wzrok", " — klocki kontrastowe, brzegi blatu oznaczone")],
    "06", "Strefa budowania i konstruowania w praktyce", "Budowanie na podłodze i przy blacie"))

P("Strefa 3 — działań artystycznych", "pink", lambda n, t: zone_page(
    3, "pink", "Strefa działań artystycznych",
    "Strefa artystyczna rozwija wrażliwość estetyczną w plastyce, muzyce, tańcu, śpiewie i teatrze. "
    "Kluczowy jest łatwy, samodzielny dostęp do materiałów, a nie gotowy zestaw wydawany przez nauczyciela.",
    ["Blat lub sztaluga — także na wysokości wózka",
     "Fartuszki i materiały plastyczne w zasięgu dziecka",
     "Przybory z nakładkami i grubym uchwytem",
     "Miejsce ekspozycji prac na wysokości oczu dziecka"],
    [("autyzm", "mint", "Spektrum autyzmu", " — stały porządek materiałów, uprzedzenie o zmianie"),
     ("ruch", "pink", "Niepełnosprawność ruchowa", " — blat z podjazdem, mata antypoślizgowa"),
     ("intelekt", "purple", "Niepełnosprawność intelektualna", " — zadania jednoetapowe, wzór obok"),
     ("adhd", "pink", "ADHD", " — jeden materiał na stole naraz"),
     ("sensor", "purple", "Nadwrażliwość dotykowa", " — alternatywa dla farb: pędzel, gąbka, folia"),
     ("mowa", "mint", "Trudności w mowie", " — wybór materiału przez wskazanie obrazka")],
    "07", "Wspólna praca w strefie działań artystycznych", "Wspólna praca przy jednym blacie"))

P("Strefa 4 — umiejętności odpoczywania", "purple", lambda n, t: zone_page(
    4, "purple", "Strefa umiejętności odpoczywania",
    "To zupełnie nowy element — wcześniejsza podstawa go nie wyodrębniała. Strefa wyciszenia jest "
    "dostępna dla wszystkich dzieci. <strong>To nie kara w kącie</strong> — to prawo dziecka do odpoczynku "
    "i najważniejsze narzędzie samoregulacji w sali.",
    ["Miękkie siedziska, pufy lub materac",
     "Kołdra lub przytulanka obciążeniowa",
     "Zabawki sensoryczne — gniotki, panele dotykowe",
     "Słuchawki wygłuszające dostępne bez pytania"],
    [("autyzm", "mint", "Spektrum autyzmu", " — stały wystrój, wejście bez negocjacji"),
     ("ruch", "pink", "Niepełnosprawność ruchowa", " — wejście bez progu, podparcie pleców"),
     ("intelekt", "purple", "Niepełnosprawność intelektualna", " — piktogram „tu mogę odpocząć”"),
     ("adhd", "pink", "ADHD", " — wejście bez pytania o zgodę, krótkie sesje"),
     ("sensor", "purple", "Zaburzenia SI", " — regulowane światło, brak bodźców dźwiękowych"),
     ("zdrowie", "mint", "Choroby przewlekłe", " — miejsce na krótki odpoczynek po wysiłku")],
    "08", "Kącik wyciszenia z panelem dotykowym", "Kącik wyciszenia z panelem dotykowym",
    '<span class="kicker t-pink" style="margin-left:3mm;">NOWOŚĆ W PODSTAWIE 2026</span>'))

P("Strefa 5 — odkrywania świata nauki i przyrody", "mint", lambda n, t: zone_page(
    5, "mint", "Strefa odkrywania świata nauki i przyrody",
    "Strefa pozwala odkrywać zjawiska zachodzące w przyrodzie, prowadzić samodzielne obserwacje "
    "i proste eksperymenty. Każde dziecko powinno mieć możliwość korzystania z niej bez zbędnych "
    "ograniczeń czasowych.",
    ["Lupy, szkiełka, proste przyrządy obserwacyjne",
     "Hodowla roślin lub mini-ogródek",
     "Tablica obserwacji pogody — obrazkowa",
     "Materiały naturalne o różnej fakturze"],
    [("autyzm", "mint", "Spektrum autyzmu", " — przewidywalny przebieg eksperymentu"),
     ("ruch", "pink", "Niepełnosprawność ruchowa", " — taca wysuwana, pojemniki lekkie"),
     ("intelekt", "purple", "Niepełnosprawność intelektualna", " — jedna obserwacja, jeden krok"),
     ("adhd", "pink", "ADHD", " — krótkie doświadczenia z szybkim efektem"),
     ("wzrok", "purple", "Słaby wzrok", " — lupa powiększająca, doświadczenia dotykowe"),
     ("jezyk", "mint", "Bariera językowa", " — nazwy przedmiotów z obrazkiem")],
    "09", "Obserwacja próbek przyrodniczych przez lupę", "Obserwacja przez lupę"))

P("Wszystkie strefy razem — mapa sali", "mint", lambda n, t:
  head("SPOJRZENIE Z GÓRY", "mint", "Wszystkie strefy razem",
       "Pięć stref stałych i strefy czasowe w jednym widoku — jak elementy łączą się w spójną przestrzeń.") +
  '<div style="flex:1;min-height:0;border-radius:5mm;overflow:hidden;border:1.6pt solid var(--mint-deep);'
  'box-shadow:0 3px 12px rgba(46,142,116,.15);display:flex;align-items:flex-start;justify-content:center;'
  'background:var(--mint-soft);"><img src="%s" alt="Mapa mentalna wszystkich stref sali przedszkolnej" '
  'style="width:100%%;height:auto;display:block;"></div>' % img("10"))

P("Strefy stałe i czasowe — sala, która oddycha", "pink", lambda n, t:
  head("STREFY W RUCHU", "pink", "Strefy stałe i czasowe — sala, która oddycha") +
  '<div class="two-col"><div class="col-text body-text">'
  '<p>Nie wszystkie pięć stref musi istnieć jednocześnie, przez cały dzień. Część może mieć charakter '
  '<strong>czasowy</strong> — powstawać na potrzeby działania i być rozkładana po jego zakończeniu.</p>'
  '<p>Strefy mogą być też <strong>wspólne dla kilku grup</strong> albo zorganizowane poza salą. '
  'Wielkość i liczbę stref dopasowujemy do metrażu i liczby dzieci — nie odwrotnie.</p>' +
  nice_list(["Strefa czasowa może pojawić się na środku sali tylko na czas zajęć",
             "Kilka grup może dzielić jedną strefę konstrukcyjną",
             "Strefa czytelnicza może działać w holu lub bibliotece"], "pink") +
  '<div class="warn-box"><strong>Częsty błąd:</strong> codzienne przestawianie mebli. '
  'Dla dziecka ze spektrum autyzmu, z niepełnosprawnością intelektualną lub słabowidzącego '
  'zmiana układu sali to utrata mapy — jeśli zmieniasz, uprzedź i pokaż nowy układ.</div>'
  '</div><div class="col-photo">' +
  photo("11", "Strefa czytelnicza zorganizowana w holu przedszkola",
        "Strefa czytelnicza w holu przedszkola") + '</div></div>')

P("Ogród, taras, spacer — też są salą", "mint", lambda n, t:
  head("NA ZEWNĄTRZ", "mint", "Ogród, taras, spacer — też są salą") +
  '<div class="two-col"><div class="col-text body-text">'
  '<p>Nowa podstawa wprost wymaga <strong>codziennych zajęć na świeżym powietrzu</strong> oraz '
  'co najmniej <strong>raz w tygodniu pobytu poza budynkiem dłużej niż godzinę</strong>. '
  'To stały element planu dnia, nie okazjonalny spacer.</p>'
  '<p>Nawet niewielki teren zielony można wykorzystać jako naturalne przedłużenie strefy przyrodniczej — '
  'do obserwacji i swobodnej zabawy ruchowej.</p>' +
  check_box("Co warto zaplanować", [
      "Kącik ogrodowy do obserwacji przyrody",
      "Utwardzone dojście dla wózka i dziecka niepewnego ruchowo",
      "Miejsce zacienione — dla dzieci z chorobami skóry i przewlekłymi",
      "Cotygodniowy, dłuższy pobyt poza budynkiem"]) +
  '</div><div class="col-photo">' +
  photo("12", "Kącik ogrodowy — obserwacja i badanie przyrody",
        "Kącik ogrodowy — obserwacja przyrody") + '</div></div>')

P("Bezpieczeństwo w strefach aktywności", "pink", lambda n, t:
  head("BEZPIECZEŃSTWO", "pink", "Wolność działania w bezpiecznych granicach") +
  '<div class="two-col"><div class="col-text body-text">'
  '<p>Samodzielność nie oznacza braku zasad. Szczególnie w strefie konstrukcyjnej i artystycznej '
  'ważne są jasne reguły korzystania z narzędzi — najlepiej ustalone <strong>razem z dziećmi</strong>, '
  'nie tylko im narzucone.</p>' +
  check_box("Krótka checklista bezpieczeństwa", [
      "Zasady narzędzi ustalone wspólnie z dziećmi",
      "Regularny przegląd stanu wyposażenia",
      "Oznaczenia „praca w toku” zamiast pospiesznego sprzątania",
      "Drobne elementy poza zasięgiem najmłodszych grup",
      "Meble stabilne i przymocowane do ściany",
      "Wolna droga ewakuacyjna również przy zmianie układu stref"]) +
  '</div><div class="col-photo">' +
  photo("14", "Praca z narzędziami według wspólnie ustalonych zasad",
        "Praca z narzędziami według wspólnych zasad") + '</div></div>')

P("Higiena cyfrowa — ekrany z umiarem", "mint", lambda n, t:
  head("EKRANY Z UMIAREM", "mint", "Miejsce dla technologii — z umiarem") +
  '<div class="two-col"><div class="col-text body-text">'
  '<p>Nowa podstawa programowa ogranicza kontakt dzieci z narzędziami ekranowymi niemal wyłącznie '
  'do sytuacji prowadzonych przez nauczyciela, w celach dydaktycznych. Priorytetem pozostaje higiena '
  'cyfrowa wspierająca prawidłowy rozwój dziecka.</p>'
  '<p>Wyjątkiem są <strong>technologie wspomagające</strong>: komunikator AAC, powiększalnik, system FM '
  'dla dziecka z aparatem słuchowym. To nie są „ekrany dla rozrywki” — to proteza komunikacji '
  'lub zmysłu i dziecko musi mieć do nich dostęp stały, nie regulowany limitem czasu.</p>' +
  info_box("Zasada rozdzielenia", [], "purple",
           "Sprzęt dydaktyczny trzymamy poza strefami swobodnej zabawy, w miejscu kontrolowanym "
           "przez nauczyciela. Sprzęt wspomagający dziecko trzyma przy sobie — zawsze.") +
  '</div><div class="col-photo">' +
  photo("15", "Praca z tabletem prowadzona przez nauczycielkę",
        "Praca z tabletem prowadzona przez nauczycielkę") + '</div></div>')

P("Rytm dnia i celebrowanie posiłków", "pink", lambda n, t:
  head("RYTM DNIA", "pink", "Spokojny czas przy stole") +
  '<div class="two-col"><div class="col-text body-text">'
  '<p>W planie dnia warto uwzględnić realny czas na spokojne spożywanie posiłków, połączone z nauką '
  'samodzielnego posługiwania się łyżką, widelcem i nożem. To integralna część rytmu dnia, '
  'a nie przerwa między zajęciami.</p>' +
  nice_list(["Stoły dostosowane do wzrostu dzieci i do wózka",
             "Sztućce z pogrubioną rączką, talerz z podwyższonym brzegiem, mata antypoślizgowa",
             "Spokojna, wyciszona atmosfera — mniej hałasu, mniej odmów jedzenia",
             "Miejsce na samodzielne nakrycie i sprzątnięcie po sobie"], "pink") +
  '<div class="warn-box"><strong>Pamiętaj:</strong> wybiórczość pokarmowa u dziecka ze spektrum '
  'autyzmu lub z zaburzeniami sensorycznymi to nie kaprys. Zapewnij dziecku możliwość jedzenia '
  'w spokojniejszym miejscu i nie wymuszaj próbowania.</div>'
  '</div><div class="col-photo">' +
  photo("16", "Wspólny, spokojny posiłek grupy", "Wspólny, spokojny posiłek grupy") + '</div></div>')

# ---------- CZĘŚĆ II — TRZY POZIOMY ----------
P("Trzy poziomy wsparcia — mapa systemu", "purple", lambda n, t:
  head("SYSTEM DOSTOSOWAŃ", "purple", "Trzy poziomy wsparcia w jednej sali",
       "Dostosowania nie zaczynają się od orzeczenia. Zaczynają się od sposobu, "
       "w jaki urządzasz salę dla całej grupy.") +
  lvl_strip() +
  '<div class="pyramid" style="width:100%;">'
  '<div class="pyr-row bg-l1" style="width:100%;"><span>POZIOM 1 · Projektowanie uniwersalne — cała grupa</span>'
  '<span class="pw">≈ 100% dzieci</span></div>'
  '<div class="pyr-row bg-l2" style="width:72%;"><span>POZIOM 2 · Dostosowania ukierunkowane</span>'
  '<span class="pw">≈ 15–20%</span></div>'
  '<div class="pyr-row bg-l3" style="width:44%;"><span>POZIOM 3 · Wsparcie indywidualne</span>'
  '<span class="pw">≈ 3–5%</span></div></div>' +
  '<div class="two-col" style="margin-top:1mm;"><div class="col-text body-text">'
  '<p>Piramida działa tylko w jedną stronę: <strong>im lepiej zaprojektowany poziom 1, tym mniej '
  'dzieci potrzebuje poziomu 2 i 3</strong>. Sala, w której wszystko jest podpisane wyłącznie tekstem, '
  'sztucznie tworzy potrzebę wsparcia u dzieci, które przy piktogramach poradziłyby sobie same.</p>' +
  info_box("Trzy pytania, które porządkują decyzję", [
      "Czy to rozwiązanie pomoże <b>wszystkim</b> dzieciom? → poziom 1",
      "Czy pomoże <b>grupie dzieci</b> z podobną trudnością? → poziom 2",
      "Czy jest potrzebne <b>temu jednemu dziecku</b> i zapisane w IPET? → poziom 3"], "purple") +
  '</div><div style="flex:.9;">' +
  wide_photo("n08", "Sala zaprojektowana uniwersalnie — wszystkie dzieci razem",
             "Poziom 1: jedna przestrzeń, w której mieszczą się wszyscy", "height:60mm;") +
  '</div></div>')

P("Poziom 1 — projektowanie uniwersalne", "mint", lambda n, t:
  head("POZIOM 1", "mint", "Projektowanie uniwersalne — na czym polega",
       "„Projektowanie produktów, środowiska, programów i usług w taki sposób, by były użyteczne "
       "dla wszystkich, w możliwie największym stopniu, bez potrzeby adaptacji" +
       " lub specjalistycznego projektowania” — Konwencja ONZ, art. 2.") +
  '<div class="body-text"><p>W przedszkolu oznacza to jedno: <strong>salę projektujesz od razu tak, '
  'żeby działała dla dziecka na wózku, dziecka, które nie mówi, i dziecka, które nie czyta</strong> — '
  'zanim takie dziecko trafi do grupy. Dostosowanie robione „po fakcie” zawsze wyróżnia dziecko; '
  'projektowanie uniwersalne nie wyróżnia nikogo.</p></div>' +
  '<table class="grid" style="margin-top:1mm;"><thead><tr><th style="width:34%">7 zasad projektowania uniwersalnego</th>'
  '<th>Jak to wygląda w sali przedszkolnej</th></tr></thead><tbody>' +
  "".join('<tr><td class="k">%s</td><td>%s</td></tr>' % (a, b) for a, b in [
      ("1. Równość w użyciu", "Ta sama półka i ten sam stół działa dla dziecka chodzącego i jeżdżącego na wózku"),
      ("2. Elastyczność", "Można pracować przy stole, na podłodze i na stojąco — dziecko wybiera pozycję"),
      ("3. Prostota i intuicyjność", "Widać, gdzie co jest, bez tłumaczenia — pojemnik ma zdjęcie zawartości"),
      ("4. Postrzegalna informacja", "Ta sama treść w trzech kanałach: obrazek, słowo, gest lub dźwięk"),
      ("5. Tolerancja na błąd", "Rozlana woda i przewrócona wieża to element zabawy, a nie awaria"),
      ("6. Niski wysiłek fizyczny", "Lekkie pojemniki, uchwyty zamiast gałek, brak ciężkich drzwi"),
      ("7. Przestrzeń dostępu", "Przejścia min. 90 cm, miejsce do obrotu wózkiem w każdej strefie"),
  ]) + '</tbody></table>' +
  info_box("Test trzech pytań — czy Twoja sala jest zaprojektowana uniwersalnie", [
      "Czy dziecko na wózku dojedzie do <b>każdej</b> z pięciu stref i sięgnie po materiały?",
      "Czy dziecko, które nie mówi, może pokazać, czego chce, w każdej strefie?",
      "Czy dziecko, które nie czyta, wie bez pytania dorosłego, co jest w którym pojemniku?"], "mint") +
  '<div class="legal-note" style="margin-top:auto;">Projektowanie uniwersalne nie zwalnia '
  'z dostosowań indywidualnych. Ono je <b>zmniejsza</b> — i sprawia, że dziecko z orzeczeniem '
  'potrzebuje ich mniej, żeby uczestniczyć na równi z grupą.</div>')

P("Poziom 1 w praktyce — jak to zorganizować", "mint", lambda n, t:
  head("POZIOM 1 · PRAKTYKA", "mint", "Jak zorganizować projektowanie uniwersalne w sali",
       "Dwanaście rozwiązań, które nie wymagają orzeczenia, wniosku ani zgody organu prowadzącego.") +
  '<div class="two-col"><div class="col-text">' +
  info_box("Przestrzeń i meble", [
      "Główne ciągi komunikacyjne min. 90 cm szerokości, bez przeszkód",
      "Każda strefa dostępna także z pozycji siedzącej na podłodze i z wózka",
      "Blaty na różnych wysokościach — także jeden regulowany",
      "Meble stabilne, z zaokrąglonymi krawędziami, przytwierdzone do ściany"], "mint") +
  info_box("Informacja i orientacja", [
      "Każdy pojemnik opisany <b>obrazkiem + słowem</b>, nie samym napisem",
      "Plan dnia w piktogramach, na wysokości oczu dziecka",
      "Granice stref widoczne: dywan, kolor podłogi, niski regał",
      "Stałe miejsce każdej strefy — zmiana zawsze zapowiedziana"], "pink") +
  '</div><div class="col-text">' +
  info_box("Bodźce i regulacja", [
      "Ściany spokojne — dekoracje na jednej ścianie, nie na wszystkich",
      "Miękkie powierzchnie tłumiące hałas: dywan, filc, zasłony",
      "Możliwość przyciemnienia światła w części sali",
      "Strefa wyciszenia dostępna dla każdego, bez pytania o zgodę"], "purple") +
  info_box("Uczestnictwo", [
      "Każda aktywność ma wersję łatwiejszą i trudniejszą — bez zmiany tematu",
      "Dziecko może odpowiedzieć słowem, gestem lub wskazaniem obrazka",
      "Materiały w kilku fakturach i rozmiarach chwytu",
      "Czas na zadanie elastyczny — brak wyścigu, kto pierwszy"], "mint") +
  '</div></div>' +
  wide_photo("n01", "Sala z szerokimi przejściami i regulowanym blatem",
             "Szerokie przejście, otwarta półka i blat z miejscem na wózek — bez żadnego sprzętu specjalistycznego",
             "height:52mm;"))

P("Poziom 1 — uniwersalne projektowanie zajęć", "mint", lambda n, t:
  head("POZIOM 1 · ZAJĘCIA", "mint", "Nie tylko meble — uniwersalne projektowanie zajęć",
       "Ta sama zasada, zastosowana do sposobu prowadzenia zajęć: trzy kanały zamiast jednego.") +
  '<div class="three-lvl" style="grid-template-columns:1fr 1fr 1fr;">'
  '<div class="tl-col sf-l1"><div class="tlh"><div class="tlb bg-l1">1</div>'
  '<div class="tlt tx-l1">Wiele sposobów zaangażowania</div></div><ul>'
  '<li>Dziecko ma realny wybór aktywności</li><li>Temat bliski doświadczeniu dziecka</li>'
  '<li>Praca sama, w parze lub w grupie</li><li>Możliwość wyjścia i powrotu bez oceny</li></ul></div>'
  '<div class="tl-col sf-l2"><div class="tlh"><div class="tlb bg-l2">2</div>'
  '<div class="tlt tx-l2">Wiele sposobów przekazu</div></div><ul>'
  '<li>Polecenie mówione + obrazek + pokaz</li><li>Historia obrazkowa zamiast długiej instrukcji</li>'
  '<li>Model do dotknięcia, nie tylko rysunek</li><li>Kluczowe słowa powtarzane w tej samej formie</li></ul></div>'
  '<div class="tl-col sf-l3"><div class="tlh"><div class="tlb bg-l3">3</div>'
  '<div class="tlt tx-l3">Wiele sposobów działania</div></div><ul>'
  '<li>Odpowiedź słowem, gestem, obrazkiem</li><li>Praca na stojąco, siedząco lub leżąco</li>'
  '<li>Efekt: budowla, rysunek, opowiedzenie</li><li>Ocenianie postępu, nie tempa</li></ul></div></div>' +
  '<div class="two-col" style="margin-top:2mm;"><div class="col-text body-text">'
  '<p>Zasada praktyczna: <strong>jeśli zajęcia da się wykonać tylko jednym sposobem, '
  'zawsze wykluczysz część grupy</strong>. Jeśli da się je wykonać trzema — nikt nie musi być '
  'wyciągany na zewnątrz i „dostosowywany” osobno.</p>' +
  warn("„Zrobiłam dodatkowe zajęcia dla Zosi” — jeśli Zosia musi wychodzić z sali za każdym razem, "
       "gdy grupa robi coś ciekawego, to nie jest wsparcie, tylko wykluczenie z lepszą nazwą.") +
  '</div><div style="flex:.85;">' +
  wide_photo("n03", "Plan dnia w piktogramach i oznaczenia obrazkowe pojemników",
             "Ta sama informacja w obrazku i w słowie — działa dla całej grupy", "height:58mm;") +
  '</div></div>')

P("Poziom 2 — dla jakich dzieci", "pink", lambda n, t:
  head("POZIOM 2", "pink", "Dostosowania ukierunkowane — dla jakich dzieci",
       "Wsparcie dla dziecka, które ma rozpoznaną trudność, ale <b>nie ma orzeczenia</b> "
       "o potrzebie kształcenia specjalnego.") +
  '<div class="two-col"><div class="col-text">'
  '<div class="body-text"><p>Poziom 2 to obszar pomocy psychologiczno-pedagogicznej. '
  'Uruchamia go <strong>rozpoznanie nauczyciela</strong> albo opinia poradni — nie orzeczenie. '
  'Nie potrzebujesz dokumentu, żeby zacząć: potrzebujesz obserwacji i decyzji.</p></div>' +
  info_box("Dla kogo — konkretnie", [
      "Dzieci z opinią poradni psychologiczno-pedagogicznej",
      "Dzieci z rozpoznaną trudnością rozwojową bez orzeczenia (mowa, motoryka, uwaga)",
      "Dzieci z zaburzeniami przetwarzania sensorycznego",
      "Dzieci z chorobą przewlekłą — cukrzyca, padaczka, astma, alergie",
      "Dzieci z doświadczeniem migracji, nieznające języka polskiego",
      "Dzieci po trudnych doświadczeniach — strata, rozstanie rodziców, hospitalizacja",
      "Dzieci nieśmiałe, wycofane, z mutyzmem wybiórczym",
      "Dzieci ze szczególnymi uzdolnieniami, którym w grupie jest za wolno"], "pink") +
  '</div><div class="col-text">' +
  info_box("Co robisz na tym poziomie", [
      "Dostosowujesz <b>miejsce</b> dziecka w sali — bliżej nauczyciela, dalej od hałasu",
      "Dajesz <b>dodatkowy sygnał</b> — uprzedzenie o zmianie, minutnik, obrazek",
      "Zmniejszasz obciążenie — mniej elementów, krótsze zadanie, przerwa ruchowa",
      "Dokładasz konkretną pomoc — nakładka na kredkę, mata, słuchawki",
      "Ustalasz stały sygnał wyjścia do strefy wyciszenia",
      "Dokumentujesz, co zadziałało — to podstawa ewentualnego wniosku o orzeczenie"], "purple") +
  warn("Czekanie na „papier”. Dziecko, które od pół roku zatyka uszy przy każdym hałasie, "
       "nie potrzebuje najpierw diagnozy — potrzebuje słuchawek wygłuszających dzisiaj.") +
  info_box("Kiedy poziom 2 nie wystarcza", [
      "Trudność utrzymuje się mimo trzech różnych dostosowań i trzech miesięcy pracy",
      "Dziecko nie uczestniczy w większości aktywności grupy",
      "Potrzebne są pomoce specjalistyczne lub stałe wsparcie osoby dorosłej",
      "Wtedy zespół rozmawia z rodzicami o wniosku do poradni — z dokumentacją tego, co już próbowaliście"], "mint") +
  '</div></div>' +
  '<div class="legal-note">Pomoc psychologiczno-pedagogiczna w przedszkolu jest udzielana '
  'z inicjatywy m.in. nauczyciela, rodzica lub specjalisty — nie wymaga orzeczenia o potrzebie '
  'kształcenia specjalnego.</div>')

P("Poziom 2 w praktyce — organizacja i wyposażenie", "pink", lambda n, t:
  head("POZIOM 2 · PRAKTYKA", "pink", "Jak zorganizować poziom 2 w sali") +
  '<div class="two-col"><div class="col-text" style="flex:1.2;">' +
  '<table class="grid"><thead><tr><th style="width:38%">Trudność dziecka</th>'
  '<th>Konkretne rozwiązanie w sali</th></tr></thead><tbody>' +
  "".join('<tr><td class="k">%s</td><td>%s</td></tr>' % (a, b) for a, b in [
      ("Trudność z koncentracją", "Stałe miejsce przy blacie tyłem do ruchu, parawan, mniej elementów"),
      ("Nadwrażliwość słuchowa", "Słuchawki wygłuszające na haczyku w strefie wyciszenia"),
      ("Trudność motoryczna", "Nakładki na kredki, nożyczki sprężynowe, mata antypoślizgowa"),
      ("Trudność w mowie", "Tablica wyboru z obrazkami przy każdej strefie"),
      ("Choroba przewlekła", "Miejsce na krótki odpoczynek, dostęp do wody, procedura na ścianie"),
      ("Bariera językowa", "Słownik obrazkowy, plan dnia w obrazkach, para wspierająca"),
      ("Silne reakcje emocjonalne", "Umówiony sygnał wyjścia, termometr emocji, kącik ciszy"),
  ]) + '</tbody></table>' +
  '</div><div class="col-text" style="flex:.85;">' +
  info_box("Wyposażenie startowe — poziom 2", [
      "Słuchawki wygłuszające (2 pary na salę)",
      "Zestaw nakładek i pogrubionych uchwytów",
      "Maty antypoślizgowe pod prace",
      "Minutnik wizualny",
      "Tablice wyboru i piktogramy",
      "Parawan lub przenośna przegroda",
      "Poduszka sensoryczna do siedzenia",
      "Gniotki i chwytki do rąk"], "mint") +
  '</div></div>' +
  wide_photo("n09", "Pomoce wspierające motorykę małą",
             "Nakładki, pogrubione kredki, mata antypoślizgowa — tanie rozwiązania poziomu 2",
             "height:56mm;"))

P("Poziom 3 — dla jakich dzieci", "purple", lambda n, t:
  head("POZIOM 3", "purple", "Wsparcie zindywidualizowane — dla jakich dzieci",
       "Dzieci z orzeczeniem o potrzebie kształcenia specjalnego. Podstawą działania jest "
       "WOPFU i IPET, a nie sama diagnoza medyczna.") +
  '<div class="two-col"><div class="col-text">' +
  info_box("Dla kogo", [
      "Dzieci niesłyszące i słabosłyszące",
      "Dzieci niewidome i słabowidzące",
      "Dzieci z niepełnosprawnością ruchową, w tym z afazją",
      "Dzieci z niepełnosprawnością intelektualną (lekką, umiarkowaną, znaczną)",
      "Dzieci ze spektrum autyzmu, w tym z zespołem Aspergera",
      "Dzieci z niepełnosprawnościami sprzężonymi",
      "Dzieci zagrożone niedostosowaniem społecznym"], "purple") +
  '<div class="body-text" style="margin-top:1mm;"><p>Na tym poziomie dostosowanie przestrzeni '
  '<strong>przestaje być decyzją nauczyciela, a staje się zapisem w dokumencie</strong>. '
  'To, co ustalisz w IPET, musi mieć odzwierciedlenie w wyglądzie sali.</p></div>'
  '</div><div class="col-text">' +
  '<div class="flow-steps">'
  '<div class="flow-step"><div class="fs-n">1</div><div class="fs-t">'
  '<strong>Orzeczenie</strong> z poradni psychologiczno-pedagogicznej trafia do przedszkola.</div></div>'
  '<div class="flow-step"><div class="fs-n">2</div><div class="fs-t">'
  '<strong>WOPFU</strong> — zespół opisuje mocne strony, trudności i <b>bariery w środowisku</b>. '
  'Tu wpisuje się układ sali.</div></div>'
  '<div class="flow-step"><div class="fs-n">3</div><div class="fs-t">'
  '<strong>IPET</strong> — zespół zapisuje konkretne dostosowania warunków i sprzęt specjalistyczny.</div></div>'
  '<div class="flow-step"><div class="fs-n">4</div><div class="fs-t">'
  '<strong>Realizacja w sali</strong> — meble, sprzęt i organizacja dnia zmieniają się zgodnie z IPET.</div></div>'
  '<div class="flow-step"><div class="fs-n">5</div><div class="fs-t">'
  '<strong>Ewaluacja</strong> — co najmniej dwa razy w roku szkolnym; wnioski wracają do układu sali.</div></div>'
  '</div>' +
  warn("IPET opisuje dziecko, ale nie opisuje przestrzeni. Zapis „zapewnić spokojne miejsce pracy” "
       "bez wskazania, gdzie ono jest w tej konkretnej sali, nie zmienia niczego.") +
  '</div></div>')

P("Poziom 3 w praktyce — sala, sprzęt, organizacja", "purple", lambda n, t:
  head("POZIOM 3 · PRAKTYKA", "purple", "Jak zorganizować poziom 3 w sali") +
  '<div class="two-col"><div class="col-text" style="flex:1.15;">' +
  info_box("Co zwykle trzeba zmienić w przestrzeni", [
      "Stałe, oznaczone miejsce pracy indywidualnej — w sali, nie na korytarzu",
      "Miejsce na sprzęt: wózek, pionizator, komunikator, powiększalnik",
      "Poszerzone dojście do jednej lub dwóch stref (min. 120 cm dla manewru wózkiem)",
      "Indywidualny plan dnia dziecka obok planu grupowego",
      "Miejsce dla nauczyciela wspomagającego, które nie odgradza dziecka od grupy"], "purple") +
  info_box("Sprzęt specjalistyczny — typowe pozycje z IPET", [
      "Komunikator AAC lub tablet z aplikacją komunikacyjną",
      "System FM / pętla indukcyjna dla dziecka z aparatem",
      "Powiększalnik, materiały w druku powiększonym, oznaczenia dotykowe",
      "Krzesło z podparciem, stolik z wycięciem, pas stabilizujący",
      "Sprzęt do terapii SI uzgodniony z terapeutą"], "mint") +
  '</div><div class="col-text" style="flex:.85;">' +
  wide_photo("n11", "Miejsce pracy indywidualnej w sali przedszkolnej",
             "Miejsce pracy 1:1 — w sali, obok grupy, nie za drzwiami", "height:52mm;") +
  '<div style="height:3mm;"></div>' +
  warn("Wyprowadzanie dziecka z sali „dla świętego spokoju grupy”. Poziom 3 ma umożliwić "
       "uczestnictwo w zajęciach grupy — nie zastąpić go osobnym trybem dnia.") +
  '</div></div>')

P("Matryca: strefa × poziom wsparcia", "mint", lambda n, t:
  head("MATRYCA", "mint", "Pięć stref × trzy poziomy wsparcia",
       "Jedna tabela, w której widać, co zrobić w każdej strefie na każdym poziomie.") +
  '<table class="grid" style="font-size:7.6pt;"><thead><tr>'
  '<th style="width:19%">Strefa</th><th style="width:27%">Poziom 1 — dla wszystkich</th>'
  '<th style="width:27%">Poziom 2 — ukierunkowany</th><th>Poziom 3 — indywidualny</th></tr></thead><tbody>' +
  "".join('<tr><td class="k">%s</td><td class="c1">%s</td><td class="c2">%s</td><td>%s</td></tr>' % r for r in [
      ("Czytelnictwa", "Książki obrazkowe i dotykowe, niski regał, oznaczenia obrazkowe",
       "Duży druk, mniej książek naraz, miejsce z dala od hałasu",
       "Książki brajlowskie, wersje AAC, mówiące książki, podpórka do czytania"),
      ("Budowania", "Klocki różnej wielkości i faktury, praca na podłodze i przy blacie",
       "Mata antypoślizgowa, mniej elementów, instrukcja obrazkowa",
       "Klocki magnetyczne, uchwyt adaptacyjny, blat z wycięciem na wózek"),
      ("Artystyczna", "Materiały w zasięgu dziecka, kilka wysokości blatu, fartuchy",
       "Nakładki na kredki, nożyczki sprężynowe, alternatywa dla farb",
       "Sztaluga na wysokości wózka, stabilizacja ręki, malowanie z asystą"),
      ("Odpoczywania", "Dostępna dla każdego bez pytania, miękko, ciszej, ciemniej",
       "Słuchawki wygłuszające, kołdra obciążeniowa, minutnik wizualny",
       "Indywidualny plan wyciszania, namiot sensoryczny, sprzęt z zaleceń terapeuty"),
      ("Przyrody", "Materiały naturalne, obserwacje wielozmysłowe, tablica obrazkowa",
       "Krótsze doświadczenia, lupa powiększająca, jedna czynność naraz",
       "Taca wysuwana, pomoce dotykowe, opis doświadczenia w AAC"),
      ("Poza salą (ogród)", "Utwardzone dojście, cień, miejsce do siedzenia",
       "Strefa spokojniejsza na placu, zabawa równoległa obok grupy",
       "Sprzęt terenowy dostępny z wózka, asysta przy przemieszczaniu"),
      ("Miejsce posiłków", "Stoły na wysokości dziecka, spokojna atmosfera, samodzielne nakrycie",
       "Sztućce z pogrubioną rączką, mata antypoślizgowa, cichsze miejsce",
       "Krzesło z podparciem, karmienie zgodnie z zaleceniem, dieta eliminacyjna"),
  ]) + '</tbody></table>' +
  info_box("Jak używać matrycy w zespole", [
      "Wydrukuj tabelę i zaznacz kolorem to, co już jest w Twojej sali",
      "Puste pola w kolumnie „poziom 1” to zawsze pierwszy priorytet zespołu",
      "Do kolumny „poziom 3” wpisz imiona dzieci, których zapisy z IPET dotyczą",
      "Wróć do matrycy po każdym monitoringu — to gotowa lista zadań na kolejny miesiąc"], "purple") +
  '<div class="legal-note" style="margin-top:auto;">Zasada czytania tabeli: zaczynasz zawsze '
  'od lewej kolumny. Kolumnę „poziom 3” wypełniasz dopiero wtedy, gdy poziom 1 i 2 są już w sali — '
  'inaczej sprzęt specjalistyczny zastępuje organizację, zamiast ją uzupełniać.</div>')

P("Ścieżka decyzyjna — który poziom wybrać", "purple", lambda n, t:
  head("DECYZJA", "purple", "Który poziom wsparcia wybrać — ścieżka decyzyjna",
       "Pięć pytań, które prowadzą od obserwacji dziecka do konkretnej zmiany w sali.") +
  '<div class="two-col"><div class="col-text">'
  '<div class="flow-steps">'
  '<div class="flow-step"><div class="fs-n">1</div><div class="fs-t">'
  '<strong>Co dokładnie widzę?</strong> Opisz zachowanie, nie etykietę: „nie wchodzi do strefy '
  'budowania”, a nie „jest niegrzeczny”.</div></div>'
  '<div class="flow-step"><div class="fs-n">2</div><div class="fs-t">'
  '<strong>Czy przeszkoda jest w przestrzeni?</strong> Hałas, tłok, brak miejsca, wysoka półka — '
  'zmiana układu sali rozwiązuje więcej sytuacji, niż się wydaje.</div></div>'
  '<div class="flow-step"><div class="fs-n">3</div><div class="fs-t">'
  '<strong>Czy inne dzieci mają podobnie?</strong> Jeśli tak — to poziom 1: zmień rozwiązanie '
  'dla całej grupy.</div></div>'
  '<div class="flow-step"><div class="fs-n">4</div><div class="fs-t">'
  '<strong>Czy to dotyczy jednego dziecka i mija po prostym dostosowaniu?</strong> '
  'To poziom 2 — wdrażasz od razu i notujesz efekt.</div></div>'
  '<div class="flow-step"><div class="fs-n">5</div><div class="fs-t">'
  '<strong>Czy dziecko ma orzeczenie lub trudność jest trwała i głęboka?</strong> '
  'To poziom 3 — zespół, WOPFU, IPET i zapis dostosowań.</div></div></div>' +
  info_box("Reguła 4 tygodni", [], "mint",
           "Każde dostosowanie sprawdzasz przez około cztery tygodnie. Jeśli nie widać zmiany w "
           "funkcjonowaniu dziecka — nie dokładaj kolejnego sprzętu, tylko zmień hipotezę.") +
  '</div><div class="col-photo">' +
  photo("n12", "Widok sali z góry z wyraźnymi ciągami komunikacyjnymi",
        "Zanim zmienisz dziecko — sprawdź, czy da się zmienić przestrzeń") + '</div></div>')

# ---------- CZĘŚĆ III — DEFICYTY ----------
def deficit_page(icon, tone, title, subtitle, intro, barriers, l1, l2, l3, gear, mistake,
                 photo_name, photo_alt, photo_cap):
    tones = {"mint": "var(--mint-deep)", "pink": "var(--pink-deep)", "purple": "var(--purple-deep)"}
    return (deco(tone) +
            '<div class="def-head"><div class="dh-ic" style="background:%s;">%s</div><div>'
            '<h2>%s</h2><div class="dh-sub">%s</div></div></div>' % (tones[tone], IC[icon], title, subtitle) +
            '<div class="two-col" style="flex:none;margin-bottom:2.5mm;">'
            '<div class="col-text" style="flex:1.35;"><div class="body-text" style="font-size:9.6pt;">'
            '<p>%s</p></div>%s</div>'
            '<div style="flex:.75;">%s</div></div>' % (
                intro, info_box("Co utrudnia funkcjonowanie w sali", barriers, tone),
                wide_photo(photo_name, photo_alt, photo_cap, "height:64mm;")) +
            three_lvl(l1, l2, l3) +
            info_box("Wyposażenie i pomoce", gear, "mint") +
            warn(mistake) +
            doc_box(title))

P("Dostosowania — spektrum autyzmu", "mint", lambda n, t: deficit_page(
    "autyzm", "mint", "Spektrum autyzmu", "Przewidywalność · mniej bodźców · jasne granice stref",
    "Dziecko ze spektrum autyzmu czyta salę dosłownie: jeśli układ się zmienia, znika mapa, "
    "według której funkcjonuje. Najważniejszym dostosowaniem nie jest sprzęt, tylko "
    "<strong>stałość i czytelność przestrzeni</strong> oraz realny dostęp do wyciszenia.",
    ["Nadmiar bodźców: dekoracje na wszystkich ścianach, muzyka w tle, echo",
     "Nieoznaczone granice stref — nie wiadomo, gdzie kończy się jedna aktywność",
     "Nagła zmiana układu sali lub planu dnia bez zapowiedzi",
     "Brak miejsca, do którego można się wycofać bez pytania o zgodę"],
    ["Plan dnia w piktogramach dla całej grupy",
     "Stałe miejsce każdej strefy i każdego pojemnika",
     "Spokojne ściany — dekoracje na jednej",
     "Strefa wyciszenia dostępna dla wszystkich"],
    ["Indywidualny plan dnia dziecka na jego półce",
     "Uprzedzenie o zmianie: „za chwilę sprzątamy”",
     "Minutnik wizualny przy zadaniu",
     "Słuchawki wygłuszające na stałym haczyku"],
    ["Stałe miejsce pracy z parawanem, zapisane w IPET",
     "Namiot lub buda sensoryczna w strefie odpoczynku",
     "Historyjki społeczne do sytuacji trudnych w sali",
     "Sprzęt zgodny z zaleceniami terapeuty SI"],
    ["Zestaw piktogramów (plan dnia, strefy, emocje) · Słuchawki wygłuszające · Kołdra lub kamizelka "
     "obciążeniowa · Minutnik wizualny · Namiot / buda · Panele dotykowe · Pudełko z ulubionymi bodźcami"],
    "traktowanie strefy wyciszenia jako miejsca kary. Jeśli dziecko trafia tam „za karę”, "
    "przestaje z niej korzystać wtedy, gdy naprawdę jej potrzebuje.",
    "n02", "Kącik wyciszenia z namiotem, kołdrą obciążeniową i słuchawkami",
    "Wyciszenie: miękko, ciemniej, ciszej — i dostępne bez pytania"))

P("Dostosowania — ADHD i trudności z koncentracją", "pink", lambda n, t: deficit_page(
    "adhd", "pink", "ADHD i trudności z koncentracją", "Mniej bodźców w polu widzenia · ruch jako narzędzie",
    "Dziecko z ADHD nie „nie chce” się skupić — ono reaguje na wszystko, co dzieje się w sali. "
    "Dostosowanie polega na <strong>zmniejszeniu liczby bodźców w polu widzenia</strong> i na "
    "wpisaniu ruchu w plan dnia, zamiast walki z nim.",
    ["Miejsce twarzą do przejścia, drzwi lub okna",
     "Zbyt wiele materiałów wyłożonych naraz",
     "Długie zadania bez wyraźnego końca",
     "Brak legalnej możliwości ruchu między zadaniami"],
    ["Wyraźne granice stref — dywan, kolor, regał",
     "Uporządkowane, zamykane pojemniki",
     "Krótkie zadania z widocznym końcem",
     "Przerwy ruchowe wpisane w rytm dnia"],
    ["Stałe miejsce tyłem do ruchu, przy blacie",
     "Ograniczenie: jeden materiał na stole",
     "Minutnik i sygnał zakończenia",
     "Poduszka sensoryczna, gniotek do rąk"],
    ["Umówiony sygnał wyjścia do strefy ruchu",
     "Zadania dzielone na etapy z obrazkiem",
     "Wzmocnienia zapisane w IPET",
     "Stałe zadanie porządkowe jako regulacja"],
    ["Parawan lub przegroda · Poduszka sensoryczna · Gniotki i chwytki · Minutnik wizualny · "
     "Pojemniki zamykane · Karty „najpierw – potem” · Mata do skakania w strefie ruchu"],
    "sadzanie dziecka „pod okiem” nauczyciela w centrum sali. To najbardziej stymulujące miejsce "
    "w całym pomieszczeniu — sprawdź, gdzie jest najspokojniej, a nie najbliżej.",
    "13", "Dziecko skupione na jednej aktywności w strefie przyrody",
    "Jeden materiał naraz — zamiast wyścigu bodźców"))

P("Dostosowania — niepełnosprawność intelektualna", "purple", lambda n, t: deficit_page(
    "intelekt", "purple", "Niepełnosprawność intelektualna", "Obrazek zamiast napisu · jeden krok naraz",
    "Dziecko z niepełnosprawnością intelektualną potrzebuje sali, w której <strong>informacja jest "
    "widoczna i konkretna</strong>: obrazek zamiast napisu, jedna czynność naraz, ten sam schemat dnia. "
    "To jednocześnie rozwiązania, które pomagają całej grupie.",
    ["Oznaczenia wyłącznie tekstowe — dziecko nie wie, gdzie co jest",
     "Wieloetapowe polecenia podawane naraz",
     "Zbyt duży wybór materiałów w jednym miejscu",
     "Tempo grupy jako jedyne dopuszczalne tempo"],
    ["Każdy pojemnik z obrazkiem zawartości",
     "Plan dnia obrazkowy dla całej grupy",
     "Zadania z wersją prostszą i trudniejszą",
     "Stały, powtarzalny schemat dnia"],
    ["Instrukcja obrazkowa krok po kroku przy strefie",
     "Zadanie dzielone: „najpierw – potem”",
     "Więcej czasu bez presji grupy",
     "Model gotowej pracy obok materiałów"],
    ["Cele z IPET przełożone na czynności w strefach",
     "Stałe wsparcie osoby dorosłej w strefie trudnej",
     "Materiały o obniżonym stopniu złożoności",
     "Ocena postępu wobec siebie, nie wobec grupy"],
    ["Zestaw piktogramów i etykiet obrazkowych · Karty „najpierw – potem” · Instrukcje obrazkowe "
     "do stref · Puzzle i układanki wielopoziomowe · Materiały o dużych elementach · Aparat "
     "do zdjęć własnych oznaczeń"],
    "obniżanie oczekiwań zamiast zmiany sposobu przekazu. Dziecko częściej nie rozumie polecenia, "
    "niż nie umie wykonać zadania.",
    "n03", "Oznaczenia obrazkowe pojemników i plan dnia w piktogramach",
    "Obrazek na pojemniku działa lepiej niż jakikolwiek napis"))

P("Dostosowania — niepełnosprawność ruchowa", "pink", lambda n, t: deficit_page(
    "ruch", "pink", "Niepełnosprawność ruchowa", "Dojazd · dosięg · stabilizacja ciała",
    "Dla dziecka z niepełnosprawnością ruchową sala dzieli się na dwie części: tę, do której dojedzie "
    "i sięgnie, i tę, która dla niego nie istnieje. <strong>Dostępność mierzy się w centymetrach</strong> — "
    "szerokości przejść, wysokości półek, miejscu pod blatem.",
    ["Przejścia zastawione meblami, dywanem z zawiniętym brzegiem, torbami",
     "Półki i haczyki powyżej zasięgu z pozycji siedzącej",
     "Blaty bez wolnej przestrzeni pod spodem",
     "Aktywności organizowane wyłącznie na podłodze"],
    ["Główne ciągi min. 90 cm, wolne przez cały dzień",
     "Materiały na wysokości 40–120 cm",
     "Blaty na kilku wysokościach, jeden regulowany",
     "Zabawa możliwa przy stole i na podłodze"],
    ["Mata antypoślizgowa i pojemniki przysuwane",
     "Nakładki na przybory, uchwyty zamiast gałek",
     "Krzesło z podparciem boków i stóp",
     "Miejsce w strefie zarezerwowane dla dziecka"],
    ["Miejsce na wózek, pionizator, sprzęt rehabilitacyjny",
     "Stolik z wycięciem, pas stabilizujący",
     "Manewr wózkiem min. 120 cm w kluczowych strefach",
     "Asysta zapisana w IPET — kiedy i do czego"],
    ["Blat regulowany · Stolik z wycięciem · Mata antypoślizgowa · Nakładki i pogrubione uchwyty · "
     "Nożyczki sprężynowe · Podpórka pod książkę · Pojemniki na wysuwanych tacach"],
    "przenoszenie dziecka „na skróty” zamiast zmiany układu mebli. Każde przeniesienie odbiera "
    "dziecku decyzję o tym, gdzie chce być.",
    "n01", "Dziecko na wózku samodzielnie korzystające z otwartej półki",
    "Otwarta półka i blat z miejscem na wózek — samodzielność bez proszenia"))

P("Dostosowania — dziecko niesłyszące i słabosłyszące", "mint", lambda n, t: deficit_page(
    "sluch", "mint", "Dziecko niesłyszące i słabosłyszące", "Akustyka · światło na twarzy · sygnał widoczny",
    "Dla dziecka z niedosłuchem najważniejszym parametrem sali jest <strong>akustyka</strong>: "
    "pogłos i szum tła męczą bardziej niż sama głośność. Drugim jest światło — dziecko odczytuje "
    "z twarzy i musi ją widzieć.",
    ["Twarde powierzchnie i pogłos — hałas klocków, krzeseł, echo",
     "Nauczyciel mówiący tyłem lub pod światło",
     "Sygnały wyłącznie dźwiękowe (dzwonek, klaśnięcie)",
     "Rozmowa w dużym kole, gdzie nie widać twarzy mówiącego"],
    ["Dywan, filc, zasłony — tłumienie pogłosu",
     "Nakładki filcowe na nogi krzeseł",
     "Sygnały widoczne: gest, światło, obrazek",
     "Mówienie twarzą do grupy, w dobrym świetle"],
    ["Stałe miejsce blisko nauczyciela, plecami do okna",
     "Powtórzenie polecenia po sprawdzeniu kontaktu wzrokowego",
     "Cichsza strefa do zabaw wymagających rozmowy",
     "Wsparcie obrazkowe do każdego polecenia"],
    ["System FM lub pętla indukcyjna — z miejscem na sprzęt",
     "Wsparcie w komunikacji zgodne z orzeczeniem",
     "Elementy języka migowego wprowadzone w całej grupie",
     "Alarm i sygnały bezpieczeństwa również świetlne"],
    ["Nakładki filcowe na meble · Dywany i panele akustyczne · Karty obrazkowe do poleceń · "
     "Lampa doświetlająca twarz nauczyciela · System FM (z IPET) · Sygnalizator świetlny"],
    "krzyczenie zamiast mówienia wyraźnie. Podniesiony głos zniekształca dźwięk w aparacie — "
    "działa gorsze zrozumienie, nie lepsze.",
    "n05", "Nauczycielka mówi twarzą do dziecka z aparatem słuchowym",
    "Twarz w świetle, dziecko blisko, pogłos wytłumiony panelami"))

P("Dostosowania — dziecko niewidome i słabowidzące", "purple", lambda n, t: deficit_page(
    "wzrok", "purple", "Dziecko niewidome i słabowidzące", "Kontrast · stałość układu · dotyk i dźwięk",
    "Dziecko z dysfunkcją wzroku buduje mapę sali w pamięci i przez dotyk. Dlatego "
    "<strong>przestawienie mebli jest dla niego poważniejszą zmianą niż dla całej reszty grupy</strong>. "
    "Kluczowe są: stałość, kontrast i oznaczenia dotykowe.",
    ["Zmiana układu mebli bez uprzedzenia i bez pokazania",
     "Niski kontrast — jasne przedmioty na jasnym tle",
     "Przedmioty pozostawione na ciągach komunikacyjnych",
     "Instrukcje typu „to weź stamtąd” — bez konkretu"],
    ["Stały układ sali i wolne ciągi komunikacyjne",
     "Kontrastowe oznaczenia krawędzi i drzwi",
     "Równomierne oświetlenie bez olśnienia",
     "Nazywanie czynności słowem: „kładę klocek po Twojej lewej”"],
    ["Materiały powiększone i kontrastowe",
     "Lampka punktowa przy stanowisku pracy",
     "Lupa lub powiększalnik w strefie przyrody",
     "Podkładka kontrastowa pod pracę"],
    ["Oznaczenia dotykowe stref i szafek",
     "Książki brajlowskie i dotykowe, pomoce wypukłe",
     "Nauka trasy po sali z nauczycielem wspomagającym",
     "Sprzęt optyczny wskazany w orzeczeniu"],
    ["Taśma kontrastowa na krawędzie · Oznaczenia dotykowe (fakturowe) · Lampka punktowa · "
     "Lupa i powiększalnik · Książki dotykowe · Podkładki kontrastowe · Materiały o wyraźnej fakturze"],
    "prowadzenie dziecka za rękę wszędzie, gdzie idzie. Zabiera to możliwość nauczenia się sali — "
    "lepiej nauczyć trasy raz, niż prowadzić sto razy.",
    "n06", "Książki dotykowe, lupa i kontrastowe oznaczenia krawędzi",
    "Kontrast, faktura i punktowe światło zamiast domyślnego wystroju"))

P("Dostosowania — zaburzenia przetwarzania sensorycznego", "mint", lambda n, t: deficit_page(
    "sensor", "mint", "Zaburzenia przetwarzania sensorycznego", "Regulacja bodźców · ruch · odpoczynek",
    "Dziecko z zaburzeniami przetwarzania sensorycznego odbiera bodźce mocniej lub słabiej niż "
    "reszta grupy. Sala powinna dawać obie możliwości: <strong>wyciszenie dla nadwrażliwych "
    "i mocny bodziec ruchowy dla poszukujących</strong>.",
    ["Jednolita głośność i jasność sali przez cały dzień",
     "Brak legalnego sposobu na dostarczenie sobie ruchu",
     "Materiały tylko o jednej fakturze",
     "Przymus udziału w zabawie o dużym natężeniu bodźców"],
    ["Strefa wyciszenia i strefa ruchu — obie dostępne",
     "Materiały o różnych fakturach w każdej strefie",
     "Możliwość przyciemnienia części sali",
     "Przerwy ruchowe w rytmie dnia"],
    ["Poduszka sensoryczna, taśma oporowa przy krześle",
     "Kołdra obciążeniowa dostępna w strefie ciszy",
     "Słuchawki wygłuszające na czas hałaśliwych zajęć",
     "Uprzedzanie o zajęciach głośnych i mokrych"],
    ["Sprzęt zgodny z zaleceniem terapeuty SI",
     "Indywidualna dieta sensoryczna wpisana w plan dnia",
     "Huśtawka lub deska równoważna, jeśli warunki pozwalają",
     "Stały rytuał wejścia i wyjścia z zajęć"],
    ["Poduszka sensoryczna · Kołdra obciążeniowa · Słuchawki wygłuszające · Panele i ścieżki "
     "dotykowe · Deska równoważna · Gniotki, masy plastyczne · Taśma oporowa do krzesła"],
    "traktowanie potrzeby ruchu jako złego zachowania. Dziecko, które kręci się na krześle, "
    "najczęściej reguluje się, a nie przeszkadza.",
    "n04", "Strefa ruchu i integracji sensorycznej w przedszkolu",
    "Strefa ruchu to nie nagroda — to narzędzie regulacji"))

P("Dostosowania — mowa i komunikacja (AAC)", "pink", lambda n, t: deficit_page(
    "mowa", "pink", "Zaburzenia mowy i komunikacji", "Komunikacja alternatywna · wybór bez słów",
    "Dziecko, które nie mówi lub mówi niewyraźnie, w źle zorganizowanej sali traci wpływ na cały "
    "swój dzień — bo każda decyzja wymaga słów. <strong>Rozwiązaniem jest komunikacja "
    "wspomagająca (AAC)</strong>: obrazek, gest, tablica wyboru, komunikator.",
    ["Wszystkie wybory dokonywane wyłącznie słownie",
     "Materiały schowane — nie da się pokazać, czego się chce",
     "Presja czasu na odpowiedź",
     "Odpowiadanie za dziecko przez dorosłego lub rówieśników"],
    ["Materiały widoczne — można wskazać zamiast nazwać",
     "Tablica wyboru z obrazkami przy każdej strefie",
     "Akceptacja odpowiedzi gestem i wskazaniem",
     "Kluczowe słowa wspierane gestem w całej grupie"],
    ["Osobista książka lub tablica komunikacyjna dziecka",
     "Symbole dla najczęstszych potrzeb: pić, toaleta, pomoc, koniec",
     "Czas na odpowiedź — co najmniej kilka sekund ciszy",
     "Wsparcie obrazkowe do zabaw zespołowych"],
    ["Komunikator lub tablet z aplikacją AAC — zawsze przy dziecku",
     "Symbole AAC w całej sali, nie tylko na ławce dziecka",
     "Szkolenie zespołu i rówieśników z korzystania z tablicy",
     "Cele komunikacyjne zapisane w IPET"],
    ["Tablice wyboru · Książka komunikacyjna · Symbole PCS / piktogramy · Komunikator "
     "jednoprzyciskowy · Tablet z aplikacją AAC · Karty „chcę / nie chcę / koniec” · Gesty wspomagające"],
    "odkładanie AAC „aż dziecko zacznie mówić”. Komunikacja wspomagająca nie hamuje mowy — "
    "zmniejsza frustrację i najczęściej ją wspiera.",
    "n07", "Tablica komunikacyjna AAC przy wejściu do sali",
    "Tablica AAC na ścianie sali — dostępna dla dziecka i dla grupy"))

P("Dostosowania — choroby przewlekłe", "purple", lambda n, t: deficit_page(
    "zdrowie", "purple", "Dzieci z chorobami przewlekłymi", "Cukrzyca · padaczka · astma · alergie",
    "Choroba przewlekła rzadko wymaga przebudowy sali — wymaga <strong>procedury, miejsca "
    "i przewidywalności</strong>. Dziecko ma prawo uczestniczyć we wszystkim, pod warunkiem że "
    "zespół wie, co robić, gdy pojawi się objaw.",
    ["Brak miejsca na krótki odpoczynek po wysiłku lub incydencie",
     "Brak dostępu do wody i przekąski w ciągu dnia",
     "Procedura znana tylko jednej osobie z zespołu",
     "Wykluczanie z zajęć ruchowych „na wszelki wypadek”"],
    ["Dostęp do wody przez cały dzień",
     "Miejsce do odpoczynku w strefie wyciszenia",
     "Rytm dnia z przewidywalnymi porami posiłków",
     "Bezpieczne, oznaczone wyposażenie sali"],
    ["Miejsce na leki i sprzęt — zamknięte, ale szybko dostępne",
     "Procedura postępowania widoczna dla całego zespołu",
     "Dostosowanie intensywności zajęć ruchowych",
     "Ustalone zasady posiłków przy alergii pokarmowej"],
    ["Zapisy w IPET dla dziecka z orzeczeniem",
     "Indywidualny plan opieki uzgodniony z rodzicami i lekarzem",
     "Przeszkolenie całego zespołu z konkretnej sytuacji",
     "Sprzęt medyczny dziecka w ustalonym, stałym miejscu"],
    ["Zamykana szafka na leki · Karta procedury na wewnętrznej stronie drzwi szafki · Leżanka "
     "lub materac w strefie ciszy · Dostęp do wody · Lista alergenów w kuchni i w sali"],
    "chronienie dziecka przez wyłączanie go z aktywności. Ograniczaj konkretne czynniki ryzyka, "
    "nie całe obszary życia grupy.",
    "n14", "Bezpieczne miejsce odpoczynku i zamykana szafka w sali",
    "Miejsce odpoczynku, woda i procedura — to zwykle wystarczy"))

P("Dostępność językowa — dzieci z doświadczeniem migracji", "mint", lambda n, t: deficit_page(
    "jezyk", "mint", "Dzieci nieznające języka polskiego", "Dostępność językowa · obraz zamiast słowa",
    "Dziecko z doświadczeniem migracji nie ma deficytu — ma barierę językową. W praktyce sali "
    "wygląda to jednak podobnie: <strong>bez wsparcia obrazkowego traci dostęp do informacji</strong> "
    "i wycofuje się z zabawy, mimo że wszystko rozumie poznawczo.",
    ["Cała informacja w sali wyłącznie po polsku, w formie tekstu",
     "Polecenia złożone, podawane szybko i tylko słownie",
     "Brak sygnału, że dziecko może odpowiedzieć gestem",
     "Milczenie odbierane jako brak zainteresowania"],
    ["Oznaczenia obrazkowe wszystkich stref i pojemników",
     "Plan dnia w piktogramach",
     "Polecenie + pokaz zamiast samego polecenia",
     "Zabawy niewymagające języka: budowanie, ruch, sztuka"],
    ["Słownik obrazkowy najważniejszych słów dnia",
     "Dziecko-przewodnik na pierwsze tygodnie",
     "Kluczowe słowa także w języku dziecka",
     "Akceptacja okresu ciszy — bez przymusu mówienia"],
    ["Wsparcie zapisane w pomocy psychologiczno-pedagogicznej",
     "Zajęcia z języka polskiego jako obcego, jeśli są organizowane",
     "Stały kontakt z rodzicami przez tłumaczenie lub obrazki",
     "Materiały dwujęzyczne w strefie czytelnictwa"],
    ["Słownik obrazkowy · Karty powitań i próśb · Plan dnia w piktogramach · Etykiety dwujęzyczne "
     "· Książki obrazkowe bez tekstu · Mapa z zaznaczonym krajem dziecka"],
    "traktowanie ciszy dziecka jako opóźnienia rozwojowego. Okres milczenia w nowym języku "
    "to zjawisko typowe — nie przesłanka do diagnozy.",
    "n13", "Kącik powitalny ze słownikiem obrazkowym i mapą",
    "Kącik powitalny: obraz, mapa i karty zamiast tłumaczenia słów"))

P("Ściągawka — deficyt i pierwsza zmiana w sali", "pink", lambda n, t:
  head("SZYBKA ŚCIĄGAWKA", "pink", "Od czego zacząć przy każdym deficycie",
       "Jedna zmiana, którą warto wprowadzić najpierw — zanim kupisz cokolwiek.") +
  '<table class="grid" style="font-size:7.9pt;"><thead><tr><th style="width:24%">Potrzeba dziecka</th>'
  '<th style="width:30%">Pierwsza zmiana — dziś, za zero złotych</th>'
  '<th>Druga zmiana — drobny zakup</th></tr></thead><tbody>' +
  "".join('<tr><td class="k">%s</td><td class="c1">%s</td><td class="c2">%s</td></tr>' % r for r in [
      ("Spektrum autyzmu", "Ustal stały układ sali i uprzedzaj o każdej zmianie", "Piktogramy, słuchawki wygłuszające"),
      ("ADHD", "Przesuń miejsce dziecka tyłem do ruchu w sali", "Parawan, minutnik wizualny"),
      ("Niepełnosprawność intelektualna", "Podpisz pojemniki obrazkiem, nie napisem", "Karty „najpierw – potem”"),
      ("Niepełnosprawność ruchowa", "Zwolnij przejścia i obniż jedną półkę w każdej strefie", "Mata antypoślizgowa, nakładki"),
      ("Niedosłuch", "Mów twarzą do dziecka, w świetle, bez tła muzycznego", "Filcowe nakładki na krzesła"),
      ("Słaby wzrok", "Oznacz krawędzie kontrastem i nie przestawiaj mebli", "Lampka punktowa, lupa"),
      ("Zaburzenia SI", "Wpisz przerwy ruchowe w rytm dnia", "Poduszka sensoryczna, kołdra obciążeniowa"),
      ("Trudności w mowie", "Wyłóż materiały tak, żeby dało się je wskazać", "Tablica wyboru z obrazkami"),
      ("Choroba przewlekła", "Powieś procedurę tam, gdzie widzi ją cały zespół", "Leżanka, zamykana szafka"),
      ("Bariera językowa", "Dodaj obraz do każdego polecenia", "Słownik obrazkowy"),
      ("Mutyzm wybiórczy", "Przestań wymagać odpowiedzi słownej przy grupie", "Karty odpowiedzi TAK / NIE"),
      ("Po trudnym doświadczeniu", "Zapewnij przewidywalny rytm dnia i stałe miejsce", "Kącik ciszy z przytulanką"),
      ("Szczególne uzdolnienia", "Dołóż trudniejszą wersję zadania w tej samej strefie", "Materiały o wyższym stopniu złożoności"),
  ]) + '</tbody></table>' +
  '<div class="legal-note" style="margin-top:auto;">Kolejność nie jest przypadkowa: '
  '<b>najpierw organizacja, potem sprzęt</b>. Zakup, który nie ma miejsca w rytmie dnia '
  'i w układzie sali, zwykle po miesiącu ląduje w szafie.</div>')

EXTRA_CSS2 = """
.cbx{display:inline-block;width:3.6mm;height:3.6mm;border:1pt solid var(--purple-deep);
  border-radius:1mm;background:#fff;vertical-align:-.4mm;}
.cbx+.cbx{margin-left:2.4mm;}
.tick-head{font-family:'Nunito';font-weight:800;font-size:6.6pt;color:var(--purple-deep);
  text-transform:uppercase;letter-spacing:.04em;}
.form-row{display:flex;gap:3mm;align-items:flex-end;margin-bottom:2.6mm;}
.form-row .fl{font-family:'Nunito';font-weight:800;font-size:8pt;color:var(--purple-deep);white-space:nowrap;}
.form-row .fv{flex:1;border-bottom:.9pt dashed var(--line);height:5.2mm;}
.obs-grid{display:grid;grid-template-columns:1fr 1fr;gap:2.6mm;}
.obs-card{border:1.2pt solid var(--line);border-radius:4mm;padding:2.8mm 3.2mm;}
.obs-card .oc-t{font-family:'Quicksand';font-weight:700;font-size:9.6pt;color:var(--purple-deep);margin:0 0 2mm;}
.obs-card .oc-l{border-bottom:.8pt dashed var(--line);height:6mm;margin-bottom:1.8mm;}
.kpi-row{display:flex;gap:2.6mm;margin:1mm 0 3mm;}
.kpi{flex:1;border-radius:4mm;padding:2.8mm 3mm;text-align:center;}
.kpi .kv{font-family:'Quicksand';font-weight:700;font-size:15pt;line-height:1;}
.kpi .kl{font-family:'Nunito';font-weight:700;font-size:7.2pt;line-height:1.25;margin-top:1.4mm;color:var(--ink);}
"""

def tick3():
    return '<td class="tick"><span class="cbx"></span><span class="cbx"></span><span class="cbx"></span></td>'

def sheet(rows, first_col="Co sprawdzasz"):
    out = ('<table class="sheet"><thead><tr><th class="q">%s</th>'
           '<th style="width:26%%;text-align:center;">TAK · CZĘŚCIOWO · NIE</th>'
           '<th style="width:22%%;">Uwagi / co poprawić</th></tr></thead><tbody>' % first_col)
    for r in rows:
        out += '<tr><td class="q">%s</td>%s<td class="note"></td></tr>' % (r, tick3())
    return out + "</tbody></table>"

# ---------- CZĘŚĆ IV — MONITORING ----------
P("Monitoring sali — po co i jak często", "purple", lambda n, t:
  head("MONITORING SALI", "purple", "Sala nie jest projektem — jest procesem",
       "Monitoring to nie kontrola nauczyciela. To sprawdzenie, czy przestrzeń nadal robi to, "
       "do czego została zaprojektowana.") +
  '<div class="two-col"><div class="col-text">'
  '<div class="body-text"><p>Sala zmienia się sama: przybywa pudełek, dywan wędruje, stolik zasłania '
  'przejście, strefa wyciszenia zamienia się w magazyn poduszek. <strong>Bez regularnego przeglądu '
  'wraca układ sprzed zmiany</strong> — zwykle w ciągu jednego semestru.</p></div>' +
  info_box("Rytm monitoringu", [
      "<b>Codziennie (2 minuty)</b> — czy przejścia są wolne, czy strefa ciszy jest dostępna",
      "<b>Co miesiąc (15 minut)</b> — Arkusz A: pięć stref",
      "<b>Raz na semestr (45 minut)</b> — Arkusz B: dostępność i trzy poziomy",
      "<b>Po każdej zmianie w grupie</b> — nowe dziecko, nowe orzeczenie, nowy sprzęt"], "purple") +
  info_box("Kto monitoruje", [
      "Nauczyciele obu zmian pracujący w tej sali",
      "Specjalista — psycholog, pedagog specjalny lub logopeda",
      "Dyrektor — w ramach nadzoru pedagogicznego",
      "Dzieci — ich zachowanie jest najlepszym wskaźnikiem"], "mint") +
  '</div><div style="flex:.9;">' +
  wide_photo("n10", "Nauczycielka obserwuje i notuje funkcjonowanie dzieci w strefach",
             "Monitoring to obserwacja dzieci w strefach — nie przegląd mebli", "height:62mm;") +
  '<div style="height:3mm;"></div>' +
  warn("monitoring robiony po godzinach, w pustej sali. Sala pusta zawsze wygląda dobrze — "
       "sprawdzaj ją w środku dnia, gdy pracuje w niej cała grupa.") +
  '</div></div>')

P("Arkusz A — monitoring pięciu stref", "mint", lambda n, t:
  head("ARKUSZ MONITORINGU · A", "mint", "Pięć stref — przegląd miesięczny",
       "Wypełniaj w trakcie dnia, obserwując dzieci. Kopiuj arkusz dla każdej sali.") +
  '<div class="form-row"><span class="fl">Sala / grupa:</span><span class="fv"></span>'
  '<span class="fl">Data:</span><span class="fv" style="max-width:30mm;"></span>'
  '<span class="fl">Osoba:</span><span class="fv" style="max-width:40mm;"></span></div>' +
  sheet([
      "Wszystkie pięć stref stałych jest wyodrębnionych i widocznych dla dziecka",
      "Dziecko sięga po materiały samodzielnie, bez proszenia dorosłego",
      "Strefa odpoczywania jest dostępna i faktycznie używana przez dzieci",
      "Granice stref są czytelne (dywan, kolor, regał) — dzieci ich przestrzegają",
      "Pojemniki mają oznaczenie obrazkowe, a nie tylko napis",
      "W każdej strefie można pracować przy stole i na podłodze",
      "Strefy czasowe są rozkładane i składane zgodnie z planem zajęć",
      "Prace w toku mają swoje miejsce — nie są sprzątane przedwcześnie",
      "Sala ma połączenie z przestrzenią na zewnątrz (ogród, taras)",
      "Ekrany są poza strefami swobodnej zabawy",
      "Meble są stabilne, a droga ewakuacyjna wolna",
  ]) +
  '<div class="sheet-legend"><span><b>TAK</b> — działa bez zastrzeżeń</span>'
  '<span><b>CZĘŚCIOWO</b> — działa, ale nie dla wszystkich dzieci</span>'
  '<span><b>NIE</b> — do zmiany w tym miesiącu</span></div>' +
  '<p class="mini-head">Trzy zmiany, które wprowadzamy w tym miesiącu</p>' +
  "".join('<div class="form-row"><span class="fl">%d.</span><span class="fv"></span>'
          '<span class="fl">kto:</span><span class="fv" style="max-width:34mm;"></span>'
          '<span class="fl">termin:</span><span class="fv" style="max-width:26mm;"></span></div>' % i
          for i in (1, 2, 3)))

P("Arkusz B — monitoring dostępności i trzech poziomów", "purple", lambda n, t:
  head("ARKUSZ MONITORINGU · B", "purple", "Dostępność i trzy poziomy wsparcia",
       "Przegląd semestralny — wypełniany razem ze specjalistą.") +
  '<div class="form-row"><span class="fl">Sala / grupa:</span><span class="fv"></span>'
  '<span class="fl">Data:</span><span class="fv" style="max-width:30mm;"></span>'
  '<span class="fl">Zespół:</span><span class="fv" style="max-width:40mm;"></span></div>' +
  sheet([
      "<b>P1</b> · Główne ciągi komunikacyjne mają min. 90 cm i są wolne przez cały dzień",
      "<b>P1</b> · Każda strefa jest dostępna z pozycji siedzącej i z wózka",
      "<b>P1</b> · Informacja w sali jest podana w obrazku i w słowie",
      "<b>P1</b> · Plan dnia w piktogramach wisi na wysokości oczu dziecka",
      "<b>P1</b> · Poziom hałasu i światła da się zmniejszyć w części sali",
      "<b>P2</b> · Dzieci z rozpoznaną trudnością mają przypisane konkretne rozwiązanie w sali",
      "<b>P2</b> · Pomoce poziomu 2 są dostępne dla dziecka bez proszenia dorosłego",
      "<b>P2</b> · Skuteczność dostosowań jest zapisywana i weryfikowana",
      "<b>P3</b> · Dostosowania z IPET mają odzwierciedlenie w układzie tej sali",
      "<b>P3</b> · Sprzęt specjalistyczny ma stałe miejsce i jest używany codziennie",
      "<b>P3</b> · Dziecko z orzeczeniem uczestniczy w zajęciach grupy, a nie obok grupy",
      "<b>P3</b> · Wnioski z ewaluacji IPET wróciły do organizacji przestrzeni",
  ]) +
  '<div class="sheet-legend"><span><b>P1</b> — projektowanie uniwersalne</span>'
  '<span><b>P2</b> — dostosowania ukierunkowane</span><span><b>P3</b> — wsparcie indywidualne</span>'
  '<span>Każde <b>NIE</b> przenosisz do planu naprawczego</span></div>')

P("Karta obserwacji dziecka w przestrzeni", "pink", lambda n, t:
  head("NARZĘDZIE", "pink", "Karta obserwacji dziecka w przestrzeni sali",
       "Uzupełnia WOPFU o to, czego nie widać w gabinecie: jak dziecko korzysta z konkretnej sali.") +
  '<div class="form-row"><span class="fl">Dziecko:</span><span class="fv"></span>'
  '<span class="fl">Grupa:</span><span class="fv" style="max-width:26mm;"></span>'
  '<span class="fl">Data:</span><span class="fv" style="max-width:26mm;"></span></div>' +
  '<div class="obs-grid">' +
  "".join('<div class="obs-card"><p class="oc-t">%s</p>%s</div>' % (t_, '<div class="oc-l"></div>' * k)
          for t_, k in [
              ("Z których stref korzysta samodzielnie?", 2),
              ("Do których stref nie wchodzi wcale?", 2),
              ("Co robi, gdy w sali jest głośno lub tłoczno?", 2),
              ("Jak komunikuje potrzebę — słowem, gestem, obrazkiem?", 2),
              ("Ile trwa aktywność, zanim dziecko ją przerywa?", 2),
              ("Które dostosowanie zadziałało w ostatnim miesiącu?", 2),
              ("Które dostosowanie nie zadziałało i dlaczego?", 2),
              ("Wniosek: co zmieniamy w sali w najbliższym miesiącu?", 2),
          ]) + '</div>' +
  '<div class="legal-note" style="margin-top:auto;">Kartę wypełnia nauczyciel prowadzący grupę, '
  'najlepiej po trzech obserwacjach w różnych porach dnia. Wnioski przenosi się do WOPFU, IPET '
  'lub do planu pomocy psychologiczno-pedagogicznej.</div>')

P("Wskaźniki — kiedy sala naprawdę działa", "mint", lambda n, t:
  head("WSKAŹNIKI", "mint", "Po czym poznasz, że sala działa",
       "Nie po tym, jak wygląda na zdjęciu — po tym, co robią w niej dzieci.") +
  '<div class="kpi-row">'
  '<div class="kpi sf-l1"><div class="kv tx-l1">5 / 5</div><div class="kl">stref stałych '
  'wyodrębnionych i używanych</div></div>'
  '<div class="kpi sf-l2"><div class="kv tx-l2">0</div><div class="kl">dzieci, które muszą prosić '
  'dorosłego o podanie materiału</div></div>'
  '<div class="kpi sf-l3"><div class="kv tx-l3">90 cm</div><div class="kl">minimalna szerokość '
  'wolnych ciągów komunikacyjnych</div></div>'
  '<div class="kpi sf-l1"><div class="kv tx-l1">100%</div><div class="kl">dzieci mających dostęp '
  'do strefy wyciszenia</div></div></div>' +
  '<div class="two-col"><div class="col-text">' +
  info_box("Wskaźniki obserwowalne — zaznacz, co widzisz", [
      "Dzieci wchodzą do stref bez pytania o zgodę",
      "Dziecko z orzeczeniem bawi się <b>razem</b> z grupą, nie tylko obok",
      "Strefa wyciszenia jest używana także przez dzieci bez diagnozy",
      "Dzieci odkładają materiały na miejsce, bo wiedzą, gdzie ono jest",
      "Konflikty o miejsce i materiały są rzadsze niż na początku roku",
      "Nauczyciel rzadziej powtarza te same polecenia organizacyjne"], "mint") +
  '</div><div class="col-text">' +
  info_box("Sygnały ostrzegawcze — czas na zmianę", [
      "Jedna strefa jest zawsze pusta — sprawdź dostęp, nie dzieci",
      "Do jednej strefy ustawia się kolejka i wybuchają konflikty",
      "Dziecko krąży po sali i nie zatrzymuje się nigdzie",
      "Strefa wyciszenia służy jako miejsce odsyłania „na uspokojenie”",
      "Sprzęt specjalistyczny leży nieużywany dłużej niż dwa tygodnie",
      "Materiały wracają za wysoko — bo tak wygodniej dorosłym"], "pink") +
  '</div></div>' +
  '<div class="legal-note">Jeden wskaźnik nie oznacza problemu. Trzy sygnały ostrzegawcze naraz '
  'oznaczają, że sala wróciła do układu sprzed zmiany — i warto zacząć od Arkusza A.</div>')

P("Plan naprawczy — od wniosku do zmiany", "purple", lambda n, t:
  head("PLAN NAPRAWCZY", "purple", "Od wniosku z monitoringu do zmiany w sali",
       "Każde „NIE” z arkusza zamienia się w jeden wiersz tej tabeli.") +
  '<table class="sheet"><thead><tr><th style="width:26%">Co nie działa</th>'
  '<th style="width:30%">Co zmieniamy</th><th style="width:12%">Poziom</th>'
  '<th style="width:16%">Kto</th><th>Termin</th></tr></thead><tbody>' +
  ('<tr><td>Przykład: strefa wyciszenia zastawiona pudełkami</td>'
   '<td>Przenosimy magazyn do szafy, wracają pufy i kołdra</td>'
   '<td>P1</td><td>Zespół grupy</td><td>do 15.09</td></tr>') +
  "".join('<tr><td style="height:9mm;"></td><td></td><td></td><td></td><td></td></tr>' for _ in range(7)) +
  '</tbody></table>' +
  '<div class="two-col" style="margin-top:3mm;"><div class="col-text">' +
  info_box("Zasady dobrego planu naprawczego", [
      "Maksymalnie <b>trzy zmiany naraz</b> — inaczej nie wiadomo, co zadziałało",
      "Każda zmiana ma jednego właściciela i jeden termin",
      "Najpierw zmiany bezkosztowe, potem zakupy",
      "Efekt sprawdzasz po czterech tygodniach, tym samym arkuszem"], "purple") +
  '</div><div class="col-text">' +
  info_box("Co zrobić z wnioskami", [
      "Wnioski z Arkusza A → plan pracy zespołu na kolejny miesiąc",
      "Wnioski z Arkusza B → ewaluacja IPET i plan pomocy p-p",
      "Wnioski powtarzalne → wniosek do dyrektora o zakup lub remont",
      "Wnioski dotyczące budynku → plan zapewnienia dostępności placówki"], "mint") +
  '</div></div>')

P("Naszkicuj plan swojej sali", "purple", lambda n, t:
  head("ZAPROJEKTUJ SWOJĄ SALĘ", "purple", "Naszkicuj plan swojej sali",
       "Zaznacz, gdzie w Twojej sali znajdzie się każda strefa — i którędy przejedzie wózek. "
       "Poniżej przykładowy plan jako inspiracja.") +
  '<div style="display:flex;gap:6mm;margin-bottom:3mm;flex-wrap:wrap;">' +
  "".join('<div style="display:flex;align-items:center;gap:2mm;">'
          '<span style="width:4mm;height:4mm;border-radius:50%%;background:var(--%s-deep);display:inline-block;"></span>'
          '<span style="font-family:Nunito;font-weight:700;font-size:8.6pt;">%s</span></div>' % (c, l)
          for c, l in [("purple", "1. Czytelnictwa"), ("mint", "2. Konstruowania"), ("pink", "3. Sztuki"),
                       ("purple", "4. Odpoczywania"), ("mint", "5. Przyrody"),
                       ("pink", "Ciągi komunikacyjne 90 cm")]) + '</div>' +
  '<div style="border-radius:5mm;overflow:hidden;border:1.6pt solid var(--purple-deep);'
  'box-shadow:0 3px 12px rgba(107,75,161,.15);margin-bottom:4mm;">'
  '<img src="%s" alt="Przykładowy plan sali z oznaczonymi strefami" '
  'style="width:100%%;height:auto;display:block;"></div>'
  '<p class="mini-head">Twój szkic — zaznacz strefy i ciągi komunikacyjne</p>'
  '<div style="flex:1;min-height:0;border:1.4pt dashed var(--purple-deep);border-radius:5mm;'
  'background:repeating-linear-gradient(0deg,transparent,transparent 7.4mm,#EFE9F7 7.4mm,#EFE9F7 7.5mm),'
  'repeating-linear-gradient(90deg,transparent,transparent 7.4mm,#EFE9F7 7.4mm,#EFE9F7 7.5mm);"></div>'
  % img("17"))

P("Plan wdrożenia krok po kroku", "mint", lambda n, t:
  head("WDROŻENIE", "mint", "Od kącika do strefy — plan wdrożenia",
       "Przykładowy harmonogram przygotowania sali do 1 września 2026 r. — dopasuj do własnego kalendarza.") +
  '<table class="plan" style="font-size:8.4pt;"><thead><tr><th>Krok</th><th>Co zrobić</th>'
  '<th>Szczegóły</th><th>Termin</th></tr></thead><tbody>' +
  "".join('<tr><td style="font-family:Quicksand;font-weight:700;color:var(--purple-deep);">%s</td>'
          '<td><strong>%s</strong></td><td>%s</td><td>%s</td></tr>' % r for r in [
      ("1", "Audyt obecnej sali", "Wypełnij Arkusz A i Arkusz B — zobacz, od czego zaczynasz", "do 2 tygodni"),
      ("2", "Konsultacja z zespołem i rodzicami", "Omówcie zmiany, zbierzcie pomysły i materiały", "2–3 tygodnie"),
      ("3", "Poziom 1 — projektowanie uniwersalne", "Przejścia, wysokości, oznaczenia obrazkowe, plan dnia", "1 miesiąc"),
      ("4", "Wyznaczenie 5 stref stałych", "Zaplanuj miejsce każdej strefy zgodnie z metrażem", "1 miesiąc"),
      ("5", "Priorytet: strefa odpoczywania", "Nowy, obowiązkowy element — zrób go jako pierwszy", "w pierwszej kolejności"),
      ("6", "Poziom 2 — dostosowania ukierunkowane", "Dopasuj rozwiązania do dzieci z rozpoznaną trudnością", "na bieżąco"),
      ("7", "Poziom 3 — realizacja zapisów IPET", "Sprawdź, czy każdy zapis ma odzwierciedlenie w sali", "wrzesień–październik"),
      ("8", "Pierwszy monitoring", "Arkusz A po miesiącu pracy w nowym układzie", "po 4 tygodniach"),
      ("9", "Plan naprawczy i korekty", "Maksymalnie trzy zmiany naraz", "stale"),
  ]) + '</tbody></table>' +
  info_box("Jeśli nie zdążysz ze wszystkim do września", [
      "Zrób najpierw <b>strefę odpoczywania</b> — jest nowa i obowiązkowa",
      "Potem zwolnij ciągi komunikacyjne i obniż półki — to zero złotych",
      "Następnie oznacz pojemniki obrazkami — to jedno popołudnie pracy zespołu",
      "Zakupy sprzętu specjalistycznego planuj dopiero po pierwszym monitoringu"], "mint") +
  '<div class="legal-note" style="margin-top:auto;">Harmonogram jest przykładowy — dostosuj go '
  'do wielkości placówki, liczby sal i dostępnego budżetu. Kroki 3 i 5 są najważniejsze: '
  'dają największą zmianę przy najmniejszym koszcie.</div>')

# ---------- STRONA KOŃCOWA ----------
def p_final(n, total):
    return ('<div class="deco deco-mint deco-tr"></div><div class="deco deco-mint deco-bl"></div><div>'
            '<span class="eyebrow" style="background:rgba(255,255,255,.2);display:inline-block;'
            'padding:2mm 5mm;border-radius:20mm;font-family:Nunito;font-weight:800;letter-spacing:.14em;'
            'font-size:8.5pt;">PODSUMOWANIE</span>'
            '<h2 style="font-family:Quicksand;font-weight:700;font-size:23pt;margin:4mm 0 3mm;">'
            'Sala, w której każde dziecko decyduje</h2>'
            '<p style="font-family:Nunito;font-weight:600;font-size:9.6pt;max-width:165mm;line-height:1.45;">'
            'Pięć stref daje dziecku wybór, jak spędzić swój dzień. Trzy poziomy wsparcia sprawiają, '
            'że z tego wyboru może skorzystać <b>każde</b> dziecko — także to, które jeździ na wózku, '
            'nie mówi, nie słyszy albo nie zna jeszcze języka polskiego. Monitoring pilnuje, '
            'żeby po kilku miesiącach sala nie wróciła do starego układu.</p></div>'
            '<div style="flex:1;min-height:0;border-radius:5mm;overflow:hidden;'
            'border:1.6pt solid rgba(255,255,255,.85);margin:4mm 0;display:flex;align-items:center;'
            'justify-content:center;background:rgba(255,255,255,.08);">'
            '<img src="%s" alt="Sala przedszkolna ze wszystkimi pięcioma strefami" '
            'style="width:100%%;height:100%%;object-fit:cover;object-position:center 60%%;display:block;">'
            '</div>'
            '<div style="font-family:Nunito;font-size:8.8pt;line-height:1.5;background:rgba(255,255,255,.16);'
            'border-radius:4mm;padding:3mm 4mm;margin-bottom:3mm;">'
            '<b>Jak korzystać z przewodnika:</b> strony 04–19 — organizacja sali według nowej podstawy · '
            'strony 20–29 — trzy poziomy wsparcia i projektowanie uniwersalne · strony 30–40 — dostosowania '
            'według deficytów · strony 41–48 — monitoring sali, arkusze i plan wdrożenia.</div>'
            '<div style="font-family:Nunito;font-size:9pt;line-height:1.6;display:flex;gap:6mm;'
            'flex-wrap:wrap;margin-bottom:3mm;">'
            '<span>🏫 Pomorskie Centrum Terapii Pedagogicznej w Koszalinie</span>'
            '<span>📞 94&nbsp;340&nbsp;12&nbsp;56</span>'
            '<span>✉️ kontakt@pctp-koszalin.pl</span></div>'
            '<div class="cov-footer"><span class="pill">Podstawa programowa 2026 · dostępność · '
            'monitoring sali</span><span class="pill">Przewodnik 2026 · %d stron</span></div>' % (img("18"), total))

# ---------- SKŁADANIE ----------
def build():
    total = 3 + len(PAGES) + 1
    out = []
    out.append(page(1, total, p_cover(1, total), cls="cover", panel_style="", panel_cls="panel")
               .replace(footer(1, total), ""))
    out.append(page(2, total, toc_page(1, 2, total), cls="toc", panel_style="padding-top:6mm;"))
    out.append(page(3, total, toc_page(2, 3, total), cls="toc", panel_style="padding-top:6mm;"))
    for i, (_, _, fn) in enumerate(PAGES):
        num = 4 + i
        out.append(page(num, total, fn(num, total)))
    last = total
    out.append(page(last, total, p_final(last, total),
                    panel_style="background:linear-gradient(160deg,var(--pink-deep) 0%,#C25C97 30%,"
                                "var(--purple-deep) 85%);color:#fff;justify-content:space-between;",
                    panel_cls="panel cover").replace(footer(last, total), ""))
    html = ("<!DOCTYPE html>\n<html lang=\"pl\">\n<head>\n<meta charset=\"UTF-8\">\n"
            "<title>Sala, która uczy każde dziecko — nowa podstawa programowa i dostępność</title>\n"
            "<style>" + BASE_CSS + EXTRA_CSS + EXTRA_CSS2 + "</style>\n</head>\n<body>\n<div class=\"doc\">\n"
            + "".join(out) + "</div>\n</body>\n</html>\n")
    return html, total

# ---------- gotowe zapisy do dokumentacji ----------
DOCS = {
 "Spektrum autyzmu": ("Dostosowanie warunków: stałe, oznaczone miejsce pracy w sali, plan dnia w formie "
   "wizualnej, uprzedzanie o zmianach aktywności, stały dostęp do strefy wyciszenia bez konieczności "
   "uzyskania zgody nauczyciela, słuchawki wygłuszające dostępne dla dziecka przez cały dzień."),
 "ADHD i trudności z koncentracją": ("Dostosowanie warunków: miejsce pracy poza głównym ciągiem "
   "komunikacyjnym, ograniczenie liczby materiałów dostępnych jednocześnie, zadania dzielone na etapy "
   "z sygnałem zakończenia, zaplanowane przerwy ruchowe, umówiony sygnał wyjścia do strefy ruchu."),
 "Niepełnosprawność intelektualna": ("Dostosowanie warunków: oznaczenie wszystkich pojemników i stref "
   "symbolem obrazkowym, polecenia jednoetapowe wspierane obrazem i pokazem, instrukcje obrazkowe "
   "przy strefach, wydłużony czas na wykonanie zadania, ocena postępu w odniesieniu do dziecka."),
 "Niepełnosprawność ruchowa": ("Dostosowanie warunków: ciągi komunikacyjne o szerokości min. 90 cm "
   "(min. 120 cm w strefach kluczowych), materiały na wysokości 40–120 cm, blat z wolną przestrzenią "
   "pod spodem, mata antypoślizgowa, przybory z pogrubionym uchwytem, krzesło z podparciem."),
 "Dziecko niesłyszące i słabosłyszące": ("Dostosowanie warunków: ograniczenie pogłosu w sali (dywan, "
   "panele, nakładki na meble), stałe miejsce w polu widzenia nauczyciela i przy dobrym oświetleniu "
   "twarzy, sygnały wizualne równolegle do dźwiękowych, wsparcie obrazkowe poleceń, obsługa systemu FM."),
 "Dziecko niewidome i słabowidzące": ("Dostosowanie warunków: niezmienny układ sali i wolne ciągi "
   "komunikacyjne, kontrastowe oznaczenie krawędzi i drzwi, oznaczenia dotykowe stref, materiały "
   "powiększone i wypukłe, punktowe doświetlenie stanowiska, werbalizowanie czynności przez nauczyciela."),
 "Zaburzenia przetwarzania sensorycznego": ("Dostosowanie warunków: dostęp do strefy wyciszenia "
   "i do strefy ruchu w ciągu całego dnia, możliwość regulacji natężenia światła i dźwięku, pomoce "
   "proprioceptywne (poduszka sensoryczna, kołdra obciążeniowa), uprzedzanie o zajęciach o dużym natężeniu bodźców."),
 "Zaburzenia mowy i komunikacji": ("Dostosowanie warunków: dostęp do komunikacji wspomagającej (tablica "
   "wyboru, książka komunikacyjna lub komunikator) we wszystkich strefach sali, akceptowanie odpowiedzi "
   "gestem i wskazaniem, wydłużony czas na odpowiedź, symbole AAC znane całej grupie."),
 "Dzieci z chorobami przewlekłymi": ("Dostosowanie warunków: stałe miejsce odpoczynku w sali, "
   "całodzienny dostęp do wody, procedura postępowania w sytuacji objawów dostępna dla całego zespołu, "
   "wyznaczone i zabezpieczone miejsce przechowywania leków i sprzętu, modyfikacja intensywności zajęć ruchowych."),
 "Dzieci nieznające języka polskiego": ("Dostosowanie warunków: oznaczenia obrazkowe stref i materiałów, "
   "plan dnia w piktogramach, polecenia wspierane pokazem, słownik obrazkowy, akceptacja okresu ciszy, "
   "udział w zabawach niewymagających kompetencji językowych."),
}

def doc_box(title):
    txt = DOCS.get(title)
    if not txt:
        return ""
    return ('<div class="info-box box-purple" style="margin-top:auto;margin-bottom:0;">'
            '<p class="ib-title">Gotowy zapis do dokumentacji — WOPFU / IPET / plan pomocy p-p</p>'
            '<p style="font-style:italic;">„%s”</p></div>' % txt)

if __name__ == "__main__":
    html, total = build()
    outp = os.path.join(HERE, "sala_ktora_uczy_kazde_dziecko.html")
    open(outp, "w", encoding="utf-8").write(html)
    print("stron:", total, "· rozmiar:", round(len(html.encode()) / 1024 / 1024, 2), "MB")

