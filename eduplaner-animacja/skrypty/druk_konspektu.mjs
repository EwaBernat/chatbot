/* Drukuje jeden konspekt z KPOF-T do PDF: node skrypty/druk_konspektu.mjs <html> <wersja> <nr> <lvl> <pdf> */
import {chromium} from 'playwright-core';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const [html, w, nr, lvl, pdf] = process.argv.slice(2);
const browser = await chromium.launch({executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox']});
const page = await browser.newPage({viewport: {width: 1240, height: 1400}});
await page.goto(pathToFileURL(resolve(html)).href, {waitUntil: 'load'});
await page.evaluate(() => document.fonts.ready);
await page.click(`#w-${w} tr[data-nr="${nr}"] td.g[data-lvl="${lvl}"]`);
await page.evaluate(() => document.documentElement.classList.add('druk-konspektu'));
await page.emulateMedia({media: 'print'});
await page.pdf({path: pdf, format: 'A4', printBackground: true, margin: {top: '10mm', bottom: '10mm', left: '10mm', right: '10mm'}});
await browser.close();
console.log('zapisano', pdf);
