# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 14:50:04 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$6,573.50`
- Equity: `$13,125.50`
- Realized PnL: `$3,125.50`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode           instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
 CMCSA     option         option CMCSA260618C00027500       2026-04-27                   0     52      6552.0                  6552.0         1.26           1.26       27.36         27.35             0.0                    0.0         91.67               24              0.55         32.42           32.42                  60.91                 871.0           87.0               0.03                      ok
```

## Today's Closed Trades (2026-04-27)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct           exit_reason
   TXN     option         option TXN260618C00280000      4          2026-04-24         2026-04-27       14.475      12.175 -920.0  -15.889465 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
 CMCSA           91.67               24            0.55              0.11         27.47                60.91            True
  NFLX           91.89               37            0.63              0.41         92.18                45.93            True
   KDP           83.33               12            1.76              0.36         29.07                32.43            True
   WDC           97.44               39            0.81              2.29        403.02                62.15            True
  SHOP           93.55               31            1.44              1.27        125.29                57.21            True
   WMT           83.33               12            1.77              1.61        129.23                25.05            True
   MAR           83.33               12            2.07              5.31        364.87                31.82            True
  CSCO           81.25               16            1.31              0.82         88.66                28.51            True
  AVGO           91.67               24            1.72              5.10        420.57                42.01            True
  GILD           90.00               10            1.74              1.59        129.72                21.39            True
   TXN           71.43                7            2.93              5.68        274.74                67.06           False
  PLTR           90.24               41            0.09              0.09        143.05                62.14           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                           detail
2026-04-27T14:50:04.672861-04:00  entry_1500          entry {"allocated_cash": 6552.0, "asset_type": "option", "contract_symbol": "CMCSA260618C00027500", "contracts": 52, "entry_option_price": 1.26, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 871.0, "option_spread_pct": 3.17, "option_volume": 87.0, "success_rate": 91.67, "ticker": "CMCSA", "timing_score": 0.589}
2026-04-27T14:50:04.672861-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                     {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-04-27", "training_samples": 5471, "window": 5}
2026-04-27T14:40:03.828346-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T14:35:06.501400-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T14:30:04.508052-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T14:25:02.476196-04:00 manage_1430   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T14:10:01.492312-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T14:05:03.452029-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T14:00:05.386547-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T13:55:01.507336-04:00 manage_1400   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427145004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427145004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427145004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427145004)

</details>
