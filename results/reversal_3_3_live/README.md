# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 10:45:03 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$57,703.00`
- Equity: `$57,703.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ALNY           80.95               21            2.02              3.35        234.79               131.78         0.807          pass              0.291             37.4                           0.447                6.66              0.716                                 ok            True                  False
  LRCX           82.61               23            3.19              7.01        311.00                88.60         0.591          pass              0.330             38.3                           0.742               -0.79             -0.320                                 ok            True                  False
  ASML           85.71               28            1.30             16.03       1756.89                48.84         0.552          pass              0.446             39.4                           0.474                0.43             -0.263                                 ok            True                  False
  REGN          100.00               24            0.98              5.70        831.60                30.64         0.538          pass              0.587             13.4                           0.269                2.33              0.461                                 ok            True                  False
  INSM           87.50               48            0.14              0.12        125.72               110.84         0.759          pass              0.758             94.0                           0.917               -6.79             -0.569 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.00               25            2.63              9.05        488.44                82.60         0.620          pass              0.467             30.7                           0.518               -8.09             -1.009            downtrend_blocked_slope           False                  False
   APP           66.67               36            2.12              4.54        303.83                90.15         0.601          pass              0.298             21.6                           0.260              -11.71             -0.707            downtrend_blocked_slope           False                  False
  GEHC           97.37               38            0.32              0.17         74.75                48.71         0.592          pass              0.774             42.9                           0.298                2.25              0.277                                 ok           False                  False
  UPRO           76.67               30            0.79              0.83        149.53                39.04         0.558          pass              0.317             42.7                           0.606               -4.05             -0.481            downtrend_blocked_slope           False                  False
  MCHP           83.33               24            3.19              1.69         74.90                69.56         0.555          pass              0.272             11.6                           0.320              -10.04             -0.863            downtrend_blocked_slope           False                  False
  CSCO           85.71               35            0.74              0.57        110.79                42.43         0.542          pass              0.532             52.9                           0.691              -10.08             -1.160            downtrend_blocked_slope           False                  False
   HON           84.00               25            0.83              1.25        215.36                30.43         0.535          pass              0.368             36.1                           0.439              -11.60             -1.095 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-24T10:45:03.371554-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:40:01.398782-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:35:01.378502-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:30:01.238985-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:25:06.425653-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:20:01.387196-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:15:01.389030-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:10:01.316901-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:05:05.120136-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:00:02.345614-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824104503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824104503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824104503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824104503)

</details>
