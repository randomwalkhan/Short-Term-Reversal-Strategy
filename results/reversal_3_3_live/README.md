# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 10:25:04 EDT`
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
  MSFT          100.00               11            1.69              6.31        530.25                21.62         0.532            pass              0.476              5.5                           0.170                0.25             -0.092                                 ok            True                  False
  TEAM          100.00               39            0.58              0.92        225.11                49.42         0.519            pass              0.841             65.1                           0.307               10.13              0.995                                 ok            True                  False
   CEG           75.00                8            3.52              6.66        267.88                61.93         0.564            pass              0.083              8.8                           0.241               -8.37             -1.332 downtrend_blocked_slope_and_streak           False                  False
  SNPS           57.14                7            3.25             10.27        446.79                54.60         0.549            pass              0.074              6.4                           0.219              -12.30             -1.560 downtrend_blocked_slope_and_streak           False                  False
  DXCM           75.00                8            2.12              1.19         79.75                36.58         0.506            pass              0.099             16.3                           0.200               -6.93             -0.455 downtrend_blocked_slope_and_streak           False                  False
  QCOM           95.12               41            0.19              0.23        177.86                39.95         0.496 below_threshold              0.933             94.5                           0.814                0.92              0.075                                 ok           False                  False
  MELI           80.00               25            1.72             22.37       1845.29                40.26         0.495 below_threshold              0.167              6.0                           0.220               -1.82             -0.208                                 ok           False                  False
  FAST           80.00                5            2.13              0.78         52.15                19.95         0.494 below_threshold              0.131             27.3                           0.389                1.74              0.178                                 ok           False                  False
  NXPI           93.55               31            0.82              1.39        241.76                33.60         0.478 below_threshold              0.766             72.3                           0.626                4.02              0.620                                 ok           False                   True
  MSTR           82.35               17            3.10              3.33        152.05                66.76         0.476 below_threshold              0.318             53.8                           0.660               -1.82             -0.533                                 ok           False                  False
   MAR           86.21               29            0.74              2.09        403.10                19.25         0.471 below_threshold              0.415             25.3                           0.331               11.06              1.167                                 ok           False                  False
  AVGO           55.56                9            2.84              6.71        334.92                36.08         0.470 below_threshold              0.120             24.5                           0.280               -8.87             -0.997            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-22T10:25:04.750468-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                  {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.82, "early_entry_score": 0.766, "early_reclaim_pct": 72.3, "entry_ask": 21.0, "entry_bid": 18.5, "entry_mode": "early", "entry_option_price": 19.75, "hypothetical_budget": 72415.9, "hypothetical_contracts": 36, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 12.66, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.766, "early_reclaim_pct": 72.3, "matched_signals": 31, "recovery_stability_score": 0.626, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:20:06.839812-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.67, "early_entry_score": 0.794, "early_reclaim_pct": 77.5, "entry_ask": 20.5, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 19.3, "hypothetical_budget": 72415.9, "hypothetical_contracts": 37, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 12.44, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.794, "early_reclaim_pct": 77.5, "matched_signals": 32, "recovery_stability_score": 0.673, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:15:05.850779-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 1.05, "early_entry_score": 0.729, "early_reclaim_pct": 64.4, "entry_ask": 19.8, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 18.95, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 8.97, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.729, "early_reclaim_pct": 64.4, "matched_signals": 30, "recovery_stability_score": 0.636, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:10:04.040588-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.98, "early_entry_score": 0.737, "early_reclaim_pct": 66.9, "entry_ask": 19.8, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 18.95, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 8.97, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.737, "early_reclaim_pct": 66.9, "matched_signals": 30, "recovery_stability_score": 0.722, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:05:04.719649-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "PCAR261218C00110000", "current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "entry_ask": 6.3, "entry_bid": 4.1, "entry_mode": "early", "entry_option_price": 5.2, "hypothetical_budget": 72415.9, "hypothetical_contracts": 139, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 42.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "matched_signals": 43, "recovery_stability_score": 0.768, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.7, "early_reclaim_pct": 81.3, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 88.89, "ticker": "NXPI", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T10:00:06.570400-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "entry_ask": 20.1, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 544.0, "option_spread_pct": 14.97, "option_volume": 31.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "matched_signals": 32, "recovery_stability_score": 0.698, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T09:20:05.053527-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-10-21T15:10:06.687584-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T15:05:05.870739-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T15:00:05.576532-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022102504)

</details>
