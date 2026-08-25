#!/usr/bin/env python3
"""Shared layout helpers for the content modules."""
from build import (render, write, lead_form, cross_links, emergency, brand_chips,
                   faq_html, PHONE, PHONE_H, WA)

HOME = ("Home", "index.html")


def sec(cls, inner, container=True):
    body = f'<div class="container">{inner}</div>' if container else inner
    return f'<section class="{cls}">{body}</section>'


def head(label, title, lead=None, center=True):
    c = ' text-center' if center else ''
    r = f'<div class="{ "text-center" if center else "" } reveal">'
    r += f'<span class="section-label text-royal">{label}</span>'
    r += f'<div class="gold-rule{" center" if center else ""}"></div>'
    r += f'<h2 class="headline">{title}</h2>'
    if lead:
        m = 'max-width:640px;margin:16px auto 0;' if center else 'max-width:640px;margin-top:16px;'
        r += f'<p class="lead-text" style="{m}">{lead}</p>'
    return r + '</div>'


def cards(items):
    out = ['<div class="pgrid">']
    for ic, h, p in items:
        out.append(f'<div class="pcard reveal"><div class="pcard-ic">{ic}</div>'
                   f'<h3>{h}</h3><p>{p}</p></div>')
    return "\n".join(out + ['</div>'])


def steps(items):
    out = ['<div class="steps">']
    for i, (h, p) in enumerate(items, 1):
        out.append(f'<div class="step reveal"><div class="step-n">{i}</div>'
                   f'<h3>{h}</h3><p>{p}</p></div>')
    return "\n".join(out + ['</div>'])


def stats_band():
    return """<section class="stats-band"><div class="container"><div class="stats-grid">
  <div class="reveal d1"><div class="stat-num"><span class="counter" data-t="38">0</span><em>+</em></div><div class="stat-label">Years of Service</div></div>
  <div class="reveal d2"><div class="stat-num"><span class="counter" data-t="15">0</span><em>+</em></div><div class="stat-label">Embassies Served</div></div>
  <div class="reveal d3"><div class="stat-num">2<em>hr</em></div><div class="stat-label">Emergency Response</div></div>
  <div class="reveal d4"><div class="stat-num">0</div><div class="stat-label">Safety Incidents</div></div>
</div></div></section>"""
