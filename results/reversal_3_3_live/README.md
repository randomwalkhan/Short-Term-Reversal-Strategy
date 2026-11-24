# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 10:50:05 EST`
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
  QCOM           75.00               20            2.43              2.81        164.18                82.33         0.622          pass              0.218             29.8                           0.288               -7.01             -1.185 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           75.00               20            1.34              2.65        280.96                61.35         0.599          pass              0.216             29.8                           0.261               -3.16             -0.765            downtrend_blocked_slope           False                  False
  UPRO           57.14                7            3.71              3.11        118.41                94.72         0.592          pass              0.117             19.3                           0.177              -15.45             -2.484 downtrend_blocked_slope_and_streak           False                  False
  FAST          100.00                9            1.21              0.44         51.87                27.50         0.587          pass              0.468              3.1                           0.100               -6.22             -0.882 downtrend_blocked_slope_and_streak           False                  False
  GOOG           72.73               22            1.25              2.45        278.48                58.63         0.580          pass              0.229             30.3                           0.269               -3.12             -0.737            downtrend_blocked_slope           False                  False
   CEG           87.50               16            2.51              4.42        249.82                65.44         0.578          pass              0.383             28.4                           0.286               -8.21             -1.412 downtrend_blocked_slope_and_streak           False                  False
   BKR           64.29               14            1.85              0.60         45.78                56.59         0.575          pass              0.116             10.5                           0.227               -5.40             -0.862 downtrend_blocked_slope_and_streak           False                  False
   MAR           92.86               14            1.04              3.03        414.33                26.32         0.574          pass              0.427              0.0                           0.151               -3.80             -0.436            downtrend_blocked_slope           False                  False
   AEP          100.00               25            0.10              0.09        127.15                17.59         0.547          pass              0.820             88.6                           0.447               -0.61             -0.246                                 ok           False                  False
  DASH           82.00               50            0.01              0.01        161.35                67.28         0.538          pass              0.606             99.6                           0.485               -9.49             -1.326 downtrend_blocked_slope_and_streak           False                  False
  SBUX           89.66               29            0.52              0.39        106.19                36.16         0.537          pass              0.602             54.8                           0.355               -3.20             -0.367            downtrend_blocked_slope           False                  False
  ASML           66.67                6            4.46             43.19       1365.27                73.86         0.530          pass              0.066              4.2                           0.135              -12.32             -1.615 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-24T10:50:05.812111-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:45:04.516238-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:40:03.078484-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:35:04.492903-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:30:05.555375-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:25:04.538326-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:20:05.785262-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:15:05.531160-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:10:06.086559-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T10:05:05.632379-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124105005)

</details>
