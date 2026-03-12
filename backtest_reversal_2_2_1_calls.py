from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm


TICKERS = ["SMCI", "SOXL", "TQQQ", "COIN", "MSTR", "HOOD", "PLTR", "ASML", "CRCL", "TSM", "AMZN"]
INITIAL_CAPITAL = 10_000.0
LOOKBACK_DAYS = 252
FORWARD_DAYS = 5
RECOVER_TARGET = 0.70
SUCCESS_RATE_GATE = 75.0
ROLLING_SIGMA_WINDOW = 20
TRADING_DTE_AT_ENTRY = 30
RISK_FREE = 0.04
LIMIT_BUY_DISCOUNT_PCT = 0.10
DAY1_TAKE_PROFIT_PCT = 0.10
DAY2_TAKE_PROFIT_PCT = 0.15
STOP_LOSS_PCT = 0.10
BACKTEST_YEARS = 1
OUTPUT_DIR = Path.cwd() / "backtest_outputs"
PLOT_PATH = OUTPUT_DIR / "reversal_2_2_1_call_backtest_equity.png"
TRADES_PATH = OUTPUT_DIR / "reversal_2_2_1_call_backtest_trades.csv"


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
    planned_tp_day1: float
    planned_tp_day2: float
    planned_stop: float
    day_count: int = 0


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


def download_ticker_history(ticker: str, start: str, end: str) -> pd.DataFrame:
    df = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=False,
        progress=False,
        threads=False,
    )
    if df.empty:
        raise ValueError(f"{ticker}: no price history downloaded.")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    required_cols = ["Open", "High", "Low", "Close", "Adj Close"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"{ticker}: missing columns {missing}")

    df = df[required_cols].copy().reset_index()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for col in required_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.sort_values("Date").reset_index(drop=True)
    df["Prev Close"] = df["Adj Close"].shift(1)
    df["Max Drop"] = (df["Prev Close"] - df["Low"]) / df["Prev Close"]
    df["Log Return"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
    df["Sigma Ann"] = df["Log Return"].rolling(ROLLING_SIGMA_WINDOW).std() * np.sqrt(252)
    return df.dropna(subset=["Date", "Open", "High", "Low", "Close", "Adj Close", "Prev Close", "Max Drop"]).reset_index(drop=True)


def load_universe(start: str, end: str) -> dict[str, pd.DataFrame]:
    history: dict[str, pd.DataFrame] = {}
    for ticker in TICKERS:
        history[ticker] = download_ticker_history(ticker, start=start, end=end)
    return history


def compute_signal_success_rate(
    df: pd.DataFrame,
    idx: int,
    obs_window: int,
    forward_days: int,
    recover_target: float,
) -> tuple[float, int]:
    current_drop_pct = float(df.loc[idx, "Max Drop"])
    if np.isnan(current_drop_pct) or current_drop_pct <= 0:
        return np.nan, 0

    start_idx = max(1, idx - obs_window)
    rows = []

    for signal_idx in range(start_idx, idx - forward_days):
        row = df.loc[signal_idx]
        signal_drop_pct = float(row["Max Drop"])
        signal_prev_close = float(row["Prev Close"])
        signal_low = float(row["Low"])

        if any(np.isnan(x) for x in [signal_drop_pct, signal_prev_close, signal_low]):
            continue
        if signal_drop_pct < current_drop_pct:
            continue

        signal_drop_amount = signal_drop_pct * signal_prev_close
        if signal_drop_amount <= 0:
            continue

        future_high = pd.to_numeric(df.loc[signal_idx + 1: signal_idx + forward_days, "High"], errors="coerce").max()
        if np.isnan(future_high):
            continue

        recover_ratio = (future_high - signal_low) / signal_drop_amount
        rows.append(recover_ratio >= recover_target)

    if not rows:
        return np.nan, 0
    return float(np.mean(rows) * 100), len(rows)


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


def evaluate_candidate(df: pd.DataFrame, idx: int) -> dict[str, Any] | None:
    success_rate, matched_signals = compute_signal_success_rate(
        df=df,
        idx=idx,
        obs_window=LOOKBACK_DAYS,
        forward_days=FORWARD_DAYS,
        recover_target=RECOVER_TARGET,
    )
    if np.isnan(success_rate) or success_rate < SUCCESS_RATE_GATE:
        return None

    sigma_ann = float(df.loc[idx, "Sigma Ann"])
    spot_close = float(df.loc[idx, "Close"])
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
        spot=float(df.loc[idx, "Low"]),
        strike=spot_close,
        tau_years=TRADING_DTE_AT_ENTRY / 252,
        r=RISK_FREE,
        sigma=sigma_ann,
    )
    limit_buy = option_mid * (1 - LIMIT_BUY_DISCOUNT_PCT)
    if option_low_today > limit_buy:
        return None

    return {
        "success_rate": success_rate,
        "matched_signals": matched_signals,
        "spot_close": spot_close,
        "sigma_ann": sigma_ann,
        "entry_option_price": limit_buy,
    }


def build_equity_curve(history: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame]:
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=BACKTEST_YEARS)).normalize()
    all_dates = sorted({date for df in history.values() for date in df["Date"] if date >= trade_start})

    cash = INITIAL_CAPITAL
    position: Position | None = None
    trade_rows: list[dict[str, Any]] = []
    equity_rows: list[dict[str, Any]] = []

    for current_date in all_dates:
        if position is not None:
            df = history[position.ticker]
            row = df[df["Date"] == current_date]
            if not row.empty:
                row = row.iloc[0]
                sigma_ann = float(row["Sigma Ann"])
                if np.isnan(sigma_ann) or sigma_ann <= 0:
                    sigma_ann = 0.60

                position.day_count += 1
                option_high = mark_option_price(
                    spot=float(row["High"]),
                    strike=position.strike,
                    entry_date=position.entry_date,
                    current_date=current_date,
                    sigma_ann=sigma_ann,
                )
                option_low = mark_option_price(
                    spot=float(row["Low"]),
                    strike=position.strike,
                    entry_date=position.entry_date,
                    current_date=current_date,
                    sigma_ann=sigma_ann,
                )
                option_close = mark_option_price(
                    spot=float(row["Close"]),
                    strike=position.strike,
                    entry_date=position.entry_date,
                    current_date=current_date,
                    sigma_ann=sigma_ann,
                )

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

                if exit_reason is not None and exit_price is not None:
                    proceeds = exit_price * 100 * position.contracts
                    cash += proceeds
                    pnl = proceeds - position.entry_option_price * 100 * position.contracts
                    trade_rows.append({
                        "ticker": position.ticker,
                        "entry_date": position.entry_date,
                        "exit_date": current_date,
                        "success_rate": position.success_rate,
                        "contracts": position.contracts,
                        "entry_option_price": position.entry_option_price,
                        "exit_option_price": exit_price,
                        "entry_spot": position.entry_spot,
                        "exit_spot_close": float(row["Close"]),
                        "pnl": pnl,
                        "return_pct": pnl / (position.entry_option_price * 100 * position.contracts) * 100,
                        "exit_reason": exit_reason,
                    })
                    position = None

        if position is None:
            candidates = []
            for ticker, df in history.items():
                row_idx = df.index[df["Date"] == current_date]
                if len(row_idx) == 0:
                    continue
                idx = int(row_idx[0])
                if idx <= LOOKBACK_DAYS or idx + FORWARD_DAYS >= len(df):
                    continue
                candidate = evaluate_candidate(df, idx)
                if candidate is None:
                    continue
                candidates.append((ticker, idx, candidate))

            if candidates:
                ticker, idx, candidate = max(
                    candidates,
                    key=lambda item: (item[2]["success_rate"], item[2]["matched_signals"]),
                )
                entry_cost = candidate["entry_option_price"] * 100
                contracts = int(cash // entry_cost)
                if contracts > 0:
                    cash -= contracts * entry_cost
                    position = Position(
                        ticker=ticker,
                        entry_date=current_date,
                        expiry_date=next_business_day(current_date, TRADING_DTE_AT_ENTRY),
                        entry_spot=candidate["spot_close"],
                        strike=candidate["spot_close"],
                        entry_option_price=candidate["entry_option_price"],
                        contracts=contracts,
                        success_rate=candidate["success_rate"],
                        planned_tp_day1=candidate["entry_option_price"] * (1 + DAY1_TAKE_PROFIT_PCT),
                        planned_tp_day2=candidate["entry_option_price"] * (1 + DAY2_TAKE_PROFIT_PCT),
                        planned_stop=candidate["entry_option_price"] * (1 - STOP_LOSS_PCT),
                    )

        marked_position_value = 0.0
        if position is not None:
            df = history[position.ticker]
            row = df[df["Date"] == current_date]
            if not row.empty:
                row = row.iloc[0]
                sigma_ann = float(row["Sigma Ann"])
                if np.isnan(sigma_ann) or sigma_ann <= 0:
                    sigma_ann = 0.60
                mark = mark_option_price(
                    spot=float(row["Close"]),
                    strike=position.strike,
                    entry_date=position.entry_date,
                    current_date=current_date,
                    sigma_ann=sigma_ann,
                )
                marked_position_value = mark * 100 * position.contracts

        equity_rows.append({
            "date": current_date,
            "cash": cash,
            "position_value": marked_position_value,
            "equity": cash + marked_position_value,
            "open_ticker": position.ticker if position is not None else "",
        })

    equity_df = pd.DataFrame(equity_rows)
    trades_df = pd.DataFrame(trade_rows)
    return equity_df, trades_df


def plot_equity_curve(equity_df: pd.DataFrame, trades_df: pd.DataFrame) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    equity_df = equity_df.copy()
    equity_df["cum_return_pct"] = (equity_df["equity"] / INITIAL_CAPITAL - 1) * 100

    plt.figure(figsize=(12, 7))
    plt.plot(equity_df["date"], equity_df["equity"], linewidth=2, label="Strategy Equity")
    plt.axhline(INITIAL_CAPITAL, color="gray", linestyle="--", alpha=0.5, label="Initial Capital")
    plt.title("Reversal 2.2.1 Call Backtest Equity Curve")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value ($)")
    plt.grid(alpha=0.25)
    plt.legend()

    final_equity = float(equity_df["equity"].iloc[-1])
    total_return = (final_equity / INITIAL_CAPITAL - 1) * 100
    max_drawdown = ((equity_df["equity"] / equity_df["equity"].cummax()) - 1).min() * 100
    trade_count = len(trades_df)
    win_rate = float((trades_df["pnl"] > 0).mean() * 100) if not trades_df.empty else 0.0

    text = (
        f"Final Equity: ${final_equity:,.2f}\n"
        f"Total Return: {total_return:.2f}%\n"
        f"Trades: {trade_count}\n"
        f"Win Rate: {win_rate:.1f}%\n"
        f"Max Drawdown: {max_drawdown:.2f}%"
    )
    plt.text(
        0.02,
        0.98,
        text,
        transform=plt.gca().transAxes,
        va="top",
        ha="left",
        bbox={"facecolor": "white", "alpha": 0.85, "edgecolor": "lightgray"},
    )

    plt.tight_layout()
    plt.savefig(PLOT_PATH, dpi=160, bbox_inches="tight")
    plt.close()


def main() -> None:
    end_date = pd.Timestamp.today().normalize() + pd.Timedelta(days=1)
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=BACKTEST_YEARS)).normalize()
    data_start = trade_start - pd.DateOffset(days=500)

    history = load_universe(start=data_start.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"))
    equity_df, trades_df = build_equity_curve(history)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    equity_df.to_csv(OUTPUT_DIR / "reversal_2_2_1_call_backtest_equity.csv", index=False)
    trades_df.to_csv(TRADES_PATH, index=False)
    plot_equity_curve(equity_df, trades_df)

    final_equity = float(equity_df["equity"].iloc[-1])
    total_return = (final_equity / INITIAL_CAPITAL - 1) * 100
    print(f"Final equity: ${final_equity:,.2f}")
    print(f"Total return: {total_return:.2f}%")
    print(f"Trades: {len(trades_df)}")
    if not trades_df.empty:
        print(f"Win rate: {(trades_df['pnl'] > 0).mean() * 100:.1f}%")
    print(f"Saved plot -> {PLOT_PATH}")
    print(f"Saved trades -> {TRADES_PATH}")


if __name__ == "__main__":
    main()
