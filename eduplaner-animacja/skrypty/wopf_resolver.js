/* Wspólny „tłumacz” kroków z public/wopf-dane.json na elementy oryginalnego arkusza WOPF.
   Używany przez skrypt wypełniający (Node + Chromium) i przez animację (Remotion) — jeden opis danych, dwa zastosowania. */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.WopfResolver = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  function norm(t) { return (t || '').replace(/\s+/g, ' ').trim(); }
  function strona(doc, n) { return doc.querySelectorAll('.page')[n - 1] || null; }
  function znajdz(doc, k) {
    if (k.meta !== undefined) {
      return Array.from(doc.querySelectorAll('.pmeta')).map(function (pm) { return pm.querySelectorAll('.mv')[k.meta]; }).filter(Boolean);
    }
    var pg = strona(doc, k.s); if (!pg) return [];
    if (k.pole) {
      var fl = Array.from(pg.querySelectorAll('.f .fl')).find(function (l) { return norm(l.textContent) === k.pole; });
      var fv = fl && fl.parentElement.querySelector('.fv'); return fv ? [fv] : [];
    }
    if (k.bx) {
      var c = Array.from(pg.querySelectorAll('.checks .c')).find(function (x) { var sp = x.querySelectorAll('span')[1]; return sp && norm(sp.textContent).indexOf(k.bx) === 0; });
      var bx = c && c.querySelector('.bx'); return bx ? [bx] : [];
    }
    if (k.tab !== undefined) {
      var t = pg.querySelectorAll('table')[k.tab]; var tr = t && t.tBodies[0] && t.tBodies[0].rows[k.w - 1];
      var td = tr && tr.cells[k.k - 1]; return td ? [td] : [];
    }
    if (k.wt) {
      var rows = Array.from(pg.querySelectorAll('table tbody tr'));
      var r = rows.find(function (tr) { return Array.from(tr.cells).some(function (c) { return norm(c.textContent).indexOf(k.wt) === 0; }); });
      var cell = r && r.cells[k.k - 1]; return cell ? [cell] : [];
    }
    if (k.qtab !== undefined) {
      var q = doc.querySelector('table.qtab'); var qr = q && q.tBodies[0].rows[k.qtab - 1];
      var qc = qr && qr.cells[1]; return qc ? [qc] : [];
    }
    if (k.ed) {
      var ta = Array.from(pg.querySelectorAll('.ta')).find(function (x) { var tl = x.querySelector('.tl'); return tl && norm(tl.textContent).indexOf(k.ed) === 0; });
      var ed = ta && ta.querySelector('.ed'); return ed ? [ed] : [];
    }
    if (k.lvl !== undefined) { var l = pg.querySelectorAll('.lvl-x')[k.lvl]; return l ? [l] : []; }
    return [];
  }
  /* zaznaczenie pola .bx dokładnie tak, jak robi to funkcja selBx() z arkusza */
  function zaznaczBx(el, on) {
    el.textContent = on ? '✓' : '';
    el.style.background = on ? '#2D1B69' : '#fff'; el.style.color = '#fff'; el.style.fontSize = '8px'; el.style.textAlign = 'center'; el.style.lineHeight = '11px';
  }
  function zastosuj(doc, k, tekst) {
    var els = znajdz(doc, k);
    els.forEach(function (el) {
      if (k.bx) { zaznaczBx(el, true); return; }
      el.textContent = tekst === undefined ? k.tekst : tekst;
      el.dataset.man = '1'; // pole wpisane ręcznie — automat arkusza go nie nadpisze
      if (k.qtab !== undefined) el.dispatchEvent(new Event('input', { bubbles: true }));
    });
    return els.length;
  }
  return { znajdz: znajdz, zastosuj: zastosuj, zaznaczBx: zaznaczBx, norm: norm };
});
