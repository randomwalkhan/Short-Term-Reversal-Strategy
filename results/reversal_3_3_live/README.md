# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 10:55:01 EDT`
Last processed slot: `manage_1100`

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
  MSTR           84.21               38            0.83              0.77        132.37               104.12         0.676            pass              0.610             81.0                           0.841                6.83              0.629                                 ok            True                  False
   KHC          100.00               11            0.75              0.13         24.55                28.60         0.610            pass              0.618             50.0                           0.390                0.10             -0.103                                 ok            True                  False
   STX           87.50               32            1.45              8.99        882.07                74.71         0.565            pass              0.584             60.3                           0.643                3.16              0.564                                 ok            True                  False
   CEG           86.67               15            1.76              3.62        292.36                32.56         0.505            pass              0.378             38.7                           0.296                3.30              0.673                                 ok            True                  False
  AMGN          100.00                7            1.80              4.94        389.15                44.45         0.638            pass              0.488              8.0                           0.130              -12.75             -1.238 downtrend_blocked_slope_and_streak           False                  False
  MRVL           75.68               37            1.13              1.86        234.21                80.25         0.572            pass              0.459             73.9                           0.738               -5.21             -0.140           downtrend_blocked_streak           False                  False
  ADBE           96.30               27            1.19              2.12        253.95                48.69         0.558            pass              0.700             43.5                           0.452               -7.91             -1.347 downtrend_blocked_slope_and_streak           False                  False
    ZS           97.78               45            0.02              0.02        166.09                64.27         0.554            pass              0.953             99.4                           0.473               -2.49             -1.095            downtrend_blocked_slope           False                  False
   EXC           94.44               18            0.32              0.10         43.66                15.30         0.552            pass              0.539             15.2                           0.142               -1.05              0.020                                 ok           False                  False
  REGN          100.00               14            1.45              8.20        804.14                27.92         0.536            pass              0.571             30.2                           0.310               -2.31              0.034           downtrend_blocked_streak           False                  False
  FAST           96.30               27            0.49              0.17         48.72                20.91         0.497 below_threshold              0.757             64.7                           0.559               -5.08             -0.411 downtrend_blocked_slope_and_streak           False                  False
   KDP           87.10               31            0.59              0.13         32.02                29.72         0.497 below_threshold              0.558             59.7                           0.639               -0.99              0.078                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-10T10:55:01.100392-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.3, "entry_ask": 6.6, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.95, "hypothetical_budget": 34870.55, "hypothetical_contracts": 58, "matched_signals": 39, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 21.85, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.72, "shadow_only": true, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.3, "matched_signals": 39, "recovery_stability_score": 0.72, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:50:03.195197-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.2, "entry_ask": 6.6, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 39, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 25.64, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.704, "shadow_only": true, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.2, "matched_signals": 39, "recovery_stability_score": 0.704, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.683, "early_reclaim_pct": 70.5, "matched_signals": 32, "recovery_stability_score": 0.798, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:45:02.277962-04:00 early_entry_1045 early_entry_shadow   {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.92, "early_entry_score": 0.688, "early_reclaim_pct": 73.7, "entry_ask": 6.6, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 25.64, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.688, "early_reclaim_pct": 73.7, "matched_signals": 37, "recovery_stability_score": 0.676, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.671, "early_reclaim_pct": 66.6, "matched_signals": 32, "recovery_stability_score": 0.792, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:40:01.116495-04:00 early_entry_1040 early_entry_shadow    {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 73.9, "entry_ask": 6.6, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.4, "hypothetical_budget": 34870.55, "hypothetical_contracts": 64, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 44.44, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.669, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 73.9, "matched_signals": 37, "recovery_stability_score": 0.669, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.67, "early_reclaim_pct": 66.3, "matched_signals": 32, "recovery_stability_score": 0.79, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:35:01.109260-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T10:30:01.098158-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "entry_ask": 7.1, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 51.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.588, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "matched_signals": 37, "recovery_stability_score": 0.588, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:25:01.160051-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.8, "early_entry_score": 0.746, "early_reclaim_pct": 77.3, "entry_ask": 7.1, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 51.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.746, "early_reclaim_pct": 77.3, "matched_signals": 41, "recovery_stability_score": 0.58, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.405, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:20:01.150296-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T10:15:05.197385-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T10:10:04.284123-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                         {"contract_symbol": "MSFT261016C00500000", "current_drop_pct": 0.52, "early_entry_score": 0.74, "early_reclaim_pct": 97.5, "entry_ask": 13.2, "entry_bid": 12.6, "entry_mode": "early", "entry_option_price": 12.9, "hypothetical_budget": 34870.55, "hypothetical_contracts": 27, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 24351.0, "option_spread_pct": 4.65, "option_volume": 115.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.728, "shadow_only": true, "success_rate": 90.32, "ticker": "MSFT", "timing_score": 0.32, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.74, "early_reclaim_pct": 97.5, "matched_signals": 31, "recovery_stability_score": 0.728, "success_rate": 90.32, "ticker": "MSFT", "timing_score": 0.32, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910105501)

</details>
