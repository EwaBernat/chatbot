#!/usr/bin/env python3
"""Plansze spotu EduPlaner 2026 -> PNG, w poziomie (1920x1080) i w pionie (1080x1920).

Marka PCTP: fiolet #2D1B69, pomaranicz #E8450A, krój metrycznie zgodny z Arialem.

Uruchomienie:
    python3 reklama/build_plansze.py            # oba formaty
    python3 reklama/build_plansze.py poziom     # tylko 16:9
    python3 reklama/build_plansze.py pion       # tylko 9:16
"""
import asyncio
import base64
import sys
from pathlib import Path

from playwright.async_api import async_playwright

KATALOG = Path(__file__).parent
# W tym kontenerze Chromium jest wgrany osobno; podajemy sciezke wprost,
# zeby Playwright nie probowal pobierac wlasnej wersji.
CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
# Logo PCTP. Gdy plik istnieje, plansze pokazuja znak; gdy nie — napis tekstowy.
LOGO = KATALOG.parent / "assets" / "logo-pctp.png"
FIOLET, FIOLET_C, POMARANCZ = "#2D1B69", "#1a0f42", "#E8450A"

FORMATY = {
    "poziom": {"w": 1920, "h": 1080, "katalog": KATALOG / "plansze"},
    "pion": {"w": 1080, "h": 1920, "katalog": KATALOG / "plansze-pion"},
}


def css(w: int, h: int, pion: bool) -> str:
    """Arkusz stylu dla jednego formatu.

    W pionie os etapow ustawia sie w kolumne, a typografia schodzi o ok. 20%,
    zeby najdluzszy etap ("Plan wsparcia") miescil sie w kadrze bez lamania.
    """
    return f"""
*{{margin:0;padding:0;box-sizing:border-box;
   font-family:'Liberation Sans','DejaVu Sans',Arial,sans-serif;}}
html,body{{width:{w}px;height:{h}px;overflow:hidden;}}
.stage{{width:{w}px;height:{h}px;position:relative;color:#fff;overflow:hidden;
  background:radial-gradient(circle at 76% 18%, #3a2483 0%, {FIOLET} 44%, {FIOLET_C} 100%);}}
.blob{{position:absolute;border-radius:50%;filter:blur(3px);}}
.b1{{width:{560 if not pion else 460}px;height:{560 if not pion else 460}px;
     background:{POMARANCZ};top:-160px;right:-130px;opacity:.20;}}
.b2{{width:{420 if not pion else 360}px;height:{420 if not pion else 360}px;
     background:#6b4bd6;bottom:-140px;left:-90px;opacity:.28;}}
.bar{{position:absolute;left:0;top:0;width:{14 if not pion else 12}px;
      height:100%;background:{POMARANCZ};}}
.wm{{position:absolute;top:{56 if not pion else 74}px;left:{100 if not pion else 68}px;
     font-size:{26 if not pion else 24}px;letter-spacing:7px;font-weight:700;color:#d9ccff;}}
.wm b{{color:{POMARANCZ};}}
.logo{{position:absolute;top:{40 if not pion else 56}px;left:{88 if not pion else 56}px;
       width:{104 if not pion else 92}px;height:{104 if not pion else 92}px;
       border-radius:50%;background:rgba(255,255,255,.94);padding:5px;
       box-shadow:0 8px 24px rgba(0,0,0,.35);}}
.logo img{{width:100%;height:100%;border-radius:50%;display:block;}}
.mid{{position:absolute;inset:0;display:flex;flex-direction:column;
      justify-content:center;align-items:center;text-align:center;
      padding:0 {140 if not pion else 80}px;}}
h1{{font-size:{112 if not pion else 88}px;line-height:1.05;font-weight:700;letter-spacing:-2px;}}
h1 .o{{color:{POMARANCZ};}}
.sub{{font-size:{46 if not pion else 40}px;color:#e7deff;margin-top:34px;
      font-weight:400;line-height:1.35;}}
.podpis{{position:absolute;left:0;right:0;bottom:{118 if not pion else 210}px;text-align:center;}}
.podpis .imie{{font-size:{44 if not pion else 38}px;font-weight:700;color:#fff;}}
.podpis .rola{{font-size:{30 if not pion else 26}px;color:{POMARANCZ};margin-top:10px;
               font-weight:700;letter-spacing:3px;text-transform:uppercase;}}
.os{{display:flex;align-items:center;justify-content:center;
     flex-direction:{'row' if not pion else 'column'};gap:{22 if not pion else 16}px;
     margin-top:14px;}}
.krok{{padding:{'24px 34px' if not pion else '22px 40px'};border-radius:18px;
       font-size:{34 if not pion else 40}px;font-weight:700;
       border:3px solid rgba(255,255,255,.22);color:#8d7cc4;white-space:nowrap;}}
.krok.byl{{color:#fff;border-color:rgba(255,255,255,.55);}}
.krok.teraz{{color:#fff;background:{POMARANCZ};border-color:{POMARANCZ};
             box-shadow:0 14px 42px rgba(232,69,10,.45);}}
.strzalka{{font-size:{34 if not pion else 30}px;color:#6b58a8;}}
.kafle{{display:flex;gap:{34 if not pion else 22}px;justify-content:center;
        margin-top:{64 if not pion else 56}px;}}
.kafel{{padding:{'30px 52px' if not pion else '24px 34px'};border-radius:20px;
        font-size:{36 if not pion else 32}px;font-weight:700;
        background:rgba(255,255,255,.08);border:2px solid rgba(255,255,255,.20);}}
.naglowek{{font-size:{32 if not pion else 28}px;letter-spacing:4px;text-transform:uppercase;
           color:#bfa9ff;font-weight:700;margin-bottom:{52 if not pion else 46}px;}}
.nie{{font-size:{62 if not pion else 52}px;font-weight:700;line-height:1.6;color:#7e6cb8;
      text-decoration:line-through;text-decoration-color:{POMARANCZ};
      text-decoration-thickness:5px;}}
.czas{{font-size:{230 if not pion else 150}px;font-weight:700;color:{POMARANCZ};
       letter-spacing:{16 if not pion else 10}px;}}
.czas-sub{{font-size:{52 if not pion else 42}px;color:#e7deff;margin-top:26px;font-weight:400;}}
.stopka{{position:absolute;left:0;right:0;bottom:{96 if not pion else 180}px;text-align:center;
         font-size:{32 if not pion else 28}px;color:#d9ccff;line-height:1.9;}}
.stopka .kontakt{{color:{POMARANCZ};font-weight:700;font-size:{36 if not pion else 30}px;}}
.qr{{width:{190 if not pion else 220}px;height:{190 if not pion else 220}px;
     margin:{44 if not pion else 60}px auto 0;border-radius:18px;
     border:4px dashed rgba(232,69,10,.75);display:flex;align-items:center;
     justify-content:center;font-size:22px;color:#e0a68c;text-align:center;
     line-height:1.4;padding:14px;}}
"""


def znak() -> str:
    """Logo PCTP jako data URI, a bez pliku — napis tekstowy.

    Logo jest ciemnofioletowe i okragle, wiec na tle marki #2D1B69 gubi sie.
    Dlatego lezy na jasnym krazku — inaczej widac sam kwiat, bez konturu pieczeci.
    """
    if LOGO.exists():
        dane = base64.b64encode(LOGO.read_bytes()).decode()
        return f"<div class='logo'><img src='data:image/png;base64,{dane}' alt='PCTP'></div>"
    return "<div class='wm'>EDU<b>PLANER</b> 2026</div>"


def strona(tresc: str, w: int, h: int, pion: bool, podpis: bool = False) -> str:
    stopka = ""
    if podpis:
        stopka = ("<div class='podpis'>"
                  "<div class='imie'>Pomorskie Centrum Terapii Pedagogicznej</div>"
                  "<div class='rola'>Koszalin</div></div>")
    return (f"<!doctype html><meta charset='utf-8'><style>{css(w, h, pion)}</style>"
            f"<div class='stage'><div class='blob b1'></div><div class='blob b2'></div>"
            f"<div class='bar'></div>{znak()}"
            f"{tresc}{stopka}</div>")


def os_etapow(aktywny: int, pion: bool) -> str:
    """aktywny = indeks etapu podswietlonego; wczesniejsze biale, pozniejsze wygaszone."""
    etapy = ["Metryczka", "WOPF", "Plan wsparcia", "Realizacja", "Ewaluacja"]
    strzalka = "&#8595;" if pion else "&#8594;"
    czesci = []
    for i, e in enumerate(etapy):
        klasa = "teraz" if i == aktywny else ("byl" if i < aktywny else "")
        czesci.append(f"<div class='krok {klasa}'>{e}</div>")
        if i < len(etapy) - 1:
            czesci.append(f"<div class='strzalka'>{strzalka}</div>")
    return "<div class='os'>" + "".join(czesci) + "</div>"


def plansze(w: int, h: int, pion: bool):
    """(nazwa, czas mowy w sekundach, HTML) — czasy wspolne dla obu formatow."""
    s = lambda tresc, podpis=False: strona(tresc, w, h, pion, podpis)
    return [
        ("s1a", 2.0, s(
            "<div class='mid'><h1>EduPlaner <span class='o'>2026</span></h1>"
            "<div class='sub'>Cyfrowa szafa dla Twojej placówki</div></div>")),
        ("s1b", 9.0, s(
            "<div class='mid'><h1>EduPlaner <span class='o'>2026</span></h1>"
            "<div class='sub'>Zbudowana przez praktyków, dla praktyków</div></div>",
            podpis=True)),
        ("s2a", 7.0, s(
            "<div class='mid'><div class='naglowek'>Ścieżka dziecka</div>"
            + os_etapow(1, pion) + "</div>")),
        ("s2b", 7.0, s(
            "<div class='mid'><div class='naglowek'>Od zgłoszenia po podsumowanie</div>"
            + os_etapow(4, pion)
            + "<div class='kafle'><div class='kafel'>Zespół</div>"
              "<div class='kafel'>Baza wiedzy</div></div></div>")),
        ("s3a", 9.0, s(
            "<div class='mid'><div class='nie'>szukanie wzorów</div>"
            "<div class='nie'>przepisywanie od zera</div>"
            "<div class='nie'>niepokój o przepisy</div></div>")),
        ("s3b", 6.0, s(
            "<div class='mid'><div class='czas'>CZAS</div>"
            "<div class='czas-sub'>Dla dziecka. Dla ucznia. I dla siebie.</div></div>")),
        ("s4", 9.0, s(
            "<div class='mid'><h1>Otwarty <span class='o'>projekt</span></h1>"
            "<div class='sub'>Zmienia się prawo — aplikacja zmienia się razem z Tobą.<br>"
            "To Ty jesteś jej współautorką.</div></div>")),
        ("s5", 14.0, s(
            "<div class='mid'><h1>Mniej dokumentów.<br>"
            "<span class='o'>Więcej edukacji.</span></h1>"
            "<div class='qr'>QR / link do zamówienia</div></div>"
            "<div class='stopka'>Pomorskie Centrum Terapii Pedagogicznej<br>"
            "<span class='kontakt'>kontakt@eduplaner2026.pl &nbsp;·&nbsp; 662 888 403</span>"
            "</div>")),
    ]


# Czasy plansz — jedno zrodlo prawdy dla build_wideo.py, niezalezne od formatu.
CZASY = [(nazwa, czas) for nazwa, czas, _ in plansze(1920, 1080, False)]


async def zbuduj(nazwa_formatu: str) -> None:
    f = FORMATY[nazwa_formatu]
    pion = nazwa_formatu == "pion"
    f["katalog"].mkdir(exist_ok=True)
    async with async_playwright() as pw:
        przegladarka = await pw.chromium.launch(
            executable_path=CHROMIUM if Path(CHROMIUM).exists() else None)
        karta = await przegladarka.new_page(viewport={"width": f["w"], "height": f["h"]})
        for nazwa, _, html in plansze(f["w"], f["h"], pion):
            await karta.set_content(html)
            await karta.screenshot(path=str(f["katalog"] / f"{nazwa}.png"))
        await przegladarka.close()
    print(f"{nazwa_formatu}: {len(CZASY)} plansz {f['w']}x{f['h']} w {f['katalog']}")


async def main() -> None:
    wybrane = sys.argv[1:] or list(FORMATY)
    for nazwa in wybrane:
        if nazwa not in FORMATY:
            raise SystemExit(f"Nieznany format: {nazwa}. Dostępne: {', '.join(FORMATY)}")
        await zbuduj(nazwa)


if __name__ == "__main__":
    asyncio.run(main())
