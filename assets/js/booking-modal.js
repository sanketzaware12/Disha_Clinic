/* Book Appointment overlay.
   Every link that points to book-appointment/index.html opens this centered popup instead of a new page.
   Settings (slots, closed days, WhatsApp, email) come from assets/js/config.js.
   The /book-appointment/ page itself is unchanged and still works as a fallback. */
(function () {
  'use strict';
  if (document.getElementById('bookForm')) return; // already on the full booking page

  const S = window.SITE || {};
  const me = document.currentScript || document.querySelector('script[src*="booking-modal.js"]');
  const BASE = me && me.src ? me.src.replace(/assets\/js\/booking-modal\.js.*$/, '') : '';
  const SERVICES = ['Laser Piles Treatment', 'Piles (Haemorrhoid) Treatment', 'Anal Fissure Treatment', 'Anal Fistula Treatment', 'Pilonidal Sinus Treatment', 'Perianal Abscess Treatment', 'Laparoscopic (Keyhole) Surgery', 'Gallbladder Stone Surgery', 'Hernia Repair Surgery', 'Appendix Surgery', 'Diagnostic Laparoscopy', 'Hydrocele Surgery', 'Small & Large Bowel Surgery', 'Kidney Stone Treatment', 'Ureteric Stone Removal (URS)', 'Prostate Surgery (TURP)', 'Stricture Urethra Treatment', 'Lipoma, Cyst & Swelling Removal', 'Breast Lump Removal', 'Thyroid Surgery', 'Circumcision (Adult & Child)', 'Foot Corn Treatment', 'Ingrown Toenail Surgery', 'Abscess Surgery', 'Diabetic Foot Care & Surgery', 'Upper GI Endoscopy', 'Lower GI Endoscopy (Colonoscopy)', 'Emergency G.I. Surgery', 'Other / Not sure'];

  const css = `
.bm{position:fixed;inset:0;z-index:2000;display:grid;place-items:center;padding:20px;background:rgba(5,26,15,.58);backdrop-filter:blur(7px);-webkit-backdrop-filter:blur(7px);opacity:0;visibility:hidden;transition:opacity .35s,visibility .35s}
.bm.on{opacity:1;visibility:visible}
.bm-shell{position:relative;width:min(1000px,100%)}
.bm-card{position:relative;display:grid;grid-template-columns:.85fr 1.5fr;width:100%;grid-template-rows:minmax(0,1fr);max-height:min(760px,calc(100vh - 40px));border-radius:26px;overflow:hidden;background:#fff;box-shadow:0 40px 90px rgba(0,0,0,.45);transform:translateY(26px) scale(.96);transition:transform .5s cubic-bezier(.2,.8,.2,1)}
.bm.on .bm-card{transform:none}
.bm-side{position:relative;overflow:hidden;display:flex;flex-direction:column;padding:28px 28px 26px;color:#fff;background:linear-gradient(165deg,#0F6B38 0%,#0A4A2A 48%,#062816 100%)}
.bm-side::before{content:"";position:absolute;width:520px;height:520px;border-radius:50%;left:-120px;bottom:-250px;border:70px solid rgba(255,255,255,.05);pointer-events:none}
.bm-side::after{content:"";position:absolute;width:340px;height:340px;border-radius:50%;right:-150px;top:-130px;background:radial-gradient(circle,rgba(200,162,74,.34),transparent 70%);pointer-events:none}
.bm-side>*{position:relative;z-index:1}
.bm-logo{display:flex;align-items:center;gap:12px;text-decoration:none}
.bm-logo img{width:56px;height:56px;object-fit:contain;flex:none;background:#fff;border-radius:50%;padding:4px;box-shadow:0 8px 20px rgba(0,0,0,.28)}
.bm-lt{display:flex;flex-direction:column;line-height:1}
.bm-lt b{font-family:var(--hf,'Playfair Display',serif);font-size:26px;letter-spacing:.06em;color:#fff;font-weight:700}
.bm-lt small{font-family:var(--bf,Inter,sans-serif);font-size:8.5px;letter-spacing:.09em;text-transform:uppercase;color:#9fd5b2;font-weight:700;margin-top:5px;white-space:nowrap}
.bm-side h2{font-family:var(--hf,'Playfair Display',serif);font-size:clamp(26px,2.7vw,34px);line-height:1.15;margin:22px 0 10px;color:#fff}
.bm-side h2::after{content:"";display:block;width:56px;height:3px;border-radius:3px;margin-top:14px;background:linear-gradient(90deg,#D32F3C,#C8A24A)}
.bm-side>p{margin-bottom:20px;color:rgba(255,255,255,.8);font-size:14.5px;line-height:1.55;max-width:32ch}
.bm-pts{margin-top:auto;display:grid;gap:10px}
.bm-pt{position:relative;overflow:hidden;display:flex;gap:13px;align-items:center;padding:12px 14px;border-radius:16px;cursor:default;background:linear-gradient(135deg,rgba(255,255,255,.16),rgba(255,255,255,.05));border:1px solid rgba(255,255,255,.2);backdrop-filter:blur(14px) saturate(150%);-webkit-backdrop-filter:blur(14px) saturate(150%);box-shadow:0 10px 26px rgba(0,0,0,.2),inset 0 1px 0 rgba(255,255,255,.28);transition:transform .4s cubic-bezier(.2,.8,.2,1),background .4s,border-color .4s,box-shadow .4s}
.bm-pt::before{content:"";position:absolute;top:0;bottom:0;left:-60%;width:45%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.28),transparent);transform:skewX(-18deg);transition:left .8s ease;pointer-events:none}
.bm-pt:hover{transform:translateY(-3px) translateX(4px);background:linear-gradient(135deg,rgba(255,255,255,.26),rgba(255,255,255,.1));border-color:rgba(200,162,74,.75);box-shadow:0 16px 34px rgba(0,0,0,.3),0 0 0 3px rgba(200,162,74,.12),inset 0 1px 0 rgba(255,255,255,.38)}
.bm-pt:hover::before{left:120%}
.bm-pt i{position:relative;flex:none;width:38px;height:38px;border-radius:12px;display:grid;place-items:center;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);color:#f1e3bb;transition:background .4s,color .4s,transform .5s,box-shadow .4s}
.bm-pt:hover i{background:linear-gradient(135deg,#E2C477,#C8A24A);color:#2a2108;border-color:transparent;transform:rotate(-8deg) scale(1.08);box-shadow:0 8px 18px rgba(200,162,74,.45)}
.bm-pt svg{width:19px;height:19px;stroke:currentColor;fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.bm-pt div{position:relative}
.bm-pt b{display:block;font-size:14px;color:#fff}.bm-pt span{display:block;font-size:12.5px;line-height:1.4;color:rgba(255,255,255,.76);margin-top:2px}
.bm-main{position:relative;display:flex;flex-direction:column;overflow-y:auto;padding:30px 36px 28px;background:#fff;scrollbar-width:thin}
.bm-main>form,.bm-main>.bm-ok{margin:auto 0}
.bm-x{position:absolute;top:-14px;right:-14px;z-index:5;width:40px;height:40px;border-radius:50%;border:0;background:#fff;color:#0A4A2A;display:grid;place-items:center;cursor:pointer;box-shadow:0 8px 22px rgba(0,0,0,.3);transition:background .25s,transform .35s,color .25s}
.bm-x:hover{background:#C8A24A;color:#2a2108;transform:rotate(90deg)}
.bm-x svg{width:20px;height:20px;stroke:currentColor;fill:none;stroke-width:2.2;stroke-linecap:round}
.bm-form{display:grid;grid-template-columns:1fr 1fr;gap:12px 16px}
.bm-f{display:flex;flex-direction:column;gap:5px;min-width:0}.bm-f.full{grid-column:1/-1}
.bm-f label,.bm-lb{font-weight:600;font-size:13.5px;color:#1c2b33}.bm-f label em,.bm-lb em{font-style:normal;font-weight:400;color:#6a7a72}
.bm-f input,.bm-f select,.bm-f textarea{width:100%;font:inherit;font-size:14.5px;color:#1c2b33;padding:9px 14px;border:1.5px solid #dfe8e1;border-radius:12px;background:#f8faf6;transition:border-color .25s,box-shadow .25s,background .25s}
.bm-f select{appearance:none;-webkit-appearance:none;padding-right:40px;background:#f8faf6 url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%230A4A2A' stroke-width='2.4' stroke-linecap='round'%3E%3Cpath d='M6 9l6 6 6-6'/%3E%3C/svg%3E") no-repeat right 15px center}
.bm-f textarea{min-height:54px;height:54px;resize:none}
.bm-f input::placeholder,.bm-f textarea::placeholder{color:#9aa8a0}
.bm-f input:focus,.bm-f select:focus,.bm-f textarea:focus{outline:0;background-color:#fff;border-color:#0F6B38;box-shadow:0 0 0 4px rgba(15,107,56,.14)}
.bm-f.bad input,.bm-f.bad select,.bm-f.bad textarea{border-color:#d94141;background-color:#fff8f8}
.bm-e{color:#d94141;font-size:12px;min-height:0;line-height:1.2}.bm-e:empty{display:none}
.bm-chk{display:flex;gap:10px;align-items:flex-start;font-size:13.5px;color:#4a5b53;line-height:1.5;cursor:pointer}
.bm-chk input{width:18px;height:18px;margin-top:2px;flex:none;accent-color:#0F6B38}
.bm-chk a{color:#0F6B38;font-weight:600}
.bm-go{width:100%;display:flex;align-items:center;justify-content:center;gap:10px;padding:13px 20px;border:0;border-radius:50px;cursor:pointer;font:inherit;font-weight:700;font-size:16px;color:#fff;background:linear-gradient(135deg,#0F6B38,#08381E);box-shadow:0 14px 28px rgba(8,56,30,.3);transition:transform .3s,box-shadow .3s}
.bm-go:hover{transform:translateY(-2px);box-shadow:0 18px 34px rgba(8,56,30,.38)}
.bm-go:disabled{opacity:.7;cursor:progress;transform:none}
.bm-go svg{width:19px;height:19px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.bm-ok{display:none;text-align:center;padding:34px 8px 10px}
.bm-ok.on{display:block;animation:bmUp .6s}
.bm-tick{width:76px;height:76px;margin:0 auto 16px;border-radius:50%;display:grid;place-items:center;background:#e6f6ec;color:#1f9d55}
.bm-tick svg{width:38px;height:38px;stroke:currentColor;fill:none;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.bm-ok h3{font-family:var(--hf,'Playfair Display',serif);font-size:26px;margin-bottom:8px;color:#0A4A2A}
.bm-ok p{color:#4a5b53;margin:0 auto 6px;max-width:42ch;line-height:1.55}
.bm-ok .bm-sum{font-weight:600;color:#1c2b33}
.bm-act{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:18px}
.bm-b{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;border-radius:50px;font-weight:600;font-size:14.5px;text-decoration:none;cursor:pointer;border:1.5px solid #0F6B38;color:#0F6B38;background:#fff;transition:.25s}
.bm-b.p{background:linear-gradient(135deg,#0F6B38,#08381E);border-color:transparent;color:#fff}
.bm-b:hover{transform:translateY(-2px)}
.bm-b svg{width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
@keyframes bmUp{from{opacity:0;transform:translateY(18px)}}
body.bm-lock{overflow:hidden}
@media(max-width:900px){
.bm{padding:0;align-items:end}
.bm-shell{width:100%}.bm-card{grid-template-columns:1fr;grid-template-rows:auto minmax(0,1fr);max-height:94vh;border-radius:24px 24px 0 0;transform:translateY(60px)}
.bm-side{padding:22px 24px 20px}.bm-side h2{margin:14px 0 4px;font-size:24px}.bm-side h2::after{display:none}.bm-side>p,.bm-pts{display:none}.bm-logo img{width:44px;height:44px}.bm-lt b{font-size:22px}.bm-lt small{display:none}
.bm-main{padding:20px 20px 24px}
.bm-x{top:12px;right:12px;width:38px;height:38px;background:rgba(255,255,255,.18);color:#fff;box-shadow:none}.bm-x:hover{background:rgba(255,255,255,.3);color:#fff}
}
@media(max-width:560px){.bm-form{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){.bm,.bm-card{transition:none}.bm-ok.on{animation:none}}
.bm-cap{display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:14px;background:linear-gradient(135deg,#f3f9f5,#fff);border:1.5px dashed #bfdcc9}
.bm-cap canvas{flex:none;display:block;width:150px;height:44px;border-radius:10px;border:1px solid #cfe5d6;background:#fff;user-select:none;-webkit-user-select:none}
.bm-cr{flex:none;width:34px;height:34px;border-radius:50%;border:1px solid #dfe8e1;background:#fff;color:#0F6B38;display:grid;place-items:center;cursor:pointer;transition:transform .5s cubic-bezier(.2,1.3,.4,1),background .25s,color .25s}
.bm-cr svg{width:16px;height:16px;stroke:currentColor;fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.bm-cr:hover{background:#0F6B38;color:#fff;transform:rotate(180deg)}
.bm-cap input{flex:1;min-width:0;text-transform:uppercase;letter-spacing:2px;font-weight:700}
.bm-cap input::placeholder{text-transform:none;letter-spacing:0;font-weight:400}
.bm-hp{position:absolute!important;left:-9999px;width:1px;height:1px;overflow:hidden;opacity:0}
@media(max-width:420px){.bm-cap{flex-wrap:wrap}.bm-cap input{flex:1 1 100%}}

.bm-f label[for=bmCap]{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media(min-width:901px){.bm-main{overflow:hidden}}
/* ---- compact popup (smaller width + height) ---- */
@media(min-width:901px){
.bm-shell{width:min(840px,100%)}
.bm-card{grid-template-columns:.72fr 1.5fr;border-radius:22px}
.bm-side{padding:20px 20px 18px}
.bm-logo{gap:9px}.bm-logo img{width:42px;height:42px}.bm-lt b{font-size:21px}.bm-lt small{font-size:7px;letter-spacing:.05em}
.bm-side h2{font-size:24px;margin:14px 0 8px}.bm-side h2::after{margin-top:9px;width:48px}
.bm-side>p{font-size:13px;margin-bottom:12px;line-height:1.5}
.bm-pts{gap:7px}.bm-pt{padding:8px 11px;gap:10px;border-radius:13px}.bm-pt i{width:32px;height:32px;border-radius:10px}.bm-pt svg{width:16px;height:16px}
.bm-pt b{font-size:13px}.bm-pt span{font-size:11.5px;line-height:1.35}
.bm-main{padding:20px 24px 18px}
.bm-form{gap:8px 12px}
.bm-f{gap:3px}
.bm-f label,.bm-lb{font-size:12.5px}
.bm-f input,.bm-f select{padding:6px 11px;font-size:13.5px;border-radius:10px}
.bm-f select{padding-right:34px;background-position:right 12px center}
.bm-f textarea{min-height:36px;height:36px;padding:6px 11px;font-size:13.5px;border-radius:10px}
.bm-chk{font-size:12.5px;line-height:1.4}.bm-chk input{width:16px;height:16px}
.bm-cap{padding:5px 8px;border-radius:12px;gap:6px}.bm-cap canvas{width:124px;height:36px}.bm-cr{width:30px;height:30px}
.bm-go{padding:10px 18px;font-size:14.5px}
.bm-e{font-size:11.5px}
.bm-x{top:-12px;right:-12px;width:36px;height:36px}
}
@media(min-width:901px) and (max-height:640px){.bm-side>p{display:none}.bm-pt span{display:none}}
`;

  const ic = {
    refresh: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11a8 8 0 10-2.3 5.7"/><path d="M20 4v7h-7"/></svg>',
    close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
    lock: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/></svg>',
    clock: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    check: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 13l4 4L19 7"/></svg>',
    cal: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
    wa: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21l1.6-4.8A9 9 0 1112 21a9 9 0 01-4.2-1z"/><path d="M9 9c0 3 3 6 6 6l1-2-2-1-1 .8c-.8-.4-1.6-1.2-2-2L11.8 10l-1-2z"/></svg>',
    mail: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
  };
  const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  let root, form, lastFocus, built = false;
  const $ = (s, c = root) => c.querySelector(s), $$ = (s, c = root) => [...c.querySelectorAll(s)];

  function build() {
    const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    root = document.createElement('div'); root.className = 'bm'; root.setAttribute('role', 'dialog'); root.setAttribute('aria-modal', 'true'); root.setAttribute('aria-labelledby', 'bmTitle');
    const hrs = esc(S.hours || 'Daily: 10:00 AM – 9:00 PM').replace(/^Daily:\s*/, 'Daily, ');
    root.innerHTML =
      '<div class="bm-shell">' +
        '<button class="bm-x" type="button" aria-label="Close">' + ic.close + '</button>' +
        '<div class="bm-card">' +
        '<aside class="bm-side">' +
          '<div class="bm-logo"><img src="' + BASE + 'assets/img/emblem.png" alt="' + esc(S.name || 'DISHA') + ' logo" width="56" height="56"><span class="bm-lt"><b>' + esc(S.short || 'DISHA') + '</b><small>' + esc(S.subtitle || '') + '</small></span></div>' +
          '<h2 id="bmTitle">Book a consultation</h2>' +
          '<p>Tell us a little about your problem and when suits you. The clinic will call you to confirm.</p>' +
          '<div class="bm-pts">' +
            '<div class="bm-pt"><i>' + ic.lock + '</i><div><b>Private and respectful</b><span>Your details are used only to contact you about this request.</span></div></div>' +
            '<div class="bm-pt"><i>' + ic.clock + '</i><div><b>Clinic hours</b><span>' + hrs + '</span></div></div>' +
            '<div class="bm-pt"><i>' + ic.check + '</i><div><b>A request, not a final booking</b><span>Your slot is confirmed once our team calls you back.</span></div></div>' +
          '</div>' +
        '</aside>' +
        '<div class="bm-main">' +
          '<form class="bm-wrap" novalidate>' +
            '<div class="bm-form">' +
              '<div class="bm-f"><label for="bmName">Full name</label><input id="bmName" name="name" type="text" placeholder="Your name" autocomplete="name"><small class="bm-e"></small></div>' +
              '<div class="bm-f"><label for="bmPhone">Mobile number</label><input id="bmPhone" name="phone" type="tel" inputmode="tel" placeholder="+91" autocomplete="tel"><small class="bm-e"></small></div>' +
              '<div class="bm-f"><label for="bmEmail">Email <em>(optional)</em></label><input id="bmEmail" name="email" type="email" placeholder="you@example.com" autocomplete="email"><small class="bm-e"></small></div>' +
              '<div class="bm-f"><label for="bmDate">Preferred date</label><input id="bmDate" name="date" type="date"><small class="bm-e"></small></div>' +
              '<div class="bm-f"><label for="bmService">Service / problem</label><select id="bmService" name="service"><option value="">Select a service</option>' + SERVICES.map(x => '<option>' + esc(x) + '</option>').join('') + '</select><small class="bm-e"></small></div>' +
              '<div class="bm-f"><label for="bmSlot">Preferred time</label><select id="bmSlot" name="slot"></select><small class="bm-e"></small></div>' +
              '<div class="bm-f full"><label for="bmMsg">Brief message <em>(optional)</em></label><textarea id="bmMsg" name="message" placeholder="Briefly describe your problem"></textarea></div>' +
              '<div class="bm-f full"><label class="bm-chk"><input type="checkbox" name="consent"><span>I have read the <a href="' + BASE + 'privacy-policy/index.html" target="_blank" rel="noopener">Privacy Policy</a> and agree to be contacted.</span></label><small class="bm-e"></small></div>' +
              '<div class="bm-f full"><label for="bmCap">Security check</label><div class="bm-cap"><canvas id="bmCapCv" width="150" height="44" role="img" aria-label="Captcha code"></canvas><button class="bm-cr" type="button" aria-label="Get a new code" title="New code">' + ic.refresh + '</button><input id="bmCap" name="captcha" type="text" placeholder="Type the code" maxlength="5" autocomplete="off" autocapitalize="characters" spellcheck="false"></div><small class="bm-e"></small></div>' +
              '<div class="bm-hp" aria-hidden="true"><label>Leave this empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>' +
              '<div class="bm-f full"><button class="bm-go" type="submit">' + ic.cal + ' <span>Request consultation</span></button></div>' +
            '</div>' +
          '</form>' +
          '<div class="bm-ok" aria-live="polite">' +
            '<div class="bm-tick">' + ic.check + '</div><h3>Request received</h3><p class="bm-sum"></p>' +
            '<p>Our team will call you to confirm the appointment. You can also send the details straight away:</p>' +
            '<div class="bm-act"><a class="bm-b p bm-wa" target="_blank" rel="noopener" href="#">' + ic.wa + ' Send via WhatsApp</a><a class="bm-b bm-mail" href="#">' + ic.mail + ' Send via Email</a></div>' +
            '<div class="bm-act"><button class="bm-b bm-done" type="button">Close</button></div>' +
          '</div>' +
        '</div>' +
      '</div></div>';
    document.body.appendChild(root);
    form = $('form');
    wire();
    built = true;
  }

  const setErr = (el, msg) => {
    const f = el.closest('.bm-f'); if (!f) return;
    f.classList.toggle('bad', !!msg); $('.bm-e', f).textContent = msg || '';
  };

  /* ---- captcha: canvas code, case-insensitive check, new code on wrong answer / each open ---- */
  let capCode = '';
  function capDraw() {
    const cv = $('#bmCapCv'); if (!cv) return;
    const W = 150, H = 44, r = window.devicePixelRatio || 1, x = cv.getContext('2d'), CH = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', rnd = n => Math.floor(Math.random() * n);
    cv.width = W * r; cv.height = H * r; x.setTransform(r, 0, 0, r, 0, 0);
    capCode = ''; for (let i = 0; i < 5; i++) capCode += CH.charAt(rnd(CH.length));
    const g = x.createLinearGradient(0, 0, W, H); g.addColorStop(0, '#eef7f1'); g.addColorStop(1, '#fbf5e4'); x.fillStyle = g; x.fillRect(0, 0, W, H);
    for (let i = 0; i < 6; i++) { x.strokeStyle = 'rgba(' + (i % 2 ? '200,162,74' : '15,107,56') + ',.45)'; x.lineWidth = 1 + Math.random(); x.beginPath(); x.moveTo(rnd(W), rnd(H)); x.bezierCurveTo(rnd(W), rnd(H), rnd(W), rnd(H), rnd(W), rnd(H)); x.stroke(); }
    for (let i = 0; i < 40; i++) { x.fillStyle = 'rgba(8,56,30,' + (Math.random() * .35) + ')'; x.fillRect(rnd(W), rnd(H), 2, 2); }
    for (let i = 0; i < capCode.length; i++) {
      x.save(); x.translate(16 + i * 28, 28 + rnd(6) - 3); x.rotate((Math.random() - .5) * .6);
      x.font = '700 ' + (24 + rnd(5)) + 'px Georgia, serif'; x.textAlign = 'center'; x.fillStyle = i % 2 ? '#0a4a2a' : '#7a5c12'; x.fillText(capCode.charAt(i), 0, 0); x.restore();
    }
  }
  function capReset() { capDraw(); if (form) { form.elements.captcha.value = ''; setErr(form.elements.captcha, ''); } }

  function wire() {
    const pad = n => String(n).padStart(2, '0'), now = new Date();
    const di = $('#bmDate'), sel = $('#bmSlot');
    di.min = now.getFullYear() + '-' + pad(now.getMonth() + 1) + '-' + pad(now.getDate());

    const render = () => {
      sel.innerHTML = '<option value="">Select a slot</option>';
      let closed = false, d = null;
      if (di.value) { d = new Date(di.value + 'T00:00'); closed = (S.closedDays || []).includes(d.getDay()); }
      if (closed) { sel.innerHTML = '<option value="">Closed on this day</option>'; sel.disabled = true; return; }
      sel.disabled = false;
      const seed = d ? d.getDate() + d.getMonth() : 0, today = new Date();
      (S.slots || []).forEach((s2, k) => {
        const o = document.createElement('option'); o.value = s2; o.textContent = s2;
        if (d) {
          let off = (seed + k) % 5 === 0; // demo: some slots shown as booked (same as the booking page)
          if (d.toDateString() === today.toDateString()) {
            const [m, ap] = s2.split(' '); let [h, mi] = m.split(':').map(Number);
            if (ap === 'PM' && h < 12) h += 12; if (ap === 'AM' && h === 12) h = 0;
            const sd = new Date(d); sd.setHours(h, mi); if (sd <= today) off = true;
          }
          if (off) { o.disabled = true; o.textContent = s2 + ' (booked)'; }
        }
        sel.appendChild(o);
      });
    };
    $('.bm-cr').onclick = () => { capReset(); form.elements.captcha.focus(); };
    capDraw();
    di.addEventListener('change', () => { render(); setErr(di, ''); setErr(sel, ''); });
    render();

    $$('input,select,textarea', form).forEach(el => el.addEventListener('input', () => setErr(el, '')));

    form.addEventListener('submit', e => {
      e.preventDefault();
      const v = n => form.elements[n].value.trim();
      if (form.elements.website.value) return; // honeypot: bots fill hidden fields
      let bad = null; const fail = (el, m) => { setErr(el, m); bad = bad || el; };
      if (v('name').length < 2) fail(form.elements.name, 'Please enter your full name.');
      if (!/^\+?[0-9\s-]{10,15}$/.test(v('phone'))) fail(form.elements.phone, 'Enter a valid mobile number.');
      if (v('email') && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v('email'))) fail(form.elements.email, 'Enter a valid email address.');
      if (!v('date')) fail(form.elements.date, 'Please pick a date.');
      if (!v('service')) fail(form.elements.service, 'Please select a service.');
      if (!v('date')) { /* handled above */ } else if (sel.disabled) fail(form.elements.date, 'OPD is closed on this day. Please choose another date.');
      else if (!v('slot')) fail(sel, 'Please choose a time slot.');
      if (!form.elements.consent.checked) fail(form.elements.consent, 'Please accept to continue.');
      { const c = v('captcha').toUpperCase();
        if (!c) fail(form.elements.captcha, 'Please type the code shown.');
        else if (c !== capCode) { fail(form.elements.captcha, 'Wrong code. Please try the new one.'); capDraw(); form.elements.captcha.value = ''; } }
      if (bad) { bad.focus && bad.focus({ preventScroll: true }); bad.closest('.bm-f').scrollIntoView({ behavior: 'smooth', block: 'center' }); return; }

      const btn = $('.bm-go', form), lab = $('span', btn); btn.disabled = true; lab.textContent = 'Sending…';
      const msg = encodeURIComponent('Appointment Request\nName: ' + v('name') + '\nPhone: ' + v('phone') + '\nService: ' + v('service') + '\nDoctor: Dr. Abhijeet Suresh Shinde\nDate: ' + v('date') + '\nTime: ' + v('slot') + '\nNote: ' + (v('message') || '-'));
      // TODO: connect your backend / form service here (fetch POST) before going live
      setTimeout(() => {
        form.style.display = 'none';
        $('.bm-sum').textContent = v('service') + ' on ' + v('date') + ' at ' + v('slot');
        $('.bm-wa').href = 'https://wa.me/' + (S.whatsapp || '') + '?text=' + msg;
        $('.bm-mail').href = 'mailto:' + (S.email || '') + '?subject=' + encodeURIComponent('Appointment Request') + '&body=' + msg;
        $('.bm-ok').classList.add('on'); $('.bm-main').scrollTo({ top: 0 });
      }, 900);
    });

    $('.bm-x').onclick = close; $('.bm-done').onclick = close;
    root.addEventListener('mousedown', e => { if (e.target === root) close(); });
    document.addEventListener('keydown', e => {
      if (!root.classList.contains('on')) return;
      if (e.key === 'Escape') { close(); return; }
      if (e.key === 'Tab') { // keep focus inside the dialog
        const f = $$('a[href],button:not(:disabled),input:not([type=hidden]),select,textarea', root).filter(x => x.offsetParent !== null);
        if (!f.length) return; const a = f[0], z = f[f.length - 1];
        if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
        else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
      }
    });
  }

  /* keep the popup fully visible without scrolling: if the screen is too short, scale the whole card down */
  function fit() {
    const sh = $('.bm-shell'); if (!sh) return;
    sh.style.zoom = ''; $('.bm-card').style.maxHeight = '';
    if (window.innerWidth <= 900) return;
    const card = $('.bm-card'), main = $('.bm-main');
    card.style.maxHeight = 'none';
    const need = Math.max(main.scrollHeight, card.getBoundingClientRect().height), avail = window.innerHeight - 30;
    if (need > avail) sh.style.zoom = Math.max(.6, avail / need).toFixed(3); else card.style.maxHeight = '';
  }
  window.addEventListener('resize', () => { if (root && root.classList.contains('on')) fit(); });

  function open(service) {
    if (!built) build();
    lastFocus = document.activeElement;
    // fresh form each time (unless the thank-you screen was showing)
    form.reset(); form.style.display = ''; capReset(); $('.bm-ok').classList.remove('on');
    $$('.bm-f.bad', form).forEach(f => { f.classList.remove('bad'); $('.bm-e', f).textContent = ''; });
    const btn = $('.bm-go', form); btn.disabled = false; $('span', btn).textContent = 'Request consultation';
    $('#bmDate').dispatchEvent(new Event('change'));
    if (service) { const o = [...$('#bmService').options].find(x => x.text === service); if (o) $('#bmService').value = o.value; }
    // close the mobile menu if it is open
    document.body.classList.remove('menu-open');
    document.body.classList.add('bm-lock');
    requestAnimationFrame(() => { fit(); root.classList.add('on'); setTimeout(() => $('#bmName').focus({ preventScroll: true }), 380); });
  }
  function close() {
    root.classList.remove('on'); document.body.classList.remove('bm-lock');
    lastFocus && lastFocus.focus && lastFocus.focus({ preventScroll: true });
  }

  // Intercept every link to the booking page (header, nav, hero, CTAs, footer, service pages)
  document.addEventListener('click', e => {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    const a = e.target.closest && e.target.closest('a[href]'); if (!a) return;
    const h = a.getAttribute('href') || '';
    if (!/(^|\/)book-appointment\/(index\.html)?(\?.*)?(#.*)?$/.test(h) || a.target === '_blank') return;
    e.preventDefault(); open(a.dataset.service);
  });
  window.openBooking = open;
})();
