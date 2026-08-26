# -*- coding: utf-8 -*-
CSS = r'''
:root{
  --z900:#06281E; --z800:#0B3D2E; --z700:#14664A; --z600:#1F8A63; --z500:#3FA87C;
  --z400:#6FC5A0; --z300:#A7DCC4; --z200:#CFEBDD; --z100:#E8F5EF; --z050:#F4FBF7;
  --gold:#E3B23C; --gold2:#F4D06F; --roza:#D96D8B; --roza2:#F0A9BE;
  --czerw:#B23A48; --zolt:#D9902F; --ziel:#2E9E5B;
  --ink:#08251C; --tekst:#173B30; --szary:#5C7A6E;
  --pg:#fff; --cien:0 2px 10px rgba(6,40,30,.07);
  --font-h:'Poppins','Trebuchet MS',sans-serif;
  --font-t:'Lato','Segoe UI',system-ui,sans-serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--z100);color:var(--tekst);
  font-family:var(--font-t);font-size:11.4pt;line-height:1.55;
  -webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:var(--font-h);color:var(--z800);margin:0 0 .5em;line-height:1.18;font-weight:700}
p{margin:0 0 .7em}
ul,ol{margin:0 0 .7em;padding-left:1.25em}
li{margin-bottom:.28em}
b,strong{color:var(--z800);font-weight:700}
small{font-weight:400;font-size:.82em;color:var(--szary)}

/* ---------- STRONA A4 ---------- */
.page{width:210mm;min-height:297mm;margin:0 auto 9mm;
  padding:12mm 12mm 9mm;position:relative;box-shadow:0 6px 26px rgba(6,40,30,.13);
  border-radius:3px;display:flex;flex-direction:column;
  background:linear-gradient(180deg,var(--z600),var(--z400) 45%,var(--gold)) left top/6mm 100% no-repeat,
             var(--pg)}

/* ---------- OKŁADKA ---------- */
.okladka{padding:0;background:var(--z900);color:#fff;display:flex;flex-direction:column;
  height:297mm;overflow:hidden}
.ok-tlo{position:relative;overflow:hidden}
.ok-box{position:relative;width:100%;height:0;padding-bottom:40%}
.ok-box-foto{position:relative;width:100%;height:0;overflow:hidden}
.ok-box-foto img{position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover;display:block}
.ok-box svg{position:absolute;left:0;top:0;width:100%;height:100%;display:block}
.ok-tlo::after{content:"";position:absolute;inset:auto 0 0 0;height:30mm;z-index:2;
  background:linear-gradient(180deg,rgba(6,40,30,0),var(--z900))}
.ok-tresc{flex:1;padding:5mm 18mm 0;text-align:center;position:relative;z-index:2}
.ok-logo{width:21mm;margin:0 auto 2.5mm}
.ok-logo svg{width:100%;height:auto;display:block;
  filter:drop-shadow(0 3px 10px rgba(0,0,0,.35))}
.ok-org{font-family:var(--font-h);font-size:10.4pt;font-weight:600;color:#fff;
  letter-spacing:.04em;margin-bottom:3.5mm}
.ok-nad{font-family:var(--font-h);text-transform:uppercase;letter-spacing:.22em;
  font-size:8.6pt;color:var(--z300);margin-bottom:6mm}
.okladka h1{font-size:36pt;color:#fff;letter-spacing:-.5px;margin-bottom:2mm;line-height:1.05}
.okladka h1 span{color:var(--gold2);font-weight:600}
.ok-pod{font-family:var(--font-h);font-size:16pt;color:var(--z300);
  letter-spacing:.16em;text-transform:lowercase;margin-bottom:6mm}
.ok-linia{width:44mm;height:3px;margin:0 auto 7mm;border-radius:2px;
  background:linear-gradient(90deg,var(--z500),var(--gold))}
.ok-lista{list-style:none;padding:0;max-width:132mm;margin:0 auto;text-align:left;
  display:grid;gap:2.4mm}
.ok-lista li{color:var(--z200);font-size:11pt;padding-left:8mm;position:relative}
.ok-lista li::before{content:"✦";position:absolute;left:0;color:var(--gold);font-size:11pt}
.ok-stopka{text-align:center;padding:0 0 9mm;margin:7mm 0 0}
.ok-autor{color:var(--z200);font-size:10.4pt;margin:0 0 1mm}
.ok-autor b{color:var(--gold2);font-family:var(--font-h)}
.ok-mail{color:var(--gold2);font-size:10pt;font-family:var(--font-h);letter-spacing:.03em;margin:0 0 4mm}
.ok-zrodlo{color:var(--z400);font-size:8.6pt;margin:0}

/* ---------- NAGŁÓWKI DZIAŁÓW ---------- */
.dzial-h{font-size:23pt;color:var(--z800);display:flex;align-items:center;gap:5mm;
  padding-bottom:3mm;margin-bottom:5mm;border-bottom:3px solid var(--z200)}
.dzial-litera{display:inline-flex;align-items:center;justify-content:center;
  width:13mm;height:13mm;border-radius:50%;background:var(--z600);color:#fff;
  font-size:15pt;flex:none;box-shadow:0 3px 0 var(--z700)}
.pod-h{font-size:14pt;color:var(--z700);margin:7mm 0 3mm;padding-left:4mm;
  border-left:4px solid var(--gold)}
.lead{font-size:11.8pt;color:var(--z700);background:var(--z050);
  border-left:4px solid var(--z400);padding:3.5mm 5mm;border-radius:0 6px 6px 0;margin-bottom:5mm}

/* ---------- SPIS TREŚCI ---------- */
.spis-grid{display:grid;grid-template-columns:1fr 1.15fr;gap:8mm}
.spis-jedna{max-width:150mm;margin:0 auto}
.dwie-kolumny{column-count:2;column-gap:8mm}
.dwie-kolumny li{break-inside:avoid}
.uwaga.jasna{background:var(--z050);color:var(--z800);border:1px solid var(--z300);border-left:5px solid var(--gold)}
.uwaga.jasna b{color:var(--z700)}
.spis-h{font-size:12pt;color:var(--z600);text-transform:uppercase;letter-spacing:.08em;
  border-bottom:2px solid var(--z200);padding-bottom:1.5mm;margin-bottom:3mm}
.spis-lista{list-style:none;padding:0;margin:0}
.spis-lista li{margin:0}
.spis-lista a{display:flex;align-items:center;gap:3mm;text-decoration:none;color:var(--tekst);
  padding:1.5mm 2mm;border-radius:4px;font-size:10.2pt;border-bottom:1px dotted var(--z200)}
.spis-lista a:hover{background:var(--z050)}
.s-nr{flex:none;width:7mm;height:7mm;border-radius:4px;background:var(--z200);color:var(--z800);
  font-family:var(--font-h);font-weight:700;font-size:8.5pt;display:inline-flex;
  align-items:center;justify-content:center}
.spis-czesci .s-nr{background:var(--z600);color:#fff}
.s-tyt{flex:1}
.s-etap{flex:none;font-family:var(--font-h);font-size:8pt;font-weight:700;color:var(--z600);
  background:var(--z100);border-radius:20px;padding:.6mm 2.2mm}
.s-str{flex:none;min-width:7mm;text-align:right;font-family:var(--font-h);font-weight:700;
  font-size:9.6pt;color:var(--z700);font-variant-numeric:tabular-nums}
.spis-str-h{float:right;font-size:8.4pt;color:var(--z600);letter-spacing:.06em}
.spis-legenda{font-size:8.8pt;color:var(--szary);margin:-1mm 0 2.5mm}
.spis-legenda span{font-family:var(--font-h);font-weight:700;color:var(--z600)}
.spis-info{margin-top:6mm;background:var(--z050);border:1px solid var(--z200);
  border-radius:8px;padding:4mm}
.rytm{padding-left:5mm;margin:2mm 0}
.rytm li{font-size:9.7pt;margin-bottom:1.4mm}
.rytm li::marker{color:var(--z500);font-weight:700}
.siedem{counter-reset:s;list-style:none;padding:0;margin:2mm 0 0;
  display:grid;grid-template-columns:1fr 1fr;gap:1.2mm 3mm}
.siedem li{counter-increment:s;font-size:9.6pt;padding-left:6mm;position:relative;color:var(--z700)}
.siedem li::before{content:counter(s);position:absolute;left:0;width:4.4mm;height:4.4mm;
  background:var(--z400);color:#fff;border-radius:50%;font-size:7pt;font-weight:700;
  display:flex;align-items:center;justify-content:center;font-family:var(--font-h);top:.4mm}

/* ---------- KARTY / SIATKI ---------- */
.karty3{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm;margin-bottom:5mm}
.karta{background:var(--z050);border:1px solid var(--z200);border-radius:10px;padding:4mm;
  border-top:4px solid var(--z500)}
.karta h3{font-size:12pt;color:var(--z700);margin-bottom:2mm}
.karta ul{padding-left:4.5mm;margin:0}
.karta li{font-size:9.9pt;margin-bottom:1.4mm}
.karta li::marker{color:var(--z400)}

.zalozenia{display:grid;grid-template-columns:1fr 1fr;gap:2.5mm;margin-bottom:5mm}
.zalozenia div{background:#fff;border:1px solid var(--z200);border-left:4px solid var(--gold);
  border-radius:0 7px 7px 0;padding:2.8mm 3.5mm;font-size:9.9pt}
.uwaga{background:linear-gradient(135deg,var(--z700),var(--z600));color:#fff;
  border-radius:10px;padding:4.5mm 5mm;font-size:10.2pt;margin-top:4mm}
.uwaga b{color:var(--gold2)}

/* ---------- NARZĘDZIA ---------- */
.kiedy{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.kiedy div{display:block;background:var(--z050);
  border:1px solid var(--z200);border-left:4px solid var(--gold);border-radius:0 7px 7px 0;padding:2.2mm 3.4mm}
.kiedy b{display:block;margin-bottom:1mm;color:var(--z700);font-family:var(--font-h);font-size:10pt}
.kiedy span{font-size:9.7pt}
.narz{display:grid;grid-template-columns:1fr 1fr;gap:5mm;margin-bottom:5mm}
.narz-box{background:var(--z050);border:1px solid var(--z200);border-radius:10px;padding:4mm}
.narz-box .ilu{max-width:62mm;margin-left:auto;margin-right:auto}
.narz-box.szeroki{margin-top:0}
.narz-box h3{font-size:13pt;color:var(--z700)}
.narz-box p{font-size:10.2pt}
.sygn-lista{display:grid;gap:2.5mm;margin:3mm 0}
.sy{display:flex;gap:3mm;align-items:flex-start;background:#fff;border-radius:8px;
  padding:2.8mm 3.5mm;border:1px solid var(--z200)}
.sy .znak{flex:none;width:8mm;height:8mm;border-radius:50%;color:#fff;font-weight:700;
  display:flex;align-items:center;justify-content:center;font-size:11pt}
.sy p{margin:.3mm 0 0;font-size:9.6pt;color:var(--szary)}
.sy b{font-size:10pt}
.sy.zielone .znak{background:var(--ziel)} .sy.zolte .znak{background:var(--zolt)}
.sy.czerwone .znak{background:var(--czerw)}
.mini{font-size:9.2pt;color:var(--szary);font-style:italic}
.drabina{display:grid;grid-template-columns:.85fr 1.15fr;gap:5mm;align-items:start;margin:3mm 0}
.etapy{list-style:none;padding:0;counter-reset:e;margin:0}
.etapy li{background:#fff;border:1px solid var(--z200);border-radius:8px;padding:2.6mm 3.2mm;
  margin-bottom:2mm;font-size:9.8pt;border-left:4px solid var(--z500)}
.etapy li:nth-child(2){border-left-color:var(--z400)}
.etapy li:nth-child(3){border-left-color:var(--z500)}
.etapy li:nth-child(4){border-left-color:var(--z600)}
.etapy li:nth-child(5){border-left-color:var(--z700)}
.etapy span{display:block;font-size:8.6pt;color:var(--szary);margin-top:.8mm}

/* ---------- ILUSTRACJE ---------- */
.ilu.maly{max-width:96mm;margin:0 auto 4mm}
.ilu.mini{max-width:58mm;margin:0 auto 3mm}
.kol-b .ilu{max-width:54mm;margin:0 auto 3mm}
.dzial-h .cd{font-size:.5em;color:var(--z400);font-weight:400}
.ilu{width:100%;flex:none;margin:0 0 3.5mm;padding:0;border-radius:10px;overflow:hidden;background:var(--z100)}
.ilu-box{position:relative;width:100%;height:0;overflow:hidden}
.ilu-box > svg,.ilu-box > img{position:absolute;left:0;top:0;width:100%;height:100%;display:block}
.ilu-box > img{object-fit:cover}
.ilu-foto{background:var(--z200)}
figcaption{font-size:9pt;color:var(--szary);padding:2mm 3mm;background:var(--z050);text-align:center}

/* ---------- POSTACIE ---------- */
.postacie{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.postac{display:flex;gap:3.5mm;background:var(--z050);border:1px solid var(--z200);
  border-radius:10px;padding:4mm;border-top:4px solid var(--z500)}
.p-ico{flex:none}
.p-ico svg{display:block;border-radius:50%}
.p-tresc h3{font-size:12.5pt;margin-bottom:.8mm}
.p-kim{font-style:italic;color:var(--z600);font-size:9.8pt;margin-bottom:1.5mm}
.p-tresc p{font-size:9.7pt;margin-bottom:1.2mm}

/* ---------- ROZDZIAŁ ---------- */
.rozdzial{}
.r-head.mini{padding-bottom:2.4mm;margin-bottom:3mm;border-bottom-width:2px}
.r-head.mini .r-nr{width:14mm;padding:1.2mm 0}
.r-head.mini .r-nr b{font-size:15pt}
.r-head.mini .r-tyt h2{font-size:15pt}
.notatki{margin-top:4mm}
.notatki h3{font-size:9.4pt;color:var(--z600);text-transform:uppercase;letter-spacing:.05em;margin-bottom:2.5mm}
.linie{display:grid;gap:7mm}
.linie i{display:block;height:0;border-bottom:1.4px dotted var(--z300)}
.r-head{display:flex;align-items:center;gap:4mm;padding-bottom:3mm;margin-bottom:3.5mm;
  border-bottom:3px solid var(--z200)}
.r-nr{flex:none;width:17mm;text-align:center;background:var(--z700);color:#fff;
  border-radius:8px;padding:1.6mm 0;box-shadow:0 3px 0 var(--z800)}
.r-nr span{display:block;font-family:var(--font-h);font-size:5.6pt;letter-spacing:.14em;color:var(--z300)}
.r-nr b{display:block;font-family:var(--font-h);font-size:19pt;line-height:1;color:#fff}
.r-tyt{flex:1}
.r-tyt h2{font-size:19pt;margin-bottom:.8mm;letter-spacing:-.2px}
.r-miejsce{font-size:9.3pt;color:var(--szary);margin:0;font-family:var(--font-h);letter-spacing:.03em}
.r-ikona{flex:none}
.r-ikona svg{display:block;border-radius:50%;box-shadow:0 3px 8px rgba(6,40,30,.16)}
.r-mysl{font-family:var(--font-h);font-size:12pt;font-style:italic;color:var(--z700);
  background:linear-gradient(90deg,var(--z100),transparent);
  border-left:4px solid var(--gold);padding:2.6mm 4mm;border-radius:0 6px 6px 0;margin-bottom:4mm}

.r-grid{display:grid;grid-template-columns:1.12fr 1fr;gap:4mm;align-items:start}
.r-grid2{display:grid;grid-template-columns:1fr 1fr;gap:4mm;align-items:start}
.blok{background:var(--z050);border:1px solid var(--z200);border-radius:9px;
  padding:3mm 3.6mm;margin-bottom:3mm}
.blok h3{font-size:11.2pt;color:var(--z700);display:flex;align-items:center;gap:2mm;
  margin-bottom:2.2mm;text-transform:uppercase;letter-spacing:.045em;font-size:9.6pt}
.bi{font-size:11pt;line-height:1}
.blok p{font-size:9.9pt;margin-bottom:.4em}

.stresz{counter-reset:st;list-style:none;padding:0;margin:0}
.stresz li{counter-increment:st;position:relative;padding-left:7mm;font-size:10.1pt;
  margin-bottom:1.1mm;line-height:1.36}
.stresz li::before{content:counter(st);position:absolute;left:0;top:.3mm;width:5mm;height:5mm;
  background:var(--z500);color:#fff;border-radius:50%;font-size:7.2pt;font-weight:700;
  font-family:var(--font-h);display:flex;align-items:center;justify-content:center}

.blok-kto{display:flex;align-items:baseline;gap:3mm;flex-wrap:wrap;padding:2.6mm 3.4mm}
.kto-etykieta{flex:none;font-family:var(--font-h);font-size:9pt;font-weight:700;color:var(--z600);
  text-transform:uppercase;letter-spacing:.05em}
.chipy{display:flex;flex-wrap:wrap;gap:2mm;flex:1}
.chip{background:var(--z600);color:#fff;border-radius:20px;padding:1.2mm 3.4mm;
  font-family:var(--font-h);font-size:9pt;font-weight:600}
.slownik{margin:0}

.slowo{margin-bottom:1.5mm;padding-bottom:1.2mm;border-bottom:1px dotted var(--z300)}
.slowo:last-child{border-bottom:0;margin-bottom:0;padding-bottom:0}
.slownik dt{font-family:var(--font-h);font-weight:700;color:var(--z800);font-size:9.7pt}
.slownik dd{margin:.3mm 0 0;font-size:9.5pt;color:var(--tekst);line-height:1.4}

.tab-emo{width:100%;border-collapse:collapse;font-size:9.4pt;table-layout:fixed}
.tab-emo th{background:var(--z600);color:#fff;font-family:var(--font-h);font-size:7.6pt;
  text-transform:uppercase;letter-spacing:.05em;padding:1.4mm 1.6mm;text-align:left;font-weight:600}
.tab-emo th:last-child{text-align:center;width:16%}
.tab-emo td{padding:1.5mm 1.6mm;border-bottom:1px solid var(--z200);vertical-align:top;line-height:1.34}
.tab-emo tr:last-child td{border-bottom:0}
.tab-emo .kto{font-weight:700;color:var(--z800);width:19%}
.tab-emo .emo{color:var(--z600);font-weight:700;width:20%}
.tab-emo .sygn{color:var(--szary);font-size:9pt;width:45%}
.tab-emo .lvl{text-align:center}
.skala{display:inline-flex;gap:.7mm}
.skala i{width:2.1mm;height:2.1mm;border-radius:50%;background:var(--z200);display:block}
.skala i.on{background:var(--z600)}

.wnioski{list-style:none;padding:0;margin:0}
.wnioski li{display:flex;align-items:center;gap:2mm;font-size:9.3pt;margin-bottom:1.8mm;
  background:#fff;border:1px solid var(--z200);border-radius:6px;padding:1.8mm 2.4mm}
.przycz{flex:1.1}
.skutek{flex:1;color:var(--z700);font-weight:700}
.strzalka{flex:none;color:var(--gold);font-size:10pt}

.blok-ocena{border-left:4px solid var(--zolt)}
.blok-ocena.zielone{border-left-color:var(--ziel)}
.blok-ocena.czerwone{border-left-color:var(--czerw)}
.o-pyt{font-weight:700;color:var(--z800);font-size:10pt !important}
.o-odp{display:flex;gap:2.4mm;align-items:flex-start;font-size:9.6pt !important;margin:0}
.o-odp .znak{flex:none;width:6mm;height:6mm;border-radius:50%;background:var(--zolt);color:#fff;
  display:flex;align-items:center;justify-content:center;font-weight:700;font-size:9pt}
.blok-ocena.zielone .znak{background:var(--ziel)}
.blok-ocena.czerwone .znak{background:var(--czerw)}

.blok-tom{background:linear-gradient(135deg,var(--z800),var(--z600));color:#fff;border:0;
  margin-top:1mm}
.blok-tom h3{color:#fff;font-size:10.4pt;text-transform:none;letter-spacing:0}
.blok-tom .etap{background:var(--gold);color:var(--z900);font-family:var(--font-h);font-weight:700;
  font-size:9pt;border-radius:20px;padding:.7mm 3mm;flex:none}
.tom-tresc{background:rgba(255,255,255,.11);border-radius:7px;padding:3mm 3.6mm}
.tom-tresc p{margin:0 0 1.4mm;font-size:9.8pt;color:#EAF6F0;white-space:pre-line}
.tom-tresc p:last-child{margin-bottom:0}
.tom-tyt{color:var(--gold2) !important;font-size:10.4pt !important}
.tom-tresc b{color:var(--gold2)}

.pytania{display:grid;grid-template-columns:1fr 1fr;gap:4mm;margin-top:3.5mm}
.pyt{border-radius:9px;padding:3.4mm 4mm;border:1px solid var(--z200)}
.pyt h3{font-size:9.6pt;text-transform:uppercase;letter-spacing:.045em;display:flex;
  align-items:center;gap:2mm;flex-wrap:wrap;margin-bottom:2mm}
.pyt h3 small{text-transform:none;letter-spacing:0;flex-basis:100%;margin-left:6mm}
.pyt ol{padding-left:5mm;margin:0}
.pyt li{font-size:9.8pt;margin-bottom:1.6mm;line-height:1.4}
.pyt-latwe{background:var(--z050);border-left:4px solid var(--z500)}
.pyt-latwe li::marker{color:var(--z500);font-weight:700}
.pyt-trudne{background:#F1F7FB;border-left:4px solid #3E7CA8}
.pyt-trudne li::marker{color:#3E7CA8;font-weight:700}
.pyt-trudne h3{color:#2C5F82}

.r-foot{margin-top:auto;padding-top:2.6mm;display:flex;justify-content:space-between;
  align-items:center;gap:4mm;
  font-size:8pt;color:var(--z400);border-top:1px solid var(--z200);
  font-family:var(--font-h);letter-spacing:.05em}
.f-znak{display:flex;align-items:center;gap:2mm}
.f-znak svg.mark{width:5mm;height:5mm;display:block;flex:none}
.f-znak b{color:var(--z600);letter-spacing:.08em}
.f-srodek{margin:0 auto;text-align:center}
.f-nr{font-family:var(--font-h);font-size:11.5pt;font-weight:700;color:var(--z600);
  line-height:1;letter-spacing:0;min-width:9mm;text-align:right;
  font-variant-numeric:tabular-nums}

/* ---------- ĆWICZENIA ---------- */
.cwiczenia{display:grid;gap:4mm}
.cwicz{background:var(--z050);border:1px solid var(--z200);border-radius:10px;padding:4mm 4.5mm;
  border-left:5px solid var(--z500);break-inside:avoid}
.c-head{display:flex;gap:3.5mm;align-items:flex-start;margin-bottom:2mm}
.c-nr{flex:none;width:9mm;height:9mm;border-radius:50%;background:var(--z600);color:#fff;
  font-family:var(--font-h);font-weight:700;font-size:12pt;display:flex;align-items:center;justify-content:center}
.c-head h3{font-size:13pt;margin-bottom:.5mm}
.c-meta{font-size:9pt;color:var(--z600);font-family:var(--font-h);margin:0;letter-spacing:.02em}
.c-opis{font-size:10pt}
.c-kroki{padding-left:5mm;margin-bottom:2mm}
.c-kroki li{font-size:9.8pt}
.c-kroki li::marker{color:var(--z500);font-weight:700}
.c-dost{background:#fff;border:1px dashed var(--z400);border-radius:7px;padding:2.4mm 3mm;
  font-size:9.5pt;margin:0}
.c-dost b{color:var(--z600)}

/* ---------- GRA ---------- */
.gra-glowna{display:grid;grid-template-columns:1.05fr 1fr;gap:5mm;align-items:start;margin-bottom:4mm}
.gra-zasady{background:var(--z050);border:1px solid var(--z200);border-radius:10px;padding:4mm}
.gra-zasady h3{font-size:12.5pt}
.gra-zasady ol{padding-left:5mm}
.gra-zasady li{font-size:9.8pt}
.gra-uwaga{background:var(--z700);color:#fff;border-radius:8px;padding:3mm 3.6mm;font-size:9.5pt;margin-top:3mm}
.gra-uwaga b{color:var(--gold2)}
.talie{display:grid;grid-template-columns:1fr 1fr;gap:4mm}
.talia{background:var(--z050);border:1px solid var(--z200);border-radius:10px;padding:3.6mm 4mm}
.talia h4{font-size:10.6pt;display:flex;align-items:center;gap:2.4mm;margin-bottom:2mm;
  text-transform:uppercase;letter-spacing:.05em;font-size:9.6pt}
.kropka{width:4.4mm;height:4.4mm;border-radius:50%;display:inline-block;flex:none;
  border:1.5px solid var(--z800)}
.talia ol{padding-left:5mm;margin:0}
.talia li{font-size:9.4pt;margin-bottom:1.3mm}
.specjalne{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.spec{background:#fff;border:1px solid var(--z200);border-top:4px solid var(--gold);
  border-radius:8px;padding:3mm}
.spec b{font-size:9.6pt;display:block;margin-bottom:1mm;color:var(--z700)}
.spec p{font-size:9.2pt;margin:0;color:var(--szary)}
.plansza{max-width:104mm;margin-left:auto;margin-right:auto}
.plansza figcaption{font-size:8.8pt}

/* ---------- ZAŁĄCZNIKI ---------- */
.plansza-duza{max-width:100%;margin:2mm 0 4mm}
.termometr-duzy{max-width:132mm;margin:3mm auto 5mm}
.krazki{display:grid;grid-template-columns:repeat(2,1fr);gap:7mm;margin:5mm 0 4mm;max-width:158mm}
.krazek{aspect-ratio:1;border-radius:50%;border:2px dashed rgba(255,255,255,.65);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1mm;
  color:#fff;text-align:center;padding:4mm}
.krazek .znak{font-size:26pt;line-height:1;font-weight:700}
.krazek b{font-family:var(--font-h);font-size:13pt;color:#fff;letter-spacing:.06em}
.krazek p{margin:0;font-size:10pt;color:rgba(255,255,255,.9)}
.krazek.zielony{background:var(--ziel)}
.krazek.zolty{background:var(--zolt)}
.krazek.czerwony{background:var(--czerw)}
.karty-planet{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.karta-planeta{border:2px dashed var(--z400);border-radius:12px;overflow:hidden;background:#fff;
  break-inside:avoid;display:flex;flex-direction:column}
.kp-gora .ilu{margin:0;border-radius:0;background:none}
.kp-dol{padding:3.4mm 4mm 4mm;flex:1}
.kp-dol h4{font-size:13pt;margin:0 0 .8mm;color:var(--z800)}
.kp-kto{font-size:9.6pt;color:var(--z600);font-family:var(--font-h);margin:0 0 1.6mm}
.kp-opis{font-size:10pt;margin:0 0 2mm;line-height:1.4}
.kp-pyt{font-size:9.8pt;margin:0;color:var(--z700);background:var(--z050);
  border-left:3px solid var(--gold);border-radius:0 5px 5px 0;padding:1.8mm 2.6mm}

/* ---------- SCENARIUSZ ---------- */
.podtytul-spekt{font-size:16pt;color:var(--z600);text-align:center;font-style:italic;margin:-2mm 0 3mm}
.spekt-info{display:grid;grid-template-columns:repeat(4,1fr);gap:3mm;margin:4mm 0 5mm}
.spekt-info div{background:var(--z700);color:#fff;border-radius:9px;padding:3mm;text-align:center}
.spekt-info span{display:block;font-size:7.8pt;color:var(--z300);text-transform:uppercase;
  letter-spacing:.1em;font-family:var(--font-h);margin-bottom:1mm}
.spekt-info b{font-size:9.8pt;color:#fff;line-height:1.3;display:block}
.spekt-2kol{display:grid;grid-template-columns:1fr 1fr;gap:5mm;align-items:start}
.tab-role,.tab-prob{width:100%;border-collapse:collapse;font-size:9.4pt}
.tab-role td,.tab-prob td{padding:1.4mm 2mm;border-bottom:1px solid var(--z200);vertical-align:top}
.tab-role td:first-child{width:38%;color:var(--z800)}
.tab-prob td:first-child{width:18mm;color:var(--z700)}
.tab-role.szeroka td:first-child{width:30%}
.program{counter-reset:pr;list-style:none;padding:0;margin:0 0 3mm;
  display:grid;grid-template-columns:1fr 1fr;gap:1.6mm 4mm}
.program li{counter-increment:pr;background:var(--z050);border:1px solid var(--z200);
  border-left:4px solid var(--z500);border-radius:0 7px 7px 0;padding:1.8mm 3mm;
  font-size:9.5pt;position:relative;padding-left:9mm}
.program li::before{content:counter(pr);position:absolute;left:3mm;top:2.4mm;color:var(--z500);
  font-family:var(--font-h);font-weight:700}
.program li span{display:block;font-size:8.6pt;color:var(--szary);margin-top:.5mm}
.zas-spekt{padding-left:5mm;column-count:2;column-gap:7mm}
.zas-spekt li{break-inside:avoid}
.rek{padding-left:5mm}
.rek li{font-size:9.4pt}
.zas-spekt li{font-size:9.5pt;margin-bottom:1.8mm}
.zas-spekt li::marker{color:var(--z500);font-weight:700}
.sceny{display:grid;gap:4mm}
.scena{background:var(--z050);border:1px solid var(--z200);border-radius:10px;padding:4mm 4.5mm;
  border-left:5px solid var(--z600);break-inside:avoid}
.s-head{display:flex;align-items:baseline;gap:3mm;margin-bottom:1.5mm}
.s-nr{font-family:var(--font-h);font-size:7.6pt;letter-spacing:.12em;background:var(--z600);
  color:#fff;border-radius:20px;padding:.8mm 3mm;flex:none}
.s-head h4{font-size:13pt;margin:0}
.s-meta{font-size:9pt;color:var(--szary);margin-bottom:2.5mm}
.kwestie{background:#fff;border-radius:8px;padding:3mm 3.6mm;margin-bottom:2.5mm}
.kwestia{display:flex;gap:3mm;padding:1.3mm 0;border-bottom:1px dotted var(--z200);font-size:9.8pt}
.kwestia:last-child{border-bottom:0}
.kwestia .kto{flex:none;width:34mm;font-family:var(--font-h);font-weight:700;font-size:8.6pt;
  color:var(--z700);text-transform:uppercase;letter-spacing:.02em;padding-top:.4mm}
.kwestia .tekst{flex:1}
.s-wsk{font-size:9.3pt;background:#fff;border:1px dashed var(--z400);border-radius:7px;
  padding:2.4mm 3mm;margin:0}
.s-wsk b{color:var(--z600)}

/* ---------- KONIEC ---------- */
.cytat{font-family:var(--font-h);font-size:15pt;font-style:italic;color:var(--z700);
  text-align:center;margin:3mm 6mm;line-height:1.4;position:relative}
.cytat cite{display:block;font-size:10pt;font-style:normal;color:var(--szary);margin-top:3mm;
  font-family:var(--font-t)}
.konc-tresc{max-width:150mm;margin:0 auto 4mm;font-size:10.6pt}
.konc-info{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}
.konc-info div{background:var(--z050);border:1px solid var(--z200);border-radius:9px;padding:3.4mm;
  border-top:4px solid var(--z500)}
.konc-info b{display:block;font-size:9.4pt;color:var(--z700);text-transform:uppercase;
  letter-spacing:.06em;margin-bottom:1mm;font-family:var(--font-h)}
.konc-info span{font-size:9.6pt;color:var(--tekst)}
.metryczka{margin-top:4mm;display:flex;align-items:center;gap:6mm;
  background:var(--z800);border-radius:12px;padding:5mm 6mm;color:#fff}
.metryczka .m-logo{width:24mm;flex:none}
.metryczka .m-logo svg{width:100%;height:auto;display:block}
.m-dane{flex:1}
.m-org{font-family:var(--font-h);font-size:13pt;font-weight:700;color:#fff;margin:0 0 1.5mm}
.m-autor{font-size:10.4pt;color:var(--z200);margin:0 0 2mm}
.m-autor b{color:var(--gold2)}
.m-mail{font-family:var(--font-h);font-size:11pt;color:var(--gold2);margin:0;
  display:flex;align-items:baseline;gap:3mm}
.m-mail span{font-size:8pt;text-transform:uppercase;letter-spacing:.14em;color:var(--z300)}

/* ---------- NAWIGACJA EKRANOWA ---------- */
.topbar{position:sticky;top:0;z-index:50;background:rgba(11,61,46,.97);color:#fff;
  padding:2.5mm 6mm;display:flex;align-items:center;gap:6mm;
  box-shadow:0 2px 12px rgba(6,40,30,.25);backdrop-filter:blur(6px)}
.topbar b{color:#fff;font-family:var(--font-h);font-size:10.5pt;letter-spacing:.02em}
.topbar nav{display:flex;gap:3mm;flex-wrap:wrap;margin-left:auto}
.topbar a{color:var(--z200);text-decoration:none;font-size:9.4pt;border:1px solid rgba(207,235,221,.3);
  border-radius:20px;padding:1mm 3.4mm;font-family:var(--font-h)}
.topbar a:hover{background:var(--z600);color:#fff;border-color:var(--z600)}

/* ---------- DRUK ---------- */
@media print{
  @page{size:A4;margin:0}
  body{background:#fff}
  .topbar{display:none}
  html,body{width:auto}
  .page{margin:0;box-shadow:none;border-radius:0;break-after:page;
    width:auto;max-width:100%;min-height:0;height:auto;display:block;
    padding:12mm 12mm 9mm;overflow:hidden}
  .okladka{height:auto;min-height:0;padding:0}
  .page:last-child{break-after:auto}
  .tab-emo tr,.kwestia,.slowo,.wnioski li,.stresz li,.etapy li,.sy,
  .c-head,.s-head,.program li,.spis-lista li{break-inside:avoid}
  .r-head,.dzial-h,.pod-h{break-after:avoid}
  .r-foot{margin-top:4mm}
  a{color:inherit;text-decoration:none}
}
@media screen and (max-width:800px){
  .page{width:100%;padding:6mm 4mm}
  .r-grid,.r-grid2,.pytania,.spis-grid,.dwie-kolumny,.zas-spekt{column-count:1}
  .r-grid,.r-grid2,.pytania,.spis-grid,.narz,.drabina,.karty3,.zalozenia,.postacie,
  .gra-glowna,.talie,.specjalne,.spekt-2kol,.konc-info,.spekt-info{grid-template-columns:1fr}
  .okladka h1{font-size:28pt}
  .kwestia{flex-direction:column;gap:.5mm}
  .kwestia .kto{width:auto}
}
'''

import re as _re


def css(skala=1.0):
    """Zwraca arkusz stylów ze stopniem pisma przeskalowanym o `skala`.

    Powiększony druk (1.10–1.20) bywa potrzebny uczniom z trudnościami wzrokowymi
    albo młodszym. Skalowane są wyłącznie wartości w punktach — marginesy i siatka
    zostają w milimetrach, dzięki czemu proporcje strony A4 się nie zmieniają.
    """
    if abs(skala - 1.0) < 1e-9:
        return CSS
    return _re.sub(r"([\d.]+)pt", lambda m: f"{float(m.group(1)) * skala:.2f}pt", CSS)
