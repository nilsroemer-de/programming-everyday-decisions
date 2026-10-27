"""Erzeugt den QR-Code zum Installation Guide als SVG (lokal, ohne externe Dienste).

Aufruf aus dem Repo-Root:
    uv run --with qrcode python helpers/make_qr.py

Das Ergebnis liegt in images/qr-installation-guide.svg und ist versioniert;
das Skript muss nur laufen, wenn sich die URL des Guides ändert.
"""
import pathlib

import qrcode
import qrcode.image.svg

URL = "https://courses.nilsroemer.com/general/uv.html"
OUT = pathlib.Path(__file__).resolve().parent.parent / "images" / "qr-installation-guide.svg"
INK = "#1e2648"  # Textfarbe aus _brand.yml

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=2)
qr.add_data(URL)
qr.make(fit=True)
img = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
svg = img.to_string(encoding="unicode")
assert svg.count('fill="#000000"') == 1
svg = svg.replace('fill="#000000"', f'fill="{INK}"')
OUT.write_text(svg + "\n")
print(f"{OUT} ({qr.modules_count} x {qr.modules_count} modules)")
