# REVIEW.md: Inhaltliche Prüfung vor dem Kursstart

Stand: 10. Oktober 2026, Branch `inhalt-review` (von `main` 51b9446). Geprüft: alle Lectures, Tutorials, Website-Seiten (Startseite, Syllabus, FAQ, Installation, Literatur, Cheatsheet), Rechtstexte nur gelesen. Alle Code-Zellen wurden einmal komplett ausgeführt (`_freeze/` leer, `uv run quarto render`, Exit 0, keine Warnungen im Log, keine stderr-Ausgaben in den gerenderten Seiten). Links und Bildverweise automatisch geprüft (40 externe Links, 0 fehlende lokale Verweise).

Prioritäten: **hoch** = fachlich falsch oder kaputt, **mittel** = veraltet oder inkonsistent, **niedrig** = Stil.

## 1. Direkte Korrekturen (committet)

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

Nicht geändert, obwohl eindeutig (Inhalt oder Code-Ausgabe, deine Entscheidung): siehe Befunde „hoch".

## 2. Befunde

### Hoch

| Datei | Stelle | Problem | Vorschlag |
|---|---|---|---|
| `lectures/lec_04_scheduling.qmd` | „Optimal Solution" und `images/atlb/atlb_schedule-johnson-optimal.svg` | Gesamtzeit „4 hours 20 minutes" ist falsch. Mit den Tabellenwerten (C trocknet 20 min) ergibt B A D C 250 min = 4 h 10 min (nachgerechnet, über alle 24 Reihenfolgen minimal). Die Grafik zeichnet C im Trockner 30 min lang und beschriftet 260 m. | Text auf „4 hours 10 minutes", Grafik korrigieren (C-Trocknen 2 Kästchen, Ende 250). Alternativ C-Trocknen in der Tabelle auf 30 min setzen, dann stimmt 260, die Suboptimal-Variante wird 320. |
| `lectures/lec_05_randomness.qmd` | „Time and Space Requirements" | „20! … would take 77 **billion** years at 1 ms per check": 2,43·10¹⁸ ms ≈ 7,7·10⁷ Jahre = 77 **Millionen** Jahre. | „77 million years". |
| `lectures/lec_01_optimal_stopping.qmd` | „Why 37%?" und Folientitel „Geometric Distribution" | Das 37-%-Ergebnis hat nichts mit der geometrischen Verteilung zu tun (es folgt aus der Maximierung von −x·ln x, Ferguson 1989). Die Simulationsfolie heißt ebenfalls „Geometric Distribution", zeigt aber Erfolgsquoten je Stopp-Position. | Satz „This is based on the geometric distribution" streichen, Folie umbenennen in „Simulation: Success Rate per Stopping Position". |
| `lectures/lec_01_optimal_stopping.qmd` | „Step-by-step Approximation" | Die Reihe 100 %, 50 %, 33 %, … (1/n) ist die Trefferchance bei **zufälliger** Wahl, nicht die „success probability" der Strategie (die fällt nicht auf 20 %, sondern konvergiert gegen 37 %). Der Folientext legt Letzteres nahe. | Umformulieren: „Chance of picking the best by random choice", danach der Kontrast zur 37-%-Strategie. |
| `lectures/lec_01_optimal_stopping.qmd` | Zelle „Computing the number" | Ausgabe lautet `Percentage of options to look at: 0.368%`, Einheit falsch. | `{percentage:.1%}` → `36.8%`. Code-Ausgabe, deshalb nicht geändert. |
| `lectures/lec_02_explore_exploit.qmd` | „The Bellman approach II", „Question time", „Bellman approach III" | (w+1)/(w+l+2) ist die Laplace-Regel (Schätzer für die Gewinnwahrscheinlichkeit), nicht Bellmans „optimale Strategie". Bellmans Beitrag ist die Rückwärtsrechnung bei bekanntem Horizont (Folie I und IV beschreiben das richtig). Das Buch führt die Formel nur als Faustregel ein. | Die drei Folien als „A simple estimate (Laplace's rule of succession)" abtrennen und bei Bellman nur die Rückwärtsinduktion lassen. |
| `lectures/lec_04_scheduling.qmd` | „Priority Inversion" / „Priority Inheritance" | Prioritätsskala widersprüchlich: Tabelle A 3, B 1; Text „A gets the highest priority from B" setzt 1 = höchste voraus; nach der Vererbung steht A 3, B 3. Ist 1 die höchste Priorität, müsste A auf 1 steigen; ist 3 die höchste, hätte A schon die höchste und es gäbe keine Inversion. | Skala festlegen (1 = höchste) und Tabelle nach Vererbung auf A 1, B 1 setzen. |
| `index.qmd` vs. `lectures/lec_00_introduction.qmd` | „Course Structure" vs. „Passing the Course" / „Handing in Assignments" | Abgaberegeln widersprechen sich: Startseite „assignments from 2 out of the 5 tutorials … due by the end of the quarter"; Einführung „assignments of at least two lectures … due at the beginning of the next lecture", „You have to pass at least twice". Außerdem gibt es 15 Tutorials in 5 Teilen, nicht „5 tutorials". | Eine Regel festlegen und an beiden Stellen gleich formulieren („two of the five tutorial parts", Frist). |
| `tutorials/tut_05_02_recap.qmd` | Exercise 4.1, Test | `assert schedule_df.shape == (5, 4)` passt nicht zur Aufgabe: Spalten aus dem Dictionary (name, duration, due_time) plus start und end sind 5 Spalten. Korrekte Lösungen fallen durch. | Erwartung auf (5, 5) ändern oder nur eine Spalte `end_time` verlangen. |
| `tutorials/tut_03_03_packages.qmd` | Section 3, Liste der uv-Befehle | „Update dependencies (`uv update`)": den Befehl gibt es nicht. | `uv lock --upgrade` und `uv sync` (oder `uv sync --upgrade`); `uv self update` aktualisiert uv selbst. |
| `tutorials/tut_03_01_recap.qmd` | Section 2, Beispiel „Simple cache eviction policy" | Regel `access_count > 10 and last_accessed_minutes < 30 → evict` wirft genau das häufig und kürzlich genutzte Element raus, das Gegenteil von LRU aus der Vorlesung. | Bedingung umdrehen (`access_count < 10 and last_accessed_minutes > 30`), Text anpassen. |
| `lectures/lec_05_randomness.qmd` | „After the break: Randomness" | Bullets aus Lecture IV kopiert („Different scheduling algorithms applied to problems"). | Auf Tutorial V.I (Programming with AI) und V.II verweisen. |

### Mittel

| Datei | Stelle | Problem | Vorschlag |
|---|---|---|---|
| `general/syllabus.qmd`, `index.qmd` | Programming-Zeilen, Lecture VI, Kursbeschreibung | Syllabus verspricht „Implementing an LRU cache" (III), „Monte Carlo simulation" (V), „Algorithms for social good, Ethical considerations" (VI); die Tutorials III sind Recap/Funktionen/Pakete, V.II zieht nur zufällige Routen, Lecture VI ist Computational Kindness plus Ausblick. Startseite nennt „game theory" als Thema, das nur im Ausblick vorkommt. | Syllabus-Zeilen an den Inhalt anpassen (III: „Functions and packages", V: „Random sampling and AI-assisted coding", VI: „Computational kindness, outlook, presentations"), „game theory" auf der Startseite streichen oder durch „randomness" ersetzen. |
| alle Lectures, `include/tutorial_end.qmd`, `general/syllabus.qmd` | „we/us/our" | Seit Juli 2026 ein Lehrender; FAQ und Startseite sagen „me", Folien „we will help you", „Ask us!", „Provide us", „We were rather ambitious", „We have read it and discussed it in depth". | Sprecherperspektive festlegen (Vorschlag: „I" für den Lehrenden, „we" nur für „wir im Kurs") und einmal durchgehen. |
| `general/uv.qmd` | „Run the starter script", „What does that code mean?", „Install Python" | `uv init` (uv 0.11) erzeugt `print("Hello from <projekt>!")` und zusätzlich ein Git-Repo; Seite zeigt „Hello World!" / `print("Hello, World!")`. Python 3.12 „for the course this year": 3.12 ist 2026 im Security-only-Status. | Ausgabe und Codebeispiel auf das aktuelle uv-Template bringen; Python-Version prüfen (3.13 oder 3.14, dann auch `requires-python` in `pyproject.toml`). |
| `lectures/lec_00_introduction.qmd` | „Help from AI" | Modellliste „Claude, ChatGPT, LLama3" veraltet. | „Claude, ChatGPT, Gemini" oder allgemein „current AI assistants". |
| `tutorials/tut_05_02_recap.qmd` | Callout „How to start with AI pair programming" | Beschreibt Cursor-Shortcuts (Ctrl+L, Ctrl+K); Tutorial V.I und V.III empfehlen VS Code mit Copilot. | Auf Copilot Chat umschreiben (Chat öffnen, Inline-Chat, Tab zum Annehmen) oder Cursor-Hinweis als Alternative kennzeichnen. |
| `tutorials/tut_04_03_dataframes.qmd`, `general/cheatsheet.qmd` | Installationshinweis | `conda install pandas` / „If you are using Miniconda": der Kurs nutzt nur uv. | Conda-Zeilen entfernen. |
| `lectures/lec_02_explore_exploit.qmd` | Titel, Folien „Multi-Armed Bandit …" | „Explore Vs. Exploit" (Titel) vs. „Explore & Exploit" (Einführung, Syllabus) vs. „Explore/Exploit" (Sidebar). Folien nummeriert I, II, III, IV, VI (V fehlt). | Einheitlich „Explore & Exploit"; Folien durchnummerieren. |
| `lectures/lec_01_optimal_stopping.qmd` | „Look-and-Leap Strategy" (2×), „Rejection" / „Mutual Rejection" | Je zwei Folien mit fast identischem Inhalt. | Je eine streichen (kürzt das Deck um zwei Folien). |
| `lectures/lec_01_optimal_stopping.qmd` | „After the break: Optimal Stopping" | Titel nennt Optimal Stopping, Inhalt beschreibt die Python-Session. | „After the break: First Steps in Python". |
| `lectures/lec_03_caching.qmd` | „Learning from Computer Science", „Why the Trade-off?", „Why LRU Works", „Cache Vulnerabilities" | Zeitangaben unscharf (1950s, Moore's Law 1965, „Memory Wall" 1994); „SRAM $50,000/GB", „80-90 % hit rate (vs. 50-60 % random)" ohne Quelle; „Cache Poisoning: insert malicious data to evict" beschreibt eher Flooding, Poisoning heißt falsche Daten einschleusen (DNS). | Zahlen mit Quelle versehen oder als Größenordnung kennzeichnen; Poisoning-Definition korrigieren. |
| `lectures/lec_04_scheduling.qmd` | „Industrial Revolution", YAML-Header, „Questions & Discussion" | Gantt-Chart um 1910 liegt nach der Industriellen Revolution. `format.revealjs.html.mermaid.theme` ist falsch verschachtelt und wirkungslos. Die Folie „Questions & Discussion" enthält nur den Think-Python-Hinweis (Kopierfehler aus „Books on Programming"). | „Industrialization"; `mermaid: theme: neutral` direkt unter `revealjs`; Folie mit „Books on Programming" zusammenlegen. |
| alle Lectures | „Interesting literature to start", „Books on Programming" | Identische Literaturfolien in jedem Deck, Lectures II und III zitieren Ferguson (Secretary Problem) ohne Bezug. | Einen Include `include/lecture_literature.qmd` nutzen, Ferguson nur in Lecture I. |
| `tutorials/tut_02_01_lists.qmd` | Exercise 2.1 | „Keep track of the highest rating" verlangt faktisch eine Schleife; Schleifen kommen erst in II.II. Mit drei Einträgen geht es auch mit if-Vergleichen, das sagt die Aufgabe aber nicht. | Hinweis „use comparisons, loops come next" ergänzen oder Aufgabe nach II.II verschieben. |
| `tutorials/tut_03_03_packages.qmd` | Schlusssatz | Verspricht „read and write files … tabular data"; IV.I bis IV.III behandeln Recap, Dictionaries, DataFrames, keine Dateien. | „dictionaries and tabular data with pandas". |
| `tutorials/tut_04_01_recap.qmd` | Tests zu Exercise 2.1 und 3.1 | Test 3.1 überschreibt `drinks` mit 3 Einträgen; ein erneuter Lauf von Test 2.1 (`len(drinks) >= 5`) scheitert danach. | In Test 3.1 `test_names`, `test_drinks` verwenden. |
| `tutorials/tut_04_02_dicts.qmd` | Section 1, Exercise 2.3, Tests | `del()` als Funktion erklärt (`del` ist eine Anweisung). Beispieldaten „2023-12-31". Testzellen ohne `#| code-fold: true`, anders als in allen anderen Tutorials. | `del tasks["…"]`; Daten auf 2026/2027; code-fold ergänzen. |
| `tutorials/tut_05_03_free.qmd` | Überschrift „Pygame Games" | Projekte 5 bis 8 (Tic-Tac-Toe im Terminal, OCR, Streamlit) stehen unter „Pygame Games". | Zweite Überschrift „Other Projects". |
| `general/cheatsheet.qmd` | Umfang | Endet bei Paketen: keine Dictionaries, keine DataFrames (Tutorials IV.II, IV.III), Abschnitt „Tuple unpacking: Structure" leer. | Zwei Abschnitte ergänzen, leeren Punkt füllen. |
| `general/faq.qmd` | „How can I download PDF slides" | Beschreibt den Reveal-Menü-Weg; jede Lecture-Seite hat inzwischen einen direkten PDF-Link (Typst). | Beide Wege nennen. |
| `pyproject.toml` / `uv.lock` | Abhängigkeiten | Veraltet, nicht aktualisiert (siehe Tabelle unten). pandas 3.0 ist ein Major-Release (String-Dtype, Copy-on-Write), IV.III und V.II vor einem Upgrade testen. | Nach dem Review gezielt `uv lock --upgrade` und Tutorials IV.III, V.II, Lectures I und V neu ausführen. |
| `lectures/lec_02_explore_exploit.qmd` | „Hollywood's Strategy" | Tabelle endet 2011 (Buchstand). | Zeile 2021 oder 2025 ergänzen, Quelle nennen. |
| `tutorials/tut_01_02_comparisons.qmd`, `tut_01_03_stopping.qmd` | Testmeldungen | „as his salary expectation" (Exercise 3.1); Meldung in 5.1 („searching for 4 weeks") passt nicht zur Aufgabe. | „their"; Meldung anpassen. |

### Niedrig

| Datei | Stelle | Problem | Vorschlag |
|---|---|---|---|
| `lectures/lec_01_optimal_stopping.qmd` | Simulationszelle | Kommentar „first stopping_position-1 candidates" vs. Schleife über `stopping_position`; kein Seed, Abbildung ändert sich je Lauf; 20 × 10.000 Durchläufe dauern spürbar. | Seed setzen, Kommentar angleichen, 2.000 Durchläufe. |
| `lectures/lec_01_optimal_stopping.qmd` | durchgehend | „37 %" und „37%" gemischt; Fußnoten [^1], [^8], [^4] unsystematisch. | Eine Schreibweise. |
| `lectures/lec_02_explore_exploit.qmd` | „## [Question:]{.question} Do you have any examples…", „Explore vs Exploit: Summary" | Frage als Folientitel; Abschnitts- und Folientitel identisch. | Titel „Examples from your life", Folie „Summary I". |
| `lectures/lec_04_scheduling.qmd` | „Preventing Thrashing Strategic/Tactical" | Doppelpunkt fehlt. | „Preventing Thrashing: Strategic". |
| `lectures/lec_05_randomness.qmd` | „## Randomness" | Pausenmarker am Folienende ohne Inhalt danach. | Marker streichen. |
| `lectures/lec_06_kindness.qmd` | „Topics from the Lecture" | „Caching: … by sticking to a task" trifft den Inhalt von Lecture III nicht. | „Keeping what you use and letting go of the rest". |
| `tutorials/tut_03_01_recap.qmd` | Section 3 | Variable `poped_song`. | `popped_song`. |
| `tutorials/tut_04_03_dataframes.qmd` | „Accessing Columns" | `priorities = tasks.deadline`, Ausgabe „Priorities". | `deadlines`. |
| `tutorials/tut_05_02_recap.qmd` | Section 5 | Aufgabe ohne „Exercise 5.1"-Überschrift; Lösung braucht `sorted(key=…)` oder Permutationen, die nie eingeführt wurden (ist als KI-gestützte Aufgabe vertretbar). | Überschrift ergänzen. |
| `tutorials/tut_05_03_free.qmd` | Einleitung | „put some time 2-3 hours outside of class". | „spend two to three hours outside of class". |
| `tutorials/tut_01_01_variables.qmd` | Einleitung | „Let's learn how to use Python to help us in order to make better dating decisions". | „…to make better dating decisions". |
| `general/literature.qmd` | Zingaro | „AU: No Starch Press" (Verlag sitzt in San Francisco). | „San Francisco: No Starch Press". |

**Folien mit viel Text (Kandidaten zum Kürzen, Wörter sichtbarer Text):** Lecture II „Win-Stay Lose-Shift" (73), „The Gittins Index II" (70), „A Possible Explanation" (69), „The Bellman approach I" (67), „Gittins Index: The Scary Math" (64), „What is Discounting?" (59), „Your Personal Action Plan" (zwei Callouts), „Interactive Casino Challenge" und „Follow-up" (gleiche Tabelle zweimal); Lecture I „The Secretary Problem" (68), „Look-and-Leap Strategy" (63), „Time Constraints" (58); Lecture V „Selection Bias" (71); Tutorial V.I „What is GitHub Copilot?" (77), „Accept without reading?" (66), „Impact on Jobs" (63); Einführung „Our Recommendation" (71), „Install VS Code" (62), „Handing in Assignments" (58); in jedem Deck „Books on Programming" (69, Volltitel der Zitate).

**Links:** alle lokalen Verweise vorhanden. Extern 36 × 200, `cursor.sh` korrigiert. Nicht per Skript erreichbar, im Browser aber in Ordnung: `openai.com/index/strengthening-chatgpt-responses…` (403, Bot-Schutz) und die acht Unsplash-Fotografenlinks (401, Bot-Schutz).

**Python-Abhängigkeiten (gesperrt vs. PyPI am 10.10.2026, nicht aktualisiert):**

| Paket | uv.lock | aktuell |
|---|---|---|
| numpy | 2.3.2 | 2.5.4 |
| pandas | 2.3.2 | 3.0.6 (Major) |
| matplotlib | 3.10.6 | 3.11.2 |
| jupytext | 1.17.3 | 1.19.6 |
| jupyter | 1.1.1 | 1.1.1 |
| ipykernel | 6.30.1 | 7.4.0 (Major) |
| jupyterlab | 4.4.6 | 4.6.4 |
| notebook | 7.4.5 | 7.6.3 |
| pillow | 11.3.0 | 12.3.0 (Major) |

## 3. Gesamteinschätzung

Der Kurs ist inhaltlich tragfähig und didaktisch gut aufgebaut: Jede Lecture hat einen klaren Alltagsbezug, die Tutorials führen Python in kleinen, getesteten Schritten ein und greifen das Vorlesungsthema auf. Die Qualität schwankt zwischen den Teilen. Lecture II ist am textlastigsten und hat die meisten Unschärfen (Bellman vs. Laplace, Nummerierung), Lecture IV ist am dichtesten und enthält zwei Rechenfehler, Lectures III, V und VI sind rund. Die Tutorials I bis IV sind solide; V.II und V.III setzen auf KI-gestütztes Arbeiten und sind entsprechend offener. Die größten Risiken für den neuen Durchlauf sind die widersprüchlichen Abgaberegeln, die Abweichung zwischen Syllabus und tatsächlichen Tutorial-Inhalten und die veralteten Tool-Angaben (uv-Ausgabe, Python-Version, Cursor vs. Copilot).

## 4. Die fünf wichtigsten Empfehlungen

1. **Abgaberegeln und Syllabus festziehen.** Eine Regel für Abgaben (welche Tutorials, welche Frist, Gruppengröße) auf Startseite und Einführungsfolien, Syllabus-Zeilen an die realen Tutorial-Inhalte anpassen, „game theory" streichen.
2. **Die vier fachlichen Fehler beheben:** Johnson-Gesamtzeit und Grafik (4 h 10), 77 Millionen Jahre, 37-%-Herleitung ohne „geometric distribution", Bellman-Folien von der Laplace-Regel trennen. Dazu die Prioritätsskala bei Priority Inheritance und den Test in Tutorial V.II.
3. **Werkzeuge auf Stand bringen:** uv-Seite gegen das aktuelle `uv init` prüfen, Python-Version entscheiden, Copilot statt Cursor in V.II, Conda-Reste entfernen, Modellliste in der Einführung. Danach Abhängigkeiten gezielt aktualisieren und die Tutorials mit pandas 3 testen.
4. **Sprecherperspektive vereinheitlichen** („I" statt „we/us"), passend zur Übernahme durch einen Lehrenden; dabei die doppelten Folien in Lecture I und die Literaturfolien in einen Include ziehen.
5. **Lecture II entschlacken:** Folien mit über 60 Wörtern kürzen, Casino-Tabelle nur einmal zeigen, „Personal Action Plan" auf einen Callout reduzieren, Folien durchnummerieren. Das ist das Deck, bei dem Kürzen am meisten bringt.
