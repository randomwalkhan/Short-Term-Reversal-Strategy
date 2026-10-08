# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 12:55:06 EDT`
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

- Cash: `$108,579.30`
- Equity: `$108,579.30`
- Realized PnL: `$98,579.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0  -10.000000        stop_loss_hit_at_scan
  ABNB     option         option ABNB261120C00160000     55          2026-10-06         2026-10-08        9.475     11.0500  8662.5   16.622691 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           84.21               19            2.73             27.21       1414.32                55.22         0.540            pass              0.269             14.4                           0.194                4.01              0.799                                 ok            True                  False
  UPRO           88.89               18            1.51              1.64        154.46                30.53         0.532            pass              0.396             17.6                           0.273                1.89              0.387                                 ok            True                  False
   ADI           85.71               21            1.37              3.94        408.39                34.70         0.528            pass              0.377             33.0                           0.257                5.71              0.708                                 ok            True                  False
  MELI           81.25               32            1.20             15.77       1866.02                42.10         0.506            pass              0.323             30.9                           0.299                5.48              0.827                                 ok            True                  False
  CRWD           88.64               44            0.66              1.22        264.92                59.00         0.503            pass              0.619             46.3                           0.305                1.55              0.541                                 ok            True                  False
  MSTR           85.71               21            3.04              3.26        151.97                80.80         0.590            pass              0.335             16.6                           0.217               -7.98             -0.223           downtrend_blocked_streak           False                  False
  META           80.65               31            0.66              3.35        719.88                52.76         0.573            pass              0.387             57.4                           0.287               -7.85             -0.423            downtrend_blocked_slope           False                  False
  QCOM           85.71               21            2.43              3.01        175.83                56.66         0.558            pass              0.311              9.9                           0.248              -11.04             -1.133 downtrend_blocked_slope_and_streak           False                  False
  CSCO           72.73               11            1.86              1.53        116.74                34.80         0.558            pass              0.089              8.8                           0.188                8.12              1.145                                 ok           False                  False
   TRI           90.48               42            0.01              0.00         99.28                44.07         0.506            pass              0.829             99.8                           0.919               -1.04              0.003                                 ok           False                  False
  AVGO           83.33               12            2.75              7.25        373.40                34.55         0.497 below_threshold              0.171              6.4                           0.238                4.51              0.682                                 ok           False                  False
  ASML           80.00               30            0.87             11.00       1800.25                39.58         0.496 below_threshold              0.384             67.0                           0.335                3.88              0.445                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-08T12:00:05.051219-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.63, "early_entry_score": 0.858, "early_reclaim_pct": 84.8, "entry_ask": 3.7, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.55, "hypothetical_budget": 54289.65, "hypothetical_contracts": 152, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 8.45, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.858, "early_reclaim_pct": 84.8, "matched_signals": 36, "recovery_stability_score": 0.751, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:55:05.190220-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:50:07.100494-04:00 early_entry_1150 early_entry_shadow  {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.51, "early_entry_score": 0.897, "early_reclaim_pct": 87.8, "entry_ask": 3.5, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 3.4, "hypothetical_budget": 54289.65, "hypothetical_contracts": 159, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 5.88, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.727, "shadow_only": true, "success_rate": 94.87, "ticker": "CTSH", "timing_score": 0.438, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.897, "early_reclaim_pct": 87.8, "matched_signals": 39, "recovery_stability_score": 0.727, "success_rate": 94.87, "ticker": "CTSH", "timing_score": 0.438, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:45:05.150899-04:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.85, "early_entry_score": 0.82, "early_reclaim_pct": 79.5, "entry_ask": 3.5, "entry_bid": 3.2, "entry_mode": "early", "entry_option_price": 3.35, "hypothetical_budget": 54289.65, "hypothetical_contracts": 162, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 8.96, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.608, "shadow_only": true, "success_rate": 94.12, "ticker": "CTSH", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.82, "early_reclaim_pct": 79.5, "matched_signals": 34, "recovery_stability_score": 0.608, "success_rate": 94.12, "ticker": "CTSH", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:40:06.664778-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:35:04.845679-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:30:01.685924-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:25:05.197379-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:20:05.981785-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:15:06.509064-04:00 early_entry_1115 early_entry_shadow                 {"contract_symbol": "ISRG261120C00410000", "current_drop_pct": 0.51, "early_entry_score": 0.75, "early_reclaim_pct": 69.2, "entry_ask": 27.4, "entry_bid": 24.5, "entry_mode": "early", "entry_option_price": 25.95, "hypothetical_budget": 54289.65, "hypothetical_contracts": 20, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 121.0, "option_spread_pct": 11.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.75, "early_reclaim_pct": 69.2, "matched_signals": 37, "recovery_stability_score": 0.721, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008125506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008125506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008125506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008125506)

</details>
