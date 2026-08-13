# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-13 11:35:08 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   ROP          100.00               21            1.40              3.86        393.57                44.32         0.611          pass              0.611             25.5                           0.253                0.12              0.142                  ok            True                  False
  FAST          100.00               17            0.93              0.34         52.07                25.01         0.589          pass              0.555             16.4                           0.168               10.88              1.176                  ok            True                  False
  MPWR           83.78               37            0.94              9.36       1421.00                55.33         0.538          pass              0.400             21.7                           0.240                7.25              0.592                  ok            True                  False
  PCAR           95.65               23            1.25              1.14        130.57                29.70         0.537          pass              0.608             22.5                           0.391               -3.24             -0.206                  ok            True                  False
  CTSH           87.18               39            0.60              0.25         58.09                52.45         0.515          pass              0.672             78.5                           0.361                7.33              0.753                  ok            True                  False
   BKR           80.00               25            1.09              0.49         64.07                33.24         0.510          pass              0.333             60.7                           0.690                6.53              0.788                  ok            True                  False
  INSM           66.67               12            3.62              3.35        130.84               107.72         0.702          pass              0.096              4.1                           0.151               25.62              3.731                  ok           False                  False
  ISRG           87.80               41            0.09              0.24        401.17                69.94         0.667          pass              0.743             89.3                           0.725               13.58              1.349                  ok           False                  False
  WDAY           85.00               40            0.09              0.11        175.24                68.78         0.614          pass              0.673             92.7                           0.369                4.24              1.144                  ok           False                  False
  AMZN           84.44               45            0.19              0.36        267.13                61.57         0.609          pass              0.589             70.0                           0.329               13.28              0.462                  ok           False                  False
   TRI           87.80               41            0.26              0.19        102.53                74.92         0.608          pass              0.750             93.6                           0.449                3.55              0.393                  ok           False                  False
  NXPI           74.36               39            0.12              0.20        233.33                51.39         0.567          pass              0.452             67.4                           0.334               -4.91              0.085                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-13T11:35:08.590651-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:30:06.832547-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:25:05.233989-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:20:08.326885-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:15:07.600567-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:10:09.886626-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:05:09.901418-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T11:00:08.468855-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:55:08.693001-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-13T10:50:06.656727-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260813113508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260813113508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260813113508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260813113508)

</details>
