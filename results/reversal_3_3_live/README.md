# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 11:50:01 EDT`
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
   ROP           90.91               33            0.60              1.66        391.86                47.45         0.560          pass              0.717             72.3                           0.747               11.27              1.495                                 ok            True                   True
  DXCM           88.89               36            0.71              0.43         87.12                57.42         0.553          pass              0.597             43.6                           0.252               15.97              1.961                                 ok            True                  False
   PEP           83.33               24            0.76              0.74        139.31                26.13         0.539          pass              0.409             57.6                           0.679                2.64              0.386                                 ok            True                  False
  ALNY           77.78               18            1.99              3.07        219.02               126.96         0.820          pass              0.178             14.1                           0.153              -20.42             -2.950            downtrend_blocked_slope           False                  False
  ISRG           69.23               13            2.33              6.14        372.78                72.79         0.655          pass              0.123             12.6                           0.291                4.74              0.805                                 ok           False                  False
 CMCSA           87.50               24            0.08              0.01         24.55                43.78         0.634          pass              0.640             94.4                           0.664                3.07              0.715                                 ok           False                  False
  TMUS           92.31               26            1.06              1.32        176.52                55.96         0.631          pass              0.602             34.8                           0.305               -8.16             -0.672            downtrend_blocked_slope           False                  False
  GEHC           95.12               41            0.16              0.08         69.70                58.11         0.614          pass              0.926             88.3                           0.790               12.27              1.654                                 ok           False                  False
  AMZN           73.33               15            2.34              4.64        282.03                60.32         0.589          pass              0.181             29.5                           0.333               12.05              1.475                                 ok           False                  False
  MDLZ           92.31               26            0.29              0.13         61.68                32.17         0.584          pass              0.743             83.3                           0.742                2.82              0.417                                 ok           False                  False
   MAR          100.00               22            1.04              2.53        345.74                34.81         0.572          pass              0.657             39.8                           0.505               -6.69             -0.485 downtrend_blocked_slope_and_streak           False                  False
  META           81.48               27            1.23              5.09        588.06                55.17         0.546          pass              0.360             51.0                           0.599               -9.45             -1.097 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-08-04T11:50:01.376014-04:00 early_entry_1150 early_entry_shadow               {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.53, "early_entry_score": 0.828, "early_reclaim_pct": 87.9, "entry_ask": 36.7, "entry_bid": 34.0, "entry_mode": "early", "entry_option_price": 35.35, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 7.64, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.828, "early_reclaim_pct": 87.9, "matched_signals": 39, "recovery_stability_score": 0.646, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.43, "trend_health_status": "ok"}, {"current_drop_pct": 0.6, "early_entry_score": 0.717, "early_reclaim_pct": 72.3, "matched_signals": 33, "recovery_stability_score": 0.747, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.56, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:45:01.424926-04:00 early_entry_1145 early_entry_shadow              {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.55, "early_entry_score": 0.827, "early_reclaim_pct": 87.6, "entry_ask": 37.4, "entry_bid": 34.0, "entry_mode": "early", "entry_option_price": 35.7, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 9.52, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.429, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.827, "early_reclaim_pct": 87.6, "matched_signals": 39, "recovery_stability_score": 0.69, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.429, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.752, "early_reclaim_pct": 68.4, "matched_signals": 30, "recovery_stability_score": 0.736, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.578, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:40:04.541695-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.51, "early_entry_score": 0.83, "early_reclaim_pct": 88.3, "entry_ask": 40.8, "entry_bid": 34.6, "entry_mode": "early", "entry_option_price": 37.7, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 16.45, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.83, "early_reclaim_pct": 88.3, "matched_signals": 39, "recovery_stability_score": 0.715, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.431, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.741, "early_reclaim_pct": 64.9, "matched_signals": 30, "recovery_stability_score": 0.733, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.573, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:35:05.362040-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.8, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.711, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "matched_signals": 30, "recovery_stability_score": 0.711, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:30:01.403472-04:00 early_entry_1130 early_entry_shadow  {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.58, "early_entry_score": 0.808, "early_reclaim_pct": 70.3, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.585, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.808, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.585, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}, {"current_drop_pct": 0.71, "early_entry_score": 0.749, "early_reclaim_pct": 67.3, "matched_signals": 30, "recovery_stability_score": 0.694, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:25:01.272769-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:20:01.453908-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:15:06.199893-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "matched_signals": 35, "recovery_stability_score": 0.657, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:10:06.366472-04:00 early_entry_1110 early_entry_shadow             {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.6, "early_entry_score": 0.812, "early_reclaim_pct": 86.4, "entry_ask": 37.3, "entry_bid": 32.7, "entry_mode": "early", "entry_option_price": 35.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 13.14, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 92.11, "ticker": "REGN", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.812, "early_reclaim_pct": 86.4, "matched_signals": 38, "recovery_stability_score": 0.749, "success_rate": 92.11, "ticker": "REGN", "timing_score": 0.432, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.801, "early_reclaim_pct": 60.2, "matched_signals": 36, "recovery_stability_score": 0.601, "success_rate": 94.44, "ticker": "GEHC", "timing_score": 0.62, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:05:01.401227-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 70.4, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.629, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 70.4, "matched_signals": 35, "recovery_stability_score": 0.629, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804115001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804115001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804115001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804115001)

</details>
