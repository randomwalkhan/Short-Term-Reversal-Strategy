# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 13:05:06 EST`
Last processed slot: `manage_1300`

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
  ODFL           85.71               28            1.08              1.30        170.71                44.14         0.511          pass              0.547             74.5                           0.646                0.83             -0.006                                 ok            True                  False
  UPRO           78.57               28            1.38              1.16        119.24                94.72         0.633          pass              0.393             69.9                           0.656              -13.41             -2.376 downtrend_blocked_slope_and_streak           False                  False
  INTC           57.14                7            7.86              3.28         58.25               154.63         0.598          pass              0.130             23.4                           0.323               -5.44             -1.043 downtrend_blocked_slope_and_streak           False                  False
  ASML           70.00               10            3.17             30.73       1370.61                73.86         0.585          pass              0.176             39.2                           0.576              -11.14             -1.554 downtrend_blocked_slope_and_streak           False                  False
   BKR           80.77               26            0.87              0.28         45.92                56.59         0.584          pass              0.359             57.9                           0.495               -4.46             -0.817 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           77.78               27            1.05              2.07        281.21                61.35         0.575          pass              0.325             51.2                           0.656               -2.87             -0.751            downtrend_blocked_slope           False                  False
   CEG           85.71               14            2.83              4.99        249.58                65.44         0.568          pass              0.293             19.2                           0.219               -8.52             -1.427 downtrend_blocked_slope_and_streak           False                  False
  GOOG           78.57               28            0.96              1.87        278.73                58.63         0.566          pass              0.334             52.5                           0.627               -2.83             -0.724            downtrend_blocked_slope           False                  False
  AVGO           63.64               11            3.49              7.66        310.27                86.52         0.541          pass              0.152             30.5                           0.487               -8.85             -1.208            downtrend_blocked_slope           False                  False
  SHOP           83.72               43            0.34              0.32        134.16                71.17         0.540          pass              0.610             85.4                           0.568               -8.71             -1.515 downtrend_blocked_slope_and_streak           False                  False
  NVDA           66.67                3            7.19              8.31        161.49               126.24         0.527          pass              0.108             18.4                           0.353               -9.30             -1.625 downtrend_blocked_slope_and_streak           False                  False
  SBUX           88.89               36            0.08              0.06        106.33                36.16         0.519          pass              0.743             93.6                           0.829               -2.77             -0.347            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-24T12:00:06.462519-05:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:55:05.635523-05:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:50:06.028676-05:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:45:06.576648-05:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:40:05.757709-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:35:05.562629-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:30:04.516511-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:25:06.575801-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:20:05.808543-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:15:03.611406-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124130506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124130506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124130506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124130506)

</details>
