/* Wypełnia oryginalny druk (strony .page/.sheet) krokami {sel,t|k}: node skrypty/wypelnij_druk.mjs <html> <kroki.json> <out-html> <out-pdf> [png-dir] [zamiany.json] */
import {chromium} from 'playwright-core';
import {readFileSync, writeFileSync, mkdirSync} from 'node:fs';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const [html, kroki, outHtml, outPdf, pngdir, zamiany] = process.argv.slice(2);
const K = JSON.parse(readFileSync(kroki, 'utf8')).kroki;
const Z = zamiany ? JSON.parse(readFileSync(zamiany, 'utf8')) : [];
const browser = await chromium.launch({executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox']});
const page = await browser.newPage({viewport: {width: 900, height: 1300}});
await page.goto(pathToFileURL(resolve(html)).href, {waitUntil: 'load'});
await page.evaluate(() => document.fonts.ready);
const brak = await page.evaluate(({K, Z}) => {
  const wybierz = (sel) => { const m = /^(?:@(\d+)\s+)?(.*?)(?:\s+#(\d+))?$/.exec(sel); const z = m[1] ? document.querySelectorAll('.page, .sheet')[Number(m[1]) - 1] : document; if (!z) return null; return m[3] !== undefined ? z.querySelectorAll(m[2])[Number(m[3])] : z.querySelector(m[2]); };
  const brak = [];
  for (const k of K) { const el = wybierz(k.sel); if (!el) { brak.push(k.sel); continue; } if (k.k) { const c = el.querySelector('.chk'); (c ?? el).classList.add('on'); if (el.classList.contains('opt')) el.classList.add('on'); } else el.textContent = k.t; }
  for (const [a, b] of Z) { document.body.innerHTML = document.body.innerHTML.split(a).join(b); }
  document.querySelectorAll('.addrow, .delcell, .printcell, .delrow').forEach((e) => e.remove());
  return brak;
}, {K, Z});
console.log('nie znaleziono:', brak.length ? brak : 'nic');
writeFileSync(outHtml, await page.content());
await page.emulateMedia({media: 'print'});
await page.pdf({path: outPdf, format: 'A4', printBackground: true, preferCSSPageSize: true});
if (pngdir) { mkdirSync(pngdir, {recursive: true}); await page.emulateMedia({media: 'screen'}); const els = await page.$$('.page, .sheet'); for (let i = 0; i < els.length; i++) await els[i].screenshot({path: resolve(pngdir, `str${i + 1}.png`), scale: 'css'}); }
await browser.close();
