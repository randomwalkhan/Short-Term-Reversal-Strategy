# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 11:55:01 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$31,411.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ASML           94.29               35            0.61              7.49       1744.37                63.09         0.590          pass              0.716             36.3                           0.310               -4.83             -0.200                                 ok            True                  False
   WBD           83.33               12            1.10              0.21         26.78                20.40         0.568          pass              0.210             16.9                           0.341                1.74              0.371                                 ok            True                  False
   CSX           86.67               15            0.97              0.34         50.60                17.40         0.537          pass              0.274              3.0                           0.149                2.97              0.430                                 ok            True                  False
  MNST          100.00               14            1.54              1.05         97.05                20.09         0.527          pass              0.543             21.1                           0.181               -1.41              0.116                                 ok            True                  False
  CTAS           85.00               20            1.38              1.98        203.60                36.07         0.521          pass              0.354             34.0                           0.593               13.12              1.523                                 ok            True                  False
  ORLY           80.00               25            1.42              0.85         85.68                41.23         0.520          pass              0.206             18.1                           0.272                0.70             -0.010                                 ok            True                  False
  BKNG           83.33               24            1.34              1.71        180.95                41.44         0.516          pass              0.364             43.5                           0.404               -0.99              0.162                                 ok            True                  False
  GILD           92.86               28            0.57              0.53        134.05                34.72         0.515          pass              0.630             38.7                           0.452                3.02              0.047                                 ok            True                  False
  PCAR           87.88               33            0.54              0.48        126.00                30.30         0.502          pass              0.572             52.8                           0.644               -0.31              0.121                                 ok            True                  False
  KLAC           88.89               36            0.72              1.07        212.29               107.27         0.694          pass              0.658             59.5                           0.534               -9.47             -0.582 downtrend_blocked_slope_and_streak           False                  False
  LRCX           88.89               27            0.90              1.97        312.45                96.49         0.677          pass              0.612             64.7                           0.526              -11.34             -0.900 downtrend_blocked_slope_and_streak           False                  False
  AAPL          100.00                3            2.24              5.22        331.50                36.42         0.620          pass              0.522             20.0                           0.440                4.36              0.684                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-07-20T11:55:01.102362-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:50:01.110550-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:45:01.103753-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "VRSK260821C00200000", "current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 68.7, "entry_ask": 9.6, "entry_bid": 8.6, "entry_mode": "early", "entry_option_price": 9.1, "hypothetical_budget": 15705.88, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 47.0, "option_spread_pct": 10.99, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.668, "shadow_only": true, "success_rate": 90.24, "ticker": "VRSK", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 68.7, "matched_signals": 41, "recovery_stability_score": 0.668, "success_rate": 90.24, "ticker": "VRSK", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-20T11:40:02.180070-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:35:01.099987-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "VRSK260821C00200000", "current_drop_pct": 0.57, "early_entry_score": 0.695, "early_reclaim_pct": 65.2, "entry_ask": 9.4, "entry_bid": 8.7, "entry_mode": "early", "entry_option_price": 9.05, "hypothetical_budget": 15705.88, "hypothetical_contracts": 17, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 47.0, "option_spread_pct": 7.73, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.692, "shadow_only": true, "success_rate": 89.74, "ticker": "VRSK", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.695, "early_reclaim_pct": 65.2, "matched_signals": 39, "recovery_stability_score": 0.692, "success_rate": 89.74, "ticker": "VRSK", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-20T11:30:02.147951-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:25:05.073932-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:20:01.956277-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:15:03.134685-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                            {"contract_symbol": "ADP260821C00250000", "current_drop_pct": 0.55, "early_entry_score": 0.785, "early_reclaim_pct": 67.0, "entry_ask": 13.2, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.35, "hypothetical_budget": 15705.88, "hypothetical_contracts": 12, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 640.0, "option_spread_pct": 13.77, "option_volume": 704.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.779, "shadow_only": true, "success_rate": 96.67, "ticker": "ADP", "timing_score": 0.502, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.785, "early_reclaim_pct": 67.0, "matched_signals": 30, "recovery_stability_score": 0.779, "success_rate": 96.67, "ticker": "ADP", "timing_score": 0.502, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-20T11:10:02.138494-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ADP260821C00250000", "current_drop_pct": 0.51, "early_entry_score": 0.792, "early_reclaim_pct": 69.3, "entry_ask": 13.0, "entry_bid": 11.2, "entry_mode": "early", "entry_option_price": 12.1, "hypothetical_budget": 15705.88, "hypothetical_contracts": 12, "matched_signals": 30, "option_liquidity_status": "wide_spread", "option_open_interest": 640.0, "option_spread_pct": 14.88, "option_volume": 704.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.802, "shadow_only": true, "success_rate": 96.67, "ticker": "ADP", "timing_score": 0.505, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.792, "early_reclaim_pct": 69.3, "matched_signals": 30, "recovery_stability_score": 0.802, "success_rate": 96.67, "ticker": "ADP", "timing_score": 0.505, "trend_health_status": "ok"}, {"current_drop_pct": 0.54, "early_entry_score": 0.7, "early_reclaim_pct": 66.9, "matched_signals": 39, "recovery_stability_score": 0.736, "success_rate": 89.74, "ticker": "VRSK", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720115501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720115501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720115501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720115501)

</details>
