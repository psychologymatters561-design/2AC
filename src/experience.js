'use strict';
(function(){
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- the journey: scroll -> temperature -> everything ---------- */
  var HOT  = [26,14,6],    COLD = [10,22,40];    // ground, rgb
  var HOTA = [240,217,184],COLDA= [214,228,244];  // air, rgb
  function mix(a,b,t){return 'rgb('+
    Math.round(a[0]+(b[0]-a[0])*t)+','+
    Math.round(a[1]+(b[1]-a[1])*t)+','+
    Math.round(a[2]+(b[2]-a[2])*t)+')';}

  var root=document.documentElement, tempEl=document.getElementById('temp'),
      fillEl=document.getElementById('tempFill'), stateEl=document.getElementById('tempState'),
      navEl=document.getElementById('nav');
  var STATES=[[0,'Rooftop'],[.3,'Descending'],[.55,'Entering'],[.78,'Balancing'],[.92,'Engineered']];
  var journey=0, target=0;

  function readScroll(){
    var max=document.documentElement.scrollHeight-innerHeight;
    target = max>0 ? Math.min(1,Math.max(0,scrollY/max)) : 0;
  }

  /* ---------- act one: pinned dolly + line-by-line assembly ---------- */
  var act1=document.getElementById('act1'),
      p1=document.getElementById('p1'),p2=document.getElementById('p2'),p3=document.getElementById('p3'),
      lines=[document.getElementById('l1'),document.getElementById('l2'),document.getElementById('l3')],
      hsub=document.getElementById('hsub'),
      heroCopy=document.querySelector('.hero-copy');

  /* the headline assembles itself on arrival, line by line, then scroll
     takes over and carries it away. Waiting for scroll to show line one
     left the hero blank on load. */
  function assemble(){
    lines.forEach(function(el,i){ setTimeout(function(){ el.classList.add('on'); }, 260+i*190); });
    setTimeout(function(){ hsub.classList.add('on'); }, 1080);
  }
  if(document.readyState==='complete') assemble();
  else addEventListener('load',assemble);

  // base opacity per plane, so haze depth survives the scroll fade
  var BASE=[.5,.85,1];
  function act1Frame(){
    var r=act1.getBoundingClientRect(), h=act1.offsetHeight-innerHeight;
    var p = h>0 ? Math.min(1,Math.max(0,-r.top/h)) : 0;
    // each plane pushes toward the camera at its own rate — a dolly, not a slide
    var pz=[[1.00,.30,.06],[1.10,.60,.13],[1.22,1.05,.24]], el=[p1,p2,p3];
    for(var i=0;i<3;i++){
      var s=pz[i][0]+p*pz[i][1];
      var y=p*innerHeight*pz[i][2];
      el[i].style.transform=
        'translate3d(calc(-50% + '+(varPx*(i+1)*8).toFixed(1)+'px),'+
        (y+varPy*(i+1)*6).toFixed(1)+'px,0) scale('+s.toFixed(4)+')';
      el[i].style.opacity=(BASE[i]*Math.max(0,1-p*1.15)).toFixed(3);
    }
    // the copy lifts away as the camera pushes past it
    heroCopy.style.transform=
      'translate3d('+(varPx*-9).toFixed(1)+'px,'+(varPy*-7 - p*130).toFixed(1)+'px,0)';
    heroCopy.style.opacity=Math.max(0,1-p*1.9).toFixed(3);
  }

  /* ---------- act two: pinned rail pans sideways ---------- */
  var act2=document.getElementById('act2'), rail=document.getElementById('rail');
  function act2Frame(){
    var r=act2.getBoundingClientRect(), h=act2.offsetHeight-innerHeight;
    var p = h>0 ? Math.min(1,Math.max(0,-r.top/h)) : 0;
    var dist=Math.max(0, rail.scrollWidth - innerWidth + 40);
    rail.style.transform='translate3d('+(-dist*p).toFixed(2)+'px,0,0)';
  }

  /* ---------- pointer: moves what is not scrolling ---------- */
  var varPx=0, varPy=0, tx=0, ty=0;
  if(!reduce && matchMedia('(pointer:fine)').matches){
    addEventListener('mousemove',function(e){
      tx=(e.clientX/innerWidth-.5)*2; ty=(e.clientY/innerHeight-.5)*2;
    },{passive:true});
  }

  /* ---------- atmosphere canvas: heat above, cool below ---------- */
  var cv=document.getElementById('sky'), cx=cv.getContext('2d'), W=0,H=0,DPR=1,motes=[];
  function sizeCanvas(){
    DPR=Math.min(devicePixelRatio||1,2);
    W=innerWidth; H=innerHeight;
    cv.width=W*DPR; cv.height=H*DPR; cv.style.width=W+'px'; cv.style.height=H+'px';
    cx.setTransform(DPR,0,0,DPR,0,0);
    var n=Math.round(Math.min(90,W/16));
    motes=[];
    for(var i=0;i<n;i++) motes.push({
      x:Math.random()*W, y:Math.random()*H,
      r:Math.random()*1.9+.35, s:Math.random()*.5+.12,
      d:Math.random()*Math.PI*2, w:Math.random()*.9+.25
    });
  }
  function drawSky(t){
    cx.clearRect(0,0,W,H);
    // heat haze bands at the top of the journey, stillness at the bottom
    var heat=1-t;
    if(heat>.02){
      var bands=7;
      for(var b=0;b<bands;b++){
        var yy=H*(b/bands)+Math.sin(now*.0007+b*1.3)*11*heat;
        var g=cx.createLinearGradient(0,yy,0,yy+H/bands);
        g.addColorStop(0,'rgba(255,168,76,0)');
        g.addColorStop(.5,'rgba(255,152,60,'+(0.045*heat).toFixed(3)+')');
        g.addColorStop(1,'rgba(255,168,76,0)');
        cx.fillStyle=g; cx.fillRect(0,yy,W,H/bands);
      }
    }
    // motes: dust rising in the heat, settling to a slow cool drift
    for(var i=0;i<motes.length;i++){
      var m=motes[i];
      m.d+=0.006;
      m.x+=Math.sin(m.d)*m.w*(0.35+heat*0.9);
      m.y-=m.s*(0.25+heat*1.25);
      if(m.y<-8){m.y=H+8;m.x=Math.random()*W}
      if(m.x<-8)m.x=W+8; if(m.x>W+8)m.x=-8;
      var col = heat>.5 ? '236,170,96' : '176,204,236';
      cx.beginPath(); cx.arc(m.x,m.y,m.r,0,6.2832);
      cx.fillStyle='rgba('+col+','+(0.05+0.16*(heat>.5?heat:1-heat)).toFixed(3)+')';
      cx.fill();
    }
  }

  /* ---------- reveals + counters ---------- */
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){e.target.classList.add('on'); io.unobserve(e.target);} });
  },{threshold:.16,rootMargin:'0px 0px -50px'});
  document.querySelectorAll('.rev,.std').forEach(function(el){io.observe(el)});

  var cio=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(!e.isIntersecting) return;
      cio.unobserve(e.target);
      var to=parseInt(e.target.dataset.to,10), st=performance.now(), dur=1500;
      (function tick(n){
        var p=Math.min((n-st)/dur,1), ease=1-Math.pow(1-p,3);
        e.target.textContent=Math.round(ease*to);
        if(p<1) requestAnimationFrame(tick); else e.target.textContent=to;
      })(st);
    });
  },{threshold:.6});
  document.querySelectorAll('.cnt').forEach(function(el){cio.observe(el)});

  /* ---------- proof marquee (duplicated for a seamless loop) ---------- */
  var PROOF=['🏛 <b>Vatican Embassy</b> · 35 years','📦 <b>DHL Express</b> · VRF across 3 floors',
    '💎 <b>Tanishq</b> · Connaught Place','⭐ <b>4.9 / 5.0</b> · 150+ verified reviews',
    '🛡 <b>Zero</b> safety incidents in 38 years','🏥 Hospitals · Hotels · Data centres',
    '⚡ <b>2-hour</b> emergency response','📋 <b>15+</b> diplomatic missions'];
  var track=document.getElementById('proofTrack'), html='';
  for(var k=0;k<2;k++) for(var q=0;q<PROOF.length;q++)
    html+='<span class="proof-item"'+(k?' aria-hidden="true"':'')+'>'+PROOF[q]+'</span>';
  track.innerHTML=html;

  /* ---------- one loop drives the whole page ---------- */
  var now=0;
  function frame(ts){
    now=ts||0;
    readScroll();
    journey += (target-journey)*0.09;           // eased travel
    varPx += (tx-varPx)*0.06;
    varPy += (ty-varPy)*0.06;

    var t=journey;
    root.style.setProperty('--t',t.toFixed(4));
    root.style.setProperty('--ground',mix(HOT,COLD,t));
    root.style.setProperty('--air',mix(HOTA,COLDA,t));
    root.style.setProperty('--px',varPx.toFixed(4));
    root.style.setProperty('--py',varPy.toFixed(4));

    var deg=Math.round(45-(45-22)*t);
    if(tempEl.textContent!==String(deg)) tempEl.textContent=deg;
    if(innerWidth<=820){ fillEl.style.width=(t*100).toFixed(1)+'%'; fillEl.style.height='auto'; }
    else { fillEl.style.height=(t*100).toFixed(1)+'%'; fillEl.style.width='auto'; }
    var s=STATES[0][1];
    for(var i=0;i<STATES.length;i++) if(t>=STATES[i][0]) s=STATES[i][1];
    if(stateEl.textContent!==s) stateEl.textContent=s;

    navEl.classList.toggle('solid', scrollY>60);

    act1Frame();
    act2Frame();
    if(!reduce) drawSky(t);

    requestAnimationFrame(frame);
  }

  sizeCanvas();
  addEventListener('resize',sizeCanvas,{passive:true});
  readScroll(); journey=target;
  requestAnimationFrame(frame);
})();
