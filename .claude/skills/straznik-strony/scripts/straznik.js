#!/usr/bin/env node
/**
 * Strażnik strony — kontroler zgodności prawnej, dostępności, czytelności,
 * wizualnej i sprzedażowej strony internetowej.
 *
 *   node straznik.js <plik-lub-URL> [--json] [--tylko bledy]
 *
 * Kod wyjścia: 0 = brak błędów, 1 = są błędy.
 */
const path = require('path');
const fs = require('fs');

let chromium;
try { ({ chromium } = require('playwright')); }
catch (e) {
  console.error('Brak Playwrighta. Zainstaluj: npm i -D playwright');
  process.exit(2);
}

const args = process.argv.slice(2);
const cel = args.find(a => !a.startsWith('--'));
const jakoJson = args.includes('--json');
const tylkoBledy = args.includes('--tylko') && args[args.indexOf('--tylko') + 1] === 'bledy';
if (!cel) { console.error('Podaj plik HTML albo adres URL.'); process.exit(2); }

const adres = /^https?:\/\//.test(cel) ? cel : 'file://' + path.resolve(cel);
const katalog = /^https?:\/\//.test(cel) ? null : path.dirname(path.resolve(cel));

const uwagi = [];
const dodaj = (poziom, obszar, tresc, szczegol) =>
  uwagi.push({ poziom, obszar, tresc, szczegol: szczegol || '' });
const blad = (o, t, s) => dodaj('BŁĄD', o, t, s);
const ostrzez = (o, t, s) => dodaj('OSTRZEŻENIE', o, t, s);
const uzupelnij = (o, t, s) => dodaj('DO UZUPEŁNIENIA', o, t, s);

/* ---------- kontrast wg WCAG ---------- */
function luminancja(rgb) {
  const k = rgb.map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
  return 0.2126 * k[0] + 0.7152 * k[1] + 0.0722 * k[2];
}
function kontrast(a, b) {
  const la = luminancja(a), lb = luminancja(b);
  return (Math.max(la, lb) + 0.05) / (Math.min(la, lb) + 0.05);
}
/* Zwraca kolor jako RGB. Kolor półprzezroczysty nakładamy na tło, bo inaczej
   porównywalibyśmy wartość, której użytkownik nigdy nie widzi. */
function naRgb(s, pod) {
  s = String(s);
  const m = s.match(/-?\d*\.?\d+/g);
  if (!m) return null;
  let v = m.slice(0, 3).map(Number);
  const zeroDoJeden = /^color\(/.test(s) || v.every(x => x <= 1);
  if (zeroDoJeden) v = v.map(x => Math.round(x * 255));
  const alfa = m.length > 3 ? Number(m[3]) : 1;
  if (alfa < 1) {
    const tlo = pod || [255, 255, 255];
    v = v.map((x, i) => Math.round(x * alfa + tlo[i] * (1 - alfa)));
  }
  return v;
}

(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
  const kontekst = await b.newContext({ viewport: { width: 1440, height: 1000 } });
  const p = await kontekst.newPage();
  const bledyJs = [];
  p.on('pageerror', e => bledyJs.push(e.message));

  try { await p.goto(adres, { waitUntil: 'networkidle', timeout: 45000 }); }
  catch (e) { console.error('Nie udało się otworzyć strony: ' + e.message); process.exit(2); }
  await p.waitForTimeout(600);

  const d = await p.evaluate(() => {
    const tekst = document.body.innerText;
    const widoczny = el => { const s = getComputedStyle(el); return s.display !== 'none' && s.visibility !== 'hidden'; };
    const nazwaDostepna = el =>
      (el.getAttribute('aria-label') || el.getAttribute('title') ||
       el.textContent || (el.querySelector('img') ? el.querySelector('img').alt : '')).trim();

    /* nagłówki */
    const naglowki = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')]
      .map(h => ({ poziom: +h.tagName[1], tekst: h.textContent.trim().slice(0, 60) }));

    /* obrazy */
    const obrazy = [...document.querySelectorAll('img')].map(i => ({
      src: (i.getAttribute('src') || '').slice(0, 120),
      alt: i.getAttribute('alt'),
      lazy: i.getAttribute('loading') === 'lazy',
      wDom: Math.round(i.getBoundingClientRect().width),
      wNat: i.naturalWidth,
      nadFold: i.getBoundingClientRect().top < window.innerHeight,
      dataUri: (i.getAttribute('src') || '').startsWith('data:')
    }));

    /* formularze */
    const formularze = [...document.querySelectorAll('form')].map(f => {
      const pola = [...f.querySelectorAll('input,select,textarea')].filter(e => e.type !== 'hidden');
      return {
        action: f.getAttribute('action'),
        submit: (() => { const s = f.querySelector('[type=submit],button:not([type=button])'); return s ? s.textContent.trim() : null; })(),
        checkboxy: [...f.querySelectorAll('input[type=checkbox]')].map(c => ({
          id: c.id || c.name || '',
          domyslnie: c.defaultChecked,
          etykieta: (c.closest('label') || document.querySelector('label[for="' + c.id + '"]') || {}).textContent
            ? (c.closest('label') || document.querySelector('label[for="' + c.id + '"]')).textContent.trim().slice(0, 160) : ''
        })),
        bezEtykiety: pola.filter(e => e.type !== 'checkbox' && e.type !== 'radio').filter(e => {
          if (e.getAttribute('aria-label')) return false;
          if (e.id && document.querySelector('label[for="' + CSS.escape(e.id) + '"]')) return false;
          return !e.closest('label');
        }).map(e => e.id || e.name || e.tagName.toLowerCase())
      };
    });

    /* linki i przyciski */
    const linki = [...document.querySelectorAll('a')];
    const martwe = linki.filter(a => (a.getAttribute('href') || '') === '#').length;
    const bezNazwy = [...document.querySelectorAll('a,button')]
      .filter(widoczny).filter(el => !nazwaDostepna(el)).length;

    /* cele dotykowe */
    /* WCAG 2.2 wyłącza z wymogu wielkości celu odnośniki osadzone w zdaniu —
       tam rozmiar wyznacza tekst i powiększanie go psułoby akapit. */
    const wZdaniu = el => {
      if (getComputedStyle(el).display !== 'inline') return false;
      const rodzic = el.parentElement;
      return !!rodzic && /^(P|LI|SPAN|TD|H1|H2|H3|H4|LABEL)$/.test(rodzic.tagName) &&
             rodzic.textContent.trim().length > el.textContent.trim().length + 12;
    };
    const male = [...document.querySelectorAll('a,button,input[type=checkbox],input[type=radio],select')]
      .filter(widoczny).filter(el => !wZdaniu(el))
      .map(el => { const r = el.getBoundingClientRect(); return { w: r.width, h: r.height, t: nazwaDostepna(el).slice(0, 30) }; })
      .filter(r => r.w > 0 && r.h > 0 && (r.w < 24 || r.h < 24));

    /* czytelność tekstu ciągłego */
    const akapity = [...document.querySelectorAll('p,li')].filter(widoczny)
      .filter(e => e.textContent.trim().length > 60).slice(0, 200);
    const czyt = akapity.map(e => {
      const s = getComputedStyle(e), r = e.getBoundingClientRect();
      const px = parseFloat(s.fontSize);
      const lh = s.lineHeight === 'normal' ? px * 1.2 : parseFloat(s.lineHeight);
      return { px, lh: +(lh / px).toFixed(2), znaki: Math.round(r.width / (px * 0.5)), kolor: s.color, tag: e.tagName };
    });

    /* kontrast — próbka tekstu na jego realnym tle */
    /* Tło szukamy w górę drzewa. Gdy po drodze trafimy na gradient albo obraz,
       kontrastu nie da się policzyć rzetelnie — lepiej pominąć element, niż
       zgłosić fałszywy alarm. To samo dotyczy sekcji malowanych pseudoelementem. */
    function tlo(el) {
      let e = el;
      while (e && e !== document.documentElement) {
        const s = getComputedStyle(e);
        if (s.backgroundImage && s.backgroundImage !== 'none') return null;
        for (const pseudo of ['::before', '::after']) {
          const ps = getComputedStyle(e, pseudo);
          if (ps.content !== 'none' && ps.position === 'absolute' &&
              ((ps.backgroundImage && ps.backgroundImage !== 'none') ||
               (ps.backgroundColor && !/rgba\(0, 0, 0, 0\)|transparent/.test(ps.backgroundColor)))) return null;
        }
        if (s.backgroundColor && !/rgba\(0, 0, 0, 0\)|transparent/.test(s.backgroundColor)) return s.backgroundColor;
        e = e.parentElement;
      }
      return getComputedStyle(document.body).backgroundColor || 'rgb(255,255,255)';
    }
    const probki = [...document.querySelectorAll('p,li,h1,h2,h3,span,a,td,label')].filter(widoczny)
      .filter(e => e.textContent.trim().length > 12).slice(0, 300).map(e => {
        const s = getComputedStyle(e), px = parseFloat(s.fontSize);
        const bg = tlo(e); if (!bg) return null;
        return { kolor: s.color, tlo: bg, px, duzy: px >= 24 || (px >= 19 && +s.fontWeight >= 700),
                 tekst: e.textContent.trim().slice(0, 42) };
      }).filter(Boolean);

    /* skrypty zewnętrzne */
    const skrypty = [...document.querySelectorAll('script[src]')].map(s => s.src)
      .filter(u => !u.startsWith('file:')).map(u => { try { return new URL(u).hostname; } catch (e) { return u; } });
    const style = [...document.querySelectorAll('link[rel=stylesheet]')].map(l => l.href)
      .filter(u => !u.startsWith('file:')).map(u => { try { return new URL(u).hostname; } catch (e) { return u; } });
    const ramki = [...document.querySelectorAll('iframe')].map(f => f.src).filter(Boolean);

    return {
      title: document.title, lang: document.documentElement.lang,
      meta: {
        opis: (document.querySelector('meta[name=description]') || {}).content || null,
        canonical: !!document.querySelector('link[rel=canonical]'),
        og: [...document.querySelectorAll('meta[property^="og:"]')].map(m => m.getAttribute('property')),
        viewport: !!document.querySelector('meta[name=viewport]')
      },
      naglowki, obrazy, formularze, martwe, bezNazwy, male, czyt, probki,
      skrypty, style, ramki, bledyJs: [],
      tekst: tekst.toLowerCase(),
      dlugoscTekstu: tekst.replace(/\s+/g, ' ').length,
      linkiTekst: linki.map(a => (a.textContent || '').trim().toLowerCase() + '|' + (a.getAttribute('href') || '')),
      fokus: [...document.styleSheets].some(ss => { try { return [...ss.cssRules].some(r => /:focus-visible|:focus/.test(r.selectorText || '')); } catch (e) { return false; } }),
      ruch: [...document.styleSheets].some(ss => { try { return [...ss.cssRules].some(r => /prefers-reduced-motion/.test(r.conditionText || '')); } catch (e) { return false; } })
    };
  });

  /* ---------- przewijanie w poziomie ---------- */
  const szerokosci = [390, 768, 1440];
  const przewijanie = [];
  for (const w of szerokosci) {
    await p.setViewportSize({ width: w, height: 900 });
    await p.waitForTimeout(250);
    const r = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
    if (r.sw > r.cw + 1) przewijanie.push(w + ' px (treść szersza o ' + (r.sw - r.cw) + ' px)');
  }
  await b.close();

  /* =================== OCENA =================== */
  const t = d.tekst;
  const maLink = (frazy) => d.linkiTekst.some(l => frazy.some(f => l.includes(f)));

  /* --- 1. PRAWO --- */
  if (!maLink(['regulamin'])) blad('prawo', 'Brak linku do regulaminu', 'Regulamin musi być dostępny przed zakupem, najlepiej w stopce i przy formularzu.');
  if (!maLink(['polityka prywatn', 'polityka-prywatn', 'prywatnoś'])) blad('prawo', 'Brak linku do polityki prywatności', 'Obowiązek informacyjny z art. 13 RODO.');
  if (!maLink(['odstąpieni', 'odstapieni', 'zwrot'])) ostrzez('prawo', 'Brak linku do formularza odstąpienia', 'Wzór oświadczenia musi być łatwo dostępny i wysyłany z potwierdzeniem zamówienia.');

  if (!/nip[:\s]*[\d\- ]{10,}/.test(t)) uzupelnij('prawo', 'Brak numeru NIP sprzedawcy', 'Samo pole na NIP kupującego w formularzu to co innego.');
  if (!/regon[:\s]*\d/.test(t)) uzupelnij('prawo', 'Brak numeru REGON sprzedawcy');
  if (!/\b\d{2}-\d{3}\b/.test(t)) uzupelnij('prawo', 'Brak pełnego adresu rejestrowego', 'Sama nazwa miasta nie wystarcza — potrzebna ulica i kod pocztowy.');
  if (!/tel:|telefon|\+48|\b\d{3}[ -]?\d{3}[ -]?\d{3}\b/.test(t)) blad('prawo', 'Brak numeru telefonu', 'Telefon do szybkiego kontaktu jest obowiązkowy przy sprzedaży konsumenckiej.');
  if (!/@[\w.-]+\.\w+/.test(t)) blad('prawo', 'Brak adresu e-mail sprzedawcy');
  if (!/wszelkie prawa zastrzeżone|prawa autorskie|©/.test(t)) ostrzez('prawo', 'Brak noty o prawach autorskich w stopce');

  /* checkout */
  const zForm = d.formularze.filter(f => f.submit);
  if (!zForm.length) {
    ostrzez('sprzedaż', 'Na stronie nie ma formularza zamówienia', 'Jeśli strona ma sprzedawać, to jest brak podstawowy.');
  }
  zForm.forEach(f => {
    const s = (f.submit || '').toLowerCase();
    const bezplatny = /pokaz|demo|zapisz się na bezpłatn|umów/.test(s);
    if (!bezplatny && !/obowiązkiem zapłaty|obowiazkiem zaplaty|kupuję i płacę|zamawiam i płacę/.test(s))
      blad('prawo', 'Przycisk zamówienia nie informuje o obowiązku zapłaty', 'Jest: „' + f.submit + '". Wymagane: „Zamawiam z obowiązkiem zapłaty".');
    if (!f.checkboxy.length && !bezplatny)
      blad('prawo', 'Formularz zamówienia nie ma żadnych checkboxów zgody', 'Brakuje co najmniej akceptacji regulaminu.');
    f.checkboxy.forEach(c => {
      if (c.domyslnie) blad('prawo', 'Checkbox zaznaczony domyślnie: ' + (c.id || '(bez id)'), 'Zgoda musi być czynnością świadomą.');
      if (!c.etykieta) ostrzez('dostępność', 'Checkbox bez etykiety: ' + (c.id || '(bez id)'));
    });
    const maCyfrowa = f.checkboxy.some(c => /odstąpieni|odstapieni|treści cyfrow|tracę prawo/.test(c.etykieta.toLowerCase()));
    const sprzedajePliki = /pdf|broszur|e-book|plik do pobrania|treść cyfrow/.test(t);
    if (sprzedajePliki && !maCyfrowa)
      blad('prawo', 'Brak zgody na dostarczenie treści cyfrowej przed terminem odstąpienia',
        'Bez niej konsument może pobrać plik i zażądać zwrotu w ciągu 14 dni.');
    if (f.action === null && /mailto/.test(String(f.action)) === false)
      ostrzez('bezpieczeństwo', 'Formularz nie ma atrybutu action', 'Jeśli zamówienie idzie przez mailto:, na telefonie bez poczty przepadnie bez śladu.');
    if (f.bezEtykiety.length)
      blad('dostępność', 'Pola formularza bez etykiety: ' + f.bezEtykiety.join(', '), 'Sam placeholder nie jest etykietą — znika po wpisaniu tekstu.');
  });

  /* Omnibus i opinie */
  /* Szukamy śladu realnej obniżki przy cenie, a nie samego słowa „obniżka" —
     regulamin opisujący obowiązek Omnibus nie jest promocją. */
  const obnizka = /-\s?\d{1,2}\s?%|było[:\s]+\d+[\d ,]*\s?zł|zamiast\s+\d+[\d ,]*\s?zł|cena regularna|przecena/.test(t);
  if (obnizka && !/najniższa cena/.test(t))
    blad('prawo', 'Obniżka bez informacji o najniższej cenie z 30 dni', 'Wymóg dyrektywy Omnibus.');
  if (/opinie|opinia|recenzj|referencj/.test(t) && !/weryfik/.test(t))
    ostrzez('prawo', 'Opinie bez informacji o weryfikacji', 'Trzeba napisać, czy i jak sprawdzasz, że pochodzą od kupujących.');

  /* cookies */
  const sledzace = ['google-analytics.com','googletagmanager.com','connect.facebook.net','hotjar.com','clarity.ms','doubleclick.net']
    .filter(h => d.skrypty.some(s => s.includes(h)) || d.ramki.some(r => r.includes(h)));
  if (sledzace.length && !/cookie|ciasteczk/.test(t))
    blad('prawo', 'Skrypty śledzące bez banera cookies: ' + sledzace.join(', '), 'Zgoda musi być zebrana przed załadowaniem skryptu.');
  if (!sledzace.length && !/cookie|ciasteczk/.test(t))
    dodaj('INFO', 'prawo', 'Brak skryptów śledzących — baner cookies nie jest wymagany', 'Warto napisać to wprost w polityce prywatności.');

  /* --- 2. DOSTĘPNOŚĆ --- */
  if (!d.lang) blad('dostępność', 'Brak atrybutu lang', 'Czytnik ekranu nie wie, w jakim języku czytać.');
  const h1 = d.naglowki.filter(h => h.poziom === 1).length;
  if (h1 === 0) blad('dostępność', 'Brak nagłówka H1');
  if (h1 > 1) ostrzez('dostępność', 'Więcej niż jeden H1 (' + h1 + ')');
  let poprzedni = 0, przeskoki = [];
  d.naglowki.forEach(h => { if (poprzedni && h.poziom > poprzedni + 1) przeskoki.push('H' + poprzedni + ' → H' + h.poziom + ' („' + h.tekst + '")'); poprzedni = h.poziom; });
  if (przeskoki.length) ostrzez('dostępność', 'Przeskoki w hierarchii nagłówków', przeskoki.slice(0, 3).join('; '));

  const bezAlt = d.obrazy.filter(i => i.alt === null);
  if (bezAlt.length) blad('dostępność', bezAlt.length + ' obraz(y) bez atrybutu alt', bezAlt.map(i => i.src.slice(0, 50)).join(', '));
  if (d.bezNazwy) blad('dostępność', d.bezNazwy + ' link(ów) lub przycisk(ów) bez dostępnej nazwy', 'Czytnik przeczyta „link" i nic więcej.');
  if (d.male.length) ostrzez('dostępność', d.male.length + ' cel(e) dotykowe mniejsze niż 24×24 px',
    d.male.slice(0, 4).map(m => '„' + m.t + '" ' + Math.round(m.w) + '×' + Math.round(m.h)).join('; '));
  if (!d.fokus) ostrzez('dostępność', 'Brak stylu widocznego fokusu klawiatury');
  if (!d.ruch) ostrzez('dostępność', 'Brak reguły prefers-reduced-motion', 'Animacje powinny się wyłączać dla osób wrażliwych na ruch.');

  const zleKontrasty = [];
  d.probki.forEach(s => {
    const tl = naRgb(s.tlo, [255, 255, 255]);
    const k = naRgb(s.kolor, tl);
    if (!k || !tl) return;
    const w = kontrast(k, tl), prog = s.duzy ? 3 : 4.5;
    if (w < prog) zleKontrasty.push('„' + s.tekst + '" ' + w.toFixed(2) + ':1 (wymagane ' + prog + ':1)');
  });
  if (zleKontrasty.length) blad('dostępność', zleKontrasty.length + ' element(ów) o zbyt niskim kontraście', [...new Set(zleKontrasty)].slice(0, 5).join('; '));

  /* --- 3. CZYTELNOŚĆ --- */
  const male16 = d.czyt.filter(c => c.px < 16).length;
  if (male16) ostrzez('czytelność', male16 + ' bloków tekstu mniejszych niż 16 px');
  const ciasne = d.czyt.filter(c => c.lh < 1.5).length;
  if (ciasne > d.czyt.length * 0.3) ostrzez('czytelność', 'Interlinia poniżej 1,5 w ' + ciasne + ' blokach tekstu');
  const dlugie = d.czyt.filter(c => c.znaki > 85).length;
  const krotkie = d.czyt.filter(c => c.znaki < 40 && c.tag === 'P').length;
  if (dlugie) ostrzez('czytelność', dlugie + ' bloków o wierszu dłuższym niż 85 znaków');
  if (krotkie > 3) ostrzez('czytelność', krotkie + ' bloków o wierszu krótszym niż 40 znaków', 'Łamanie co trzy słowa męczy tak samo jak zbyt długi wiersz.');

  /* --- 4. WIZUALNIE I WYDAJNOŚĆ --- */
  przewijanie.forEach(w => blad('wizualnie', 'Poziome przewijanie przy ' + w));
  if (!d.meta.viewport) blad('wizualnie', 'Brak meta viewport', 'Strona nie będzie działać na telefonie.');
  const leniwe = d.obrazy.filter(i => !i.nadFold && !i.lazy && !i.dataUri);
  if (leniwe.length) ostrzez('wizualnie', leniwe.length + ' obraz(ów) poniżej pierwszego ekranu bez loading="lazy"');
  const przeskalowane = d.obrazy.filter(i => i.wNat && i.wDom && i.wNat > i.wDom * 2.2);
  if (przeskalowane.length) ostrzez('wizualnie', przeskalowane.length + ' obraz(ów) znacznie większych niż miejsce wyświetlania',
    przeskalowane.slice(0, 3).map(i => i.src.split('/').pop() + ' ' + i.wNat + 'px → ' + i.wDom + 'px').join('; '));

  if (katalog) {
    d.obrazy.filter(i => !i.dataUri && i.src).forEach(i => {
      const f = path.join(katalog, decodeURIComponent(i.src.split('?')[0]));
      if (!fs.existsSync(f)) return;
      const kb = Math.round(fs.statSync(f).size / 1024);
      if (kb > 120) ostrzez('wizualnie', 'Obraz cięższy niż 120 KB: ' + path.basename(f) + ' (' + kb + ' KB)');
      if (!/\.webp$/i.test(f)) ostrzez('wizualnie', 'Obraz nie jest w formacie WebP: ' + path.basename(f));
    });
  }

  /* --- 5. SEO --- */
  if (!d.title) blad('seo', 'Brak tytułu strony');
  else if (d.title.length > 65) ostrzez('seo', 'Tytuł dłuższy niż 65 znaków (' + d.title.length + ')');
  if (!d.meta.opis) blad('seo', 'Brak meta description');
  if (!d.meta.canonical) ostrzez('seo', 'Brak linku canonical');
  ['og:title','og:description','og:image','og:url'].forEach(x => { if (!d.meta.og.includes(x)) ostrzez('seo', 'Brak tagu ' + x, 'Link wklejony w mediach społecznościowych pokaże się bez podglądu.'); });

  /* --- 6. SPRZEDAŻ --- */
  if (d.martwe) blad('sprzedaż', d.martwe + ' odnośnik(ów) prowadzących donikąd (href="#")');
  const naZapytanie = (t.match(/na zapytanie/g) || []).length;
  if (naZapytanie) ostrzez('sprzedaż', naZapytanie + '× cena „na zapytanie"', 'Kupujący instytucjonalny potrzebuje kwoty do planu finansowego; bez niej odkłada decyzję.');
  const wkrotce = (t.match(/wkrótce|w przygotowaniu|coming soon/g) || []).length;
  if (wkrotce > 3) ostrzez('sprzedaż', wkrotce + '× „wkrótce" na stronie', 'Powyżej kilku sztuk strona zaczyna wyglądać na niegotową.');
  if (!/opinia|opinie|referencj|rekomendacj|poleca|korzysta z/.test(t))
    uzupelnij('sprzedaż', 'Brak dowodu, że ktoś już z tego korzysta', 'Nazwa placówki, funkcja osoby i konkretne zdanie robią więcej niż cała sekcja opisu.');
  if (!/zł|pln/.test(t)) blad('sprzedaż', 'Na stronie nie ma ani jednej kwoty');
  if (d.dlugoscTekstu > 12000) ostrzez('sprzedaż', 'Bardzo dużo tekstu (' + d.dlugoscTekstu + ' znaków)', 'Powyżej mniej więcej 7 000 znaków strona główna zaczyna męczyć.');

  /* --- 7. BEZPIECZEŃSTWO --- */
  const zaufane = ['fonts.googleapis.com','fonts.gstatic.com','cdnjs.cloudflare.com','cdn.jsdelivr.net'];
  const obce = [...new Set([...d.skrypty, ...d.style])].filter(h => !zaufane.includes(h));
  if (obce.length) ostrzez('bezpieczeństwo', 'Zasoby z zewnętrznych źródeł: ' + obce.join(', '), 'Każde zewnętrzne źródło to nowy powód, żeby potrzebować banera cookies.');
  if (bledyJs.length) blad('bezpieczeństwo', 'Błędy JavaScriptu na stronie', bledyJs.slice(0, 3).join(' | '));

  /* =================== RAPORT =================== */
  const kolejnosc = { 'BŁĄD': 0, 'OSTRZEŻENIE': 1, 'DO UZUPEŁNIENIA': 2, 'INFO': 3 };
  uwagi.sort((a, b2) => kolejnosc[a.poziom] - kolejnosc[b2.poziom] || a.obszar.localeCompare(b2.obszar, 'pl'));
  const licz = pz => uwagi.filter(u => u.poziom === pz).length;

  if (jakoJson) {
    console.log(JSON.stringify({ adres: cel, tytul: d.title, uwagi,
      podsumowanie: { bledy: licz('BŁĄD'), ostrzezenia: licz('OSTRZEŻENIE'), doUzupelnienia: licz('DO UZUPEŁNIENIA') } }, null, 2));
  } else {
    const kreska = '─'.repeat(74);
    console.log('\n' + kreska + '\nSTRAŻNIK STRONY  ·  ' + (d.title || cel) + '\n' + kreska);
    const znak = { 'BŁĄD': '✖', 'OSTRZEŻENIE': '▲', 'DO UZUPEŁNIENIA': '□', 'INFO': 'ℹ' };
    let ostatni = null;
    uwagi.filter(u => !tylkoBledy || u.poziom === 'BŁĄD').forEach(u => {
      if (u.poziom !== ostatni) { console.log('\n' + u.poziom + '\n'); ostatni = u.poziom; }
      console.log('  ' + znak[u.poziom] + ' [' + u.obszar + '] ' + u.tresc);
      if (u.szczegol) console.log('      ' + u.szczegol);
    });
    console.log('\n' + kreska);
    console.log('Błędy: ' + licz('BŁĄD') + '   Ostrzeżenia: ' + licz('OSTRZEŻENIE') + '   Do uzupełnienia: ' + licz('DO UZUPEŁNIENIA'));
    console.log(kreska);
    console.log('Kontroler sprawdza to, co mierzalne. Nie oceni, czy treść regulaminu pasuje');
    console.log('do tego, co sprzedajesz, czy zdjęcia mają licencję ani czy opinie są prawdziwe.');
    console.log('Dokumenty prawne przed publikacją sprawdza prawnik.\n');
  }
  process.exit(licz('BŁĄD') ? 1 : 0);
})();
