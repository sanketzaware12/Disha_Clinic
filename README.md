# DISHA Advanced Surgical & Laser Piles Clinic - Website
Pure static HTML / CSS / JavaScript multipage site. No backend, no build step, no installs.
Open `index.html` in a browser (or upload the folder to any hosting) - that's all.

## What lives where
| What | Where |
|---|---|
| Clinic name, phone, WhatsApp, email, address, timings, social links, footer text | `assets/js/config.js` |
| Services menu (header dropdown) + services listed in the footer | `assets/js/config.js` (`serviceGroups`, `footerServices`) |
| Booking time slots, closed days | `assets/js/config.js` |
| Top bar, header + menu, footer, floating WhatsApp/Call buttons | rendered by `assets/js/layout.js` from `config.js` (edit once, all 49 pages update) |
| Colours, spacing, animations | `assets/css/style.css` (variables at the top: `--p`, `--pd`, `--a`) |
| Menu / sliders / forms / animations behaviour | `assets/js/main.js` |
| Page text, headings, FAQs, images | that page's own `index.html` |

## Add a new service
1. Copy an existing folder, e.g. `services/fistula-treatment/` -> `services/my-new-service/`, edit its `index.html` (title, description, canonical URL, text, image `assets/img/service-my-new-service.jpg`).
2. Add one line in `assets/js/config.js` -> `serviceGroups` (slug = folder name). The header menu updates on every page. Optionally add the slug to `footerServices`.
3. Add its card in `services/index.html` (copy a neighbouring card) and a `<url>` entry in `sitemap.xml`.

## Add a new blog / product
Copy an existing folder inside `blogs/` or `products/`, edit its `index.html`, add its card in that section's `index.html` and a `<url>` in `sitemap.xml`. (Blogs and products are not in the header menu, so `config.js` needs no change.)

## One-time Find & Replace before going live (VS Code: Ctrl+Shift+H, search whole folder)
These appear inside page text, FAQ answers, CTA buttons and SEO schema, so they are not driven by `config.js`:
| Search for | Replace with |
|---|---|
| `919766815782` (WhatsApp / tel links) | real number, digits only |
| `+91 97668 15782` (text shown on pages) | real number as displayed |
| `info@dishaclinic.example` | real email |
| `dishaclinic.example` (canonical, schema, sitemap, robots) | real domain |
| `10:00 AM – 9:00 PM` / `10:00 AM to 9:00 PM` | real timings |
Then update the same values in `assets/js/config.js`.

## Images
Replace files in `assets/img/` using the same file names (`hero-1`, `service-<name>`, `product-<name>`, `blog-<name>`, ...). Sizes: banner 1920x800, service 800x600, product 800x800, logo SVG/PNG. Hero, doctor, about, gallery, service and blog photos are stock placeholders; product images are illustrated placeholders.

## Going live
1. Do the Find & Replace above.
2. Add Google Search Console verification and Analytics snippet in `<head>` (marked `[REPLACE]`), submit `sitemap.xml`.
3. Connect booking / enquiry forms to a backend or form service: search `TODO` in `assets/js/main.js`.

## Service internal pages (static HTML)

All service pages use the same layout as `services/piles-haemorrhoid-surgery/index.html`
(hero, stats, on-page nav, then the same sections in the same order). The design lives in
`assets/css/service-detail.css`, the behaviour in `assets/js/service-detail.js`.
To edit a service, open its `services/<slug>/index.html` and change only the text.
Pages done in this template: piles, fissure, fistula, pilonidal sinus, hernia, gallbladder stone, appendix.
The project contains only HTML, CSS and JavaScript (no Python).

## Blog internal pages (static HTML)

All 6 blog articles share one premium template: hero, numbered content sections, sticky table of contents with scroll-spy,
doctor/booking card, related posts with thumbnails, share + author box and a closing CTA band.
The design lives in `assets/css/blog-detail.css`, the behaviour (scroll reveal, TOC highlight, hover spotlight) in `assets/js/blog-detail.js`.
To add a new blog, copy an existing `blogs/<slug>/index.html` and change only the text. Wrap each topic as
`<section class="bd-s bd-rv" id="..."><h2>...</h2>...</section>`; add class `bd-alert` for a red emergency callout.
