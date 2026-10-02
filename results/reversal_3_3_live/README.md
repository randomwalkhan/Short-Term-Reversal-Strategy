# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 10:20:07 EDT`
Last processed slot: `manage_1030`

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
   WBD           95.65               46            0.00              0.00         30.95                37.65         0.553            pass              0.952             99.0                           0.604               11.33              0.523                                 ok           False                  False
    MU           92.50               40            0.11              0.84       1097.03                49.88         0.542            pass              0.864             92.0                           0.723                7.91              0.415                                 ok           False                  False
  AMGN           84.85               33            0.45              1.29        406.72                47.14         0.510            pass              0.444             36.8                           0.355                5.13              0.533                                 ok           False                  False
  ADBE           90.00               40            0.57              0.97        240.87                44.30         0.494 below_threshold              0.621             34.9                           0.255               -3.62             -0.359                                 ok           False                  False
  CDNS           66.67               21            1.60              3.93        349.05                41.27         0.492 below_threshold              0.123              0.0                           0.157               21.99              1.869                                 ok           False                  False
  PAYX           80.49               41            0.16              0.11        100.79                39.54         0.491 below_threshold              0.520             85.8                           0.759              -13.31             -1.652 downtrend_blocked_slope_and_streak           False                  False
  CTSH           93.10               29            1.23              0.52         60.66                46.07         0.488 below_threshold              0.659             44.9                           0.590                0.43             -0.027                                 ok           False                  False
  VRSK           83.78               37            0.86              1.02        167.94                37.65         0.474 below_threshold              0.428             33.2                           0.308               -4.83             -0.437 downtrend_blocked_slope_and_streak           False                  False
   CEG           84.62               13            2.19              3.98        257.22                41.85         0.472 below_threshold              0.317             42.4                           0.382               -0.58             -0.170                                 ok           False                  False
  GILD           96.00               25            0.82              0.85        147.14                19.81         0.464 below_threshold              0.630             28.0                           0.313               -2.54             -0.243           downtrend_blocked_streak           False                  False
   KHC           92.86               28            0.16              0.02         22.45                18.85         0.463 below_threshold              0.757             82.5                           0.699               -8.21             -0.873 downtrend_blocked_slope_and_streak           False                  False
   ADP           90.48               21            1.06              1.96        263.12                23.86         0.463 below_threshold              0.485             28.7                           0.338               -3.71             -0.390 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-02T10:20:07.304982-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:15:06.003196-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:10:02.761986-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:05:05.705073-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:00:06.267323-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T09:20:04.739617-04:00     data_refresh       data_refresh                                             {'saved': 92, 'empty': 1}
2026-10-01T15:10:06.086305-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-01T15:05:04.536150-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-01T15:00:06.279684-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-01T14:55:05.658187-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002102007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002102007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002102007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002102007)

</details>
