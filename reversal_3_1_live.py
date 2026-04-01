from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
import yfinance as yf

from reversal_universe import build_named_universe_map
from update_reversal_data import refresh_reversal_data


VERSION = "3.1"
UNIVERSE_NAME = "qqq_plus_leverage_etfs"
INITIAL_CAPITAL = 10_000.0
LOOKBACK_DAYS = 60
FORWARD_DAYS = 5
RECOVER_TARGET = 0.70
SUCCESS_RATE_GATE = 80.0
MIN_MATCHED_SIGNALS = 10
MINIMUM_CURRENT_DROP_PCT = 0.005
ROLLING_SIGMA_WINDOW = 20
MIN_TRADING_DTE = 21
MAX_TRADING_DTE = 40
MAX_ABS_MONEYNESS_PCT = 0.08
MAX_OTM_PCT = 0.05
MAX_SPREAD_PCT = 0.25
MIN_OPEN_INTEREST = 10
MAX_OPEN_POSITIONS = 2
TARGET_POSITION_WEIGHT = 0.50
DAY1_TAKE_PROFIT_PCT = 0.10
DAY2_TAKE_PROFIT_PCT = 0.15
STOP_LOSS_PCT = 0.10
REFRESH_DATA_IF_STALE = True
LIVE_START_DATE = "2026-03-24"

ET = ZoneInfo("America/New_York")
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "reversal_data"
ASSETS_DIR = BASE_DIR / "assets"
LIVE_DIR = BASE_DIR / "results" / "reversal_3_1_live"
ROOT_README_PATH = BASE_DIR / "README.md"
ROOT_SECTION_START = "<!-- reversal-3.1-live:start -->"
ROOT_SECTION_END = "<!-- reversal-3.1-live:end -->"

STATE_PATH = LIVE_DIR / "state.json"
TRADES_PATH = LIVE_DIR / "live_trades.csv"
EVENTS_PATH = LIVE_DIR / "live_events.csv"
POSITIONS_PATH = LIVE_DIR / "live_positions.csv"
EQUITY_PATH = LIVE_DIR / "live_equity.csv"
DASHBOARD_PATH = LIVE_DIR / "README.md"
PLOT_PATH = ASSETS_DIR / "reversal_3_1_live_equity.png"
PLOT_WINDOW_DAYS = 7

SLOT_TO_ET = {
    "manage_0930": (9, 30),
    "manage_1000": (10, 0),
    "manage_1030": (10, 30),
    "manage_1100": (11, 0),
    "manage_1130": (11, 30),
    "manage_1200": (12, 0),
    "manage_1230": (12, 30),
    "manage_1300": (13, 0),
    "manage_1330": (13, 30),
    "manage_1400": (14, 0),
    "manage_1430": (14, 30),
    "entry_1500": (15, 0),
    "manage_1530": (15, 30),
    "manage_1600": (16, 0),
}


@dataclass
class Position:
    position_id: str
    ticker: str
    contract_symbol: str
    expiry: str
    strike: float
    entry_timestamp: str
    entry_trade_date: str
    entry_slot: str
    entry_spot: float
    entry_option_price: float
    entry_bid: float | None
    entry_ask: float | None
    entry_iv_pct: float | None
    contracts: int
    allocated_cash: float
    success_rate: float
    matched_signals: int
    current_drop_pct: float
    rolling_sigma_20d_pct: float | None
    planned_tp_day1: float
    planned_tp_day2: float
    planned_stop: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the Reversal 3.1 live paper-trading cycle.")
    parser.add_argument("--force-slot", choices=sorted(SLOT_TO_ET), default=None)
    parser.add_argument("--now", default=None, help="Optional override timestamp, e.g. 2026-03-24T15:00:00-04:00")
    parser.add_argument("--start-date", default=LIVE_START_DATE, help="Do not trade before this ET date.")
    parser.add_argument("--skip-git-publish", action="store_true", help="Generate files only, skip git commit/push.")
    parser.add_argument("--skip-data-refresh", action="store_true", help="Skip the daily CSV freshness check.")
    parser.add_argument("--dry-run", action="store_true", help="Do not persist state or write outputs.")
    return parser.parse_args()


def ensure_dirs() -> None:
    LIVE_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)


def now_et_from_arg(value: str | None) -> pd.Timestamp:
    if value:
        ts = pd.Timestamp(value)
    else:
        ts = pd.Timestamp.now(tz=ET)
    if ts.tzinfo is None:
        ts = ts.tz_localize(ET)
    else:
        ts = ts.tz_convert(ET)
    return ts


def slot_key_for_timestamp(now_et: pd.Timestamp, force_slot: str | None = None) -> str | None:
    if force_slot:
        return force_slot

    for slot, (hour, minute) in SLOT_TO_ET.items():
        scheduled = now_et.normalize() + pd.Timedelta(hours=hour, minutes=minute)
        if abs((now_et - scheduled).total_seconds()) <= 12 * 60:
            return slot
    return None


def load_state(start_date: str) -> dict[str, Any]:
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text())
    else:
        state = {
            "version": VERSION,
            "initial_capital": INITIAL_CAPITAL,
            "cash": INITIAL_CAPITAL,
            "positions": [],
            "processed_slots": {},
            "start_date": start_date,
        }
    state.setdefault("version", VERSION)
    state.setdefault("initial_capital", INITIAL_CAPITAL)
    state.setdefault("cash", INITIAL_CAPITAL)
    state.setdefault("positions", [])
    state.setdefault("processed_slots", {})
    state.setdefault("start_date", start_date)
    return state


def save_state(state: dict[str, Any]) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2))


def load_csv_log(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def save_csv_log(path: Path, df: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def build_universe() -> list[str]:
    presets = build_named_universe_map(
        min_market_cap=1e9,
        min_price=10.0,
        spy_tickers_path=BASE_DIR / "spy_tickers.txt",
        qqq_tickers_path=BASE_DIR / "qqq_tickers.txt",
    )
    return presets[UNIVERSE_NAME]


def latest_required_history_date(now_et: pd.Timestamp) -> pd.Timestamp:
    current = now_et.normalize().tz_localize(None)
    return (current - pd.offsets.BDay(1)).normalize()


def csv_history_is_stale(tickers: list[str], now_et: pd.Timestamp) -> bool:
    required = latest_required_history_date(now_et).normalize()
    sample = tickers[: min(10, len(tickers))]
    for ticker in sample:
        path = DATA_DIR / f"{ticker}.csv"
        if not path.exists():
            return True
        try:
            df = pd.read_csv(path, usecols=["Date"])
            last_date = pd.to_datetime(df["Date"], errors="coerce").dropna().max()
        except Exception:
            return True
        if pd.isna(last_date) or pd.Timestamp(last_date).normalize() < required:
            return True
    return False


def maybe_refresh_daily_data(tickers: list[str], now_et: pd.Timestamp, events_df: pd.DataFrame) -> pd.DataFrame:
    if not REFRESH_DATA_IF_STALE:
        return events_df
    if not csv_history_is_stale(tickers, now_et):
        return events_df

    summary = refresh_reversal_data(
        tickers=tickers,
        start_date="2024-01-01",
        data_dir=DATA_DIR,
        skip_existing=False,
    )
    refresh_event = {
        "timestamp_et": now_et.isoformat(),
        "trade_date_et": now_et.date().isoformat(),
        "slot": "data_refresh",
        "event_type": "data_refresh",
        "detail": summary["status"].value_counts(dropna=False).to_dict(),
    }
    return pd.concat([events_df, pd.DataFrame([refresh_event])], ignore_index=True)


def load_reversal_csv(ticker: str) -> pd.DataFrame:
    file_path = DATA_DIR / f"{ticker}.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"{ticker}: file not found -> {file_path}")

    df = pd.read_csv(file_path)
    df.columns = df.columns.str.replace(r"[ 　\t]", " ", regex=True).str.strip()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for col in ["Open", "High", "Low", "Adj Close", "Max Drop"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.sort_values("Date").reset_index(drop=True)
    df["Prev Close"] = df["Adj Close"].shift(1).fillna(df["Adj Close"])
    df["Log Return"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
    df["Rolling Sigma 20d"] = df["Log Return"].rolling(ROLLING_SIGMA_WINDOW).std() * np.sqrt(252)
    return df


def _clean_yf_columns(df: pd.DataFrame) -> pd.DataFrame:
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df


def get_live_snapshot(ticker: str, allow_extended_hours: bool = True) -> dict[str, Any]:
    def _safe_float(value: Any) -> float | None:
        if value is None:
            return None
        try:
            value = float(value)
        except (TypeError, ValueError):
            return None
        return value if np.isfinite(value) else None

    def _session_from_timestamp(ts: pd.Timestamp | None) -> str:
        if ts is None or pd.isna(ts):
            return "regular"
        clock = pd.Timestamp(ts)
        if clock.tzinfo is not None:
            try:
                clock = clock.tz_convert(ET)
            except Exception:
                clock = clock.tz_localize(None)
        minutes = clock.hour * 60 + clock.minute
        if minutes < 9 * 60 + 30:
            return "pre"
        if minutes >= 16 * 60:
            return "post"
        return "regular"

    tk = yf.Ticker(ticker)
    intraday = tk.history(period="5d", interval="1m", auto_adjust=False, prepost=allow_extended_hours)
    regular_intraday = tk.history(period="5d", interval="1m", auto_adjust=False, prepost=False)
    daily = tk.history(period="10d", interval="1d", auto_adjust=False)

    intraday = _clean_yf_columns(intraday)
    regular_intraday = _clean_yf_columns(regular_intraday)
    daily = _clean_yf_columns(daily)

    if daily.empty or "Close" not in daily.columns:
        raise ValueError(f"{ticker}: unable to fetch recent daily close data.")

    intraday_close = pd.Series(dtype=float)
    regular_close = pd.Series(dtype=float)
    if not intraday.empty and "Close" in intraday.columns:
        intraday_close = pd.to_numeric(intraday["Close"], errors="coerce").dropna()
    if not regular_intraday.empty and "Close" in regular_intraday.columns:
        regular_close = pd.to_numeric(regular_intraday["Close"], errors="coerce").dropna()
    daily_close = pd.to_numeric(daily["Close"], errors="coerce").dropna()

    info: dict[str, Any]
    try:
        info = tk.info or {}
    except Exception:
        info = {}

    post_market_price = _safe_float(info.get("postMarketPrice")) if allow_extended_hours else None
    pre_market_price = _safe_float(info.get("preMarketPrice")) if allow_extended_hours else None
    regular_market_price = _safe_float(info.get("regularMarketPrice"))

    current_price = None
    asof = pd.Timestamp(intraday_close.index[-1]) if not intraday_close.empty else pd.NaT
    session = _session_from_timestamp(asof if not pd.isna(asof) else None)
    price_source = "1m intraday close"

    if post_market_price is not None:
        current_price = post_market_price
        session = "post"
        price_source = "Yahoo info.postMarketPrice"
    elif pre_market_price is not None:
        current_price = pre_market_price
        session = "pre"
        price_source = "Yahoo info.preMarketPrice"
    elif not intraday_close.empty:
        current_price = float(intraday_close.iloc[-1])
        price_source = "1m pre/post close" if allow_extended_hours else "1m regular close"
    elif regular_market_price is not None:
        current_price = regular_market_price
        session = "regular"
        price_source = "Yahoo info.regularMarketPrice"
    elif not regular_close.empty:
        current_price = float(regular_close.iloc[-1])
        session = "regular"
        price_source = "1m regular close"
        asof = pd.Timestamp(regular_close.index[-1])
    else:
        current_price = float(daily_close.iloc[-1])
        session = "regular"
        price_source = "1d close fallback"
        asof = pd.Timestamp(daily_close.index[-1])

    prev_close = _safe_float(info.get("regularMarketPreviousClose")) or _safe_float(info.get("previousClose"))
    if prev_close is None:
        daily_dates = pd.to_datetime(daily_close.index)
        asof_date = pd.Timestamp(asof).date() if not pd.isna(asof) else None
        if asof_date is not None and len(daily_close) >= 2 and daily_dates[-1].date() == asof_date:
            prev_close = float(daily_close.iloc[-2])
        else:
            prev_close = float(daily_close.iloc[-1])

    if prev_close <= 0:
        raise ValueError(f"{ticker}: previous close is non-positive.")

    current_drop_amount = max(prev_close - current_price, 0.0)
    current_drop_pct = current_drop_amount / prev_close if prev_close > 0 else np.nan
    target_rebound_amount = current_drop_amount * RECOVER_TARGET
    target_price = current_price + target_rebound_amount

    return {
        "ticker": ticker,
        "asof": asof,
        "session": session,
        "price_source": price_source,
        "current_price": float(current_price),
        "prev_close": float(prev_close),
        "current_drop_amount": float(current_drop_amount),
        "current_drop_pct": float(current_drop_pct),
        "target_rebound_amount": float(target_rebound_amount),
        "target_price": float(target_price),
    }


def trading_days_to_expiry(expiry_str: str) -> int:
    today = pd.Timestamp.today().normalize()
    expiry_ts = pd.Timestamp(expiry_str).normalize()
    if expiry_ts <= today:
        return 0
    return len(pd.bdate_range(today + pd.Timedelta(days=1), expiry_ts))


def choose_option_mark(calls: pd.DataFrame) -> pd.Series:
    bid = pd.to_numeric(calls.get("bid"), errors="coerce")
    ask = pd.to_numeric(calls.get("ask"), errors="coerce")
    last = pd.to_numeric(calls.get("lastPrice"), errors="coerce")
    mark = np.where((bid > 0) & (ask > 0), (bid + ask) / 2, np.nan)
    mark = np.where(np.isnan(mark) & (last > 0), last, mark)
    mark = np.where(np.isnan(mark) & (ask > 0), ask, mark)
    mark = np.where(np.isnan(mark) & (bid > 0), bid, mark)
    return pd.Series(mark, index=calls.index, dtype=float)


def fetch_call_candidates(
    ticker: str,
    spot: float,
    min_trading_dte: int = MIN_TRADING_DTE,
    max_trading_dte: int = MAX_TRADING_DTE,
    max_abs_moneyness_pct: float = MAX_ABS_MONEYNESS_PCT,
    max_otm_pct: float = MAX_OTM_PCT,
) -> pd.DataFrame:
    tk = yf.Ticker(ticker)
    expiries = list(getattr(tk, "options", []) or [])
    if not expiries:
        raise ValueError(f"{ticker}: no option expiries returned by Yahoo Finance.")

    frames = []
    today = pd.Timestamp.today().normalize()
    for expiry in expiries:
        tdte = trading_days_to_expiry(expiry)
        if tdte < min_trading_dte or tdte > max_trading_dte:
            continue
        try:
            calls = tk.option_chain(expiry).calls.copy()
        except Exception:
            continue
        if calls.empty:
            continue
        calls["expiry"] = pd.Timestamp(expiry)
        calls["trading_dte"] = tdte
        calls["calendar_dte"] = int((pd.Timestamp(expiry).normalize() - today).days)
        frames.append(calls)

    if not frames:
        raise ValueError(f"{ticker}: no call expiries found in the {min_trading_dte}-{max_trading_dte} trading-day window.")

    calls = pd.concat(frames, ignore_index=True)
    calls["strike"] = pd.to_numeric(calls.get("strike"), errors="coerce")
    calls["bid"] = pd.to_numeric(calls.get("bid"), errors="coerce")
    calls["ask"] = pd.to_numeric(calls.get("ask"), errors="coerce")
    calls["lastPrice"] = pd.to_numeric(calls.get("lastPrice"), errors="coerce")
    calls["volume"] = pd.to_numeric(calls.get("volume"), errors="coerce").fillna(0)
    calls["openInterest"] = pd.to_numeric(calls.get("openInterest"), errors="coerce").fillna(0)
    calls["impliedVolatility"] = pd.to_numeric(calls.get("impliedVolatility"), errors="coerce")
    calls["mark_price"] = choose_option_mark(calls)
    calls = calls[calls["mark_price"] > 0].copy()

    calls["spread_pct"] = np.where(
        calls["mark_price"] > 0,
        (calls["ask"] - calls["bid"]) / calls["mark_price"],
        np.nan,
    )
    calls["moneyness_pct"] = (calls["strike"] - spot) / spot
    calls["abs_moneyness_pct"] = calls["moneyness_pct"].abs()
    calls = calls[calls["abs_moneyness_pct"] <= max_abs_moneyness_pct].copy()
    calls = calls[calls["moneyness_pct"] <= max_otm_pct].copy()
    if calls.empty:
        raise ValueError(f"{ticker}: no near-ATM calls remain after the moneyness filter.")

    calls["liquidity_ok"] = (
        (calls["openInterest"] >= MIN_OPEN_INTEREST)
        & (calls["spread_pct"].fillna(1.0) <= MAX_SPREAD_PCT)
    )
    calls = calls.sort_values(
        ["abs_moneyness_pct", "liquidity_ok", "spread_pct", "trading_dte", "openInterest", "volume"],
        ascending=[True, False, True, True, False, False],
        na_position="last",
    ).reset_index(drop=True)
    return calls


def fetch_contract_quote(ticker: str, expiry: str, contract_symbol: str, strike: float) -> dict[str, Any]:
    tk = yf.Ticker(ticker)
    calls = tk.option_chain(expiry).calls.copy()
    if calls.empty:
        raise ValueError(f"{ticker}: option chain for {expiry} is empty.")

    calls["strike"] = pd.to_numeric(calls.get("strike"), errors="coerce")
    calls["bid"] = pd.to_numeric(calls.get("bid"), errors="coerce")
    calls["ask"] = pd.to_numeric(calls.get("ask"), errors="coerce")
    calls["lastPrice"] = pd.to_numeric(calls.get("lastPrice"), errors="coerce")
    calls["impliedVolatility"] = pd.to_numeric(calls.get("impliedVolatility"), errors="coerce")
    calls["mark_price"] = choose_option_mark(calls)

    selected = calls[calls["contractSymbol"].astype(str) == contract_symbol]
    if selected.empty:
        selected = calls[np.isclose(calls["strike"], strike, atol=1e-9)]
    if selected.empty:
        raise ValueError(f"{ticker}: contract {contract_symbol} not found on expiry {expiry}.")

    row = selected.iloc[0]
    iv = float(row["impliedVolatility"]) * 100 if pd.notna(row["impliedVolatility"]) else np.nan
    return {
        "contract_symbol": str(row["contractSymbol"]),
        "mark_price": float(row["mark_price"]),
        "bid": float(row["bid"]) if pd.notna(row["bid"]) else np.nan,
        "ask": float(row["ask"]) if pd.notna(row["ask"]) else np.nan,
        "last_price": float(row["lastPrice"]) if pd.notna(row["lastPrice"]) else np.nan,
        "iv_pct": iv if np.isfinite(iv) else np.nan,
    }


def compute_live_reversal_probability(
    df: pd.DataFrame,
    current_drop_pct: float,
    target_bounce_pct: float = RECOVER_TARGET,
    forward_days: int = FORWARD_DAYS,
    obs_window: int = LOOKBACK_DAYS,
) -> tuple[float, pd.DataFrame]:
    if current_drop_pct <= 0:
        return np.nan, pd.DataFrame()

    start_idx = max(1, len(df) - obs_window)
    rows = []
    for idx in range(start_idx, len(df) - forward_days):
        row = df.loc[idx]
        signal_prev_close = float(row["Prev Close"])
        signal_low = float(row["Low"])
        signal_drop_pct = float(row["Max Drop"])

        if any(np.isnan(x) for x in [signal_prev_close, signal_low, signal_drop_pct]):
            continue
        if signal_prev_close <= 0 or signal_low <= 0:
            continue
        if signal_drop_pct < current_drop_pct:
            continue

        signal_drop_amount = signal_drop_pct * signal_prev_close
        if signal_drop_amount <= 0:
            continue

        future_high = pd.to_numeric(df.loc[idx + 1: idx + forward_days, "High"], errors="coerce").max()
        if np.isnan(future_high):
            continue

        recovered_amount = future_high - signal_low
        recover_ratio = recovered_amount / signal_drop_amount
        target_price = signal_low + signal_drop_amount * target_bounce_pct
        rows.append(
            {
                "signal_date": row["Date"].date().isoformat(),
                "signal_drop_pct": signal_drop_pct * 100,
                "signal_drop_amount": signal_drop_amount,
                "entry_ref_price": signal_low,
                "rebound_target_price": target_price,
                "future_high": future_high,
                "recover_pct_of_drop": recover_ratio * 100,
                "success": bool(recover_ratio >= target_bounce_pct),
            }
        )

    matches = pd.DataFrame(rows)
    success_rate = matches["success"].mean() * 100 if not matches.empty else np.nan
    return float(success_rate) if not np.isnan(success_rate) else np.nan, matches


def screen_live_candidates(tickers: list[str]) -> tuple[pd.DataFrame, dict[str, pd.DataFrame]]:
    summary_rows: list[dict[str, Any]] = []
    detail_map: dict[str, pd.DataFrame] = {}

    for ticker in tickers:
        try:
            df = load_reversal_csv(ticker)
            live = get_live_snapshot(ticker)
            success_rate, matches = compute_live_reversal_probability(df=df, current_drop_pct=live["current_drop_pct"])
            rolling_sigma_series = pd.to_numeric(df.get("Rolling Sigma 20d"), errors="coerce").dropna()
            latest_rolling_sigma = float(rolling_sigma_series.iloc[-1]) * 100 if not rolling_sigma_series.empty else np.nan
            matched_signals = int(len(matches))
            detail_map[ticker] = matches
            summary_rows.append(
                {
                    "ticker": ticker,
                    "asof": live["asof"],
                    "live_price": round(live["current_price"], 2),
                    "live_price_raw": float(live["current_price"]),
                    "prev_close": round(live["prev_close"], 2),
                    "current_drop_%": round(live["current_drop_pct"] * 100, 2),
                    "current_drop_pct_raw": float(live["current_drop_pct"]),
                    "target_rebound_$": round(live["target_rebound_amount"], 2),
                    "target_price": round(live["target_price"], 2),
                    "rolling_sigma_20d_%": round(latest_rolling_sigma, 2) if np.isfinite(latest_rolling_sigma) else np.nan,
                    "matched_signals": matched_signals,
                    "success_rate_%": round(success_rate, 2) if not np.isnan(success_rate) else np.nan,
                }
            )
        except Exception as exc:
            summary_rows.append(
                {
                    "ticker": ticker,
                    "asof": pd.NaT,
                    "live_price": np.nan,
                    "live_price_raw": np.nan,
                    "prev_close": np.nan,
                    "current_drop_%": np.nan,
                    "current_drop_pct_raw": np.nan,
                    "target_rebound_$": np.nan,
                    "target_price": np.nan,
                    "rolling_sigma_20d_%": np.nan,
                    "matched_signals": 0,
                    "success_rate_%": np.nan,
                    "error": str(exc),
                }
            )

    summary_df = pd.DataFrame(summary_rows)
    if summary_df.empty:
        return summary_df, detail_map

    summary_df["call_candidate"] = (
        summary_df["success_rate_%"].fillna(-np.inf).ge(SUCCESS_RATE_GATE)
        & summary_df["matched_signals"].ge(MIN_MATCHED_SIGNALS)
        & summary_df["current_drop_pct_raw"].fillna(0).gt(MINIMUM_CURRENT_DROP_PCT)
    )
    summary_df = summary_df.sort_values(
        ["call_candidate", "success_rate_%", "matched_signals", "current_drop_%"],
        ascending=[False, False, False, False],
        na_position="last",
    ).reset_index(drop=True)
    return summary_df, detail_map


def business_days_since(entry_trade_date: str, current_trade_date: str) -> int:
    entry = pd.Timestamp(entry_trade_date).normalize()
    current = pd.Timestamp(current_trade_date).normalize()
    if current <= entry:
        return 0
    return len(pd.bdate_range(entry + pd.Timedelta(days=1), current))


def append_event(events_df: pd.DataFrame, now_et: pd.Timestamp, trade_date: str, slot: str, event_type: str, detail: dict[str, Any]) -> pd.DataFrame:
    row = {
        "timestamp_et": now_et.isoformat(),
        "trade_date_et": trade_date,
        "slot": slot,
        "event_type": event_type,
        "detail": json.dumps(detail, ensure_ascii=False, sort_keys=True),
    }
    return pd.concat([events_df, pd.DataFrame([row])], ignore_index=True)


def mark_open_positions(state: dict[str, Any], now_et: pd.Timestamp) -> tuple[list[dict[str, Any]], float]:
    marked = []
    total_value = 0.0
    trade_date = now_et.date().isoformat()
    for raw in state["positions"]:
        quote = fetch_contract_quote(raw["ticker"], raw["expiry"], raw["contract_symbol"], raw["strike"])
        live = get_live_snapshot(raw["ticker"])
        current_price = float(quote["mark_price"])
        position_value = current_price * 100 * raw["contracts"]
        pnl = (current_price - raw["entry_option_price"]) * 100 * raw["contracts"]
        pnl_pct = (current_price / raw["entry_option_price"] - 1) * 100 if raw["entry_option_price"] > 0 else np.nan
        day_number = business_days_since(raw["entry_trade_date"], trade_date)
        marked_row = {
            **raw,
            "asof_et": now_et.isoformat(),
            "current_spot": live["current_price"],
            "current_option_price": current_price,
            "current_bid": quote["bid"],
            "current_ask": quote["ask"],
            "current_iv_pct": quote["iv_pct"],
            "position_value": position_value,
            "unrealized_pnl": pnl,
            "unrealized_return_pct": pnl_pct,
            "business_days_held": day_number,
            "session": live["session"],
        }
        marked.append(marked_row)
        total_value += position_value
    return marked, total_value


def maybe_exit_positions(
    state: dict[str, Any],
    now_et: pd.Timestamp,
    slot_key: str,
    trades_df: pd.DataFrame,
    events_df: pd.DataFrame,
) -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame]:
    trade_date = now_et.date().isoformat()
    remaining_positions = []
    marked_positions, _ = mark_open_positions(state, now_et) if state["positions"] else ([], 0.0)
    by_id = {row["position_id"]: row for row in marked_positions}

    for raw in state["positions"]:
        marked = by_id[raw["position_id"]]
        current_price = float(marked["current_option_price"])
        business_days_held = int(marked["business_days_held"])
        target = raw["planned_tp_day1"] if business_days_held <= 1 else raw["planned_tp_day2"]
        exit_reason = None

        if current_price <= raw["planned_stop"]:
            exit_reason = "stop_loss_hit_at_scan"
        elif current_price >= target:
            exit_reason = "take_profit_day1_hit_at_scan" if business_days_held <= 1 else "take_profit_day2_hit_at_scan"
        elif business_days_held >= 2 and slot_key == "manage_1600":
            exit_reason = "time_exit_at_4pm_scan"

        if exit_reason is None:
            remaining_positions.append(raw)
            continue

        proceeds = current_price * 100 * raw["contracts"]
        pnl = proceeds - raw["entry_option_price"] * 100 * raw["contracts"]
        state["cash"] += proceeds
        trade_row = {
            "position_id": raw["position_id"],
            "ticker": raw["ticker"],
            "contract_symbol": raw["contract_symbol"],
            "entry_timestamp_et": raw["entry_timestamp"],
            "exit_timestamp_et": now_et.isoformat(),
            "entry_trade_date_et": raw["entry_trade_date"],
            "exit_trade_date_et": trade_date,
            "entry_option_price": raw["entry_option_price"],
            "exit_option_price": current_price,
            "entry_spot": raw["entry_spot"],
            "exit_spot": marked["current_spot"],
            "entry_iv_pct": raw.get("entry_iv_pct"),
            "exit_iv_pct": marked.get("current_iv_pct"),
            "contracts": raw["contracts"],
            "allocated_cash": raw["allocated_cash"],
            "proceeds": proceeds,
            "pnl": pnl,
            "return_pct": pnl / raw["allocated_cash"] * 100 if raw["allocated_cash"] > 0 else np.nan,
            "success_rate": raw["success_rate"],
            "matched_signals": raw["matched_signals"],
            "current_drop_pct_at_entry": raw["current_drop_pct"],
            "exit_reason": exit_reason,
            "business_days_held": business_days_held,
        }
        trades_df = pd.concat([trades_df, pd.DataFrame([trade_row])], ignore_index=True)
        events_df = append_event(
            events_df,
            now_et=now_et,
            trade_date=trade_date,
            slot=slot_key,
            event_type="exit",
            detail={
                "ticker": raw["ticker"],
                "contract_symbol": raw["contract_symbol"],
                "reason": exit_reason,
                "pnl": round(float(pnl), 2),
                "return_pct": round(float(trade_row["return_pct"]), 2) if pd.notna(trade_row["return_pct"]) else None,
            },
        )

    state["positions"] = remaining_positions
    return state, trades_df, events_df


def maybe_enter_position(
    state: dict[str, Any],
    now_et: pd.Timestamp,
    slot_key: str,
    summary_df: pd.DataFrame,
    trades_df: pd.DataFrame,
    events_df: pd.DataFrame,
) -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame]:
    if slot_key != "entry_1500":
        return state, trades_df, events_df
    if len(state["positions"]) >= MAX_OPEN_POSITIONS:
        return state, trades_df, append_event(events_df, now_et, now_et.date().isoformat(), slot_key, "entry_skipped", {"reason": "max_open_positions"})  # type: ignore[arg-type]

    open_tickers = {position["ticker"] for position in state["positions"]}
    candidates = summary_df[
        summary_df["call_candidate"]
        & ~summary_df["ticker"].isin(open_tickers)
    ].copy()
    if candidates.empty:
        events_df = append_event(
            events_df,
            now_et=now_et,
            trade_date=now_et.date().isoformat(),
            slot=slot_key,
            event_type="entry_skipped",
            detail={"reason": "no_candidate"},
        )
        return state, trades_df, events_df

    candidate = candidates.iloc[0]
    ticker = str(candidate["ticker"])
    spot = float(candidate["live_price_raw"])
    calls = fetch_call_candidates(ticker, spot=spot)
    selected = calls.iloc[0]
    entry_price = float(selected["mark_price"])
    if entry_price <= 0:
        events_df = append_event(
            events_df,
            now_et=now_et,
            trade_date=now_et.date().isoformat(),
            slot=slot_key,
            event_type="entry_skipped",
            detail={"ticker": ticker, "reason": "invalid_entry_price"},
        )
        return state, trades_df, events_df

    marked_positions, current_position_value = mark_open_positions(state, now_et) if state["positions"] else ([], 0.0)
    current_equity = float(state["cash"]) + current_position_value
    budget = min(float(state["cash"]), current_equity * TARGET_POSITION_WEIGHT)
    entry_cost = entry_price * 100
    contracts = int(budget // entry_cost)
    if contracts <= 0:
        events_df = append_event(
            events_df,
            now_et=now_et,
            trade_date=now_et.date().isoformat(),
            slot=slot_key,
            event_type="entry_skipped",
            detail={"ticker": ticker, "reason": "insufficient_cash", "budget": round(budget, 2), "entry_cost": round(entry_cost, 2)},
        )
        return state, trades_df, events_df

    spent = contracts * entry_cost
    state["cash"] -= spent
    entry_iv_pct = float(selected["impliedVolatility"]) * 100 if pd.notna(selected["impliedVolatility"]) else np.nan
    position = Position(
        position_id=f"{ticker}_{now_et.strftime('%Y%m%dT%H%M%S')}",
        ticker=ticker,
        contract_symbol=str(selected["contractSymbol"]),
        expiry=pd.Timestamp(selected["expiry"]).date().isoformat(),
        strike=float(selected["strike"]),
        entry_timestamp=now_et.isoformat(),
        entry_trade_date=now_et.date().isoformat(),
        entry_slot=slot_key,
        entry_spot=spot,
        entry_option_price=entry_price,
        entry_bid=float(selected["bid"]) if pd.notna(selected["bid"]) else np.nan,
        entry_ask=float(selected["ask"]) if pd.notna(selected["ask"]) else np.nan,
        entry_iv_pct=entry_iv_pct if np.isfinite(entry_iv_pct) else np.nan,
        contracts=contracts,
        allocated_cash=spent,
        success_rate=float(candidate["success_rate_%"]),
        matched_signals=int(candidate["matched_signals"]),
        current_drop_pct=float(candidate["current_drop_%"]),
        rolling_sigma_20d_pct=float(candidate["rolling_sigma_20d_%"]) if pd.notna(candidate["rolling_sigma_20d_%"]) else np.nan,
        planned_tp_day1=entry_price * (1 + DAY1_TAKE_PROFIT_PCT),
        planned_tp_day2=entry_price * (1 + DAY2_TAKE_PROFIT_PCT),
        planned_stop=entry_price * (1 - STOP_LOSS_PCT),
    )
    state["positions"].append(asdict(position))
    events_df = append_event(
        events_df,
        now_et=now_et,
        trade_date=now_et.date().isoformat(),
        slot=slot_key,
        event_type="entry",
        detail={
            "ticker": ticker,
            "contract_symbol": position.contract_symbol,
            "contracts": contracts,
            "entry_option_price": round(entry_price, 4),
            "allocated_cash": round(spent, 2),
            "success_rate": round(position.success_rate, 2),
            "matched_signals": position.matched_signals,
        },
    )
    return state, trades_df, events_df


def build_positions_frame(state: dict[str, Any], now_et: pd.Timestamp) -> pd.DataFrame:
    marked_positions, _ = mark_open_positions(state, now_et) if state["positions"] else ([], 0.0)
    if not marked_positions:
        return pd.DataFrame(
            columns=[
                "ticker",
                "contract_symbol",
                "entry_trade_date",
                "current_option_price",
                "unrealized_pnl",
                "unrealized_return_pct",
                "business_days_held",
            ]
        )
    df = pd.DataFrame(marked_positions)
    return df.sort_values(["unrealized_pnl", "ticker"], ascending=[False, True]).reset_index(drop=True)


def build_equity_row(state: dict[str, Any], now_et: pd.Timestamp, slot_key: str | None) -> dict[str, Any]:
    positions_df = build_positions_frame(state, now_et)
    position_value = float(positions_df["position_value"].sum()) if not positions_df.empty else 0.0
    equity = float(state["cash"]) + position_value
    return {
        "timestamp_et": now_et.isoformat(),
        "trade_date_et": now_et.date().isoformat(),
        "slot": slot_key or "manual",
        "cash": round(float(state["cash"]), 2),
        "position_value": round(position_value, 2),
        "equity": round(equity, 2),
        "open_count": int(len(state["positions"])),
        "open_tickers": ",".join(sorted(position["ticker"] for position in state["positions"])),
    }


def format_table(df: pd.DataFrame, columns: list[str] | None = None, max_rows: int = 20) -> str:
    if df.empty:
        return "_None_"
    if columns is not None:
        usable = [col for col in columns if col in df.columns]
        df = df[usable]
    return "```text\n" + df.head(max_rows).to_string(index=False) + "\n```"


def humanize_exit_reason(reason: str) -> str:
    mapping = {
        "stop_scan": "stop_loss_hit_at_scan",
        "tp_day1_scan": "take_profit_day1_hit_at_scan",
        "tp_day2_scan": "take_profit_day2_hit_at_scan",
        "time_exit_scan": "time_exit_at_4pm_scan",
    }
    return mapping.get(reason, reason)


def plot_live_equity(equity_df: pd.DataFrame) -> None:
    if equity_df.empty:
        return
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    plot_df = equity_df.copy()
    plot_df["timestamp_et"] = pd.to_datetime(plot_df["timestamp_et"], errors="coerce", utc=True)
    plot_df = plot_df[plot_df["timestamp_et"].notna()].copy()
    if plot_df.empty:
        return
    plot_df["timestamp_plot"] = plot_df["timestamp_et"].dt.tz_convert(ET).dt.tz_localize(None)
    plot_df = plot_df.sort_values("timestamp_plot").drop_duplicates(subset=["timestamp_plot"], keep="last")
    latest_ts = plot_df["timestamp_plot"].max()
    window_start = latest_ts - pd.Timedelta(days=PLOT_WINDOW_DAYS)
    plot_df = plot_df[plot_df["timestamp_plot"] >= window_start].copy()
    period_start_equity = float(plot_df["equity"].iloc[0])
    period_end_equity = float(plot_df["equity"].iloc[-1])
    period_return_pct = (period_end_equity / INITIAL_CAPITAL - 1.0) * 100
    line_color = "#34C759" if period_end_equity >= period_start_equity else "#FF3B30"
    y_band = INITIAL_CAPITAL * 0.10
    data_min = float(plot_df["equity"].min())
    data_max = float(plot_df["equity"].max())
    lower_bound = min(INITIAL_CAPITAL - y_band, data_min - INITIAL_CAPITAL * 0.01)
    upper_bound = max(INITIAL_CAPITAL + y_band, data_max + INITIAL_CAPITAL * 0.01)

    plt.figure(figsize=(12, 6))
    plt.plot(plot_df["timestamp_plot"], plot_df["equity"], linewidth=2.5, color=line_color, label="Equity")
    plt.fill_between(plot_df["timestamp_plot"], plot_df["equity"], period_start_equity, color=line_color, alpha=0.12)
    plt.axhline(INITIAL_CAPITAL, color="gray", linestyle="--", alpha=0.5, label="Initial Capital")
    axis = plt.gca()
    axis.set_ylim(lower_bound, upper_bound)
    locator = mdates.AutoDateLocator(minticks=3, maxticks=6)
    formatter = mdates.DateFormatter("%m-%d")
    axis.xaxis.set_major_locator(locator)
    axis.xaxis.set_major_formatter(formatter)
    return_axis = axis.twinx()
    return_axis.set_ylim(axis.get_ylim())
    return_axis.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{((value / INITIAL_CAPITAL) - 1.0) * 100:+.1f}%"))
    return_axis.set_ylabel("Return (%)")

    last_row = plot_df.iloc[-1]
    last_label = (
        f"{last_row['timestamp_plot'].strftime('%m-%d %I:%M %p ET')}\n"
        f"{((float(last_row['equity']) / INITIAL_CAPITAL) - 1.0) * 100:+.2f}%"
    )
    y_span = upper_bound - lower_bound
    near_top = float(last_row["equity"]) >= lower_bound + 0.82 * y_span
    label_offset = (-12, -18) if near_top else (-12, 14)
    label_va = "top" if near_top else "bottom"
    axis.annotate(
        last_label,
        xy=(last_row["timestamp_plot"], last_row["equity"]),
        xytext=label_offset,
        textcoords="offset points",
        ha="right",
        va=label_va,
        fontsize=9,
        color="#0F172A",
        bbox={"boxstyle": "round,pad=0.25", "facecolor": "white", "edgecolor": line_color, "alpha": 0.95},
    )
    plt.title(f"Reversal 3.1 Live Paper Equity (1W)  |  Return {period_return_pct:+.2f}%")
    plt.xlabel("Date (ET, trailing 1W)")
    plt.ylabel("Portfolio Value ($)")
    plt.grid(alpha=0.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(PLOT_PATH, dpi=160, bbox_inches="tight")
    plt.close()


def render_dashboard(
    state: dict[str, Any],
    summary_df: pd.DataFrame,
    trades_df: pd.DataFrame,
    events_df: pd.DataFrame,
    positions_df: pd.DataFrame,
    equity_df: pd.DataFrame,
    now_et: pd.Timestamp,
    slot_key: str | None,
) -> tuple[str, str]:
    last_equity = float(equity_df["equity"].iloc[-1]) if not equity_df.empty else float(state["cash"])
    realized_pnl = float(trades_df["pnl"].sum()) if not trades_df.empty else 0.0
    unrealized_pnl = float(positions_df["unrealized_pnl"].sum()) if not positions_df.empty else 0.0
    today = now_et.date().isoformat()
    today_trades = trades_df[trades_df.get("exit_trade_date_et", pd.Series(dtype=str)).astype(str) == today].copy() if not trades_df.empty and "exit_trade_date_et" in trades_df.columns else pd.DataFrame()
    recent_events = events_df.sort_values("timestamp_et", ascending=False).head(10) if not events_df.empty else pd.DataFrame()
    if not today_trades.empty and "exit_reason" in today_trades.columns:
        today_trades["exit_reason"] = today_trades["exit_reason"].astype(str).map(humanize_exit_reason)

    positions_view = positions_df.copy()
    if not positions_view.empty:
        numeric_cols = [
            "entry_spot", "current_spot", "entry_option_price", "current_option_price", "unrealized_pnl",
            "unrealized_return_pct", "entry_iv_pct", "current_iv_pct", "success_rate", "current_drop_pct", "rolling_sigma_20d_pct"
        ]
        for col in numeric_cols:
            if col in positions_view.columns:
                positions_view[col] = pd.to_numeric(positions_view[col], errors="coerce").round(2)

    screener_view = summary_df.copy()
    if not screener_view.empty:
        screener_view = screener_view[[
            "ticker", "success_rate_%", "matched_signals", "current_drop_%", "target_rebound_$",
            "target_price", "rolling_sigma_20d_%", "call_candidate"
        ]].head(12)

    dashboard_md = "\n".join(
        [
            "# Reversal 3.1 Live Paper Test",
            "",
            f"Last updated (ET): `{now_et.strftime('%Y-%m-%d %H:%M:%S %Z')}`",
            f"Last processed slot: `{slot_key or 'manual_refresh'}`",
            "",
            "## Active Configuration",
            "",
            "- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)",
            "- Lookback window: `60d`",
            "- Minimum current drop: `> 0.5%`",
            "- Recovery target: `70% of the signal-day drop`",
            "- Success-rate gate: `>= 80%`",
            "- Matched-signal gate: `>= 10`",
            "- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers",
            "- Entry scan: `3:00 PM ET`",
            "- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`",
            "- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed",
            "- Chart view: default display is trailing `1W`, with latest ET checkpoint annotation and return % axis",
            "",
            "## Portfolio Snapshot",
            "",
            f"- Cash: `${state['cash']:,.2f}`",
            f"- Equity: `${last_equity:,.2f}`",
            f"- Realized PnL: `${realized_pnl:,.2f}`",
            f"- Unrealized PnL: `${unrealized_pnl:,.2f}`",
            f"- Open positions: `{len(state['positions'])}`",
            "",
            "## Open Positions",
            "",
            format_table(
                positions_view,
                columns=[
                    "ticker", "contract_symbol", "entry_trade_date", "business_days_held",
                    "entry_option_price", "current_option_price", "entry_spot", "current_spot",
                    "unrealized_pnl", "unrealized_return_pct", "success_rate", "matched_signals",
                    "current_drop_pct", "entry_iv_pct", "current_iv_pct", "rolling_sigma_20d_pct"
                ],
                max_rows=10,
            ),
            "",
            f"## Today's Closed Trades ({today})",
            "",
            format_table(
                today_trades,
                columns=[
                    "ticker", "contract_symbol", "entry_trade_date_et", "exit_trade_date_et",
                    "entry_option_price", "exit_option_price", "pnl", "return_pct", "exit_reason"
                ],
                max_rows=20,
            ),
            "",
            "## Current Screener Snapshot",
            "",
            format_table(
                screener_view,
                columns=[
                    "ticker", "success_rate_%", "matched_signals", "current_drop_%",
                    "target_rebound_$", "target_price", "rolling_sigma_20d_%", "call_candidate"
                ],
                max_rows=12,
            ),
            "",
            "## Recent Events",
            "",
            format_table(recent_events, columns=["timestamp_et", "slot", "event_type", "detail"], max_rows=10),
            "",
            "## Equity Curve (1W)",
            "",
            "Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.",
            "",
            "![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)",
            "",
        ]
    )

    root_section = "\n".join(
        [
            ROOT_SECTION_START,
            "## Reversal 3.1 Live Paper Test",
            "",
            f"- Last updated (ET): `{now_et.strftime('%Y-%m-%d %H:%M:%S %Z')}`",
            f"- Equity: `${last_equity:,.2f}` | Realized: `${realized_pnl:,.2f}` | Unrealized: `${unrealized_pnl:,.2f}` | Open positions: `{len(state['positions'])}`",
            f"- Today closed trades: `{len(today_trades)}`",
            f"- Current slot: `{slot_key or 'manual_refresh'}`",
            "- Universe: `qqq_plus_leverage_etfs`",
            "- Chart: trailing `1W` with ET timestamps",
            "",
            format_table(
                positions_view,
                columns=["ticker", "contract_symbol", "current_option_price", "unrealized_pnl", "unrealized_return_pct", "business_days_held"],
                max_rows=8,
            ),
            "",
            "![Reversal 3.1 Live Equity 1W](assets/reversal_3_1_live_equity.png)",
            "",
            "- [Full live dashboard](results/reversal_3_1_live/README.md)",
            "- [Live trades csv](results/reversal_3_1_live/live_trades.csv)",
            "- [Live equity csv](results/reversal_3_1_live/live_equity.csv)",
            ROOT_SECTION_END,
        ]
    )
    return dashboard_md, root_section


def update_root_readme(root_section: str) -> None:
    if not ROOT_README_PATH.exists():
        return
    text = ROOT_README_PATH.read_text()
    if ROOT_SECTION_START in text and ROOT_SECTION_END in text:
        start = text.index(ROOT_SECTION_START)
        end = text.index(ROOT_SECTION_END) + len(ROOT_SECTION_END)
        text = text[:start] + root_section + text[end:]
    else:
        text = text.replace("# Reversal 2.5.3\n", "# Reversal 2.5.3\n\n" + root_section + "\n\n", 1)
    ROOT_README_PATH.write_text(text)


def extract_github_token() -> str | None:
    hosts_path = Path.home() / ".config" / "gh" / "hosts.yml"
    if not hosts_path.exists():
        return None
    current_host = None
    for raw_line in hosts_path.read_text().splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if not line.startswith(" "):
            current_host = line.rstrip(":")
            continue
        if current_host == "github.com" and "oauth_token:" in line:
            return line.split("oauth_token:", 1)[1].strip()
    return None


def maybe_git_publish(now_et: pd.Timestamp, dry_run: bool, skip_git_publish: bool) -> None:
    if dry_run or skip_git_publish:
        return
    token = extract_github_token()
    tracked_paths = [
        "README.md",
        "results/reversal_3_1_live/README.md",
        "results/reversal_3_1_live/live_trades.csv",
        "results/reversal_3_1_live/live_events.csv",
        "results/reversal_3_1_live/live_positions.csv",
        "results/reversal_3_1_live/live_equity.csv",
        "results/reversal_3_1_live/state.json",
        "assets/reversal_3_1_live_equity.png",
    ]

    def run_git(cmd: list[str]) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True, check=False)
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.returncode != 0 and result.stderr.strip():
            print(result.stderr.strip(), file=sys.stderr)
        return result

    run_git(["git", "add", *tracked_paths])
    status = run_git(["git", "status", "--short", "--", *tracked_paths])
    if not status.stdout.strip():
        return

    commit_message = f"Update Reversal 3.1 live paper test {now_et.strftime('%Y-%m-%d %H:%M ET')}"
    commit_result = run_git(["git", "commit", "-m", commit_message])
    if commit_result.returncode != 0:
        return

    if token:
        remote_url = f"https://x-access-token:{token}@github.com/randomwalkhan/Short-Term-Reversal-Strategy.git"
        run_git(["git", "pull", "--rebase", "--autostash", remote_url, "main"])
        run_git(["git", "push", remote_url, "HEAD:main"])
    else:
        run_git(["git", "pull", "--rebase", "--autostash", "origin", "main"])
        run_git(["git", "push", "origin", "HEAD:main"])


def run_cycle(args: argparse.Namespace) -> dict[str, Any]:
    ensure_dirs()
    now_et = now_et_from_arg(args.now)
    slot_key = slot_key_for_timestamp(now_et, args.force_slot)
    state = load_state(args.start_date)
    trades_df = load_csv_log(TRADES_PATH)
    events_df = load_csv_log(EVENTS_PATH)
    equity_df = load_csv_log(EQUITY_PATH)

    universe = build_universe()
    trade_date = now_et.date().isoformat()
    pre_start = pd.Timestamp(trade_date) < pd.Timestamp(state["start_date"])

    if not pre_start and REFRESH_DATA_IF_STALE and not args.skip_data_refresh:
        events_df = maybe_refresh_daily_data(universe, now_et, events_df)

    if pre_start:
        summary_df = pd.DataFrame()
    else:
        summary_df, _ = screen_live_candidates(universe)

    if pre_start:
        events_df = append_event(
            events_df,
            now_et=now_et,
            trade_date=trade_date,
            slot=slot_key or "manual",
            event_type="pre_start",
            detail={"start_date": state["start_date"]},
        )
    else:
        processed_for_day = state["processed_slots"].setdefault(trade_date, [])
        if slot_key and slot_key not in processed_for_day:
            if slot_key.startswith("manage_"):
                state, trades_df, events_df = maybe_exit_positions(state, now_et, slot_key, trades_df, events_df)
            if slot_key == "entry_1500":
                state, trades_df, events_df = maybe_enter_position(state, now_et, slot_key, summary_df, trades_df, events_df)
            processed_for_day.append(slot_key)
        elif slot_key:
            events_df = append_event(
                events_df,
                now_et=now_et,
                trade_date=trade_date,
                slot=slot_key,
                event_type="slot_skipped",
                detail={"reason": "already_processed"},
            )

    positions_df = build_positions_frame(state, now_et)
    equity_row = build_equity_row(state, now_et, slot_key)
    equity_df = pd.concat([equity_df, pd.DataFrame([equity_row])], ignore_index=True)

    if not args.dry_run:
        save_state(state)
        save_csv_log(TRADES_PATH, trades_df)
        save_csv_log(EVENTS_PATH, events_df)
        save_csv_log(POSITIONS_PATH, positions_df)
        save_csv_log(EQUITY_PATH, equity_df)
        plot_live_equity(equity_df)
        dashboard_md, root_section = render_dashboard(state, summary_df, trades_df, events_df, positions_df, equity_df, now_et, slot_key)
        DASHBOARD_PATH.write_text(dashboard_md)
        update_root_readme(root_section)
        maybe_git_publish(now_et, dry_run=args.dry_run, skip_git_publish=args.skip_git_publish)

    return {
        "timestamp_et": now_et.isoformat(),
        "slot": slot_key,
        "open_positions": len(state["positions"]),
        "cash": round(float(state["cash"]), 2),
        "equity": float(equity_row["equity"]),
    }


def main() -> None:
    args = parse_args()
    summary = run_cycle(args)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
