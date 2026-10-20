# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 15:25:06 EDT`
Last processed slot: `manage_1530`

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
  SNPS           76.19               21            1.37              4.37        452.71                54.29         0.582            pass              0.293             53.7                           0.590              -11.25             -1.353 downtrend_blocked_slope_and_streak           False                  False
   CEG           87.50               24            1.35              2.49        262.12                59.49         0.578            pass              0.454             34.2                           0.377              -13.57             -1.460 downtrend_blocked_slope_and_streak           False                  False
  META           80.00               10            2.26             11.15        700.66                40.24         0.519            pass              0.156             34.7                           0.334               -6.68             -0.401 downtrend_blocked_slope_and_streak           False                  False
   WMT           85.19               27            0.64              0.54        118.47                25.19         0.498 below_threshold              0.316              5.0                           0.253               10.01              1.096                                 ok           False                  False
  DRAM           83.87               31            0.90              0.30         48.20                49.05         0.494 below_threshold              0.529             78.9                           0.629              -19.53             -2.678 downtrend_blocked_slope_and_streak           False                  False
  GOOG           83.33               12            1.54              3.67        338.59                21.64         0.493 below_threshold              0.155              1.1                           0.094               -2.81             -0.299            downtrend_blocked_slope           False                  False
 GOOGL           84.62               13            1.55              3.72        342.58                22.41         0.491 below_threshold              0.195              0.9                           0.088               -2.54             -0.270            downtrend_blocked_slope           False                  False
  CDNS           80.77               26            1.26              2.87        324.63                37.22         0.488 below_threshold              0.341             55.1                           0.446              -10.51             -1.271 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.43               28            0.48              1.80        532.75                21.83         0.484 below_threshold              0.768             66.5                           0.430                0.31              0.075                                 ok           False                  False
  DASH           88.64               44            0.41              0.55        193.29                49.82         0.482 below_threshold              0.703             74.7                           0.438               -0.45             -0.095                                 ok           False                  False
  CSCO           91.89               37            0.03              0.02        106.49                35.33         0.480 below_threshold              0.836             97.1                           0.726               -9.73             -1.153 downtrend_blocked_slope_and_streak           False                  False
  NFLX           73.33               15            1.69              0.83         69.50                27.22         0.473 below_threshold              0.140             19.6                           0.336               -0.03              0.025                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-10-20T15:10:05.817672-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T15:05:04.338456-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T15:00:02.391381-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T14:55:05.300060-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T14:50:06.260078-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-10-20T14:50:06.260078-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-20", "training_samples": 6130, "window": 5}
2026-10-20T12:00:03.885046-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:40:09.833456-04:00 early_entry_1140 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:35:07.546342-04:00 early_entry_1135 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:30:04.347725-04:00 early_entry_1130 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020152506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020152506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020152506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020152506)

</details>
