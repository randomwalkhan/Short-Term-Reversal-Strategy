# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 10:35:03 EDT`
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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ALNY           88.00               25            1.51              2.63        247.55                49.38         0.500 below_threshold              0.543             60.0                           0.299                3.30              0.202                                 ok            True                  False
   KHC           92.31               13            0.59              0.10         24.56                26.10         0.581            pass              0.477             23.7                           0.133               -3.32             -0.462            downtrend_blocked_slope           False                  False
  SNPS           72.22               18            2.21              6.15        394.74                60.55         0.576            pass              0.119              2.7                           0.111              -12.20             -1.234            downtrend_blocked_slope           False                  False
  CHTR           90.48               42            0.08              0.08        145.73                68.13         0.563            pass              0.827             97.2                           0.820               -5.19             -0.859            downtrend_blocked_slope           False                  False
   EXC          100.00               10            0.78              0.23         43.06                14.68         0.552            pass              0.524             23.0                           0.232               -1.59             -0.084           downtrend_blocked_streak           False                  False
 CMCSA           96.67               30            0.46              0.08         25.17                34.99         0.531            pass              0.714             42.5                           0.304               -7.30             -0.832 downtrend_blocked_slope_and_streak           False                  False
   AEP           77.78                9            1.08              0.93        122.93                16.49         0.528            pass              0.086             11.0                           0.257               -0.25              0.048                                 ok           False                  False
  NVDA           80.00                5            3.50              5.35        216.00                43.68         0.519            pass              0.107             18.4                           0.414               -3.06             -0.181           downtrend_blocked_streak           False                  False
  UPRO           92.86               14            2.23              2.31        147.03                26.03         0.501            pass              0.452             10.9                           0.177               -4.65             -0.371 downtrend_blocked_slope_and_streak           False                  False
   CSX           80.00               20            0.65              0.22         48.85                18.07         0.494 below_threshold              0.277             53.6                           0.314               -4.91             -0.334            downtrend_blocked_slope           False                  False
  MELI           97.22               36            0.57              7.56       1894.13                37.25         0.490 below_threshold              0.771             49.5                           0.413               -4.05             -0.495 downtrend_blocked_slope_and_streak           False                  False
  CDNS           71.43               21            1.95              3.95        287.68                43.36         0.488 below_threshold              0.208             28.6                           0.417              -16.65             -1.857 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-14T10:35:03.129508-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.56, "early_entry_score": 0.845, "early_reclaim_pct": 76.9, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.845, "early_reclaim_pct": 76.9, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:30:01.152638-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.68, "early_entry_score": 0.818, "early_reclaim_pct": 72.0, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.771, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.818, "early_reclaim_pct": 72.0, "matched_signals": 34, "recovery_stability_score": 0.771, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:25:02.232009-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "matched_signals": 35, "recovery_stability_score": 0.789, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:20:02.245642-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.54, "early_entry_score": 0.848, "early_reclaim_pct": 77.7, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.792, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.848, "early_reclaim_pct": 77.7, "matched_signals": 36, "recovery_stability_score": 0.792, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:15:01.117814-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.67, "early_entry_score": 0.825, "early_reclaim_pct": 72.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.825, "early_reclaim_pct": 72.3, "matched_signals": 35, "recovery_stability_score": 0.743, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:10:06.027535-04:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.87, "early_entry_score": 0.774, "early_reclaim_pct": 64.0, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.774, "early_reclaim_pct": 64.0, "matched_signals": 31, "recovery_stability_score": 0.68, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:05:06.288532-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T10:00:06.059973-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T09:20:04.227328-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-09-11T15:10:01.826868-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914103503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914103503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914103503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914103503)

</details>
