"""Checks the lecture frame of every lecture (see CLAUDE.md, "Rahmenstruktur").

The frame slides are written out in each lecture. For each lectures/lec_0*.qmd the script
reports, as hints only (exit code is always 0):
- the frame slides: "Today in one sentence", the opening "Roadmap", a roadmap slide before
  section 2 and 3, one covered slide per section, "What we covered", "Why it matters" and
  the key message slide,
- whether there are exactly three level-1 sections whose titles equal the points of the
  opening roadmap, and whether every roadmap slide lists the same three points,
- slides (level-2 headers) whose visible text has more than 40 words
  (code, speaker notes, footnote definitions, image credits and table rows do not count),
- slides without a title; loud slides and photo slides are listed separately because they
  are untitled by design.

Usage: uv run python helpers/check_lecture_frame.py [lectures/lec_01_optimal_stopping.qmd ...]
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_WORDS = 40


def strip_front_matter(text: str) -> str:
    m = re.match(r"^---\n.*?\n---\n", text, flags=re.S)
    return text[m.end():] if m else text


def strip_code(body: str) -> str:
    return re.sub(r"```.*?```", "\n", body, flags=re.S)


def plain_title(header: str) -> str:
    """'# [About this course]{.flow} {.title}' -> 'About this course'."""
    t = re.sub(r"^#+\s*", "", header)
    t = re.sub(r"\[([^\]]*)\]\{[^}]*\}", r"\1", t)     # spans
    t = re.sub(r"\{[^}]*\}", "", t)                   # attributes
    t = re.sub(r"\[\^[^\]]+\]", "", t)                 # footnote refs
    return t.strip()


def visible_words(slide_body: str) -> int:
    s = re.sub(r"::: ?\{\.notes\}.*?\n:::", " ", slide_body, flags=re.S)
    s = re.sub(r"::: ?footer.*?\n:::", " ", s, flags=re.S)
    s = re.sub(r"^\[\^[^\]]+\]:.*$", " ", s, flags=re.M)      # footnote definitions
    s = re.sub(r"^\|.*$", " ", s, flags=re.M)                   # table rows
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", s)                # images
    s = re.sub(r"<[^>]+>", " ", s)                              # html
    s = re.sub(r"\$\$.*?\$\$", " formula ", s, flags=re.S)      # display math counts as one word
    s = re.sub(r"\{[^}]*\}", " ", s)                            # attributes
    s = re.sub(r"[:\-\*\.`\[\]#>|_]", " ", s)
    return len([w for w in s.split() if len(w) > 1])


def roadmap_points(block: str) -> list[str]:
    return [re.sub(r"\]\{[^}]*\}$", "", m.group(1)) for m in re.finditer(r"^\d+\. \[(.*)$", block, flags=re.M)]


def check(path: pathlib.Path) -> list[str]:
    hints: list[str] = []
    body = strip_code(strip_front_matter(path.read_text()))
    parts = re.split(r"^(#{1,2} .*)$", body, flags=re.M)
    slides = []  # (level, header line, title, body)
    for i in range(1, len(parts), 2):
        header = parts[i]
        slides.append((1 if header.startswith("# ") else 2, header, plain_title(header), parts[i + 1] if i + 1 < len(parts) else ""))

    # frame slides
    titles = [t for lvl, _, t, _ in slides if lvl == 2]
    headers = [h for lvl, h, _, _ in slides if lvl == 2]
    want = ["Today in one sentence", "Roadmap", "What we covered", "Why it matters"]
    for w in want:
        if w not in titles:
            hints.append(f"frame slide missing: {w}")
    if not any(".lecture-key" in h for h in headers):
        hints.append("frame slide missing: key message (## {.loud-slide .lecture-key})")
    roadmaps = [roadmap_points(b) for lvl, h, t, b in slides if lvl == 2 and t == "Roadmap"]
    if len(roadmaps) != 3:
        hints.append(f"{len(roadmaps)} roadmap slides, expected 3 (opening, before section 2 and 3)")
    if roadmaps and any(r != roadmaps[0] for r in roadmaps):
        hints.append("roadmap slides list different points")
    covered = [t for lvl, h, t, _ in slides if lvl == 2 and ".section-covered" in h]
    sections = [t for lvl, _, t, _ in slides if lvl == 1]
    if roadmaps:
        if len(roadmaps[0]) != 3:
            hints.append(f"opening roadmap has {len(roadmaps[0])} points, expected 3")
        if [s.lower() for s in sections] != [p.lower() for p in roadmaps[0]]:
            hints.append(f"sections {sections} do not equal the roadmap {roadmaps[0]}")
        if [c.lower() for c in covered] != [p.lower() for p in roadmaps[0]]:
            hints.append(f"covered slides {covered} do not match the roadmap (one per section, same title)")
    elif len(sections) != 3:
        hints.append(f"{len(sections)} level-1 sections, expected 3")

    # text per slide
    untitled, untitled_by_design, long = [], [], []
    for lvl, header, title, slide_body in slides:
        if lvl != 2:
            continue
        if not title:
            if ".loud-slide" in header or "background-image" in header or "background-color" in header:
                untitled_by_design.append(header.strip())
            else:
                untitled.append(header.strip())
        if re.search(r"\.(lecture-opening|lecture-closing|section-covered|section-roadmap|lecture-key)\b", header):
            continue  # frame slides carry fixed text and are not counted
        n = visible_words(slide_body)
        if n > MAX_WORDS:
            long.append(f"{n:3d} words: {title or header.strip()}")
    if long:
        hints.append("slides over %d words:" % MAX_WORDS)
        hints.extend("  " + l for l in long)
    if untitled:
        hints.append("slides without title:")
        hints.extend("  " + u for u in untitled)
    if untitled_by_design:
        hints.append(f"untitled by design (loud or photo slides): {len(untitled_by_design)}")
    return hints


def main(argv: list[str]) -> int:
    files = [pathlib.Path(a) for a in argv] or sorted((ROOT / "lectures").glob("lec_0*.qmd"))
    for f in files:
        hints = check(f)
        print(f"{f.name}: {'no hints' if not hints else str(len(hints)) + ' hint(s)'}")
        for h in hints:
            print("  " + h)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
