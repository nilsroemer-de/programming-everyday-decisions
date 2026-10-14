"""Checks the lecture frame of every lecture (see CLAUDE.md, "Rahmenstruktur").

For each lectures/lec_0*.qmd it reports
- whether the five frame fields in the YAML header are complete
  (lecture-summary, lecture-why, lecture-roadmap with 3 points, lecture-covered with 3
  sentences, lecture-key) and whether the closing marker `::: {.lecture-closing}` exists,
- whether there are exactly three level-1 sections whose titles equal the roadmap points,
- slides (level-2 headers) whose visible text has more than 40 words
  (code, speaker notes, footnote definitions and image credits do not count),
- slides without a title (`## ` with attributes only); loud slides and photo slides are
  listed separately because they are untitled by design.

Usage: uv run python helpers/check_lecture_frame.py [lectures/lec_01_optimal_stopping.qmd ...]
Exit code 1 if any lecture fails a structural check (fields, sections, marker).
"""
from __future__ import annotations

import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAX_WORDS = 40
FIELDS = ["lecture-summary", "lecture-why", "lecture-roadmap", "lecture-covered", "lecture-key"]


def split_front_matter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


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
    s = re.sub(r"^\|.*$", " ", s, flags=re.M)                   # table rows (lookup tables are not prose)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", s)                # images
    s = re.sub(r"<[^>]+>", " ", s)                              # html
    s = re.sub(r"\$\$.*?\$\$", " formula ", s, flags=re.S)      # display math counts as one word
    s = re.sub(r"\{[^}]*\}", " ", s)                            # attributes
    s = re.sub(r"[:\-\*\.`\[\]#>|_]", " ", s)
    return len([w for w in s.split() if len(w) > 1])


def check(path: pathlib.Path) -> tuple[list[str], list[str]]:
    errors, notes = [], []
    meta, body = split_front_matter(path.read_text())
    for f in FIELDS:
        if f not in meta or not meta[f]:
            errors.append(f"missing field {f}")
    roadmap = meta.get("lecture-roadmap") or []
    covered = meta.get("lecture-covered") or []
    if roadmap and len(roadmap) != 3:
        errors.append(f"lecture-roadmap has {len(roadmap)} points, expected 3")
    if covered and len(covered) != len(roadmap):
        errors.append(f"lecture-covered has {len(covered)} sentences, roadmap has {len(roadmap)}")
    if "{.lecture-closing}" not in body:
        errors.append("closing marker ::: {.lecture-closing} missing")

    code_free = strip_code(body)
    sections = [plain_title(l) for l in code_free.splitlines() if re.match(r"^# ", l)]
    want = [str(p).strip() for p in roadmap]
    if [s.lower() for s in sections] != [w.lower() for w in want]:
        errors.append(f"sections {sections} do not equal roadmap {want}")

    # slides
    parts = re.split(r"^(## .*)$", code_free, flags=re.M)
    untitled, untitled_by_design, long = [], [], []
    for i in range(1, len(parts), 2):
        header, slide_body = parts[i], parts[i + 1] if i + 1 < len(parts) else ""
        title = plain_title(header)
        if not title:
            if ".loud-slide" in header or "background-image" in header or "background-color" in header:
                untitled_by_design.append(header.strip())
            else:
                untitled.append(header.strip())
        n = visible_words(slide_body)
        if n > MAX_WORDS:
            long.append(f"{n:3d} words: {title or header.strip()}")
    if long:
        notes.append("slides over %d words:" % MAX_WORDS)
        notes.extend("  " + l for l in long)
    if untitled:
        notes.append("slides without title:")
        notes.extend("  " + u for u in untitled)
    if untitled_by_design:
        notes.append(f"untitled by design (loud or photo slides): {len(untitled_by_design)}")
    return errors, notes


def main(argv: list[str]) -> int:
    files = [pathlib.Path(a) for a in argv] or sorted((ROOT / "lectures").glob("lec_0*.qmd"))
    failed = False
    for f in files:
        errors, notes = check(f)
        status = "OK " if not errors else "FAIL"
        print(f"{status} {f.name}")
        for e in errors:
            print("  ERROR", e)
        for n in notes:
            print("  " + n)
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
