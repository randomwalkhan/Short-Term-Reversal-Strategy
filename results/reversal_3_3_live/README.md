# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-29 14:55:06 EDT`
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

- Cash: `$61,734.30`
- Equity: `$123,541.80`
- Realized PnL: `$113,336.80`
- Unrealized PnL: `$205.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261218C00140000       2026-10-29                   0     41     61602.5                 61807.5        15.02          15.08      141.06        141.62          bid_ask_mid                      15.08                bid_ask_mid                    True           205.0                   0.33         86.96               23              2.82         69.46           68.08                  71.12                1665.0           96.0               0.02                      ok
```

## Today's Closed Trades (2026-10-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261218C00110000     90          2026-10-28         2026-10-29        7.275      6.5475 -6547.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           87.50               24            2.56              2.60        144.05                71.12         0.564          pass              0.472             40.9                           0.352               -6.50             -0.068                                 ok            True                  False
  UPRO           92.31               13            1.89              2.00        150.28                30.20         0.551          pass              0.454             16.8                           0.370               -2.14             -0.040                                 ok            True                  False
  ADBE           87.10               31            1.15              2.00        248.90                41.65         0.505          pass              0.582             67.3                           0.538               -1.90              0.038                                 ok            True                  False
  TMUS           82.14               28            0.67              0.70        147.78                64.00         0.649          pass              0.294             17.4                           0.210               -6.33             -0.898            downtrend_blocked_slope           False                  False
  MPWR           63.64               22            1.88             15.97       1204.37                59.53         0.561          pass              0.292             51.8                           0.471               -4.87             -0.548            downtrend_blocked_slope           False                  False
  CSCO           69.23               13            1.64              1.26        109.75                35.33         0.555          pass              0.101              8.4                           0.237               -1.24              0.215                                 ok           False                  False
   WDC           73.17               41            0.87              2.41        395.39                80.12         0.550          pass              0.493             79.5                           0.482               10.25              1.173                                 ok           False                  False
  MELI           79.31               29            1.28             15.03       1666.65                48.85         0.542          pass              0.341             53.4                           0.639              -11.06             -1.352 downtrend_blocked_slope_and_streak           False                  False
  AVGO           64.29               14            2.11              5.20        349.58                43.15         0.540          pass              0.209             42.9                           0.507                0.02              0.237                                 ok           False                  False
  NVDA           75.00               20            1.17              1.76        214.62                30.56         0.540          pass              0.192             23.6                           0.314               -2.01             -0.111                                 ok           False                  False
  SOXL           66.67               21            6.73              5.05        105.18               137.18         0.520          pass              0.212             28.9                           0.303               -6.73             -0.083                                 ok           False                  False
   LIN           77.78                9            1.27              4.53        506.22                14.48         0.515          pass              0.153             33.7                           0.372                1.72              0.211                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-29T14:55:06.721591-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-10-29T14:50:05.643869-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"allocated_cash": 61602.5, "asset_type": "option", "contract_symbol": "MSTR261218C00140000", "contracts": 41, "early_entry_score": 0.432, "entry_mode": "regular", "entry_option_price": 15.025, "execution_mode": "option", "matched_signals": 23, "option_liquidity_status": "ok", "option_open_interest": 1665.0, "option_spread_pct": 2.33, "option_volume": 96.0, "success_rate": 86.96, "ticker": "MSTR", "timing_score": 0.554}
2026-10-29T14:50:05.643869-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-29", "training_samples": 6227, "window": 5}
2026-10-29T12:00:05.637930-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                        {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.02, "early_entry_score": 0.747, "early_reclaim_pct": 76.4, "entry_ask": 14.7, "entry_bid": 14.3, "entry_mode": "early", "entry_option_price": 14.5, "hypothetical_budget": 61668.4, "hypothetical_contracts": 42, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 2.76, "option_volume": 136.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.594, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.747, "early_reclaim_pct": 76.4, "matched_signals": 34, "recovery_stability_score": 0.658, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.594, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:55:05.739980-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.04, "early_entry_score": 0.745, "early_reclaim_pct": 76.0, "entry_ask": 14.8, "entry_bid": 14.35, "entry_mode": "early", "entry_option_price": 14.575, "hypothetical_budget": 61668.4, "hypothetical_contracts": 42, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 3.09, "option_volume": 136.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.667, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.593, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.745, "early_reclaim_pct": 76.0, "matched_signals": 34, "recovery_stability_score": 0.667, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.593, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:50:04.572626-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.17, "early_entry_score": 0.722, "early_reclaim_pct": 72.9, "entry_ask": 14.95, "entry_bid": 14.55, "entry_mode": "early", "entry_option_price": 14.75, "hypothetical_budget": 61668.4, "hypothetical_contracts": 41, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 2.71, "option_volume": 135.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 90.91, "ticker": "MSTR", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 1.17, "early_entry_score": 0.722, "early_reclaim_pct": 72.9, "matched_signals": 33, "recovery_stability_score": 0.703, "success_rate": 90.91, "ticker": "MSTR", "timing_score": 0.591, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:45:01.204806-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                       {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.11, "early_entry_score": 0.74, "early_reclaim_pct": 74.4, "entry_ask": 14.45, "entry_bid": 14.0, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 61668.4, "hypothetical_contracts": 43, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 3.16, "option_volume": 135.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.738, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.589, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.74, "early_reclaim_pct": 74.4, "matched_signals": 34, "recovery_stability_score": 0.738, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.589, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:40:06.675305-04:00 early_entry_1140 early_entry_shadow                                              {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.11, "early_entry_score": 0.74, "early_reclaim_pct": 74.4, "entry_ask": 14.55, "entry_bid": 14.1, "entry_mode": "early", "entry_option_price": 14.325, "hypothetical_budget": 61668.4, "hypothetical_contracts": 43, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 3.14, "option_volume": 135.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.744, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.589, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.74, "early_reclaim_pct": 74.4, "matched_signals": 34, "recovery_stability_score": 0.744, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.589, "trend_health_status": "ok"}, {"current_drop_pct": 0.54, "early_entry_score": 0.706, "early_reclaim_pct": 87.5, "matched_signals": 35, "recovery_stability_score": 0.67, "success_rate": 88.57, "ticker": "INTU", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:35:06.603938-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                       {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 0.55, "early_entry_score": 0.774, "early_reclaim_pct": 87.3, "entry_ask": 14.6, "entry_bid": 14.1, "entry_mode": "early", "entry_option_price": 14.35, "hypothetical_budget": 61668.4, "hypothetical_contracts": 42, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 3.48, "option_volume": 135.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.852, "shadow_only": true, "success_rate": 89.74, "ticker": "MSTR", "timing_score": 0.589, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.774, "early_reclaim_pct": 87.3, "matched_signals": 39, "recovery_stability_score": 0.852, "success_rate": 89.74, "ticker": "MSTR", "timing_score": 0.589, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:30:06.096109-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "INTU261204C00325000", "current_drop_pct": 0.59, "early_entry_score": 0.702, "early_reclaim_pct": 86.4, "entry_ask": 26.9, "entry_bid": 21.9, "entry_mode": "early", "entry_option_price": 24.4, "hypothetical_budget": 61668.4, "hypothetical_contracts": 25, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 4.0, "option_spread_pct": 20.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.591, "shadow_only": true, "success_rate": 88.57, "ticker": "INTU", "timing_score": 0.476, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.702, "early_reclaim_pct": 86.4, "matched_signals": 35, "recovery_stability_score": 0.591, "success_rate": 88.57, "ticker": "INTU", "timing_score": 0.476, "trend_health_status": "ok"}, {"current_drop_pct": 1.35, "early_entry_score": 0.695, "early_reclaim_pct": 68.8, "matched_signals": 32, "recovery_stability_score": 0.787, "success_rate": 90.62, "ticker": "MSTR", "timing_score": 0.587, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261029145506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261029145506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261029145506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261029145506)

</details>
