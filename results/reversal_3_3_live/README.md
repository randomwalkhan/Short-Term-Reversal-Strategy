# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 10:15:05 EDT`
Last processed slot: `early_entry_1015`

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
  MSFT          100.00               11            1.70              6.36        530.23                21.62         0.532            pass              0.460              0.0                           0.176                0.24             -0.092                                 ok            True                  False
   CEG           71.43                7            3.59              6.81        267.82                61.93         0.562            pass              0.074              5.8                           0.195               -8.44             -1.336 downtrend_blocked_slope_and_streak           False                  False
  SNPS           57.14                7            3.06              9.67        447.05                54.60         0.561            pass              0.083              8.8                           0.211              -12.13             -1.551 downtrend_blocked_slope_and_streak           False                  False
  CSCO           50.00                6            2.36              1.77        106.50                31.32         0.508            pass              0.051              0.0                           0.177               -8.84             -1.184 downtrend_blocked_slope_and_streak           False                  False
  MELI           80.00               30            1.23             16.01       1848.02                40.26         0.498 below_threshold              0.239             18.7                           0.179               -1.33             -0.185                                 ok           False                  False
  QCOM           95.12               41            0.20              0.25        177.85                39.95         0.495 below_threshold              0.932             94.0                           0.938                0.91              0.074                                 ok           False                  False
  FAST           87.50                8            2.04              0.75         52.17                19.95         0.490 below_threshold              0.341             30.5                           0.393                1.84              0.182                                 ok           False                  False
  AVGO           60.00               10            2.73              6.45        335.04                36.08         0.476 below_threshold              0.130             27.4                           0.494               -8.76             -0.992            downtrend_blocked_slope           False                  False
  DXCM           90.48               21            1.61              0.90         79.87                36.58         0.475 below_threshold              0.510             36.5                           0.336               -6.44             -0.432 downtrend_blocked_slope_and_streak           False                  False
  NXPI           93.33               30            1.05              1.79        241.59                33.60         0.469 below_threshold              0.729             64.4                           0.636                3.78              0.610                                 ok           False                   True
  CRWD           86.67               45            0.14              0.23        239.24                50.83         0.466 below_threshold              0.706             93.9                           0.397               -9.13             -1.668 downtrend_blocked_slope_and_streak           False                  False
  MCHP           88.89               18            2.68              1.45         76.53                39.64         0.460 below_threshold              0.415             26.1                           0.334               -0.58              0.162                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-22T10:15:05.850779-04:00 early_entry_1015      early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 1.05, "early_entry_score": 0.729, "early_reclaim_pct": 64.4, "entry_ask": 19.8, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 18.95, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 8.97, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.636, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.729, "early_reclaim_pct": 64.4, "matched_signals": 30, "recovery_stability_score": 0.636, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:10:04.040588-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.98, "early_entry_score": 0.737, "early_reclaim_pct": 66.9, "entry_ask": 19.8, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 18.95, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 544.0, "option_spread_pct": 8.97, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.737, "early_reclaim_pct": 66.9, "matched_signals": 30, "recovery_stability_score": 0.722, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T10:05:04.719649-04:00 early_entry_1005      early_entry_shadow {"contract_symbol": "PCAR261218C00110000", "current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "entry_ask": 6.3, "entry_bid": 4.1, "entry_mode": "early", "entry_option_price": 5.2, "hypothetical_budget": 72415.9, "hypothetical_contracts": 139, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 42.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "matched_signals": 43, "recovery_stability_score": 0.768, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.7, "early_reclaim_pct": 81.3, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 88.89, "ticker": "NXPI", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T10:00:06.570400-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "entry_ask": 20.1, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 544.0, "option_spread_pct": 14.97, "option_volume": 31.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "matched_signals": 32, "recovery_stability_score": 0.698, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T09:20:05.053527-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-10-21T15:10:06.687584-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T15:05:05.870739-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T15:00:05.576532-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T14:55:05.525520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T14:50:04.709155-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"early_entry_score": 0.216, "option_liquidity_status": "no_two_sided_quote,wide_spread", "option_open_interest": 112.0, "option_spread_pct": null, "option_volume": 63.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.504}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022101505)

</details>
