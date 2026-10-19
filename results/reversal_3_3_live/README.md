# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 11:05:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           90.91               11            0.91              0.14         21.84                21.89         0.564          pass              0.492             45.9                           0.667                2.17              0.312                                 ok            True                  False
   ADP           90.00               20            1.10              2.22        287.95                21.32         0.524          pass              0.491             35.2                           0.278                9.79              1.070                                 ok            True                  False
  CTAS           90.48               21            1.17              1.75        212.94                23.07         0.513          pass              0.461             19.1                           0.391                8.08              0.964                                 ok            True                  False
  CTSH           94.29               35            0.88              0.41         65.86                41.45         0.506          pass              0.700             34.1                           0.396               12.52              1.549                                 ok            True                  False
  GILD           91.67               24            0.92              1.01        155.76                24.77         0.506          pass              0.455              0.0                           0.150                7.00              0.844                                 ok            True                  False
   KHC           88.00               25            0.89              0.15         23.62                22.28         0.501          pass              0.483             40.0                           0.355                7.46              0.771                                 ok            True                  False
  TMUS           82.14               28            0.77              0.85        158.73                56.39         0.626          pass              0.334             31.5                           0.412               -4.11             -0.640            downtrend_blocked_slope           False                  False
  PAYX           68.42               19            1.50              1.18        111.13                41.41         0.574          pass              0.162             14.7                           0.342               10.19              1.128                                 ok           False                  False
   KDP           96.00               25            0.49              0.12         34.57                30.61         0.567          pass              0.779             74.2                           0.579               11.52              1.320                                 ok           False                  False
   CEG           90.00               10            2.94              5.59        268.97                59.14         0.551          pass              0.347              8.3                           0.141               -1.58             -0.718 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           95.00               20            0.47              0.21         63.82                19.69         0.549          pass              0.661             46.4                           0.332                8.75              0.869                                 ok           False                  False
   XEL           77.78                9            1.27              0.68         76.02                16.32         0.536          pass              0.074              6.7                           0.197                5.39              0.572                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-19T11:05:06.144826-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:45:07.151563-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:40:09.556532-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:35:09.745420-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.596, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "matched_signals": 35, "recovery_stability_score": 0.596, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T10:30:09.531569-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:25:06.859178-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.62, "early_entry_score": 0.845, "early_reclaim_pct": 77.8, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 94.59, "ticker": "PYPL", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.845, "early_reclaim_pct": 77.8, "matched_signals": 37, "recovery_stability_score": 0.607, "success_rate": 94.59, "ticker": "PYPL", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T10:20:06.047125-04:00 early_entry_1020 early_entry_shadow                                             {"contract_symbol": "PYPL261120C00057500", "current_drop_pct": 0.58, "early_entry_score": 0.859, "early_reclaim_pct": 79.1, "entry_ask": 2.57, "entry_bid": 2.42, "entry_mode": "early", "entry_option_price": 2.495, "hypothetical_budget": 65765.9, "hypothetical_contracts": 263, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 5457.0, "option_spread_pct": 6.01, "option_volume": 754.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.656, "shadow_only": true, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.859, "early_reclaim_pct": 79.1, "matched_signals": 38, "recovery_stability_score": 0.656, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-19T10:15:09.644271-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:10:06.129033-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T10:05:07.192059-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019110506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019110506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019110506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019110506)

</details>
