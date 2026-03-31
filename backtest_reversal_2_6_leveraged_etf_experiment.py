from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

import backtest_reversal_2_5_calls as base


VARIANTS: dict[str, list[str]] = {
    "baseline_qqq_only_filtered": [],
    "plus_tqqq": ["TQQQ"],
    "plus_soxl": ["SOXL"],
    "plus_upro": ["UPRO"],
    "plus_soxl_upro": ["SOXL", "UPRO"],
    "plus_tqqq_soxl_upro": ["TQQQ", "SOXL", "UPRO"],
}
ROBUSTNESS_YEARS = [1, 2, 3]

RESULTS_DIR = Path.cwd() / "results" / "reversal_2_6_leveraged_etf_experiment"
SUMMARY_PATH = RESULTS_DIR / "reversal_2_6_leveraged_etf_summary.csv"
ROBUSTNESS_PATH = RESULTS_DIR / "reversal_2_6_leveraged_etf_robustness.csv"
EQUITY_PATH = RESULTS_DIR / "reversal_2_6_leveraged_etf_equity.csv"
PLOT_PATH = Path.cwd() / "assets" / "reversal_2_6_leveraged_etf_experiment.png"


def build_variant_tickers(baseline: list[str], extras: list[str]) -> list[str]:
    return sorted(set(baseline).union(extras))


def run_variant_summary(
    years: int,
    baseline: list[str],
    history_cache: dict[str, base.PreparedHistory],
) -> tuple[pd.DataFrame, dict[str, pd.DataFrame]]:
    rows: list[dict[str, object]] = []
    equity_curves: dict[str, pd.DataFrame] = {}

    for label, extras in VARIANTS.items():
        tickers = build_variant_tickers(baseline, extras)
        equity_df, trades_df, summary = base.summarize_backtest(label, tickers, history_cache)
        equity_curves[label] = equity_df
        rows.append(
            {
                "years": years,
                "label": label,
                "extra_tickers": ",".join(extras),
                "usable_tickers": summary["usable_tickers"],
                "final_equity": summary["final_equity"],
                "total_return_pct": summary["total_return_pct"],
                "max_drawdown_pct": summary["max_drawdown_pct"],
                "trade_count": summary["trade_count"],
                "win_rate_pct": summary["win_rate_pct"],
                "sharpe_rf_10y_tbill": summary["sharpe_rf_10y_tbill"],
                "extra_trade_count": int(trades_df["ticker"].isin(extras).sum()) if extras and not trades_df.empty else 0,
            }
        )

    return pd.DataFrame(rows), equity_curves


def plot_one_year_comparison(equity_curves: dict[str, pd.DataFrame]) -> None:
    plt.figure(figsize=(12, 7))
    for label, equity_df in equity_curves.items():
        plt.plot(equity_df["date"], equity_df["equity"] / base.INITIAL_CAPITAL, linewidth=2, label=label)

    plt.axhline(1.0, color="gray", linestyle="--", alpha=0.45)
    plt.title("Reversal 2.6 Leveraged ETF Overlay Experiment (1Y)")
    plt.xlabel("Date")
    plt.ylabel("Equity / Initial Capital")
    plt.grid(alpha=0.25)
    plt.legend()
    plt.tight_layout()
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(PLOT_PATH, dpi=160, bbox_inches="tight")
    plt.close()


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    presets = base.build_universe_presets()
    baseline = presets["qqq_only_filtered"]
    all_tickers = sorted(set(baseline).union(*[set(extras) for extras in VARIANTS.values()]))
    end_date = pd.Timestamp.today().normalize() + pd.Timedelta(days=1)

    original_years = base.BACKTEST_YEARS
    robustness_frames: list[pd.DataFrame] = []
    one_year_curves: dict[str, pd.DataFrame] = {}

    try:
        for years in ROBUSTNESS_YEARS:
            base.BACKTEST_YEARS = years
            trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=years)).normalize()
            data_start = trade_start - pd.DateOffset(days=700)
            history_cache = base.load_history_cache(
                all_tickers,
                data_start.strftime("%Y-%m-%d"),
                end_date.strftime("%Y-%m-%d"),
            )
            summary_df, equity_curves = run_variant_summary(years, baseline, history_cache)
            robustness_frames.append(summary_df)
            if years == 1:
                one_year_curves = equity_curves
    finally:
        base.BACKTEST_YEARS = original_years

    robustness_df = pd.concat(robustness_frames, ignore_index=True)
    one_year_summary = robustness_df.loc[robustness_df["years"] == 1].copy()

    merged_equity: pd.DataFrame | None = None
    for label, equity_df in one_year_curves.items():
        curve_df = equity_df[["date", "equity"]].rename(columns={"equity": label})
        merged_equity = curve_df if merged_equity is None else merged_equity.merge(curve_df, on="date", how="outer")

    if merged_equity is None:
        merged_equity = pd.DataFrame(columns=["date"])

    one_year_summary.to_csv(SUMMARY_PATH, index=False)
    robustness_df.to_csv(ROBUSTNESS_PATH, index=False)
    merged_equity.sort_values("date").to_csv(EQUITY_PATH, index=False)
    plot_one_year_comparison(one_year_curves)

    print("1Y summary:")
    print(one_year_summary.sort_values("total_return_pct", ascending=False).to_string(index=False))
    print("\n1Y/2Y/3Y robustness:")
    print(robustness_df.to_string(index=False))
    print(f"\nSaved summary -> {SUMMARY_PATH}")
    print(f"Saved robustness -> {ROBUSTNESS_PATH}")
    print(f"Saved equity -> {EQUITY_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")


if __name__ == "__main__":
    main()
