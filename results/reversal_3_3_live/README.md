# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 11:05:06 EDT`
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
  SNPS           82.14               28            0.93              2.96        453.31                54.29         0.572            pass              0.440             68.6                           0.678              -10.85             -1.333 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.10               42            0.12              0.22        263.10                59.49         0.545            pass              0.753             94.3                           0.807              -12.49             -1.404 downtrend_blocked_slope_and_streak           False                  False
  META           86.67               15            1.45              7.17        702.37                40.24         0.543            pass              0.439             58.0                           0.692               -5.91             -0.364 downtrend_blocked_slope_and_streak           False                  False
  DRAM           78.95               38            0.08              0.03         48.32                49.05         0.498 below_threshold              0.531             98.1                           0.789              -18.87             -2.641 downtrend_blocked_slope_and_streak           False                  False
   LIN           70.59               17            0.98              3.45        501.96                13.47         0.481 below_threshold              0.114              6.5                           0.195                1.75              0.360                                 ok           False                  False
  MSFT           93.55               31            0.40              1.48        532.89                21.83         0.468 below_threshold              0.766             72.5                           0.645                0.40              0.079                                 ok           False                  False
  CDNS           82.86               35            0.83              1.90        325.05                37.22         0.462 below_threshold              0.500             70.4                           0.599              -10.12             -1.251 downtrend_blocked_slope_and_streak           False                  False
  AAPL           82.61               23            0.86              2.07        342.05                16.04         0.456 below_threshold              0.353             50.3                           0.316                1.91              0.211                                 ok           False                  False
  CRWD           89.74               39            0.74              1.18        227.59                50.50         0.452 below_threshold              0.723             74.9                           0.514              -18.81             -2.157 downtrend_blocked_slope_and_streak           False                  False
  PANW           82.35               34            1.65              4.01        345.23                55.73         0.451 below_threshold              0.427             53.1                           0.364              -18.74             -2.219 downtrend_blocked_slope_and_streak           False                  False
  ASML           82.05               39            0.02              0.18       1647.04                29.62         0.444 below_threshold              0.590             99.2                           0.789              -10.21             -1.211            downtrend_blocked_slope           False                  False
  AMAT           77.14               35            1.37              3.95        411.42                46.44         0.433 below_threshold              0.390             60.0                           0.519              -23.16             -3.034 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-20T11:05:06.503440-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:00:06.812644-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:55:08.897321-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:50:04.954872-04:00 early_entry_1050 early_entry_shadow  {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.57, "early_entry_score": 0.765, "early_reclaim_pct": 63.6, "entry_ask": 2.85, "entry_bid": 2.55, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 268, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 584.0, "option_spread_pct": 11.11, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.411, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.765, "early_reclaim_pct": 63.6, "matched_signals": 40, "recovery_stability_score": 0.604, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-20T10:45:05.488379-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:40:06.473835-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.55, "early_entry_score": 0.771, "early_reclaim_pct": 65.3, "entry_ask": 2.85, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 2.675, "hypothetical_budget": 72415.9, "hypothetical_contracts": 270, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 584.0, "option_spread_pct": 13.08, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.771, "early_reclaim_pct": 65.3, "matched_signals": 40, "recovery_stability_score": 0.634, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-20T10:30:06.843333-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:25:04.152080-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:20:05.290913-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:15:05.434773-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020110506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020110506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020110506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020110506)

</details>
