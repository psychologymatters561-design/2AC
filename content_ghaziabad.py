#!/usr/bin/env python3
"""Ghaziabad location page content."""
from content_loc_common import location_page, local_faqs

# ============================================================= GHAZIABAD ====
def ghaziabad():
    zones = [
        ("Indirapuram & Trans-Hindon", "High-density residential",
         "Indirapuram, Vaishali, Vasundhara and Kaushambi form the Trans-Hindon belt, and this is our busiest part of Ghaziabad by a clear margin. It is dense apartment housing, largely split systems, and outdoor unit placement is the constant challenge — condensers crowded into shared shafts with no clearance simply cannot reject heat, however good the machine. Correcting siting frequently solves cooling complaints that residents have lived with for several summers.",
         ["Indirapuram", "Vaishali", "Vasundhara", "Kaushambi", "Ahinsa Khand",
          "Shakti Khand", "Abhay Khand", "Nyay Khand", "Niti Khand"]),
        ("Raj Nagar & North Ghaziabad", "Established & new",
         "Raj Nagar and Raj Nagar Extension pair older established colonies with substantial recent high-rise development. The newer towers bring the familiar pattern of fit-out installations needing correction, while the older colonies more often need electrical assessment before new systems go in. Govindpuram and Pratap Vihar add steady residential servicing work.",
         ["Raj Nagar", "Raj Nagar Extension", "Govindpuram", "Pratap Vihar",
          "Nehru Nagar", "Vijay Nagar"]),
        ("NH-9 & Eastern Corridor", "Growth belt",
         "The NH-9 and NH-58 corridors carry Ghaziabad's newer growth, including Wave City and Crossing Republik. These are large developments where we frequently work across multiple units in the same tower, which is exactly the situation where a maintenance contract stops being a luxury and starts being the sensible way to manage it.",
         ["Wave City", "Crossing Republik", "NH-9 Corridor", "NH-58 Corridor",
          "Mohan Nagar", "Sahibabad"]),
        ("Older Ghaziabad", "Established colonies",
         "Shalimar Garden, Surya Nagar and the Loni belt are older established areas where building stock and electrical infrastructure both need proper assessment before installation. Voltage stability varies noticeably here, and getting that assessment right at the outset prevents the compressor and control board failures that otherwise appear two or three summers later.",
         ["Shalimar Garden", "Surya Nagar", "Loni", "Gandhi Nagar", "Kavi Nagar",
          "Model Town Ghaziabad"]),
    ]

    intro = ("<p>Ghaziabad's centre of gravity for us is the <strong>Trans-Hindon belt</strong> — Indirapuram, "
             "Vaishali, Vasundhara and Kaushambi — which is dense apartment housing sitting right on the Delhi border.</p>"
             "<p>The recurring problem across this belt is not the machines, it is where their outdoor units were put. "
             "Condensers crowded into shared service shafts with no clearance cannot reject heat properly, and the "
             "resulting poor cooling gets blamed on the AC itself. It is usually correctable, and correcting it is "
             "cheaper than the replacement people are often told they need.</p>")

    faqs = local_faqs("Ghaziabad", "Indirapuram, Vaishali, Vasundhara, Kaushambi, Raj Nagar Extension, Crossing Republik and the NH-9 corridor", extra=[
        ("My AC in Indirapuram never cools properly even after servicing. Why?",
         "In this belt the most common cause is the outdoor unit rather than the indoor one. Condensers installed in shared shafts or tight ledges without clearance recirculate their own hot air and cannot reject heat, so the system runs continuously and never reaches temperature. Servicing the indoor unit will not fix that. We assess siting and airflow as part of diagnosis, and relocating or re-orienting the condenser often resolves a problem people have had for years."),
    ])

    return location_page(
        slug="ac-service-ghaziabad.html",
        title="AC Repair &amp; Service in Ghaziabad | Air Control",
        desc="AC repair, service &amp; installation across Ghaziabad. Indirapuram, Vaishali, Vasundhara, Raj Nagar Extension &amp; NH-9 corridor. Call +91 93122 64832.",
        h1="AC Repair, Service &amp; Installation in <em>Ghaziabad</em>",
        hero_sub="Indirapuram, Vaishali, Vasundhara and the wider Trans-Hindon belt — where getting outdoor unit placement right matters more than any other single factor.",
        city="Ghaziabad", intro_html=intro, zones=zones, faqs=faqs,
        area_list=["Ghaziabad", "Indirapuram", "Vaishali", "Vasundhara", "Delhi NCR"],
        xlinks=[
            ("ac-repair.html", "AC Repair", "Same-day diagnosis, including condenser siting assessment."),
            ("ac-servicing.html", "AC Servicing", "Deep cleaning and performance restoration."),
            ("ac-amc.html", "AC AMC", "Planned maintenance — sensible once you have several units."),
            ("ac-installation.html", "AC Installation", "Correct siting and sizing from the outset."),
            ("ac-service-noida.html", "AC Service Noida", "All sectors plus Greater Noida and Noida Extension."),
            ("ac-service-delhi.html", "AC Service Delhi", "Full zone-by-zone coverage across Delhi."),
        ])
