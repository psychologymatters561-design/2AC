#!/usr/bin/env python3
"""The blog index page."""
from build import render, cross_links, emergency, PHONE, PHONE_H, WA
from content_common import sec, head

HOME = ("Home", "index.html")

# slug, category, title, excerpt, date, read-minutes
ARTICLES = [
    ("blog/ac-not-cooling.html", "Troubleshooting",
     "AC Not Cooling? 12 Reasons Why, and How to Fix Each One",
     "Your AC runs, the fan turns, the room stays warm. The twelve real causes in the order we find "
     "them, what you can check yourself in five minutes, and what needs instruments.",
     "25 August 2026", 9),
    ("blog/best-ac-for-home.html", "Buying Guides",
     "Best AC for Your Home: An Engineer's Buying Guide",
     "Sizing on the room rather than floor area, inverter versus non-inverter, star ratings that "
     "actually pay back, and why installation predicts an AC's life better than the brand.",
     "25 August 2026", 9),
    ("blog/how-often-ac-service.html", "Maintenance",
     "How Often Should You Service Your AC?",
     "Every three to six months in Delhi NCR, and the reason is not sales pressure. Guidance by "
     "usage, what a genuine service covers, and the signs you have left it too long.",
     "25 August 2026", 7),
    ("blog/ac-gas-filling-cost-delhi.html", "Cost Guides",
     "AC Gas Filling in Delhi NCR: What It Costs and What to Ask",
     "Refrigerant is not a consumable. What drives the cost, how the job should be done, and how to "
     "tell a real repair from a top-up you will be paying for again next summer.",
     "25 August 2026", 8),
    ("blog/ac-amc-worth-it.html", "Cost Guides",
     "Is an AC AMC Worth It? An Honest Cost-Benefit Analysis",
     "We sell these contracts, so start sceptical. The case against, the point where the arithmetic "
     "flips, and the situations where we tell clients not to bother.",
     "25 August 2026", 8),
    ("blog/ac-market-guide-delhi.html", "Buying Guides",
     "AC Buying Guide for Delhi NCR",
     "Where to look, what to check before you hand over money, and the traps that catch people "
     "buying used or wholesale in Delhi.",
     "12 April 2026", 6),
    ("blog/choose-hvac-small-apartment.html", "Buying Guides",
     "Choosing an AC for a Small Apartment",
     "Sizing, placement and running costs when the room is compact and the outdoor space is tight. "
     "Includes when a ductless mini-split is the right answer.",
     "12 April 2026", 6),
    ("blog/ac-gas-refill-cost-2025.html", "Cost Guides",
     "AC Gas Refill: What Affects the Price",
     "Refrigerant type, system capacity, access and whether there is a leak to repair. The factors "
     "that move a quote, explained plainly.",
     "12 April 2026", 6),
    ("blog/furnace-repair-signs.html", "Troubleshooting",
     "Heating System Repair: The Warning Signs",
     "For clients with heating as well as cooling. The symptoms worth acting on early, and the ones "
     "that mean switching off and calling immediately.",
     "12 April 2026", 6),
]


def cards():
    out = ['<div class="bgrid">']
    for href, cat, title, excerpt, date, mins in ARTICLES:
        out.append(
            f'<a class="bcard reveal" href="{href}">'
            f'<div class="bcard-cat">{cat}</div>'
            f'<h3>{title}</h3>'
            f'<p>{excerpt}</p>'
            f'<div class="bcard-foot"><span>{date}</span>'
            f'<span class="bcard-read">{mins} min read</span></div></a>')
    out.append("</div>")
    return "\n".join(out)


def blog_index():
    from build_blog import ARTICLE_CSS
    trail = [HOME, ("Insights", None)]
    body = "".join([
        sec("section", head("Insights & Guides", "AC Tips &amp; <em>Expert Advice</em>",
            "Practical guides written by the engineers who do the work — no filler, no padding, "
            "and no prices quoted before anyone has seen your system.")
            + cards()),
        sec("section section-dark",
            '<div class="text-center reveal">'
            + '<span class="section-label text-gold">Need Help Now?</span>'
            + '<div class="gold-rule center"></div>'
            + '<h2 class="headline text-white">Reading Can Wait. <em>A Warm Room Cannot.</em></h2>'
            + '<p class="lead-text" style="max-width:560px;margin:16px auto 0;">'
            + 'If your AC has stopped working, skip the guides and call us. '
            + '2-hour emergency response across Delhi NCR.</p>'
            + '<div class="cta-btns" style="margin-top:28px;">'
            + f'<a class="btn btn-gold btn-lg" href="tel:{PHONE}">\U0001f4de Call {PHONE_H}</a>'
            + f'<a class="btn btn-navy btn-lg" href="{WA}" target="_blank" rel="noopener">\U0001f4ac WhatsApp Us</a>'
            + '</div></div>'),
        sec("section section-cream", head("Our Services", "How We Can <em>Help</em>")
            + cross_links([
                ("ac-repair.html", "AC Repair",
                 "Not cooling, gas leaks, noise or tripping — diagnosed properly, usually same day."),
                ("ac-servicing.html", "AC Servicing",
                 "Deep cleaning, coil and condenser washing, gas checks and a measured report."),
                ("ac-installation.html", "AC Installation",
                 "Split, cassette, ducted, central and VRF, sized on real heat load."),
                ("ac-amc.html", "AC AMC",
                 "Scheduled maintenance with priority response and documented visits."),
                ("ac-service-delhi.html", "AC Service Delhi",
                 "Every zone and locality we cover across the city."),
                ("why-us.html", "Why Air Control",
                 "The engineering standards and safety record behind the work."),
            ])),
    ])
    html = render(
        slug="blog.html",
        title="AC Tips, Guides &amp; Expert Advice | Air Control",
        desc="Practical AC guides from Delhi NCR engineers since 1987: why an AC stops cooling, how often to service, choosing a unit, and what maintenance really costs.",
        h1="AC Tips &amp; <em>Expert Advice</em>",
        hero_sub="Guides written by the engineers who do the work. What actually goes wrong with air "
                 "conditioners in Delhi, what it takes to fix properly, and how to avoid paying twice.",
        trail=trail, body=body,
        area=["Delhi", "New Delhi", "Gurgaon", "Noida", "Faridabad", "Ghaziabad"])
    # the card styles live with the article template
    return html.replace("</style>", ARTICLE_CSS + "</style>", 1)
