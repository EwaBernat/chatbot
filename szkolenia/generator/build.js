const G = require('./gen.js');
const { Document, Packer, Paragraph, AlignmentType, BorderStyle, Header, Footer, PageNumber,
        LevelFormat, fs, t, PURPLE, ORANGE, FONT } = G;

const children = []
  .concat(require('./c1.js'), require('./c2.js'), require('./c3.js'), require('./c4.js'),
          require('./c5.js'), require('./c6.js'), require('./c7.js'), require('./c8.js'));

const header = new Header({ children: [ new Paragraph({
  spacing: { after: 60 },
  border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [
    t('PCTP · EduPlaner 2026', { size: 15, color: ORANGE, bold: true }),
    t('     Scenariusz szkolenia: dokumentacja przedszkolna 2026/2027', { size: 15, color: '8A8A8A' }),
  ],
})]});

const footer = new Footer({ children: [ new Paragraph({
  alignment: AlignmentType.CENTER,
  spacing: { before: 60 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: 'D6D1E4', space: 4 } },
  children: [
    new (require('docx').TextRun)({ font: FONT, size: 15, color: '8A8A8A',
      children: ['Strona ', PageNumber.CURRENT, ' z ', PageNumber.TOTAL_PAGES] }),
  ],
})]});

const doc = new Document({
  creator: 'EduPlaner 2026 · PCTP',
  title: 'Scenariusz szkolenia — dokumentacja przedszkolna 2026/2027',
  description: 'Kompleksowe szkolenie rady pedagogicznej: podstawy prawne, ICF, metryczka, KPOF, obserwacja pogłębiona, WOPF, IPET, cele SMART, ewaluacja.',
  styles: {
    default: {
      document: { run: { font: FONT, size: 20, color: '1A1A1A' },
                  paragraph: { spacing: { line: 264 } } },
    },
  },
  numbering: {
    config: [
      { reference: 'kropki', levels: [{ level: 0, format: LevelFormat.BULLET, text: '▪',
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 340, hanging: 220 } },
                 run: { color: ORANGE, font: FONT, size: 18 } } }] },
      { reference: 'kroki', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.',
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 380, hanging: 380 } },
                 run: { color: ORANGE, font: FONT, bold: true } } }] },
    ],
  },
  sections: [{
    properties: { page: { margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } },
    headers: { default: header },
    footers: { default: footer },
    children,
  }],
});

Packer.toBuffer(doc).then(b => {
  const out = '/home/user/chatbot/szkolenia/Scenariusz_szkolenia_dokumentacja_przedszkolna_2026-2027.docx';
  fs.writeFileSync(out, b);
  console.log('OK ->', out, (b.length / 1024).toFixed(0) + ' KB', '| elementów:', children.length);
});
