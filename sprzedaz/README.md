# Strona sprzedażowa — Kolorowy Świat Emocji

Jednostronicowa oferta do wklejenia na **www.eduplaner2026.pl**.

## Pliki

```
sprzedaz/
├── oferta.html            ← gotowa strona (otwórz w przeglądarce)
├── oferta-artefakt.html   ← ta sama treść do publikacji online
├── generuj_oferte.py      ← treść, ceny, licencje i wygląd
└── _zdjecia.py            ← budowany automatycznie ze zdjęć broszury
```

Przebudowa po zmianie: `python3 sprzedaz/generuj_oferte.py`

## Przed publikacją — uzupełnij ceny

W `generuj_oferte.py` w słowniku `LICENCJE` trzy pola `"cena"` mają wartość
`[ cena ]`. Wpisz kwoty i uruchom generator ponownie.

## Licencje

| Licencja | Dla kogo |
|---|---|
| indywidualna | jeden specjalista, wydruki dla własnych podopiecznych |
| placówkowa | cała szkoła, przedszkole lub poradnia |
| szkoleniowa | prowadzący szkolenia i warsztaty |

Zasady „Wolno / Nie wolno" są w `LICENCJA_ZASADY`. To propozycja typowa dla
materiałów edukacyjnych sprzedawanych w PDF — przed publikacją warto ją
przejrzeć pod kątem własnego regulaminu sklepu.

## Jak wstawić na stronę

- **Najprościej:** wgraj `oferta.html` jako osobną podstronę. Plik jest
  samowystarczalny — kroje pisma i zdjęcia siedzą w środku, nic nie dociąga
  się z sieci.
- **Do systemu CMS:** skopiuj zawartość `<body>` do edytora HTML, a `<style>`
  do arkusza stylów motywu.

Strona jest responsywna — układ przestawia się na dwie kolumny poniżej 900 px
i na jedną poniżej 560 px. Sprawdzona na 1280 px i 390 px, bez przewijania
w poziomie.

## Dane firmowe i logo

Pochodzą ze skilla `pctp-marka` (`.claude/skills/pctp-marka`). Jeśli zmienisz
je tam, zaktualizuj też słownik `FIRMA` na górze `generuj_oferte.py`.
