# Kącik dyrektora — przedszkole · paczka do EduPlaner 2026

**Wersja 1.0.0 · rok szkolny 2026/2027 · 18 druków w 6 plikach · 43 strony A4**

Komplet dokumentacji dyrektora przedszkola, zbudowany na tej samej zasadzie co
kącik nauczyciela: strona startowa ze spisem, potem druk po druku, każdy osobno.
Wszystko po polsku, format A4, marka PCTP (fiolet `#2D1B69`, pomarańcz
`#E8450A`, Arial).

---

## 1. Co jest w paczce

| Plik | Druki | Stron |
|---|---|---|
| `INDEKS_Kacik_Dyrektora.html` | strona startowa kącika (czego pilnować + kalendarz + matryca + lista druków) | 6 |
| `Kacik_Dyrektora_Sprawozdanie_Nauczyciela_PPP` | D-1 | 9 |
| `Kacik_Dyrektora_Pomoc_PP_PCTP` | DP-1, DP-2, DP-3, DP-4 | 8 |
| `Kacik_Dyrektora_Nadzor_PCTP` | DN-1, DN-2, DN-3, DN-4 | 8 |
| `Kacik_Dyrektora_Organizacja_PCTP` | DO-1, DO-2, DO-3 | 6 |
| `Kacik_Dyrektora_Bezpieczenstwo_PCTP` | DB-1, DB-2, DB-3 | 6 |
| `Kacik_Dyrektora_Poradnia_Rodzice_PCTP` | DR-1, DR-2, DR-3 | 6 |

Każdy druk występuje w dwóch postaciach: **`.html`** (do podglądu w aplikacji)
i **`.pdf`** (gotowy wydruk). Pełne mapowanie sygnatura → plik → zakres stron
jest w `MANIFEST.json`.

---

## 2. Jak to osadzić w aplikacji

### Strona startowa
`INDEKS_Kacik_Dyrektora.html` to gotowy widok kącika. Ma cztery sekcje
w kolejności, którą zamówiła autorka:

1. **Czego dyrektor musi pilnować** — sześć obszarów odpowiedzialności
2. **Kalendarz roku** — terminy z przepisu, każdy z sygnaturą druku
3. **Jaki dokument w jakiej sytuacji** — matryca sytuacja → sygnatury
4. **Lista druków** — karta na każdy druk z przyciskami *Otwórz PDF* / *Podgląd HTML*

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

## 4. Stan prawny

Zestaw uwzględnia dwie zmiany obowiązujące **od 1 września 2026 r.**:

- **Nowa podstawa programowa wychowania przedszkolnego** — rozp. ME z 11 marca
  2026 r. (Dz.U. 2026 poz. 378, zm. poz. 958): dziewięć obszarów, racjonalne
  usprawnienia, projektowanie uniwersalne. Druk **DN-2** sprawdza na obserwacji,
  czy dziecko z niepełnosprawnością wykonuje **to samo zadanie w dostosowanej
  formie**, a nie inne zadanie obok grupy.
- **Ocena funkcjonalna** — rozp. ME z 2 marca 2026 r. (Dz.U. 2026 poz. 428):
  dyrektor wydaje **opinię o funkcjonowaniu dziecka w terminie 10 dni** od
  otrzymania wniosku, z kopią dla rodziców. To druk **DR-1**.

Terminy sztywne wpisane w druki: **15 września** (plan nadzoru), **31 sierpnia**
(wyniki i wnioski z nadzoru), **10 dni** (opinia dla poradni), **miesiąc**
(załatwienie skargi), **30 kwietnia** (informacja o gotowości szkolnej),
**co najmniej raz w roku** (kontrola obiektu), **co najmniej dwa razy w roku**
(WOPFU i ocena efektywności pomocy).

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
