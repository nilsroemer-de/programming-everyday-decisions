#!/usr/bin/env python3
"""Remove the cdnjs.cloudflare.com polyfill <script> that Quarto/Pandoc
injects alongside MathJax. Modern browsers need no ES6 polyfill, and the
site must not trigger any automatic third-party requests (GDPR).

Runs as a Quarto post-render script over the project output directory.
"""

import os
import re
import pathlib

OUT_DIR = pathlib.Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "_site"))
POLYFILL_RE = re.compile(
    r'[ \t]*<script src="https://cdnjs\.cloudflare\.com/polyfill/[^"]*"></script>\n?'
)

changed = 0
for html_file in OUT_DIR.rglob("*.html"):
    text = html_file.read_text(encoding="utf-8")
    if "cdnjs.cloudflare.com/polyfill" in text:
        html_file.write_text(POLYFILL_RE.sub("", text), encoding="utf-8")
        changed += 1

print(f"strip_polyfill: removed polyfill script from {changed} file(s)")
