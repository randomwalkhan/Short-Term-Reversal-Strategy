# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-28 15:40:04 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,922.50`
- Equity: `$14,722.50`
- Realized PnL: `$4,997.50`
- Unrealized PnL: `$-275.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260529C00084000       2026-04-28                   0     10      7075.0                  6800.0         7.08            6.8       84.22         83.95          -275.0                  -3.89         100.0               38              0.91         70.58           68.97                  91.28                 369.0           78.0               0.05                      ok
```

## Today's Closed Trades (2026-04-28)

```text
ticker asset_type execution_mode           instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price         pnl  return_pct                  exit_reason
 CMCSA     option         option CMCSA260618C00027500     52          2026-04-27         2026-04-28         1.26        1.62 1872.000025   28.571429 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               34            1.31              0.78         84.66                91.28            True
  CHTR           91.67               36            0.84              1.03        174.17               113.25            True
  FAST           86.96               23            1.42              0.45         45.09                39.39            True
  PLTR           89.19               37            1.08              1.08        142.64                61.16            True
  UPRO           92.86               28            1.48              1.32        127.02                41.61            True
  SHOP           93.55               31            1.36              1.18        123.72                56.03            True
  SNPS           94.12               17            2.62              9.13        494.63                48.57            True
   CSX           90.00               30            0.57              0.18         45.38                28.49            True
   TXN           79.17               24            1.57              2.97        268.23                67.99           False
   ADI           69.23               13            2.13              5.86        390.08                38.73           False
  META           75.86               29            1.22              5.82        676.13                37.38           False
  TSLA           87.18               39            0.46              1.21        378.04                46.97           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                          detail
2026-04-28T15:40:04.250884-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-04-28T15:35:04.434156-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-04-28T15:30:04.969222-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-04-28T15:25:07.342993-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-04-28T15:10:03.802677-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-04-28T15:05:08.809866-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-04-28T15:00:07.737334-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-04-28T14:55:08.310355-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                 {"reason": "already_processed"}
2026-04-28T14:50:07.517584-04:00  entry_1500          entry {"allocated_cash": 7075.0, "asset_type": "option", "contract_symbol": "INTC260529C00084000", "contracts": 10, "entry_option_price": 7.075, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 369.0, "option_spread_pct": 4.95, "option_volume": 78.0, "success_rate": 100.0, "ticker": "INTC", "timing_score": 0.645}
2026-04-28T14:50:07.517584-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                    {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-04-28", "training_samples": 5496, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260428154004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260428154004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260428154004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260428154004)

</details>
