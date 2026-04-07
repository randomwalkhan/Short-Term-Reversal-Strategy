# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 10:50:05 EDT`
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
- Equity: `$10,950.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$-490.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4690.0                 7.4                   6.7      227.61         225.2          -490.0                  -9.46         100.0               20               0.8         28.89           30.66                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               11            1.28              2.05        227.33                20.19            True
  REGN           96.77               31            1.04              5.57        760.65                25.24            True
  MRVL           96.00               25            2.05              1.57        108.84                70.84            True
  NVDA           95.65               23            1.60              1.98        176.79                33.70            True
  FAST           91.43               35            0.64              0.21         45.78                20.98            True
  MPWR           91.18               34            1.21              9.99       1175.75                51.99            True
  CDNS           90.91               44            0.85              1.66        278.68                25.26            True
   MAR           90.91               33            0.88              2.08        337.11                25.97            True
  UPRO           90.91               22            2.40              1.69        100.01                53.86            True
  ABNB           89.29               28            1.46              1.30        126.25                36.80            True
  GILD           88.46               26            0.74              0.72        139.82                20.18            True
  VRTX           88.00               25            1.58              4.81        432.24                40.01            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T10:40:05.892021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:35:05.885837-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:30:05.884012-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:25:05.889349-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:10:05.890428-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:05:05.888815-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:00:05.892155-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T09:55:05.880017-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T09:40:05.898554-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-07T09:35:05.899056-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407105005)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407105005)

</details>
