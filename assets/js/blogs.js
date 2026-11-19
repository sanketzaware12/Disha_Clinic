/* Blogs page: switch bento layout to a clean grid while filtering/searching */
(function () {
  var root = document.querySelector('[data-filter-root]');
  if (!root) return;
  var grid = root.querySelector('.bl-grid'),
      chips = root.querySelectorAll('.chip'),
      q = root.querySelector('.search');
  if (!grid) return;
  function sync() {
    var on = root.querySelector('.chip.on');
    var flat = (on && on.dataset.f !== 'all') || (q && q.value.trim() !== '');
    grid.classList.toggle('is-flat', !!flat);
  }
  chips.forEach(function (c) { c.addEventListener('click', sync); });
  if (q) q.addEventListener('input', sync);
})();
