/* Homepage-only micro interactions (tilt, spotlight, hero parallax). Safe to delete. */
(function () {
  var fine = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  var calm = window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  if (!fine || calm) return;
  var $$ = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };

  // spotlight that follows the mouse on speciality cards
  $$('.spec .card').forEach(function (c) {
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
