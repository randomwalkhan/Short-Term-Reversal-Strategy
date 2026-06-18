# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 11:55:04 EDT`
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

- Cash: `$26,514.50`
- Equity: `$26,514.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           85.71               28            0.74              0.61        117.87                34.58         0.556          pass              0.359             10.3                           0.237               -0.41              0.018                                 ok            True                  False
  CRWD           83.33               30            1.21              5.80        680.47                64.33         0.552          pass              0.465             62.4                           0.373               -6.18              0.037                                 ok            True                  False
   HON           80.00               30            0.61              0.97        228.19                41.75         0.544          pass              0.280             30.6                           0.170                4.40              0.813                                 ok            True                  False
  MDLZ           94.44               18            1.06              0.45         60.67                21.28         0.533          pass              0.574             27.5                           0.433               -1.27             -0.163                                 ok            True                  False
  VRTX           93.33               15            1.65              5.31        456.71                24.55         0.508          pass              0.473             11.2                           0.256                2.19              0.296                                 ok            True                  False
    ZS           77.14               35            1.26              1.10        123.91               152.31         0.865          pass              0.448             65.0                           0.515               -9.20             -0.565 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.71              0.12         23.15                27.50         0.703          pass              0.605             45.0                           0.641                4.37              0.401                                 ok           False                  False
  INTU           69.23               26            1.97              3.71        267.49                98.62         0.684          pass              0.314             46.2                           0.320              -12.65             -1.299 downtrend_blocked_slope_and_streak           False                  False
   TRI           78.57               28            0.55              0.30         79.12                52.51         0.586          pass              0.419             80.0                           0.658               -8.08             -0.797 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            1.79              4.29        339.82                27.62         0.572          pass              0.200             17.9                           0.349               -2.91             -0.124           downtrend_blocked_streak           False                  False
  PAYX          100.00               28            0.16              0.11         97.53                31.76         0.565          pass              0.847             90.1                           0.743               -2.07             -0.159                                 ok           False                  False
  TEAM           88.10               42            0.62              0.37         84.23                82.55         0.559          pass              0.712             80.0                           0.377              -17.37             -1.867 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-18T11:55:04.331586-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:50:03.235877-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:45:01.152442-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:40:06.149608-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:35:05.166451-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:30:05.153206-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:25:04.328726-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:20:05.337026-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:15:05.288880-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:10:05.442470-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618115504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618115504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618115504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618115504)

</details>
