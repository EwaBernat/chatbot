import { chromium } from 'playwright';
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p = await b.newPage();
await p.goto('file:///home/user/chatbot/eduplaner_przedszkole/Bank_celow_SMART_KPOF.html');
await p.waitForTimeout(3000);
await p.evaluate(()=>{
  otworzKonspekt('kon-C-1','p3');
  document.querySelector('#kon-C-1 .zal-strefa').style.display='block';
  document.documentElement.classList.add('print-zal');
  const st=document.createElement('style');
  st.textContent='@media print{@page{size:A4 portrait; margin:9mm 10mm}}';
  document.head.appendChild(st);
});
await p.waitForTimeout(1200);
await p.pdf({path:'/home/user/chatbot/eduplaner_przedszkole/Zalaczniki_KC3_C1-01_Historyjki_6lat.pdf',
  printBackground:true, preferCSSPageSize:true});
await b.close();
console.log('ok');
