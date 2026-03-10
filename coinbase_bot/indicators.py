from __future__ import annotations

import pandas as pd

from coinbase_bot.config import StrategyConfig


def _compute_rsi(close: pd.Series, window: int) -> pd.Series:
    delta = close.diff()
    gains = delta.clip(lower=0.0)
    losses = -delta.clip(upper=0.0)
    avg_gain = gains.ewm(alpha=1 / window, adjust=False, min_periods=window).mean()
    avg_loss = losses.ewm(alpha=1 / window, adjust=False, min_periods=window).mean()
    rs = avg_gain / avg_loss.replace(0.0, pd.NA)
    rsi = 100 - (100 / (1 + rs))
    return pd.to_numeric(rsi, errors="coerce").fillna(100.0)


def _compute_atr(frame: pd.DataFrame, window: int) -> pd.Series:
    prev_close = frame["close"].shift(1)
    high_low = frame["high"] - frame["low"]
    high_close = (frame["high"] - prev_close).abs()
    low_close = (frame["low"] - prev_close).abs()
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return true_range.ewm(alpha=1 / window, adjust=False, min_periods=window).mean()


def normalize_candles(frame: pd.DataFrame) -> pd.DataFrame:
    columns = {col.lower().replace(" ", "_"): col for col in frame.columns}
    rename_map = {}
    for normalized_name, original_name in columns.items():
        if normalized_name in {"start", "date", "timestamp"}:
            rename_map[original_name] = "start"
        elif normalized_name in {"open"}:
            rename_map[original_name] = "open"
        elif normalized_name in {"high"}:
            rename_map[original_name] = "high"
        elif normalized_name in {"low"}:
            rename_map[original_name] = "low"
        elif normalized_name in {"close", "adj_close"}:
            rename_map[original_name] = "close"
        elif normalized_name in {"volume"}:
            rename_map[original_name] = "volume"

    normalized = frame.rename(columns=rename_map).copy()
    required = ["start", "open", "high", "low", "close"]
    missing = [column for column in required if column not in normalized.columns]
    if missing:
        raise ValueError(f"Missing candle columns: {missing}")

    if "volume" not in normalized.columns:
        normalized["volume"] = 0.0

    normalized["start"] = pd.to_datetime(normalized["start"], utc=True)
    for column in ["open", "high", "low", "close", "volume"]:
        normalized[column] = pd.to_numeric(normalized[column], errors="coerce")

    normalized = normalized.dropna(subset=["start", "open", "high", "low", "close"])
    normalized = normalized.sort_values("start").drop_duplicates("start")
    normalized = normalized.reset_index(drop=True)
    return normalized[["start", "open", "high", "low", "close", "volume"]]


def build_signal_frame(candles: pd.DataFrame, config: StrategyConfig) -> pd.DataFrame:
    frame = normalize_candles(candles)

    frame["bb_mid"] = frame["close"].rolling(config.bollinger_window).mean()
    std = frame["close"].rolling(config.bollinger_window).std(ddof=0)
    frame["bb_upper"] = frame["bb_mid"] + (std * config.bollinger_stddev)
    frame["bb_lower"] = frame["bb_mid"] - (std * config.bollinger_stddev)
    frame["ema_fast"] = frame["close"].ewm(span=config.ema_fast, adjust=False).mean()
    frame["ema_slow"] = frame["close"].ewm(span=config.ema_slow, adjust=False).mean()
    frame["ema_slow_change"] = frame["ema_slow"] - frame["ema_slow"].shift(5)
    frame["rsi"] = _compute_rsi(frame["close"], config.rsi_window)
    frame["atr"] = _compute_atr(frame, config.atr_window)
    frame["atr_pct"] = frame["atr"] / frame["close"]
    volume_median = frame["volume"].rolling(20).median()
    frame["volume_ratio"] = frame["volume"] / volume_median.replace(0.0, pd.NA)
    return frame
