# Kącik nauczyciela — przedszkole · paczka do EduPlaner 2026

**Wersja 1.1.0 · rok szkolny 2026/2027 · 26 druków w 10 plikach · 61 stron A4**

Komplet dokumentacji nauczyciela wychowawcy grupy przedszkolnej. Wszystko po
polsku, format A4, marka PCTP (fiolet `#2D1B69`, pomarańcz `#E8450A`, Arial).

---

## 1. Co jest w paczce

| Plik | Druki | Stron |
|---|---|---|
| `INDEKS_Kacik_Nauczyciela.html` | strona startowa kącika (checklista + matryca + lista druków) | — |
| `Kacik_Nauczyciela_Checklista_Wychowawcy_PCTP` | K-1 | 5 |
| `Kacik_Nauczyciela_Dostosowania_PCTP` | DS-1 | 3 |
| `Kacik_Nauczyciela_Wzory_Opinii_PCTP` | O-1, O-2, O-3, O-4, O-5 | 12 |
| `Kacik_Nauczyciela_Pomoc_PP_PCTP` | P-1, P-2, P-3 | 6 |
| `Kacik_Nauczyciela_Rewalidacja_Dziennik_PCTP` | Z-1, Z-2, Z-3 | 8 |
| `Kacik_Nauczyciela_Planowanie_PCTP` | R-1, R-2, R-3, R-4 | 8 |
| `Kacik_Nauczyciela_Rodzice_PCTP` | W-1, W-2, W-3 | 6 |
| `Kacik_Nauczyciela_Bezpieczenstwo_PCTP` | B-1, B-2, B-3, B-4 | 8 |
| `Konspekt_Zajec_Szablon_PCTP` | KON | 1 |
| `Instrukcja_Cele_SMART_PCTP` | I-1 | 4 |

Każdy druk występuje w dwóch postaciach: **`.html`** (do podglądu w aplikacji)
i **`.pdf`** (gotowy wydruk). Pełne mapowanie sygnatura → plik → zakres stron
jest w `MANIFEST.json`.

---

## 2. Jak to osadzić w aplikacji

### Strona startowa
`INDEKS_Kacik_Nauczyciela.html` to gotowy widok kącika. Ma trzy sekcje w
kolejności, którą zamówiła autorka:

1. **Czego nauczyciel musi pilnować** — sześć bloków rytmu roku
2. **Jaki dokument w jakiej sytuacji** — matryca sytuacja → sygnatury druków
3. **Lista druków** — karta na każdy druk z przyciskami *Otwórz PDF* / *Podgląd HTML*

Linki w kartach są **względne** (`nazwa_pliku.pdf`), więc działają, jeśli
wszystkie pliki leżą w jednym katalogu. Przy innej strukturze podmień ścieżki
albo zbuduj listę z `MANIFEST.json`.

### Podgląd druku dla nauczyciela
Otwórz plik `.html` — na górze jest **panel informacyjny** (co zawiera druk,
kiedy się go używa, terminy, zasady wypełniania) i przycisk **Drukuj**.
Panel ma `@media print { display: none }`, więc **nie trafia na wydruk** —
drukuje się wyłącznie sam formularz.

### Druk
```
format: A4
marginesy: brak
grafika tła: włączona
orientacja: pionowa
```
Bez włączonej grafiki tła znikną kolorowe nagłówki tabel i karty.

### Pliki są samowystarczalne
Zero zależności zewnętrznych: brak CDN, brak fontów z sieci, logo osadzone
jako inline SVG. Można je serwować z dowolnego katalogu statycznego, otworzyć
z dysku, wsadzić w `iframe` albo w WebView.

---

## 3. MANIFEST.json

Maszynowy opis paczki — użyj go do zbudowania listy druków w aplikacji zamiast
kodować ją na sztywno:

```jsonc
{
  "druki": [
    { "sygnatura": "O-2", "nazwa": "...", "plik": "Kacik_Nauczyciela_Wzory_Opinii_PCTP",
      "strona_od": 3, "strona_do": 6, "kategoria": "opinie" }
  ],
  "pliki":  { "<plik>": { "html": "...", "pdf": "...", "stron": 12, "sha256_pdf": "..." } },
  "kategorie": { "opinie": "Opinie o dziecku", "...": "..." }
}
```

`strona_od` / `strona_do` pozwalają otworzyć PDF od razu na właściwym druku
(`plik.pdf#page=3`) albo wyciąć pojedynczy druk do osobnego pliku.

---

## 4. Stan prawny — dlaczego to jest aktualne

Zestaw jest zgodny z dwiema zmianami obowiązującymi **od 1 września 2026 r.**:

- **Nowa podstawa programowa wychowania przedszkolnego** — rozp. ME z 11 marca
  2026 r. (Dz.U. 2026 poz. 378, zm. poz. 958). Wprowadza **dziewięć obszarów**
  (społeczny, osobisty, językowy, matematyczny, przyrodniczy, techniczny,
  cyfrowy, artystyczny, ruchowy) w miejsce dotychczasowych czterech, a także
  **racjonalne usprawnienia** i **projektowanie uniwersalne**. Wszystkie tabele
  obszarowe w druku R-1, R-4, O-2, DS-1 są już przestawione na dziewięć obszarów.
- **Ocena funkcjonalna** — rozp. ME z 2 marca 2026 r. (Dz.U. 2026 poz. 428).
  Przedszkole wydaje **opinię o funkcjonowaniu dziecka** w terminie **10 dni**
  od wniosku, z kopią dla rodziców — to druk **O-2**.

Dokumentacja zajęć rewalidacyjnych i zajęć z zakresu pomocy
psychologiczno-pedagogicznej opiera się na **§ 11 rozp. MEN z 25 sierpnia
2017 r.** (Dz.U. 2017 poz. 1646). Przepis wymienia wprost, co musi zawierać
dziennik tych zajęć: imiona i nazwiska dzieci, oddział, **adresy i telefony
rodziców**, indywidualny program pracy z dzieckiem (przy zajęciach grupowych —
program pracy grupy), **tygodniowy rozkład zajęć**, daty, czas trwania i tematy
przeprowadzonych zajęć, **ocenę postępów i wnioski dotyczące dalszej pracy**
oraz obecność dzieci; przeprowadzenie zajęć potwierdza się podpisem. Druki
**Z-1 → Z-2 → Z-3** pokrywają ten wymóg w całości.

Pełna lista podstaw prawnych: sekcja 4 indeksu oraz pole `podstawa_prawna`
w `MANIFEST.json`.

---

## 5. Czego paczka nie zastępuje

Trzy druki mają w treści wyraźne zastrzeżenia — proszę ich nie usuwać przy
adaptacji:

- **O-5** nie zastępuje urzędowego wzoru **MEN-I/74** (informacja o gotowości
  szkolnej wydawana rodzicom do końca kwietnia).
- **B-2** nie zastępuje **protokołu powypadkowego** sporządzanego przez zespół
  powypadkowy.
- **R-3** nie zastępuje **dziennika zajęć** wymaganego rozporządzeniem
  o dokumentacji — tylko go uzupełnia. Dziennikiem w rozumieniu § 11 jest
  druk **Z-2**.
- **Z-1** nie zastępuje **IPET** ani **WOPFU** — przenosi z nich zalecenia
  i dostarcza materiału do ich modyfikacji.

Dodatkowo **W-3** (zgody i upoważnienia) wymaga porównania zakresu zgód ze
statutem i procedurami konkretnej placówki przed wdrożeniem.

---

## 6. Jak zmieniać druki

Źródłem jest **HTML**, PDF się z niego generuje:

```bash
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=NAZWA.pdf NAZWA.html
```

Po każdej zmianie sprawdź, czy żadna strona się nie przelewa — kryterium jest
proste: liczba stron PDF musi się zgadzać z liczbą sekcji `<section class="page">`
w pliku HTML i z wartością `stron` w `MANIFEST.json`.

Wspólne tokeny marki (kolory, ramki, odstępy) siedzą w bloku `:root` na górze
każdego pliku — zmiana tam przechodzi na cały druk.
