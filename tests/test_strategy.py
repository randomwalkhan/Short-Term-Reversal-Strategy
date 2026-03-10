from __future__ import annotations

import unittest

import pandas as pd

from coinbase_bot.config import StrategyConfig
from coinbase_bot.indicators import build_signal_frame
from coinbase_bot.strategy import evaluate_long_entry


class StrategyTests(unittest.TestCase):
    def test_build_signal_frame_adds_required_columns(self) -> None:
        candles = pd.DataFrame(
            {
                "start": pd.date_range("2025-01-01", periods=260, freq="h", tz="UTC"),
                "open": [100 + (index * 0.1) for index in range(260)],
                "high": [101 + (index * 0.1) for index in range(260)],
                "low": [99 + (index * 0.1) for index in range(260)],
                "close": [100 + (index * 0.1) for index in range(260)],
                "volume": [1000 + index for index in range(260)],
            }
        )
        frame = build_signal_frame(candles, StrategyConfig())
        for column in ["bb_mid", "bb_lower", "ema_fast", "ema_slow", "rsi", "atr"]:
            self.assertIn(column, frame.columns)

    def test_entry_signal_is_generated_for_valid_setup(self) -> None:
        frame = pd.DataFrame(
            [
                {
                    "close": 100.0,
                    "bb_mid": 103.0,
                    "bb_lower": 100.0,
                    "ema_fast": 108.0,
                    "ema_slow": 104.0,
                    "ema_slow_change": 0.8,
                    "rsi": 25.0,
                    "atr": 1.5,
                    "atr_pct": 0.015,
                    "volume_ratio": 1.2,
                }
            ]
        )
        decision = evaluate_long_entry(frame, StrategyConfig(), reference_price=100.1)
        self.assertEqual(decision.action, "BUY")
        self.assertGreater(decision.take_profit_price, decision.entry_price)
        self.assertLess(decision.stop_price, decision.entry_price)

    def test_entry_signal_is_blocked_when_trend_filter_fails(self) -> None:
        frame = pd.DataFrame(
            [
                {
                    "close": 100.0,
                    "bb_mid": 103.0,
                    "bb_lower": 99.8,
                    "ema_fast": 99.0,
                    "ema_slow": 101.0,
                    "ema_slow_change": -0.4,
                    "rsi": 25.0,
                    "atr": 1.5,
                    "atr_pct": 0.015,
                    "volume_ratio": 1.2,
                }
            ]
        )
        decision = evaluate_long_entry(frame, StrategyConfig(), reference_price=100.0)
        self.assertEqual(decision.action, "HOLD")
        self.assertIn("trend", decision.reason)


if __name__ == "__main__":
    unittest.main()
