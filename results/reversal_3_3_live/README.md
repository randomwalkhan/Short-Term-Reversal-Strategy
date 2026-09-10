# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 11:45:04 EDT`
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

- Cash: `$69,741.10`
- Equity: `$69,741.10`
- Realized PnL: `$59,741.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261009C00135000     34          2026-09-09         2026-09-10        10.85       9.765 -3689.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           82.35               34            1.44              1.33        132.13               104.12         0.663            pass              0.490             67.1                           0.626                6.17              0.601                                 ok            True                  False
   KHC          100.00               10            0.91              0.16         24.54                28.60         0.606            pass              0.578             39.2                           0.413               -0.06             -0.110                                 ok            True                  False
   EXC           92.31               13            0.54              0.16         43.63                15.30         0.564            pass              0.491             28.8                           0.300               -1.26              0.011                                 ok            True                  False
   STX           84.00               25            2.71             16.84        878.70                74.71         0.528            pass              0.337             25.7                           0.181                1.83              0.505                                 ok            True                  False
   AEP           90.48               21            0.65              0.57        124.43                16.58         0.505            pass              0.551             49.2                           0.284                0.41              0.188                                 ok            True                  False
  AMGN          100.00                3            2.04              5.58        388.88                44.45         0.646            pass              0.491              8.7                           0.256              -12.95             -1.249 downtrend_blocked_slope_and_streak           False                  False
  MRVL           74.29               35            1.64              2.69        233.86                80.25         0.552            pass              0.409             62.3                           0.504               -5.69             -0.163           downtrend_blocked_streak           False                  False
  REGN          100.00               11            1.57              8.85        803.86                27.92         0.548            pass              0.535             24.6                           0.226               -2.43              0.028           downtrend_blocked_streak           False                  False
  ADBE           96.00               25            1.63              2.90        253.62                48.69         0.543            pass              0.622             22.6                           0.335               -8.32             -1.367 downtrend_blocked_slope_and_streak           False                  False
  CPRT           88.64               44            0.08              0.02         32.02                45.10         0.497 below_threshold              0.744             88.1                           0.579               -2.04             -0.138                                 ok           False                  False
  FAST           95.83               24            0.78              0.27         48.68                20.91         0.497 below_threshold              0.675             44.1                           0.324               -5.36             -0.424 downtrend_blocked_slope_and_streak           False                  False
  TMUS           96.00               25            0.94              1.17        176.84                27.01         0.492 below_threshold              0.576              9.0                           0.273               -1.63             -0.018                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-10T11:45:04.259583-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "entry_ask": 5.9, "entry_bid": 4.4, "entry_mode": "early", "entry_option_price": 5.15, "hypothetical_budget": 34870.55, "hypothetical_contracts": 67, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 29.13, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:40:01.104202-04:00 early_entry_1140 early_entry_shadow              {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "entry_ask": 5.8, "entry_bid": 5.2, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 10.91, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "matched_signals": 37, "recovery_stability_score": 0.632, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:35:01.128582-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:30:05.235557-04:00 early_entry_1130 early_entry_shadow             {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "entry_ask": 6.0, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.39, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.653, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "matched_signals": 37, "recovery_stability_score": 0.653, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:25:01.128031-04:00 early_entry_1125 early_entry_shadow             {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "entry_ask": 5.8, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.45, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.84, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.629, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "matched_signals": 37, "recovery_stability_score": 0.629, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:20:01.183708-04:00 early_entry_1120 early_entry_shadow               {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "entry_ask": 5.7, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 5.35, "hypothetical_budget": 34870.55, "hypothetical_contracts": 65, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 13.08, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "matched_signals": 37, "recovery_stability_score": 0.632, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:15:01.146533-04:00 early_entry_1115 early_entry_shadow                {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.89, "early_entry_score": 0.705, "early_reclaim_pct": 74.7, "entry_ask": 6.2, "entry_bid": 5.4, "entry_mode": "early", "entry_option_price": 5.8, "hypothetical_budget": 34870.55, "hypothetical_contracts": 60, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 13.79, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.705, "early_reclaim_pct": 74.7, "matched_signals": 38, "recovery_stability_score": 0.61, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:10:01.103447-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:05:01.145835-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:00:02.278798-04:00 early_entry_1100 early_entry_shadow    {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "entry_ask": 6.6, "entry_bid": 5.2, "entry_mode": "early", "entry_option_price": 5.9, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 23.73, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.689, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "matched_signals": 37, "recovery_stability_score": 0.689, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910114504)

</details>
