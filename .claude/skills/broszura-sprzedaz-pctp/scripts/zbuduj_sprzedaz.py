#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Składa komplet plików sprzedażowych z gotowego PDF-u broszury.

Wejście : Echolalia_DRUK.pdf  + struktura.json (mapa rozdziałów na strony)
Wyjście : PDF główny z metadanymi i zakładkami, próbka, załączniki do druku,
          okładka jako PNG oraz zrzuty stron do strony sprzedażowej.
"""
import json, io, os, sys
import pymupdf

ZRODLO   = sys.argv[1] if len(sys.argv) > 1 else 'Echolalia_DRUK.pdf'
STRUKT   = 'struktura.json'
WYNIK    = 'Echolalia_i_rozumienie_jej_funkcji.pdf'
KATALOG  = 'sprzedaz'

META = {
 'title':    'Echolalia i rozumienie jej funkcji przez nauczycieli, terapeutów i rodziców',
 'author':   'mgr Mirosława Jurczyszyn',
 'subject':  'Dostosowania i zintegrowane działania w szkole i placówkach. Siedem mechanizmów '
             'echolalii z oceną siły dowodów, dziesięć ćwiczeń, karta uzgodnień zespołu.',
 'keywords': 'echolalia, autyzm, spektrum autyzmu, pedagogika specjalna, IPET, dostosowania, '
             'terapia komunikacji, logopedia, nauczyciel, rodzic, PCTP Koszalin',
 'creator':  'Pomorskie Centrum Terapii Pedagogicznej, Koszalin',
 'producer': 'PCTP Koszalin — EduPlaner2026-MJ-PCTP',
}

os.makedirs(KATALOG, exist_ok=True)
d = pymupdf.open(ZRODLO)
print('wczytano %s — %d stron' % (ZRODLO, d.page_count))

# ── 1. metadane ────────────────────────────────────────────────────────
d.set_metadata(META)

# ── 2. zakładki nawigacyjne ────────────────────────────────────────────
struktura = json.load(io.open(STRUKT, encoding='utf-8'))
spis = [[poz['poziom'] + 1, poz['tytul'], min(poz['str'], d.page_count)] for poz in struktura]
d.set_toc(spis)
print('zakładek: %d' % len(spis))

# ── 3. otwieranie z panelem zakładek ───────────────────────────────────
d.set_pagemode('UseOutlines')
d.set_pagelayout('SinglePage')

d.save(WYNIK, garbage=4, deflate=True, clean=True)
print('zapisano %s — %.1f MB' % (WYNIK, os.path.getsize(WYNIK) / 1048576))

# ── 4. próbka dla kupujących ───────────────────────────────────────────
STRONY_PROBKI = [0, 1, 2, 3, 5]          # okładka, redakcyjna, licencja, spis, przykładowa
probka = pymupdf.open()
for n in STRONY_PROBKI:
    probka.insert_pdf(d, from_page=n, to_page=n)
for strona in probka:
    strona.insert_textbox(
        pymupdf.Rect(0, strona.rect.height - 30, strona.rect.width, strona.rect.height - 8),
        'FRAGMENT BEZPŁATNY · pełna publikacja liczy %d stron' % d.page_count,
        fontsize=8, align=pymupdf.TEXT_ALIGN_CENTER, color=(0.42, 0.39, 0.47))
probka.set_metadata({**META, 'title': META['title'] + ' — fragment bezpłatny'})
probka.save(os.path.join(KATALOG, 'probka_5_stron.pdf'), garbage=4, deflate=True)
print('próbka: %d stron' % probka.page_count)

# ── 5. załączniki do druku ─────────────────────────────────────────────
def strona_z_tekstem(fraza, od=4):
    """Szuka od strony `od`, żeby pominąć spis treści, gdzie tytuły też występują."""
    for n in range(od, d.page_count):
        if fraza.lower() in d[n].get_text().lower():
            return n
    return None

# frazy dobrane tak, by występowały wyłącznie na stronie z danym materiałem
ZALACZNIKI = [
    ('Możliwe wartości',        'zalacznik_1_arkusz_obserwacji.pdf'),
    ('Rozpoznane funkcje echa', 'zalacznik_2_karta_uzgodnien.pdf'),
]
for fraza, plik in ZALACZNIKI:
    n = strona_z_tekstem(fraza)
    if n is None:
        print('  ! nie znaleziono: %s' % fraza); continue
    z = pymupdf.open(); z.insert_pdf(d, from_page=n, to_page=n)
    z.set_metadata({**META, 'title': plik.replace('_',' ')[:-4] + ' — PCTP Koszalin'})
    z.save(os.path.join(KATALOG, plik), garbage=4, deflate=True)
    print('załącznik: %s (str. %d)' % (plik, n + 1))

# ── 6. okładka i zrzuty do strony sprzedażowej ─────────────────────────
d[0].get_pixmap(dpi=200).save(os.path.join(KATALOG, 'okladka.png'))
for etykieta, n in (('podglad_1', 5), ('podglad_2', 21), ('podglad_3', 34)):
    if n < d.page_count:
        d[n].get_pixmap(dpi=150).save(os.path.join(KATALOG, '%s_str%02d.png' % (etykieta, n + 1)))
print('okładka i podglądy zapisane w katalogu %s/' % KATALOG)
d.close()
