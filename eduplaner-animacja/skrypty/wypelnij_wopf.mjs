/* Wypełnia ORYGINALNY arkusz WOPF danymi z public/wopf-dane.json w prawdziwej przeglądarce
   (własny skrypt arkusza liczy średnie, wykresy i opisy) i zapisuje gotowy HTML + PDF.
   Uruchomienie: node skrypty/wypelnij_wopf.mjs  */
import {chromium} from 'playwright-core';
import {readFileSync, writeFileSync, mkdirSync} from 'node:fs';
import {resolve, dirname} from 'node:path';
import {fileURLToPath, pathToFileURL} from 'node:url';

const tu = dirname(fileURLToPath(import.meta.url));
const katalog = resolve(tu, '..');
const dane = JSON.parse(readFileSync(resolve(katalog, 'public/wopf-dane.json'), 'utf8'));
const resolver = readFileSync(resolve(tu, 'wopf_resolver.js'), 'utf8');
const exe = process.env.CHROME_PATH || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const wyj = process.argv[2] || resolve(katalog, 'out/wopf');
mkdirSync(wyj, {recursive: true});

const browser = await chromium.launch({executablePath: exe, args: ['--no-sandbox']});
const page = await browser.newPage({viewport: {width: 1000, height: 1400}});
await page.goto(pathToFileURL(resolve(katalog, 'public/wopf.html')).href, {waitUntil: 'load'});
await page.evaluate(resolver);
const raport = await page.evaluate((kroki) => {
  const R = window.WopfResolver; const brak = [];
  kroki.forEach((k, i) => { if (R.zastosuj(document, k) === 0) brak.push(i + ' ' + JSON.stringify(k).slice(0, 90)); });
  // przelicz wszystko jeszcze raz (średnie, poziomy, wykresy, opisy z bazy wzorów)
  const q = document.querySelector('table.qtab tbody td'); if (q) q.dispatchEvent(new Event('input', {bubbles: true}));
  document.querySelector('.itoolbar')?.remove(); // pasek narzędzi ekranowy nie należy do dokumentu
  return {brak, srednia: [...document.querySelectorAll('.f')].filter((f) => /Średnia ogólna/.test(f.textContent)).map((f) => f.querySelector('.fv').textContent)[0]};
}, dane.kroki);
console.log('nie znaleziono:', raport.brak.length ? raport.brak : 'nic — wszystkie kroki trafiły', '| średnia ogólna:', raport.srednia);
const html = await page.content();
writeFileSync(resolve(wyj, 'WOPF_2026_Zofia_Lewandowska_wypelniony.html'), html);
await page.emulateMedia({media: 'print'});
await page.pdf({path: resolve(wyj, 'WOPF_2026_Zofia_Lewandowska_wypelniony.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true});
await page.emulateMedia({media: 'screen'});
for (const n of [1, 2, 5, 6, 7, 14, 15, 17]) {
  const el = (await page.$$('.page'))[n - 1];
  await el.screenshot({path: resolve(wyj, `str${n}.png`)});
}
await browser.close();
console.log('zapisano w', wyj);
