# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 14:50:01 EDT`
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

- Cash: `$21,916.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ASML     option         option ASML260821C01800000       2026-07-20                   0      1      9495.0                  9495.0        94.95          94.95     1735.72       1737.25          bid_ask_mid                      94.95                bid_ask_mid                    True             0.0                    0.0         94.29               35              0.68         58.71           58.71                  63.09                 214.0           26.0               0.04                      ok
```

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  ASML           94.29               35            0.68              8.30       1744.02                63.09         0.585          pass              0.694             29.4                           0.234               -4.90             -0.203                                 ok            True                  False
  MNST          100.00               11            1.69              1.16         97.00                20.09         0.537          pass              0.509             16.2                           0.404               -1.56              0.109                                 ok            True                  False
  CTAS           80.00               15            1.62              2.32        203.46                36.07         0.533          pass              0.155             22.8                           0.264               12.85              1.512                                 ok            True                  False
  GILD           91.30               23            0.82              0.77        133.95                34.72         0.528          pass              0.498             19.0                           0.273                2.75              0.036                                 ok            True                  False
  PCAR           85.71               28            0.97              0.86        125.83                30.30         0.505          pass              0.373             16.7                           0.228               -0.74              0.101                                 ok            True                  False
  BKNG           85.71               21            1.88              2.39        180.66                41.44         0.504          pass              0.339             21.1                           0.226               -1.52              0.137                                 ok            True                  False
  AMAT           91.18               34            0.27              1.02        529.22                99.49         0.710          pass              0.646             39.1                           0.238              -10.89             -0.776 downtrend_blocked_slope_and_streak           False                  False
  KLAC           84.62               26            1.41              2.10        211.85               107.27         0.703          pass              0.379             26.5                           0.245              -10.10             -0.614 downtrend_blocked_slope_and_streak           False                  False
  AAPL          100.00                3            2.14              5.01        331.59                36.42         0.623          pass              0.549             28.8                           0.485                4.46              0.689                                 ok           False                  False
  LRCX           88.46               26            1.86              4.07        311.56                96.49         0.620          pass              0.476             27.2                           0.188              -12.20             -0.944 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                8            1.24              0.53         60.77                32.63         0.603          pass              0.587             42.4                           0.525                1.82              0.229                                 ok           False                  False
   KDP           85.71               14            1.26              0.27         30.79                36.31         0.589          pass              0.272             11.4                           0.242               -3.87             -0.279            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-20T14:50:01.117820-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"allocated_cash": 9495.0, "asset_type": "option", "contract_symbol": "ASML260821C01800000", "contracts": 1, "early_entry_score": 0.694, "entry_mode": "regular", "entry_option_price": 94.95, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 214.0, "option_spread_pct": 3.9, "option_volume": 26.0, "success_rate": 94.29, "ticker": "ASML", "timing_score": 0.585}
2026-07-20T14:50:01.117820-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-20", "training_samples": 5478, "window": 5}
2026-07-20T12:00:04.096666-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:55:01.102362-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:50:01.110550-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:45:01.103753-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "VRSK260821C00200000", "current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 68.7, "entry_ask": 9.6, "entry_bid": 8.6, "entry_mode": "early", "entry_option_price": 9.1, "hypothetical_budget": 15705.88, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 47.0, "option_spread_pct": 10.99, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.668, "shadow_only": true, "success_rate": 90.24, "ticker": "VRSK", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 68.7, "matched_signals": 41, "recovery_stability_score": 0.668, "success_rate": 90.24, "ticker": "VRSK", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-20T11:40:02.180070-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:35:01.099987-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "VRSK260821C00200000", "current_drop_pct": 0.57, "early_entry_score": 0.695, "early_reclaim_pct": 65.2, "entry_ask": 9.4, "entry_bid": 8.7, "entry_mode": "early", "entry_option_price": 9.05, "hypothetical_budget": 15705.88, "hypothetical_contracts": 17, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 47.0, "option_spread_pct": 7.73, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.692, "shadow_only": true, "success_rate": 89.74, "ticker": "VRSK", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.695, "early_reclaim_pct": 65.2, "matched_signals": 39, "recovery_stability_score": 0.692, "success_rate": 89.74, "ticker": "VRSK", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-20T11:30:02.147951-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:25:05.073932-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720145001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720145001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720145001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720145001)

</details>
