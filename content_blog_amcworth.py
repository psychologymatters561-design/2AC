#!/usr/bin/env python3
"""Article: is an AC AMC worth it."""
from build_blog import render_article

FAQS = [
    ("Is an AC AMC actually worth the money?",
     "For a single lightly used bedroom unit, honestly no. Book a service twice a year and you are fine. It becomes worth it once you have several units, or when a failure carries real consequences: a showroom that empties when it gets warm, a clinic with air quality obligations, a restaurant mid-service, a server room. The value is only partly the maintenance; it is also priority access in July."),
    ("What does an AC AMC actually cover?",
     "Scheduled preventive visits, filter cleaning and replacement, coil and condenser cleaning, drain line clearing, refrigerant pressure checks, electrical inspection, performance optimisation, emergency breakdown cover, priority response and a written report after each visit. Exactly which apply, and how often, depends on the plan and what the site needs."),
    ("How many visits should an AMC include?",
     "Our Essential plan covers two scheduled visits a year, timed before and during the cooling season. Professional covers four, effectively quarterly, plus breakdown cover. Enterprise is built around the site rather than a fixed count, with unlimited scheduled visits, two-hour priority response and named engineers. Most offices and showrooms land on Professional."),
    ("Does an AMC cover parts and gas?",
     "Cover varies by plan, and it should be stated explicitly in the contract rather than left vague. Consumables and routine items are normally included; major components such as compressors and control boards depend on the plan level and the age of the equipment. Have that conversation at the survey, not during a breakdown."),
    ("Can I put an AMC on old air conditioners?",
     "Usually yes. We survey first and give an honest assessment of each unit. If a particular system is genuinely at the end of its life, we will say so rather than sell a contract to maintain something that should be replaced. It is better to hear that at the survey than a month into the contract."),
    ("What happens if something breaks between scheduled visits?",
     "You call and we come. That is the point of the contract. AMC clients get priority scheduling ahead of ad-hoc callers, and Enterprise contracts carry a two-hour response commitment. In peak summer this is the difference clients tell us they value most, because availability matters more than price at 45 degrees."),
    ("Is an AMC worth it for just one or two ACs?",
     "Often not, and we will say so. Two units in a normal home are straightforward to manage yourself with a service booked twice a year. The calculation changes at around three or four units, or sooner if the ACs are in a business where warm rooms cost you customers or staff productivity."),
    ("How is an AMC different from just booking services?",
     "Three things: the scheduling becomes our responsibility rather than yours, you get priority when demand peaks, and you get a documented history of every unit. That last one matters more than people expect, both for warranty claims and for knowing which units are ageing and should be budgeted for replacement."),
]

INTRO = """<p>We sell annual maintenance contracts, so treat what follows with appropriate scepticism. To
earn that, we will start with the case against.</p>

<p><strong>If you have one air conditioner in a bedroom you use for a few months a year, an AMC is not
worth it.</strong> Book a service before summer and another midway through, and you have covered
essentially everything a contract would do for you, without the contract.</p>

<p>That is genuinely our advice, and we give it regularly. The interesting question is where the line
sits, and what changes on the other side of it.</p>

<div class="takeaway">
  <h4>Where the line usually falls</h4>
  <ul>
    <li><strong>1 to 2 units, light home use:</strong> book services individually.</li>
    <li><strong>3+ units, or heavy daily use:</strong> a contract starts making sense.</li>
    <li><strong>Any business where warm rooms cost money:</strong> almost always worth it.</li>
    <li><strong>Critical cooling</strong> (server room, clinic, jewellery retail): not really optional.</li>
  </ul>
</div>"""

BODY = INTRO + """
<h2>The four things you are actually buying</h2>

<p>People assume an AMC is a discount on servicing. It is not, mainly. It is four distinct things, and
their relative value depends entirely on your situation.</p>

<h3>1. Somebody else remembers</h3>
<p>This sounds trivial and is not. Maintenance that depends on a busy person noticing it is due tends to
happen late or not at all. Once you have several units, tracking which was last serviced and when becomes
a genuine administrative chore, and the failure mode is silent: nothing breaks, the coils just quietly
get dirtier and the bills quietly climb.</p>

<h3>2. Priority when it matters</h3>
<p>This is the one clients mention most, and it is invisible until you need it. In May and June every AC
company in Delhi NCR is at capacity. Response times across the whole industry stretch to days. A contract
puts you ahead of ad-hoc callers, and on our Enterprise plan carries a two-hour commitment.</p>

<p>If your AC failing means a warm bedroom for a night, that is an inconvenience. If it means a showroom
full of customers who leave, a restaurant that cannot serve, or a server room climbing through its
temperature limits, the wait is the whole cost.</p>

<h3>3. Cost predictability</h3>
<p>Emergency repairs at peak season are the most expensive way to buy air conditioning. You are choosing
under time pressure, from whoever is available, at whatever they quote. A contract converts an unknown
into a budgeted annual figure agreed in advance, in writing.</p>

<h3>4. A documented history</h3>
<p>Every visit produces a report: what was checked, what was found, what was done. That matters in three
practical ways. Manufacturers frequently require evidence of maintenance for warranty claims. Compliance
audits in healthcare and hospitality go considerably better with records. And knowing which units are
ageing lets you plan replacement rather than being surprised by it.</p>

<h2>Working the numbers honestly</h2>

<p>We do not publish prices, because a figure quoted without seeing the site is either padded or
misleading. But you can do the arithmetic yourself, and we would encourage it.</p>

<p>Take what you actually spent on air conditioning last year. Include every service call, every repair,
every gas top-up, and be honest about the emergency call-outs at peak rates. Then add the costs that do
not appear on an invoice:</p>

<ul>
  <li>Extra electricity from running dirty coils for months.</li>
  <li>Shortened compressor life, amortised across the replacement you will eventually make.</li>
  <li>Business lost during downtime, if you run a customer-facing space.</li>
  <li>Your own time spent arranging it all.</li>
</ul>

<p>Compare that total with an AMC quote for your site. For single-unit homes the arithmetic usually
favours booking individually. From about three units upward, and for essentially any commercial site, it
tends to go the other way, and the gap widens the worse your breakdown year was.</p>

<div class="callout">
  <p><strong>A pattern we see often:</strong> clients who move to a contract after a bad summer almost
  always spend less overall the following year. Not because the contract is cheap, but because the
  expensive events stop happening.</p>
</div>

<h2>Reactive versus planned, side by side</h2>

<div class="tbl-wrap">
<table class="cmp">
  <thead><tr><th>Consideration</th><th>Pay per breakdown</th><th>With an AMC</th></tr></thead>
  <tbody>
    <tr><td>When work happens</td><td>After something has failed</td><td>Before failure, on a schedule</td></tr>
    <tr><td>Peak-summer availability</td><td>Join the queue, often days</td><td>Priority; 2-hour on Enterprise</td></tr>
    <tr><td>Cost predictability</td><td>Unknown until it breaks</td><td>Budgeted annual figure</td></tr>
    <tr><td>Negotiating position</td><td>While the room heats up</td><td>Agreed in advance, in writing</td></tr>
    <tr><td>Parts quality</td><td>Whatever is on the van</td><td>Genuine parts, proper channels</td></tr>
    <tr><td>Equipment lifespan</td><td>Shortened by running stressed</td><td>Extended by consistent care</td></tr>
    <tr><td>Running cost</td><td>Creeps up as coils foul</td><td>Held near design efficiency</td></tr>
    <tr><td>Records</td><td>Scattered invoices, if any</td><td>Documented every visit</td></tr>
    <tr><td>Warranty claims</td><td>Often refused, no evidence</td><td>Maintenance history on file</td></tr>
    <tr><td>Accountability</td><td>A different technician each time</td><td>One company, across the year</td></tr>
  </tbody>
</table></div>

<h2>When an AMC is the wrong purchase</h2>

<p>We would rather lose a contract than sell one that does not make sense, so here is when to decline:</p>

<ul>
  <li><strong>One or two units, light seasonal use.</strong> Book services individually.</li>
  <li><strong>Equipment genuinely at end of life.</strong> Maintaining a fifteen-year-old R22 system with
  a failing compressor is spending good money after bad. Replace, then cover the new equipment.</li>
  <li><strong>A contract with vague terms.</strong> If what is included is not written plainly, including
  how major components are handled, that ambiguity will surface at the worst moment.</li>
  <li><strong>You are moving out within the year.</strong> Obvious, but worth saying.</li>
</ul>

<div class="warn">
  <p><strong>What to check before signing anything:</strong> visit count and timing, exactly what is
  covered on parts, the response commitment in writing, whether you get a written report each visit, and
  what happens at renewal. Vague answers now become disputes in July.</p>
</div>

<h2>What our own track record looks like</h2>

<p>Our AMC clients stay, on average, more than fifteen years. In a trade where most relationships last a
single season, that retention is the number we are proudest of, and it is the only evidence we would ask
you to weigh: people who could leave every twelve months, choosing not to, repeatedly.</p>

<p>Fifteen-plus embassies and consulates, alongside hospitals, hotels and Fortune 500 offices, sit in that
group. These are clients who audit their vendors annually, which is a more demanding test than any
marketing claim.</p>
"""

RELATED = [
    ("../ac-amc.html", "AC AMC Plans",
     "What is included at each level, how the programme works, and how to request a quote."),
    ("how-often-ac-service.html", "How Often to Service?",
     "If a contract is not right for you, this is the schedule to follow instead."),
    ("../ac-servicing.html", "AC Servicing",
     "One-off servicing, booked when you need it."),
    ("ac-not-cooling.html", "AC Not Cooling?",
     "Most breakdowns start as something a scheduled visit would have caught."),
    ("../why-us.html", "Why Air Control",
     "The engineering standards and safety record behind the contract."),
    ("../ac-service-delhi.html", "AC Service in Delhi",
     "Zone-by-zone coverage across every part of Delhi."),
]


def build():
    return render_article(
        slug="ac-amc-worth-it.html",
        title="Is an AC AMC Worth It? An Honest Cost-Benefit Look",
        desc="When an AC maintenance contract pays for itself and when it does not, from a company that sells them. Includes when we tell clients to decline.",
        h1="Is an AC AMC Worth It? An Honest Cost-Benefit Analysis",
        lede="We sell these contracts, so start sceptical. Here is the case against, the point where the arithmetic flips, and the situations where we tell people not to bother.",
        body=BODY, faqs=FAQS, related_cards=RELATED,
        category="Cost Guides", read_minutes=8)
