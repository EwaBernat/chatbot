# Angielski dla Maksia — fiszki

Pakiet do nauki angielskiego: 10 zdań potrzebnych, żeby się przedstawić.

## Co jest w środku

- **`angielski-dla-maksia.html`** — fiszki na ekran. Jeden plik, otwiera się
  w przeglądarce (też na telefonie), działa bez internetu — nagrania są
  wbudowane w plik jako `data:` URI.
- **`Fiszki-Angielski-dla-Maksia.pdf`** — te same fiszki do druku i wycięcia:
  4 strony A4, po 8 kart na stronie, dwustronnie.
- **`druk/`** — skrypty, którymi PDF powstał.
Osobnych plików MP3 tu nie ma — repozytorium ignoruje `*.mp3`
(`.gitignore`), a nagrania i tak siedzą w środku HTML-a.

## Jak działają fiszki

Każda fiszka pokazuje:

| element | co to jest |
|---|---|
| po polsku | zdanie, które Maks chce powiedzieć |
| jak się pisze | wersja angielska |
| jak się czyta | zapis polskimi literami, `DUŻE LITERY` = akcent |
| IPA | zapis fonetyczny dla dociekliwych |
| ▶ Posłuchaj / 🐢 Wolno | nagranie w normalnym tempie i spowolnione do 0,65× |
| odpowiedz tak | przykładowa odpowiedź, też z nagraniem |
| pułapka | typowy błąd Polaka przy tym zdaniu |

Skróty klawiszowe: `←` `→` zmiana fiszki, `spacja` odsłania angielski,
`P` odtwarza nagranie.

Na dole strony jest ściąga ze wszystkimi dziesięcioma zdaniami.

## Zdania

1. Good morning. — Dzień dobry (rano)
2. Good afternoon. — Dzień dobry (po południu)
3. Good evening. — Dobry wieczór
4. What's your name? — Jak masz na imię?
5. What's your surname? — Jak się nazywasz?
6. Where are you from? — Skąd jesteś?
7. Tell me something about yourself. — Powiedz coś o sobie
8. Where do you live? — Gdzie mieszkasz?
9. What do you do now? — Co teraz robisz w życiu?
10. What do you like? — Co lubisz?

## Nagrania

Wygenerowane w ElevenLabs, głos **Alvina — Clear Natural Narrator**
(amerykański, neutralny), model `eleven_multilingual_v2`.

Wolne tempo nie jest osobnym nagraniem — przeglądarka odtwarza to samo MP3
z `playbackRate = 0.65` i zachowaną wysokością głosu, więc brzmi naturalnie,
tylko wolniej.

## Do podmiany

Przykładowe odpowiedzi zawierają dane zastępcze: nazwisko *Nowak*,
miasto *Koszalin*, zainteresowania *muzyka, sport, gry*. Maks powinien
wstawić swoje — tekst jest w tablicy `CARDS` w pliku HTML.


## Fiszki papierowe (PDF)

16 kart o wymiarach 95 × 68 mm, po 8 na stronie A4.

- karty **01–03** — powitania (zielona plakietka)
- karty **04–10** — pytania o ciebie (granatowa)
- karty **11–15** — gotowe odpowiedzi (pomarańczowa)
- karta **16** — ściąga: jak czytać zapis i które powitanie o której porze

Przód karty jest po polsku, tył po angielsku razem z zapisem fonetycznym
i IPA. Strony w PDF idą naprzemiennie przód–tył–przód–tył.

### Jak drukować

1. Drukuj **dwustronnie**, obrót **wzdłuż dłuższej krawędzi** (domyślne
   ustawienie w większości drukarek). Tyły są dlatego odbite w poziomie,
   żeby po wydruku trafiły dokładnie na swoje przody.
2. Skalowanie ustaw na **100% / rozmiar rzeczywisty**, nie „dopasuj do strony”
   — inaczej karty wyjdą mniejsze niż linie cięcia.
3. Tnij po przerywanych liniach. Grubszy papier (160–200 g) trzyma się lepiej,
   ale zwykły też zadziała.

### Jak przebudować PDF

```bash
cd druk
python3 fetch_fonts.py     # pobiera fonty i zapisuje fonts.css
python3 build.py           # składa arkusze -> fiszki-druk.html
npm install playwright
node render.mjs            # renderuje ../Fiszki-Angielski-dla-Maksia.pdf
```

Treść kart siedzi w liście `CARDS` na górze `build.py`. Gwiazdki w polu `say`
zaznaczają sylabę akcentowaną: `gud *MOR*-ning`.
