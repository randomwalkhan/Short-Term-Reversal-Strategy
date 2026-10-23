# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-23 10:30:06 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$140,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-4,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM261120C00230000       2026-10-22                   1     40     71400.0                 67400.0        17.85          16.85      223.97        222.55          bid_ask_mid                      16.85                bid_ask_mid                    True         -4000.0                   -5.6         100.0               38              0.68         80.16           80.19                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           83.33               18            0.90              0.77        120.79                23.20         0.531          pass              0.252             18.8                           0.136                7.79              0.754                                 ok            True                  False
   EXC           82.35               17            0.91              0.29         44.73                20.91         0.526          pass              0.270             35.9                           0.305                6.42              0.573                                 ok            True                  False
   MAR           88.89               18            1.11              3.08        395.48                21.06         0.520          pass              0.421             26.3                           0.216                7.25              0.940                                 ok            True                  False
 CMCSA           89.47               19            0.52              0.08         22.80                23.88         0.513          pass              0.582             72.8                           0.382                9.97              1.061                                 ok            True                  False
  ORLY          100.00               15            1.45              0.93         91.60                17.78         0.513          pass              0.503              6.0                           0.138                4.88              0.608                                 ok            True                  False
   ADP           90.91               22            0.83              1.78        307.18                23.94         0.511          pass              0.614             64.0                           0.322               12.74              1.233                                 ok            True                  False
   AEP           86.36               22            0.73              0.67        130.35                17.81         0.508          pass              0.344             14.7                           0.234                5.59              0.487                                 ok            True                  False
   CEG           85.71               28            1.11              1.99        254.36                65.49         0.604          pass              0.526             64.3                           0.720              -15.33             -1.691 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                1            2.24              1.02         64.75                24.03         0.574          pass              0.489             10.4                           0.215                5.50              0.538                                 ok           False                  False
   KDP           87.50                8            1.76              0.43         35.00                27.06         0.557          pass              0.294             12.7                           0.188                8.85              0.882                                 ok           False                  False
  MSTR           90.24               41            0.12              0.12        145.75                68.96         0.547          pass              0.819             97.0                           0.462               -5.65             -0.512            downtrend_blocked_slope           False                  False
  REGN           77.78                9            2.03             11.67        814.09                31.70         0.546          pass              0.061              2.2                           0.172                7.49              0.821                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-23T10:30:06.026140-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:25:06.029286-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:20:06.283023-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:15:04.978635-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:10:06.503805-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:05:04.082507-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T10:00:04.565947-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-23T00:00:06.660227-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-22T15:10:06.169647-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-22T15:05:02.793544-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261023103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261023103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261023103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261023103006)

</details>
