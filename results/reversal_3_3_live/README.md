# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 12:55:01 EDT`
Last processed slot: `manage_1300`

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
  CRWD           82.76               29            1.24              5.91        680.43                64.33         0.557          pass              0.441             61.7                           0.430               -6.20              0.036                                 ok            True                  False
   WMT           86.21               29            0.69              0.57        117.88                34.58         0.553          pass              0.394             15.5                           0.237               -0.37              0.020                                 ok            True                  False
  MDLZ           95.24               21            0.97              0.41         60.68                21.28         0.518          pass              0.626             33.7                           0.484               -1.18             -0.158                                 ok            True                  False
  VRTX           94.74               19            1.31              4.22        457.18                24.55         0.503          pass              0.592             29.5                           0.410                2.54              0.312                                 ok            True                  False
    ZS           77.14               35            1.09              0.95        123.97               152.31         0.871          pass              0.463             69.9                           0.543               -9.04             -0.557 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.73              0.12         23.15                27.50         0.702          pass              0.600             43.3                           0.610                4.35              0.400                                 ok           False                  False
  INTU           69.23               26            2.00              3.77        267.47                98.62         0.682          pass              0.311             45.4                           0.423              -12.68             -1.301 downtrend_blocked_slope_and_streak           False                  False
  AMGN           85.71                7            1.57              3.77        340.05                27.62         0.583          pass              0.294             27.9                           0.463               -2.70             -0.114           downtrend_blocked_streak           False                  False
   TRI           77.27               22            1.32              0.74         78.93                52.51         0.573          pass              0.292             51.6                           0.365               -8.79             -0.832 downtrend_blocked_slope_and_streak           False                  False
  TEAM           86.11               36            1.27              0.75         84.07                82.55         0.553          pass              0.569             59.2                           0.321              -17.91             -1.896 downtrend_blocked_slope_and_streak           False                  False
  GILD           85.71                7            1.93              1.69        124.72                29.17         0.548          pass              0.267             19.9                           0.496               -4.13             -0.250 downtrend_blocked_slope_and_streak           False                  False
  WDAY           83.33               18            3.13              2.67        120.69                69.08         0.532          pass              0.231             12.0                           0.152              -20.21             -2.173 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-18T12:00:02.352957-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:55:04.331586-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:50:03.235877-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:45:01.152442-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:40:06.149608-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:35:05.166451-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:30:05.153206-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:25:04.328726-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:20:05.337026-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T11:15:05.288880-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618125501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618125501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618125501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618125501)

</details>
