# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 15:00:02 EDT`
Last processed slot: `entry_1500`

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
  SNPS           73.68               19            1.48              4.71        452.56                54.29         0.585            pass              0.269             50.1                           0.534              -11.35             -1.358 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.50               24            1.49              2.75        262.01                59.49         0.570            pass              0.432             27.4                           0.318              -13.70             -1.467 downtrend_blocked_slope_and_streak           False                  False
  META           80.00               10            2.25             11.12        700.68                40.24         0.520            pass              0.157             34.9                           0.343               -6.67             -0.401 downtrend_blocked_slope_and_streak           False                  False
  DRAM           80.00               35            0.60              0.20         48.24                49.05         0.485 below_threshold              0.473             85.9                           0.636              -19.29             -2.664 downtrend_blocked_slope_and_streak           False                  False
  GOOG           80.00               15            1.34              3.20        338.79                21.64         0.484 below_threshold              0.097              5.1                           0.167               -2.61             -0.290            downtrend_blocked_slope           False                  False
 GOOGL           81.25               16            1.34              3.23        342.80                22.41         0.483 below_threshold              0.140              6.3                           0.183               -2.33             -0.260            downtrend_blocked_slope           False                  False
  CDNS           79.31               29            1.20              2.74        324.68                37.22         0.472 below_threshold              0.345             57.1                           0.359              -10.46             -1.268 downtrend_blocked_slope_and_streak           False                  False
  NFLX           76.47               17            1.56              0.76         69.52                27.22         0.472 below_threshold              0.165             23.8                           0.327                0.10              0.031                                 ok           False                  False
   LIN           77.27               22            0.72              2.52        502.36                13.47         0.471 below_threshold              0.267             46.7                           0.552                2.02              0.373                                 ok           False                  False
  ALNY           78.12               32            1.27              2.08        232.40                43.08         0.470 below_threshold              0.256             20.8                           0.314                2.85              0.356                                 ok           False                  False
   WMT           88.24               34            0.49              0.41        118.53                25.19         0.469 below_threshold              0.481             18.3                           0.222               10.19              1.103                                 ok           False                  False
  AAPL           85.71               21            0.92              2.21        341.99                16.04         0.467 below_threshold              0.413             46.7                           0.380                1.84              0.208                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-10-20T15:00:02.391381-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T14:55:05.300060-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T14:50:06.260078-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-10-20T14:50:06.260078-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-20", "training_samples": 6130, "window": 5}
2026-10-20T12:00:03.885046-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:40:09.833456-04:00 early_entry_1140 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:35:07.546342-04:00 early_entry_1135 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:30:04.347725-04:00 early_entry_1130 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:25:10.020404-04:00 early_entry_1125 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:20:08.949800-04:00 early_entry_1120 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020150002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020150002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020150002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020150002)

</details>
