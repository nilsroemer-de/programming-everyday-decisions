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
- **Toolchain:** Quarto 1.9.x, `uv` (Python 3.13, Abhängigkeiten in `pyproject.toml`/`uv.lock`: jupyter, jupytext, matplotlib, numpy, pandas 3), Git, Claude Code.
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
general/             # Syllabus, FAQ, Installation Guide (uv.qmd, einzige Quelle für Installationsbefehle), Literatur, Cheatsheet, Imprint, Privacy, header.html (leer)
lectures/            # Vorlesungen als .qmd (HTML-Seite + RevealJS-Folien + PDF)
tutorials/           # Interaktive Python-Tutorials (HTML, ipynb, PDF); tut_05_01_llm.qmd ist ein Foliensatz und trägt die RevealJS-Einstellungen aus lectures/_metadata.yml im eigenen Kopf
include/             # Wiederverwendbare Includes (lecture_literature_start/_books.qmd: Literaturfolien aller Lectures)
helpers/             # speaker-notes.lua (Sprechernotizen auf der HTML-Seite als Notes-Block, im PDF weg), check_lecture_frame.py (Prüfskript Rahmen), course_plots.py (Grafiken im Website-Stil), strip_polyfill.py (Post-Render, entfernt cdnjs-Polyfill), strip-pauses.lua (Pausenmarker nur in RevealJS), Konvertierungsskripte
assets/              # Self-hosted MathJax: assets/mathjax (v3, HTML) und assets/mathjax2 (v2, RevealJS-Plugin braucht v2-API)
fonts/               # woff2: Poppins, Inter, Space Mono (latin + latin-ext)
fonts-ttf/           # TTF-Varianten für den Typst-PDF-Export (font-paths)
images/              # Alle Bilder lokal: Fotos (bg/), GIFs (gif/), Illustrationen (alg/, caching/), Porträts (derzeit ungenutzt)
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
- **Kontakt nur per E-Mail** (nils.roemer@planningio.com). Keine Verweise auf GitHub-Issues, keine Repo-Actions, kein Link auf das GitHub-Repo (seit Oktober 2026 auch nicht mehr im Footer; `repo-url` ist entfernt). Die Tutorials enthalten keinen Hinweis auf geteilte Lösungen (Block „Solutions" im Oktober 2026 entfernt). GitHub als Inhalt (Copilot in Tutorial V.I, Ressource auf der Literaturseite) ist davon nicht betroffen.
- **Keine Requests an Dritte:** Fonts self-hosted (`fonts/`, `@font-face` in `styles.scss`, `$web-font-path: false`), MathJax self-hosted (`assets/`), alle Bilder und GIFs lokal (`images/`, `animations/`), der von Pandoc injizierte cdnjs-Polyfill wird per Post-Render-Skript entfernt. Keine Analytics, keine Cookies, keine CDN-Skripte. Einzige Ausnahme: ein YouTube-Embed im privacy-enhanced Mode (youtube-nocookie.com) in `tutorials/tut_05_01_llm.qmd`, der in der Datenschutzerklärung erfasst ist. Die Datenschutzerklärung sichert genau diesen Stand zu, jede neue Abhängigkeit muss dagegen geprüft werden.
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
- **Zwei Prinzipien für alle Lectures:** (1) „Say what you're going to say, say it, say what you said": feste Eröffnung, Hauptteil entlang einer Roadmap mit genau drei Abschnitten, fester Abschluss. (2) „Speak simply, think deeply": einfache Sprache auf den Folien (eine Aussage pro Folie, Folientitel möglichst als kurze Aussage, Richtwert höchstens 6 Zeilen bzw. 40 Wörter, kurze Sätze, Aktiv, Alltagswörter, Fachbegriffe beim ersten Auftreten erklären), die Tiefe liegt in fachlicher Präzision, Sprechernotizen (`::: {.notes}`) und Fußnoten. Erst Beispiel, dann Regel, dann Formel; jede Formel bekommt einen Satz in Alltagssprache. Überschüssigen Text in Notizen verschieben, nicht löschen. Sprecherperspektive „we".
- **Rahmenstruktur der Lectures:** Die Rahmenfolien stehen ausgeschrieben in jeder Lecture-Datei, es gibt keine Automatik und nur diese eine Quelle. Reihenfolge: direkt nach dem YAML-Kopf (bzw. der versteckten Setup-Zelle) die Folien `## Today in one sentence {.lecture-opening}` (Div `.lecture-summary` mit `[…]{.statement}`, Div `.lecture-why` mit `[Why it matters]{.eyebrow}` und dem Absatz) und `## Roadmap {.lecture-opening}` (Div `.roadmap` mit nummerierter Liste, Einträge `[Punkt]{.roadmap-item .future}`); dann die drei Abschnitte als `# [Punkt]{.flow} {.title visibility="hidden"}`, deren Titel exakt den Roadmap-Punkten entsprechen (in RevealJS unsichtbar, auf der HTML-Seite normale Überschriften). Abschnitt 1 folgt direkt auf die Roadmap; vor Abschnitt 2 und 3 steht je eine Folie `## Roadmap {.section-roadmap}` mit derselben Liste, der aktuelle Punkt `.current`, frühere `.done`, spätere `.future`. Abschnitts-Abschlussfolien (`{.section-covered}`) sind seit dem 27. Oktober 2026 nicht mehr Teil der Rahmung: Lecture 0 und I haben keine mehr; in Lecture II bis VI stehen sie noch und können beim nächsten Durchgang entfernt werden (der Stil in `styles.scss` bleibt bis dahin). Abschluss: `## What we covered {.lecture-closing}` (Div `.covered-list` mit je einem Div `.covered-item`: Punkt als Eyebrow, Satz als Absatz), `## Why it matters {.lecture-closing}` (Div `.lecture-why .closing`), `## {.loud-slide .lecture-key}` mit `.r-fit-text` (ein Satz je Absatz); danach wie bisher „After the break" und das Literatur-Include. Texte in Roadmap-Folien, Abschnittstiteln und den Eyebrows von „What we covered" müssen übereinstimmen; bei Änderungen alle Stellen anpassen. Stil in `styles.scss` (Block „Lecture frame" für Folien, HTML-Fallbacks am Ende). Sprechernotizen (`::: {.notes}`) erscheinen auf der HTML-Seite als „Notes"-Block (`helpers/speaker-notes.lua`), im PDF und md nicht.
- **Rahmen prüfen:** `uv run python helpers/check_lecture_frame.py` meldet je Lecture als Hinweise (Exit immer 0): fehlende Rahmenfolien, Abschnitte ungleich Roadmap, abweichende Roadmap-Folien (und, falls noch vorhanden, Abschnitts-Abschlussfolien mit anderem Titel), Folien über 40 Wörter und Folien ohne Titel (Loud- und Fotofolien sind bewusst ohne Titel). Nach jeder Änderung an einer Lecture laufen lassen.
- **Folien-Pausen:** Pausenmarker `. . .` nur in Lectures verwenden. Der Lua-Filter `helpers/strip-pauses.lua` (in `_quarto.yml` registriert) entfernt sie in allen Formaten außer revealjs, sonst stehen sie als Text auf der HTML-Seite und im PDF.
- **Tutorials:** Aufgaben als `## Exercise x.y - Titel` mit einer leeren Code-Zelle (`# YOUR CODE BELOW`) und einer eingeklappten Test-Zelle (`#| code-fold: true`) mit `assert`. Kein Abschluss-Include und kein Hinweis auf Lösungen am Ende der Tutorials. Inhalte erst verwenden, wenn sie eingeführt sind (Schleifen ab II.II, Funktionen ab III.II, Dictionaries ab IV.II). Tutorials III haben einen eigenen LRU-Cache als roten Faden (Listen, Funktionen, `random`), IV.II greift ihn mit Dictionaries auf.
- **Tests prüfen:** Nach Änderungen an Übungen jede Übung einmal korrekt lösen und zusätzlich eine typische Fehlerlösung probieren: Tests dürfen korrekte Lösungen nicht ablehnen und typische Fehler nicht durchlassen. Testdaten so wählen, dass die häufigste Auslassung auffällt; Zufall nur mit festem Seed. Lösungen nie committen und auf der Kursseite nicht ankündigen.
- **pandas 3:** Positionszugriff immer mit `.iloc[...]`, nie `serie[-1]` (wirft bei Datums- oder Textindex einen KeyError).
- **Bilder:** Vor dem Einchecken für Web komprimieren und EXIF-Metadaten entfernen. Keine Hotlinks auf fremde Server.
- **Grafiken per Code:** Diagramme, Zeitpläne und Kurven entstehen in Code-Zellen aus denselben Daten, die auf der Folie stehen (`helpers/course_plots.py`: `use_course_style()` lädt Inter/Poppins aus `fonts-ttf/` und die Farben aus `_brand.yml`; Funktionen für Gantt-Pläne, Echtzeit-Scheduling, Abhängigkeiten, Zugriffszeiten). Eine versteckte Setup-Zelle (`#| include: false`) am Anfang der Lecture bindet das Modul ein (`sys.path.insert(0, "../helpers")`). Achtung: `freeze: auto` merkt Änderungen an `course_plots.py` nicht; danach die betroffenen Lectures (III, IV, V) mit gelöschtem `_freeze/lectures/<datei>` neu rendern. Dasselbe gilt für Includes (Literaturfolien): der Cache enthält das fertige Markdown mit aufgelösten Includes, also nach einer Include-Änderung `_freeze/tutorials` bzw. `_freeze/lectures` löschen und neu rendern, sonst geht der alte Text live. Fotos und Illustrationen bleiben Bilddateien. Grafiken auf Folien, die nach dem Ergebnis fragen (z. B. maximale Verspätung), zeigen die Antwort nicht vorab.
- **Installation, Single Source of Truth:** Befehle, Codeblöcke und Klickanleitungen zur Einrichtung (VS Code, Erweiterungen, Terminal, uv, Python, Projekt, Notebooks) stehen **nur** im Installation Guide (`general/uv.qmd`). Alle macOS/Windows-Tabsets dort tragen `group="os"`, damit die Systemwahl für die ganze Seite gilt; jeder nötige VS-Code-Neustart steht als eigener `callout-warning` „Restart required“. Lectures erklären (was ist ein Terminal, was macht uv, was ist ein Notebook) und verweisen auf den Guide: Lecture 0 hat dafür die Folie „Now we install together" (Link zum Guide, kein QR-Code) und vier Checkpoint-Folien, die nur das erwartete Ergebnis und den passenden Step nennen. Fehlt in einer Lecture ein Installationsinhalt, kommt er in den Guide, nicht auf die Folie.
- **Zahlen und Fakten:** Konkrete Zahlen auf Folien mit Quelle (Fußnote) oder ausdrücklich als Größenordnung kennzeichnen.
- **Literaturfolien:** Jede Lecture endet mit `{{< include ../include/lecture_literature_start.qmd >}}` und `{{< include ../include/lecture_literature_books.qmd >}}`; lecture-spezifische Literatur (z. B. Ferguson in Lecture I) als eigene Folie dazwischen.
- **Abgaberegel** (Quelle: `klu_syllabus.md`): pass/fail, mindestens 75 % Anwesenheit, zwei Assignments zu algorithmischen Problemen aus dem Kurs, kurze Abschlusspräsentation, alles bis Quartalsende, mindestens 50 % korrekt, Gruppen bis drei Personen. Startseite und Einführungsfolien müssen gleich lauten.
- **Build-Artefakte** (`_site/`, `_freeze/`, `.quarto/`, `.DS_Store`, `*.quarto_ipynb`) niemals committen.

## Stand und offene Punkte

**Stand**

- Live unter courses.nilsroemer.com (GitHub Pages). Kursstart Ende Oktober 2026.
- Seit Juli 2026 betreibt Nils die Seite allein; Design an nilsroemer.com angeglichen, alle Drittanbieter-Requests entfernt, Rechtstexte aktualisiert, Tobias nur noch in den Credits.
- Design-Pass Oktober 2026 (Branch `design-angleich`): globaler Linkstil, ruhige Abschnittstitel und Labels, Gedankenstriche im sichtbaren Text entfernt, Tutorial-Nummerierung in der Sidebar vereinheitlicht, `animations/` versioniert. Details in `UEBERGABE.md`.
- Inhaltliches Review Oktober 2026 (Branch `inhalt-review`): Runde 1 Prüfung und eindeutige Korrekturen, Runde 2 alle Befunde umgesetzt (Fachfehler, Abgaberegel, LRU-/Monte-Carlo-/Fairness-Inhalte, Python 3.13 und pandas 3, Grafiken per Code, gekürzte Folien, geschärfte Tests). Status je Befund in `REVIEW.md`. Runde 3: alle Lectures in die Rahmenstruktur gebracht (Eröffnung, drei Abschnitte, Abschluss) und sprachlich vereinfacht; Details in `RAHMUNG.md`.

**Vor jedem Kursstart (Checkliste)**

- Zwei Wochen vorher den Installation Guide (`general/uv.qmd`) auf einem frischen macOS und einem frischen Windows mit der aktuellen uv-Version komplett durchspielen, Schritt für Schritt wie Studierende.
- Die uv-Release-Notes seit dem letzten Test auf geänderte Standardwerte prüfen (Beispiel: seit uv 0.12 legt `uv init` ein Paket mit `src/` ohne `main.py` an, deshalb `uv init --no-package --python 3.13` im Guide) und den Guide anpassen.
- Danach den Abschnitt „Tested with" am Ende des Guides mit uv-Version und Testdatum (nur Testdatum, kein Änderungsdatum) einfügen bzw. aktualisieren. Das Testdatum darf **nur nach einem echten Durchlauf auf frischen Systemen** gesetzt werden, nie auf Basis von Dokumentation oder Release-Notes. Solange kein Durchlauf stattgefunden hat, gibt es keinen Abschnitt „Tested with" (Stand Oktober 2026: entfernt).

**Offene Punkte**

- Vor Kursstart: Termine und Semesterangaben prüfen (Syllabus, Startseite, `klu_syllabus.md`), Welcome-Mail in `messages/` aktualisieren.
- Wenn eigene Analytics gewünscht: neu einbauen und Datenschutzerklärung ergänzen (nach Freigabe).
- Optional: Favicon, Open-Graph-Metadaten.
