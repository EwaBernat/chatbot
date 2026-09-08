import { chromium } from 'playwright';
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p = await b.newPage();
await p.goto('file:///home/user/chatbot/eduplaner_przedszkole/Bank_celow_SMART_KPOF.html');
await p.waitForTimeout(2300);
const ids=(process.env.KIDS||'kon-A-29,kon-A-30,kon-A-31,kon-A-32,kon-A-33').split(',');
const PAGE_H = 297*96/25.4 - 2*(10*96/25.4);   // A4 minus margines 10mm
for(const id of ids){
  await p.evaluate(id=>{
    document.querySelectorAll('.kmodal.open').forEach(m=>m.classList.remove('open'));
    otworzKonspekt(id,'p2');
    document.documentElement.classList.add('print-konspekt');
    if(!document.getElementById('konfix')){
      const st=document.createElement('style'); st.id='konfix';
      st.textContent='@media print{@page{size:A4 portrait; margin:10mm 11mm}}';
      document.head.appendChild(st);
    }
  }, id);
  await p.emulateMedia({media:'print'});
  await p.setViewportSize({width:710, height:1050});
  await p.waitForTimeout(250);
  const h = await p.evaluate(()=>document.querySelector('.kmodal.open .kcard').getBoundingClientRect().height);
  const scale = Math.min(1, Math.max(0.55, (PAGE_H/h)*0.985));
  await p.emulateMedia({media:null});
  await p.pdf({path:`/tmp/claude-0/-home-user-chatbot/aa44147f-aeb3-5c19-9c99-76b87107e663/scratchpad/${id}.pdf`,
    printBackground:true, preferCSSPageSize:true, scale:Number(scale.toFixed(3))});
  console.log(id,'h=',Math.round(h),'scale=',scale.toFixed(3));
}
await b.close();
