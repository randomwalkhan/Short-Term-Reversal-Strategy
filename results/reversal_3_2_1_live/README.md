# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 12:35:02 EDT`
Last processed slot: `manage_1230`

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
- Equity: `$12,149.55`
- Realized PnL: `$2,120.42`
- Unrealized PnL: `$29.13`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   2      9     6720.93                 6750.06       746.77         750.01      746.77        750.01           29.13                   0.43         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  INTC     option         option INTC260529C00068000      9          2026-04-17         2026-04-20        6.775         5.4 -1237.5  -20.295203 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               11            1.51              2.47        232.49                24.45            True
  INTC           94.44               18            3.81              1.83         67.72                74.75            True
   STX           94.29               35            1.27              4.86        545.67                70.39            True
  SBUX           94.29               35            0.74              0.52         99.78                34.23            True
  NVDA           92.59               27            1.12              1.59        201.00                35.90            True
  ORLY           90.70               43            0.55              0.36         93.55                22.78            True
  UPRO           90.62               32            0.99              0.87        124.86                56.64            True
  AVGO           90.48               21            2.08              5.91        404.01                45.93            True
  FAST           90.32               31            0.73              0.23         45.68                38.81            True
  VRTX           90.00               40            0.51              1.57        440.53                26.94            True
  BKNG           88.89               36            1.05              1.41        191.41                38.41            True
  GILD           88.89               27            0.75              0.72        137.33                20.86            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-20T12:35:02.934530-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-20T12:30:03.948088-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-20T12:25:01.938674-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-20T12:10:05.422263-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-20T12:05:02.935642-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-20T12:00:02.937779-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-20T11:55:05.931999-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-20T11:40:02.972371-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-20T11:35:04.939359-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-20T11:30:05.954810-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420123502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420123502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420123502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420123502)

</details>
