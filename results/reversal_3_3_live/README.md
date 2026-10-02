# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 11:35:05 EDT`
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
  DRAM           80.00               30            0.95              0.41         61.85                54.09         0.572            pass              0.298             35.9                           0.307                3.07             -0.013                                 ok            True                  False
  AMGN           84.62               26            0.75              2.13        406.36                47.14         0.531            pass              0.395             37.3                           0.500                4.82              0.520                                 ok            True                  False
    MU           92.31               26            1.91             14.65       1091.11                49.88         0.505            pass              0.530             14.9                           0.225                5.97              0.333                                 ok            True                  False
  MSTR           92.31               39            0.07              0.08        160.47                96.54         0.620            pass              0.837             84.5                           0.471                4.20             -0.344                                 ok           False                  False
   WBD           95.65               46            0.02              0.00         30.95                37.65         0.551            pass              0.805             50.0                           0.398               11.31              0.523                                 ok           False                  False
  TEAM          100.00               38            1.06              1.41        189.31                55.53         0.515            pass              0.730             30.5                           0.179               -2.15             -0.603           downtrend_blocked_streak           False                  False
  VRSK           80.00               20            1.78              2.09        167.48                37.65         0.503            pass              0.168             17.2                           0.251               -5.71             -0.479 downtrend_blocked_slope_and_streak           False                  False
  GILD           88.89                9            1.70              1.75        146.75                19.81         0.495 below_threshold              0.329             14.2                           0.338               -3.41             -0.284 downtrend_blocked_slope_and_streak           False                  False
  PAYX           73.08               26            1.25              0.88        100.46                39.54         0.494 below_threshold              0.211             18.2                           0.287              -14.26             -1.702 downtrend_blocked_slope_and_streak           False                  False
  ADBE           86.67               30            1.45              2.44        240.23                44.30         0.487 below_threshold              0.409             16.5                           0.299               -4.47             -0.399            downtrend_blocked_slope           False                  False
   ADP           80.00               10            1.60              2.96        262.69                23.86         0.479 below_threshold              0.101             17.7                           0.314               -4.23             -0.415 downtrend_blocked_slope_and_streak           False                  False
   CEG           86.96               23            1.18              2.14        258.00                41.85         0.478 below_threshold              0.527             69.0                           0.488                0.45             -0.123                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-02T11:35:05.841468-04:00 early_entry_1135 early_entry_shadow     {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.61, "early_entry_score": 0.78, "early_reclaim_pct": 62.7, "entry_ask": 23.4, "entry_bid": 21.8, "entry_mode": "early", "entry_option_price": 22.6, "hypothetical_budget": 40682.15, "hypothetical_contracts": 18, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 7.08, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 94.29, "ticker": "ISRG", "timing_score": 0.446, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.78, "early_reclaim_pct": 62.7, "matched_signals": 35, "recovery_stability_score": 0.592, "success_rate": 94.29, "ticker": "ISRG", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:30:06.447357-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:25:01.826552-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:20:06.662983-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:15:03.733352-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:10:04.764942-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:05:01.135805-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "entry_ask": 26.3, "entry_bid": 23.2, "entry_mode": "early", "entry_option_price": 24.75, "hypothetical_budget": 40682.15, "hypothetical_contracts": 16, "matched_signals": 36, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 12.53, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "matched_signals": 36, "recovery_stability_score": 0.605, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:00:06.275509-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:55:04.805646-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:50:04.979298-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002113505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002113505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002113505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002113505)

</details>
