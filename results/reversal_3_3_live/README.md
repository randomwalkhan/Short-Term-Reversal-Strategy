# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 12:50:04 EDT`
Last processed slot: `manage_1300`

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
   CEG           87.50               16            2.11              4.01        269.65                59.14         0.560          pass              0.399             34.2                           0.377               -0.74             -0.679                      ok            True                  False
   ADP           91.30               23            0.74              1.49        288.26                21.32         0.529          pass              0.611             56.5                           0.640               10.19              1.086                      ok            True                  False
   KHC           84.62               13            1.79              0.30         23.55                22.28         0.511          pass              0.217              7.6                           0.275                6.48              0.729                      ok            True                  False
  CTAS           92.59               27            0.78              1.17        213.19                23.07         0.502          pass              0.637             46.0                           0.658                8.51              0.981                      ok            True                  False
  GILD           90.91               22            1.11              1.22        155.67                24.77         0.501          pass              0.479             19.4                           0.297                6.79              0.835                      ok            True                  False
  TMUS           81.48               27            0.80              0.89        158.72                56.39         0.629          pass              0.302             28.7                           0.416               -4.14             -0.642 downtrend_blocked_slope           False                  False
   KDP           96.55               29            0.27              0.07         34.59                30.61         0.556          pass              0.839             85.6                           0.792               11.77              1.330                      ok           False                  False
  PAYX           75.00               28            1.07              0.84        111.27                41.41         0.553          pass              0.293             39.1                           0.649               10.67              1.148                      ok           False                  False
  MDLZ           95.00               20            0.47              0.21         63.82                19.69         0.549          pass              0.661             46.4                           0.416                8.75              0.869                      ok           False                  False
 CMCSA           90.00               20            0.25              0.04         21.88                21.89         0.549          pass              0.644             85.1                           0.804                2.85              0.343                      ok           False                  False
  AMGN           78.95               19            1.18              3.57        430.96                28.96         0.530          pass              0.161             16.0                           0.360                6.06              0.740                      ok           False                  False
   XEL           66.67                6            1.51              0.80         75.97                16.32         0.527          pass              0.054              0.4                           0.199                5.13              0.562                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-19T12:00:05.186192-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.582, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "matched_signals": 35, "recovery_stability_score": 0.582, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T11:55:09.715127-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.56, "early_entry_score": 0.861, "early_reclaim_pct": 79.7, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.861, "early_reclaim_pct": 79.7, "matched_signals": 38, "recovery_stability_score": 0.632, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T11:50:02.588008-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:45:09.986778-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:40:09.738573-04:00 early_entry_1140 early_entry_shadow   {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.51, "early_entry_score": 0.887, "early_reclaim_pct": 81.6, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.887, "early_reclaim_pct": 81.6, "matched_signals": 40, "recovery_stability_score": 0.715, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T11:35:06.347486-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:30:09.037804-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:25:06.081540-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:20:07.934552-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:15:04.155259-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019125004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019125004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019125004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019125004)

</details>
