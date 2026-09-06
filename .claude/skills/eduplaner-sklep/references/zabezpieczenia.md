# Zabezpieczenie broszur i nagrań

Właścicielka sprzedaje pliki i nagrania. Pytanie brzmi: jak zrobić, żeby kupujący
nie rozesłał ich całej radzie pedagogicznej. Ten plik mówi, co da się zrobić,
czego się nie da, i czego nie wolno obiecywać.

## Czego nie da się zrobić — i trzeba to powiedzieć wprost

**Nagrania ekranu nie da się zablokować.** Kto ogląda film, ten może go nagrać —
telefonem, jeśli nie inaczej. Każdy, kto twierdzi inaczej, sprzedaje złudzenie.
Nawet DRM (Widevine, FairPlay) tego nie powstrzymuje; DRM podnosi próg techniczny,
nie zamyka drogi.

**PDF-a nie da się zamknąć przed czytelnikiem, który ma go otworzyć.** Hasła
i uprawnienia w PDF zdejmuje się darmowym narzędziem w minutę. Blokada drukowania
jest gorsza niż nic: łamie ją każdy, kogo to obchodzi, a przeszkadza tym, którzy
kupili broszurę **właśnie po to, żeby ją wydrukować i pracować z dzieckiem**.

Wniosek, który przesądza całą resztę: **celem nie jest uniemożliwienie kopiowania,
tylko sprawienie, żeby kopiowanie było kłopotliwe i imienne.** Plik ze swoim
nazwiskiem w stopce rozsyła się dużo rzadziej niż plik anonimowy.

## Broszury: trzy poziomy, wdrażać po kolei

**Poziom 0 — czego nie robić nigdy.** Płatny PDF nie może leżeć w katalogu
publicznym pod stałym adresem. Jeden taki adres wysłany dalej to koniec sprzedaży
tej pozycji. `gotowosc.js` sprawdza to i zgłasza blokadę.

**Poziom 1 — link wygasający.** Token losowy, ważny 72 godziny, najwyżej 5 pobrań,
powiązany z numerem zamówienia. Link nie jest adresem pliku, tylko adresem punktu
końcowego, który sprawdza token i dopiero potem oddaje plik. Po wyczerpaniu limitu
strona z przyciskiem „poproś o nowy link" — nie martwy błąd, bo najczęstszy powód
wyczerpania to zwykła zmiana komputera.

**Poziom 2 — znak wodny nadawany przy pobraniu.** Nie w pliku źródłowym, tylko
generowany w chwili wydania: imię i nazwisko lub nazwa placówki, adres e-mail,
numer zamówienia, data. Dyskretnie, w stopce każdej strony, szarym drukiem —
ma nie psuć wydruku do pracy z dzieckiem. To jest jedyne zabezpieczenie, które
naprawdę działa, bo działa na człowieka, nie na plik.

Licencja z regulaminu § 7 mówi, do czego kupujący ma prawo: osoba prywatna drukuje
na własny użytek zawodowy, placówka na potrzeby swojego zespołu. Znak wodny ma
o tym przypominać, nie straszyć. Ton stopki: „Egzemplarz dla: Anna Kowalska ·
zamówienie 2026/09/0014", a nie ostrzeżenie o odpowiedzialności karnej.

## Nagrania: gdzie je trzymać

**Nagrania bezpłatne** (film wprowadzający i pozostałe z sekcji „Zobacz, jak to
działa") — YouTube jako film niepubliczny albo Vimeo. Mają się rozchodzić, to jest
ich zadanie; zabezpieczanie ich to strata czasu.

**Nagrania płatnych szkoleń** — nigdy YouTube, nawet niepubliczny: adres da się
przesłać dalej, a filmy z YouTube pobiera się jednym poleceniem. Potrzebny jest
hosting, który potrafi trzy rzeczy:

- **podpisane adresy wygasające** — odtwarzacz dostaje adres ważny kilkadziesiąt
  minut, nie stały link do pliku;
- **ograniczenie do domeny** — film odtworzy się wyłącznie osadzony na
  eduplaner2026.pl, nie po wklejeniu adresu gdziekolwiek indziej;
- **znak wodny z adresem e-mail widza** nałożony na obraz, najlepiej ruchomy.

Vimeo w planach wyższych daje pierwsze dwa. Platformy do kursów (Cloudflare Stream,
Mux, polskie systemy kursowe) dają wszystkie trzy. Wybór należy do właścicielki
i zależy od ceny; wymagania są powyżej.

Do tego zasady po stronie konta: **jedno konto = jedna sesja naraz** i licznik
odtworzeń. Nie zatrzymają zdeterminowanego, ale wyłapią konto krążące po pokoju
nauczycielskim — a to jest realny scenariusz, nie hipotetyczny.

## Co jest zrobione w kodzie dziś

`index.html`, funkcja `embed()`:

- odtwarzacz `<video>` dostaje `controlslist="nodownload noremoteplayback"`,
  `disablepictureinpicture` i zablokowane menu prawego przycisku — znika przycisk
  pobierania i „zapisz wideo jako";
- YouTube osadzany jest przez `youtube-nocookie.com` z `modestbranding`,
  Vimeo z `dnt=1` — mniej śladów po widzu i mniej odnośników na zewnątrz;
- `allow` nie zawiera już `picture-in-picture`.

To są progi zwalniające, nie zamki. Nie opisuj ich klientowi jako zabezpieczenia.

## Czego nie wolno napisać na stronie

Żadnego „pliki są zabezpieczone przed kopiowaniem" ani „nagrań nie można pobrać".
To jest obietnica niemożliwa do dotrzymania, a przy sprzedaży placówce publicznej
— oświadczenie, z którego można zostać rozliczonym. Można napisać prawdę:
że egzemplarz jest imienny i że licencja obejmuje zespół placówki.
