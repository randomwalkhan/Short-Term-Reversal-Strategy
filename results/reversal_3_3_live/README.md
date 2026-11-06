# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 14:50:04 EST`
Last processed slot: `entry_1500`

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

- Cash: `$61,782.80`
- Equity: `$123,162.80`
- Realized PnL: `$113,162.80`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MDLZ     option         option MDLZ261218C00065000       2026-11-06                   0    198     61380.0                 61380.0          3.1            3.1       66.26         66.26          bid_ask_mid                        3.1                bid_ask_mid                    True             0.0                    0.0         93.33               15              0.83         28.08           28.08                  30.66                3966.0           43.0               0.06                      ok
```

## Today's Closed Trades (2026-11-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  ORLY     option         option ORLY261218C00095000    345          2026-11-05         2026-11-06        1.875      1.6875 -6468.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.33               15            0.83              0.39         66.65                30.66         0.574          pass              0.675             76.1                           0.542                3.86              0.747                                 ok            True                  False
   KDP           95.24               21            0.77              0.20         36.80                35.93         0.558          pass              0.757             75.8                           0.564                5.55              0.613                                 ok            True                  False
 CMCSA           92.86               14            1.29              0.22         24.85                35.54         0.558          pass              0.626             66.9                           0.630                8.55              1.406                                 ok            True                  False
  COST           83.33               18            0.90              6.71       1062.71                23.23         0.535          pass              0.375             59.9                           0.363                5.41              0.717                                 ok            True                  False
   PEP           83.33               18            0.98              0.98        142.29                27.68         0.527          pass              0.404             69.6                           0.631                4.08              0.654                                 ok            True                  False
  CTAS           94.12               17            1.23              1.95        225.57                27.57         0.515          pass              0.646             57.1                           0.518               -0.21              0.291                                 ok            True                  False
   ADP           85.71               21            1.06              2.28        306.16                28.50         0.512          pass              0.490             71.2                           0.715               -0.09              0.269                                 ok            True                  False
  ROST           81.25               16            1.56              2.58        234.13                35.60         0.512          pass              0.147              7.5                           0.193                0.98              0.263                                 ok            True                  False
  MSFT          100.00               29            0.69              2.60        534.82                35.82         0.506          pass              0.807             76.7                           0.465                1.47              0.137                                 ok            True                  False
  ALNY           84.44               45            0.42              0.47        156.46               108.53         0.693          pass              0.603             71.8                           0.443              -30.37             -4.705            downtrend_blocked_slope           False                  False
  FTNT           80.77               26            1.84              1.57        121.84                92.45         0.648          pass              0.275             27.7                           0.467              -33.19             -4.920 downtrend_blocked_slope_and_streak           False                  False
  MSTR           88.24               34            0.88              0.80        128.96                81.05         0.564          pass              0.643             69.2                           0.653              -12.23             -1.051            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-06T14:50:04.935495-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 61380.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "contracts": 198, "early_entry_score": 0.675, "entry_mode": "regular", "entry_option_price": 3.1, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 3966.0, "option_spread_pct": 6.45, "option_volume": 43.0, "success_rate": 93.33, "ticker": "MDLZ", "timing_score": 0.574}
2026-11-06T14:50:04.935495-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-06", "training_samples": 6334, "window": 5}
2026-11-06T12:00:04.909641-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:55:04.780197-05:00 early_entry_1155 early_entry_shadow {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "entry_ask": 4.3, "entry_bid": 4.05, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 5.99, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "matched_signals": 38, "recovery_stability_score": 0.712, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:50:06.989427-05:00 early_entry_1150 early_entry_shadow {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 83.0, "entry_ask": 4.25, "entry_bid": 4.1, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 3.59, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.669, "shadow_only": true, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 83.0, "matched_signals": 37, "recovery_stability_score": 0.669, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:45:04.961396-05:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.52, "early_entry_score": 0.747, "early_reclaim_pct": 84.0, "entry_ask": 4.2, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.05, "hypothetical_budget": 61581.4, "hypothetical_contracts": 152, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 7.41, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.747, "early_reclaim_pct": 84.0, "matched_signals": 39, "recovery_stability_score": 0.646, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:40:05.161435-05:00 early_entry_1140 early_entry_shadow  {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.64, "early_entry_score": 0.694, "early_reclaim_pct": 80.4, "entry_ask": 4.2, "entry_bid": 4.15, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 1.2, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.587, "shadow_only": true, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.694, "early_reclaim_pct": 80.4, "matched_signals": 36, "recovery_stability_score": 0.587, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:35:06.887510-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:30:05.913627-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:25:05.831838-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106145004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106145004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106145004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106145004)

</details>
