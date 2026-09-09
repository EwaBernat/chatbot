/* Mapa pól druku: node skrypty/mapa_druku.mjs <html> [arkusze np. 1,2,5]
   Dla każdego arkusza (.sheet/.page) wypisuje elementy wypełnialne z indeksem w obrębie arkusza
   (selektor "@N .klasa #k" jak w OryginalnyDruk / wypelnij_druk) oraz etykietę w pobliżu. */
import {chromium} from 'playwright-core';
import {resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
const [html, strony] = process.argv.slice(2);
const exe = process.env.CHROME_PATH || '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell';
const browser = await chromium.launch({executablePath: exe, args: ['--no-sandbox']});
const page = await browser.newPage({viewport: {width: 900, height: 1300}});
await page.goto(pathToFileURL(resolve(html)).href, {waitUntil: 'load'});
const wynik = await page.evaluate((strony) => {
  const arkusze = [...document.querySelectorAll('.sheet, .page')];
  const lista = strony ? strony.split(',').map(Number) : arkusze.map((_, i) => i + 1);
  const SEL = ['.dline', '.blankline', '.blank', '.box', '.field .val', '.fg .v', 'td.ex', '.ex', '.opt', '.chk', '.optlabel', '[contenteditable="true"]'];
  const out = [];
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : '');
  for (const n of lista) {
    const a = arkusze[n - 1];
    if (!a) continue;
    out.push(`===== @${n}`);
    for (const s of SEL) {
      const els = [...a.querySelectorAll(s)];
      if (!els.length) continue;
      els.forEach((el, k) => {
        if (s === '[contenteditable="true"]' && el.matches('.dline,.blankline,.blank,.box,.field .val,.fg .v,.ex,.optlabel')) return;
        if (s === '.ex' && el.matches('td')) return;
        // etykieta: poprzedni element z tekstem w tym samym wierszu/komórce lub nagłówek sekcji
        let lab = '';
        const cell = el.closest('td,th,.field,.fg,.opt,.box,.two > div,.sgc,.sg,div');
        if (cell && cell !== el) { const c = cell.cloneNode(true); c.querySelectorAll(s).forEach((x) => x.remove()); lab = txt(c).slice(0, 60); }
        if (!lab) { const tr = el.closest('tr'); if (tr) lab = txt(tr).slice(0, 60); }
        const sec = el.closest('.sheet, .page').querySelector('.sec h2, .sec');
        const wl = el.getAttribute('data-ph') || '';
        const ist = txt(el).slice(0, 40);
        const r = el.getBoundingClientRect();
        out.push(`${s} #${k} [${Math.round(r.width)}x${Math.round(r.height)}] lab="${lab}" ph="${wl.slice(0, 50)}" tekst="${ist}"`);
      });
    }
    void 0;
  }
  return out.join('\n');
}, strony || null);
console.log(wynik);
await browser.close();
