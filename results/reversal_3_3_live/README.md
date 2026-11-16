# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 15:05:04 EST`
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

- Cash: `$59,174.80`
- Equity: `$114,814.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$-2,210.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  QCOM     option         option QCOM261218C00170000       2026-11-16                   0     52     57850.0                 55640.0        11.12           10.7      170.26        170.96          bid_ask_mid                       10.7                bid_ask_mid                    True         -2210.0                  -3.82         85.19               27              1.28         54.03           50.61                  68.34                3371.0          163.0               0.02                      ok
```

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   KDP           95.00               20            0.85              0.22         36.25                45.67         0.613          pass              0.528              0.0                           0.150               -2.15              0.051                  ok            True                  False
  QCOM           88.24               34            0.88              1.06        172.02                68.34         0.585          pass              0.637             66.2                           0.521                5.48              0.738                  ok            True                  False
   TXN           80.00               10            2.37              5.03        301.44                58.41         0.582          pass              0.204             48.7                           0.556               -1.86              0.087                  ok            True                  False
  AAPL          100.00               17            1.18              2.94        355.01                27.52         0.569          pass              0.550             15.3                           0.332                4.14              0.564                  ok            True                  False
  CTAS           95.00               20            0.98              1.55        225.57                28.07         0.558          pass              0.548              8.6                           0.248               -0.11              0.045                  ok            True                  False
  ISRG           90.00               30            1.01              3.12        442.25                45.74         0.557          pass              0.556             33.4                           0.421                0.52             -0.284                  ok            True                  False
   CEG           86.21               29            1.79              3.51        278.27                61.55         0.546          pass              0.424             25.8                           0.476                6.81              1.215                  ok            True                  False
  MSFT           96.15               26            0.99              3.64        522.32                36.51         0.543          pass              0.637             25.3                           0.281                2.28             -0.090                  ok            True                  False
  NXPI           92.86               14            2.37              4.40        263.21                48.08         0.531          pass              0.548             41.9                           0.392                0.61              0.308                  ok            True                  False
  ALNY           50.00               10            3.40              3.93        163.36               110.81         0.707          pass              0.092              7.1                           0.224                0.91              0.091                  ok           False                  False
  IDXX           97.73               44            0.21              1.05        703.78                78.00         0.687          pass              0.825             52.2                           0.364                4.63              0.485                  ok           False                  False
  FTNT           76.92               26            2.09              1.86        126.42                93.31         0.669          pass              0.295             40.4                           0.555               -1.31              0.035                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-16T15:05:04.471128-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:00:02.614277-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:55:05.526400-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:50:05.632368-05:00       entry_1500              entry {"allocated_cash": 57850.0, "asset_type": "option", "contract_symbol": "QCOM261218C00170000", "contracts": 52, "early_entry_score": 0.463, "entry_mode": "regular", "entry_option_price": 11.125, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 2.25, "option_volume": 163.0, "success_rate": 85.19, "ticker": "QCOM", "timing_score": 0.599}
2026-11-16T14:50:05.632368-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-16", "training_samples": 6252, "window": 5}
2026-11-16T12:00:06.189973-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:55:04.372932-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:50:05.541562-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:45:04.541902-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:40:05.500831-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116150504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116150504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116150504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116150504)

</details>
