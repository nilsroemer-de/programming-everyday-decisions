# RAHMUNG.md: Lectures nach „Say what you're going to say" und „Speak simply, think deeply"

Stand: 14. Oktober 2026, Branch `inhalt-review` (Runde 3 nach REVIEW.md). Nicht gemergt, nicht veröffentlicht. Je Lecture ein Commit, dazu ein Technik-Commit und ein Abschluss-Commit.

## Technik

**Stand 27. Oktober 2026 (zweite Nachschärfung):** Die Rahmenfolien stehen jetzt ausgeschrieben in jeder Lecture-Datei (gleicher Text, gleiche Klassen, gleiches Aussehen wie vorher automatisch erzeugt), die Felder `lecture-*` im Kopf und der Filter `helpers/lecture-frame.lua` sind entfernt. Die Abschnittsüberschriften `# … {.title visibility="hidden"}` bleiben für die HTML-Seite stehen und sind in RevealJS unsichtbar. Übrig bleibt der kleine Filter `helpers/speaker-notes.lua` für die Notizen (HTML-Seite: Block „Notes", PDF und md: entfernt). Das Prüfskript meldet Abweichungen nur noch als Hinweise. Der folgende Abschnitt beschreibt den Zwischenstand mit Filter.


- **`helpers/lecture-frame.lua`** (Lua-Filter, projektweit in `_quarto.yml`): liest `lecture-summary`, `lecture-why`, `lecture-roadmap`, `lecture-covered`, `lecture-key` aus dem YAML-Kopf und erzeugt in RevealJS die Folien „Today in one sentence" (summary mit „Why it matters"), „Roadmap", danach direkt den Inhalt von Abschnitt 1; Abschnitt 2 und 3 beginnen mit genau einer Roadmap-Folie (aktueller Punkt in Ink, andere gedämpft, Nummern in Space Mono), die die Abschnittstitelfolie ersetzt (Nachschärfung vom 27. Oktober; auf der HTML-Seite bleiben die `#`-Überschriften), je Abschnitt eine Folie mit dem covered-Satz (Titel = Roadmap-Punkt, Eyebrow „What we covered"), und an der Marke `::: {.lecture-closing}` die Folien „What we covered" (drei Sätze mit Roadmap-Punkt als Eyebrow), „Why it matters" (why) und die Kernbotschaft als Loud-Slide. Auf der HTML-Seite: summary fett, why, Roadmap als Liste oben; „What we covered" plus Kernbotschaft an der Marke. Sprechernotizen (`::: {.notes}`) werden auf der HTML-Seite zum Block „Notes" (sky-100, kleiner Eyebrow), im PDF und md entfallen sie. Eine Änderung im Kopf genügt, nichts ist von Hand nachgebaut.
- **Warum Filter und nicht Shortcode:** Ein Shortcode müsste an mehreren Stellen im Text stehen (Eröffnung, jede Abschnittsfolie, jedes Abschnittsende, Abschluss). Der Filter findet Abschnittsanfang und -ende selbst über die `#`-Überschriften; im Text bleibt nur die eine Abschlussmarke.
- **`helpers/check_lecture_frame.py`:** meldet je Lecture fehlende Felder, Anzahl und Titel der Abschnitte (müssen exakt der Roadmap entsprechen), fehlende Abschlussmarke, Folien über 40 Wörter sichtbaren Textes (Code, Notizen, Fußnoten, Bildnachweise und Tabellenzeilen zählen nicht) und Folien ohne Titel (Loud- und Fotofolien getrennt als „untitled by design").
- **Stil** in `styles.scss` (Block „Lecture frame"): Eyebrow, Statement, Roadmap-Liste, covered-Folien, Notes-Block der HTML-Seite. Keine neuen Farben, Primärblau weiterhin nur für Fragen.
- **MathJax:** `assets/mathjax2/config/TeX-AMS_HTML-full.js` setzt `availableFonts: ["TeX"]`. Vorher fragte MathJax auf Rechnern mit installierter STIX-Schrift `fonts/STIX/fontdata.js` an (404, reproduziert in Lecture II und VI). Nach der Änderung: alle acht Decks ohne fehlgeschlagene Requests (`net404`-Prüfung per Chrome DevTools, jede Folie besucht).

## Änderungen je Lecture

Gemeinsam: alte Topic-, Agenda-, Learning-Objectives-, Key-Takeaways- und Summary-Folien entfallen, ihr Text steht in den Sprechernotizen der ersten bzw. letzten Inhaltsfolie. Unter-Abschnittsfolien (`#`) innerhalb eines Teils entfallen, weil nur drei `#`-Abschnitte erlaubt sind; die Orientierung gibt die Roadmap. Bilder, Animationen, Code, Formeln und Beispiele sind vollständig erhalten.

| Lecture | Abschnitte (= Roadmap) | Umstrukturierung | Beispiele für neue Titel | In Notizen verschoben |
|---|---|---|---|---|
| 00 Introduction | About this course / How to learn programming / Setting up Python | Agenda-Folie entfällt; „Using Notebooks with uv" in Teil 3 aufgegangen | „You learn Python in the tutorials", „Programming is like a new language", „AI is allowed, but learn yourself" | alte Agenda, Erklärungen zu Lecture/Tutorial/Difficulty, Python-Herkunft, Callout-Texte |
| I Optimal Stopping | The problem / The rule / Real life | Abschnitte „Optimal Stopping", „Secretary Problem", „Variations" neu zugeschnitten; „Building Your Technical Mindset" in „After the break" integriert; Key Takeaways entfallen | „Options come one by one, and there is no going back", „Look at the first 37 %, then leap", „If you can be rejected, leap earlier", „Picking at random gets worse with every candidate" | Topic, Objectives, Agenda, Takeaways, Herleitung von −x·ln x, Hinweis zur großen Kandidatenzahl, Parking-Lot-Nebenbemerkung |
| II Explore & Exploit | The dilemma / Time decides / Smart strategies | Teil 3 = Win-Stay, Laplace, Bellman, Gittins (wie vorgegeben); Summary-Folien zu „Which rule when?" plus Notizen; „The Scary Math" bleibt im Hauptteil mit Alltagssatz | „Long interval: explore. Short interval: exploit.", „Hollywood exploits: 9 of the top 10 films are sequels", „By the Gittins index, machine B wins", „A fair estimate: Laplace's rule of succession" | Trade-off-Callout, Bellman-Herleitung, Class-Discussion-Fragen, Situation/Anecdotally/Takeaways |
| III Caching | The problem / The solution / Your mind is a cache | Learning Objectives entfallen; Introduction + Clearing out = Teil 1, Cache + Strategies = Teil 2, Productivity + Mitigation = Teil 3; Key Takeaways entfallen | „Fast memory is small, big memory is slow", „LRU works because the recent past predicts the near future", „Marie Kondo is LRU for your home", „Caches can be flooded and poisoned" | Objectives, Takeaways, Cache-Jargon in Klammern der Produktivitätsfolien, Flooding/Poisoning-Details, Quellen bleiben als Fußnoten |
| IV Scheduling | The basics / Your goal decides the rule / Real life | Johnson, Historie, Klassifikation = Teil 1; EDD, SPT, gewichtetes SPT, Lawler, NP-hard = Teil 2; Priority Inversion (hinter Lawler verschoben), Echtzeit, Thrashing = Teil 3; Agenda und „Programming Connections" entfallen | „For total time alone, the order doesn't matter", „Goal 1: nobody waits too long past the deadline", „Weighted SPT: highest value per minute first", „EDD in real time: switch only for an earlier deadline" | Topic, Agenda, Takeaways, Quick-reminder-Callouts, Equal-Deadline/Duration-Hinweise, Anwendungsliste |
| V Randomness | Randomness everywhere / Simulate instead of calculate / Let chance help you decide | Understanding + Daily Life (+ „Why computer scientists love randomness", echte/Pseudo-Zufälligkeit) = Teil 1; Monte Carlo = Teil 2; Brute Force bis TSP + Society + Uncertainty + Good enough = Teil 3 | „Twenty cities would take 77 million years", „Hill climbing: improve step by step, until you are stuck", „Most likely 21 days, but only 63 % finish by day 25", „Random choices can be the fairest choices" | Welcome/Topic/Agenda, Monte-Carlo-Geschichte, Wald-Beispiel im Detail, Takeaway-Callouts |
| VI Kindness | Looking back / Computational kindness / Looking ahead | Q&A-Abschnittsfolie entfällt; Schlussfolie gekürzt | „Propose two slots instead of asking "when are you free?"", „Biased data leads to biased decisions", „Bayes' rule: update your beliefs with new evidence" | Fairness-Callout, Feedback-Loop-Beispiel |

Deck-Längen (Folien in RevealJS, nach der Nachschärfung vom 27. Oktober ohne Abschnittstitelfolien): 00: 35, I: 35, II: 60, III: 48, IV: 78, V: 58, VI: 35.

## Entscheidungen

1. **Roadmap-Folie statt Abschnittstitelfolie:** Abschnitt 1 folgt direkt auf die Eröffnungs-Roadmap, Abschnitt 2 und 3 beginnen mit genau einer Roadmap-Folie mit hervorgehobenem Punkt. Ohne `#`-Folien sind die Decks flache Folgen ohne vertikale Stapel; Foliennummern laufen durch.
8. **Review-PDFs** (`review-pdfs/`, committet): Druckansicht `?print-pdf&showNotes=separate-page`, gedruckt mit chrome-headless-shell. Jede Folie mit Sprechernotizen bekommt die Notizen auf einer eigenen Seite direkt nach der Folie; Folien ohne Notizen stehen allein. Erzeugt mit `helpers/review_pdf.sh`.
2. **Abschluss auf der HTML-Seite:** „What we covered" und Kernbotschaft stehen auch auf der Lecture-Seite (an der Marke), damit die Seite als Lernnotiz vollständig ist. Die Roadmap-Wiederholungen und covered-Folien der Abschnitte erscheinen nur in RevealJS.
3. **Notizen auf der HTML-Seite sichtbar**, im PDF nicht: Die Seite ist die „tiefe" Fassung für Studierende, das PDF bleibt die reine Folienfassung.
4. **Richtwert 40 Wörter:** Nach dem Umbau liegen 10 Folien zwischen 41 und 45 Wörtern (Lecture I: 1, II: 6, III: 1, VI: 2), alle ohne Kürzung der Kernaussage möglich, deshalb belassen; das Prüfskript listet sie weiter.
5. **Loud- und Fotofolien ohne Titel** bleiben (je Deck 1 bis 3), sie sind bewusst so gestaltet; das Prüfskript führt sie getrennt.
6. **Lecture VI ohne „After the break"**, wie bisher: nach der Kernbotschaft folgen „That's it for the lecture series!", die Abschiedsanimation und die Literatur.
7. **Vorgegebene Texte** (summary, why, roadmap, covered, key) sind exakt übernommen, inklusive „Five topics" in Lecture 00, obwohl das Deck sechs Sitzungen aufzählt.

## Probleme

- Mitten im Auftrag ging die Verbindung verloren und das Scratchpad wurde geleert; die Hilfsskripte (CDP-Treiber, Überlaufprüfung, Screenshots) wurden neu geschrieben. Keine Auswirkung auf das Ergebnis.
- Quarto meldet „problem with a fenced div", wenn ein `:::`-Div direkt nach einer Textzeile ohne Leerzeile beginnt; in Lecture III beim Einfügen der Fragezeilen passiert und behoben.
- `freeze: auto` sieht Änderungen an `helpers/course_plots.py` und am Lua-Filter nicht; der Abschluss-Render lief deshalb ohne `_site` neu, `_freeze` wurde für die Lectures mit Code vorher gelöscht.

## Ergebnis der Prüfungen

- **Komplett-Render** ohne `_site` (`uv run quarto render`): Exit 0, keine Warnungen aus Filter oder Kurscode.
- **Prüfskript** (`uv run python helpers/check_lecture_frame.py`): alle sieben Lectures OK. Rahmenfelder vollständig, genau drei Abschnitte mit Titeln gleich Roadmap, Abschlussmarke vorhanden. Folien über 40 Wörter: Lecture I 1 (42), II 6 (41 bis 43), III 1 (41), VI 2 (43, 45), alle anderen 0. Folien ohne Titel: nur Loud- und Fotofolien (00: 1, I: 3, II: 1, IV: 1, V: 1, VI: 1).
- **Überlaufprüfung** aller acht Decks, normale Ansicht und `?print-pdf`: kein Überlauf, keine Footer-Berührung, keine Folie mit zwei Druckseiten. Einzige Meldung ist das bekannte Messartefakt des Kopieren-Buttons (8 px) auf drei Codefolien. Messung in `screenshots-review/rahmung/messung-ueberlauf.json`.
- **404-Prüfung** aller acht Decks (jede Folie besucht): 0 fehlgeschlagene Requests; vorher 1 je Deck mit Formeln (STIX-fontdata).
- **Screenshots** je Lecture in `screenshots-review/rahmung/` (gitignored): Titelfolie, „Today in one sentence", „Roadmap", eine Abschnittsfolie mit Roadmap, eine Abschnitts-Abschlussfolie, „What we covered", „Why it matters", Kernbotschaft, dazu die HTML-Lecture-Seite oben. 63 Dateien.

## Nachschärfung 27. Oktober 2026

- Abschnitt 1 folgt direkt auf die Eröffnungs-Roadmap; Abschnitt 2 und 3 beginnen mit genau einer Roadmap-Folie (hervorgehobener Punkt), die die Abschnittstitelfolie ersetzt. HTML-Seiten behalten die `#`-Überschriften. Filter, Prüfskript-Beschreibung und CLAUDE.md angepasst, unbenutzte CSS-Regel entfernt.
- Alle sieben Lectures neu gerendert, Prüfskript 7× OK, Überlaufprüfung aller acht Decks ohne Befund (nur das Kopieren-Button-Artefakt).
- Review-PDFs `review-pdfs/lec_00-review.pdf` (44 Seiten: 35 Folien + 9 Notizseiten) und `lec_01-review.pdf` (45 Seiten: 35 + 10), erzeugt mit `zsh helpers/review_pdf.sh lec_00 lec_01`. Die Notizen stehen jeweils auf der Seite direkt nach der Folie.
