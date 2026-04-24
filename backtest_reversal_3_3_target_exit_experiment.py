from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from backtest_metrics import TEN_YEAR_TBILL_DATE, TEN_YEAR_TBILL_RATE, compute_annualized_sharpe
from backtest_reversal_3_1_calls import (
    FORWARD_DAYS,
    INITIAL_CAPITAL,
    LOOKBACK_DAYS,
    MAX_OPEN_POSITIONS,
    OFFICIAL_UNIVERSE_NAME,
    RECOVER_TARGET,
    TARGET_POSITION_WEIGHT,
    TRADING_DTE_AT_ENTRY,
    PreparedHistory,
    bs_call,
    build_universe_presets,
    load_history_cache,
    mark_option_price,
)
from backtest_reversal_3_3_timing_overlay_experiment import (
    build_candidate_dataset,
    compute_walk_forward_scores,
    event_key,
    score_map_for_variant,
)
from plot_theme import BASELINE, FIG_BG, GREEN_LINE, RED_LINE, TEXT, style_dark_axis, style_date_axis


VERSION = "3.3"
TIMING_WINDOW = 5
TIMING_THRESHOLD = 0.50
OFFICIAL_BACKTEST_YEARS = 1
TRAINING_WARMUP_YEARS = 3
STOP_PCT = 0.12

OUTPUT_DIR = Path.cwd() / "results" / "reversal_3_3_target_exit_experiment"
SUMMARY_PATH = OUTPUT_DIR / "reversal_3_3_target_exit_summary.csv"
TRADES_PATH = OUTPUT_DIR / "reversal_3_3_target_exit_trades.csv"
EQUITY_PATH = OUTPUT_DIR / "reversal_3_3_target_exit_equity.csv"
PLOT_PATH = Path.cwd() / "assets" / "reversal_3_3_target_exit_experiment.png"


@dataclass(frozen=True)
class ExitPolicy:
    label: str
    mode: str
    target_reference: str = "close"
    stop_mode: str = "fixed_12"
    fixed_tp_pct: float = 0.15
    fixed_stop_pct: float = STOP_PCT


@dataclass
class Position:
    ticker: str
    entry_date: pd.Timestamp
    strike: float
    entry_option_price: float
    contracts: int
    success_rate: float
    matched_signals: int
    allocated_cash: float
    planned_tp: float
    planned_stop: float
    target_spot: float
    stop_spot: float | None
    day_count: int = 0


POLICIES = [
    ExitPolicy(label="fixed_15_12", mode="fixed", fixed_tp_pct=0.15, fixed_stop_pct=0.12),
    ExitPolicy(label="target_close_stop12", mode="target", target_reference="close", stop_mode="fixed_12"),
    ExitPolicy(label="target_low_stop12", mode="target", target_reference="low", stop_mode="fixed_12"),
    ExitPolicy(label="target_close_symmetric_stop", mode="target", target_reference="close", stop_mode="symmetric_stock"),
    ExitPolicy(label="target_low_symmetric_stop", mode="target", target_reference="low", stop_mode="symmetric_stock"),
]


def _safe_sigma(value: float) -> float:
    return float(value) if np.isfinite(value) and value > 0 else 0.60


def option_price_for_entry_target(spot: float, strike: float, sigma_ann: float) -> float:
    return bs_call(
        spot=spot,
        strike=strike,
        tau_years=TRADING_DTE_AT_ENTRY / 252,
        r=TEN_YEAR_TBILL_RATE,
        sigma=_safe_sigma(sigma_ann),
    )


def compute_target_and_stop(
    history: PreparedHistory,
    entry_date: pd.Timestamp,
    entry_spot: float,
    strike: float,
    entry_option_price: float,
    policy: ExitPolicy,
) -> tuple[float, float, float, float | None]:
    if policy.mode == "fixed":
        return (
            entry_option_price * (1.0 + policy.fixed_tp_pct),
            entry_option_price * (1.0 - policy.fixed_stop_pct),
            np.nan,
            None,
        )

    idx = history.date_to_idx[entry_date]
    row = history.df.iloc[idx]
    prev_close = float(row["Prev Close"])
    low = float(row["Low"])
    sigma_ann = _safe_sigma(float(row["Sigma Ann"]))

    if policy.target_reference == "low":
        reference_spot = low
        drop_amount = max(prev_close - low, 0.0)
    else:
        reference_spot = entry_spot
        drop_amount = max(prev_close - entry_spot, 0.0)

    target_spot = reference_spot + drop_amount * RECOVER_TARGET
    target_option_price = option_price_for_entry_target(target_spot, strike, sigma_ann)

    if policy.stop_mode == "symmetric_stock":
        stop_spot = max(reference_spot - drop_amount * RECOVER_TARGET, 0.01)
        stop_price = option_price_for_entry_target(stop_spot, strike, sigma_ann)
        stop_price = min(stop_price, entry_option_price * (1.0 - 0.02))
    else:
        stop_spot = None
        stop_price = entry_option_price * (1.0 - policy.fixed_stop_pct)

    # If the modeled recovery target is already below the limit-buy price, the
    # target is not actionable; keep a tiny minimum target to avoid instant exits.
    target_option_price = max(target_option_price, entry_option_price * 1.01)
    stop_price = max(stop_price, 0.01)
    return target_option_price, stop_price, target_spot, stop_spot


def summarize_result(label: str, equity_df: pd.DataFrame, trades_df: pd.DataFrame, candidate_df: pd.DataFrame) -> dict[str, Any]:
    final_equity = float(equity_df["equity"].iloc[-1])
    total_return_pct = (final_equity / INITIAL_CAPITAL - 1.0) * 100.0
    max_drawdown_pct = float(((equity_df["equity"] / equity_df["equity"].cummax()) - 1.0).min() * 100.0)
    win_rate_pct = float((trades_df["pnl"] > 0).mean() * 100.0) if not trades_df.empty else 0.0
    return {
        "variant": label,
        "final_equity": final_equity,
        "total_return_pct": total_return_pct,
        "max_drawdown_pct": max_drawdown_pct,
        "trade_count": int(len(trades_df)),
        "candidate_days": int(candidate_df["date"].nunique()),
        "take_rate_pct": float(trades_df["entry_date"].nunique() / candidate_df["date"].nunique() * 100.0) if not trades_df.empty else 0.0,
        "win_rate_pct": win_rate_pct,
        "avg_return_pct_per_trade": float(trades_df["return_pct"].mean()) if not trades_df.empty else 0.0,
        "median_return_pct_per_trade": float(trades_df["return_pct"].median()) if not trades_df.empty else 0.0,
        "sharpe_rf_10y_tbill": compute_annualized_sharpe(equity_df),
        "risk_free_rate_annual": TEN_YEAR_TBILL_RATE,
        "risk_free_rate_source_date": TEN_YEAR_TBILL_DATE,
    }


def build_equity_curve(
    history_map: dict[str, PreparedHistory],
    candidate_df: pd.DataFrame,
    policy: ExitPolicy,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    trade_start = pd.Timestamp(candidate_df["date"].min()).normalize()
    all_dates = sorted(
        {
            date
            for history in history_map.values()
            for date in history.df["Date"]
            if date >= trade_start
        }
    )
    score_map = score_map_for_variant(candidate_df, f"score_w{TIMING_WINDOW}")
    candidates_by_date = {
        pd.Timestamp(date).normalize(): group.sort_values(
            ["success_rate", "matched_signals", "current_drop_pct", "ticker"],
            ascending=[False, False, False, True],
        )
        for date, group in candidate_df.groupby("date")
    }

    cash = INITIAL_CAPITAL
    positions: list[Position] = []
    trades: list[dict[str, Any]] = []
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
            sigma_ann = _safe_sigma(float(row["Sigma Ann"]))
            position.day_count += 1
            option_high = mark_option_price(float(row["High"]), position.strike, position.entry_date, current_date, sigma_ann)
            option_low = mark_option_price(float(row["Low"]), position.strike, position.entry_date, current_date, sigma_ann)
            option_close = mark_option_price(float(row["Close"]), position.strike, position.entry_date, current_date, sigma_ann)

            exit_reason = None
            exit_price = None
            if option_low <= position.planned_stop:
                exit_reason = "stop"
                exit_price = position.planned_stop
            elif option_high >= position.planned_tp:
                exit_reason = "target_tp" if policy.mode == "target" else "fixed_tp"
                exit_price = position.planned_tp
            elif position.day_count >= 2:
                exit_reason = "time_exit"
                exit_price = option_close

            if exit_reason is None or exit_price is None:
                updated_positions.append(position)
                continue

            proceeds = exit_price * 100.0 * position.contracts
            cost = position.entry_option_price * 100.0 * position.contracts
            cash += proceeds
            trades.append(
                {
                    "variant": policy.label,
                    "ticker": position.ticker,
                    "entry_date": position.entry_date,
                    "exit_date": current_date,
                    "success_rate": position.success_rate,
                    "matched_signals": position.matched_signals,
                    "allocated_cash": position.allocated_cash,
                    "contracts": position.contracts,
                    "entry_option_price": position.entry_option_price,
                    "exit_option_price": exit_price,
                    "target_option_price": position.planned_tp,
                    "stop_option_price": position.planned_stop,
                    "target_spot": position.target_spot,
                    "stop_spot": position.stop_spot,
                    "pnl": proceeds - cost,
                    "return_pct": (proceeds / cost - 1.0) * 100.0,
                    "exit_reason": exit_reason,
                    "days_held": position.day_count,
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
            sigma_ann = _safe_sigma(float(row["Sigma Ann"]))
            mark = mark_option_price(float(row["Close"]), position.strike, position.entry_date, current_date, sigma_ann)
            marked_position_value += mark * 100.0 * position.contracts

        if len(positions) < MAX_OPEN_POSITIONS:
            open_tickers = {position.ticker for position in positions}
            day_candidates = candidates_by_date.get(pd.Timestamp(current_date).normalize(), pd.DataFrame())
            remaining = day_candidates[~day_candidates["ticker"].isin(open_tickers)] if not day_candidates.empty else pd.DataFrame()
            if not remaining.empty:
                candidate = remaining.iloc[0]
                score = score_map.get(event_key(candidate["date"], candidate["ticker"]), np.nan)
                if np.isfinite(score) and float(score) >= TIMING_THRESHOLD:
                    entry_cost = float(candidate["entry_option_price"]) * 100.0
                    current_equity = cash + marked_position_value
                    budget = min(cash, current_equity * TARGET_POSITION_WEIGHT)
                    contracts = int(budget // entry_cost)
                    if contracts > 0:
                        history = history_map[str(candidate["ticker"])]
                        entry_date = pd.Timestamp(candidate["date"]).normalize()
                        entry_price = float(candidate["entry_option_price"])
                        strike = float(candidate["spot_close"])
                        tp_price, stop_price, target_spot, stop_spot = compute_target_and_stop(
                            history=history,
                            entry_date=entry_date,
                            entry_spot=strike,
                            strike=strike,
                            entry_option_price=entry_price,
                            policy=policy,
                        )
                        spent = contracts * entry_cost
                        cash -= spent
                        positions.append(
                            Position(
                                ticker=str(candidate["ticker"]),
                                entry_date=entry_date,
                                strike=strike,
                                entry_option_price=entry_price,
                                contracts=contracts,
                                success_rate=float(candidate["success_rate"]),
                                matched_signals=int(candidate["matched_signals"]),
                                allocated_cash=float(spent),
                                planned_tp=float(tp_price),
                                planned_stop=float(stop_price),
                                target_spot=float(target_spot) if np.isfinite(target_spot) else np.nan,
                                stop_spot=float(stop_spot) if stop_spot is not None and np.isfinite(stop_spot) else None,
                            )
                        )
                        marked_position_value += spent

        equity_rows.append(
            {
                "variant": policy.label,
                "date": current_date,
                "cash": cash,
                "position_value": marked_position_value,
                "equity": cash + marked_position_value,
                "open_tickers": ",".join(sorted(position.ticker for position in positions)),
                "open_count": len(positions),
            }
        )

    return pd.DataFrame(equity_rows), pd.DataFrame(trades)


def plot_results(curves: dict[str, pd.DataFrame], summary_df: pd.DataFrame) -> None:
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(12, 7), facecolor=FIG_BG)
    colors = [GREEN_LINE, "#60a5fa", "#f59e0b", "#f472b6", RED_LINE]
    for idx, (label, equity_df) in enumerate(curves.items()):
        row = summary_df.loc[summary_df["variant"] == label].iloc[0]
        display_label = f"{label} ({row['total_return_pct']:+.0f}%, DD {row['max_drawdown_pct']:.0f}%)"
        ax.plot(equity_df["date"], equity_df["equity"], linewidth=2.15, color=colors[idx % len(colors)], label=display_label)

    ax.axhline(INITIAL_CAPITAL, color=BASELINE, linestyle="--", alpha=0.55, label="Initial Capital")
    style_dark_axis(ax)
    first_curve = next(iter(curves.values()))
    dates = pd.to_datetime(first_curve["date"], errors="coerce").dropna()
    date_label = f"{dates.min():%Y-%m-%d} to {dates.max():%Y-%m-%d}" if not dates.empty else "date unavailable"
    span_days = int((dates.max() - dates.min()).days) if not dates.empty else None
    style_date_axis(ax, span_days=span_days)
    ax.set_title(f"Target-Recovery Exit Experiment\nBacktest window: {date_label}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value ($)")
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
        raise RuntimeError("No candidate events were generated.")

    candidate_df[f"score_w{TIMING_WINDOW}"] = compute_walk_forward_scores(candidate_df, TIMING_WINDOW)
    candidate_trade_df = candidate_df[candidate_df["date"] >= trade_start].copy()
    if candidate_trade_df.empty:
        raise RuntimeError("No candidate events remain inside the official backtest window.")

    summaries: list[dict[str, Any]] = []
    curves: dict[str, pd.DataFrame] = {}
    all_trades: list[pd.DataFrame] = []
    all_equity: list[pd.DataFrame] = []

    for policy in POLICIES:
        equity_df, trades_df = build_equity_curve(history_map, candidate_trade_df, policy)
        summaries.append(summarize_result(policy.label, equity_df, trades_df, candidate_trade_df))
        curves[policy.label] = equity_df
        all_trades.append(trades_df)
        all_equity.append(equity_df)

    summary_df = pd.DataFrame(summaries).sort_values(
        ["sharpe_rf_10y_tbill", "max_drawdown_pct", "total_return_pct"],
        ascending=[False, False, False],
    )
    trades_out = pd.concat(all_trades, ignore_index=True) if all_trades else pd.DataFrame()
    equity_out = pd.concat(all_equity, ignore_index=True) if all_equity else pd.DataFrame()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(SUMMARY_PATH, index=False)
    trades_out.to_csv(TRADES_PATH, index=False)
    equity_out.to_csv(EQUITY_PATH, index=False)
    plot_results(curves, summary_df)

    print("Target-recovery exit experiment:")
    print(summary_df.to_string(index=False))
    print(f"Saved summary -> {SUMMARY_PATH}")
    print(f"Saved trades -> {TRADES_PATH}")
    print(f"Saved equity -> {EQUITY_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")


if __name__ == "__main__":
    main()
