# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 11:50:01 EDT`
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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   AEP           83.33               12            0.96              0.83        122.98                16.49         0.524            pass              0.231             25.6                           0.413               -0.13              0.053                                 ok            True                  False
   KHC           92.31               13            0.59              0.10         24.56                26.10         0.577            pass              0.566             53.2                           0.486               -3.32             -0.462            downtrend_blocked_slope           False                  False
  SNPS           69.23               13            2.60              7.24        394.28                60.55         0.575            pass              0.112             11.5                           0.366              -12.56             -1.252            downtrend_blocked_slope           False                  False
   EXC          100.00                6            1.23              0.37         43.00                14.68         0.548            pass              0.471              5.4                           0.143               -2.04             -0.105           downtrend_blocked_streak           False                  False
 CMCSA           96.97               33            0.14              0.02         25.19                34.99         0.530            pass              0.869             87.5                           0.737               -7.00             -0.817 downtrend_blocked_slope_and_streak           False                  False
  NVDA           90.91               11            3.00              4.58        216.33                43.68         0.525            pass              0.440             30.1                           0.638               -2.56             -0.157           downtrend_blocked_streak           False                  False
   CSX           78.57               14            0.94              0.32         48.81                18.07         0.510            pass              0.178             33.3                           0.402               -5.18             -0.347            downtrend_blocked_slope           False                  False
  CDNS           73.68               19            2.15              4.35        287.51                43.36         0.490 below_threshold              0.173             21.4                           0.349              -16.81             -1.866 downtrend_blocked_slope_and_streak           False                  False
  UPRO           88.46               26            1.15              1.19        147.51                26.03         0.487 below_threshold              0.544             54.2                           0.776               -3.60             -0.321 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.55               29            0.44              0.30         98.61                21.82         0.485 below_threshold              0.634             19.4                           0.274               -8.85             -1.023 downtrend_blocked_slope_and_streak           False                  False
   XEL           90.48               21            1.01              0.54         75.27                16.49         0.477 below_threshold              0.440             13.1                           0.263               -2.24             -0.107                                 ok           False                  False
  ABNB           94.74               38            0.20              0.24        170.09                31.21         0.474 below_threshold              0.861             77.9                           0.581              -10.34             -1.191 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-14T11:50:01.134863-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.85, "early_entry_score": 0.777, "early_reclaim_pct": 64.9, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.777, "early_reclaim_pct": 64.9, "matched_signals": 31, "recovery_stability_score": 0.577, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:45:04.190429-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.71, "early_entry_score": 0.813, "early_reclaim_pct": 70.4, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.572, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.813, "early_reclaim_pct": 70.4, "matched_signals": 34, "recovery_stability_score": 0.572, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}, {"current_drop_pct": 1.43, "early_entry_score": 0.671, "early_reclaim_pct": 81.0, "matched_signals": 34, "recovery_stability_score": 0.937, "success_rate": 88.24, "ticker": "STX", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:40:05.469838-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                              {"contract_symbol": "STX261016C00850000", "current_drop_pct": 1.33, "early_entry_score": 0.676, "early_reclaim_pct": 82.4, "entry_ask": 45.3, "entry_bid": 40.7, "entry_mode": "early", "entry_option_price": 43.0, "hypothetical_budget": 38058.05, "hypothetical_contracts": 8, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 147.0, "option_spread_pct": 10.7, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.94, "shadow_only": true, "success_rate": 88.24, "ticker": "STX", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 1.33, "early_entry_score": 0.676, "early_reclaim_pct": 82.4, "matched_signals": 34, "recovery_stability_score": 0.94, "success_rate": 88.24, "ticker": "STX", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-14T11:35:05.164573-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:30:05.695481-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:25:05.217490-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:20:05.740603-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.83, "early_entry_score": 0.779, "early_reclaim_pct": 65.5, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.779, "early_reclaim_pct": 65.5, "matched_signals": 31, "recovery_stability_score": 0.551, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:15:01.136676-04:00 early_entry_1115 early_entry_shadow   {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.74, "early_entry_score": 0.803, "early_reclaim_pct": 69.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.598, "shadow_only": true, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.803, "early_reclaim_pct": 69.3, "matched_signals": 33, "recovery_stability_score": 0.598, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "trend_health_status": "ok"}, {"current_drop_pct": 0.6, "early_entry_score": 0.712, "early_reclaim_pct": 84.2, "matched_signals": 36, "recovery_stability_score": 0.754, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:10:05.058091-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                     {"contract_symbol": "ALNY261016C00250000", "current_drop_pct": 0.53, "early_entry_score": 0.731, "early_reclaim_pct": 85.9, "entry_ask": 12.3, "entry_bid": 11.1, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 38058.05, "hypothetical_contracts": 32, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 838.0, "option_spread_pct": 10.26, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 89.19, "ticker": "ALNY", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.731, "early_reclaim_pct": 85.9, "matched_signals": 37, "recovery_stability_score": 0.736, "success_rate": 89.19, "ticker": "ALNY", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:05:02.179238-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914115001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914115001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914115001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914115001)

</details>
