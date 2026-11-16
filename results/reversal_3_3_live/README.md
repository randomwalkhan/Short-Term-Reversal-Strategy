# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 11:30:04 EST`
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

- Cash: `$117,024.80`
- Equity: `$117,024.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TXN           83.33               12            2.09              4.43        301.70                58.41         0.591          pass              0.326             54.8                           0.725               -1.57              0.100                      ok            True                  False
   CEG           88.24               34            0.96              1.88        278.97                61.55         0.569          pass              0.613             58.8                           0.627                7.71              1.253                      ok            True                  False
  ISRG           91.43               35            0.65              2.03        442.72                45.74         0.551          pass              0.678             50.5                           0.388                0.87             -0.268                      ok            True                  False
  DXCM           82.35               34            0.98              0.57         83.08                50.11         0.535          pass              0.344             22.6                           0.280               -2.65             -0.419                      ok            True                  False
   HON           82.76               29            0.65              1.00        222.03                32.11         0.530          pass              0.295             14.1                           0.275               -0.92              0.014                      ok            True                  False
  NXPI           96.43               28            1.40              2.60        263.98                48.08         0.506          pass              0.768             65.6                           0.758                1.61              0.353                      ok            True                  False
  ALNY           71.43               28            1.71              1.97        164.20               110.81         0.729          pass              0.325             44.1                           0.708                2.67              0.170                      ok           False                  False
  INTC           63.64               11            6.01              2.51         58.58               143.21         0.673          pass              0.124             16.6                           0.447               -6.49              0.130                      ok           False                  False
  FTNT           77.78               27            2.03              1.81        126.45                93.31         0.671          pass              0.290             36.6                           0.475               -1.24              0.038                      ok           False                  False
  UPRO           80.00                5            3.04              2.95        137.24                68.17         0.629          pass              0.155             30.6                           0.428               -3.49             -0.107                      ok           False                  False
   BKR           63.64               11            2.06              0.71         49.13                57.94         0.608          pass              0.171             34.6                           0.512               -8.29             -0.524 downtrend_blocked_slope           False                  False
   ADI           70.00               10            2.59              7.21        394.88                66.18         0.598          pass              0.179             39.7                           0.615               -6.10             -0.161                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T11:30:04.371241-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:25:06.045979-05:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "entry_ask": 11.05, "entry_bid": 10.65, "entry_mode": "early", "entry_option_price": 10.85, "hypothetical_budget": 58512.4, "hypothetical_contracts": 53, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 3.69, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "matched_signals": 37, "recovery_stability_score": 0.58, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T11:20:06.269332-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:15:03.556110-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:10:05.513008-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:05:06.280493-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:00:05.564099-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "entry_ask": 10.9, "entry_bid": 10.45, "entry_mode": "early", "entry_option_price": 10.675, "hypothetical_budget": 58512.4, "hypothetical_contracts": 54, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.22, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "matched_signals": 38, "recovery_stability_score": 0.789, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:55:01.591806-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:50:02.516929-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:45:04.401367-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116113004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116113004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116113004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116113004)

</details>
