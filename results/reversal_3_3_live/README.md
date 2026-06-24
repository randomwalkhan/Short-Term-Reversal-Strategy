# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-24 10:35:01 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$30,612.50`
- Equity: `$30,612.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               23            2.25              4.39        277.16               157.48         0.778            pass              0.735             56.7                           0.614                2.21              0.845                                 ok            True                  False
  KLAC           92.59               27            1.15              1.97        243.65                93.06         0.721            pass              0.697             58.7                           0.541               12.97              1.316                                 ok            True                  False
  ASML           96.43               28            1.17             14.58       1772.21                65.60         0.638            pass              0.754             56.8                           0.676               -1.13              0.134                                 ok            True                  False
  PANW           92.86               42            0.55              1.12        290.44                56.69         0.531            pass              0.824             75.9                           0.680               11.05              0.951                                 ok            True                   True
   STX           95.00               20            1.64             11.94       1033.47                68.20         0.525            pass              0.767             82.6                           0.688               20.75              2.660                                 ok            True                  False
  NXPI           92.00               25            1.54              3.24        298.55                63.85         0.520            pass              0.580             36.0                           0.287               -0.71              0.324                                 ok            True                  False
  CDNS           94.44               36            0.65              1.72        378.32                55.93         0.504            pass              0.811             67.2                           0.586               -3.66             -0.190                                 ok            True                   True
   WDC           90.00               20            2.59             12.15        665.54                96.85         0.503            pass              0.630             82.2                           0.633               26.21              3.676                                 ok            True                  False
  MPWR           93.94               33            0.48              4.77       1421.71                86.34         0.683            pass              0.827             77.7                           0.749               -7.51             -0.704            downtrend_blocked_slope           False                  False
  MCHP           93.75               32            0.38              0.25         93.15                72.77         0.641            pass              0.815             79.2                           0.819                1.57              0.585                                 ok           False                  False
   EXC           87.50               24            0.24              0.08         46.59                19.83         0.541            pass              0.556             69.4                           0.308                2.60              0.194                                 ok           False                  False
   ADP           90.91               22            0.85              1.32        219.94                30.11         0.497 below_threshold              0.654             77.9                           0.431               -4.71             -0.563 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-24T10:35:01.108253-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PANW260731C00290000", "current_drop_pct": 0.55, "early_entry_score": 0.824, "early_reclaim_pct": 75.9, "entry_ask": 19.45, "entry_bid": 15.35, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 42, "option_liquidity_status": "wide_spread", "option_open_interest": 234.0, "option_spread_pct": 23.56, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 92.86, "ticker": "PANW", "timing_score": 0.531, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.824, "early_reclaim_pct": 75.9, "matched_signals": 42, "recovery_stability_score": 0.68, "success_rate": 92.86, "ticker": "PANW", "timing_score": 0.531, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 67.2, "matched_signals": 36, "recovery_stability_score": 0.586, "success_rate": 94.44, "ticker": "CDNS", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:30:01.120180-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:25:01.196604-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                          {"contract_symbol": "LRCX260731C00370000", "current_drop_pct": 0.72, "early_entry_score": 0.874, "early_reclaim_pct": 92.7, "entry_ask": 41.0, "entry_bid": 37.95, "entry_mode": "early", "entry_option_price": 39.475, "hypothetical_budget": 15306.25, "hypothetical_contracts": 3, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 87.0, "option_spread_pct": 7.73, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 96.67, "ticker": "LRCX", "timing_score": 0.629, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.874, "early_reclaim_pct": 92.7, "matched_signals": 30, "recovery_stability_score": 0.562, "success_rate": 96.67, "ticker": "LRCX", "timing_score": 0.629, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:20:01.164945-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                            {"contract_symbol": "AMAT260724C00580000", "current_drop_pct": 0.65, "early_entry_score": 0.888, "early_reclaim_pct": 96.1, "entry_ask": 54.55, "entry_bid": 49.75, "entry_mode": "early", "entry_option_price": 52.15, "hypothetical_budget": 15306.25, "hypothetical_contracts": 2, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 65.0, "option_spread_pct": 9.2, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.599, "shadow_only": true, "success_rate": 96.88, "ticker": "AMAT", "timing_score": 0.53, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.888, "early_reclaim_pct": 96.1, "matched_signals": 32, "recovery_stability_score": 0.599, "success_rate": 96.88, "ticker": "AMAT", "timing_score": 0.53, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:15:01.116504-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:10:01.169006-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"current_drop_pct": 0.84, "early_entry_score": 0.805, "early_reclaim_pct": 69.9, "entry_mode": "early", "error": "KLAC: no call expiries found in the 21-40 trading-day window.", "matched_signals": 33, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 93.94, "ticker": "KLAC", "timing_score": 0.705, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.805, "early_reclaim_pct": 69.9, "matched_signals": 33, "recovery_stability_score": 0.751, "success_rate": 93.94, "ticker": "KLAC", "timing_score": 0.705, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:05:01.111815-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:00:02.286958-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                  {"contract_symbol": "LRCX260724C00370000", "current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.3, "entry_ask": 35.3, "entry_bid": 32.3, "entry_mode": "early", "entry_option_price": 33.8, "hypothetical_budget": 15306.25, "hypothetical_contracts": 4, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 114.0, "option_spread_pct": 8.88, "option_volume": 38.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.62, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.3, "matched_signals": 33, "recovery_stability_score": 0.655, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.62, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-24T09:20:01.109273-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-06-23T12:00:01.662630-04:00 early_entry_1200 early_entry_shadow                  {"contract_symbol": "GOOG260724C00345000", "current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "entry_ask": 15.1, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.775, "hypothetical_budget": 15306.25, "hypothetical_contracts": 10, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 118.0, "option_spread_pct": 4.4, "option_volume": 45.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "matched_signals": 34, "recovery_stability_score": 0.751, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.743, "early_reclaim_pct": 90.5, "matched_signals": 32, "recovery_stability_score": 0.752, "success_rate": 90.62, "ticker": "GOOGL", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260624103501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260624103501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260624103501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260624103501)

</details>
