# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 10:40:05 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$10,915.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$-525.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4655.0                 7.4                  6.65      227.61        225.66          -525.0                 -10.14         100.0               20               0.8         28.89           30.32                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               14            1.14              1.83        227.43                20.19            True
  TSLA          100.00               10            3.69              9.11        348.92                42.33            True
  REGN           96.77               31            1.03              5.52        760.67                25.24            True
  MRVL           96.00               25            2.07              1.59        108.83                70.84            True
  NVDA           95.65               23            1.62              2.01        176.78                33.70            True
  UPRO           92.00               25            2.09              1.48        100.11                53.86            True
  MPWR           91.18               34            1.18              9.75       1175.85                51.99            True
  CDNS           90.91               44            0.78              1.53        278.73                25.26            True
   MAR           90.91               33            0.89              2.12        337.09                25.97            True
  ABNB           90.32               31            1.37              1.22        126.29                36.80            True
  VRTX           88.46               26            1.48              4.51        432.37                40.01            True
  GILD           88.46               26            0.80              0.78        139.79                20.18            True
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

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407104005)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407104005)

</details>
