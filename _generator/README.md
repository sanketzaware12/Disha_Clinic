# DISHA Advanced Surgical & Laser Piles Clinic - Website Template
Static HTML/CSS/JS multipage site (no backend). Open `index.html` to preview.

## Structure
`index.html` Home · `about-us/` · `services/` (+8 detail pages) · `products/` (+4 detail pages) · `blogs/` (+3 articles) · `book-appointment/` · `contact-us/` · `privacy-policy/` · `terms-and-conditions/` · `404.html` · `sitemap.xml` · `robots.txt` · `assets/` (css, js, img)

## Change brand, numbers, content (one place)
All content lives in `_generator/content.py` (brand, phones, WhatsApp, email, address, map, hours, time slots, social links, services, products, blogs, legal text).
Edit it, then run `cd _generator && python build.py` - the full site is regenerated in `_generator/site/`.
Colours: variables at the top of `assets/css/style.css` (`--p`, `--pd`, `--a`).

## Add a service / product / blog
Add one entry to `SERVICES`, `PRODUCTS` or `BLOGS` in `content.py` and rebuild. Pages, menus, cards, sitemap and schema are created automatically.

## Images
Placeholders are SVG files in `assets/img/`. Replace with real images using the same names (e.g. `banner`/`hero-1`, `service-<name>`, `product-<name>`) and update the extension if you use JPG/WebP. Sizes: banner 1920x800, service 800x600, product 800x800, logo SVG/PNG.

## Going live
1. Set `base` (domain) and `link_index=False` in `content.py`, rebuild, upload `site/` contents to hosting (clean URLs like /about-us/).
2. Add Google Search Console verification and Analytics snippet (marked in `<head>`), submit `sitemap.xml`.
3. Connect booking / enquiry forms to a backend or form service: search `TODO` in `assets/js/main.js`.

## Dummy photos (replace before launch)
Hero, doctor, about, gallery, service and blog photos are stock placeholders (`assets/img/*.jpg`, sources in `_generator/src/assets/img`). Replace with the clinic's own photos using the same file names and rebuild. Product images are still illustrated placeholders.
