// Ciasno rozkłada bloki w podanym zakresie stron (numeracja od 1, włącznie).
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
  const [od,doo]=process.argv.slice(2).map(Number);
  const b=await chromium.launch(fs.existsSync(PRZEGL)?{executablePath:PRZEGL}:{});
  const p=await b.newPage({viewport:{width:1000,height:1200}});
  fs.writeFileSync('_pp.html','<!doctype html><html lang="pl"><head><meta charset="utf-8"></head><body>'+fs.readFileSync(WEJSCIE,'utf8')+'</body></html>');
  await p.goto('file://'+process.cwd()+'/_pp.html',{waitUntil:'networkidle'});
  await p.waitForTimeout(2500);
  const r=await p.evaluate(({od,doo})=>{
    const MM=96/25.4, WYS=297*MM;
    const strony=[...document.querySelectorAll('.page')];
    const grupa=strony.slice(od-1,doo);
    const stopka=grupa[0].querySelector('.footer').cloneNode(true);
    const tlo=grupa[0].className;
    const bloki=[]; grupa.forEach(s=>[...s.children].forEach(c=>{ if(!c.classList.contains('footer')) bloki.push(c); }));
    grupa.forEach(s=>[...s.children].forEach(c=>{ if(!c.classList.contains('footer')) c.remove(); }));

    let i=0, str=grupa[0];
    const nowa=()=>{ i++;
      if(grupa[i]) return grupa[i];
      const d=document.createElement('div'); d.className=tlo;
      d.appendChild(stopka.cloneNode(true)); grupa[i-1].after(d); grupa.push(d); return d; };
    const trzyma = el => el.matches('div.kicker, h2.section, h3.sub') ||
      (el.matches('p, p.lead') && el.previousElementSibling &&
       el.previousElementSibling.matches('div.kicker, h2.section, h3.sub'));

    for(const blok of bloki){
      str.insertBefore(blok, str.querySelector('.footer'));
      if(str.scrollHeight > WYS+1){
        str.removeChild(blok);
        const przenies=[];
        for(;;){
          const dzieci=[...str.children].filter(c=>!c.classList.contains('footer'));
          const ost=dzieci[dzieci.length-1];
          if(dzieci.length>1 && ost && trzyma(ost)){ przenies.unshift(ost); str.removeChild(ost); } else break;
        }
        if([...str.children].filter(c=>!c.classList.contains('footer')).length===0){
          str.insertBefore(blok, str.querySelector('.footer')); continue; }
        str=nowa();
        przenies.forEach(e=>str.insertBefore(e, str.querySelector('.footer')));
        str.insertBefore(blok, str.querySelector('.footer'));
      }
    }
    let usuniete=0;
    grupa.forEach(s=>{ if([...s.children].filter(c=>!c.classList.contains('footer')).length===0){ s.remove(); usuniete++; } });
    return {przed:doo-od+1, po:grupa.length-usuniete};
  },{od,doo});
  console.log(`strony ${od}–${doo}: było ${r.przed}, jest ${r.po}`);
  const wynik=await p.evaluate(()=>{
    const tb=document.querySelector('.toolbar');
    return (tb?tb.outerHTML+'\n\n':'')+[...document.querySelectorAll('.page')].map(s=>s.outerHTML).join('\n\n');
  });
  const zrod=fs.readFileSync(WEJSCIE,'utf8');
  fs.writeFileSync(WEJSCIE, zrod.slice(0, zrod.indexOf('<div class="toolbar">')) + wynik + '\n');
  await b.close();
})();
