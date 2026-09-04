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

## Weryfikacja publikatorów

Pozycje oznaczone w dokumencie znakiem ⚑ wymagają sprawdzenia w ISAP przed wpisaniem do
dokumentacji ucznia — dotyczy to w szczególności tekstów jednolitych ogłaszanych w trakcie roku
szkolnego oraz terminów i katalogu dostosowań z corocznego komunikatu dyrektora CKE.

## Budowanie dokumentu

```bash
pip install python-docx
python3 build_skrypt_szkola.py     # → Skrypt_dla_nauczycieli_SZKOLA_PODSTAWOWA_EduPlaner_2026.docx
```

Marka PCTP: Arial, fiolet `#2D1B69`, pomarańcz `#E8450A`, tła `#F2F0F7` / `#F7F6FA` — zgodnie
ze skryptem przedszkolnym.
