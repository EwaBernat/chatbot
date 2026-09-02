# -*- coding: utf-8 -*-
"""Własne konspekty nauczycielki — dopisywane wprost do celu w tabeli FBA-T.

To samo, co bank celów SMART KPOF dostał w `moje_konspekty.py`, tylko dla druku
FBA-T: przy każdej komórce z celem jest **+**, który otwiera formularz o takiej
samej strukturze co konspekt gotowy (I cel · II pomoce · III metody · IV–V
realizacja · przebieg N/D · VI modyfikacje · wskazówka). Zapisany scenariusz
otwiera się i drukuje tak samo jak gotowy — ta sama karta, ten sam druk KC-3 A4.

Czego nie wolno tu zgubić
-------------------------
Ten moduł opisuje **zachowanie zastępcze**: plan PBS uczy innej drogi do tej
samej funkcji, nie odbiera dziecku funkcji. Dlatego formularz ma osobne pole
„zachowanie zastępcze”, wypełnione z wiersza tabeli — nauczycielka może je
doprecyzować pod swoje dziecko, ale nie da się napisać konspektu, który o nim
milczy. W banku KPOF tego pola nie ma, bo tam cel nie wisi na funkcji zachowania.

Konspekt jest **przypisany do celu**, nie do dokumentu: pamięta wersję wiekową,
numer wskaźnika i poziom wsparcia, z którego wyszedł. Cel edukacyjny czyta się
**na żywo z tabeli** — po poprawce w `dane_poziomy.py` konspekt nie zaczyna żyć
własną wersją celu, tak samo jak konspekty gotowe.

Pomoc dydaktyczna zostaje wspólna
---------------------------------
Własny scenariusz może **dołączyć sekcję VII gotowego konspektu tego wskaźnika**
— kartę pomocy ze zdjęciem i nagranym jej głosem poleceniem oraz materiał do
wycięcia. Klonujemy wtedy gotowy węzeł z dokumentu, nie kopiujemy mediów do
`localStorage`: nagranie waży 30 kB w base64 i po kilku konspektach magazyn
przeglądarki byłby pełny, a dziecko i tak ma słyszeć **to samo** polecenie, co
przy gotowym scenariuszu — inaczej pomoc przestaje być dla niego słowem.

Gdzie to siedzi
---------------
Dane trzymamy w `localStorage` pod kluczem `KLUCZ`, **innym niż klucz banku
KPOF** — te dwa zbiory nie mogą się mieszać. Dokument jest jednym plikiem HTML
otwieranym z dysku, bez serwera i bez konta, więc nie ma dokąd wysłać danych;
przeglądarka pamięta je między otwarciami i przeżywa przebudowę druku, bo klucz
nie zależy od nazwy pliku.

Czego `localStorage` nie zrobi: nie przeniesie konspektów na drugi komputer ani
do innej przeglądarki. Dlatego panel ma **zapis kopii do pliku JSON i wczytanie
jej z powrotem** — to jest właściwa droga przenoszenia, nie dodatek, i panel
mówi o tym wprost. Gdy przeglądarka blokuje `localStorage` (tryb prywatny),
edytor **nadal działa** w pamięci karty i pokazuje ostrzeżenie, zamiast udawać,
że zapisało się na stałe.

Uwagi do składania
------------------
* `STYL` do arkusza dokumentu, `SZKIELET` raz na dokument, `panel()` raz na
  wersję wiekową, `skrypt()` **przed** `konspekt_fba.SKRYPT`.
* Kolejność skryptów jest istotna: plus łapiemy w fazie przechwytywania na
  `document` i wygaszamy zdarzenie, żeby nie otworzył się przy okazji gotowy
  konspekt komórki. Oba nasłuchy wiszą na tym samym węźle, więc decyduje
  kolejność rejestracji — nasz musi być pierwszy.
* Okno podglądu jest zwykłym `.kmodal`, więc dziedziczy wszystko: Escape,
  kliknięcie w tło, `[data-zamknij]`, `[data-druk]` i reguły druku. Edytor
  celowo nim **nie** jest — Escape nie może kasować niezapisanego formularza.
"""

import json

import dane_poziomy as P

KLUCZ = "eduplaner2026.moje-konspekty-fba.v1"

# ——— arkusz stylów ————————————————————————————————————————————————————————
STYL = """
/* ——— własne konspekty (druk FBA-T) ——— */
/* Plus jest widoczny zawsze, tylko przygaszony. Na hoverze byłby nie do
   znalezienia na tablecie, a w tym projekcie już raz przepadła funkcja
   schowana pod najechaniem myszą. */
.mkf-add{position:absolute; top:3px; right:3px; width:19px; height:19px; padding:0;
  display:grid; place-items:center; border:1px solid var(--line-2); border-radius:6px;
  background:var(--paper); color:var(--szary); font:700 12px/1 inherit; cursor:pointer;
  opacity:.45; transition:opacity .12s; z-index:2}
td.g:hover .mkf-add, td.g:focus-within .mkf-add, .mkf-add:focus-visible{opacity:1}
.mkf-add:hover{border-color:var(--accent); color:var(--accent); opacity:1}
td.g.mkf-ma .mkf-add{opacity:1; border-color:var(--accent); color:var(--accent); font-size:10px}
/* Miejsce na plus robimy pływakiem w pierwszym wierszu, a nie wcięciem całego
   akapitu: plus siedzi w prawym górnym rogu, więc reszta wierszy ma biec do
   samej krawędzi komórki — inaczej cele robią się o wiersz dłuższe i tabela
   rośnie o kartkę. Pływak wisi na **komórce**, nie na tekście celu: wpięty
   w `.tresc` wciągał róg z przyciskiem do prostokąta tekstu i kliknięcie
   w cel trafiało w plus zamiast otwierać gotowy konspekt. */
@media screen{td.g.haskon::before{content:""; float:right; width:22px; height:15px}}

.mkf-panel{margin:0 0 11px; border:1px solid var(--line); border-radius:10px;
  background:var(--paper); overflow:hidden}
.mkf-panel > summary{list-style:none; cursor:pointer; padding:9px 15px; background:var(--ink);
  color:#fff; font:700 11.5px/1.4 inherit; letter-spacing:.02em; display:flex;
  align-items:center; gap:10px}
.mkf-panel > summary::-webkit-details-marker{display:none}
.mkf-panel > summary .ile{margin-left:auto; font-weight:600; opacity:.85; font-size:10.5px}
.mkf-panel[open] > summary .rozwin, .mkf-panel:not([open]) > summary .zwin{display:none}
.mkf-tresc{padding:13px 15px 15px}
.mkf-info{margin:0 0 11px; font-size:10.5px; line-height:1.6; color:var(--szary)}
.mkf-info b{color:var(--ink)}
.mkf-ostrz{margin:0 0 11px; padding:8px 11px; border-radius:7px; font-size:10.5px;
  line-height:1.55; background:var(--t2); border:1px solid var(--r2); color:var(--tekst)}
.mkf-ostrz b{color:var(--p2)}
.mkf-narzedzia{display:flex; flex-wrap:wrap; gap:8px; margin:0 0 12px}
.mkf-lista{display:grid; grid-template-columns:repeat(auto-fill,minmax(248px,1fr)); gap:7px}
.mkf-poz{display:flex; align-items:center; gap:9px; min-height:40px; padding:7px 11px;
  border:1px solid var(--line); border-radius:9px; background:var(--paper);
  font:600 11px/1.35 inherit; color:var(--ink); text-align:left; cursor:pointer}
.mkf-poz:hover{border-color:var(--accent); color:var(--accent)}
.mkf-poz b{flex:0 0 42px; font:700 9.5px/1 "JetBrains Mono",ui-monospace,"Courier New",monospace;
  color:var(--szary); letter-spacing:.02em}
.mkf-poz:hover b{color:var(--accent)}
.mkf-poz .tyt{flex:1 1 auto}
.mkf-poz .lvl{flex:0 0 auto; width:18px; height:18px; border-radius:50%; display:grid;
  place-items:center; font:700 8.5px/1 inherit; color:#fff}
.mkf-poz .lvl.p3{background:var(--p3)} .mkf-poz .lvl.p2{background:var(--p2)}
.mkf-poz .lvl.p1{background:var(--p1)}
.mkf-pusto{margin:0; font-size:10.5px; color:var(--szary); font-style:italic}

/* edytor — własne okno, bo Escape nie może kasować niezapisanej pracy */
.mkfmodal{position:fixed; inset:0; z-index:70; display:none; overflow:auto;
  background:rgba(36,28,58,.62); padding:22px 16px}
.mkfmodal.open{display:block}
.mkfcard{max-width:940px; margin:0 auto; background:var(--paper); border-radius:14px;
  padding:21px 23px 19px; box-shadow:0 18px 60px rgba(36,28,58,.35)}
.mkf-head{display:flex; align-items:baseline; gap:12px; padding-bottom:10px;
  border-bottom:2px solid var(--ink); margin-bottom:13px}
.mkf-head h3{margin:0; font-size:18px; color:var(--ink)}
.mkf-head .skad{margin-left:auto; font-size:10.5px; color:var(--szary); text-align:right;
  line-height:1.5}
.mkf-cel{margin:0 0 14px; padding:10px 12px; border-radius:9px; background:var(--soft);
  border:1px solid var(--line); font-size:11px; line-height:1.6}
.mkf-cel .lab{display:block; font-weight:700; color:var(--ink); font-size:9.5px;
  letter-spacing:.08em; text-transform:uppercase; margin-bottom:4px}
.mkf-pola{display:grid; grid-template-columns:1fr 1fr; gap:11px 15px}
.mkf-pole{display:flex; flex-direction:column; gap:4px}
.mkf-pole.szer{grid-column:1/-1}
.mkf-pole label{font:700 9.5px/1.3 inherit; letter-spacing:.07em; text-transform:uppercase;
  color:var(--ink)}
.mkf-pole .podp{font:400 10px/1.5 inherit; text-transform:none; letter-spacing:0; color:var(--szary)}
.mkf-pole input, .mkf-pole textarea, .mkf-pole select{font:400 11.5px/1.6 inherit;
  color:var(--tekst); padding:7px 9px; border:1px solid var(--line); border-radius:7px;
  background:var(--paper); width:100%; box-sizing:border-box; resize:vertical}
.mkf-pole input:focus, .mkf-pole textarea:focus, .mkf-pole select:focus{outline:2px solid var(--accent);
  outline-offset:1px; border-color:var(--accent)}
.mkf-grupa{grid-column:1/-1; margin:7px 0 0; padding-top:9px; border-top:1px solid var(--line);
  font:700 9.5px/1.3 inherit; letter-spacing:.08em; text-transform:uppercase; color:var(--accent)}
.mkf-zgoda{grid-column:1/-1; display:flex; gap:9px; align-items:flex-start; padding:9px 11px;
  border:1px solid var(--line); border-radius:8px; background:var(--soft); font-size:11px;
  line-height:1.55}
.mkf-zgoda input{width:16px; height:16px; flex:0 0 auto; margin-top:2px}
.mkf-zgoda b{color:var(--ink)}
.mkf-prz{grid-column:1/-1; display:flex; flex-direction:column; gap:7px}
.mkf-prz-w{display:grid; grid-template-columns:22px 1fr 1fr 26px; gap:8px; align-items:start}
.mkf-prz-w .nr{padding-top:8px; font:700 10.5px/1 "JetBrains Mono",ui-monospace,monospace;
  color:var(--szary); text-align:right}
.mkf-prz-w textarea{min-height:50px}
.mkf-usun-w{align-self:start; margin-top:4px; width:24px; height:24px; padding:0; border-radius:6px;
  border:1px solid var(--line); background:var(--paper); color:var(--szary); cursor:pointer;
  font:600 13px/1 inherit}
.mkf-usun-w:hover{border-color:var(--p3); color:var(--p3)}
.mkf-stopka{display:flex; flex-wrap:wrap; gap:9px; align-items:center; margin-top:17px;
  padding-top:13px; border-top:1px solid var(--line)}
.mkf-stopka .rozdziel{margin-left:auto}
.mkf-blad{margin:10px 0 0; padding:8px 11px; border-radius:7px; font-size:11px;
  background:var(--t3); border:1px solid var(--r3); color:var(--p3); display:none}
.mkf-blad.jest{display:block}
@media (max-width:760px){.mkf-pola{grid-template-columns:1fr}
  .mkf-prz-w{grid-template-columns:20px 1fr 24px}
  .mkf-prz-w textarea:last-of-type{grid-column:2}}
/* `display:grid` z klasy bije regułę przeglądarki `[hidden]{display:none}`, bo
   styl autora ma pierwszeństwo przed stylem przeglądarki — bez tej linijki pola
   własnej karty pokazywały się także przy karcie gotowej. */
.mkf-pola[hidden]{display:none}
.mkf-media{grid-column:1/-1; display:grid; grid-template-columns:1fr 1fr; gap:12px;
  margin-top:2px}   /* klasa `szer` działa tylko na `.mkf-pole` */
.mkf-media-poz{border:1px solid var(--line); border-radius:9px; padding:10px 12px; background:var(--soft)}
.mkf-media-poz > b{display:block; font:700 9.5px/1.3 inherit; letter-spacing:.07em;
  text-transform:uppercase; color:var(--ink); margin-bottom:6px}
.mkf-podglad{height:104px; border:1px dashed var(--line-2); border-radius:7px; background:var(--paper);
  background-size:cover; background-position:center; display:grid; place-items:center;
  font-size:10px; color:var(--szary); text-align:center; padding:0 10px}
.mkf-podglad.ma{border-style:solid}
.mkf-media-btn{display:flex; flex-wrap:wrap; gap:6px; margin-top:7px}
.mkf-media-btn .chipbtn{font-size:10.5px; padding:5px 11px}
.mkf-uwaga{display:block; margin-top:6px; font-size:9.5px; line-height:1.5; color:var(--szary)}
.mkf-miejsce{margin:10px 0 0; font-size:10px; color:var(--szary)}
.mkf-miejsce b{color:var(--ink)}
.mkf-miejsce.pelno b{color:var(--p3)}

/* Zachowanie zastępcze nad celem — we własnym konspekcie to jedyne miejsce,
   w którym widać, czego właściwie uczymy zamiast zachowania trudnego. */
.kzast{margin:11px 0 0; padding:8px 12px; border-left:4px solid var(--accent);
  border-radius:0 8px 8px 0; background:var(--soft); font-size:11px; line-height:1.55}
.kzast b{color:var(--ink)}
.kzast span{display:block; color:var(--szary); font-size:9.5px; margin-top:2px}
@media print{.mkf-add, .mkf-panel, .mkfmodal{display:none !important}
  .kzast{font-size:9.5px; padding:6px 10px; margin-top:8px}}
"""

# ——— dwa okna, raz na dokument ————————————————————————————————————————————
SZKIELET = """
<div class="kmodal" id="mkf-widok" data-wersja="" data-wsk="" role="dialog" aria-modal="true"
  aria-label="Mój konspekt">
  <div class="kcard" id="mkf-widok-tresc"></div>
</div>
<div class="mkfmodal" id="mkf-edytor" role="dialog" aria-modal="true"
  aria-label="Edytor własnego konspektu">
  <div class="mkfcard">
    <div class="mkf-head">
      <h3 id="mkf-edytor-tytul">Nowy konspekt własny</h3>
      <div class="skad" id="mkf-edytor-skad"></div>
    </div>
    <div class="mkf-cel" id="mkf-edytor-cel"></div>
    <form id="mkf-form" class="mkf-pola" autocomplete="off">
      <div class="mkf-pole szer"><label for="mkf-tytul">Tytuł zajęć
        <span class="podp">— pole wymagane</span></label>
        <input id="mkf-tytul" maxlength="90" required></div>
      <div class="mkf-pole szer"><label for="mkf-podtytul">Czego dotyczy
        <span class="podp">— jedno zdanie pod tytułem</span></label>
        <input id="mkf-podtytul" maxlength="140"></div>
      <div class="mkf-pole szer"><label for="mkf-zast">Zachowanie zastępcze
        <span class="podp">— co dziecko robi zamiast zachowania trudnego, w tej samej funkcji</span></label>
        <input id="mkf-zast" maxlength="160"></div>
      <div class="mkf-pole"><label for="mkf-czas">Czas</label>
        <input id="mkf-czas" maxlength="30" placeholder="20 min"></div>
      <div class="mkf-pole"><label for="mkf-forma">Forma</label>
        <input id="mkf-forma" maxlength="60" placeholder="indywidualnie przy stoliku"></div>
      <div class="mkf-pole"><label for="mkf-cykl">Cykl</label>
        <input id="mkf-cykl" maxlength="40" placeholder="3× w tygodniu"></div>
      <div class="mkf-pole"><label for="mkf-poziom">Poziom wsparcia</label>
        <select id="mkf-poziom">__OPCJE__</select></div>

      <div class="mkf-grupa">I · Cel terapeutyczny</div>
      <div class="mkf-pole szer"><label for="mkf-ter">Cel terapeutyczny
        <span class="podp">— co dziecko zrobi, w ilu sytuacjach i w jakim czasie</span></label>
        <textarea id="mkf-ter" rows="3"></textarea></div>
      <div class="mkf-pole szer"><label for="mkf-kryt">Kryterium — czym mierzysz</label>
        <input id="mkf-kryt" maxlength="160" placeholder="arkusz obserwacji · 5 sytuacji w tygodniu"></div>

      <div class="mkf-grupa">II–V · Pomoce, metody, rodzaj zajęć</div>
      <div class="mkf-pole"><label for="mkf-pomoce">Pomoce dydaktyczne
        <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mkf-pomoce" rows="5"></textarea></div>
      <div class="mkf-pole"><label for="mkf-metody">Metody i formy działań
        <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mkf-metody" rows="5"></textarea></div>
      <div class="mkf-pole szer"><label for="mkf-rodzaj">Rodzaj zajęć</label>
        <input id="mkf-rodzaj" maxlength="120"
          placeholder="Zajęcia z zakresu pozytywnych oddziaływań behawioralnych (PBS)"></div>

      <div class="mkf-grupa">Przebieg zajęć — czynność nauczyciela (N) i reakcja dziecka (D)</div>
      <div class="mkf-prz" id="mkf-przebieg"></div>
      <div class="mkf-pole szer"><button type="button" class="chipbtn" id="mkf-dodaj-wiersz">
        + Dodaj krok</button></div>

      <div class="mkf-grupa">VI · Modyfikacja przy ocenie czerwonej / żółtej / zielonej</div>
      <div class="mkf-pole"><label for="mkf-mod3">Poziom III · czerwona
        <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mkf-mod3" rows="4"></textarea></div>
      <div class="mkf-pole"><label for="mkf-mod2">Poziom II · żółta
        <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mkf-mod2" rows="4"></textarea></div>
      <div class="mkf-pole szer"><label for="mkf-mod1">Poziom I · zielona — rozszerzenie
        <span class="podp">— jedna w wierszu</span></label>
        <textarea id="mkf-mod1" rows="3"></textarea></div>
      <div class="mkf-pole szer"><label for="mkf-wsk">Wskazówka dla prowadzącego</label>
        <textarea id="mkf-wsk" rows="2"></textarea></div>

      <div class="mkf-grupa">VII · Materiały do wydruku</div>
      <div class="mkf-pole szer"><label for="mkf-vii">Karta pomocy dydaktycznej</label>
        <select id="mkf-vii">
          <option value="gotowa">Gotowa — karta tego wskaźnika, ze zdjęciem i nagranym poleceniem</option>
          <option value="wlasna">Własna — moje zdjęcie, moje kroki, moje nagranie</option>
          <option value="brak">Bez karty pomocy</option>
        </select></div>
      <label class="mkf-zgoda"><input type="checkbox" id="mkf-arkusz" checked>
        <span><b>Dołącz materiał do wycięcia z gotowego konspektu</b> — karty i pasek kolejności
        z biblioteki symboli EduPlaner. Ten sam symbol tutaj, na tablicy AAC i w planie dnia:
        symbol, który zmienia wygląd między materiałami, przestaje być dla dziecka słowem.</span></label>

      <div class="mkf-pola" id="mkf-wlasna" hidden style="grid-column:1/-1; gap:11px 15px">
        <div class="mkf-pole szer"><label for="mkf-p-nazwa">Nazwa pomocy
          <span class="podp">— wymagana przy własnej karcie</span></label>
          <input id="mkf-p-nazwa" maxlength="70" placeholder="Pudełko pierwszego kroku"></div>
        <div class="mkf-pole"><label for="mkf-p-przygotuj">Co przygotować
          <span class="podp">— jedno w wierszu</span></label>
          <textarea id="mkf-p-przygotuj" rows="5"></textarea></div>
        <div class="mkf-pole"><label for="mkf-p-kroki">Jak użyć — trzy kroki
          <span class="podp">— jeden w wierszu</span></label>
          <textarea id="mkf-p-kroki" rows="5"></textarea></div>
        <div class="mkf-pole szer"><label for="mkf-p-wsk">Wskazówka do pomocy
          <span class="podp">— dla dorosłego, nie dla dziecka</span></label>
          <input id="mkf-p-wsk" maxlength="180"></div>
        <div class="mkf-pole szer"><label for="mkf-p-polecenie">Polecenie dla dziecka
          <span class="podp">— w drugiej osobie, prostymi słowami: krótkie zdania, żadnych
          trudnych wyrazów</span></label>
          <input id="mkf-p-polecenie" maxlength="180"
            placeholder="Weź jedną rzecz z pudełka i połóż ją przed sobą."></div>
        <div class="mkf-media szer">
          <div class="mkf-media-poz"><b>Zdjęcie pomocy</b>
            <div class="mkf-podglad" id="mkf-foto-podglad">nie dodano zdjęcia</div>
            <div class="mkf-media-btn">
              <button type="button" class="chipbtn" id="mkf-foto-wybierz">Wybierz zdjęcie</button>
              <button type="button" class="chipbtn" id="mkf-foto-usun">Usuń</button>
            </div>
            <span class="mkf-uwaga">Zdjęcie zmniejszamy do 900 px i zapisujemy jako JPEG. Bez tego
            jedno zdjęcie z telefonu zajęłoby cały magazyn przeglądarki.</span>
          </div>
          <div class="mkf-media-poz"><b>Nagranie polecenia</b>
            <div class="mkf-podglad" id="mkf-audio-podglad">nie dodano nagrania</div>
            <div class="mkf-media-btn">
              <button type="button" class="chipbtn" id="mkf-audio-wybierz">Wybierz nagranie</button>
              <button type="button" class="chipbtn" id="mkf-audio-sluchaj">▶ Posłuchaj</button>
              <button type="button" class="chipbtn" id="mkf-audio-usun">Usuń</button>
            </div>
            <span class="mkf-uwaga">MP3, M4A, WAV albo OGG do 600 kB — tyle waży kilkanaście sekund
            mowy. Nagranie z ElevenLabs Twoim głosem waży około 30 kB.</span>
          </div>
        </div>
      </div>
    </form>
    <p class="mkf-blad" id="mkf-blad"></p>
    <div class="mkf-stopka">
      <button type="button" class="chipbtn" id="mkf-anuluj">Anuluj</button>
      <button type="button" class="chipbtn rozdziel" id="mkf-usun"
        style="border-color:var(--r3); color:var(--p3)">Usuń konspekt</button>
      <button type="button" class="chipbtn mocny" id="mkf-zapisz">Zapisz konspekt</button>
    </div>
  </div>
</div>
<input type="file" id="mkf-plik" accept="application/json,.json" hidden>
<input type="file" id="mkf-foto-plik" accept="image/*" hidden>
<input type="file" id="mkf-audio-plik" accept="audio/*,.mp3,.m4a,.wav,.ogg" hidden>
"""


def przycisk_dodania():
    """Plus w rogu komórki z celem — jedyna droga do własnego konspektu.

    Trzymamy go w źródle zamiast dorabiać skryptem: 225 komórek to na tym
    dokumencie ułamek promila wagi, a przycisk działa od pierwszej klatki.
    """
    return ('<button class="mkf-add" type="button"'
            ' title="Dodaj własny konspekt do tego celu"'
            ' aria-label="Dodaj własny konspekt do tego celu">+</button>')


def panel(kod_wersji):
    """Panel „Moje konspekty" dla jednej wersji wiekowej — wypełnia go skrypt."""
    return f"""  <details class="mkf-panel" data-mkf-panel="{kod_wersji}">
    <summary>Moje konspekty<span class="rozwin"> — kliknij, aby rozwinąć</span>
<span class="zwin"> — kliknij, aby zwinąć</span><span class="ile" data-mkf-ile>brak</span></summary>
    <div class="mkf-tresc">
      <p class="mkf-ostrz" data-mkf-ostrz hidden></p>
      <p class="mkf-info">Własny scenariusz dopisujesz <b>plusem w komórce z celem</b> — najedź
      myszą na dowolny cel w tabeli poniżej i kliknij <b>+</b> w jego prawym górnym rogu.
      Konspekt zostaje przy tym celu, czyta jego treść <b>na żywo z tabeli</b> i otwiera się
      tak samo jak gotowy, razem z drukiem A4. Zapisuje się <b>w tej przeglądarce</b>, więc
      żeby przenieść go na inny komputer albo mieć kopię — zapisz plik JSON poniżej.</p>
      <div class="mkf-narzedzia">
        <button type="button" class="chipbtn" data-mkf-eksport>Zapisz kopię do pliku (JSON)</button>
        <button type="button" class="chipbtn" data-mkf-import>Wczytaj kopię z pliku</button>
      </div>
      <div class="mkf-lista" data-mkf-lista></div>
      <p class="mkf-pusto" data-mkf-pusto>Nie masz jeszcze własnych konspektów w tej wersji.</p>
      <p class="mkf-miejsce" data-mkf-miejsce></p>
    </div>
  </details>"""


# ——— skrypt ————————————————————————————————————————————————————————————————
SKRYPT = """
/* Własne konspekty nauczycielki — dopisywane do celu w tabeli FBA-T.
   Całość w jednym domknięciu; zdarzenia obsługujemy delegacją, bo pozycje
   panelu i przyciski w karcie konspektu powstają dopiero w trakcie pracy. */
(function(){
  const KLUCZ='__KLUCZ__';
  const POZIOMY=__POZIOMY__;      // kod → {rzym, nazwa, kryt, hor}
  const FUNKCJE=__FUNKCJE__;      // I…V → nazwa funkcji zachowania
  const WERSJE=__WERSJE__;        // A/B/C → przedział wieku
  let pamiec=null;                // kopia robocza, gdy localStorage jest zablokowany
  let edytowany=null;             // rekord w edycji albo null przy nowym konspekcie
  let kontekstBiezacy=null;       // cel, z którego wyszedł otwarty formularz
  let media={foto:null, audio:null};  // zdjęcie i nagranie własnej karty pomocy
  let sluchane=null;                  // podgląd nagrania w edytorze
  const SZEROKOSC_FOTO=900;           // tyle samo, co zdjęcia pomocy gotowych
  const LIMIT_AUDIO=600*1024;

  const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,
    c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const linie=s=>String(s||'').split('\\n').map(x=>x.trim()).filter(Boolean);
  const kid=(nr,w)=>'kon-'+w+'-'+String(nr).replace('.','-');

  function magazynDziala(){
    try{const k='__mkf_test__'; localStorage.setItem(k,'1'); localStorage.removeItem(k); return true;}
    catch(e){return false;}
  }
  const MAGAZYN=magazynDziala();

  function wczytaj(){
    if(!MAGAZYN) return pamiec||(pamiec=[]);
    try{const s=localStorage.getItem(KLUCZ); const t=s?JSON.parse(s):[]; return Array.isArray(t)?t:[];}
    catch(e){return [];}
  }
  /* Zwraca 'ok', 'pamiec' (magazyn zablokowany) albo 'brak-miejsca' — komunikat
     „nie udało się zapisać" bez powodu nie mówi nauczycielce, co ma zrobić,
     a przy własnych zdjęciach i nagraniach magazyn kończy się naprawdę. */
  function zapisz(lista){
    if(!MAGAZYN){pamiec=lista; return 'pamiec';}
    try{localStorage.setItem(KLUCZ,JSON.stringify(lista)); return 'ok';}
    catch(e){
      pamiec=lista;
      return (e && (e.name==='QuotaExceededError'||e.code===22)) ? 'brak-miejsca' : 'blad';
    }
  }
  function zajete(){
    try{return (MAGAZYN?(localStorage.getItem(KLUCZ)||''):JSON.stringify(pamiec||[])).length;}
    catch(e){return 0;}
  }
  const waga=b=>b>=1048576?(b/1048576).toFixed(1).replace('.',',')+' MB':Math.round(b/1024)+' kB';
  const noweId=()=>'mkf'+Date.now().toString(36)+Math.random().toString(36).slice(2,7);

  /* Kontekst celu bierzemy z atrybutów komórki i wiersza — tabela już je niesie,
     więc nie powtarzamy danych w osobnym obiekcie JS ani nie parsujemy tekstu. */
  function kontekst(td){
    const tr=td.closest('tr');
    return {
      wersja: td.dataset.wersja||'',
      nr: td.dataset.wsk||'',
      poziom: td.dataset.lvl||'p2',
      wskaznik: ((tr.querySelector('td.wsk b')||{}).textContent||'').trim(),
      zastepcze: tr.dataset.zast||'',
      funkcja: tr.dataset.fun||''
    };
  }
  /* Cel z tabeli dla wybranego poziomu — zawsze na świeżo, żeby konspekt nie
     zaczął żyć własną wersją celu po poprawce w `dane_poziomy.py`. */
  function zTabeli(k,poziom){
    const td=document.querySelector('#w-'+k.wersja+' tr[data-wsk="'+CSS.escape(k.nr)
      +'"] td.g[data-lvl="'+(poziom||k.poziom)+'"]');
    if(!td) return {cel:'', ram:''};
    return {cel:(td.querySelector('.tresc')||{}).textContent||'',
            ram:(td.querySelector('.ram')||{}).textContent||''};
  }

  /* ——— podgląd konspektu ——— */
  function widok(k){
    const t=zTabeli(k,k.poziom), poz=POZIOMY[k.poziom];
    const li=x=>x.map(y=>'<li>'+esc(y)+'</li>').join('');
    const pusty='<li style="color:var(--szary); font-style:italic">— nie wypełniono</li>';
    const prz=(k.przebieg||[]).map((p,i)=>
      '<tr><td class="lp">'+(i+1)+'</td><td>'+esc(p[0])+'</td><td>'+esc(p[1])+'</td></tr>').join('');
    const mod=(kod,klasa,etykieta,tresc)=>
      '<div class="kmod '+klasa+(k.poziom===kod?' wyb':'')+'"><b>'+etykieta+'</b>'
      +'<ul class="klista">'+(tresc&&tresc.length?li(tresc):pusty)+'</ul></div>';
    return `
    <button class="kclose" data-zamknij aria-label="Zamknij konspekt" title="Zamknij (Esc)">✕</button>
    <div class="khead">
      <span class="mark" role="img" aria-label="Logo PCTP"></span>
      <div>
        <div class="kw">EduPlaner 2026</div>
        <div class="ks">Konspekt własny · funkcja ${esc(k.funkcja)} · ${esc(FUNKCJE[k.funkcja]||'')}
          · wersja ${esc(k.wersja)} · ${esc(WERSJE[k.wersja]||'')} · wskaźnik ${esc(k.nr)}</div>
      </div>
      <span class="kpill">Mój konspekt</span>
    </div>
    <div class="kmeta" style="grid-template-columns:1.6fr 1fr 1fr">
      <div class="field"><b>Dotyczy dziecka</b><span class="dots"></span></div>
      <div class="field"><b>Grupa</b><span class="dots"></span></div>
      <div class="field"><b>Data</b><span class="dots"></span></div>
    </div>
    <div class="ktitle">
      <span class="kp">Konspekt zajęć · druk KC-3 · opracowanie własne</span>
      <div class="ksfera">Wskaźnik ${esc(k.nr)} · ${esc(k.wskaznik)}</div>
      <h3>${esc(k.tytul)}</h3>
      <div class="kpod">${esc(k.podtytul||'')}</div>
    </div>
    <div class="kmeta">
      <div class="field"><b>Czas</b><span class="val">${esc(k.czas||'—')}</span></div>
      <div class="field"><b>Forma</b><span class="val">${esc(k.forma||'—')}</span></div>
      <div class="field"><b>Cykl</b><span class="val">${esc(k.cykl||'—')}</span></div>
      <div class="field"><b>Poziom wsparcia</b><span class="klvl ${k.poziom}">${poz.rzym}</span></div>
    </div>
    <div class="kzast"><b>Zachowanie zastępcze:</b> ${esc(k.zastepcze||'—')}
      <span>plan uczy innej drogi do tej samej funkcji, nie odbiera dziecku funkcji</span></div>
    <div class="ksec"><span class="sq">I</span><h4>Cel SMART</h4><span class="line"></span></div>
    <div class="kcele">
      <div class="kcel edu jeden">
        <div class="kchead">Cel edukacyjny — z tabeli FBA-T · ${poz.nazwa}</div>
        <div class="kvar on" data-lvl="${k.poziom}">
          <div class="ktresc">${esc(t.cel)}</div>
          <div class="kkryt"><b>Kryterium:</b> ${esc(t.ram)}</div></div>
      </div>
      <div class="kcel ter">
        <div class="kchead">Cel terapeutyczny</div>
        <div class="ktresc">${esc(k.ter||'—')}</div>
        <div class="kkryt"><b>Kryterium:</b> ${esc(k.kryt||'—')}</div>
      </div>
    </div>
    <div class="kdwie">
      <div><div class="ksec"><span class="sq">II</span><h4>Pomoce dydaktyczne</h4>
        <span class="line"></span></div>
        <ul class="klista">${(k.pomoce||[]).length?li(k.pomoce):pusty}</ul></div>
      <div><div class="ksec"><span class="sq">III</span><h4>Metody i formy działań</h4>
        <span class="line"></span></div>
        <ul class="klista">${(k.metody||[]).length?li(k.metody):pusty}</ul></div>
    </div>
    <div class="kdwie" style="align-items:end">
      <div><div class="ksec"><span class="sq">IV</span><h4>Sposób realizacji</h4>
        <span class="line"></span></div>
        <div class="krodzaj" style="font-style:italic">Tabela poniżej ↓</div></div>
      <div><div class="ksec"><span class="sq">V</span><h4>Rodzaj zajęć</h4>
        <span class="line"></span></div>
        <div class="krodzaj">${esc(k.rodzaj||'—')}</div></div>
    </div>
    <p class="kkurs">Konkretne czynności nauczyciela (N) i odpowiadające im oczekiwane reakcje
      i umiejętności dziecka (D).</p>
    <table class="ktab">
      <thead><tr><th style="width:26px">Lp.</th><th style="width:47%">Czynności nauczyciela (N)</th>
        <th>Oczekiwane reakcje i umiejętności dziecka (D)</th></tr></thead>
      <tbody>${prz||'<tr><td class="lp">1</td><td>—</td><td>—</td></tr>'}</tbody>
    </table>
    <div class="ksec"><span class="sq">VI</span><h4>Modyfikacja przy ocenie żółtej / czerwonej</h4>
      <span class="line"></span></div>
    <p class="kkurs">Modyfikację stosuje się, gdy brak progresu w dwóch kolejnych sesjach.
      Zielona — rozszerzenie przy pełnym sukcesie. Wybrany poziom wyróżniony.</p>
    <div class="kmods">
      ${mod('p3','m3','Poziom III · Czerwona',k.mod3)}
      ${mod('p2','m2','Poziom II · Żółta',k.mod2)}
      ${mod('p1','m1','Poziom I · Zielona',k.mod1)}
    </div>
    <div class="kwsk"><b>Wskazówka dla prowadzącego:</b> ${esc(k.wskazowka||'—')}</div>
    <div data-mkf-vii></div>
    <div class="kfoot">
      <button class="chipbtn" data-zamknij>✕ Zamknij i wróć do tabeli</button>
      <button class="chipbtn" data-mkf-edytuj="${k.id}">Edytuj konspekt</button>
      <button class="chipbtn mocny" data-druk>Drukuj konspekt A4</button>
    </div>
    <p class="kesc">zamkniesz też klawiszem <b>Esc</b> albo kliknięciem w tło poza kartą</p>`;
  }

  /* Własna karta pomocy — ten sam wzór KC-4 co karty gotowe, żeby wyglądała
     i drukowała się identycznie. Zdjęcie i nagranie siedzą w rekordzie jako
     data-URI, a przycisk gra dzięki nasłuchowi delegowanemu na dokumencie. */
  function kartaWlasna(k){
    const p=k.pomoc||{};
    const li=t=>(t||[]).map(x=>'<li>'+esc(x)+'</li>').join('');
    const pusto='<li style="color:var(--szary); font-style:italic">— nie wypełniono</li>';
    const foto=p.foto
      ? '<div class="pom-foto" style="background-image:url('+p.foto+')" role="img"'
        +' aria-label="Pomoc dydaktyczna: '+esc(p.nazwa||'')+'"></div>'
      : '<div class="pom-foto brak">zdjęcie poglądowe<br>nie zostało dodane</div>';
    const btn=p.audio
      ? '<button type="button" class="pom-play" data-src="'+p.audio+'"'
        +' aria-label="Posłuchaj polecenia">▶</button>'
      : '<button type="button" class="pom-play" disabled'
        +' title="Nagranie nie zostało dodane">▶</button>';
    return '<section class="pom">'
      +'<div class="pom-head"><span class="kp">Pomoc dydaktyczna · druk KC-4 · własna</span>'
      +'<h5>'+esc(p.nazwa||'Pomoc własna')+'</h5>'
      +'<span class="wiek">'+esc(WERSJE[k.wersja]||'')+'</span></div>'
      +'<div class="pom-ciało">'+foto+'<div class="pom-tresc">'
      +'<h6>Co przygotować</h6><ul>'+((p.przygotuj||[]).length?li(p.przygotuj):pusto)+'</ul>'
      +'<h6>Jak użyć — trzy kroki</h6><ol>'+((p.kroki||[]).length?li(p.kroki):pusto)+'</ol>'
      +'<div class="pom-glos">'+btn+'<span class="tekst"><b>Polecenie dla dziecka · jej głosem</b>'
      +'„'+esc(p.polecenie||'—')+'”</span></div>'
      +'</div></div>'
      +'<div class="pom-wsk"><b>Wskazówka:</b> '+esc(p.wskazowka||'—')+'</div></section>';
  }

  /* Sekcja VII składa się z trzech niezależnych rzeczy: karty pomocy (gotowej
     albo własnej), arkusza do wycięcia z gotowego konspektu i niczego. Kartę
     i arkusz gotowe **klonujemy** z dokumentu, zamiast kopiować ich zdjęcia
     i nagrania do magazynu przeglądarki — jedno nagranie to 30 kB w base64,
     a magazyn kończy się po kilkunastu konspektach. */
  function dolaczVII(k,gniazdo){
    const tryb=k.vii||(k.zPomoca===false?'brak':'gotowa');
    const zArk=(k.zArkuszem!==undefined)?k.zArkuszem:(k.zPomoca!==false);
    const zrodlo=document.getElementById(kid(k.nr,k.wersja));
    const klony=[];
    if(tryb==='gotowa'&&zrodlo){const p=zrodlo.querySelector('.pom'); if(p) klony.push(p);}
    if(zArk&&zrodlo){const z=zrodlo.querySelector('.zal'); if(z) klony.push(z);}
    const wlasna=(tryb==='wlasna')?kartaWlasna(k):'';
    if(!klony.length&&!wlasna) return;
    const skad=tryb==='wlasna'
      ? 'Twoja karta pomocy'+(zArk?' i materiał do wycięcia z gotowego konspektu':'')+'.'
      : 'Karta pomocy'+(zArk?' i materiał do wycięcia':'')+' z gotowego konspektu tego wskaźnika '
        +'— to samo nagrane polecenie i ten sam symbol, co przy scenariuszu gotowym.';
    gniazdo.innerHTML='<div class="ksec"><span class="sq">VII</span>'
      +'<h4>Materiały do wydruku</h4><span class="line"></span></div>'
      +'<p class="kkurs">'+skad+'</p>'+wlasna;
    klony.forEach(c=>gniazdo.appendChild(c.cloneNode(true)));
  }

  function pokazKonspekt(id){
    const k=wczytaj().find(x=>x.id===id); if(!k) return;
    /* Gotowy konspekt tej komórki mógł zostać otwarty wcześniej; dwa otwarte
       okna naraz wyszłyby na wydruku jako dwa konspekty pod rząd. */
    document.querySelectorAll('.kmodal.open').forEach(m=>m.classList.remove('open'));
    /* Podgląd celowo nie niesie `data-wersja`: wydruk zeszytu wybiera konspekty
       po tym atrybucie i wciągnąłby do niego ten jeden, akurat otwarty własny. */
    const m=document.getElementById('mkf-widok');
    const c=document.getElementById('mkf-widok-tresc');
    c.innerHTML=widok(k);
    dolaczVII(k,c.querySelector('[data-mkf-vii]'));
    m.classList.add('open'); document.body.style.overflow='hidden';
    const b=m.querySelector('.kclose'); if(b) b.focus();
  }

  /* ——— edytor ——— */
  function wierszPrzebiegu(n,d){
    const box=document.getElementById('mkf-przebieg');
    const w=document.createElement('div'); w.className='mkf-prz-w';
    w.innerHTML='<span class="nr"></span>'
      +'<textarea placeholder="N — co robi nauczyciel" data-n></textarea>'
      +'<textarea placeholder="D — co robi dziecko" data-d></textarea>'
      +'<button type="button" class="mkf-usun-w" title="Usuń ten krok" aria-label="Usuń krok">×</button>';
    w.querySelector('[data-n]').value=n||'';
    w.querySelector('[data-d]').value=d||'';
    box.appendChild(w); numeruj();
  }
  const numeruj=()=>[...document.querySelectorAll('#mkf-przebieg .mkf-prz-w')]
      .forEach((w,i)=>w.querySelector('.nr').textContent=(i+1)+'.');

  function otworzEdytor(dane,k){
    edytowany=dane||null;
    const ctx=dane||k;
    kontekstBiezacy=ctx;
    document.getElementById('mkf-edytor-tytul').textContent=
      dane?'Edytuj własny konspekt':'Nowy konspekt własny';
    document.getElementById('mkf-edytor-skad').innerHTML=
      'wersja '+esc(ctx.wersja)+' · '+esc(WERSJE[ctx.wersja]||'')+'<br>funkcja '+esc(ctx.funkcja)
      +' · '+esc(FUNKCJE[ctx.funkcja]||'')+' · wskaźnik '+esc(ctx.nr);
    const f=id=>document.getElementById(id);
    f('mkf-tytul').value=dane?dane.tytul||'':'';
    f('mkf-podtytul').value=dane?dane.podtytul||'':'';
    f('mkf-zast').value=(dane?dane.zastepcze:k.zastepcze)||'';
    f('mkf-czas').value=dane?dane.czas||'':'20 min';
    f('mkf-forma').value=dane?dane.forma||'':'';
    f('mkf-cykl').value=dane?dane.cykl||'':'';
    f('mkf-poziom').value=(dane?dane.poziom:k.poziom)||'p2';
    f('mkf-ter').value=dane?dane.ter||'':'';
    f('mkf-kryt').value=dane?dane.kryt||'':'';
    f('mkf-pomoce').value=dane?(dane.pomoce||[]).join('\\n'):'';
    f('mkf-metody').value=dane?(dane.metody||[]).join('\\n'):'';
    f('mkf-rodzaj').value=dane?dane.rodzaj||'':'';
    f('mkf-mod3').value=dane?(dane.mod3||[]).join('\\n'):'';
    f('mkf-mod2').value=dane?(dane.mod2||[]).join('\\n'):'';
    f('mkf-mod1').value=dane?(dane.mod1||[]).join('\\n'):'';
    f('mkf-wsk').value=dane?dane.wskazowka||'':'';
    const p=(dane&&dane.pomoc)||{};
    f('mkf-vii').value=dane?(dane.vii||(dane.zPomoca===false?'brak':'gotowa')):'gotowa';
    f('mkf-arkusz').checked=dane
      ? ((dane.zArkuszem!==undefined)?dane.zArkuszem:(dane.zPomoca!==false)) : true;
    f('mkf-p-nazwa').value=p.nazwa||'';
    f('mkf-p-przygotuj').value=(p.przygotuj||[]).join('\\n');
    f('mkf-p-kroki').value=(p.kroki||[]).join('\\n');
    f('mkf-p-wsk').value=p.wskazowka||'';
    f('mkf-p-polecenie').value=p.polecenie||'';
    media={foto:p.foto||null, audio:p.audio||null};
    pokazMedia(); przelaczVII();
    document.getElementById('mkf-przebieg').innerHTML='';
    const kroki=(dane&&dane.przebieg&&dane.przebieg.length)?dane.przebieg:[['',''],['',''],['','']];
    kroki.forEach(p=>wierszPrzebiegu(p[0],p[1]));
    document.getElementById('mkf-usun').style.display=dane?'':'none';
    document.getElementById('mkf-blad').classList.remove('jest');
    odswiezCelWEdytorze(ctx);
    document.getElementById('mkf-edytor').classList.add('open');
    document.body.style.overflow='hidden';
    f('mkf-tytul').focus();
  }
  function odswiezCelWEdytorze(ctx){
    const p=document.getElementById('mkf-poziom').value, t=zTabeli(ctx,p);
    document.getElementById('mkf-edytor-cel').innerHTML=
      '<span class="lab">Cel edukacyjny z tabeli · '+POZIOMY[p].nazwa+'</span>'
      +esc(t.cel)+'<br><span style="color:var(--szary)">'+esc(t.ram)
      +' · wskaźnik: '+esc(ctx.wskaznik)+'</span>';
  }
  function zamknijEdytor(){
    document.getElementById('mkf-edytor').classList.remove('open');
    if(!document.querySelector('.kmodal.open')) document.body.style.overflow='';
    edytowany=null; kontekstBiezacy=null;
  }

  function zbierz(ctx){
    const v=id=>document.getElementById(id).value.trim();
    const przebieg=[...document.querySelectorAll('#mkf-przebieg .mkf-prz-w')]
      .map(w=>[w.querySelector('[data-n]').value.trim(), w.querySelector('[data-d]').value.trim()])
      .filter(p=>p[0]||p[1]);
    return {
      id: ctx.id||noweId(),
      wersja: ctx.wersja, nr: ctx.nr, poziom: v('mkf-poziom'),
      wskaznik: ctx.wskaznik, funkcja: ctx.funkcja,
      zastepcze: v('mkf-zast'),
      tytul: v('mkf-tytul'), podtytul: v('mkf-podtytul'),
      czas: v('mkf-czas'), forma: v('mkf-forma'), cykl: v('mkf-cykl'),
      ter: v('mkf-ter'), kryt: v('mkf-kryt'),
      pomoce: linie(v('mkf-pomoce')), metody: linie(v('mkf-metody')), rodzaj: v('mkf-rodzaj'),
      przebieg, mod3: linie(v('mkf-mod3')), mod2: linie(v('mkf-mod2')), mod1: linie(v('mkf-mod1')),
      wskazowka: v('mkf-wsk'),
      vii: v('mkf-vii'),
      zArkuszem: document.getElementById('mkf-arkusz').checked,
      /* Własną kartę trzymamy niezależnie od tego, która jest teraz wybrana:
         przełączenie na kartę gotową nie może skasować zdjęcia i nagrania,
         które nauczycielka dopiero co wgrała. Miejsce zwalnia się przyciskiem
         „Usuń" przy zdjęciu albo nagraniu — świadomie, a nie przy okazji. */
      pomoc: pomocZFormularza(),
      utworzono: ctx.utworzono||new Date().toISOString(),
      zmieniono: new Date().toISOString()
    };
  }
  function pomocZFormularza(){
    const v=id=>document.getElementById(id).value.trim();
    const p={nazwa:v('mkf-p-nazwa'), przygotuj:linie(v('mkf-p-przygotuj')),
             kroki:linie(v('mkf-p-kroki')), wskazowka:v('mkf-p-wsk'),
             polecenie:v('mkf-p-polecenie'), foto:media.foto, audio:media.audio};
    const puste = !p.nazwa && !p.przygotuj.length && !p.kroki.length && !p.wskazowka
                  && !p.polecenie && !p.foto && !p.audio;
    return puste ? null : p;
  }
  function blad(t){
    const b=document.getElementById('mkf-blad'); b.textContent=t; b.classList.add('jest');
  }

  /* ——— zdjęcie i nagranie własnej karty ——— */
  function przelaczVII(){
    document.getElementById('mkf-wlasna').hidden =
      document.getElementById('mkf-vii').value !== 'wlasna';
  }
  function pokazMedia(){
    const f=document.getElementById('mkf-foto-podglad');
    f.classList.toggle('ma', !!media.foto);
    f.style.backgroundImage = media.foto ? 'url('+media.foto+')' : '';
    f.textContent = media.foto ? '' : 'nie dodano zdjęcia';
    const a=document.getElementById('mkf-audio-podglad');
    a.classList.toggle('ma', !!media.audio);
    a.textContent = media.audio
      ? 'nagranie gotowe · '+waga(Math.round(media.audio.length*0.75))
      : 'nie dodano nagrania';
    document.getElementById('mkf-audio-sluchaj').disabled=!media.audio;
  }
  /* Zdjęcie z telefonu ma 3–5 MB; w magazynie przeglądarki mieści się kilka
     takich i koniec. Zmniejszamy je do tej samej szerokości, co zdjęcia pomocy
     gotowych, i zapisujemy jako JPEG — na ekranie i w druku A4 nie widać różnicy. */
  function wczytajZdjecie(plik){
    const r=new FileReader();
    r.onload=()=>{
      const im=new Image();
      im.onload=()=>{
        const sk=Math.min(1, SZEROKOSC_FOTO/im.width);
        const c=document.createElement('canvas');
        c.width=Math.round(im.width*sk); c.height=Math.round(im.height*sk);
        c.getContext('2d').drawImage(im,0,0,c.width,c.height);
        media.foto=c.toDataURL('image/jpeg',0.82);
        pokazMedia();
      };
      im.onerror=()=>alert('Nie udało się odczytać tego pliku jako zdjęcia. '
        +'Wybierz plik JPG albo PNG.');
      im.src=r.result;
    };
    r.readAsDataURL(plik);
  }
  function wczytajNagranie(plik){
    if(plik.size>LIMIT_AUDIO){
      alert('To nagranie waży '+waga(plik.size)+', a karta przyjmuje do '+waga(LIMIT_AUDIO)+'.\\n\\n'
        +'Skróć je albo zapisz w niższej jakości — kilkanaście sekund mowy w 40 kbps mono '
        +'to około 60 kB. Nagranie z ElevenLabs Twoim głosem waży zwykle 30 kB.');
      return;
    }
    const r=new FileReader();
    r.onload=()=>{media.audio=r.result; pokazMedia();};
    r.onerror=()=>alert('Nie udało się odczytać tego pliku jako nagrania.');
    r.readAsDataURL(plik);
  }

  /* ——— panele i oznaczenia w tabeli ——— */
  function odswiez(){
    const lista=wczytaj();
    document.querySelectorAll('td.g.mkf-ma').forEach(td=>{
      td.classList.remove('mkf-ma');
      const b=td.querySelector('.mkf-add');
      if(b){b.textContent='+'; b.title='Dodaj własny konspekt do tego celu';}
    });
    lista.forEach(k=>{
      const td=document.querySelector('#w-'+k.wersja+' tr[data-wsk="'+CSS.escape(k.nr)
        +'"] td.g[data-lvl="'+k.poziom+'"]');
      if(!td) return;
      td.classList.add('mkf-ma');
      const b=td.querySelector('.mkf-add');
      if(b){b.textContent='✎'; b.title='Mój konspekt: '+k.tytul;}
    });
    document.querySelectorAll('[data-mkf-panel]').forEach(p=>{
      const w=p.dataset.mkfPanel, moje=lista.filter(k=>k.wersja===w);
      p.querySelector('[data-mkf-ile]').textContent=
        moje.length?(moje.length+(moje.length===1?' konspekt własny':' konspektów własnych')):'brak';
      p.querySelector('[data-mkf-lista]').innerHTML=moje.map(k=>
        '<button type="button" class="mkf-poz" data-mkf-otworz="'+k.id+'">'
        +'<b>'+esc(k.nr)+'</b><span class="tyt">'+esc(k.tytul)+'</span>'
        +'<span class="lvl '+k.poziom+'">'+POZIOMY[k.poziom].rzym+'</span></button>').join('');
      p.querySelector('[data-mkf-pusto]').hidden=moje.length>0;
      const m=p.querySelector('[data-mkf-miejsce]'), b=zajete();
      m.innerHTML=lista.length
        ? 'Twoje konspekty zajmują <b>'+waga(b)+'</b> w pamięci tej przeglądarki '
          +'(mieści się w niej około 5 MB). Zdjęcie własnej pomocy to około 100 kB, '
          +'nagranie — od 30 kB.'
        : '';
      m.classList.toggle('pelno', b>4*1048576);
      const o=p.querySelector('[data-mkf-ostrz]');
      if(!MAGAZYN){
        o.hidden=false;
        o.innerHTML='<b>Ta przeglądarka nie pozwala zapisać danych witryny</b> (tryb prywatny albo '
          +'wyłączone dane lokalne). Konspekty będą działać do zamknięcia karty — zapisz je '
          +'do pliku JSON, zanim ją zamkniesz.';
      } else o.hidden=true;
    });
  }

  /* ——— kopia do pliku ——— */
  function eksport(){
    const lista=wczytaj();
    if(!lista.length){alert('Nie masz jeszcze żadnego własnego konspektu do zapisania.'); return;}
    const dane={dokument:'EduPlaner 2026 · druk FBA-T · moje konspekty', wersjaZapisu:1,
                zapisano:new Date().toISOString(), konspekty:lista};
    const b=new Blob([JSON.stringify(dane,null,2)],{type:'application/json'});
    const a=document.createElement('a');
    a.href=URL.createObjectURL(b);
    a.download='moje_konspekty_FBA_'+new Date().toISOString().slice(0,10)+'.json';
    document.body.appendChild(a); a.click();
    setTimeout(()=>{URL.revokeObjectURL(a.href); a.remove();},1000);
  }
  function importuj(plik){
    const r=new FileReader();
    r.onload=()=>{
      let dane;
      try{dane=JSON.parse(r.result);}
      catch(e){alert('To nie jest plik z konspektami — nie udało się go odczytać.'); return;}
      const nowe=Array.isArray(dane)?dane:(dane&&Array.isArray(dane.konspekty)?dane.konspekty:null);
      if(!nowe){alert('W tym pliku nie ma konspektów.'); return;}
      const lista=wczytaj(), wg={}; lista.forEach(k=>wg[k.id]=k);
      let dodane=0, zastapione=0, obce=0;
      nowe.forEach(k=>{
        if(!k||!k.id||!k.tytul) return;
        /* Plik z banku KPOF ma inne klucze celu (numer twierdzenia zamiast
           wskaźnika FBA) — wpuszczony tutaj dałby konspekty wiszące w próżni. */
        if(!k.nr||!POZIOMY[k.poziom]||!WERSJE[k.wersja]||!/^(I|II|III|IV|V)\\.[1-5]$/.test(k.nr)){
          obce++; return;
        }
        if(wg[k.id]) zastapione++; else dodane++;
        wg[k.id]=k;
      });
      zapisz(Object.values(wg)); odswiez();
      alert('Wczytano kopię: '+dodane+' nowych, '+zastapione+' zaktualizowanych.'
        +(obce?'\\n\\nPominięto '+obce+' pozycji spoza tego druku — to konspekty z innego dokumentu.':''));
    };
    r.readAsText(plik);
  }

  /* ——— zdarzenia ——— */
  /* Plus łapiemy w fazie przechwytywania i wygaszamy zdarzenie do końca:
     konspekty gotowe też nasłuchują kliknięć na `document` w tej samej fazie,
     więc bez `stopImmediatePropagation` otwierałyby się dwa okna naraz i tyle
     samo wychodziło z drukarki. Ten skrypt musi iść przed skryptem konspektów —
     w tej samej fazie decyduje kolejność rejestracji. */
  document.addEventListener('click',e=>{
    const dod=e.target.closest('.mkf-add'); if(!dod) return;
    e.preventDefault(); e.stopImmediatePropagation();
    const td=dod.closest('td.g'), k=kontekst(td);
    const moj=wczytaj().find(x=>x.wersja===k.wersja&&x.nr===k.nr&&x.poziom===k.poziom);
    if(moj) pokazKonspekt(moj.id); else otworzEdytor(null,k);
  },true);
  /* Komórka ma `role="button"`, więc Enter na plusie wywołałby jeszcze nasłuch
     klawiatury konspektów gotowych. Kliknięcie i tak powstanie z akcji domyślnej. */
  document.addEventListener('keydown',e=>{
    if(e.target.closest&&e.target.closest('.mkf-add')&&(e.key==='Enter'||e.key===' '))
      e.stopImmediatePropagation();
  },true);

  document.addEventListener('click',e=>{
    const otw=e.target.closest('[data-mkf-otworz]');
    if(otw){pokazKonspekt(otw.dataset.mkfOtworz); return;}
    const edy=e.target.closest('[data-mkf-edytuj]');
    if(edy){
      const k=wczytaj().find(x=>x.id===edy.dataset.mkfEdytuj);
      if(k){document.getElementById('mkf-widok').classList.remove('open'); otworzEdytor(k,k);}
      return;
    }
    if(e.target.closest('[data-mkf-eksport]')){eksport(); return;}
    if(e.target.closest('[data-mkf-import]')){document.getElementById('mkf-plik').click(); return;}
    if(e.target.closest('.mkf-usun-w')){
      const w=e.target.closest('.mkf-prz-w');
      if(document.querySelectorAll('#mkf-przebieg .mkf-prz-w').length>1){w.remove(); numeruj();}
      else{w.querySelectorAll('textarea').forEach(t=>t.value='');}
      return;
    }
  });
  document.getElementById('mkf-vii').addEventListener('change',przelaczVII);
  document.getElementById('mkf-foto-wybierz').addEventListener('click',
    ()=>document.getElementById('mkf-foto-plik').click());
  document.getElementById('mkf-audio-wybierz').addEventListener('click',
    ()=>document.getElementById('mkf-audio-plik').click());
  document.getElementById('mkf-foto-usun').addEventListener('click',()=>{media.foto=null; pokazMedia();});
  document.getElementById('mkf-audio-usun').addEventListener('click',()=>{
    if(sluchane){sluchane.pause(); sluchane=null;}
    media.audio=null; pokazMedia();
  });
  document.getElementById('mkf-audio-sluchaj').addEventListener('click',()=>{
    if(!media.audio) return;
    if(sluchane){sluchane.pause(); sluchane=null; return;}
    sluchane=new Audio(media.audio);
    sluchane.onended=()=>{sluchane=null;};
    sluchane.play();
  });
  document.getElementById('mkf-foto-plik').addEventListener('change',e=>{
    if(e.target.files&&e.target.files[0]) wczytajZdjecie(e.target.files[0]);
    e.target.value='';
  });
  document.getElementById('mkf-audio-plik').addEventListener('change',e=>{
    if(e.target.files&&e.target.files[0]) wczytajNagranie(e.target.files[0]);
    e.target.value='';
  });
  document.getElementById('mkf-dodaj-wiersz').addEventListener('click',()=>wierszPrzebiegu('',''));
  document.getElementById('mkf-poziom').addEventListener('change',()=>{
    if(kontekstBiezacy) odswiezCelWEdytorze(kontekstBiezacy);
  });
  document.getElementById('mkf-anuluj').addEventListener('click',()=>{
    if(confirm('Zamknąć edytor bez zapisania zmian?')) zamknijEdytor();
  });
  document.getElementById('mkf-zapisz').addEventListener('click',()=>{
    const k=zbierz(kontekstBiezacy||{});
    if(!k.tytul){blad('Konspekt musi mieć tytuł — bez niego nie znajdziesz go później na liście.');
      document.getElementById('mkf-tytul').focus(); return;}
    if(!k.zastepcze){blad('Wpisz zachowanie zastępcze — to ono jest treścią planu PBS. '
      +'Możesz zostawić brzmienie z tabeli.');
      document.getElementById('mkf-zast').focus(); return;}
    if(k.vii==='wlasna'&&!(k.pomoc&&k.pomoc.nazwa)){
      blad('Własna karta pomocy musi mieć nazwę — bez niej karta wychodzi z drukarki bez tytułu.');
      document.getElementById('mkf-p-nazwa').focus(); return;}
    const lista=wczytaj().filter(x=>x.id!==k.id);
    lista.push(k);
    const wynik=zapisz(lista);
    zamknijEdytor(); odswiez();
    if(wynik==='brak-miejsca')
      alert('Konspekt jest gotowy, ale w pamięci tej przeglądarki skończyło się miejsce.\\n\\n'
        +'Zapisz kopię do pliku JSON (przycisk w panelu „Moje konspekty"), a potem usuń zdjęcie '
        +'albo nagranie z któregoś konspektu — zdjęcie zajmuje około 100 kB, nagranie od 30 kB.\\n\\n'
        +'Do zamknięcia karty wszystko działa normalnie.');
    else if(wynik!=='ok')
      alert('Konspekt jest gotowy, ale przeglądarka nie pozwoliła go zapisać na stałe. '
        +'Zapisz kopię do pliku JSON, zanim zamkniesz kartę.');
    pokazKonspekt(k.id);
  });
  document.getElementById('mkf-usun').addEventListener('click',()=>{
    const ctx=edytowany; if(!ctx) return;
    if(!confirm('Usunąć konspekt „'+ctx.tytul+'"? Tej operacji nie da się cofnąć.')) return;
    zapisz(wczytaj().filter(x=>x.id!==ctx.id));
    zamknijEdytor(); odswiez();
  });
  document.getElementById('mkf-plik').addEventListener('change',e=>{
    if(e.target.files&&e.target.files[0]) importuj(e.target.files[0]);
    e.target.value='';
  });

  odswiez();
})();
"""


def _opcje():
    """Poziomy w selekcie — kryterium i horyzont wprost z `dane_poziomy`."""
    return "".join(
        f'<option value="{kod}">{nazwa} · {kryt} sytuacji · weryfikacja po '
        f'{hor.replace("tygodni", "tygodniach")}</option>'
        for kod, nazwa, kryt, hor, _o in P.POZIOMY)


def szkielet():
    return SZKIELET.replace("__OPCJE__", _opcje())


def skrypt():
    poziomy = {kod: {"rzym": nazwa.split()[-1], "nazwa": nazwa, "kryt": kryt, "hor": hor}
               for kod, nazwa, kryt, hor, _o in P.POZIOMY}
    funkcje = {rzym: f["nazwa"] for rzym, f in P.CELE.items()}
    wersje = dict(P.WERSJE)
    return (SKRYPT.replace("__KLUCZ__", KLUCZ)
            .replace("__POZIOMY__", json.dumps(poziomy, ensure_ascii=False))
            .replace("__FUNKCJE__", json.dumps(funkcje, ensure_ascii=False))
            .replace("__WERSJE__", json.dumps(wersje, ensure_ascii=False)))
