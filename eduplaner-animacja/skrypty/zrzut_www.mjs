/* Zrzuty strony HTML: node skrypty/zrzut_www.mjs <html> <png-prefix> [selektor-klik] */
import {chromium} from 'playwright-core';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const [html, pref, klik] = process.argv.slice(2);
const exe = process.env.CHROME_PATH || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const browser = await chromium.launch({executablePath: exe, args: ['--no-sandbox']});
const page = await browser.newPage({viewport: {width: 1240, height: 1100}});
await page.goto(pathToFileURL(resolve(html)).href, {waitUntil: 'load'});
await page.evaluate(() => document.fonts.ready);
await page.screenshot({path: pref + '_1.png'});
if (klik) { await page.click(klik); await page.waitForTimeout(300); await page.screenshot({path: pref + '_2.png'}); }
await browser.close();
