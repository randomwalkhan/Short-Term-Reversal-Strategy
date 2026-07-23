# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 16:00:03 EDT`
Last processed slot: `manage_1600`

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
- Equity: `$31,378.00`
- Realized PnL: `$20,858.00`
- Unrealized PnL: `$520.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL260821C00320000       2026-07-23                   0     13     14592.5                 15112.5        11.22          11.62      320.41        321.64          bid_ask_mid                      11.62                bid_ask_mid                    True           520.0                   3.56          90.0               10              1.68         30.72           29.57                  37.45               25201.0         5101.0               0.02                      ok
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
  AAPL           93.33               15            1.27              2.89        324.65                37.45         0.621          pass              0.562             36.9                           0.564                1.75              0.371                                 ok            True                  False
   PEP           87.50               24            0.52              0.49        135.44                30.61         0.579          pass              0.542             63.5                           0.602               -2.11             -0.201                                 ok            True                  False
   MAR          100.00               15            1.39              3.61        368.25                21.19         0.541          pass              0.624             45.6                           0.593               -2.10             -0.109                                 ok            True                  False
  SOXL           85.29               34            1.18              1.33        160.42               181.21         0.843          pass              0.635             83.3                           0.694              -17.33             -2.273            downtrend_blocked_slope           False                  False
  MRVL           86.11               36            0.47              0.69        210.69                89.79         0.648          pass              0.652             83.5                           0.658              -13.65             -1.515            downtrend_blocked_slope           False                  False
  MDLZ          100.00                9            1.33              0.57         60.62                31.72         0.633          pass              0.575             37.2                           0.633                3.00              0.337                                 ok           False                  False
   KDP           88.89                9            1.74              0.37         30.04                36.78         0.603          pass              0.353             18.6                           0.246               -3.40             -0.393 downtrend_blocked_slope_and_streak           False                  False
  ISRG           63.64               11            2.54              6.07        338.09                68.45         0.602          pass              0.152             28.5                           0.484              -19.32             -2.271            downtrend_blocked_slope           False                  False
  MPWR           84.62               39            0.09              0.91       1398.06                64.79         0.590          pass              0.667             97.2                           0.755                1.68              0.292                                 ok           False                  False
   KHC          100.00                4            2.31              0.42         25.78                31.13         0.585          pass              0.531             24.1                           0.393                2.76              0.413                                 ok           False                  False
  MNST          100.00                5            2.21              1.48         95.04                21.66         0.545          pass              0.506             17.3                           0.328               -3.10             -0.331            downtrend_blocked_slope           False                  False
   ADP           97.22               36            0.00              0.00        243.12                36.25         0.532          pass              0.927            100.0                           0.806                0.76              0.092                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-07-23T15:10:05.971667-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T15:05:04.134167-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T15:00:04.002554-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T14:55:02.141413-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-07-23T14:50:05.030619-04:00       entry_1500              entry {"allocated_cash": 14592.5, "asset_type": "option", "contract_symbol": "AAPL260821C00320000", "contracts": 13, "early_entry_score": 0.378, "entry_mode": "regular", "entry_option_price": 11.225, "execution_mode": "option", "matched_signals": 10, "option_liquidity_status": "ok", "option_open_interest": 25201.0, "option_spread_pct": 2.23, "option_volume": 5101.0, "success_rate": 90.0, "ticker": "AAPL", "timing_score": 0.624}
2026-07-23T14:50:05.030619-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-23", "training_samples": 5516, "window": 5}
2026-07-23T12:00:02.078304-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:55:05.041109-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:50:02.063008-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:45:02.073454-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723160003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723160003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723160003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723160003)

</details>
