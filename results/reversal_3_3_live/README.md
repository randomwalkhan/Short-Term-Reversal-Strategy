# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 10:00:06 EDT`
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
  MSFT          100.00               15            1.35              5.03        530.80                21.62         0.531            pass              0.511              8.1                           0.091                0.60             -0.076                                 ok            True                  False
  MELI           82.76               29            1.32             17.09       1847.56                40.26         0.504            pass              0.251              0.0                           0.237               -1.41             -0.189                                 ok            True                  False
   CEG           80.00               10            2.79              5.28        268.48                61.93         0.601            pass              0.141             26.9                           0.262               -7.68             -1.298 downtrend_blocked_slope_and_streak           False                  False
  SNPS           57.14                7            2.73              8.62        447.49                54.60         0.580            pass              0.114             18.7                           0.264              -11.83             -1.535 downtrend_blocked_slope_and_streak           False                  False
  CSCO           76.47               17            1.36              1.02        106.82                31.32         0.537            pass              0.156             18.7                           0.319               -7.91             -1.138 downtrend_blocked_slope_and_streak           False                  False
  UPRO           88.89                9            2.31              2.46        150.96                26.42         0.498 below_threshold              0.381             31.4                           0.535               -3.02             -0.442            downtrend_blocked_slope           False                  False
  AVGO           66.67               12            2.28              5.40        335.49                36.08         0.498 below_threshold              0.181             39.3                           0.660               -8.35             -0.971            downtrend_blocked_slope           False                  False
  QCOM           95.12               41            0.28              0.35        177.81                39.95         0.493 below_threshold              0.924             91.6                           0.961                0.82              0.071                                 ok           False                  False
  FAST           80.00                5            2.23              0.82         52.14                19.95         0.489 below_threshold              0.121             24.0                           0.239                1.64              0.173                                 ok           False                  False
  NXPI           93.75               32            0.73              1.24        241.83                33.60         0.478 below_threshold              0.787             75.4                           0.698                4.12              0.625                                 ok           False                   True
  MCHP           90.48               21            2.13              1.15         76.66                39.64         0.476 below_threshold              0.524             41.2                           0.573               -0.02              0.188                                 ok           False                  False
  MSTR           86.67               15            3.47              3.72        151.88                66.76         0.471 below_threshold              0.403             48.4                           0.734               -2.19             -0.550                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-22T10:00:06.570400-04:00 early_entry_1000      early_entry_shadow {"contract_symbol": "NXPI261218C00240000", "current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "entry_ask": 20.1, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 38, "matched_signals": 32, "option_liquidity_status": "wide_spread", "option_open_interest": 544.0, "option_spread_pct": 14.97, "option_volume": 31.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.787, "early_reclaim_pct": 75.4, "matched_signals": 32, "recovery_stability_score": 0.698, "success_rate": 93.75, "ticker": "NXPI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-22T09:20:05.053527-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 91, 'empty': 2}
2026-10-21T15:10:06.687584-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-21T15:05:05.870739-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-21T15:00:05.576532-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-21T14:55:05.525520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-21T14:50:04.709155-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_trade_after_option_and_timing_filters"}
2026-10-21T14:50:04.709155-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"early_entry_score": 0.216, "option_liquidity_status": "no_two_sided_quote,wide_spread", "option_open_interest": 112.0, "option_spread_pct": null, "option_volume": 63.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.504}
2026-10-21T14:50:04.709155-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"early_entry_score": 0.255, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 40.0, "option_spread_pct": 10.41, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.508}
2026-10-21T14:50:04.709155-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-21", "training_samples": 6158, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022100006)

</details>
