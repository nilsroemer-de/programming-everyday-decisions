# Review Lecture 0 und Lecture I vor der Veröffentlichung

Stand: 27. Oktober 2026, Branch `inhalt-review`. Geprüft wurden `lectures/lec_00_introduction.qmd` und `lectures/lec_01_optimal_stopping.qmd` Folie für Folie auf Fachlichkeit, Quellen, Rahmung, Sprache, Technik, Didaktik und Konsistenz mit dem KLU-Syllabus.

Vorab: Nils' ungesicherte Änderungen in beiden Dateien wurden als eigener Commit gesichert (dee0756). Die Folie „The same idea in other places" war darin bereits gelöscht; die Parkplatz-Notiz stand aber noch nirgends und wurde in die Notizen von „In practice, people stop too early" übernommen.

## 1. Direkt korrigiert

| Datei | Folie | Korrektur |
|---|---|---|
| lec_00 | About this course (covered) und What we covered | „Five topics" durch „Six topics" ersetzt. Die Folie „Six topics, one per session" listet I bis VI, der Syllabus hat sechs Sessions. |
| lec_00 | How to hand in assignments, covered-Folien | Prozentangaben ohne Leerzeichen: „50 %", „75 %" (dreimal). |
| lec_00 | You learn Python in the tutorials | Doppelpunkt in den Question-Span gezogen (`[Question:]{.question}`, wie überall sonst) und Frage geglättet: „Does anybody know why?". |
| lec_00 | Take part, it pays off | Buchtitel in Titelschreibweise: „Algorithms to Live By". |
| lec_01 | Loud-Folie nach „Options come one by one" | „Anybody an example of optimal stopping?" zu „Does anybody have an example of optimal stopping?" (drei Zeilen bleiben). |
| lec_01 | In practice, people stop too early | Parkplatz-Notiz aus der gelöschten Folie als zweiter Absatz in die Notizen übernommen. |

Nichts davon ändert eine Aussage, außer „Five" zu „Six", was ein eindeutiger Zählfehler war.

## 2. Offene Befunde je Folie, nach Priorität

**Hoch**

1. lec_01, „If you can be rejected, leap earlier", Notizen. Problem: „keep exploring until 34.4" stimmt rechnerisch nicht. 18 + 0,61 × 22 = 31,4 (die anderen beiden Zahlen stimmen: 26,1 und 23,5). Vorschlag: im Buch (Kapitel 1) nachschlagen und auf 31.4 korrigieren, falls dort nichts anderes steht.
2. lec_01, Rahmung. Problem: Lecture I hat keine Abschnitts-Abschlussfolien (`{.section-covered}`) mehr, Lecture 0 hat sie, und CLAUDE.md beschreibt sie als Teil der Struktur. Das Prüfskript meldet es als Hinweis. Vorschlag: entweder die drei Folien mit den Sätzen aus „What we covered" wieder einsetzen, oder bewusst darauf verzichten und dann Lecture 0, CLAUDE.md und das Prüfskript angleichen.

**Mittel**

3. lec_01, „If you can go back, wait longer". Problem: „61%" ohne Quelle auf der Folie (das Buch steht nur in den Notizen). Vorschlag: Fußnote „Christian, B. & Griffiths, T. (2016). Algorithms to Live By, Kapitel 1."
4. lec_01, „Fixed time instead of a fixed number of options". Problem: „37% of the time" ohne Quelle. Vorschlag: dieselbe Buch-Fußnote.
5. lec_01, „In practice, people stop too early". Problem: „about a dozen experiments" ohne Quelle auf der Folie. Vorschlag: Fußnote „Seale, D.A. & Rapoport, A. (1997). Sequential decision making with relative ranks: An experimental investigation of the secretary problem. Organizational Behavior and Human Decision Processes, 69(3), 221–236."
6. lec_00, „Add notebooks to your project". Problem: Die Befehle `uv add --dev ipykernel` und `uv add jupyter` stehen nicht auf der Installationsseite `general/uv.qmd`, obwohl die Folie davor alle dorthin schickt. Vorschlag: einen kurzen Abschnitt „Notebooks" auf der uv-Seite ergänzen (außerhalb dieses Auftrags, nicht geändert).
7. lec_01, „The burglar: knowing when to quit", Fußnote. Problem: Ferguson-Skript ohne Jahr oder Link, schwer auffindbar. Vorschlag: „Ferguson, T.S. Optimal Stopping and Applications, Kapitel 1, https://www.math.ucla.edu/~tom/Stopping/Contents.html".

**Niedrig**

8. lec_01, „Real life changes the assumptions". 65 Wörter und sechs Punkte, über dem Richtwert. Als Überblick des Abschnitts vertretbar, alle sechs Punkte bekommen danach eine eigene Folie. Vorschlag: so lassen.
9. lec_01, „The setup in three lines" (54 Wörter) und weitere sieben Folien zwischen 41 und 55 Wörtern. Hinweise des Prüfskripts, kein Überlauf. Vorschlag: so lassen.
10. lec_00, „Why it matters". Die Eröffnung endet mit „No prior knowledge required.", der Abschluss nicht. Vorschlag: entscheiden, ob der Unterschied gewollt ist.
11. lec_00, „VS Code is an IDE" folgt auf „Install VS Code". Vorschlag: Reihenfolge tauschen oder beide Folien zusammenlegen (erst erklären, dann installieren).
12. lec_00, „Don't give up!". Das GIF hat einen leeren Alt-Text. Vorschlag: kurzen Alt-Text ergänzen.
13. lec_01, „After the break: First Steps in Python". Passt zum Tutorial, nennt es aber nicht. Vorschlag: optional „Tutorial I.I: Variables and Types" nennen.
14. lec_01, Bildfolien. Die drei Unsplash-Links in den Credits antworten auf automatisierte Anfragen mit 401 und konnten nicht per Skript geprüft werden; im Browser funktionieren sie erfahrungsgemäß.

## 3. Prüfergebnisse

- Zahlen nachgerechnet: 1/e = 0,368; Maximum von −x ln x bei x = 1/e mit Wert 0,368; exakte Erfolgswahrscheinlichkeit bei n = 100 maximal für 37 angeschaute Kandidaten (0,371); n = 3: 50 %, n = 20: 7 von 20 (0,384); q^(1/(1−q)) bei q = 0,5 gleich 0,25 und bei q nahe 1 gegen 1/e; q/(1−q) bei q = 0,9 gleich 9; 58 % nach Gilbert & Mosteller (1966) korrekt; Alter 26,1 und 23,5 korrekt, 34,4 nicht (siehe Befund 1). Code-Zelle liefert 37,5 % Treffer bei 10.000 Runden.
- Rahmung: Roadmap-Punkte in beiden Lectures an allen Stellen identisch, Eröffnung und Abschluss vollständig, „What we covered" passt zum Inhalt. Lecture I ohne Abschnitts-Abschlussfolien (Befund 2).
- Sprache: keine Gedankenstriche als Satzzeichen, Prozentangaben jetzt einheitlich ohne Leerzeichen, Pausenmarker stehen alle in eigener Zeile.
- Technik: beide Dateien einzeln gerendert (HTML, RevealJS, PDF, md) ohne Fehler. Überlaufprüfung aller Decks ohne Befund (lec_00: 35 Folien, lec_01: 37 Folien; einzig das bekannte 8-px-Artefakt des Kopierknopfs auf der Code-Folie). Fußnoten auf „Why 37%?", „If you can be rejected" und „The burglar" rendern und bleiben über dem Footer (Screenshots geprüft). Bilder und GIF vorhanden, alle externen Links außer Unsplash antworten mit 200.
- Konsistenz: Abgaberegel auf lec_00, Startseite und `klu_syllabus.md` identisch (pass/fail, 75 % Anwesenheit, zwei Assignments, 50 % korrekt, Präsentation, Gruppen bis drei, Abgabe bis Quartalsende). Lecturer und Affiliation kommen aus `lectures/_metadata.yml`. „After the break" in lec_00 nennt Secretary Problem, 37%-Regel und Simulation, genau der Inhalt von lec_01.
- Review-PDFs neu erzeugt: `review-pdfs/lec_00-review.pdf` (35 Folien + 9 Notizseiten), `review-pdfs/lec_01-review.pdf` (37 Folien + 11 Notizseiten).

## 4. Gesamteinschätzung

Beide Lectures sind bereit für morgen. Die Aussagen und Zahlen auf den Folien sind korrekt und belegt, Rahmung und Übergänge stimmen, nichts läuft über. Vor dem Vortrag lohnen zwei Minuten für Befund 1 (eine Zahl nur in den Sprechernotizen) und eine Entscheidung zu Befund 2 (Abschnitts-Abschlussfolien in Lecture I). Die fehlenden Fußnoten (Befunde 3 bis 5) sind Kür.
