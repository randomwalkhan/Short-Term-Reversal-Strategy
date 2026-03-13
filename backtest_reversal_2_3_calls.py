from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm

from reversal_universe import build_nasdaq_spy_universe


INITIAL_CAPITAL = 10_000.0
LOOKBACK_DAYS = 252
FORWARD_DAYS = 5
RECOVER_TARGET = 0.70
SUCCESS_RATE_GATE = 80.0
ROLLING_SIGMA_WINDOW = 20
TRADING_DTE_AT_ENTRY = 30
RISK_FREE = 0.04
LIMIT_BUY_DISCOUNT_PCT = 0.10
DAY1_TAKE_PROFIT_PCT = 0.10
DAY2_TAKE_PROFIT_PCT = 0.15
STOP_LOSS_PCT = 0.10
BACKTEST_YEARS = 1
MAX_OPEN_POSITIONS = 2
MIN_MARKET_CAP = 1e9
MIN_PRICE = 10.0
DOWNLOAD_BATCH_SIZE = 100

OUTPUT_DIR = Path.cwd() / "backtest_outputs"
UNIVERSE_PATH = Path.cwd() / "universe_tickers.csv"
PLOT_PATH = OUTPUT_DIR / "reversal_2_3_call_backtest_equity.png"
TRADES_PATH = OUTPUT_DIR / "reversal_2_3_call_backtest_trades.csv"
EQUITY_PATH = OUTPUT_DIR / "reversal_2_3_call_backtest_equity.csv"


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
    daily_rank: int
    score_weight: float
    allocated_cash: float
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


def prepare_history_frame(raw_df: pd.DataFrame) -> pd.DataFrame:
    required_cols = ["Open", "High", "Low", "Close", "Adj Close"]
    missing = [col for col in required_cols if col not in raw_df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df = raw_df[required_cols].copy().reset_index()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce").dt.normalize()
    for col in required_cols:
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


def load_universe_history(start: str, end: str) -> tuple[pd.DataFrame, dict[str, PreparedHistory]]:
    universe_df = build_nasdaq_spy_universe(
        min_market_cap=MIN_MARKET_CAP,
        min_price=MIN_PRICE,
        spy_tickers_path=Path.cwd() / "spy_tickers.txt",
        save_path=UNIVERSE_PATH,
    )
    tickers = universe_df["ticker"].tolist()

    histories: dict[str, PreparedHistory] = {}
    for batch_start in range(0, len(tickers), DOWNLOAD_BATCH_SIZE):
        batch = tickers[batch_start: batch_start + DOWNLOAD_BATCH_SIZE]
        downloaded = yf.download(
            tickers=batch,
            start=start,
            end=end,
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
                df = prepare_history_frame(frame)
            except ValueError:
                continue
            if len(df) <= LOOKBACK_DAYS + FORWARD_DAYS:
                continue
            histories[ticker] = PreparedHistory(
                ticker=ticker,
                df=df,
                date_to_idx={date: idx for idx, date in enumerate(df["Date"])},
                max_drop=df["Max Drop"].to_numpy(dtype=float),
                signal_success=df["Signal Success"].fillna(False).to_numpy(dtype=bool),
                valid_signal=df["Valid Signal"].fillna(False).to_numpy(dtype=bool),
            )

    final_universe_df = universe_df[universe_df["ticker"].isin(histories)].reset_index(drop=True)
    final_universe_df.to_csv(UNIVERSE_PATH, index=False)
    return final_universe_df, histories


def compute_signal_success_rate(history: PreparedHistory, idx: int) -> tuple[float, int]:
    current_drop_pct = history.max_drop[idx]
    if np.isnan(current_drop_pct) or current_drop_pct <= 0:
        return np.nan, 0

    start_idx = max(1, idx - LOOKBACK_DAYS)
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


def evaluate_candidate(history: PreparedHistory, idx: int) -> dict[str, Any] | None:
    success_rate, matched_signals = compute_signal_success_rate(history=history, idx=idx)
    if np.isnan(success_rate) or success_rate < SUCCESS_RATE_GATE:
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
        "sigma_ann": sigma_ann,
        "entry_option_price": limit_buy,
    }


def allocate_scores(candidates: list[dict[str, Any]]) -> np.ndarray:
    scores = np.array([candidate["success_rate"] for candidate in candidates], dtype=float)
    total = float(scores.sum())
    if total <= 0:
        return np.repeat(1 / len(candidates), len(candidates))
    return scores / total


def build_equity_curve(history_map: dict[str, PreparedHistory]) -> tuple[pd.DataFrame, pd.DataFrame]:
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=BACKTEST_YEARS)).normalize()
    all_dates = sorted(
        {
            date
            for history in history_map.values()
            for date in history.df["Date"]
            if date >= trade_start
        }
    )

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
                    "daily_rank": position.daily_rank,
                    "score_weight": position.score_weight,
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

        open_tickers = {position.ticker for position in positions}
        remaining_slots = MAX_OPEN_POSITIONS - len(positions)
        if remaining_slots > 0:
            candidates = []
            for ticker, history in history_map.items():
                if ticker in open_tickers:
                    continue
                idx = history.date_to_idx.get(current_date)
                if idx is None or idx <= LOOKBACK_DAYS or idx + FORWARD_DAYS >= len(history.df):
                    continue
                candidate = evaluate_candidate(history, idx)
                if candidate is None:
                    continue
                candidates.append(candidate)

            if candidates:
                ranked = sorted(
                    candidates,
                    key=lambda item: (item["success_rate"], item["matched_signals"]),
                    reverse=True,
                )[:remaining_slots]
                score_weights = allocate_scores(ranked)
                starting_cash = cash

                for daily_rank, (candidate, weight) in enumerate(zip(ranked, score_weights), start=1):
                    entry_cost = candidate["entry_option_price"] * 100
                    budget = starting_cash * float(weight)
                    contracts = int(budget // entry_cost)
                    if contracts <= 0:
                        continue
                    spent = contracts * entry_cost
                    if spent > cash:
                        contracts = int(cash // entry_cost)
                        spent = contracts * entry_cost
                    if contracts <= 0 or spent <= 0:
                        continue

                    cash -= spent
                    positions.append(
                        Position(
                            ticker=str(candidate["ticker"]),
                            entry_date=current_date,
                            expiry_date=next_business_day(current_date, TRADING_DTE_AT_ENTRY),
                            entry_spot=float(candidate["spot_close"]),
                            strike=float(candidate["spot_close"]),
                            entry_option_price=float(candidate["entry_option_price"]),
                            contracts=contracts,
                            success_rate=float(candidate["success_rate"]),
                            matched_signals=int(candidate["matched_signals"]),
                            daily_rank=daily_rank,
                            score_weight=float(weight),
                            allocated_cash=spent,
                            planned_tp_day1=float(candidate["entry_option_price"]) * (1 + DAY1_TAKE_PROFIT_PCT),
                            planned_tp_day2=float(candidate["entry_option_price"]) * (1 + DAY2_TAKE_PROFIT_PCT),
                            planned_stop=float(candidate["entry_option_price"]) * (1 - STOP_LOSS_PCT),
                        )
                    )

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
            mark = mark_option_price(
                spot=float(row["Close"]),
                strike=position.strike,
                entry_date=position.entry_date,
                current_date=current_date,
                sigma_ann=sigma_ann,
            )
            marked_position_value += mark * 100 * position.contracts

        equity_rows.append(
            {
                "date": current_date,
                "cash": cash,
                "position_value": marked_position_value,
                "equity": cash + marked_position_value,
                "open_tickers": ",".join(sorted(position.ticker for position in positions)),
                "open_count": len(positions),
            }
        )

    equity_df = pd.DataFrame(equity_rows)
    trades_df = pd.DataFrame(trade_rows)
    return equity_df, trades_df


def plot_equity_curve(equity_df: pd.DataFrame, trades_df: pd.DataFrame, universe_size: int) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(12, 7))
    plt.plot(equity_df["date"], equity_df["equity"], linewidth=2, label="Strategy Equity")
    plt.axhline(INITIAL_CAPITAL, color="gray", linestyle="--", alpha=0.5, label="Initial Capital")
    plt.title("Reversal 2.3 Call Backtest Equity Curve")
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
        f"Universe: {universe_size}\n"
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

    universe_df, history_map = load_universe_history(
        start=data_start.strftime("%Y-%m-%d"),
        end=end_date.strftime("%Y-%m-%d"),
    )
    equity_df, trades_df = build_equity_curve(history_map)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    equity_df.to_csv(EQUITY_PATH, index=False)
    trades_df.to_csv(TRADES_PATH, index=False)
    plot_equity_curve(equity_df, trades_df, universe_size=len(universe_df))

    final_equity = float(equity_df["equity"].iloc[-1])
    total_return = (final_equity / INITIAL_CAPITAL - 1) * 100
    max_drawdown = ((equity_df["equity"] / equity_df["equity"].cummax()) - 1).min() * 100
    print(f"Universe size: {len(universe_df)}")
    print(f"Final equity: ${final_equity:,.2f}")
    print(f"Total return: {total_return:.2f}%")
    print(f"Max drawdown: {max_drawdown:.2f}%")
    print(f"Trades: {len(trades_df)}")
    if not trades_df.empty:
        print(f"Win rate: {(trades_df['pnl'] > 0).mean() * 100:.1f}%")
    print(f"Saved universe -> {UNIVERSE_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")
    print(f"Saved trades -> {TRADES_PATH}")


if __name__ == "__main__":
    main()
