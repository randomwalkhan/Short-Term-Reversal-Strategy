# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 11:40:05 EST`
Last processed slot: `manage_1130`

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
  PANW           80.00               40            0.66              1.62        352.73                70.38         0.544          pass              0.480             75.4                           0.645                7.58              0.978                                 ok            True                  False
  QCOM           80.00               15            2.66              3.08        164.06                82.33         0.644          pass              0.167             23.0                           0.251               -7.24             -1.196 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           80.00               15            1.78              3.51        280.60                61.35         0.607          pass              0.146             17.4                           0.354               -3.58             -0.785            downtrend_blocked_slope           False                  False
  UPRO           66.67                6            3.90              3.27        118.34                94.72         0.598          pass              0.105             15.1                           0.266              -15.62             -2.493 downtrend_blocked_slope_and_streak           False                  False
  SBUX           85.71               14            1.17              0.87        105.99                36.16         0.587          pass              0.240              0.8                           0.056               -3.83             -0.396            downtrend_blocked_slope           False                  False
  GOOG           72.22               18            1.55              3.04        278.23                58.63         0.584          pass              0.180             22.8                           0.393               -3.41             -0.751            downtrend_blocked_slope           False                  False
  FAST          100.00               11            1.09              0.40         51.89                27.50         0.582          pass              0.510             14.9                           0.254               -6.11             -0.876 downtrend_blocked_slope_and_streak           False                  False
   BKR           73.68               19            1.46              0.47         45.84                56.59         0.581          pass              0.207             29.5                           0.363               -5.02             -0.844 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71               14            2.91              5.12        249.52                65.44         0.564          pass              0.287             17.1                           0.235               -8.58             -1.430 downtrend_blocked_slope_and_streak           False                  False
   MAR           95.00               20            0.70              2.04        414.75                26.32         0.558          pass              0.661             46.3                           0.507               -3.47             -0.420            downtrend_blocked_slope           False                  False
  SHOP           81.58               38            0.71              0.67        134.01                71.17         0.545          pass              0.493             69.8                           0.446               -9.05             -1.532 downtrend_blocked_slope_and_streak           False                  False
   HON           82.76               29            0.67              1.04        221.52                37.67         0.528          pass              0.440             62.5                           0.397               -3.09             -0.368           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-24T11:40:05.757709-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:35:05.562629-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:30:04.516511-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:25:06.575801-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:20:05.808543-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:15:03.611406-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:10:04.431868-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:05:06.530028-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:00:06.064942-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:55:05.583055-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124114005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124114005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124114005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124114005)

</details>
