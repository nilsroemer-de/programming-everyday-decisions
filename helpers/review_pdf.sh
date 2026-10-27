#!/bin/zsh
# Review-PDFs der Folien: Druckansicht mit Sprechernotizen auf einer eigenen Seite nach jeder Folie.
# Voraussetzung: _site/ gerendert, chrome-headless-shell installiert (quarto install chrome-headless-shell), Node 22+.
# Aufruf aus dem Projektordner: zsh helpers/review_pdf.sh lec_00 lec_01 ...   (ohne Argument: alle Decks)
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PORT=8766
decks=("$@")
if [ ${#decks} -eq 0 ]; then decks=(lec_00 lec_01 lec_02 lec_03 lec_04 lec_05 lec_06 tut_05_01); fi
python3 -m http.server $PORT --directory "$ROOT/_site" --bind 127.0.0.1 >/dev/null 2>&1 &
SRV=$!
trap "kill $SRV" EXIT
sleep 1
node "$ROOT/helpers/review_pdf.mjs" $PORT "$ROOT/review-pdfs" $decks
