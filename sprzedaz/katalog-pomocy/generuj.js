/* Katalog pomocy dydaktycznych — skład HTML z dane.js.  node generuj.js     */
const { esc, lista, zapisz } = require("../wspolne/styl-katalogu.js");
const { TELEFON } = require("../wspolne/kontakt.js");
const { KATEGORIE, POMOCE, ZESTAWY } = require("./dane.js");

const kat = (id) => KATEGORIE.find((k) => k.id === id);
const wgKodu = (kod) => POMOCE.find((p) => p.kod === kod);

const tytulowa = () => `<section class="tytulowa">
  <div class="nad">Pomorskie Centrum Terapii Pedagogicznej · Koszalin</div>
  <h1>Katalog pomocy<br>dydaktycznych</h1>
  <h1 style="font-size:28px;color:var(--pomarancz);margin-top:8px">Rok szkolny 2026/2027</h1>
  <div class="rule"></div>
  <p class="lead">Dwadzieścia dwie pomoce w czterech kategoriach — od zeszytu o emocjach po szablony
    dokumentacji. Wszystkie do samodzielnego wydruku: kupujesz raz, drukujesz tyle egzemplarzy,
    ilu masz dzieci, w zakresie licencji.</p>
  <div class="pasy">
    ${KATEGORIE.map((k) => `<div style="background:${k.hex};color:#fff">${k.id} · ${esc(k.nazwa.split(" i ")[0])}</div>`).join("")}
    <div style="background:var(--brzoskwinia);color:var(--fiolet)">4 zestawy</div>
  </div>
  <div class="metryczka">
    <div><span class="etyk">W katalogu</span><b>22 pomoce</b></div>
    <div><span class="etyk">Postać</span><b>PDF · Word · Excel</b></div>
    <div><span class="etyk">Zestawy</span><b>4 pakiety</b></div>
    <div><span class="etyk">Dostęp</span><b>dożywotni</b></div>
  </div>
  <div class="stopka-dok">
    <strong>Mirosława Ewa Jurczyszyn</strong>, pedagog specjalny · Pomorskie Centrum Terapii Pedagogicznej, Koszalin<br>
    kontakt@eduplaner2026.pl · ${TELEFON} · www.eduplaner2026.pl · EduPlaner 2026
  </div>
</section>`;

const wstep = () => `<section>
  <div class="nad">Zanim wybierzesz</div>
  <h1>Jak dobrać pomoc do potrzeby</h1><div class="rule"></div>
  <p class="lead">Najczęstszy błąd przy kompletowaniu materiałów to kupowanie po temacie, a nie po
    trudności. Poniżej — od czego zacząć, jeżeli problem brzmi tak, jak w pierwszej kolumnie.</p>
  <table><thead><tr><th style="width:44%">Jeżeli trudność brzmi tak…</th>
    <th style="width:34%">Zacznij od</th><th style="width:22%">Potem dołóż</th></tr></thead><tbody>
  ${[
    ["Dziecko wybucha i nie umie powiedzieć, o co chodzi", "A3 — Karty emocji", "A5, B2, C3"],
    ["Nastolatek nie nazywa tego, co czuje", "A1 — Zeszyt „Kolorowy Świat Emocji”", "A4, A6"],
    ["Grupa przedszkolna, chcę pracować z emocjami systematycznie", "A2 — Konspekty 3–4 lata", "A3, A6, A7"],
    ["Dziecko nie mówi", "B1 — Zestaw startowy kart", "B2, B3, B4"],
    ["Zmiana planu kończy się płaczem albo ucieczką", "C1 — Plan dnia obrazkowy", "A5, C2"],
    ["Uczeń wychodzi z sali w trakcie lekcji", "B2 — Karty „Przerwa” i „Pomoc”", "C2, C3"],
    ["IPET-y piszemy długo i nie wiadomo, czy dobrze", "D2 — Szablon IPET", "D1, D5, D7"],
    ["Nie potrafimy udowodnić, że program zadziałał", "D5 — Karta obserwacji celów", "A4, A7, D2"],
    ["Zachowania trudne wracają mimo rozmów", "D6 — Arkusz ABC", "C2, C3"],
    ["Dyrektor pyta o liczby, a my szukamy w teczkach", "D4 — Baza Uczniów", "D1, D2, D3"],
  ].map(([a, b, c]) => `<tr><td>${esc(a)}</td><td><strong>${esc(b)}</strong></td>
    <td style="font-size:8.8px;color:var(--szept)">${esc(c)}</td></tr>`).join("")}
  </tbody></table>

  <h2>Cztery kategorie</h2>
  ${KATEGORIE.map((k) => `<div class="blok" style="border-left:4px solid ${k.hex}">
    <span class="etyk" style="color:${k.hex}">Kategoria ${k.id}</span>
    <strong style="font-size:13px">${esc(k.nazwa)}</strong><br>${esc(k.opis)}</div>`).join("")}

  <div class="blok akcent"><strong>Wszystko drukujesz sam.</strong> Pomoce dostajesz jako pliki —
    PDF do wydruku, Word i Excel do edycji. Nie ma wysyłki ani czekania: plik trafia do Państwa
    od razu po opłaceniu zamówienia, a dostęp do zakupionego wydania jest dożywotni.</div>
</section>`;

const zestawienie = () => `<section class="czesc">
  <div class="nad">Wszystkie pomoce</div>
  <h1>Zestawienie</h1><div class="rule"></div>
  <p class="lead">Dwadzieścia dwie pozycje w czterech kategoriach. Kod pomocy podajemy przy zamówieniu.</p>
  <table><thead><tr><th style="width:7%">Kod</th><th style="width:31%">Pomoc</th>
    <th style="width:26%">Postać i format</th><th style="width:22%">Licencja</th>
    <th style="width:14%">Cena</th></tr></thead><tbody>
  ${KATEGORIE.map((k) => {
    const w = POMOCE.filter((p) => p.kat === k.id).map((p) => `<tr>
      <td style="font-weight:700;color:${k.hex}">${p.kod}</td>
      <td><strong>${esc(p.nazwa)}</strong>${p.polecane ? ' <span class="wstazka" style="margin:0">Polecane</span>' : ""}<br>
          <span style="font-size:8.6px;color:var(--szept)">${esc(p.podtytul)}</span></td>
      <td style="font-size:8.8px">${esc(p.postac)}<br><span style="color:var(--szept)">${esc(p.format)}</span></td>
      <td style="font-size:8.8px">${esc(p.licencja)}</td>
      <td style="font-weight:700;color:var(--pomarancz)">[ cena ]</td></tr>`).join("");
    return `<tr><td colspan="5" style="background:${k.hex};color:#fff;font-family:var(--naglowek);
      font-weight:700;font-size:9px;letter-spacing:.14em;text-transform:uppercase">
      Kategoria ${k.id} — ${esc(k.nazwa)}</td></tr>${w}`;
  }).join("")}
  </tbody></table>
</section>`;

function kartaKategorii(k) {
  const pozycje = POMOCE.filter((p) => p.kat === k.id).map((p) => `
  <div class="poz"><div class="pas" style="background:${k.hex}"></div>
    <div class="srodek">
      ${p.polecane ? '<div class="wstazka">Polecane</div>' : ""}
      <div class="kod">Kod ${p.kod}</div>
      <h3>${esc(p.nazwa)}</h3>
      <div class="pod" style="color:${k.hex}">${esc(p.podtytul)}</div>
      <p class="opis">${esc(p.opis)}</p>
      <div class="fakty">
        <div><span class="etyk">Postać</span><b style="font-size:10px">${esc(p.postac)}</b></div>
        <div><span class="etyk">Format</span><b style="font-size:10px">${esc(p.format)}</b></div>
        <div><span class="etyk">Licencja</span><b style="font-size:10px">${esc(p.licencja)}</b></div>
        <div><span class="etyk">Cena</span><b style="color:var(--pomarancz)">[ cena ]</b></div>
      </div>
      <div class="dwie">
        <div><span class="etyk">Dla kogo</span>${lista(p.dlaKogo, k.hex)}</div>
        <div><span class="etyk">Jak używać</span>${lista(p.jakUzywac, "var(--zielony)")}</div>
      </div>
      <div style="border-top:1px dashed var(--kreska);margin-top:10px;padding-top:8px;
                  font-size:8.8px;color:var(--szept)">
        <strong style="color:${k.hex}">Pasuje do:</strong> ${esc(p.pasuje.join(" · "))}</div>
    </div></div>`).join("");

  return `<section class="czesc">
  <div class="nad" style="color:${k.hex}">Kategoria ${k.id}</div>
  <h1>${esc(k.nazwa)}</h1>
  <div class="rule" style="background:${k.hex}"></div>
  <p class="lead">${esc(k.opis)}</p>
  ${pozycje}</section>`;
}

const zestawy = () => `<section class="czesc">
  <div class="nad">Taniej i spójniej</div>
  <h1>Cztery zestawy</h1><div class="rule"></div>
  <p class="lead">Pomoce, które działają razem, zamawiane w jednym pakiecie. Zestaw jest tańszy niż
    suma pozycji i ma spójne oznaczenia — te same symbole wracają w planie dnia, na kartach
    i na etykietach szafek.</p>
  ${ZESTAWY.map((z) => {
    const skl = z.sklad.map(wgKodu);
    return `<div class="poz"><div class="pas" style="background:var(--pomarancz)"></div>
    <div class="srodek">
      <div class="kod">Kod ${z.kod}</div>
      <h3>${esc(z.nazwa)}</h3>
      <p class="opis">${esc(z.opis)}</p>
      <div class="fakty">
        <div><span class="etyk">Pozycji</span><b>${skl.length}</b></div>
        <div><span class="etyk">Postać</span><b style="font-size:10px">pliki do pobrania</b></div>
        <div><span class="etyk">Dostęp</span><b style="font-size:10px">dożywotni</b></div>
        <div><span class="etyk">Cena zestawu</span><b style="color:var(--pomarancz)">[ cena ]</b></div>
      </div>
      <span class="etyk">W zestawie</span>
      ${lista(skl.map((p) => `${p.kod} — ${p.nazwa}`), "var(--pomarancz)")}
    </div></div>`;
  }).join("")}
</section>`;

const warunki = () => `<section class="czesc">
  <div class="nad">Sprawy organizacyjne</div>
  <h1>Licencje i zamówienie</h1><div class="rule"></div>

  <h2>Trzy licencje</h2>
  <table><thead><tr><th style="width:22%">Licencja</th><th style="width:30%">Dla kogo</th>
    <th style="width:34%">Co obejmuje</th><th style="width:14%">Cena</th></tr></thead><tbody>
    <tr><td><strong>Indywidualna</strong></td><td>Jeden specjalista — nauczyciel, terapeuta, pedagog, psycholog lub rodzic</td>
      <td>Wydruk dla własnych uczniów bez limitu kopii; praca indywidualna i w małej grupie</td>
      <td style="font-weight:700;color:var(--pomarancz)">[ cena ]</td></tr>
    <tr><td><strong>Placówkowa</strong></td><td>Jedna szkoła, przedszkole, poradnia lub ośrodek</td>
      <td>Wszystko z indywidualnej; korzystanie przez wszystkich specjalistów w placówce, wydruki dla wszystkich jej dzieci, plik w wewnętrznej sieci</td>
      <td style="font-weight:700;color:var(--pomarancz)">[ cena ]</td></tr>
    <tr><td><strong>Szkoleniowa</strong></td><td>Prowadzący szkolenia i warsztaty</td>
      <td>Wszystko z placówkowej; prezentowanie materiałów podczas szkoleń i webinarów, materiały ćwiczeniowe dla uczestników</td>
      <td style="font-weight:700;color:var(--pomarancz)">[ cena ]</td></tr>
  </tbody></table>

  <div class="dwie">
    <div>
      <h3>Wolno</h3>
      ${lista(["drukować dowolną liczbę egzemplarzy w zakresie swojej licencji",
               "wypełniać, kopiować pojedyncze strony i karty do zajęć",
               "wycinać i laminować karty oraz materiały do gry",
               "pokazywać materiały rodzicom dzieci, z którymi się pracuje",
               "przechowywać kopię zapasową pliku na własnych nośnikach"], "var(--zielony)")}
    </div>
    <div>
      <h3>Nie wolno</h3>
      ${lista(["odsprzedawać materiałów ani ich fragmentów",
               "udostępniać plików poza swoją licencją",
               "publikować stron w internecie i mediach społecznościowych",
               "usuwać oznaczeń autorki i wydawcy"], "#B8350D")}
    </div>
  </div>

  <h2>Wydruk i przygotowanie</h2>
  <div class="dwie">
    <div>${lista(["Drukarka A4 wystarcza do wszystkich pomocy; formaty A3 i większe — w punkcie ksero",
                  "Karty do wycięcia: papier 160–200 g albo wydruk na zwykłym i laminowanie",
                  "Materiały suchościeralne: laminowanie 100 mikronów i pisak do folii"])}</div>
    <div>${lista(["Wydruk A4 na A3 działa dla dzieci słabowidzących — układ się nie łamie",
                  "Piktogramy i etykiety najlepiej laminować od razu w komplecie",
                  "Pliki mają osadzone kroje i zdjęcia — otworzą się tak samo na każdym komputerze"])}</div>
  </div>

  <h2>Jak zamówić</h2>
  <div class="blok akcent">
    Prosimy o wiadomość na <strong>kontakt@eduplaner2026.pl</strong> albo telefon
    <strong>${TELEFON}</strong> z trzema informacjami: <strong>kody pomocy</strong> albo kod zestawu,
    <strong>rodzaj licencji</strong> oraz <strong>dane do faktury</strong>.
    Pliki wysyłamy po zaksięgowaniu wpłaty, zwykle tego samego dnia roboczego.
  </div>

  <div class="blok"><strong>Zamawiasz razem ze szkoleniem?</strong> Materiały objęte programem
    szkolenia są w jego cenie — nie trzeba ich kupować osobno. Przy zamówieniu prosimy podać
    kod szkolenia, a dobierzemy tylko to, czego szkolenie nie obejmuje.</div>

  <div class="stopka-dok" style="text-align:center;margin-top:40px">
    <strong>Mirosława Ewa Jurczyszyn</strong>, pedagog specjalny<br>
    Pomorskie Centrum Terapii Pedagogicznej, Koszalin<br>
    kontakt@eduplaner2026.pl · ${TELEFON} · www.eduplaner2026.pl<br>
    <span style="font-size:8.4px">Materiały edukacyjne i pomocnicze. Nie zastępują diagnozy
    ani terapii prowadzonej przez specjalistę.</span>
  </div>
</section>`;

const tresc = [tytulowa(), wstep(), zestawienie(),
  ...KATEGORIE.map(kartaKategorii), zestawy(), warunki()].join("\n");

zapisz({
  katalog: __dirname,
  plikBazowy: "Katalog-pomocy-dydaktycznych-PCTP",
  tytul: "Katalog pomocy dydaktycznych PCTP",
  opis: "Dwadzieścia dwie pomoce dydaktyczne w czterech kategoriach — emocje, komunikacja i AAC, organizacja przestrzeni, dokumentacja. PCTP Koszalin.",
  tresc,
});
console.log("Katalog pomocy · pozycji:", POMOCE.length, "· zestawów:", ZESTAWY.length);
