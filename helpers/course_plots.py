"""Shared plotting helpers for the lectures.

Charts in the course (schedules, curves, simple diagrams) are generated from
the data shown on the slides, so text and figure cannot drift apart. The style
follows the website: Inter for text, Poppins for titles, ink/blue palette from
_brand.yml. Fonts are loaded from fonts-ttf/ (no system fonts needed).

Usage inside a lecture (cells run in lectures/):

    import sys; sys.path.insert(0, "../helpers")
    from course_plots import use_course_style, johnson_gantt
    use_course_style()
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# --- Design tokens (see _brand.yml) ---------------------------------------
INK = "#1e2648"
PRIMARY = "#01579b"
PRIMARY_LIGHT = "#85bae3"
SKY_300 = "#cfe2f4"
SKY_500 = "#9cc6e8"
FG_2 = "#4a5578"
FG_3 = "#8a93ad"
BORDER = "#dde5ee"
BORDER_STRONG = "#c3d2e2"
AMBER = "#b07a2a"
RED = "#b0485a"
GREEN = "#4a7c59"

# Soft fills per task letter (same hue per task across all charts)
TASK_COLORS = {
    "A": "#f1dfbf",  # amber tint
    "B": "#eccfd5",  # red tint
    "C": "#cfe2f4",  # sky-300
    "D": "#dde5ee",  # border grey
    "E": "#d4e5d9",  # green tint
    "F": "#e7f1fb",  # sky-200
    "G": "#f6e9d4",
    "H": "#d2e7f8",
    "I": "#edf1f5",
}
WAIT_COLOR = "#8a93ad"   # fg-3, used for waiting time
DEADLINE_COLOR = RED

_FONT_DIR = Path(__file__).resolve().parent.parent / "fonts-ttf"


def use_course_style() -> None:
    """Register the website fonts and set matplotlib defaults."""
    for ttf in _FONT_DIR.glob("*.ttf"):
        font_manager.fontManager.addfont(str(ttf))
    plt.rcParams.update({
        "font.family": "Inter",
        "font.size": 12,
        "text.color": INK,
        "axes.labelcolor": FG_2,
        "axes.edgecolor": BORDER_STRONG,
        "axes.titlesize": 14,
        "axes.titleweight": "semibold",
        "axes.titlecolor": INK,
        "axes.titlelocation": "left",
        "axes.titlepad": 12,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": False,
        "grid.color": BORDER,
        "grid.linewidth": 0.8,
        "xtick.color": FG_2,
        "ytick.color": FG_2,
        "legend.frameon": False,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.prop_cycle": plt.cycler(color=[PRIMARY, SKY_500, AMBER, RED, GREEN, FG_2]),
    })


def _title(ax, text: str | None) -> None:
    if text:
        ax.set_title(text, fontfamily="Poppins")


def _bar(ax, y, start, length, task, label=None, height=0.62, color=None, text_color=INK):
    ax.barh(y, length, left=start, height=height, color=color or TASK_COLORS.get(task, BORDER),
            edgecolor=INK, linewidth=0.8)
    if label:
        ax.text(start + 2, y, label, va="center", ha="left", fontsize=12, color=text_color)


def _time_axis(ax, end, step=10, major=60, clock_start=None):
    ax.set_xlim(0, end)
    ax.set_xticks(range(0, end + 1, major))
    ax.set_xticks(range(0, end + 1, step), minor=True)
    if clock_start is not None:
        h0, m0 = clock_start
        ax.set_xticklabels([f"{h0 + (m0 + t) // 60}:{(m0 + t) % 60:02d}" for t in range(0, end + 1, major)])
        ax.set_xlabel("")
    else:
        ax.set_xlabel("Minutes")
    ax.grid(True, axis="x", which="both", color=BORDER, linewidth=0.6)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)


# --- Task lists (input view) ----------------------------------------------
def task_durations(columns: dict[str, dict[str, int]], title: str | None = None, width=9, height=3.2):
    """Bars of task durations, one panel per resource (e.g. washing and drying)."""
    fig, axes = plt.subplots(1, len(columns), figsize=(width, height), sharex=True, squeeze=False)
    longest = max(max(c.values()) for c in columns.values())
    for ax, (name, tasks) in zip(axes[0], columns.items()):
        names = list(tasks)[::-1]
        for y, t in enumerate(names):
            _bar(ax, y, 0, tasks[t], t, f"{tasks[t]} min")
        ax.set_yticks(range(len(names)), names, fontsize=13)
        ax.set_xlim(0, longest * 1.1)
        ax.set_xticks([])
        for s in ("left", "bottom"):
            ax.spines[s].set_visible(False)
        ax.tick_params(axis="y", length=0)
        ax.set_title(name, fontfamily="Poppins")
    if title:
        fig.suptitle(title, fontfamily="Poppins", x=0.02, ha="left")
    fig.tight_layout()
    return fig


# --- Two machines (Johnson) -----------------------------------------------
def two_machine_schedule(order: str, first: dict[str, int], second: dict[str, int]):
    """Start/finish times of a permutation flow shop with two machines."""
    t1 = t2 = 0
    plan = []
    for job in order:
        s1 = t1
        t1 = s1 + first[job]
        s2 = max(t2, t1)
        t2 = s2 + second[job]
        plan.append((job, s1, first[job], s2, second[job]))
    return plan, t2


def johnson_order(first: dict[str, int], second: dict[str, int]) -> str:
    """Johnson's rule: shortest time on machine 1 goes first, on machine 2 last."""
    remaining = list(first)
    front, back = [], []
    while remaining:
        candidates = [(first[j], 1, j) for j in remaining] + [(second[j], 2, j) for j in remaining]
        _, machine, job = min(candidates)
        if machine == 1:
            front.append(job)
        else:
            back.insert(0, job)
        remaining.remove(job)
    return "".join(front + back)


def johnson_gantt(order: str, first: dict[str, int], second: dict[str, int],
                  labels=("Washing", "Drying"), title: str | None = None, end: int | None = None,
                  width=10, height=2.6):
    plan, makespan = two_machine_schedule(order, first, second)
    fig, ax = plt.subplots(figsize=(width, height))
    for job, s1, d1, s2, d2 in plan:
        _bar(ax, 1, s1, d1, job, job)
        _bar(ax, 0, s2, d2, job, job)
    ax.set_yticks([1, 0], labels, fontsize=12)
    _time_axis(ax, end or (makespan // 60 + 1) * 60)
    ax.axvline(makespan, color=PRIMARY, linewidth=1.6)
    ax.text(makespan + 3, 1.45, f"{makespan} min = {makespan // 60} h {makespan % 60} min",
            color=PRIMARY, fontsize=12, va="center", fontweight="semibold")
    ax.set_ylim(-0.6, 1.7)
    _title(ax, title)
    fig.tight_layout()
    return fig


# --- One machine ------------------------------------------------------------
def single_machine_gantt(order: str, durations: dict[str, int], deadlines: dict[str, int] | None = None,
                         show_wait=False, show_late=True, row_labels: dict[str, str] | None = None,
                         title: str | None = None, end: int | None = None, width=10, height=3.0):
    """One row per task in processing order; optional deadline markers and waiting time."""
    fig, ax = plt.subplots(figsize=(width, height))
    t = 0
    rows = list(order)
    finish = {}
    for i, job in enumerate(rows):
        y = len(rows) - 1 - i
        if show_wait and t > 0:
            ax.barh(y, t, left=0, height=0.62, color=WAIT_COLOR, alpha=0.55, edgecolor="none")
        _bar(ax, y, t, durations[job], job, f"{durations[job]} min")
        t += durations[job]
        finish[job] = t
        if deadlines:
            dl = deadlines[job]
            ax.plot([dl, dl], [y - 0.38, y + 0.38], color=DEADLINE_COLOR, linewidth=3, solid_capstyle="butt")
            if show_late and t > dl:
                ax.text(t + 2, y, f"{t - dl} min late", va="center", fontsize=11, color=DEADLINE_COLOR)
    labels = [(row_labels or {}).get(j, j) for j in rows]
    ax.set_yticks(range(len(rows) - 1, -1, -1), labels, fontsize=12)
    horizon = end or max([t] + list((deadlines or {}).values())) + 30
    _time_axis(ax, horizon, major=30 if horizon <= 240 else 60)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    _title(ax, title)
    fig.tight_layout()
    return fig, finish


def lawler_order(durations: dict[str, int], deadlines: dict[str, int], predecessor: dict[str, str | None]) -> str:
    """Lawler (1973) for 1|prec|Lmax: repeatedly put the job without open successors
    and the latest deadline at the end."""
    remaining = set(durations)
    order = []
    while remaining:
        free = [j for j in remaining if not any(predecessor.get(k) == j for k in remaining)]
        last = max(free, key=lambda j: (deadlines[j], j))
        order.insert(0, last)
        remaining.remove(last)
    return "".join(order)


# --- Real-time (preemptive) scheduling --------------------------------------
def simulate_realtime(tasks: list[dict], rule: str, step: int = 10):
    """Preemptive single-machine simulation.

    tasks: dicts with name, release, duration, deadline (minutes from start).
    rule: "edd" (earliest deadline) or "spt" (shortest duration). On a tie the
    running task continues (avoids a needless context switch).
    Returns a list of (name, start, length) segments and the finish times.
    """
    key = {"edd": lambda t: t["deadline"], "spt": lambda t: t["duration"]}[rule]
    left = {t["name"]: t["duration"] for t in tasks}
    segments, finish, now, current = [], {}, 0, None
    while left:
        ready = [t for t in tasks if t["name"] in left and t["release"] <= now]
        if not ready:
            now += step
            current = None
            continue
        best = min(ready, key=lambda t: (key(t), tasks.index(t)))
        if current in left and key(next(t for t in tasks if t["name"] == current)) <= key(best):
            best = next(t for t in tasks if t["name"] == current)
        name = best["name"]
        if segments and segments[-1][0] == name and segments[-1][1] + segments[-1][2] == now:
            segments[-1] = (name, segments[-1][1], segments[-1][2] + step)
        else:
            segments.append((name, now, step))
        left[name] -= step
        now += step
        current = name
        if left[name] == 0:
            del left[name]
            finish[name] = now
            current = None
    return segments, finish


def realtime_gantt(tasks: list[dict], rule: str, show_wait=False, deadlines=True, show_late=True,
                   clock_start=(8, 0), title: str | None = None, end: int = 240, width=10.5, height=3.6):
    segments, finish = simulate_realtime(tasks, rule)
    fig, ax = plt.subplots(figsize=(width, height))
    n = len(tasks)
    colors = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    for i, t in enumerate(tasks):
        y = n - 1 - i
        color = TASK_COLORS[colors[i]]
        if show_wait:
            # waiting = time in the system that is not processing
            busy = [(s, s + l) for name, s, l in segments if name == t["name"]]
            cursor = t["release"]
            for s, e in sorted(busy):
                if s > cursor:
                    ax.barh(y, s - cursor, left=cursor, height=0.62, color=WAIT_COLOR, alpha=0.55, edgecolor="none")
                cursor = e
        for name, s, l in segments:
            if name == t["name"]:
                ax.barh(y, l, left=s, height=0.62, color=color, edgecolor=INK, linewidth=0.8)
        ax.plot([t["release"]] * 2, [y - 0.38, y + 0.38], color=FG_3, linewidth=1.2)
        if deadlines:
            ax.plot([t["deadline"]] * 2, [y - 0.38, y + 0.38], color=DEADLINE_COLOR, linewidth=3, solid_capstyle="butt")
            late = finish[t["name"]] - t["deadline"]
            if show_late and late > 0:
                ax.text(finish[t["name"]] + 2, y, f"+{late} min", va="center", fontsize=10, color=DEADLINE_COLOR)
    ax.set_yticks(range(n - 1, -1, -1), [f'{t["name"]} ({t["duration"]} min)' for t in tasks], fontsize=11)
    _time_axis(ax, end, major=60, clock_start=clock_start)
    ax.set_ylim(-0.6, n - 0.4)
    _title(ax, title)
    fig.tight_layout()
    return fig, segments, finish


# --- Dependencies -----------------------------------------------------------
def dependency_diagram(first: tuple[str, int], second: tuple[str, int], note: str | None = None,
                       width=5.2, height=1.3):
    """Two tasks with a precedence arrow: first must finish before second starts."""
    fig, ax = plt.subplots(figsize=(width, height))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2)
    ax.axis("off")
    for x, (name, dur) in ((0.2, first), (6.2, second)):
        ax.add_patch(FancyBboxPatch((x, 0.75), 3.6, 1.0, boxstyle="round,pad=0.02,rounding_size=0.15",
                                    facecolor=TASK_COLORS.get(name, BORDER), edgecolor=INK, linewidth=0.8))
        ax.text(x + 0.3, 1.25, name, fontsize=15, fontfamily="Poppins", fontweight="semibold", va="center")
        ax.text(x + 1.3, 1.25, f"{dur} min", fontsize=13, va="center")
    ax.add_patch(FancyArrowPatch((3.95, 1.25), (6.05, 1.25), arrowstyle="-|>", mutation_scale=18,
                                 color=INK, linewidth=1.4))
    if note:
        ax.text(5.0, 0.2, note, ha="center", fontsize=10, color=FG_2)
    fig.tight_layout()
    return fig


# --- Memory hierarchy (Lecture III) -----------------------------------------
def latency_ladder(levels: list[tuple[str, float, str]], title: str | None = None, source: str | None = None,
                   width=10, height=3.8):
    """Horizontal log-scale bars: (name, latency in ns, typical size)."""
    import numpy as np

    fig, ax = plt.subplots(figsize=(width, height))
    names = [l[0] for l in levels][::-1]
    values = [l[1] for l in levels][::-1]
    sizes = [l[2] for l in levels][::-1]
    shades = np.linspace(0.25, 1.0, len(levels))
    for y, (v, a) in enumerate(zip(values, shades)):
        ax.barh(y, v, color=PRIMARY, alpha=float(a) * 0.85, height=0.62)
        ax.text(v * 1.4, y, _fmt_ns(v), va="center", fontsize=11, color=INK)
    ax.set_xscale("log")
    ax.set_xlim(0.1, 1e9)
    ax.set_yticks(range(len(names)), [f"{n}\n{s}" for n, s in zip(names, sizes)], fontsize=10.5)
    ax.set_xticks([1, 1e3, 1e6, 1e9], ["1 ns", "1 µs", "1 ms", "1 s"])
    ax.grid(True, axis="x", color=BORDER)
    ax.set_axisbelow(True)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.set_xlabel("Typical access time (log scale)")
    _title(ax, title)
    if source:
        fig.text(0.01, 0.01, source, fontsize=8.5, color=FG_3)
    fig.tight_layout(rect=(0, 0.04 if source else 0, 1, 1))
    return fig


def _fmt_ns(v: float) -> str:
    if v < 1e3:
        return f"{v:g} ns"
    if v < 1e6:
        return f"{v / 1e3:g} µs"
    return f"{v / 1e6:g} ms"
