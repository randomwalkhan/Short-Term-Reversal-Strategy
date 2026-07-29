# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 11:40:04 EDT`
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

- Cash: `$34,954.75`
- Equity: `$34,954.75`
- Realized PnL: `$24,954.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00052500    129          2026-07-28         2026-07-29        1.425      1.2825 -1838.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST          100.00               11            1.29              0.43         47.91                27.18         0.588          pass              0.561             31.9                           0.326                4.37              0.455                                 ok            True                  False
   XEL          100.00               14            0.93              0.52         80.11                19.80         0.574          pass              0.598             38.0                           0.518               -0.74              0.104                                 ok            True                  False
   CSX           95.83               24            0.54              0.19         50.76                28.82         0.547          pass              0.637             29.5                           0.260                2.30              0.302                                 ok            True                  False
   MAR          100.00               23            1.04              2.80        382.32                28.18         0.539          pass              0.684             47.7                           0.312                4.50              0.392                                 ok            True                  False
  ISRG           75.00               20            1.54              3.91        360.12                72.57         0.651          pass              0.242             36.6                           0.273               -8.42             -0.893                                 ok           False                  False
  META           91.43               35            0.71              2.93        592.15                53.87         0.585          pass              0.651             40.3                           0.431              -13.52             -1.522 downtrend_blocked_slope_and_streak           False                  False
  TMUS           90.91               33            0.57              0.73        182.08                56.22         0.572          pass              0.668             55.6                           0.473               -3.34             -0.872            downtrend_blocked_slope           False                  False
   EXC           96.77               31            0.10              0.03         47.30                23.57         0.527          pass              0.855             87.5                           0.680                0.74              0.234                                 ok           False                  False
  MSTR           75.00               40            1.02              0.69         95.87                69.55         0.527          pass              0.280              9.3                           0.152               -2.35             -0.086                                 ok           False                  False
   CEG           68.75               32            0.83              1.51        259.17                41.76         0.506          pass              0.288             30.3                           0.331               -0.18              0.484                                 ok           False                  False
  ASML           95.24               21            2.29             25.41       1572.06                55.40         0.504          pass              0.651             42.3                           0.272              -14.69             -1.262 downtrend_blocked_slope_and_streak           False                  False
  PCAR          100.00                9            2.23              2.16        137.29                29.38         0.504          pass              0.455              1.6                           0.063                9.03              1.013                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-29T11:40:04.512640-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:35:01.518792-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:30:04.462568-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:25:01.480196-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:20:05.598758-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:15:04.531641-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:10:04.418819-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:05:04.380925-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T11:00:05.486916-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-29T10:55:01.499037-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729114004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729114004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729114004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729114004)

</details>
