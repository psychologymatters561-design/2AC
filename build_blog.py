#!/usr/bin/env python3
"""
Article template for the blog.

Reuses the chrome and design system from build.py so the articles sit in the
same world as the rest of the site, and adds the article-specific furniture:
a meta row, pull-out callouts, an FAQ block and BlogPosting schema.
"""
import json, re, html as H
from build import (base_css, PAGE_CSS, nav, footer, chatbot, scripts,
                   crumbs_html, crumb_schema, faq_html, faq_schema,
                   PHONE, PHONE_H, WA, SITE, EMAIL)

DEPTH = 1  # every article lives in blog/

ARTICLE_CSS = """
/* ===== ARTICLE ===== */
.art-hero{position:relative;padding:150px 0 60px;overflow:hidden;
  background:linear-gradient(160deg,#081524,var(--navy) 45%,var(--navy-3))}
.art-hero-inner{position:relative;z-index:3;max-width:800px}
.art-cat{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.16em;
  text-transform:uppercase;color:#12203a;padding:5px 13px;border-radius:100px;
  background:linear-gradient(135deg,var(--gold-lt),var(--gold));margin:16px 0 18px}
.art-hero h1{color:#fff;font-size:clamp(1.9rem,4.2vw,3rem);line-height:1.14;margin-bottom:18px}
.art-lede{color:rgba(255,255,255,.68);font-size:clamp(1rem,1.6vw,1.16rem);line-height:1.75;max-width:680px}
.art-meta{display:flex;flex-wrap:wrap;gap:18px;align-items:center;margin-top:26px;
  padding-top:20px;border-top:1px solid rgba(255,255,255,.12);
  font-size:12.5px;color:rgba(255,255,255,.55)}
.art-meta strong{color:var(--gold);font-weight:600}

.art-wrap{max-width:800px;margin:0 auto;padding:clamp(48px,6vw,76px) clamp(20px,4vw,32px)}
.art-body h2{font-size:clamp(1.5rem,2.9vw,2rem);margin:44px 0 14px;scroll-margin-top:90px}
.art-body h2:first-child{margin-top:0}
.art-body h3{font-size:clamp(1.1rem,1.8vw,1.3rem);margin:30px 0 10px;color:var(--ink)}
.art-body p{color:var(--muted);line-height:1.85;margin-bottom:16px;font-size:15.5px}
.art-body ul,.art-body ol{margin:0 0 20px;padding-left:0}
.art-body li{color:var(--muted);line-height:1.8;margin-bottom:10px;padding-left:28px;
  position:relative;font-size:15.5px}
.art-body ul li::before{content:'';position:absolute;left:8px;top:12px;width:6px;height:6px;
  border-radius:50%;background:var(--gold)}
.art-body ol{counter-reset:n}
.art-body ol li{counter-increment:n}
.art-body ol li::before{content:counter(n);position:absolute;left:0;top:1px;width:20px;height:20px;
  border-radius:6px;background:rgba(200,168,110,.16);color:var(--gold-dk);
  font-size:11.5px;font-weight:700;display:grid;place-items:center}
.art-body strong{color:var(--ink);font-weight:600}
.art-body a{color:var(--gold-dk);font-weight:600;border-bottom:1px solid rgba(200,168,110,.4)}
.art-body a:hover{color:var(--gold)}

/* takeaways / callouts */
.takeaway{background:linear-gradient(150deg,rgba(200,168,110,.09),rgba(30,77,183,.05));
  border:1px solid rgba(200,168,110,.28);border-radius:var(--r-lg);
  padding:26px 28px;margin:32px 0}
.takeaway h4{font-family:'DM Sans',sans-serif;font-size:11.5px;font-weight:700;
  letter-spacing:.16em;text-transform:uppercase;color:var(--gold-dk);margin-bottom:14px}
.takeaway ul{margin:0}
.takeaway li{font-size:14.5px;margin-bottom:9px}

.callout{border-left:3px solid var(--gold);background:#fff;border-radius:0 var(--r) var(--r) 0;
  padding:20px 24px;margin:28px 0;box-shadow:var(--sh)}
.callout p{margin:0;font-size:14.8px;color:var(--muted)}
.callout strong{color:var(--ink)}

.warn{border-left:3px solid #b91c1c;background:#fff5f5;border-radius:0 var(--r) var(--r) 0;
  padding:20px 24px;margin:28px 0}
.warn p{margin:0;font-size:14.8px;color:#7f1d1d}

/* article cta */
.art-cta{background:linear-gradient(150deg,var(--navy),var(--royal));border-radius:var(--r-xl);
  padding:clamp(30px,4vw,44px);margin:44px 0 0;text-align:center;position:relative;overflow:hidden}
.art-cta h3{color:#fff;font-size:clamp(1.3rem,2.4vw,1.75rem);margin-bottom:10px;position:relative;z-index:1}
.art-cta p{color:rgba(255,255,255,.62);font-size:14.5px;max-width:480px;margin:0 auto 22px;
  position:relative;z-index:1}
.art-cta-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;position:relative;z-index:1}

/* blog index cards */
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:24px;margin-top:50px}
.bcard{background:#fff;border:1px solid rgba(15,28,46,.08);border-radius:var(--r-lg);
  padding:30px 28px;display:flex;flex-direction:column;transition:all .5s var(--ease);position:relative;overflow:hidden}
.bcard::after{content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,var(--gold),var(--gold-lt));transform:scaleX(0);
  transform-origin:left;transition:transform .5s var(--ease)}
.bcard:hover{transform:translateY(-7px);box-shadow:var(--sh-lg);border-color:rgba(200,168,110,.3)}
.bcard:hover::after{transform:scaleX(1)}
.bcard-cat{font-size:10.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold-dk);margin-bottom:12px}
.bcard h3{font-size:19.5px;line-height:1.3;margin-bottom:11px}
.bcard p{font-size:14px;color:var(--muted);line-height:1.7;margin-bottom:18px;flex:1}
.bcard-foot{display:flex;justify-content:space-between;align-items:center;gap:12px;
  padding-top:16px;border-top:1px solid #eef1f5;font-size:12px;color:var(--muted)}
.bcard-read{font-weight:700;color:var(--gold-dk)}
"""


def article_schema(slug, title, desc, published, modified, section):
    return {
        "@type": "BlogPosting",
        "headline": re.sub(r"<[^>]+>", "", title),
        "description": desc,
        "url": f"{SITE}/blog/{slug}",
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE}/blog/{slug}"},
        "datePublished": published,
        "dateModified": modified,
        "articleSection": section,
        "inLanguage": "en-IN",
        "image": f"{SITE}/logo.png",
        "author": {"@type": "Organization", "name": "Air Control", "url": SITE},
        "publisher": {
            "@type": "Organization", "name": "Air Control", "url": SITE,
            "logo": {"@type": "ImageObject", "url": f"{SITE}/logo.png"},
        },
    }


def art_cta(heading, sub):
    return f"""<div class="art-cta reveal">
  <div class="orb orb2" style="top:-120px;right:-110px;left:auto;bottom:auto;"></div>
  <h3>{heading}</h3>
  <p>{sub}</p>
  <div class="art-cta-btns">
    <a class="btn btn-gold btn-lg" href="tel:{PHONE}">\U0001f4de Call {PHONE_H}</a>
    <a class="btn btn-navy btn-lg" href="{WA}" target="_blank" rel="noopener">\U0001f4ac WhatsApp Us</a>
  </div>
</div>"""


def related(cards):
    out = ['<div class="xgrid">']
    for href, h4, txt in cards:
        out.append(f'<a class="xcard reveal" href="{href}"><h4>{h4}</h4><p>{txt}</p>'
                   f'<span>Read more →</span></a>')
    return "\n".join(out + ["</div>"])


def render_article(slug, title, desc, h1, lede, body, faqs, related_cards,
                   category="AC Guides", published="2026-08-25", modified="2026-08-25",
                   read_minutes=8):
    trail = [("Home", "index.html"), ("Insights", "blog.html"),
             (re.sub(r"<[^>]+>", "", h1), None)]
    graph = [crumb_schema(trail),
             article_schema(slug, h1, desc, published, modified, category)]
    if faqs:
        graph.append(faq_schema(faqs))
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    ensure_ascii=False, indent=2)
    canonical = f"{SITE}/blog/{slug}"
    css = base_css() + PAGE_CSS + ARTICLE_CSS
    esc = H.escape(title, quote=True)
    faq_block = ""
    if faqs:
        faq_block = ('<h2>Frequently asked questions</h2>' + faq_html(faqs))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{esc}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/logo.png">
<meta property="og:site_name" content="Air Control">
<meta property="article:published_time" content="{published}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/logo.png">
<meta name="theme-color" content="#0a1628">
<link rel="icon" href="../logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<script type="application/ld+json">
{ld}
</script>
<style>{css}</style>
</head>
<body>
{nav(DEPTH)}
<article>
<section class="art-hero">
  <div class="orb orb1"></div><div class="orb orb2"></div><div class="hero-grid"></div>
  <div class="container">
    <div class="art-hero-inner">
      {crumbs_html(trail, DEPTH)}
      <span class="art-cat">{category}</span>
      <h1 class="reveal">{h1}</h1>
      <p class="art-lede reveal d1">{lede}</p>
      <div class="art-meta reveal d2">
        <span>By <strong>Air Control</strong> · Delhi NCR since 1987</span>
        <span>{read_minutes} min read</span>
        <span>Updated {modified}</span>
      </div>
    </div>
  </div>
</section>

<div class="art-wrap">
  <div class="art-body">
{body}
{faq_block}
  </div>
  {art_cta("Still not sure what is wrong?",
           "Tell us what your AC is doing and our engineer will call you back within 2 hours. No obligation.")}
</div>
</article>

<section class="section section-cream">
  <div class="container">
    <div class="text-center reveal">
      <span class="section-label text-royal">Keep Reading</span>
      <div class="gold-rule center"></div>
      <h2 class="headline">Related <em>Guides</em> &amp; Services</h2>
    </div>
    {related(related_cards)}
  </div>
</section>
{footer(DEPTH)}
{chatbot(DEPTH)}
{scripts()}
</body>
</html>"""
