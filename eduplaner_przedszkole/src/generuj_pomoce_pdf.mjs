/* PDF z zeszytów pomocy dydaktycznych — po jednej karcie na stronę A4 pionowo.
   Fonty z sieci blokujemy celowo: PDF ma powstawać tak samo szybko i tak samo
   wyglądać także wtedy, gdy CDN jest niedostępny (dokument ma zapasowy Arial).
   Wymaga playwrighta (npm i playwright). Bez niego to samo osiąga się
   z przeglądarki: otwórz zeszyt i Ctrl+P → „Zapisz jako PDF", format A4
   pionowo — karty i tak wychodzą po jednej na stronę.
   Uruchomienie: node src/generuj_pomoce_pdf.mjs */
let chromium;
try {
  ({ chromium } = await import('playwright'));
} catch {
  console.error('Brak playwrighta. Zainstaluj: npm i playwright\n' +
                'albo wydrukuj zeszyt do PDF z przeglądarki (Ctrl+P, A4 pionowo).');
  process.exit(1);
}

const KORZEN = '/home/user/chatbot/eduplaner_przedszkole/';
const ZESZYTY = [
  ['Pomoce_dydaktyczne_3-4_lata.html', 'Pomoce_dydaktyczne_3-4_lata.pdf'],
  ['Pomoce_dydaktyczne_5_lat.html',    'Pomoce_dydaktyczne_5_lat.pdf'],
  ['Pomoce_dydaktyczne_6_lat.html',    'Pomoce_dydaktyczne_6_lat.pdf'],
];

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
for (const [zrodlo, cel] of ZESZYTY) {
  const p = await b.newPage();
  await p.route('**://fonts.*/**', r => r.abort());
  await p.goto('file://' + KORZEN + zrodlo, { waitUntil: 'domcontentloaded' });
  await p.pdf({ path: KORZEN + cel, format: 'A4', printBackground: true });
  await p.close();
  console.log('zapisano:', cel);
}
await b.close();
