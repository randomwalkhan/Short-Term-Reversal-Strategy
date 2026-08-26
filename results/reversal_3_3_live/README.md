# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 10:35:05 EDT`
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
- Equity: `$54,460.60`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$-315.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 27000.0        30.35           30.0      310.66        310.65          bid_ask_mid                       30.0                bid_ask_mid                    True          -315.0                  -1.15          87.5               32              1.06         63.04           63.33                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ABNB           93.94               33            0.70              0.94        190.10                61.60         0.648          pass              0.668             26.1                           0.209                5.03              0.505                      ok            True                  False
  SHOP           91.18               34            1.38              1.49        153.24                72.08         0.615          pass              0.626             35.6                           0.291                0.89             -0.138                      ok            True                  False
  WDAY           80.65               31            1.78              2.43        193.38                76.21         0.603          pass              0.377             53.2                           0.419                8.93              0.290                      ok            True                  False
  REGN          100.00               17            1.33              7.74        830.24                29.20         0.579          pass              0.548             14.5                           0.278                3.19              0.439                      ok            True                  False
  MELI           96.77               31            1.13             15.85       1990.21                47.50         0.540          pass              0.594              0.0                           0.190                7.99              1.022                      ok            True                  False
   KHC           80.00               10            2.25              0.40         25.15                34.81         0.533          pass              0.193             46.7                           0.306                0.90              0.136                      ok            True                  False
  BKNG           95.65               23            1.62              2.43        212.74                35.36         0.521          pass              0.591             17.3                           0.266               -0.92              0.032                      ok            True                  False
  VRTX           97.22               36            0.57              2.21        551.90                33.40         0.506          pass              0.762             45.9                           0.408                4.56              0.799                      ok            True                  False
  CPRT           84.85               33            0.99              0.23         33.23                43.23         0.505          pass              0.362              9.6                           0.182               13.83              1.380                      ok            True                  False
  MNST           94.12               34            0.35              0.12         48.68               552.32         1.000          pass              0.842             68.5                           0.694                5.61              0.615                      ok           False                  False
  SOXL           80.00               35            1.61              1.30        115.11               150.52         0.760          pass              0.365             40.8                           0.284              -19.94             -3.031 downtrend_blocked_slope           False                  False
  DRAM           77.78               36            0.46              0.18         56.16                90.57         0.705          pass              0.455             70.4                           0.362                2.15             -0.140                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                          detail
2026-08-26T10:35:05.204853-04:00 early_entry_1035 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:30:05.720184-04:00 early_entry_1030 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:25:04.269067-04:00 early_entry_1025 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:20:05.153824-04:00 early_entry_1020 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:15:01.106842-04:00 early_entry_1015 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:10:05.242748-04:00 early_entry_1010 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:05:01.196440-04:00 early_entry_1005 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T10:00:05.932819-04:00 early_entry_1000 early_entry_shadow                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T09:50:01.107222-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "KHC261016C00025000", "fill_price": 0.918, "pnl": -2927.4, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "KHC"}
2026-08-26T00:00:04.646772-04:00     data_refresh       data_refresh                                                                                                                                                                   {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826103505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826103505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826103505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826103505)

</details>
