# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 13:40:05 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SHOP           95.24               42            0.54              0.59        154.08                69.26         0.608          pass              0.771             36.8                           0.288               -0.54              0.284                                 ok            True                  False
  AMGN          100.00               13            1.11              3.39        435.54                27.65         0.600          pass              0.528             16.0                           0.257                4.69              0.526                                 ok            True                  False
   MAR           96.67               30            0.58              1.44        353.25                33.75         0.555          pass              0.687             32.7                           0.431               -1.18             -0.057                                 ok            True                  False
  GILD          100.00               10            2.33              2.43        147.82                26.47         0.525          pass              0.470              6.0                           0.263                5.08              0.599                                 ok            True                  False
  VRTX           96.88               32            0.80              3.07        546.23                32.96         0.518          pass              0.756             52.4                           0.499                7.40              0.655                                 ok            True                  False
  INSM           73.33               15            2.42              2.06        120.51               110.68         0.783          pass              0.204             30.7                           0.340               -4.28             -0.593            downtrend_blocked_slope           False                  False
   STX           83.33               30            1.18              7.01        844.20                71.05         0.590          pass              0.440             52.8                           0.485              -14.00             -1.533            downtrend_blocked_slope           False                  False
   AEP           94.44               18            0.56              0.48        122.50                17.88         0.560          pass              0.545             16.9                           0.301               -2.85             -0.387 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               11            1.41              0.76         76.83                16.83         0.559          pass              0.488              8.4                           0.246               -3.92             -0.396            downtrend_blocked_slope           False                  False
  DRAM           78.12               32            1.79              0.71         56.52                68.22         0.546          pass              0.353             50.7                           0.482               -2.63             -0.297            downtrend_blocked_slope           False                  False
  CSCO           75.00               20            1.79              1.41        111.55                41.41         0.546          pass              0.151             10.1                           0.297               -1.38             -0.055                                 ok           False                  False
  REGN          100.00                6            1.96             11.11        802.95                24.94         0.543          pass              0.576             40.4                           0.373               -1.33             -0.047                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-28T12:00:05.127019-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:55:02.090702-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:50:05.095730-04:00 early_entry_1150 early_entry_shadow       {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "entry_ask": 19.8, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 11.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "matched_signals": 42, "recovery_stability_score": 0.663, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "trend_health_status": "ok"}, {"current_drop_pct": 0.54, "early_entry_score": 0.821, "early_reclaim_pct": 67.7, "matched_signals": 35, "recovery_stability_score": 0.659, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:45:05.139618-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                 {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "entry_ask": 19.6, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 10.75, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "matched_signals": 42, "recovery_stability_score": 0.749, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:40:03.918133-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.57, "early_entry_score": 0.816, "early_reclaim_pct": 66.2, "entry_ask": 27.7, "entry_bid": 25.4, "entry_mode": "early", "entry_option_price": 26.55, "hypothetical_budget": 26394.05, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 34.0, "option_spread_pct": 8.66, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.566, "shadow_only": true, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.512, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.816, "early_reclaim_pct": 66.2, "matched_signals": 35, "recovery_stability_score": 0.566, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.512, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:35:02.077001-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.55, "early_entry_score": 0.82, "early_reclaim_pct": 67.3, "entry_ask": 27.8, "entry_bid": 25.7, "entry_mode": "early", "entry_option_price": 26.75, "hypothetical_budget": 26394.05, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 34.0, "option_spread_pct": 7.85, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.514, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.82, "early_reclaim_pct": 67.3, "matched_signals": 35, "recovery_stability_score": 0.651, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:30:05.095211-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "VRTX261016C00540000", "current_drop_pct": 0.52, "early_entry_score": 0.826, "early_reclaim_pct": 69.2, "entry_ask": 26.9, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 25.55, "hypothetical_budget": 26394.05, "hypothetical_contracts": 10, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 34.0, "option_spread_pct": 10.57, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.515, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.826, "early_reclaim_pct": 69.2, "matched_signals": 35, "recovery_stability_score": 0.632, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.515, "trend_health_status": "ok"}, {"current_drop_pct": 0.96, "early_entry_score": 0.706, "early_reclaim_pct": 63.3, "matched_signals": 42, "recovery_stability_score": 0.66, "success_rate": 90.48, "ticker": "CDNS", "timing_score": 0.37, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:25:02.223727-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                   {"contract_symbol": "ZS261002C00187500", "current_drop_pct": 0.54, "early_entry_score": 0.897, "early_reclaim_pct": 82.2, "entry_ask": 15.85, "entry_bid": 13.5, "entry_mode": "early", "entry_option_price": 14.675, "hypothetical_budget": 26394.05, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 16.01, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.888, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.502, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.897, "early_reclaim_pct": 82.2, "matched_signals": 42, "recovery_stability_score": 0.888, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.502, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:20:02.016207-04:00 early_entry_1120 early_entry_shadow      {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.96, "early_entry_score": 0.844, "early_reclaim_pct": 68.3, "entry_ask": 18.4, "entry_bid": 17.45, "entry_mode": "early", "entry_option_price": 17.925, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 5.3, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.815, "shadow_only": true, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.844, "early_reclaim_pct": 68.3, "matched_signals": 39, "recovery_stability_score": 0.815, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.827, "early_reclaim_pct": 69.5, "matched_signals": 35, "recovery_stability_score": 0.552, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.516, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:15:03.127521-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.95, "early_entry_score": 0.845, "early_reclaim_pct": 68.7, "entry_ask": 18.3, "entry_bid": 17.45, "entry_mode": "early", "entry_option_price": 17.875, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 4.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.826, "shadow_only": true, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.845, "early_reclaim_pct": 68.7, "matched_signals": 39, "recovery_stability_score": 0.826, "success_rate": 94.87, "ticker": "ZS", "timing_score": 0.494, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828134005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828134005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828134005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828134005)

</details>
