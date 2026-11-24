# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 11:10:04 EST`
Last processed slot: `manage_1100`

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
  UPRO           57.14                7            3.23              2.71        118.58                94.72         0.622          pass              0.151             29.6                           0.248              -15.03             -2.462 downtrend_blocked_slope_and_streak           False                  False
  QCOM           79.17               24            2.13              2.46        164.32                82.33         0.621          pass              0.271             38.5                           0.290               -6.73             -1.171 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           70.59               17            1.63              3.22        280.72                61.35         0.592          pass              0.178             24.1                           0.286               -3.44             -0.778            downtrend_blocked_slope           False                  False
  GOOG           73.68               19            1.49              2.91        278.28                58.63         0.583          pass              0.197             26.1                           0.303               -3.35             -0.748            downtrend_blocked_slope           False                  False
   BKR           73.68               19            1.48              0.48         45.84                56.59         0.579          pass              0.203             28.4                           0.398               -5.05             -0.845 downtrend_blocked_slope_and_streak           False                  False
   MAR           94.12               17            0.79              2.30        414.64                26.32         0.570          pass              0.599             39.5                           0.324               -3.55             -0.424            downtrend_blocked_slope           False                  False
   CEG           90.91               22            2.14              3.77        250.10                65.44         0.567          pass              0.545             39.0                           0.347               -7.86             -1.395 downtrend_blocked_slope_and_streak           False                  False
  SHOP           84.09               44            0.11              0.11        134.25                71.17         0.549          pass              0.650             95.3                           0.441               -8.50             -1.504 downtrend_blocked_slope_and_streak           False                  False
  PANW           80.95               42            0.47              1.15        352.94                70.38         0.545          pass              0.527             82.5                           0.664                7.79              0.987                                 ok           False                  False
  DASH           81.25               48            0.14              0.16        161.28                67.28         0.541          pass              0.562             91.5                           0.500               -9.61             -1.333 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00               19            0.94              0.34         51.91                27.50         0.540          pass              0.595             26.9                           0.332               -5.96             -0.869 downtrend_blocked_slope_and_streak           False                  False
  SBUX           89.29               28            0.60              0.45        106.17                36.16         0.538          pass              0.565             47.9                           0.262               -3.28             -0.371            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-24T11:10:04.431868-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:05:06.530028-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:00:06.064942-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:55:05.583055-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:50:05.812111-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:45:04.516238-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:40:03.078484-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:35:04.492903-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:30:05.555375-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:25:04.538326-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124111004)

</details>
