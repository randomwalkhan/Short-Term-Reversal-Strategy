# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 11:25:05 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$10,880.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$-560.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4620.0                 7.4                   6.6      227.61        223.29          -560.0                 -10.81         100.0               20               0.8         28.89           32.78                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.56               41            0.50              1.07        303.69                83.06            True
  MRVL           96.00               25            2.31              1.77        108.75                70.84            True
  REGN           94.74               19            1.82              9.70        758.88                25.24            True
  SBUX           94.12               34            0.72              0.48         94.58                40.32            True
  NVDA           91.67               24            1.56              1.94        176.81                33.70            True
  GILD           90.91               11            1.47              1.44        139.51                20.18            True
  UPRO           90.48               21            2.75              1.94         99.91                53.86            True
  MPWR           90.32               31            1.44             11.90       1174.93                51.99            True
  COST           90.32               31            0.68              4.87       1016.46                13.04            True
  CDNS           90.00               40            1.16              2.26        278.42                25.26            True
  PCAR           89.19               37            0.70              0.58        118.07                21.97            True
  DDOG           88.89               27            2.00              1.63        115.80                49.06            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T11:25:05.887847-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-07T11:10:00.929829-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:05:05.886675-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:00:05.892871-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:55:05.886961-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:40:05.892021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:35:05.885837-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:30:05.884012-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:25:05.889349-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:10:05.890428-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407112505)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407112505)

</details>
