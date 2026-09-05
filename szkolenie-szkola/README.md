# Skrypt dla nauczycieli — szkoła podstawowa (EduPlaner 2026 · PCTP)

Szkolenie rady pedagogicznej w tym samym systemie co skrypt przedszkolny, ale na danych
szkolnych i przepisach dotyczących szkoły podstawowej.

## Zawartość dokumentu (64 strony A4)

| Część | Tytuł | Czas |
|---|---|---|
| 1 | Podstawa prawna — co obowiązuje w szkole od 1 września 2026 r. | 10:40 |
| 2 | **Dlaczego szkoła musi zmienić dokumentację kształcenia specjalnego — uzasadnienie i zakres zmian** | 12:20 |
| 3 | Obieg dokumentów w szkole — jak jeden wynika z drugiego | 6:10 |
| 4 | Metryczka i teczka ucznia — pierwszy dokument września | 6:30 |
| 5 | KSzOF — budowa narzędzia, skala, steny, liczenie wyniku, odczyt profilu | 11:20 |
| 6 | Obserwacja pogłębiona — ABC i FBA, profil sensoryczny, teoria umysłu, karta mowy | 10:30 |
| 7 | WOPF-SP, IPET, PWES, cele SMART, ewaluacja i opinia dla poradni | 14:10 |

Załączniki: A — kalendarz dokumentacji na rok szkolny · B — język funkcjonalny ·
C — 18 druków do powielenia · D — wzór zarządzenia dyrektora · E — checklista wdrożenia 30/60/90 dni.

Każda część ma trzy warstwy, tak jak skrypt przedszkolny: podstawę prawną, pełną transkrypcję
narracji (numerowane plansze) oraz instrukcję przygotowania dokumentu krok po kroku.

## Osiemnaście druków (załącznik C)

1. KD-SP — karta decyzyjna obserwacji pogłębionej
2. ABC-SP — karta obserwacji zachowania (model ABC)
3. FBA-SP — arkusz analizy funkcjonalnej zachowania
4. PS-SP — profil sensoryczny ucznia
5. KM-SP — karta obserwacji rozwoju mowy i komunikacji
6. ToM-SP — arkusz obserwacji poznania społecznego i teorii umysłu
7. KFU-SP — karta obserwacji funkcji uczenia się
8. MG-SP — ankieta „Mój głos" (perspektywa ucznia)
9. AR-SP — ankieta dla rodzica i wywiad środowiskowy
10. NP-SP — arkusz informacji od nauczyciela przedmiotu (II etap)
11. KDP-SP — karta dostosowań przedmiotowych
12. AD-E8 — karta dostosowań warunków egzaminu ósmoklasisty
13. SMART-SP — karta celu i ewaluacji
14. OE-SP — karta oceny efektywności udzielanej pomocy
15. PWES — plan wsparcia edukacyjnego ucznia (bez orzeczenia)
16. KP-SP — karta przekazania informacji o uczniu (klasa III → IV)
17. AUD-SP — arkusz audytu dokumentacji kształcenia specjalnego
18. RK-SP — rejestr kontaktów z rodzicami

## Dane wzorcowe

Szkoła Podstawowa nr 7 im. Jana Brzechwy w Koszalinie · Zofia Lewandowska, klasa III A ·
orzeczenie PPP.4223.18.2026 z 12.06.2026 r. (niepełnosprawność sprzężona) ·
IPET/2026-2027/III A/07 — zgodnie z dokumentacją wzorcową EduPlaner 2026.

Przykład obliczeniowy KSzOF jest wewnętrznie spójny z tabelą obszarów w druku IPET:
suma 114/260 pkt → sten 4 (wynik niski), profil obszarowy 6–12 pkt w skali 0–20.

## Weryfikacja publikatorów — wydanie 2 (5 września 2026)

Dokument przeszedł audyt podstaw prawnych. Wszystkie publikatory zweryfikowano i wpisano do
**rejestru przepisów (załącznik F)** z datą sprawdzenia. Fragmenty zmienione w audycie oznaczono
w dokumencie **kolorem niebieskim**; pełny wykaz ustaleń zawiera **Raport Strażnika Prawa**
(strona 3 dokumentu) oraz plik [`AUDYT-2026-09-05.md`](AUDYT-2026-09-05.md).

Wynik audytu: 5 błędów potwierdzonych i poprawionych, 2 zarzuty odrzucone jako nietrafne
(rozporządzenie Dz.U. 2026 poz. 428 obowiązuje i uchyliło akt z 2017 r.; Prawo oświatowe ma t.j.
Dz.U. 2026 poz. 820), 5 ustaleń własnych.

Znak ⚑ pozostaje w dokumencie tylko przy komunikacie dyrektora CKE o dostosowaniach egzaminu
ósmoklasisty — jedynym źródle, które zmienia się co roku.

## Budowanie dokumentu

```bash
pip install python-docx
python3 build_skrypt_szkola.py     # → Skrypt_dla_nauczycieli_SZKOLA_PODSTAWOWA_EduPlaner_2026.docx
```

Marka PCTP: Arial, fiolet `#2D1B69`, pomarańcz `#E8450A`, tła `#F2F0F7` / `#F7F6FA` — zgodnie
ze skryptem przedszkolnym.

---

## Audyt skryptu przedszkolnego (5 września 2026)

Tą samą metodą sprawdzono oryginalny skrypt przedszkolny. Wynik: **zero nieaktualnych publikatorów
i zero błędów w treści przepisu** — 4 sprostowania merytoryczne i 5 luk (czynność wymagana przez skrypt
bez wskazanej podstawy prawnej).

- `AUDYT_Skryptu_PRZEDSZKOLNEGO_Straznik_Prawa_2026-09-05.docx` — raport (5 stron)
- `AUDYT-PRZEDSZKOLE-2026-09-05.md` — ta sama treść w markdownie
- `Skrypt_dla_nauczycieli_PRZEDSZKOLE_wydanie2_po_audycie.docx` — oryginał z poprawkami na niebiesko
- `patch_skrypt_przedszkole.py` — skrypt nanoszący poprawki na plik źródłowy

Ustalenie wspólne dla obu skryptów: numeracja ustępów § 6 rozporządzenia o kształceniu specjalnym nie jest
potwierdzona w ogłoszonym tekście, więc w obu dokumentach cytujemy „§ 6 rozporządzenia” i opisujemy obowiązek
słowami.

## Dogrywki do materiału filmowego — przedszkole

Ustalenia audytu przełożone na produkcję filmu (moduły M1–M6):

- `DOGRYWKI_film_PRZEDSZKOLE_po_audycie_2026-09-05.docx` — karta dogrywek (8 stron): moduł, plansza,
  po której następuje cięcie, gotowy tekst do przeczytania, treść nowej planszy, czas
- `dogrywki-narracja.txt` — sam tekst do nagrania i do napisów, jeden fragment na blok
- `dogrywki_film_przedszkole.py` — generator obu plików

**9 dogrywek, ~5:44 materiału.** Wszystkie są wstawkami między istniejące plansze — żadne nagrane
zdanie nie wymaga powtórzenia. Moduły M2 i M5 bez zmian. Do wymiany 5 plansz z podstawą prawną
(zmiana wyłącznie graficzna).

Tempo dogrywek policzone z istniejącego filmu: 5753 słowa / 53:57 = **107 słów na minutę**.

## Montaż wstawek do filmu (M1, M3, M4)

- `wstawki_manifest.json` — siedem wstawek: punkt cięcia, tytuł, punkty planszy, tekst narracji
- `plansza.py` — renderer plansz w projekcie filmu (Chromium, 1920×1080)
- `zloz_wstawki.py` — potok montażowy: dzieli film, buduje wstawkę, skleja
- `nagraj_wstawki.py` — generuje nagrania głosem autorki (uruchamiać tam, gdzie sieć przepuszcza)
- `plansze_wstawek/` — podglądy siedmiu plansz
- `INSTRUKCJA-montazu-filmu.md` — punkty cięcia i trzy polecenia do dokończenia

Punkty cięcia namierzone OCR-em paska napisów i potwierdzone klatkami; potok przetestowany
na M3 (345 s → 410 s, styki czyste). Nagrania czekają na dostęp do ElevenLabs — skrypt nie
podstawia cudzego głosu.
