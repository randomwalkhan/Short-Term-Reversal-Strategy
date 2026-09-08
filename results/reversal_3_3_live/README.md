# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 15:20:01 EDT`
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

- Cash: `$39,968.10`
- Equity: `$76,368.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-780.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   0     26     37180.0                 36400.0         14.3           14.0      209.63        209.46          bid_ask_mid                       14.0                bid_ask_mid                    True          -780.0                   -2.1         88.89               36              1.63         52.75           52.42                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261016C00145000     30          2026-09-04         2026-09-08       13.375     12.0375 -4012.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           88.89               36            1.66              2.47        212.04                91.63         0.616            pass              0.634             54.1                           0.519                9.91              1.064                                 ok            True                  False
   WMT           84.62               26            0.88              0.66        106.86                40.24         0.570            pass              0.396             36.5                           0.619               -0.27              0.237                                 ok            True                  False
  REGN          100.00               10            1.55              8.98        823.87                29.02         0.537            pass              0.618             54.7                           0.676               -1.64              0.124                                 ok            True                  False
  NVDA           89.47               19            2.14              3.46        228.88                44.80         0.524            pass              0.375              3.3                           0.146                8.13              0.844                                 ok            True                  False
    MU           86.49               37            0.63              4.50       1014.66                54.29         0.515            pass              0.480             25.1                           0.211               10.95              0.882                                 ok            True                  False
  MSFT           88.89               18            1.46              5.10        497.52                23.39         0.502            pass              0.412             23.8                           0.586                1.05              0.128                                 ok            True                  False
  AAPL           80.00               15            1.31              2.93        318.71                21.39         0.500 below_threshold              0.134             17.0                           0.350                1.75              0.395                                 ok            True                  False
  PYPL           80.00                5            3.07              1.18         54.45                57.43         0.592            pass              0.096             12.4                           0.368              -13.42             -1.565 downtrend_blocked_slope_and_streak           False                  False
  MELI          100.00                8            2.72             37.69       1962.21                45.80         0.584            pass              0.529             23.5                           0.380               -1.20              0.036                                 ok           False                  False
  MSTR           72.22               18            4.31              4.31        140.95               102.15         0.570            pass              0.162             17.1                           0.293               11.43              1.148                                 ok           False                  False
  SBUX          100.00                1            2.48              1.81        103.69                22.08         0.551            pass              0.469              4.8                           0.218               -5.22             -0.380            downtrend_blocked_slope           False                  False
 CMCSA           92.59               27            0.64              0.12         26.44                26.03         0.519            pass              0.705             67.9                           0.780               -2.59             -0.256            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-08T15:10:02.485838-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-08T15:05:04.629730-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-08T15:00:03.621763-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-08T14:55:03.619621-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "already_processed"}
2026-09-08T14:50:01.652709-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"allocated_cash": 37180.0, "asset_type": "option", "contract_symbol": "CRWD261016C00210000", "contracts": 26, "early_entry_score": 0.637, "entry_mode": "regular", "entry_option_price": 14.3, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 699.0, "option_spread_pct": 4.2, "option_volume": 116.0, "success_rate": 88.89, "ticker": "CRWD", "timing_score": 0.617}
2026-09-08T14:50:01.652709-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-08", "training_samples": 5748, "window": 5}
2026-09-08T12:00:01.401463-04:00 early_entry_1200 early_entry_shadow                            {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.67, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "entry_ask": 10.05, "entry_bid": 9.45, "entry_mode": "early", "entry_option_price": 9.75, "hypothetical_budget": 38574.05, "hypothetical_contracts": 39, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 6.15, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 92.86, "ticker": "FTNT", "timing_score": 0.472, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "matched_signals": 42, "recovery_stability_score": 0.62, "success_rate": 92.86, "ticker": "FTNT", "timing_score": 0.472, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.716, "early_reclaim_pct": 77.6, "matched_signals": 38, "recovery_stability_score": 0.691, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:55:05.335939-04:00 early_entry_1155 early_entry_shadow                              {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.6, "entry_ask": 10.1, "entry_bid": 9.15, "entry_mode": "early", "entry_option_price": 9.625, "hypothetical_budget": 38574.05, "hypothetical_contracts": 40, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 9.87, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.6, "matched_signals": 40, "recovery_stability_score": 0.605, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "trend_health_status": "ok"}, {"current_drop_pct": 0.97, "early_entry_score": 0.693, "early_reclaim_pct": 74.9, "matched_signals": 37, "recovery_stability_score": 0.648, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:50:01.520765-04:00 early_entry_1150 early_entry_shadow                           {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 73.9, "entry_ask": 10.15, "entry_bid": 9.15, "entry_mode": "early", "entry_option_price": 9.65, "hypothetical_budget": 38574.05, "hypothetical_contracts": 39, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 10.36, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.71, "shadow_only": true, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 73.9, "matched_signals": 41, "recovery_stability_score": 0.71, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.474, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.716, "early_reclaim_pct": 77.6, "matched_signals": 38, "recovery_stability_score": 0.648, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:45:03.461951-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.71, "early_entry_score": 0.755, "early_reclaim_pct": 81.7, "entry_ask": 7.0, "entry_bid": 5.9, "entry_mode": "early", "entry_option_price": 6.45, "hypothetical_budget": 38574.05, "hypothetical_contracts": 59, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 17.05, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.645, "shadow_only": true, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.755, "early_reclaim_pct": 81.7, "matched_signals": 40, "recovery_stability_score": 0.645, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.434, "trend_health_status": "ok"}, {"current_drop_pct": 1.34, "early_entry_score": 0.676, "early_reclaim_pct": 62.8, "matched_signals": 37, "recovery_stability_score": 0.699, "success_rate": 89.19, "ticker": "CRWD", "timing_score": 0.629, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908152001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908152001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908152001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908152001)

</details>
