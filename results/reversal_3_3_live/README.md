# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 12:50:06 EDT`
Last processed slot: `manage_1300`

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
  AMGN          100.00               13            1.11              3.39        435.54                27.65         0.600          pass              0.529             16.2                           0.264                4.69              0.526                                 ok            True                  False
   MAR           96.30               27            0.61              1.52        353.22                33.75         0.575          pass              0.582              3.8                           0.213               -1.21             -0.058                                 ok            True                  False
  GILD          100.00               10            2.22              2.31        147.87                26.47         0.533          pass              0.465              3.8                           0.179                5.20              0.604                                 ok            True                  False
  FAST          100.00               10            1.96              0.70         50.83                21.07         0.517          pass              0.514             20.6                           0.376               -1.73             -0.122                                 ok            True                  False
  VRTX           96.67               30            1.11              4.24        545.73                32.96         0.512          pass              0.687             34.3                           0.207                7.07              0.641                                 ok            True                  False
  MNST           91.89               37            0.19              0.06         46.67               551.83         1.000          pass              0.814             72.3                           0.523               -0.45              0.173                                 ok           False                  False
  INSM           73.33               15            2.39              2.03        120.52               110.68         0.784          pass              0.207             31.6                           0.282               -4.24             -0.592            downtrend_blocked_slope           False                  False
  SHOP           95.45               44            0.06              0.07        154.30                69.26         0.624          pass              0.940             92.5                           0.511               -0.06              0.306                                 ok           False                  False
   STX           83.33               30            1.23              7.29        844.08                71.05         0.588          pass              0.434             50.9                           0.432              -14.04             -1.536            downtrend_blocked_slope           False                  False
  CSCO           76.19               21            1.57              1.23        111.62                41.41         0.558          pass              0.141              3.8                           0.130               -1.16             -0.044                                 ok           False                  False
  DRAM           78.12               32            1.72              0.68         56.54                68.22         0.551          pass              0.360             52.9                           0.425               -2.56             -0.293            downtrend_blocked_slope           False                  False
   AEP           95.45               22            0.44              0.38        122.55                17.88         0.546          pass              0.535              0.0                           0.249               -2.73             -0.381 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828125006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828125006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828125006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828125006)

</details>
