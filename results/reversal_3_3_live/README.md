# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 11:50:01 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           87.50               32            0.68              0.27         56.61                63.95         0.627          pass              0.632             74.0                           0.771               23.92              2.502                  ok            True                  False
   TXN           89.47               19            2.36              4.81        289.16                64.46         0.594          pass              0.500             42.7                           0.620               -2.98             -0.220                  ok            True                  False
  MPWR           81.82               33            0.93              8.50       1302.01                74.72         0.589          pass              0.512             83.7                           0.876                0.42              0.100                  ok            True                  False
  ASML           93.10               29            1.25             15.65       1778.16                64.12         0.586          pass              0.752             72.6                           0.829               -0.38             -0.028                  ok            True                  False
   ADI           84.62               26            1.33              3.53        379.02                54.65         0.583          pass              0.478             63.3                           0.654               -0.45              0.002                  ok            True                  False
   ADP           95.24               21            1.22              2.20        255.62                34.79         0.535          pass              0.534              2.5                           0.167                4.60              0.549                  ok            True                  False
  NXPI           83.33               24            1.78              3.37        269.21                54.99         0.531          pass              0.416             60.3                           0.716               -2.75             -0.237                  ok            True                  False
  PAYX          100.00               21            1.34              1.08        114.24                35.43         0.526          pass              0.543              5.5                           0.167                6.40              0.724                  ok            True                  False
  CTAS           81.25               16            1.61              2.33        205.25                39.81         0.522          pass              0.134              2.8                           0.160               11.88              1.267                  ok            True                  False
  AVGO           84.38               32            0.92              2.41        373.42                50.81         0.514          pass              0.553             79.3                           0.755                2.93              0.267                  ok            True                  False
  UPRO           92.86               14            2.31              2.32        142.61                37.18         0.511          pass              0.551             43.3                           0.595               -0.34              0.067                  ok            True                  False
  SBUX           82.35               17            1.18              0.90        107.99                23.69         0.508          pass              0.180              6.6                           0.183                2.70              0.425                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T11:50:01.906755-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:45:01.890808-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:40:01.919825-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:35:01.723156-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:30:05.718379-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:25:05.915843-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:20:01.891090-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:15:01.934131-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:10:03.757690-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:05:01.918068-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717115001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717115001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717115001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717115001)

</details>
