# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 15:15:05 EST`
Last processed slot: `manual`

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
- Equity: `$118,324.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$1,300.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  QCOM     option         option QCOM261218C00170000       2026-11-16                   0     52     57850.0                 59150.0        11.12          11.38      170.26        169.68          bid_ask_mid                      11.38                bid_ask_mid                    True          1300.0                   2.25         85.19               27              1.28         54.03            56.8                  68.34                3371.0          163.0               0.02                      ok
```

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   KDP           92.86               14            1.25              0.32         36.20                45.67         0.619          pass              0.431              0.0                           0.150               -2.54              0.033                  ok            True                  False
  QCOM           84.00               25            1.61              1.94        171.64                68.34         0.590          pass              0.380             38.0                           0.368                4.70              0.704                  ok            True                  False
  AAPL          100.00               15            1.30              3.23        354.88                27.52         0.574          pass              0.511              6.9                           0.256                4.02              0.559                  ok            True                  False
  ISRG           88.46               26            1.35              4.20        441.79                45.74         0.559          pass              0.420             10.4                           0.274                0.16             -0.300                  ok            True                  False
  CTAS           94.74               19            1.08              1.72        225.50                28.07         0.558          pass              0.526              5.8                           0.255               -0.21              0.040                  ok            True                  False
  REGN           82.86               35            0.78              5.23        953.23                54.80         0.555          pass              0.298              0.0                           0.204               -1.38              0.051                  ok            True                  False
   CEG           86.21               29            1.83              3.59        278.24                61.55         0.544          pass              0.419             24.1                           0.513                6.76              1.213                  ok            True                  False
  MSFT           96.00               25            1.11              4.08        522.13                36.51         0.542          pass              0.603             16.2                           0.243                2.16             -0.095                  ok            True                  False
  PCAR           80.00               15            1.63              1.22        106.14                30.01         0.525          pass              0.086              0.0                           0.290                2.46              0.400                  ok            True                  False
  PYPL           90.48               21            1.29              0.54         59.05                28.33         0.524          pass              0.405              0.0                           0.286               -0.45             -0.033                  ok            True                  False
  ALNY           50.00               10            3.41              3.93        163.35               110.81         0.705          pass              0.105             11.6                           0.250                0.90              0.091                  ok           False                  False
  IDXX           97.50               40            0.41              2.01        703.37                78.00         0.698          pass              0.696              8.6                           0.181                4.42              0.477                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-16T15:10:06.484281-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:05:04.471128-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T15:00:02.614277-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:55:05.526400-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-16T14:50:05.632368-05:00       entry_1500              entry {"allocated_cash": 57850.0, "asset_type": "option", "contract_symbol": "QCOM261218C00170000", "contracts": 52, "early_entry_score": 0.463, "entry_mode": "regular", "entry_option_price": 11.125, "execution_mode": "option", "matched_signals": 27, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 2.25, "option_volume": 163.0, "success_rate": 85.19, "ticker": "QCOM", "timing_score": 0.599}
2026-11-16T14:50:05.632368-05:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-16", "training_samples": 6252, "window": 5}
2026-11-16T12:00:06.189973-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:55:04.372932-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:50:05.541562-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:45:04.541902-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116151505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116151505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116151505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116151505)

</details>
