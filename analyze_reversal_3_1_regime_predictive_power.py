from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import backtest_reversal_3_1_calls as base
from plot_theme import AX_BG, BLUE_LINE, FIG_BG, GREEN_LINE, RED_LINE, SUBTEXT, TEXT, style_dark_axis


STUDY_YEARS = 5
FORWARD_WINDOWS = [5, 10, 20]
THRESHOLDS = [0, 35, 50, 60, 70]
REGIME_DAILY_PATH = Path.cwd() / "results" / "reversal_3_1_regime_score" / "reversal_3_1_regime_daily.csv"

RESULTS_DIR = Path.cwd() / "results" / "reversal_3_1_regime_predictive_power"
FORWARD_SUMMARY_PATH = RESULTS_DIR / "reversal_3_1_forward_score_summary.csv"
BUCKET_SUMMARY_PATH = RESULTS_DIR / "reversal_3_1_score_bucket_negative_rate.csv"
GATING_SUMMARY_PATH = RESULTS_DIR / "reversal_3_1_regime_gating_summary.csv"
RECENT_WINDOW_PATH = RESULTS_DIR / "reversal_3_1_regime_gating_recent_window.csv"
GATING_EQUITY_PATH = RESULTS_DIR / "reversal_3_1_regime_gating_equity.csv"
PLOT_PATH = Path.cwd() / "assets" / "reversal_3_1_regime_gating_comparison.png"


@dataclass
class Position:
    ticker: str
    entry_date: pd.Timestamp
    expiry_date: pd.Timestamp
    entry_spot: float
    strike: float
    entry_option_price: float
    contracts: int
    success_rate: float
    matched_signals: int
    allocated_cash: float
    planned_tp_day1: float
    planned_tp_day2: float
    planned_stop: float
    day_count: int = 0


def load_score_frame() -> pd.DataFrame:
    df = pd.read_csv(REGIME_DAILY_PATH, parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)
    for window in FORWARD_WINDOWS:
        df[f"strategy_forward_{window}d_return"] = (df["equity"].shift(-window) / df["equity"] - 1) * 100
    return df


def summarize_forward_predictiveness(score_df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for window in FORWARD_WINDOWS:
        col = f"strategy_forward_{window}d_return"
        valid = score_df[["reversal_score", col]].dropna()
        rows.append(
            {
                "forward_window_days": window,
                "sample_size": len(valid),
                "pearson_corr": valid["reversal_score"].corr(valid[col], method="pearson"),
                "spearman_corr": valid["reversal_score"].corr(valid[col], method="spearman"),
                "avg_forward_return_pct": valid[col].mean(),
                "negative_forward_return_rate_pct": (valid[col] < 0).mean() * 100,
            }
        )
    out = pd.DataFrame(rows)
    for col in ["pearson_corr", "spearman_corr", "avg_forward_return_pct", "negative_forward_return_rate_pct"]:
        out[col] = out[col].round(4)
    return out


def summarize_buckets(score_df: pd.DataFrame) -> pd.DataFrame:
    df = score_df.copy()
    df["score_bucket"] = pd.cut(
        df["reversal_score"],
        bins=[-np.inf, 35, 50, 60, 70, np.inf],
        labels=["0-35", "35-50", "50-60", "60-70", "70-100"],
    ).astype("string")

    rows: list[dict[str, object]] = []
    for bucket, group in df.groupby("score_bucket", dropna=False):
        if pd.isna(bucket):
            continue
        row: dict[str, object] = {
            "score_bucket": str(bucket),
            "days": len(group),
            "avg_score": group["reversal_score"].mean(),
        }
        for window in FORWARD_WINDOWS:
            col = f"strategy_forward_{window}d_return"
            valid = group[col].dropna()
            row[f"avg_forward_{window}d_return_pct"] = valid.mean()
            row[f"negative_{window}d_rate_pct"] = (valid < 0).mean() * 100 if len(valid) else np.nan
        rows.append(row)

    out = pd.DataFrame(rows)
    numeric_cols = [col for col in out.columns if col != "score_bucket"]
    out[numeric_cols] = out[numeric_cols].round(2)
    return out


def build_history_cache() -> dict[str, base.PreparedHistory]:
    original_years = base.BACKTEST_YEARS
    try:
        base.BACKTEST_YEARS = STUDY_YEARS
        presets = base.build_universe_presets()
        tickers = presets[base.OFFICIAL_UNIVERSE_NAME]
        end_date = pd.Timestamp.today().normalize() + pd.Timedelta(days=1)
        trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=STUDY_YEARS)).normalize()
        data_start = trade_start - pd.DateOffset(days=700)
        return base.load_history_cache(
            sorted(set(tickers)),
            data_start.strftime("%Y-%m-%d"),
            end_date.strftime("%Y-%m-%d"),
        )
    finally:
        base.BACKTEST_YEARS = original_years


def build_equity_curve_gated(
    history_map: dict[str, base.PreparedHistory],
    score_map: dict[pd.Timestamp, float],
    threshold: float,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=STUDY_YEARS)).normalize()
    all_dates = sorted(
        {
            date
            for history in history_map.values()
            for date in history.df["Date"]
            if date >= trade_start
        }
    )

    cash = base.INITIAL_CAPITAL
    positions: list[Position] = []
    trade_rows: list[dict[str, Any]] = []
    equity_rows: list[dict[str, Any]] = []

    for current_date in all_dates:
        updated_positions: list[Position] = []
        for position in positions:
            history = history_map[position.ticker]
            idx = history.date_to_idx.get(current_date)
            if idx is None:
                updated_positions.append(position)
                continue

            row = history.df.iloc[idx]
            sigma_ann = float(row["Sigma Ann"])
            if np.isnan(sigma_ann) or sigma_ann <= 0:
                sigma_ann = 0.60

            position.day_count += 1
            option_high = base.mark_option_price(float(row["High"]), position.strike, position.entry_date, current_date, sigma_ann)
            option_low = base.mark_option_price(float(row["Low"]), position.strike, position.entry_date, current_date, sigma_ann)
            option_close = base.mark_option_price(float(row["Close"]), position.strike, position.entry_date, current_date, sigma_ann)

            exit_reason = None
            exit_price = None
            if option_low <= position.planned_stop:
                exit_reason = "stop"
                exit_price = position.planned_stop
            else:
                target = position.planned_tp_day1 if position.day_count == 1 else position.planned_tp_day2
                if option_high >= target:
                    exit_reason = "tp_day1" if position.day_count == 1 else "tp_day2"
                    exit_price = target
                elif position.day_count >= 2:
                    exit_reason = "time_exit"
                    exit_price = option_close

            if exit_reason is None or exit_price is None:
                updated_positions.append(position)
                continue

            proceeds = exit_price * 100 * position.contracts
            cash += proceeds
            pnl = proceeds - position.entry_option_price * 100 * position.contracts
            trade_rows.append(
                {
                    "ticker": position.ticker,
                    "entry_date": position.entry_date,
                    "exit_date": current_date,
                    "success_rate": position.success_rate,
                    "matched_signals": position.matched_signals,
                    "allocated_cash": position.allocated_cash,
                    "contracts": position.contracts,
                    "entry_option_price": position.entry_option_price,
                    "exit_option_price": exit_price,
                    "pnl": pnl,
                    "return_pct": pnl / (position.entry_option_price * 100 * position.contracts) * 100,
                    "exit_reason": exit_reason,
                    "gate_threshold": threshold,
                }
            )

        positions = updated_positions

        marked_position_value = 0.0
        for position in positions:
            history = history_map[position.ticker]
            idx = history.date_to_idx.get(current_date)
            if idx is None:
                continue
            row = history.df.iloc[idx]
            sigma_ann = float(row["Sigma Ann"])
            if np.isnan(sigma_ann) or sigma_ann <= 0:
                sigma_ann = 0.60
            mark = base.mark_option_price(float(row["Close"]), position.strike, position.entry_date, current_date, sigma_ann)
            marked_position_value += mark * 100 * position.contracts

        current_score = score_map.get(pd.Timestamp(current_date).normalize(), np.nan)
        gate_open = bool(pd.notna(current_score) and float(current_score) >= threshold)

        if gate_open and len(positions) < base.MAX_OPEN_POSITIONS:
            open_tickers = {position.ticker for position in positions}
            candidates = []
            for ticker, history in history_map.items():
                if ticker in open_tickers:
                    continue
                idx = history.date_to_idx.get(current_date)
                if idx is None or idx <= base.LOOKBACK_DAYS or idx + base.FORWARD_DAYS >= len(history.df):
                    continue
                candidate = base.evaluate_candidate(history, idx)
                if candidate is not None:
                    candidates.append(candidate)

            if candidates:
                candidate = max(candidates, key=lambda item: (item["success_rate"], item["matched_signals"]))
                entry_cost = candidate["entry_option_price"] * 100
                current_equity = cash + marked_position_value
                budget = min(cash, current_equity * base.TARGET_POSITION_WEIGHT)
                contracts = int(budget // entry_cost)
                if contracts > 0:
                    spent = contracts * entry_cost
                    cash -= spent
                    positions.append(
                        Position(
                            ticker=str(candidate["ticker"]),
                            entry_date=current_date,
                            expiry_date=base.next_business_day(current_date, base.TRADING_DTE_AT_ENTRY),
                            entry_spot=float(candidate["spot_close"]),
                            strike=float(candidate["spot_close"]),
                            entry_option_price=float(candidate["entry_option_price"]),
                            contracts=contracts,
                            success_rate=float(candidate["success_rate"]),
                            matched_signals=int(candidate["matched_signals"]),
                            allocated_cash=float(spent),
                            planned_tp_day1=float(candidate["entry_option_price"]) * (1 + base.DAY1_TAKE_PROFIT_PCT),
                            planned_tp_day2=float(candidate["entry_option_price"]) * (1 + base.DAY2_TAKE_PROFIT_PCT),
                            planned_stop=float(candidate["entry_option_price"]) * (1 - base.STOP_LOSS_PCT),
                        )
                    )
                    marked_position_value += spent

        equity_rows.append(
            {
                "date": current_date,
                "cash": cash,
                "position_value": marked_position_value,
                "equity": cash + marked_position_value,
                "open_count": len(positions),
                "gate_threshold": threshold,
                "gate_score": current_score,
                "gate_open": gate_open,
            }
        )

    return pd.DataFrame(equity_rows), pd.DataFrame(trade_rows)


def summarize_variant(label: str, threshold: float, equity_df: pd.DataFrame, trades_df: pd.DataFrame) -> dict[str, object]:
    final_equity = float(equity_df["equity"].iloc[-1])
    total_return = (final_equity / base.INITIAL_CAPITAL - 1) * 100
    max_drawdown = ((equity_df["equity"] / equity_df["equity"].cummax()) - 1).min() * 100
    win_rate = float((trades_df["pnl"] > 0).mean() * 100) if not trades_df.empty else 0.0
    gate_open_rate = float(equity_df["gate_open"].mean() * 100)
    return {
        "label": label,
        "threshold": threshold,
        "final_equity": round(final_equity, 2),
        "total_return_pct": round(total_return, 2),
        "max_drawdown_pct": round(float(max_drawdown), 2),
        "trade_count": int(len(trades_df)),
        "win_rate_pct": round(win_rate, 2),
        "days_gate_open_pct": round(gate_open_rate, 2),
    }


def plot_gating_comparison(merged_equity: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(13, 7), facecolor=FIG_BG)
    palette = {
        "Always On (0)": "#9ca3af",
        "Gate >= 35": "#22c55e",
        "Gate >= 50": "#38bdf8",
        "Gate >= 60": "#a78bfa",
        "Gate >= 70": "#f97316",
    }

    for column in merged_equity.columns:
        if column == "date":
            continue
        ax.plot(
            merged_equity["date"],
            merged_equity[column],
            linewidth=2.2,
            color=palette.get(column, BLUE_LINE),
            label=column,
        )

    style_dark_axis(ax)
    ax.set_title("Reversal 3.1 Regime-Gating Comparison")
    ax.set_ylabel("Equity ($)")
    ax.set_xlabel("Date")
    legend = ax.legend(frameon=False, loc="upper left", ncol=3)
    for text in legend.get_texts():
        text.set_color(TEXT)
    fig.tight_layout()
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PLOT_PATH, dpi=170, bbox_inches="tight", facecolor=FIG_BG)
    plt.close(fig)


def main() -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    score_df = load_score_frame()
    forward_summary = summarize_forward_predictiveness(score_df)
    bucket_summary = summarize_buckets(score_df)

    score_map = pd.Series(score_df["reversal_score"].values, index=pd.to_datetime(score_df["Date"]).dt.normalize()).to_dict()
    history_cache = build_history_cache()

    summary_rows: list[dict[str, object]] = []
    recent_rows: list[dict[str, object]] = []
    merged_equity: pd.DataFrame | None = None
    recent_start = pd.Timestamp("2026-03-06")

    for threshold in THRESHOLDS:
        label = "Always On (0)" if threshold == 0 else f"Gate >= {threshold}"
        equity_df, trades_df = build_equity_curve_gated(history_cache, score_map, threshold)
        summary_rows.append(summarize_variant(label, threshold, equity_df, trades_df))

        recent = equity_df[equity_df["date"] >= recent_start].copy()
        if not recent.empty:
            recent_rows.append(
                {
                    "label": label,
                    "threshold": threshold,
                    "recent_window_start": recent_start.date().isoformat(),
                    "recent_return_pct": round((float(recent["equity"].iloc[-1]) / float(recent["equity"].iloc[0]) - 1) * 100, 2),
                    "recent_max_drawdown_pct": round(float(((recent["equity"] / recent["equity"].cummax()) - 1).min() * 100), 2),
                    "recent_days_gate_open_pct": round(float(recent["gate_open"].mean() * 100), 2),
                }
            )

        curve = equity_df[["date", "equity"]].rename(columns={"equity": label})
        merged_equity = curve if merged_equity is None else merged_equity.merge(curve, on="date", how="outer")

    gating_summary = pd.DataFrame(summary_rows)
    recent_window = pd.DataFrame(recent_rows)

    forward_summary.to_csv(FORWARD_SUMMARY_PATH, index=False)
    bucket_summary.to_csv(BUCKET_SUMMARY_PATH, index=False)
    gating_summary.to_csv(GATING_SUMMARY_PATH, index=False)
    recent_window.to_csv(RECENT_WINDOW_PATH, index=False)
    merged_equity.sort_values("date").to_csv(GATING_EQUITY_PATH, index=False)
    plot_gating_comparison(merged_equity.sort_values("date"))

    print("Forward predictiveness:")
    print(forward_summary.to_string(index=False))
    print("\nBucket negative-rate summary:")
    print(bucket_summary.to_string(index=False))
    print("\nGating comparison:")
    print(gating_summary.to_string(index=False))
    print("\nRecent stress-window comparison:")
    print(recent_window.to_string(index=False))
    print(f"\nSaved forward summary -> {FORWARD_SUMMARY_PATH}")
    print(f"Saved bucket summary -> {BUCKET_SUMMARY_PATH}")
    print(f"Saved gating summary -> {GATING_SUMMARY_PATH}")
    print(f"Saved recent window -> {RECENT_WINDOW_PATH}")
    print(f"Saved gating equity -> {GATING_EQUITY_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")


if __name__ == "__main__":
    main()
