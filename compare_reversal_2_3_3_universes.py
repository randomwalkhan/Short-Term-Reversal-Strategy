from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from backtest_reversal_2_3_3_calls import (
    BACKTEST_YEARS,
    INITIAL_CAPITAL,
    OUTPUT_DIR,
    build_universe_presets,
    load_history_cache,
    summarize_backtest,
)


RESULTS_DIR = Path.cwd() / "results" / "reversal_2_3_3_universe_comparison"
SUMMARY_PATH = RESULTS_DIR / "reversal_2_3_3_universe_comparison.csv"
PLOT_PATH = RESULTS_DIR / "reversal_2_3_3_universe_comparison.png"
ASSET_PLOT_PATH = Path.cwd() / "assets" / "reversal_2_3_3_universe_comparison.png"


def plot_comparison(equity_curves: dict[str, pd.DataFrame]) -> None:
    plt.figure(figsize=(13, 7))
    for label, equity_df in equity_curves.items():
        series = equity_df[["date", "equity"]].copy()
        plt.plot(series["date"], series["equity"] / INITIAL_CAPITAL, linewidth=1.8, label=label)

    plt.axhline(1.0, color="gray", linestyle="--", alpha=0.5)
    plt.title("Reversal 2.3.3 Universe Comparison (dynamic matched_signals filter)")
    plt.xlabel("Date")
    plt.ylabel("Equity / Initial Capital")
    plt.grid(alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(PLOT_PATH, dpi=160, bbox_inches="tight")
    plt.savefig(ASSET_PLOT_PATH, dpi=160, bbox_inches="tight")
    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    ASSET_PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)

    presets = build_universe_presets()
    selected_labels = [
        "qqq_only_filtered",
        "spy_only_filtered",
        "qqq_spy_filtered",
        "nasdaq_only_filtered",
        "nasdaq_spy_filtered",
    ]
    presets = {label: presets[label] for label in selected_labels if label in presets}

    end_date = pd.Timestamp.today().normalize() + pd.Timedelta(days=1)
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=BACKTEST_YEARS)).normalize()
    data_start = trade_start - pd.DateOffset(days=500)

    all_tickers = sorted({ticker for tickers in presets.values() for ticker in tickers})
    history_cache = load_history_cache(
        all_tickers,
        data_start.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
    )

    equity_curves: dict[str, pd.DataFrame] = {}
    summaries: list[dict[str, object]] = []
    for label, tickers in presets.items():
        equity_df, trades_df, summary = summarize_backtest(label, tickers, history_cache)
        summary["candidate_universe_size"] = len(tickers)
        summary["dynamic_filter"] = "matched_signals >= 10"
        summaries.append(summary)
        equity_curves[label] = equity_df

        equity_df.to_csv(RESULTS_DIR / f"{label}_equity.csv", index=False)
        trades_df.to_csv(RESULTS_DIR / f"{label}_trades.csv", index=False)

    summary_df = pd.DataFrame(summaries).sort_values(
        ["win_rate_pct", "final_equity"],
        ascending=[False, False],
    )
    summary_df.to_csv(SUMMARY_PATH, index=False)
    plot_comparison(equity_curves)

    print(summary_df.to_string(index=False))
    print(f"Saved summary -> {SUMMARY_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")


if __name__ == "__main__":
    main()
