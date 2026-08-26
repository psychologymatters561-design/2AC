#!/usr/bin/env python3
"""Article: how often to service an AC."""
from build_blog import render_article

FAQS = [
    ("How often should an AC be serviced in Delhi?",
     "Every three to six months for normal household use. Delhi is harsher on air conditioners than most of India: construction dust, high particulate pollution and a cooling season that runs most of the year all load filters and coat coils faster. Light or seasonal use can stretch to twice a year. Anything running long hours should be on a quarterly schedule."),
    ("Is servicing before summer enough?",
     "For a lightly used bedroom unit, often yes. For a system running daily through a Delhi summer, one service in March means running from June onward on coils that have been collecting dust for months, at exactly the time you need full capacity. A mid-season clean restores efficiency when the system is working hardest."),
    ("What should a proper AC service include?",
     "Filter cleaning or replacement, evaporator and condenser coil cleaning, a proper condenser wash, drain line clearing, refrigerant pressure verification, electrical inspection of capacitors, contactors and terminals, and a measured performance check of temperature split and airflow. If someone is in and out in fifteen minutes having wiped the filter, that was not a service."),
    ("Does regular servicing actually lower the electricity bill?",
     "Usually yes, and sometimes substantially. Dirty coils and clogged filters force the compressor to run longer to reach the same room temperature, and run time is what you pay for. The worse the neglect, the larger the improvement when it is put right. On a badly fouled system the difference is obvious within a day."),
    ("How long does a service take?",
     "A general service on a single split AC is typically forty-five to ninety minutes. A deep clean with foam treatment and jet washing takes longer, usually ninety minutes to two hours per unit, because the coil is treated and flushed rather than wiped. Cassette and ducted systems take longer again."),
    ("Can servicing be done without removing the unit from the wall?",
     "Yes. The great majority of servicing, including deep foam cleaning, is done in place with covers and drainage protecting your wall and floor. Full dismantling is only needed in specific cases, such as severe contamination or when a component behind the unit needs access, and we would explain why before doing it."),
    ("Do I still need servicing if the AC seems fine?",
     "That is exactly when it is worth doing. Servicing is preventive: it keeps a working system working and catches small problems while they are cheap. Waiting until performance drops means the coils have already been costing you money in extra run time for months, and possibly stressing the compressor."),
    ("Is an AMC better value than booking services individually?",
     "Once you have several units, or when a breakdown has real consequences, generally yes. The value is only partly the maintenance itself; it is also that scheduling becomes somebody else's job and that you get priority when everyone else is waiting a week in July. For a single lightly used unit, booking twice a year is perfectly sensible."),
]

INTRO = """<p>The honest answer for Delhi NCR is <strong>every three to six months</strong>, and that is not
an upsell. It is a reflection of what the air here does to a heat exchanger.</p>

<p>Manufacturer guidance is usually written for milder, cleaner conditions. Delhi supplies construction
dust much of the year, high particulate pollution through winter, and a cooling season that runs from
March to October. Filters and coils load up here considerably faster than the generic advice assumes.</p>

<div class="takeaway">
  <h4>Quick guidance by usage</h4>
  <ul>
    <li><strong>Typical home, summer use:</strong> twice a year, before and mid-season.</li>
    <li><strong>Near construction, a main road, or with pets:</strong> every three months.</li>
    <li><strong>Offices, showrooms, clinics:</strong> quarterly minimum.</li>
    <li><strong>Restaurant kitchens:</strong> more often; grease-laden air fouls coils fast.</li>
    <li><strong>Server rooms and critical cooling:</strong> scheduled preventive maintenance, documented.</li>
  </ul>
</div>"""

BODY = INTRO + """
<h2>Why an air conditioner is really a heat exchanger</h2>

<p>It helps to think about what the machine actually does. An air conditioner does not create cold; it
moves heat from inside your room to the outside air. Both ends of that transfer happen across metal
coils with fins, and both depend entirely on air being able to flow freely across clean surfaces.</p>

<p>Put a layer of dust on those fins and you have insulated the very surface whose whole purpose is to
transfer heat. The system compensates by running longer, which is the point at which the problem starts
appearing on your electricity bill rather than as an obvious fault.</p>

<h2>Residential use</h2>

<p>For a typical Delhi home running the AC through summer, two services a year works: a thorough one
before the season starts, and another midway through the heavy-use months. The pre-season service
matters because it is when parts can be sourced without the peak-season wait; the mid-season one matters
because that is when the coils have loaded up and the system is under most strain.</p>

<p>Move to quarterly if you are near a construction site or a main road, if you keep pets, or if the
unit runs most of the day. Any of those roughly doubles the rate at which filters clog.</p>

<h2>Commercial use</h2>

<p>Offices, restaurants, showrooms and clinics should be on a quarterly schedule as a minimum. The usage
pattern is different: long continuous run times, higher occupancy, doors opening constantly, and often
heat-generating equipment in the same space.</p>

<p>Kitchens deserve a specific mention. Grease-laden air coats coils in a way plain dust does not, and it
is considerably harder to remove once it has baked on. Restaurants that stretch servicing intervals
generally end up paying for coil replacement rather than coil cleaning.</p>

<h2>Critical environments</h2>

<p>Server rooms, laboratories, operating theatres and jewellery showrooms are a different category
altogether. Here the objective is not comfort but continuity, and the strategy is not fast repair but
never failing in the first place. That means scheduled preventive maintenance with documented checks,
which is precisely what our AMC programme was built around and why institutional clients have stayed
with it for decades.</p>

<h2>What "serviced" should actually mean</h2>

<p>There is a wide gap between a genuine service and a quick wipe, and from the customer's side the two
can look similar. A proper service covers:</p>

<ul>
  <li>Filter cleaning, or replacement where the mesh has degraded.</li>
  <li>Evaporator coil cleaning, with foam treatment where the fouling warrants it.</li>
  <li>A proper condenser wash. This is the highest-impact single step on most systems.</li>
  <li>Drain line clearing and a check that the fall is correct, before the monsoon rather than after.</li>
  <li>Refrigerant pressure verification, recorded so a slow leak shows up as a trend.</li>
  <li>Electrical inspection: capacitors, contactors, terminal tightness and current draw.</li>
  <li>A measured performance check of temperature split and airflow, before and after.</li>
</ul>

<div class="callout">
  <p><strong>A useful question to ask:</strong> "what was the temperature split before and after?" A
  service that improved anything will have moved that number, and an engineer doing the job properly
  will have measured it.</p>
</div>

<h2>Signs you have left it too long</h2>

<ul>
  <li>The unit runs noticeably longer to reach the same temperature.</li>
  <li>The electricity bill has crept up without a change in how you use the AC.</li>
  <li>A musty smell when it starts up, which is microbial growth on the coil.</li>
  <li>Water dripping indoors, which is a blocked drain line.</li>
  <li>Rattles, hums or grinding that were not there before.</li>
  <li>The system switching on and off every few minutes.</li>
</ul>

<h2>What regular servicing is really buying</h2>

<p>Three things, in order of how much they matter financially.</p>

<p><strong>Avoided breakdowns.</strong> The overwhelming majority of emergency calls we attend trace back
to something a routine service would have caught early and cheaply. A blocked drain is trivial to clear
and expensive to ignore once it has damaged a ceiling.</p>

<p><strong>Compressor life.</strong> Compressors fail from sustained stress: running hot, running long,
running against restricted airflow. Removing that stress is the single most effective thing you can do
to extend the life of the most expensive component in the system.</p>

<p><strong>Lower running cost.</strong> Restoring proper heat transfer directly reduces run time, every
day, for the rest of the season.</p>

<div class="takeaway">
  <h4>The practical rule</h4>
  <ul>
    <li>Two services a year is the floor for a Delhi home that uses AC through summer.</li>
    <li>Quarterly if usage is heavy, the environment is dusty, or a failure would cost you.</li>
    <li>The best time is before summer. The second best time is now: a neglected unit does not improve by waiting.</li>
  </ul>
</div>
"""

RELATED = [
    ("../ac-servicing.html", "AC Servicing",
     "What a proper service covers: deep cleaning, coil washing, gas checks and a measured report."),
    ("../ac-amc.html", "AC AMC",
     "Put servicing on a schedule with priority response and documented visits."),
    ("ac-not-cooling.html", "AC Not Cooling?",
     "Twelve reasons an AC stops cooling, most of which servicing prevents."),
    ("ac-amc-worth-it.html", "Is an AMC Worth It?",
     "A straight cost-benefit look, including when the honest answer is no."),
    ("../ac-repair.html", "AC Repair",
     "When something has already failed: diagnosis and repair with 2-hour response."),
    ("../ac-service-delhi.html", "AC Service in Delhi",
     "Zone-by-zone coverage across every part of Delhi."),
]


def build():
    return render_article(
        slug="how-often-ac-service.html",
        title="How Often Should You Service Your AC? Expert Guide",
        desc="How often an AC needs servicing in Delhi NCR, by usage: homes, offices, kitchens and critical cooling. What a real service covers. Call +91 93122 64832.",
        h1="How Often Should You Service Your AC?",
        lede="Every three to six months in Delhi NCR, and the reason is not sales pressure. It is what construction dust and this cooling season do to a heat exchanger.",
        body=BODY, faqs=FAQS, related_cards=RELATED,
        category="Maintenance", read_minutes=7)
