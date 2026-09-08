import { chromium } from 'playwright';
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p = await b.newPage();
await p.goto('file:///home/user/chatbot/eduplaner_przedszkole/Bank_celow_SMART_KPOF.html');
await p.waitForTimeout(2500);
await p.pdf({path:'/home/user/chatbot/eduplaner_przedszkole/Bank_celow_SMART_KPOF.pdf',
  format:'A4', landscape:true, printBackground:true,
  margin:{top:'24mm',bottom:'13mm',left:'9mm',right:'9mm'},
  displayHeaderFooter:true,
  headerTemplate:'<div></div>',
  footerTemplate:`<div style="width:100%;padding:0 9mm;font-family:Arial,sans-serif;font-size:7pt;color:#6C6489;display:flex;justify-content:space-between;border-top:1px solid #DCD7EC;padding-top:3px;">
    <span>EduPlaner 2026 &middot; PCTP &middot; pedagog specjalny mgr Miros&#322;awa Ewa Jurczyszyn</span>
    <span><b style="color:#2D1B69">Strona <span class="pageNumber"></span> z <span class="totalPages"></span></b> &middot; Bank cel&oacute;w SMART &middot; druk KC-1</span></div>`});
await b.close();
