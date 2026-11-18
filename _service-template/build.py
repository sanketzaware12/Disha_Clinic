#!/usr/bin/env python3
"""
Service page generator for Disha Clinic.
Usage:   python3 _service-template/build.py piles-haemorrhoid-surgery
         python3 _service-template/build.py --all
Reads    _service-template/content/<slug>.json
Writes   services/<slug>/index.html
The layout is identical for every service. Only the JSON content changes.
"""
import json, sys, html, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "_service-template" / "content"
PHONE, PHONE_D, WA = "+919766815782", "+91 97668 15782", "919766815782"
SITE = "https://www.dishaclinic.example"
CLINIC = "DISHA Advanced Surgical & Laser Piles Clinic"
ADDR = "1st Floor, OPD No. 2, Survey No. 22/2, Ganga Altus, F Building, Cherry Life, Near Manipal Hospital, Thite Nagar, Kharadi, Pune 411014"
HOURS = "Daily: 10:00 AM – 9:00 PM"
e = lambda s: html.escape(str(s), quote=True)

P = {
 "check": '<path d="M5 13l4 4L19 7"/>',
 "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 01-12 0c0-4.5 6-11 6-11z"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
 "alert": '<path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.5"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "home": '<path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-6h4v6"/>',
 "leaf": '<path d="M5 19c0-9 5-14 15-14 0 10-5 15-14 15"/><path d="M5 19c3-5 6-8 10-10"/>',
 "timer": '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2 2M9 2h6"/>',
 "walk": '<circle cx="13" cy="4.5" r="2"/><path d="M12 8l-3 4 3 3-1 6M12 8l3 3 3 1M9 12l-3 1"/>',
 "heart": '<path d="M12 20s-8-5-8-11a4.5 4.5 0 018-2.5A4.5 4.5 0 0120 9c0 6-8 11-8 11z"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>',
 "wa": '<path d="M3 21l1.6-4.8A9 9 0 1112 21a9 9 0 01-4.2-1z"/><path d="M9 9c0 3 3 6 6 6l1-2-2-1-1 .8c-.8-.4-1.6-1.2-2-2L11.8 10l-1-2z"/>',
 "pin": '<path d="M12 21s7-6 7-12a7 7 0 00-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5L15.5 10"/>',
 "plus": '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
 "zoom": '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/>',
}
def ic(n, c=""):
    return f'<svg class="ico {c}" viewBox="0 0 24 24" aria-hidden="true">{P[n]}</svg>'

def delay(i, step=.07): return f' style="--d:{min(i*step,.5):.2f}s"'
def lis(items, icon="check"):
    return "".join(f'<li>{ic(icon)}<span>{e(x)}</span></li>' for x in items)
def head(b, center=True, dark=False):
    s = f'<div class="sd-head{" left" if not center else ""} reveal"><span class="eyebrow">{e(b["eyebrow"])}</span><h2>{e(b["h2"])}</h2>'
    if b.get("intro"): s += f'<p>{e(b["intro"])}</p>'
    return s + '</div>'
def sec(b, inner, extra=""):
    return f'<section class="sd-sec sd-{b["tone"]} {extra}" id="{b["id"]}"><span class="sd-orb o1"></span><span class="sd-orb o2"></span><div class="container">{inner}</div></section>'
def table(headrow, rows, cls=""):
    th = "".join(f'<th>{e(h)}</th>' for h in headrow)
    tr = "".join("<tr>" + "".join(f'<td data-l="{e(headrow[j])}">{e(c)}</td>' for j, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="sd-table reveal {cls}"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

R = {}
def kind(f): R[f.__name__[2:]] = f; return f

@kind
def r_overview(b, d):
    mini = "".join(f'<div class="sd-mini"><b>{e(m["t"])}</b><p>{e(m["d"])}</p></div>' for m in b["mini"])
    paras = "".join(f'<p>{e(p)}</p>' for p in b["paras"])
    gr = "".join(f'<div class="sd-grade g{i+1}"><span title="{e(g["g"])}">{e(g["g"]).split()[-1]}</span><p><b>{e(g["g"])}:</b> {e(g["d"])}</p></div>' for i, g in enumerate(b["grades"]))
    inner = f'''<div class="sd-two">
<div class="reveal">{head(b, False).replace(" reveal","",1)}{paras}<div class="sd-minis">{mini}</div></div>
<aside class="sd-gradebox reveal" style="--d:.12s"><h3>{e(b["grades_title"])}</h3><div class="sd-grades">{gr}</div></aside></div>'''
    return sec(b, inner)

@kind
def r_cards(b, d):
    cols = b.get("cols", 4)
    cards = "".join(f'<article class="sd-card reveal"{delay(i)}><span class="sd-ico">{ic(x["i"])}</span><h3>{e(x["t"])}</h3><p>{e(x["d"])}</p></article>' for i, x in enumerate(b["items"]))
    return sec(b, head(b) + f'<div class="sd-grid c{cols}">{cards}</div>')

@kind
def r_symptoms(b, d):
    cols = "".join(f'<div class="sd-col reveal"{delay(i)}><h3><span class="sd-ico sm">{ic(c["icon"])}</span>{e(c["t"])}</h3><ul class="sd-tick">{lis(c["items"], "check" if i==0 else "arrow")}</ul></div>' for i, c in enumerate(b["cols"]))
    warn = f'<div class="sd-warn reveal">{ic("alert")}<p>{e(b["warn"])}</p></div>' if b.get("warn") else ""
    return sec(b, head(b) + f'<div class="sd-grid c3">{cols}</div>{warn}')

@kind
def r_table(b, d):
    return sec(b, head(b) + table(b["head"], b["rows"], "cmp"))

@kind
def r_causes(b, d):
    paras = "".join(f'<p>{e(p)}</p>' for p in b["paras"])
    chips = "".join(f'<span class="sd-chip reveal"{delay(i,.04)}>{e(c)}</span>' for i, c in enumerate(b["chips"]))
    return sec(b, f'<div class="sd-two"><div class="reveal">{head(b, False).replace(" reveal","",1)}{paras}</div><div class="sd-chips">{chips}</div></div>')

@kind
def r_steps(b, d):
    st = "".join(f'<li class="reveal"{delay(i,.1)}><span class="n">{i+1}</span><h3>{e(x["t"])}</h3><p>{e(x["d"])}</p></li>' for i, x in enumerate(b["items"]))
    note = f'<p class="sd-note reveal">{ic("info")}{e(b["note"])}</p>' if b.get("note") else ""
    return sec(b, head(b) + f'<ol class="sd-steps">{st}</ol>{note}')

@kind
def r_gradetable(b, d):
    return sec(b, head(b) + table(b["head"], b["rows"], "grade"))

@kind
def r_split(b, d):
    groups = "".join(f'<div class="sd-group reveal"{delay(i)}><h3>{e(g["t"])}</h3><ul class="sd-tick">{lis(g["items"])}</ul></div>' for i, g in enumerate(b["groups"]))
    inner = f'''{head(b)}<div class="sd-split"><div class="sd-groups">{groups}</div>
<figure class="sd-fig reveal" style="--d:.15s"><img src="../../{e(b["img"])}" alt="{e(b["img_alt"])}" loading="lazy"><figcaption>{e(b["cap"])}</figcaption></figure></div>'''
    return sec(b, inner)

@kind
def r_foods(b, d):
    inner = f'''{head(b)}<div class="sd-grid c2"><div class="sd-food yes reveal"><h3>{ic("check")} {e(b["more_t"])}</h3><ul class="sd-tick">{lis(b["more"])}</ul></div>
<div class="sd-food no reveal" style="--d:.1s"><h3>{ic("alert")} {e(b["less_t"])}</h3><ul class="sd-tick">{lis(b["less"],"arrow")}</ul></div></div>
<p class="sd-note reveal">{ic("info")}{e(b["note"])}</p>'''
    return sec(b, inner)

@kind
def r_surgery(b, d):
    inner = f'''<div class="sd-surg"><figure class="sd-fig tall reveal"><img src="../../{e(b["img"])}" alt="{e(b["img_alt"])}" loading="lazy"><figcaption>{e(b["cap"])}</figcaption></figure>
<div>{head(b, False)}{table(b["head"], b["rows"], "surg")}</div></div>'''
    return sec(b, inner)

@kind
def r_laser(b, d):
    paras = "".join(f'<p>{e(p)}</p>' for p in b["paras"])
    inner = f'''<div class="sd-laser"><div class="reveal">{head(b, False).replace(" reveal","",1)}{paras}</div>
<div class="sd-stack"><div class="sd-box light reveal"><h3><span class="sd-ico sm">{ic("check")}</span>{e(b["good_t"])}</h3><ul class="sd-tick">{lis(b["good"])}</ul></div>
<div class="sd-box glass reveal" style="--d:.12s"><h3><span class="sd-ico sm">{ic("info")}</span>{e(b["note_t"])}</h3><ul class="sd-tick">{lis(b["note"],"arrow")}</ul></div></div></div>'''
    return sec(b, inner)

@kind
def r_tiers(b, d):
    t = "".join(f'<div class="sd-tier reveal"{delay(i,.1)}><h3><span class="sd-ico sm">{ic(x["icon"])}</span>{e(x["t"])}</h3><ul class="sd-tick">{lis(x["items"])}</ul></div>' for i, x in enumerate(b["tiers"]))
    return sec(b, head(b) + f'<div class="sd-grid c3">{t}</div>')

@kind
def r_journey(b, d):
    it = "".join(f'<li class="reveal"{delay(i,.1)}><span class="dot">{i+1}</span><h3>{e(x["t"])}</h3><p>{e(x["d"])}</p></li>' for i, x in enumerate(b["items"]))
    return sec(b, head(b) + f'<ol class="sd-journey">{it}</ol>')

@kind
def r_recovery(b, d):
    paras = "".join(f'<p>{e(p)}</p>' for p in b["paras"])
    inner = f'''{head(b)}<p class="sd-lead reveal">{paras.replace("<p>","").replace("</p>","")}</p>
<figure class="sd-banner reveal"><img src="../../{e(b["img"])}" alt="{e(b["img_alt"])}" loading="lazy"></figure>
<div class="sd-grid c2 recov"><div class="sd-box reveal"><h3>{e(b["help_t"])}</h3><ul class="sd-tick">{lis(b["help"])}</ul></div>
<div class="sd-box urgent reveal" style="--d:.1s"><h3>{ic("alert")} {e(b["call_t"])}</h3><p>{e(b["call"])}</p><a class="btn btn-a btn-sm" href="tel:{PHONE}">{ic("phone")} Call Now</a></div></div>'''
    return sec(b, inner)

@kind
def r_myths(b, d):
    it = "".join(f'<div class="sd-myth reveal"{delay(i)}><div class="in"><div class="fr"><span>Myth</span><b>{e(x["m"])}</b></div><div class="bk"><span>Fact</span><p>{e(x["f"])}</p></div></div></div>' for i, x in enumerate(b["items"]))
    return sec(b, head(b) + f'<div class="sd-grid c4">{it}</div><p class="sd-hint">Hover or tap a card to see the fact.</p>')

@kind
def r_cost(b, d):
    paras = "".join(f'<p>{e(p)}</p>' for p in b["paras"])
    inner = f'''<div class="sd-two"><div class="reveal">{head(b, False).replace(" reveal","",1)}{paras}<ul class="sd-tick">{lis(b["items"])}</ul></div>
<aside class="sd-box accent reveal" style="--d:.12s"><h3>{ic("shield")} {e(b["box_t"])}</h3><p>{e(b["box"])}</p><a class="btn btn-a btn-sm" href="../../book-appointment/index.html">{ic("calendar")} Ask Us</a></aside></div>'''
    return sec(b, inner)

@kind
def r_why(b, d):
    pts = "".join(f'<li class="reveal"{delay(i)}>{ic("check")}<div><b>{e(t)}</b><p>{e(x)}</p></div></li>' for i, (t, x) in enumerate(b["points"]))
    inner = f'''<div class="sd-split whysp"><div>{head(b, False)}<ul class="sd-why">{pts}</ul></div>
<figure class="sd-fig reveal" style="--d:.15s"><img src="../../{e(b["img"])}" alt="{e(b["img_alt"])}" loading="lazy"><figcaption>{e(b["cap"])}</figcaption></figure></div>'''
    return sec(b, inner)

@kind
def r_reviews(b, d):
    revs = b.get("reviews") or [{"i": c, "name": "[Reviewer name]", "date": "[Month, Year]", "text": "[Paste a real Google review here, exactly as the patient wrote it.]"} for c in "ABCDEF"]
    cards = "".join(f'<article class="card rv"><div class="rv-h"><span class="rv-av">{e(r.get("i", r["name"][:1]))}</span><div><b>{e(r["name"])}</b><small>{e(r.get("date",""))}</small></div></div><div class="stars" aria-label="5 stars">★★★★★</div><p>{e(r["text"])}</p><span class="rv-src">Posted on Google</span></article>' for r in revs)
    inner = f'''{head(b)}<div class="rv-slider reveal" data-rv><button class="rv-nav prev" type="button" aria-label="Previous review">{ic("arrow").replace('<path d="M5 12h14M13 6l6 6-6 6"/>','<path d="M15 6l-6 6 6 6"/>')}</button><div class="rv-track" tabindex="0" aria-label="Patient reviews">{cards}</div><button class="rv-nav next" type="button" aria-label="Next review">{ic("arrow").replace('<path d="M5 12h14M13 6l6 6-6 6"/>','<path d="M9 6l6 6-6 6"/>')}</button><div class="rv-ctrl"><div class="rv-dots" aria-hidden="true"></div></div>
<div class="rv-more"><a class="btn btn-a btn-sm" href="{e(b["gmaps"])}" target="_blank" rel="noopener">More Reviews</a></div></div>'''
    return sec(b, inner, "reviews")

@kind
def r_visit(b, d):
    wa = f"https://wa.me/{WA}?text=Hello%2C%20I%20would%20like%20to%20enquire"
    inner = f'''<div class="sd-visit-card reveal"><figure class="sd-vimg"><img src="../../{e(b["img"])}" alt="{e(b["img_alt"])}" loading="lazy"><figcaption>{e(b["cap"])}</figcaption></figure>
<div class="sd-vtxt">{head(b, False).replace(" reveal","",1)}<div class="sd-addr"><p>{ic("pin")}<span><b>{e(CLINIC)}</b><br>{e(ADDR)}</span></p>
<div class="two"><p>{ic("clock")}<span>{e(HOURS)}</span></p><p>{ic("phone")}<span><a href="tel:{PHONE}">{e(PHONE_D)}</a></span></p></div></div>
<div class="sd-btns"><a class="btn btn-a btn-sm" href="{e(b["directions"])}" target="_blank" rel="noopener">{ic("pin")} Get Directions</a><a class="btn btn-p btn-sm" href="tel:{PHONE}">{ic("phone")} Call Now</a><a class="btn btn-ol btn-sm" href="{wa}" target="_blank" rel="noopener">{ic("wa")} WhatsApp Chat</a></div></div></div>'''
    return sec(b, inner)

@kind
def r_faq(b, d):
    q = "".join(f'<div class="acc reveal"{delay(i,.04)}><button class="acc-q" aria-expanded="false">{e(x[0])}<span class="pm"></span></button><div class="acc-a"><div><p>{e(x[1])}</p></div></div></div>' for i, x in enumerate(b["items"]))
    return sec(b, head(b) + f'<div class="sd-faq">{q}</div>')

@kind
def r_cta(b, d):
    wa = f"https://wa.me/{WA}?text=Hello%2C%20I%20would%20like%20to%20enquire"
    return f'''<section class="sd-final" id="{b["id"]}"><span class="sd-orb o1"></span><span class="sd-orb o2"></span><div class="container reveal"><div class="txt"><h2>{e(b["h2"])}</h2><p>{e(b["p"])}</p></div>
<div class="sd-btns"><a class="btn btn-a pulse" href="{wa}" target="_blank" rel="noopener">{ic("wa")} WhatsApp Chat</a><a class="btn btn-o" href="tel:{PHONE}">{ic("phone")} Call Now</a><a class="btn btn-o" href="../../contact-us/index.html">{ic("pin")} Directions</a></div></div></section>'''

def page(d):
    wa = f"https://wa.me/{WA}?text=Hello%2C%20I%20would%20like%20to%20enquire"
    url = f'{SITE}/services/{d["slug"]}/'
    faq_b = next(b for b in d["blocks"] if b["kind"] == "faq")
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q[0], "acceptedAnswer": {"@type": "Answer", "text": q[1]}} for q in faq_b["items"]]}
    svc_ld = {"@context": "https://schema.org", "@type": ["Service", "MedicalProcedure"], "name": d["name"], "description": d["seo_desc"], "provider": {"@type": "MedicalClinic", "name": CLINIC, "url": SITE}, "areaServed": "Kharadi, Pune"}
    bc_ld = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE + "/services/"},
        {"@type": "ListItem", "position": 3, "name": d["name"], "item": url}]}
    j = lambda o: json.dumps(o, ensure_ascii=False)
    stats = "".join(
        f'<div class="sd-stat reveal"{delay(i,.08)}><b' + (f' data-count="{s["n"]}" data-suf="{e(s.get("suf",""))}">0' if "n" in s else f'>{e(s["text"])}') + f'</b><span>{e(s["label"])}</span></div>'
        for i, s in enumerate(d["stats"]))
    nav = "".join(f'<a href="#{i}">{e(l)}</a>' for i, l in d["nav"])
    body = "".join(R[b["kind"]](b, d) for b in d["blocks"])
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(d["seo_title"])}</title><meta name="description" content="{e(d["seo_desc"])}">
<link rel="canonical" href="{url}"><meta name="theme-color" content="#0A4A2A"><meta name="robots" content="index,follow">
<meta property="og:type" content="website"><meta property="og:title" content="{e(d["seo_title"])}"><meta property="og:description" content="{e(d["seo_desc"])}"><meta property="og:url" content="{url}"><meta property="og:site_name" content="{e(CLINIC)}"><meta property="og:image" content="{SITE}/{d["hero_img"]}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(d["seo_title"])}"><meta name="twitter:description" content="{e(d["seo_desc"])}">
<link rel="icon" href="../../assets/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../assets/css/style.css"><link rel="stylesheet" href="../../assets/css/premium.css"><link rel="stylesheet" href="../../assets/css/service-detail.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{j(svc_ld)}</script>
<script type="application/ld+json">{j(faq_ld)}</script>
<script type="application/ld+json">{j(bc_ld)}</script>
</head><body class="svc">
<div class="pre"><span></span></div><div class="pbar"></div>
<script src="../../assets/js/config.js"></script><script src="../../assets/js/layout.js" data-part="header" data-active="services"></script>
<main class="sd">
<section class="sd-hero"><span class="sd-orb o1"></span><span class="sd-orb o2"></span><span class="sd-orb o3"></span>
<div class="container"><div class="bc"><a href="../../index.html">Home</a><span>/</span><a href="../../services/index.html">Services</a><span>/</span>{e(d["name"])}</div>
<div class="sd-hero-grid"><div class="sd-hero-txt">
<span class="eyebrow">{e(d["eyebrow"])}</span><h1>{e(d["h1"])}</h1>
<p class="sd-short"><b>In short:</b> {e(d["short"])}</p><p class="sd-by">{ic("shield")}<span>{e(d["byline"])}</span></p>
<div class="sd-btns"><a class="btn btn-a pulse" href="{wa}" target="_blank" rel="noopener">{ic("wa")} WhatsApp Chat</a><a class="btn btn-o" href="tel:{PHONE}">{ic("phone")} Call Now</a></div></div>
<div class="sd-hero-card"><div class="sd-photo"><img src="../../{e(d["hero_img"])}" alt="{e(d["hero_alt"])}" width="900" height="1200"></div>
<div class="sd-float f1">{ic("shield")}<span>Private consultation</span></div><div class="sd-float f2">{ic("clock")}<span>{e(HOURS)}</span></div></div></div></div></section>
<div class="container"><div class="sd-stats">{stats}</div></div>
<nav class="sd-nav" aria-label="On this page"><div class="container"><span class="lbl">On this page</span><div class="sd-nav-in">{nav}</div></div></nav>
{body}
<p class="sd-medical container">{e(d["medical_note"])}</p>
</main>
<script src="../../assets/js/layout.js" data-part="footer"></script>
<button class="totop" aria-label="Back to top"><svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 15l6-6 6 6"/></svg></button><div class="lb"><img src="" alt="Enlarged view"></div>
<script src="../../assets/js/main.js"></script><script src="../../assets/js/premium.js" defer></script><script src="../../assets/js/service-detail.js" defer></script>
</body></html>
'''

def build(slug):
    d = json.loads((CONTENT / f"{slug}.json").read_text(encoding="utf-8"))
    out = ROOT / "services" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page(d), encoding="utf-8")
    print("built", out.relative_to(ROOT))

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args: sys.exit(__doc__)
    for s in ([p.stem for p in CONTENT.glob("*.json")] if args[0] == "--all" else args): build(s)
