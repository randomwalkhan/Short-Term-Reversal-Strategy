# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 15:40:07 EDT`
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

- Cash: `$6,573.50`
- Equity: `$12,813.50`
- Realized PnL: `$3,125.50`
- Unrealized PnL: `$-312.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode           instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
 CMCSA     option         option CMCSA260618C00027500       2026-04-27                   0     52      6552.0                  6240.0         1.26            1.2       27.36         27.36          -312.0                  -4.76         91.67               24              0.55         32.42           31.06                  60.91                 871.0           87.0               0.03                      ok
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
  NFLX           90.91               33            0.78              0.50         92.14                45.93            True
  SHOP           93.55               31            1.41              1.24        125.30                57.21            True
   MAR           84.62               13            1.92              4.93        365.04                31.82            True
  AVGO           92.00               25            1.50              4.44        420.86                42.01            True
   WDC           97.22               36            1.28              3.63        402.44                62.15            True
   WMT           83.33               12            1.75              1.60        129.24                25.05            True
  AAPL           84.21               19            1.35              2.57        269.96                26.22            True
  MSTR           82.93               41            0.85              1.01        170.59                71.85            True
  SOXL           80.00               25            4.76              4.28        126.49               109.31            True
  KLAC           83.33               18            2.59             35.11       1919.95                47.17            True
  CSCO           86.36               22            1.08              0.68         88.72                28.51            True
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                           detail
2026-04-27T15:40:07.694980-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:35:07.539962-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:30:04.079813-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:25:07.581352-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:10:04.191055-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:05:07.808930-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:00:08.586913-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T14:55:05.183836-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T14:50:04.672861-04:00  entry_1500          entry {"allocated_cash": 6552.0, "asset_type": "option", "contract_symbol": "CMCSA260618C00027500", "contracts": 52, "entry_option_price": 1.26, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 871.0, "option_spread_pct": 3.17, "option_volume": 87.0, "success_rate": 91.67, "ticker": "CMCSA", "timing_score": 0.589}
2026-04-27T14:50:04.672861-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                     {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-04-27", "training_samples": 5471, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427154007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427154007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427154007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427154007)

</details>
