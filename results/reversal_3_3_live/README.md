# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-24 11:50:03 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$30,612.50`
- Equity: `$30,612.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           90.91               33            0.66              4.86       1049.69               131.92         0.769          pass              0.730             69.6                           0.607               11.64              1.859                                 ok            True                   True
  MRVL          100.00               23            2.62              5.11        276.85               157.48         0.758          pass              0.711             49.6                           0.428                1.82              0.828                                 ok            True                  False
  KLAC           90.48               21            1.99              3.41        243.03                93.06         0.705          pass              0.509             28.5                           0.248               12.01              1.277                                 ok            True                  False
  ASML           96.97               33            0.56              7.01       1775.46                65.60         0.646          pass              0.856             79.2                           0.736               -0.52              0.162                                 ok            True                   True
  LRCX           96.67               30            0.64              1.68        370.61                85.65         0.634          pass              0.877             93.5                           0.540               12.85              1.481                                 ok            True                  False
  NXPI           92.86               28            1.36              2.85        298.72                63.85         0.514          pass              0.646             43.9                           0.209               -0.52              0.333                                 ok            True                  False
  PANW           92.50               40            1.01              2.05        290.04                56.69         0.513          pass              0.752             55.9                           0.693               10.54              0.930                                 ok            True                  False
  SOXL           93.33               30            0.41              0.67        231.13               242.24         0.963          pass              0.859             91.4                           0.660               14.27              2.488                                 ok           False                  False
  MCHP           93.75               32            0.38              0.25         93.15                72.77         0.641          pass              0.815             79.3                           0.569                1.57              0.585                                 ok           False                  False
   TXN           94.12               34            0.06              0.13        304.31                65.59         0.626          pass              0.887             95.9                           0.458                5.39              0.914                                 ok           False                  False
   APP           87.50               40            0.79              2.58        465.92                74.04         0.551          pass              0.647             63.9                           0.356              -11.04             -0.958 downtrend_blocked_slope_and_streak           False                  False
  CDNS           94.74               38            0.26              0.70        378.76                55.93         0.518          pass              0.891             86.6                           0.578               -3.28             -0.172                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-24T11:50:03.210933-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "ASML260724C01770000", "current_drop_pct": 0.56, "early_entry_score": 0.856, "early_reclaim_pct": 79.2, "entry_ask": 127.0, "entry_bid": 112.0, "entry_mode": "early", "entry_option_price": 119.5, "hypothetical_budget": 15306.25, "hypothetical_contracts": 1, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 15.0, "option_spread_pct": 12.55, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 96.97, "ticker": "ASML", "timing_score": 0.646, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.856, "early_reclaim_pct": 79.2, "matched_signals": 33, "recovery_stability_score": 0.736, "success_rate": 96.97, "ticker": "ASML", "timing_score": 0.646, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.73, "early_reclaim_pct": 69.6, "matched_signals": 33, "recovery_stability_score": 0.607, "success_rate": 90.91, "ticker": "MU", "timing_score": 0.769, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:45:01.165602-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ASML260724C01765000", "current_drop_pct": 0.8, "early_entry_score": 0.822, "early_reclaim_pct": 70.6, "entry_ask": 128.5, "entry_bid": 118.4, "entry_mode": "early", "entry_option_price": 123.45, "hypothetical_budget": 15306.25, "hypothetical_contracts": 1, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 8.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.822, "early_reclaim_pct": 70.6, "matched_signals": 32, "recovery_stability_score": 0.721, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:40:02.100349-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "ASML260724C01765000", "current_drop_pct": 0.86, "early_entry_score": 0.814, "early_reclaim_pct": 68.1, "entry_ask": 127.9, "entry_bid": 117.3, "entry_mode": "early", "entry_option_price": 122.6, "hypothetical_budget": 15306.25, "hypothetical_contracts": 1, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 8.65, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.725, "shadow_only": true, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.632, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.814, "early_reclaim_pct": 68.1, "matched_signals": 32, "recovery_stability_score": 0.725, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.632, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:35:01.113114-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "ASML260724C01765000", "current_drop_pct": 0.81, "early_entry_score": 0.82, "early_reclaim_pct": 70.0, "entry_ask": 131.6, "entry_bid": 118.6, "entry_mode": "early", "entry_option_price": 125.1, "hypothetical_budget": 15306.25, "hypothetical_contracts": 1, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 10.39, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.71, "shadow_only": true, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.636, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.82, "early_reclaim_pct": 70.0, "matched_signals": 32, "recovery_stability_score": 0.71, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.636, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:30:02.288213-04:00 early_entry_1130 early_entry_shadow         {"contract_symbol": "SOXL260731C00230000", "current_drop_pct": 0.57, "early_entry_score": 0.85, "early_reclaim_pct": 88.2, "entry_ask": 57.0, "entry_bid": 54.4, "entry_mode": "early", "entry_option_price": 55.7, "hypothetical_budget": 15306.25, "hypothetical_contracts": 2, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 89.0, "option_spread_pct": 4.67, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.56, "shadow_only": true, "success_rate": 93.33, "ticker": "SOXL", "timing_score": 0.961, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.85, "early_reclaim_pct": 88.2, "matched_signals": 30, "recovery_stability_score": 0.56, "success_rate": 93.33, "ticker": "SOXL", "timing_score": 0.961, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.84, "early_reclaim_pct": 74.4, "matched_signals": 33, "recovery_stability_score": 0.7, "success_rate": 96.97, "ticker": "ASML", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:25:04.327397-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T11:20:05.200537-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T11:15:03.335760-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "LRCX260731C00370000", "current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.2, "entry_ask": 42.45, "entry_bid": 39.15, "entry_mode": "early", "entry_option_price": 40.8, "hypothetical_budget": 15306.25, "hypothetical_contracts": 3, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 87.0, "option_spread_pct": 8.09, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.619, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.2, "matched_signals": 33, "recovery_stability_score": 0.562, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.619, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:10:02.276540-04:00 early_entry_1110 early_entry_shadow               {"contract_symbol": "LRCX260724C00370000", "current_drop_pct": 0.53, "early_entry_score": 0.899, "early_reclaim_pct": 94.6, "entry_ask": 36.65, "entry_bid": 33.7, "entry_mode": "early", "entry_option_price": 35.175, "hypothetical_budget": 15306.25, "hypothetical_contracts": 4, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 114.0, "option_spread_pct": 8.39, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.591, "shadow_only": true, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.899, "early_reclaim_pct": 94.6, "matched_signals": 33, "recovery_stability_score": 0.591, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.622, "trend_health_status": "ok"}, {"current_drop_pct": 0.83, "early_entry_score": 0.774, "early_reclaim_pct": 65.7, "matched_signals": 33, "recovery_stability_score": 0.649, "success_rate": 93.94, "ticker": "NXPI", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:05:02.319682-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                 {"current_drop_pct": 0.58, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "entry_mode": "early", "error": "NXPI: no call expiries found in the 21-40 trading-day window.", "matched_signals": 34, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 94.12, "ticker": "NXPI", "timing_score": 0.529, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "matched_signals": 34, "recovery_stability_score": 0.731, "success_rate": 94.12, "ticker": "NXPI", "timing_score": 0.529, "trend_health_status": "ok"}, {"current_drop_pct": 0.95, "early_entry_score": 0.792, "early_reclaim_pct": 64.8, "matched_signals": 30, "recovery_stability_score": 0.748, "success_rate": 96.67, "ticker": "ASML", "timing_score": 0.639, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260624115003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260624115003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260624115003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260624115003)

</details>
