import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const WEB3FORMS_KEY = "YOUR_WEB3FORMS_ACCESS_KEY";

const css = `
:root {
  --primary: #0F172A; /* Deep Navy/Slate */
  --accent: #B4935A; /* Institutional Gold */
  --accent-hover: #9A7B48;
  --bg-light: #F8FAFC;
  --surface: #FFFFFF;
  --text-main: #334155;
  --text-muted: #64748B;
  --border: #E2E8F0;
}

* { margin: 0; padding: 0; box-sizing: border-box; }
html { scroll-behavior: smooth; font-size: 16px; }
body { 
  background-color: var(--bg-light); 
  color: var(--text-main); 
  font-family: 'Inter', sans-serif; 
  line-height: 1.7; 
  overflow-x: hidden; 
}

h1, h2, h3, h4, h5, h6 { 
  font-family: 'Playfair Display', serif; 
  color: var(--primary); 
  font-weight: 700;
  line-height: 1.2;
}

a { text-decoration: none; color: inherit; transition: all 0.3s ease; }
img { max-width: 100%; height: auto; display: block; }

/* Premium Header */
header {
  position: fixed; 
  top: 0; left: 0; right: 0;
  z-index: 1000;
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(255,255,255,0.05);
  padding: 1.25rem 5%;
  display: flex; 
  justify-content: space-between; 
  align-items: center;
  transition: all 0.4s ease;
}
header.scrolled {
  padding: 0.75rem 5%;
  background: rgba(15, 23, 42, 0.98);
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.logo-container {
  display: flex;
  align-items: center;
}
.logo-img {
  height: 80px;
  width: auto;
  object-fit: contain;
  transition: transform 0.3s ease;
}
.logo-img:hover {
  transform: scale(1.05);
}
.logo-text {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--surface);
  letter-spacing: 1px;
  text-transform: uppercase;
}
.logo-text span { color: var(--accent); }

.nav-links { display: flex; gap: 2rem; align-items: center; }
.nav-links > a, .dropdown > a { 
  font-family: 'Inter', sans-serif;
  font-size: 0.875rem;
  font-weight: 500;
  color: #E2E8F0; 
  text-transform: uppercase;
  letter-spacing: 1px;
  position: relative;
}
.nav-links > a::after, .dropdown > a::after {
  content: '';
  position: absolute;
  bottom: -4px; left: 0;
  width: 0; height: 2px;
  background: var(--accent);
  transition: width 0.3s ease;
}
.nav-links > a:hover::after, .dropdown:hover > a::after { width: 100%; }
.nav-links > a:hover, .dropdown:hover > a { color: var(--surface); }

.dropdown { position: relative; padding-bottom: 10px; margin-bottom: -10px; }
.dropdown-content {
  visibility: hidden;
  opacity: 0;
  position: absolute; 
  top: 100%; left: 0;
  background: var(--surface); 
  min-width: 220px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1); 
  border-radius: 4px; 
  overflow: hidden;
  transform: translateY(10px);
  transition: all 0.3s ease;
  border: 1px solid var(--border);
}
.dropdown:hover .dropdown-content { 
  visibility: visible;
  opacity: 1;
  transform: translateY(0);
}
.dropdown-content a { 
  display: block; 
  padding: 1rem 1.5rem; 
  color: var(--text-main);
  font-size: 0.875rem;
  border-bottom: 1px solid var(--bg-light); 
  transition: background 0.2s, color 0.2s;
}
.dropdown-content a:hover { 
  background: var(--bg-light); 
  color: var(--accent);
  padding-left: 1.75rem;
}

/* Institutional Buttons */
.btn-premium {
  background-color: var(--accent);
  color: var(--surface);
  padding: 14px 32px;
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 0.875rem;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  border: 1px solid var(--accent);
  border-radius: 2px;
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  z-index: 1;
}
.btn-premium::before {
  content: '';
  position: absolute;
  top: 0; left: 0; width: 0; height: 100%;
  background-color: var(--primary);
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  z-index: -1;
}
.btn-premium:hover::before { width: 100%; }
.btn-premium:hover { border-color: var(--primary); color: var(--surface); }

.btn-outline {
  background-color: transparent;
  color: var(--surface);
  border: 1px solid var(--surface);
}
.btn-outline::before { background-color: var(--surface); }
.btn-outline:hover { color: var(--primary); border-color: var(--surface); }

/* Hero Section */
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 8rem 5% 4rem;
  background-color: var(--primary);
  overflow: hidden;
}
.hero-bg {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: url('https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=2069') center/cover no-repeat;
  opacity: 0.4;
  transform: scale(1.05);
  animation: slowZoom 20s linear infinite alternate;
}
@keyframes slowZoom {
  0% { transform: scale(1.05); }
  100% { transform: scale(1.15); }
}
.hero-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(90deg, rgba(15,23,42,0.9) 0%, rgba(15,23,42,0.6) 100%);
}
.hero-content {
  position: relative;
  z-index: 2;
  max-width: 800px;
}
.hero-subtitle {
  color: var(--accent);
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  letter-spacing: 3px;
  text-transform: uppercase;
  font-size: 0.875rem;
  margin-bottom: 1.5rem;
  display: block;
}
.hero h1 { 
  color: var(--surface); 
  font-size: 4.5rem; 
  margin-bottom: 1.5rem; 
  line-height: 1.1;
}
.hero p { 
  color: #CBD5E1; 
  font-size: 1.125rem; 
  margin-bottom: 3rem; 
  max-width: 600px; 
  font-weight: 300;
}
.hero .cta-group { display: flex; gap: 1.5rem; flex-wrap: wrap; }

/* Sections & Cards */
section { padding: 6rem 5%; }
.section-header { text-align: center; margin-bottom: 4rem; }
.section-subtitle {
  color: var(--accent);
  font-size: 0.875rem;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-bottom: 1rem;
  display: block;
}
.section-title { font-size: 3rem; color: var(--primary); }

.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2.5rem; }
.premium-card {
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 3rem 2rem;
  border-radius: 4px;
  transition: all 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
  position: relative;
  overflow: hidden;
  z-index: 1;
}
.premium-card::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0; width: 100%; height: 3px;
  background: var(--accent);
  transform: scaleX(0);
  transform-origin: right;
  transition: transform 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
  z-index: -1;
}
.premium-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08);
  border-color: transparent;
}
.premium-card:hover::after {
  transform: scaleX(1);
  transform-origin: left;
}
.premium-card h3 { font-size: 1.5rem; margin-bottom: 1rem; }
.premium-card p { color: var(--text-muted); margin-bottom: 2rem; }
.card-link {
  color: var(--primary);
  font-weight: 600;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}
.card-link::after { content: '→'; transition: transform 0.3s ease; }
.premium-card:hover .card-link { color: var(--accent); }
.premium-card:hover .card-link::after { transform: translateX(5px); }

/* Stats Section */
.stats-section {
  background-color: var(--primary);
  color: var(--surface);
  padding: 5rem 5%;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 3rem;
  text-align: center;
}
.stat-item h3 {
  font-size: 4rem;
  color: var(--accent);
  margin-bottom: 0.5rem;
}
.stat-item p {
  font-family: 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 0.875rem;
  color: #94A3B8;
}

/* Forms */
.form-container {
  background: var(--surface);
  padding: 4rem;
  border-radius: 4px;
  box-shadow: 0 20px 40px rgba(15, 23, 42, 0.05);
  border: 1px solid var(--border);
  max-width: 700px;
  margin: 0 auto;
}
.form-group { margin-bottom: 2rem; }
.form-group label { 
  display: block; 
  margin-bottom: 0.75rem; 
  font-weight: 600; 
  font-size: 0.875rem;
  color: var(--primary);
  text-transform: uppercase;
  letter-spacing: 1px;
}
.form-control {
  width: 100%; 
  padding: 1rem 1.25rem; 
  border: 1px solid var(--border); 
  border-radius: 2px;
  font-family: 'Inter', sans-serif; 
  font-size: 1rem;
  background: var(--bg-light);
  transition: all 0.3s ease;
}
.form-control:focus {
  outline: none;
  border-color: var(--accent);
  background: var(--surface);
  box-shadow: 0 0 0 3px rgba(180, 147, 90, 0.1);
}
textarea.form-control { resize: vertical; min-height: 150px; }

/* Breadcrumbs */
.breadcrumbs { 
  padding: 8rem 5% 2rem; 
  background: var(--primary); 
  color: #94A3B8;
  font-size: 0.875rem; 
}
.breadcrumbs a { color: var(--surface); }
.breadcrumbs a:hover { color: var(--accent); }

/* Footer */
footer { 
  background: #080C17; 
  color: #94A3B8; 
  padding: 6rem 5% 2rem; 
}
.footer-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
  gap: 4rem; 
  margin-bottom: 4rem; 
}
.footer-col h3 { 
  color: var(--surface); 
  margin-bottom: 2rem; 
  font-size: 1.25rem;
}
.footer-col ul { list-style: none; }
.footer-col ul li { margin-bottom: 1rem; }
.footer-col ul li a:hover { color: var(--accent); padding-left: 5px; }
.footer-bottom { 
  text-align: center; 
  padding-top: 2rem; 
  border-top: 1px solid rgba(255,255,255,0.05); 
  font-size: 0.875rem; 
}

/* Mobile Bottom Bar */
.mobile-bottom-bar {
  display: none; 
  position: fixed; 
  bottom: 24px; 
  left: 50%; 
  transform: translateX(-50%);
  background: rgba(15, 23, 42, 0.85); 
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.3), inset 0 1px 1px rgba(255,255,255,0.1);
  z-index: 1000;
  border-radius: 100px;
  overflow: hidden;
  width: 92%;
  max-width: 420px;
  border: 1px solid rgba(255,255,255,0.15);
  padding: 6px;
  gap: 8px;
}
.mobile-bottom-bar a {
  flex: 1; 
  text-align: center; 
  padding: 14px 10px; 
  font-weight: 600;
  display: flex; 
  justify-content: center; 
  align-items: center; 
  gap: 8px;
  font-size: 0.9rem; 
  text-transform: uppercase; 
  letter-spacing: 1px;
  border-radius: 100px;
  transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
  position: relative;
  overflow: hidden;
}
.mobile-call { 
  background: var(--surface); 
  color: var(--primary); 
}
.mobile-call:hover { 
  background: #f1f5f9; 
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(255,255,255,0.1);
}
.mobile-wa { 
  background: linear-gradient(135deg, #25D366, #128C7E); 
  color: var(--surface); 
  box-shadow: 0 4px 15px rgba(37, 211, 102, 0.3);
}
.mobile-wa:hover { 
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(37, 211, 102, 0.4);
}
.mobile-wa::before {
  content: '';
  position: absolute;
  top: 0; left: -100%; width: 50%; height: 100%;
  background: linear-gradient(to right, rgba(255,255,255,0) 0%, rgba(255,255,255,0.3) 50%, rgba(255,255,255,0) 100%);
  transform: skewX(-25deg);
  animation: shine 3s infinite;
}
@keyframes shine {
  0% { left: -100%; }
  20% { left: 200%; }
  100% { left: 200%; }
}

.pulse-icon {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.15); opacity: 0.8; }
}

/* Animations */
.reveal { 
  opacity: 0; 
  transform: translateY(40px); 
  transition: opacity 1s cubic-bezier(0.165, 0.84, 0.44, 1), transform 1s cubic-bezier(0.165, 0.84, 0.44, 1); 
}
.reveal.active { opacity: 1; transform: translateY(0); }
.delay-1 { transition-delay: 0.1s; }
.delay-2 { transition-delay: 0.2s; }
.delay-3 { transition-delay: 0.3s; }

/* Responsive */
@media (max-width: 992px) {
  .hero h1 { font-size: 3.5rem; }
}
@media (max-width: 768px) {
  .nav-links { display: none; }
  .mobile-bottom-bar { display: flex; }
  body { padding-bottom: 70px; }
  .hero { padding-top: 10rem; }
  .hero h1 { font-size: 2.5rem; }
  .form-container { padding: 2rem; }
}
`;

const js = `
document.addEventListener('DOMContentLoaded', () => {
  // Reveal Animations
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Header Scroll Effect
  const header = document.querySelector('header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });
});
`;

function getHeader(pathPrefix = '') {
  return `
  <header>
    <div class="logo-container">
      <a href="${pathPrefix}index.html">
        <img src="${pathPrefix}logo.png" alt="Air Control Logo" class="logo-img" onerror="this.onerror=null; this.src='https://placehold.co/200x80/0F172A/FFFFFF?text=Air+Control&font=Playfair+Display';">
      </a>
    </div>
    <nav class="nav-links">
      <a href="${pathPrefix}index.html">Home</a>
      <a href="${pathPrefix}why-us.html">Why Us</a>
      <div class="dropdown">
        <a href="#">Services</a>
        <div class="dropdown-content">
          <a href="${pathPrefix}ac-repair.html">AC Repair</a>
          <a href="${pathPrefix}ac-servicing.html">AC Servicing</a>
          <a href="${pathPrefix}ac-installation.html">AC Installation</a>
          <a href="${pathPrefix}ac-amc.html">AC AMC</a>
        </div>
      </div>
      <div class="dropdown">
        <a href="#">Areas</a>
        <div class="dropdown-content">
          <a href="${pathPrefix}ac-service-delhi.html">Delhi</a>
          <a href="${pathPrefix}ac-service-gurgaon.html">Gurgaon</a>
          <a href="${pathPrefix}ac-service-noida.html">Noida</a>
          <a href="${pathPrefix}ac-service-faridabad.html">Faridabad</a>
          <a href="${pathPrefix}ac-service-ghaziabad.html">Ghaziabad</a>
        </div>
      </div>
      <a href="${pathPrefix}blog.html">Insights</a>
      <a href="#contact" class="btn-premium" style="padding: 10px 24px; margin-left: 1rem;">Contact Us</a>
    </nav>
  </header>
  <div class="mobile-bottom-bar">
    <a href="tel:+919312264832" class="mobile-call">
      <svg class="pulse-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
      Call Now
    </a>
    <a href="https://wa.me/919312264832" class="mobile-wa">
      <svg class="pulse-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
      WhatsApp
    </a>
  </div>
  `;
}

function getFooter(pathPrefix = '') {
  return `
  <footer id="contact">
    <div class="footer-grid">
      <div class="footer-col">
        <h3 style="font-family: 'Playfair Display', serif; font-size: 1.75rem; font-weight: 700; color: var(--accent);">Air Control</h3>
        <p>Delhi NCR's top-rated AC repair, professional AC installation, and reliable AC servicing experts since 1987.</p>
        <br>
        <p>📍 Sant Nagar, East of Kailash, New Delhi 110065</p>
        <p>📞 <a href="tel:+919312264832" style="color: var(--surface);">+91 93122 64832</a></p>
        <p>✉️ <a href="mailto:ajay@aircontrols.in" style="color: var(--surface);">ajay@aircontrols.in</a></p>
      </div>
      <div class="footer-col">
        <h3>Expertise</h3>
        <ul>
          <li><a href="${pathPrefix}ac-repair.html">AC Repair & Diagnostics</a></li>
          <li><a href="${pathPrefix}ac-servicing.html">Comprehensive Servicing</a></li>
          <li><a href="${pathPrefix}ac-installation.html">System Installation</a></li>
          <li><a href="${pathPrefix}ac-amc.html">Annual Maintenance (AMC)</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Service Regions</h3>
        <ul>
          <li><a href="${pathPrefix}ac-service-delhi.html">Delhi</a></li>
          <li><a href="${pathPrefix}ac-service-gurgaon.html">Gurgaon</a></li>
          <li><a href="${pathPrefix}ac-service-noida.html">Noida</a></li>
          <li><a href="${pathPrefix}ac-service-faridabad.html">Faridabad</a></li>
          <li><a href="${pathPrefix}ac-service-ghaziabad.html">Ghaziabad</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h3>Corporate</h3>
        <ul>
          <li><a href="${pathPrefix}index.html">Company Overview</a></li>
          <li><a href="${pathPrefix}blog.html">Industry Insights</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-seo" style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.05); font-size: 0.75rem; color: #475569; line-height: 1.8; text-align: justify;">
      <p style="margin-bottom: 1rem;"><strong style="color: #64748B;">Local Service Areas & Searches:</strong> HVAC near me, heating and cooling near me, AC repair near me, furnace repair near me, air conditioning near me, HVAC installation near me, HVAC replacement near me, heating and air conditioning repair near me, HVAC companies near me, HVAC repair near me, duct cleaning near me, air duct cleaning near me, HVAC service near me, AC service near me, HVAC company near me, HVAC contractors near me, heating and cooling companies near me, air conditioning service near me, air conditioning services near me, HVAC services near me, air conditioning repair near me, best HVAC companies near me, commercial HVAC companies near me, air ducts cleaning near me, air condition service near me, emergency AC repair near me, heating and cooling service near me, home AC repair near me, local HVAC companies, commercial HVAC repair near me, local HVAC repair, best HVAC repair near me, residential HVAC near me, best heating and cooling companies near me, heat and air conditioning service near me, AC vent cleaning near me, ductless heating and cooling near me, best AC repair service in Gurgaon, AC repair Delhi, AC installation Noida, AC servicing Faridabad.</p>
      <p><strong style="color: #64748B;">Comprehensive HVAC Solutions:</strong> HVAC, air conditioning repair, AC repair, furnace repair, HVAC installation, HVAC replacement, air duct cleaning, HVAC system, air conditioning service, HVAC maintenance, commercial HVAC, heating repair, duct cleaning, heating and cooling companies, residential HVAC, AC servicing, air conditioning servicing, ductless heating and cooling, HVAC duct cleaning, central air installation, HVAC air purifier, whole house air purifier HVAC, water heater repair, air conditioning repair services, air duct cleaning services, air conditioning services, AC services, heat pump repair, air condition services, air conditioning service repair, duct cleaning services, furnace repair service, duct cleaning service, emergency furnace repair, AC vent cleaning, heating and air conditioning service, heating and cooling repair, heating and cooling services, commercial HVAC repair, HVAC repair service, air conditioning duct cleaning, best air purifier for HVAC system, split AC repair, AC installation services, air conditioning maintenance, affordable HVAC services, HVAC maintenance plan, AC tune-up near me, furnace maintenance service, air conditioning installation, HVAC system upgrade, HVAC system inspection, ductwork installation, indoor air quality solutions, HVAC energy efficiency upgrades, ventilation system maintenance, smart thermostat installation, boiler repair services, boiler replacement, ductless mini-split installation, smart thermostat setup, air handler repair, radiant heating system installation, ventilation system repair, thermostat replacement, energy-efficient HVAC installation.</p>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2025 Air Control. Excellence in Climate Management. All rights reserved.</p>
    </div>
  </footer>
  `;
}

function getForm() {
  return `
  <div class="form-container reveal">
    <div class="section-header" style="margin-bottom: 2rem;">
      <span class="section-subtitle">Connect With Us</span>
      <h3 style="font-size: 2.5rem;">Request a Consultation</h3>
    </div>
    <form action="https://api.web3forms.com/submit" method="POST">
      <input type="hidden" name="access_key" value="${WEB3FORMS_KEY}">
      <div class="form-group">
        <label>Full Name</label>
        <input type="text" name="name" class="form-control" placeholder="Enter your full name" required>
      </div>
      <div class="form-group">
        <label>Contact Number</label>
        <input type="tel" name="phone" class="form-control" placeholder="Enter your phone number" required>
      </div>
      <div class="form-group">
        <label>Service Required</label>
        <select name="service" class="form-control" required>
          <option value="" disabled selected>Select a service...</option>
          <option value="Repair">AC Repair & Diagnostics</option>
          <option value="Servicing">Comprehensive Servicing</option>
          <option value="Installation">System Installation</option>
          <option value="AMC">Annual Maintenance Contract (AMC)</option>
        </select>
      </div>
      <div class="form-group">
        <label>Project Details / Inquiry</label>
        <textarea name="message" class="form-control" placeholder="Please describe your requirements..." required></textarea>
      </div>
      <button type="submit" class="btn-premium" style="width: 100%; padding: 18px;">Submit Inquiry</button>
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
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet">
  
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

// --- PAGE 1: Home ---
generatePage(
  'index.html',
  'Air Control | Premium AC Repair, Servicing & AMC in Delhi NCR',
  'Top-rated AC repair, professional AC installation, and reliable AC servicing in Delhi NCR. We provide expert cooling solutions, deep cleaning, and comprehensive Annual Maintenance Contracts (AMC) for homes and businesses.',
  'Excellence in Climate Management',
  'AC repair Delhi NCR, premium AC service, commercial HVAC maintenance, VRF installation, AC AMC Delhi, Air Control since 1987, central air conditioning repair',
  `
  <section class="hero">
    <div class="hero-bg"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <span class="hero-subtitle reveal">Est. 1987 • 38 Years of Excellence</span>
      <h1 class="reveal delay-1">Where Air Conditioning Is Engineered, Not Improvised.</h1>
      <p class="reveal delay-2">Expert AC repair, professional air conditioning installation, and reliable AC servicing in Delhi NCR. We offer top-rated cooling solutions, split and window AC maintenance, central air conditioning repair, and comprehensive AMC services for residential and commercial spaces.</p>
      <div class="cta-group reveal delay-3">
        <a href="#contact" class="btn-premium">Schedule Consultation</a>
        <a href="tel:+919312264832" class="btn-premium btn-outline">Call +91 93122 64832</a>
      </div>
    </div>
  </section>
  
  <section>
    <div class="section-header reveal">
      <span class="section-subtitle">Our Expertise</span>
      <h2 class="section-title">Institutional Grade Services</h2>
    </div>
    <div class="grid">
      <div class="premium-card reveal">
        <h3>Diagnostics & Repair</h3>
        <p>Precision troubleshooting and repair for all major brands and complex HVAC systems. We ensure minimal downtime for your home or business.</p>
        <a href="ac-repair.html" class="card-link">Explore Service</a>
      </div>
      <div class="premium-card reveal delay-1">
        <h3>Comprehensive Servicing</h3>
        <p>Advanced deep cleaning and preventive maintenance protocols designed to extend equipment lifespan and optimize energy efficiency.</p>
        <a href="ac-servicing.html" class="card-link">Explore Service</a>
      </div>
      <div class="premium-card reveal delay-2">
        <h3>System Installation</h3>
        <p>Professional deployment of split, cassette, and central VRF systems, executed to the highest industry standards.</p>
        <a href="ac-installation.html" class="card-link">Explore Service</a>
      </div>
      <div class="premium-card reveal delay-3">
        <h3>Annual Maintenance (AMC)</h3>
        <p>Tailored maintenance contracts providing priority support, regular inspections, and complete peace of mind year-round.</p>
        <a href="ac-amc.html" class="card-link">Explore Service</a>
      </div>
    </div>
  </section>
  
  <section class="stats-section">
    <div class="stats-grid">
      <div class="stat-item reveal">
        <h3>38+</h3>
        <p>Years of Excellence</p>
      </div>
      <div class="stat-item reveal delay-1">
        <h3>10k+</h3>
        <p>Projects Completed</p>
      </div>
      <div class="stat-item reveal delay-2">
        <h3>24/7</h3>
        <p>Emergency Support</p>
      </div>
      <div class="stat-item reveal delay-3">
        <h3>100%</h3>
        <p>Client Satisfaction</p>
      </div>
    </div>
  </section>
  
  <section style="background-color: var(--bg-light);">
    ${getForm()}
  </section>
  `
);

// --- PAGE 2: AC Repair ---
generatePage(
  'ac-repair.html',
  'Premium AC Repair Services | Air Control Delhi NCR',
  'Expert AC repair services in Delhi NCR. We diagnose and fix all AC issues with precision and genuine parts.',
  'AC Repair & Diagnostics',
  'AC repair, AC not cooling, AC gas leak, AC compressor repair, Air Control repair',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; <a href="#">Services</a> &gt; AC Repair
  </div>
  <section class="hero" style="min-height: 60vh; padding-top: 12rem;">
    <div class="hero-bg" style="background-image: url('https://images.unsplash.com/photo-1581094288338-2314dddb7ece?q=80&w=2070');"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <span class="hero-subtitle reveal">Precision Diagnostics</span>
      <h1 class="reveal delay-1">AC Repair & Diagnostics</h1>
      <p class="reveal delay-2">Rapid response, expert troubleshooting, and lasting repairs for all commercial and residential air conditioning systems.</p>
    </div>
  </section>
  <section>
    <div class="grid">
      <div class="premium-card reveal">
        <h3>Advanced Troubleshooting</h3>
        <p>Our certified technicians use state-of-the-art diagnostic tools to identify the root cause of cooling failures, unusual noises, or electrical issues.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3>Genuine Components</h3>
        <p>We exclusively use OEM (Original Equipment Manufacturer) parts for all replacements, ensuring the longevity and optimal performance of your system.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3>Emergency Response</h3>
        <p>Understanding the critical nature of climate control, we offer priority emergency repair services across the Delhi NCR region.</p>
      </div>
    </div>
  </section>

  <section style="background-color: var(--surface);">
    <div class="section-header reveal">
      <span class="section-subtitle">Diagnostic Expertise</span>
      <h2 class="section-title">Common HVAC Problems We Solve</h2>
    </div>
    <div class="grid">
      <div class="premium-card reveal">
        <h3 style="font-size: 1.25rem;">Cooling & Airflow Issues</h3>
        <p>Experiencing an <strong>AC not blowing cold air</strong>, <strong>AC not cooling</strong> properly, or <strong>weak airflow AC</strong>? We diagnose frozen evaporator coils, signs of a refrigerant leak, and resolve issues where your AC compressor runs continuously.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3 style="font-size: 1.25rem;">Leaks, Noises & Odours</h3>
        <p>Don't ignore an <strong>AC leaking water</strong>, <strong>hissing sounds AC</strong>, <strong>AC making banging noise</strong>, <strong>AC making buzzing noise</strong>, or an <strong>AC unit emitting unusual odours</strong>. We fix AC water leakage problems fast.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3 style="font-size: 1.25rem;">Power & Thermostat Failures</h3>
        <p>If your <strong>AC not turning on</strong>, you're asking "<strong>why is my AC not working?</strong>", or dealing with <strong>AC remote not working</strong>, <strong>AC thermostat issues</strong>, or frequent cycling AC, our technicians provide immediate air conditioner fixes.</p>
      </div>
      <div class="premium-card reveal delay-3">
        <h3 style="font-size: 1.25rem;">Emergency Heating & AC</h3>
        <p>We offer <strong>emergency AC repair</strong>, <strong>24 hour AC repair</strong>, <strong>24/7 AC repair</strong>, <strong>emergency HVAC repair</strong>, <strong>same-day furnace repair</strong>, <strong>after-hours HVAC repair</strong>, <strong>weekend furnace repair</strong>, and <strong>late-night emergency AC service</strong> with a rapid response HVAC technician.</p>
      </div>
    </div>
  </section>

  <section style="background-color: var(--bg-light);">
    ${getForm()}
  </section>
  `
);

// --- PAGE 3: AC Servicing ---
generatePage(
  'ac-servicing.html',
  'Comprehensive AC Servicing & Maintenance | Air Control',
  'Professional AC servicing and deep cleaning to improve efficiency and air quality. Book your service today.',
  'Comprehensive Servicing',
  'AC servicing, AC deep clean, AC maintenance, AC filter cleaning, Air Control service',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; <a href="#">Services</a> &gt; AC Servicing
  </div>
  <section class="hero" style="min-height: 60vh; padding-top: 12rem;">
    <div class="hero-bg" style="background-image: url('https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=2069');"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <span class="hero-subtitle reveal">Preventive Care</span>
      <h1 class="reveal delay-1">Comprehensive Servicing</h1>
      <p class="reveal delay-2">Enhance efficiency, improve indoor air quality, and extend the lifespan of your HVAC systems with our rigorous servicing protocols.</p>
    </div>
  </section>
  <section>
    <div class="grid">
      <div class="premium-card reveal">
        <h3>Deep Chemical Wash</h3>
        <p>Thorough cleaning of evaporator coils, condenser coils, and filters using industry-approved, eco-friendly chemical solutions.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3>Performance Tuning</h3>
        <p>Calibration of thermostats, checking of refrigerant levels, and optimization of airflow for maximum cooling efficiency.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3>Air Quality Enhancement</h3>
        <p>Elimination of mold, bacteria, and dust buildup to ensure the air circulated in your premises is clean and healthy.</p>
      </div>
    </div>
  </section>

  <section style="background-color: var(--surface);">
    <div class="section-header reveal">
      <span class="section-subtitle">Beyond Basic Maintenance</span>
      <h2 class="section-title">Indoor Air Quality & Duct Cleaning</h2>
    </div>
    <div class="grid">
      <div class="premium-card reveal">
        <h3 style="font-size: 1.25rem;">Air Duct Cleaning Services</h3>
        <p>Our comprehensive <strong>air duct cleaning</strong> and <strong>HVAC duct cleaning</strong> services remove allergens and dust. We offer <strong>air ducts cleaning near me</strong> and <strong>AC vent cleaning</strong> to ensure pristine indoor air quality solutions.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3 style="font-size: 1.25rem;">HVAC Air Purifiers</h3>
        <p>We install the <strong>best air purifier for HVAC system</strong> and <strong>whole house air purifier HVAC</strong> setups. Breathe easier with our advanced ventilation system maintenance and repair.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3 style="font-size: 1.25rem;">AC Tune-Up & Maintenance</h3>
        <p>Looking for an <strong>AC tune-up near me</strong>? Our <strong>air conditioning maintenance</strong> includes <strong>AC filter cleaning</strong>, teaching you <strong>how to clean HVAC coils</strong>, and providing <strong>DIY HVAC maintenance tips</strong> to prevent a spike in electricity bills AC.</p>
      </div>
    </div>
  </section>

  <section style="background-color: var(--bg-light);">
    ${getForm()}
  </section>
  `
);

// --- PAGE 4: AC Installation ---
generatePage(
  'ac-installation.html',
  'Professional AC Installation Services | Air Control',
  'Expert installation of split, window, cassette, and central AC systems. Ensure optimal cooling with Air Control.',
  'System Installation',
  'AC installation, split AC installation, VRF installation, central AC setup, Air Control',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; <a href="#">Services</a> &gt; AC Installation
  </div>
  <section class="hero" style="min-height: 60vh; padding-top: 12rem;">
    <div class="hero-bg" style="background-image: url('https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?q=80&w=2070');"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <span class="hero-subtitle reveal">Flawless Execution</span>
      <h1 class="reveal delay-1">System Installation</h1>
      <p class="reveal delay-2">From residential split units to complex commercial VRF systems, we deliver seamless installations engineered for peak performance.</p>
    </div>
  </section>
  <section>
    <div class="grid">
      <div class="premium-card reveal">
        <h3>Site Assessment</h3>
        <p>Comprehensive load calculations and site surveys to recommend the optimal capacity and type of air conditioning system for your space.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3>Commercial VRF & Central</h3>
        <p>Specialized expertise in the design and deployment of large-scale Variable Refrigerant Flow (VRF) and central cooling infrastructures.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3>Aesthetic Integration</h3>
        <p>Meticulous installation practices ensuring minimal disruption and seamless integration with your interior architecture.</p>
      </div>
    </div>
  </section>

  <section style="background-color: var(--surface);">
    <div class="section-header reveal">
      <span class="section-subtitle">Modern Solutions</span>
      <h2 class="section-title">HVAC Installation & Replacement</h2>
    </div>
    <div class="grid">
      <div class="premium-card reveal">
        <h3 style="font-size: 1.25rem;">System Upgrades & Replacement</h3>
        <p>Whether you need an <strong>HVAC replacement</strong>, <strong>boiler replacement</strong>, or <strong>thermostat replacement</strong>, we provide transparent <strong>AC replacement cost</strong> and <strong>new AC unit installation cost</strong> estimates.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3 style="font-size: 1.25rem;">Ductless & Smart Systems</h3>
        <p>We specialize in <strong>ductless heating and cooling</strong>, <strong>ductless mini-split installation</strong>, <strong>smart thermostat installation</strong>, and <strong>smart thermostat setup</strong> for maximum energy efficiency.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3 style="font-size: 1.25rem;">Heating & Cooling Companies</h3>
        <p>As one of the leading <strong>heating and cooling companies</strong>, we handle <strong>central air installation</strong>, <strong>furnace installation cost</strong> assessments, <strong>radiant heating system installation</strong>, and <strong>ductwork installation</strong>.</p>
      </div>
    </div>
  </section>

  <section style="background-color: var(--bg-light);">
    ${getForm()}
  </section>
  `
);

// --- PAGE 5: AC AMC ---
generatePage(
  'ac-amc.html',
  'AC Annual Maintenance Contract (AMC) | Air Control',
  'Secure your cooling systems with our comprehensive Annual Maintenance Contracts. Priority service and regular checkups.',
  'Annual Maintenance (AMC)',
  'AC AMC, AC maintenance contract, commercial AC AMC, Air Control AMC',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; <a href="#">Services</a> &gt; AC AMC
  </div>
  <section class="hero" style="min-height: 60vh; padding-top: 12rem;">
    <div class="hero-bg" style="background-image: url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?q=80&w=2070');"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <span class="hero-subtitle reveal">Uninterrupted Comfort</span>
      <h1 class="reveal delay-1">Annual Maintenance Contracts</h1>
      <p class="reveal delay-2">Protect your investment with our tailored AMC plans. Enjoy priority support, zero labor charges, and proactive system care.</p>
    </div>
  </section>
  <section>
    <div class="grid">
      <div class="premium-card reveal">
        <h3>Priority Support</h3>
        <p>AMC clients receive expedited response times for all service calls, ensuring minimal downtime during peak summer months.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3>Proactive Inspections</h3>
        <p>Scheduled preventive maintenance visits to identify and resolve potential issues before they escalate into costly failures.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3>Cost Efficiency</h3>
        <p>Fixed annual costs with complimentary labor on repairs, providing predictable budgeting for facility management.</p>
      </div>
    </div>
  </section>
  <section style="background-color: var(--bg-light);">
    ${getForm()}
  </section>
  `
);

// --- PAGE 6: Why Us ---
generatePage(
  'why-us.html',
  'Why Choose Air Control | The AC Decision That Protects Everything',
  'Why professional engineering matters in every AC installation. Discover the Air Control standard of safety, precision welding, and 38 years of trust.',
  'Why Professional Engineering Matters',
  'Why Air Control, AC safety, professional AC installation, AC engineering, reliable AC service Delhi',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; Why Us
  </div>
  <section class="hero" style="min-height: 60vh; padding-top: 12rem;">
    <div class="hero-bg" style="background-image: url('https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?q=80&w=2070');"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <span class="hero-subtitle reveal">The Honest Comparison</span>
      <h1 class="reveal delay-1">Why Professional Engineering<br>Matters in Every Installation</h1>
      <p class="reveal delay-2">The AC decision that protects everything you've built. Discover the Air Control standard of safety, precision, and 38 years of trust.</p>
    </div>
  </section>

  <section>
    <div class="section-header reveal">
      <span class="section-subtitle">Safety First</span>
      <h2 class="section-title">Safety Is Not a Feature —<br>It Is Our Foundation</h2>
      <p style="max-width: 600px; margin: 0 auto; color: var(--text-muted);">Why air conditioning must be treated as a critical engineering system, not a commodity service call.</p>
    </div>
    <div class="grid">
      <div class="premium-card reveal">
        <h3 style="font-size: 1.25rem;">Refrigerant Choice Determines Safety</h3>
        <p>The refrigerant inside your AC system is either your greatest protection or your silent threat. Flammable R-32 in untrained hands creates hazards that remain invisible until an incident occurs. We use only certified, non-hazardous refrigerants — no exceptions, no commercial pressure.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3 style="font-size: 1.25rem;">Precision Welding Is Non-Negotiable</h3>
        <p>Every copper pipe joint we create is welded to structural engineering standards — tested, verified, and guaranteed. Improper welding creates micro-leaks that silently degrade your system over months, eventually creating both safety hazards and very expensive failures.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3 style="font-size: 1.25rem;">Systems, Not Appliances</h3>
        <p>An AC installation touches your building's structure, electrical infrastructure, and indoor air quality simultaneously. We design holistically — every component from insulation to fittings is selected for compatibility, safety, and 20-year operational performance.</p>
      </div>
      <div class="premium-card reveal delay-3">
        <h3 style="font-size: 1.25rem;">Long-Term Value Always Prevails</h3>
        <p>"Cheap today" becomes catastrophically expensive tomorrow. Our clients who switched to Air Control after bad experiences consistently tell us the same thing: <em>"The extra investment paid for itself within the first year of zero breakdowns."</em></p>
      </div>
    </div>
  </section>

  <section style="background-color: var(--primary); color: var(--surface); padding: 6rem 5%;">
    <div class="section-header reveal">
      <span class="section-subtitle" style="color: var(--accent);">Our Guarantees</span>
      <h2 class="section-title" style="color: var(--surface);">What We Guarantee<br>on Every Engagement</h2>
    </div>
    <div class="grid">
      <div class="premium-card reveal" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
        <h3 style="color: var(--surface);">Zero Safety Compromise</h3>
        <p style="color: #CBD5E1;">We have never compromised on safety in 38 years. Not once. Not for budget. Not for deadlines.</p>
      </div>
      <div class="premium-card reveal delay-1" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
        <h3 style="color: var(--surface);">2-Hour Emergency Response</h3>
        <p style="color: #CBD5E1;">When critical systems fail, every hour costs you. We guarantee 2-hour response across Delhi NCR.</p>
      </div>
      <div class="premium-card reveal delay-2" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
        <h3 style="color: var(--surface);">Full Accountability</h3>
        <p style="color: #CBD5E1;">Every project comes with complete documentation, warranty, and an ongoing accountability structure.</p>
      </div>
      <div class="premium-card reveal delay-3" style="background: rgba(255,255,255,0.05); border-color: rgba(255,255,255,0.1);">
        <h3 style="color: var(--surface);">Lifetime Partnership</h3>
        <p style="color: #CBD5E1;">We build relationships, not transactions. Our AMC clients average 15+ years of continuous partnership.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="section-header reveal">
      <span class="section-subtitle">Our Legacy</span>
      <h2 class="section-title">38 Years of Building<br>Unbreakable Trust</h2>
      <p style="max-width: 600px; margin: 0 auto; color: var(--text-muted);">Our reputation was built long before shortcuts became common.</p>
    </div>
    <div class="grid">
      <div class="premium-card reveal">
        <h3 style="font-size: 1.25rem;">Consultant-First AC Solutions</h3>
        <p>We don't just install; we consult. From residential air conditioning to commercial & industrial AC systems, we provide expert guidance on split, VRF, VRV & chiller installations, system audits, upgrades, and safety optimization.</p>
      </div>
      <div class="premium-card reveal delay-1">
        <h3 style="font-size: 1.25rem;">Trusted by Institutions That Cannot Afford Risk</h3>
        <p>Our clients include embassies & consulates, logistics & warehousing, high-value retail & jewellers, medical facilities, IT parks & data centers, and corporate offices & premium residences.</p>
      </div>
      <div class="premium-card reveal delay-2">
        <h3 style="font-size: 1.25rem;">AC Services for All Industries</h3>
        <p>We provide specialized AC services for industrial systems, commercial setups, hospital air conditioning, hotel cooling, and data center environments across Delhi NCR.</p>
      </div>
    </div>
  </section>

  <section style="background-color: var(--bg-light);">
    ${getForm()}
  </section>
  `
);

// --- LOCATION PAGES ---
const locations = ['Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Ghaziabad'];
locations.forEach(loc => {
  generatePage(
    `ac-service-${loc.toLowerCase()}.html`,
    `Premium AC Service in ${loc} | Air Control`,
    `Top-rated AC repair, servicing, and installation in ${loc}. Air Control provides expert cooling solutions with 38 years of experience.`,
    `AC Service in ${loc}`,
    `AC service ${loc}, AC repair ${loc}, AC installation ${loc}, Air Control ${loc}`,
    `
    <div class="breadcrumbs">
      <a href="index.html">Home</a> &gt; <a href="#">Areas</a> &gt; ${loc}
    </div>
    <section class="hero" style="min-height: 60vh; padding-top: 12rem;">
      <div class="hero-bg" style="background-image: url('https://images.unsplash.com/photo-1582653291997-079a1c04e5d1?q=80&w=2070');"></div>
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <span class="hero-subtitle reveal">Local Expertise</span>
        <h1 class="reveal delay-1">Premium AC Services in ${loc}</h1>
        <p class="reveal delay-2">Delivering institutional-grade air conditioning repair, installation, and maintenance across ${loc} and surrounding areas.</p>
      </div>
    </section>
    <section>
      <div class="section-header reveal">
        <h2 class="section-title">Why Choose Us in ${loc}?</h2>
      </div>
      <div class="grid">
        <div class="premium-card reveal">
          <h3>Rapid Deployment</h3>
          <p>Our locally stationed technicians in ${loc} ensure swift response times for all emergency repair requests.</p>
        </div>
        <div class="premium-card reveal delay-1">
          <h3>Commercial & Residential</h3>
          <p>Equipped to handle everything from individual split units in homes to massive VRF systems in corporate offices.</p>
        </div>
        <div class="premium-card reveal delay-2">
          <h3>Trusted Heritage</h3>
          <p>Serving the NCR region since 1987, we have built a reputation for uncompromising quality and integrity.</p>
        </div>
      </div>
    </section>
    <section style="background-color: var(--primary); color: var(--surface); padding: 4rem 5%; text-align: center;">
      <div class="reveal">
        <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--accent);">Your Local HVAC Experts</h3>
        <p style="max-width: 800px; margin: 0 auto; color: #CBD5E1; line-height: 1.8;">Looking for an <strong>HVAC contractor in ${loc}</strong> or the <strong>best HVAC contractor in ${loc}</strong>? We are your local experts for <strong>AC repair in ${loc}</strong>, <strong>AC service in ${loc}</strong>, and the <strong>best AC repair service in ${loc}</strong>. We also provide <strong>commercial HVAC repair near me</strong> and <strong>residential HVAC near me</strong> to ensure your environment remains perfectly climate-controlled.</p>
      </div>
    </section>
    <section style="background-color: var(--bg-light);">
      ${getForm()}
    </section>
    `
  );
});

// --- BLOG PAGES ---
generatePage(
  'blog.html',
  'Industry Insights & HVAC Tips | Air Control Blog',
  'Read the latest insights, maintenance tips, and industry news from the climate control experts at Air Control.',
  'Industry Insights',
  'AC tips, HVAC blog, Air Control insights, AC maintenance guide',
  `
  <div class="breadcrumbs">
    <a href="index.html">Home</a> &gt; Insights
  </div>
  <section class="hero" style="min-height: 50vh; padding-top: 10rem;">
    <div class="hero-bg" style="background-image: url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070');"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <span class="hero-subtitle reveal">Knowledge Base</span>
      <h1 class="reveal delay-1">Industry Insights</h1>
      <p class="reveal delay-2">Expert advice, technical guides, and the latest trends in HVAC technology.</p>
    </div>
  </section>
  <section>
    <div class="grid">
      <div class="premium-card reveal">
        <span class="section-subtitle" style="margin-bottom: 0.5rem;">Maintenance</span>
        <h3 style="margin-bottom: 1rem;">Why is My AC Not Cooling?</h3>
        <p>Explore the technical reasons behind cooling failures, from refrigerant leaks to compressor malfunctions.</p>
        <a href="blog/ac-not-cooling.html" class="card-link">Read Article</a>
      </div>
      <div class="premium-card reveal delay-1">
        <span class="section-subtitle" style="margin-bottom: 0.5rem;">Cost Guide</span>
        <h3 style="margin-bottom: 1rem;">AC Gas Filling Costs in Delhi</h3>
        <p>A comprehensive breakdown of refrigerant types and the associated costs for professional recharging.</p>
        <a href="blog/ac-gas-filling-cost-delhi.html" class="card-link">Read Article</a>
      </div>
      <div class="premium-card reveal delay-2">
        <span class="section-subtitle" style="margin-bottom: 0.5rem;">Best Practices</span>
        <h3 style="margin-bottom: 1rem;">Optimal Servicing Frequency</h3>
        <p>How often should institutional and residential systems undergo deep cleaning and maintenance?</p>
        <a href="blog/how-often-ac-service.html" class="card-link">Read Article</a>
      </div>
      <div class="premium-card reveal">
        <span class="section-subtitle" style="margin-bottom: 0.5rem;">Market Guide</span>
        <h3 style="margin-bottom: 1rem;">Cheapest AC Market in Delhi</h3>
        <p>Explore our guide to the used AC market Delhi, old AC market Delhi, second hand AC Delhi, and Delhi AC wholesale market.</p>
        <a href="blog/ac-market-guide-delhi.html" class="card-link">Read Article</a>
      </div>
      <div class="premium-card reveal delay-1">
        <span class="section-subtitle" style="margin-bottom: 0.5rem;">Pricing</span>
        <h3 style="margin-bottom: 1rem;">AC Gas Refill Cost in India 2025</h3>
        <p>A detailed breakdown of the AC gas refill cost in India 2025, signs of a refrigerant leak, and why professional AC servicing matters.</p>
        <a href="blog/ac-gas-refill-cost-2025.html" class="card-link">Read Article</a>
      </div>
      <div class="premium-card reveal delay-2">
        <span class="section-subtitle" style="margin-bottom: 0.5rem;">Installation</span>
        <h3 style="margin-bottom: 1rem;">HVAC for Small Apartments</h3>
        <p>Expert advice on how to choose the best HVAC system for a small apartment, including ductless mini-split installation.</p>
        <a href="blog/choose-hvac-small-apartment.html" class="card-link">Read Article</a>
      </div>
    </div>
  </section>
  `
);

const blogPosts = [
  { slug: 'ac-not-cooling', title: 'Why is My AC Not Cooling?', desc: 'Discover the common reasons why your AC is not cooling and how our experts diagnose the issue.' },
  { slug: 'ac-gas-filling-cost-delhi', title: 'AC Gas Filling Cost in Delhi', desc: 'Understand the costs involved in AC gas filling and why professional service is crucial.' },
  { slug: 'how-often-ac-service', title: 'How Often Should You Service Your AC?', desc: 'Learn about the recommended frequency for AC servicing to maintain optimal performance.' },
  { slug: 'best-ac-for-home', title: 'Best AC for Home: A Buying Guide', desc: 'A comprehensive guide to choosing the right air conditioning system for your residential needs.' },
  { slug: 'ac-amc-worth-it', title: 'Is an AC AMC Worth It?', desc: 'Analyze the cost-benefits of Annual Maintenance Contracts for commercial and residential setups.' },
  { slug: 'ac-market-guide-delhi', title: 'Cheapest AC Market in Delhi: Used & Wholesale Guide', desc: 'Looking for the cheapest AC market Delhi? Explore our guide to the used AC market Delhi, old AC market Delhi, second hand AC Delhi, and Delhi AC wholesale market.' },
  { slug: 'ac-gas-refill-cost-2025', title: 'AC Gas Refill Cost in India 2025', desc: 'A detailed breakdown of the AC gas refill cost in India 2025, signs of a refrigerant leak, and why professional AC servicing matters.' },
  { slug: 'choose-hvac-small-apartment', title: 'How to Choose the Best HVAC System for a Small Apartment', desc: 'Expert advice on how to choose the best HVAC system for a small apartment, including ductless mini-split installation and energy-efficient HVAC installation.' },
  { slug: 'furnace-repair-signs', title: 'Signs Your Furnace Needs Repair', desc: "Don't wait for a breakdown. Learn the signs your furnace needs repair, common HVAC problems, and when to call for emergency furnace repair." }
];

blogPosts.forEach(post => {
  generatePage(
    `blog/${post.slug}.html`,
    `${post.title} | Air Control Insights`,
    post.desc,
    post.title,
    `${post.title.toLowerCase().replace(/ /g, ', ')}, HVAC insights, Air Control`,
    `
    <div class="breadcrumbs">
      <a href="../index.html">Home</a> &gt; <a href="../blog.html">Insights</a> &gt; Article
    </div>
    <section style="padding-top: 8rem; max-width: 800px; margin: 0 auto;">
      <span class="section-subtitle reveal">Technical Guide</span>
      <h1 class="section-title reveal delay-1" style="font-size: 2.5rem; margin-bottom: 2rem;">${post.title}</h1>
      <div class="reveal delay-2" style="font-size: 1.125rem; color: var(--text-main); line-height: 1.8;">
        <p style="margin-bottom: 1.5rem;">${post.desc}</p>
        <p style="margin-bottom: 1.5rem;">At Air Control, we approach every HVAC challenge with institutional-grade precision. Understanding the root cause of climate control issues is the first step toward a lasting solution.</p>
        <h3 style="margin: 2.5rem 0 1rem; color: var(--primary);">Professional Diagnostics</h3>
        <p style="margin-bottom: 1.5rem;">Our certified technicians utilize advanced diagnostic equipment to evaluate system performance, ensuring that every repair or maintenance action is data-driven and highly effective.</p>
        <div style="background: var(--bg-light); padding: 2rem; border-left: 4px solid var(--accent); margin: 3rem 0;">
          <h4 style="margin-bottom: 1rem;">Need Expert Assistance?</h4>
          <p style="margin-bottom: 1.5rem; font-size: 1rem;">Contact our engineering team for a comprehensive evaluation of your HVAC systems.</p>
          <a href="tel:+919312264832" class="btn-premium">Schedule Consultation</a>
        </div>
      </div>
    </section>
    `,
    '../'
  );
});
