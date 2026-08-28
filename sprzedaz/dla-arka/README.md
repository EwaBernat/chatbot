# Pakiet wdrożeniowy — „Kolorowy Świat Emocji"

Wszystko, co potrzebne, żeby podłączyć zeszyt do sprzedaży na
**www.eduplaner2026.pl**. Materiał gotowy — nie trzeba nic dorabiać
poza cenami i podpięciem płatności.

---

## Co jest w paczce

```
dla-arka/
├── README.md              ← ten plik: kolejność wdrożenia i checklista
├── karta-produktu.md      ← opisy i pola do wklejenia w sklepie
├── licencja.md            ← treść licencji dla kupującego (projekt)
├── seo.md                 ← tytuł, opis, adres, grafika do udostępniania
├── pliki/
│   ├── Kolorowy-Swiat-Emocji-czesc-1.pdf   ← PRODUKT do sprzedaży
│   └── strona-oferty.html                  ← gotowa strona sprzedażowa
└── grafiki/
    ├── okladka.jpg           1112×1572  — główne zdjęcie produktu
    ├── podglad-1-spis.jpg    1112×1574  — spis treści
    ├── podglad-2-cialo.jpg   1112×1574  — mapa ciała
    ├── podglad-3-pytania.jpg 1112×1572  — pytania do pracy
    ├── podglad-4-plansza.jpg 1112×1574  — plansza gry
    ├── podglad-5-karty.jpg   1112×1574  — karty emocji
    ├── miniatura-800.jpg      800×800   — kafelek na liście produktów
    ├── og-social.jpg         1200×630   — udostępnianie w sieci
    └── logo-pctp.svg / .png             — logo wydawcy
```

**Produkt to jeden plik PDF: 59 stron A4, 7,5 MB.** Zdjęcia i kroje pisma
są w nim osadzone — otworzy się identycznie na każdym komputerze i wydrukuje
bez dociągania czegokolwiek z sieci.

---

## Kolejność wdrożenia

### 1. Ustal ceny
Trzy warianty licencji opisane w `karta-produktu.md`. Ceny nie są ustalone —
w opisach stoi `[ cena ]`. Bez nich nie ma czego podłączać.

### 2. Załóż produkt w sklepie
Typ: **produkt cyfrowy do pobrania**, nie wysyłkowy.
Trzy warianty (albo trzy osobne produkty) — indeksy w `karta-produktu.md`.
Pola opisowe gotowe do wklejenia, nic nie trzeba przepisywać.

### 3. Podłącz plik
`pliki/Kolorowy-Swiat-Emocji-czesc-1.pdf` jako plik do pobrania po opłaceniu.
Zalecane ustawienia:
- link ważny **7 dni**, limit **5 pobrań** — wystarczy kupującemu, ogranicza
  krążenie linku;
- plik **poza katalogiem publicznym** (nie `/wp-content/uploads/`), wydawany
  przez skrypt sprawdzający zamówienie;
- jeśli sklep to potrafi — **stemplowanie PDF** danymi kupującego
  (e-mail albo numer zamówienia w stopce). To najskuteczniejsze zabezpieczenie
  przed udostępnianiem dalej i nie przeszkadza uczciwemu klientowi.

### 4. Wstaw stronę sprzedażową
`pliki/strona-oferty.html` — samowystarczalna, ze zdjęciami i krojami pisma
w środku. Dwie drogi:
- **osobna podstrona** — wgraj plik jak jest;
- **do CMS-a** — zawartość `<body>` do edytora HTML, `<style>` do arkusza
  stylów motywu.

Responsywna: trzy kolumny, dwie poniżej 900 px, jedna poniżej 560 px.
Sprawdzona na 1280 px i 390 px — bez przewijania w poziomie.
Przyciski „Zobacz licencje" i „Napisz do nas" trzeba podmienić na koszyk,
gdy produkt będzie już w sklepie.

### 5. Podepnij licencję
Treść w `licencja.md`. Musi być dostępna **przed zakupem**, nie dopiero
w pliku — najlepiej jako zakładka na karcie produktu i osobna podstrona.

### 6. Ustaw SEO i podgląd w mediach
Gotowe wartości w `seo.md`, grafika `grafiki/og-social.jpg`.

---

## Checklista przed uruchomieniem

- [ ] Ceny wpisane we wszystkich trzech wariantach
- [ ] Plik PDF podpięty i **poza katalogiem publicznym**
- [ ] Test zakupu na własne konto — od koszyka po pobranie
- [ ] PDF otwiera się i drukuje poprawnie (sprawdź stronę 51 — planszę gry
      i stronę 54 — karty; tam jest najwięcej koloru)
- [ ] Licencja dostępna przed zakupem
- [ ] Regulamin sklepu i polityka prywatności podlinkowane
- [ ] Zgoda na dostarczenie treści cyfrowej przed upływem terminu odstąpienia
      (patrz niżej — do potwierdzenia z prawnikiem)
- [ ] Faktury / paragony ustawione zgodnie z tym, co powie księgowość
- [ ] Podgląd linku sprawdzony na Facebooku i LinkedInie
- [ ] Strona oferty otwarta na telefonie

---

## Dwie sprawy do potwierdzenia poza IT

Nie są to decyzje techniczne i nie powinien ich podejmować programista:

**Prawo odstąpienia od umowy.** Przy treściach cyfrowych kupujący traci prawo
do zwrotu w ciągu 14 dni, ale tylko wtedy, gdy przed pobraniem wyraźnie się
na to zgodzi i zostanie o tym poinformowany. W sklepie musi więc być
obowiązkowy checkbox przy zakupie. Dokładne brzmienie zgody i regulaminu
niech potwierdzi prawnik.

**Podatki.** Sprzedaż plików cyfrowych rozlicza się inaczej niż towar,
a inaczej przy sprzedaży do placówek niż osobom prywatnym. To pytanie
do księgowości, nie do sklepu.

---

## Kontakt w sprawie treści

Mirosława Ewa Jurczyszyn · kontakt@eduplaner2026.pl · [usunięto]

Gdyby trzeba było poprawić coś w samym zeszycie — treść, ceny na stronie,
układ — całość generuje się ze źródeł w tym repozytorium
(`broszura/` i `sprzedaz/`), więc poprawka to zmiana jednej linijki
i ponowne uruchomienie generatora. Instrukcje w `broszura/README.md`
i `sprzedaz/README.md`.
