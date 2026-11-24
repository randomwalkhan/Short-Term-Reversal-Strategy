# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 13:35:05 EST`
Last processed slot: `manage_1330`

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
  INTC           57.14                7            7.17              2.99         58.38               154.63         0.641          pass              0.155             30.2                           0.580               -4.72             -1.009 downtrend_blocked_slope_and_streak           False                  False
  UPRO           78.57               28            1.39              1.16        119.24                94.72         0.633          pass              0.393             69.8                           0.647              -13.41             -2.376 downtrend_blocked_slope_and_streak           False                  False
  ASML           66.67               12            2.91             28.21       1371.69                73.86         0.584          pass              0.204             44.2                           0.639              -10.90             -1.542 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71               14            2.69              4.75        249.69                65.44         0.577          pass              0.306             23.2                           0.309               -8.38             -1.420 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           77.78               27            1.12              2.20        281.16                61.35         0.571          pass              0.315             48.1                           0.515               -2.93             -0.754            downtrend_blocked_slope           False                  False
  GOOG           78.57               28            0.99              1.95        278.70                58.63         0.564          pass              0.328             50.5                           0.521               -2.87             -0.725            downtrend_blocked_slope           False                  False
   BKR           86.11               36            0.35              0.11         45.99                56.59         0.562          pass              0.642             83.2                           0.761               -3.96             -0.793 downtrend_blocked_slope_and_streak           False                  False
  AVGO           61.54               13            2.93              6.42        310.80                86.52         0.561          pass              0.201             41.7                           0.641               -8.32             -1.182            downtrend_blocked_slope           False                  False
  NVDA           75.00                4            6.73              7.78        161.72               126.24         0.561          pass              0.127             23.6                           0.603               -8.85             -1.602 downtrend_blocked_slope_and_streak           False                  False
  SHOP           80.65               31            1.31              1.23        133.77                71.17         0.550          pass              0.345             44.3                           0.216               -9.60             -1.559 downtrend_blocked_slope_and_streak           False                  False
  DASH           81.63               49            0.10              0.11        161.30                67.28         0.537          pass              0.580             94.1                           0.412               -9.57             -1.331 downtrend_blocked_slope_and_streak           False                  False
  CSCO           37.50                8            2.56              1.74         96.06                56.18         0.527          pass              0.173             40.0                           0.698               -3.90             -0.642            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124133505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124133505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124133505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124133505)

</details>
