# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 10:50:04 EDT`
Last processed slot: `manage_1100`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   ADP     option         option ADP261120C00290000     70          2026-10-19         2026-10-20          9.3        11.2 13300.0   20.430108 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           81.48               27            1.00              3.19        453.21                54.29         0.573            pass              0.409             66.3                           0.576              -10.92             -1.336 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.64               44            0.00              0.01        263.19                59.49         0.540            pass              0.784             99.8                           0.915              -12.39             -1.399 downtrend_blocked_slope_and_streak           False                  False
  META           81.82               11            1.87              9.25        701.48                40.24         0.538            pass              0.246             45.8                           0.604               -6.31             -0.383 downtrend_blocked_slope_and_streak           False                  False
  DRAM           78.95               38            0.13              0.05         48.31                49.05         0.495 below_threshold              0.527             96.8                           0.838              -18.91             -2.643 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.55               29            0.46              1.71        532.79                21.83         0.479 below_threshold              0.779             68.2                           0.676                0.34              0.077                                 ok           False                  False
   LIN           77.27               22            0.76              2.69        502.29                13.47         0.473 below_threshold              0.159             10.7                           0.151                1.97              0.370                                 ok           False                  False
  CDNS           83.33               36            0.70              1.60        325.17                37.22         0.465 below_threshold              0.534             74.9                           0.660              -10.01             -1.245 downtrend_blocked_slope_and_streak           False                  False
  PANW           82.86               35            1.46              3.55        345.43                55.73         0.456 below_threshold              0.464             58.4                           0.523              -18.58             -2.210 downtrend_blocked_slope_and_streak           False                  False
  CPRT           62.50               16            2.29              0.44         27.32                31.97         0.448 below_threshold              0.164             26.3                           0.470                0.22              0.189                                 ok           False                  False
  CRWD           90.70               43            0.50              0.80        227.76                50.50         0.444 below_threshold              0.779             83.1                           0.597              -18.61             -2.146 downtrend_blocked_slope_and_streak           False                  False
  ASML           80.56               36            0.30              3.46       1645.64                29.62         0.443 below_threshold              0.488             85.3                           0.750              -10.46             -1.224            downtrend_blocked_slope           False                  False
  IDXX           93.48               46            0.02              0.06        555.77                25.12         0.439 below_threshold              0.894             97.0                           0.602                7.82              1.027                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-20T10:50:04.954872-04:00 early_entry_1050 early_entry_shadow  {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.57, "early_entry_score": 0.765, "early_reclaim_pct": 63.6, "entry_ask": 2.85, "entry_bid": 2.55, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 268, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 584.0, "option_spread_pct": 11.11, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.411, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.765, "early_reclaim_pct": 63.6, "matched_signals": 40, "recovery_stability_score": 0.604, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-20T10:45:05.488379-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:40:06.473835-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.55, "early_entry_score": 0.771, "early_reclaim_pct": 65.3, "entry_ask": 2.85, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 2.675, "hypothetical_budget": 72415.9, "hypothetical_contracts": 270, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 584.0, "option_spread_pct": 13.08, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.771, "early_reclaim_pct": 65.3, "matched_signals": 40, "recovery_stability_score": 0.634, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-20T10:30:06.843333-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:25:04.152080-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:20:05.290913-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:15:05.434773-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:10:06.028828-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:05:04.298275-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:00:02.343877-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020105004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020105004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020105004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020105004)

</details>
