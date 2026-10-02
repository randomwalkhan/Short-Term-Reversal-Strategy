# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 10:15:06 EDT`
Last processed slot: `early_entry_1015`

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
    MU           92.11               38            0.51              3.92       1095.71                49.88         0.528            pass              0.750             62.7                           0.413                7.48              0.397                                 ok            True                  False
   WBD           95.65               46            0.02              0.00         30.95                37.65         0.551            pass              0.805             50.0                           0.358               11.31              0.523                                 ok           False                  False
  PAYX           79.41               34            0.46              0.32        100.70                39.54         0.511            pass              0.389             59.3                           0.595              -13.57             -1.665 downtrend_blocked_slope_and_streak           False                  False
  AMGN           86.11               36            0.33              0.94        406.87                47.14         0.501            pass              0.548             53.8                           0.442                5.26              0.539                                 ok           False                  False
  CTSH           92.00               25            1.54              0.65         60.60                46.07         0.492 below_threshold              0.563             31.2                           0.466                0.13             -0.041                                 ok           False                  False
   ADP           85.71               14            1.26              2.33        262.96                23.86         0.487 below_threshold              0.273             15.2                           0.184               -3.90             -0.400 downtrend_blocked_slope_and_streak           False                  False
  ADBE           90.00               40            0.69              1.17        240.78                44.30         0.486 below_threshold              0.580             21.5                           0.205               -3.74             -0.364                                 ok           False                  False
  VRSK           84.62               39            0.72              0.85        168.01                37.65         0.472 below_threshold              0.495             43.8                           0.380               -4.70             -0.430 downtrend_blocked_slope_and_streak           False                  False
   KHC           92.86               28            0.04              0.01         22.46                18.85         0.471 below_threshold              0.795             95.0                           0.742               -8.10             -0.868 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71                7            2.85              5.17        256.71                41.85         0.469 below_threshold              0.275             25.2                           0.229               -1.24             -0.200                                 ok           False                  False
  CDNS           76.47               34            1.03              2.52        349.65                41.27         0.464 below_threshold              0.206              0.0                           0.157               22.70              1.895                                 ok           False                  False
  NFLX           83.72               43            0.41              0.20         67.77                35.87         0.448 below_threshold              0.520             58.8                           0.536               -5.88             -0.718            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-02T10:15:06.003196-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:10:02.761986-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:05:05.705073-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:00:06.267323-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T09:20:04.739617-04:00     data_refresh       data_refresh                                             {'saved': 92, 'empty': 1}
2026-10-01T15:10:06.086305-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-01T15:05:04.536150-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-01T15:00:06.279684-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-01T14:55:05.658187-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-01T14:50:05.514279-04:00       entry_1500      entry_skipped                                            {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002101506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002101506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002101506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002101506)

</details>
