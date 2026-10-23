# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 11:15:05 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$73,431.80`
- Equity: `$142,031.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-2,800.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 68600.0        17.85          17.15      223.97        224.93          bid_ask_mid                      17.15                bid_ask_mid                    True         -2800.0                  -3.92         100.0               38              0.68         80.16           76.34                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           94.44               18            0.98              0.24         35.09                27.06         0.548          pass              0.648             51.4                           0.539                9.71              0.918                                 ok            True                  False
   WMT           83.33               18            0.88              0.74        120.80                23.20         0.530          pass              0.301             35.4                           0.521                7.82              0.756                                 ok            True                  False
   EXC           80.00               15            1.03              0.32         44.71                20.91         0.529          pass              0.176             29.8                           0.504                6.30              0.568                                 ok            True                  False
   KHC           85.71               21            1.20              0.21         25.00                34.71         0.526          pass              0.410             43.9                           0.681               11.32              1.103                                 ok            True                  False
  ORLY          100.00               13            1.59              1.02         91.56                17.78         0.516          pass              0.489              5.8                           0.233                4.73              0.601                                 ok            True                  False
   AEP           86.36               22            0.77              0.71        130.34                17.81         0.504          pass              0.374             24.6                           0.420                5.55              0.485                                 ok            True                  False
   CEG           82.86               35            0.61              1.09        254.74                65.49         0.590          pass              0.543             80.4                           0.715              -14.90             -1.668 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           88.89                9            1.18              0.19         22.76                23.88         0.535          pass              0.406             38.6                           0.224                9.24              1.031                                 ok           False                  False
   WDC           75.56               45            0.30              0.75        353.87                71.39         0.531          pass              0.534             93.7                           0.549              -11.12             -0.883 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           50.00                2            1.88              0.86         64.82                24.03         0.530          pass              0.128             24.8                           0.501                5.88              0.554                                 ok           False                  False
   CSX           70.00               10            1.38              0.50         51.46                26.41         0.529          pass              0.205             50.9                           0.773                7.82              0.643                                 ok           False                  False
   XEL           75.00               12            1.08              0.60         78.71                16.59         0.523          pass              0.117             17.0                           0.408                5.87              0.593                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-23T11:15:05.326587-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                              {"contract_symbol": "MAR261127C00395000", "current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 62.0, "entry_ask": 16.1, "entry_bid": 13.1, "entry_mode": "early", "entry_option_price": 14.6, "hypothetical_budget": 36715.9, "hypothetical_contracts": 25, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 20.55, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 91.67, "ticker": "MAR", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 62.0, "matched_signals": 36, "recovery_stability_score": 0.676, "success_rate": 91.67, "ticker": "MAR", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-23T11:10:05.113003-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                   {"contract_symbol": "TRI261218C00125000", "current_drop_pct": 0.52, "early_entry_score": 0.776, "early_reclaim_pct": 73.8, "entry_ask": 8.3, "entry_bid": 7.1, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 36715.9, "hypothetical_contracts": 47, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 133.0, "option_spread_pct": 15.58, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.78, "shadow_only": true, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.776, "early_reclaim_pct": 73.8, "matched_signals": 38, "recovery_stability_score": 0.78, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-23T11:05:04.249585-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                {"contract_symbol": "TRI261218C00120000", "current_drop_pct": 0.64, "early_entry_score": 0.757, "early_reclaim_pct": 67.6, "entry_ask": 10.6, "entry_bid": 9.0, "entry_mode": "early", "entry_option_price": 9.8, "hypothetical_budget": 36715.9, "hypothetical_contracts": 37, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 242.0, "option_spread_pct": 16.33, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.716, "shadow_only": true, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.757, "early_reclaim_pct": 67.6, "matched_signals": 38, "recovery_stability_score": 0.716, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-23T11:00:04.428143-04:00 early_entry_1100 early_entry_shadow       {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.64, "early_entry_score": 0.8, "early_reclaim_pct": 61.5, "entry_ask": 1.9, "entry_bid": 1.7, "entry_mode": "early", "entry_option_price": 1.8, "hypothetical_budget": 36715.9, "hypothetical_contracts": 203, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1606.0, "option_spread_pct": 11.11, "option_volume": 39.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.8, "early_reclaim_pct": 61.5, "matched_signals": 36, "recovery_stability_score": 0.75, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.419, "trend_health_status": "ok"}, {"current_drop_pct": 0.5, "early_entry_score": 0.764, "early_reclaim_pct": 60.1, "matched_signals": 41, "recovery_stability_score": 0.604, "success_rate": 92.68, "ticker": "TTWO", "timing_score": 0.453, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-23T10:55:02.008027-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.65, "early_entry_score": 0.796, "early_reclaim_pct": 60.3, "entry_ask": 1.8, "entry_bid": 1.7, "entry_mode": "early", "entry_option_price": 1.75, "hypothetical_budget": 36715.9, "hypothetical_contracts": 209, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1606.0, "option_spread_pct": 5.71, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.699, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.796, "early_reclaim_pct": 60.3, "matched_signals": 36, "recovery_stability_score": 0.699, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.758, "early_reclaim_pct": 60.2, "matched_signals": 40, "recovery_stability_score": 0.584, "success_rate": 92.5, "ticker": "WDAY", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-23T10:50:06.270815-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:45:06.482363-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:40:06.544410-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:35:06.665286-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:30:06.026140-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023111505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023111505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023111505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023111505)

</details>
