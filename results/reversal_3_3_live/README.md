# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 10:25:01 EDT`
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

- Cash: `$17,610.75`
- Equity: `$32,330.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$-1,040.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   1     16     15760.0                 14720.0         9.85            9.2       98.17          99.1          bid_ask_mid                        9.2                bid_ask_mid                    True         -1040.0                   -6.6         95.65               23              3.29          79.1           73.52                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-08)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               20            0.70              0.49        100.32                33.39         0.598          pass              0.719             64.0                           0.702                2.91              0.570                                 ok            True                  False
  MSFT           84.62               26            0.98              2.86        415.44                34.82         0.558          pass              0.357             24.0                           0.339               -1.43              0.124                                 ok            True                  False
  DASH           92.68               41            0.62              0.68        156.51                51.66         0.501          pass              0.835             82.2                           0.701               -2.16             -0.045                                 ok            True                   True
   TRI           78.95               19            1.46              0.88         85.66                69.04         0.650          pass              0.272             49.0                           0.689               -1.26              0.170                                 ok           False                  False
  TEAM           95.35               43            0.37              0.26         99.36                86.36         0.649          pass              0.932             89.0                           0.771               16.01              1.865                                 ok           False                  False
   CEG           82.35               34            0.57              1.01        254.40                55.63         0.575          pass              0.488             69.3                           0.618              -11.35             -1.486            downtrend_blocked_slope           False                  False
  ROST           94.74               38            0.35              0.57        230.13                43.36         0.561          pass              0.775             46.4                           0.253               -2.24             -0.132                                 ok           False                  False
   AEP           69.23               13            0.98              0.88        128.76                24.28         0.560          pass              0.207             43.7                           0.242               -2.82             -0.246           downtrend_blocked_streak           False                  False
  INSM           73.68               38            1.02              0.67         93.93                54.02         0.558          pass              0.409             55.3                           0.653              -12.22             -0.913            downtrend_blocked_slope           False                  False
   EXC           72.73               11            0.80              0.26         45.64                19.68         0.558          pass              0.189             42.1                           0.271               -0.90             -0.190                                 ok           False                  False
  REGN           80.00               20            1.64              7.27        632.33                43.33         0.558          pass              0.124              0.6                           0.022               -2.16             -0.110           downtrend_blocked_streak           False                  False
  GOOG           87.50                8            1.99              5.10        363.57                28.09         0.553          pass              0.329             24.5                           0.176               -6.52             -0.818 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-06-08T10:25:01.721372-04:00 early_entry_1025 early_entry_shadow     {"contract_symbol": "DASH260717C00155000", "current_drop_pct": 0.62, "early_entry_score": 0.835, "early_reclaim_pct": 82.2, "entry_ask": 13.05, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.275, "hypothetical_budget": 8805.38, "hypothetical_contracts": 7, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1085.0, "option_spread_pct": 12.63, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.835, "early_reclaim_pct": 82.2, "matched_signals": 41, "recovery_stability_score": 0.701, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.501, "trend_health_status": "ok"}, {"current_drop_pct": 0.52, "early_entry_score": 0.704, "early_reclaim_pct": 73.4, "matched_signals": 38, "recovery_stability_score": 0.641, "success_rate": 89.47, "ticker": "VRTX", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:20:04.721849-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                   {"contract_symbol": "DASH260717C00155000", "current_drop_pct": 0.55, "early_entry_score": 0.841, "early_reclaim_pct": 84.0, "entry_ask": 13.05, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 12.025, "hypothetical_budget": 8805.38, "hypothetical_contracts": 7, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 1085.0, "option_spread_pct": 17.05, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.506, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.841, "early_reclaim_pct": 84.0, "matched_signals": 41, "recovery_stability_score": 0.749, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.506, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:15:04.701232-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                    {"contract_symbol": "PANW260717C00250000", "current_drop_pct": 0.55, "early_entry_score": 0.806, "early_reclaim_pct": 80.5, "entry_ask": 30.2, "entry_bid": 26.25, "entry_mode": "early", "entry_option_price": 28.225, "hypothetical_budget": 8805.38, "hypothetical_contracts": 3, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 502.0, "option_spread_pct": 13.99, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.63, "shadow_only": true, "success_rate": 92.11, "ticker": "PANW", "timing_score": 0.553, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.806, "early_reclaim_pct": 80.5, "matched_signals": 38, "recovery_stability_score": 0.63, "success_rate": 92.11, "ticker": "PANW", "timing_score": 0.553, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-08T10:10:04.752289-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.63, "early_entry_score": 0.814, "early_reclaim_pct": 66.4, "entry_ask": 9.9, "entry_bid": 8.4, "entry_mode": "early", "entry_option_price": 9.15, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 16.39, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.616, "shadow_only": true, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.814, "early_reclaim_pct": 66.4, "matched_signals": 35, "recovery_stability_score": 0.616, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.485, "trend_health_status": "ok"}, {"current_drop_pct": 0.68, "early_entry_score": 0.768, "early_reclaim_pct": 75.9, "matched_signals": 36, "recovery_stability_score": 0.675, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.558, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:05:01.849254-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ADP260717C00230000", "current_drop_pct": 0.58, "early_entry_score": 0.822, "early_reclaim_pct": 68.7, "entry_ask": 9.9, "entry_bid": 8.4, "entry_mode": "early", "entry_option_price": 9.15, "hypothetical_budget": 8805.38, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 263.0, "option_spread_pct": 16.39, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.822, "early_reclaim_pct": 68.7, "matched_signals": 35, "recovery_stability_score": 0.633, "success_rate": 97.14, "ticker": "ADP", "timing_score": 0.488, "trend_health_status": "ok"}, {"current_drop_pct": 0.68, "early_entry_score": 0.767, "early_reclaim_pct": 75.7, "matched_signals": 36, "recovery_stability_score": 0.788, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.557, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-08T10:00:02.881266-04:00 early_entry_1000 early_entry_shadow                            {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.7, "entry_ask": 15.4, "entry_bid": 14.0, "entry_mode": "early", "entry_option_price": 14.7, "hypothetical_budget": 8805.38, "hypothetical_contracts": 5, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 1806.0, "option_spread_pct": 9.52, "option_volume": 195.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.802, "shadow_only": true, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.833, "early_reclaim_pct": 81.7, "matched_signals": 40, "recovery_stability_score": 0.802, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.542, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.821, "early_reclaim_pct": 77.9, "matched_signals": 41, "recovery_stability_score": 0.585, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-06T02:55:05.037778-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:50:04.162002-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:45:02.082249-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"holiday_name": null, "reason": "weekend"}
2026-06-06T02:40:02.201062-04:00   share_ext_0240      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608102501)

</details>
