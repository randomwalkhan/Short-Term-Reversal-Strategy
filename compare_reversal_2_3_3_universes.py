from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from backtest_reversal_2_3_3_calls import (
    BACKTEST_YEARS,
    FORWARD_DAYS,
    INITIAL_CAPITAL,
    OUTPUT_DIR,
    RECOVER_TARGET,
    build_universe_presets,
    load_history_cache,
    summarize_backtest,
)


LOOKAHEAD_WINDOWS = [1, 2, 3, 4]
DROP_THR = 0.04
MIN_SIGNAL_DAYS = 11  # strictly greater than 10

RESULTS_DIR = Path.cwd() / "results" / "reversal_2_3_3_universe_comparison"
SUMMARY_PATH = RESULTS_DIR / "reversal_2_3_3_universe_comparison.csv"
PLOT_PATH = RESULTS_DIR / "reversal_2_3_3_universe_comparison.png"
ASSET_PLOT_PATH = Path.cwd() / "assets" / "reversal_2_3_3_universe_comparison.png"


def notebook_style_signal_summary(history) -> dict[str, object]:
    df = history.df.reset_index(drop=True)
    signal_rows: list[dict[str, object]] = []

    for idx, row in df[df["Max Drop"] >= DROP_THR].iterrows():
        prev_close = float(row["Prev Close"])
        low_today = float(row["Low"])
        fall_amt = float(row["Max Drop"]) * prev_close
        if fall_amt <= 0:
            continue

        hit = False
        has_window = False
        for window in LOOKAHEAD_WINDOWS:
            if idx + window >= len(df):
                break
            has_window = True
            high_n = pd.to_numeric(df.loc[idx + 1: idx + window, "High"], errors="coerce").max()
            recover_ratio = (high_n - low_today) / fall_amt
            if recover_ratio >= RECOVER_TARGET:
                hit = True

        if has_window:
            signal_rows.append(
                {
                    "ticker": history.ticker,
                    "signal_date": df.loc[idx, "Date"],
                    "success": hit,
                }
            )

    result = pd.DataFrame(signal_rows)
    signal_days = int(result["signal_date"].nunique()) if not result.empty else 0
    success_rate = float(result.groupby("signal_date")["success"].any().mean() * 100) if not result.empty else 0.0
    return {
        "ticker": history.ticker,
        "signal_days": signal_days,
        "success_rate": success_rate,
    }


def plot_comparison(equity_curves: dict[str, pd.DataFrame]) -> None:
    plt.figure(figsize=(13, 7))
    for label, equity_df in equity_curves.items():
        series = equity_df[["date", "equity"]].copy()
        plt.plot(series["date"], series["equity"] / INITIAL_CAPITAL, linewidth=1.8, label=label)

    plt.axhline(1.0, color="gray", linestyle="--", alpha=0.5)
    plt.title("Reversal 2.3.3 Universe Comparison (signal_days > 10)")
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

    signal_summary_rows = [notebook_style_signal_summary(history) for history in history_cache.values()]
    signal_summary_df = pd.DataFrame(signal_summary_rows)

    equity_curves: dict[str, pd.DataFrame] = {}
    summaries: list[dict[str, object]] = []
    for label, tickers in presets.items():
        eligible_df = signal_summary_df[
            (signal_summary_df["ticker"].isin(tickers))
            & (signal_summary_df["signal_days"] >= MIN_SIGNAL_DAYS)
        ].copy()
        eligible_tickers = eligible_df["ticker"].tolist()

        equity_df, trades_df, summary = summarize_backtest(label, eligible_tickers, history_cache)
        summary["candidate_universe_size"] = len(tickers)
        summary["signal_days_gate"] = f"> {MIN_SIGNAL_DAYS - 1}"
        summary["signal_filtered_size"] = len(eligible_tickers)
        summary["avg_signal_days"] = float(eligible_df["signal_days"].mean()) if not eligible_df.empty else 0.0
        summaries.append(summary)
        equity_curves[label] = equity_df

        equity_df.to_csv(RESULTS_DIR / f"{label}_equity.csv", index=False)
        trades_df.to_csv(RESULTS_DIR / f"{label}_trades.csv", index=False)
        eligible_df.sort_values(["success_rate", "signal_days"], ascending=[False, False]).to_csv(
            RESULTS_DIR / f"{label}_signal_filtered_universe.csv",
            index=False,
        )

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
