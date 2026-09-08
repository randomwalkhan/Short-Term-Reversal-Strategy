# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 15:40:01 EDT`
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
- Equity: `$76,563.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-585.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   0     26     37180.0                 36595.0         14.3          14.08      209.63        208.51          bid_ask_mid                      14.08                bid_ask_mid                    True          -585.0                  -1.57         88.89               36              1.63         52.75           54.49                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261016C00145000     30          2026-09-04         2026-09-08       13.375     12.0375 -4012.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           83.33               24            2.22              3.31        211.68                91.63         0.645          pass              0.362             38.5                           0.258                9.28              1.037                                 ok            True                  False
   WMT           83.33               24            0.91              0.69        106.85                40.24         0.578          pass              0.341             33.8                           0.598               -0.31              0.236                                 ok            True                  False
  REGN          100.00               10            1.66              9.60        823.61                29.02         0.531          pass              0.608             51.6                           0.552               -1.75              0.119                                 ok            True                  False
  NVDA           90.00               20            2.03              3.28        228.96                44.80         0.526          pass              0.411              8.4                           0.304                8.25              0.849                                 ok            True                  False
    MU           85.71               35            0.89              6.31       1013.89                54.29         0.510          pass              0.397              8.9                           0.120               10.67              0.870                                 ok            True                  False
  UPRO           85.71               21            1.27              1.35        151.30                24.27         0.502          pass              0.364             29.3                           0.450                0.92              0.082                                 ok            True                  False
  PYPL           83.33                6            2.84              1.09         54.49                57.43         0.604          pass              0.207             19.2                           0.525              -13.21             -1.553 downtrend_blocked_slope_and_streak           False                  False
  MELI          100.00                8            2.73             37.79       1962.16                45.80         0.583          pass              0.528             23.3                           0.275               -1.21              0.036                                 ok           False                  False
  MSTR           73.68               19            4.16              4.16        141.02               102.15         0.575          pass              0.177             19.9                           0.337               11.60              1.155                                 ok           False                  False
  CPRT           80.00                5            3.22              0.76         33.39                42.28         0.525          pass              0.106             17.8                           0.404               -1.88             -0.017                                 ok           False                  False
 CMCSA           92.86               28            0.51              0.09         26.45                26.03         0.521          pass              0.739             74.5                           0.737               -2.46             -0.250            downtrend_blocked_slope           False                  False
  GILD          100.00                5            2.71              2.87        149.77                24.06         0.521          pass              0.531             26.1                           0.483                0.11              0.151                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908154001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908154001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908154001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908154001)

</details>
