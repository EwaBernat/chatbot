# Dostępność — WCAG w praktyce

Poziom odniesienia: WCAG 2.2 AA. Poniżej to, co realnie rozstrzyga o tym,
czy strona da się obsłużyć — bez wyliczanki wszystkich kryteriów.

## Dlaczego to nie jest formalność

Stronę placówki edukacyjnej otwierają osoby, które same pracują z niepełnosprawnością,
a często i osoby z nią żyjące. Strona, której nie da się obsłużyć klawiaturą albo
przeczytać przy słabszym wzroku, podważa wiarygodność oferty skuteczniej niż
jakikolwiek błąd merytoryczny. Do tego podmioty publiczne mają w tym zakresie
obowiązki ustawowe, a szkoła jest podmiotem publicznym.

## Kontrast

| Rodzaj tekstu | Wymagany kontrast |
|---|---|
| Zwykły (poniżej 24 px albo poniżej 19 px pogrubiony) | **4,5:1** |
| Duży (od 24 px albo od 19 px pogrubiony) | **3:1** |
| Elementy interfejsu: ramki pól, ikony niosące treść | **3:1** |

Pułapki, które łapie się dopiero pomiarem:

- **Biały tekst na kolorze marki.** Nasycone pomarańcze i czerwienie zwykle dają
  około 4:1 — czyli minimalnie za mało. Wystarczy przyciemnić kolor o kilka procent;
  marka tego nie odczuje, a przycisk zacznie spełniać wymóg. Warto trzymać osobny
  token na tło pod białym tekstem, żeby nie ruszać koloru akcentu w całej stronie.
- **Szary tekst pomocniczy.** Kolory w okolicy `#8A8399` wyglądają na wystarczające,
  a dają około 3,5:1. Wszystko, co jest zdaniem do przeczytania — podpis pod ceną,
  nota, opis techniczny — musi spełniać 4,5:1, nawet jeśli jest małe i szare z założenia.
- **Przezroczystość.** Kolor z alfą trzeba policzyć po nałożeniu na tło.
- **Ciemne tło.** Powyżej mniej więcej 12:1 jasne litery zaczynają się rozlewać.
  Kontrast ma być wysoki, ale nie maksymalny: zamiast czystej bieli na czerni
  lepiej działa jasny odcień o lekkim odchyleniu od tła sekcji.

## Klawiatura

- Każdy element interaktywny osiągalny tabulatorem, w kolejności zgodnej z układem.
- **Fokus musi być widoczny** — obrys o kontraście co najmniej 3:1 wobec tła.
  Usunięcie `outline` bez zastąpienia go czymś innym jest częstym i kosztownym błędem.
- Okno modalne: Escape zamyka, fokus wraca na element, który je otworzył.
- Zakładki i listy: strzałki przełączają, `aria-selected` mówi, co jest wybrane.
- Nic nie może zamykać użytkownika w pułapce fokusu.

## Formularze

- Każde pole ma etykietę powiązaną (`<label for>` albo `aria-label`).
  **Placeholder nie jest etykietą** — znika po wpisaniu pierwszego znaku
  i zwykle ma za niski kontrast.
- Błąd opisany słowem, nie samym kolorem ramki: co jest źle i co zrobić.
- Grupy pól (rodzaj kupującego) w `fieldset` z `legend`.
- Pola zbierające dane osobowe z `autocomplete`.
- Komunikat o wysłaniu formularza w obszarze `role="status"`, żeby czytnik go ogłosił.

## Struktura

- Jeden `h1`. Hierarchia bez przeskoków: po `h2` nie przychodzi `h4`.
- Nagłówek opisuje sekcję. „Rewelacja!" nie jest nagłówkiem.
- Punkty w `ul`/`ol`, nie w akapitach z myślnikami.
- Punkty orientacyjne: `header`, `nav`, `main`, `footer`.
- Odnośnik pomijający nawigację, jeśli menu jest długie.

## Obrazy

- Obraz niosący treść: `alt` opisujący **treść**, nie plik.
  Źle: `alt="zrzut ekranu"`. Dobrze: `alt="Ekran aplikacji: kartoteka dzieci z listą uczniów"`.
- Obraz dekoracyjny: `alt=""` (puste, ale obecne) — inaczej czytnik przeczyta nazwę pliku.
- Ikona jako jedyna treść przycisku: `aria-label` na przycisku.
- Wykres: opis słowny albo tabela z tymi samymi danymi obok.

## Cele dotykowe

Minimum **24×24 px**, w praktyce warto celować w 44 px. Wyjątek: odnośnik osadzony
w zdaniu — tam rozmiar wyznacza tekst i powiększanie go psuje akapit.

Checkbox 20×20 px jest za mały, nawet jeśli cała etykieta jest klikalna.
Taniej powiększyć pole niż tłumaczyć, dlaczego nie.

## Ruch i animacja

```css
@media (prefers-reduced-motion: reduce){
  *{animation:none!important;transition:none!important}
}
```

Nic nie miga częściej niż trzy razy na sekundę. Karuzela, która przewija się sama,
ma pauzę — a najlepiej nie przewija się sama.

## Kolor nigdy sam

Status, błąd, wyróżnienie — zawsze kolor **plus** coś jeszcze: ikona, słowo, kształt.
Około 8% mężczyzn nie odróżnia czerwieni od zieleni; czerwona ramka bez komunikatu
nie niesie dla nich żadnej informacji.

## Szybki test bez narzędzi

1. Odłóż mysz. Przejdź całą stronę tabulatorem — czy widać, gdzie jesteś?
2. Powiększ stronę do 200%. Czy coś się nakłada albo znika?
3. Zwęź okno do 390 px. Czy trzeba przewijać w bok?
4. Wyłącz obrazy. Czy strona nadal ma sens?
5. Przeczytaj na głos sam tekst odnośników. Czy „kliknij tutaj" mówi cokolwiek?
