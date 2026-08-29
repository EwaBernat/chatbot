/* Wersja do czytania i druku — z tego samego źródła co Word (dane.js).
   node generuj-html.js  →  Konspekty-...html  +  konspekty-artifact.html    */

const fs = require("fs");
const path = require("path");
const { BRAND, KOLORY_EMOCJI, POZIOMY, KONSPEKTY } = require("./dane.js");

const KROJE = fs.readFileSync(path.join(__dirname, "..", "broszura", "fonts.css"), "utf8");
const e = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const li = (xs, kolor) => xs.map((x) => `<li${kolor ? ` style="--pkt:${kolor}"` : ""}>${e(x)}</li>`).join("");

/* ── nagłówek dokumentu ───────────────────────────────────────────────── */
const STYL = `
<style>
${KROJE}
:root{
  --fiolet:#2D1B69; --fiolet-jasny:#4B3494; --pomarancz:#E8450A; --brzoskwinia:#F5B98E;
  --zielony:#0D7D5C; --bezowy:#C47A10; --papier:#FBF8F3; --atrament:#241C33;
  --szept:#6E6880; --kreska:#E3DDD2; --tlo-fiolet:#F4F2FA; --tlo-pomarancz:#FDF1EC;
  --naglowek:'Baloo 2','Trebuchet MS',system-ui,sans-serif;
  --tekst:'Atkinson Hyperlegible',Verdana,system-ui,sans-serif;
}
*{box-sizing:border-box}
body{margin:0;background:#EFEAE1;color:var(--atrament);font-family:var(--tekst);font-size:10.4px;line-height:1.55}
#dok{max-width:794px;margin:0 auto;background:var(--papier);padding:44px 58px 60px;
     box-shadow:0 18px 44px -12px rgba(36,28,51,.3)}
h1,h2,h3,h4{font-family:var(--naglowek);margin:0;line-height:1.1;font-weight:700;color:var(--fiolet)}
h1{font-size:34px;letter-spacing:-.015em}
h2{font-size:21px;margin-top:24px}
h3{font-size:15px;margin-top:16px}
p{margin:0 0 9px}
strong{color:var(--fiolet)}
.nad{font-family:var(--naglowek);font-weight:700;font-size:9.4px;letter-spacing:.26em;
     text-transform:uppercase;color:var(--pomarancz);margin-bottom:8px}
.lead{font-size:12.6px;line-height:1.55;color:#453D5A;margin:10px 0 16px}
.rule{height:4px;width:52px;border-radius:2px;background:var(--pomarancz);margin:12px 0 18px}
ul{list-style:none;margin:0 0 10px;padding:0}
li{position:relative;padding-left:15px;margin-bottom:4px;line-height:1.5}
li::before{content:"";position:absolute;left:0;top:6px;width:6px;height:6px;border-radius:2px;
           background:var(--pkt,var(--pomarancz))}
table{width:100%;border-collapse:collapse;font-size:9.4px;margin:10px 0 14px}
th{background:var(--fiolet);color:#fff;font-family:var(--naglowek);font-weight:700;font-size:8.4px;
   letter-spacing:.14em;text-transform:uppercase;text-align:left;padding:7px 9px}
td{padding:8px 9px;border-bottom:1px solid var(--kreska);vertical-align:top;color:#4A4358}
tr:nth-child(even) td{background:var(--tlo-fiolet)}
.etyk{font-family:var(--naglowek);font-weight:700;font-size:8px;letter-spacing:.16em;
      text-transform:uppercase;color:var(--szept);display:block;margin-bottom:4px}
.blok{background:var(--tlo-fiolet);border-radius:8px;padding:13px 15px;margin:12px 0}
.blok.akcent{background:var(--tlo-pomarancz);border-left:4px solid var(--pomarancz)}
.podstawa{font-size:8.8px;color:var(--bezowy);letter-spacing:.02em}
.kryt{color:var(--zielony);font-size:8.8px}
.metryczka{display:grid;grid-template-columns:repeat(4,1fr);gap:2px;margin:12px 0 4px}
.metryczka div{background:var(--tlo-fiolet);padding:9px 11px}
.metryczka b{display:block;font-family:var(--naglowek);font-size:12px;color:var(--fiolet);margin-top:2px}
.poz{display:inline-block;font-family:var(--naglowek);font-weight:800;font-size:15px;
     color:var(--pomarancz);background:var(--tlo-pomarancz);border-radius:5px;padding:2px 9px}
.pasy{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin:18px 0}
.pas{border-radius:4px;padding:9px 6px;text-align:center;font-family:var(--naglowek);
     font-weight:700;font-size:12px}
.tytulowa{padding:60px 0 30px}
.tytulowa h1{font-size:52px}
.stopka-dok{margin-top:26px;padding-top:12px;border-top:1.5px solid var(--kreska);
            font-size:9px;color:var(--szept)}
.konspekt{break-before:page;page-break-before:always}
.czesc{break-before:page;page-break-before:always}
.tytulowa{break-after:page;page-break-after:always}
h2,h3,tr{break-inside:avoid;page-break-inside:avoid}
.blok{break-inside:avoid}
@media print{
  @page{size:A4;margin:16mm 15mm 14mm}
  body{background:#fff;font-size:9.6px}
  #dok{max-width:none;padding:0;box-shadow:none;background:#fff}
  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
</style>`;

/* ── składanie ────────────────────────────────────────────────────────── */
const kolorHex = (k) => KOLORY_EMOCJI[k].hex;

function tytulowa() {
  const pasy = [["Radość", "F2B21A", "#8A6203"], ["Smutek", "2E6FB7", "#fff"],
                ["Złość", "D33B2C", "#fff"], ["Wstyd", "E0619B", "#fff"], ["Strach", "6E7681", "#fff"]]
    .map(([n, tlo, kol]) => `<div class="pas" style="background:#${tlo};color:${kol}">${n}</div>`).join("");
  return `<section class="tytulowa">
  <div class="nad">Świat Kolorów · przedszkole · część 1</div>
  <h1>Kolorowy Świat Emocji</h1>
  <h1 style="font-size:30px;color:var(--pomarancz);margin-top:6px">Konspekty zajęć dla dzieci 3–4 lata</h1>
  <div class="rule"></div>
  <p class="lead">Siedem konspektów zajęć rozwijających kompetencje emocjonalne i społeczne,
    z kompletem 21 celów SMART przypisanych do trzech poziomów wsparcia — gotowych do przeniesienia do IPET-u.</p>
  <div class="pasy">${pasy}</div>
  <div class="metryczka">
    <div><span class="etyk">W dokumencie</span><b>7 konspektów · 21 celów</b></div>
    <div><span class="etyk">Grupa wiekowa</span><b>3–4 lata</b></div>
    <div><span class="etyk">Czas zajęć</span><b>20 min (nr 7 — 25)</b></div>
    <div><span class="etyk">Cykl</span><b>12 tygodni</b></div>
  </div>
  <div class="stopka-dok">
    <strong>Mirosława Ewa Jurczyszyn</strong>, pedagog specjalny · Pomorskie Centrum Terapii Pedagogicznej, Koszalin<br>
    kontakt@eduplaner2026.pl · [usunięto] · www.eduplaner2026.pl · EduPlaner 2026
  </div>
</section>`;
}

function jakKorzystac() {
  const zasady = [
    ["Dwadzieścia minut, nie więcej", "Trzylatek utrzymuje uwagę w zorganizowanej aktywności około 15–20 minut. Konspekty są napisane na ten czas i nie warto ich wydłużać — lepiej powtórzyć zajęcia w kolejnym tygodniu."],
    ["Jeden kolor na tydzień", "Cały cykl to 12 tygodni: tydzień wprowadzający, po dwa tygodnie na każdy kolor i tydzień podsumowujący. Emocja potrzebuje powtórzeń, nie tempa."],
    ["Ta sama kolejność za każdym razem", "Każdy konspekt ma pięć etapów w stałym porządku: rytuał powitania, wprowadzenie, część główna, ruch, domknięcie. Przewidywalność jest tu narzędziem terapeutycznym."],
    ["Miś Kolorek zamiast Rajmunda", "W wersji dla nastolatka bohaterem jest siedemnastoletni Rajmund. Dla trzylatka jego rolę przejmuje Miś Kolorek, który zmienia chustkę razem z emocją."],
    ["Kolor jest odpowiedzią", "Podanie karty w kolorze jest pełnoprawną odpowiedzią. Dziecko, które jeszcze nie mówi albo nie chce mówić, uczestniczy w zajęciach tak samo jak pozostałe."],
    ["Nie ma dobrych i złych odpowiedzi", "Nie poprawiamy nazwy emocji, nie porównujemy dzieci, nie wymagamy dokończenia zadania. Zasada „pas” obowiązuje na każdych zajęciach."],
  ];
  const plan = [
    ["1", "Konspekt 1 — Pięć kolorów", "wszystkie pięć", "wspólny kod grupy"],
    ["2–3", "Konspekt 2 — Żółty dzień", "żółty · radość", "rozpoznawanie radości"],
    ["4–5", "Konspekt 3 — Niebieski Miś", "niebieski · smutek", "proszenie o wsparcie"],
    ["6–7", "Konspekt 4 — Czerwony Miś", "czerwony · złość", "sygnał STOP i oddech"],
    ["8–9", "Konspekt 5 — Różowy Miś", "różowy · wstyd", "bezpieczeństwo po pomyłce"],
    ["10–11", "Konspekt 6 — Szary Miś", "szary · strach", "plan obrazkowy"],
    ["12", "Konspekt 7 — Paleta i gra", "wszystkie pięć", "ewaluacja celów SMART"],
  ];
  return `<section class="czesc" style="break-before:auto;page-break-before:auto">
  <div class="nad">Część I</div><h1>Jak korzystać z konspektów</h1><div class="rule"></div>
  <p class="lead">Sześć zasad, na których stoi cały cykl. Każdy konspekt jest napisany tak, żeby dało się go
    poprowadzić bez wcześniejszego przygotowania — wystarczy przeczytać przebieg zajęć i przygotować środki dydaktyczne.</p>
  ${zasady.map(([tyt, op]) => `<p><strong>${e(tyt)} — </strong>${e(op)}</p>`).join("")}
  <h2>Ramowy plan cyklu</h2>
  <table><thead><tr><th>Tydzień</th><th>Konspekt</th><th>Kolor i emocja</th><th>Co domykamy</th></tr></thead>
  <tbody>${plan.map(([a, b, c, d]) =>
    `<tr><td style="color:var(--pomarancz);font-weight:700">${e(a)}</td><td>${e(b)}</td><td>${e(c)}</td><td>${e(d)}</td></tr>`).join("")}
  </tbody></table></section>`;
}

function poziomy() {
  return `<section class="czesc">
  <div class="nad">Część II</div><h1>Trzy poziomy wsparcia</h1><div class="rule"></div>
  <p class="lead">Ten sam konspekt realizuje troje dzieci o różnych potrzebach — i każde z nich ma inny cel.
    Poziom wsparcia nie zmienia tematu zajęć; zmienia kryterium osiągnięcia i ilość podpowiedzi wpisaną w cel.</p>
  <div class="blok akcent"><strong>Zasada zapisu:</strong> im wyższy poziom wsparcia, tym więcej podpowiedzi
    w treści celu i niższe kryterium samodzielności. Cel na poziomie III nie jest „gorszy” — jest realny
    dla dziecka, które potrzebuje dorosłego obok.</div>
  ${POZIOMY.map((poz) => `
    <h2>${e(poz.nazwa)}</h2>
    <p>${e(poz.kto)}</p>
    <span class="etyk">Formy realizacji</span><ul>${li(poz.formy)}</ul>
    <div class="blok"><span class="podstawa"><strong style="color:var(--bezowy)">PODSTAWA PRAWNA:</strong> ${e(poz.podstawa)}</span></div>`).join("")}
  </section>`;
}

function zbiorcza() {
  const wiersze = KONSPEKTY.flatMap((k) => k.smart.map((s, i) => `<tr>
    <td style="font-weight:700;color:var(--pomarancz)">${i === 0 ? k.nr : ""}</td>
    <td style="font-weight:700;color:var(--fiolet)">${s.poziom}</td>
    <td>KSzOF ${s.kszof}<br><span class="podstawa">ICF ${e(s.icf)}</span></td>
    <td>${e(s.cel)}</td>
    <td class="kryt">${e(s.kryterium)}</td></tr>`)).join("");
  return `<section class="czesc">
  <div class="nad">Część III</div><h1>Wszystkie 21 celów SMART</h1><div class="rule"></div>
  <p class="lead">Komplet celów z siedmiu konspektów, w układzie do przeniesienia wprost do sekcji III IPET-u
    (cele edukacyjno-terapeutyczne KSzOF + ICF). Pełne brzmienie każdego celu wraz z formą realizacji
    i podstawą prawną znajduje się przy odpowiednim konspekcie.</p>
  <table><thead><tr><th style="width:5%">Nr</th><th style="width:6%">Poz.</th><th style="width:16%">KSzOF · ICF</th>
    <th style="width:50%">Cel SMART</th><th style="width:23%">Kryterium</th></tr></thead><tbody>${wiersze}</tbody></table>
  <div class="blok akcent"><strong>Jak to przenieść do IPET-u:</strong> wybierz cele z poziomu, na który dziecko
    zostało zakwalifikowane w sekcji II. Kolumna „KSzOF · ICF” odpowiada polom obszaru i kodu w tabeli celów.
    Kryterium wpisz do kolumny ewaluacji.</div></section>`;
}

function konspekt(k) {
  const hex = "#" + kolorHex(k.kolor);
  const pkt = k.kolor === "paleta" ? "var(--pomarancz)" : hex;
  const smart = k.smart.map((s) => `<tr>
    <td style="text-align:center"><span class="poz">${s.poziom}</span></td>
    <td><strong>${e(s.obszar)}</strong><br><span class="podstawa" style="color:var(--szept)">KSzOF ${s.kszof}</span><br><span class="podstawa">ICF ${e(s.icf)}</span></td>
    <td>${e(s.cel)}</td>
    <td>${e(s.forma)}<br><span class="kryt"><strong style="color:var(--zielony)">Kryterium:</strong> ${e(s.kryterium)}</span><br><span class="podstawa">${e(s.podstawa)}</span></td></tr>`).join("");
  const przebieg = k.przebieg.map((x) => `<tr>
    <td style="font-weight:700;color:var(--pomarancz)">${e(x.czas)}</td>
    <td><strong>${e(x.etap)}</strong></td><td>${e(x.n)}</td><td>${e(x.d)}</td></tr>`).join("");
  const dost = k.dostosowania.map((d) => {
    const [g, ...r] = d.split(" — ");
    return `<li style="--pkt:${pkt}"><strong>${e(g)} — </strong>${e(r.join(" — "))}</li>`;
  }).join("");

  return `<section class="konspekt">
  <div class="nad" style="color:${pkt}">Konspekt ${k.nr} · ${e(k.podtytul)}</div>
  <h1>${e(k.temat)}</h1>
  <div class="rule" style="background:${pkt}"></div>
  <div class="metryczka">
    <div><span class="etyk">Grupa wiekowa</span><b>3–4 lata</b></div>
    <div><span class="etyk">Czas</span><b>${e(k.czas)}</b></div>
    <div><span class="etyk">Kolor przewodni</span><b style="color:${hex}">${e(KOLORY_EMOCJI[k.kolor].nazwa)}</b></div>
    <div><span class="etyk">Data / grupa</span><b style="color:var(--szept)">.....................</b></div>
  </div>

  <h2>Cel ogólny</h2><p>${e(k.celOgolny)}</p>
  <h2>Cele operacyjne</h2><span class="etyk">Dziecko:</span><ul>${li(k.celeOperacyjne, pkt)}</ul>

  <h2>Cele SMART według poziomu wsparcia</h2>
  <table><thead><tr><th style="width:8%">Poziom</th><th style="width:20%">Obszar KSzOF · ICF</th>
    <th style="width:41%">Cel SMART</th><th style="width:31%">Forma realizacji i kryterium</th></tr></thead>
    <tbody>${smart}</tbody></table>

  <h2>Metody, formy i środki</h2>
  <h3>Metody pracy</h3><ul>${li(k.metody, pkt)}</ul>
  <h3>Formy pracy</h3><ul>${li(k.formy, pkt)}</ul>
  <h3>Środki dydaktyczne</h3><ul>${li(k.srodki, pkt)}</ul>

  <h2>Przebieg zajęć</h2>
  <table><thead><tr><th style="width:9%">Czas</th><th style="width:21%">Etap</th>
    <th style="width:36%">Czynności nauczyciela</th><th style="width:34%">Czynności dziecka</th></tr></thead>
    <tbody>${przebieg}</tbody></table>

  <h2>Dostosowania dla dzieci z różnymi potrzebami</h2><ul>${dost}</ul>
  <h2>Ewaluacja zajęć — pytania dla prowadzącego</h2><ul>${li(k.ewaluacja, "var(--zielony)")}</ul>
  <h2>Podstawa programowa wychowania przedszkolnego</h2><ul>${li(k.podstawaProgramowa, "var(--bezowy)")}</ul>
  <div class="blok akcent"><span class="etyk" style="color:var(--pomarancz)">Notatka dla prowadzącego</span>${e(k.notatka)}</div>
</section>`;
}

function karta() {
  const wiersze = KONSPEKTY.flatMap((k) => k.smart.map((s, i) => `<tr>
    <td>${i === 0 ? `<strong>${k.nr}. ${e(k.podtytul.split(" · ")[0])}</strong>` : ""}</td>
    <td style="text-align:center;font-weight:700;color:var(--pomarancz)">${s.poziom}</td>
    <td style="font-size:8.6px">${e(s.cel.split(" ").slice(0, 14).join(" "))}…</td>
    <td></td><td></td><td></td></tr>`)).join("");
  return `<section class="czesc">
  <div class="nad">Część V</div><h1>Karta obserwacji i ewaluacji celów</h1><div class="rule"></div>
  <p class="lead">Do wydruku dla każdego dziecka objętego IPET-em. Wypełnia się na bieżąco, po zajęciach.
    Wypełniona karta jest gotowym załącznikiem do oceny efektywności programu (sekcja VIII IPET-u).</p>
  <p><strong>Imię i nazwisko dziecka:</strong> ...................................................................</p>
  <p><strong>Grupa:</strong> ..............................  <strong>Poziom wsparcia wg IPET:</strong>
     <span style="color:var(--pomarancz);font-weight:700">I &nbsp;/&nbsp; II &nbsp;/&nbsp; III</span></p>
  <p><strong>Okres obserwacji:</strong> ..............................................</p>
  <table><thead><tr><th style="width:17%">Konspekt</th><th style="width:8%">Poziom</th>
    <th style="width:39%">Cel SMART — skrót</th><th style="width:12%">Data</th>
    <th style="width:12%">Wynik</th><th style="width:12%">Uwagi</th></tr></thead><tbody>${wiersze}</tbody></table>
  <p style="margin-top:14px"><strong>Wniosek do ewaluacji IPET:</strong></p>
  <p style="color:var(--kreska)">${".".repeat(110)}</p>
  <p style="color:var(--kreska)">${".".repeat(110)}</p>
  <p style="color:var(--kreska)">${".".repeat(110)}</p>
  <p style="margin-top:18px">Podpis prowadzącego: ..............................................
     &nbsp;&nbsp; Data: ..............................</p></section>`;
}

function prawo() {
  const akty = [
    ["Podstawa programowa wychowania przedszkolnego", "Rozporządzenie Ministra Edukacji Narodowej z dnia 14 lutego 2017 r. w sprawie podstawy programowej wychowania przedszkolnego oraz kształcenia ogólnego — załącznik nr 1. Numeracja obszarów i punktów przywoływana w konspektach pochodzi z tego załącznika."],
    ["Kształcenie specjalne i poziomy wsparcia", "Rozporządzenie Ministra Edukacji Narodowej w sprawie warunków organizowania kształcenia, wychowania i opieki dla dzieci i młodzieży niepełnosprawnych, niedostosowanych społecznie i zagrożonych niedostosowaniem społecznym — § 6 i § 7 (formy wsparcia, IPET, zajęcia rewalidacyjne)."],
    ["Pomoc psychologiczno-pedagogiczna", "Rozporządzenie Ministra Edukacji Narodowej z dnia 9 sierpnia 2017 r. w sprawie zasad organizacji i udzielania pomocy psychologiczno-pedagogicznej w publicznych przedszkolach, szkołach i placówkach — § 6 (formy pomocy, zajęcia specjalistyczne)."],
    ["Klasyfikacja funkcjonowania", "Międzynarodowa Klasyfikacja Funkcjonowania, Niepełnosprawności i Zdrowia (ICF, WHO) — kody d i b przywoływane przy celach. Obszary KSzOF 1–9 zgodnie ze standardem oceny funkcjonalnej stosowanym w ekosystemie EduPlaner 2026."],
  ];
  return `<section class="czesc">
  <div class="nad">Część VI</div><h1>Podstawa prawna i źródła</h1><div class="rule"></div>
  ${akty.map(([t, o]) => `<h3>${e(t)}</h3><p>${e(o)}</p>`).join("")}
  <div class="blok akcent"><span class="etyk" style="color:#B8350D">Zastrzeżenie</span>
    Konspekty są materiałem edukacyjnym i metodycznym. Cele SMART wymagają dostosowania do konkretnego dziecka
    na podstawie wielospecjalistycznej oceny poziomu funkcjonowania (WOPF). Materiał nie zastępuje diagnozy
    ani terapii prowadzonej przez specjalistę.</div>
  <div class="stopka-dok" style="text-align:center">
    Mirosława Ewa Jurczyszyn · Pomorskie Centrum Terapii Pedagogicznej, Koszalin · EduPlaner 2026</div></section>`;
}

/* ── zapis ────────────────────────────────────────────────────────────── */
const tresc = `<title>Konspekty 3–4 lata</title>
${STYL}
<div id="dok">
${tytulowa()}
${jakKorzystac()}
${poziomy()}
${zbiorcza()}
${KONSPEKTY.map(konspekt).join("\n")}
${karta()}
${prawo()}
</div>`;

fs.writeFileSync(path.join(__dirname, "konspekty-artifact.html"), tresc);
fs.writeFileSync(path.join(__dirname, "Konspekty-Kolorowy-Swiat-Emocji-3-4-lata.html"),
`<!doctype html>
<html lang="pl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Siedem konspektów zajęć dla dzieci 3–4 lata z 21 celami SMART dla trzech poziomów wsparcia. PCTP Koszalin.">
<meta name="author" content="Mirosława Ewa Jurczyszyn">
</head><body>
${tresc}
</body></html>`);
console.log("Zapisano HTML · konspektów:", KONSPEKTY.length, "· celów SMART:",
  KONSPEKTY.reduce((a, k) => a + k.smart.length, 0));
