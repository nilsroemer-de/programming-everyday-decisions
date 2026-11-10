"""Simple SVG illustrations in the course style (Lecture III).

Drawn with matplotlib patches and saved as SVG with text converted to paths,
so the illustrations use Inter/Poppins without embedding fonts and render the
same in the browser (as <img>) and in the Typst PDF. Colours come from the
design tokens in course_plots.py (_brand.yml).

Usage (from the repo root):

    uv run python helpers/course_illustrations.py          # writes images/caching/*.svg
"""
from __future__ import annotations

from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle

from course_plots import (AMBER, BORDER, BORDER_STRONG, FG_2, FG_3, GREEN, INK, PRIMARY,
                          PRIMARY_LIGHT, RED, SKY_300, SKY_500, TASK_COLORS, use_course_style)

OUT_DIR = Path(__file__).resolve().parent.parent / "images" / "caching"
WOOD = "#e9d9c1"
WOOD_DARK = "#cdb594"
WALL = "#f3f8fd"
FLOOR = "#eef3f8"

BOOK_COLORS = [TASK_COLORS["A"], TASK_COLORS["B"], TASK_COLORS["C"], TASK_COLORS["E"],
               TASK_COLORS["G"], TASK_COLORS["H"], TASK_COLORS["D"], TASK_COLORS["F"]]


def _canvas(width: float, height: float, xlim, ylim):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)
    return fig, ax


def _rect(ax, x, y, w, h, fc, ec=INK, lw=1.2, **kw):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=fc, edgecolor=ec, linewidth=lw, **kw))


def _rounded(ax, x, y, w, h, fc, ec=INK, lw=1.2, r=0.12):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                facecolor=fc, edgecolor=ec, linewidth=lw))


LABEL_SCALE = 1.8  # illustrations appear at about a third of their drawn size on the slides


def _label(ax, x, y, text, size=12, color=FG_2, ha="center", family="Inter", weight="normal"):
    ax.text(x, y, text, fontsize=size * LABEL_SCALE, color=color, ha=ha, va="center", fontfamily=family, fontweight=weight)


def _book(ax, x, y, w=0.55, h=1.6, color=SKY_300, letter=None, angle=0.0):
    """An upright book standing at (x, y), optionally rotated around its base."""
    import matplotlib.transforms as mtrans
    t = mtrans.Affine2D().rotate_deg_around(x + w / 2, y, angle) + ax.transData
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor=INK, linewidth=1.2, transform=t))
    ax.add_patch(Rectangle((x, y + h * 0.78), w, h * 0.06, facecolor=INK, edgecolor="none", transform=t))
    if letter:
        ax.text(x + w / 2, y + h * 0.42, letter, fontsize=11 * LABEL_SCALE, color=INK, ha="center", va="center",
                fontfamily="Poppins", fontweight="semibold", transform=t)


def _shelf_unit(ax, x, y, w, h, rows=3):
    """A cupboard/shelf frame with `rows` boards; returns the board y positions and inner box."""
    _rect(ax, x, y, w, h, WOOD, lw=1.4)
    inner = (x + 0.18, y + 0.18, w - 0.36, h - 0.36)
    _rect(ax, *inner, WALL, ec=WOOD_DARK, lw=1.0)
    step = inner[3] / rows
    boards = []
    for i in range(1, rows):
        by = inner[1] + i * step
        _rect(ax, inner[0], by - 0.07, inner[2], 0.14, WOOD, ec=WOOD_DARK, lw=0.8)
        boards.append(by)
    return [inner[1]] + boards, inner, step


def _pile(ax, x, y, w, color, h=0.28, tilt=0.0):
    """A folded piece of clothing (soft rounded rectangle)."""
    import matplotlib.transforms as mtrans
    t = mtrans.Affine2D().rotate_deg_around(x + w / 2, y + h / 2, tilt) + ax.transData
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.1",
                                facecolor=color, edgecolor=INK, linewidth=1.0, transform=t))


# --- Cupboards -----------------------------------------------------------------
def cupboard_messy(path: Path):
    fig, ax = _canvas(4.2, 5.2, (0, 4.2), (0, 5.2))
    _rect(ax, 0, 0, 4.2, 0.5, FLOOR, ec="none")
    boards, inner, step = _shelf_unit(ax, 0.8, 0.5, 2.6, 4.3)
    x0, w = inner[0] + 0.1, inner[2] - 0.2
    colors = [SKY_300, TASK_COLORS["A"], TASK_COLORS["B"], SKY_500, TASK_COLORS["E"], TASK_COLORS["G"]]
    # top shelf: crammed, crooked
    by = boards[2] + 0.07
    _pile(ax, x0 + 0.05, by, 1.1, colors[0], tilt=-8)
    _pile(ax, x0 + 0.9, by + 0.1, 1.0, colors[1], tilt=12)
    _pile(ax, x0 + 0.3, by + 0.45, 1.3, colors[2], tilt=5)
    _pile(ax, x0 + 1.2, by + 0.55, 0.9, colors[3], tilt=-14)
    # middle shelf: hanging over the edge
    by = boards[1] + 0.07
    _pile(ax, x0 - 0.15, by + 0.05, 1.2, colors[4], tilt=-18)
    _pile(ax, x0 + 0.8, by, 1.1, colors[5], tilt=6)
    _pile(ax, x0 + 0.45, by + 0.42, 1.4, colors[0], tilt=-4)
    # bottom shelf: heap
    by = boards[0] + 0.03
    _pile(ax, x0 + 0.1, by, 1.0, colors[1], tilt=20)
    _pile(ax, x0 + 1.0, by + 0.05, 1.0, colors[3], tilt=-25)
    _pile(ax, x0 + 0.5, by + 0.35, 1.2, colors[2], tilt=9)
    # things on the floor
    _pile(ax, 0.1, 0.5, 0.8, colors[4], tilt=-12)
    _pile(ax, 3.5, 0.52, 0.65, colors[5], tilt=18)
    fig.savefig(path)
    plt.close(fig)


def cupboard_full(path: Path):
    fig, ax = _canvas(4.2, 5.2, (0, 4.2), (0, 5.2))
    _rect(ax, 0, 0, 4.2, 0.5, FLOOR, ec="none")
    boards, inner, step = _shelf_unit(ax, 0.8, 0.5, 2.6, 4.3)
    x0, w = inner[0] + 0.12, inner[2] - 0.24
    stack_w = (w - 0.12) / 2
    colors = [[SKY_300, SKY_500, PRIMARY_LIGHT], [TASK_COLORS["A"], TASK_COLORS["G"], AMBER],
              [TASK_COLORS["B"], TASK_COLORS["E"], GREEN]]
    for row, by in enumerate(boards):
        y = by + 0.09
        # two neat stacks per shelf, filled to the board above
        for col in range(2):
            x = x0 + col * (stack_w + 0.12)
            shades = colors[(row + col) % 3]
            for k in range(4):
                _pile(ax, x, y + k * 0.29, stack_w, shades[k % 3])
    # one piece that does not fit anymore, on top of the cupboard
    _pile(ax, 1.6, 4.82, 1.0, SKY_300)
    fig.savefig(path)
    plt.close(fig)


# --- Desk and shelf --------------------------------------------------------------
def _desk(ax, x, y, w=4.0, h=0.22, legs=1.1):
    _rect(ax, x, y, w, h, WOOD, lw=1.3)
    _rect(ax, x + 0.25, y - legs, 0.16, legs, WOOD_DARK, ec=INK, lw=1.0)
    _rect(ax, x + w - 0.41, y - legs, 0.16, legs, WOOD_DARK, ec=INK, lw=1.0)


def _bookshelf(ax, x, y, w=2.6, h=4.0, rows=4, letters_from="D"):
    boards, inner, step = _shelf_unit(ax, x, y, w, h, rows)
    letter = ord(letters_from)
    bw = 0.42
    for by in boards:
        bx = inner[0] + 0.1
        i = 0
        while bx + bw <= inner[0] + inner[2] - 0.08:
            _book(ax, bx, by + 0.08, w=bw, h=step - 0.3, color=BOOK_COLORS[(i + letter) % len(BOOK_COLORS)],
                  letter=chr(letter) if letter <= ord("Z") else None)
            bx += bw + 0.08
            i += 1
            letter += 1
    return inner


def desk_three_books(path: Path):
    fig, ax = _canvas(9.0, 4.6, (0, 9.0), (0, 4.6))
    _rect(ax, 0, 0, 9.0, 0.5, FLOOR, ec="none")
    _desk(ax, 0.5, 1.6)
    for i, (letter, color) in enumerate(zip("ABC", BOOK_COLORS)):
        _book(ax, 1.1 + i * 0.95, 1.82, w=0.6, h=1.6, color=color, letter=letter)
    _label(ax, 2.5, 4.25, "Desk: three books", size=11, color=INK, family="Poppins", weight="semibold")
    _bookshelf(ax, 5.9, 0.5, 2.6, 3.4, rows=3)
    _label(ax, 7.2, 4.25, "Shelf", size=11, color=INK, family="Poppins", weight="semibold")
    ax.add_patch(FancyArrowPatch((4.6, 1.0), (5.85, 1.0), arrowstyle="<|-|>", mutation_scale=16,
                                 color=FG_2, linewidth=1.3, linestyle=(0, (4, 3))))
    _label(ax, 5.22, 0.65, "a trip", size=9, color=FG_2)
    fig.savefig(path)
    plt.close(fig)


def attention_desk(path: Path):
    fig, ax = _canvas(7.0, 4.6, (0, 7.0), (0, 4.6))
    _rect(ax, 0, 0, 7.0, 0.5, FLOOR, ec="none")
    _desk(ax, 0.8, 1.6, w=4.2)
    # two books that stay, one that is being pushed off the right edge
    _book(ax, 1.3, 1.82, w=0.6, h=1.6, color=BOOK_COLORS[0], letter="A")
    _book(ax, 2.25, 1.82, w=0.6, h=1.6, color=BOOK_COLORS[1], letter="B")
    _book(ax, 4.85, 1.25, w=0.6, h=1.6, color=BOOK_COLORS[2], letter="C", angle=-38)
    # the notification takes the free slot on the desk
    _rounded(ax, 3.15, 1.82, 1.25, 1.6, "white", ec=PRIMARY, lw=1.6, r=0.14)
    ax.add_patch(Circle((3.77, 2.95), 0.11, facecolor=RED, edgecolor="none"))
    for k in range(3):
        _rect(ax, 3.42, 2.15 + k * 0.22, 0.7 if k else 0.5, 0.08, SKY_500, ec="none")
    # arrow: new notification drops in from above
    ax.add_patch(FancyArrowPatch((3.77, 4.3), (3.77, 3.55), arrowstyle="-|>", mutation_scale=16,
                                 color=PRIMARY, linewidth=1.6))
    _label(ax, 3.77, 4.45, "new notification", size=10.5, color=PRIMARY)
    # arrow: book pushed off
    ax.add_patch(FancyArrowPatch((4.55, 2.6), (5.55, 2.0), arrowstyle="-|>", mutation_scale=16,
                                 color=FG_2, linewidth=1.3, connectionstyle="arc3,rad=-0.3"))
    fig.savefig(path)
    plt.close(fig)


# --- Noguchi filing ----------------------------------------------------------------
def noguchi_row(path: Path):
    fig, ax = _canvas(9.0, 3.4, (0, 9.0), (0, 3.4))
    # shelf board
    _rect(ax, 0.3, 0.6, 8.4, 0.16, WOOD, lw=1.2)
    n = 9
    fw, gap, x0 = 0.72, 0.1, 0.55
    used = 5  # index of the folder that was just used
    for i in range(n):
        if i == used:
            continue
        x = x0 + i * (fw + gap)
        color = SKY_300 if i % 2 else TASK_COLORS["D"]
        _rect(ax, x, 0.76, fw, 1.7, color, lw=1.1)
        _rect(ax, x + 0.14, 1.95, fw - 0.28, 0.3, "white", ec=BORDER_STRONG, lw=0.8)
    # the used folder, lifted out of its slot, on its way to the left end
    xl = x0 + used * (fw + gap)
    _rect(ax, xl, 0.76, fw, 1.7, "white", ec=BORDER_STRONG, lw=1.0, linestyle=(0, (3, 3)))
    _rect(ax, xl, 2.62, fw, 0.6, TASK_COLORS["A"], lw=1.1)
    _rect(ax, xl + 0.14, 2.87, fw - 0.28, 0.22, "white", ec=BORDER_STRONG, lw=0.8)
    ax.add_patch(FancyArrowPatch((xl - 0.05, 2.92), (x0 + fw / 2, 2.62), arrowstyle="-|>", mutation_scale=16,
                                 color=PRIMARY, linewidth=1.6, connectionstyle="arc3,rad=0.22"))
    _label(ax, xl + fw + 0.12, 2.92, "just used", size=10.5, color=FG_2, ha="left")
    _label(ax, x0, 0.3, "most recently used", size=10.5, color=PRIMARY, ha="left")
    _label(ax, x0 + (n - 1) * (fw + gap) + fw, 0.3, "longest untouched", size=10.5, color=FG_3, ha="right")
    fig.savefig(path)
    plt.close(fig)


# --- Warehouse, top view -------------------------------------------------------------
def warehouse_top(path: Path):
    fig, ax = _canvas(8.0, 4.6, (0, 8.0), (0, 4.6))
    _rect(ax, 0.3, 0.3, 7.4, 4.0, "white", lw=1.4)
    # dispatch area along the bottom wall
    _rect(ax, 0.3, 0.3, 7.4, 0.8, SKY_300, ec=INK, lw=1.4)
    _label(ax, 4.0, 0.7, "Dispatch area", size=12, color=INK, family="Poppins", weight="semibold")
    for x in (1.3, 4.0, 6.7):
        ax.add_patch(FancyArrowPatch((x, 0.55), (x, -0.05), arrowstyle="-|>", mutation_scale=14,
                                     color=INK, linewidth=1.3, clip_on=False))
    # rack rows: nearest row fast movers (primary), then medium, then slow (faint)
    rows = [(1.45, PRIMARY, "Fast movers"), (2.4, SKY_500, ""), (3.35, BORDER, "Slow movers")]
    for y, color, text in rows:
        for x in (0.6, 2.35, 4.1, 5.85):
            _rect(ax, x, y, 1.5, 0.6, color, lw=1.0)
        if text:
            _label(ax, 7.95, y + 0.3, text, size=10.5, color=INK if color == PRIMARY else FG_2, ha="left")
    # distance arrow at the left
    ax.add_patch(FancyArrowPatch((0.1, 1.1), (0.1, 3.95), arrowstyle="-|>", mutation_scale=12,
                                 color=FG_3, linewidth=1.0, clip_on=False))
    ax.text(0.0, 2.5, "longer walk", rotation=90, fontsize=9.5 * LABEL_SCALE, color=FG_3, ha="right", va="center")
    ax.set_xlim(-0.7, 10.6)
    ax.set_ylim(-0.3, 4.6)
    fig.savefig(path)
    plt.close(fig)


ILLUSTRATIONS = {
    "cupboard_messy.svg": cupboard_messy,
    "cupboard_full.svg": cupboard_full,
    "desk_three_books.svg": desk_three_books,
    "noguchi_row.svg": noguchi_row,
    "warehouse_top.svg": warehouse_top,
    "attention_desk.svg": attention_desk,
}


def main() -> None:
    use_course_style()
    matplotlib.rcParams["svg.fonttype"] = "path"  # text as outlines: no font dependency
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, draw in ILLUSTRATIONS.items():
        draw(OUT_DIR / name)
        print("wrote", OUT_DIR / name)


if __name__ == "__main__":
    main()
