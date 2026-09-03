const fs = require('fs');
const L = require('../lib.js');
const { Document, Packer, FONT, C, makeHeader, makeFooter } = L;

const children = [...require('./content1.js'), ...require('./content2.js'), ...require('./content3.js')];

const doc = new Document({
  creator: 'EduPlaner 2026 · PCTP',
  title: 'Indywidualny Program Edukacyjno-Terapeutyczny (IPET) z WOPFU (ICF) — druk szkolny',
  description: 'EduPlaner2026-MJ-PCTP · IPET szkolny · druk do wypełnienia przez zespół',
  styles: { default: { document: { run: { font: FONT, size: 20, color: C.ink }, paragraph: { spacing: { line: 260 } } } } },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: { top: 1000, right: 1080, bottom: 900, left: 1080, header: 500, footer: 400 }
      }
    },
    headers: { default: makeHeader({ kind: 'IPET · szkoła', badge: 'IPET', tagline: 'z WOPFU (ICF) · szkoła · 2026' }) },
    footers: { default: makeFooter({ left: 'EduPlaner 2026 · PCTP · szkoła', badge: 'IPET' }) },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(process.argv[2] || 'EduPlaner2026_IPET_druk.docx', buf);
  console.log('zapisano', (buf.length / 1024).toFixed(1) + ' KB, bloków:', children.length);
});
