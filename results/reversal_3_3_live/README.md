# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 13:45:03 EST`
Last processed slot: `manual`

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

- Cash: `$123,162.80`
- Equity: `$123,162.80`
- Realized PnL: `$113,162.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  ORLY     option         option ORLY261218C00095000    345          2026-11-05         2026-11-06        1.875      1.6875 -6468.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.75               16            0.56              0.26         66.71                30.66         0.585          pass              0.716             83.7                           0.624                4.14              0.759                                 ok            True                  False
 CMCSA           92.31               13            1.38              0.24         24.85                35.54         0.558          pass              0.598             64.6                           0.662                8.45              1.402                                 ok            True                  False
   KDP           96.15               26            0.50              0.13         36.83                35.93         0.545          pass              0.814             84.3                           0.654                5.84              0.626                                 ok            True                  False
   KHC           83.33               12            1.95              0.35         25.17                36.03         0.534          pass              0.308             50.9                           0.575                0.10              0.330                                 ok            True                  False
   ADP           85.00               20            1.11              2.38        306.12                28.50         0.515          pass              0.461             69.8                           0.590               -0.14              0.267                                 ok            True                  False
   PEP           81.82               22            0.88              0.87        142.34                27.68         0.507          pass              0.397             72.8                           0.618                4.19              0.659                                 ok            True                  False
  ORLY           94.44               18            1.30              0.83         91.13                25.42         0.505          pass              0.663             57.8                           0.632                0.43              0.130                                 ok            True                  False
  CTAS           95.45               22            0.93              1.48        225.78                27.57         0.504          pass              0.733             67.6                           0.724                0.09              0.305                                 ok            True                  False
  FTNT           78.26               23            2.10              1.80        121.74                92.45         0.650          pass              0.172              6.9                           0.144              -33.36             -4.932 downtrend_blocked_slope_and_streak           False                  False
   CSX           80.00                5            1.91              0.68         50.54                30.62         0.554          pass              0.093             12.6                           0.356               -1.83             -0.185                                 ok           False                  False
  MSTR           90.32               31            1.41              1.27        128.75                81.05         0.550          pass              0.623             50.9                           0.550              -12.69             -1.075            downtrend_blocked_slope           False                  False
   EXC           75.00                8            1.34              0.44         46.34                23.57         0.550          pass              0.203             49.4                           0.592                3.32              0.440                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-06T12:00:04.909641-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:55:04.780197-05:00 early_entry_1155 early_entry_shadow {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "entry_ask": 4.3, "entry_bid": 4.05, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 5.99, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "matched_signals": 38, "recovery_stability_score": 0.712, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:50:06.989427-05:00 early_entry_1150 early_entry_shadow {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 83.0, "entry_ask": 4.25, "entry_bid": 4.1, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 3.59, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.669, "shadow_only": true, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 83.0, "matched_signals": 37, "recovery_stability_score": 0.669, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:45:04.961396-05:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.52, "early_entry_score": 0.747, "early_reclaim_pct": 84.0, "entry_ask": 4.2, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.05, "hypothetical_budget": 61581.4, "hypothetical_contracts": 152, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 7.41, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.747, "early_reclaim_pct": 84.0, "matched_signals": 39, "recovery_stability_score": 0.646, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:40:05.161435-05:00 early_entry_1140 early_entry_shadow  {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.64, "early_entry_score": 0.694, "early_reclaim_pct": 80.4, "entry_ask": 4.2, "entry_bid": 4.15, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 1.2, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.587, "shadow_only": true, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.694, "early_reclaim_pct": 80.4, "matched_signals": 36, "recovery_stability_score": 0.587, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:35:06.887510-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:30:05.913627-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:25:05.831838-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:20:05.913571-05:00 early_entry_1120 early_entry_shadow  {"contract_symbol": "SBUX261218C00110000", "current_drop_pct": 0.51, "early_entry_score": 0.748, "early_reclaim_pct": 84.5, "entry_ask": 2.25, "entry_bid": 2.09, "entry_mode": "early", "entry_option_price": 2.17, "hypothetical_budget": 61581.4, "hypothetical_contracts": 283, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 12765.0, "option_spread_pct": 7.37, "option_volume": 91.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.748, "early_reclaim_pct": 84.5, "matched_signals": 39, "recovery_stability_score": 0.55, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:15:06.867015-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106134503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106134503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106134503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106134503)

</details>
