# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 11:45:04 EDT`
Last processed slot: `manual_refresh`

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
- Chart views: GitHub-native `1D / 1W / 1M`, default open panel is `1W`

## Portfolio Snapshot

- Cash: `$6,260.00`
- Equity: `$10,285.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$-1,155.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4025.0                 7.4                  5.75      227.61        223.03         -1155.0                  -22.3         100.0               20               0.8         28.89           30.69                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  MRVL           96.00               25            2.39              1.83        108.73                70.84            True
  REGN           95.00               20            1.64              8.74        759.29                25.24            True
  SBUX           93.55               31            0.84              0.56         94.54                40.32            True
  NVDA           91.67               24            1.54              1.92        176.82                33.70            True
  MPWR           91.18               34            1.14              9.44       1175.99                51.99            True
  GILD           90.91               11            1.51              1.48        139.49                20.18            True
  CDNS           90.24               41            1.06              2.06        278.51                25.26            True
  UPRO           90.00               20            2.84              2.00         99.88                53.86            True
  ORLY           88.57               35            0.72              0.46         91.93                23.11            True
  PCAR           87.10               31            1.00              0.83        117.96                21.97            True
  ASML           86.67               30            1.21             11.08       1299.26                47.16            True
  CTAS           86.67               30            0.78              0.94        171.29                28.73            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T11:40:05.887766-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-07T11:35:05.890463-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-07T11:30:02.894028-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-07T11:25:05.887847-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-07T11:10:00.929829-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:05:05.886675-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:00:05.892871-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:55:05.886961-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:40:05.892021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:35:05.885837-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407114504)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407114504)

</details>
