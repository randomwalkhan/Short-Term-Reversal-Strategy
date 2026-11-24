# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 11:15:03 EST`
Last processed slot: `early_entry_1115`

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
  PANW           80.00               40            0.76              1.88        352.63                70.38         0.537          pass              0.468             71.5                           0.538                7.47              0.974                                 ok            True                  False
  QCOM           76.47               17            2.51              2.91        164.13                82.33         0.637          pass              0.193             27.4                           0.244               -7.09             -1.189 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           76.92               13            1.99              3.93        280.41                61.35         0.602          pass              0.102              7.4                           0.136               -3.79             -0.795            downtrend_blocked_slope           False                  False
  UPRO           66.67                6            3.86              3.23        118.35                94.72         0.601          pass              0.108             16.0                           0.188              -15.58             -2.491 downtrend_blocked_slope_and_streak           False                  False
  GOOG           80.00               15            1.81              3.53        278.02                58.63         0.596          pass              0.123             10.1                           0.160               -3.66             -0.763            downtrend_blocked_slope           False                  False
   BKR           73.68               19            1.39              0.45         45.85                56.59         0.585          pass              0.216             32.6                           0.495               -4.96             -0.841 downtrend_blocked_slope_and_streak           False                  False
   CEG           86.67               15            2.59              4.57        249.76                65.44         0.578          pass              0.347             26.1                           0.281               -8.29             -1.415 downtrend_blocked_slope_and_streak           False                  False
   MAR           94.12               17            0.81              2.35        414.62                26.32         0.569          pass              0.595             38.3                           0.351               -3.57             -0.425            downtrend_blocked_slope           False                  False
  SBUX           90.91               22            0.80              0.59        106.11                36.16         0.566          pass              0.520             30.9                           0.181               -3.47             -0.380            downtrend_blocked_slope           False                  False
  SHOP           80.00               35            0.87              0.82        133.95                71.17         0.552          pass              0.411             63.0                           0.320               -9.19             -1.539 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               22            0.86              0.31         51.93                27.50         0.525          pass              0.631             32.8                           0.428               -5.89             -0.866 downtrend_blocked_slope_and_streak           False                  False
  DASH           80.43               46            0.64              0.72        161.04                67.28         0.520          pass              0.450             62.1                           0.343              -10.06             -1.355 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-24T11:15:03.611406-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:10:04.431868-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:05:06.530028-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:00:06.064942-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:55:05.583055-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:50:05.812111-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:45:04.516238-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:40:03.078484-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:35:04.492903-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:30:05.555375-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124111503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124111503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124111503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124111503)

</details>
