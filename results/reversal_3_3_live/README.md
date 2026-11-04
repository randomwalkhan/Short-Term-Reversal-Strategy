# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 15:05:06 EST`
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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           58.33               12            4.22              1.79         59.78               129.60         0.712            pass              0.182             32.4                           0.282              -37.61             -5.009            downtrend_blocked_slope           False                  False
  REGN           66.67                3            3.14             21.37        964.20                48.26         0.521            pass              0.089             12.3                           0.214               17.02              2.081                                 ok           False                  False
  AVGO           68.42               19            1.82              4.22        330.32                44.04         0.508            pass              0.237             42.0                           0.291               -3.46             -0.067                                 ok           False                  False
  NVDA           66.67               12            2.10              3.04        205.39                32.59         0.482 below_threshold              0.135             24.4                           0.179               -8.84             -0.750 downtrend_blocked_slope_and_streak           False                  False
   TXN           90.32               31            0.63              1.39        311.90                35.19         0.479 below_threshold              0.694             77.0                           0.465                9.62              1.052                                 ok           False                  False
  CSCO           86.11               36            0.16              0.11        102.92                32.31         0.477 below_threshold              0.643             86.3                           0.409               -4.15             -0.508 downtrend_blocked_slope_and_streak           False                  False
  ASML           66.67                3            4.02             43.64       1533.44                44.05         0.457 below_threshold              0.090             14.8                           0.169              -11.03             -0.627            downtrend_blocked_slope           False                  False
  CRWD           87.23               47            0.42              0.72        244.37                59.77         0.450 below_threshold              0.697             86.2                           0.560                1.80             -0.094                                 ok           False                  False
  DRAM           63.64               11            4.97              1.66         46.93                69.30         0.443 below_threshold              0.099             16.0                           0.179               -7.91             -0.255            downtrend_blocked_slope           False                  False
   ADI           60.00                5            3.58             10.53        415.28                38.61         0.409 below_threshold              0.145             34.7                           0.367               -0.30              0.499                                 ok           False                  False
  AMAT           50.00                8            4.72             12.61        376.52                58.39         0.401 below_threshold              0.052              3.9                           0.077              -11.01             -0.420            downtrend_blocked_slope           False                  False
  MCHP           71.43                7            4.06              2.22         76.95                45.40         0.396 below_threshold              0.122             27.3                           0.266               -3.13              0.136                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-11-04T15:05:06.426407-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:00:04.760681-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:55:04.187352-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:50:05.817314-05:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-11-04T14:50:05.817314-05:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-04", "training_samples": 6270, "window": 5}
2026-11-04T12:00:04.108894-05:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:55:06.127851-05:00 early_entry_1155 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:50:05.872989-05:00 early_entry_1150 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:45:05.372887-05:00 early_entry_1145 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:40:03.980969-05:00 early_entry_1140 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104150506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104150506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104150506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104150506)

</details>
