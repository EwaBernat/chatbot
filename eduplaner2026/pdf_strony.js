#!/usr/bin/env node
/* PDF ze strony eduplaner2026.pl
 *
 * Robi z żywej strony jeden plik PDF: do wysłania mailem, wydrukowania na
 * spotkanie z dyrektorem albo dołączenia do oferty. Nie jest to zrzut ekranu —
 * tekst w PDF-ie zostaje tekstem, można go zaznaczyć i przeszukać.
 *
 *   node pdf_strony.js
 *   node pdf_strony.js index.html --wyjscie oferta.pdf
 *   node pdf_strony.js --poziomo --szerokosc 1400
 *
 * Opcje:
 *   --wyjscie <plik>      nazwa pliku wynikowego (domyślnie eduplaner2026-strona.pdf)
 *   --format <A4|A3|Letter>   rozmiar kartki (domyślnie A4)
 *   --poziomo             kartka w orientacji poziomej
 *   --szerokosc <px>      szerokość okna przeglądarki (domyślnie 1240)
 *   --ciemny              wersja w trybie ciemnym
 *   --bez-katalogow       nie dokładaj pozycji ukrytych w oknach katalogów
 *   --bez-ekranow         nie rozwijaj wycieczki po ekranach aplikacji
 *
 * Strona jest jednoplikowa i wiele treści dokłada skrypt, więc przed drukiem
 * trzeba ją przygotować: przewinąć (obrazy wczytują się leniwie), wyciągnąć
 * pozycje z okien katalogów, rozłożyć wycieczkę po ekranach na wszystkie
 * ekrany naraz i rozwinąć pytania w sekcji „Zanim zamówisz". Bez tego PDF
 * pokazywałby trzy szkolenia z dziesięciu i jeden ekran z siedmiu.
 */

'use strict';
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

/* ---------- argumenty ------------------------------------------------ */

const args = process.argv.slice(2);
const opcja = (nazwa, domyslna) => {
  const i = args.indexOf('--' + nazwa);
  return i >= 0 && args[i + 1] && !args[i + 1].startsWith('--') ? args[i + 1] : domyslna;
};
const flaga = nazwa => args.includes('--' + nazwa);

const zrodlo = path.resolve(args.find(a => !a.startsWith('--') &&
  args[args.indexOf(a) - 1] !== '--wyjscie' &&
  args[args.indexOf(a) - 1] !== '--format' &&
  args[args.indexOf(a) - 1] !== '--szerokosc') || 'index.html');

const wyjscie   = path.resolve(opcja('wyjscie', 'eduplaner2026-strona.pdf'));
const format    = opcja('format', 'A4');
const szerokosc = parseInt(opcja('szerokosc', '1240'), 10);
const poziomo   = flaga('poziomo');
const ciemny    = flaga('ciemny');

if (!fs.existsSync(zrodlo)) {
  console.error('Nie ma pliku: ' + zrodlo);
  process.exit(2);
}

/* Szerokość kartki w pikselach CSS przy 96 dpi — z tego liczy się pomniejszenie,
   żeby układ z ekranu 1240 px zmieścił się na kartce bez ucinania boków. */
const KARTKI = { A4: [794, 1123], A3: [1123, 1587], Letter: [816, 1056] };
if (!KARTKI[format]) {
  console.error('Nieznany format: ' + format + '. Dostępne: ' + Object.keys(KARTKI).join(', '));
  process.exit(2);
}
const [w, h] = KARTKI[format];
const szerokoscKartki = poziomo ? h : w;
const skala = Math.min(2, Math.max(0.1, +(szerokoscKartki / szerokosc).toFixed(3)));

/* ---------- przygotowanie strony do druku ---------------------------- */

const STYL_DRUKU = `
  /* Pasek, który na ekranie jedzie za czytelnikiem, w PDF-ie powtarzałby się
     na każdej stronie albo zasłaniał treść. Zostaje raz, na górze. */
  .site-header { position: static !important; }
  * { animation: none !important; transition: none !important; scroll-behavior: auto !important; }
  .sheet, .vbox, .do-gory, [data-motyw], .theme-toggle { display: none !important; }

  /* Karty, tabele i zdjęcia nie mają się łamać w połowie między kartkami. */
  .offer, .tier, .buy-card, .stage, figure, details, .trust-strip li,
  .faq-grid details, .prices, .poz-side { break-inside: avoid; page-break-inside: avoid; }
  section { break-inside: auto; }
  h2, h3 { break-after: avoid; page-break-after: avoid; }

  /* Rozłożona wycieczka po ekranach: jeden ekran pod drugim, na całą szerokość.
     Klasa tour-view musi zostać — bez niej przepadają style zrzutów i lupka
     rozdyma się do czarnego koła. Dokładamy tour-druk obok, nie zamiast. */
  .tour { display: block !important; }
  #tour-list, .nav-btns { display: none !important; }
  .tour-view.tour-druk { display: grid; gap: 30px; }
  .tour-view.tour-druk .shot { margin: 0; }
  .tour-view.tour-druk .zoom { display: none !important; }
`;

async function przygotuj(page) {
  // 1. Przewiń całą stronę, żeby doczytały się obrazy z loading="lazy".
  await page.evaluate(async () => {
    const krok = window.innerHeight * 0.8;
    for (let y = 0; y < document.body.scrollHeight; y += krok) {
      window.scrollTo(0, y);
      await new Promise(r => setTimeout(r, 60));
    }
    window.scrollTo(0, 0);
  });

  // 2. Pełna oferta: wyciągnij pozycje z okien katalogów do sekcji na stronie.
  if (!flaga('bez-katalogow')) {
    const kategorie = [
      ['szkolenie', 'lista-szkolen'],
      ['broszura', 'lista-broszur'],
      ['pomoc', 'lista-pomocy']
    ];
    for (const [typ, lista] of kategorie) {
      const dodane = await page.evaluate(async ([typ, lista]) => {
        const cel = document.getElementById(lista);
        if (!cel) return 0;
        location.hash = '#katalog-' + typ;
        await new Promise(r => setTimeout(r, 350));
        const siatka = document.getElementById('kat-siatka');
        const ile = siatka ? siatka.children.length : 0;
        if (ile) cel.innerHTML = siatka.innerHTML;      // wraz z kartami spoza strony
        location.hash = '';
        await new Promise(r => setTimeout(r, 250));
        return ile;
      }, [typ, lista]);
      if (dodane) console.log('  ' + typ + ': ' + dodane + ' pozycji w PDF-ie');
    }
  }

  // 3. Wycieczka po ekranach: wszystkie ekrany jeden pod drugim.
  if (!flaga('bez-ekranow')) {
    const ekranow = await page.evaluate(async () => {
      const lista = document.getElementById('tour-list');
      const widok = document.getElementById('tour-view');
      if (!lista || !widok) return 0;
      const taby = [...lista.querySelectorAll('button')];
      const kawalki = [];
      for (const t of taby) {
        t.click();
        await new Promise(r => setTimeout(r, 220));
        kawalki.push(widok.innerHTML);
      }
      if (!kawalki.length) return 0;
      widok.classList.add('tour-druk');
      widok.innerHTML = kawalki.join('');
      return kawalki.length;
    });
    if (ekranow) console.log('  ekrany aplikacji: ' + ekranow + ' zrzutów w PDF-ie');
  }

  // 4. Rozwiń pytania — w PDF-ie nikt nie kliknie, żeby zobaczyć odpowiedź.
  await page.evaluate(() => {
    document.querySelectorAll('details').forEach(d => { d.open = true; });
  });

  // 5. Doczekaj czcionek i obrazów; bez tego pierwsze strony wychodzą puste.
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(async () => {
    const obrazy = [...document.images].filter(i => !i.complete);
    await Promise.all(obrazy.map(i => new Promise(r => {
      i.addEventListener('load', r, { once: true });
      i.addEventListener('error', r, { once: true });
      setTimeout(r, 4000);
    })));
  });
}

/* ---------- druk ------------------------------------------------------ */

(async () => {
  console.log('Składam PDF z ' + path.basename(zrodlo) + ' …');

  const browser = await chromium.launch({
    executablePath: process.env.CHROMIUM_PATH || undefined
  });
  const page = await browser.newPage({ viewport: { width: szerokosc, height: 1400 } });

  await page.emulateMedia({
    media: 'screen',                       // strona nie ma stylów @media print
    colorScheme: ciemny ? 'dark' : 'light',
    reducedMotion: 'reduce'
  });

  await page.goto('file://' + zrodlo, { waitUntil: 'networkidle' });
  await page.addStyleTag({ content: STYL_DRUKU });
  await przygotuj(page);

  await page.pdf({
    path: wyjscie,
    format: format,
    landscape: poziomo,
    printBackground: true,
    scale: skala,
    margin: { top: '10mm', bottom: '12mm', left: '8mm', right: '8mm' },
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate:
      '<div style="width:100%;font-size:8px;color:#6A6377;font-family:Arial,sans-serif;' +
      'padding:0 12mm;display:flex;justify-content:space-between">' +
      '<span>EduPlaner 2026 · PCTP Koszalin · eduplaner2026.pl</span>' +
      '<span class="pageNumber"></span>/<span class="totalPages"></span></div>'
  });

  await browser.close();

  const kb = Math.round(fs.statSync(wyjscie).size / 1024);
  console.log('Zapisano ' + path.relative(process.cwd(), wyjscie) + ' (' + kb + ' KB, ' +
    format + (poziomo ? ' poziomo' : '') + ', pomniejszenie ' + skala + ')');
})().catch(e => {
  console.error('Nie udało się złożyć PDF-u: ' + e.message);
  process.exit(1);
});
