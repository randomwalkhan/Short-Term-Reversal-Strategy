# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 11:05:03 EDT`
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

- Cash: `$35,098.00`
- Equity: `$35,098.00`
- Realized PnL: `$25,098.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  LRCX     option         option LRCX260918C00310000      5          2026-08-10         2026-08-12        26.85        34.9 4025.0   29.981378 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.35               34            1.23              1.33        153.51               126.50         0.787          pass              0.470             56.2                           0.300               45.93              5.170                  ok            True                  False
  PYPL           91.67               24            1.08              0.44         58.81                59.96         0.676          pass              0.631             53.0                           0.532                0.03              0.212                  ok            True                  False
  SHOP           96.43               28            1.66              1.78        151.85                81.89         0.663          pass              0.605              6.3                           0.194               16.18              2.890                  ok            True                  False
  ABNB          100.00               10            2.40              3.11        183.65                64.05         0.642          pass              0.521             19.0                           0.291               17.99              2.263                  ok            True                  False
  GEHC           95.45               22            1.28              0.65         72.47                54.33         0.633          pass              0.683             46.6                           0.567               -0.11              0.325                  ok            True                  False
 CMCSA           87.50               16            1.35              0.24         25.55                42.38         0.619          pass              0.349             15.9                           0.314                6.91              0.679                  ok            True                  False
  TMUS           90.62               32            0.73              0.92        178.20                55.82         0.615          pass              0.555             21.1                           0.338                2.27              0.266                  ok            True                  False
   ROP          100.00               15            2.02              5.66        397.08                44.32         0.603          pass              0.547             17.6                           0.188                0.56              0.162                  ok            True                  False
  PAYX          100.00               11            1.83              1.56        120.63                33.26         0.570          pass              0.525             20.5                           0.260                2.36              0.354                  ok            True                  False
  FAST          100.00               20            0.79              0.29         52.26                25.01         0.567          pass              0.653             43.2                           0.407               11.37              1.196                  ok            True                  False
  MDLZ           88.46               26            0.53              0.23         61.68                29.90         0.559          pass              0.572             61.4                           0.641               -2.58             -0.195                  ok            True                  False
   LIN           80.00               15            1.49              5.11        488.34                25.58         0.549          pass              0.088              0.0                           0.208               -5.00             -0.067                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-12T11:05:03.802537-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.8, "early_entry_score": 0.741, "early_reclaim_pct": 76.8, "entry_ask": 17.05, "entry_bid": 16.3, "entry_mode": "early", "entry_option_price": 16.675, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 4.5, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.568, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.741, "early_reclaim_pct": 76.8, "matched_signals": 40, "recovery_stability_score": 0.568, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.439, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T11:00:05.629703-04:00 early_entry_1100 early_entry_shadow  {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.84, "early_entry_score": 0.737, "early_reclaim_pct": 75.5, "entry_ask": 17.35, "entry_bid": 16.7, "entry_mode": "early", "entry_option_price": 17.025, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 3.82, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.596, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.737, "early_reclaim_pct": 75.5, "matched_signals": 40, "recovery_stability_score": 0.596, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.437, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.721, "early_reclaim_pct": 94.2, "matched_signals": 30, "recovery_stability_score": 0.661, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:55:04.810521-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.6, "entry_ask": 17.7, "entry_bid": 16.95, "entry_mode": "early", "entry_option_price": 17.325, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 4.33, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.6, "matched_signals": 41, "recovery_stability_score": 0.696, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:50:01.775257-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.5, "entry_ask": 17.55, "entry_bid": 16.45, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.47, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.5, "matched_signals": 41, "recovery_stability_score": 0.789, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:45:05.750947-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:40:06.908628-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:35:08.326280-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:30:06.810656-04:00 early_entry_1030 early_entry_shadow     {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "entry_ask": 16.5, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.25, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.838, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "matched_signals": 40, "recovery_stability_score": 0.838, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.72, "early_reclaim_pct": 94.1, "matched_signals": 30, "recovery_stability_score": 0.734, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.379, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:25:01.823569-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.68, "early_entry_score": 0.757, "early_reclaim_pct": 80.1, "entry_ask": 16.5, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 15.95, "hypothetical_budget": 17549.0, "hypothetical_contracts": 11, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.9, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.843, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.441, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.757, "early_reclaim_pct": 80.1, "matched_signals": 41, "recovery_stability_score": 0.843, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.441, "trend_health_status": "ok"}, {"current_drop_pct": 0.59, "early_entry_score": 0.746, "early_reclaim_pct": 95.5, "matched_signals": 37, "recovery_stability_score": 0.717, "success_rate": 89.19, "ticker": "CTAS", "timing_score": 0.347, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:20:04.811080-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "matched_signals": 34, "recovery_stability_score": 0.643, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812110503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812110503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812110503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812110503)

</details>
