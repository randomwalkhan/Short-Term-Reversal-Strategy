# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 14:15:04 EDT`
Last processed slot: `manual`

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
   AEP           80.00               10            0.96              0.83        122.97                16.49         0.531            pass              0.128             24.9                           0.321               -0.14              0.053                                 ok            True                  False
  SNPS           63.64               11            2.70              7.50        394.17                60.55         0.574            pass              0.095             10.2                           0.267              -12.64             -1.257            downtrend_blocked_slope           False                  False
   KHC           91.67               12            0.79              0.14         24.54                26.10         0.570            pass              0.493             37.1                           0.266               -3.52             -0.471            downtrend_blocked_slope           False                  False
   EXC          100.00                8            0.98              0.30         43.03                14.68         0.550            pass              0.527             24.1                           0.364               -1.79             -0.094           downtrend_blocked_streak           False                  False
  CHTR           90.00               40            0.76              0.78        145.44                68.13         0.531            pass              0.741             73.8                           0.531               -5.83             -0.890            downtrend_blocked_slope           False                  False
 CMCSA           96.43               28            0.65              0.12         25.15                34.99         0.526            pass              0.731             52.9                           0.480               -7.48             -0.841 downtrend_blocked_slope_and_streak           False                  False
  NVDA           84.62               13            2.67              4.08        216.54                43.68         0.524            pass              0.309             37.8                           0.558               -2.23             -0.142           downtrend_blocked_streak           False                  False
  CDNS           63.64               11            2.56              5.19        287.15                43.36         0.499 below_threshold              0.102             15.1                           0.261              -17.17             -1.886 downtrend_blocked_slope_and_streak           False                  False
   CSX           83.33               24            0.45              0.15         48.88                18.07         0.487 below_threshold              0.435             68.1                           0.488               -4.71             -0.325            downtrend_blocked_slope           False                  False
   XEL           86.67               15            1.48              0.78         75.16                16.49         0.478 below_threshold              0.266              2.2                           0.148               -2.71             -0.129                                 ok           False                  False
  ALNY           90.48               42            0.21              0.36        248.52                49.38         0.477 below_threshold              0.810             94.5                           0.594                4.66              0.261                                 ok           False                  False
  UPRO           83.87               31            0.72              0.75        147.70                26.03         0.477 below_threshold              0.504             71.2                           0.601               -3.18             -0.302 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-14T12:00:04.262790-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.73, "early_entry_score": 0.804, "early_reclaim_pct": 69.6, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.804, "early_reclaim_pct": 69.6, "matched_signals": 33, "recovery_stability_score": 0.663, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:55:01.111232-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.8, "early_entry_score": 0.783, "early_reclaim_pct": 66.7, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.783, "early_reclaim_pct": 66.7, "matched_signals": 31, "recovery_stability_score": 0.61, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:50:01.134863-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.85, "early_entry_score": 0.777, "early_reclaim_pct": 64.9, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.777, "early_reclaim_pct": 64.9, "matched_signals": 31, "recovery_stability_score": 0.577, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:45:04.190429-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.71, "early_entry_score": 0.813, "early_reclaim_pct": 70.4, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.572, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.813, "early_reclaim_pct": 70.4, "matched_signals": 34, "recovery_stability_score": 0.572, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}, {"current_drop_pct": 1.43, "early_entry_score": 0.671, "early_reclaim_pct": 81.0, "matched_signals": 34, "recovery_stability_score": 0.937, "success_rate": 88.24, "ticker": "STX", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:40:05.469838-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                              {"contract_symbol": "STX261016C00850000", "current_drop_pct": 1.33, "early_entry_score": 0.676, "early_reclaim_pct": 82.4, "entry_ask": 45.3, "entry_bid": 40.7, "entry_mode": "early", "entry_option_price": 43.0, "hypothetical_budget": 38058.05, "hypothetical_contracts": 8, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 147.0, "option_spread_pct": 10.7, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.94, "shadow_only": true, "success_rate": 88.24, "ticker": "STX", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 1.33, "early_entry_score": 0.676, "early_reclaim_pct": 82.4, "matched_signals": 34, "recovery_stability_score": 0.94, "success_rate": 88.24, "ticker": "STX", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-14T11:35:05.164573-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:30:05.695481-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:25:05.217490-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:20:05.740603-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.83, "early_entry_score": 0.779, "early_reclaim_pct": 65.5, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.779, "early_reclaim_pct": 65.5, "matched_signals": 31, "recovery_stability_score": 0.551, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:15:01.136676-04:00 early_entry_1115 early_entry_shadow   {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.74, "early_entry_score": 0.803, "early_reclaim_pct": 69.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.598, "shadow_only": true, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.803, "early_reclaim_pct": 69.3, "matched_signals": 33, "recovery_stability_score": 0.598, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "trend_health_status": "ok"}, {"current_drop_pct": 0.6, "early_entry_score": 0.712, "early_reclaim_pct": 84.2, "matched_signals": 36, "recovery_stability_score": 0.754, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914141504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914141504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914141504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914141504)

</details>
