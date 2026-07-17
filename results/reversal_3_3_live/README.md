# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-17 12:40:01 EDT`
Last processed slot: `manage_1230`

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
   KHC           91.67               12            0.71              0.13         26.17                36.78         0.627          pass              0.422             11.6                           0.206                2.66              0.368                  ok            True                  False
   TXN           91.30               23            1.79              3.65        289.65                64.46         0.608          pass              0.618             56.4                           0.591               -2.42             -0.193                  ok            True                  False
  ASML           94.29               35            0.59              7.39       1781.70                64.12         0.591          pass              0.868             87.0                           0.624                0.28              0.003                  ok            True                   True
   ADI           86.67               30            1.08              2.89        379.29                54.65         0.575          pass              0.579             70.0                           0.588               -0.20              0.014                  ok            True                  False
  NXPI           86.67               30            1.04              1.97        269.81                54.99         0.546          pass              0.596             76.8                           0.668               -2.02             -0.203                  ok            True                  False
   XEL          100.00               22            0.58              0.32         79.84                21.95         0.544          pass              0.550              5.2                           0.102               -2.98             -0.174                  ok            True                  False
   ADP           92.86               14            1.64              2.94        255.30                34.79         0.544          pass              0.477             17.8                           0.383                4.16              0.530                  ok            True                  False
  PAYX          100.00               18            1.63              1.31        114.14                35.43         0.522          pass              0.551             15.2                           0.355                6.10              0.711                  ok            True                  False
  CTAS           81.25               16            1.60              2.31        205.26                39.81         0.516          pass              0.213             29.5                           0.514               11.90              1.267                  ok            True                  False
   ROP           91.30               23            1.24              3.16        362.86                33.17         0.511          pass              0.491             17.4                           0.339               -0.99             -0.177                  ok            True                  False
  UPRO           93.75               16            2.15              2.16        142.68                37.18         0.509          pass              0.600             47.3                           0.535               -0.17              0.075                  ok            True                  False
   CSX           91.30               23            0.67              0.24         50.79                21.08         0.503          pass              0.571             44.3                           0.230                3.40              0.405                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-17T12:00:05.871771-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:55:01.882856-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:50:01.906755-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:45:01.890808-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:40:01.919825-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:35:01.723156-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:30:05.718379-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:25:05.915843-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:20:01.891090-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:15:01.934131-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260717124001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260717124001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260717124001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260717124001)

</details>
