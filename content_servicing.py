#!/usr/bin/env python3
"""AC servicing page content."""
from build import (render, lead_form, cross_links, emergency,
                   brand_chips, faq_html, PHONE_H)
from content_common import sec, head, cards, steps, stats_band

HOME = ("Home", "index.html")


# ========================================================== AC SERVICING ====
def ac_servicing():
    trail = [HOME, ("Services", "ac-servicing.html"), ("AC Servicing Delhi NCR", None)]

    services = [
        ("🧹", "General AC Service", "The standard periodic service — filter cleaning, coil check, drain clearing, gas pressure verification and a full performance check."),
        ("🫧", "Deep Cleaning (Foam Wash)", "Chemical foam is worked through the evaporator coil to lift the grime a surface clean cannot reach, then flushed thoroughly."),
        ("💦", "Jet Wash / Pressure Cleaning", "High-pressure water cleaning of condenser and evaporator coils, restoring the heat transfer that dirt has been blocking."),
        ("⛽", "Gas Filling & Top-Up", "R32, R410A and R22 charging by weight to manufacturer specification — always after finding and repairing the leak first."),
        ("🌬", "Filter Cleaning & Replacement", "Filters are the single biggest cause of poor cooling and high bills. Cleaned, or replaced where the mesh has degraded."),
        ("🌡", "Coil Cleaning", "Evaporator and condenser coils cleaned so the system can actually reject heat instead of struggling against a layer of dust."),
        ("🔄", "Condenser Wash", "The outdoor unit takes the worst of Delhi's dust and pollution. A proper wash here has the biggest single effect on efficiency."),
        ("🚿", "Drain Pipe Cleaning", "Blocked drain lines cleared and the fall corrected, which is what stops water dripping down your wall next month."),
        ("🧴", "Sanitisation & Deodorising", "Anti-microbial treatment of coil and drain pan to eliminate the musty smell at its source rather than masking it."),
        ("🔌", "Electrical Inspection", "Capacitors, contactors, terminals and current draw checked. Loose terminals are a common and entirely preventable fire risk."),
        ("📊", "Performance Check", "Temperature split, pressures and airflow measured against specification, so you get a factual report on how the system is actually performing."),
        ("🧯", "Safety Inspection", "Refrigerant leak check, earthing verification and mounting-bracket inspection — particularly important on older outdoor units."),
    ]

    signs = [
        ("🌡", "Reduced Cooling", "It runs longer to reach the same temperature, or never quite gets there. Usually dirty coils or low refrigerant."),
        ("💸", "Higher Electricity Bills", "A neglected AC can draw significantly more power for the same cooling. Servicing frequently pays for itself over a season."),
        ("👃", "Musty Smell", "Microbial growth on the coil. It affects indoor air quality and only gets worse if left."),
        ("💧", "Water Dripping", "A blocked drain line. Left alone it damages walls, ceilings and furniture."),
        ("🔊", "Unusual Sounds", "Rattles, hums and grinding indicate loose parts or worn bearings — cheap now, expensive later."),
        ("🔁", "Switching On and Off Often", "Short cycling stresses the compressor, the most expensive component in the system."),
        ("🌬", "Weak Airflow", "Clogged filters or a tired blower. Simple to fix, and immediately noticeable."),
        ("🕒", "Over Six Months Since Last Service", "In Delhi's dust and air quality, six months of heavy use is genuinely a long time."),
    ]

    faqs = [
        ("How often should an AC be serviced?",
         "In Delhi NCR we recommend every three to six months for regular household use. Our conditions are harsher than most of India — construction dust, high pollution and long summers all load the coils and filters faster. Light or seasonal use can stretch to twice a year, but a commercial kitchen, a showroom or anything running twelve hours a day should be on a quarterly schedule at minimum."),
        ("What is included in an AC service?",
         "A proper service includes filter cleaning, evaporator and condenser coil cleaning, condenser washing, drain line clearing, refrigerant pressure verification, electrical inspection of capacitors, contactors and terminals, and a measured performance check of temperature split and airflow. If somebody is in and out in fifteen minutes having only wiped the filter, that was not a service."),
        ("What is the difference between AC service and AC repair?",
         "Servicing is planned maintenance to keep a working system working — cleaning, checking and adjusting. Repair is fixing something that has already failed. The relationship between them is straightforward: consistent servicing prevents the large majority of repairs, because most breakdowns start as dirt, restricted airflow or a small leak that nobody caught."),
        ("How much does AC servicing cost in Delhi?",
         "It varies by system type and by whether you need a general service or a full deep clean with foam and jet wash. A single split unit and a multi-head cassette system are very different jobs. We quote after knowing what you have — and if you have several units, or want servicing scheduled through the year, an AMC generally works out considerably better value."),
        ("Does AC servicing include gas filling?",
         "No, and you should be cautious of anyone who bundles it in automatically. Refrigerant is a sealed system — it is not consumed, so if it is low, there is a leak. We check gas pressure as part of every service, and if it is down we find the leak, repair it and then recharge to the correct weight. Simply topping up a leaking system means paying again in a few months."),
        ("How long does an AC service take?",
         "A general service on a single split AC is usually forty-five to ninety minutes. A deep clean with foam wash and jet washing takes longer, typically ninety minutes to two hours per unit, because the coil is treated and flushed properly rather than wiped. Cassette and ducted systems take longer again."),
        ("Will servicing reduce my electricity bill?",
         "Usually yes, sometimes substantially. Dirty coils and clogged filters force the compressor to run longer and harder to achieve the same room temperature. Restoring proper heat transfer and airflow directly reduces run time. The worse the neglect, the bigger the improvement you will notice."),
        ("Can you service the AC without removing it from the wall?",
         "Yes. The great majority of servicing, including deep foam cleaning, is done in place with proper covers and drainage to protect your wall and floor. Full dismantling is only necessary in specific cases such as severe contamination or when a component behind the unit needs access — and we would explain why before doing it."),
        ("Do you service commercial and office AC systems?",
         "Yes. Offices, showrooms, restaurants, clinics, hotels and factories are a large part of our work, including cassette, ducted, central and VRF/VRV systems. For multiple units we normally recommend a maintenance contract so servicing happens on schedule rather than when someone notices a problem."),
        ("What is the best time of year to service an AC?",
         "Ideally just before summer, in February or March, so the system is at full capability when you start relying on it and any parts needed can be sourced without the peak-season wait. The second best time is genuinely right now — a neglected unit does not improve by waiting, and mid-season service still restores most of the lost efficiency."),
    ]

    body = "".join([
        sec("section", head("What We Do", "Types of <em>AC Servicing</em> We Offer",
            "From a routine tune-up to a full strip-down deep clean — done thoroughly, not superficially.")
            + cards(services)),
        stats_band(),
        sec("section section-cream", head("Timing", "How Often Should You <em>Service</em> Your AC?", center=False)
            + '<div class="prose reveal" style="max-width:820px;margin-top:8px;">'
            + '<p>The honest answer for Delhi NCR is <strong>every three to six months</strong> — and that is not an upsell, it is a reflection of the conditions here. Delhi air carries construction dust, vehicular particulates and seasonal pollution at levels that load filters and coat coils far faster than in most cities. An air conditioner is fundamentally a heat exchanger, and a heat exchanger covered in dust cannot exchange heat.</p>'
            + '<h3>Residential use</h3><p>For a typical home running the AC through summer, twice a year works: a thorough service before summer begins and another midway through the heavy-use months. If you are near a construction site, a main road, or you keep pets, move to quarterly.</p>'
            + '<h3>Commercial use</h3><p>Offices, restaurants, showrooms and clinics should be on a quarterly schedule as a minimum. Kitchens need more frequent attention because grease-laden air coats coils quickly and dramatically reduces heat transfer.</p>'
            + '<h3>Critical environments</h3><p>Server rooms, laboratories, operating theatres and jewellery showrooms need scheduled preventive maintenance with documented checks. This is precisely what our AMC programme was built around, and why institutional clients have stayed with it for decades.</p></div>'),
        sec("section", head("Warning Signs", "Signs Your AC <em>Needs Servicing</em>",
            "Your air conditioner usually signals trouble well before it fails. These are the signals worth acting on.")
            + cards(signs)),
        sec("section section-cream", head("How We Work", "Our <em>Servicing</em> Process")
            + steps([
                ("Booking & Assessment", "Tell us your system type and when it was last serviced. We schedule a slot and arrive with the right equipment for your specific units."),
                ("Inspection & Testing", "Before touching anything we record how the system is currently performing — pressures, temperature split, airflow and electrical draw."),
                ("Deep Clean", "Filters, evaporator coil, condenser coil and drain line are cleaned properly, with covers and drainage protecting your walls and floors."),
                ("Verify & Report", "We re-measure performance after cleaning, show you the difference, note anything that needs watching, and leave the site clean."),
            ])),
        sec("section", head("All Major Brands", "Every <em>Brand</em> Serviced") + brand_chips()),
        sec("section section-cream", head("The Payoff", "Benefits of Regular <em>AC Servicing</em>")
            + cards([
                ("💰", "Lower Electricity Bills", "Clean coils and clear filters let the compressor reach target temperature faster and run less. On a neglected system the saving is immediately noticeable."),
                ("📅", "Longer System Life", "Compressors fail from stress — running hot, running long, running against restricted airflow. Servicing removes that stress and adds years."),
                ("🌬", "Better Indoor Air Quality", "Your AC circulates the air your family or staff breathe all day. A clean, sanitised coil matters more than most people realise."),
                ("🛡", "Fewer Breakdowns", "The overwhelming majority of emergency calls trace back to something a routine service would have caught early and cheaply."),
                ("❄", "Consistent Cooling", "Rooms cool evenly and hold temperature, instead of the system struggling through the hottest part of the afternoon."),
                ("🧾", "Warranty Protection", "Most manufacturers require evidence of regular maintenance for warranty claims. We document every visit, so you have the record."),
            ])),
        sec("section section-dark", '<div class="text-center reveal">'
            + '<span class="section-label text-gold">Book a Service</span>'
            + '<div class="gold-rule center"></div>'
            + '<h2 class="headline text-white">Get Your AC <em>Properly</em> Serviced</h2></div>'
            + '<div style="margin-top:40px;">'
            + lead_form("Book an AC Service",
                        "Tell us what you have and when it was last serviced. We will confirm a slot within 2 hours.",
                        "AC Servicing Enquiry — Air Control",
                        extra_fields="""<div class="frow">
      <div class="fld"><label>Service Required *</label><select name="service_type" required>
        <option value="">Select service...</option>
        <option>General service</option><option>Deep cleaning (foam + jet wash)</option>
        <option>Gas filling / top-up</option><option>Sanitisation &amp; deodorising</option>
        <option>Multiple units — need a quote</option><option>Not sure — please advise</option>
      </select></div>
      <div class="fld"><label>Number of AC Units *</label><select name="units" required>
        <option value="">Select...</option><option>1</option><option>2–3</option>
        <option>4–6</option><option>7–15</option><option>15+</option>
      </select></div>
    </div>""")
            + '</div>' + emergency()),
        sec("section", head("Questions", "AC Servicing <em>FAQs</em>") + faq_html(faqs)),
        sec("section section-cream", head("Keep Exploring", "Related <em>Services</em> &amp; Guides")
            + cross_links([
                ("ac-repair.html", "AC Repair", "Something already broken? Diagnosis and repair with a 2-hour emergency response."),
                ("ac-amc.html", "AC AMC", "Put servicing on a schedule with priority response and documented visits."),
                ("ac-installation.html", "AC Installation", "New systems installed to engineering standard, sized by proper load calculation."),
                ("blog/how-often-ac-service.html", "How Often to Service?", "A fuller guide to servicing frequency by usage pattern and environment."),
                ("blog/ac-gas-filling-cost-delhi.html", "AC Gas Filling Guide", "What gas top-up involves and why the leak must be found first."),
                ("ac-service-delhi.html", "AC Service in Delhi", "Every locality we cover, zone by zone across Delhi."),
            ])),
    ])

    return render(
        slug="ac-servicing.html",
        title="AC Service in Delhi NCR | Deep Cleaning &amp; Gas Filling",
        desc="Professional AC servicing across Delhi NCR since 1987. Deep cleaning, foam wash, gas filling, coil cleaning. Call +91 93122 64832.",
        h1="Professional <em>AC Servicing</em> in Delhi NCR",
        hero_sub="Deep cleaning, gas top-up, coil and condenser washing and full performance checks — carried out thoroughly by engineers who measure results rather than just wipe a filter and leave.",
        trail=trail, body=body, faqs=faqs,
        area=["Delhi", "New Delhi", "Gurgaon", "Noida", "Faridabad", "Ghaziabad"])
