# CLAUDE.md

Anleitung für Claude Code (claude.ai/code) beim Arbeiten in diesem Repository.

## Projektkontext

Kurs-Website für „Programming: Everyday Decision-Making Algorithms" an der Kühne Logistics University (KLU), Hamburg, unter `https://courses.nilsroemer.com`. Der Kurs vermittelt algorithmisches Denken nach dem Buch „Algorithms to Live By" (Optimal Stopping, Explore/Exploit, Caching, Scheduling, Randomness, Computational Kindness) und führt Business-Studierende nebenbei in Python ein. Die Website enthält Vorlesungsfolien, interaktive Tutorials und Kursinformationen (Syllabus, FAQ, Installation, Literatur, Cheatsheet). Die Seiteninhalte sind auf Englisch, die Kommunikation im Repo (Commits, diese Datei) auf Deutsch.

Lehrender und Betreiber ist Dr. Nils Roemer. Dr. Tobias Vlćek hat die Materialien mitentwickelt und wird **nur in den Credits** genannt: auf der Startseite (Author-Zeile und Hinweis im Einleitungstext) und im CC-BY-NC-SA-Footer („Nils Roemer and Tobias Vlćek"). In Lectures und Tutorials steht ausschließlich Nils Roemer als Lecturer, einheitlich über `lectures/_metadata.yml` und `tutorials/_metadata.yml`: `author: "Dr. Nils Roemer, External Lecturer"`, `institute: "Planningio GmbH"` (erscheint als „Lecturer" und „Affiliation" im Titelblock und auf der Titelfolie). Keine `author:`- oder `institute:`-Angaben in einzelnen Dateien. Der Folien-Footer nennt nur „Dr. Nils Roemer".

Der Name wird immer **„Roemer"** geschrieben, nie „Römer", auch in Alt-Texten, Metadaten und Dateinamen.

## Infrastruktur

- **Hosting:** GitHub Pages aus dem Branch `gh-pages` des Repos `github.com/nilsroemer-de/programming-everyday-decisions` (Remote `origin`, SSH).
- **Branches:** `main` enthält ausschließlich die Quelldateien. `gh-pages` enthält nur den gebauten Output und wird allein von `quarto publish gh-pages` geschrieben, nie manuell.
- **Domain:** `courses.nilsroemer.com` ist eine Subdomain von `nilsroemer.com` (bei Strato registriert, dient nur als DNS). DNS-Einstellungen nie anfassen.
- **CNAME:** Die Datei `CNAME` (Inhalt: `courses.nilsroemer.com`) liegt im Repo-Root und ist in `_quarto.yml` unter `project.resources` eingetragen. Dadurch landet sie bei jedem Build in `_site/` und auf `gh-pages`, sonst verliert GitHub Pages die Custom Domain.
- **Keine CI/CD:** Keine GitHub Actions, kein automatischer Deploy. Veröffentlicht wird ausschließlich manuell (siehe Workflow).
- **Toolchain:** Quarto 1.9.x, `uv` (Python 3.12, Abhängigkeiten in `pyproject.toml`/`uv.lock`: jupyter, jupytext, matplotlib, numpy, pandas), Git, Claude Code.
- **Mermaid:** Die Mermaid-Diagramme in `lectures/lec_04_scheduling.qmd` brauchen für den Typst-/PDF-Export das Quarto-Tool `chrome-headless-shell` (`quarto tools`; installieren mit `quarto install chrome-headless-shell`). Ohne das Tool scheitert der Render.
- **Nicht versionierte Build-Voraussetzung:** `_freeze/` (Ausführungs-Cache) ist gitignored. In einem frischen Clone oder Worktree den Ordner aus dem Hauptcheckout kopieren, sonst werden alle Python-Zellen neu ausgeführt (dauert deutlich länger, scheitert aber nicht).

## Wichtige Befehle

```bash
uv sync                          # Python-Umgebung (.venv) aus pyproject.toml/uv.lock anlegen
uv run quarto preview            # lokal rendern mit Live-Reload
uv run quarto render             # kompletter Build nach _site/ (gitignored)
uv run quarto render tutorials/tut_01_01_variables.qmd   # einzelne Datei
quarto publish gh-pages          # Deploy auf GitHub Pages → courses.nilsroemer.com (nur auf Anweisung!)
quarto tools                     # Status von chrome-headless-shell prüfen
```

Immer `uv run quarto …` verwenden, nicht `quarto …` allein: Jupyter liegt im `.venv`, und Quarto findet den Python-Kernel sonst nicht.

## Workflow

**Veröffentlichen**

- `quarto publish gh-pages` wird **nur auf ausdrückliche Anweisung von Nils** ausgeführt. Ein Push auf `main` veröffentlicht nichts; erst `publish` ändert die Live-Seite.
- Vor dem Publish lokal mit `uv run quarto render` prüfen, dass der Build fehlerfrei durchläuft (alle Formate: HTML, RevealJS, Typst-PDF, ipynb, hugo-md).

**Kleine Änderungen** (Texte, Styling, einzelne Seiten)

- Direkt auf `main` arbeiten, committen und pushen (Commit-Messages auf Deutsch, wie in der Historie).

**Größere Umbauten** (neue Bereiche, Struktur-/Designänderungen, mehrere Seiten gleichzeitig)

- Mit den Superpowers-Skills arbeiten: Brainstorming → Plan → Umsetzung auf einem eigenen Branch in einem Git-Worktree (`superpowers:using-git-worktrees`).
- Am Ende das Ergebnis zeigen. **Erst nach Freigabe von Nils** in `main` mergen, dann den Branch und den Worktree aufräumen (`superpowers:finishing-a-development-branch`).
- Auch danach gilt: kein Publish ohne Anweisung.

## Projektstruktur

```
_quarto.yml          # Projektkonfiguration: Sidebar, Footer, Theme, Formate, Resources (CNAME, fonts/, assets/, images/)
_brand.yml           # Quarto-Brand: Farbpalette und Schriftfamilien (Planningio-Ableitung wie nilsroemer.com, plus Kurs-Akzente)
styles.scss          # @font-face (self-hosted), Design-Tokens, Seitenkopf, Linkstil, Sidebar/Footer, kompletter Folienstil (Block „SLIDES")
_typst/              # typst-template.typ: Vorlage für den PDF-Export (Titelblock, Überschriften, Code), in _quarto.yml registriert
index.qmd            # Startseite: Kursbeschreibung, Learning Outcomes, Struktur, AI Policy, Kontakt
general/             # Syllabus, FAQ, Installation (uv.qmd), Literatur, Cheatsheet, Imprint, Privacy, header.html (leer)
lectures/            # Vorlesungen als .qmd (HTML-Seite + RevealJS-Folien + PDF); tut_05_01_llm.qmd ist ein Tutorial im Lecture-Ordner
tutorials/           # Interaktive Python-Tutorials (HTML, ipynb, PDF)
include/             # Wiederverwendbare Includes (tutorial_end.qmd: Abschnitt „Solutions")
helpers/             # strip_polyfill.py (Post-Render, entfernt cdnjs-Polyfill), strip-pauses.lua (Pausenmarker nur in RevealJS), Konvertierungsskripte
assets/              # Self-hosted MathJax: assets/mathjax (v3, HTML) und assets/mathjax2 (v2, RevealJS-Plugin braucht v2-API)
fonts/               # woff2: Poppins, Inter, Space Mono (latin + latin-ext)
fonts-ttf/           # TTF-Varianten für den Typst-PDF-Export (font-paths)
images/              # Alle Bilder lokal (bg/, gif/, alg/, atlb/, caching/, Porträts)
animations/          # GIFs für Lecture 05 (versioniert, ca. 23 MB, von lec_05 mit festem Seed erzeugt)
CNAME                # Custom Domain für GitHub Pages
pyproject.toml, uv.lock   # Python-Abhängigkeiten
_freeze/, _site/, .quarto/   # Build-Cache und Output, gitignored, nie manuell bearbeiten
```

Sonstige Dateien im Root (`klu_syllabus.md`, `manual.md`, `main.py`, `messages/`, `projects/`) sind Arbeitsmaterial und werden nicht gerendert (`project.render` in `_quarto.yml` listet die Quellen explizit).

**Navigation:** Sidebar (Welcome, Syllabus, Kapitel 01 bis 06 mit Lecture und Tutorials, FAQs, Installation, Literature, Cheatsheet) und Footer werden zentral in `_quarto.yml` konfiguriert. Neue Seiten dort eintragen. Die Anzeige-Titel der Tutorials folgen dem Schema `01-01: Variables` (Kapitel-Nummer, Tutorial-Nummer, Thema); Dateinamen und URLs bleiben davon unberührt. Keine Repo-Actions (Edit this page, View source, Report an issue) in `_quarto.yml`.

**Theme:** Cosmo + `styles.scss` + Brand, in genau dieser Reihenfolge (`brand` muss nach `styles.scss` stehen, sonst „Undefined variable $brand-*", weil die Defaults-Ebenen rückwärts verarbeitet werden). Die RevealJS-Folien binden dieselbe `styles.scss` über `lectures/_metadata.yml` ein. Das Design ist eine reduzierte Ableitung des Planningio-Brands wie auf nilsroemer.com (Navy/Blau, Poppins für Überschriften, Inter für Fließtext, Space Mono für Code und Meta-Angaben). Kurs-spezifische Zusatzakzente (Amber, Rot, Grün) nur für Folien-Hervorhebungen und Callouts.

**Ausführung:** `execute: freeze: auto` in `_quarto.yml`. Dokumente mit Python-Zellen (alle Tutorials, `lec_01`, `lec_05`) werden beim Render nur dann neu ausgeführt, wenn sich ihre Quelle geändert hat; sonst kommt der Inhalt aus `_freeze/`. Nicht auf `freeze: true` wechseln: damit würde Quarto auch nach Quelländerungen den alten Cache nehmen (inklusive veralteter Titel und Texte). Lecture V erzeugt beim Ausführen die GIFs in `animations/` mit festem Random-Seed (`np.random.seed(42)` in jeder Animationszelle), damit die versionierten Dateien bei jedem Lauf identisch bleiben; der Seed bleibt erhalten.

## Konventionen

- **Titel:** Inhaltsseiten mit Quarto-Title-Block nutzen `title:` und `subtitle:`. Die Rechtstexte (`general/imprint.qmd`, `general/privacy.qmd`) nutzen `pagetitle:` und setzen die sichtbare Überschrift als `# …` im Body. Nummer und Thema werden in Seitentiteln und Sidebar mit Doppelpunkt getrennt (`Lecture I: Optimal Stopping`, `Tutorial I.I: Variables and Types`, `01-01: Variables`), nicht mit ` - `.
- **Kontakt nur per E-Mail** (nils.roemer@planningio.com). Keine Verweise auf GitHub-Issues, keine Repo-Actions. Der GitHub-Link im Footer bleibt (Quelle der Lösungen, siehe `include/tutorial_end.qmd`).
- **Keine Requests an Dritte:** Fonts self-hosted (`fonts/`, `@font-face` in `styles.scss`, `$web-font-path: false`), MathJax self-hosted (`assets/`), alle Bilder und GIFs lokal (`images/`, `animations/`), der von Pandoc injizierte cdnjs-Polyfill wird per Post-Render-Skript entfernt. Keine Analytics, keine Cookies, keine CDN-Skripte. Einzige Ausnahme: ein YouTube-Embed im privacy-enhanced Mode (youtube-nocookie.com) in `lectures/tut_05_01_llm.qmd`, der in der Datenschutzerklärung erfasst ist. Die Datenschutzerklärung sichert genau diesen Stand zu, jede neue Abhängigkeit muss dagegen geprüft werden.
- **Rechtstexte (`general/imprint.qmd`, `general/privacy.qmd`):**
  - Keine sichtbaren Datumsangaben („Stand: …", „Last updated …") einfügen.
  - Änderungen an Rechtstexten vor dem Einarbeiten als Vorschlag zeigen und von Nils freigeben lassen. Das gilt auch für scheinbar triviale Korrekturen.
- **Keine Gedankenstriche als Satzzeichen im sichtbaren Text.** Sätze stattdessen umformulieren (Komma, Punkt, Doppelpunkt, Klammer). Bereichsangaben wie `2018–2022` bleiben. Code, Code-Kommentare und Rechtstexte sind davon ausgenommen und werden nicht angefasst.
- **Links im Inhalt:** Textfarbe mit dezenter grauer Unterstreichung (`--border-strong`), bei Hover Primärfarbe mit Unterstreichung in Primärfarbe. Gilt für den Inhaltsbereich der gesamten Kursseite (Website und Tutorials), global in `styles.scss` definiert, keine seitenspezifischen Abweichungen. Navigationselemente (Breadcrumbs, Sidebar, Inhaltsverzeichnis, Format-Links, Seiten-Footer, Titelblock) sind ausgenommen und behalten ihren eigenen Stil. Bewusste Abweichung von nilsroemer.com: Die graue Linie bleibt, damit Links in Aufgaben- und Fließtexten auffindbar sind. Folien ausgenommen: dort Textfarbe ohne Linie, Hover Primärfarbe mit Linie.
- **Seitenkopf:** Auf allen Website-Seiten gleich, global in `styles.scss` definiert (Block „Page header", Spacing über die `--space-*`-Tokens). Anders als auf nilsroemer.com bleibt Quartos Title-Block der Seitenkopf (Titel, Untertitel, Lecturer/Affiliation, Format-Links); die Rechtstexte nutzen `pagetitle:` und ein `#` im Body. Abstände: oberhalb des Kopfs `padding-top` auf `main` (`--space-6`), Kopf → Inhalt `margin-bottom` des Title-Blocks bzw. der Body-h1 (`--space-5`), vor jedem Abschnitt `margin-top` der h2 (`--space-7`). Keine Linie unter h1 oder h2, keine seitenspezifischen Abweichungen. Folien sind davon ausgenommen.
- **Abschnittstitel und Labels** ruhig halten wie auf nilsroemer.com: Meta-Angaben (Untertitel, Lecturer, Breadcrumbs, „On this page", „Other Formats") als kleine, gedämpfte Labels in Space Mono bzw. Poppins-Uppercase.
- **Eintrags-Layout (Startseite, Syllabus):** Entspricht `.entries` auf nilsroemer.com, wird hier aber über `body-classes: entries` im YAML-Header aktiviert, nicht über ein `::: {.entries}`-Div. Grund: Pandoc erzeugt kein Inhaltsverzeichnis, wenn mehrere `##`-Abschnitte in einem Div liegen. Abschnitte als `##` (kleine Uppercase-Labels), Einträge als `###`, Meta-Zeile als `[…]{.entry-meta}` (Space Mono, gedämpft).
- **Folien (RevealJS):** Gestaltung komplett in `styles.scss` (Defaults `$presentation-*`, Block „SLIDES", alles auf `.reveal` gescoped). Hell und ruhig: weißer Grund, Text und Überschriften in Ink, Inter für Text, Poppins für Überschriften, Space Mono für Meta-Angaben (Untertitel, Lecturer/Affiliation, Footer, Foliennummer). Primärblau nur für `.question`-Labels, den Fortschrittsbalken und Links beim Hover. Titelfolie wie der Seitenkopf der Website (Lecturer/Affiliation mit kleinen Uppercase-Labels per CSS), Abschnittsfolien (`# Titel {.title}`) weiß mit Titel in Ink, `.loud-slide` weiß mit großem Ink-Text. Eigene Klassen bleiben erhalten: `.flow` (statisch, früher Gradient-Animation), `.highlight` (Ink fett auf Sky-Hintergrund), `.question` (Primärblau), `.task` (Amber), `.errors` (Rot), `.invert-font` (weiß auf halbtransparentem Ink-Panel, nur auf Bildfolien), `.loud-slide`, `.incremental`. Slide-Klassen dürfen auf den HTML-Lecture-Seiten keinen weißen Text auf dunklem Grund erzeugen; dafür gibt es am Ende des Blocks HTML-Fallbacks. `strong` und `em` bleiben in Textfarbe. Keine neuen Logos oder Hintergrundbilder, Seitenverhältnis 1050 × 700 unverändert. Keine persönlichen „About me"-Folien, Nils' Person wird über nilsroemer.com abgedeckt.
- **Folien prüfen:** Nach Gestaltungsänderungen alle Decks auf Überlauf prüfen (normale Ansicht und `?print-pdf`). Überlauf durch zu viel Inhalt wird nicht per CSS kaschiert, sondern als Vorschlag (kürzen, aufteilen, in Notizen) gelistet.
- **PDF (Typst):** Schriften und Farben kommen aus `_brand.yml`, Layout aus `_typst/typst-template.typ` (Titelblock linksbündig wie der Seitenkopf, Untertitel und Lecturer/Affiliation als Space-Mono-Labels, ruhige Überschriften, Code in Sky-Panel, Seitenzahl in Space Mono). Die Vorlage ist eine Kopie von Quartos Standard-`typst-template.typ` mit angepasstem Titelblock; bei Quarto-Updates gegen das Original (`quarto --paths`, `share/formats/typst/pandoc/quarto/`) abgleichen.
- **Folien-Pausen:** Pausenmarker `. . .` nur in Lectures verwenden. Der Lua-Filter `helpers/strip-pauses.lua` (in `_quarto.yml` registriert) entfernt sie in allen Formaten außer revealjs, sonst stehen sie als Text auf der HTML-Seite und im PDF.
- **Tutorials:** Aufgaben als `## Exercise x.y - Titel` mit einer leeren Code-Zelle (`# YOUR CODE BELOW`) und einer eingeklappten Test-Zelle mit `assert`. Am Ende jedes Tutorials `{{< include ../include/tutorial_end.qmd >}}`.
- **Bilder:** Vor dem Einchecken für Web komprimieren und EXIF-Metadaten entfernen. Keine Hotlinks auf fremde Server.
- **Build-Artefakte** (`_site/`, `_freeze/`, `.quarto/`, `.DS_Store`, `*.quarto_ipynb`) niemals committen.

## Stand und offene Punkte

**Stand**

- Live unter courses.nilsroemer.com (GitHub Pages). Kursstart Ende Oktober 2026.
- Seit Juli 2026 betreibt Nils die Seite allein; Design an nilsroemer.com angeglichen, alle Drittanbieter-Requests entfernt, Rechtstexte aktualisiert, Tobias nur noch in den Credits.
- Design-Pass Oktober 2026 (Branch `design-angleich`): globaler Linkstil, ruhige Abschnittstitel und Labels, Gedankenstriche im sichtbaren Text entfernt, Tutorial-Nummerierung in der Sidebar vereinheitlicht, `animations/` versioniert. Details in `UEBERGABE.md`.
- Inhaltliches Review Oktober 2026 (Branch `inhalt-review`): Tippfehler und eindeutige Fehler korrigiert, Pausenmarker-Filter, alle Befunde mit Priorität und Vorschlag in `REVIEW.md`.

**Offene Punkte**

- Vor Kursstart: Termine und Semesterangaben prüfen (Syllabus, Startseite, `klu_syllabus.md`), Welcome-Mail in `messages/` aktualisieren.
- Wenn eigene Analytics gewünscht: neu einbauen und Datenschutzerklärung ergänzen (nach Freigabe).
- Optional: Favicon, Open-Graph-Metadaten.
