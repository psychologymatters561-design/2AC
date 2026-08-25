#!/usr/bin/env python3
"""
Air Control site generator.

Builds the service and location pages from a shared premium template so that
design, schema and chrome stay identical across the site. The base CSS is read
straight out of index.html rather than duplicated, so the homepage remains the
single source of truth for the design system.
"""
import re, os, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PHONE_H = "+91 93122 64832"
PHONE = "+919312264832"
WA = "https://wa.me/919312264832"
EMAIL = "ajay@aircontrols.in"
KEY = "0b3287e6-ba3f-4a09-93ed-2212b40ea680"
SITE = "https://aircontrols.in"
TODAY = "2026-08-25"

BRANDS = ["Daikin","Blue Star","Voltas","LG","Samsung","Hitachi","Carrier","O General",
          "Mitsubishi","Panasonic","Godrej","Lloyd","Whirlpool","Haier","Toshiba","Sanyo"]


def base_css():
    """Pull the design-system CSS out of index.html so it never drifts."""
    h = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    m = re.search(r"<style>(.*?)</style>", h, re.S)
    if not m:
        raise SystemExit("could not find <style> block in index.html")
    return m.group(1)


PAGE_CSS = """
/* ===== PAGE CHROME ===== */
.page-hero{position:relative;padding:150px 0 72px;overflow:hidden;
  background:linear-gradient(160deg,#081524,var(--navy) 45%,var(--navy-3))}
.page-hero .hero-grid{opacity:.45}
.page-hero-inner{position:relative;z-index:3;max-width:860px}
.page-hero h1{color:#fff;margin:16px 0 18px}
.page-hero p{color:rgba(255,255,255,.66);font-size:clamp(1rem,1.5vw,1.13rem);line-height:1.75;max-width:680px}
.page-hero .hero-actions{margin-top:30px;margin-bottom:0}

/* breadcrumbs */
.crumbs{display:flex;flex-wrap:wrap;gap:7px;align-items:center;font-size:12.5px;
  color:rgba(255,255,255,.5);position:relative;z-index:3}
.crumbs a{color:rgba(255,255,255,.66);transition:color .3s var(--ease)}
.crumbs a:hover{color:var(--gold)}
.crumbs span[aria-current]{color:var(--gold)}
.crumb-sep{opacity:.4}

/* prose */
.prose h2{font-size:clamp(1.55rem,3vw,2.1rem);margin:0 0 16px}
.prose h3{font-size:clamp(1.12rem,1.9vw,1.32rem);margin:28px 0 9px;color:var(--ink)}
.prose p{color:var(--muted);line-height:1.8;margin-bottom:15px}
.prose ul{margin:0 0 18px}
.prose ul li{color:var(--muted);line-height:1.8;padding-left:26px;position:relative;margin-bottom:8px}
.prose ul li::before{content:'';position:absolute;left:6px;top:12px;width:6px;height:6px;
  border-radius:50%;background:var(--gold)}
.prose strong{color:var(--ink);font-weight:600}

/* problem / feature grid */
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(268px,1fr));gap:20px;margin-top:36px}
.pcard{background:#fff;border:1px solid rgba(15,28,46,.08);border-radius:var(--r-lg);padding:26px 24px;
  transition:all .45s var(--ease)}
.pcard:hover{transform:translateY(-6px);box-shadow:var(--sh-lg);border-color:rgba(200,168,110,.3)}
.pcard-ic{width:44px;height:44px;border-radius:12px;display:grid;place-items:center;font-size:19px;
  margin-bottom:14px;background:linear-gradient(140deg,rgba(200,168,110,.17),rgba(30,77,183,.08));
  border:1px solid rgba(200,168,110,.22)}
.pcard h3{font-size:17.5px;margin:0 0 8px}
.pcard p{font-size:13.8px;color:var(--muted);line-height:1.7;margin:0}

/* numbered process */
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:22px;margin-top:40px}
.step{position:relative;background:#fff;border:1px solid rgba(15,28,46,.08);border-radius:var(--r-lg);
  padding:30px 24px 24px;transition:all .45s var(--ease)}
.step:hover{transform:translateY(-6px);box-shadow:var(--sh-lg);border-color:rgba(200,168,110,.3)}
.step-n{position:absolute;top:-16px;left:24px;width:38px;height:38px;border-radius:11px;
  display:grid;place-items:center;font-family:'Playfair Display',serif;font-weight:700;font-size:17px;
  color:#12203a;background:linear-gradient(135deg,var(--gold-lt),var(--gold));
  box-shadow:0 6px 18px rgba(200,168,110,.4)}
.step h3{font-size:17px;margin:12px 0 8px}
.step p{font-size:13.6px;color:var(--muted);line-height:1.7;margin:0}

/* chips */
.chips{display:flex;flex-wrap:wrap;gap:9px;margin-top:26px}
.chip{padding:9px 17px;border-radius:100px;background:#fff;border:1px solid rgba(15,28,46,.1);
  font-size:13.2px;font-weight:600;color:var(--ink);transition:all .35s var(--ease)}
.chip:hover{border-color:var(--gold);background:rgba(200,168,110,.09);transform:translateY(-2px)}
.section-dark .chip{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.82)}
.section-dark .chip:hover{background:rgba(200,168,110,.16);border-color:var(--gold);color:#fff}

/* zones (location pages) */
.zone{background:#fff;border:1px solid rgba(15,28,46,.08);border-radius:var(--r-lg);
  padding:30px 28px;margin-bottom:22px;transition:all .45s var(--ease)}
.zone:hover{box-shadow:var(--sh);border-color:rgba(200,168,110,.28)}
.zone h3{font-size:19.5px;margin:0 0 10px;display:flex;align-items:center;gap:10px}
.zone h3 .zbadge{font-family:'DM Sans',sans-serif;font-size:10.5px;font-weight:700;letter-spacing:.1em;
  text-transform:uppercase;color:var(--gold-dk);background:rgba(200,168,110,.14);
  padding:4px 10px;border-radius:100px}
.zone p{font-size:14.2px;color:var(--muted);line-height:1.78;margin-bottom:14px}
.zlist{display:flex;flex-wrap:wrap;gap:7px}
.zlist span{font-size:12.2px;color:var(--muted);background:#f5f7fa;border:1px solid rgba(15,28,46,.06);
  padding:5px 11px;border-radius:100px}

/* AMC tiers */
.tiers{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:44px}
.tier{background:#fff;border:1.5px solid rgba(15,28,46,.09);border-radius:var(--r-xl);padding:34px 28px;
  display:flex;flex-direction:column;position:relative;transition:all .45s var(--ease)}
.tier:hover{transform:translateY(-8px);box-shadow:var(--sh-lg)}
.tier.featured{border-color:var(--gold);box-shadow:0 20px 56px rgba(200,168,110,.22)}
.tier-flag{position:absolute;top:-13px;left:50%;transform:translateX(-50%);font-size:10.5px;
  font-weight:700;letter-spacing:.13em;text-transform:uppercase;color:#12203a;
  background:linear-gradient(135deg,var(--gold-lt),var(--gold));padding:6px 16px;border-radius:100px;
  white-space:nowrap;box-shadow:0 6px 18px rgba(200,168,110,.4)}
.tier h3{font-size:22px;margin:0 0 6px}
.tier-sub{font-size:13px;color:var(--gold-dk);font-weight:600;margin-bottom:18px}
.tier ul{margin:0 0 24px;flex:1}
.tier ul li{font-size:13.6px;color:var(--muted);line-height:1.65;padding-left:25px;position:relative;margin-bottom:10px}
.tier ul li::before{content:'✓';position:absolute;left:0;top:0;color:var(--gold);font-weight:700}

/* comparison table */
.tbl-wrap{overflow-x:auto;margin-top:38px;border-radius:var(--r-lg);border:1px solid rgba(15,28,46,.09);background:#fff}
table.cmp{width:100%;border-collapse:collapse;min-width:520px}
table.cmp th,table.cmp td{padding:15px 18px;text-align:left;font-size:14px;
  border-bottom:1px solid rgba(15,28,46,.07)}
table.cmp thead th{background:var(--navy);color:#fff;font-family:'DM Sans',sans-serif;
  font-weight:600;font-size:13px;letter-spacing:.04em}
table.cmp thead th:last-child{background:linear-gradient(135deg,var(--gold-dk),var(--gold));color:#12203a}
table.cmp td{color:var(--muted)}
table.cmp td:first-child{color:var(--ink);font-weight:600}
table.cmp tbody tr:last-child td{border-bottom:none}
table.cmp tbody tr:hover td{background:rgba(200,168,110,.05)}

/* FAQ */
.faq{max-width:840px;margin:40px auto 0}
.faq-item{background:#fff;border:1px solid rgba(15,28,46,.09);border-radius:var(--r);margin-bottom:12px;
  overflow:hidden;transition:all .4s var(--ease)}
.faq-item[open]{border-color:rgba(200,168,110,.4);box-shadow:var(--sh)}
.faq-item summary{padding:19px 54px 19px 22px;font-weight:600;font-size:15.3px;cursor:pointer;
  position:relative;list-style:none;color:var(--ink);line-height:1.5}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item summary::after{content:'+';position:absolute;right:22px;top:50%;transform:translateY(-50%);
  font-size:21px;color:var(--gold);font-weight:400;transition:transform .35s var(--ease)}
.faq-item[open] summary::after{transform:translateY(-50%) rotate(45deg)}
.faq-item summary:hover{color:var(--gold-dk)}
.faq-body{padding:0 22px 20px;font-size:14.2px;color:var(--muted);line-height:1.8}

/* cross links */
.xgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:18px;margin-top:36px}
.xcard{background:#fff;border:1px solid rgba(15,28,46,.08);border-radius:var(--r);padding:22px 20px;
  transition:all .4s var(--ease)}
.xcard:hover{transform:translateY(-5px);box-shadow:var(--sh);border-color:rgba(200,168,110,.32)}
.xcard h4{font-family:'Playfair Display',serif;font-size:16.5px;margin:0 0 6px;color:var(--ink)}
.xcard p{font-size:12.8px;color:var(--muted);line-height:1.6;margin:0 0 10px}
.xcard span{font-size:12px;font-weight:700;color:var(--gold-dk)}

/* emergency banner */
.emerg{background:linear-gradient(135deg,#7f1d1d,#b91c1c);border-radius:var(--r-lg);
  padding:26px 30px;display:flex;align-items:center;justify-content:space-between;gap:20px;
  flex-wrap:wrap;margin-top:40px}
.emerg-t{color:#fff;font-family:'Playfair Display',serif;font-size:21px;font-weight:600;line-height:1.3}
.emerg-s{color:rgba(255,255,255,.78);font-size:13.5px;margin-top:5px}

/* lead form block */
.leadwrap{max-width:760px;margin:0 auto;background:#fff;border-radius:var(--r-xl);
  padding:clamp(28px,4vw,44px);box-shadow:var(--sh-lg);border:1px solid rgba(15,28,46,.07)}
.leadwrap h2{font-size:clamp(1.5rem,2.7vw,2rem);margin-bottom:8px}
.leadwrap>p{color:var(--muted);font-size:14.5px;margin-bottom:26px}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-bottom:14px}
.fld label{display:block;font-size:12.5px;font-weight:600;color:var(--ink);margin-bottom:6px}
.fld input,.fld select,.fld textarea{width:100%;border:1.5px solid #e4e9f0;border-radius:11px;
  padding:12px 14px;font-size:14px;background:#f8f9fb;outline:none;transition:all .3s var(--ease);
  font-family:inherit}
.fld input:focus,.fld select:focus,.fld textarea:focus{border-color:var(--gold);background:#fff;
  box-shadow:0 0 0 3px rgba(200,168,110,.13)}
.fld textarea{resize:vertical;min-height:96px}
.fld select{appearance:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%2367768f' stroke-width='1.6' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
  background-repeat:no-repeat;background-position:right 14px center;background-size:11px}
@media(max-width:620px){.frow{grid-template-columns:1fr}}
"""


# ---------------------------------------------------------------- chrome ----
def nav(depth=0):
    p = "../" * depth
    return f"""<nav id="mainNav">
  <a class="nav-logo" href="{p}index.html">
    <img src="{p}logo.png" alt="Air Control — AC repair and service company in Delhi NCR since 1987" class="nav-logo-img" width="52" height="52" onerror="this.onerror=null;this.src='{p}logo.svg'">
    <div><div class="nav-brand-name">Air Control</div><div class="nav-brand-sub">Est. 1987 · 38 Years</div></div>
  </a>
  <ul class="nav-links-list">
    <li><a href="{p}index.html">Home</a></li>
    <li><a href="{p}why-us.html">Why Us</a></li>
    <li class="nav-drop"><a>Services <span class="caret">▼</span></a>
      <div class="drop-menu">
        <a href="{p}ac-repair.html">AC Repair</a>
        <a href="{p}ac-servicing.html">AC Servicing</a>
        <a href="{p}ac-installation.html">AC Installation</a>
        <a href="{p}ac-amc.html">AC AMC</a>
      </div></li>
    <li class="nav-drop"><a>Areas <span class="caret">▼</span></a>
      <div class="drop-menu">
        <a href="{p}ac-service-delhi.html">Delhi</a>
        <a href="{p}ac-service-gurgaon.html">Gurgaon</a>
        <a href="{p}ac-service-noida.html">Noida</a>
        <a href="{p}ac-service-faridabad.html">Faridabad</a>
        <a href="{p}ac-service-ghaziabad.html">Ghaziabad</a>
      </div></li>
    <li><a href="{p}blog.html">Insights</a></li>
  </ul>
  <a class="nav-cta-btn" href="tel:{PHONE}">📞 {PHONE_H}</a>
  <div class="hamburger" id="hamburger" onclick="toggleMobileNav()"><span></span><span></span><span></span></div>
</nav>
<div class="mobile-nav" id="mobileNav">
  <a href="{p}index.html">Home</a>
  <a href="{p}why-us.html">Why Us</a>
  <div class="mn-label">Services</div>
  <a href="{p}ac-repair.html">AC Repair</a>
  <a href="{p}ac-servicing.html">AC Servicing</a>
  <a href="{p}ac-installation.html">AC Installation</a>
  <a href="{p}ac-amc.html">AC AMC</a>
  <div class="mn-label">Service Areas</div>
  <a href="{p}ac-service-delhi.html">Delhi</a>
  <a href="{p}ac-service-gurgaon.html">Gurgaon</a>
  <a href="{p}ac-service-noida.html">Noida</a>
  <a href="{p}ac-service-faridabad.html">Faridabad</a>
  <a href="{p}ac-service-ghaziabad.html">Ghaziabad</a>
  <div class="mn-label">More</div>
  <a href="{p}blog.html">Insights &amp; Guides</a>
  <a href="tel:{PHONE}" style="color:var(--gold);font-weight:700;">📞 Call {PHONE_H}</a>
</div>"""


def footer(depth=0):
    p = "../" * depth
    return f"""<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="footer-logo">
          <img src="{p}logo.png" alt="Air Control logo" class="footer-logo-img" loading="lazy" width="52" height="52" onerror="this.onerror=null;this.src='{p}logo.svg'">
          <div><div class="nav-brand-name">Air Control</div><div class="nav-brand-sub">Est. 1987 · 38 Years</div></div>
        </div>
        <p>Delhi NCR's most trusted air conditioning company. Serving embassies, global brands and premium establishments with engineering-grade AC solutions since 1987.</p>
      </div>
      <div class="footer-col"><h4>Services</h4><ul>
        <li><a href="{p}ac-repair.html">AC Repair</a></li>
        <li><a href="{p}ac-servicing.html">AC Servicing</a></li>
        <li><a href="{p}ac-installation.html">AC Installation</a></li>
        <li><a href="{p}ac-amc.html">AC AMC</a></li>
        <li><a href="{p}why-us.html">Why Air Control</a></li>
      </ul></div>
      <div class="footer-col"><h4>Service Areas</h4><ul>
        <li><a href="{p}ac-service-delhi.html">AC Service Delhi</a></li>
        <li><a href="{p}ac-service-gurgaon.html">AC Service Gurgaon</a></li>
        <li><a href="{p}ac-service-noida.html">AC Service Noida</a></li>
        <li><a href="{p}ac-service-faridabad.html">AC Service Faridabad</a></li>
        <li><a href="{p}ac-service-ghaziabad.html">AC Service Ghaziabad</a></li>
        <li><a href="{p}blog.html">Insights &amp; Guides</a></li>
      </ul></div>
      <div class="footer-col"><h4>Contact</h4>
        <div class="footer-contact-item">📞 <a href="tel:{PHONE}">{PHONE_H}</a></div>
        <div class="footer-contact-item">✉ <a href="mailto:{EMAIL}">{EMAIL}</a></div>
        <div class="footer-contact-item">💬 <a href="{WA}" target="_blank" rel="noopener">WhatsApp Chat</a></div>
        <div class="footer-contact-item">📍 <span>Ground Floor, 209, Sant Nagar,<br>East of Kailash, New Delhi 110065</span></div>
        <div style="margin-top:16px;"><button class="btn btn-gold btn-sm" onclick="openChat()">Talk to an Expert →</button></div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2025 Air Control. All rights reserved. Trusted since 1987.</span>
      <span>38+ Years · 15+ Embassies · 4.9/5.0 Rating</span>
    </div>
  </div>
</footer>
<div class="mobile-bar">
  <a class="mb-call" href="tel:{PHONE}">📞 Call Now</a>
  <a class="mb-wa" href="{WA}" target="_blank" rel="noopener">💬 WhatsApp</a>
</div>"""


def chatbot(depth=0):
    p = "../" * depth
    return f"""<button class="chat-fab" id="chatFab" onclick="openChat()" aria-label="Chat with our AC expert">💬<span class="chat-badge">1</span></button>
<div class="chat-window" id="chatWindow" role="dialog" aria-label="Chat with Air Control">
  <div class="chat-header">
    <img src="{p}logo.png" alt="Air Control" class="chat-avatar" width="42" height="42" onerror="this.onerror=null;this.src='{p}logo.svg'">
    <div><div class="chat-agent-name">Arjun — AC Expert</div>
      <div class="chat-agent-status"><span class="status-dot"></span>Online · Replies instantly</div></div>
    <button class="chat-close" onclick="closeChat()" aria-label="Close chat">✕</button>
  </div>
  <div class="chat-prog-wrap"><div class="chat-prog" id="chatProg"></div></div>
  <div class="chat-saved" id="chatSaved">✓ Saved — our engineer will call you shortly</div>
  <div class="chat-msgs" id="chatMsgs"></div>
  <div class="chat-qr" id="chatQR"></div>
  <div class="chat-input-row" id="chatInputRow">
    <input class="chat-input" id="chatInput" placeholder="Type your answer..." aria-label="Your message"
      onkeypress="if(event.key==='Enter')sendChat()">
    <button class="chat-send" onclick="sendChat()" aria-label="Send"><svg viewBox="0 0 24 24"><path d="M2 21l21-9L2 3v7l15 2-15 2v7z"/></svg></button>
  </div>
</div>"""


def scripts():
    """Shared JS — same behaviour as index.html."""
    return """<script>
'use strict';
var CFG={key:'%s',phone:'%s'};
function toggleMobileNav(){
  document.getElementById('mobileNav').classList.toggle('open');
  document.getElementById('hamburger').classList.toggle('open');
}
addEventListener('scroll',function(){
  document.getElementById('mainNav').classList.toggle('scrolled',scrollY>60);
},{passive:true});
var io=new IntersectionObserver(function(es){
  es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);}});
},{threshold:.12,rootMargin:'0px 0px -40px'});
document.querySelectorAll('.reveal,.reveal-l,.reveal-r,.reveal-s').forEach(function(el){io.observe(el);});
var cio=new IntersectionObserver(function(es){
  es.forEach(function(e){
    if(!e.isIntersecting)return;
    cio.unobserve(e.target);
    var t=parseInt(e.target.dataset.t,10),d=1700,s=performance.now();
    (function tick(now){
      var p=Math.min((now-s)/d,1),ease=1-Math.pow(1-p,3);
      e.target.textContent=Math.round(ease*t);
      if(p<1)requestAnimationFrame(tick);else e.target.textContent=t;
    })(s);
  });
},{threshold:.5});
document.querySelectorAll('.counter').forEach(function(el){cio.observe(el);});
var FLOW=[
 {q:"Hi! I'm Arjun from Air Control \\ud83d\\udc4b We've been keeping Delhi cool since 1987. What can we help you with today?",
  opts:["AC not cooling","Need AC servicing","New AC installation","AMC / Maintenance","Emergency \\u2014 urgent!"],key:'need'},
 {q:"Got it. Which type of AC is it?",opts:["Split AC","Window AC","Cassette AC","Central / VRF","Not sure"],key:'acType'},
 {q:"Perfect. What's your name?",input:true,key:'name'},
 {q:"Thanks! What's the best number to reach you on?",input:true,key:'phone',tel:true},
 {q:"And which area are you in?",input:true,key:'location'}
];
var step=0,data={},sent=false;
function el(id){return document.getElementById(id);}
function msgs(){return el('chatMsgs');}
function openChat(){
  var w=el('chatWindow');
  if(w.classList.contains('open'))return;
  w.classList.add('open');el('chatFab').classList.add('hidden');
  if(step===0&&!msgs().children.length)setTimeout(ask,420);
}
function closeChat(){
  el('chatWindow').classList.remove('open');el('chatFab').classList.remove('hidden');
}
function bubble(t,who){
  var d=document.createElement('div');
  d.className='chat-msg chat-msg-'+who;d.textContent=t;
  msgs().appendChild(d);msgs().scrollTop=msgs().scrollHeight;
}
function typing(on){
  var ex=el('acTw');
  if(on){ if(ex)return;
    var d=document.createElement('div');
    d.className='chat-typing';d.id='acTw';
    d.innerHTML='<span></span><span></span><span></span>';
    msgs().appendChild(d);msgs().scrollTop=msgs().scrollHeight;
  } else if(ex) ex.remove();
}
function setQR(opts){
  var b=el('chatQR');b.innerHTML='';
  (opts||[]).forEach(function(o){
    var x=document.createElement('button');
    x.className='chat-qr-btn';x.textContent=o;
    x.onclick=function(){answer(o);};
    b.appendChild(x);
  });
}
function ask(){
  var s=FLOW[step];
  if(!s)return finish();
  el('chatProg').style.width=(step/FLOW.length*100)+'%%';
  typing(true);
  setTimeout(function(){
    typing(false);bubble(s.q,'bot');setQR(s.opts);
    el('chatInputRow').style.display=s.input?'flex':'none';
    if(s.input)setTimeout(function(){el('chatInput').focus();},120);
  },680);
}
function answer(v){
  v=(v||'').trim();if(!v)return;
  var s=FLOW[step];
  if(s.tel&&v.replace(/\\D/g,'').length<10){
    bubble(v,'user');typing(true);
    setTimeout(function(){typing(false);
      bubble("That number looks a bit short \\u2014 could you share a 10-digit mobile number?",'bot');},600);
    return;
  }
  bubble(v,'user');data[s.key]=v;setQR([]);el('chatInput').value='';step++;
  if(s.key==='phone')push(false);
  ask();
}
function sendChat(){answer(el('chatInput').value);}
function finish(){
  el('chatProg').style.width='100%%';el('chatInputRow').style.display='none';
  typing(true);
  setTimeout(function(){
    typing(false);
    bubble("Thank you, "+(data.name||'')+"! \\u2705 Our senior engineer will call you within 2 hours. For anything urgent, call us directly on %s.",'bot');
    el('chatSaved').classList.add('show');
    setQR(["\\ud83d\\udcde Call now","\\ud83d\\udcac WhatsApp"]);
    var bs=document.querySelectorAll('#chatQR .chat-qr-btn');
    for(var i=0;i<bs.length;i++){
      bs[i].onclick=(function(b){return function(){
        location.href=b.textContent.indexOf('Call')>-1?'tel:'+CFG.phone:'%s';
      };})(bs[i]);
    }
    push(true);
  },700);
}
function push(complete){
  if(sent&&!complete)return;
  if(complete)sent=true;
  if(!data.phone)return;
  fetch('https://api.web3forms.com/submit',{
    method:'POST',
    headers:{'Content-Type':'application/json',Accept:'application/json'},
    body:JSON.stringify({
      access_key:CFG.key,
      subject:(complete?'New Chatbot Lead (Complete)':'New Chatbot Lead (Partial)')+' \\u2014 Air Control',
      from_name:'aircontrols.in chatbot',
      page:location.pathname,
      name:data.name||'Not provided',
      phone:data.phone||'',
      requirement:data.need||'',
      ac_type:data.acType||'',
      location:data.location||'',
      status:complete?'Complete':'Partial \\u2014 user dropped off'
    })
  })['catch'](function(){});
}
</script>""" % (KEY, PHONE, PHONE_H, WA)


# ---------------------------------------------------------------- blocks ----
def crumbs_html(trail, depth=0):
    p = "../" * depth
    out = []
    for i, (label, href) in enumerate(trail):
        if href and i < len(trail) - 1:
            out.append(f'<a href="{p}{href}">{label}</a>')
        else:
            out.append(f'<span aria-current="page">{label}</span>')
        if i < len(trail) - 1:
            out.append('<span class="crumb-sep">›</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + "".join(out) + "</nav>"


def crumb_schema(trail):
    items = []
    for i, (label, href) in enumerate(trail):
        item = {"@type": "ListItem", "position": i + 1, "name": label}
        if href is not None:
            item["item"] = SITE + "/" + ("" if href == "index.html" else href)
        items.append(item)
    return {"@type": "BreadcrumbList", "itemListElement": items}


def faq_html(faqs):
    out = ['<div class="faq">']
    for q, a in faqs:
        out.append(f'<details class="faq-item reveal"><summary>{q}</summary>'
                   f'<div class="faq-body">{a}</div></details>')
    out.append("</div>")
    return "\n".join(out)


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": re.sub(r"<[^>]+>", "", q),
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in faqs]}


def local_business(name, desc, area=None):
    d = {
        "@type": "LocalBusiness",
        "@id": SITE + "/#business",
        "name": "Air Control",
        "description": desc,
        "url": SITE,
        "logo": SITE + "/logo.png",
        "image": SITE + "/logo.png",
        "telephone": PHONE,
        "email": EMAIL,
        "foundingDate": "1987",
        "priceRange": "₹₹",
        "address": {"@type": "PostalAddress",
                    "streetAddress": "Ground Floor, 209, Sant Nagar, East of Kailash",
                    "addressLocality": "New Delhi", "addressRegion": "Delhi",
                    "postalCode": "110065", "addressCountry": "IN"},
        "geo": {"@type": "GeoCoordinates", "latitude": "28.5530", "longitude": "77.2436"},
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "opens": "08:00", "closes": "20:00"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9",
                            "reviewCount": "150", "bestRating": "5", "worstRating": "1"},
    }
    if area:
        d["areaServed"] = [{"@type": "City", "name": a} for a in area]
    return d


def lead_form(title, sub, subject, extra_fields=""):
    return f"""<div class="leadwrap reveal">
  <h2>{title}</h2>
  <p>{sub}</p>
  <form action="https://api.web3forms.com/submit" method="POST">
    <input type="hidden" name="access_key" value="{KEY}">
    <input type="hidden" name="subject" value="{subject}">
    <input type="hidden" name="from_name" value="aircontrols.in">
    <div class="frow">
      <div class="fld"><label>Full Name *</label><input type="text" name="name" placeholder="e.g. Rajesh Sharma" required></div>
      <div class="fld"><label>Phone Number *</label><input type="tel" name="phone" placeholder="+91 98XXX XXXXX" required></div>
    </div>
    <div class="frow">
      <div class="fld"><label>Email Address</label><input type="email" name="email" placeholder="you@example.com"></div>
      <div class="fld"><label>Your Area / Locality *</label><input type="text" name="location" placeholder="e.g. Greater Kailash" required></div>
    </div>
    {extra_fields}
    <div class="fld" style="margin-bottom:18px;"><label>Tell us what's happening</label>
      <textarea name="message" placeholder="Describe the problem or what you need — the more detail, the better we can prepare."></textarea></div>
    <button type="submit" class="btn btn-gold btn-lg" style="width:100%;">Request Free Assessment <span class="arrow-icon">→</span></button>
    <p style="font-size:12px;color:var(--muted);text-align:center;margin-top:14px;">🔒 Your details stay with our engineers. We respond within 2 hours.</p>
  </form>
</div>"""


def cross_links(cards, depth=0):
    p = "../" * depth
    out = ['<div class="xgrid">']
    for href, h4, txt in cards:
        out.append(f'<a class="xcard reveal" href="{p}{href}"><h4>{h4}</h4><p>{txt}</p>'
                   f'<span>Read more →</span></a>')
    out.append("</div>")
    return "\n".join(out)


def emergency():
    return f"""<div class="emerg reveal">
  <div><div class="emerg-t">AC Emergency? We answer the phone.</div>
    <div class="emerg-s">2-hour response across Delhi NCR — 7 days a week.</div></div>
  <div style="display:flex;gap:11px;flex-wrap:wrap;">
    <a class="btn btn-gold" href="tel:{PHONE}">📞 Call Now</a>
    <a class="btn btn-navy" href="{WA}" target="_blank" rel="noopener">💬 WhatsApp</a>
  </div>
</div>"""


def brand_chips():
    return '<div class="chips">' + "".join(f'<span class="chip">{b}</span>' for b in BRANDS) + "</div>"


# ---------------------------------------------------------------- render ----
def render(slug, title, desc, h1, hero_sub, trail, body, faqs=None,
           extra_schema=None, depth=0, area=None):
    p = "../" * depth
    graph = [local_business("Air Control", desc, area), crumb_schema(trail)]
    if faqs:
        graph.append(faq_schema(faqs))
    if extra_schema:
        graph.extend(extra_schema)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph},
                    ensure_ascii=False, indent=2)
    canonical = f"{SITE}/{slug}"
    css = base_css() + PAGE_CSS
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/logo.png">
<meta property="og:site_name" content="Air Control">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title, quote=True)}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/logo.png">
<meta name="theme-color" content="#0a1628">
<link rel="icon" href="{p}logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&display=swap" rel="stylesheet">
<script type="application/ld+json">
{ld}
</script>
<style>{css}</style>
</head>
<body>
{nav(depth)}
<section class="page-hero">
  <div class="orb orb1"></div><div class="orb orb2"></div><div class="hero-grid"></div>
  <div class="container">
    <div class="page-hero-inner">
      {crumbs_html(trail, depth)}
      <h1 class="display reveal">{h1}</h1>
      <p class="reveal d1">{hero_sub}</p>
      <div class="hero-actions reveal d2">
        <a class="btn btn-gold btn-lg" href="tel:{PHONE}">📞 Call {PHONE_H}</a>
        <a class="btn btn-navy btn-lg" href="{WA}" target="_blank" rel="noopener">💬 WhatsApp Us</a>
      </div>
    </div>
  </div>
</section>
{body}
{footer(depth)}
{chatbot(depth)}
{scripts()}
</body>
</html>"""


def write(slug, content):
    path = os.path.join(ROOT, slug)
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) != ROOT else None
    open(path, "w", encoding="utf-8").write(content)
    return len(content)
