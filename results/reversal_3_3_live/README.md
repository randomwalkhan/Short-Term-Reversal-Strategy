# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 10:45:04 EDT`
Last processed slot: `early_entry_1045`

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
  MSFT          100.00               11            1.76              6.56        530.14                21.62         0.527            pass              0.494             11.6                           0.216                0.19             -0.095                                 ok            True                  False
  QCOM           92.00               25            1.40              1.75        177.21                39.95         0.510            pass              0.645             58.1                           0.466               -0.31              0.019                                 ok            True                  False
  SNPS           50.00                6            3.52             11.12        446.42                54.60         0.527            pass              0.091             12.9                           0.214              -12.55             -1.573 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               44            0.13              0.20        225.42                49.42         0.517            pass              0.929             92.4                           0.438               10.63              1.016                                 ok           False                  False
  MELI           73.33               15            2.15             27.96       1842.90                40.26         0.516            pass              0.105              6.7                           0.146               -2.25             -0.228                                 ok           False                  False
   MAR           62.50                8            1.84              5.19        401.77                19.25         0.496 below_threshold              0.093             14.3                           0.215                9.83              1.117                                 ok           False                  False
  FAST           93.75               16            1.43              0.52         52.27                19.95         0.485 below_threshold              0.609             51.3                           0.729                2.48              0.210                                 ok           False                  False
  NXPI           93.55               31            0.90              1.53        241.70                33.60         0.473 below_threshold              0.757             69.5                           0.592                3.94              0.617                                 ok           False                   True
  DXCM           90.91               22            1.58              0.89         79.88                36.58         0.466 below_threshold              0.567             50.0                           0.430               -6.42             -0.431 downtrend_blocked_slope_and_streak           False                  False
  MSTR           85.71               21            2.93              3.15        152.13                66.76         0.466 below_threshold              0.441             56.4                           0.711               -1.64             -0.525                                 ok           False                  False
  SHOP           77.78               18            2.07              2.52        173.21                40.35         0.465 below_threshold              0.196             32.2                           0.300                3.72              0.077                                 ok           False                  False
 GOOGL           66.67                6            2.30              5.40        332.45                18.62         0.455 below_threshold              0.108             20.7                           0.211               -6.10             -0.632            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-22T10:45:04.357952-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.9, "early_entry_score": 0.757, "early_reclaim_pct": 69.5, "entry_ask": 20.6, "entry_bid": 18.0, "entry_mode": "early", "entry_option_price": 19.3, "hypothetical_budget": 72415.9, "hypothetical_contracts": 37, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 13.47, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.757, "early_reclaim_pct": 69.5, "matched_signals": 31, "recovery_stability_score": 0.592, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:40:06.149138-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.93, "early_entry_score": 0.742, "early_reclaim_pct": 68.5, "entry_ask": 20.6, "entry_bid": 18.0, "entry_mode": "early", "entry_option_price": 19.3, "hypothetical_budget": 72415.9, "hypothetical_contracts": 37, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 13.47, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.554, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.93, "early_entry_score": 0.742, "early_reclaim_pct": 68.5, "matched_signals": 30, "recovery_stability_score": 0.554, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:35:05.575135-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-22T10:30:01.703410-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                  {"contract_symbol": "QCOM261218C00180000", "current_drop_pct": 0.69, "early_entry_score": 0.815, "early_reclaim_pct": 79.5, "entry_ask": 13.6, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.125, "hypothetical_budget": 72415.9, "hypothetical_contracts": 55, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1533.0, "option_spread_pct": 7.24, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.665, "shadow_only": true, "success_rate": 93.94, "ticker": "QCOM", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.815, "early_reclaim_pct": 79.5, "matched_signals": 33, "recovery_stability_score": 0.665, "success_rate": 93.94, "ticker": "QCOM", "timing_score": 0.51, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:25:04.750468-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                  {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.82, "early_entry_score": 0.766, "early_reclaim_pct": 72.3, "entry_ask": 21.0, "entry_bid": 18.5, "entry_mode": "early", "entry_option_price": 19.75, "hypothetical_budget": 72415.9, "hypothetical_contracts": 36, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 12.66, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.766, "early_reclaim_pct": 72.3, "matched_signals": 31, "recovery_stability_score": 0.626, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:20:06.839812-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.67, "early_entry_score": 0.794, "early_reclaim_pct": 77.5, "entry_ask": 20.5, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 19.3, "hypothetical_budget": 72415.9, "hypothetical_contracts": 37, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 12.44, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.794, "early_reclaim_pct": 77.5, "matched_signals": 32, "recovery_stability_score": 0.673, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:15:05.850779-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 1.05, "early_entry_score": 0.729, "early_reclaim_pct": 64.4, "entry_ask": 19.8, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 18.95, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 8.97, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.729, "early_reclaim_pct": 64.4, "matched_signals": 30, "recovery_stability_score": 0.636, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:10:04.040588-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.98, "early_entry_score": 0.737, "early_reclaim_pct": 66.9, "entry_ask": 19.8, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 18.95, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 8.97, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.737, "early_reclaim_pct": 66.9, "matched_signals": 30, "recovery_stability_score": 0.722, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:05:04.719649-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "PCAR261218C00110000", "current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "entry_ask": 6.3, "entry_bid": 4.1, "entry_mode": "early", "entry_option_price": 5.2, "hypothetical_budget": 72415.9, "hypothetical_contracts": 139, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 42.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "matched_signals": 43, "recovery_stability_score": 0.768, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.7, "early_reclaim_pct": 81.3, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 88.89, "ticker": "NXPI", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T10:00:06.570400-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "entry_ask": 20.1, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 544.0, "option_spread_pct": 14.97, "option_volume": 31.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "matched_signals": 32, "recovery_stability_score": 0.698, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022104504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022104504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022104504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022104504)

</details>
