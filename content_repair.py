#!/usr/bin/env python3
"""AC repair page content."""
from build import (render, lead_form, cross_links, emergency,
                   brand_chips, faq_html, PHONE_H)
from content_common import sec, head, cards, steps, stats_band

HOME = ("Home", "index.html")


# ============================================================ AC REPAIR ====
def ac_repair():
    trail = [HOME, ("Services", "ac-repair.html"), ("AC Repair Delhi NCR", None)]

    problems = [
        ("❄", "AC Not Cooling", "The most common call we get. Usually low refrigerant, a clogged filter, a dirty condenser coil or a failing compressor. We measure pressures and temperature split before replacing anything."),
        ("💨", "AC Running But Not Cold", "Air moves but never chills. Typically a refrigerant leak, iced evaporator coil or a compressor that starts but does not build pressure."),
        ("🫧", "Refrigerant Gas Leak", "We trace leaks with electronic detectors and nitrogen pressure testing, repair the joint properly, then recharge to the manufacturer's stated weight — not by guesswork."),
        ("💧", "Water Leaking Indoors", "Almost always a blocked drain line, a cracked drain pan or an incorrectly sloped indoor unit. We clear the line and correct the fall so it does not return."),
        ("🔊", "Strange Noises", "Rattling, grinding or screeching each point somewhere different — loose panels, worn fan bearings or compressor trouble. We diagnose by sound signature and inspection."),
        ("👃", "Bad Smell From AC", "Musty odours mean microbial growth on the coil or in the drain pan. Burning smells mean stop using it and call us immediately — that is electrical."),
        ("⚡", "AC Tripping the MCB", "A short circuit, a seized compressor drawing locked-rotor current or an undersized circuit. We test insulation resistance and current draw before restoring power."),
        ("🧊", "Frozen Coils / Ice on Pipes", "Ice forms when airflow is restricted or refrigerant is low. Running it frozen destroys compressors, so switch to fan-only and call us."),
        ("🔌", "AC Not Turning On", "Could be as simple as a tripped breaker or as involved as a failed PCB or capacitor. We work from supply side inward so you pay for the actual fault."),
        ("🖥", "PCB / Control Board Failure", "Inverter boards fail from voltage spikes and moisture. We test the board properly and replace only when genuinely faulty — boards are expensive."),
        ("🌀", "Fan Motor Problems", "Indoor blower or outdoor fan motors seize, lose bearings or burn windings. Symptoms are weak airflow, noise or a unit that cuts out on high pressure."),
        ("🔁", "AC Short Cycling", "Turning on and off every few minutes stresses the compressor badly. Causes include oversizing, low refrigerant, a dirty coil or a faulty thermostat."),
        ("📱", "Remote Not Working", "Often just batteries or a paired-mode setting — we will tell you honestly if that is all it is rather than booking a service call."),
    ]

    types_ = [
        ("🧱", "Split AC Repair", "Wall-mounted split units of every brand and tonnage — the most common system in Delhi homes and offices."),
        ("🪟", "Window AC Repair", "Still widely used and entirely serviceable. We repair rather than push replacement where the unit has life left."),
        ("⬜", "Cassette AC Repair", "Ceiling cassettes in offices, showrooms and restaurants, including four-way and two-way units."),
        ("🗼", "Tower / Floor Standing AC", "High-capacity floor units for lobbies, banquet halls and showrooms."),
        ("🛠", "Ducted AC Repair", "Concealed ducted systems where diagnosis means understanding the whole air path, not just the machine."),
        ("🏢", "Central AC Repair", "Central plant systems for larger buildings — chilled water, AHUs and associated controls."),
        ("🔷", "VRF / VRV Systems", "Variable refrigerant flow systems require manufacturer-level diagnostics. We have run these for institutional clients for decades."),
        ("🧳", "Portable AC Repair", "Portable and standalone units for temporary or supplementary cooling."),
    ]

    faqs = [
        ("Why is my AC not cooling even though it is running?",
         "Nine times out of ten it is one of four things: low refrigerant from a leak, a badly clogged air filter, a dirty outdoor condenser coil, or a compressor that is no longer pumping properly. A technician should measure the suction and discharge pressures and the temperature split across the coil before recommending anything. If somebody wants to add gas without first finding where the old gas went, get a second opinion — refrigerant does not get consumed, so if it is low, it leaked."),
        ("How much does AC repair cost in Delhi?",
         "It depends entirely on the fault. Clearing a blocked drain line is a small job; replacing a compressor or an inverter PCB is a significant one. We do not publish fixed prices because quoting before diagnosis is how customers get overcharged. Our engineer diagnoses the fault, explains exactly what failed and why, and quotes before any work begins. You approve the cost first — there are no surprises on the invoice."),
        ("How long does an AC repair take?",
         "Most common repairs — gas leak repair and recharge, capacitor replacement, drain cleaning, fan motor replacement, sensor faults — are completed in a single visit of one to three hours. Jobs needing a part we do not carry on the vehicle, such as a specific inverter board or compressor, typically take one to three days depending on brand availability."),
        ("Do you provide same-day AC repair?",
         "Yes. For most of Delhi NCR we offer same-day attendance, and for genuine emergencies we target a two-hour response. Call us on " + PHONE_H + " — during peak summer, calling early in the day gives you the best chance of a same-day slot."),
        ("Do you repair all AC brands?",
         "Yes. We repair Daikin, Blue Star, Voltas, LG, Samsung, Hitachi, Carrier, O General, Mitsubishi, Panasonic, Godrej, Lloyd, Whirlpool, Haier, Toshiba and Sanyo, across split, window, cassette, tower, ducted, central and VRF/VRV systems. Thirty-eight years in the trade means very few faults are new to us."),
        ("Is my AC worth repairing or should I replace it?",
         "Our honest rule of thumb: if the unit is under eight years old and the repair costs less than about a third of a new system, repair it. If it is over twelve years old, using obsolete R-22 refrigerant, and facing compressor failure, replacement usually makes better financial sense. We will tell you plainly which side of that line you are on, even when replacement is not the answer that earns us more."),
        ("Do you offer a warranty on repairs?",
         "Yes. Every repair is warranted, and any spare part we fit carries its manufacturer warranty. We document what was replaced and why on the service report, so you have a record — this matters especially for AMC clients and for institutional buyers who need an audit trail."),
        ("My AC smells bad when I switch it on. Is that dangerous?",
         "A musty or sour smell is microbial growth on the evaporator coil and in the drain pan — unpleasant and bad for indoor air quality, but not dangerous. A deep clean resolves it. A burning or electrical smell is different: switch the unit off at the breaker and call us straight away, as that indicates an electrical fault that can become a fire risk."),
        ("Can you repair an AC that another technician has already worked on?",
         "Yes, and we do it often. We will assess the current state of the system honestly, including any previous work that was not done correctly — improper flare joints, incorrect gas charge and missing insulation are the three we see most. We tell you what we find without drama and quote to put it right."),
        ("Do you charge a visit fee if I decide not to proceed?",
         "We charge for the diagnostic visit itself, because proper diagnosis takes an engineer's time and instruments. That charge is told to you upfront when you book, never added afterwards, and it is adjusted against the repair cost if you go ahead with the work."),
    ]

    body = "".join([
        sec("section", head("Diagnostic Expertise", "Common <em>AC Problems</em> We Fix",
            "If your air conditioner is doing something it should not, it is almost certainly on this list — and we have fixed it several thousand times.")
            + cards(problems)),
        stats_band(),
        sec("section section-cream", head("Every System Type", "Types of AC We <em>Repair</em>",
            "From a single bedroom split to a multi-floor VRF installation, the same diagnostic discipline applies.")
            + cards(types_)),
        sec("section", head("All Major Brands", "AC <em>Brands</em> We Repair",
            "We carry brand-specific diagnostic knowledge and source genuine spare parts — never counterfeit components.")
            + brand_chips()),
        sec("section section-cream", head("How We Work", "Our <em>Repair</em> Process")
            + steps([
                ("Call or WhatsApp", "Tell us what the AC is doing. We ask the right questions upfront so our engineer arrives prepared with the likely parts already on the vehicle."),
                ("On-Site Diagnosis", "We measure rather than guess — pressures, temperature split, current draw and insulation resistance. Then we explain the actual fault in plain language."),
                ("Approved Repair", "You get the cost before we start. We use genuine parts and repair properly: correct joints, correct insulation, correct refrigerant charge by weight."),
                ("Testing & Warranty", "We run the system, verify cooling performance against specification, document what was done, and hand over with warranty on the work."),
            ])),
        sec("section", head("Why Air Control", "Why Choose Us for <em>AC Repair</em>")
            + cards([
                ("🏛", "38 Years, One Standard", "Founded in 1987 and still family-run. The engineer who quotes your job is accountable for it — there is no call-centre layer between you and the people doing the work."),
                ("🛡", "Embassy-Trusted", "Fifteen-plus diplomatic missions, Fortune 500 offices, hospitals and jewellery showrooms rely on us. These clients audit their vendors — we pass, year after year."),
                ("⚡", "2-Hour Emergency Response", "When cooling is critical — a server room, a restaurant kitchen, a clinic — we treat it as critical. Two-hour response across Delhi NCR."),
                ("🔩", "Genuine Parts Only", "We source authentic spares. Counterfeit compressors and boards are common in this market and they fail fast, usually taking something else with them."),
                ("📋", "Documented & Warranted", "Every repair is written up: what failed, what was replaced, what we recommend next. Warranty on our workmanship, manufacturer warranty on parts."),
                ("🎓", "Trained Engineers", "Our people are trained on refrigerant handling and electrical safety. Zero safety incidents in thirty-eight years is not luck — it is process."),
            ])),
        sec("section section-dark", '<div class="text-center reveal">'
            + '<span class="section-label text-gold">Book a Repair</span>'
            + '<div class="gold-rule center"></div>'
            + '<h2 class="headline text-white">Get Your AC Fixed <em>Properly</em></h2></div>'
            + '<div style="margin-top:40px;">'
            + lead_form("Request an AC Repair Visit",
                        "Tell us what is happening and our engineer will call you within 2 hours to confirm a slot.",
                        "AC Repair Enquiry — Air Control",
                        extra_fields="""<div class="frow">
      <div class="fld"><label>AC Type *</label><select name="ac_type" required>
        <option value="">Select AC type...</option>
        <option>Split AC</option><option>Window AC</option><option>Cassette AC</option>
        <option>Tower / Floor Standing</option><option>Ducted AC</option>
        <option>Central AC</option><option>VRF / VRV</option><option>Not sure</option>
      </select></div>
      <div class="fld"><label>Main Problem *</label><select name="problem" required>
        <option value="">Select the problem...</option>
        <option>Not cooling</option><option>Running but not cold</option><option>Gas leak</option>
        <option>Water leaking</option><option>Strange noise</option><option>Bad smell</option>
        <option>Tripping MCB</option><option>Not turning on</option><option>Ice on pipes</option>
        <option>Other / not sure</option>
      </select></div>
    </div>""")
            + '</div>' + emergency()),
        sec("section", head("Questions", "AC Repair <em>FAQs</em>") + faq_html(faqs)),
        sec("section section-cream", head("Keep Exploring", "Related <em>Services</em> &amp; Areas")
            + cross_links([
                ("ac-servicing.html", "AC Servicing", "Deep cleaning, gas top-up and preventive maintenance that stops breakdowns before they start."),
                ("ac-amc.html", "AC AMC", "Annual maintenance contracts with priority response — the programme our institutional clients use."),
                ("ac-installation.html", "AC Installation", "Split, cassette, ducted, central and VRF systems installed to engineering standard."),
                ("ac-service-delhi.html", "AC Service in Delhi", "Every zone and locality we cover across Delhi, with engineers stationed nearby."),
                ("blog/ac-not-cooling.html", "AC Not Cooling?", "Twelve reasons your AC has stopped cooling and how each one is diagnosed."),
                ("blog/ac-gas-filling-cost-delhi.html", "AC Gas Filling Guide", "What gas refilling actually involves, and why a leak must be found first."),
            ])),
    ])

    return render(
        slug="ac-repair.html",
        title="AC Repair in Delhi NCR | Emergency AC Repair | Air Control",
        desc="Expert AC repair across Delhi NCR since 1987. Not cooling, gas leaks, noise, tripping — fixed properly. 2-hour emergency response. Call +91 93122 64832.",
        h1="Expert <em>AC Repair</em> Service in Delhi NCR",
        hero_sub="Not cooling, leaking, tripping or making a noise it never used to? Our engineers diagnose the real fault, explain it plainly and fix it properly — the same standard that has kept embassies and Fortune 500 offices with us for thirty-eight years.",
        trail=trail, body=body, faqs=faqs,
        area=["Delhi", "New Delhi", "Gurgaon", "Noida", "Faridabad", "Ghaziabad"])
