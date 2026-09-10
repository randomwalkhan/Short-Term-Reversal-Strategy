# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 11:05:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           82.35               34            1.31              1.22        132.18               104.12         0.670          pass              0.500             69.9                           0.702                6.31              0.607                                 ok            True                  False
   STX           87.50               32            1.18              7.31        882.79                74.71         0.582          pass              0.608             67.7                           0.630                3.44              0.576                                 ok            True                  False
   CEG           86.67               15            1.65              3.40        292.45                32.56         0.512          pass              0.389             42.3                           0.285                3.41              0.677                                 ok            True                  False
  TMUS           96.00               25            0.76              0.94        176.94                27.01         0.505          pass              0.563              4.3                           0.176               -1.45             -0.009                                 ok            True                  False
  AMGN          100.00                5            1.96              5.36        388.97                44.45         0.640          pass              0.486              7.3                           0.178              -12.88             -1.245 downtrend_blocked_slope_and_streak           False                  False
  WDAY           93.18               44            0.10              0.13        185.99                77.13         0.629          pass              0.895             93.5                           0.476               -2.56             -0.497 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                9            1.06              0.18         24.53                28.60         0.604          pass              0.550             29.7                           0.226               -0.20             -0.117                                 ok           False                  False
  MRVL           75.00               36            1.26              2.07        234.12                80.25         0.570          pass              0.443             71.0                           0.630               -5.33             -0.146           downtrend_blocked_streak           False                  False
   EXC           93.75               16            0.39              0.12         43.65                15.30         0.558          pass              0.520             19.0                           0.217               -1.12              0.017                                 ok           False                  False
    ZS           97.78               45            0.04              0.04        166.08                64.27         0.553          pass              0.951             98.5                           0.499               -2.51             -1.096            downtrend_blocked_slope           False                  False
  ADBE           96.00               25            1.50              2.68        253.71                48.69         0.551          pass              0.640             28.5                           0.275               -8.21             -1.361 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               15            1.42              8.04        804.21                27.92         0.532          pass              0.581             31.5                           0.348               -2.29              0.035           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-10T11:05:01.145835-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:00:02.278798-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "entry_ask": 6.6, "entry_bid": 5.2, "entry_mode": "early", "entry_option_price": 5.9, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 23.73, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.689, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "matched_signals": 37, "recovery_stability_score": 0.689, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:55:01.100392-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.3, "entry_ask": 6.6, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.95, "hypothetical_budget": 34870.55, "hypothetical_contracts": 58, "matched_signals": 39, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 21.85, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.72, "shadow_only": true, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.3, "matched_signals": 39, "recovery_stability_score": 0.72, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:50:03.195197-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.2, "entry_ask": 6.6, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 39, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 25.64, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.704, "shadow_only": true, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.723, "early_reclaim_pct": 76.2, "matched_signals": 39, "recovery_stability_score": 0.704, "success_rate": 89.74, "ticker": "INSM", "timing_score": 0.414, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.683, "early_reclaim_pct": 70.5, "matched_signals": 32, "recovery_stability_score": 0.798, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:45:02.277962-04:00 early_entry_1045 early_entry_shadow   {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.92, "early_entry_score": 0.688, "early_reclaim_pct": 73.7, "entry_ask": 6.6, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 34870.55, "hypothetical_contracts": 59, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 25.64, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.688, "early_reclaim_pct": 73.7, "matched_signals": 37, "recovery_stability_score": 0.676, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.671, "early_reclaim_pct": 66.6, "matched_signals": 32, "recovery_stability_score": 0.792, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:40:01.116495-04:00 early_entry_1040 early_entry_shadow    {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 73.9, "entry_ask": 6.6, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.4, "hypothetical_budget": 34870.55, "hypothetical_contracts": 64, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 44.44, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.669, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 73.9, "matched_signals": 37, "recovery_stability_score": 0.669, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.67, "early_reclaim_pct": 66.3, "matched_signals": 32, "recovery_stability_score": 0.79, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:35:01.109260-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T10:30:01.098158-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "entry_ask": 7.1, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 51.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.588, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "matched_signals": 37, "recovery_stability_score": 0.588, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:25:01.160051-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.8, "early_entry_score": 0.746, "early_reclaim_pct": 77.3, "entry_ask": 7.1, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 51.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.746, "early_reclaim_pct": 77.3, "matched_signals": 41, "recovery_stability_score": 0.58, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.405, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:20:01.150296-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910110501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910110501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910110501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910110501)

</details>
