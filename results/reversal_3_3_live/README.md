# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 14:50:01 EDT`
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

- Cash: `$13,976.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   KDP     option         option KDP260821C00033000       2026-07-02                   0     96     13920.0                 13920.0         1.45           1.45       33.12          33.1          bid_ask_mid                       1.45                bid_ask_mid                    True             0.0                    0.0         100.0               15              0.76         30.37           30.37                  28.32                2956.0          194.0               0.14                      ok
```

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  UPRO           86.36               22            1.12              1.11        140.91                55.10         0.614          pass              0.470             52.8                           0.615                0.99              0.061                      ok            True                  False
   KDP          100.00               15            0.76              0.18         33.29                28.32         0.609          pass              0.630             45.2                           0.590                7.97              1.073                      ok            True                  False
  ASML           90.00               10            4.38             56.50       1818.83                76.04         0.503          pass              0.362             15.1                           0.418               -5.65             -0.227                      ok            True                  False
  AVGO           69.23               13            2.84              7.34        366.20                71.90         0.626          pass              0.109              8.9                           0.185               -8.52             -0.971 downtrend_blocked_slope           False                  False
   WBD           87.50                8            1.14              0.21         26.72                21.87         0.605          pass              0.401             47.0                           0.575                1.01              0.101                      ok           False                  False
    MU           90.91               11            5.63             40.66       1014.85               134.25         0.595          pass              0.434             25.5                           0.533               -6.61             -0.560 downtrend_blocked_slope           False                  False
   TXN           86.67               15            2.46              5.14        296.21                67.74         0.589          pass              0.335             21.8                           0.339               -3.58             -0.920 downtrend_blocked_slope           False                  False
   ADI           71.43                7            3.38              9.21        385.03                61.24         0.535          pass              0.103             16.7                           0.347               -9.32             -1.290 downtrend_blocked_slope           False                  False
  NXPI           83.33               12            3.06              5.97        276.62                63.41         0.523          pass              0.233             26.2                           0.413               -8.93             -1.388 downtrend_blocked_slope           False                  False
  MPWR           86.67               15            4.04             37.62       1315.61                89.16         0.513          pass              0.330             22.5                           0.428              -11.62             -1.655 downtrend_blocked_slope           False                  False
  PCAR           78.95               19            1.44              1.22        120.72                34.47         0.511          pass              0.209             32.6                           0.549                1.84              0.224                      ok           False                  False
  ODFL           87.18               39            0.29              0.45        217.77                43.21         0.501          pass              0.632             65.6                           0.573               -0.48             -0.093                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-02T14:50:01.813724-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 13920.0, "asset_type": "option", "contract_symbol": "KDP260821C00033000", "contracts": 96, "early_entry_score": 0.63, "entry_mode": "regular", "entry_option_price": 1.45, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 2956.0, "option_spread_pct": 13.79, "option_volume": 194.0, "success_rate": 100.0, "ticker": "KDP", "timing_score": 0.609}
2026-07-02T14:50:01.813724-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"early_entry_score": 0.47, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 22.49, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.614}
2026-07-02T14:50:01.813724-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-02", "training_samples": 5311, "window": 5}
2026-07-02T12:00:01.950437-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:55:04.784699-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:50:04.781471-04:00 early_entry_1150      early_entry_shadow    {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "entry_ask": 14.2, "entry_bid": 13.8, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 2.86, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:45:01.785204-04:00 early_entry_1145      early_entry_shadow   {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.9, "entry_ask": 14.9, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.475, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.87, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.678, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.9, "matched_signals": 44, "recovery_stability_score": 0.678, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:40:01.586831-04:00 early_entry_1140      early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.65, "early_entry_score": 0.824, "early_reclaim_pct": 60.8, "entry_ask": 14.5, "entry_bid": 13.75, "entry_mode": "early", "entry_option_price": 14.125, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.31, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.641, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.824, "early_reclaim_pct": 60.8, "matched_signals": 43, "recovery_stability_score": 0.641, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:35:01.638961-04:00 early_entry_1135      early_entry_shadow     {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.7, "entry_ask": 14.55, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 3.5, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.691, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.7, "matched_signals": 44, "recovery_stability_score": 0.691, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:30:01.731929-04:00 early_entry_1130      early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.66, "early_entry_score": 0.822, "early_reclaim_pct": 60.1, "entry_ask": 15.0, "entry_bid": 13.95, "entry_mode": "early", "entry_option_price": 14.475, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 7.25, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.648, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.822, "early_reclaim_pct": 60.1, "matched_signals": 43, "recovery_stability_score": 0.648, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702145001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702145001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702145001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702145001)

</details>
