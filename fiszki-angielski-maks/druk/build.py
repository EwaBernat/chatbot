#!/usr/bin/env python3
"""Sklada arkusze A4 z fiszkami (8 na stronie, dwustronnie) i zapisuje HTML do druku."""
import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = open(os.path.join(HERE, "fonts.css"), encoding="utf-8").read()

# kind: powitanie | pytanie | odpowiedz | legenda
CARDS = [
    dict(kind="powitanie", pl="Dzień dobry", sub="rano, do ok. 12:00",
         en="Good morning.", say="gud *MOR*-ning", ipa="/ɡʊd ˈmɔːnɪŋ/"),
    dict(kind="powitanie", pl="Dzień dobry", sub="po południu, 12:00–18:00",
         en="Good afternoon.", say="gud af-te-*NUUN*", ipa="/ˌɡʊd ɑːftəˈnuːn/"),
    dict(kind="powitanie", pl="Dobry wieczór", sub="wieczorem, od ok. 18:00",
         en="Good evening.", say="gud *IIW*-ning", ipa="/ɡʊd ˈiːvnɪŋ/"),
    dict(kind="pytanie", pl="Jak masz na imię?", sub="pytanie o imię",
         en="What's your name?", say="łots jor *NEJM*?", ipa="/wɒts jɔː ˈneɪm/"),
    dict(kind="pytanie", pl="Jak się nazywasz?", sub="pytanie o nazwisko",
         en="What's your surname?", say="łots jor *SER*-nejm?", ipa="/wɒts jɔː ˈsɜːneɪm/"),
    dict(kind="pytanie", pl="Skąd jesteś?", sub="pytanie o kraj",
         en="Where are you from?", say="łer ar ju *FROM*?", ipa="/weər ə juː ˈfrɒm/"),
    dict(kind="pytanie", pl="Powiedz coś o sobie.", sub="prośba o kilka zdań",
         en="Tell me something about yourself.", say="tel mi *SAM*-tyng e-*BAŁT* jor-*SELF*",
         ipa="/tel miː ˈsʌmθɪŋ əˈbaʊt jɔːˈself/"),
    dict(kind="pytanie", pl="Gdzie mieszkasz?", sub="pytanie o miasto",
         en="Where do you live?", say="łer du ju *LIW*?", ipa="/weə duː juː ˈlɪv/"),
    dict(kind="pytanie", pl="Co teraz robisz w życiu?", sub="praca, szkoła, plany",
         en="What do you do now?", say="łot du ju *DU* nał?", ipa="/wɒt duː juː ˈduː naʊ/"),
    dict(kind="pytanie", pl="Co lubisz?", sub="zainteresowania",
         en="What do you like?", say="łot du ju *LAJK*?", ipa="/wɒt duː juː ˈlaɪk/"),
    dict(kind="odpowiedz", pl="Mam na imię Maks.", sub="odpowiedź na pytanie 04",
         en="My name is Maks.", say="maj nejm iz *MAKS*", ipa=""),
    dict(kind="odpowiedz", pl="Jestem z Polski.", sub="odpowiedź na pytanie 06",
         en="I'm from Poland.", say="ajm from *POŁ*-lend", ipa=""),
    dict(kind="odpowiedz", pl="Mieszkam w Koszalinie, na północy Polski.", sub="odpowiedź na pytanie 08",
         en="I live in Koszalin, in the north of Poland.",
         say="aj liw in ko-*SZA*-lin, in de *NORS* ow *POŁ*-lend", ipa=""),
    dict(kind="odpowiedz", pl="Jestem uczniem. Uczę się angielskiego.", sub="odpowiedź na pytanie 09",
         en="I'm a student. I'm learning English.",
         say="ajm e *STJU*-dent. ajm *LER*-ning *ING*-lisz", ipa=""),
    dict(kind="odpowiedz", pl="Lubię muzykę, sport i gry komputerowe.", sub="odpowiedź na pytanie 10",
         en="I like music, sport and computer games.",
         say="aj lajk *MJU*-zik, sport end kom-*PJU*-ter gejms", ipa=""),
    dict(kind="legenda",
         front_title="Jak czytać zapis",
         front_rows=[("DUŻE LITERY", "tu pada akcent"),
                     ("ł", "angielskie w — what → łot"),
                     ("ii", "długie i — see → sii"),
                     ("th", "język między zębami")],
         back_title="Które powitanie kiedy",
         back_rows=[("Good morning", "do 12:00"),
                    ("Good afternoon", "12:00–18:00"),
                    ("Good evening", "po 18:00"),
                    ("Hello / Hi", "o każdej porze")]),
]

KIND_LABEL = {"powitanie": "Powitanie", "pytanie": "Pytanie", "odpowiedz": "Odpowiedź", "legenda": "Ściąga"}

COLS, ROWS = 2, 4
PER_SHEET = COLS * ROWS


def size_for(text, steps):
    n = len(text)
    for limit, pt in steps:
        if n <= limit:
            return pt
    return steps[-1][1]


PL_STEPS = [(14, 20), (26, 16), (40, 12.5), (999, 10.5)]
EN_STEPS = [(16, 19), (30, 15), (45, 11.5), (999, 9.5)]
SAY_STEPS = [(24, 9.5), (34, 8.4), (46, 7.4), (999, 6.6)]


def stress(text):
    out = []
    for i, part in enumerate(text.split("*")):
        esc = html.escape(part)
        out.append('<b>%s</b>' % esc if i % 2 else esc)
    return "".join(out)


def head(num, kind, side):
    return ('<div class="ctop"><span class="badge">%s</span>'
            '<span class="kind">%s</span><span class="side">%s</span></div>'
            % (num, html.escape(KIND_LABEL[kind]), side))


def legend_body(title, rows):
    items = "".join(
        '<div class="lg-row"><span class="lg-k">%s</span><span class="lg-v">%s</span></div>'
        % (html.escape(k), html.escape(v)) for k, v in rows)
    return '<div class="cmid legend"><p class="lg-title">%s</p>%s</div>' % (html.escape(title), items)


def render(card, i, side):
    num = "%02d" % (i + 1)
    kind = card["kind"]
    cls = "card %s %s" % (kind, side)
    if kind == "legenda":
        if side == "front":
            body = legend_body(card["front_title"], card["front_rows"])
        else:
            body = legend_body(card["back_title"], card["back_rows"])
        return '<div class="%s">%s%s</div>' % (cls, head(num, kind, "★"), body)

    if side == "front":
        body = ('<div class="cmid">'
                '<p class="pl" style="font-size:%spt">%s</p>'
                '<p class="sub">%s</p></div>'
                % (size_for(card["pl"], PL_STEPS), html.escape(card["pl"]), html.escape(card["sub"])))
        return '<div class="%s">%s%s</div>' % (cls, head(num, kind, "PL"), body)

    ipa = '<p class="ipa">%s</p>' % html.escape(card["ipa"]) if card["ipa"] else ""
    body = ('<div class="cmid">'
            '<p class="en" style="font-size:%spt">%s</p>'
            '<p class="say" style="font-size:%spt">%s</p>%s</div>'
            % (size_for(card["en"], EN_STEPS), html.escape(card["en"]),
               size_for(card["say"].replace("*", ""), SAY_STEPS), stress(card["say"]), ipa))
    return '<div class="%s">%s%s</div>' % (cls, head(num, kind, "EN"), body)


def blank():
    return '<div class="card blank"></div>'


def sheet(cards_idx, side, page_no, pages_total):
    """cards_idx: lista globalnych indeksow (dlugosci PER_SHEET, None = pusto)."""
    order = list(cards_idx)
    if side == "back":                      # lustro kolumn dla druku dwustronnego
        mirrored = []
        for r in range(ROWS):
            row = order[r * COLS:(r + 1) * COLS]
            mirrored.extend(reversed(row))
        order = mirrored
    cells = "".join(blank() if gi is None else render(CARDS[gi], gi, side) for gi in order)
    note = ("PRZÓD — polski" if side == "front" else "TYŁ — angielski (drukuj dwustronnie, obrót wzdłuż dłuższej krawędzi)")
    return ('<section class="sheet"><div class="grid">%s</div>'
            '<div class="foot"><span>Angielski dla Maksia · fiszki do wycięcia</span>'
            '<span>%s · strona %d/%d</span></div></section>' % (cells, note, page_no, pages_total))


def build():
    groups = [list(range(s, min(s + PER_SHEET, len(CARDS))))
              for s in range(0, len(CARDS), PER_SHEET)]
    for g in groups:
        g += [None] * (PER_SHEET - len(g))
    total = len(groups) * 2
    sheets, page = [], 1
    for g in groups:                        # przod, tyl, przod, tyl — gotowe do duplexu
        sheets.append(sheet(g, "front", page, total)); page += 1
        sheets.append(sheet(g, "back", page, total)); page += 1
    return TEMPLATE.replace("/*FONTS*/", FONTS).replace("<!--SHEETS-->", "\n".join(sheets))


TEMPLATE = """<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<title>Fiszki do druku — Angielski dla Maksia</title>
<style>
/*FONTS*/

@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; }
body {
  color: #17233B;
  font-family: "Source Serif 4", Georgia, serif;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}

.sheet {
  width: 210mm; height: 297mm;
  padding: 10mm 10mm 0;
  display: flex; flex-direction: column;
  page-break-after: always; break-after: page;
}
.sheet:last-child { page-break-after: auto; break-after: auto; }

.grid {
  width: 190mm; height: 271mm;
  display: grid;
  grid-template-columns: repeat(2, 95mm);
  grid-template-rows: repeat(4, 67.75mm);
  border-top: .25mm dashed #A9A396;
  border-left: .25mm dashed #A9A396;
}
.card {
  border-right: .25mm dashed #A9A396;
  border-bottom: .25mm dashed #A9A396;
  padding: 5mm 5.5mm 4mm;
  display: flex; flex-direction: column;
  overflow: hidden;
}
.card.blank { background: #fff; }

.ctop {
  display: flex; align-items: center; gap: 2.2mm;
  font-family: "IBM Plex Mono", monospace;
  font-size: 6.2pt; letter-spacing: .12em; text-transform: uppercase;
  color: #8A8FA0;
}
.badge {
  font-weight: 600; font-size: 6.6pt; letter-spacing: .04em;
  border: .3mm solid currentColor; border-radius: 999px;
  padding: .4mm 1.6mm; color: #8A8FA0;
}
.kind { font-weight: 500; }
.side { margin-left: auto; font-weight: 600; color: #B4B8C4; }

.powitanie .badge, .powitanie .kind { color: #1F6F5C; }
.pytanie   .badge, .pytanie .kind   { color: #2B4A8B; }
.odpowiedz .badge, .odpowiedz .kind { color: #A8480F; }
.legenda   .badge, .legenda .kind   { color: #6B7080; }
.powitanie .badge { background: #E4F0EC; border-color: #BFDCD3; }
.pytanie   .badge { background: #E8EDF8; border-color: #C3D0E8; }
.odpowiedz .badge { background: #FAEBE0; border-color: #E8CBB4; }
.legenda   .badge { background: #EDEEF1; border-color: #D3D6DD; }

.cmid { flex: 1; display: flex; flex-direction: column; justify-content: center; gap: 1.6mm; }

.pl {
  margin: 0; font-weight: 600; line-height: 1.16; text-wrap: balance;
}
.sub {
  margin: 0; font-size: 7.8pt; font-style: italic; color: #8A8FA0; line-height: 1.3;
}

.back .cmid { gap: 2mm; }
.en {
  margin: 0; line-height: 1.14; text-wrap: balance;
  font-family: "Bricolage Grotesque", Arial, sans-serif; font-weight: 800;
  letter-spacing: -.01em;
}
.say {
  margin: 0; font-family: "IBM Plex Mono", monospace; font-weight: 500;
  line-height: 1.45; color: #3E4657;
}
.say b { color: #A8480F; font-weight: 600; }
.ipa {
  margin: 0; font-family: "IBM Plex Mono", monospace;
  font-size: 6.2pt; color: #A6AAB6;
}

.legend { justify-content: flex-start; padding-top: 2mm; gap: 1.4mm; }
.lg-title {
  margin: 0 0 1mm; font-family: "Bricolage Grotesque", Arial, sans-serif;
  font-weight: 800; font-size: 11pt; letter-spacing: -.01em;
}
.lg-row { display: flex; gap: 2.5mm; align-items: baseline; }
.lg-k {
  font-family: "IBM Plex Mono", monospace; font-weight: 600; font-size: 7.4pt;
  color: #A8480F; min-width: 21mm;
}
.lg-v { font-size: 7.8pt; color: #3E4657; line-height: 1.3; }

.foot {
  height: 6mm; display: flex; align-items: center; justify-content: space-between;
  font-family: "IBM Plex Mono", monospace;
  font-size: 5.6pt; letter-spacing: .08em; text-transform: uppercase;
  color: #B4B8C4;
}
</style></head><body>
<!--SHEETS-->
</body></html>
"""

if __name__ == "__main__":
    out = os.path.join(HERE, "fiszki-druk.html")
    open(out, "w", encoding="utf-8").write(build())
    print("cards:", len(CARDS), "| sheets:", (len(CARDS) + PER_SHEET - 1) // PER_SHEET * 2)
    print("wrote:", out, round(os.path.getsize(out) / 1048576, 2), "MB")
