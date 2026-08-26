#!/usr/bin/env python3
"""Article: AC gas filling in Delhi NCR."""
from build_blog import render_article

FAQS = [
    ("How much does AC gas filling cost in Delhi?",
     "It depends on the refrigerant type, the capacity of the system and, above all, whether there is a leak to repair first. R32 and R410A are priced differently to the older R22, and a 1 ton split takes a fraction of what a cassette or VRF system needs. We quote after diagnosis rather than over the phone, because a figure quoted blind either has to assume the worst case or hide the leak repair that actually matters."),
    ("How often does an AC need gas refilling?",
     "In principle, never. Refrigerant circulates in a sealed loop and is not consumed the way fuel is. A properly installed system can run a decade without losing charge. If you are topping up every year or two, you do not have a gas consumption problem, you have a leak nobody has found."),
    ("What are the signs my AC needs gas?",
     "Reduced cooling with the unit running constantly, ice forming on the copper pipework or the indoor coil, a hissing or bubbling sound, and a temperature split across the indoor coil well below the normal range. None of these is conclusive on its own, which is why pressures should be measured rather than assumed."),
    ("Which gas does my AC use: R32, R410A or R22?",
     "Check the rating plate on the outdoor unit; it states the refrigerant and the correct charge weight. Most units sold in India in recent years use R32 or R410A. R22 is being phased out globally, which matters if you own an older system: it is increasingly scarce and expensive, and that changes the repair-or-replace calculation."),
    ("Can I mix refrigerants or use a substitute?",
     "No. Different refrigerants operate at different pressures and need different compressor oils. Mixing them, or substituting a cheaper drop-in, gives poor cooling at best and destroys the compressor at worst. It also makes future diagnosis much harder, because the pressures no longer mean what the gauges say they mean."),
    ("Is topping up without fixing the leak ever reasonable?",
     "Occasionally, as a stopgap: a wedding at the weekend, a system due for replacement next month. What is not reasonable is being sold it as a repair. If someone recharges your system without discussing where the refrigerant went, you will be paying for the same gas again, and the leak is quietly damaging the compressor in the meantime."),
    ("How long does gas filling take?",
     "Finding the leak is the part that takes time. The recharge itself is quick. A straightforward leak at an accessible joint might be repaired, evacuated and recharged in two to three hours. A leak inside a coil, or on a long concealed pipe run, can take considerably longer or need the component replaced."),
    ("Does gas filling improve cooling immediately?",
     "If low charge was genuinely the fault, yes, and noticeably. If cooling does not improve, the charge was not the problem and something else was missed, most often a fouled condenser, a failing compressor or restricted airflow. That is the point at which a second opinion is worth having."),
]

INTRO = """<p>Refrigerant, or "gas" as everyone in the trade calls it, is the most misunderstood part of
owning an air conditioner, and the area where customers in Delhi NCR are most often overcharged. The
misunderstanding is simple and costly: people assume refrigerant is a consumable, like petrol, that
runs down and needs topping up periodically.</p>

<p>It is not. Understanding that one fact changes how you judge every quote you are given.</p>

<div class="takeaway">
  <h4>What to take away</h4>
  <ul>
    <li><strong>Refrigerant is not consumed.</strong> It circulates in a sealed loop. If it is low, it leaked.</li>
    <li><strong>A top-up is not a repair.</strong> Without finding the leak, you pay again within months.</li>
    <li><strong>Charge is by weight,</strong> to the figure on the unit's rating plate, not "until it looks right".</li>
    <li><strong>Running low on charge damages the compressor,</strong> so delay costs more than the refill.</li>
  </ul>
</div>"""

BODY = INTRO + """
<h2>Why "annual gas filling" is a warning sign</h2>

<p>A sealed refrigeration circuit should hold its charge for the life of the equipment. Domestic
refrigerators run for fifteen years on their original charge and nobody tops those up. An air
conditioner is the same closed system, with the added complication of joints made on site during
installation.</p>

<p>So when a technician tells you an AC needs gas every year as routine maintenance, one of two things
is true. Either the system has a leak that has never been found, or you are being sold something you
do not need. Both are worth pushing back on.</p>

<h2>Where the refrigerant actually goes</h2>

<p>Every low charge has an escape route. In our experience across Delhi NCR these are the common ones:</p>

<ul>
  <li><strong>Poorly made joints at installation.</strong> A flare not seated correctly or a braze with
  a pinhole loses charge slowly for months before anyone notices.</li>
  <li><strong>Vibration cracks.</strong> Copper work-hardens. Pipework that is inadequately clipped
  flexes with every compressor start until it splits, usually near the outdoor unit.</li>
  <li><strong>Corrosion in the coils.</strong> Urban air is corrosive, and coastal or industrial
  atmospheres more so. Pinholes develop in aluminium fins and copper tube over years.</li>
  <li><strong>Damage during shifting.</strong> Moving an AC is where a great many leaks are created:
  pipes bent past their radius, joints reused that should have been remade.</li>
  <li><strong>Schrader valve seepage.</strong> The service ports themselves can weep slowly, which is
  cheap to fix once identified.</li>
</ul>

<h2>What determines the cost</h2>

<p>We do not publish fixed prices, for the same reason we do not quote repairs before diagnosis: a
number given blind is either padded to cover the worst case or quietly excludes the part that matters.
What we can do is set out honestly what moves the figure.</p>

<h3>The refrigerant type</h3>
<p>R32, R410A and R22 are priced differently, and availability differs too. R22 in particular is being
phased out under international agreement, so it is scarce and getting scarcer. If you own an R22 system
facing a significant leak, that scarcity is a genuine factor in whether repair still makes sense.</p>

<h3>System capacity</h3>
<p>A 1 ton split unit holds a modest charge. A 2 ton unit holds more. Cassette, ducted and VRF systems
hold considerably more again, and VRF charge calculation has to account for the actual pipe run length.
Capacity is the largest single driver of the refrigerant portion of any quote.</p>

<h3>Whether there is a leak to repair</h3>
<p>This is usually the bigger part of the job. An accessible joint is straightforward. A leak inside an
evaporator coil, or on a concealed run behind finished walls, is a different piece of work entirely and
may mean replacing a component rather than repairing a joint.</p>

<h3>Access and system type</h3>
<p>A wall-mounted split at ground level is quick. A condenser on a roof, in a tight service shaft, or
behind a ceiling in a working office all add time, and sometimes require the work to be scheduled
outside business hours.</p>

<div class="callout">
  <p><strong>What a fair quote looks like:</strong> it separates leak detection, leak repair, evacuation
  and refrigerant, and it states the charge weight being put in. A single lump sum labelled "gas filling"
  tells you nothing about whether the underlying fault is being addressed at all.</p>
</div>

<h2>How the job should be done</h2>

<p>Recharging correctly is a sequence, and skipping steps is what turns a repair into a repeat visit.</p>

<ol>
  <li><strong>Confirm the charge is genuinely low</strong> by measuring pressures and the temperature
  split, not by assuming from the symptom.</li>
  <li><strong>Find the leak</strong> using an electronic detector, and where necessary nitrogen pressure
  testing to hold the system and locate slow losses.</li>
  <li><strong>Recover the remaining refrigerant</strong> properly rather than venting it. It is a
  greenhouse gas, and venting is both unlawful in many jurisdictions and simply poor practice.</li>
  <li><strong>Repair the leak</strong> by remaking the joint or replacing the failed component.</li>
  <li><strong>Pressure-test with nitrogen</strong> and hold, to prove the repair before going further.</li>
  <li><strong>Evacuate to a deep vacuum</strong> and hold it, to pull out air and moisture. Skipping
  this is the step that quietly destroys compressors, because moisture in the circuit forms acids.</li>
  <li><strong>Charge by weight</strong> to the manufacturer's figure, adjusted for actual pipe length.</li>
  <li><strong>Verify performance</strong> by re-measuring pressures and temperature split, and record
  the readings.</li>
</ol>

<div class="warn">
  <p><strong>The step most often skipped:</strong> vacuum evacuation. It takes time and no customer can
  see whether it was done. It is also the single biggest determinant of whether the compressor is still
  running in five years.</p>
</div>

<h2>Protecting yourself from being overcharged</h2>

<ul>
  <li>Ask where the refrigerant went. A technician who cannot answer has not looked.</li>
  <li>Ask for the charge weight going in, and compare it with the rating plate on the outdoor unit.</li>
  <li>Be wary of "your gas is low" offered without gauges having been connected.</li>
  <li>Ask whether the system was evacuated before charging, and for how long.</li>
  <li>Get the readings written down. Documented before-and-after figures are hard to fake and easy to
  check against next time.</li>
</ul>

<h2>When replacement makes more sense</h2>

<p>Sometimes the honest answer is not to repair. An R22 system over twelve years old, with a leak inside
the evaporator coil, is a case where the cost of a coil plus increasingly scarce refrigerant approaches
the cost of a new, far more efficient unit that will also cost less to run. We would rather tell you that
than take the repair.</p>
"""

RELATED = [
    ("ac-not-cooling.html", "AC Not Cooling?",
     "Twelve reasons an AC stops cooling, and how each one is actually diagnosed."),
    ("../ac-repair.html", "AC Repair",
     "Leak detection, proper repair and recharge by weight, with 2-hour emergency response."),
    ("../ac-servicing.html", "AC Servicing",
     "Regular servicing catches slow leaks as a trend, before they become breakdowns."),
    ("how-often-ac-service.html", "How Often to Service?",
     "Servicing frequency for Delhi conditions, by usage pattern and environment."),
    ("../ac-amc.html", "AC AMC",
     "Pressures recorded at every visit, so a slow leak shows up early."),
    ("../ac-service-delhi.html", "AC Service in Delhi",
     "Zone-by-zone coverage across every part of Delhi."),
]


def build():
    return render_article(
        slug="ac-gas-filling-cost-delhi.html",
        title="AC Gas Filling in Delhi NCR: The Complete Guide",
        desc="What AC gas filling really involves, what drives the cost, and why a top-up without finding the leak is money wasted. Call +91 93122 64832.",
        h1="AC Gas Filling in Delhi NCR: What It Costs and What You Should Ask",
        lede="Refrigerant is not a consumable. Understanding that one fact is the difference between a repair that lasts and paying for the same gas every summer.",
        body=BODY, faqs=FAQS, related_cards=RELATED,
        category="Cost Guides", read_minutes=8)
