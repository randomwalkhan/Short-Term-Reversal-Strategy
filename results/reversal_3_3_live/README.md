# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 14:50:05 EDT`
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

- Cash: `$16,265.50`
- Equity: `$30,858.00`
- Realized PnL: `$20,858.00`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00320000       2026-07-23                   0     13     14592.5                 14592.5        11.22          11.22      320.41        320.16          bid_ask_mid                      11.22                bid_ask_mid                    True             0.0                    0.0          90.0               10              1.68         30.72           30.72                  37.45               25201.0         5101.0               0.02                      ok
```

## Today's Closed Trades (2026-07-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  AAPL     option         option AAPL260821C00325000     15          2026-07-22         2026-07-23       10.850      9.7650 -1627.50       -10.0 stop_loss_hit_at_scan
  PYPL     option         option PYPL260821C00055000     55          2026-07-21         2026-07-23        3.075      2.7675 -1691.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AAPL           90.00               10            1.68              3.84        324.25                37.45         0.624          pass              0.378             16.2                           0.267                1.32              0.352                                 ok            True                  False
  ASML           94.29               35            0.52              6.52       1799.06                56.20         0.592          pass              0.826             72.9                           0.554               -0.65              0.024                                 ok            True                   True
   PEP           85.71               21            0.81              0.77        135.32                30.61         0.577          pass              0.412             42.7                           0.417               -2.40             -0.215                                 ok            True                  False
  MPWR           82.86               35            1.09             10.63       1393.90                64.79         0.544          pass              0.499             67.3                           0.490                0.67              0.247                                 ok            True                  False
  PAYX          100.00               29            0.69              0.53        110.51                34.17         0.533          pass              0.712             44.1                           0.480                3.50              0.420                                 ok            True                  False
   MAR          100.00               12            1.90              4.93        367.69                21.19         0.528          pass              0.543             25.6                           0.315               -2.61             -0.133                                 ok            True                  False
  CTSH           86.11               36            0.85              0.26         43.07                49.36         0.506          pass              0.594             69.1                           0.778               -1.35              0.057                                 ok            True                  False
  SOXL           84.62               26            4.76              5.37        158.69               181.21         0.694          pass              0.397             32.6                           0.351              -20.33             -2.441            downtrend_blocked_slope           False                  False
  LRCX           88.89               36            0.30              0.68        319.00                89.02         0.684          pass              0.747             89.5                           0.604               -9.87             -1.157 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                5            1.88              0.80         60.52                31.72         0.624          pass              0.496             11.2                           0.324                2.43              0.312                                 ok           False                  False
   KDP           88.89                9            1.64              0.35         30.05                36.78         0.612          pass              0.338             13.1                           0.232               -3.30             -0.388 downtrend_blocked_slope_and_streak           False                  False
  ISRG           63.64               11            2.65              6.32        337.98                68.45         0.595          pass              0.143             25.5                           0.424              -19.41             -2.276            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-23T14:50:05.030619-04:00       entry_1500              entry {"allocated_cash": 14592.5, "asset_type": "option", "contract_symbol": "AAPL260821C00320000", "contracts": 13, "early_entry_score": 0.378, "entry_mode": "regular", "entry_option_price": 11.225, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 25201.0, "option_spread_pct": 2.23, "option_volume": 5101.0, "success_rate": 90.0, "ticker": "AAPL", "timing_score": 0.624}
2026-07-23T14:50:05.030619-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-23", "training_samples": 5516, "window": 5}
2026-07-23T12:00:02.078304-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:55:05.041109-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:50:02.063008-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:45:02.073454-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:40:05.071726-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:35:03.088888-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:30:02.112498-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:25:02.129403-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723145005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723145005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723145005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723145005)

</details>
