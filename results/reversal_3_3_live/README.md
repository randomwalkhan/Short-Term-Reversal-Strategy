# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 13:55:02 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.65               31            1.93              1.79        131.93               104.12         0.651          pass              0.390             55.8                           0.538                5.64              0.578                                 ok            True                  False
   KHC          100.00               11            0.79              0.14         24.55                28.60         0.607          pass              0.609             47.3                           0.354                0.06             -0.105                                 ok            True                  False
   EXC           92.31               13            0.56              0.17         43.63                15.30         0.562          pass              0.511             35.5                           0.535               -1.29              0.009                                 ok            True                  False
   STX           84.00               25            2.73             16.93        878.66                74.71         0.521          pass              0.366             35.8                           0.495                1.82              0.504                                 ok            True                  False
   AEP           90.48               21            0.63              0.55        124.43                16.58         0.506          pass              0.555             50.5                           0.449                0.42              0.189                                 ok            True                  False
  AMGN          100.00                1            2.29              6.28        388.58                44.45         0.641          pass              0.489              8.1                           0.242              -13.18             -1.261 downtrend_blocked_slope_and_streak           False                  False
  WDAY           91.67               36            0.71              0.92        185.65                77.13         0.639          pass              0.714             55.1                           0.318               -3.16             -0.524 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               11            1.61              9.11        803.74                27.92         0.545          pass              0.528             22.4                           0.251               -2.47              0.026           downtrend_blocked_streak           False                  False
  INTU           97.14               35            0.50              1.10        313.47                48.73         0.537          pass              0.806             62.0                           0.312               -9.69             -1.295 downtrend_blocked_slope_and_streak           False                  False
  MRVL           76.47               34            2.09              3.43        233.54                80.25         0.533          pass              0.369             52.0                           0.471               -6.12             -0.184           downtrend_blocked_streak           False                  False
    ZS           96.88               32            1.70              1.98        165.25                64.27         0.528          pass              0.681             27.2                           0.155               -4.13             -1.172            downtrend_blocked_slope           False                  False
  ADBE           94.44               18            2.52              4.49        252.93                48.69         0.525          pass              0.519              9.2                           0.171               -9.15             -1.408 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-10T12:00:03.311742-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:55:04.274439-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "entry_ask": 5.8, "entry_bid": 4.7, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 20.95, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "matched_signals": 37, "recovery_stability_score": 0.651, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:50:01.152194-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "entry_ask": 5.7, "entry_bid": 4.8, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 17.14, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "matched_signals": 41, "recovery_stability_score": 0.674, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.67, "early_reclaim_pct": 66.3, "matched_signals": 32, "recovery_stability_score": 0.576, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:45:04.259583-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "entry_ask": 5.9, "entry_bid": 4.4, "entry_mode": "early", "entry_option_price": 5.15, "hypothetical_budget": 34870.55, "hypothetical_contracts": 67, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 29.13, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:40:01.104202-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                       {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "entry_ask": 5.8, "entry_bid": 5.2, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 10.91, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "matched_signals": 37, "recovery_stability_score": 0.632, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:35:01.128582-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:30:05.235557-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "entry_ask": 6.0, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.39, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.653, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "matched_signals": 37, "recovery_stability_score": 0.653, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:25:01.128031-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "entry_ask": 5.8, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.45, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.84, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.629, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "matched_signals": 37, "recovery_stability_score": 0.629, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:20:01.183708-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                        {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "entry_ask": 5.7, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 5.35, "hypothetical_budget": 34870.55, "hypothetical_contracts": 65, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 13.08, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "matched_signals": 37, "recovery_stability_score": 0.632, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:15:01.146533-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                         {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.89, "early_entry_score": 0.705, "early_reclaim_pct": 74.7, "entry_ask": 6.2, "entry_bid": 5.4, "entry_mode": "early", "entry_option_price": 5.8, "hypothetical_budget": 34870.55, "hypothetical_contracts": 60, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 13.79, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.705, "early_reclaim_pct": 74.7, "matched_signals": 38, "recovery_stability_score": 0.61, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910135502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910135502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910135502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910135502)

</details>
