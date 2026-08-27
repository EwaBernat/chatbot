# Pułapki przy składaniu PDF-u z HTML

Wszystkie opisane niżej błędy wyglądają identycznie z zewnątrz: **PDF nie wygląda
tak, jak strona na ekranie**. Różnią się przyczyną, więc warto je odróżniać.
Kolejność odpowiada temu, jak często występują.

---

## 1. Reguła `@media (max-width: …)` obowiązuje także przy druku

**Objaw:** w PDF-ie treść dotyka górnej krawędzi, marginesy boczne są węższe niż
w projekcie, stopka siedzi tuż przy dole strony.

**Przyczyna:** przy druku szerokość obszaru layoutu równa się szerokości strony,
czyli 210 mm. Każdy `@media (max-width: 230mm)` — pomyślany jako układ mobilny —
jest wtedy spełniony i nadpisuje `padding` oraz `width` strony.

**Rozwiązanie:** zawsze `@media screen and (max-width: …)`. Skrypt
`osadz_fonty.py` poprawia to automatycznie i wypisuje komunikat.

**Jak sprawdzić:** zmierz w PDF-ie górny margines tekstu. Jeżeli wynosi dokładnie
tyle, ile `padding-top` z reguły mobilnej (np. 24 px ≈ 6,3 mm), to jest ta pułapka.

```python
import pymupdf
d = pymupdf.open('plik.pdf'); MM = 72/25.4
w = d[5].get_text('words')
print('góra:', min(x[1] for x in w)/MM, 'mm')   # ma odpowiadać padding-top strony
```

---

## 2. Fonty z sieci nie są dostępne w chwili renderowania

**Objaw:** PDF wygląda jak zwykły dokument tekstowy — inne proporcje liter,
inne łamanie wierszy niż na ekranie.

**Przyczyna:** środowisko generujące PDF nie ma dostępu do `fonts.googleapis.com`.
Przeglądarka po cichu podstawia kroje systemowe (Liberation, DejaVu).

**Rozwiązanie:** osadzić kroje w pliku jako `data:` URI — robi to `osadz_fonty.py`.

**Jak sprawdzić:**

```python
import pymupdf
d = pymupdf.open('plik.pdf')
print(sorted({f[3] for n in range(d.page_count) for f in d[n].get_fonts()}))
```

Nazwy w rodzaju `LiberationSerif` albo `DejaVuSans` przy tekście ciągłym oznaczają
podmianę. Pojedyncze wystąpienia DejaVu przy znakach ✓ ✗ ◆ są normalne — tych
glifów nie ma w krojach marki.

---

## 3. Fonty zmienne dają glify typu Type3

**Objaw:** kroje są właściwe, ale tekst źle się zaznacza i nie działa
wyszukiwanie; drukarnia zgłasza problem z plikiem.

**Przyczyna:** przeglądarka rasteryzuje instancje fontów zmiennych do fontów
Type3 (procedury rysujące), zamiast osadzić prawdziwy krój.

**Rozwiązanie:** pobierać **statyczne** pliki na wagę. Wymusza je nagłówek
`User-Agent` starszej przeglądarki — patrz stała `UA` w `osadz_fonty.py`.

**Jak sprawdzić:**

```python
import pypdf
r = pypdf.PdfReader('plik.pdf')
typy = {}
for pg in r.pages:
    for k, v in (pg.get('/Resources', {}).get('/Font', {}) or {}).items():
        t = str(v.get_object().get('/Subtype')); typy[t] = typy.get(t, 0) + 1
print(typy)   # oczekujemy wyłącznie {'/Type0': N}
```

---

## 4. Waga kroju spoza dostępnego zakresu

**Objaw:** pojedyncze elementy (zwykle pogrubienia) mają inny krój niż reszta.

**Przyczyna:** CSS prosi o `font-weight:800`, a statyczny font kończy się na 700.
Przeglądarka podstawia krój systemowy zamiast syntetyzować pogrubienie.

**Rozwiązanie:** używać wyłącznie wag faktycznie pobranych. Dla marki PCTP:
Fraunces 400–900, DM Sans 400/500/700, JetBrains Mono 400/500/700.

---

## 5. Nazwy rodzin w SVG bez cudzysłowów

**Objaw:** podpisy wewnątrz rycin mają inny krój niż tekst wokół.

**Przyczyna:** w atrybucie SVG `font-family="DM Sans,sans-serif"` nazwa
dwuczłonowa bez cudzysłowów bywa niedopasowana.

**Rozwiązanie:** `font-family="'DM Sans',sans-serif"`.

---

## 6. Strona wyższa niż arkusz — nadmiarowe puste strony

**Objaw:** PDF ma więcej stron niż projekt; co druga jest pusta lub zawiera
wąski pasek treści.

**Przyczyna:** `.page` ma dokładnie 297 mm, a przez zaokrąglenia jednostek
przelewa się o ułamek milimetra na kolejny arkusz.

**Rozwiązanie:** w bloku `@media print` ustawić `height:296.9mm` przy
`overflow:hidden` i `break-after:page`. Zapas 0,1 mm jest niewidoczny, a usuwa
przelewanie.

**Jak sprawdzić:** liczba stron w PDF-ie musi się zgadzać z liczbą `.page`
w dokumencie. Sprawdza to `sprawdz_uklad.js`.

---

## Kolejność diagnozy

Przy każdej skardze „PDF wygląda inaczej niż HTML" sprawdzaj w tej kolejności —
od najczęstszej przyczyny:

1. marginesy w PDF (pułapka 1),
2. nazwy krojów w PDF (pułapka 2),
3. typy fontów: Type0 czy Type3 (pułapka 3),
4. liczba stron (pułapka 6).

Nie zgaduj — wszystkie cztery sprawdzenia zajmują łącznie kilkanaście sekund
i od razu wskazują winowajcę.
