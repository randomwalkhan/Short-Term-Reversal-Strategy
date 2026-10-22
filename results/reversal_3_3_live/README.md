# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 14:00:04 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSFT          100.00               11            1.79              6.69        530.08                21.62         0.525            pass              0.488              9.7                           0.190                0.15             -0.096                                 ok            True                  False
  TEAM          100.00               39            0.41              0.65        225.23                49.42         0.530            pass              0.872             75.4                           0.531               10.32              1.003                                 ok           False                  False
  MELI           72.73               11            2.28             29.57       1842.21                40.26         0.529            pass              0.113             17.8                           0.408               -2.37             -0.234                                 ok           False                  False
  QCOM           90.91               11            2.94              3.66        176.39                39.95         0.497 below_threshold              0.385             12.7                           0.259               -1.86             -0.052                                 ok           False                  False
  DXCM          100.00                3            3.16              1.78         79.50                36.58         0.494 below_threshold              0.477              9.1                           0.191               -7.93             -0.504 downtrend_blocked_slope_and_streak           False                  False
   MAR           84.21               19            1.09              3.09        402.68                19.25         0.493 below_threshold              0.385             54.5                           0.630               10.67              1.151                                 ok           False                  False
  CSCO           40.00                5            2.59              1.95        106.43                31.32         0.482 below_threshold              0.122             24.5                           0.399               -9.06             -1.195 downtrend_blocked_slope_and_streak           False                  False
  NXPI           92.31               26            1.43              2.43        241.32                33.60         0.469 below_threshold              0.637             51.7                           0.489                3.38              0.592                                 ok           False                  False
  CRWD           84.21               38            0.79              1.32        238.77                50.83         0.464 below_threshold              0.541             65.2                           0.358               -9.72             -1.697 downtrend_blocked_slope_and_streak           False                  False
   APP           86.11               36            1.27              2.39        266.88                46.80         0.458 below_threshold              0.534             50.7                           0.588               -5.58             -0.375            downtrend_blocked_slope           False                  False
  SNPS           50.00                4            4.90             15.49        444.55                54.60         0.453 below_threshold              0.045              0.0                           0.163              -13.80             -1.638 downtrend_blocked_slope_and_streak           False                  False
  MCHP           87.50               16            3.08              1.67         76.44                39.64         0.439 below_threshold              0.370             28.5                           0.323               -0.99              0.144                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-22T12:00:04.790529-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.63, "early_entry_score": 0.851, "early_reclaim_pct": 78.6, "entry_ask": 1.95, "entry_bid": 1.75, "entry_mode": "early", "entry_option_price": 1.85, "hypothetical_budget": 72415.9, "hypothetical_contracts": 391, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1598.0, "option_spread_pct": 10.81, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.678, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.851, "early_reclaim_pct": 78.6, "matched_signals": 36, "recovery_stability_score": 0.678, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.735, "early_reclaim_pct": 66.4, "matched_signals": 30, "recovery_stability_score": 0.625, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:55:05.698440-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "entry_ask": 1.3, "entry_bid": 1.15, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 12.24, "option_volume": 356.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "matched_signals": 36, "recovery_stability_score": 0.623, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:50:06.422891-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.63, "early_entry_score": 0.851, "early_reclaim_pct": 78.6, "entry_ask": 2.85, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 2.725, "hypothetical_budget": 72415.9, "hypothetical_contracts": 265, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 5099.0, "option_spread_pct": 9.17, "option_volume": 183.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.637, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.851, "early_reclaim_pct": 78.6, "matched_signals": 36, "recovery_stability_score": 0.637, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:45:04.817612-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "entry_ask": 3.0, "entry_bid": 2.7, "entry_mode": "early", "entry_option_price": 2.85, "hypothetical_budget": 72415.9, "hypothetical_contracts": 254, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 5099.0, "option_spread_pct": 10.53, "option_volume": 173.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "matched_signals": 36, "recovery_stability_score": 0.603, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:40:06.326699-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "entry_ask": 2.0, "entry_bid": 1.75, "entry_mode": "early", "entry_option_price": 1.875, "hypothetical_budget": 72415.9, "hypothetical_contracts": 386, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1598.0, "option_spread_pct": 13.33, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.617, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "matched_signals": 36, "recovery_stability_score": 0.617, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:35:01.699329-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.75, "early_entry_score": 0.831, "early_reclaim_pct": 74.4, "entry_ask": 1.3, "entry_bid": 1.15, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 12.24, "option_volume": 352.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.641, "shadow_only": true, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.75, "early_entry_score": 0.831, "early_reclaim_pct": 74.4, "matched_signals": 35, "recovery_stability_score": 0.641, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:30:05.774807-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.79, "early_entry_score": 0.815, "early_reclaim_pct": 73.1, "entry_ask": 1.25, "entry_bid": 1.2, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 4.08, "option_volume": 349.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.672, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.815, "early_reclaim_pct": 73.1, "matched_signals": 33, "recovery_stability_score": 0.672, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:25:06.800091-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.65, "early_entry_score": 0.849, "early_reclaim_pct": 77.9, "entry_ask": 1.3, "entry_bid": 1.15, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 12.24, "option_volume": 348.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.74, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.849, "early_reclaim_pct": 77.9, "matched_signals": 36, "recovery_stability_score": 0.74, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:20:06.050823-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.55, "early_entry_score": 0.877, "early_reclaim_pct": 81.2, "entry_ask": 1.3, "entry_bid": 1.2, "entry_mode": "early", "entry_option_price": 1.25, "hypothetical_budget": 72415.9, "hypothetical_contracts": 579, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 8.0, "option_volume": 302.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 97.44, "ticker": "FAST", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.877, "early_reclaim_pct": 81.2, "matched_signals": 39, "recovery_stability_score": 0.762, "success_rate": 97.44, "ticker": "FAST", "timing_score": 0.405, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:15:05.450000-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                              {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.76, "early_entry_score": 0.83, "early_reclaim_pct": 74.0, "entry_ask": 2.1, "entry_bid": 1.7, "entry_mode": "early", "entry_option_price": 1.9, "hypothetical_budget": 72415.9, "hypothetical_contracts": 381, "matched_signals": 35, "option_liquidity_status": "wide_spread", "option_open_interest": 1598.0, "option_spread_pct": 21.05, "option_volume": 20.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.76, "shadow_only": true, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.83, "early_reclaim_pct": 74.0, "matched_signals": 35, "recovery_stability_score": 0.76, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022140004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022140004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022140004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022140004)

</details>
