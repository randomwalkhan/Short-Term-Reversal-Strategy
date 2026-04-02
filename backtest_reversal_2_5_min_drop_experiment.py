from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import backtest_reversal_2_4_calls as base
from plot_theme import BASELINE, FIG_BG, TEXT, style_dark_axis


MINIMUM_DROP_PCTS = [0.00, 0.005, 0.01, 0.02, 0.03, 0.04]
RESULTS_DIR = Path.cwd() / "results" / "reversal_2_5_min_drop_experiment"
SUMMARY_PATH = RESULTS_DIR / "reversal_2_5_min_drop_summary.csv"
EQUITY_PATH = RESULTS_DIR / "reversal_2_5_min_drop_equity.csv"
PLOT_PATH = Path.cwd() / "assets" / "reversal_2_5_min_drop_experiment.png"


def build_min_drop_evaluator(minimum_drop_pct: float):
    original_evaluate_candidate = base.evaluate_candidate

    def evaluate_candidate(history: base.PreparedHistory, idx: int):
        current_drop_pct = float(history.max_drop[idx])
        if np.isnan(current_drop_pct) or current_drop_pct <= minimum_drop_pct:
            return None
        return original_evaluate_candidate(history, idx)

    return evaluate_candidate


def run_backtest_variant(
    label: str,
    tickers: list[str],
    history_cache: dict[str, base.PreparedHistory],
    minimum_drop_pct: float | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    original_evaluate_candidate = base.evaluate_candidate
    try:
        if minimum_drop_pct is not None:
            base.evaluate_candidate = build_min_drop_evaluator(minimum_drop_pct)
        equity_df, trades_df, summary = base.summarize_backtest(label, tickers, history_cache)
    finally:
        base.evaluate_candidate = original_evaluate_candidate

    summary["minimum_drop_pct"] = minimum_drop_pct if minimum_drop_pct is not None else 0.0
    return equity_df, trades_df, summary


def plot_comparison(equity_curves: dict[str, pd.DataFrame]) -> None:
    fig, ax = plt.subplots(figsize=(12, 7), facecolor=FIG_BG)
    for label, equity_df in equity_curves.items():
        ax.plot(equity_df["date"], equity_df["equity"] / base.INITIAL_CAPITAL, linewidth=2, label=label)

    ax.axhline(1.0, color=BASELINE, linestyle="--", alpha=0.5)
    style_dark_axis(ax)
    ax.set_title("Reversal 2.5 Minimum Drop Experiment")
    ax.set_xlabel("Date")
    ax.set_ylabel("Equity / Initial Capital")
    legend = ax.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color(TEXT)
    fig.tight_layout()
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOT_PATH, dpi=160, bbox_inches="tight", facecolor=FIG_BG)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    presets = base.build_universe_presets()
    tickers = presets["qqq_only_filtered"]
    end_date = pd.Timestamp.today().normalize() + pd.Timedelta(days=1)
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=base.BACKTEST_YEARS)).normalize()
    data_start = trade_start - pd.DateOffset(days=500)
    history_cache = base.load_history_cache(
        sorted(set(tickers)),
        data_start.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
    )

    summaries: list[dict[str, object]] = []
    equity_curves: dict[str, pd.DataFrame] = {}
    merged_equity: pd.DataFrame | None = None

    for minimum_drop_pct in MINIMUM_DROP_PCTS:
        label = "baseline_60d" if minimum_drop_pct == 0 else f"min_drop_{minimum_drop_pct * 100:.1f}pct"
        equity_df, trades_df, summary = run_backtest_variant(
            label=label,
            tickers=tickers,
            history_cache=history_cache,
            minimum_drop_pct=None if minimum_drop_pct == 0 else minimum_drop_pct,
        )
        summary["variant"] = label
        summaries.append(summary)
        equity_curves[label] = equity_df

        equity_col = label
        curve_df = equity_df[["date", "equity"]].rename(columns={"equity": equity_col})
        merged_equity = curve_df if merged_equity is None else merged_equity.merge(curve_df, on="date", how="outer")

        trades_path = RESULTS_DIR / f"{label}_trades.csv"
        trades_df.to_csv(trades_path, index=False)

    summary_df = pd.DataFrame(summaries).sort_values("minimum_drop_pct").reset_index(drop=True)
    if merged_equity is None:
        merged_equity = pd.DataFrame(columns=["date"])
    merged_equity = merged_equity.sort_values("date").reset_index(drop=True)

    summary_df.to_csv(SUMMARY_PATH, index=False)
    merged_equity.to_csv(EQUITY_PATH, index=False)
    plot_comparison(equity_curves)

    print(summary_df.to_string(index=False))
    print(f"Saved summary -> {SUMMARY_PATH}")
    print(f"Saved equity -> {EQUITY_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")


if __name__ == "__main__":
    main()
