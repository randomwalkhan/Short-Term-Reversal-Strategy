# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 11:10:01 EDT`
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

- Cash: `$72,316.10`
- Equity: `$72,316.10`
- Realized PnL: `$62,316.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-15)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   EXC     option         option EXC261016C00043000    400          2026-09-14         2026-09-15         0.95       0.855 -3800.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           93.33               30            0.78              0.29         53.90                58.07         0.624          pass              0.657             35.4                           0.428                2.05              0.013                                 ok            True                  False
  TEAM          100.00               35            1.02              1.38        192.18                63.46         0.570          pass              0.821             65.8                           0.775               -1.74             -0.276                                 ok            True                   True
   AEP           81.82               11            0.93              0.80        121.89                16.70         0.529          pass              0.134              8.8                           0.230               -1.09             -0.094                                 ok            True                  False
  TMUS           96.30               27            0.55              0.71        182.60                25.87         0.513          pass              0.730             55.0                           0.281                0.80             -0.152                                 ok            True                  False
  AAPL           85.71               21            1.14              2.65        331.94                23.75         0.508          pass              0.336             19.9                           0.333                3.93              0.301                                 ok            True                  False
  ISRG           80.95               21            1.62              4.28        376.10                34.61         0.508          pass              0.248             32.7                           0.648               -1.34             -0.077                                 ok            True                  False
  AMGN           91.67               12            1.40              3.75        379.89                45.29         0.624          pass              0.420             11.0                           0.209              -12.50             -1.919 downtrend_blocked_slope_and_streak           False                  False
    ZS           97.62               42            0.31              0.41        191.55                82.09         0.623          pass              0.924             87.3                           0.715                1.46              0.023                                 ok           False                  False
  MSTR           77.78               18            4.28              4.10        135.18               103.17         0.593          pass              0.204             30.6                           0.622               -1.40              0.155                                 ok           False                  False
   WMT           85.71               35            0.36              0.27        108.96                40.03         0.562          pass              0.542             55.6                           0.350                3.64              0.240                                 ok           False                  False
  REGN          100.00                4            2.29             12.72        788.29                29.50         0.556          pass              0.477              7.0                           0.225               -2.94             -0.641 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00               10            0.82              0.25         42.61                14.63         0.550          pass              0.532             25.5                           0.190               -2.17             -0.212           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-15T11:10:01.228919-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                              {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.02, "early_entry_score": 0.821, "early_reclaim_pct": 65.8, "entry_ask": 13.4, "entry_bid": 12.3, "entry_mode": "early", "entry_option_price": 12.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 8.56, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.775, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.57, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.821, "early_reclaim_pct": 65.8, "matched_signals": 35, "recovery_stability_score": 0.775, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.57, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:05:02.271330-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                             {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.16, "early_entry_score": 0.795, "early_reclaim_pct": 61.3, "entry_ask": 13.1, "entry_bid": 12.1, "entry_mode": "early", "entry_option_price": 12.6, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 7.94, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.708, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.574, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.795, "early_reclaim_pct": 61.3, "matched_signals": 33, "recovery_stability_score": 0.708, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.574, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:00:05.317059-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                             {"contract_symbol": "GILD261016C00150000", "current_drop_pct": 0.77, "early_entry_score": 0.748, "early_reclaim_pct": 68.8, "entry_ask": 3.1, "entry_bid": 2.74, "entry_mode": "early", "entry_option_price": 2.92, "hypothetical_budget": 36158.05, "hypothetical_contracts": 123, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 529.0, "option_spread_pct": 12.33, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.576, "shadow_only": true, "success_rate": 91.89, "ticker": "GILD", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.748, "early_reclaim_pct": 68.8, "matched_signals": 37, "recovery_stability_score": 0.576, "success_rate": 91.89, "ticker": "GILD", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:55:01.169845-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "CTSH261016C00065000", "current_drop_pct": 0.55, "early_entry_score": 0.871, "early_reclaim_pct": 84.0, "entry_ask": 2.55, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.475, "hypothetical_budget": 36158.05, "hypothetical_contracts": 146, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 712.0, "option_spread_pct": 6.06, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.691, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.871, "early_reclaim_pct": 84.0, "matched_signals": 35, "recovery_stability_score": 0.691, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.769, "early_reclaim_pct": 71.9, "matched_signals": 38, "recovery_stability_score": 0.65, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.441, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:50:06.229690-04:00 early_entry_1050 early_entry_shadow   {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.72, "early_entry_score": 0.849, "early_reclaim_pct": 79.0, "entry_ask": 3.8, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.6, "hypothetical_budget": 36158.05, "hypothetical_contracts": 100, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 792.0, "option_spread_pct": 11.11, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 97.06, "ticker": "CTSH", "timing_score": 0.516, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.849, "early_reclaim_pct": 79.0, "matched_signals": 34, "recovery_stability_score": 0.593, "success_rate": 97.06, "ticker": "CTSH", "timing_score": 0.516, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.799, "early_reclaim_pct": 77.7, "matched_signals": 39, "recovery_stability_score": 0.735, "success_rate": 92.31, "ticker": "GILD", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:45:06.502503-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:40:02.128909-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:35:06.132265-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:30:04.241835-04:00 early_entry_1030 early_entry_shadow                   {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.61, "early_entry_score": 0.781, "early_reclaim_pct": 83.2, "entry_ask": 9.9, "entry_bid": 9.25, "entry_mode": "early", "entry_option_price": 9.575, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 602.0, "option_spread_pct": 6.79, "option_volume": 100.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.581, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.781, "early_reclaim_pct": 83.2, "matched_signals": 42, "recovery_stability_score": 0.581, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.778, "early_reclaim_pct": 74.8, "matched_signals": 38, "recovery_stability_score": 0.752, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:25:01.133088-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "entry_ask": 4.8, "entry_bid": 4.3, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 36158.05, "hypothetical_contracts": 79, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 10.99, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.739, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "matched_signals": 38, "recovery_stability_score": 0.739, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915111001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915111001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915111001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915111001)

</details>
