# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 10:30:01 EDT`
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
  MSFT          100.00               10            1.89              7.05        529.93                21.62         0.526            pass              0.453              0.0                           0.150                0.05             -0.101                                 ok            True                  False
  TEAM          100.00               35            0.94              1.48        224.87                49.42         0.522            pass              0.750             43.7                           0.214                9.74              0.979                                 ok            True                  False
   MAR           84.21               19            0.97              2.75        402.82                19.25         0.513            pass              0.281             19.2                           0.310               10.80              1.156                                 ok            True                  False
  QCOM           93.94               33            0.69              0.85        177.59                39.95         0.510            pass              0.815             79.5                           0.665                0.41              0.052                                 ok            True                   True
  FAST           90.00               10            1.63              0.60         52.23                19.95         0.505            pass              0.451             44.5                           0.626                2.27              0.201                                 ok            True                  False
  SNPS           60.00                5            3.70             11.68        446.19                54.60         0.536            pass              0.054              0.0                           0.177              -12.71             -1.581 downtrend_blocked_slope_and_streak           False                  False
  DXCM           83.33                6            2.31              1.29         79.71                36.58         0.515            pass              0.179             12.7                           0.242               -7.11             -0.464 downtrend_blocked_slope_and_streak           False                  False
  MELI           73.68               19            1.94             25.13       1844.11                40.26         0.508            pass              0.134              7.7                           0.215               -2.03             -0.218                                 ok           False                  False
   CEG           66.67                6            4.65              8.82        266.96                61.93         0.492 below_threshold              0.049              0.0                           0.177               -9.45             -1.386 downtrend_blocked_slope_and_streak           False                  False
  NXPI           92.59               27            1.28              2.17        241.43                33.60         0.473 below_threshold              0.667             56.8                           0.514                3.54              0.599                                 ok           False                  False
  SHOP           77.78               18            2.09              2.56        173.19                40.35         0.465 below_threshold              0.183             27.9                           0.283                3.69              0.076                                 ok           False                  False
   APP           86.49               37            1.18              2.22        266.95                46.80         0.461 below_threshold              0.538             46.2                           0.325               -5.49             -0.371            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-22T10:30:01.703410-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                  {"contract_symbol": "QCOM261218C00180000", "current_drop_pct": 0.69, "early_entry_score": 0.815, "early_reclaim_pct": 79.5, "entry_ask": 13.6, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.125, "hypothetical_budget": 72415.9, "hypothetical_contracts": 55, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1533.0, "option_spread_pct": 7.24, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.665, "shadow_only": true, "success_rate": 93.94, "ticker": "QCOM", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.815, "early_reclaim_pct": 79.5, "matched_signals": 33, "recovery_stability_score": 0.665, "success_rate": 93.94, "ticker": "QCOM", "timing_score": 0.51, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:25:04.750468-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                  {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.82, "early_entry_score": 0.766, "early_reclaim_pct": 72.3, "entry_ask": 21.0, "entry_bid": 18.5, "entry_mode": "early", "entry_option_price": 19.75, "hypothetical_budget": 72415.9, "hypothetical_contracts": 36, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 12.66, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.626, "shadow_only": true, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.766, "early_reclaim_pct": 72.3, "matched_signals": 31, "recovery_stability_score": 0.626, "success_rate": 93.55, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:20:06.839812-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.67, "early_entry_score": 0.794, "early_reclaim_pct": 77.5, "entry_ask": 20.5, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 19.3, "hypothetical_budget": 72415.9, "hypothetical_contracts": 37, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 12.44, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.794, "early_reclaim_pct": 77.5, "matched_signals": 32, "recovery_stability_score": 0.673, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:15:05.850779-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 1.05, "early_entry_score": 0.729, "early_reclaim_pct": 64.4, "entry_ask": 19.8, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 18.95, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 8.97, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.729, "early_reclaim_pct": 64.4, "matched_signals": 30, "recovery_stability_score": 0.636, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:10:04.040588-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.98, "early_entry_score": 0.737, "early_reclaim_pct": 66.9, "entry_ask": 19.8, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 18.95, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 8.97, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.737, "early_reclaim_pct": 66.9, "matched_signals": 30, "recovery_stability_score": 0.722, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:05:04.719649-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "PCAR261218C00110000", "current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "entry_ask": 6.3, "entry_bid": 4.1, "entry_mode": "early", "entry_option_price": 5.2, "hypothetical_budget": 72415.9, "hypothetical_contracts": 139, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 42.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "matched_signals": 43, "recovery_stability_score": 0.768, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.7, "early_reclaim_pct": 81.3, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 88.89, "ticker": "NXPI", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T10:00:06.570400-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "entry_ask": 20.1, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 544.0, "option_spread_pct": 14.97, "option_volume": 31.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "matched_signals": 32, "recovery_stability_score": 0.698, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T09:20:05.053527-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-10-21T15:10:06.687584-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T15:05:05.870739-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022103001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022103001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022103001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022103001)

</details>
