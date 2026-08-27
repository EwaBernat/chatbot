// Renderuje broszurę A4 do PDF-u z zachowaniem marginesów i fontów marki.
//
// Użycie:  node zloz_pdf.js Broszura_DRUK.html Broszura_DRUK.pdf
//
// Dwie rzeczy, które łatwo tu zepsuć — obie opisane w references/pulapki_pdf.md:
//  1. reguła @media (max-width:...) bez słowa `screen` działa też przy druku
//     i nadpisuje marginesy strony,
//  2. bez `await document.fonts.ready` PDF wychodzi krojami zastępczymi.


// Playwright bywa zainstalowany w katalogu roboczym, a nie przy skillu.
function wczytajPlaywright(){
  try { return require('playwright'); } catch(e) {}
  try { return require(require('path').join(process.cwd(),'node_modules','playwright')); } catch(e) {}
  console.error('Brak playwright. Uruchom w katalogu projektu:  npm install playwright');
  process.exit(1);
}
const {chromium}=wczytajPlaywright();
const WEJSCIE = process.argv[2] || 'Broszura_DRUK.html';
const WYJSCIE = process.argv[3] || WEJSCIE.replace(/\.html$/, '.pdf');
const PRZEGLADARKA = process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

(async () => {
  const b = await chromium.launch(
    require('fs').existsSync(PRZEGLADARKA) ? { executablePath: PRZEGLADARKA } : {}
  );
  const p = await b.newPage();
  await p.goto('file://' + require('path').resolve(WEJSCIE), { waitUntil: 'load' });

  // Fonty osadzone jako data: URI ładują się natychmiast, ale renderowanie
  // startuje dopiero po ich rozpakowaniu — bez tego PDF łapie kroje systemowe.
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(2000);

  const kroje = await p.evaluate(() =>
    [...new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family))]);
  console.log('fonty załadowane:', kroje.join(' | ') || 'ŻADEN — sprawdź osadzenie!');
  if (!kroje.length) { await b.close(); process.exit(1); }

  await p.pdf({
    path: WYJSCIE,
    preferCSSPageSize: true,          // rozmiar bierzemy z @page w CSS
    printBackground: true,            // bez tego znikają tła ramek i okładka
    margin: { top: '0', right: '0', bottom: '0', left: '0' },
  });
  console.log('zapisano', WYJSCIE);
  await b.close();
})();
