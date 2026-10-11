# REVIEW.md: Inhaltliche Prüfung vor dem Kursstart

Stand: 11. Oktober 2026, Branch `inhalt-review` (von `main` 51b9446). Runde 1 (10. Oktober): Prüfung und eindeutige Korrekturen. Runde 2 (11. Oktober): alle Befunde umgesetzt, siehe Status in Abschnitt 2 und Zusammenfassung in Abschnitt 3.

Runde 1: Geprüft: alle Lectures, Tutorials, Website-Seiten (Startseite, Syllabus, FAQ, Installation, Literatur, Cheatsheet), Rechtstexte nur gelesen. Alle Code-Zellen wurden einmal komplett ausgeführt (`_freeze/` leer, `uv run quarto render`, Exit 0, keine Warnungen im Log, keine stderr-Ausgaben in den gerenderten Seiten). Links und Bildverweise automatisch geprüft (40 externe Links, 0 fehlende lokale Verweise).

Prioritäten: **hoch** = fachlich falsch oder kaputt, **mittel** = veraltet oder inkonsistent, **niedrig** = Stil.

## 1. Direkte Korrekturen aus Runde 1 (committet)

| Commit | Inhalt |
|---|---|
| 349241c | 78 Tippfehler, Grammatik- und Schreibweisenkorrekturen (Liste unten) |
| c9f8f18 | Eindeutige Fehler in Code-Beispielen und Befehlen |
| 132761f | Cursor-Link `cursor.sh` → `cursor.com` (308-Redirect) |
| ee899c2 | Pausenmarker `. . .` nur noch in RevealJS wirksam (Lua-Filter) |

**Text (349241c)**

- Startseite: Attendence → Attendance, programm → program, „without understand" → „without understanding", „contact me under" → „contact me at", python/jupyter → Python/Jupyter (4 Stellen).
- Literatur: fantasticbook, programm, christmas. Installation: „InstallPython", „To these, you need" → „For this".
- Einführung: zweites `<center>` war kein Schließ-Tag, Checkboxen `[]` → `[ ]` (wurden als Text gerendert), eingerückter Pausenmarker.
- Lecture I: essentialy. Lecture II: beeing, prety rush → pretty rash, untill, loose → lose, Loses → Losses (Tabellen und Text, 5 Stellen), „todays", banded → bandit, „to to", „than choose" → „than choosing", „comes" → „come", „was good start", „Few years later, Richard Bellman,". Lecture III: nessecity. Lecture IV: „What's was". Lecture VI: Untertitel war „Programming with Python" statt wie überall, Q&A-Folie ohne `.title`.
- Tutorial V.I: ressources, „a advanced", „then what", „alternative like", „Introduce", „Login into", copilot, **Greg Sanderson → Grant Sanderson** (3Blue1Brown), überzähliges `</p>`.
- Tutorials: „a some variables", „is send", „help us how to make", **Exercise 2.3 nach 3.1 → 3.2** (I.II), „skills exploration", „reate", Überschriftenebene von Exercise 2.2 (II.I), „Range in For Loops" (II.II) und vier Exercises in II.III (waren `#` statt `##`), „look on how", „th previous", „a inbuilt", excercises, „easier as", **„four columns" → „three columns"**, **Nummerierung in IV.III** (Exercise 4.1 in Section 2, zwei „Section 3", jetzt 2.1 / 3.1 / 3.2 / Section 4 mit 4.1 / 4.2), Unfortuantely, variabel, „this weeks", responsiblities, „an pandas", Marker einheitlich `# YOUR CODE BELOW` (IV.I, V.II), Cheatsheet „# Lists" → `##`.

**Code (c9f8f18)**

- Tutorial III.III, Exercise 1.2: `#| # YOUR CODE BELOW` war als Zellenoption getarnt und fehlte im Notebook.
- Tutorial IV.III: `uv install pandas` gibt es nicht, jetzt `uv add pandas`.
- Cheatsheet: Nested-Lists-Beispiel las `restaurants[0][1]` statt `restaurant_data[0][1]`; im break/continue-Beispiel stand das `print` unerreichbar unter `continue`.

**Pausenmarker (ee899c2)**

- `helpers/strip-pauses.lua`, projektweit in `_quarto.yml` registriert. Entfernt `. . .`-Absätze in allen Formaten außer revealjs. Geprüft: 0 Marker in HTML und hugo-md, Fragmentzahl der Folien unverändert (Lecture IV: 77, vorher 78 wegen der in Nachtrag 4 aufgeteilten Folie).


## 2. Befunde mit Status

Status nach der Überarbeitung vom 11. Oktober 2026 (Runde 2, alle Befunde von dir freigegeben). Der Commit steht jeweils dabei.

### Hoch

| Datei | Stelle | Problem | Status |
|---|---|---|---|
| `lectures/lec_04_scheduling.qmd` | Johnson „Optimal Solution" | Gesamtzeit 4 h 20 falsch (richtig 250 min), Grafik zeichnete C-Trocknen 30 statt 20 min | erledigt: 4 h 10 min, Grafik per Code aus der Tabelle (739fc03) |
| `lectures/lec_05_randomness.qmd` | „Time and Space Requirements" | 77 Milliarden statt 77 Millionen Jahre | erledigt (00a3e7f) |
| `lectures/lec_01_optimal_stopping.qmd` | „Why 37%?", Simulationsfolie | 37 % über „geometric distribution" begründet | erledigt: Herleitung über −x·ln x, Folie „Simulation: Success Rate by Stopping Point" (6031e84) |
| `lectures/lec_01_optimal_stopping.qmd` | „Step-by-step Approximation" | 1/n als Erfolgschance der Strategie lesbar | erledigt: „Why not pick at random?" mit Kontrast (6031e84) |
| `lectures/lec_01_optimal_stopping.qmd` | Zelle „Computing the number" | Ausgabe 0.368% | erledigt: 36.8% (6031e84) |
| `lectures/lec_02_explore_exploit.qmd` | Bellman II bis III | Laplace-Regel als Bellmans Strategie dargestellt | erledigt: eigener Teil „A simple estimate: Laplace's rule of succession", Bellman nur Rückwärtsrechnung (ae40a7e) |
| `lectures/lec_04_scheduling.qmd` | Priority Inversion/Inheritance | Prioritätsskala widersprüchlich | erledigt: 1 = höchste, A erbt 1 (4ec220b) |
| `index.qmd`, `lec_00_introduction.qmd` | Abgaberegeln | widersprüchlich | erledigt nach KLU-Syllabus (7a3abf8) |
| `tutorials/tut_05_02_recap.qmd` | Exercise 4.1, Test | erwartete 4 statt 5 Spalten | erledigt, Spalten in der Aufgabe benannt (1cad20e) |
| `tutorials/tut_03_03_packages.qmd` | uv-Befehle | `uv update` existiert nicht | erledigt (1cad20e) |
| `tutorials/tut_03_01_recap.qmd` | Eviction-Beispiel | Gegenteil von LRU | erledigt im LRU-Umbau (8802dee) |
| `lectures/lec_05_randomness.qmd` | „After the break" | aus Lecture IV kopiert | erledigt (00a3e7f) |
| *neu gefunden* `lectures/lec_01_optimal_stopping.qmd` | „Rejection" | In q^(1/(1−q)) ist q die **Annahme**-, nicht die Ablehnungswahrscheinlichkeit (bei q → 1 ergibt sich 1/e) | erledigt (00fca45) |
| *neu gefunden* `lectures/lec_04_scheduling.qmd` | „Lawler's Solution" | Grafik zeigte A D B C E statt D B A C E von der Folie | erledigt, Grafik per Code (220b72c) |
| *neu gefunden* `tutorials/tut_05_02_recap.qmd` | alte Routenaufgabe | Test `min_cost < 6000` bei 10 Versuchen lehnte rund 38 % der korrekten Lösungen ab | erledigt im Monte-Carlo-Umbau (3504308) |
| *neu gefunden* `tutorials/tut_02_03_explore_exploit.qmd` | Exercise 2.1, Test | Grenze 60 Spiele lehnte korrekte Lösungen ab (Rate 1,8 ergibt im Mittel rund 90) | erledigt (7a8a485) |
| *neu gefunden* `projects/stocks_streamlit.py` | Kennzahlen | `['Close'][-1]` wirft unter pandas 3 KeyError | erledigt (163d556) |

### Mittel

| Datei | Problem | Status |
|---|---|---|
| `general/syllabus.qmd`, `index.qmd` | Syllabus versprach Inhalte, die fehlten | erledigt: Inhalte ergänzt (LRU in III, Monte Carlo in V, Fairness in VI) und Syllabus/Startseite angeglichen; Game Theory bleibt als Ausblick (8802dee, 3504308, ae5a422, 6ec996d) |
| alle | „we/us" trotz Einzel-Lehrendem | **nicht umgesetzt**, Vorgabe: Sprecherperspektive „we" bleibt |
| `general/uv.qmd` | veraltete `uv init`-Ausgabe, Python 3.12 | erledigt: aktuelles Template, Python 3.13, `uv python pin` (66d8256) |
| `lec_00_introduction.qmd` | Modellliste veraltet | erledigt: „current AI assistants such as Claude, ChatGPT or Gemini", auch Startseite und Tutorial-Abschluss (66d8256) |
| `tut_05_02_recap.qmd` | Cursor-Kürzel | erledigt: werkzeugneutral, Copilot, Cursor, Claude Code (66d8256) |
| `tut_04_03_dataframes.qmd`, Cheatsheet | Conda-Reste | erledigt (66d8256) |
| `lec_02_explore_exploit.qmd` | Schreibweise, Nummerierung I/II/III/IV/VI | erledigt: „Explore & Exploit" (auch Sidebar), sprechende Folientitel (2eddd4b) |
| `lec_01_optimal_stopping.qmd` | doppelte Folien | erledigt: zusammengelegt (00fca45) |
| `lec_01_optimal_stopping.qmd` | „After the break" | erledigt (00fca45) |
| `lec_03_caching.qmd` | Zahlen ohne Quelle, Poisoning-Definition | erledigt: Quellen oder Größenordnung, Poisoning = falsche Daten (d3d4682) |
| `lec_04_scheduling.qmd` | „Industrial Revolution", Mermaid-YAML, Folie „Questions & Discussion" | erledigt (e8e914a, c5807e2) |
| alle Lectures | Literaturfolien doppelt, Ferguson ohne Bezug | erledigt: gemeinsame Includes, Ferguson nur in Lecture I (c5807e2) |
| `tut_02_01_lists.qmd` | Schleife vor II.II | erledigt: Hinweis auf Vergleiche/`max()` (fc33ab5) |
| `tut_03_03_packages.qmd` | Schlusssatz | erledigt (8802dee) |
| `tut_04_01_recap.qmd` | Test überschreibt Listen | erledigt (fc33ab5) |
| `tut_04_02_dicts.qmd` | `del()`, 2023, Testzellen offen | erledigt (fc33ab5) |
| `tut_05_03_free.qmd` | Überschrift für Nicht-Pygame-Projekte | erledigt (fc33ab5) |
| `general/cheatsheet.qmd` | Dictionaries und DataFrames fehlten | erledigt (a350eab) |
| `general/faq.qmd` | PDF-Weg | erledigt (a350eab) |
| `pyproject.toml` | veraltete Pakete | erledigt: aktualisiert und alles neu ausgeführt (66d8256) |
| `lec_02_explore_exploit.qmd` | Hollywood endet 2011 | erledigt: 2024 9 von 10 (Box Office Mojo, US domestic; *Twisters* als Fortsetzung gezählt, *Wicked* nicht) (2eddd4b) |
| `tut_01_02`, `tut_01_03` | Testmeldungen | erledigt (fc33ab5, 7a8a485) |

### Niedrig

Alle erledigt: Simulation in Lecture I mit Seed und 2.000 Durchläufen (00fca45), „37%" einheitlich, Fußnoten benannt (00fca45), Frage nicht mehr als Folientitel und Summary getrennt (2eddd4b), „Preventing Thrashing: …" (e8e914a), leerer Pausenmarker in Lecture V (580fe95), Caching-Beschreibung in Lecture VI (e8e914a), `popped_song` (8802dee), `deadlines` statt `priorities` (fc33ab5), „Exercise 5.1" in V.II (3504308), Satz in V.III (fc33ab5), Einleitung I.I (fc33ab5), Zingaro-Verlagsort (a350eab).

## 3. Überarbeitung Runde 2 (11. Oktober 2026)

### Neue Inhalte

- **Tutorials III:** eigener LRU-Cache als roter Faden. III.I: LRU-Liste, Cache-Hit, Übungen 3.2 (ein LRU-Schritt) und 4.2 (Treffer zählen). III.II: `lru_access()` und `hit_rate()`. III.III: `random_access()`, Vergleich LRU gegen Zufall mit `random` (LRU 71,9 % Treffer), `functools.lru_cache`. IV.II: LRU-Cache mit einem Dictionary.
- **Block V:** Lecture V „Monte Carlo in Business" und „Will the Project Finish on Time?" (10.000 simulierte Projekte, 63 % pünktlich, obwohl die wahrscheinlichsten Dauern 21 von 25 Tagen ergeben). Tutorial V.II: Routenaufgabe als Monte-Carlo-Simulation mit Schätzung der erwarteten Kosten.
- **Lecture VI:** „Fairness in Algorithms", „Where Bias Comes From", „Kind Algorithm Design".

### Kürzungen (Wörter sichtbarer Text, vorher → nachher)

| Deck | Folie | Wörter | Was entfiel |
|---|---|---|---|
| Lecture I | The Secretary Problem | 64 → 52 | Hinweis zum Namen auf einen Satz |
| Lecture I | Look-and-Leap Strategy (2 Folien) | 105 → 62 | doppelte Folie, Fußnote präzisiert |
| Lecture I | Rejection / Mutual Rejection | 100 → 61 | doppelte Folie |
| Lecture I | Time Constraints | 55 → 50 | Satz zu Ressourcenallokation |
| Lecture II | The problem with exploitation / exploration | 45 → 27, 56 → 35 | je ein Beispielsatz |
| Lecture II | Multi-Armed Bandit Problem II | 45 → 33 | Satzform in Stichpunkte |
| Lecture II | Interactive Casino Challenge + Follow-up | 2 Folien → 1 | gleiche Tabelle zweimal |
| Lecture II | Expected value for a decision | 44 → 25 | Herleitung gestrafft |
| Lecture II | The influence of the interval | 57 → 41 | Satzform in Stichpunkte |
| Lecture II | A Possible Explanation | 68 → 42 | Wiederholungen |
| Lecture II | Win-Stay Lose-Shift | 71 → 29 | Definition doppelt |
| Lecture II | Win-Stay = No Brainer? / Lose-Shift | 38 → 23, 53 → 29 | Beispiel gestrafft |
| Lecture II | The Gittins Index I / II / III | 53 → 31, 69 → 23, 45 → 27 | Annahmen-Details |
| Lecture II | What is Discounting? | 58 → 25 | Unterpunkte zusammengefasst |
| Lecture II | Question (Gittins) | 53 → 30 | Konvergenz-Detail |
| Lecture II | The Scary Math | 48 → 35 | drei Stichpunkte im Callout zusammengefasst |
| Lecture II | Explore vs Exploit: Mathematically | 50 → 20 | Formulierungen |
| Lecture II | Personal Action Plan | 2 Callouts → Frageliste + 1 Callout | vierte Dimension, drei der vier „Key Insights" |
| Lecture II | gesamt | 2304 → 1792 | |
| Einführung | Our Recommendation / Install VS Code | 66 → 48, 59 → 45 | Callout-Text |
| Lecture V | Selection Bias | 68 → 45 | Wald-Beispiel gestrafft |
| Tutorial V.I | What is GitHub Copilot? / Accept without reading? / Impact on Jobs | 74 → 43, 65 → 33, 57 → 39 | Callouts zusammengefasst |
| alle Lectures | Books on Programming | 67 → 50 | Callout gekürzt, im Include |

### Grafiken

| Datei | Entscheidung |
|---|---|
| `images/atlb/*.svg` (12 Scheduling-Diagramme) | per Code ersetzt (`helpers/course_plots.py`, Inter/Poppins, Farben aus `_brand.yml`), Ordner entfernt |
| `images/caching/lec03-tradeoff.png` (Speicherpyramide ohne Quelle) | per Code ersetzt (Zugriffszeiten nach Gregg 2020), entfernt |
| Lecture IV Mindmap (Mermaid) | bleibt Code, Theme `neutral` jetzt wirksam |
| Lecture I Erfolgsquote, Lecture V GIFs | waren schon Code |
| neu: Lecture V Projektsimulation | Code |
| Fotos in `images/bg/`, GIFs in `images/gif/`, Illustrationen `closet_*`, `Desk*`, `Bed.png`, `lec03-caching-photo.jpg` | bleiben (Fotos und Illustrationen) |
| `images/caching/motivation.png`, `images/nils-roemer.jpeg`, `images/tobias-vlcek.jpg` | werden nirgends verwendet, aber nicht ersetzt; bleiben, bitte selbst entscheiden |

### Werkzeuge

Python 3.13, `uv lock --upgrade` (numpy 2.5.4, pandas 3.0.6, matplotlib 3.11.2, jupytext 1.19.6, ipykernel 7.4.0, pillow 12.3.0). Inkompatibilitäten: in Lectures und Tutorials keine; im Projekt `stocks_streamlit.py` eine (behoben). Die GIFs in `animations/` ändern sich mit matplotlib 3.11/pillow 12 einmalig, zwei unabhängige Läufe ergeben identische Hashes. ipykernel 7 meldet beim Kernelstart „Kernel is running over TCP without encryption"; das ist eine Startmeldung von Quarto/Jupyter, keine Warnung aus dem Kurscode.

### Qualitätstest

- **Tutorials:** Alle 79 Übungszellen gelöst (Lösungen nur im Scratchpad, nicht committet), alle 71 Tests bestehen. Zusätzlich 30 typische Fehlerlösungen: alle werden abgelehnt, nachdem sechs Tests geschärft wurden (7a8a485). Zwei Tests lehnten korrekte Lösungen ab (II.III 2.1, alte V.II-Route), fünf ließen Fehler durch (I.II 3.2, I.III 5.1, II.I 2.1, IV.III 3.1, V.II 1.1).
- **Offene Übungen ohne harten Test:** I.III 1.1 (Ausgabe selbst prüfen), III.I 1.1/2.1/3.1 (eigene Werte), V.III (freie Projekte). Bewusst so gelassen.
- **projects/:** `jump-and-run.py` (pygame, headless mit simulierten Tasten), `tutorial_randomwalk.py` und `stocks_streamlit.py` (Streamlit AppTest mit echten Kursdaten) laufen mit Python 3.13.

### Entscheidungen

1. **Tutorials III arbeiten mit Listen, nicht mit Dictionaries:** Dictionaries kommen erst in IV.II. Der LRU-Cache mit Dictionary steht deshalb als Anschluss in IV.II.
2. **Literatur als zwei Includes** (`include/lecture_literature_start.qmd`, `include/lecture_literature_books.qmd`), damit Lecture I dazwischen die Ferguson-Folie zeigen kann.
3. **Grafik-Hilfsmodul** `helpers/course_plots.py` statt Code in jeder Folie: Folien enthalten nur einen Aufruf mit den Daten der Tabelle, Stil und Fonts kommen zentral.
4. **Fragen nach der Verspätung:** Die Grafiken auf diesen Folien zeigen Deadlines, aber nicht die Antwort.
5. **Hollywood 2024:** US-Inlandszahlen wie im Buch; *Twisters* zählt als Fortsetzung, *Wicked* nicht. Ohne *Twisters* wären es 8.
6. **Tests mit einem Szenario:** Wo ein Test nur ein Szenario prüfen kann, sind die Daten so gewählt, dass die häufigste Auslassung auffällt.
7. **Gittins-Tabelle:** Werte wie im Buch (Diskontfaktor 0,9), nicht neu berechnet.

## 4. Gesamteinschätzung

Der Kurs war inhaltlich tragfähig, hatte aber in Lecture I, II und IV echte Fachfehler und in Lecture II zu viel Text. Nach Runde 2 sind alle bekannten Fehler behoben, die Syllabus-Versprechen sind durch echte Inhalte gedeckt (LRU-Cache, Monte Carlo, Fairness), und die Tutorials sind durchgängig getestet. Die größten verbleibenden Hebel liegen nicht mehr in Korrekturen, sondern im Feinschliff einzelner Folien im Probelauf vor Kursstart.

## 5. Empfehlungen für den neuen Durchlauf

1. **Probelauf der Lectures II und IV** im Hörsaal-Format: beide Decks haben die meisten neuen Folien und Grafiken.
2. **Zeitbedarf der Tutorials III messen:** durch den LRU-Faden haben sie vier neue Übungen.
3. **Gittins-Werte und Hollywood-Zahl gegenlesen**, falls du andere Quellen bevorzugst.
4. **Ungenutzte Bilder** (`motivation.png`, Porträts) behalten oder löschen.
5. **Abhängigkeiten zum Semesterende** noch einmal mit `uv lock --upgrade` prüfen und den Komplett-Render laufen lassen.

## 6. Abschlussprüfung

- **Komplett-Render** ohne Ausführungs-Cache (`_freeze/` gelöscht, `uv run quarto render`): Exit 0, keine Warnungen aus dem Kurscode; danach Lectures III bis V nach der Grafik-Anpassung erneut ausgeführt, ebenfalls fehlerfrei.
- **Überlaufprüfung** aller acht Decks, normale Ansicht und `?print-pdf`: kein Überlauf, keine Footer-Berührung, keine Folie mit zwei Druckseiten. Einzige Meldung ist das bekannte Messartefakt des Kopieren-Buttons (8 px) auf drei Codefolien. Messung in `screenshots-review/inhalt/messung.json`.
- **Screenshots** der 55 geänderten oder neuen Folien in `screenshots-review/inhalt/` (gitignored).
- **Animationen:** Lecture V erzeugt die GIFs mit festem Seed; zwei vollständige Läufe ergeben identische Dateien.
- **Hinweis ohne Änderung:** Die Aufgaben-Tabellen in Lecture IV stehen in ```` ```python ````-Blöcken, die Syntaxfärbung markiert deshalb „min" rot. Das war schon vorher so; als ```` ```text ```` wären sie neutral.
