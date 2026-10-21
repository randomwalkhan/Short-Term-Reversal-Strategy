# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 14:05:04 EDT`
Last processed slot: `manage_1400`

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
   KHC           83.33               18            1.41              0.23         23.73                25.26         0.508            pass              0.229             11.8                           0.239                6.89              0.754                      ok            True                  False
  TMUS           50.00                8            2.90              3.21        156.38                56.37         0.557            pass              0.135             26.5                           0.325               -8.64             -0.472 downtrend_blocked_slope           False                  False
  MDLZ          100.00                1            2.38              1.06         63.53                19.17         0.550            pass              0.470              5.0                           0.224                5.20              0.637                      ok           False                  False
   KDP           96.67               30            0.27              0.07         34.60                29.04         0.540            pass              0.848             87.0                           0.572               13.08              1.296                      ok           False                  False
  GILD           87.50                8            1.98              2.17        155.58                26.70         0.526            pass              0.359             35.4                           0.453                4.47              0.583                      ok           False                  False
  DASH           76.47               17            2.33              3.12        190.33                49.85         0.511            pass              0.191             31.2                           0.465               -2.11             -0.188                      ok           False                  False
  INTU           88.89               36            0.36              0.84        334.93                37.42         0.503            pass              0.674             71.0                           0.545               12.92              1.302                      ok           False                  False
  MELI           78.12               32            1.08             14.24       1873.40                40.36         0.498 below_threshold              0.284             29.2                           0.409               -0.73             -0.128                      ok           False                  False
 CMCSA           75.00                4            2.25              0.35         22.21                21.50         0.491 below_threshold              0.157             35.9                           0.413                4.38              0.688                      ok           False                  False
  GEHC           76.47               17            1.48              0.73         69.92                23.16         0.484 below_threshold              0.191             32.0                           0.450                6.99              0.863                      ok           False                  False
  ORLY           94.74               19            1.28              0.81         89.67                13.90         0.481 below_threshold              0.530              9.8                           0.277                5.03              0.550                      ok           False                  False
   ROP           88.57               35            0.53              1.49        397.57                26.56         0.475 below_threshold              0.620             59.0                           0.436               10.46              1.027                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021140504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021140504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021140504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021140504)

</details>
