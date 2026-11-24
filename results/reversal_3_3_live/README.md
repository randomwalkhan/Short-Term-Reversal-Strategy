# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 14:30:06 EST`
Last processed slot: `manage_1430`

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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PANW           80.00               40            0.89              2.21        352.48                70.38         0.526          pass              0.452             66.4                           0.337                7.33              0.967                                 ok            True                  False
  ODFL           86.67               30            0.95              1.14        170.78                44.14         0.508          pass              0.595             77.6                           0.688                0.97             -0.000                                 ok            True                  False
  INTC           50.00                8            6.87              2.87         58.43               154.63         0.644          pass              0.163             33.0                           0.686               -4.42             -0.994 downtrend_blocked_slope_and_streak           False                  False
  UPRO           80.77               26            1.57              1.31        119.18                94.72         0.637          pass              0.389             65.9                           0.695              -13.57             -2.384 downtrend_blocked_slope_and_streak           False                  False
  ASML           66.67               12            2.92             28.27       1371.66                73.86         0.584          pass              0.204             44.1                           0.636              -10.91             -1.542 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           73.91               23            1.27              2.50        281.03                61.35         0.582          pass              0.268             41.2                           0.570               -3.08             -0.761            downtrend_blocked_slope           False                  False
   CEG           85.71               14            2.66              4.69        249.71                65.44         0.579          pass              0.309             24.1                           0.405               -8.35             -1.419 downtrend_blocked_slope_and_streak           False                  False
   BKR           85.29               34            0.49              0.16         45.97                56.59         0.564          pass              0.587             76.3                           0.714               -4.09             -0.800 downtrend_blocked_slope_and_streak           False                  False
  GOOG           77.78               27            1.14              2.23        278.57                58.63         0.560          pass              0.299             43.2                           0.583               -3.01             -0.732            downtrend_blocked_slope           False                  False
  AVGO           61.54               13            3.05              6.70        310.68                86.52         0.554          pass              0.193             39.2                           0.565               -8.43             -1.188            downtrend_blocked_slope           False                  False
  SHOP           73.91               23            2.16              2.03        133.43                71.17         0.537          pass              0.165              8.2                           0.148              -10.37             -1.598 downtrend_blocked_slope_and_streak           False                  False
  LRCX           62.50                8            6.03              8.85        205.97               114.43         0.524          pass              0.156             34.5                           0.638              -11.37             -1.824 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-24T12:00:06.462519-05:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:55:05.635523-05:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:50:06.028676-05:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:45:06.576648-05:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:40:05.757709-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:35:05.562629-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:30:04.516511-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:25:06.575801-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:20:05.808543-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:15:03.611406-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124143006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124143006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124143006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124143006)

</details>
