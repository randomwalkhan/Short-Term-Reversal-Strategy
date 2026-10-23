# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 11:10:05 EDT`
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

- Cash: `$73,431.80`
- Equity: `$142,031.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-2,800.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 68600.0        17.85          17.15      223.97        225.38          bid_ask_mid                      17.15                bid_ask_mid                    True         -2800.0                  -3.92         100.0               38              0.68         80.16           75.78                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           94.44               18            0.98              0.24         35.09                27.06         0.548          pass              0.648             51.4                           0.571                9.71              0.918                                 ok            True                  False
 CMCSA           90.00               10            1.06              0.17         22.77                23.88         0.537          pass              0.456             45.1                           0.258                9.38              1.037                                 ok            True                  False
   EXC           80.00               15            0.97              0.30         44.72                20.91         0.532          pass              0.187             33.6                           0.523                6.36              0.571                                 ok            True                  False
  REGN           80.00               15            1.70              9.74        814.91                31.70         0.531          pass              0.153             22.1                           0.408                7.85              0.837                                 ok            True                  False
   KHC           85.71               21            1.14              0.20         25.00                34.71         0.530          pass              0.419             46.7                           0.710               11.38              1.105                                 ok            True                  False
   WMT           83.33               18            0.91              0.77        120.79                23.20         0.529          pass              0.294             32.9                           0.483                7.79              0.754                                 ok            True                  False
  AMGN           81.82               22            1.01              3.17        445.92                28.21         0.519          pass              0.290             36.6                           0.659                6.72              0.744                                 ok            True                  False
  ORLY          100.00               13            1.58              1.01         91.57                17.78         0.517          pass              0.491              6.5                           0.256                4.74              0.602                                 ok            True                  False
   AEP           86.36               22            0.75              0.69        130.35                17.81         0.505          pass              0.381             26.9                           0.425                5.58              0.486                                 ok            True                  False
   CEG           82.86               35            0.62              1.10        254.74                65.49         0.589          pass              0.542             80.2                           0.750              -14.91             -1.668 downtrend_blocked_slope_and_streak           False                  False
   CSX           71.43                7            1.54              0.56         51.43                26.41         0.540          pass              0.190             45.4                           0.749                7.65              0.635                                 ok           False                  False
   WDC           76.09               46            0.12              0.30        354.06                71.39         0.537          pass              0.546             97.5                           0.591              -10.96             -0.875 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-23T11:10:05.113003-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                   {"contract_symbol": "TRI261218C00125000", "current_drop_pct": 0.52, "early_entry_score": 0.776, "early_reclaim_pct": 73.8, "entry_ask": 8.3, "entry_bid": 7.1, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 36715.9, "hypothetical_contracts": 47, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 133.0, "option_spread_pct": 15.58, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.78, "shadow_only": true, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.776, "early_reclaim_pct": 73.8, "matched_signals": 38, "recovery_stability_score": 0.78, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-23T11:05:04.249585-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                {"contract_symbol": "TRI261218C00120000", "current_drop_pct": 0.64, "early_entry_score": 0.757, "early_reclaim_pct": 67.6, "entry_ask": 10.6, "entry_bid": 9.0, "entry_mode": "early", "entry_option_price": 9.8, "hypothetical_budget": 36715.9, "hypothetical_contracts": 37, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 242.0, "option_spread_pct": 16.33, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.716, "shadow_only": true, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.757, "early_reclaim_pct": 67.6, "matched_signals": 38, "recovery_stability_score": 0.716, "success_rate": 92.11, "ticker": "TRI", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-23T11:00:04.428143-04:00 early_entry_1100 early_entry_shadow       {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.64, "early_entry_score": 0.8, "early_reclaim_pct": 61.5, "entry_ask": 1.9, "entry_bid": 1.7, "entry_mode": "early", "entry_option_price": 1.8, "hypothetical_budget": 36715.9, "hypothetical_contracts": 203, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1606.0, "option_spread_pct": 11.11, "option_volume": 39.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.8, "early_reclaim_pct": 61.5, "matched_signals": 36, "recovery_stability_score": 0.75, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.419, "trend_health_status": "ok"}, {"current_drop_pct": 0.5, "early_entry_score": 0.764, "early_reclaim_pct": 60.1, "matched_signals": 41, "recovery_stability_score": 0.604, "success_rate": 92.68, "ticker": "TTWO", "timing_score": 0.453, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-23T10:55:02.008027-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.65, "early_entry_score": 0.796, "early_reclaim_pct": 60.3, "entry_ask": 1.8, "entry_bid": 1.7, "entry_mode": "early", "entry_option_price": 1.75, "hypothetical_budget": 36715.9, "hypothetical_contracts": 209, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1606.0, "option_spread_pct": 5.71, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.699, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.796, "early_reclaim_pct": 60.3, "matched_signals": 36, "recovery_stability_score": 0.699, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.758, "early_reclaim_pct": 60.2, "matched_signals": 40, "recovery_stability_score": 0.584, "success_rate": 92.5, "ticker": "WDAY", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-23T10:50:06.270815-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:45:06.482363-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:40:06.544410-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:35:06.665286-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:30:06.026140-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:25:06.029286-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023111005)

</details>
