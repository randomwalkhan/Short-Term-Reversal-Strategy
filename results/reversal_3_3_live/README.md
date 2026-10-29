# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-29 10:40:05 EDT`
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

- Cash: `$64,409.30`
- Equity: `$127,184.30`
- Realized PnL: `$119,884.30`
- Unrealized PnL: `$-2,700.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261218C00110000       2026-10-28                   1     90     65475.0                 62775.0         7.28           6.98      110.47         109.3          bid_ask_mid                       6.98                bid_ask_mid                    True         -2700.0                  -4.12         80.77               26              0.82         42.92           45.58                  35.12                4095.0         1198.0               0.02                      ok
```

## Today's Closed Trades (2026-10-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           89.29               28            1.97              2.00        144.30                71.12         0.574          pass              0.588             54.5                           0.677               -5.94             -0.040                                 ok            True                  False
  CSCO           82.14               28            0.74              0.57        110.04                35.33         0.531          pass              0.331             33.6                           0.231               -0.35              0.256                                 ok            True                  False
  UPRO           83.33               24            1.09              1.15        150.65                30.20         0.520          pass              0.371             45.8                           0.658               -1.33             -0.002                                 ok            True                  False
  ADBE           85.71               28            1.51              2.63        248.63                41.65         0.502          pass              0.493             57.0                           0.360               -2.25              0.021                                 ok            True                  False
  SOXL           68.18               22            5.04              3.79        105.73               137.18         0.614          pass              0.281             46.7                           0.706               -5.04             -0.002                                 ok           False                  False
  MPWR           65.22               23            1.57             13.27       1205.53                59.53         0.575          pass              0.324             60.0                           0.785               -4.56             -0.534            downtrend_blocked_slope           False                  False
  NVDA           76.92               26            0.62              0.93        214.98                30.56         0.535          pass              0.339             59.7                           0.709               -1.46             -0.085                                 ok           False                  False
  AVGO           54.55               11            2.43              6.00        349.24                43.15         0.532          pass              0.162             34.2                           0.620               -0.32              0.222                                 ok           False                  False
   ROP           88.89               36            0.50              1.54        440.00                39.09         0.519          pass              0.610             49.2                           0.322               14.65              1.751                                 ok           False                  False
  DRAM           66.67               18            3.33              1.26         53.58                63.50         0.512          pass              0.201             32.1                           0.601                6.06              0.927                                 ok           False                  False
  MELI           72.22               36            1.05             12.29       1667.82                48.85         0.505          pass              0.410             61.9                           0.664              -10.85             -1.341 downtrend_blocked_slope_and_streak           False                  False
    MU           72.22               18            3.17             21.84        973.87                57.32         0.503          pass              0.181             25.9                           0.431                2.23              0.558                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-29T10:40:05.590194-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "QCOM261218C00190000", "current_drop_pct": 0.9, "early_entry_score": 0.744, "early_reclaim_pct": 60.9, "entry_ask": 10.15, "entry_bid": 9.6, "entry_mode": "early", "entry_option_price": 9.875, "hypothetical_budget": 32204.65, "hypothetical_contracts": 32, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 1786.0, "option_spread_pct": 5.57, "option_volume": 811.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.744, "early_reclaim_pct": 60.9, "matched_signals": 32, "recovery_stability_score": 0.662, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:35:05.458266-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:30:06.113309-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:25:05.571151-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:20:06.041880-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "QCOM261218C00190000", "current_drop_pct": 0.87, "early_entry_score": 0.747, "early_reclaim_pct": 61.8, "entry_ask": 10.2, "entry_bid": 9.95, "entry_mode": "early", "entry_option_price": 10.075, "hypothetical_budget": 32204.65, "hypothetical_contracts": 31, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 1786.0, "option_spread_pct": 2.48, "option_volume": 811.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.747, "early_reclaim_pct": 61.8, "matched_signals": 32, "recovery_stability_score": 0.651, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:15:06.489089-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                    {"contract_symbol": "ADBE261218C00250000", "current_drop_pct": 0.9, "early_entry_score": 0.697, "early_reclaim_pct": 74.4, "entry_ask": 18.1, "entry_bid": 15.55, "entry_mode": "early", "entry_option_price": 16.825, "hypothetical_budget": 32204.65, "hypothetical_contracts": 19, "matched_signals": 37, "option_liquidity_status": "wide_spread", "option_open_interest": 5906.0, "option_spread_pct": 15.16, "option_volume": 156.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.697, "early_reclaim_pct": 74.4, "matched_signals": 37, "recovery_stability_score": 0.759, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.484, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-29T10:10:04.545250-04:00 early_entry_1010 early_entry_shadow       {"contract_symbol": "MCHP261218C00077500", "current_drop_pct": 0.6, "early_entry_score": 0.757, "early_reclaim_pct": 85.7, "entry_ask": 7.9, "entry_bid": 6.9, "entry_mode": "early", "entry_option_price": 7.4, "hypothetical_budget": 32204.65, "hypothetical_contracts": 43, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 827.0, "option_spread_pct": 13.51, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.788, "shadow_only": true, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.757, "early_reclaim_pct": 85.7, "matched_signals": 39, "recovery_stability_score": 0.788, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.9, "early_entry_score": 0.696, "early_reclaim_pct": 74.1, "matched_signals": 37, "recovery_stability_score": 0.812, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.484, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:05:06.192375-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ADBE261218C00250000", "current_drop_pct": 0.64, "early_entry_score": 0.777, "early_reclaim_pct": 81.8, "entry_ask": 17.25, "entry_bid": 15.55, "entry_mode": "early", "entry_option_price": 16.4, "hypothetical_budget": 32204.65, "hypothetical_contracts": 19, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 5906.0, "option_spread_pct": 10.37, "option_volume": 156.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.915, "shadow_only": true, "success_rate": 90.7, "ticker": "ADBE", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.777, "early_reclaim_pct": 81.8, "matched_signals": 43, "recovery_stability_score": 0.915, "success_rate": 90.7, "ticker": "ADBE", "timing_score": 0.464, "trend_health_status": "ok"}, {"current_drop_pct": 1.41, "early_entry_score": 0.758, "early_reclaim_pct": 84.8, "matched_signals": 34, "recovery_stability_score": 0.949, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:00:05.728324-04:00 early_entry_1000 early_entry_shadow      {"contract_symbol": "MCHP261218C00077500", "current_drop_pct": 0.67, "early_entry_score": 0.753, "early_reclaim_pct": 84.2, "entry_ask": 7.9, "entry_bid": 6.9, "entry_mode": "early", "entry_option_price": 7.4, "hypothetical_budget": 32204.65, "hypothetical_contracts": 43, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 827.0, "option_spread_pct": 13.51, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.753, "early_reclaim_pct": 84.2, "matched_signals": 39, "recovery_stability_score": 0.707, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.469, "trend_health_status": "ok"}, {"current_drop_pct": 0.83, "early_entry_score": 0.742, "early_reclaim_pct": 76.3, "matched_signals": 40, "recovery_stability_score": 0.898, "success_rate": 90.0, "ticker": "ADBE", "timing_score": 0.47, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T00:00:06.637519-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261029104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261029104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261029104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261029104005)

</details>
