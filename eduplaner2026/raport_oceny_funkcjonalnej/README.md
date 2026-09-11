# Raport Oceny Funkcjonalnej · EduPlaner 2026

Wzór opinii przedszkola/szkoły o funkcjonowaniu dziecka w obszarach ICF, przygotowany
dla rodzica i zespołu orzekającego poradni (Rozp. MEN z 2 marca 2026 r., Dz. U. 2026 poz. 428, § 7 ust. 6–7).

Styl graficzny wg wzoru IPET EduPlaner 2026: biały papier, lawendowe pola `#EFE9F9`, cienkie linie `#D9D0F0`, fiolet `#2D1B69` tylko w akcentach, pomarańczowe plakietki `#E74509`, tytuł wyśrodkowany. A4, 3 strony (okładka · metryczka i procedura · narzędzia i podpisy).

| Plik | Przeznaczenie |
|---|---|
| `Raport_Oceny_Funkcjonalnej.html` | wersja do aplikacji EduPlaner 2026 (ekran + druk A4, responsywna na telefon) |
| `Raport_Oceny_Funkcjonalnej.pdf` | gotowy wydruk / wysyłka dla rodzica |
| `Raport_Oceny_Funkcjonalnej.docx` | wersja edytowalna Word (Arial, nagłówek i stopka z paginacją) |
| `generate_raport_docx.js` | generator Worda (`npm i docx@9 && node generate_raport_docx.js Raport_Oceny_Funkcjonalnej.docx`) |

PDF powstaje z HTML przez Chromium:

```
chrome --headless --no-pdf-header-footer --print-to-pdf=Raport_Oceny_Funkcjonalnej.pdf Raport_Oceny_Funkcjonalnej.html
```
