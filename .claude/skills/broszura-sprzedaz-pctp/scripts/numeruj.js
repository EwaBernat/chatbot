// Przelicza numery stron w stopkach i w spisie treści na podstawie faktycznego układu.
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
  fs.writeFileSync('_n.html','<!doctype html><html lang="pl"><head><meta charset="utf-8"></head><body>'+fs.readFileSync(WEJSCIE,'utf8')+'</body></html>');
  await p.goto('file://'+process.cwd()+'/_n.html',{waitUntil:'networkidle'});
  await p.waitForTimeout(2500);

  const r=await p.evaluate(()=>{
    const strony=[...document.querySelectorAll('.page')];
    const RAZEM=strony.length;
    strony.forEach((s,i)=>{
      const nr=i+1;
      const pn=s.querySelector('.pagenum');
      if(pn) pn.innerHTML='Strona <b>'+String(nr).padStart(2,'0')+'</b> z '+RAZEM;
    });
    const na=new Map();
    strony.forEach((s,i)=>s.querySelectorAll('[data-toc]').forEach(el=>{
      if(!na.has(el.dataset.toc)) na.set(el.dataset.toc,i+1);
    }));
    const braki=[];
    document.querySelectorAll('[data-ref]').forEach(el=>{
      const n=na.get(el.dataset.ref);
      if(n) el.textContent=String(n).padStart(2,'0'); else braki.push(el.dataset.ref);
    });
    // metryka: liczba stron
    document.querySelectorAll('.metryka dd').forEach(dd=>{
      dd.innerHTML=dd.innerHTML.replace(/\d+ stron A4/, RAZEM+' stron A4');
    });
    document.querySelectorAll('.tyl-stopka .meta').forEach(m=>{
      m.innerHTML=m.innerHTML.replace(/\d+ stron/, RAZEM+' stron');
    });
    return {razem:RAZEM, braki};
  });
  console.log('stron:', r.razem, '| nieuzupełnione kotwice:', JSON.stringify(r.braki));

  const wynik=await p.evaluate(()=>{
    const tb=document.querySelector('.toolbar');
    return (tb?tb.outerHTML+'\n\n':'')+[...document.querySelectorAll('.page')].map(s=>s.outerHTML).join('\n\n');
  });
  const zrod=fs.readFileSync(WEJSCIE,'utf8');
  fs.writeFileSync(WEJSCIE, zrod.slice(0, zrod.indexOf('<div class="toolbar">')) + wynik + '\n');
  await b.close();
})();
