
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
  fs.writeFileSync('_a.html','<!doctype html><html lang="pl"><head><meta charset="utf-8"></head><body>'+fs.readFileSync(WEJSCIE,'utf8')+'</body></html>');
  await p.goto('file://'+process.cwd()+'/_a.html',{waitUntil:'networkidle'});
  await p.waitForTimeout(2500);
  const r=await p.evaluate(()=>{
    const MM=96/25.4;
    const strony=[...document.querySelectorAll('.page')];
    const puste=[], przelane=[];
    strony.forEach((s,i)=>{
      const kids=[...s.children].filter(c=>!c.classList.contains('footer'));
      if(kids.length===0) puste.push(i+1);
      if(s.getBoundingClientRect().height/MM > 298) przelane.push(i+1);
    });
    const bezStopki=strony.map((s,i)=>({i:i+1,s})).filter(x=>!x.s.querySelector('.footer')
        && !x.s.classList.contains('cover') && !x.s.classList.contains('tyl')).map(x=>x.i);
    // spis treści vs faktyczne strony
    const na=new Map();
    strony.forEach((s,i)=>s.querySelectorAll('[data-toc]').forEach(el=>{ if(!na.has(el.dataset.toc)) na.set(el.dataset.toc,i+1); }));
    const zleToc=[];
    document.querySelectorAll('[data-ref]').forEach(el=>{
      const ma=na.get(el.dataset.ref), jest=parseInt(el.textContent,10);
      if(ma!==jest) zleToc.push(el.dataset.ref+': spis '+jest+' ≠ faktycznie '+ma);
    });
    // numeracja stopek
    const zlaNum=[];
    strony.forEach((s,i)=>{
      const pn=s.querySelector('.pagenum b');
      if(pn && parseInt(pn.textContent,10)!==i+1) zlaNum.push(i+1);
    });
    // kluczowe elementy
    const ma = sel => !!document.querySelector(sel);
    const braki=[];
    [['logo PCTP','svg[aria-label^="Logo PCTP"]'],['metryka','.metryka'],['spis treści','.toc'],
     ['koło funkcji','[data-toc="funkcje"]'],['ćwiczenia','.cwiczenie'],['karta uzgodnień','.karta'],
     ['bibliografia','ol.zrodla'],['słowniczek','.slownik'],['ściągawka','.sciagawka'],
     ['tylna okładka','.tyl']].forEach(([n,sel])=>{ if(!ma(sel)) braki.push(n); });
    return {stron:strony.length, puste, przelane, bezStopki, zleToc, zlaNum, braki,
            cwiczen:document.querySelectorAll('.cwiczenie').length,
            zrodel:document.querySelectorAll('ol.zrodla li').length,
            hasel:document.querySelectorAll('.haslo').length,
            logo:document.querySelectorAll('svg[aria-label^="Logo PCTP"]').length};
  });
  console.log(JSON.stringify(r,null,1));
  await b.close();
})();
