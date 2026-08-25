#!/usr/bin/env python3
"""Delhi location page content."""
from content_loc_common import location_page, local_faqs

# ================================================================= DELHI ====
def delhi():
    zones = [
        ("South Delhi", "Our home turf",
         "Our office has been in Sant Nagar, East of Kailash since 1987, so South Delhi is genuinely local for us — most of these localities are within a short drive. The mix here runs from independent kothis in Defence Colony and Golf Links to high-rise apartments in Vasant Kunj and the commercial density of Nehru Place. We handle a great deal of diplomatic and institutional work in this zone, alongside long-standing household clients whose systems we have maintained for decades. Nearest metro references our engineers work from include Lajpat Nagar, Kailash Colony, Nehru Place, Saket, Hauz Khas and Malviya Nagar.",
         ["Saket", "Vasant Kunj", "Vasant Vihar", "Hauz Khas", "Green Park", "Greater Kailash I",
          "Greater Kailash II", "East of Kailash", "Defence Colony", "Lajpat Nagar", "Malviya Nagar",
          "Chittaranjan Park", "Nehru Place", "Kalkaji", "Govindpuri", "Okhla", "New Friends Colony",
          "Maharani Bagh", "Safdarjung Enclave", "SDA", "Panchsheel Park", "Panchsheel Enclave",
          "South Extension I", "South Extension II", "Jor Bagh", "Golf Links", "Lodhi Colony",
          "Jangpura", "Andrews Ganj", "Alaknanda", "Chhatarpur", "Mehrauli", "Sainik Farm",
          "Pushp Vihar", "Sarita Vihar", "Jasola", "Shaheen Bagh", "Jamia Nagar", "Sukhdev Vihar",
          "Badarpur", "Tughlakabad", "Sangam Vihar", "Madangir", "Ambedkar Nagar", "Moolchand",
          "Chirag Delhi", "Sheikh Sarai", "Khirki Extension", "Lado Sarai", "Satbari", "Fatehpur Beri"]),
        ("North Delhi", "Established colonies",
         "North Delhi mixes old established colonies such as Civil Lines and Model Town with the planned sectors of Rohini and the dense residential blocks of Pitampura and Shalimar Bagh. A large share of our work here is with older buildings, where wiring and existing pipe routing need proper assessment before any new installation — something a quick quote over the phone cannot cover. The student housing belt around Kamla Nagar and Mukherjee Nagar also brings steady demand for window and split repairs, where repairing rather than replacing is usually the right call.",
         ["Model Town", "Civil Lines", "Rohini", "Pitampura", "Shalimar Bagh", "Ashok Vihar",
          "Adarsh Nagar", "Kamla Nagar", "Shakti Nagar", "Mukherjee Nagar", "Burari", "Alipur",
          "Narela", "Bawana", "Timarpur", "Wazirabad", "Gulabi Bagh", "Sadar Bazar",
          "Chandni Chowk", "Kashmere Gate"]),
        ("East Delhi", "Dense residential",
         "East Delhi is dense, largely residential and heavily apartment-based, from Mayur Vihar and Patparganj through to Preet Vihar and Laxmi Nagar. Outdoor unit placement is the recurring challenge here — balconies are shared, shafts are tight, and condensers are frequently installed where they cannot breathe or be serviced safely. We spend real time on siting in this zone, because an outdoor unit starved of airflow will never cool properly no matter how good the machine is. The Anand Vihar and Vivek Vihar commercial pockets add regular cassette and ducted work.",
         ["Preet Vihar", "Laxmi Nagar", "Mayur Vihar Phase 1", "Mayur Vihar Phase 2",
          "Mayur Vihar Phase 3", "Patparganj", "IP Extension", "Pandav Nagar", "Nirman Vihar",
          "Krishna Nagar", "Shakarpur", "Anand Vihar", "Vivek Vihar", "Dilshad Garden",
          "Harsh Vihar", "New Ashok Nagar", "Vasundhara Enclave", "Geeta Colony", "Gandhi Nagar",
          "Jhilmil Colony", "Shahdara", "Mansarovar Park"]),
        ("West Delhi", "Wide coverage",
         "West Delhi spans a lot of ground, from the planned sectors of Dwarka through Janakpuri, Rajouri Garden and Punjabi Bagh out to Najafgarh and Uttam Nagar. Dwarka in particular generates steady multi-unit apartment work, where coordinating servicing across several systems in one flat makes an annual contract genuinely worthwhile. The retail concentration around Rajouri Garden and Kirti Nagar brings regular commercial cassette and ducted work, usually scheduled outside trading hours so we are not working around customers.",
         ["Janakpuri", "Dwarka", "Rajouri Garden", "Punjabi Bagh", "Paschim Vihar", "Vikaspuri",
          "Tilak Nagar", "Uttam Nagar", "Hari Nagar", "Subhash Nagar", "Kirti Nagar", "Moti Nagar",
          "Tagore Garden", "Ramesh Nagar", "Patel Nagar", "Rajendra Place", "Naraina", "Mayapuri",
          "Najafgarh", "Palam", "Dabri", "Bindapur", "Kakrola", "Matiala", "Mahavir Enclave",
          "Mohan Garden", "Nihal Vihar"]),
        ("Central Delhi", "Commercial core",
         "Central Delhi is where our commercial and institutional work concentrates — Connaught Place, Barakhamba Road and the offices around ITO. Buildings here are frequently older with retrofitted systems, and access is genuinely constrained: service windows are narrow, lifts are shared, and roof access needs arranging in advance. We plan these jobs around the building rather than around our own convenience. Karol Bagh and Paharganj add a steady stream of hotel and guest-house work where quiet operation matters more than anything else.",
         ["Connaught Place", "Karol Bagh", "Paharganj", "Rajendra Nagar", "Daryaganj", "ITO",
          "Barakhamba Road", "Mandi House", "Chelmsford Road", "Patel Chest", "Gole Market"]),
        ("New Delhi (NDMC)", "Diplomatic zone",
         "This is the zone that shaped how we work. We took our first embassy contract in 1995, and diplomatic and government properties across Chanakyapuri, the Diplomatic Enclave and Lutyens' Delhi have been part of our client base ever since. Work here comes with requirements most residential jobs never involve: security clearance and escorting, documented procedures, strict scheduling, and an absolute expectation that nothing goes wrong. Fifteen-plus missions have kept us on for decades, which is the reference we point to most often.",
         ["Chanakyapuri", "Diplomatic Enclave", "Lutyens Delhi", "Race Course Road", "Teen Murti",
          "Akbar Road", "Aurangzeb Road", "Prithviraj Road", "Amrita Shergill Marg", "Sundar Nagar",
          "Nizamuddin East", "Nizamuddin West", "Jor Bagh", "Lodi Estate", "Golf Links",
          "Bharati Nagar", "Pandara Road"]),
    ]

    intro = ("<p>Air Control has served Delhi from the same East of Kailash office since <strong>1987</strong>. "
             "Over thirty-eight years that has meant working in nearly every kind of building this city has — "
             "Lutyens bungalows and Dwarka apartments, Nehru Place offices and Chandni Chowk shopfronts, "
             "embassies in Chanakyapuri and clinics in Rohini.</p>"
             "<p>That range matters more than it might sound, because Delhi is not one cooling problem. "
             "A top-floor west-facing flat in Rohini, a glass-fronted showroom in South Extension and a "
             "server room in Nehru Place need genuinely different answers. Our engineers work these areas "
             "daily and know the recurring local constraints — which colonies have voltage problems, where "
             "outdoor units cannot be sited safely, which buildings need roof access arranged in advance.</p>"
             "<p>Below is our coverage by zone. If your locality is not listed, call us anyway — the list "
             "reflects where we work most often, not the limit of where we go.</p>")

    faqs = local_faqs("Delhi", "all of South, North, East, West and Central Delhi as well as the NDMC area", extra=[
        ("Do you cover both South Delhi and outer areas like Najafgarh or Narela?",
         "Yes. South Delhi is our home ground — our office is in East of Kailash — but we cover the whole city including outer areas such as Najafgarh, Narela, Bawana and Alipur. Scheduling for outer localities is sometimes a day rather than same-day in peak season, and we will tell you that honestly when you call rather than promising same-day and missing it."),
        ("Do you work with embassies and government properties in Delhi?",
         "Yes, and we have since 1995. We work across Chanakyapuri, the Diplomatic Enclave and Lutyens' Delhi, and we are used to the requirements that come with it — security clearance, escorted access, documented procedures and strict scheduling windows. Fifteen-plus diplomatic missions have retained us over the long term."),
    ])

    return location_page(
        slug="ac-service-delhi.html",
        title="AC Repair &amp; Service in Delhi | All Areas | Air Control",
        desc="AC repair, service &amp; installation across all Delhi since 1987. South, North, East, West, Central &amp; NDMC areas. Call +91 93122 64832.",
        h1="AC Repair, Service &amp; Installation Across <em>All Delhi</em>",
        hero_sub="Based in East of Kailash since 1987, our engineers work every zone of Delhi daily — from Lutyens bungalows and Chanakyapuri missions to Dwarka apartments and Nehru Place offices.",
        city="Delhi", intro_html=intro, zones=zones, faqs=faqs,
        area_list=["Delhi", "New Delhi", "South Delhi", "North Delhi", "East Delhi",
                   "West Delhi", "Central Delhi"],
        xlinks=[
            ("ac-repair.html", "AC Repair", "Not cooling, leaking or tripping — diagnosed and fixed, usually same day."),
            ("ac-servicing.html", "AC Servicing", "Deep cleaning, gas top-up and performance checks that lower running costs."),
            ("ac-amc.html", "AC AMC", "Scheduled maintenance with priority response for homes and commercial sites."),
            ("ac-service-gurgaon.html", "AC Service Gurgaon", "DLF, Golf Course Road, Cyber City and all sectors."),
            ("ac-service-noida.html", "AC Service Noida", "All sectors plus Greater Noida and Noida Extension."),
            ("ac-service-ghaziabad.html", "AC Service Ghaziabad", "Indirapuram, Vaishali, Vasundhara and the NH-9 corridor."),
        ])
