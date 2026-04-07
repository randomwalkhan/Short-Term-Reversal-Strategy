# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-07 16:00:01 EDT`
Last processed slot: `manage_1600`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$5,640.00`
- Equity: `$10,305.00`
- Realized PnL: `$320.00`
- Unrealized PnL: `$410.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  TSLA TSLA260515C00340000       2026-04-07                   0          2      4680.0                  5090.0                23.4                 25.45      340.83        347.65           410.0                   8.76         100.0               13               3.4         51.95           49.34                  42.33
```

## Today's Closed Trades (2026-04-07)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price     pnl  return_pct           exit_reason
   HON HON260515C00230000          2026-04-06         2026-04-07                 7.4                5.8 -1120.0  -21.621622 stop_loss_hit_at_scan
```

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T16:00:01.902913-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-07T15:55:05.888167-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-07T15:40:05.893189-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-07T15:35:04.883314-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-07T15:30:03.886489-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-07T15:25:00.886285-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-07T15:10:03.881676-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-07T15:05:00.890479-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-07T15:00:05.890204-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-07T14:55:00.887138-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260407160001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407160001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407160001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407160001)

</details>
