import {chromium} from 'playwright-core';
import {pathToFileURL} from 'node:url';
import {resolve} from 'node:path';
const b = await chromium.launch({executablePath: '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell', args: ['--no-sandbox']});
const p = await b.newPage({viewport: {width: 900, height: 1300}});
await p.goto(pathToFileURL(resolve(process.argv[2])).href, {waitUntil: 'load'});
await p.emulateMedia({media: 'print'});
const r = await p.evaluate(() => {
  const sh = document.querySelectorAll('.sheet')[8]; const t = sh.querySelector('table.tbl');
  const cs = getComputedStyle(t); const cells = [...t.querySelectorAll('thead th')].map(th => Math.round(th.getBoundingClientRect().width));
  const dl = t.querySelector('tbody tr:nth-child(2) td:last-child .dline'); const dcs = getComputedStyle(dl);
  return {sheet: sh.getBoundingClientRect().width, sbody: sh.querySelector('.sbody').getBoundingClientRect().width, table: t.getBoundingClientRect().width, layout: cs.tableLayout, cells, dline: {display: dcs.display, width: dcs.width, minWidth: dcs.minWidth, ws: dcs.whiteSpace}};
});
console.log(JSON.stringify(r)); await b.close();
