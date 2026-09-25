# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 15:25:06 EDT`
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

- Cash: `$38,003.30`
- Equity: `$73,353.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$-200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261120C00160000       2026-09-25                   0     20     35550.0                 35350.0        17.77          17.68      158.68        159.78          bid_ask_mid                      17.68                bid_ask_mid                    True          -200.0                  -0.56          93.1               29              1.81         73.26           70.83                 109.71                2435.0         2824.0               0.01                      ok
```

## Today's Closed Trades (2026-09-25)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL261030C00145000     16          2026-09-24         2026-09-25       20.275      23.775 5600.0   17.262639 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.12               34            1.14              1.30        161.05               109.71         0.721          pass              0.794             61.7                           0.739               21.98              2.851                      ok            True                   True
  FTNT           84.62               13            2.81              3.51        177.16                58.17         0.566          pass              0.242             14.0                           0.165                9.32              1.050                      ok            True                  False
   TRI           87.50               24            1.89              1.33         99.75                57.78         0.554          pass              0.532             61.1                           0.361                2.84             -0.157                      ok            True                  False
  TEAM          100.00               32            1.53              2.06        191.73                57.21         0.546          pass              0.619              5.9                           0.162                5.62              0.597                      ok            True                  False
  SHOP           84.00               25            1.69              1.71        144.43                62.63         0.527          pass              0.386             42.0                           0.546               10.81              1.307                      ok            True                  False
  INTC           81.25               32            2.09              1.86        126.59                68.53         0.502          pass              0.355             41.5                           0.605               21.17              2.964                      ok            True                  False
  CRWD           79.17               24            2.42              4.40        257.78                96.70         0.683          pass              0.207             15.2                           0.137               21.32              2.041                      ok           False                  False
  PANW           53.85               13            3.65              9.96        385.65                80.20         0.575          pass              0.107              9.9                           0.126               10.99              1.165                      ok           False                  False
   KHC           92.31               13            1.32              0.22         23.77                23.05         0.526          pass              0.452             17.1                           0.319               -3.46             -0.364 downtrend_blocked_slope           False                  False
  NVDA           90.62               32            0.39              0.61        224.32                44.14         0.525          pass              0.601             39.5                           0.265                2.48              0.661                      ok           False                  False
  ADSK           82.50               40            0.36              0.54        211.12                55.76         0.523          pass              0.413             31.3                           0.183               -0.49             -0.261                      ok           False                  False
  WDAY           95.00               40            0.43              0.58        190.74                49.78         0.516          pass              0.909             85.8                           0.656                2.74              0.240                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-09-25T15:10:05.947782-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T15:05:07.061521-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T15:00:05.968673-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T14:55:06.191609-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-09-25T14:50:06.559632-04:00       entry_1500              entry {"allocated_cash": 35550.0, "asset_type": "option", "contract_symbol": "MSTR261120C00160000", "contracts": 20, "early_entry_score": 0.665, "entry_mode": "regular", "entry_option_price": 17.775, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 2435.0, "option_spread_pct": 1.41, "option_volume": 2824.0, "success_rate": 93.1, "ticker": "MSTR", "timing_score": 0.711}
2026-09-25T14:50:06.559632-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-25", "training_samples": 5827, "window": 5}
2026-09-25T12:00:04.925096-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:55:06.011160-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:50:06.515187-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:45:06.706431-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925152506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925152506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925152506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925152506)

</details>
