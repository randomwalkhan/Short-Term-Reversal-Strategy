# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 13:10:03 EDT`
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

- Cash: `$30,222.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           83.33               18            1.32              0.77         82.85                69.62         0.688          pass              0.251             13.4                           0.152               -1.96             -0.120                                 ok            True                  False
  CTSH           93.55               31            0.75              0.28         52.87                51.28         0.565          pass              0.726             56.0                           0.485                1.51             -0.115                                 ok            True                  False
  CDNS          100.00               10            2.82              7.78        390.91                58.79         0.561          pass              0.561             35.1                           0.535                0.36              0.381                                 ok            True                  False
   WMT           84.62               26            0.85              0.71        119.52                36.35         0.551          pass              0.377             30.6                           0.180                0.20              0.097                                 ok            True                  False
  TEAM           94.12               17            4.29              2.94         96.63                87.01         0.513          pass              0.561             28.8                           0.603               10.33              0.738                                 ok            True                  False
    ZS           57.14                7            5.16              4.67        127.25               157.94         0.794          pass              0.141             20.6                           0.491              -33.60             -1.958            downtrend_blocked_slope           False                  False
  INTU           54.55               11            4.33              9.25        301.54               100.92         0.607          pass              0.091              7.7                           0.306               -3.96             -0.641 downtrend_blocked_slope_and_streak           False                  False
  DRAM          100.00                8            4.33              1.83         59.73               103.58         0.581          pass              0.603             48.3                           0.640               -4.31             -0.433            downtrend_blocked_slope           False                  False
   ADI          100.00                6            2.77              7.83        400.54                49.72         0.566          pass              0.594             45.6                           0.632               -6.23             -0.360            downtrend_blocked_slope           False                  False
   CEG           75.00               28            1.33              2.33        249.67                55.25         0.556          pass              0.282             35.6                           0.459              -17.98             -1.880 downtrend_blocked_slope_and_streak           False                  False
  MSFT           66.67                3            2.69              7.76        408.42                36.13         0.554          pass              0.105             16.4                           0.391               -3.69             -0.406            downtrend_blocked_slope           False                  False
  ADSK           88.46               26            1.20              1.89        224.23                42.71         0.535          pass              0.498             37.3                           0.529               -6.67             -0.682            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-09T12:00:03.055569-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:55:04.019844-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:50:02.014967-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:45:02.008648-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:40:06.401362-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:35:02.395564-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:30:02.013445-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:25:01.954572-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:20:06.212106-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:15:02.033784-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609131003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609131003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609131003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609131003)

</details>
