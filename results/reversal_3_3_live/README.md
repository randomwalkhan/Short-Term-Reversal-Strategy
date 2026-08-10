# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 11:45:06 EDT`
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

- Cash: `$31,073.00`
- Equity: `$31,073.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  PYPL     option         option PYPL260918C00060000     94          2026-08-07         2026-08-10        1.725      1.5525 -1621.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           84.62               39            0.70              0.73        148.76               133.30         0.804          pass              0.620             74.4                           0.526               54.41              3.919                  ok            True                  False
  SOXL           80.65               31            3.60              3.54        138.73               179.06         0.699          pass              0.312             28.5                           0.364                5.50              2.570                  ok            True                  False
  PYPL           93.10               29            0.94              0.39         58.90                60.12         0.662          pass              0.646             34.7                           0.244                4.36              0.336                  ok            True                  False
  LRCX           87.50               32            1.02              2.23        310.39                90.05         0.654          pass              0.549             45.6                           0.482                5.68              1.430                  ok            True                  False
  AMAT           89.66               29            1.54              5.81        536.65                85.88         0.641          pass              0.542             31.3                           0.408                2.70              1.268                  ok            True                  False
 CMCSA           92.31               13            1.56              0.28         25.24                44.15         0.632          pass              0.509             32.5                           0.528                9.50              0.763                  ok            True                  False
  TMUS           92.59               27            1.08              1.34        176.61                55.81         0.629          pass              0.671             53.1                           0.579               -1.09             -0.154                  ok            True                  False
  MDLZ           91.67               12            1.69              0.74         62.29                30.17         0.558          pass              0.426             15.2                           0.254                1.46             -0.040                  ok            True                  False
  BKNG           95.00               20            1.82              2.74        213.25                46.72         0.554          pass              0.597             25.0                           0.326               12.70              1.022                  ok            True                  False
  ORLY           88.46               26            1.23              0.81         93.18                35.75         0.527          pass              0.487             34.1                           0.402                1.98              0.410                  ok            True                  False
   PEP           80.00               25            0.76              0.74        138.70                22.07         0.504          pass              0.248             32.5                           0.394               -1.31             -0.278                  ok            True                  False
   HON           86.96               23            1.06              1.83        245.42                29.28         0.503          pass              0.477             51.7                           0.338               -0.88              0.010                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-08-10T11:45:06.232412-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:40:01.623818-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:35:01.707228-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:30:06.173236-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:25:02.712869-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:20:04.669365-04:00 early_entry_1120 early_entry_shadow   {"contract_symbol": "HON260911C00245000", "current_drop_pct": 0.58, "early_entry_score": 0.738, "early_reclaim_pct": 73.6, "entry_ask": 9.4, "entry_bid": 6.7, "entry_mode": "early", "entry_option_price": 8.05, "hypothetical_budget": 15536.5, "hypothetical_contracts": 19, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 33.54, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 91.43, "ticker": "HON", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.738, "early_reclaim_pct": 73.6, "matched_signals": 35, "recovery_stability_score": 0.743, "success_rate": 91.43, "ticker": "HON", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-10T11:15:01.972299-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "HON260911C00245000", "current_drop_pct": 0.65, "early_entry_score": 0.688, "early_reclaim_pct": 70.3, "entry_ask": 9.4, "entry_bid": 6.7, "entry_mode": "early", "entry_option_price": 8.05, "hypothetical_budget": 15536.5, "hypothetical_contracts": 19, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 33.54, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 90.62, "ticker": "HON", "timing_score": 0.475, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.688, "early_reclaim_pct": 70.3, "matched_signals": 32, "recovery_stability_score": 0.713, "success_rate": 90.62, "ticker": "HON", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-10T11:10:06.738408-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:05:04.768952-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:00:02.784116-04:00 early_entry_1100 early_entry_shadow                           {"contract_symbol": "TMUS260918C00175000", "current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "entry_ask": 7.0, "entry_bid": 6.5, "entry_mode": "early", "entry_option_price": 6.75, "hypothetical_budget": 15536.5, "hypothetical_contracts": 23, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 971.0, "option_spread_pct": 7.41, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "matched_signals": 33, "recovery_stability_score": 0.827, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810114506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810114506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810114506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810114506)

</details>
