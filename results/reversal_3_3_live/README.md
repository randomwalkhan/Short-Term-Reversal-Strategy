# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 15:40:03 EDT`
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
   CEG           87.50               24            1.41              2.59        262.08                59.49         0.575            pass              0.446             31.6                           0.357              -13.62             -1.463 downtrend_blocked_slope_and_streak           False                  False
  SNPS           82.76               29            0.81              2.58        453.48                54.29         0.574            pass              0.476             72.7                           0.763              -10.74             -1.327 downtrend_blocked_slope_and_streak           False                  False
  META           77.78                9            2.40             11.86        700.36                40.24         0.515            pass              0.143             30.5                           0.310               -6.82             -0.408 downtrend_blocked_slope_and_streak           False                  False
  DRAM           83.33               30            0.98              0.33         48.19                49.05         0.494 below_threshold              0.502             76.9                           0.540              -19.60             -2.682 downtrend_blocked_slope_and_streak           False                  False
  GOOG           84.62               13            1.48              3.52        338.65                21.64         0.492 below_threshold              0.221              9.6                           0.203               -2.74             -0.296            downtrend_blocked_slope           False                  False
 GOOGL           85.71               14            1.51              3.63        342.63                22.41         0.488 below_threshold              0.258             10.1                           0.185               -2.50             -0.268            downtrend_blocked_slope           False                  False
  MSFT           96.30               27            0.52              1.95        532.68                21.83         0.487 below_threshold              0.753             63.7                           0.366                0.27              0.074                                 ok           False                  False
  DASH           88.10               42            0.59              0.80        193.19                49.82         0.482 below_threshold              0.653             63.1                           0.310               -0.64             -0.104                                 ok           False                  False
  CDNS           78.57               28            1.22              2.79        324.67                37.22         0.476 below_threshold              0.337             56.5                           0.438              -10.48             -1.269 downtrend_blocked_slope_and_streak           False                  False
  CSCO           92.11               38            0.02              0.01        106.49                35.33         0.475 below_threshold              0.852             98.3                           0.655               -9.72             -1.152 downtrend_blocked_slope_and_streak           False                  False
  AVGO           82.50               40            0.08              0.18        334.51                36.85         0.472 below_threshold              0.593             93.1                           0.482              -11.04             -1.320            downtrend_blocked_slope           False                  False
  NFLX           71.43               14            1.81              0.89         69.47                27.22         0.470 below_threshold              0.115             13.9                           0.351               -0.15              0.019                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020154003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020154003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020154003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020154003)

</details>
