# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 11:20:07 EDT`
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
  MDLZ           92.31               13            0.77              0.34         63.76                19.69         0.570          pass              0.443             12.5                           0.185                8.43              0.856                      ok            True                  False
   CEG           85.00               20            1.94              3.69        269.79                59.14         0.544          pass              0.373             39.5                           0.531               -0.57             -0.672                      ok            True                  False
   ADP           90.91               22            0.84              1.69        288.17                21.32         0.528          pass              0.575             50.5                           0.437               10.07              1.082                      ok            True                  False
  GILD           88.89               18            1.26              1.38        155.60                24.77         0.515          pass              0.369              9.0                           0.101                6.63              0.829                      ok            True                  False
  CTAS           91.67               24            0.91              1.36        213.11                23.07         0.512          pass              0.566             36.9                           0.654                8.36              0.975                      ok            True                  False
   KHC           85.71               21            1.25              0.21         23.59                22.28         0.501          pass              0.323             15.7                           0.178                7.07              0.754                      ok            True                  False
  TMUS           85.71               35            0.39              0.43        158.91                56.39         0.612          pass              0.576             65.2                           0.761               -3.74             -0.623 downtrend_blocked_slope           False                  False
   KDP           96.15               26            0.43              0.10         34.58                30.61         0.564          pass              0.795             77.3                           0.632               11.59              1.322                      ok           False                  False
  PAYX           68.18               22            1.39              1.08        111.17                41.41         0.563          pass              0.200             21.3                           0.431               10.32              1.133                      ok           False                  False
 CMCSA           90.48               21            0.18              0.03         21.89                21.89         0.548          pass              0.675             89.2                           0.903                2.92              0.346                      ok           False                  False
   XEL           77.78                9            1.22              0.65         76.03                16.32         0.538          pass              0.091             12.3                           0.266                5.44              0.575                      ok           False                  False
  AMGN           78.95               19            1.17              3.55        430.97                28.96         0.531          pass              0.162             16.5                           0.161                6.06              0.740                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-19T11:20:07.934552-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:15:04.155259-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:10:06.177116-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.58, "early_entry_score": 0.859, "early_reclaim_pct": 79.1, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.859, "early_reclaim_pct": 79.1, "matched_signals": 38, "recovery_stability_score": 0.662, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T11:05:06.144826-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:45:07.151563-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:40:09.556532-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:35:09.745420-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.596, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "matched_signals": 35, "recovery_stability_score": 0.596, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T10:30:09.531569-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:25:06.859178-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.62, "early_entry_score": 0.845, "early_reclaim_pct": 77.8, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 94.59, "ticker": "PYPL", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.845, "early_reclaim_pct": 77.8, "matched_signals": 37, "recovery_stability_score": 0.607, "success_rate": 94.59, "ticker": "PYPL", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T10:20:06.047125-04:00 early_entry_1020 early_entry_shadow                                             {"contract_symbol": "PYPL261120C00057500", "current_drop_pct": 0.58, "early_entry_score": 0.859, "early_reclaim_pct": 79.1, "entry_ask": 2.57, "entry_bid": 2.42, "entry_mode": "early", "entry_option_price": 2.495, "hypothetical_budget": 65765.9, "hypothetical_contracts": 263, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 5457.0, "option_spread_pct": 6.01, "option_volume": 754.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.656, "shadow_only": true, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.859, "early_reclaim_pct": 79.1, "matched_signals": 38, "recovery_stability_score": 0.656, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019112007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019112007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019112007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019112007)

</details>
