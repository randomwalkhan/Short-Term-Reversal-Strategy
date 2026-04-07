# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 11:00:05 EDT`
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
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4690.0                 7.4                   6.7      227.61        224.15          -490.0                  -9.46         100.0               20               0.8         28.89           32.23                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.30               37            0.86              1.82        303.37                83.06            True
  REGN           95.65               23            1.45              7.74        759.72                25.24            True
  MRVL           95.00               20            2.85              2.18        108.57                70.84            True
  NVDA           94.44               18            2.03              2.52        176.56                33.70            True
  FAST           90.00               30            0.83              0.27         45.76                20.98            True
  UPRO           90.00               20            3.07              2.16         99.81                53.86            True
  ORLY           89.74               39            0.60              0.38         91.97                23.11            True
  MPWR           89.29               28            1.85             15.32       1173.47                51.99            True
  DXCM           89.13               46            0.52              0.23         63.11                29.92            True
  DDOG           88.89               27            1.86              1.52        115.85                49.06            True
   CSX           88.89               27            0.54              0.16         41.41                24.91            True
  CDNS           88.57               35            1.46              2.86        278.17                25.26            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T11:00:05.892871-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:55:05.886961-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:40:05.892021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:35:05.885837-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:30:05.884012-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:25:05.889349-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:10:05.890428-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:05:05.888815-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T10:00:05.892155-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-07T09:55:05.880017-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407110005)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407110005)

</details>
