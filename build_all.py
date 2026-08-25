#!/usr/bin/env python3
"""Regenerate every generated page. Run: python3 build_all.py"""
from build import write
from content_repair import ac_repair
from content_servicing import ac_servicing
from content_installation import ac_installation
from content_amc import ac_amc
from content_delhi import delhi
from content_gurgaon import gurgaon
from content_noida import noida
from content_faridabad import faridabad
from content_ghaziabad import ghaziabad

JOBS = [
    ("ac-repair.html",            ac_repair),
    ("ac-servicing.html",         ac_servicing),
    ("ac-installation.html",      ac_installation),
    ("ac-amc.html",               ac_amc),
    ("ac-service-delhi.html",     delhi),
    ("ac-service-gurgaon.html",   gurgaon),
    ("ac-service-noida.html",     noida),
    ("ac-service-faridabad.html", faridabad),
    ("ac-service-ghaziabad.html", ghaziabad),
]

if __name__ == "__main__":
    for slug, fn in JOBS:
        n = write(slug, fn())
        print("  %-30s %6.1f KB" % (slug, n / 1024))
    print("built %d pages" % len(JOBS))
