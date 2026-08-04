# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 11:25:01 EDT`
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

- Cash: `$33,480.75`
- Equity: `$33,480.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-04)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00050000    106          2026-08-03         2026-08-04         1.65       1.485 -1749.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ROP           93.10               29            0.99              2.72        391.40                47.45         0.564          pass              0.696             54.6                           0.493               10.83              1.477                                 ok            True                  False
   PEP           86.36               22            0.86              0.84        139.27                26.13         0.551          pass              0.461             52.2                           0.596                2.54              0.382                                 ok            True                  False
  ALNY           83.33               24            1.73              2.66        219.19               126.96         0.812          pass              0.340             25.4                           0.264              -20.21             -2.938            downtrend_blocked_slope           False                  False
  ISRG           69.23               13            2.24              5.89        372.89                72.79         0.663          pass              0.113              8.9                           0.212                4.84              0.809                                 ok           False                  False
  TMUS           92.59               27            0.90              1.11        176.61                55.96         0.636          pass              0.648             45.2                           0.512               -8.00             -0.664            downtrend_blocked_slope           False                  False
 CMCSA           85.71               21            0.31              0.05         24.54                43.78         0.636          pass              0.527             79.2                           0.417                2.83              0.705                                 ok           False                  False
   KHC           92.00               25            0.09              0.02         26.41                32.72         0.622          pass              0.755             91.1                           0.733                2.35              0.318                                 ok           False                  False
  GEHC           95.00               40            0.25              0.12         69.68                58.11         0.615          pass              0.908             82.1                           0.790               12.18              1.650                                 ok           False                  False
   MAR          100.00               14            1.37              3.33        345.40                34.81         0.603          pass              0.549             20.8                           0.173               -7.00             -0.501 downtrend_blocked_slope_and_streak           False                  False
  AMZN           75.00               16            2.22              4.41        282.13                60.32         0.592          pass              0.198             33.0                           0.329               12.19              1.480                                 ok           False                  False
  MDLZ           91.67               24            0.42              0.18         61.65                32.17         0.588          pass              0.691             75.9                           0.754                2.69              0.411                                 ok           False                  False
  DXCM           90.00               40            0.25              0.15         87.24                57.42         0.560          pass              0.763             80.0                           0.625               16.51              1.982                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-08-04T11:25:01.272769-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:20:01.453908-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:15:06.199893-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "matched_signals": 35, "recovery_stability_score": 0.657, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:10:06.366472-04:00 early_entry_1110 early_entry_shadow              {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.6, "early_entry_score": 0.812, "early_reclaim_pct": 86.4, "entry_ask": 37.3, "entry_bid": 32.7, "entry_mode": "early", "entry_option_price": 35.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 13.14, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 92.11, "ticker": "REGN", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.812, "early_reclaim_pct": 86.4, "matched_signals": 38, "recovery_stability_score": 0.749, "success_rate": 92.11, "ticker": "REGN", "timing_score": 0.432, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.801, "early_reclaim_pct": 60.2, "matched_signals": 36, "recovery_stability_score": 0.601, "success_rate": 94.44, "ticker": "GEHC", "timing_score": 0.62, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:05:01.401227-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 70.4, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.629, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 70.4, "matched_signals": 35, "recovery_stability_score": 0.629, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:00:04.371634-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.56, "early_entry_score": 0.812, "early_reclaim_pct": 71.4, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.812, "early_reclaim_pct": 71.4, "matched_signals": 35, "recovery_stability_score": 0.607, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:55:01.394123-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.62, "early_entry_score": 0.798, "early_reclaim_pct": 85.8, "entry_ask": 37.5, "entry_bid": 32.5, "entry_mode": "early", "entry_option_price": 35.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 14.29, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.656, "shadow_only": true, "success_rate": 91.89, "ticker": "REGN", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.798, "early_reclaim_pct": 85.8, "matched_signals": 37, "recovery_stability_score": 0.656, "success_rate": 91.89, "ticker": "REGN", "timing_score": 0.437, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.786, "early_reclaim_pct": 66.6, "matched_signals": 34, "recovery_stability_score": 0.556, "success_rate": 94.12, "ticker": "CTAS", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:50:01.407562-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.56, "early_entry_score": 0.826, "early_reclaim_pct": 87.1, "entry_ask": 37.5, "entry_bid": 31.5, "entry_mode": "early", "entry_option_price": 34.5, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 17.39, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.635, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.826, "early_reclaim_pct": 87.1, "matched_signals": 39, "recovery_stability_score": 0.635, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:45:04.409620-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "GEHC260904C00069000", "current_drop_pct": 0.53, "early_entry_score": 0.817, "early_reclaim_pct": 62.2, "entry_ask": 3.8, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 3.15, "hypothetical_budget": 16740.38, "hypothetical_contracts": 53, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 41.27, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.554, "shadow_only": true, "success_rate": 94.59, "ticker": "GEHC", "timing_score": 0.616, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.817, "early_reclaim_pct": 62.2, "matched_signals": 37, "recovery_stability_score": 0.554, "success_rate": 94.59, "ticker": "GEHC", "timing_score": 0.616, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.798, "early_reclaim_pct": 85.8, "matched_signals": 37, "recovery_stability_score": 0.594, "success_rate": 91.89, "ticker": "REGN", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T10:40:01.354459-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804112501)

</details>
