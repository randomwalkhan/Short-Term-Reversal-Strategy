# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 11:10:00 EDT`
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
- Equity: `$11,055.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$-385.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4795.0                 7.4                  6.85      227.61        223.33          -385.0                  -7.43         100.0               20               0.8         28.89           34.14                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.22               36            1.05              2.23        303.19                83.06            True
  REGN           95.65               23            1.42              7.59        759.79                25.24            True
  MRVL           95.00               20            2.90              2.23        108.56                70.84            True
  NVDA           95.00               20            1.92              2.39        176.62                33.70            True
  SBUX           94.44               36            0.60              0.40         94.61                40.32            True
  MPWR           90.00               30            1.61             13.33       1174.32                51.99            True
  PCAR           89.47               38            0.62              0.51        118.10                21.97            True
  DXCM           88.89               45            0.66              0.29         63.09                29.92            True
  DDOG           88.89               27            2.16              1.76        115.74                49.06            True
  FAST           88.46               26            0.95              0.30         45.74                20.98            True
  COST           88.24               34            0.52              3.72       1016.96                13.04            True
  UPRO           88.24               17            3.21              2.26         99.77                53.86            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T11:10:00.929829-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:05:05.886675-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:00:05.892871-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:55:05.886961-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:40:05.892021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:35:05.885837-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:30:05.884012-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:25:05.889349-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:10:05.890428-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:05:05.888815-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407111000)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407111000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407111000)

</details>
