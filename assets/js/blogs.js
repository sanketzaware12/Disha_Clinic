/* Blogs page: scroll-triggered staggered card entrance, replay on filter/search, cursor spotlight */
(function () {
  var root = document.querySelector('[data-filter-root]');
  var grid = root && root.querySelector('.bl-grid');
  if (!grid) return;
  var cards = Array.prototype.slice.call(grid.querySelectorAll('.bl-card'));
  var calm = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

  function play(list) {
    list.forEach(function (c, i) {
      c.style.setProperty('--i', i);
      c.classList.remove('bl-in');
      c.classList.add('bl-pre');
      void c.offsetWidth;                         // restart animation
      c.classList.add('bl-in');
    });
  }
  grid.addEventListener('animationend', function (e) {
    if (e.animationName !== 'blIn') return;
    e.target.classList.remove('bl-pre', 'bl-in'); // hand control back to hover styles
    e.target.style.removeProperty('--i');
  });

  var io = null;
  function watch() {
    if (io) io.disconnect();
    var vis = cards.filter(function (c) { return !c.classList.contains('hidden'); });
    if (calm || !('IntersectionObserver' in window)) return;
    vis.forEach(function (c) { c.classList.remove('bl-in'); c.classList.add('bl-pre'); });
    io = new IntersectionObserver(function (entries) {
      var batch = entries.filter(function (e) { return e.isIntersecting; }).map(function (e) { io.unobserve(e.target); return e.target; });
      if (batch.length) play(batch);
    }, { threshold: 0.12 });
    vis.forEach(function (c) { io.observe(c); });
  }
  // main.js hides/shows cards first, then we replay the entrance
  function refresh() { setTimeout(watch, 0); }
  root.querySelectorAll('.chip').forEach(function (c) { c.addEventListener('click', refresh); });
  var q = root.querySelector('.search'); if (q) q.addEventListener('input', refresh);
  watch();

  /* cursor spotlight (mouse devices only) */
  if (window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
    cards.forEach(function (c) {
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        c.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }
})();
