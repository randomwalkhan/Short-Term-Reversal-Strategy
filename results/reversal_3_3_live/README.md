# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 11:10:06 EDT`
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
  MSFT          100.00               19            1.26              4.68        530.94                21.62         0.509            pass              0.621             36.8                           0.680                0.70             -0.071                                 ok            True                  False
  SNPS           60.00                5            3.65             11.53        446.25                54.60         0.536            pass              0.083              9.8                           0.311              -12.66             -1.579 downtrend_blocked_slope_and_streak           False                  False
   MAR           71.43                7            2.09              5.92        401.46                19.25         0.497 below_threshold              0.057              2.4                           0.095                9.54              1.105                                 ok           False                  False
  NXPI           87.50               16            2.07              3.51        240.85                33.60         0.486 below_threshold              0.379             30.1                           0.235                2.71              0.563                                 ok           False                  False
  DXCM           88.89               18            1.68              0.94         79.86                36.58         0.482 below_threshold              0.480             47.0                           0.464               -6.51             -0.435 downtrend_blocked_slope_and_streak           False                  False
  MELI           82.14               28            1.63             21.13       1845.83                40.26         0.480 below_threshold              0.314             29.5                           0.465               -1.72             -0.204                                 ok           False                  False
  QCOM           90.00               20            2.41              3.00        176.68                39.95         0.475 below_threshold              0.465             28.2                           0.174               -1.32             -0.027                                 ok           False                  False
  SHOP           80.00               20            1.76              2.15        173.37                40.35         0.473 below_threshold              0.240             42.1                           0.544                4.04              0.091                                 ok           False                  False
   APP           85.29               34            1.51              2.83        266.69                46.80         0.457 below_threshold              0.441             31.4                           0.270               -5.80             -0.386            downtrend_blocked_slope           False                  False
 GOOGL           66.67                6            2.36              5.53        332.39                18.62         0.452 below_threshold              0.102             18.9                           0.267               -6.15             -0.634            downtrend_blocked_slope           False                  False
  CSCO           25.00                4            2.99              2.25        106.30                31.32         0.450 below_threshold              0.067              7.2                           0.273               -9.44             -1.214 downtrend_blocked_slope_and_streak           False                  False
  CRWD           83.78               37            1.16              1.95        238.51                50.83         0.447 below_threshold              0.472             48.8                           0.353              -10.06             -1.714 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-22T11:10:06.105210-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.65, "early_entry_score": 0.849, "early_reclaim_pct": 77.9, "entry_ask": 1.95, "entry_bid": 1.65, "entry_mode": "early", "entry_option_price": 1.8, "hypothetical_budget": 72415.9, "hypothetical_contracts": 402, "matched_signals": 36, "option_liquidity_status": "wide_spread", "option_open_interest": 1598.0, "option_spread_pct": 16.67, "option_volume": 20.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.834, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.849, "early_reclaim_pct": 77.9, "matched_signals": 36, "recovery_stability_score": 0.834, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T11:05:03.636550-04:00 early_entry_1105 early_entry_shadow                         {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.78, "early_entry_score": 0.822, "early_reclaim_pct": 73.4, "entry_ask": 1.8, "entry_bid": 1.6, "entry_mode": "early", "entry_option_price": 1.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 425, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1598.0, "option_spread_pct": 11.76, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.844, "shadow_only": true, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.822, "early_reclaim_pct": 73.4, "matched_signals": 34, "recovery_stability_score": 0.844, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:00:05.675210-04:00 early_entry_1100 early_entry_shadow                    {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.59, "early_entry_score": 0.867, "early_reclaim_pct": 79.9, "entry_ask": 1.1, "entry_bid": 1.05, "entry_mode": "early", "entry_option_price": 1.075, "hypothetical_budget": 72415.9, "hypothetical_contracts": 673, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 4.65, "option_volume": 265.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.891, "shadow_only": true, "success_rate": 97.37, "ticker": "FAST", "timing_score": 0.409, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.867, "early_reclaim_pct": 79.9, "matched_signals": 38, "recovery_stability_score": 0.891, "success_rate": 97.37, "ticker": "FAST", "timing_score": 0.409, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:55:05.770000-04:00 early_entry_1055 early_entry_shadow                      {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.77, "early_entry_score": 0.829, "early_reclaim_pct": 73.7, "entry_ask": 1.1, "entry_bid": 1.0, "entry_mode": "early", "entry_option_price": 1.05, "hypothetical_budget": 72415.9, "hypothetical_contracts": 689, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 9.52, "option_volume": 248.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.852, "shadow_only": true, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.829, "early_reclaim_pct": 73.7, "matched_signals": 35, "recovery_stability_score": 0.852, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:50:04.903507-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-22T10:45:04.357952-04:00 early_entry_1045 early_entry_shadow                        {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.9, "early_entry_score": 0.757, "early_reclaim_pct": 69.5, "entry_ask": 20.6, "entry_bid": 18.0, "entry_mode": "early", "entry_option_price": 19.3, "hypothetical_budget": 72415.9, "hypothetical_contracts": 37, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 13.47, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.757, "early_reclaim_pct": 69.5, "matched_signals": 31, "recovery_stability_score": 0.592, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:40:06.149138-04:00 early_entry_1040 early_entry_shadow                      {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.93, "early_entry_score": 0.742, "early_reclaim_pct": 68.5, "entry_ask": 20.6, "entry_bid": 18.0, "entry_mode": "early", "entry_option_price": 19.3, "hypothetical_budget": 72415.9, "hypothetical_contracts": 37, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 13.47, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.554, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.93, "early_entry_score": 0.742, "early_reclaim_pct": 68.5, "matched_signals": 30, "recovery_stability_score": 0.554, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:35:05.575135-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-22T10:30:01.703410-04:00 early_entry_1030 early_entry_shadow                     {"contract_symbol": "QCOM261218C00180000", "current_drop_pct": 0.69, "early_entry_score": 0.815, "early_reclaim_pct": 79.5, "entry_ask": 13.6, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.125, "hypothetical_budget": 72415.9, "hypothetical_contracts": 55, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1533.0, "option_spread_pct": 7.24, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.665, "shadow_only": true, "success_rate": 93.94, "ticker": "QCOM", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.815, "early_reclaim_pct": 79.5, "matched_signals": 33, "recovery_stability_score": 0.665, "success_rate": 93.94, "ticker": "QCOM", "timing_score": 0.51, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:25:04.750468-04:00 early_entry_1025 early_entry_shadow                     {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.82, "early_entry_score": 0.766, "early_reclaim_pct": 72.3, "entry_ask": 21.0, "entry_bid": 18.5, "entry_mode": "early", "entry_option_price": 19.75, "hypothetical_budget": 72415.9, "hypothetical_contracts": 36, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 12.66, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.766, "early_reclaim_pct": 72.3, "matched_signals": 31, "recovery_stability_score": 0.626, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022111006)

</details>
