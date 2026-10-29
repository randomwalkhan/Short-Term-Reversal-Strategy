# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-29 11:00:06 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$124,709.30`
- Realized PnL: `$119,884.30`
- Unrealized PnL: `$-5,175.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261218C00110000       2026-10-28                   1     90     65475.0                 60300.0         7.28            6.7      110.47        109.06          bid_ask_mid                        6.7                bid_ask_mid                    True         -5175.0                   -7.9         80.77               26              0.82         42.92            44.4                  35.12                4095.0         1198.0               0.02                      ok
```

## Today's Closed Trades (2026-10-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           89.29               28            2.18              2.21        144.21                71.12         0.563          pass              0.573             49.7                           0.616               -6.14             -0.050                                 ok            True                  False
   ROP           88.57               35            0.52              1.59        439.98                39.09         0.524          pass              0.590             47.5                           0.441               14.63              1.750                                 ok            True                  False
  UPRO           82.61               23            1.24              1.31        150.58                30.20         0.517          pass              0.322             38.1                           0.480               -1.49             -0.009                                 ok            True                  False
  SOXL           69.57               23            4.39              3.30        105.94               137.18         0.646          pass              0.312             53.5                           0.572               -4.39              0.029                                 ok           False                  False
  MPWR           67.86               28            1.34             11.36       1206.35                59.53         0.560          pass              0.373             65.7                           0.660               -4.34             -0.523            downtrend_blocked_slope           False                  False
  CSCO           72.22               18            1.24              0.96        109.88                35.33         0.551          pass              0.159             16.7                           0.217               -0.85              0.233                                 ok           False                  False
  MELI           78.57               28            1.55             18.18       1665.30                48.85         0.532          pass              0.304             43.6                           0.466              -11.30             -1.364 downtrend_blocked_slope_and_streak           False                  False
  AVGO           50.00               10            2.56              6.31        349.10                43.15         0.526          pass              0.145             30.7                           0.551               -0.45              0.216                                 ok           False                  False
  NVDA           75.00               28            0.55              0.82        215.03                30.56         0.525          pass              0.366             64.4                           0.668               -1.39             -0.082                                 ok           False                  False
   ADP           93.33               30            0.26              0.51        285.15                29.33         0.524          pass              0.688             48.8                           0.372               -0.35              0.077                                 ok           False                  False
   LIN           75.00                8            1.29              4.59        506.19                14.48         0.523          pass              0.108             18.5                           0.199                1.70              0.210                                 ok           False                  False
    MU           72.22               18            2.93             20.14        974.60                57.32         0.517          pass              0.200             31.7                           0.512                2.49              0.570                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-29T11:00:06.462507-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "QCOM261218C00185000", "current_drop_pct": 0.85, "early_entry_score": 0.75, "early_reclaim_pct": 62.8, "entry_ask": 12.1, "entry_bid": 11.75, "entry_mode": "early", "entry_option_price": 11.925, "hypothetical_budget": 32204.65, "hypothetical_contracts": 27, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 3107.0, "option_spread_pct": 2.94, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.75, "early_reclaim_pct": 62.8, "matched_signals": 32, "recovery_stability_score": 0.605, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.479, "trend_health_status": "ok"}, {"current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 85.5, "matched_signals": 35, "recovery_stability_score": 0.552, "success_rate": 88.57, "ticker": "INTU", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:55:05.704456-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:50:05.735637-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:45:05.600888-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:40:05.590194-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "QCOM261218C00190000", "current_drop_pct": 0.9, "early_entry_score": 0.744, "early_reclaim_pct": 60.9, "entry_ask": 10.15, "entry_bid": 9.6, "entry_mode": "early", "entry_option_price": 9.875, "hypothetical_budget": 32204.65, "hypothetical_contracts": 32, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 1786.0, "option_spread_pct": 5.57, "option_volume": 811.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.744, "early_reclaim_pct": 60.9, "matched_signals": 32, "recovery_stability_score": 0.662, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:35:05.458266-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:30:06.113309-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:25:05.571151-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:20:06.041880-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "QCOM261218C00190000", "current_drop_pct": 0.87, "early_entry_score": 0.747, "early_reclaim_pct": 61.8, "entry_ask": 10.2, "entry_bid": 9.95, "entry_mode": "early", "entry_option_price": 10.075, "hypothetical_budget": 32204.65, "hypothetical_contracts": 31, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 1786.0, "option_spread_pct": 2.48, "option_volume": 811.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.747, "early_reclaim_pct": 61.8, "matched_signals": 32, "recovery_stability_score": 0.651, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:15:06.489089-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                     {"contract_symbol": "ADBE261218C00250000", "current_drop_pct": 0.9, "early_entry_score": 0.697, "early_reclaim_pct": 74.4, "entry_ask": 18.1, "entry_bid": 15.55, "entry_mode": "early", "entry_option_price": 16.825, "hypothetical_budget": 32204.65, "hypothetical_contracts": 19, "matched_signals": 37, "option_liquidity_status": "wide_spread", "option_open_interest": 5906.0, "option_spread_pct": 15.16, "option_volume": 156.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.697, "early_reclaim_pct": 74.4, "matched_signals": 37, "recovery_stability_score": 0.759, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.484, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261029110006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261029110006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261029110006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261029110006)

</details>
