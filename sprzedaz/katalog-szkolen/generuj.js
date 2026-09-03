/* Katalog szkoleń — skład HTML z dane.js.  node generuj.js                  */
const path = require("path");
const { esc, lista, zapisz } = require("../wspolne/styl-katalogu.js");
const { TELEFON } = require("../wspolne/kontakt.js");
const { SCIEZKI, FORMY, SZKOLENIA, PAKIETY } = require("./dane.js");

const sciezka = (id) => SCIEZKI.find((s) => s.id === id);
const wgKodu = (kod) => SZKOLENIA.find((s) => s.kod === kod);

const tytulowa = () => `<section class="tytulowa">
  <div class="nad">Pomorskie Centrum Terapii Pedagogicznej · Koszalin</div>
  <h1>Katalog szkoleń</h1>
  <h1 style="font-size:28px;color:var(--pomarancz);margin-top:6px">Rok szkolny 2026/2027</h1>
  <div class="rule"></div>
  <p class="lead">Dwanaście szkoleń dla nauczycieli, specjalistów i dyrektorów przedszkoli, szkół
    i poradni. Cztery ścieżki tematyczne, trzy pakiety dla zespołów. Każde szkolenie kończy się
    materiałem, który zostaje w placówce i działa następnego dnia.</p>
  <div class="pasy">
    ${SCIEZKI.map((s) => `<div style="background:${s.hex};color:#fff;grid-column:span 1">Ścieżka ${s.id}</div>`).join("")}
    <div style="background:var(--brzoskwinia);color:var(--fiolet)">3 pakiety</div>
  </div>
  <div class="metryczka">
    <div><span class="etyk">W katalogu</span><b>12 szkoleń</b></div>
    <div><span class="etyk">Formy</span><b>4 · od rady po webinar</b></div>
    <div><span class="etyk">Czas</span><b>4–8 godzin</b></div>
    <div><span class="etyk">Materiały</span><b>w cenie szkolenia</b></div>
  </div>
  <div class="stopka-dok">
    <strong>Mirosława Ewa Jurczyszyn</strong>, pedagog specjalny · Pomorskie Centrum Terapii Pedagogicznej, Koszalin<br>
    kontakt@eduplaner2026.pl · ${TELEFON} · www.eduplaner2026.pl · EduPlaner 2026
  </div>
</section>`;

const wstep = () => `<section>
  <div class="nad">Jak z nami pracować</div>
  <h1>Cztery formy, jeden standard</h1><div class="rule"></div>
  <p class="lead">To samo szkolenie da się poprowadzić na cztery sposoby. Wybór formy zależy od tego,
    ile osób ma je przejść i czy potrzebna jest praca na dokumentacji konkretnych dzieci.</p>
  <table><thead><tr><th style="width:26%">Forma</th><th style="width:56%">Na czym polega</th>
    <th style="width:18%">Liczebność</th></tr></thead><tbody>
  ${FORMY.map((f) => `<tr><td><strong>${esc(f.nazwa)}</strong></td><td>${esc(f.opis)}</td><td>${esc(f.ile)}</td></tr>`).join("")}
  </tbody></table>

  <h2>Przebieg współpracy</h2>
  <table><thead><tr><th style="width:8%">Krok</th><th style="width:32%">Co się dzieje</th><th style="width:60%">Szczegóły</th></tr></thead><tbody>
    <tr><td style="color:var(--pomarancz);font-weight:700">1</td><td><strong>Rozmowa wstępna</strong></td><td>Bezpłatna, 20–30 minut. Ustalamy, czego zespół naprawdę potrzebuje — czasem to nie jest szkolenie, o które Państwo pytają.</td></tr>
    <tr><td style="color:var(--pomarancz);font-weight:700">2</td><td><strong>Dopasowanie programu</strong></td><td>Przykłady i materiały dobieramy do typu placówki i wieku dzieci. Program bazowy zostaje, zmieniają się przypadki.</td></tr>
    <tr><td style="color:var(--pomarancz);font-weight:700">3</td><td><strong>Szkolenie</strong></td><td>U Państwa albo online. Materiały dla każdego uczestnika, zaświadczenia po zakończeniu.</td></tr>
    <tr><td style="color:var(--pomarancz);font-weight:700">4</td><td><strong>Wsparcie po</strong></td><td>Trzydzieści dni na pytania mailowe. Konsultacja wdrożeniowa — opcjonalnie, na dokumentacji Państwa dzieci.</td></tr>
  </tbody></table>

  <h2>Cztery ścieżki tematyczne</h2>
  ${SCIEZKI.map((s) => `<div class="blok" style="border-left:4px solid ${s.hex}">
    <span class="etyk" style="color:${s.hex}">Ścieżka ${s.id}</span>
    <strong style="font-size:13px">${esc(s.nazwa)}</strong><br>${esc(s.opis)}</div>`).join("")}
</section>`;

const zestawienie = () => `<section class="czesc">
  <div class="nad">Wszystkie szkolenia</div>
  <h1>Zestawienie</h1><div class="rule"></div>
  <p class="lead">Dwanaście pozycji w czterech ścieżkach. Kod szkolenia podajemy przy zamówieniu.</p>
  <div class="blok akcent" style="margin-top:0"><strong>Ceny.</strong> Stawka zależy od formy
    (rada szkoleniowa rozliczana ryczałtem za grupę, warsztat otwarty i webinar — od uczestnika),
    liczby osób i dojazdu. Wycenę przygotowujemy po rozmowie wstępnej, zwykle w ciągu dwóch dni roboczych.</div>
  <table><thead><tr><th style="width:8%">Kod</th><th style="width:30%">Szkolenie</th>
    <th style="width:12%">Czas</th><th style="width:34%">Dla kogo przede wszystkim</th>
    <th style="width:16%">Cena</th></tr></thead><tbody>
  ${SCIEZKI.map((s) => {
    const wiersze = SZKOLENIA.filter((x) => x.sciezka === s.id).map((x) => `<tr>
      <td style="font-weight:700;color:${s.hex}">${x.kod}</td>
      <td><strong>${esc(x.tytul)}</strong>${x.polecane ? ' <span class="wstazka" style="margin:0">Polecane</span>' : ""}<br>
          <span style="font-size:8.6px;color:var(--szept)">${esc(x.podtytul)}</span></td>
      <td>${esc(x.czas.replace(" dydaktycznych", " dyd.").replace(" dydaktyczne", " dyd."))}</td>
      <td style="font-size:8.8px">${esc(x.dlaKogo.slice(0, 2).join(" · "))}</td>
      <td style="font-weight:700;color:var(--pomarancz)">[ cena ]</td></tr>`).join("");
    return `<tr><td colspan="5" style="background:${s.hex};color:#fff;font-family:var(--naglowek);
      font-weight:700;font-size:9px;letter-spacing:.14em;text-transform:uppercase">
      Ścieżka ${s.id} — ${esc(s.nazwa)}</td></tr>${wiersze}`;
  }).join("")}
  </tbody></table>
</section>`;

function karta(s) {
  const sc = sciezka(s.sciezka);
  const program = s.program.map((m) => `<tr>
    <td style="font-weight:700;color:var(--pomarancz);white-space:nowrap">${esc(m.czas)}</td>
    <td><strong>${esc(m.modul)}</strong></td>
    <td>${m.punkty.map((x) => `<div style="position:relative;padding-left:12px;margin-bottom:3px">
      <span style="position:absolute;left:0;top:5px;width:5px;height:5px;border-radius:2px;
      background:${sc.hex};display:block"></span>${esc(x)}</div>`).join("")}</td></tr>`).join("");

  return `<section class="czesc">
  <div class="nad" style="color:${sc.hex}">Ścieżka ${sc.id} · ${esc(sc.nazwa)} · kod ${s.kod}</div>
  ${s.polecane ? '<div class="wstazka">Najczęściej zamawiane</div>' : ""}
  <h1>${esc(s.tytul)}</h1>
  <p style="font-family:var(--naglowek);font-weight:600;font-size:15px;color:${sc.hex};margin:4px 0 0">${esc(s.podtytul)}</p>
  <div class="rule" style="background:${sc.hex}"></div>
  <p class="lead">${esc(s.opis)}</p>

  <div class="fakty">
    <div><span class="etyk">Czas</span><b>${esc(s.czas)}</b></div>
    <div><span class="etyk">Grupa</span><b>${esc(s.uczestnicy)}</b></div>
    <div><span class="etyk">Kod</span><b>${s.kod}</b></div>
    <div><span class="etyk">Cena</span><b style="color:var(--pomarancz)">[ cena ]</b></div>
  </div>

  <div class="dwie">
    <div><span class="etyk">Dla kogo</span>${lista(s.dlaKogo, sc.hex)}</div>
    <div><span class="etyk">Dostępne formy</span>${lista(s.formy, sc.hex)}</div>
  </div>

  <h2>Program</h2>
  <table><thead><tr><th style="width:12%">Czas</th><th style="width:30%">Moduł</th>
    <th style="width:58%">Zakres</th></tr></thead><tbody>${program}</tbody></table>

  <div class="dwie">
    <div><span class="etyk">Co uczestnik wynosi</span>${lista(s.efekty, "var(--zielony)")}</div>
    <div><span class="etyk">Materiały w cenie</span>${lista(s.materialy, sc.hex)}</div>
  </div>
</section>`;
}

const pakiety = () => `<section class="czesc">
  <div class="nad">Dla całego zespołu</div>
  <h1>Trzy pakiety</h1><div class="rule"></div>
  <p class="lead">Szkolenia zamawiane razem, realizowane w jednym roku szkolnym. Pakiet jest tańszy
    niż suma pojedynczych szkoleń i zawiera dodatkowe wsparcie po ostatnim spotkaniu.</p>
  ${PAKIETY.map((pk) => {
    const skl = pk.sklad.map(wgKodu);
    const godz = skl.reduce((a, x) => a + parseInt(x.czas, 10), 0);
    return `<div class="poz"><div class="pas" style="background:var(--pomarancz)"></div>
    <div class="srodek">
      <div class="kod">Kod ${pk.kod}</div>
      <h3>${esc(pk.nazwa)}</h3>
      <p class="opis">${esc(pk.opis)}</p>
      <div class="fakty">
        <div><span class="etyk">Szkoleń</span><b>${skl.length}</b></div>
        <div><span class="etyk">Łącznie</span><b>${godz} godzin</b></div>
        <div><span class="etyk">Realizacja</span><b>jeden rok szkolny</b></div>
        <div><span class="etyk">Cena pakietu</span><b style="color:var(--pomarancz)">[ cena ]</b></div>
      </div>
      <span class="etyk">W pakiecie</span>
      ${lista(skl.map((x) => `${x.kod} — ${x.tytul} (${x.czas})`), "var(--pomarancz)")}
      <div class="blok akcent" style="margin-bottom:0"><strong>Dodatkowo:</strong> ${esc(pk.bonus)}</div>
    </div></div>`;
  }).join("")}
</section>`;

const warunki = () => `<section class="czesc">
  <div class="nad">Sprawy organizacyjne</div>
  <h1>Warunki i zamówienie</h1><div class="rule"></div>
  <div class="dwie">
    <div>
      <h3>Co zapewnia PCTP</h3>
      ${lista(["Prowadzenie szkolenia i pełny scenariusz zajęć",
               "Materiały dla każdego uczestnika — w wersji papierowej lub PDF",
               "Zaświadczenia o ukończeniu szkolenia",
               "Trzydzieści dni wsparcia mailowego po szkoleniu",
               "Dopasowanie przykładów do typu placówki"])}
      <h3>Czego potrzebujemy od placówki</h3>
      ${lista(["Sala z rzutnikiem i możliwością pracy w małych grupach",
               "Lista uczestników do zaświadczeń — najpóźniej w dniu szkolenia",
               "Przy warsztacie na dokumentacji — anonimizowane przypadki przygotowane wcześniej"])}
    </div>
    <div>
      <h3>Terminy i rezygnacja</h3>
      ${lista(["Termin rezerwujemy po potwierdzeniu mailowym",
               "Zmiana terminu bez kosztów do 14 dni przed szkoleniem",
               "Rezygnacja później niż 7 dni przed — 50% wynagrodzenia"])}
      <h3>Rozliczenie</h3>
      ${lista(["Faktura na placówkę, płatność przelewem, 14 dni",
               "Rada szkoleniowa — ryczałt za grupę do 30 osób",
               "Warsztat otwarty i webinar — stawka od uczestnika",
               "Dojazd poza Koszalin — rozliczany oddzielnie"])}
    </div>
  </div>

  <h2>Jak zamówić</h2>
  <div class="blok akcent">
    Prosimy o wiadomość na <strong>kontakt@eduplaner2026.pl</strong> albo telefon
    <strong>${TELEFON}</strong> z trzema informacjami: <strong>kod szkolenia</strong>
    (albo temat, jeśli żaden kod nie pasuje), <strong>typ placówki i liczba uczestników</strong>
    oraz <strong>proponowany termin</strong>. Odpowiadamy z wyceną zwykle w ciągu dwóch dni roboczych.
  </div>

  <h2>Szkolenie spoza katalogu</h2>
  <p>Jeżeli żadna z dwunastu pozycji nie odpowiada na Państwa potrzebę, prosimy o kontakt mimo to.
    Część szkoleń w tym katalogu powstała z pytania placówki, na które nie było wtedy gotowej odpowiedzi.</p>

  <div class="stopka-dok" style="text-align:center;margin-top:40px">
    <strong>Mirosława Ewa Jurczyszyn</strong>, pedagog specjalny<br>
    Pomorskie Centrum Terapii Pedagogicznej, Koszalin<br>
    kontakt@eduplaner2026.pl · ${TELEFON} · www.eduplaner2026.pl
  </div>
</section>`;

const tresc = [tytulowa(), wstep(), zestawienie(),
  ...SZKOLENIA.map(karta), pakiety(), warunki()].join("\n");

zapisz({
  katalog: __dirname,
  plikBazowy: "Katalog-szkolen-PCTP",
  tytul: "Katalog szkoleń PCTP",
  opis: "Dwanaście szkoleń dla nauczycieli, specjalistów i dyrektorów przedszkoli, szkół i poradni. PCTP Koszalin, rok szkolny 2026/2027.",
  tresc,
});
console.log("Katalog szkoleń · pozycji:", SZKOLENIA.length, "· pakietów:", PAKIETY.length);
