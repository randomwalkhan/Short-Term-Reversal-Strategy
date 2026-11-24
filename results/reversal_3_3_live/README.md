# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 14:45:05 EST`
Last processed slot: `manual`

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
  ODFL           86.21               29            1.03              1.23        170.74                44.14         0.509          pass              0.570             75.8                           0.596                0.89             -0.004                                 ok            True                  False
  UPRO           80.00               20            1.90              1.60        119.06                94.72         0.651          pass              0.307             58.5                           0.548              -13.87             -2.400 downtrend_blocked_slope_and_streak           False                  False
  INTC           57.14                7            7.03              2.94         58.40               154.63         0.649          pass              0.159             31.5                           0.505               -4.58             -1.002 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           70.59               17            1.61              3.19        280.73                61.35         0.593          pass              0.181             25.0                           0.287               -3.42             -0.777            downtrend_blocked_slope           False                  False
  ASML           70.00               10            3.10             30.08       1370.89                73.86         0.589          pass              0.180             40.5                           0.516              -11.08             -1.551 downtrend_blocked_slope_and_streak           False                  False
  GOOG           73.68               19            1.50              2.94        278.27                58.63         0.582          pass              0.194             25.3                           0.279               -3.37             -0.749            downtrend_blocked_slope           False                  False
  ABNB           90.70               43            0.01              0.01        173.95                57.35         0.569          pass              0.839             98.8                           0.549               -6.93             -0.812 downtrend_blocked_slope_and_streak           False                  False
   BKR           84.85               33            0.51              0.16         45.97                56.59         0.568          pass              0.565             75.3                           0.626               -4.11             -0.801 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71               14            2.86              5.04        249.56                65.44         0.567          pass              0.291             18.4                           0.228               -8.54             -1.428 downtrend_blocked_slope_and_streak           False                  False
   AEP          100.00               25            0.07              0.06        127.16                17.59         0.549          pass              0.831             92.1                           0.485               -0.58             -0.245                                 ok           False                  False
  AVGO           61.54               13            3.12              6.85        310.62                86.52         0.549          pass              0.189             37.9                           0.448               -8.50             -1.191            downtrend_blocked_slope           False                  False
  SHOP           72.73               22            2.24              2.11        133.40                71.17         0.536          pass              0.155              7.1                           0.211              -10.45             -1.602 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124144505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124144505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124144505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124144505)

</details>
