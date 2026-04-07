# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 10:15:05 EDT`
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
- Equity: `$11,020.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$-420.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4760.0                 7.4                   6.8      227.61         225.4          -420.0                  -8.11         100.0               20               0.8         28.89           32.77                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA          100.00               14            3.39              8.38        349.23                42.33            True
   HON          100.00               14            1.23              1.97        227.37                20.19            True
   WDC           97.44               39            0.71              1.50        303.50                83.06            True
  MRVL           95.65               23            2.55              1.96        108.67                70.84            True
  REGN           95.65               23            1.45              7.76        759.71                25.24            True
  COST           93.10               29            0.71              5.04       1016.39                13.04            True
  NVDA           92.00               25            1.37              1.71        176.91                33.70            True
  MPWR           91.43               35            1.04              8.57       1176.36                51.99            True
  CDNS           90.91               44            0.82              1.60        278.71                25.26            True
  UPRO           90.91               22            2.63              1.86         99.94                53.86            True
  FAST           90.00               30            0.80              0.26         45.76                20.98            True
  PCAR           88.24               34            0.82              0.68        118.03                21.97            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-07T10:10:05.890428-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:05:05.888815-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:00:05.892155-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T09:55:05.880017-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T09:40:05.898554-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-07T09:35:05.899056-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-07T09:30:05.896974-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-06T16:00:05.887844-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-06T15:55:05.885666-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-06T15:40:05.890163-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407101505)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407101505)

</details>
