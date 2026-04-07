# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 11:50:05 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$10,320.00`
- Equity: `$10,320.00`
- Realized PnL: `$320.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-07)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price     pnl  return_pct           exit_reason
   HON HON260515C00230000          2026-04-06         2026-04-07                 7.4                5.8 -1120.0  -21.621622 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  MRVL           96.00               25            2.32              1.78        108.75                70.84            True
  REGN           94.74               19            1.76              9.41        759.01                25.24            True
  SBUX           94.12               34            0.79              0.53         94.55                40.32            True
  NVDA           91.67               24            1.51              1.88        176.83                33.70            True
  MPWR           91.18               34            1.12              9.27       1176.06                51.99            True
  GILD           90.91               11            1.51              1.48        139.50                20.18            True
  CDNS           90.70               43            0.95              1.86        278.59                25.26            True
  UPRO           90.48               21            2.79              1.97         99.90                53.86            True
  COST           90.32               31            0.64              4.53       1016.61                13.04            True
  ORLY           88.57               35            0.72              0.46         91.93                23.11            True
  MDLZ           88.24               17            0.51              0.21         58.29                25.49            True
  ASML           87.10               31            0.97              8.84       1300.22                47.16            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                              detail
2026-04-07T11:50:05.887768-04:00 manage_1200         exit {"contract_symbol": "HON260515C00230000", "pnl": -1120.0, "reason": "stop_loss_hit_at_scan", "return_pct": -21.62, "ticker": "HON"}
2026-04-07T11:40:05.887766-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:35:05.890463-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:30:02.894028-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:25:05.887847-04:00 manage_1130 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:10:00.929829-04:00 manage_1100 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:05:05.886675-04:00 manage_1100 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T11:00:05.892871-04:00 manage_1100 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T10:55:05.886961-04:00 manage_1100 slot_skipped                                                                                                     {"reason": "already_processed"}
2026-04-07T10:40:05.892021-04:00 manage_1030 slot_skipped                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407115005)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407115005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407115005)

</details>
