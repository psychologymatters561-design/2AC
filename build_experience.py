#!/usr/bin/env python3
"""
Assemble experience.html from plain-text sources in src/.

Kept as three readable files rather than one 42 KB page: each moves
through the contents API in one piece, and CSS/JS stay editable as
CSS and JS rather than escaped inside a Python string.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def build():
    def read(name):
        return open(os.path.join(HERE, "src", name), encoding="utf-8").read()
    shell = read("experience.shell.html")
    return (shell
            .replace("/*__CSS__*/", read("experience.css"), 1)
            .replace("//__JS__\n", read("experience.js"), 1))


if __name__ == "__main__":
    out = build()
    open(os.path.join(HERE, "experience.html"), "w", encoding="utf-8").write(out)
    print("experience.html %.1f KB" % (len(out) / 1024))
