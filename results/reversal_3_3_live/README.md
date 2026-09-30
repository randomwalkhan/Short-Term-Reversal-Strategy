# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-30 11:05:05 EDT`
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

- Cash: `$85,238.30`
- Equity: `$85,238.30`
- Realized PnL: `$75,238.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261120C00155000     24          2026-09-29         2026-09-30         15.9        18.6 6480.0   16.981132 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           85.71               35            0.77              0.79        146.66               117.21         0.746          pass              0.610             72.1                           0.551               40.40              2.912                  ok            True                  False
  MSTR           94.12               34            0.90              0.97        154.25                99.32         0.672          pass              0.746             47.5                           0.467               21.48              1.369                  ok            True                  False
  DRAM           82.76               29            1.08              0.46         61.09                54.99         0.587          pass              0.353             31.2                           0.363                9.58              0.602                  ok            True                  False
  META           86.21               29            1.05              5.43        736.46                54.80         0.558          pass              0.515             55.7                           0.717                8.66              0.943                  ok            True                  False
  ASML           80.65               31            0.77              9.84       1830.17                42.72         0.554          pass              0.280             22.6                           0.392               13.61              1.176                  ok            True                  False
  PYPL           88.24               17            1.47              0.55         53.65                34.93         0.538          pass              0.326              1.9                           0.096                0.74              0.271                  ok            True                  False
  MPWR           85.19               27            1.47             13.92       1348.03                52.13         0.528          pass              0.399             31.4                           0.402               16.25              1.599                  ok            True                  False
   ADI           88.89               27            0.80              2.23        397.27                32.38         0.516          pass              0.517             38.4                           0.503                9.12              0.908                  ok            True                  False
  MRVL           82.76               29            2.01              3.71        261.68                56.16         0.508          pass              0.325             24.6                           0.411               12.30              0.957                  ok            True                  False
   BKR           91.67               24            1.02              0.40         55.75                31.55         0.504          pass              0.593             46.0                           0.277               -1.72             -0.127                  ok            True                  False
   WBD           94.87               39            0.11              0.02         30.84                37.86         0.568          pass              0.737             30.0                           0.361                9.78              1.038                  ok           False                  False
  AMAT           84.62               39            0.47              1.68        511.29                51.71         0.552          pass              0.563             63.8                           0.470               22.69              2.002                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-30T11:05:05.139754-04:00 early_entry_1105 early_entry_shadow   {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.54, "early_entry_score": 0.745, "early_reclaim_pct": 62.4, "entry_ask": 8.1, "entry_bid": 7.5, "entry_mode": "early", "entry_option_price": 7.8, "hypothetical_budget": 42619.15, "hypothetical_contracts": 54, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 4833.0, "option_spread_pct": 7.69, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.686, "shadow_only": true, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.745, "early_reclaim_pct": 62.4, "matched_signals": 32, "recovery_stability_score": 0.686, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.443, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.717, "early_reclaim_pct": 69.9, "matched_signals": 40, "recovery_stability_score": 0.704, "success_rate": 90.0, "ticker": "DXCM", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T11:00:06.131458-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.54, "early_entry_score": 0.746, "early_reclaim_pct": 62.8, "entry_ask": 8.1, "entry_bid": 7.3, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 42619.15, "hypothetical_contracts": 55, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 4833.0, "option_spread_pct": 10.39, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.672, "shadow_only": true, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.746, "early_reclaim_pct": 62.8, "matched_signals": 32, "recovery_stability_score": 0.672, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.444, "trend_health_status": "ok"}, {"current_drop_pct": 0.52, "early_entry_score": 0.702, "early_reclaim_pct": 69.2, "matched_signals": 39, "recovery_stability_score": 0.727, "success_rate": 89.74, "ticker": "DXCM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T10:55:04.133991-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:50:05.630077-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.53, "early_entry_score": 0.76, "early_reclaim_pct": 63.5, "entry_ask": 8.1, "entry_bid": 7.3, "entry_mode": "early", "entry_option_price": 7.7, "hypothetical_budget": 42619.15, "hypothetical_contracts": 55, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 4833.0, "option_spread_pct": 10.39, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.76, "early_reclaim_pct": 63.5, "matched_signals": 33, "recovery_stability_score": 0.593, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T10:45:06.139283-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                {"contract_symbol": "DXCM261030C00086000", "current_drop_pct": 0.62, "early_entry_score": 0.67, "early_reclaim_pct": 63.0, "entry_ask": 5.3, "entry_bid": 3.2, "entry_mode": "early", "entry_option_price": 4.25, "hypothetical_budget": 42619.15, "hypothetical_contracts": 100, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 49.41, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.614, "shadow_only": true, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.67, "early_reclaim_pct": 63.0, "matched_signals": 38, "recovery_stability_score": 0.614, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T10:40:05.432480-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:35:02.181722-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:30:04.117201-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:25:03.100104-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T10:20:05.117028-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260930110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260930110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260930110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260930110505)

</details>
