# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 12:35:02 EDT`
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

- Cash: `$38,043.00`
- Equity: `$38,043.00`
- Realized PnL: `$28,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   ROP          100.00               20            1.41              3.89        393.56                44.32         0.617          pass              0.603             25.0                           0.388                0.11              0.142                      ok            True                  False
  DXCM           88.89               36            0.63              0.40         90.63                59.17         0.598          pass              0.505             11.5                           0.155               21.04              1.212                      ok            True                  False
  FAST          100.00               10            1.75              0.64         51.95                25.01         0.578          pass              0.472              4.7                           0.130                9.95              1.138                      ok            True                  False
  MPWR           84.21               38            0.75              7.52       1421.79                55.33         0.539          pass              0.511             52.8                           0.585                7.45              0.601                      ok            True                  False
  PCAR           96.00               25            1.11              1.01        130.63                29.70         0.533          pass              0.647             31.3                           0.352               -3.10             -0.200                      ok            True                  False
   BKR           82.14               28            0.96              0.43         64.10                33.24         0.502          pass              0.424             65.4                           0.582                6.68              0.794                      ok            True                  False
  INSM           66.67                9            4.26              3.94        130.59               107.72         0.678          pass              0.079              3.6                           0.219               24.79              3.701                      ok           False                  False
  ISRG           86.49               37            0.35              0.98        400.85                69.94         0.673          pass              0.592             57.2                           0.494               13.29              1.337                      ok           False                  False
  AMZN           79.41               34            0.81              1.52        266.63                61.57         0.629          pass              0.258             11.8                           0.176               12.57              0.434                      ok           False                  False
   TRI           87.80               41            0.09              0.06        102.58                74.92         0.619          pass              0.764             97.9                           0.577                3.73              0.401                      ok           False                  False
  NXPI           74.36               39            0.05              0.08        233.37                51.39         0.566          pass              0.530             93.3                           0.698               -4.84              0.089                      ok           False                  False
   HON           88.00               25            0.84              1.38        234.75                35.57         0.555          pass              0.457             29.5                           0.273               -3.53             -0.610 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-13T11:55:02.213370-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:53:25.963945-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:45:10.117918-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:40:06.788937-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:35:08.590651-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:30:06.832547-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:25:05.233989-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:20:08.326885-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:15:07.600567-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:10:09.886626-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813123502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813123502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813123502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813123502)

</details>
