/* Shared layout: top bar + header/menu, footer, floating WhatsApp/Call buttons.
   Content comes from assets/js/config.js (edit there, not in every page).
   Each page has two tags where its header / footer used to be:
     <script src="assets/js/config.js"></script>
     <script src="assets/js/layout.js" data-part="header" data-active="home"></script>
     ...
     <script src="assets/js/layout.js" data-part="footer"></script>
   data-active = home | about | services | products | blogs | contact (highlights the menu item). */
(function () {
  var cs = document.currentScript;
  if (!cs) return;
  var S = window.SITE || {};
  var root = (cs.getAttribute('src') || '').replace(/assets\/js\/layout\.js.*$/, '');
  var part = cs.getAttribute('data-part');
  var active = cs.getAttribute('data-active') || '';

  function esc(v) {
    return String(v == null ? '' : v).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  function u(p) { return root + p; }

  var ICO = function (d) { return '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true">' + d + '</svg>'; };
  var I = {
    clock: ICO('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    phone: ICO('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>'),
    mail: ICO('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>'),
    cal: ICO('<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>'),
    pin: ICO('<path d="M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>'),
    menu: ICO('<path d="M4 7h16M4 12h16M4 17h16"/>'),
    close: ICO('<path d="M6 6l12 12M18 6L6 18"/>'),
    wa: ICO('<path d="M3 21l1.6-4.8A9 9 0 1112 21a9 9 0 01-4.2-1z"/><path d="M9 9c0 3 3 6 6 6l1-2-2-1-1 .8c-.8-.4-1.6-1.2-2-2L11.8 10l-1-2z"/>')
  };

  function social() {
    return (S.social || []).map(function (s) {
      return '<a href="' + esc(s.url) + '" aria-label="' + esc(s.label) + '" target="_blank" rel="noopener">' + esc(s.letter) + '</a>';
    }).join('');
  }
  function logo(extraImgClass) {
    return '<a class="logo" href="' + u('index.html') + '"' + (extraImgClass ? '' : ' aria-label="' + esc(S.name) + ' home"') + '>' +
      '<img ' + (extraImgClass ? 'class="' + extraImgClass + '" ' : '') + 'src="' + u('assets/img/emblem.png') + '" alt="' + esc(S.name) + ' logo" width="52" height="48">' +
      '<span class="lt"><b>' + esc(S.short) + '</b><small>' + esc(S.subtitle) + '</small></span></a>';
  }
  function on(key) { return active === key ? ' class="on"' : ''; }
  function link(key, path, label) { return '<a href="' + u(path) + '"' + on(key) + '>' + label + '</a>'; }

  function header() {
    var menu = (S.menuServices || []);
    var ddCls = menu.length ? 'dd-m dd-one' : 'dd-m';
    var groups = menu.length
      ? '<div class="dg">' + menu.map(function (it) {
          return '<a href="' + u('services/' + it.slug + '/index.html') + '">' + esc(it.label) + '</a>';
        }).join('') + '</div>'
      : (S.serviceGroups || []).map(function (g) {
          return '<div class="dg"><h5>' + esc(g.title) + '</h5>' + g.items.map(function (it) {
            return '<a href="' + u('services/' + it.slug + '/index.html') + '">' + esc(it.label) + '</a>';
          }).join('') + '</div>';
        }).join('');
    var waHref = 'https://wa.me/' + esc(S.whatsapp) + '?text=' + encodeURIComponent(S.waText || '');
    var tel = 'tel:' + esc(S.phone);
    return '<div class="top"><div class="container"><div class="l"><span>' + I.clock + esc(S.hours) + '</span><span>' + I.phone + 'Call / WhatsApp: <a href="' + tel + '">' + esc(S.phoneDisplay) + '</a></span></div>' +
      '<div class="r"><a href="mailto:' + esc(S.email) + '">' + I.mail + esc(S.email) + '</a><div class="soc">' + social() + '</div></div></div></div>\n' +
      '<header class="hdr"><div class="container">' + logo() + '\n' +
      '<nav class="nav" id="mainnav" aria-label="Main">' +
      link('home', 'index.html', 'Home') +
      '<div class="dd">' + link('services', 'services/index.html', 'Services \u25be') + '<div class="' + ddCls + '">' + groups + '</div></div>' +
      /* PRODUCTS (hidden for now): link('products', 'products/index.html', 'Products') + */ link('blogs', 'blogs/index.html', 'Blog') + link('about', 'about-us/index.html', 'About Us') + link('contact', 'contact-us/index.html', 'Contact Us') +
      '<div class="nav-cta"><a class="btn btn-a btn-sm" href="' + tel + '">' + I.phone + ' Call Now</a><a class="btn btn-p btn-sm" href="' + waHref + '" target="_blank" rel="noopener">' + I.wa + ' WhatsApp Chat</a></div></nav>\n' +
      '<div class="hcta"><a class="btn btn-a btn-sm" href="' + tel + '">' + I.phone + ' Call Now</a><a class="btn btn-p btn-sm pulse" href="' + waHref + '" target="_blank" rel="noopener">' + I.wa + ' WhatsApp Chat</a>' +
      '<button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mainnav"><span class="b-o">' + I.menu + '</span><span class="b-c">' + I.close + '</span></button></div></div></header>' +
      '<div class="nav-ov" aria-hidden="true"></div>\n';
  }

  function footer() {
    var label = {};
    (S.serviceGroups || []).forEach(function (g) { g.items.forEach(function (it) { label[it.slug] = it.label; }); });
    var fsvc = (S.footerServices || []).map(function (slug) {
      return '<li><a href="' + u('services/' + slug + '/index.html') + '">' + esc(label[slug] || slug) + '</a></li>';
    }).join('');
    var tel = 'tel:' + esc(S.phone);
    return '<footer class="ft"><div class="container"><div class="grid">\n' +
      '<div class="f-brand">' + logo('ew') + '<p>' + esc(S.about) + '</p><div class="soc" style="margin-top:14px">' + social() + '</div></div>\n' +
      '<div class="f-links"><h4>Quick Links</h4><ul>' +
      '<li><a href="' + u('about-us/index.html') + '">About Us</a></li><li><a href="' + u('services/index.html') + '">Services</a></li>' +
      /* PRODUCTS (hidden for now): '<li><a href="' + u('products/index.html') + '">Products</a></li>' + */
      '<li><a href="' + u('blogs/index.html') + '">Blogs</a></li>' +
      '<li><a href="' + u('book-appointment/index.html') + '">Book Appointment</a></li><li><a href="' + u('contact-us/index.html') + '">Contact Us</a></li></ul></div>\n' +
      '<div class="f-svc"><h4>Our Services</h4><ul>' + fsvc + '</ul></div>\n' +
      '<div class="f-contact"><h4>Contact</h4><ul><li>' + I.pin + ' ' + esc(S.address) + '</li>' +
      '<li>' + I.phone + ' <a href="' + tel + '">' + esc(S.phoneDisplay) + '</a></li>' +
      '<li>' + I.mail + ' <a href="mailto:' + esc(S.email) + '">' + esc(S.email) + '</a></li>' +
      '<li>' + I.clock + ' ' + esc(S.hours) + '</li><li>' + esc(S.callAhead) + '</li></ul></div></div>\n' +
      '<div class="bot"><span>\u00a9 ' + esc(S.year) + ' ' + esc(S.name) + '. All rights reserved.</span><div>' +
      '<a href="' + u('privacy-policy/index.html') + '">Privacy Policy</a><a href="' + u('terms-and-conditions/index.html') + '">Terms &amp; Conditions</a></div></div></div></footer>\n' +
      '<div class="fl"><a class="wa" href="https://wa.me/' + esc(S.whatsapp) + '?text=' + encodeURIComponent(S.waText || '') + '" target="_blank" rel="noopener" aria-label="WhatsApp enquiry">' + I.wa + '</a>' +
      '<a class="cl" href="' + tel + '" aria-label="Call now">' + I.phone + '</a></div>\n';
  }

  var html = part === 'header' ? header() : part === 'footer' ? footer() : '';
  if (html) cs.insertAdjacentHTML('beforebegin', html);
})();
