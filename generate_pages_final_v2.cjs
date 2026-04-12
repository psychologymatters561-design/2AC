const fs = require('fs');
const path = require('path');

const WEB3FORMS_KEY = "YOUR_WEB3FORMS_ACCESS_KEY";

const css = `
:root {
  --primary-navy: #0a1628;
  --gold-accent: #c8a86e;
  --royal-blue: #1e3a5f;
  --light-bg: #f8f6f2;
  --white: #ffffff;
  --text-dark: #333333;
  --text-light: #f4f4f4;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; font-family: 'DM Sans', sans-serif; }
body { background-color: var(--light-bg); color: var(--text-dark); line-height: 1.6; overflow-x: hidden; }
h1, h2, h3, h4, h5, h6 { font-family: 'Playfair Display', serif; color: var(--primary-navy); margin-bottom: 1rem; }
a { text-decoration: none; color: inherit; }
img { max-width: 100%; height: auto; display: block; }

/* Header */
header {
  position: sticky; top: 0; z-index: 1000;
  background: rgba(10, 22, 40, 0.95);
  backdrop-filter: blur(10px);
  color: var(--white);
  padding: 1rem 5%;
  display: flex; justify-content: space-between; align-items: center;
}
header h1, header h2, header a { color: var(--white); margin: 0; }
.nav-links { display: flex; gap: 1.5rem; align-items: center; }
.nav-links a { font-weight: 500; transition: color 0.3s; }
.nav-links a:hover { color: var(--gold-accent); }
.dropdown { position: relative; }
.dropdown-content {
  display: none; position: absolute; top: 100%; left: 0;
  background: var(--primary-navy); min-width: 200px;
  box-shadow: 0 8px 16px rgba(0,0,0,0.2); border-radius: 4px; overflow: hidden;
}
.dropdown:hover .dropdown-content { display: block; }
.dropdown-content a { display: block; padding: 0.75rem 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); }
.dropdown-content a:hover { background: var(--royal-blue); }

/* CTAs */
.cta-btn {
  background: linear-gradient(135deg, #c8a86e, #b08d55);
  color: var(--white); padding: 0.75rem 1.5rem; border-radius: 4px;
  font-weight: bold; transition: transform 0.3s, box-shadow 0.3s;
  display: inline-block; border: none; cursor: pointer;
}
.cta-btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(200, 168, 110, 0.4); }
.cta-btn-outline {
  background: transparent; border: 2px solid var(--gold-accent);
  color: var(--gold-accent); padding: 0.75rem 1.5rem; border-radius: 4px;
  font-weight: bold; transition: all 0.3s; display: inline-block;
}
.cta-btn-outline:hover { background: var(--gold-accent); color: var(--white); }

/* Hero Section */
.hero {
  background: linear-gradient(rgba(10, 22, 40, 0.8), rgba(10, 22, 40, 0.8)), url('https://picsum.photos/seed/ac/1920/1080') center/cover;
  color: var(--white); padding: 6rem 5%; text-align: center;
}
.hero h1 { color: var(--white); font-size: 3rem; margin-bottom: 1rem; }
.hero p { font-size: 1.2rem; margin-bottom: 2rem; max-width: 800px; margin-inline: auto; }
.hero .cta-group { display: flex; gap: 1rem; justify-content: center; }

/* Sections & Cards */
section { padding: 4rem 5%; }
.section-title { text-align: center; font-size: 2.5rem; margin-bottom: 3rem; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }
.glass-card {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 8px; padding: 2rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.05);
  transition: transform 0.3s;
}
.glass-card:hover { transform: translateY(-5px); }

/* Forms */
.form-group { margin-bottom: 1.5rem; }
.form-group label { display: block; margin-bottom: 0.5rem; font-weight: bold; }
.form-control {
  width: 100%; padding: 0.75rem; border: 1px solid #ccc; border-radius: 4px;
  font-family: inherit; font-size: 1rem;
}
textarea.form-control { resize: vertical; min-height: 100px; }

/* Breadcrumbs */
.breadcrumbs { padding: 1rem 5%; background: var(--white); font-size: 0.9rem; border-bottom: 1px solid #eee; }
.breadcrumbs a { color: var(--royal-blue); }
.breadcrumbs a:hover { text-decoration: underline; }

/* Footer */
footer { background: var(--primary-navy); color: var(--white); padding: 4rem 5% 2rem; }
.footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin-bottom: 2rem; }
.footer-col h3 { color: var(--gold-accent); margin-bottom: 1.5rem; }
.footer-col ul { list-style: none; }
.footer-col ul li { margin-bottom: 0.75rem; }
.footer-col ul li a:hover { color: var(--gold-accent); }
.footer-bottom { text-align: center; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); font-size: 0.9rem; }

/* Mobile Bottom Bar */
.mobile-bottom-bar {
  display: none; position: fixed; bottom: 0; left: 0; right: 0;
  background: var(--white); box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
  z-index: 1000;
}
.mobile-bottom-bar a {
  flex: 1; text-align: center; padding: 1rem; font-weight: bold;
  display: flex; justify-content: center; align-items: center; gap: 0.5rem;
}
.mobile-call { background: var(--primary-navy); color: var(--white); }
.mobile-wa { background: #25D366; color: var(--white); }

/* Animations */
.fade-in-up { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease-out, transform 0.8s ease-out; }
.fade-in-up.visible { opacity: 1; transform: translateY(0); }

/* Responsive */
@media (max-width: 768px) {
  .nav-links { display: none; }
  .mobile-bottom-bar { display: flex; }
  body { padding-bottom: 60px; }
  .hero h1 { font-size: 2rem; }
}
`;

const js = `
document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in-up').forEach(el => observer.observe(el));
});
`;

function getHeader(pathPrefix = '') {
  return `
  <header>
    <div class="logo">
      <a href="${pathPrefix}index.html" style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: bold; color: var(--gold-accent);">Air Control</a>
    </div>
    <nav class="nav-links">
      <a href="${pathPrefix}index.html">Home</a>
      <div class="dropdown">
        <a href="#">Services ▾</a>
        <div class="dropdown-content">
          <a href="${pathPrefix}ac-repair.html">AC Repair</a>
          <a href="${pathPrefix}ac-servicing.html">AC Servicing</a>
          <a href="${pathPrefix}ac-installation.html">AC Installation</a>
          <a href="${pathPrefix}ac-amc.html">AC AMC</a>
        </div>
      </div>
      <div class="dropdown">
        <a href="#">Areas ▾</a>
        <div class="dropdown-content">
          <a href="${pathPrefix}ac-service-delhi.html">Delhi</a>
          <a href="${pathPrefix}ac-service-gurgaon.html">Gurgaon</a>
          <a href="${pathPrefix}ac-service-noida.html">Noida</a>
          <a href="${pathPrefix}ac-service-faridabad.html">Faridabad</a>
          <a href="${pathPrefix}ac-service-ghaziabad.html">Ghaziabad</a>
        </div>
      </div>
      <a href="${pathPrefix}blog.html">Blog</a>
      <a href="#contact" class="cta-btn">Call +91 93122 64832</a>
    </nav>
  </header>
  <div class="mobile-bottom-bar">
    <a href="tel:+919312264832" class="mobile-call">📞 Call Now</a>
    <a href="https://wa.me/919312264832" class="mobile-wa">💬 WhatsApp</a>
  </div>
  `;
}

function getFooter(pathPrefix = '') {
  return `
  <footer id="contact">
    <div class="footer-grid">
      <div class="footer-col">
        <h3 style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: bold; color: var(--gold-accent);">Air Control</h3>
        <p>Trusted AC repair, servicing, installation, and AMC company in Delhi NCR since 1987.</p>
        <br>
        <p>📍 Sant Nagar, East of Kailash, New Delhi 110065</p>
        <p>📞 <a href="tel:+919312264832">+91 93122 64832</a></p>
        <p>✉️ <a href="mailto:ajay@aircontrols.in">ajay@aircontrols.in</a></p>
      </div>
      <div class="footer-col">
        <h3>Services</h3>
        <ul>
          <li><a href="${pathPrefix}ac-repair.html">AC Repair</a></li>
          <li><a href="${pathPrefix}ac-servicing.html">AC Servicing</a></li>
          <li><a href="${pathPrefix}ac-installation.html">AC Installation</a></li>
          <li><a href="${pathPrefix}ac-amc.html">AC AMC</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Service Areas</h3>
        <ul>
          <li><a href="${pathPrefix}ac-service-delhi.html">Delhi</a></li>
          <li><a href="${pathPrefix}ac-service-gurgaon.html">Gurgaon</a></li>
          <li><a href="${pathPrefix}ac-service-noida.html">Noida</a></li>
          <li><a href="${pathPrefix}ac-service-faridabad.html">Faridabad</a></li>
          <li><a href="${pathPrefix}ac-service-ghaziabad.html">Ghaziabad</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Quick Links</h3>
        <ul>
          <li><a href="${pathPrefix}index.html">Home</a></li>
          <li><a href="${pathPrefix}blog.html">Blog</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 Air Control. All rights reserved.</p>
    </div>
  </footer>
  `;
}

function getForm() {
  return `
  <div class="glass-card fade-in-up" style="max-width: 600px; margin: 0 auto;">
    <h3 style="text-align: center; margin-bottom: 1.5rem;">Request a Free Quote</h3>
    <form action="https://api.web3forms.com/submit" method="POST">
      <input type="hidden" name="access_key" value="${WEB3FORMS_KEY}">
      <div class="form-group">
        <label>Name</label>
        <input type="text" name="name" class="form-control" required>
      </div>
      <div class="form-group">
        <label>Phone Number</label>
        <input type="tel" name="phone" class="form-control" required>
      </div>
      <div class="form-group">
        <label>Service Required</label>
        <select name="service" class="form-control" required>
          <option value="Repair">AC Repair</option>
          <option value="Servicing">AC Servicing</option>
          <option value="Installation">AC Installation</option>
          <option value="AMC">AC AMC</option>
        </select>
      </div>
      <div class="form-group">
        <label>Message / Problem Description</label>
        <textarea name="message" class="form-control" required></textarea>
      </div>
      <button type="submit" class="cta-btn" style="width: 100%;">Submit Request</button>
    </form>
  </div>
  `;
}

function generatePage(filename, title, desc, h1, keywords, content, pathPrefix = '') {
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <meta name="description" content="${desc}">
  <meta name="keywords" content="${keywords}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://aircontrols.in/${filename}">
  
  <!-- Open Graph -->
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${desc}">
  <meta property="og:url" content="https://aircontrols.in/${filename}">
  <meta property="og:type" content="website">
  
  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title}">
  <meta name="twitter:description" content="${desc}">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet">
  
  <style>${css}</style>
</head>
<body>
  ${getHeader(pathPrefix)}
  
  <main>
    ${content}
  </main>
  
  ${getFooter(pathPrefix)}
  
  <script>${js}</script>
</body>
</html>`;

  const fullPath = path.join(__dirname, filename);
  const dir = path.dirname(fullPath);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  fs.writeFileSync(fullPath, html);
  console.log(`Created ${filename}`);
}

// --- PAGE 1: AC Repair ---
generatePage(
  'ac-repair.html',
  'AC Repair in Delhi NCR | Emergency AC Repair Service | Air Control Since 1987',
  'Expert AC repair in Delhi NCR. 38 years of trust, 2-hour response, genuine parts. Call us for split, window, and central AC repair services.',
  'Expert AC Repair Service in Delhi NCR',
  'AC repair Delhi, AC repair near me, AC not cooling, AC not working, AC gas leak repair',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; <a href="#">Services</a> &gt; AC Repair
  </div>
  <section class="hero">
    <h1 class="fade-in-up">Expert AC Repair Service in Delhi NCR</h1>
    <p class="fade-in-up">38 years of trust. 2-hour emergency response. Genuine parts with warranty.</p>
    <div class="cta-group fade-in-up">
      <a href="tel:+919312264832" class="cta-btn">Call Now: +91 93122 64832</a>
      <a href="https://wa.me/919312264832" class="cta-btn-outline" style="background: rgba(255,255,255,0.1);">WhatsApp Us</a>
    </div>
  </section>
  
  <section>
    <h2 class="section-title fade-in-up">Common AC Problems We Fix</h2>
    <div class="grid">
      <div class="glass-card fade-in-up">
        <h3>❄️ AC Not Cooling</h3>
        <p>Compressor issues, gas leaks, or blocked filters causing poor cooling performance.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h3>💧 Water Leaking</h3>
        <p>Clogged drain pipes or frozen coils causing water to drip inside your room.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h3>🔊 Strange Noises</h3>
        <p>Rattling, buzzing, or grinding sounds indicating motor or fan issues.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h3>⚡ AC Tripping</h3>
        <p>Electrical faults, PCB board failures, or overloaded compressors.</p>
      </div>
    </div>
  </section>
  
  <section style="background: var(--white);">
    <h2 class="section-title fade-in-up">AC Brands We Repair</h2>
    <p class="fade-in-up" style="text-align: center; max-width: 800px; margin: 0 auto 2rem;">We repair all major brands including Daikin, Blue Star, Voltas, LG, Samsung, Hitachi, Carrier, O General, Mitsubishi, Panasonic, Godrej, Lloyd, Whirlpool, Haier, Toshiba, and Sanyo.</p>
    <h2 class="section-title fade-in-up" style="margin-top: 4rem;">Types of AC We Repair</h2>
    <div class="grid">
      <div class="glass-card fade-in-up" style="text-align: center;"><h4>Split AC</h4></div>
      <div class="glass-card fade-in-up" style="text-align: center;"><h4>Window AC</h4></div>
      <div class="glass-card fade-in-up" style="text-align: center;"><h4>Cassette AC</h4></div>
      <div class="glass-card fade-in-up" style="text-align: center;"><h4>Tower AC</h4></div>
      <div class="glass-card fade-in-up" style="text-align: center;"><h4>Ducted AC</h4></div>
      <div class="glass-card fade-in-up" style="text-align: center;"><h4>Central AC</h4></div>
      <div class="glass-card fade-in-up" style="text-align: center;"><h4>VRF/VRV Systems</h4></div>
    </div>
  </section>
  
  <section>
    <h2 class="section-title fade-in-up">Why Choose Air Control?</h2>
    <div class="grid" style="text-align: center; margin-bottom: 4rem;">
      <div class="fade-in-up">
        <h3 style="font-size: 3rem; color: var(--gold-accent);">38+</h3>
        <p>Years Experience</p>
      </div>
      <div class="fade-in-up">
        <h3 style="font-size: 3rem; color: var(--gold-accent);">15+</h3>
        <p>Embassies Trusted</p>
      </div>
      <div class="fade-in-up">
        <h3 style="font-size: 3rem; color: var(--gold-accent);">2hr</h3>
        <p>Response Time</p>
      </div>
    </div>
    ${getForm()}
  </section>
  
  <section style="background: var(--white);">
    <h2 class="section-title fade-in-up">Frequently Asked Questions</h2>
    <div style="max-width: 800px; margin: 0 auto;" class="fade-in-up">
      <div style="margin-bottom: 1.5rem;">
        <h4>Why is my AC not cooling?</h4>
        <p>Common reasons include dirty air filters, low refrigerant (gas leak), a faulty compressor, or a blocked condenser coil.</p>
      </div>
      <div style="margin-bottom: 1.5rem;">
        <h4>How much does AC repair cost in Delhi?</h4>
        <p>Costs vary depending on the issue. Minor repairs start at nominal rates, while part replacements (like PCB or compressor) cost more. We provide an upfront estimate after diagnosis.</p>
      </div>
      <div style="margin-bottom: 1.5rem;">
        <h4>How long does AC repair take?</h4>
        <p>Most common repairs are completed within 1-2 hours at your premises. Complex issues might require taking the unit to our workshop.</p>
      </div>
    </div>
  </section>
  `
);

// --- PAGE 2: AC Servicing ---
generatePage(
  'ac-servicing.html',
  'AC Service in Delhi NCR | AC Deep Cleaning & Gas Filling | Air Control',
  'Professional AC servicing, deep cleaning, foam wash, and gas filling in Delhi NCR. Improve cooling and reduce electricity bills.',
  'Professional AC Servicing in Delhi NCR',
  'AC service Delhi, AC servicing near me, AC cleaning, AC deep cleaning, AC foam wash',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; <a href="#">Services</a> &gt; AC Servicing
  </div>
  <section class="hero">
    <h1 class="fade-in-up">Professional AC Servicing in Delhi NCR</h1>
    <p class="fade-in-up">Deep cleaning, gas filling, and preventive maintenance for optimal cooling.</p>
    <div class="cta-group fade-in-up">
      <a href="tel:+919312264832" class="cta-btn">Book Service Now</a>
    </div>
  </section>
  
  <section>
    <h2 class="section-title fade-in-up">Types of AC Servicing We Offer</h2>
    <div class="grid">
      <div class="glass-card fade-in-up">
        <h3>General Service</h3>
        <p>Filter cleaning, basic coil check, and performance testing.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h3>Deep Cleaning (Foam + Jet Wash)</h3>
        <p>Thorough cleaning of indoor and outdoor units using pressurized water and specialized foam.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h3>Gas Filling / Refill</h3>
        <p>R32, R410A, and R22 gas top-up and complete refill after leak fixing.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h3>Sanitization</h3>
        <p>Elimination of bacteria, mold, and bad odors from your AC system.</p>
      </div>
    </div>
  </section>
  
  <section style="background: var(--white);">
    <div style="max-width: 800px; margin: 0 auto; text-align: center;" class="fade-in-up">
      <h2 class="section-title">Signs Your AC Needs Servicing</h2>
      <ul style="list-style: none; text-align: left; display: inline-block; font-size: 1.1rem;">
        <li style="margin-bottom: 0.5rem;">⚠️ Reduced cooling performance</li>
        <li style="margin-bottom: 0.5rem;">⚠️ Unusually high electricity bills</li>
        <li style="margin-bottom: 0.5rem;">⚠️ Bad smell or musty odor</li>
        <li style="margin-bottom: 0.5rem;">⚠️ Water leaking from the indoor unit</li>
        <li style="margin-bottom: 0.5rem;">⚠️ Unusual sounds during operation</li>
      </ul>
    </div>
  </section>
  
  <section>
    ${getForm()}
  </section>
  `
);

// --- PAGE 3: AC Installation ---
generatePage(
  'ac-installation.html',
  'AC Installation in Delhi NCR | Split AC, VRF & Central AC | Air Control',
  'Professional AC installation services in Delhi NCR. Split AC, Cassette, Ducted, VRF, and Central AC systems for homes and offices.',
  'Professional AC Installation in Delhi NCR',
  'AC installation Delhi, AC installation near me, split AC installation, VRF installation Delhi',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; <a href="#">Services</a> &gt; AC Installation
  </div>
  <section class="hero">
    <h1 class="fade-in-up">Professional AC Installation in Delhi NCR</h1>
    <p class="fade-in-up">Precision installation for Split ACs, VRF/VRV, and Central Air Conditioning systems.</p>
    <div class="cta-group fade-in-up">
      <a href="tel:+919312264832" class="cta-btn">Get Installation Quote</a>
    </div>
  </section>
  
  <section>
    <h2 class="section-title fade-in-up">Installation for Every Space</h2>
    <div class="grid">
      <div class="glass-card fade-in-up">
        <h3>Residential</h3>
        <p>Homes, apartments, and villas. Split and window AC installations with perfect aesthetics.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h3>Commercial</h3>
        <p>Offices, showrooms, and retail spaces. Cassette, ducted, and VRF systems.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h3>Industrial & Institutional</h3>
        <p>Hospitals, hotels, factories, and data centers. Heavy-duty central AC systems.</p>
      </div>
    </div>
  </section>
  
  <section style="background: var(--white);">
    <h2 class="section-title fade-in-up">Our Installation Standards</h2>
    <div class="grid">
      <div class="glass-card fade-in-up">
        <h4>Precision Pipe Welding</h4>
        <p>Ensuring zero gas leaks for the lifetime of the unit.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h4>Proper Insulation</h4>
        <p>High-quality insulation to prevent condensation and energy loss.</p>
      </div>
      <div class="glass-card fade-in-up">
        <h4>Load Calculation</h4>
        <p>Scientific assessment to recommend the exact tonnage required for your space.</p>
      </div>
    </div>
  </section>
  
  <section>
    ${getForm()}
  </section>
  `
);

// --- PAGE 4: AC AMC ---
generatePage(
  'ac-amc.html',
  'AC AMC in Delhi NCR | Annual Maintenance Contract for AC | Air Control Since 1987',
  'Premium AC Annual Maintenance Contract (AMC) in Delhi NCR. Preventive maintenance, priority response, and breakdown cover for homes and offices.',
  'AC Annual Maintenance Contract (AMC) — Premium Protection',
  'AC AMC, AC annual maintenance contract, AC AMC Delhi, commercial AC AMC',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; <a href="#">Services</a> &gt; AC AMC
  </div>
  <section class="hero">
    <h1 class="fade-in-up">AC Annual Maintenance Contract (AMC)</h1>
    <p class="fade-in-up">Premium Protection for Your Cooling Systems. Trusted by embassies and Fortune 500 companies.</p>
    <div class="cta-group fade-in-up">
      <a href="#quote" class="cta-btn">Request AMC Quote</a>
    </div>
  </section>
  
  <section>
    <div style="max-width: 900px; margin: 0 auto;">
      <h2 class="section-title fade-in-up">What is an AC AMC?</h2>
      <p class="fade-in-up" style="font-size: 1.1rem; margin-bottom: 2rem;">An Annual Maintenance Contract (AMC) is a premium service agreement that ensures your air conditioning systems run efficiently year-round. Instead of waiting for a breakdown, our proactive approach prevents issues before they occur, extending the lifespan of your equipment and significantly reducing energy consumption.</p>
      
      <h2 class="section-title fade-in-up" style="margin-top: 4rem;">What's Included in Our AMC</h2>
      <div class="grid">
        <div class="glass-card fade-in-up">
          <h4>Scheduled Preventive Visits</h4>
          <p>Quarterly comprehensive check-ups and deep cleaning.</p>
        </div>
        <div class="glass-card fade-in-up">
          <h4>Emergency Breakdown Cover</h4>
          <p>Priority response for any unexpected failures.</p>
        </div>
        <div class="glass-card fade-in-up">
          <h4>Performance Optimization</h4>
          <p>Gas pressure checks, electrical inspections, and coil cleaning.</p>
        </div>
        <div class="glass-card fade-in-up">
          <h4>Detailed Reporting</h4>
          <p>Digital service reports provided after every visit.</p>
        </div>
      </div>
    </div>
  </section>
  
  <section style="background: var(--white);">
    <h2 class="section-title fade-in-up">AMC Plans</h2>
    <div class="grid">
      <div class="glass-card fade-in-up" style="border-top: 4px solid var(--royal-blue);">
        <h3>Essential</h3>
        <p>Perfect for residential units.</p>
        <ul style="margin: 1rem 0 2rem 1.5rem;">
          <li>2 Preventive Visits/Year</li>
          <li>Filter & Coil Cleaning</li>
          <li>Performance Check</li>
        </ul>
        <a href="#quote" class="cta-btn-outline" style="width: 100%; text-align: center;">Request Quote</a>
      </div>
      <div class="glass-card fade-in-up" style="border-top: 4px solid var(--gold-accent); transform: scale(1.05); box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <h3>Professional</h3>
        <p>Ideal for offices and showrooms.</p>
        <ul style="margin: 1rem 0 2rem 1.5rem;">
          <li>4 Preventive Visits/Year</li>
          <li>Breakdown Coverage</li>
          <li>Priority Support</li>
          <li>Deep Jet Cleaning</li>
        </ul>
        <a href="#quote" class="cta-btn" style="width: 100%; text-align: center;">Request Quote</a>
      </div>
      <div class="glass-card fade-in-up" style="border-top: 4px solid var(--primary-navy);">
        <h3>Enterprise</h3>
        <p>For critical infrastructure.</p>
        <ul style="margin: 1rem 0 2rem 1.5rem;">
          <li>Unlimited Visits</li>
          <li>2-Hour Priority Response</li>
          <li>Dedicated Engineer</li>
          <li>Comprehensive Parts Cover</li>
        </ul>
        <a href="#quote" class="cta-btn-outline" style="width: 100%; text-align: center;">Request Quote</a>
      </div>
    </div>
  </section>
  
  <section id="quote">
    ${getForm()}
  </section>
  `
);

// --- LOCATION PAGES ---
const locations = [
  { file: 'ac-service-delhi.html', name: 'Delhi', desc: 'South Delhi, North Delhi, East Delhi, West Delhi, Central Delhi, and NDMC areas.' },
  { file: 'ac-service-gurgaon.html', name: 'Gurgaon', desc: 'DLF Phases, Sushant Lok, Golf Course Road, Cyber City, and all major sectors.' },
  { file: 'ac-service-noida.html', name: 'Noida & Greater Noida', desc: 'Sector 18, Noida Extension, Greater Noida, and Expressway sectors.' },
  { file: 'ac-service-faridabad.html', name: 'Faridabad', desc: 'NIT, Neharpar, Surajkund, and all major Faridabad sectors.' },
  { file: 'ac-service-ghaziabad.html', name: 'Ghaziabad', desc: 'Indirapuram, Vaishali, Vasundhara, and Raj Nagar Extension.' }
];

locations.forEach(loc => {
  generatePage(
    loc.file,
    `AC Repair & Service in ${loc.name} | Air Control Since 1987`,
    `Expert AC repair, servicing, and installation in ${loc.name}. Fast response, genuine parts, and 38 years of experience.`,
    `AC Repair, Service & Installation in ${loc.name}`,
    `AC repair ${loc.name}, AC service ${loc.name}, AC installation ${loc.name}`,
    `
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="#">Areas</a> &gt; ${loc.name}
    </div>
    <section class="hero">
      <h1 class="fade-in-up">AC Repair, Service & Installation in ${loc.name}</h1>
      <p class="fade-in-up">Serving all major localities in ${loc.name} with rapid response times.</p>
      <div class="cta-group fade-in-up">
        <a href="tel:+919312264832" class="cta-btn">Call Now</a>
      </div>
    </section>
    <section>
      <div style="max-width: 800px; margin: 0 auto;" class="fade-in-up">
        <h2>Areas We Cover in ${loc.name}</h2>
        <p style="font-size: 1.1rem; margin-top: 1rem;">${loc.desc} We provide comprehensive AC repair, deep cleaning, gas filling, and installation services across these localities. Our engineers are stationed strategically to ensure quick response times for both residential and commercial clients.</p>
      </div>
    </section>
    <section style="background: var(--white);">
      ${getForm()}
    </section>
    `
  );
});

// --- BLOG INDEX ---
generatePage(
  'blog.html',
  'AC Tips, Guides & Expert Advice | Air Control Blog',
  'Read expert tips on AC maintenance, repair guides, and buying advice from Air Control engineers.',
  'AC Tips & Expert Advice',
  'AC tips, AC maintenance guide, AC buying guide',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; Blog
  </div>
  <section class="hero" style="padding: 4rem 5%;">
    <h1 class="fade-in-up">AC Tips & Expert Advice</h1>
    <p class="fade-in-up">Insights from 38 years of cooling expertise.</p>
  </section>
  <section>
    <div class="grid">
      <div class="glass-card fade-in-up">
        <h3><a href="blog/ac-not-cooling.html">AC Not Cooling? 12 Reasons Why & How to Fix It</a></h3>
        <p>Discover the most common reasons your AC is running but not blowing cold air.</p>
        <a href="blog/ac-not-cooling.html" style="color: var(--royal-blue); font-weight: bold; margin-top: 1rem; display: inline-block;">Read More →</a>
      </div>
      <div class="glass-card fade-in-up">
        <h3><a href="blog/ac-gas-filling-cost-delhi.html">AC Gas Filling Cost in Delhi NCR (2025)</a></h3>
        <p>A complete guide to R32, R410A, and R22 gas refill prices and procedures.</p>
        <a href="blog/ac-gas-filling-cost-delhi.html" style="color: var(--royal-blue); font-weight: bold; margin-top: 1rem; display: inline-block;">Read More →</a>
      </div>
      <div class="glass-card fade-in-up">
        <h3><a href="blog/how-often-ac-service.html">How Often Should You Service Your AC?</a></h3>
        <p>Expert recommendations on maintenance schedules for optimal performance.</p>
        <a href="blog/how-often-ac-service.html" style="color: var(--royal-blue); font-weight: bold; margin-top: 1rem; display: inline-block;">Read More →</a>
      </div>
      <div class="glass-card fade-in-up">
        <h3><a href="blog/best-ac-for-home.html">Best AC for Home in India (2025)</a></h3>
        <p>Our expert buying guide to choosing the right split or window AC for your space.</p>
        <a href="blog/best-ac-for-home.html" style="color: var(--royal-blue); font-weight: bold; margin-top: 1rem; display: inline-block;">Read More →</a>
      </div>
      <div class="glass-card fade-in-up">
        <h3><a href="blog/ac-amc-worth-it.html">Is AC AMC Worth It?</a></h3>
        <p>A complete cost-benefit analysis of Annual Maintenance Contracts vs Pay-Per-Service.</p>
        <a href="blog/ac-amc-worth-it.html" style="color: var(--royal-blue); font-weight: bold; margin-top: 1rem; display: inline-block;">Read More →</a>
      </div>
    </div>
  </section>
  `
);

// --- BLOG ARTICLES ---
const blogs = [
  { file: 'blog/ac-not-cooling.html', title: 'AC Not Cooling? 12 Reasons Why & How to Fix It', h1: 'AC Not Cooling? 12 Reasons Why & How to Fix It' },
  { file: 'blog/ac-gas-filling-cost-delhi.html', title: 'AC Gas Filling Cost in Delhi NCR (2025) — Complete Guide', h1: 'AC Gas Filling Cost in Delhi NCR (2025)' },
  { file: 'blog/how-often-ac-service.html', title: 'How Often Should You Service Your AC? Expert Guide', h1: 'How Often Should You Service Your AC?' },
  { file: 'blog/best-ac-for-home.html', title: 'Best AC for Home in India (2025) — Expert Buying Guide', h1: 'Best AC for Home in India (2025)' },
  { file: 'blog/ac-amc-worth-it.html', title: 'Is AC AMC Worth It? Complete Cost-Benefit Analysis', h1: 'Is AC AMC Worth It? Complete Cost-Benefit Analysis' }
];

blogs.forEach(blog => {
  generatePage(
    blog.file,
    blog.title,
    blog.title,
    blog.h1,
    'AC tips, AC repair',
    `
    <div class="breadcrumbs">
      <a href="../index.html">Home</a> &gt; <a href="../blog.html">Blog</a> &gt; Article
    </div>
    <section style="max-width: 800px; margin: 0 auto; padding: 4rem 5%;">
      <h1 class="fade-in-up" style="font-size: 2.5rem; margin-bottom: 2rem;">${blog.h1}</h1>
      <div class="fade-in-up" style="font-size: 1.1rem; line-height: 1.8;">
        <p>Welcome to our expert guide. With over 38 years of experience in the air conditioning industry, our engineers have compiled this comprehensive resource to help you make informed decisions about your cooling systems.</p>
        <br>
        <p>Regular maintenance, timely repairs, and choosing the right equipment are crucial for optimal performance, energy efficiency, and longevity of your AC units. If you need professional assistance, our team is always ready to help.</p>
        <br>
        <div style="background: var(--light-bg); padding: 2rem; border-left: 4px solid var(--gold-accent); margin: 2rem 0;">
          <h3>Need Expert Help?</h3>
          <p>Contact Air Control for professional AC services in Delhi NCR.</p>
          <a href="tel:+919312264832" class="cta-btn" style="margin-top: 1rem;">Call Now</a>
        </div>
      </div>
    </section>
    `,
    '../'
  );
});

// --- SITEMAP & ROBOTS ---
const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://aircontrols.in/</loc></url>
  <url><loc>https://aircontrols.in/ac-repair.html</loc></url>
  <url><loc>https://aircontrols.in/ac-servicing.html</loc></url>
  <url><loc>https://aircontrols.in/ac-installation.html</loc></url>
  <url><loc>https://aircontrols.in/ac-amc.html</loc></url>
  <url><loc>https://aircontrols.in/ac-service-delhi.html</loc></url>
  <url><loc>https://aircontrols.in/ac-service-gurgaon.html</loc></url>
  <url><loc>https://aircontrols.in/ac-service-noida.html</loc></url>
  <url><loc>https://aircontrols.in/ac-service-faridabad.html</loc></url>
  <url><loc>https://aircontrols.in/ac-service-ghaziabad.html</loc></url>
  <url><loc>https://aircontrols.in/blog.html</loc></url>
  <url><loc>https://aircontrols.in/blog/ac-not-cooling.html</loc></url>
  <url><loc>https://aircontrols.in/blog/ac-gas-filling-cost-delhi.html</loc></url>
  <url><loc>https://aircontrols.in/blog/how-often-ac-service.html</loc></url>
  <url><loc>https://aircontrols.in/blog/best-ac-for-home.html</loc></url>
  <url><loc>https://aircontrols.in/blog/ac-amc-worth-it.html</loc></url>
</urlset>`;
fs.writeFileSync(path.join(__dirname, 'sitemap.xml'), sitemap);

const robots = `User-agent: *
Allow: /
Sitemap: https://aircontrols.in/sitemap.xml`;
fs.writeFileSync(path.join(__dirname, 'robots.txt'), robots);

console.log('All files generated successfully!');
