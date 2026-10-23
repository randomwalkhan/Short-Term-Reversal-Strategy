# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 15:25:05 EDT`
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

- Cash: `$1,161.80`
- Equity: `$147,316.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$2,485.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   0    657     72270.0                 75555.0         1.10           1.15       44.42         44.49          bid_ask_mid                       1.15                bid_ask_mid                    True          3285.0                   4.55          80.0               15              0.97         20.09           21.09                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 70600.0        17.85          17.65      223.97        224.61          bid_ask_mid                      17.65                bid_ask_mid                    True          -800.0                  -1.12         100.0               38              0.68         80.16           79.25                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           94.12               17            1.04              0.26         35.08                27.06         0.551          pass              0.624             48.6                           0.449                9.65              0.916                                 ok            True                  False
   MAR           81.82               11            1.51              4.20        395.00                21.06         0.531          pass              0.123              4.8                           0.215                6.81              0.922                                 ok            True                  False
   KHC           85.71               21            1.18              0.21         25.00                34.71         0.527          pass              0.413             44.9                           0.653               11.34              1.104                                 ok            True                  False
  COST           80.00               10            1.42             10.14       1013.86                17.03         0.521          pass              0.072              6.7                           0.279                6.00              0.642                                 ok            True                  False
   ADP           91.30               23            0.71              1.53        307.29                23.94         0.513          pass              0.647             69.1                           0.649               12.88              1.239                                 ok            True                  False
   AEP           83.33               18            0.88              0.80        130.30                17.81         0.513          pass              0.324             43.4                           0.653                5.44              0.480                                 ok            True                  False
   EXC           85.71               21            0.81              0.26         44.74                20.91         0.511          pass              0.410             44.3                           0.610                6.53              0.578                                 ok            True                  False
  ORLY          100.00               13            1.64              1.06         91.55                17.78         0.509          pass              0.530             19.7                           0.420                4.67              0.599                                 ok            True                  False
   CEG           83.33               36            0.52              0.92        254.81                65.49         0.590          pass              0.571             83.4                           0.708              -14.82             -1.663 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                1            2.21              1.01         64.76                24.03         0.573          pass              0.517             19.8                           0.503                5.53              0.539                                 ok           False                  False
   STX           73.68               38            0.78              3.51        640.64                72.64         0.545          pass              0.470             76.3                           0.481              -18.63             -1.848 downtrend_blocked_slope_and_streak           False                  False
   XEL           75.00                8            1.21              0.67         78.68                16.59         0.535          pass              0.160             35.6                           0.664                5.73              0.587                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-23T15:10:05.007293-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-23T15:05:06.359707-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-23T15:00:05.816544-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-23T14:55:04.189334-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-23T14:50:05.144728-04:00       entry_1500                   entry {"allocated_cash": 72270.0, "asset_type": "option", "contract_symbol": "EXC261218C00045000", "contracts": 657, "early_entry_score": 0.187, "entry_mode": "regular", "entry_option_price": 1.1, "execution_mode": "option", "matched_signals": 15, "option_liquidity_status": "ok", "option_open_interest": 278.0, "option_spread_pct": 9.09, "option_volume": 48.0, "success_rate": 80.0, "ticker": "EXC", "timing_score": 0.532}
2026-10-23T14:50:05.144728-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                            {"early_entry_score": 0.573, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 3202.0, "option_spread_pct": 23.73, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "KDP", "timing_score": 0.556}
2026-10-23T14:50:05.144728-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-23", "training_samples": 6184, "window": 5}
2026-10-23T12:00:05.040170-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:55:05.962130-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T11:50:05.123171-04:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023152505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023152505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023152505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023152505)

</details>
