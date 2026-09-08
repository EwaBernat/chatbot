/* Drukuje plik HTML (druk A4) do PDF i zrzutów stron: node skrypty/drukuj_pdf.mjs <html> <pdf> [katalog_png] [strony np. 1,2,5] */
import {chromium} from 'playwright-core';
import {mkdirSync} from 'node:fs';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const [html, pdf, pngdir, strony] = process.argv.slice(2);
const exe = process.env.CHROME_PATH || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const browser = await chromium.launch({executablePath: exe, args: ['--no-sandbox']});
const page = await browser.newPage({viewport: {width: 900, height: 1300}});
await page.goto(pathToFileURL(resolve(html)).href, {waitUntil: 'load'});
await page.evaluate(() => document.fonts.ready);
await page.emulateMedia({media: 'print'});
await page.pdf({path: resolve(pdf), format: 'A4', printBackground: true, preferCSSPageSize: true});
await page.emulateMedia({media: 'screen'});
if (pngdir) {
  mkdirSync(pngdir, {recursive: true});
  const els = await page.$$('.page');
  const lista = strony ? strony.split(',').map(Number) : els.map((_, i) => i + 1);
  for (const n of lista) { await els[n - 1].screenshot({path: resolve(pngdir, `str${String(n).padStart(2, '0')}.png`), scale: 'css'}); }
  // wykryj przepełnienie: elementy .pbody, których scrollHeight > clientHeight
  const over = await page.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => { const b = p.querySelector('.pbody'); return b.scrollHeight - b.clientHeight > 2 ? (i + 1) + ':' + (b.scrollHeight - b.clientHeight) : null; }).filter(Boolean));
  console.log('przepełnione strony (nr:px):', over.length ? over.join(' ') : 'brak');
}
await browser.close();
console.log('zapisano', pdf);
