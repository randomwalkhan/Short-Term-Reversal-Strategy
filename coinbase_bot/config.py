from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv


GRANULARITY_SECONDS = {
    "ONE_MINUTE": 60,
    "FIVE_MINUTE": 300,
    "FIFTEEN_MINUTE": 900,
    "THIRTY_MINUTE": 1800,
    "ONE_HOUR": 3600,
    "TWO_HOUR": 7200,
    "FOUR_HOUR": 14400,
    "SIX_HOUR": 21600,
    "ONE_DAY": 86400,
}


def _parse_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def _parse_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    return int(raw) if raw is not None else default


def _parse_float(name: str, default: float) -> float:
    raw = os.getenv(name)
    return float(raw) if raw is not None else default


def _parse_list(name: str, default: list[str]) -> list[str]:
    raw = os.getenv(name)
    if raw is None:
        return default
    return [item.strip().upper() for item in raw.split(",") if item.strip()]


@dataclass(frozen=True)
class StrategyConfig:
    bollinger_window: int = 20
    bollinger_stddev: float = 1.8
    rsi_window: int = 13
    rsi_entry: float = 32.0
    ema_fast: int = 50
    ema_slow: int = 200
    atr_window: int = 14
    atr_stop_multiple: float = 1.0
    entry_buffer: float = 0.003
    max_chase_atr: float = 0.35
    min_reward_risk: float = 1.25
    cooldown_candles: int = 4
    max_hold_candles: int = 48
    min_atr_pct: float = 0.004
    max_atr_pct: float = 0.08
    min_volume_ratio: float = 0.70


@dataclass(frozen=True)
class BotConfig:
    product_ids: list[str] = field(default_factory=lambda: ["BTC-USD", "ETH-USD", "SOL-USD"])
    granularity: str = "ONE_HOUR"
    lookback_candles: int = 260
    quote_currency: str = "USD"
    per_trade_quote_fraction: float = 0.08
    min_quote_order_size: float = 25.0
    min_cash_reserve: float = 150.0
    max_open_positions: int = 1
    max_daily_loss_quote: float = 150.0
    preview_live_orders: bool = True
    allow_live_trading: bool = False
    state_path: Path = Path("state/live_state.json")
    strategy: StrategyConfig = field(default_factory=StrategyConfig)

    @property
    def granularity_seconds(self) -> int:
        try:
            return GRANULARITY_SECONDS[self.granularity]
        except KeyError as exc:
            raise ValueError(f"Unsupported granularity: {self.granularity}") from exc


def load_config() -> BotConfig:
    load_dotenv()

    strategy = StrategyConfig(
        bollinger_window=_parse_int("STRATEGY_BOLLINGER_WINDOW", 20),
        bollinger_stddev=_parse_float("STRATEGY_BOLLINGER_STDDEV", 1.8),
        rsi_window=_parse_int("STRATEGY_RSI_WINDOW", 13),
        rsi_entry=_parse_float("STRATEGY_RSI_ENTRY", 32.0),
        ema_fast=_parse_int("STRATEGY_EMA_FAST", 50),
        ema_slow=_parse_int("STRATEGY_EMA_SLOW", 200),
        atr_window=_parse_int("STRATEGY_ATR_WINDOW", 14),
        atr_stop_multiple=_parse_float("STRATEGY_ATR_STOP_MULTIPLE", 1.0),
        entry_buffer=_parse_float("STRATEGY_ENTRY_BUFFER", 0.003),
        max_chase_atr=_parse_float("STRATEGY_MAX_CHASE_ATR", 0.35),
        min_reward_risk=_parse_float("STRATEGY_MIN_REWARD_RISK", 1.25),
        cooldown_candles=_parse_int("STRATEGY_COOLDOWN_CANDLES", 4),
        max_hold_candles=_parse_int("STRATEGY_MAX_HOLD_CANDLES", 48),
        min_atr_pct=_parse_float("STRATEGY_MIN_ATR_PCT", 0.004),
        max_atr_pct=_parse_float("STRATEGY_MAX_ATR_PCT", 0.08),
        min_volume_ratio=_parse_float("STRATEGY_MIN_VOLUME_RATIO", 0.70),
    )

    state_path = Path(os.getenv("BOT_STATE_PATH", "state/live_state.json"))

    return BotConfig(
        product_ids=_parse_list("BOT_PRODUCTS", ["BTC-USD", "ETH-USD", "SOL-USD"]),
        granularity=os.getenv("BOT_GRANULARITY", "ONE_HOUR").strip().upper(),
        lookback_candles=_parse_int("BOT_LOOKBACK_CANDLES", 260),
        quote_currency=os.getenv("BOT_QUOTE_CURRENCY", "USD").strip().upper(),
        per_trade_quote_fraction=_parse_float("BOT_PER_TRADE_QUOTE_FRACTION", 0.08),
        min_quote_order_size=_parse_float("BOT_MIN_QUOTE_ORDER_SIZE", 25.0),
        min_cash_reserve=_parse_float("BOT_MIN_CASH_RESERVE", 150.0),
        max_open_positions=_parse_int("BOT_MAX_OPEN_POSITIONS", 1),
        max_daily_loss_quote=_parse_float("BOT_MAX_DAILY_LOSS_QUOTE", 150.0),
        preview_live_orders=_parse_bool("BOT_PREVIEW_LIVE_ORDERS", True),
        allow_live_trading=_parse_bool("COINBASE_ALLOW_LIVE_TRADING", False),
        state_path=state_path,
        strategy=strategy,
    )

