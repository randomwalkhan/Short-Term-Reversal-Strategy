# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-08 15:05:04 EDT`
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

- Cash: `$16,069.75`
- Equity: `$31,369.75`
- Realized PnL: `$21,794.75`
- Unrealized PnL: `$-425.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-08                   0     17     15725.0                 15300.0         9.25            9.0       97.75         97.87          bid_ask_mid                        9.0                bid_ask_mid                    True          -425.0                   -2.7         93.94               33              1.73         79.38           76.97                  86.36                1396.0           69.0               0.05                      ok
```

## Today's Closed Trades (2026-06-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     16          2026-06-05         2026-06-08         9.85       8.865 -1576.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           93.94               33            1.61              1.12         98.99                86.36         0.631          pass              0.745             52.2                           0.379               14.58              1.808                      ok            True                  False
  PAYX          100.00               13            1.15              0.81        100.18                33.39         0.614          pass              0.605             41.1                           0.375                2.45              0.549                      ok            True                  False
  ROST           91.67               24            1.06              1.70        229.64                43.36         0.597          pass              0.513             16.3                           0.209               -2.93             -0.164                      ok            True                  False
  CRWD           83.33               18            1.97              9.25        667.06                64.90         0.588          pass              0.275             24.6                           0.332                1.48              0.948                      ok            True                  False
  PANW           86.36               22            1.88              3.58        270.52                60.15         0.567          pass              0.405             33.0                           0.371                5.54              1.178                      ok            True                  False
  MSFT           84.62               26            0.97              2.83        415.46                34.82         0.551          pass              0.435             50.1                           0.652               -1.42              0.125                      ok            True                  False
  AMGN           90.00               10            1.21              2.96        348.31                22.27         0.539          pass              0.538             72.5                           0.586                1.78              0.301                      ok            True                  False
   ADP           96.15               26            1.03              1.67        231.23                32.55         0.518          pass              0.692             44.6                           0.338                1.89              0.593                      ok            True                  False
  ADBE           80.77               26            1.84              3.24        250.05                48.16         0.513          pass              0.308             43.0                           0.529                0.84              0.642                      ok            True                  False
  DASH           89.29               28            1.73              1.90        155.98                51.66         0.510          pass              0.569             50.1                           0.472               -3.26             -0.096                      ok            True                  False
  FAST           91.67               24            0.93              0.30         46.66                21.36         0.504          pass              0.577             40.9                           0.418                5.50              0.696                      ok            True                  False
    ZS           80.56               36            0.75              0.69        130.48               157.69         0.896          pass              0.481             67.6                           0.390              -28.83             -2.391 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-08T15:05:04.798011-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T15:00:02.588621-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T14:55:02.835387-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T14:50:04.804691-04:00       entry_1500              entry {"allocated_cash": 15725.0, "asset_type": "option", "contract_symbol": "TEAM260717C00100000", "contracts": 17, "early_entry_score": 0.733, "entry_mode": "regular", "entry_option_price": 9.25, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1396.0, "option_spread_pct": 5.41, "option_volume": 69.0, "success_rate": 93.94, "ticker": "TEAM", "timing_score": 0.623}
2026-06-08T14:50:04.804691-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-08", "training_samples": 5231, "window": 5}
2026-06-08T12:35:06.508215-04:00      manage_1230               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.865, "pnl": -1576.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-08T12:00:05.977560-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:55:06.347594-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:50:04.863668-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:45:02.732022-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260608150504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260608150504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260608150504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260608150504)

</details>
