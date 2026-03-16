from __future__ import annotations

import itertools
import math
import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm


INITIAL_CAPITAL = 10_000.0
FORWARD_DAYS = 5
RECOVER_TARGET = 0.70
ROLLING_SIGMA_WINDOW = 20
TRADING_DTE_AT_ENTRY = 30
RISK_FREE = 0.04
LIMIT_BUY_DISCOUNT_PCT = 0.10
DAY1_TAKE_PROFIT_PCT = 0.10
DAY2_TAKE_PROFIT_PCT = 0.15
STOP_LOSS_PCT = 0.10
MAX_OPEN_POSITIONS = 2
TARGET_POSITION_WEIGHT = 0.50
DOWNLOAD_BATCH_SIZE = 50

DATA_START = "2020-01-01"
TRADE_START = "2021-01-01"

LOOKBACK_SWEEP = [20, 40, 60, 80, 100, 126, 160, 252]
SUCCESS_GATE_SWEEP = [70.0, 75.0, 78.0, 80.0, 82.0, 85.0]
MIN_MATCHED_SWEEP = [6, 8, 10, 12, 15]
LOCAL_GRID_LOOKBACKS = [40, 60, 80, 126, 252]
LOCAL_GRID_GATES = [75.0, 80.0, 85.0]
LOCAL_GRID_MATCHED = [8, 10, 12]
WALK_FORWARD_LOOKBACKS = [40, 60, 80, 126, 252]
PLACEBO_RUNS = 30
TRAIN_WINDOW_DAYS = 252
TEST_WINDOW_DAYS = 126

OUTPUT_DIR = Path.cwd() / "results" / "reversal_2_4_overfit"
ASSET_DIR = Path.cwd() / "assets"
PREPARED_CACHE_PATH = OUTPUT_DIR / "prepared_histories.pkl"
SUMMARY_PATH = OUTPUT_DIR / "reversal_2_4_overfit_summary.csv"
LOOKBACK_PATH = OUTPUT_DIR / "lookback_sensitivity.csv"
SUCCESS_GATE_PATH = OUTPUT_DIR / "success_gate_sensitivity.csv"
MIN_MATCHED_PATH = OUTPUT_DIR / "min_matched_sensitivity.csv"
LOCAL_GRID_PATH = OUTPUT_DIR / "local_parameter_grid.csv"
SEGMENT_PATH = OUTPUT_DIR / "segment_stability.csv"
TICKER_PNL_PATH = OUTPUT_DIR / "ticker_pnl_concentration.csv"
WALK_FORWARD_PATH = OUTPUT_DIR / "walk_forward_lookback_selection.csv"
PLACEBO_PATH = OUTPUT_DIR / "placebo_random_selection.csv"
PARAMETER_PLOT_PATH = ASSET_DIR / "reversal_2_4_overfit_parameters.png"
ROBUSTNESS_PLOT_PATH = ASSET_DIR / "reversal_2_4_overfit_robustness.png"


@dataclass(frozen=True)
class StrategyConfig:
    label: str
    lookback_days: int = 60
    success_rate_gate: float = 80.0
    min_matched_signals: int = 10


@dataclass
class PreparedHistory:
    ticker: str
    df: pd.DataFrame
    date_to_idx: dict[pd.Timestamp, int]
    max_drop: np.ndarray
    signal_success: np.ndarray
    valid_signal: np.ndarray


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


def load_tickers() -> list[str]:
    path = Path.cwd() / "qqq_only_filtered_tickers.csv"
    df = pd.read_csv(path)
    return (
        df["ticker"]
        .dropna()
        .astype(str)
        .str.strip()
        .str.upper()
        .loc[lambda s: s != ""]
        .drop_duplicates()
        .tolist()
    )


def _extract_single_ticker_frame(downloaded: pd.DataFrame, ticker: str) -> pd.DataFrame:
    if downloaded.empty:
        return pd.DataFrame()
    if isinstance(downloaded.columns, pd.MultiIndex):
        if ticker not in downloaded.columns.get_level_values(0):
            return pd.DataFrame()
        frame = downloaded.xs(ticker, axis=1, level=0, drop_level=True).copy()
    else:
        frame = downloaded.copy()
    return frame.dropna(how="all")


def bs_call(spot: float, strike: float, tau_years: float, r: float, sigma: float) -> float:
    if spot <= 0 or strike <= 0:
        return 0.0
    if tau_years <= 0:
        return max(spot - strike, 0.0)
    if sigma <= 0 or np.isnan(sigma):
        return max(spot - strike * np.exp(-r * tau_years), 0.0)

    d1 = (np.log(spot / strike) + (r + 0.5 * sigma**2) * tau_years) / (sigma * np.sqrt(tau_years))
    d2 = d1 - sigma * np.sqrt(tau_years)
    return float(spot * norm.cdf(d1) - strike * np.exp(-r * tau_years) * norm.cdf(d2))


def prepare_history_frame(raw_df: pd.DataFrame) -> pd.DataFrame:
    close_source = "Close" if "Close" in raw_df.columns else "Adj Close"
    required_cols = ["Open", "High", "Low", close_source, "Adj Close"]
    missing = [col for col in required_cols if col not in raw_df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = raw_df[required_cols].copy().reset_index()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.normalize()
    rename_map = {close_source: "Close"}
    df = df.rename(columns=rename_map)
    for col in ["Open", "High", "Low", "Close", "Adj Close"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.sort_values("Date").reset_index(drop=True)
    df["Prev Close"] = df["Adj Close"].shift(1)
    df["Max Drop"] = (df["Prev Close"] - df["Low"]) / df["Prev Close"]
    df["Log Return"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
    df["Sigma Ann"] = df["Log Return"].rolling(ROLLING_SIGMA_WINDOW).std() * np.sqrt(252)

    future_high = pd.concat(
        [df["High"].shift(-i) for i in range(1, FORWARD_DAYS + 1)],
        axis=1,
    ).max(axis=1)
    df["Future High"] = future_high
    df["Signal Drop Amount"] = df["Max Drop"] * df["Prev Close"]
    df["Recover Ratio"] = (df["Future High"] - df["Low"]) / df["Signal Drop Amount"]
    df["Signal Success"] = df["Recover Ratio"] >= RECOVER_TARGET
    df["Valid Signal"] = (
        df["Signal Drop Amount"].replace([np.inf, -np.inf], np.nan).gt(0)
        & df["Future High"].notna()
    )

    return df.dropna(
        subset=["Date", "Open", "High", "Low", "Close", "Adj Close", "Prev Close", "Max Drop"]
    ).reset_index(drop=True)


def load_or_download_histories(tickers: list[str], end_date: pd.Timestamp) -> dict[str, PreparedHistory]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if PREPARED_CACHE_PATH.exists():
        with PREPARED_CACHE_PATH.open("rb") as fh:
            payload = pickle.load(fh)
        if payload.get("tickers") == sorted(tickers) and payload.get("data_start") == DATA_START and payload.get("data_end") == end_date.strftime("%Y-%m-%d"):
            cached_histories: dict[str, pd.DataFrame] = payload["frames"]
            return {
                ticker: PreparedHistory(
                    ticker=ticker,
                    df=df,
                    date_to_idx={date: idx for idx, date in enumerate(df["Date"])},
                    max_drop=df["Max Drop"].to_numpy(dtype=float),
                    signal_success=df["Signal Success"].fillna(False).to_numpy(dtype=bool),
                    valid_signal=df["Valid Signal"].fillna(False).to_numpy(dtype=bool),
                )
                for ticker, df in cached_histories.items()
            }

    frames: dict[str, pd.DataFrame] = {}
    for batch_start in range(0, len(tickers), DOWNLOAD_BATCH_SIZE):
        batch = tickers[batch_start: batch_start + DOWNLOAD_BATCH_SIZE]
        print(f"Downloading batch {batch_start // DOWNLOAD_BATCH_SIZE + 1}: {len(batch)} tickers")
        downloaded = yf.download(
            tickers=batch,
            start=DATA_START,
            end=(end_date + pd.Timedelta(days=1)).strftime("%Y-%m-%d"),
            auto_adjust=False,
            progress=False,
            threads=True,
            group_by="ticker",
        )
        for ticker in batch:
            frame = _extract_single_ticker_frame(downloaded, ticker)
            if frame.empty:
                continue
            try:
                prepared = prepare_history_frame(frame)
            except ValueError:
                continue
            if len(prepared) <= max(LOOKBACK_SWEEP) + FORWARD_DAYS:
                continue
            frames[ticker] = prepared

    payload = {
        "tickers": sorted(tickers),
        "data_start": DATA_START,
        "data_end": end_date.strftime("%Y-%m-%d"),
        "frames": frames,
    }
    with PREPARED_CACHE_PATH.open("wb") as fh:
        pickle.dump(payload, fh)

    return {
        ticker: PreparedHistory(
            ticker=ticker,
            df=df,
            date_to_idx={date: idx for idx, date in enumerate(df["Date"])},
            max_drop=df["Max Drop"].to_numpy(dtype=float),
            signal_success=df["Signal Success"].fillna(False).to_numpy(dtype=bool),
            valid_signal=df["Valid Signal"].fillna(False).to_numpy(dtype=bool),
        )
        for ticker, df in frames.items()
    }


def compute_signal_success_rate(config: StrategyConfig, history: PreparedHistory, idx: int) -> tuple[float, int]:
    current_drop_pct = history.max_drop[idx]
    if np.isnan(current_drop_pct) or current_drop_pct <= 0:
        return np.nan, 0

    start_idx = max(1, idx - config.lookback_days)
    end_idx = idx - FORWARD_DAYS
    if end_idx <= start_idx:
        return np.nan, 0

    hist_drop = history.max_drop[start_idx:end_idx]
    hist_valid = history.valid_signal[start_idx:end_idx]
    hist_success = history.signal_success[start_idx:end_idx]

    mask = hist_valid & np.isfinite(hist_drop) & (hist_drop >= current_drop_pct)
    matched_signals = int(mask.sum())
    if matched_signals == 0:
        return np.nan, 0
    return float(hist_success[mask].mean() * 100), matched_signals


def next_business_day(date: pd.Timestamp, days: int) -> pd.Timestamp:
    return pd.bdate_range(date + pd.Timedelta(days=1), periods=days)[-1]


def remaining_tau(entry_date: pd.Timestamp, current_date: pd.Timestamp, trading_dte: int) -> float:
    elapsed = len(pd.bdate_range(entry_date + pd.Timedelta(days=1), current_date))
    return max((trading_dte - elapsed) / 252, 0.0)


def mark_option_price(
    spot: float,
    strike: float,
    entry_date: pd.Timestamp,
    current_date: pd.Timestamp,
    sigma_ann: float,
) -> float:
    tau = remaining_tau(entry_date, current_date, TRADING_DTE_AT_ENTRY)
    return bs_call(spot=spot, strike=strike, tau_years=tau, r=RISK_FREE, sigma=sigma_ann)


def evaluate_candidate(config: StrategyConfig, history: PreparedHistory, idx: int) -> dict[str, Any] | None:
    success_rate, matched_signals = compute_signal_success_rate(config=config, history=history, idx=idx)
    if np.isnan(success_rate) or success_rate < config.success_rate_gate or matched_signals < config.min_matched_signals:
        return None

    row = history.df.iloc[idx]
    sigma_ann = float(row["Sigma Ann"])
    spot_close = float(row["Close"])
    if np.isnan(sigma_ann) or sigma_ann <= 0 or spot_close <= 0:
        return None

    option_mid = bs_call(
        spot=spot_close,
        strike=spot_close,
        tau_years=TRADING_DTE_AT_ENTRY / 252,
        r=RISK_FREE,
        sigma=sigma_ann,
    )
    if option_mid <= 0:
        return None

    option_low_today = bs_call(
        spot=float(row["Low"]),
        strike=spot_close,
        tau_years=TRADING_DTE_AT_ENTRY / 252,
        r=RISK_FREE,
        sigma=sigma_ann,
    )
    limit_buy = option_mid * (1 - LIMIT_BUY_DISCOUNT_PCT)
    if option_low_today > limit_buy:
        return None

    return {
        "ticker": history.ticker,
        "success_rate": success_rate,
        "matched_signals": matched_signals,
        "spot_close": spot_close,
        "entry_option_price": limit_buy,
    }


def collect_all_dates(history_map: dict[str, PreparedHistory], trade_start: pd.Timestamp, trade_end: pd.Timestamp) -> list[pd.Timestamp]:
    return sorted(
        {
            date
            for history in history_map.values()
            for date in history.df["Date"]
            if trade_start <= date <= trade_end
        }
    )


def backtest_period(
    config: StrategyConfig,
    history_map: dict[str, PreparedHistory],
    trade_start: pd.Timestamp,
    trade_end: pd.Timestamp,
    candidate_mode: str = "ranked",
    rng: np.random.Generator | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    all_dates = collect_all_dates(history_map, trade_start=trade_start, trade_end=trade_end)
    if not all_dates:
        return pd.DataFrame(), pd.DataFrame(), {
            "label": config.label,
            "trade_start": trade_start,
            "trade_end": trade_end,
            "final_equity": INITIAL_CAPITAL,
            "total_return_pct": 0.0,
            "max_drawdown_pct": 0.0,
            "trade_count": 0,
            "win_rate_pct": 0.0,
            "avg_trade_return_pct": 0.0,
        }

    cash = INITIAL_CAPITAL
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
            option_high = mark_option_price(float(row["High"]), position.strike, position.entry_date, current_date, sigma_ann)
            option_low = mark_option_price(float(row["Low"]), position.strike, position.entry_date, current_date, sigma_ann)
            option_close = mark_option_price(float(row["Close"]), position.strike, position.entry_date, current_date, sigma_ann)

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
                    "config": config.label,
                    "ticker": position.ticker,
                    "entry_date": position.entry_date,
                    "exit_date": current_date,
                    "success_rate": position.success_rate,
                    "matched_signals": position.matched_signals,
                    "allocated_cash": position.allocated_cash,
                    "contracts": position.contracts,
                    "entry_option_price": position.entry_option_price,
                    "exit_option_price": exit_price,
                    "entry_spot": position.entry_spot,
                    "exit_spot_close": float(row["Close"]),
                    "pnl": pnl,
                    "return_pct": pnl / (position.entry_option_price * 100 * position.contracts) * 100,
                    "exit_reason": exit_reason,
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
            mark = mark_option_price(float(row["Close"]), position.strike, position.entry_date, current_date, sigma_ann)
            marked_position_value += mark * 100 * position.contracts

        if len(positions) < MAX_OPEN_POSITIONS:
            open_tickers = {position.ticker for position in positions}
            candidates: list[dict[str, Any]] = []
            for ticker, history in history_map.items():
                if ticker in open_tickers:
                    continue
                idx = history.date_to_idx.get(current_date)
                if idx is None or idx <= config.lookback_days or idx + FORWARD_DAYS >= len(history.df):
                    continue
                candidate = evaluate_candidate(config=config, history=history, idx=idx)
                if candidate is not None:
                    candidates.append(candidate)

            if candidates:
                if candidate_mode == "random":
                    if rng is None:
                        raise ValueError("rng is required for random candidate selection")
                    picked = candidates[int(rng.integers(0, len(candidates)))]
                else:
                    picked = max(candidates, key=lambda item: (item["success_rate"], item["matched_signals"]))
                entry_cost = picked["entry_option_price"] * 100
                current_equity = cash + marked_position_value
                budget = min(cash, current_equity * TARGET_POSITION_WEIGHT)
                contracts = int(budget // entry_cost)
                if contracts > 0:
                    spent = contracts * entry_cost
                    cash -= spent
                    positions.append(
                        Position(
                            ticker=str(picked["ticker"]),
                            entry_date=current_date,
                            expiry_date=next_business_day(current_date, TRADING_DTE_AT_ENTRY),
                            entry_spot=float(picked["spot_close"]),
                            strike=float(picked["spot_close"]),
                            entry_option_price=float(picked["entry_option_price"]),
                            contracts=contracts,
                            success_rate=float(picked["success_rate"]),
                            matched_signals=int(picked["matched_signals"]),
                            allocated_cash=float(spent),
                            planned_tp_day1=float(picked["entry_option_price"]) * (1 + DAY1_TAKE_PROFIT_PCT),
                            planned_tp_day2=float(picked["entry_option_price"]) * (1 + DAY2_TAKE_PROFIT_PCT),
                            planned_stop=float(picked["entry_option_price"]) * (1 - STOP_LOSS_PCT),
                        )
                    )
                    marked_position_value += spent

        equity_rows.append(
            {
                "date": current_date,
                "equity": cash + marked_position_value,
                "cash": cash,
                "position_value": marked_position_value,
                "open_count": len(positions),
            }
        )

    equity_df = pd.DataFrame(equity_rows)
    trades_df = pd.DataFrame(trade_rows)
    final_equity = float(equity_df["equity"].iloc[-1]) if not equity_df.empty else INITIAL_CAPITAL
    total_return = (final_equity / INITIAL_CAPITAL - 1) * 100
    max_drawdown = ((equity_df["equity"] / equity_df["equity"].cummax()) - 1).min() * 100 if not equity_df.empty else 0.0
    win_rate = float((trades_df["pnl"] > 0).mean() * 100) if not trades_df.empty else 0.0
    avg_trade_return = float(trades_df["return_pct"].mean()) if not trades_df.empty else 0.0
    summary = {
        "label": config.label,
        "lookback_days": config.lookback_days,
        "success_rate_gate": config.success_rate_gate,
        "min_matched_signals": config.min_matched_signals,
        "trade_start": trade_start,
        "trade_end": trade_end,
        "final_equity": final_equity,
        "total_return_pct": total_return,
        "max_drawdown_pct": max_drawdown,
        "trade_count": len(trades_df),
        "win_rate_pct": win_rate,
        "avg_trade_return_pct": avg_trade_return,
    }
    return equity_df, trades_df, summary


def run_parameter_sweeps(history_map: dict[str, PreparedHistory], trade_start: pd.Timestamp, trade_end: pd.Timestamp) -> dict[str, pd.DataFrame]:
    lookback_rows = []
    for lookback in LOOKBACK_SWEEP:
        _, _, summary = backtest_period(
            StrategyConfig(label=f"lookback_{lookback}", lookback_days=lookback),
            history_map,
            trade_start,
            trade_end,
        )
        lookback_rows.append(summary)

    gate_rows = []
    for gate in SUCCESS_GATE_SWEEP:
        _, _, summary = backtest_period(
            StrategyConfig(label=f"gate_{gate:g}", lookback_days=60, success_rate_gate=gate),
            history_map,
            trade_start,
            trade_end,
        )
        gate_rows.append(summary)

    matched_rows = []
    for min_matched in MIN_MATCHED_SWEEP:
        _, _, summary = backtest_period(
            StrategyConfig(label=f"matched_{min_matched}", lookback_days=60, min_matched_signals=min_matched),
            history_map,
            trade_start,
            trade_end,
        )
        matched_rows.append(summary)

    grid_rows = []
    for lookback, gate, min_matched in itertools.product(LOCAL_GRID_LOOKBACKS, LOCAL_GRID_GATES, LOCAL_GRID_MATCHED):
        _, _, summary = backtest_period(
            StrategyConfig(
                label=f"lb{lookback}_gate{gate:g}_m{min_matched}",
                lookback_days=lookback,
                success_rate_gate=gate,
                min_matched_signals=min_matched,
            ),
            history_map,
            trade_start,
            trade_end,
        )
        grid_rows.append(summary)

    return {
        "lookback": pd.DataFrame(lookback_rows),
        "success_gate": pd.DataFrame(gate_rows),
        "min_matched": pd.DataFrame(matched_rows),
        "local_grid": pd.DataFrame(grid_rows),
    }


def build_segment_periods(trade_start: pd.Timestamp, trade_end: pd.Timestamp) -> list[tuple[str, pd.Timestamp, pd.Timestamp]]:
    periods: list[tuple[str, pd.Timestamp, pd.Timestamp]] = []
    current = pd.Timestamp(year=trade_start.year, month=1 if trade_start.month <= 6 else 7, day=1)
    while current <= trade_end:
        if current.month == 1:
            period_end = pd.Timestamp(year=current.year, month=6, day=30)
            label = f"{current.year}-H1"
        else:
            period_end = pd.Timestamp(year=current.year, month=12, day=31)
            label = f"{current.year}-H2"
        start = max(current, trade_start)
        end = min(period_end, trade_end)
        if start <= end:
            periods.append((label, start, end))
        current = period_end + pd.Timedelta(days=1)
    return periods


def run_segment_stability(
    config: StrategyConfig,
    history_map: dict[str, PreparedHistory],
    trade_start: pd.Timestamp,
    trade_end: pd.Timestamp,
) -> pd.DataFrame:
    rows = []
    for label, start, end in build_segment_periods(trade_start, trade_end):
        _, _, summary = backtest_period(config, history_map, start, end)
        summary["segment"] = label
        rows.append(summary)
    return pd.DataFrame(rows)


def run_walk_forward_lookback_selection(
    history_map: dict[str, PreparedHistory],
    trade_start: pd.Timestamp,
    trade_end: pd.Timestamp,
) -> pd.DataFrame:
    all_dates = collect_all_dates(history_map, trade_start=trade_start, trade_end=trade_end)
    rows = []
    window_start_idx = TRAIN_WINDOW_DAYS
    while window_start_idx + TEST_WINDOW_DAYS <= len(all_dates):
        train_start = all_dates[window_start_idx - TRAIN_WINDOW_DAYS]
        train_end = all_dates[window_start_idx - 1]
        test_start = all_dates[window_start_idx]
        test_end = all_dates[window_start_idx + TEST_WINDOW_DAYS - 1]

        train_summaries = []
        for lookback in WALK_FORWARD_LOOKBACKS:
            _, _, train_summary = backtest_period(
                StrategyConfig(label=f"wf_train_{lookback}", lookback_days=lookback),
                history_map,
                train_start,
                train_end,
            )
            train_summaries.append(train_summary)
        train_df = pd.DataFrame(train_summaries)
        picked_row = train_df.sort_values(
            ["total_return_pct", "max_drawdown_pct", "trade_count"],
            ascending=[False, False, False],
        ).iloc[0]
        selected_lookback = int(picked_row["lookback_days"])

        _, _, selected_test = backtest_period(
            StrategyConfig(label=f"wf_selected_{selected_lookback}", lookback_days=selected_lookback),
            history_map,
            test_start,
            test_end,
        )
        _, _, fixed_60_test = backtest_period(
            StrategyConfig(label="wf_fixed_60", lookback_days=60),
            history_map,
            test_start,
            test_end,
        )
        _, _, fixed_252_test = backtest_period(
            StrategyConfig(label="wf_fixed_252", lookback_days=252),
            history_map,
            test_start,
            test_end,
        )

        rows.append(
            {
                "train_start": train_start,
                "train_end": train_end,
                "test_start": test_start,
                "test_end": test_end,
                "selected_lookback": selected_lookback,
                "selected_train_return_pct": picked_row["total_return_pct"],
                "selected_train_max_drawdown_pct": picked_row["max_drawdown_pct"],
                "selected_oos_return_pct": selected_test["total_return_pct"],
                "selected_oos_max_drawdown_pct": selected_test["max_drawdown_pct"],
                "fixed_60_oos_return_pct": fixed_60_test["total_return_pct"],
                "fixed_60_oos_max_drawdown_pct": fixed_60_test["max_drawdown_pct"],
                "fixed_252_oos_return_pct": fixed_252_test["total_return_pct"],
                "fixed_252_oos_max_drawdown_pct": fixed_252_test["max_drawdown_pct"],
            }
        )
        window_start_idx += TEST_WINDOW_DAYS
    return pd.DataFrame(rows)


def run_placebo_random_selection(
    history_map: dict[str, PreparedHistory],
    trade_start: pd.Timestamp,
    trade_end: pd.Timestamp,
) -> pd.DataFrame:
    rows = []
    for seed in range(PLACEBO_RUNS):
        _, _, summary = backtest_period(
            StrategyConfig(label=f"placebo_{seed}", lookback_days=60),
            history_map,
            trade_start,
            trade_end,
            candidate_mode="random",
            rng=np.random.default_rng(seed),
        )
        summary["seed"] = seed
        rows.append(summary)
    return pd.DataFrame(rows)


def summarize_official_vs_252(
    history_map: dict[str, PreparedHistory],
    trade_start: pd.Timestamp,
    trade_end: pd.Timestamp,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    _, official_trades, official_summary = backtest_period(
        StrategyConfig(label="official_60d", lookback_days=60),
        history_map,
        trade_start,
        trade_end,
    )
    _, baseline_252_trades, baseline_252_summary = backtest_period(
        StrategyConfig(label="legacy_252d", lookback_days=252),
        history_map,
        trade_start,
        trade_end,
    )
    summary_df = pd.DataFrame([official_summary, baseline_252_summary])

    ticker_rows = []
    if not official_trades.empty:
        ticker_pnl = official_trades.groupby("ticker", as_index=False)["pnl"].sum().sort_values("pnl", ascending=False)
        total_pnl = ticker_pnl["pnl"].sum()
        ticker_pnl["share_of_total_pnl_pct"] = np.where(total_pnl == 0, np.nan, ticker_pnl["pnl"] / total_pnl * 100)
        ticker_rows = ticker_pnl.to_dict("records")
    ticker_df = pd.DataFrame(ticker_rows)
    return summary_df, official_trades, ticker_df


def plot_parameter_sensitivity(
    official_summary: pd.Series,
    lookback_df: pd.DataFrame,
    gate_df: pd.DataFrame,
    matched_df: pd.DataFrame,
) -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    axes[0].plot(lookback_df["lookback_days"], lookback_df["total_return_pct"], marker="o", linewidth=2)
    axes[0].axvline(60, color="tab:red", linestyle="--", alpha=0.7)
    axes[0].set_title("Lookback Sensitivity")
    axes[0].set_xlabel("Lookback Days")
    axes[0].set_ylabel("Total Return (%)")
    axes[0].grid(alpha=0.25)

    axes[1].plot(gate_df["success_rate_gate"], gate_df["total_return_pct"], marker="o", linewidth=2, color="tab:green")
    axes[1].axvline(80.0, color="tab:red", linestyle="--", alpha=0.7)
    axes[1].set_title("Success Gate Sensitivity")
    axes[1].set_xlabel("Success Rate Gate (%)")
    axes[1].set_ylabel("Total Return (%)")
    axes[1].grid(alpha=0.25)

    axes[2].plot(matched_df["min_matched_signals"], matched_df["total_return_pct"], marker="o", linewidth=2, color="tab:purple")
    axes[2].axvline(10, color="tab:red", linestyle="--", alpha=0.7)
    axes[2].set_title("Matched Signal Sensitivity")
    axes[2].set_xlabel("Min Matched Signals")
    axes[2].set_ylabel("Total Return (%)")
    axes[2].grid(alpha=0.25)

    fig.suptitle(
        f"Reversal 2.4 Parameter Sensitivity | Official 60d return {official_summary['total_return_pct']:.1f}% | Max DD {official_summary['max_drawdown_pct']:.1f}%",
        fontsize=13,
    )
    fig.tight_layout()
    fig.savefig(PARAMETER_PLOT_PATH, dpi=160, bbox_inches="tight")
    plt.close(fig)


def plot_robustness(
    segment_df: pd.DataFrame,
    walk_forward_df: pd.DataFrame,
    placebo_df: pd.DataFrame,
    ticker_df: pd.DataFrame,
    official_summary: pd.Series,
) -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))

    axes[0, 0].bar(segment_df["segment"], segment_df["total_return_pct"], color=np.where(segment_df["total_return_pct"] >= 0, "tab:blue", "tab:orange"))
    axes[0, 0].axhline(0, color="black", linewidth=1)
    axes[0, 0].set_title("Half-Year Segment Returns")
    axes[0, 0].set_ylabel("Return (%)")
    axes[0, 0].tick_params(axis="x", rotation=45)
    axes[0, 0].grid(alpha=0.2, axis="y")

    if not walk_forward_df.empty:
        x = np.arange(len(walk_forward_df))
        cum_selected = (1 + walk_forward_df["selected_oos_return_pct"] / 100).cumprod()
        cum_60 = (1 + walk_forward_df["fixed_60_oos_return_pct"] / 100).cumprod()
        cum_252 = (1 + walk_forward_df["fixed_252_oos_return_pct"] / 100).cumprod()
        axes[0, 1].plot(x, cum_selected, marker="o", label="Walk-forward selected lookback")
        axes[0, 1].plot(x, cum_60, marker="o", label="Fixed 60d")
        axes[0, 1].plot(x, cum_252, marker="o", label="Fixed 252d")
        axes[0, 1].set_title("Walk-Forward OOS Growth")
        axes[0, 1].set_xlabel("OOS Window")
        axes[0, 1].set_ylabel("Growth of $1")
        axes[0, 1].grid(alpha=0.25)
        axes[0, 1].legend()

    axes[1, 0].hist(placebo_df["total_return_pct"], bins=12, color="lightgray", edgecolor="black")
    axes[1, 0].axvline(float(official_summary["total_return_pct"]), color="tab:red", linestyle="--", linewidth=2)
    axes[1, 0].set_title("Random Candidate Placebo")
    axes[1, 0].set_xlabel("Total Return (%)")
    axes[1, 0].set_ylabel("Simulation Count")
    axes[1, 0].grid(alpha=0.2, axis="y")

    top_tickers = ticker_df.head(10)
    axes[1, 1].bar(top_tickers["ticker"], top_tickers["share_of_total_pnl_pct"], color="tab:cyan")
    axes[1, 1].set_title("Top-10 Ticker PnL Contribution")
    axes[1, 1].set_ylabel("Share of Total PnL (%)")
    axes[1, 1].tick_params(axis="x", rotation=45)
    axes[1, 1].grid(alpha=0.2, axis="y")

    fig.suptitle("Reversal 2.4 Robustness Audit", fontsize=14)
    fig.tight_layout()
    fig.savefig(ROBUSTNESS_PLOT_PATH, dpi=160, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    end_date = (pd.Timestamp.today().normalize() - pd.Timedelta(days=1)).normalize()
    trade_start = pd.Timestamp(TRADE_START)
    tickers = load_tickers()
    history_map = load_or_download_histories(tickers, end_date=end_date)
    usable_tickers = len(history_map)
    trade_end = min(
        end_date,
        max(history.df["Date"].max() for history in history_map.values()),
    )
    print(f"Usable tickers: {usable_tickers}")
    print(f"Trade window: {trade_start.date()} -> {trade_end.date()}")

    official_config = StrategyConfig(label="official_60d", lookback_days=60)
    summary_df, official_trades, ticker_df = summarize_official_vs_252(history_map, trade_start, trade_end)
    official_summary = summary_df.loc[summary_df["label"].eq("official_60d")].iloc[0]

    sweep_results = run_parameter_sweeps(history_map, trade_start, trade_end)
    segment_df = run_segment_stability(official_config, history_map, trade_start, trade_end)
    walk_forward_df = run_walk_forward_lookback_selection(history_map, trade_start, trade_end)
    placebo_df = run_placebo_random_selection(history_map, trade_start, trade_end)

    local_grid_df = sweep_results["local_grid"].sort_values("total_return_pct", ascending=False).reset_index(drop=True)
    official_grid_row = local_grid_df[
        (local_grid_df["lookback_days"] == 60)
        & (local_grid_df["success_rate_gate"] == 80.0)
        & (local_grid_df["min_matched_signals"] == 10)
    ].copy()
    if not official_grid_row.empty:
        official_rank = int(official_grid_row.index[0] + 1)
        summary_df = pd.concat(
            [
                summary_df,
                pd.DataFrame(
                    [
                        {
                            "label": "official_local_grid_rank",
                            "lookback_days": 60,
                            "success_rate_gate": 80.0,
                            "min_matched_signals": 10,
                            "trade_start": trade_start,
                            "trade_end": trade_end,
                            "final_equity": np.nan,
                            "total_return_pct": official_rank,
                            "max_drawdown_pct": np.nan,
                            "trade_count": len(local_grid_df),
                            "win_rate_pct": np.nan,
                            "avg_trade_return_pct": np.nan,
                        }
                    ]
                ),
            ],
            ignore_index=True,
        )

    placebo_percentile = float((placebo_df["total_return_pct"] < official_summary["total_return_pct"]).mean() * 100) if not placebo_df.empty else np.nan
    summary_df = pd.concat(
        [
            summary_df,
            pd.DataFrame(
                [
                    {
                        "label": "placebo_percentile",
                        "lookback_days": 60,
                        "success_rate_gate": 80.0,
                        "min_matched_signals": 10,
                        "trade_start": trade_start,
                        "trade_end": trade_end,
                        "final_equity": np.nan,
                        "total_return_pct": placebo_percentile,
                        "max_drawdown_pct": np.nan,
                        "trade_count": PLACEBO_RUNS,
                        "win_rate_pct": np.nan,
                        "avg_trade_return_pct": np.nan,
                    }
                ]
            ),
        ],
        ignore_index=True,
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(SUMMARY_PATH, index=False)
    sweep_results["lookback"].to_csv(LOOKBACK_PATH, index=False)
    sweep_results["success_gate"].to_csv(SUCCESS_GATE_PATH, index=False)
    sweep_results["min_matched"].to_csv(MIN_MATCHED_PATH, index=False)
    local_grid_df.to_csv(LOCAL_GRID_PATH, index=False)
    segment_df.to_csv(SEGMENT_PATH, index=False)
    ticker_df.to_csv(TICKER_PNL_PATH, index=False)
    walk_forward_df.to_csv(WALK_FORWARD_PATH, index=False)
    placebo_df.to_csv(PLACEBO_PATH, index=False)

    plot_parameter_sensitivity(
        official_summary=official_summary,
        lookback_df=sweep_results["lookback"],
        gate_df=sweep_results["success_gate"],
        matched_df=sweep_results["min_matched"],
    )
    plot_robustness(
        segment_df=segment_df,
        walk_forward_df=walk_forward_df,
        placebo_df=placebo_df,
        ticker_df=ticker_df,
        official_summary=official_summary,
    )

    print(summary_df.to_string(index=False))
    print(f"Saved summary -> {SUMMARY_PATH}")
    print(f"Saved parameter sweep -> {LOOKBACK_PATH}")
    print(f"Saved segment stability -> {SEGMENT_PATH}")
    print(f"Saved walk-forward -> {WALK_FORWARD_PATH}")
    print(f"Saved placebo -> {PLACEBO_PATH}")
    print(f"Saved parameter plot -> {PARAMETER_PLOT_PATH}")
    print(f"Saved robustness plot -> {ROBUSTNESS_PLOT_PATH}")


if __name__ == "__main__":
    main()
