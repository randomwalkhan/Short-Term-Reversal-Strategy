# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 14:35:01 EDT`
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
   WMT           85.71               28            0.74              0.62        117.87                34.58         0.551          pass              0.430             34.1                           0.538               -0.42              0.018                                 ok            True                  False
  MDLZ           94.44               18            1.03              0.44         60.67                21.28         0.535          pass              0.581             29.8                           0.339               -1.24             -0.161                                 ok            True                  False
  INTU           73.33               30            1.58              2.98        267.80                98.62         0.688          pass              0.373             56.9                           0.523              -12.30             -1.281 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            1.27              0.21         23.11                27.50         0.668          pass              0.503             12.2                           0.268                3.78              0.375                                 ok           False                  False
   TRI           77.27               22            1.34              0.75         78.93                52.51         0.572          pass              0.290             50.9                           0.335               -8.81             -0.833 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            1.80              4.31        339.81                27.62         0.571          pass              0.203             19.1                           0.430               -2.92             -0.125           downtrend_blocked_streak           False                  False
  TEAM           87.80               41            0.75              0.44         84.20                82.55         0.557          pass              0.691             75.8                           0.577              -17.48             -1.873 downtrend_blocked_slope_and_streak           False                  False
  CRWD           87.50               40            0.33              1.59        682.28                64.33         0.547          pass              0.724             89.7                           0.633               -5.34              0.077                                 ok           False                  False
  GILD           85.71                7            1.98              1.74        124.71                29.17         0.545          pass              0.261             17.9                           0.401               -4.18             -0.252 downtrend_blocked_slope_and_streak           False                  False
   STX           97.37               38            0.21              1.59       1065.39                67.39         0.541          pass              0.845             68.0                           0.375               14.88              2.366                                 ok           False                  False
  WDAY           72.73               22            2.73              2.33        120.83                69.08         0.517          pass              0.201             23.1                           0.275              -19.88             -2.154 downtrend_blocked_slope_and_streak           False                  False
   BKR           70.00               10            2.21              0.93         59.67                38.86         0.515          pass              0.161             36.6                           0.551              -11.14             -0.859 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618143501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618143501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618143501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618143501)

</details>
