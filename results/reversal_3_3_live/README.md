# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-24 11:45:01 EDT`
Last processed slot: `early_entry_1145`

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
  SOXL           93.10               29            1.24              2.01        230.56               242.24         0.953          pass              0.794             74.3                           0.439               13.32              2.450                                 ok            True                  False
    MU           90.32               31            1.33              9.81       1047.57               131.92         0.742          pass              0.605             38.7                           0.382               10.88              1.828                                 ok            True                  False
  MRVL          100.00               21            3.27              6.39        276.30               157.48         0.731          pass              0.657             36.9                           0.301                1.14              0.797                                 ok            True                  False
  KLAC           90.00               20            2.05              3.51        242.98                93.06         0.706          pass              0.482             26.2                           0.270               11.93              1.274                                 ok            True                  False
  LRCX           96.30               27            0.88              2.28        370.35                85.65         0.638          pass              0.850             91.1                           0.507               12.58              1.470                                 ok            True                  False
  ASML           96.88               32            0.80              9.90       1774.22                65.60         0.637          pass              0.822             70.6                           0.721               -0.76              0.151                                 ok            True                   True
  MCHP           93.33               30            0.68              0.44         93.07                72.77         0.634          pass              0.741             62.9                           0.395                1.27              0.571                                 ok            True                  False
  PANW           91.18               34            1.23              2.50        289.84                56.69         0.540          pass              0.651             46.2                           0.505               10.30              0.920                                 ok            True                  False
  NXPI           93.10               29            1.26              2.65        298.80                63.85         0.513          pass              0.670             47.7                           0.238               -0.42              0.337                                 ok            True                  False
   TXN           94.12               34            0.15              0.32        304.22                65.59         0.620          pass              0.867             89.4                           0.407                5.29              0.910                                 ok           False                  False
   APP           87.50               40            0.77              2.53        465.94                74.04         0.552          pass              0.649             64.5                           0.379              -11.03             -0.958 downtrend_blocked_slope_and_streak           False                  False
  CDNS           94.59               37            0.43              1.13        378.57                55.93         0.513          pass              0.855             78.3                           0.551               -3.44             -0.180                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-06-24T11:45:01.165602-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                   {"contract_symbol": "ASML260724C01765000", "current_drop_pct": 0.8, "early_entry_score": 0.822, "early_reclaim_pct": 70.6, "entry_ask": 128.5, "entry_bid": 118.4, "entry_mode": "early", "entry_option_price": 123.45, "hypothetical_budget": 15306.25, "hypothetical_contracts": 1, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 8.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.822, "early_reclaim_pct": 70.6, "matched_signals": 32, "recovery_stability_score": 0.721, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:40:02.100349-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                  {"contract_symbol": "ASML260724C01765000", "current_drop_pct": 0.86, "early_entry_score": 0.814, "early_reclaim_pct": 68.1, "entry_ask": 127.9, "entry_bid": 117.3, "entry_mode": "early", "entry_option_price": 122.6, "hypothetical_budget": 15306.25, "hypothetical_contracts": 1, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 8.65, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.725, "shadow_only": true, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.632, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.814, "early_reclaim_pct": 68.1, "matched_signals": 32, "recovery_stability_score": 0.725, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.632, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:35:01.113114-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                     {"contract_symbol": "ASML260724C01765000", "current_drop_pct": 0.81, "early_entry_score": 0.82, "early_reclaim_pct": 70.0, "entry_ask": 131.6, "entry_bid": 118.6, "entry_mode": "early", "entry_option_price": 125.1, "hypothetical_budget": 15306.25, "hypothetical_contracts": 1, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 7.0, "option_spread_pct": 10.39, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.71, "shadow_only": true, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.636, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.82, "early_reclaim_pct": 70.0, "matched_signals": 32, "recovery_stability_score": 0.71, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.636, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:30:02.288213-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "SOXL260731C00230000", "current_drop_pct": 0.57, "early_entry_score": 0.85, "early_reclaim_pct": 88.2, "entry_ask": 57.0, "entry_bid": 54.4, "entry_mode": "early", "entry_option_price": 55.7, "hypothetical_budget": 15306.25, "hypothetical_contracts": 2, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 89.0, "option_spread_pct": 4.67, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.56, "shadow_only": true, "success_rate": 93.33, "ticker": "SOXL", "timing_score": 0.961, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.85, "early_reclaim_pct": 88.2, "matched_signals": 30, "recovery_stability_score": 0.56, "success_rate": 93.33, "ticker": "SOXL", "timing_score": 0.961, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.84, "early_reclaim_pct": 74.4, "matched_signals": 33, "recovery_stability_score": 0.7, "success_rate": 96.97, "ticker": "ASML", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:25:04.327397-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T11:20:05.200537-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T11:15:03.335760-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                  {"contract_symbol": "LRCX260731C00370000", "current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.2, "entry_ask": 42.45, "entry_bid": 39.15, "entry_mode": "early", "entry_option_price": 40.8, "hypothetical_budget": 15306.25, "hypothetical_contracts": 3, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 87.0, "option_spread_pct": 8.09, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.619, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.2, "matched_signals": 33, "recovery_stability_score": 0.562, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.619, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:10:02.276540-04:00 early_entry_1110 early_entry_shadow       {"contract_symbol": "LRCX260724C00370000", "current_drop_pct": 0.53, "early_entry_score": 0.899, "early_reclaim_pct": 94.6, "entry_ask": 36.65, "entry_bid": 33.7, "entry_mode": "early", "entry_option_price": 35.175, "hypothetical_budget": 15306.25, "hypothetical_contracts": 4, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 114.0, "option_spread_pct": 8.39, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.591, "shadow_only": true, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.899, "early_reclaim_pct": 94.6, "matched_signals": 33, "recovery_stability_score": 0.591, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.622, "trend_health_status": "ok"}, {"current_drop_pct": 0.83, "early_entry_score": 0.774, "early_reclaim_pct": 65.7, "matched_signals": 33, "recovery_stability_score": 0.649, "success_rate": 93.94, "ticker": "NXPI", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:05:02.319682-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                         {"current_drop_pct": 0.58, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "entry_mode": "early", "error": "NXPI: no call expiries found in the 21-40 trading-day window.", "matched_signals": 34, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 94.12, "ticker": "NXPI", "timing_score": 0.529, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "matched_signals": 34, "recovery_stability_score": 0.731, "success_rate": 94.12, "ticker": "NXPI", "timing_score": 0.529, "trend_health_status": "ok"}, {"current_drop_pct": 0.95, "early_entry_score": 0.792, "early_reclaim_pct": 64.8, "matched_signals": 30, "recovery_stability_score": 0.748, "success_rate": 96.67, "ticker": "ASML", "timing_score": 0.639, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T11:00:02.279797-04:00 early_entry_1100 early_entry_shadow {"current_drop_pct": 0.53, "early_entry_score": 0.862, "early_reclaim_pct": 80.9, "entry_mode": "early", "error": "KLAC: no call expiries found in the 21-40 trading-day window.", "matched_signals": 35, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.83, "shadow_only": true, "success_rate": 94.29, "ticker": "KLAC", "timing_score": 0.712, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.862, "early_reclaim_pct": 80.9, "matched_signals": 35, "recovery_stability_score": 0.83, "success_rate": 94.29, "ticker": "KLAC", "timing_score": 0.712, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.825, "early_reclaim_pct": 71.6, "matched_signals": 32, "recovery_stability_score": 0.787, "success_rate": 96.88, "ticker": "ASML", "timing_score": 0.639, "trend_health_status": "ok"}, {"current_drop_pct": 0.52, "early_entry_score": 0.825, "early_reclaim_pct": 78.4, "matched_signals": 34, "recovery_stability_score": 0.706, "success_rate": 94.12, "ticker": "NXPI", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260624114501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260624114501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260624114501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260624114501)

</details>
