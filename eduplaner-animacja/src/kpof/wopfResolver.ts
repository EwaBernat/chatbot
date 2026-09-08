/** Port TS wspólnego „tłumacza” kroków (skrypty/wopf_resolver.js) — te same reguły co w skrypcie wypełniającym. */
export type WopfKrok = {
  faza?: string;
  s?: number;
  meta?: number;
  pole?: string;
  bx?: string;
  tab?: number;
  w?: number;
  k?: number;
  wt?: string;
  qtab?: number;
  ed?: string;
  lvl?: number;
  tekst?: string;
};

const norm = (t: string | null | undefined) => (t ?? '').replace(/\s+/g, ' ').trim();
const strona = (root: ParentNode, n: number) => root.querySelectorAll('.page')[n - 1] ?? null;

export function znajdz(root: ParentNode, k: WopfKrok): HTMLElement[] {
  if (k.meta !== undefined) {
    return Array.from(root.querySelectorAll('.pmeta')).map((pm) => pm.querySelectorAll<HTMLElement>('.mv')[k.meta as number]).filter(Boolean);
  }
  const pg = strona(root, k.s ?? 1);
  if (!pg) return [];
  if (k.pole) {
    const fl = Array.from(pg.querySelectorAll<HTMLElement>('.f .fl')).find((l) => norm(l.textContent) === k.pole);
    const fv = fl?.parentElement?.querySelector<HTMLElement>('.fv');
    return fv ? [fv] : [];
  }
  if (k.bx) {
    const c = Array.from(pg.querySelectorAll<HTMLElement>('.checks .c')).find((x) => {
      const sp = x.querySelectorAll('span')[1];
      return sp ? norm(sp.textContent).indexOf(k.bx as string) === 0 : false;
    });
    const bx = c?.querySelector<HTMLElement>('.bx');
    return bx ? [bx] : [];
  }
  if (k.tab !== undefined) {
    const t = pg.querySelectorAll('table')[k.tab];
    const tr = t?.tBodies[0]?.rows[(k.w ?? 1) - 1];
    const td = tr?.cells[(k.k ?? 1) - 1];
    return td ? [td] : [];
  }
  if (k.wt) {
    const rows = Array.from(pg.querySelectorAll<HTMLTableRowElement>('table tbody tr'));
    const r = rows.find((tr) => Array.from(tr.cells).some((c) => norm(c.textContent).indexOf(k.wt as string) === 0));
    const cell = r?.cells[(k.k ?? 1) - 1];
    return cell ? [cell] : [];
  }
  if (k.qtab !== undefined) {
    const q = root.querySelector<HTMLTableElement>('table.qtab');
    const qr = q?.tBodies[0]?.rows[k.qtab - 1];
    const qc = qr?.cells[1];
    return qc ? [qc] : [];
  }
  if (k.ed) {
    const ta = Array.from(pg.querySelectorAll<HTMLElement>('.ta')).find((x) => norm(x.querySelector('.tl')?.textContent).indexOf(k.ed as string) === 0);
    const ed = ta?.querySelector<HTMLElement>('.ed');
    return ed ? [ed] : [];
  }
  if (k.lvl !== undefined) {
    const l = pg.querySelectorAll<HTMLElement>('.lvl-x')[k.lvl];
    return l ? [l] : [];
  }
  return [];
}

/** Zaznaczenie pola .bx dokładnie tak, jak robi to funkcja selBx() z arkusza. */
export function zaznaczBx(el: HTMLElement, on: boolean) {
  el.textContent = on ? '✓' : '';
  el.style.background = on ? '#2D1B69' : '#fff';
  el.style.color = '#fff';
  el.style.fontSize = '8px';
  el.style.textAlign = 'center';
  el.style.lineHeight = '11px';
}
