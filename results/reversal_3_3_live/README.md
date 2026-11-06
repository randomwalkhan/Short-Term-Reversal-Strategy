# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 15:35:03 EST`
Last processed slot: `manage_1530`

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
- Equity: `$120,192.80`
- Realized PnL: `$113,162.80`
- Unrealized PnL: `$-2,970.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MDLZ     option         option MDLZ261218C00065000       2026-11-06                   0    198     61380.0                 58410.0          3.1           2.95       66.26         65.94          bid_ask_mid                       2.95                bid_ask_mid                    True         -2970.0                  -4.84         93.33               15              0.83         28.08            29.0                  30.66                3966.0           43.0               0.06                      ok
```

## Today's Closed Trades (2026-11-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  ORLY     option         option ORLY261218C00095000    345          2026-11-05         2026-11-06        1.875      1.6875 -6468.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           91.67               12            1.35              0.63         66.55                30.66         0.560          pass              0.564             61.2                           0.351                3.32              0.723                                 ok            True                  False
   KDP           95.24               21            0.77              0.20         36.80                35.93         0.558          pass              0.757             75.8                           0.618                5.55              0.613                                 ok            True                  False
   PEP           84.62               13            1.35              1.35        142.13                27.68         0.536          pass              0.370             58.0                           0.380                3.69              0.637                                 ok            True                  False
   ADP           83.33               18            1.18              2.53        306.06                28.50         0.521          pass              0.398             68.0                           0.627               -0.21              0.264                                 ok            True                  False
  ORLY          100.00               15            1.42              0.91         91.10                25.42         0.520          pass              0.647             53.7                           0.547                0.30              0.124                                 ok            True                  False
  CTAS           93.75               16            1.40              2.23        225.46                27.57         0.510          pass              0.611             51.2                           0.432               -0.39              0.284                                 ok            True                  False
  MSFT          100.00               29            0.65              2.45        534.88                35.82         0.509          pass              0.812             78.0                           0.529                1.51              0.139                                 ok            True                  False
  ALNY           85.11               47            0.36              0.39        156.49               108.53         0.687          pass              0.634             76.3                           0.506              -30.32             -4.702            downtrend_blocked_slope           False                  False
  FTNT           78.26               23            2.13              1.83        121.73                92.45         0.646          pass              0.199             16.1                           0.246              -33.39             -4.933 downtrend_blocked_slope_and_streak           False                  False
  MSTR           88.10               42            0.16              0.15        129.24                81.05         0.561          pass              0.755             94.3                           0.702              -11.59             -1.018            downtrend_blocked_slope           False                  False
  PAYX           75.00                4            2.02              1.69        118.78                35.22         0.561          pass              0.216             53.5                           0.686                0.21              0.523                                 ok           False                  False
 CMCSA           83.33                6            1.96              0.34         24.80                35.54         0.559          pass              0.293             49.5                           0.352                7.80              1.375                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-06T15:10:05.130683-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T15:05:05.959531-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T15:00:05.889317-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T14:55:04.803922-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-06T14:50:04.935495-05:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 61380.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "contracts": 198, "early_entry_score": 0.675, "entry_mode": "regular", "entry_option_price": 3.1, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 3966.0, "option_spread_pct": 6.45, "option_volume": 43.0, "success_rate": 93.33, "ticker": "MDLZ", "timing_score": 0.574}
2026-11-06T14:50:04.935495-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-06", "training_samples": 6334, "window": 5}
2026-11-06T12:00:04.909641-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:55:04.780197-05:00 early_entry_1155 early_entry_shadow {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "entry_ask": 4.3, "entry_bid": 4.05, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 5.99, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.732, "early_reclaim_pct": 83.7, "matched_signals": 38, "recovery_stability_score": 0.712, "success_rate": 89.47, "ticker": "SBUX", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:50:06.989427-05:00 early_entry_1150 early_entry_shadow {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 83.0, "entry_ask": 4.25, "entry_bid": 4.1, "entry_mode": "early", "entry_option_price": 4.175, "hypothetical_budget": 61581.4, "hypothetical_contracts": 147, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 3.59, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.669, "shadow_only": true, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 83.0, "matched_signals": 37, "recovery_stability_score": 0.669, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:45:04.961396-05:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "SBUX261218C00105000", "current_drop_pct": 0.52, "early_entry_score": 0.747, "early_reclaim_pct": 84.0, "entry_ask": 4.2, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.05, "hypothetical_budget": 61581.4, "hypothetical_contracts": 152, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 4507.0, "option_spread_pct": 7.41, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.747, "early_reclaim_pct": 84.0, "matched_signals": 39, "recovery_stability_score": 0.646, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106153503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106153503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106153503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106153503)

</details>
