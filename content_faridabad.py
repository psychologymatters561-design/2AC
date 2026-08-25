#!/usr/bin/env python3
"""Faridabad location page content."""
from content_loc_common import location_page, local_faqs

# ============================================================= FARIDABAD ====
def faridabad():
    zones = [
        ("NIT & Old Faridabad", "Established areas",
         "NIT and Old Faridabad are the city's older established areas, with building stock that frequently needs its electrical supply assessed before any new installation goes in. Voltage fluctuation is a genuine and recurring issue in parts of this belt, and it destroys compressors and control boards over time. We check supply conditions properly and advise on stabilisation where it is actually needed — and tell you when it is not.",
         ["NIT 1", "NIT 2", "NIT 3", "NIT 4", "NIT 5", "Old Faridabad", "Dabua Colony",
          "RPS Colony", "Ashoka Enclave", "Ajronda"]),
        ("Sector Belt", "Planned sectors",
         "Faridabad's numbered sectors from 14 through 89 form the planned residential core, mixing independent houses with newer group housing. Split systems dominate, and the most frequent call is straightforward reduced cooling from condensers heavily fouled by road dust — this belt sits close to major arterial roads and the coils load up faster than owners expect. A proper condenser wash often restores performance people assumed was gone for good.",
         ["Sector 14", "Sector 15", "Sector 16", "Sector 17", "Sector 19", "Sector 21",
          "Sector 28", "Sector 29", "Sector 31", "Sector 37", "Sector 46", "Sector 48",
          "Sector 62", "Sector 75", "Sector 76", "Sector 78", "Sector 82", "Sector 85",
          "Sector 86", "Sector 88", "Sector 89"]),
        ("Greater Faridabad (Neharpar)", "New development",
         "Neharpar, generally referred to as Greater Faridabad, is the newer development belt including the BPTP and Omaxe projects. As with most recent high-rise construction across NCR, a significant share of our work here involves correcting original fit-out installations — insulation gaps, drain runs without proper fall and outdoor units sited where they cannot get airflow.",
         ["Neharpar", "Greater Faridabad", "BPTP", "Omaxe Heights", "SRS Residency",
          "Greenfields Colony", "Sector 84", "Sector 87"]),
        ("Surajkund & Southern Belt", "Premium & industrial",
         "The Surajkund and Badkhal belt holds premium residential properties and hospitality venues, while Ballabgarh anchors the industrial side with factories needing high-capacity cooling and ventilation rather than comfort systems. These are genuinely different jobs, and we resource them differently — industrial work is planned around production schedules and shutdown windows.",
         ["Surajkund", "Badkhal", "Mewla Maharajpur", "Ballabgarh",
          "Crown Interiorz Mall area", "Sector 37"]),
    ]

    intro = ("<p>Faridabad combines established residential areas, a large planned sector belt and a substantial "
             "<strong>industrial base around Ballabgarh</strong> — three quite different types of cooling work.</p>"
             "<p>Two local factors shape what we do here. Voltage fluctuation in parts of the older belt causes "
             "compressor and control board failures that get misdiagnosed as machine faults. And proximity to major "
             "arterial roads means condenser coils foul faster than owners expect, quietly costing cooling capacity "
             "every season. Both are straightforward to address once correctly identified.</p>")

    faqs = local_faqs("Faridabad", "NIT, Old Faridabad, all sectors, Neharpar (Greater Faridabad), Surajkund and Ballabgarh", extra=[
        ("Do you handle industrial AC and ventilation in Ballabgarh?",
         "Yes. Factory and warehouse work around Ballabgarh and the wider industrial belt is established for us, covering high-capacity cooling and industrial ventilation as well as comfort systems for office areas. We plan this work around production schedules and shutdown windows rather than expecting the plant to stop for us."),
    ])

    return location_page(
        slug="ac-service-faridabad.html",
        title="AC Repair &amp; Service in Faridabad | Air Control",
        desc="AC repair, service &amp; installation across Faridabad. NIT, Old Faridabad, all sectors, Neharpar, Surajkund &amp; Ballabgarh. Call +91 93122 64832.",
        h1="AC Repair, Service &amp; Installation in <em>Faridabad</em>",
        hero_sub="From NIT and Old Faridabad through the sector belt to Neharpar and the Ballabgarh industrial area — residential, commercial and industrial cooling.",
        city="Faridabad", intro_html=intro, zones=zones, faqs=faqs,
        area_list=["Faridabad", "Ballabgarh", "Greater Faridabad", "Delhi NCR"],
        xlinks=[
            ("ac-repair.html", "AC Repair", "Same-day diagnosis and repair across Faridabad."),
            ("ac-servicing.html", "AC Servicing", "Condenser washing and deep cleaning that restores lost cooling."),
            ("ac-amc.html", "AC AMC", "Planned maintenance for homes, offices and industrial sites."),
            ("ac-installation.html", "AC Installation", "Correctly sized systems with proper electrical assessment."),
            ("ac-service-delhi.html", "AC Service Delhi", "Full zone-by-zone coverage across Delhi."),
            ("ac-service-gurgaon.html", "AC Service Gurgaon", "DLF, Golf Course Road, Cyber City and all sectors."),
        ])
