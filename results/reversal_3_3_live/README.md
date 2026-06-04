# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-04 14:20:05 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$34,571.75`
- Equity: `$34,571.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  QCOM           91.67               12            2.89              5.06        247.84                96.24         0.650          pass              0.543             51.1                           0.651               19.89              1.346                                 ok            True                  False
  MELI           94.59               37            0.65              7.43       1635.35                61.24         0.593          pass              0.683             18.1                           0.170               -1.41             -0.048                                 ok            True                  False
  SOXL           90.00               20            3.18              6.25        277.86               141.59         0.584          pass              0.640             82.8                           0.878               56.82              4.640                                 ok            True                  False
  CTSH           93.55               31            0.67              0.25         53.40                51.56         0.546          pass              0.578              7.3                           0.201                3.61              0.586                                 ok            True                  False
  PANW           87.50               24            1.69              3.32        279.01                59.60         0.533          pass              0.546             66.3                           0.752               11.77              1.640                                 ok            True                  False
   WDC           96.88               32            1.04              4.33        592.26                59.52         0.529          pass              0.837             79.0                           0.596               27.92              2.332                                 ok            True                   True
   ADI           95.45               22            1.41              4.32        435.82                44.48         0.525          pass              0.724             63.9                           0.756                8.70              0.961                                 ok            True                  False
  LRCX           88.46               26            1.10              2.64        342.58                54.10         0.512          pass              0.624             80.1                           0.785               16.38              1.371                                 ok            True                  False
  SNPS           93.10               29            1.09              3.80        496.39                43.50         0.506          pass              0.702             58.3                           0.611               -1.27             -0.429                                 ok            True                  False
  INTU           70.59               17            3.26              7.12        308.39               102.00         0.647          pass              0.112              0.0                           0.123              -21.53             -0.691            downtrend_blocked_slope           False                  False
  DRAM          100.00                8            4.13              2.02         68.85                86.94         0.594          pass              0.627             55.9                           0.689               29.74              3.089                                 ok           False                  False
  INTC           97.30               37            0.32              0.25        112.60                77.78         0.580          pass              0.921             94.2                           0.861               -5.56             -1.004 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-04T11:33:58.038645-04:00 early_entry_1130 early_entry_shadow  {"contract_symbol": "SNPS260717C00510000", "current_drop_pct": 0.55, "early_entry_score": 0.825, "early_reclaim_pct": 79.1, "entry_ask": 29.4, "entry_bid": 27.7, "entry_mode": "early", "entry_option_price": 28.55, "hypothetical_budget": 17285.88, "hypothetical_contracts": 6, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 124.0, "option_spread_pct": 5.95, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.81, "shadow_only": true, "success_rate": 94.12, "ticker": "SNPS", "timing_score": 0.51, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.825, "early_reclaim_pct": 79.1, "matched_signals": 34, "recovery_stability_score": 0.81, "success_rate": 94.12, "ticker": "SNPS", "timing_score": 0.51, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-04T10:52:01.009972-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "ASML260717C01640000", "current_drop_pct": 0.96, "early_entry_score": 0.753, "early_reclaim_pct": 69.9, "entry_ask": 176.5, "entry_bid": 162.4, "entry_mode": "early", "entry_option_price": 169.45, "hypothetical_budget": 17285.88, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 116.0, "option_spread_pct": 8.32, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 93.33, "ticker": "ASML", "timing_score": 0.54, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.753, "early_reclaim_pct": 69.9, "matched_signals": 30, "recovery_stability_score": 0.7, "success_rate": 93.33, "ticker": "ASML", "timing_score": 0.54, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-04T10:07:26.962733-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 1.2, "early_entry_score": 0.681, "early_reclaim_pct": 76.1, "entry_ask": 19.1, "entry_bid": 17.1, "entry_mode": "early", "entry_option_price": 18.1, "hypothetical_budget": 17285.88, "hypothetical_contracts": 9, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 1675.0, "option_spread_pct": 11.05, "option_volume": 84.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.831, "shadow_only": true, "success_rate": 90.0, "ticker": "PANW", "timing_score": 0.527, "top_candidates": [{"current_drop_pct": 1.2, "early_entry_score": 0.681, "early_reclaim_pct": 76.1, "matched_signals": 30, "recovery_stability_score": 0.831, "success_rate": 90.0, "ticker": "PANW", "timing_score": 0.527, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-04T09:22:28.092024-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-03T15:10:03.976623-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-03T15:05:05.758809-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-03T15:00:06.248089-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-03T14:55:06.012322-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-03T14:50:06.341439-04:00       entry_1500      entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-06-03T14:50:06.341439-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-03", "training_samples": 5182, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260604142005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260604142005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260604142005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260604142005)

</details>
