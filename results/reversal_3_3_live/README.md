# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 10:05:04 EDT`
Last processed slot: `manage_1000`

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
  MSFT          100.00               17            1.32              4.94        530.83                21.62         0.520            pass              0.527              9.6                           0.113                0.63             -0.075                                 ok            True                  False
  MELI           82.76               29            1.33             17.27       1847.48                40.26         0.501            pass              0.287             12.3                           0.150               -1.42             -0.190                                 ok            True                  False
   CEG           72.73               11            2.72              5.16        268.53                61.93         0.591            pass              0.152             28.6                           0.305               -7.61             -1.295 downtrend_blocked_slope_and_streak           False                  False
  SNPS           57.14                7            2.85              9.01        447.33                54.60         0.573            pass              0.102             15.0                           0.281              -11.94             -1.541 downtrend_blocked_slope_and_streak           False                  False
  CSCO           76.47               17            1.47              1.11        106.79                31.32         0.529            pass              0.135             11.7                           0.226               -8.02             -1.143 downtrend_blocked_slope_and_streak           False                  False
  AVGO           66.67               12            2.31              5.45        335.46                36.08         0.497 below_threshold              0.179             38.7                           0.662               -8.37             -0.972            downtrend_blocked_slope           False                  False
  FAST           83.33                6            2.07              0.76         52.16                19.95         0.496 below_threshold              0.227             29.5                           0.271                1.81              0.181                                 ok           False                  False
  UPRO           87.50                8            2.44              2.59        150.90                26.42         0.495 below_threshold              0.332             27.6                           0.530               -3.15             -0.448            downtrend_blocked_slope           False                  False
  MCHP           90.48               21            2.13              1.15         76.66                39.64         0.477 below_threshold              0.525             41.4                           0.614               -0.01              0.188                                 ok           False                  False
 GOOGL           71.43                7            2.04              4.78        332.71                18.62         0.469 below_threshold              0.136             29.8                           0.242               -5.85             -0.620            downtrend_blocked_slope           False                  False
  NVDA           70.00               10            2.43              3.77        220.35                25.09         0.469 below_threshold              0.090             14.3                           0.257               -6.03             -0.645            downtrend_blocked_slope           False                  False
  DXCM           91.67               24            1.47              0.83         79.91                36.58         0.467 below_threshold              0.577             41.9                           0.436               -6.31             -0.425 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-22T10:05:04.719649-04:00 early_entry_1005      early_entry_shadow {"contract_symbol": "PCAR261218C00110000", "current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "entry_ask": 6.3, "entry_bid": 4.1, "entry_mode": "early", "entry_option_price": 5.2, "hypothetical_budget": 72415.9, "hypothetical_contracts": 139, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 42.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.768, "shadow_only": true, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.731, "early_reclaim_pct": 69.0, "matched_signals": 43, "recovery_stability_score": 0.768, "success_rate": 90.7, "ticker": "PCAR", "timing_score": 0.388, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.7, "early_reclaim_pct": 81.3, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 88.89, "ticker": "NXPI", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T10:00:06.570400-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "entry_ask": 20.1, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 544.0, "option_spread_pct": 14.97, "option_volume": 31.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "matched_signals": 32, "recovery_stability_score": 0.698, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T09:20:05.053527-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-10-21T15:10:06.687584-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T15:05:05.870739-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T15:00:05.576532-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T14:55:05.525520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-21T14:50:04.709155-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-21", "training_samples": 6158, "window": 5}
2026-10-21T14:50:04.709155-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_trade_after_option_and_timing_filters"}
2026-10-21T14:50:04.709155-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"early_entry_score": 0.216, "option_liquidity_status": "no_two_sided_quote,wide_spread", "option_open_interest": 112.0, "option_spread_pct": null, "option_volume": 63.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.504}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022100504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022100504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022100504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022100504)

</details>
