# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-19 15:15:04 EDT`
Last processed slot: `manual`

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

- Cash: `$66,431.80`
- Equity: `$131,181.80`
- Realized PnL: `$121,531.80`
- Unrealized PnL: `$-350.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   ADP     option         option ADP261120C00290000       2026-10-19                   0     70     65100.0                 64750.0          9.3           9.25      287.14        286.71          bid_ask_mid                       9.25                bid_ask_mid                    True          -350.0                  -0.54         92.31               26              0.61         32.26           32.58                  21.32                 958.0           21.0               0.11                      ok
```

## Today's Closed Trades (2026-10-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     35          2026-10-16         2026-10-19        17.05       19.65 9100.0   15.249267 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ADP           91.30               23            0.76              1.55        288.24                21.32         0.527            pass              0.605             54.8                           0.364               10.16              1.085                                 ok            True                  False
  GILD           89.47               19            1.20              1.31        155.63                24.77         0.513            pass              0.404             13.4                           0.219                6.70              0.831                                 ok            True                  False
   KHC           84.62               13            1.84              0.30         23.55                22.28         0.503            pass              0.262             23.0                           0.388                6.43              0.727                                 ok            True                  False
  CTAS           92.86               28            0.71              1.06        213.23                23.07         0.501            pass              0.665             50.8                           0.457                8.58              0.985                                 ok            True                  False
  TMUS           76.19               21            1.07              1.19        158.59                56.39         0.641            pass              0.160              7.4                           0.227               -4.40             -0.654            downtrend_blocked_slope           False                  False
  PAYX           75.00               28            0.99              0.78        111.30                41.41         0.558            pass              0.307             43.7                           0.531               10.76              1.152                                 ok           False                  False
   CEG           90.00               10            2.86              5.44        269.04                59.14         0.554            pass              0.375             17.7                           0.383               -1.50             -0.715 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           95.45               22            0.41              0.19         63.83                19.69         0.541            pass              0.692             52.7                           0.513                8.81              0.872                                 ok           False                  False
  AMGN           77.78               18            1.27              3.86        430.84                28.96         0.530            pass              0.134              9.2                           0.113                5.96              0.735                                 ok           False                  False
   XEL           50.00                4            1.61              0.86         75.94                16.32         0.514            pass              0.051              0.0                           0.091                5.02              0.557                                 ok           False                  False
  CSCO           94.29               35            0.21              0.16        107.32                35.92         0.489 below_threshold              0.815             72.9                           0.530               -5.01             -0.801 downtrend_blocked_slope_and_streak           False                  False
  META           90.91               33            0.45              2.23        708.37                56.19         0.481 below_threshold              0.731             79.4                           0.781               -4.82             -0.220           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-19T15:10:06.181493-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-19T15:07:09.479134-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-19T14:50:05.293487-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 65100.0, "asset_type": "option", "contract_symbol": "ADP261120C00290000", "contracts": 70, "early_entry_score": 0.679, "entry_mode": "regular", "entry_option_price": 9.3, "execution_mode": "option", "matched_signals": 26, "option_liquidity_status": "ok", "option_open_interest": 958.0, "option_spread_pct": 10.75, "option_volume": 21.0, "success_rate": 92.31, "ticker": "ADP", "timing_score": 0.52}
2026-10-19T14:50:05.293487-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-19", "training_samples": 6120, "window": 5}
2026-10-19T12:00:05.186192-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.582, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.821, "early_reclaim_pct": 76.6, "matched_signals": 35, "recovery_stability_score": 0.582, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T11:55:09.715127-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.56, "early_entry_score": 0.861, "early_reclaim_pct": 79.7, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.861, "early_reclaim_pct": 79.7, "matched_signals": 38, "recovery_stability_score": 0.632, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T11:50:02.588008-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:45:09.986778-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-19T11:40:09.738573-04:00 early_entry_1140 early_entry_shadow   {"contract_symbol": "PYPL261127C00056000", "current_drop_pct": 0.51, "early_entry_score": 0.887, "early_reclaim_pct": 81.6, "entry_ask": 4.8, "entry_bid": 2.35, "entry_mode": "early", "entry_option_price": 3.575, "hypothetical_budget": 65765.9, "hypothetical_contracts": 183, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 68.53, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.887, "early_reclaim_pct": 81.6, "matched_signals": 40, "recovery_stability_score": 0.715, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-19T11:35:06.347486-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261019151504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261019151504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261019151504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261019151504)

</details>
