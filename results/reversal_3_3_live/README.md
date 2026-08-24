# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 11:35:02 EDT`
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
  ALNY           85.29               34            1.03              1.70        235.49               131.78         0.799          pass              0.586             68.2                           0.762                7.75              0.762                                 ok            True                  False
  GEHC           96.67               30            0.87              0.46         74.62                48.71         0.605          pass              0.621              9.1                           0.179                1.69              0.252                                 ok            True                  False
  LRCX           84.00               25            2.91              6.40        311.26                88.60         0.597          pass              0.397             43.6                           0.724               -0.51             -0.307                                 ok            True                  False
  REGN          100.00               21            1.11              6.48        831.26                30.64         0.547          pass              0.567             13.0                           0.313                2.19              0.455                                 ok            True                  False
  ASML           85.19               27            1.51             18.65       1755.77                48.84         0.545          pass              0.394             29.4                           0.366                0.21             -0.272                                 ok            True                  False
  PCAR          100.00               31            0.54              0.50        130.82                25.90         0.505          pass              0.621             10.1                           0.100               -0.44             -0.161                                 ok            True                  False
  INSM           85.00               40            0.64              0.56        125.53               110.84         0.771          pass              0.628             72.4                           0.528               -7.26             -0.591 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.89               27            2.21              7.60        489.06                82.60         0.633          pass              0.539             41.8                           0.733               -7.69             -0.989            downtrend_blocked_slope           False                  False
   APP           69.23               39            1.32              2.82        304.56                90.15         0.633          pass              0.410             51.2                           0.678              -10.99             -0.670            downtrend_blocked_slope           False                  False
  MCHP           83.33               24            2.92              1.54         74.96                69.56         0.569          pass              0.308             22.9                           0.553               -9.79             -0.850            downtrend_blocked_slope           False                  False
  UPRO           76.67               30            0.71              0.75        149.56                39.04         0.563          pass              0.335             48.3                           0.589               -3.98             -0.478            downtrend_blocked_slope           False                  False
   HON           84.62               26            0.67              1.02        215.46                30.43         0.539          pass              0.428             48.2                           0.484              -11.46             -1.088 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-24T11:35:02.435409-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:30:05.214831-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:25:01.307994-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:20:05.923954-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:15:03.452955-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:10:01.504842-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:05:03.408199-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:00:02.496687-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:55:01.403337-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:50:01.400899-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824113502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824113502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824113502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824113502)

</details>
