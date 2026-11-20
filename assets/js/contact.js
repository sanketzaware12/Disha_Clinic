/* Contact page: scroll reveal, live "open now" status, today highlight, copy-to-clipboard, cursor spotlight */
(function () {
  var calm = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

  /* ---- scroll reveal (hands control back to hover styles once done) ---- */
  var rv = Array.prototype.slice.call(document.querySelectorAll('.ct-rv'));
  function done(el) { setTimeout(function () { el.classList.add('settled'); }, 1200 + (parseFloat(el.style.getPropertyValue('--d')) || 0) * 1000); }
  if (calm || !('IntersectionObserver' in window)) {
    rv.forEach(function (el) { el.classList.add('in', 'settled'); });
  } else {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in'); done(e.target); io.unobserve(e.target);
      });
    }, { threshold: 0.01, rootMargin: '0px 0px -40px 0px' });
    rv.forEach(function (el) { io.observe(el); });
  }

  /* ---- live open / closed + today (clinic time, IST). Only today's row is shown and it refreshes itself ---- */
  var S = window.SITE || {};
  var closed = S.closedDays || [];
  var DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  function clinicNow() {
    var d, h;
    try {
      var parts = new Intl.DateTimeFormat('en-US', { timeZone: 'Asia/Kolkata', weekday: 'short', hour: 'numeric', minute: 'numeric', hour12: false }).formatToParts(new Date()), o = {};
      parts.forEach(function (p) { o[p.type] = p.value; });
      d = DAYS.indexOf(o.weekday);
      h = (+o.hour % 24) + (+o.minute) / 60;
    } catch (e) { var n = new Date(); d = n.getDay(); h = n.getHours() + n.getMinutes() / 60; }
    return { d: d, h: h };
  }
  function refreshLive() {
    var t = clinicNow(), d = t.d, h = t.h;
    var isOpen = closed.indexOf(d) === -1 && h >= 10 && h < 21;
    document.querySelectorAll('[data-live]').forEach(function (el) {
      el.classList.toggle('closed', !isOpen);
      var x = el.querySelector('[data-live-t]') || el;
      x.textContent = isOpen ? 'Open now \u00b7 until 9:00 PM' : 'Closed now \u00b7 opens 10:00 AM';
    });
    document.querySelectorAll('.ct-day').forEach(function (row) {
      var isToday = +row.getAttribute('data-d') === d;
      row.hidden = !isToday;
      row.classList.toggle('today', isToday);
    });
  }
  refreshLive();
  setInterval(refreshLive, 60000);
  document.addEventListener('visibilitychange', function () { if (!document.hidden) refreshLive(); });

  /* ---- copy buttons ---- */
  var toast = document.querySelector('.ct-toast'), tt;
  function say(msg) {
    if (!toast) return;
    toast.querySelector('span').textContent = msg;
    toast.classList.add('on'); clearTimeout(tt);
    tt = setTimeout(function () { toast.classList.remove('on'); }, 1800);
  }
  function copy(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) return navigator.clipboard.writeText(text);
    return new Promise(function (res) {
      var a = document.createElement('textarea'); a.value = text; a.style.position = 'fixed'; a.style.opacity = '0';
      document.body.appendChild(a); a.select(); try { document.execCommand('copy'); } catch (e) {} a.remove(); res();
    });
  }
  document.querySelectorAll('.ct-copy').forEach(function (b) {
    b.addEventListener('click', function () {
      copy(b.getAttribute('data-copy')).then(function () {
        b.classList.add('done'); say((b.getAttribute('data-label') || 'Text') + ' copied');
        setTimeout(function () { b.classList.remove('done'); }, 1600);
      });
    });
  });

  /* ---- cursor spotlight (mouse devices only) ---- */
  if (window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
    document.querySelectorAll('.ct-q,.ct-card').forEach(function (c) {
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        c.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }

  /* ---- captcha (frontend): canvas code, case-insensitive check, auto-refresh, blocks submit until correct ---- */
  (function () {
    var form = document.getElementById('enqForm'), cv = document.getElementById('capCanvas'), inp = document.getElementById('captcha');
    if (!form || !cv || !inp) return;
    var refBtn = form.querySelector('.cap-ref'), hp = form.querySelector('input[name="website"]');
    var CH = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789', code = '';
    function rnd(n) { return Math.floor(Math.random() * n); }
    function draw() {
      var W = 150, H = 44, r = window.devicePixelRatio || 1, x = cv.getContext('2d');
      cv.width = W * r; cv.height = H * r; x.setTransform(r, 0, 0, r, 0, 0);
      code = ''; for (var i = 0; i < 5; i++) code += CH.charAt(rnd(CH.length));
      var g = x.createLinearGradient(0, 0, W, H); g.addColorStop(0, '#eef7f1'); g.addColorStop(1, '#fbf5e4');
      x.fillStyle = g; x.fillRect(0, 0, W, H);
      for (i = 0; i < 6; i++) { x.strokeStyle = 'rgba(' + (i % 2 ? '200,162,74' : '15,107,56') + ',.45)'; x.lineWidth = 1 + Math.random(); x.beginPath(); x.moveTo(rnd(W), rnd(H)); x.bezierCurveTo(rnd(W), rnd(H), rnd(W), rnd(H), rnd(W), rnd(H)); x.stroke(); }
      for (i = 0; i < 40; i++) { x.fillStyle = 'rgba(8,56,30,' + (Math.random() * .35) + ')'; x.fillRect(rnd(W), rnd(H), 2, 2); }
      for (i = 0; i < code.length; i++) {
        x.save(); x.translate(16 + i * 28, 28 + rnd(6) - 3); x.rotate((Math.random() - .5) * .6);
        x.font = '700 ' + (24 + rnd(5)) + 'px Georgia, serif'; x.textAlign = 'center';
        x.fillStyle = i % 2 ? '#0a4a2a' : '#7a5c12'; x.fillText(code.charAt(i), 0, 0); x.restore();
      }
    }
    function newCode(clear) { draw(); if (clear) inp.value = ''; }
    function fix(msg) { /* runs after main.js has applied its own messages */
      setTimeout(function () {
        var f = inp.closest('.fld'), e = f && f.querySelector('.err');
        if (!f) return;
        if (f.classList.contains('bad') && e) e.textContent = msg;
      }, 0);
    }
    draw();
    refBtn.addEventListener('click', function () { newCode(true); inp.focus(); });
    form.addEventListener('reset', function () { setTimeout(function () { newCode(true); }, 0); });
    /* capture phase: runs before the generic form handler in main.js */
    form.addEventListener('submit', function (e) {
      if (hp && hp.value) { e.preventDefault(); e.stopImmediatePropagation(); return; } /* bot caught by honeypot */
      var v = inp.value.trim().toUpperCase();
      if (v && v !== code) {
        inp.value = ''; newCode(false); /* empty value makes main.js flag every error together */
        fix('Wrong code. Please try the new one.');
      } else if (!v) { fix('Please type the code shown.'); }
    }, true);
  })();

  /* ---- valid enquiry: go straight to WhatsApp with the details pre-filled (no thank-you card) ---- */
  (function () {
    var form = document.getElementById('enqForm'), ok = document.getElementById('enqOk');
    if (!form || !ok) return;
    var num = (window.SITE && window.SITE.whatsapp) || '919766815782', go = false;
    /* bubble phase = after main.js validated; it adds .ld only when everything (incl. captcha) is valid */
    form.addEventListener('submit', function () {
      if (!form.classList.contains('ld')) return;
      var v = function (n) { return (form.elements[n] && form.elements[n].value || '').trim() || '-'; };
      var msg = 'New Enquiry (Website)\nName: ' + v('name') + '\nPhone: ' + v('phone') + '\nEmail: ' + v('email') + '\nSubject: ' + v('subject') + '\nMessage: ' + v('message');
      var u = 'https://wa.me/' + num + '?text=' + encodeURIComponent(msg);
      go = true; say('Opening WhatsApp\u2026');
      var w = window.open(u, '_blank'); if (!w) window.location.href = u;
    });
    /* main.js shows the thank-you card after its timer; undo it so the form stays ready */
    new MutationObserver(function () {
      if (!go || !ok.classList.contains('on')) return;
      go = false; ok.classList.remove('on'); form.style.display = '';
    }).observe(ok, { attributes: true, attributeFilter: ['class'] });
  })();
})();
