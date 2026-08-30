import { chromium } from 'playwright';
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p = await b.newPage();
await p.goto('file:///home/user/chatbot/eduplaner_przedszkole/Bank_celow_SMART_KPOF.html');
await p.waitForTimeout(4500);
const kody = ['kon-A-1','kon-A-2','kon-A-3','kon-A-4','kon-A-5'];
for (const [i,k] of kody.entries()) {
  await p.evaluate((k)=>{
    document.querySelectorAll('.kmodal.open').forEach(m=>m.classList.remove('open'));
    otworzKonspekt(k,'p3');
    document.querySelector('#'+k+' .zal-strefa').style.display='block';
    document.documentElement.classList.add('print-zal');
    if(!document.getElementById('pgs')){const st=document.createElement('style');st.id='pgs';
      st.textContent='@media print{@page{size:A4 portrait; margin:9mm 10mm}}';document.head.appendChild(st);}
  }, k);
  await p.waitForTimeout(700);
  await p.pdf({path:`/tmp/pom_${i}.pdf`, printBackground:true, preferCSSPageSize:true});
}
await b.close();
console.log('ok');
