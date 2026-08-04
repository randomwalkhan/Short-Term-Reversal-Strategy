# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 11:45:01 EDT`
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
   ROP           93.33               30            0.69              1.90        391.76                47.45         0.578          pass              0.752             68.4                           0.736               11.17              1.491                                 ok            True                   True
  DXCM           88.89               36            0.65              0.40         87.14                57.42         0.557          pass              0.611             48.2                           0.284               16.04              1.963                                 ok            True                  False
   PEP           83.33               24            0.75              0.73        139.32                26.13         0.540          pass              0.411             58.2                           0.680                2.66              0.386                                 ok            True                  False
  ALNY           77.78               18            2.02              3.11        219.00               126.96         0.818          pass              0.174             12.9                           0.147              -20.44             -2.951            downtrend_blocked_slope           False                  False
  ISRG           66.67               12            2.48              6.52        372.62                72.79         0.649          pass              0.100              7.1                           0.172                4.58              0.798                                 ok           False                  False
  TMUS           92.31               26            0.93              1.16        176.59                55.96         0.640          pass              0.627             42.7                           0.351               -8.04             -0.666            downtrend_blocked_slope           False                  False
  GEHC           95.12               41            0.19              0.09         69.69                58.11         0.612          pass              0.920             86.2                           0.776               12.24              1.653                                 ok           False                  False
  AMZN           69.23               13            2.40              4.77        281.97                60.32         0.591          pass              0.162             27.5                           0.350               11.98              1.472                                 ok           False                  False
  MDLZ           91.67               24            0.42              0.18         61.65                32.17         0.588          pass              0.691             75.9                           0.708                2.69              0.411                                 ok           False                  False
   MAR          100.00               20            1.12              2.71        345.67                34.81         0.580          pass              0.631             35.5                           0.330               -6.76             -0.489 downtrend_blocked_slope_and_streak           False                  False
  META           80.77               26            1.31              5.43        587.91                55.17         0.546          pass              0.325             47.7                           0.480               -9.53             -1.100 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00               25            0.45              0.14         45.57                21.77         0.533          pass              0.808             84.9                           0.708               -1.01             -0.295                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-08-04T11:45:01.424926-04:00 early_entry_1145 early_entry_shadow              {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.55, "early_entry_score": 0.827, "early_reclaim_pct": 87.6, "entry_ask": 37.4, "entry_bid": 34.0, "entry_mode": "early", "entry_option_price": 35.7, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 9.52, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.429, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.827, "early_reclaim_pct": 87.6, "matched_signals": 39, "recovery_stability_score": 0.69, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.429, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.752, "early_reclaim_pct": 68.4, "matched_signals": 30, "recovery_stability_score": 0.736, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.578, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:40:04.541695-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.51, "early_entry_score": 0.83, "early_reclaim_pct": 88.3, "entry_ask": 40.8, "entry_bid": 34.6, "entry_mode": "early", "entry_option_price": 37.7, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 16.45, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.83, "early_reclaim_pct": 88.3, "matched_signals": 39, "recovery_stability_score": 0.715, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.431, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.741, "early_reclaim_pct": 64.9, "matched_signals": 30, "recovery_stability_score": 0.733, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.573, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:35:05.362040-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.8, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.711, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "matched_signals": 30, "recovery_stability_score": 0.711, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:30:01.403472-04:00 early_entry_1130 early_entry_shadow  {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.58, "early_entry_score": 0.808, "early_reclaim_pct": 70.3, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.585, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.808, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.585, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}, {"current_drop_pct": 0.71, "early_entry_score": 0.749, "early_reclaim_pct": 67.3, "matched_signals": 30, "recovery_stability_score": 0.694, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:25:01.272769-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:20:01.453908-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:15:06.199893-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "matched_signals": 35, "recovery_stability_score": 0.657, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:10:06.366472-04:00 early_entry_1110 early_entry_shadow             {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.6, "early_entry_score": 0.812, "early_reclaim_pct": 86.4, "entry_ask": 37.3, "entry_bid": 32.7, "entry_mode": "early", "entry_option_price": 35.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 13.14, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 92.11, "ticker": "REGN", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.812, "early_reclaim_pct": 86.4, "matched_signals": 38, "recovery_stability_score": 0.749, "success_rate": 92.11, "ticker": "REGN", "timing_score": 0.432, "trend_health_status": "ok"}, {"current_drop_pct": 0.56, "early_entry_score": 0.801, "early_reclaim_pct": 60.2, "matched_signals": 36, "recovery_stability_score": 0.601, "success_rate": 94.44, "ticker": "GEHC", "timing_score": 0.62, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:05:01.401227-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 70.4, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.629, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 70.4, "matched_signals": 35, "recovery_stability_score": 0.629, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:00:04.371634-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.56, "early_entry_score": 0.812, "early_reclaim_pct": 71.4, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.812, "early_reclaim_pct": 71.4, "matched_signals": 35, "recovery_stability_score": 0.607, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804114501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804114501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804114501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804114501)

</details>
