# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 09:30:05 EDT`
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
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  5320.0                 7.4                   7.6      227.61        225.75           140.0                    2.7         100.0               20               0.8         28.89            1.56                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               16            1.05              1.67        227.49                20.19            True
   WDC           97.44               39            0.78              1.67        303.43                83.06            True
  REGN           97.14               35            0.69              3.71        761.45                25.24            True
  MRVL           96.30               27            1.79              1.37        108.92                70.84            True
  NVDA           92.00               25            1.32              1.64        176.94                33.70            True
  MPWR           91.89               37            0.58              4.79       1177.98                51.99            True
  CDNS           90.91               44            0.71              1.39        278.80                25.26            True
   WMT           90.48               21            1.01              0.90        126.41                17.13            True
  UPRO           90.32               31            1.35              0.95        100.35                53.86            True
  ASML           88.24               34            0.81              7.36       1300.86                47.16            True
   BKR           88.24               34            0.54              0.23         60.60                40.15            True
  PLTR           87.80               41            0.53              0.55        147.69                48.99            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-07T09:30:05.896974-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-06T16:00:05.887844-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-06T15:55:05.885666-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-06T15:40:05.890163-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-06T15:35:05.886061-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-06T15:30:05.882298-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-06T15:25:05.886761-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-06T15:10:05.888760-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-06T15:00:05.880499-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-06T14:55:05.887845-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407093005)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407093005)

</details>
