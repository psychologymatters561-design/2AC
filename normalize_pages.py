#!/usr/bin/env python3
"""
Normalise the hand-written pages (homepage, why-us, blog).

The generated service and location pages get these properties from the
template in build.py. The hand-written pages need them applied in place, so
this script does it idempotently: running it twice changes nothing.

  - logo <img> falls back to logo.svg when logo.png is missing
  - favicon points at logo.svg, since <link> cannot fall back
  - images below the fold get loading="lazy"
  - every page carries BreadcrumbList schema
"""
import glob, json, os, re

SITE = "https://aircontrols.in"
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


def normalise(path):
    html = open(path, encoding="utf-8").read()
    original = html
    prefix = "../" * path.count("/")

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
    changed = [p for p in pages if p not in GENERATED and normalise(p)]
    print(f"normalised {len(changed)} of {len(pages) - len(GENERATED)} hand-written pages")
    for p in changed:
        print("  ", p)
