/* ============================================================================
 * generuj.js — generator kompletu druków nadzoru pedagogicznego (.docx)
 * Użycie:  node generuj.js [katalog_wyjściowy]   (domyślnie ./out)
 *          node generuj.js out NP-03 NP-04       (tylko wybrane druki)
 * ========================================================================== */
const fs = require("fs");
const path = require("path");
const { Packer } = require("docx");
const S = require("./styl.js");
const W = require("./wspolne.js");

const DRUKI = fs
  .readdirSync(path.join(__dirname, "druki"))
  .filter((f) => f.endsWith(".js"))
  .sort()
  .map((f) => require(path.join(__dirname, "druki", f)));

const OUT = path.resolve(process.argv[2] || path.join(__dirname, "out"));
const FILTR = process.argv.slice(3).map((s) => s.toUpperCase());

fs.mkdirSync(OUT, { recursive: true });

(async () => {
  const wybrane = FILTR.length ? DRUKI.filter((d) => FILTR.includes(d.kod)) : DRUKI;
  for (const druk of wybrane) {
    const doc = S.dokument({
      modul: W.MODUL,
      kodDruku: druk.kod,
      tytul: druk.tytul,
      children: druk.build(),
    });
    const buf = await Packer.toBuffer(doc);
    const cel = path.join(OUT, druk.plik);
    fs.writeFileSync(cel, buf);
    console.log(`✓ ${druk.kod}  ${druk.plik}  (${(buf.length / 1024).toFixed(0)} kB)`);
  }
  console.log(`\nGotowe: ${wybrane.length} druk(ów) w ${OUT}`);
})().catch((e) => {
  console.error("BŁĄD:", e.message);
  process.exit(1);
});
