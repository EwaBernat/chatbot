/* Pomiar, czy każda strona druku FBA-C mieści się na jednej kartce A4 pionowo.
 *
 * Strona, która wyjdzie poza budżet, nie zgłasza błędu — po prostu przelewa się
 * na następną kartkę i rozcina kartę celu w pół. Widać to dopiero przy drukarce.
 * Budżet: A4 210×297 mm, margines 9 mm → 726×1054 px przy 96 dpi.
 *
 *   node src/zmierz_strony.mjs [plik.html ...]
 */
import path from 'node:path';
import fs from 'node:fs';
import { pathToFileURL } from 'node:url';

async function wczytajPlaywright() {
  const kandydaci = ['playwright', path.resolve('node_modules/playwright/index.js'),
    '/opt/node22/lib/node_modules/playwright/index.js', '/usr/lib/node_modules/playwright/index.js'];
  for (const k of kandydaci) {
    try { const m = await import(k.startsWith('/') ? pathToFileURL(k).href : k);
          return m.chromium ?? m.default?.chromium; } catch { /* następny */ }
  }
  console.error('Nie znalazłem playwrighta.'); process.exit(2);
}
const chromium = await wczytajPlaywright();
const PRZEGLADARKA = fs.existsSync('/opt/pw-browsers/chromium')
  ? { executablePath: '/opt/pw-browsers/chromium' } : {};

const MM = 96 / 25.4;
const SZEROKOSC = Math.round(192 * MM), WYSOKOSC = Math.round(279 * MM);
const pliki = (process.argv.slice(2).length ? process.argv.slice(2)
  : ['Cele_SMART_FBA_obserwacja_poglebiona.html']).map(p => path.resolve(p));

const b = await chromium.launch(PRZEGLADARKA);
const p = await b.newPage({ viewport: { width: SZEROKOSC, height: 1200 } });
await p.route('**://fonts.*/**', r => r.abort());   // pomiar także bez internetu
await p.emulateMedia({ media: 'print' });

let zle = 0;
for (const plik of pliki) {
  await p.goto('file://' + plik, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(400);
  const s = await p.evaluate(() => [...document.querySelectorAll('.strona')].map(x => ({
    h: Math.round(x.getBoundingClientRect().height),
    w: Math.round(x.getBoundingClientRect().width),
    opis: (x.querySelector('.stopka span:last-child') || {}).textContent || '',
  })));
  console.log('\n' + path.basename(plik));
  for (const x of s) {
    const ok = x.h <= WYSOKOSC && x.w <= SZEROKOSC;
    if (!ok) zle++;
    console.log(`  ${ok ? 'OK  ' : 'POZA'} ${String(x.h).padStart(5)}×${x.w} px  ${x.opis.trim()}`);
  }
}
await b.close();
console.log(`\nbudżet ${SZEROKOSC}×${WYSOKOSC} px · poza stroną: ${zle}`);
process.exit(zle ? 1 : 0);
