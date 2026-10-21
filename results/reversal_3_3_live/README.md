# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 14:15:03 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MELI           82.14               28            1.30             17.11       1872.17                40.36         0.514            pass              0.273             14.9                           0.311               -0.95             -0.138                      ok            True                  False
   KHC           83.33               18            1.43              0.24         23.73                25.26         0.507            pass              0.224             10.5                           0.249                6.87              0.753                      ok            True                  False
  TMUS           50.00                8            2.92              3.22        156.37                56.37         0.556            pass              0.134             26.2                           0.355               -8.65             -0.473 downtrend_blocked_slope           False                  False
  MDLZ          100.00                1            2.41              1.08         63.53                19.17         0.548            pass              0.465              3.4                           0.234                5.16              0.635                      ok           False                  False
   KDP           96.88               32            0.16              0.04         34.61                29.04         0.536            pass              0.878             92.5                           0.763               13.21              1.301                      ok           False                  False
  GILD           87.50                8            2.03              2.23        155.56                26.70         0.524            pass              0.354             33.7                           0.388                4.41              0.580                      ok           False                  False
  DASH           76.47               17            2.31              3.10        190.34                49.85         0.512            pass              0.192             31.6                           0.428               -2.09             -0.187                      ok           False                  False
 CMCSA           75.00                4            2.08              0.33         22.22                21.50         0.500            pass              0.172             40.8                           0.593                4.56              0.696                      ok           False                  False
  INTU           89.19               37            0.33              0.77        334.96                37.42         0.499 below_threshold              0.696             73.7                           0.694               12.96              1.303                      ok           False                  False
  GEHC           80.95               21            1.32              0.65         69.95                23.16         0.475 below_threshold              0.264             39.2                           0.621                7.16              0.870                      ok           False                  False
  GOOG           75.00                8            1.77              4.17        334.61                21.71         0.474 below_threshold              0.171             41.3                           0.524               -4.87             -0.454 downtrend_blocked_slope           False                  False
 GOOGL           81.82               11            1.69              4.02        338.55                22.44         0.472 below_threshold              0.228             41.9                           0.557               -4.56             -0.431 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-21T12:00:03.696470-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:55:05.704920-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.72, "early_entry_score": 0.748, "early_reclaim_pct": 61.1, "entry_ask": 32.2, "entry_bid": 27.2, "entry_mode": "early", "entry_option_price": 29.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 16.84, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.433, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.748, "early_reclaim_pct": 61.1, "matched_signals": 39, "recovery_stability_score": 0.62, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.433, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T11:50:06.757863-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:45:06.913191-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.71, "early_entry_score": 0.75, "early_reclaim_pct": 61.7, "entry_ask": 31.6, "entry_bid": 27.2, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 14.97, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.75, "early_reclaim_pct": 61.7, "matched_signals": 39, "recovery_stability_score": 0.619, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T11:40:05.964445-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:35:04.680033-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:30:04.338069-04:00 early_entry_1130 early_entry_shadow              {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.58, "early_entry_score": 0.783, "early_reclaim_pct": 68.6, "entry_ask": 30.9, "entry_bid": 27.9, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 22.0, "option_spread_pct": 10.2, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.635, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.436, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.783, "early_reclaim_pct": 68.6, "matched_signals": 40, "recovery_stability_score": 0.635, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T11:25:05.346017-04:00 early_entry_1125 early_entry_shadow                 {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.65, "early_entry_score": 0.771, "early_reclaim_pct": 64.7, "entry_ask": 31.0, "entry_bid": 27.8, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 22.0, "option_spread_pct": 10.88, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.6, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.771, "early_reclaim_pct": 64.7, "matched_signals": 40, "recovery_stability_score": 0.6, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T11:20:06.788412-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:15:06.754370-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021141503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021141503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021141503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021141503)

</details>
