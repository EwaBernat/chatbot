#!/usr/bin/env node
/* Gotowość do publikacji — czyta pliki źródłowe, nie renderuje strony.
 *
 * straznik.js mierzy stronę w przeglądarce: kontrast, kolejność nagłówków,
 * wagę obrazów. Ten skrypt sprawdza rzecz inną i równie ważną: czy w kodzie
 * nie zostały puste miejsca, atrapy i odnośniki do plików, których nie ma.
 * Uruchamiaj tuż przed wysłaniem strony na serwer.
 *
 *   node gotowosc.js [katalog] [--json]
 *
 * Kod wyjścia: 0 gdy nie ma blokad, 1 gdy są.
 */

'use strict';
const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);
const json = args.includes('--json');
const katalog = path.resolve(args.find(a => !a.startsWith('--')) || '.');

const uwagi = [];
const dodaj = (poziom, obszar, tresc, gdzie, szczegol) =>
  uwagi.push({ poziom, obszar, tresc, gdzie: gdzie || '', szczegol: szczegol || '' });
const blokada = (o, t, g, s) => dodaj('BLOKADA', o, t, g, s);
const ostrzez = (o, t, g, s) => dodaj('OSTRZEŻENIE', o, t, g, s);
const info = (o, t, g, s) => dodaj('INFO', o, t, g, s);

/* ---------- zbieranie plików ---------------------------------------- */

const POMIN = new Set(['node_modules', '.git', 'dist', '__pycache__']);

function pliki(dir, rozsz, wynik) {
  wynik = wynik || [];
  let wpisy;
  try { wpisy = fs.readdirSync(dir, { withFileTypes: true }); } catch (e) { return wynik; }
  for (const w of wpisy) {
    if (w.name.startsWith('.') || POMIN.has(w.name)) continue;
    const p = path.join(dir, w.name);
    if (w.isDirectory()) pliki(p, rozsz, wynik);
    else if (rozsz.test(w.name)) wynik.push(p);
  }
  return wynik;
}

const strony = pliki(katalog, /\.html$/i);
const wzgledna = p => path.relative(katalog, p) || path.basename(p);

if (!strony.length) {
  console.error('Nie znalazłem żadnego pliku .html w ' + katalog);
  process.exit(2);
}

/* ---------- czytanie ------------------------------------------------- */

const tresci = new Map();
strony.forEach(p => tresci.set(p, fs.readFileSync(p, 'utf8')));

const bezKomentarzy = s => s.replace(/<!--[\s\S]*?-->/g, '');
const bezSkryptow = s => s.replace(/<script[\s\S]*?<\/script>/gi, '')
                          .replace(/<style[\s\S]*?<\/style>/gi, '');

/* ---------- 1. puste miejsca w dokumentach --------------------------- */

for (const [p, s] of tresci) {
  const nazwa = wzgledna(p);

  const puste = (s.match(/class="puste"/g) || []).length;
  if (puste) {
    blokada('dane', puste + '× puste miejsce w dokumencie', nazwa,
      'Znacznik class="puste" oznacza dane, których nikt jeszcze nie podał. ' +
      'Dokument z takim miejscem nie może zostać opublikowany.');
  }

  /* Liczy się znacznik, nie sam zwrot: „do uzupełnienia z dokumentacji" bywa
     normalną treścią broszury i nie jest brakiem w projekcie. */
  const douzup = (s.match(/do-uzupelnienia|\(do uzupełnienia\)/gi) || []).length;
  if (douzup) {
    blokada('dane', douzup + '× oznaczenie „do uzupełnienia"', nazwa,
      'Najczęściej NIP, REGON, adres rejestrowy albo termin płatności.');
  }

  if (/projekt dokumentu, nie dokument obowiązujący/i.test(s)) {
    blokada('prawo', 'Dokument jest oznaczony jako projekt', nazwa,
      'Regulamin i polityka prywatności muszą przejść przez prawnika, a baner ' +
      '„projekt dokumentu" trzeba zdjąć dopiero po jego akceptacji.');
  }

  const todo = (s.match(/TODO|FIXME|XXX:/g) || []).length;
  if (todo) ostrzez('kod', todo + '× TODO w kodzie', nazwa);

  if (/lorem ipsum|przykładowy tekst|placeholder text/i.test(s)) {
    blokada('treść', 'Tekst zastępczy w treści', nazwa);
  }
}

/* ---------- 2. odnośniki do plików, których nie ma -------------------- */

const brakujace = new Map();      // ścieżka → strony, które o nią proszą
const zewnetrzne = new Set();

function zglosPlik(zStrony, cel) {
  if (!cel || /^(#|mailto:|tel:|javascript:|data:)/i.test(cel)) return;
  if (/^https?:\/\//i.test(cel)) {
    try { zewnetrzne.add(new URL(cel).host); } catch (e) { /* nieczytelny adres */ }
    return;
  }
  const czysty = cel.split(/[?#]/)[0];
  if (!czysty) return;
  const pelna = path.resolve(path.dirname(zStrony), czysty);
  if (!fs.existsSync(pelna)) {
    const k = path.relative(katalog, pelna);
    if (!brakujace.has(k)) brakujace.set(k, new Set());
    brakujace.get(k).add(wzgledna(zStrony));
  }
}

for (const [p, s] of tresci) {
  const tekst = bezKomentarzy(s);

  // href i src w znacznikach
  const re = /\b(?:href|src|poster)\s*=\s*["']([^"']+)["']/gi;
  let m;
  while ((m = re.exec(bezSkryptow(tekst)))) zglosPlik(p, m[1]);

  // ścieżki do obrazów wpisane w danych JavaScriptu: plik:"img/..."
  const reJs = /["'](img\/[^"']+\.(?:webp|jpg|jpeg|png|svg|avif))["']/gi;
  while ((m = reJs.exec(tekst))) zglosPlik(p, m[1]);
}

for (const [plik, gdzie] of brakujace) {
  blokada('pliki', 'Brak pliku: ' + plik, [...gdzie].join(', '),
    'Strona prosi o plik, którego nie ma w projekcie. Na serwerze da to pustą ramkę albo 404.');
}

/* ---------- 3. martwe odnośniki i atrapy ----------------------------- */

for (const [p, s] of tresci) {
  const nazwa = wzgledna(p);
  const tekst = bezSkryptow(bezKomentarzy(s));

  /* href="#" bez żadnego zaczepu data- to odnośnik donikąd. Z zaczepem
     (data-link, data-video, data-poz) obsługuje go skrypt i to jest w porządku. */
  const kotwice = tekst.match(/<a\b[^>]*href\s*=\s*["']#["'][^>]*>/gi) || [];
  const martwe = kotwice.filter(a => !/\bdata-[a-z-]+\s*=/i.test(a)).length;
  if (martwe) blokada('sprzedaż', martwe + '× odnośnik prowadzący donikąd (href="#")', nazwa,
    'Przycisk, który nic nie robi, kosztuje więcej zaufania niż brak przycisku.');

  if (/<form\b(?![^>]*\baction=)/i.test(tekst)) {
    ostrzez('backend', 'Formularz bez atrybutu action', nazwa,
      'Zamówienie idzie przez mailto: albo nigdzie. Na telefonie bez skonfigurowanej ' +
      'poczty przepada po cichu — patrz references/backend.md w skillu eduplaner-sklep.');
  }

  /* Tylko tam, gdzie „na zapytanie" stoi w miejscu kwoty — nie w zdaniu
     „odpowiedź na zapytanie" w polityce prywatności. */
  const zapytanie = (tekst.match(/(?:data-price=|>\s*|["'])na zapytanie(?:["']|\s*<)/gi) || []).length;
  if (zapytanie) ostrzez('sprzedaż', zapytanie + '× cena „na zapytanie"', nazwa,
    'Każda taka pozycja to klient, który odkłada decyzję.');
}

/* ---------- 4. komplet dokumentów prawnych --------------------------- */

const WYMAGANE = [
  ['regulamin.html', 'Regulamin sklepu'],
  ['polityka-prywatnosci.html', 'Polityka prywatności'],
  ['formularz-odstapienia.html', 'Formularz odstąpienia']
];
/* Tylko dla katalogu, który jest korzeniem serwisu. Uruchomiony na podkatalogu
   (np. broszury/) nie ma prawa wymagać regulaminu. */
const korzen = fs.existsSync(path.join(katalog, 'index.html'));
if (korzen) WYMAGANE.forEach(([plik, nazwa]) => {
  if (!fs.existsSync(path.join(katalog, plik))) {
    blokada('prawo', 'Brak dokumentu: ' + nazwa, plik,
      'Sprzedaż konsumencka w Polsce wymaga wszystkich trzech, dostępnych przed zakupem.');
  }
});

/* ---------- 5. sekrety w kodzie -------------------------------------- */

const SEKRETY = [
  [/\b(sk|pk)_(live|test)_[A-Za-z0-9]{16,}/, 'klucz operatora płatności'],
  [/\bAKIA[0-9A-Z]{16}\b/, 'klucz AWS'],
  [/\bghp_[A-Za-z0-9]{20,}\b/, 'token GitHuba'],
  [/["']?(?:password|haslo|hasło|secret|api[_-]?key)["']?\s*[:=]\s*["'][^"'\s]{8,}["']/i, 'hasło lub klucz w kodzie']
];
for (const [p, s] of tresci) {
  SEKRETY.forEach(([re, opis]) => {
    if (re.test(s)) blokada('bezpieczeństwo', 'Możliwy ' + opis + ' w kodzie strony', wzgledna(p),
      'Klucze trzymaj po stronie serwera, nigdy w pliku, który pobiera przeglądarka.');
  });
}

/* ---------- 6. zasoby zewnętrzne ------------------------------------- */

if (zewnetrzne.size) {
  info('bezpieczeństwo', 'Zasoby z zewnętrznych źródeł: ' + [...zewnetrzne].join(', '), '',
    'Każde źródło to zależność, która może zniknąć, zwolnić albo wymusić baner cookies.');
}

/* ---------- 7. obrazy nieużywane ------------------------------------- */

const uzywane = new Set();
for (const [p, s] of tresci) {
  const re = /["']([^"']*\.(?:webp|jpg|jpeg|png|svg|avif))["']/gi;
  let m;
  while ((m = re.exec(s))) {
    const czysty = m[1].split(/[?#]/)[0];
    uzywane.add(path.resolve(path.dirname(p), czysty));
  }
}
const obrazy = pliki(path.join(katalog, 'img'), /\.(webp|jpg|jpeg|png|svg|avif)$/i);
const nieuzywane = obrazy.filter(o => !uzywane.has(path.resolve(o)) && !/\.(jpg|jpeg)$/i.test(o));
if (nieuzywane.length) {
  info('pliki', nieuzywane.length + ' obraz(ów) nieużywanych na żadnej stronie',
    nieuzywane.map(wzgledna).slice(0, 6).join(', '),
    'Pliki .jpg pomijam — to źródła. Reszta niepotrzebnie idzie na serwer.');
}

/* ---------- raport --------------------------------------------------- */

if (json) {
  const bl = uwagi.filter(u => u.poziom === 'BLOKADA').length;
  console.log(JSON.stringify({ katalog, stron: strony.length, uwagi }, null, 2));
  process.exit(bl ? 1 : 0);
}

const KRESKA = '─'.repeat(74);
const kolejnosc = { BLOKADA: 0, OSTRZEŻENIE: 1, INFO: 2 };
uwagi.sort((a, b) => kolejnosc[a.poziom] - kolejnosc[b.poziom] || a.obszar.localeCompare(b.obszar));

console.log('\n' + KRESKA);
console.log('GOTOWOŚĆ DO PUBLIKACJI  ·  ' + path.basename(katalog) + '  ·  ' + strony.length + ' stron(y)');
console.log(KRESKA + '\n');

if (!uwagi.length) {
  console.log('Nic do zgłoszenia. Strona jest gotowa do wysłania na serwer.\n');
} else {
  let poprzedni = '';
  uwagi.forEach(u => {
    if (u.poziom !== poprzedni) { console.log('\n' + u.poziom + '\n'); poprzedni = u.poziom; }
    console.log('  · [' + u.obszar + '] ' + u.tresc);
    if (u.gdzie) console.log('    gdzie: ' + u.gdzie);
    if (u.szczegol) console.log('    ' + u.szczegol);
  });
}

const bl = uwagi.filter(u => u.poziom === 'BLOKADA').length;
const os = uwagi.filter(u => u.poziom === 'OSTRZEŻENIE').length;
console.log('\n' + KRESKA);
console.log('Blokady: ' + bl + '   Ostrzeżenia: ' + os);
console.log(KRESKA);
console.log('Ten skrypt czyta pliki źródłowe. Wygląd, kontrast i dostępność sprawdza');
console.log('straznik.js — uruchom oba przed publikacją, w trybie jasnym i ciemnym.\n');

process.exit(bl ? 1 : 0);
