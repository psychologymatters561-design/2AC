#!/usr/bin/env python3
"""Noida location page content."""
from content_loc_common import location_page, local_faqs

# ================================================================= NOIDA ====
def noida():
    zones = [
        ("Noida Central Sectors", "Core residential",
         "The core Noida sectors cover a wide span of building ages, from the original planned sectors through to recent high-rise developments. Sector 18, the Atta Market area and Noida City Centre form the commercial heart, where retail and restaurant work means cassette and ducted systems serviced outside trading hours. The residential sectors are predominantly split systems, and the most common call we get is reduced cooling traced to condensers that have never been washed properly.",
         ["Sector 11", "Sector 12", "Sector 15", "Sector 18", "Sector 19", "Sector 22",
          "Sector 25", "Sector 26", "Sector 27", "Sector 29", "Sector 30", "Sector 34",
          "Sector 37", "Sector 44", "Sector 47", "Sector 50", "Sector 51", "Sector 52",
          "Noida City Centre", "Atta Market", "Botanical Garden"]),
        ("IT Corridor", "Corporate & data",
         "Sectors 62, 63, 125, 126 and 132 form Noida's IT and corporate belt, and this is where our most demanding technical work sits — server rooms and precision cooling where downtime carries direct financial consequence. These sites run on documented preventive maintenance with redundancy planning, because the strategy for a data centre is not fast repair, it is never failing in the first place. Film City adds broadcast facilities with their own continuous-operation requirements.",
         ["Sector 62", "Sector 63", "Sector 125", "Sector 126", "Sector 132", "Sector 135",
          "Sector 142", "Film City", "Techzone"]),
        ("Noida Expressway & New Sectors", "New high-rise",
         "The Expressway sectors — 137, 143, 150 and their neighbours — are dominated by recent high-rise apartment towers. Two issues recur here: fit-out installations done at speed during handover, and outdoor units placed in tight service shafts with insufficient clearance. Both show up as poor cooling that owners assume is a faulty machine when it is actually a siting and airflow problem, which is usually correctable.",
         ["Sector 137", "Sector 143", "Sector 150", "Sector 151", "Sector 168",
          "Yamuna Expressway", "Jaypee Greens", "Golf Foreste"]),
        ("Greater Noida", "Planned sectors",
         "Greater Noida's alphabetical sectors, Knowledge Park institutions and the Pari Chowk area cover a large geographic spread with lower density, which we plan routes around so response times stay realistic. Educational campuses here bring bulk servicing work that has to be completed within vacation windows, and we schedule those as projects rather than individual call-outs.",
         ["Alpha 1", "Alpha 2", "Beta 1", "Beta 2", "Gamma 1", "Gamma 2", "Chi", "Phi",
          "Omega", "Zeta", "Delta", "Knowledge Park 1", "Knowledge Park 2", "Knowledge Park 3",
          "Knowledge Park 4", "Knowledge Park 5", "Pari Chowk"]),
        ("Noida Extension", "High-density new build",
         "Noida Extension, covering Gaur City, Ace City, the Supertech developments and Crossing Republik, is dense new-build apartment housing. Volume is high and so is the proportion of installations that need correcting — insulation gaps and drain lines without proper fall are the two we see constantly, and both produce water damage that residents initially blame on the building rather than the AC fit-out.",
         ["Gaur City", "Ace City", "Supertech Eco Village", "Crossing Republik",
          "Noida Extension", "Bisrakh", "Greater Noida West"]),
    ]

    intro = ("<p>Noida and Greater Noida cover an unusually wide spread — from the original planned sectors "
             "through the <strong>IT corridor at Sectors 62 and 63</strong>, out along the Expressway to Sector 150, "
             "and across to Greater Noida's Knowledge Park.</p>"
             "<p>That spread means the work varies enormously. A data centre in Sector 62 needs precision cooling "
             "with redundancy planning; a new tower on the Expressway usually needs fit-out shortcuts corrected; "
             "a Greater Noida campus needs bulk servicing inside a vacation window. We plan our routing across "
             "this region so response times stay honest rather than optimistic.</p>")

    faqs = local_faqs("Noida", "all Noida sectors, Greater Noida, Noida Extension and the Yamuna Expressway corridor", extra=[
        ("Do you cover Greater Noida and Noida Extension as well as Noida?",
         "Yes — all three, including Gaur City, Ace City, the Supertech developments and Crossing Republik, plus the Greater Noida alphabetical sectors and Knowledge Park. Greater Noida is geographically spread out, so we plan routing accordingly and will give you a realistic slot rather than promising same-day everywhere."),
        ("Can you handle server room and precision cooling in the Noida IT sectors?",
         "Yes. Precision cooling for server rooms and data facilities across Sectors 62, 63, 125 and 132 is established work for us. These sites run on documented preventive maintenance with redundancy planning, because the objective is not fast repair — it is never failing in the first place."),
    ])

    return location_page(
        slug="ac-service-noida.html",
        title="AC Repair &amp; Service in Noida &amp; Greater Noida",
        desc="AC repair, service &amp; installation across Noida, Greater Noida &amp; Noida Extension. All sectors covered. Call +91 93122 64832.",
        h1="AC Repair, Service &amp; Installation in <em>Noida &amp; Greater Noida</em>",
        hero_sub="Every sector from the old core to Sector 150, plus Greater Noida and Noida Extension — including precision cooling for the Sector 62 and 63 IT corridor.",
        city="Noida", intro_html=intro, zones=zones, faqs=faqs,
        area_list=["Noida", "Greater Noida", "Noida Extension", "Delhi NCR"],
        xlinks=[
            ("ac-repair.html", "AC Repair", "Same-day diagnosis and repair across Noida and Greater Noida."),
            ("ac-servicing.html", "AC Servicing", "Deep cleaning and performance checks for every system type."),
            ("ac-amc.html", "AC AMC", "Documented preventive maintenance for offices and critical facilities."),
            ("ac-installation.html", "AC Installation", "New systems sized and commissioned properly."),
            ("ac-service-ghaziabad.html", "AC Service Ghaziabad", "Indirapuram, Vaishali and the NH-9 corridor."),
            ("ac-service-delhi.html", "AC Service Delhi", "Full zone-by-zone coverage across Delhi."),
        ])
