# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 09:40:05 EDT`
Last processed slot: `manage_0930`

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
- Equity: `$11,580.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$140.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  5320.0                 7.4                   7.6      227.61        224.81           140.0                    2.7         100.0               20               0.8         28.89            1.56                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               10            1.42              2.27        227.24                20.19            True
  MRVL           96.00               25            2.14              1.64        108.81                70.84            True
  REGN           95.00               20            1.54              8.24        759.51                25.24            True
  UPRO           92.59               27            1.77              1.25        100.23                53.86            True
  NVDA           91.67               36            0.77              0.96        177.23                33.70            True
  CDNS           91.11               45            0.65              1.27        278.85                25.26            True
  FAST           90.00               30            0.76              0.24         45.77                20.98            True
  SNPS           88.89               45            0.53              1.47        396.44                35.70            True
  ROST           88.89               18            1.14              1.77        220.45                20.32            True
   BKR           88.24               34            0.60              0.26         60.59                40.15            True
  COST           88.24               34            0.52              3.70       1016.96                13.04            True
  PLTR           87.50               40            0.68              0.71        147.63                48.99            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-07T09:40:05.898554-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-07T09:35:05.899056-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-07T09:30:05.896974-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-06T16:00:05.887844-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-06T15:55:05.885666-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-06T15:40:05.890163-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-06T15:35:05.886061-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-06T15:30:05.882298-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-06T15:25:05.886761-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-06T15:10:05.888760-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407094005)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407094005)

</details>
