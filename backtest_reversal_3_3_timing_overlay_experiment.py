from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from backtest_metrics import TEN_YEAR_TBILL_DATE, TEN_YEAR_TBILL_RATE, compute_annualized_sharpe
from backtest_reversal_3_1_calls import (
    DAY1_TAKE_PROFIT_PCT,
    DAY2_TAKE_PROFIT_PCT,
    FORWARD_DAYS,
    INITIAL_CAPITAL,
    LOOKBACK_DAYS,
    MAX_OPEN_POSITIONS,
    OFFICIAL_UNIVERSE_NAME,
    RISK_FREE,
    STOP_LOSS_PCT,
    TARGET_POSITION_WEIGHT,
    TRADING_DTE_AT_ENTRY,
    PreparedHistory,
    build_universe_presets,
    evaluate_candidate,
    load_history_cache,
    mark_option_price,
)
from plot_theme import AX_BG, BASELINE, FIG_BG, GREEN_LINE, RED_LINE, TEXT, style_dark_axis, style_date_axis


RESEARCH_YEARS = 3
TIMING_WINDOWS = (3, 5, 7, 10)
PROB_THRESHOLDS = (0.50, 0.55, 0.60, 0.65)
MIN_TRAIN_SIGNALS = 250
MIN_CLASS_COUNT = 40
MAX_TOP_VARIANTS = 4

OUTPUT_DIR = Path.cwd() / "results" / "reversal_3_3_timing_overlay_experiment"
SUMMARY_PATH = OUTPUT_DIR / "reversal_3_3_timing_overlay_summary.csv"
OOS_SCORE_PATH = OUTPUT_DIR / "reversal_3_3_timing_overlay_oos_scores.csv"
CANDIDATE_PATH = OUTPUT_DIR / "reversal_3_3_timing_overlay_candidates.csv"
SELECTION_PATH = OUTPUT_DIR / "reversal_3_3_timing_overlay_selected_variants.csv"
PLOT_PATH = Path.cwd() / "assets" / "reversal_3_3_timing_overlay_experiment.png"
HEATMAP_PATH = Path.cwd() / "assets" / "reversal_3_3_timing_overlay_heatmap.png"

COMMON_FEATURES = [
    "success_rate",
    "matched_signals",
    "current_drop_pct",
    "rolling_sigma_20d_pct",
]


@dataclass
class SignalOutcome:
    exit_date: pd.Timestamp
    exit_reason: str
    exit_option_price: float
    return_pct: float
    pnl_per_contract: float


@dataclass
class BacktestPosition:
    ticker: str
    entry_date: pd.Timestamp
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


def _safe_div(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    out = numerator / denominator.replace(0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def _rolling_mean_abs_deviation(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window).apply(lambda x: np.mean(np.abs(x - np.mean(x))), raw=True)


def add_timing_indicators(df: pd.DataFrame, windows: tuple[int, ...]) -> pd.DataFrame:
    out = df.copy()
    close = pd.to_numeric(out["Close"], errors="coerce")
    high = pd.to_numeric(out["High"], errors="coerce")
    low = pd.to_numeric(out["Low"], errors="coerce")
    prev_close = close.shift(1)
    typical = (high + low + close) / 3.0
    true_range = pd.concat(
        [
            (high - low),
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    delta = close.diff()
    gains = delta.clip(lower=0.0)
    losses = (-delta).clip(lower=0.0)
    dm_plus = gains
    dm_minus = losses

    for window in windows:
        sma = close.rolling(window).mean()
        ema = close.ewm(span=window, adjust=False, min_periods=window).mean()
        atr = true_range.ewm(span=window, adjust=False, min_periods=window).mean()

        di_plus = 100.0 * _safe_div(dm_plus.ewm(span=window, adjust=False, min_periods=window).mean(), atr)
        di_minus = 100.0 * _safe_div(dm_minus.ewm(span=window, adjust=False, min_periods=window).mean(), atr)
        admi = 100.0 * _safe_div((di_plus - di_minus).abs(), (di_plus + di_minus))

        tp_sma = typical.rolling(window).mean()
        mean_dev = _rolling_mean_abs_deviation(typical, window)
        cci = _safe_div(typical - tp_sma, 0.015 * mean_dev)

        roc = close / close.shift(window) - 1.0

        avg_gain = gains.ewm(alpha=1 / window, adjust=False, min_periods=window).mean()
        avg_loss = losses.ewm(alpha=1 / window, adjust=False, min_periods=window).mean()
        rs = _safe_div(avg_gain, avg_loss)
        rsi = 100.0 - 100.0 / (1.0 + rs)

        hh = high.rolling(window).max()
        ll = low.rolling(window).min()
        range_span = (hh - ll).replace(0, np.nan)
        willr = -100.0 * _safe_div(hh - close, range_span)
        stoch_k = 100.0 * _safe_div(close - ll, range_span)
        stoch_d = stoch_k.ewm(span=3, adjust=False, min_periods=3).mean()
        close_location = _safe_div(close - ll, range_span)

        out[f"sma_gap_{window}"] = close / sma - 1.0
        out[f"ema_gap_{window}"] = close / ema - 1.0
        out[f"atr_pct_{window}"] = _safe_div(atr, close)
        out[f"admi_{window}"] = admi
        out[f"cci_{window}"] = cci
        out[f"roc_{window}"] = roc
        out[f"rsi_{window}"] = rsi
        out[f"willr_{window}"] = willr
        out[f"stoch_k_{window}"] = stoch_k
        out[f"stoch_d_{window}"] = stoch_d
        out[f"close_location_{window}"] = close_location

    return out


def timing_feature_columns(window: int) -> list[str]:
    return COMMON_FEATURES + [
        f"sma_gap_{window}",
        f"ema_gap_{window}",
        f"atr_pct_{window}",
        f"admi_{window}",
        f"cci_{window}",
        f"roc_{window}",
        f"rsi_{window}",
        f"willr_{window}",
        f"stoch_k_{window}",
        f"stoch_d_{window}",
        f"close_location_{window}",
    ]


def simulate_signal_outcome(history: PreparedHistory, idx: int, candidate: dict[str, Any]) -> SignalOutcome:
    entry_date = pd.Timestamp(history.df.iloc[idx]["Date"])
    strike = float(candidate["spot_close"])
    entry_price = float(candidate["entry_option_price"])
    stop_price = entry_price * (1 - STOP_LOSS_PCT)
    tp_day1 = entry_price * (1 + DAY1_TAKE_PROFIT_PCT)
    tp_day2 = entry_price * (1 + DAY2_TAKE_PROFIT_PCT)

    for step in (1, 2):
        future_idx = idx + step
        row = history.df.iloc[future_idx]
        current_date = pd.Timestamp(row["Date"])
        sigma_ann = float(row["Sigma Ann"])
        if np.isnan(sigma_ann) or sigma_ann <= 0:
            sigma_ann = 0.60

        option_high = mark_option_price(float(row["High"]), strike, entry_date, current_date, sigma_ann)
        option_low = mark_option_price(float(row["Low"]), strike, entry_date, current_date, sigma_ann)
        option_close = mark_option_price(float(row["Close"]), strike, entry_date, current_date, sigma_ann)

        if option_low <= stop_price:
            exit_price = stop_price
            exit_reason = "stop"
        else:
            target = tp_day1 if step == 1 else tp_day2
            if option_high >= target:
                exit_price = target
                exit_reason = "tp_day1" if step == 1 else "tp_day2"
            elif step >= 2:
                exit_price = option_close
                exit_reason = "time_exit"
            else:
                continue

        pnl_per_contract = (exit_price - entry_price) * 100.0
        return SignalOutcome(
            exit_date=current_date,
            exit_reason=exit_reason,
            exit_option_price=float(exit_price),
            return_pct=float((exit_price / entry_price - 1.0) * 100.0),
            pnl_per_contract=float(pnl_per_contract),
        )

    raise RuntimeError("Signal outcome simulation did not exit within two business days.")


def build_candidate_dataset(history_map: dict[str, PreparedHistory], trade_start: pd.Timestamp) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for history in history_map.values():
        history.df = add_timing_indicators(history.df, TIMING_WINDOWS)
        for idx, current_date in enumerate(history.df["Date"]):
            if current_date < trade_start or idx <= LOOKBACK_DAYS or idx + FORWARD_DAYS >= len(history.df):
                continue

            candidate = evaluate_candidate(history, idx)
            if candidate is None:
                continue

            outcome = simulate_signal_outcome(history, idx, candidate)
            row = history.df.iloc[idx]
            event: dict[str, Any] = {
                "date": pd.Timestamp(current_date),
                "ticker": history.ticker,
                "success_rate": float(candidate["success_rate"]),
                "matched_signals": int(candidate["matched_signals"]),
                "spot_close": float(candidate["spot_close"]),
                "entry_option_price": float(candidate["entry_option_price"]),
                "current_drop_pct": float(history.max_drop[idx]),
                "rolling_sigma_20d_pct": float(row["Sigma Ann"]) * 100 if pd.notna(row["Sigma Ann"]) else np.nan,
                "sigma_ann": float(row["Sigma Ann"]) if pd.notna(row["Sigma Ann"]) else np.nan,
                "signal_positive": int(outcome.return_pct > 0),
                "signal_return_pct": float(outcome.return_pct),
                "signal_pnl_per_contract": float(outcome.pnl_per_contract),
                "signal_exit_date": outcome.exit_date,
                "signal_exit_reason": outcome.exit_reason,
                "signal_exit_option_price": outcome.exit_option_price,
            }
            for window in TIMING_WINDOWS:
                for feature in timing_feature_columns(window):
                    if feature in event:
                        continue
                    event[feature] = float(row.get(feature, np.nan)) if pd.notna(row.get(feature, np.nan)) else np.nan
            rows.append(event)

    candidate_df = pd.DataFrame(rows)
    if candidate_df.empty:
        return candidate_df

    return candidate_df.sort_values(["date", "success_rate", "matched_signals", "ticker"], ascending=[True, False, False, True]).reset_index(drop=True)


def compute_walk_forward_scores(candidate_df: pd.DataFrame, window: int) -> pd.Series:
    features = timing_feature_columns(window)
    scores = pd.Series(np.nan, index=candidate_df.index, dtype=float)
    unique_dates = list(pd.Series(candidate_df["date"].drop_duplicates()).sort_values())

    pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("logit", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )

    for current_date in unique_dates:
        train_mask = candidate_df["date"] < current_date
        test_mask = candidate_df["date"] == current_date
        train_df = candidate_df.loc[train_mask]
        if len(train_df) < MIN_TRAIN_SIGNALS:
            continue
        positive_count = int(train_df["signal_positive"].sum())
        negative_count = int((1 - train_df["signal_positive"]).sum())
        if positive_count < MIN_CLASS_COUNT or negative_count < MIN_CLASS_COUNT:
            continue

        x_train = train_df[features]
        y_train = train_df["signal_positive"].astype(int)
        x_test = candidate_df.loc[test_mask, features]
        if x_test.empty:
            continue

        pipeline.fit(x_train, y_train)
        scores.loc[test_mask] = pipeline.predict_proba(x_test)[:, 1]

    return scores


def fit_timing_model_asof(
    candidate_df: pd.DataFrame,
    window: int,
    asof_date: pd.Timestamp,
) -> Pipeline | None:
    features = timing_feature_columns(window)
    train_df = candidate_df.loc[candidate_df["date"] < pd.Timestamp(asof_date)].copy()
    if len(train_df) < MIN_TRAIN_SIGNALS:
        return None

    positive_count = int(train_df["signal_positive"].sum())
    negative_count = int((1 - train_df["signal_positive"]).sum())
    if positive_count < MIN_CLASS_COUNT or negative_count < MIN_CLASS_COUNT:
        return None

    pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
            ("logit", LogisticRegression(max_iter=1000, class_weight="balanced")),
        ]
    )
    pipeline.fit(train_df[features], train_df["signal_positive"].astype(int))
    return pipeline


def score_live_feature_row(feature_row: dict[str, Any], model: Pipeline | None, window: int) -> float:
    if model is None:
        return np.nan
    features = timing_feature_columns(window)
    row_df = pd.DataFrame([{feature: feature_row.get(feature, np.nan) for feature in features}])
    return float(model.predict_proba(row_df)[:, 1][0])


def event_key(date_value: pd.Timestamp, ticker: str) -> tuple[pd.Timestamp, str]:
    return pd.Timestamp(date_value).normalize(), str(ticker)


def score_map_for_variant(candidate_df: pd.DataFrame, score_column: str) -> dict[tuple[pd.Timestamp, str], float]:
    valid = candidate_df[["date", "ticker", score_column]].dropna()
    return {
        event_key(row.date, row.ticker): float(getattr(row, score_column))
        for row in valid.itertuples(index=False)
    }


def build_equity_curve_with_overlay(
    history_map: dict[str, PreparedHistory],
    candidate_df: pd.DataFrame,
    score_column: str | None = None,
    threshold: float | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    trade_start = pd.Timestamp(candidate_df["date"].min()).normalize()
    all_dates = sorted(
        {
            date
            for history in history_map.values()
            for date in history.df["Date"]
            if date >= trade_start
        }
    )
    score_map = score_map_for_variant(candidate_df, score_column) if score_column else {}

    cash = INITIAL_CAPITAL
    positions: list[BacktestPosition] = []
    trade_rows: list[dict[str, Any]] = []
    equity_rows: list[dict[str, Any]] = []

    candidates_by_date = {
        pd.Timestamp(date).normalize(): group.sort_values(
            ["success_rate", "matched_signals", "current_drop_pct", "ticker"],
            ascending=[False, False, False, True],
        )
        for date, group in candidate_df.groupby("date")
    }

    for current_date in all_dates:
        updated_positions: list[BacktestPosition] = []
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
                    "ticker": position.ticker,
                    "entry_date": position.entry_date,
                    "exit_date": current_date,
                    "success_rate": position.success_rate,
                    "matched_signals": position.matched_signals,
                    "allocated_cash": position.allocated_cash,
                    "contracts": position.contracts,
                    "entry_option_price": position.entry_option_price,
                    "exit_option_price": exit_price,
                    "pnl": pnl,
                    "return_pct": pnl / (position.entry_option_price * 100 * position.contracts) * 100,
                    "exit_reason": exit_reason,
                    "score_column": score_column or "baseline",
                    "score_threshold": threshold,
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
            day_candidates = candidates_by_date.get(pd.Timestamp(current_date).normalize(), pd.DataFrame())
            if not day_candidates.empty:
                remaining = day_candidates[~day_candidates["ticker"].isin(open_tickers)]
                if not remaining.empty:
                    candidate = remaining.iloc[0]
                    if score_column is not None and threshold is not None:
                        score = score_map.get(event_key(candidate["date"], candidate["ticker"]), np.nan)
                        if not np.isfinite(score) or float(score) < threshold:
                            equity_rows.append(
                                {
                                    "date": current_date,
                                    "cash": cash,
                                    "position_value": marked_position_value,
                                    "equity": cash + marked_position_value,
                                    "open_tickers": ",".join(sorted(position.ticker for position in positions)),
                                    "open_count": len(positions),
                                    "entry_action": "skip",
                                    "entry_ticker": candidate["ticker"],
                                    "entry_score": score,
                                }
                            )
                            continue

                    entry_cost = float(candidate["entry_option_price"]) * 100.0
                    current_equity = cash + marked_position_value
                    budget = min(cash, current_equity * TARGET_POSITION_WEIGHT)
                    contracts = int(budget // entry_cost)
                    if contracts > 0:
                        spent = contracts * entry_cost
                        cash -= spent
                        positions.append(
                            BacktestPosition(
                                ticker=str(candidate["ticker"]),
                                entry_date=current_date,
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
                "date": current_date,
                "cash": cash,
                "position_value": marked_position_value,
                "equity": cash + marked_position_value,
                "open_tickers": ",".join(sorted(position.ticker for position in positions)),
                "open_count": len(positions),
                "entry_action": "enter_or_hold",
                "entry_ticker": None,
                "entry_score": np.nan,
            }
        )

    return pd.DataFrame(equity_rows), pd.DataFrame(trade_rows)


def summarize_variant(label: str, equity_df: pd.DataFrame, trades_df: pd.DataFrame, candidate_df: pd.DataFrame) -> dict[str, Any]:
    final_equity = float(equity_df["equity"].iloc[-1])
    total_return = (final_equity / INITIAL_CAPITAL - 1.0) * 100.0
    drawdown = ((equity_df["equity"] / equity_df["equity"].cummax()) - 1.0)
    max_drawdown = float(drawdown.min() * 100.0) if not drawdown.empty else 0.0
    win_rate = float((trades_df["pnl"] > 0).mean() * 100.0) if not trades_df.empty else 0.0
    trade_count = int(len(trades_df))
    candidate_days = int(candidate_df["date"].nunique())
    trade_days = int(trades_df["entry_date"].nunique()) if not trades_df.empty else 0
    return {
        "variant": label,
        "final_equity": final_equity,
        "total_return_pct": total_return,
        "max_drawdown_pct": max_drawdown,
        "trade_count": trade_count,
        "trade_days": trade_days,
        "candidate_days": candidate_days,
        "take_rate_pct": (trade_days / candidate_days * 100.0) if candidate_days else 0.0,
        "win_rate_pct": win_rate,
        "avg_return_pct_per_trade": float(trades_df["return_pct"].mean()) if not trades_df.empty else 0.0,
        "median_return_pct_per_trade": float(trades_df["return_pct"].median()) if not trades_df.empty else 0.0,
        "sharpe_rf_10y_tbill": compute_annualized_sharpe(equity_df),
        "risk_free_rate_annual": TEN_YEAR_TBILL_RATE,
        "risk_free_rate_source_date": TEN_YEAR_TBILL_DATE,
    }


def plot_variant_equity_curves(variant_curves: dict[str, pd.DataFrame], summary_df: pd.DataFrame) -> None:
    PLOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(12, 7), facecolor=FIG_BG)

    color_cycle = [GREEN_LINE, "#60a5fa", "#f59e0b", "#f472b6", "#a78bfa"]
    for idx, (label, equity_df) in enumerate(variant_curves.items()):
        color = color_cycle[idx % len(color_cycle)]
        ax.plot(equity_df["date"], equity_df["equity"], linewidth=2.2, label=label, color=color)

    ax.axhline(INITIAL_CAPITAL, color=BASELINE, linestyle="--", alpha=0.55, label="Initial Capital")
    style_dark_axis(ax)
    valid_dates = pd.to_datetime(next(iter(variant_curves.values()))["date"], errors="coerce").dropna()
    span_days = int((valid_dates.max() - valid_dates.min()).days) if not valid_dates.empty else None
    style_date_axis(ax, span_days=span_days)
    ax.set_title("Timing Overlay Experiment Equity Curves")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio Value ($)")
    legend = ax.legend(frameon=False, loc="upper left")
    for text in legend.get_texts():
        text.set_color(TEXT)
    fig.tight_layout()
    fig.savefig(PLOT_PATH, dpi=160, bbox_inches="tight", facecolor=FIG_BG)
    plt.close(fig)


def plot_threshold_heatmap(summary_df: pd.DataFrame) -> None:
    HEATMAP_PATH.parent.mkdir(parents=True, exist_ok=True)
    overlay_df = summary_df[summary_df["window"].notna()].copy()
    if overlay_df.empty:
        return

    pivot = overlay_df.pivot(index="window", columns="threshold", values="sharpe_rf_10y_tbill").sort_index()
    returns = overlay_df.pivot(index="window", columns="threshold", values="total_return_pct").sort_index()
    drawdowns = overlay_df.pivot(index="window", columns="threshold", values="max_drawdown_pct").sort_index()

    fig, ax = plt.subplots(figsize=(10, 6), facecolor=FIG_BG)
    im = ax.imshow(pivot.values, cmap="viridis", aspect="auto")
    ax.set_xticks(np.arange(len(pivot.columns)))
    ax.set_xticklabels([f"{col:.2f}" for col in pivot.columns], color=TEXT)
    ax.set_yticks(np.arange(len(pivot.index)))
    ax.set_yticklabels([f"{int(idx)}d" for idx in pivot.index], color=TEXT)
    ax.set_xlabel("Timing probability threshold")
    ax.set_ylabel("Indicator window")
    ax.set_title("Timing Overlay Sharpe Heatmap\ntext = return % / max DD %")
    style_dark_axis(ax)

    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            sharpe = pivot.iloc[i, j]
            ret = returns.iloc[i, j]
            dd = drawdowns.iloc[i, j]
            ax.text(
                j,
                i,
                f"{ret:+.0f}%\n{dd:.0f}%",
                ha="center",
                va="center",
                fontsize=8,
                color="white",
            )

    cbar = fig.colorbar(im, ax=ax)
    cbar.ax.yaxis.set_tick_params(color=TEXT)
    plt.setp(cbar.ax.get_yticklabels(), color=TEXT)
    fig.tight_layout()
    fig.savefig(HEATMAP_PATH, dpi=160, bbox_inches="tight", facecolor=FIG_BG)
    plt.close(fig)


def main() -> None:
    presets = build_universe_presets()
    tickers = presets[OFFICIAL_UNIVERSE_NAME]
    end_date = pd.Timestamp.today().normalize() + pd.Timedelta(days=1)
    trade_start = (pd.Timestamp.today().normalize() - pd.DateOffset(years=RESEARCH_YEARS)).normalize()
    data_start = trade_start - pd.DateOffset(days=500)

    history_map = load_history_cache(sorted(set(tickers)), data_start.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
    candidate_df = build_candidate_dataset(history_map, trade_start)
    if candidate_df.empty:
        raise RuntimeError("No candidate events were generated for the timing overlay experiment.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    candidate_df.to_csv(CANDIDATE_PATH, index=False)

    for window in TIMING_WINDOWS:
        candidate_df[f"score_w{window}"] = compute_walk_forward_scores(candidate_df, window)

    candidate_df.to_csv(OOS_SCORE_PATH, index=False)

    summaries: list[dict[str, Any]] = []
    variant_curves: dict[str, pd.DataFrame] = {}

    baseline_equity, baseline_trades = build_equity_curve_with_overlay(history_map, candidate_df)
    baseline_summary = summarize_variant("baseline_option_only", baseline_equity, baseline_trades, candidate_df)
    baseline_summary["window"] = np.nan
    baseline_summary["threshold"] = np.nan
    summaries.append(baseline_summary)
    variant_curves["Baseline"] = baseline_equity

    for window in TIMING_WINDOWS:
        score_column = f"score_w{window}"
        for threshold in PROB_THRESHOLDS:
            label = f"timing_w{window}_p{int(round(threshold * 100))}"
            equity_df, trades_df = build_equity_curve_with_overlay(
                history_map,
                candidate_df,
                score_column=score_column,
                threshold=threshold,
            )
            summary = summarize_variant(label, equity_df, trades_df, candidate_df)
            summary["window"] = window
            summary["threshold"] = threshold
            summaries.append(summary)

    summary_df = pd.DataFrame(summaries).sort_values(
        ["window", "threshold", "sharpe_rf_10y_tbill"],
        ascending=[True, True, False],
        na_position="first",
    ).reset_index(drop=True)
    summary_df.to_csv(SUMMARY_PATH, index=False)

    overlay_only = summary_df[summary_df["window"].notna()].copy()
    improved = overlay_only[
        (overlay_only["sharpe_rf_10y_tbill"] >= baseline_summary["sharpe_rf_10y_tbill"])
        & (overlay_only["max_drawdown_pct"] >= baseline_summary["max_drawdown_pct"])
    ].copy()
    ranked = improved if not improved.empty else overlay_only
    ranked = ranked.sort_values(
        ["sharpe_rf_10y_tbill", "max_drawdown_pct", "total_return_pct", "win_rate_pct"],
        ascending=[False, False, False, False],
    )
    selected = ranked.head(MAX_TOP_VARIANTS).copy()
    selected.to_csv(SELECTION_PATH, index=False)

    for _, row in selected.iterrows():
        window = int(row["window"])
        threshold = float(row["threshold"])
        label = f"{window}d gate {threshold:.2f}"
        equity_df, _ = build_equity_curve_with_overlay(
            history_map,
            candidate_df,
            score_column=f"score_w{window}",
            threshold=threshold,
        )
        variant_curves[label] = equity_df

    plot_variant_equity_curves(variant_curves, summary_df)
    plot_threshold_heatmap(summary_df)

    print(f"Candidate events: {len(candidate_df):,}")
    print(f"Candidate days: {candidate_df['date'].nunique():,}")
    print("Baseline:")
    print(
        f"  return {baseline_summary['total_return_pct']:+.2f}% | "
        f"max DD {baseline_summary['max_drawdown_pct']:.2f}% | "
        f"win rate {baseline_summary['win_rate_pct']:.2f}% | "
        f"Sharpe {baseline_summary['sharpe_rf_10y_tbill']:.2f} | "
        f"trades {baseline_summary['trade_count']}"
    )
    print("Top timing overlays:")
    cols = ["variant", "window", "threshold", "total_return_pct", "max_drawdown_pct", "win_rate_pct", "trade_count", "take_rate_pct", "sharpe_rf_10y_tbill"]
    print(selected[cols].to_string(index=False))
    print(f"Saved summary -> {SUMMARY_PATH}")
    print(f"Saved scores -> {OOS_SCORE_PATH}")
    print(f"Saved plot -> {PLOT_PATH}")
    print(f"Saved heatmap -> {HEATMAP_PATH}")


if __name__ == "__main__":
    main()
