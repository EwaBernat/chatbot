
// Playwright bywa zainstalowany w katalogu roboczym, a nie przy skillu.
function wczytajPlaywright(){
  try { return require('playwright'); } catch(e) {}
  try { return require(require('path').join(process.cwd(),'node_modules','playwright')); } catch(e) {}
  console.error('Brak playwright. Uruchom w katalogu projektu:  npm install playwright');
  process.exit(1);
}
const {chromium}=wczytajPlaywright();
const fs=require('fs');
const WEJSCIE=process.argv[2]&&!/^\d+$/.test(process.argv[2]) ? process.argv[2] : 'broszura.html';
const PRZEGL=process.env.CHROMIUM_PATH||'/opt/pw-browsers/chromium-1194/chrome-linux/chrome';
(async()=>{
  const b=await chromium.launch(fs.existsSync(PRZEGL)?{executablePath:PRZEGL}:{});
  const p=await b.newPage({viewport:{width:1000,height:1200}});
  await p.goto('file://'+require('path').resolve(WEJSCIE),{waitUntil:'load'});
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(1500);
  const s=await p.evaluate(()=>{
    const strony=[...document.querySelectorAll('.page')];
    const nr=el=>{ const s=el.closest('.page'); return strony.indexOf(s)+1; };
    const wynik=[];
    // strony wstępne
    strony.forEach((s,i)=>{
      const h=s.querySelector('h2.section, h1');
      if(i===0) wynik.push({poziom:0,tytul:'Okładka',str:1});
    });
    const red=document.querySelector('[data-toc="redakcyjna"]');
    if(red) wynik.push({poziom:0,tytul:'O tej broszurze',str:nr(red)});
    const toc=document.querySelector('.toc');
    if(toc) wynik.push({poziom:0,tytul:'Spis treści',str:nr(toc)});
    const wpr=document.querySelector('[data-toc="wprowadzenie"]');
    if(wpr) wynik.push({poziom:0,tytul:'Wprowadzenie',str:nr(wpr)});
    // rozdziały i podsekcje ze spisu treści
    document.querySelectorAll('.toc-grupa').forEach(g=>{
      const nrRz=g.querySelector('.toc-naglowek .nr')?.textContent.trim();
      const tyt=g.querySelector('.toc-naglowek .tyt')?.textContent.trim();
      const str=parseInt(g.querySelector('.toc-naglowek .str')?.textContent,10);
      const etykieta = (nrRz && /^[IVXLC]+$/.test(nrRz)) ? nrRz+'. '+tyt : tyt;
      if(tyt&&str) wynik.push({poziom:0,tytul:etykieta,str});
      g.querySelectorAll('.toc-poz').forEach(poz=>{
        const t=poz.querySelector('.co')?.textContent.trim();
        const s2=parseInt(poz.querySelector('.str')?.textContent,10);
        if(t&&s2) wynik.push({poziom:1,tytul:t,str:s2});
      });
    });
    const tyl=document.querySelector('.page.tyl');
    if(tyl) wynik.push({poziom:0,tytul:'Tylna okładka',str:strony.indexOf(tyl)+1});
    // zakładki muszą iść w kolejności stron, inaczej czytnik pokazuje je chaotycznie;
    // przy równych stronach rozdział (poziom 0) ma być przed swoimi podsekcjami
    wynik.sort((a,b)=> a.str-b.str || a.poziom-b.poziom);
    return wynik;
  });
  fs.writeFileSync('struktura.json', JSON.stringify(s,null,1));
  console.log('pozycji do zakładek:', s.length);
  s.filter(x=>x.poziom===0).forEach(x=>console.log('  ', String(x.str).padStart(2), x.tytul));
  await b.close();
})();
