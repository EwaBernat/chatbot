/* Wydruk obu druków do PDF — bez klikania w przeglądarce.
 *
 * FBA-C (cele do obserwacji pogłębionej) idzie pionowo, FBA-T (tabela wiek ×
 * poziom) poziomo: trzy poziomy wsparcia obok siebie nie mieszczą się na
 * kartce pionowej. Marginesy 9 mm — te same, w których mierzy `zmierz_strony.mjs`.
 *
 *   node src/do_pdf.mjs [plik.html ...]
 *
 * Bez argumentów robi oba druki z katalogu głównego modułu.
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
const domyslne = ['Cele_SMART_FBA_obserwacja_poglebiona.html', 'Tabela_celow_FBA_wiek_poziom.html']
  .map(p => path.join(KOR, p));
const pliki = (process.argv.slice(2).length ? process.argv.slice(2).map(p => path.resolve(p)) : domyslne)
  .filter(p => fs.existsSync(p) || (console.log('pomijam, nie ma pliku:', p), false));

const b = await chromium.launch(PRZEGLADARKA);
const p = await b.newPage();
for (const plik of pliki) {
  const poziomo = path.basename(plik).startsWith('Tabela_');
  const out = plik.replace(/\.html$/, '.pdf');
  await p.goto('file://' + plik, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(700);   // czas na fonty, jeśli sieć jest
  await p.pdf({ path: out, format: 'A4', landscape: poziomo, printBackground: true,
                margin: { top: '9mm', right: '9mm', bottom: '9mm', left: '9mm' } });
  console.log(`${path.basename(out)} · ${poziomo ? 'poziomo' : 'pionowo'} · ${(fs.statSync(out).size / 1024).toFixed(0)} kB`);

  /* Konspekty siedzą w tabeli jako modale i normalny wydruk je pomija. Zeszyt
     jednej wersji wiekowej to 25 scenariuszy plus 25 arkuszy — po jednej
     kartce A4 pionowo na każdy. */
  if (poziomo) {
    for (const w of ['A', 'B', 'C']) {
      await p.evaluate(v => { document.documentElement.dataset.zeszyt = v;
        document.documentElement.classList.add('print-zeszyt'); }, w);
      const kon = path.join(path.dirname(plik), `Konspekty_FBA_${w}.pdf`);
      await p.pdf({ path: kon, format: 'A4', printBackground: true,
                    margin: { top: '10mm', right: '10mm', bottom: '10mm', left: '10mm' } });
      await p.evaluate(() => { document.documentElement.classList.remove('print-zeszyt');
        delete document.documentElement.dataset.zeszyt; });
      console.log(`${path.basename(kon)} · pionowo · ${(fs.statSync(kon).size / 1024).toFixed(0)} kB`);
    }
  }
}
await b.close();
