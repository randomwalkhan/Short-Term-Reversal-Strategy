# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 10:25:04 EDT`
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

- Cash: `$27,460.60`
- Equity: `$54,798.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$22.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 27337.5        30.35          30.38      310.66        308.51          bid_ask_mid                      30.38                bid_ask_mid                    True            22.5                   0.08          87.5               32              1.06         63.04           67.33                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ABNB           93.94               33            0.69              0.92        190.11                61.60         0.649          pass              0.673             27.8                           0.220                5.05              0.506                      ok            True                  False
  SHOP           91.43               35            1.22              1.32        153.32                72.08         0.619          pass              0.663             43.2                           0.365                1.06             -0.130                      ok            True                  False
  WDAY           80.00               35            1.24              1.69        193.69                76.21         0.610          pass              0.430             67.4                           0.640                9.53              0.315                      ok            True                  False
  REGN          100.00               23            0.95              5.55        831.18                29.20         0.562          pass              0.659             38.7                           0.442                3.58              0.456                      ok            True                  False
   KHC           86.36               22            1.22              0.22         25.23                34.81         0.529          pass              0.516             71.1                           0.573                1.96              0.184                      ok            True                  False
  BKNG           96.00               25            1.45              2.17        212.85                35.36         0.519          pass              0.630             26.1                           0.319               -0.74              0.040                      ok            True                  False
  CPRT           86.11               36            0.77              0.18         33.25                43.23         0.502          pass              0.455             22.7                           0.161               14.09              1.390                      ok            True                  False
  MNST           93.75               32            0.45              0.15         48.66               552.32         1.000          pass              0.791             59.2                           0.565                5.50              0.610                      ok           False                  False
  ALNY           88.10               42            0.04              0.07        240.05               130.65         0.847          pass              0.792             97.0                           0.828                7.16              0.697                      ok           False                  False
  SOXL           78.79               33            2.12              1.72        114.93               150.52         0.744          pass              0.288             20.2                           0.173              -20.36             -3.054 downtrend_blocked_slope           False                  False
  DRAM           77.78               36            0.57              0.22         56.14                90.57         0.699          pass              0.434             63.6                           0.366                2.04             -0.144                      ok           False                  False
  INSM           86.49               37            1.15              0.99        123.46               110.58         0.690          pass              0.640             72.7                           0.451               -7.42             -0.477 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                          detail
2026-08-26T10:25:04.269067-04:00 early_entry_1025 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:20:05.153824-04:00 early_entry_1020 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:15:01.106842-04:00 early_entry_1015 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:10:05.242748-04:00 early_entry_1010 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:05:01.196440-04:00 early_entry_1005 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:00:05.932819-04:00 early_entry_1000 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T09:50:01.107222-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "KHC261016C00025000", "fill_price": 0.918, "pnl": -2927.4, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "KHC"}
2026-08-26T00:00:04.646772-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
2026-08-25T15:10:01.918364-04:00       entry_1500       slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-08-25T15:05:01.097664-04:00       entry_1500       slot_skipped                                                                                                                                                 {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826102504)

</details>
