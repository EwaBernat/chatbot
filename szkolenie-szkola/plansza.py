# -*- coding: utf-8 -*-
"""Renderuje planszę wstawki w projekcie filmu EduPlaner (1920×1080)."""
import os, sys, json, asyncio
from playwright.async_api import async_playwright

SZABLON = """<!doctype html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1920px;height:1080px;background:#FCFCFA;font-family:'Liberation Sans',Arial,sans-serif;
     position:relative;overflow:hidden}
.gora{position:absolute;top:0;left:0;right:0;height:8px;background:#E8450C}
.modul{position:absolute;top:30px;right:80px;font-size:23px;font-weight:700;color:#968B9F;
       letter-spacing:3.2px;text-transform:uppercase}
.srodek{position:absolute;top:150px;left:130px;right:130px;bottom:190px;display:flex;
        flex-direction:column;align-items:center;justify-content:center}
.kreska{width:110px;height:7px;background:#E34919;margin-bottom:44px;border-radius:3px}
.tytul{font-size:54px;font-weight:700;color:#2D1B69;text-align:center;line-height:1.28;
       max-width:1500px;margin-bottom:38px}
.punkty{display:flex;flex-direction:column;gap:20px;align-items:flex-start;max-width:1360px}
.p{display:flex;gap:20px;align-items:flex-start;font-size:33px;color:#2D1B69;font-weight:600;
   line-height:1.4}
.p b{display:block;width:15px;height:15px;background:#E8450C;border-radius:3px;margin-top:13px;
     flex:0 0 15px}
.napisy{position:absolute;left:388px;width:1148px;top:922px;min-height:104px;background:#FFFDFB;
        border-radius:16px;box-shadow:0 4px 22px rgba(45,27,105,.10);display:flex;align-items:center;
        justify-content:center;padding:16px 34px}
.napisy span{font-size:31px;font-weight:700;color:#2D1B69;text-align:center;line-height:1.34}
.stopka{position:absolute;left:75px;bottom:26px;font-size:21px;color:#C4C9CE}
</style></head><body>
<div class="gora"></div>
<div class="modul">__MODUL__</div>
<div class="srodek"><div class="kreska"></div>
  <div class="tytul">__TYTUL__</div>
  <div class="punkty">__PUNKTY__</div>
</div>
<div class="napisy"><span>__NAPIS__</span></div>
<div class="stopka">EduPlaner 2026 · PCTP · szkolenie rady pedagogicznej</div>
</body></html>"""


async def renderuj(zadania, katalog):
    os.makedirs(katalog, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
        pg = await b.new_page(viewport={'width': 1920, 'height': 1080})
        for z in zadania:
            punkty = ''.join(f'<div class="p"><b></b><div>{t}</div></div>' for t in z['punkty'])
            html = (SZABLON.replace('__MODUL__', z['modul']).replace('__TYTUL__', z['tytul'])
                    .replace('__PUNKTY__', punkty).replace('__NAPIS__', z['napis']))
            await pg.set_content(html)
            await pg.screenshot(path=os.path.join(katalog, z['plik']))
        await b.close()


if __name__ == '__main__':
    zad = json.load(open(sys.argv[1], encoding='utf-8'))
    asyncio.run(renderuj(zad, sys.argv[2]))
    print(f'Wyrenderowano {len(zad)} plansz do {sys.argv[2]}')
