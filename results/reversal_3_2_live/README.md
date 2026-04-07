# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 13:30:05 EDT`
Last processed slot: `manage_1330`

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
  REGN           97.06               34            0.74              3.93        761.36                25.24            True
  COST           95.24               21            0.91              6.49       1015.77                13.04            True
  UPRO           92.86               28            1.46              1.03        100.30                53.86            True
  NVDA           92.00               25            1.28              1.59        176.96                33.70            True
  CDNS           90.91               44            0.70              1.36        278.81                25.26            True
  PCAR           89.19               37            0.70              0.58        118.07                21.97            True
   KDP           88.24               17            0.80              0.14         25.64                20.32            True
  ASML           87.88               33            0.82              7.44       1300.82                47.16            True
  KLAC           87.50               32            1.11             12.01       1534.91                45.70            True
  MDLZ           86.67               15            0.63              0.26         58.27                25.49            True
  MCHP           86.49               37            0.71              0.34         67.08                42.27            True
  ABNB           86.36               22            1.78              1.58        126.13                36.80            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-07T13:30:05.887210-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:25:05.882654-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-07T13:10:04.926634-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T13:05:02.889424-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T13:00:02.895617-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T12:55:00.916656-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-07T12:40:05.895143-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-07T12:35:03.878614-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-07T12:30:00.912059-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-07T12:25:00.895869-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407133005)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407133005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407133005)

</details>
