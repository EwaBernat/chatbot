/**
 * Kopiuje prawdziwe zrzuty druków z ../zrzuty do public/zrzuty,
 * bo Remotion czyta pliki statyczne tylko z katalogu public/.
 * Uruchamiane automatycznie przez `npm start` i `npm run render`.
 */
import { cp, mkdir, readdir } from 'node:fs/promises';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const tu = dirname(fileURLToPath(import.meta.url));
const zrodlo = join(tu, '..', '..', 'zrzuty');
const cel = join(tu, '..', 'public', 'zrzuty');

await mkdir(cel, { recursive: true });
await cp(zrodlo, cel, { recursive: true });
const pliki = await readdir(cel);
console.log(`✓ skopiowano ${pliki.length} zrzutów → public/zrzuty`);
