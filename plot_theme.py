from __future__ import annotations

from matplotlib.axes import Axes


FIG_BG = "#0b0d12"
AX_BG = "#11151c"
GRID = "#283241"
TEXT = "#e5e7eb"
SUBTEXT = "#9ca3af"
WHITE_LINE = "#f5f5f7"
BLUE_LINE = "#3b82f6"
GREEN_LINE = "#34C759"
RED_LINE = "#FF453A"
BASELINE = "#6b7280"

REGIME_COLORS = {
    "favorable": "#14532d",
    "selective": "#854d0e",
    "caution": "#9a3412",
    "risk_off": "#7f1d1d",
}


def style_dark_axis(ax: Axes) -> None:
    ax.set_facecolor(AX_BG)
    ax.grid(color=GRID, alpha=0.35, linewidth=0.8)
    ax.tick_params(colors=SUBTEXT, labelsize=10)
    for spine in ax.spines.values():
        spine.set_color("#1f2937")
    ax.yaxis.label.set_color(TEXT)
    ax.xaxis.label.set_color(TEXT)
    ax.title.set_color(TEXT)
