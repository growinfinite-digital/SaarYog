#!/usr/bin/env python3
"""SaarYog static site generator. Run: python3 build.py  -> writes HTML/sitemap/robots next to this file.
Edit BASE_URL + the TODO items below, then rebuild. Output is plain HTML/CSS/JS (GitHub Pages ready)."""
import json, os, html
ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://YOUR-DOMAIN.com"      # TODO: custom domain or https://<user>.github.io/<repo>
PHONE, TEL = "90493 00831", "+919049300831"
WA = "919049300831"
# TODO: PLACEHOLDER testimonials - replace with real client reviews before launch (do not publish as-is)
REVIEWS = [
 {"name": "Anita K.", "text": "I joined the general batch for back stiffness and feel lighter and calmer within weeks. The teachers correct every posture patiently.", "program": "General Yoga"},
 {"name": "Rahul M.", "text": "The weight-loss batch kept me consistent. The diet sessions and the daily routine made it easy to follow.", "program": "Weight Loss Batch"},
 {"name": "Sunita P.", "text": "My father attends the seniors batch and looks forward to it every morning. The pace and the Om chanting suit him well.", "program": "Yoga for Seniors"},
]
GBP = {"v": "https://g.co/kgs/w93FZ5W",
       "d": "https://www.google.com/localservices/profile?spp=Cg0vZy8xMXZ3bG5nbGZ6&scp=CgAaDVNhYXJZb2cgQ2xhc3MqDVNhYXJZb2cgQ2xhc3M%3D&q=SaarYog%20Class&source=sh%2Fx%2Floc%2Fsrv%2Fm1%2F0&kgs=293f480625a9576a"}
e = html.escape

def prog(icon, name, days, times, fees, items, note=""):
    return dict(icon=icon, name=name, days=days, times=times, fees=fees, items=items, note=note)

GEN = ["Micro yoga", "Asanas", "Sun salutation", "Pranayam", "Meditation", "Shuddhi kriya (cleansing)", "Knowledge session"]
WL = ["Asanas and pranayam for weight reduction", "Shuddhi kriya for weight loss", "Yog nidra", "Mudras for weight loss", "Diet session", "Special diet for two days a week", "Knowledge session", "Unique preparatory movements", "Dedicated weight-loss batch"]
SR = ["Asanas, pranayam, meditation and preparatory movements suited to seniors", "Shuddhi kriya", "Fun activities", "Knowledge session", "Om chanting"]
KD = ["Unique preparatory movements", "Sun salutation", "Moon salutation", "Asanas to support height growth", "Pranayam", "Om chanting", "Fun, creative activities", "Right-brain development process"]
PN = ["Asanas", "Pranayam", "Meditation", "Garbh sanskar", "Knowledge session"]
THERAPY_FOR = ["High blood pressure", "Diabetes", "Spine care", "Spondylitis, neck and lumbar pain", "Sciatica", "Abdominal problems", "Yoga for Her", "Increase children's height", "Pranayam & meditation program"]

BR = {
 "v": dict(slug="vishal-nagar.html", name="Vishal Nagar", full="SaarYog – Vishal Nagar (Pimple Nilakh, Wakad)",
   street="Above Dr. Sanap's Laxmi Polyclinic, Laxmi Clinic Vishal Nagar, Jagtap Dairy Rd", locality="Wakad, Pune", zip="411027",
   areas=["Vishal Nagar", "Pimple Nilakh", "Wakad"],
   title="Yoga Classes in Vishal Nagar, Pimple Nilakh & Wakad, Pune | SaarYog",
   desc="SaarYog yoga classes in Vishal Nagar near Pimple Nilakh & Wakad, Pune: general yoga, weight loss, seniors, kids, prenatal and 1-to-1 yoga therapy by Dr. Yogeshwar Sanap. Call or WhatsApp 90493 00831.",
   h1="Yoga Classes in Vishal Nagar, Pimple Nilakh &amp; Wakad",
   lead="Daily batches for everyone, from weight loss and seniors to kids, prenatal and yoga therapy, above Laxmi Polyclinic, Jagtap Dairy Rd.",
   progs=[
    prog("yoga", "General Yoga Batch", "Mon – Fri", ["8:00 – 9:00 AM", "9:00 – 10:00 AM", "6:30 – 7:30 PM"], "₹2,000 first month · ₹1,500 from 2nd month", GEN, "Open for all"),
    prog("flame", "Weight Loss Batch (21 days)", "Mon – Sat", ["6:30 – 8:00 AM", "7:30 – 9:00 PM"], "₹3,000 / month · ₹7,500 / 3 months", WL, "Targeted 21-day program. Results vary with consistency and diet."),
    prog("leaf", "Yoga for Seniors", "Mon – Fri", ["9:00 – 10:00 AM"], "₹2,000 first month · ₹1,200 from 2nd month", SR),
    prog("kids", "Kids Yoga", "Mon – Fri", ["5:30 – 6:15 PM"], "₹1,500 first month · ₹1,200 from 2nd month", KD),
    prog("heart", "Prenatal Yoga & Garbh Sanskar", "Call for days", ["10:30 – 11:30 AM"], "₹3,000 · 12 sessions / month", PN),
    prog("plus", "Yoga Therapy (1-to-1)", "By appointment", ["Customised to you"], "₹1,000 / session · ₹15,000 for 21 days (paid in advance)", ["21 days of one-to-one customised sessions", "Customised yog nidra", "For BP, diabetes, back and neck pain, sciatica, abdominal issues, pregnancy and more"]),
    prog("home", "Yoga at Home", "Mon – Fri", ["Teacher visits your home"], "₹700 / day · ₹3,200 / week · ₹12,000 / month", GEN),
   ],
   gbp=GBP["v"], map_q="SaarYog+Class+Laxmi+Polyclinic+Vishal+Nagar+Wakad+Pune"),
 "d": dict(slug="dange-chowk.html", name="Dange Chowk", full="SaarYog – Dange Chowk (Wakad Road)",
   street="Metropole, 3rd Floor, Wakad Road, Datta Mandir Road, Dange Chowk Rd", locality="Thergaon, Pune", zip="411033",
   areas=["Wakad", "Dange Chowk", "Thergaon"],
   title="Yoga Classes in Wakad & Dange Chowk, Pune | SaarYog",
   desc="SaarYog yoga classes near Wakad & Dange Chowk, Pune: general yoga, dynamic weight-loss batch, seniors, kids, prenatal and 1-to-1 yoga therapy. Call or WhatsApp 90493 00831.",
   h1="Yoga Classes in Wakad &amp; Dange Chowk, Pune",
   lead="Morning and evening batches on Wakad Road, Dange Chowk, guided by Dr. Yogeshwar Sanap and the SaarYog team.",
   progs=[
    prog("yoga", "General Yoga Batch", "Mon – Fri", ["7:30 – 8:30 AM", "8:30 – 9:30 AM", "6:00 – 7:00 PM"], "₹1,500 first month · ₹1,200 from 2nd month", GEN, "Open for all"),
    prog("flame", "Dynamic Yoga (Weight Loss)", "Mon – Sat", ["6:30 – 7:30 AM", "7:00 – 8:00 PM"], "₹2,000 first month · ₹1,500 from 2nd month", WL, "Targeted 21-day program. Results vary with consistency and diet."),
    prog("leaf", "Yoga for Seniors", "Mon – Fri", ["9:30 – 10:30 AM"], "₹1,500 first month · ₹1,200 from 2nd month", SR),
    prog("kids", "Kids Yoga", "Mon – Fri", ["5:15 – 6:00 PM"], "₹1,500 first month · ₹1,200 from 2nd month", KD),
    prog("heart", "Prenatal Yoga & Garbh Sanskar", "3 or 5 days / week", ["10:30 – 11:30 AM"], "₹3,000 (3 days/week, 12 sessions) · ₹6,000 (5 days/week)", PN),
    prog("plus", "Yoga Therapy (1-to-1)", "By appointment", ["Customised to you"], "₹700 / session · ₹12,000 for 21 days (paid in advance)", ["21 days of one-to-one customised sessions", "Customised yog nidra", "For BP, diabetes, back and neck pain, sciatica, abdominal issues and more"]),
   ],
   gbp=GBP["d"], map_q="SaarYog+Class+Metropole+Dange+Chowk+Wakad+Road+Pune"),
}


def _p(d): return f'<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
ICONS = {
 "phone": _p('<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>'),
 "wa": _p('<path d="M3 21l1.6-4.7A8.5 8.5 0 1 1 8 19.5z"/><path d="M9 9.5c0 3 2.5 5.5 5.5 5.5l1-1.2-2-1-.8.7c-.8-.4-1.5-1.1-1.9-1.9l.7-.8-1-2z"/>'),
 "pin": _p('<path d="M12 22s7-6.1 7-12a7 7 0 0 0-14 0c0 5.9 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>'),
 "star": '<svg class="ic star" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.7 5 1.7 7.4L12 18l-6.5 4 1.7-7.4-5.7-5L9 8.9z"/></svg>',
 "yoga": _p('<circle cx="12" cy="5" r="2.2"/><path d="M12 8v5M12 13l-5 4h10zM7 17l-3 2M17 17l3 2M8 10.5l4 1.5 4-1.5"/>'),
 "flame": _p('<path d="M12 22c4 0 7-2.8 7-6.8 0-3.3-2.3-5.4-3.6-7.2-.6 1.3-1.4 2-2.4 2.4.3-3-.6-5.8-3-8.4-.4 3.2-1.8 5.1-3.3 7C5.2 10.9 5 12.8 5 15.2 5 19.2 8 22 12 22z"/>'),
 "leaf": _p('<path d="M20 4C9 4 4 9 4 15c0 2 .7 3.6 1.8 4.8C7 20.6 8.700 21 10 21c6 0 10-5 10-17z"/><path d="M4 21c2-6 6-9 10-11"/>'),
 "kids": _p('<circle cx="12" cy="12" r="9"/><path d="M8.500 14a4 4 0 0 0 7 0"/><path d="M9 9.500h.01M15 9.500h.01"/>'),
 "heart": _p('<path d="M12 21s-8-5-8-11a4.500 4.500 0 0 1 8-2.800A4.500 4.500 0 0 1 20 10c0 6-8 11-8 11z"/>'),
 "plus": _p('<rect x="3" y="3" width="18" height="18" rx="4"/><path d="M12 8v8M8 12h8"/>'),
 "home": _p('<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>'),
 "clock": _p('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
 "img": _p('<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.800"/><path d="M21 16l-5-5-8 9"/>'),
}
def ic(n): return ICONS[n]

def wa_link(msg): return f"https://wa.me/{WA}?text=" + msg.replace(" ", "%20")
def btns(msg, cls=""):
    return (f'<a class="btn btn-solid {cls}" href="tel:{TEL}" data-cta="call">{ic("phone")} Call Now</a>'
            f'<a class="btn btn-wa {cls}" href="{wa_link(msg)}" target="_blank" rel="noopener" data-cta="whatsapp">{ic("wa")} WhatsApp Now</a>')

LOGO_OLD = '<svg viewBox="0 0 48 48" width="38" height="38" aria-hidden="true"><circle cx="24" cy="24" r="22" fill="none" stroke="#DB9543" stroke-width="2"/><circle cx="24" cy="13" r="4" fill="#DB9543"/><path d="M24 18c-5 0-8 3-9 8l-5 5 6 1 8-3 8 3 6-1-5-5c-1-5-4-8-9-8z" fill="#DB9543"/></svg>'

HERO_SVG = '''<svg class="yoga-anim" viewBox="0 0 400 400" role="img" aria-label="Animated figure meditating in lotus pose">
<g class="aura"><circle cx="200" cy="190" r="150"/><circle cx="200" cy="190" r="115"/><circle cx="200" cy="190" r="80"/></g>
<g class="petal"><ellipse cx="70" cy="300" rx="8" ry="14"/><ellipse cx="335" cy="120" rx="7" ry="12"/><ellipse cx="320" cy="310" rx="6" ry="11"/><ellipse cx="85" cy="110" rx="6" ry="10"/></g>
<g class="figure"><circle cx="200" cy="118" r="26" fill="#DB9543"/>
<path d="M200 148c-34 0-52 24-56 60l-26 40 34 8 48-18 48 18 34-8-26-40c-4-36-22-60-56-60z" fill="#DB9543"/>
<path d="M118 262c30 30 134 30 164 0-14 26-48 38-82 38s-68-12-82-38z" fill="#b97a2e"/>
<path d="M150 200l-34 52M250 200l34 52" stroke="#fff" stroke-width="5" stroke-linecap="round"/></g>
<circle class="om" cx="200" cy="340" r="4" fill="#DB9543"/></svg>'''

ABOUT_SVG = '''<svg viewBox="0 0 400 300" class="about-art" role="img" aria-label="Illustration of yoga practice"><rect width="400" height="300" rx="18" fill="#fdf3e6"/><circle cx="200" cy="140" r="90" fill="none" stroke="#DB9543" stroke-width="2" stroke-dasharray="4 8"/><circle cx="200" cy="95" r="20" fill="#DB9543"/><path d="M200 120c-28 0-42 20-45 46l-22 32 28 6 39-14 39 14 28-6-22-32c-3-26-17-46-45-46z" fill="#DB9543"/><text x="200" y="272" text-anchor="middle" font-size="16" fill="#8a5a1e" font-family="Georgia,serif">TODO: replace with a real studio / teacher photo</text></svg>'''

def header(page):
    nav = [("index.html", "Home"), ("vishal-nagar.html", "Vishal Nagar"), ("dange-chowk.html", "Dange Chowk"), ("#programs", "Programs"), ("#about", "About"), ("#gallery", "Gallery"), ("#contact", "Contact")]
    items = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in nav)
    msg = "Hi SaarYog, I would like to know about yoga classes."
    return f'''<header class="site-header"><div class="wrap bar"><a class="logo" href="index.html" aria-label="SaarYog home"><img class="logo-img" src="assets/logo.png" width="48" height="48" alt="SaarYog logo"><span>Saar<b>Yog</b></span></a>
<nav id="nav" aria-label="Main"><ul>{items}</ul></nav><div class="hdr-cta">{btns(msg, "sm")}</div>
<button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button></div></header>'''

def prog_card(p):
    times = "".join(f"<li>{e(t)}</li>" for t in p["times"])
    its = "".join(f"<li>{e(i)}</li>" for i in p["items"])
    note = f'<p class="note">{e(p["note"])}</p>' if p["note"] else ""
    return f'''<article class="card prog"><div class="ico">{ic(p["icon"])}</div><h3>{e(p["name"])}</h3><p class="meta"><b>{e(p["days"])}</b></p>
<ul class="times">{times}</ul><p class="fee">{e(p["fees"])}</p>{note}<details><summary>What's included</summary><ul>{its}</ul></details></article>'''

def reviews_html(b):
    if REVIEWS:
        cards = "".join(f'<figure class="card review"><div class="stars">{ic("star")*5}</div><blockquote>{e(r["text"])}</blockquote><figcaption><b>{e(r["name"])}</b> · {e(r.get("program",""))}</figcaption></figure>' for r in REVIEWS)
        return f'<div class="grid g3">{cards}</div>'
    return f'<div class="card center"><p>See what our students say about SaarYog on Google.</p><a class="btn btn-solid" href="{b}" target="_blank" rel="noopener">{ic("star")} Read Google Reviews</a></div>'

def contact_block(b, msg):
    return f'''<div class="card contact"><iframe class="map" src="https://www.google.com/maps?q={b["map_q"]}&output=embed" title="Map of SaarYog {e(b["name"])} branch" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
<h3>{e(b["name"])} Branch</h3><address>{e(b["street"])}, {e(b["locality"])} {b["zip"]}</address>
<p><a href="tel:{TEL}">{ic("phone")} {PHONE}</a></p><div class="row">{btns(msg)}</div>
<p><a class="link" href="{b["gbp"]}" target="_blank" rel="noopener">{ic("pin")} Get directions on Google</a></p></div>'''

TEAM = '''<ul class="team"><li><b>Dr. Yogeshwar Sanap, MD</b> – Yog Master (YCB 2, 3, 4), Yog Teacher &amp; Evaluator, Therapeutic Yog Consultant, Consulting Family Physician.</li>
<li><b>Dr. Rekha Sanap, MD</b> – Consulting Homoeopath, Yog Teacher, Happiness Program Teacher (Art of Living).</li>
<li><b>Mrs. Surekha Sawant</b> – Yog Teacher.</li></ul>'''


GALLERY = [("gallery-1.jpg", "Morning yoga batch at SaarYog"), ("gallery-2.jpg", "Group asana practice"), ("gallery-3.jpg", "Pranayam and meditation session"),
           ("gallery-4.jpg", "Kids yoga class"), ("gallery-5.jpg", "Yoga for seniors"), ("gallery-6.jpg", "One-to-one yoga therapy session")]
def gallery(place=""):
    t = "".join(f'<a class="gi" href="assets/gallery/{f}" data-lb><img src="assets/gallery/{f}" alt="{e(a)}{place}" width="600" height="450" loading="lazy"></a>' for f, a in GALLERY)
    return f'''<section id="gallery" class="sec"><div class="wrap"><h2>Our Yoga Gallery</h2><p class="sub">A glimpse of life at SaarYog.</p><div class="gallery">{t}</div></div></section>'''

def make_placeholders():
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return
    def mk(path, size, label):
        full = os.path.join(ROOT, path)
        if os.path.exists(full): return          # never overwrite your real images
        os.makedirs(os.path.dirname(full), exist_ok=True)
        im = Image.new("RGB", size, "#fdf3e6"); d = ImageDraw.Draw(im); w_, h_ = size
        d.rectangle([8, 8, w_-9, h_-9], outline="#DB9543", width=3); d.ellipse([w_/2-h_*.12, h_*.3, w_/2+h_*.12, h_*.3+h_*.24], fill="#2196B7")
        d.text((w_/2, h_*.72), label, fill="#8a5a1e", anchor="mm"); im.save(full)
    mk("assets/logo.png", (512, 512), "LOGO 512x512")
    for f, _ in GALLERY: mk("assets/gallery/" + f, (600, 450), "PHOTO " + f)

def about(extra=""):
    return f'''<section id="about" class="sec alt"><div class="wrap split"><div>{ABOUT_SVG}</div><div><h2>About SaarYog</h2>
<p class="tag">Yoga for me, myself.</p><p>SaarYog is a yoga and yoga-therapy centre in Pune led by doctors who are also yoga teachers. Every batch blends asanas, pranayam, meditation and cleansing kriyas with simple knowledge sessions so you learn to care for your own health.</p>{extra}{TEAM}</div></div></section>'''

def jsonld(data): return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + '</script>'

def org_node(k, b):
    return {"@type": ["SportsActivityLocation", "HealthAndBeautyBusiness"], "@id": f"{BASE_URL}/{b['slug']}#business", "name": b["full"], "url": f"{BASE_URL}/{b['slug']}",
            "telephone": TEL, "image": f"{BASE_URL}/assets/og.png", "slogan": "Yoga for me, myself.", "priceRange": "₹₹", "hasMap": b["gbp"],
            "address": {"@type": "PostalAddress", "streetAddress": b["street"], "addressLocality": b["locality"].split(",")[0], "addressRegion": "Maharashtra", "postalCode": b["zip"], "addressCountry": "IN"},
            "areaServed": [{"@type": "Place", "name": a} for a in b["areas"]],
            "founder": {"@type": "Person", "name": "Dr. Yogeshwar Sanap"}}

def faqs(k, b):
    p = b["progs"]
    qs = [(f"What yoga classes does SaarYog offer in {b['name']}?", "General yoga, weight loss, seniors, kids, prenatal yoga, yoga therapy" + (" and yoga at home." if k == "v" else ".")),
          (f"What are the fees for the general yoga batch in {b['name']}?", p[0]["fees"] + "."),
          ("Do you offer one-to-one yoga therapy?", "Yes. Customised one-to-one sessions for health issues such as high blood pressure, diabetes, back and neck pain. " + p[5]["fees"] + "."),
          ("How can I book a class?", f"Call or WhatsApp {PHONE} and we will confirm the batch timing for you.")]
    return qs

def page(k):
    b = BR[k]; other = BR["d" if k == "v" else "v"]
    url = f"{BASE_URL}/{b['slug']}"
    msg = f"Hi SaarYog {b['name']}, I would like to know about yoga classes."
    cards = "".join(prog_card(p) for p in b["progs"])
    tf = "".join(f"<li>{e(t)}</li>" for t in THERAPY_FOR)
    fq = faqs(k, b)
    fq_html = "".join(f"<details class='card faq'><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in fq)
    ld = jsonld({"@context": "https://schema.org", "@graph": [org_node(k, b),
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in fq]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL + "/"}, {"@type": "ListItem", "position": 2, "name": b["name"], "item": url}]}]})
    body = f'''{header(k)}<main>
<section id="home" class="hero"><div class="wrap split"><div><p class="eyebrow">SaarYog · {e(b["name"])} Branch</p><h1>{b["h1"]}</h1><p class="lead">{e(b["lead"])}</p>
<div class="row">{btns(msg, "lg")}</div><p class="small">Yoga for me, myself.</p></div><div>{HERO_SVG}</div></div></section>
<section id="programs" class="sec"><div class="wrap"><h2>Our Yoga Programs in {e(b["name"])}</h2><p class="sub">Batches, timings and fees for the {e(b["name"])} branch.</p><div class="grid g3">{cards}</div>
<div class="card therapy"><h3>Yoga Therapy Programs</h3><p>Programs designed around your health needs:</p><ul class="chips">{tf}</ul></div></div></section>
{about(f"<p>Prefer another location? See our <a class='link' href='{other['slug']}'>{other['name']} branch</a>.</p>")}
{gallery(" in " + b["name"])}
<section id="testimonials" class="sec"><div class="wrap"><h2>What Our Students Say</h2>{reviews_html(b["gbp"])}</div></section>
<section id="faq" class="sec alt"><div class="wrap narrow"><h2>Frequently Asked Questions</h2>{fq_html}</div></section>
<section id="contact" class="sec"><div class="wrap"><h2>Contact Us</h2><div class="grid g2">{contact_block(b, msg)}{contact_block(other, f"Hi SaarYog {other['name']}, I would like to know about yoga classes.")}</div></div></section></main>'''
    return shell(b["title"], b["desc"], url, body, ld, k)

def home():
    url = BASE_URL + "/"
    msg = "Hi SaarYog, I would like to know about yoga classes."
    cards = ""
    for k, b in BR.items():
        cards += f'''<article class="card"><h3>{e(b["name"])} Branch</h3><p>{e(", ".join(b["areas"]))}</p><address>{e(b["street"])}, {e(b["locality"])} {b["zip"]}</address>
<div class="row"><a class="btn btn-solid" href="{b["slug"]}">View {e(b["name"])} Batches</a></div></article>'''
    names = [("yoga", "General Yoga"), ("flame", "Weight Loss"), ("leaf", "Seniors"), ("kids", "Kids"), ("heart", "Prenatal & Garbh Sanskar"), ("plus", "Yoga Therapy")]
    pc = "".join(f'<div class="card center"><div class="ico">{ic(i)}</div><h3>{n}</h3></div>' for i, n in names)
    ld = jsonld({"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": BASE_URL + "/#org", "name": "SaarYog", "url": url, "slogan": "Yoga for me, myself.", "telephone": TEL, "logo": f"{BASE_URL}/assets/logo.png",
         "founder": {"@type": "Person", "name": "Dr. Yogeshwar Sanap"}},
        {"@type": "WebSite", "name": "SaarYog", "url": url},
        org_node("v", BR["v"]), org_node("d", BR["d"])]})
    body = f'''{header("h")}<main><section id="home" class="hero"><div class="wrap split"><div><p class="eyebrow">Wakad · Pimple Nilakh · Vishal Nagar · Dange Chowk</p>
<h1>SaarYog – Yoga Classes in Wakad, Pune</h1><p class="lead">Yoga for me, myself. Doctor-led yoga for weight loss, seniors, kids, pregnancy and health conditions at two convenient Pune branches.</p>
<div class="row">{btns(msg, "lg")}</div></div><div>{HERO_SVG}</div></div></section>
<section id="branches" class="sec"><div class="wrap"><h2>Choose Your Branch</h2><div class="grid g2">{cards}</div></div></section>
<section id="programs" class="sec alt"><div class="wrap"><h2>Our Programs</h2><p class="sub">Timings and fees differ by branch. Pick yours to see details.</p><div class="grid g3">{pc}</div></div></section>
{about()}
{gallery()}
<section id="testimonials" class="sec"><div class="wrap"><h2>What Our Students Say</h2>{reviews_html(GBP["v"])}</div></section>
<section id="contact" class="sec alt"><div class="wrap"><h2>Contact Us</h2><div class="grid g2">{contact_block(BR["v"], "Hi SaarYog Vishal Nagar, I would like to know about yoga classes.")}{contact_block(BR["d"], "Hi SaarYog Dange Chowk, I would like to know about yoga classes.")}</div></div></section></main>'''
    return shell("SaarYog – Yoga Classes in Wakad, Pimple Nilakh & Pune | Yoga for me, myself", "SaarYog yoga and yoga therapy in Wakad, Vishal Nagar, Pimple Nilakh and Dange Chowk, Pune. Weight loss, seniors, kids, prenatal batches. Call or WhatsApp 90493 00831.", url, body, ld, "h")

def shell(title, desc, url, body, ld, k):
    msg = "Hi SaarYog, I would like to know about yoga classes."
    footer = f'''<footer class="site-footer"><div class="wrap grid g3"><div><b>SaarYog</b><p>Yoga for me, myself.</p><p><a href="tel:{TEL}">{ic("phone")} {PHONE}</a></p></div>
<div><b>Branches</b><p><a href="vishal-nagar.html">Yoga in Vishal Nagar, Pimple Nilakh</a></p><p><a href="dange-chowk.html">Yoga in Wakad, Dange Chowk</a></p></div>
<div><b>Quick links</b><p><a href="index.html">Home</a></p><p><a href="#programs">Programs</a></p><p><a href="#contact">Contact</a></p></div></div>
<p class="copy">© <span id="yr">2026</span> SaarYog. All rights reserved.</p></footer>
<div class="mobile-bar"><a href="tel:{TEL}" data-cta="call">{ic("phone")} Call Now</a><a href="{wa_link(msg)}" target="_blank" rel="noopener" data-cta="whatsapp">{ic("wa")} WhatsApp</a></div>'''
    return f'''<!DOCTYPE html><html lang="en-IN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large"><meta name="theme-color" content="#DB9543"><meta name="geo.region" content="IN-MH"><meta name="geo.placename" content="Pune">
<meta property="og:type" content="website"><meta property="og:site_name" content="SaarYog"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta property="og:locale" content="en_IN"><meta property="og:image" content="{BASE_URL}/assets/og.png">
<meta name="twitter:card" content="summary_large_image"><link rel="icon" href="assets/logo.png" type="image/png"><link rel="stylesheet" href="assets/style.css">{ld}</head>
<body>{body}{footer}<script src="assets/main.js" defer></script></body></html>'''

CSS = ''':root{--o:#DB9543;--od:#b97a2e;--t:#2196B7;--td:#176f88;--ink:#2b1d0e;--mut:#6b5a47;--bg:#fff;--alt:#fdf6ec;--r:16px}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:80px}body{margin:0;font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg)}
a{color:inherit}.wrap{max-width:1160px;margin:auto;padding:0 20px}.narrow{max-width:760px}h1,h2,h3{line-height:1.2;margin:.2em 0 .5em}h1{font-size:clamp(2rem,5vw,3.2rem)}h2{font-size:clamp(1.6rem,3.5vw,2.2rem)}h2::after{content:'';display:block;width:56px;height:4px;border-radius:4px;background:var(--t);margin-top:8px}
.site-header{position:sticky;top:0;z-index:50;background:#fff;border-bottom:1px solid #f0e2cf}.bar{display:flex;align-items:center;gap:16px;min-height:68px}
.logo-img{width:48px;height:48px;object-fit:cover;border-radius:10px}.logo{display:flex;align-items:center;gap:8px;text-decoration:none;font:700 1.4rem Georgia,serif}.logo b{color:var(--o)}nav{margin-left:auto}nav ul{display:flex;gap:18px;list-style:none;margin:0;padding:0}nav a{text-decoration:none;font-weight:500}nav a:hover{color:var(--od)}
.hdr-cta{display:flex;gap:8px}.btn{display:inline-block;padding:11px 20px;border-radius:999px;font-weight:600;text-decoration:none;border:2px solid var(--o);transition:.2s}
.btn.sm{padding:8px 14px;font-size:.9rem}.btn.lg{padding:14px 26px;font-size:1.05rem}.btn-solid{background:var(--o);color:var(--ink)}.btn-wa{background:#fff;color:var(--ink)}.btn:hover{transform:translateY(-2px);box-shadow:0 6px 16px rgba(219,149,67,.35)}
.burger{display:none;background:none;border:0;padding:8px;cursor:pointer}.burger span{display:block;width:24px;height:2px;background:var(--ink);margin:5px 0;transition:.2s}
.hero{padding:56px 0;background:linear-gradient(180deg,#fff,var(--alt))}.split{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}.eyebrow{color:var(--od);font-weight:600;letter-spacing:.04em}.lead{font-size:1.15rem;color:var(--mut)}.row{display:flex;flex-wrap:wrap;gap:12px;margin:18px 0}.small,.tag{color:var(--od);font-style:italic}
.sec{padding:64px 0}.alt{background:var(--alt)}.sub{color:var(--mut);margin-top:-.2em}.grid{display:grid;gap:20px;margin-top:24px}.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}
.card{background:#fff;border:1px solid #f0e2cf;border-radius:var(--r);padding:22px;box-shadow:0 4px 18px rgba(219,149,67,.08)}.center{text-align:center}.ico{color:var(--t)}.ico .ic{width:34px;height:34px}.ic{width:1.15em;height:1.15em;vertical-align:-.2em;flex:none}.btn .ic{margin-right:4px}.star{color:var(--o)}.stars{margin-bottom:6px}.prog h3{margin:.3em 0}.times{padding-left:18px;margin:.3em 0}.fee{font-weight:700;color:var(--od)}.note{font-size:.9rem;color:var(--mut)}
details summary{cursor:pointer;font-weight:600;margin-top:8px}details ul{padding-left:18px}.faq{margin:10px 0;padding:14px 20px}.therapy{margin-top:24px}.chips{display:flex;flex-wrap:wrap;gap:8px;list-style:none;padding:0}.chips li{background:var(--alt);border:1px solid var(--t);border-radius:999px;padding:6px 14px}
.about-art,.yoga-anim{width:100%;height:auto;display:block}.team{padding-left:18px}.link{color:var(--td);font-weight:600}.link:hover{text-decoration:underline}address{font-style:normal;color:var(--mut)}blockquote{margin:0 0 8px}
.site-footer{background:#2b1d0e;color:#f6e9d6;padding:40px 0 20px}.site-footer a{text-decoration:none}.copy{text-align:center;margin-top:24px;font-size:.85rem}.mobile-bar{display:none}
.aura circle{fill:none;stroke:var(--o);stroke-opacity:.35;transform-origin:200px 190px;animation:pulse 5s ease-in-out infinite}.aura circle:nth-child(2){animation-delay:.8s}.aura circle:nth-child(3){animation-delay:1.6s}
.figure{transform-origin:200px 300px;animation:breathe 5s ease-in-out infinite}.petal ellipse{fill:var(--o);opacity:.5;animation:float 6s ease-in-out infinite}.petal ellipse:nth-child(2n){animation-delay:1.5s}.om{animation:pulse 5s infinite;transform-origin:200px 340px}
@keyframes pulse{0%,100%{transform:scale(.92);opacity:.4}50%{transform:scale(1.08);opacity:1}}@keyframes breathe{0%,100%{transform:scale(1)}50%{transform:scale(1.035) translateY(-4px)}}@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;scroll-behavior:auto}}
@media(max-width:900px){.g3{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr}.hero .split>div:last-child{max-width:340px;margin:auto}
.burger{display:block;margin-left:auto}.hdr-cta{display:none}nav{position:absolute;top:68px;left:0;right:0;background:#fff;border-bottom:1px solid #f0e2cf;display:none;padding:12px 20px}nav.open{display:block}nav ul{flex-direction:column;gap:12px}}
@media(max-width:600px){.g2,.g3{grid-template-columns:1fr}body{padding-bottom:58px}.mobile-bar{display:flex;position:fixed;bottom:0;left:0;right:0;z-index:60;box-shadow:0 -4px 16px rgba(0,0,0,.12)}.mobile-bar a{flex:1;text-align:center;padding:15px;font-weight:700;text-decoration:none;background:var(--o);color:var(--ink)}.mobile-bar a+a{background:#fff;border-top:2px solid var(--o)}}'''

JS = '''(function(){var b=document.querySelector(".burger"),n=document.getElementById("nav");
b.addEventListener("click",function(){var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o)});
n.addEventListener("click",function(e){if(e.target.tagName==="A"){n.classList.remove("open");b.setAttribute("aria-expanded","false")}});
var y=document.getElementById("yr");if(y)y.textContent=new Date().getFullYear();
document.querySelectorAll("[data-lb]").forEach(function(a){a.addEventListener("click",function(ev){ev.preventDefault();var d=document.createElement("div");d.className="lb";d.innerHTML='<img alt="" src="'+a.href+'">';d.onclick=function(){d.remove()};document.body.appendChild(d)})});
document.querySelectorAll("[data-cta]").forEach(function(a){a.addEventListener("click",function(){if(window.gtag)gtag("event","cta_click",{method:a.dataset.cta,page:location.pathname})})});})();'''

CSS += '''
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:24px}.gi{display:block;overflow:hidden;border-radius:var(--r);border:1px solid #f0e2cf}.gi img{width:100%;height:100%;aspect-ratio:4/3;object-fit:cover;display:block;transition:transform .3s}.gi:hover img{transform:scale(1.05)}
.contact{padding:0;overflow:hidden}.contact>*:not(.map){margin-left:22px;margin-right:22px}.contact>h3{margin-top:18px}.contact>p:last-child{margin-bottom:22px}.map{width:100%;height:240px;border:0;display:block}
.review blockquote{font-style:italic}.review figcaption{color:var(--mut);font-size:.9rem}.mobile-bar a .ic{margin-right:6px}.lb{position:fixed;inset:0;background:rgba(0,0,0,.85);display:flex;align-items:center;justify-content:center;z-index:100;cursor:zoom-out}.lb img{max-width:92vw;max-height:88vh;border-radius:12px}
@media(max-width:900px){.gallery{grid-template-columns:repeat(2,1fr)}}@media(max-width:600px){.gallery{gap:8px}}
'''

def w(path, s):
    os.makedirs(os.path.dirname(os.path.join(ROOT, path)), exist_ok=True)
    open(os.path.join(ROOT, path), "w", encoding="utf-8").write(s)

w("index.html", home()); w("vishal-nagar.html", page("v")); w("dange-chowk.html", page("d"))
w("404.html", shell("Page not found | SaarYog", "Page not found.", BASE_URL + "/404.html", header("h") + '<main class="sec"><div class="wrap center"><h1>Page not found</h1><p>Let us take you back to yoga.</p><div class="row" style="justify-content:center"><a class="btn btn-solid" href="index.html">Go to Home</a></div></div></main>', "", "h").replace('content="index,follow,max-image-preview:large"', 'content="noindex"'))
w("assets/style.css", CSS); w("assets/main.js", JS)
w("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n")
w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{BASE_URL}/{p}</loc></url>" for p in ["", "vishal-nagar.html", "dange-chowk.html"]) + "</urlset>")
w(".nojekyll", "")
make_placeholders()
print("built")

