#!/usr/bin/env python3
"""Article: AC not cooling."""
from build_blog import render_article

FAQS = [
    ("Why is my AC running but not cooling?",
     "The unit is powered and the fan is moving air, but no heat is being removed. That points at the refrigerant circuit rather than the electrics: low refrigerant from a leak, an iced evaporator coil, a condenser coil too dirty to reject heat, or a compressor that starts but no longer builds pressure. A technician should measure suction and discharge pressures and the temperature split across the coil before recommending any part."),
    ("How do I know if my AC needs gas or something else?",
     "Refrigerant is sealed in a closed circuit and is not consumed, so if it is low, it leaked. Genuine signs of low charge are ice on the copper pipework, a hissing or bubbling sound, and a temperature split well under the normal range. If someone offers to top up the gas without first finding where the old gas went, get a second opinion. You will be paying for the same refrigerant again within months."),
    ("Can a dirty filter really stop an AC cooling?",
     "Yes, and it is the single most common cause we find. A clogged filter starves the evaporator of airflow. Less air across the coil means the coil gets colder than designed, moisture on it freezes, and the ice then blocks airflow completely. By the time most people call, the unit is producing almost no cold air at all and there is visible ice inside."),
    ("Why does my AC cool at night but not in the afternoon?",
     "That is a capacity problem rather than a fault. The system is close to its limit and copes while the outdoor temperature is lower, then falls behind in peak heat. Usual causes are a dirty condenser, a slightly low charge, or a unit undersized for a west-facing or top-floor room. It is worth diagnosing early, because a system running flat out for hours is the one that fails in May."),
    ("Is it safe to keep running an AC that is not cooling?",
     "If there is ice on the pipes or the indoor coil, switch to fan-only mode and let it thaw before running it again. Running a frozen system pulls liquid refrigerant back to the compressor, which is one of the fastest ways to destroy it. If you notice a burning or electrical smell, switch off at the breaker and call us rather than waiting."),
    ("How long should an AC take to cool a room?",
     "A correctly sized system should bring a normal room down noticeably within fifteen to twenty minutes and reach the set temperature within about half an hour, even on a hot Delhi afternoon. If yours runs for hours without reaching the thermostat setting, something is wrong: it is not simply that the weather is hot."),
    ("Does closing curtains actually help?",
     "Considerably, in Delhi. Direct sun through glass is one of the largest heat loads in a typical room, and a west-facing room in the afternoon can gain more heat through the window than from every other source combined. Blinds or curtains during peak sun reduce the load your AC has to fight, which shortens run times and lowers the bill."),
    ("My AC is old. Is it worth repairing?",
     "Our honest rule of thumb: under about eight years old, and a repair costing less than roughly a third of a new system is usually worth doing. Over twelve years old, running obsolete R-22 refrigerant, and facing compressor failure, replacement generally makes better financial sense. We will tell you plainly which side of that line you are on, including when the answer earns us less."),
]

INTRO = """<p>An air conditioner that runs but does not cool is the most common call we get, and in
thirty-eight years across Delhi NCR the cause is almost always one of a familiar handful. The
frustrating part for most people is that the unit <em>looks</em> fine: the light is on, the fan is
turning, air is coming out. Something invisible has gone wrong.</p>

<p>This guide walks through twelve real causes, in roughly the order we encounter them, with what
each one looks like from the outside and what actually fixes it. A few you can check yourself in
five minutes. The rest need instruments, because guessing at a refrigerant circuit is how people
end up paying for parts they never needed.</p>

<div class="takeaway">
  <h4>The short version</h4>
  <ul>
    <li><strong>Check first:</strong> thermostat mode and setting, air filter, outdoor unit clearance, tripped breaker.</li>
    <li><strong>Most common real faults:</strong> clogged filter, dirty condenser coil, refrigerant leak, frozen evaporator.</li>
    <li><strong>Stop running it</strong> if you see ice on the pipes, or smell burning.</li>
    <li><strong>Refrigerant is not consumed.</strong> If it is low, there is a leak, and topping up without repair is money wasted.</li>
  </ul>
</div>"""

BODY = INTRO + """
<h2>Start with the five-minute checks</h2>

<p>Before anyone books a service call, there are four things worth ruling out. We would rather you
found the problem yourself than paid a diagnostic fee to be told the mode was wrong.</p>

<ol>
  <li><strong>Mode and temperature.</strong> Remotes get knocked. If the unit is on fan or dry mode
  it will blow air and never cool. Set cool mode and a target several degrees below the room.</li>
  <li><strong>The air filter.</strong> Open the front panel and look. If the mesh is grey rather
  than translucent, that is very likely your answer.</li>
  <li><strong>The outdoor unit.</strong> It needs clear air on all sides. Boxes stacked against it,
  a shed built around it, or dense plant growth will all stop it rejecting heat.</li>
  <li><strong>The breaker.</strong> Some systems trip the outdoor unit while the indoor unit
  continues to run on its own supply, which produces exactly this symptom.</li>
</ol>

<h2>The twelve causes, and what each one looks like</h2>

<h3>1. A clogged air filter</h3>
<p>The most frequent cause by a wide margin, and the one most easily prevented. Delhi air carries
construction dust and seasonal pollution that load a filter far faster than most cities. Restricted
airflow means the evaporator coil runs colder than designed, condensation on it freezes, and the ice
then blocks airflow entirely. Cleaning the filter is a five-minute job; if the mesh has gone brittle
it should be replaced instead.</p>

<h3>2. A dirty condenser coil</h3>
<p>The outdoor unit's job is to dump your room's heat into the outside air. Coated in road dust and
grime, it cannot, so pressures climb and cooling capacity falls away. This is the single highest-impact
clean on most systems, and it is why a proper service washes the outdoor coil rather than just wiping
the indoor filter.</p>

<h3>3. Low refrigerant from a leak</h3>
<p>Refrigerant sits in a sealed circuit. It does not get used up, so a low charge always means a leak
somewhere: a poorly brazed joint, a corroded coil, a vibration crack. Signs are ice on the copper
pipework, a hiss or bubble from the indoor unit, and a temperature split well below normal. The correct
repair is to find the leak, fix it, pressure-test, and recharge by weight to the manufacturer figure.</p>

<div class="warn">
  <p><strong>Worth knowing:</strong> a top-up without leak repair is the most common way customers get
  overcharged in this trade. The gas goes back out the same hole, and you pay again next season.</p>
</div>

<h3>4. A frozen evaporator coil</h3>
<p>Ice on the indoor coil is a symptom, not a root cause. It follows either restricted airflow (dirty
filter, failing blower, closed vents) or low refrigerant. Switch to fan-only and let it thaw fully
before running again, because running a frozen system risks liquid refrigerant reaching the compressor.</p>

<h3>5. A failing compressor</h3>
<p>The compressor is the pump at the heart of the system. When it is worn it may start, hum and draw
current without building useful pressure, giving a unit that runs continuously and cools slightly or
not at all. This is the most expensive component, which is exactly why the cheap causes above should
be ruled out first, properly, with gauges.</p>

<h3>6. A capacitor that has failed</h3>
<p>Capacitors give the compressor and fan motors the kick they need to start. A failed one produces a
hum without a start, or a compressor that trips out repeatedly on overload. It is an inexpensive part
and a quick replacement, and it is worth checking before anyone declares the compressor dead.</p>

<h3>7. Thermostat or sensor fault</h3>
<p>The indoor sensor tells the system what the room temperature actually is. If it has drifted or come
loose from its holder, the unit may believe the room is already cool and cycle off early, leaving you
warm. Symptoms look like weak cooling but the fix is small.</p>

<h3>8. A failed fan motor</h3>
<p>Two motors matter: the indoor blower that moves air across the coil, and the outdoor fan that pulls
air through the condenser. If the outdoor fan stops, the system cuts out on high pressure within
minutes. If the indoor blower weakens, airflow drops and the coil ices.</p>

<h3>9. Control board or inverter fault</h3>
<p>Inverter boards are sensitive to voltage spikes and to moisture, both of which parts of Delhi NCR
supply generously. A board fault can produce almost any symptom, including a compressor that never
starts. Boards are expensive, so they should be properly tested rather than swapped on suspicion.</p>

<h3>10. Leaking or badly insulated ductwork</h3>
<p>On ducted and cassette systems, cooled air escaping into a ceiling void never reaches the room. You
pay to cool a space nobody occupies. Gaps in duct insulation produce the same loss, and both are
invisible from inside the room.</p>

<h3>11. The unit is undersized for the room</h3>
<p>A system that cools adequately in April and fails in June may never have been large enough. Delhi
adds load a chart does not capture: top-floor exposure, west-facing glazing, high ceilings, more
occupants than assumed, and equipment giving off heat. Sizing should be done from heat load, not floor
area alone.</p>

<h3>12. Poor original installation</h3>
<p>The quiet one. Inadequate vacuum evacuation leaves air and moisture in the circuit, which form acids
that corrode a compressor from inside. Pipe runs longer than specified without a charge adjustment
leave the system permanently under-performing. These faults do not announce themselves; they simply
mean the unit never quite worked and gets worse each year.</p>

<h2>What a proper diagnosis involves</h2>

<p>An engineer who can tell you the fault without measuring anything is guessing. On a no-cooling call
we would expect to see suction and discharge pressures read on gauges, the temperature split measured
across the indoor coil, current draw checked against the compressor's rating, and the electrical side
verified before anything is replaced.</p>

<div class="callout">
  <p><strong>A fair test of any technician:</strong> ask what the temperature split is and what the
  pressures read. Someone diagnosing properly will have those numbers and will explain what they mean.
  Someone who does not will reach for the refrigerant cylinder first.</p>
</div>

<h2>How to stop it happening again</h2>

<p>The overwhelming majority of no-cooling calls trace back to something a routine service would have
caught while it was still cheap. In Delhi conditions that means cleaning every three to six months for
normal household use, and quarterly for anything running long hours or near a construction site or main
road.</p>

<ul>
  <li>Clean or replace filters regularly through the season.</li>
  <li>Keep at least a foot of clear air around the outdoor unit on every side.</li>
  <li>Have the condenser coil washed properly at least once a year, before summer.</li>
  <li>Act on small changes. A slight drop in cooling is a cheap fix; a dead compressor is not.</li>
  <li>If you have several units, put them on a schedule rather than trying to remember.</li>
</ul>
"""

RELATED = [
    ("../ac-repair.html", "AC Repair",
     "Not cooling, gas leaks, noise or tripping — diagnosed properly and repaired, usually same day."),
    ("../ac-servicing.html", "AC Servicing",
     "Deep cleaning, coil and condenser washing and gas checks that prevent most breakdowns."),
    ("how-often-ac-service.html", "How Often to Service?",
     "How frequently an AC needs servicing in Delhi conditions, by usage pattern."),
    ("ac-gas-filling-cost-delhi.html", "AC Gas Filling Guide",
     "What refrigerant top-up really involves, and why the leak must be found first."),
    ("../ac-amc.html", "AC AMC",
     "Scheduled maintenance with priority response, for homes and commercial sites."),
    ("../ac-service-delhi.html", "AC Service in Delhi",
     "Zone-by-zone coverage across every part of Delhi."),
]


def build():
    return render_article(
        slug="ac-not-cooling.html",
        title="AC Not Cooling? 12 Reasons Why and How to Fix It",
        desc="AC running but not cooling? The 12 real causes, what each looks like, what you can check yourself and what needs an engineer. Call +91 93122 64832.",
        h1="AC Not Cooling? 12 Reasons Why, and How to Fix Each One",
        lede="Your air conditioner is running, the fan is turning, and the room stays warm. Here is what is actually going on, in the order we find it across Delhi NCR.",
        body=BODY, faqs=FAQS, related_cards=RELATED,
        category="Troubleshooting", read_minutes=9)
