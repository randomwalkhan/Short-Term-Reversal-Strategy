# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 09:55:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           73.08               26            1.61              4.47        395.47                60.55         0.567            pass              0.251             29.3                           0.380              -11.66             -1.206            downtrend_blocked_slope           False                  False
  CHTR           90.48               42            0.23              0.23        145.67                68.13         0.554            pass              0.811             92.2                           0.588               -5.32             -0.865            downtrend_blocked_slope           False                  False
   EXC           94.44               18            0.28              0.08         43.12                14.68         0.532            pass              0.492              0.0                           0.275               -1.09             -0.061                                 ok           False                  False
  UPRO           93.75               16            1.71              1.77        147.26                26.03         0.520            pass              0.554             31.6                           0.639               -4.14             -0.347 downtrend_blocked_slope_and_streak           False                  False
  NVDA           80.00                5            3.48              5.32        216.01                43.68         0.520            pass              0.108             18.8                           0.416               -3.04             -0.180           downtrend_blocked_streak           False                  False
   AEP           91.30               23            0.49              0.43        123.15                16.49         0.498 below_threshold              0.583             48.2                           0.306                0.34              0.074                                 ok           False                  False
  MELI           97.22               36            0.57              7.54       1894.14                37.25         0.492 below_threshold              0.736             38.0                           0.347               -4.05             -0.494 downtrend_blocked_slope_and_streak           False                  False
  CDNS           71.43               21            1.94              3.93        287.69                43.36         0.490 below_threshold              0.191             23.0                           0.257              -16.64             -1.857 downtrend_blocked_slope_and_streak           False                  False
  ALNY           90.48               42            0.21              0.36        248.52                49.38         0.477 below_threshold              0.810             94.5                           0.545                4.66              0.261                                 ok           False                  False
   LIN           73.68               19            0.85              2.78        465.03                15.11         0.475 below_threshold              0.143             11.9                           0.142               -5.26             -0.647 downtrend_blocked_slope_and_streak           False                  False
   BKR           91.67               12            1.69              0.70         58.76                29.92         0.474 below_threshold              0.420             16.0                           0.196               -6.97             -0.808 downtrend_blocked_slope_and_streak           False                  False
  AMZN           69.57               23            1.41              2.53        255.70                26.09         0.465 below_threshold              0.254             40.1                           0.522               -4.98             -0.332 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-09-14T09:20:04.227328-04:00     data_refresh       data_refresh                                                                                                {'saved': 93}
2026-09-11T15:10:01.826868-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:05:01.876732-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T15:00:02.857606-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:55:03.823001-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-09-11T14:50:04.839039-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-09-11T14:50:04.839039-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-11", "training_samples": 5769, "window": 5}
2026-09-11T12:00:03.003315-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:55:01.842224-04:00 early_entry_1155 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:50:02.882708-04:00 early_entry_1150 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914095506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914095506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914095506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914095506)

</details>
