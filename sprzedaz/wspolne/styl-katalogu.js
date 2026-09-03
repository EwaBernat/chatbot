/* Wspólna warstwa graficzna katalogów PCTP.
   Używają jej: katalog-szkolen/ i katalog-pomocy/                          */

const fs = require("fs");
const path = require("path");

const KROJE = fs.readFileSync(
  path.join(__dirname, "..", "broszura", "fonts.css"), "utf8");

const esc = (s) => String(s)
  .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

const lista = (xs, kolor) => `<ul>${xs.map((x) =>
  `<li${kolor ? ` style="--pkt:${kolor}"` : ""}>${esc(x)}</li>`).join("")}</ul>`;

const styl = () => `<style>
${KROJE}
:root{
  --fiolet:#2D1B69; --fiolet-jasny:#4B3494; --pomarancz:#E8450A; --brzoskwinia:#F5B98E;
  --zielony:#0D7D5C; --bezowy:#C47A10; --papier:#FBF8F3; --atrament:#241C33;
  --szept:#6E6880; --kreska:#E3DDD2; --tlo-fiolet:#F4F2FA; --tlo-pomarancz:#FDF1EC;
  --naglowek:'Baloo 2','Trebuchet MS',system-ui,sans-serif;
  --tekst:'Atkinson Hyperlegible',Verdana,system-ui,sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:#EFEAE1;color:var(--atrament);font-family:var(--tekst);
     font-size:10.4px;line-height:1.55}
#dok{max-width:794px;margin:0 auto;background:var(--papier);padding:44px 56px 60px;
     box-shadow:0 18px 44px -12px rgba(36,28,51,.3)}
h1,h2,h3,h4{font-family:var(--naglowek);margin:0;line-height:1.1;font-weight:700;color:var(--fiolet)}
h1{font-size:34px;letter-spacing:-.015em}
h2{font-size:21px;margin-top:24px}
h3{font-size:14.5px;margin-top:14px}
p{margin:0 0 9px}
strong{color:var(--fiolet)}
.nad{font-family:var(--naglowek);font-weight:700;font-size:9.4px;letter-spacing:.26em;
     text-transform:uppercase;color:var(--pomarancz);margin-bottom:8px}
.lead{font-size:12.6px;line-height:1.55;color:#453D5A;margin:10px 0 16px}
.rule{height:4px;width:52px;border-radius:2px;background:var(--pomarancz);margin:12px 0 18px}
ul{list-style:none;margin:0 0 10px;padding:0}
li{position:relative;padding-left:15px;margin-bottom:4px;line-height:1.5}
li::before{content:"";position:absolute;left:0;top:6px;width:6px;height:6px;border-radius:2px;
           background:var(--pkt,var(--pomarancz))}
table{width:100%;border-collapse:collapse;font-size:9.2px;margin:10px 0 14px}
th{background:var(--fiolet);color:#fff;font-family:var(--naglowek);font-weight:700;font-size:8.2px;
   letter-spacing:.14em;text-transform:uppercase;text-align:left;padding:7px 9px}
td{padding:8px 9px;border-bottom:1px solid var(--kreska);vertical-align:top;color:#4A4358}
tr:nth-child(even) td{background:var(--tlo-fiolet)}
.etyk{font-family:var(--naglowek);font-weight:700;font-size:8px;letter-spacing:.16em;
      text-transform:uppercase;color:var(--szept);display:block;margin-bottom:4px}
.blok{background:var(--tlo-fiolet);border-radius:8px;padding:13px 15px;margin:12px 0}
.blok.akcent{background:var(--tlo-pomarancz);border-left:4px solid var(--pomarancz)}
.podstawa{font-size:8.8px;color:var(--bezowy)}

/* karta pozycji katalogu */
.poz{border:1.5px solid var(--kreska);border-radius:10px;background:#fff;padding:0;
     margin:16px 0;overflow:hidden;break-inside:avoid;page-break-inside:avoid}
.poz .pas{height:5px}
.poz .srodek{padding:16px 18px 18px}
.poz .kod{font-family:var(--naglowek);font-weight:700;font-size:8.6px;letter-spacing:.2em;
          text-transform:uppercase;color:var(--szept)}
.poz h3{font-size:19px;margin:4px 0 0}
.poz .pod{font-size:11px;color:var(--pomarancz);font-family:var(--naglowek);font-weight:600;margin-top:2px}
.poz .opis{margin-top:8px;color:#4A4358}
.fakty{display:grid;grid-template-columns:repeat(4,1fr);gap:2px;margin:12px 0}
.fakty div{background:var(--tlo-fiolet);padding:8px 10px}
.fakty b{display:block;font-family:var(--naglowek);font-size:11.5px;color:var(--fiolet);margin-top:2px}
.dwie{display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:10px}
.cena{font-family:var(--naglowek);font-weight:800;font-size:17px;color:var(--pomarancz);
      border-top:1.5px solid var(--kreska);margin-top:12px;padding-top:10px;
      display:flex;justify-content:space-between;align-items:baseline}
.cena small{font-family:var(--tekst);font-weight:400;font-size:8.8px;color:var(--szept);letter-spacing:.08em}
.wstazka{display:inline-block;background:var(--pomarancz);color:#fff;border-radius:3px;
         font-family:var(--naglowek);font-weight:700;font-size:8px;letter-spacing:.16em;
         padding:3px 9px;text-transform:uppercase;margin-bottom:6px}

/* pasek pięciu kolorów */
.pasy{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin:18px 0}
.pasy div{border-radius:4px;padding:9px 6px;text-align:center;
          font-family:var(--naglowek);font-weight:700;font-size:12px}
.metryczka{display:grid;grid-template-columns:repeat(4,1fr);gap:2px;margin:12px 0 4px}
.metryczka div{background:var(--tlo-fiolet);padding:9px 11px}
.metryczka b{display:block;font-family:var(--naglowek);font-size:12px;color:var(--fiolet);margin-top:2px}
.stopka-dok{margin-top:26px;padding-top:12px;border-top:1.5px solid var(--kreska);
            font-size:9px;color:var(--szept)}
.tytulowa{padding:60px 0 30px;break-after:page;page-break-after:always}
.tytulowa h1{font-size:52px}
.czesc{break-before:page;page-break-before:always}
h2,h3,tr{break-inside:avoid;page-break-inside:avoid}
.blok{break-inside:avoid}
@media print{
  @page{size:A4;margin:15mm 14mm 13mm}
  body{background:#fff;font-size:9.6px}
  #dok{max-width:none;padding:0;box-shadow:none;background:#fff}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
</style>`;

/* pełny dokument + wersja do publikacji */
function zapisz({ katalog, plikBazowy, tytul, opis, tresc }) {
  const strona = `<title>${esc(tytul)}</title>\n${styl()}\n<div id="dok">\n${tresc}\n</div>`;
  fs.writeFileSync(path.join(katalog, plikBazowy + "-artifact.html"), strona);
  fs.writeFileSync(path.join(katalog, plikBazowy + ".html"),
`<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="${esc(opis)}">
<meta name="author" content="Mirosława Ewa Jurczyszyn">
</head><body>
${strona}
</body></html>`);
  return strona.length;
}

module.exports = { styl, esc, lista, zapisz, KROJE };
