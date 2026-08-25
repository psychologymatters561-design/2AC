#!/usr/bin/env python3
"""Regenerate every generated page. Run: python3 build_all.py"""
from build import write
import content_services as S
import content_services2 as S2
import content_locations as L

JOBS = [
    ("ac-repair.html",            S.ac_repair),
    ("ac-servicing.html",         S.ac_servicing),
    ("ac-installation.html",      S2.ac_installation),
    ("ac-amc.html",               S2.ac_amc),
    ("ac-service-delhi.html",     L.delhi),
    ("ac-service-gurgaon.html",   L.gurgaon),
    ("ac-service-noida.html",     L.noida),
    ("ac-service-faridabad.html", L.faridabad),
    ("ac-service-ghaziabad.html", L.ghaziabad),
]

if __name__ == "__main__":
    for slug, fn in JOBS:
        n = write(slug, fn())
        print("  %-30s %6.1f KB" % (slug, n / 1024))
    print("built %d pages" % len(JOBS))
