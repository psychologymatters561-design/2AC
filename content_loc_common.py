#!/usr/bin/env python3
"""Shared helpers for the location pages."""
from build import render, lead_form, cross_links, emergency, brand_chips, faq_html, PHONE_H
from content_common import sec, head, cards, steps, stats_band

HOME = ("Home", "index.html")


def zones_html(zones):
    out = []
    for name, badge, blurb, locs in zones:
        chips = "".join(f"<span>{l}</span>" for l in locs)
        out.append(f'<div class="zone reveal"><h3>{name}<span class="zbadge">{badge}</span></h3>'
                   f'<p>{blurb}</p><div class="zlist">{chips}</div></div>')
    return "\n".join(out)


def services_block(city):
    return cards([
        ("🔧", f"AC Repair in {city}", f"Not cooling, gas leaks, water dripping, tripping, compressor and PCB faults — diagnosed and repaired, usually same day."),
        ("💧", f"AC Servicing in {city}", "Deep cleaning with foam and jet wash, coil and condenser cleaning, gas top-up and full performance checks."),
        ("❄", f"AC Installation in {city}", "Split, cassette, ducted, central and VRF systems, sized on real heat load and commissioned properly."),
        ("🛡", f"AC AMC in {city}", "Scheduled preventive maintenance with priority response — for homes with several units and for commercial sites."),
    ])


def local_faqs(city, areas_line, extra=None):
    f = [
        (f"Do you provide AC repair near me in {city}?",
         f"Yes. We cover {areas_line} and the surrounding areas. Our engineers work across the region daily, so in most cases we can attend the same day. Call {PHONE_H} and tell us your locality — we will give you a realistic time, not an optimistic one."),
        (f"How quickly can you reach {city} for an emergency?",
         f"We target a two-hour response for genuine emergencies across {city}. In peak summer, response times across the whole industry stretch, which is one of the practical reasons our AMC clients get priority scheduling ahead of ad-hoc callers."),
        (f"Do you charge extra for {city} locations?",
         f"No. Our pricing is based on the work required, not on which part of the region you are in. We have covered all of Delhi NCR for thirty-eight years, so there is no premium for being at the far end of it."),
        ("Which AC brands do you service?",
         "All major brands — Daikin, Blue Star, Voltas, LG, Samsung, Hitachi, Carrier, O General, Mitsubishi, Panasonic, Godrej, Lloyd, Whirlpool, Haier, Toshiba and Sanyo — across split, window, cassette, tower, ducted, central and VRF/VRV systems."),
        (f"Do you handle commercial AC work in {city}?",
         f"Yes. Offices, showrooms, restaurants, clinics, hotels and factories across {city} are a large part of our work, including cassette, ducted, central and VRF systems. For multi-unit sites we normally recommend a maintenance contract so servicing happens on schedule."),
        (f"Can I book an AC service in {city} for a specific day?",
         "Yes. Tell us the day and rough time window that suits you and we will schedule accordingly. Booking a few days ahead is worth doing between April and July, when slots fill quickly."),
    ]
    if extra:
        f.extend(extra)
    return f


def location_page(slug, title, desc, h1, hero_sub, city, intro_html, zones,
                  faqs, xlinks, area_list):
    trail = [HOME, ("Service Areas", "ac-service-delhi.html"), (f"AC Service {city}", None)]
    body = "".join([
        sec("section", head("Local Coverage", f"AC Service Across <em>{city}</em>", center=False)
            + f'<div class="prose reveal" style="max-width:860px;margin-top:8px;">{intro_html}</div>'),
        stats_band(),
        sec("section section-cream", head("Areas We Cover", f"Every Corner of <em>{city}</em>",
            "Organised by zone, with the localities our engineers attend regularly.")
            + f'<div style="margin-top:44px;">{zones_html(zones)}</div>'),
        sec("section", head("What We Do", f"Our Services in <em>{city}</em>") + services_block(city)),
        sec("section section-cream", head("All Major Brands", "Every <em>Brand</em> Serviced") + brand_chips()),
        sec("section", head("How We Work", "From Your Call to <em>Cool Air</em>")
            + steps([
                ("Call or WhatsApp", "Tell us your locality and what the AC is doing. We ask the right questions so the engineer arrives prepared."),
                ("Same-Day Scheduling", "In most of the region we can attend the same day, and we give you a realistic window rather than an optimistic one."),
                ("Diagnose & Quote", "We measure rather than guess, explain the actual fault plainly, and quote before starting any work."),
                ("Fix, Test & Warrant", "Repair with genuine parts, verified against specification, documented and warranted."),
            ])),
        sec("section section-dark", '<div class="text-center reveal">'
            + '<span class="section-label text-gold">Book a Visit</span>'
            + '<div class="gold-rule center"></div>'
            + f'<h2 class="headline text-white">AC Service in <em>{city}</em></h2></div>'
            + '<div style="margin-top:40px;">'
            + lead_form(f"Book an Engineer in {city}",
                        "Tell us your locality and what you need. We will call you back within 2 hours.",
                        f"AC Enquiry ({city}) — Air Control",
                        extra_fields="""<div class="frow">
      <div class="fld"><label>Service Required *</label><select name="service_type" required>
        <option value="">Select service...</option>
        <option>AC repair — not cooling / breakdown</option><option>AC servicing / deep cleaning</option>
        <option>Gas filling / top-up</option><option>New AC installation</option>
        <option>AC AMC / maintenance contract</option><option>Emergency — urgent</option>
      </select></div>
      <div class="fld"><label>AC Type *</label><select name="ac_type" required>
        <option value="">Select AC type...</option>
        <option>Split AC</option><option>Window AC</option><option>Cassette AC</option>
        <option>Ducted AC</option><option>Central AC</option><option>VRF / VRV</option>
        <option>Not sure</option>
      </select></div>
    </div>""")
            + '</div>' + emergency()),
        sec("section", head("Questions", f"AC Service in {city} — <em>FAQs</em>") + faq_html(faqs)),
        sec("section section-cream", head("Keep Exploring", "Related <em>Services</em> &amp; Areas")
            + cross_links(xlinks)),
    ])
    return render(slug=slug, title=title, desc=desc, h1=h1, hero_sub=hero_sub,
                  trail=trail, body=body, faqs=faqs, area=area_list)
