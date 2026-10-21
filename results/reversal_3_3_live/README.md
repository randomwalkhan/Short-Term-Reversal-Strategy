# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 11:50:06 EDT`
Last processed slot: `manage_1200`

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
   KHC           85.71               21            1.24              0.21         23.74                25.26         0.505            pass              0.308             10.6                           0.241                7.07              0.762                      ok            True                  False
  MDLZ          100.00                1            2.28              1.02         63.55                19.17         0.557            pass              0.459              1.0                           0.120                5.30              0.642                      ok           False                  False
   KDP           96.43               28            0.35              0.08         34.59                29.04         0.548            pass              0.825             83.6                           0.446               13.00              1.293                      ok           False                  False
  TMUS           42.86                7            3.13              3.45        156.27                56.37         0.541            pass              0.117             20.9                           0.172               -8.85             -0.483 downtrend_blocked_slope           False                  False
  GILD           83.33                6            2.24              2.46        155.46                26.70         0.518            pass              0.221             26.9                           0.284                4.19              0.571                      ok           False                  False
  DASH           76.92               13            2.65              3.56        190.15                49.85         0.516            pass              0.136             21.6                           0.422               -2.43             -0.203                      ok           False                  False
 CMCSA          100.00                3            2.62              0.41         22.18                21.50         0.507            pass              0.527             25.5                           0.311                3.99              0.671                      ok           False                  False
  INTU           89.19               37            0.22              0.51        335.07                37.42         0.505            pass              0.723             82.3                           0.705               13.08              1.308                      ok           False                  False
  GEHC           72.73               11            1.87              0.92         69.84                23.16         0.493 below_threshold              0.099             14.4                           0.270                6.57              0.845                      ok           False                  False
  MELI           80.00               45            0.22              2.92       1878.25                40.36         0.481 below_threshold              0.484             78.6                           0.532                0.14             -0.089                      ok           False                  False
  ORLY           95.45               22            1.18              0.75         89.70                13.90         0.470 below_threshold              0.577             16.8                           0.379                5.14              0.555                      ok           False                  False
  AMGN           83.33               30            0.77              2.36        437.93                28.05         0.469 below_threshold              0.456             62.2                           0.339                5.44              0.686                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-21T11:50:06.757863-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:45:06.913191-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.71, "early_entry_score": 0.75, "early_reclaim_pct": 61.7, "entry_ask": 31.6, "entry_bid": 27.2, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 14.97, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.75, "early_reclaim_pct": 61.7, "matched_signals": 39, "recovery_stability_score": 0.619, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T11:40:05.964445-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:35:04.680033-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:30:04.338069-04:00 early_entry_1130 early_entry_shadow              {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.58, "early_entry_score": 0.783, "early_reclaim_pct": 68.6, "entry_ask": 30.9, "entry_bid": 27.9, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 22.0, "option_spread_pct": 10.2, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.635, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.436, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.783, "early_reclaim_pct": 68.6, "matched_signals": 40, "recovery_stability_score": 0.635, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T11:25:05.346017-04:00 early_entry_1125 early_entry_shadow                 {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.65, "early_entry_score": 0.771, "early_reclaim_pct": 64.7, "entry_ask": 31.0, "entry_bid": 27.8, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 22.0, "option_spread_pct": 10.88, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.6, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.771, "early_reclaim_pct": 64.7, "matched_signals": 40, "recovery_stability_score": 0.6, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T11:20:06.788412-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:15:06.754370-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:10:03.902127-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T11:05:02.562193-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021115006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021115006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021115006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021115006)

</details>
