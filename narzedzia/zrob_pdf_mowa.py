"""Robi gotowe PDF-y modułu mowy — takie, jak wygląda ekran.

Wydruk z przeglądarki zależy od jej ustawień (nagłówki z adresem i datą, skala,
marginesy, która zakładka była otwarta). Te pliki nie zależą od niczego:
rozmiar strony bierze się z @page w dokumencie, tła są włączone, a zakładka
wersji wiekowej jest ustawiana przed drukiem.
"""
import asyncio, pathlib, re, sys
from playwright.async_api import async_playwright

MM = 96 / 25.4
KAT = pathlib.Path("/tmp/mowa_pdf"); KAT.mkdir(exist_ok=True)
MOD = pathlib.Path("eduplaner_mowa/02_gotowe_dokumenty")

def kartek(p: pathlib.Path) -> int:
    return len(re.findall(rb"/Type\s*/Page[^s]", p.read_bytes()))

async def strona(b, plik, szer, wys):
    p = await b.new_page(viewport={"width": round(szer*MM), "height": round(wys*MM)})
    await p.goto(f"file://{pathlib.Path(plik).resolve()}")
    await p.wait_for_timeout(1800)
    return p

async def main():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")

        # ——— dokumenty A4 pionowo: co strona w podglądzie, to kartka w PDF ———
        for nazwa, plik in [("Karty_pracy_MOWA", "Karty_pracy_MOWA.html"),
                            ("Cele_SMART_MOWA", "Cele_SMART_MOWA_obserwacja_poglebiona.html")]:
            p = await strona(b, MOD / plik, 210, 297)
            ile = await p.evaluate("document.querySelectorAll('.strona').length")
            cel = KAT / f"{nazwa}.pdf"
            await p.pdf(path=str(cel), format="A4", print_background=True, prefer_css_page_size=True)
            print(f"{cel.name:<38} podgląd {ile:>3} · PDF {kartek(cel):>3} kartek",
                  "✓" if ile == kartek(cel) else "✗ ROZJAZD")
            await p.close()

        # ——— tabela: osobny plik na każdą wersję wiekową, bo na ekranie widać jedną ———
        for w, opis in [("A", "3-4_lata"), ("B", "5_lat"), ("C", "6_lat")]:
            p = await strona(b, MOD / "Tabela_celow_MOWA_wiek_poziom.html", 279, 192)
            await p.evaluate("""w => {
                document.querySelectorAll('.tab').forEach(x =>
                    x.setAttribute('aria-selected', String(x.dataset.wersja === w)));
                document.querySelectorAll('.wersja').forEach(s => { s.hidden = s.dataset.wersja !== w; });
            }""", w)
            await p.wait_for_timeout(500)
            widoczna = await p.evaluate("""() => {const s=[...document.querySelectorAll('.wersja')].find(x=>!x.hidden);
                                             return s.querySelector('caption').textContent.trim();}""")
            cel = KAT / f"Tabela_celow_MOWA_wersja_{w}_{opis}.pdf"
            await p.pdf(path=str(cel), format="A4", landscape=True, print_background=True,
                        prefer_css_page_size=True)
            print(f"{cel.name:<38} {widoczna} · PDF {kartek(cel)} kartek")
            await p.close()

        # ——— zeszyty konspektów: 25 konspektów danej wersji, A4 pionowo ———
        for w, opis in [("A", "3-4_lata"), ("B", "5_lat"), ("C", "6_lat")]:
            p = await strona(b, MOD / "Tabela_celow_MOWA_wiek_poziom.html", 210, 297)
            ile = await p.evaluate("""w => {
                const m = [...document.querySelectorAll('.kmodal[data-wersja="'+w+'"]')];
                m.forEach(x => {
                  x.classList.add('open');
                  x.querySelectorAll('.kvar').forEach(v => {
                    const t = zTabeli(w, x.dataset.wsk, v.dataset.lvl);
                    v.querySelector('.kon-cel').textContent = t.cel;
                    v.querySelector('.kon-kryt').textContent = t.ram;
                  });
                });
                document.documentElement.classList.add('druk-konspektu');
                return m.length;
            }""", w)
            await p.wait_for_timeout(900)
            cel = KAT / f"Konspekty_MOWA_wersja_{w}_{opis}.pdf"
            await p.pdf(path=str(cel), format="A4", print_background=True, prefer_css_page_size=True)
            print(f"{cel.name:<38} {ile} konspektów · PDF {kartek(cel)} kartek")
            await p.close()
        await b.close()
asyncio.run(main())
