# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 09:35:01 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$1,114.00`
- Equity: `$58,490.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$787.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 29250.0        30.35          32.50      310.66        310.83     last_price_stale                        NaN                unavailable                   False          1935.0                   7.08         87.50               32              1.06         63.04            0.00                  88.60                 214.0           30.0               0.05                      ok
   KHC     option         option  KHC261016C00025000       2026-08-25                   1    287     29274.0                 28126.0         1.02           0.98       25.19         24.87     last_price_stale                        NaN                unavailable                   False         -1148.0                  -3.92         86.67               15              1.85         24.46            0.78                  37.91                4031.0          107.0               0.04                      ok
```

## Today's Closed Trades (2026-08-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           93.10               29            0.53              0.18         48.65               552.32         1.000          pass              0.665             29.7                           0.276                5.42              0.606                      ok            True                  False
  SHOP           91.43               35            0.94              1.02        153.44                72.08         0.634          pass              0.703             56.2                           0.365                1.34             -0.118                      ok            True                  False
  MRVL           80.00               35            1.43              2.40        239.35                91.37         0.619          pass              0.240              3.9                           0.288                9.15              0.930                      ok            True                  False
  WDAY           80.00               35            1.31              1.78        193.66                76.21         0.606          pass              0.425             65.8                           0.571                9.46              0.313                      ok            True                  False
  DXCM           87.88               33            0.77              0.48         88.95                51.46         0.570          pass              0.595             58.2                           0.489               -2.57             -0.094                      ok            True                  False
   MAR           93.94               33            0.51              1.27        357.23                33.77         0.552          pass              0.628             15.8                           0.292                0.59              0.123                      ok            True                  False
   KHC           87.50               16            1.78              0.31         25.19                34.81         0.534          pass              0.467             57.9                           0.600                1.39              0.158                      ok            True                  False
  REGN          100.00               32            0.59              3.43        832.09                29.20         0.526          pass              0.785             62.0                           0.492                3.96              0.473                      ok            True                  False
  ALNY           88.10               42            0.14              0.23        239.98               130.65         0.844          pass              0.772             90.5                           0.466                7.05              0.692                      ok           False                  False
  SOXL           80.56               36            0.57              0.46        115.66               150.52         0.802          pass              0.508             79.8                           0.722              -18.96             -2.975 downtrend_blocked_slope           False                  False
  DRAM           75.68               37            0.18              0.07         56.15                90.57         0.712          pass              0.515             87.8                           0.803                2.34             -0.131                      ok           False                  False
  INSM           89.13               46            0.44              0.39        123.72               110.58         0.683          pass              0.780             89.4                           0.405               -6.76             -0.444 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                  detail
2026-08-26T00:00:04.646772-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                                           {'saved': 93}
2026-08-25T15:10:01.918364-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T15:05:01.097664-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T15:00:03.828348-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T14:55:05.864506-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped            {"early_entry_score": 0.306, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.47, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.567}
2026-08-25T14:50:01.861538-04:00   entry_1500          timing_overlay                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-25", "training_samples": 5700, "window": 5}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped                                  {"early_entry_score": 0.418, "option_liquidity_status": "low_volume", "option_open_interest": 249.0, "option_spread_pct": 6.9, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MNST", "timing_score": 1.0}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.342, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 85.0, "option_spread_pct": 14.43, "option_volume": 7.0, "reason": "no_trade_low_option_liquidity", "ticker": "DXCM", "timing_score": 0.569}
2026-08-25T14:50:01.861538-04:00   entry_1500 entry_candidate_skipped              {"early_entry_score": 0.471, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 11.32, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "FAST", "timing_score": 0.558}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826093501)

</details>
