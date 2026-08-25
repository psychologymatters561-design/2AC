#!/usr/bin/env python3
"""
Normalise the hand-written pages (homepage, why-us, blog).

The generated service and location pages get these properties from the
template in build.py. The hand-written pages need them applied in place, so
this script does it idempotently: running it twice changes nothing.

  - keyword-stuffed footer blocks removed
  - placeholder form key replaced with the real one
  - over-length titles and descriptions shortened
  - "HVAC" replaced with "AC" in visible copy only
  - logo <img> falls back to logo.svg when logo.png is missing
  - favicon points at logo.svg, since <link> cannot fall back
  - images below the fold get loading="lazy"
  - every page carries BreadcrumbList schema
"""
import glob, json, os, re

SITE = "https://aircontrols.in"
WEB3FORMS_KEY = "0b3287e6-ba3f-4a09-93ed-2212b40ea680"

# Titles beyond roughly 60 characters get truncated in search results, and one
# of these still carried trade jargon. Descriptions beyond ~155 truncate too.
TITLE_OVERRIDES = {
    "why-us.html": "Why Air Control | 38 Years of AC Engineering",
    "blog/ac-market-guide-delhi.html": "AC Buying Guide for Delhi NCR | Air Control",
    "blog/choose-hvac-small-apartment.html": "Choosing an AC for a Small Apartment | Air Control",
}
DESC_OVERRIDES = {
    "blog/ac-market-guide-delhi.html":
        "A practical guide to buying an AC in Delhi NCR: where to look, what to "
        "check and what to avoid. Call +91 93122 64832.",
    "blog/choose-hvac-small-apartment.html":
        "How to choose the right AC for a small apartment in Delhi NCR: sizing, "
        "placement and running costs. Call +91 93122 64832.",
}
GENERATED = {
    "ac-repair.html", "ac-servicing.html", "ac-installation.html", "ac-amc.html",
    "ac-service-delhi.html", "ac-service-gurgaon.html", "ac-service-noida.html",
    "ac-service-faridabad.html", "ac-service-ghaziabad.html",
}


def h1_of(path, html):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    if not m:
        return os.path.basename(path)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", m.group(1))).strip()


def crumb_schema(trail):
    items = []
    for i, (label, href) in enumerate(trail):
        item = {"@type": "ListItem", "position": i + 1, "name": label}
        if href is not None:
            item["item"] = SITE + "/" + ("" if href == "index.html" else href)
        items.append(item)
    return {"@context": "https://schema.org",
            "@type": "BreadcrumbList", "itemListElement": items}


def strip_visible_hvac(html):
    """
    Replace "HVAC" with "AC" in visible copy only.

    Trade jargon, and the brief asks for consumer-facing wording on the page.
    Attributes, script, style and meta tags are left alone, so keyword and
    schema values keep their SEO weight and no filename in an href is ever
    rewritten (which would silently break the link).
    """
    start = html.find("<body")
    if start == -1:
        return html
    head, body = html[:start], html[start:]
    parts = re.split(r"(<[^>]+>)", body)
    skip = 0
    for i, part in enumerate(parts):
        if part.startswith("<"):
            tag = part.lower()
            if tag.startswith(("<script", "<style")):
                skip += 1
            elif tag.startswith(("</script", "</style")):
                skip = max(0, skip - 1)
            continue
        if skip:
            continue
        parts[i] = re.sub(r"\bHVAC\b", "AC", part)
    return head + "".join(parts)


def normalise(path):
    html = open(path, encoding="utf-8").read()
    original = html
    prefix = "../" * path.count("/")

    # Some footer-seo blocks hold a legitimate paragraph describing the
    # services and areas covered; others hold dozens of comma-separated
    # "<thing> near me" search phrases, which read as spam to a visitor and
    # risk a ranking penalty. Remove only the latter, identified by a run of
    # "near me" phrases that no ordinary sentence would contain.
    def drop_if_stuffed(m):
        text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", m.group(0)))
        return "" if len(re.findall(r"near me", text, re.I)) >= 5 else m.group(0)

    html = re.sub(r'<div class="footer-seo".*?</div>', drop_if_stuffed, html, flags=re.S)

    # A placeholder form key means the form accepts submissions and silently
    # discards them, so every lead through that page is lost.
    html = html.replace("YOUR_WEB3FORMS_ACCESS_KEY", WEB3FORMS_KEY)

    # Over-length titles and descriptions truncate in search results.
    title = TITLE_OVERRIDES.get(path)
    if title:
        html = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", html,
                      count=1, flags=re.S)
        for attr in ('property="og:title"', 'name="twitter:title"'):
            html = re.sub(r'(<meta ' + re.escape(attr) + r' content=")[^"]*(")',
                          r"\g<1>" + title + r"\g<2>", html, count=1)
    desc = DESC_OVERRIDES.get(path)
    if desc:
        for attr in ('name="description"', 'property="og:description"',
                     'name="twitter:description"'):
            html = re.sub(r'(<meta ' + re.escape(attr) + r' content=")[^"]*(")',
                          r"\g<1>" + desc + r"\g<2>", html, count=1)

    html = strip_visible_hvac(html)

    # Some pages fell back to a third-party placeholder service. That is an
    # external request on every page view and renders generic text instead of
    # the brand mark, so point those at the local svg instead.
    html = re.sub(r"this\.src='https://placehold\.co/[^']*'",
                  f"this.src='{prefix}logo.svg'", html)

    # logo fallback on every logo.png <img>
    def add_fallback(m):
        tag = m.group(0)
        if "onerror" in tag:
            return tag
        return tag[:-1].rstrip() + f" onerror=\"this.onerror=null;this.src='{prefix}logo.svg'\">"

    html = re.sub(r'<img\b[^>]*src="(?:\.\./)*logo\.png"[^>]*>', add_fallback, html)

    # favicon cannot fall back, so point it straight at the svg
    html = re.sub(r'(<link rel="icon" href=")(?:\.\./)*logo\.png(")',
                  r"\g<1>" + prefix + r"logo.svg\g<2>", html)

    # lazy-load everything except the first image (usually the nav logo)
    for m in reversed(list(re.finditer(r"<img\b[^>]*>", html))[1:]):
        tag = m.group(0)
        if "loading=" in tag:
            continue
        html = html[:m.start()] + tag[:-1].rstrip() + ' loading="lazy">' + html[m.end():]

    # breadcrumb schema
    if "BreadcrumbList" not in html:
        if path == "index.html":
            trail = [("Home", None)]
        elif path == "blog.html":
            trail = [("Home", "index.html"), ("Insights", None)]
        elif path.startswith("blog/"):
            trail = [("Home", "index.html"), ("Insights", "blog.html"),
                     (h1_of(path, html), None)]
        else:
            trail = [("Home", "index.html"), (h1_of(path, html), None)]
        block = ('<script type="application/ld+json">\n'
                 + json.dumps(crumb_schema(trail), ensure_ascii=False, indent=2)
                 + "\n</script>\n")
        html = html.replace("</head>", block + "</head>", 1)

    if html != original:
        open(path, "w", encoding="utf-8").write(html)
        return True
    return False


if __name__ == "__main__":
    pages = sorted(set(glob.glob("*.html")) | set(glob.glob("blog/*.html")))
    handwritten = [p for p in pages if p not in GENERATED]
    changed = [p for p in handwritten if normalise(p)]
    print(f"normalised {len(changed)} of {len(handwritten)} hand-written pages")
    for p in changed:
        print("  ", p)
