# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 15:05:01 EDT`
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

- Cash: `$41,035.60`
- Equity: `$81,985.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$825.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261016C00145000       2026-09-04                   0     30     40125.0                 40950.0        13.38          13.65      142.86        143.89          bid_ask_mid                      13.65                bid_ask_mid                    True           825.0                   2.06         82.86               35              1.36         73.28           72.07                 101.55                5516.0          964.0               0.01                      ok
```

## Today's Closed Trades (2026-09-04)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261016C00110000     99          2026-09-03         2026-09-04        3.725         4.4 6682.5   18.120805 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           84.21               38            0.64              0.65        144.54               101.55         0.659          pass              0.636             90.2                           0.880               20.66              1.374                                 ok            True                  False
  CRWD           90.00               40            0.97              1.47        214.34                92.33         0.631          pass              0.658             42.6                           0.456               10.90              1.405                                 ok            True                  False
   WMT           85.00               20            1.10              0.84        108.06                40.07         0.587          pass              0.284              8.4                           0.357                3.40              0.283                                 ok            True                  False
  REGN          100.00               10            1.57              9.26        839.50                28.19         0.551          pass              0.455              0.0                           0.186               -0.46              0.114                                 ok            True                  False
  MELI          100.00               35            0.50              6.98       1988.07                45.76         0.542          pass              0.802             60.2                           0.326                3.04              0.243                                 ok            True                  False
  VRTX           91.67               12            2.08              8.14        554.47                32.02         0.538          pass              0.497             39.7                           0.292               -0.31              0.069                                 ok            True                  False
  SBUX           95.45               22            0.74              0.55        105.59                21.61         0.527          pass              0.594             20.4                           0.263               -1.91             -0.168                                 ok            True                  False
  WDAY           85.71               14            4.31              6.24        204.24                73.93         0.513          pass              0.287             18.7                           0.326               -1.00              0.272                                 ok            True                  False
   KDP           86.21               29            0.81              0.19         32.80                30.98         0.510          pass              0.387             14.5                           0.149                1.79              0.167                                 ok            True                  False
   KHC           88.89               27            0.82              0.14         24.96                29.47         0.506          pass              0.481             26.8                           0.386               -2.99              0.023                                 ok            True                  False
  MNST           83.33               24            0.78              0.24         43.98               424.09         0.998          pass              0.341             19.8                           0.192               -8.49             -1.160 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00                2            3.74              1.49         56.18                56.63         0.579          pass              0.482              8.0                           0.267              -11.14             -1.631 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-04T15:05:01.435734-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-04T15:00:02.489419-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-04T14:55:06.412965-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-09-04T14:50:01.408299-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 40125.0, "asset_type": "option", "contract_symbol": "MSTR261016C00145000", "contracts": 30, "early_entry_score": 0.544, "entry_mode": "regular", "entry_option_price": 13.375, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 5516.0, "option_spread_pct": 1.12, "option_volume": 964.0, "success_rate": 82.86, "ticker": "MSTR", "timing_score": 0.635}
2026-09-04T14:50:01.408299-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-04", "training_samples": 5767, "window": 5}
2026-09-04T12:00:02.433039-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T11:55:02.514482-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "VRTX261016C00550000", "current_drop_pct": 0.99, "early_entry_score": 0.803, "early_reclaim_pct": 71.5, "entry_ask": 24.0, "entry_bid": 21.7, "entry_mode": "early", "entry_option_price": 22.85, "hypothetical_budget": 40580.3, "hypothetical_contracts": 17, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 220.0, "option_spread_pct": 10.07, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.49, "top_candidates": [{"current_drop_pct": 0.99, "early_entry_score": 0.803, "early_reclaim_pct": 71.5, "matched_signals": 31, "recovery_stability_score": 0.731, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.49, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T11:50:01.382488-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "VRTX261016C00550000", "current_drop_pct": 1.0, "early_entry_score": 0.802, "early_reclaim_pct": 71.0, "entry_ask": 24.5, "entry_bid": 21.6, "entry_mode": "early", "entry_option_price": 23.05, "hypothetical_budget": 40580.3, "hypothetical_contracts": 17, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 220.0, "option_spread_pct": 12.58, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.489, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.802, "early_reclaim_pct": 71.0, "matched_signals": 31, "recovery_stability_score": 0.707, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.489, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T11:45:06.187028-04:00 early_entry_1145 early_entry_shadow                       {"contract_symbol": "VRTX261016C00560000", "current_drop_pct": 1.02, "early_entry_score": 0.8, "early_reclaim_pct": 70.4, "entry_ask": 18.5, "entry_bid": 16.9, "entry_mode": "early", "entry_option_price": 17.7, "hypothetical_budget": 40580.3, "hypothetical_contracts": 22, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 286.0, "option_spread_pct": 9.04, "option_volume": 55.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.8, "early_reclaim_pct": 70.4, "matched_signals": 31, "recovery_stability_score": 0.676, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-04T11:40:05.184091-04:00 early_entry_1140 early_entry_shadow                   {"contract_symbol": "VRTX261016C00560000", "current_drop_pct": 1.06, "early_entry_score": 0.791, "early_reclaim_pct": 69.5, "entry_ask": 18.5, "entry_bid": 16.9, "entry_mode": "early", "entry_option_price": 17.7, "hypothetical_budget": 40580.3, "hypothetical_contracts": 22, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 286.0, "option_spread_pct": 9.04, "option_volume": 55.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 1.06, "early_entry_score": 0.791, "early_reclaim_pct": 69.5, "matched_signals": 30, "recovery_stability_score": 0.551, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904150501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904150501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904150501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904150501)

</details>
