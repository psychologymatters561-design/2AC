#!/usr/bin/env python3
"""Article: choosing an AC for an Indian home."""
from build_blog import render_article

FAQS = [
    ("Which AC is best for a 150 sq ft bedroom?",
     "A 1.5 ton unit is usually right for a typical 150 sq ft Delhi bedroom, though 1 ton can suffice for a shaded, north-facing room on a lower floor. The variables that actually decide it are direct sunlight, top-floor exposure, window area, ceiling height and how many people use the room. A west-facing top-floor room genuinely needs more capacity than the same floor area on the ground floor."),
    ("Is an inverter AC worth the extra cost?",
     "For anything you run more than a few hours a day, yes. An inverter modulates compressor speed to match demand instead of switching fully on and off, which means lower running cost, steadier room temperature and less noise. For a guest room used a dozen nights a year, the lower purchase price of a non-inverter is not offset by running hours, and the simpler unit is the sensible buy."),
    ("Does a 5-star rating pay for itself?",
     "In a room used daily through a Delhi summer, a 5-star inverter unit typically repays its premium within two to three seasons. In a lightly used room it will not. Star ratings are measured under standard test conditions, so your real saving depends on your usage, but the relative ranking between units still holds."),
    ("Which AC brand is most reliable?",
     "We service every major brand and the honest answer is that reliability varies more by model line and by installation quality than by badge. Daikin, Blue Star, Hitachi, Voltas, LG, Samsung, Carrier and O General all make units we see running well for a decade, and all make budget lines we see fail early. What separates a ten-year unit from a four-year one is far more often how it was installed and maintained."),
    ("Copper or aluminium condenser coils?",
     "Copper, if the choice is available. It is more repairable and generally more durable, which matters in Delhi's corrosive urban air. A pinhole in a copper coil can often be repaired; an aluminium coil more often means replacement. Over a ten-year life that repairability is worth real money."),
    ("Should I buy a bigger AC to cool faster?",
     "No, and this is a common and expensive mistake. An oversized unit cools the air quickly, hits the thermostat and switches off before it has removed much moisture, leaving a room that feels cold and clammy. It also short-cycles, and frequent starts are exactly what wears a compressor. Correct sizing beats generous sizing."),
    ("Is it better to buy in the off-season?",
     "Generally yes, for two reasons. Prices are usually keener outside the March-to-June rush, and more importantly you get installers who are not working through a backlog. An installation done unhurried in November is more likely to include the pressure testing and proper evacuation that a team doing four jobs a day may rush."),
    ("Does installation quality really matter that much?",
     "It matters more than the brand. We regularly see excellent units performing poorly because of inadequate vacuum evacuation, an incorrect charge, unsupported pipework or a condenser sited where it cannot breathe. If your budget is tight, buy a simpler unit and have it installed properly rather than the reverse."),
]

INTRO = """<p>Most buying guides start with brands. We would start somewhere else, because after
thirty-eight years of installing and repairing air conditioners across Delhi NCR, the pattern is
consistent: <strong>how a unit is sized and installed predicts its life far better than whose name is
on it</strong>.</p>

<p>That is not a claim that brands are identical. It is that the difference between a good unit and a
very good unit is small compared with the difference between a careful installation and a rushed one.</p>

<div class="takeaway">
  <h4>The short version</h4>
  <ul>
    <li><strong>Size on the room,</strong> not on floor area alone. Orientation and floor level matter.</li>
    <li><strong>Inverter</strong> for daily use; non-inverter is fine for occasional rooms.</li>
    <li><strong>5-star</strong> pays back in heavily used rooms, not in guest bedrooms.</li>
    <li><strong>Copper coils</strong> where you have the choice, for repairability.</li>
    <li><strong>Never economise on installation.</strong> It is what determines whether you get ten years.</li>
  </ul>
</div>"""

BODY = INTRO + """
<h2>Start with tonnage, but size on the room</h2>

<p>Tonnage is the cooling capacity. As a rough starting point in Delhi:</p>

<ul>
  <li><strong>Up to 120 sq ft:</strong> 1 ton</li>
  <li><strong>120 to 180 sq ft:</strong> 1.5 ton</li>
  <li><strong>180 to 250 sq ft:</strong> 2 ton</li>
</ul>

<p>Then adjust upward for any of the following, because each adds real heat load that floor area does
not capture:</p>

<ul>
  <li>A west or south-facing room, which takes direct afternoon sun.</li>
  <li>Top floor, where the roof radiates heat downward all evening.</li>
  <li>Large windows or a glazed wall.</li>
  <li>Ceilings above the standard height, since you are cooling more volume.</li>
  <li>More than two regular occupants.</li>
  <li>Heat-generating equipment: computers, kitchen appliances, heavy lighting.</li>
</ul>

<p>A top-floor west-facing room can genuinely need a full tonnage step above what its floor area
suggests. Equally, a shaded north-facing room on the ground floor may be comfortable a step below.</p>

<div class="warn">
  <p><strong>Do not oversize deliberately.</strong> A unit that is too large cools the air fast, reaches
  the thermostat and shuts off before removing much humidity. The result is a room that feels cold and
  damp rather than comfortable, plus short-cycling that wears the compressor.</p>
</div>

<h2>Inverter or non-inverter</h2>

<p>A non-inverter compressor runs at one speed: full. It cools until the thermostat is satisfied, stops,
and starts again when the room warms. An inverter compressor varies its speed continuously, running
gently to hold the temperature once the room is down.</p>

<p>That difference produces three practical benefits for daily use: lower running cost, because most of
the time the compressor is not working at full output; steadier temperature, without the swing between
cycles; and less noise, both from the outdoor unit and from the absence of repeated starts.</p>

<p>The case for non-inverter is narrower but real. In a guest room used occasionally, the purchase price
difference is not recovered because there are not enough running hours to recover it through.</p>

<h2>Star ratings and what they mean in practice</h2>

<p>The BEE star rating measures efficiency under standard test conditions. Higher stars mean less
electricity for the same cooling. The subtlety is that the test conditions are not your room, so treat
the rating as a reliable way to rank units against each other rather than a promise of a specific bill.</p>

<p>In Delhi's long cooling season, a 5-star inverter unit in a room used daily typically repays its
premium within two to three summers. In a room used a dozen nights a year, it will not, and the money is
better spent on the installation.</p>

<h2>What actually varies between brands</h2>

<p>We service Daikin, Blue Star, Voltas, LG, Samsung, Hitachi, Carrier, O General, Mitsubishi, Panasonic,
Godrej, Lloyd, Whirlpool, Haier, Toshiba and Sanyo. Across all of them, the things worth comparing are:</p>

<ul>
  <li><strong>Spare parts availability.</strong> A compressor or board you can source in two days beats
  one you wait three weeks for, especially in June.</li>
  <li><strong>Service network in your area.</strong> Coverage varies considerably outside central Delhi.</li>
  <li><strong>Warranty terms on the compressor,</strong> which is the expensive component.</li>
  <li><strong>Noise ratings,</strong> which matter more than people expect in a bedroom.</li>
  <li><strong>Coil material,</strong> for the repairability reason above.</li>
</ul>

<div class="callout">
  <p><strong>What we would tell a friend:</strong> pick two or three units in your budget that are the
  right tonnage, then choose between them on parts availability and local service rather than on the
  feature list. Wi-Fi control is pleasant. A compressor you can get hold of in peak summer is worth more.</p>
</div>

<h2>The features worth paying for, and the ones that are not</h2>

<p><strong>Worth it:</strong> a genuinely good filter if anyone in the house has respiratory sensitivity;
a wide voltage operating range if your supply fluctuates, which in parts of NCR it does; and a quiet
outdoor unit if it sits near a bedroom window or a neighbour's.</p>

<p><strong>Usually not:</strong> elaborate air-purification claims layered onto a basic filter; and
"turbo" modes, which mostly run the fan faster rather than adding cooling capacity.</p>

<h2>Why installation decides the outcome</h2>

<p>It is entirely possible to buy an excellent air conditioner and take years off its life in a two-hour
installation. The steps that get skipped are invisible once the panels are on:</p>

<ul>
  <li><strong>Vacuum evacuation.</strong> Air and moisture left in the circuit form acids that corrode
  the compressor from within. This is the most commonly skipped step in cheap installations.</li>
  <li><strong>Charging by weight</strong> to the manufacturer figure, adjusted for actual pipe run,
  rather than until the gauge looks about right.</li>
  <li><strong>Continuous insulation</strong> on the suction line, including at joints and wall penetrations.</li>
  <li><strong>Drainage with real fall,</strong> tested with water. Most "AC leaking water" calls a year
  later are drainage never set correctly on day one.</li>
  <li><strong>Condenser siting</strong> with clearance on every side, and somewhere it can be serviced
  safely later.</li>
</ul>

<h2>A sensible buying sequence</h2>

<ol>
  <li>Measure the room and note orientation, floor level, window area and typical occupancy.</li>
  <li>Work out tonnage from that, not from floor area alone.</li>
  <li>Decide inverter or not, based honestly on daily running hours.</li>
  <li>Set the star rating from the same usage figure.</li>
  <li>Shortlist units in budget, then choose on parts availability and local service.</li>
  <li>Budget properly for installation, including copper, drainage and electrical work.</li>
  <li>Buy off-season if you can, for keener prices and unhurried installers.</li>
</ol>
"""

RELATED = [
    ("../ac-installation.html", "AC Installation",
     "Load calculation, brazed pipework, full evacuation and charge by weight, verified before handover."),
    ("how-often-ac-service.html", "How Often to Service?",
     "Keeping a new unit performing at the level it was commissioned to."),
    ("../ac-amc.html", "AC AMC",
     "Protect a new installation with scheduled maintenance from day one."),
    ("ac-not-cooling.html", "AC Not Cooling?",
     "What goes wrong, and how much of it traces back to sizing and installation."),
    ("../ac-repair.html", "AC Repair",
     "We repair every brand listed here, across split, cassette, ducted and VRF."),
    ("../ac-service-gurgaon.html", "AC Service Gurgaon",
     "DLF, Golf Course Road, Cyber City and all sectors."),
]


def build():
    return render_article(
        slug="best-ac-for-home.html",
        title="Best AC for Home in India: Expert Buying Guide",
        desc="How to choose an AC for an Indian home: sizing by room not floor area, inverter vs non-inverter, star ratings, coils and why installation decides the outcome.",
        h1="Best AC for Your Home: An Engineer's Buying Guide",
        lede="After thirty-eight years of installing and repairing these machines, the pattern is consistent: sizing and installation predict an AC's life far better than the brand on the box.",
        body=BODY, faqs=FAQS, related_cards=RELATED,
        category="Buying Guides", read_minutes=9)
