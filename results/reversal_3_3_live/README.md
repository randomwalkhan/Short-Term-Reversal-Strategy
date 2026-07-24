# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 13:00:02 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$34,043.00`
- Equity: `$34,043.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00320000     13          2026-07-23         2026-07-24       11.225      13.675 3185.0   21.826281 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           89.47               19            4.07             26.04        902.20               102.76         0.583          pass              0.451             26.8                           0.204               -3.76              0.334                                 ok            True                  False
  GILD           92.00               25            0.61              0.56        130.62                35.55         0.569          pass              0.607             43.5                           0.315                0.18             -0.041                                 ok            True                  False
  ASML           93.75               32            1.09             13.80       1797.09                56.08         0.565          pass              0.749             59.9                           0.480               -0.78              0.125                                 ok            True                  False
   WDC           94.44               18            5.27             20.60        549.47               114.14         0.545          pass              0.552             19.7                           0.179               -9.22             -0.297                                 ok            True                  False
  KLAC           84.62               26            1.93              2.96        217.46                98.03         0.689          pass              0.447             49.4                           0.347               -7.35             -0.704 downtrend_blocked_slope_and_streak           False                  False
  AMAT           90.91               22            2.55             10.03        558.50                96.41         0.602          pass              0.575             48.0                           0.347               -8.97             -0.812 downtrend_blocked_slope_and_streak           False                  False
  LRCX           84.62               26            2.32              5.20        317.55                88.87         0.601          pass              0.427             45.9                           0.308              -10.84             -0.970 downtrend_blocked_slope_and_streak           False                  False
   KDP           93.94               33            0.03              0.01         29.67                36.62         0.578          pass              0.861             92.6                           0.493               -6.35             -0.524 downtrend_blocked_slope_and_streak           False                  False
  META           82.35               34            0.81              3.44        604.63                54.86         0.571          pass              0.384             34.8                           0.218              -10.16             -1.051 downtrend_blocked_slope_and_streak           False                  False
  MSTR           75.61               41            1.04              0.68         93.34                85.75         0.523          pass              0.477             74.9                           0.509               -2.09              0.149                                 ok           False                  False
  CRWD           91.30               46            0.41              0.53        183.19                61.02         0.521          pass              0.708             51.6                           0.278               -2.41             -0.671 downtrend_blocked_slope_and_streak           False                  False
   APP           77.78               36            2.06              5.75        396.39                79.31         0.520          pass              0.317             30.7                           0.247              -22.95             -1.917            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-24T12:00:04.447749-04:00 early_entry_1200 early_entry_shadow        {"contract_symbol": "ASML260918C01790000", "current_drop_pct": 0.6, "early_entry_score": 0.84, "early_reclaim_pct": 78.1, "entry_ask": 155.4, "entry_bid": 151.0, "entry_mode": "early", "entry_option_price": 153.2, "hypothetical_budget": 17021.5, "hypothetical_contracts": 1, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 3.0, "option_spread_pct": 2.87, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.83, "shadow_only": true, "success_rate": 94.29, "ticker": "ASML", "timing_score": 0.58, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.84, "early_reclaim_pct": 78.1, "matched_signals": 35, "recovery_stability_score": 0.83, "success_rate": 94.29, "ticker": "ASML", "timing_score": 0.58, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-24T11:55:05.489069-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ASML260828C01785000", "current_drop_pct": 0.92, "early_entry_score": 0.781, "early_reclaim_pct": 66.4, "entry_ask": 129.0, "entry_bid": 115.0, "entry_mode": "early", "entry_option_price": 122.0, "hypothetical_budget": 17021.5, "hypothetical_contracts": 1, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 11.48, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.77, "shadow_only": true, "success_rate": 93.94, "ticker": "ASML", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.781, "early_reclaim_pct": 66.4, "matched_signals": 33, "recovery_stability_score": 0.77, "success_rate": 93.94, "ticker": "ASML", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-24T11:50:02.496150-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:45:02.490359-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:40:02.395425-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:35:03.478911-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:30:02.536091-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:25:02.429701-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:20:02.438945-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:15:02.420314-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724130002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724130002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724130002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724130002)

</details>
