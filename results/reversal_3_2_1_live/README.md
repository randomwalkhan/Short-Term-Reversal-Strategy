# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 11:35:04 EDT`
Last processed slot: `manage_1130`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$5,399.49`
- Equity: `$12,153.81`
- Realized PnL: `$2,120.42`
- Unrealized PnL: `$33.39`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   2      9     6720.93                 6754.32       746.77         750.48      746.77        750.48           33.39                    0.5         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  INTC     option         option INTC260529C00068000      9          2026-04-17         2026-04-20        6.775         5.4 -1237.5  -20.295203 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               16            1.25              2.04        232.68                24.45            True
  SBUX           94.59               37            0.63              0.44         99.81                34.23            True
  INTC           94.44               18            3.81              1.83         67.72                74.75            True
   STX           94.29               35            1.45              5.57        545.36                70.39            True
  NVDA           92.00               25            1.29              1.82        200.90                35.90            True
  AVGO           90.48               21            2.11              5.99        403.97                45.93            True
  UPRO           90.00               30            1.15              1.01        124.80                56.64            True
  BKNG           87.50               32            1.28              1.73        191.27                38.41            True
  GILD           87.50               24            0.89              0.86        137.27                20.86            True
  AMAT           86.84               38            0.54              1.51        396.29                56.13            True
  PLTR           86.49               37            1.20              1.23        145.86                63.50            True
  MELI           85.71               42            0.50              6.50       1853.05                35.92            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-20T11:35:04.939359-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-20T11:30:05.954810-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-20T11:25:05.930636-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-20T11:10:06.024388-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-20T11:05:04.134434-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-20T11:00:05.949180-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-20T10:55:05.948674-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-20T10:40:00.901789-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-20T10:35:00.907804-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-20T10:30:01.916831-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420113504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420113504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420113504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420113504)

</details>
