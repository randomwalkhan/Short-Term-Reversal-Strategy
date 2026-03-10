from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from coinbase_bot.config import StrategyConfig


@dataclass(frozen=True)
class SignalDecision:
    action: str
    reason: str
    entry_price: float | None = None
    stop_price: float | None = None
    take_profit_price: float | None = None
    reward_risk: float | None = None
    indicators: dict[str, float] = field(default_factory=dict)


def _hold(reason: str, indicators: dict[str, float] | None = None) -> SignalDecision:
    return SignalDecision(action="HOLD", reason=reason, indicators=indicators or {})


def evaluate_long_entry(
    signal_frame: pd.DataFrame,
    config: StrategyConfig,
    reference_price: float | None = None,
) -> SignalDecision:
    if signal_frame.empty:
        return _hold("no candles")

    latest = signal_frame.iloc[-1]
    required_fields = [
        "close",
        "bb_mid",
        "bb_lower",
        "ema_fast",
        "ema_slow",
        "ema_slow_change",
        "rsi",
        "atr",
        "atr_pct",
        "volume_ratio",
    ]
    if latest[required_fields].isna().any():
        return _hold("indicator warmup incomplete")

    entry_price = float(reference_price if reference_price is not None else latest["close"])
    indicators = {
        "close": float(latest["close"]),
        "bb_mid": float(latest["bb_mid"]),
        "bb_lower": float(latest["bb_lower"]),
        "ema_fast": float(latest["ema_fast"]),
        "ema_slow": float(latest["ema_slow"]),
        "rsi": float(latest["rsi"]),
        "atr": float(latest["atr"]),
        "atr_pct": float(latest["atr_pct"]),
        "volume_ratio": float(latest["volume_ratio"]),
    }

    if latest["ema_fast"] <= latest["ema_slow"]:
        return _hold("trend filter failed", indicators)

    if latest["ema_slow_change"] <= 0:
        return _hold("slow trend is not rising", indicators)

    if latest["close"] > latest["bb_lower"] * (1 + config.entry_buffer):
        return _hold("price is not stretched below lower band", indicators)

    if latest["rsi"] > config.rsi_entry:
        return _hold("rsi is not oversold enough", indicators)

    if latest["atr_pct"] < config.min_atr_pct or latest["atr_pct"] > config.max_atr_pct:
        return _hold("volatility filter failed", indicators)

    if latest["volume_ratio"] < config.min_volume_ratio:
        return _hold("volume filter failed", indicators)

    if entry_price > latest["close"] + (latest["atr"] * config.max_chase_atr):
        return _hold("price already bounced too far after the signal candle", indicators)

    stop_price = float(entry_price - (latest["atr"] * config.atr_stop_multiple))
    take_profit_price = float(latest["bb_mid"])
    risk = entry_price - stop_price
    reward = take_profit_price - entry_price

    if risk <= 0:
        return _hold("invalid stop distance", indicators)

    if reward <= 0:
        return _hold("mean target is already below the entry", indicators)

    reward_risk = reward / risk
    if reward_risk < config.min_reward_risk:
        return _hold("reward to risk is too small", indicators)

    return SignalDecision(
        action="BUY",
        reason="mean reversion setup matched",
        entry_price=entry_price,
        stop_price=stop_price,
        take_profit_price=take_profit_price,
        reward_risk=reward_risk,
        indicators=indicators,
    )

