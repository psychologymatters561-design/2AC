#!/usr/bin/env python3
"""AC AMC page content."""
from build import (render, lead_form, cross_links, emergency,
                   brand_chips, faq_html, PHONE_H)
from content_common import sec, head, cards, steps, stats_band

HOME = ("Home", "index.html")


# ================================================================ AC AMC ====
def ac_amc():
    trail = [HOME, ("Services", "ac-amc.html"), ("AC AMC Delhi NCR", None)]

    included = [
        ("📅", "Scheduled Preventive Visits", "Planned maintenance visits through the year, timed around the cooling season rather than left until something fails."),
        ("🌬", "Filter Cleaning & Replacement", "Filters cleaned or replaced at every visit — the single highest-impact maintenance task for both efficiency and air quality."),
        ("🌡", "Gas Pressure Checks", "Refrigerant pressures measured and recorded at each visit, so a slow leak is caught as a trend rather than as a breakdown."),
        ("🔌", "Electrical Inspection", "Capacitors, contactors, terminals, earthing and current draw checked. Loose terminals are a preventable fire risk we take seriously."),
        ("❄", "Coil & Condenser Cleaning", "Evaporator and condenser coils cleaned so heat transfer stays close to design, keeping run times and bills down."),
        ("🚿", "Drain Line Cleaning", "Drain lines cleared and fall verified before the monsoon, which is when blocked drains turn into damaged ceilings."),
        ("📊", "Performance Optimisation", "Temperature split, airflow and pressures measured against specification, with adjustments made to restore designed performance."),
        ("🚨", "Emergency Breakdown Cover", "When something does fail, you are covered — and you are not negotiating a price while the room heats up."),
        ("⚡", "Priority Response", "AMC clients go to the front of the queue. In peak summer, that difference is measured in days, not hours."),
        ("🔩", "Genuine Parts", "Authentic components sourced through proper channels. Counterfeit boards and compressors are common here and fail fast."),
        ("📋", "Detailed Service Reports", "A written report after every visit: what was checked, what was found, what was done, what to watch. Useful for audits and for warranty claims."),
        ("👷", "Named Engineers", "You deal with engineers who know your building and your systems, not a different stranger each visit."),
    ]

    who = [
        ("🏠", "Homes with Multiple ACs", "Once you have three or more units, coordinating servicing yourself becomes a genuine chore. An AMC makes it somebody else's job."),
        ("🏢", "Offices", "Staff comfort affects productivity, and a failed system in an open-plan floor affects everyone at once."),
        ("🛍", "Showrooms", "Customers do not linger in a warm showroom. For jewellery and luxury retail, climate stability also protects the stock."),
        ("🍽", "Restaurants", "Kitchen heat loads punish equipment, and a breakdown during service is lost revenue you cannot recover."),
        ("🏥", "Hospitals & Clinics", "Air quality and reliability are clinical requirements, not comfort preferences. Documentation matters for compliance."),
        ("🏨", "Hotels", "Guest complaints about room temperature convert directly into reviews. Quiet, reliable operation is the product."),
        ("🏭", "Factories", "Process cooling and worker comfort both depend on systems that are maintained rather than run until failure."),
        ("💾", "Data Centres", "Precision cooling with no tolerance for downtime. Preventive maintenance is the entire strategy."),
        ("😤", "Anyone Tired of Breakdowns", "If you have had the same argument with a different technician three summers running, an AMC is the structural fix."),
    ]

    faqs = [
        ("What is an AC AMC?",
         "An Annual Maintenance Contract is an agreement under which we take ongoing responsibility for maintaining your air conditioning systems across a year. Rather than calling somebody when something breaks, you get scheduled preventive visits, priority response when you need help, and a documented record of the condition of every unit. It shifts you from reacting to failures to preventing them."),
        ("How much does an AC AMC cost in Delhi?",
         "It depends on how many units you have, what type they are, where they are, and which level of cover you choose — a home with three split units and a hotel with sixty are not comparable. We survey the site, count and assess the systems, then quote. What we can say generally is that clients who move to an AMC after a bad breakdown year almost always spend less overall, because emergency repairs at peak season are the most expensive way to buy air conditioning."),
        ("Is an AC AMC actually worth it?",
         "For a single lightly used bedroom unit, probably not — book a service twice a year and you are fine. It becomes worth it once you have multiple units, or when a failure has consequences: a showroom losing customers, a clinic that must maintain air quality, a restaurant mid-service, a server room. The value is only partly the maintenance; it is also priority access in July when everyone else is waiting a week."),
        ("What is covered in your AC AMC?",
         "Scheduled preventive visits, filter cleaning and replacement, coil and condenser cleaning, drain line clearing, refrigerant pressure checks, electrical inspection, performance optimisation, emergency breakdown cover, priority response and written service reports after each visit. Precisely which of these apply, and how often, depends on the plan you select and what your site actually needs."),
        ("How many visits are included in an AC AMC?",
         "Our Essential plan covers two scheduled visits a year, timed before and during the cooling season. Professional covers four — effectively quarterly — plus breakdown cover. Enterprise is built around the site rather than a fixed count, with unlimited scheduled visits, two-hour priority response and named engineers. Most offices and showrooms land on Professional; critical facilities take Enterprise."),
        ("Does the AMC cover spare parts and gas?",
         "Cover varies by plan, and we are explicit about it in the contract rather than leaving it ambiguous. Consumables and routine items are included; major components such as compressors and PCBs are handled according to the plan level and the age of the equipment. We would rather have a clear conversation about this at the survey than an awkward one during a breakdown."),
        ("What happens if my AC breaks down outside a scheduled visit?",
         "You call us and we come — that is the point of the contract. AMC clients receive priority scheduling ahead of ad-hoc callers, and Enterprise clients have a two-hour response commitment. During peak summer this is the difference that clients tell us they value most, because availability matters more than price when the temperature is at 45 degrees."),
        ("Can I put an AMC on old air conditioners?",
         "Usually yes. We survey first and give you an honest assessment of each unit. If a particular system is genuinely at the end of its life, we will say so rather than sell you a contract to maintain something that should be replaced — and we would rather tell you that at the survey than a month into the contract."),
        ("Do you provide AMC for VRF and central AC systems?",
         "Yes. Commercial systems — VRF, VRV, central plant, chillers and AHUs — are a significant part of our AMC work, and have been for decades. These systems particularly reward planned maintenance, because component costs are high and unplanned downtime affects the whole building rather than one room."),
        ("How do I start an AMC with Air Control?",
         "Request a quote through the form on this page or call us on " + PHONE_H + ". We arrange a site survey, assess and log every unit, then propose a plan and maintenance schedule based on what is actually there. Once agreed, we take over scheduling entirely — you do not have to remember when the next visit is due."),
    ]

    tiers = """<div class="tiers">
  <div class="tier reveal">
    <h3>Essential</h3><div class="tier-sub">For homes &amp; small offices</div>
    <ul>
      <li>2 scheduled preventive visits per year</li>
      <li>Filter cleaning &amp; replacement</li>
      <li>Coil and condenser cleaning</li>
      <li>Drain line clearing</li>
      <li>Refrigerant pressure check</li>
      <li>Electrical safety inspection</li>
      <li>Written service report each visit</li>
      <li>Priority over non-contract callers</li>
    </ul>
    <button class="btn btn-outline" onclick="openChat()">Request Quote →</button>
  </div>
  <div class="tier featured reveal d1">
    <div class="tier-flag">Most Chosen</div>
    <h3>Professional</h3><div class="tier-sub">For offices, showrooms &amp; restaurants</div>
    <ul>
      <li><strong>4 scheduled visits per year</strong> (quarterly)</li>
      <li>Everything in Essential</li>
      <li><strong>Emergency breakdown cover</strong></li>
      <li>Priority response scheduling</li>
      <li>Performance optimisation each visit</li>
      <li>Genuine parts sourcing</li>
      <li>Pre-monsoon drainage inspection</li>
      <li>Annual system condition review</li>
    </ul>
    <button class="btn btn-gold" onclick="openChat()">Request Quote →</button>
  </div>
  <div class="tier reveal d2">
    <h3>Enterprise</h3><div class="tier-sub">For critical &amp; institutional facilities</div>
    <ul>
      <li><strong>Unlimited scheduled visits</strong></li>
      <li>Everything in Professional</li>
      <li><strong>2-hour priority response</strong></li>
      <li><strong>Named dedicated engineers</strong></li>
      <li>Full asset register &amp; service history</li>
      <li>Compliance-ready documentation</li>
      <li>VRF, central plant &amp; chiller cover</li>
      <li>Annual engineering review &amp; planning</li>
    </ul>
    <button class="btn btn-outline" onclick="openChat()">Request Quote →</button>
  </div>
</div>
<p class="text-center" style="margin-top:26px;font-size:13.5px;color:var(--muted);">
  Every plan is quoted after a site survey, because unit count, system type and site access change the work involved.
</p>"""

    table = """<div class="tbl-wrap reveal">
<table class="cmp">
  <thead><tr><th>Consideration</th><th>Pay Per Breakdown</th><th>With an AMC</th></tr></thead>
  <tbody>
    <tr><td>When work happens</td><td>After something has already failed</td><td>Before failure, on a schedule</td></tr>
    <tr><td>Peak-summer availability</td><td>Join the queue — often several days</td><td>Priority; 2-hour response on Enterprise</td></tr>
    <tr><td>Cost predictability</td><td>Unknown until it breaks</td><td>Known annual figure, budgeted upfront</td></tr>
    <tr><td>Pricing position</td><td>Negotiating while the room heats up</td><td>Agreed in advance, in writing</td></tr>
    <tr><td>Parts quality</td><td>Whatever the technician carries</td><td>Genuine parts through proper channels</td></tr>
    <tr><td>Equipment lifespan</td><td>Shortened by running dirty and stressed</td><td>Extended by consistent maintenance</td></tr>
    <tr><td>Running cost</td><td>Creeps up as coils foul</td><td>Held near design efficiency</td></tr>
    <tr><td>Record keeping</td><td>Scattered invoices, if any</td><td>Documented reports for every visit</td></tr>
    <tr><td>Warranty claims</td><td>Often refused for lack of maintenance evidence</td><td>Maintenance history on file</td></tr>
    <tr><td>Accountability</td><td>A different technician each time</td><td>One company, answerable across the year</td></tr>
  </tbody>
</table></div>"""

    body = "".join([
        sec("section", head("Start Here", "What Is an <em>AC AMC</em>?", center=False)
            + '<div class="prose reveal" style="max-width:860px;margin-top:8px;">'
            + '<p>An <strong>Annual Maintenance Contract</strong> is an agreement under which we take ongoing responsibility for keeping your air conditioning systems working, across a full year, rather than appearing only after something has broken.</p>'
            + '<p>The difference is more fundamental than it first sounds. Without a contract, air conditioning is a series of emergencies: a unit fails, you start ringing around, you accept whoever can come soonest at whatever they quote, and you repeat the process next season. With a contract, maintenance happens on a schedule you never have to think about, small problems are caught while they are still small, and when something does fail you are already a client rather than a stranger asking for a favour in the middle of July.</p>'
            + '<p>For a single bedroom unit, this is over-engineering — book a service twice a year and get on with your life. The calculation changes once you have several units, or once a failure carries real consequences: a showroom that empties when it gets warm, a clinic with air quality obligations, a restaurant mid-service, a server room where downtime is measured in money per minute.</p>'
            + '<p>This is the programme diplomatic missions, hospitals and Fortune 500 offices in Delhi have used with us for decades — not because it is glamorous, but because it removes an entire category of problem from their week.</p></div>'),
        stats_band(),
        sec("section section-cream", head("The Detail", "What's Included in <em>Our AMC</em>",
            "Every item below is performed and recorded. Which apply, and how often, depends on the plan and your site.")
            + cards(included)),
        sec("section", head("Choose Your Level", "AMC <em>Plans</em>",
            "Three levels of cover, from a straightforward household contract to full institutional support.")
            + tiers),
        sec("section section-cream", head("Who It Suits", "Who <em>Needs</em> an AC AMC?",
            "An honest filter — if none of these describe you, a twice-yearly service is probably enough.")
            + cards(who)),
        sec("section", head("The Comparison", "AMC vs Pay-Per-Service: <em>Why AMC Wins</em>",
            "The financial argument matters, but availability in peak season is what clients tell us they value most.")
            + table),
        sec("section section-dark",
            '<div class="text-center reveal"><span class="section-label text-gold">Our Record</span>'
            + '<div class="gold-rule center"></div>'
            + '<h2 class="headline text-white">Our AMC <em>Track Record</em></h2>'
            + '<p class="lead-text" style="max-width:620px;margin:16px auto 0;">Thirty-eight years of contracts that clients chose to keep renewing.</p></div>'
            + '<div class="pgrid" style="margin-top:44px;">'
            + '<div class="pcard reveal" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">'
            + '<div class="pcard-ic">🤝</div><h3 style="color:#fff;">15+ Year Average Retention</h3>'
            + '<p style="color:rgba(255,255,255,.6);">Our AMC clients stay, on average, more than fifteen years. In a trade where most relationships last a single season, that is the number we are proudest of.</p></div>'
            + '<div class="pcard reveal d1" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">'
            + '<div class="pcard-ic">🏛</div><h3 style="color:#fff;">Diplomatic &amp; Institutional</h3>'
            + '<p style="color:rgba(255,255,255,.6);">Fifteen-plus embassies and consulates, alongside hospitals, hotels and Fortune 500 offices — clients who audit their vendors annually.</p></div>'
            + '<div class="pcard reveal d2" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">'
            + '<div class="pcard-ic">🛡</div><h3 style="color:#fff;">Zero Safety Incidents</h3>'
            + '<p style="color:rgba(255,255,255,.6);">Thirty-eight years of refrigerant handling and electrical work without a safety incident. That is process and training, not good fortune.</p></div>'
            + '<div class="pcard reveal d3" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12);">'
            + '<div class="pcard-ic">📋</div><h3 style="color:#fff;">Documented Every Visit</h3>'
            + '<p style="color:rgba(255,255,255,.6);">Written reports for every visit, which is what makes warranty claims straightforward and compliance audits uneventful.</p></div>'
            + '</div>'),
        sec("section", head("How It Works", "How Our <em>AMC</em> Works")
            + steps([
                ("Enquiry", "Tell us roughly what you have — how many units, what type, what building. We can give you a sense of the right plan before anyone visits."),
                ("Site Survey", "We attend, inspect and log every unit: make, model, age, condition and access. You get an honest assessment, including any unit we think is beyond economic maintenance."),
                ("Plan & Schedule", "We propose a plan and a maintenance calendar built around your season and your operating hours, so visits do not land in the middle of your busiest period."),
                ("Scheduled Visits", "We turn up as scheduled. You do not have to track it, chase it or remember it — that transfer of responsibility is most of the value."),
                ("Emergency Support", "If something fails between visits, you have priority access, with a two-hour response commitment on Enterprise contracts."),
                ("Annual Review", "At renewal we review the year: what failed, what is ageing, what should be budgeted for replacement. Planning beats surprises."),
            ])),
        sec("section section-cream", head("Sectors", "Industries We Serve with <em>AMC</em>")
            + cards([
                ("🏛", "Diplomatic Facilities", "Embassies and consulates, where reliability, discretion and documented process are all non-negotiable."),
                ("🏢", "Corporate Offices", "Multi-floor offices and campuses, coordinated around working hours and facilities teams."),
                ("🛍", "Retail & Showrooms", "Including jewellery and luxury retail, where climate stability protects stock as well as comfort."),
                ("🏥", "Healthcare", "Hospitals and clinics with air quality requirements and compliance documentation obligations."),
                ("🏨", "Hospitality", "Hotels and restaurants where guest comfort is the product and quiet operation is part of it."),
                ("💾", "IT & Data Centres", "Precision cooling with redundancy planning and no tolerance for unplanned downtime."),
                ("🏭", "Industrial", "Factories and warehouses with process cooling and large-volume ventilation requirements."),
                ("🏠", "Premium Residential", "Homes with multiple units, VRF or ducted systems where coordination is genuinely worth outsourcing."),
            ])),
        sec("section", head("In Their Words", "What AMC <em>Clients</em> Say")
            + '<div class="rev-grid">'
            + '<div class="rev-card reveal"><div class="rev-stars">★★★★★</div>'
            + '<p class="rev-text">"Air Control has maintained our embassy\'s air conditioning for over 35 years. In a diplomatic facility we cannot compromise on reliability or safety. Their professionalism is exactly why we never considered switching."</p>'
            + '<div class="rev-footer"><div><div class="rev-name">Facilities Head</div><div class="rev-org">Vatican Embassy, New Delhi</div></div><span class="rev-verified">Verified</span></div></div>'
            + '<div class="rev-card reveal d1"><div class="rev-stars">★★★★★</div>'
            + '<p class="rev-text">"For a jewellery showroom, climate control is critical. Air Control installed our precision cooling 8 years ago and it hasn\'t given a single problem. Their AMC team is equally exceptional."</p>'
            + '<div class="rev-footer"><div><div class="rev-name">Priya Sharma</div><div class="rev-org">Tanishq, Connaught Place</div></div><span class="rev-verified">Verified</span></div></div>'
            + '<div class="rev-card reveal d2"><div class="rev-stars">★★★★★</div>'
            + '<p class="rev-text">"They installed our complete VRF system across 3 floors and have maintained it since. No shortcuts, and they turn up when they say they will — which in this trade is rarer than it should be."</p>'
            + '<div class="rev-footer"><div><div class="rev-name">R*j*sh M**h****</div><div class="rev-org">DHL Express</div></div><span class="rev-verified">Verified</span></div></div>'
            + '</div>'),
        sec("section section-dark", '<div class="text-center reveal">'
            + '<span class="section-label text-gold">Get Started</span>'
            + '<div class="gold-rule center"></div>'
            + '<h2 class="headline text-white">Request an <em>AMC Quote</em></h2>'
            + '<p class="lead-text" style="max-width:600px;margin:16px auto 0;">Tell us what you have. We survey, assess honestly and propose a plan that fits the site.</p></div>'
            + '<div style="margin-top:40px;">'
            + lead_form("Request an AMC Quote",
                        "The more detail you give us here, the more accurate our proposal will be before anyone visits.",
                        "AC AMC Enquiry — Air Control",
                        extra_fields="""<div class="frow">
      <div class="fld"><label>Number of AC Units *</label><select name="units" required>
        <option value="">Select...</option><option>1–3</option><option>4–6</option>
        <option>7–15</option><option>16–40</option><option>40+</option>
      </select></div>
      <div class="fld"><label>Building Type *</label><select name="building_type" required>
        <option value="">Select...</option>
        <option>Home / apartment</option><option>Office</option><option>Showroom / retail</option>
        <option>Restaurant / café</option><option>Hospital / clinic</option><option>Hotel</option>
        <option>Factory / warehouse</option><option>Data centre</option>
        <option>Diplomatic / institutional</option>
      </select></div>
    </div>
    <div class="frow">
      <div class="fld"><label>AC Types Installed</label><select name="ac_types">
        <option value="">Select...</option>
        <option>Split AC only</option><option>Split + window</option><option>Cassette</option>
        <option>Ducted</option><option>Central AC</option><option>VRF / VRV</option>
        <option>Mixed / multiple types</option>
      </select></div>
      <div class="fld"><label>Current Maintenance Status</label><select name="current_status">
        <option value="">Select...</option>
        <option>No maintenance at present</option><option>Ad-hoc, when something breaks</option>
        <option>Existing AMC with another company</option><option>Self-managed servicing</option>
      </select></div>
    </div>""")
            + '</div>' + emergency()),
        sec("section", head("Questions", "AC AMC <em>FAQs</em>") + faq_html(faqs)),
        sec("section section-cream", head("Keep Exploring", "Related <em>Services</em> &amp; Guides")
            + cross_links([
                ("blog/ac-amc-worth-it.html", "Is AC AMC Worth It?", "A straight cost-benefit analysis, including when the answer is honestly no."),
                ("ac-servicing.html", "AC Servicing", "One-off servicing if you are not ready for a contract."),
                ("ac-repair.html", "AC Repair", "Emergency and scheduled repair with 2-hour response across Delhi NCR."),
                ("ac-installation.html", "AC Installation", "New systems installed to a standard that makes maintenance straightforward."),
                ("why-us.html", "Why Air Control", "The engineering standards and safety record behind the contract."),
                ("ac-service-delhi.html", "AC Service in Delhi", "Zone-by-zone coverage across every part of Delhi."),
            ])),
    ])

    return render(
        slug="ac-amc.html",
        title="AC AMC in Delhi NCR | Annual Maintenance Contract",
        desc="AC AMC in Delhi NCR since 1987. Scheduled preventive visits, priority response, genuine parts. Trusted by 15+ embassies. Request a quote: +91 93122 64832.",
        h1="AC <em>Annual Maintenance Contract</em> — Premium Protection for Your Cooling Systems",
        hero_sub="Scheduled preventive maintenance, priority emergency response and documented service reports — the programme diplomatic missions, hospitals and Fortune 500 offices in Delhi have relied on for decades.",
        trail=trail, body=body, faqs=faqs,
        area=["Delhi", "New Delhi", "Gurgaon", "Noida", "Faridabad", "Ghaziabad"])
