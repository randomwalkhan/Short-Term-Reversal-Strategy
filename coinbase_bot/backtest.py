from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
from pathlib import Path

import pandas as pd

from coinbase_bot.config import BotConfig, load_config
from coinbase_bot.exchange import CoinbaseAdvancedClient
from coinbase_bot.indicators import build_signal_frame, normalize_candles
from coinbase_bot.strategy import evaluate_long_entry


@dataclass
class TradeResult:
    product_id: str
    entry_time: str
    exit_time: str
    entry_price: float
    exit_price: float
    return_pct: float
    pnl_quote: float
    exit_reason: str


def _load_csv(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    return normalize_candles(frame)


def _find_exit(
    frame: pd.DataFrame,
    entry_index: int,
    stop_price: float,
    take_profit_price: float,
    max_hold_candles: int,
) -> tuple[int, float, str]:
    final_index = min(len(frame) - 1, entry_index + max_hold_candles)
    for index in range(entry_index, final_index + 1):
        candle = frame.iloc[index]
        if candle["low"] <= stop_price and candle["high"] >= take_profit_price:
            return index, stop_price, "stop_hit_same_candle"
        if candle["low"] <= stop_price:
            return index, stop_price, "stop_hit"
        if candle["high"] >= take_profit_price:
            return index, take_profit_price, "take_profit_hit"
    last_candle = frame.iloc[final_index]
    return final_index, float(last_candle["close"]), "max_hold"


def run_backtest(product_id: str, candles: pd.DataFrame, config: BotConfig) -> tuple[dict[str, float], pd.DataFrame]:
    frame = build_signal_frame(candles, config.strategy)
    cash = 10_000.0
    equity_curve = [cash]
    trades: list[TradeResult] = []
    index = 0

    while index < len(frame) - 1:
        history = frame.iloc[: index + 1]
        next_open = float(frame.iloc[index + 1]["open"])
        decision = evaluate_long_entry(history, config.strategy, reference_price=next_open)
        if decision.action != "BUY":
            index += 1
            equity_curve.append(cash)
            continue

        entry_index = index + 1
        entry_time = frame.iloc[entry_index]["start"]
        position_quote = cash * config.per_trade_quote_fraction
        if position_quote <= 0:
            break

        trade_decision = evaluate_long_entry(history, config.strategy, reference_price=next_open)
        if trade_decision.action != "BUY":
            index += 1
            equity_curve.append(cash)
            continue

        exit_index, exit_price, exit_reason = _find_exit(
            frame=frame,
            entry_index=entry_index,
            stop_price=float(trade_decision.stop_price),
            take_profit_price=float(trade_decision.take_profit_price),
            max_hold_candles=config.strategy.max_hold_candles,
        )
        return_pct = (exit_price - next_open) / next_open
        pnl_quote = position_quote * return_pct
        cash += pnl_quote
        equity_curve.append(cash)
        trades.append(
            TradeResult(
                product_id=product_id,
                entry_time=entry_time.isoformat(),
                exit_time=frame.iloc[exit_index]["start"].isoformat(),
                entry_price=next_open,
                exit_price=exit_price,
                return_pct=return_pct * 100,
                pnl_quote=pnl_quote,
                exit_reason=exit_reason,
            )
        )
        index = exit_index + 1

    trades_frame = pd.DataFrame([asdict(trade) for trade in trades])
    peak = equity_curve[0]
    max_drawdown = 0.0
    for value in equity_curve:
        peak = max(peak, value)
        drawdown = 0.0 if peak == 0 else (peak - value) / peak
        max_drawdown = max(max_drawdown, drawdown)

    metrics = {
        "trades": float(len(trades_frame)),
        "win_rate_pct": 0.0 if trades_frame.empty else float((trades_frame["pnl_quote"] > 0).mean() * 100),
        "avg_return_pct": 0.0 if trades_frame.empty else float(trades_frame["return_pct"].mean()),
        "total_pnl_quote": 0.0 if trades_frame.empty else float(trades_frame["pnl_quote"].sum()),
        "total_return_pct": ((cash / 10_000.0) - 1) * 100,
        "max_drawdown_pct": max_drawdown * 100,
    }
    return metrics, trades_frame


def main() -> None:
    parser = argparse.ArgumentParser(description="Backtest the Coinbase mean-reversion strategy.")
    parser.add_argument("--product", required=True, help="Trading pair, for example BTC-USD.")
    parser.add_argument("--csv", type=Path, help="Optional CSV with candle data.")
    parser.add_argument("--candles", type=int, default=500, help="How many candles to test.")
    args = parser.parse_args()

    config = load_config()
    if args.csv:
        candles = _load_csv(args.csv)
    else:
        client = CoinbaseAdvancedClient()
        candles = client.fetch_candles(args.product, config.granularity, args.candles)

    metrics, trades = run_backtest(args.product, candles, config)
    print(f"Backtest for {args.product}")
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")
    if not trades.empty:
        print()
        print(trades.tail(10).to_string(index=False))


if __name__ == "__main__":
    main()

