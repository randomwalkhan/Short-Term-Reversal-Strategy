from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from backtest_metrics import TEN_YEAR_TBILL_DATE, TEN_YEAR_TBILL_RATE, compute_annualized_sharpe
from backtest_reversal_3_1_calls import (
    INITIAL_CAPITAL,
    OFFICIAL_UNIVERSE_NAME,
    build_universe_presets,
    load_history_cache,
)
from backtest_reversal_3_3_timing_overlay_experiment import (
    build_candidate_dataset,
    build_equity_curve_with_overlay,
    compute_walk_forward_scores,
)
from plot_theme import BASELINE, FIG_BG, GREEN_LINE, TEXT, style_dark_axis, style_date_axis


VERSION = "3.3"
TIMING_WINDOW = 5
TIMING_THRESHOLD = 0.50
OFFICIAL_BACKTEST_YEARS = 1
TRAINING_WARMUP_YEARS = 3

OUTPUT_DIR = Path.cwd() / "results" / "reversal_3_3"
SUMMARY_PATH = OUTPUT_DIR / "reversal_3_3_summary.csv"
TRADES_PATH = OUTPUT_DIR / "reversal_3_3_call_backtest_trades.csv"
EQUITY_PATH = OUTPUT_DIR / "reversal_3_3_call_backtest_equity.csv"
COMPARISON_PATH = OUTPUT_DIR / "reversal_3_3_baseline_comparison.csv"
PLOT_PATH = Path.cwd() / "assets" / "reversal_3_3_call_backtest_equity.png"


def summarize_result(label: str, equity_df: pd.DataFrame, trades_df: pd.DataFrame, tickers: list[str]) -> dict[str, float | str | int]:
    final_equity = float(equity_df["equity"].iloc[-1])
    total_return_pct = (final_equity / INITIAL_CAPITAL - 1.0) * 100.0
    max_drawdown_pct = float(((equity_df["equity"] / equity_df["equity"].cummax()) - 1.0).min() * 100.0)
    win_rate_pct = float((trades_df["pnl"] > 0).mean() * 100.0) if not trades_df.empty else 0.0
    sharpe_rf_10y_tbill = compute_annualized_sharpe(equity_df)
    return {
        "label": label,
        "universe_name": OFFICIAL_UNIVERSE_NAME,
        "universe_size": len(tickers),
        "final_equity": final_equity,
        "total_return_pct": total_return_pct,
        "max_drawdown_pct": max_drawdown_pct,
        "trade_count": int(len(trades_df)),
        "win_rate_pct": win_rate_pct,
        "timing_window": TIMING_WINDOW if label == "reversal_3_3_official" else None,
        "timing_threshold": TIMING_THRESHOLD if label == "reversal_3_3_official" else None,
        "sharpe_rf_10y_tbill": sharpe_rf_10y_tbill,
        "risk_free_rate_annual": TEN_YEAR_TBILL_RATE,
        "risk_free_rate_source_date": TEN_YEAR_TBILL_DATE,
    }


def plot_equity_curve(equity_df: pd.DataFrame) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    date_series = pd.to_datetime(equity_df["date"], errors="coerce")
    valid_dates = date_series[date_series.notna()]
    if not valid_dates.empty:
        date_label = f"{valid_dates.min():%Y-%m-%d} to {valid_dates.max():%Y-%m-%d}"
    else:
        date_label = "date unavailable"

    fig, ax = plt.subplots(figsize=(12, 7), facecolor=FIG_BG)
    ax.plot(equity_df["date"], equity_df["equity"], linewidth=2.2, label="Strategy", color=GREEN_LINE)
    ax.axhline(INITIAL_CAPITAL, color=BASELINE, linestyle="--", alpha=0.55, label="Initial Capital")
    ax.fill_between(equity_df["date"], equity_df["equity"], INITIAL_CAPITAL, color=GREEN_LINE, alpha=0.10)
    style_dark_axis(ax)
    ax.set_title(f"Short-Term Reversal Call Backtest\nBacktest window: {date_label}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value ($)")
    span_days = int((valid_dates.max() - valid_dates.min()).days) if not valid_dates.empty else None
    style_date_axis(ax, span_days=span_days)
    legend = ax.legend(frameon=False, loc="upper left")
    for text in legend.get_texts():
        text.set_color(TEXT)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=160, bbox_inches="tight", facecolor=FIG_BG)
    plt.close(fig)


def main() -> None:
    presets = build_universe_presets()
    tickers = presets[OFFICIAL_UNIVERSE_NAME]

    end_date = pd.Timestamp.today().normalize() + pd.Timedelta(days=1)
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=OFFICIAL_BACKTEST_YEARS)).normalize()
    candidate_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=TRAINING_WARMUP_YEARS)).normalize()
    data_start = candidate_start - pd.DateOffset(days=500)

    history_map = load_history_cache(sorted(set(tickers)), data_start.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
    candidate_df = build_candidate_dataset(history_map, candidate_start)
    if candidate_df.empty:
        raise RuntimeError("No candidate events were generated for the official Reversal 3.3 backtest.")

    candidate_df[f"score_w{TIMING_WINDOW}"] = compute_walk_forward_scores(candidate_df, TIMING_WINDOW)
    candidate_trade_df = candidate_df[candidate_df["date"] >= trade_start].copy()
    if candidate_trade_df.empty:
        raise RuntimeError("No candidate events remain inside the official backtest window.")

    baseline_equity, baseline_trades = build_equity_curve_with_overlay(history_map, candidate_trade_df)
    official_equity, official_trades = build_equity_curve_with_overlay(
        history_map,
        candidate_trade_df,
        score_column=f"score_w{TIMING_WINDOW}",
        threshold=TIMING_THRESHOLD,
    )

    baseline_summary = summarize_result("baseline_no_timing_overlay", baseline_equity, baseline_trades, tickers)
    official_summary = summarize_result("reversal_3_3_official", official_equity, official_trades, tickers)
    summary_df = pd.DataFrame([official_summary])
    comparison_df = pd.DataFrame([baseline_summary, official_summary])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(SUMMARY_PATH, index=False)
    comparison_df.to_csv(COMPARISON_PATH, index=False)
    official_trades.to_csv(TRADES_PATH, index=False)
    official_equity.to_csv(EQUITY_PATH, index=False)
    plot_equity_curve(official_equity)

    print(f"Official Reversal {VERSION} summary:")
    print(summary_df.to_string(index=False))
    print("")
    print("Baseline comparison:")
    print(comparison_df.to_string(index=False))
    print(f"Saved summary -> {SUMMARY_PATH}")
    print(f"Saved comparison -> {COMPARISON_PATH}")
    print(f"Saved equity -> {EQUITY_PATH}")
    print(f"Saved trades -> {TRADES_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")


if __name__ == "__main__":
    main()
