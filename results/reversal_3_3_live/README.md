# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 11:25:01 EDT`
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
  DRAM           81.48               27            1.40              0.61         61.77                54.09         0.564            pass              0.216              2.2                           0.158                2.60             -0.034                                 ok            True                  False
  AMGN           84.62               26            0.79              2.26        406.30                47.14         0.528            pass              0.383             33.4                           0.372                4.77              0.517                                 ok            True                  False
    ZS           95.74               47            0.06              0.08        198.75                77.30         0.643            pass              0.948             94.5                           0.462                0.69             -0.471                                 ok           False                  False
  MSTR           91.89               37            0.34              0.38        160.34                96.54         0.615            pass              0.629             23.3                           0.126                3.92             -0.357                                 ok           False                  False
   WBD           95.65               46            0.02              0.00         30.95                37.65         0.551            pass              0.805             50.0                           0.392               11.31              0.523                                 ok           False                  False
   TRI           89.74               39            0.18              0.12         99.31                57.35         0.532            pass              0.795             96.1                           0.531                5.08              0.350                                 ok           False                  False
  TEAM          100.00               37            1.10              1.46        189.29                55.53         0.519            pass              0.717             28.3                           0.198               -2.18             -0.604           downtrend_blocked_streak           False                  False
  VRSK           76.47               17            1.99              2.35        167.37                37.65         0.503            pass              0.119              7.2                           0.104               -5.92             -0.489 downtrend_blocked_slope_and_streak           False                  False
  PAYX           68.18               22            1.46              1.03        100.40                39.54         0.498 below_threshold              0.139              3.0                           0.054              -14.44             -1.712 downtrend_blocked_slope_and_streak           False                  False
  GILD           87.50                8            1.76              1.81        146.72                19.81         0.496 below_threshold              0.283             11.3                           0.276               -3.46             -0.286 downtrend_blocked_slope_and_streak           False                  False
  ADBE           86.67               30            1.36              2.30        240.29                44.30         0.492 below_threshold              0.425             21.4                           0.247               -4.39             -0.395            downtrend_blocked_slope           False                  False
    MU           92.31               26            2.14             16.41       1090.36                49.88         0.491 below_threshold              0.498              4.7                           0.082                5.72              0.322                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-02T11:25:01.826552-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:20:06.662983-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:15:03.733352-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:10:04.764942-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:05:01.135805-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "entry_ask": 26.3, "entry_bid": 23.2, "entry_mode": "early", "entry_option_price": 24.75, "hypothetical_budget": 40682.15, "hypothetical_contracts": 16, "matched_signals": 36, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 12.53, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.804, "early_reclaim_pct": 66.9, "matched_signals": 36, "recovery_stability_score": 0.605, "success_rate": 94.44, "ticker": "ISRG", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:00:06.275509-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:55:04.805646-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:50:04.979298-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:45:02.843264-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:40:04.819800-04:00 early_entry_1040 early_entry_shadow                         {"contract_symbol": "CEG261120C00260000", "current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "entry_ask": 16.1, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 15.5, "hypothetical_budget": 40682.15, "hypothetical_contracts": 26, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 433.0, "option_spread_pct": 7.74, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.898, "shadow_only": true, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.693, "early_reclaim_pct": 77.5, "matched_signals": 31, "recovery_stability_score": 0.898, "success_rate": 90.32, "ticker": "CEG", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002112501)

</details>
