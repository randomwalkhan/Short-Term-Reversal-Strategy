# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 11:30:02 EDT`
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
  CRWD           89.47               38            1.30              1.94        212.27                91.63         0.626          pass              0.694             63.9                           0.765               10.30              1.080                                 ok            True                   True
   KHC          100.00               11            0.74              0.13         24.79                29.15         0.620          pass              0.664             65.1                           0.499               -2.38              0.035                                 ok            True                  False
   WMT           84.21               19            1.18              0.88        106.76                40.24         0.593          pass              0.273             13.7                           0.313               -0.57              0.224                                 ok            True                  False
  MELI          100.00               13            2.52             34.93       1963.39                45.80         0.575          pass              0.478              0.3                           0.075               -1.00              0.045                                 ok            True                  False
  NVDA           92.00               25            1.48              2.39        229.33                44.80         0.535          pass              0.516             14.2                           0.288                8.85              0.875                                 ok            True                  False
  MSFT           88.89               18            1.32              4.63        497.72                23.39         0.510          pass              0.433             30.5                           0.571                1.19              0.134                                 ok            True                  False
  TMUS           96.43               28            0.56              0.71        181.22                25.50         0.507          pass              0.714             47.7                           0.386               -0.58              0.243                                 ok            True                  False
  PYPL           80.00                5            3.18              1.23         54.43                57.43         0.588          pass              0.067              2.8                           0.210              -13.52             -1.570 downtrend_blocked_slope_and_streak           False                  False
  MSTR           77.27               22            3.84              3.84        141.15               102.15         0.580          pass              0.216             26.0                           0.310               11.97              1.170                                 ok           False                  False
  SBUX           83.33                6            1.71              1.25        103.93                22.08         0.552          pass              0.147              0.8                           0.164               -4.47             -0.344            downtrend_blocked_slope           False                  False
  REGN          100.00                6            2.06             11.96        822.60                29.02         0.531          pass              0.572             39.6                           0.290               -2.16              0.100                                 ok           False                  False
 CMCSA           89.47               19            1.36              0.25         26.38                26.03         0.521          pass              0.461             32.1                           0.350               -3.29             -0.289            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-08T11:30:02.526432-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                       {"contract_symbol": "CRWD261016C00210000", "current_drop_pct": 1.3, "early_entry_score": 0.694, "early_reclaim_pct": 63.9, "entry_ask": 14.6, "entry_bid": 13.75, "entry_mode": "early", "entry_option_price": 14.175, "hypothetical_budget": 38574.05, "hypothetical_contracts": 27, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 699.0, "option_spread_pct": 6.0, "option_volume": 51.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.765, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.626, "top_candidates": [{"current_drop_pct": 1.3, "early_entry_score": 0.694, "early_reclaim_pct": 63.9, "matched_signals": 38, "recovery_stability_score": 0.765, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.626, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-08T11:25:02.514910-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                       {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.71, "early_entry_score": 0.808, "early_reclaim_pct": 74.2, "entry_ask": 9.5, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.0, "hypothetical_budget": 38574.05, "hypothetical_contracts": 42, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 11.11, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.805, "shadow_only": true, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.475, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.808, "early_reclaim_pct": 74.2, "matched_signals": 41, "recovery_stability_score": 0.805, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:20:06.485706-04:00 early_entry_1120 early_entry_shadow                               {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.88, "early_entry_score": 0.784, "early_reclaim_pct": 67.8, "entry_ask": 9.05, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 8.775, "hypothetical_budget": 38574.05, "hypothetical_contracts": 43, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 6.27, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.767, "shadow_only": true, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.784, "early_reclaim_pct": 67.8, "matched_signals": 40, "recovery_stability_score": 0.767, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "trend_health_status": "ok"}, {"current_drop_pct": 1.07, "early_entry_score": 0.671, "early_reclaim_pct": 72.5, "matched_signals": 36, "recovery_stability_score": 0.572, "success_rate": 88.89, "ticker": "INSM", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:15:01.537130-04:00 early_entry_1115 early_entry_shadow                              {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.82, "early_entry_score": 0.791, "early_reclaim_pct": 70.2, "entry_ask": 9.45, "entry_bid": 8.75, "entry_mode": "early", "entry_option_price": 9.1, "hypothetical_budget": 38574.05, "hypothetical_contracts": 42, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 7.69, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.791, "early_reclaim_pct": 70.2, "matched_signals": 40, "recovery_stability_score": 0.753, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.474, "trend_health_status": "ok"}, {"current_drop_pct": 1.03, "early_entry_score": 0.675, "early_reclaim_pct": 73.5, "matched_signals": 36, "recovery_stability_score": 0.569, "success_rate": 88.89, "ticker": "INSM", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:10:05.032926-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                     {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 1.08, "early_entry_score": 0.738, "early_reclaim_pct": 60.6, "entry_ask": 9.2, "entry_bid": 8.35, "entry_mode": "early", "entry_option_price": 8.775, "hypothetical_budget": 38574.05, "hypothetical_contracts": 43, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 9.69, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.689, "shadow_only": true, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 1.08, "early_entry_score": 0.738, "early_reclaim_pct": 60.6, "matched_signals": 38, "recovery_stability_score": 0.689, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:05:02.503396-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.79, "early_entry_score": 0.748, "early_reclaim_pct": 79.6, "entry_ask": 8.3, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 7.05, "hypothetical_budget": 38574.05, "hypothetical_contracts": 54, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 35.46, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.594, "shadow_only": true, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.429, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.748, "early_reclaim_pct": 79.6, "matched_signals": 40, "recovery_stability_score": 0.594, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.429, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.712, "early_reclaim_pct": 86.2, "matched_signals": 36, "recovery_stability_score": 0.577, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:00:03.391042-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                   {"contract_symbol": "ALNY261016C00260000", "current_drop_pct": 0.77, "early_entry_score": 0.712, "early_reclaim_pct": 86.1, "entry_ask": 20.4, "entry_bid": 19.5, "entry_mode": "early", "entry_option_price": 19.95, "hypothetical_budget": 38574.05, "hypothetical_contracts": 19, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 37.0, "option_spread_pct": 4.51, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.712, "early_reclaim_pct": 86.1, "matched_signals": 36, "recovery_stability_score": 0.597, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:55:04.328012-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "ALNY261016C00260000", "current_drop_pct": 0.83, "early_entry_score": 0.709, "early_reclaim_pct": 85.0, "entry_ask": 20.0, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 19.05, "hypothetical_budget": 38574.05, "hypothetical_contracts": 20, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 37.0, "option_spread_pct": 9.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.578, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.709, "early_reclaim_pct": 85.0, "matched_signals": 36, "recovery_stability_score": 0.578, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:50:03.448452-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "ALNY261016C00260000", "current_drop_pct": 0.81, "early_entry_score": 0.71, "early_reclaim_pct": 85.4, "entry_ask": 19.8, "entry_bid": 18.5, "entry_mode": "early", "entry_option_price": 19.15, "hypothetical_budget": 38574.05, "hypothetical_contracts": 20, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 37.0, "option_spread_pct": 6.79, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.71, "early_reclaim_pct": 85.4, "matched_signals": 36, "recovery_stability_score": 0.586, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:45:04.455818-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908113002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908113002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908113002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908113002)

</details>
