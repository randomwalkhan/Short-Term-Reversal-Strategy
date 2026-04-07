# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 11:05:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$11,160.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$-280.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4900.0                 7.4                   7.0      227.61        223.65          -280.0                  -5.41         100.0               20               0.8         28.89           33.67                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.14               35            1.49              3.17        302.79                83.06            True
  REGN           95.65               23            1.36              7.24        759.94                25.24            True
  MRVL           95.00               20            3.08              2.36        108.50                70.84            True
  SBUX           94.44               36            0.57              0.38         94.62                40.32            True
  NVDA           94.12               17            2.23              2.77        176.45                33.70            True
  ORLY           89.74               39            0.60              0.38         91.97                23.11            True
  DXCM           88.89               45            0.75              0.33         63.07                29.92            True
  PCAR           88.89               36            0.76              0.63        118.05                21.97            True
  DDOG           88.89               27            2.18              1.78        115.74                49.06            True
  FAST           88.89               27            0.89              0.29         45.75                20.98            True
  MPWR           88.46               26            2.04             16.82       1172.82                51.99            True
  GILD           88.46               26            0.72              0.71        139.83                20.18            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T11:05:05.886675-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:00:05.892871-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:55:05.886961-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:40:05.892021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:35:05.885837-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:30:05.884012-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:25:05.889349-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:10:05.890428-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:05:05.888815-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:00:05.892155-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407110505)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407110505)

</details>
