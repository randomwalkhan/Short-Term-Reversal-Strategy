# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 13:55:00 EDT`
Last processed slot: `manage_1400`

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
  MRVL           97.67               43            0.53              0.41        109.34                70.84            True
  COST           95.24               21            0.92              6.57       1015.73                13.04            True
  NVDA           93.33               30            0.97              1.21        177.12                33.70            True
  UPRO           91.18               34            0.95              0.67        100.45                53.86            True
   LIN           90.00               10            1.46              5.10        497.29                19.02            True
  PCAR           89.47               38            0.62              0.51        118.10                21.97            True
   KDP           89.47               19            0.58              0.11         25.65                20.32            True
  ASML           89.19               37            0.50              4.59       1302.04                47.16            True
  CDNS           89.13               46            0.50              0.99        278.97                25.26            True
  ABNB           88.46               26            1.57              1.39        126.21                36.80            True
  GILD           88.46               26            0.78              0.77        139.80                20.18            True
  ORLY           88.24               34            0.76              0.49         91.92                23.11            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T13:55:00.552170-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-07T13:40:00.942700-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:35:03.883059-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:30:05.887210-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:25:05.882654-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:10:04.926634-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T13:05:02.889424-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T13:00:02.895617-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T12:55:00.916656-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T12:40:05.895143-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407135500)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407135500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407135500)

</details>
