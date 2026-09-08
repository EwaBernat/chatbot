/* Zeszyt konspektów KPOF-T (wszystkie konspekty jednej wersji) do PDF: node skrypty/druk_zeszytu.mjs <html> <wersja> <pdf> */
import {chromium} from 'playwright-core';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const [html, w, pdf] = process.argv.slice(2);
const browser = await chromium.launch({executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox']});
const page = await browser.newPage({viewport: {width: 1240, height: 1400}});
await page.goto(pathToFileURL(resolve(html)).href, {waitUntil: 'load'});
await page.evaluate(() => document.fonts.ready);
await page.evaluate((w) => {
  document.querySelectorAll('.kmodal[data-wersja="' + w + '"]').forEach((m) => {
    m.classList.add('open');
    m.querySelectorAll('.kvar').forEach((v) => {
      const td = document.querySelector('#w-' + w + ' tr[data-wsk="' + m.dataset.wsk + '"] td.g[data-lvl="' + v.dataset.lvl + '"]');
      v.querySelector('.kon-cel').textContent = td.querySelector('.tresc').textContent;
      v.querySelector('.kon-kryt').textContent = td.querySelector('.ram').textContent;
    });
  });
  document.documentElement.classList.add('druk-konspektu');
}, w);
await page.emulateMedia({media: 'print'});
await page.pdf({path: pdf, format: 'A4', printBackground: true, margin: {top: '10mm', bottom: '10mm', left: '10mm', right: '10mm'}});
await browser.close();
console.log('zapisano', pdf);
