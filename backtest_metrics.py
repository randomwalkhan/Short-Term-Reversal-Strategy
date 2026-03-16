from __future__ import annotations

import numpy as np
import pandas as pd


# Source: U.S. Treasury daily par yield curve rates, 10-year tenor on 2026-03-16.
TEN_YEAR_TBILL_DATE = "2026-03-16"
TEN_YEAR_TBILL_RATE = 0.0423
TRADING_DAYS_PER_YEAR = 252


def compute_annualized_sharpe(
    equity_df: pd.DataFrame,
    annual_risk_free_rate: float = TEN_YEAR_TBILL_RATE,
    trading_days_per_year: int = TRADING_DAYS_PER_YEAR,
) -> float:
    if equity_df.empty or "equity" not in equity_df.columns:
        return float("nan")

    daily_returns = equity_df["equity"].pct_change().dropna()
    if daily_returns.empty:
        return float("nan")

    daily_vol = float(daily_returns.std(ddof=1))
    if daily_vol == 0 or np.isnan(daily_vol):
        return float("nan")

    daily_rf = (1 + annual_risk_free_rate) ** (1 / trading_days_per_year) - 1
    excess_returns = daily_returns - daily_rf
    return float(excess_returns.mean() / daily_vol * np.sqrt(trading_days_per_year))
