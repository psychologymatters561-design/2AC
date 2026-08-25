#!/usr/bin/env python3
"""AC installation page content."""
from build import (render, lead_form, cross_links, emergency,
                   brand_chips, faq_html, PHONE_H)
from content_common import sec, head, cards, steps, stats_band

HOME = ("Home", "index.html")


# ====================================================== AC INSTALLATION ====
def ac_installation():
    trail = [HOME, ("Services", "ac-installation.html"), ("AC Installation Delhi NCR", None)]

    types_ = [
        ("🧱", "Split AC Installation", "The standard choice for homes and small offices. Correct indoor placement, proper pipe routing and a level, well-drained mount."),
        ("🪟", "Window AC Installation", "Secure framing, correct outward slope for drainage and proper sealing against heat and insect ingress."),
        ("⬜", "Cassette AC Installation", "Ceiling-recessed units for offices, showrooms and restaurants, set out so the four-way throw actually covers the room."),
        ("🗼", "Floor Standing AC", "High-capacity units for lobbies, halls and showrooms where a wall unit cannot move enough air."),
        ("🛠", "Ducted AC Installation", "Concealed systems with duct design, grille placement and airflow balancing so every room gets its share."),
        ("🏢", "Central AC Installation", "Central plant, chilled water systems and AHUs for larger buildings, designed around genuine load figures."),
        ("🔷", "VRF / VRV Systems", "Variable refrigerant flow for multi-zone commercial buildings, with individual zone control and high part-load efficiency."),
        ("🔗", "Multi-Split Systems", "Several indoor units on one outdoor unit — efficient where outdoor space is limited, provided the pipe runs are designed correctly."),
    ]

    spaces = [
        ("🏠", "Homes & Apartments", "Single rooms through to whole-home multi-zone systems, installed with attention to how the space is actually lived in."),
        ("🏢", "Offices", "Open-plan floors, cabins and meeting rooms — zoned so occupied areas are comfortable without cooling empty ones."),
        ("🛍", "Showrooms & Retail", "High footfall, large glazing and heavy lighting loads all change the calculation. Jewellery retail needs particularly tight control."),
        ("🍽", "Restaurants & Cafés", "Kitchen heat, dining comfort and ventilation have to be handled together or the dining room never settles."),
        ("🏥", "Hospitals & Clinics", "Filtration, air-change rates and reliability standards that go well beyond ordinary comfort cooling."),
        ("🏨", "Hotels", "Guest-room systems that must be genuinely quiet at night, with central control for housekeeping and engineering."),
        ("🏭", "Factories & Warehouses", "Large volumes, high heat loads and process requirements — often ventilation as much as cooling."),
        ("💾", "Data Centres", "Precision cooling with redundancy. Downtime is not an acceptable outcome, so the design assumes failure and plans around it."),
        ("🎓", "Schools & Colleges", "High occupancy in bursts, tight budgets and holiday-window installation schedules."),
    ]

    faqs = [
        ("How much does AC installation cost in Delhi?",
         "It depends on the system, the tonnage and — most of all — the site. A straightforward split AC with a short pipe run on an accessible wall is very different from a cassette unit needing ceiling work, or a long copper run to a rooftop condenser. We survey first, then quote for the actual job. Beware of a headline installation price that excludes copper piping, stabiliser, drainage and core cutting, because that is where the final bill usually doubles."),
        ("How long does AC installation take?",
         "A single split AC is typically three to five hours including pressure testing and commissioning. Cassette and ducted units take a full day or more because of ceiling and duct work. VRF and central systems run to a project schedule of days or weeks depending on scale. We would rather take the extra hour to braze and pressure-test properly than hand over a system that leaks in month three."),
        ("What is included in your AC installation?",
         "Site survey and load calculation, indoor and outdoor unit mounting, copper pipe routing with proper insulation, brazed joints, nitrogen pressure testing, vacuum evacuation, refrigerant charging to specification, drainage with correct fall, electrical connection with appropriate protection, commissioning and performance verification, plus handover documentation. Vacuum evacuation is the step most commonly skipped by cheap installers, and it is the one that quietly destroys compressors."),
        ("Which AC is best for a 150 sq ft room?",
         "For a typical 150 sq ft bedroom in Delhi, a 1.5 ton unit is usually right, though 1 ton can suffice for a shaded north-facing room on a lower floor. The variables that actually matter are direct sunlight, top-floor exposure, window area, ceiling height and occupancy. A west-facing top-floor room needs materially more capacity than the same square footage on the ground floor. We size on the room, not on a chart."),
        ("Should I choose an inverter or a non-inverter AC?",
         "For anything you run more than a few hours a day, inverter is the better choice — it modulates compressor speed instead of cycling on and off, which means lower running cost, steadier temperature and less noise. Non-inverter still makes sense for a guest room or a space used occasionally, where the lower upfront cost is not offset by running hours."),
        ("What star rating should I buy?",
         "For a primary bedroom or living room used daily through summer, a 5-star inverter unit generally pays back its premium within two to three seasons in Delhi's climate. For rooms used lightly, a 3-star unit is perfectly sensible. Ratings are measured under standard test conditions, so real-world savings depend on your usage — but the relative ranking still holds."),
        ("Do you install ACs bought from somewhere else?",
         "Yes. Many clients buy their unit online or during a sale and want it installed properly rather than by whoever the retailer sends. We install any brand, and we will tell you honestly during the survey if the unit you have bought is undersized or oversized for the space before we fit it."),
        ("Can you shift an existing AC to a new location?",
         "Yes — uninstallation, transport, reinstallation, fresh copper where the existing run cannot be reused safely, pressure testing and recharging. Shifting is where a lot of systems get quietly damaged, usually through bent pipes, contaminated lines or refrigerant simply vented to atmosphere. We recover refrigerant properly and re-commission the system at the new location."),
        ("Do you handle the electrical work and stabiliser?",
         "Yes. We check that your existing point and wiring can carry the load, install appropriate protection, and advise on whether a stabiliser is needed for your supply conditions. Many modern inverter units have wide voltage tolerance and do not need one — we will tell you if yours does rather than selling you a box you do not need."),
        ("What warranty do I get on installation?",
         "Your unit carries its manufacturer warranty, and our installation workmanship is warranted separately. This distinction matters: manufacturer warranties are frequently voided by poor installation — inadequate evacuation, incorrect charge, unsupported pipework. We document the commissioning readings at handover so there is evidence the system was set up to specification."),
    ]

    body = "".join([
        sec("section", head("Every System", "Types of <em>AC Installation</em>",
            "Whatever the system, the fundamentals are identical: correct sizing, clean pipework, proper evacuation and verified commissioning.")
            + cards(types_)),
        stats_band(),
        sec("section section-cream", head("Every Environment", "Installation for <em>Every Space</em>",
            "A jewellery showroom, a server room and a bedroom are three genuinely different engineering problems.")
            + cards(spaces)),
        sec("section", head("Non-Negotiables", "Our <em>Installation</em> Standards", center=False)
            + '<div class="prose reveal" style="max-width:840px;margin-top:8px;">'
            + '<p>Most air conditioners that fail early were not badly manufactured — they were badly installed. These are the steps we do not skip, whatever the quoted timeline.</p>'
            + '<h3>Precision pipe work and brazing</h3><p>Copper joints are brazed properly and pressure-tested with nitrogen before the system ever sees refrigerant. A poorly made joint produces a micro-leak that will not show up for months, then slowly starves the compressor.</p>'
            + '<h3>Full vacuum evacuation</h3><p>Air and moisture inside a refrigerant circuit form acids that corrode the compressor from within. We evacuate to a proper vacuum and hold it to confirm the system is tight. This is the single most commonly skipped step in cheap installations.</p>'
            + '<h3>Charging by weight</h3><p>Refrigerant is charged to the manufacturer\'s stated weight, adjusted for actual pipe run — not until the gauge "looks about right". Overcharging and undercharging both reduce capacity and shorten compressor life.</p>'
            + '<h3>Continuous insulation</h3><p>Every centimetre of suction line is insulated, including at the joints and where the pipe passes through the wall. Gaps cause condensation, which causes dripping, staining and eventually structural damp.</p>'
            + '<h3>Electrical safety</h3><p>Correct cable sizing, proper earthing, appropriate circuit protection and secure terminations. Loose terminals heat up over time and are a genuine and entirely avoidable fire risk.</p>'
            + '<h3>Drainage with real fall</h3><p>The drain line is run with continuous downward slope and tested with water before handover. Most "AC leaking water" calls a year later are drainage that was never set correctly on day one.</p>'
            + '<h3>Load calculation before selection</h3><p>We size on heat load — orientation, glazing, floor level, occupancy, appliances — not on floor area alone. Oversized systems short-cycle, dehumidify poorly and cost more to run than a correctly sized unit.</p></div>'),
        sec("section section-cream", head("All Major Brands", "AC <em>Brands</em> We Install") + brand_chips()),
        sec("section", head("Buying Advice", "How to Choose the <em>Right AC</em>", center=False)
            + '<div class="prose reveal" style="max-width:840px;margin-top:8px;">'
            + '<h3>Start with tonnage, but size on the room</h3>'
            + '<p>As a rough starting point in Delhi: up to 120 sq ft suits 1 ton, 120–180 sq ft suits 1.5 ton, and 180–250 sq ft suits 2 ton. Then adjust upward for a west or south-facing room, a top floor, large windows, high ceilings, more than two regular occupants, or heat-generating equipment. A top-floor west-facing room can genuinely need a full tonnage step above what the floor area alone suggests.</p>'
            + '<h3>Inverter versus non-inverter</h3>'
            + '<p>Inverter units vary compressor speed to match demand rather than switching fully on and off. For daily summer use that means lower bills, steadier room temperature and quieter running. Non-inverter remains reasonable for occasional-use rooms where the lower purchase price is not cancelled out by running hours.</p>'
            + '<h3>Star rating and payback</h3>'
            + '<p>In Delhi\'s long cooling season, a 5-star inverter unit in a heavily used room typically repays its premium within two to three summers. In a guest room used a dozen nights a year, it will not — buy the 3-star and spend the difference on getting the installation done properly.</p>'
            + '<h3>Copper condenser coils</h3>'
            + '<p>Copper coils are more repairable and generally more durable than aluminium alternatives, which matters in Delhi\'s corrosive urban air. Repairability is worth real money over a ten-year life.</p>'
            + '<h3>Do not economise on installation</h3>'
            + '<p>It is entirely possible to buy an excellent air conditioner and destroy its lifespan with a two-hour installation that skipped evacuation and pressure testing. If your budget is tight, buy a simpler unit and have it installed properly rather than the reverse.</p></div>'),
        sec("section section-cream", head("How We Work", "Our <em>Installation</em> Process")
            + steps([
                ("Site Survey", "We visit, measure the space, check orientation, glazing, floor level and electrical supply, and identify where units can actually be sited and serviced later."),
                ("Load Calculation", "Capacity is calculated from real heat load, not floor area. You get a recommendation with the reasoning explained, not just a number."),
                ("Selection Advice", "We advise on system type, tonnage, inverter choice and star rating — including when a cheaper unit is genuinely the sensible option."),
                ("Installation", "Mounting, brazed pipework, insulation, drainage and electrical work carried out to the standards above, with the site protected throughout."),
                ("Testing & Commissioning", "Nitrogen pressure test, vacuum evacuation, charging by weight, then measured verification of cooling performance."),
                ("Handover & Documentation", "We walk you through operation and maintenance, and hand over commissioning readings and warranty documentation."),
            ])),
        sec("section section-dark", '<div class="text-center reveal">'
            + '<span class="section-label text-gold">Plan Your Installation</span>'
            + '<div class="gold-rule center"></div>'
            + '<h2 class="headline text-white">Get a Free <em>Site Survey</em></h2></div>'
            + '<div style="margin-top:40px;">'
            + lead_form("Request an Installation Quote",
                        "Tell us about the space and we will arrange a survey. No obligation, and honest advice on sizing.",
                        "AC Installation Enquiry — Air Control",
                        extra_fields="""<div class="frow">
      <div class="fld"><label>System Type *</label><select name="system_type" required>
        <option value="">Select system...</option>
        <option>Split AC</option><option>Window AC</option><option>Cassette AC</option>
        <option>Floor standing</option><option>Ducted AC</option><option>Central AC</option>
        <option>VRF / VRV</option><option>Not sure — please advise</option>
      </select></div>
      <div class="fld"><label>Property Type *</label><select name="property_type" required>
        <option value="">Select property...</option>
        <option>Home / apartment</option><option>Office</option><option>Showroom / retail</option>
        <option>Restaurant / café</option><option>Hospital / clinic</option><option>Hotel</option>
        <option>Factory / warehouse</option><option>Data centre</option><option>School / college</option>
      </select></div>
    </div>""")
            + '</div>' + emergency()),
        sec("section", head("Questions", "AC Installation <em>FAQs</em>") + faq_html(faqs)),
        sec("section section-cream", head("Keep Exploring", "Related <em>Services</em> &amp; Guides")
            + cross_links([
                ("ac-amc.html", "AC AMC", "Protect a new installation with scheduled maintenance from day one."),
                ("ac-servicing.html", "AC Servicing", "Keep the system performing at the level it was commissioned to."),
                ("ac-repair.html", "AC Repair", "Diagnosis and repair for systems already installed, whoever fitted them."),
                ("blog/best-ac-for-home.html", "Best AC for Home", "A fuller buying guide covering brands, tonnage and inverter choice."),
                ("ac-service-gurgaon.html", "AC Service Gurgaon", "Installation and service across DLF, Golf Course Road and all sectors."),
                ("ac-service-noida.html", "AC Service Noida", "Coverage across Noida, Greater Noida and Noida Extension."),
            ])),
    ])

    return render(
        slug="ac-installation.html",
        title="AC Installation in Delhi NCR | Split, VRF &amp; Central AC",
        desc="Professional AC installation across Delhi NCR since 1987. Split, cassette, ducted, central &amp; VRF systems. Call +91 93122 64832.",
        h1="Professional <em>AC Installation</em> in Delhi NCR",
        hero_sub="Most air conditioners that fail early were not badly made — they were badly installed. We size on real heat load, braze and pressure-test properly, evacuate fully and charge by weight, then prove the performance before we leave.",
        trail=trail, body=body, faqs=faqs,
        area=["Delhi", "New Delhi", "Gurgaon", "Noida", "Faridabad", "Ghaziabad"])
