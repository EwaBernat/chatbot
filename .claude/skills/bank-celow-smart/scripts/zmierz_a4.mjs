/* Pomiar, czy każdy arkusz i każda karta mieszczą się na jednej stronie A4 pionowo.
 *
 * Arkusz, który nie mieści się na stronie, nie wysypuje budowania — po prostu
 * wychodzi z drukarki na dwóch kartkach, z kaflami rozciętymi w pół. Wychodzi
 * to na jaw dopiero przy drukarce, u nauczyciela. Dlatego po każdej zmianie
 * układu arkusza mierzymy, zamiast zakładać.
 *
 * Budżet strony: A4 to 210×297 mm; przy marginesie 9 mm z boku i 9 mm góra/dół
 * zostaje 192×279 mm, czyli 726×1054 px przy 96 dpi. Skrypt renderuje dokumenty
 * w trybie druku i sprawdza wysokość każdej sekcji `.zal`.
 *
 * Uruchomienie z katalogu eduplaner_przedszkole:
 *   node .claude/skills/bank-celow-smart/scripts/zmierz_a4.mjs
 *
 * Domyślnie mierzy cztery zeszyty konspektów; inne pliki podaje się argumentami.
 */
import path from 'node:path';
import fs from 'node:fs';
import { pathToFileURL } from 'node:url';

/* Playwright bywa zainstalowany globalnie, a nie obok tego skryptu — node szuka
   modułów przy pliku, nie przy katalogu roboczym, więc sprawdzamy kilka miejsc
   zamiast wymagać dowiązania node_modules w konkretnym katalogu. */
async function wczytajPlaywright() {
  const kandydaci = [
    'playwright',
    path.resolve('node_modules/playwright/index.js'),
    '/opt/node22/lib/node_modules/playwright/index.js',
    '/usr/lib/node_modules/playwright/index.js',
    ...(process.env.NODE_PATH || '').split(path.delimiter).filter(Boolean)
      .map(d => path.join(d, 'playwright/index.js')),
  ];
  for (const k of kandydaci) {
    try {
      const m = await import(k.startsWith('/') ? pathToFileURL(k).href : k);
      return m.chromium ?? m.default?.chromium;
    } catch { /* następny kandydat */ }
  }
  console.error('Nie znalazłem playwrighta. Zainstaluj: npm i playwright');
  process.exit(2);
}
const chromium = await wczytajPlaywright();

/* Przeglądarka: gotowa w obrazie, jeśli jest; inaczej ta, którą zna playwright. */
const PRZEGLADARKA = fs.existsSync('/opt/pw-browsers/chromium')
  ? { executablePath: '/opt/pw-browsers/chromium' } : {};

const MM = 96 / 25.4;
const SZEROKOSC = Math.round(192 * MM);   // 726 px
const WYSOKOSC  = Math.round(279 * MM);   // 1054 px

const podane = process.argv.slice(2);
const domyslne = ['Konspekty_3-4_lata', 'Konspekty_5_lat',
                  'Konspekty_6_lat', 'Konspekty_uzupelnienia'];
const pliki = (podane.length ? podane : domyslne)
  .map(p => path.resolve(p.endsWith('.html') ? p : p + '.html'))
  .filter(p => { const jest = fs.existsSync(p);
                 if (!jest) console.log('pomijam, nie ma pliku:', p);
                 return jest; });

if (!pliki.length) { console.log('Nie ma czego mierzyć.'); process.exit(2); }

const b = await chromium.launch(PRZEGLADARKA);
const p = await b.newPage({ viewport: { width: SZEROKOSC, height: 1200 } });
// Fonty z sieci blokujemy: pomiar ma być powtarzalny także bez internetu,
// a dokument ma zapasowy Arial o zbliżonych metrykach.
await p.route('**://fonts.*/**', r => r.abort());
await p.emulateMedia({ media: 'print' });

const wszystkie = [];
for (const plik of pliki) {
  await p.goto('file://' + plik, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(600);
  const z = await p.evaluate(() => [...document.querySelectorAll('section.zal')].map(s => {
    const t = s.querySelector('[class^=kd-],[class*=" kd-"],.zal-siatka');
    return {
      h: Math.round(s.getBoundingClientRect().height),
      rodzaj: s.classList.contains('pomoc') ? 'karta pomocy'
            : t ? (t.className.match(/kd-\w+|zal-siatka/) || ['arkusz'])[0] : 'arkusz',
      skad: ((s.querySelector('.zal-s') || {}).textContent || '').trim(),
    };
  }));
  wszystkie.push(...z.map(x => ({ ...x, plik: path.basename(plik) })));
}
await b.close();

const grupy = {};
for (const x of wszystkie) (grupy[x.rodzaj] ||= []).push(x);

console.log(`\nbudżet strony: ${SZEROKOSC} × ${WYSOKOSC} px (A4 pionowo, margines 9 mm)\n`);
for (const [rodzaj, lista] of Object.entries(grupy).sort()) {
  const h = lista.map(x => x.h).sort((a, b) => a - b);
  const nad = lista.filter(x => x.h > WYSOKOSC);
  console.log(
    rodzaj.padEnd(13),
    'n=' + String(lista.length).padStart(3),
    'min', String(h[0]).padStart(4),
    'mediana', String(h[h.length >> 1]).padStart(4),
    'max', String(h[h.length - 1]).padStart(4),
    '| nad stronę:', nad.length);
  for (const x of nad.slice(0, 5)) console.log(`      ✗ ${x.h} px — ${x.skad} (${x.plik})`);
}

const nad = wszystkie.filter(x => x.h > WYSOKOSC);
console.log('\n' + '═'.repeat(60));
if (nad.length) {
  console.log(`NAD STRONĘ WYCHODZI ${nad.length} z ${wszystkie.length} arkuszy.`);
  console.log('Zwykle pomaga: więcej kolumn w siatce (_kolumny w karty_druk.py),');
  console.log('krótszy wstęp arkusza albo mniej kafli na jednym arkuszu.');
  process.exit(1);
}
console.log(`WSZYSTKIE ${wszystkie.length} ARKUSZY MIEŚCI SIĘ NA JEDNEJ STRONIE A4.`);
