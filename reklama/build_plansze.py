#!/usr/bin/env python3
"""Plansze spotu EduPlaner 2026 (60 s) -> PNG 1920x1080.

Marka PCTP: fiolet #2D1B69, pomaranicz #E8450A, krój metrycznie zgodny z Arialem.
Uruchomienie:  python3 reklama/build_plansze.py
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

WYJSCIE = Path(__file__).parent / "plansze"
# W tym kontenerze Chromium jest wgrany osobno; podajemy sciezke wprost,
# zeby Playwright nie probowal pobierac wlasnej wersji.
CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
FIOLET, FIOLET_C, POMARANCZ = "#2D1B69", "#1a0f42", "#E8450A"

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box;
   font-family:'Liberation Sans','DejaVu Sans',Arial,sans-serif;}}
html,body{{width:1920px;height:1080px;overflow:hidden;}}
.stage{{width:1920px;height:1080px;position:relative;color:#fff;overflow:hidden;
  background:radial-gradient(circle at 76% 20%, #3a2483 0%, {FIOLET} 44%, {FIOLET_C} 100%);}}
.blob{{position:absolute;border-radius:50%;filter:blur(3px);}}
.b1{{width:560px;height:560px;background:{POMARANCZ};top:-180px;right:-140px;opacity:.20;}}
.b2{{width:420px;height:420px;background:#6b4bd6;bottom:-150px;left:-100px;opacity:.28;}}
.bar{{position:absolute;left:0;top:0;width:14px;height:100%;background:{POMARANCZ};}}
.wm{{position:absolute;top:56px;left:100px;font-size:26px;letter-spacing:7px;
     font-weight:700;color:#d9ccff;}}
.wm b{{color:{POMARANCZ};}}
.mid{{position:absolute;inset:0;display:flex;flex-direction:column;
      justify-content:center;align-items:center;text-align:center;padding:0 140px;}}
h1{{font-size:112px;line-height:1.03;font-weight:700;letter-spacing:-2px;}}
h1 .o{{color:{POMARANCZ};}}
.sub{{font-size:46px;color:#e7deff;margin-top:34px;font-weight:400;line-height:1.3;}}
.podpis{{position:absolute;left:0;right:0;bottom:118px;text-align:center;}}
.podpis .imie{{font-size:44px;font-weight:700;color:#fff;letter-spacing:.5px;}}
.podpis .rola{{font-size:30px;color:{POMARANCZ};margin-top:10px;font-weight:700;
               letter-spacing:3px;text-transform:uppercase;}}
.os{{display:flex;align-items:center;justify-content:center;gap:22px;margin-top:14px;}}
.krok{{padding:24px 34px;border-radius:18px;font-size:34px;font-weight:700;
       border:3px solid rgba(255,255,255,.22);color:#8d7cc4;white-space:nowrap;}}
.krok.byl{{color:#fff;border-color:rgba(255,255,255,.55);}}
.krok.teraz{{color:#fff;background:{POMARANCZ};border-color:{POMARANCZ};
             box-shadow:0 14px 42px rgba(232,69,10,.45);}}
.strzalka{{font-size:34px;color:#6b58a8;}}
.kafle{{display:flex;gap:34px;justify-content:center;margin-top:64px;}}
.kafel{{padding:30px 52px;border-radius:20px;font-size:36px;font-weight:700;
        background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.20);}}
.naglowek{{font-size:32px;letter-spacing:4px;text-transform:uppercase;
           color:#bfa9ff;font-weight:700;margin-bottom:52px;}}
.nie{{font-size:62px;font-weight:700;line-height:1.5;color:#7e6cb8;
      text-decoration:line-through;text-decoration-color:{POMARANCZ};
      text-decoration-thickness:5px;}}
.nie .zywy{{color:#fff;text-decoration:none;}}
.czas{{font-size:230px;font-weight:700;color:{POMARANCZ};letter-spacing:16px;}}
.czas-sub{{font-size:52px;color:#e7deff;margin-top:26px;font-weight:400;}}
.stopka{{position:absolute;left:0;right:0;bottom:96px;text-align:center;
         font-size:32px;color:#d9ccff;line-height:1.9;}}
.stopka .kontakt{{color:{POMARANCZ};font-weight:700;font-size:36px;}}
.qr{{width:190px;height:190px;margin:44px auto 0;border-radius:18px;
     border:4px dashed rgba(232,69,10,.75);display:flex;align-items:center;
     justify-content:center;font-size:22px;color:#e0a68c;text-align:center;
     line-height:1.4;padding:14px;}}
"""


def strona(tresc: str, podpis: bool = False) -> str:
    stopka = ""
    if podpis:
        stopka = ("<div class='podpis'>"
                  "<div class='imie'>mgr Mirosława Ewa Jurczyszyn</div>"
                  "<div class='rola'>pedagog specjalny</div></div>")
    return (f"<!doctype html><meta charset='utf-8'><style>{CSS}</style>"
            f"<div class='stage'><div class='blob b1'></div><div class='blob b2'></div>"
            f"<div class='bar'></div><div class='wm'>EDU<b>PLANER</b> 2026</div>"
            f"{tresc}{stopka}</div>")


def os_etapow(aktywny: int) -> str:
    """aktywny = indeks etapu podswietlonego; wczesniejsze biale, pozniejsze wygaszone."""
    etapy = ["Metryczka", "WOPF", "Plan wsparcia", "Realizacja", "Ewaluacja"]
    czesci = []
    for i, e in enumerate(etapy):
        klasa = "teraz" if i == aktywny else ("byl" if i < aktywny else "")
        czesci.append(f"<div class='krok {klasa}'>{e}</div>")
        if i < len(etapy) - 1:
            czesci.append("<div class='strzalka'>&#8594;</div>")
    return "<div class='os'>" + "".join(czesci) + "</div>"


PLANSZE = [
    # (nazwa, czas mowy w sekundach, HTML)
    ("s1a", 2.0, strona(
        "<div class='mid'><h1>EduPlaner <span class='o'>2026</span></h1>"
        "<div class='sub'>Cyfrowa szafa dla Twojej placówki</div></div>")),
    ("s1b", 9.0, strona(
        "<div class='mid'><h1>EduPlaner <span class='o'>2026</span></h1>"
        "<div class='sub'>Zbudowana przez praktyków, dla praktyków</div></div>",
        podpis=True)),
    ("s2a", 7.0, strona(
        "<div class='mid'><div class='naglowek'>Ścieżka dziecka</div>"
        + os_etapow(1) + "</div>")),
    ("s2b", 7.0, strona(
        "<div class='mid'><div class='naglowek'>Od zgłoszenia po podsumowanie</div>"
        + os_etapow(4)
        + "<div class='kafle'><div class='kafel'>Zespół</div>"
          "<div class='kafel'>Baza wiedzy</div></div></div>")),
    ("s3a", 9.0, strona(
        "<div class='mid'><div class='nie'>szukanie wzorów</div>"
        "<div class='nie'>przepisywanie od zera</div>"
        "<div class='nie'>niepokój o przepisy</div></div>")),
    ("s3b", 6.0, strona(
        "<div class='mid'><div class='czas'>CZAS</div>"
        "<div class='czas-sub'>Dla dziecka. Dla ucznia. I dla siebie.</div></div>")),
    ("s4", 9.0, strona(
        "<div class='mid'><h1>Otwarty <span class='o'>projekt</span></h1>"
        "<div class='sub'>Zmienia się prawo — aplikacja zmienia się razem z Tobą.<br>"
        "To Ty jesteś jej współautorką.</div></div>")),
    ("s5", 14.0, strona(
        "<div class='mid'><h1>Mniej dokumentów.<br><span class='o'>Więcej edukacji.</span></h1>"
        "<div class='qr'>QR / link do formularza analizy potrzeb</div></div>"
        "<div class='stopka'>mgr Mirosława Ewa Jurczyszyn · pedagog specjalny<br>"
        "<span class='kontakt'>kontakt@eduplaner2026.pl &nbsp;·&nbsp; [usunięto]</span></div>")),
]


async def main() -> None:
    WYJSCIE.mkdir(exist_ok=True)
    async with async_playwright() as pw:
        przegladarka = await pw.chromium.launch(
            executable_path=CHROMIUM if Path(CHROMIUM).exists() else None)
        karta = await przegladarka.new_page(viewport={"width": 1920, "height": 1080})
        for nazwa, _, html in PLANSZE:
            await karta.set_content(html)
            await karta.screenshot(path=str(WYJSCIE / f"{nazwa}.png"))
            print(f"  {nazwa}.png")
        await przegladarka.close()
    print(f"Gotowe: {len(PLANSZE)} plansz w {WYJSCIE}")


if __name__ == "__main__":
    asyncio.run(main())
