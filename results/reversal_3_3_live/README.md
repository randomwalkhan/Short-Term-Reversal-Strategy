# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 11:35:06 EDT`
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

- Cash: `$131,531.80`
- Equity: `$131,531.80`
- Realized PnL: `$121,531.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     35          2026-10-16         2026-10-19        17.05       19.65 9100.0   15.249267 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.86               14            0.61              0.27         63.79                19.69         0.574          pass              0.518             30.4                           0.293                8.60              0.863                      ok            True                  False
   CEG           85.71               21            1.80              3.41        269.91                59.14         0.547          pass              0.412             44.0                           0.645               -0.42             -0.665                      ok            True                  False
   ADP           90.91               22            0.85              1.72        288.16                21.32         0.528          pass              0.573             49.8                           0.515               10.06              1.081                      ok            True                  False
  GILD           89.47               19            1.21              1.33        155.62                24.77         0.512          pass              0.401             12.3                           0.165                6.68              0.831                      ok            True                  False
  CTAS           91.67               24            0.95              1.42        213.08                23.07         0.509          pass              0.558             34.3                           0.632                8.32              0.974                      ok            True                  False
  TMUS           85.29               34            0.50              0.56        158.86                56.39         0.610          pass              0.527             55.1                           0.666               -3.85             -0.628 downtrend_blocked_slope           False                  False
   KDP           96.15               26            0.48              0.12         34.57                30.61         0.562          pass              0.788             75.0                           0.651               11.54              1.320                      ok           False                  False
  PAYX           75.00               28            1.12              0.88        111.25                41.41         0.551          pass              0.285             36.5                           0.649               10.62              1.146                      ok           False                  False
 CMCSA           89.47               19            0.39              0.06         21.87                21.89         0.546          pass              0.598             77.0                           0.798                2.71              0.336                      ok           False                  False
  AMGN           77.78               18            1.24              3.74        430.89                28.96         0.532          pass              0.142             11.9                           0.159                6.00              0.737                      ok           False                  False
   XEL           77.78                9            1.32              0.71         76.01                16.32         0.532          pass              0.067              4.7                           0.176                5.33              0.570                      ok           False                  False
  CTSH           95.35               43            0.11              0.05         66.01                41.45         0.504          pass              0.927             92.0                           0.852               13.39              1.584                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-19T11:35:06.347486-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:30:09.037804-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:25:06.081540-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:20:07.934552-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:15:04.155259-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:10:06.177116-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.58, "early_entry_score": 0.859, "early_reclaim_pct": 79.1, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.859, "early_reclaim_pct": 79.1, "matched_signals": 38, "recovery_stability_score": 0.662, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T11:05:06.144826-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:45:07.151563-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:40:09.556532-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:35:09.745420-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.596, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "matched_signals": 35, "recovery_stability_score": 0.596, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019113506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019113506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019113506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019113506)

</details>
