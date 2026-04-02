from __future__ import annotations

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd

from plot_theme import (
    AX_BG,
    BLUE_LINE,
    FIG_BG,
    GRID,
    REGIME_COLORS,
    SUBTEXT,
    TEXT,
    WHITE_LINE,
    style_dark_axis,
)


DAILY_PATH = Path.cwd() / "results" / "reversal_3_1_regime_score" / "reversal_3_1_regime_daily.csv"
SEGMENTS_PATH = Path.cwd() / "results" / "reversal_3_1_regime_score" / "reversal_3_1_regime_segments.csv"
PLOT_PATH = Path.cwd() / "assets" / "reversal_3_1_regime_score.png"

def main() -> None:
    daily = pd.read_csv(DAILY_PATH, parse_dates=["Date"])
    segments = pd.read_csv(SEGMENTS_PATH, parse_dates=["start_date", "end_date"])

    fig, (ax_market, ax_strategy) = plt.subplots(
        2,
        1,
        figsize=(15, 9),
        sharex=True,
        gridspec_kw={"height_ratios": [1.0, 1.0]},
        facecolor=FIG_BG,
    )

    for _, row in segments.iterrows():
        start = row["start_date"]
        end = row["end_date"] + pd.Timedelta(days=1)
        shade = REGIME_COLORS.get(str(row["regime"]), "#374151")
        for ax in (ax_market, ax_strategy):
            ax.axvspan(start, end, color=shade, alpha=0.16, linewidth=0, zorder=0)

    ax_market.plot(daily["Date"], daily["market_norm"], color=WHITE_LINE, linewidth=2.2, zorder=3)
    ax_strategy.plot(daily["Date"], daily["strategy_equity_norm"], color=BLUE_LINE, linewidth=2.2, zorder=3)

    market_ymax = float(daily["market_norm"].max())
    market_ymin = float(daily["market_norm"].min())
    ax_market.set_ylim(market_ymin * 0.96, market_ymax * 1.10)

    for _, row in segments.iterrows():
        if int(row["trading_days"]) < 12:
            continue
        midpoint = row["start_date"] + (row["end_date"] - row["start_date"]) / 2
        ax_market.text(
            midpoint,
            market_ymax * 1.05,
            f"{row['regime_label']}\nScore {row['avg_reversal_score']:.0f}",
            ha="center",
            va="top",
            fontsize=8,
            color=TEXT,
            bbox={
                "boxstyle": "round,pad=0.25",
                "facecolor": "#0f172a",
                "edgecolor": "#334155",
                "alpha": 0.75,
            },
            zorder=4,
        )

    ax_market.set_title("Reversal 3.1 Market-Regime Study", fontsize=16, pad=14)
    ax_market.set_ylabel("QQQ (start=100)")
    ax_strategy.set_ylabel("Strategy Equity (start=100)")
    ax_strategy.set_xlabel("Date")

    style_dark_axis(ax_market)
    style_dark_axis(ax_strategy)

    handles = [
        Line2D([0], [0], color=REGIME_COLORS["favorable"], linewidth=8, alpha=0.9, label="Favorable"),
        Line2D([0], [0], color=REGIME_COLORS["selective"], linewidth=8, alpha=0.9, label="Selective"),
        Line2D([0], [0], color=REGIME_COLORS["caution"], linewidth=8, alpha=0.9, label="Caution"),
        Line2D([0], [0], color=REGIME_COLORS["risk_off"], linewidth=8, alpha=0.9, label="Risk-Off"),
    ]
    legend = ax_strategy.legend(handles=handles, loc="upper left", ncol=4, frameon=False, fontsize=10)
    for text in legend.get_texts():
        text.set_color(TEXT)

    ax_strategy.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax_strategy.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    fig.autofmt_xdate()
    fig.tight_layout()
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOT_PATH, dpi=170, bbox_inches="tight", facecolor=FIG_BG)
    plt.close(fig)
    print(f"Saved dark plot -> {PLOT_PATH}")


if __name__ == "__main__":
    main()
