# Kącik dyrektora — przedszkole · paczka do EduPlaner 2026

**Wersja 2.2.0 · rok szkolny 2026/2027 · 32 druki w 12 plikach · 91 stron A4 + 9-stronicowy spis**

Komplet dokumentacji dyrektora przedszkola, zbudowany na tej samej zasadzie co
kącik nauczyciela: strona startowa ze spisem, potem druk po druku, każdy osobno.
Wszystko po polsku, format A4, marka PCTP (fiolet `#2D1B69`, pomarańcz
`#E8450A`, Arial).

---

## 1. Co jest w paczce

| Plik | Druki | Stron |
|---|---|---|
| `INDEKS_Kacik_Dyrektora.html` | strona startowa kącika (czego pilnować + kalendarz + matryca + lista druków + druki powiązane) | 9 |
| `Kacik_Dyrektora_Kalendarz_PCTP` | DK-1 — kalendarz roku z podziałem miesięcznym | 6 |
| `Kacik_Dyrektora_Plan_Pracy_PCTP` | DW-1 — plan pracy z wariantami placówek | 6 |
| `Kacik_Dyrektora_Nadzor_PCTP` | DN-1, DN-2, DN-3, DN-4, DN-5 | 14 |
| `Kacik_Dyrektora_Sprawozdanie_Nauczyciela_PPP` | D-1 | 9 |
| `Kacik_Dyrektora_Pomoc_PP_PCTP` | DP-1, DP-2, DP-3, DP-4 | 8 |
| `Kacik_Dyrektora_Organizacja_PCTP` | DO-1, DO-2, DO-3 | 6 |
| `Kacik_Dyrektora_Bezpieczenstwo_PCTP` | DB-1, DB-2, DB-3 | 6 |
| `Kacik_Dyrektora_Poradnia_Rodzice_PCTP` | DR-1, DR-2, DR-3 | 6 |
| `Kacik_Dyrektora_Rada_Pedagogiczna_PCTP` | RP-1, RP-2, RP-3, RP-4 | 10 |
| `Kacik_Dyrektora_Zmiany_2026_PCTP` | DZ-1, DZ-2, DZ-3 | 6 |
| `Kacik_Dyrektora_Rekrutacja_Ewaluacja_PCTP` | RE-1, EW-1, ZD-1 | 8 |
| `Kacik_Dyrektora_Program_Wychowawczy_PCTP` | PW-1 *(fakultatywny)* | 6 |

Każdy druk występuje w dwóch postaciach: **`.html`** (do podglądu w aplikacji)
i **`.pdf`** (gotowy wydruk). Pełne mapowanie sygnatura → plik → zakres stron
jest w `MANIFEST.json`.

---

## 2. Jak to osadzić w aplikacji

### Strona startowa
`INDEKS_Kacik_Dyrektora.html` to gotowy widok kącika (8 stron). Ma cztery
sekcje w kolejności, którą zamówiła autorka:

1. **Czego dyrektor musi pilnować** — osiem obszarów odpowiedzialności
2. **Kalendarz roku** — terminy z przepisu, każdy z sygnaturą druku
3. **Jaki dokument w jakiej sytuacji** — matryca sytuacja → sygnatury (2 strony)
4. **Lista druków** — karta na każdy druk z przyciskami *Otwórz PDF* / *Podgląd HTML* (4 strony)
5. **Druki z kącika nauczyciela, których potrzebuje dyrektor** — 9 pozycji z linkami do sąsiedniego katalogu, plus podstawa prawna zestawu

Linki w kartach są **względne** (`nazwa_pliku.pdf`), więc działają, jeśli
wszystkie pliki leżą w jednym katalogu. Przy innej strukturze podmień ścieżki
albo zbuduj listę z `MANIFEST.json`.

### Podgląd druku dla dyrektora
Otwórz plik `.html` — na górze jest **panel informacyjny** (co zawiera druk,
kiedy się go używa, terminy, na czym wykłada się kontrola) i przycisk **Drukuj**.
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
jako inline SVG.

---

## 3. Powiązania z kącikiem nauczyciela

Oba kąciki są jednym systemem — `MANIFEST.json` ma na to pole `powiazania`:

| Druk dyrektora | Powiązany druk nauczyciela |
|---|---|
| **D-1** — sprawozdanie z pomocy p-p | wypełnia **nauczyciel**; ostatnia strona (sekcje XV–XVII) należy do dyrektora |
| **DR-1** — wniosek poradni o opinię | samą opinię pisze nauczyciel na druku **O-2** |
| **DO-2** — kontrola dokumentacji | kontroluje dzienniki prowadzone na druku **Z-2** |
| **DP-4** — zbiorcza ocena efektywności | powstaje ze sprawozdań **D-1** i rejestru **DP-2** |
| **DN-2** — arkusz obserwacji zajęć | patrzy na zajęcia planowane drukami **R-2** i **KON** |

Jeżeli aplikacja pokazuje oba kąciki, warto zrobić z tych sygnatur linki
krzyżowe.

---

## 3a. Co doszło w wersji 2.0.0

| Nowość | Druk | Dlaczego |
|---|---|---|
| Podział miesięczny obowiązków, taki sam jak w checkliście nauczyciela K-1 | **DK-1** | dyrektor i nauczyciel patrzą na rok w tym samym układzie: zadanie, podstawa, termin, kratka, data wykonania |
| Plan nadzoru rozbudowany do 6 stron, z przepisem przy **każdym** elemencie | **DN-1** | § 23 ust. 2 i 3 rozporządzenia o nadzorze wymienia elementy planu wprost — każdy z nich ma teraz w druku własną podstawę |
| Pełna, ponumerowana lista **ośmiu kierunków polityki oświatowej 2026/2027** | **DN-1**, **DZ-3** | § 23 ust. 2 czyni je obowiązkową podstawą planu nadzoru |
| Sprawozdanie **semestralne** i **roczne**, oba rozliczające plan sekcja po sekcji | **DN-4**, **DN-5** | pierwsza tabela obu sprawozdań ma wiersze nazwane sekcjami planu DN-1 |
| Plan pracy przedszkola z wariantami: ogólnodostępne, z oddziałami integracyjnymi, integracyjne, specjalne | **DW-1** | limity liczebności oddziałów i zadania specyficzne różnią się między typami placówek |
| Protokół rady z **listą obecności i kworum**, harmonogram ośmiu zebrań obowiązkowych, wzór uchwały i rejestr | **RP-1**, **RP-2**, **RP-3** | art. 69–73 Prawa oświatowego; bez kworum uchwała jest nieważna |
| Karta zmian w statucie z terminami ustawowymi na rok 2026/2027 | **DZ-1** | ustawa z 3.07.2026 r. (Dz.U. 2026 poz. 1036) — statuty do 31.12.2026 r. |
| Plan wdrożenia nowej podstawy programowej z listą kontrolną na obserwację | **DZ-2** | Dz.U. 2026 poz. 378, zm. poz. 958 — obowiązuje od 1.09.2026 r. |

---

## 4. Stan prawny

Zestaw uwzględnia **cztery zmiany obowiązujące w roku szkolnym 2026/2027**:

- **Zakaz urządzeń elektronicznych — także w przedszkolach.** Ustawa z dnia
  3 lipca 2026 r. o zmianie ustawy — Prawo oświatowe (**Dz.U. 2026 poz. 1036**).
  Obowiązuje od **1 września 2026 r.**, statuty dostosowuje się **do 31 grudnia
  2026 r.** — to jedyny termin zapisany w ustawie wprost. Druki **DZ-1** i **RP-2**.
- **Nowa podstawa programowa wychowania przedszkolnego.** Rozp. ME z 11 marca
  2026 r. (**Dz.U. 2026 poz. 378**, zm. poz. 958): dziewięć obszarów, racjonalne
  usprawnienia, projektowanie uniwersalne. Druki **DZ-2**, **DW-1**, **DN-2**.
- **Ocena funkcjonalna.** Rozp. ME z 2 marca 2026 r. (**Dz.U. 2026 poz. 428**):
  opinia o funkcjonowaniu dziecka w **10 dni** od wniosku, z kopią dla rodziców.
  Druk **DR-1**.
- **Standardy ochrony małoletnich po nowelizacji.** Ustawa z 13 maja 2016 r.
  (t.j. Dz.U. 2024 poz. 560), zmieniona ustawą z 5 sierpnia 2025 r. — aktualizacja
  **do 15 sierpnia 2026 r.** Druki **DZ-1**, **DB-3**.

### Osiem kierunków polityki oświatowej państwa 2026/2027

Ustalone przez Ministra Edukacji na podstawie **art. 60 ust. 3 pkt 1** Prawa
oświatowego; **§ 23 ust. 2** rozporządzenia o nadzorze czyni je obowiązkową
podstawą planu nadzoru. Pełna lista jest w polu
`kierunki_polityki_oswiatowej_2026_2027` w `MANIFEST.json`, w sekcji II druku
**DN-1** i w druku **DZ-3**, gdzie każdy kierunek ma przypisane druki, w których
ma się pojawić.

### Terminy sztywne wpisane w druki

`MANIFEST.json` ma je maszynowo w polu `terminy_2026_2027`:
**15.08.2026** (standardy ochrony małoletnich) · **1.09.2026** (podstawa, zakaz
urządzeń, ocena funkcjonalna) · **15.09.2026** (plan nadzoru) · **31.12.2026**
(statut) · **30.04.2027** (MEN-I/74) · **31.08.2027** (wyniki i wnioski z nadzoru).
Poza nimi: **10 dni** na opinię dla poradni, **miesiąc** na skargę, **co najmniej
raz w roku** kontrola obiektu, **co najmniej dwa razy w roku** WOPFU.

Pełna lista podstaw prawnych: sekcja V indeksu oraz pole `podstawa_prawna`
w `MANIFEST.json`.

---

## 5. Czego paczka nie zastępuje

- **DB-2** nie zastępuje **protokołu powypadkowego** sporządzanego przez zespół
  powypadkowy według wzoru z załącznika do rozporządzenia MENiS.
- **DR-1** nie zastępuje **samej opinii** o funkcjonowaniu dziecka — to karta
  obiegu i terminu; opinię pisze nauczyciel na druku **O-2**.
- **DP-3** nie zastępuje **IPET** ani **WOPFU** — organizuje pracę zespołu,
  który je opracowuje.
- **DO-2** nie zastępuje **dzienników**, tylko je kontroluje.
- **DO-2** wskazuje na urzędowy wzór **MEN-I/74** — informacji o gotowości
  szkolnej nie da się zastąpić drukiem własnym.
- **DZ-1** nie zastępuje **statutu** — jest kartą zmian; statut przygotowuje
  i uchwala **rada pedagogiczna** (art. 72 ust. 1 Prawa oświatowego).
- **RP-3** nie zastępuje **regulaminu rady pedagogicznej** — ten rada ustala
  odrębnie (art. 73 ust. 2).

Zakres zgód w druku **DR-2** wymaga porównania ze statutem i procedurami
konkretnej placówki przed wdrożeniem.

---

## 6. Jak zmieniać druki

Źródłem jest **HTML**, PDF się z niego generuje:

```bash
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=NAZWA.pdf NAZWA.html
```

Po każdej zmianie sprawdź, czy żadna strona się nie przelewa: liczba stron PDF
musi się zgadzać z liczbą sekcji `<section class="page">` w pliku HTML i z
wartością `stron` w `MANIFEST.json`.

Wspólne tokeny marki (kolory, ramki, odstępy) siedzą w bloku `:root` na górze
każdego pliku — zmiana tam przechodzi na cały druk.
