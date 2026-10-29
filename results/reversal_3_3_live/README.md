# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-29 10:25:05 EDT`
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
- Equity: `$128,534.30`
- Realized PnL: `$119,884.30`
- Unrealized PnL: `$-1,350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261218C00110000       2026-10-28                   1     90     65475.0                 64125.0         7.28           7.12      110.47        109.72          bid_ask_mid                       7.12                bid_ask_mid                    True         -1350.0                  -2.06         80.77               26              0.82         42.92           45.25                  35.12                4095.0         1198.0               0.02                      ok
```

## Today's Closed Trades (2026-10-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.33               18            3.10              3.15        143.81                71.12         0.566          pass              0.284             28.3                           0.446               -7.03             -0.093                                 ok            True                  False
  CSCO           83.33               30            0.55              0.43        110.11                35.33         0.531          pass              0.427             50.6                           0.433               -0.15              0.265                                 ok            True                  False
  UPRO           82.61               23            1.21              1.28        150.59                30.20         0.518          pass              0.326             39.5                           0.589               -1.46             -0.008                                 ok            True                  False
  ADBE           85.71               28            1.52              2.65        248.62                41.65         0.501          pass              0.492             56.6                           0.439               -2.26              0.021                                 ok            True                  False
  SOXL           68.18               22            5.05              3.79        105.72               137.18         0.613          pass              0.281             46.6                           0.776               -5.05             -0.002                                 ok           False                  False
  PAYX           80.77               26            0.01              0.01        108.21                35.46         0.584          pass              0.396             70.0                           0.375               -1.34             -0.036                                 ok           False                  False
  MPWR           65.22               23            1.73             14.64       1204.95                59.53         0.566          pass              0.311             55.8                           0.748               -4.71             -0.541            downtrend_blocked_slope           False                  False
  MELI           80.00               30            1.28             14.97       1666.67                48.85         0.536          pass              0.348             53.6                           0.592              -11.05             -1.352 downtrend_blocked_slope_and_streak           False                  False
  NVDA           73.91               23            0.88              1.33        214.81                30.56         0.536          pass              0.268             42.4                           0.596               -1.73             -0.098                                 ok           False                  False
   ROP           89.19               37            0.37              1.13        440.18                39.09         0.526          pass              0.508             10.0                           0.235               14.80              1.757                                 ok           False                  False
   LIN           77.78                9            1.20              4.26        506.33                14.48         0.524          pass              0.125             24.3                           0.211                1.79              0.215                                 ok           False                  False
   ADP           93.33               30            0.41              0.82        285.02                29.33         0.516          pass              0.550              3.3                           0.082               -0.51              0.070                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-29T10:25:05.571151-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:20:06.041880-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "QCOM261218C00190000", "current_drop_pct": 0.87, "early_entry_score": 0.747, "early_reclaim_pct": 61.8, "entry_ask": 10.2, "entry_bid": 9.95, "entry_mode": "early", "entry_option_price": 10.075, "hypothetical_budget": 32204.65, "hypothetical_contracts": 31, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 1786.0, "option_spread_pct": 2.48, "option_volume": 811.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.747, "early_reclaim_pct": 61.8, "matched_signals": 32, "recovery_stability_score": 0.651, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:15:06.489089-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                    {"contract_symbol": "ADBE261218C00250000", "current_drop_pct": 0.9, "early_entry_score": 0.697, "early_reclaim_pct": 74.4, "entry_ask": 18.1, "entry_bid": 15.55, "entry_mode": "early", "entry_option_price": 16.825, "hypothetical_budget": 32204.65, "hypothetical_contracts": 19, "matched_signals": 37, "option_liquidity_status": "wide_spread", "option_open_interest": 5906.0, "option_spread_pct": 15.16, "option_volume": 156.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.759, "shadow_only": true, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.697, "early_reclaim_pct": 74.4, "matched_signals": 37, "recovery_stability_score": 0.759, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.484, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-29T10:10:04.545250-04:00 early_entry_1010 early_entry_shadow       {"contract_symbol": "MCHP261218C00077500", "current_drop_pct": 0.6, "early_entry_score": 0.757, "early_reclaim_pct": 85.7, "entry_ask": 7.9, "entry_bid": 6.9, "entry_mode": "early", "entry_option_price": 7.4, "hypothetical_budget": 32204.65, "hypothetical_contracts": 43, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 827.0, "option_spread_pct": 13.51, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.788, "shadow_only": true, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.757, "early_reclaim_pct": 85.7, "matched_signals": 39, "recovery_stability_score": 0.788, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.9, "early_entry_score": 0.696, "early_reclaim_pct": 74.1, "matched_signals": 37, "recovery_stability_score": 0.812, "success_rate": 89.19, "ticker": "ADBE", "timing_score": 0.484, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:05:06.192375-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ADBE261218C00250000", "current_drop_pct": 0.64, "early_entry_score": 0.777, "early_reclaim_pct": 81.8, "entry_ask": 17.25, "entry_bid": 15.55, "entry_mode": "early", "entry_option_price": 16.4, "hypothetical_budget": 32204.65, "hypothetical_contracts": 19, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 5906.0, "option_spread_pct": 10.37, "option_volume": 156.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.915, "shadow_only": true, "success_rate": 90.7, "ticker": "ADBE", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.777, "early_reclaim_pct": 81.8, "matched_signals": 43, "recovery_stability_score": 0.915, "success_rate": 90.7, "ticker": "ADBE", "timing_score": 0.464, "trend_health_status": "ok"}, {"current_drop_pct": 1.41, "early_entry_score": 0.758, "early_reclaim_pct": 84.8, "matched_signals": 34, "recovery_stability_score": 0.949, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:00:05.728324-04:00 early_entry_1000 early_entry_shadow      {"contract_symbol": "MCHP261218C00077500", "current_drop_pct": 0.67, "early_entry_score": 0.753, "early_reclaim_pct": 84.2, "entry_ask": 7.9, "entry_bid": 6.9, "entry_mode": "early", "entry_option_price": 7.4, "hypothetical_budget": 32204.65, "hypothetical_contracts": 43, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 827.0, "option_spread_pct": 13.51, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.753, "early_reclaim_pct": 84.2, "matched_signals": 39, "recovery_stability_score": 0.707, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.469, "trend_health_status": "ok"}, {"current_drop_pct": 0.83, "early_entry_score": 0.742, "early_reclaim_pct": 76.3, "matched_signals": 40, "recovery_stability_score": 0.898, "success_rate": 90.0, "ticker": "ADBE", "timing_score": 0.47, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T00:00:06.637519-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-10-28T15:50:06.462666-04:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TEAM261218C00230000", "fill_price": 19.1, "pnl": -2880.0, "reason": "time_exit_at_4pm_scan", "return_pct": -4.5, "ticker": "TEAM"}
2026-10-28T15:10:04.409011-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-28T15:05:05.708724-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261029102505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261029102505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261029102505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261029102505)

</details>
