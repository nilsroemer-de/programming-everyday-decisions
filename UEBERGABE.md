# Übergabe: Branch `design-angleich`

Stand: 10. Oktober 2026 (Nachträge unten). Branch ist gepusht, nicht in `main` gemergt, nicht veröffentlicht. Worktree: `.claude/worktrees/design-angleich`.

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

## Offene Fragen an dich

- Syllabus-Untertitel „This year's course structure" und Semesterangaben vor Kursstart prüfen.

## Probleme

- **Build in frischem Checkout** (erledigt im Nachtrag): `animations/` war gitignored, ohne den Ordner scheiterte der Typst-Export von Lecture 05. Jetzt versioniert. `_freeze/` bleibt gitignored; ohne den Cache werden alle Python-Zellen neu ausgeführt, der Build läuft aber durch.
- **Slide-Klassen auf der Lecture-HTML-Seite**: `.invert-font`, `.loud-slide` und Bildnachweise mit weißem Text auf dunklem Grund erscheinen auch in der HTML-Version der Lectures (vorbestehend, nicht Teil dieses Auftrags, siehe Screenshot `lecture-page.png`).
- Beim Bisect für das TOC-Problem habe ich `index.qmd` und `general/syllabus.qmd` mehrfach einzeln gerendert; der finale Komplett-Render lief danach fehlerfrei durch (siehe Log).

## Screenshots und Logs

Alle im Scratchpad der Session:

```
/private/tmp/claude-501/-Users-nils-Projekte-Programming-Everyday-Decisions/cf5c9fb6-d317-4fff-bb24-e4a13102ce62/scratchpad/
  screenshots/before/   index, syllabus, tutorial, lecture-page, slides-title, slides-content, slides-section, faq, literature
  screenshots/after/    dieselben plus imprint
  render_baseline.log   Komplett-Render vor den Änderungen (erster Lauf scheiterte an animations/, zweiter fehlerfrei)
  render_final.log      Komplett-Render nach allen Änderungen
  shoot.sh              Screenshot-Skript (chrome-headless-shell gegen lokalen http.server)
```

Das Scratchpad ist sessionspezifisch; wenn du die Screenshots behalten willst, kopiere den Ordner.
