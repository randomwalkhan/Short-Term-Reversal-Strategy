# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 11:40:05 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$81,364.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           80.00               30            0.94              0.41         61.86                54.09         0.573            pass              0.302             37.0                           0.375                3.09             -0.012                                 ok            True                  False
  AMGN           85.71               28            0.65              1.85        406.48                47.14         0.526            pass              0.461             45.5                           0.562                4.92              0.524                                 ok            True                  False
    MU           92.31               26            1.96             15.04       1090.94                49.88         0.502            pass              0.523             12.7                           0.203                5.92              0.330                                 ok            True                  False
  MSTR           91.89               37            0.33              0.37        160.34                96.54         0.615            pass              0.652             31.2                           0.264                3.93             -0.356                                 ok           False                  False
   WBD           95.65               46            0.02              0.00         30.95                37.65         0.551            pass              0.805             50.0                           0.379               11.31              0.523                                 ok           False                  False
  TEAM          100.00               39            0.74              0.98        189.49                55.53         0.530            pass              0.801             51.7                           0.309               -1.83             -0.588           downtrend_blocked_streak           False                  False
  VRSK           76.47               17            2.00              2.36        167.37                37.65         0.502            pass              0.117              6.6                           0.154               -5.93             -0.489 downtrend_blocked_slope_and_streak           False                  False
  PAYX           73.08               26            1.20              0.85        100.48                39.54         0.497 below_threshold              0.221             21.4                           0.377              -14.22             -1.699 downtrend_blocked_slope_and_streak           False                  False
  GILD           87.50                8            1.75              1.80        146.73                19.81         0.496 below_threshold              0.285             11.7                           0.318               -3.46             -0.286 downtrend_blocked_slope_and_streak           False                  False
  ADBE           86.67               30            1.42              2.39        240.26                44.30         0.489 below_threshold              0.415             18.3                           0.328               -4.44             -0.398            downtrend_blocked_slope           False                  False
  CTSH           93.10               29            1.23              0.52         60.66                46.07         0.488 below_threshold              0.659             44.9                           0.638                0.43             -0.027                                 ok           False                  False
   ADP           80.00               10            1.57              2.90        262.72                23.86         0.481 below_threshold              0.106             19.4                           0.379               -4.20             -0.414 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-02T11:40:05.643538-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:35:05.841468-04:00 early_entry_1135 early_entry_shadow     {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.61, "early_entry_score": 0.78, "early_reclaim_pct": 62.7, "entry_ask": 23.4, "entry_bid": 21.8, "entry_mode": "early", "entry_option_price": 22.6, "hypothetical_budget": 40682.15, "hypothetical_contracts": 18, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 7.08, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 94.29, "ticker": "ISRG", "timing_score": 0.446, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.78, "early_reclaim_pct": 62.7, "matched_signals": 35, "recovery_stability_score": 0.592, "success_rate": 94.29, "ticker": "ISRG", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:30:06.447357-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:25:01.826552-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:20:06.662983-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:15:03.733352-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:10:04.764942-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:05:01.135805-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "entry_ask": 26.3, "entry_bid": 23.2, "entry_mode": "early", "entry_option_price": 24.75, "hypothetical_budget": 40682.15, "hypothetical_contracts": 16, "matched_signals": 36, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 12.53, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "matched_signals": 36, "recovery_stability_score": 0.605, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:00:06.275509-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:55:04.805646-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002114005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002114005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002114005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002114005)

</details>
