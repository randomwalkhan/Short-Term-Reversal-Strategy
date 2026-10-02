# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 12:00:05 EDT`
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
  MSTR           91.43               35            0.59              0.66        160.22                96.54         0.607            pass              0.626             31.2                           0.201                3.66             -0.368                                 ok            True                  False
  AMGN           83.33               24            0.97              2.76        406.09                47.14         0.527            pass              0.291             18.8                           0.279                4.58              0.509                                 ok            True                  False
    MU           89.66               29            1.51             11.61       1092.42                49.88         0.509            pass              0.533             32.6                           0.503                6.40              0.351                                 ok            True                  False
    ZS           95.56               45            0.29              0.40        198.61                77.30         0.640            pass              0.878             71.4                           0.429                0.46             -0.481                                 ok           False                  False
  DRAM           79.41               34            0.48              0.21         61.94                54.09         0.577            pass              0.420             67.4                           0.673                3.56              0.008                                 ok           False                  False
   WBD           95.65               46            0.02              0.00         30.95                37.65         0.551            pass              0.805             50.0                           0.345               11.31              0.523                                 ok           False                  False
  TEAM          100.00               33            1.52              2.02        189.05                55.53         0.515            pass              0.640             11.9                           0.221               -2.60             -0.624           downtrend_blocked_streak           False                  False
   ADP          100.00                7            1.91              3.53        262.45                23.86         0.499 below_threshold              0.455              1.7                           0.179               -4.54             -0.430 downtrend_blocked_slope_and_streak           False                  False
  CTSH           89.47               19            1.92              0.82         60.53                46.07         0.499 below_threshold              0.430             22.5                           0.273               -0.27             -0.059                                 ok           False                  False
  GILD           87.50                8            1.75              1.81        146.73                19.81         0.496 below_threshold              0.285             11.6                           0.277               -3.46             -0.286 downtrend_blocked_slope_and_streak           False                  False
  NFLX           72.73               22            1.39              0.66         67.57                35.87         0.496 below_threshold              0.163             11.0                           0.201               -6.80             -0.763            downtrend_blocked_slope           False                  False
  PAYX           72.00               25            1.32              0.93        100.44                39.54         0.493 below_threshold              0.197             16.0                           0.303              -14.32             -1.705 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-02T12:00:05.856785-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:55:04.675487-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:50:01.924134-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:45:02.865482-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:40:05.643538-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:35:05.841468-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "ISRG261120C00400000", "current_drop_pct": 0.61, "early_entry_score": 0.78, "early_reclaim_pct": 62.7, "entry_ask": 23.4, "entry_bid": 21.8, "entry_mode": "early", "entry_option_price": 22.6, "hypothetical_budget": 40682.15, "hypothetical_contracts": 18, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 285.0, "option_spread_pct": 7.08, "option_volume": 15.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 94.29, "ticker": "ISRG", "timing_score": 0.446, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.78, "early_reclaim_pct": 62.7, "matched_signals": 35, "recovery_stability_score": 0.592, "success_rate": 94.29, "ticker": "ISRG", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-02T11:30:06.447357-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:25:01.826552-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:20:06.662983-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T11:15:03.733352-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002120005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002120005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002120005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002120005)

</details>
