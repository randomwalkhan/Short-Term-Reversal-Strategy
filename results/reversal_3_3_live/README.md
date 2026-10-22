# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 11:30:05 EDT`
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
  MSFT          100.00               13            1.49              5.57        530.56                21.62         0.531            pass              0.547             24.8                           0.474                0.45             -0.082                                 ok            True                  False
  SNPS           60.00                5            3.77             11.91        446.09                54.60         0.529            pass              0.073              6.8                           0.270              -12.77             -1.584 downtrend_blocked_slope_and_streak           False                  False
   MAR           71.43                7            1.87              5.29        401.73                19.25         0.507            pass              0.117             22.0                           0.360                9.79              1.115                                 ok           False                  False
  DXCM           88.24               17            1.72              0.97         79.85                36.58         0.485 below_threshold              0.452             45.7                           0.412               -6.55             -0.437 downtrend_blocked_slope_and_streak           False                  False
  MELI           82.76               29            1.55             20.17       1846.23                40.26         0.479 below_threshold              0.346             32.7                           0.483               -1.65             -0.200                                 ok           False                  False
  NXPI           91.30               23            1.62              2.74        241.18                33.60         0.475 below_threshold              0.572             45.4                           0.400                3.19              0.584                                 ok           False                  False
  QCOM           91.30               23            2.17              2.70        176.80                39.95         0.473 below_threshold              0.541             35.2                           0.349               -1.09             -0.016                                 ok           False                  False
  SHOP           77.78               18            2.04              2.48        173.23                40.35         0.467 below_threshold              0.199             33.1                           0.411                3.76              0.078                                 ok           False                  False
 GOOGL           66.67                6            2.22              5.20        332.53                18.62         0.460 below_threshold              0.117             23.7                           0.343               -6.02             -0.628            downtrend_blocked_slope           False                  False
  CRWD           86.36               44            0.34              0.57        239.10                50.83         0.459 below_threshold              0.671             85.1                           0.650               -9.31             -1.677 downtrend_blocked_slope_and_streak           False                  False
   APP           85.71               35            1.40              2.63        266.77                46.80         0.458 below_threshold              0.474             36.3                           0.281               -5.70             -0.381            downtrend_blocked_slope           False                  False
  CSCO           25.00                4            2.86              2.15        106.34                31.32         0.457 below_threshold              0.080             11.4                           0.388               -9.31             -1.207 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-22T11:30:05.774807-04:00 early_entry_1130 early_entry_shadow                    {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.79, "early_entry_score": 0.815, "early_reclaim_pct": 73.1, "entry_ask": 1.25, "entry_bid": 1.2, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 4.08, "option_volume": 349.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.672, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.815, "early_reclaim_pct": 73.1, "matched_signals": 33, "recovery_stability_score": 0.672, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:25:06.800091-04:00 early_entry_1125 early_entry_shadow                     {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.65, "early_entry_score": 0.849, "early_reclaim_pct": 77.9, "entry_ask": 1.3, "entry_bid": 1.15, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 12.24, "option_volume": 348.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.74, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.849, "early_reclaim_pct": 77.9, "matched_signals": 36, "recovery_stability_score": 0.74, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:20:06.050823-04:00 early_entry_1120 early_entry_shadow                       {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.55, "early_entry_score": 0.877, "early_reclaim_pct": 81.2, "entry_ask": 1.3, "entry_bid": 1.2, "entry_mode": "early", "entry_option_price": 1.25, "hypothetical_budget": 72415.9, "hypothetical_contracts": 579, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 8.0, "option_volume": 302.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 97.44, "ticker": "FAST", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.877, "early_reclaim_pct": 81.2, "matched_signals": 39, "recovery_stability_score": 0.762, "success_rate": 97.44, "ticker": "FAST", "timing_score": 0.405, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:15:05.450000-04:00 early_entry_1115 early_entry_shadow       {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.76, "early_entry_score": 0.83, "early_reclaim_pct": 74.0, "entry_ask": 2.1, "entry_bid": 1.7, "entry_mode": "early", "entry_option_price": 1.9, "hypothetical_budget": 72415.9, "hypothetical_contracts": 381, "matched_signals": 35, "option_liquidity_status": "wide_spread", "option_open_interest": 1598.0, "option_spread_pct": 21.05, "option_volume": 20.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.76, "shadow_only": true, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.83, "early_reclaim_pct": 74.0, "matched_signals": 35, "recovery_stability_score": 0.76, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T11:10:06.105210-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.65, "early_entry_score": 0.849, "early_reclaim_pct": 77.9, "entry_ask": 1.95, "entry_bid": 1.65, "entry_mode": "early", "entry_option_price": 1.8, "hypothetical_budget": 72415.9, "hypothetical_contracts": 402, "matched_signals": 36, "option_liquidity_status": "wide_spread", "option_open_interest": 1598.0, "option_spread_pct": 16.67, "option_volume": 20.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.834, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.849, "early_reclaim_pct": 77.9, "matched_signals": 36, "recovery_stability_score": 0.834, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T11:05:03.636550-04:00 early_entry_1105 early_entry_shadow                         {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.78, "early_entry_score": 0.822, "early_reclaim_pct": 73.4, "entry_ask": 1.8, "entry_bid": 1.6, "entry_mode": "early", "entry_option_price": 1.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 425, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1598.0, "option_spread_pct": 11.76, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.844, "shadow_only": true, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.822, "early_reclaim_pct": 73.4, "matched_signals": 34, "recovery_stability_score": 0.844, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:00:05.675210-04:00 early_entry_1100 early_entry_shadow                    {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.59, "early_entry_score": 0.867, "early_reclaim_pct": 79.9, "entry_ask": 1.1, "entry_bid": 1.05, "entry_mode": "early", "entry_option_price": 1.075, "hypothetical_budget": 72415.9, "hypothetical_contracts": 673, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 4.65, "option_volume": 265.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.891, "shadow_only": true, "success_rate": 97.37, "ticker": "FAST", "timing_score": 0.409, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.867, "early_reclaim_pct": 79.9, "matched_signals": 38, "recovery_stability_score": 0.891, "success_rate": 97.37, "ticker": "FAST", "timing_score": 0.409, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:55:05.770000-04:00 early_entry_1055 early_entry_shadow                      {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.77, "early_entry_score": 0.829, "early_reclaim_pct": 73.7, "entry_ask": 1.1, "entry_bid": 1.0, "entry_mode": "early", "entry_option_price": 1.05, "hypothetical_budget": 72415.9, "hypothetical_contracts": 689, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 9.52, "option_volume": 248.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.852, "shadow_only": true, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.829, "early_reclaim_pct": 73.7, "matched_signals": 35, "recovery_stability_score": 0.852, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:50:04.903507-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-22T10:45:04.357952-04:00 early_entry_1045 early_entry_shadow                        {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.9, "early_entry_score": 0.757, "early_reclaim_pct": 69.5, "entry_ask": 20.6, "entry_bid": 18.0, "entry_mode": "early", "entry_option_price": 19.3, "hypothetical_budget": 72415.9, "hypothetical_contracts": 37, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 13.47, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.757, "early_reclaim_pct": 69.5, "matched_signals": 31, "recovery_stability_score": 0.592, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022113005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022113005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022113005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022113005)

</details>
