# Reversal 3.2.1 Live Paper Test

Latest checkpoint (ET): `2026-04-13 23:55:05 EDT`
Last processed slot: `share_ext_2355`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; share-fallback positions also run take-profit and stop-loss scans in after-hours / overnight / pre-market on `5-minute` checkpoints
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours share handling: only share positions participate; fresh extended-hours quotes can trigger take-profit fills at the target price and stop-loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,229.00`
- Equity: `$13,188.00`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$43.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   0      8      5916.0                  5959.0        739.5         744.88       739.5        744.88            43.0                   0.73         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  PLTR     option         option PLTR260522C00125000      5          2026-04-10         2026-04-13        12.06       13.88 910.0   15.091211 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et           slot   event_type                          detail
2026-04-13T23:54:15.718712-04:00 share_ext_2350 slot_skipped {"reason": "already_processed"}
2026-04-13T16:00:05.899443-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-13T15:55:05.891523-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-13T15:40:00.935651-04:00    manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-13T15:35:03.917727-04:00    manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-13T15:30:05.898340-04:00    manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-13T15:25:05.902167-04:00    manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-13T15:10:02.902553-04:00     entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-13T15:05:02.884164-04:00     entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-13T15:00:05.899871-04:00     entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.1 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260413235505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.1 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260413235505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.1 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260413235505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.1 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260413235505)

</details>
