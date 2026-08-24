# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 12:40:04 EDT`
Last processed slot: `manage_1230`

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
  ALNY           84.00               25            1.70              2.80        235.02               131.78         0.807          pass              0.430             47.5                           0.373                7.02              0.732                                 ok            True                  False
  TEAM           82.86               35            0.97              1.17        171.31               117.34         0.771          pass              0.439             39.5                           0.201               12.03              1.330                                 ok            True                  False
  GEHC           96.30               27            0.94              0.49         74.61                48.71         0.617          pass              0.617             14.0                           0.289                1.61              0.248                                 ok            True                  False
  LRCX           84.62               26            2.58              5.67        311.57                88.60         0.611          pass              0.441             50.1                           0.543               -0.16             -0.292                                 ok            True                  False
  DXCM           88.57               35            0.62              0.40         92.17                49.72         0.566          pass              0.542             30.1                           0.177                4.70              0.270                                 ok            True                  False
  ASML           86.67               30            1.00             12.29       1758.49                48.84         0.558          pass              0.528             53.5                           0.565                0.73             -0.249                                 ok            True                  False
  REGN          100.00               21            1.14              6.66        831.19                30.64         0.546          pass              0.560             10.7                           0.231                2.16              0.454                                 ok            True                  False
  CPRT           85.00               20            1.89              0.45         33.61                47.97         0.513          pass              0.258              2.3                           0.186               12.06              1.740                                 ok            True                  False
  PCAR          100.00               28            0.87              0.80        130.69                25.90         0.501          pass              0.589              6.1                           0.196               -0.77             -0.177                                 ok            True                  False
  INSM           83.78               37            1.09              0.96        125.36               110.84         0.763          pass              0.516             52.8                           0.417               -7.68             -0.612 downtrend_blocked_slope_and_streak           False                  False
  AMAT           89.29               28            1.89              6.52        489.53                82.60         0.646          pass              0.582             50.1                           0.588               -7.39             -0.974            downtrend_blocked_slope           False                  False
  WDAY           82.50               40            0.18              0.26        199.90                82.42         0.639          pass              0.604             91.3                           0.407                8.39              0.937                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-24T12:00:04.404720-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:55:01.402592-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:50:02.380511-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:45:05.900318-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:40:01.544592-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:35:02.435409-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:30:05.214831-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:25:01.307994-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:20:05.923954-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:15:03.452955-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824124004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824124004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824124004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824124004)

</details>
