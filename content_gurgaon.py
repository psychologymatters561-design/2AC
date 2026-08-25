#!/usr/bin/env python3
"""Gurgaon location page content."""
from content_loc_common import location_page, local_faqs

# =============================================================== GURGAON ====
def gurgaon():
    zones = [
        ("DLF & Golf Course Road", "Premium residential",
         "This corridor holds much of Gurgaon's premium housing, from the DLF phases through to the Camellias, Aralias and Magnolias. The work here is predominantly VRF, ducted and multi-split systems rather than single wall units, which means proper commissioning and planned maintenance matter far more — a fault in a zoned system affects the whole floor, not one room. Many of these residences run maintenance contracts because coordinating servicing across eight or ten indoor units otherwise becomes a job in itself.",
         ["DLF Phase 1", "DLF Phase 2", "DLF Phase 3", "DLF Phase 4", "DLF Phase 5",
          "Golf Course Road", "Golf Course Extension Road", "The Magnolias", "DLF Camellias",
          "DLF Aralias", "Laburnum", "The Palm Springs", "Hamilton Court", "Central Park",
          "Bestech Park View", "M3M Golfestate"]),
        ("Cyber City & Commercial Belt", "Corporate hub",
         "Cyber City, Udyog Vihar and the MG Road commercial stretch are dense with corporate offices, and the cooling here is almost entirely central plant, VRF and cassette systems running long hours under heavy occupancy. Downtime in these buildings is expensive and visible, so this is contract territory — planned quarterly maintenance with documented reports, and response commitments that facilities managers can hold us to. We schedule the disruptive work outside office hours.",
         ["Cyber City", "Udyog Vihar", "MG Road", "IFFCO Chowk", "Huda City Centre",
          "Sohna Road", "Dwarka Expressway"]),
        ("Sushant Lok & Sector Belt", "Mixed residential",
         "Sushant Lok, South City and the numbered sectors from 14 through 57 form Gurgaon's broad residential middle, mixing builder floors, older independent houses and gated societies. Split systems dominate, and the recurring issue we see is outdoor units sited badly during original construction — crowded into shafts or ledges with no clearance, which quietly costs cooling capacity every summer. Relocating a condenser correctly often fixes a problem people have lived with for years.",
         ["Sushant Lok 1", "Sushant Lok 2", "Sushant Lok 3", "South City 1", "South City 2",
          "Sector 14", "Sector 15", "Sector 17", "Sector 21", "Sector 23", "Sector 27",
          "Sector 31", "Sector 38", "Sector 40", "Sector 43", "Sector 45", "Sector 47",
          "Sector 49", "Sector 50", "Sector 52", "Sector 54", "Sector 56", "Sector 57"]),
        ("New Gurgaon & Manesar", "Growth corridor",
         "The newer townships and the Manesar industrial belt bring a different mix again — recently built apartments still under builder warranty alongside factories and warehouses with genuine industrial cooling and ventilation requirements. For new apartments we are frequently called to correct installation shortcuts left by the original fit-out, most commonly inadequate insulation and drain lines run without proper fall.",
         ["Palam Vihar", "Nirvana Country", "Malibu Town", "Ardee City", "Vipul World",
          "Vatika City", "Emaar Palm Gardens", "Heritage City", "Suncity",
          "Gurgaon-Faridabad Road", "Manesar", "IMT Manesar"]),
    ]

    intro = ("<p>Gurgaon presents a genuinely different engineering picture to old Delhi. The building stock is "
             "newer and taller, glazing ratios are far higher, and a large share of the premium residential and "
             "corporate space runs <strong>VRF, ducted and central systems</strong> rather than individual split units.</p>"
             "<p>High-rise glass buildings gain heat quickly and unevenly, which makes correct sizing and zoning "
             "more important here than almost anywhere else in NCR. We have worked this market since it was "
             "farmland, and we cover it from DLF Phase 1 through to IMT Manesar.</p>")

    faqs = local_faqs("Gurgaon", "DLF Phases 1 to 5, Golf Course Road, Cyber City, Sohna Road, Sushant Lok, South City, Palam Vihar and all sectors", extra=[
        ("Do you service VRF systems in Gurgaon high-rises?",
         "Yes. VRF and VRV systems are a core part of our Gurgaon work, in both premium residences and corporate buildings. These systems need manufacturer-level diagnostics rather than general AC troubleshooting, and they reward planned maintenance because component costs are high and a fault affects a whole zone rather than one room."),
    ])

    return location_page(
        slug="ac-service-gurgaon.html",
        title="AC Repair &amp; Service in Gurgaon | Air Control Since 1987",
        desc="AC repair, service &amp; installation across Gurgaon. DLF, Golf Course Road, Cyber City &amp; all sectors. Call +91 93122 64832.",
        h1="AC Repair, Service &amp; Installation in <em>Gurgaon</em>",
        hero_sub="From DLF Phase 1 to IMT Manesar — split, cassette, ducted and VRF systems maintained by engineers who have worked this market since before the towers arrived.",
        city="Gurgaon", intro_html=intro, zones=zones, faqs=faqs,
        area_list=["Gurgaon", "Gurugram", "Manesar", "Delhi NCR"],
        xlinks=[
            ("ac-amc.html", "AC AMC", "Planned maintenance for multi-unit homes, offices and VRF systems."),
            ("ac-installation.html", "AC Installation", "VRF, ducted and central systems sized on real heat load."),
            ("ac-repair.html", "AC Repair", "Same-day diagnosis and repair across Gurgaon."),
            ("ac-servicing.html", "AC Servicing", "Deep cleaning and performance restoration for every system type."),
            ("ac-service-delhi.html", "AC Service Delhi", "Full zone-by-zone coverage across Delhi."),
            ("ac-service-faridabad.html", "AC Service Faridabad", "NIT, Old Faridabad, Neharpar and all sectors."),
        ])
