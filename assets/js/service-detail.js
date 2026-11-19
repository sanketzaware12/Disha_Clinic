/* Service detail page behaviour: sticky-nav scrollspy, hero tilt, myth cards on touch. FAQ + counters + reveal come from main.js */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  // keep the page nav just under the sticky header
  var hdr = $('.hdr'), nav = $('.sd-nav');
  function setHH() { if (hdr && nav) document.documentElement.style.setProperty('--hh', hdr.offsetHeight + 'px'); }
  setHH(); addEventListener('resize', setHH); addEventListener('scroll', setHH, { passive: true });

  if (nav) {
    var links = $$('.sd-nav a'), inner = $('.sd-nav-in');
    var targets = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
    function spy() {
      var y = (hdr ? hdr.offsetHeight : 74) + nav.offsetHeight + 40, cur = -1;
      targets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top <= y) cur = i; });
      links.forEach(function (a, i) {
        var on = i === cur; a.classList.toggle('on', on);
        if (on && inner) { var l = a.offsetLeft - inner.clientWidth / 2 + a.offsetWidth / 2; inner.scrollTo({ left: l, behavior: 'smooth' }); }
      });
      nav.classList.toggle('stuck', nav.getBoundingClientRect().top <= (hdr ? hdr.offsetHeight : 74) + 1);
    }
    var tick = false;
    addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(function () { spy(); tick = false; }); } }, { passive: true });
    spy();
  }

  // myth cards: tap to flip on touch screens
  $$('.sd-myth').forEach(function (m) { m.setAttribute('tabindex', '0'); m.addEventListener('click', function () { m.classList.toggle('flip'); }); });

  // gentle 3D tilt on the doctor card (desktop only)
  var fine = matchMedia('(hover:hover) and (pointer:fine)').matches, calm = matchMedia('(prefers-reduced-motion:reduce)').matches;
  var card = $('.sd-hero-card');
  if (card && fine && !calm) {
    card.addEventListener('pointermove', function (e) {
      var r = card.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      card.style.setProperty('--ry', (x * 8).toFixed(2) + 'deg'); card.style.setProperty('--rx', (-y * 8).toFixed(2) + 'deg');
    });
    card.addEventListener('pointerleave', function () { card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg'); });
  }
})();

/* premium sections: cursor spotlight on cards + draw the journey track when it scrolls into view */
(function () {
  var $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };
  var fine = matchMedia('(hover:hover) and (pointer:fine)').matches;
  if (fine) {
    $$('#types .sd-card').forEach(function (c) {
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        c.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }
  var tl = $$('.sd-journey');
  if (tl.length) {
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('go'); io.unobserve(e.target); } });
      }, { threshold: .3 });
      tl.forEach(function (t) { io.observe(t); });
    } else tl.forEach(function (t) { t.classList.add('go'); });
  }
})();

/* comparison cards: soft cursor spotlight (desktop only) */
(function () {
  if (!matchMedia('(hover:hover) and (pointer:fine)').matches) return;
  Array.prototype.slice.call(document.querySelectorAll('.dx-card')).forEach(function (c) {
    c.addEventListener('pointermove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });
})();
