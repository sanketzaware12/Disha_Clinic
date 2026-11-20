/* Blog detail page: scroll reveal, TOC scroll-spy (+ smooth jump), cursor spotlight on side boxes */
(function () {
  var calm = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

  /* ---- scroll reveal ---- */
  var rv = Array.prototype.slice.call(document.querySelectorAll('.bd-rv'));
  if (rv.length) {
    if (calm || !('IntersectionObserver' in window)) {
      rv.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('in');
          io.unobserve(e.target);
        });
      }, { threshold: 0.01, rootMargin: '0px 0px -40px 0px' });
      rv.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---- TOC scroll-spy ---- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.bd-toc a[href^="#"]'));
  var secs = links.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
  if (links.length && 'IntersectionObserver' in window) {
    var cur = -1;
    function mark(i) {
      if (i === cur || i < 0) return;
      cur = i;
      links.forEach(function (a, k) { a.classList.toggle('on', k === i); });
      var nav = links[i].parentNode;                      // keep active link visible inside the TOC
      if (nav.scrollHeight > nav.clientHeight) {
        nav.scrollTo({ top: links[i].offsetTop - nav.clientHeight / 2, behavior: calm ? 'auto' : 'smooth' });
      }
    }
    function spy() {
      var y = window.innerHeight * 0.28, idx = 0;
      secs.forEach(function (s, k) { if (s && s.getBoundingClientRect().top <= y) idx = k; });
      mark(idx);
    }
    var tick = false;
    window.addEventListener('scroll', function () {
      if (tick) return; tick = true;
      requestAnimationFrame(function () { tick = false; spy(); });
    }, { passive: true });
    spy();
  }

  /* ---- cursor spotlight (mouse devices only) ---- */
  if (window.matchMedia('(hover:hover) and (pointer:fine)').matches) {
    document.querySelectorAll('.bd-box').forEach(function (b) {
      b.addEventListener('pointermove', function (e) {
        var r = b.getBoundingClientRect();
        b.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        b.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }
})();
