/* Pomiar wysokości druku wszystkich konspektów FBA-T.
 *
 * Konspekt ma się mieścić na jednej kartce A4 pionowo, a materiał do wydruku
 * na drugiej — tak jak konspekty w banku. Przekroczenie budżetu nie zgłasza
 * błędu: konspekt po prostu pęka w pół tabeli przebiegu, co widać dopiero
 * przy drukarce. Budżet: A4 297 mm, margines 10 mm → 1047 px przy 96 dpi;
 * karta jest w druku skalowana do 0.96, więc mieści się 1090 px treści.
 *
 *   node src/zmierz_konspekty.mjs
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

const KOR = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const PLIK = process.argv[2] ? path.resolve(process.argv[2])
                             : path.join(KOR, 'Tabela_celow_FBA_wiek_poziom.html');
const SKALA = 0.96;                    // zoom karty w druku
const BUDZET = Math.round(1047 / SKALA);

const b = await chromium.launch(PRZEGLADARKA);
const p = await b.newPage({ viewport: { width: 718, height: 1047 } });
await p.route('**://fonts.*/**', r => r.abort());   // pomiar także bez internetu
await p.goto('file://' + PLIK, { waitUntil: 'domcontentloaded' });
await p.evaluate(() => document.documentElement.classList.add('print-konspekt'));
await p.emulateMedia({ media: 'print' });
await p.waitForTimeout(400);

const wyniki = await p.evaluate(() => {
  const out = [];
  for (const m of document.querySelectorAll('.kmodal')) {
    m.classList.add('open');
    const k = m.querySelector('.kcard');
    const zal = m.querySelector('.zal');
    out.push({ id: m.id,
      scenariusz: Math.round(k.getBoundingClientRect().height - zal.getBoundingClientRect().height),
      arkusz: Math.round(zal.getBoundingClientRect().height) });
    m.classList.remove('open');
  }
  return out;
});
await b.close();

const poza = wyniki.filter(w => w.scenariusz > BUDZET || w.arkusz > BUDZET);
const max = wyniki.reduce((a, w) => Math.max(a, w.scenariusz), 0);
for (const w of poza) console.log(`  POZA ${w.id}: scenariusz ${w.scenariusz}, arkusz ${w.arkusz}`);
console.log(`${wyniki.length} konspektów · najwyższy scenariusz ${max} px · budżet ${BUDZET} px `
          + `(A4 pionowo, skala ${SKALA}) · poza stroną: ${poza.length}`);
process.exit(poza.length ? 1 : 0);
