# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 14:55:05 EDT`
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

- Cash: `$73,431.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   0     40     71400.0                 71400.0        17.85          17.85      223.97        223.97          bid_ask_mid                      17.85                bid_ask_mid                    True             0.0                    0.0         100.0               38              0.68         80.16           79.74                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM          100.00               38            0.68              1.07        225.04                49.42         0.519            pass              0.816             59.1                           0.295               10.02              0.991                                 ok            True                  False
  MSFT          100.00                6            2.06              7.68        529.66                21.62         0.539            pass              0.463              3.2                           0.186               -0.12             -0.109                                 ok           False                  False
  MELI           72.73               11            2.38             30.85       1841.66                40.26         0.523            pass              0.102             14.3                           0.245               -2.47             -0.238                                 ok           False                  False
  CSCO           62.50                8            2.11              1.59        106.58                31.32         0.517            pass              0.167             38.5                           0.526               -8.61             -1.173 downtrend_blocked_slope_and_streak           False                  False
  QCOM           90.91               11            2.94              3.66        176.39                39.95         0.496 below_threshold              0.385             12.6                           0.252               -1.87             -0.052                                 ok           False                  False
  DXCM          100.00                3            3.13              1.76         79.51                36.58         0.495 below_threshold              0.490             13.6                           0.394               -7.90             -0.503 downtrend_blocked_slope_and_streak           False                  False
   MAR           62.50                8            1.82              5.16        401.79                19.25         0.494 below_threshold              0.121             23.9                           0.199                9.85              1.117                                 ok           False                  False
  NXPI           92.86               28            1.07              1.82        241.58                33.60         0.480 below_threshold              0.702             63.7                           0.614                3.76              0.609                                 ok           False                  False
  DASH           87.50               40            0.90              1.16        183.95                51.42         0.471 below_threshold              0.603             51.9                           0.249               -4.65             -0.454            downtrend_blocked_slope           False                  False
  CRWD           86.05               43            0.55              0.92        238.95                50.83         0.451 below_threshold              0.634             75.9                           0.459               -9.50             -1.686 downtrend_blocked_slope_and_streak           False                  False
   APP           83.33               30            1.91              3.58        266.37                46.80         0.451 below_threshold              0.346             26.2                           0.274               -6.19             -0.404            downtrend_blocked_slope           False                  False
  MCHP           85.71               14            3.21              1.74         76.41                39.64         0.442 below_threshold              0.300             25.5                           0.299               -1.13              0.138                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-22T14:55:05.642488-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-10-22T14:50:05.810841-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"allocated_cash": 71400.0, "asset_type": "option", "contract_symbol": "TEAM261120C00230000", "contracts": 40, "early_entry_score": 0.816, "entry_mode": "regular", "entry_option_price": 17.85, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 7633.0, "option_spread_pct": 10.64, "option_volume": 62.0, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.519}
2026-10-22T14:50:05.810841-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-22", "training_samples": 6173, "window": 5}
2026-10-22T12:00:04.790529-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.63, "early_entry_score": 0.851, "early_reclaim_pct": 78.6, "entry_ask": 1.95, "entry_bid": 1.75, "entry_mode": "early", "entry_option_price": 1.85, "hypothetical_budget": 72415.9, "hypothetical_contracts": 391, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1598.0, "option_spread_pct": 10.81, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.678, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.851, "early_reclaim_pct": 78.6, "matched_signals": 36, "recovery_stability_score": 0.678, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "trend_health_status": "ok"}, {"current_drop_pct": 0.99, "early_entry_score": 0.735, "early_reclaim_pct": 66.4, "matched_signals": 30, "recovery_stability_score": 0.625, "success_rate": 93.33, "ticker": "NXPI", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:55:05.698440-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "entry_ask": 1.3, "entry_bid": 1.15, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 12.24, "option_volume": 356.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "matched_signals": 36, "recovery_stability_score": 0.623, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:50:06.422891-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.63, "early_entry_score": 0.851, "early_reclaim_pct": 78.6, "entry_ask": 2.85, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 2.725, "hypothetical_budget": 72415.9, "hypothetical_contracts": 265, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 5099.0, "option_spread_pct": 9.17, "option_volume": 183.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.637, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.851, "early_reclaim_pct": 78.6, "matched_signals": 36, "recovery_stability_score": 0.637, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:45:04.817612-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "entry_ask": 3.0, "entry_bid": 2.7, "entry_mode": "early", "entry_option_price": 2.85, "hypothetical_budget": 72415.9, "hypothetical_contracts": 254, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 5099.0, "option_spread_pct": 10.53, "option_volume": 173.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "matched_signals": 36, "recovery_stability_score": 0.603, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:40:06.326699-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "FAST261218C00052500", "current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "entry_ask": 2.0, "entry_bid": 1.75, "entry_mode": "early", "entry_option_price": 1.875, "hypothetical_budget": 72415.9, "hypothetical_contracts": 386, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1598.0, "option_spread_pct": 13.33, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.617, "shadow_only": true, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.841, "early_reclaim_pct": 75.3, "matched_signals": 36, "recovery_stability_score": 0.617, "success_rate": 97.22, "ticker": "FAST", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:35:01.699329-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.75, "early_entry_score": 0.831, "early_reclaim_pct": 74.4, "entry_ask": 1.3, "entry_bid": 1.15, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 12.24, "option_volume": 352.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.641, "shadow_only": true, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.75, "early_entry_score": 0.831, "early_reclaim_pct": 74.4, "matched_signals": 35, "recovery_stability_score": 0.641, "success_rate": 97.14, "ticker": "FAST", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-22T11:30:05.774807-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.79, "early_entry_score": 0.815, "early_reclaim_pct": 73.1, "entry_ask": 1.25, "entry_bid": 1.2, "entry_mode": "early", "entry_option_price": 1.225, "hypothetical_budget": 72415.9, "hypothetical_contracts": 591, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 5976.0, "option_spread_pct": 4.08, "option_volume": 349.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.672, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.815, "early_reclaim_pct": 73.1, "matched_signals": 33, "recovery_stability_score": 0.672, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022145505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022145505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022145505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022145505)

</details>
