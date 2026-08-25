import {continueRender, delayRender, staticFile} from 'remotion';

// Kroje pisma leżą w public/fonty (podzbiór latin-ext, z polskimi znakami),
// więc film renderuje się identycznie bez dostępu do internetu.
export const FIGTREE = 'Figtree, Arial, sans-serif';
export const SANS = '"Source Sans 3", Arial, sans-serif';

let zaladowane = false;

export const zaladujFonty = () => {
  if (zaladowane || typeof document === 'undefined') return;
  zaladowane = true;
  const uchwyt = delayRender('Ładowanie krojów pisma');
  const styl = document.createElement('style');
  styl.textContent = `
    @font-face{font-family:'Figtree';src:url('${staticFile('fonty/Figtree-800.woff2')}') format('woff2');font-weight:100 900;font-display:block}
    @font-face{font-family:'Source Sans 3';src:url('${staticFile('fonty/SourceSans3-400.woff2')}') format('woff2');font-weight:100 900;font-display:block}
  `;
  document.head.appendChild(styl);
  Promise.all([
    document.fonts.load('800 60px Figtree'),
    document.fonts.load('400 30px "Source Sans 3"'),
    document.fonts.load('600 30px "Source Sans 3"'),
  ])
    .then(() => continueRender(uchwyt))
    .catch(() => continueRender(uchwyt));
};
