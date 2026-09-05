# -*- coding: utf-8 -*-
"""Wspólna oprawa graficzna druków — marka PCTP / EduPlaner 2026.

Fiolet #2D1B69 + pomarańcz #E8450A, arkusz A4, stopka z autorką i numeracją.
Kroje pisma: Mulish (nagłówki i tekst) z zapasem systemowym — druk otwiera się
z dysku, bez serwera i bez pobierania z sieci.
"""

STYL = """
:root{
  --purple:#2D1B69; --purple-soft:#efeaf9; --purple-line:#d9d0f0; --purple-mid:#5a4a94;
  --orange:#E8450A; --orange-soft:#fdece4; --orange-line:#f3cdbd;
  --ink:#2b2733; --muted:#6f6a7d; --paper:#fff; --hair:#e4e1ec; --zebra:#faf7f2;
  --lvl1:#1f8a5b; --lvl1-bg:#eaf6f0; --lvl2:#c8811b; --lvl2-bg:#fbf3e3; --lvl3:#c0392b; --lvl3-bg:#fbebe9;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:#e9e7ef;color:var(--ink);
     font-family:'Mulish','Segoe UI',Candara,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.sheet{width:210mm;min-height:297mm;margin:12px auto;background:var(--paper);
       padding:9mm 11mm 7mm;box-shadow:0 6px 30px rgba(45,27,105,.16);
       position:relative;display:flex;flex-direction:column}
.head{display:flex;align-items:center;justify-content:space-between;gap:14px}
.brand{display:flex;align-items:center;gap:11px}
.logo{width:38px;height:38px;border-radius:50%;background:var(--purple);color:#fff;display:flex;
      align-items:center;justify-content:center;font-size:8.5px;font-weight:700;letter-spacing:.4px;
      border:2px solid #cfc4ea;flex:0 0 auto}
.brand h1{font-size:16px;margin:0;color:var(--purple);letter-spacing:.3px;line-height:1.1}
.brand .sub{font-size:8.5px;color:var(--muted);margin-top:2px;letter-spacing:.5px;
            text-transform:uppercase;font-weight:700}
.badge{text-align:right}
.pill{display:inline-block;background:var(--orange);color:#fff;font-size:10px;font-weight:700;
      padding:5px 12px;border-radius:20px}
.pill.p{background:var(--purple)}
.badge .tag{font-size:8px;color:var(--muted);letter-spacing:.9px;margin-top:4px;text-transform:uppercase}
.rule{height:3px;border-radius:3px;margin:8px 0 0;
      background:linear-gradient(90deg,var(--purple) 0%,var(--purple) 55%,var(--orange) 55%,var(--orange) 100%)}
.student{display:flex;gap:9px;margin-top:9px}
.field{flex:1;background:var(--purple-soft);border:1px solid var(--purple-line);border-radius:8px;
       padding:6px 11px;display:flex;align-items:baseline;gap:8px}
.field .lab{font-size:7.5px;font-weight:700;letter-spacing:.7px;color:var(--purple);text-transform:uppercase}
.field .val{font-size:11.5px;font-weight:700}
.field .blank{flex:1;border-bottom:1.5px dotted #b7add6;height:13px}
.sec{display:flex;align-items:center;gap:9px;margin:13px 0 3px}
.sec .n{min-width:22px;padding:0 6px;height:22px;border-radius:6px;background:var(--orange);color:#fff;
        display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px}
.sec .n.p{background:var(--purple)}
.sec h2{font-size:12.5px;letter-spacing:.8px;color:var(--purple);margin:0;text-transform:uppercase}
.sec .line{flex:1;height:1px;background:var(--hair)}
.note{font-size:8.5px;color:var(--muted);margin:2px 0 6px 31px;line-height:1.45}
p{line-height:1.5}
.tbl{width:100%;border-collapse:collapse;font-size:9px;margin-top:5px}
.tbl th{background:var(--purple);color:#fff;font-size:7.5px;letter-spacing:.6px;text-transform:uppercase;
        padding:5px 6px;text-align:left;font-weight:700}
.tbl td{border-bottom:1px solid var(--hair);padding:5px 6px;vertical-align:top;line-height:1.42}
.tbl tr:nth-child(even) td{background:var(--zebra)}
.lvl{display:inline-block;font-size:7.5px;font-weight:700;padding:2px 7px;border-radius:10px;white-space:nowrap}
.lvl.III{background:var(--lvl3-bg);color:var(--lvl3)}
.lvl.II{background:var(--lvl2-bg);color:var(--lvl2)}
.lvl.I{background:var(--lvl1-bg);color:var(--lvl1)}
.box{background:var(--purple-soft);border:1px solid var(--purple-line);border-radius:9px;
     padding:8px 11px;font-size:9px;line-height:1.5;margin-top:6px}
.box.o{background:var(--orange-soft);border-color:var(--orange-line)}
.box b{color:var(--purple)}
.blk{font-size:9px;font-weight:700;letter-spacing:.6px;color:var(--purple);text-transform:uppercase;
     margin:9px 0 3px;display:flex;align-items:center;gap:6px}
.blk::before{content:"";width:9px;height:9px;border-radius:2px;background:var(--orange)}
.dziecko{background:#fff8f4;border-left:3px solid var(--orange);padding:5px 9px;font-size:9.5px;
         border-radius:0 6px 6px 0;margin:3px 0}
.doroslego{background:#f6f4fb;border-left:3px solid var(--purple-mid);padding:5px 9px;font-size:9px;
           border-radius:0 6px 6px 0;margin:3px 0}
.audio{font-size:8px;color:var(--muted);font-family:ui-monospace,Consolas,monospace}
.foot{margin-top:auto;padding-top:7px;border-top:1px solid var(--hair);display:flex;
      justify-content:space-between;font-size:8px;color:var(--muted);letter-spacing:.3px}
.edit{border:1px dashed var(--purple-line);border-radius:6px;padding:5px 8px;min-height:20px;
      font-size:9px;color:var(--muted);background:#fdfdff}
.edit:focus{outline:2px solid var(--orange);color:var(--ink)}
.filtry{position:sticky;top:0;z-index:9;background:var(--purple);color:#fff;padding:8px 14px;
        display:flex;gap:10px;align-items:center;flex-wrap:wrap;font-size:11px}
.filtry select{font:inherit;padding:3px 6px;border-radius:6px;border:0}
.filtry .licz{margin-left:auto;font-weight:700}
@media print{
  body{background:#fff}
  .sheet{box-shadow:none;margin:0;page-break-after:always}
  .filtry{display:none}
  @page{size:A4;margin:0}
}
"""


def naglowek(podtytul: str, plakietka: str, tag: str,
             uczen: str = "", grupa: str = "") -> str:
    pola = (
        f'<div class="field"><span class="lab">Dotyczy dziecka</span>'
        f'{f"<span class=val>{uczen}</span>" if uczen else "<span class=blank></span>"}</div>'
        f'<div class="field"><span class="lab">Grupa</span>'
        f'{f"<span class=val>{grupa}</span>" if grupa else "<span class=blank></span>"}</div>'
        f'<div class="field"><span class="lab">Data</span><span class="blank"></span>'
        f'<span class="val">r.</span></div>'
    )
    return f"""<div class="head">
  <div class="brand"><div class="logo">PCTP</div>
    <div><h1>EduPlaner 2026</h1><div class="sub">{podtytul}</div></div></div>
  <div class="badge"><span class="pill">{plakietka}</span><div class="tag">{tag}</div></div>
</div>
<div class="rule"></div>
<div class="student">{pola}</div>"""


def stopka(numer: int, ile: int, nazwa_druku: str) -> str:
    return (f'<div class="foot"><span>EduPlaner 2026 · PCTP · pedagog specjalny '
            f'<b>mgr Mirosława Ewa Jurczyszyn</b></span>'
            f'<span>Strona {numer} z {ile} · {nazwa_druku}</span></div>')


def dokument(tytul: str, arkusze: list[str], pasek: str = "") -> str:
    return (f'<!DOCTYPE html>\n<html lang="pl">\n<head>\n<meta charset="UTF-8">\n'
            f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            f'<title>{tytul}</title>\n<style>{STYL}</style>\n</head>\n<body>\n'
            f'{pasek}\n' + "\n".join(arkusze) + "\n</body>\n</html>\n")
