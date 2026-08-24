# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 13:25:05 EDT`
Last processed slot: `manage_1330`

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
  ALNY           80.00               20            2.13              3.51        234.71               131.78         0.806          pass              0.250             34.2                           0.327                6.55              0.712                                 ok            True                  False
  GEHC           96.00               25            1.03              0.54         74.59                48.71         0.623          pass              0.581              6.1                           0.246                1.52              0.244                                 ok            True                  False
  LRCX           84.00               25            2.78              6.10        311.38                88.60         0.605          pass              0.406             46.2                           0.529               -0.37             -0.301                                 ok            True                  False
  DXCM           87.88               33            0.77              0.50         92.13                49.72         0.567          pass              0.507             28.8                           0.389                4.54              0.263                                 ok            True                  False
  ASML           87.10               31            0.97             11.96       1758.63                48.84         0.554          pass              0.549             54.7                           0.576                0.76             -0.247                                 ok            True                  False
  REGN          100.00               26            0.93              5.42        831.72                30.64         0.527          pass              0.641             27.3                           0.399                2.38              0.463                                 ok            True                  False
  PCAR          100.00               24            1.07              0.98        130.61                25.90         0.513          pass              0.549              1.4                           0.215               -0.97             -0.186                                 ok            True                  False
  CPRT           82.61               23            1.64              0.39         33.63                47.97         0.507          pass              0.253             15.3                           0.350               12.35              1.752                                 ok            True                  False
  TEAM           83.78               37            0.42              0.50        171.59               117.34         0.786          pass              0.582             74.0                           0.536               12.66              1.356                                 ok           False                  False
  INSM           83.78               37            1.13              1.00        125.34               110.84         0.761          pass              0.510             50.9                           0.405               -7.72             -0.614 downtrend_blocked_slope_and_streak           False                  False
  AMAT           89.29               28            1.82              6.28        489.63                82.60         0.650          pass              0.588             51.9                           0.617               -7.33             -0.971            downtrend_blocked_slope           False                  False
   APP           66.67               36            2.10              4.49        303.84                90.15         0.602          pass              0.301             22.4                           0.245              -11.70             -0.706            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824132505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824132505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824132505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824132505)

</details>
