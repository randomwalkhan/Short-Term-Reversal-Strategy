# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 13:00:04 EST`
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
  ODFL           84.62               26            1.17              1.41        170.67                44.14         0.516          pass              0.498             72.3                           0.648                0.74             -0.011                                 ok            True                  False
  UPRO           79.31               29            1.27              1.06        119.28                94.72         0.635          pass              0.407             72.4                           0.656              -13.31             -2.371 downtrend_blocked_slope_and_streak           False                  False
  INTC           57.14                7            7.64              3.19         58.29               154.63         0.611          pass              0.138             25.5                           0.375               -5.21             -1.032 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           77.78               27            0.94              1.85        281.31                61.35         0.582          pass              0.341             56.3                           0.694               -2.76             -0.746            downtrend_blocked_slope           False                  False
   CEG           85.71               14            2.64              4.65        249.73                65.44         0.581          pass              0.311             24.7                           0.277               -8.33             -1.418 downtrend_blocked_slope_and_streak           False                  False
  ASML           70.00               10            3.23             31.25       1370.39                73.86         0.581          pass              0.173             38.2                           0.581              -11.19             -1.557 downtrend_blocked_slope_and_streak           False                  False
   BKR           81.48               27            0.85              0.27         45.92                56.59         0.580          pass              0.388             58.9                           0.543               -4.44             -0.816 downtrend_blocked_slope_and_streak           False                  False
  GOOG           79.31               29            0.86              1.68        278.81                58.63         0.567          pass              0.355             57.2                           0.668               -2.74             -0.719            downtrend_blocked_slope           False                  False
  SHOP           84.09               44            0.06              0.06        134.27                71.17         0.553          pass              0.656             97.3                           0.624               -8.45             -1.502 downtrend_blocked_slope_and_streak           False                  False
  AVGO           58.33               12            3.19              7.01        310.55                86.52         0.547          pass              0.177             36.4                           0.547               -8.57             -1.195            downtrend_blocked_slope           False                  False
  NVDA           75.00                4            7.01              8.10        161.58               126.24         0.543          pass              0.116             20.5                           0.486               -9.13             -1.616 downtrend_blocked_slope_and_streak           False                  False
  LRCX           66.67                6            6.45              9.48        205.70               114.43         0.516          pass              0.141             29.9                           0.588              -11.77             -1.845 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124130004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124130004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124130004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124130004)

</details>
