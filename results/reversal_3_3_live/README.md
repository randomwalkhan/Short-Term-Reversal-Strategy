# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-24 12:20:05 EDT`
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
  ALNY           83.33               30            1.35              2.23        235.26               131.78         0.800          pass              0.477             58.2                           0.562                7.40              0.747                                 ok            True                  False
  TEAM           83.78               37            0.53              0.64        171.54               117.34         0.782          pass              0.561             67.1                           0.369               12.53              1.351                                 ok            True                  False
  LRCX           85.71               28            2.43              5.35        311.71                88.60         0.609          pass              0.492             52.9                           0.575               -0.01             -0.285                                 ok            True                  False
  GEHC           97.06               34            0.75              0.39         74.65                48.71         0.587          pass              0.714             31.7                           0.438                1.81              0.257                                 ok            True                  False
  ASML           87.10               31            0.98             12.15       1758.55                48.84         0.554          pass              0.547             54.0                           0.589                0.75             -0.248                                 ok            True                  False
  REGN          100.00               24            0.98              5.73        831.59                30.64         0.536          pass              0.616             23.2                           0.436                2.32              0.461                                 ok            True                  False
  MRVL           80.00               30            3.31              5.48        234.69                96.35         0.510          pass              0.343             52.9                           0.639                9.90              1.320                                 ok            True                  False
  PCAR          100.00               28            0.77              0.71        130.73                25.90         0.507          pass              0.600              9.8                           0.247               -0.67             -0.172                                 ok            True                  False
   WDC           90.00               20            4.95             15.93        452.61               100.71         0.502          pass              0.512             43.0                           0.662               -0.38              0.126                                 ok            True                  False
  INSM           83.78               37            1.07              0.95        125.36               110.84         0.764          pass              0.518             53.4                           0.344               -7.67             -0.611 downtrend_blocked_slope_and_streak           False                  False
  AMAT           89.29               28            1.86              6.42        489.57                82.60         0.647          pass              0.585             50.8                           0.617               -7.36             -0.973            downtrend_blocked_slope           False                  False
   APP           67.57               37            1.69              3.62        304.22                90.15         0.621          pass              0.355             37.5                           0.323              -11.33             -0.687            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260824122005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260824122005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260824122005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260824122005)

</details>
