# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 10:30:06 EDT`
Last processed slot: `manage_1030`

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
  SNPS           82.14               28            0.89              2.84        453.36                54.29         0.575            pass              0.445             70.0                           0.812              -10.82             -1.331 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.50               40            0.25              0.46        262.99                59.49         0.551            pass              0.719             87.9                           0.796              -12.60             -1.410 downtrend_blocked_slope_and_streak           False                  False
  META           85.71               14            1.47              7.27        702.32                40.24         0.547            pass              0.406             57.4                           0.824               -5.93             -0.365 downtrend_blocked_slope_and_streak           False                  False
  MSFT           93.55               31            0.32              1.20        533.00                21.83         0.473 below_threshold              0.781             77.6                           0.781                0.47              0.083                                 ok           False                  False
  CDNS           83.33               42            0.07              0.15        325.79                37.22         0.468 below_threshold              0.628             97.6                           0.941               -9.43             -1.216 downtrend_blocked_slope_and_streak           False                  False
  PANW           85.37               41            0.76              1.83        346.16                55.73         0.465 below_threshold              0.625             78.5                           0.808              -18.00             -2.178 downtrend_blocked_slope_and_streak           False                  False
  AMAT           76.32               38            0.50              1.45        412.49                46.44         0.465 below_threshold              0.489             85.3                           0.844              -22.48             -2.994 downtrend_blocked_slope_and_streak           False                  False
   LIN           81.48               27            0.54              1.92        502.62                13.47         0.462 below_threshold              0.294             31.5                           0.268                2.19              0.380                                 ok           False                  False
  CPRT           60.00               10            2.76              0.53         27.28                31.97         0.455 below_threshold              0.079             11.1                           0.171               -0.26              0.167                                 ok           False                  False
  IDXX           93.18               44            0.19              0.72        555.49                25.12         0.440 below_threshold              0.793             65.9                           0.371                7.64              1.020                                 ok           False                  False
  LRCX           76.92               39            0.63              1.20        271.68                43.91         0.431 below_threshold              0.493             85.5                           0.885              -18.99             -2.504 downtrend_blocked_slope_and_streak           False                  False
   BKR           92.11               38            0.63              0.25         55.70                25.31         0.419 below_threshold              0.732             60.2                           0.503               -2.92             -0.226                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-10-20T10:30:06.843333-04:00 early_entry_1030 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:25:04.152080-04:00 early_entry_1025 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:20:05.290913-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:15:05.434773-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:10:06.028828-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:05:04.298275-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:00:02.343877-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T09:50:06.258363-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "ADP261120C00290000", "fill_price": 11.2, "pnl": 13300.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.43, "ticker": "ADP"}
2026-10-20T00:00:06.202426-04:00     data_refresh       data_refresh                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-10-19T15:10:06.181493-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020103006)

</details>
