from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.stats import norm

from backtest_metrics import TEN_YEAR_TBILL_DATE, TEN_YEAR_TBILL_RATE, compute_annualized_sharpe
from plot_theme import BASELINE, FIG_BG, TEXT, style_dark_axis
from reversal_universe import build_named_universe_map


INITIAL_CAPITAL = 10_000.0
FORWARD_DAYS = 5
RECOVER_TARGET = 0.70
SUCCESS_RATE_GATE = 80.0
MIN_MATCHED_SIGNALS = 10
ROLLING_SIGMA_WINDOW = 20
TRADING_DTE_AT_ENTRY = 30
RISK_FREE = 0.04
LIMIT_BUY_DISCOUNT_PCT = 0.10
DAY1_TAKE_PROFIT_PCT = 0.10
DAY2_TAKE_PROFIT_PCT = 0.15
STOP_LOSS_PCT = 0.10
BACKTEST_YEARS = 1
MAX_OPEN_POSITIONS = 2
TARGET_POSITION_WEIGHT = 0.50
MIN_MARKET_CAP = 1e9
MIN_PRICE = 10.0
DOWNLOAD_BATCH_SIZE = 100

BASE_LOOKBACK_DAYS = 252
PCA_WINDOW_DAYS = 60
PCA_COMPONENTS = 15
FAST_KAPPA_THRESHOLD = 252 / 30
SCORE_OPEN_LONG = -1.25
VOLUME_TRAILING_WINDOW = 60
RECENT_WEIGHT_HALF_LIFE = 60.0
QQQ_PROXY = "QQQ"

OUTPUT_DIR = Path.cwd() / "results" / "reversal_2_4_article_variants"
PLOT_PATH = Path.cwd() / "assets" / "reversal_2_4_article_variants.png"
SUMMARY_PATH = OUTPUT_DIR / "reversal_article_variants_summary.csv"
CURVES_PATH = OUTPUT_DIR / "reversal_article_variants_equity.csv"


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


@dataclass
class VariantConfig:
    key: str
    label: str
    color: str
    linestyle: str
    evaluate_candidate: Callable[[PreparedHistory, int], dict[str, Any] | None]
    rank_key: Callable[[dict[str, Any]], tuple[Any, ...]]


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


def build_universe() -> list[str]:
    presets = build_named_universe_map(
        min_market_cap=MIN_MARKET_CAP,
        min_price=MIN_PRICE,
        spy_tickers_path=Path.cwd() / "spy_tickers.txt",
        qqq_tickers_path=Path.cwd() / "qqq_tickers.txt",
    )
    return presets["qqq_only_filtered"]


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
    required_cols = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
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
    df["Simple Return"] = df["Adj Close"].pct_change()
    df["Log Return"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
    df["Sigma Ann"] = df["Log Return"].rolling(ROLLING_SIGMA_WINDOW).std() * np.sqrt(252)
    df["Avg Volume"] = df["Volume"].rolling(VOLUME_TRAILING_WINDOW).mean()
    df["Volume Adjusted Drop"] = df["Max Drop"] * (df["Avg Volume"] / df["Volume"].replace(0, np.nan))

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
        subset=["Date", "Open", "High", "Low", "Close", "Adj Close", "Prev Close", "Max Drop", "Volume"]
    ).reset_index(drop=True)


def load_history_cache(tickers: list[str], start: str, end: str) -> dict[str, PreparedHistory]:
    histories: dict[str, PreparedHistory] = {}
    all_tickers = sorted(set(tickers + [QQQ_PROXY]))
    for batch_start in range(0, len(all_tickers), DOWNLOAD_BATCH_SIZE):
        batch = all_tickers[batch_start: batch_start + DOWNLOAD_BATCH_SIZE]
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
            if len(df) <= BASE_LOOKBACK_DAYS + FORWARD_DAYS:
                continue
            histories[ticker] = PreparedHistory(
                ticker=ticker,
                df=df,
                date_to_idx={date: idx for idx, date in enumerate(df["Date"])},
                max_drop=df["Max Drop"].to_numpy(dtype=float),
                signal_success=df["Signal Success"].fillna(False).to_numpy(dtype=bool),
                valid_signal=df["Valid Signal"].fillna(False).to_numpy(dtype=bool),
            )
    return histories


def build_return_matrix(history_map: dict[str, PreparedHistory], tickers: list[str]) -> pd.DataFrame:
    series = []
    for ticker in tickers:
        history = history_map.get(ticker)
        if history is None:
            continue
        s = history.df.set_index("Date")["Simple Return"].rename(ticker)
        series.append(s)
    if not series:
        return pd.DataFrame()
    return pd.concat(series, axis=1).sort_index()


def estimate_ou_from_residuals(residuals: np.ndarray) -> tuple[float, float, float] | None:
    if residuals.size < 3 or not np.isfinite(residuals).all():
        return None
    x_process = residuals.cumsum()
    x_lag = x_process[:-1]
    x_next = x_process[1:]
    design = np.column_stack([np.ones_like(x_lag), x_lag])
    try:
        coeffs, _, _, _ = np.linalg.lstsq(design, x_next, rcond=None)
    except np.linalg.LinAlgError:
        return None

    a, b = float(coeffs[0]), float(coeffs[1])
    if not np.isfinite(a) or not np.isfinite(b) or b <= 0 or b >= 1:
        return None

    zeta = x_next - (a + b * x_lag)
    var_zeta = float(np.var(zeta, ddof=1))
    if not np.isfinite(var_zeta) or var_zeta <= 0:
        return None

    kappa = -np.log(b) * 252
    sigma_eq = np.sqrt(var_zeta / (1 - b**2))
    if not np.isfinite(kappa) or not np.isfinite(sigma_eq) or sigma_eq <= 0:
        return None

    mean_level = a / (1 - b)
    return kappa, mean_level, sigma_eq


def compute_pca_metrics(
    history_map: dict[str, PreparedHistory],
    tickers: list[str],
    lookback: int = PCA_WINDOW_DAYS,
    n_components: int = PCA_COMPONENTS,
) -> pd.DataFrame:
    returns = build_return_matrix(history_map, tickers)
    results: list[dict[str, Any]] = []
    if returns.empty:
        return pd.DataFrame(columns=["Date", "ticker", "pca_resid", "pca_resid_z", "pca_kappa", "pca_s_score"])

    all_dates = list(returns.index)
    for end_idx in range(lookback - 1, len(all_dates)):
        window = returns.iloc[end_idx - lookback + 1: end_idx + 1]
        valid_cols = window.columns[window.notna().all(axis=0)]
        if len(valid_cols) < 5:
            continue

        window_values = window.loc[:, valid_cols]
        sigma = window_values.std(ddof=1)
        valid_cols = sigma.index[sigma.gt(0) & sigma.notna()]
        if len(valid_cols) < 5:
            continue

        window_values = window_values.loc[:, valid_cols]
        sigma = sigma.loc[valid_cols]
        centered = window_values - window_values.mean(axis=0)
        standardized = centered.divide(sigma, axis=1)
        corr = standardized.corr().to_numpy(dtype=float)
        if corr.size == 0 or not np.isfinite(corr).all():
            continue

        eigvals, eigvecs = np.linalg.eigh(corr)
        order = np.argsort(eigvals)[::-1]
        eigvecs = eigvecs[:, order]
        component_count = min(n_components, len(valid_cols) - 1, lookback - 2)
        if component_count < 1:
            continue

        loadings = eigvecs[:, :component_count] / sigma.to_numpy(dtype=float)[:, None]
        factor_returns = window_values.to_numpy(dtype=float) @ loadings
        design = np.column_stack([np.ones(lookback), factor_returns])
        y = window_values.to_numpy(dtype=float)
        try:
            betas, _, _, _ = np.linalg.lstsq(design, y, rcond=None)
        except np.linalg.LinAlgError:
            continue
        fitted = design @ betas
        residuals = y - fitted
        resid_std = residuals.std(axis=0, ddof=1)
        current_resid = residuals[-1]

        raw_means: dict[str, float] = {}
        sigma_eqs: dict[str, float] = {}
        kappas: dict[str, float] = {}
        for col_idx, ticker in enumerate(valid_cols):
            ou = estimate_ou_from_residuals(residuals[:, col_idx])
            if ou is None:
                continue
            kappa, mean_level, sigma_eq = ou
            kappas[ticker] = kappa
            raw_means[ticker] = mean_level
            sigma_eqs[ticker] = sigma_eq

        if not raw_means:
            continue

        cross_sectional_mean = float(np.mean(list(raw_means.values())))
        current_date = all_dates[end_idx]
        for col_idx, ticker in enumerate(valid_cols):
            resid_value = float(current_resid[col_idx])
            resid_scale = float(resid_std[col_idx]) if np.isfinite(resid_std[col_idx]) and resid_std[col_idx] > 0 else np.nan
            row = {
                "Date": current_date,
                "ticker": ticker,
                "pca_resid": resid_value,
                "pca_resid_z": resid_value / resid_scale if np.isfinite(resid_scale) else np.nan,
                "pca_kappa": np.nan,
                "pca_s_score": np.nan,
            }
            if ticker in raw_means and ticker in sigma_eqs and sigma_eqs[ticker] > 0:
                centered_mean = raw_means[ticker] - cross_sectional_mean
                row["pca_kappa"] = kappas[ticker]
                row["pca_s_score"] = -centered_mean / sigma_eqs[ticker]
            results.append(row)

    return pd.DataFrame(results)


def attach_pca_metrics(history_map: dict[str, PreparedHistory], metrics: pd.DataFrame) -> None:
    if metrics.empty:
        for history in history_map.values():
            history.df["pca_resid"] = np.nan
            history.df["pca_resid_z"] = np.nan
            history.df["pca_kappa"] = np.nan
            history.df["pca_s_score"] = np.nan
        return

    for ticker, history in history_map.items():
        ticker_metrics = metrics.loc[metrics["ticker"].eq(ticker), ["Date", "pca_resid", "pca_resid_z", "pca_kappa", "pca_s_score"]]
        if ticker_metrics.empty:
            history.df["pca_resid"] = np.nan
            history.df["pca_resid_z"] = np.nan
            history.df["pca_kappa"] = np.nan
            history.df["pca_s_score"] = np.nan
            continue
        history.df = history.df.merge(ticker_metrics, on="Date", how="left")
        history.date_to_idx = {date: idx for idx, date in enumerate(history.df["Date"])}
        history.max_drop = history.df["Max Drop"].to_numpy(dtype=float)
        history.signal_success = history.df["Signal Success"].fillna(False).to_numpy(dtype=bool)
        history.valid_signal = history.df["Valid Signal"].fillna(False).to_numpy(dtype=bool)


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


def compute_match_stats(
    history: PreparedHistory,
    idx: int,
    lookback_days: int,
    signal_values: np.ndarray,
    match_rule: Callable[[np.ndarray, float, PreparedHistory, int, np.ndarray], np.ndarray],
    weighted: bool = False,
) -> tuple[float, int]:
    current_signal = signal_values[idx]
    if not np.isfinite(current_signal) or current_signal <= 0:
        return np.nan, 0

    start_idx = max(1, idx - lookback_days)
    end_idx = idx - FORWARD_DAYS
    if end_idx <= start_idx:
        return np.nan, 0

    hist_slice = slice(start_idx, end_idx)
    hist_signal = signal_values[hist_slice]
    hist_valid = history.valid_signal[hist_slice]
    hist_success = history.signal_success[hist_slice]
    base_mask = hist_valid & np.isfinite(hist_signal)
    mask = match_rule(hist_signal, current_signal, history, idx, base_mask)
    matched_signals = int(mask.sum())
    if matched_signals == 0:
        return np.nan, 0

    if not weighted:
        return float(hist_success[mask].mean() * 100), matched_signals

    hist_indices = np.arange(start_idx, end_idx, dtype=float)
    ages = idx - hist_indices
    weights = np.exp(-np.log(2.0) * ages / RECENT_WEIGHT_HALF_LIFE)
    selected_weights = weights[mask]
    if not np.isfinite(selected_weights).all() or selected_weights.sum() <= 0:
        return np.nan, 0
    weighted_success = np.average(hist_success[mask].astype(float), weights=selected_weights)
    return float(weighted_success * 100), matched_signals


def baseline_match_rule(
    hist_signal: np.ndarray,
    current_signal: float,
    history: PreparedHistory,
    idx: int,
    base_mask: np.ndarray,
) -> np.ndarray:
    return base_mask & (hist_signal >= current_signal)


def pca_match_rule(
    hist_signal: np.ndarray,
    current_signal: float,
    history: PreparedHistory,
    idx: int,
    base_mask: np.ndarray,
) -> np.ndarray:
    current_resid_z = float(history.df.iloc[idx]["pca_resid_z"])
    if not np.isfinite(current_resid_z) or current_resid_z >= 0:
        return np.zeros_like(base_mask, dtype=bool)

    start_idx = max(1, idx - BASE_LOOKBACK_DAYS)
    end_idx = idx - FORWARD_DAYS
    hist_resid = history.df["pca_resid_z"].to_numpy(dtype=float)[start_idx:end_idx]
    return base_mask & (hist_signal >= current_signal) & np.isfinite(hist_resid) & (hist_resid <= current_resid_z)


def build_candidate(
    history: PreparedHistory,
    idx: int,
    success_rate: float,
    matched_signals: int,
    extra_fields: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    if np.isnan(success_rate) or success_rate < SUCCESS_RATE_GATE or matched_signals < MIN_MATCHED_SIGNALS:
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

    candidate: dict[str, Any] = {
        "ticker": history.ticker,
        "success_rate": float(success_rate),
        "matched_signals": int(matched_signals),
        "spot_close": spot_close,
        "entry_option_price": limit_buy,
    }
    if extra_fields:
        candidate.update(extra_fields)
    return candidate


def evaluate_baseline(history: PreparedHistory, idx: int) -> dict[str, Any] | None:
    success_rate, matched_signals = compute_match_stats(
        history=history,
        idx=idx,
        lookback_days=BASE_LOOKBACK_DAYS,
        signal_values=history.df["Max Drop"].to_numpy(dtype=float),
        match_rule=baseline_match_rule,
    )
    return build_candidate(history, idx, success_rate, matched_signals)


def evaluate_volume(history: PreparedHistory, idx: int) -> dict[str, Any] | None:
    signal_values = history.df["Volume Adjusted Drop"].to_numpy(dtype=float)
    success_rate, matched_signals = compute_match_stats(
        history=history,
        idx=idx,
        lookback_days=BASE_LOOKBACK_DAYS,
        signal_values=signal_values,
        match_rule=baseline_match_rule,
    )
    return build_candidate(history, idx, success_rate, matched_signals)


def evaluate_pca(history: PreparedHistory, idx: int) -> dict[str, Any] | None:
    success_rate, matched_signals = compute_match_stats(
        history=history,
        idx=idx,
        lookback_days=BASE_LOOKBACK_DAYS,
        signal_values=history.df["Max Drop"].to_numpy(dtype=float),
        match_rule=pca_match_rule,
    )
    row = history.df.iloc[idx]
    extra = {"pca_resid_z": float(row["pca_resid_z"])} if np.isfinite(row["pca_resid_z"]) else None
    return build_candidate(history, idx, success_rate, matched_signals, extra)


def evaluate_kappa(history: PreparedHistory, idx: int) -> dict[str, Any] | None:
    row = history.df.iloc[idx]
    kappa = float(row["pca_kappa"])
    s_score = float(row["pca_s_score"])
    if not np.isfinite(kappa) or not np.isfinite(s_score):
        return None
    if kappa <= FAST_KAPPA_THRESHOLD or s_score >= SCORE_OPEN_LONG:
        return None

    success_rate, matched_signals = compute_match_stats(
        history=history,
        idx=idx,
        lookback_days=BASE_LOOKBACK_DAYS,
        signal_values=history.df["Max Drop"].to_numpy(dtype=float),
        match_rule=baseline_match_rule,
    )
    extra = {"pca_kappa": kappa, "pca_s_score": s_score}
    return build_candidate(history, idx, success_rate, matched_signals, extra)


def make_window_evaluator(lookback_days: int, weighted: bool = False) -> Callable[[PreparedHistory, int], dict[str, Any] | None]:
    def evaluator(history: PreparedHistory, idx: int) -> dict[str, Any] | None:
        success_rate, matched_signals = compute_match_stats(
            history=history,
            idx=idx,
            lookback_days=lookback_days,
            signal_values=history.df["Max Drop"].to_numpy(dtype=float),
            match_rule=baseline_match_rule,
            weighted=weighted,
        )
        return build_candidate(history, idx, success_rate, matched_signals)

    return evaluator


def build_equity_curve(
    history_map: dict[str, PreparedHistory],
    variant: VariantConfig,
) -> tuple[pd.DataFrame, pd.DataFrame]:
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
                    "variant": variant.key,
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
            candidates = []
            for ticker, history in history_map.items():
                if ticker in open_tickers or ticker == QQQ_PROXY:
                    continue
                idx = history.date_to_idx.get(current_date)
                if idx is None or idx <= BASE_LOOKBACK_DAYS or idx + FORWARD_DAYS >= len(history.df):
                    continue
                candidate = variant.evaluate_candidate(history, idx)
                if candidate is not None:
                    candidates.append(candidate)

            if candidates:
                candidate = max(candidates, key=variant.rank_key)
                entry_cost = candidate["entry_option_price"] * 100
                current_equity = cash + marked_position_value
                budget = min(cash, current_equity * TARGET_POSITION_WEIGHT)
                contracts = int(budget // entry_cost)
                if contracts > 0:
                    spent = contracts * entry_cost
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
                            allocated_cash=float(spent),
                            planned_tp_day1=float(candidate["entry_option_price"]) * (1 + DAY1_TAKE_PROFIT_PCT),
                            planned_tp_day2=float(candidate["entry_option_price"]) * (1 + DAY2_TAKE_PROFIT_PCT),
                            planned_stop=float(candidate["entry_option_price"]) * (1 - STOP_LOSS_PCT),
                        )
                    )
                    marked_position_value += spent

        equity_rows.append(
            {
                "variant": variant.key,
                "date": current_date,
                "cash": cash,
                "position_value": marked_position_value,
                "equity": cash + marked_position_value,
                "open_tickers": ",".join(sorted(position.ticker for position in positions)),
                "open_count": len(positions),
            }
        )

    return pd.DataFrame(equity_rows), pd.DataFrame(trade_rows)


def summarize_backtest(
    variant: VariantConfig,
    history_cache: dict[str, PreparedHistory],
) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, Any]]:
    subset = {ticker: history for ticker, history in history_cache.items() if ticker != QQQ_PROXY}
    equity_df, trades_df = build_equity_curve(subset, variant)

    final_equity = float(equity_df["equity"].iloc[-1])
    total_return = (final_equity / INITIAL_CAPITAL - 1) * 100
    max_drawdown = ((equity_df["equity"] / equity_df["equity"].cummax()) - 1).min() * 100
    win_rate = float((trades_df["pnl"] > 0).mean() * 100) if not trades_df.empty else 0.0
    sharpe_rf_10y_tbill = compute_annualized_sharpe(equity_df)

    summary = {
        "variant": variant.key,
        "label": variant.label,
        "final_equity": final_equity,
        "total_return_pct": total_return,
        "max_drawdown_pct": max_drawdown,
        "trade_count": len(trades_df),
        "win_rate_pct": win_rate,
        "sharpe_rf_10y_tbill": sharpe_rf_10y_tbill,
        "risk_free_rate_annual": TEN_YEAR_TBILL_RATE,
        "risk_free_rate_source_date": TEN_YEAR_TBILL_DATE,
    }
    return equity_df, trades_df, summary


def build_variants() -> list[VariantConfig]:
    return [
        VariantConfig(
            key="baseline_original",
            label="Original 2.3.3",
            color="#111111",
            linestyle="-",
            evaluate_candidate=evaluate_baseline,
            rank_key=lambda item: (item["success_rate"], item["matched_signals"]),
        ),
        VariantConfig(
            key="volume_adjusted",
            label="Add Volume",
            color="#d95f02",
            linestyle="-",
            evaluate_candidate=evaluate_volume,
            rank_key=lambda item: (item["success_rate"], item["matched_signals"]),
        ),
        VariantConfig(
            key="pca_defactored",
            label="PCA Defactored",
            color="#1b9e77",
            linestyle="-",
            evaluate_candidate=evaluate_pca,
            rank_key=lambda item: (item["success_rate"], item["matched_signals"], -abs(item.get("pca_resid_z", 0.0))),
        ),
        VariantConfig(
            key="kappa_signal",
            label="Kappa / s-score",
            color="#7570b3",
            linestyle="-",
            evaluate_candidate=evaluate_kappa,
            rank_key=lambda item: (-item.get("pca_s_score", 0.0), item["success_rate"], item["matched_signals"]),
        ),
        VariantConfig(
            key="window_60d",
            label="Window 60d",
            color="#e7298a",
            linestyle="--",
            evaluate_candidate=make_window_evaluator(60),
            rank_key=lambda item: (item["success_rate"], item["matched_signals"]),
        ),
        VariantConfig(
            key="window_126d",
            label="Window 126d",
            color="#66a61e",
            linestyle="--",
            evaluate_candidate=make_window_evaluator(126),
            rank_key=lambda item: (item["success_rate"], item["matched_signals"]),
        ),
        VariantConfig(
            key="window_252d_recent_weighted",
            label="Window 252d + Recent Weight",
            color="#e6ab02",
            linestyle="--",
            evaluate_candidate=make_window_evaluator(252, weighted=True),
            rank_key=lambda item: (item["success_rate"], item["matched_signals"]),
        ),
    ]


def plot_variant_curves(curves_df: pd.DataFrame, variants: list[VariantConfig]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    date_series = pd.to_datetime(curves_df["date"], errors="coerce")
    valid_dates = date_series[date_series.notna()]
    if not valid_dates.empty:
        date_label = f"{valid_dates.min():%Y-%m-%d} to {valid_dates.max():%Y-%m-%d}"
    else:
        date_label = "date unavailable"
    fig, ax = plt.subplots(figsize=(14, 8), facecolor=FIG_BG)
    for variant in variants:
        subset = curves_df.loc[curves_df["variant"].eq(variant.key)].copy()
        if subset.empty:
            continue
        ax.plot(
            subset["date"],
            subset["equity"],
            label=variant.label,
            color=variant.color,
            linestyle=variant.linestyle,
            linewidth=2.0,
        )
    ax.axhline(INITIAL_CAPITAL, color=BASELINE, linestyle=":", alpha=0.6, linewidth=1.2)
    style_dark_axis(ax)
    ax.set_title(
        "Reversal Article Variants Equity Curve Comparison\n"
        f"Backtest window: {date_label}"
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value ($)")
    legend = ax.legend(frameon=False)
    for text in legend.get_texts():
        text.set_color(TEXT)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=180, bbox_inches="tight", facecolor=FIG_BG)
    plt.close(fig)


def main() -> None:
    tickers = build_universe()
    end_date = pd.Timestamp.today().normalize() + pd.Timedelta(days=1)
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=BACKTEST_YEARS)).normalize()
    data_start = trade_start - pd.DateOffset(days=500)

    history_cache = load_history_cache(sorted(set(tickers)), data_start.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
    pca_metrics = compute_pca_metrics(history_cache, [ticker for ticker in tickers if ticker in history_cache])
    attach_pca_metrics(history_cache, pca_metrics)

    variants = build_variants()
    all_curves: list[pd.DataFrame] = []
    all_trades: list[pd.DataFrame] = []
    summaries: list[dict[str, Any]] = []

    for variant in variants:
        equity_df, trades_df, summary = summarize_backtest(variant, history_cache)
        equity_out = OUTPUT_DIR / f"{variant.key}_equity.csv"
        trades_out = OUTPUT_DIR / f"{variant.key}_trades.csv"
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        equity_df.to_csv(equity_out, index=False)
        trades_df.to_csv(trades_out, index=False)
        all_curves.append(equity_df)
        all_trades.append(trades_df)
        summaries.append(summary)
        print(
            f"{variant.key}: return={summary['total_return_pct']:.2f}% "
            f"max_dd={summary['max_drawdown_pct']:.2f}% "
            f"win_rate={summary['win_rate_pct']:.2f}% "
            f"trades={summary['trade_count']} "
            f"sharpe={summary['sharpe_rf_10y_tbill']:.2f}"
        )

    summary_df = pd.DataFrame(summaries).sort_values("total_return_pct", ascending=False).reset_index(drop=True)
    curves_df = pd.concat(all_curves, ignore_index=True)
    trades_df = pd.concat(all_trades, ignore_index=True) if all_trades else pd.DataFrame()

    summary_df.to_csv(SUMMARY_PATH, index=False)
    curves_df.to_csv(CURVES_PATH, index=False)
    trades_df.to_csv(OUTPUT_DIR / "reversal_article_variants_trades.csv", index=False)
    plot_variant_curves(curves_df, variants)

    print(f"Saved summary -> {SUMMARY_PATH}")
    print(f"Saved curves -> {CURVES_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")


if __name__ == "__main__":
    main()
