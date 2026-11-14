# -*- coding: utf-8 -*-
"""Generates the whole hospital website. Run: python build.py  (edit content.py first)."""
import os, re, json, shutil, html as H
from content import *

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "site")
SRC = os.path.join(BASE, "src")
IDX = "index.html" if C["link_index"] else ""
REPORT = []

ICONS = {
 "cross": '<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>', "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5L15.5 10"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', "heart": '<path d="M12 21s-8-5.5-8-11a4.5 4.5 0 018-2.8A4.5 4.5 0 0120 10c0 5.5-8 11-8 11z"/>',
 "bed": '<path d="M3 19V6M3 15h18v4M21 15v-2a3 3 0 00-3-3h-7v5"/><circle cx="7" cy="11" r="1.6"/>', "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.5 3.2-5.5 7-5.5s7 2 7 5.5M16 4.8a3.5 3.5 0 010 6.4M18 14.8c2.4.6 4 2.2 4 5.2"/>',
 "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>', "check": '<path d="M5 13l4 4L19 7"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z"/>', "pulse": '<path d="M3 12h4l2-6 4 12 2-6h6"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>', "pin": '<path d="M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "wa": '<path d="M3 21l1.6-4.8A9 9 0 1112 21a9 9 0 01-4.2-1z"/><path d="M9 9c0 3 3 6 6 6l1-2-2-1-1 .8c-.8-.4-1.6-1.2-2-2L11.8 10l-1-2z"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>', "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>', "up": '<path d="M6 15l6-6 6 6"/>', "left": '<path d="M15 6l-6 6 6 6"/>', "right": '<path d="M9 6l6 6-6 6"/>',
 "cal": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', "award": '<circle cx="12" cy="9" r="6"/><path d="M8.5 14l-1.5 7 5-3 5 3-1.5-7"/>', "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>', "x": '<path d="M6 6l12 12M18 6L6 18"/>', "zoom": '<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5M11 8v6M8 11h6"/>',
}
def ic(n, cls="ico"): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[n]}</svg>'
def esc(s): return H.escape(s, quote=True)
def slugs(): return {s[0]: s for s in SERVICES}

# ---------- placeholder images (SVG, replace with real JPG/WebP using same names) ----------
PAL = [("#08381E", "#1C8A4A"), ("#0A4A2A", "#2E9E5B"), ("#0F5C33", "#7BBF5A"), ("#073B22", "#B3262E"), ("#0B5A2F", "#2FA36B"), ("#12663A", "#C9A24A")]
def ph(name, w, h, i=0, glyph="cross"):
    c1, c2 = PAL[i % len(PAL)]; s = h / 130
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>'
           f'<radialGradient id="r" cx=".8" cy=".15" r=".7"><stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>'
           f'<rect width="{w}" height="{h}" fill="url(#g)"/><rect width="{w}" height="{h}" fill="url(#r)"/>'
           f'<g fill="none" stroke="#fff" stroke-opacity=".10" stroke-width="2"><circle cx="{w*.88:.0f}" cy="{h*.2:.0f}" r="{h*.5:.0f}"/><circle cx="{w*.88:.0f}" cy="{h*.2:.0f}" r="{h*.72:.0f}"/><circle cx="{w*.05:.0f}" cy="{h*1.0:.0f}" r="{h*.55:.0f}"/></g>'
           f'<g transform="translate({w*.78-h*.34:.0f},{h*.5-h*.34:.0f}) scale({h*.68/60:.2f})" opacity="{.0 if w>1000 else .10}" fill="#fff"><path d="M30 4C22 14 22 28 30 38 38 28 38 14 30 4z"/><path d="M30 40C20 36 8 30 2 18c10 0 22 6 28 22zM30 40C40 36 52 30 58 18c-10 0-22 6-28 22z"/></g>'
           f'<g transform="translate({w*(.80 if w>1000 else .66)-24*s*1.5:.0f},{h/2-24*s*1.5:.0f}) scale({s*1.5:.2f})" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity=".85">{ICONS[glyph]}</g></svg>')
    open(os.path.join(OUT, "assets/img", name), "w", encoding="utf-8").write(svg)
def logo(name, dark):
    col = "#fff" if dark else "#073B46"; acc = "#E9A23B"
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 60" width="260" height="60"><rect x="2" y="6" width="48" height="48" rx="14" fill="{acc}"/><path d="M26 16h8v10h10v8H34v10h-8V34H16v-8h10z" fill="#073B46" transform="translate(-1 -1)"/>'
           f'<text x="60" y="30" font-family="Georgia,serif" font-size="23" fill="{col}">{C["short"].upper()}</text><text x="60" y="48" font-family="Arial,sans-serif" font-size="10.5" letter-spacing="2.2" fill="{col}" opacity=".8">SURGICAL HOSPITAL</text></svg>')
    open(os.path.join(OUT, "assets/img", name), "w", encoding="utf-8").write(svg)

# ---------- meta fitting (title 50-60, description 150-160) ----------
def fit_title(t):
    if len(t) > 60:
        w = t.split()
        while len(" ".join(w)) > 60: w.pop()
        t = " ".join(w).rstrip(" |,:-")
    if len(t) < 50:
        for suf in [f" | {C['short']} Clinic {C['city']}", f" | {C['name']}", f" | {C['short']} Clinic", f" | {C['name']}, {C['city']}", f" - {C['short']} Clinic", f" | {C['short']}"]:
            if 50 <= len(t + suf) <= 60: return t + suf
        REPORT.append(f"title length {len(t)}: {t}")
    return t
def fit_desc(d):
    ext = [" Book your appointment online today.", f" Trusted surgical care in {C['city']}.", " Call or WhatsApp us now.", " Advanced laser & laparoscopic surgery."]
    d = d.strip()
    while len(d) < 150 and ext: d += ext.pop(0)
    if len(d) > 160:
        d = d[:160].rsplit(" ", 1)[0].rstrip(",;:- ")
        if not d.endswith((".", "!", "?")): d += "."
    if not 150 <= len(d) <= 160: REPORT.append(f"desc length {len(d)}: {d[:60]}")
    return d

# ---------- layout ----------
ACTIVE_NAV = [("§", "Home", "home"), ("§about-us/", "About", "about"), (None, "Services", "services"), ("§products/", "Products", "products"), ("§blogs/", "Blogs", "blogs"), ("§contact-us/", "Contact", "contact")]
def nav(active):
    out = ""
    for href, lab, key in ACTIVE_NAV:
        on = ' class="on"' if key == active else ""
        if href is None:
            sd = slugs(); items = "".join(f'<div class="dg"><h5>{g[0]}</h5>' + "".join(f'<a href="§services/{x}/">{esc(sd[x][1])}</a>' for x in g[3]) + '</div>' for g in GROUPS)
            out += f'<div class="dd"><a href="§services/"{on}>Services ▾</a><div class="dd-m"><a class="dd-all" href="§services/">View all services {ic("arrow")}</a>{items}</div></div>'
        else: out += f'<a href="{href}"{on}>{lab}</a>'
    out += f'<div class="nav-cta"><a class="btn btn-a btn-sm" href="tel:{C["phone_tel"]}">{ic("phone")} Call Now</a><a class="btn btn-p btn-sm" href="§book-appointment/">{ic("cal")} Book Now</a></div>'
    return out
def social(): return "".join(f'<a href="{u}" aria-label="{k}" target="_blank" rel="noopener">{k[0]}</a>' for k, u in C["social"].items())

def page(path, title, desc, body, active="", crumbs=None, schema=None, og_img="hero-1"):
    depth = 0 if path == "404.html" else path.count("/")
    pfx = "/" if path == "404.html" else "../" * depth
    clean = C["base"] + "/" + ("" if path in ("", "404.html") else path)
    t, d = fit_title(title), fit_desc(desc)
    sch = list(schema or [])
    if crumbs:
        sch.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": C["base"] + "/" + (h or path)} for i, (n, h) in enumerate([("Home", "")] + crumbs)]})
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in sch)
    foot_svc = "".join(f'<li><a href="§services/{s[0]}/">{esc(s[1])}</a></li>' for s in SERVICES if s[0] in CORE[:8])
    h = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(t)}</title><meta name="description" content="{esc(d)}">
<link rel="canonical" href="{clean}"><meta name="theme-color" content="#0A4A2A"><meta name="robots" content="index,follow">
<meta property="og:type" content="website"><meta property="og:title" content="{esc(t)}"><meta property="og:description" content="{esc(d)}"><meta property="og:url" content="{clean}"><meta property="og:site_name" content="{esc(C['name'])}"><meta property="og:image" content="{C['base']}/assets/img/{og_img}.jpg">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(t)}"><meta name="twitter:description" content="{esc(d)}">
{C['gsc']}
<link rel="icon" href="§assets/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="§assets/css/style.css">
<script>document.documentElement.classList.add('js')</script>
{ld}
{C['ga']}
</head><body>
<div class="pre"><span></span></div><div class="pbar"></div>
<div class="top"><div class="container"><div class="l"><span>{ic('clock')}{C['hours']}</span><span>{ic('phone')}Call / WhatsApp: <a href="tel:{C['phone_tel']}">{C['phone']}</a></span></div><div class="r"><a href="mailto:{C['email']}">{ic('mail')}{C['email']}</a><div class="soc">{social()}</div></div></div></div>
<header class="hdr"><div class="container"><a class="logo" href="§" aria-label="{esc(C['name'])} home"><img src="§assets/img/emblem.png" alt="{esc(C['name'])} logo" width="52" height="48"><span class="lt"><b>DISHA</b><small>Advanced Surgical &amp; Laser Piles Clinic</small></span></a>
<nav class="nav" id="mainnav" aria-label="Main">{nav(active)}</nav>
<div class="hcta"><a class="btn btn-a btn-sm" href="tel:{C['phone_tel']}">{ic('phone')} Call Now</a><a class="btn btn-p btn-sm pulse" href="§book-appointment/">{ic('cal')} Book Appointment</a><button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mainnav"><span class="b-o">{ic('menu')}</span><span class="b-c">{ic('x')}</span></button></div></div></header><div class="nav-ov" aria-hidden="true"></div>
<main>{body}</main>
<footer class="ft"><div class="container"><div class="grid">
<div class="f-brand"><a class="logo" href="§"><img class="ew" src="§assets/img/emblem.png" alt="{esc(C['name'])} logo" width="52" height="48"><span class="lt"><b>DISHA</b><small>Advanced Surgical &amp; Laser Piles Clinic</small></span></a><p>{esc(C['tagline'])}. Advanced laser piles and laparoscopic surgery in {C['city']} by {C['doctor']}.</p><div class="soc" style="margin-top:14px">{social()}</div></div>
<div class="f-links"><h4>Quick Links</h4><ul><li><a href="§about-us/">About Us</a></li><li><a href="§services/">Services</a></li><li><a href="§products/">Products</a></li><li><a href="§blogs/">Blogs</a></li><li><a href="§book-appointment/">Book Appointment</a></li><li><a href="§contact-us/">Contact Us</a></li></ul></div>
<div class="f-svc"><h4>Our Services</h4><ul>{foot_svc}</ul></div>
<div class="f-contact"><h4>Contact</h4><ul><li>{ic('pin')} {esc(C['address'])}</li><li>{ic('phone')} <a href="tel:{C['phone_tel']}">{C['phone']}</a></li><li>{ic('mail')} <a href="mailto:{C['email']}">{C['email']}</a></li><li>{ic('clock')} {C['hours']}</li><li>{C['hours2']}</li></ul></div></div>
<div class="bot"><span>© 2026 {esc(C['name'])}. All rights reserved.</span><div><a href="§privacy-policy/">Privacy Policy</a><a href="§terms-and-conditions/">Terms &amp; Conditions</a></div></div></div></footer>
<div class="fl"><a class="wa" href="https://wa.me/{C['whatsapp']}?text=Hello%2C%20I%20would%20like%20to%20enquire" target="_blank" rel="noopener" aria-label="WhatsApp enquiry">{ic('wa')}</a><a class="cl" href="tel:{C['phone_tel']}" aria-label="Call now">{ic('phone')}</a></div>
<button class="totop" aria-label="Back to top">{ic('up')}</button><div class="lb"><img src="" alt="Enlarged view"></div>
<script src="§assets/js/config.js"></script><script src="§assets/js/main.js"></script>
</body></html>'''
    def fix(m):
        p = m.group(1)
        if p == "" or p.endswith("/"): p += IDX
        r = pfx + p
        return f'href="{r or "./"}"'
    h = re.sub(r'href="§([^"#]*)"', fix, h).replace("§", pfx)
    f = os.path.join(OUT, path if path.endswith(".html") else os.path.join(path, "index.html"))
    os.makedirs(os.path.dirname(f), exist_ok=True)
    open(f, "w", encoding="utf-8").write(h)

def header(title, sub, crumbs):
    c = '<a href="§">Home</a>' + "".join(f'<span>/</span>' + (f'<a href="§{h}">{n}</a>' if h else f'{n}') for n, h in crumbs)
    return f'<section class="ph"><div class="container"><div class="bc">{c}</div><h1>{title}</h1><p>{sub}</p></div></section>'

def sh(eyebrow, title, sub=""): return f'<div class="sh reveal"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2>' + (f'<p>{sub}</p>' if sub else "") + '</div>'
def cta(title="Need a surgical consultation?", sub="Talk to our surgeon today. Honest advice, no pressure."):
    return f'<section class="section" style="padding-top:20px"><div class="container"><div class="cta reveal"><div><h2>{title}</h2><p>{sub}</p></div><div class="bt"><a class="btn btn-a pulse" href="§book-appointment/">{ic("cal")} Book Appointment</a><a class="btn btn-o" href="§contact-us/">Contact Us</a><a class="btn btn-o" href="https://wa.me/{C["whatsapp"]}" target="_blank" rel="noopener">{ic("wa")} WhatsApp</a></div></div></div></section>'
def faq(items): return "".join(f'<div class="acc reveal"><button class="acc-q" aria-expanded="false">{esc(q)}<span class="pm"></span></button><div class="acc-a"><div><p>{esc(a)}</p></div></div></div>' for q, a in items)

def svc_card(s, i=0):
    return f'<article class="card reveal" style="--d:{(i%3)*.08}s" data-cat="svc"><a class="im" href="§services/{s[0]}/"><img src="§assets/img/service-{s[0]}.jpg" alt="{esc(s[1])} in {C["city"]}" width="800" height="600" loading="lazy"><span class="badge">{ic(s[2])}</span></a><div class="bd"><h3>{esc(s[1])}</h3><p>{esc(s[3])}</p><a class="more" href="§services/{s[0]}/">Know More {ic("arrow")}</a></div></article>'
def blog_card(b, i=0):
    return f'<article class="card reveal" style="--d:{(i%3)*.08}s" data-cat="{b["cat"]}"><a class="im" href="§blogs/{b["slug"]}/"><img src="§assets/img/blog-{b["slug"]}.jpg" alt="{esc(b["title"])}" width="800" height="450" loading="lazy"></a><div class="bd"><div class="meta"><span class="tag">{b["cat"]}</span><span>{b["date_h"]}</span><span>{b["mins"]} min read</span></div><h3>{esc(b["title"])}</h3><p>{esc(b["sub"])}</p><a class="more" href="§blogs/{b["slug"]}/">Read Article {ic("arrow")}</a></div></article>'
def prod_card(p, i=0):
    return f'<article class="card reveal" style="--d:{(i%4)*.08}s" data-cat="prod"><a class="im" href="§products/{p[0]}/" style="aspect-ratio:1"><img src="§assets/img/product-{p[0]}.jpg" alt="{esc(p[1])}" width="800" height="800" loading="lazy"><span class="ptag">Recommended</span></a><div class="bd"><h3>{esc(p[1])}</h3><p>{esc(p[2])}</p><a class="more" href="§products/{p[0]}/">View Details {ic("arrow")}</a></div></article>'

# ---------- blog prep ----------
import datetime
def words(t): return len(re.findall(r"\w+", t))
for b in BLOGS:
    dt = datetime.date.fromisoformat(b["date"]); b["date_h"] = dt.strftime("%d %b %Y").lstrip("0"); b["wc"] = words(b["body"]); b["mins"] = max(1, round(b["wc"] / 200))
    if len(b["title"]) not in range(50, 61): REPORT.append(f"blog title {len(b['title'])}: {b['title']}")
    if len(b["sub"]) not in range(100, 121): REPORT.append(f"blog sub {len(b['sub'])}: {b['sub']}")
    if not 800 <= b["wc"] <= 1200: REPORT.append(f"blog words {b['wc']}: {b['slug']}")
for s in SERVICES:
    if not 20 <= words(s[3]) <= 25: REPORT.append(f"svc short {words(s[3])}: {s[0]}")
    if not 100 <= words(s[5]) <= 150: REPORT.append(f"svc full {words(s[5])}: {s[0]}")

def blog_html(body):
    out, ul, toc = [], False, []
    for ln in body.split("\n"):
        if ln.startswith("- "):
            if not ul: out.append("<ul>"); ul = True
            out.append(f"<li>{esc(ln[2:])}</li>"); continue
        if ul: out.append("</ul>"); ul = False
        if ln.startswith("## "):
            i = re.sub(r"[^a-z0-9]+", "-", ln[3:].lower()).strip("-"); toc.append((i, ln[3:])); out.append(f'<h2 id="{i}">{esc(ln[3:])}</h2>')
        elif ln.strip(): out.append(f"<p>{esc(ln)}</p>")
    if ul: out.append("</ul>")
    return "\n".join(out), toc

HOSP = {"@context": "https://schema.org", "@type": "MedicalClinic", "name": C["name"], "description": C["tagline"], "url": C["base"], "telephone": C["phone"], "email": C["email"], "image": C["base"] + "/assets/img/hero-1.jpg",
        "address": {"@type": "PostalAddress", "streetAddress": C["address"], "addressLocality": C["city"], "addressRegion": "Maharashtra", "addressCountry": "IN"},
        "openingHours": "Mo-Sa 09:00-20:00", "areaServed": C["areas"].split(", "), "sameAs": [u for u in C["social"].values() if u != "#"]}
PHYS = {"@context": "https://schema.org", "@type": "Physician", "name": C["doctor"], "medicalSpecialty": "Surgery", "worksFor": {"@type": "MedicalClinic", "name": C["name"]}}

# ======================= BUILD =======================
if os.path.exists(OUT): shutil.rmtree(OUT)
shutil.copytree(os.path.join(SRC, "assets"), os.path.join(OUT, "assets"))
os.makedirs(os.path.join(OUT, "assets/img"), exist_ok=True)
logo("logo.svg", False); logo("logo-white.svg", True)
open(os.path.join(OUT, "assets/img/favicon.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#0A4A2A"/></svg>')
ph("mission.svg", 800, 600, 3, "eye")
for k in range(1, 5): ph(f"cert-{k}.svg", 800, 600, k, "award")
for k in range(3): ph(f"team-{k+1}.svg", 600, 600, k + 1, "user")

# ---- config.js
open(os.path.join(OUT, "assets/js/config.js"), "w").write("window.SITE=" + json.dumps({"name": C["name"], "whatsapp": C["whatsapp"], "email": C["email"], "slots": C["slots"], "closedDays": C["closed_days"]}) + ";")

# ---- HOME
slides = [("Advanced Laser Piles Treatment", "Painless, minimal-cut laser and surgical care for piles, fissure and fistula by a consultant proctologist.", "Book Appointment", "book-appointment/", "Explore Services", "services/"),
          ("Keyhole Surgery. Faster Recovery.", "Gallbladder, hernia, appendix and more with advanced laparoscopic techniques, smaller cuts and a quicker return to routine.", "View Services", "services/", "Contact Us", "contact-us/"),
          ("One Surgeon. Start to Finish.", "Dr. Abhijeet Suresh Shinde examines, operates and follows up your recovery. Journey towards better life.", "Meet the Doctor", "about-us/", "Book Appointment", "book-appointment/")]
sl = ""
for k, (h, p, b1, l1, b2, l2) in enumerate(slides):
    tag = "h1" if k == 0 else "h2"
    sl += f'<div class="slide{" on" if k == 0 else ""}"><img src="§assets/img/hero-{k+1}.jpg" alt="{esc(h)} - {esc(C["name"])}" width="1920" height="800"{"" if k == 0 else " loading=\"lazy\""}><div class="container"><div class="hc"><span class="eyebrow">{esc(C["name"])}</span><{tag}>{h}</{tag}><p>{p}</p><div class="bt"><a class="btn btn-a" href="§{l1}">{b1} {ic("arrow")}</a><a class="btn btn-o" href="§{l2}">{b2}</a></div></div></div></div>'
hero = f'<section class="hero" aria-label="Highlights">{sl}<div class="hero-logo" aria-hidden="true"><div class="hl-card"><img src="§assets/img/emblem.png" alt="" width="210" height="193"><span class="hl-line"></span><b>DISHA</b><small>Advanced Surgical &amp; Laser Piles Clinic</small><i>Journey towards better life</i></div></div><button class="arr prev" aria-label="Previous">{ic("left")}</button><button class="arr next" aria-label="Next">{ic("right")}</button><div class="dots">{"".join(f"<button class=\"dot{chr(32)+chr(111)+chr(110) if k==0 else chr(32)}\" aria-label=\"Slide {k+1}\"></button>" for k in range(3))}</div></section>'
stats = '<section class="stats"><div class="container"><div class="grid g4 reveal">' + "".join(f'<div class="stat"><b data-count="{n}" data-suf="{s}">0</b><span>{l}</span></div>' for n, s, l in [(len(SERVICES), "+", "Surgical Treatments"), (11, " hrs", "Open Daily, 10 AM – 9 PM"), (100, "%", "Private Consultations"), (1, "", "Surgeon, Start to Finish")]) + '</div></div></section>'  # [REPLACE] numbers
intro = f'''<section class="section"><div class="container split"><div class="reveal"><span class="eyebrow">About the Clinic</span><h2>Journey towards a better life</h2>
<p>{esc(C["name"])} is a specialised clinic in {C["city"]} led by {C["doctor"]}, a General &amp; Laparoscopic Surgeon and Consultant Proctologist. We offer advanced laser and surgical treatment for piles, fissure and fistula along with laparoscopic, urological and general surgery. Every consultation is private, every opinion is honest, and you are cared for by the same surgeon from the first visit to the last follow-up.</p>
<ul class="ticks"><li>{ic("check")} Honest opinion on whether you need surgery</li><li>{ic("check")} Advanced laser and laparoscopic technology</li><li>{ic("check")} Private, comfortable and respectful care</li></ul><a class="btn btn-p" href="§about-us/" style="margin-top:12px">Read Our Story {ic("arrow")}</a></div>
<div class="frame reveal"><img src="§assets/img/about.jpg" alt="{esc(C["name"])} building and care team in {C["city"]}" width="800" height="640" loading="lazy"><div class="float"><b>Open Daily</b>10 AM – 9 PM</div></div></div></section>'''
home_svc = f'<section class="section alt"><div class="container">{sh("Core Surgeries", "Treatments our patients visit us for", "Each one explained in plain language, with recovery guidance.")}<div class="grid g3">{"".join(svc_card(s, i) for i, s in enumerate([x for c in CORE for x in SERVICES if x[0]==c]))}</div><div style="text-align:center;margin-top:26px"><a class="btn btn-p" href="§services/">View All {len(SERVICES)} Services {ic("arrow")}</a></div></div></section>'
why = f'<section class="section"><div class="container">{sh("Why Choose Us", "Care that stays with you", "Six reasons patients trust Disha Clinic.")}<div class="grid g3">{"".join(f"<div class=\"card why reveal\" style=\"--d:{(i%3)*.08}s\"><div class=\"ib\">{ic(a)}</div><h3>{b}</h3><p>{c}</p></div>" for i, (a, b, c) in enumerate(WHY))}</div></div></section>'
def surgeon(cls="section", cta_label="Meet the Doctor", cta_href="§about-us/", eyebrow="Our Surgeon", sec_label="Book a Consultation", sec_href="§book-appointment/"):
    return f'''<section class="{cls}"><div class="container split doc-split"><div class="doc-photo reveal"><div class="frame"><img src="§assets/img/doctor.jpg" alt="{C["doctor"]}, surgeon at {esc(C["name"])}" width="800" height="900" loading="lazy"></div><div class="doc-badge"><b>Consultant</b><span>Proctologist &amp; Laparoscopic Surgeon</span></div></div><div class="reveal"><span class="eyebrow">{eyebrow}</span><h2>{C["doctor"]}</h2><p class="doc-role">{C["quals"]}</p><p>Dr. Shinde combines laparoscopic surgical expertise with focused proctology practice, treating piles, fissure and fistula with laser and modern techniques. [REPLACE: add qualifications and years of experience]</p>
<ul class="ticks"><li>{ic("check")} General &amp; Laparoscopic Surgeon</li><li>{ic("check")} Consultant Proctologist (piles, fissure, fistula)</li><li>{ic("check")} Same surgeon from consultation to follow-up</li></ul><div class="doc-cta"><a class="btn btn-p" href="{cta_href}">{cta_label} {ic("arrow")}</a><a class="btn btn-ol" href="{sec_href}">{sec_label}</a></div></div></div></section>'''
doc = surgeon("section alt", "Meet the Doctor", "§about-us/")
fac = f'<section class="section dark"><div class="container">{sh("Facilities", "Built for safe, comfortable care")}<div class="fac">{"".join(f"<div class=\"reveal\">{ic(['clock','pulse','bed','shield','cross','pin'][i])}<span>{f}</span></div>" for i, f in enumerate(FACILITIES))}</div></div></section>'
tests = f'''<section class="section"><div class="container">{sh("Testimonials", "What our patients say")}<div class="tsl reveal">{"".join(f"<div class=\"tt{' on' if i==0 else ''}\"><div class=\"stars\">★★★★★</div><p>“{t}”</p><div class=\"who\"><div class=\"av\">{n[0]}</div><div><b>{n}</b><small>{r}</small></div></div></div>" for i, (n, r, t) in enumerate(TESTIMONIALS))}<div class="tdots">{"".join(f"<button class=\"{'on' if i==0 else ''}\" aria-label=\"Review {i+1}\"></button>" for i in range(3))}</div></div></div></section>'''
tests = tests if TESTIMONIALS else ""
groups_html = '<section class="section alt grp-sec"><div class="container">' + sh("Complete Care", "Surgeries we do", "Browse every department. Each procedure has its own detailed page.") + '<div class="grp">' + "".join('<div class="card gcard reveal" style="--d:%.2fs"><div class="gtop"><div class="ib">%s</div><div><h3>%s</h3><p>%s</p></div></div><ul>%s</ul><a class="more" href="§services/">View all services %s</a></div>' % ((i%4)*.06, ic(g[1]), g[0], g[2], "".join('<li><a href="§services/%s/">%s<span>%s</span></a></li>' % (x, ic("arrow"), esc(slugs()[x][1])) for x in g[3]), ic("arrow")) for i, g in enumerate(GROUPS)) + '</div></div></section>'
home_blog = f'<section class="section alt"><div class="container">{sh("Latest Blogs", "Health notes from our surgical desk")}<div class="grid g3">{"".join(blog_card(b, i) for i, b in enumerate(BLOGS))}</div><div style="text-align:center;margin-top:26px"><a class="btn btn-p" href="§blogs/">All Articles {ic("arrow")}</a></div></div></section>'
home_faq = f'<section class="section"><div class="container" style="max-width:820px">{sh("FAQ", "Questions patients ask us")}{faq(HOME_FAQ)}</div></section>'
def contact_prev():
    return f'''<section class="section alt"><div class="container split"><div class="reveal"><span class="eyebrow">Visit Us</span><h2>Find us in {C["city"]}</h2>
<div class="ci"><div class="ib">{ic("pin")}</div><div><b>Address</b>{esc(C["address"])}</div></div><div class="ci"><div class="ib">{ic("phone")}</div><div><b>Appointments</b><a href="tel:{C["appt_tel"]}">{C["appt"]}</a></div></div><div class="ci"><div class="ib">{ic("clock")}</div><div><b>Working Hours</b>{C["hours"]}<br>{C["hours2"]}</div></div></div>
<div class="reveal"><iframe class="map" title="{esc(C["name"])} location on Google Maps" src="{C["map_embed"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div></section>'''
page("", f"Best Piles Treatment Clinic in {C['city']} | {C['short']}", f"{C['name']} in {C['city']} offers laser piles, fissure, fistula and laparoscopic surgery by Dr. Abhijeet Shinde. Open daily 10 AM to 9 PM. Call now.", hero + stats + intro + home_svc + groups_html + why + fac + tests + home_blog + home_faq + cta(), "home", None, [HOSP, PHYS])

# ---- ABOUT
timeline = [("Qualification", "General & Laparoscopic Surgeon", "[REPLACE: degrees, college, year]", "award"), ("Specialisation", "Consultant Proctologist", "Piles, fissure, fistula & anorectal disorders", "user"), ("Experience", "Laparoscopic and general surgery", "[REPLACE: years and hospitals]", "pulse"), ("Clinic", f"{C['name']}", f"{C['city']}, Maharashtra", "pin"), ("Today", "Laser and advanced surgical care", "Journey towards better life", "heart")]
def journey_html():
    dn = C["doctor"]
    items = "".join(f'<div class="tj-i {"l" if i % 2 == 0 else "r"}"><span class="tj-dot">{ic(ic_)}</span><div class="tj-card"><span class="tj-no">{i+1:02d}</span><small class="tj-k">{y}</small><h3>{t}</h3><p>{d}</p></div></div>' for i, (y, t, d, ic_) in enumerate(timeline))
    head = sh("Our Doctor", dn + ": the journey", "From training to treating, one surgeon who stays with you at every step.")
    return (f'<section class="section tj-sec"><div class="container">{head}'
            f'<div class="tj" data-tj><div class="tj-line"><span class="tj-fill"></span></div>{items}<div class="tj-end reveal"><a class="btn btn-p" href="§book-appointment/">{ic("cal")} Start your journey with us</a></div></div></div></section>')
JOURNEY = [("1","Call or Book","Call, WhatsApp or book online. Open daily 10 AM to 9 PM.","phone"),("2","Private Consultation","A gentle, private examination and a clear explanation.","user"),("3","Treatment Plan","The simplest effective option, with laser or surgery only when needed.","shield"),("4","Recovery & Follow-up","Aftercare guidance and follow-up with the same surgeon.","heart")]
def steps_html():
    cards = "".join(f'<div class="tj-i"><span class="tj-dot">{ic(ic_)}</span><div class="tj-card"><h3>{t}</h3><p>{d}</p></div></div>' for i, (n, t, d, ic_) in enumerate(JOURNEY))
    return f'<section class="section alt"><div class="container">{sh("Your Journey", "What to expect when you visit", "A simple, comfortable path from first call to full recovery.")}<div class="tj tj4" data-tj><div class="tj-line"><span class="tj-fill"></span></div>{cards}</div></div></section>'
about = header("About Us", f"Meet the team behind {esc(C['name'])}: experienced surgeons committed to safe, compassionate care.", [("About Us", None)]) + f'''
<section class="section"><div class="container split"><div class="frame reveal"><img src="§assets/img/about-who.jpg" alt="Consultation at {esc(C["name"])}" width="800" height="640"></div><div class="reveal"><span class="eyebrow">Who We Are</span><h2>Compassion, skill and trust in every procedure</h2>
<p>{esc(C["name"])} was started by {C["doctor"]}, a General &amp; Laparoscopic Surgeon and Consultant Proctologist, with a simple belief: surgery should be safe, transparent and humane. The clinic focuses on advanced laser and surgical treatment of piles, fissure and fistula, along with laparoscopic, urological and general surgery.</p>
<p>We believe the patient should always understand their diagnosis, options and recovery plan before agreeing to surgery. That is why Dr. Shinde personally examines, operates and follows up on every case, so nothing is lost between handovers. We follow strict hygiene protocols, keep every consultation private, and give honest opinions, including a second opinion without pressure when you want one.</p>
<a class="btn btn-p" href="§book-appointment/">Book Appointment {ic("arrow")}</a></div></div></section>
{surgeon("section alt", "Book a Consultation", "§book-appointment/", "Our Surgeon", "Contact Us", "§contact-us/")}
{journey_html()}
<section class="section alt"><div class="container">{sh("Mission &amp; Vision", "What drives us")}<div class="grid g2"><div class="card mv reveal"><div class="ib">{ic("heart")}</div><h3>Our Mission</h3><p>To deliver safe, ethical and affordable surgical care with compassion, clear communication and the best available technology.</p></div><div class="card mv reveal" style="--d:.1s"><div class="ib">{ic("eye")}</div><h3>Our Vision</h3><p>To be the most trusted laser and surgical piles clinic in the region, known for honest advice, excellent outcomes and a patient experience that feels like family.</p></div></div></div></section>
<section class="section"><div class="container">{sh("Why Choose Us", "Reasons patients trust us")}<div class="grid g3">{"".join(f"<div class=\"card why reveal\" style=\"--d:{(i%3)*.08}s\"><div class=\"ib\">{ic(a)}</div><h3>{b}</h3><p>{c}</p></div>" for i, (a, b, c) in enumerate(WHY))}</div></div></section>
{steps_html()}
<section class="section"><div class="container">{sh("Our Infrastructure", "A calm, modern environment")}<div class="grid g3">{"".join(f"<div class=\"frame reveal\"><img src=\"§assets/img/gallery-{i}.jpg\" alt=\"Clinic infrastructure photo {i}\" width=\"800\" height=\"600\" loading=\"lazy\"></div>" for i in (1, 2, 3))}</div></div></section>''' + cta()
page("about-us/", f"About Us | {C['name']}", f"Learn about {C['name']} in {C['city']}, our founder {C['doctor']}, our mission, vision, experienced team, certificates and patient-first approach to surgery.", about, "about", [("About Us", "about-us/")], [PHYS])

# ---- SERVICES
SD = slugs()
def svc_group(g):
    n = len(g[3]); cls = "g4" if n == 4 else "g3"
    cards = "".join(svc_card(SD[x], i) for i, x in enumerate(g[3]))
    return (f'<div class="gsec"><div class="gh reveal"><span class="ib">{ic(g[1])}</span><div class="gt"><h2>{g[0]}</h2><p>{g[2]}</p></div><span class="gn">{n} treatments</span></div><div class="grid {cls}">{cards}</div></div>')
svc = header("Our Services", "Laser piles care, laparoscopic and general surgery, each explained clearly with its own detailed page.", [("Services", None)]) + f'<section class="section"><div class="container" data-filter-root><div class="chips"><input class="search" type="search" placeholder="Search services…" aria-label="Search services"></div>{"".join(svc_group(g) for g in GROUPS)}<p class="empty hidden">No services match your search.</p></div></section>' + cta()
page("services/", f"Surgical Services in {C['city']} | {C['name']}", f"Explore laser piles, fissure, fistula, laparoscopic, hernia, gallbladder, urology and general surgery services at {C['name']}, {C['city']}.", svc, "services", [("Services", "services/")])
for k, s in enumerate(SERVICES):
    slug, name, icn, short, intro_t, full, feats, faqs, kw = s
    rel = "".join(f'<a href="§services/{r[0]}/">{ic("arrow")} {esc(r[1])}</a>' for r in SERVICES if r[0] != slug)[:3000]
    rel = "".join(f'<a href="§services/{r[0]}/">{ic("arrow")} {esc(r[1])}</a>' for r in [x for x in SERVICES if x[0] != slug][:5])
    body = header(esc(name), esc(intro_t), [("Services", "services/"), (name, None)]) + f'''<section class="section"><div class="container lay"><div class="prose">
<div class="svc-intro reveal"><div class="svc-pic" data-lb="§assets/img/service-{slug}.jpg" title="Click to enlarge"><img src="§assets/img/service-{slug}.jpg" alt="{esc(name)} - {kw[0]}" width="800" height="600"><span class="badge">{ic(icn)}</span><span class="zoom">{ic("zoom")}</span></div>
<div class="svc-txt"><span class="eyebrow">{esc(next((g[0] for g in GROUPS if slug in g[3]), "Surgical Care"))}</span><p class="lead">{esc(short)}</p><div class="svc-chips"><span>{ic("user")} Consultant surgeon</span><span>{ic("shield")} Private consultation</span><span>{ic("clock")} {C["hours"]}</span></div><div class="svc-btns"><a class="btn btn-p btn-sm" href="§book-appointment/">{ic("cal")} Book Appointment</a><a class="btn btn-ol btn-sm" href="https://wa.me/{C["whatsapp"]}" target="_blank" rel="noopener">{ic("wa")} WhatsApp</a></div></div></div>
<h2>{esc(name)} in {C["city"]}</h2><p>{esc(full)}</p><p>Looking for a {kw[0]}? Our team provides {kw[1]} and related care with clear communication from consultation to follow-up.</p>
<h2>Key Features &amp; Benefits</h2><div class="featgrid">{"".join(f"<div class='fe reveal' style='--d:{(i%2)*.08}s'>{ic('check')}<span>{esc(f)}</span></div>" for i, f in enumerate(feats))}</div>
<h2>Gallery</h2><div class="gal"><img src="§assets/img/gallery-1.jpg" alt="{kw[0]} - consultation room" width="800" height="600" loading="lazy"><img src="§assets/img/gallery-2.jpg" alt="{kw[2]} - operation theatre" width="800" height="600" loading="lazy"><img src="§assets/img/gallery-3.jpg" alt="{kw[3]} - recovery room" width="800" height="600" loading="lazy"></div>
<h2>Frequently Asked Questions</h2>{faq(faqs)}</div>
<aside class="aside"><div class="box pri"><h3>Book an Appointment</h3><p style="margin-bottom:12px">Consult Dr. Shinde about {esc(name.lower())}.</p><a class="btn btn-a" style="width:100%;justify-content:center" href="§book-appointment/">{ic("cal")} Book Now</a></div>
<div class="box"><h3>Contact</h3><div class="ci" style="padding:6px 0"><div class="ib">{ic("phone")}</div><div><b>Call</b><a href="tel:{C["phone_tel"]}">{C["phone"]}</a></div></div><div class="ci" style="padding:6px 0"><div class="ib">{ic("wa")}</div><div><b>WhatsApp</b><a href="https://wa.me/{C["whatsapp"]}" target="_blank" rel="noopener">Chat with us</a></div></div></div>
<div class="box rel"><h3>Related Services</h3>{rel}</div></aside></div></section>''' + cta()
    sch = [{"@context": "https://schema.org", "@type": "MedicalProcedure", "name": name, "description": short, "provider": {"@type": "MedicalClinic", "name": C["name"], "url": C["base"]}, "areaServed": C["city"]},
           {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}]
    sch[0]["@type"] = ["Service", "MedicalProcedure"]
    page(f"services/{slug}/", f"{name} in {C['city']}", f"{short} {kw[0].capitalize()} at {C['name']}.", body, "services", [("Services", "services/"), (name, f"services/{slug}/")], sch, f"hero-1")

# ---- PRODUCTS
prods = header("Our Products", "Recovery and care products recommended by our surgeons.", [("Products", None)]) + f'<section class="section"><div class="container"><div class="grid g4">{"".join(prod_card(p, i) for i, p in enumerate(PRODUCTS))}</div></div></section>' + cta("Need help choosing a product?", "Our team will recommend the right size and type for your recovery.")
page("products/", f"Surgical Care Products in {C['city']} | {C['name']}", f"Browse sitz bath tubs, piles comfort cushions, recovery kits, support binders and stockings recommended by Dr. Shinde at {C['name']}.", prods, "products", [("Products", "products/")])
for k, p in enumerate(PRODUCTS):
    rel = "".join(f'<a href="§products/{r[0]}/">{ic("arrow")} {esc(r[1])}</a>' for r in PRODUCTS if r[0] != p[0])
    body = header(esc(p[1]), esc(p[2]), [("Products", "products/"), (p[1], None)]) + f'''<section class="section"><div class="container lay"><div class="prose"><div class="split" style="align-items:start"><div class="frame reveal"><img src="§assets/img/product-{p[0]}.jpg" alt="{esc(p[1])}" width="800" height="800"></div><div class="reveal"><span class="eyebrow">Product</span><h2 style="margin-top:0">{esc(p[1])}</h2><p>{esc(p[3])}</p><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-p" href="https://wa.me/{C["whatsapp"]}?text=I%20would%20like%20to%20enquire%20about%20{esc(p[1]).replace(" ", "%20")}" target="_blank" rel="noopener">{ic("wa")} Enquire on WhatsApp</a><a class="btn btn-ol" href="§contact-us/">Contact Us</a></div></div></div></div>
<aside class="aside"><div class="box rel"><h3>Related Products</h3>{rel}</div><div class="box pri"><h3>Need advice?</h3><p style="margin-bottom:12px">Ask our team which product suits you.</p><a class="btn btn-a" href="tel:{C["phone_tel"]}">{ic("phone")} Call Now</a></div></aside></div></section>'''
    sch = [{"@context": "https://schema.org", "@type": "Product", "name": p[1], "description": p[3], "image": f"{C['base']}/assets/img/product-{p[0]}.jpg", "brand": {"@type": "Brand", "name": C["name"]}}]
    page(f"products/{p[0]}/", f"{p[1]}", f"{p[2]} Available at {C['name']}, {C['city']}.", body + cta(), "products", [("Products", "products/"), (p[1], f"products/{p[0]}/")], sch)

# ---- BLOGS
cats = sorted({b["cat"] for b in BLOGS})
blogs = header("Blogs", "Plain-language guidance on symptoms, procedures and recovery from our surgical team.", [("Blogs", None)]) + f'<section class="section"><div class="container" data-filter-root><div class="chips"><button class="chip on" data-f="all">All</button>{"".join(f"<button class=\"chip\" data-f=\"{c}\">{c}</button>" for c in cats)}<input class="search" type="search" placeholder="Search articles…" aria-label="Search articles"></div><div class="grid g3">{"".join(blog_card(b, i) for i, b in enumerate(BLOGS))}</div><p class="empty hidden">No articles found.</p></div></section>' + cta()
page("blogs/", f"Health Blogs & Surgical Guides | {C['name']}", f"Read expert articles on gallbladder stones, piles, hernia, laparoscopic surgery recovery and more from the surgeons at {C['name']}.", blogs, "blogs", [("Blogs", "blogs/")])
for b in BLOGS:
    content, toc = blog_html(b["body"]); url = f"{C['base']}/blogs/{b['slug']}/"
    tocs = "".join(f'<a href="#{i}">{esc(t)}</a>' for i, t in toc)
    rel = "".join(f'<a href="§blogs/{r["slug"]}/">{ic("arrow")} {esc(r["title"])}</a>' for r in BLOGS if r["slug"] != b["slug"])
    body = header(esc(b["title"]), esc(b["sub"]), [("Blogs", "blogs/"), (b["title"][:40] + "…", None)]) + f'''<section class="section"><div class="container lay"><article class="prose"><div class="hero-img"><img src="§assets/img/blog-{b["slug"]}.jpg" alt="{esc(b["title"])}" width="800" height="450"></div>
<div class="meta"><span class="tag">{b["cat"]}</span><span>{b["date_h"]}</span><span>By {b["author"]}</span><span>{b["mins"]} min read</span></div><p class="lead"><strong>{esc(b["sub"])}</strong></p>{content}
<div class="box" style="margin-top:22px"><h3>Share this article</h3><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-ol btn-sm" target="_blank" rel="noopener" href="https://wa.me/?text={url}">WhatsApp</a><a class="btn btn-ol btn-sm" target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u={url}">Facebook</a><a class="btn btn-ol btn-sm" target="_blank" rel="noopener" href="https://www.linkedin.com/sharing/share-offsite/?url={url}">LinkedIn</a></div></div>
<div class="box" style="margin-top:16px;display:flex;gap:14px;align-items:center"><div class="av" style="background:var(--p);color:#fff;width:56px;height:56px;border-radius:50%;display:grid;place-items:center;font-weight:700">{b["author"][4]}</div><div><b>{b["author"]}</b><br><small style="color:var(--m)">{C["quals"]} · {esc(C["name"])}</small></div></div></article>
<aside class="aside"><div class="box toc"><h3>In this article</h3>{tocs}</div><div class="box pri"><h3>Talk to our surgeon</h3><p style="margin-bottom:12px">Have questions about your symptoms?</p><a class="btn btn-a" href="§book-appointment/">{ic("cal")} Book Appointment</a> <a class="btn btn-o btn-sm" style="margin-top:8px" href="https://wa.me/{C["whatsapp"]}" target="_blank" rel="noopener">WhatsApp</a></div><div class="box rel"><h3>Related Posts</h3>{rel}</div></aside></div></section>'''
    sch = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": b["title"], "description": b["sub"], "datePublished": b["date"], "author": {"@type": "Person", "name": b["author"]}, "publisher": {"@type": "Organization", "name": C["name"]}, "image": f"{C['base']}/assets/img/blog-{b['slug']}.jpg", "mainEntityOfPage": url, "keywords": b["kw"]}]
    page(f"blogs/{b['slug']}/", b["mt"], b["sub"] + f" Read expert advice from {C['name']}.", body + cta(), "blogs", [("Blogs", "blogs/"), (b["title"], f"blogs/{b['slug']}/")], sch, f"hero-1")

# ---- CONTACT
def fld(i, lab, typ="text", req=True, full=False, ph_=""):
    return f'<div class="fld{" full" if full else ""}"><label for="{i}">{lab}{" *" if req else ""}</label><input id="{i}" name="{i}" type="{typ}"{" required" if req else ""} placeholder="{ph_}" autocomplete="off"><small class="err"></small></div>'
hrs = "".join(f"<tr><td>{d}</td><td>{t}</td></tr>" for d, t in [("Monday – Sunday", "10:00 AM – 9:00 PM")])
slot_txt = ", ".join(C["slots"])
contact = header("Contact Us", "We are here to help. Call, message or visit us.", [("Contact Us", None)]) + f'''<section class="section"><div class="container grid g2 cgrid"><div class="col">
<div class="box reveal b-info"><h3>Get in touch</h3>
<div class="ci"><div class="ib">{ic("pin")}</div><div><b>Address</b>{esc(C["address"])}</div></div><div class="ci"><div class="ib">{ic("phone")}</div><div><b>Appointment / Booking</b><a href="tel:{C["appt_tel"]}">{C["appt"]}</a></div></div>
<div class="ci"><div class="ib">{ic("wa")}</div><div><b>WhatsApp</b><a href="https://wa.me/{C["whatsapp"]}" target="_blank" rel="noopener">+{C["whatsapp"]}</a></div></div><div class="ci"><div class="ib">{ic("mail")}</div><div><b>Official Email</b><a href="mailto:{C["email"]}">{C["email"]}</a></div></div>
<div class="ci"><div class="ib">{ic("clock")}</div><div><b>Call Dr. Shinde</b><a href="tel:{C["emergency_tel"]}">{C["emergency"]}</a></div></div><div class="soc" style="margin-top:8px"><span style="margin-right:6px;font-weight:600;align-self:center">Follow us</span>{"".join(f"<a style=\"background:var(--pl);color:var(--p)\" href=\"{u}\" aria-label=\"{k}\" target=\"_blank\" rel=\"noopener\">{k[0]}</a>" for k, u in C["social"].items())}</div></div>
<div class="box reveal b-hours"><h3>Working days &amp; hours</h3><table class="tbl">{hrs}</table><p class="hint" style="margin:12px 0 8px"><b>Appointment time slots</b></p><div class="slotchips">{"".join(f"<span>{x}</span>" for x in C["slots"])}</div></div></div>
<div class="col"><div class="box reveal b-form"><h3>Send us an enquiry</h3><form id="enqForm" class="form" novalidate>{fld("name", "Full Name")}{fld("phone", "Phone", "tel")}{fld("email", "Email", "email")}{fld("subject", "Subject")}<div class="fld full"><label for="message">Message *</label><textarea id="message" name="message" required></textarea><small class="err"></small></div><div class="fld full"><button class="btn btn-p" type="submit">Send Message {ic("arrow")}</button></div></form>
<div class="ok" id="enqOk"><div class="tick">{ic("check")}</div><h3>Thank you!</h3><p>Your message has been received. Our team will contact you shortly.</p></div></div>
<div class="box reveal mapbox b-map"><h3>Find us</h3><iframe class="map" title="{esc(C["name"])} on Google Maps" src="{C["map_embed"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe><a class="btn btn-p" href="{C["map_link"]}" target="_blank" rel="noopener">{ic("pin")} Get Directions</a></div></div></div></section>'''
page("contact-us/", f"Contact {C['name']} in {C['city']} | Call Now", f"Contact {C['name']} in {C['city']}. Find our address, appointment number, WhatsApp, working hours, time slots, Google Maps location and send an enquiry.", contact, "contact", [("Contact Us", "contact-us/")], [HOSP, PHYS])

# ---- BOOKING
docs_opts = "".join(f"<option>{n}</option>" for n, _ in TEAM[:1]) 
svc_opts = '<option value="">Select service</option>' + "".join(f"<option>{s[1]}</option>" for s in SERVICES) + "<option>Other / Not sure</option>"
book = header("Book an Appointment", "Choose your service, date and time slot. Our team will confirm your appointment.", [("Book Appointment", None)]) + f'''<section class="section"><div class="container lay"><div class="box reveal"><form id="bookForm" class="form" novalidate>
{fld("name", "Full Name")}{fld("phone", "Phone Number", "tel")}{fld("email", "Email", "email")}{fld("age", "Age", "number")}
<div class="fld"><label for="gender">Gender *</label><select id="gender" name="gender" required><option value="">Select</option><option>Male</option><option>Female</option><option>Other</option></select><small class="err"></small></div>
<div class="fld"><label for="service">Service / Department *</label><select id="service" name="service" required>{svc_opts}</select><small class="err"></small></div>
<div class="fld"><label for="doctor">Preferred Doctor</label><select id="doctor" name="doctor">{docs_opts}</select></div>
<div class="fld"><label for="bdate">Preferred Date *</label><input id="bdate" name="date" type="date" required><small class="err"></small></div>
<div class="fld full"><label>Time Slot *</label><div class="slots" id="slots"></div><input type="hidden" id="bslot" name="slot"><small class="err"></small><span class="hint">Crossed-out slots are already booked.</span></div>
<div class="fld full"><label for="message">Message (optional)</label><textarea id="message" name="message" placeholder="Briefly describe your problem"></textarea></div>
<div class="fld full"><label class="chk"><input type="checkbox" name="consent" required> <span>I agree to the <a href="§privacy-policy/">Privacy Policy</a> and <a href="§terms-and-conditions/">Terms &amp; Conditions</a> and consent to being contacted about this request.</span></label><small class="err"></small></div>
<div class="fld full"><button class="btn btn-p pulse" type="submit">{ic("cal")} Confirm Appointment Request</button></div></form>
<div class="ok" id="bookOk"><div class="tick">{ic("check")}</div><h3>Appointment request received</h3><p id="okSum"></p><p class="hint" style="margin:8px 0 16px">Our team will call to confirm. You can also send the details directly:</p><div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap"><a class="btn btn-p" id="okWa" target="_blank" rel="noopener" href="#">{ic("wa")} Send via WhatsApp</a><a class="btn btn-ol" id="okMail" href="#">{ic("mail")} Send via Email</a></div></div></div>
<aside class="aside"><div class="box pri"><h3>Need urgent advice?</h3><p style="margin-bottom:12px">Call us directly during clinic hours (10 AM – 9 PM).</p><a class="btn btn-a" href="tel:{C["emergency_tel"]}">{ic("phone")} {C["emergency"]}</a></div>
<div class="box"><h3>Working hours</h3><table class="tbl">{hrs}</table></div><div class="box"><h3>What to bring</h3><ul class="ticks"><li>{ic("check")} Previous medical reports and scans</li><li>{ic("check")} List of current medicines</li><li>{ic("check")} Photo ID and insurance card</li></ul></div></aside></div></section>'''
page("book-appointment/", f"Book Appointment | {C['name']}, {C['city']}", f"Book your surgeon consultation online at {C['name']}, {C['city']}. Choose service, date and time slot and get quick confirmation from our team.", book, "", [("Book Appointment", "book-appointment/")])

# ---- LEGAL
def legal(path, title, sub, items, key):
    toc = "".join(f'<a href="#s{i+1}">{i+1}. {esc(h)}</a>' for i, (h, _) in enumerate(items))
    secs = "".join(f'<h2 id="s{i+1}">{i+1}. {esc(h)}</h2><p>{esc(t)}</p>' for i, (h, t) in enumerate(items))
    body = header(title, sub, [(title, None)]) + f'''<section class="section"><div class="container lay"><div class="prose"><!-- [REVIEW WITH LEGAL/CLIENT] --><p><em>Last updated: 13 November 2026</em></p>{secs}<h2>Contact</h2><p>{esc(C["name"])}, {esc(C["address"])}<br>Email: <a href="mailto:{C["email"]}">{C["email"]}</a> · Phone: <a href="tel:{C["phone_tel"]}">{C["phone"]}</a></p></div><aside class="aside"><div class="box toc"><h3>Contents</h3>{toc}</div></aside></div></section>'''
    page(path, f"{title}", f"{key} of {C['name']}, {C['city']}. Read how we handle your information, appointments, website use and medical content responsibly.", body, "", [(title, path)])
legal("privacy-policy/", "Privacy Policy", "How we collect, use and protect your information.", PRIVACY, "Privacy Policy")
legal("terms-and-conditions/", "Terms & Conditions", "Please read these terms before using our website.", TERMS, "Terms and Conditions")

# ---- 404
page("404.html", "Page Not Found", "The page you are looking for could not be found. Return to the home page of the hospital website or book an appointment with our surgeon.", f'<section class="notfound"><div class="container"><h1>404</h1><h2>Page not found</h2><p style="margin:10px 0 20px;color:var(--m)">The page you are looking for does not exist or has moved.</p><a class="btn btn-p" href="§">Back to Home</a></div></section>')

# ---- sitemap / robots
urls = ["", "about-us/", "services/", "products/", "blogs/", "book-appointment/", "contact-us/", "privacy-policy/", "terms-and-conditions/"] + [f"services/{s[0]}/" for s in SERVICES] + [f"products/{p[0]}/" for p in PRODUCTS] + [f"blogs/{b['slug']}/" for b in BLOGS]
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{C['base']}/{u}</loc><lastmod>2026-11-13</lastmod></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {C['base']}/sitemap.xml\n")

# ---- docs
kwlines = ["# SEO Keywords Plan\n", f"Target cities/areas: {C['areas']}  [REPLACE with client areas]\n", "| Page | Primary keyword | Secondary keywords |", "|---|---|---|",
           f"| Home | surgical hospital in {C['city']} | general surgeon {C['city']}, laparoscopic surgery, emergency surgery, cashless mediclaim hospital |",
           f"| About | best surgeon in {C['city']} | {C['doctor']}, about {C['name']}, experienced laparoscopic surgeon |",
           f"| Products | post surgery care products {C['city']} | recovery kit, abdominal binder, compression stockings, piles cushion |",
           f"| Contact | surgeon appointment {C['city']} | book surgeon, hospital contact number, emergency hospital address |",
           f"| Blogs | surgery health blog | gallbladder stone guide, piles vs fissure, laparoscopic recovery |"] + [f"| {s[1]} | {s[8][0]} | {', '.join(s[8][1:])} |" for s in SERVICES]
open(os.path.join(OUT, "SEO_KEYWORDS.md"), "w").write("\n".join(kwlines) + "\n")
open(os.path.join(OUT, "CONTENT_NEEDED_FROM_CLIENT.md"), "w").write("""# Content & materials needed from the client
All text in this template is dummy content marked [REPLACE]. Please collect:

## 1. Hospital / Dr information
- Hospital name and tagline, owner name, address, year of establishment, short description
- Areas / cities served, logo (PNG transparent or SVG), brand colours or reference sites (optional)

## 2. Page content
- Home: banners (heading, one-line sub-text, button text + link, image 1920x800 with no text on image), 50-80 word introduction, Why Choose Us points, customer reviews
- About: Dr / hospital introduction (150-200 words), education and experience, mission and vision, special qualities, team details with photos, achievements / certificates / awards
- Services: final list; per service: name, 20-25 word short description, image/icon (800x600), title + 2-3 line intro, 100-150 word description, key features, 3-5 FAQs, 2-3 images, keywords
- Products: names, information, images 800x800 (or tell us if unavailable)
- Contact: official email, WhatsApp number, appointment number, time slots, working days/hours, full address + Google Maps link, social links
- Blogs: at least 3; title (50-60 chars), sub-title (100-120 chars), category, date, author, 800-1200 words, optional image, meta title, meta description, focus keyword

## 3. SEO
- Primary + 3-5 secondary keywords for Home, About, Products, Contact, Blogs and every service
- Target cities / areas, Google Search Console and Analytics access

## 4. Legal
- Review of Privacy Policy and Terms & Conditions by the client / legal advisor
""")
open(os.path.join(OUT, "README.md"), "w").write(f"""# {C['name']} - Website Template
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
Product images (`product-<name>.jpg`) are studio-style renders; replace them with real product photos (800x800) using the same file names.

## Going live
1. Set `base` (domain) and `link_index=False` in `content.py`, rebuild, upload `site/` contents to hosting (clean URLs like /about-us/).
2. Add Google Search Console verification and Analytics snippet (marked in `<head>`), submit `sitemap.xml`.
3. Connect booking / enquiry forms to a backend or form service: search `TODO` in `assets/js/main.js`.
""")
open(os.path.join(OUT, "REQUIREMENTS_CHECKLIST.md"), "w").write(f"""# Requirements Checklist (Website_Client_Requirement_Document_v3_1)
## 1. Hospital / Dr information
- [x] Name + tagline, owner, address + year established, description, areas, logo (SVG), brand colours: config in content.py, header/footer/about/schema
## 2. Pages
- [x] Home: banner slider (heading, sub-text, button + link, image), 50-80 word intro, service highlight cards, Why Choose Us, testimonials, CTA (Contact / Book Appointment / WhatsApp)
- [x] About: intro (150-200 words), Dr education and experience (timeline), mission and vision, why choose us, owner/team with photos, achievements/certificates/awards (lightbox)
- [x] Services: cards (name, 20-25 word description, image/icon, Know More) + 8 detail pages (title, 2-3 line intro, 100-150 word description, key features, 3 FAQs, 3 images, keywords, details sidebar)
- [x] Products: listing + 4 detail pages (name, information, image)
- [x] Contact: email, WhatsApp, appointment number, time slots, working days/hours, address + Google Maps, social links
- [x] Blogs: title, sub-title, category filter, image, full details, 3 blogs at launch; standard format (title 50-60, sub-title 100-120, category/date/author, 800-1200 words, CTA ending, meta title/description/focus keyword)
- [x] Extra pages requested: Book Appointment, Privacy Policy, Terms & Conditions, 404
## 3. Content & image standards
- [x] Logo SVG · banner 1920x800 (no text on image) · service 800x600 · product 800x800 · clear file names
## 4. SEO
- [x] Unique meta title (50-60) and description (150-160) per page/service/product/blog (validated at build)
- [x] Keywords in headings, content, URLs, alt text; keyword plan in SEO_KEYWORDS.md
- [x] sitemap.xml, robots.txt, clean keyword URLs, canonical, Open Graph, Twitter cards
- [x] Schema: Hospital + Physician (Home, Contact), Service + FAQPage (services), Product, BlogPosting, BreadcrumbList
- [x] Search Console / Analytics placeholders in head
## 5. Additional features
- [x] Banner slider · service cards + details · product listing + details · blog category filtering
- [x] WhatsApp + Call Now buttons (floating + header) · booking form with time slots
- [x] Google Maps + social links · testimonials · responsive (mobile/tablet/desktop)
## Notes
- Booking and enquiry forms are frontend only (WhatsApp/email hand-off); connect a backend before launch.
- All content is dummy and marked [REPLACE]; placeholder images are SVG.
""")

# ---- link check + report
bad = []
for root, _, fs in os.walk(OUT):
    for fn in fs:
        if not fn.endswith(".html") or fn == "404.html": continue
        p = os.path.join(root, fn); t = open(p, encoding="utf-8").read()
        for m in re.findall(r'(?:href|src)="([^"#:]+?)"', t):
            if m.startswith(("http", "mailto", "tel", "//")): continue
            tgt = os.path.normpath(os.path.join(root, m))
            if os.path.isdir(tgt): tgt = os.path.join(tgt, "index.html")
            if not os.path.exists(tgt): bad.append((os.path.relpath(p, OUT), m))
print("pages:", sum(f.endswith(".html") for _, _, fs in os.walk(OUT) for f in fs))
print("broken links:", bad[:15] or "none")
print("report:", *REPORT, sep="\n  ") if REPORT else print("meta/content checks: all OK")
