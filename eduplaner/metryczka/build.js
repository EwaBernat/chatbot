const fs = require('fs');
const L = require('../lib.js');
const { Document, Packer, FONT, C, makeHeader, makeFooter } = L;

const children = require('./content.js');

const doc = new Document({
  creator: 'EduPlaner 2026 · PCTP',
  title: 'Metryczka dziecka — przedszkole 2026',
  description: 'EduPlaner2026-MJ-PCTP · Metryczka dziecka · karta danych i dokumentacji',
  styles: { default: { document: { run: { font: FONT, size: 20, color: C.ink }, paragraph: { spacing: { line: 260 } } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1000, right: 1080, bottom: 900, left: 1080, header: 500, footer: 400 }
      }
    },
    headers: { default: makeHeader({ kind: 'Metryczka · przedszkole', badge: 'METRYCZKA', tagline: 'karta danych dziecka · rok szkolny 2026 / 27' }) },
    footers: { default: makeFooter({ left: 'EduPlaner 2026 · PCTP · pedagog specjalny mgr Mirosława Ewa Jurczyszyn', badge: 'Metryczka' }) },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(process.argv[2] || 'Metryczka_dziecka_przedszkole_2026.docx', buf);
  console.log('zapisano', (buf.length / 1024).toFixed(1) + ' KB, bloków:', children.length);
});
