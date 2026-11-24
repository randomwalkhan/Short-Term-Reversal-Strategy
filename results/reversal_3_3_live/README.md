# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 10:40:03 EST`
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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  UPRO           70.00               10            2.76              2.31        118.75                94.72         0.648          pass              0.185             40.0                           0.304              -14.62             -2.440 downtrend_blocked_slope_and_streak           False                  False
  QCOM           78.57               28            1.35              1.57        164.71                82.33         0.643          pass              0.367             60.8                           0.613               -5.99             -1.135 downtrend_blocked_slope_and_streak           False                  False
  INTC           57.14                7            7.62              3.18         58.30               154.63         0.634          pass              0.081              5.9                           0.120               -5.19             -1.031 downtrend_blocked_slope_and_streak           False                  False
   BKR           73.68               19            1.30              0.42         45.86                56.59         0.594          pass              0.197             25.9                           0.233               -4.88             -0.837 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           76.00               25            1.19              2.36        281.09                61.35         0.579          pass              0.259             33.5                           0.261               -3.01             -0.758            downtrend_blocked_slope           False                  False
  ASML           62.50                8            3.71             35.89       1368.40                73.86         0.567          pass              0.076              6.4                           0.149              -11.63             -1.579 downtrend_blocked_slope_and_streak           False                  False
   MAR           94.74               19            0.77              2.24        414.67                26.32         0.565          pass              0.514              1.7                           0.091               -3.53             -0.424            downtrend_blocked_slope           False                  False
  GOOG           78.57               28            1.06              2.08        278.64                58.63         0.562          pass              0.292             38.5                           0.288               -2.94             -0.729            downtrend_blocked_slope           False                  False
  AVGO           61.54               13            3.05              6.69        310.69                86.52         0.556          pass              0.186             36.9                           0.459               -8.43             -1.188            downtrend_blocked_slope           False                  False
  NVDA           66.67                3            7.21              8.33        161.48               126.24         0.534          pass              0.084             10.2                           0.225               -9.32             -1.626 downtrend_blocked_slope_and_streak           False                  False
   CEG           90.00               30            1.86              3.28        250.32                65.44         0.533          pass              0.594             47.0                           0.466               -7.60             -1.381 downtrend_blocked_slope_and_streak           False                  False
  PANW           78.95               38            1.10              2.71        352.27                70.38         0.526          pass              0.416             58.9                           0.391                7.11              0.958                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-24T10:40:03.078484-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:35:04.492903-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:30:05.555375-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:25:04.538326-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:20:05.785262-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:15:05.531160-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:10:06.086559-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:05:05.632379-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:00:05.622595-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T09:20:05.669985-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124104003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124104003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124104003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124104003)

</details>
