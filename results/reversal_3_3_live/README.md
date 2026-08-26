# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 10:45:02 EDT`
Last processed slot: `early_entry_1045`

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
- Equity: `$53,313.10`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$-1,462.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 25852.5        30.35          28.72      310.66        311.77          bid_ask_mid                      28.72                bid_ask_mid                    True         -1462.5                  -5.35          87.5               32              1.06         63.04            58.9                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           93.10               29            0.51              0.18         48.65               552.32         1.000          pass              0.737             53.6                           0.473                5.44              0.607                      ok            True                  False
  ABNB           93.94               33            0.59              0.79        190.16                61.60         0.654          pass              0.704             37.7                           0.283                5.15              0.510                      ok            True                  False
  SHOP           90.91               33            1.44              1.55        153.22                72.08         0.617          pass              0.605             33.1                           0.245                0.83             -0.141                      ok            True                  False
  WDAY           80.00               30            2.00              2.72        193.25                76.21         0.596          pass              0.336             47.6                           0.354                8.69              0.280                      ok            True                  False
  REGN          100.00               17            1.34              7.82        830.21                29.20         0.578          pass              0.545             13.6                           0.224                3.18              0.438                      ok            True                  False
  MELI           96.77               31            1.12             15.70       1990.27                47.50         0.538          pass              0.651             19.0                           0.242                8.00              1.022                      ok            True                  False
  BKNG           96.00               25            1.47              2.20        212.84                35.36         0.518          pass              0.627             25.1                           0.371               -0.76              0.039                      ok            True                  False
  VRTX           97.22               36            0.52              2.02        551.98                33.40         0.508          pass              0.775             50.4                           0.493                4.61              0.801                      ok            True                  False
  CPRT           83.33               30            1.19              0.28         33.21                43.23         0.507          pass              0.304             10.2                           0.135               13.61              1.371                      ok            True                  False
  ALNY           88.10               42            0.05              0.08        240.05               130.65         0.847          pass              0.791             96.9                           0.813                7.15              0.697                      ok           False                  False
  SOXL           80.00               35            1.06              0.86        115.30               150.52         0.784          pass              0.428             61.0                           0.536              -19.49             -3.005 downtrend_blocked_slope           False                  False
  DRAM           77.78               36            0.29              0.12         56.19                90.57         0.713          pass              0.488             81.2                           0.542                2.33             -0.132                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-26T10:45:02.279556-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:40:01.110768-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:35:05.204853-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:30:05.720184-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:25:04.269067-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:20:05.153824-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:15:01.106842-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:10:05.242748-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:05:01.196440-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:00:05.932819-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826104502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826104502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826104502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826104502)

</details>
