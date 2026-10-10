# Übergabe: Branch `design-angleich`

Stand: 10. Oktober 2026 (drei Nachträge unten, der jüngste ist die Design-Angleichung der Folien und PDFs). Branch ist gepusht, nicht in `main` gemergt, nicht veröffentlicht. Worktree: `.claude/worktrees/design-angleich`.

## Was geändert wurde

**CLAUDE.md** (Commit f41668c, ergänzt im letzten Commit)

- Aufbau und Konventionen von nilsroemer.com übernommen: Infrastruktur, Workflow (Branch bei größeren Umbauten, Publish nur auf Anweisung), keine Requests an Dritte, Rechtstexte (keine Datumsangaben, keine Änderung ohne Freigabe), Name „Roemer", keine Gedankenstriche, globaler Linkstil, Seitenkopf-Regel, Eintrags-Layout.
- Ergänzt: Python über uv, `execute: freeze: true`, Mermaid braucht `chrome-headless-shell`, Tobias Vlćek nur in den Credits, Abschnitt „Stand und offene Punkte" mit Kursstart Ende Oktober 2026.

**Design** (`styles.scss`, `_brand.yml`, Commits df20e52 und 148f9eb)

- Linkstil wie auf nilsroemer.com: Textfarbe, keine Unterstreichung, Hover Primärfarbe mit Unterstreichung. Gilt auf Website, Tutorials und Folien. Nebenbei behoben: Der bisherige Linkstil griff auch auf Sidebar und Inhaltsverzeichnis (jeder Eintrag war unterstrichen), jetzt auf den Inhaltsbereich beschränkt.
- Seitenkopf-Regel (deine Ergänzung): Abstände über `--space-*`-Tokens, keine Linie unter h1 und h2, keine seitenspezifischen Abweichungen. Folien ausgenommen.
- Ruhige Labels: Untertitel, Lecturer/Affiliation, Breadcrumbs in Space Mono gedämpft; „On this page" und „Other Formats" als kleine Uppercase-Labels; Sidebar-Kapitel in Poppins, Einträge gedämpft, aktiver Eintrag in Primärfarbe.
- Eintrags-Layout (`.entries` von nilsroemer.com) für Startseite und Syllabus. Syllabus umstrukturiert: `## Lectures` als Label, je Vorlesung `###` plus `[Lecture I]{.entry-meta}`. Startseite: Abschnitte von `#` auf `##`.
- Sidebar-Trenner: `***` wurde als Text angezeigt, jetzt `---` (echte Linie).

**Text** (Commit 8c47ba9)

- Gedankenstriche als Satzzeichen entfernt und umformuliert in: `index.qmd` (2), `lec_00`, `lec_01`, `lec_04`, `lec_05` (je „After the break: …"), `lec_02` (Invert-Font-Zeile), `lec_03` (Spotlight/Starlight/Daylight-Liste), `tut_03_03_packages.qmd` (1).
- Rechtstexte: keine Gedankenstriche gefunden, nichts zu listen.

**Sidebar** (Commit a8625d7)

- Tutorial-Titel ab Kapitel 4 vereinheitlicht: `10 - Recap` → `04-01 - Recap`, `11 - Dictionaries` → `04-02 - Dictionaries`, `12 - DataFrames` → `04-03 - DataFrames`, `13 - LLM` → `05-01 - LLM`, `14 - Recap` → `05-02 - Recap`, `15 - Free Tasks` → `05-03 - Free Tasks`. Dateinamen und URLs unverändert.

## Getroffene Entscheidungen

1. **Links in Tutorials behalten eine dezente Kennzeichnung** (graue Unterstreichung in `--border-strong`, Hover Primärfarbe). Grund: In Aufgabentexten wie „See the separate guide: uv setup" wäre der Link sonst nicht erkennbar. Umgesetzt über `body-classes: tutorial` in `tutorials/_metadata.yml` und in `lectures/tut_05_01_llm.qmd`. Auf der Website (z. B. „syllabus", „Quarto", „revealjs" auf der Startseite) gilt der reine nilsroemer.com-Stil, diese Links sind nur per Hover erkennbar.
2. **Eintrags-Layout über Body-Klasse statt `::: {.entries}`-Div.** Pandoc erzeugt kein Inhaltsverzeichnis, wenn mehrere `##`-Abschnitte in einem Div liegen (auf nilsroemer.com fällt das nicht auf, weil CV und Lectures `toc: false` haben). Deshalb `body-classes: entries` im YAML von `index.qmd` und `general/syllabus.qmd`, CSS auf `body.entries` gescoped.
3. **Quartos Title-Block bleibt der Seitenkopf.** nilsroemer.com blendet ihn aus und nutzt `pagetitle` plus `#` im Body. Hier hängen Lecturer/Affiliation, Untertitel, RevealJS-Titelfolien und PDF-Export am `title:`-Feld, eine Umstellung aller 30 Seiten wäre ein eigener Umbau. Die Abstände folgen trotzdem den Tokens der Seitenkopf-Regel.
4. **Tote YAML-Reste entfernt**: `html: theme: [litera, ../styles_html.scss]` in `faq.qmd` und `cheatsheet.qmd` (Datei existiert nicht, Key lag nicht unter `format:`, wurde ignoriert).
5. **Tippfehler im Syllabus-Untertitel** korrigiert: „This years" → „This year's".
6. **Umformulierungen** konservativ: Doppelpunkt oder Komma statt Gedankenstrich, keine inhaltlichen Änderungen. Beispiel `lec_03`: „**Spotlight** – Immediate goals – Focus (…)" → „**Spotlight**: Immediate goals, your focus (…)".
7. **`_brand.yml`**: `link.decoration` von `underline` auf `none`, damit Brand und Linkstil nicht gegeneinander arbeiten.
8. **Nicht angefasst**: Rechtstexte, Code, Code-Kommentare, Bindestriche mit Leerzeichen in Titeln („Lecture I - Optimal Stopping"), Folien-Typografie abseits des Linkstils, `author:`-Zeile der Startseite (Credit).

## Nachtrag 10. Oktober 2026: deine Antworten umgesetzt

1. **Linkkennzeichnung gilt auf der gesamten Kursseite.** Die graue Unterstreichung (`--border-strong`, Hover Primärfarbe) ist jetzt die globale Regel in `styles.scss`, die Tutorial-Ausnahme und die `body-classes: tutorial` in `tutorials/_metadata.yml` und `lectures/tut_05_01_llm.qmd` sind entfernt (beide Dateien wieder wie auf `main`). Folien unverändert: Textfarbe ohne Linie, Hover Primärfarbe. Entscheidung 1 unten ist damit überholt.
2. **`animations/` versioniert.** Gesamtgröße 23 MB (vier GIFs, größte `dice_fairness.gif` mit 9,6 MB), also unter deiner 50-MB-Grenze. Eintrag aus `.gitignore` entfernt, Ordner eingecheckt.
3. **`404.qmd` aus `project.render` entfernt.**
4. **`.claude/worktrees/` in `.gitignore` aufgenommen.**

CLAUDE.md entsprechend angepasst (Linkkonvention, Build-Voraussetzungen, offene Punkte).

## Nachtrag 2, 10. Oktober 2026: weitere Anpassungen

1. **GitHub-Issue-Verweise entfernt.** Nur die FAQ hatte welche (zwei Sätze „or by creating an issue on GitHub"), jetzt Kontakt nur per E-Mail. Nicht angefasst, weil kein Issue-Verweis: der GitHub-Link im Footer und der Hinweis in `include/tutorial_end.qmd`, dass die Lösungen im GitHub-Repository liegen (Button unten links). Die Erwähnungen von GitHub Copilot in `tut_05_01_llm.qmd` sind Inhalt.
2. **Repo-Actions entfernt** (`repo-actions` in `_quarto.yml`). `repo-url` steht noch drin, ist ohne Actions aber wirkungslos.
3. **Lecturer und Affiliation** zentral in `lectures/_metadata.yml` und `tutorials/_metadata.yml`: `author: "Dr. Nils Roemer, External Lecturer"`, `institute: "Planningio GmbH"`. Die `author:`- und `institute:`-Zeilen in den einzelnen Lectures (darunter „Kühne Logistics University Hamburg - Fall 2024" in Lecture VI) sind entfernt. Entscheidungen dabei:
   - Startseite behält die Author-Zeile „Dr. Nils Roemer and Dr. Tobias Vlćek" (Credits-Regel). Die allgemeinen Seiten (Syllabus, FAQ, Installation, Literature, Cheatsheet) hatten bisher keinen Lecturer-Block und haben weiterhin keinen. Wenn du ihn dort auch willst: `author`/`institute` in den Dateien oder in `_quarto.yml` ergänzen.
   - Der Folien-Footer stand auf `{{< meta author >}}` und hätte „Dr. Nils Roemer, External Lecturer" auf jeder Folie gezeigt. Jetzt fest „Dr. Nils Roemer".
   - Quarto rendert den Autor-String mit Komma als eine Person (geprüft im Titelblock und auf der Titelfolie).
4. **Navigationselemente ohne Link-Unterstreichung.** Die Linkregel in `styles.scss` schließt jetzt `nav` (Breadcrumbs, Sidebar, TOC), Titelblock, Format-Links, TOC-Actions und Seiten-Footer aus.
5. **Doppelpunkt statt „ - " in Titeln:** alle `title:` in `lectures/` und `tutorials/` (z. B. „Lecture I: Optimal Stopping", „Tutorial I.I: Variables and Types", „Introduction: Programming") und die 15 Tutorial-Einträge in der Sidebar („01-01: Variables"). Dateinamen und URLs unverändert. Nicht angefasst: Abschnittsüberschriften in Tutorials (`# Section 1 - Using Standard Libraries`, rund 30 Stück) und die 57 Exercise-Überschriften (`## Exercise 1.1 - …`, dokumentierte Konvention). Sag Bescheid, wenn die auch umgestellt werden sollen.

CLAUDE.md entsprechend angepasst (Lecturer-Meta, Titel-Trennzeichen, Kontakt, Links).

## Nachtrag 3, 10. Oktober 2026: Design-Angleichung Folien, PDF und Website

Auftrag: Website, Tutorials, RevealJS-Folien und Typst-PDF einheitlich nach nilsroemer.com. Alles auf `design-angleich`, nicht gemergt, nicht veröffentlicht. Der Auftrag endete mit „ENDE DES AUFTRAGS", war also vollständig.

**Schritt 1 (Issue-Verweise, Repo-Actions, Lecturer, Navigation, Titel)** war aus Nachtrag 2 bereits erledigt. Zusätzlich geprüft: Der PDF-Titelblock zeigt Lecturer und Affiliation (siehe Typst unten).

**Schritt 2 („based on" → „inspired by")**

- Geändert: `index.qmd` (Credits-Zeile und Kursbeschreibung), `lectures/lec_00_introduction.qmd` („Lecture inspired by the book"). Auf nilsroemer.com war das schon erledigt.
- Bewusst nicht geändert: `klu_syllabus.md` (nicht gerenderte Kopie des bei der KLU eingereichten Syllabus, sollte dem eingereichten Text entsprechen) und fachliche Formulierungen wie „based on the geometric distribution" oder „based on dynamic programming", die nichts mit dem Buch zu tun haben.

**Schritt 3 (RevealJS-Folien)**, alles in `styles.scss` (Defaults `$presentation-*`, Block „SLIDES"), keine Inhalte, keine Bilder, keine Reihenfolge geändert:

- Typografie: Root-Schriftgröße 32 px statt 40 px (Quarto-Standard), Zeilenhöhe 1.45, Überschriften Poppins 600 in Ink (h2 1.45em), Listen mit gedämpften Aufzählungszeichen und etwas Luft. Die kleinere Grundschrift ist die wichtigste Einzelmaßnahme gegen den Überlauf und wirkt ruhiger; wenn dir die Folien im Hörsaal zu klein sind, ist `$presentation-font-size-root` die eine Stellschraube.
- Titelfolie wie der Seitenkopf der Website: Titel in Poppins, Untertitel als Space-Mono-Label, darunter „Lecturer" und „Affiliation" als kleine Uppercase-Labels (per CSS `::before`, kein Inhalt geändert) mit den Werten in Space Mono.
- Abschnittsfolien (`# Titel {.title}`): weiß statt Sky-Blau, Titel in Ink. `.flow` ist jetzt statisch (vorher animierter Farbverlauf), die Klasse bleibt in allen Dateien erhalten.
- `.loud-slide`: weiß mit großem Ink-Text in Poppins statt dunkelblau mit heller Schrift. Reveal erkennt den hellen Hintergrund automatisch, Footer und Foliennummer passen sich an.
- Hervorhebungen: `strong`/`em` in Textfarbe (vorher Primärblau), `.highlight` Ink fett auf Sky-200-Fläche (vorher Rot), `.question` Primärblau, `.task` Amber, `.errors` Rot. Primärblau bleibt damit den Frage-Labels, dem Fortschrittsbalken und Hover-Links vorbehalten.
- Bildfolien: `.invert-font` als halbtransparentes Ink-Panel mit kleinem Radius (vorher Vollton mit 5-px-Rahmen), Bildnachweis im Footer als Space Mono.
- Code: Sky-100-Panel mit feinem Rahmen und Radius, Space Mono, Ausgabe gedämpft; Inline-Code primärblau auf Sky-100.
- Callouts: weiß, feiner Rahmen, 4-px-Akzentlinie links, Titel in Poppins; Tabellen: Inter, Kopfzeile als kleines Uppercase-Label, nur horizontale Linien.
- Footer und Foliennummer in Space Mono 13 px gedämpft, Fortschrittsbalken 3 px Primärblau, Menü-Button gedämpft.
- Fußnoten klein und gedämpft, 44 px über dem unteren Rand (Quarto setzt sie auf 20 px, direkt auf die Footer-Zeile). Bilder im Inhalt auf max. 440 px Höhe begrenzt (`r-stretch` 520 px), `.r-fit-text` mit engem Zeilenabstand; in der Druckansicht feste Größe statt Fit.
- HTML-Lecture-Seiten: alle Slide-Klassen sind auf `.reveal` gescoped, dazu HTML-Fallbacks (`.invert-font`, `.loud-slide`, `.flow`, `.white` → normaler Text; Bildnachweise als Meta-Text). Kein weißer Text auf dunklem Grund mehr (Screenshot `nachher/html-lecture-01.png`).
- Druckansicht (`?print-pdf`): gemessen 0 abgeschnittene Seiten bei Lecture I (alte Gestaltung: 6), siehe `nachher/print-lec01.png`.

**Schritt 4 (Typst-PDF)**

- Schriften (Inter, Poppins, Space Mono), Farben, Code-Hintergrund und Link-Farbe kamen schon aus `_brand.yml`. Neu: `_typst/typst-template.typ` (in `_quarto.yml` unter `format.typst.template-partials` registriert), Kopie von Quartos Standardvorlage mit angepasstem Titelblock (linksbündig, Untertitel und Lecturer/Affiliation als Labels wie auf der Website), ruhigeren Überschriften (Abstände, Größen 15/12.5/11 pt), Code-Panel mit feinem Rahmen, gedämpften Aufzählungszeichen, Flattersatz statt Blocksatz und Seitenzahl in Space Mono.
- Nicht gemacht: Callout-Boxen im PDF (Quarto-eigene Funktion, Farben kommen bereits aus dem Brand), Tabellen (Quarto-Standard). Beides wäre nur mit Eingriffen in Quartos Typst-Definitionen machbar.
- Vorbestehend, nicht Teil des Auftrags: Die Pausenmarker `. . .` aus den Folien erscheinen im PDF und auf den HTML-Seiten als Text, ebenso werden die `.loud-slide`-Texte zu drei kurzen Absätzen. Beides ist Inhalt (Quarto rendert Pausen nur in RevealJS); Abhilfe wäre, Pausen über `{.fragment}` zu setzen oder die Lecture-Seiten als eigene Quelle zu führen.

**Schritt 5 (Überlaufprüfung)**, Skript `overflow.mjs` (chrome-headless-shell per DevTools-Protokoll, misst sichtbare Textausdehnung aller Folien mit allen Fragmenten und zählt die PDF-Seiten pro Folie in `?print-pdf`), Messwerte in `screenshots-review/ueberlauf/messung-*.json`:

- Vorher (40 px, alte Gestaltung): 10 Folien brauchten im Druck zwei Seiten, zahlreiche Folien liefen in den Footer (z. B. „The Secretary Problem", „Interactive Casino Challenge", alle Fußnotenfolien).
- Nachher: 1 Folie mit Überlauf, 2 Folien, die den Footer-Bereich berühren, 1 Folie mit zwei Druckseiten. Alle vier sind Inhaltsfragen, nichts davon habe ich per CSS kaschiert:

| Lecture | Folie | Problem | Vorschlag | Screenshot |
|---|---|---|---|---|
| II Explore vs. Exploit | 40 „The Bellman approach III" | 10 × 10-Tabelle, 70 px zu hoch und 44 px zu breit, im Druck 2 Seiten | `## … {.smaller}` oder Tabelle auf zwei Folien aufteilen, alternativ auf 5 Spalten kürzen | `ueberlauf/lec02-39-bellman-iii.png`, `ueberlauf/print-lec02-bellman.png` |
| II Explore vs. Exploit | 47 „The Gittins Index IV" | 10 × 10-Tabelle, 64 px zu breit, berührt den Footer | `{.smaller}` oder weniger Spalten | `ueberlauf/lec02-46-gittins-iv.png` |
| IV Scheduling | 22 „Single Machine Scheduling" | Bild plus Frage reicht in den Footer-Bereich (670 von 700 px) | Bild mit `{height=380}` oder Frage auf die nächste Folie | `ueberlauf/lec04-21-single-machine.png` |
| IV Scheduling | 21 „Task Classification" | Mermaid-Diagramm plus zweite Frage endet knapp über dem Footer (697 px) | zweite Frage in die Notizen oder auf eine eigene Folie | `ueberlauf/lec04-20-task-classification.png` |

Messartefakt, kein Problem: Codefolien melden 8 px „zu breit" (1058/1050), das ist der Kopieren-Button am rechten Rand des Code-Panels.

**Schritt 6 (Render, Screenshots)**

- Nach jedem Schritt `uv run quarto render`, letzter Lauf fehlerfrei ohne Warnungen (`render_final2.log` im Scratchpad).
- Screenshots in `screenshots-review/` im Worktree (gitignored): `vorher/` und `nachher/` je 30 Bilder (Titel-, Abschnitts-, Text-, Code-, Bild-, Tabellen-, Callout-Folien aus Lectures I, II, IV, V, VI und Tutorial V.I, Druckansicht Lecture I, Typst-PDF Seite 1 und 3 von Lecture I, Lecture-HTML-Seite, Tutorial), `ueberlauf/` mit den Folien aus der Tabelle, dazu `vorher-runde-1/` und `nachher-runde-1-3/` aus den vorherigen Aufträgen.

**Entscheidungen**

1. Grundschrift der Folien 32 px statt 40 px (siehe oben), eine Stellschraube.
2. `.flow` ohne Animation, `.loud-slide` und Abschnittsfolien weiß: entspricht „hell, weißer Grund, Primärblau sparsam"; die Klassen bleiben, nur der Stil ändert sich.
3. `strong` nicht mehr blau. Mit 100+ fetten Begriffen pro Deck wäre Primärblau sonst Flächenfarbe. Falls du die Hervorhebung vermisst: `.reveal strong { color: var(--primary) }` ist eine Zeile.
4. `.highlight` von Rot auf Ink-fett-mit-Sky-Fläche: Rot ist für `.errors` reserviert.
5. Typst-Vorlage als Kopie der Quarto-Standardvorlage statt nur `include-in-header`: nur so lässt sich der Titelblock umbauen. Nachteil: bei Quarto-Updates gegen das Original abgleichen (steht in CLAUDE.md).
6. `freeze: true` beibehalten, siehe Probleme (in Nachtrag 4 auf `auto` umgestellt).

**Probleme, die dabei aufgefallen sind**

- **`freeze: true` liefert veraltete Inhalte.** Beim Komplett-Render nimmt Quarto für Dokumente mit Python-Zellen den kompletten Inhalt aus `_freeze/`, auch Titel und Text, und zwar auch dann, wenn die Quelle geändert wurde. Dadurch standen nach Nachtrag 2 in 12 Tutorials und Lecture V noch die alten Titel („Tutorial I.II - …", „Lecture V - Randomness") im Output, obwohl der Render fehlerfrei war. Für diesen Auftrag habe ich `_freeze/` einmal gelöscht und alles neu ausgeführt; der Output ist jetzt konsistent. In CLAUDE.md steht die Regel, geänderte Dateien mit Code-Zellen einzeln zu rendern. Empfehlung: in `_quarto.yml` auf `freeze: auto` wechseln (führt nur bei geänderter Quelle neu aus), das ist das Verhalten, das man erwartet. Habe ich nicht geändert, weil du `freeze: true` explizit vorgegeben hast.
- **`animations/` wird von Lecture V erzeugt.** Die vier GIFs entstehen in den Code-Zellen von `lec_05_randomness.qmd` und sehen nach jedem Neu-Ausführen anders aus (Zufallssimulation). Seit sie versioniert sind, erzeugt jeder Lauf ohne Freeze-Cache 23 MB Diff. Ich habe nach dem Neu-Ausführen die committeten Versionen wiederhergestellt. Entscheide, ob die GIFs versioniert bleiben (dann nach einem Neu-Ausführen jeweils `git checkout -- animations`) oder ob sie wieder gitignored werden und die Erzeugung Teil des Builds ist (dann scheitert ein frischer Clone nicht mehr, weil `_freeze/` ohnehin fehlt und die Zellen laufen).
- **`lectures/lec_01_optimal_stopping_files/figure-revealjs/cell-3-output-1.png`** ist im Repo versioniert, wird aber von jedem Render gelöscht (Quarto legt die Grafik in `_freeze/` ab). Ich habe die Datei jeweils wiederhergestellt. Empfehlung: `git rm`, sie ist ein Build-Artefakt.

## Nachtrag 4, 10. Oktober 2026: Freeze, Seed, Überlauf-Folien, Merge

**Umgesetzt**

1. `execute: freeze: auto` in `_quarto.yml`; CLAUDE.md entsprechend (Abschnitt „Ausführung" und Projektstruktur). Dokumente mit Code-Zellen werden jetzt nur bei geänderter Quelle neu ausgeführt.
2. `lec_05_randomness.qmd`: in jeder der vier Animationszellen (Dice Rolls, Estimating π, Simulated Annealing, TSP) steht am Anfang `np.random.seed(42)`. Die GIFs in `animations/` wurden einmal neu erzeugt und committet (24 MB). Reproduzierbarkeit geprüft: `_freeze/lectures/lec_05_randomness` gelöscht, Lecture V erneut gerendert, MD5-Summen aller vier GIFs identisch (siehe unten).
3. `lectures/lec_01_optimal_stopping_files/figure-revealjs/cell-3-output-1.png` per `git rm` entfernt.
4. Überlauf-Folien: Lecture II „The Bellman approach III" und „The Gittins Index IV" mit `{.smaller}`; Lecture IV „Single Machine Scheduling" Bild auf `{height="340px"}`; „Task Classification" zweite Frage auf die neue Folie „Task Classification II" (Lecture IV hat jetzt 83 statt 82 Folien). Überlaufprüfung erneut für alle acht Decks (normal und `?print-pdf`): 0 Überläufe, 0 Footer-Berührungen, 0 Folien mit zwei Druckseiten. Übrig bleibt nur das bekannte Messartefakt (Kopieren-Button, 8 px) auf drei Codefolien. Screenshots in `screenshots-review/nachtrag-4/`.
5. Komplett-Render fehlerfrei ohne Warnungen (`render_round4.log` im Scratchpad). `design-angleich` in `main` gemergt, Worktree und Branch aufgeräumt, nichts veröffentlicht.

**Entscheidungen**

- Seed 42 in jeder Zelle statt einmal am Anfang: die Zellen sind unabhängig voneinander ausführbar (z. B. beim Rendern einzelner Abschnitte oder in einem Notebook), und jede soll für sich reproduzierbar sein.
- Neue Folie heißt „Task Classification II" (römische Nummerierung wie bei „The Bellman approach III").

## Offene Fragen an dich

- Syllabus-Untertitel „This year's course structure" und Semesterangaben vor Kursstart prüfen.
- Grundschrift der Folien: 32 px passend für den Hörsaal, oder lieber 34 bis 36 px?

## Probleme

- **Build in frischem Checkout** (erledigt im Nachtrag): `animations/` war gitignored, ohne den Ordner scheiterte der Typst-Export von Lecture 05. Jetzt versioniert. `_freeze/` bleibt gitignored; ohne den Cache werden alle Python-Zellen neu ausgeführt, der Build läuft aber durch.
- **Slide-Klassen auf der Lecture-HTML-Seite**: `.invert-font`, `.loud-slide` und Bildnachweise mit weißem Text auf dunklem Grund erscheinen auch in der HTML-Version der Lectures (vorbestehend, nicht Teil dieses Auftrags, siehe Screenshot `lecture-page.png`).
- Beim Bisect für das TOC-Problem habe ich `index.qmd` und `general/syllabus.qmd` mehrfach einzeln gerendert; der finale Komplett-Render lief danach fehlerfrei durch (siehe Log).

## Screenshots und Logs

Ab Nachtrag 3 liegen alle Screenshots zusätzlich in `screenshots-review/` im Worktree (gitignored, siehe oben). Ältere Pfade im Scratchpad der Session:

```
/private/tmp/claude-501/-Users-nils-Projekte-Programming-Everyday-Decisions/cf5c9fb6-d317-4fff-bb24-e4a13102ce62/scratchpad/
  screenshots/before/   index, syllabus, tutorial, lecture-page, slides-title, slides-content, slides-section, faq, literature
  screenshots/after/    dieselben plus imprint
  render_baseline.log   Komplett-Render vor den Änderungen (erster Lauf scheiterte an animations/, zweiter fehlerfrei)
  render_final.log      Komplett-Render nach allen Änderungen
  shoot.sh              Screenshot-Skript (chrome-headless-shell gegen lokalen http.server)
```

Das Scratchpad ist sessionspezifisch; wenn du die Screenshots behalten willst, kopiere den Ordner.
