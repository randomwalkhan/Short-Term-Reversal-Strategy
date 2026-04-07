# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 11:30:02 EDT`
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
- Equity: `$10,635.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$-805.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   1          7      5180.0                  4375.0                 7.4                  6.25      227.61        223.03          -805.0                 -15.54         100.0               20               0.8         28.89           32.46                  20.57
```

## Today's Closed Trades (2026-04-07)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  MRVL           96.00               25            2.22              1.70        108.78                70.84            True
  REGN           95.00               20            1.66              8.84        759.25                25.24            True
  SBUX           94.12               34            0.69              0.46         94.58                40.32            True
  MPWR           91.67               36            0.79              6.54       1177.23                51.99            True
  NVDA           91.67               24            1.54              1.92        176.82                33.70            True
  GILD           91.67               12            1.40              1.38        139.54                20.18            True
  UPRO           90.48               21            2.75              1.94         99.91                53.86            True
  COST           90.32               31            0.60              4.29       1016.71                13.04            True
  CDNS           90.00               40            1.16              2.27        278.42                25.26            True
  ORLY           89.74               39            0.64              0.41         91.95                23.11            True
  PCAR           89.19               37            0.71              0.59        118.07                21.97            True
   CSX           88.00               25            0.59              0.17         41.41                24.91            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T11:30:02.894028-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-07T11:25:05.887847-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-07T11:10:00.929829-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:05:05.886675-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T11:00:05.892871-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:55:05.886961-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-07T10:40:05.892021-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:35:05.885837-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:30:05.884012-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-07T10:25:05.889349-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407113002)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407113002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407113002)

</details>
