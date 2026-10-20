# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 12:00:03 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   ADP     option         option ADP261120C00290000     70          2026-10-19         2026-10-20          9.3        11.2 13300.0   20.430108 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           75.00               20            1.44              4.57        452.62                54.29         0.583            pass              0.280             51.6                           0.535              -11.31             -1.356 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71               35            0.65              1.20        262.68                59.49         0.552            pass              0.579             68.3                           0.596              -12.96             -1.428 downtrend_blocked_slope_and_streak           False                  False
  META           81.82               11            1.87              9.21        701.49                40.24         0.538            pass              0.247             46.0                           0.524               -6.31             -0.383 downtrend_blocked_slope_and_streak           False                  False
  DASH           88.64               44            0.28              0.38        193.37                49.82         0.500            pass              0.646             55.4                           0.420               -0.33             -0.090                                 ok           False                  False
  DRAM           78.95               38            0.25              0.08         48.29                49.05         0.487 below_threshold              0.518             94.2                           0.788              -19.00             -2.648 downtrend_blocked_slope_and_streak           False                  False
  CSCO           91.18               34            0.26              0.19        106.42                35.33         0.484 below_threshold              0.738             77.1                           0.467               -9.93             -1.163 downtrend_blocked_slope_and_streak           False                  False
  CDNS           79.31               29            1.13              2.58        324.76                37.22         0.476 below_threshold              0.354             59.7                           0.500              -10.39             -1.265 downtrend_blocked_slope_and_streak           False                  False
  MSFT           93.55               31            0.31              1.14        533.03                21.83         0.474 below_threshold              0.785             78.8                           0.759                0.49              0.083                                 ok           False                  False
   LIN           75.00               20            0.82              2.89        502.20                13.47         0.474 below_threshold              0.231             38.9                           0.531                1.91              0.368                                 ok           False                  False
  ALNY           85.42               48            0.07              0.11        233.24                43.08         0.467 below_threshold              0.660             89.6                           0.462                4.11              0.412                                 ok           False                  False
   WMT           88.89               36            0.38              0.32        118.56                25.19         0.467 below_threshold              0.464              2.2                           0.212               10.31              1.108                                 ok           False                  False
  DXCM           90.91               33            0.76              0.45         85.79                29.30         0.466 below_threshold              0.491              0.0                           0.170                2.33              0.278                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-20T12:00:03.885046-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:40:09.833456-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:35:07.546342-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:30:04.347725-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:25:10.020404-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:20:08.949800-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:15:05.273794-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:10:09.912817-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:05:06.503440-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:00:06.812644-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020120003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020120003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020120003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020120003)

</details>
