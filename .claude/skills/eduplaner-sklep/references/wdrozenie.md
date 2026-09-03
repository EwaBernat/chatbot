# Wdrożenie i publikacja

## Co idzie na serwer

```
index.html
regulamin.html  polityka-prywatnosci.html  formularz-odstapienia.html
img/*.webp  img/og.jpg
broszury/*.pdf          ← tylko te, które mają być publiczne; płatne NIE
```

**Nie idą na serwer:** `img/*.jpg` (źródła), `dist/` (podgląd sklejony przez
`build_single.py`), `panel-filmow.html` (narzędzie autorki — po co ma być publiczne),
`PRZEKAZANIE.md`, `ANALIZA.md`, pliki PDF broszur płatnych.

Płatne PDF-y leżą **poza katalogiem publicznym** i wychodzą wyłącznie przez
punkt `/pobierz/<token>` — patrz `backend.md`. Plik pod stałym adresem to plik
darmowy, niezależnie od tego, co pisze na stronie.

## Kolejność publikacji

1. `node …/gotowosc.js .` — zero blokad. Dopóki są, publikacja jest przedwczesna:
   blokada to albo brakujący plik, albo puste miejsce w dokumencie prawnym.
2. `node …/straznik.js index.html` i to samo `--ciemny` — zero błędów.
   Powtórz dla trzech dokumentów prawnych.
3. Prawnik zatwierdza regulamin, politykę i formularz odstąpienia. Dopiero po
   tym zdejmij pomarańczowy baner „projekt dokumentu" i wpisz datę wejścia w życie.
4. HTTPS z certyfikatem odnawianym automatycznie. Bez tego przeglądarki oznaczą
   formularz zamówienia jako niebezpieczny — i będą miały rację.
5. Przekierowanie `www` → domena główna (albo odwrotnie, byle jedno), żeby nie
   dublować treści.
6. Nagłówki bezpieczeństwa: `Content-Security-Policy` (fonts.googleapis.com
   i fonts.gstatic.com to jedyne zewnętrzne źródła), `X-Content-Type-Options: nosniff`,
   `Referrer-Policy: strict-origin-when-cross-origin`, `Strict-Transport-Security`.
7. Kompresja (gzip lub brotli) i długie `Cache-Control` dla `img/`, krótkie dla HTML.
8. Kopie zapasowe: pliki i baza zamówień. Kopia, której nikt nie odtworzył
   próbnie, nie jest kopią.

## Dwa różne serwery — nie mylić

To jest najczęstsze nieporozumienie w tym projekcie:

| | Gdzie stoi | Co trzyma |
|---|---|---|
| **Strona sprzedażowa** | hosting PCTP, publiczny | oferta, zamówienia, faktury |
| **Aplikacja EduPlaner** | serwer placówki, jej sieć | dokumentacja uczniów |

Obietnica ze strony brzmi: *dane uczniów nie wychodzą poza placówkę, administratorem
jest dyrektor*. Utrzymanie tej obietnicy jest warunkiem sprzedaży do szkół publicznych,
bo to ona zamyka rozmowę o RODO na pierwszym spotkaniu.

Wszystko, co przenosiłoby dokumentację uczniów na serwer PCTP — kopia zapasowa,
statystyki użycia z treścią, „synchronizacja między placówkami" — łamie tę obietnicę
i wymaga rozmowy z właścicielką, zanim powstanie linijka kodu.

Trzy pytania o model z serwerem placówki, na które wciąż nie ma odpowiedzi
i które padną przy pierwszej sprzedaży: **kto robi kopie zapasowe, czy nauczyciel
otworzy aplikację z domu, kto instaluje i aktualizuje**. Odpowiedzi trzeba dopisać
do FAQ, zanim dyrektor zapyta o nie sam.

## Po publikacji

- Sprawdź stronę na telefonie, nie tylko w oknie zwężonym na komputerze.
- Złóż zamówienie testowe każdą ścieżką: placówka na fakturę, osoba prywatna
  online, bezpłatny pokaz. Sprawdź, czy przyszedł mail i czy zapisały się zgody.
- Zgłoś stronę w Google Search Console i wyślij mapę witryny.
- Nagraj sobie w kalendarzu przegląd co pół roku: linki gasną, przepisy się
  zmieniają, a strona sprzedaje przez trzy lata.

## Środowisko pracy z kontrolerami

Skrypty potrzebują Node 18+ i Playwrighta z Chromium. W tym repozytorium:

```bash
export NODE_PATH=/opt/node22/lib/node_modules
export CHROMIUM_PATH=/opt/pw-browsers/chromium
```

`gotowosc.js` nie potrzebuje przeglądarki — działa wszędzie, gdzie jest Node.
Nadaje się na hak przed wysyłką (`pre-push`) albo na krok w CI.
