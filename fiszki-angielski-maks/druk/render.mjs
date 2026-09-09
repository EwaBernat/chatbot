// Renderuje fiszki-druk.html do PDF w formacie A4. Wymaga: npm install playwright
import { chromium } from 'playwright';
import path from 'node:path';

const here = path.dirname(new URL(import.meta.url).pathname);
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + path.join(here, 'fiszki-druk.html'), { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);

const overflowing = await page.evaluate(() =>
  [...document.querySelectorAll('.card')]
    .flatMap((c, i) => (c.scrollHeight > c.clientHeight + 1 ? [i] : [])));
if (overflowing.length) console.warn('Karty z przepełnioną treścią:', overflowing.join(', '));

await page.pdf({
  path: path.join(here, '..', 'Fiszki-Angielski-dla-Maksia.pdf'),
  width: '8.2677in', height: '11.6929in',
  printBackground: true,
  margin: { top: 0, right: 0, bottom: 0, left: 0 },
});
await browser.close();
