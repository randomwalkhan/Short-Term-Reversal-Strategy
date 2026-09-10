# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 11:30:05 EDT`
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
  MSTR           80.65               31            1.77              1.64        132.00               104.12         0.660            pass              0.401             59.4                           0.436                5.81              0.585                                 ok            True                  False
   KHC          100.00               11            0.87              0.15         24.55                28.60         0.602            pass              0.593             41.9                           0.372               -0.02             -0.108                                 ok            True                  False
   EXC          100.00               12            0.62              0.19         43.62                15.30         0.574            pass              0.471              0.0                           0.186               -1.34              0.007                                 ok            True                  False
   STX           85.19               27            2.52             15.62        879.22                74.71         0.529            pass              0.398             31.0                           0.287                2.04              0.514                                 ok            True                  False
   AEP           89.47               19            0.67              0.58        124.42                16.58         0.515            pass              0.507             47.6                           0.249                0.39              0.187                                 ok            True                  False
  AMGN          100.00                3            2.08              5.71        388.82                44.45         0.643            pass              0.484              6.5                           0.184              -13.00             -1.251 downtrend_blocked_slope_and_streak           False                  False
  ADBE           96.00               25            1.39              2.48        253.80                48.69         0.557            pass              0.658             34.0                           0.347               -8.10             -1.356 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               11            1.55              8.79        803.88                27.92         0.549            pass              0.537             25.2                           0.246               -2.42              0.029           downtrend_blocked_streak           False                  False
  MRVL           74.29               35            1.69              2.78        233.82                80.25         0.549            pass              0.405             61.1                           0.445               -5.74             -0.166           downtrend_blocked_streak           False                  False
    ZS           97.78               45            0.15              0.17        166.03                64.27         0.546            pass              0.935             93.6                           0.477               -2.62             -1.101            downtrend_blocked_slope           False                  False
  FAST           95.83               24            0.68              0.23         48.69                20.91         0.504            pass              0.698             51.5                           0.494               -5.26             -0.419 downtrend_blocked_slope_and_streak           False                  False
   CEG           92.00               25            0.94              1.93        293.08                32.56         0.499 below_threshold              0.672             67.2                           0.704                4.16              0.710                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-10T11:30:05.235557-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                       {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "entry_ask": 6.0, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.39, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.653, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "matched_signals": 37, "recovery_stability_score": 0.653, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:25:01.128031-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                       {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "entry_ask": 5.8, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.45, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.84, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.629, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "matched_signals": 37, "recovery_stability_score": 0.629, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:20:01.183708-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                         {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "entry_ask": 5.7, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 5.35, "hypothetical_budget": 34870.55, "hypothetical_contracts": 65, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 13.08, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "matched_signals": 37, "recovery_stability_score": 0.632, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:15:01.146533-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.89, "early_entry_score": 0.705, "early_reclaim_pct": 74.7, "entry_ask": 6.2, "entry_bid": 5.4, "entry_mode": "early", "entry_option_price": 5.8, "hypothetical_budget": 34870.55, "hypothetical_contracts": 60, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 13.79, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.705, "early_reclaim_pct": 74.7, "matched_signals": 38, "recovery_stability_score": 0.61, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:10:01.103447-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:05:01.145835-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:00:02.278798-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "entry_ask": 6.6, "entry_bid": 5.2, "entry_mode": "early", "entry_option_price": 5.9, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 23.73, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.689, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "matched_signals": 37, "recovery_stability_score": 0.689, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:55:01.100392-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.3, "entry_ask": 6.6, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.95, "hypothetical_budget": 34870.55, "hypothetical_contracts": 58, "matched_signals": 39, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 21.85, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.72, "shadow_only": true, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.3, "matched_signals": 39, "recovery_stability_score": 0.72, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:50:03.195197-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.2, "entry_ask": 6.6, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 39, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 25.64, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.704, "shadow_only": true, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.2, "matched_signals": 39, "recovery_stability_score": 0.704, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.683, "early_reclaim_pct": 70.5, "matched_signals": 32, "recovery_stability_score": 0.798, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:45:02.277962-04:00 early_entry_1045 early_entry_shadow   {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.92, "early_entry_score": 0.688, "early_reclaim_pct": 73.7, "entry_ask": 6.6, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 25.64, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.688, "early_reclaim_pct": 73.7, "matched_signals": 37, "recovery_stability_score": 0.676, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.671, "early_reclaim_pct": 66.6, "matched_signals": 32, "recovery_stability_score": 0.792, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910113005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910113005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910113005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910113005)

</details>
