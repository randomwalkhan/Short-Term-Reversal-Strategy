# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 11:30:05 EDT`
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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               18            0.81              2.49        435.92                27.65         0.586          pass              0.627             38.4                           0.496                5.00              0.540                      ok            True                  False
  FAST          100.00               12            1.46              0.52         50.91                21.07         0.543          pass              0.503             11.8                           0.258               -1.23             -0.099                      ok            True                  False
  REGN          100.00               10            1.58              8.96        803.87                24.94         0.540          pass              0.610             51.9                           0.384               -0.95             -0.030                      ok            True                  False
  CSCO           85.71               35            0.85              0.67        111.86                41.41         0.528          pass              0.501             43.1                           0.621               -0.43             -0.011                      ok            True                  False
  GILD          100.00               15            1.82              1.90        148.05                26.47         0.527          pass              0.508              7.2                           0.245                5.63              0.622                      ok            True                  False
  VRTX           97.14               35            0.52              1.99        546.70                32.96         0.515          pass              0.826             69.2                           0.632                7.70              0.668                      ok            True                   True
  NVDA           88.00               25            1.82              2.90        226.74                42.92         0.507          pass              0.401             12.3                           0.125               -0.59             -0.181                      ok            True                  False
  MNST           91.67               36            0.30              0.10         46.66               551.83         1.000          pass              0.755             56.9                           0.586               -0.56              0.169                      ok           False                  False
  INSM           73.33               15            2.64              2.25        120.43               110.68         0.773          pass              0.184             24.3                           0.287               -4.49             -0.603 downtrend_blocked_slope           False                  False
  DRAM           77.78               36            0.30              0.12         56.78                68.22         0.612          pass              0.510             91.8                           0.682               -1.15             -0.228                      ok           False                  False
   STX           86.11               36            0.38              2.23        846.24                71.05         0.608          pass              0.652             85.0                           0.516              -13.30             -1.497 downtrend_blocked_slope           False                  False
  MCHP           88.89               27            1.70              0.90         75.11                63.59         0.606          pass              0.460             16.3                           0.238               -5.70             -0.689 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-08-28T11:30:05.095211-04:00 early_entry_1130 early_entry_shadow        {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.52, "early_entry_score": 0.826, "early_reclaim_pct": 69.2, "entry_ask": 26.9, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 25.55, "hypothetical_budget": 26394.05, "hypothetical_contracts": 10, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 34.0, "option_spread_pct": 10.57, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.515, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.826, "early_reclaim_pct": 69.2, "matched_signals": 35, "recovery_stability_score": 0.632, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.515, "trend_health_status": "ok"}, {"current_drop_pct": 0.96, "early_entry_score": 0.706, "early_reclaim_pct": 63.3, "matched_signals": 42, "recovery_stability_score": 0.66, "success_rate": 90.48, "ticker": "CDNS", "timing_score": 0.37, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:25:02.223727-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "ZS261002C00187500", "current_drop_pct": 0.54, "early_entry_score": 0.897, "early_reclaim_pct": 82.2, "entry_ask": 15.85, "entry_bid": 13.5, "entry_mode": "early", "entry_option_price": 14.675, "hypothetical_budget": 26394.05, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 16.01, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.888, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.502, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.897, "early_reclaim_pct": 82.2, "matched_signals": 42, "recovery_stability_score": 0.888, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.502, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:20:02.016207-04:00 early_entry_1120 early_entry_shadow             {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.96, "early_entry_score": 0.844, "early_reclaim_pct": 68.3, "entry_ask": 18.4, "entry_bid": 17.45, "entry_mode": "early", "entry_option_price": 17.925, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 5.3, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.815, "shadow_only": true, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.844, "early_reclaim_pct": 68.3, "matched_signals": 39, "recovery_stability_score": 0.815, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.827, "early_reclaim_pct": 69.5, "matched_signals": 35, "recovery_stability_score": 0.552, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:15:03.127521-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.95, "early_entry_score": 0.845, "early_reclaim_pct": 68.7, "entry_ask": 18.3, "entry_bid": 17.45, "entry_mode": "early", "entry_option_price": 17.875, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 4.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.826, "shadow_only": true, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.845, "early_reclaim_pct": 68.7, "matched_signals": 39, "recovery_stability_score": 0.826, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:10:06.058739-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:05:02.171965-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:00:04.200311-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "CDNS261016C00345000", "current_drop_pct": 1.04, "early_entry_score": 0.69, "early_reclaim_pct": 60.1, "entry_ask": 19.2, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 17.6, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 17.0, "option_spread_pct": 18.18, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.754, "shadow_only": true, "success_rate": 90.24, "ticker": "CDNS", "timing_score": 0.37, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.69, "early_reclaim_pct": 60.1, "matched_signals": 41, "recovery_stability_score": 0.754, "success_rate": 90.24, "ticker": "CDNS", "timing_score": 0.37, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.68, "early_reclaim_pct": 72.5, "matched_signals": 36, "recovery_stability_score": 0.819, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T10:55:06.098266-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NVDA261016C00225000", "current_drop_pct": 0.5, "early_entry_score": 0.689, "early_reclaim_pct": 75.7, "entry_ask": 11.8, "entry_bid": 11.75, "entry_mode": "early", "entry_option_price": 11.775, "hypothetical_budget": 26394.05, "hypothetical_contracts": 22, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 17410.0, "option_spread_pct": 0.42, "option_volume": 1301.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.819, "shadow_only": true, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.689, "early_reclaim_pct": 75.7, "matched_signals": 36, "recovery_stability_score": 0.819, "success_rate": 88.89, "ticker": "NVDA", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-28T10:50:01.894913-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T10:45:05.072825-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828113005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828113005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828113005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828113005)

</details>
