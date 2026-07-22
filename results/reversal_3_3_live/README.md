# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 10:00:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$17,264.25`
- Equity: `$35,964.25`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$1,787.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 18700.0         3.08            3.4       55.67         55.82          bid_ask_mid                        3.4                bid_ask_mid                    True          1787.5                  10.57          80.0               10              2.03         42.85           47.83                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.76               29            1.26              0.52         58.63               115.77         0.698          pass              0.500             76.5                           0.930               -6.33             -1.387                                 ok            True                  False
  AAPL           96.55               29            0.57              1.31        327.18                37.60         0.589          pass              0.613              9.0                           0.114                3.98              0.547                                 ok            True                  False
   ADP           96.55               29            0.61              1.06        245.77                36.45         0.566          pass              0.649             21.8                           0.202                1.38              0.349                                 ok            True                  False
  ABNB           93.75               16            2.05              2.07        143.21                31.72         0.531          pass              0.499             13.0                           0.175               -1.27             -0.193                                 ok            True                  False
   TRI           86.49               37            0.51              0.32         90.56                49.06         0.520          pass              0.546             47.1                           0.360                1.52              0.420                                 ok            True                  False
  DXCM           85.71               21            1.74              0.91         74.36                40.17         0.514          pass              0.352             24.9                           0.236               -0.82              0.127                                 ok            True                  False
  CRWD           86.21               29            1.44              1.92        190.33                59.78         0.508          pass              0.508             55.0                           0.372               -1.42              0.070                                 ok            True                  False
    MU           81.82               33            0.01              0.05        970.80               110.72         0.726          pass              0.574             99.9                           0.989                2.31             -0.618                                 ok           False                  False
  AMAT           90.91               33            0.49              1.92        563.73               100.84         0.724          pass              0.785             89.4                           0.928               -1.52             -0.799 downtrend_blocked_slope_and_streak           False                  False
  KLAC           88.89               36            0.55              0.83        217.20               102.77         0.716          pass              0.747             88.2                           0.905               -2.17             -0.716 downtrend_blocked_slope_and_streak           False                  False
  LRCX           90.00               30            0.65              1.47        321.37                94.63         0.690          pass              0.727             86.0                           0.946               -3.98             -1.045 downtrend_blocked_slope_and_streak           False                  False
  MSTR           75.61               41            1.03              0.74        101.63                91.33         0.619          pass              0.455             64.2                           0.692                7.48              0.737                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-22T10:00:06.589934-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.69, "early_entry_score": 0.836, "early_reclaim_pct": 74.2, "entry_ask": 108.0, "entry_bid": 87.1, "entry_mode": "early", "entry_option_price": 97.55, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 21.42, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.625, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.836, "early_reclaim_pct": 74.2, "matched_signals": 37, "recovery_stability_score": 0.625, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T00:00:04.624946-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 93}
2026-07-21T15:10:09.418772-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-21T15:05:04.539660-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-21T15:00:02.487183-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-21T14:55:03.644573-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-07-21T14:50:05.500810-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 16912.5, "asset_type": "option", "contract_symbol": "PYPL260821C00055000", "contracts": 55, "early_entry_score": 0.165, "entry_mode": "regular", "entry_option_price": 3.075, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 6395.0, "option_spread_pct": 4.88, "option_volume": 68.0, "success_rate": 80.0, "ticker": "PYPL", "timing_score": 0.663}
2026-07-21T14:50:05.500810-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-21", "training_samples": 5488, "window": 5}
2026-07-21T11:17:25.409204-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-21T10:59:34.342189-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722100006)

</details>
