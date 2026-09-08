# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 14:10:05 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$77,148.10`
- Equity: `$77,148.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261016C00145000     30          2026-09-04         2026-09-08       13.375     12.0375 -4012.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           89.47               38            1.27              1.89        212.29                91.63         0.628          pass              0.697             64.9                           0.521               10.34              1.082                                 ok            True                  False
   WMT           80.95               21            1.03              0.77        106.81                40.24         0.586          pass              0.233             25.3                           0.503               -0.43              0.230                                 ok            True                  False
  MELI          100.00               13            2.56             35.50       1963.15                45.80         0.563          pass              0.560             27.9                           0.486               -1.04              0.043                                 ok            True                  False
  REGN          100.00               11            1.50              8.69        824.00                29.02         0.534          pass              0.628             56.1                           0.699               -1.59              0.126                                 ok            True                  False
  NVDA           91.30               23            1.89              3.04        229.06                44.80         0.519          pass              0.474             11.3                           0.321                8.41              0.856                                 ok            True                  False
  MSFT           88.89               18            1.44              5.02        497.55                23.39         0.504          pass              0.414             24.6                           0.491                1.07              0.129                                 ok            True                  False
   KDP           86.67               30            0.72              0.16         32.52                30.79         0.502          pass              0.434             24.2                           0.254               -0.48              0.151                                 ok            True                  False
   KHC          100.00               18            0.20              0.04         24.83                29.15         0.610          pass              0.786             90.6                           0.687               -1.84              0.059                                 ok           False                  False
  PYPL           80.00                5            2.97              1.14         54.47                57.43         0.598          pass              0.103             14.4                           0.292              -13.33             -1.560 downtrend_blocked_slope_and_streak           False                  False
  MSTR           76.92               26            3.37              3.37        141.36               102.15         0.583          pass              0.270             35.1                           0.525               12.52              1.193                                 ok           False                  False
  NFLX           88.24               17            1.80              0.98         77.83                39.36         0.521          pass              0.437             39.7                           0.631               -3.96             -0.269            downtrend_blocked_slope           False                  False
 CMCSA           89.47               19            1.38              0.26         26.38                26.03         0.520          pass              0.458             31.1                           0.402               -3.31             -0.290            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-08T12:00:01.401463-04:00 early_entry_1200 early_entry_shadow                            {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.67, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "entry_ask": 10.05, "entry_bid": 9.45, "entry_mode": "early", "entry_option_price": 9.75, "hypothetical_budget": 38574.05, "hypothetical_contracts": 39, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 6.15, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 92.86, "ticker": "FTNT", "timing_score": 0.472, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "matched_signals": 42, "recovery_stability_score": 0.62, "success_rate": 92.86, "ticker": "FTNT", "timing_score": 0.472, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.716, "early_reclaim_pct": 77.6, "matched_signals": 38, "recovery_stability_score": 0.691, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:55:05.335939-04:00 early_entry_1155 early_entry_shadow                              {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.6, "entry_ask": 10.1, "entry_bid": 9.15, "entry_mode": "early", "entry_option_price": 9.625, "hypothetical_budget": 38574.05, "hypothetical_contracts": 40, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 9.87, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.6, "matched_signals": 40, "recovery_stability_score": 0.605, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "trend_health_status": "ok"}, {"current_drop_pct": 0.97, "early_entry_score": 0.693, "early_reclaim_pct": 74.9, "matched_signals": 37, "recovery_stability_score": 0.648, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:50:01.520765-04:00 early_entry_1150 early_entry_shadow                           {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 73.9, "entry_ask": 10.15, "entry_bid": 9.15, "entry_mode": "early", "entry_option_price": 9.65, "hypothetical_budget": 38574.05, "hypothetical_contracts": 39, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 10.36, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.71, "shadow_only": true, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 73.9, "matched_signals": 41, "recovery_stability_score": 0.71, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.474, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.716, "early_reclaim_pct": 77.6, "matched_signals": 38, "recovery_stability_score": 0.648, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:45:03.461951-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.71, "early_entry_score": 0.755, "early_reclaim_pct": 81.7, "entry_ask": 7.0, "entry_bid": 5.9, "entry_mode": "early", "entry_option_price": 6.45, "hypothetical_budget": 38574.05, "hypothetical_contracts": 59, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 17.05, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.645, "shadow_only": true, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.755, "early_reclaim_pct": 81.7, "matched_signals": 40, "recovery_stability_score": 0.645, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.434, "trend_health_status": "ok"}, {"current_drop_pct": 1.34, "early_entry_score": 0.676, "early_reclaim_pct": 62.8, "matched_signals": 37, "recovery_stability_score": 0.699, "success_rate": 89.19, "ticker": "CRWD", "timing_score": 0.629, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:40:05.489649-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.56, "early_entry_score": 0.784, "early_reclaim_pct": 85.5, "entry_ask": 7.0, "entry_bid": 5.9, "entry_mode": "early", "entry_option_price": 6.45, "hypothetical_budget": 38574.05, "hypothetical_contracts": 59, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 17.05, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.631, "shadow_only": true, "success_rate": 90.7, "ticker": "INSM", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.784, "early_reclaim_pct": 85.5, "matched_signals": 43, "recovery_stability_score": 0.631, "success_rate": 90.7, "ticker": "INSM", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:35:03.323433-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 1.07, "early_entry_score": 0.671, "early_reclaim_pct": 72.5, "entry_ask": 7.0, "entry_bid": 5.9, "entry_mode": "early", "entry_option_price": 6.45, "hypothetical_budget": 38574.05, "hypothetical_contracts": 59, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 17.05, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.552, "shadow_only": true, "success_rate": 88.89, "ticker": "INSM", "timing_score": 0.435, "top_candidates": [{"current_drop_pct": 1.07, "early_entry_score": 0.671, "early_reclaim_pct": 72.5, "matched_signals": 36, "recovery_stability_score": 0.552, "success_rate": 88.89, "ticker": "INSM", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:30:02.526432-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                       {"contract_symbol": "CRWD261016C00210000", "current_drop_pct": 1.3, "early_entry_score": 0.694, "early_reclaim_pct": 63.9, "entry_ask": 14.6, "entry_bid": 13.75, "entry_mode": "early", "entry_option_price": 14.175, "hypothetical_budget": 38574.05, "hypothetical_contracts": 27, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 699.0, "option_spread_pct": 6.0, "option_volume": 51.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.765, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.626, "top_candidates": [{"current_drop_pct": 1.3, "early_entry_score": 0.694, "early_reclaim_pct": 63.9, "matched_signals": 38, "recovery_stability_score": 0.765, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.626, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-08T11:25:02.514910-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                       {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.71, "early_entry_score": 0.808, "early_reclaim_pct": 74.2, "entry_ask": 9.5, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 38574.05, "hypothetical_contracts": 42, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 11.11, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.805, "shadow_only": true, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.475, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.808, "early_reclaim_pct": 74.2, "matched_signals": 41, "recovery_stability_score": 0.805, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:20:06.485706-04:00 early_entry_1120 early_entry_shadow                               {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.88, "early_entry_score": 0.784, "early_reclaim_pct": 67.8, "entry_ask": 9.05, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 8.775, "hypothetical_budget": 38574.05, "hypothetical_contracts": 43, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 6.27, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.767, "shadow_only": true, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.784, "early_reclaim_pct": 67.8, "matched_signals": 40, "recovery_stability_score": 0.767, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "trend_health_status": "ok"}, {"current_drop_pct": 1.07, "early_entry_score": 0.671, "early_reclaim_pct": 72.5, "matched_signals": 36, "recovery_stability_score": 0.572, "success_rate": 88.89, "ticker": "INSM", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:15:01.537130-04:00 early_entry_1115 early_entry_shadow                              {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.82, "early_entry_score": 0.791, "early_reclaim_pct": 70.2, "entry_ask": 9.45, "entry_bid": 8.75, "entry_mode": "early", "entry_option_price": 9.1, "hypothetical_budget": 38574.05, "hypothetical_contracts": 42, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 7.69, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.791, "early_reclaim_pct": 70.2, "matched_signals": 40, "recovery_stability_score": 0.753, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.474, "trend_health_status": "ok"}, {"current_drop_pct": 1.03, "early_entry_score": 0.675, "early_reclaim_pct": 73.5, "matched_signals": 36, "recovery_stability_score": 0.569, "success_rate": 88.89, "ticker": "INSM", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908141005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908141005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908141005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908141005)

</details>
