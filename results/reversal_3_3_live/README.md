# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 13:30:06 EDT`
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
  SNPS           68.75               16            1.68              5.36        452.28                54.29         0.586            pass              0.229             43.3                           0.418              -11.53             -1.367 downtrend_blocked_slope_and_streak           False                  False
   CEG           86.96               23            1.57              2.89        261.95                59.49         0.571            pass              0.400             23.7                           0.162              -13.76             -1.470 downtrend_blocked_slope_and_streak           False                  False
   KDP           96.77               31            0.10              0.02         34.45                30.22         0.549            pass              0.856             87.0                           0.460               10.58              1.319                                 ok           False                  False
  META           81.82               11            1.88              9.30        701.45                40.24         0.537            pass              0.245             45.5                           0.626               -6.32             -0.384 downtrend_blocked_slope_and_streak           False                  False
  DRAM           81.08               37            0.27              0.09         48.29                49.05         0.494 below_threshold              0.539             93.7                           0.804              -19.02             -2.649 downtrend_blocked_slope_and_streak           False                  False
  DASH           87.80               41            0.63              0.85        193.16                49.82         0.485 below_threshold              0.639             60.9                           0.597               -0.68             -0.106                                 ok           False                  False
   LIN           72.22               18            0.92              3.25        502.05                13.47         0.477 below_threshold              0.195             31.2                           0.385                1.80              0.363                                 ok           False                  False
  CSCO           91.89               37            0.10              0.08        106.47                35.33         0.476 below_threshold              0.817             90.8                           0.754               -9.79             -1.156 downtrend_blocked_slope_and_streak           False                  False
  CDNS           80.00               30            1.05              2.39        324.84                37.22         0.476 below_threshold              0.369             62.7                           0.579              -10.32             -1.261 downtrend_blocked_slope_and_streak           False                  False
  ALNY           82.93               41            0.63              1.02        232.85                43.08         0.463 below_threshold              0.491             55.5                           0.525                3.52              0.386                                 ok           False                  False
   WMT           89.47               38            0.27              0.23        118.60                25.19         0.459 below_threshold              0.648             54.2                           0.548               10.42              1.113                                 ok           False                  False
 GOOGL           85.19               27            0.81              1.95        343.34                22.41         0.457 below_threshold              0.351             17.9                           0.396               -1.81             -0.236                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020133006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020133006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020133006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020133006)

</details>
