# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 15:30:05 EDT`
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

- Cash: `$160.60`
- Equity: `$55,133.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$357.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 28372.5        30.35          31.52      310.66        313.80          bid_ask_mid                      31.52                bid_ask_mid                    True          1057.5                   3.87         87.50               32              1.06         63.04           63.09                  88.60                 214.0           30.0               0.05                      ok
  MNST     option         option MNST261016C00048000       2026-08-26                   0    140     27300.0                 26600.0         1.95           1.90       48.03         48.15          bid_ask_mid                       1.90                bid_ask_mid                    True          -700.0                  -2.56         85.71               14              1.44         27.42           25.78                 552.32                 249.0           74.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           87.50               16            1.20              0.41         48.55               552.32         1.000          pass              0.406             22.0                           0.484                4.71              0.576                                 ok            True                  False
  ABNB           96.15               26            1.14              1.52        189.85                61.60         0.664          pass              0.623             16.5                           0.181                4.57              0.485                                 ok            True                  False
  SHOP           90.00               30            1.65              1.78        153.12                72.08         0.622          pass              0.532             23.2                           0.184                0.62             -0.150                                 ok            True                  False
   TRI           88.89               27            1.61              1.18        103.88                66.28         0.605          pass              0.562             50.3                           0.337                0.74              0.322                                 ok            True                  False
  MELI           95.24               21            1.78             24.84       1986.35                47.50         0.549          pass              0.609             27.0                           0.492                7.29              0.992                                 ok            True                  False
   KHC           83.33               12            2.05              0.36         25.16                34.81         0.537          pass              0.310             51.4                           0.659                1.10              0.145                                 ok            True                  False
  BKNG           95.24               21            1.77              2.65        212.65                35.36         0.518          pass              0.627             33.9                           0.324               -1.06              0.025                                 ok            True                  False
  CPRT           84.00               25            1.57              0.37         33.17                43.23         0.511          pass              0.304             15.5                           0.215               13.16              1.353                                 ok            True                  False
  VRTX           97.06               34            0.74              2.87        551.62                33.40         0.509          pass              0.700             29.8                           0.251                4.38              0.791                                 ok            True                  False
  VRSK           89.47               38            0.50              0.66        188.21                41.10         0.506          pass              0.702             70.6                           0.526                3.97              0.505                                 ok            True                  False
  ALNY           87.80               41            0.23              0.39        239.91               130.65         0.843          pass              0.746             84.4                           0.380                6.96              0.688                                 ok           False                  False
  AMAT           88.57               35            0.14              0.48        479.84                76.53         0.673          pass              0.736             91.1                           0.671              -12.46             -1.297 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-26T15:10:04.393572-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T15:05:01.392780-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T15:00:04.399840-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T14:55:02.427965-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-08-26T14:50:02.229559-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 27300.0, "asset_type": "option", "contract_symbol": "MNST261016C00048000", "contracts": 140, "early_entry_score": 0.298, "entry_mode": "regular", "entry_option_price": 1.95, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 249.0, "option_spread_pct": 5.13, "option_volume": 74.0, "success_rate": 85.71, "ticker": "MNST", "timing_score": 1.0}
2026-08-26T14:50:02.229559-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-26", "training_samples": 5704, "window": 5}
2026-08-26T12:00:04.193922-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:55:03.284797-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261002C00062000", "current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "entry_ask": 2.68, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.465, "hypothetical_budget": 13730.3, "hypothetical_contracts": 55, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 610.0, "option_spread_pct": 17.44, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.702, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "matched_signals": 35, "recovery_stability_score": 0.702, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-26T11:50:01.099073-04:00 early_entry_1150 early_entry_shadow                                   {"contract_symbol": "PYPL261016C00065000", "current_drop_pct": 0.57, "early_entry_score": 0.788, "early_reclaim_pct": 64.9, "entry_ask": 1.6, "entry_bid": 1.5, "entry_mode": "early", "entry_option_price": 1.55, "hypothetical_budget": 13730.3, "hypothetical_contracts": 88, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 6048.0, "option_spread_pct": 6.45, "option_volume": 584.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.734, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.788, "early_reclaim_pct": 64.9, "matched_signals": 35, "recovery_stability_score": 0.734, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:45:03.275607-04:00 early_entry_1145 early_entry_shadow                                    {"contract_symbol": "PYPL260925C00060000", "current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "entry_ask": 3.45, "entry_bid": 3.15, "entry_mode": "early", "entry_option_price": 3.3, "hypothetical_budget": 13730.3, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 240.0, "option_spread_pct": 9.09, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "matched_signals": 35, "recovery_stability_score": 0.706, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826153005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826153005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826153005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826153005)

</details>
