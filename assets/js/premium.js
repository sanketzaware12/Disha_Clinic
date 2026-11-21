/* Patient reviews: centre-focus looping slider (arrows, dots, drag/swipe, keys) */
(function () {
  var box = document.querySelector('[data-rv]'); if (!box) return;
  var track = box.querySelector('.rv-track'), cards = Array.prototype.slice.call(track.children), n = cards.length;
  var prev = box.querySelector('.prev'), next = box.querySelector('.next'), dotsEl = box.querySelector('.rv-dots'), cur = 0, dots = [];
  cards.forEach(function (c, i) { c.addEventListener('click', function () { if (c.classList.contains('is-l')) go(cur - 1); else if (c.classList.contains('is-r')) go(cur + 1); }); });
  for (var d = 0; d < n; d++) (function (d) { var b = document.createElement('button'); b.type = 'button'; b.setAttribute('aria-label', 'Show review ' + (d + 1)); b.addEventListener('click', function () { go(d); }); dotsEl.appendChild(b); dots.push(b); })(d);
  function render() {
    cards.forEach(function (c, i) {
      var o = ((i - cur) % n + n) % n; if (o > n / 2) o -= n;
      c.className = 'card rv ' + (o === 0 ? 'is-c' : o === -1 ? 'is-l' : o === 1 ? 'is-r' : o < 0 ? 'is-hl' : 'is-hr');
      c.setAttribute('aria-hidden', o === 0 ? 'false' : 'true');
    });
    dots.forEach(function (b, i) { b.classList.toggle('on', i === cur); });
  }
  function go(i) { cur = ((i % n) + n) % n; render(); }
  function height() { var m = 0; cards.forEach(function (c) { m = Math.max(m, c.scrollHeight); }); box.style.setProperty('--rvh', (m + 24) + 'px'); }
  prev.addEventListener('click', function () { go(cur - 1); }); next.addEventListener('click', function () { go(cur + 1); });
  track.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') { e.preventDefault(); go(cur + 1); } if (e.key === 'ArrowLeft') { e.preventDefault(); go(cur - 1); } });
  var sx = null, moved = false;
  track.addEventListener('pointerdown', function (e) { sx = e.clientX; moved = false; });
  window.addEventListener('pointermove', function (e) { if (sx === null) return; if (Math.abs(e.clientX - sx) > 6) { moved = true; track.classList.add('drag'); } });
  window.addEventListener('pointerup', function (e) { if (sx === null) return; var dx = e.clientX - sx; sx = null; track.classList.remove('drag'); if (moved && Math.abs(dx) > 40) go(cur + (dx < 0 ? 1 : -1)); });
  track.addEventListener('click', function (e) { if (moved) { e.stopImmediatePropagation(); e.preventDefault(); moved = false; } }, true);
  window.addEventListener('resize', height); window.addEventListener('load', height);
  render(); height();
})();

/* Homepage-only micro interactions (tilt, spotlight, hero parallax). Safe to delete. */
(function () {
  var fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  var calm = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  if (!fine || calm) return;
  var $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };

  // spotlight that follows the mouse on speciality cards
  $$('.card:has(>.im)').forEach(function (c) {
    c.addEventListener('pointermove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  // gentle 3D tilt (hero illustration card, surgeon photo)
  function tilt(el, max) {
    el.addEventListener('pointermove', function (e) {
      var r = el.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      el.style.setProperty('--ry', (x * max).toFixed(2) + 'deg');
      el.style.setProperty('--rx', (-y * max).toFixed(2) + 'deg');
    });
    el.addEventListener('pointerleave', function () { el.style.setProperty('--rx', '0deg'); el.style.setProperty('--ry', '0deg'); });
  }
  var art = document.querySelector('.hero-art');
  if (art) {
    var card = art.querySelector('.ha-card');
    art.addEventListener('pointermove', function (e) {
      var r = art.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      card.style.setProperty('--ry', (x * 9).toFixed(2) + 'deg'); card.style.setProperty('--rx', (-y * 9).toFixed(2) + 'deg');
    });
    art.addEventListener('pointerleave', function () { card.style.setProperty('--rx', '0deg'); card.style.setProperty('--ry', '0deg'); });
  }
  $$('.docpic').forEach(function (e) { tilt(e, 7); });

  // hero: floating chips drift with the mouse
  var hero = document.querySelector('.hero-one');
  if (hero && art) {
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      art.style.setProperty('--px', ((e.clientX - r.left) / r.width - .5).toFixed(3));
      art.style.setProperty('--py', ((e.clientY - r.top) / r.height - .5).toFixed(3));
    });
  }
})();

/* Credentials: soft 3D tilt that follows the pointer (desktop only) */
(function(){var c=document.querySelector('.cred');if(!c||!window.matchMedia('(hover:hover) and (min-width:1021px)').matches||window.matchMedia('(prefers-reduced-motion:reduce)').matches)return;var f=c.querySelector('.credf');
c.addEventListener('mousemove',function(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;f.style.transform='rotateY('+(x*7)+'deg) rotateX('+(-y*6)+'deg) translateY(-6px)'});
c.addEventListener('mouseleave',function(){f.style.transform=''});})();
