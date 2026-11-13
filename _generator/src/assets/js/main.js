/* Main site script. Settings come from assets/js/config.js (generated from content.py) */
(function () {
  const $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const S = window.SITE || {};
  addEventListener('load', () => setTimeout(() => { const p = $('.pre'); p && p.classList.add('hide'); }, 300));

  // progress bar, sticky header, back to top
  const pb = $('.pbar'), hd = $('.hdr'), tp = $('.totop');
  function sc() {
    const y = scrollY, h = document.documentElement.scrollHeight - innerHeight;
    pb.style.width = (h > 0 ? y / h * 100 : 0) + '%';
    hd.classList.toggle('sm', y > 40); tp.classList.toggle('show', y > 500);
  }
  addEventListener('scroll', sc, { passive: true }); sc();
  tp.onclick = () => scrollTo({ top: 0, behavior: 'smooth' });

  // mobile menu + dropdown
  $('.burger').onclick = () => document.body.classList.toggle('menu-open');
  $$('.dd > a').forEach(a => a.addEventListener('click', e => { if (innerWidth < 1021) { e.preventDefault(); a.parentElement.classList.toggle('open'); } }));

  // scroll reveal + counters
  function count(el) {
    const end = +el.dataset.count, suf = el.dataset.suf || '', t0 = performance.now(), d = 1600;
    (function f(t) { const k = Math.min((t - t0) / d, 1), e = 1 - Math.pow(1 - k, 3); el.textContent = Math.round(end * e).toLocaleString('en-IN') + suf; if (k < 1) requestAnimationFrame(f); })(t0);
  }
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); if (e.target.dataset.count) count(e.target); }
  }), { threshold: .12 });
  $$('.reveal,[data-count]').forEach(el => io.observe(el));

  // hero slider
  const hero = $('.hero');
  if (hero) {
    const ss = $$('.slide', hero), ds = $$('.dot', hero); let i = 0, t;
    const go = n => { i = (n + ss.length) % ss.length; ss.forEach((s, k) => s.classList.toggle('on', k === i)); ds.forEach((d, k) => d.classList.toggle('on', k === i)); };
    const st = () => { clearInterval(t); t = setInterval(() => go(i + 1), 5500); };
    $('.prev', hero).onclick = () => { go(i - 1); st(); }; $('.next', hero).onclick = () => { go(i + 1); st(); };
    ds.forEach((d, k) => d.onclick = () => { go(k); st(); });
    hero.onmouseenter = () => clearInterval(t); hero.onmouseleave = st;
    let x0 = 0; hero.addEventListener('touchstart', e => x0 = e.touches[0].clientX, { passive: true });
    hero.addEventListener('touchend', e => { const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) { go(i + (dx < 0 ? 1 : -1)); st(); } });
    st();
  }

  // testimonials slider
  const ts = $$('.tt');
  if (ts.length) {
    const td = $$('.tdots button'); let k = 0, tm;
    const sh = n => { k = (n + ts.length) % ts.length; ts.forEach((e, j) => e.classList.toggle('on', j === k)); td.forEach((e, j) => e.classList.toggle('on', j === k)); };
    td.forEach((b, j) => b.onclick = () => { sh(j); clearInterval(tm); tm = setInterval(() => sh(k + 1), 6000); });
    tm = setInterval(() => sh(k + 1), 6000);
  }

  // accordion
  $$('.acc-q').forEach(q => q.onclick = () => { const a = q.parentElement, o = a.classList.toggle('open'); q.setAttribute('aria-expanded', o); });

  // blog / service filter + search
  const fl = $('[data-filter-root]');
  if (fl) {
    const items = $$('[data-cat]', fl), chips = $$('.chip', fl), q = $('.search', fl); let cat = 'all';
    const run = () => {
      const s = (q ? q.value : '').toLowerCase().trim(); let n = 0;
      items.forEach(it => { const ok = (cat === 'all' || it.dataset.cat === cat) && it.textContent.toLowerCase().includes(s); it.classList.toggle('hidden', !ok); if (ok) n++; });
      $('.empty', fl).classList.toggle('hidden', n > 0);
    };
    chips.forEach(c => c.onclick = () => { chips.forEach(x => x.classList.remove('on')); c.classList.add('on'); cat = c.dataset.f; run(); });
    q && q.addEventListener('input', run);
  }

  // lightbox
  const lb = $('.lb');
  $$('[data-lb]').forEach(a => a.onclick = () => { $('img', lb).src = a.dataset.lb; lb.classList.add('on'); });
  lb.onclick = () => lb.classList.remove('on');

  // validation helpers
  const setErr = (el, m) => { const f = el.closest('.fld') || el.closest('.chk') || el.parentElement; f.classList.toggle('bad', !!m); const e = f.querySelector('.err'); if (e) e.textContent = m || ''; };
  const validate = form => {
    let ok = true;
    $$('[required]', form).forEach(el => {
      let m = '';
      if (el.type === 'checkbox') { if (!el.checked) m = 'Please accept to continue.'; }
      else if (!el.value.trim()) m = 'This field is required.';
      else if (el.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value)) m = 'Enter a valid email address.';
      else if (el.type === 'tel' && !/^[+]?[0-9\s-]{10,14}$/.test(el.value)) m = 'Enter a valid phone number.';
      setErr(el, m); if (m) ok = false;
    });
    return ok;
  };
  $$('input,select,textarea').forEach(el => el.addEventListener('input', () => setErr(el, '')));

  // enquiry form
  const ef = $('#enqForm');
  if (ef) ef.addEventListener('submit', e => {
    e.preventDefault(); if (!validate(ef)) return;
    const b = $('button[type=submit]', ef); b.textContent = 'Sending…'; ef.classList.add('ld');
    // TODO: connect your backend / form service here (fetch POST) before going live
    setTimeout(() => { ef.classList.remove('ld'); b.textContent = 'Send Message'; ef.reset(); $('#enqOk').classList.add('on'); ef.style.display = 'none'; }, 900);
  });

  // booking form
  const bf = $('#bookForm');
  if (bf) {
    const di = $('#bdate'), box = $('#slots'), hid = $('#bslot'), now = new Date(), pad = n => String(n).padStart(2, '0');
    di.min = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`;
    const render = () => {
      box.innerHTML = ''; hid.value = '';
      if (!di.value) { box.innerHTML = '<p class="hint">Select a date to view available time slots.</p>'; return; }
      const d = new Date(di.value + 'T00:00');
      if ((S.closedDays || []).includes(d.getDay())) { box.innerHTML = '<p class="hint">OPD is closed on this day (emergency care is available 24×7). Please choose another date.</p>'; return; }
      const seed = d.getDate() + d.getMonth();
      (S.slots || []).forEach((s, k) => {
        const b = document.createElement('button'); b.type = 'button'; b.className = 'slot'; b.textContent = s;
        let off = (seed + k) % 5 === 0; // demo: some slots shown as booked
        if (d.toDateString() === now.toDateString()) {
          const [m, ap] = s.split(' '); let [h, mi] = m.split(':').map(Number);
          if (ap === 'PM' && h < 12) h += 12; if (ap === 'AM' && h === 12) h = 0;
          const sd = new Date(d); sd.setHours(h, mi); if (sd <= now) off = true;
        }
        b.disabled = off;
        b.onclick = () => { $$('.slot', box).forEach(x => x.classList.remove('sel')); b.classList.add('sel'); hid.value = s; setErr(hid, ''); };
        box.appendChild(b);
      });
    };
    di.addEventListener('change', render); render();
    bf.addEventListener('submit', e => {
      e.preventDefault(); let ok = validate(bf);
      if (!hid.value) { setErr(hid, 'Please choose a date and time slot.'); ok = false; }
      if (!ok) { const f = $('.bad', bf); f && f.scrollIntoView({ behavior: 'smooth', block: 'center' }); return; }
      const v = n => bf.elements[n].value, btn = $('button[type=submit]', bf); btn.textContent = 'Booking…'; bf.classList.add('ld');
      const msg = `Appointment Request%0AName: ${v('name')}%0APhone: ${v('phone')}%0AService: ${v('service')}%0ADoctor: ${v('doctor')}%0ADate: ${v('date')}%0ATime: ${v('slot')}%0ANote: ${v('message') || '-'}`;
      // TODO: connect backend / API here to store the appointment before going live
      setTimeout(() => {
        bf.classList.remove('ld'); bf.style.display = 'none';
        $('#okSum').textContent = `${v('service')} on ${v('date')} at ${v('slot')}`;
        $('#okWa').href = `https://wa.me/${S.whatsapp}?text=${msg}`;
        $('#okMail').href = `mailto:${S.email}?subject=Appointment Request&body=${msg.replace(/%0A/g, '%0D%0A')}`;
        $('#bookOk').classList.add('on'); $('#bookOk').scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 1000);
    });
  }
})();
