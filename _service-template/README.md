# Service page template

Every service internal page uses the same layout. Only the content changes.

1. Copy `content/piles-haemorrhoid-surgery.json` to `content/<service-slug>.json`
2. Replace the text (headings, lists, tables, FAQs, images)
3. Run: `python3 _service-template/build.py <service-slug>`
   -> writes `services/<service-slug>/index.html`

Design lives in `assets/css/service-detail.css`, behaviour in `assets/js/service-detail.js`.
Reviews: add `{"name": "...", "text": "..."}` items to the `reviews` block when real Google reviews are available.
